"""Exercise bounded ONTFS retrieval, source fidelity and freshness protection."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import subprocess
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
sys.path.insert(0, str(ROOT / 'deps/ONTFS'))
from test_context import TestContext, bounded_page, encode

AVAILABLE = all(importlib.util.find_spec(m) for m in ('rdflib', 'ontfs'))


class OutputBudgetTests(unittest.TestCase):
    def test_unicode_records_page_without_clipping_assumptions(self):
        records = [{'id': str(i), 'formalStatement': '∀x: ' + 'α' * 850,
                    'assumptions': ['all inputs satisfy the stated precondition']} for i in range(3)]
        offset, actual = 0, []
        while offset is not None:
            result = bounded_page(records[offset:], 3, offset, 3, 2048, {'command': 'test'})
            self.assertLessEqual(len(encode(result)), 2048)
            self.assertGreater(result['returned'], 0)
            actual.extend(result['records'])
            offset = result['nextOffset']
        self.assertEqual(actual, records)

    def test_oversized_record_is_explicit_without_partial_statement(self):
        record = {'id': 'large', 'formalStatement': 'x' * 5000, 'assumptions': ['critical']}
        result = bounded_page([record], 1, 0, 1, 2048, {'command': 'test'})
        self.assertEqual(result['records'], [])
        self.assertTrue(result['needsLargerBudget'])
        self.assertTrue(result['truncated'])
        self.assertEqual(result['nextOffset'], 0)
        self.assertEqual(result['blockedRecord'], 'large')
        self.assertGreater(result['requiredChars'], 2048)
        self.assertLessEqual(len(encode(result)), 2048)

    def test_depth_truncation_survives_end_of_page(self):
        result = bounded_page([{'id': 'root'}], 1, 0, 1, 2048,
                              {'depthBoundary': {'count': 1, 'sample': ['premise']}})
        self.assertTrue(result['truncated'])
        self.assertIsNone(result['nextOffset'])


@unittest.skipUnless(AVAILABLE, 'ONTFS/RDF dependencies are not installed')
class OntfsTestContextTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from ontology import build
        cls.tmp = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.tmp.cleanup)
        cls.directory = Path(cls.tmp.name)
        build(cls.directory)
        cls.context = TestContext(cls.directory)

    def test_search_paginates_real_ontfs_results(self):
        offset, found = 0, []
        while offset is not None:
            result = self.context.search('queue', offset=offset, limit=1, max_chars=4000)
            self.assertEqual(result['selectionBackend'], 'ONTFS/SPARQL')
            self.assertLessEqual(len(encode(result)), 4000)
            self.assertEqual(result['returned'], 1)
            found.extend(n['shortForm'] for n in result['records'])
            offset = result['nextOffset']
        self.assertEqual(len(found), len(set(found)))
        self.assertIn('Queue', found)
        self.assertIn('PriorityQueue', found)

    def test_search_includes_operation_behavior(self):
        result = self.context.search('dequeue', limit=8)
        self.assertIn('Queue', [n['shortForm'] for n in result['records']])

    def test_search_finds_readable_formulation_semantics(self):
        # This phrase describes an order convention in the readable formulation,
        # rather than a concept/operation name. Search still returns compact IDs.
        result = self.context.search('reverse numerical order', limit=8)
        self.assertIn('MinPlusSemiring', [n['shortForm'] for n in result['records']])
        self.assertTrue(all('leanFormulation' not in n for n in result['records']))

    def test_sparql_text_is_literal_not_query_injection(self):
        result = self.context.search('queue") } UNION { ?id a ca:Concept } #')
        self.assertEqual(result['total'], 0)

    def test_category_filter(self):
        result = self.context.search('', category='data-structures', limit=4)
        self.assertGreater(result['returned'], 0)
        from subjects import in_category
        self.assertTrue(all(in_category(self.context.index, n, 'data-structures') for n in result['records']))

    def test_nested_category_search_includes_descendants(self):
        result = self.context.search('', category='synchronization', limit=20)
        self.assertEqual({n['shortForm'] for n in result['records']}, {'Lock', 'Mutex', 'LamportBakery'})
        full = self.context.search('', category='urn:csabs:category/synchronization', limit=20)
        self.assertEqual(full['records'], result['records'])

    def test_interface_keeps_root_first_and_does_not_inherit_axioms(self):
        result = self.context.interface('Group', sections=['axioms'], limit=32, max_chars=40000)
        self.assertFalse(result['truncated'])
        self.assertEqual(result['records'][0]['shortForm'], 'Group')
        actual = {n['id'] for n in result['records'][1:]}
        self.assertEqual(actual, set(self.context.index[result['records'][0]['id']]['hasAxiom']))
        self.assertNotIn('urn:csabs:axiom/Monoid-identity', actual)

    def test_node_preserves_all_authoritative_conditions_and_provenance(self):
        ident = 'urn:csabs:theorem/Group-inverse-product'
        result = self.context.node(ident, view='full')
        self.assertEqual(result['records'], [self.context.index[ident]])
        self.assertEqual(result['records'][0]['provenanceStatus'], 'legacy-source-missing')
        self.assertTrue(result['records'][0]['assumptions'])

    def test_citations_are_direct_not_inherited(self):
        self.assertGreater(self.context.sources('Group')['total'], 0)
        result = self.context.sources('urn:csabs:theorem/Group-inverse-product')
        self.assertEqual(result['total'], 0)

    def test_local_formulation_source_does_not_close_a_citation_gap(self):
        ident = 'urn:csabs:theorem/Group-inverse-product'
        result = self.context.sources(ident, kind='formulation', max_chars=4000)
        self.assertEqual(result['kind'], 'formulation')
        self.assertEqual([n['path'] for n in result['records']], ['lean/Catalog/Witnesses.lean'])
        self.assertEqual(self.context.sources(ident)['total'], 0)
        self.assertEqual(self.context.node(ident)['records'][0]['provenanceStatus'], 'legacy-source-missing')
        # The concept's separate Algebra source must not be inherited by its claim.
        concept = self.context.sources('Group', kind='formulation')
        self.assertEqual([n['path'] for n in concept['records']], ['lean/Catalog/Algebra.lean'])

    def test_partial_scope_and_witness_premises_survive_atomic_retrieval(self):
        model = self.context.node('BTree', view='full')['records'][0]
        self.assertEqual(model['formulationScope'], 'partial')
        self.assertTrue(model['leanModelLimitations'])
        self.assertEqual(model, self.context.index[model['id']])
        claim = self.context.node('urn:csabs:law/stack-push-pop', view='lean')['records'][0]
        self.assertEqual(set(json.loads(claim['leanPremiseMapping'])), set(claim['dependsOn']))
        self.assertIn('some', claim['leanFormulation'])

    def test_default_interface_loads_only_operations_without_proof_payload(self):
        result = self.context.interface('Group', limit=32, max_chars=40000)
        self.assertEqual(result['view'], 'focused')
        self.assertEqual(result['sections'], ['operations'])
        self.assertEqual({n['type'] for n in result['records']}, {'Concept', 'Operation'})
        for record in result['records']:
            for field in ('hasAxiom', 'hasLaw', 'hasTheorem', 'leanFormulation', 'leanPremiseMapping', 'proofSketch'):
                self.assertNotIn(field, record)
        root = result['records'][0]
        self.assertTrue(root['mathematicalFormulation'])
        self.assertTrue(root['leanModelLimitations'])

    def test_theorems_are_retrieved_only_when_selected(self):
        result = self.context.interface('Group', sections=['theorems'], limit=32, max_chars=40000)
        expected = set(self.context.index['urn:csabs:concept/Group']['hasTheorem'])
        self.assertEqual({n['id'] for n in result['records'][1:]}, expected)
        self.assertNotIn('hasAxiom', result['records'][0])
        self.assertNotIn('hasLaw', result['records'][0])
        for record in result['records'][1:]:
            self.assertNotIn('leanFormulation', record)
            self.assertTrue(record['assumptions'])

    def test_focused_claim_keeps_conditions_and_omits_lean_and_proof_text(self):
        ident = 'urn:csabs:law/stack-push-pop'
        record = self.context.node(ident)['records'][0]
        original = self.context.index[ident]
        for field in ('formalStatement', 'assumptions', 'appliesTo', 'dependsOn', 'provenanceStatus'):
            self.assertEqual(record[field], original[field])
        self.assertNotIn('leanFormulation', record)
        self.assertNotIn('leanPremiseMapping', record)
        self.assertNotIn('proofSketch', record)

    def test_zero_depth_discloses_unexpanded_premises(self):
        ident = 'urn:csabs:theorem/Group-inverse-product'
        result = self.context.premises(ident, depth=0)
        self.assertEqual(result['total'], 1)
        self.assertEqual(result['depthBoundary']['count'], len(self.context.index[ident]['dependsOn']))
        self.assertTrue(result['truncated'])
        self.assertIsNone(result['nextOffset'])

    def test_multistep_depth_boundary_matches_explicit_dependencies(self):
        ident = 'urn:csabs:law/FormalLanguage-concatenation-monoid'
        first = {ident, *self.context.index[ident]['dependsOn']}
        boundary = {p for node in first for p in self.context.index[node].get('dependsOn', [])} - first
        self.assertTrue(boundary)
        result = self.context.premises(ident, depth=1, limit=32, max_chars=40000)
        self.assertEqual({n['id'] for n in result['records']}, first)
        self.assertEqual(result['depthBoundary']['count'], len(boundary))
        self.assertTrue(set(result['depthBoundary']['sample']) <= boundary)
        deeper = self.context.premises(ident, depth=2, limit=32, max_chars=40000)
        self.assertTrue(first | boundary <= {n['id'] for n in deeper['records']})

    def test_rejects_changed_source_inputs(self):
        from markdown_graph import load_graph
        doc = copy.deepcopy(load_graph())
        next(n for n in doc['@graph'] if n.get('shortForm') == 'Queue')['definition'] += ' changed'
        with patch('test_context.load_graph', return_value=doc):
            with self.assertRaisesRegex(ValueError, 'stale'):
                TestContext(self.directory)

    def test_rejects_an_unpinned_preloaded_backend(self):
        class ForeignOntFS:
            pass
        with patch('test_context.backend', return_value=ForeignOntFS):
            with self.assertRaisesRegex(RuntimeError, 'not from the pinned checkout'):
                TestContext(self.directory)

    def test_rejects_locally_edited_projection_without_overwriting(self):
        with tempfile.TemporaryDirectory() as directory:
            directory = Path(directory)
            marker = self.directory / '.ontfs.generated.json'
            (directory / marker.name).write_bytes(marker.read_bytes())
            target = directory / '.ontfs.ttl'
            edited = (self.directory / target.name).read_bytes() + b'\n# scratch edit\n'
            target.write_bytes(edited)
            with self.assertRaisesRegex(ValueError, 'local edits'):
                TestContext(directory)
            self.assertEqual(target.read_bytes(), edited)

    def test_queries_leave_projection_unchanged(self):
        target = self.directory / '.ontfs.ttl'
        before = hashlib.sha256(target.read_bytes()).hexdigest()
        self.context.claims('Queue', kind='law')
        self.context.node('Queue')
        self.assertEqual(hashlib.sha256(target.read_bytes()).hexdigest(), before)

    def test_unsafe_bounds_and_unknown_ids_fail(self):
        with self.assertRaisesRegex(ValueError, 'Source kind'):
            self.context.sources('Group', kind='formulation } UNION { ?id ?p ?o }')
        with self.assertRaisesRegex(ValueError, 'limit 1..32'):
            self.context.search('queue', limit=10000)
        with self.assertRaisesRegex(ValueError, 'depth'):
            self.context.premises('urn:csabs:theorem/Group-inverse-product', depth=100)
        with self.assertRaisesRegex(ValueError, 'Unknown'):
            self.context.node('not-a-concept')

    def test_skill_entrypoint_works_from_another_repository(self):
        entrypoint = ROOT / 'ai/skills/mathematical-tests/scripts/query.py'
        result = subprocess.run([sys.executable, '-B', str(entrypoint), '--directory', str(self.directory),
                                 'search', 'dequeue', '--limit', '1', '--max-chars', '4000'],
                                cwd=self.directory, text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        response = json.loads(result.stdout)
        self.assertEqual(response['records'][0]['shortForm'], 'Queue')
        self.assertLessEqual(len(result.stdout), 4000)

    def test_cli_signals_atomic_record_budget_failure(self):
        entrypoint = ROOT / 'ai/skills/mathematical-tests/scripts/query.py'
        result = subprocess.run([sys.executable, '-B', str(entrypoint), '--directory', str(self.directory),
                                 'node', 'SumType', '--view', 'full', '--max-chars', '2048'],
                                cwd=self.directory, text=True, capture_output=True)
        self.assertEqual(result.returncode, 2, result.stderr)
        response = json.loads(result.stdout)
        self.assertTrue(response['needsLargerBudget'])
        self.assertEqual(response['records'], [])
        self.assertLessEqual(len(result.stdout), 2048)

    def test_cli_retrieves_formulation_sources_from_another_directory(self):
        entrypoint = ROOT / 'ai/skills/mathematical-tests/scripts/query.py'
        result = subprocess.run([sys.executable, '-B', str(entrypoint), '--directory', str(self.directory),
                                 'sources', 'Stack', '--kind', 'formulation', '--max-chars', '4000'],
                                cwd=self.directory, text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        response = json.loads(result.stdout)
        self.assertEqual(response['kind'], 'formulation')
        self.assertEqual([n['path'] for n in response['records']], ['lean/Catalog/DataStructures.lean'])


if __name__ == '__main__':
    unittest.main()
