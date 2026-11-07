module

public import Catalog.Graphs

@[expose] public section

namespace Catalog
universe u v

abbrev Command (S : Type u) := S → S → Prop

def HoareTriple {S : Type u} (P : S → Prop) (C : Command S) (Q : S → Prop) : Prop :=
  ∀ s t, P s → C s t → Q t

def seq {S : Type u} (C D : Command S) : Command S :=
  fun s t => ∃ m, C s m ∧ D m t

structure LoopInvariant {S : Type u} (P guard : S → Prop) (C : Command S)
    (I : S → Prop) : Prop where
  initial : ∀ s, P s → I s
  preserved : ∀ s t, I s → guard s → C s t → I t

structure TerminationVariant {S : Type u} {W : Type v} (C : Command S)
    (r : W → W → Prop) where
  measure : S → W
  wellFounded : WellFounded r
  decreasing : ∀ s t, C s t → r (measure t) (measure s)

/-- All normal outcomes and an explicit operational termination/no-fault predicate.
The client must connect this predicate to its own execution/scheduler semantics. -/
structure TotalCommand (S : Type u) where
  normal : Command S
  allTerminateNormally : S → Prop
  hasOutcome : ∀ s, allTerminateNormally s → ∃ t, normal s t

def WeakestPrecondition {S : Type u} (C : TotalCommand S) (Q : S → Prop) (s : S) : Prop :=
  C.allTerminateNormally s ∧ ∀ t, C.normal s t → Q t

def extendsPrefix {A : Type u} (word : List A) (trace : Nat → A) : Prop :=
  ∀ i : Fin word.length, trace i.val = word[i]

def SafetyProperty {A : Type u} (P : (Nat → A) → Prop) : Prop :=
  ∀ trace, ¬ P trace → ∃ n, ∀ other,
    (∀ i, i < n → other i = trace i) → ¬ P other

def LivenessProperty {A : Type u} (P : (Nat → A) → Prop) : Prop :=
  ∀ word : List A, ∃ trace, extendsPrefix word trace ∧ P trace

structure HappensBefore (E : Type u) where
  processOrder : E → E → Prop
  sendReceive : E → E → Prop
  acyclic : ∀ e, ¬ Relation.TransGen (fun a b => processOrder a b ∨ sendReceive a b) e e

def HappensBefore.rel {E : Type u} (h : HappensBefore E) :=
  Relation.TransGen (fun a b => h.processOrder a b ∨ h.sendReceive a b)

/-- Abstract history interface: clients supply well-formedness, projections,
completion, legality and real-time order. No scheduler policy is implicit. -/
structure HistoryModel (H S : Type u) where
  wellFormed : H → Prop
  completed : H → Prop
  legal : S → Prop
  equivalent : H → S → Prop
  processOrderPreserved : H → S → Prop
  realTimePreserved : H → S → Prop
  permissibleCompletion : H → H → Prop

def SequentialConsistency {H S : Type u} (m : HistoryModel H S) (h : H) : Prop :=
  m.wellFormed h ∧ m.completed h ∧ ∃ s,
    m.legal s ∧ m.equivalent h s ∧ m.processOrderPreserved h s

def Linearizability {H S : Type u} (m : HistoryModel H S) (h : H) : Prop :=
  m.wellFormed h ∧ ∃ completed s,
    m.permissibleCompletion h completed ∧ m.completed completed ∧
    m.legal s ∧ m.equivalent completed s ∧ m.processOrderPreserved completed s ∧
    m.realTimePreserved h s

end Catalog
