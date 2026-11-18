module

public import Mathlib.Order.Lattice.Nat
import Catalog.Audit

@[expose] public section

set_option warningAsError true

namespace AcquisitionExample

-- The selected order-based JoinSemilattice basis, not just associativity.
def JoinBasis (A : Type) (le : A → A → Prop) (join : A → A → A) : Prop :=
  (∀ a, le a a) ∧
  (∀ a b c, le a b → le b c → le a c) ∧
  (∀ a b, le a b → le b a → a = b) ∧
  (∀ a b, le a (join a b) ∧ le b (join a b)) ∧
  (∀ a b c, le a c → le b c → le (join a b) c)

def merge (a b : Nat) : Nat := max a b

-- No JoinBasis hypothesis is assumed: prove each constraint for these operations.
theorem natural_model_satisfies : JoinBasis Nat (· ≤ ·) merge := by
  exact ⟨Nat.le_refl, fun _ _ _ hab hbc => Nat.le_trans hab hbc,
    fun _ _ hab hba => Nat.le_antisymm hab hba,
    fun a b => ⟨Nat.le_max_left a b, Nat.le_max_right a b⟩,
    fun _ _ _ hac hbc => max_le hac hbc⟩

-- Additional task obligation: a merge of three replicas cannot regress any input.
theorem merge_three_covers (a b c : Nat) :
    a ≤ merge (merge a b) c ∧ b ≤ merge (merge a b) c ∧
      c ≤ merge (merge a b) c := by
  have upper := natural_model_satisfies.2.2.2.1
  exact ⟨Nat.le_trans (upper a b).1 (upper (merge a b) c).1,
    Nat.le_trans (upper a b).2 (upper (merge a b) c).1,
    (upper (merge a b) c).2⟩

-- Nontrivial task inputs, with exact unbounded natural-number semantics.
example : merge 0 7 = 7 := rfl
example : merge (merge 3 7) 5 = 7 := rfl
example : (0 : Nat) ≠ 1 := Nat.zero_ne_one

-- Independently specified expected propositions plus transitive axiom audits.
example : JoinBasis Nat (· ≤ ·) merge := natural_model_satisfies
example : ∀ a b c : Nat,
    a ≤ merge (merge a b) c ∧ b ≤ merge (merge a b) c ∧
      c ≤ merge (merge a b) c := merge_three_covers

#catalog_witness AcquisitionExample.natural_model_satisfies
#catalog_witness AcquisitionExample.merge_three_covers

end AcquisitionExample
