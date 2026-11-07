module

public import Catalog.Algebra
public import Catalog.Foundations
public import Catalog.DataStructures
public import Catalog.Order
public import Catalog.Semantics
public import Catalog.Numeric

@[expose] public section

/-! Proofs bound to existing catalog claims in bindings.json. The manifest pins
the expected proposition and maps each catalog premise to the chosen interface. -/
namespace Catalog.Proofs
universe u v w x

theorem semigroup_four_factor {A : Type u} [Catalog.Semigroup A] (a b c d : A) :
    ((a * b) * c) * d = (a * b) * (c * d) ∧
    (a * b) * (c * d) = a * (b * (c * d)) :=
  ⟨mul_assoc _ _ _, mul_assoc _ _ _⟩

theorem group_inverse_product {A : Type u} [Catalog.Group A] (a b : A) :
    (a * b)⁻¹ = b⁻¹ * a⁻¹ := mul_inv_rev a b

theorem group_cancellation {A : Type u} [Catalog.Group A] (a x y : A) :
    (a * x = a * y → x = y) ∧ (x * a = y * a → x = y) :=
  ⟨mul_left_cancel, mul_right_cancel⟩

theorem monoid_identity_unique {A : Type u} [Catalog.Monoid A] (e e' : A)
    (he : (∀ x, e * x = x) ∧ (∀ x, x * e = x))
    (he' : (∀ x, e' * x = x) ∧ (∀ x, x * e' = x)) : e = e' := by
  calc
    e = e * e' := (he'.2 e).symm
    _ = e' := he.1 e'

theorem monoid_power_addition {A : Type u} [Catalog.Monoid A] (a : A) (m n : Nat) :
    a ^ 0 = 1 ∧ a ^ (n + 1) = a ^ n * a ∧ a ^ (m + n) = a ^ m * a ^ n :=
  ⟨pow_zero a, pow_succ a n, pow_add a m n⟩

theorem stack_push_top {A : Type u} (s : Catalog.Stack A) (x : A) :
    Catalog.Stack.top (Catalog.Stack.push s x) = some x := rfl

theorem stack_push_pop {A : Type u} (s : Catalog.Stack A) (x : A) :
    Catalog.Stack.pop (Catalog.Stack.push s x) = some (s, x) := rfl

theorem stack_push_injective {A : Type u} (s t : Catalog.Stack A) (x y : A)
    (h : Catalog.Stack.push s x = Catalog.Stack.push t y) : s = t ∧ x = y := by
  cases h
  exact ⟨rfl, rfl⟩

theorem array_read_same {A : Type u} {n : Nat} (a : Catalog.Array A n) (i : Fin n) (x : A) :
    Catalog.Array.store a i x i = x := by simp [Catalog.Array.store]

theorem array_read_other {A : Type u} {n : Nat} (a : Catalog.Array A n)
    (i j : Fin n) (x : A) (h : i ≠ j) : Catalog.Array.store a i x j = a j := by
  simp [Catalog.Array.store, Ne.symm h]

theorem array_overwrite {A : Type u} {n : Nat} (a : Catalog.Array A n)
    (i : Fin n) (x y : A) :
    Catalog.Array.store (Catalog.Array.store a i x) i y = Catalog.Array.store a i y := by
  funext j
  by_cases h : j = i <;> simp [Catalog.Array.store, h]

theorem function_composition_associative {A : Type u} {B : Type v} {C : Type w} {D : Type x}
    (f : A → B) (g : B → C) (h : C → D) :
    (h ∘ (g ∘ f)) = ((h ∘ g) ∘ f) := rfl

theorem function_composition_injective {A : Type u} {B : Type v} {C : Type w}
    (f : A → B) (g : B → C) (hf : _root_.Function.Injective f)
    (hg : _root_.Function.Injective g) : _root_.Function.Injective (g ∘ f) :=
  fun _ _ h => hf (hg h)

theorem hoare_sequence {S : Type u} (P R Q : S → Prop) (C D : Catalog.Command S)
    (hC : Catalog.HoareTriple P C R) (hD : Catalog.HoareTriple R D Q) :
    Catalog.HoareTriple P (Catalog.seq C D) Q := by
  intro s t hp h
  obtain ⟨m, hcm, hdm⟩ := h
  exact hD m t (hC s m hp hcm) hdm

theorem hoare_consequence {S : Type u} (P' P Q Q' : S → Prop) (C : Catalog.Command S)
    (hP : ∀ s, P' s → P s) (hC : Catalog.HoareTriple P C Q)
    (hQ : ∀ s, Q s → Q' s) : Catalog.HoareTriple P' C Q' :=
  fun s t hp hc => hQ t (hC s t (hP s hp) hc)

theorem natural_zero_addition (n : Catalog.NaturalNumber) : 0 + n = n := Nat.zero_add n

theorem order_extensionality {A : Type u} [Catalog.PartialOrder A] (x y : A)
    (h : ∀ z, x ≤ z ↔ y ≤ z) : x = y :=
  le_antisymm ((h y).mpr le_rfl) ((h x).mp le_rfl)

end Catalog.Proofs
