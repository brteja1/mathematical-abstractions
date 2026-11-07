# Structural Induction

A proof principle for inductively generated finite values: prove the property for every constructor assuming it for its recursive arguments.

**Notation:** For each constructor K, (∀recursive arguments t: P(t)) ⇒ P(K(...))

**Stable ID:** `urn:csabs:concept/StructuralInduction`

**Categories:** Counting and induction

**Kind:** principle

**Prerequisites:** [Natural Number](NaturalNumber.md)

## Interface and scope

**axiomBasis:** Selected presentation: A proof principle for inductively generated finite values: prove the property for every constructor assuming it for its recursive arguments. Governing rules: Values form the least set closed under the given finitary constructors. A constructor-closed predicate contains every generated value.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**noPrimitiveOperationsReason:** This entry is a theorem/proof schema over its stated carriers and constructor signature. It introduces no new value-level operation; the quantified functions or constructors belong to its prerequisites.

**verificationObligation:** Instantiate carrier, equality, and stated semantic conventions before using this entry.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

**provenanceStatus:** legacy-source-missing

## Operations

No entries recorded. This does not assert absence of mathematical facts.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-StructuralInduction-least-carrier"></a>

### least-carrier

`urn:csabs:axiom/StructuralInduction-least-carrier`

**statement:** Values form the least set closed under the given finitary constructors.

**formalStatement:** T=μX.F(X), for the stated strictly positive finitary constructor signature F

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-StructuralInduction-induction-schema"></a>

### induction-schema

`urn:csabs:axiom/StructuralInduction-induction-schema`

**statement:** A constructor-closed predicate contains every generated value.

**formalStatement:** ∀K: (P holds on each recursive argument ⇒ P holds on K(arguments)) ⇒ ∀t∈T:P(t)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

<a id="node-urn-csabs-law-StructuralInduction-core"></a>

### law/StructuralInduction-core

`urn:csabs:law/StructuralInduction-core`

**statement:** A predicate preserved by every constructor holds for every generated value.

**formalStatement:** ∀t in the least constructor-closed carrier: P(t)

**reviewStatus:** editorial-summary; not machine-proved

**assumptions:** Use the carrier and semantic convention in the linked concept definition.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [least-carrier](StructuralInduction.md#node-urn-csabs-axiom-StructuralInduction-least-carrier); [induction-schema](StructuralInduction.md#node-urn-csabs-axiom-StructuralInduction-induction-schema)

**provenanceStatus:** legacy-source-missing

## Theorems

<a id="node-urn-csabs-theorem-StructuralInduction-constructor-uniqueness"></a>

### constructor-uniqueness

`urn:csabs:theorem/StructuralInduction-constructor-uniqueness`

**statement:** Two constructor-respecting recursive maps into the same algebra agree.

**formalStatement:** f(K(args))=K′(f(recArgs)); g(K(args))=K′(g(recArgs)) ⇒ f=g

**proofSketch:** Induct on generated values; equal recursive results give the same constructor output.

**assumptions:** The explicit basis, carriers, and side conditions stated for StructuralInduction apply.

**dependsOn:** [least-carrier](StructuralInduction.md#node-urn-csabs-axiom-StructuralInduction-least-carrier); [induction-schema](StructuralInduction.md#node-urn-csabs-axiom-StructuralInduction-induction-schema)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Concept provenance

Historical source gap retained; see `provenanceStatus` and the frozen baseline.

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/StructuralInduction",
    "type": "Concept",
    "shortForm": "StructuralInduction",
    "fullName": "Structural Induction",
    "category": [
      "urn:csabs:category/combinatorics"
    ],
    "kind": "urn:csabs:kind/principle",
    "definition": "A proof principle for inductively generated finite values: prove the property for every constructor assuming it for its recursive arguments.",
    "notation": "For each constructor K, (∀recursive arguments t: P(t)) ⇒ P(K(...))",
    "hasOperation": [],
    "hasAxiom": [
      "urn:csabs:axiom/StructuralInduction-least-carrier",
      "urn:csabs:axiom/StructuralInduction-induction-schema"
    ],
    "hasLaw": [
      "urn:csabs:law/StructuralInduction-core"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/StructuralInduction-constructor-uniqueness"
    ],
    "requiresConcept": [
      "urn:csabs:concept/NaturalNumber"
    ],
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Instantiate carrier, equality, and stated semantic conventions before using this entry.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: A proof principle for inductively generated finite values: prove the property for every constructor assuming it for its recursive arguments. Governing rules: Values form the least set closed under the given finitary constructors. A constructor-closed predicate contains every generated value.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "noPrimitiveOperationsReason": "This entry is a theorem/proof schema over its stated carriers and constructor signature. It introduces no new value-level operation; the quantified functions or constructors belong to its prerequisites.",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/StructuralInduction-least-carrier",
    "type": "Axiom",
    "name": "least-carrier",
    "statement": "Values form the least set closed under the given finitary constructors.",
    "formalStatement": "T=μX.F(X), for the stated strictly positive finitary constructor signature F",
    "appliesTo": [
      "urn:csabs:concept/StructuralInduction"
    ],
    "assumptions": [
      "All variables range over the carriers and semantic conventions specified in this concept."
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/StructuralInduction-induction-schema",
    "type": "Axiom",
    "name": "induction-schema",
    "statement": "A constructor-closed predicate contains every generated value.",
    "formalStatement": "∀K: (P holds on each recursive argument ⇒ P holds on K(arguments)) ⇒ ∀t∈T:P(t)",
    "appliesTo": [
      "urn:csabs:concept/StructuralInduction"
    ],
    "assumptions": [
      "All variables range over the carriers and semantic conventions specified in this concept."
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:law/StructuralInduction-core",
    "type": "Law",
    "statement": "A predicate preserved by every constructor holds for every generated value.",
    "formalStatement": "∀t in the least constructor-closed carrier: P(t)",
    "appliesTo": [
      "urn:csabs:concept/StructuralInduction"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "assumptions": [
      "Use the carrier and semantic convention in the linked concept definition."
    ],
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/StructuralInduction-least-carrier",
      "urn:csabs:axiom/StructuralInduction-induction-schema"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/StructuralInduction-constructor-uniqueness",
    "type": "Theorem",
    "name": "constructor-uniqueness",
    "statement": "Two constructor-respecting recursive maps into the same algebra agree.",
    "formalStatement": "f(K(args))=K′(f(recArgs)); g(K(args))=K′(g(recArgs)) ⇒ f=g",
    "proofSketch": "Induct on generated values; equal recursive results give the same constructor output.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for StructuralInduction apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/StructuralInduction"
    ],
    "dependsOn": [
      "urn:csabs:axiom/StructuralInduction-least-carrier",
      "urn:csabs:axiom/StructuralInduction-induction-schema"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
