# Visible-state object invariant protocol

A predicate on an allocated receiver and whole-object environment, established by constructors and preserved between explicitly chosen externally visible boundaries.

**Notation:** I:H×Addr→Prop; Init⊆H×Addr; B⊆(H×Addr)²; Good(h,a) iff a∈dom(h) ∧ I(h,a)

**Stable ID:** `urn:csabs:concept/ObjectInvariant`

**Categories:** Programming-language semantics → Object-oriented semantics

**Kind:** semantic-model

**Prerequisites:** [Sequential object heap with reference identity](ObjectHeap.md), [Transition System](TransitionSystem.md)

**Related concepts:** [Relational method contract with write effects](MethodContract.md), [Exclusive finite-heap separation predicates](HeapSeparation.md), [Loop Invariant](LoopInvariant.md)

## Backlinks

- [Behavioral subtyping with explicit history constraints](BehavioralSubtyping.md) — `requiresConcept`
- [Relational method contract with write effects](MethodContract.md) — `relatedConcept`

## Mathematical formulation

For heap/receiver states (h,a), Holds(h,a) ⇔ a∈dom(h)∧Inv(h,a). The protocol requires Init⇒Holds and Holds(h,a)∧Boundary((h,a),(k,b))⇒Holds(k,b), with a=b across boundary transitions. No assertion is imposed at hidden intermediate instructions.

**Lean formulation** (in its source module context):

```lean
structure ObjectInvariant (C : Type u) (F : Type v) (P : Type w) where
  predicate : ObjectHeap C F P → PNat → Prop
  initial : ObjectHeap C F P × PNat → Prop
  boundary : (ObjectHeap C F P × PNat) → (ObjectHeap C F P × PNat) → Prop
  receiver_stable : ∀ a b, boundary a b → a.2 = b.2
  establishes : ∀ h a, initial (h, a) → (h.lookup a).isSome ∧ predicate h a
  preserves : ∀ h a k b, (h.lookup a).isSome ∧ predicate h a →
    boundary (h, a) (k, b) → (k.lookup b).isSome ∧ predicate k b
```

**Source:** [`Catalog.OOP.ObjectInvariant`](../lean/Catalog/ObjectOrientation.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Whole-object-heap predicate, allocated receiver, constructor poststates and receiver-preserving boundary relation. Establishment and preservation are explicit structure hypotheses; reachable uses finite reflexive-transitive closure.

**Limits:** Boundary completeness is a client obligation: callbacks and alias interference must be included. No compiled reachable-valid witness or hidden-instruction, liveness or concurrency claim is registered.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Selected defining rules: ∀(h,a)∈Init, a∈dom(h) ∧ I(h,a). ∀x,y, Good(x) ∧ B(x,y) ⇒ Good(y); all externally permitted receiver exposures/interference belong to B. reachable(Init,B,x) iff ∃n≥0, x₀,…,xₙ=x with x₀∈Init and B(xⱼ,xⱼ₊₁) for every j<n.

**basisKind:** extensional-structural-definition

**basisScope:** Sequential visible-boundary protocol, not an assertion at every internal instruction. B includes every completed public operation and every callback/reentrant exposure or external mutation allowed by the environment. The same receiver identity is preserved along B; destruction is excluded. The predicate may inspect shared reachable objects. A temporary violation is allowed only between boundaries without exposing it. No automatic ownership, encapsulation, termination or concurrency safety is implied. Predicate equality is extensional.

**verificationObligation:** Instantiate carriers, equality, definedness and the stated semantic profile before using these records.; Catalog validation checks structure, not source entailment or target implementation conformance.

**reviewStatus:** Editorial source and interface review; Lean model bindings and individual proof witnesses are separate.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-ObjectInvariant-holds"></a>

### holds

`urn:csabs:operation/ObjectInvariant-holds`

**signature:** holds : I×H×Addr→Prop

**description:** holds(I,h,a) iff Good(h,a); allocation is part of validity, not implied by a field predicate alone.

**precondition:** Typed inputs in the stated semantic profile.

**postcondition:** holds(I,h,a) iff Good(h,a); allocation is part of validity, not implied by a field predicate alone.

**totality:** Total mathematical operation.

**source:** [OpenJML tutorial: Invariants](https://www.openjml.org/tutorial/Invariants); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** Simple invariants and helper methods; Invariants when calling methods, including callbacks

**sourceNote:** Abstracts constructor establishment and visible-call preservation. Boundary relation includes relevant interference explicitly; visibility and helper policies of particular languages require their own instantiation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-ObjectInvariant-preserves"></a>

### preserves

`urn:csabs:operation/ObjectInvariant-preserves`

**signature:** preserves : I×B→Prop

**description:** preserves(I,B) iff ∀x,y, Good(x) ∧ B(x,y) ⇒ Good(y), where x=(h,a) and B preserves receiver identity.

**precondition:** Typed inputs in the stated semantic profile.

**postcondition:** preserves(I,B) iff ∀x,y, Good(x) ∧ B(x,y) ⇒ Good(y), where x=(h,a) and B preserves receiver identity.

**totality:** Total mathematical operation.

**source:** [OpenJML tutorial: Invariants](https://www.openjml.org/tutorial/Invariants); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** Simple invariants and helper methods; Invariants when calling methods, including callbacks

**sourceNote:** Abstracts constructor establishment and visible-call preservation. Boundary relation includes relevant interference explicitly; visibility and helper policies of particular languages require their own instantiation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-ObjectInvariant-reachable"></a>

### reachable

`urn:csabs:operation/ObjectInvariant-reachable`

**signature:** reachable : Init×B×(H×Addr)→Prop

**description:** Reachability is a finite B path from some constructor poststate in Init, including a zero-step path.

**precondition:** Typed inputs in the stated semantic profile.

**postcondition:** Reachability is a finite B path from some constructor poststate in Init, including a zero-step path.

**totality:** Total mathematical operation.

**source:** [OpenJML tutorial: Invariants](https://www.openjml.org/tutorial/Invariants); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** Simple invariants and helper methods; Invariants when calling methods, including callbacks

**sourceNote:** Abstracts constructor establishment and visible-call preservation. Boundary relation includes relevant interference explicitly; visibility and helper policies of particular languages require their own instantiation.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-ObjectInvariant-constructor-establishment"></a>

### constructor-establishment

`urn:csabs:axiom/ObjectInvariant-constructor-establishment`

**statement:** ∀(h,a)∈Init, a∈dom(h) ∧ I(h,a).

**formalStatement:** ∀(h,a)∈Init, a∈dom(h) ∧ I(h,a).

**assumptions:** Sequential visible-boundary protocol, not an assertion at every internal instruction. B includes every completed public operation and every callback/reentrant exposure or external mutation allowed by the environment. The same receiver identity is preserved along B; destruction is excluded. The predicate may inspect shared reachable objects. A temporary violation is allowed only between boundaries without exposing it. No automatic ownership, encapsulation, termination or concurrency safety is implied. Predicate equality is extensional.; Variables have the carriers declared in the notation and operation signatures.

**reviewStatus:** Editorial mathematical statement; no compiled witness asserted by this record.

**notationLanguage:** informal mathematical Unicode

**source:** [OpenJML tutorial: Invariants](https://www.openjml.org/tutorial/Invariants); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** Simple invariants and helper methods; Invariants when calling methods, including callbacks

**sourceNote:** Abstracts constructor establishment and visible-call preservation. Boundary relation includes relevant interference explicitly; visibility and helper policies of particular languages require their own instantiation.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-ObjectInvariant-boundary-preservation"></a>

### boundary-preservation

`urn:csabs:axiom/ObjectInvariant-boundary-preservation`

**statement:** ∀x,y, Good(x) ∧ B(x,y) ⇒ Good(y); all externally permitted receiver exposures/interference belong to B.

**formalStatement:** ∀x,y, Good(x) ∧ B(x,y) ⇒ Good(y); all externally permitted receiver exposures/interference belong to B.

**assumptions:** Sequential visible-boundary protocol, not an assertion at every internal instruction. B includes every completed public operation and every callback/reentrant exposure or external mutation allowed by the environment. The same receiver identity is preserved along B; destruction is excluded. The predicate may inspect shared reachable objects. A temporary violation is allowed only between boundaries without exposing it. No automatic ownership, encapsulation, termination or concurrency safety is implied. Predicate equality is extensional.; Variables have the carriers declared in the notation and operation signatures.

**reviewStatus:** Editorial mathematical statement; no compiled witness asserted by this record.

**notationLanguage:** informal mathematical Unicode

**source:** [OpenJML tutorial: Invariants](https://www.openjml.org/tutorial/Invariants); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** Simple invariants and helper methods; Invariants when calling methods, including callbacks

**sourceNote:** Abstracts constructor establishment and visible-call preservation. Boundary relation includes relevant interference explicitly; visibility and helper policies of particular languages require their own instantiation.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-ObjectInvariant-finite-reachability"></a>

### finite-reachability

`urn:csabs:axiom/ObjectInvariant-finite-reachability`

**statement:** reachable(Init,B,x) iff ∃n≥0, x₀,…,xₙ=x with x₀∈Init and B(xⱼ,xⱼ₊₁) for every j<n.

**formalStatement:** reachable(Init,B,x) iff ∃n≥0, x₀,…,xₙ=x with x₀∈Init and B(xⱼ,xⱼ₊₁) for every j<n.

**assumptions:** Sequential visible-boundary protocol, not an assertion at every internal instruction. B includes every completed public operation and every callback/reentrant exposure or external mutation allowed by the environment. The same receiver identity is preserved along B; destruction is excluded. The predicate may inspect shared reachable objects. A temporary violation is allowed only between boundaries without exposing it. No automatic ownership, encapsulation, termination or concurrency safety is implied. Predicate equality is extensional.; Variables have the carriers declared in the notation and operation signatures.

**reviewStatus:** Editorial mathematical statement; no compiled witness asserted by this record.

**notationLanguage:** informal mathematical Unicode

**source:** [OpenJML tutorial: Invariants](https://www.openjml.org/tutorial/Invariants); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** Simple invariants and helper methods; Invariants when calling methods, including callbacks

**sourceNote:** Abstracts constructor establishment and visible-call preservation. Boundary relation includes relevant interference explicitly; visibility and helper policies of particular languages require their own instantiation.

**provenanceKind:** adapted

**ruleRole:** defining-rule

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-ObjectInvariant-visible-reachable-valid"></a>

### visible-reachable-valid

`urn:csabs:theorem/ObjectInvariant-visible-reachable-valid`

**statement:** reachable(Init,B,(h,a)) ⇒ a∈dom(h) ∧ I(h,a).

**formalStatement:** reachable(Init,B,(h,a)) ⇒ a∈dom(h) ∧ I(h,a).

**assumptions:** Sequential visible-boundary protocol, not an assertion at every internal instruction. B includes every completed public operation and every callback/reentrant exposure or external mutation allowed by the environment. The same receiver identity is preserved along B; destruction is excluded. The predicate may inspect shared reachable objects. A temporary violation is allowed only between boundaries without exposing it. No automatic ownership, encapsulation, termination or concurrency safety is implied. Predicate equality is extensional.; Variables have the carriers declared in the notation and operation signatures.

**reviewStatus:** Editorial mathematical statement; no compiled witness asserted by this record.

**notationLanguage:** informal mathematical Unicode

**source:** [OpenJML tutorial: Invariants](https://www.openjml.org/tutorial/Invariants); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** Simple invariants and helper methods; Invariants when calling methods, including callbacks

**sourceNote:** Catalog derivation from the linked premises in this explicitly scoped model; the cited source supplies the underlying definitions. This is not a claim of executable proof.

**provenanceKind:** derived

**dependsOn:** [constructor-establishment](ObjectInvariant.md#node-urn-csabs-axiom-ObjectInvariant-constructor-establishment); [boundary-preservation](ObjectInvariant.md#node-urn-csabs-axiom-ObjectInvariant-boundary-preservation); [finite-reachability](ObjectInvariant.md#node-urn-csabs-axiom-ObjectInvariant-finite-reachability)

**proofSketch:** Induct on the finite path length. Constructor establishment proves length zero; boundary preservation gives the induction step. The result says nothing about unmodeled interference or internal instruction states.

## Concept provenance

- [OpenJML tutorial: Invariants](https://www.openjml.org/tutorial/Invariants); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** Simple invariants and helper methods; Invariants when calling methods, including callbacks

**sourceNote:** Abstracts constructor establishment and visible-call preservation. Boundary relation includes relevant interference explicitly; visibility and helper policies of particular languages require their own instantiation.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/ObjectInvariant",
    "type": "Concept",
    "shortForm": "ObjectInvariant",
    "fullName": "Visible-state object invariant protocol",
    "category": [
      "urn:csabs:category/object-oriented-semantics"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "definition": "A predicate on an allocated receiver and whole-object environment, established by constructors and preserved between explicitly chosen externally visible boundaries.",
    "notation": "I:H×Addr→Prop; Init⊆H×Addr; B⊆(H×Addr)²; Good(h,a) iff a∈dom(h) ∧ I(h,a)",
    "requiresConcept": [
      "urn:csabs:concept/ObjectHeap",
      "urn:csabs:concept/TransitionSystem"
    ],
    "relatedConcept": [
      "urn:csabs:concept/MethodContract",
      "urn:csabs:concept/HeapSeparation",
      "urn:csabs:concept/LoopInvariant"
    ],
    "hasOperation": [
      "urn:csabs:operation/ObjectInvariant-holds",
      "urn:csabs:operation/ObjectInvariant-preserves",
      "urn:csabs:operation/ObjectInvariant-reachable"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/ObjectInvariant-constructor-establishment",
      "urn:csabs:axiom/ObjectInvariant-boundary-preservation",
      "urn:csabs:axiom/ObjectInvariant-finite-reachability"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/ObjectInvariant-visible-reachable-valid"
    ],
    "basisKind": "extensional-structural-definition",
    "basisScope": "Sequential visible-boundary protocol, not an assertion at every internal instruction. B includes every completed public operation and every callback/reentrant exposure or external mutation allowed by the environment. The same receiver identity is preserved along B; destruction is excluded. The predicate may inspect shared reachable objects. A temporary violation is allowed only between boundaries without exposing it. No automatic ownership, encapsulation, termination or concurrency safety is implied. Predicate equality is extensional.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source and interface review; Lean model bindings and individual proof witnesses are separate.",
    "verificationObligation": [
      "Instantiate carriers, equality, definedness and the stated semantic profile before using these records.",
      "Catalog validation checks structure, not source entailment or target implementation conformance."
    ],
    "source": [
      "urn:csabs:source/oop-jml-invariants"
    ],
    "sourceLocator": "Simple invariants and helper methods; Invariants when calling methods, including callbacks",
    "sourceNote": "Abstracts constructor establishment and visible-call preservation. Boundary relation includes relevant interference explicitly; visibility and helper policies of particular languages require their own instantiation.",
    "provenanceKind": "adapted",
    "axiomBasis": "Selected defining rules: ∀(h,a)∈Init, a∈dom(h) ∧ I(h,a). ∀x,y, Good(x) ∧ B(x,y) ⇒ Good(y); all externally permitted receiver exposures/interference belong to B. reachable(Init,B,x) iff ∃n≥0, x₀,…,xₙ=x with x₀∈Init and B(xⱼ,xⱼ₊₁) for every j<n.",
    "leanFormulation": "structure ObjectInvariant (C : Type u) (F : Type v) (P : Type w) where\n  predicate : ObjectHeap C F P → PNat → Prop\n  initial : ObjectHeap C F P × PNat → Prop\n  boundary : (ObjectHeap C F P × PNat) → (ObjectHeap C F P × PNat) → Prop\n  receiver_stable : ∀ a b, boundary a b → a.2 = b.2\n  establishes : ∀ h a, initial (h, a) → (h.lookup a).isSome ∧ predicate h a\n  preserves : ∀ h a k b, (h.lookup a).isSome ∧ predicate h a →\n    boundary (h, a) (k, b) → (k.lookup b).isSome ∧ predicate k b",
    "formulationSource": "urn:csabs:source/local-lean-ObjectOrientation",
    "formulationLocator": "Catalog.OOP.ObjectInvariant",
    "formulationScope": "model",
    "leanModelMapping": "Whole-object-heap predicate, allocated receiver, constructor poststates and receiver-preserving boundary relation. Establishment and preservation are explicit structure hypotheses; reachable uses finite reflexive-transitive closure.",
    "leanModelLimitations": "Boundary completeness is a client obligation: callbacks and alias interference must be included. No compiled reachable-valid witness or hidden-instruction, liveness or concurrency claim is registered.",
    "mathematicalFormulation": "For heap/receiver states (h,a), Holds(h,a) ⇔ a∈dom(h)∧Inv(h,a). The protocol requires Init⇒Holds and Holds(h,a)∧Boundary((h,a),(k,b))⇒Holds(k,b), with a=b across boundary transitions. No assertion is imposed at hidden intermediate instructions."
  },
  {
    "id": "urn:csabs:operation/ObjectInvariant-holds",
    "type": "Operation",
    "name": "holds",
    "signature": "holds : I×H×Addr→Prop",
    "description": "holds(I,h,a) iff Good(h,a); allocation is part of validity, not implied by a field predicate alone.",
    "concept": "urn:csabs:concept/ObjectInvariant",
    "precondition": "Typed inputs in the stated semantic profile.",
    "postcondition": "holds(I,h,a) iff Good(h,a); allocation is part of validity, not implied by a field predicate alone.",
    "totality": "Total mathematical operation.",
    "source": [
      "urn:csabs:source/oop-jml-invariants"
    ],
    "sourceLocator": "Simple invariants and helper methods; Invariants when calling methods, including callbacks",
    "sourceNote": "Abstracts constructor establishment and visible-call preservation. Boundary relation includes relevant interference explicitly; visibility and helper policies of particular languages require their own instantiation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/ObjectInvariant-preserves",
    "type": "Operation",
    "name": "preserves",
    "signature": "preserves : I×B→Prop",
    "description": "preserves(I,B) iff ∀x,y, Good(x) ∧ B(x,y) ⇒ Good(y), where x=(h,a) and B preserves receiver identity.",
    "concept": "urn:csabs:concept/ObjectInvariant",
    "precondition": "Typed inputs in the stated semantic profile.",
    "postcondition": "preserves(I,B) iff ∀x,y, Good(x) ∧ B(x,y) ⇒ Good(y), where x=(h,a) and B preserves receiver identity.",
    "totality": "Total mathematical operation.",
    "source": [
      "urn:csabs:source/oop-jml-invariants"
    ],
    "sourceLocator": "Simple invariants and helper methods; Invariants when calling methods, including callbacks",
    "sourceNote": "Abstracts constructor establishment and visible-call preservation. Boundary relation includes relevant interference explicitly; visibility and helper policies of particular languages require their own instantiation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/ObjectInvariant-reachable",
    "type": "Operation",
    "name": "reachable",
    "signature": "reachable : Init×B×(H×Addr)→Prop",
    "description": "Reachability is a finite B path from some constructor poststate in Init, including a zero-step path.",
    "concept": "urn:csabs:concept/ObjectInvariant",
    "precondition": "Typed inputs in the stated semantic profile.",
    "postcondition": "Reachability is a finite B path from some constructor poststate in Init, including a zero-step path.",
    "totality": "Total mathematical operation.",
    "source": [
      "urn:csabs:source/oop-jml-invariants"
    ],
    "sourceLocator": "Simple invariants and helper methods; Invariants when calling methods, including callbacks",
    "sourceNote": "Abstracts constructor establishment and visible-call preservation. Boundary relation includes relevant interference explicitly; visibility and helper policies of particular languages require their own instantiation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/ObjectInvariant-constructor-establishment",
    "type": "Axiom",
    "name": "constructor-establishment",
    "statement": "∀(h,a)∈Init, a∈dom(h) ∧ I(h,a).",
    "formalStatement": "∀(h,a)∈Init, a∈dom(h) ∧ I(h,a).",
    "assumptions": [
      "Sequential visible-boundary protocol, not an assertion at every internal instruction. B includes every completed public operation and every callback/reentrant exposure or external mutation allowed by the environment. The same receiver identity is preserved along B; destruction is excluded. The predicate may inspect shared reachable objects. A temporary violation is allowed only between boundaries without exposing it. No automatic ownership, encapsulation, termination or concurrency safety is implied. Predicate equality is extensional.",
      "Variables have the carriers declared in the notation and operation signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/ObjectInvariant"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled witness asserted by this record.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/oop-jml-invariants"
    ],
    "sourceLocator": "Simple invariants and helper methods; Invariants when calling methods, including callbacks",
    "sourceNote": "Abstracts constructor establishment and visible-call preservation. Boundary relation includes relevant interference explicitly; visibility and helper policies of particular languages require their own instantiation.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/ObjectInvariant-boundary-preservation",
    "type": "Axiom",
    "name": "boundary-preservation",
    "statement": "∀x,y, Good(x) ∧ B(x,y) ⇒ Good(y); all externally permitted receiver exposures/interference belong to B.",
    "formalStatement": "∀x,y, Good(x) ∧ B(x,y) ⇒ Good(y); all externally permitted receiver exposures/interference belong to B.",
    "assumptions": [
      "Sequential visible-boundary protocol, not an assertion at every internal instruction. B includes every completed public operation and every callback/reentrant exposure or external mutation allowed by the environment. The same receiver identity is preserved along B; destruction is excluded. The predicate may inspect shared reachable objects. A temporary violation is allowed only between boundaries without exposing it. No automatic ownership, encapsulation, termination or concurrency safety is implied. Predicate equality is extensional.",
      "Variables have the carriers declared in the notation and operation signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/ObjectInvariant"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled witness asserted by this record.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/oop-jml-invariants"
    ],
    "sourceLocator": "Simple invariants and helper methods; Invariants when calling methods, including callbacks",
    "sourceNote": "Abstracts constructor establishment and visible-call preservation. Boundary relation includes relevant interference explicitly; visibility and helper policies of particular languages require their own instantiation.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/ObjectInvariant-finite-reachability",
    "type": "Axiom",
    "name": "finite-reachability",
    "statement": "reachable(Init,B,x) iff ∃n≥0, x₀,…,xₙ=x with x₀∈Init and B(xⱼ,xⱼ₊₁) for every j<n.",
    "formalStatement": "reachable(Init,B,x) iff ∃n≥0, x₀,…,xₙ=x with x₀∈Init and B(xⱼ,xⱼ₊₁) for every j<n.",
    "assumptions": [
      "Sequential visible-boundary protocol, not an assertion at every internal instruction. B includes every completed public operation and every callback/reentrant exposure or external mutation allowed by the environment. The same receiver identity is preserved along B; destruction is excluded. The predicate may inspect shared reachable objects. A temporary violation is allowed only between boundaries without exposing it. No automatic ownership, encapsulation, termination or concurrency safety is implied. Predicate equality is extensional.",
      "Variables have the carriers declared in the notation and operation signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/ObjectInvariant"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled witness asserted by this record.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/oop-jml-invariants"
    ],
    "sourceLocator": "Simple invariants and helper methods; Invariants when calling methods, including callbacks",
    "sourceNote": "Abstracts constructor establishment and visible-call preservation. Boundary relation includes relevant interference explicitly; visibility and helper policies of particular languages require their own instantiation.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:theorem/ObjectInvariant-visible-reachable-valid",
    "type": "Theorem",
    "name": "visible-reachable-valid",
    "statement": "reachable(Init,B,(h,a)) ⇒ a∈dom(h) ∧ I(h,a).",
    "formalStatement": "reachable(Init,B,(h,a)) ⇒ a∈dom(h) ∧ I(h,a).",
    "assumptions": [
      "Sequential visible-boundary protocol, not an assertion at every internal instruction. B includes every completed public operation and every callback/reentrant exposure or external mutation allowed by the environment. The same receiver identity is preserved along B; destruction is excluded. The predicate may inspect shared reachable objects. A temporary violation is allowed only between boundaries without exposing it. No automatic ownership, encapsulation, termination or concurrency safety is implied. Predicate equality is extensional.",
      "Variables have the carriers declared in the notation and operation signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/ObjectInvariant"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled witness asserted by this record.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/oop-jml-invariants"
    ],
    "sourceLocator": "Simple invariants and helper methods; Invariants when calling methods, including callbacks",
    "sourceNote": "Catalog derivation from the linked premises in this explicitly scoped model; the cited source supplies the underlying definitions. This is not a claim of executable proof.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/ObjectInvariant-constructor-establishment",
      "urn:csabs:axiom/ObjectInvariant-boundary-preservation",
      "urn:csabs:axiom/ObjectInvariant-finite-reachability"
    ],
    "proofSketch": "Induct on the finite path length. Constructor establishment proves length zero; boundary preservation gives the induction step. The result says nothing about unmodeled interference or internal instruction states."
  }
]
```
<!-- graph-record:end -->
