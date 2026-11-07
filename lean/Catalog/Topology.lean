module

public import Mathlib.Geometry.Manifold.Instances.Real
public import Mathlib.Geometry.Manifold.IsManifold.Basic

@[expose] public section

namespace Catalog
open scoped Manifold

abbrev TopologicalSpace (M : Type*) := _root_.TopologicalSpace M

/-- Boundaryless real charts, with separation and countability explicit.
The atlas is supplied by the ChartedSpace parameter and covers the carrier. -/
structure Manifold (n : Nat) (M : Type*) [_root_.TopologicalSpace M]
    [ChartedSpace (EuclideanSpace ℝ (Fin n)) M] : Prop where
  hausdorff : T2Space M
  secondCountable : SecondCountableTopology M

/-- Compatibility of the supplied covering atlas; its maximal compatible
extension is not separately constructed by this wrapper. -/
structure SmoothManifold (n : Nat) (M : Type*) [_root_.TopologicalSpace M]
    [ChartedSpace (EuclideanSpace ℝ (Fin n)) M] : Prop extends Manifold n M where
  compatible : IsManifold (𝓡 n) ((⊤ : ENat) : WithTop ENat) M

end Catalog
