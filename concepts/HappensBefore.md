# Happens Before

The transitive closure of per-process event order and message send-before-receive edges in the distributed execution model.

**Notation:** → = (processOrder ∪ sendReceive)+

**Stable ID:** `urn:csabs:concept/HappensBefore`

**Categories:** Concurrency and distributed systems → Ordering and consistency

**Kind:** Relation

**Prerequisites:** [Partial Order](PartialOrder.md)

## Backlinks

- [Lock with compatible access modes](Lock.md) — `relatedConcept`

## Interface and scope

**axiomBasis:** Selected presentation: The transitive closure of per-process event order and message send-before-receive edges in the distributed execution model. Governing rules: Happens-before is the least transitive relation containing process and send-receive precedence. The selected execution model has no causal cycles.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**verificationObligation:** Do not infer a happens-before edge solely from scalar timestamp inequality.; Use the strict, irreflexive order convention; its reflexive closure is a non-strict partial order.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-HappensBefore-basis-precedes"></a>

### precedes

`urn:csabs:operation/HappensBefore-basis-precedes`

**signature:** precedes : Event×Event→Prop

**description:** States membership in the strict causal transitive closure.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-HappensBefore-generators"></a>

### generators

`urn:csabs:axiom/HappensBefore-generators`

**statement:** Happens-before is the least transitive relation containing process and send-receive precedence.

**formalStatement:** HB=(ProcessOrder∪SendReceive)+

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-HappensBefore-causal-consistency"></a>

### causal-consistency

`urn:csabs:axiom/HappensBefore-causal-consistency`

**statement:** The selected execution model has no causal cycles.

**formalStatement:** ∀e:¬HB(e,e); each SendReceive edge connects a matched send to its later receive

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

<a id="node-urn-csabs-law-HappensBefore-core"></a>

### law/HappensBefore-core

`urn:csabs:law/HappensBefore-core`

**statement:** A clock satisfying Lamport's clock condition preserves happens-before; the converse need not hold.

**formalStatement:** a→b ⇒ C(a)<C(b)

**reviewStatus:** editorial-summary; not machine-proved

**assumptions:** Execution has acyclic process/send-receive precedence; Clock satisfies the clock condition, e.g. Lamport update discipline

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [generators](HappensBefore.md#node-urn-csabs-axiom-HappensBefore-generators); [causal-consistency](HappensBefore.md#node-urn-csabs-axiom-HappensBefore-causal-consistency)

**provenanceStatus:** legacy-source-missing

## Theorems

<a id="node-urn-csabs-theorem-HappensBefore-transitive"></a>

### transitive

`urn:csabs:theorem/HappensBefore-transitive`

**statement:** Happens-before is transitive.

**formalStatement:** HB(a,b)∧HB(b,c)⇒HB(a,c)

**proofSketch:** Concatenate paths in the transitive closure of its generating edges.

**assumptions:** The explicit basis, carriers, and side conditions stated for HappensBefore apply.

**dependsOn:** [generators](HappensBefore.md#node-urn-csabs-axiom-HappensBefore-generators); [causal-consistency](HappensBefore.md#node-urn-csabs-axiom-HappensBefore-causal-consistency)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Concept provenance

- [Lamport: Time, Clocks, and the Ordering of Events in a Distributed System (1978)](https://lamport.azurewebsites.net/pubs/time-clocks.pdf); sourceRole: primary-paper

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/HappensBefore",
    "type": "Concept",
    "shortForm": "HappensBefore",
    "fullName": "Happens Before",
    "category": [
      "urn:csabs:category/ordering-consistency"
    ],
    "kind": "urn:csabs:kind/relation",
    "definition": "The transitive closure of per-process event order and message send-before-receive edges in the distributed execution model.",
    "notation": "→ = (processOrder ∪ sendReceive)+",
    "hasOperation": [
      "urn:csabs:operation/HappensBefore-basis-precedes"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/HappensBefore-generators",
      "urn:csabs:axiom/HappensBefore-causal-consistency"
    ],
    "hasLaw": [
      "urn:csabs:law/HappensBefore-core"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/HappensBefore-transitive"
    ],
    "requiresConcept": [
      "urn:csabs:concept/PartialOrder"
    ],
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Do not infer a happens-before edge solely from scalar timestamp inequality.",
      "Use the strict, irreflexive order convention; its reflexive closure is a non-strict partial order.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "source": [
      "urn:csabs:source/lamport1978"
    ],
    "axiomBasis": "Selected presentation: The transitive closure of per-process event order and message send-before-receive edges in the distributed execution model. Governing rules: Happens-before is the least transitive relation containing process and send-receive precedence. The selected execution model has no causal cycles.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof"
  },
  {
    "id": "urn:csabs:operation/HappensBefore-basis-precedes",
    "type": "Operation",
    "name": "precedes",
    "signature": "precedes : Event×Event→Prop",
    "description": "States membership in the strict causal transitive closure.",
    "concept": "urn:csabs:concept/HappensBefore"
  },
  {
    "id": "urn:csabs:axiom/HappensBefore-generators",
    "type": "Axiom",
    "name": "generators",
    "statement": "Happens-before is the least transitive relation containing process and send-receive precedence.",
    "formalStatement": "HB=(ProcessOrder∪SendReceive)+",
    "appliesTo": [
      "urn:csabs:concept/HappensBefore"
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
    "id": "urn:csabs:axiom/HappensBefore-causal-consistency",
    "type": "Axiom",
    "name": "causal-consistency",
    "statement": "The selected execution model has no causal cycles.",
    "formalStatement": "∀e:¬HB(e,e); each SendReceive edge connects a matched send to its later receive",
    "appliesTo": [
      "urn:csabs:concept/HappensBefore"
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
    "id": "urn:csabs:law/HappensBefore-core",
    "type": "Law",
    "statement": "A clock satisfying Lamport's clock condition preserves happens-before; the converse need not hold.",
    "formalStatement": "a→b ⇒ C(a)<C(b)",
    "appliesTo": [
      "urn:csabs:concept/HappensBefore"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "assumptions": [
      "Execution has acyclic process/send-receive precedence",
      "Clock satisfies the clock condition, e.g. Lamport update discipline"
    ],
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/HappensBefore-generators",
      "urn:csabs:axiom/HappensBefore-causal-consistency"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/HappensBefore-transitive",
    "type": "Theorem",
    "name": "transitive",
    "statement": "Happens-before is transitive.",
    "formalStatement": "HB(a,b)∧HB(b,c)⇒HB(a,c)",
    "proofSketch": "Concatenate paths in the transitive closure of its generating edges.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for HappensBefore apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/HappensBefore"
    ],
    "dependsOn": [
      "urn:csabs:axiom/HappensBefore-generators",
      "urn:csabs:axiom/HappensBefore-causal-consistency"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
