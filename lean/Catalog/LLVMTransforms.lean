module

public import Catalog.CompilerTransforms
public import Mathlib.Data.BitVec
public import Mathlib.Logic.Relation

@[expose] public section

namespace Catalog.LLVM
universe u

structure DataLayout (Ty AddressSpace : Type u) where
  storeSize : Ty → Nat
  allocationSize : Ty → Nat
  abiAlignment : Ty → Nat
  pointerWidth : AddressSpace → Nat
  indexWidth : AddressSpace → Nat
  littleEndian : Bool
  sized : Ty → Prop

structure PointerProvenance (Ptr Object : Type u) where
  associated : Ptr → Set Object
  basedOn : Ptr → Ptr → Prop
  preservesAssociation : ∀ p q, basedOn p q → associated q ⊆ associated p

structure ByteMemory (Address Cell State : Type u) where
  allocated : State → Set Address
  alive : State → Set Address
  contents : State → Address → Cell
  read : State → List Address → List Cell
  readLaw : ∀ s addresses, read s addresses = addresses.map (contents s)

inductive AliasVerdict where
  | noAlias
  | mayAlias
  | partialAlias
  | mustAlias

structure AliasAnalysis (Location : Type u) where
  possibleConflict : Location → Location → Prop
  query : Location → Location → AliasVerdict
  noAliasSound : ∀ x y, query x y = .noAlias → ¬ possibleConflict x y

inductive MemoryAccessKind where
  | entry
  | definition
  | use
  | phi

structure MemorySSA (Access : Type u) where
  kind : Access → MemoryAccessKind
  concreteClobber : Access → Access → Prop
  candidate : Access → Access → Prop
  conservative : ∀ d use, concreteClobber d use → candidate d use

structure ControlFlowRefinement (S T : Type u) where
  sourceStep : S → S → Prop
  targetStep : T → T → Prop
  sourceSafe : S → Prop
  related : S → T → Prop
  matchTargetStep : ∀ s t t', related s t → sourceSafe s → targetStep t t' →
    ∃ s', Relation.ReflTransGen sourceStep s s' ∧ related s' t'

structure LoopIterationMapping (S T : Type u) where
  sourceActive : Set S
  targetActive : Set T
  original : T → S
  mapsActive : ∀ t ∈ targetActive, original t ∈ sourceActive
  covers : ∀ s ∈ sourceActive, ∃ t ∈ targetActive, original t = s
  unique : ∀ t ∈ targetActive, ∀ t' ∈ targetActive, original t = original t' → t = t'

structure ScalarRecurrence where
  start : Int
  stride : Int

def recurrenceValue (r : ScalarRecurrence) (iteration : Nat) : Int :=
  r.start + (iteration : Int) * r.stride

inductive IntegerOutcome (width : Nat) where
  | value : Transforms.LLVMPoisonSemantics (BitVec width) → IntegerOutcome width
  | immediateUB : IntegerOutcome width

structure LLVMIntegerSemantics (Op : Type u) (width : Nat) where
  positiveWidth : 0 < width
  run : Op → BitVec width → BitVec width → Set (IntegerOutcome width)

structure LLVMFloatingPointSemantics (Op Value Env : Type u) where
  isNaN : Value → Prop
  isInfinity : Value → Prop
  run : Op → Env → List Value → Set (Value × Env)
  permittedRewrite : Op → Op → Prop

structure PredicatedVectorSemantics (Value : Type u) (width : Nat) where
  evl : Nat
  evlBound : evl ≤ width
  mask : Fin width → Bool
  inactiveResult : Fin width → Set Value

def activeLane {A : Type u} {w : Nat} (m : PredicatedVectorSemantics A w)
    (lane : Fin w) : Prop := lane.val < m.evl ∧ m.mask lane = true

structure AtomicMemoryModel (Event : Type u) where
  programOrder : Event → Event → Prop
  synchronizesWith : Event → Event → Prop
  readsFrom : Event → Event → Prop
  modificationOrder : Event → Event → Prop
  allowed : Prop

def atomicHappensBefore {E : Type u} (m : AtomicMemoryModel E) : E → E → Prop :=
  Relation.TransGen (fun x y => m.programOrder x y ∨ m.synchronizesWith x y)

structure CallEffectContract (Input Output State : Type u) where
  precondition : Input → State → Prop
  outcome : Input → State → Output → State → Prop
  allowedEffect : State → State → Prop
  effectSound : ∀ i s o t, precondition i s → outcome i s o t → allowedEffect s t

inductive ExceptionalControlFlow (Value Exception : Type u) where
  | returned : Value → ExceptionalControlFlow Value Exception
  | unwound : Exception → ExceptionalControlFlow Value Exception
  | diverged : ExceptionalControlFlow Value Exception
  | immediateUB : ExceptionalControlFlow Value Exception

structure ConvergentExecution (Instance Thread Value : Type u) where
  participants : Instance → Set Thread
  allowedResult : Instance → (Thread → Value) → Prop
  sameCommunication : Instance → Instance → Prop

structure StateRepresentation (S T Observation : Type u) where
  related : S → T → Prop
  sourceObserve : S → Observation
  targetObserve : T → Observation
  observationAgreement : ∀ s t, related s t → sourceObserve s = targetObserve t

structure SymbolLinkage (Module Environment Symbol Definition : Type u) where
  admissible : Environment → Prop
  resolve : Module → Environment → Symbol → Set Definition
  exposed : Module → Symbol → Prop

structure LLVMAttributeContract (Program Input : Type u) where
  admitted : Program → Input → Prop
  guarantees : Program → Input → Prop
  justified : ∀ p i, admitted p i → guarantees p i

structure RuntimeInstrumentation (SourceEvent TargetEvent : Type u) where
  erase : TargetEvent → List SourceEvent
  acceptedExecution : List TargetEvent → Prop

def eraseInstrumentation {S T : Type u} (m : RuntimeInstrumentation S T)
    (trace : List T) : List S := trace.flatMap m.erase

end Catalog.LLVM
