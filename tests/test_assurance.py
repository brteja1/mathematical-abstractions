"""Admission regressions; compiler-backed cases are enabled by test-assurance."""
import copy
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import assurance as A


class LedgerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in ('spec.md', 'Counter.lean', 'checks.py', 'toolchain.json'):
            shutil.copy2(ROOT / 'examples/assurance-counter' / name, self.root / name)
        self.ledger = self.root / 'ledger.json'
        self.doc = json.loads((ROOT / 'examples/assurance-counter/ledger.json').read_text())
        self.doc['obligations'] = self.doc['obligations'][:1]
        self.doc['requirements'] = self.doc['requirements'][:1]
        obligation = self.doc['obligations'][0]
        obligation['evidenceRequired'] = ['test']
        obligation['checks'] = [{'id':'oracle','kind':'test','scope':'R1 fixture source is unchanged',
            'argv':[sys.executable, 'checks.py']}]
        # This fixture exercises receipt mechanics, not actual-source proof efficacy.
        (self.root / 'checks.py').write_text(
            "from pathlib import Path\nassert 'n + 1 else n' in Path('Counter.lean').read_text()\n")
        self.save()

    def save(self):
        self.ledger.write_text(json.dumps(self.doc))

    def run_check(self):
        self.save()
        return A.run_check(self.doc, self.root, self.ledger, 'O1', 'oracle')

    def assess(self):
        return A.assess(self.doc, self.root, self.ledger)

    def test_missing_pass_failure_overwrites_and_source_staleness(self):
        self.assertEqual(self.assess()['checks'][0]['status'], 'missing')
        self.assertEqual(self.run_check()['exitCode'], 0)
        self.assertTrue(self.assess()['admitted'])
        path = self.root / 'Counter.lean'
        path.write_text(path.read_text().replace('n + 1 else n', 'n + 2 else n'))
        self.assertEqual(self.assess()['checks'][0]['status'], 'stale')
        self.assertNotEqual(self.run_check()['exitCode'], 0)
        self.assertEqual(self.assess()['checks'][0]['status'], 'failed')

    def test_contract_catalog_helpers_environment_and_new_files_invalidate(self):
        self.run_check()
        original = copy.deepcopy(self.doc)
        self.doc['obligations'][0]['statement'] += ' changed'
        self.assertEqual(self.assess()['checks'][0]['status'], 'stale')
        self.doc = original
        # Catalog mutation is simulated at the query boundary, never in graph storage.
        real = A.catalog_record
        def changed(ident):
            record = real(ident); record['definition'] += ' edited'; return record
        with patch.object(A, 'catalog_record', changed):
            self.assertEqual(self.assess()['checks'][0]['status'], 'stale')
        for name in ('toolchain.json', 'checks.py'):
            path = self.root / name
            contents = path.read_text(); path.write_text(contents + '\n')
            self.assertEqual(self.assess()['checks'][0]['status'], 'stale')
            path.write_text(contents)
        (self.root / 'new-config.txt').write_text('new input')
        self.assertEqual(self.assess()['checks'][0]['status'], 'stale')

    def test_changed_inputs_during_run_are_failure(self):
        (self.root / 'checks.py').write_text(
            "from pathlib import Path\np=Path('Counter.lean'); p.write_text(p.read_text()+chr(10))\n")
        report = self.run_check()
        self.assertNotEqual(report['exitCode'], 0)
        self.assertIn('Inputs changed during verification', report['output'])

    def test_changed_ledger_during_run_is_failure(self):
        (self.root / 'checks.py').write_text(
            "import json\nfrom pathlib import Path\np=Path('ledger.json')\nd=json.loads(p.read_text())\n"
            "d['obligations'][0]['statement']+=' edited'\np.write_text(json.dumps(d))\n")
        self.assertNotEqual(self.run_check()['exitCode'], 0)

    def test_pending_decisions_and_orphan_requirements_block(self):
        self.run_check()
        self.doc['requirements'][0]['validation']['status'] = 'pending'
        self.assertFalse(self.assess()['admitted'])
        self.doc['requirements'][0]['validation']['status'] = 'accepted'
        self.doc['decisions'] = ['Resolve numeric domain']
        self.assertIn('Unresolved decisions', self.assess()['blockers'])
        self.doc['requirements'].append(dict(self.doc['requirements'][0], id='R3'))
        with self.assertRaisesRegex(ValueError, 'Orphan requirements'):
            A.validate(self.doc, self.root)

    def test_schema_rejects_cycles_unmapped_artifacts_and_fake_proof(self):
        original = copy.deepcopy(self.doc)
        self.doc['obligations'][0]['dependsOn'] = ['O1']
        with self.assertRaisesRegex(ValueError, 'cycle'):
            A.validate(self.doc, self.root)
        self.doc = copy.deepcopy(original)
        self.doc['artifacts'].append({'id':'unmapped','role':'implementation','path':'extra.py'})
        (self.root / 'extra.py').write_text('')
        with self.assertRaisesRegex(ValueError, 'Unmapped normative'):
            A.validate(self.doc, self.root)
        self.doc = original
        self.doc['obligations'][0]['checks'][0]['kind'] = 'proof'
        self.doc['obligations'][0]['evidenceRequired'] = ['proof']
        with self.assertRaisesRegex(ValueError, 'supported lean-source-v1'):
            A.validate(self.doc, self.root)

    def test_paths_symlinks_and_timeout(self):
        self.doc['artifacts'][0]['path'] = '../escape'
        with self.assertRaisesRegex(ValueError, 'escapes'):
            A.validate(self.doc, self.root)
        (self.root / 'link').symlink_to('/tmp')
        with self.assertRaisesRegex(ValueError, 'symlinks'):
            A.inventory(self.root, self.ledger)
        code, output = A.process([sys.executable, '-c', 'import time; time.sleep(2)'], self.root, 0.05)
        self.assertEqual(code, 124)
        self.assertIn('TIMEOUT', output)

    def test_malformed_evidence_fails_closed(self):
        self.run_check()
        path = self.root / '.assurance' / (A.digest(['O1','oracle']) + '.json')
        path.write_text('[]')
        with self.assertRaisesRegex(ValueError, 'Evidence report must be a record'):
            self.assess()

    def test_dependency_closure_and_conservative_fallback(self):
        self.doc['artifacts'].append({'id':'other','path':'other.py','role':'implementation'})
        (self.root / 'other.py').write_text('first')
        other = copy.deepcopy(self.doc['obligations'][0])
        other.update(id='O2', artifacts=['brief','other'])
        self.doc['obligations'].append(other)
        before = A.snapshot(self.doc,self.root,self.ledger,'O1')
        (self.root / 'other.py').write_text('second')
        self.assertEqual(before, A.snapshot(self.doc,self.root,self.ledger,'O1'))
        self.doc['obligations'][0]['dependsOn'] = ['O2']
        before = A.snapshot(self.doc,self.root,self.ledger,'O1')
        (self.root / 'other.py').write_text('third')
        self.assertNotEqual(before, A.snapshot(self.doc,self.root,self.ledger,'O1'))
        self.doc['obligations'][0]['dependsOn'] = []
        self.doc['dependencyGraphComplete'] = False
        before = A.snapshot(self.doc,self.root,self.ledger,'O1')
        (self.root / 'other.py').write_text('fourth')
        self.assertNotEqual(before, A.snapshot(self.doc,self.root,self.ledger,'O1'))

    def test_contradiction_and_missing_outcomes_need_semantic_checks(self):
        # Exhaustive finite relation checker: input 1 is required even when no
        # result is permitted. Merely finding some satisfying input is inadequate.
        checker = """from itertools import product
inputs = (0, 1)
outputs = (0, 1)
mode = open('contract.txt').read().strip()
def allowed(i, o):
    if mode == 'contradiction': return o == 0 and o == 1
    if mode == 'missing': return i == 0 and o == 0
    return o == i
assert all(any(allowed(i, o) for o in outputs) for i in inputs), 'required input without outcome'
"""
        (self.root / 'checks.py').write_text(checker)
        path = self.root / 'contract.txt'
        for mode, expected in [('sound',0),('contradiction',1),('missing',1)]:
            path.write_text(mode)
            self.assertEqual(self.run_check()['exitCode'], expected)
        self.assertFalse(self.assess()['admitted'])


@unittest.skipUnless(os.environ.get('CATALOG_TEST_ASSURANCE') == '1', 'requires pinned Lean runtime')
class ActualSourceProofTests(unittest.TestCase):
    def test_actual_source_proof_mutants_and_full_pilot(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / 'pilot'
            shutil.copytree(ROOT / 'examples/assurance-counter', root,
                            ignore=shutil.ignore_patterns('.assurance','__pycache__'))
            ledger = root / 'ledger.json'
            doc = json.loads(ledger.read_text())
            for obligation in doc['obligations']:
                obligation['checks'][1]['argv'] = [sys.executable,'checks.py',str(ROOT)]
            ledger.write_text(json.dumps(doc))
            for obligation in doc['obligations']:
                for check in obligation['checks']:
                    report = A.run_check(doc,root,ledger,obligation['id'],check['id'])
                    self.assertEqual(report['exitCode'],0,report['output'])
            self.assertTrue(A.assess(doc,root,ledger)['admitted'])
            source = root / 'Counter.lean'
            correct = source.read_text()
            source.write_text(correct.replace('n + 1 else n','n + 2 else n'))
            self.assertTrue(all(c['status']=='stale' for c in A.assess(doc,root,ledger)['checks']))
            report = A.run_check(doc,root,ledger,'O1','lean')
            self.assertNotEqual(report['exitCode'],0,report['output'])
            # The expected type must match, not just any theorem that compiles.
            source.write_text(correct)
            doc['obligations'][0]['checks'][0]['expectedType'] = 'True'
            ledger.write_text(json.dumps(doc))
            report = A.run_check(doc,root,ledger,'O1','lean')
            self.assertNotEqual(report['exitCode'],0,report['output'])
            doc['obligations'][0]['checks'][0]['expectedType'] = '∀ limit n, Counter.allowed limit n (Counter.bump limit n)'
            ledger.write_text(json.dumps(doc))
            start = correct.index('theorem refines')
            end = correct.index('theorem bounded')
            for replacement in [
                'theorem refines : ∀ limit n, allowed limit n (bump limit n) := by sorry\n\n',
                'axiom refines : ∀ limit n, allowed limit n (bump limit n)\n\n']:
                source.write_text(correct[:start]+replacement+correct[end:])
                report = A.run_check(doc,root,ledger,'O1','lean')
                self.assertNotEqual(report['exitCode'],0,report['output'])
                self.assertFalse(A.assess(doc,root,ledger)['admitted'])


if __name__ == '__main__':
    unittest.main()
