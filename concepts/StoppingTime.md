# Stopping time (discrete time, possibly infinite)

A random time τ:Ω→ℕ∪{∞} relative to a filtration, for which whether stopping has occurred by time n is determined by information available at n. Infinity means never stopping.

**Notation:** τ:Ω→ℕ∪{∞}; {τ≤n}∈𝓕ₙ for every n∈ℕ

**Stable ID:** `urn:csabs:concept/StoppingTime`

**Categories:** Probability and stochastic models → Stochastic processes, Probability and stochastic models, Measure theory

**Kind:** Mathematical structure

**Prerequisites:** [Filtration (increasing sub-sigma-algebras)](Filtration.md)

## Mathematical formulation

τ:Ω→ℕ∪{∞}; {τ≤n}∈𝓕ₙ for every n∈ℕ. For each finite n, the decision event {ω:τ(ω)≤n} is 𝓕ₙ-measurable. Discrete nonnegative integer times with an explicit infinity value. No almost-sure finiteness, boundedness or finite expectation assumption. Equality is pointwise in all supplied arguments; almost-sure equality and equality in distribution are distinct.

**Lean formulation** (in its source module context):

```lean
abbrev StoppingTime {Ω : Type*} [m : _root_.MeasurableSpace Ω]
    (f : Filtration ℕ m) :=
  {τ : Ω → WithTop ℕ // MeasureTheory.IsStoppingTime f τ}
```

**Source:** [`Catalog.StoppingTime`](../lean/Catalog/StochasticProcesses.lean); consulted 2026-11-20.

**Scope:** model

**Interpretation:** Subtype Ω → WithTop ℕ constrained by MeasureTheory.IsStoppingTime. The top value is never stopping; equality is pointwise, not equality almost surely.

**Limits:** Only discrete time is selected. No optional-stopping result, stopped-process construction or finiteness claim.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** For each finite n, the decision event {ω:τ(ω)≤n} is 𝓕ₙ-measurable.

**basisKind:** defined-structure

**basisScope:** Discrete nonnegative integer times with an explicit infinity value. No almost-sure finiteness, boundedness or finite expectation assumption.

**verificationObligation:** Use the declared carriers, equality and measurable sigma-algebras. Prerequisites do not automatically transfer claims.; Only discrete time is selected. No optional-stopping result, stopped-process construction or finiteness claim.

**reviewStatus:** sourced editorial interface; model-satisfaction witness registered separately

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-StoppingTime-occurred-by"></a>

### occurred-by

`urn:csabs:operation/StoppingTime-occurred-by`

**signature:** (n:ℕ) → {A⊆Ω | A∈𝓕ₙ}

**description:** n ↦ {ω:τ(ω)≤n}; for τ(ω)=∞ this decision is false at every finite n. Total on ℕ.

**precondition:** Fix the concept parameters; inputs lie in the signature domains and satisfy its displayed constraints.

**postcondition:** n ↦ {ω:τ(ω)≤n}; for τ(ω)=∞ this decision is false at every finite n. Total on ℕ.

**totality:** total on the stated domain

## Axioms and defining rules

<a id="node-urn-csabs-axiom-StoppingTime-basis"></a>

### basis

`urn:csabs:axiom/StoppingTime-basis`

**statement:** For each finite n, the decision event {ω:τ(ω)≤n} is 𝓕ₙ-measurable.

**formalStatement:** ∀n∈ℕ: {ω:τ(ω)≤n}∈𝓕ₙ

**assumptions:** (Ω,Σ) is a measurable space; 𝓕 is an ℕ-indexed filtration in Σ; τ:Ω→ℕ∪{∞}.

**ruleRole:** defining-rule

**reviewStatus:** sourced defining constraint; not itself a theorem witness

**notationLanguage:** informal mathematical Unicode

**source:** [Mathlib 4.35.0: Stopping times](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Probability/Process/Stopping.lean); citation: Mathlib contributors, mathlib4, revision 56a005855ea17e0b0958f73ec801ae140b0a1679. Consulted installed source; Apache-2.0 license. Definitions adapted, not copied as prose.; path: lean/.lake/packages/mathlib/Mathlib/Probability/Process/Stopping.lean; accessedOn: 2026-11-20; sourceRole: primary mathematical definition and formal reference

**sourceLocator:** MeasureTheory.IsStoppingTime; isStoppingTime_const; module introduction explaining WithTop

**sourceNote:** Adapted from the consulted pinned source to the explicit catalog carriers and equality conventions.

**provenanceKind:** adapted

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-StoppingTime-model-satisfaction"></a>

### model-satisfaction

`urn:csabs:theorem/StoppingTime-model-satisfaction`

**statement:** For every filtration indexed by ℕ, τ(ω)=0 is a stopping time.

**formalStatement:** For every filtration indexed by ℕ, τ(ω)=0 is a stopping time.

**assumptions:** Use the parameters and semantic conventions in the concept definition.

**dependsOn:** [basis](StoppingTime.md#node-urn-csabs-axiom-StoppingTime-basis)

**proofSketch:** For every n∈ℕ, the event {0≤n} is Ω and is measurable in 𝓕ₙ. This is a concrete finite stopping rule, not a finiteness assertion about arbitrary τ.

**reviewStatus:** constructive Lean witness registered; verification requires a fresh compiler and axiom-audit report

**notationLanguage:** informal mathematical Unicode

**source:** [Mathlib 4.35.0: Stopping times](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Probability/Process/Stopping.lean); citation: Mathlib contributors, mathlib4, revision 56a005855ea17e0b0958f73ec801ae140b0a1679. Consulted installed source; Apache-2.0 license. Definitions adapted, not copied as prose.; path: lean/.lake/packages/mathlib/Mathlib/Probability/Process/Stopping.lean; accessedOn: 2026-11-20; sourceRole: primary mathematical definition and formal reference

**sourceLocator:** MeasureTheory.IsStoppingTime; isStoppingTime_const; module introduction explaining WithTop

**sourceNote:** Constructive model derived from the linked defining constraints and the cited library construction; the local Lean theorem separately checks the stated type.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {Ω : Type} [m : MeasurableSpace Ω] (f : Catalog.Filtration ℕ m), Nonempty (Catalog.StoppingTime f)
```

**Source:** [`Catalog.stoppingTime_model_satisfaction`](../lean/Catalog/StochasticProcesses.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** For every filtration indexed by ℕ, τ(ω)=0 is a stopping time. The Nonempty inhabitant contains the defining constraints as checked proof fields; this witnesses model existence, not all properties of arbitrary processes.

**Limits:** Constructive model satisfaction for the stated parameters only. No blanket proof of other catalog operations or derived results.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/StoppingTime-basis": "Satisfied by the concrete construction in the proof: For every n∈ℕ, the event {0≤n} is Ω and is measurable in 𝓕ₙ. This is a concrete finite stopping rule, not a finiteness assertion about arbitrary τ."
}
```

## Concept provenance

- [Mathlib 4.35.0: Stopping times](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Probability/Process/Stopping.lean); citation: Mathlib contributors, mathlib4, revision 56a005855ea17e0b0958f73ec801ae140b0a1679. Consulted installed source; Apache-2.0 license. Definitions adapted, not copied as prose.; path: lean/.lake/packages/mathlib/Mathlib/Probability/Process/Stopping.lean; accessedOn: 2026-11-20; sourceRole: primary mathematical definition and formal reference

**sourceLocator:** MeasureTheory.IsStoppingTime; isStoppingTime_const; module introduction explaining WithTop

**sourceNote:** Adapted from the consulted pinned source to the explicit catalog carriers and equality conventions.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/StoppingTime",
    "type": "Concept",
    "shortForm": "StoppingTime",
    "fullName": "Stopping time (discrete time, possibly infinite)",
    "synonyms": [
      "Extended-natural stopping time",
      "Discrete stopping rule"
    ],
    "category": [
      "urn:csabs:category/stochastic-processes",
      "urn:csabs:category/probability",
      "urn:csabs:category/measure-theory"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "A random time τ:Ω→ℕ∪{∞} relative to a filtration, for which whether stopping has occurred by time n is determined by information available at n. Infinity means never stopping.",
    "notation": "τ:Ω→ℕ∪{∞}; {τ≤n}∈𝓕ₙ for every n∈ℕ",
    "hasOperation": [
      "urn:csabs:operation/StoppingTime-occurred-by"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/StoppingTime-basis"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/StoppingTime-model-satisfaction"
    ],
    "axiomBasis": "For each finite n, the decision event {ω:τ(ω)≤n} is 𝓕ₙ-measurable.",
    "basisKind": "defined-structure",
    "basisScope": "Discrete nonnegative integer times with an explicit infinity value. No almost-sure finiteness, boundedness or finite expectation assumption.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "sourced editorial interface; model-satisfaction witness registered separately",
    "requiresConcept": [
      "urn:csabs:concept/Filtration"
    ],
    "verificationObligation": [
      "Use the declared carriers, equality and measurable sigma-algebras. Prerequisites do not automatically transfer claims.",
      "Only discrete time is selected. No optional-stopping result, stopped-process construction or finiteness claim."
    ],
    "mathematicalFormulation": "τ:Ω→ℕ∪{∞}; {τ≤n}∈𝓕ₙ for every n∈ℕ. For each finite n, the decision event {ω:τ(ω)≤n} is 𝓕ₙ-measurable. Discrete nonnegative integer times with an explicit infinity value. No almost-sure finiteness, boundedness or finite expectation assumption. Equality is pointwise in all supplied arguments; almost-sure equality and equality in distribution are distinct.",
    "source": [
      "urn:csabs:source/mathlib-pinned-stochastic-stopping"
    ],
    "sourceLocator": "MeasureTheory.IsStoppingTime; isStoppingTime_const; module introduction explaining WithTop",
    "sourceNote": "Adapted from the consulted pinned source to the explicit catalog carriers and equality conventions.",
    "provenanceKind": "adapted",
    "leanFormulation": "abbrev StoppingTime {Ω : Type*} [m : _root_.MeasurableSpace Ω]\n    (f : Filtration ℕ m) :=\n  {τ : Ω → WithTop ℕ // MeasureTheory.IsStoppingTime f τ}",
    "formulationSource": "urn:csabs:source/local-lean-StochasticProcesses",
    "formulationLocator": "Catalog.StoppingTime",
    "formulationScope": "model",
    "leanModelMapping": "Subtype Ω → WithTop ℕ constrained by MeasureTheory.IsStoppingTime. The top value is never stopping; equality is pointwise, not equality almost surely.",
    "leanModelLimitations": "Only discrete time is selected. No optional-stopping result, stopped-process construction or finiteness claim."
  },
  {
    "id": "urn:csabs:operation/StoppingTime-occurred-by",
    "type": "Operation",
    "name": "occurred-by",
    "signature": "(n:ℕ) → {A⊆Ω | A∈𝓕ₙ}",
    "description": "n ↦ {ω:τ(ω)≤n}; for τ(ω)=∞ this decision is false at every finite n. Total on ℕ.",
    "concept": "urn:csabs:concept/StoppingTime",
    "precondition": "Fix the concept parameters; inputs lie in the signature domains and satisfy its displayed constraints.",
    "postcondition": "n ↦ {ω:τ(ω)≤n}; for τ(ω)=∞ this decision is false at every finite n. Total on ℕ.",
    "totality": "total on the stated domain"
  },
  {
    "id": "urn:csabs:axiom/StoppingTime-basis",
    "type": "Axiom",
    "name": "basis",
    "statement": "For each finite n, the decision event {ω:τ(ω)≤n} is 𝓕ₙ-measurable.",
    "formalStatement": "∀n∈ℕ: {ω:τ(ω)≤n}∈𝓕ₙ",
    "assumptions": [
      "(Ω,Σ) is a measurable space; 𝓕 is an ℕ-indexed filtration in Σ; τ:Ω→ℕ∪{∞}."
    ],
    "appliesTo": [
      "urn:csabs:concept/StoppingTime"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "sourced defining constraint; not itself a theorem witness",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/mathlib-pinned-stochastic-stopping"
    ],
    "sourceLocator": "MeasureTheory.IsStoppingTime; isStoppingTime_const; module introduction explaining WithTop",
    "sourceNote": "Adapted from the consulted pinned source to the explicit catalog carriers and equality conventions.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:theorem/StoppingTime-model-satisfaction",
    "type": "Theorem",
    "name": "model-satisfaction",
    "statement": "For every filtration indexed by ℕ, τ(ω)=0 is a stopping time.",
    "formalStatement": "For every filtration indexed by ℕ, τ(ω)=0 is a stopping time.",
    "assumptions": [
      "Use the parameters and semantic conventions in the concept definition."
    ],
    "appliesTo": [
      "urn:csabs:concept/StoppingTime"
    ],
    "dependsOn": [
      "urn:csabs:axiom/StoppingTime-basis"
    ],
    "proofSketch": "For every n∈ℕ, the event {0≤n} is Ω and is measurable in 𝓕ₙ. This is a concrete finite stopping rule, not a finiteness assertion about arbitrary τ.",
    "reviewStatus": "constructive Lean witness registered; verification requires a fresh compiler and axiom-audit report",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/mathlib-pinned-stochastic-stopping"
    ],
    "sourceLocator": "MeasureTheory.IsStoppingTime; isStoppingTime_const; module introduction explaining WithTop",
    "sourceNote": "Constructive model derived from the linked defining constraints and the cited library construction; the local Lean theorem separately checks the stated type.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {Ω : Type} [m : MeasurableSpace Ω] (f : Catalog.Filtration ℕ m), Nonempty (Catalog.StoppingTime f)",
    "formulationSource": "urn:csabs:source/local-lean-StochasticProcesses",
    "formulationLocator": "Catalog.stoppingTime_model_satisfaction",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "For every filtration indexed by ℕ, τ(ω)=0 is a stopping time. The Nonempty inhabitant contains the defining constraints as checked proof fields; this witnesses model existence, not all properties of arbitrary processes.",
    "leanModelLimitations": "Constructive model satisfaction for the stated parameters only. No blanket proof of other catalog operations or derived results.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/StoppingTime-basis\": \"Satisfied by the concrete construction in the proof: For every n∈ℕ, the event {0≤n} is Ω and is measurable in 𝓕ₙ. This is a concrete finite stopping rule, not a finiteness assertion about arbitrary τ.\"}"
  }
]
```
<!-- graph-record:end -->
