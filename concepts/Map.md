# Map

A finite partial function associating each present key with exactly one value; absence is distinct from stored values.

**Notation:** m:K⇀V; dom(m) finite

**Stable ID:** `urn:csabs:concept/Map`

**Categories:** Data structures → Sets and mappings

**Kind:** Abstract data type

**Prerequisites:** [Partial function](PartialFunction.md)

**Specializes:** [Partial function](PartialFunction.md)

**Related concepts:** [Named relational schema with attribute domains](RelationalSchema.md)

## Backlinks

- [Candidate key relative to functional dependencies](CandidateKey.md) — `relatedConcept`
- [Single-inheritance class table and dynamic dispatch](ClassTable.md) — `requiresConcept`
- [Finite JSON document value (interoperable profile)](DocumentValue.md) — `requiresConcept`
- [Finite allocated heap store](HeapStore.md) — `requiresConcept`
- [Lock with compatible access modes](Lock.md) — `requiresConcept`
- [Finite set-valued multimap](Multimap.md) — `requiresConcept`
- [Sequential object heap with reference identity](ObjectHeap.md) — `requiresConcept`
- [Ordered collection without duplicates](OrderedSet.md) — `relatedConcept`
- [Finite labelled property graph (single-valued profile)](PropertyGraph.md) — `requiresConcept`
- [Finite RDF 1.1 dataset](RDFDataset.md) — `requiresConcept`
- [Named relational schema with attribute domains](RelationalSchema.md) — `relatedConcept`
- [Finite prefix dictionary](Trie.md) — `requiresConcept`
- [Finite prefix dictionary](Trie.md) — `specializationOf`

## Mathematical formulation

Map(K,V)={f:K→Option(V) | {k | f(k)≠none} is finite}. lookup(f,k)=f(k); setting k to v replaces f(k) with some(v); erasing k replaces it with none. Equality is extensional on lookup. Utility profile: Right-biased override: lookup(m▷n,k)=lookup(n,k) when present, otherwise lookup(m,k). Finite domain is the domain union; a missing value in n does not delete m.; All keys where Option-valued lookups differ, including addition, deletion and replacement; value identity equality and absent/present distinction are explicit.

**Lean formulation** (in its source module context):

```lean
structure Map (K : Type u) (V : Type v) where
  lookup : K → Option V
  finite_domain : {k | (lookup k).isSome}.Finite
```

**Source:** [`Catalog.Map`](../lean/Catalog/DataStructures.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Lookup K -> Option V plus proof that the defined-key set is finite; record proof fields are propositionally irrelevant.

**Limits:** Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Selected presentation: A finite partial function associating each present key with exactly one value; absence is distinct from stored values. Governing rules: A finite map is a partial function with a finite defined domain. Empty has no bindings. Updating a key overwrites it and leaves other bindings unchanged. Deleting a key makes it absent and preserves other bindings. Maps are equal if all lookups agree. Utility definitions are recorded separately; optional bottom, subtype and goal-relative conventions are conditional and do not strengthen the base carrier.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**specializationNote:** Interpret a map state as a partial function K⇀V with finite defined domain. None denotes absence, not a stored V value; update and lookup remain the Map interface.

**verificationObligation:** Instantiate carrier, equality, and stated semantic conventions before using this entry.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

**provenanceStatus:** legacy-source-missing

## Operations

<a id="node-urn-csabs-operation-Map-lookup"></a>

### lookup

`urn:csabs:operation/Map-lookup`

**signature:** lookup : Map(K,V)×K→Option(V)

**description:** Returns Some(value) for a present key and None otherwise.

<a id="node-urn-csabs-operation-Map-set"></a>

### set

`urn:csabs:operation/Map-set`

**signature:** set : Map(K,V)×K×V→Map(K,V)

**description:** Associates the key with a value, replacing any previous association.

<a id="node-urn-csabs-operation-Map-delete"></a>

### delete

`urn:csabs:operation/Map-delete`

**signature:** delete : Map(K,V)×K→Map(K,V)

**description:** Removes the key if present and preserves other bindings.

<a id="node-urn-csabs-operation-Map-basis-empty"></a>

### empty

`urn:csabs:operation/Map-basis-empty`

**signature:** empty : Map(K,V)

**description:** Constructs a map with no bindings.

<a id="node-urn-csabs-operation-Map-override-merge"></a>

### override-merge

`urn:csabs:operation/Map-override-merge`

**signature:** overrideMerge : Map(K,V)²→Map(K,V)

**description:** Right-biased override: lookup(m▷n,k)=lookup(n,k) when present, otherwise lookup(m,k). Finite domain is the domain union; a missing value in n does not delete m.

**precondition:** Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.

**postcondition:** Right-biased override: lookup(m▷n,k)=lookup(n,k) when present, otherwise lookup(m,k). Finite domain is the domain union; a missing value in n does not delete m.

**totality:** Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.

**sourceLocator:** Data/Set/Finite/Basic.lean: finite union and subset; Option.or; constructed finite-support override and unequal-lookup support

**sourceNote:** Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-Map-diff"></a>

### diff

`urn:csabs:operation/Map-diff`

**signature:** diff : Map(K,V)²→FinSet(K)

**description:** All keys where Option-valued lookups differ, including addition, deletion and replacement; value identity equality and absent/present distinction are explicit.

**precondition:** Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.

**postcondition:** All keys where Option-valued lookups differ, including addition, deletion and replacement; value identity equality and absent/present distinction are explicit.

**totality:** Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.

**sourceLocator:** Data/Set/Finite/Basic.lean: finite union and subset; Option.or; constructed finite-support override and unequal-lookup support

**sourceNote:** Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-Map-finite-graph"></a>

### finite-graph

`urn:csabs:axiom/Map-finite-graph`

**statement:** A finite map is a partial function with a finite defined domain.

**formalStatement:** m:K⇀V; dom(m) finite; lookup(m,k)=Some(m(k)) if k∈dom(m), otherwise None

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Software Foundations, Separation Logic Foundations: Heap Predicates](https://softwarefoundations.cis.upenn.edu/slf-current/Hprop.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Java SE 21 Map API: mappings, put and equality](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html); accessedOn: 2026-11-07; sourceRole: consulted-interface-reference

**sourceLocator:** SLF Hprop, Description of Memory States; Java Map interface, get/containsKey, put and equals contracts

**sourceNote:** Finite partial-map value semantics adapted from SLF; overwrite and mapping equality corroborated by Map API. Absence uses Option rather than Java null; no Java mutation, exceptions, ordering or key-object behavior is imported.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-Map-empty-lookup"></a>

### empty-lookup

`urn:csabs:axiom/Map-empty-lookup`

**statement:** Empty has no bindings.

**formalStatement:** lookup(empty,k)=None

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Map-update-lookup"></a>

### update-lookup

`urn:csabs:axiom/Map-update-lookup`

**statement:** Updating a key overwrites it and leaves other bindings unchanged.

**formalStatement:** lookup(set(m,k,v),j)=if j=k then Some(v) else lookup(m,j)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Software Foundations, Separation Logic Foundations: Heap Predicates](https://softwarefoundations.cis.upenn.edu/slf-current/Hprop.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Java SE 21 Map API: mappings, put and equality](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html); accessedOn: 2026-11-07; sourceRole: consulted-interface-reference

**sourceLocator:** SLF Hprop, Description of Memory States; Java Map interface, get/containsKey, put and equals contracts

**sourceNote:** Finite partial-map value semantics adapted from SLF; overwrite and mapping equality corroborated by Map API. Absence uses Option rather than Java null; no Java mutation, exceptions, ordering or key-object behavior is imported.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-Map-delete-lookup"></a>

### delete-lookup

`urn:csabs:axiom/Map-delete-lookup`

**statement:** Deleting a key makes it absent and preserves other bindings.

**formalStatement:** lookup(delete(m,k),j)=if j=k then None else lookup(m,j)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Map-lookup-extensionality"></a>

### lookup-extensionality

`urn:csabs:axiom/Map-lookup-extensionality`

**statement:** Maps are equal if all lookups agree.

**formalStatement:** m=n iff ∀k:lookup(m,k)=lookup(n,k)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Software Foundations, Separation Logic Foundations: Heap Predicates](https://softwarefoundations.cis.upenn.edu/slf-current/Hprop.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Java SE 21 Map API: mappings, put and equality](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html); accessedOn: 2026-11-07; sourceRole: consulted-interface-reference

**sourceLocator:** SLF Hprop, Description of Memory States; Java Map interface, get/containsKey, put and equals contracts

**sourceNote:** Finite partial-map value semantics adapted from SLF; overwrite and mapping equality corroborated by Map API. Absence uses Option rather than Java null; no Java mutation, exceptions, ordering or key-object behavior is imported.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-Map-utility-profile"></a>

### Explicit utility operation definitions

`urn:csabs:axiom/Map-utility-profile`

**statement:** Right-biased override: lookup(m▷n,k)=lookup(n,k) when present, otherwise lookup(m,k). Finite domain is the domain union; a missing value in n does not delete m.; All keys where Option-valued lookups differ, including addition, deletion and replacement; value identity equality and absent/present distinction are explicit.

**formalStatement:** overrideMerge : Map(K,V)²→Map(K,V): Right-biased override: lookup(m▷n,k)=lookup(n,k) when present, otherwise lookup(m,k). Finite domain is the domain union; a missing value in n does not delete m.; diff : Map(K,V)²→FinSet(K): All keys where Option-valued lookups differ, including addition, deletion and replacement; value identity equality and absent/present distinction are explicit.

**assumptions:** Base concept conventions remain unchanged. Optional profiles apply only under their explicitly stated additional hypotheses; identity equality, finite inputs and exact mathematics.

**ruleRole:** defining-rule

**reviewStatus:** Definitions of a selected extension, not new foundational axioms; individual model and result witnesses are separate.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.

**sourceLocator:** Data/Set/Finite/Basic.lean: finite union and subset; Option.or; constructed finite-support override and unequal-lookup support

**sourceNote:** Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-Map-core"></a>

### law/Map-core

`urn:csabs:law/Map-core`

**statement:** Looking up a key after setting it returns the assigned value.

**formalStatement:** lookup(set(m,k,v),k)=Some(v)

**reviewStatus:** editorial-summary; not machine-proved

**assumptions:** Use the carrier and semantic convention in the linked concept definition.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [finite-graph](Map.md#node-urn-csabs-axiom-Map-finite-graph); [empty-lookup](Map.md#node-urn-csabs-axiom-Map-empty-lookup); [update-lookup](Map.md#node-urn-csabs-axiom-Map-update-lookup); [delete-lookup](Map.md#node-urn-csabs-axiom-Map-delete-lookup); [lookup-extensionality](Map.md#node-urn-csabs-axiom-Map-lookup-extensionality)

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-law-map-frame"></a>

### law/map-frame

`urn:csabs:law/map-frame`

**statement:** Updating one key preserves every other key binding.

**formalStatement:** k≠j ⇒ lookup(set(m,k,v),j)=lookup(m,j)

**assumptions:** Key equality is fixed and stable

**reviewStatus:** editorial-summary; not machine-proved

**dependsOn:** [finite-graph](Map.md#node-urn-csabs-axiom-Map-finite-graph); [empty-lookup](Map.md#node-urn-csabs-axiom-Map-empty-lookup); [update-lookup](Map.md#node-urn-csabs-axiom-Map-update-lookup); [delete-lookup](Map.md#node-urn-csabs-axiom-Map-delete-lookup); [lookup-extensionality](Map.md#node-urn-csabs-axiom-Map-lookup-extensionality)

**provenanceStatus:** legacy-source-missing

## Theorems

<a id="node-urn-csabs-theorem-Map-update-shadow"></a>

### update-shadow

`urn:csabs:theorem/Map-update-shadow`

**statement:** The latest update of a given key overrides earlier ones.

**formalStatement:** set(set(m,k,v),k,w)=set(m,k,w)

**proofSketch:** Compare lookup at k and at every other key; apply lookup extensionality.

**assumptions:** The explicit basis, carriers, and side conditions stated for Map apply.

**dependsOn:** [finite-graph](Map.md#node-urn-csabs-axiom-Map-finite-graph); [empty-lookup](Map.md#node-urn-csabs-axiom-Map-empty-lookup); [update-lookup](Map.md#node-urn-csabs-axiom-Map-update-lookup); [delete-lookup](Map.md#node-urn-csabs-axiom-Map-delete-lookup); [lookup-extensionality](Map.md#node-urn-csabs-axiom-Map-lookup-extensionality)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-theorem-Map-override-lookup"></a>

### override-lookup

`urn:csabs:theorem/Map-override-lookup`

**statement:** lookup(m▷n,k)=Option.or(lookup(n,k),lookup(m,k)); right present values override, right absence preserves left.

**formalStatement:** lookup(m▷n,k)=Option.or(lookup(n,k),lookup(m,k)); right present values override, right absence preserves left.

**proofSketch:** Construct finite support by inclusion in the union of the input finite supports; lookup equation is definitional.

**assumptions:** Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles.

**dependsOn:** [Explicit utility operation definitions](Map.md#node-urn-csabs-axiom-Map-utility-profile); [finite-graph](Map.md#node-urn-csabs-axiom-Map-finite-graph)

**reviewStatus:** Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.; Catalog CollectionUtilities Lean formulations and proofs; path: lean/Catalog/CollectionUtilities.lean; accessedOn: 2026-11-20; sourceRole: Local formulation and derived-proof evidence. Independent mathematical provenance is linked separately.

**sourceLocator:** Data/Set/Finite/Basic.lean: finite union and subset; Option.or; constructed finite-support override and unequal-lookup support; Catalog.mapOverride_lookup

**sourceNote:** Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.

**provenanceKind:** derived

#### Mathematical formulation

lookup(m▷n,k)=Option.or(lookup(n,k),lookup(m,k)); right present values override, right absence preserves left.

**Lean formulation** (in its source module context):

```lean
∀ {K : Type u} {V : Type v} (m n : Catalog.Map K V) (k : K), (Catalog.mapOverride m n).lookup k = (n.lookup k).or (m.lookup k)
```

**Source:** [`Catalog.mapOverride_lookup`](../lean/Catalog/CollectionUtilities.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** lookup(m▷n,k)=Option.or(lookup(n,k),lookup(m,k)); right present values override, right absence preserves left. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.

**Limits:** Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/Map-finite-graph": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.",
  "urn:csabs:axiom/Map-utility-profile": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders."
}
```

<a id="node-urn-csabs-theorem-Map-diff-membership"></a>

### diff-membership

`urn:csabs:theorem/Map-diff-membership`

**statement:** k∈diff(m,n) iff lookup(m,k)≠lookup(n,k).

**formalStatement:** k∈diff(m,n) iff lookup(m,k)≠lookup(n,k).

**proofSketch:** Unequal Option lookups imply at least one is present, so the finite union support contains every changed key.

**assumptions:** Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles.

**dependsOn:** [Explicit utility operation definitions](Map.md#node-urn-csabs-axiom-Map-utility-profile); [finite-graph](Map.md#node-urn-csabs-axiom-Map-finite-graph)

**reviewStatus:** Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.; Catalog CollectionUtilities Lean formulations and proofs; path: lean/Catalog/CollectionUtilities.lean; accessedOn: 2026-11-20; sourceRole: Local formulation and derived-proof evidence. Independent mathematical provenance is linked separately.

**sourceLocator:** Data/Set/Finite/Basic.lean: finite union and subset; Option.or; constructed finite-support override and unequal-lookup support; Catalog.mapDiff_membership

**sourceNote:** Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.

**provenanceKind:** derived

#### Mathematical formulation

k∈diff(m,n) iff lookup(m,k)≠lookup(n,k).

**Lean formulation** (in its source module context):

```lean
∀ {K : Type u} {V : Type v} (m n : Catalog.Map K V) (k : K), k ∈ Catalog.mapDiff m n ↔ m.lookup k ≠ n.lookup k
```

**Source:** [`Catalog.mapDiff_membership`](../lean/Catalog/CollectionUtilities.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** k∈diff(m,n) iff lookup(m,k)≠lookup(n,k). Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.

**Limits:** Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/Map-finite-graph": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.",
  "urn:csabs:axiom/Map-utility-profile": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders."
}
```

## Concept provenance

Historical source gap retained; see `provenanceStatus` and the frozen baseline.

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/Map",
    "type": "Concept",
    "shortForm": "Map",
    "fullName": "Map",
    "category": [
      "urn:csabs:category/associative-collections"
    ],
    "kind": "urn:csabs:kind/abstract-data-type",
    "definition": "A finite partial function associating each present key with exactly one value; absence is distinct from stored values.",
    "notation": "m:K⇀V; dom(m) finite",
    "hasOperation": [
      "urn:csabs:operation/Map-lookup",
      "urn:csabs:operation/Map-set",
      "urn:csabs:operation/Map-delete",
      "urn:csabs:operation/Map-basis-empty",
      "urn:csabs:operation/Map-override-merge",
      "urn:csabs:operation/Map-diff"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/Map-finite-graph",
      "urn:csabs:axiom/Map-empty-lookup",
      "urn:csabs:axiom/Map-update-lookup",
      "urn:csabs:axiom/Map-delete-lookup",
      "urn:csabs:axiom/Map-lookup-extensionality",
      "urn:csabs:axiom/Map-utility-profile"
    ],
    "hasLaw": [
      "urn:csabs:law/Map-core",
      "urn:csabs:law/map-frame"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/Map-update-shadow",
      "urn:csabs:theorem/Map-override-lookup",
      "urn:csabs:theorem/Map-diff-membership"
    ],
    "requiresConcept": [
      "urn:csabs:concept/PartialFunction"
    ],
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Instantiate carrier, equality, and stated semantic conventions before using this entry.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: A finite partial function associating each present key with exactly one value; absence is distinct from stored values. Governing rules: A finite map is a partial function with a finite defined domain. Empty has no bindings. Updating a key overwrites it and leaves other bindings unchanged. Deleting a key makes it absent and preserves other bindings. Maps are equal if all lookups agree. Utility definitions are recorded separately; optional bottom, subtype and goal-relative conventions are conditional and do not strengthen the base carrier.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "provenanceStatus": "legacy-source-missing",
    "specializationOf": [
      "urn:csabs:concept/PartialFunction"
    ],
    "specializationNote": "Interpret a map state as a partial function K⇀V with finite defined domain. None denotes absence, not a stored V value; update and lookup remain the Map interface.",
    "relatedConcept": [
      "urn:csabs:concept/RelationalSchema"
    ],
    "leanFormulation": "structure Map (K : Type u) (V : Type v) where\n  lookup : K → Option V\n  finite_domain : {k | (lookup k).isSome}.Finite",
    "formulationSource": "urn:csabs:source/local-lean-DataStructures",
    "formulationLocator": "Catalog.Map",
    "formulationScope": "model",
    "leanModelMapping": "Lookup K -> Option V plus proof that the defined-key set is finite; record proof fields are propositionally irrelevant.",
    "leanModelLimitations": "Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.",
    "mathematicalFormulation": "Map(K,V)={f:K→Option(V) | {k | f(k)≠none} is finite}. lookup(f,k)=f(k); setting k to v replaces f(k) with some(v); erasing k replaces it with none. Equality is extensional on lookup. Utility profile: Right-biased override: lookup(m▷n,k)=lookup(n,k) when present, otherwise lookup(m,k). Finite domain is the domain union; a missing value in n does not delete m.; All keys where Option-valued lookups differ, including addition, deletion and replacement; value identity equality and absent/present distinction are explicit."
  },
  {
    "id": "urn:csabs:operation/Map-lookup",
    "type": "Operation",
    "name": "lookup",
    "signature": "lookup : Map(K,V)×K→Option(V)",
    "description": "Returns Some(value) for a present key and None otherwise.",
    "concept": "urn:csabs:concept/Map"
  },
  {
    "id": "urn:csabs:operation/Map-set",
    "type": "Operation",
    "name": "set",
    "signature": "set : Map(K,V)×K×V→Map(K,V)",
    "description": "Associates the key with a value, replacing any previous association.",
    "concept": "urn:csabs:concept/Map"
  },
  {
    "id": "urn:csabs:operation/Map-delete",
    "type": "Operation",
    "name": "delete",
    "signature": "delete : Map(K,V)×K→Map(K,V)",
    "description": "Removes the key if present and preserves other bindings.",
    "concept": "urn:csabs:concept/Map"
  },
  {
    "id": "urn:csabs:operation/Map-basis-empty",
    "type": "Operation",
    "name": "empty",
    "signature": "empty : Map(K,V)",
    "description": "Constructs a map with no bindings.",
    "concept": "urn:csabs:concept/Map"
  },
  {
    "id": "urn:csabs:operation/Map-override-merge",
    "type": "Operation",
    "concept": "urn:csabs:concept/Map",
    "name": "override-merge",
    "signature": "overrideMerge : Map(K,V)²→Map(K,V)",
    "description": "Right-biased override: lookup(m▷n,k)=lookup(n,k) when present, otherwise lookup(m,k). Finite domain is the domain union; a missing value in n does not delete m.",
    "precondition": "Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.",
    "postcondition": "Right-biased override: lookup(m▷n,k)=lookup(n,k) when present, otherwise lookup(m,k). Finite domain is the domain union; a missing value in n does not delete m.",
    "totality": "Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned"
    ],
    "sourceLocator": "Data/Set/Finite/Basic.lean: finite union and subset; Option.or; constructed finite-support override and unequal-lookup support",
    "sourceNote": "Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/Map-diff",
    "type": "Operation",
    "concept": "urn:csabs:concept/Map",
    "name": "diff",
    "signature": "diff : Map(K,V)²→FinSet(K)",
    "description": "All keys where Option-valued lookups differ, including addition, deletion and replacement; value identity equality and absent/present distinction are explicit.",
    "precondition": "Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.",
    "postcondition": "All keys where Option-valued lookups differ, including addition, deletion and replacement; value identity equality and absent/present distinction are explicit.",
    "totality": "Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned"
    ],
    "sourceLocator": "Data/Set/Finite/Basic.lean: finite union and subset; Option.or; constructed finite-support override and unequal-lookup support",
    "sourceNote": "Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/Map-finite-graph",
    "type": "Axiom",
    "name": "finite-graph",
    "statement": "A finite map is a partial function with a finite defined domain.",
    "formalStatement": "m:K⇀V; dom(m) finite; lookup(m,k)=Some(m(k)) if k∈dom(m), otherwise None",
    "appliesTo": [
      "urn:csabs:concept/Map",
      "urn:csabs:concept/Trie"
    ],
    "assumptions": [
      "All variables range over the carriers and semantic conventions specified in this concept."
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/slf-heap-core",
      "urn:csabs:source/java-map-core"
    ],
    "sourceLocator": "SLF Hprop, Description of Memory States; Java Map interface, get/containsKey, put and equals contracts",
    "sourceNote": "Finite partial-map value semantics adapted from SLF; overwrite and mapping equality corroborated by Map API. Absence uses Option rather than Java null; no Java mutation, exceptions, ordering or key-object behavior is imported.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/Map-empty-lookup",
    "type": "Axiom",
    "name": "empty-lookup",
    "statement": "Empty has no bindings.",
    "formalStatement": "lookup(empty,k)=None",
    "appliesTo": [
      "urn:csabs:concept/Map"
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
    "id": "urn:csabs:axiom/Map-update-lookup",
    "type": "Axiom",
    "name": "update-lookup",
    "statement": "Updating a key overwrites it and leaves other bindings unchanged.",
    "formalStatement": "lookup(set(m,k,v),j)=if j=k then Some(v) else lookup(m,j)",
    "appliesTo": [
      "urn:csabs:concept/Map",
      "urn:csabs:concept/Trie"
    ],
    "assumptions": [
      "All variables range over the carriers and semantic conventions specified in this concept."
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/slf-heap-core",
      "urn:csabs:source/java-map-core"
    ],
    "sourceLocator": "SLF Hprop, Description of Memory States; Java Map interface, get/containsKey, put and equals contracts",
    "sourceNote": "Finite partial-map value semantics adapted from SLF; overwrite and mapping equality corroborated by Map API. Absence uses Option rather than Java null; no Java mutation, exceptions, ordering or key-object behavior is imported.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/Map-delete-lookup",
    "type": "Axiom",
    "name": "delete-lookup",
    "statement": "Deleting a key makes it absent and preserves other bindings.",
    "formalStatement": "lookup(delete(m,k),j)=if j=k then None else lookup(m,j)",
    "appliesTo": [
      "urn:csabs:concept/Map"
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
    "id": "urn:csabs:axiom/Map-lookup-extensionality",
    "type": "Axiom",
    "name": "lookup-extensionality",
    "statement": "Maps are equal if all lookups agree.",
    "formalStatement": "m=n iff ∀k:lookup(m,k)=lookup(n,k)",
    "appliesTo": [
      "urn:csabs:concept/Map",
      "urn:csabs:concept/Trie"
    ],
    "assumptions": [
      "All variables range over the carriers and semantic conventions specified in this concept."
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/slf-heap-core",
      "urn:csabs:source/java-map-core"
    ],
    "sourceLocator": "SLF Hprop, Description of Memory States; Java Map interface, get/containsKey, put and equals contracts",
    "sourceNote": "Finite partial-map value semantics adapted from SLF; overwrite and mapping equality corroborated by Map API. Absence uses Option rather than Java null; no Java mutation, exceptions, ordering or key-object behavior is imported.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/Map-utility-profile",
    "type": "Axiom",
    "name": "Explicit utility operation definitions",
    "statement": "Right-biased override: lookup(m▷n,k)=lookup(n,k) when present, otherwise lookup(m,k). Finite domain is the domain union; a missing value in n does not delete m.; All keys where Option-valued lookups differ, including addition, deletion and replacement; value identity equality and absent/present distinction are explicit.",
    "formalStatement": "overrideMerge : Map(K,V)²→Map(K,V): Right-biased override: lookup(m▷n,k)=lookup(n,k) when present, otherwise lookup(m,k). Finite domain is the domain union; a missing value in n does not delete m.; diff : Map(K,V)²→FinSet(K): All keys where Option-valued lookups differ, including addition, deletion and replacement; value identity equality and absent/present distinction are explicit.",
    "assumptions": [
      "Base concept conventions remain unchanged. Optional profiles apply only under their explicitly stated additional hypotheses; identity equality, finite inputs and exact mathematics."
    ],
    "appliesTo": [
      "urn:csabs:concept/Map"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Definitions of a selected extension, not new foundational axioms; individual model and result witnesses are separate.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned"
    ],
    "sourceLocator": "Data/Set/Finite/Basic.lean: finite union and subset; Option.or; constructed finite-support override and unequal-lookup support",
    "sourceNote": "Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/Map-core",
    "type": "Law",
    "statement": "Looking up a key after setting it returns the assigned value.",
    "formalStatement": "lookup(set(m,k,v),k)=Some(v)",
    "appliesTo": [
      "urn:csabs:concept/Map"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "assumptions": [
      "Use the carrier and semantic convention in the linked concept definition."
    ],
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/Map-finite-graph",
      "urn:csabs:axiom/Map-empty-lookup",
      "urn:csabs:axiom/Map-update-lookup",
      "urn:csabs:axiom/Map-delete-lookup",
      "urn:csabs:axiom/Map-lookup-extensionality"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:law/map-frame",
    "type": "Law",
    "statement": "Updating one key preserves every other key binding.",
    "formalStatement": "k≠j ⇒ lookup(set(m,k,v),j)=lookup(m,j)",
    "assumptions": [
      "Key equality is fixed and stable"
    ],
    "appliesTo": [
      "urn:csabs:concept/Map"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "dependsOn": [
      "urn:csabs:axiom/Map-finite-graph",
      "urn:csabs:axiom/Map-empty-lookup",
      "urn:csabs:axiom/Map-update-lookup",
      "urn:csabs:axiom/Map-delete-lookup",
      "urn:csabs:axiom/Map-lookup-extensionality"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/Map-update-shadow",
    "type": "Theorem",
    "name": "update-shadow",
    "statement": "The latest update of a given key overrides earlier ones.",
    "formalStatement": "set(set(m,k,v),k,w)=set(m,k,w)",
    "proofSketch": "Compare lookup at k and at every other key; apply lookup extensionality.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for Map apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/Map"
    ],
    "dependsOn": [
      "urn:csabs:axiom/Map-finite-graph",
      "urn:csabs:axiom/Map-empty-lookup",
      "urn:csabs:axiom/Map-update-lookup",
      "urn:csabs:axiom/Map-delete-lookup",
      "urn:csabs:axiom/Map-lookup-extensionality"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/Map-override-lookup",
    "type": "Theorem",
    "name": "override-lookup",
    "statement": "lookup(m▷n,k)=Option.or(lookup(n,k),lookup(m,k)); right present values override, right absence preserves left.",
    "formalStatement": "lookup(m▷n,k)=Option.or(lookup(n,k),lookup(m,k)); right present values override, right absence preserves left.",
    "mathematicalFormulation": "lookup(m▷n,k)=Option.or(lookup(n,k),lookup(m,k)); right present values override, right absence preserves left.",
    "proofSketch": "Construct finite support by inclusion in the union of the input finite supports; lookup equation is definitional.",
    "assumptions": [
      "Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles."
    ],
    "appliesTo": [
      "urn:csabs:concept/Map"
    ],
    "dependsOn": [
      "urn:csabs:axiom/Map-utility-profile",
      "urn:csabs:axiom/Map-finite-graph"
    ],
    "reviewStatus": "Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned",
      "urn:csabs:source/utility-lean-CollectionUtilities"
    ],
    "sourceLocator": "Data/Set/Finite/Basic.lean: finite union and subset; Option.or; constructed finite-support override and unequal-lookup support; Catalog.mapOverride_lookup",
    "sourceNote": "Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {K : Type u} {V : Type v} (m n : Catalog.Map K V) (k : K), (Catalog.mapOverride m n).lookup k = (n.lookup k).or (m.lookup k)",
    "leanModelMapping": "lookup(m▷n,k)=Option.or(lookup(n,k),lookup(m,k)); right present values override, right absence preserves left. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.",
    "leanModelLimitations": "Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/Map-finite-graph\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\", \"urn:csabs:axiom/Map-utility-profile\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\"}",
    "formulationScope": "registered-witness-type",
    "formulationSource": "urn:csabs:source/utility-lean-CollectionUtilities",
    "formulationLocator": "Catalog.mapOverride_lookup"
  },
  {
    "id": "urn:csabs:theorem/Map-diff-membership",
    "type": "Theorem",
    "name": "diff-membership",
    "statement": "k∈diff(m,n) iff lookup(m,k)≠lookup(n,k).",
    "formalStatement": "k∈diff(m,n) iff lookup(m,k)≠lookup(n,k).",
    "mathematicalFormulation": "k∈diff(m,n) iff lookup(m,k)≠lookup(n,k).",
    "proofSketch": "Unequal Option lookups imply at least one is present, so the finite union support contains every changed key.",
    "assumptions": [
      "Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles."
    ],
    "appliesTo": [
      "urn:csabs:concept/Map"
    ],
    "dependsOn": [
      "urn:csabs:axiom/Map-utility-profile",
      "urn:csabs:axiom/Map-finite-graph"
    ],
    "reviewStatus": "Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned",
      "urn:csabs:source/utility-lean-CollectionUtilities"
    ],
    "sourceLocator": "Data/Set/Finite/Basic.lean: finite union and subset; Option.or; constructed finite-support override and unequal-lookup support; Catalog.mapDiff_membership",
    "sourceNote": "Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {K : Type u} {V : Type v} (m n : Catalog.Map K V) (k : K), k ∈ Catalog.mapDiff m n ↔ m.lookup k ≠ n.lookup k",
    "leanModelMapping": "k∈diff(m,n) iff lookup(m,k)≠lookup(n,k). Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.",
    "leanModelLimitations": "Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/Map-finite-graph\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\", \"urn:csabs:axiom/Map-utility-profile\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\"}",
    "formulationScope": "registered-witness-type",
    "formulationSource": "urn:csabs:source/utility-lean-CollectionUtilities",
    "formulationLocator": "Catalog.mapDiff_membership"
  }
]
```
<!-- graph-record:end -->
