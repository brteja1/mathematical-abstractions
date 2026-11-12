# Finite complete binary min-heap

A finite level-order sequence with complete binary-tree shape and parent priority at most child priority.

**Notation:** H_p(A)={xs∈Seq(A) | ∀0<i<|xs|, p(xs[⌊(i-1)/2⌋])≤p(xs[i])}

**Stable ID:** `urn:csabs:concept/BinaryHeap`

**Categories:** Data structures → Tree structures, Data structures → Priority collections

**Kind:** Abstract data type

**Prerequisites:** [Finite sequence (List datatype)](Sequence.md), [Priority Queue](PriorityQueue.md), [Total Order](TotalOrder.md)

**Related concepts:** [Finite ordered binary tree with node labels](BinaryTree.md)

## Mathematical formulation

A min-heap is a finite sequence xs with ∀i,0<i<|xs|⇒p(xs[⌊(i−1)/2⌋])≤p(xs[i]), where p:A→K and K is linearly ordered. Array indices impose complete binary shape; equal priorities are allowed.

**Lean formulation** (in its source module context):

```lean
structure BinaryHeap (A : Type u) (K : Type v) [LinearOrder K] (priority : A → K) where
  items : List A
  ordered : ∀ (i : Fin items.length), 0 < i.val →
    priority (items.get ⟨(i.val - 1) / 2, by have := i.isLt; omega⟩) ≤ priority (items.get i)
```

**Source:** [`Catalog.BinaryHeap`](../lean/Catalog/StructuredData.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** H_p(A)={xs∈Seq(A) | ∀0<i<|xs|, p(xs[⌊(i-1)/2⌋])≤p(xs[i])}. Fixed p:A→K into a linear order. Empty allowed, duplicate values/priorities allowed, ties unspecified. Equality retains level-order sequence. No capacity/overflow bound, stable tie order, or algorithm complexity promised.

**Limits:** Compiled carrier and selected interface interpretation. Some catalog operations are specified mathematically rather than wrapped as Lean declarations; no blanket proof of claims, algorithms, parsing, liveness or complexity. See individual witnesses.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Nodes are indices 0,…,n-1; parent(i)=⌊(i-1)/2⌋ for 0<i<n; children 2i+1,2i+2 when <n; ∀i with 0<i<n, p(xs[parent(i)])≤p(xs[i]); minimum(xs)=None if n=0, else Some(xs[0]); (x,h′)∈pop(h) iff minimum(h)=Some(x) and bag(items(h))={x}+bag(items(h′)); h′∈insert(h,x) iff bag(items(h′))=bag(items(h))+{x}

**basisKind:** extensional-structural-definition

**basisScope:** Fixed p:A→K into a linear order. Empty allowed, duplicate values/priorities allowed, ties unspecified. Equality retains level-order sequence. No capacity/overflow bound, stable tie order, or algorithm complexity promised.

**verificationObligation:** Map carrier, equality, operation definedness and stated profile to the target API or proof context.; Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.; Model coverage does not establish every recorded claim or an implementation refinement.

**reviewStatus:** Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-BinaryHeap-items"></a>

### items

`urn:csabs:operation/BinaryHeap-items`

**signature:** items : H_p(A)→Seq(A)

**description:** Observes the level-order sequence.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Fixed p:A→K into a linear order. Empty allowed, duplicate values/priorities allowed, ties unspecified. Equality retains level-order sequence. No capacity/overflow bound, stable tie order, or algorithm complexity promised.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Observes the level-order sequence.

**source:** [Pat Morin: Open Data Structures, BinaryHeap](https://opendatastructures.org/ods-python/10_1_BinaryHeap_Implicit_Bi.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §10.1: complete-array shape, parent index, heap order and minimum root

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-BinaryHeap-minimum"></a>

### minimum

`urn:csabs:operation/BinaryHeap-minimum`

**signature:** minimum : H_p(A)→Option(A)

**description:** None when empty; Some(xs[0]) otherwise.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Fixed p:A→K into a linear order. Empty allowed, duplicate values/priorities allowed, ties unspecified. Equality retains level-order sequence. No capacity/overflow bound, stable tie order, or algorithm complexity promised.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** None when empty; Some(xs[0]) otherwise.

**source:** [Pat Morin: Open Data Structures, BinaryHeap](https://opendatastructures.org/ods-python/10_1_BinaryHeap_Implicit_Bi.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §10.1: complete-array shape, parent index, heap order and minimum root

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-BinaryHeap-insert"></a>

### insert

`urn:csabs:operation/BinaryHeap-insert`

**signature:** insert : H_p(A)×A→𝒫(H_p(A))

**description:** Result heaps have occurrence multiset old plus one occurrence of x.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Fixed p:A→K into a linear order. Empty allowed, duplicate values/priorities allowed, ties unspecified. Equality retains level-order sequence. No capacity/overflow bound, stable tie order, or algorithm complexity promised.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Result heaps have occurrence multiset old plus one occurrence of x.

**source:** [Pat Morin: Open Data Structures, BinaryHeap](https://opendatastructures.org/ods-python/10_1_BinaryHeap_Implicit_Bi.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §10.1: complete-array shape, parent index, heap order and minimum root

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-BinaryHeap-pop"></a>

### pop

`urn:csabs:operation/BinaryHeap-pop`

**signature:** pop : H_p(A)⇀A×H_p(A)

**description:** Nonempty only; returns root and a heap with exactly one occurrence of it removed.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Fixed p:A→K into a linear order. Empty allowed, duplicate values/priorities allowed, ties unspecified. Equality retains level-order sequence. No capacity/overflow bound, stable tie order, or algorithm complexity promised.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Nonempty only; returns root and a heap with exactly one occurrence of it removed.

**source:** [Pat Morin: Open Data Structures, BinaryHeap](https://opendatastructures.org/ods-python/10_1_BinaryHeap_Implicit_Bi.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §10.1: complete-array shape, parent index, heap order and minimum root

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-BinaryHeap-complete-shape"></a>

### complete-shape

`urn:csabs:axiom/BinaryHeap-complete-shape`

**statement:** Defining requirement: Nodes are indices 0,…,n-1; parent(i)=⌊(i-1)/2⌋ for 0<i<n; children 2i+1,2i+2 when <n

**formalStatement:** Nodes are indices 0,…,n-1; parent(i)=⌊(i-1)/2⌋ for 0<i<n; children 2i+1,2i+2 when <n

**assumptions:** Fixed p:A→K into a linear order. Empty allowed, duplicate values/priorities allowed, ties unspecified. Equality retains level-order sequence. No capacity/overflow bound, stable tie order, or algorithm complexity promised.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Pat Morin: Open Data Structures, BinaryHeap](https://opendatastructures.org/ods-python/10_1_BinaryHeap_Implicit_Bi.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §10.1: complete-array shape, parent index, heap order and minimum root

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-BinaryHeap-heap-order"></a>

### heap-order

`urn:csabs:axiom/BinaryHeap-heap-order`

**statement:** Defining requirement: ∀i with 0<i<n, p(xs[parent(i)])≤p(xs[i])

**formalStatement:** ∀i with 0<i<n, p(xs[parent(i)])≤p(xs[i])

**assumptions:** Fixed p:A→K into a linear order. Empty allowed, duplicate values/priorities allowed, ties unspecified. Equality retains level-order sequence. No capacity/overflow bound, stable tie order, or algorithm complexity promised.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Pat Morin: Open Data Structures, BinaryHeap](https://opendatastructures.org/ods-python/10_1_BinaryHeap_Implicit_Bi.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §10.1: complete-array shape, parent index, heap order and minimum root

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-BinaryHeap-minimum-observation"></a>

### minimum-observation

`urn:csabs:axiom/BinaryHeap-minimum-observation`

**statement:** Defining requirement: minimum(xs)=None if n=0, else Some(xs[0])

**formalStatement:** minimum(xs)=None if n=0, else Some(xs[0])

**assumptions:** Fixed p:A→K into a linear order. Empty allowed, duplicate values/priorities allowed, ties unspecified. Equality retains level-order sequence. No capacity/overflow bound, stable tie order, or algorithm complexity promised.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Pat Morin: Open Data Structures, BinaryHeap](https://opendatastructures.org/ods-python/10_1_BinaryHeap_Implicit_Bi.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §10.1: complete-array shape, parent index, heap order and minimum root

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-BinaryHeap-update-bags"></a>

### update-bags

`urn:csabs:axiom/BinaryHeap-update-bags`

**statement:** Defining requirement: (x,h′)∈pop(h) iff minimum(h)=Some(x) and bag(items(h))={x}+bag(items(h′)); h′∈insert(h,x) iff bag(items(h′))=bag(items(h))+{x}

**formalStatement:** (x,h′)∈pop(h) iff minimum(h)=Some(x) and bag(items(h))={x}+bag(items(h′)); h′∈insert(h,x) iff bag(items(h′))=bag(items(h))+{x}

**assumptions:** Fixed p:A→K into a linear order. Empty allowed, duplicate values/priorities allowed, ties unspecified. Equality retains level-order sequence. No capacity/overflow bound, stable tie order, or algorithm complexity promised.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Pat Morin: Open Data Structures, BinaryHeap](https://opendatastructures.org/ods-python/10_1_BinaryHeap_Implicit_Bi.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §10.1: complete-array shape, parent index, heap order and minimum root

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-BinaryHeap-root-is-minimum"></a>

### root-is-minimum

`urn:csabs:law/BinaryHeap-root-is-minimum`

**statement:** n>0 ⇒ ∀i<n, p(xs[0])≤p(xs[i])

**formalStatement:** n>0 ⇒ ∀i<n, p(xs[0])≤p(xs[i])

**assumptions:** Fixed p:A→K into a linear order. Empty allowed, duplicate values/priorities allowed, ties unspecified. Equality retains level-order sequence. No capacity/overflow bound, stable tie order, or algorithm complexity promised.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [complete-shape](BinaryHeap.md#node-urn-csabs-axiom-BinaryHeap-complete-shape); [heap-order](BinaryHeap.md#node-urn-csabs-axiom-BinaryHeap-heap-order)

**proofSketch:** Repeated parent indices strictly decrease until zero; chain heap inequalities by transitivity.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Pat Morin: Open Data Structures, BinaryHeap](https://opendatastructures.org/ods-python/10_1_BinaryHeap_Implicit_Bi.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §10.1: complete-array shape, parent index, heap order and minimum root

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Theorems

<a id="node-urn-csabs-theorem-BinaryHeap-pop-cardinality"></a>

### pop-cardinality

`urn:csabs:theorem/BinaryHeap-pop-cardinality`

**statement:** (x,h′)∈pop(h) ⇒ |items(h′)|+1=|items(h)|

**formalStatement:** (x,h′)∈pop(h) ⇒ |items(h′)|+1=|items(h)|

**assumptions:** Fixed p:A→K into a linear order. Empty allowed, duplicate values/priorities allowed, ties unspecified. Equality retains level-order sequence. No capacity/overflow bound, stable tie order, or algorithm complexity promised.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [update-bags](BinaryHeap.md#node-urn-csabs-axiom-BinaryHeap-update-bags)

**proofSketch:** Take multiset cardinalities in the pop equation; a singleton contributes one.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Pat Morin: Open Data Structures, BinaryHeap](https://opendatastructures.org/ods-python/10_1_BinaryHeap_Implicit_Bi.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §10.1: complete-array shape, parent index, heap order and minimum root

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Concept provenance

- [Pat Morin: Open Data Structures, BinaryHeap](https://opendatastructures.org/ods-python/10_1_BinaryHeap_Implicit_Bi.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §10.1: complete-array shape, parent index, heap order and minimum root

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/BinaryHeap",
    "type": "Concept",
    "shortForm": "BinaryHeap",
    "fullName": "Finite complete binary min-heap",
    "category": [
      "urn:csabs:category/tree-structures",
      "urn:csabs:category/priority-collections"
    ],
    "kind": "urn:csabs:kind/abstract-data-type",
    "definition": "A finite level-order sequence with complete binary-tree shape and parent priority at most child priority.",
    "notation": "H_p(A)={xs∈Seq(A) | ∀0<i<|xs|, p(xs[⌊(i-1)/2⌋])≤p(xs[i])}",
    "requiresConcept": [
      "urn:csabs:concept/Sequence",
      "urn:csabs:concept/PriorityQueue",
      "urn:csabs:concept/TotalOrder"
    ],
    "relatedConcept": [
      "urn:csabs:concept/BinaryTree"
    ],
    "hasOperation": [
      "urn:csabs:operation/BinaryHeap-items",
      "urn:csabs:operation/BinaryHeap-minimum",
      "urn:csabs:operation/BinaryHeap-insert",
      "urn:csabs:operation/BinaryHeap-pop"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/BinaryHeap-complete-shape",
      "urn:csabs:axiom/BinaryHeap-heap-order",
      "urn:csabs:axiom/BinaryHeap-minimum-observation",
      "urn:csabs:axiom/BinaryHeap-update-bags"
    ],
    "hasLaw": [
      "urn:csabs:law/BinaryHeap-root-is-minimum"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/BinaryHeap-pop-cardinality"
    ],
    "axiomBasis": "Nodes are indices 0,…,n-1; parent(i)=⌊(i-1)/2⌋ for 0<i<n; children 2i+1,2i+2 when <n; ∀i with 0<i<n, p(xs[parent(i)])≤p(xs[i]); minimum(xs)=None if n=0, else Some(xs[0]); (x,h′)∈pop(h) iff minimum(h)=Some(x) and bag(items(h))={x}+bag(items(h′)); h′∈insert(h,x) iff bag(items(h′))=bag(items(h))+{x}",
    "basisKind": "extensional-structural-definition",
    "basisScope": "Fixed p:A→K into a linear order. Empty allowed, duplicate values/priorities allowed, ties unspecified. Equality retains level-order sequence. No capacity/overflow bound, stable tie order, or algorithm complexity promised.",
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Map carrier, equality, operation definedness and stated profile to the target API or proof context.",
      "Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.",
      "Model coverage does not establish every recorded claim or an implementation refinement."
    ],
    "reviewStatus": "Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.",
    "source": [
      "urn:csabs:source/ods-heap-core"
    ],
    "sourceLocator": "§10.1: complete-array shape, parent index, heap order and minimum root",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted",
    "leanFormulation": "structure BinaryHeap (A : Type u) (K : Type v) [LinearOrder K] (priority : A → K) where\n  items : List A\n  ordered : ∀ (i : Fin items.length), 0 < i.val →\n    priority (items.get ⟨(i.val - 1) / 2, by have := i.isLt; omega⟩) ≤ priority (items.get i)",
    "formulationSource": "urn:csabs:source/local-lean-StructuredData",
    "formulationLocator": "Catalog.BinaryHeap",
    "formulationScope": "model",
    "leanModelMapping": "H_p(A)={xs∈Seq(A) | ∀0<i<|xs|, p(xs[⌊(i-1)/2⌋])≤p(xs[i])}. Fixed p:A→K into a linear order. Empty allowed, duplicate values/priorities allowed, ties unspecified. Equality retains level-order sequence. No capacity/overflow bound, stable tie order, or algorithm complexity promised.",
    "leanModelLimitations": "Compiled carrier and selected interface interpretation. Some catalog operations are specified mathematically rather than wrapped as Lean declarations; no blanket proof of claims, algorithms, parsing, liveness or complexity. See individual witnesses.",
    "mathematicalFormulation": "A min-heap is a finite sequence xs with ∀i,0<i<|xs|⇒p(xs[⌊(i−1)/2⌋])≤p(xs[i]), where p:A→K and K is linearly ordered. Array indices impose complete binary shape; equal priorities are allowed."
  },
  {
    "id": "urn:csabs:operation/BinaryHeap-items",
    "type": "Operation",
    "name": "items",
    "signature": "items : H_p(A)→Seq(A)",
    "description": "Observes the level-order sequence.",
    "concept": "urn:csabs:concept/BinaryHeap",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Fixed p:A→K into a linear order. Empty allowed, duplicate values/priorities allowed, ties unspecified. Equality retains level-order sequence. No capacity/overflow bound, stable tie order, or algorithm complexity promised.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Observes the level-order sequence.",
    "source": [
      "urn:csabs:source/ods-heap-core"
    ],
    "sourceLocator": "§10.1: complete-array shape, parent index, heap order and minimum root",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/BinaryHeap-minimum",
    "type": "Operation",
    "name": "minimum",
    "signature": "minimum : H_p(A)→Option(A)",
    "description": "None when empty; Some(xs[0]) otherwise.",
    "concept": "urn:csabs:concept/BinaryHeap",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Fixed p:A→K into a linear order. Empty allowed, duplicate values/priorities allowed, ties unspecified. Equality retains level-order sequence. No capacity/overflow bound, stable tie order, or algorithm complexity promised.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "None when empty; Some(xs[0]) otherwise.",
    "source": [
      "urn:csabs:source/ods-heap-core"
    ],
    "sourceLocator": "§10.1: complete-array shape, parent index, heap order and minimum root",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/BinaryHeap-insert",
    "type": "Operation",
    "name": "insert",
    "signature": "insert : H_p(A)×A→𝒫(H_p(A))",
    "description": "Result heaps have occurrence multiset old plus one occurrence of x.",
    "concept": "urn:csabs:concept/BinaryHeap",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Fixed p:A→K into a linear order. Empty allowed, duplicate values/priorities allowed, ties unspecified. Equality retains level-order sequence. No capacity/overflow bound, stable tie order, or algorithm complexity promised.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Result heaps have occurrence multiset old plus one occurrence of x.",
    "source": [
      "urn:csabs:source/ods-heap-core"
    ],
    "sourceLocator": "§10.1: complete-array shape, parent index, heap order and minimum root",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/BinaryHeap-pop",
    "type": "Operation",
    "name": "pop",
    "signature": "pop : H_p(A)⇀A×H_p(A)",
    "description": "Nonempty only; returns root and a heap with exactly one occurrence of it removed.",
    "concept": "urn:csabs:concept/BinaryHeap",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Fixed p:A→K into a linear order. Empty allowed, duplicate values/priorities allowed, ties unspecified. Equality retains level-order sequence. No capacity/overflow bound, stable tie order, or algorithm complexity promised.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Nonempty only; returns root and a heap with exactly one occurrence of it removed.",
    "source": [
      "urn:csabs:source/ods-heap-core"
    ],
    "sourceLocator": "§10.1: complete-array shape, parent index, heap order and minimum root",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/BinaryHeap-complete-shape",
    "type": "Axiom",
    "name": "complete-shape",
    "statement": "Defining requirement: Nodes are indices 0,…,n-1; parent(i)=⌊(i-1)/2⌋ for 0<i<n; children 2i+1,2i+2 when <n",
    "formalStatement": "Nodes are indices 0,…,n-1; parent(i)=⌊(i-1)/2⌋ for 0<i<n; children 2i+1,2i+2 when <n",
    "assumptions": [
      "Fixed p:A→K into a linear order. Empty allowed, duplicate values/priorities allowed, ties unspecified. Equality retains level-order sequence. No capacity/overflow bound, stable tie order, or algorithm complexity promised.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/BinaryHeap"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/ods-heap-core"
    ],
    "sourceLocator": "§10.1: complete-array shape, parent index, heap order and minimum root",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/BinaryHeap-heap-order",
    "type": "Axiom",
    "name": "heap-order",
    "statement": "Defining requirement: ∀i with 0<i<n, p(xs[parent(i)])≤p(xs[i])",
    "formalStatement": "∀i with 0<i<n, p(xs[parent(i)])≤p(xs[i])",
    "assumptions": [
      "Fixed p:A→K into a linear order. Empty allowed, duplicate values/priorities allowed, ties unspecified. Equality retains level-order sequence. No capacity/overflow bound, stable tie order, or algorithm complexity promised.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/BinaryHeap"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/ods-heap-core"
    ],
    "sourceLocator": "§10.1: complete-array shape, parent index, heap order and minimum root",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/BinaryHeap-minimum-observation",
    "type": "Axiom",
    "name": "minimum-observation",
    "statement": "Defining requirement: minimum(xs)=None if n=0, else Some(xs[0])",
    "formalStatement": "minimum(xs)=None if n=0, else Some(xs[0])",
    "assumptions": [
      "Fixed p:A→K into a linear order. Empty allowed, duplicate values/priorities allowed, ties unspecified. Equality retains level-order sequence. No capacity/overflow bound, stable tie order, or algorithm complexity promised.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/BinaryHeap"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/ods-heap-core"
    ],
    "sourceLocator": "§10.1: complete-array shape, parent index, heap order and minimum root",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/BinaryHeap-update-bags",
    "type": "Axiom",
    "name": "update-bags",
    "statement": "Defining requirement: (x,h′)∈pop(h) iff minimum(h)=Some(x) and bag(items(h))={x}+bag(items(h′)); h′∈insert(h,x) iff bag(items(h′))=bag(items(h))+{x}",
    "formalStatement": "(x,h′)∈pop(h) iff minimum(h)=Some(x) and bag(items(h))={x}+bag(items(h′)); h′∈insert(h,x) iff bag(items(h′))=bag(items(h))+{x}",
    "assumptions": [
      "Fixed p:A→K into a linear order. Empty allowed, duplicate values/priorities allowed, ties unspecified. Equality retains level-order sequence. No capacity/overflow bound, stable tie order, or algorithm complexity promised.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/BinaryHeap"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/ods-heap-core"
    ],
    "sourceLocator": "§10.1: complete-array shape, parent index, heap order and minimum root",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/BinaryHeap-root-is-minimum",
    "type": "Law",
    "name": "root-is-minimum",
    "statement": "n>0 ⇒ ∀i<n, p(xs[0])≤p(xs[i])",
    "formalStatement": "n>0 ⇒ ∀i<n, p(xs[0])≤p(xs[i])",
    "assumptions": [
      "Fixed p:A→K into a linear order. Empty allowed, duplicate values/priorities allowed, ties unspecified. Equality retains level-order sequence. No capacity/overflow bound, stable tie order, or algorithm complexity promised.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/BinaryHeap"
    ],
    "dependsOn": [
      "urn:csabs:axiom/BinaryHeap-complete-shape",
      "urn:csabs:axiom/BinaryHeap-heap-order"
    ],
    "proofSketch": "Repeated parent indices strictly decrease until zero; chain heap inequalities by transitivity.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/ods-heap-core"
    ],
    "sourceLocator": "§10.1: complete-array shape, parent index, heap order and minimum root",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/BinaryHeap-pop-cardinality",
    "type": "Theorem",
    "name": "pop-cardinality",
    "statement": "(x,h′)∈pop(h) ⇒ |items(h′)|+1=|items(h)|",
    "formalStatement": "(x,h′)∈pop(h) ⇒ |items(h′)|+1=|items(h)|",
    "assumptions": [
      "Fixed p:A→K into a linear order. Empty allowed, duplicate values/priorities allowed, ties unspecified. Equality retains level-order sequence. No capacity/overflow bound, stable tie order, or algorithm complexity promised.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/BinaryHeap"
    ],
    "dependsOn": [
      "urn:csabs:axiom/BinaryHeap-update-bags"
    ],
    "proofSketch": "Take multiset cardinalities in the pop equation; a singleton contributes one.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/ods-heap-core"
    ],
    "sourceLocator": "§10.1: complete-array shape, parent index, heap order and minimum root",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
