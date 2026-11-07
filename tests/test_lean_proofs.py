"""Actual Lean rejection tests, enabled by make test-lean after a fresh build."""
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
LEAN = ROOT / 'lean'


@unittest.skipUnless(os.environ.get('CATALOG_TEST_LEAN') == '1', 'run make test-lean for compiler rejection tests')
class LeanProofRejectionTests(unittest.TestCase):
    def compile(self, body):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.lean', dir=LEAN / '.lake') as stream:
            stream.write('module\nimport Catalog\nimport Catalog.Audit\n' + body)
            stream.flush()
            return subprocess.run(['lake', 'env', 'lean', stream.name], cwd=LEAN,
                                  text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    def test_axiom_cannot_impersonate_a_theorem(self):
        result = self.compile('axiom forged : True\n#catalog_witness forged\n')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('must be theorem declarations', result.stdout)

    def test_admitted_proof_is_rejected(self):
        result = self.compile('theorem admitted : True := by sorry\n#catalog_witness admitted\n')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('sorryAx', result.stdout)

    def test_transitive_custom_axiom_is_rejected(self):
        result = self.compile('axiom fabricated : False\ntheorem derived : True := False.elim fabricated\n#catalog_witness derived\n')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Unapproved axiom', result.stdout)

    def test_wrong_statement_is_rejected(self):
        result = self.compile('example : 1 + 1 = 3 := Catalog.Proofs.natural_zero_addition 2\n')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Type mismatch', result.stdout)


if __name__ == '__main__':
    unittest.main()
