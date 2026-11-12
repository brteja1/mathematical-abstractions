# Nonempty bounded closed interval

An ordered endpoint pair representing the closed interval between its endpoints in a linearly ordered carrier.

**Notation:** [l,u], l≤u

**Stable ID:** `urn:csabs:concept/ClosedInterval`

**Categories:** Data structures → Intervals

**Kind:** Abstract data type

**Prerequisites:** [Total Order](TotalOrder.md), [Option Type](OptionType.md)

## Mathematical formulation

For a linear order A, interval values are pairs (l,u) with l≤u; x∈[l,u] ⇔ l≤x≤u. Intersection returns [max(l,l′),min(u,u′)] if these endpoints are ordered, and none otherwise.

**Lean formulation** (in its source module context):

```lean
structure ClosedInterval (A : Type u) [LinearOrder A] where
  lower : A
  upper : A
  ordered : lower ≤ upper
```

**Source:** [`Catalog.ClosedInterval`](../lean/Catalog/CoreData.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** [l,u], l≤u. A has a linear order. Singleton intervals allowed. No empty, open, unbounded or NaN endpoints in the carrier. Intersection returns Option to represent disjointness. Equality is endpoint equality.

**Limits:** Compiled carrier and selected interface interpretation. Some catalog operations are specified mathematically rather than wrapped as Lean declarations; no blanket proof of claims, algorithms, parsing, liveness or complexity. See individual witnesses.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

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

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {A : Type} [LinearOrder A] (i : Catalog.ClosedInterval A), i.contains i.lower ∧ i.contains i.upper
```

**Source:** [`Catalog.CoreDataProofs.interval_endpoints`](../lean/Catalog/CoreData.lean); consulted 2026-11-12.

**Scope:** registered-witness-type

**Interpretation:** ClosedInterval stores ordered endpoints; contains is lower≤x∧x≤upper. LinearOrder supplies reflexivity and the stored ordered proof supplies lower≤upper; no empty interval is an inhabitant.

**Limits:** Only the displayed proposition for this explicit interpretation. No proof of all catalog claims or of a software implementation; informal/formal correspondence remains reviewed metadata.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/ClosedInterval-membership": "Interpreted premise: x∈[l,u] ⇔ l≤x ∧ x≤u. ClosedInterval stores ordered endpoints; contains is lower≤x∧x≤upper. LinearOrder supplies reflexivity and the stored ordered proof supplies lower≤upper; no empty interval is an inhabitant.",
  "urn:csabs:axiom/ClosedInterval-ordered-endpoints": "Interpreted premise: l≤u. ClosedInterval stores ordered endpoints; contains is lower≤x∧x≤upper. LinearOrder supplies reflexivity and the stored ordered proof supplies lower≤upper; no empty interval is an inhabitant."
}
```

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
      "urn:csabs:category/interval-structures"
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
    "provenanceKind": "adapted",
    "leanFormulation": "structure ClosedInterval (A : Type u) [LinearOrder A] where\n  lower : A\n  upper : A\n  ordered : lower ≤ upper",
    "formulationSource": "urn:csabs:source/local-lean-CoreData",
    "formulationLocator": "Catalog.ClosedInterval",
    "formulationScope": "model",
    "leanModelMapping": "[l,u], l≤u. A has a linear order. Singleton intervals allowed. No empty, open, unbounded or NaN endpoints in the carrier. Intersection returns Option to represent disjointness. Equality is endpoint equality.",
    "leanModelLimitations": "Compiled carrier and selected interface interpretation. Some catalog operations are specified mathematically rather than wrapped as Lean declarations; no blanket proof of claims, algorithms, parsing, liveness or complexity. See individual witnesses.",
    "mathematicalFormulation": "For a linear order A, interval values are pairs (l,u) with l≤u; x∈[l,u] ⇔ l≤x≤u. Intersection returns [max(l,l′),min(u,u′)] if these endpoints are ordered, and none otherwise."
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
    "provenanceKind": "derived",
    "leanFormulation": "∀ {A : Type} [LinearOrder A] (i : Catalog.ClosedInterval A), i.contains i.lower ∧ i.contains i.upper",
    "formulationSource": "urn:csabs:source/local-lean-CoreData",
    "formulationLocator": "Catalog.CoreDataProofs.interval_endpoints",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "ClosedInterval stores ordered endpoints; contains is lower≤x∧x≤upper. LinearOrder supplies reflexivity and the stored ordered proof supplies lower≤upper; no empty interval is an inhabitant.",
    "leanModelLimitations": "Only the displayed proposition for this explicit interpretation. No proof of all catalog claims or of a software implementation; informal/formal correspondence remains reviewed metadata.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/ClosedInterval-membership\": \"Interpreted premise: x∈[l,u] ⇔ l≤x ∧ x≤u. ClosedInterval stores ordered endpoints; contains is lower≤x∧x≤upper. LinearOrder supplies reflexivity and the stored ordered proof supplies lower≤upper; no empty interval is an inhabitant.\", \"urn:csabs:axiom/ClosedInterval-ordered-endpoints\": \"Interpreted premise: l≤u. ClosedInterval stores ordered endpoints; contains is lower≤x∧x≤upper. LinearOrder supplies reflexivity and the stored ordered proof supplies lower≤upper; no empty interval is an inhabitant.\"}"
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
