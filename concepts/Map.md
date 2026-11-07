# Map

A finite partial function associating each present key with exactly one value; absence is distinct from stored values.

**Notation:** m:K⇀V; dom(m) finite

**Stable ID:** `urn:csabs:concept/Map`

**Categories:** Data structures

**Kind:** Abstract data type

**Prerequisites:** [Partial function](PartialFunction.md)

**Specializes:** [Partial function](PartialFunction.md)

**Related concepts:** [Named relational schema with attribute domains](RelationalSchema.md)

## Backlinks

- [Candidate key relative to functional dependencies](CandidateKey.md) — `relatedConcept`
- [Finite JSON document value (interoperable profile)](DocumentValue.md) — `requiresConcept`
- [Finite allocated heap store](HeapStore.md) — `requiresConcept`
- [Finite set-valued multimap](Multimap.md) — `requiresConcept`
- [Ordered collection without duplicates](OrderedSet.md) — `relatedConcept`
- [Finite labelled property graph (single-valued profile)](PropertyGraph.md) — `requiresConcept`
- [Finite RDF 1.1 dataset](RDFDataset.md) — `requiresConcept`
- [Named relational schema with attribute domains](RelationalSchema.md) — `relatedConcept`
- [Finite prefix dictionary](Trie.md) — `requiresConcept`
- [Finite prefix dictionary](Trie.md) — `specializationOf`

## Interface and scope

**axiomBasis:** Selected presentation: A finite partial function associating each present key with exactly one value; absence is distinct from stored values. Governing rules: A finite map is a partial function with a finite defined domain. Empty has no bindings. Updating a key overwrites it and leaves other bindings unchanged. Deleting a key makes it absent and preserves other bindings. Maps are equal if all lookups agree.

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
      "urn:csabs:category/data-structures"
    ],
    "kind": "urn:csabs:kind/abstract-data-type",
    "definition": "A finite partial function associating each present key with exactly one value; absence is distinct from stored values.",
    "notation": "m:K⇀V; dom(m) finite",
    "hasOperation": [
      "urn:csabs:operation/Map-lookup",
      "urn:csabs:operation/Map-set",
      "urn:csabs:operation/Map-delete",
      "urn:csabs:operation/Map-basis-empty"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/Map-finite-graph",
      "urn:csabs:axiom/Map-empty-lookup",
      "urn:csabs:axiom/Map-update-lookup",
      "urn:csabs:axiom/Map-delete-lookup",
      "urn:csabs:axiom/Map-lookup-extensionality"
    ],
    "hasLaw": [
      "urn:csabs:law/Map-core",
      "urn:csabs:law/map-frame"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/Map-update-shadow"
    ],
    "requiresConcept": [
      "urn:csabs:concept/PartialFunction"
    ],
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Instantiate carrier, equality, and stated semantic conventions before using this entry.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: A finite partial function associating each present key with exactly one value; absence is distinct from stored values. Governing rules: A finite map is a partial function with a finite defined domain. Empty has no bindings. Updating a key overwrites it and leaves other bindings unchanged. Deleting a key makes it absent and preserves other bindings. Maps are equal if all lookups agree.",
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
    ]
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
  }
]
```
<!-- graph-record:end -->
