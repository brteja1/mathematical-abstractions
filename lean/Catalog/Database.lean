module

public import Mathlib.Data.Finset.Basic
public import Mathlib.Data.Fintype.Basic

@[expose] public section

namespace Catalog
universe u v

structure RelationalSchema where
  Attribute : Type u
  finiteAttributes : Fintype Attribute
  Domain : Attribute → Type v

abbrev NamedTuple (s : RelationalSchema) := (a : s.Attribute) → s.Domain a
abbrev DatabaseRelation (s : RelationalSchema) := Finset (NamedTuple s)

def agreeOn {s : RelationalSchema} (X : _root_.Set s.Attribute)
    (a b : NamedTuple s) : Prop := ∀ k ∈ X, a k = b k

abbrev FD (s : RelationalSchema) := _root_.Set s.Attribute × _root_.Set s.Attribute

def FunctionalDependency {s : RelationalSchema} (r : DatabaseRelation s) (d : FD s) : Prop :=
  ∀ a ∈ r, ∀ b ∈ r, agreeOn d.1 a b → agreeOn d.2 a b

def impliesFD {s : RelationalSchema} (F : _root_.Set (FD s)) (d : FD s) : Prop :=
  ∀ r : DatabaseRelation s, (∀ premise ∈ F, FunctionalDependency r premise) →
    FunctionalDependency r d

def CandidateKey {s : RelationalSchema} (F : _root_.Set (FD s))
    (K : _root_.Set s.Attribute) : Prop :=
  impliesFD F (K, _root_.Set.univ) ∧
    ∀ J, J ⊂ K → ¬ impliesFD F (J, _root_.Set.univ)

end Catalog
