# Exclusive finite-heap separation predicates

Predicates over finite heap fragments with exact empty/singleton assertions and separating conjunction interpreted by disjoint heap union.

**Notation:** Heap=HeapStore(V); HProp=Heap→Prop; h₁⊥h₂ iff dom(h₁)∩dom(h₂)=∅; (P∗Q)(h) iff ∃h₁⊥h₂, h=h₁⊎h₂ ∧ P(h₁) ∧ Q(h₂)

**Stable ID:** `urn:csabs:concept/HeapSeparation`

**Categories:** Programming-language semantics → Object-oriented semantics

**Kind:** semantic-model

**Prerequisites:** [Finite allocated heap store](HeapStore.md), [Predicate Logic](PredicateLogic.md)

**Related concepts:** [Sequential object heap with reference identity](ObjectHeap.md), [Relational method contract with write effects](MethodContract.md), [Monoid](Monoid.md)

## Backlinks

- [Sequential object heap with reference identity](ObjectHeap.md) — `relatedConcept`
- [Visible-state object invariant protocol](ObjectInvariant.md) — `relatedConcept`

## Interface and scope

**axiomBasis:** Selected defining rules: h₁⊥h₂ ⇔ dom(h₁)∩dom(h₂)=∅; merge is defined exactly then and has the union of their lookups. emp(h) ⇔ dom(h)=∅; (a↦v)(h) ⇔ dom(h)={a} ∧ h(a)=v. (P∗Q)(h) ⇔ ∃h₁,h₂, h₁⊥h₂ ∧ h=h₁⊎h₂ ∧ P(h₁) ∧ Q(h₂); predicate equality means pointwise logical equivalence.

**basisKind:** extensional-structural-definition

**basisScope:** Classical extensional predicates over finite positive-address heap fragments. Points-to owns exactly one whole cell; using ObjectHeap records therefore separates objects, not individual fields. Disjointness concerns allocated domains, not pointer reachability: stored references may point into another fragment. Exclusive ownership assertions do not forbid alias references. No fractional permissions, borrowing, magic wand, concurrency rule or general frame rule is included. A frame rule additionally needs a local operational semantics; disjointness alone is insufficient.

**verificationObligation:** Instantiate carriers, equality, definedness and the stated semantic profile before using these records.; Catalog validation checks structure, not source entailment or target implementation conformance.

**reviewStatus:** Editorial source and interface review; Lean model bindings and individual proof witnesses are separate.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-HeapSeparation-disjoint"></a>

### disjoint

`urn:csabs:operation/HeapSeparation-disjoint`

**signature:** disjoint : Heap×Heap→Prop

**description:** disjoint(h₁,h₂) iff no address is allocated in both heaps.

**precondition:** Typed inputs in the stated semantic profile.

**postcondition:** disjoint(h₁,h₂) iff no address is allocated in both heaps.

**totality:** Total mathematical operation.

**source:** [Software Foundations, Separation Logic Foundations: Hprop — Heap Predicates](https://softwarefoundations.cis.upenn.edu/slf-current/Hprop.html); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** Hprop: Description of Memory States; Heap Predicates (hempty, hsingle, hstar); Fundamental Properties of Operators

**sourceNote:** Uses the existing HeapStore address convention and exact heap-fragment assertions. Ownership is logical permission to a cell, not absence of aliases or an automatic encapsulation guarantee.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-HeapSeparation-merge"></a>

### merge

`urn:csabs:operation/HeapSeparation-merge`

**signature:** merge : Heap×Heap⇀Heap

**description:** For disjoint heaps return their extensional union.

**precondition:** The two allocated domains are disjoint.

**postcondition:** For disjoint heaps return their extensional union.

**totality:** Partial; overlapping heaps are undefined even if their overlapping values agree.

**source:** [Software Foundations, Separation Logic Foundations: Hprop — Heap Predicates](https://softwarefoundations.cis.upenn.edu/slf-current/Hprop.html); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** Hprop: Description of Memory States; Heap Predicates (hempty, hsingle, hstar); Fundamental Properties of Operators

**sourceNote:** Uses the existing HeapStore address convention and exact heap-fragment assertions. Ownership is logical permission to a cell, not absence of aliases or an automatic encapsulation guarantee.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-HeapSeparation-emp"></a>

### emp

`urn:csabs:operation/HeapSeparation-emp`

**signature:** emp : HProp

**description:** emp(h) iff dom(h)=∅.

**precondition:** Typed inputs in the stated semantic profile.

**postcondition:** emp(h) iff dom(h)=∅.

**totality:** Total mathematical operation.

**source:** [Software Foundations, Separation Logic Foundations: Hprop — Heap Predicates](https://softwarefoundations.cis.upenn.edu/slf-current/Hprop.html); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** Hprop: Description of Memory States; Heap Predicates (hempty, hsingle, hstar); Fundamental Properties of Operators

**sourceNote:** Uses the existing HeapStore address convention and exact heap-fragment assertions. Ownership is logical permission to a cell, not absence of aliases or an automatic encapsulation guarantee.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-HeapSeparation-points-to"></a>

### points-to

`urn:csabs:operation/HeapSeparation-points-to`

**signature:** pointsTo : Addr×V→HProp

**description:** (a↦v)(h) iff dom(h)={a} and h(a)=v; additional cells do not satisfy this exact predicate.

**precondition:** Typed inputs in the stated semantic profile.

**postcondition:** (a↦v)(h) iff dom(h)={a} and h(a)=v; additional cells do not satisfy this exact predicate.

**totality:** Total mathematical operation.

**source:** [Software Foundations, Separation Logic Foundations: Hprop — Heap Predicates](https://softwarefoundations.cis.upenn.edu/slf-current/Hprop.html); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** Hprop: Description of Memory States; Heap Predicates (hempty, hsingle, hstar); Fundamental Properties of Operators

**sourceNote:** Uses the existing HeapStore address convention and exact heap-fragment assertions. Ownership is logical permission to a cell, not absence of aliases or an automatic encapsulation guarantee.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-HeapSeparation-star"></a>

### star

`urn:csabs:operation/HeapSeparation-star`

**signature:** star : HProp×HProp→HProp

**description:** (P∗Q)(h) iff ∃h₁,h₂, h₁⊥h₂ ∧ h=h₁⊎h₂ ∧ P(h₁) ∧ Q(h₂).

**precondition:** Typed inputs in the stated semantic profile.

**postcondition:** (P∗Q)(h) iff ∃h₁,h₂, h₁⊥h₂ ∧ h=h₁⊎h₂ ∧ P(h₁) ∧ Q(h₂).

**totality:** Total mathematical operation.

**source:** [Software Foundations, Separation Logic Foundations: Hprop — Heap Predicates](https://softwarefoundations.cis.upenn.edu/slf-current/Hprop.html); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** Hprop: Description of Memory States; Heap Predicates (hempty, hsingle, hstar); Fundamental Properties of Operators

**sourceNote:** Uses the existing HeapStore address convention and exact heap-fragment assertions. Ownership is logical permission to a cell, not absence of aliases or an automatic encapsulation guarantee.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-HeapSeparation-disjoint-union"></a>

### disjoint-union

`urn:csabs:axiom/HeapSeparation-disjoint-union`

**statement:** h₁⊥h₂ ⇔ dom(h₁)∩dom(h₂)=∅; merge is defined exactly then and has the union of their lookups.

**formalStatement:** h₁⊥h₂ ⇔ dom(h₁)∩dom(h₂)=∅; merge is defined exactly then and has the union of their lookups.

**assumptions:** Classical extensional predicates over finite positive-address heap fragments. Points-to owns exactly one whole cell; using ObjectHeap records therefore separates objects, not individual fields. Disjointness concerns allocated domains, not pointer reachability: stored references may point into another fragment. Exclusive ownership assertions do not forbid alias references. No fractional permissions, borrowing, magic wand, concurrency rule or general frame rule is included. A frame rule additionally needs a local operational semantics; disjointness alone is insufficient.; Variables have the carriers declared in the notation and operation signatures.

**reviewStatus:** Editorial mathematical statement; no compiled witness asserted by this record.

**notationLanguage:** informal mathematical Unicode

**source:** [Software Foundations, Separation Logic Foundations: Hprop — Heap Predicates](https://softwarefoundations.cis.upenn.edu/slf-current/Hprop.html); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** Hprop: Description of Memory States; Heap Predicates (hempty, hsingle, hstar); Fundamental Properties of Operators

**sourceNote:** Uses the existing HeapStore address convention and exact heap-fragment assertions. Ownership is logical permission to a cell, not absence of aliases or an automatic encapsulation guarantee.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-HeapSeparation-exact-atoms"></a>

### exact-atoms

`urn:csabs:axiom/HeapSeparation-exact-atoms`

**statement:** emp(h) ⇔ dom(h)=∅; (a↦v)(h) ⇔ dom(h)={a} ∧ h(a)=v.

**formalStatement:** emp(h) ⇔ dom(h)=∅; (a↦v)(h) ⇔ dom(h)={a} ∧ h(a)=v.

**assumptions:** Classical extensional predicates over finite positive-address heap fragments. Points-to owns exactly one whole cell; using ObjectHeap records therefore separates objects, not individual fields. Disjointness concerns allocated domains, not pointer reachability: stored references may point into another fragment. Exclusive ownership assertions do not forbid alias references. No fractional permissions, borrowing, magic wand, concurrency rule or general frame rule is included. A frame rule additionally needs a local operational semantics; disjointness alone is insufficient.; Variables have the carriers declared in the notation and operation signatures.

**reviewStatus:** Editorial mathematical statement; no compiled witness asserted by this record.

**notationLanguage:** informal mathematical Unicode

**source:** [Software Foundations, Separation Logic Foundations: Hprop — Heap Predicates](https://softwarefoundations.cis.upenn.edu/slf-current/Hprop.html); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** Hprop: Description of Memory States; Heap Predicates (hempty, hsingle, hstar); Fundamental Properties of Operators

**sourceNote:** Uses the existing HeapStore address convention and exact heap-fragment assertions. Ownership is logical permission to a cell, not absence of aliases or an automatic encapsulation guarantee.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-HeapSeparation-star-splitting"></a>

### star-splitting

`urn:csabs:axiom/HeapSeparation-star-splitting`

**statement:** (P∗Q)(h) ⇔ ∃h₁,h₂, h₁⊥h₂ ∧ h=h₁⊎h₂ ∧ P(h₁) ∧ Q(h₂); predicate equality means pointwise logical equivalence.

**formalStatement:** (P∗Q)(h) ⇔ ∃h₁,h₂, h₁⊥h₂ ∧ h=h₁⊎h₂ ∧ P(h₁) ∧ Q(h₂); predicate equality means pointwise logical equivalence.

**assumptions:** Classical extensional predicates over finite positive-address heap fragments. Points-to owns exactly one whole cell; using ObjectHeap records therefore separates objects, not individual fields. Disjointness concerns allocated domains, not pointer reachability: stored references may point into another fragment. Exclusive ownership assertions do not forbid alias references. No fractional permissions, borrowing, magic wand, concurrency rule or general frame rule is included. A frame rule additionally needs a local operational semantics; disjointness alone is insufficient.; Variables have the carriers declared in the notation and operation signatures.

**reviewStatus:** Editorial mathematical statement; no compiled witness asserted by this record.

**notationLanguage:** informal mathematical Unicode

**source:** [Software Foundations, Separation Logic Foundations: Hprop — Heap Predicates](https://softwarefoundations.cis.upenn.edu/slf-current/Hprop.html); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** Hprop: Description of Memory States; Heap Predicates (hempty, hsingle, hstar); Fundamental Properties of Operators

**sourceNote:** Uses the existing HeapStore address convention and exact heap-fragment assertions. Ownership is logical permission to a cell, not absence of aliases or an automatic encapsulation guarantee.

**provenanceKind:** adapted

**ruleRole:** defining-rule

## Laws

<a id="node-urn-csabs-law-HeapSeparation-star-commutative"></a>

### star-commutative

`urn:csabs:law/HeapSeparation-star-commutative`

**statement:** ∀h, (P∗Q)(h) ⇔ (Q∗P)(h).

**formalStatement:** ∀h, (P∗Q)(h) ⇔ (Q∗P)(h).

**assumptions:** Classical extensional predicates over finite positive-address heap fragments. Points-to owns exactly one whole cell; using ObjectHeap records therefore separates objects, not individual fields. Disjointness concerns allocated domains, not pointer reachability: stored references may point into another fragment. Exclusive ownership assertions do not forbid alias references. No fractional permissions, borrowing, magic wand, concurrency rule or general frame rule is included. A frame rule additionally needs a local operational semantics; disjointness alone is insufficient.; Variables have the carriers declared in the notation and operation signatures.

**reviewStatus:** Editorial mathematical statement; no compiled witness asserted by this record.

**notationLanguage:** informal mathematical Unicode

**source:** [Software Foundations, Separation Logic Foundations: Hprop — Heap Predicates](https://softwarefoundations.cis.upenn.edu/slf-current/Hprop.html); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** Hprop: Description of Memory States; Heap Predicates (hempty, hsingle, hstar); Fundamental Properties of Operators

**sourceNote:** Catalog derivation from the linked premises in this explicitly scoped model; the cited source supplies the underlying definitions. This is not a claim of executable proof.

**provenanceKind:** derived

**dependsOn:** [disjoint-union](HeapSeparation.md#node-urn-csabs-axiom-HeapSeparation-disjoint-union); [star-splitting](HeapSeparation.md#node-urn-csabs-axiom-HeapSeparation-star-splitting)

**proofSketch:** Swap the witnessing fragments; disjointness and union are symmetric on disjoint domains.

<a id="node-urn-csabs-law-HeapSeparation-star-empty-unit"></a>

### star-empty-unit

`urn:csabs:law/HeapSeparation-star-empty-unit`

**statement:** ∀h, (emp∗P)(h) ⇔ P(h).

**formalStatement:** ∀h, (emp∗P)(h) ⇔ P(h).

**assumptions:** Classical extensional predicates over finite positive-address heap fragments. Points-to owns exactly one whole cell; using ObjectHeap records therefore separates objects, not individual fields. Disjointness concerns allocated domains, not pointer reachability: stored references may point into another fragment. Exclusive ownership assertions do not forbid alias references. No fractional permissions, borrowing, magic wand, concurrency rule or general frame rule is included. A frame rule additionally needs a local operational semantics; disjointness alone is insufficient.; Variables have the carriers declared in the notation and operation signatures.

**reviewStatus:** Editorial mathematical statement; no compiled witness asserted by this record.

**notationLanguage:** informal mathematical Unicode

**source:** [Software Foundations, Separation Logic Foundations: Hprop — Heap Predicates](https://softwarefoundations.cis.upenn.edu/slf-current/Hprop.html); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** Hprop: Description of Memory States; Heap Predicates (hempty, hsingle, hstar); Fundamental Properties of Operators

**sourceNote:** Catalog derivation from the linked premises in this explicitly scoped model; the cited source supplies the underlying definitions. This is not a claim of executable proof.

**provenanceKind:** derived

**dependsOn:** [disjoint-union](HeapSeparation.md#node-urn-csabs-axiom-HeapSeparation-disjoint-union); [exact-atoms](HeapSeparation.md#node-urn-csabs-axiom-HeapSeparation-exact-atoms); [star-splitting](HeapSeparation.md#node-urn-csabs-axiom-HeapSeparation-star-splitting)

**proofSketch:** A satisfying empty fragment has empty domain, so its union leaves the other fragment unchanged. Conversely choose the empty heap and h.

<a id="node-urn-csabs-law-HeapSeparation-exclusive-points-to"></a>

### exclusive-points-to

`urn:csabs:law/HeapSeparation-exclusive-points-to`

**statement:** ∀a,v,w,h, ¬((a↦v)∗(a↦w))(h).

**formalStatement:** ∀a,v,w,h, ¬((a↦v)∗(a↦w))(h).

**assumptions:** Classical extensional predicates over finite positive-address heap fragments. Points-to owns exactly one whole cell; using ObjectHeap records therefore separates objects, not individual fields. Disjointness concerns allocated domains, not pointer reachability: stored references may point into another fragment. Exclusive ownership assertions do not forbid alias references. No fractional permissions, borrowing, magic wand, concurrency rule or general frame rule is included. A frame rule additionally needs a local operational semantics; disjointness alone is insufficient.; Variables have the carriers declared in the notation and operation signatures.

**reviewStatus:** Editorial mathematical statement; no compiled witness asserted by this record.

**notationLanguage:** informal mathematical Unicode

**source:** [Software Foundations, Separation Logic Foundations: Hprop — Heap Predicates](https://softwarefoundations.cis.upenn.edu/slf-current/Hprop.html); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** Hprop: Description of Memory States; Heap Predicates (hempty, hsingle, hstar); Fundamental Properties of Operators

**sourceNote:** Catalog derivation from the linked premises in this explicitly scoped model; the cited source supplies the underlying definitions. This is not a claim of executable proof.

**provenanceKind:** derived

**dependsOn:** [disjoint-union](HeapSeparation.md#node-urn-csabs-axiom-HeapSeparation-disjoint-union); [exact-atoms](HeapSeparation.md#node-urn-csabs-axiom-HeapSeparation-exact-atoms); [star-splitting](HeapSeparation.md#node-urn-csabs-axiom-HeapSeparation-star-splitting)

**proofSketch:** Both singleton fragments would allocate a, contradicting the required disjoint domains, even when v=w.

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [Software Foundations, Separation Logic Foundations: Hprop — Heap Predicates](https://softwarefoundations.cis.upenn.edu/slf-current/Hprop.html); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** Hprop: Description of Memory States; Heap Predicates (hempty, hsingle, hstar); Fundamental Properties of Operators

**sourceNote:** Uses the existing HeapStore address convention and exact heap-fragment assertions. Ownership is logical permission to a cell, not absence of aliases or an automatic encapsulation guarantee.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/HeapSeparation",
    "type": "Concept",
    "shortForm": "HeapSeparation",
    "fullName": "Exclusive finite-heap separation predicates",
    "category": [
      "urn:csabs:category/object-oriented-semantics"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "definition": "Predicates over finite heap fragments with exact empty/singleton assertions and separating conjunction interpreted by disjoint heap union.",
    "notation": "Heap=HeapStore(V); HProp=Heap→Prop; h₁⊥h₂ iff dom(h₁)∩dom(h₂)=∅; (P∗Q)(h) iff ∃h₁⊥h₂, h=h₁⊎h₂ ∧ P(h₁) ∧ Q(h₂)",
    "requiresConcept": [
      "urn:csabs:concept/HeapStore",
      "urn:csabs:concept/PredicateLogic"
    ],
    "relatedConcept": [
      "urn:csabs:concept/ObjectHeap",
      "urn:csabs:concept/MethodContract",
      "urn:csabs:concept/Monoid"
    ],
    "hasOperation": [
      "urn:csabs:operation/HeapSeparation-disjoint",
      "urn:csabs:operation/HeapSeparation-merge",
      "urn:csabs:operation/HeapSeparation-emp",
      "urn:csabs:operation/HeapSeparation-points-to",
      "urn:csabs:operation/HeapSeparation-star"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/HeapSeparation-disjoint-union",
      "urn:csabs:axiom/HeapSeparation-exact-atoms",
      "urn:csabs:axiom/HeapSeparation-star-splitting"
    ],
    "hasLaw": [
      "urn:csabs:law/HeapSeparation-star-commutative",
      "urn:csabs:law/HeapSeparation-star-empty-unit",
      "urn:csabs:law/HeapSeparation-exclusive-points-to"
    ],
    "hasTheorem": [],
    "basisKind": "extensional-structural-definition",
    "basisScope": "Classical extensional predicates over finite positive-address heap fragments. Points-to owns exactly one whole cell; using ObjectHeap records therefore separates objects, not individual fields. Disjointness concerns allocated domains, not pointer reachability: stored references may point into another fragment. Exclusive ownership assertions do not forbid alias references. No fractional permissions, borrowing, magic wand, concurrency rule or general frame rule is included. A frame rule additionally needs a local operational semantics; disjointness alone is insufficient.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source and interface review; Lean model bindings and individual proof witnesses are separate.",
    "verificationObligation": [
      "Instantiate carriers, equality, definedness and the stated semantic profile before using these records.",
      "Catalog validation checks structure, not source entailment or target implementation conformance."
    ],
    "source": [
      "urn:csabs:source/oop-slf-separation"
    ],
    "sourceLocator": "Hprop: Description of Memory States; Heap Predicates (hempty, hsingle, hstar); Fundamental Properties of Operators",
    "sourceNote": "Uses the existing HeapStore address convention and exact heap-fragment assertions. Ownership is logical permission to a cell, not absence of aliases or an automatic encapsulation guarantee.",
    "provenanceKind": "adapted",
    "axiomBasis": "Selected defining rules: h₁⊥h₂ ⇔ dom(h₁)∩dom(h₂)=∅; merge is defined exactly then and has the union of their lookups. emp(h) ⇔ dom(h)=∅; (a↦v)(h) ⇔ dom(h)={a} ∧ h(a)=v. (P∗Q)(h) ⇔ ∃h₁,h₂, h₁⊥h₂ ∧ h=h₁⊎h₂ ∧ P(h₁) ∧ Q(h₂); predicate equality means pointwise logical equivalence."
  },
  {
    "id": "urn:csabs:operation/HeapSeparation-disjoint",
    "type": "Operation",
    "name": "disjoint",
    "signature": "disjoint : Heap×Heap→Prop",
    "description": "disjoint(h₁,h₂) iff no address is allocated in both heaps.",
    "concept": "urn:csabs:concept/HeapSeparation",
    "precondition": "Typed inputs in the stated semantic profile.",
    "postcondition": "disjoint(h₁,h₂) iff no address is allocated in both heaps.",
    "totality": "Total mathematical operation.",
    "source": [
      "urn:csabs:source/oop-slf-separation"
    ],
    "sourceLocator": "Hprop: Description of Memory States; Heap Predicates (hempty, hsingle, hstar); Fundamental Properties of Operators",
    "sourceNote": "Uses the existing HeapStore address convention and exact heap-fragment assertions. Ownership is logical permission to a cell, not absence of aliases or an automatic encapsulation guarantee.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/HeapSeparation-merge",
    "type": "Operation",
    "name": "merge",
    "signature": "merge : Heap×Heap⇀Heap",
    "description": "For disjoint heaps return their extensional union.",
    "concept": "urn:csabs:concept/HeapSeparation",
    "precondition": "The two allocated domains are disjoint.",
    "postcondition": "For disjoint heaps return their extensional union.",
    "totality": "Partial; overlapping heaps are undefined even if their overlapping values agree.",
    "source": [
      "urn:csabs:source/oop-slf-separation"
    ],
    "sourceLocator": "Hprop: Description of Memory States; Heap Predicates (hempty, hsingle, hstar); Fundamental Properties of Operators",
    "sourceNote": "Uses the existing HeapStore address convention and exact heap-fragment assertions. Ownership is logical permission to a cell, not absence of aliases or an automatic encapsulation guarantee.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/HeapSeparation-emp",
    "type": "Operation",
    "name": "emp",
    "signature": "emp : HProp",
    "description": "emp(h) iff dom(h)=∅.",
    "concept": "urn:csabs:concept/HeapSeparation",
    "precondition": "Typed inputs in the stated semantic profile.",
    "postcondition": "emp(h) iff dom(h)=∅.",
    "totality": "Total mathematical operation.",
    "source": [
      "urn:csabs:source/oop-slf-separation"
    ],
    "sourceLocator": "Hprop: Description of Memory States; Heap Predicates (hempty, hsingle, hstar); Fundamental Properties of Operators",
    "sourceNote": "Uses the existing HeapStore address convention and exact heap-fragment assertions. Ownership is logical permission to a cell, not absence of aliases or an automatic encapsulation guarantee.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/HeapSeparation-points-to",
    "type": "Operation",
    "name": "points-to",
    "signature": "pointsTo : Addr×V→HProp",
    "description": "(a↦v)(h) iff dom(h)={a} and h(a)=v; additional cells do not satisfy this exact predicate.",
    "concept": "urn:csabs:concept/HeapSeparation",
    "precondition": "Typed inputs in the stated semantic profile.",
    "postcondition": "(a↦v)(h) iff dom(h)={a} and h(a)=v; additional cells do not satisfy this exact predicate.",
    "totality": "Total mathematical operation.",
    "source": [
      "urn:csabs:source/oop-slf-separation"
    ],
    "sourceLocator": "Hprop: Description of Memory States; Heap Predicates (hempty, hsingle, hstar); Fundamental Properties of Operators",
    "sourceNote": "Uses the existing HeapStore address convention and exact heap-fragment assertions. Ownership is logical permission to a cell, not absence of aliases or an automatic encapsulation guarantee.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/HeapSeparation-star",
    "type": "Operation",
    "name": "star",
    "signature": "star : HProp×HProp→HProp",
    "description": "(P∗Q)(h) iff ∃h₁,h₂, h₁⊥h₂ ∧ h=h₁⊎h₂ ∧ P(h₁) ∧ Q(h₂).",
    "concept": "urn:csabs:concept/HeapSeparation",
    "precondition": "Typed inputs in the stated semantic profile.",
    "postcondition": "(P∗Q)(h) iff ∃h₁,h₂, h₁⊥h₂ ∧ h=h₁⊎h₂ ∧ P(h₁) ∧ Q(h₂).",
    "totality": "Total mathematical operation.",
    "source": [
      "urn:csabs:source/oop-slf-separation"
    ],
    "sourceLocator": "Hprop: Description of Memory States; Heap Predicates (hempty, hsingle, hstar); Fundamental Properties of Operators",
    "sourceNote": "Uses the existing HeapStore address convention and exact heap-fragment assertions. Ownership is logical permission to a cell, not absence of aliases or an automatic encapsulation guarantee.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/HeapSeparation-disjoint-union",
    "type": "Axiom",
    "name": "disjoint-union",
    "statement": "h₁⊥h₂ ⇔ dom(h₁)∩dom(h₂)=∅; merge is defined exactly then and has the union of their lookups.",
    "formalStatement": "h₁⊥h₂ ⇔ dom(h₁)∩dom(h₂)=∅; merge is defined exactly then and has the union of their lookups.",
    "assumptions": [
      "Classical extensional predicates over finite positive-address heap fragments. Points-to owns exactly one whole cell; using ObjectHeap records therefore separates objects, not individual fields. Disjointness concerns allocated domains, not pointer reachability: stored references may point into another fragment. Exclusive ownership assertions do not forbid alias references. No fractional permissions, borrowing, magic wand, concurrency rule or general frame rule is included. A frame rule additionally needs a local operational semantics; disjointness alone is insufficient.",
      "Variables have the carriers declared in the notation and operation signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/HeapSeparation"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled witness asserted by this record.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/oop-slf-separation"
    ],
    "sourceLocator": "Hprop: Description of Memory States; Heap Predicates (hempty, hsingle, hstar); Fundamental Properties of Operators",
    "sourceNote": "Uses the existing HeapStore address convention and exact heap-fragment assertions. Ownership is logical permission to a cell, not absence of aliases or an automatic encapsulation guarantee.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/HeapSeparation-exact-atoms",
    "type": "Axiom",
    "name": "exact-atoms",
    "statement": "emp(h) ⇔ dom(h)=∅; (a↦v)(h) ⇔ dom(h)={a} ∧ h(a)=v.",
    "formalStatement": "emp(h) ⇔ dom(h)=∅; (a↦v)(h) ⇔ dom(h)={a} ∧ h(a)=v.",
    "assumptions": [
      "Classical extensional predicates over finite positive-address heap fragments. Points-to owns exactly one whole cell; using ObjectHeap records therefore separates objects, not individual fields. Disjointness concerns allocated domains, not pointer reachability: stored references may point into another fragment. Exclusive ownership assertions do not forbid alias references. No fractional permissions, borrowing, magic wand, concurrency rule or general frame rule is included. A frame rule additionally needs a local operational semantics; disjointness alone is insufficient.",
      "Variables have the carriers declared in the notation and operation signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/HeapSeparation"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled witness asserted by this record.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/oop-slf-separation"
    ],
    "sourceLocator": "Hprop: Description of Memory States; Heap Predicates (hempty, hsingle, hstar); Fundamental Properties of Operators",
    "sourceNote": "Uses the existing HeapStore address convention and exact heap-fragment assertions. Ownership is logical permission to a cell, not absence of aliases or an automatic encapsulation guarantee.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/HeapSeparation-star-splitting",
    "type": "Axiom",
    "name": "star-splitting",
    "statement": "(P∗Q)(h) ⇔ ∃h₁,h₂, h₁⊥h₂ ∧ h=h₁⊎h₂ ∧ P(h₁) ∧ Q(h₂); predicate equality means pointwise logical equivalence.",
    "formalStatement": "(P∗Q)(h) ⇔ ∃h₁,h₂, h₁⊥h₂ ∧ h=h₁⊎h₂ ∧ P(h₁) ∧ Q(h₂); predicate equality means pointwise logical equivalence.",
    "assumptions": [
      "Classical extensional predicates over finite positive-address heap fragments. Points-to owns exactly one whole cell; using ObjectHeap records therefore separates objects, not individual fields. Disjointness concerns allocated domains, not pointer reachability: stored references may point into another fragment. Exclusive ownership assertions do not forbid alias references. No fractional permissions, borrowing, magic wand, concurrency rule or general frame rule is included. A frame rule additionally needs a local operational semantics; disjointness alone is insufficient.",
      "Variables have the carriers declared in the notation and operation signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/HeapSeparation"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled witness asserted by this record.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/oop-slf-separation"
    ],
    "sourceLocator": "Hprop: Description of Memory States; Heap Predicates (hempty, hsingle, hstar); Fundamental Properties of Operators",
    "sourceNote": "Uses the existing HeapStore address convention and exact heap-fragment assertions. Ownership is logical permission to a cell, not absence of aliases or an automatic encapsulation guarantee.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:law/HeapSeparation-star-commutative",
    "type": "Law",
    "name": "star-commutative",
    "statement": "∀h, (P∗Q)(h) ⇔ (Q∗P)(h).",
    "formalStatement": "∀h, (P∗Q)(h) ⇔ (Q∗P)(h).",
    "assumptions": [
      "Classical extensional predicates over finite positive-address heap fragments. Points-to owns exactly one whole cell; using ObjectHeap records therefore separates objects, not individual fields. Disjointness concerns allocated domains, not pointer reachability: stored references may point into another fragment. Exclusive ownership assertions do not forbid alias references. No fractional permissions, borrowing, magic wand, concurrency rule or general frame rule is included. A frame rule additionally needs a local operational semantics; disjointness alone is insufficient.",
      "Variables have the carriers declared in the notation and operation signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/HeapSeparation"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled witness asserted by this record.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/oop-slf-separation"
    ],
    "sourceLocator": "Hprop: Description of Memory States; Heap Predicates (hempty, hsingle, hstar); Fundamental Properties of Operators",
    "sourceNote": "Catalog derivation from the linked premises in this explicitly scoped model; the cited source supplies the underlying definitions. This is not a claim of executable proof.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/HeapSeparation-disjoint-union",
      "urn:csabs:axiom/HeapSeparation-star-splitting"
    ],
    "proofSketch": "Swap the witnessing fragments; disjointness and union are symmetric on disjoint domains."
  },
  {
    "id": "urn:csabs:law/HeapSeparation-star-empty-unit",
    "type": "Law",
    "name": "star-empty-unit",
    "statement": "∀h, (emp∗P)(h) ⇔ P(h).",
    "formalStatement": "∀h, (emp∗P)(h) ⇔ P(h).",
    "assumptions": [
      "Classical extensional predicates over finite positive-address heap fragments. Points-to owns exactly one whole cell; using ObjectHeap records therefore separates objects, not individual fields. Disjointness concerns allocated domains, not pointer reachability: stored references may point into another fragment. Exclusive ownership assertions do not forbid alias references. No fractional permissions, borrowing, magic wand, concurrency rule or general frame rule is included. A frame rule additionally needs a local operational semantics; disjointness alone is insufficient.",
      "Variables have the carriers declared in the notation and operation signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/HeapSeparation"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled witness asserted by this record.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/oop-slf-separation"
    ],
    "sourceLocator": "Hprop: Description of Memory States; Heap Predicates (hempty, hsingle, hstar); Fundamental Properties of Operators",
    "sourceNote": "Catalog derivation from the linked premises in this explicitly scoped model; the cited source supplies the underlying definitions. This is not a claim of executable proof.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/HeapSeparation-disjoint-union",
      "urn:csabs:axiom/HeapSeparation-exact-atoms",
      "urn:csabs:axiom/HeapSeparation-star-splitting"
    ],
    "proofSketch": "A satisfying empty fragment has empty domain, so its union leaves the other fragment unchanged. Conversely choose the empty heap and h."
  },
  {
    "id": "urn:csabs:law/HeapSeparation-exclusive-points-to",
    "type": "Law",
    "name": "exclusive-points-to",
    "statement": "∀a,v,w,h, ¬((a↦v)∗(a↦w))(h).",
    "formalStatement": "∀a,v,w,h, ¬((a↦v)∗(a↦w))(h).",
    "assumptions": [
      "Classical extensional predicates over finite positive-address heap fragments. Points-to owns exactly one whole cell; using ObjectHeap records therefore separates objects, not individual fields. Disjointness concerns allocated domains, not pointer reachability: stored references may point into another fragment. Exclusive ownership assertions do not forbid alias references. No fractional permissions, borrowing, magic wand, concurrency rule or general frame rule is included. A frame rule additionally needs a local operational semantics; disjointness alone is insufficient.",
      "Variables have the carriers declared in the notation and operation signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/HeapSeparation"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled witness asserted by this record.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/oop-slf-separation"
    ],
    "sourceLocator": "Hprop: Description of Memory States; Heap Predicates (hempty, hsingle, hstar); Fundamental Properties of Operators",
    "sourceNote": "Catalog derivation from the linked premises in this explicitly scoped model; the cited source supplies the underlying definitions. This is not a claim of executable proof.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/HeapSeparation-disjoint-union",
      "urn:csabs:axiom/HeapSeparation-exact-atoms",
      "urn:csabs:axiom/HeapSeparation-star-splitting"
    ],
    "proofSketch": "Both singleton fragments would allocate a, contradicting the required disjoint domains, even when v=w."
  }
]
```
<!-- graph-record:end -->
