# Join semilattice

A partially ordered carrier with a least upper bound for each pair.

**Notation:** (S,≤,⊔)

**Stable ID:** `urn:csabs:concept/JoinSemilattice`

**Categories:** Order and fixed points

**Kind:** Mathematical structure

**Prerequisites:** [Partial Order](PartialOrder.md)

**Specializes:** [Partial Order](PartialOrder.md)

## Backlinks

- [Lattice](Lattice.md) — `specializationOf`
- [State-based CRDT replication algebra](StateBasedCRDT.md) — `requiresConcept`

## Interface and scope

**axiomBasis:** ≤ is reflexive, antisymmetric and transitive; x≤x⊔y ∧ y≤x⊔y; x≤z ∧ y≤z ⇒ x⊔y≤z

**basisKind:** extensional-structural-definition

**basisScope:** Binary joins only. A bottom element, meets, completeness or distributivity is additional structure. Equality is the carrier equality used by antisymmetry; empty carrier allowed.

**specializationNote:** Keep the same carrier and ≤; forget ⊔ to obtain PartialOrder. Binary joins add explicit upper-bound and leastness requirements.

**verificationObligation:** Map carrier, equality, operation definedness and stated profile to the target API or proof context.; Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.; Model coverage does not establish every recorded claim or an implementation refinement.

**reviewStatus:** Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-JoinSemilattice-order"></a>

### order

`urn:csabs:operation/JoinSemilattice-order`

**signature:** le : S×S→Prop

**description:** The given partial order.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Binary joins only. A bottom element, meets, completeness or distributivity is additional structure. Equality is the carrier equality used by antisymmetry; empty carrier allowed.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** The given partial order.

**source:** [Mathlib pinned definitions: Order/Defs/Lattice.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Order/Defs/Lattice.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** SemilatticeSup: PartialOrder, le_sup_left, le_sup_right, sup_le

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-JoinSemilattice-join"></a>

### join

`urn:csabs:operation/JoinSemilattice-join`

**signature:** join : S×S→S

**description:** Returns the least upper bound of its two operands.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Binary joins only. A bottom element, meets, completeness or distributivity is additional structure. Equality is the carrier equality used by antisymmetry; empty carrier allowed.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Returns the least upper bound of its two operands.

**source:** [Mathlib pinned definitions: Order/Defs/Lattice.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Order/Defs/Lattice.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** SemilatticeSup: PartialOrder, le_sup_left, le_sup_right, sup_le

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

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

<a id="node-urn-csabs-axiom-JoinSemilattice-upper-bounds"></a>

### upper-bounds

`urn:csabs:axiom/JoinSemilattice-upper-bounds`

**statement:** Defining requirement: x≤x⊔y ∧ y≤x⊔y

**formalStatement:** x≤x⊔y ∧ y≤x⊔y

**assumptions:** Binary joins only. A bottom element, meets, completeness or distributivity is additional structure. Equality is the carrier equality used by antisymmetry; empty carrier allowed.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Mathlib pinned definitions: Order/Defs/Lattice.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Order/Defs/Lattice.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** SemilatticeSup: PartialOrder, le_sup_left, le_sup_right, sup_le

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-JoinSemilattice-leastness"></a>

### leastness

`urn:csabs:axiom/JoinSemilattice-leastness`

**statement:** Defining requirement: x≤z ∧ y≤z ⇒ x⊔y≤z

**formalStatement:** x≤z ∧ y≤z ⇒ x⊔y≤z

**assumptions:** Binary joins only. A bottom element, meets, completeness or distributivity is additional structure. Equality is the carrier equality used by antisymmetry; empty carrier allowed.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Mathlib pinned definitions: Order/Defs/Lattice.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Order/Defs/Lattice.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** SemilatticeSup: PartialOrder, le_sup_left, le_sup_right, sup_le

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-JoinSemilattice-commutativity"></a>

### commutativity

`urn:csabs:law/JoinSemilattice-commutativity`

**statement:** x⊔y=y⊔x

**formalStatement:** x⊔y=y⊔x

**assumptions:** Binary joins only. A bottom element, meets, completeness or distributivity is additional structure. Equality is the carrier equality used by antisymmetry; empty carrier allowed.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [reflexive](PartialOrder.md#node-urn-csabs-axiom-PartialOrder-reflexive); [transitive](PartialOrder.md#node-urn-csabs-axiom-PartialOrder-transitive); [antisymmetric](PartialOrder.md#node-urn-csabs-axiom-PartialOrder-antisymmetric); [upper-bounds](JoinSemilattice.md#node-urn-csabs-axiom-JoinSemilattice-upper-bounds); [leastness](JoinSemilattice.md#node-urn-csabs-axiom-JoinSemilattice-leastness)

**proofSketch:** Each join is an upper bound for both operands; use leastness in both directions and antisymmetry.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Mathlib pinned definitions: Order/Defs/Lattice.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Order/Defs/Lattice.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** SemilatticeSup: PartialOrder, le_sup_left, le_sup_right, sup_le

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Theorems

<a id="node-urn-csabs-theorem-JoinSemilattice-idempotence"></a>

### idempotence

`urn:csabs:theorem/JoinSemilattice-idempotence`

**statement:** x⊔x=x

**formalStatement:** x⊔x=x

**assumptions:** Binary joins only. A bottom element, meets, completeness or distributivity is additional structure. Equality is the carrier equality used by antisymmetry; empty carrier allowed.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [reflexive](PartialOrder.md#node-urn-csabs-axiom-PartialOrder-reflexive); [transitive](PartialOrder.md#node-urn-csabs-axiom-PartialOrder-transitive); [antisymmetric](PartialOrder.md#node-urn-csabs-axiom-PartialOrder-antisymmetric); [upper-bounds](JoinSemilattice.md#node-urn-csabs-axiom-JoinSemilattice-upper-bounds); [leastness](JoinSemilattice.md#node-urn-csabs-axiom-JoinSemilattice-leastness)

**proofSketch:** The join is above x; x is an upper bound of both copies. Use leastness and antisymmetry.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Mathlib pinned definitions: Order/Defs/Lattice.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Order/Defs/Lattice.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** SemilatticeSup: PartialOrder, le_sup_left, le_sup_right, sup_le

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Concept provenance

- [Mathlib pinned definitions: Order/Defs/Lattice.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Order/Defs/Lattice.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** SemilatticeSup: PartialOrder, le_sup_left, le_sup_right, sup_le

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/JoinSemilattice",
    "type": "Concept",
    "shortForm": "JoinSemilattice",
    "fullName": "Join semilattice",
    "category": [
      "urn:csabs:category/order"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "A partially ordered carrier with a least upper bound for each pair.",
    "notation": "(S,≤,⊔)",
    "requiresConcept": [
      "urn:csabs:concept/PartialOrder"
    ],
    "relatedConcept": [],
    "hasOperation": [
      "urn:csabs:operation/JoinSemilattice-order",
      "urn:csabs:operation/JoinSemilattice-join"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/PartialOrder-reflexive",
      "urn:csabs:axiom/PartialOrder-transitive",
      "urn:csabs:axiom/PartialOrder-antisymmetric",
      "urn:csabs:axiom/JoinSemilattice-upper-bounds",
      "urn:csabs:axiom/JoinSemilattice-leastness"
    ],
    "hasLaw": [
      "urn:csabs:law/JoinSemilattice-commutativity"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/JoinSemilattice-idempotence"
    ],
    "axiomBasis": "≤ is reflexive, antisymmetric and transitive; x≤x⊔y ∧ y≤x⊔y; x≤z ∧ y≤z ⇒ x⊔y≤z",
    "basisKind": "extensional-structural-definition",
    "basisScope": "Binary joins only. A bottom element, meets, completeness or distributivity is additional structure. Equality is the carrier equality used by antisymmetry; empty carrier allowed.",
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Map carrier, equality, operation definedness and stated profile to the target API or proof context.",
      "Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.",
      "Model coverage does not establish every recorded claim or an implementation refinement."
    ],
    "reviewStatus": "Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.",
    "source": [
      "urn:csabs:source/mathlib-join-core"
    ],
    "sourceLocator": "SemilatticeSup: PartialOrder, le_sup_left, le_sup_right, sup_le",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/PartialOrder"
    ],
    "specializationNote": "Keep the same carrier and ≤; forget ⊔ to obtain PartialOrder. Binary joins add explicit upper-bound and leastness requirements."
  },
  {
    "id": "urn:csabs:operation/JoinSemilattice-order",
    "type": "Operation",
    "name": "order",
    "signature": "le : S×S→Prop",
    "description": "The given partial order.",
    "concept": "urn:csabs:concept/JoinSemilattice",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Binary joins only. A bottom element, meets, completeness or distributivity is additional structure. Equality is the carrier equality used by antisymmetry; empty carrier allowed.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "The given partial order.",
    "source": [
      "urn:csabs:source/mathlib-join-core"
    ],
    "sourceLocator": "SemilatticeSup: PartialOrder, le_sup_left, le_sup_right, sup_le",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/JoinSemilattice-join",
    "type": "Operation",
    "name": "join",
    "signature": "join : S×S→S",
    "description": "Returns the least upper bound of its two operands.",
    "concept": "urn:csabs:concept/JoinSemilattice",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Binary joins only. A bottom element, meets, completeness or distributivity is additional structure. Equality is the carrier equality used by antisymmetry; empty carrier allowed.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Returns the least upper bound of its two operands.",
    "source": [
      "urn:csabs:source/mathlib-join-core"
    ],
    "sourceLocator": "SemilatticeSup: PartialOrder, le_sup_left, le_sup_right, sup_le",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/PartialOrder-reflexive",
    "type": "Axiom",
    "name": "reflexive",
    "statement": "The order is reflexive.",
    "formalStatement": "∀x∈A:x≤x",
    "appliesTo": [
      "urn:csabs:concept/PartialOrder",
      "urn:csabs:concept/JoinSemilattice"
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
    "id": "urn:csabs:axiom/PartialOrder-transitive",
    "type": "Axiom",
    "name": "transitive",
    "statement": "The order is transitive.",
    "formalStatement": "x≤y ∧ y≤z ⇒ x≤z",
    "appliesTo": [
      "urn:csabs:concept/PartialOrder",
      "urn:csabs:concept/JoinSemilattice"
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
    "id": "urn:csabs:axiom/PartialOrder-antisymmetric",
    "type": "Axiom",
    "name": "antisymmetric",
    "statement": "Mutual ordering implies equality.",
    "formalStatement": "x≤y ∧ y≤x ⇒ x=y",
    "appliesTo": [
      "urn:csabs:concept/PartialOrder",
      "urn:csabs:concept/JoinSemilattice"
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
    "id": "urn:csabs:axiom/JoinSemilattice-upper-bounds",
    "type": "Axiom",
    "name": "upper-bounds",
    "statement": "Defining requirement: x≤x⊔y ∧ y≤x⊔y",
    "formalStatement": "x≤x⊔y ∧ y≤x⊔y",
    "assumptions": [
      "Binary joins only. A bottom element, meets, completeness or distributivity is additional structure. Equality is the carrier equality used by antisymmetry; empty carrier allowed.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/JoinSemilattice"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/mathlib-join-core"
    ],
    "sourceLocator": "SemilatticeSup: PartialOrder, le_sup_left, le_sup_right, sup_le",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/JoinSemilattice-leastness",
    "type": "Axiom",
    "name": "leastness",
    "statement": "Defining requirement: x≤z ∧ y≤z ⇒ x⊔y≤z",
    "formalStatement": "x≤z ∧ y≤z ⇒ x⊔y≤z",
    "assumptions": [
      "Binary joins only. A bottom element, meets, completeness or distributivity is additional structure. Equality is the carrier equality used by antisymmetry; empty carrier allowed.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/JoinSemilattice"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/mathlib-join-core"
    ],
    "sourceLocator": "SemilatticeSup: PartialOrder, le_sup_left, le_sup_right, sup_le",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/JoinSemilattice-commutativity",
    "type": "Law",
    "name": "commutativity",
    "statement": "x⊔y=y⊔x",
    "formalStatement": "x⊔y=y⊔x",
    "assumptions": [
      "Binary joins only. A bottom element, meets, completeness or distributivity is additional structure. Equality is the carrier equality used by antisymmetry; empty carrier allowed.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/JoinSemilattice"
    ],
    "dependsOn": [
      "urn:csabs:axiom/PartialOrder-reflexive",
      "urn:csabs:axiom/PartialOrder-transitive",
      "urn:csabs:axiom/PartialOrder-antisymmetric",
      "urn:csabs:axiom/JoinSemilattice-upper-bounds",
      "urn:csabs:axiom/JoinSemilattice-leastness"
    ],
    "proofSketch": "Each join is an upper bound for both operands; use leastness in both directions and antisymmetry.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/mathlib-join-core"
    ],
    "sourceLocator": "SemilatticeSup: PartialOrder, le_sup_left, le_sup_right, sup_le",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/JoinSemilattice-idempotence",
    "type": "Theorem",
    "name": "idempotence",
    "statement": "x⊔x=x",
    "formalStatement": "x⊔x=x",
    "assumptions": [
      "Binary joins only. A bottom element, meets, completeness or distributivity is additional structure. Equality is the carrier equality used by antisymmetry; empty carrier allowed.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/JoinSemilattice"
    ],
    "dependsOn": [
      "urn:csabs:axiom/PartialOrder-reflexive",
      "urn:csabs:axiom/PartialOrder-transitive",
      "urn:csabs:axiom/PartialOrder-antisymmetric",
      "urn:csabs:axiom/JoinSemilattice-upper-bounds",
      "urn:csabs:axiom/JoinSemilattice-leastness"
    ],
    "proofSketch": "The join is above x; x is an upper bound of both copies. Use leastness and antisymmetry.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/mathlib-join-core"
    ],
    "sourceLocator": "SemilatticeSup: PartialOrder, le_sup_left, le_sup_right, sup_le",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
