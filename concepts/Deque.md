# Deque

A finite sequence allowing insertion and removal at both ends, with explicit empty behavior.

**Notation:** Deque(V) ≅ Seq(V)

**Stable ID:** `urn:csabs:concept/Deque`

**Categories:** Data structures → Sequential collections

**Kind:** Abstract data type

**Prerequisites:** [Finite sequence (List datatype)](Sequence.md)

## Interface and scope

**axiomBasis:** Selected presentation: A finite sequence allowing insertion and removal at both ends, with explicit empty behavior. Governing rules: A deque is a finite sequence and empty deque is empty sequence. Front and back insertions prepend and append. Removals return the matching endpoint and leave the other values in order.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**verificationObligation:** Instantiate carrier, equality, and stated semantic conventions before using this entry.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

**provenanceStatus:** legacy-source-missing

## Operations

<a id="node-urn-csabs-operation-Deque-pushFront"></a>

### pushFront

`urn:csabs:operation/Deque-pushFront`

**signature:** pushFront : Deque(V)×V→Deque(V)

**description:** Adds at the front.

<a id="node-urn-csabs-operation-Deque-pushBack"></a>

### pushBack

`urn:csabs:operation/Deque-pushBack`

**signature:** pushBack : Deque(V)×V→Deque(V)

**description:** Adds at the back.

<a id="node-urn-csabs-operation-Deque-popFront"></a>

### popFront

`urn:csabs:operation/Deque-popFront`

**signature:** popFront : Deque(V)⇀Deque(V)×V

**description:** Removes the front; defined only for nonempty deques.

<a id="node-urn-csabs-operation-Deque-popBack"></a>

### popBack

`urn:csabs:operation/Deque-popBack`

**signature:** popBack : Deque(V)⇀Deque(V)×V

**description:** Removes the back; defined only for nonempty deques.

<a id="node-urn-csabs-operation-Deque-basis-empty"></a>

### empty

`urn:csabs:operation/Deque-basis-empty`

**signature:** empty : Deque(V)

**description:** Returns the empty deque.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-Deque-sequence-model"></a>

### sequence-model

`urn:csabs:axiom/Deque-sequence-model`

**statement:** A deque is a finite sequence and empty deque is empty sequence.

**formalStatement:** Deque(V)=Seq(V); empty=[]

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Deque-insert"></a>

### insert

`urn:csabs:axiom/Deque-insert`

**statement:** Front and back insertions prepend and append.

**formalStatement:** pushFront(d,x)=[x]·d; pushBack(d,x)=d·[x]

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Deque-remove"></a>

### remove

`urn:csabs:axiom/Deque-remove`

**statement:** Removals return the matching endpoint and leave the other values in order.

**formalStatement:** popFront([x]·d)=(d,x); popBack(d·[x])=(d,x); both removals undefined exactly on []

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

<a id="node-urn-csabs-law-Deque-core"></a>

### law/Deque-core

`urn:csabs:law/Deque-core`

**statement:** Removing from the front immediately after adding there recovers the prior deque and added value.

**formalStatement:** popFront(pushFront(d,x))=(d,x)

**reviewStatus:** editorial-summary; not machine-proved

**assumptions:** Use the carrier and semantic convention in the linked concept definition.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [sequence-model](Deque.md#node-urn-csabs-axiom-Deque-sequence-model); [insert](Deque.md#node-urn-csabs-axiom-Deque-insert); [remove](Deque.md#node-urn-csabs-axiom-Deque-remove)

**provenanceStatus:** legacy-source-missing

## Theorems

<a id="node-urn-csabs-theorem-Deque-front-roundtrip"></a>

### front-roundtrip

`urn:csabs:theorem/Deque-front-roundtrip`

**statement:** A front insertion followed by a front removal restores the prior deque.

**formalStatement:** popFront(pushFront(d,x))=(d,x)

**proofSketch:** Substitute the sequence-model insertion into the endpoint removal rule.

**assumptions:** The explicit basis, carriers, and side conditions stated for Deque apply.

**dependsOn:** [sequence-model](Deque.md#node-urn-csabs-axiom-Deque-sequence-model); [insert](Deque.md#node-urn-csabs-axiom-Deque-insert); [remove](Deque.md#node-urn-csabs-axiom-Deque-remove)

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
    "id": "urn:csabs:concept/Deque",
    "type": "Concept",
    "shortForm": "Deque",
    "fullName": "Deque",
    "category": [
      "urn:csabs:category/sequential-collections"
    ],
    "kind": "urn:csabs:kind/abstract-data-type",
    "definition": "A finite sequence allowing insertion and removal at both ends, with explicit empty behavior.",
    "notation": "Deque(V) ≅ Seq(V)",
    "hasOperation": [
      "urn:csabs:operation/Deque-pushFront",
      "urn:csabs:operation/Deque-pushBack",
      "urn:csabs:operation/Deque-popFront",
      "urn:csabs:operation/Deque-popBack",
      "urn:csabs:operation/Deque-basis-empty"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/Deque-sequence-model",
      "urn:csabs:axiom/Deque-insert",
      "urn:csabs:axiom/Deque-remove"
    ],
    "hasLaw": [
      "urn:csabs:law/Deque-core"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/Deque-front-roundtrip"
    ],
    "requiresConcept": [
      "urn:csabs:concept/Sequence"
    ],
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Instantiate carrier, equality, and stated semantic conventions before using this entry.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: A finite sequence allowing insertion and removal at both ends, with explicit empty behavior. Governing rules: A deque is a finite sequence and empty deque is empty sequence. Front and back insertions prepend and append. Removals return the matching endpoint and leave the other values in order.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:operation/Deque-pushFront",
    "type": "Operation",
    "name": "pushFront",
    "signature": "pushFront : Deque(V)×V→Deque(V)",
    "description": "Adds at the front.",
    "concept": "urn:csabs:concept/Deque"
  },
  {
    "id": "urn:csabs:operation/Deque-pushBack",
    "type": "Operation",
    "name": "pushBack",
    "signature": "pushBack : Deque(V)×V→Deque(V)",
    "description": "Adds at the back.",
    "concept": "urn:csabs:concept/Deque"
  },
  {
    "id": "urn:csabs:operation/Deque-popFront",
    "type": "Operation",
    "name": "popFront",
    "signature": "popFront : Deque(V)⇀Deque(V)×V",
    "description": "Removes the front; defined only for nonempty deques.",
    "concept": "urn:csabs:concept/Deque"
  },
  {
    "id": "urn:csabs:operation/Deque-popBack",
    "type": "Operation",
    "name": "popBack",
    "signature": "popBack : Deque(V)⇀Deque(V)×V",
    "description": "Removes the back; defined only for nonempty deques.",
    "concept": "urn:csabs:concept/Deque"
  },
  {
    "id": "urn:csabs:operation/Deque-basis-empty",
    "type": "Operation",
    "name": "empty",
    "signature": "empty : Deque(V)",
    "description": "Returns the empty deque.",
    "concept": "urn:csabs:concept/Deque"
  },
  {
    "id": "urn:csabs:axiom/Deque-sequence-model",
    "type": "Axiom",
    "name": "sequence-model",
    "statement": "A deque is a finite sequence and empty deque is empty sequence.",
    "formalStatement": "Deque(V)=Seq(V); empty=[]",
    "appliesTo": [
      "urn:csabs:concept/Deque"
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
    "id": "urn:csabs:axiom/Deque-insert",
    "type": "Axiom",
    "name": "insert",
    "statement": "Front and back insertions prepend and append.",
    "formalStatement": "pushFront(d,x)=[x]·d; pushBack(d,x)=d·[x]",
    "appliesTo": [
      "urn:csabs:concept/Deque"
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
    "id": "urn:csabs:axiom/Deque-remove",
    "type": "Axiom",
    "name": "remove",
    "statement": "Removals return the matching endpoint and leave the other values in order.",
    "formalStatement": "popFront([x]·d)=(d,x); popBack(d·[x])=(d,x); both removals undefined exactly on []",
    "appliesTo": [
      "urn:csabs:concept/Deque"
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
    "id": "urn:csabs:law/Deque-core",
    "type": "Law",
    "statement": "Removing from the front immediately after adding there recovers the prior deque and added value.",
    "formalStatement": "popFront(pushFront(d,x))=(d,x)",
    "appliesTo": [
      "urn:csabs:concept/Deque"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "assumptions": [
      "Use the carrier and semantic convention in the linked concept definition."
    ],
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/Deque-sequence-model",
      "urn:csabs:axiom/Deque-insert",
      "urn:csabs:axiom/Deque-remove"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/Deque-front-roundtrip",
    "type": "Theorem",
    "name": "front-roundtrip",
    "statement": "A front insertion followed by a front removal restores the prior deque.",
    "formalStatement": "popFront(pushFront(d,x))=(d,x)",
    "proofSketch": "Substitute the sequence-model insertion into the endpoint removal rule.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for Deque apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/Deque"
    ],
    "dependsOn": [
      "urn:csabs:axiom/Deque-sequence-model",
      "urn:csabs:axiom/Deque-insert",
      "urn:csabs:axiom/Deque-remove"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
