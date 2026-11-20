module

public import Mathlib.Data.Finset.Sort
public import Mathlib.Analysis.SpecialFunctions.Log.Basic
public import Mathlib.Data.Rat.Defs
public import Mathlib.Tactic.NormNum

@[expose] public section
namespace Catalog
universe u v w

/-- Exact scores; smaller lexicographic keys mean earlier results. -/
abbrev RankedRetrieval (D : Type u) := D → ℝ

noncomputable def retrievalKeys {D : Type u} [LinearOrder D]
    (s : Finset D) (score : RankedRetrieval D) : List (ℝ ×ₗ D) := by
  classical
  exact (s.image (fun d => toLex (-score d, d))).sort (· ≤ ·)

theorem retrieval_model_satisfaction {D : Type u} [LinearOrder D]
    (s : Finset D) (score : RankedRetrieval D) :
    (retrievalKeys s score).Nodup ∧
    (retrievalKeys s score).Pairwise (· ≤ ·) ∧
    (retrievalKeys s score).toFinset = s.image (fun d => toLex (-score d, d)) := by
  classical
  exact ⟨Finset.sort_nodup .., Finset.pairwise_sort .., Finset.sort_toFinset ..⟩

/-- Positive-length finite corpus, with lengths and document frequencies derived from counts. -/
structure BM25 (T : Type u) (D : Type v) [Fintype T] where
  docs : Finset D
  tf : T → D → ℕ
  nonempty : docs.Nonempty
  positiveLength : ∀ d ∈ docs, 0 < ∑ t, tf t d
  k1 : ℝ
  b : ℝ
  k1_pos : 0 < k1
  b_range : 0 ≤ b ∧ b ≤ 1

noncomputable def bm25Length {T D} [Fintype T] (m : BM25 T D) (d : D) : ℝ :=
  ∑ t, (m.tf t d : ℝ)

noncomputable def bm25Average {T D} [Fintype T] (m : BM25 T D) : ℝ :=
  (∑ d ∈ m.docs, bm25Length m d) / m.docs.card

noncomputable def bm25DF {T D} [Fintype T] (m : BM25 T D) (t : T) : ℕ := by
  classical
  exact (m.docs.filter (fun d => 0 < m.tf t d)).card

noncomputable def bm25IDF {T D} [Fintype T] (m : BM25 T D) (t : T) : ℝ :=
  Real.log (1 + ((m.docs.card : ℝ) - (bm25DF m t) + 1/2) / ((bm25DF m t) + 1/2))

noncomputable def bm25Term {T D} [Fintype T] (m : BM25 T D) (t : T) (d : D) : ℝ :=
  (bm25IDF m t) * (m.tf t d : ℝ) /
    ((m.tf t d : ℝ) + m.k1 * (1 - m.b + m.b * bm25Length m d / bm25Average m))

noncomputable def bm25Score {T D} [Fintype T] (m : BM25 T D)
    (q : Finset T) (d : D) : ℝ := ∑ t ∈ q, bm25Term m t d

def unitBM25 : BM25 Unit Unit where
  docs := {()}
  tf := fun _ _ => 1
  nonempty := by simp
  positiveLength := by simp
  k1 := 1
  b := 0
  k1_pos := by norm_num
  b_range := by norm_num

theorem bm25_model_satisfaction :
    unitBM25.docs.Nonempty ∧ (∀ d ∈ unitBM25.docs, 0 < ∑ t, unitBM25.tf t d) ∧
    0 < unitBM25.k1 ∧ 0 ≤ unitBM25.b ∧ unitBM25.b ≤ 1 := by
  exact ⟨unitBM25.nonempty, unitBM25.positiveLength, unitBM25.k1_pos, unitBM25.b_range⟩

theorem bm25_zero_term {T D} [Fintype T] (m : BM25 T D) (t : T) (d : D)
    (h : m.tf t d = 0) : bm25Term m t d = 0 := by
  simp [bm25Term, h]

theorem bm25_empty_query {T D} [Fintype T] (m : BM25 T D) (d : D) :
    bm25Score m ∅ d = 0 := by simp [bm25Score]

/-- Finite unique-hit tables: guards can leave inputs unmatched. -/
structure DecisionTable (X : Type u) (R : Type v) (V : Type w) where
  rules : Finset R
  guard : R → X → Prop
  verdict : R → V
  uniqueHit : ∀ x, ∀ r ∈ rules, ∀ s ∈ rules, guard r x → guard s x → r = s

noncomputable def tableMatches {X R V} (m : DecisionTable X R V) (x : X) : Finset R := by
  classical
  exact m.rules.filter (fun r => m.guard r x)

noncomputable def tableFeasible {X R V} (m : DecisionTable X R V) : Finset R := by
  classical
  exact m.rules.filter (fun r => ∃ x, m.guard r x)

noncomputable def tableExercised {X R V} (m : DecisionTable X R V) (suite : Finset X) : Finset R := by
  classical
  exact m.rules.filter (fun r => ∃ x ∈ suite, m.guard r x)

def booleanTable : DecisionTable Bool Bool Unit where
  rules := Finset.univ
  guard := fun r x => r = x
  verdict := fun _ => ()
  uniqueHit := by intro x r _ s _ hr hs; exact hr.trans hs.symm

theorem decision_model_satisfaction :
    (∀ x, ∀ r ∈ booleanTable.rules, ∀ s ∈ booleanTable.rules,
      booleanTable.guard r x → booleanTable.guard s x → r = s) ∧
    (∀ x : Bool, ∃ r ∈ booleanTable.rules, booleanTable.guard r x) := by
  refine ⟨booleanTable.uniqueHit, ?_⟩
  intro x
  exact ⟨x, Finset.mem_univ x, rfl⟩

theorem decision_matching_unique {X R V} (m : DecisionTable X R V) (x : X)
    (r s : R) (hr : r ∈ tableMatches m x) (hs : s ∈ tableMatches m x) : r = s := by
  classical
  simp only [tableMatches, Finset.mem_filter] at hr hs
  exact m.uniqueHit x r hr.1 s hs.1 hr.2 hs.2

/-- A finite target set and finite observations; irrelevant observations are ignored. -/
structure VerdictCoverage (V : Type u) where
  target : Finset V
  observed : Finset V

noncomputable def coveredVerdicts {V} (m : VerdictCoverage V) : Finset V := by
  classical
  exact m.target ∩ m.observed

noncomputable def verdictRatio {V} (m : VerdictCoverage V) : Option ℚ :=
  if m.target.card = 0 then none else some (((coveredVerdicts m).card : ℚ) / m.target.card)

theorem verdict_model_satisfaction {V} (m : VerdictCoverage V) :
    (coveredVerdicts m) ⊆ m.target ∧ (coveredVerdicts m) ⊆ m.observed := by
  classical
  exact ⟨Finset.inter_subset_left, Finset.inter_subset_right⟩

theorem verdict_count_bound {V} (m : VerdictCoverage V) :
    (coveredVerdicts m).card ≤ m.target.card :=
  Finset.card_le_card (verdict_model_satisfaction m).1

theorem verdict_empty_target {V} (observed : Finset V) :
    verdictRatio ⟨∅, observed⟩ = none := by simp [verdictRatio]

theorem verdict_not_rule_coverage :
    (tableExercised booleanTable {false}).image booleanTable.verdict =
      (tableFeasible booleanTable).image booleanTable.verdict ∧
    tableExercised booleanTable {false} ≠ tableFeasible booleanTable := by
  simp [tableExercised, tableFeasible, booleanTable, Finset.filter_insert, Finset.filter_singleton]
  decide

end Catalog
