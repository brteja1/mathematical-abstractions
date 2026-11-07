# Finite allocated heap store

A finite map from nonnull addresses to values, with partial allocated-cell access and fresh allocation.

**Notation:** Heap(V)=Addr⇀fin V; Addr=ℕ_{>0}

**Stable ID:** `urn:csabs:concept/HeapStore`

**Categories:** Programming-language semantics

**Kind:** Abstract data type

**Prerequisites:** [Map](Map.md), [Option Type](OptionType.md), [Natural Number](NaturalNumber.md)

## Interface and scope

**axiomBasis:** dom(h) is a finite subset of positive addresses; heap equality is lookup equality; a∈dom(h) ⇒ write(h,a,v)(b)=Some(v) if b=a, else h(b); a∈dom(h) ⇒ free(h,a)(b)=None if b=a, else h(b); (a,h′)∈alloc(h,v) ⇔ a∉dom(h) ∧ h′=h[a↦v]

**basisKind:** extensional-structural-definition

**basisScope:** Pure mathematical snapshots. Unallocated read/write/free is undefined (None); stored values may themselves encode options. Allocation nondeterministically chooses any fresh positive address; address reuse after free allowed. No pointer arithmetic, GC, permissions, typing or concurrency assumed.

**verificationObligation:** Map carrier, equality, operation definedness and stated profile to the target API or proof context.; Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.; Model coverage does not establish every recorded claim or an implementation refinement.

**reviewStatus:** Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-HeapStore-read"></a>

### read

`urn:csabs:operation/HeapStore-read`

**signature:** read : Heap(V)×Addr→Option(V)

**description:** read(h,a)=h(a).

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Pure mathematical snapshots. Unallocated read/write/free is undefined (None); stored values may themselves encode options. Allocation nondeterministically chooses any fresh positive address; address reuse after free allowed. No pointer arithmetic, GC, permissions, typing or concurrency assumed.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** read(h,a)=h(a).

**source:** [Software Foundations, Separation Logic Foundations: Heap Predicates](https://softwarefoundations.cis.upenn.edu/slf-current/Hprop.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Description of Memory States: heaps as finite maps

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-HeapStore-write"></a>

### write

`urn:csabs:operation/HeapStore-write`

**signature:** write : Heap(V)×Addr×V⇀Heap(V)

**description:** For a∈dom(h), update only a to v; absent address undefined.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Pure mathematical snapshots. Unallocated read/write/free is undefined (None); stored values may themselves encode options. Allocation nondeterministically chooses any fresh positive address; address reuse after free allowed. No pointer arithmetic, GC, permissions, typing or concurrency assumed.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** For a∈dom(h), update only a to v; absent address undefined.

**source:** [Software Foundations, Separation Logic Foundations: Heap Predicates](https://softwarefoundations.cis.upenn.edu/slf-current/Hprop.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Description of Memory States: heaps as finite maps

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-HeapStore-free"></a>

### free

`urn:csabs:operation/HeapStore-free`

**signature:** free : Heap(V)×Addr⇀Heap(V)

**description:** For a∈dom(h), erase a; absent address undefined.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Pure mathematical snapshots. Unallocated read/write/free is undefined (None); stored values may themselves encode options. Allocation nondeterministically chooses any fresh positive address; address reuse after free allowed. No pointer arithmetic, GC, permissions, typing or concurrency assumed.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** For a∈dom(h), erase a; absent address undefined.

**source:** [Software Foundations, Separation Logic Foundations: Heap Predicates](https://softwarefoundations.cis.upenn.edu/slf-current/Hprop.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Description of Memory States: heaps as finite maps

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-HeapStore-allocate"></a>

### allocate

`urn:csabs:operation/HeapStore-allocate`

**signature:** alloc : Heap(V)×V→𝒫(Addr×Heap(V))

**description:** alloc(h,v)={(a,h[a↦v]) | a∉dom(h)}.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Pure mathematical snapshots. Unallocated read/write/free is undefined (None); stored values may themselves encode options. Allocation nondeterministically chooses any fresh positive address; address reuse after free allowed. No pointer arithmetic, GC, permissions, typing or concurrency assumed.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** alloc(h,v)={(a,h[a↦v]) | a∉dom(h)}.

**source:** [Software Foundations, Separation Logic Foundations: Heap Predicates](https://softwarefoundations.cis.upenn.edu/slf-current/Hprop.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Description of Memory States: heaps as finite maps

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-HeapStore-finite-domain"></a>

### finite-domain

`urn:csabs:axiom/HeapStore-finite-domain`

**statement:** Defining requirement: dom(h) is a finite subset of positive addresses; heap equality is lookup equality

**formalStatement:** dom(h) is a finite subset of positive addresses; heap equality is lookup equality

**assumptions:** Pure mathematical snapshots. Unallocated read/write/free is undefined (None); stored values may themselves encode options. Allocation nondeterministically chooses any fresh positive address; address reuse after free allowed. No pointer arithmetic, GC, permissions, typing or concurrency assumed.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Software Foundations, Separation Logic Foundations: Heap Predicates](https://softwarefoundations.cis.upenn.edu/slf-current/Hprop.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Description of Memory States: heaps as finite maps

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-HeapStore-write-frame"></a>

### write-frame

`urn:csabs:axiom/HeapStore-write-frame`

**statement:** Defining requirement: a∈dom(h) ⇒ write(h,a,v)(b)=Some(v) if b=a, else h(b)

**formalStatement:** a∈dom(h) ⇒ write(h,a,v)(b)=Some(v) if b=a, else h(b)

**assumptions:** Pure mathematical snapshots. Unallocated read/write/free is undefined (None); stored values may themselves encode options. Allocation nondeterministically chooses any fresh positive address; address reuse after free allowed. No pointer arithmetic, GC, permissions, typing or concurrency assumed.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Software Foundations, Separation Logic Foundations: Heap Predicates](https://softwarefoundations.cis.upenn.edu/slf-current/Hprop.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Description of Memory States: heaps as finite maps

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-HeapStore-free-frame"></a>

### free-frame

`urn:csabs:axiom/HeapStore-free-frame`

**statement:** Defining requirement: a∈dom(h) ⇒ free(h,a)(b)=None if b=a, else h(b)

**formalStatement:** a∈dom(h) ⇒ free(h,a)(b)=None if b=a, else h(b)

**assumptions:** Pure mathematical snapshots. Unallocated read/write/free is undefined (None); stored values may themselves encode options. Allocation nondeterministically chooses any fresh positive address; address reuse after free allowed. No pointer arithmetic, GC, permissions, typing or concurrency assumed.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Software Foundations, Separation Logic Foundations: Heap Predicates](https://softwarefoundations.cis.upenn.edu/slf-current/Hprop.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Description of Memory States: heaps as finite maps

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-HeapStore-allocation"></a>

### allocation

`urn:csabs:axiom/HeapStore-allocation`

**statement:** Defining requirement: (a,h′)∈alloc(h,v) ⇔ a∉dom(h) ∧ h′=h[a↦v]

**formalStatement:** (a,h′)∈alloc(h,v) ⇔ a∉dom(h) ∧ h′=h[a↦v]

**assumptions:** Pure mathematical snapshots. Unallocated read/write/free is undefined (None); stored values may themselves encode options. Allocation nondeterministically chooses any fresh positive address; address reuse after free allowed. No pointer arithmetic, GC, permissions, typing or concurrency assumed.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Software Foundations, Separation Logic Foundations: Heap Predicates](https://softwarefoundations.cis.upenn.edu/slf-current/Hprop.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Description of Memory States: heaps as finite maps

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-HeapStore-read-after-write"></a>

### read-after-write

`urn:csabs:law/HeapStore-read-after-write`

**statement:** a∈dom(h) ⇒ read(write(h,a,v),a)=Some(v)

**formalStatement:** a∈dom(h) ⇒ read(write(h,a,v),a)=Some(v)

**assumptions:** Pure mathematical snapshots. Unallocated read/write/free is undefined (None); stored values may themselves encode options. Allocation nondeterministically chooses any fresh positive address; address reuse after free allowed. No pointer arithmetic, GC, permissions, typing or concurrency assumed.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [write-frame](HeapStore.md#node-urn-csabs-axiom-HeapStore-write-frame)

**proofSketch:** Instantiate the write frame equation at b=a.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Software Foundations, Separation Logic Foundations: Heap Predicates](https://softwarefoundations.cis.upenn.edu/slf-current/Hprop.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Description of Memory States: heaps as finite maps

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Theorems

<a id="node-urn-csabs-theorem-HeapStore-fresh-allocation-exists"></a>

### fresh-allocation-exists

`urn:csabs:theorem/HeapStore-fresh-allocation-exists`

**statement:** ∀h,v, alloc(h,v)≠∅

**formalStatement:** ∀h,v, alloc(h,v)≠∅

**assumptions:** Pure mathematical snapshots. Unallocated read/write/free is undefined (None); stored values may themselves encode options. Allocation nondeterministically chooses any fresh positive address; address reuse after free allowed. No pointer arithmetic, GC, permissions, typing or concurrency assumed.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [finite-domain](HeapStore.md#node-urn-csabs-axiom-HeapStore-finite-domain); [allocation](HeapStore.md#node-urn-csabs-axiom-HeapStore-allocation)

**proofSketch:** A finite positive-address domain omits some address in the infinite positive naturals; map extension supplies a successor heap.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Software Foundations, Separation Logic Foundations: Heap Predicates](https://softwarefoundations.cis.upenn.edu/slf-current/Hprop.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Description of Memory States: heaps as finite maps

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Concept provenance

- [Software Foundations, Separation Logic Foundations: Heap Predicates](https://softwarefoundations.cis.upenn.edu/slf-current/Hprop.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Description of Memory States: heaps as finite maps

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/HeapStore",
    "type": "Concept",
    "shortForm": "HeapStore",
    "fullName": "Finite allocated heap store",
    "category": [
      "urn:csabs:category/programming-semantics"
    ],
    "kind": "urn:csabs:kind/abstract-data-type",
    "definition": "A finite map from nonnull addresses to values, with partial allocated-cell access and fresh allocation.",
    "notation": "Heap(V)=Addr⇀fin V; Addr=ℕ_{>0}",
    "requiresConcept": [
      "urn:csabs:concept/Map",
      "urn:csabs:concept/OptionType",
      "urn:csabs:concept/NaturalNumber"
    ],
    "relatedConcept": [],
    "hasOperation": [
      "urn:csabs:operation/HeapStore-read",
      "urn:csabs:operation/HeapStore-write",
      "urn:csabs:operation/HeapStore-free",
      "urn:csabs:operation/HeapStore-allocate"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/HeapStore-finite-domain",
      "urn:csabs:axiom/HeapStore-write-frame",
      "urn:csabs:axiom/HeapStore-free-frame",
      "urn:csabs:axiom/HeapStore-allocation"
    ],
    "hasLaw": [
      "urn:csabs:law/HeapStore-read-after-write"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/HeapStore-fresh-allocation-exists"
    ],
    "axiomBasis": "dom(h) is a finite subset of positive addresses; heap equality is lookup equality; a∈dom(h) ⇒ write(h,a,v)(b)=Some(v) if b=a, else h(b); a∈dom(h) ⇒ free(h,a)(b)=None if b=a, else h(b); (a,h′)∈alloc(h,v) ⇔ a∉dom(h) ∧ h′=h[a↦v]",
    "basisKind": "extensional-structural-definition",
    "basisScope": "Pure mathematical snapshots. Unallocated read/write/free is undefined (None); stored values may themselves encode options. Allocation nondeterministically chooses any fresh positive address; address reuse after free allowed. No pointer arithmetic, GC, permissions, typing or concurrency assumed.",
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Map carrier, equality, operation definedness and stated profile to the target API or proof context.",
      "Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.",
      "Model coverage does not establish every recorded claim or an implementation refinement."
    ],
    "reviewStatus": "Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.",
    "source": [
      "urn:csabs:source/slf-heap-core"
    ],
    "sourceLocator": "Description of Memory States: heaps as finite maps",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/HeapStore-read",
    "type": "Operation",
    "name": "read",
    "signature": "read : Heap(V)×Addr→Option(V)",
    "description": "read(h,a)=h(a).",
    "concept": "urn:csabs:concept/HeapStore",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Pure mathematical snapshots. Unallocated read/write/free is undefined (None); stored values may themselves encode options. Allocation nondeterministically chooses any fresh positive address; address reuse after free allowed. No pointer arithmetic, GC, permissions, typing or concurrency assumed.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "read(h,a)=h(a).",
    "source": [
      "urn:csabs:source/slf-heap-core"
    ],
    "sourceLocator": "Description of Memory States: heaps as finite maps",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/HeapStore-write",
    "type": "Operation",
    "name": "write",
    "signature": "write : Heap(V)×Addr×V⇀Heap(V)",
    "description": "For a∈dom(h), update only a to v; absent address undefined.",
    "concept": "urn:csabs:concept/HeapStore",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Pure mathematical snapshots. Unallocated read/write/free is undefined (None); stored values may themselves encode options. Allocation nondeterministically chooses any fresh positive address; address reuse after free allowed. No pointer arithmetic, GC, permissions, typing or concurrency assumed.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "For a∈dom(h), update only a to v; absent address undefined.",
    "source": [
      "urn:csabs:source/slf-heap-core"
    ],
    "sourceLocator": "Description of Memory States: heaps as finite maps",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/HeapStore-free",
    "type": "Operation",
    "name": "free",
    "signature": "free : Heap(V)×Addr⇀Heap(V)",
    "description": "For a∈dom(h), erase a; absent address undefined.",
    "concept": "urn:csabs:concept/HeapStore",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Pure mathematical snapshots. Unallocated read/write/free is undefined (None); stored values may themselves encode options. Allocation nondeterministically chooses any fresh positive address; address reuse after free allowed. No pointer arithmetic, GC, permissions, typing or concurrency assumed.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "For a∈dom(h), erase a; absent address undefined.",
    "source": [
      "urn:csabs:source/slf-heap-core"
    ],
    "sourceLocator": "Description of Memory States: heaps as finite maps",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/HeapStore-allocate",
    "type": "Operation",
    "name": "allocate",
    "signature": "alloc : Heap(V)×V→𝒫(Addr×Heap(V))",
    "description": "alloc(h,v)={(a,h[a↦v]) | a∉dom(h)}.",
    "concept": "urn:csabs:concept/HeapStore",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Pure mathematical snapshots. Unallocated read/write/free is undefined (None); stored values may themselves encode options. Allocation nondeterministically chooses any fresh positive address; address reuse after free allowed. No pointer arithmetic, GC, permissions, typing or concurrency assumed.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "alloc(h,v)={(a,h[a↦v]) | a∉dom(h)}.",
    "source": [
      "urn:csabs:source/slf-heap-core"
    ],
    "sourceLocator": "Description of Memory States: heaps as finite maps",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/HeapStore-finite-domain",
    "type": "Axiom",
    "name": "finite-domain",
    "statement": "Defining requirement: dom(h) is a finite subset of positive addresses; heap equality is lookup equality",
    "formalStatement": "dom(h) is a finite subset of positive addresses; heap equality is lookup equality",
    "assumptions": [
      "Pure mathematical snapshots. Unallocated read/write/free is undefined (None); stored values may themselves encode options. Allocation nondeterministically chooses any fresh positive address; address reuse after free allowed. No pointer arithmetic, GC, permissions, typing or concurrency assumed.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/HeapStore"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/slf-heap-core"
    ],
    "sourceLocator": "Description of Memory States: heaps as finite maps",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/HeapStore-write-frame",
    "type": "Axiom",
    "name": "write-frame",
    "statement": "Defining requirement: a∈dom(h) ⇒ write(h,a,v)(b)=Some(v) if b=a, else h(b)",
    "formalStatement": "a∈dom(h) ⇒ write(h,a,v)(b)=Some(v) if b=a, else h(b)",
    "assumptions": [
      "Pure mathematical snapshots. Unallocated read/write/free is undefined (None); stored values may themselves encode options. Allocation nondeterministically chooses any fresh positive address; address reuse after free allowed. No pointer arithmetic, GC, permissions, typing or concurrency assumed.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/HeapStore"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/slf-heap-core"
    ],
    "sourceLocator": "Description of Memory States: heaps as finite maps",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/HeapStore-free-frame",
    "type": "Axiom",
    "name": "free-frame",
    "statement": "Defining requirement: a∈dom(h) ⇒ free(h,a)(b)=None if b=a, else h(b)",
    "formalStatement": "a∈dom(h) ⇒ free(h,a)(b)=None if b=a, else h(b)",
    "assumptions": [
      "Pure mathematical snapshots. Unallocated read/write/free is undefined (None); stored values may themselves encode options. Allocation nondeterministically chooses any fresh positive address; address reuse after free allowed. No pointer arithmetic, GC, permissions, typing or concurrency assumed.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/HeapStore"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/slf-heap-core"
    ],
    "sourceLocator": "Description of Memory States: heaps as finite maps",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/HeapStore-allocation",
    "type": "Axiom",
    "name": "allocation",
    "statement": "Defining requirement: (a,h′)∈alloc(h,v) ⇔ a∉dom(h) ∧ h′=h[a↦v]",
    "formalStatement": "(a,h′)∈alloc(h,v) ⇔ a∉dom(h) ∧ h′=h[a↦v]",
    "assumptions": [
      "Pure mathematical snapshots. Unallocated read/write/free is undefined (None); stored values may themselves encode options. Allocation nondeterministically chooses any fresh positive address; address reuse after free allowed. No pointer arithmetic, GC, permissions, typing or concurrency assumed.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/HeapStore"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/slf-heap-core"
    ],
    "sourceLocator": "Description of Memory States: heaps as finite maps",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/HeapStore-read-after-write",
    "type": "Law",
    "name": "read-after-write",
    "statement": "a∈dom(h) ⇒ read(write(h,a,v),a)=Some(v)",
    "formalStatement": "a∈dom(h) ⇒ read(write(h,a,v),a)=Some(v)",
    "assumptions": [
      "Pure mathematical snapshots. Unallocated read/write/free is undefined (None); stored values may themselves encode options. Allocation nondeterministically chooses any fresh positive address; address reuse after free allowed. No pointer arithmetic, GC, permissions, typing or concurrency assumed.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/HeapStore"
    ],
    "dependsOn": [
      "urn:csabs:axiom/HeapStore-write-frame"
    ],
    "proofSketch": "Instantiate the write frame equation at b=a.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/slf-heap-core"
    ],
    "sourceLocator": "Description of Memory States: heaps as finite maps",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/HeapStore-fresh-allocation-exists",
    "type": "Theorem",
    "name": "fresh-allocation-exists",
    "statement": "∀h,v, alloc(h,v)≠∅",
    "formalStatement": "∀h,v, alloc(h,v)≠∅",
    "assumptions": [
      "Pure mathematical snapshots. Unallocated read/write/free is undefined (None); stored values may themselves encode options. Allocation nondeterministically chooses any fresh positive address; address reuse after free allowed. No pointer arithmetic, GC, permissions, typing or concurrency assumed.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/HeapStore"
    ],
    "dependsOn": [
      "urn:csabs:axiom/HeapStore-finite-domain",
      "urn:csabs:axiom/HeapStore-allocation"
    ],
    "proofSketch": "A finite positive-address domain omits some address in the infinite positive naturals; map extension supplies a successor heap.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/slf-heap-core"
    ],
    "sourceLocator": "Description of Memory States: heaps as finite maps",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
