module

public import Catalog.Coroutines

@[expose] public section

namespace Catalog.CoroutineProofs
universe u

def Unresumable {K R E : Type u} : CoroutineState K R E → Prop
  | .created _ | .suspended _ => False
  | _ => True

theorem step_without_yield {K I O R E : Type u} (m : AsymmetricCoroutine K I O R E)
    {s t : CoroutineState K R E} {a : CoroutineAction I O R E}
    (hs : Unresumable s) (ha : ∀ o, a ≠ .yieldValue o)
    (h : coroutineStep m s a t) : Unresumable t := by
  cases s <;> cases a <;> cases t <;> simp_all [Unresumable, coroutineStep]

theorem path_without_yield {K I O R E : Type u} (m : AsymmetricCoroutine K I O R E)
    {s t : CoroutineState K R E} {w : List (CoroutineAction I O R E)}
    (hs : Unresumable s) (hw : ∀ o, CoroutineAction.yieldValue o ∉ w)
    (hp : LabelledPath (coroutineLTS m) s w t) : Unresumable t := by
  induction hp with
  | nil => exact hs
  | cons hstep _ ih =>
    apply ih
    · exact step_without_yield m hs (by intro o he; subst he; exact (hw o) (by simp)) hstep
    · intro o ho
      exact hw o (by simp [ho])

theorem path_split {S A : Type u} (lts : LabelledTransitionSystem S A)
    {s t : S} {xs ys : List A} (hp : LabelledPath lts s (xs ++ ys) t) :
    ∃ mid, LabelledPath lts s xs mid ∧ LabelledPath lts mid ys t := by
  induction xs generalizing s with
  | nil => exact ⟨s, .nil s, hp⟩
  | cons a xs ih =>
    cases hp with
    | cons hs rest =>
      obtain ⟨mid, first, last⟩ := ih rest
      exact ⟨mid, .cons hs first, last⟩

theorem resume_target {K I O R E : Type u} (m : AsymmetricCoroutine K I O R E)
    {s t : CoroutineState K R E} {i : I} (h : coroutineStep m s (.resume i) t) :
    ∃ k, t = .running k := by
  cases s <;> cases t <;> simp_all [coroutineStep]

theorem unresumable_no_resume {K I O R E : Type u} (m : AsymmetricCoroutine K I O R E)
    {s t : CoroutineState K R E} {i : I} (hs : Unresumable s) :
    ¬ coroutineStep m s (.resume i) t := by
  cases s <;> cases t <;> simp_all [Unresumable, coroutineStep]

theorem successive_resumes_require_yield {K I O R E : Type u}
    (m : AsymmetricCoroutine K I O R E)
    (leading middle trailing : List (CoroutineAction I O R E)) (i j : I)
    (last : CoroutineState K R E)
    (hp : LabelledPath (coroutineLTS m) (.created m.entry)
      (leading ++ (.resume i :: (middle ++ (.resume j :: trailing)))) last) :
    ∃ o, CoroutineAction.yieldValue o ∈ middle := by
  classical
  by_contra hy
  have hnone : ∀ o, CoroutineAction.yieldValue o ∉ middle := by
    simpa only [not_exists] using hy
  obtain ⟨s, _, rest⟩ := path_split (coroutineLTS m) hp
  cases rest with
  | cons first tail =>
    obtain ⟨k, rfl⟩ := resume_target m first
    obtain ⟨mid, between, lastPart⟩ := path_split (coroutineLTS m) tail
    have hu := path_without_yield m (s := .running k) (by trivial) hnone between
    cases lastPart with
    | cons next _ => exact unresumable_no_resume m hu next

theorem initial_valid {T K I O R E : Type u} [Fintype T]
    (m : CooperativeScheduler T K I O R E) : cooperativeValid (cooperativeInitial m) := by
  simp [cooperativeValid, cooperativeInitial]

theorem active_not_waiting {T K R E : Type u} {s : CooperativeState T K R E}
    (hv : cooperativeValid s) {j : T} (hj : s.active = some j) : j ∉ s.waiting := by
  intro hw
  obtain ⟨k, hk⟩ := (hv.1 j).mpr hj
  obtain ⟨k', hk'⟩ := hv.2 j hw
  rw [hk] at hk'
  cases hk'

theorem replace_valid {T K R E : Type u} [DecidableEq T]
    {s : CooperativeState T K R E} (hv : cooperativeValid s)
    (j : T) (next : CoroutineState K R E) (owner : Option T)
    (hold : s.active = none ∨ s.active = some j)
    (hnew : owner = none ∨ owner = some j) (hw : j ∉ s.waiting)
    (hphase : (∃ k, next = .running k) ↔ owner = some j) :
    cooperativeValid (cooperativeUpdate s j next owner s.waiting) := by
  constructor
  · intro t
    by_cases ht : t = j
    · subst t
      simpa [cooperativeUpdate] using hphase
    · have hne : j ≠ t := Ne.symm ht
      have oldNot : s.active ≠ some t := by
        rcases hold with h | h <;> simp_all
      have newNot : owner ≠ some t := by
        rcases hnew with h | h <;> simp_all
      simpa [cooperativeUpdate, ht, hne, newNot] using (hv.1 t).not.mpr oldNot
  · intro t ht
    have hne : t ≠ j := by intro he; subst t; exact hw ht
    simpa [cooperativeUpdate, hne, Ne.symm hne] using hv.2 t ht

theorem add_waiting_valid {T K R E : Type u} {s : CooperativeState T K R E}
    (hv : cooperativeValid s) (j : T) (hj : ∃ k, s.tasks j = .suspended k) :
    cooperativeValid { s with waiting := insert j s.waiting } := by
  refine ⟨hv.1, ?_⟩
  intro t ht
  rcases ht with he | hw
  · subst t; exact hj
  · exact hv.2 t hw

theorem running_step_target {K I O R E : Type u} (m : AsymmetricCoroutine K I O R E)
    {k : K} {a : CoroutineAction I O R E} {s : CoroutineState K R E}
    (hs : coroutineStep m (.running k) a s) :
    match a with
    | .internal => ∃ k', s = .running k'
    | .yieldValue _ => ∃ k', s = .suspended k'
    | .returnValue r => s = .returned r
    | .raiseError e => s = .failed e
    | .resume _ => False := by
  cases a <;> cases s <;> simp [coroutineStep] at hs ⊢ <;> tauto

theorem step_preserves_valid {T K I O R E : Type u} [Fintype T] [DecidableEq T]
    (m : CooperativeScheduler T K I O R E)
    {s s' : CooperativeState T K R E} {a : CooperativeAction T I O R E}
    (hv : cooperativeValid s) (hs : cooperativeStep m s a s') : cooperativeValid s' := by
  cases a with
  | dispatch j i =>
    obtain ⟨hi, hw, next, hl, rfl⟩ := hs
    obtain ⟨k, rfl⟩ := resume_target (m.machine j) hl
    exact replace_valid hv j (.running k) (some j) (Or.inl hi) (Or.inr rfl) hw (by simp)
  | wake j =>
    obtain ⟨_, rfl⟩ := hs
    exact ⟨hv.1, fun t ht => hv.2 t ht.1⟩
  | internal =>
    obtain ⟨j, next, ho, hl, rfl⟩ := hs
    obtain ⟨k, hk⟩ := (hv.1 j).mpr ho
    rw [hk] at hl
    obtain ⟨k', rfl⟩ := running_step_target (m.machine j) hl
    exact replace_valid hv j (.running k') (some j) (Or.inr ho) (Or.inr rfl)
      (active_not_waiting hv ho) (by simp)
  | yieldValue o =>
    obtain ⟨j, next, ho, hl, rfl⟩ := hs
    obtain ⟨k, hk⟩ := (hv.1 j).mpr ho
    rw [hk] at hl
    obtain ⟨k', rfl⟩ := running_step_target (m.machine j) hl
    exact replace_valid hv j (.suspended k') none (Or.inr ho) (Or.inl rfl)
      (active_not_waiting hv ho) (by simp)
  | wait o =>
    obtain ⟨j, next, ho, hl, rfl⟩ := hs
    obtain ⟨k, hk⟩ := (hv.1 j).mpr ho
    rw [hk] at hl
    obtain ⟨k', rfl⟩ := running_step_target (m.machine j) hl
    have hbase := replace_valid hv j (.suspended k') none (Or.inr ho) (Or.inl rfl)
      (active_not_waiting hv ho) (by simp)
    exact add_waiting_valid hbase j ⟨k', by simp [cooperativeUpdate]⟩
  | returnValue r =>
    obtain ⟨j, next, ho, hl, rfl⟩ := hs
    obtain ⟨k, hk⟩ := (hv.1 j).mpr ho
    rw [hk] at hl
    have he := running_step_target (m.machine j) hl
    change next = .returned r at he
    subst next
    exact replace_valid hv j (.returned r) none (Or.inr ho) (Or.inl rfl)
      (active_not_waiting hv ho) (by simp)
  | raiseError e =>
    obtain ⟨j, next, ho, hl, rfl⟩ := hs
    obtain ⟨k, hk⟩ := (hv.1 j).mpr ho
    rw [hk] at hl
    have he := running_step_target (m.machine j) hl
    change next = .failed e at he
    subst next
    exact replace_valid hv j (.failed e) none (Or.inr ho) (Or.inl rfl)
      (active_not_waiting hv ho) (by simp)

theorem reachable_owner_invariant {T K I O R E : Type u} [Fintype T] [DecidableEq T]
    (m : CooperativeScheduler T K I O R E) (s : CooperativeState T K R E)
    (hr : Relation.ReflTransGen (fun a b => ∃ label, cooperativeStep m a label b)
      (cooperativeInitial m) s) : cooperativeValid s := by
  induction hr with
  | refl => exact initial_valid m
  | tail _ hs ih =>
    obtain ⟨a, ha⟩ := hs
    exact step_preserves_valid m ih ha

theorem cooperation_does_not_imply_progress {T K I O R E : Type u}
    [Fintype T] [DecidableEq T] (m : CooperativeScheduler T K I O R E)
    (s : CooperativeState T K R E) (j h : T) (k : K)
    (_hr : Relation.ReflTransGen (fun a b => ∃ label, cooperativeStep m a label b)
      (cooperativeInitial m) s)
    (hv : cooperativeValid s) (hne : j ≠ h) (ho : s.active = some j)
    (hh : h ∈ cooperativeRunnable s) (hk : s.tasks j = .running k)
    (hloop : (m.machine j).internal k k) :
    ∃ run : Nat → CooperativeState T K R E,
      run 0 = s ∧ ∀ n, run n = s ∧ cooperativeStep m (run n) .internal (run (n + 1)) ∧
        (run n).active = some j ∧ h ∈ cooperativeRunnable (run n) ∧
        ¬ (∃ k', (run n).tasks h = .running k') := by
  have hupdate : cooperativeUpdate s j (.running k) (some j) s.waiting = s := by
    cases s
    simp_all [cooperativeUpdate, Function.update_eq_self_iff]
  have hs : cooperativeStep m s .internal s := by
    refine ⟨j, .running k, ho, ?_, hupdate.symm⟩
    simpa [hk, coroutineStep] using hloop
  have notRunning : ¬ (∃ k', s.tasks h = .running k') := by
    rw [hv.1 h, ho]
    simpa using hne
  exact ⟨fun _ => s, rfl, fun _ => ⟨rfl, hs, ho, hh, notRunning⟩⟩

/-- A concrete two-task model makes the starvation hypotheses nonvacuous. -/
def loopingExamplePool : CooperativeScheduler Bool Unit Unit Unit Unit Unit where
  machine := fun _ => {
    entry := ()
    accept := fun _ _ => ()
    internal := fun _ _ => True
    yields := fun _ _ _ => False
    returns := fun _ _ => False
    raises := fun _ _ => False }

example : ∃ s : CooperativeState Bool Unit Unit Unit,
    Relation.ReflTransGen
      (fun a b => ∃ label, cooperativeStep loopingExamplePool a label b)
      (cooperativeInitial loopingExamplePool) s ∧
    cooperativeValid s ∧ s.active = some false ∧ true ∈ cooperativeRunnable s ∧
    s.tasks false = .running () ∧ (loopingExamplePool.machine false).internal () () := by
  let s := cooperativeUpdate (cooperativeInitial loopingExamplePool) false
    (.running ()) (some false) ∅
  have hs : cooperativeStep loopingExamplePool (cooperativeInitial loopingExamplePool)
      (.dispatch false ()) s := by
    refine ⟨rfl, by simp [cooperativeInitial], .running (), ?_, rfl⟩
    simp [coroutineStep, cooperativeInitial, loopingExamplePool]
  have hr : Relation.ReflTransGen
      (fun a b => ∃ label, cooperativeStep loopingExamplePool a label b)
      (cooperativeInitial loopingExamplePool) s := .tail .refl ⟨_, hs⟩
  refine ⟨s, hr, reachable_owner_invariant loopingExamplePool s hr, rfl, ?_, ?_, trivial⟩
  · change true ∉ s.waiting ∧
      ((∃ k, s.tasks true = .created k) ∨ (∃ k, s.tasks true = .suspended k))
    simp [s, cooperativeUpdate, cooperativeInitial]
  · simp [s, cooperativeUpdate]

end Catalog.CoroutineProofs
