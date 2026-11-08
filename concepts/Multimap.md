# Finite set-valued multimap

A finite relation of key/value pairs with a set of associated values at each key.

**Notation:** M⊆fin K×V; values_M(k)={v | (k,v)∈M}

**Stable ID:** `urn:csabs:concept/Multimap`

**Categories:** Data structures → Sets and mappings

**Kind:** Abstract data type

**Prerequisites:** [Finite set collection](FiniteSet.md), [Map](Map.md), [Binary relation](Relation.md)

## Interface and scope

**axiomBasis:** v∈values(M,k) ⇔ (k,v)∈M; (x,y)∈insert(M,k,v) ⇔ (x,y)=(k,v) ∨ (x,y)∈M; (x,y)∈remove(M,k,v) ⇔ (x,y)∈M ∧ (x,y)≠(k,v)

**basisKind:** extensional-structural-definition

**basisScope:** No duplicate pair or ordering. Missing key yields empty set, not None; there are no explicit stored empty buckets. List-valued or bag-valued multimaps are different variants. Equality is pair-set equality.

**verificationObligation:** Map carrier, equality, operation definedness and stated profile to the target API or proof context.; Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.; Model coverage does not establish every recorded claim or an implementation refinement.

**reviewStatus:** Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-Multimap-values"></a>

### values

`urn:csabs:operation/Multimap-values`

**signature:** values : Multi(K,V)×K→FinSet(V)

**description:** Returns {v | (k,v)∈M}.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. No duplicate pair or ordering. Missing key yields empty set, not None; there are no explicit stored empty buckets. List-valued or bag-valued multimaps are different variants. Equality is pair-set equality.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Returns {v | (k,v)∈M}.

**source:** [Guava 19.0: SetMultimap](https://guava.dev/releases/19.0/api/docs/com/google/common/collect/SetMultimap.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Interface contract; get, put, remove, equals; no duplicate key/value pairs

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-Multimap-insert"></a>

### insert

`urn:csabs:operation/Multimap-insert`

**signature:** insert : Multi(K,V)×K×V→Multi(K,V)

**description:** insert(M,k,v)=M∪{(k,v)}.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. No duplicate pair or ordering. Missing key yields empty set, not None; there are no explicit stored empty buckets. List-valued or bag-valued multimaps are different variants. Equality is pair-set equality.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** insert(M,k,v)=M∪{(k,v)}.

**source:** [Guava 19.0: SetMultimap](https://guava.dev/releases/19.0/api/docs/com/google/common/collect/SetMultimap.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Interface contract; get, put, remove, equals; no duplicate key/value pairs

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-Multimap-remove"></a>

### remove

`urn:csabs:operation/Multimap-remove`

**signature:** remove : Multi(K,V)×K×V→Multi(K,V)

**description:** remove(M,k,v)=M∖{(k,v)}.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. No duplicate pair or ordering. Missing key yields empty set, not None; there are no explicit stored empty buckets. List-valued or bag-valued multimaps are different variants. Equality is pair-set equality.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** remove(M,k,v)=M∖{(k,v)}.

**source:** [Guava 19.0: SetMultimap](https://guava.dev/releases/19.0/api/docs/com/google/common/collect/SetMultimap.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Interface contract; get, put, remove, equals; no duplicate key/value pairs

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-Multimap-values-definition"></a>

### values-definition

`urn:csabs:axiom/Multimap-values-definition`

**statement:** Defining requirement: v∈values(M,k) ⇔ (k,v)∈M

**formalStatement:** v∈values(M,k) ⇔ (k,v)∈M

**assumptions:** No duplicate pair or ordering. Missing key yields empty set, not None; there are no explicit stored empty buckets. List-valued or bag-valued multimaps are different variants. Equality is pair-set equality.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Guava 19.0: SetMultimap](https://guava.dev/releases/19.0/api/docs/com/google/common/collect/SetMultimap.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Interface contract; get, put, remove, equals; no duplicate key/value pairs

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-Multimap-insert-definition"></a>

### insert-definition

`urn:csabs:axiom/Multimap-insert-definition`

**statement:** Defining requirement: (x,y)∈insert(M,k,v) ⇔ (x,y)=(k,v) ∨ (x,y)∈M

**formalStatement:** (x,y)∈insert(M,k,v) ⇔ (x,y)=(k,v) ∨ (x,y)∈M

**assumptions:** No duplicate pair or ordering. Missing key yields empty set, not None; there are no explicit stored empty buckets. List-valued or bag-valued multimaps are different variants. Equality is pair-set equality.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Guava 19.0: SetMultimap](https://guava.dev/releases/19.0/api/docs/com/google/common/collect/SetMultimap.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Interface contract; get, put, remove, equals; no duplicate key/value pairs

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-Multimap-remove-definition"></a>

### remove-definition

`urn:csabs:axiom/Multimap-remove-definition`

**statement:** Defining requirement: (x,y)∈remove(M,k,v) ⇔ (x,y)∈M ∧ (x,y)≠(k,v)

**formalStatement:** (x,y)∈remove(M,k,v) ⇔ (x,y)∈M ∧ (x,y)≠(k,v)

**assumptions:** No duplicate pair or ordering. Missing key yields empty set, not None; there are no explicit stored empty buckets. List-valued or bag-valued multimaps are different variants. Equality is pair-set equality.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Guava 19.0: SetMultimap](https://guava.dev/releases/19.0/api/docs/com/google/common/collect/SetMultimap.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Interface contract; get, put, remove, equals; no duplicate key/value pairs

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-Multimap-insert-idempotent"></a>

### insert-idempotent

`urn:csabs:law/Multimap-insert-idempotent`

**statement:** insert(insert(M,k,v),k,v)=insert(M,k,v)

**formalStatement:** insert(insert(M,k,v),k,v)=insert(M,k,v)

**assumptions:** No duplicate pair or ordering. Missing key yields empty set, not None; there are no explicit stored empty buckets. List-valued or bag-valued multimaps are different variants. Equality is pair-set equality.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [insert-definition](Multimap.md#node-urn-csabs-axiom-Multimap-insert-definition)

**proofSketch:** Pair membership on both sides is the same disjunction; use set extensionality.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Guava 19.0: SetMultimap](https://guava.dev/releases/19.0/api/docs/com/google/common/collect/SetMultimap.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Interface contract; get, put, remove, equals; no duplicate key/value pairs

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Theorems

<a id="node-urn-csabs-theorem-Multimap-remove-absent"></a>

### remove-absent

`urn:csabs:theorem/Multimap-remove-absent`

**statement:** v∉values(remove(M,k,v),k)

**formalStatement:** v∉values(remove(M,k,v),k)

**assumptions:** No duplicate pair or ordering. Missing key yields empty set, not None; there are no explicit stored empty buckets. List-valued or bag-valued multimaps are different variants. Equality is pair-set equality.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [values-definition](Multimap.md#node-urn-csabs-axiom-Multimap-values-definition); [remove-definition](Multimap.md#node-urn-csabs-axiom-Multimap-remove-definition)

**proofSketch:** Expand the pair-removal and values equations; equality of the removed pair contradicts membership.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Guava 19.0: SetMultimap](https://guava.dev/releases/19.0/api/docs/com/google/common/collect/SetMultimap.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Interface contract; get, put, remove, equals; no duplicate key/value pairs

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Concept provenance

- [Guava 19.0: SetMultimap](https://guava.dev/releases/19.0/api/docs/com/google/common/collect/SetMultimap.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Interface contract; get, put, remove, equals; no duplicate key/value pairs

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/Multimap",
    "type": "Concept",
    "shortForm": "Multimap",
    "fullName": "Finite set-valued multimap",
    "category": [
      "urn:csabs:category/associative-collections"
    ],
    "kind": "urn:csabs:kind/abstract-data-type",
    "definition": "A finite relation of key/value pairs with a set of associated values at each key.",
    "notation": "M⊆fin K×V; values_M(k)={v | (k,v)∈M}",
    "requiresConcept": [
      "urn:csabs:concept/FiniteSet",
      "urn:csabs:concept/Map",
      "urn:csabs:concept/Relation"
    ],
    "relatedConcept": [],
    "hasOperation": [
      "urn:csabs:operation/Multimap-values",
      "urn:csabs:operation/Multimap-insert",
      "urn:csabs:operation/Multimap-remove"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/Multimap-values-definition",
      "urn:csabs:axiom/Multimap-insert-definition",
      "urn:csabs:axiom/Multimap-remove-definition"
    ],
    "hasLaw": [
      "urn:csabs:law/Multimap-insert-idempotent"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/Multimap-remove-absent"
    ],
    "axiomBasis": "v∈values(M,k) ⇔ (k,v)∈M; (x,y)∈insert(M,k,v) ⇔ (x,y)=(k,v) ∨ (x,y)∈M; (x,y)∈remove(M,k,v) ⇔ (x,y)∈M ∧ (x,y)≠(k,v)",
    "basisKind": "extensional-structural-definition",
    "basisScope": "No duplicate pair or ordering. Missing key yields empty set, not None; there are no explicit stored empty buckets. List-valued or bag-valued multimaps are different variants. Equality is pair-set equality.",
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Map carrier, equality, operation definedness and stated profile to the target API or proof context.",
      "Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.",
      "Model coverage does not establish every recorded claim or an implementation refinement."
    ],
    "reviewStatus": "Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.",
    "source": [
      "urn:csabs:source/guava-set-multimap-core"
    ],
    "sourceLocator": "Interface contract; get, put, remove, equals; no duplicate key/value pairs",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/Multimap-values",
    "type": "Operation",
    "name": "values",
    "signature": "values : Multi(K,V)×K→FinSet(V)",
    "description": "Returns {v | (k,v)∈M}.",
    "concept": "urn:csabs:concept/Multimap",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. No duplicate pair or ordering. Missing key yields empty set, not None; there are no explicit stored empty buckets. List-valued or bag-valued multimaps are different variants. Equality is pair-set equality.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Returns {v | (k,v)∈M}.",
    "source": [
      "urn:csabs:source/guava-set-multimap-core"
    ],
    "sourceLocator": "Interface contract; get, put, remove, equals; no duplicate key/value pairs",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/Multimap-insert",
    "type": "Operation",
    "name": "insert",
    "signature": "insert : Multi(K,V)×K×V→Multi(K,V)",
    "description": "insert(M,k,v)=M∪{(k,v)}.",
    "concept": "urn:csabs:concept/Multimap",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. No duplicate pair or ordering. Missing key yields empty set, not None; there are no explicit stored empty buckets. List-valued or bag-valued multimaps are different variants. Equality is pair-set equality.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "insert(M,k,v)=M∪{(k,v)}.",
    "source": [
      "urn:csabs:source/guava-set-multimap-core"
    ],
    "sourceLocator": "Interface contract; get, put, remove, equals; no duplicate key/value pairs",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/Multimap-remove",
    "type": "Operation",
    "name": "remove",
    "signature": "remove : Multi(K,V)×K×V→Multi(K,V)",
    "description": "remove(M,k,v)=M∖{(k,v)}.",
    "concept": "urn:csabs:concept/Multimap",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. No duplicate pair or ordering. Missing key yields empty set, not None; there are no explicit stored empty buckets. List-valued or bag-valued multimaps are different variants. Equality is pair-set equality.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "remove(M,k,v)=M∖{(k,v)}.",
    "source": [
      "urn:csabs:source/guava-set-multimap-core"
    ],
    "sourceLocator": "Interface contract; get, put, remove, equals; no duplicate key/value pairs",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/Multimap-values-definition",
    "type": "Axiom",
    "name": "values-definition",
    "statement": "Defining requirement: v∈values(M,k) ⇔ (k,v)∈M",
    "formalStatement": "v∈values(M,k) ⇔ (k,v)∈M",
    "assumptions": [
      "No duplicate pair or ordering. Missing key yields empty set, not None; there are no explicit stored empty buckets. List-valued or bag-valued multimaps are different variants. Equality is pair-set equality.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/Multimap"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/guava-set-multimap-core"
    ],
    "sourceLocator": "Interface contract; get, put, remove, equals; no duplicate key/value pairs",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/Multimap-insert-definition",
    "type": "Axiom",
    "name": "insert-definition",
    "statement": "Defining requirement: (x,y)∈insert(M,k,v) ⇔ (x,y)=(k,v) ∨ (x,y)∈M",
    "formalStatement": "(x,y)∈insert(M,k,v) ⇔ (x,y)=(k,v) ∨ (x,y)∈M",
    "assumptions": [
      "No duplicate pair or ordering. Missing key yields empty set, not None; there are no explicit stored empty buckets. List-valued or bag-valued multimaps are different variants. Equality is pair-set equality.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/Multimap"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/guava-set-multimap-core"
    ],
    "sourceLocator": "Interface contract; get, put, remove, equals; no duplicate key/value pairs",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/Multimap-remove-definition",
    "type": "Axiom",
    "name": "remove-definition",
    "statement": "Defining requirement: (x,y)∈remove(M,k,v) ⇔ (x,y)∈M ∧ (x,y)≠(k,v)",
    "formalStatement": "(x,y)∈remove(M,k,v) ⇔ (x,y)∈M ∧ (x,y)≠(k,v)",
    "assumptions": [
      "No duplicate pair or ordering. Missing key yields empty set, not None; there are no explicit stored empty buckets. List-valued or bag-valued multimaps are different variants. Equality is pair-set equality.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/Multimap"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/guava-set-multimap-core"
    ],
    "sourceLocator": "Interface contract; get, put, remove, equals; no duplicate key/value pairs",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/Multimap-insert-idempotent",
    "type": "Law",
    "name": "insert-idempotent",
    "statement": "insert(insert(M,k,v),k,v)=insert(M,k,v)",
    "formalStatement": "insert(insert(M,k,v),k,v)=insert(M,k,v)",
    "assumptions": [
      "No duplicate pair or ordering. Missing key yields empty set, not None; there are no explicit stored empty buckets. List-valued or bag-valued multimaps are different variants. Equality is pair-set equality.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/Multimap"
    ],
    "dependsOn": [
      "urn:csabs:axiom/Multimap-insert-definition"
    ],
    "proofSketch": "Pair membership on both sides is the same disjunction; use set extensionality.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/guava-set-multimap-core"
    ],
    "sourceLocator": "Interface contract; get, put, remove, equals; no duplicate key/value pairs",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/Multimap-remove-absent",
    "type": "Theorem",
    "name": "remove-absent",
    "statement": "v∉values(remove(M,k,v),k)",
    "formalStatement": "v∉values(remove(M,k,v),k)",
    "assumptions": [
      "No duplicate pair or ordering. Missing key yields empty set, not None; there are no explicit stored empty buckets. List-valued or bag-valued multimaps are different variants. Equality is pair-set equality.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/Multimap"
    ],
    "dependsOn": [
      "urn:csabs:axiom/Multimap-values-definition",
      "urn:csabs:axiom/Multimap-remove-definition"
    ],
    "proofSketch": "Expand the pair-removal and values equations; equality of the removed pair contradicts membership.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/guava-set-multimap-core"
    ],
    "sourceLocator": "Interface contract; get, put, remove, equals; no duplicate key/value pairs",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
