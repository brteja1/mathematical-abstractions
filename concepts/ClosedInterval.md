# Nonempty bounded closed interval

An ordered endpoint pair representing the closed interval between its endpoints in a linearly ordered carrier.

**Notation:** [l,u], l≤u

**Stable ID:** `urn:csabs:concept/ClosedInterval`

**Categories:** Data structures

**Kind:** Abstract data type

**Prerequisites:** [Total Order](TotalOrder.md), [Option Type](OptionType.md)

## Interface and scope

**axiomBasis:** l≤u; x∈[l,u] ⇔ l≤x ∧ x≤u; intersect([l,u],[a,b])=Some([max(l,a),min(u,b)]) if max(l,a)≤min(u,b), otherwise None

**basisKind:** extensional-structural-definition

**basisScope:** A has a linear order. Singleton intervals allowed. No empty, open, unbounded or NaN endpoints in the carrier. Intersection returns Option to represent disjointness. Equality is endpoint equality.

**verificationObligation:** Map carrier, equality, operation definedness and stated profile to the target API or proof context.; Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.; Model coverage does not establish every recorded claim or an implementation refinement.

**reviewStatus:** Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-ClosedInterval-construct"></a>

### construct

`urn:csabs:operation/ClosedInterval-construct`

**signature:** interval : {(l,u)∈A² | l≤u}→Interval(A)

**description:** Constructs ordered endpoints.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. A has a linear order. Singleton intervals allowed. No empty, open, unbounded or NaN endpoints in the carrier. Intersection returns Option to represent disjointness. Equality is endpoint equality.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Constructs ordered endpoints.

**source:** [Mathlib pinned definitions: Order/Interval/Set/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Order/Interval/Set/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Set.Icc and membership definition

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-ClosedInterval-contains"></a>

### contains

`urn:csabs:operation/ClosedInterval-contains`

**signature:** contains : Interval(A)×A→Prop

**description:** x∈[l,u] iff l≤x≤u.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. A has a linear order. Singleton intervals allowed. No empty, open, unbounded or NaN endpoints in the carrier. Intersection returns Option to represent disjointness. Equality is endpoint equality.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** x∈[l,u] iff l≤x≤u.

**source:** [Mathlib pinned definitions: Order/Interval/Set/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Order/Interval/Set/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Set.Icc and membership definition

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-ClosedInterval-intersect"></a>

### intersect

`urn:csabs:operation/ClosedInterval-intersect`

**signature:** intersect : Interval(A)²→Option(Interval(A))

**description:** Some([max(l₁,l₂),min(u₁,u₂)]) if ordered, else None.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. A has a linear order. Singleton intervals allowed. No empty, open, unbounded or NaN endpoints in the carrier. Intersection returns Option to represent disjointness. Equality is endpoint equality.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Some([max(l₁,l₂),min(u₁,u₂)]) if ordered, else None.

**source:** [Mathlib pinned definitions: Order/Interval/Set/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Order/Interval/Set/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Set.Icc and membership definition

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-ClosedInterval-ordered-endpoints"></a>

### ordered-endpoints

`urn:csabs:axiom/ClosedInterval-ordered-endpoints`

**statement:** Defining requirement: l≤u

**formalStatement:** l≤u

**assumptions:** A has a linear order. Singleton intervals allowed. No empty, open, unbounded or NaN endpoints in the carrier. Intersection returns Option to represent disjointness. Equality is endpoint equality.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Mathlib pinned definitions: Order/Interval/Set/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Order/Interval/Set/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Set.Icc and membership definition

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-ClosedInterval-membership"></a>

### membership

`urn:csabs:axiom/ClosedInterval-membership`

**statement:** Defining requirement: x∈[l,u] ⇔ l≤x ∧ x≤u

**formalStatement:** x∈[l,u] ⇔ l≤x ∧ x≤u

**assumptions:** A has a linear order. Singleton intervals allowed. No empty, open, unbounded or NaN endpoints in the carrier. Intersection returns Option to represent disjointness. Equality is endpoint equality.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Mathlib pinned definitions: Order/Interval/Set/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Order/Interval/Set/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Set.Icc and membership definition

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-ClosedInterval-intersection"></a>

### intersection

`urn:csabs:axiom/ClosedInterval-intersection`

**statement:** Defining requirement: intersect([l,u],[a,b])=Some([max(l,a),min(u,b)]) if max(l,a)≤min(u,b), otherwise None

**formalStatement:** intersect([l,u],[a,b])=Some([max(l,a),min(u,b)]) if max(l,a)≤min(u,b), otherwise None

**assumptions:** A has a linear order. Singleton intervals allowed. No empty, open, unbounded or NaN endpoints in the carrier. Intersection returns Option to represent disjointness. Equality is endpoint equality.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Mathlib pinned definitions: Order/Interval/Set/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Order/Interval/Set/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Set.Icc and membership definition

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-ClosedInterval-endpoints-contained"></a>

### endpoints-contained

`urn:csabs:law/ClosedInterval-endpoints-contained`

**statement:** l∈[l,u] ∧ u∈[l,u]

**formalStatement:** l∈[l,u] ∧ u∈[l,u]

**assumptions:** A has a linear order. Singleton intervals allowed. No empty, open, unbounded or NaN endpoints in the carrier. Intersection returns Option to represent disjointness. Equality is endpoint equality.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [ordered-endpoints](ClosedInterval.md#node-urn-csabs-axiom-ClosedInterval-ordered-endpoints); [membership](ClosedInterval.md#node-urn-csabs-axiom-ClosedInterval-membership)

**proofSketch:** Use reflexivity and the stored endpoint inequality in the membership equation.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Mathlib pinned definitions: Order/Interval/Set/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Order/Interval/Set/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Set.Icc and membership definition

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Theorems

<a id="node-urn-csabs-theorem-ClosedInterval-intersection-membership"></a>

### intersection-membership

`urn:csabs:theorem/ClosedInterval-intersection-membership`

**statement:** intersect(I,J)=Some(K) ⇒ ∀x, (x∈K ⇔ x∈I ∧ x∈J)

**formalStatement:** intersect(I,J)=Some(K) ⇒ ∀x, (x∈K ⇔ x∈I ∧ x∈J)

**assumptions:** A has a linear order. Singleton intervals allowed. No empty, open, unbounded or NaN endpoints in the carrier. Intersection returns Option to represent disjointness. Equality is endpoint equality.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [membership](ClosedInterval.md#node-urn-csabs-axiom-ClosedInterval-membership); [intersection](ClosedInterval.md#node-urn-csabs-axiom-ClosedInterval-intersection)

**proofSketch:** Expand max lower bound and min upper bound inequalities in a linear order.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Mathlib pinned definitions: Order/Interval/Set/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Order/Interval/Set/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Set.Icc and membership definition

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Concept provenance

- [Mathlib pinned definitions: Order/Interval/Set/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Order/Interval/Set/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Set.Icc and membership definition

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/ClosedInterval",
    "type": "Concept",
    "shortForm": "ClosedInterval",
    "fullName": "Nonempty bounded closed interval",
    "category": [
      "urn:csabs:category/data-structures"
    ],
    "kind": "urn:csabs:kind/abstract-data-type",
    "definition": "An ordered endpoint pair representing the closed interval between its endpoints in a linearly ordered carrier.",
    "notation": "[l,u], l≤u",
    "requiresConcept": [
      "urn:csabs:concept/TotalOrder",
      "urn:csabs:concept/OptionType"
    ],
    "relatedConcept": [],
    "hasOperation": [
      "urn:csabs:operation/ClosedInterval-construct",
      "urn:csabs:operation/ClosedInterval-contains",
      "urn:csabs:operation/ClosedInterval-intersect"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/ClosedInterval-ordered-endpoints",
      "urn:csabs:axiom/ClosedInterval-membership",
      "urn:csabs:axiom/ClosedInterval-intersection"
    ],
    "hasLaw": [
      "urn:csabs:law/ClosedInterval-endpoints-contained"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/ClosedInterval-intersection-membership"
    ],
    "axiomBasis": "l≤u; x∈[l,u] ⇔ l≤x ∧ x≤u; intersect([l,u],[a,b])=Some([max(l,a),min(u,b)]) if max(l,a)≤min(u,b), otherwise None",
    "basisKind": "extensional-structural-definition",
    "basisScope": "A has a linear order. Singleton intervals allowed. No empty, open, unbounded or NaN endpoints in the carrier. Intersection returns Option to represent disjointness. Equality is endpoint equality.",
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Map carrier, equality, operation definedness and stated profile to the target API or proof context.",
      "Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.",
      "Model coverage does not establish every recorded claim or an implementation refinement."
    ],
    "reviewStatus": "Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.",
    "source": [
      "urn:csabs:source/mathlib-interval-core"
    ],
    "sourceLocator": "Set.Icc and membership definition",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/ClosedInterval-construct",
    "type": "Operation",
    "name": "construct",
    "signature": "interval : {(l,u)∈A² | l≤u}→Interval(A)",
    "description": "Constructs ordered endpoints.",
    "concept": "urn:csabs:concept/ClosedInterval",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. A has a linear order. Singleton intervals allowed. No empty, open, unbounded or NaN endpoints in the carrier. Intersection returns Option to represent disjointness. Equality is endpoint equality.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Constructs ordered endpoints.",
    "source": [
      "urn:csabs:source/mathlib-interval-core"
    ],
    "sourceLocator": "Set.Icc and membership definition",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/ClosedInterval-contains",
    "type": "Operation",
    "name": "contains",
    "signature": "contains : Interval(A)×A→Prop",
    "description": "x∈[l,u] iff l≤x≤u.",
    "concept": "urn:csabs:concept/ClosedInterval",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. A has a linear order. Singleton intervals allowed. No empty, open, unbounded or NaN endpoints in the carrier. Intersection returns Option to represent disjointness. Equality is endpoint equality.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "x∈[l,u] iff l≤x≤u.",
    "source": [
      "urn:csabs:source/mathlib-interval-core"
    ],
    "sourceLocator": "Set.Icc and membership definition",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/ClosedInterval-intersect",
    "type": "Operation",
    "name": "intersect",
    "signature": "intersect : Interval(A)²→Option(Interval(A))",
    "description": "Some([max(l₁,l₂),min(u₁,u₂)]) if ordered, else None.",
    "concept": "urn:csabs:concept/ClosedInterval",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. A has a linear order. Singleton intervals allowed. No empty, open, unbounded or NaN endpoints in the carrier. Intersection returns Option to represent disjointness. Equality is endpoint equality.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Some([max(l₁,l₂),min(u₁,u₂)]) if ordered, else None.",
    "source": [
      "urn:csabs:source/mathlib-interval-core"
    ],
    "sourceLocator": "Set.Icc and membership definition",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/ClosedInterval-ordered-endpoints",
    "type": "Axiom",
    "name": "ordered-endpoints",
    "statement": "Defining requirement: l≤u",
    "formalStatement": "l≤u",
    "assumptions": [
      "A has a linear order. Singleton intervals allowed. No empty, open, unbounded or NaN endpoints in the carrier. Intersection returns Option to represent disjointness. Equality is endpoint equality.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/ClosedInterval"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/mathlib-interval-core"
    ],
    "sourceLocator": "Set.Icc and membership definition",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/ClosedInterval-membership",
    "type": "Axiom",
    "name": "membership",
    "statement": "Defining requirement: x∈[l,u] ⇔ l≤x ∧ x≤u",
    "formalStatement": "x∈[l,u] ⇔ l≤x ∧ x≤u",
    "assumptions": [
      "A has a linear order. Singleton intervals allowed. No empty, open, unbounded or NaN endpoints in the carrier. Intersection returns Option to represent disjointness. Equality is endpoint equality.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/ClosedInterval"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/mathlib-interval-core"
    ],
    "sourceLocator": "Set.Icc and membership definition",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/ClosedInterval-intersection",
    "type": "Axiom",
    "name": "intersection",
    "statement": "Defining requirement: intersect([l,u],[a,b])=Some([max(l,a),min(u,b)]) if max(l,a)≤min(u,b), otherwise None",
    "formalStatement": "intersect([l,u],[a,b])=Some([max(l,a),min(u,b)]) if max(l,a)≤min(u,b), otherwise None",
    "assumptions": [
      "A has a linear order. Singleton intervals allowed. No empty, open, unbounded or NaN endpoints in the carrier. Intersection returns Option to represent disjointness. Equality is endpoint equality.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/ClosedInterval"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/mathlib-interval-core"
    ],
    "sourceLocator": "Set.Icc and membership definition",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/ClosedInterval-endpoints-contained",
    "type": "Law",
    "name": "endpoints-contained",
    "statement": "l∈[l,u] ∧ u∈[l,u]",
    "formalStatement": "l∈[l,u] ∧ u∈[l,u]",
    "assumptions": [
      "A has a linear order. Singleton intervals allowed. No empty, open, unbounded or NaN endpoints in the carrier. Intersection returns Option to represent disjointness. Equality is endpoint equality.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/ClosedInterval"
    ],
    "dependsOn": [
      "urn:csabs:axiom/ClosedInterval-ordered-endpoints",
      "urn:csabs:axiom/ClosedInterval-membership"
    ],
    "proofSketch": "Use reflexivity and the stored endpoint inequality in the membership equation.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/mathlib-interval-core"
    ],
    "sourceLocator": "Set.Icc and membership definition",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/ClosedInterval-intersection-membership",
    "type": "Theorem",
    "name": "intersection-membership",
    "statement": "intersect(I,J)=Some(K) ⇒ ∀x, (x∈K ⇔ x∈I ∧ x∈J)",
    "formalStatement": "intersect(I,J)=Some(K) ⇒ ∀x, (x∈K ⇔ x∈I ∧ x∈J)",
    "assumptions": [
      "A has a linear order. Singleton intervals allowed. No empty, open, unbounded or NaN endpoints in the carrier. Intersection returns Option to represent disjointness. Equality is endpoint equality.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/ClosedInterval"
    ],
    "dependsOn": [
      "urn:csabs:axiom/ClosedInterval-membership",
      "urn:csabs:axiom/ClosedInterval-intersection"
    ],
    "proofSketch": "Expand max lower bound and min upper bound inequalities in a linear order.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/mathlib-interval-core"
    ],
    "sourceLocator": "Set.Icc and membership definition",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
