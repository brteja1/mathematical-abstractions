# Product Type

A type whose values contain one value from each component type.

**Notation:** A×B = {(a,b) | a∈A ∧ b∈B}; pair(a,b)=(a,b).

**Stable ID:** `urn:csabs:concept/ProductType`

**Categories:** Types and semantics

**Kind:** Numeric data type

**Prerequisites:** [Cartesian product](CartesianProduct.md), [Function type](FunctionType.md)

## Backlinks

- [Named relational schema with attribute domains](RelationalSchema.md) — `relatedConcept`

## Interface and scope

**axiomBasis:** Extensional total set-like types: constructor/eliminator beta and eta equations; operation-definition equations where specified. Equality of functions is pointwise; no divergence, effects, or bottom values.

**basisKind:** extensional-type-theory

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**verificationObligation:** Instantiate type parameters and operation domains.; Function equality here is extensional; translating to intensional type theory may require function extensionality.; Account separately for nontermination, exceptions, mutation, or untagged representation in concrete software.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-ProductType-first"></a>

### first

`urn:csabs:operation/ProductType-first`

**signature:** fst : A×B→A

**description:** Projects the first component.

<a id="node-urn-csabs-operation-ProductType-second"></a>

### second

`urn:csabs:operation/ProductType-second`

**signature:** snd : A×B→B

**description:** Projects the second component.

<a id="node-urn-csabs-operation-product-pair"></a>

### pair

`urn:csabs:operation/product-pair`

**signature:** pair : A→B→A×B

**description:** Constructs a product from its two components.

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

<a id="node-urn-csabs-operation-product-map"></a>

### mapProduct

`urn:csabs:operation/product-map`

**signature:** mapProduct : (A→C)×(B→D)→(A×B→C×D)

**description:** Applies the respective map to each product component.

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

## Axioms and defining rules

<a id="node-urn-csabs-axiom-product-beta-first"></a>

### product-beta-first

`urn:csabs:axiom/product-beta-first`

**statement:** The first projection of a pair is its first component.

**formalStatement:** fst(pair(a,b))=a

**assumptions:** Extensional total set-like types; all displayed functions total and correctly typed.

**dependsOn:** [pair](ProductType.md#node-urn-csabs-operation-product-pair)

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

<a id="node-urn-csabs-axiom-product-beta-second"></a>

### product-beta-second

`urn:csabs:axiom/product-beta-second`

**statement:** The second projection of a pair is its second component.

**formalStatement:** snd(pair(a,b))=b

**assumptions:** Extensional total set-like types; all displayed functions total and correctly typed.

**dependsOn:** [pair](ProductType.md#node-urn-csabs-operation-product-pair)

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

<a id="node-urn-csabs-axiom-product-eta"></a>

### product-eta

`urn:csabs:axiom/product-eta`

**statement:** A product is determined by its two projections.

**formalStatement:** ∀p:A×B: pair(fst(p),snd(p))=p

**assumptions:** Extensional total set-like types; all displayed functions total and correctly typed.

**dependsOn:** [pair](ProductType.md#node-urn-csabs-operation-product-pair)

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

<a id="node-urn-csabs-axiom-map-product-definition"></a>

### map-product-definition

`urn:csabs:axiom/map-product-definition`

**statement:** Product mapping applies the supplied maps to the two projections.

**formalStatement:** mapProduct(f,g)(p)=pair(f(fst(p)),g(snd(p)))

**assumptions:** Extensional total set-like types; all displayed functions total and correctly typed.

**dependsOn:** [mapProduct](ProductType.md#node-urn-csabs-operation-product-map); [pair](ProductType.md#node-urn-csabs-operation-product-pair)

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

## Laws

<a id="node-urn-csabs-law-ProductType-core"></a>

### law/ProductType-core

`urn:csabs:law/ProductType-core`

**statement:** Pairing and projection recover each component.

**formalStatement:** fst(a,b)=a; snd(a,b)=b

**reviewStatus:** editorial-summary; not machine-proved

**assumptions:** Use the carrier and semantic convention in the linked concept definition.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [product-beta-first](ProductType.md#node-urn-csabs-axiom-product-beta-first); [product-beta-second](ProductType.md#node-urn-csabs-axiom-product-beta-second); [product-eta](ProductType.md#node-urn-csabs-axiom-product-eta); [map-product-definition](ProductType.md#node-urn-csabs-axiom-map-product-definition)

**provenanceStatus:** legacy-source-missing

## Theorems

<a id="node-urn-csabs-theorem-product-universal"></a>

### product-universal

`urn:csabs:theorem/product-universal`

**statement:** Two functions into the factors determine a unique function into the product.

**formalStatement:** ∀f:C→A,g:C→B ∃!h:C→A×B: fst∘h=f ∧ snd∘h=g

**assumptions:** Extensional total set-like types; all displayed functions total and correctly typed.

**dependsOn:** [product-beta-first](ProductType.md#node-urn-csabs-axiom-product-beta-first); [product-beta-second](ProductType.md#node-urn-csabs-axiom-product-beta-second); [product-eta](ProductType.md#node-urn-csabs-axiom-product-eta); [map-product-definition](ProductType.md#node-urn-csabs-axiom-map-product-definition)

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**proofSketch:** Use h(c)=pair(f(c),g(c)). Projection computation gives existence and eta gives uniqueness.

<a id="node-urn-csabs-theorem-ProductType-pair-injective"></a>

### pair-injective

`urn:csabs:theorem/ProductType-pair-injective`

**statement:** Pair construction is injective in both components.

**formalStatement:** pair(a,b)=pair(a′,b′) iff a=a′∧b=b′

**proofSketch:** Apply the two projections for the forward implication and congruence for the reverse.

**assumptions:** The explicit basis, carriers, and side conditions stated for ProductType apply.

**dependsOn:** [product-beta-first](ProductType.md#node-urn-csabs-axiom-product-beta-first); [product-beta-second](ProductType.md#node-urn-csabs-axiom-product-beta-second); [product-eta](ProductType.md#node-urn-csabs-axiom-product-eta); [map-product-definition](ProductType.md#node-urn-csabs-axiom-map-product-definition)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Concept provenance

- [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/ProductType",
    "type": "Concept",
    "shortForm": "ProductType",
    "fullName": "Product Type",
    "category": [
      "urn:csabs:category/types"
    ],
    "kind": "urn:csabs:kind/data-type",
    "definition": "A type whose values contain one value from each component type.",
    "notation": "A×B = {(a,b) | a∈A ∧ b∈B}; pair(a,b)=(a,b).",
    "hasOperation": [
      "urn:csabs:operation/ProductType-first",
      "urn:csabs:operation/ProductType-second",
      "urn:csabs:operation/product-pair",
      "urn:csabs:operation/product-map"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/product-beta-first",
      "urn:csabs:axiom/product-beta-second",
      "urn:csabs:axiom/product-eta",
      "urn:csabs:axiom/map-product-definition"
    ],
    "hasLaw": [
      "urn:csabs:law/ProductType-core"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/product-universal",
      "urn:csabs:theorem/ProductType-pair-injective"
    ],
    "requiresConcept": [
      "urn:csabs:concept/CartesianProduct",
      "urn:csabs:concept/FunctionType"
    ],
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Instantiate type parameters and operation domains.",
      "Function equality here is extensional; translating to intensional type theory may require function extensionality.",
      "Account separately for nontermination, exceptions, mutation, or untagged representation in concrete software.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Extensional total set-like types: constructor/eliminator beta and eta equations; operation-definition equations where specified. Equality of functions is pointwise; no divergence, effects, or bottom values.",
    "source": [
      "urn:csabs:source/awodey-types"
    ],
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "basisKind": "extensional-type-theory"
  },
  {
    "id": "urn:csabs:operation/ProductType-first",
    "type": "Operation",
    "name": "first",
    "signature": "fst : A×B→A",
    "description": "Projects the first component.",
    "concept": "urn:csabs:concept/ProductType"
  },
  {
    "id": "urn:csabs:operation/ProductType-second",
    "type": "Operation",
    "name": "second",
    "signature": "snd : A×B→B",
    "description": "Projects the second component.",
    "concept": "urn:csabs:concept/ProductType"
  },
  {
    "id": "urn:csabs:operation/product-pair",
    "type": "Operation",
    "name": "pair",
    "signature": "pair : A→B→A×B",
    "description": "Constructs a product from its two components.",
    "concept": "urn:csabs:concept/ProductType",
    "source": [
      "urn:csabs:source/awodey-types"
    ]
  },
  {
    "id": "urn:csabs:operation/product-map",
    "type": "Operation",
    "name": "mapProduct",
    "signature": "mapProduct : (A→C)×(B→D)→(A×B→C×D)",
    "description": "Applies the respective map to each product component.",
    "concept": "urn:csabs:concept/ProductType",
    "source": [
      "urn:csabs:source/awodey-types"
    ]
  },
  {
    "id": "urn:csabs:axiom/product-beta-first",
    "type": "Axiom",
    "name": "product-beta-first",
    "statement": "The first projection of a pair is its first component.",
    "formalStatement": "fst(pair(a,b))=a",
    "assumptions": [
      "Extensional total set-like types; all displayed functions total and correctly typed."
    ],
    "appliesTo": [
      "urn:csabs:concept/ProductType"
    ],
    "dependsOn": [
      "urn:csabs:operation/product-pair"
    ],
    "source": [
      "urn:csabs:source/awodey-types"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law"
  },
  {
    "id": "urn:csabs:axiom/product-beta-second",
    "type": "Axiom",
    "name": "product-beta-second",
    "statement": "The second projection of a pair is its second component.",
    "formalStatement": "snd(pair(a,b))=b",
    "assumptions": [
      "Extensional total set-like types; all displayed functions total and correctly typed."
    ],
    "appliesTo": [
      "urn:csabs:concept/ProductType"
    ],
    "dependsOn": [
      "urn:csabs:operation/product-pair"
    ],
    "source": [
      "urn:csabs:source/awodey-types"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law"
  },
  {
    "id": "urn:csabs:axiom/product-eta",
    "type": "Axiom",
    "name": "product-eta",
    "statement": "A product is determined by its two projections.",
    "formalStatement": "∀p:A×B: pair(fst(p),snd(p))=p",
    "assumptions": [
      "Extensional total set-like types; all displayed functions total and correctly typed."
    ],
    "appliesTo": [
      "urn:csabs:concept/ProductType"
    ],
    "dependsOn": [
      "urn:csabs:operation/product-pair"
    ],
    "source": [
      "urn:csabs:source/awodey-types"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law"
  },
  {
    "id": "urn:csabs:axiom/map-product-definition",
    "type": "Axiom",
    "name": "map-product-definition",
    "statement": "Product mapping applies the supplied maps to the two projections.",
    "formalStatement": "mapProduct(f,g)(p)=pair(f(fst(p)),g(snd(p)))",
    "assumptions": [
      "Extensional total set-like types; all displayed functions total and correctly typed."
    ],
    "appliesTo": [
      "urn:csabs:concept/ProductType"
    ],
    "dependsOn": [
      "urn:csabs:operation/product-map",
      "urn:csabs:operation/product-pair"
    ],
    "source": [
      "urn:csabs:source/awodey-types"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law"
  },
  {
    "id": "urn:csabs:law/ProductType-core",
    "type": "Law",
    "statement": "Pairing and projection recover each component.",
    "formalStatement": "fst(a,b)=a; snd(a,b)=b",
    "appliesTo": [
      "urn:csabs:concept/ProductType"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "assumptions": [
      "Use the carrier and semantic convention in the linked concept definition."
    ],
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/product-beta-first",
      "urn:csabs:axiom/product-beta-second",
      "urn:csabs:axiom/product-eta",
      "urn:csabs:axiom/map-product-definition"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/product-universal",
    "type": "Theorem",
    "name": "product-universal",
    "statement": "Two functions into the factors determine a unique function into the product.",
    "formalStatement": "∀f:C→A,g:C→B ∃!h:C→A×B: fst∘h=f ∧ snd∘h=g",
    "assumptions": [
      "Extensional total set-like types; all displayed functions total and correctly typed."
    ],
    "appliesTo": [
      "urn:csabs:concept/ProductType"
    ],
    "dependsOn": [
      "urn:csabs:axiom/product-beta-first",
      "urn:csabs:axiom/product-beta-second",
      "urn:csabs:axiom/product-eta",
      "urn:csabs:axiom/map-product-definition"
    ],
    "source": [
      "urn:csabs:source/awodey-types"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "proofSketch": "Use h(c)=pair(f(c),g(c)). Projection computation gives existence and eta gives uniqueness."
  },
  {
    "id": "urn:csabs:theorem/ProductType-pair-injective",
    "type": "Theorem",
    "name": "pair-injective",
    "statement": "Pair construction is injective in both components.",
    "formalStatement": "pair(a,b)=pair(a′,b′) iff a=a′∧b=b′",
    "proofSketch": "Apply the two projections for the forward implication and congruence for the reverse.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for ProductType apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/ProductType"
    ],
    "dependsOn": [
      "urn:csabs:axiom/product-beta-first",
      "urn:csabs:axiom/product-beta-second",
      "urn:csabs:axiom/product-eta",
      "urn:csabs:axiom/map-product-definition"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
