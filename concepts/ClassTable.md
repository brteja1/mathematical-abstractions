# Single-inheritance class table and dynamic dispatch

A finite rooted acyclic nominal class hierarchy with finite local method declarations and nearest-ancestor method lookup.

**Notation:** CT=(C,root,parent,methods); parent:C→Option(C); methods:C→(Selector⇀fin Body); C≤nom D iff D is on C’s inclusive ancestor chain

**Stable ID:** `urn:csabs:concept/ClassTable`

**Categories:** Programming-language semantics → Object-oriented semantics

**Kind:** semantic-model

**Prerequisites:** [Map](Map.md), [Partial function](PartialFunction.md)

**Related concepts:** [Sequential object heap with reference identity](ObjectHeap.md), [Partial Order](PartialOrder.md), [Behavioral subtyping with explicit history constraints](BehavioralSubtyping.md)

## Backlinks

- [Behavioral subtyping with explicit history constraints](BehavioralSubtyping.md) — `relatedConcept`
- [Definition/instantiation lookup for dependent calls](DependentNameLookup.md) — `relatedConcept`
- [Java type erasure and selected reifiability rules](JavaTypeErasure.md) — `relatedConcept`
- [Sequential object heap with reference identity](ObjectHeap.md) — `relatedConcept`

## Interface and scope

**axiomBasis:** Selected defining rules: parent(root)=None; every C≠root has exactly one parent in C; every parent chain reaches root without repetition. lookup(CT,C,m)=methods(C)(m) when locally declared; otherwise lookup(CT,parent(C),m) if a parent exists; otherwise undefined. dispatch(CT,h,r,m)=lookup(CT,classOf(h,r),m) on the stated domain; nominalSubtype(CT,C,D) ⇔ D∈ancestors(CT,C).

**basisKind:** extensional-structural-definition

**basisScope:** Finite nonempty class carrier C and one root. Every nonroot has exactly one parent; following parents reaches root without repetition. Selectors have already been resolved and are not overload-resolution requests. Bodies are opaque declarations; no typing, evaluation, casts, interfaces, multiple inheritance, method combination, reflection or behavioral compatibility is assumed. Table equality is extensional in parent and declaration lookups. Heap class tags supplied to dispatch belong to C.

**verificationObligation:** Instantiate carriers, equality, definedness and the stated semantic profile before using these records.; Catalog validation checks structure, not source entailment or target implementation conformance.

**reviewStatus:** Editorial source and interface review; Lean model bindings and individual proof witnesses are separate.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-ClassTable-ancestors"></a>

### ancestors

`urn:csabs:operation/ClassTable-ancestors`

**signature:** ancestors : CT×C→Seq(C)

**description:** Return [C,parent(C),…,root], including the receiver class first and root last.

**precondition:** Typed inputs in the stated semantic profile.

**postcondition:** Return [C,parent(C),…,root], including the receiver class first and root last.

**totality:** Total mathematical operation.

**source:** [Igarashi, Pierce and Wadler: Featherweight Java: A Minimal Core Calculus for Java and GJ](https://www.cis.upenn.edu/~bcpierce/papers/fj-toplas.pdf); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** §2.1 and Figure 1, class tables/subtyping/method-body lookup; §2.3 and Figure 3, invocation reduction

**sourceNote:** Extracts the single-inheritance lookup fragment of Featherweight Java. Represents the distinguished root explicitly and allows root declarations as a stated generalization; does not import FJ type safety or its entire calculus.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-ClassTable-nominal-subtype"></a>

### nominal-subtype

`urn:csabs:operation/ClassTable-nominal-subtype`

**signature:** nominalSubtype : CT×C×C→Prop

**description:** nominalSubtype(CT,C,D) iff D occurs in ancestors(CT,C).

**precondition:** Typed inputs in the stated semantic profile.

**postcondition:** nominalSubtype(CT,C,D) iff D occurs in ancestors(CT,C).

**totality:** Total mathematical operation.

**source:** [Igarashi, Pierce and Wadler: Featherweight Java: A Minimal Core Calculus for Java and GJ](https://www.cis.upenn.edu/~bcpierce/papers/fj-toplas.pdf); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** §2.1 and Figure 1, class tables/subtyping/method-body lookup; §2.3 and Figure 3, invocation reduction

**sourceNote:** Extracts the single-inheritance lookup fragment of Featherweight Java. Represents the distinguished root explicitly and allows root declarations as a stated generalization; does not import FJ type safety or its entire calculus.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-ClassTable-lookup"></a>

### lookup

`urn:csabs:operation/ClassTable-lookup`

**signature:** lookup : CT×C×Selector⇀Body

**description:** Return the first declaration of the selector along the inclusive ancestor chain, or undefined when none exists.

**precondition:** Class belongs to the table.

**postcondition:** Return the first declaration of the selector along the inclusive ancestor chain, or undefined when none exists.

**totality:** Partial on selectors absent from the whole ancestor chain.

**source:** [Igarashi, Pierce and Wadler: Featherweight Java: A Minimal Core Calculus for Java and GJ](https://www.cis.upenn.edu/~bcpierce/papers/fj-toplas.pdf); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** §2.1 and Figure 1, class tables/subtyping/method-body lookup; §2.3 and Figure 3, invocation reduction

**sourceNote:** Extracts the single-inheritance lookup fragment of Featherweight Java. Represents the distinguished root explicitly and allows root declarations as a stated generalization; does not import FJ type safety or its entire calculus.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-ClassTable-dispatch"></a>

### dispatch

`urn:csabs:operation/ClassTable-dispatch`

**signature:** dispatch : CT×H×Ref×Selector⇀Body

**description:** dispatch(CT,h,r,m)=lookup(CT,classOf(h,r),m); receiver class comes from the heap, not the reference’s static type.

**precondition:** Receiver is allocated and nonnull with tag in CT; a declaration exists on its ancestor chain.

**postcondition:** dispatch(CT,h,r,m)=lookup(CT,classOf(h,r),m); receiver class comes from the heap, not the reference’s static type.

**totality:** Partial outside the precondition; returns a declaration, not an evaluated result.

**source:** [Igarashi, Pierce and Wadler: Featherweight Java: A Minimal Core Calculus for Java and GJ](https://www.cis.upenn.edu/~bcpierce/papers/fj-toplas.pdf); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** §2.1 and Figure 1, class tables/subtyping/method-body lookup; §2.3 and Figure 3, invocation reduction

**sourceNote:** Extracts the single-inheritance lookup fragment of Featherweight Java. Represents the distinguished root explicitly and allows root declarations as a stated generalization; does not import FJ type safety or its entire calculus.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-ClassTable-rooted-chain"></a>

### rooted-chain

`urn:csabs:axiom/ClassTable-rooted-chain`

**statement:** parent(root)=None; every C≠root has exactly one parent in C; every parent chain reaches root without repetition.

**formalStatement:** parent(root)=None; every C≠root has exactly one parent in C; every parent chain reaches root without repetition.

**assumptions:** Finite nonempty class carrier C and one root. Every nonroot has exactly one parent; following parents reaches root without repetition. Selectors have already been resolved and are not overload-resolution requests. Bodies are opaque declarations; no typing, evaluation, casts, interfaces, multiple inheritance, method combination, reflection or behavioral compatibility is assumed. Table equality is extensional in parent and declaration lookups. Heap class tags supplied to dispatch belong to C.; Variables have the carriers declared in the notation and operation signatures.

**reviewStatus:** Editorial mathematical statement; no compiled witness asserted by this record.

**notationLanguage:** informal mathematical Unicode

**source:** [Igarashi, Pierce and Wadler: Featherweight Java: A Minimal Core Calculus for Java and GJ](https://www.cis.upenn.edu/~bcpierce/papers/fj-toplas.pdf); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** §2.1 and Figure 1, class tables/subtyping/method-body lookup; §2.3 and Figure 3, invocation reduction

**sourceNote:** Extracts the single-inheritance lookup fragment of Featherweight Java. Represents the distinguished root explicitly and allows root declarations as a stated generalization; does not import FJ type safety or its entire calculus.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-ClassTable-nearest-declaration"></a>

### nearest-declaration

`urn:csabs:axiom/ClassTable-nearest-declaration`

**statement:** lookup(CT,C,m)=methods(C)(m) when locally declared; otherwise lookup(CT,parent(C),m) if a parent exists; otherwise undefined.

**formalStatement:** lookup(CT,C,m)=methods(C)(m) when locally declared; otherwise lookup(CT,parent(C),m) if a parent exists; otherwise undefined.

**assumptions:** Finite nonempty class carrier C and one root. Every nonroot has exactly one parent; following parents reaches root without repetition. Selectors have already been resolved and are not overload-resolution requests. Bodies are opaque declarations; no typing, evaluation, casts, interfaces, multiple inheritance, method combination, reflection or behavioral compatibility is assumed. Table equality is extensional in parent and declaration lookups. Heap class tags supplied to dispatch belong to C.; Variables have the carriers declared in the notation and operation signatures.

**reviewStatus:** Editorial mathematical statement; no compiled witness asserted by this record.

**notationLanguage:** informal mathematical Unicode

**source:** [Igarashi, Pierce and Wadler: Featherweight Java: A Minimal Core Calculus for Java and GJ](https://www.cis.upenn.edu/~bcpierce/papers/fj-toplas.pdf); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** §2.1 and Figure 1, class tables/subtyping/method-body lookup; §2.3 and Figure 3, invocation reduction

**sourceNote:** Extracts the single-inheritance lookup fragment of Featherweight Java. Represents the distinguished root explicitly and allows root declarations as a stated generalization; does not import FJ type safety or its entire calculus.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-ClassTable-runtime-receiver"></a>

### runtime-receiver

`urn:csabs:axiom/ClassTable-runtime-receiver`

**statement:** dispatch(CT,h,r,m)=lookup(CT,classOf(h,r),m) on the stated domain; nominalSubtype(CT,C,D) ⇔ D∈ancestors(CT,C).

**formalStatement:** dispatch(CT,h,r,m)=lookup(CT,classOf(h,r),m) on the stated domain; nominalSubtype(CT,C,D) ⇔ D∈ancestors(CT,C).

**assumptions:** Finite nonempty class carrier C and one root. Every nonroot has exactly one parent; following parents reaches root without repetition. Selectors have already been resolved and are not overload-resolution requests. Bodies are opaque declarations; no typing, evaluation, casts, interfaces, multiple inheritance, method combination, reflection or behavioral compatibility is assumed. Table equality is extensional in parent and declaration lookups. Heap class tags supplied to dispatch belong to C.; Variables have the carriers declared in the notation and operation signatures.

**reviewStatus:** Editorial mathematical statement; no compiled witness asserted by this record.

**notationLanguage:** informal mathematical Unicode

**source:** [Igarashi, Pierce and Wadler: Featherweight Java: A Minimal Core Calculus for Java and GJ](https://www.cis.upenn.edu/~bcpierce/papers/fj-toplas.pdf); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** §2.1 and Figure 1, class tables/subtyping/method-body lookup; §2.3 and Figure 3, invocation reduction

**sourceNote:** Extracts the single-inheritance lookup fragment of Featherweight Java. Represents the distinguished root explicitly and allows root declarations as a stated generalization; does not import FJ type safety or its entire calculus.

**provenanceKind:** adapted

**ruleRole:** defining-rule

## Laws

<a id="node-urn-csabs-law-ClassTable-local-override"></a>

### local-override

`urn:csabs:law/ClassTable-local-override`

**statement:** methods(C)(m)=body ⇒ lookup(CT,C,m)=body, irrespective of declarations in ancestors.

**formalStatement:** methods(C)(m)=body ⇒ lookup(CT,C,m)=body, irrespective of declarations in ancestors.

**assumptions:** Finite nonempty class carrier C and one root. Every nonroot has exactly one parent; following parents reaches root without repetition. Selectors have already been resolved and are not overload-resolution requests. Bodies are opaque declarations; no typing, evaluation, casts, interfaces, multiple inheritance, method combination, reflection or behavioral compatibility is assumed. Table equality is extensional in parent and declaration lookups. Heap class tags supplied to dispatch belong to C.; Variables have the carriers declared in the notation and operation signatures.

**reviewStatus:** Editorial mathematical statement; no compiled witness asserted by this record.

**notationLanguage:** informal mathematical Unicode

**source:** [Igarashi, Pierce and Wadler: Featherweight Java: A Minimal Core Calculus for Java and GJ](https://www.cis.upenn.edu/~bcpierce/papers/fj-toplas.pdf); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** §2.1 and Figure 1, class tables/subtyping/method-body lookup; §2.3 and Figure 3, invocation reduction

**sourceNote:** Catalog derivation from the linked premises in this explicitly scoped model; the cited source supplies the underlying definitions. This is not a claim of executable proof.

**provenanceKind:** derived

**dependsOn:** [nearest-declaration](ClassTable.md#node-urn-csabs-axiom-ClassTable-nearest-declaration)

**proofSketch:** Apply the local-declaration branch of lookup before searching any parent.

<a id="node-urn-csabs-law-ClassTable-inherited-lookup"></a>

### inherited-lookup

`urn:csabs:law/ClassTable-inherited-lookup`

**statement:** methods(C)(m) undefined ∧ parent(C)=Some(D) ⇒ lookup(CT,C,m)=lookup(CT,D,m), including equality of undefined outcomes.

**formalStatement:** methods(C)(m) undefined ∧ parent(C)=Some(D) ⇒ lookup(CT,C,m)=lookup(CT,D,m), including equality of undefined outcomes.

**assumptions:** Finite nonempty class carrier C and one root. Every nonroot has exactly one parent; following parents reaches root without repetition. Selectors have already been resolved and are not overload-resolution requests. Bodies are opaque declarations; no typing, evaluation, casts, interfaces, multiple inheritance, method combination, reflection or behavioral compatibility is assumed. Table equality is extensional in parent and declaration lookups. Heap class tags supplied to dispatch belong to C.; Variables have the carriers declared in the notation and operation signatures.

**reviewStatus:** Editorial mathematical statement; no compiled witness asserted by this record.

**notationLanguage:** informal mathematical Unicode

**source:** [Igarashi, Pierce and Wadler: Featherweight Java: A Minimal Core Calculus for Java and GJ](https://www.cis.upenn.edu/~bcpierce/papers/fj-toplas.pdf); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** §2.1 and Figure 1, class tables/subtyping/method-body lookup; §2.3 and Figure 3, invocation reduction

**sourceNote:** Catalog derivation from the linked premises in this explicitly scoped model; the cited source supplies the underlying definitions. This is not a claim of executable proof.

**provenanceKind:** derived

**dependsOn:** [nearest-declaration](ClassTable.md#node-urn-csabs-axiom-ClassTable-nearest-declaration)

**proofSketch:** Apply the parent branch of the lookup definition; partial-result equality includes joint undefinedness.

## Theorems

<a id="node-urn-csabs-theorem-ClassTable-lookup-terminates"></a>

### lookup-terminates

`urn:csabs:theorem/ClassTable-lookup-terminates`

**statement:** Lookup on a well-formed CT examines at most |C| classes and yields at most one declaration.

**formalStatement:** Lookup on a well-formed CT examines at most |C| classes and yields at most one declaration.

**assumptions:** Finite nonempty class carrier C and one root. Every nonroot has exactly one parent; following parents reaches root without repetition. Selectors have already been resolved and are not overload-resolution requests. Bodies are opaque declarations; no typing, evaluation, casts, interfaces, multiple inheritance, method combination, reflection or behavioral compatibility is assumed. Table equality is extensional in parent and declaration lookups. Heap class tags supplied to dispatch belong to C.; Variables have the carriers declared in the notation and operation signatures.

**reviewStatus:** Editorial mathematical statement; no compiled witness asserted by this record.

**notationLanguage:** informal mathematical Unicode

**source:** [Igarashi, Pierce and Wadler: Featherweight Java: A Minimal Core Calculus for Java and GJ](https://www.cis.upenn.edu/~bcpierce/papers/fj-toplas.pdf); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** §2.1 and Figure 1, class tables/subtyping/method-body lookup; §2.3 and Figure 3, invocation reduction

**sourceNote:** Catalog derivation from the linked premises in this explicitly scoped model; the cited source supplies the underlying definitions. This is not a claim of executable proof.

**provenanceKind:** derived

**dependsOn:** [rooted-chain](ClassTable.md#node-urn-csabs-axiom-ClassTable-rooted-chain); [nearest-declaration](ClassTable.md#node-urn-csabs-axiom-ClassTable-nearest-declaration)

**proofSketch:** The ancestor chain has no repetition and is contained in the finite class carrier. Each class has a functional local method map, and lookup stops at its first match.

## Concept provenance

- [Igarashi, Pierce and Wadler: Featherweight Java: A Minimal Core Calculus for Java and GJ](https://www.cis.upenn.edu/~bcpierce/papers/fj-toplas.pdf); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** §2.1 and Figure 1, class tables/subtyping/method-body lookup; §2.3 and Figure 3, invocation reduction

**sourceNote:** Extracts the single-inheritance lookup fragment of Featherweight Java. Represents the distinguished root explicitly and allows root declarations as a stated generalization; does not import FJ type safety or its entire calculus.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/ClassTable",
    "type": "Concept",
    "shortForm": "ClassTable",
    "fullName": "Single-inheritance class table and dynamic dispatch",
    "category": [
      "urn:csabs:category/object-oriented-semantics"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "definition": "A finite rooted acyclic nominal class hierarchy with finite local method declarations and nearest-ancestor method lookup.",
    "notation": "CT=(C,root,parent,methods); parent:C→Option(C); methods:C→(Selector⇀fin Body); C≤nom D iff D is on C’s inclusive ancestor chain",
    "requiresConcept": [
      "urn:csabs:concept/Map",
      "urn:csabs:concept/PartialFunction"
    ],
    "relatedConcept": [
      "urn:csabs:concept/ObjectHeap",
      "urn:csabs:concept/PartialOrder",
      "urn:csabs:concept/BehavioralSubtyping"
    ],
    "hasOperation": [
      "urn:csabs:operation/ClassTable-ancestors",
      "urn:csabs:operation/ClassTable-nominal-subtype",
      "urn:csabs:operation/ClassTable-lookup",
      "urn:csabs:operation/ClassTable-dispatch"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/ClassTable-rooted-chain",
      "urn:csabs:axiom/ClassTable-nearest-declaration",
      "urn:csabs:axiom/ClassTable-runtime-receiver"
    ],
    "hasLaw": [
      "urn:csabs:law/ClassTable-local-override",
      "urn:csabs:law/ClassTable-inherited-lookup"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/ClassTable-lookup-terminates"
    ],
    "basisKind": "extensional-structural-definition",
    "basisScope": "Finite nonempty class carrier C and one root. Every nonroot has exactly one parent; following parents reaches root without repetition. Selectors have already been resolved and are not overload-resolution requests. Bodies are opaque declarations; no typing, evaluation, casts, interfaces, multiple inheritance, method combination, reflection or behavioral compatibility is assumed. Table equality is extensional in parent and declaration lookups. Heap class tags supplied to dispatch belong to C.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source and interface review; Lean model bindings and individual proof witnesses are separate.",
    "verificationObligation": [
      "Instantiate carriers, equality, definedness and the stated semantic profile before using these records.",
      "Catalog validation checks structure, not source entailment or target implementation conformance."
    ],
    "source": [
      "urn:csabs:source/oop-featherweight-java"
    ],
    "sourceLocator": "§2.1 and Figure 1, class tables/subtyping/method-body lookup; §2.3 and Figure 3, invocation reduction",
    "sourceNote": "Extracts the single-inheritance lookup fragment of Featherweight Java. Represents the distinguished root explicitly and allows root declarations as a stated generalization; does not import FJ type safety or its entire calculus.",
    "provenanceKind": "adapted",
    "axiomBasis": "Selected defining rules: parent(root)=None; every C≠root has exactly one parent in C; every parent chain reaches root without repetition. lookup(CT,C,m)=methods(C)(m) when locally declared; otherwise lookup(CT,parent(C),m) if a parent exists; otherwise undefined. dispatch(CT,h,r,m)=lookup(CT,classOf(h,r),m) on the stated domain; nominalSubtype(CT,C,D) ⇔ D∈ancestors(CT,C)."
  },
  {
    "id": "urn:csabs:operation/ClassTable-ancestors",
    "type": "Operation",
    "name": "ancestors",
    "signature": "ancestors : CT×C→Seq(C)",
    "description": "Return [C,parent(C),…,root], including the receiver class first and root last.",
    "concept": "urn:csabs:concept/ClassTable",
    "precondition": "Typed inputs in the stated semantic profile.",
    "postcondition": "Return [C,parent(C),…,root], including the receiver class first and root last.",
    "totality": "Total mathematical operation.",
    "source": [
      "urn:csabs:source/oop-featherweight-java"
    ],
    "sourceLocator": "§2.1 and Figure 1, class tables/subtyping/method-body lookup; §2.3 and Figure 3, invocation reduction",
    "sourceNote": "Extracts the single-inheritance lookup fragment of Featherweight Java. Represents the distinguished root explicitly and allows root declarations as a stated generalization; does not import FJ type safety or its entire calculus.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/ClassTable-nominal-subtype",
    "type": "Operation",
    "name": "nominal-subtype",
    "signature": "nominalSubtype : CT×C×C→Prop",
    "description": "nominalSubtype(CT,C,D) iff D occurs in ancestors(CT,C).",
    "concept": "urn:csabs:concept/ClassTable",
    "precondition": "Typed inputs in the stated semantic profile.",
    "postcondition": "nominalSubtype(CT,C,D) iff D occurs in ancestors(CT,C).",
    "totality": "Total mathematical operation.",
    "source": [
      "urn:csabs:source/oop-featherweight-java"
    ],
    "sourceLocator": "§2.1 and Figure 1, class tables/subtyping/method-body lookup; §2.3 and Figure 3, invocation reduction",
    "sourceNote": "Extracts the single-inheritance lookup fragment of Featherweight Java. Represents the distinguished root explicitly and allows root declarations as a stated generalization; does not import FJ type safety or its entire calculus.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/ClassTable-lookup",
    "type": "Operation",
    "name": "lookup",
    "signature": "lookup : CT×C×Selector⇀Body",
    "description": "Return the first declaration of the selector along the inclusive ancestor chain, or undefined when none exists.",
    "concept": "urn:csabs:concept/ClassTable",
    "precondition": "Class belongs to the table.",
    "postcondition": "Return the first declaration of the selector along the inclusive ancestor chain, or undefined when none exists.",
    "totality": "Partial on selectors absent from the whole ancestor chain.",
    "source": [
      "urn:csabs:source/oop-featherweight-java"
    ],
    "sourceLocator": "§2.1 and Figure 1, class tables/subtyping/method-body lookup; §2.3 and Figure 3, invocation reduction",
    "sourceNote": "Extracts the single-inheritance lookup fragment of Featherweight Java. Represents the distinguished root explicitly and allows root declarations as a stated generalization; does not import FJ type safety or its entire calculus.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/ClassTable-dispatch",
    "type": "Operation",
    "name": "dispatch",
    "signature": "dispatch : CT×H×Ref×Selector⇀Body",
    "description": "dispatch(CT,h,r,m)=lookup(CT,classOf(h,r),m); receiver class comes from the heap, not the reference’s static type.",
    "concept": "urn:csabs:concept/ClassTable",
    "precondition": "Receiver is allocated and nonnull with tag in CT; a declaration exists on its ancestor chain.",
    "postcondition": "dispatch(CT,h,r,m)=lookup(CT,classOf(h,r),m); receiver class comes from the heap, not the reference’s static type.",
    "totality": "Partial outside the precondition; returns a declaration, not an evaluated result.",
    "source": [
      "urn:csabs:source/oop-featherweight-java"
    ],
    "sourceLocator": "§2.1 and Figure 1, class tables/subtyping/method-body lookup; §2.3 and Figure 3, invocation reduction",
    "sourceNote": "Extracts the single-inheritance lookup fragment of Featherweight Java. Represents the distinguished root explicitly and allows root declarations as a stated generalization; does not import FJ type safety or its entire calculus.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/ClassTable-rooted-chain",
    "type": "Axiom",
    "name": "rooted-chain",
    "statement": "parent(root)=None; every C≠root has exactly one parent in C; every parent chain reaches root without repetition.",
    "formalStatement": "parent(root)=None; every C≠root has exactly one parent in C; every parent chain reaches root without repetition.",
    "assumptions": [
      "Finite nonempty class carrier C and one root. Every nonroot has exactly one parent; following parents reaches root without repetition. Selectors have already been resolved and are not overload-resolution requests. Bodies are opaque declarations; no typing, evaluation, casts, interfaces, multiple inheritance, method combination, reflection or behavioral compatibility is assumed. Table equality is extensional in parent and declaration lookups. Heap class tags supplied to dispatch belong to C.",
      "Variables have the carriers declared in the notation and operation signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/ClassTable"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled witness asserted by this record.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/oop-featherweight-java"
    ],
    "sourceLocator": "§2.1 and Figure 1, class tables/subtyping/method-body lookup; §2.3 and Figure 3, invocation reduction",
    "sourceNote": "Extracts the single-inheritance lookup fragment of Featherweight Java. Represents the distinguished root explicitly and allows root declarations as a stated generalization; does not import FJ type safety or its entire calculus.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/ClassTable-nearest-declaration",
    "type": "Axiom",
    "name": "nearest-declaration",
    "statement": "lookup(CT,C,m)=methods(C)(m) when locally declared; otherwise lookup(CT,parent(C),m) if a parent exists; otherwise undefined.",
    "formalStatement": "lookup(CT,C,m)=methods(C)(m) when locally declared; otherwise lookup(CT,parent(C),m) if a parent exists; otherwise undefined.",
    "assumptions": [
      "Finite nonempty class carrier C and one root. Every nonroot has exactly one parent; following parents reaches root without repetition. Selectors have already been resolved and are not overload-resolution requests. Bodies are opaque declarations; no typing, evaluation, casts, interfaces, multiple inheritance, method combination, reflection or behavioral compatibility is assumed. Table equality is extensional in parent and declaration lookups. Heap class tags supplied to dispatch belong to C.",
      "Variables have the carriers declared in the notation and operation signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/ClassTable"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled witness asserted by this record.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/oop-featherweight-java"
    ],
    "sourceLocator": "§2.1 and Figure 1, class tables/subtyping/method-body lookup; §2.3 and Figure 3, invocation reduction",
    "sourceNote": "Extracts the single-inheritance lookup fragment of Featherweight Java. Represents the distinguished root explicitly and allows root declarations as a stated generalization; does not import FJ type safety or its entire calculus.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/ClassTable-runtime-receiver",
    "type": "Axiom",
    "name": "runtime-receiver",
    "statement": "dispatch(CT,h,r,m)=lookup(CT,classOf(h,r),m) on the stated domain; nominalSubtype(CT,C,D) ⇔ D∈ancestors(CT,C).",
    "formalStatement": "dispatch(CT,h,r,m)=lookup(CT,classOf(h,r),m) on the stated domain; nominalSubtype(CT,C,D) ⇔ D∈ancestors(CT,C).",
    "assumptions": [
      "Finite nonempty class carrier C and one root. Every nonroot has exactly one parent; following parents reaches root without repetition. Selectors have already been resolved and are not overload-resolution requests. Bodies are opaque declarations; no typing, evaluation, casts, interfaces, multiple inheritance, method combination, reflection or behavioral compatibility is assumed. Table equality is extensional in parent and declaration lookups. Heap class tags supplied to dispatch belong to C.",
      "Variables have the carriers declared in the notation and operation signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/ClassTable"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled witness asserted by this record.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/oop-featherweight-java"
    ],
    "sourceLocator": "§2.1 and Figure 1, class tables/subtyping/method-body lookup; §2.3 and Figure 3, invocation reduction",
    "sourceNote": "Extracts the single-inheritance lookup fragment of Featherweight Java. Represents the distinguished root explicitly and allows root declarations as a stated generalization; does not import FJ type safety or its entire calculus.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:law/ClassTable-local-override",
    "type": "Law",
    "name": "local-override",
    "statement": "methods(C)(m)=body ⇒ lookup(CT,C,m)=body, irrespective of declarations in ancestors.",
    "formalStatement": "methods(C)(m)=body ⇒ lookup(CT,C,m)=body, irrespective of declarations in ancestors.",
    "assumptions": [
      "Finite nonempty class carrier C and one root. Every nonroot has exactly one parent; following parents reaches root without repetition. Selectors have already been resolved and are not overload-resolution requests. Bodies are opaque declarations; no typing, evaluation, casts, interfaces, multiple inheritance, method combination, reflection or behavioral compatibility is assumed. Table equality is extensional in parent and declaration lookups. Heap class tags supplied to dispatch belong to C.",
      "Variables have the carriers declared in the notation and operation signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/ClassTable"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled witness asserted by this record.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/oop-featherweight-java"
    ],
    "sourceLocator": "§2.1 and Figure 1, class tables/subtyping/method-body lookup; §2.3 and Figure 3, invocation reduction",
    "sourceNote": "Catalog derivation from the linked premises in this explicitly scoped model; the cited source supplies the underlying definitions. This is not a claim of executable proof.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/ClassTable-nearest-declaration"
    ],
    "proofSketch": "Apply the local-declaration branch of lookup before searching any parent."
  },
  {
    "id": "urn:csabs:law/ClassTable-inherited-lookup",
    "type": "Law",
    "name": "inherited-lookup",
    "statement": "methods(C)(m) undefined ∧ parent(C)=Some(D) ⇒ lookup(CT,C,m)=lookup(CT,D,m), including equality of undefined outcomes.",
    "formalStatement": "methods(C)(m) undefined ∧ parent(C)=Some(D) ⇒ lookup(CT,C,m)=lookup(CT,D,m), including equality of undefined outcomes.",
    "assumptions": [
      "Finite nonempty class carrier C and one root. Every nonroot has exactly one parent; following parents reaches root without repetition. Selectors have already been resolved and are not overload-resolution requests. Bodies are opaque declarations; no typing, evaluation, casts, interfaces, multiple inheritance, method combination, reflection or behavioral compatibility is assumed. Table equality is extensional in parent and declaration lookups. Heap class tags supplied to dispatch belong to C.",
      "Variables have the carriers declared in the notation and operation signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/ClassTable"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled witness asserted by this record.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/oop-featherweight-java"
    ],
    "sourceLocator": "§2.1 and Figure 1, class tables/subtyping/method-body lookup; §2.3 and Figure 3, invocation reduction",
    "sourceNote": "Catalog derivation from the linked premises in this explicitly scoped model; the cited source supplies the underlying definitions. This is not a claim of executable proof.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/ClassTable-nearest-declaration"
    ],
    "proofSketch": "Apply the parent branch of the lookup definition; partial-result equality includes joint undefinedness."
  },
  {
    "id": "urn:csabs:theorem/ClassTable-lookup-terminates",
    "type": "Theorem",
    "name": "lookup-terminates",
    "statement": "Lookup on a well-formed CT examines at most |C| classes and yields at most one declaration.",
    "formalStatement": "Lookup on a well-formed CT examines at most |C| classes and yields at most one declaration.",
    "assumptions": [
      "Finite nonempty class carrier C and one root. Every nonroot has exactly one parent; following parents reaches root without repetition. Selectors have already been resolved and are not overload-resolution requests. Bodies are opaque declarations; no typing, evaluation, casts, interfaces, multiple inheritance, method combination, reflection or behavioral compatibility is assumed. Table equality is extensional in parent and declaration lookups. Heap class tags supplied to dispatch belong to C.",
      "Variables have the carriers declared in the notation and operation signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/ClassTable"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled witness asserted by this record.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/oop-featherweight-java"
    ],
    "sourceLocator": "§2.1 and Figure 1, class tables/subtyping/method-body lookup; §2.3 and Figure 3, invocation reduction",
    "sourceNote": "Catalog derivation from the linked premises in this explicitly scoped model; the cited source supplies the underlying definitions. This is not a claim of executable proof.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/ClassTable-rooted-chain",
      "urn:csabs:axiom/ClassTable-nearest-declaration"
    ],
    "proofSketch": "The ancestor chain has no repetition and is contained in the finite class carrier. Each class has a functional local method map, and lookup stops at its first match."
  }
]
```
<!-- graph-record:end -->
