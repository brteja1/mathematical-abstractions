module

public import Mathlib.Data.Finsupp.Defs
public import Mathlib.Data.List.Nodup
public import Mathlib.Data.Multiset.Basic
public import Mathlib.Data.Finset.Basic

@[expose] public section

namespace Catalog
universe u v

abbrev Sequence (A : Type u) := List A
abbrev Array (A : Type u) (n : Nat) := Fin n → A

def Array.store {A : Type u} {n : Nat} (a : Catalog.Array A n) (i : Fin n) (x : A) :=
  _root_.Function.update a i x
abbrev FiniteSet (A : Type u) := Finset A
abbrev Multiset (A : Type u) := _root_.Multiset A
abbrev OrderedSet (A : Type u) := {xs : List A // xs.Nodup}

/-- Absence is Option.none; support finiteness is an explicit invariant. -/
structure Map (K : Type u) (V : Type v) where
  lookup : K → Option V
  finite_domain : {k | (lookup k).isSome}.Finite

abbrev Stack (A : Type u) := List A
abbrev Queue (A : Type u) := List A
abbrev Deque (A : Type u) := List A

namespace Stack
def push {A : Type u} (s : Catalog.Stack A) (x : A) := x :: s
def pop {A : Type u} : Catalog.Stack A → Option (Catalog.Stack A × A)
  | [] => none
  | x :: xs => some (xs, x)
def top {A : Type u} : Catalog.Stack A → Option A := List.head?
end Stack

namespace Queue
def enqueue {A : Type u} (q : Catalog.Queue A) (x : A) := q ++ [x]
def dequeue {A : Type u} : Catalog.Queue A → Option (Catalog.Queue A × A) := Stack.pop
end Queue

namespace Deque
def pushFront {A : Type u} (q : Catalog.Deque A) (x : A) := x :: q
def pushBack {A : Type u} (q : Catalog.Deque A) (x : A) := q ++ [x]
def popFront {A : Type u} : Catalog.Deque A → Option (Catalog.Deque A × A) := Stack.pop
def popBack {A : Type u} (q : Catalog.Deque A) : Option (Catalog.Deque A × A) :=
  (Stack.pop q.reverse).map fun (xs, x) => (xs.reverse, x)
end Deque

/-- Extraction is relational, so equal-priority choices stay unspecified. -/
abbrev PriorityQueue (A : Type u) := _root_.Multiset A

def extractMin {A : Type u} {K : Type v} [LinearOrder K] (priority : A → K)
    (q q' : PriorityQueue A) (x : A) : Prop :=
  q = x ::ₘ q' ∧ ∀ y ∈ q, priority x ≤ priority y

end Catalog
