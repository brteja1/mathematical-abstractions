# Partial Order

A reflexive, antisymmetric, transitive relation.

**Notation:** (A,≤); x≤y ∧ y≤x ⇒ x=y

**Stable ID:** `urn:csabs:concept/PartialOrder`

**Categories:** Order and fixed points

**Kind:** Relation

**Prerequisites:** [Preorder](Preorder.md)

**Specializes:** [Preorder](Preorder.md)

## Backlinks

- [Single-inheritance class table and dynamic dispatch](ClassTable.md) — `relatedConcept`
- [Closure Operator](ClosureOperator.md) — `requiresConcept`
- [Galois Connection](GaloisConnection.md) — `requiresConcept`
- [Happens Before](HappensBefore.md) — `requiresConcept`
- [Join semilattice](JoinSemilattice.md) — `requiresConcept`
- [Join semilattice](JoinSemilattice.md) — `specializationOf`
- [Lattice](Lattice.md) — `requiresConcept`
- [Lattice](Lattice.md) — `specializationOf`
- [Monotone Function](MonotoneFunction.md) — `requiresConcept`
- [State-based CRDT replication algebra](StateBasedCRDT.md) — `requiresConcept`
- [Class template partial-specialization selection](TemplateSpecialization.md) — `requiresConcept`
- [Total Order](TotalOrder.md) — `requiresConcept`
- [Total Order](TotalOrder.md) — `specializationOf`

## Mathematical formulation

A partial order is a preorder (A,≤) satisfying ∀a,b,a≤b∧b≤a⇒a=b. The empty carrier is permitted.

**Lean formulation** (in its source module context):

```lean
abbrev PartialOrder (A : Type u) := _root_.PartialOrder A
```

**Source:** [`Catalog.PartialOrder`](../lean/Catalog/Order.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Mathlib PartialOrder; antisymmetry uses Lean equality.

**Limits:** Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Selected presentation: A reflexive, antisymmetric, transitive relation. Governing rules: The order is reflexive. The order is transitive. Mutual ordering implies equality.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**specializationNote:** Keep the same carrier and relation; antisymmetry is the additional constraint.

**verificationObligation:** Instantiate carrier, equality, and stated semantic conventions before using this entry.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-PartialOrder-basis-le"></a>

### le

`urn:csabs:operation/PartialOrder-basis-le`

**signature:** le : A×A→Prop

**description:** Returns the proposition that the first element precedes the second.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-PartialOrder-reflexive"></a>

### reflexive

`urn:csabs:axiom/PartialOrder-reflexive`

**statement:** The order is reflexive.

**formalStatement:** ∀x∈A:x≤x

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-PartialOrder-transitive"></a>

### transitive

`urn:csabs:axiom/PartialOrder-transitive`

**statement:** The order is transitive.

**formalStatement:** x≤y ∧ y≤z ⇒ x≤z

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-PartialOrder-antisymmetric"></a>

### antisymmetric

`urn:csabs:axiom/PartialOrder-antisymmetric`

**statement:** Mutual ordering implies equality.

**formalStatement:** x≤y ∧ y≤x ⇒ x=y

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

<a id="node-urn-csabs-law-PartialOrder-core"></a>

### law/PartialOrder-core

`urn:csabs:law/PartialOrder-core`

**statement:** A finite nonempty partially ordered set has a minimal element.

**formalStatement:** A finite ∧ A≠∅ ⇒ ∃m∈A ∀x∈A: x≤m⇒x=m

**reviewStatus:** editorial-summary; not machine-proved

**assumptions:** Use the carrier and semantic convention in the linked concept definition.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [reflexive](PartialOrder.md#node-urn-csabs-axiom-PartialOrder-reflexive); [transitive](PartialOrder.md#node-urn-csabs-axiom-PartialOrder-transitive); [antisymmetric](PartialOrder.md#node-urn-csabs-axiom-PartialOrder-antisymmetric)

**provenanceStatus:** legacy-source-missing

## Theorems

<a id="node-urn-csabs-theorem-PartialOrder-order-extensionality"></a>

### order-extensionality

`urn:csabs:theorem/PartialOrder-order-extensionality`

**statement:** Elements with the same upper comparisons are equal.

**formalStatement:** (∀z:x≤z iff y≤z) ⇒ x=y

**proofSketch:** Set z=y and z=x; reflexivity yields both inequalities, then use antisymmetry.

**assumptions:** The explicit basis, carriers, and side conditions stated for PartialOrder apply.

**dependsOn:** [reflexive](PartialOrder.md#node-urn-csabs-axiom-PartialOrder-reflexive); [transitive](PartialOrder.md#node-urn-csabs-axiom-PartialOrder-transitive); [antisymmetric](PartialOrder.md#node-urn-csabs-axiom-PartialOrder-antisymmetric)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {A : Type u} [Catalog.PartialOrder A] (x y : A), (∀ z, x ≤ z ↔ y ≤ z) → x = y
```

**Source:** [`Catalog.Proofs.order_extensionality`](../lean/Catalog/Witnesses.lean); consulted 2026-11-12.

**Scope:** registered-witness-type

**Interpretation:** Mathlib PartialOrder; antisymmetry uses Lean equality.

**Limits:** Witness proves the explicit expectedType under its binders. Correspondence to the informal statement is reviewed metadata, not mechanically proved. Original citation gaps remain disclosed in the catalog.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/PartialOrder-antisymmetric": "Explicit interface premise: x≤y ∧ y≤x ⇒ x=y; interpreted by Catalog.PartialOrder. See the carrier/operation mapping; closure is enforced by typed operations and axioms are hypotheses carried by these structures, not new Lean axiom declarations.",
  "urn:csabs:axiom/PartialOrder-reflexive": "Explicit interface premise: ∀x∈A:x≤x; interpreted by Catalog.PartialOrder. See the carrier/operation mapping; closure is enforced by typed operations and axioms are hypotheses carried by these structures, not new Lean axiom declarations.",
  "urn:csabs:axiom/PartialOrder-transitive": "Explicit interface premise: x≤y ∧ y≤z ⇒ x≤z; interpreted by Catalog.PartialOrder. See the carrier/operation mapping; closure is enforced by typed operations and axioms are hypotheses carried by these structures, not new Lean axiom declarations."
}
```

## Concept provenance

- [Mathlib partial-order definitions](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Order/Defs/PartialOrder.html); sourceRole: reference-for-selected-basis

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/PartialOrder",
    "type": "Concept",
    "shortForm": "PartialOrder",
    "fullName": "Partial Order",
    "category": [
      "urn:csabs:category/order"
    ],
    "kind": "urn:csabs:kind/relation",
    "definition": "A reflexive, antisymmetric, transitive relation.",
    "notation": "(A,≤); x≤y ∧ y≤x ⇒ x=y",
    "hasOperation": [
      "urn:csabs:operation/PartialOrder-basis-le"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/PartialOrder-reflexive",
      "urn:csabs:axiom/PartialOrder-transitive",
      "urn:csabs:axiom/PartialOrder-antisymmetric"
    ],
    "hasLaw": [
      "urn:csabs:law/PartialOrder-core"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/PartialOrder-order-extensionality"
    ],
    "requiresConcept": [
      "urn:csabs:concept/Preorder"
    ],
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Instantiate carrier, equality, and stated semantic conventions before using this entry.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: A reflexive, antisymmetric, transitive relation. Governing rules: The order is reflexive. The order is transitive. Mutual ordering implies equality.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "source": [
      "urn:csabs:source/mathlib-order"
    ],
    "specializationOf": [
      "urn:csabs:concept/Preorder"
    ],
    "specializationNote": "Keep the same carrier and relation; antisymmetry is the additional constraint.",
    "leanFormulation": "abbrev PartialOrder (A : Type u) := _root_.PartialOrder A",
    "formulationSource": "urn:csabs:source/local-lean-Order",
    "formulationLocator": "Catalog.PartialOrder",
    "formulationScope": "model",
    "leanModelMapping": "Mathlib PartialOrder; antisymmetry uses Lean equality.",
    "leanModelLimitations": "Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.",
    "mathematicalFormulation": "A partial order is a preorder (A,≤) satisfying ∀a,b,a≤b∧b≤a⇒a=b. The empty carrier is permitted."
  },
  {
    "id": "urn:csabs:operation/PartialOrder-basis-le",
    "type": "Operation",
    "name": "le",
    "signature": "le : A×A→Prop",
    "description": "Returns the proposition that the first element precedes the second.",
    "concept": "urn:csabs:concept/PartialOrder"
  },
  {
    "id": "urn:csabs:law/PartialOrder-core",
    "type": "Law",
    "statement": "A finite nonempty partially ordered set has a minimal element.",
    "formalStatement": "A finite ∧ A≠∅ ⇒ ∃m∈A ∀x∈A: x≤m⇒x=m",
    "appliesTo": [
      "urn:csabs:concept/PartialOrder"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "assumptions": [
      "Use the carrier and semantic convention in the linked concept definition."
    ],
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/PartialOrder-reflexive",
      "urn:csabs:axiom/PartialOrder-transitive",
      "urn:csabs:axiom/PartialOrder-antisymmetric"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/PartialOrder-order-extensionality",
    "type": "Theorem",
    "name": "order-extensionality",
    "statement": "Elements with the same upper comparisons are equal.",
    "formalStatement": "(∀z:x≤z iff y≤z) ⇒ x=y",
    "proofSketch": "Set z=y and z=x; reflexivity yields both inequalities, then use antisymmetry.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for PartialOrder apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/PartialOrder"
    ],
    "dependsOn": [
      "urn:csabs:axiom/PartialOrder-reflexive",
      "urn:csabs:axiom/PartialOrder-transitive",
      "urn:csabs:axiom/PartialOrder-antisymmetric"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing",
    "leanFormulation": "∀ {A : Type u} [Catalog.PartialOrder A] (x y : A), (∀ z, x ≤ z ↔ y ≤ z) → x = y",
    "formulationSource": "urn:csabs:source/local-lean-Witnesses",
    "formulationLocator": "Catalog.Proofs.order_extensionality",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Mathlib PartialOrder; antisymmetry uses Lean equality.",
    "leanModelLimitations": "Witness proves the explicit expectedType under its binders. Correspondence to the informal statement is reviewed metadata, not mechanically proved. Original citation gaps remain disclosed in the catalog.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/PartialOrder-antisymmetric\": \"Explicit interface premise: x≤y ∧ y≤x ⇒ x=y; interpreted by Catalog.PartialOrder. See the carrier/operation mapping; closure is enforced by typed operations and axioms are hypotheses carried by these structures, not new Lean axiom declarations.\", \"urn:csabs:axiom/PartialOrder-reflexive\": \"Explicit interface premise: ∀x∈A:x≤x; interpreted by Catalog.PartialOrder. See the carrier/operation mapping; closure is enforced by typed operations and axioms are hypotheses carried by these structures, not new Lean axiom declarations.\", \"urn:csabs:axiom/PartialOrder-transitive\": \"Explicit interface premise: x≤y ∧ y≤z ⇒ x≤z; interpreted by Catalog.PartialOrder. See the carrier/operation mapping; closure is enforced by typed operations and axioms are hypotheses carried by these structures, not new Lean axiom declarations.\"}"
  }
]
```
<!-- graph-record:end -->
