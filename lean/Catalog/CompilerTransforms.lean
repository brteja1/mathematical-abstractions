module

public import Mathlib.Data.Set.Basic

@[expose] public section

namespace Catalog.Transforms
universe u v w

/-- Whole-behavior inclusion; UB must be totalized by the supplied semantics. -/
def BehaviorRefinement {P I O : Type u} (behaviors : P → I → Set O)
    (source target : P) : Prop :=
  ∀ i, behaviors target i ⊆ behaviors source i

structure GuardedRewrite (P : Type u) where
  guard : P → Prop
  rewrite : P → P → Prop
  wellFormed : P → Prop

/-- A path oracle includes the entry and endpoint of each finite CFG path. -/
def Dominance {V : Type u} (paths : V → V → List V → Prop)
    (entry dominator node : V) : Prop :=
  (∃ path, paths entry node path) ∧
    ∀ path, paths entry node path → dominator ∈ path

structure SSAForm (Value Use Position Ty : Type u) where
  definition : Value → Position
  operand : Use → Value
  usePosition : Use → Position
  available : Position → Position → Prop
  valueType : Value → Ty
  expectedType : Use → Ty
  availableAtUse : ∀ use, available (definition (operand use)) (usePosition use)
  typedUse : ∀ use, valueType (operand use) = expectedType use

structure EffectSummary (Op Resource : Type u) where
  actual : Op → Set Resource
  summary : Op → Set Resource
  sound : ∀ op, actual op ⊆ summary op

def SpeculationSafety {State : Type u} (newlyExecuted : Set State)
    (defined terminates silent : State → Prop) : Prop :=
  ∀ s ∈ newlyExecuted, defined s ∧ terminates s ∧ silent s

inductive LLVMPoisonSemantics (A : Type u) where
  | concrete : A → LLVMPoisonSemantics A
  | undef : LLVMPoisonSemantics A
  | poison : LLVMPoisonSemantics A

/-- This relation is for one dynamic scalar freeze execution; clients share its result. -/
def freezeResult {A : Type u} (input : LLVMPoisonSemantics A) (output : A) : Prop :=
  match input with
  | .concrete a => output = a
  | .undef => True
  | .poison => True

structure DialectConversion (S T STy TTy : Type u) where
  convert : S → T → Prop
  legal : T → Prop
  typeConvert : STy → List TTy → Prop
  represents : S → T → Prop

inductive ValidationVerdict where
  | proved
  | counterexample
  | unknown

structure TranslationValidation (P : Type u) where
  obligation : P → P → Prop
  check : P → P → ValidationVerdict
  acceptedSound : ∀ s t, check s t = .proved → obligation s t

structure AbstractInterpretation (C A : Type u) where
  gamma : A → Set C
  step : C → C → Prop
  transfer : A → A
  sound : ∀ a c d, c ∈ gamma a → step c d → d ∈ gamma (transfer a)

/-- Literal-constant multiplication/divisors only; all arithmetic is exact Int. -/
inductive AffineExpr (n : Nat) where
  | variable : Fin n → AffineExpr n
  | constant : Int → AffineExpr n
  | add : AffineExpr n → AffineExpr n → AffineExpr n
  | scale : Int → AffineExpr n → AffineExpr n
  | floorDiv : AffineExpr n → (k : Nat) → 0 < k → AffineExpr n
  | ceilDiv : AffineExpr n → (k : Nat) → 0 < k → AffineExpr n
  | mod : AffineExpr n → (k : Nat) → 0 < k → AffineExpr n

abbrev IntegerAffineMap (dimensions symbols results : Nat) :=
  Fin results → AffineExpr (dimensions + symbols)

structure LoopDependence (Event Address Time : Type u) where
  active : Set Event
  address : Event → Address
  writes : Event → Prop
  before : Event → Event → Prop
  schedule : Event → Time
  timeBefore : Time → Time → Prop

def preservesDependence {E A T : Type u} (m : LoopDependence E A T) : Prop :=
  ∀ x ∈ m.active, ∀ y ∈ m.active,
    m.address x = m.address y → (m.writes x ∨ m.writes y) → m.before x y →
      m.timeBefore (m.schedule x) (m.schedule y)

structure AnalysisPreservation (IR Result : Type u) where
  valid : IR → Result → Prop
  transform : IR → IR
  update : Result → Result
  preserved : ∀ ir result, valid ir result → valid (transform ir) (update result)

end Catalog.Transforms
