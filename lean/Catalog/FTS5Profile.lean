module

public import Catalog.RetrievalDecisions
public import Catalog.Audit

@[expose] public section
namespace Catalog
universe u v

/-- Tokenization and phrase occurrence extraction are inputs to this exact-real profile. -/
structure BM25FTS5 (P : Type u) (D : Type v) (columns : Nat) where
  docs : Finset D
  nonempty : docs.Nonempty
  tokens : D → Fin columns → Nat
  positiveLength : ∀ d ∈ docs, 0 < ∑ c, tokens d c
  occurrences : P → D → Fin columns → Nat

def fts5Weight (weights : List ℝ) (c : Nat) : ℝ := (weights[c]?).getD 1

noncomputable def fts5Length {P D n} (m : BM25FTS5 P D n) (d : D) : ℝ :=
  ∑ c, (m.tokens d c : ℝ)

noncomputable def fts5Average {P D n} (m : BM25FTS5 P D n) : ℝ :=
  (∑ d ∈ m.docs, fts5Length m d) / m.docs.card

noncomputable def fts5DF {P D n} (m : BM25FTS5 P D n) (p : P) : Nat := by
  classical
  exact (m.docs.filter (fun d => ∃ c, 0 < m.occurrences p d c)).card

noncomputable def fts5RawIDF {P D n} (m : BM25FTS5 P D n) (p : P) : ℝ :=
  Real.log (((m.docs.card : ℝ) - fts5DF m p + 1/2) / (fts5DF m p + 1/2))

noncomputable def fts5IDF {P D n} (m : BM25FTS5 P D n) (p : P) : ℝ :=
  if fts5RawIDF m p ≤ 0 then 1 / 1000000 else fts5RawIDF m p

noncomputable def fts5Frequency {P D n} (m : BM25FTS5 P D n)
    (weights : List ℝ) (p : P) (d : D) : ℝ :=
  ∑ c : Fin n, fts5Weight weights c.val * m.occurrences p d c

noncomputable def fts5Term {P D n} (m : BM25FTS5 P D n)
    (weights : List ℝ) (p : P) (d : D) : ℝ :=
  let f := fts5Frequency m weights p d
  fts5IDF m p * (f * (6/5 + 1)) /
    (f + 6/5 * (1 - 3/4 + 3/4 * fts5Length m d / fts5Average m))

/-- Query phrases retain multiplicity and order; matching is a separate predicate. -/
noncomputable def fts5SQLScore {P D n} (m : BM25FTS5 P D n)
    (weights : List ℝ) (phrases : List P) (d : D) : ℝ :=
  -(phrases.map (fun p => fts5Term m weights p d)).sum

def phraseAND {D : Type u} {P : Type v} (hit : P → D → Prop) (ps : List P) : Set D :=
  {d | ∀ p ∈ ps, hit p d}

def phraseOR {D : Type u} {P : Type v} (hit : P → D → Prop) (ps : List P) : Set D :=
  {d | ∃ p ∈ ps, hit p d}

theorem fts5_boolean {D : Type u} {P : Type v} (hit : P → D → Prop) (p : P) (ps : List P) (d : D) :
    (d ∈ phraseAND hit (p :: ps) ↔ hit p d ∧ d ∈ phraseAND hit ps) ∧
    (d ∈ phraseOR hit (p :: ps) ↔ hit p d ∨ d ∈ phraseOR hit ps) ∧
    d ∈ phraseAND hit [] ∧ d ∉ phraseOR hit [] := by
  simp [phraseAND, phraseOR]

theorem fts5_default_weights (c : Nat) : fts5Weight [] c = 1 := by
  simp [fts5Weight]

theorem fts5_idf_cases {P D n} (m : BM25FTS5 P D n) (p : P) :
    (fts5RawIDF m p ≤ 0 → fts5IDF m p = 1/1000000) ∧
    (0 < fts5RawIDF m p → fts5IDF m p = fts5RawIDF m p) := by
  constructor
  · intro h; simp [fts5IDF, h]
  · intro h; simp [fts5IDF, not_le.mpr h]

theorem fts5_empty_query {P D n} (m : BM25FTS5 P D n) (weights : List ℝ) (d : D) :
    fts5SQLScore m weights [] d = 0 := by simp [fts5SQLScore]

theorem fts5_score_definition {P D n} (m : BM25FTS5 P D n)
    (weights : List ℝ) (ps : List P) (d : D) :
    fts5SQLScore m weights ps d = - (ps.map (fun p =>
      let f := fts5Frequency m weights p d
      fts5IDF m p * (f * (6/5 + 1)) /
        (f + 6/5 * (1 - 3/4 + 3/4 * fts5Length m d / fts5Average m)))).sum := rfl

theorem fts5_rank_direction (sql₁ sql₂ : ℝ) : -sql₁ ≥ -sql₂ ↔ sql₁ ≤ sql₂ := neg_le_neg_iff

def unitFTS5 : BM25FTS5 Unit Unit 1 where
  docs := {()}
  nonempty := by simp
  tokens := fun _ _ => 1
  positiveLength := by simp
  occurrences := fun _ _ _ => 1

theorem fts5_model_satisfaction :
    unitFTS5.docs.Nonempty ∧
    (∀ d ∈ unitFTS5.docs, 0 < ∑ c, unitFTS5.tokens d c) ∧
    (∀ c, fts5Weight [] c = 1) ∧
    fts5SQLScore unitFTS5 [] [] () = 0 := by
  exact ⟨unitFTS5.nonempty, unitFTS5.positiveLength, fts5_default_weights, fts5_empty_query _ _ _⟩

#catalog_witness fts5_boolean
#catalog_witness fts5_default_weights
#catalog_witness fts5_idf_cases
#catalog_witness fts5_empty_query
#catalog_witness fts5_score_definition
#catalog_witness fts5_rank_direction
#catalog_witness fts5_model_satisfaction
end Catalog
