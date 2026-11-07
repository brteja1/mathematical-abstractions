# Pigeonhole Principle

Mapping more elements into fewer finite slots forces two distinct elements to share a slot.

**Notation:** f:A→B; A,B finite; card(A)>card(B)

**Stable ID:** `urn:csabs:concept/PigeonholePrinciple`

**Categories:** Counting and induction

**Kind:** principle

**Prerequisites:** [Total function](Function.md), [Set](Set.md)

## Interface and scope

**axiomBasis:** Selected presentation: Mapping more elements into fewer finite slots forces two distinct elements to share a slot. Governing rules: The principle is a theorem schema in finite set theory, rather than a new foundational postulate.

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

<a id="node-urn-csabs-axiom-PigeonholePrinciple-finite-counting-context"></a>

### finite-counting-context

`urn:csabs:axiom/PigeonholePrinciple-finite-counting-context`

**statement:** The principle is a theorem schema in finite set theory, rather than a new foundational postulate.

**formalStatement:** A,B finite; f:A→B; card(A)>card(B)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-law-PigeonholePrinciple-core"></a>

### law/PigeonholePrinciple-core

`urn:csabs:law/PigeonholePrinciple-core`

**statement:** No injection exists from a larger finite set into a smaller finite set.

**formalStatement:** ∃x,y∈A: x≠y ∧ f(x)=f(y)

**reviewStatus:** editorial-summary; not machine-proved

**assumptions:** Use the carrier and semantic convention in the linked concept definition.

**proofSketch:** An injection between finite sets implies the domain cardinality is at most that of the codomain, contradicting the strict inequality.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [finite-counting-context](PigeonholePrinciple.md#node-urn-csabs-axiom-PigeonholePrinciple-finite-counting-context)

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-theorem-PigeonholePrinciple-collision-finite"></a>

### collision-finite

`urn:csabs:theorem/PigeonholePrinciple-collision-finite`

**statement:** A map from a strictly larger finite set into a smaller one has a collision.

**formalStatement:** card(A)>card(B) ⇒ ∃a≠a′:f(a)=f(a′)

**proofSketch:** If no collision existed, f would inject A into B, contradicting finite cardinality monotonicity.

**assumptions:** The explicit basis, carriers, and side conditions stated for PigeonholePrinciple apply.

**dependsOn:** [finite-counting-context](PigeonholePrinciple.md#node-urn-csabs-axiom-PigeonholePrinciple-finite-counting-context)

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
    "id": "urn:csabs:concept/PigeonholePrinciple",
    "type": "Concept",
    "shortForm": "PigeonholePrinciple",
    "fullName": "Pigeonhole Principle",
    "category": [
      "urn:csabs:category/combinatorics"
    ],
    "kind": "urn:csabs:kind/principle",
    "definition": "Mapping more elements into fewer finite slots forces two distinct elements to share a slot.",
    "notation": "f:A→B; A,B finite; card(A)>card(B)",
    "hasOperation": [],
    "hasAxiom": [
      "urn:csabs:axiom/PigeonholePrinciple-finite-counting-context"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:law/PigeonholePrinciple-core",
      "urn:csabs:theorem/PigeonholePrinciple-collision-finite"
    ],
    "requiresConcept": [
      "urn:csabs:concept/Function",
      "urn:csabs:concept/Set"
    ],
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Instantiate carrier, equality, and stated semantic conventions before using this entry.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: Mapping more elements into fewer finite slots forces two distinct elements to share a slot. Governing rules: The principle is a theorem schema in finite set theory, rather than a new foundational postulate.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "noPrimitiveOperationsReason": "This entry is a theorem/proof schema over its stated carriers and constructor signature. It introduces no new value-level operation; the quantified functions or constructors belong to its prerequisites.",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/PigeonholePrinciple-finite-counting-context",
    "type": "Axiom",
    "name": "finite-counting-context",
    "statement": "The principle is a theorem schema in finite set theory, rather than a new foundational postulate.",
    "formalStatement": "A,B finite; f:A→B; card(A)>card(B)",
    "appliesTo": [
      "urn:csabs:concept/PigeonholePrinciple"
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
    "id": "urn:csabs:law/PigeonholePrinciple-core",
    "type": "Theorem",
    "statement": "No injection exists from a larger finite set into a smaller finite set.",
    "formalStatement": "∃x,y∈A: x≠y ∧ f(x)=f(y)",
    "appliesTo": [
      "urn:csabs:concept/PigeonholePrinciple"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "assumptions": [
      "Use the carrier and semantic convention in the linked concept definition."
    ],
    "proofSketch": "An injection between finite sets implies the domain cardinality is at most that of the codomain, contradicting the strict inequality.",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/PigeonholePrinciple-finite-counting-context"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/PigeonholePrinciple-collision-finite",
    "type": "Theorem",
    "name": "collision-finite",
    "statement": "A map from a strictly larger finite set into a smaller one has a collision.",
    "formalStatement": "card(A)>card(B) ⇒ ∃a≠a′:f(a)=f(a′)",
    "proofSketch": "If no collision existed, f would inject A into B, contradicting finite cardinality monotonicity.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for PigeonholePrinciple apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/PigeonholePrinciple"
    ],
    "dependsOn": [
      "urn:csabs:axiom/PigeonholePrinciple-finite-counting-context"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
