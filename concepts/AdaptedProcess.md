# Adapted stochastic process

A stochastic process equipped with a specified filtration such that the coordinate at each time is measurable with respect to the information available by that time.

**Notation:** X:T→Ω→E; 𝓕 filtration of Σ; Xₜ:(Ω,𝓕ₜ)→(E,𝓔)

**Stable ID:** `urn:csabs:concept/AdaptedProcess`

**Categories:** Probability and stochastic models → Stochastic processes, Probability and stochastic models, Measure theory

**Kind:** Mathematical structure

**Prerequisites:** [Stochastic process (measurable random family)](StochasticProcess.md), [Filtration (increasing sub-sigma-algebras)](Filtration.md)

**Specializes:** [Stochastic process (measurable random family)](StochasticProcess.md)

## Backlinks

- [Martingale (discrete-time real-valued)](Martingale.md) — `requiresConcept`
- [Martingale (discrete-time real-valued)](Martingale.md) — `specializationOf`

## Mathematical formulation

X:T→Ω→E; 𝓕 filtration of Σ; Xₜ:(Ω,𝓕ₜ)→(E,𝓔). Retain coordinate measurability of StochasticProcess and require Xₜ to be 𝓕ₜ/𝓔-measurable at every t. General measurable value space E and preordered time. Adaptedness does not imply progressive or joint measurability for continuous time. Equality is pointwise in all supplied arguments; almost-sure equality and equality in distribution are distinct.

**Lean formulation** (in its source module context):

```lean
abbrev AdaptedProcess (T E : Type*) [Preorder T] {Ω : Type*}
    [m : _root_.MeasurableSpace Ω] [_root_.MeasurableSpace E]
    (P : ProbabilitySpace Ω) (f : Filtration T m) :=
  {X : StochasticProcess T E P // MeasureTheory.Adapted f X.value}
```

**Source:** [`Catalog.AdaptedProcess`](../lean/Catalog/StochasticProcesses.lean); consulted 2026-11-20.

**Scope:** model

**Interpretation:** Subtype of StochasticProcess with MeasureTheory.Adapted f X.value, using ordinary measurable adaptedness, not strongly adaptedness as a different general definition.

**Limits:** No predictable/progressive measurability or path regularity. Equality is pointwise equality of the underlying process for fixed P and f.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Retain coordinate measurability of StochasticProcess and require Xₜ to be 𝓕ₜ/𝓔-measurable at every t.

**basisKind:** defined-structure

**basisScope:** General measurable value space E and preordered time. Adaptedness does not imply progressive or joint measurability for continuous time.

**basisInstantiation:** Retain coordinate measurability of StochasticProcess and require Xₜ to be 𝓕ₜ/𝓔-measurable at every t.

**specializationNote:** Keep the same T, E, Ω, Σ, P and family X; supply the filtration and strengthen coordinate measurability to 𝓕ₜ.

**verificationObligation:** Use the declared carriers, equality and measurable sigma-algebras. Prerequisites do not automatically transfer claims.; No predictable/progressive measurability or path regularity. Equality is pointwise equality of the underlying process for fixed P and f.

**reviewStatus:** sourced editorial interface; model-satisfaction witness registered separately

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-AdaptedProcess-observe"></a>

### observe

`urn:csabs:operation/AdaptedProcess-observe`

**signature:** (t:T) → RandomVariable((Ω,𝓕ₜ,P restricted to 𝓕ₜ),E)

**description:** Return Xₜ with its time-local measurability evidence; 𝓕ₜ⊆Σ makes restriction of P well-defined.

**precondition:** Fix the concept parameters; inputs lie in the signature domains and satisfy its displayed constraints.

**postcondition:** Return Xₜ with its time-local measurability evidence; 𝓕ₜ⊆Σ makes restriction of P well-defined.

**totality:** total on the stated domain

## Axioms and defining rules

<a id="node-urn-csabs-axiom-AdaptedProcess-basis"></a>

### basis

`urn:csabs:axiom/AdaptedProcess-basis`

**statement:** Retain coordinate measurability of StochasticProcess and require Xₜ to be 𝓕ₜ/𝓔-measurable at every t.

**formalStatement:** ∀t∈T, B∈𝓔: {ω:Xₜ(ω)∈B}∈𝓕ₜ

**assumptions:** T is preordered; (Ω,Σ,P) is a probability space; (E,𝓔) is measurable; 𝓕 is a filtration in Σ; X is an E-valued stochastic process on Ω.

**ruleRole:** defining-rule

**reviewStatus:** sourced defining constraint; not itself a theorem witness

**notationLanguage:** informal mathematical Unicode

**source:** [Mathlib 4.35.0: Adapted stochastic processes](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Probability/Process/Adapted.lean); citation: Mathlib contributors, mathlib4, revision 56a005855ea17e0b0958f73ec801ae140b0a1679. Consulted installed source; Apache-2.0 license. Definitions adapted, not copied as prose.; path: lean/.lake/packages/mathlib/Mathlib/Probability/Process/Adapted.lean; accessedOn: 2026-11-20; sourceRole: primary mathematical definition and formal reference

**sourceLocator:** MeasureTheory.Adapted; Adapted.measurable; adapted_const

**sourceNote:** Adapted from the consulted pinned source to the explicit catalog carriers and equality conventions.

**provenanceKind:** adapted

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-AdaptedProcess-model-satisfaction"></a>

### model-satisfaction

`urn:csabs:theorem/AdaptedProcess-model-satisfaction`

**statement:** For any filtration 𝓕 and e∈E, Xₜ(ω)=e is adapted to 𝓕.

**formalStatement:** For any filtration 𝓕 and e∈E, Xₜ(ω)=e is adapted to 𝓕.

**assumptions:** Supply e∈E; no empty-value-space existence is claimed.

**dependsOn:** [basis](AdaptedProcess.md#node-urn-csabs-axiom-AdaptedProcess-basis)

**proofSketch:** Constant coordinates have inverse images ∅ or Ω in each 𝓕ₜ and in Σ. Construct the process and its adaptedness evidence explicitly.

**reviewStatus:** constructive Lean witness registered; verification requires a fresh compiler and axiom-audit report

**notationLanguage:** informal mathematical Unicode

**source:** [Mathlib 4.35.0: Adapted stochastic processes](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Probability/Process/Adapted.lean); citation: Mathlib contributors, mathlib4, revision 56a005855ea17e0b0958f73ec801ae140b0a1679. Consulted installed source; Apache-2.0 license. Definitions adapted, not copied as prose.; path: lean/.lake/packages/mathlib/Mathlib/Probability/Process/Adapted.lean; accessedOn: 2026-11-20; sourceRole: primary mathematical definition and formal reference

**sourceLocator:** MeasureTheory.Adapted; Adapted.measurable; adapted_const

**sourceNote:** Constructive model derived from the linked defining constraints and the cited library construction; the local Lean theorem separately checks the stated type.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ (T E : Type) [Preorder T] {Ω : Type} [m : MeasurableSpace Ω] [MeasurableSpace E] (P : Catalog.ProbabilitySpace Ω) (f : Catalog.Filtration T m) (_e : E), Nonempty (Catalog.AdaptedProcess T E P f)
```

**Source:** [`Catalog.adaptedProcess_model_satisfaction`](../lean/Catalog/StochasticProcesses.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** For any filtration 𝓕 and e∈E, Xₜ(ω)=e is adapted to 𝓕. The Nonempty inhabitant contains the defining constraints as checked proof fields; this witnesses model existence, not all properties of arbitrary processes.

**Limits:** Constructive model satisfaction for the stated parameters only. No blanket proof of other catalog operations or derived results.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/AdaptedProcess-basis": "Satisfied by the concrete construction in the proof: Constant coordinates have inverse images ∅ or Ω in each 𝓕ₜ and in Σ. Construct the process and its adaptedness evidence explicitly."
}
```

## Concept provenance

- [Mathlib 4.35.0: Adapted stochastic processes](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Probability/Process/Adapted.lean); citation: Mathlib contributors, mathlib4, revision 56a005855ea17e0b0958f73ec801ae140b0a1679. Consulted installed source; Apache-2.0 license. Definitions adapted, not copied as prose.; path: lean/.lake/packages/mathlib/Mathlib/Probability/Process/Adapted.lean; accessedOn: 2026-11-20; sourceRole: primary mathematical definition and formal reference

**sourceLocator:** MeasureTheory.Adapted; Adapted.measurable; adapted_const

**sourceNote:** Adapted from the consulted pinned source to the explicit catalog carriers and equality conventions.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/AdaptedProcess",
    "type": "Concept",
    "shortForm": "AdaptedProcess",
    "fullName": "Adapted stochastic process",
    "synonyms": [
      "Process adapted to an information filtration"
    ],
    "category": [
      "urn:csabs:category/stochastic-processes",
      "urn:csabs:category/probability",
      "urn:csabs:category/measure-theory"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "A stochastic process equipped with a specified filtration such that the coordinate at each time is measurable with respect to the information available by that time.",
    "notation": "X:T→Ω→E; 𝓕 filtration of Σ; Xₜ:(Ω,𝓕ₜ)→(E,𝓔)",
    "hasOperation": [
      "urn:csabs:operation/AdaptedProcess-observe"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/AdaptedProcess-basis"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/AdaptedProcess-model-satisfaction"
    ],
    "axiomBasis": "Retain coordinate measurability of StochasticProcess and require Xₜ to be 𝓕ₜ/𝓔-measurable at every t.",
    "basisKind": "defined-structure",
    "basisScope": "General measurable value space E and preordered time. Adaptedness does not imply progressive or joint measurability for continuous time.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "sourced editorial interface; model-satisfaction witness registered separately",
    "requiresConcept": [
      "urn:csabs:concept/StochasticProcess",
      "urn:csabs:concept/Filtration"
    ],
    "verificationObligation": [
      "Use the declared carriers, equality and measurable sigma-algebras. Prerequisites do not automatically transfer claims.",
      "No predictable/progressive measurability or path regularity. Equality is pointwise equality of the underlying process for fixed P and f."
    ],
    "mathematicalFormulation": "X:T→Ω→E; 𝓕 filtration of Σ; Xₜ:(Ω,𝓕ₜ)→(E,𝓔). Retain coordinate measurability of StochasticProcess and require Xₜ to be 𝓕ₜ/𝓔-measurable at every t. General measurable value space E and preordered time. Adaptedness does not imply progressive or joint measurability for continuous time. Equality is pointwise in all supplied arguments; almost-sure equality and equality in distribution are distinct.",
    "source": [
      "urn:csabs:source/mathlib-pinned-stochastic-adapted"
    ],
    "sourceLocator": "MeasureTheory.Adapted; Adapted.measurable; adapted_const",
    "sourceNote": "Adapted from the consulted pinned source to the explicit catalog carriers and equality conventions.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/StochasticProcess"
    ],
    "specializationNote": "Keep the same T, E, Ω, Σ, P and family X; supply the filtration and strengthen coordinate measurability to 𝓕ₜ.",
    "basisInstantiation": "Retain coordinate measurability of StochasticProcess and require Xₜ to be 𝓕ₜ/𝓔-measurable at every t.",
    "leanFormulation": "abbrev AdaptedProcess (T E : Type*) [Preorder T] {Ω : Type*}\n    [m : _root_.MeasurableSpace Ω] [_root_.MeasurableSpace E]\n    (P : ProbabilitySpace Ω) (f : Filtration T m) :=\n  {X : StochasticProcess T E P // MeasureTheory.Adapted f X.value}",
    "formulationSource": "urn:csabs:source/local-lean-StochasticProcesses",
    "formulationLocator": "Catalog.AdaptedProcess",
    "formulationScope": "model",
    "leanModelMapping": "Subtype of StochasticProcess with MeasureTheory.Adapted f X.value, using ordinary measurable adaptedness, not strongly adaptedness as a different general definition.",
    "leanModelLimitations": "No predictable/progressive measurability or path regularity. Equality is pointwise equality of the underlying process for fixed P and f."
  },
  {
    "id": "urn:csabs:operation/AdaptedProcess-observe",
    "type": "Operation",
    "name": "observe",
    "signature": "(t:T) → RandomVariable((Ω,𝓕ₜ,P restricted to 𝓕ₜ),E)",
    "description": "Return Xₜ with its time-local measurability evidence; 𝓕ₜ⊆Σ makes restriction of P well-defined.",
    "concept": "urn:csabs:concept/AdaptedProcess",
    "precondition": "Fix the concept parameters; inputs lie in the signature domains and satisfy its displayed constraints.",
    "postcondition": "Return Xₜ with its time-local measurability evidence; 𝓕ₜ⊆Σ makes restriction of P well-defined.",
    "totality": "total on the stated domain"
  },
  {
    "id": "urn:csabs:axiom/AdaptedProcess-basis",
    "type": "Axiom",
    "name": "basis",
    "statement": "Retain coordinate measurability of StochasticProcess and require Xₜ to be 𝓕ₜ/𝓔-measurable at every t.",
    "formalStatement": "∀t∈T, B∈𝓔: {ω:Xₜ(ω)∈B}∈𝓕ₜ",
    "assumptions": [
      "T is preordered; (Ω,Σ,P) is a probability space; (E,𝓔) is measurable; 𝓕 is a filtration in Σ; X is an E-valued stochastic process on Ω."
    ],
    "appliesTo": [
      "urn:csabs:concept/AdaptedProcess"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "sourced defining constraint; not itself a theorem witness",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/mathlib-pinned-stochastic-adapted"
    ],
    "sourceLocator": "MeasureTheory.Adapted; Adapted.measurable; adapted_const",
    "sourceNote": "Adapted from the consulted pinned source to the explicit catalog carriers and equality conventions.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:theorem/AdaptedProcess-model-satisfaction",
    "type": "Theorem",
    "name": "model-satisfaction",
    "statement": "For any filtration 𝓕 and e∈E, Xₜ(ω)=e is adapted to 𝓕.",
    "formalStatement": "For any filtration 𝓕 and e∈E, Xₜ(ω)=e is adapted to 𝓕.",
    "assumptions": [
      "Supply e∈E; no empty-value-space existence is claimed."
    ],
    "appliesTo": [
      "urn:csabs:concept/AdaptedProcess"
    ],
    "dependsOn": [
      "urn:csabs:axiom/AdaptedProcess-basis"
    ],
    "proofSketch": "Constant coordinates have inverse images ∅ or Ω in each 𝓕ₜ and in Σ. Construct the process and its adaptedness evidence explicitly.",
    "reviewStatus": "constructive Lean witness registered; verification requires a fresh compiler and axiom-audit report",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/mathlib-pinned-stochastic-adapted"
    ],
    "sourceLocator": "MeasureTheory.Adapted; Adapted.measurable; adapted_const",
    "sourceNote": "Constructive model derived from the linked defining constraints and the cited library construction; the local Lean theorem separately checks the stated type.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ (T E : Type) [Preorder T] {Ω : Type} [m : MeasurableSpace Ω] [MeasurableSpace E] (P : Catalog.ProbabilitySpace Ω) (f : Catalog.Filtration T m) (_e : E), Nonempty (Catalog.AdaptedProcess T E P f)",
    "formulationSource": "urn:csabs:source/local-lean-StochasticProcesses",
    "formulationLocator": "Catalog.adaptedProcess_model_satisfaction",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "For any filtration 𝓕 and e∈E, Xₜ(ω)=e is adapted to 𝓕. The Nonempty inhabitant contains the defining constraints as checked proof fields; this witnesses model existence, not all properties of arbitrary processes.",
    "leanModelLimitations": "Constructive model satisfaction for the stated parameters only. No blanket proof of other catalog operations or derived results.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/AdaptedProcess-basis\": \"Satisfied by the concrete construction in the proof: Constant coordinates have inverse images ∅ or Ω in each 𝓕ₜ and in Σ. Construct the process and its adaptedness evidence explicitly.\"}"
  }
]
```
<!-- graph-record:end -->
