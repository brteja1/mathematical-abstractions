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

    def test_cslib_bridge_expected_types_and_axioms(self):
        result = self.compile('''
import all Catalog.CSLib
example {S Act : Type} (t : Catalog.LabelledTransitionSystem S Act) :
    Catalog.CSLib.fromLTS (Catalog.CSLib.toLTS t) t.initial = t :=
  Catalog.CSLib.roundTrip t
example {S Act : Type} (t : Catalog.LabelledTransitionSystem S Act)
    (s e : S) (word : List Act) :
    Catalog.LabelledPath t s word e ↔ (Catalog.CSLib.toLTS t).MTr s word e :=
  Catalog.CSLib.labelledPath_iff t s word e
example {S Act : Type} (t : Catalog.LabelledTransitionSystem S Act) (s : S) :
    Catalog.finiteTraces t s = (Catalog.CSLib.toLTS t).traces s :=
  Catalog.CSLib.finiteTraces_eq t s
#catalog_witness Catalog.CSLib.roundTrip
#catalog_witness Catalog.CSLib.labelledPath_iff
#catalog_witness Catalog.CSLib.finiteTraces_eq
''')
        self.assertEqual(result.returncode, 0, result.stdout)
        for name in ('roundTrip', 'labelledPath_iff', 'finiteTraces_eq'):
            self.assertIn('CATALOG_WITNESS Catalog.CSLib.' + name + ' |', result.stdout)

    def acquisition_source(self):
        return (ROOT / 'ai/skills/abstraction-acquisition/references/watermark.lean').read_text()

    def compile_acquisition(self, source):
        # Keep the example outside the catalog library and authoritative graph.
        with tempfile.NamedTemporaryFile(mode='w', suffix='.lean', dir=LEAN / '.lake') as stream:
            stream.write(source)
            stream.flush()
            return subprocess.run(['lake', 'env', 'lean', '-DwarningAsError=true', stream.name],
                                  cwd=LEAN, text=True, stdout=subprocess.PIPE,
                                  stderr=subprocess.STDOUT)

    def test_acquisition_constructs_and_audits_model_and_downstream_claim(self):
        result = self.compile_acquisition(self.acquisition_source())
        self.assertEqual(result.returncode, 0, result.stdout)
        for name in ('natural_model_satisfies', 'merge_three_covers'):
            self.assertIn('CATALOG_WITNESS AcquisitionExample.' + name + ' |', result.stdout)

    def test_acquisition_rejects_inapplicable_merge(self):
        # A minimum operation cannot satisfy the same upper-bound obligations.
        source = self.acquisition_source().replace(':= max a b', ':= min a b')
        result = self.compile_acquisition(source)
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn('Type mismatch', result.stdout)

    def test_acquisition_rejects_admitted_model_satisfaction(self):
        source = self.acquisition_source()
        start = source.index('  exact ⟨Nat.le_refl')
        end = source.index('\n\n-- Additional task obligation', start)
        result = self.compile_acquisition(source[:start] + '  sorry' + source[end:])
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn('sorryAx', result.stdout)

    def test_acquisition_rejects_fabricated_model_satisfaction(self):
        source = self.acquisition_source()
        declaration = 'theorem natural_model_satisfies : JoinBasis Nat (· ≤ ·) merge := by'
        source = source.replace(declaration,
                                'axiom fabricated_basis : JoinBasis Nat (· ≤ ·) merge\n\n' + declaration)
        start = source.index('  exact ⟨Nat.le_refl')
        end = source.index('\n\n-- Additional task obligation', start)
        result = self.compile_acquisition(source[:start] + '  exact fabricated_basis' + source[end:])
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn('Unapproved axiom', result.stdout)


if __name__ == '__main__':
    unittest.main()
