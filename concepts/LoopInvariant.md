# Loop Invariant

A predicate true before a loop and preserved whenever its body executes; termination requires a separate argument.

**Notation:** P⇒I; {I∧b} C {I}

**Stable ID:** `urn:csabs:concept/LoopInvariant`

**Categories:** Programming-language semantics

**Kind:** principle

**Prerequisites:** [Hoare Triple](HoareTriple.md)

## Interface and scope

**axiomBasis:** Selected presentation: A predicate true before a loop and preserved whenever its body executes; termination requires a separate argument. Governing rules: The proposed invariant holds before entering the loop. Each normally terminating enabled body execution preserves the invariant.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**verificationObligation:** Instantiate carrier, equality, and stated semantic conventions before using this entry.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-LoopInvariant-basis-preserves"></a>

### preserves

`urn:csabs:operation/LoopInvariant-basis-preserves`

**signature:** preserves : Predicate×Guard×Command→Prop

**description:** States that normally terminating enabled body executions preserve the predicate.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-LoopInvariant-initialization"></a>

### initialization

`urn:csabs:axiom/LoopInvariant-initialization`

**statement:** The proposed invariant holds before entering the loop.

**formalStatement:** ∀s:P(s)⇒I(s)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-LoopInvariant-preservation"></a>

### preservation

`urn:csabs:axiom/LoopInvariant-preservation`

**statement:** Each normally terminating enabled body execution preserves the invariant.

**formalStatement:** ∀s,t:I(s)∧b(s)∧Exec_C(s,t)⇒I(t)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

<a id="node-urn-csabs-law-LoopInvariant-core"></a>

### law/LoopInvariant-core

`urn:csabs:law/LoopInvariant-core`

**statement:** The while rule yields partial correctness.

**formalStatement:** {I∧b}C{I} ⇒ {I}while b do C{I∧¬b}

**reviewStatus:** editorial-summary; not machine-proved

**assumptions:** Use the carrier and semantic convention in the linked concept definition.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [initialization](LoopInvariant.md#node-urn-csabs-axiom-LoopInvariant-initialization); [preservation](LoopInvariant.md#node-urn-csabs-axiom-LoopInvariant-preservation)

**provenanceStatus:** legacy-source-missing

## Theorems

<a id="node-urn-csabs-theorem-LoopInvariant-exit-correctness"></a>

### exit-correctness

`urn:csabs:theorem/LoopInvariant-exit-correctness`

**statement:** A preserved loop invariant holds at normal termination, where the guard is false.

**formalStatement:** P⇒I ∧ {I∧b}C{I} ⇒ {P}while b do C{I∧¬b}

**proofSketch:** Induct on the number of completed iterations of a normally terminating loop.

**assumptions:** The explicit basis, carriers, and side conditions stated for LoopInvariant apply.

**dependsOn:** [initialization](LoopInvariant.md#node-urn-csabs-axiom-LoopInvariant-initialization); [preservation](LoopInvariant.md#node-urn-csabs-axiom-LoopInvariant-preservation)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Concept provenance

- [Software Foundations: Hoare Logic](https://softwarefoundations.cis.upenn.edu/plf-current/Hoare.html); sourceRole: reference-for-selected-basis

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/LoopInvariant",
    "type": "Concept",
    "shortForm": "LoopInvariant",
    "fullName": "Loop Invariant",
    "category": [
      "urn:csabs:category/programming-semantics"
    ],
    "kind": "urn:csabs:kind/principle",
    "definition": "A predicate true before a loop and preserved whenever its body executes; termination requires a separate argument.",
    "notation": "P⇒I; {I∧b} C {I}",
    "hasOperation": [
      "urn:csabs:operation/LoopInvariant-basis-preserves"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/LoopInvariant-initialization",
      "urn:csabs:axiom/LoopInvariant-preservation"
    ],
    "hasLaw": [
      "urn:csabs:law/LoopInvariant-core"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/LoopInvariant-exit-correctness"
    ],
    "requiresConcept": [
      "urn:csabs:concept/HoareTriple"
    ],
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Instantiate carrier, equality, and stated semantic conventions before using this entry.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: A predicate true before a loop and preserved whenever its body executes; termination requires a separate argument. Governing rules: The proposed invariant holds before entering the loop. Each normally terminating enabled body execution preserves the invariant.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "source": [
      "urn:csabs:source/sf-hoare"
    ]
  },
  {
    "id": "urn:csabs:operation/LoopInvariant-basis-preserves",
    "type": "Operation",
    "name": "preserves",
    "signature": "preserves : Predicate×Guard×Command→Prop",
    "description": "States that normally terminating enabled body executions preserve the predicate.",
    "concept": "urn:csabs:concept/LoopInvariant"
  },
  {
    "id": "urn:csabs:axiom/LoopInvariant-initialization",
    "type": "Axiom",
    "name": "initialization",
    "statement": "The proposed invariant holds before entering the loop.",
    "formalStatement": "∀s:P(s)⇒I(s)",
    "appliesTo": [
      "urn:csabs:concept/LoopInvariant"
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
    "id": "urn:csabs:axiom/LoopInvariant-preservation",
    "type": "Axiom",
    "name": "preservation",
    "statement": "Each normally terminating enabled body execution preserves the invariant.",
    "formalStatement": "∀s,t:I(s)∧b(s)∧Exec_C(s,t)⇒I(t)",
    "appliesTo": [
      "urn:csabs:concept/LoopInvariant"
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
    "id": "urn:csabs:law/LoopInvariant-core",
    "type": "Law",
    "statement": "The while rule yields partial correctness.",
    "formalStatement": "{I∧b}C{I} ⇒ {I}while b do C{I∧¬b}",
    "appliesTo": [
      "urn:csabs:concept/LoopInvariant"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "assumptions": [
      "Use the carrier and semantic convention in the linked concept definition."
    ],
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/LoopInvariant-initialization",
      "urn:csabs:axiom/LoopInvariant-preservation"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/LoopInvariant-exit-correctness",
    "type": "Theorem",
    "name": "exit-correctness",
    "statement": "A preserved loop invariant holds at normal termination, where the guard is false.",
    "formalStatement": "P⇒I ∧ {I∧b}C{I} ⇒ {P}while b do C{I∧¬b}",
    "proofSketch": "Induct on the number of completed iterations of a normally terminating loop.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for LoopInvariant apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/LoopInvariant"
    ],
    "dependsOn": [
      "urn:csabs:axiom/LoopInvariant-initialization",
      "urn:csabs:axiom/LoopInvariant-preservation"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
