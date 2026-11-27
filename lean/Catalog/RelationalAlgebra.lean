module

public import Catalog.Database
public import Mathlib.Data.Finset.Prod

@[expose] public section

namespace Catalog.RelationalAlgebra
universe u v
variable {A : Type u} {B : Type v}

noncomputable def intersection (r s : Finset A) : Finset A := by
  classical
  exact r ∩ s

noncomputable def difference (r s : Finset A) : Finset A := by
  classical
  exact r \ s

def product (r : Finset A) (s : Finset B) : Finset (A × B) := r.product s

noncomputable def thetaJoin (p : A × B → Prop) (r : Finset A) (s : Finset B) :
    Finset (A × B) := by
  classical
  exact (product r s).filter p

noncomputable def projectLeft (r : Finset (A × B)) : Finset A := by
  classical
  exact r.image Prod.fst

noncomputable def divide (r : Finset (A × B)) (s : Finset B) : Finset A := by
  classical
  exact (projectLeft r).filter (fun x => ∀ y ∈ s, (x, y) ∈ r)

/-- Satisfaction of the added basis, for disjoint whole-tuple blocks A and B. -/
theorem model_satisfaction (r t : Finset A) (s : Finset B) (q : Finset (A × B))
    (p : A × B → Prop) (x : A) (y : B) :
    (x ∈ intersection r t ↔ x ∈ r ∧ x ∈ t) ∧
    (x ∈ difference r t ↔ x ∈ r ∧ x ∉ t) ∧
    ((x, y) ∈ product r s ↔ x ∈ r ∧ y ∈ s) ∧
    ((x, y) ∈ thetaJoin p r s ↔ x ∈ r ∧ y ∈ s ∧ p (x, y)) ∧
    (x ∈ divide q s ↔ x ∈ projectLeft q ∧ ∀ z ∈ s, (x, z) ∈ q) := by
  classical
  simp [intersection, difference, product, thetaJoin, divide, and_assoc]

theorem division_empty (r : Finset (A × B)) (s : Finset B) :
    divide r (∅ : Finset B) = projectLeft r ∧ divide (∅ : Finset (A × B)) s = ∅ := by
  classical
  simp [divide, projectLeft]

theorem division_elimination (r : Finset (A × B)) (s : Finset B) :
    divide r s = difference (projectLeft r)
      (projectLeft (difference (product (projectLeft r) s) r)) := by
  classical
  ext x
  simp only [divide, difference, projectLeft, product, Finset.mem_filter,
    Finset.mem_sdiff, Finset.mem_image, Finset.product_eq_sprod, Finset.mem_product]
  constructor
  · rintro ⟨hx, hall⟩
    refine ⟨hx, ?_⟩
    rintro ⟨⟨a, b⟩, ⟨⟨_, hb⟩, hab⟩, hax⟩
    change a = x at hax
    subst a
    exact hab (hall b hb)
  · rintro ⟨hx, hbad⟩
    refine ⟨hx, ?_⟩
    intro b hb
    by_contra hab
    exact hbad ⟨(x, b), ⟨⟨hx, hb⟩, hab⟩, rfl⟩

end Catalog.RelationalAlgebra
