module

public import Catalog.DataStructures
public import Catalog.BinaryTree
public import Mathlib.Data.List.Pairwise
public import Mathlib.Data.Set.Finite.Basic
public import Mathlib.Data.PNat.Basic

@[expose] public section

namespace Catalog
universe u v w

/-- Set-valued finite relation; duplicate key/value pairs are absent. -/
abbrev Multimap (K : Type u) (V : Type v) := Finset (K × V)

noncomputable def Multimap.values {K : Type u} {V : Type v} (m : Multimap K V) (k : K) : Finset V := by
  classical
  exact (m.filter fun entry => entry.1 = k).image Prod.snd

noncomputable def finiteMapSet {K : Type u} {V : Type v}
    (m : Catalog.Map K V) (k : K) (v : V) : Catalog.Map K V := by
  classical
  refine ⟨_root_.Function.update m.lookup k (some v), ?_⟩
  apply (m.finite_domain.insert k).subset
  intro a ha
  by_cases h : a = k
  · exact Or.inl h
  · exact Or.inr (by simpa [_root_.Function.update_of_ne h] using ha)

noncomputable def finiteMapErase {K : Type u} {V : Type v}
    (m : Catalog.Map K V) (k : K) : Catalog.Map K V := by
  classical
  refine ⟨_root_.Function.update m.lookup k none, ?_⟩
  apply m.finite_domain.subset
  intro a ha
  by_cases h : a = k
  · simp [h] at ha
  · simpa [_root_.Function.update_of_ne h] using ha

abbrev HeapStore (V : Type u) := Catalog.Map PNat V

noncomputable def HeapStore.write {V : Type u} (h : HeapStore V) (a : PNat) (v : V) : Option (HeapStore V) :=
  match h.lookup a with
  | none => none
  | some _ => some (finiteMapSet h a v)

noncomputable def HeapStore.free {V : Type u} (h : HeapStore V) (a : PNat) : Option (HeapStore V) :=
  match h.lookup a with
  | none => none
  | some _ => some (finiteMapErase h a)

def HeapStore.allocates {V : Type u} (h : HeapStore V) (v : V) (a : PNat) (out : HeapStore V) : Prop :=
  h.lookup a = none ∧ out = finiteMapSet h a v

/-- Observable representative of each equivalence class. Parent pointers and
path compression are implementation refinements, not part of this carrier. -/
structure DisjointSet (n : Nat) where
  representative : Fin n → Fin n
  idempotent : ∀ x, representative (representative x) = representative x

def DisjointSet.connected {n : Nat} (d : DisjointSet n) (x y : Fin n) : Prop :=
  d.representative x = d.representative y

def DisjointSet.unites {n : Nat} (d : DisjointSet n) (a b : Fin n) (out : DisjointSet n) : Prop :=
  ∃ chosen, (chosen = d.representative a ∨ chosen = d.representative b) ∧
    ∀ x, out.representative x =
      if d.representative x = d.representative a ∨ d.representative x = d.representative b then chosen else d.representative x

inductive RoseTree (A : Type u) where
  | node : A → List (RoseTree A) → RoseTree A

/-- Raw B-tree shape only: key lists at nodes and ordered children.
Occupancy, search ordering, equal leaf depth and updates are not formalized. -/
abbrev BTreeShape (A : Type u) := RoseTree (List A)

def RoseTree.root {A : Type u} : RoseTree A → A
  | .node a _ => a

def RoseTree.children {A : Type u} : RoseTree A → List (RoseTree A)
  | .node _ children => children

/-- Finite first-order, binder-free terms over ranked operators and variables. -/
inductive TermAlgebra (Op : Type u) (arity : Op → Nat) (Var : Type v) where
  | variable : Var → TermAlgebra Op arity Var
  | app (op : Op) : (Fin (arity op) → TermAlgebra Op arity Var) → TermAlgebra Op arity Var

def TermAlgebra.eval {Op : Type u} {arity : Op → Nat} {Var : Type v} {B : Type w}
    (valuation : Var → B) (operators : ∀ o, (Fin (arity o) → B) → B) : TermAlgebra Op arity Var → B
  | .variable v => valuation v
  | .app o children => operators o (fun i => eval valuation operators (children i))

structure BinarySearchTree (A : Type u) [LinearOrder A] where
  tree : Catalog.BinaryTree A
  ordered : (Catalog.BinaryTree.inorder tree).Pairwise (· < ·)

def BinarySearchTree.member {A : Type u} [LinearOrder A] (t : BinarySearchTree A) (x : A) : Prop :=
  x ∈ Catalog.BinaryTree.inorder t.tree

/-- An array-position min heap: finite complete shape, ties allowed. -/
structure BinaryHeap (A : Type u) (K : Type v) [LinearOrder K] (priority : A → K) where
  items : List A
  ordered : ∀ (i : Fin items.length), 0 < i.val →
    priority (items.get ⟨(i.val - 1) / 2, by have := i.isLt; omega⟩) ≤ priority (items.get i)

abbrev Trie (A : Type u) (V : Type v) := Catalog.Map (List A) V

noncomputable def Trie.prefixed {A : Type u} {V : Type v} (t : Trie A V) (p : List A) : Trie A V := by
  classical
  refine ⟨fun key => if ∃ suffix, key = p ++ suffix then t.lookup key else none, ?_⟩
  apply t.finite_domain.subset
  intro key h
  change (if ∃ suffix, key = p ++ suffix then t.lookup key else none).isSome = true at h
  split_ifs at h with hp
  · exact h
  · simp at h

namespace StructuredDataProofs

theorem disjoint_set_find_idempotent {n : Nat} (d : DisjointSet n) (x : Fin n) :
    d.representative (d.representative x) = d.representative x := d.idempotent x

theorem disjoint_set_connected_symmetric {n : Nat} (d : DisjointSet n) (x y : Fin n)
    (h : d.connected x y) : d.connected y x := h.symm

theorem rose_root {A : Type u} (a : A) (children : List (RoseTree A)) :
    RoseTree.root (.node a children) = a := rfl

theorem rose_eta {A : Type u} (t : RoseTree A) :
    RoseTree.node t.root t.children = t := by cases t; rfl

theorem term_eval_variable {Op : Type u} {arity : Op → Nat} {Var : Type v} {B : Type w}
    (valuation : Var → B) (operators : ∀ o, (Fin (arity o) → B) → B) (x : Var) :
    TermAlgebra.eval valuation operators (.variable x : TermAlgebra Op arity Var) = valuation x := rfl

theorem map_set_lookup_same {K : Type u} {V : Type v} (m : Catalog.Map K V) (k : K) (v : V) :
    (finiteMapSet m k v).lookup k = some v := by
  classical
  simp [finiteMapSet]

end StructuredDataProofs
end Catalog
