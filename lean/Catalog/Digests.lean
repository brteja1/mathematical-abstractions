module

public import Mathlib.Data.Set.Function
public import Mathlib.Data.Fin.Basic

@[expose] public section

namespace Catalog

/-- A deterministic digest with a fixed, finite output space of size n. -/
abbrev DigestFunction (A : Type) (n : Nat) := A → Fin n

/-- The evidence applies only to the explicitly supplied set S. -/
structure CollisionFreeDigest (A : Type) (n : Nat) (S : Set A) where
  digest : DigestFunction A n
  collisionFree : Set.InjOn digest S

def exampleDigest : DigestFunction Nat 2 :=
  fun x => ⟨x % 2, Nat.mod_lt x (by decide)⟩

def exampleDigestScope : Set Nat := {x | x < 2}

theorem digest_model_satisfaction :
    (∀ (A : Type) (n : Nat) (h : DigestFunction A n) (x : A),
      ∃! d : Fin n, d = h x) ∧ exampleDigest 0 ≠ exampleDigest 1 := by
  constructor
  · intro A n h x
    exact ⟨h x, rfl, fun _ hd => hd⟩
  · decide

theorem scoped_digest_model_satisfaction :
    Set.InjOn exampleDigest exampleDigestScope ∧
    (0 ∈ exampleDigestScope ∧ 1 ∈ exampleDigestScope ∧ (0 : Nat) ≠ 1) ∧
    (2 ∉ exampleDigestScope ∧ exampleDigest 0 = exampleDigest 2) := by
  refine ⟨?_, ?_, ?_⟩
  · intro x hx y hy hxy
    have hv := congrArg Fin.val hxy
    change x % 2 = y % 2 at hv
    change x < 2 at hx
    change y < 2 at hy
    simpa only [Nat.mod_eq_of_lt hx, Nat.mod_eq_of_lt hy] using hv
  · change 0 < 2 ∧ 1 < 2 ∧ (0 : Nat) ≠ 1
    decide
  · change ¬2 < 2 ∧ exampleDigest 0 = exampleDigest 2
    decide

def exampleCollisionFreeDigest : CollisionFreeDigest Nat 2 exampleDigestScope :=
  ⟨exampleDigest, scoped_digest_model_satisfaction.1⟩

theorem scoped_digest_eq_iff {A : Type} {n : Nat} {S : Set A}
    (h : CollisionFreeDigest A n S) (x y : A) (hx : x ∈ S) (hy : y ∈ S) :
    h.digest x = h.digest y ↔ x = y :=
  h.collisionFree.eq_iff hx hy

theorem scoped_digest_subset {A : Type} {n : Nat} {S T : Set A}
    (h : CollisionFreeDigest A n S) (hTS : T ⊆ S) : Set.InjOn h.digest T :=
  h.collisionFree.mono hTS

end Catalog
