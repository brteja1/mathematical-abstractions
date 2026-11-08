module

public import Catalog.Semantics
public import Mathlib.Data.Set.Finite.Basic

@[expose] public section

namespace Catalog
universe u v

/-- One resource, one mode per holder, with finite compatible holdings.
This carrier has no waiting queue, scheduler or language memory model. -/
structure Lock (P : Type u) (M : Type v) (compatible : M → M → Prop) where
  holders : P → Option M
  finite_holders : {p | (holders p).isSome}.Finite
  symmetric : ∀ a b, compatible a b → compatible b a
  pairwise : ∀ p q a b, p ≠ q → holders p = some a →
    holders q = some b → compatible a b

def Lock.canAcquire {P : Type u} {M : Type v} {C : M → M → Prop}
    (h : Lock P M C) (p : P) (m : M) : Prop :=
  h.holders p = none ∧ ∀ q a, h.holders q = some a → C m a

def Lock.acquires {P : Type u} {M : Type v} {C : M → M → Prop}
    (h : Lock P M C) (p : P) (m : M) (out : Lock P M C) : Prop := by
  classical
  exact h.canAcquire p m ∧ ∀ q, out.holders q = if q = p then some m else h.holders q

def Lock.releases {P : Type u} {M : Type v} {C : M → M → Prop}
    (h : Lock P M C) (p : P) (out : Lock P M C) : Prop := by
  classical
  exact (∃ m, h.holders p = some m) ∧
    ∀ q, out.holders q = if q = p then none else h.holders q

/-- Non-reentrant optional-owner carrier; partial operations are guarded relations. -/
abbrev Mutex (P : Type u) := Option P

def Mutex.acquires {P : Type u} (owner : Mutex P) (p : P) (out : Mutex P) : Prop :=
  owner = none ∧ out = some p

def Mutex.releases {P : Type u} (owner : Mutex P) (p : P) (out : Mutex P) : Prop :=
  owner = some p ∧ out = none

def Mutex.tryAcquire {P : Type u} (owner : Mutex P) (p : P) : Mutex P × Bool :=
  match owner with
  | none => (some p, true)
  | some q => (some q, false)

/-- Raw bakery data only. Program counters and local scan data are uninterpreted;
no protocol transition relation, reachability or exclusion proof is supplied. -/
structure LamportBakeryState (n : Nat) where
  choosing : Fin n → Bool
  number : Fin n → Nat
  pc : Fin n → Nat
  scanIndex : Fin n → Nat
  localReads : Fin n → Fin n → Nat

end Catalog
