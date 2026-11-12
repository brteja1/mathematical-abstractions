# Option Type

A value that is either absent or a present payload, using a tag to distinguish absence from every payload.

**Notation:** Option(A)=1+A; None or Some(a)

**Stable ID:** `urn:csabs:concept/OptionType`

**Categories:** Types and semantics

**Kind:** Numeric data type

**Prerequisites:** [Sum Type](SumType.md), [Unit type](UnitType.md)

**Specializes:** [Sum Type](SumType.md)

## Backlinks

- [Nonce-based authenticated encryption with associated data](AEAD.md) — `requiresConcept`
- [Finite ordered binary tree with node labels](BinaryTree.md) — `requiresConcept`
- [Nonempty bounded closed interval](ClosedInterval.md) — `requiresConcept`
- [Finite fused sequence iterator](FiniteIterator.md) — `requiresConcept`
- [Resolved generic argument binding with ordered defaults](GenericArgumentBinding.md) — `requiresConcept`
- [Finite allocated heap store](HeapStore.md) — `requiresConcept`
- [Mutex (non-reentrant mutual-exclusion lock)](Mutex.md) — `requiresConcept`
- [Sequential object heap with reference identity](ObjectHeap.md) — `requiresConcept`
- [Finite RDF 1.1 dataset](RDFDataset.md) — `requiresConcept`

## Mathematical formulation

Option(A)=1+A with constructors none and some(a). some(a)=some(b) ⇔ a=b; none≠some(a). Case analysis distinguishes absence from every present value.

**Lean formulation** (in its source module context):

```lean
abbrev OptionType (A : Type u) := Option A
```

**Source:** [`Catalog.OptionType`](../lean/Catalog/Foundations.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Lean Option A; none and some are disjoint constructors.

**Limits:** Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Extensional total set-like types: constructor/eliminator beta and eta equations; operation-definition equations where specified. Equality of functions is pointwise; no divergence, effects, or bottom values.

**basisKind:** extensional-type-theory

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**specializationNote:** Instantiate SumType at UnitType and A: None corresponds to inl(⋆), Some(a) to inr(a), with the corresponding case eliminator. This is an explicit tagged-type identification.

**verificationObligation:** Instantiate type parameters and operation domains.; Function equality here is extensional; translating to intensional type theory may require function extensionality.; Account separately for nontermination, exceptions, mutation, or untagged representation in concrete software.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-OptionType-some"></a>

### some

`urn:csabs:operation/OptionType-some`

**signature:** Some : A→Option(A)

**description:** Constructs a present value.

<a id="node-urn-csabs-operation-option-none"></a>

### None

`urn:csabs:operation/option-none`

**signature:** None : Option(A)

**description:** Constructs absence, distinct from every present value.

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

<a id="node-urn-csabs-operation-option-case"></a>

### optionCase

`urn:csabs:operation/option-case`

**signature:** optionCase : C×(A→C)×Option(A)→C

**description:** Returns the default value for None and applies a branch to a Some payload.

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

<a id="node-urn-csabs-operation-option-map"></a>

### mapOption

`urn:csabs:operation/option-map`

**signature:** mapOption : (A→B)→Option(A)→Option(B)

**description:** Maps a present payload and preserves absence.

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

## Axioms and defining rules

<a id="node-urn-csabs-axiom-option-case-none"></a>

### option-case-none

`urn:csabs:axiom/option-case-none`

**statement:** Case analysis of absence returns the default.

**formalStatement:** optionCase(c,f,None)=c

**assumptions:** Extensional total set-like types; all displayed functions total and correctly typed.

**dependsOn:** [optionCase](OptionType.md#node-urn-csabs-operation-option-case); [None](OptionType.md#node-urn-csabs-operation-option-none)

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

<a id="node-urn-csabs-axiom-option-case-some"></a>

### option-case-some

`urn:csabs:axiom/option-case-some`

**statement:** Case analysis of a present value applies the branch.

**formalStatement:** optionCase(c,f,Some(a))=f(a)

**assumptions:** Extensional total set-like types; all displayed functions total and correctly typed.

**dependsOn:** [optionCase](OptionType.md#node-urn-csabs-operation-option-case)

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

<a id="node-urn-csabs-axiom-option-eta"></a>

### option-eta

`urn:csabs:axiom/option-eta`

**statement:** Every function out of Option is determined by its absent and present cases.

**formalStatement:** h=optionCase(h(None),h∘Some)

**assumptions:** Extensional total set-like types; all displayed functions total and correctly typed.

**dependsOn:** [optionCase](OptionType.md#node-urn-csabs-operation-option-case)

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

<a id="node-urn-csabs-axiom-map-option-definition"></a>

### map-option-definition

`urn:csabs:axiom/map-option-definition`

**statement:** Option mapping is defined by case analysis preserving None.

**formalStatement:** mapOption(f)=optionCase(None,Some∘f)

**assumptions:** Extensional total set-like types; all displayed functions total and correctly typed.

**dependsOn:** [mapOption](OptionType.md#node-urn-csabs-operation-option-map); [optionCase](OptionType.md#node-urn-csabs-operation-option-case)

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

## Laws

<a id="node-urn-csabs-law-OptionType-core"></a>

### law/OptionType-core

`urn:csabs:law/OptionType-core`

**statement:** The Some constructor is injective and distinct from None.

**formalStatement:** Some(a)=Some(b) iff a=b; None≠Some(a)

**reviewStatus:** editorial-summary; not machine-proved

**assumptions:** Use the carrier and semantic convention in the linked concept definition.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [option-constructors](OptionType.md#node-urn-csabs-theorem-option-constructors); [option-case-none](OptionType.md#node-urn-csabs-axiom-option-case-none); [option-case-some](OptionType.md#node-urn-csabs-axiom-option-case-some); [option-eta](OptionType.md#node-urn-csabs-axiom-option-eta); [map-option-definition](OptionType.md#node-urn-csabs-axiom-map-option-definition)

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-law-option-map-identity"></a>

### option-map-identity

`urn:csabs:law/option-map-identity`

**statement:** Mapping identity over an optional value preserves it.

**formalStatement:** mapOption(id_A)=id_(Option(A))

**assumptions:** Extensional total set-like types; all displayed functions total and correctly typed.

**dependsOn:** [option-case-none](OptionType.md#node-urn-csabs-axiom-option-case-none); [option-case-some](OptionType.md#node-urn-csabs-axiom-option-case-some); [option-eta](OptionType.md#node-urn-csabs-axiom-option-eta); [map-option-definition](OptionType.md#node-urn-csabs-axiom-map-option-definition)

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**proofSketch:** Check None and Some and apply option eta.

<a id="node-urn-csabs-law-option-map-composition"></a>

### option-map-composition

`urn:csabs:law/option-map-composition`

**statement:** Option mapping preserves function composition.

**formalStatement:** mapOption(g)∘mapOption(f)=mapOption(g∘f)

**assumptions:** Extensional total set-like types; all displayed functions total and correctly typed.

**dependsOn:** [option-case-none](OptionType.md#node-urn-csabs-axiom-option-case-none); [option-case-some](OptionType.md#node-urn-csabs-axiom-option-case-some); [option-eta](OptionType.md#node-urn-csabs-axiom-option-eta); [map-option-definition](OptionType.md#node-urn-csabs-axiom-map-option-definition)

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**proofSketch:** Check None and Some and apply option eta.

## Theorems

<a id="node-urn-csabs-theorem-option-constructors"></a>

### option-constructors

`urn:csabs:theorem/option-constructors`

**statement:** Some is injective and None is distinct from every Some value.

**formalStatement:** Some(a)=Some(b) iff a=b; None≠Some(a)

**assumptions:** Extensional total set-like types; all displayed functions total and correctly typed.

**dependsOn:** [option-case-none](OptionType.md#node-urn-csabs-axiom-option-case-none); [option-case-some](OptionType.md#node-urn-csabs-axiom-option-case-some); [option-eta](OptionType.md#node-urn-csabs-axiom-option-eta); [map-option-definition](OptionType.md#node-urn-csabs-axiom-map-option-definition)

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**proofSketch:** Identify Option(A) with 1+A and use the injectivity and disjointness of sum injections.

<a id="node-urn-csabs-theorem-OptionType-some-not-none"></a>

### some-not-none

`urn:csabs:theorem/OptionType-some-not-none`

**statement:** Every present option is distinguishable from absence.

**formalStatement:** Some(a)≠None

**proofSketch:** Use the already established option constructor disjointness theorem.

**assumptions:** The explicit basis, carriers, and side conditions stated for OptionType apply.

**dependsOn:** [option-case-none](OptionType.md#node-urn-csabs-axiom-option-case-none); [option-case-some](OptionType.md#node-urn-csabs-axiom-option-case-some); [option-eta](OptionType.md#node-urn-csabs-axiom-option-eta); [map-option-definition](OptionType.md#node-urn-csabs-axiom-map-option-definition)

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
    "id": "urn:csabs:concept/OptionType",
    "type": "Concept",
    "shortForm": "OptionType",
    "fullName": "Option Type",
    "category": [
      "urn:csabs:category/types"
    ],
    "kind": "urn:csabs:kind/data-type",
    "definition": "A value that is either absent or a present payload, using a tag to distinguish absence from every payload.",
    "notation": "Option(A)=1+A; None or Some(a)",
    "hasOperation": [
      "urn:csabs:operation/OptionType-some",
      "urn:csabs:operation/option-none",
      "urn:csabs:operation/option-case",
      "urn:csabs:operation/option-map"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/option-case-none",
      "urn:csabs:axiom/option-case-some",
      "urn:csabs:axiom/option-eta",
      "urn:csabs:axiom/map-option-definition"
    ],
    "hasLaw": [
      "urn:csabs:law/OptionType-core",
      "urn:csabs:law/option-map-identity",
      "urn:csabs:law/option-map-composition"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/option-constructors",
      "urn:csabs:theorem/OptionType-some-not-none"
    ],
    "requiresConcept": [
      "urn:csabs:concept/SumType",
      "urn:csabs:concept/UnitType"
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
    "basisKind": "extensional-type-theory",
    "specializationOf": [
      "urn:csabs:concept/SumType"
    ],
    "specializationNote": "Instantiate SumType at UnitType and A: None corresponds to inl(⋆), Some(a) to inr(a), with the corresponding case eliminator. This is an explicit tagged-type identification.",
    "leanFormulation": "abbrev OptionType (A : Type u) := Option A",
    "formulationSource": "urn:csabs:source/local-lean-Foundations",
    "formulationLocator": "Catalog.OptionType",
    "formulationScope": "model",
    "leanModelMapping": "Lean Option A; none and some are disjoint constructors.",
    "leanModelLimitations": "Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.",
    "mathematicalFormulation": "Option(A)=1+A with constructors none and some(a). some(a)=some(b) ⇔ a=b; none≠some(a). Case analysis distinguishes absence from every present value."
  },
  {
    "id": "urn:csabs:operation/OptionType-some",
    "type": "Operation",
    "name": "some",
    "signature": "Some : A→Option(A)",
    "description": "Constructs a present value.",
    "concept": "urn:csabs:concept/OptionType"
  },
  {
    "id": "urn:csabs:operation/option-none",
    "type": "Operation",
    "name": "None",
    "signature": "None : Option(A)",
    "description": "Constructs absence, distinct from every present value.",
    "concept": "urn:csabs:concept/OptionType",
    "source": [
      "urn:csabs:source/awodey-types"
    ]
  },
  {
    "id": "urn:csabs:operation/option-case",
    "type": "Operation",
    "name": "optionCase",
    "signature": "optionCase : C×(A→C)×Option(A)→C",
    "description": "Returns the default value for None and applies a branch to a Some payload.",
    "concept": "urn:csabs:concept/OptionType",
    "source": [
      "urn:csabs:source/awodey-types"
    ]
  },
  {
    "id": "urn:csabs:operation/option-map",
    "type": "Operation",
    "name": "mapOption",
    "signature": "mapOption : (A→B)→Option(A)→Option(B)",
    "description": "Maps a present payload and preserves absence.",
    "concept": "urn:csabs:concept/OptionType",
    "source": [
      "urn:csabs:source/awodey-types"
    ]
  },
  {
    "id": "urn:csabs:axiom/option-case-none",
    "type": "Axiom",
    "name": "option-case-none",
    "statement": "Case analysis of absence returns the default.",
    "formalStatement": "optionCase(c,f,None)=c",
    "assumptions": [
      "Extensional total set-like types; all displayed functions total and correctly typed."
    ],
    "appliesTo": [
      "urn:csabs:concept/OptionType"
    ],
    "dependsOn": [
      "urn:csabs:operation/option-case",
      "urn:csabs:operation/option-none"
    ],
    "source": [
      "urn:csabs:source/awodey-types"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law"
  },
  {
    "id": "urn:csabs:axiom/option-case-some",
    "type": "Axiom",
    "name": "option-case-some",
    "statement": "Case analysis of a present value applies the branch.",
    "formalStatement": "optionCase(c,f,Some(a))=f(a)",
    "assumptions": [
      "Extensional total set-like types; all displayed functions total and correctly typed."
    ],
    "appliesTo": [
      "urn:csabs:concept/OptionType"
    ],
    "dependsOn": [
      "urn:csabs:operation/option-case"
    ],
    "source": [
      "urn:csabs:source/awodey-types"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law"
  },
  {
    "id": "urn:csabs:axiom/option-eta",
    "type": "Axiom",
    "name": "option-eta",
    "statement": "Every function out of Option is determined by its absent and present cases.",
    "formalStatement": "h=optionCase(h(None),h∘Some)",
    "assumptions": [
      "Extensional total set-like types; all displayed functions total and correctly typed."
    ],
    "appliesTo": [
      "urn:csabs:concept/OptionType"
    ],
    "dependsOn": [
      "urn:csabs:operation/option-case"
    ],
    "source": [
      "urn:csabs:source/awodey-types"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law"
  },
  {
    "id": "urn:csabs:axiom/map-option-definition",
    "type": "Axiom",
    "name": "map-option-definition",
    "statement": "Option mapping is defined by case analysis preserving None.",
    "formalStatement": "mapOption(f)=optionCase(None,Some∘f)",
    "assumptions": [
      "Extensional total set-like types; all displayed functions total and correctly typed."
    ],
    "appliesTo": [
      "urn:csabs:concept/OptionType"
    ],
    "dependsOn": [
      "urn:csabs:operation/option-map",
      "urn:csabs:operation/option-case"
    ],
    "source": [
      "urn:csabs:source/awodey-types"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law"
  },
  {
    "id": "urn:csabs:law/OptionType-core",
    "type": "Law",
    "statement": "The Some constructor is injective and distinct from None.",
    "formalStatement": "Some(a)=Some(b) iff a=b; None≠Some(a)",
    "appliesTo": [
      "urn:csabs:concept/OptionType"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "assumptions": [
      "Use the carrier and semantic convention in the linked concept definition."
    ],
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:theorem/option-constructors",
      "urn:csabs:axiom/option-case-none",
      "urn:csabs:axiom/option-case-some",
      "urn:csabs:axiom/option-eta",
      "urn:csabs:axiom/map-option-definition"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:law/option-map-identity",
    "type": "Law",
    "name": "option-map-identity",
    "statement": "Mapping identity over an optional value preserves it.",
    "formalStatement": "mapOption(id_A)=id_(Option(A))",
    "assumptions": [
      "Extensional total set-like types; all displayed functions total and correctly typed."
    ],
    "appliesTo": [
      "urn:csabs:concept/OptionType"
    ],
    "dependsOn": [
      "urn:csabs:axiom/option-case-none",
      "urn:csabs:axiom/option-case-some",
      "urn:csabs:axiom/option-eta",
      "urn:csabs:axiom/map-option-definition"
    ],
    "source": [
      "urn:csabs:source/awodey-types"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "proofSketch": "Check None and Some and apply option eta."
  },
  {
    "id": "urn:csabs:law/option-map-composition",
    "type": "Law",
    "name": "option-map-composition",
    "statement": "Option mapping preserves function composition.",
    "formalStatement": "mapOption(g)∘mapOption(f)=mapOption(g∘f)",
    "assumptions": [
      "Extensional total set-like types; all displayed functions total and correctly typed."
    ],
    "appliesTo": [
      "urn:csabs:concept/OptionType"
    ],
    "dependsOn": [
      "urn:csabs:axiom/option-case-none",
      "urn:csabs:axiom/option-case-some",
      "urn:csabs:axiom/option-eta",
      "urn:csabs:axiom/map-option-definition"
    ],
    "source": [
      "urn:csabs:source/awodey-types"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "proofSketch": "Check None and Some and apply option eta."
  },
  {
    "id": "urn:csabs:theorem/option-constructors",
    "type": "Theorem",
    "name": "option-constructors",
    "statement": "Some is injective and None is distinct from every Some value.",
    "formalStatement": "Some(a)=Some(b) iff a=b; None≠Some(a)",
    "assumptions": [
      "Extensional total set-like types; all displayed functions total and correctly typed."
    ],
    "appliesTo": [
      "urn:csabs:concept/OptionType"
    ],
    "dependsOn": [
      "urn:csabs:axiom/option-case-none",
      "urn:csabs:axiom/option-case-some",
      "urn:csabs:axiom/option-eta",
      "urn:csabs:axiom/map-option-definition"
    ],
    "source": [
      "urn:csabs:source/awodey-types"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "proofSketch": "Identify Option(A) with 1+A and use the injectivity and disjointness of sum injections."
  },
  {
    "id": "urn:csabs:theorem/OptionType-some-not-none",
    "type": "Theorem",
    "name": "some-not-none",
    "statement": "Every present option is distinguishable from absence.",
    "formalStatement": "Some(a)≠None",
    "proofSketch": "Use the already established option constructor disjointness theorem.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for OptionType apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/OptionType"
    ],
    "dependsOn": [
      "urn:csabs:axiom/option-case-none",
      "urn:csabs:axiom/option-case-some",
      "urn:csabs:axiom/option-eta",
      "urn:csabs:axiom/map-option-definition"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
