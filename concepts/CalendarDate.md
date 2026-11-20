# Positive-year proleptic Gregorian calendar date

A valid year/month/day value in the proleptic Gregorian calendar with positive unbounded year and lexicographic chronological order.

**Notation:** (y,m,d); y≥1; 1≤m≤12; 1≤d≤days(y,m)

**Stable ID:** `urn:csabs:concept/CalendarDate`

**Categories:** Order and fixed points

**Kind:** Abstract data type

**Prerequisites:** [Total Order](TotalOrder.md)

**Specializes:** [Total Order](TotalOrder.md)

## Mathematical formulation

Date={(y,m,d)∈ℕ³ | y≥1 ∧ 1≤m≤12 ∧ 1≤d≤days(y,m)}; leap(y)⇔4|y∧(100∤y∨400|y); a≤b ⇔ (a.y,a.m,a.d)≤lex(b.y,b.m,b.d).

**Lean formulation** (in its source module context):

```lean
abbrev CalendarDate := {t : Nat × Nat × Nat // validDate t.1 t.2.1 t.2.2}
```

**Source:** [`Catalog.CalendarDate`](../lean/Catalog/ReleaseSequenceModels.lean); consulted 2026-11-20.

**Scope:** model

**Interpretation:** Date={(y,m,d)∈ℕ³ | y≥1 ∧ 1≤m≤12 ∧ 1≤d≤days(y,m)}; leap(y)⇔4|y∧(100∤y∨400|y); a≤b ⇔ (a.y,a.m,a.d)≤lex(b.y,b.m,b.d).

**Limits:** Years are positive unbounded naturals, with no year zero or BCE dates. Apply Gregorian rules uniformly to all years, independent of historical calendar adoption. Exact tuple equality; no timezone, UTC instant, time of day, leap seconds, duration, date arithmetic, parsing/formatting, overflow or locale semantics. This extends RFC 3339 calendar rules beyond its four-digit timestamp syntax; it is not that timestamp datatype. Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Valid dates satisfy year≥1, month∈1..12 and day∈1..monthDays. February has 29 days iff year divisible by 4 and (not by 100 or divisible by 400); otherwise 28. April,June,September,November have 30, others 31. Compare valid tuples by year,month,day lexicographically.

**basisKind:** defined-structure

**basisScope:** Years are positive unbounded naturals, with no year zero or BCE dates. Apply Gregorian rules uniformly to all years, independent of historical calendar adoption. Exact tuple equality; no timezone, UTC instant, time of day, leap seconds, duration, date arithmetic, parsing/formatting, overflow or locale semantics. This extends RFC 3339 calendar rules beyond its four-digit timestamp syntax; it is not that timestamp datatype.

**specializationNote:** Instantiate the carrier with valid Gregorian date tuples, equality with exact tuple equality and le with year/month/day lexicographic order; preserve all linear-order laws explicitly.

**verificationObligation:** Map exact carriers, equality, totality and the explicit profile conventions before use.; Model and theorem evidence does not establish a concrete software implementation refinement.

**reviewStatus:** Sourced model with separately registered Lean satisfaction and derived witnesses; verification requires fresh audit evidence.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-CalendarDate-valid"></a>

### date validity

`urn:csabs:operation/CalendarDate-valid`

**signature:** valid : ℕ×ℕ×ℕ→Bool

**description:** Check positive year and Gregorian month/day bounds.

**precondition:** Natural tuple; monthDays is meaningful for valid month only.

**postcondition:** True exactly for the selected date carrier; reject invalid month/day/year zero.

**totality:** Total on the stated domain.

**source:** [RFC 3339: Date and Time on the Internet: Timestamps](https://www.rfc-editor.org/rfc/rfc3339); citation: July 2002, §§5.6–5.7 and Appendix C: Gregorian month lengths and leap-year calculation.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; [Pinned Mathlib list and lexicographic order constructions and linear-order extension](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); citation: Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679: Data/Finset/Card.lean Finset.card; Data/List/TakeDrop.lean dropSlice_eq and length_dropSlice; Data/List/Lex.lean linearOrder; Order/Sum/Order.lean Sum.Lex; Order/Prod/Lex/Basic.lean Prod.Lex; Order/Extension/Linear.lean extend_partialOrder and toLinearExtension. Apache-2.0.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference

**sourceLocator:** RFC 3339 §§5.6–5.7, Appendix C; Mathlib Prod.Lex

**sourceNote:** Adapts the consulted Gregorian month/leap rules to positive unbounded years; tuple order is a derived construction.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-CalendarDate-month-days"></a>

### Gregorian month length

`urn:csabs:operation/CalendarDate-month-days`

**signature:** days : {(y,m)∈ℕ² | y≥1 ∧ 1≤m≤12}→{28,29,30,31}

**description:** Evaluate leap rule and month table.

**precondition:** Positive year and valid month.

**postcondition:** February 28 or 29, listed short months 30, others 31.

**totality:** Partial on invalid calendar month/year; Lean total helper outside that domain is not a calendar contract.

**source:** [RFC 3339: Date and Time on the Internet: Timestamps](https://www.rfc-editor.org/rfc/rfc3339); citation: July 2002, §§5.6–5.7 and Appendix C: Gregorian month lengths and leap-year calculation.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; [Pinned Mathlib list and lexicographic order constructions and linear-order extension](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); citation: Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679: Data/Finset/Card.lean Finset.card; Data/List/TakeDrop.lean dropSlice_eq and length_dropSlice; Data/List/Lex.lean linearOrder; Order/Sum/Order.lean Sum.Lex; Order/Prod/Lex/Basic.lean Prod.Lex; Order/Extension/Linear.lean extend_partialOrder and toLinearExtension. Apache-2.0.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference

**sourceLocator:** RFC 3339 §§5.6–5.7, Appendix C; Mathlib Prod.Lex

**sourceNote:** Adapts the consulted Gregorian month/leap rules to positive unbounded years; tuple order is a derived construction.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-CalendarDate-le"></a>

### chronological date order

`urn:csabs:operation/CalendarDate-le`

**signature:** le : Date×Date→Prop

**description:** Compare year, then month, then day.

**precondition:** Both values valid.

**postcondition:** Exact non-strict chronological order for this Gregorian profile.

**totality:** Total on the stated domain.

**source:** [RFC 3339: Date and Time on the Internet: Timestamps](https://www.rfc-editor.org/rfc/rfc3339); citation: July 2002, §§5.6–5.7 and Appendix C: Gregorian month lengths and leap-year calculation.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; [Pinned Mathlib list and lexicographic order constructions and linear-order extension](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); citation: Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679: Data/Finset/Card.lean Finset.card; Data/List/TakeDrop.lean dropSlice_eq and length_dropSlice; Data/List/Lex.lean linearOrder; Order/Sum/Order.lean Sum.Lex; Order/Prod/Lex/Basic.lean Prod.Lex; Order/Extension/Linear.lean extend_partialOrder and toLinearExtension. Apache-2.0.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference

**sourceLocator:** RFC 3339 §§5.6–5.7, Appendix C; Mathlib Prod.Lex

**sourceNote:** Adapts the consulted Gregorian month/leap rules to positive unbounded years; tuple order is a derived construction.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-CalendarDate-defining-profile"></a>

### defining profile

`urn:csabs:axiom/CalendarDate-defining-profile`

**statement:** Valid dates satisfy year≥1, month∈1..12 and day∈1..monthDays. February has 29 days iff year divisible by 4 and (not by 100 or divisible by 400); otherwise 28. April,June,September,November have 30, others 31. Compare valid tuples by year,month,day lexicographically.

**formalStatement:** Date={(y,m,d)∈ℕ³ | y≥1 ∧ 1≤m≤12 ∧ 1≤d≤days(y,m)}; leap(y)⇔4|y∧(100∤y∨400|y); a≤b ⇔ (a.y,a.m,a.d)≤lex(b.y,b.m,b.d).

**assumptions:** Years are positive unbounded naturals, with no year zero or BCE dates. Apply Gregorian rules uniformly to all years, independent of historical calendar adoption. Exact tuple equality; no timezone, UTC instant, time of day, leap seconds, duration, date arithmetic, parsing/formatting, overflow or locale semantics. This extends RFC 3339 calendar rules beyond its four-digit timestamp syntax; it is not that timestamp datatype.

**ruleRole:** defining-rule

**reviewStatus:** Structure constraints; satisfaction is established separately for the selected model.

**source:** [RFC 3339: Date and Time on the Internet: Timestamps](https://www.rfc-editor.org/rfc/rfc3339); citation: July 2002, §§5.6–5.7 and Appendix C: Gregorian month lengths and leap-year calculation.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; [Pinned Mathlib list and lexicographic order constructions and linear-order extension](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); citation: Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679: Data/Finset/Card.lean Finset.card; Data/List/TakeDrop.lean dropSlice_eq and length_dropSlice; Data/List/Lex.lean linearOrder; Order/Sum/Order.lean Sum.Lex; Order/Prod/Lex/Basic.lean Prod.Lex; Order/Extension/Linear.lean extend_partialOrder and toLinearExtension. Apache-2.0.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference

**sourceLocator:** RFC 3339 §§5.6–5.7, Appendix C; Mathlib Prod.Lex

**sourceNote:** Adapts the consulted Gregorian month/leap rules to positive unbounded years; tuple order is a derived construction.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-CalendarDate-date-order"></a>

### date-order

`urn:csabs:law/CalendarDate-date-order`

**statement:** Lift the lexicographic linear order on year/month/day; injectivity of the tuple key gives exact date antisymmetry.

**formalStatement:** (∀ a : Catalog.CalendarDate, Catalog.dateLE a a) ∧ (∀ a b c, Catalog.dateLE a b → Catalog.dateLE b c → Catalog.dateLE a c) ∧ (∀ a b, Catalog.dateLE a b ∨ Catalog.dateLE b a) ∧ (∀ a b, Catalog.dateLE a b → Catalog.dateLE b a → a = b)

**assumptions:** Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality.

**dependsOn:** [defining profile](CalendarDate.md#node-urn-csabs-axiom-CalendarDate-defining-profile)

**proofSketch:** Lift the lexicographic linear order on year/month/day; injectivity of the tuple key gives exact date antisymmetry.

**reviewStatus:** Derived mathematical law; separately registered theorem supplies explicit proof evidence.

**source:** [RFC 3339: Date and Time on the Internet: Timestamps](https://www.rfc-editor.org/rfc/rfc3339); citation: July 2002, §§5.6–5.7 and Appendix C: Gregorian month lengths and leap-year calculation.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; [Pinned Mathlib list and lexicographic order constructions and linear-order extension](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); citation: Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679: Data/Finset/Card.lean Finset.card; Data/List/TakeDrop.lean dropSlice_eq and length_dropSlice; Data/List/Lex.lean linearOrder; Order/Sum/Order.lean Sum.Lex; Order/Prod/Lex/Basic.lean Prod.Lex; Order/Extension/Linear.lean extend_partialOrder and toLinearExtension. Apache-2.0.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; Catalog release, sequence, transducer, schema, date and extension models and witnesses; path: lean/Catalog/ReleaseSequenceModels.lean; accessedOn: 2026-11-20; sourceRole: local-lean-formulation-and-proof

**sourceLocator:** RFC 3339 §§5.6–5.7, Appendix C; Mathlib Prod.Lex; Catalog.date_order_laws

**sourceNote:** Derived for the explicit selected model. Lift the lexicographic linear order on year/month/day; injectivity of the tuple key gives exact date antisymmetry.

**provenanceKind:** derived

**ruleRole:** derived-law

## Theorems

<a id="node-urn-csabs-theorem-CalendarDate-model-satisfaction"></a>

### model-satisfaction

`urn:csabs:theorem/CalendarDate-model-satisfaction`

**statement:** Compute the Gregorian century rule and month lengths; include valid and invalid dates.

**formalStatement:** Catalog.validDate 2000 2 29 ∧ ¬ Catalog.validDate 1900 2 29 ∧ Catalog.validDate 2026 11 20 ∧ ¬ Catalog.validDate 2026 4 31

**assumptions:** Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality.

**dependsOn:** [defining profile](CalendarDate.md#node-urn-csabs-axiom-CalendarDate-defining-profile)

**proofSketch:** Compute the Gregorian century rule and month lengths; include valid and invalid dates.

**reviewStatus:** Separately registered Lean witness; require fresh compiler and axiom audit for verified status.

**source:** [RFC 3339: Date and Time on the Internet: Timestamps](https://www.rfc-editor.org/rfc/rfc3339); citation: July 2002, §§5.6–5.7 and Appendix C: Gregorian month lengths and leap-year calculation.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; [Pinned Mathlib list and lexicographic order constructions and linear-order extension](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); citation: Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679: Data/Finset/Card.lean Finset.card; Data/List/TakeDrop.lean dropSlice_eq and length_dropSlice; Data/List/Lex.lean linearOrder; Order/Sum/Order.lean Sum.Lex; Order/Prod/Lex/Basic.lean Prod.Lex; Order/Extension/Linear.lean extend_partialOrder and toLinearExtension. Apache-2.0.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; Catalog release, sequence, transducer, schema, date and extension models and witnesses; path: lean/Catalog/ReleaseSequenceModels.lean; accessedOn: 2026-11-20; sourceRole: local-lean-formulation-and-proof

**sourceLocator:** RFC 3339 §§5.6–5.7, Appendix C; Mathlib Prod.Lex; Catalog.date_model_satisfaction

**sourceNote:** Derived for the explicit selected model. Compute the Gregorian century rule and month lengths; include valid and invalid dates.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
Catalog.validDate 2000 2 29 ∧ ¬ Catalog.validDate 1900 2 29 ∧ Catalog.validDate 2026 11 20 ∧ ¬ Catalog.validDate 2026 4 31
```

**Source:** [`Catalog.date_model_satisfaction`](../lean/Catalog/ReleaseSequenceModels.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** Compute the Gregorian century rule and month lengths; include valid and invalid dates.

**Limits:** Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/CalendarDate-defining-profile": "Proved constraint for the specified concrete interpretation or structural recursion; not a hypothesis asserting its own satisfaction. Compute the Gregorian century rule and month lengths; include valid and invalid dates."
}
```

<a id="node-urn-csabs-theorem-CalendarDate-date-order"></a>

### date-order

`urn:csabs:theorem/CalendarDate-date-order`

**statement:** Lift the lexicographic linear order on year/month/day; injectivity of the tuple key gives exact date antisymmetry.

**formalStatement:** (∀ a : Catalog.CalendarDate, Catalog.dateLE a a) ∧ (∀ a b c, Catalog.dateLE a b → Catalog.dateLE b c → Catalog.dateLE a c) ∧ (∀ a b, Catalog.dateLE a b ∨ Catalog.dateLE b a) ∧ (∀ a b, Catalog.dateLE a b → Catalog.dateLE b a → a = b)

**assumptions:** Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality.

**dependsOn:** [defining profile](CalendarDate.md#node-urn-csabs-axiom-CalendarDate-defining-profile)

**proofSketch:** Lift the lexicographic linear order on year/month/day; injectivity of the tuple key gives exact date antisymmetry.

**reviewStatus:** Separately registered Lean witness; require fresh compiler and axiom audit for verified status.

**source:** [RFC 3339: Date and Time on the Internet: Timestamps](https://www.rfc-editor.org/rfc/rfc3339); citation: July 2002, §§5.6–5.7 and Appendix C: Gregorian month lengths and leap-year calculation.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; [Pinned Mathlib list and lexicographic order constructions and linear-order extension](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); citation: Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679: Data/Finset/Card.lean Finset.card; Data/List/TakeDrop.lean dropSlice_eq and length_dropSlice; Data/List/Lex.lean linearOrder; Order/Sum/Order.lean Sum.Lex; Order/Prod/Lex/Basic.lean Prod.Lex; Order/Extension/Linear.lean extend_partialOrder and toLinearExtension. Apache-2.0.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; Catalog release, sequence, transducer, schema, date and extension models and witnesses; path: lean/Catalog/ReleaseSequenceModels.lean; accessedOn: 2026-11-20; sourceRole: local-lean-formulation-and-proof

**sourceLocator:** RFC 3339 §§5.6–5.7, Appendix C; Mathlib Prod.Lex; Catalog.date_order_laws

**sourceNote:** Derived for the explicit selected model. Lift the lexicographic linear order on year/month/day; injectivity of the tuple key gives exact date antisymmetry.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
(∀ a : Catalog.CalendarDate, Catalog.dateLE a a) ∧ (∀ a b c, Catalog.dateLE a b → Catalog.dateLE b c → Catalog.dateLE a c) ∧ (∀ a b, Catalog.dateLE a b ∨ Catalog.dateLE b a) ∧ (∀ a b, Catalog.dateLE a b → Catalog.dateLE b a → a = b)
```

**Source:** [`Catalog.date_order_laws`](../lean/Catalog/ReleaseSequenceModels.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** Lift the lexicographic linear order on year/month/day; injectivity of the tuple key gives exact date antisymmetry.

**Limits:** Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/CalendarDate-defining-profile": "Proved constraint for the specified concrete interpretation or structural recursion; not a hypothesis asserting its own satisfaction. Lift the lexicographic linear order on year/month/day; injectivity of the tuple key gives exact date antisymmetry."
}
```

## Concept provenance

- [RFC 3339: Date and Time on the Internet: Timestamps](https://www.rfc-editor.org/rfc/rfc3339); citation: July 2002, §§5.6–5.7 and Appendix C: Gregorian month lengths and leap-year calculation.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference
- [Pinned Mathlib list and lexicographic order constructions and linear-order extension](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); citation: Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679: Data/Finset/Card.lean Finset.card; Data/List/TakeDrop.lean dropSlice_eq and length_dropSlice; Data/List/Lex.lean linearOrder; Order/Sum/Order.lean Sum.Lex; Order/Prod/Lex/Basic.lean Prod.Lex; Order/Extension/Linear.lean extend_partialOrder and toLinearExtension. Apache-2.0.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference

**sourceLocator:** RFC 3339 §§5.6–5.7, Appendix C; Mathlib Prod.Lex

**sourceNote:** Adapts the consulted Gregorian month/leap rules to positive unbounded years; tuple order is a derived construction.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/CalendarDate",
    "type": "Concept",
    "shortForm": "CalendarDate",
    "fullName": "Positive-year proleptic Gregorian calendar date",
    "synonyms": [
      "Gregorian civil date (positive-year profile)",
      "Year-month-day date (Gregorian)"
    ],
    "category": [
      "urn:csabs:category/order"
    ],
    "kind": "urn:csabs:kind/abstract-data-type",
    "definition": "A valid year/month/day value in the proleptic Gregorian calendar with positive unbounded year and lexicographic chronological order.",
    "notation": "(y,m,d); y≥1; 1≤m≤12; 1≤d≤days(y,m)",
    "requiresConcept": [
      "urn:csabs:concept/TotalOrder"
    ],
    "relatedConcept": [],
    "axiomBasis": "Valid dates satisfy year≥1, month∈1..12 and day∈1..monthDays. February has 29 days iff year divisible by 4 and (not by 100 or divisible by 400); otherwise 28. April,June,September,November have 30, others 31. Compare valid tuples by year,month,day lexicographically.",
    "basisKind": "defined-structure",
    "basisScope": "Years are positive unbounded naturals, with no year zero or BCE dates. Apply Gregorian rules uniformly to all years, independent of historical calendar adoption. Exact tuple equality; no timezone, UTC instant, time of day, leap seconds, duration, date arithmetic, parsing/formatting, overflow or locale semantics. This extends RFC 3339 calendar rules beyond its four-digit timestamp syntax; it is not that timestamp datatype.",
    "mathematicalFormulation": "Date={(y,m,d)∈ℕ³ | y≥1 ∧ 1≤m≤12 ∧ 1≤d≤days(y,m)}; leap(y)⇔4|y∧(100∤y∨400|y); a≤b ⇔ (a.y,a.m,a.d)≤lex(b.y,b.m,b.d).",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Sourced model with separately registered Lean satisfaction and derived witnesses; verification requires fresh audit evidence.",
    "verificationObligation": [
      "Map exact carriers, equality, totality and the explicit profile conventions before use.",
      "Model and theorem evidence does not establish a concrete software implementation refinement."
    ],
    "hasOperation": [
      "urn:csabs:operation/CalendarDate-valid",
      "urn:csabs:operation/CalendarDate-month-days",
      "urn:csabs:operation/CalendarDate-le"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/CalendarDate-defining-profile"
    ],
    "hasLaw": [
      "urn:csabs:law/CalendarDate-date-order"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/CalendarDate-model-satisfaction",
      "urn:csabs:theorem/CalendarDate-date-order"
    ],
    "source": [
      "urn:csabs:source/seven-calendar",
      "urn:csabs:source/seven-mathlib"
    ],
    "sourceLocator": "RFC 3339 §§5.6–5.7, Appendix C; Mathlib Prod.Lex",
    "sourceNote": "Adapts the consulted Gregorian month/leap rules to positive unbounded years; tuple order is a derived construction.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/TotalOrder"
    ],
    "specializationNote": "Instantiate the carrier with valid Gregorian date tuples, equality with exact tuple equality and le with year/month/day lexicographic order; preserve all linear-order laws explicitly.",
    "leanFormulation": "abbrev CalendarDate := {t : Nat × Nat × Nat // validDate t.1 t.2.1 t.2.2}",
    "formulationSource": "urn:csabs:source/seven-lean-models",
    "formulationLocator": "Catalog.CalendarDate",
    "formulationScope": "model",
    "leanModelMapping": "Date={(y,m,d)∈ℕ³ | y≥1 ∧ 1≤m≤12 ∧ 1≤d≤days(y,m)}; leap(y)⇔4|y∧(100∤y∨400|y); a≤b ⇔ (a.y,a.m,a.d)≤lex(b.y,b.m,b.d).",
    "leanModelLimitations": "Years are positive unbounded naturals, with no year zero or BCE dates. Apply Gregorian rules uniformly to all years, independent of historical calendar adoption. Exact tuple equality; no timezone, UTC instant, time of day, leap seconds, duration, date arithmetic, parsing/formatting, overflow or locale semantics. This extends RFC 3339 calendar rules beyond its four-digit timestamp syntax; it is not that timestamp datatype. Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit."
  },
  {
    "id": "urn:csabs:operation/CalendarDate-valid",
    "type": "Operation",
    "concept": "urn:csabs:concept/CalendarDate",
    "name": "date validity",
    "signature": "valid : ℕ×ℕ×ℕ→Bool",
    "description": "Check positive year and Gregorian month/day bounds.",
    "precondition": "Natural tuple; monthDays is meaningful for valid month only.",
    "postcondition": "True exactly for the selected date carrier; reject invalid month/day/year zero.",
    "totality": "Total on the stated domain.",
    "source": [
      "urn:csabs:source/seven-calendar",
      "urn:csabs:source/seven-mathlib"
    ],
    "sourceLocator": "RFC 3339 §§5.6–5.7, Appendix C; Mathlib Prod.Lex",
    "sourceNote": "Adapts the consulted Gregorian month/leap rules to positive unbounded years; tuple order is a derived construction.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/CalendarDate-month-days",
    "type": "Operation",
    "concept": "urn:csabs:concept/CalendarDate",
    "name": "Gregorian month length",
    "signature": "days : {(y,m)∈ℕ² | y≥1 ∧ 1≤m≤12}→{28,29,30,31}",
    "description": "Evaluate leap rule and month table.",
    "precondition": "Positive year and valid month.",
    "postcondition": "February 28 or 29, listed short months 30, others 31.",
    "totality": "Partial on invalid calendar month/year; Lean total helper outside that domain is not a calendar contract.",
    "source": [
      "urn:csabs:source/seven-calendar",
      "urn:csabs:source/seven-mathlib"
    ],
    "sourceLocator": "RFC 3339 §§5.6–5.7, Appendix C; Mathlib Prod.Lex",
    "sourceNote": "Adapts the consulted Gregorian month/leap rules to positive unbounded years; tuple order is a derived construction.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/CalendarDate-le",
    "type": "Operation",
    "concept": "urn:csabs:concept/CalendarDate",
    "name": "chronological date order",
    "signature": "le : Date×Date→Prop",
    "description": "Compare year, then month, then day.",
    "precondition": "Both values valid.",
    "postcondition": "Exact non-strict chronological order for this Gregorian profile.",
    "totality": "Total on the stated domain.",
    "source": [
      "urn:csabs:source/seven-calendar",
      "urn:csabs:source/seven-mathlib"
    ],
    "sourceLocator": "RFC 3339 §§5.6–5.7, Appendix C; Mathlib Prod.Lex",
    "sourceNote": "Adapts the consulted Gregorian month/leap rules to positive unbounded years; tuple order is a derived construction.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/CalendarDate-defining-profile",
    "type": "Axiom",
    "name": "defining profile",
    "statement": "Valid dates satisfy year≥1, month∈1..12 and day∈1..monthDays. February has 29 days iff year divisible by 4 and (not by 100 or divisible by 400); otherwise 28. April,June,September,November have 30, others 31. Compare valid tuples by year,month,day lexicographically.",
    "formalStatement": "Date={(y,m,d)∈ℕ³ | y≥1 ∧ 1≤m≤12 ∧ 1≤d≤days(y,m)}; leap(y)⇔4|y∧(100∤y∨400|y); a≤b ⇔ (a.y,a.m,a.d)≤lex(b.y,b.m,b.d).",
    "assumptions": [
      "Years are positive unbounded naturals, with no year zero or BCE dates. Apply Gregorian rules uniformly to all years, independent of historical calendar adoption. Exact tuple equality; no timezone, UTC instant, time of day, leap seconds, duration, date arithmetic, parsing/formatting, overflow or locale semantics. This extends RFC 3339 calendar rules beyond its four-digit timestamp syntax; it is not that timestamp datatype."
    ],
    "appliesTo": [
      "urn:csabs:concept/CalendarDate"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Structure constraints; satisfaction is established separately for the selected model.",
    "source": [
      "urn:csabs:source/seven-calendar",
      "urn:csabs:source/seven-mathlib"
    ],
    "sourceLocator": "RFC 3339 §§5.6–5.7, Appendix C; Mathlib Prod.Lex",
    "sourceNote": "Adapts the consulted Gregorian month/leap rules to positive unbounded years; tuple order is a derived construction.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/CalendarDate-date-order",
    "type": "Law",
    "name": "date-order",
    "statement": "Lift the lexicographic linear order on year/month/day; injectivity of the tuple key gives exact date antisymmetry.",
    "formalStatement": "(∀ a : Catalog.CalendarDate, Catalog.dateLE a a) ∧ (∀ a b c, Catalog.dateLE a b → Catalog.dateLE b c → Catalog.dateLE a c) ∧ (∀ a b, Catalog.dateLE a b ∨ Catalog.dateLE b a) ∧ (∀ a b, Catalog.dateLE a b → Catalog.dateLE b a → a = b)",
    "assumptions": [
      "Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/CalendarDate"
    ],
    "dependsOn": [
      "urn:csabs:axiom/CalendarDate-defining-profile"
    ],
    "proofSketch": "Lift the lexicographic linear order on year/month/day; injectivity of the tuple key gives exact date antisymmetry.",
    "reviewStatus": "Derived mathematical law; separately registered theorem supplies explicit proof evidence.",
    "source": [
      "urn:csabs:source/seven-calendar",
      "urn:csabs:source/seven-mathlib",
      "urn:csabs:source/seven-lean-models"
    ],
    "sourceLocator": "RFC 3339 §§5.6–5.7, Appendix C; Mathlib Prod.Lex; Catalog.date_order_laws",
    "sourceNote": "Derived for the explicit selected model. Lift the lexicographic linear order on year/month/day; injectivity of the tuple key gives exact date antisymmetry.",
    "provenanceKind": "derived",
    "ruleRole": "derived-law"
  },
  {
    "id": "urn:csabs:theorem/CalendarDate-model-satisfaction",
    "type": "Theorem",
    "name": "model-satisfaction",
    "statement": "Compute the Gregorian century rule and month lengths; include valid and invalid dates.",
    "formalStatement": "Catalog.validDate 2000 2 29 ∧ ¬ Catalog.validDate 1900 2 29 ∧ Catalog.validDate 2026 11 20 ∧ ¬ Catalog.validDate 2026 4 31",
    "assumptions": [
      "Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/CalendarDate"
    ],
    "dependsOn": [
      "urn:csabs:axiom/CalendarDate-defining-profile"
    ],
    "proofSketch": "Compute the Gregorian century rule and month lengths; include valid and invalid dates.",
    "reviewStatus": "Separately registered Lean witness; require fresh compiler and axiom audit for verified status.",
    "source": [
      "urn:csabs:source/seven-calendar",
      "urn:csabs:source/seven-mathlib",
      "urn:csabs:source/seven-lean-models"
    ],
    "sourceLocator": "RFC 3339 §§5.6–5.7, Appendix C; Mathlib Prod.Lex; Catalog.date_model_satisfaction",
    "sourceNote": "Derived for the explicit selected model. Compute the Gregorian century rule and month lengths; include valid and invalid dates.",
    "provenanceKind": "derived",
    "leanFormulation": "Catalog.validDate 2000 2 29 ∧ ¬ Catalog.validDate 1900 2 29 ∧ Catalog.validDate 2026 11 20 ∧ ¬ Catalog.validDate 2026 4 31",
    "formulationSource": "urn:csabs:source/seven-lean-models",
    "formulationLocator": "Catalog.date_model_satisfaction",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Compute the Gregorian century rule and month lengths; include valid and invalid dates.",
    "leanModelLimitations": "Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/CalendarDate-defining-profile\": \"Proved constraint for the specified concrete interpretation or structural recursion; not a hypothesis asserting its own satisfaction. Compute the Gregorian century rule and month lengths; include valid and invalid dates.\"}"
  },
  {
    "id": "urn:csabs:theorem/CalendarDate-date-order",
    "type": "Theorem",
    "name": "date-order",
    "statement": "Lift the lexicographic linear order on year/month/day; injectivity of the tuple key gives exact date antisymmetry.",
    "formalStatement": "(∀ a : Catalog.CalendarDate, Catalog.dateLE a a) ∧ (∀ a b c, Catalog.dateLE a b → Catalog.dateLE b c → Catalog.dateLE a c) ∧ (∀ a b, Catalog.dateLE a b ∨ Catalog.dateLE b a) ∧ (∀ a b, Catalog.dateLE a b → Catalog.dateLE b a → a = b)",
    "assumptions": [
      "Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/CalendarDate"
    ],
    "dependsOn": [
      "urn:csabs:axiom/CalendarDate-defining-profile"
    ],
    "proofSketch": "Lift the lexicographic linear order on year/month/day; injectivity of the tuple key gives exact date antisymmetry.",
    "reviewStatus": "Separately registered Lean witness; require fresh compiler and axiom audit for verified status.",
    "source": [
      "urn:csabs:source/seven-calendar",
      "urn:csabs:source/seven-mathlib",
      "urn:csabs:source/seven-lean-models"
    ],
    "sourceLocator": "RFC 3339 §§5.6–5.7, Appendix C; Mathlib Prod.Lex; Catalog.date_order_laws",
    "sourceNote": "Derived for the explicit selected model. Lift the lexicographic linear order on year/month/day; injectivity of the tuple key gives exact date antisymmetry.",
    "provenanceKind": "derived",
    "leanFormulation": "(∀ a : Catalog.CalendarDate, Catalog.dateLE a a) ∧ (∀ a b c, Catalog.dateLE a b → Catalog.dateLE b c → Catalog.dateLE a c) ∧ (∀ a b, Catalog.dateLE a b ∨ Catalog.dateLE b a) ∧ (∀ a b, Catalog.dateLE a b → Catalog.dateLE b a → a = b)",
    "formulationSource": "urn:csabs:source/seven-lean-models",
    "formulationLocator": "Catalog.date_order_laws",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Lift the lexicographic linear order on year/month/day; injectivity of the tuple key gives exact date antisymmetry.",
    "leanModelLimitations": "Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/CalendarDate-defining-profile\": \"Proved constraint for the specified concrete interpretation or structural recursion; not a hypothesis asserting its own satisfaction. Lift the lexicographic linear order on year/month/day; injectivity of the tuple key gives exact date antisymmetry.\"}"
  }
]
```
<!-- graph-record:end -->
