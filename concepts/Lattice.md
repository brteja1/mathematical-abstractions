# Lattice

A partially ordered set where every pair has a greatest lower bound and a least upper bound.

**Notation:** (L,≤,∧,∨); x∧y=glb{x,y}; x∨y=lub{x,y}

**Stable ID:** `urn:csabs:concept/Lattice`

**Categories:** Order and fixed points

**Kind:** Mathematical structure

**Prerequisites:** [Partial Order](PartialOrder.md)

**Specializes:** [Partial Order](PartialOrder.md)

## Backlinks

- [Boolean algebra](BooleanAlgebra.md) — `specializationOf`
- [Complete Lattice](CompleteLattice.md) — `requiresConcept`
- [Complete Lattice](CompleteLattice.md) — `specializationOf`

## Interface and scope

**axiomBasis:** Selected presentation: A partially ordered set where every pair has a greatest lower bound and a least upper bound. Governing rules: The underlying relation is a partial order. Meet is the greatest lower bound. Join is the least upper bound.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**specializationNote:** Retain the underlying carrier and order; meet and join are the specified binary greatest lower and least upper bounds.

**verificationObligation:** Instantiate carrier, equality, and stated semantic conventions before using this entry.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

**provenanceStatus:** legacy-source-missing

## Operations

<a id="node-urn-csabs-operation-Lattice-meet"></a>

### meet

`urn:csabs:operation/Lattice-meet`

**signature:** ∧ : L×L→L

**description:** Returns the greatest lower bound of the two inputs.

<a id="node-urn-csabs-operation-Lattice-join"></a>

### join

`urn:csabs:operation/Lattice-join`

**signature:** ∨ : L×L→L

**description:** Returns the least upper bound of the two inputs.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-Lattice-partial-order"></a>

### partial-order

`urn:csabs:axiom/Lattice-partial-order`

**statement:** The underlying relation is a partial order.

**formalStatement:** x≤x; x≤y∧y≤z⇒x≤z; x≤y∧y≤x⇒x=y

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Lattice-meet-bound"></a>

### meet-bound

`urn:csabs:axiom/Lattice-meet-bound`

**statement:** Meet is the greatest lower bound.

**formalStatement:** z≤x∧y iff z≤x ∧ z≤y

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Lattice-join-bound"></a>

### join-bound

`urn:csabs:axiom/Lattice-join-bound`

**statement:** Join is the least upper bound.

**formalStatement:** x∨y≤z iff x≤z ∧ y≤z

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

<a id="node-urn-csabs-law-Lattice-core"></a>

### law/Lattice-core

`urn:csabs:law/Lattice-core`

**statement:** Meet and join obey absorption.

**formalStatement:** x∧(x∨y)=x; x∨(x∧y)=x

**reviewStatus:** editorial-summary; not machine-proved

**assumptions:** Use the carrier and semantic convention in the linked concept definition.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [partial-order](Lattice.md#node-urn-csabs-axiom-Lattice-partial-order); [meet-bound](Lattice.md#node-urn-csabs-axiom-Lattice-meet-bound); [join-bound](Lattice.md#node-urn-csabs-axiom-Lattice-join-bound)

**provenanceStatus:** legacy-source-missing

## Theorems

<a id="node-urn-csabs-theorem-Lattice-meet-idempotence"></a>

### meet-idempotence

`urn:csabs:theorem/Lattice-meet-idempotence`

**statement:** Meeting an element with itself yields that element.

**formalStatement:** x∧x=x

**proofSketch:** The lower bounds of {x,x} are exactly those of x; greatest-lower-bound uniqueness gives equality.

**assumptions:** The explicit basis, carriers, and side conditions stated for Lattice apply.

**dependsOn:** [partial-order](Lattice.md#node-urn-csabs-axiom-Lattice-partial-order); [meet-bound](Lattice.md#node-urn-csabs-axiom-Lattice-meet-bound); [join-bound](Lattice.md#node-urn-csabs-axiom-Lattice-join-bound)

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
    "id": "urn:csabs:concept/Lattice",
    "type": "Concept",
    "shortForm": "Lattice",
    "fullName": "Lattice",
    "category": [
      "urn:csabs:category/order"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "A partially ordered set where every pair has a greatest lower bound and a least upper bound.",
    "notation": "(L,≤,∧,∨); x∧y=glb{x,y}; x∨y=lub{x,y}",
    "hasOperation": [
      "urn:csabs:operation/Lattice-meet",
      "urn:csabs:operation/Lattice-join"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/Lattice-partial-order",
      "urn:csabs:axiom/Lattice-meet-bound",
      "urn:csabs:axiom/Lattice-join-bound"
    ],
    "hasLaw": [
      "urn:csabs:law/Lattice-core"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/Lattice-meet-idempotence"
    ],
    "requiresConcept": [
      "urn:csabs:concept/PartialOrder"
    ],
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Instantiate carrier, equality, and stated semantic conventions before using this entry.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: A partially ordered set where every pair has a greatest lower bound and a least upper bound. Governing rules: The underlying relation is a partial order. Meet is the greatest lower bound. Join is the least upper bound.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "provenanceStatus": "legacy-source-missing",
    "specializationOf": [
      "urn:csabs:concept/PartialOrder"
    ],
    "specializationNote": "Retain the underlying carrier and order; meet and join are the specified binary greatest lower and least upper bounds."
  },
  {
    "id": "urn:csabs:operation/Lattice-meet",
    "type": "Operation",
    "name": "meet",
    "signature": "∧ : L×L→L",
    "description": "Returns the greatest lower bound of the two inputs.",
    "concept": "urn:csabs:concept/Lattice"
  },
  {
    "id": "urn:csabs:operation/Lattice-join",
    "type": "Operation",
    "name": "join",
    "signature": "∨ : L×L→L",
    "description": "Returns the least upper bound of the two inputs.",
    "concept": "urn:csabs:concept/Lattice"
  },
  {
    "id": "urn:csabs:axiom/Lattice-partial-order",
    "type": "Axiom",
    "name": "partial-order",
    "statement": "The underlying relation is a partial order.",
    "formalStatement": "x≤x; x≤y∧y≤z⇒x≤z; x≤y∧y≤x⇒x=y",
    "appliesTo": [
      "urn:csabs:concept/Lattice"
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
    "id": "urn:csabs:axiom/Lattice-meet-bound",
    "type": "Axiom",
    "name": "meet-bound",
    "statement": "Meet is the greatest lower bound.",
    "formalStatement": "z≤x∧y iff z≤x ∧ z≤y",
    "appliesTo": [
      "urn:csabs:concept/Lattice"
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
    "id": "urn:csabs:axiom/Lattice-join-bound",
    "type": "Axiom",
    "name": "join-bound",
    "statement": "Join is the least upper bound.",
    "formalStatement": "x∨y≤z iff x≤z ∧ y≤z",
    "appliesTo": [
      "urn:csabs:concept/Lattice"
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
    "id": "urn:csabs:law/Lattice-core",
    "type": "Law",
    "statement": "Meet and join obey absorption.",
    "formalStatement": "x∧(x∨y)=x; x∨(x∧y)=x",
    "appliesTo": [
      "urn:csabs:concept/Lattice"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "assumptions": [
      "Use the carrier and semantic convention in the linked concept definition."
    ],
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/Lattice-partial-order",
      "urn:csabs:axiom/Lattice-meet-bound",
      "urn:csabs:axiom/Lattice-join-bound"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/Lattice-meet-idempotence",
    "type": "Theorem",
    "name": "meet-idempotence",
    "statement": "Meeting an element with itself yields that element.",
    "formalStatement": "x∧x=x",
    "proofSketch": "The lower bounds of {x,x} are exactly those of x; greatest-lower-bound uniqueness gives equality.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for Lattice apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/Lattice"
    ],
    "dependsOn": [
      "urn:csabs:axiom/Lattice-partial-order",
      "urn:csabs:axiom/Lattice-meet-bound",
      "urn:csabs:axiom/Lattice-join-bound"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
