module

public import Catalog.Graphs
public import Catalog.Logic
public import Mathlib.Tactic.FinCases

@[expose] public section

namespace Catalog
universe u

/-- 0 = false, 1 = unknown, 2 = true; order is truth order. -/
abbrev KleeneLogic := Fin 3

def kleeneNeg (a : KleeneLogic) : KleeneLogic :=
  if a = 0 then 2 else if a = 1 then 1 else 0

def kleeneAnd (a b : KleeneLogic) : KleeneLogic := min a b

def kleeneOr (a b : KleeneLogic) : KleeneLogic := max a b

def kleeneDesignated (a : KleeneLogic) : Prop := a = 2

def kleeneEval {AP : Type u} (valuation : AP → KleeneLogic) : PropFormula AP → KleeneLogic
  | .atom p => valuation p
  | .bottom => 0
  | .neg p => kleeneNeg (kleeneEval valuation p)
  | .conj p q => kleeneAnd (kleeneEval valuation p) (kleeneEval valuation q)

def kleeneConsequence {AP : Type u} (premises : Set (PropFormula AP))
    (conclusion : PropFormula AP) : Prop :=
  ∀ valuation : AP → KleeneLogic,
    (∀ p ∈ premises, kleeneEval valuation p = 2) → kleeneEval valuation conclusion = 2

theorem kleene_model_satisfaction :
    kleeneNeg 0 = 2 ∧ kleeneNeg 1 = 1 ∧ kleeneNeg 2 = 0 ∧
    (∀ a b : KleeneLogic, kleeneAnd a b = min a b ∧ kleeneOr a b = max a b) ∧
    (∀ a : KleeneLogic, kleeneDesignated a ↔ a = 2) := by
  exact ⟨rfl, rfl, rfl, fun _ _ => ⟨rfl, rfl⟩, fun _ => Iff.rfl⟩

theorem kleene_involution (a : KleeneLogic) : kleeneNeg (kleeneNeg a) = a := by
  fin_cases a <;> decide

theorem kleene_de_morgan (a b : KleeneLogic) :
    kleeneNeg (kleeneAnd a b) = kleeneOr (kleeneNeg a) (kleeneNeg b) := by
  fin_cases a <;> fin_cases b <;> decide

theorem kleene_unknown_excluded_middle :
    kleeneOr 1 (kleeneNeg 1) = 1 ∧ ¬ kleeneDesignated 1 := by
  exact ⟨rfl, by simp [kleeneDesignated]⟩

/-- Finite simple undirected forest, including empty and disconnected graphs. -/
structure AcyclicGraph (V : Type u) [Fintype V] where
  graph : SimpleGraph V
  acyclic : graph.IsAcyclic

def edgelessForest (V : Type u) [Fintype V] : AcyclicGraph V :=
  ⟨⊥, SimpleGraph.isAcyclic_bot⟩

def pathForest (n : Nat) : AcyclicGraph (Fin n) :=
  ⟨SimpleGraph.pathGraph n, SimpleGraph.isAcyclic_pathGraph n⟩

theorem forest_model_satisfaction (n : Nat) :
    (pathForest n).graph.IsAcyclic := (pathForest n).acyclic

theorem forest_path_unique {V : Type u} [Fintype V] (f : AcyclicGraph V)
    (v w : V) (p q : f.graph.Path v w) : p = q :=
  (f.acyclic.subsingleton_path v w).elim p q

end Catalog
