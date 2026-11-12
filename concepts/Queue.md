# Queue abstract data type

A collection supporting first-in, first-out insertion and removal, with empty behavior specified by the contract.

**Notation:** enqueue : Queue×V→Queue; dequeue : Queue⇀Queue×V; front : Queue⇀V.

**Stable ID:** `urn:csabs:concept/Queue`

**Categories:** Data structures → Sequential collections

**Kind:** Abstract data type

## Mathematical formulation

Queue(A)=A\*. empty=[]; enqueue(q,x)=q++[x]; dequeue(x::q)=some(q,x); dequeue([])=none. The head is the front and equality retains order and multiplicity.

**Lean formulation** (in its source module context):

```lean
abbrev Queue (A : Type u) := List A
```

**Source:** [`Catalog.Queue`](../lean/Catalog/DataStructures.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** List A with front at head; enqueue appends, dequeue removes head; empty returns none.

**Limits:** Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Selected presentation: A collection supporting first-in, first-out insertion and removal, with empty behavior specified by the contract. Governing rules: A queue is a finite sequence ordered from front to back. Front and dequeue remove the earliest remaining item and are undefined on empty.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**verificationObligation:** Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-queue-enqueue"></a>

### enqueue

`urn:csabs:operation/queue-enqueue`

**signature:** enqueue : Queue×V→Queue

**description:** Adds a value at the back of the queue.

<a id="node-urn-csabs-operation-queue-dequeue"></a>

### dequeue

`urn:csabs:operation/queue-dequeue`

**signature:** dequeue : Queue⇀Queue×V

**description:** Removes and returns the front value and resulting queue.

**precondition:** queue is nonempty

<a id="node-urn-csabs-operation-queue-front"></a>

### front

`urn:csabs:operation/queue-front`

**signature:** front : Queue⇀V

**description:** Returns the oldest queued value.

**precondition:** queue is nonempty

<a id="node-urn-csabs-operation-Queue-basis-empty"></a>

### empty

`urn:csabs:operation/Queue-basis-empty`

**signature:** empty : Queue(V)

**description:** Returns the empty sequence model.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-Queue-sequence-model"></a>

### sequence-model

`urn:csabs:axiom/Queue-sequence-model`

**statement:** A queue is a finite sequence ordered from front to back.

**formalStatement:** Queue(V)=Seq(V); empty=[]; enqueue(q,x)=q·[x]

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Queue-observers"></a>

### observers

`urn:csabs:axiom/Queue-observers`

**statement:** Front and dequeue remove the earliest remaining item and are undefined on empty.

**formalStatement:** front(x::s)=x; dequeue(x::s)=(s,x); dom(front)=dom(dequeue)=Queue(V)−{[]}

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

<a id="node-urn-csabs-law-queue-fifo"></a>

### law/queue-fifo

`urn:csabs:law/queue-fifo`

**statement:** Dequeue returns the earliest enqueued value not yet removed.

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [sequence-model](Queue.md#node-urn-csabs-axiom-Queue-sequence-model); [observers](Queue.md#node-urn-csabs-axiom-Queue-observers)

**assumptions:** Use the explicit mathematical bases and typed carriers of the linked concepts.

**formalStatement:** q=[x₀,…,xₙ], n≥0 ⇒ dequeue(q)=([x₁,…,xₙ],x₀); enqueue(q,x)=q·[x]

**provenanceStatus:** legacy-source-missing

## Theorems

<a id="node-urn-csabs-theorem-Queue-enqueue-nonempty"></a>

### enqueue-nonempty

`urn:csabs:theorem/Queue-enqueue-nonempty`

**statement:** Enqueue creates a nonempty queue and increases length by one.

**formalStatement:** len(enqueue(q,x))=len(q)+1

**proofSketch:** Use the sequence-model definition and additivity of concatenation length.

**assumptions:** The explicit basis, carriers, and side conditions stated for Queue apply.

**dependsOn:** [sequence-model](Queue.md#node-urn-csabs-axiom-Queue-sequence-model); [observers](Queue.md#node-urn-csabs-axiom-Queue-observers)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Concept provenance

- [List of data structures (Wikipedia)](https://en.wikipedia.org/wiki/List_of_data_structures); sourceRole: discovery

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/Queue",
    "type": "Concept",
    "shortForm": "Queue",
    "fullName": "Queue abstract data type",
    "category": [
      "urn:csabs:category/sequential-collections"
    ],
    "kind": "urn:csabs:kind/abstract-data-type",
    "definition": "A collection supporting first-in, first-out insertion and removal, with empty behavior specified by the contract.",
    "notation": "enqueue : Queue×V→Queue; dequeue : Queue⇀Queue×V; front : Queue⇀V.",
    "hasOperation": [
      "urn:csabs:operation/queue-enqueue",
      "urn:csabs:operation/queue-dequeue",
      "urn:csabs:operation/queue-front",
      "urn:csabs:operation/Queue-basis-empty"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/Queue-sequence-model",
      "urn:csabs:axiom/Queue-observers"
    ],
    "hasLaw": [
      "urn:csabs:law/queue-fifo"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/Queue-enqueue-nonempty"
    ],
    "source": [
      "urn:csabs:source/wikipedia-data-structures"
    ],
    "coverageStatus": "basis-reviewed",
    "requiresConcept": [],
    "verificationObligation": [
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: A collection supporting first-in, first-out insertion and removal, with empty behavior specified by the contract. Governing rules: A queue is a finite sequence ordered from front to back. Front and dequeue remove the earliest remaining item and are undefined on empty.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "leanFormulation": "abbrev Queue (A : Type u) := List A",
    "formulationSource": "urn:csabs:source/local-lean-DataStructures",
    "formulationLocator": "Catalog.Queue",
    "formulationScope": "model",
    "leanModelMapping": "List A with front at head; enqueue appends, dequeue removes head; empty returns none.",
    "leanModelLimitations": "Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.",
    "mathematicalFormulation": "Queue(A)=A*. empty=[]; enqueue(q,x)=q++[x]; dequeue(x::q)=some(q,x); dequeue([])=none. The head is the front and equality retains order and multiplicity."
  },
  {
    "id": "urn:csabs:operation/queue-enqueue",
    "type": "Operation",
    "name": "enqueue",
    "signature": "enqueue : Queue×V→Queue",
    "description": "Adds a value at the back of the queue.",
    "concept": "urn:csabs:concept/Queue"
  },
  {
    "id": "urn:csabs:operation/queue-dequeue",
    "type": "Operation",
    "name": "dequeue",
    "signature": "dequeue : Queue⇀Queue×V",
    "description": "Removes and returns the front value and resulting queue.",
    "precondition": "queue is nonempty",
    "concept": "urn:csabs:concept/Queue"
  },
  {
    "id": "urn:csabs:operation/queue-front",
    "type": "Operation",
    "name": "front",
    "signature": "front : Queue⇀V",
    "description": "Returns the oldest queued value.",
    "precondition": "queue is nonempty",
    "concept": "urn:csabs:concept/Queue"
  },
  {
    "id": "urn:csabs:operation/Queue-basis-empty",
    "type": "Operation",
    "name": "empty",
    "signature": "empty : Queue(V)",
    "description": "Returns the empty sequence model.",
    "concept": "urn:csabs:concept/Queue"
  },
  {
    "id": "urn:csabs:axiom/Queue-sequence-model",
    "type": "Axiom",
    "name": "sequence-model",
    "statement": "A queue is a finite sequence ordered from front to back.",
    "formalStatement": "Queue(V)=Seq(V); empty=[]; enqueue(q,x)=q·[x]",
    "appliesTo": [
      "urn:csabs:concept/Queue"
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
    "id": "urn:csabs:axiom/Queue-observers",
    "type": "Axiom",
    "name": "observers",
    "statement": "Front and dequeue remove the earliest remaining item and are undefined on empty.",
    "formalStatement": "front(x::s)=x; dequeue(x::s)=(s,x); dom(front)=dom(dequeue)=Queue(V)−{[]}",
    "appliesTo": [
      "urn:csabs:concept/Queue"
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
    "id": "urn:csabs:law/queue-fifo",
    "type": "Law",
    "statement": "Dequeue returns the earliest enqueued value not yet removed.",
    "appliesTo": [
      "urn:csabs:concept/Queue"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/Queue-sequence-model",
      "urn:csabs:axiom/Queue-observers"
    ],
    "assumptions": [
      "Use the explicit mathematical bases and typed carriers of the linked concepts."
    ],
    "formalStatement": "q=[x₀,…,xₙ], n≥0 ⇒ dequeue(q)=([x₁,…,xₙ],x₀); enqueue(q,x)=q·[x]",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/Queue-enqueue-nonempty",
    "type": "Theorem",
    "name": "enqueue-nonempty",
    "statement": "Enqueue creates a nonempty queue and increases length by one.",
    "formalStatement": "len(enqueue(q,x))=len(q)+1",
    "proofSketch": "Use the sequence-model definition and additivity of concatenation length.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for Queue apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/Queue"
    ],
    "dependsOn": [
      "urn:csabs:axiom/Queue-sequence-model",
      "urn:csabs:axiom/Queue-observers"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
