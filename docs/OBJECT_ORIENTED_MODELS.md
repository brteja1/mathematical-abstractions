# Object-oriented semantic models

The OOP core adds six sourced concepts under Programming-language semantics → Object-oriented semantics. These mathematical profiles connect specifications to software; they do not prescribe a class architecture or implement a complete programming language.

| Concept | Selected interface | Software obligation it exposes |
| --- | --- | --- |
| [ObjectHeap](../concepts/ObjectHeap.md) | Class-tagged finite records, reference identity, partial field access/update, allocated aliasing | Equal values do not establish identity; a write through one alias is observable through another. |
| [ClassTable](../concepts/ClassTable.md) | Finite acyclic single inheritance, nearest-declaration lookup and receiver-class dispatch | Resolve selectors before lookup and use the runtime receiver tag; nominal inheritance supplies no behavioral guarantee. |
| [MethodContract](../concepts/MethodContract.md) | Preconditions, normal/exceptional outcomes, prestate-indexed permitted writes and input coverage | Check exceptional state effects and actual writes, including assignments that retain old values. Partial correctness does not require termination. |
| [ObjectInvariant](../concepts/ObjectInvariant.md) | Constructor establishment and preservation at explicit visible boundaries | Include callbacks and allowed alias interference before claiming validity at reachable boundaries. |
| [BehavioralSubtyping](../concepts/BehavioralSubtyping.md) | Legal-state abstraction, method correspondence, pre/post refinement and history constraints | Check inherited contracts and history changes caused by extra methods; superclass syntax alone is insufficient. |
| [HeapSeparation](../concepts/HeapSeparation.md) | Exact empty/singleton ownership assertions and disjoint heap splitting | Two exclusive points-to assertions cannot own the same cell, although references to that cell may be aliased. |

## Reuse and hierarchy

`ObjectHeap` specializes the existing `HeapStore`: its stored value is a class tag paired with a finite field map. It preserves the parent's positive-address carrier, lookup equality and heap operations. Field access and update are added operations. Qualified field identifiers avoid confusing field hiding with method dispatch. Raw inherited replacement/free retain their original semantics; safe class/lifetime disciplines must restrict them explicitly.

The other concepts use prerequisites and related links. `MethodContract` relates to `HoareTriple`, while explicitly modeling outcomes and writes. `ObjectInvariant` concerns visible object boundaries rather than loop iterations. `BehavioralSubtyping` differs from predicate-restricted `Subtype` and is related to simulation without claiming identical step semantics. Subject containment and prerequisites do not inherit axioms.

## Profile boundaries

- Object heaps permit null and dangling references as stored values, but dereferencing either is undefined. Map this partiality to the actual exception/error contract. Field updates preserve class tags; arbitrary raw heap replacement need not.
- Class tables cover single inheritance and already-resolved selectors. Bodies are opaque. Overloading, interfaces, multiple inheritance, language-specific method-resolution orders, casts and type safety are outside this profile.
- Method contracts use fixed-domain total stores, excluding allocation/deallocation until an explicit lifting is supplied. Traces record all writes: writing and restoring can violate a frame clause despite identical before/after observations. Outcome feasibility and actual termination are separate.
- Object invariants hold at chosen boundaries, not every internal instruction. Mutation of a reachable object invalidates an invariant argument unless prohibited or included in boundary preservation. Empty constructor sets can make reachability vacuous; check required constructors/scenarios separately.
- Behavioral subtyping uses the **constraint-rule** profile from Liskov–Wing §5.2, not the alternative explanation approach. Shared input/outcome carriers represent already-compatible signatures. General adapters, termination and contextual substitutability are outside this initial profile. Each type must satisfy its own specification.
- Heap separation assigns exclusive assertions to whole cells. With object records, cells are whole objects, not individual fields. Disjoint domains do not imply disjoint reachability or absence of aliases. A general frame rule needs a justified local execution semantics and is not inferred here.

The concept records link directly to consulted JLS, Featherweight Java, OpenJML, Liskov–Wing and Software Foundations sources, with locators, adaptation notes and consultation dates. These references describe different languages/models; no single reference is asserted to define the entire combined system.

## Example: exposing a mutable set representation

Suppose an object's field points to a mutable sequence representing a set, with uniqueness as its invariant. A constructor establishes uniqueness, and the object's own insertion method preserves it. If a getter exposes the sequence reference, external code can append a duplicate:

1. `ObjectHeap-alias-observes-write` explains why the returned alias accesses the same underlying object.
2. `ObjectInvariant-boundary-preservation` requires external mutation to preserve uniqueness when it is an allowed boundary transition. Preservation by the insertion method does not establish this.
3. A `MethodContract` with no permitted writes describes the getter call only; it does not prevent later mutation through the returned reference.
4. `HeapSeparation-exclusive-points-to` prevents claiming two independent exclusive fragments for the same cell. It does not itself forbid returning an alias or establish encapsulation.

Possible designs include returning an immutable observation, copying the representation, or enforcing an ownership/permission discipline. The specification and mapping must choose one; no universal encapsulation theorem is claimed.

For inheritance, a bounded subclass of an unbounded stack rejects required full-stack pushes, violating `BehavioralSubtyping-methods-rule` regardless of nominal inheritance. An extra method that changes a superclass-declared immutable property must also satisfy the history rule; inherited-method tests alone are insufficient.

## Retrieval and implementation

```sh
python3 scripts/catalog.py list --category object-oriented-semantics
python3 scripts/catalog.py get ObjectHeap --sections operations axioms laws sources
python3 scripts/agent_query.py node urn:csabs:axiom/BehavioralSubtyping-methods-rule
python3 scripts/agent_query.py node urn:csabs:theorem/ObjectInvariant-visible-reachable-valid
python3 scripts/lean.py get ClassTable
```

Use [implementation-mapping](../ai/skills/implementation-mapping/SKILL.md) to connect clauses and catalog IDs to API symbols, representation relations, equality, effects and boundaries. Use [implementation-conformance](../ai/skills/implementation-conformance/SKILL.md) to review code against that mapping and [mathematical-tests](../ai/skills/mathematical-tests/SKILL.md) for executable properties. Retrieve necessary premises and sources; structural checks do not establish semantic correctness.

## Lean scope

[`Catalog/ObjectOrientation.lean`](../lean/Catalog/ObjectOrientation.lean) supplies all six bindings. `ObjectHeap`, `MethodContract`, `ObjectInvariant` and `HeapSeparation` interpret carriers and selected interfaces. Merge is relational; extensional observation remains intended when structures carry auxiliary evidence.

`ClassTable` and `BehavioralSubtyping` are explicitly partial bindings. Class lookup uses a class-count bound and decreasing parent rank, but its general sufficiency and recursive-equation correspondence are not registered witnesses. Behavioral subtyping models semantic implications; its supplied history-pair relation needs connection to executions and general signature adapters.

No new OOP law/theorem is registered as a compiled witness. Invariant establishment/preservation fields are explicit hypotheses, not proofs about arbitrary software. Lean checks compile/audit models and existing witnesses; they do not establish target-code refinement or source correspondence.
