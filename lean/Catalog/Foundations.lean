module

public import Mathlib.SetTheory.ZFC.Basic
public import Mathlib.Data.Finset.Card
public import Mathlib.Data.Fintype.Card
public import Mathlib.Data.Set.Function

@[expose] public section

/-! Typed interpretations of the catalog. These definitions do not change graph facts.
`ZFSet` is Mathlib's universe-indexed set model, not an assertion of ZF consistency.
Function equality uses Lean equality and, where needed, function extensionality. -/
namespace Catalog
universe u v

abbrev Set := ZFSet
abbrev Relation (A : Type u) (B : Type v) := A → B → Prop
abbrev Function (A : Type u) (B : Type v) := A → B
abbrev PartialFunction (A : Type u) (B : Type v) := A → Option B
abbrev CartesianProduct (A : Type u) (B : Type v) := A × B
abbrev PowerSet (A : Type u) := _root_.Set A
abbrev FunctionType (A : Type u) (B : Type v) := A → B
abbrev ProductType (A : Type u) (B : Type v) := A × B
abbrev SumType (A : Type u) (B : Type v) := A ⊕ B
abbrev OptionType (A : Type u) := Option A
abbrev EmptyType := Empty
abbrev UnitType := Unit
abbrev EquivalenceRelation (A : Type u) := Setoid A

/-- Blocks are nonempty, disjoint, and cover even when the carrier is empty. -/
structure Partition (A : Type u) where
  blocks : _root_.Set (_root_.Set A)
  nonempty : ∀ b ∈ blocks, b.Nonempty
  cover : ∀ x, ∃ b ∈ blocks, x ∈ b
  disjoint : ∀ b ∈ blocks, ∀ c ∈ blocks, b ≠ c → Disjoint b c

/-- The proposition to prove, not an axiom postulating the pigeonhole principle. -/
def PigeonholePrinciple (A B : Type u) [Fintype A] [Fintype B] : Prop :=
  ∀ f : A → B, Fintype.card B < Fintype.card A →
    ∃ x y, x ≠ y ∧ f x = f y

/-- Representative finitary inductive tree; the eliminator is the proof principle.
General user datatypes should use their own generated recursor. -/
inductive InductiveTree (A : Type u) where
  | leaf : A → InductiveTree A
  | branch : InductiveTree A → InductiveTree A → InductiveTree A

def StructuralInduction (A : Type u) : Prop :=
  ∀ P : InductiveTree A → Prop,
    (∀ a, P (.leaf a)) →
    (∀ s t, P s → P t → P (.branch s t)) → ∀ t, P t

end Catalog
