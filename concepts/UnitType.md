# Unit type

A type with one value, used as the terminal object for total functions.

**Notation:** 1={⋆}; unit:1

**Stable ID:** `urn:csabs:concept/UnitType`

**Categories:** Types and semantics

**Kind:** Numeric data type

**Prerequisites:** [Total function](Function.md)

## Backlinks

- [Option Type](OptionType.md) — `requiresConcept`
- [Sum Type](SumType.md) — `requiresConcept`

## Interface and scope

**axiomBasis:** Extensional total set-like types: constructor/eliminator beta and eta equations; operation-definition equations where specified. Equality of functions is pointwise; no divergence, effects, or bottom values.

**basisKind:** extensional-type-theory

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**verificationObligation:** Instantiate type parameters and operation domains.; Function equality here is extensional; translating to intensional type theory may require function extensionality.; Account separately for nontermination, exceptions, mutation, or untagged representation in concrete software.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-unit-value"></a>

### unit

`urn:csabs:operation/unit-value`

**signature:** ⋆ : 1

**description:** Constructs the unique unit value.

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

## Axioms and defining rules

<a id="node-urn-csabs-axiom-unit-eta"></a>

### unit-eta

`urn:csabs:axiom/unit-eta`

**statement:** Every unit value equals its sole constructor.

**formalStatement:** ∀x:1: x=⋆

**assumptions:** Extensional total set-like types; all displayed functions total and correctly typed.

**dependsOn:** [unit](UnitType.md#node-urn-csabs-operation-unit-value)

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-unit-terminal"></a>

### unit-terminal

`urn:csabs:theorem/unit-terminal`

**statement:** There is exactly one total function from any type into unit.

**formalStatement:** ∀A ∃!f:A→1

**assumptions:** Extensional total set-like types; all displayed functions total and correctly typed.

**dependsOn:** [unit-eta](UnitType.md#node-urn-csabs-axiom-unit-eta)

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**proofSketch:** The constant function λa.⋆ exists and any other function is pointwise equal to it.

<a id="node-urn-csabs-theorem-UnitType-all-values-equal"></a>

### all-values-equal

`urn:csabs:theorem/UnitType-all-values-equal`

**statement:** Every two unit values agree.

**formalStatement:** x,y:1 ⇒ x=y

**proofSketch:** Both equal the unique constructor ⋆.

**assumptions:** The explicit basis, carriers, and side conditions stated for UnitType apply.

**dependsOn:** [unit-eta](UnitType.md#node-urn-csabs-axiom-unit-eta)

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
    "id": "urn:csabs:concept/UnitType",
    "type": "Concept",
    "shortForm": "UnitType",
    "fullName": "Unit type",
    "definition": "A type with one value, used as the terminal object for total functions.",
    "notation": "1={⋆}; unit:1",
    "category": [
      "urn:csabs:category/types"
    ],
    "kind": "urn:csabs:kind/data-type",
    "hasOperation": [
      "urn:csabs:operation/unit-value"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/unit-eta"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/unit-terminal",
      "urn:csabs:theorem/UnitType-all-values-equal"
    ],
    "requiresConcept": [
      "urn:csabs:concept/Function"
    ],
    "coverageStatus": "basis-reviewed",
    "axiomBasis": "Extensional total set-like types: constructor/eliminator beta and eta equations; operation-definition equations where specified. Equality of functions is pointwise; no divergence, effects, or bottom values.",
    "source": [
      "urn:csabs:source/awodey-types"
    ],
    "verificationObligation": [
      "Instantiate type parameters and operation domains.",
      "Function equality here is extensional; translating to intensional type theory may require function extensionality.",
      "Account separately for nontermination, exceptions, mutation, or untagged representation in concrete software.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "basisKind": "extensional-type-theory"
  },
  {
    "id": "urn:csabs:operation/unit-value",
    "type": "Operation",
    "name": "unit",
    "signature": "⋆ : 1",
    "description": "Constructs the unique unit value.",
    "concept": "urn:csabs:concept/UnitType",
    "source": [
      "urn:csabs:source/awodey-types"
    ]
  },
  {
    "id": "urn:csabs:axiom/unit-eta",
    "type": "Axiom",
    "name": "unit-eta",
    "statement": "Every unit value equals its sole constructor.",
    "formalStatement": "∀x:1: x=⋆",
    "assumptions": [
      "Extensional total set-like types; all displayed functions total and correctly typed."
    ],
    "appliesTo": [
      "urn:csabs:concept/UnitType"
    ],
    "dependsOn": [
      "urn:csabs:operation/unit-value"
    ],
    "source": [
      "urn:csabs:source/awodey-types"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law"
  },
  {
    "id": "urn:csabs:theorem/unit-terminal",
    "type": "Theorem",
    "name": "unit-terminal",
    "statement": "There is exactly one total function from any type into unit.",
    "formalStatement": "∀A ∃!f:A→1",
    "assumptions": [
      "Extensional total set-like types; all displayed functions total and correctly typed."
    ],
    "appliesTo": [
      "urn:csabs:concept/UnitType"
    ],
    "dependsOn": [
      "urn:csabs:axiom/unit-eta"
    ],
    "source": [
      "urn:csabs:source/awodey-types"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "proofSketch": "The constant function λa.⋆ exists and any other function is pointwise equal to it."
  },
  {
    "id": "urn:csabs:theorem/UnitType-all-values-equal",
    "type": "Theorem",
    "name": "all-values-equal",
    "statement": "Every two unit values agree.",
    "formalStatement": "x,y:1 ⇒ x=y",
    "proofSketch": "Both equal the unique constructor ⋆.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for UnitType apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/UnitType"
    ],
    "dependsOn": [
      "urn:csabs:axiom/unit-eta"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
