# Tensor of specified valence on a finite-dimensional vector space

An element of a mixed tensor power of a finite-dimensional vector space V and its dual, with contravariant and covariant valences specified.

**Notation:** T∈T^p_q(V)=V^{⊗p}⊗(V*)^{⊗q}; p,q∈ℕ; V*=Hom_F(V,F)

**Stable ID:** `urn:csabs:concept/Tensor`

**Categories:** Linear and multilinear algebra, Geometry and manifolds

**Kind:** Mathematical structure

**Prerequisites:** [Tensor product of vector spaces](TensorProduct.md), [Linear map](LinearMap.md), [Vector space over a field](VectorSpace.md)

**Specializes:** [Vector space over a field](VectorSpace.md)

**Related concepts:** [Finite rectangular matrix over a field](Matrix.md), [Smooth manifold (C∞, without boundary)](SmoothManifold.md)

## Backlinks

- [Finite rectangular matrix over a field](Matrix.md) — `relatedConcept`
- [Smooth manifold (C∞, without boundary)](SmoothManifold.md) — `relatedConcept`
- [Tensor product of vector spaces](TensorProduct.md) — `relatedConcept`

## Interface and scope

**axiomBasis:** Use iterated TensorProduct with p copies of V and q copies of its dual, in that order; the empty tensor power is F.

**basisKind:** defined-structure

**basisScope:** Algebraic finite-dimensional mixed tensors and basis coordinates. Tensor fields, metric index raising and completed tensor products are outside scope.

**basisInstantiation:** Form the ordered iterated TensorProduct of the specified V and V*=Hom_F(V,F) factors, retaining the common field and vector-space interfaces. Use F for zero factors.

**specializationNote:** For fixed F,V,p,q, retain the vector space T^p_q(V); its elements are tensors of that valence.

**verificationObligation:** Equality is equality in the tensor space, independent of basis; a multidimensional array is a coordinate representation only after bases and slot conventions are fixed.; Order p+q differs from tensor decomposition rank. Use F=ℝ or ℂ for the geometric interpretation; the algebraic definition permits any commutative field.; p=q=0 gives scalar tensors. For dim(V)=0 and positive order the tensor space is the zero space. No identification of V with V* is assumed.; Use the stated carriers and equality. Specialization does not automatically transfer operations or claims.

**reviewStatus:** editorial interface review; not machine-proved

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-Tensor-add"></a>

### add

`urn:csabs:operation/Tensor-add`

**signature:** T^p_q(V)×T^p_q(V) → T^p_q(V)

**description:** Add tensors with the same field, vector space and valence.

**precondition:** Inputs belong to the stated domains.

**postcondition:** Add tensors with the same field, vector space and valence.

**totality:** total on the stated domain

<a id="node-urn-csabs-operation-Tensor-scale"></a>

### scale

`urn:csabs:operation/Tensor-scale`

**signature:** F×T^p_q(V) → T^p_q(V)

**description:** Scale a tensor in its tensor vector space.

**precondition:** Inputs belong to the stated domains.

**postcondition:** Scale a tensor in its tensor vector space.

**totality:** total on the stated domain

<a id="node-urn-csabs-operation-Tensor-components"></a>

### components

`urn:csabs:operation/Tensor-components`

**signature:** T^p_q(V) → F^{[d]^p×[d]^q}; T ↦ (T^{i₁…iₚ}_{j₁…j_q})

**description:** Expand in the tensor basis from an ordered basis of V and its dual.

**precondition:** V is finite-dimensional with a chosen ordered basis e₁,…,e_d and its dual basis.

**postcondition:** Expand in the tensor basis from an ordered basis of V and its dual.

**totality:** total on the stated domain

## Axioms and defining rules

<a id="node-urn-csabs-axiom-Tensor-mixed-power-definition"></a>

### mixed-power-definition

`urn:csabs:axiom/Tensor-mixed-power-definition`

**statement:** Mixed tensor spaces use ordered primal and dual factors, with scalar empty power.

**formalStatement:** T^p_q(V)=V^{⊗p}⊗(Hom_F(V,F))^{⊗q}; T^0_0(V)=F

**assumptions:** T∈T^p_q(V)=V^{⊗p}⊗(V*)^{⊗q}; p,q∈ℕ; V*=Hom_F(V,F); Use the concept’s declared semantic conventions.

**reviewStatus:** editorial definition; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Sheldon Axler, Linear Algebra Done Right, fourth edition (consulted revision dated 30 October 2026)](https://linear.axler.net/LADR4e.pdf); accessedOn: 2026-11-07; sourceRole: primary mathematical reference; license: CC BY-NC 4.0; licenseUrl: https://creativecommons.org/licenses/by-nc/4.0/; [Mathlib: tensor product universal property](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/TensorProduct/Basic.html); accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** §3F; §9D, Definition 9.88; empty-power convention stated explicitly; Mathlib TensorProduct.lift and ext for the algebraic universal property over a commutative field

**sourceNote:** Defining constraint or equation adapted to the declared carriers and catalog notation.

**provenanceKind:** adapted

**ruleRole:** definition

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-Tensor-basis-expansion"></a>

### basis-expansion

`urn:csabs:theorem/Tensor-basis-expansion`

**statement:** A chosen basis and dual basis give a unique tensor-coordinate expansion.

**formalStatement:** T=∑_{I∈[d]^p,J∈[d]^q}T^I_J e_{i₁}⊗⋯⊗e_{iₚ}⊗e^{j₁}⊗⋯⊗e^{j_q}, uniquely; empty basis tensor=1_F

**assumptions:** F is a commutative field; V is finite-dimensional with an ordered basis e₁,…,e_d and its dual basis; p,q∈ℕ.; The tensor slot order and empty-power conventions are those of Tensor.

**reviewStatus:** editorial derivation; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Sheldon Axler, Linear Algebra Done Right, fourth edition (consulted revision dated 30 October 2026)](https://linear.axler.net/LADR4e.pdf); accessedOn: 2026-11-07; sourceRole: primary mathematical reference; license: CC BY-NC 4.0; licenseUrl: https://creativecommons.org/licenses/by-nc/4.0/; [Mathlib: tensor product universal property](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/TensorProduct/Basic.html); accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** §9D, result 9.90, applied to V and V*; §3F dual basis; Mathlib TensorProduct.lift and ext for the algebraic universal property over a commutative field

**sourceNote:** Mixed-factor specialization of the tensor-basis theorem, derived from the local universal property with bases explicitly fixed. The empty-power convention is stated separately.

**provenanceKind:** derived

**dependsOn:** [mixed-power-definition](Tensor.md#node-urn-csabs-axiom-Tensor-mixed-power-definition); [universal-property](TensorProduct.md#node-urn-csabs-axiom-TensorProduct-universal-property); [pure-extensionality](TensorProduct.md#node-urn-csabs-theorem-TensorProduct-pure-extensionality)

**proofSketch:** Fix ordered bases for V and V*, using the dual basis for the latter. Iterating the universal property identifies the tensor product with the finite coordinate space indexed by choices of one basis element per factor: coordinate multiplication on pure tensors induces the forward linear map, and linear combination of the corresponding pure basis tensors defines the reverse map. They are inverse on coordinate basis elements and on pure tensors; uniqueness of linear extension gives inverse maps everywhere. The empty product is F with basis 1, and an empty positive-order index set gives the zero space.

<a id="node-urn-csabs-theorem-Tensor-component-extensionality"></a>

### component-extensionality

`urn:csabs:theorem/Tensor-component-extensionality`

**statement:** In a fixed tensor basis, equality is equivalent to equality of all components.

**formalStatement:** S,T∈T^p_q(V):S=T ⇔ ∀I∈[d]^p,J∈[d]^q:S^I_J=T^I_J

**assumptions:** F is a commutative field; V is finite-dimensional with an ordered basis e₁,…,e_d and its dual basis; p,q∈ℕ.; The tensor slot order and empty-power conventions are those of Tensor.

**reviewStatus:** editorial derivation; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Sheldon Axler, Linear Algebra Done Right, fourth edition (consulted revision dated 30 October 2026)](https://linear.axler.net/LADR4e.pdf); accessedOn: 2026-11-07; sourceRole: primary mathematical reference; license: CC BY-NC 4.0; licenseUrl: https://creativecommons.org/licenses/by-nc/4.0/; [Mathlib: tensor product universal property](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/TensorProduct/Basic.html); accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** §9D, result 9.90 (derived uniqueness consequence); Mathlib TensorProduct.lift and ext for the algebraic universal property over a commutative field

**sourceNote:** Derived from the linked local premises; proof sketch gives the adaptation.

**provenanceKind:** derived

**dependsOn:** [mixed-power-definition](Tensor.md#node-urn-csabs-axiom-Tensor-mixed-power-definition); [basis-expansion](Tensor.md#node-urn-csabs-theorem-Tensor-basis-expansion); [components](Tensor.md#node-urn-csabs-operation-Tensor-components)

**proofSketch:** Equal tensors have the same unique expansion. Conversely, identical coefficients give identical finite sums. For order zero the sole coefficient is the scalar; for d=0 and positive order the empty sum is the unique zero tensor.

## Concept provenance

- [Sheldon Axler, Linear Algebra Done Right, fourth edition (consulted revision dated 30 October 2026)](https://linear.axler.net/LADR4e.pdf); accessedOn: 2026-11-07; sourceRole: primary mathematical reference; license: CC BY-NC 4.0; licenseUrl: https://creativecommons.org/licenses/by-nc/4.0/
- [Mathlib: tensor product universal property](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/TensorProduct/Basic.html); accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** §3F Duality; §9D, tensor products of multiple spaces, Definitions 9.85 and 9.88, results 9.89–9.90 (mixed dual-factor adaptation); Mathlib TensorProduct.lift and ext for the algebraic universal property over a commutative field

**sourceNote:** Interface adapted to the catalog notation and explicitly restricted to the stated scope.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/Tensor",
    "type": "Concept",
    "shortForm": "Tensor",
    "fullName": "Tensor of specified valence on a finite-dimensional vector space",
    "category": [
      "urn:csabs:category/linear-algebra",
      "urn:csabs:category/geometry"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "An element of a mixed tensor power of a finite-dimensional vector space V and its dual, with contravariant and covariant valences specified.",
    "notation": "T∈T^p_q(V)=V^{⊗p}⊗(V*)^{⊗q}; p,q∈ℕ; V*=Hom_F(V,F)",
    "hasOperation": [
      "urn:csabs:operation/Tensor-add",
      "urn:csabs:operation/Tensor-scale",
      "urn:csabs:operation/Tensor-components"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/Tensor-mixed-power-definition"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/Tensor-basis-expansion",
      "urn:csabs:theorem/Tensor-component-extensionality"
    ],
    "axiomBasis": "Use iterated TensorProduct with p copies of V and q copies of its dual, in that order; the empty tensor power is F.",
    "basisKind": "defined-structure",
    "basisScope": "Algebraic finite-dimensional mixed tensors and basis coordinates. Tensor fields, metric index raising and completed tensor products are outside scope.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "editorial interface review; not machine-proved",
    "requiresConcept": [
      "urn:csabs:concept/TensorProduct",
      "urn:csabs:concept/LinearMap",
      "urn:csabs:concept/VectorSpace"
    ],
    "verificationObligation": [
      "Equality is equality in the tensor space, independent of basis; a multidimensional array is a coordinate representation only after bases and slot conventions are fixed.",
      "Order p+q differs from tensor decomposition rank. Use F=ℝ or ℂ for the geometric interpretation; the algebraic definition permits any commutative field.",
      "p=q=0 gives scalar tensors. For dim(V)=0 and positive order the tensor space is the zero space. No identification of V with V* is assumed.",
      "Use the stated carriers and equality. Specialization does not automatically transfer operations or claims."
    ],
    "source": [
      "urn:csabs:source/axler-ladr4",
      "urn:csabs:source/mathlib-tensor-universal"
    ],
    "sourceLocator": "§3F Duality; §9D, tensor products of multiple spaces, Definitions 9.85 and 9.88, results 9.89–9.90 (mixed dual-factor adaptation); Mathlib TensorProduct.lift and ext for the algebraic universal property over a commutative field",
    "sourceNote": "Interface adapted to the catalog notation and explicitly restricted to the stated scope.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/VectorSpace"
    ],
    "specializationNote": "For fixed F,V,p,q, retain the vector space T^p_q(V); its elements are tensors of that valence.",
    "relatedConcept": [
      "urn:csabs:concept/Matrix",
      "urn:csabs:concept/SmoothManifold"
    ],
    "basisInstantiation": "Form the ordered iterated TensorProduct of the specified V and V*=Hom_F(V,F) factors, retaining the common field and vector-space interfaces. Use F for zero factors."
  },
  {
    "id": "urn:csabs:operation/Tensor-add",
    "type": "Operation",
    "name": "add",
    "signature": "T^p_q(V)×T^p_q(V) → T^p_q(V)",
    "description": "Add tensors with the same field, vector space and valence.",
    "concept": "urn:csabs:concept/Tensor",
    "precondition": "Inputs belong to the stated domains.",
    "postcondition": "Add tensors with the same field, vector space and valence.",
    "totality": "total on the stated domain"
  },
  {
    "id": "urn:csabs:operation/Tensor-scale",
    "type": "Operation",
    "name": "scale",
    "signature": "F×T^p_q(V) → T^p_q(V)",
    "description": "Scale a tensor in its tensor vector space.",
    "concept": "urn:csabs:concept/Tensor",
    "precondition": "Inputs belong to the stated domains.",
    "postcondition": "Scale a tensor in its tensor vector space.",
    "totality": "total on the stated domain"
  },
  {
    "id": "urn:csabs:operation/Tensor-components",
    "type": "Operation",
    "name": "components",
    "signature": "T^p_q(V) → F^{[d]^p×[d]^q}; T ↦ (T^{i₁…iₚ}_{j₁…j_q})",
    "description": "Expand in the tensor basis from an ordered basis of V and its dual.",
    "concept": "urn:csabs:concept/Tensor",
    "precondition": "V is finite-dimensional with a chosen ordered basis e₁,…,e_d and its dual basis.",
    "postcondition": "Expand in the tensor basis from an ordered basis of V and its dual.",
    "totality": "total on the stated domain"
  },
  {
    "id": "urn:csabs:axiom/Tensor-mixed-power-definition",
    "type": "Axiom",
    "name": "mixed-power-definition",
    "statement": "Mixed tensor spaces use ordered primal and dual factors, with scalar empty power.",
    "formalStatement": "T^p_q(V)=V^{⊗p}⊗(Hom_F(V,F))^{⊗q}; T^0_0(V)=F",
    "appliesTo": [
      "urn:csabs:concept/Tensor"
    ],
    "assumptions": [
      "T∈T^p_q(V)=V^{⊗p}⊗(V*)^{⊗q}; p,q∈ℕ; V*=Hom_F(V,F)",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial definition; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/axler-ladr4",
      "urn:csabs:source/mathlib-tensor-universal"
    ],
    "sourceLocator": "§3F; §9D, Definition 9.88; empty-power convention stated explicitly; Mathlib TensorProduct.lift and ext for the algebraic universal property over a commutative field",
    "sourceNote": "Defining constraint or equation adapted to the declared carriers and catalog notation.",
    "provenanceKind": "adapted",
    "ruleRole": "definition"
  },
  {
    "id": "urn:csabs:theorem/Tensor-basis-expansion",
    "type": "Theorem",
    "name": "basis-expansion",
    "statement": "A chosen basis and dual basis give a unique tensor-coordinate expansion.",
    "formalStatement": "T=∑_{I∈[d]^p,J∈[d]^q}T^I_J e_{i₁}⊗⋯⊗e_{iₚ}⊗e^{j₁}⊗⋯⊗e^{j_q}, uniquely; empty basis tensor=1_F",
    "appliesTo": [
      "urn:csabs:concept/Tensor"
    ],
    "assumptions": [
      "F is a commutative field; V is finite-dimensional with an ordered basis e₁,…,e_d and its dual basis; p,q∈ℕ.",
      "The tensor slot order and empty-power conventions are those of Tensor."
    ],
    "reviewStatus": "editorial derivation; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/axler-ladr4",
      "urn:csabs:source/mathlib-tensor-universal"
    ],
    "sourceLocator": "§9D, result 9.90, applied to V and V*; §3F dual basis; Mathlib TensorProduct.lift and ext for the algebraic universal property over a commutative field",
    "sourceNote": "Mixed-factor specialization of the tensor-basis theorem, derived from the local universal property with bases explicitly fixed. The empty-power convention is stated separately.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/Tensor-mixed-power-definition",
      "urn:csabs:axiom/TensorProduct-universal-property",
      "urn:csabs:theorem/TensorProduct-pure-extensionality"
    ],
    "proofSketch": "Fix ordered bases for V and V*, using the dual basis for the latter. Iterating the universal property identifies the tensor product with the finite coordinate space indexed by choices of one basis element per factor: coordinate multiplication on pure tensors induces the forward linear map, and linear combination of the corresponding pure basis tensors defines the reverse map. They are inverse on coordinate basis elements and on pure tensors; uniqueness of linear extension gives inverse maps everywhere. The empty product is F with basis 1, and an empty positive-order index set gives the zero space."
  },
  {
    "id": "urn:csabs:theorem/Tensor-component-extensionality",
    "type": "Theorem",
    "name": "component-extensionality",
    "statement": "In a fixed tensor basis, equality is equivalent to equality of all components.",
    "formalStatement": "S,T∈T^p_q(V):S=T ⇔ ∀I∈[d]^p,J∈[d]^q:S^I_J=T^I_J",
    "appliesTo": [
      "urn:csabs:concept/Tensor"
    ],
    "assumptions": [
      "F is a commutative field; V is finite-dimensional with an ordered basis e₁,…,e_d and its dual basis; p,q∈ℕ.",
      "The tensor slot order and empty-power conventions are those of Tensor."
    ],
    "reviewStatus": "editorial derivation; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/axler-ladr4",
      "urn:csabs:source/mathlib-tensor-universal"
    ],
    "sourceLocator": "§9D, result 9.90 (derived uniqueness consequence); Mathlib TensorProduct.lift and ext for the algebraic universal property over a commutative field",
    "sourceNote": "Derived from the linked local premises; proof sketch gives the adaptation.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/Tensor-mixed-power-definition",
      "urn:csabs:theorem/Tensor-basis-expansion",
      "urn:csabs:operation/Tensor-components"
    ],
    "proofSketch": "Equal tensors have the same unique expansion. Conversely, identical coefficients give identical finite sums. For order zero the sole coefficient is the scalar; for d=0 and positive order the empty sum is the unique zero tensor."
  }
]
```
<!-- graph-record:end -->
