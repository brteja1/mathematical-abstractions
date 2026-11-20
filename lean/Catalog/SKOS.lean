module

public import Mathlib.Order.RelClasses

@[expose] public section

namespace Catalog
universe u

/-- Selected SKOS semantic-relation interface. D denotes interpreted resources,
not RDF names. This partial binding omits labels, schemes, collections, mappings
other than exactMatch, RDF interpretation and OWL Full metamodel semantics.
Law fields specify admissible structures; they are not satisfaction witnesses. -/
structure SKOS (D : Type u) [Nonempty D] where
  concept : D → Prop
  broader : D → D → Prop
  narrower : D → D → Prop
  broaderTransitive : D → D → Prop
  related : D → D → Prop
  exactMatch : D → D → Prop
  broaderTyping : ∀ x y, broader x y → concept x ∧ concept y
  transitiveTyping : ∀ x y, broaderTransitive x y → concept x ∧ concept y
  relatedTyping : ∀ x y, related x y → concept x ∧ concept y
  exactTyping : ∀ x y, exactMatch x y → concept x ∧ concept y
  inverseHierarchy : ∀ x y, narrower x y ↔ broader y x
  hierarchyInclusion : ∀ x y, broader x y → broaderTransitive x y
  hierarchyTransitivity : ∀ x y z,
    broaderTransitive x y → broaderTransitive y z → broaderTransitive x z
  relatedSymmetry : ∀ x y, related x y → related y x
  hierarchyDisjointness : ∀ x y, related x y → ¬ broaderTransitive x y
  exactSymmetry : ∀ x y, exactMatch x y → exactMatch y x
  exactTransitivity : ∀ x y z, exactMatch x y → exactMatch y z → exactMatch x z

end Catalog
