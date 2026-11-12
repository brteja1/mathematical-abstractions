# Sequential Consistency

A completed well-formed concurrent history is sequentially consistent when a legal sequential history preserves each process’s projection. Pending calls require a separate completion convention.

**Notation:** ∃legal S: S≡H and each process order is preserved

**Stable ID:** `urn:csabs:concept/SequentialConsistency`

**Categories:** Concurrency and distributed systems → Ordering and consistency

**Kind:** semantic-model

**Prerequisites:** [Binary relation](Relation.md)

## Backlinks

- [Lamport bakery lock protocol](LamportBakery.md) — `relatedConcept`

## Mathematical formulation

For an instantiated history model, SC(h) ⇔ wellFormed(h)∧completed(h)∧∃s,legal(s)∧equivalent(h,s)∧processOrderPreserved(h,s). Legality, projection equality and process order are supplied predicates.

**Lean formulation** (in its source module context):

```lean
def SequentialConsistency {H S : Type u} (m : HistoryModel H S) (h : H) : Prop :=
  m.wellFormed h ∧ m.completed h ∧ ∃ s,
    m.legal s ∧ m.equivalent h s ∧ m.processOrderPreserved h s
```

**Source:** [`Catalog.SequentialConsistency`](../lean/Catalog/Semantics.lean); consulted 2026-11-12.

**Scope:** partial

**Interpretation:** Completed well-formed history admitting a legal sequential witness with equivalent process projections.

**Limits:** Process projection and legality predicates are abstract client parameters, not an event-level history construction.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Selected presentation: A concurrent history is equivalent to a legal sequential history preserving each process's program order. Governing rules: This entry concerns completed well-formed histories and requires a legal sequential witness preserving process projections.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**verificationObligation:** Instantiate carrier, equality, and stated semantic conventions before using this entry.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

**provenanceStatus:** legacy-source-missing

## Operations

<a id="node-urn-csabs-operation-SequentialConsistency-basis-isSequentiallyConsistent"></a>

### isSequentiallyConsistent

`urn:csabs:operation/SequentialConsistency-basis-isSequentiallyConsistent`

**signature:** isSequentiallyConsistent : CompleteHistory×SequentialSpecification→Prop

**description:** States existence of a legal per-process-order-preserving sequential history.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-SequentialConsistency-sequential-witness"></a>

### sequential-witness

`urn:csabs:axiom/SequentialConsistency-sequential-witness`

**statement:** This entry concerns completed well-formed histories and requires a legal sequential witness preserving process projections.

**formalStatement:** SC(H) iff ∃legal sequential S:∀process p:projection(S,p)=projection(H,p)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

<a id="node-urn-csabs-law-SequentialConsistency-core"></a>

### law/SequentialConsistency-core

`urn:csabs:law/SequentialConsistency-core`

**statement:** Real-time precedence is not required by sequential consistency.

**formalStatement:** Different processes may be reordered subject to program order and legality

**reviewStatus:** editorial-summary; not machine-proved

**assumptions:** Use the carrier and semantic convention in the linked concept definition.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [sequential-witness](SequentialConsistency.md#node-urn-csabs-axiom-SequentialConsistency-sequential-witness)

**provenanceStatus:** legacy-source-missing

## Theorems

<a id="node-urn-csabs-theorem-SequentialConsistency-process-projection"></a>

### process-projection

`urn:csabs:theorem/SequentialConsistency-process-projection`

**statement:** A sequential-consistency witness preserves each process's ordered operations and results.

**formalStatement:** SC(H) with witness S ⇒ projection(S,p)=projection(H,p)

**proofSketch:** This follows directly from the witness condition; other processes may be interleaved differently.

**assumptions:** The explicit basis, carriers, and side conditions stated for SequentialConsistency apply.

**dependsOn:** [sequential-witness](SequentialConsistency.md#node-urn-csabs-axiom-SequentialConsistency-sequential-witness)

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
    "id": "urn:csabs:concept/SequentialConsistency",
    "type": "Concept",
    "shortForm": "SequentialConsistency",
    "fullName": "Sequential Consistency",
    "category": [
      "urn:csabs:category/ordering-consistency"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "definition": "A completed well-formed concurrent history is sequentially consistent when a legal sequential history preserves each process’s projection. Pending calls require a separate completion convention.",
    "notation": "∃legal S: S≡H and each process order is preserved",
    "hasOperation": [
      "urn:csabs:operation/SequentialConsistency-basis-isSequentiallyConsistent"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/SequentialConsistency-sequential-witness"
    ],
    "hasLaw": [
      "urn:csabs:law/SequentialConsistency-core"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/SequentialConsistency-process-projection"
    ],
    "requiresConcept": [
      "urn:csabs:concept/Relation"
    ],
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Instantiate carrier, equality, and stated semantic conventions before using this entry.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: A concurrent history is equivalent to a legal sequential history preserving each process's program order. Governing rules: This entry concerns completed well-formed histories and requires a legal sequential witness preserving process projections.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "provenanceStatus": "legacy-source-missing",
    "leanFormulation": "def SequentialConsistency {H S : Type u} (m : HistoryModel H S) (h : H) : Prop :=\n  m.wellFormed h ∧ m.completed h ∧ ∃ s,\n    m.legal s ∧ m.equivalent h s ∧ m.processOrderPreserved h s",
    "formulationSource": "urn:csabs:source/local-lean-Semantics",
    "formulationLocator": "Catalog.SequentialConsistency",
    "formulationScope": "partial",
    "leanModelMapping": "Completed well-formed history admitting a legal sequential witness with equivalent process projections.",
    "leanModelLimitations": "Process projection and legality predicates are abstract client parameters, not an event-level history construction.",
    "mathematicalFormulation": "For an instantiated history model, SC(h) ⇔ wellFormed(h)∧completed(h)∧∃s,legal(s)∧equivalent(h,s)∧processOrderPreserved(h,s). Legality, projection equality and process order are supplied predicates."
  },
  {
    "id": "urn:csabs:operation/SequentialConsistency-basis-isSequentiallyConsistent",
    "type": "Operation",
    "name": "isSequentiallyConsistent",
    "signature": "isSequentiallyConsistent : CompleteHistory×SequentialSpecification→Prop",
    "description": "States existence of a legal per-process-order-preserving sequential history.",
    "concept": "urn:csabs:concept/SequentialConsistency"
  },
  {
    "id": "urn:csabs:axiom/SequentialConsistency-sequential-witness",
    "type": "Axiom",
    "name": "sequential-witness",
    "statement": "This entry concerns completed well-formed histories and requires a legal sequential witness preserving process projections.",
    "formalStatement": "SC(H) iff ∃legal sequential S:∀process p:projection(S,p)=projection(H,p)",
    "appliesTo": [
      "urn:csabs:concept/SequentialConsistency"
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
    "id": "urn:csabs:law/SequentialConsistency-core",
    "type": "Law",
    "statement": "Real-time precedence is not required by sequential consistency.",
    "formalStatement": "Different processes may be reordered subject to program order and legality",
    "appliesTo": [
      "urn:csabs:concept/SequentialConsistency"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "assumptions": [
      "Use the carrier and semantic convention in the linked concept definition."
    ],
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/SequentialConsistency-sequential-witness"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/SequentialConsistency-process-projection",
    "type": "Theorem",
    "name": "process-projection",
    "statement": "A sequential-consistency witness preserves each process's ordered operations and results.",
    "formalStatement": "SC(H) with witness S ⇒ projection(S,p)=projection(H,p)",
    "proofSketch": "This follows directly from the witness condition; other processes may be interleaved differently.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for SequentialConsistency apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/SequentialConsistency"
    ],
    "dependsOn": [
      "urn:csabs:axiom/SequentialConsistency-sequential-witness"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
