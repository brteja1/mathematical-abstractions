# Stochastic process (measurable random family)

A family of measurable random elements on one probability space, indexed by a set T and taking values in a fixed measurable space E. Each coordinate is measurable; no joint time-sample measurability or path regularity is imposed.

**Notation:** (Ω,Σ,P), (E,𝓔); X:T→Ω→E; Xₜ(ω)=X(t,ω)

**Stable ID:** `urn:csabs:concept/StochasticProcess`

**Categories:** Probability and stochastic models → Stochastic processes, Probability and stochastic models, Measure theory

**Kind:** Mathematical structure

**Prerequisites:** [Probability space (normalized measure)](ProbabilitySpace.md), [Random variable (measurable random element)](RandomVariable.md)

**Related concepts:** [Markov chain (finite-state, discrete-time, time-homogeneous)](MarkovChain.md)

## Backlinks

- [Adapted stochastic process](AdaptedProcess.md) — `requiresConcept`
- [Adapted stochastic process](AdaptedProcess.md) — `specializationOf`
- [Markov chain (finite-state, discrete-time, time-homogeneous)](MarkovChain.md) — `specializationOf`

## Mathematical formulation

(Ω,Σ,P), (E,𝓔); X:T→Ω→E; Xₜ(ω)=X(t,ω). For every t∈T, Xₜ:(Ω,Σ)→(E,𝓔) is measurable. The probability-space and measurable-space interfaces are explicit parameters. Arbitrary index set T, including empty T. Standard time choices are ℕ and ℝ≥0. No independence, stationarity, Markov property or continuity is assumed. Equality is pointwise in all supplied arguments; almost-sure equality and equality in distribution are distinct.

**Lean formulation** (in its source module context):

```lean
structure StochasticProcess (T E : Type*) {Ω : Type*}
    [_root_.MeasurableSpace Ω] [_root_.MeasurableSpace E] (_P : ProbabilitySpace Ω) where
  value : T → Ω → E
  measurable : ∀ t, Measurable (value t)
```

**Source:** [`Catalog.StochasticProcess`](../lean/Catalog/StochasticProcesses.lean); consulted 2026-11-20.

**Scope:** model

**Interpretation:** T is an arbitrary index type, Ω carries P, E is measurable; value is the total family and measurable proves every coordinate is measurable. Equality is pointwise via structure equality.

**Limits:** No joint measurability, path regularity, almost-sure quotient, independence or Markov law. Law operations are specified mathematically and not wrapped in this module.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** For every t∈T, Xₜ:(Ω,Σ)→(E,𝓔) is measurable. The probability-space and measurable-space interfaces are explicit parameters.

**basisKind:** defined-structure

**basisScope:** Arbitrary index set T, including empty T. Standard time choices are ℕ and ℝ≥0. No independence, stationarity, Markov property or continuity is assumed.

**verificationObligation:** Use the declared carriers, equality and measurable sigma-algebras. Prerequisites do not automatically transfer claims.; No joint measurability, path regularity, almost-sure quotient, independence or Markov law. Law operations are specified mathematically and not wrapped in this module.

**reviewStatus:** sourced editorial interface; model-satisfaction witness registered separately

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-StochasticProcess-at-time"></a>

### at-time

`urn:csabs:operation/StochasticProcess-at-time`

**signature:** T → RandomVariable(Ω,E)

**description:** t ↦ Xₜ; total for supplied t, with Σ/𝓔 measurability.

**precondition:** Fix the concept parameters; inputs lie in the signature domains and satisfy its displayed constraints.

**postcondition:** t ↦ Xₜ; total for supplied t, with Σ/𝓔 measurability.

**totality:** total on the stated domain

<a id="node-urn-csabs-operation-StochasticProcess-sample-path"></a>

### sample-path

`urn:csabs:operation/StochasticProcess-sample-path`

**signature:** Ω → (T → E)

**description:** ω ↦ (t ↦ Xₜ(ω)); a total path with no continuity or time-measurability promise.

**precondition:** Fix the concept parameters; inputs lie in the signature domains and satisfy its displayed constraints.

**postcondition:** ω ↦ (t ↦ Xₜ(ω)); a total path with no continuity or time-measurability promise.

**totality:** total on the stated domain

<a id="node-urn-csabs-operation-StochasticProcess-finite-dimensional-law"></a>

### finite-dimensional-law

`urn:csabs:operation/StochasticProcess-finite-dimensional-law`

**signature:** List(T) → ProbabilityMeasure(E^length)

**description:** (t₁,…,tₖ) ↦ P∘(ω↦(Xₜ₁(ω),…,Xₜₖ(ω)))⁻¹ on the finite product sigma-algebra. Repeated times allowed; k=0 gives the unique law on the one-point empty product.

**precondition:** Fix the concept parameters; inputs lie in the signature domains and satisfy its displayed constraints.

**postcondition:** (t₁,…,tₖ) ↦ P∘(ω↦(Xₜ₁(ω),…,Xₜₖ(ω)))⁻¹ on the finite product sigma-algebra. Repeated times allowed; k=0 gives the unique law on the one-point empty product.

**totality:** total on the stated domain

## Axioms and defining rules

<a id="node-urn-csabs-axiom-StochasticProcess-basis"></a>

### basis

`urn:csabs:axiom/StochasticProcess-basis`

**statement:** For every t∈T, Xₜ:(Ω,Σ)→(E,𝓔) is measurable. The probability-space and measurable-space interfaces are explicit parameters.

**formalStatement:** ∀t∈T, B∈𝓔: {ω:Xₜ(ω)∈B}∈Σ

**assumptions:** T is an index set; (Ω,Σ,P) is a probability space; (E,𝓔) is a measurable space; X:T→Ω→E.

**ruleRole:** defining-rule

**reviewStatus:** sourced defining constraint; not itself a theorem witness

**notationLanguage:** informal mathematical Unicode

**source:** [Mathlib 4.35.0: Stochastic processes and finite-dimensional laws](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Probability/Process/FiniteDimensionalLaws.lean); citation: Mathlib contributors, mathlib4, revision 56a005855ea17e0b0958f73ec801ae140b0a1679. Consulted installed source; Apache-2.0 license. Definitions adapted, not copied as prose.; path: lean/.lake/packages/mathlib/Mathlib/Probability/Process/FiniteDimensionalLaws.lean; accessedOn: 2026-11-20; sourceRole: primary mathematical definition and formal reference

**sourceLocator:** Module introduction: X : T → Ω → 𝓧, process law and finite-dimensional distributions; isProjectiveMeasureFamily_map_restrict

**sourceNote:** Adapted from the consulted pinned source to the explicit catalog carriers and equality conventions.

**provenanceKind:** adapted

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-StochasticProcess-model-satisfaction"></a>

### model-satisfaction

`urn:csabs:theorem/StochasticProcess-model-satisfaction`

**statement:** For every T and every e∈E, Xₜ(ω)=e is a stochastic process on (Ω,Σ,P).

**formalStatement:** For every T and every e∈E, Xₜ(ω)=e is a stochastic process on (Ω,Σ,P).

**assumptions:** Supply e∈E; no empty-value-space existence is claimed.

**dependsOn:** [basis](StochasticProcess.md#node-urn-csabs-axiom-StochasticProcess-basis)

**proofSketch:** Every inverse image under a constant coordinate is either Ω or ∅, hence measurable. The supplied e covers every time and outcome, including empty T.

**reviewStatus:** constructive Lean witness registered; verification requires a fresh compiler and axiom-audit report

**notationLanguage:** informal mathematical Unicode

**source:** [Mathlib 4.35.0: Stochastic processes and finite-dimensional laws](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Probability/Process/FiniteDimensionalLaws.lean); citation: Mathlib contributors, mathlib4, revision 56a005855ea17e0b0958f73ec801ae140b0a1679. Consulted installed source; Apache-2.0 license. Definitions adapted, not copied as prose.; path: lean/.lake/packages/mathlib/Mathlib/Probability/Process/FiniteDimensionalLaws.lean; accessedOn: 2026-11-20; sourceRole: primary mathematical definition and formal reference

**sourceLocator:** Module introduction: X : T → Ω → 𝓧, process law and finite-dimensional distributions; isProjectiveMeasureFamily_map_restrict

**sourceNote:** Constructive model derived from the linked defining constraints and the cited library construction; the local Lean theorem separately checks the stated type.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ (T E : Type) {Ω : Type} [MeasurableSpace Ω] [MeasurableSpace E] (P : Catalog.ProbabilitySpace Ω) (_e : E), Nonempty (Catalog.StochasticProcess T E P)
```

**Source:** [`Catalog.stochasticProcess_model_satisfaction`](../lean/Catalog/StochasticProcesses.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** For every T and every e∈E, Xₜ(ω)=e is a stochastic process on (Ω,Σ,P). The Nonempty inhabitant contains the defining constraints as checked proof fields; this witnesses model existence, not all properties of arbitrary processes.

**Limits:** Constructive model satisfaction for the stated parameters only. No blanket proof of other catalog operations or derived results.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/StochasticProcess-basis": "Satisfied by the concrete construction in the proof: Every inverse image under a constant coordinate is either Ω or ∅, hence measurable. The supplied e covers every time and outcome, including empty T."
}
```

## Concept provenance

- [Mathlib 4.35.0: Stochastic processes and finite-dimensional laws](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Probability/Process/FiniteDimensionalLaws.lean); citation: Mathlib contributors, mathlib4, revision 56a005855ea17e0b0958f73ec801ae140b0a1679. Consulted installed source; Apache-2.0 license. Definitions adapted, not copied as prose.; path: lean/.lake/packages/mathlib/Mathlib/Probability/Process/FiniteDimensionalLaws.lean; accessedOn: 2026-11-20; sourceRole: primary mathematical definition and formal reference

**sourceLocator:** Module introduction: X : T → Ω → 𝓧, process law and finite-dimensional distributions; isProjectiveMeasureFamily_map_restrict

**sourceNote:** Adapted from the consulted pinned source to the explicit catalog carriers and equality conventions.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/StochasticProcess",
    "type": "Concept",
    "shortForm": "StochasticProcess",
    "fullName": "Stochastic process (measurable random family)",
    "synonyms": [
      "Random process",
      "Measurable stochastic process"
    ],
    "category": [
      "urn:csabs:category/stochastic-processes",
      "urn:csabs:category/probability",
      "urn:csabs:category/measure-theory"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "A family of measurable random elements on one probability space, indexed by a set T and taking values in a fixed measurable space E. Each coordinate is measurable; no joint time-sample measurability or path regularity is imposed.",
    "notation": "(Ω,Σ,P), (E,𝓔); X:T→Ω→E; Xₜ(ω)=X(t,ω)",
    "hasOperation": [
      "urn:csabs:operation/StochasticProcess-at-time",
      "urn:csabs:operation/StochasticProcess-sample-path",
      "urn:csabs:operation/StochasticProcess-finite-dimensional-law"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/StochasticProcess-basis"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/StochasticProcess-model-satisfaction"
    ],
    "axiomBasis": "For every t∈T, Xₜ:(Ω,Σ)→(E,𝓔) is measurable. The probability-space and measurable-space interfaces are explicit parameters.",
    "basisKind": "defined-structure",
    "basisScope": "Arbitrary index set T, including empty T. Standard time choices are ℕ and ℝ≥0. No independence, stationarity, Markov property or continuity is assumed.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "sourced editorial interface; model-satisfaction witness registered separately",
    "requiresConcept": [
      "urn:csabs:concept/ProbabilitySpace",
      "urn:csabs:concept/RandomVariable"
    ],
    "verificationObligation": [
      "Use the declared carriers, equality and measurable sigma-algebras. Prerequisites do not automatically transfer claims.",
      "No joint measurability, path regularity, almost-sure quotient, independence or Markov law. Law operations are specified mathematically and not wrapped in this module."
    ],
    "mathematicalFormulation": "(Ω,Σ,P), (E,𝓔); X:T→Ω→E; Xₜ(ω)=X(t,ω). For every t∈T, Xₜ:(Ω,Σ)→(E,𝓔) is measurable. The probability-space and measurable-space interfaces are explicit parameters. Arbitrary index set T, including empty T. Standard time choices are ℕ and ℝ≥0. No independence, stationarity, Markov property or continuity is assumed. Equality is pointwise in all supplied arguments; almost-sure equality and equality in distribution are distinct.",
    "source": [
      "urn:csabs:source/mathlib-pinned-stochastic-process"
    ],
    "sourceLocator": "Module introduction: X : T → Ω → 𝓧, process law and finite-dimensional distributions; isProjectiveMeasureFamily_map_restrict",
    "sourceNote": "Adapted from the consulted pinned source to the explicit catalog carriers and equality conventions.",
    "provenanceKind": "adapted",
    "relatedConcept": [
      "urn:csabs:concept/MarkovChain"
    ],
    "leanFormulation": "structure StochasticProcess (T E : Type*) {Ω : Type*}\n    [_root_.MeasurableSpace Ω] [_root_.MeasurableSpace E] (_P : ProbabilitySpace Ω) where\n  value : T → Ω → E\n  measurable : ∀ t, Measurable (value t)",
    "formulationSource": "urn:csabs:source/local-lean-StochasticProcesses",
    "formulationLocator": "Catalog.StochasticProcess",
    "formulationScope": "model",
    "leanModelMapping": "T is an arbitrary index type, Ω carries P, E is measurable; value is the total family and measurable proves every coordinate is measurable. Equality is pointwise via structure equality.",
    "leanModelLimitations": "No joint measurability, path regularity, almost-sure quotient, independence or Markov law. Law operations are specified mathematically and not wrapped in this module."
  },
  {
    "id": "urn:csabs:operation/StochasticProcess-at-time",
    "type": "Operation",
    "name": "at-time",
    "signature": "T → RandomVariable(Ω,E)",
    "description": "t ↦ Xₜ; total for supplied t, with Σ/𝓔 measurability.",
    "concept": "urn:csabs:concept/StochasticProcess",
    "precondition": "Fix the concept parameters; inputs lie in the signature domains and satisfy its displayed constraints.",
    "postcondition": "t ↦ Xₜ; total for supplied t, with Σ/𝓔 measurability.",
    "totality": "total on the stated domain"
  },
  {
    "id": "urn:csabs:operation/StochasticProcess-sample-path",
    "type": "Operation",
    "name": "sample-path",
    "signature": "Ω → (T → E)",
    "description": "ω ↦ (t ↦ Xₜ(ω)); a total path with no continuity or time-measurability promise.",
    "concept": "urn:csabs:concept/StochasticProcess",
    "precondition": "Fix the concept parameters; inputs lie in the signature domains and satisfy its displayed constraints.",
    "postcondition": "ω ↦ (t ↦ Xₜ(ω)); a total path with no continuity or time-measurability promise.",
    "totality": "total on the stated domain"
  },
  {
    "id": "urn:csabs:operation/StochasticProcess-finite-dimensional-law",
    "type": "Operation",
    "name": "finite-dimensional-law",
    "signature": "List(T) → ProbabilityMeasure(E^length)",
    "description": "(t₁,…,tₖ) ↦ P∘(ω↦(Xₜ₁(ω),…,Xₜₖ(ω)))⁻¹ on the finite product sigma-algebra. Repeated times allowed; k=0 gives the unique law on the one-point empty product.",
    "concept": "urn:csabs:concept/StochasticProcess",
    "precondition": "Fix the concept parameters; inputs lie in the signature domains and satisfy its displayed constraints.",
    "postcondition": "(t₁,…,tₖ) ↦ P∘(ω↦(Xₜ₁(ω),…,Xₜₖ(ω)))⁻¹ on the finite product sigma-algebra. Repeated times allowed; k=0 gives the unique law on the one-point empty product.",
    "totality": "total on the stated domain"
  },
  {
    "id": "urn:csabs:axiom/StochasticProcess-basis",
    "type": "Axiom",
    "name": "basis",
    "statement": "For every t∈T, Xₜ:(Ω,Σ)→(E,𝓔) is measurable. The probability-space and measurable-space interfaces are explicit parameters.",
    "formalStatement": "∀t∈T, B∈𝓔: {ω:Xₜ(ω)∈B}∈Σ",
    "assumptions": [
      "T is an index set; (Ω,Σ,P) is a probability space; (E,𝓔) is a measurable space; X:T→Ω→E."
    ],
    "appliesTo": [
      "urn:csabs:concept/StochasticProcess"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "sourced defining constraint; not itself a theorem witness",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/mathlib-pinned-stochastic-process"
    ],
    "sourceLocator": "Module introduction: X : T → Ω → 𝓧, process law and finite-dimensional distributions; isProjectiveMeasureFamily_map_restrict",
    "sourceNote": "Adapted from the consulted pinned source to the explicit catalog carriers and equality conventions.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:theorem/StochasticProcess-model-satisfaction",
    "type": "Theorem",
    "name": "model-satisfaction",
    "statement": "For every T and every e∈E, Xₜ(ω)=e is a stochastic process on (Ω,Σ,P).",
    "formalStatement": "For every T and every e∈E, Xₜ(ω)=e is a stochastic process on (Ω,Σ,P).",
    "assumptions": [
      "Supply e∈E; no empty-value-space existence is claimed."
    ],
    "appliesTo": [
      "urn:csabs:concept/StochasticProcess"
    ],
    "dependsOn": [
      "urn:csabs:axiom/StochasticProcess-basis"
    ],
    "proofSketch": "Every inverse image under a constant coordinate is either Ω or ∅, hence measurable. The supplied e covers every time and outcome, including empty T.",
    "reviewStatus": "constructive Lean witness registered; verification requires a fresh compiler and axiom-audit report",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/mathlib-pinned-stochastic-process"
    ],
    "sourceLocator": "Module introduction: X : T → Ω → 𝓧, process law and finite-dimensional distributions; isProjectiveMeasureFamily_map_restrict",
    "sourceNote": "Constructive model derived from the linked defining constraints and the cited library construction; the local Lean theorem separately checks the stated type.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ (T E : Type) {Ω : Type} [MeasurableSpace Ω] [MeasurableSpace E] (P : Catalog.ProbabilitySpace Ω) (_e : E), Nonempty (Catalog.StochasticProcess T E P)",
    "formulationSource": "urn:csabs:source/local-lean-StochasticProcesses",
    "formulationLocator": "Catalog.stochasticProcess_model_satisfaction",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "For every T and every e∈E, Xₜ(ω)=e is a stochastic process on (Ω,Σ,P). The Nonempty inhabitant contains the defining constraints as checked proof fields; this witnesses model existence, not all properties of arbitrary processes.",
    "leanModelLimitations": "Constructive model satisfaction for the stated parameters only. No blanket proof of other catalog operations or derived results.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/StochasticProcess-basis\": \"Satisfied by the concrete construction in the proof: Every inverse image under a constant coordinate is either Ω or ∅, hence measurable. The supplied e covers every time and outcome, including empty T.\"}"
  }
]
```
<!-- graph-record:end -->
