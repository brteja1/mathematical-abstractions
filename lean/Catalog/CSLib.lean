module

public import Catalog.Graphs
public import Cslib.Foundations.Semantics.LTS.Bisimulation

/-! Interoperability with the pinned CSLib. Initial states remain explicit:
`Cslib.LTS` contains only a transition relation. No hiding or fairness is added. -/

@[expose] public section

namespace Catalog.CSLib
universe u v w

variable {S : Type u} {Act : Type v}

def toLTS (t : LabelledTransitionSystem S Act) : Cslib.LTS S Act where
  Tr := t.step

def fromLTS (t : Cslib.LTS S Act) (initial : Set S) :
    LabelledTransitionSystem S Act where
  initial := initial
  step := t.Tr

theorem roundTrip (t : LabelledTransitionSystem S Act) :
    fromLTS (toLTS t) t.initial = t := rfl

theorem labelledPath_iff (t : LabelledTransitionSystem S Act)
    (s : S) (word : List Act) (e : S) :
    LabelledPath t s word e ↔ (toLTS t).MTr s word e := by
  constructor
  · intro h
    induction h with
    | nil => exact .refl
    | cons step _ ih => exact .stepL step ih
  · intro h
    induction h with
    | refl => exact .nil _
    | stepL step _ ih => exact .cons step ih

theorem finiteTraces_eq (t : LabelledTransitionSystem S Act) (s : S) :
    finiteTraces t s = (toLTS t).traces s := by
  funext word
  apply propext
  exact exists_congr (fun e => labelledPath_iff t s word e)

/-- Strong step matching preserves the relation and the common label carrier. -/
theorem simulation_iff {T : Type w} (s : LabelledTransitionSystem S Act)
    (t : LabelledTransitionSystem T Act) (r : S → T → Prop) :
    Simulation s t r ↔ Cslib.LTS.IsSimulation (toLTS s) (toLTS t) r := by
  constructor
  · intro h x y hr a x' ht
    exact h x y hr a x' ht
  · intro h x y hr a x' ht
    exact h hr a x' ht

/-- Match both directions with the same relation, rather than independent simulations. -/
theorem bisimulation_iff {T : Type w} (s : LabelledTransitionSystem S Act)
    (t : LabelledTransitionSystem T Act) (r : S → T → Prop) :
    Bisimulation s t r ↔ Cslib.LTS.IsBisimulation (toLTS s) (toLTS t) r := by
  rw [Cslib.LTS.IsBisimulation.isSimulation_iff]
  exact and_congr (simulation_iff s t r) (simulation_iff t s (fun y x => r x y))

/-- The catalog's fixed-system profile is obtained by setting `s = t`. -/
theorem traceEquivalence_iff {T : Type w} (s : LabelledTransitionSystem S Act)
    (t : LabelledTransitionSystem T Act) (x : S) (y : T) :
    TraceEquivalence s t x y ↔ Cslib.LTS.TraceEq (toLTS s) (toLTS t) x y := by
  unfold TraceEquivalence Cslib.LTS.TraceEq
  rw [finiteTraces_eq, finiteTraces_eq]

end Catalog.CSLib
