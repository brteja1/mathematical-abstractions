module

public import Catalog.Foundations
public import Catalog.DataStructures
public import Catalog.Order
public import Mathlib.Data.Stream.Defs
public import Mathlib.Data.Rat.Defs
public import Mathlib.Algebra.Field.Rat
public import Mathlib.Algebra.Order.Archimedean.Real.Basic
public import Mathlib.Basic.Complex.Basic
public import Mathlib.LinearAlgebra.Finsupp.Defs
public import Mathlib.Algebra.BigOperators.Finsupp.Basic
public import Mathlib.Basic.NNReal.Basic
public import Lean.Elab.Tactic.Omega

@[expose] public section

namespace Catalog
universe u v w

abbrev BooleanType := Bool
abbrev FiniteType (A : Type u) := Fintype A
abbrev DependentPair (A : Type u) (B : A → Type v) := Sigma B
abbrev DependentFunction (A : Type u) (B : A → Type v) := (a : A) → B a
abbrev Subtype (A : Type u) (P : A → Prop) := {a : A // P a}
abbrev QuotientType (A : Type u) (r : Setoid A) := Quotient r
abbrev RationalNumber := Rat
abbrev RealNumber := Real
abbrev ComplexNumber := Complex
abbrev Stream (A : Type u) := Stream' A
abbrev SparseVector (F : Type u) (I : Type v) [_root_.Field F] := I →₀ F
abbrev JoinSemilattice (A : Type u) := SemilatticeSup A

/-- A finite immutable cursor. Equality retains the original sequence and cursor
position; a next step on exhaustion returns the same exhausted cursor. -/
structure FiniteIterator (A : Type u) where
  values : List A
  position : Fin (values.length + 1)

def FiniteIterator.remaining {A : Type u} (it : FiniteIterator A) : List A :=
  it.values.drop it.position.val

def FiniteIterator.next {A : Type u} (it : FiniteIterator A) : Option A × FiniteIterator A :=
  if h : it.position.val < it.values.length then
    (some it.values[it.position.val],
      ⟨it.values, ⟨it.position.val + 1, by have := it.position.isLt; omega⟩⟩)
  else (none, it)

structure ClosedInterval (A : Type u) [LinearOrder A] where
  lower : A
  upper : A
  ordered : lower ≤ upper

def ClosedInterval.contains {A : Type u} [LinearOrder A] (i : ClosedInterval A) (x : A) : Prop :=
  i.lower ≤ x ∧ x ≤ i.upper

def ClosedInterval.intersect {A : Type u} [LinearOrder A]
    (i j : ClosedInterval A) : Option (ClosedInterval A) :=
  if h : max i.lower j.lower ≤ min i.upper j.upper then
    some ⟨max i.lower j.lower, min i.upper j.upper, h⟩ else none

/-- Finitely supported, exactly normalized nonnegative mass. Empty supports are
excluded by normalization; the ambient type itself need not be finite. -/
structure FiniteDistribution (A : Type u) where
  mass : A →₀ NNReal
  normalized : mass.sum (fun _ p => p) = 1

/-- State-based replication algebra. No transport, delivery or liveness theorem
is hidden in this structure; updates are inflationary, not assumed commutative. -/
structure StateBasedCRDT (S : Type u) (Op : Type v) [SemilatticeSup S] [OrderBot S] where
  update : Op → S → S
  inflationary : ∀ op s, s ≤ update op s

def StateBasedCRDT.merge {S : Type u} [SemilatticeSup S] (x y : S) : S := x ⊔ y

namespace CoreDataProofs

theorem bool_not_not (b : BooleanType) : !(!b) = b := by cases b <;> rfl

theorem sigma_eta {A : Type u} {B : A → Type v} (p : DependentPair A B) :
    Sigma.mk p.1 p.2 = p := by cases p; rfl

theorem dependent_function_eta {A : Type u} {B : A → Type v} (f : DependentFunction A B) :
    (fun a => f a) = f := rfl

theorem subtype_value_injective {A : Type u} {P : A → Prop} (x y : Catalog.Subtype A P)
    (h : x.val = y.val) : x = y := _root_.Subtype.ext h

theorem rational_add_zero (q : RationalNumber) : q + 0 = q := add_zero q

theorem real_square_nonnegative (x : RealNumber) : 0 ≤ x * x := mul_self_nonneg x

theorem complex_eta (z : ComplexNumber) : Complex.mk z.re z.im = z := Complex.eta z

theorem stream_map_identity {A : Type u} (s : Stream A) : Stream'.map id s = s := rfl

theorem stream_extensionality {A : Type u} (s t : Stream A) (h : ∀ n, s n = t n) : s = t :=
  funext h

theorem interval_endpoints {A : Type u} [LinearOrder A] (i : ClosedInterval A) :
    i.contains i.lower ∧ i.contains i.upper := ⟨⟨le_rfl, i.ordered⟩, ⟨i.ordered, le_rfl⟩⟩

theorem join_commutative {A : Type u} [JoinSemilattice A] (x y : A) : x ⊔ y = y ⊔ x := sup_comm x y

theorem join_idempotent {A : Type u} [JoinSemilattice A] (x : A) : x ⊔ x = x := sup_idem x

theorem crdt_merge_idempotent {S : Type u} [SemilatticeSup S] (x : S) :
    StateBasedCRDT.merge x x = x := sup_idem x

theorem iterator_fused {A : Type u} (it j : FiniteIterator A)
    (h : it.next = (none, j)) : j.next = (none, j) := by
  unfold FiniteIterator.next at h ⊢
  split_ifs at h with hp
  · simp at h
  · have heq : it = j := (Prod.mk.inj h).2
    subst j
    simp [hp]

end CoreDataProofs
end Catalog
