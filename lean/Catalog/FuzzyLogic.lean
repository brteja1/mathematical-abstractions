module

public import Mathlib.Basic.Real.Basic

@[expose] public section

namespace Catalog
universe u

/-- Exact real truth degrees; excludes NaN, overflow and rounded arithmetic. -/
abbrev FuzzyDegree := {x : ℝ // 0 ≤ x ∧ x ≤ 1}

/-- Membership functions, including the unique function on an empty universe. -/
abbrev FuzzySet (A : Type u) := A → FuzzyDegree

namespace FuzzySet

def empty {A : Type u} : FuzzySet A := fun _ => ⟨0, le_refl 0, zero_le_one⟩

def full {A : Type u} : FuzzySet A := fun _ => ⟨1, zero_le_one, le_refl 1⟩

def intersection {A : Type u} (s t : FuzzySet A) : FuzzySet A := fun x =>
  ⟨min (s x).val (t x).val, le_min (s x).property.1 (t x).property.1,
    le_trans (min_le_left _ _) (s x).property.2⟩

def union {A : Type u} (s t : FuzzySet A) : FuzzySet A := fun x =>
  ⟨max (s x).val (t x).val, le_trans (s x).property.1 (le_max_left _ _),
    max_le (s x).property.2 (t x).property.2⟩

def complement {A : Type u} (s : FuzzySet A) : FuzzySet A := fun x =>
  ⟨1 - (s x).val, sub_nonneg.mpr (s x).property.2, sub_le_self 1 (s x).property.1⟩

def alphaCut {A : Type u} (s : FuzzySet A) (alpha : FuzzyDegree) : _root_.Set A :=
  {x | alpha.val ≤ (s x).val}

end FuzzySet

/-- No continuity or idempotence is required of a general triangular norm. -/
structure TNorm where
  combine : FuzzyDegree → FuzzyDegree → FuzzyDegree
  commutative : ∀ a b, combine a b = combine b a
  associative : ∀ a b c, combine (combine a b) c = combine a (combine b c)
  monotone : ∀ a b c d, a ≤ b → c ≤ d → combine a c ≤ combine b d
  identity : ∀ a, combine a ⟨1, zero_le_one, le_refl 1⟩ = a

/-- Triangular conorms have neutral degree zero. -/
structure TConorm where
  combine : FuzzyDegree → FuzzyDegree → FuzzyDegree
  commutative : ∀ a b, combine a b = combine b a
  associative : ∀ a b c, combine (combine a b) c = combine a (combine b c)
  monotone : ∀ a b c d, a ≤ b → c ≤ d → combine a c ≤ combine b d
  identity : ∀ a, combine a ⟨0, le_refl 0, zero_le_one⟩ = a

/-- Truth-value algebra: adjunction selects exactly the residuated t-norms.
    Formula syntax, quantifiers and proof calculi are outside this interface. -/
structure ResiduatedFuzzyLogic extends TNorm where
  residuum : FuzzyDegree → FuzzyDegree → FuzzyDegree
  adjunction : ∀ a b c, combine a c ≤ b ↔ c ≤ residuum a b

end Catalog
