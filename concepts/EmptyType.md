# Empty type

A type with no values; its eliminator supplies a unique total function into any target type.

**Notation:** 0=∅; absurd_C : 0→C

**Stable ID:** `urn:csabs:concept/EmptyType`

**Categories:** Types and semantics

**Kind:** Numeric data type

**Prerequisites:** [Total function](Function.md)

## Backlinks

- [Sum Type](SumType.md) — `requiresConcept`

## Interface and scope

**axiomBasis:** Extensional total set-like types: constructor/eliminator beta and eta equations; operation-definition equations where specified. Equality of functions is pointwise; no divergence, effects, or bottom values.

**basisKind:** extensional-type-theory

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**verificationObligation:** Instantiate type parameters and operation domains.; Function equality here is extensional; translating to intensional type theory may require function extensionality.; Account separately for nontermination, exceptions, mutation, or untagged representation in concrete software.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-empty-absurd"></a>

### absurd

`urn:csabs:operation/empty-absurd`

**signature:** absurd_C : 0→C

**description:** Eliminates an impossible input into any target; there are no input values on which to compute.

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

## Axioms and defining rules

<a id="node-urn-csabs-axiom-absurd-unique"></a>

### absurd-unique

`urn:csabs:axiom/absurd-unique`

**statement:** Every total function from the empty type equals its canonical eliminator.

**formalStatement:** ∀C ∀f:0→C: f=absurd_C

**assumptions:** Extensional total set-like types; all displayed functions total and correctly typed.

**dependsOn:** [absurd](EmptyType.md#node-urn-csabs-operation-empty-absurd)

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-empty-initial"></a>

### empty-initial

`urn:csabs:theorem/empty-initial`

**statement:** The empty type is initial in the category of set-like types and total functions.

**formalStatement:** ∀C ∃!f:0→C

**assumptions:** Extensional total set-like types; all displayed functions total and correctly typed.

**dependsOn:** [absurd-unique](EmptyType.md#node-urn-csabs-axiom-absurd-unique)

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**proofSketch:** Existence is the eliminator; uniqueness is absurd-unique.

<a id="node-urn-csabs-theorem-EmptyType-maps-out-equal"></a>

### maps-out-equal

`urn:csabs:theorem/EmptyType-maps-out-equal`

**statement:** All total maps from empty into the same target agree.

**formalStatement:** f,g:0→C ⇒ f=g

**proofSketch:** Both functions equal absurd_C by empty uniqueness.

**assumptions:** The explicit basis, carriers, and side conditions stated for EmptyType apply.

**dependsOn:** [absurd-unique](EmptyType.md#node-urn-csabs-axiom-absurd-unique)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Concept provenance

- [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference
- [Lean reference: empty type](https://lean-lang.org/doc/reference/latest/Basic-Types/The-Empty-Type/); sourceRole: reference

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/EmptyType",
    "type": "Concept",
    "shortForm": "EmptyType",
    "fullName": "Empty type",
    "definition": "A type with no values; its eliminator supplies a unique total function into any target type.",
    "notation": "0=∅; absurd_C : 0→C",
    "category": [
      "urn:csabs:category/types"
    ],
    "kind": "urn:csabs:kind/data-type",
    "hasOperation": [
      "urn:csabs:operation/empty-absurd"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/absurd-unique"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/empty-initial",
      "urn:csabs:theorem/EmptyType-maps-out-equal"
    ],
    "requiresConcept": [
      "urn:csabs:concept/Function"
    ],
    "coverageStatus": "basis-reviewed",
    "axiomBasis": "Extensional total set-like types: constructor/eliminator beta and eta equations; operation-definition equations where specified. Equality of functions is pointwise; no divergence, effects, or bottom values.",
    "source": [
      "urn:csabs:source/awodey-types",
      "urn:csabs:source/lean-empty"
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
    "id": "urn:csabs:operation/empty-absurd",
    "type": "Operation",
    "name": "absurd",
    "signature": "absurd_C : 0→C",
    "description": "Eliminates an impossible input into any target; there are no input values on which to compute.",
    "concept": "urn:csabs:concept/EmptyType",
    "source": [
      "urn:csabs:source/awodey-types"
    ]
  },
  {
    "id": "urn:csabs:axiom/absurd-unique",
    "type": "Axiom",
    "name": "absurd-unique",
    "statement": "Every total function from the empty type equals its canonical eliminator.",
    "formalStatement": "∀C ∀f:0→C: f=absurd_C",
    "assumptions": [
      "Extensional total set-like types; all displayed functions total and correctly typed."
    ],
    "appliesTo": [
      "urn:csabs:concept/EmptyType"
    ],
    "dependsOn": [
      "urn:csabs:operation/empty-absurd"
    ],
    "source": [
      "urn:csabs:source/awodey-types"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law"
  },
  {
    "id": "urn:csabs:theorem/empty-initial",
    "type": "Theorem",
    "name": "empty-initial",
    "statement": "The empty type is initial in the category of set-like types and total functions.",
    "formalStatement": "∀C ∃!f:0→C",
    "assumptions": [
      "Extensional total set-like types; all displayed functions total and correctly typed."
    ],
    "appliesTo": [
      "urn:csabs:concept/EmptyType"
    ],
    "dependsOn": [
      "urn:csabs:axiom/absurd-unique"
    ],
    "source": [
      "urn:csabs:source/awodey-types"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "proofSketch": "Existence is the eliminator; uniqueness is absurd-unique."
  },
  {
    "id": "urn:csabs:theorem/EmptyType-maps-out-equal",
    "type": "Theorem",
    "name": "maps-out-equal",
    "statement": "All total maps from empty into the same target agree.",
    "formalStatement": "f,g:0→C ⇒ f=g",
    "proofSketch": "Both functions equal absurd_C by empty uniqueness.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for EmptyType apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/EmptyType"
    ],
    "dependsOn": [
      "urn:csabs:axiom/absurd-unique"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
