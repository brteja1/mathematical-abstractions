"""Keep the declared broad-core inventory usable for retrieval and formalization."""
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from markdown_graph import load_graph
from agent_query import resolve, dossier


class FoundationalModelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.inventory = json.loads((ROOT / 'data/foundational_models.json').read_text())
        cls.index = {n['id']: n for n in load_graph()['@graph']}
        cls.bindings = json.loads((ROOT / 'lean/bindings.json').read_text())['bindings']

    def test_declared_families_and_instantiations_resolve_to_models(self):
        covered = set()
        families = self.inventory['families']
        self.assertEqual(len({f['name'] for f in families}), len(families))
        for entry in families + self.inventory['instantiations']:
            self.assertTrue(entry['concepts'], entry['name'])
            for name in entry['concepts']:
                ident = resolve(self.index, name)
                self.assertEqual(self.index[ident]['type'], 'Concept')
                self.assertEqual(self.bindings[ident]['kind'], 'model')
                covered.add(name)
        additions = self.inventory['addedConcepts']
        self.assertEqual(len(set(additions)), len(additions))
        self.assertTrue(set(additions) <= covered)

    def test_shared_prefix_map_rules_retrieve_once_with_explicit_applicability(self):
        seed = resolve(self.index, 'Trie')
        context = dossier(self.index, seed, 'tests', 100)
        self.assertFalse(context['truncated'])
        nodes = {n['id']: n for n in context['nodes']}
        rule = 'urn:csabs:axiom/Map-update-lookup'
        self.assertIn(rule, self.index[seed]['hasAxiom'])
        self.assertIn(seed, nodes[rule]['appliesTo'])
        self.assertNotIn('urn:csabs:axiom/Trie-put-equation', self.index)
        self.assertIn(rule, {ref for n in context['nodes'] for ref in n.get('dependsOn', [])} |
                      set(self.index[seed]['hasAxiom']))

    def test_cross_concept_proof_premises_are_available_in_dossiers(self):
        seed = resolve(self.index, 'BipartiteGraph')
        context = dossier(self.index, seed, 'proof', 100)
        self.assertFalse(context['truncated'])
        ids = {n['id'] for n in context['nodes']}
        claim = self.index['urn:csabs:theorem/BipartiteGraph-sides-partition']
        self.assertIn('urn:csabs:axiom/BooleanType-enumeration', claim['dependsOn'])
        self.assertTrue(set(claim['dependsOn']) <= ids)
        for source in self.index['urn:csabs:axiom/BooleanType-enumeration']['source']:
            self.assertIn(source, ids)


if __name__ == '__main__':
    unittest.main()
