module

public import Catalog.InformationTheoryProofs
public import Mathlib.Basic.ENNReal.Basic
public import Mathlib.FieldTheory.Finiteness
public import Mathlib.LinearAlgebra.BilinearForm.Orthogonal
public import Mathlib.LinearAlgebra.Matrix.ToLin

/-!
Concrete targets for all 29 catalog claims. A `def ... : Prop` states a proposition;
it does not prove it. Only theorem declarations with audited bindings are witnesses.
No conclusion below is introduced as an axiom or a structure field.
-/
@[expose] public section
noncomputable section
namespace Catalog.Information
open scoped BigOperators ENNReal

variable {A B : Type} [Fintype A] [Fintype B]

def Independent (p : Law (A × B)) : Prop :=
  ∀ a b, p.mass (a,b) = (marginalX p).mass a * (marginalY p).mass b

def errorOfEstimate [DecidableEq A] (p : Law (A × B)) (g : B → A) : ℝ :=
  ∑ a, ∑ b, if a = g b then 0 else p.mass (a,b)

def binaryEntropy (u : ℝ) : ℝ := -u * logTwo u - (1-u) * logTwo (1-u)

/-- Strong eventual upper/lower bounds encode limsup≤r and liminf≥r without
assuming the sequence has a limit. Codes below always use positive block length. -/
def UpperLimit (s : ℕ → ℝ) (r : ℝ) : Prop :=
  ∀ ε > 0, ∃ N, ∀ n ≥ N, s n ≤ r + ε

def LowerLimit (s : ℕ → ℝ) (r : ℝ) : Prop :=
  ∀ ε > 0, ∃ N, ∀ n ≥ N, r - ε ≤ s n

def Vanishes (s : ℕ → ℝ) : Prop :=
  ∀ ε > 0, ∃ N, ∀ n ≥ N, |s n| < ε

def bitRate (messages length : ℕ) : ℝ := logTwo messages / length

structure SourceCode (A : Type) (n : ℕ) where
  size : ℕ
  size_positive : 0 < size
  encode : (Fin n → A) → Fin size
  decode : Fin size → (Fin n → A)

def sourceError [DecidableEq A] {n : ℕ} (p : Law A) (c : SourceCode A n) : ℝ :=
  ∑ x, if c.decode (c.encode x) = x then 0 else (iidLaw p n).mass x

structure ChannelCode (A B : Type) (n : ℕ) where
  size : ℕ
  size_positive : 0 < size
  encode : Fin size → (Fin n → A)
  decode : (Fin n → B) → Fin size

def channelError {n : ℕ} (w : Channel A B) (c : ChannelCode A B n) : ℝ :=
  (∑ m, ∑ y, if c.decode y = m then 0 else blockKernel w n (c.encode m) y) / c.size

def Achievable (w : Channel A B) (r : ℝ) : Prop :=
  ∃ c : (n : ℕ) → ChannelCode A B (n+1),
    LowerLimit (fun n => bitRate (c n).size (n+1)) r ∧
    Vanishes (fun n => channelError w (c n))

def operationalCapacity (w : Channel A B) : ℝ :=
  sSup {r | 0 ≤ r ∧ Achievable w r}

structure LossyCode (A B : Type) (n : ℕ) where
  size : ℕ
  size_positive : 0 < size
  encode : (Fin n → A) → Fin size
  decode : Fin size → (Fin n → B)

def lossyCost {n : ℕ} (p : Law A) (d : Cost A B) (c : LossyCode A B n) : ℝ :=
  expectation (iidLaw p n) (fun x => averageCost d x (c.decode (c.encode x)))

def kernelCost (p : Law A) (d : Cost A B) (w : Channel A B) : ℝ :=
  ∑ a, ∑ b, p.mass a * (w a).mass b * d.value a b

/-- Complete lattices give inf ∅=∞. ofReal is used only on information quantities;
nonnegativity is a separate target, not a supplied hypothesis. -/
def informationRD (p : Law A) (d : Cost A B) (D : ℝ) : ℝ≥0∞ :=
  sInf {r | ∃ w : Channel A B, kernelCost p d w ≤ D ∧
    r = ENNReal.ofReal (mutualInformation (joint p w))}

def lossyAchievable (p : Law A) (d : Cost A B) (D r : ℝ) : Prop :=
  0 ≤ r ∧ ∃ c : (n : ℕ) → LossyCode A B (n+1),
    UpperLimit (fun n => bitRate (c n).size (n+1)) r ∧
    UpperLimit (fun n => lossyCost p d (c n)) D

def operationalRD (p : Law A) (d : Cost A B) (D : ℝ) : ℝ≥0∞ :=
  sInf (ENNReal.ofReal '' {r | lossyAchievable p d D r})

def minDistortion (p : Law A) (d : Cost A B) : ℝ :=
  ∑ a, p.mass a * sInf (Set.range (d.value a))

def expectedLength {M : Type} [Fintype M] (p : Law M) (f : M → List Bool) : ℝ :=
  ∑ m, p.mass m * (f m).length

def kraftSum {M : Type} [Fintype M] (f : M → List Bool) : ℝ :=
  ∑ m, (1 / 2 : ℝ) ^ (f m).length

def hammingBall {X : Type} [Fintype X] [DecidableEq X] {n : ℕ}
    (x : Fin n → X) (t : ℕ) : Finset (Fin n → X) :=
  Finset.univ.filter (fun y => hamming x y ≤ t)

/-- Unguarded minimum is an auxiliary total function. Catalog dmin is exposed only
through dmin, which returns none when there are fewer than two codewords. -/
def pairDistances {X : Type} [DecidableEq X] {n : ℕ} (C : Set (Fin n → X)) : Set ℕ :=
  {d | ∃ x ∈ C, ∃ y ∈ C, x ≠ y ∧ d = hamming x y}

def pairMinimum {X : Type} [DecidableEq X] {n : ℕ} (C : Set (Fin n → X)) : ℕ :=
  sInf (pairDistances C)

def dmin {X : Type} [DecidableEq X] {n : ℕ} (C : Code X n) : Option ℕ :=
  if 2 ≤ C.words.card then some (pairMinimum (C.words : Set (Fin n → X))) else none

def ballVolume (n q t : ℕ) : ℕ := ∑ i ∈ Finset.range (t+1), n.choose i * (q-1)^i

def nearest {X : Type} [DecidableEq X] {n : ℕ} (C : Code X n) (y : Fin n → X) :
    Set (Fin n → X) := {c | c ∈ C.words ∧ ∀ c' ∈ C.words, hamming c y ≤ hamming c' y}

section Linear
variable {F : Type} [Field F] [Fintype F] {n k : ℕ}

def nonzeroWeights [DecidableEq F] (c : LinearCode F n) : Set ℕ :=
  {d | ∃ x ∈ c.space, x ≠ 0 ∧ d = hamming x 0}

def qaryRate (c : LinearCode F n) : ℝ :=
  logTwo (Nat.card c.space) / logTwo (Fintype.card F) / n

/-- Concrete row matrix for the already registered basis model. -/
def generatorMatrix (g : Generator F n k) : _root_.Matrix (Fin k) (Fin n) F :=
  fun i j => (g.basis i).val j

def dualSpace (c : Submodule F (Fin n → F)) : Submodule F (Fin n → F) where
  carrier := {v | ∀ x ∈ c, ∑ i, v i * x i = 0}
  zero_mem' := by simp
  add_mem' := by
    intro u v hu hv x hx
    simp only [Pi.add_apply, add_mul, Finset.sum_add_distrib]
    rw [hu x hx, hv x hx, add_zero]
  smul_mem' := by
    intro a v hv x hx
    simp only [Pi.smul_apply, smul_eq_mul, mul_assoc, ← Finset.mul_sum]
    rw [hv x hx, mul_zero]
end Linear

namespace Targets

-- Each constant below is a proposition, not an asserted theorem.
-- urn:csabs:theorem/ShannonEntropy-entropy-bounds
def entropyBounds : Prop := ∀ (A : Type) [Fintype A] [Nonempty A] [DecidableEq A] (p : Law A),
  (0 ≤ entropy p ∧ entropy p ≤ logTwo (Fintype.card A)) ∧
  (entropy p = 0 ↔ ∃ a, ∀ x, p.mass x = if x=a then 1 else 0) ∧
  (entropy p = logTwo (Fintype.card A) ↔ ∀ x, p.mass x = 1 / Fintype.card A)

-- urn:csabs:theorem/ShannonEntropy-source-coding
def sourceCoding : Prop := ∀ (A : Type) [Fintype A] [Nonempty A] [DecidableEq A] (p : Law A),
  (∀ r > entropy p, ∃ c : (n : ℕ) → SourceCode A (n+1),
    UpperLimit (fun n => bitRate (c n).size (n+1)) r ∧
    Vanishes (fun n => sourceError p (c n))) ∧
  (∀ c : (n : ℕ) → SourceCode A (n+1), Vanishes (fun n => sourceError p (c n)) →
    LowerLimit (fun n => bitRate (c n).size (n+1)) (entropy p))

-- urn:csabs:law/ConditionalEntropy-chain-rule
def chainRule : Prop := ∀ (A B : Type) [Fintype A] [Fintype B] (p : Law (A×B)),
  entropy p = entropy (marginalY p) + conditionalEntropy p

-- urn:csabs:theorem/ConditionalEntropy-conditioning-reduces
def conditioningReduces : Prop := ∀ (A B : Type) [Fintype A] [Fintype B] (p : Law (A×B)),
  (0 ≤ conditionalEntropy p ∧ conditionalEntropy p ≤ entropy (marginalX p)) ∧
  (conditionalEntropy p = entropy (marginalX p) ↔ Independent p)

-- urn:csabs:theorem/ConditionalEntropy-fano
def fano : Prop := ∀ (A B : Type) [Fintype A] [Fintype B] [DecidableEq A],
  2 ≤ Fintype.card A → ∀ (p : Law (A×B)) (g : B → A),
  conditionalEntropy p ≤ binaryEntropy (errorOfEstimate p g) +
    errorOfEstimate p g * logTwo (Fintype.card A - 1 : ℕ)

-- urn:csabs:theorem/RelativeEntropy-gibbs
def gibbs : Prop := ∀ (A : Type) [Fintype A] (p q : Law A),
  (∀ d, divergence p q = some d → 0 ≤ d) ∧
  (divergence p q = some 0 ↔ p.mass = q.mass)

-- urn:csabs:theorem/MutualInformation-entropy-identity
def informationIdentity : Prop := ∀ (A B : Type) [Fintype A] [Fintype B] (p : Law (A×B)),
  (mutualInformation p = entropy (marginalX p) + entropy (marginalY p) - entropy p) ∧
  (mutualInformation p = entropy (marginalX p) - conditionalEntropy p) ∧
  (0 ≤ mutualInformation p) ∧ (mutualInformation p = 0 ↔ Independent p)

-- urn:csabs:theorem/MutualInformation-data-processing
def dataProcessing : Prop := ∀ (A B C : Type) [Fintype A] [Fintype B] [Fintype C]
  (p : Law A) (w : Channel A B) (v : Channel B C),
  mutualInformation (joint p (fun a => output (w a) v)) ≤ mutualInformation (joint p w)

-- urn:csabs:law/StochasticChannel-output-normalized
def outputNormalized : Prop := ∀ (A B : Type) [Fintype A] [Fintype B]
  (p : Law A) (w : Channel A B), (∑ b, outputMass p w b) = 1 ∧ ∀ b, 0 ≤ outputMass p w b

-- urn:csabs:law/DiscreteMemorylessChannel-product-normalized
def productNormalized : Prop := ∀ (A B : Type) [Fintype B]
  (w : Channel A B) (n : ℕ) (x : Fin n → A), (∑ y, blockKernel w n x y) = 1

-- urn:csabs:theorem/ChannelCapacity-shannon
def channelCoding : Prop := ∀ (A B : Type) [Fintype A] [Fintype B] [Nonempty A] [Nonempty B]
  (w : Channel A B),
  (∃ p : Law A, operationalCapacity w = mutualInformation (joint p w) ∧
    ∀ q : Law A, mutualInformation (joint q w) ≤ mutualInformation (joint p w)) ∧
  (∀ r, 0 ≤ r → r < operationalCapacity w → Achievable w r) ∧
  (∀ c : (n : ℕ) → ChannelCode A B (n+1), Vanishes (fun n => channelError w (c n)) →
    UpperLimit (fun n => bitRate (c n).size (n+1)) (operationalCapacity w))

-- urn:csabs:theorem/PrefixFreeCode-unique-decoding
def prefixUnique : Prop := ∀ (M : Type) (f : PrefixCode M),
  Function.Injective (fun s : List M => s.flatMap f.word)

-- urn:csabs:theorem/UniquelyDecodableCode-kraft-mcmillan
def kraftMcMillan : Prop := ∀ (M : Type) [Fintype M] [Nonempty M],
  (∀ f : UniqueCode M, kraftSum f.word ≤ 1) ∧
  (∀ lengths : M → ℕ, (∀ m, 0 < lengths m) →
    (∑ m, (1/2 : ℝ)^(lengths m)) ≤ 1 →
    ∃ f : PrefixCode M, ∀ m, (f.word m).length = lengths m)

-- urn:csabs:theorem/PrefixFreeCode-source-length
def sourceLength : Prop := ∀ (M : Type) [Fintype M] [Nonempty M] (p : Law M),
  (∀ m, 0 < p.mass m) →
  (∀ f : UniqueCode M, entropy p ≤ expectedLength p f.word) ∧
  (∃ f : PrefixCode M, expectedLength p f.word ≤ entropy p + 1) ∧
  (2 ≤ Fintype.card M → ∃ f : PrefixCode M, expectedLength p f.word < entropy p + 1)

-- urn:csabs:law/DistortionMeasure-expected-block
def expectedBlock : Prop := ∀ (A B : Type) [Fintype A] [Fintype B]
  (n : ℕ), 0 < n → ∀ (p : Law ((Fin n → A) × (Fin n → B))) (d : Cost A B),
  expectation p (fun xz => averageCost d xz.1 xz.2) =
    (∑ i, expectation p (fun xz => d.value (xz.1 i) (xz.2 i))) / n

-- urn:csabs:theorem/RateDistortion-monotone-convex
def rateDistortionConvex : Prop := ∀ (A B : Type) [Fintype A] [Fintype B]
  (p : Law A) (d : Cost A B),
  (∀ D₁ D₂ : ℝ, 0 ≤ D₁ → D₁ ≤ D₂ → informationRD p d D₂ ≤ informationRD p d D₁) ∧
  (∀ D₁ D₂ a : ℝ, 0 ≤ D₁ → 0 ≤ D₂ → 0 < a → a < 1 →
    informationRD p d (a*D₁+(1-a)*D₂) ≤
      ENNReal.ofReal a * informationRD p d D₁ + ENNReal.ofReal (1-a) * informationRD p d D₂)

-- urn:csabs:theorem/RateDistortion-shannon-lossy
def lossyCoding : Prop := ∀ (A B : Type) [Fintype A] [Fintype B] [Nonempty A] [Nonempty B]
  (p : Law A) (d : Cost A B) (D : ℝ),
  0 ≤ D → minDistortion p d < D → informationRD p d D = operationalRD p d D

-- urn:csabs:law/HammingSpace-metric
def hammingMetric : Prop := ∀ (X : Type) [DecidableEq X] (n : ℕ) (x y z : Fin n → X),
  0 ≤ hamming x y ∧ (hamming x y = 0 ↔ x=y) ∧
  hamming x y = hamming y x ∧ hamming x z ≤ hamming x y + hamming y z

-- urn:csabs:theorem/HammingSpace-ball-volume
def hammingVolume : Prop := ∀ (X : Type) [Fintype X] [DecidableEq X],
  2 ≤ Fintype.card X → ∀ (n t : ℕ), 0 < n → t ≤ n → ∀ x : Fin n → X,
  (hammingBall x t).card = ballVolume n (Fintype.card X) t

-- urn:csabs:theorem/BlockCode-unique-radius
def uniqueRadius : Prop := ∀ (X : Type) [Fintype X] [DecidableEq X], 2 ≤ Fintype.card X →
  ∀ (n t : ℕ) (C : Code X n), 2 ≤ C.words.card →
  ((∀ x ∈ C.words, ∀ y ∈ C.words, x ≠ y → Disjoint (hammingBall x t) (hammingBall y t)) ↔
    2*t+1 ≤ pairMinimum (C.words : Set (Fin n → X))) ∧
  (2*t+1 ≤ pairMinimum (C.words : Set (Fin n → X)) →
    ∀ c ∈ C.words, ∀ y, hamming c y ≤ t → nearest C y = {c})

-- urn:csabs:theorem/BlockCode-hamming-bound
def hammingBound : Prop := ∀ (X : Type) [Fintype X] [DecidableEq X], 2 ≤ Fintype.card X →
  ∀ (n : ℕ) (C : Code X n), 2 ≤ C.words.card →
  C.words.card * ballVolume n (Fintype.card X)
    ((pairMinimum (C.words : Set (Fin n → X)) - 1)/2) ≤ (Fintype.card X)^n

-- urn:csabs:theorem/BlockCode-singleton
def singletonBound : Prop :=
  (∀ (X : Type) [Fintype X] [DecidableEq X], 2 ≤ Fintype.card X →
    ∀ (n : ℕ) (C : Code X n), 2 ≤ C.words.card →
    C.words.card ≤ (Fintype.card X)^(n-pairMinimum (C.words : Set (Fin n → X))+1)) ∧
  (∀ (F : Type) [Field F] [Fintype F] [DecidableEq F] (n : ℕ) (c : LinearCode F n),
    0 < Module.finrank F c.space → pairMinimum (c.space : Set (Fin n → F)) ≤ n-Module.finrank F c.space+1)

-- urn:csabs:theorem/LinearBlockCode-cardinality
def linearCardinality : Prop := ∀ (F : Type) [Field F] [Fintype F] (n : ℕ) (c : LinearCode F n),
  Nat.card c.space = (Fintype.card F)^(Module.finrank F c.space) ∧
    qaryRate c = (Module.finrank F c.space : ℝ)/n

-- urn:csabs:theorem/LinearBlockCode-distance-weight
def distanceWeight : Prop := ∀ (F : Type) [Field F] [Fintype F] [DecidableEq F]
  (n : ℕ) (c : LinearCode F n), 0 < Module.finrank F c.space →
  pairMinimum (c.space : Set (Fin n → F)) = sInf (nonzeroWeights c)

-- urn:csabs:theorem/NonlinearBlockCode-witness-exists
def nonlinearWitness : Prop := ∀ (F : Type) [Field F] (n : ℕ) (C : Set (Fin n → F)),
  (¬ ∃ S : Submodule F (Fin n → F), (S : Set (Fin n → F)) = C) ↔ NonlinearWitness C

-- urn:csabs:theorem/GeneratorMatrix-encoding-isomorphism
def generatorIsomorphism : Prop := ∀ (F : Type) [Field F] [Fintype F]
  (n k : ℕ) (g : Generator F n k),
  Function.Bijective (generatorEncode g) ∧
    (∀ x y, generatorEncode g (x+y) = generatorEncode g x + generatorEncode g y) ∧
    (∀ (a : F) x, generatorEncode g (a • x) = a • generatorEncode g x)

-- urn:csabs:theorem/ParityCheckMatrix-orthogonality
-- Linear-map composition zero is the coordinate-independent GHᵀ=0 condition;
-- injectivity/surjectivity express full generator/check ranks.
def checkOrthogonality : Prop := ∀ (F : Type) [Field F] [Fintype F] (n k : ℕ),
  (∀ (g : Generator F n k) (h : CheckMatrix F n k), g.code.space = h.code.space →
    ∀ m, h.checkMap (generatorEncode g m).val = 0) ∧
  (∀ (G : (Fin k → F) →ₗ[F] (Fin n → F))
      (H : (Fin n → F) →ₗ[F] (Fin (n-k) → F)),
    k ≤ n → Function.Injective G → Function.Surjective H → H.comp G = 0 →
    LinearMap.range G = LinearMap.ker H)

-- urn:csabs:theorem/Syndrome-coset-invariance
def syndromeCoset : Prop := ∀ (F : Type) [Field F] [Fintype F] (n k : ℕ)
  (h : CheckMatrix F n k) (y z c e : Fin n → F), c ∈ h.code.space →
  (h.checkMap y = 0 ↔ y ∈ h.code.space) ∧
  (h.checkMap y = h.checkMap z ↔ y-z ∈ h.code.space) ∧ h.checkMap (c+e) = h.checkMap e

-- urn:csabs:theorem/DualCode-dimension-involution
-- dualSpace constructs the submodule, thereby encoding linearity as a type.
def dualDimension : Prop := ∀ (F : Type) [Field F] [Fintype F] (n : ℕ) (c : LinearCode F n),
  Module.finrank F (dualSpace c.space) = n - Module.finrank F c.space ∧
    dualSpace (dualSpace c.space) = c.space

end Targets
end Catalog.Information

namespace Catalog.Information
variable {A B : Type} [Fintype A] [Fintype B]

lemma logTwo_div {x y : ℝ} (hx : x ≠ 0) (hy : y ≠ 0) :
    logTwo (x/y) = logTwo x - logTwo y := by
  simp only [logTwo, Real.log_div hx hy, sub_div]

-- urn:csabs:law/ConditionalEntropy-chain-rule
theorem entropy_chain_rule (p : Law (A×B)) :
    entropy p = entropy (marginalY p) + conditionalEntropy p := by
  have term (a : A) (b : B) :
      p.mass (a,b) * logTwo (p.mass (a,b) / ∑ x, p.mass (x,b)) =
      p.mass (a,b) * logTwo (p.mass (a,b)) -
        p.mass (a,b) * logTwo (∑ x, p.mass (x,b)) := by
    by_cases hz : p.mass (a,b) = 0
    · simp [hz]
    · have ht : 0 < p.mass (a,b) := lt_of_le_of_ne (p.nonnegative _) (Ne.symm hz)
      have hm : 0 < ∑ x, p.mass (x,b) :=
        lt_of_lt_of_le ht (Finset.single_le_sum (fun x _ => p.nonnegative (x,b)) (Finset.mem_univ a))
      rw [logTwo_div hz (ne_of_gt hm), mul_sub]
  have regroup : (∑ a, ∑ b, p.mass (a,b) * logTwo (∑ x, p.mass (x,b))) =
      ∑ b, (∑ a, p.mass (a,b)) * logTwo (∑ x, p.mass (x,b)) := by
    rw [Finset.sum_comm]
    simp_rw [Finset.sum_mul]
  simp only [entropy, conditionalEntropy, Fintype.sum_prod_type, marginalY]
  simp_rw [term, Finset.sum_sub_distrib]
  rw [regroup]
  ring

section LinearMore
variable {F : Type} [Field F] [Fintype F] {n k : ℕ}

-- urn:csabs:theorem/LinearBlockCode-cardinality
theorem linear_cardinality (c : LinearCode F n) :
    Nat.card c.space = (Fintype.card F)^(Module.finrank F c.space) ∧
    qaryRate c = (Module.finrank F c.space : ℝ)/n := by
  have card : Nat.card c.space = (Fintype.card F)^(Module.finrank F c.space) := by
    simpa only [Nat.card_eq_fintype_card] using (Module.natCard_eq_pow_finrank (K := F) (V := c.space))
  refine ⟨card, ?_⟩
  have hq : (1 : ℝ) < Fintype.card F := by exact_mod_cast Fintype.one_lt_card
  have hl : logTwo (Fintype.card F) ≠ 0 :=
    ne_of_gt (div_pos (Real.log_pos hq) (Real.log_pos (by norm_num)))
  have hlog : logTwo ((Fintype.card F : ℝ)^(Module.finrank F c.space)) =
      (Module.finrank F c.space : ℝ) * logTwo (Fintype.card F) := by
    simp only [logTwo, Real.log_pow, mul_div_assoc]
  unfold qaryRate
  rw [card, Nat.cast_pow, hlog, mul_div_assoc, div_self hl, mul_one]

-- urn:csabs:theorem/LinearBlockCode-distance-weight
-- Equal distance sets give the same minimum; the positive dimension is retained
-- in the final target to exclude the catalog's undefined singleton minimum.
theorem distance_sets [DecidableEq F] (c : LinearCode F n) :
    pairDistances (c.space : Set (Fin n → F)) = nonzeroWeights c := by
  ext d
  constructor
  · rintro ⟨x,hx,y,hy,hne,rfl⟩
    refine ⟨-x+y, c.space.add_mem (c.space.neg_mem hx) hy, ?_, ?_⟩
    · intro heq
      exact hne (neg_add_eq_zero.mp heq)
    · exact hammingDist_eq_hammingNorm x y
  · rintro ⟨x,hx,hne,rfl⟩
    exact ⟨x,hx,0,c.space.zero_mem,hne,rfl⟩

theorem distance_weight [DecidableEq F] (c : LinearCode F n)
    (_hk : 0 < Module.finrank F c.space) :
    pairMinimum (c.space : Set (Fin n → F)) = sInf (nonzeroWeights c) := by
  unfold pairMinimum
  rw [distance_sets]

-- urn:csabs:theorem/ParityCheckMatrix-orthogonality
theorem generator_checked (g : Generator F n k) (h : CheckMatrix F n k)
    (hc : g.code.space = h.code.space) (m : Fin k → F) :
    h.checkMap (generatorEncode g m).val = 0 := by
  have hm : (generatorEncode g m).val ∈ h.code.space := hc ▸ (generatorEncode g m).property
  change (generatorEncode g m).val ∈ LinearMap.ker h.checkMap
  rw [h.kernel]
  exact hm

omit [Fintype F] in
theorem full_rank_kernel (G : (Fin k → F) →ₗ[F] (Fin n → F))
    (H : (Fin n → F) →ₗ[F] (Fin (n-k) → F)) (hk : k ≤ n)
    (hG : Function.Injective G) (hH : Function.Surjective H) (hzero : H.comp G = 0) :
    LinearMap.range G = LinearMap.ker H := by
  have hincl : LinearMap.range G ≤ LinearMap.ker H := by
    rintro _ ⟨x,rfl⟩
    change (H.comp G) x = 0
    rw [hzero, LinearMap.zero_apply]
  have grank : Module.finrank F (LinearMap.range G) = k := by
    simpa using LinearMap.finrank_range_of_inj hG
  have hrank : Module.finrank F (LinearMap.range H) = n-k := by
    rw [LinearMap.range_eq_top.mpr hH]
    simp
  have ranks := H.finrank_range_add_finrank_ker
  simp only [Module.finrank_pi, Fintype.card_fin] at ranks
  apply Submodule.eq_of_le_of_finrank_eq hincl
  omega
end LinearMore
end Catalog.Information

namespace Catalog.Information
section DualProof
variable {F : Type} [Field F] {n : ℕ}

def dotForm : _root_.LinearMap.BilinForm F (Fin n → F) := dotProductBilin F F

lemma dot_nondegenerate : (dotForm (F := F) (n := n)).Nondegenerate := by
  classical
  constructor
  · intro x hx
    funext i
    have hi := hx (Pi.single i 1)
    simpa [dotForm, dotProductBilin, dotProduct, Pi.single_apply] using hi
  · intro x hx
    funext i
    have hi := hx (Pi.single i 1)
    simpa [dotForm, dotProductBilin, dotProduct, Pi.single_apply] using hi

lemma dot_reflexive : (dotForm (F := F) (n := n)).IsRefl := by
  intro x y h
  simpa only [dotForm, dotProductBilin, LinearMap.coe_mk, AddHom.coe_mk, dotProduct_comm] using h

lemma dual_eq_orthogonal (c : Submodule F (Fin n → F)) :
    dualSpace c = (dotForm (F := F)).orthogonal c := by
  ext x
  simp only [dualSpace, Submodule.mem_mk, AddSubmonoid.mem_mk, AddSubsemigroup.mem_mk,
    LinearMap.BilinForm.mem_orthogonal_iff, dotForm, dotProductBilin,
    LinearMap.coe_mk, AddHom.coe_mk, dotProduct]
  simp only [Set.mem_ofPred_eq, mul_comm]

-- urn:csabs:theorem/DualCode-dimension-involution
theorem dual_dimension [Fintype F] (c : LinearCode F n) :
    Module.finrank F (dualSpace c.space) = n - Module.finrank F c.space ∧
    dualSpace (dualSpace c.space) = c.space := by
  constructor
  · rw [dual_eq_orthogonal, LinearMap.BilinForm.finrank_orthogonal dot_nondegenerate]
    simp
  · simp_rw [dual_eq_orthogonal]
    exact LinearMap.BilinForm.orthogonal_orthogonal dot_nondegenerate dot_reflexive _
end DualProof
end Catalog.Information

namespace Catalog.Information.Verified

-- Every wrapper below proves the complete corresponding Targets proposition.
theorem outputNormalized : Targets.outputNormalized := by
  intro A B _ _ p w
  exact output_normalized p w

theorem productNormalized : Targets.productNormalized := by
  intro A B _ w n x
  exact block_normalized w n x

theorem expectedBlock : Targets.expectedBlock := by
  intro A B _ _ n hn p d
  exact expected_block n hn p d

theorem hammingMetric : Targets.hammingMetric := by
  intro X _ n x y z
  exact hamming_metric x y z

theorem prefixUnique : Targets.prefixUnique := by
  intro M f
  exact prefix_unique f

theorem generatorIsomorphism : Targets.generatorIsomorphism := by
  intro F _ _ n k g
  exact generator_bijective g

theorem syndromeCoset : Targets.syndromeCoset := by
  intro F _ _ n k h y z c e hc
  exact syndrome_coset h y z c e hc

theorem nonlinearWitness : Targets.nonlinearWitness := by
  intro F _ n C
  exact nonlinear_witness C

theorem chainRule : Targets.chainRule := by
  intro A B _ _ p
  exact entropy_chain_rule p

theorem linearCardinality : Targets.linearCardinality := by
  intro F _ _ n c
  exact linear_cardinality c

theorem distanceWeight : Targets.distanceWeight := by
  intro F _ _ _ n c hk
  exact distance_weight c hk

theorem checkOrthogonality : Targets.checkOrthogonality := by
  intro F _ _ n k
  exact ⟨fun g h hc m => generator_checked g h hc m,
    fun G H hk hG hH hz => full_rank_kernel G H hk hG hH hz⟩

theorem dualDimension : Targets.dualDimension := by
  intro F _ _ n c
  exact dual_dimension c

end Catalog.Information.Verified

namespace Catalog.Information
section Coordinates
variable {F : Type} [Field F] [Fintype F] {n k : ℕ}

/-- Proved bridge from the abstract basis encoding to the concrete row matrix mG. -/
theorem generator_coordinates (g : Generator F n k) (m : Fin k → F) :
    (generatorEncode g m).val = fun j => ∑ i, m i * generatorMatrix g i j := by
  simp only [generatorEncode, Module.Basis.equivFun_symm_apply]
  ext j
  simp [generatorMatrix]

def parityMatrix (h : CheckMatrix F n k) : _root_.Matrix (Fin (n-k)) (Fin n) F :=
  LinearMap.toMatrix' h.checkMap

/-- Proved bridge from the check map to ordinary matrix-vector multiplication. -/
theorem parity_coordinates (h : CheckMatrix F n k) (y : Fin n → F) :
    (parityMatrix h).mulVec y = h.checkMap y :=
  LinearMap.toMatrix'_mulVec h.checkMap y

end Coordinates

/-- Necessity half of Kraft–McMillan. This alone is not a witness for the full
catalog theorem, which also asserts the constructive converse. -/
theorem kraft_necessity {M : Type} [Fintype M] (f : UniqueCode M) :
    kraftSum f.word ≤ 1 := by
  classical
  have injective : Function.Injective f.word := by
    intro a b h
    have heq := f.unique (show ([a] : List M).flatMap f.word = [b].flatMap f.word by simp [h])
    simpa using heq
  have lift (L : List (List Bool)) (hL : ∀ w ∈ L, w ∈ Set.range f.word) :
      ∃ s : List M, s.map f.word = L := by
    induction L with
    | nil => exact ⟨[],rfl⟩
    | cons w L ih =>
      obtain ⟨m,hm⟩ := hL w (by simp)
      obtain ⟨s,hs⟩ := ih (by intro u hu; exact hL u (by simp [hu]))
      exact ⟨m::s, by simp [hm,hs]⟩
  have hud : _root_.InformationTheory.IsUniquelyDecodable (Set.range f.word) := by
    intro L T hL hT heq
    obtain ⟨s,rfl⟩ := lift L hL
    obtain ⟨t,rfl⟩ := lift T hT
    change s.flatMap f.word = t.flatMap f.word at heq
    exact congrArg (List.map f.word) (f.unique heq)
  let S : Finset (List Bool) := Finset.univ.image f.word
  have hS : _root_.InformationTheory.IsUniquelyDecodable (S : Set (List Bool)) := by
    simpa [S] using hud
  have hK := hS.finsetSum_one_div_card_pow_length_le_one
  have hsum : (∑ w ∈ S, (1/2 : ℝ)^w.length) = kraftSum f.word := by
    exact Finset.sum_image (fun _ _ _ _ h => injective h)
  rw [← hsum]
  simpa only [Fintype.card_bool, Nat.cast_ofNat] using hK
end Catalog.Information
