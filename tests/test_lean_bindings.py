"""Reject incomplete, stale, or misleading formal proof metadata."""
import copy
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import lean as integration
from markdown_graph import load_graph


class LeanBindingTests(unittest.TestCase):
    def setUp(self):
        self.manifest = json.loads(integration.MANIFEST.read_text())
        self.index = {n['id']: n for n in load_graph()['@graph']}
        self.target = 'urn:csabs:theorem/Group-inverse-product'

    def errors(self):
        return integration.validate(self.manifest, self.index)

    def test_current_bindings_cover_every_concept(self):
        self.assertEqual(self.errors(), [])

    def test_new_concept_needs_a_model(self):
        node = copy.deepcopy(self.index['urn:csabs:concept/Group'])
        node['id'] = 'urn:csabs:concept/NewConcept'
        self.index[node['id']] = node
        self.assertTrue(any('Concepts without a Lean model' in e for e in self.errors()))

    def test_changed_claim_invalidates_binding(self):
        self.index[self.target]['formalStatement'] += ' changed'
        self.assertTrue(any('premises changed' in e for e in self.errors()))

    def test_changed_axiom_invalidates_its_witness(self):
        premise = self.index[self.target]['dependsOn'][0]
        self.index[premise]['formalStatement'] = 'False'
        self.assertTrue(any(self.target in e and 'premises changed' in e for e in self.errors()))

    def test_expected_type_required(self):
        del self.manifest['bindings'][self.target]['expectedType']
        self.assertTrue(any('expectedType' in e for e in self.errors()))

    def test_every_explicit_premise_needs_mapping(self):
        self.manifest['bindings'][self.target]['premiseMapping'] = {}
        self.assertTrue(any('dependsOn premise' in e for e in self.errors()))

    def test_sorry_cannot_be_whitelisted(self):
        self.manifest['bindings'][self.target]['allowedAxioms'].append('sorryAx')
        self.assertTrue(any('foundational axioms' in e for e in self.errors()))

    def test_path_escape_in_module_rejected(self):
        self.manifest['bindings'][self.target]['module'] = '../outside'
        self.assertTrue(any('invalid local module' in e for e in self.errors()))

    def test_old_report_is_not_evidence(self):
        with patch.object(integration, 'inputs_digest', return_value='changed'):
            self.assertIsNone(integration.fresh_report())


if __name__ == '__main__':
    unittest.main()
