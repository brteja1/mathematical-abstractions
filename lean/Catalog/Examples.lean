module

public import Catalog.Algebra

@[expose] public section

namespace Catalog.Examples

/-- A worked proof from the group interface. Not a new catalog fact until it is
reviewed, sourced, recorded in Markdown and registered as a witness. -/
theorem inverse_involutive {A : Type*} [Catalog.Group A] (a : A) : (a⁻¹)⁻¹ = a := by
  have h : a⁻¹ * (a⁻¹)⁻¹ = a⁻¹ * a := by
    rw [mul_inv_cancel, inv_mul_cancel]
  exact mul_left_cancel h

end Catalog.Examples
