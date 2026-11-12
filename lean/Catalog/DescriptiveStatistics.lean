module

public import Catalog.DataStructures
public import Mathlib.Basic.Real.Basic
public import Mathlib.Algebra.BigOperators.Group.Multiset.Basic
public import Mathlib.Data.Multiset.Sort
public import Mathlib.Data.Finset.Max
public import Mathlib.Tactic.FieldSimp
public import Lean.Elab.Tactic.Omega

@[expose] public section

noncomputable section
namespace Catalog
universe u

/-- Exact, unweighted sample arithmetic mean; empty data are undefined. -/
def ArithmeticMean (sample : _root_.Multiset ℝ) : Option ℝ :=
  if sample.card = 0 then none else some (sample.sum / (sample.card : ℝ))

/-- The two central order statistics, with equal indices for an odd sample. -/
def medianCenters (sample : _root_.Multiset ℝ) : Option (ℝ × ℝ) :=
  if h : sample.card = 0 then none else
    let ordered := sample.sort (· ≤ ·)
    let lo : Fin ordered.length := ⟨(sample.card - 1) / 2, by
      have : ordered.length = sample.card := _root_.Multiset.length_sort (· ≤ ·)
      omega⟩
    let hi : Fin ordered.length := ⟨sample.card / 2, by
      have : ordered.length = sample.card := _root_.Multiset.length_sort (· ≤ ·)
      omega⟩
    some (ordered.get lo, ordered.get hi)

/-- Conventional real sample median: midpoint in the even case. -/
def Median (sample : _root_.Multiset ℝ) : Option ℝ :=
  (medianCenters sample).map fun p => (p.1 + p.2) / 2

/-- Observed frequency maximizers. All ties are retained, including all-unique data. -/
def Mode {A : Type u} [DecidableEq A] (sample : _root_.Multiset A) : Finset A := by
  classical
  exact sample.toFinset.filter (fun a => ∀ b ∈ sample, sample.count b ≤ sample.count a)

namespace DescriptiveStatisticsProofs

theorem mean_singleton (x : ℝ) : ArithmeticMean {x} = some x := by
  simp [ArithmeticMean]

theorem mean_balance (sample : _root_.Multiset ℝ) (m : ℝ)
    (h : ArithmeticMean sample = some m) : (sample.card : ℝ) * m = sample.sum := by
  by_cases hc : sample.card = 0
  · simp [ArithmeticMean, hc] at h
  · have hm : sample.sum / (sample.card : ℝ) = m := Option.some.inj (by simpa [ArithmeticMean, hc] using h)
    have hn : (sample.card : ℝ) ≠ 0 := Nat.cast_ne_zero.mpr hc
    rw [← hm]
    field_simp [hn]

theorem median_singleton (x : ℝ) : Median {x} = some x := by
  simp [Median, medianCenters]

theorem median_pair (a b : ℝ) : Median ({a, b} : _root_.Multiset ℝ) = some ((a + b) / 2) := by
  have ordered_pair (x y : ℝ) (hxy : x ≤ y) : Median ({x, y} : _root_.Multiset ℝ) = some ((x + y) / 2) := by
    have hs : (x ::ₘ ({y} : _root_.Multiset ℝ)).sort (· ≤ ·) = [x, y] := by
      simpa only [_root_.Multiset.sort_singleton] using
        (_root_.Multiset.sort_cons x ({y} : _root_.Multiset ℝ) (· ≤ ·) (by simpa using hxy))
    simp [Median, medianCenters, hs]
  by_cases h : a ≤ b
  · exact ordered_pair a b h
  · simpa only [_root_.Multiset.pair_comm b a, add_comm b a] using ordered_pair b a (le_of_not_ge h)

theorem mode_singleton {A : Type u} [DecidableEq A] (x : A) : Mode {x} = {x} := by
  classical
  simp [Mode]

theorem mode_nonempty {A : Type u} [DecidableEq A] (sample : _root_.Multiset A)
    (h : sample ≠ 0) : (Mode sample).Nonempty := by
  classical
  obtain ⟨a, ha, hmax⟩ := sample.exists_max_image (fun x => sample.count x) h
  exact ⟨a, Finset.mem_filter.mpr ⟨_root_.Multiset.mem_toFinset.mpr ha, hmax⟩⟩

end DescriptiveStatisticsProofs
end Catalog
