# Priority Queue

A finite bag of items with ordered priorities, returning an item of minimal priority; tie choice is unspecified.

**Notation:** Q∈Bag(Item); extractMin ⊆ PQ×PQ×Item; ties unspecified.

**Stable ID:** `urn:csabs:concept/PriorityQueue`

**Categories:** Data structures → Priority collections

**Kind:** Abstract data type

**Prerequisites:** [Multiset](Multiset.md), [Total Order](TotalOrder.md)

## Backlinks

- [Finite complete binary min-heap](BinaryHeap.md) — `requiresConcept`

## Mathematical formulation

PQ(A)=Multiset(A). Given priority p:A→K into a linear order, extractMin(q,q′,x) ⇔ q={x}⊎q′ ∧ ∀y∈q, p(x)≤p(y). Ties are relationally nondeterministic; an empty q has no extraction.

**Lean formulation** (in its source module context):

```lean
abbrev PriorityQueue (A : Type u) := _root_.Multiset A
```

**Source:** [`Catalog.PriorityQueue`](../lean/Catalog/DataStructures.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Multiset A with supplied LinearOrder on priorities; extractMin is a relation removing one minimal occurrence, allowing all ties.

**Limits:** Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Selected presentation: A finite bag of items with ordered priorities, returning an item of minimal priority; tie choice is unspecified. Governing rules: Queue state is a finite bag of items with a total order on their keys. Insertion adds exactly one occurrence. Extraction is a relation if ties are unspecified, defined on all nonempty bags.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**verificationObligation:** Specify tie behavior only if callers rely on stability; a total priority order alone does not order equal-priority items.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

**provenanceStatus:** legacy-source-missing

## Operations

<a id="node-urn-csabs-operation-PriorityQueue-insert"></a>

### insert

`urn:csabs:operation/PriorityQueue-insert`

**signature:** insert : PQ×Item→PQ

**description:** Adds one occurrence of an item.

<a id="node-urn-csabs-operation-PriorityQueue-extractMin"></a>

### extractMin

`urn:csabs:operation/PriorityQueue-extractMin`

**signature:** extractMin ⊆ PQ×PQ×Item; enabled iff the input bag is nonempty

**description:** Relates an input bag to any allowed remainder and minimum-priority item; equal-priority ties may produce multiple results.

<a id="node-urn-csabs-operation-PriorityQueue-basis-empty"></a>

### empty

`urn:csabs:operation/PriorityQueue-basis-empty`

**signature:** empty : PQ

**description:** Returns the empty bag.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-PriorityQueue-bag-model"></a>

### bag-model

`urn:csabs:axiom/PriorityQueue-bag-model`

**statement:** Queue state is a finite bag of items with a total order on their keys.

**formalStatement:** Q∈Bag(Item); key:Item→P; (P,≤) a total order

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-PriorityQueue-insert"></a>

### insert

`urn:csabs:axiom/PriorityQueue-insert`

**statement:** Insertion adds exactly one occurrence.

**formalStatement:** insert(Q,x)=Q⊎{x}

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-PriorityQueue-minimum-removal"></a>

### minimum-removal

`urn:csabs:axiom/PriorityQueue-minimum-removal`

**statement:** Extraction is a relation if ties are unspecified, defined on all nonempty bags.

**formalStatement:** extractMin(Q,Q′,x) iff Q≠empty ∧ count(Q,x)>0 ∧ Q′=Q−{x} ∧ ∀y∈support(Q):key(x)≤key(y)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

<a id="node-urn-csabs-law-PriorityQueue-core"></a>

### law/PriorityQueue-core

`urn:csabs:law/PriorityQueue-core`

**statement:** Extraction removes one item whose priority is no greater than every remaining item's priority.

**formalStatement:** extractMin(Q)=(Q−{x},x), ∀y∈Q: key(x)≤key(y)

**reviewStatus:** editorial-summary; not machine-proved

**assumptions:** Use the carrier and semantic convention in the linked concept definition.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [bag-model](PriorityQueue.md#node-urn-csabs-axiom-PriorityQueue-bag-model); [insert](PriorityQueue.md#node-urn-csabs-axiom-PriorityQueue-insert); [minimum-removal](PriorityQueue.md#node-urn-csabs-axiom-PriorityQueue-minimum-removal)

**provenanceStatus:** legacy-source-missing

## Theorems

<a id="node-urn-csabs-theorem-PriorityQueue-extraction-size"></a>

### extraction-size

`urn:csabs:theorem/PriorityQueue-extraction-size`

**statement:** Any permitted extraction decreases bag cardinality by one.

**formalStatement:** extractMin(Q,Q′,x) ⇒ size(Q′)=size(Q)−1

**proofSketch:** The removal rule subtracts one positive multiplicity and preserves all others.

**assumptions:** The explicit basis, carriers, and side conditions stated for PriorityQueue apply.

**dependsOn:** [bag-model](PriorityQueue.md#node-urn-csabs-axiom-PriorityQueue-bag-model); [insert](PriorityQueue.md#node-urn-csabs-axiom-PriorityQueue-insert); [minimum-removal](PriorityQueue.md#node-urn-csabs-axiom-PriorityQueue-minimum-removal)

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
    "id": "urn:csabs:concept/PriorityQueue",
    "type": "Concept",
    "shortForm": "PriorityQueue",
    "fullName": "Priority Queue",
    "category": [
      "urn:csabs:category/priority-collections"
    ],
    "kind": "urn:csabs:kind/abstract-data-type",
    "definition": "A finite bag of items with ordered priorities, returning an item of minimal priority; tie choice is unspecified.",
    "notation": "Q∈Bag(Item); extractMin ⊆ PQ×PQ×Item; ties unspecified.",
    "hasOperation": [
      "urn:csabs:operation/PriorityQueue-insert",
      "urn:csabs:operation/PriorityQueue-extractMin",
      "urn:csabs:operation/PriorityQueue-basis-empty"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/PriorityQueue-bag-model",
      "urn:csabs:axiom/PriorityQueue-insert",
      "urn:csabs:axiom/PriorityQueue-minimum-removal"
    ],
    "hasLaw": [
      "urn:csabs:law/PriorityQueue-core"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/PriorityQueue-extraction-size"
    ],
    "requiresConcept": [
      "urn:csabs:concept/Multiset",
      "urn:csabs:concept/TotalOrder"
    ],
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Specify tie behavior only if callers rely on stability; a total priority order alone does not order equal-priority items.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: A finite bag of items with ordered priorities, returning an item of minimal priority; tie choice is unspecified. Governing rules: Queue state is a finite bag of items with a total order on their keys. Insertion adds exactly one occurrence. Extraction is a relation if ties are unspecified, defined on all nonempty bags.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "provenanceStatus": "legacy-source-missing",
    "leanFormulation": "abbrev PriorityQueue (A : Type u) := _root_.Multiset A",
    "formulationSource": "urn:csabs:source/local-lean-DataStructures",
    "formulationLocator": "Catalog.PriorityQueue",
    "formulationScope": "model",
    "leanModelMapping": "Multiset A with supplied LinearOrder on priorities; extractMin is a relation removing one minimal occurrence, allowing all ties.",
    "leanModelLimitations": "Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.",
    "mathematicalFormulation": "PQ(A)=Multiset(A). Given priority p:A→K into a linear order, extractMin(q,q′,x) ⇔ q={x}⊎q′ ∧ ∀y∈q, p(x)≤p(y). Ties are relationally nondeterministic; an empty q has no extraction."
  },
  {
    "id": "urn:csabs:operation/PriorityQueue-insert",
    "type": "Operation",
    "name": "insert",
    "signature": "insert : PQ×Item→PQ",
    "description": "Adds one occurrence of an item.",
    "concept": "urn:csabs:concept/PriorityQueue"
  },
  {
    "id": "urn:csabs:operation/PriorityQueue-extractMin",
    "type": "Operation",
    "name": "extractMin",
    "signature": "extractMin ⊆ PQ×PQ×Item; enabled iff the input bag is nonempty",
    "description": "Relates an input bag to any allowed remainder and minimum-priority item; equal-priority ties may produce multiple results.",
    "concept": "urn:csabs:concept/PriorityQueue"
  },
  {
    "id": "urn:csabs:operation/PriorityQueue-basis-empty",
    "type": "Operation",
    "name": "empty",
    "signature": "empty : PQ",
    "description": "Returns the empty bag.",
    "concept": "urn:csabs:concept/PriorityQueue"
  },
  {
    "id": "urn:csabs:axiom/PriorityQueue-bag-model",
    "type": "Axiom",
    "name": "bag-model",
    "statement": "Queue state is a finite bag of items with a total order on their keys.",
    "formalStatement": "Q∈Bag(Item); key:Item→P; (P,≤) a total order",
    "appliesTo": [
      "urn:csabs:concept/PriorityQueue"
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
    "id": "urn:csabs:axiom/PriorityQueue-insert",
    "type": "Axiom",
    "name": "insert",
    "statement": "Insertion adds exactly one occurrence.",
    "formalStatement": "insert(Q,x)=Q⊎{x}",
    "appliesTo": [
      "urn:csabs:concept/PriorityQueue"
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
    "id": "urn:csabs:axiom/PriorityQueue-minimum-removal",
    "type": "Axiom",
    "name": "minimum-removal",
    "statement": "Extraction is a relation if ties are unspecified, defined on all nonempty bags.",
    "formalStatement": "extractMin(Q,Q′,x) iff Q≠empty ∧ count(Q,x)>0 ∧ Q′=Q−{x} ∧ ∀y∈support(Q):key(x)≤key(y)",
    "appliesTo": [
      "urn:csabs:concept/PriorityQueue"
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
    "id": "urn:csabs:law/PriorityQueue-core",
    "type": "Law",
    "statement": "Extraction removes one item whose priority is no greater than every remaining item's priority.",
    "formalStatement": "extractMin(Q)=(Q−{x},x), ∀y∈Q: key(x)≤key(y)",
    "appliesTo": [
      "urn:csabs:concept/PriorityQueue"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "assumptions": [
      "Use the carrier and semantic convention in the linked concept definition."
    ],
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/PriorityQueue-bag-model",
      "urn:csabs:axiom/PriorityQueue-insert",
      "urn:csabs:axiom/PriorityQueue-minimum-removal"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/PriorityQueue-extraction-size",
    "type": "Theorem",
    "name": "extraction-size",
    "statement": "Any permitted extraction decreases bag cardinality by one.",
    "formalStatement": "extractMin(Q,Q′,x) ⇒ size(Q′)=size(Q)−1",
    "proofSketch": "The removal rule subtracts one positive multiplicity and preserves all others.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for PriorityQueue apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/PriorityQueue"
    ],
    "dependsOn": [
      "urn:csabs:axiom/PriorityQueue-bag-model",
      "urn:csabs:axiom/PriorityQueue-insert",
      "urn:csabs:axiom/PriorityQueue-minimum-removal"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
