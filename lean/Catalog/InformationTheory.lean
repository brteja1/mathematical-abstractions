module

public import Catalog.Algebra
public import Mathlib.LinearAlgebra.Basis.Defs
public import Mathlib.Analysis.SpecialFunctions.Log.Basic
public import Mathlib.Order.ConditionallyCompleteLattice.Basic

@[expose] public section

noncomputable section

namespace Catalog
namespace Information

/-- Exact finite laws; normalized mass, not a sampling implementation. -/
structure Law (A : Type) [Fintype A] where
  mass : A → ℝ
  nonnegative : ∀ a, 0 ≤ mass a
  normalized : ∑ a, mass a = 1

noncomputable def logTwo (x : ℝ) : ℝ := Real.log x / Real.log 2

noncomputable def entropy {A : Type} [Fintype A] (p : Law A) : ℝ :=
  -∑ a, p.mass a * logTwo (p.mass a)

/-- Conditional entropy via finite joint/marginal log ratios; null joint masses vanish. -/
noncomputable def conditionalEntropy {A B : Type} [Fintype A] [Fintype B]
    (p : Law (A × B)) : ℝ :=
  -∑ a, ∑ b, p.mass (a, b) * logTwo (p.mass (a, b) / ∑ x, p.mass (x, b))

/-- None represents positive infinity. Finite branch is the exact KL sum.
The positivity and equality characterization are not registered witnesses. -/
noncomputable def divergence {A : Type} [Fintype A] (p q : Law A) : Option ℝ := by
  classical
  exact if ∃ a, 0 < p.mass a ∧ q.mass a = 0 then none
    else some (∑ a, p.mass a * logTwo (p.mass a / q.mass a))

noncomputable def mutualInformation {A B : Type} [Fintype A] [Fintype B]
    (p : Law (A × B)) : ℝ :=
  ∑ a, ∑ b, p.mass (a, b) *
    logTwo (p.mass (a, b) / ((∑ y, p.mass (a, y)) * (∑ x, p.mass (x, b))))

abbrev Channel (A B : Type) [Fintype B] := A → Law B

/-- Stationary product kernel weights, without assuming independent inputs. -/
noncomputable def blockKernel {A B : Type} [Fintype B]
    (w : Channel A B) (n : Nat) (x : Fin n → A) (y : Fin n → B) : ℝ :=
  ∏ i, (w (x i)).mass (y i)

/-- Information-expression side of capacity. Operational correspondence is not formalized. -/
noncomputable def informationCapacity {A B : Type} [Fintype A] [Fintype B]
    (w : Channel A B) : ℝ :=
  sSup {r | ∃ p : Law A, r = ∑ a, ∑ b, p.mass a * (w a).mass b *
    logTwo ((w a).mass b / ∑ x, p.mass x * (w x).mass b)}

structure UniqueCode (M : Type) where
  word : M → List Bool
  positive : ∀ m, word m ≠ []
  unique : Function.Injective (fun s : List M => s.flatMap word)

structure PrefixCode (M : Type) where
  word : M → List Bool
  positive : ∀ m, word m ≠ []
  prefixFree : ∀ a b, (word a).IsPrefix (word b) → a = b

structure Cost (A B : Type) where
  value : A → B → ℝ
  nonnegative : ∀ a b, 0 ≤ value a b

/-- Base reconstruction data. The constrained infimum and operational targets are defined
in InformationTheoryStatements; those coding targets are not registered proofs. -/
structure DistortionProblem (A B : Type) [Fintype A] [Fintype B] where
  sourceLaw : Law A
  cost : Cost A B
  budget : ℝ
  budget_nonnegative : 0 ≤ budget

def DistortionProblem.feasible {A B : Type} [Fintype A] [Fintype B]
    (problem : DistortionProblem A B) (w : Channel A B) : Prop :=
  (∑ a, ∑ b, problem.sourceLaw.mass a * (w a).mass b * problem.cost.value a b) ≤
    problem.budget

/-- Hamming distance counts unequal coordinates, with no field operations needed. -/
def hamming {A : Type} [DecidableEq A] {n : Nat} (x y : Fin n → A) : Nat :=
  (Finset.univ.filter (fun i => x i ≠ y i)).card

structure Code (A : Type) (n : Nat) where
  words : Finset (Fin n → A)
  nonempty : words.Nonempty
  length_positive : 0 < n

/-- Exact finite-field submodule carrier; length zero is excluded by the graph profile. -/
structure LinearCode (F : Type) [Field F] [Fintype F] (n : Nat) where
  space : Submodule F (Fin n → F)
  length_positive : 0 < n

structure NonlinearCode (F : Type) [Field F] [Fintype F] (n : Nat) where
  code : Code F n
  not_subspace : ¬ ∃ s : Submodule F (Fin n → F),
    ∀ x, x ∈ code.words ↔ x ∈ s

/-- A row basis is stored as a basis of the code subspace; coordinate multiplication
and correspondence to a concrete matrix API are separate obligations. -/
structure Generator (F : Type) [Field F] [Fintype F] (n k : Nat) where
  code : LinearCode F n
  basis : Module.Basis (Fin k) F code.space

/-- Kernel correspondence, with surjectivity making the n-k checks independent. -/
structure CheckMatrix (F : Type) [Field F] [Fintype F] (n k : Nat) where
  code : LinearCode F n
  dimension_valid : k ≤ n
  checkMap : (Fin n → F) →ₗ[F] (Fin (n-k) → F)
  onto : Function.Surjective checkMap
  kernel : LinearMap.ker checkMap = code.space

/-- Dot product is bilinear, not Hermitian. -/
def dualCarrier {F : Type} [Field F] [Fintype F] {n : Nat}
    (c : LinearCode F n) : Set (Fin n → F) :=
  {v | ∀ x ∈ c.space, ∑ i, v i * x i = 0}

end Information

abbrev ShannonEntropy := @Information.entropy
abbrev ConditionalEntropy := @Information.conditionalEntropy
abbrev RelativeEntropy := @Information.divergence
abbrev MutualInformation := @Information.mutualInformation
abbrev StochasticChannel := Information.Channel
abbrev DiscreteMemorylessChannel := @Information.blockKernel
abbrev ChannelCapacity := @Information.informationCapacity
abbrev UniquelyDecodableCode := Information.UniqueCode
abbrev PrefixFreeCode := Information.PrefixCode
abbrev DistortionMeasure := Information.Cost
abbrev RateDistortion := Information.DistortionProblem
abbrev HammingSpace := @Information.hamming
abbrev BlockCode := Information.Code
abbrev LinearBlockCode := Information.LinearCode
abbrev NonlinearBlockCode := Information.NonlinearCode
abbrev GeneratorMatrix := Information.Generator
abbrev ParityCheckMatrix := Information.CheckMatrix
abbrev Syndrome {F : Type} [Field F] [Fintype F] {n k : Nat}
    (h : ParityCheckMatrix F n k) := h.checkMap
abbrev DualCode := @Information.dualCarrier

end Catalog
