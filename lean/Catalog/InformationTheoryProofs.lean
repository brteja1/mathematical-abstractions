module

public import Catalog.InformationTheory
public import Mathlib.InformationTheory.Hamming
public import Mathlib.InformationTheory.Coding.KraftMcMillan
public import Mathlib.InformationTheory.Coding.PrefixFree
public import Mathlib.LinearAlgebra.FiniteDimensional.Basic
public import Mathlib.LinearAlgebra.FiniteDimensional.Lemmas
public import Mathlib.LinearAlgebra.Dimension.Finite
public import Mathlib.Algebra.BigOperators.Ring.Finset
public import Mathlib.Tactic

@[expose] public section
noncomputable section
namespace Catalog.Information
open scoped BigOperators
variable {A B : Type} [Fintype A] [Fintype B]

/-- Output masses: normalization is derived, not supplied as an assumption. -/
def outputMass (p : Law A) (w : Channel A B) (b : B) : ℝ :=
  ∑ a, p.mass a * (w a).mass b

-- urn:csabs:law/StochasticChannel-output-normalized
theorem output_normalized (p : Law A) (w : Channel A B) :
    (∑ b, outputMass p w b) = 1 ∧ ∀ b, 0 ≤ outputMass p w b := by
  constructor
  · simp_rw [outputMass]
    rw [Finset.sum_comm]
    simp_rw [← Finset.mul_sum, Law.normalized, mul_one]
    exact p.normalized
  · intro b
    exact Finset.sum_nonneg fun a _ => mul_nonneg (p.nonnegative a) ((w a).nonnegative b)

def output (p : Law A) (w : Channel A B) : Law B where
  mass := outputMass p w
  nonnegative := (output_normalized p w).2
  normalized := (output_normalized p w).1

-- urn:csabs:law/DiscreteMemorylessChannel-product-normalized
omit [Fintype A] in
theorem block_normalized (w : Channel A B) (n : Nat) (x : Fin n → A) :
    (∑ y, blockKernel w n x y) = 1 := by
  classical
  unfold blockKernel
  rw [← Fintype.prod_sum]
  simp only [Law.normalized, Finset.prod_const_one]

def iidLaw (p : Law A) (n : Nat) : Law (Fin n → A) where
  mass x := ∏ i, p.mass (x i)
  nonnegative x := Finset.prod_nonneg fun i _ => p.nonnegative (x i)
  normalized := by
    classical
    rw [← Fintype.prod_sum]
    simp only [p.normalized, Finset.prod_const_one]

def blockLaw (w : Channel A B) (n : Nat) (x : Fin n → A) : Law (Fin n → B) where
  mass := blockKernel w n x
  nonnegative y := Finset.prod_nonneg fun i _ => (w (x i)).nonnegative (y i)
  normalized := block_normalized w n x

def joint (p : Law A) (w : Channel A B) : Law (A × B) where
  mass ab := p.mass ab.1 * (w ab.1).mass ab.2
  nonnegative ab := mul_nonneg (p.nonnegative ab.1) ((w ab.1).nonnegative ab.2)
  normalized := by simp [Fintype.sum_prod_type, ← Finset.mul_sum, Law.normalized]

def marginalX (p : Law (A × B)) : Law A where
  mass a := ∑ b, p.mass (a,b)
  nonnegative a := Finset.sum_nonneg fun b _ => p.nonnegative (a,b)
  normalized := by simpa only [Fintype.sum_prod_type] using p.normalized

def marginalY (p : Law (A × B)) : Law B where
  mass b := ∑ a, p.mass (a,b)
  nonnegative b := Finset.sum_nonneg fun a _ => p.nonnegative (a,b)
  normalized := by rw [Finset.sum_comm]; simpa only [Fintype.sum_prod_type] using p.normalized

def expectation (p : Law A) (f : A → ℝ) : ℝ := ∑ a, p.mass a * f a

def averageCost {n : Nat} (d : Cost A B) (x : Fin n → A) (z : Fin n → B) : ℝ :=
  (∑ i, d.value (x i) (z i)) / n

-- urn:csabs:law/DistortionMeasure-expected-block
-- An arbitrary joint block law: no independence hypothesis.
theorem expected_block (n : Nat) (_hn : 0 < n)
    (p : Law ((Fin n → A) × (Fin n → B))) (d : Cost A B) :
    expectation p (fun xz => averageCost d xz.1 xz.2) =
      (∑ i, expectation p (fun xz => d.value (xz.1 i) (xz.2 i))) / n := by
  simpa only [expectation, averageCost, mul_div_assoc, Finset.mul_sum, Finset.sum_div]
    using (Finset.sum_comm (s := Finset.univ) (t := Finset.univ)
      (f := fun (xz : (Fin n → A) × (Fin n → B)) (i : Fin n) =>
        p.mass xz * d.value (xz.1 i) (xz.2 i) / (n : ℝ)))

-- urn:csabs:law/HammingSpace-metric
-- Definitionally identical to Mathlib.hammingDist on the same carrier.
theorem hamming_metric {X : Type} [DecidableEq X] {n : Nat}
    (x y z : Fin n → X) :
    0 ≤ hamming x y ∧ (hamming x y = 0 ↔ x = y) ∧
      hamming x y = hamming y x ∧ hamming x z ≤ hamming x y + hamming y z :=
  ⟨Nat.zero_le _, hammingDist_eq_zero, hammingDist_comm _ _, hammingDist_triangle _ _ _⟩

-- urn:csabs:theorem/PrefixFreeCode-unique-decoding
-- Uses prefix-freeness and positive lengths, never a supplied unique-decoding conclusion.
theorem prefix_unique {M : Type} (f : PrefixCode M) :
    Function.Injective (fun s : List M => s.flatMap f.word) := by
  intro s
  induction s with
  | nil =>
    intro t h
    cases t with
    | nil => rfl
    | cons b t =>
      have : f.word b = [] := (List.append_eq_nil_iff.mp (show f.word b ++ t.flatMap f.word = [] from h.symm)).1
      exact (f.positive b this).elim
  | cons a s ih =>
    intro t h
    cases t with
    | nil =>
      have : f.word a = [] := (List.append_eq_nil_iff.mp (show f.word a ++ s.flatMap f.word = [] from h)).1
      exact (f.positive a this).elim
    | cons b t =>
      have hab : a = b := by
        rcases List.append_eq_append_iff.mp (show f.word a ++ s.flatMap f.word =
          f.word b ++ t.flatMap f.word from h) with ⟨u, hu, _⟩ | ⟨u, hu, _⟩
        · exact f.prefixFree a b ⟨u, hu.symm⟩
        · exact (f.prefixFree b a ⟨u, hu.symm⟩).symm
      subst b
      have hst := List.append_cancel_left (show f.word a ++ s.flatMap f.word =
        f.word a ++ t.flatMap f.word from h)
      exact congrArg (List.cons a) (ih hst)

def PrefixCode.toUnique {M : Type} (f : PrefixCode M) : UniqueCode M :=
  ⟨f.word, f.positive, prefix_unique f⟩

section Linear
variable {F : Type} [Field F] [Fintype F] {n k : Nat}

def generatorEncode (g : Generator F n k) : (Fin k → F) ≃ₗ[F] g.code.space :=
  g.basis.equivFun.symm

-- urn:csabs:theorem/GeneratorMatrix-encoding-isomorphism
theorem generator_bijective (g : Generator F n k) :
    Function.Bijective (generatorEncode g) ∧
      (∀ x y, generatorEncode g (x+y) = generatorEncode g x + generatorEncode g y) ∧
      (∀ (a : F) x, generatorEncode g (a • x) = a • generatorEncode g x) :=
  ⟨(generatorEncode g).bijective, (generatorEncode g).map_add, (generatorEncode g).map_smul⟩

-- urn:csabs:theorem/Syndrome-coset-invariance
theorem syndrome_coset (h : CheckMatrix F n k) (y z c e : Fin n → F) (hc : c ∈ h.code.space) :
    (h.checkMap y = 0 ↔ y ∈ h.code.space) ∧
    (h.checkMap y = h.checkMap z ↔ y-z ∈ h.code.space) ∧
    h.checkMap (c+e) = h.checkMap e := by
  have mem (x : Fin n → F) : h.checkMap x = 0 ↔ x ∈ h.code.space := by
    rw [← h.kernel]; rfl
  refine ⟨mem y, ?_, ?_⟩
  · rw [← mem, map_sub, sub_eq_zero]
  · rw [map_add, (mem c).mpr hc, zero_add]

/-- Concrete failure of the zero/linear-combination closure criterion. -/
def NonlinearWitness (C : Set (Fin n → F)) : Prop :=
  (0 : Fin n → F) ∉ C ∨ ∃ a b : F, ∃ u ∈ C, ∃ v ∈ C, a • u + b • v ∉ C

-- urn:csabs:theorem/NonlinearBlockCode-witness-exists
omit [Fintype F] in
theorem nonlinear_witness (C : Set (Fin n → F)) :
    (¬ ∃ S : Submodule F (Fin n → F), (S : Set (Fin n → F)) = C) ↔
      NonlinearWitness C := by
  classical
  constructor
  · intro hn
    by_contra hw
    have hz : (0 : Fin n → F) ∈ C := by
      have hp := (show ((0 : Fin n → F) ∈ C) ∧ (∀ a b : F, ∀ u ∈ C, ∀ v ∈ C, a • u + b • v ∈ C) by simpa [NonlinearWitness] using hw)
      exact hp.1
    have hclosed : ∀ a b : F, ∀ u ∈ C, ∀ v ∈ C, a • u + b • v ∈ C := by
      have hp := (show ((0 : Fin n → F) ∈ C) ∧ (∀ a b : F, ∀ u ∈ C, ∀ v ∈ C, a • u + b • v ∈ C) by simpa [NonlinearWitness] using hw)
      exact hp.2
    let S : Submodule F (Fin n → F) := {
      carrier := C
      zero_mem' := hz
      add_mem' := by intro u v hu hv; simpa using hclosed 1 1 u hu v hv
      smul_mem' := by intro a u hu; simpa using hclosed a 0 u hu 0 hz }
    exact hn ⟨S, rfl⟩
  · rintro hw ⟨S, rfl⟩
    rcases hw with hz | ⟨a,b,u,hu,v,hv,hfail⟩
    · exact hz S.zero_mem
    · exact hfail (S.add_mem (S.smul_mem a hu) (S.smul_mem b hv))
end Linear
end Catalog.Information
