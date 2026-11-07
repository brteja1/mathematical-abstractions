module

public import Mathlib.Data.Tree.Basic
public import Mathlib.Data.List.Basic
public import Lean.Elab.Tactic.Omega

@[expose] public section

namespace Catalog
universe u v w

/-- Finite ordered node-labelled binary trees, including the empty tree.
Labels may repeat; no ordering or balance invariant is imposed. -/
abbrev BinaryTree (A : Type u) := _root_.BinaryTree A

namespace BinaryTree

abbrev empty {A : Type u} : Catalog.BinaryTree A := .nil
abbrev node {A : Type u} (a : A) (l r : Catalog.BinaryTree A) : Catalog.BinaryTree A :=
  _root_.BinaryTree.node a l r

def view {A : Type u} : Catalog.BinaryTree A → Option (A × Catalog.BinaryTree A × Catalog.BinaryTree A)
  | .nil => none
  | _root_.BinaryTree.node a l r => some (a, l, r)

def fold {A : Type u} {B : Type v} (z : B) (k : A → B → B → B) : Catalog.BinaryTree A → B
  | .nil => z
  | _root_.BinaryTree.node a l r => k a (fold z k l) (fold z k r)

abbrev size {A : Type u} : Catalog.BinaryTree A → Nat := _root_.BinaryTree.numNodes
abbrev height {A : Type u} : Catalog.BinaryTree A → Nat := _root_.BinaryTree.height
/-- Count occurrences of empty child positions, including one for empty itself.
This does not count the labelled nodes having no nonempty children. -/
abbrev externalLeaves {A : Type u} : Catalog.BinaryTree A → Nat := _root_.BinaryTree.numLeaves
abbrev map {A : Type u} {B : Type v} (f : A → B) := _root_.BinaryTree.map f

def inorder {A : Type u} : Catalog.BinaryTree A → List A
  | .nil => []
  | _root_.BinaryTree.node a l r => inorder l ++ [a] ++ inorder r

def mirror {A : Type u} : Catalog.BinaryTree A → Catalog.BinaryTree A
  | .nil => .nil
  | _root_.BinaryTree.node a l r => _root_.BinaryTree.node a (mirror r) (mirror l)

namespace Proofs

theorem map_identity {A : Type u} (t : Catalog.BinaryTree A) : map id t = t :=
  _root_.BinaryTree.id_map t

theorem map_composition {A : Type u} {B : Type v} {C : Type w}
    (f : A → B) (g : B → C) (t : Catalog.BinaryTree A) :
    map (g ∘ f) t = map g (map f t) := _root_.BinaryTree.comp_map f g t

theorem mirror_involution {A : Type u} (t : Catalog.BinaryTree A) : mirror (mirror t) = t := by
  induction t with
  | nil => rfl
  | node a l r hl hr => simp only [mirror, hl, hr]

theorem size_zero_iff_empty {A : Type u} (t : Catalog.BinaryTree A) : size t = 0 ↔ t = empty := by
  cases t <;> simp [size, empty]

theorem fold_unique {A : Type u} {B : Type v} (z : B) (k : A → B → B → B)
    (g : Catalog.BinaryTree A → B) (he : g empty = z)
    (hn : ∀ a l r, g (node a l r) = k a (g l) (g r)) : g = fold z k := by
  funext t
  induction t with
  | nil => exact he
  | node a l r hl hr =>
    change g (node a l r) = k a (fold z k l) (fold z k r)
    rw [hn, hl, hr]

theorem inorder_length {A : Type u} (t : Catalog.BinaryTree A) : (inorder t).length = size t := by
  induction t with
  | nil => rfl
  | node a l r hl hr =>
    simp only [inorder, List.length_append, List.length_singleton, size, _root_.BinaryTree.numNodes] at *
    omega

theorem mirror_size {A : Type u} (t : Catalog.BinaryTree A) : size (mirror t) = size t := by
  induction t with
  | nil => rfl
  | node a l r hl hr => simp [mirror, size, hl, hr, Nat.add_comm]

theorem mirror_height {A : Type u} (t : Catalog.BinaryTree A) : height (mirror t) = height t := by
  induction t with
  | nil => rfl
  | node a l r hl hr => simp [mirror, height, hl, hr, Nat.max_comm]

theorem inorder_mirror {A : Type u} (t : Catalog.BinaryTree A) :
    inorder (mirror t) = (inorder t).reverse := by
  induction t with
  | nil => rfl
  | node a l r hl hr => simp [mirror, inorder, hl, hr, List.reverse_append, List.append_assoc]

theorem external_leaves_size {A : Type u} (t : Catalog.BinaryTree A) :
    externalLeaves t = size t + 1 := _root_.BinaryTree.numLeaves_eq_numNodes_succ t

theorem height_le_size {A : Type u} (t : Catalog.BinaryTree A) :
    height t ≤ size t := _root_.BinaryTree.height_le_numNodes t

end Proofs
end BinaryTree
end Catalog
