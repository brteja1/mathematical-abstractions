"""Inventory completeness and drift checks; not LLVM semantic correctness tests."""
import copy
import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from llvm_transform_coverage import MANIFEST, REPORT, parse_registry, render, validate
from markdown_graph import load_graph


class LLVMTransformCoverageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = json.loads(MANIFEST.read_text())
        cls.index = {n['id']: n for n in load_graph()['@graph']}

    def test_current_mapping_and_generated_report(self):
        self.assertEqual(validate(self.manifest, self.index), [])
        self.assertEqual(REPORT.read_text(), render(self.manifest, self.index))

    def test_rejects_unmapped_pass_and_missing_concept(self):
        manifest = copy.deepcopy(self.manifest)
        manifest['entries'][0]['family'] = 'unmapped'
        manifest['families']['scalar-algebra']['concepts'] = ['urn:csabs:concept/missing']
        errors = validate(manifest, self.index)
        self.assertTrue(any('Unmapped pass:' in e for e in errors))
        self.assertTrue(any('Unknown concept' in e for e in errors))

    def test_does_not_accept_new_registration_as_covered(self):
        source = 'FUNCTION_PASS("new-pass", NewPass())\n'
        errors = validate(self.manifest, self.index, source)
        self.assertTrue(any('missing mappings=' in e and 'new-pass' in e for e in errors))
        self.assertTrue(any('content hash differs' in e for e in errors))

    def test_parser_preserves_scope_parameters_and_multiline_locators(self):
        source = ('#define FUNCTION_PASS(NAME, CREATE)\n'
                  'FUNCTION_PASS("same", Pass())\n'
                  'LOOP_PASS_WITH_PARAMS(\n  "same",\n  Pass(), Parser)\n')
        self.assertEqual(parse_registry(source), [
            {'kind': 'FUNCTION_PASS', 'name': 'same', 'line': 2},
            {'kind': 'LOOP_PASS_WITH_PARAMS', 'name': 'same', 'line': 3}])

    def test_rejects_unrecognized_nonliteral_and_duplicate_registrations(self):
        for source in ('MACHINE_FUNCTION_PASS("x", X())\n',
                       'FUNCTION_PASS(NAME_MACRO, X())\n',
                       'FUNCTION_PASS("x", X())\nFUNCTION_PASS("x", X())\n'):
            with self.subTest(source=source), self.assertRaises(ValueError):
                parse_registry(source)


if __name__ == '__main__':
    unittest.main()
