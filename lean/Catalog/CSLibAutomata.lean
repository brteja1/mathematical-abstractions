module

public import Catalog.Languages
public import Cslib.Computability.Automata.NA.ToDA

@[expose] public section

namespace Catalog.CSLib
universe u v
variable {A : Type u} {Q : Type v} [Fintype A] [Fintype Q]

/-- Preserve the catalog's finite, singleton-start, epsilon-free interpretation. -/
def toNA (m : Catalog.NFA A Q) : Cslib.Automata.NA.FinAcc Q A where
  Tr := m.step
  start := m.start
  accept := m.accept

theorem path_iff (m : Catalog.NFA A Q) (s t : Q) (word : List A) :
    Nonempty (m.toNFA.Path s t word) ↔ (toNA m).MTr s word t := by
  constructor
  · rintro ⟨h⟩
    induction h with
    | nil => exact .refl
    | cons _ _ _ _ _ h _ ih => exact .stepL h ih
  · intro h
    induction h with
    | refl => exact ⟨.nil _⟩
    | stepL h _ ih =>
      obtain ⟨p⟩ := ih
      exact ⟨.cons _ _ _ _ _ h p⟩

theorem nfa_language_eq (m : Catalog.NFA A Q) :
    Cslib.Automata.Acceptor.language (toNA m) = m.toNFA.accepts := by
  ext word
  rw [_root_.NFA.accepts_iff_exists_path]
  change (∃ s ∈ m.start, ∃ t ∈ m.accept, (toNA m).MTr s word t) ↔ _
  simp only [path_iff]

/-- View a deterministic CSLib finite-word acceptor as the catalog's DFA. -/
def fromDA {R : Type v} [Fintype R] (d : Cslib.Automata.DA.FinAcc R A) :
    Catalog.DFA A R where
  step := d.tr
  start := d.start
  accept := d.accept

theorem dfa_language_eq {R : Type v} [Fintype R]
    (d : Cslib.Automata.DA.FinAcc R A) :
    (fromDA d).accepts = Cslib.Automata.Acceptor.language d := rfl

/-- The powerset includes the empty subset, providing a total rejecting sink. -/
noncomputable def subsetDFA (m : Catalog.NFA A Q) : Catalog.DFA A (Set Q) := by
  classical
  exact fromDA (toNA m).toDAFinAcc

theorem subsetDFA_language (m : Catalog.NFA A Q) :
    (subsetDFA m).accepts = m.toNFA.accepts := by
  classical
  exact (dfa_language_eq (toNA m).toDAFinAcc).trans
    (Cslib.Automata.NA.FinAcc.toDAFinAcc_language_eq.trans (nfa_language_eq m))

theorem subset_construction (m : Catalog.NFA A Q) :
    ∃ d : Catalog.DFA A (Set Q), d.accepts = m.toNFA.accepts := by
  classical
  exact ⟨subsetDFA m, subsetDFA_language m⟩

end Catalog.CSLib
