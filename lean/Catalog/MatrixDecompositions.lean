module

public import Catalog.Algebra
public import Mathlib.Analysis.RCLike.Basic
public import Mathlib.LinearAlgebra.Matrix.ConjTranspose
public import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
public import Lean.Elab.Tactic.Omega

@[expose] public section

noncomputable section
namespace Catalog
universe u v

/-- An exact factor witness for a supplied reconstruction map, not a solver. -/
structure MatrixDecomposition {F : Type u} [Field F] {m n : Nat}
    (W : Type v) (reconstruct : W → Catalog.Matrix F m n) (A : Catalog.Matrix F m n) where
  factors : W
  reconstructs : reconstruct factors = A

def matrixLower {F : Type u} [Zero F] {n : Nat}
    (L : _root_.Matrix (Fin n) (Fin n) F) : Prop := ∀ i j, i < j → L i j = 0

def matrixUpper {F : Type u} [Zero F] {m n : Nat}
    (R : _root_.Matrix (Fin m) (Fin n) F) : Prop := ∀ i j, j.val < i.val → R i j = 0

def rowPermute {F : Type u} {n : Nat} (p : Equiv.Perm (Fin n))
    (A : _root_.Matrix (Fin n) (Fin n) F) : _root_.Matrix (Fin n) (Fin n) F :=
  fun i j => A (p i) j

/-- Square row-pivoted LU: P A = L U, P acting as A(p i,j). -/
structure LUDecomposition {F : Type u} [Field F] {n : Nat} (A : Catalog.Matrix F n n) where
  permutation : Equiv.Perm (Fin n)
  lower : Catalog.Matrix F n n
  upper : Catalog.Matrix F n n
  lower_triangular : matrixLower lower
  unit_diagonal : ∀ i, lower i i = 1
  upper_triangular : matrixUpper upper
  reconstructs : rowPermute permutation A = lower * upper

/-- Full rectangular QR, without a diagonal phase/sign normalization. -/
structure QRDecomposition {F : Type u} [RCLike F] {m n : Nat} (A : Catalog.Matrix F m n) where
  orthogonal : Catalog.Matrix F m m
  upper : Catalog.Matrix F m n
  unitary_left : orthogonal.conjTranspose * orthogonal = 1
  unitary_right : orthogonal * orthogonal.conjTranspose = 1
  upper_trapezoidal : matrixUpper upper
  reconstructs : A = orthogonal * upper

def rectangularSingularDiagonal {F : Type u} [RCLike F] {m n : Nat}
    (sigma : Fin (min m n) → ℝ) : Catalog.Matrix F m n :=
  fun i j => if h : i.val = j.val then (sigma ⟨i.val, by omega⟩ : F) else 0

/-- Full SVD with sorted nonnegative real singular values, including zeros. -/
structure SVD {F : Type u} [RCLike F] {m n : Nat} (A : Catalog.Matrix F m n) where
  left : Catalog.Matrix F m m
  right : Catalog.Matrix F n n
  singularValues : Fin (min m n) → ℝ
  nonnegative : ∀ i, 0 ≤ singularValues i
  descending : ∀ i j, i ≤ j → singularValues j ≤ singularValues i
  left_unitary_left : left.conjTranspose * left = 1
  left_unitary_right : left * left.conjTranspose = 1
  right_unitary_left : right.conjTranspose * right = 1
  right_unitary_right : right * right.conjTranspose = 1
  reconstructs : A = left * rectangularSingularDiagonal singularValues * right.conjTranspose

/-- An eigenbasis witness; matrices lacking a full eigenbasis have no value here. -/
structure EigenDecomposition {F : Type u} [Field F] {n : Nat} (A : Catalog.Matrix F n n) where
  vectors : Catalog.Matrix F n n
  inverse : Catalog.Matrix F n n
  eigenvalues : Fin n → F
  inverse_left : inverse * vectors = 1
  inverse_right : vectors * inverse = 1
  reconstructs : A = vectors * _root_.Matrix.diagonal eigenvalues * inverse

/-- Hermitian positive definiteness stated with the real quadratic form. -/
def matrixHermitianPositiveDefinite {F : Type u} [RCLike F] {n : Nat}
    (A : Catalog.Matrix F n n) : Prop :=
  A.conjTranspose = A ∧ ∀ x : Fin n → F, x ≠ 0 →
    0 < RCLike.re (_root_.dotProduct (star x) (A.mulVec x))

/-- Lower Cholesky with positive real diagonal; no semidefinite variant. -/
structure CholeskyDecomposition {F : Type u} [RCLike F] {n : Nat}
    (A : Catalog.Matrix F n n) where
  lower : Catalog.Matrix F n n
  positive_definite : matrixHermitianPositiveDefinite A
  lower_triangular : matrixLower lower
  positive_real_diagonal : ∀ i, ∃ r : ℝ, 0 < r ∧ lower i i = (r : F)
  reconstructs : A = lower * lower.conjTranspose

namespace MatrixDecompositionProofs

theorem target_unique {F : Type u} [Field F] {m n : Nat} {W : Type v}
    {r : W → Catalog.Matrix F m n} {A B : Catalog.Matrix F m n}
    (d : MatrixDecomposition W r A) (e : MatrixDecomposition W r B)
    (h : d.factors = e.factors) : A = B := by
  rw [← d.reconstructs, h, e.reconstructs]

theorem lu_unpermute {F : Type u} [Field F] {n : Nat} {A : Catalog.Matrix F n n}
    (d : LUDecomposition A) : A = rowPermute d.permutation.symm (d.lower * d.upper) := by
  funext i j
  have h := congrFun (congrFun d.reconstructs (d.permutation.symm i)) j
  simpa only [rowPermute, Equiv.apply_symm_apply] using h

theorem qr_gram {F : Type u} [RCLike F] {m n : Nat} {A : Catalog.Matrix F m n}
    (d : QRDecomposition A) : A.conjTranspose * A = d.upper.conjTranspose * d.upper := by
  simp only [d.reconstructs, _root_.Matrix.conjTranspose_mul]
  calc
    d.upper.conjTranspose * d.orthogonal.conjTranspose * (d.orthogonal * d.upper) =
        d.upper.conjTranspose * (d.orthogonal.conjTranspose * d.orthogonal) * d.upper := by
      simp only [_root_.Matrix.mul_assoc]
    _ = d.upper.conjTranspose * d.upper := by rw [d.unitary_left, _root_.Matrix.mul_one]

theorem svd_coordinates {F : Type u} [RCLike F] {m n : Nat} {A : Catalog.Matrix F m n}
    (d : SVD A) : d.left.conjTranspose * A * d.right =
      rectangularSingularDiagonal d.singularValues := by
  simp only [d.reconstructs]
  calc
    d.left.conjTranspose * (d.left * rectangularSingularDiagonal (F := F) (m := m) (n := n) d.singularValues *
        d.right.conjTranspose) * d.right =
        (d.left.conjTranspose * d.left) * rectangularSingularDiagonal (F := F) (m := m) (n := n) d.singularValues *
          (d.right.conjTranspose * d.right) := by simp only [_root_.Matrix.mul_assoc]
    _ = rectangularSingularDiagonal (F := F) (m := m) (n := n) d.singularValues := by
      rw [d.left_unitary_left, d.right_unitary_left, _root_.Matrix.one_mul, _root_.Matrix.mul_one]

theorem eigen_basis_equation {F : Type u} [Field F] {n : Nat} {A : Catalog.Matrix F n n}
    (d : EigenDecomposition A) : A * d.vectors = d.vectors * _root_.Matrix.diagonal d.eigenvalues := by
  simp only [d.reconstructs, _root_.Matrix.mul_assoc, d.inverse_left, _root_.Matrix.mul_one]

theorem cholesky_determinant {F : Type u} [RCLike F] {n : Nat} {A : Catalog.Matrix F n n}
    (d : CholeskyDecomposition A) : A.det = d.lower.det * star d.lower.det := by
  simp only [d.reconstructs, _root_.Matrix.det_mul, _root_.Matrix.det_conjTranspose]

end MatrixDecompositionProofs
end Catalog
