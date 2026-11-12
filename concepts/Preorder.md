# Preorder

A reflexive and transitive relation on a carrier; distinct values may be mutually related.

**Notation:** ≤ ⊆ A×A; x≤x; x≤y ∧ y≤z ⇒ x≤z

**Stable ID:** `urn:csabs:concept/Preorder`

**Categories:** Order and fixed points

**Kind:** Relation

**Prerequisites:** [Binary relation](Relation.md)

**Specializes:** [Binary relation](Relation.md)

## Backlinks

- [Equivalence relation](EquivalenceRelation.md) — `specializationOf`
- [Partial Order](PartialOrder.md) — `requiresConcept`
- [Partial Order](PartialOrder.md) — `specializationOf`

## Mathematical formulation

A preorder is (A,≤) with ∀a,a≤a and ∀a,b,c,a≤b∧b≤c⇒a≤c. Antisymmetry is not imposed, so a≤b∧b≤a need not imply a=b.

**Lean formulation** (in its source module context):

```lean
abbrev Preorder (A : Type u) := _root_.Preorder A
```

**Source:** [`Catalog.Preorder`](../lean/Catalog/Order.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Mathlib Preorder with reflexivity and transitivity; no antisymmetry assumed.

**Limits:** Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Selected presentation: A reflexive and transitive relation on a carrier; distinct values may be mutually related. Governing rules: The order is reflexive. The order is transitive.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**specializationNote:** Use A=B and the same relation; reflexivity and transitivity are additional constraints.

**verificationObligation:** Instantiate carrier, equality, and stated semantic conventions before using this entry.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-Preorder-basis-le"></a>

### le

`urn:csabs:operation/Preorder-basis-le`

**signature:** le : A×A→Prop

**description:** Tests the abstract relation as a proposition, not a promised executable Boolean procedure.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-Preorder-reflexive"></a>

### reflexive

`urn:csabs:axiom/Preorder-reflexive`

**statement:** The order is reflexive.

**formalStatement:** ∀x∈A:x≤x

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Preorder-transitive"></a>

### transitive

`urn:csabs:axiom/Preorder-transitive`

**statement:** The order is transitive.

**formalStatement:** x≤y ∧ y≤z ⇒ x≤z

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

<a id="node-urn-csabs-law-Preorder-core"></a>

### law/Preorder-core

`urn:csabs:law/Preorder-core`

**statement:** Mutual comparability in both directions defines an equivalence relation.

**formalStatement:** x≈y iff x≤y ∧ y≤x

**reviewStatus:** editorial-summary; not machine-proved

**assumptions:** Use the carrier and semantic convention in the linked concept definition.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [reflexive](Preorder.md#node-urn-csabs-axiom-Preorder-reflexive); [transitive](Preorder.md#node-urn-csabs-axiom-Preorder-transitive)

**provenanceStatus:** legacy-source-missing

## Theorems

<a id="node-urn-csabs-theorem-Preorder-strict-part-asymmetry"></a>

### strict-part-asymmetry

`urn:csabs:theorem/Preorder-strict-part-asymmetry`

**statement:** The strict part of a preorder is asymmetric.

**formalStatement:** x<y iff x≤y ∧ ¬(y≤x); x<y ⇒ ¬(y<x)

**proofSketch:** The first strict inequality directly excludes the reverse non-strict premise.

**assumptions:** The explicit basis, carriers, and side conditions stated for Preorder apply.

**dependsOn:** [reflexive](Preorder.md#node-urn-csabs-axiom-Preorder-reflexive); [transitive](Preorder.md#node-urn-csabs-axiom-Preorder-transitive)

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
    "id": "urn:csabs:concept/Preorder",
    "type": "Concept",
    "shortForm": "Preorder",
    "fullName": "Preorder",
    "category": [
      "urn:csabs:category/order"
    ],
    "kind": "urn:csabs:kind/relation",
    "definition": "A reflexive and transitive relation on a carrier; distinct values may be mutually related.",
    "notation": "≤ ⊆ A×A; x≤x; x≤y ∧ y≤z ⇒ x≤z",
    "hasOperation": [
      "urn:csabs:operation/Preorder-basis-le"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/Preorder-reflexive",
      "urn:csabs:axiom/Preorder-transitive"
    ],
    "hasLaw": [
      "urn:csabs:law/Preorder-core"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/Preorder-strict-part-asymmetry"
    ],
    "requiresConcept": [
      "urn:csabs:concept/Relation"
    ],
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Instantiate carrier, equality, and stated semantic conventions before using this entry.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: A reflexive and transitive relation on a carrier; distinct values may be mutually related. Governing rules: The order is reflexive. The order is transitive.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "source": [
      "urn:csabs:source/mathlib-order"
    ],
    "specializationOf": [
      "urn:csabs:concept/Relation"
    ],
    "specializationNote": "Use A=B and the same relation; reflexivity and transitivity are additional constraints.",
    "leanFormulation": "abbrev Preorder (A : Type u) := _root_.Preorder A",
    "formulationSource": "urn:csabs:source/local-lean-Order",
    "formulationLocator": "Catalog.Preorder",
    "formulationScope": "model",
    "leanModelMapping": "Mathlib Preorder with reflexivity and transitivity; no antisymmetry assumed.",
    "leanModelLimitations": "Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.",
    "mathematicalFormulation": "A preorder is (A,≤) with ∀a,a≤a and ∀a,b,c,a≤b∧b≤c⇒a≤c. Antisymmetry is not imposed, so a≤b∧b≤a need not imply a=b."
  },
  {
    "id": "urn:csabs:operation/Preorder-basis-le",
    "type": "Operation",
    "name": "le",
    "signature": "le : A×A→Prop",
    "description": "Tests the abstract relation as a proposition, not a promised executable Boolean procedure.",
    "concept": "urn:csabs:concept/Preorder"
  },
  {
    "id": "urn:csabs:axiom/Preorder-reflexive",
    "type": "Axiom",
    "name": "reflexive",
    "statement": "The order is reflexive.",
    "formalStatement": "∀x∈A:x≤x",
    "appliesTo": [
      "urn:csabs:concept/Preorder"
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
    "id": "urn:csabs:axiom/Preorder-transitive",
    "type": "Axiom",
    "name": "transitive",
    "statement": "The order is transitive.",
    "formalStatement": "x≤y ∧ y≤z ⇒ x≤z",
    "appliesTo": [
      "urn:csabs:concept/Preorder"
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
    "id": "urn:csabs:law/Preorder-core",
    "type": "Law",
    "statement": "Mutual comparability in both directions defines an equivalence relation.",
    "formalStatement": "x≈y iff x≤y ∧ y≤x",
    "appliesTo": [
      "urn:csabs:concept/Preorder"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "assumptions": [
      "Use the carrier and semantic convention in the linked concept definition."
    ],
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/Preorder-reflexive",
      "urn:csabs:axiom/Preorder-transitive"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/Preorder-strict-part-asymmetry",
    "type": "Theorem",
    "name": "strict-part-asymmetry",
    "statement": "The strict part of a preorder is asymmetric.",
    "formalStatement": "x<y iff x≤y ∧ ¬(y≤x); x<y ⇒ ¬(y<x)",
    "proofSketch": "The first strict inequality directly excludes the reverse non-strict premise.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for Preorder apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/Preorder"
    ],
    "dependsOn": [
      "urn:csabs:axiom/Preorder-reflexive",
      "urn:csabs:axiom/Preorder-transitive"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
