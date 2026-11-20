module

public import Catalog.Probability
public import Mathlib.Probability.Process.Adapted
public import Mathlib.Probability.Process.Stopping
public import Mathlib.Probability.Martingale.Basic

@[expose] public section

namespace Catalog
open MeasureTheory

structure StochasticProcess (T E : Type*) {Ω : Type*}
    [_root_.MeasurableSpace Ω] [_root_.MeasurableSpace E] (_P : ProbabilitySpace Ω) where
  value : T → Ω → E
  measurable : ∀ t, Measurable (value t)

abbrev Filtration (T : Type*) [Preorder T] {Ω : Type*}
    (m : _root_.MeasurableSpace Ω) := MeasureTheory.Filtration T m

abbrev AdaptedProcess (T E : Type*) [Preorder T] {Ω : Type*}
    [m : _root_.MeasurableSpace Ω] [_root_.MeasurableSpace E]
    (P : ProbabilitySpace Ω) (f : Filtration T m) :=
  {X : StochasticProcess T E P // MeasureTheory.Adapted f X.value}

abbrev StoppingTime {Ω : Type*} [m : _root_.MeasurableSpace Ω]
    (f : Filtration ℕ m) :=
  {τ : Ω → WithTop ℕ // MeasureTheory.IsStoppingTime f τ}

abbrev Martingale {Ω : Type*} [m : _root_.MeasurableSpace Ω]
    (P : ProbabilitySpace Ω) (f : Filtration ℕ m) :=
  {X : StochasticProcess ℕ ℝ P // MeasureTheory.Martingale X.value f P.val}

theorem stochasticProcess_model_satisfaction (T E : Type*) {Ω : Type*}
    [_root_.MeasurableSpace Ω] [_root_.MeasurableSpace E]
    (P : ProbabilitySpace Ω) (e : E) : Nonempty (StochasticProcess T E P) :=
  ⟨⟨fun _ _ => e, fun _ => measurable_const⟩⟩

theorem filtration_model_satisfaction (T : Type*) [Preorder T] {Ω : Type*}
    (m : _root_.MeasurableSpace Ω) : Nonempty (Filtration T m) :=
  ⟨MeasureTheory.Filtration.const T m le_rfl⟩

theorem adaptedProcess_model_satisfaction (T E : Type*) [Preorder T] {Ω : Type*}
    [m : _root_.MeasurableSpace Ω] [_root_.MeasurableSpace E]
    (P : ProbabilitySpace Ω) (f : Filtration T m) (e : E) :
    Nonempty (AdaptedProcess T E P f) :=
  ⟨⟨⟨fun _ _ => e, fun _ => measurable_const⟩, MeasureTheory.adapted_const f e⟩⟩

theorem stoppingTime_model_satisfaction {Ω : Type*} [m : _root_.MeasurableSpace Ω]
    (f : Filtration ℕ m) : Nonempty (StoppingTime f) :=
  ⟨⟨fun _ => (0 : ℕ), MeasureTheory.isStoppingTime_const f 0⟩⟩

theorem martingale_model_satisfaction {Ω : Type*} [m : _root_.MeasurableSpace Ω]
    (P : ProbabilitySpace Ω) (f : Filtration ℕ m) (c : ℝ) :
    Nonempty (Martingale P f) := by
  let : IsProbabilityMeasure P.val := P.prop
  exact ⟨⟨⟨fun _ _ => c, fun _ => measurable_const⟩,
    MeasureTheory.martingale_const f P.val c⟩⟩

end Catalog
