module

public import Catalog.Graphs
public import Cslib.Foundations.Semantics.LTS.Basic

/-! Interoperability with the pinned CSLib. Initial states remain explicit:
`Cslib.LTS` contains only a transition relation. No hiding or fairness is added. -/

@[expose] public section

namespace Catalog.CSLib
universe u v

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

end Catalog.CSLib
