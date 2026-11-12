"""Progressive disclosure keeps guards intact and proof material opt-in."""
import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from retrieval_views import record_view


class RetrievalViewTests(unittest.TestCase):
    def test_guard_and_partial_scope_survive_without_optional_payload(self):
        record = {'type': 'Concept', 'definition': 'a guarded partial interface',
                  'mathematicalFormulation': 'f : A ⇀ B', 'precondition': 'x ≠ 0',
                  'assumptions': ['finite A'], 'formulationScope': 'partial',
                  'leanModelLimitations': 'no totality proof', 'hasTheorem': ['claim'],
                  'leanFormulation': 'def f := ...', 'proofSketch': 'long proof'}
        focused = record_view(record)
        for field in ('definition', 'mathematicalFormulation', 'precondition', 'assumptions',
                      'formulationScope', 'leanModelLimitations'):
            self.assertEqual(focused[field], record[field])
        self.assertNotIn('hasTheorem', focused)
        self.assertNotIn('leanFormulation', focused)
        self.assertNotIn('proofSketch', focused)
        self.assertEqual(record_view(record, 'full'), record)
        self.assertIn('hasTheorem', record)  # projection never mutates the source

    def test_lean_does_not_expand_other_claims(self):
        record = {'leanFormulation': 'def target : Prop := True',
                  'hasTheorem': ['unrelated'], 'hasOperation': ['needed']}
        projected = record_view(record, 'lean', selected_links=['hasOperation'])
        self.assertIn('leanFormulation', projected)
        self.assertEqual(projected['hasOperation'], ['needed'])
        self.assertNotIn('hasTheorem', projected)

    def test_dependency_free_clis_use_focused_views_by_default(self):
        commands = [
            ['scripts/catalog.py', 'get', 'Stack', '--sections', 'operations'],
            ['scripts/agent_query.py', 'node', 'Stack'],
        ]
        for command in commands:
            result = subprocess.run([sys.executable, *command], cwd=ROOT, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            record = json.loads(result.stdout)
            self.assertTrue(record['mathematicalFormulation'])
            self.assertNotIn('hasTheorem', record)
            self.assertNotIn('leanFormulation', record)

    def test_cli_neighbors_omit_proof_payload_and_lean_is_opt_in(self):
        result = subprocess.run([sys.executable, 'scripts/agent_query.py', 'neighbors', 'Stack',
                                 '--relations', 'requiresConcept', '--limit', '4'],
                                cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        response = json.loads(result.stdout)
        self.assertEqual(response['view'], 'focused')
        self.assertTrue(all('leanFormulation' not in n and 'hasTheorem' not in n
                            for n in response['nodes']))
        result = subprocess.run([sys.executable, 'scripts/agent_query.py', 'node', 'Stack',
                                 '--view', 'lean'], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        record = json.loads(result.stdout)
        self.assertIn('leanFormulation', record)
        self.assertNotIn('hasTheorem', record)

    def test_catalog_full_view_returns_the_canonical_concept(self):
        from markdown_graph import load_graph
        expected = next(n for n in load_graph()['@graph'] if n.get('shortForm') == 'Stack')
        result = subprocess.run([sys.executable, 'scripts/catalog.py', 'get', 'Stack',
                                 '--view', 'full'], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), expected)


if __name__ == '__main__':
    unittest.main()
