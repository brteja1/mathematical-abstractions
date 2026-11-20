"""DT-1 protocol tests; synthetic adapters/labels are not AI accuracy evidence."""
from contextlib import redirect_stderr
import copy
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import triage_duplicates as triage
from audit_duplicates import Audit, AuditError, Snapshot, canon, digest
from test_audit_duplicates import fixture, concept, write_page


def proposal(body, decision='distinct'):
    evidence = []
    for ident in body['pair']:
        n = body['records'][ident]
        field = 'definition' if n['type'] == 'Concept' else 'formalStatement'
        evidence.append({'recordId': ident, 'field': field, 'quote': n[field]})
    return {'decision': decision, 'rationale': 'Synthetic protocol result, not a mathematical judgment.',
            'mapping': {k: 'Synthetic explicit mapping.' for k in ('carriers', 'equality', 'operations', 'assumptions')},
            'differences': ['Synthetic test distinction.'], 'missingContext': [], 'evidence': evidence}


class TriageTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name); fixture(self.root)
        self.snapshot = Snapshot(self.root)
        self.workspace = triage.Workspace(self.root / 'experiment', self.snapshot, create=True)
        self.plan = triage.prepare(self.workspace, self.snapshot, limit=4, threshold=0)
        self.engine = Audit(self.snapshot)
        self.config = triage.reviewer_config('synthetic-adapter', '1', kind='synthetic-fixture')

    def bundle(self, count=1, decisions=None, config=None):
        entries = []
        for i, row in enumerate(self.plan['pairs'][:count]):
            key, body = triage.packet(self.workspace, self.engine, row)
            entries.append({'pair': row['pair'], 'packetKey': key,
                            'result': proposal(body, decisions[i] if decisions else 'distinct')})
        return {'schemaVersion': 1, 'reviews': entries}

    def test_selection_and_report_partition(self):
        """T-01/05, DT-01/08; FiniteSet extensionality: counts retain selected and excluded domains."""
        self.assertEqual(self.plan['scope']['actionableCount'], 18)
        self.assertEqual(self.plan['scope']['selectedCount'], 4)
        triage.import_reviews(self.workspace, self.plan, self.engine, self.config, self.bundle(1))
        report = triage.build_report(self.workspace, self.plan, self.engine)
        self.assertEqual(report['counts']['reviewed'], 1)
        self.assertEqual(report['counts']['pending'], 3)
        self.assertEqual(report['scope']['notSelectedCount'], 14)
        self.assertEqual(report['counts']['automaticallySuppressed'], 0)
        text = (self.workspace.path / 'report.md').read_text()
        self.assertIn('<details>', text)
        self.assertIn('14 additional candidates were not selected', text)
        self.assertIn('not accepted or suppressed', text)

    def test_capsules_are_reused_and_preserve_source_semantics(self):
        """T-02, DT-02/03; finite exact source sets preserve scope and do not preload Lean proof text."""
        ident = self.plan['pairs'][0]['pair'][0]
        first = triage.capsule(self.workspace, self.engine, ident)
        files = list((self.workspace.path / 'capsules').glob('*.json'))
        times = {p: p.stat().st_mtime_ns for p in files}
        second = triage.capsule(self.workspace, self.engine, ident)
        self.assertEqual(first, second)
        self.assertEqual(times, {p: p.stat().st_mtime_ns for p in files})
        self.assertIn('assumptions', first['records'][ident])
        self.assertNotIn('leanFormulation', first['records'][ident])
        self.assertIn('unexpandedContext', first)

    def test_partial_model_limits_are_retained_without_proof_text(self):
        """T-02, DT-02; partial interface boundaries remain explicit without importing Lean declarations."""
        nodes = concept('A')
        nodes[0].update(formulationScope='partial', leanModelLimitations='Carrier only; arithmetic is unproved.',
                        leanFormulation='not needed for this task')
        write_page(self.root, 'A', nodes)
        engine = Audit(Snapshot(self.root))
        record = triage.capsule(self.workspace, engine, 'c:A')['records']['c:A']
        self.assertEqual(record['formulationScope'], 'partial')
        self.assertEqual(record['leanModelLimitations'], 'Carrier only; arithmetic is unproved.')
        self.assertNotIn('leanFormulation', record)

    def test_rule_hints_are_observations_not_dispositions(self):
        """T-01/02, DT-04; Relation has no automatic inheritance or equivalence semantics."""
        nodes = concept('B'); nodes[0]['specializationOf'] = ['c:A']; nodes[0]['specializationNote'] = 'Same carrier with an additional condition.'
        write_page(self.root, 'B', nodes)
        engine = Audit(Snapshot(self.root))
        row = {'pair': ['c:A', 'c:B'], 'fingerprints': [engine.fingerprint(i) for i in ('c:A', 'c:B')]}
        _, body = triage.packet(self.workspace, engine, row)
        self.assertEqual(body['ruleHints'][0]['kind'], 'documented_specialization')
        self.assertNotIn('decision', body)

    def test_citation_validation_rejects_hallucinated_or_one_sided_quotes(self):
        """T-03, DT-05; exact string equality verifies citation existence, not entailment."""
        _, body = triage.packet(self.workspace, self.engine, self.plan['pairs'][0])
        good = proposal(body)
        self.assertEqual(triage.validate_review(good, body), good)
        for modify in ('quote', 'one-sided', 'missing-map', 'confidence'):
            bad = copy.deepcopy(good)
            if modify == 'quote': bad['evidence'][0]['quote'] = 'invented quotation'
            elif modify == 'one-sided': bad['evidence'] = bad['evidence'][:1]
            elif modify == 'missing-map': bad['mapping'].pop('equality')
            else: bad['confidence'] = 1.0
            with self.assertRaises(AuditError): triage.validate_review(bad, body)

    def test_immutable_review_import_is_idempotent_and_conflicts_fail(self):
        """T-03/07, DT-03/06; exact pair/config identity cannot overwrite prior evidence."""
        bundle = self.bundle(1)
        triage.import_reviews(self.workspace, self.plan, self.engine, self.config, bundle)
        before = {p: p.read_bytes() for p in (self.workspace.path / 'reviews').glob('*.json')}
        triage.import_reviews(self.workspace, self.plan, self.engine, self.config, bundle)
        self.assertEqual(before, {p: p.read_bytes() for p in before})
        bad = copy.deepcopy(bundle); bad['reviews'][0]['result']['decision'] = 'same_meaning'
        with self.assertRaisesRegex(AuditError, 'Conflicting'):
            triage.import_reviews(self.workspace, self.plan, self.engine, self.config, bad)

    def test_stale_plan_and_capsule_invalidation(self):
        """T-02/07, DT-03; source fingerprint changes invalidate cached context and stale plans."""
        ident = self.plan['pairs'][0]['pair'][0]
        before = triage.capsule(self.workspace, self.engine, ident)
        owner = self.engine.index[ident].get('appliesTo', [ident])[0]
        name = self.engine.index[owner]['shortForm']
        nodes = concept(name); nodes[0]['basisScope'] += ' new assumption'
        write_page(self.root, name, nodes)
        new_engine = Audit(Snapshot(self.root))
        after = triage.capsule(self.workspace, new_engine, ident)
        self.assertNotEqual(before['fingerprint'], after['fingerprint'])
        with patch.object(triage, 'Snapshot', side_effect=lambda **kw: Snapshot(self.root, **kw)):
            with self.assertRaisesRegex(AuditError, 'Stale'): triage.load_current(self.workspace.path)

    def test_cache_corruption_and_foreign_workspaces_fail(self):
        """T-07, DT-03/10; corrupted objects and foreign data are never silently reused/overwritten."""
        ident = self.plan['pairs'][0]['pair'][0]
        triage.capsule(self.workspace, self.engine, ident)
        path = next((self.workspace.path / 'capsules').glob('*.json'))
        data = json.loads(path.read_text()); data['payload']['id'] = 'tampered'; path.write_text(json.dumps(data))
        with self.assertRaisesRegex(AuditError, 'Corrupt'): triage.capsule(self.workspace, self.engine, ident)
        foreign = self.root / 'foreign'; foreign.mkdir(); (foreign / 'keep').write_text('original')
        with self.assertRaises(AuditError): triage.Workspace(foreign, self.snapshot, create=True)
        self.assertEqual((foreign / 'keep').read_text(), 'original')

    def test_workspace_protects_graph_inputs_symlinks_and_escape_paths(self):
        """T-07, DT-10; filesystem containment prevents proposal storage in authoritative data."""
        for path in (self.root / 'data/run', self.root / '.hidden/run', self.root):
            with self.assertRaises(AuditError): triage.Workspace(path, self.snapshot, create=True)
        with self.assertRaises(AuditError): self.workspace.save('../escape.json', {})
        symlink = self.workspace.path / 'linked'; symlink.symlink_to(self.root / 'data', target_is_directory=True)
        with self.assertRaises(AuditError): self.workspace.save('linked/new.json', {})
        self.assertFalse((self.root / 'data/new.json').exists())

    def test_plan_integrity_and_machine_provenance_are_enforced(self):
        """T-07, DT-03/06; altered plans fail before use and imports cannot claim human-receipt provenance."""
        altered = copy.deepcopy(self.plan); altered['scope']['notSelectedCount'] = 0
        self.workspace.save('plan.json', altered)
        with self.assertRaisesRegex(AuditError, 'integrity'):
            triage.load_current(self.workspace.path)
        with self.assertRaises(AuditError):
            triage.reviewer_config('fixture', '1', kind='human')
        with self.assertRaises(AuditError):
            triage.import_reviews(self.workspace, self.plan, self.engine, self.config, {'schemaVersion': True, 'reviews': []})

    def test_independent_review_uses_original_packet_and_disagreement_escalates(self):
        """T-03, DT-07; separate judgments on one pair do not establish equivalence or authorize merge."""
        triage.import_reviews(self.workspace, self.plan, self.engine, self.config, self.bundle(1, ['same_meaning']))
        with self.assertRaises(AuditError):
            triage.activate(self.workspace, {**self.config, 'stage': 'independent'})
        second = triage.reviewer_config('another-reviewer', '1', stage='independent')
        exported = triage.export_requests(self.workspace, self.plan, self.engine, second)
        data = self.workspace.load(exported['export'])
        self.assertNotIn('Synthetic protocol result', json.dumps(data))
        self.assertNotIn('expectedDecision', json.dumps(data))
        triage.import_reviews(self.workspace, self.plan, self.engine, second, self.bundle(1, ['distinct']))
        report = triage.build_report(self.workspace, self.plan, self.engine)
        self.assertEqual(report['counts']['unresolved'], 1)
        self.assertEqual(report['counts']['proposedDuplicates'], 0)
        self.assertIn('Independent decision:** distinct', (self.workspace.path / 'report.md').read_text())

    def test_missing_context_is_unresolved_and_same_meaning_stays_actionable(self):
        """T-03/05, DT-07/08; insufficiency is not a successful distinction or proof."""
        bundle = self.bundle(2, ['same_meaning', 'distinct'])
        bundle['reviews'][1]['result']['missingContext'] = ['c:A']
        triage.import_reviews(self.workspace, self.plan, self.engine, self.config, bundle)
        report = triage.build_report(self.workspace, self.plan, self.engine)
        self.assertEqual(report['counts']['proposedDuplicates'], 1)
        self.assertEqual(report['counts']['unresolved'], 1)
        self.assertEqual(report['counts']['suggestedDistinctions'], 0)
        self.assertIn('required before consolidation', (self.workspace.path / 'report.md').read_text())

    def test_independent_failures_are_counted_and_later_primary_cannot_review_itself(self):
        """T-03/04/05, DT-07/08; failed second passes remain visible and declared self-independence is rejected."""
        triage.import_reviews(self.workspace, self.plan, self.engine, self.config, self.bundle(1, ['same_meaning']))
        command = [sys.executable, '-c', 'raise SystemExit(1)']
        second = triage.reviewer_config('second', '1', stage='independent', argv=command)
        with redirect_stderr(io.StringIO()):
            result = triage.run_reviews(self.workspace, self.plan, self.engine, second, command, budget=1)
        self.assertEqual(result['failed'], 1)
        report = triage.build_report(self.workspace, self.plan, self.engine)
        self.assertEqual(report['counts']['independentFailed'], 1)
        self.assertEqual(report['counts']['proposedDuplicates'], 1)
        newer_primary = triage.reviewer_config('second', '1')
        triage.import_reviews(self.workspace, self.plan, self.engine, newer_primary, self.bundle(1, ['same_meaning']))
        report = triage.build_report(self.workspace, self.plan, self.engine)
        self.assertIsNone(report['independentReviewer'])

    def test_budget_resume_and_adapter_requests_exclude_labels(self):
        """T-04, DT-06/09; bounded attempts resume from immutable results, not synthetic labels."""
        code = '''import json,sys
r=json.load(sys.stdin)
assert 'expectedDecision' not in json.dumps(r)
b=r['packet']; evidence=[]
for ident in b['pair']:
 n=b['records'][ident]; field='definition' if n['type']=='Concept' else 'formalStatement'
 evidence.append(dict(recordId=ident,field=field,quote=n[field]))
print(json.dumps(dict(decision='distinct',rationale='Synthetic protocol adapter.',mapping={k:'Synthetic mapping.' for k in ['carriers','equality','operations','assumptions']},differences=[],missingContext=[],evidence=evidence)))
'''
        command = [sys.executable, '-c', code]
        config = triage.reviewer_config('fixture', '1', argv=command, kind='synthetic-fixture')
        with redirect_stderr(io.StringIO()):
            first = triage.run_reviews(self.workspace, self.plan, self.engine, config, command, budget=1)
            second = triage.run_reviews(self.workspace, self.plan, self.engine, config, command, budget=1)
        self.assertEqual((first['completed'], second['completed']), (1, 1))
        self.assertEqual(len(list((self.workspace.path / 'reviews').glob('*.json'))), 2)
        self.assertEqual(triage.build_report(self.workspace, self.plan, self.engine)['counts']['reviewed'], 2)

    def test_timeouts_invalid_results_and_oversized_inputs_are_failures_not_decisions(self):
        """T-04, DT-06; unsuccessful executions have no semantic output or silent context truncation."""
        commands = [[sys.executable, '-c', 'import time; time.sleep(1)'],
                    [sys.executable, '-c', 'print("not json")']]
        for i, command in enumerate(commands):
            config = triage.reviewer_config('fault', str(i), argv=command)
            with redirect_stderr(io.StringIO()):
                result = triage.run_reviews(self.workspace, self.plan, self.engine, config, command, budget=1, timeout=0.01 if i == 0 else 5)
            self.assertEqual(result['failed'], 1)
            self.assertEqual(triage.build_report(self.workspace, self.plan, self.engine)['counts']['reviewed'], 0)
        config = triage.reviewer_config('too-large', '1')
        with patch.object(triage.subprocess, 'run') as run, redirect_stderr(io.StringIO()):
            result = triage.run_reviews(self.workspace, self.plan, self.engine, config, commands[1], budget=1, max_input_chars=1)
        self.assertEqual(result['failed'], 1); run.assert_not_called()
        with self.assertRaises(AuditError):
            triage.run_reviews(self.workspace, self.plan, self.engine, config, commands[1], timeout=float('inf'))

    def test_evaluation_metrics_use_independent_denominators_and_missing_predictions(self):
        """T-06, DT-09; hand oracle: coverage 3/4, exact 1/3, retain precision 1/2, duplicate 0/1."""
        triage.import_reviews(self.workspace, self.plan, self.engine, self.config,
                              self.bundle(3, ['distinct', 'distinct', 'same_meaning']))
        labels = {'schemaVersion': 1, 'labeler': {'id': 'synthetic-oracle', 'independence': 'synthetic-fixture-not-model-efficacy'},
                  'cases': [{'pair': row['pair'], 'expectedDecision': expected} for row, expected in zip(
                      self.plan['pairs'], ['distinct', 'same_meaning', 'distinct', 'semantic_variant'])]}
        result = triage.evaluate(self.workspace, self.plan, self.engine, labels)
        self.assertEqual(result['coverage']['ratio'], [3, 4])
        self.assertEqual(result['exactAgreement']['ratio'], [1, 3])
        self.assertEqual(result['retainPrecision']['ratio'], [1, 2])
        self.assertEqual(result['duplicatePrecision']['ratio'], [0, 1])
        self.assertFalse(result['automaticSuppressionEnabled'])
        self.assertNotIn('expectedDecision', triage.INSTRUCTIONS)

    def test_report_links_are_relative_to_workspace_and_render_no_raw_json(self):
        """T-05, DT-08; the human artifact exposes prose and real record links, not a JSON review burden."""
        triage.import_reviews(self.workspace, self.plan, self.engine, self.config, self.bundle(1))
        triage.build_report(self.workspace, self.plan, self.engine)
        text = (self.workspace.path / 'report.md').read_text()
        self.assertIn('../concepts/', text)
        self.assertNotIn('```json', text)


if __name__ == '__main__':
    unittest.main()
