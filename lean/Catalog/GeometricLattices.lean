module

public import Catalog.Algebra
public import Catalog.CoreData
public import Mathlib.LinearAlgebra.LinearIndependent.Defs
public import Mathlib.Data.ZMod.Basic

@[expose] public section

namespace Catalog

/-- Exact squared Euclidean length; this is not the sup norm on a Pi type. -/
def latticeSquaredNorm {d : Nat} (x : Fin d → ℝ) : ℝ :=
  ∑ i, x i ^ 2

/-- Independent real basis columns. Covolume, duality and discreteness
correspondence are not yet registered theorem witnesses. -/
structure EuclideanLattice (d r : Nat) where
  basis : Fin r → (Fin d → ℝ)
  independent : LinearIndependent ℝ basis

def EuclideanLattice.contains {d r : Nat} (lattice : EuclideanLattice d r)
    (x : Fin d → ℝ) : Prop :=
  ∃ z : Fin r → ℤ, x = fun i => ∑ j, (z j : ℝ) * lattice.basis j i

/-- A modular matrix defines a kernel; it is not a Euclidean lattice basis.
The conversion to an independent real basis remains a correspondence obligation. -/
structure QaryLattice (n m q : Nat) where
  rows_positive : 0 < n
  columns_positive : 0 < m
  modulus_valid : 2 ≤ q
  matrix : Fin n → Fin m → ZMod q

def QaryLattice.contains {n m q : Nat} (lattice : QaryLattice n m q)
    (z : Fin m → ℤ) : Prop :=
  ∀ i, (∑ j, lattice.matrix i j * (z j : ZMod q)) = 0

/-- Partial SVP interpretation with an explicit positive rank and factor.
The all-competitors squared inequality avoids assuming a minimizer as a field. -/
structure SVP (d r : Nat) where
  lattice : EuclideanLattice d r
  rank_positive : 0 < r
  factor : ℝ
  factor_valid : 1 ≤ factor

def SVP.admissible {d r : Nat} (problem : SVP d r) (v : Fin d → ℝ) : Prop :=
  problem.lattice.contains v ∧ v ≠ 0 ∧
    ∀ w, problem.lattice.contains w → w ≠ 0 →
      latticeSquaredNorm v ≤ problem.factor ^ 2 * latticeSquaredNorm w

/-- Partial CVP relation; ties and rank zero are admitted. No nearest-point
algorithm or attainment witness is supplied. -/
structure CVP (d r : Nat) where
  lattice : EuclideanLattice d r
  target : Fin d → ℝ
  factor : ℝ
  factor_valid : 1 ≤ factor

def CVP.admissible {d r : Nat} (problem : CVP d r) (v : Fin d → ℝ) : Prop :=
  problem.lattice.contains v ∧
    ∀ w, problem.lattice.contains w →
      latticeSquaredNorm (problem.target - v) ≤
        problem.factor ^ 2 * latticeSquaredNorm (problem.target - w)

/-- Partial deterministic SIS witness relation. The uniform matrix experiment
and its computational hardness are not formalized by this structure. -/
structure SIS (n m q : Nat) where
  lattice : QaryLattice n m q
  bound : ℝ
  bound_positive : 0 < bound
  bound_nontrivial : bound < q

def SIS.admissible {n m q : Nat} (problem : SIS n m q) (z : Fin m → ℤ) : Prop :=
  z ≠ 0 ∧ problem.lattice.contains z ∧
    latticeSquaredNorm (fun i => (z i : ℝ)) ≤ problem.bound ^ 2

/-- Partial modular-error carrier. Error mass is normalized by FiniteDistribution;
the uniform, independent, fixed-secret experiment is not yet constructed. -/
structure LWE (n q : Nat) where
  dimension_positive : 0 < n
  modulus_valid : 2 ≤ q
  errorLaw : FiniteDistribution (ZMod q)

def LWE.encode {n q : Nat} (_problem : LWE n q)
    (secret input : Fin n → ZMod q) (error : ZMod q) : ZMod q :=
  (∑ i, input i * secret i) + error

end Catalog
