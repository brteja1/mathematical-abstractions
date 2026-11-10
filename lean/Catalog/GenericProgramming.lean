module

public import Catalog.StructuredData
public import Mathlib.Logic.Relation

@[expose] public section

namespace Catalog.Generics
universe u v w

structure GenericSignature (Name : Type u) (Kind : Type v) (Arg : Type w) where
  parameters : List (Name × Kind)
  names_unique : (parameters.map Prod.fst).Nodup
  kindOf : Arg → Kind

def GenericSignature.kindCorrect {N : Type u} {K : Type v} {A : Type w}
    (signature : GenericSignature N K A) (args : List A) : Prop :=
  List.Forall₂ (fun parameter arg => signature.kindOf arg = parameter.2)
    signature.parameters args

structure GenericArgumentBinding (Name Kind Arg : Type u) where
  signature : GenericSignature Name Kind Arg
  actual : Nat → Option Arg
  default : Nat → List Arg → Option Arg

namespace GenericArgumentBinding
def bindAux {N K A : Type u} [DecidableEq K] (kindOf : A → K)
    (actual : Nat → Option A) (fallback : Nat → List A → Option A) :
    List (N × K) → Nat → List A → Option (List A)
  | [], _, accumulated => some accumulated
  | (_, kind) :: rest, i, accumulated =>
    let selected := match actual i with
      | some arg => some arg
      | none => fallback i accumulated
    match selected with
    | none => none
    | some arg => if kindOf arg = kind then
        bindAux kindOf actual fallback rest (i + 1) (accumulated ++ [arg]) else none

def bind {N K A : Type u} [DecidableEq K] (binding : GenericArgumentBinding N K A) :=
  bindAux binding.signature.kindOf binding.actual binding.default binding.signature.parameters 0 []
end GenericArgumentBinding

/-- Language realization includes scope/hygiene and phase-specific semantics;
this relation does not turn instantiation into a universal partial function. -/
structure ParametricInstantiation (Env Decl Name Kind Arg Instance : Type u) where
  signature : Decl → GenericSignature Name Kind Arg
  admissible : Env → Decl → List Arg → Prop
  realizes : Env → Decl → List (Name × Arg) → Instance → Prop

def ParametricInstantiation.instantiates {E D N K A I : Type u}
    (model : ParametricInstantiation E D N K A I) (env : E) (decl : D)
    (args : List A) (instanceValue : I) : Prop :=
  (model.signature decl).kindCorrect args ∧ model.admissible env decl args ∧
    model.realizes env decl ((model.signature decl).parameters.map Prod.fst |>.zip args) instanceValue

structure JavaParameterizedType (Decl Arg Ty Member : Type u) where
  declarationValid : Decl → Prop
  arity : Decl → Nat
  referenceOrWildcard : Arg → Prop
  capture : Decl → List Arg → List Ty → Prop
  boundsHold : Decl → List Ty → Prop
  memberDeclaredType : Decl → Member → Option Ty
  substitute : Decl → List Ty → Ty → Ty
  directSupertype : Ty → Ty → Prop

namespace JavaParameterizedType
def wellFormed {D A T M : Type u} (model : JavaParameterizedType D A T M)
    (decl : D) (args : List A) : Prop :=
  model.declarationValid decl ∧ args.length = model.arity decl ∧
    (∀ a ∈ args, model.referenceOrWildcard a) ∧
    ∃ captured, model.capture decl args captured ∧
      captured.length = model.arity decl ∧ model.boundsHold decl captured

def memberType {D A T M : Type u} (model : JavaParameterizedType D A T M)
    (decl : D) (args : List A) (member : M) (out : T) : Prop :=
  model.wellFormed decl args ∧ ∃ captured original,
    model.capture decl args captured ∧ model.memberDeclaredType decl member = some original ∧
      out = model.substitute decl captured original

def subtype {D A T M : Type u} (model : JavaParameterizedType D A T M) :=
  Relation.ReflTransGen model.directSupertype
end JavaParameterizedType

inductive JavaArgument (Ty : Type u) where
  | exact : Ty → JavaArgument Ty
  | unbounded
  | upper : Ty → JavaArgument Ty
  | lower : Ty → JavaArgument Ty

structure CaptureSlot (Ty Var : Type u) where
  result : Ty
  freshVariable : Option Var
  lower : Option Ty
  upper : Option Ty

/-- Identity and intersection checks come from a language frontend. -/
structure JavaWildcardCapture (Ty Var : Type u) where
  nullType : Ty
  variableType : Var → Ty
  declaredBound : List Ty → Nat → Ty
  glb : Ty → Ty → Ty
  glbValid : Ty → Ty → Prop
  inEnvironment : Var → Prop

namespace JavaWildcardCapture
def slot {T V : Type u} (model : JavaWildcardCapture T V)
    (arg : JavaArgument T) (bound : T) (out : CaptureSlot T V) : Prop :=
  match arg with
  | .exact ty => out.result = ty ∧ out.freshVariable = none ∧ out.lower = none ∧ out.upper = none
  | .unbounded => ∃ fresh, out.freshVariable = some fresh ∧ out.result = model.variableType fresh ∧
      out.lower = some model.nullType ∧ out.upper = some bound
  | .upper ty => model.glbValid ty bound ∧ ∃ fresh,
      out.freshVariable = some fresh ∧ out.result = model.variableType fresh ∧
      out.lower = some model.nullType ∧ out.upper = some (model.glb ty bound)
  | .lower ty => ∃ fresh, out.freshVariable = some fresh ∧ out.result = model.variableType fresh ∧
      out.lower = some ty ∧ out.upper = some bound

def captures {T V : Type u} (model : JavaWildcardCapture T V)
    (args : List (JavaArgument T)) (out : List (CaptureSlot T V)) : Prop :=
  args.length = out.length ∧
    (out.filterMap CaptureSlot.freshVariable).Nodup ∧
    (∀ v ∈ out.filterMap CaptureSlot.freshVariable, ¬ model.inEnvironment v) ∧
    ∀ i arg result, args[i]? = some arg → out[i]? = some result →
      model.slot arg (model.declaredBound (out.map CaptureSlot.result) i) result
end JavaWildcardCapture

/-- Owner-sensitive nested types are deliberately absent from this core. -/
inductive JavaErasureSyntax (Class Var : Type u) where
  | named : Class → JavaErasureSyntax Class Var
  | parameterized : Class → List (JavaErasureSyntax Class Var) → JavaErasureSyntax Class Var
  | array : JavaErasureSyntax Class Var → JavaErasureSyntax Class Var
  | variable : Var → JavaErasureSyntax Class Var
  | unboundedWildcard

structure JavaTypeErasure (Class Var : Type u) where
  leftmostBound : Var → JavaErasureSyntax Class Var

namespace JavaTypeErasure
def eraseFuel {C V : Type u} (model : JavaTypeErasure C V) :
    Nat → JavaErasureSyntax C V → Option (JavaErasureSyntax C V)
  | 0, _ => none
  | _ + 1, .named c => some (.named c)
  | _ + 1, .parameterized c _ => some (.named c)
  | fuel + 1, .array ty => (eraseFuel model fuel ty).map .array
  | fuel + 1, .variable v => eraseFuel model fuel (model.leftmostBound v)
  | _ + 1, .unboundedWildcard => none
end JavaTypeErasure

structure JavaTypeInference (Var Ty Constraint : Type u) where
  proper : Ty → Prop
  inScope : Ty → Prop
  satisfies : (Var → Ty) → Constraint → Prop
  resolve : List Constraint → Option (Var → Ty)
  resolution_sound : ∀ constraints assignment, resolve constraints = some assignment →
    (∀ v, proper (assignment v) ∧ inScope (assignment v)) ∧
      ∀ c ∈ constraints, satisfies assignment c

def JavaTypeInference.solutions {V T C : Type u} (model : JavaTypeInference V T C)
    (constraints : List C) (assignment : V → T) : Prop :=
  (∀ v, model.proper (assignment v) ∧ model.inScope (assignment v)) ∧
    ∀ c ∈ constraints, model.satisfies assignment c

inductive VHDLGenericKind where
  | constant
  | typeFormal
  | subprogram
  | packageFormal
  deriving DecidableEq

inductive GenericAssociation (Name Actual : Type u) where
  | positional : Actual → GenericAssociation Name Actual
  | named : Name → Actual → GenericAssociation Name Actual

structure VHDLGenericInterface (Name Actual : Type u) where
  signature : GenericSignature Name VHDLGenericKind Actual
  compatible : Nat → Actual → Prop
  allowedDefault : Nat → Prop

namespace VHDLGenericInterface
def findName {N : Type u} [DecidableEq N] (name : N) : List (N × VHDLGenericKind) → Option Nat
  | [] => none
  | (other, _) :: rest => if name = other then some 0 else (findName name rest).map (· + 1)

def normalizeAux {N A : Type u} [DecidableEq N]
    (parameters : List (N × VHDLGenericKind)) :
    List (GenericAssociation N A) → Nat → Bool → (Nat → Option A) → Option (Nat → Option A)
  | [], _, _, slots => some slots
  | .positional actual :: rest, nextIndex, namedSeen, slots =>
    if namedSeen || nextIndex ≥ parameters.length then none else
      match slots nextIndex with
      | some _ => none
      | none => normalizeAux parameters rest (nextIndex + 1) false
          (_root_.Function.update slots nextIndex (some actual))
  | .named name actual :: rest, nextIndex, _, slots =>
    match findName name parameters with
    | none => none
    | some index => match slots index with
      | some _ => none
      | none => normalizeAux parameters rest nextIndex true
          (_root_.Function.update slots index (some actual))

def normalize {N A : Type u} [DecidableEq N] (interface : VHDLGenericInterface N A)
    (associations : List (GenericAssociation N A)) :=
  normalizeAux interface.signature.parameters associations 0 false (fun _ => none)
end VHDLGenericInterface

/-- Events are in formal declaration order. Language-specific evaluation,
subtype/profile checks and staticness classification remain supplied. -/
structure VHDLGenericElaboration (Env Event Instance : Type u) where
  step : Env → Event → Option Env
  finish : Env → Option Instance
  locallyStatic : Env → Event → Prop
  globallyStatic : Env → Event → Prop

namespace VHDLGenericElaboration
def runEvents {E A I : Type u} (model : VHDLGenericElaboration E A I) :
    E → List A → Option E
  | env, [] => some env
  | env, event :: rest => match model.step env event with
    | none => none
    | some next => runEvents model next rest

def elaborate {E A I : Type u} (model : VHDLGenericElaboration E A I)
    (env : E) (events : List A) : Option I :=
  match model.runEvents env events with
  | none => none
  | some finalEnv => model.finish finalEnv

def forGenerate {Index Block : Type u} (rangeValues : List Index) (body : Index → Block) :=
  rangeValues.map body

def ifGenerate {Block : Type u} (condition : Bool) (body : Block) : List Block :=
  if condition then [body] else []
end VHDLGenericElaboration

end Catalog.Generics
