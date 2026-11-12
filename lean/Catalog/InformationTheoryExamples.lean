module
public import Catalog.InformationTheoryStatements
public import Mathlib.Data.ZMod.Basic

/-! Concrete finite instances; these supplement the general witnesses, not replace them. -/
@[expose] public section
noncomputable section
namespace Catalog.Information.Examples

/-- An inhabited normalized finite-law model: fair binary source. -/
def fairBit : Law Bool where
  mass _ := 1/2
  nonnegative _ := by norm_num
  normalized := by norm_num [Fintype.sum_bool]

example : (∑ b, outputMass fairBit (fun _ => fairBit) b) = 1 :=
  (output_normalized fairBit (fun _ => fairBit)).1

/-- Three differing coordinates have Hamming distance three. -/
example : hamming (![false,false,false] : Fin 3 → Bool) ![true,true,true] = 3 := by
  decide

/-- A concrete nonlinear codebook, over the actual field F₂. -/
def nonlinearThree : Set (Fin 3 → ZMod 2) :=
  {![0,0,0], ![0,1,1], ![1,0,1]}

/-- Nonlinearity follows from a missing sum, via the universal checked theorem. -/
theorem nonlinear_three_not_subspace :
    ¬ ∃ S : Submodule (ZMod 2) (Fin 3 → ZMod 2), (S : Set _) = nonlinearThree := by
  apply (nonlinear_witness nonlinearThree).mpr
  right
  refine ⟨1,1,![0,1,1],?_,![1,0,1],?_,?_⟩
  · simp [nonlinearThree]
  · simp [nonlinearThree]
  · unfold nonlinearThree
    decide

end Catalog.Information.Examples
