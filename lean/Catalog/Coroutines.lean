module

public import Catalog.Graphs
public import Mathlib.Data.Fintype.Basic

@[expose] public section

namespace Catalog
universe u

inductive CoroutineState (K R E : Type u) where
  | created : K → CoroutineState K R E
  | suspended : K → CoroutineState K R E
  | running : K → CoroutineState K R E
  | returned : R → CoroutineState K R E
  | failed : E → CoroutineState K R E

inductive CoroutineAction (I O R E : Type u) where
  | resume : I → CoroutineAction I O R E
  | internal : CoroutineAction I O R E
  | yieldValue : O → CoroutineAction I O R E
  | returnValue : R → CoroutineAction I O R E
  | raiseError : E → CoroutineAction I O R E

/-- A single coroutine and its direct caller; K contains all retained state. -/
structure AsymmetricCoroutine (K I O R E : Type u) where
  entry : K
  accept : K → I → K
  internal : K → K → Prop
  yields : K → O → K → Prop
  returns : K → R → Prop
  raises : K → E → Prop

def coroutineStep {K I O R E : Type u} (m : AsymmetricCoroutine K I O R E) :
    CoroutineState K R E → CoroutineAction I O R E → CoroutineState K R E → Prop
  | .created k, .resume i, .running k' => k' = m.accept k i
  | .suspended k, .resume i, .running k' => k' = m.accept k i
  | .running k, .internal, .running k' => m.internal k k'
  | .running k, .yieldValue o, .suspended k' => m.yields k o k'
  | .running k, .returnValue r, .returned r' => r' = r ∧ m.returns k r
  | .running k, .raiseError e, .failed e' => e' = e ∧ m.raises k e
  | _, _, _ => False

def coroutineLTS {K I O R E : Type u} (m : AsymmetricCoroutine K I O R E) :
    LabelledTransitionSystem (CoroutineState K R E) (CoroutineAction I O R E) where
  initial := { .created m.entry }
  step := coroutineStep m

def coroutineBoundary {I O R E : Type u} : CoroutineAction I O R E → Prop
  | .yieldValue _ | .returnValue _ | .raiseError _ => True
  | _ => False

def coroutineOutcomes {K I O R E : Type u} (m : AsymmetricCoroutine K I O R E)
    (s : CoroutineState K R E) (i : I) :
    _root_.Set (CoroutineAction I O R E × CoroutineState K R E) := fun (a, t) =>
  coroutineBoundary a ∧ ∃ k k',
    coroutineStep m s (.resume i) (.running k) ∧
    Relation.ReflTransGen m.internal k k' ∧ coroutineStep m (.running k') a t

structure CooperativeState (T K R E : Type u) where
  tasks : T → CoroutineState K R E
  active : Option T
  waiting : _root_.Set T

inductive CooperativeAction (T I O R E : Type u) where
  | dispatch : T → I → CooperativeAction T I O R E
  | internal : CooperativeAction T I O R E
  | yieldValue : O → CooperativeAction T I O R E
  | wait : O → CooperativeAction T I O R E
  | wake : T → CooperativeAction T I O R E
  | returnValue : R → CooperativeAction T I O R E
  | raiseError : E → CooperativeAction T I O R E

/-- Fixed finite task pool, one execution owner, explicit waiting/wakeup. -/
structure CooperativeScheduler (T K I O R E : Type u) [Fintype T] where
  machine : T → AsymmetricCoroutine K I O R E

def cooperativeInitial {T K I O R E : Type u} [Fintype T]
    (m : CooperativeScheduler T K I O R E) : CooperativeState T K R E where
  tasks := fun t => .created (m.machine t).entry
  active := none
  waiting := ∅

def cooperativeValid {T K R E : Type u} (s : CooperativeState T K R E) : Prop :=
  (∀ t, (∃ k, s.tasks t = .running k) ↔ s.active = some t) ∧
  (∀ t ∈ s.waiting, ∃ k, s.tasks t = .suspended k)

def cooperativeRunnable {T K R E : Type u} (s : CooperativeState T K R E) : _root_.Set T :=
  fun t => t ∉ s.waiting ∧
    ((∃ k, s.tasks t = .created k) ∨ (∃ k, s.tasks t = .suspended k))

def cooperativeUpdate {T K R E : Type u} [DecidableEq T]
    (s : CooperativeState T K R E) (t : T) (state : CoroutineState K R E)
    (active : Option T) (waiting : _root_.Set T) : CooperativeState T K R E where
  tasks := Function.update s.tasks t state
  active := active
  waiting := waiting

def cooperativeStep {T K I O R E : Type u} [Fintype T] [DecidableEq T]
    (m : CooperativeScheduler T K I O R E) (s : CooperativeState T K R E)
    (a : CooperativeAction T I O R E) (s' : CooperativeState T K R E) : Prop :=
  match a with
  | .dispatch t i => s.active = none ∧ t ∉ s.waiting ∧ ∃ next,
      coroutineStep (m.machine t) (s.tasks t) (.resume i) next ∧
      s' = cooperativeUpdate s t next (some t) s.waiting
  | .internal => ∃ t next, s.active = some t ∧
      coroutineStep (m.machine t) (s.tasks t) .internal next ∧
      s' = cooperativeUpdate s t next (some t) s.waiting
  | .yieldValue o => ∃ t next, s.active = some t ∧
      coroutineStep (m.machine t) (s.tasks t) (.yieldValue o) next ∧
      s' = cooperativeUpdate s t next none s.waiting
  | .wait o => ∃ t next, s.active = some t ∧
      coroutineStep (m.machine t) (s.tasks t) (.yieldValue o) next ∧
      s' = cooperativeUpdate s t next none (insert t s.waiting)
  | .wake t => t ∈ s.waiting ∧ s' = { s with waiting := s.waiting \ {t} }
  | .returnValue r => ∃ t next, s.active = some t ∧
      coroutineStep (m.machine t) (s.tasks t) (.returnValue r) next ∧
      s' = cooperativeUpdate s t next none s.waiting
  | .raiseError e => ∃ t next, s.active = some t ∧
      coroutineStep (m.machine t) (s.tasks t) (.raiseError e) next ∧
      s' = cooperativeUpdate s t next none s.waiting

def cooperativeLTS {T K I O R E : Type u} [Fintype T] [DecidableEq T]
    (m : CooperativeScheduler T K I O R E) :
    LabelledTransitionSystem (CooperativeState T K R E) (CooperativeAction T I O R E) where
  initial := { cooperativeInitial m }
  step := cooperativeStep m

/-- Local compiler checks; these are not registered catalog proof witnesses. -/
example {K I O R E : Type u} (m : AsymmetricCoroutine K I O R E)
    (r : R) (a : CoroutineAction I O R E) (s : CoroutineState K R E) :
    ¬ coroutineStep m (.returned r) a s := by
  cases a <;> cases s <;> simp [coroutineStep]

example {K I O R E : Type u} (m : AsymmetricCoroutine K I O R E)
    (k : K) (i : I) (s : CoroutineState K R E) :
    ¬ coroutineStep m (.running k) (.resume i) s := by
  cases s <;> simp [coroutineStep]

end Catalog
