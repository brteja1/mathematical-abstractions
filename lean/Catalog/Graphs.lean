module

public import Mathlib.Combinatorics.SimpleGraph.Acyclic
public import Mathlib.Logic.Relation

@[expose] public section

namespace Catalog
universe u v w

/-- Finite simple undirected graph, excluding loops and multiedges. -/
abbrev Graph (V : Type u) [Fintype V] := SimpleGraph V
abbrev DirectedGraph (V : Type u) := V → V → Prop

structure DAG (V : Type u) where
  edge : DirectedGraph V
  acyclic : ∀ v, ¬ Relation.TransGen edge v v

structure Tree (V : Type u) [Fintype V] where
  graph : SimpleGraph V
  nonempty : Nonempty V
  isTree : graph.IsTree

structure TransitionSystem (S : Type u) where
  initial : _root_.Set S
  next : S → S → Prop

def reachable {S : Type u} (t : TransitionSystem S) (s : S) : Prop :=
  ∃ i ∈ t.initial, Relation.ReflTransGen t.next i s

structure LabelledTransitionSystem (S : Type u) (Act : Type v) where
  initial : _root_.Set S
  step : S → Act → S → Prop

inductive LabelledPath {S : Type u} {Act : Type v}
    (t : LabelledTransitionSystem S Act) : S → List Act → S → Prop where
  | nil (s) : LabelledPath t s [] s
  | cons {s m e a w} : t.step s a m → LabelledPath t m w e → LabelledPath t s (a :: w) e

def finiteTraces {S : Type u} {Act : Type v} (t : LabelledTransitionSystem S Act)
    (s : S) : _root_.Set (List Act) := fun w => ∃ e, LabelledPath t s w e

def Simulation {S : Type u} {T : Type v} {Act : Type w}
    (s : LabelledTransitionSystem S Act) (t : LabelledTransitionSystem T Act)
    (r : S → T → Prop) : Prop :=
  ∀ x y, r x y → ∀ a x', s.step x a x' → ∃ y', t.step y a y' ∧ r x' y'

def Bisimulation {S : Type u} {T : Type v} {Act : Type w}
    (s : LabelledTransitionSystem S Act) (t : LabelledTransitionSystem T Act)
    (r : S → T → Prop) : Prop :=
  Simulation s t r ∧ Simulation t s (fun y x => r x y)

def TraceEquivalence {S : Type u} {T : Type v} {Act : Type w}
    (s : LabelledTransitionSystem S Act) (t : LabelledTransitionSystem T Act)
    (x : S) (y : T) : Prop := finiteTraces s x = finiteTraces t y

structure KripkeStructure (S : Type u) (AP : Type v) [Fintype S] where
  initial : _root_.Set S
  next : S → S → Prop
  serial : ∀ s, ∃ t, next s t
  label : S → _root_.Set AP

end Catalog
