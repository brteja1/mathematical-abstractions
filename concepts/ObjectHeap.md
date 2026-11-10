# Sequential object heap with reference identity

A finite allocated heap whose cells contain class tags and finite field maps; references identify cells independently of their stored values and may alias.

**Notation:** Addr=ℕ>0; Ref={null}⊎Addr; Value=Primitive⊎Ref; Obj=Class×(Field⇀fin Value); H=HeapStore(Obj)

**Stable ID:** `urn:csabs:concept/ObjectHeap`

**Categories:** Programming-language semantics → Object-oriented semantics

**Kind:** Abstract data type

**Prerequisites:** [Finite allocated heap store](HeapStore.md), [Map](Map.md), [Option Type](OptionType.md)

**Specializes:** [Finite allocated heap store](HeapStore.md)

**Related concepts:** [Single-inheritance class table and dynamic dispatch](ClassTable.md), [Exclusive finite-heap separation predicates](HeapSeparation.md)

## Backlinks

- [Single-inheritance class table and dynamic dispatch](ClassTable.md) — `relatedConcept`
- [Exclusive finite-heap separation predicates](HeapSeparation.md) — `relatedConcept`
- [Relational method contract with write effects](MethodContract.md) — `relatedConcept`
- [Visible-state object invariant protocol](ObjectInvariant.md) — `requiresConcept`

## Interface and scope

**axiomBasis:** Selected defining rules: Every h is a finite address map of pairs (C,F) with finite field maps F; h=k iff all allocated-cell lookups agree. h(a)=(C,F) ∧ f∈dom(F) ⇒ writeField(h,a,f,v)=h[a↦(C,F[f↦v])]; readField(h,a,f)=F(f). sameRef(r,s)=true ⇔ r=s as tagged references; aliases(h,r,s) ⇔ ∃a∈dom(h), r=a ∧ s=a. Contents equality does not identify distinct addresses.

**basisKind:** extensional-structural-definition

**basisScope:** Sequential mathematical snapshots. Primitive, Class and Field are fixed carriers; fields use declaring-class-qualified identifiers, so field hiding is not dynamic dispatch. Ref equality is tagged identity; heap equality is extensional. Null is not an address. Dangling references are representable but cannot be dereferenced. No type safety, access control, ownership, constructor protocol, GC, pointer arithmetic or concurrency is inferred. Inherited raw heap replacement/free may change tags or leave dangling references; class-stable updates are the field operations below.

**specializationNote:** Instantiate HeapStore value carrier V with Obj=Class×Map(Field,Value), using the same positive addresses, extensional heap equality and read/write/free/fresh-allocation operations. Field observers/updates are additional operations; references are values, not separate heap cells. Raw inherited operations retain their original definedness.

**verificationObligation:** Instantiate carriers, equality, definedness and the stated semantic profile before using these records.; Catalog validation checks structure, not source entailment or target implementation conformance.

**reviewStatus:** Editorial source and interface review; Lean model bindings and individual proof witnesses are separate.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-ObjectHeap-class-of"></a>

### class-of

`urn:csabs:operation/ObjectHeap-class-of`

**signature:** classOf : H×Ref⇀Class

**description:** For allocated a, classOf(h,a)=h(a).class; null or an absent address is undefined.

**precondition:** Reference is nonnull and allocated.

**postcondition:** For allocated a, classOf(h,a)=h(a).class; null or an absent address is undefined.

**totality:** Partial; null/absent reference is undefined.

**source:** [Java Language Specification, Java SE 25, §4.3.1 Objects](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html#jls-4.3.1); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference; [Software Foundations, Separation Logic Foundations: Hprop — Heap Predicates](https://softwarefoundations.cis.upenn.edu/slf-current/Hprop.html); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** JLS §4.3.1, reference identity and shared-state example; SLF Hprop, Description of Memory States

**sourceNote:** Combines reference/field observations with the existing finite HeapStore. Class tags, qualified fields, dangling-reference representation and partial dereference are explicit catalog profile choices.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-ObjectHeap-read-field"></a>

### read-field

`urn:csabs:operation/ObjectHeap-read-field`

**signature:** readField : H×Ref×Field⇀Value

**description:** For h(a)=(C,F) and f∈dom(F), return F(f).

**precondition:** Reference is nonnull and allocated, and its record contains f.

**postcondition:** For h(a)=(C,F) and f∈dom(F), return F(f).

**totality:** Partial exactly outside the precondition.

**source:** [Java Language Specification, Java SE 25, §4.3.1 Objects](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html#jls-4.3.1); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference; [Software Foundations, Separation Logic Foundations: Hprop — Heap Predicates](https://softwarefoundations.cis.upenn.edu/slf-current/Hprop.html); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** JLS §4.3.1, reference identity and shared-state example; SLF Hprop, Description of Memory States

**sourceNote:** Combines reference/field observations with the existing finite HeapStore. Class tags, qualified fields, dangling-reference representation and partial dereference are explicit catalog profile choices.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-ObjectHeap-write-field"></a>

### write-field

`urn:csabs:operation/ObjectHeap-write-field`

**signature:** writeField : H×Ref×Field×Value⇀H

**description:** Replace only the existing field f at a by v, retaining its class tag, all other fields and all other objects.

**precondition:** Reference is nonnull and allocated, and its record contains f.

**postcondition:** Replace only the existing field f at a by v, retaining its class tag, all other fields and all other objects.

**totality:** Partial exactly outside the precondition.

**source:** [Java Language Specification, Java SE 25, §4.3.1 Objects](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html#jls-4.3.1); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference; [Software Foundations, Separation Logic Foundations: Hprop — Heap Predicates](https://softwarefoundations.cis.upenn.edu/slf-current/Hprop.html); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** JLS §4.3.1, reference identity and shared-state example; SLF Hprop, Description of Memory States

**sourceNote:** Combines reference/field observations with the existing finite HeapStore. Class tags, qualified fields, dangling-reference representation and partial dereference are explicit catalog profile choices.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-ObjectHeap-reference-equality"></a>

### reference-equality

`urn:csabs:operation/ObjectHeap-reference-equality`

**signature:** sameRef : Ref×Ref→Bool

**description:** Return true exactly when the tagged references are equal; sameRef(null,null)=true does not make null dereferenceable.

**precondition:** Typed inputs in the stated semantic profile.

**postcondition:** Return true exactly when the tagged references are equal; sameRef(null,null)=true does not make null dereferenceable.

**totality:** Total mathematical operation.

**source:** [Java Language Specification, Java SE 25, §4.3.1 Objects](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html#jls-4.3.1); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference; [Software Foundations, Separation Logic Foundations: Hprop — Heap Predicates](https://softwarefoundations.cis.upenn.edu/slf-current/Hprop.html); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** JLS §4.3.1, reference identity and shared-state example; SLF Hprop, Description of Memory States

**sourceNote:** Combines reference/field observations with the existing finite HeapStore. Class tags, qualified fields, dangling-reference representation and partial dereference are explicit catalog profile choices.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-ObjectHeap-aliases"></a>

### aliases

`urn:csabs:operation/ObjectHeap-aliases`

**signature:** aliases : H×Ref×Ref→Prop

**description:** aliases(h,r,s) iff ∃a∈dom(h), r=a ∧ s=a; null/null and equal dangling references do not alias an allocated object.

**precondition:** Typed inputs in the stated semantic profile.

**postcondition:** aliases(h,r,s) iff ∃a∈dom(h), r=a ∧ s=a; null/null and equal dangling references do not alias an allocated object.

**totality:** Total mathematical operation.

**source:** [Java Language Specification, Java SE 25, §4.3.1 Objects](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html#jls-4.3.1); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference; [Software Foundations, Separation Logic Foundations: Hprop — Heap Predicates](https://softwarefoundations.cis.upenn.edu/slf-current/Hprop.html); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** JLS §4.3.1, reference identity and shared-state example; SLF Hprop, Description of Memory States

**sourceNote:** Combines reference/field observations with the existing finite HeapStore. Class tags, qualified fields, dangling-reference representation and partial dereference are explicit catalog profile choices.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-ObjectHeap-object-record"></a>

### object-record

`urn:csabs:axiom/ObjectHeap-object-record`

**statement:** Every h is a finite address map of pairs (C,F) with finite field maps F; h=k iff all allocated-cell lookups agree.

**formalStatement:** Every h is a finite address map of pairs (C,F) with finite field maps F; h=k iff all allocated-cell lookups agree.

**assumptions:** Sequential mathematical snapshots. Primitive, Class and Field are fixed carriers; fields use declaring-class-qualified identifiers, so field hiding is not dynamic dispatch. Ref equality is tagged identity; heap equality is extensional. Null is not an address. Dangling references are representable but cannot be dereferenced. No type safety, access control, ownership, constructor protocol, GC, pointer arithmetic or concurrency is inferred. Inherited raw heap replacement/free may change tags or leave dangling references; class-stable updates are the field operations below.; Variables have the carriers declared in the notation and operation signatures.

**reviewStatus:** Editorial mathematical statement; no compiled witness asserted by this record.

**notationLanguage:** informal mathematical Unicode

**source:** [Java Language Specification, Java SE 25, §4.3.1 Objects](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html#jls-4.3.1); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference; [Software Foundations, Separation Logic Foundations: Hprop — Heap Predicates](https://softwarefoundations.cis.upenn.edu/slf-current/Hprop.html); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** JLS §4.3.1, reference identity and shared-state example; SLF Hprop, Description of Memory States

**sourceNote:** Combines reference/field observations with the existing finite HeapStore. Class tags, qualified fields, dangling-reference representation and partial dereference are explicit catalog profile choices.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-ObjectHeap-field-update"></a>

### field-update

`urn:csabs:axiom/ObjectHeap-field-update`

**statement:** h(a)=(C,F) ∧ f∈dom(F) ⇒ writeField(h,a,f,v)=h[a↦(C,F[f↦v])]; readField(h,a,f)=F(f).

**formalStatement:** h(a)=(C,F) ∧ f∈dom(F) ⇒ writeField(h,a,f,v)=h[a↦(C,F[f↦v])]; readField(h,a,f)=F(f).

**assumptions:** Sequential mathematical snapshots. Primitive, Class and Field are fixed carriers; fields use declaring-class-qualified identifiers, so field hiding is not dynamic dispatch. Ref equality is tagged identity; heap equality is extensional. Null is not an address. Dangling references are representable but cannot be dereferenced. No type safety, access control, ownership, constructor protocol, GC, pointer arithmetic or concurrency is inferred. Inherited raw heap replacement/free may change tags or leave dangling references; class-stable updates are the field operations below.; Variables have the carriers declared in the notation and operation signatures.

**reviewStatus:** Editorial mathematical statement; no compiled witness asserted by this record.

**notationLanguage:** informal mathematical Unicode

**source:** [Java Language Specification, Java SE 25, §4.3.1 Objects](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html#jls-4.3.1); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference; [Software Foundations, Separation Logic Foundations: Hprop — Heap Predicates](https://softwarefoundations.cis.upenn.edu/slf-current/Hprop.html); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** JLS §4.3.1, reference identity and shared-state example; SLF Hprop, Description of Memory States

**sourceNote:** Combines reference/field observations with the existing finite HeapStore. Class tags, qualified fields, dangling-reference representation and partial dereference are explicit catalog profile choices.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-ObjectHeap-reference-identity"></a>

### reference-identity

`urn:csabs:axiom/ObjectHeap-reference-identity`

**statement:** sameRef(r,s)=true ⇔ r=s as tagged references; aliases(h,r,s) ⇔ ∃a∈dom(h), r=a ∧ s=a. Contents equality does not identify distinct addresses.

**formalStatement:** sameRef(r,s)=true ⇔ r=s as tagged references; aliases(h,r,s) ⇔ ∃a∈dom(h), r=a ∧ s=a. Contents equality does not identify distinct addresses.

**assumptions:** Sequential mathematical snapshots. Primitive, Class and Field are fixed carriers; fields use declaring-class-qualified identifiers, so field hiding is not dynamic dispatch. Ref equality is tagged identity; heap equality is extensional. Null is not an address. Dangling references are representable but cannot be dereferenced. No type safety, access control, ownership, constructor protocol, GC, pointer arithmetic or concurrency is inferred. Inherited raw heap replacement/free may change tags or leave dangling references; class-stable updates are the field operations below.; Variables have the carriers declared in the notation and operation signatures.

**reviewStatus:** Editorial mathematical statement; no compiled witness asserted by this record.

**notationLanguage:** informal mathematical Unicode

**source:** [Java Language Specification, Java SE 25, §4.3.1 Objects](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html#jls-4.3.1); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference; [Software Foundations, Separation Logic Foundations: Hprop — Heap Predicates](https://softwarefoundations.cis.upenn.edu/slf-current/Hprop.html); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** JLS §4.3.1, reference identity and shared-state example; SLF Hprop, Description of Memory States

**sourceNote:** Combines reference/field observations with the existing finite HeapStore. Class tags, qualified fields, dangling-reference representation and partial dereference are explicit catalog profile choices.

**provenanceKind:** adapted

**ruleRole:** defining-rule

## Laws

<a id="node-urn-csabs-law-ObjectHeap-alias-observes-write"></a>

### alias-observes-write

`urn:csabs:law/ObjectHeap-alias-observes-write`

**statement:** aliases(h,r,s) ∧ readField(h,r,f) defined ⇒ readField(writeField(h,r,f,v),s,f)=v.

**formalStatement:** aliases(h,r,s) ∧ readField(h,r,f) defined ⇒ readField(writeField(h,r,f,v),s,f)=v.

**assumptions:** Sequential mathematical snapshots. Primitive, Class and Field are fixed carriers; fields use declaring-class-qualified identifiers, so field hiding is not dynamic dispatch. Ref equality is tagged identity; heap equality is extensional. Null is not an address. Dangling references are representable but cannot be dereferenced. No type safety, access control, ownership, constructor protocol, GC, pointer arithmetic or concurrency is inferred. Inherited raw heap replacement/free may change tags or leave dangling references; class-stable updates are the field operations below.; Variables have the carriers declared in the notation and operation signatures.

**reviewStatus:** Editorial mathematical statement; no compiled witness asserted by this record.

**notationLanguage:** informal mathematical Unicode

**source:** [Java Language Specification, Java SE 25, §4.3.1 Objects](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html#jls-4.3.1); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference; [Software Foundations, Separation Logic Foundations: Hprop — Heap Predicates](https://softwarefoundations.cis.upenn.edu/slf-current/Hprop.html); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** JLS §4.3.1, reference identity and shared-state example; SLF Hprop, Description of Memory States

**sourceNote:** Catalog derivation from the linked premises in this explicitly scoped model; the cited source supplies the underlying definitions. This is not a claim of executable proof.

**provenanceKind:** derived

**dependsOn:** [field-update](ObjectHeap.md#node-urn-csabs-axiom-ObjectHeap-field-update); [reference-identity](ObjectHeap.md#node-urn-csabs-axiom-ObjectHeap-reference-identity)

**proofSketch:** Expand aliases to the common allocated address a, then evaluate the field-update equation at a,f.

<a id="node-urn-csabs-law-ObjectHeap-other-field-frame"></a>

### other-field-frame

`urn:csabs:law/ObjectHeap-other-field-frame`

**statement:** writeField(h,a,f,v) defined ∧ (b,g)≠(a,f) ∧ readField(h,b,g) defined ⇒ readField(writeField(h,a,f,v),b,g)=readField(h,b,g).

**formalStatement:** writeField(h,a,f,v) defined ∧ (b,g)≠(a,f) ∧ readField(h,b,g) defined ⇒ readField(writeField(h,a,f,v),b,g)=readField(h,b,g).

**assumptions:** Sequential mathematical snapshots. Primitive, Class and Field are fixed carriers; fields use declaring-class-qualified identifiers, so field hiding is not dynamic dispatch. Ref equality is tagged identity; heap equality is extensional. Null is not an address. Dangling references are representable but cannot be dereferenced. No type safety, access control, ownership, constructor protocol, GC, pointer arithmetic or concurrency is inferred. Inherited raw heap replacement/free may change tags or leave dangling references; class-stable updates are the field operations below.; Variables have the carriers declared in the notation and operation signatures.

**reviewStatus:** Editorial mathematical statement; no compiled witness asserted by this record.

**notationLanguage:** informal mathematical Unicode

**source:** [Java Language Specification, Java SE 25, §4.3.1 Objects](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html#jls-4.3.1); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference; [Software Foundations, Separation Logic Foundations: Hprop — Heap Predicates](https://softwarefoundations.cis.upenn.edu/slf-current/Hprop.html); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** JLS §4.3.1, reference identity and shared-state example; SLF Hprop, Description of Memory States

**sourceNote:** Catalog derivation from the linked premises in this explicitly scoped model; the cited source supplies the underlying definitions. This is not a claim of executable proof.

**provenanceKind:** derived

**dependsOn:** [field-update](ObjectHeap.md#node-urn-csabs-axiom-ObjectHeap-field-update)

**proofSketch:** If b differs from a the object record is unchanged; otherwise g differs from f and finite-map update preserves that entry.

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [Java Language Specification, Java SE 25, §4.3.1 Objects](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html#jls-4.3.1); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference
- [Software Foundations, Separation Logic Foundations: Hprop — Heap Predicates](https://softwarefoundations.cis.upenn.edu/slf-current/Hprop.html); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** JLS §4.3.1, reference identity and shared-state example; SLF Hprop, Description of Memory States

**sourceNote:** Combines reference/field observations with the existing finite HeapStore. Class tags, qualified fields, dangling-reference representation and partial dereference are explicit catalog profile choices.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/ObjectHeap",
    "type": "Concept",
    "shortForm": "ObjectHeap",
    "fullName": "Sequential object heap with reference identity",
    "category": [
      "urn:csabs:category/object-oriented-semantics"
    ],
    "kind": "urn:csabs:kind/abstract-data-type",
    "definition": "A finite allocated heap whose cells contain class tags and finite field maps; references identify cells independently of their stored values and may alias.",
    "notation": "Addr=ℕ>0; Ref={null}⊎Addr; Value=Primitive⊎Ref; Obj=Class×(Field⇀fin Value); H=HeapStore(Obj)",
    "requiresConcept": [
      "urn:csabs:concept/HeapStore",
      "urn:csabs:concept/Map",
      "urn:csabs:concept/OptionType"
    ],
    "relatedConcept": [
      "urn:csabs:concept/ClassTable",
      "urn:csabs:concept/HeapSeparation"
    ],
    "hasOperation": [
      "urn:csabs:operation/ObjectHeap-class-of",
      "urn:csabs:operation/ObjectHeap-read-field",
      "urn:csabs:operation/ObjectHeap-write-field",
      "urn:csabs:operation/ObjectHeap-reference-equality",
      "urn:csabs:operation/ObjectHeap-aliases"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/ObjectHeap-object-record",
      "urn:csabs:axiom/ObjectHeap-field-update",
      "urn:csabs:axiom/ObjectHeap-reference-identity"
    ],
    "hasLaw": [
      "urn:csabs:law/ObjectHeap-alias-observes-write",
      "urn:csabs:law/ObjectHeap-other-field-frame"
    ],
    "hasTheorem": [],
    "basisKind": "extensional-structural-definition",
    "basisScope": "Sequential mathematical snapshots. Primitive, Class and Field are fixed carriers; fields use declaring-class-qualified identifiers, so field hiding is not dynamic dispatch. Ref equality is tagged identity; heap equality is extensional. Null is not an address. Dangling references are representable but cannot be dereferenced. No type safety, access control, ownership, constructor protocol, GC, pointer arithmetic or concurrency is inferred. Inherited raw heap replacement/free may change tags or leave dangling references; class-stable updates are the field operations below.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source and interface review; Lean model bindings and individual proof witnesses are separate.",
    "verificationObligation": [
      "Instantiate carriers, equality, definedness and the stated semantic profile before using these records.",
      "Catalog validation checks structure, not source entailment or target implementation conformance."
    ],
    "source": [
      "urn:csabs:source/oop-jls25-objects",
      "urn:csabs:source/oop-slf-separation"
    ],
    "sourceLocator": "JLS §4.3.1, reference identity and shared-state example; SLF Hprop, Description of Memory States",
    "sourceNote": "Combines reference/field observations with the existing finite HeapStore. Class tags, qualified fields, dangling-reference representation and partial dereference are explicit catalog profile choices.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/HeapStore"
    ],
    "specializationNote": "Instantiate HeapStore value carrier V with Obj=Class×Map(Field,Value), using the same positive addresses, extensional heap equality and read/write/free/fresh-allocation operations. Field observers/updates are additional operations; references are values, not separate heap cells. Raw inherited operations retain their original definedness.",
    "axiomBasis": "Selected defining rules: Every h is a finite address map of pairs (C,F) with finite field maps F; h=k iff all allocated-cell lookups agree. h(a)=(C,F) ∧ f∈dom(F) ⇒ writeField(h,a,f,v)=h[a↦(C,F[f↦v])]; readField(h,a,f)=F(f). sameRef(r,s)=true ⇔ r=s as tagged references; aliases(h,r,s) ⇔ ∃a∈dom(h), r=a ∧ s=a. Contents equality does not identify distinct addresses."
  },
  {
    "id": "urn:csabs:operation/ObjectHeap-class-of",
    "type": "Operation",
    "name": "class-of",
    "signature": "classOf : H×Ref⇀Class",
    "description": "For allocated a, classOf(h,a)=h(a).class; null or an absent address is undefined.",
    "concept": "urn:csabs:concept/ObjectHeap",
    "precondition": "Reference is nonnull and allocated.",
    "postcondition": "For allocated a, classOf(h,a)=h(a).class; null or an absent address is undefined.",
    "totality": "Partial; null/absent reference is undefined.",
    "source": [
      "urn:csabs:source/oop-jls25-objects",
      "urn:csabs:source/oop-slf-separation"
    ],
    "sourceLocator": "JLS §4.3.1, reference identity and shared-state example; SLF Hprop, Description of Memory States",
    "sourceNote": "Combines reference/field observations with the existing finite HeapStore. Class tags, qualified fields, dangling-reference representation and partial dereference are explicit catalog profile choices.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/ObjectHeap-read-field",
    "type": "Operation",
    "name": "read-field",
    "signature": "readField : H×Ref×Field⇀Value",
    "description": "For h(a)=(C,F) and f∈dom(F), return F(f).",
    "concept": "urn:csabs:concept/ObjectHeap",
    "precondition": "Reference is nonnull and allocated, and its record contains f.",
    "postcondition": "For h(a)=(C,F) and f∈dom(F), return F(f).",
    "totality": "Partial exactly outside the precondition.",
    "source": [
      "urn:csabs:source/oop-jls25-objects",
      "urn:csabs:source/oop-slf-separation"
    ],
    "sourceLocator": "JLS §4.3.1, reference identity and shared-state example; SLF Hprop, Description of Memory States",
    "sourceNote": "Combines reference/field observations with the existing finite HeapStore. Class tags, qualified fields, dangling-reference representation and partial dereference are explicit catalog profile choices.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/ObjectHeap-write-field",
    "type": "Operation",
    "name": "write-field",
    "signature": "writeField : H×Ref×Field×Value⇀H",
    "description": "Replace only the existing field f at a by v, retaining its class tag, all other fields and all other objects.",
    "concept": "urn:csabs:concept/ObjectHeap",
    "precondition": "Reference is nonnull and allocated, and its record contains f.",
    "postcondition": "Replace only the existing field f at a by v, retaining its class tag, all other fields and all other objects.",
    "totality": "Partial exactly outside the precondition.",
    "source": [
      "urn:csabs:source/oop-jls25-objects",
      "urn:csabs:source/oop-slf-separation"
    ],
    "sourceLocator": "JLS §4.3.1, reference identity and shared-state example; SLF Hprop, Description of Memory States",
    "sourceNote": "Combines reference/field observations with the existing finite HeapStore. Class tags, qualified fields, dangling-reference representation and partial dereference are explicit catalog profile choices.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/ObjectHeap-reference-equality",
    "type": "Operation",
    "name": "reference-equality",
    "signature": "sameRef : Ref×Ref→Bool",
    "description": "Return true exactly when the tagged references are equal; sameRef(null,null)=true does not make null dereferenceable.",
    "concept": "urn:csabs:concept/ObjectHeap",
    "precondition": "Typed inputs in the stated semantic profile.",
    "postcondition": "Return true exactly when the tagged references are equal; sameRef(null,null)=true does not make null dereferenceable.",
    "totality": "Total mathematical operation.",
    "source": [
      "urn:csabs:source/oop-jls25-objects",
      "urn:csabs:source/oop-slf-separation"
    ],
    "sourceLocator": "JLS §4.3.1, reference identity and shared-state example; SLF Hprop, Description of Memory States",
    "sourceNote": "Combines reference/field observations with the existing finite HeapStore. Class tags, qualified fields, dangling-reference representation and partial dereference are explicit catalog profile choices.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/ObjectHeap-aliases",
    "type": "Operation",
    "name": "aliases",
    "signature": "aliases : H×Ref×Ref→Prop",
    "description": "aliases(h,r,s) iff ∃a∈dom(h), r=a ∧ s=a; null/null and equal dangling references do not alias an allocated object.",
    "concept": "urn:csabs:concept/ObjectHeap",
    "precondition": "Typed inputs in the stated semantic profile.",
    "postcondition": "aliases(h,r,s) iff ∃a∈dom(h), r=a ∧ s=a; null/null and equal dangling references do not alias an allocated object.",
    "totality": "Total mathematical operation.",
    "source": [
      "urn:csabs:source/oop-jls25-objects",
      "urn:csabs:source/oop-slf-separation"
    ],
    "sourceLocator": "JLS §4.3.1, reference identity and shared-state example; SLF Hprop, Description of Memory States",
    "sourceNote": "Combines reference/field observations with the existing finite HeapStore. Class tags, qualified fields, dangling-reference representation and partial dereference are explicit catalog profile choices.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/ObjectHeap-object-record",
    "type": "Axiom",
    "name": "object-record",
    "statement": "Every h is a finite address map of pairs (C,F) with finite field maps F; h=k iff all allocated-cell lookups agree.",
    "formalStatement": "Every h is a finite address map of pairs (C,F) with finite field maps F; h=k iff all allocated-cell lookups agree.",
    "assumptions": [
      "Sequential mathematical snapshots. Primitive, Class and Field are fixed carriers; fields use declaring-class-qualified identifiers, so field hiding is not dynamic dispatch. Ref equality is tagged identity; heap equality is extensional. Null is not an address. Dangling references are representable but cannot be dereferenced. No type safety, access control, ownership, constructor protocol, GC, pointer arithmetic or concurrency is inferred. Inherited raw heap replacement/free may change tags or leave dangling references; class-stable updates are the field operations below.",
      "Variables have the carriers declared in the notation and operation signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/ObjectHeap"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled witness asserted by this record.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/oop-jls25-objects",
      "urn:csabs:source/oop-slf-separation"
    ],
    "sourceLocator": "JLS §4.3.1, reference identity and shared-state example; SLF Hprop, Description of Memory States",
    "sourceNote": "Combines reference/field observations with the existing finite HeapStore. Class tags, qualified fields, dangling-reference representation and partial dereference are explicit catalog profile choices.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/ObjectHeap-field-update",
    "type": "Axiom",
    "name": "field-update",
    "statement": "h(a)=(C,F) ∧ f∈dom(F) ⇒ writeField(h,a,f,v)=h[a↦(C,F[f↦v])]; readField(h,a,f)=F(f).",
    "formalStatement": "h(a)=(C,F) ∧ f∈dom(F) ⇒ writeField(h,a,f,v)=h[a↦(C,F[f↦v])]; readField(h,a,f)=F(f).",
    "assumptions": [
      "Sequential mathematical snapshots. Primitive, Class and Field are fixed carriers; fields use declaring-class-qualified identifiers, so field hiding is not dynamic dispatch. Ref equality is tagged identity; heap equality is extensional. Null is not an address. Dangling references are representable but cannot be dereferenced. No type safety, access control, ownership, constructor protocol, GC, pointer arithmetic or concurrency is inferred. Inherited raw heap replacement/free may change tags or leave dangling references; class-stable updates are the field operations below.",
      "Variables have the carriers declared in the notation and operation signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/ObjectHeap"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled witness asserted by this record.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/oop-jls25-objects",
      "urn:csabs:source/oop-slf-separation"
    ],
    "sourceLocator": "JLS §4.3.1, reference identity and shared-state example; SLF Hprop, Description of Memory States",
    "sourceNote": "Combines reference/field observations with the existing finite HeapStore. Class tags, qualified fields, dangling-reference representation and partial dereference are explicit catalog profile choices.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/ObjectHeap-reference-identity",
    "type": "Axiom",
    "name": "reference-identity",
    "statement": "sameRef(r,s)=true ⇔ r=s as tagged references; aliases(h,r,s) ⇔ ∃a∈dom(h), r=a ∧ s=a. Contents equality does not identify distinct addresses.",
    "formalStatement": "sameRef(r,s)=true ⇔ r=s as tagged references; aliases(h,r,s) ⇔ ∃a∈dom(h), r=a ∧ s=a. Contents equality does not identify distinct addresses.",
    "assumptions": [
      "Sequential mathematical snapshots. Primitive, Class and Field are fixed carriers; fields use declaring-class-qualified identifiers, so field hiding is not dynamic dispatch. Ref equality is tagged identity; heap equality is extensional. Null is not an address. Dangling references are representable but cannot be dereferenced. No type safety, access control, ownership, constructor protocol, GC, pointer arithmetic or concurrency is inferred. Inherited raw heap replacement/free may change tags or leave dangling references; class-stable updates are the field operations below.",
      "Variables have the carriers declared in the notation and operation signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/ObjectHeap"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled witness asserted by this record.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/oop-jls25-objects",
      "urn:csabs:source/oop-slf-separation"
    ],
    "sourceLocator": "JLS §4.3.1, reference identity and shared-state example; SLF Hprop, Description of Memory States",
    "sourceNote": "Combines reference/field observations with the existing finite HeapStore. Class tags, qualified fields, dangling-reference representation and partial dereference are explicit catalog profile choices.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:law/ObjectHeap-alias-observes-write",
    "type": "Law",
    "name": "alias-observes-write",
    "statement": "aliases(h,r,s) ∧ readField(h,r,f) defined ⇒ readField(writeField(h,r,f,v),s,f)=v.",
    "formalStatement": "aliases(h,r,s) ∧ readField(h,r,f) defined ⇒ readField(writeField(h,r,f,v),s,f)=v.",
    "assumptions": [
      "Sequential mathematical snapshots. Primitive, Class and Field are fixed carriers; fields use declaring-class-qualified identifiers, so field hiding is not dynamic dispatch. Ref equality is tagged identity; heap equality is extensional. Null is not an address. Dangling references are representable but cannot be dereferenced. No type safety, access control, ownership, constructor protocol, GC, pointer arithmetic or concurrency is inferred. Inherited raw heap replacement/free may change tags or leave dangling references; class-stable updates are the field operations below.",
      "Variables have the carriers declared in the notation and operation signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/ObjectHeap"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled witness asserted by this record.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/oop-jls25-objects",
      "urn:csabs:source/oop-slf-separation"
    ],
    "sourceLocator": "JLS §4.3.1, reference identity and shared-state example; SLF Hprop, Description of Memory States",
    "sourceNote": "Catalog derivation from the linked premises in this explicitly scoped model; the cited source supplies the underlying definitions. This is not a claim of executable proof.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/ObjectHeap-field-update",
      "urn:csabs:axiom/ObjectHeap-reference-identity"
    ],
    "proofSketch": "Expand aliases to the common allocated address a, then evaluate the field-update equation at a,f."
  },
  {
    "id": "urn:csabs:law/ObjectHeap-other-field-frame",
    "type": "Law",
    "name": "other-field-frame",
    "statement": "writeField(h,a,f,v) defined ∧ (b,g)≠(a,f) ∧ readField(h,b,g) defined ⇒ readField(writeField(h,a,f,v),b,g)=readField(h,b,g).",
    "formalStatement": "writeField(h,a,f,v) defined ∧ (b,g)≠(a,f) ∧ readField(h,b,g) defined ⇒ readField(writeField(h,a,f,v),b,g)=readField(h,b,g).",
    "assumptions": [
      "Sequential mathematical snapshots. Primitive, Class and Field are fixed carriers; fields use declaring-class-qualified identifiers, so field hiding is not dynamic dispatch. Ref equality is tagged identity; heap equality is extensional. Null is not an address. Dangling references are representable but cannot be dereferenced. No type safety, access control, ownership, constructor protocol, GC, pointer arithmetic or concurrency is inferred. Inherited raw heap replacement/free may change tags or leave dangling references; class-stable updates are the field operations below.",
      "Variables have the carriers declared in the notation and operation signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/ObjectHeap"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled witness asserted by this record.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/oop-jls25-objects",
      "urn:csabs:source/oop-slf-separation"
    ],
    "sourceLocator": "JLS §4.3.1, reference identity and shared-state example; SLF Hprop, Description of Memory States",
    "sourceNote": "Catalog derivation from the linked premises in this explicitly scoped model; the cited source supplies the underlying definitions. This is not a claim of executable proof.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/ObjectHeap-field-update"
    ],
    "proofSketch": "If b differs from a the object record is unchanged; otherwise g differs from f and finite-map update preserves that entry."
  }
]
```
<!-- graph-record:end -->
