# Linear extension of a partial order

A total order on exactly the same carrier as a given partial order that preserves every original comparison. Every partial order has such an extension in the classical choice-based setting.

**Notation:** (A,r) ↦ s; r⊆s; s linear on A

**Stable ID:** `urn:csabs:concept/OrderLinearExtension`

**Categories:** Order and fixed points

**Kind:** Mathematical structure

**Prerequisites:** [Partial Order](PartialOrder.md), [Total Order](TotalOrder.md)

**Specializes:** [Total Order](TotalOrder.md)

**Related concepts:** [Monotone Function](MonotoneFunction.md)

## Mathematical formulation

Ext(A,r)={s:A→A→Prop | IsLinearOrder(A,s) ∧ ∀a,b,r(a,b)⇒s(a,b)}. Szpilrajn: IsPartialOrder(A,r) ⇒ Ext(A,r)≠∅.

**Lean formulation** (in its source module context):

```lean
structure OrderLinearExtension (A : Type) (r : A → A → Prop) where
  relation : A → A → Prop
  linear : IsLinearOrder A relation
  preserves : ∀ a b, r a b → relation a b
```

**Source:** [`Catalog.OrderLinearExtension`](../lean/Catalog/ReleaseSequenceModels.lean); consulted 2026-11-20.

**Scope:** model

**Interpretation:** Ext(A,r)={s:A→A→Prop | IsLinearOrder(A,s) ∧ ∀a,b,r(a,b)⇒s(a,b)}. Szpilrajn: IsPartialOrder(A,r) ⇒ Ext(A,r)≠∅.

**Limits:** A may be empty, finite or infinite; r is a reflexive, transitive, antisymmetric non-strict partial order on A with exact equality. s is non-strict and uses the same carrier and equality. Incomparable elements may become comparable. Identity is a monotone bijection, generally not an order embedding reflecting comparisons. No uniqueness, canonical choice, finite algorithm, ordering of arbitrary preorders without quotienting, or constructive existence is promised. Existence is classical, using the choice/Zorn assumptions exposed by the pinned Lean audit. Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Input r is a partial order; output s is reflexive, transitive, antisymmetric and total, with ∀a,b, r(a,b)⇒s(a,b). Existence is a derived Szpilrajn theorem, not a defining axiom.

**basisKind:** defined-structure

**basisScope:** A may be empty, finite or infinite; r is a reflexive, transitive, antisymmetric non-strict partial order on A with exact equality. s is non-strict and uses the same carrier and equality. Incomparable elements may become comparable. Identity is a monotone bijection, generally not an order embedding reflecting comparisons. No uniqueness, canonical choice, finite algorithm, ordering of arbitrary preorders without quotienting, or constructive existence is promised. Existence is classical, using the choice/Zorn assumptions exposed by the pinned Lean audit.

**specializationNote:** For fixed input (A,r), forget the extension evidence and retain output order s on the same A and exact equality. Preservation r⊆s is extra data, not order reflection.

**verificationObligation:** Map exact carriers, equality, totality and the explicit profile conventions before use.; Model and theorem evidence does not establish a concrete software implementation refinement.

**reviewStatus:** Sourced model with separately registered Lean satisfaction and derived witnesses; verification requires fresh audit evidence.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-OrderLinearExtension-relation"></a>

### extension comparison

`urn:csabs:operation/OrderLinearExtension-relation`

**signature:** le : Ext(A,r)×A×A→Prop

**description:** Evaluate the chosen extended relation s.

**precondition:** r partial; supplied extension s.

**postcondition:** All original comparisons persist and every pair becomes comparable.

**totality:** Total on the stated domain.

**source:** [Pinned Mathlib list and lexicographic order constructions and linear-order extension](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); citation: Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679: Data/Finset/Card.lean Finset.card; Data/List/TakeDrop.lean dropSlice_eq and length_dropSlice; Data/List/Lex.lean linearOrder; Order/Sum/Order.lean Sum.Lex; Order/Prod/Lex/Basic.lean Prod.Lex; Order/Extension/Linear.lean extend_partialOrder and toLinearExtension. Apache-2.0.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference

**sourceLocator:** Order/Extension/Linear.lean: extend_partialOrder; LinearExtension; toLinearExtension

**sourceNote:** Adapts the pinned Mathlib Szpilrajn theorem and same-carrier monotone identity construction; the library proves existence via Zorn, rather than assuming an extension.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-OrderLinearExtension-extend"></a>

### choose a linear extension

`urn:csabs:operation/OrderLinearExtension-extend`

**signature:** extend : Poset(A)⇝Ext(A,r)

**description:** Classically select an order extending the given partial order.

**precondition:** A set-sized carrier and non-strict partial order; classical choice/Zorn.

**postcondition:** An s with IsLinearOrder(A,s) and r⊆s.

**totality:** Mathematical nonconstructive existence/choice; no executable algorithm, canonical order or unique result.

**source:** [Pinned Mathlib list and lexicographic order constructions and linear-order extension](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); citation: Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679: Data/Finset/Card.lean Finset.card; Data/List/TakeDrop.lean dropSlice_eq and length_dropSlice; Data/List/Lex.lean linearOrder; Order/Sum/Order.lean Sum.Lex; Order/Prod/Lex/Basic.lean Prod.Lex; Order/Extension/Linear.lean extend_partialOrder and toLinearExtension. Apache-2.0.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference

**sourceLocator:** Order/Extension/Linear.lean: extend_partialOrder; LinearExtension; toLinearExtension

**sourceNote:** Adapts the pinned Mathlib Szpilrajn theorem and same-carrier monotone identity construction; the library proves existence via Zorn, rather than assuming an extension.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-OrderLinearExtension-defining-profile"></a>

### defining profile

`urn:csabs:axiom/OrderLinearExtension-defining-profile`

**statement:** Input r is a partial order; output s is reflexive, transitive, antisymmetric and total, with ∀a,b, r(a,b)⇒s(a,b). Existence is a derived Szpilrajn theorem, not a defining axiom.

**formalStatement:** IsPartialOrder(A,r); IsLinearOrder(A,s); ∀a,b,r(a,b)⇒s(a,b)

**assumptions:** A may be empty, finite or infinite; r is a reflexive, transitive, antisymmetric non-strict partial order on A with exact equality. s is non-strict and uses the same carrier and equality. Incomparable elements may become comparable. Identity is a monotone bijection, generally not an order embedding reflecting comparisons. No uniqueness, canonical choice, finite algorithm, ordering of arbitrary preorders without quotienting, or constructive existence is promised. Existence is classical, using the choice/Zorn assumptions exposed by the pinned Lean audit.

**ruleRole:** defining-rule

**reviewStatus:** Structure constraints; satisfaction is established separately for the selected model.

**source:** [Pinned Mathlib list and lexicographic order constructions and linear-order extension](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); citation: Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679: Data/Finset/Card.lean Finset.card; Data/List/TakeDrop.lean dropSlice_eq and length_dropSlice; Data/List/Lex.lean linearOrder; Order/Sum/Order.lean Sum.Lex; Order/Prod/Lex/Basic.lean Prod.Lex; Order/Extension/Linear.lean extend_partialOrder and toLinearExtension. Apache-2.0.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference

**sourceLocator:** Order/Extension/Linear.lean: extend_partialOrder; LinearExtension; toLinearExtension

**sourceNote:** Adapts the pinned Mathlib Szpilrajn theorem and same-carrier monotone identity construction; the library proves existence via Zorn, rather than assuming an extension.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-OrderLinearExtension-szpilrajn-existence"></a>

### szpilrajn-existence

`urn:csabs:law/OrderLinearExtension-szpilrajn-existence`

**statement:** Instantiate pinned Mathlib extend_partialOrder, whose Zorn argument produces a total extension on the same carrier. This uses classical choice and gives no canonical algorithm.

**formalStatement:** ∀ (A : Type) (r : A → A → Prop) [IsPartialOrder A r], Nonempty (Catalog.OrderLinearExtension A r)

**assumptions:** Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality.

**dependsOn:** [defining profile](OrderLinearExtension.md#node-urn-csabs-axiom-OrderLinearExtension-defining-profile)

**proofSketch:** Instantiate pinned Mathlib extend_partialOrder, whose Zorn argument produces a total extension on the same carrier. This uses classical choice and gives no canonical algorithm.

**reviewStatus:** Derived mathematical law; separately registered theorem supplies explicit proof evidence.

**source:** [Pinned Mathlib list and lexicographic order constructions and linear-order extension](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); citation: Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679: Data/Finset/Card.lean Finset.card; Data/List/TakeDrop.lean dropSlice_eq and length_dropSlice; Data/List/Lex.lean linearOrder; Order/Sum/Order.lean Sum.Lex; Order/Prod/Lex/Basic.lean Prod.Lex; Order/Extension/Linear.lean extend_partialOrder and toLinearExtension. Apache-2.0.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; Catalog release, sequence, transducer, schema, date and extension models and witnesses; path: lean/Catalog/ReleaseSequenceModels.lean; accessedOn: 2026-11-20; sourceRole: local-lean-formulation-and-proof

**sourceLocator:** Order/Extension/Linear.lean: extend_partialOrder; LinearExtension; toLinearExtension; Catalog.szpilrajn

**sourceNote:** Derived for the explicit selected model. Instantiate pinned Mathlib extend_partialOrder, whose Zorn argument produces a total extension on the same carrier. This uses classical choice and gives no canonical algorithm.

**provenanceKind:** derived

**ruleRole:** derived-law

## Theorems

<a id="node-urn-csabs-theorem-OrderLinearExtension-model-satisfaction"></a>

### model-satisfaction

`urn:csabs:theorem/OrderLinearExtension-model-satisfaction`

**statement:** Natural-number ≤ is linear and contains equality, giving an inhabited infinite example with distinct comparable elements.

**formalStatement:** Nonempty (Catalog.OrderLinearExtension Nat (fun a b => a = b))

**assumptions:** Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality.

**dependsOn:** [defining profile](OrderLinearExtension.md#node-urn-csabs-axiom-OrderLinearExtension-defining-profile)

**proofSketch:** Natural-number ≤ is linear and contains equality, giving an inhabited infinite example with distinct comparable elements.

**reviewStatus:** Separately registered Lean witness; require fresh compiler and axiom audit for verified status.

**source:** [Pinned Mathlib list and lexicographic order constructions and linear-order extension](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); citation: Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679: Data/Finset/Card.lean Finset.card; Data/List/TakeDrop.lean dropSlice_eq and length_dropSlice; Data/List/Lex.lean linearOrder; Order/Sum/Order.lean Sum.Lex; Order/Prod/Lex/Basic.lean Prod.Lex; Order/Extension/Linear.lean extend_partialOrder and toLinearExtension. Apache-2.0.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; Catalog release, sequence, transducer, schema, date and extension models and witnesses; path: lean/Catalog/ReleaseSequenceModels.lean; accessedOn: 2026-11-20; sourceRole: local-lean-formulation-and-proof

**sourceLocator:** Order/Extension/Linear.lean: extend_partialOrder; LinearExtension; toLinearExtension; Catalog.linear_extension_model_satisfaction

**sourceNote:** Derived for the explicit selected model. Natural-number ≤ is linear and contains equality, giving an inhabited infinite example with distinct comparable elements.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
Nonempty (Catalog.OrderLinearExtension Nat (fun a b => a = b))
```

**Source:** [`Catalog.linear_extension_model_satisfaction`](../lean/Catalog/ReleaseSequenceModels.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** Natural-number ≤ is linear and contains equality, giving an inhabited infinite example with distinct comparable elements.

**Limits:** Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/OrderLinearExtension-defining-profile": "Proved constraint for the specified concrete interpretation or structural recursion; not a hypothesis asserting its own satisfaction. Natural-number ≤ is linear and contains equality, giving an inhabited infinite example with distinct comparable elements."
}
```

<a id="node-urn-csabs-theorem-OrderLinearExtension-szpilrajn-existence"></a>

### szpilrajn-existence

`urn:csabs:theorem/OrderLinearExtension-szpilrajn-existence`

**statement:** Instantiate pinned Mathlib extend_partialOrder, whose Zorn argument produces a total extension on the same carrier. This uses classical choice and gives no canonical algorithm.

**formalStatement:** ∀ (A : Type) (r : A → A → Prop) [IsPartialOrder A r], Nonempty (Catalog.OrderLinearExtension A r)

**assumptions:** Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality.

**dependsOn:** [defining profile](OrderLinearExtension.md#node-urn-csabs-axiom-OrderLinearExtension-defining-profile)

**proofSketch:** Instantiate pinned Mathlib extend_partialOrder, whose Zorn argument produces a total extension on the same carrier. This uses classical choice and gives no canonical algorithm.

**reviewStatus:** Separately registered Lean witness; require fresh compiler and axiom audit for verified status.

**source:** [Pinned Mathlib list and lexicographic order constructions and linear-order extension](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); citation: Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679: Data/Finset/Card.lean Finset.card; Data/List/TakeDrop.lean dropSlice_eq and length_dropSlice; Data/List/Lex.lean linearOrder; Order/Sum/Order.lean Sum.Lex; Order/Prod/Lex/Basic.lean Prod.Lex; Order/Extension/Linear.lean extend_partialOrder and toLinearExtension. Apache-2.0.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; Catalog release, sequence, transducer, schema, date and extension models and witnesses; path: lean/Catalog/ReleaseSequenceModels.lean; accessedOn: 2026-11-20; sourceRole: local-lean-formulation-and-proof

**sourceLocator:** Order/Extension/Linear.lean: extend_partialOrder; LinearExtension; toLinearExtension; Catalog.szpilrajn

**sourceNote:** Derived for the explicit selected model. Instantiate pinned Mathlib extend_partialOrder, whose Zorn argument produces a total extension on the same carrier. This uses classical choice and gives no canonical algorithm.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ (A : Type) (r : A → A → Prop) [IsPartialOrder A r], Nonempty (Catalog.OrderLinearExtension A r)
```

**Source:** [`Catalog.szpilrajn`](../lean/Catalog/ReleaseSequenceModels.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** Instantiate pinned Mathlib extend_partialOrder, whose Zorn argument produces a total extension on the same carrier. This uses classical choice and gives no canonical algorithm.

**Limits:** Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/OrderLinearExtension-defining-profile": "Proved constraint for the specified concrete interpretation or structural recursion; not a hypothesis asserting its own satisfaction. Instantiate pinned Mathlib extend_partialOrder, whose Zorn argument produces a total extension on the same carrier. This uses classical choice and gives no canonical algorithm."
}
```

## Concept provenance

- [Pinned Mathlib list and lexicographic order constructions and linear-order extension](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); citation: Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679: Data/Finset/Card.lean Finset.card; Data/List/TakeDrop.lean dropSlice_eq and length_dropSlice; Data/List/Lex.lean linearOrder; Order/Sum/Order.lean Sum.Lex; Order/Prod/Lex/Basic.lean Prod.Lex; Order/Extension/Linear.lean extend_partialOrder and toLinearExtension. Apache-2.0.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference

**sourceLocator:** Order/Extension/Linear.lean: extend_partialOrder; LinearExtension; toLinearExtension

**sourceNote:** Adapts the pinned Mathlib Szpilrajn theorem and same-carrier monotone identity construction; the library proves existence via Zorn, rather than assuming an extension.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/OrderLinearExtension",
    "type": "Concept",
    "shortForm": "OrderLinearExtension",
    "fullName": "Linear extension of a partial order",
    "synonyms": [
      "Szpilrajn order extension",
      "Same-carrier total order extension"
    ],
    "category": [
      "urn:csabs:category/order"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "A total order on exactly the same carrier as a given partial order that preserves every original comparison. Every partial order has such an extension in the classical choice-based setting.",
    "notation": "(A,r) ↦ s; r⊆s; s linear on A",
    "requiresConcept": [
      "urn:csabs:concept/PartialOrder",
      "urn:csabs:concept/TotalOrder"
    ],
    "relatedConcept": [
      "urn:csabs:concept/MonotoneFunction"
    ],
    "axiomBasis": "Input r is a partial order; output s is reflexive, transitive, antisymmetric and total, with ∀a,b, r(a,b)⇒s(a,b). Existence is a derived Szpilrajn theorem, not a defining axiom.",
    "basisKind": "defined-structure",
    "basisScope": "A may be empty, finite or infinite; r is a reflexive, transitive, antisymmetric non-strict partial order on A with exact equality. s is non-strict and uses the same carrier and equality. Incomparable elements may become comparable. Identity is a monotone bijection, generally not an order embedding reflecting comparisons. No uniqueness, canonical choice, finite algorithm, ordering of arbitrary preorders without quotienting, or constructive existence is promised. Existence is classical, using the choice/Zorn assumptions exposed by the pinned Lean audit.",
    "mathematicalFormulation": "Ext(A,r)={s:A→A→Prop | IsLinearOrder(A,s) ∧ ∀a,b,r(a,b)⇒s(a,b)}. Szpilrajn: IsPartialOrder(A,r) ⇒ Ext(A,r)≠∅.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Sourced model with separately registered Lean satisfaction and derived witnesses; verification requires fresh audit evidence.",
    "verificationObligation": [
      "Map exact carriers, equality, totality and the explicit profile conventions before use.",
      "Model and theorem evidence does not establish a concrete software implementation refinement."
    ],
    "hasOperation": [
      "urn:csabs:operation/OrderLinearExtension-relation",
      "urn:csabs:operation/OrderLinearExtension-extend"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/OrderLinearExtension-defining-profile"
    ],
    "hasLaw": [
      "urn:csabs:law/OrderLinearExtension-szpilrajn-existence"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/OrderLinearExtension-model-satisfaction",
      "urn:csabs:theorem/OrderLinearExtension-szpilrajn-existence"
    ],
    "source": [
      "urn:csabs:source/seven-mathlib"
    ],
    "sourceLocator": "Order/Extension/Linear.lean: extend_partialOrder; LinearExtension; toLinearExtension",
    "sourceNote": "Adapts the pinned Mathlib Szpilrajn theorem and same-carrier monotone identity construction; the library proves existence via Zorn, rather than assuming an extension.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/TotalOrder"
    ],
    "specializationNote": "For fixed input (A,r), forget the extension evidence and retain output order s on the same A and exact equality. Preservation r⊆s is extra data, not order reflection.",
    "leanFormulation": "structure OrderLinearExtension (A : Type) (r : A → A → Prop) where\n  relation : A → A → Prop\n  linear : IsLinearOrder A relation\n  preserves : ∀ a b, r a b → relation a b",
    "formulationSource": "urn:csabs:source/seven-lean-models",
    "formulationLocator": "Catalog.OrderLinearExtension",
    "formulationScope": "model",
    "leanModelMapping": "Ext(A,r)={s:A→A→Prop | IsLinearOrder(A,s) ∧ ∀a,b,r(a,b)⇒s(a,b)}. Szpilrajn: IsPartialOrder(A,r) ⇒ Ext(A,r)≠∅.",
    "leanModelLimitations": "A may be empty, finite or infinite; r is a reflexive, transitive, antisymmetric non-strict partial order on A with exact equality. s is non-strict and uses the same carrier and equality. Incomparable elements may become comparable. Identity is a monotone bijection, generally not an order embedding reflecting comparisons. No uniqueness, canonical choice, finite algorithm, ordering of arbitrary preorders without quotienting, or constructive existence is promised. Existence is classical, using the choice/Zorn assumptions exposed by the pinned Lean audit. Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit."
  },
  {
    "id": "urn:csabs:operation/OrderLinearExtension-relation",
    "type": "Operation",
    "concept": "urn:csabs:concept/OrderLinearExtension",
    "name": "extension comparison",
    "signature": "le : Ext(A,r)×A×A→Prop",
    "description": "Evaluate the chosen extended relation s.",
    "precondition": "r partial; supplied extension s.",
    "postcondition": "All original comparisons persist and every pair becomes comparable.",
    "totality": "Total on the stated domain.",
    "source": [
      "urn:csabs:source/seven-mathlib"
    ],
    "sourceLocator": "Order/Extension/Linear.lean: extend_partialOrder; LinearExtension; toLinearExtension",
    "sourceNote": "Adapts the pinned Mathlib Szpilrajn theorem and same-carrier monotone identity construction; the library proves existence via Zorn, rather than assuming an extension.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/OrderLinearExtension-extend",
    "type": "Operation",
    "concept": "urn:csabs:concept/OrderLinearExtension",
    "name": "choose a linear extension",
    "signature": "extend : Poset(A)⇝Ext(A,r)",
    "description": "Classically select an order extending the given partial order.",
    "precondition": "A set-sized carrier and non-strict partial order; classical choice/Zorn.",
    "postcondition": "An s with IsLinearOrder(A,s) and r⊆s.",
    "totality": "Mathematical nonconstructive existence/choice; no executable algorithm, canonical order or unique result.",
    "source": [
      "urn:csabs:source/seven-mathlib"
    ],
    "sourceLocator": "Order/Extension/Linear.lean: extend_partialOrder; LinearExtension; toLinearExtension",
    "sourceNote": "Adapts the pinned Mathlib Szpilrajn theorem and same-carrier monotone identity construction; the library proves existence via Zorn, rather than assuming an extension.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/OrderLinearExtension-defining-profile",
    "type": "Axiom",
    "name": "defining profile",
    "statement": "Input r is a partial order; output s is reflexive, transitive, antisymmetric and total, with ∀a,b, r(a,b)⇒s(a,b). Existence is a derived Szpilrajn theorem, not a defining axiom.",
    "formalStatement": "IsPartialOrder(A,r); IsLinearOrder(A,s); ∀a,b,r(a,b)⇒s(a,b)",
    "assumptions": [
      "A may be empty, finite or infinite; r is a reflexive, transitive, antisymmetric non-strict partial order on A with exact equality. s is non-strict and uses the same carrier and equality. Incomparable elements may become comparable. Identity is a monotone bijection, generally not an order embedding reflecting comparisons. No uniqueness, canonical choice, finite algorithm, ordering of arbitrary preorders without quotienting, or constructive existence is promised. Existence is classical, using the choice/Zorn assumptions exposed by the pinned Lean audit."
    ],
    "appliesTo": [
      "urn:csabs:concept/OrderLinearExtension"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Structure constraints; satisfaction is established separately for the selected model.",
    "source": [
      "urn:csabs:source/seven-mathlib"
    ],
    "sourceLocator": "Order/Extension/Linear.lean: extend_partialOrder; LinearExtension; toLinearExtension",
    "sourceNote": "Adapts the pinned Mathlib Szpilrajn theorem and same-carrier monotone identity construction; the library proves existence via Zorn, rather than assuming an extension.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/OrderLinearExtension-szpilrajn-existence",
    "type": "Law",
    "name": "szpilrajn-existence",
    "statement": "Instantiate pinned Mathlib extend_partialOrder, whose Zorn argument produces a total extension on the same carrier. This uses classical choice and gives no canonical algorithm.",
    "formalStatement": "∀ (A : Type) (r : A → A → Prop) [IsPartialOrder A r], Nonempty (Catalog.OrderLinearExtension A r)",
    "assumptions": [
      "Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/OrderLinearExtension"
    ],
    "dependsOn": [
      "urn:csabs:axiom/OrderLinearExtension-defining-profile"
    ],
    "proofSketch": "Instantiate pinned Mathlib extend_partialOrder, whose Zorn argument produces a total extension on the same carrier. This uses classical choice and gives no canonical algorithm.",
    "reviewStatus": "Derived mathematical law; separately registered theorem supplies explicit proof evidence.",
    "source": [
      "urn:csabs:source/seven-mathlib",
      "urn:csabs:source/seven-lean-models"
    ],
    "sourceLocator": "Order/Extension/Linear.lean: extend_partialOrder; LinearExtension; toLinearExtension; Catalog.szpilrajn",
    "sourceNote": "Derived for the explicit selected model. Instantiate pinned Mathlib extend_partialOrder, whose Zorn argument produces a total extension on the same carrier. This uses classical choice and gives no canonical algorithm.",
    "provenanceKind": "derived",
    "ruleRole": "derived-law"
  },
  {
    "id": "urn:csabs:theorem/OrderLinearExtension-model-satisfaction",
    "type": "Theorem",
    "name": "model-satisfaction",
    "statement": "Natural-number ≤ is linear and contains equality, giving an inhabited infinite example with distinct comparable elements.",
    "formalStatement": "Nonempty (Catalog.OrderLinearExtension Nat (fun a b => a = b))",
    "assumptions": [
      "Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/OrderLinearExtension"
    ],
    "dependsOn": [
      "urn:csabs:axiom/OrderLinearExtension-defining-profile"
    ],
    "proofSketch": "Natural-number ≤ is linear and contains equality, giving an inhabited infinite example with distinct comparable elements.",
    "reviewStatus": "Separately registered Lean witness; require fresh compiler and axiom audit for verified status.",
    "source": [
      "urn:csabs:source/seven-mathlib",
      "urn:csabs:source/seven-lean-models"
    ],
    "sourceLocator": "Order/Extension/Linear.lean: extend_partialOrder; LinearExtension; toLinearExtension; Catalog.linear_extension_model_satisfaction",
    "sourceNote": "Derived for the explicit selected model. Natural-number ≤ is linear and contains equality, giving an inhabited infinite example with distinct comparable elements.",
    "provenanceKind": "derived",
    "leanFormulation": "Nonempty (Catalog.OrderLinearExtension Nat (fun a b => a = b))",
    "formulationSource": "urn:csabs:source/seven-lean-models",
    "formulationLocator": "Catalog.linear_extension_model_satisfaction",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Natural-number ≤ is linear and contains equality, giving an inhabited infinite example with distinct comparable elements.",
    "leanModelLimitations": "Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/OrderLinearExtension-defining-profile\": \"Proved constraint for the specified concrete interpretation or structural recursion; not a hypothesis asserting its own satisfaction. Natural-number ≤ is linear and contains equality, giving an inhabited infinite example with distinct comparable elements.\"}"
  },
  {
    "id": "urn:csabs:theorem/OrderLinearExtension-szpilrajn-existence",
    "type": "Theorem",
    "name": "szpilrajn-existence",
    "statement": "Instantiate pinned Mathlib extend_partialOrder, whose Zorn argument produces a total extension on the same carrier. This uses classical choice and gives no canonical algorithm.",
    "formalStatement": "∀ (A : Type) (r : A → A → Prop) [IsPartialOrder A r], Nonempty (Catalog.OrderLinearExtension A r)",
    "assumptions": [
      "Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/OrderLinearExtension"
    ],
    "dependsOn": [
      "urn:csabs:axiom/OrderLinearExtension-defining-profile"
    ],
    "proofSketch": "Instantiate pinned Mathlib extend_partialOrder, whose Zorn argument produces a total extension on the same carrier. This uses classical choice and gives no canonical algorithm.",
    "reviewStatus": "Separately registered Lean witness; require fresh compiler and axiom audit for verified status.",
    "source": [
      "urn:csabs:source/seven-mathlib",
      "urn:csabs:source/seven-lean-models"
    ],
    "sourceLocator": "Order/Extension/Linear.lean: extend_partialOrder; LinearExtension; toLinearExtension; Catalog.szpilrajn",
    "sourceNote": "Derived for the explicit selected model. Instantiate pinned Mathlib extend_partialOrder, whose Zorn argument produces a total extension on the same carrier. This uses classical choice and gives no canonical algorithm.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ (A : Type) (r : A → A → Prop) [IsPartialOrder A r], Nonempty (Catalog.OrderLinearExtension A r)",
    "formulationSource": "urn:csabs:source/seven-lean-models",
    "formulationLocator": "Catalog.szpilrajn",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Instantiate pinned Mathlib extend_partialOrder, whose Zorn argument produces a total extension on the same carrier. This uses classical choice and gives no canonical algorithm.",
    "leanModelLimitations": "Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/OrderLinearExtension-defining-profile\": \"Proved constraint for the specified concrete interpretation or structural recursion; not a hypothesis asserting its own satisfaction. Instantiate pinned Mathlib extend_partialOrder, whose Zorn argument produces a total extension on the same carrier. This uses classical choice and gives no canonical algorithm.\"}"
  }
]
```
<!-- graph-record:end -->
