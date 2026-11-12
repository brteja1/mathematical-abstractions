# Finite prefix dictionary

A finite dictionary keyed by finite words, with an explicit whole-key prefix selection operation.

**Notation:** Trie(A,V)=Map(Seq(A),V)

**Stable ID:** `urn:csabs:concept/Trie`

**Categories:** Data structures → Tree structures, Data structures → Sets and mappings

**Kind:** Abstract data type

**Prerequisites:** [Map](Map.md), [Finite sequence (List datatype)](Sequence.md)

**Specializes:** [Map](Map.md)

## Mathematical formulation

The extensional dictionary carrier is a finite partial map A\*⇀V. prefixed(t,p) retains exactly keys k for which ∃s,k=p++s, preserving full keys and their values; no particular node representation is selected.

**Lean formulation** (in its source module context):

```lean
abbrev Trie (A : Type u) (V : Type v) := Catalog.Map (List A) V
```

**Source:** [`Catalog.Trie`](../lean/Catalog/StructuredData.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Trie(A,V)=Map(Seq(A),V). Observable finite-map/prefix interface. Empty word can be a key, and a word can be both stored and a prefix of another. Equality compares key lookups, not radix-node shape or compression; prefix selection retains full keys.

**Limits:** Compiled carrier and selected interface interpretation. Some catalog operations are specified mathematically rather than wrapped as Lean declarations; no blanket proof of claims, algorithms, parsing, liveness or complexity. See individual witnesses.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** The carrier is a finite partial map on Seq(A), with extensional lookup equality; lookup(put(t,k,v),q)=Some(v) if q=k, else lookup(t,q); lookup(prefix(t,p),k)=lookup(t,k) if ∃s,k=p++s, else None

**basisKind:** extensional-structural-definition

**basisScope:** Observable finite-map/prefix interface. Empty word can be a key, and a word can be both stored and a prefix of another. Equality compares key lookups, not radix-node shape or compression; prefix selection retains full keys.

**basisInstantiation:** Map rules apply explicitly at K=Seq(A), with put=set, and the same lookup. Its only added defining rule is prefix selection. Reused rules retain stable IDs and direct applicability links.

**specializationNote:** Instantiate Map at key carrier Seq(A) and value carrier V; finite-domain lookup/put are unchanged. Prefix is a derived query; no node-layout observation is added.

**verificationObligation:** Map carrier, equality, operation definedness and stated profile to the target API or proof context.; Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.; Model coverage does not establish every recorded claim or an implementation refinement.

**reviewStatus:** Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-Trie-lookup"></a>

### lookup

`urn:csabs:operation/Trie-lookup`

**signature:** lookup : Trie(A,V)×Seq(A)→Option(V)

**description:** Returns the exact whole-key binding, if any.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Observable finite-map/prefix interface. Empty word can be a key, and a word can be both stored and a prefix of another. Equality compares key lookups, not radix-node shape or compression; prefix selection retains full keys.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Returns the exact whole-key binding, if any.

**source:** [Paul E. Black: NIST Dictionary of Algorithms and Data Structures, trie](https://xlinux.nist.gov/dads/HTML/trie.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Definition: strings with shared prefix nodes; adapted to observable finite prefix dictionary

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-Trie-put"></a>

### put

`urn:csabs:operation/Trie-put`

**signature:** put : Trie(A,V)×Seq(A)×V→Trie(A,V)

**description:** Overwrites just the whole key.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Observable finite-map/prefix interface. Empty word can be a key, and a word can be both stored and a prefix of another. Equality compares key lookups, not radix-node shape or compression; prefix selection retains full keys.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Overwrites just the whole key.

**source:** [Paul E. Black: NIST Dictionary of Algorithms and Data Structures, trie](https://xlinux.nist.gov/dads/HTML/trie.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Definition: strings with shared prefix nodes; adapted to observable finite prefix dictionary

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-Trie-prefix"></a>

### prefix

`urn:csabs:operation/Trie-prefix`

**signature:** prefix : Trie(A,V)×Seq(A)→Trie(A,V)

**description:** Retains exactly bindings whose whole keys begin with p.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Observable finite-map/prefix interface. Empty word can be a key, and a word can be both stored and a prefix of another. Equality compares key lookups, not radix-node shape or compression; prefix selection retains full keys.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Retains exactly bindings whose whole keys begin with p.

**source:** [Paul E. Black: NIST Dictionary of Algorithms and Data Structures, trie](https://xlinux.nist.gov/dads/HTML/trie.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Definition: strings with shared prefix nodes; adapted to observable finite prefix dictionary

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

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

<a id="node-urn-csabs-axiom-Trie-prefix-equation"></a>

### prefix-equation

`urn:csabs:axiom/Trie-prefix-equation`

**statement:** Defining requirement: lookup(prefix(t,p),k)=lookup(t,k) if ∃s,k=p++s, else None

**formalStatement:** lookup(prefix(t,p),k)=lookup(t,k) if ∃s,k=p++s, else None

**assumptions:** Observable finite-map/prefix interface. Empty word can be a key, and a word can be both stored and a prefix of another. Equality compares key lookups, not radix-node shape or compression; prefix selection retains full keys.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Paul E. Black: NIST Dictionary of Algorithms and Data Structures, trie](https://xlinux.nist.gov/dads/HTML/trie.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Definition: strings with shared prefix nodes; adapted to observable finite prefix dictionary

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-Trie-empty-prefix"></a>

### empty-prefix

`urn:csabs:law/Trie-empty-prefix`

**statement:** prefix(t,[])=t

**formalStatement:** prefix(t,[])=t

**assumptions:** Observable finite-map/prefix interface. Empty word can be a key, and a word can be both stored and a prefix of another. Equality compares key lookups, not radix-node shape or compression; prefix selection retains full keys.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [finite-graph](Map.md#node-urn-csabs-axiom-Map-finite-graph); [lookup-extensionality](Map.md#node-urn-csabs-axiom-Map-lookup-extensionality); [prefix-equation](Trie.md#node-urn-csabs-axiom-Trie-prefix-equation)

**proofSketch:** Every word k=[]++k; all lookups are retained and extensionality gives equality.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Paul E. Black: NIST Dictionary of Algorithms and Data Structures, trie](https://xlinux.nist.gov/dads/HTML/trie.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Definition: strings with shared prefix nodes; adapted to observable finite prefix dictionary

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Theorems

<a id="node-urn-csabs-theorem-Trie-prefix-idempotent"></a>

### prefix-idempotent

`urn:csabs:theorem/Trie-prefix-idempotent`

**statement:** prefix(prefix(t,p),p)=prefix(t,p)

**formalStatement:** prefix(prefix(t,p),p)=prefix(t,p)

**assumptions:** Observable finite-map/prefix interface. Empty word can be a key, and a word can be both stored and a prefix of another. Equality compares key lookups, not radix-node shape or compression; prefix selection retains full keys.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [finite-graph](Map.md#node-urn-csabs-axiom-Map-finite-graph); [lookup-extensionality](Map.md#node-urn-csabs-axiom-Map-lookup-extensionality); [prefix-equation](Trie.md#node-urn-csabs-axiom-Trie-prefix-equation)

**proofSketch:** A matching key survives twice with the same value; a nonmatching key is absent both times.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Paul E. Black: NIST Dictionary of Algorithms and Data Structures, trie](https://xlinux.nist.gov/dads/HTML/trie.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Definition: strings with shared prefix nodes; adapted to observable finite prefix dictionary

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Concept provenance

- [Paul E. Black: NIST Dictionary of Algorithms and Data Structures, trie](https://xlinux.nist.gov/dads/HTML/trie.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Definition: strings with shared prefix nodes; adapted to observable finite prefix dictionary

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/Trie",
    "type": "Concept",
    "shortForm": "Trie",
    "fullName": "Finite prefix dictionary",
    "category": [
      "urn:csabs:category/tree-structures",
      "urn:csabs:category/associative-collections"
    ],
    "kind": "urn:csabs:kind/abstract-data-type",
    "definition": "A finite dictionary keyed by finite words, with an explicit whole-key prefix selection operation.",
    "notation": "Trie(A,V)=Map(Seq(A),V)",
    "requiresConcept": [
      "urn:csabs:concept/Map",
      "urn:csabs:concept/Sequence"
    ],
    "relatedConcept": [],
    "hasOperation": [
      "urn:csabs:operation/Trie-lookup",
      "urn:csabs:operation/Trie-put",
      "urn:csabs:operation/Trie-prefix"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/Map-finite-graph",
      "urn:csabs:axiom/Map-lookup-extensionality",
      "urn:csabs:axiom/Map-update-lookup",
      "urn:csabs:axiom/Trie-prefix-equation"
    ],
    "hasLaw": [
      "urn:csabs:law/Trie-empty-prefix"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/Trie-prefix-idempotent"
    ],
    "axiomBasis": "The carrier is a finite partial map on Seq(A), with extensional lookup equality; lookup(put(t,k,v),q)=Some(v) if q=k, else lookup(t,q); lookup(prefix(t,p),k)=lookup(t,k) if ∃s,k=p++s, else None",
    "basisKind": "extensional-structural-definition",
    "basisScope": "Observable finite-map/prefix interface. Empty word can be a key, and a word can be both stored and a prefix of another. Equality compares key lookups, not radix-node shape or compression; prefix selection retains full keys.",
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Map carrier, equality, operation definedness and stated profile to the target API or proof context.",
      "Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.",
      "Model coverage does not establish every recorded claim or an implementation refinement."
    ],
    "reviewStatus": "Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.",
    "source": [
      "urn:csabs:source/nist-trie-core"
    ],
    "sourceLocator": "Definition: strings with shared prefix nodes; adapted to observable finite prefix dictionary",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/Map"
    ],
    "specializationNote": "Instantiate Map at key carrier Seq(A) and value carrier V; finite-domain lookup/put are unchanged. Prefix is a derived query; no node-layout observation is added.",
    "basisInstantiation": "Map rules apply explicitly at K=Seq(A), with put=set, and the same lookup. Its only added defining rule is prefix selection. Reused rules retain stable IDs and direct applicability links.",
    "leanFormulation": "abbrev Trie (A : Type u) (V : Type v) := Catalog.Map (List A) V",
    "formulationSource": "urn:csabs:source/local-lean-StructuredData",
    "formulationLocator": "Catalog.Trie",
    "formulationScope": "model",
    "leanModelMapping": "Trie(A,V)=Map(Seq(A),V). Observable finite-map/prefix interface. Empty word can be a key, and a word can be both stored and a prefix of another. Equality compares key lookups, not radix-node shape or compression; prefix selection retains full keys.",
    "leanModelLimitations": "Compiled carrier and selected interface interpretation. Some catalog operations are specified mathematically rather than wrapped as Lean declarations; no blanket proof of claims, algorithms, parsing, liveness or complexity. See individual witnesses.",
    "mathematicalFormulation": "The extensional dictionary carrier is a finite partial map A*⇀V. prefixed(t,p) retains exactly keys k for which ∃s,k=p++s, preserving full keys and their values; no particular node representation is selected."
  },
  {
    "id": "urn:csabs:operation/Trie-lookup",
    "type": "Operation",
    "name": "lookup",
    "signature": "lookup : Trie(A,V)×Seq(A)→Option(V)",
    "description": "Returns the exact whole-key binding, if any.",
    "concept": "urn:csabs:concept/Trie",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Observable finite-map/prefix interface. Empty word can be a key, and a word can be both stored and a prefix of another. Equality compares key lookups, not radix-node shape or compression; prefix selection retains full keys.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Returns the exact whole-key binding, if any.",
    "source": [
      "urn:csabs:source/nist-trie-core"
    ],
    "sourceLocator": "Definition: strings with shared prefix nodes; adapted to observable finite prefix dictionary",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/Trie-put",
    "type": "Operation",
    "name": "put",
    "signature": "put : Trie(A,V)×Seq(A)×V→Trie(A,V)",
    "description": "Overwrites just the whole key.",
    "concept": "urn:csabs:concept/Trie",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Observable finite-map/prefix interface. Empty word can be a key, and a word can be both stored and a prefix of another. Equality compares key lookups, not radix-node shape or compression; prefix selection retains full keys.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Overwrites just the whole key.",
    "source": [
      "urn:csabs:source/nist-trie-core"
    ],
    "sourceLocator": "Definition: strings with shared prefix nodes; adapted to observable finite prefix dictionary",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/Trie-prefix",
    "type": "Operation",
    "name": "prefix",
    "signature": "prefix : Trie(A,V)×Seq(A)→Trie(A,V)",
    "description": "Retains exactly bindings whose whole keys begin with p.",
    "concept": "urn:csabs:concept/Trie",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Observable finite-map/prefix interface. Empty word can be a key, and a word can be both stored and a prefix of another. Equality compares key lookups, not radix-node shape or compression; prefix selection retains full keys.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Retains exactly bindings whose whole keys begin with p.",
    "source": [
      "urn:csabs:source/nist-trie-core"
    ],
    "sourceLocator": "Definition: strings with shared prefix nodes; adapted to observable finite prefix dictionary",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/Trie-prefix-equation",
    "type": "Axiom",
    "name": "prefix-equation",
    "statement": "Defining requirement: lookup(prefix(t,p),k)=lookup(t,k) if ∃s,k=p++s, else None",
    "formalStatement": "lookup(prefix(t,p),k)=lookup(t,k) if ∃s,k=p++s, else None",
    "assumptions": [
      "Observable finite-map/prefix interface. Empty word can be a key, and a word can be both stored and a prefix of another. Equality compares key lookups, not radix-node shape or compression; prefix selection retains full keys.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/Trie"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/nist-trie-core"
    ],
    "sourceLocator": "Definition: strings with shared prefix nodes; adapted to observable finite prefix dictionary",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/Trie-empty-prefix",
    "type": "Law",
    "name": "empty-prefix",
    "statement": "prefix(t,[])=t",
    "formalStatement": "prefix(t,[])=t",
    "assumptions": [
      "Observable finite-map/prefix interface. Empty word can be a key, and a word can be both stored and a prefix of another. Equality compares key lookups, not radix-node shape or compression; prefix selection retains full keys.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/Trie"
    ],
    "dependsOn": [
      "urn:csabs:axiom/Map-finite-graph",
      "urn:csabs:axiom/Map-lookup-extensionality",
      "urn:csabs:axiom/Trie-prefix-equation"
    ],
    "proofSketch": "Every word k=[]++k; all lookups are retained and extensionality gives equality.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/nist-trie-core"
    ],
    "sourceLocator": "Definition: strings with shared prefix nodes; adapted to observable finite prefix dictionary",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/Trie-prefix-idempotent",
    "type": "Theorem",
    "name": "prefix-idempotent",
    "statement": "prefix(prefix(t,p),p)=prefix(t,p)",
    "formalStatement": "prefix(prefix(t,p),p)=prefix(t,p)",
    "assumptions": [
      "Observable finite-map/prefix interface. Empty word can be a key, and a word can be both stored and a prefix of another. Equality compares key lookups, not radix-node shape or compression; prefix selection retains full keys.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/Trie"
    ],
    "dependsOn": [
      "urn:csabs:axiom/Map-finite-graph",
      "urn:csabs:axiom/Map-lookup-extensionality",
      "urn:csabs:axiom/Trie-prefix-equation"
    ],
    "proofSketch": "A matching key survives twice with the same value; a nonmatching key is absent both times.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/nist-trie-core"
    ],
    "sourceLocator": "Definition: strings with shared prefix nodes; adapted to observable finite prefix dictionary",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
