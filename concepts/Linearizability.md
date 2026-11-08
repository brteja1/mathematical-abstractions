# Linearizability

A concurrent operation history can be completed by appending responses to some pending calls and discarding others so that it is equivalent to a legal sequential history preserving real-time precedence.

**Notation:** ∃legal sequential S: complete(H')≡S and <H⊆<S

**Stable ID:** `urn:csabs:concept/Linearizability`

**Categories:** Concurrency and distributed systems → Ordering and consistency

**Kind:** semantic-model

**Prerequisites:** [Binary relation](Relation.md)

## Backlinks

- [Lock with compatible access modes](Lock.md) — `relatedConcept`

## Interface and scope

**axiomBasis:** Selected presentation: A concurrent operation history can be completed by appending responses to some pending calls and discarding others so that it is equivalent to a legal sequential history preserving real-time precedence. Governing rules: Histories are well-formed per process, with invocation/response matching and a legal sequential object specification. A history is linearizable exactly when a permissible completion admits a legal real-time-preserving sequential ordering.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**verificationObligation:** State the sequential object specification, per-process well-formedness, pending-call completion convention, and real-time order.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-Linearizability-basis-isLinearizable"></a>

### isLinearizable

`urn:csabs:operation/Linearizability-basis-isLinearizable`

**signature:** isLinearizable : History×SequentialSpecification→Prop

**description:** States existence of a legal real-time-preserving linearization after permissible completion.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-Linearizability-history-context"></a>

### history-context

`urn:csabs:axiom/Linearizability-history-context`

**statement:** Histories are well-formed per process, with invocation/response matching and a legal sequential object specification.

**formalStatement:** For each process, responses match the latest pending invocation; events carry process, object, operation, argument, and result identities

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Linearizability-completion"></a>

### completion

`urn:csabs:axiom/Linearizability-completion`

**statement:** A history is linearizable exactly when a permissible completion admits a legal real-time-preserving sequential ordering.

**formalStatement:** Lin(H) iff ∃H′,S: H′ extends H with responses to some pending calls ∧ S legal ∧ S≡complete(H′) ∧ realTime(H) restricted to complete(H′) ⊆ order(S)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-law-Linearizability-core"></a>

### law/Linearizability-core

`urn:csabs:law/Linearizability-core`

**statement:** Linearizability is compositional across independent objects.

**formalStatement:** H linearizable iff each object projection projection(H,o) is linearizable

**reviewStatus:** editorial-summary; not machine-proved

**assumptions:** Use the carrier and semantic convention in the linked concept definition.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [history-context](Linearizability.md#node-urn-csabs-axiom-Linearizability-history-context); [completion](Linearizability.md#node-urn-csabs-axiom-Linearizability-completion)

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-theorem-Linearizability-implies-sc-complete"></a>

### implies-sc-complete

`urn:csabs:theorem/Linearizability-implies-sc-complete`

**statement:** Linearizability implies sequential consistency for completed well-formed histories.

**formalStatement:** Lin(H)⇒SC(H), with H complete and well formed

**proofSketch:** A legal linearization preserves real-time precedence, which includes successive calls within each process; therefore it preserves each process projection.

**assumptions:** The explicit basis, carriers, and side conditions stated for Linearizability apply.

**dependsOn:** [history-context](Linearizability.md#node-urn-csabs-axiom-Linearizability-history-context); [completion](Linearizability.md#node-urn-csabs-axiom-Linearizability-completion)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Concept provenance

- [Herlihy and Wing: Linearizability (1990)](https://cs.brown.edu/~mph/HerlihyW90/p463-herlihy.pdf); sourceRole: reference-for-selected-basis

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/Linearizability",
    "type": "Concept",
    "shortForm": "Linearizability",
    "fullName": "Linearizability",
    "category": [
      "urn:csabs:category/ordering-consistency"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "definition": "A concurrent operation history can be completed by appending responses to some pending calls and discarding others so that it is equivalent to a legal sequential history preserving real-time precedence.",
    "notation": "∃legal sequential S: complete(H')≡S and <H⊆<S",
    "hasOperation": [
      "urn:csabs:operation/Linearizability-basis-isLinearizable"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/Linearizability-history-context",
      "urn:csabs:axiom/Linearizability-completion"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:law/Linearizability-core",
      "urn:csabs:theorem/Linearizability-implies-sc-complete"
    ],
    "requiresConcept": [
      "urn:csabs:concept/Relation"
    ],
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "State the sequential object specification, per-process well-formedness, pending-call completion convention, and real-time order.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: A concurrent operation history can be completed by appending responses to some pending calls and discarding others so that it is equivalent to a legal sequential history preserving real-time precedence. Governing rules: Histories are well-formed per process, with invocation/response matching and a legal sequential object specification. A history is linearizable exactly when a permissible completion admits a legal real-time-preserving sequential ordering.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "source": [
      "urn:csabs:source/herlihy-wing"
    ]
  },
  {
    "id": "urn:csabs:operation/Linearizability-basis-isLinearizable",
    "type": "Operation",
    "name": "isLinearizable",
    "signature": "isLinearizable : History×SequentialSpecification→Prop",
    "description": "States existence of a legal real-time-preserving linearization after permissible completion.",
    "concept": "urn:csabs:concept/Linearizability"
  },
  {
    "id": "urn:csabs:axiom/Linearizability-history-context",
    "type": "Axiom",
    "name": "history-context",
    "statement": "Histories are well-formed per process, with invocation/response matching and a legal sequential object specification.",
    "formalStatement": "For each process, responses match the latest pending invocation; events carry process, object, operation, argument, and result identities",
    "appliesTo": [
      "urn:csabs:concept/Linearizability"
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
    "id": "urn:csabs:axiom/Linearizability-completion",
    "type": "Axiom",
    "name": "completion",
    "statement": "A history is linearizable exactly when a permissible completion admits a legal real-time-preserving sequential ordering.",
    "formalStatement": "Lin(H) iff ∃H′,S: H′ extends H with responses to some pending calls ∧ S legal ∧ S≡complete(H′) ∧ realTime(H) restricted to complete(H′) ⊆ order(S)",
    "appliesTo": [
      "urn:csabs:concept/Linearizability"
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
    "id": "urn:csabs:law/Linearizability-core",
    "type": "Theorem",
    "statement": "Linearizability is compositional across independent objects.",
    "formalStatement": "H linearizable iff each object projection projection(H,o) is linearizable",
    "appliesTo": [
      "urn:csabs:concept/Linearizability"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "assumptions": [
      "Use the carrier and semantic convention in the linked concept definition."
    ],
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/Linearizability-history-context",
      "urn:csabs:axiom/Linearizability-completion"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/Linearizability-implies-sc-complete",
    "type": "Theorem",
    "name": "implies-sc-complete",
    "statement": "Linearizability implies sequential consistency for completed well-formed histories.",
    "formalStatement": "Lin(H)⇒SC(H), with H complete and well formed",
    "proofSketch": "A legal linearization preserves real-time precedence, which includes successive calls within each process; therefore it preserves each process projection.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for Linearizability apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/Linearizability"
    ],
    "dependsOn": [
      "urn:csabs:axiom/Linearizability-history-context",
      "urn:csabs:axiom/Linearizability-completion"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
