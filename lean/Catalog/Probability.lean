module

public import Catalog.Graphs
public import Mathlib.MeasureTheory.Measure.ProbabilityMeasure
public import Mathlib.MeasureTheory.Measure.Map
public import Mathlib.Probability.ProbabilityMassFunction.Basic

@[expose] public section

namespace Catalog
universe u v
open MeasureTheory
open scoped ENNReal

abbrev MeasurableSpace (A : Type u) := _root_.MeasurableSpace A
abbrev MeasureSpace (A : Type u) := MeasureTheory.MeasureSpace A
abbrev MeasurableFunction (A : Type u) (B : Type v)
    [_root_.MeasurableSpace A] [_root_.MeasurableSpace B] :=
  {f : A → B // Measurable f}

abbrev ProbabilitySpace (A : Type u) [_root_.MeasurableSpace A] := ProbabilityMeasure A

abbrev RandomVariable {A : Type u} (B : Type v)
    [_root_.MeasurableSpace A] [_root_.MeasurableSpace B] (_ : ProbabilitySpace A) :=
  MeasurableFunction A B

noncomputable def randomVariableLaw {A : Type u} {B : Type v}
    [_root_.MeasurableSpace A] [_root_.MeasurableSpace B]
    (P : ProbabilitySpace A) (X : RandomVariable B P) : Measure B :=
  Measure.map X.val P.val

/-- Conditioning on a null event is excluded by the argument type. -/
noncomputable def ConditionalProbability {A : Type u} [_root_.MeasurableSpace A]
    (P : ProbabilitySpace A) (event givenEvent : _root_.Set A)
    (_ : MeasurableSet event) (_ : MeasurableSet givenEvent)
    (_ : 0 < P.val givenEvent) : ℝ :=
  (P.val (event ∩ givenEvent)).toReal / (P.val givenEvent).toReal

/-- A finite-state homogeneous generative kernel. Path probabilities are defined
below; constructing an infinite process and its conditional Markov property is
a separate obligation. -/
structure MarkovChain (S : Type u) [Fintype S] [Nonempty S] where
  initial : PMF S
  transition : S → PMF S

noncomputable def MarkovChain.continuation {S : Type u} [Fintype S] [Nonempty S]
    (m : MarkovChain S) : S → List S → ℝ≥0∞
  | _, [] => 1
  | s, t :: rest => m.transition s t * m.continuation t rest

noncomputable def MarkovChain.pathProbability {S : Type u} [Fintype S] [Nonempty S]
    (m : MarkovChain S) : List S → ℝ≥0∞
  | [] => 1
  | s :: rest => m.initial s * m.continuation s rest

structure BayesianNetwork (V : Type) [Fintype V] (Value : V → Type)
    [∀ v, Fintype (Value v)] [∀ v, Nonempty (Value v)] where
  dag : DAG V
  localLaw : ∀ v, ((p : {p // dag.edge p v}) → Value p.val) → PMF (Value v)

/-- Factorized joint weights. Joint normalization is not asserted as a witness. -/
noncomputable def BayesianNetwork.joint {V : Type} [Fintype V] {Value : V → Type}
    [∀ v, Fintype (Value v)] [∀ v, Nonempty (Value v)]
    (b : BayesianNetwork V Value) (assignment : ∀ v, Value v) : ℝ≥0∞ :=
  ∏ v, b.localLaw v (fun p => assignment p.val) (assignment v)

end Catalog
