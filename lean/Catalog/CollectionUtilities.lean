module

public import Catalog.DataStructures
public import Catalog.KleeneForests
public import Mathlib.Data.List.Dedup
public import Mathlib.Data.List.TakeDrop
public import Mathlib.Data.Finset.Card
public import Mathlib.Order.Lattice.Nat
public import Catalog.Audit

@[expose] public section
namespace Catalog
universe u v

theorem finiteSet_utilities {A : Type u} [DecidableEq A] (s t : Finset A)
    (p : A → Prop) [DecidablePred p] (x : A) :
    (x ∈ s ∪ t ↔ x ∈ s ∨ x ∈ t) ∧
    (x ∈ s ∩ t ↔ x ∈ s ∧ x ∈ t) ∧
    (x ∈ s \ t ↔ x ∈ s ∧ x ∉ t) ∧
    (s ⊆ t ↔ ∀ a ∈ s, a ∈ t) ∧
    (x ∈ s.filter p ↔ x ∈ s ∧ p x) ∧
    (s ∪ t).card + (s ∩ t).card = s.card + t.card := by
  exact ⟨Finset.mem_union, Finset.mem_inter, Finset.mem_sdiff,
    Iff.rfl, Finset.mem_filter, Finset.card_union_add_card_inter s t⟩

/-- Reverse last-occurrence deduplication to retain first occurrences. -/
def dedupFirst {A : Type u} [DecidableEq A] (xs : List A) : List A :=
  xs.reverse.dedup.reverse

theorem dedupFirst_properties {A : Type u} [DecidableEq A] (xs : List A) :
    (dedupFirst xs).Nodup ∧ (dedupFirst xs).Sublist xs ∧
    (∀ a, a ∈ dedupFirst xs ↔ a ∈ xs) ∧
    dedupFirst (dedupFirst xs) = dedupFirst xs := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · simp [dedupFirst, List.nodup_dedup]
  · simpa [dedupFirst] using (List.dedup_sublist xs.reverse).reverse
  · intro a; simp [dedupFirst]
  · simp [dedupFirst, List.dedup_idem]

theorem dedupFirst_first {A : Type u} [DecidableEq A] (a : A) (xs : List A) :
    dedupFirst (a :: xs) = a :: dedupFirst (xs.filter (fun b => b != a)) := by
  simp only [dedupFirst, List.reverse_cons]
  induction xs using List.reverseRecOn with
  | nil => simp
  | append_singleton xs b ih =>
    by_cases h : b = a
    · subst b; simp_all [List.dedup_cons_of_mem, List.filter_append]
    · simp_all [List.dedup_cons, List.filter_append, List.mem_append]
      split <;> rfl

theorem sequence_split {A : Type u} (xs : List A) (n : Nat) :
    xs.take n ++ xs.drop n = xs ∧
    (xs.take n).length = min n xs.length ∧
    (xs.drop n).length = xs.length - n := by
  exact ⟨List.take_append_drop n xs, List.length_take, List.length_drop⟩

theorem sequence_filter {A : Type u} (xs : List A) (p : A → Bool) (a : A) :
    a ∈ xs.filter p ↔ a ∈ xs ∧ p a = true := List.mem_filter

theorem sequence_find {A : Type u} (xs : List A) (p : A → Bool) :
    xs.find? p = (xs.filter p).head? := by
  induction xs with
  | nil => rfl
  | cons a xs ih => cases h : p a <;> simp only [List.find?_cons, List.filter_cons, h, Bool.false_eq_true, ite_false, ite_true, List.head?_cons, ih]

theorem sequence_relations {A : Type u} (xs ys : List A) :
    (List.IsPrefix xs ys ↔ ∃ zs, xs ++ zs = ys) ∧
    (List.IsSuffix xs ys ↔ ∃ zs, zs ++ xs = ys) ∧
    (List.IsInfix xs ys ↔ ∃ as bs, as ++ xs ++ bs = ys) := by
  exact ⟨Iff.rfl, Iff.rfl, Iff.rfl⟩

def mapOverride {K : Type u} {V : Type v} (m n : Map K V) : Map K V where
  lookup k := (n.lookup k).or (m.lookup k)
  finite_domain := by
    apply (m.finite_domain.union n.finite_domain).subset
    intro k hk
    cases hn : n.lookup k <;> simp_all

noncomputable def mapDiff {K : Type u} {V : Type v} (m n : Map K V) : Finset K := by
  classical
  exact (m.finite_domain.union n.finite_domain).toFinset.filter (fun k => m.lookup k ≠ n.lookup k)

theorem mapOverride_lookup {K : Type u} {V : Type v} (m n : Map K V) (k : K) :
    (mapOverride m n).lookup k = (n.lookup k).or (m.lookup k) := rfl

theorem mapDiff_membership {K : Type u} {V : Type v} (m n : Map K V) (k : K) :
    k ∈ mapDiff m n ↔ m.lookup k ≠ n.lookup k := by
  classical
  simp only [mapDiff, Finset.mem_filter, Set.Finite.mem_toFinset, Set.mem_union,
    Set.mem_ofPred_eq]
  constructor
  · exact And.right
  · intro h
    refine ⟨?_, h⟩
    cases hm : m.lookup k <;> cases hn : n.lookup k <;> simp_all

def kleeneAll (xs : List KleeneLogic) : KleeneLogic := xs.foldr kleeneAnd 2
def kleeneAny (xs : List KleeneLogic) : KleeneLogic := xs.foldr kleeneOr 0

theorem kleene_lattice (a b c : KleeneLogic) :
    kleeneAnd (kleeneAnd a b) c = kleeneAnd a (kleeneAnd b c) ∧
    kleeneOr (kleeneOr a b) c = kleeneOr a (kleeneOr b c) ∧
    kleeneAnd a b = kleeneAnd b a ∧ kleeneOr a b = kleeneOr b a ∧
    kleeneAnd a a = a ∧ kleeneOr a a = a ∧
    kleeneAnd a 2 = a ∧ kleeneAnd 2 a = a ∧
    kleeneOr a 0 = a ∧ kleeneOr 0 a = a := by
  fin_cases a <;> fin_cases b <;> fin_cases c <;> decide

theorem kleene_folds : kleeneAll [] = 2 ∧ kleeneAny [] = 0 ∧
    (∀ a xs, kleeneAll (a :: xs) = kleeneAnd a (kleeneAll xs)) ∧
    (∀ a xs, kleeneAny (a :: xs) = kleeneOr a (kleeneAny xs)) := by
  exact ⟨rfl, rfl, fun _ _ => rfl, fun _ _ => rfl⟩

def joinAll {A : Type u} [SemilatticeSup A] [OrderBot A] (xs : List A) : A :=
  xs.foldr (· ⊔ ·) ⊥

theorem join_associative {A : Type u} [SemilatticeSup A] (a b c : A) :
    (a ⊔ b) ⊔ c = a ⊔ (b ⊔ c) := sup_assoc a b c

theorem joinAll_lub {A : Type u} [SemilatticeSup A] [OrderBot A]
    (xs : List A) (z : A) : joinAll xs ≤ z ↔ ∀ a ∈ xs, a ≤ z := by
  induction xs with
  | nil => simp [joinAll]
  | cons a xs ih => simpa [joinAll, sup_le_iff] using and_congr Iff.rfl ih

theorem join_bottom_model :
    joinAll ([] : List Nat) = 0 ∧ joinAll [1, 3, 2] = 3 := by decide

theorem join_bottom_laws {A : Type u} [SemilatticeSup A] [OrderBot A] (a : A) :
    ⊥ ⊔ a = a ∧ a ⊔ ⊥ = a ∧ joinAll ([] : List A) = ⊥ :=
  ⟨bot_sup_eq a, sup_bot_eq a, rfl⟩

#catalog_witness finiteSet_utilities
#catalog_witness dedupFirst_properties
#catalog_witness dedupFirst_first
#catalog_witness sequence_split
#catalog_witness sequence_filter
#catalog_witness sequence_find
#catalog_witness sequence_relations
#catalog_witness mapOverride_lookup
#catalog_witness mapDiff_membership
#catalog_witness kleene_lattice
#catalog_witness kleene_folds
#catalog_witness join_associative
#catalog_witness joinAll_lub
#catalog_witness join_bottom_model
#catalog_witness join_bottom_laws
end Catalog
