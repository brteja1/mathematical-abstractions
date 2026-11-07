# Finite sequence

An ordered finite collection in which repeated values are allowed.

**Notation:** s : {0,…,n−1} → V with length n; concatenation s·t.

**Stable ID:** `urn:csabs:concept/Sequence`

**Categories:** Data structures

**Kind:** Abstract data type

**Related concepts:** [Ordered collection without duplicates](OrderedSet.md), [Formal language of finite words](FormalLanguage.md)

## Backlinks

- [Fixed-length array](Array.md) — `relatedConcept`
- [Finite complete binary min-heap](BinaryHeap.md) — `requiresConcept`
- [Finite ordered binary tree with node labels](BinaryTree.md) — `requiresConcept`
- [Deque](Deque.md) — `requiresConcept`
- [Finite directed multigraph with edge identities](DirectedMultigraph.md) — `requiresConcept`
- [Finite JSON document value (interoperable profile)](DocumentValue.md) — `requiresConcept`
- [Finite fused sequence iterator](FiniteIterator.md) — `requiresConcept`
- [Finite set collection](FiniteSet.md) — `relatedConcept`
- [Formal language of finite words](FormalLanguage.md) — `requiresConcept`
- [Action-labelled transition system with initial states](LabelledTransitionSystem.md) — `requiresConcept`
- [Ordered collection without duplicates](OrderedSet.md) — `requiresConcept`
- [Finite labelled property graph (single-valued profile)](PropertyGraph.md) — `requiresConcept`
- [Finite ordered rose tree](RoseTree.md) — `requiresConcept`
- [Infinite discrete stream](Stream.md) — `requiresConcept`
- [Finite prefix dictionary](Trie.md) — `requiresConcept`

## Interface and scope

**axiomBasis:** Selected presentation: An ordered finite collection in which repeated values are allowed. Governing rules: Finite sequences consist exactly of empty or a value followed by a finite sequence. Predicates holding for nil and preserved by cons hold for every finite sequence. Concatenation is defined by recursion on the left argument. Length counts constructors.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**verificationObligation:** Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-sequence-concatenation"></a>

### concatenation

`urn:csabs:operation/sequence-concatenation`

**signature:** · : Seq(V)×Seq(V)→Seq(V)

**description:** Appends the second finite sequence after the first.

<a id="node-urn-csabs-operation-sequence-length"></a>

### length

`urn:csabs:operation/sequence-length`

**signature:** len : Seq(V)→ℕ

**description:** Returns the number of elements.

<a id="node-urn-csabs-operation-sequence-index"></a>

### index

`urn:csabs:operation/sequence-index`

**signature:** get : Seq(V)×ℕ ⇀ V; defined iff 0≤i<len(s)

**description:** Returns the value at a valid sequence index.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-Sequence-constructors"></a>

### constructors

`urn:csabs:axiom/Sequence-constructors`

**statement:** Finite sequences consist exactly of empty or a value followed by a finite sequence.

**formalStatement:** Seq(V)=μX.(1+V×X); nil≠cons(x,s); cons(x,s)=cons(y,t) iff x=y ∧ s=t

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Sequence-induction"></a>

### induction

`urn:csabs:axiom/Sequence-induction`

**statement:** Predicates holding for nil and preserved by cons hold for every finite sequence.

**formalStatement:** P(nil) ∧ (∀x,s:P(s)⇒P(cons(x,s))) ⇒ ∀s∈Seq(V):P(s)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Sequence-concat-recursion"></a>

### concat-recursion

`urn:csabs:axiom/Sequence-concat-recursion`

**statement:** Concatenation is defined by recursion on the left argument.

**formalStatement:** nil·t=t; cons(x,s)·t=cons(x,s·t)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Sequence-length-recursion"></a>

### length-recursion

`urn:csabs:axiom/Sequence-length-recursion`

**statement:** Length counts constructors.

**formalStatement:** len(nil)=0; len(cons(x,s))=1+len(s)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

<a id="node-urn-csabs-law-sequence-concat-associative"></a>

### law/sequence-concat-associative

`urn:csabs:law/sequence-concat-associative`

**statement:** Sequence concatenation is associative.

**formalStatement:** (s·t)·u=s·(t·u)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [constructors](Sequence.md#node-urn-csabs-axiom-Sequence-constructors); [induction](Sequence.md#node-urn-csabs-axiom-Sequence-induction); [concat-recursion](Sequence.md#node-urn-csabs-axiom-Sequence-concat-recursion); [length-recursion](Sequence.md#node-urn-csabs-axiom-Sequence-length-recursion)

**assumptions:** Use the explicit mathematical bases and typed carriers of the linked concepts.

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-law-sequence-empty-identity"></a>

### law/sequence-empty-identity

`urn:csabs:law/sequence-empty-identity`

**statement:** The empty sequence is an identity for concatenation.

**formalStatement:** ε·s=s=s·ε

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [constructors](Sequence.md#node-urn-csabs-axiom-Sequence-constructors); [induction](Sequence.md#node-urn-csabs-axiom-Sequence-induction); [concat-recursion](Sequence.md#node-urn-csabs-axiom-Sequence-concat-recursion); [length-recursion](Sequence.md#node-urn-csabs-axiom-Sequence-length-recursion)

**assumptions:** Use the explicit mathematical bases and typed carriers of the linked concepts.

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-law-sequence-length-concat"></a>

### law/sequence-length-concat

`urn:csabs:law/sequence-length-concat`

**statement:** Length is additive under finite concatenation.

**formalStatement:** len(s·t)=len(s)+len(t)

**assumptions:** Finite sequences

**reviewStatus:** editorial-summary; not machine-proved

**dependsOn:** [constructors](Sequence.md#node-urn-csabs-axiom-Sequence-constructors); [induction](Sequence.md#node-urn-csabs-axiom-Sequence-induction); [concat-recursion](Sequence.md#node-urn-csabs-axiom-Sequence-concat-recursion); [length-recursion](Sequence.md#node-urn-csabs-axiom-Sequence-length-recursion)

**provenanceStatus:** legacy-source-missing

## Theorems

<a id="node-urn-csabs-theorem-Sequence-concat-right-identity"></a>

### concat-right-identity

`urn:csabs:theorem/Sequence-concat-right-identity`

**statement:** Appending the empty sequence preserves a finite sequence.

**formalStatement:** s·nil=s

**proofSketch:** Induct on s; the defining concatenation equations give the base and step.

**assumptions:** The explicit basis, carriers, and side conditions stated for Sequence apply.

**dependsOn:** [constructors](Sequence.md#node-urn-csabs-axiom-Sequence-constructors); [induction](Sequence.md#node-urn-csabs-axiom-Sequence-induction); [concat-recursion](Sequence.md#node-urn-csabs-axiom-Sequence-concat-recursion); [length-recursion](Sequence.md#node-urn-csabs-axiom-Sequence-length-recursion)

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
    "id": "urn:csabs:concept/Sequence",
    "type": "Concept",
    "shortForm": "Sequence",
    "fullName": "Finite sequence",
    "category": [
      "urn:csabs:category/data-structures"
    ],
    "kind": "urn:csabs:kind/abstract-data-type",
    "definition": "An ordered finite collection in which repeated values are allowed.",
    "notation": "s : {0,…,n−1} → V with length n; concatenation s·t.",
    "hasOperation": [
      "urn:csabs:operation/sequence-concatenation",
      "urn:csabs:operation/sequence-length",
      "urn:csabs:operation/sequence-index"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/Sequence-constructors",
      "urn:csabs:axiom/Sequence-induction",
      "urn:csabs:axiom/Sequence-concat-recursion",
      "urn:csabs:axiom/Sequence-length-recursion"
    ],
    "hasLaw": [
      "urn:csabs:law/sequence-concat-associative",
      "urn:csabs:law/sequence-empty-identity",
      "urn:csabs:law/sequence-length-concat"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/Sequence-concat-right-identity"
    ],
    "source": [
      "urn:csabs:source/wikipedia-data-structures"
    ],
    "coverageStatus": "basis-reviewed",
    "requiresConcept": [],
    "verificationObligation": [
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: An ordered finite collection in which repeated values are allowed. Governing rules: Finite sequences consist exactly of empty or a value followed by a finite sequence. Predicates holding for nil and preserved by cons hold for every finite sequence. Concatenation is defined by recursion on the left argument. Length counts constructors.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "relatedConcept": [
      "urn:csabs:concept/OrderedSet",
      "urn:csabs:concept/FormalLanguage"
    ]
  },
  {
    "id": "urn:csabs:operation/sequence-concatenation",
    "type": "Operation",
    "name": "concatenation",
    "signature": "· : Seq(V)×Seq(V)→Seq(V)",
    "description": "Appends the second finite sequence after the first.",
    "concept": "urn:csabs:concept/Sequence"
  },
  {
    "id": "urn:csabs:operation/sequence-length",
    "type": "Operation",
    "name": "length",
    "signature": "len : Seq(V)→ℕ",
    "description": "Returns the number of elements.",
    "concept": "urn:csabs:concept/Sequence"
  },
  {
    "id": "urn:csabs:operation/sequence-index",
    "type": "Operation",
    "name": "index",
    "signature": "get : Seq(V)×ℕ ⇀ V; defined iff 0≤i<len(s)",
    "description": "Returns the value at a valid sequence index.",
    "concept": "urn:csabs:concept/Sequence"
  },
  {
    "id": "urn:csabs:axiom/Sequence-constructors",
    "type": "Axiom",
    "name": "constructors",
    "statement": "Finite sequences consist exactly of empty or a value followed by a finite sequence.",
    "formalStatement": "Seq(V)=μX.(1+V×X); nil≠cons(x,s); cons(x,s)=cons(y,t) iff x=y ∧ s=t",
    "appliesTo": [
      "urn:csabs:concept/Sequence"
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
    "id": "urn:csabs:axiom/Sequence-induction",
    "type": "Axiom",
    "name": "induction",
    "statement": "Predicates holding for nil and preserved by cons hold for every finite sequence.",
    "formalStatement": "P(nil) ∧ (∀x,s:P(s)⇒P(cons(x,s))) ⇒ ∀s∈Seq(V):P(s)",
    "appliesTo": [
      "urn:csabs:concept/Sequence"
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
    "id": "urn:csabs:axiom/Sequence-concat-recursion",
    "type": "Axiom",
    "name": "concat-recursion",
    "statement": "Concatenation is defined by recursion on the left argument.",
    "formalStatement": "nil·t=t; cons(x,s)·t=cons(x,s·t)",
    "appliesTo": [
      "urn:csabs:concept/Sequence"
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
    "id": "urn:csabs:axiom/Sequence-length-recursion",
    "type": "Axiom",
    "name": "length-recursion",
    "statement": "Length counts constructors.",
    "formalStatement": "len(nil)=0; len(cons(x,s))=1+len(s)",
    "appliesTo": [
      "urn:csabs:concept/Sequence"
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
    "id": "urn:csabs:law/sequence-concat-associative",
    "type": "Law",
    "statement": "Sequence concatenation is associative.",
    "formalStatement": "(s·t)·u=s·(t·u)",
    "appliesTo": [
      "urn:csabs:concept/Sequence"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/Sequence-constructors",
      "urn:csabs:axiom/Sequence-induction",
      "urn:csabs:axiom/Sequence-concat-recursion",
      "urn:csabs:axiom/Sequence-length-recursion"
    ],
    "assumptions": [
      "Use the explicit mathematical bases and typed carriers of the linked concepts."
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:law/sequence-empty-identity",
    "type": "Law",
    "statement": "The empty sequence is an identity for concatenation.",
    "formalStatement": "ε·s=s=s·ε",
    "appliesTo": [
      "urn:csabs:concept/Sequence"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/Sequence-constructors",
      "urn:csabs:axiom/Sequence-induction",
      "urn:csabs:axiom/Sequence-concat-recursion",
      "urn:csabs:axiom/Sequence-length-recursion"
    ],
    "assumptions": [
      "Use the explicit mathematical bases and typed carriers of the linked concepts."
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:law/sequence-length-concat",
    "type": "Law",
    "statement": "Length is additive under finite concatenation.",
    "formalStatement": "len(s·t)=len(s)+len(t)",
    "assumptions": [
      "Finite sequences"
    ],
    "appliesTo": [
      "urn:csabs:concept/Sequence"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "dependsOn": [
      "urn:csabs:axiom/Sequence-constructors",
      "urn:csabs:axiom/Sequence-induction",
      "urn:csabs:axiom/Sequence-concat-recursion",
      "urn:csabs:axiom/Sequence-length-recursion"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/Sequence-concat-right-identity",
    "type": "Theorem",
    "name": "concat-right-identity",
    "statement": "Appending the empty sequence preserves a finite sequence.",
    "formalStatement": "s·nil=s",
    "proofSketch": "Induct on s; the defining concatenation equations give the base and step.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for Sequence apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/Sequence"
    ],
    "dependsOn": [
      "urn:csabs:axiom/Sequence-constructors",
      "urn:csabs:axiom/Sequence-induction",
      "urn:csabs:axiom/Sequence-concat-recursion",
      "urn:csabs:axiom/Sequence-length-recursion"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
