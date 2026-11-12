# Total Order

A partial order in which every two elements are comparable.

**Notation:** ∀x,y∈A: x≤y ∨ y≤x

**Stable ID:** `urn:csabs:concept/TotalOrder`

**Categories:** Order and fixed points

**Kind:** Relation

**Prerequisites:** [Partial Order](PartialOrder.md)

**Specializes:** [Partial Order](PartialOrder.md)

## Backlinks

- [B-tree (balanced multiway search tree)](BTree.md) — `requiresConcept`
- [Finite complete binary min-heap](BinaryHeap.md) — `requiresConcept`
- [Strict binary search tree](BinarySearchTree.md) — `requiresConcept`
- [Nonempty bounded closed interval](ClosedInterval.md) — `requiresConcept`
- [Lamport bakery lock protocol](LamportBakery.md) — `requiresConcept`
- [Priority Queue](PriorityQueue.md) — `requiresConcept`
- [Exact real number](RealNumber.md) — `requiresConcept`

## Mathematical formulation

A total order is a partial order with ∀a,b,a≤b∨b≤a. The selected Lean LinearOrder also supplies decidable equality and comparisons.

**Lean formulation** (in its source module context):

```lean
abbrev TotalOrder (A : Type u) := LinearOrder A
```

**Source:** [`Catalog.TotalOrder`](../lean/Catalog/Order.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Mathlib LinearOrder; adds decidable comparison data to the catalog total partial order.

**Limits:** Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Selected presentation: A partial order in which every two elements are comparable. Governing rules: The order is reflexive. The order is transitive. Mutual ordering implies equality. Any pair is comparable.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**specializationNote:** Keep the same carrier and relation; comparability of every pair is the additional constraint.

**verificationObligation:** Instantiate carrier, equality, and stated semantic conventions before using this entry.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-TotalOrder-basis-le"></a>

### le

`urn:csabs:operation/TotalOrder-basis-le`

**signature:** le : A×A→Prop

**description:** Returns the total-order comparison proposition.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-TotalOrder-reflexive"></a>

### reflexive

`urn:csabs:axiom/TotalOrder-reflexive`

**statement:** The order is reflexive.

**formalStatement:** x≤x

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-TotalOrder-transitive"></a>

### transitive

`urn:csabs:axiom/TotalOrder-transitive`

**statement:** The order is transitive.

**formalStatement:** x≤y ∧ y≤z ⇒ x≤z

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-TotalOrder-antisymmetric"></a>

### antisymmetric

`urn:csabs:axiom/TotalOrder-antisymmetric`

**statement:** Mutual ordering implies equality.

**formalStatement:** x≤y ∧ y≤x ⇒ x=y

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-TotalOrder-comparable"></a>

### comparable

`urn:csabs:axiom/TotalOrder-comparable`

**statement:** Any pair is comparable.

**formalStatement:** x≤y ∨ y≤x

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

<a id="node-urn-csabs-law-TotalOrder-core"></a>

### law/TotalOrder-core

`urn:csabs:law/TotalOrder-core`

**statement:** Each finite nonempty subset has a least element.

**formalStatement:** ∃m∈S ∀x∈S: m≤x, for finite nonempty S⊆A

**reviewStatus:** editorial-summary; not machine-proved

**assumptions:** Use the carrier and semantic convention in the linked concept definition.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [reflexive](TotalOrder.md#node-urn-csabs-axiom-TotalOrder-reflexive); [transitive](TotalOrder.md#node-urn-csabs-axiom-TotalOrder-transitive); [antisymmetric](TotalOrder.md#node-urn-csabs-axiom-TotalOrder-antisymmetric); [comparable](TotalOrder.md#node-urn-csabs-axiom-TotalOrder-comparable)

**provenanceStatus:** legacy-source-missing

## Theorems

<a id="node-urn-csabs-theorem-TotalOrder-minimum-symmetry"></a>

### minimum-symmetry

`urn:csabs:theorem/TotalOrder-minimum-symmetry`

**statement:** The smaller of two comparable elements is independent of their order.

**formalStatement:** min(x,y)=min(y,x)

**proofSketch:** Case split on comparability; antisymmetry handles equality of both ordering directions.

**assumptions:** The explicit basis, carriers, and side conditions stated for TotalOrder apply.

**dependsOn:** [reflexive](TotalOrder.md#node-urn-csabs-axiom-TotalOrder-reflexive); [transitive](TotalOrder.md#node-urn-csabs-axiom-TotalOrder-transitive); [antisymmetric](TotalOrder.md#node-urn-csabs-axiom-TotalOrder-antisymmetric); [comparable](TotalOrder.md#node-urn-csabs-axiom-TotalOrder-comparable)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Concept provenance

- [Mathlib partial-order definitions](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Order/Defs/PartialOrder.html); sourceRole: reference-for-selected-basis

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/TotalOrder",
    "type": "Concept",
    "shortForm": "TotalOrder",
    "fullName": "Total Order",
    "category": [
      "urn:csabs:category/order"
    ],
    "kind": "urn:csabs:kind/relation",
    "definition": "A partial order in which every two elements are comparable.",
    "notation": "∀x,y∈A: x≤y ∨ y≤x",
    "hasOperation": [
      "urn:csabs:operation/TotalOrder-basis-le"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/TotalOrder-reflexive",
      "urn:csabs:axiom/TotalOrder-transitive",
      "urn:csabs:axiom/TotalOrder-antisymmetric",
      "urn:csabs:axiom/TotalOrder-comparable"
    ],
    "hasLaw": [
      "urn:csabs:law/TotalOrder-core"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/TotalOrder-minimum-symmetry"
    ],
    "requiresConcept": [
      "urn:csabs:concept/PartialOrder"
    ],
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Instantiate carrier, equality, and stated semantic conventions before using this entry.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: A partial order in which every two elements are comparable. Governing rules: The order is reflexive. The order is transitive. Mutual ordering implies equality. Any pair is comparable.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "source": [
      "urn:csabs:source/mathlib-order"
    ],
    "specializationOf": [
      "urn:csabs:concept/PartialOrder"
    ],
    "specializationNote": "Keep the same carrier and relation; comparability of every pair is the additional constraint.",
    "leanFormulation": "abbrev TotalOrder (A : Type u) := LinearOrder A",
    "formulationSource": "urn:csabs:source/local-lean-Order",
    "formulationLocator": "Catalog.TotalOrder",
    "formulationScope": "model",
    "leanModelMapping": "Mathlib LinearOrder; adds decidable comparison data to the catalog total partial order.",
    "leanModelLimitations": "Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.",
    "mathematicalFormulation": "A total order is a partial order with ∀a,b,a≤b∨b≤a. The selected Lean LinearOrder also supplies decidable equality and comparisons."
  },
  {
    "id": "urn:csabs:operation/TotalOrder-basis-le",
    "type": "Operation",
    "name": "le",
    "signature": "le : A×A→Prop",
    "description": "Returns the total-order comparison proposition.",
    "concept": "urn:csabs:concept/TotalOrder"
  },
  {
    "id": "urn:csabs:axiom/TotalOrder-reflexive",
    "type": "Axiom",
    "name": "reflexive",
    "statement": "The order is reflexive.",
    "formalStatement": "x≤x",
    "appliesTo": [
      "urn:csabs:concept/TotalOrder"
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
    "id": "urn:csabs:axiom/TotalOrder-transitive",
    "type": "Axiom",
    "name": "transitive",
    "statement": "The order is transitive.",
    "formalStatement": "x≤y ∧ y≤z ⇒ x≤z",
    "appliesTo": [
      "urn:csabs:concept/TotalOrder"
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
    "id": "urn:csabs:axiom/TotalOrder-antisymmetric",
    "type": "Axiom",
    "name": "antisymmetric",
    "statement": "Mutual ordering implies equality.",
    "formalStatement": "x≤y ∧ y≤x ⇒ x=y",
    "appliesTo": [
      "urn:csabs:concept/TotalOrder"
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
    "id": "urn:csabs:axiom/TotalOrder-comparable",
    "type": "Axiom",
    "name": "comparable",
    "statement": "Any pair is comparable.",
    "formalStatement": "x≤y ∨ y≤x",
    "appliesTo": [
      "urn:csabs:concept/TotalOrder"
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
    "id": "urn:csabs:law/TotalOrder-core",
    "type": "Law",
    "statement": "Each finite nonempty subset has a least element.",
    "formalStatement": "∃m∈S ∀x∈S: m≤x, for finite nonempty S⊆A",
    "appliesTo": [
      "urn:csabs:concept/TotalOrder"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "assumptions": [
      "Use the carrier and semantic convention in the linked concept definition."
    ],
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/TotalOrder-reflexive",
      "urn:csabs:axiom/TotalOrder-transitive",
      "urn:csabs:axiom/TotalOrder-antisymmetric",
      "urn:csabs:axiom/TotalOrder-comparable"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/TotalOrder-minimum-symmetry",
    "type": "Theorem",
    "name": "minimum-symmetry",
    "statement": "The smaller of two comparable elements is independent of their order.",
    "formalStatement": "min(x,y)=min(y,x)",
    "proofSketch": "Case split on comparability; antisymmetry handles equality of both ordering directions.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for TotalOrder apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/TotalOrder"
    ],
    "dependsOn": [
      "urn:csabs:axiom/TotalOrder-reflexive",
      "urn:csabs:axiom/TotalOrder-transitive",
      "urn:csabs:axiom/TotalOrder-antisymmetric",
      "urn:csabs:axiom/TotalOrder-comparable"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
