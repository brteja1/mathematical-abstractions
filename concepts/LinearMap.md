# Linear map

A total function between vector spaces over the same field that preserves vector addition and scalar multiplication.

**Notation:** T:V→W; T(u+v)=T(u)+T(v); T(av)=aT(v)

**Stable ID:** `urn:csabs:concept/LinearMap`

**Categories:** Linear and multilinear algebra

**Kind:** Function

**Prerequisites:** [Vector space over a field](VectorSpace.md), [Total function](Function.md)

**Specializes:** [Total function](Function.md)

**Related concepts:** [Finite rectangular matrix over a field](Matrix.md)

## Backlinks

- [Finite rectangular matrix over a field](Matrix.md) — `relatedConcept`
- [Tensor of specified valence on a finite-dimensional vector space](Tensor.md) — `requiresConcept`
- [Tensor product of vector spaces](TensorProduct.md) — `requiresConcept`

## Interface and scope

**axiomBasis:** Additivity and homogeneity over the same specified scalar field.

**basisKind:** defined-structure

**basisScope:** Linear maps, composition, kernels and ranges; continuity is not assumed for arbitrary topological vector spaces.

**specializationNote:** Forget the vector-space structures and linearity requirements, retaining the same total function.

**verificationObligation:** Pointwise equality; no bases are required. Domain and codomain may have different dimensions, including zero.; Use the stated carriers and equality. Specialization does not automatically transfer operations or claims.

**reviewStatus:** editorial interface review; not machine-proved

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-LinearMap-apply"></a>

### apply

`urn:csabs:operation/LinearMap-apply`

**signature:** V → W; v ↦ T(v)

**description:** Evaluate the linear map.

**precondition:** Inputs belong to the stated domains.

**postcondition:** Evaluate the linear map.

**totality:** total on the stated domain

<a id="node-urn-csabs-operation-LinearMap-compose"></a>

### compose

`urn:csabs:operation/LinearMap-compose`

**signature:** Hom_F(W,U) × Hom_F(V,W) → Hom_F(V,U)

**description:** Compose linear maps over the same field.

**precondition:** Inputs belong to the stated domains.

**postcondition:** Compose linear maps over the same field.

**totality:** total on the stated domain

<a id="node-urn-csabs-operation-LinearMap-kernel"></a>

### kernel

`urn:csabs:operation/LinearMap-kernel`

**signature:** Hom_F(V,W) → 𝒫(V); T ↦ {v:T(v)=0_W}

**description:** Return the kernel as a subset of V.

**precondition:** Inputs belong to the stated domains.

**postcondition:** Return the kernel as a subset of V.

**totality:** total on the stated domain

<a id="node-urn-csabs-operation-LinearMap-image"></a>

### image

`urn:csabs:operation/LinearMap-image`

**signature:** Hom_F(V,W) → 𝒫(W); T ↦ {T(v):v∈V}

**description:** Return the range as a subset of W.

**precondition:** Inputs belong to the stated domains.

**postcondition:** Return the range as a subset of W.

**totality:** total on the stated domain

## Axioms and defining rules

<a id="node-urn-csabs-axiom-LinearMap-additivity"></a>

### additivity

`urn:csabs:axiom/LinearMap-additivity`

**statement:** Linear maps preserve addition.

**formalStatement:** ∀u,v∈V:T(u+v)=T(u)+T(v)

**assumptions:** T:V→W; T(u+v)=T(u)+T(v); T(av)=aT(v); Use the concept’s declared semantic conventions.

**reviewStatus:** editorial definition; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Sheldon Axler, Linear Algebra Done Right, fourth edition (consulted revision dated 30 October 2026)](https://linear.axler.net/LADR4e.pdf); accessedOn: 2026-11-07; sourceRole: primary mathematical reference; license: CC BY-NC 4.0; licenseUrl: https://creativecommons.org/licenses/by-nc/4.0/

**sourceLocator:** §3A, Definition 3.1

**sourceNote:** Defining constraint or equation adapted to the declared carriers and catalog notation.

**provenanceKind:** adapted

**ruleRole:** structure-law

<a id="node-urn-csabs-axiom-LinearMap-homogeneity"></a>

### homogeneity

`urn:csabs:axiom/LinearMap-homogeneity`

**statement:** Linear maps preserve scalar multiplication.

**formalStatement:** ∀a∈F,v∈V:T(av)=aT(v)

**assumptions:** T:V→W; T(u+v)=T(u)+T(v); T(av)=aT(v); Use the concept’s declared semantic conventions.

**reviewStatus:** editorial definition; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Sheldon Axler, Linear Algebra Done Right, fourth edition (consulted revision dated 30 October 2026)](https://linear.axler.net/LADR4e.pdf); accessedOn: 2026-11-07; sourceRole: primary mathematical reference; license: CC BY-NC 4.0; licenseUrl: https://creativecommons.org/licenses/by-nc/4.0/

**sourceLocator:** §3A, Definition 3.1

**sourceNote:** Defining constraint or equation adapted to the declared carriers and catalog notation.

**provenanceKind:** adapted

**ruleRole:** structure-law

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-LinearMap-zero-preservation"></a>

### zero-preservation

`urn:csabs:theorem/LinearMap-zero-preservation`

**statement:** A linear map sends zero to zero.

**formalStatement:** T(0_V)=0_W

**assumptions:** T:V→W; T(u+v)=T(u)+T(v); T(av)=aT(v); Use the concept’s declared semantic conventions.

**reviewStatus:** editorial derivation; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Sheldon Axler, Linear Algebra Done Right, fourth edition (consulted revision dated 30 October 2026)](https://linear.axler.net/LADR4e.pdf); accessedOn: 2026-11-07; sourceRole: primary mathematical reference; license: CC BY-NC 4.0; licenseUrl: https://creativecommons.org/licenses/by-nc/4.0/

**sourceLocator:** §3A, result 3.10

**sourceNote:** Derived from the linked local premises; proof sketch gives the adaptation.

**provenanceKind:** derived

**dependsOn:** [additivity](LinearMap.md#node-urn-csabs-axiom-LinearMap-additivity); [additive-structure](VectorSpace.md#node-urn-csabs-axiom-VectorSpace-additive-structure); [apply](LinearMap.md#node-urn-csabs-operation-LinearMap-apply)

**proofSketch:** T(0_V)=T(0_V+0_V)=T(0_V)+T(0_V); cancellation in W yields the result.

## Concept provenance

- [Sheldon Axler, Linear Algebra Done Right, fourth edition (consulted revision dated 30 October 2026)](https://linear.axler.net/LADR4e.pdf); accessedOn: 2026-11-07; sourceRole: primary mathematical reference; license: CC BY-NC 4.0; licenseUrl: https://creativecommons.org/licenses/by-nc/4.0/

**sourceLocator:** §3A, Definition 3.1; §3B

**sourceNote:** Interface adapted to the catalog notation and explicitly restricted to the stated scope.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/LinearMap",
    "type": "Concept",
    "shortForm": "LinearMap",
    "fullName": "Linear map",
    "category": [
      "urn:csabs:category/linear-algebra"
    ],
    "kind": "urn:csabs:kind/function",
    "definition": "A total function between vector spaces over the same field that preserves vector addition and scalar multiplication.",
    "notation": "T:V→W; T(u+v)=T(u)+T(v); T(av)=aT(v)",
    "hasOperation": [
      "urn:csabs:operation/LinearMap-apply",
      "urn:csabs:operation/LinearMap-compose",
      "urn:csabs:operation/LinearMap-kernel",
      "urn:csabs:operation/LinearMap-image"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/LinearMap-additivity",
      "urn:csabs:axiom/LinearMap-homogeneity"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/LinearMap-zero-preservation"
    ],
    "axiomBasis": "Additivity and homogeneity over the same specified scalar field.",
    "basisKind": "defined-structure",
    "basisScope": "Linear maps, composition, kernels and ranges; continuity is not assumed for arbitrary topological vector spaces.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "editorial interface review; not machine-proved",
    "requiresConcept": [
      "urn:csabs:concept/VectorSpace",
      "urn:csabs:concept/Function"
    ],
    "verificationObligation": [
      "Pointwise equality; no bases are required. Domain and codomain may have different dimensions, including zero.",
      "Use the stated carriers and equality. Specialization does not automatically transfer operations or claims."
    ],
    "source": [
      "urn:csabs:source/axler-ladr4"
    ],
    "sourceLocator": "§3A, Definition 3.1; §3B",
    "sourceNote": "Interface adapted to the catalog notation and explicitly restricted to the stated scope.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/Function"
    ],
    "specializationNote": "Forget the vector-space structures and linearity requirements, retaining the same total function.",
    "relatedConcept": [
      "urn:csabs:concept/Matrix"
    ]
  },
  {
    "id": "urn:csabs:operation/LinearMap-apply",
    "type": "Operation",
    "name": "apply",
    "signature": "V → W; v ↦ T(v)",
    "description": "Evaluate the linear map.",
    "concept": "urn:csabs:concept/LinearMap",
    "precondition": "Inputs belong to the stated domains.",
    "postcondition": "Evaluate the linear map.",
    "totality": "total on the stated domain"
  },
  {
    "id": "urn:csabs:operation/LinearMap-compose",
    "type": "Operation",
    "name": "compose",
    "signature": "Hom_F(W,U) × Hom_F(V,W) → Hom_F(V,U)",
    "description": "Compose linear maps over the same field.",
    "concept": "urn:csabs:concept/LinearMap",
    "precondition": "Inputs belong to the stated domains.",
    "postcondition": "Compose linear maps over the same field.",
    "totality": "total on the stated domain"
  },
  {
    "id": "urn:csabs:operation/LinearMap-kernel",
    "type": "Operation",
    "name": "kernel",
    "signature": "Hom_F(V,W) → 𝒫(V); T ↦ {v:T(v)=0_W}",
    "description": "Return the kernel as a subset of V.",
    "concept": "urn:csabs:concept/LinearMap",
    "precondition": "Inputs belong to the stated domains.",
    "postcondition": "Return the kernel as a subset of V.",
    "totality": "total on the stated domain"
  },
  {
    "id": "urn:csabs:operation/LinearMap-image",
    "type": "Operation",
    "name": "image",
    "signature": "Hom_F(V,W) → 𝒫(W); T ↦ {T(v):v∈V}",
    "description": "Return the range as a subset of W.",
    "concept": "urn:csabs:concept/LinearMap",
    "precondition": "Inputs belong to the stated domains.",
    "postcondition": "Return the range as a subset of W.",
    "totality": "total on the stated domain"
  },
  {
    "id": "urn:csabs:axiom/LinearMap-additivity",
    "type": "Axiom",
    "name": "additivity",
    "statement": "Linear maps preserve addition.",
    "formalStatement": "∀u,v∈V:T(u+v)=T(u)+T(v)",
    "appliesTo": [
      "urn:csabs:concept/LinearMap"
    ],
    "assumptions": [
      "T:V→W; T(u+v)=T(u)+T(v); T(av)=aT(v)",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial definition; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/axler-ladr4"
    ],
    "sourceLocator": "§3A, Definition 3.1",
    "sourceNote": "Defining constraint or equation adapted to the declared carriers and catalog notation.",
    "provenanceKind": "adapted",
    "ruleRole": "structure-law"
  },
  {
    "id": "urn:csabs:axiom/LinearMap-homogeneity",
    "type": "Axiom",
    "name": "homogeneity",
    "statement": "Linear maps preserve scalar multiplication.",
    "formalStatement": "∀a∈F,v∈V:T(av)=aT(v)",
    "appliesTo": [
      "urn:csabs:concept/LinearMap"
    ],
    "assumptions": [
      "T:V→W; T(u+v)=T(u)+T(v); T(av)=aT(v)",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial definition; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/axler-ladr4"
    ],
    "sourceLocator": "§3A, Definition 3.1",
    "sourceNote": "Defining constraint or equation adapted to the declared carriers and catalog notation.",
    "provenanceKind": "adapted",
    "ruleRole": "structure-law"
  },
  {
    "id": "urn:csabs:theorem/LinearMap-zero-preservation",
    "type": "Theorem",
    "name": "zero-preservation",
    "statement": "A linear map sends zero to zero.",
    "formalStatement": "T(0_V)=0_W",
    "appliesTo": [
      "urn:csabs:concept/LinearMap"
    ],
    "assumptions": [
      "T:V→W; T(u+v)=T(u)+T(v); T(av)=aT(v)",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial derivation; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/axler-ladr4"
    ],
    "sourceLocator": "§3A, result 3.10",
    "sourceNote": "Derived from the linked local premises; proof sketch gives the adaptation.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/LinearMap-additivity",
      "urn:csabs:axiom/VectorSpace-additive-structure",
      "urn:csabs:operation/LinearMap-apply"
    ],
    "proofSketch": "T(0_V)=T(0_V+0_V)=T(0_V)+T(0_V); cancellation in W yields the result."
  }
]
```
<!-- graph-record:end -->
