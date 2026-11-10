module

public import Catalog.StructuredData
public import Mathlib.Data.Finset.Basic

@[expose] public section

namespace Catalog.TMP
universe u v w x

inductive TemplateArgument (Ty : Type u) (Constant : Type v) (Template : Type w) where
  | typeArg : Ty → TemplateArgument Ty Constant Template
  | valueArg : Constant → TemplateArgument Ty Constant Template
  | templateArg : Template → TemplateArgument Ty Constant Template

/-- Fixed-environment observation. This Option-valued semantic function is not
an algorithm deciding arbitrary C++ instantiation or nontermination. -/
structure TemplateMetafunction (Arg : Type u) (Result : Type v) where
  wellKinded : List Arg → Prop
  apply : List Arg → Option Result
  domain_kinded : ∀ args, (apply args).isSome → wellKinded args

def TemplateMetafunction.compose {A : Type u} {B : Type v} {C : Type w}
    (f : A → Option B) (g : B → Option C) (a : A) : Option C :=
  match f a with
  | none => none
  | some b => g b

inductive Selection (S : Type u) where
  | primary : Selection S
  | chosen : S → Selection S
  | ambiguous : Selection S

structure TemplateSpecialization (S : Type u) (Args : Type v) where
  matchSet : Args → Finset S
  moreSpecialized : S → S → Prop
  irreflexive : ∀ s, ¬ moreSpecialized s s
  transitive : ∀ a b c, moreSpecialized a b → moreSpecialized b c → moreSpecialized a c

def TemplateSpecialization.winner {S : Type u} {A : Type v}
    (system : TemplateSpecialization S A) (args : A) (s : S) : Prop :=
  s ∈ system.matchSet args ∧ ∀ t ∈ system.matchSet args, t ≠ s → system.moreSpecialized s t

noncomputable def TemplateSpecialization.select {S : Type u} {A : Type v}
    (system : TemplateSpecialization S A) (args : A) : Selection S := by
  classical
  exact if system.matchSet args = ∅ then .primary
    else if h : ∃ s, system.winner args s then .chosen (Classical.choose h) else .ambiguous

inductive SubstitutionEvent where
  | continue
  | immediateInvalid
  | requiredHardError

inductive SubstitutionStatus where
  | success
  | deductionFailure
  | hardError
  deriving DecidableEq

def scanSubstitution : List SubstitutionEvent → SubstitutionStatus
  | [] => .success
  | .continue :: events => scanSubstitution events
  | .immediateInvalid :: _ => .deductionFailure
  | .requiredHardError :: _ => .hardError

/-- The compiler-specific frontend remains supplied, with a success artifact.
Unsupported/IFNDR cases are excluded before using this interface. -/
structure TemplateSubstitution (Env : Type u) (Subst : Type v)
    (Syntax : Type w) (Artifact : Type x) where
  frontend : Env → Subst → Syntax → List SubstitutionEvent × Option Artifact
  success_artifact : ∀ env subst term,
    scanSubstitution (frontend env subst term).1 = .success →
      (frontend env subst term).2.isSome

inductive ConstraintStatus where
  | satisfied
  | unsatisfied
  | illFormed
  deriving DecidableEq

/-- Atom carries a resolved source-origin/parameter-map identity, not merely a
Boolean evaluator. Actual C++ normalization is a separate frontend obligation. -/
inductive TemplateConstraint (Atom : Type u) where
  | atom : Atom → TemplateConstraint Atom
  | conj : TemplateConstraint Atom → TemplateConstraint Atom → TemplateConstraint Atom
  | disj : TemplateConstraint Atom → TemplateConstraint Atom → TemplateConstraint Atom

namespace TemplateConstraint
def satisfy {A : Type u} (check : A → ConstraintStatus) : TemplateConstraint A → ConstraintStatus
  | .atom a => check a
  | .conj p q => match satisfy check p with
    | .satisfied => satisfy check q
    | .unsatisfied => .unsatisfied
    | .illFormed => .illFormed
  | .disj p q => match satisfy check p with
    | .satisfied => .satisfied
    | .unsatisfied => satisfy check q
    | .illFormed => .illFormed

def distribute {A : Type u} (left right : List (List A)) : List (List A) :=
  left.flatMap fun p => right.map fun q => p ++ q

def dnf {A : Type u} : TemplateConstraint A → List (List A)
  | .atom a => [[a]]
  | .conj p q => distribute (dnf p) (dnf q)
  | .disj p q => dnf p ++ dnf q

def cnf {A : Type u} : TemplateConstraint A → List (List A)
  | .atom a => [[a]]
  | .conj p q => cnf p ++ cnf q
  | .disj p q => distribute (cnf p) (cnf q)

def subsumes {A : Type u} (p q : TemplateConstraint A) : Prop :=
  ∀ left ∈ p.dnf, ∀ right ∈ q.cnf, ∃ a ∈ left, ∃ b ∈ right, a = b
end TemplateConstraint

abbrev TemplateParameterPack (A : Type u) := List A

namespace TemplateParameterPack
def expand {A : Type u} {B : Type v} (f : A → B) (pack : TemplateParameterPack A) :=
  pack.map f

def zipExpand {A : Type u} {B : Type v} {C : Type w}
    (f : A → B → C) (left : TemplateParameterPack A) (right : TemplateParameterPack B) :
    Option (TemplateParameterPack C) :=
  if left.length = right.length then some (List.zipWith f left right) else none

inductive FoldExpr (Op : Type u) (A : Type v) where
  | leaf : A → FoldExpr Op A
  | node : Op → FoldExpr Op A → FoldExpr Op A → FoldExpr Op A

def foldLeft {Op : Type u} {A : Type v} (op : Op)
    (initial : FoldExpr Op A) (pack : List (FoldExpr Op A)) : FoldExpr Op A :=
  pack.foldl (fun left right => .node op left right) initial

def foldRight {Op : Type u} {A : Type v} (op : Op)
    (initial : FoldExpr Op A) (pack : List (FoldExpr Op A)) : FoldExpr Op A :=
  pack.foldr (fun left right => .node op left right) initial
end TemplateParameterPack

/-- All candidate sets have already passed the relevant language lookup rules. -/
structure DependentNameLookup (Decl : Type u) where
  ordinaryDefinition : Finset Decl
  adlDefinition : Finset Decl
  adlInstantiation : Finset Decl
  adlEnabled : Bool

def DependentNameLookup.candidates {D : Type u} [DecidableEq D]
    (lookup : DependentNameLookup D) : Finset D :=
  if lookup.adlEnabled then
    lookup.ordinaryDefinition ∪ lookup.adlDefinition ∪ lookup.adlInstantiation
  else lookup.ordinaryDefinition

/-- Small pure expression language, not a complete C++ constexpr machine. -/
inductive CompileTimeEvaluation where
  | lit : Int → CompileTimeEvaluation
  | add : CompileTimeEvaluation → CompileTimeEvaluation → CompileTimeEvaluation
  | mul : CompileTimeEvaluation → CompileTimeEvaluation → CompileTimeEvaluation
  | branch : Bool → CompileTimeEvaluation → CompileTimeEvaluation → CompileTimeEvaluation

namespace CompileTimeEvaluation
abbrev inRange (width : Nat) (value : Int) : Prop :=
  -(2 : Int) ^ (width - 1) ≤ value ∧ value ≤ (2 : Int) ^ (width - 1) - 1

def checked (width : Nat) (value : Int) : Option Int :=
  if inRange width value then some value else none

def evaluate (width : Nat) : CompileTimeEvaluation → Option Int
  | .lit z => checked width z
  | .add e f => do
    let x ← evaluate width e
    let y ← evaluate width f
    checked width (x + y)
  | .mul e f => do
    let x ← evaluate width e
    let y ← evaluate width f
    checked width (x * y)
  | .branch b e f => if b then evaluate width e else evaluate width f
end CompileTimeEvaluation

end Catalog.TMP
