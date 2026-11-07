# Function type

The type of total functions from A to B, with application and abstraction and extensional equality.

**Notation:** B^A = {f | f:A→B}; app(f,a)=f(a)

**Stable ID:** `urn:csabs:concept/FunctionType`

**Categories:** Types and semantics

**Kind:** Numeric data type

**Prerequisites:** [Total function](Function.md)

**Specializes:** [Dependent function (Pi type)](DependentFunction.md)

## Backlinks

- [Dependent function (Pi type)](DependentFunction.md) — `requiresConcept`
- [Product Type](ProductType.md) — `requiresConcept`
- [Sum Type](SumType.md) — `requiresConcept`

## Interface and scope

**axiomBasis:** Extensional total set-like types: constructor/eliminator beta and eta equations; operation-definition equations where specified. Equality of functions is pointwise; no divergence, effects, or bottom values.

**basisKind:** extensional-type-theory

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**specializationNote:**  Use the constant family B(a)=B. Abstraction and application are the same total operations, with extensional equality. No automatic inheritance of claims.

**verificationObligation:** Instantiate type parameters and operation domains.; Function equality here is extensional; translating to intensional type theory may require function extensionality.; Account separately for nontermination, exceptions, mutation, or untagged representation in concrete software.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-function-abstraction"></a>

### lambda

`urn:csabs:operation/function-abstraction`

**signature:** λ : (A→B)→B^A

**description:** Constructs a function value from a total body; binding notation is λx.t(x).

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

<a id="node-urn-csabs-operation-function-application"></a>

### apply

`urn:csabs:operation/function-application`

**signature:** apply : B^A×A→B

**description:** Evaluates a function value at an input.

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

## Axioms and defining rules

<a id="node-urn-csabs-axiom-function-beta"></a>

### function-beta

`urn:csabs:axiom/function-beta`

**statement:** Applying an abstraction substitutes the argument into its body.

**formalStatement:** apply(λx.t(x),a)=t(a)

**assumptions:** Extensional total set-like types; all displayed functions total and correctly typed.; Substitution avoids capture.

**dependsOn:** [lambda](FunctionType.md#node-urn-csabs-operation-function-abstraction); [apply](FunctionType.md#node-urn-csabs-operation-function-application)

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

<a id="node-urn-csabs-axiom-function-eta"></a>

### function-eta

`urn:csabs:axiom/function-eta`

**statement:** Abstracting the application of a function recovers that function.

**formalStatement:** λx.apply(f,x)=f

**assumptions:** Extensional total set-like types; all displayed functions total and correctly typed.; x is not free in f.

**dependsOn:** [lambda](FunctionType.md#node-urn-csabs-operation-function-abstraction); [apply](FunctionType.md#node-urn-csabs-operation-function-application)

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

<a id="node-urn-csabs-axiom-function-extensionality"></a>

### function-extensionality

`urn:csabs:axiom/function-extensionality`

**statement:** Functions with equal outputs at every input are equal.

**formalStatement:** (∀x:A: apply(f,x)=apply(g,x)) ⇒ f=g

**assumptions:** Extensional total set-like types; all displayed functions total and correctly typed.

**dependsOn:** [apply](FunctionType.md#node-urn-csabs-operation-function-application)

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-FunctionType-application-congruence"></a>

### application-congruence

`urn:csabs:theorem/FunctionType-application-congruence`

**statement:** Equal function values have equal results at every input.

**formalStatement:** f=g ⇒ ∀a:apply(f,a)=apply(g,a)

**proofSketch:** Substitute equals in application.

**assumptions:** The explicit basis, carriers, and side conditions stated for FunctionType apply.

**dependsOn:** [function-beta](FunctionType.md#node-urn-csabs-axiom-function-beta); [function-eta](FunctionType.md#node-urn-csabs-axiom-function-eta); [function-extensionality](FunctionType.md#node-urn-csabs-axiom-function-extensionality)

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
    "id": "urn:csabs:concept/FunctionType",
    "type": "Concept",
    "shortForm": "FunctionType",
    "fullName": "Function type",
    "definition": "The type of total functions from A to B, with application and abstraction and extensional equality.",
    "notation": "B^A = {f | f:A→B}; app(f,a)=f(a)",
    "category": [
      "urn:csabs:category/types"
    ],
    "kind": "urn:csabs:kind/data-type",
    "hasOperation": [
      "urn:csabs:operation/function-abstraction",
      "urn:csabs:operation/function-application"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/function-beta",
      "urn:csabs:axiom/function-eta",
      "urn:csabs:axiom/function-extensionality"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/FunctionType-application-congruence"
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
    "basisKind": "extensional-type-theory",
    "specializationOf": [
      "urn:csabs:concept/DependentFunction"
    ],
    "specializationNote": " Use the constant family B(a)=B. Abstraction and application are the same total operations, with extensional equality. No automatic inheritance of claims."
  },
  {
    "id": "urn:csabs:operation/function-abstraction",
    "type": "Operation",
    "name": "lambda",
    "signature": "λ : (A→B)→B^A",
    "description": "Constructs a function value from a total body; binding notation is λx.t(x).",
    "concept": "urn:csabs:concept/FunctionType",
    "source": [
      "urn:csabs:source/awodey-types"
    ]
  },
  {
    "id": "urn:csabs:operation/function-application",
    "type": "Operation",
    "name": "apply",
    "signature": "apply : B^A×A→B",
    "description": "Evaluates a function value at an input.",
    "concept": "urn:csabs:concept/FunctionType",
    "source": [
      "urn:csabs:source/awodey-types"
    ]
  },
  {
    "id": "urn:csabs:axiom/function-beta",
    "type": "Axiom",
    "name": "function-beta",
    "statement": "Applying an abstraction substitutes the argument into its body.",
    "formalStatement": "apply(λx.t(x),a)=t(a)",
    "assumptions": [
      "Extensional total set-like types; all displayed functions total and correctly typed.",
      "Substitution avoids capture."
    ],
    "appliesTo": [
      "urn:csabs:concept/FunctionType"
    ],
    "dependsOn": [
      "urn:csabs:operation/function-abstraction",
      "urn:csabs:operation/function-application"
    ],
    "source": [
      "urn:csabs:source/awodey-types"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law"
  },
  {
    "id": "urn:csabs:axiom/function-eta",
    "type": "Axiom",
    "name": "function-eta",
    "statement": "Abstracting the application of a function recovers that function.",
    "formalStatement": "λx.apply(f,x)=f",
    "assumptions": [
      "Extensional total set-like types; all displayed functions total and correctly typed.",
      "x is not free in f."
    ],
    "appliesTo": [
      "urn:csabs:concept/FunctionType"
    ],
    "dependsOn": [
      "urn:csabs:operation/function-abstraction",
      "urn:csabs:operation/function-application"
    ],
    "source": [
      "urn:csabs:source/awodey-types"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law"
  },
  {
    "id": "urn:csabs:axiom/function-extensionality",
    "type": "Axiom",
    "name": "function-extensionality",
    "statement": "Functions with equal outputs at every input are equal.",
    "formalStatement": "(∀x:A: apply(f,x)=apply(g,x)) ⇒ f=g",
    "assumptions": [
      "Extensional total set-like types; all displayed functions total and correctly typed."
    ],
    "appliesTo": [
      "urn:csabs:concept/FunctionType"
    ],
    "dependsOn": [
      "urn:csabs:operation/function-application"
    ],
    "source": [
      "urn:csabs:source/awodey-types"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law"
  },
  {
    "id": "urn:csabs:theorem/FunctionType-application-congruence",
    "type": "Theorem",
    "name": "application-congruence",
    "statement": "Equal function values have equal results at every input.",
    "formalStatement": "f=g ⇒ ∀a:apply(f,a)=apply(g,a)",
    "proofSketch": "Substitute equals in application.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for FunctionType apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/FunctionType"
    ],
    "dependsOn": [
      "urn:csabs:axiom/function-beta",
      "urn:csabs:axiom/function-eta",
      "urn:csabs:axiom/function-extensionality"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
