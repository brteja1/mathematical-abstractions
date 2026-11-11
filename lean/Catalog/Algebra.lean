module

public import Mathlib.Algebra.Group.Basic
public import Mathlib.Algebra.Ring.Basic
public import Mathlib.Algebra.Field.Basic
public import Mathlib.LinearAlgebra.TensorProduct.Basic
public import Mathlib.LinearAlgebra.PiTensorProduct.Basic
public import Mathlib.LinearAlgebra.Dual.Defs
public import Mathlib.Data.Matrix.Basic
public import Mathlib.Algebra.Tropical.Basic
public import Mathlib.Basic.Real.Basic

@[expose] public section

namespace Catalog
universe u v w

/-- Nonempty is explicit: Mathlib's Semigroup alone permits an empty carrier. -/
class Semigroup (A : Type u) extends _root_.Semigroup A where
  carrier_nonempty : Nonempty A

abbrev Monoid (A : Type u) := _root_.Monoid A
abbrev Group (A : Type u) := _root_.Group A
abbrev Semiring (A : Type u) := _root_.Semiring A

/-- The catalog's unital convention permits zero = one. -/
class IdempotentSemiring (A : Type u) extends _root_.Semiring A where
  add_idem (a : A) : a + a = a

/-- Exact min-plus values; tropical zero is top and tropical one is real zero.
The library's transported order is numerical order, not the canonical semiring order. -/
abbrev MinPlusSemiring := MinTropical (WithTop ℝ)

noncomputable instance : IdempotentSemiring MinPlusSemiring where
  add_idem := MinTropical.add_self

def canonicalSemiringOrder {A : Type u} [IdempotentSemiring A] (a b : A) : Prop :=
  a + b = b

abbrev Ring (A : Type u) := _root_.Ring A
abbrev Field (A : Type u) := _root_.Field A

/-- Exact field structure with a finite carrier; no particular encoding is chosen.
Mathlib totalizes inverse at zero; the catalog interface restricts it to nonzero inputs. -/
class FiniteField (A : Type u) extends _root_.Field A where
  carrier_finite : Finite A

abbrev VectorSpace (F : Type u) (V : Type v) [_root_.Field F]
    [AddCommGroup V] := Module F V
abbrev LinearMap (F : Type u) (V : Type v) (W : Type w)
    [_root_.Field F] [AddCommGroup V] [AddCommGroup W]
    [Module F V] [Module F W] := V →ₗ[F] W
abbrev Matrix (F : Type u) [_root_.Field F] (m n : Nat) :=
  _root_.Matrix (Fin m) (Fin n) F
abbrev TensorProduct (F : Type u) (V W : Type v) [_root_.Field F]
    [AddCommGroup V] [AddCommGroup W] [Module F V] [Module F W] :=
  _root_.TensorProduct F V W

/-- Finite indexed tensor power. The empty product is canonically isomorphic
to the scalar field, rather than definitionally equal to it. -/
abbrev TensorPower (F V : Type u) [_root_.Field F] [AddCommGroup V] [Module F V]
    (n : Nat) := PiTensorProduct F (fun _ : Fin n => V)

abbrev Tensor (F V : Type u) [_root_.Field F] [AddCommGroup V] [Module F V]
    (p q : Nat) := _root_.TensorProduct F (TensorPower F V p)
      (TensorPower F (Module.Dual F V) q)

end Catalog
