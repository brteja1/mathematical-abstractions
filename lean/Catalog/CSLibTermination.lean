module

public import Catalog.Semantics
public import Cslib.Foundations.Relation.Termination

@[expose] public section

namespace Catalog.CSLib
universe u v
variable {S : Type u} {W : Type v} {C : Command S} {r : W → W → Prop}

/-- The forward relation records completed continuing iterations. -/
theorem variant_terminating (variant : TerminationVariant C r) :
    Relation.Terminating C := by
  exact (InvImage.wf variant.measure variant.wellFounded).mono
    (fun _ _ h => variant.decreasing _ _ h)

/-- No infinite sequence of completed iterations; body termination is separate. -/
theorem variant_no_infinite_chain (variant : TerminationVariant C r) :
    ¬ ∃ states : ℕ → S, ∀ n, C (states n) (states (n + 1)) := by
  intro ⟨states, steps⟩
  have empty := Relation.Terminating.iff_isEmpty_chain.mp (variant_terminating variant)
  exact empty.false ⟨states, steps⟩

end Catalog.CSLib
