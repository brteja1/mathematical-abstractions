"""Reject incomplete, stale, or misleading formal proof metadata."""
import copy
import contextlib
import io
import json
from pathlib import Path
import sys
import tempfile
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

    def test_refresh_selected_binding_preserves_other_fields_and_input(self):
        original = copy.deepcopy(self.manifest)
        self.index[self.target]['formalStatement'] += ' changed'
        updated, changes = integration.refresh_bindings(self.manifest, self.index, [self.target])
        self.assertEqual([c['id'] for c in changes], [self.target])
        self.assertEqual(updated['bindings'][self.target]['catalogHash'],
                         integration.catalog_hash(self.index, self.target))
        updated['bindings'][self.target]['catalogHash'] = original['bindings'][self.target]['catalogHash']
        self.assertEqual(updated, original)
        self.assertEqual(self.manifest, original)

    def test_refresh_rejects_unknown_ids_and_invalid_metadata(self):
        with self.assertRaisesRegex(ValueError, 'No Lean binding'):
            integration.refresh_bindings(self.manifest, self.index, ['MissingConcept'])
        del self.manifest['bindings'][self.target]['expectedType']
        with self.assertRaisesRegex(ValueError, 'expectedType'):
            integration.refresh_bindings(self.manifest, self.index)

    def test_refresh_cli_preview_write_and_idempotence(self):
        self.manifest['bindings'][self.target]['catalogHash'] = 'stale'
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'bindings.json'
            path.write_text(json.dumps(self.manifest, indent=2) + '\n')
            original = path.read_bytes()
            with patch.object(integration, 'MANIFEST', path), contextlib.redirect_stdout(io.StringIO()):
                with patch.object(sys, 'argv', ['lean.py', 'refresh-bindings', '--dry-run']):
                    self.assertEqual(integration.main(), 0)
                self.assertEqual(path.read_bytes(), original)
                with patch.object(sys, 'argv', ['lean.py', 'refresh-bindings']):
                    self.assertEqual(integration.main(), 0)
                updated = path.read_bytes()
                self.assertNotEqual(updated, original)
                self.assertEqual(integration.validate(json.loads(updated), self.index), [])
                with patch.object(sys, 'argv', ['lean.py', 'refresh-bindings']):
                    self.assertEqual(integration.main(), 0)
                self.assertEqual(path.read_bytes(), updated)

    def test_formulation_cannot_drift_from_lean_source(self):
        self.index['urn:csabs:concept/Stack']['leanFormulation'] = 'abbrev Stack := Nat'
        self.assertTrue(any('Lean formulation is stale' in e for e in self.errors()))

    def test_formulation_cannot_hide_partial_scope(self):
        self.index['urn:csabs:concept/BTree']['formulationScope'] = 'model'
        self.assertTrue(any('formulation scope differs' in e for e in self.errors()))

    def test_formulation_requires_its_actual_source(self):
        self.index['urn:csabs:concept/Stack']['formulationSource'] = 'urn:csabs:source/local-lean-Algebra'
        self.assertTrue(any('source/locator differs' in e for e in self.errors()))

    def test_displayed_premises_cannot_diverge_from_witness_mapping(self):
        self.index[self.target]['leanPremiseMapping'] = '{}'
        self.assertTrue(any('formulation premise mapping differs' in e for e in self.errors()))

    def test_every_concept_has_a_readable_and_typed_formulation(self):
        for node in self.index.values():
            if node['type'] == 'Concept':
                self.assertTrue(node.get('mathematicalFormulation'), node['id'])
                self.assertTrue(node.get('leanFormulation'), node['id'])

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
