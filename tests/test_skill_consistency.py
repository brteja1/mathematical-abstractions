"""Regression evidence for declared policy semantics and review drift boundaries."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('skill_consistency', ROOT / 'scripts/check_skill_consistency.py')
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class SkillConsistencyTests(unittest.TestCase):
    def setUp(self):
        self.contract = json.loads((ROOT / checker.CONTRACT).read_text())

    def policy_errors(self, formula):
        self.contract['rules'].append({'id': 'MUTANT', 'clauses': ['SCOPE'], 'formula': formula})
        return checker.check_policy(self.contract)[0]

    def test_reviewed_repository(self):
        result = checker.check_repository()
        self.assertTrue(result['ok'], result['errors'])
        self.assertEqual(result['inputContexts'], 1024)
        self.assertEqual(result['valuations'], 32768)

    def test_unconditional_ledger_conflicts_with_standalone_scope(self):
        errors = self.policy_errors('requireLedger')
        self.assertTrue(any('no permitted outcome' in e for e in errors))

    def test_unconditional_writes_conflict_with_authorization(self):
        self.assertTrue(self.policy_errors('writeImplementation'))

    def test_removed_proof_guard_fails_negative_scenarios(self):
        self.contract['rules'] = [r for r in self.contract['rules'] if r['id'] != 'P4']
        errors, _ = checker.check_policy(self.contract)
        self.assertIn('scenario not entailed: unsupported-external-proof', errors)
        self.assertIn('scenario not entailed: stale-supported-proof', errors)

    def test_no_proofs_ever_is_not_accepted_vacuously(self):
        errors = self.policy_errors({'not': 'admitSourceProof'})
        self.assertIn('required outcome unavailable: fresh-supported-proof', errors)

    def test_unknown_atoms_and_malformed_formulas_are_rejected(self):
        for expr in ['unmapped', {'implies': [True]}, {'exec': []}]:
            with self.subTest(expr=expr), self.assertRaises(ValueError):
                checker.validate_expr(expr, self.contract['inputs'] + self.contract['outputs'])

    def fixture(self, directory):
        root = Path(directory)
        for source in self.contract['sourceHashes']:
            path = root / source
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes((ROOT / source).read_bytes())
        # Link targets outside the normative skill tree need existence only.
        for source in checker.skill_sources(ROOT) | {'AGENTS.md'}:
            text = (ROOT / source).read_text()
            for destination in checker.re.findall(r'\[[^\]\n]+\]\(([^)\s]+)\)', text):
                dest = checker.urlsplit(destination.strip('<>'))
                if dest.scheme or not dest.path:
                    continue
                target = (root / source).parent / checker.unquote(dest.path)
                target = target.resolve()
                if target.is_relative_to(root) and not target.exists():
                    original = ROOT / target.relative_to(root)
                    if original.is_dir():
                        target.mkdir(parents=True, exist_ok=True)
                    else:
                        target.parent.mkdir(parents=True, exist_ok=True)
                        target.touch()
        return root

    def test_source_changes_need_review(self):
        with tempfile.TemporaryDirectory() as directory:
            root = self.fixture(directory)
            self.assertTrue(checker.check_repository(root, self.contract)['ok'])
            source = root / 'ai/skills/assurance-review/SKILL.md'
            source.write_text(source.read_text() + '\nChanged policy.\n')
            self.assertIn('review stale: ai/skills/assurance-review/SKILL.md', checker.check_repository(root, self.contract)['errors'])

    def test_broken_link_and_missing_skill_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = self.fixture(directory)
            source = root / 'ai/skills/assurance-review/SKILL.md'
            source.write_text(source.read_text() + '\n[absent](missing-policy.md)\n')
            result = checker.check_repository(root, self.contract)
            self.assertTrue(any('broken local link' in e for e in result['errors']))
            source.unlink()
            self.assertIn('skill inventory differs from reviewed contract', checker.check_repository(root, self.contract)['errors'])

    def test_disconnected_handoff_is_rejected(self):
        self.contract['handoffs'] = [h for h in self.contract['handoffs'] if 'abstraction-discovery' not in (h['from'], h['to'])]
        self.assertIn('skill missing from reviewed handoff graph', checker.check_repository(ROOT, self.contract)['errors'])

    def test_bounded_mutex_example_checks_safety_and_finds_mutant(self):
        path = ROOT / 'ai/skills/formal-model-checking/references/mutex-tla-example.md'
        code = path.read_text().split('```python\n', 1)[1].split('```', 1)[0]
        namespace = {'__name__': 'skill_example'}
        exec(compile(code, str(path), 'exec'), namespace)
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            self.assertTrue(namespace['model_check'](['P1', 'P2'], max_ticket_bound=3))
            self.assertFalse(namespace['model_check'](['P1', 'P2'], max_ticket_bound=3, inject_bug=True))
        self.assertIn('liveness/deadlock unchecked', output.getvalue())
        self.assertIn('SAFETY VIOLATION FOUND', output.getvalue())


if __name__ == '__main__':
    unittest.main()
