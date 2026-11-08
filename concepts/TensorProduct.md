# Tensor product of vector spaces

A vector space V⊗_F W with a bilinear pairing that turns each bilinear map V×W→U uniquely into a linear map V⊗_F W→U.

**Notation:** ⊗:V×W→V⊗_F W; Hom_F(V⊗_F W,U)≅Bilin_F(V,W;U)

**Stable ID:** `urn:csabs:concept/TensorProduct`

**Categories:** Algebra → Linear and multilinear algebra

**Kind:** Mathematical construction

**Prerequisites:** [Vector space over a field](VectorSpace.md), [Linear map](LinearMap.md)

**Specializes:** [Vector space over a field](VectorSpace.md)

**Related concepts:** [Tensor of specified valence on a finite-dimensional vector space](Tensor.md)

## Backlinks

- [Tensor of specified valence on a finite-dimensional vector space](Tensor.md) — `requiresConcept`

## Interface and scope

**axiomBasis:** Bilinearity of the canonical pairing and the unique linear extension property for every bilinear map into any F-vector space.

**basisKind:** defined-structure

**basisScope:** Algebraic tensor product over a commutative field; no completed topological tensor product or claim that every tensor is pure.

**basisInstantiation:** Instantiate VectorSpace over F on V, W, U and the constructed tensor product. The pairing is bilinear; its universal extension maps are LinearMap instances over the same F.

**specializationNote:** Retain the vector space V⊗_F W over F and forget its distinguished universal pairing.

**verificationObligation:** The product is specified up to a unique pairing-preserving linear isomorphism, not literal equality of arbitrary constructions.; Zero-dimensional factors are permitted. In general tensors are finite sums of pure tensors; a general tensor is not a pair.; Use the stated carriers and equality. Specialization does not automatically transfer operations or claims.

**reviewStatus:** editorial interface review; not machine-proved

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-TensorProduct-pure"></a>

### pure

`urn:csabs:operation/TensorProduct-pure`

**signature:** V×W → V⊗_F W; (v,w) ↦ v⊗w

**description:** Construct a pure tensor using the bilinear pairing.

**precondition:** Inputs belong to the stated domains.

**postcondition:** Construct a pure tensor using the bilinear pairing.

**totality:** total on the stated domain

<a id="node-urn-csabs-operation-TensorProduct-lift"></a>

### lift

`urn:csabs:operation/TensorProduct-lift`

**signature:** Bilin_F(V,W;U) → Hom_F(V⊗_F W,U)

**description:** Extend a bilinear map uniquely to a linear map.

**precondition:** b:V×W→U is bilinear and all spaces have the same scalar field F.

**postcondition:** Extend a bilinear map uniquely to a linear map.

**totality:** total on the stated domain

## Axioms and defining rules

<a id="node-urn-csabs-axiom-TensorProduct-pairing-bilinear"></a>

### pairing-bilinear

`urn:csabs:axiom/TensorProduct-pairing-bilinear`

**statement:** The canonical pairing is additive in each argument and balances scalar multiplication.

**formalStatement:** (v₁+v₂)⊗w=v₁⊗w+v₂⊗w; v⊗(w₁+w₂)=v⊗w₁+v⊗w₂; (av)⊗w=a(v⊗w)=v⊗(aw)

**assumptions:** v,v₁,v₂∈V; w,w₁,w₂∈W; a∈F; all vector spaces use the same commutative field F.

**reviewStatus:** editorial definition; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Mathlib: tensor product universal property](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/TensorProduct/Basic.html); accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** TensorProduct pairing and lift (bilinear interface)

**sourceNote:** Defining constraint or equation adapted to the declared carriers and catalog notation.

**provenanceKind:** adapted

**ruleRole:** structure-law

<a id="node-urn-csabs-axiom-TensorProduct-universal-property"></a>

### universal-property

`urn:csabs:axiom/TensorProduct-universal-property`

**statement:** Every bilinear map has exactly one linear extension agreeing on pure tensors.

**formalStatement:** ∀F-vector space U, ∀bilinear b:V×W→U, ∃!linear L:V⊗_F W→U:∀v,w:L(v⊗w)=b(v,w)

**assumptions:** ⊗:V×W→V⊗_F W; Hom_F(V⊗_F W,U)≅Bilin_F(V,W;U); Use the concept’s declared semantic conventions.

**reviewStatus:** editorial definition; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Mathlib: tensor product universal property](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/TensorProduct/Basic.html); accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** TensorProduct.lift; lift.tmul; lift.unique

**sourceNote:** Defining constraint or equation adapted to the declared carriers and catalog notation.

**provenanceKind:** adapted

**ruleRole:** defining-rule

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-TensorProduct-pure-extensionality"></a>

### pure-extensionality

`urn:csabs:theorem/TensorProduct-pure-extensionality`

**statement:** Linear maps out of a tensor product are determined by pure tensors.

**formalStatement:** L₁,L₂:V⊗_F W→U linear and (∀v,w:L₁(v⊗w)=L₂(v⊗w)) ⇒ L₁=L₂

**assumptions:** ⊗:V×W→V⊗_F W; Hom_F(V⊗_F W,U)≅Bilin_F(V,W;U); Use the concept’s declared semantic conventions.

**reviewStatus:** editorial derivation; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Mathlib: tensor product universal property](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/TensorProduct/Basic.html); accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** TensorProduct.ext

**sourceNote:** Derived from the linked local premises; proof sketch gives the adaptation.

**provenanceKind:** derived

**dependsOn:** [pairing-bilinear](TensorProduct.md#node-urn-csabs-axiom-TensorProduct-pairing-bilinear); [universal-property](TensorProduct.md#node-urn-csabs-axiom-TensorProduct-universal-property); [pure](TensorProduct.md#node-urn-csabs-operation-TensorProduct-pure); [lift](TensorProduct.md#node-urn-csabs-operation-TensorProduct-lift)

**proofSketch:** The shared restriction to pure tensors is bilinear. Both maps are linear extensions of it; uniqueness in the universal property gives equality.

## Concept provenance

- [Mathlib: tensor product universal property](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/TensorProduct/Basic.html); accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** TensorProduct.lift; lift.tmul; lift.unique; ext

**sourceNote:** Interface adapted to the catalog notation and explicitly restricted to the stated scope.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/TensorProduct",
    "type": "Concept",
    "shortForm": "TensorProduct",
    "fullName": "Tensor product of vector spaces",
    "category": [
      "urn:csabs:category/linear-algebra"
    ],
    "kind": "urn:csabs:kind/construction",
    "definition": "A vector space V⊗_F W with a bilinear pairing that turns each bilinear map V×W→U uniquely into a linear map V⊗_F W→U.",
    "notation": "⊗:V×W→V⊗_F W; Hom_F(V⊗_F W,U)≅Bilin_F(V,W;U)",
    "hasOperation": [
      "urn:csabs:operation/TensorProduct-pure",
      "urn:csabs:operation/TensorProduct-lift"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/TensorProduct-pairing-bilinear",
      "urn:csabs:axiom/TensorProduct-universal-property"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/TensorProduct-pure-extensionality"
    ],
    "axiomBasis": "Bilinearity of the canonical pairing and the unique linear extension property for every bilinear map into any F-vector space.",
    "basisKind": "defined-structure",
    "basisScope": "Algebraic tensor product over a commutative field; no completed topological tensor product or claim that every tensor is pure.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "editorial interface review; not machine-proved",
    "requiresConcept": [
      "urn:csabs:concept/VectorSpace",
      "urn:csabs:concept/LinearMap"
    ],
    "verificationObligation": [
      "The product is specified up to a unique pairing-preserving linear isomorphism, not literal equality of arbitrary constructions.",
      "Zero-dimensional factors are permitted. In general tensors are finite sums of pure tensors; a general tensor is not a pair.",
      "Use the stated carriers and equality. Specialization does not automatically transfer operations or claims."
    ],
    "source": [
      "urn:csabs:source/mathlib-tensor-universal"
    ],
    "sourceLocator": "TensorProduct.lift; lift.tmul; lift.unique; ext",
    "sourceNote": "Interface adapted to the catalog notation and explicitly restricted to the stated scope.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/VectorSpace"
    ],
    "specializationNote": "Retain the vector space V⊗_F W over F and forget its distinguished universal pairing.",
    "relatedConcept": [
      "urn:csabs:concept/Tensor"
    ],
    "basisInstantiation": "Instantiate VectorSpace over F on V, W, U and the constructed tensor product. The pairing is bilinear; its universal extension maps are LinearMap instances over the same F."
  },
  {
    "id": "urn:csabs:operation/TensorProduct-pure",
    "type": "Operation",
    "name": "pure",
    "signature": "V×W → V⊗_F W; (v,w) ↦ v⊗w",
    "description": "Construct a pure tensor using the bilinear pairing.",
    "concept": "urn:csabs:concept/TensorProduct",
    "precondition": "Inputs belong to the stated domains.",
    "postcondition": "Construct a pure tensor using the bilinear pairing.",
    "totality": "total on the stated domain"
  },
  {
    "id": "urn:csabs:operation/TensorProduct-lift",
    "type": "Operation",
    "name": "lift",
    "signature": "Bilin_F(V,W;U) → Hom_F(V⊗_F W,U)",
    "description": "Extend a bilinear map uniquely to a linear map.",
    "concept": "urn:csabs:concept/TensorProduct",
    "precondition": "b:V×W→U is bilinear and all spaces have the same scalar field F.",
    "postcondition": "Extend a bilinear map uniquely to a linear map.",
    "totality": "total on the stated domain"
  },
  {
    "id": "urn:csabs:axiom/TensorProduct-pairing-bilinear",
    "type": "Axiom",
    "name": "pairing-bilinear",
    "statement": "The canonical pairing is additive in each argument and balances scalar multiplication.",
    "formalStatement": "(v₁+v₂)⊗w=v₁⊗w+v₂⊗w; v⊗(w₁+w₂)=v⊗w₁+v⊗w₂; (av)⊗w=a(v⊗w)=v⊗(aw)",
    "appliesTo": [
      "urn:csabs:concept/TensorProduct"
    ],
    "assumptions": [
      "v,v₁,v₂∈V; w,w₁,w₂∈W; a∈F; all vector spaces use the same commutative field F."
    ],
    "reviewStatus": "editorial definition; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/mathlib-tensor-universal"
    ],
    "sourceLocator": "TensorProduct pairing and lift (bilinear interface)",
    "sourceNote": "Defining constraint or equation adapted to the declared carriers and catalog notation.",
    "provenanceKind": "adapted",
    "ruleRole": "structure-law"
  },
  {
    "id": "urn:csabs:axiom/TensorProduct-universal-property",
    "type": "Axiom",
    "name": "universal-property",
    "statement": "Every bilinear map has exactly one linear extension agreeing on pure tensors.",
    "formalStatement": "∀F-vector space U, ∀bilinear b:V×W→U, ∃!linear L:V⊗_F W→U:∀v,w:L(v⊗w)=b(v,w)",
    "appliesTo": [
      "urn:csabs:concept/TensorProduct"
    ],
    "assumptions": [
      "⊗:V×W→V⊗_F W; Hom_F(V⊗_F W,U)≅Bilin_F(V,W;U)",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial definition; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/mathlib-tensor-universal"
    ],
    "sourceLocator": "TensorProduct.lift; lift.tmul; lift.unique",
    "sourceNote": "Defining constraint or equation adapted to the declared carriers and catalog notation.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:theorem/TensorProduct-pure-extensionality",
    "type": "Theorem",
    "name": "pure-extensionality",
    "statement": "Linear maps out of a tensor product are determined by pure tensors.",
    "formalStatement": "L₁,L₂:V⊗_F W→U linear and (∀v,w:L₁(v⊗w)=L₂(v⊗w)) ⇒ L₁=L₂",
    "appliesTo": [
      "urn:csabs:concept/TensorProduct"
    ],
    "assumptions": [
      "⊗:V×W→V⊗_F W; Hom_F(V⊗_F W,U)≅Bilin_F(V,W;U)",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial derivation; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/mathlib-tensor-universal"
    ],
    "sourceLocator": "TensorProduct.ext",
    "sourceNote": "Derived from the linked local premises; proof sketch gives the adaptation.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/TensorProduct-pairing-bilinear",
      "urn:csabs:axiom/TensorProduct-universal-property",
      "urn:csabs:operation/TensorProduct-pure",
      "urn:csabs:operation/TensorProduct-lift"
    ],
    "proofSketch": "The shared restriction to pure tensors is bilinear. Both maps are linear extensions of it; uniqueness in the universal property gives equality."
  }
]
```
<!-- graph-record:end -->
