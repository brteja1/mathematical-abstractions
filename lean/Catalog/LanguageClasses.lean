module

public import Catalog.Languages
public import Mathlib.Computability.RegularExpressions

@[expose] public section

namespace Catalog
open scoped Computability

abbrev RegularExpression (A : Type) [Fintype A] := _root_.RegularExpression A

/-- Existence of a finite-nonterminal grammar, rather than a chosen representation. -/
def ContextFreeLanguage {A : Type} [Fintype A] (L : Language A) : Prop :=
  ∃ g : Catalog.ContextFreeGrammar A, g.grammar.language = L

theorem regex_model_satisfaction {A : Type} [Fintype A] :
    (RegularExpression.zero : Catalog.RegularExpression A).matches' = 0 ∧
    (RegularExpression.epsilon : Catalog.RegularExpression A).matches' = 1 ∧
    (∀ a : A, (_root_.RegularExpression.char a).matches' = {[a]}) ∧
    (∀ r s : Catalog.RegularExpression A, (r + s).matches' = r.matches' + s.matches') ∧
    (∀ r s : Catalog.RegularExpression A, (r * s).matches' = r.matches' * s.matches') ∧
    (∀ r : Catalog.RegularExpression A, r.star.matches' = r.matches'∗) := by
  exact ⟨rfl, rfl, fun _ => rfl, fun _ _ => rfl, fun _ _ => rfl, fun _ => rfl⟩

theorem regex_syntax_distinct {A : Type} [Fintype A] :
    (0 : Catalog.RegularExpression A) ≠ 1 := by
  intro h
  cases h

theorem regex_union_idempotent {A : Type} [Fintype A]
    (r : Catalog.RegularExpression A) : (r + r).matches' = r.matches' := by
  change (r.matches' ∪ r.matches' : Set (List A)) = r.matches'
  exact Set.union_self _

theorem regex_concat_associative {A : Type} [Fintype A]
    (r s t : Catalog.RegularExpression A) :
    ((r * s) * t).matches' = (r * (s * t)).matches' := by
  change (r.matches' * s.matches') * t.matches' = r.matches' * (s.matches' * t.matches')
  exact mul_assoc _ _ _

theorem regex_star_empty_word {A : Type} [Fintype A]
    (r : Catalog.RegularExpression A) : [] ∈ r.star.matches' :=
  Language.nil_mem_kstar _

theorem regex_match_correct {A : Type} [Fintype A] [DecidableEq A]
    (r : Catalog.RegularExpression A) (w : List A) :
    r.rmatch w = true ↔ w ∈ r.matches' :=
  _root_.RegularExpression.rmatch_iff_matches' r w

theorem cfl_model_satisfaction {A : Type} [Fintype A] (L : Language A) :
    Catalog.ContextFreeLanguage L ↔
      ∃ g : Catalog.ContextFreeGrammar A, g.grammar.language = L := Iff.rfl

theorem cfl_extensional_transfer {A : Type} [Fintype A] (L M : Language A)
    (h : L = M) (hL : Catalog.ContextFreeLanguage L) :
    Catalog.ContextFreeLanguage M := h ▸ hL

theorem cfl_reversal {A : Type} [Fintype A] (L : Language A)
    (hL : Catalog.ContextFreeLanguage L) : Catalog.ContextFreeLanguage L.reverse := by
  obtain ⟨g, rfl⟩ := hL
  refine ⟨⟨g.grammar.reverse, g.finite_nonterminals⟩, ?_⟩
  exact _root_.ContextFreeGrammar.language_reverse

def emptyCFGrammar (A : Type) [Fintype A] : Catalog.ContextFreeGrammar A :=
  ⟨⟨Unit, (), ∅⟩, inferInstance⟩

theorem cfl_empty {A : Type} [Fintype A] :
    Catalog.ContextFreeLanguage (0 : Language A) := by
  refine ⟨emptyCFGrammar A, ?_⟩
  apply _root_.ContextFreeGrammar.language_eq_zero_of_forall_input_ne_initial
  intro r hr
  exact False.elim (Finset.notMem_empty r hr)

def epsilonCFGrammar (A : Type) [Fintype A] : Catalog.ContextFreeGrammar A :=
  ⟨⟨Unit, (), {⟨(), []⟩}⟩, inferInstance⟩

theorem cfl_nonempty_example {A : Type} [Fintype A] :
    Catalog.ContextFreeLanguage (epsilonCFGrammar A).grammar.language ∧
      [] ∈ (epsilonCFGrammar A).grammar.language := by
  constructor
  · exact ⟨epsilonCFGrammar A, rfl⟩
  · apply _root_.ContextFreeGrammar.Produces.single
    refine ⟨⟨(), []⟩, ?_, ?_⟩
    · exact Finset.mem_singleton_self _
    · exact ContextFreeRule.Rewrites.input_output

end Catalog
