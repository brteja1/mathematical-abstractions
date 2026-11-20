# Martingale (discrete-time real-valued)

A real-valued adapted process on a probability space, integrable at every integer time, whose conditional mean at any later time given present information equals its present value almost surely.

**Notation:** X:ℕ→Ω→ℝ; E[|Xₙ|]<∞; E[Xₘ | 𝓕ₙ]=Xₙ P-a.s. for n≤m

**Stable ID:** `urn:csabs:concept/Martingale`

**Categories:** Probability and stochastic models → Stochastic processes, Probability and stochastic models, Measure theory

**Kind:** Mathematical structure

**Prerequisites:** [Adapted stochastic process](AdaptedProcess.md), [Probability space (normalized measure)](ProbabilitySpace.md), [Exact real number](RealNumber.md)

**Specializes:** [Adapted stochastic process](AdaptedProcess.md)

## Mathematical formulation

X:ℕ→Ω→ℝ; E[|Xₙ|]<∞; E[Xₘ | 𝓕ₙ]=Xₙ P-a.s. for n≤m. For every n, Xₙ is 𝓕ₙ-measurable and P-integrable; for all n≤m, E[Xₘ | 𝓕ₙ]=Xₙ almost surely. Real values with Borel sigma-algebra; integer times n≥0; a fixed probability space and filtration. No independent increments, boundedness, convergence or optional-stopping assumptions. Equality is pointwise in all supplied arguments; almost-sure equality and equality in distribution are distinct.

**Lean formulation** (in its source module context):

```lean
abbrev Martingale {Ω : Type*} [m : _root_.MeasurableSpace Ω]
    (P : ProbabilitySpace Ω) (f : Filtration ℕ m) :=
  {X : StochasticProcess ℕ ℝ P // MeasureTheory.Martingale X.value f P.val}
```

**Source:** [`Catalog.Martingale`](../lean/Catalog/StochasticProcesses.lean); consulted 2026-11-20.

**Scope:** model

**Interpretation:** Subtype of real StochasticProcess on ℕ satisfying MeasureTheory.Martingale. For real Borel values, strongly measurable adaptedness agrees with measurable adaptedness; the diagonal conditional-mean identity implies integrability via Martingale.integrable.

**Limits:** Conditional-mean equality is almost sure at each pair of times; process representatives still have pointwise equality. No convergence, optional-stopping or representation theorem is registered.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** For every n, Xₙ is 𝓕ₙ-measurable and P-integrable; for all n≤m, E[Xₘ | 𝓕ₙ]=Xₙ almost surely.

**basisKind:** defined-structure

**basisScope:** Real values with Borel sigma-algebra; integer times n≥0; a fixed probability space and filtration. No independent increments, boundedness, convergence or optional-stopping assumptions.

**basisInstantiation:** For every n, Xₙ is 𝓕ₙ-measurable and P-integrable; for all n≤m, E[Xₘ | 𝓕ₙ]=Xₙ almost surely.

**specializationNote:** Instantiate AdaptedProcess at T=ℕ, E=ℝ with Borel sigma-algebra, keeping Ω, P and 𝓕. Add coordinate integrability and the conditional-mean identity.

**verificationObligation:** Use the declared carriers, equality and measurable sigma-algebras. Prerequisites do not automatically transfer claims.; Conditional-mean equality is almost sure at each pair of times; process representatives still have pointwise equality. No convergence, optional-stopping or representation theorem is registered.

**reviewStatus:** sourced editorial interface; model-satisfaction witness registered separately

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-Martingale-at-time"></a>

### at-time

`urn:csabs:operation/Martingale-at-time`

**signature:** (n:ℕ) → {Y:Ω→ℝ | Y is 𝓕ₙ-measurable and P-integrable}

**description:** Return the integrable coordinate Xₙ, retaining its 𝓕ₙ-measurability. Process equality remains pointwise.

**precondition:** Fix the concept parameters; inputs lie in the signature domains and satisfy its displayed constraints.

**postcondition:** Return the integrable coordinate Xₙ, retaining its 𝓕ₙ-measurability. Process equality remains pointwise.

**totality:** total on ℕ; returns the chosen coordinate function with pointwise equality

<a id="node-urn-csabs-operation-Martingale-conditional-mean"></a>

### conditional-mean

`urn:csabs:operation/Martingale-conditional-mean`

**signature:** {(n,m)∈ℕ² | n≤m} → L¹(Ω,𝓕ₙ,P;ℝ)

**description:** Return the almost-sure class of E[Xₘ|𝓕ₙ], which equals the class of Xₙ. Characterization: ∫_A E[Xₘ|𝓕ₙ]dP=∫_A XₘdP for every A∈𝓕ₙ; defined up to P-null sets, not by division by an event probability.

**precondition:** Fix the concept parameters; inputs lie in the signature domains and satisfy its displayed constraints.

**postcondition:** Return the almost-sure class of E[Xₘ|𝓕ₙ], which equals the class of Xₙ. Characterization: ∫_A E[Xₘ|𝓕ₙ]dP=∫_A XₘdP for every A∈𝓕ₙ; defined up to P-null sets, not by division by an event probability.

**totality:** total on the stated domain; L¹ outputs are almost-sure equivalence classes

## Axioms and defining rules

<a id="node-urn-csabs-axiom-Martingale-basis"></a>

### basis

`urn:csabs:axiom/Martingale-basis`

**statement:** For every n, Xₙ is 𝓕ₙ-measurable and P-integrable; for all n≤m, E[Xₘ | 𝓕ₙ]=Xₙ almost surely.

**formalStatement:** ∀n: Xₙ is 𝓕ₙ-measurable ∧ ∫|Xₙ|dP<∞; ∀n≤m: E[Xₘ|𝓕ₙ]=Xₙ P-a.s.

**assumptions:** (Ω,Σ,P) is a probability space; 𝓕 is an ℕ-indexed filtration in Σ; X:ℕ→Ω→ℝ with real Borel values.

**ruleRole:** defining-rule

**reviewStatus:** sourced defining constraint; not itself a theorem witness

**notationLanguage:** informal mathematical Unicode

**source:** [Mathlib 4.35.0: Martingales](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Probability/Martingale/Basic.lean); citation: Mathlib contributors, mathlib4, revision 56a005855ea17e0b0958f73ec801ae140b0a1679. Consulted installed source; Apache-2.0 license. Definitions adapted, not copied as prose.; path: lean/.lake/packages/mathlib/Mathlib/Probability/Martingale/Basic.lean; accessedOn: 2026-11-20; sourceRole: primary mathematical definition and formal reference

**sourceLocator:** MeasureTheory.Martingale; Martingale.integrable; martingale_const; Martingale.condExp_ae_eq

**sourceNote:** Adapted from the consulted pinned source to the explicit catalog carriers and equality conventions.

**provenanceKind:** adapted

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-Martingale-model-satisfaction"></a>

### model-satisfaction

`urn:csabs:theorem/Martingale-model-satisfaction`

**statement:** For every probability space, filtration 𝓕 and c∈ℝ, Xₙ(ω)=c is an integrable real martingale.

**formalStatement:** For every probability space, filtration 𝓕 and c∈ℝ, Xₙ(ω)=c is an integrable real martingale.

**assumptions:** Use the parameters and semantic conventions in the concept definition.

**dependsOn:** [basis](Martingale.md#node-urn-csabs-axiom-Martingale-basis)

**proofSketch:** Constant real coordinates are measurable and integrable because P is finite, and conditional expectation preserves constants. Use the supplied probability measure and martingale_const to construct the subtype; no target law is assumed.

**reviewStatus:** constructive Lean witness registered; verification requires a fresh compiler and axiom-audit report

**notationLanguage:** informal mathematical Unicode

**source:** [Mathlib 4.35.0: Martingales](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Probability/Martingale/Basic.lean); citation: Mathlib contributors, mathlib4, revision 56a005855ea17e0b0958f73ec801ae140b0a1679. Consulted installed source; Apache-2.0 license. Definitions adapted, not copied as prose.; path: lean/.lake/packages/mathlib/Mathlib/Probability/Martingale/Basic.lean; accessedOn: 2026-11-20; sourceRole: primary mathematical definition and formal reference

**sourceLocator:** MeasureTheory.Martingale; Martingale.integrable; martingale_const; Martingale.condExp_ae_eq

**sourceNote:** Constructive model derived from the linked defining constraints and the cited library construction; the local Lean theorem separately checks the stated type.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {Ω : Type} [m : MeasurableSpace Ω] (P : Catalog.ProbabilitySpace Ω) (f : Catalog.Filtration ℕ m) (_c : ℝ), Nonempty (Catalog.Martingale P f)
```

**Source:** [`Catalog.martingale_model_satisfaction`](../lean/Catalog/StochasticProcesses.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** For every probability space, filtration 𝓕 and c∈ℝ, Xₙ(ω)=c is an integrable real martingale. The Nonempty inhabitant contains the defining constraints as checked proof fields; this witnesses model existence, not all properties of arbitrary processes.

**Limits:** Constructive model satisfaction for the stated parameters only. No blanket proof of other catalog operations or derived results.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/Martingale-basis": "Satisfied by the concrete construction in the proof: Constant real coordinates are measurable and integrable because P is finite, and conditional expectation preserves constants. Use the supplied probability measure and martingale_const to construct the subtype; no target law is assumed."
}
```

## Concept provenance

- [Mathlib 4.35.0: Martingales](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Probability/Martingale/Basic.lean); citation: Mathlib contributors, mathlib4, revision 56a005855ea17e0b0958f73ec801ae140b0a1679. Consulted installed source; Apache-2.0 license. Definitions adapted, not copied as prose.; path: lean/.lake/packages/mathlib/Mathlib/Probability/Martingale/Basic.lean; accessedOn: 2026-11-20; sourceRole: primary mathematical definition and formal reference

**sourceLocator:** MeasureTheory.Martingale; Martingale.integrable; martingale_const; Martingale.condExp_ae_eq

**sourceNote:** Adapted from the consulted pinned source to the explicit catalog carriers and equality conventions.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/Martingale",
    "type": "Concept",
    "shortForm": "Martingale",
    "fullName": "Martingale (discrete-time real-valued)",
    "synonyms": [
      "Integrable real discrete-time martingale",
      "Fair-game process (real discrete time)"
    ],
    "category": [
      "urn:csabs:category/stochastic-processes",
      "urn:csabs:category/probability",
      "urn:csabs:category/measure-theory"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "A real-valued adapted process on a probability space, integrable at every integer time, whose conditional mean at any later time given present information equals its present value almost surely.",
    "notation": "X:ℕ→Ω→ℝ; E[|Xₙ|]<∞; E[Xₘ | 𝓕ₙ]=Xₙ P-a.s. for n≤m",
    "hasOperation": [
      "urn:csabs:operation/Martingale-at-time",
      "urn:csabs:operation/Martingale-conditional-mean"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/Martingale-basis"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/Martingale-model-satisfaction"
    ],
    "axiomBasis": "For every n, Xₙ is 𝓕ₙ-measurable and P-integrable; for all n≤m, E[Xₘ | 𝓕ₙ]=Xₙ almost surely.",
    "basisKind": "defined-structure",
    "basisScope": "Real values with Borel sigma-algebra; integer times n≥0; a fixed probability space and filtration. No independent increments, boundedness, convergence or optional-stopping assumptions.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "sourced editorial interface; model-satisfaction witness registered separately",
    "requiresConcept": [
      "urn:csabs:concept/AdaptedProcess",
      "urn:csabs:concept/ProbabilitySpace",
      "urn:csabs:concept/RealNumber"
    ],
    "verificationObligation": [
      "Use the declared carriers, equality and measurable sigma-algebras. Prerequisites do not automatically transfer claims.",
      "Conditional-mean equality is almost sure at each pair of times; process representatives still have pointwise equality. No convergence, optional-stopping or representation theorem is registered."
    ],
    "mathematicalFormulation": "X:ℕ→Ω→ℝ; E[|Xₙ|]<∞; E[Xₘ | 𝓕ₙ]=Xₙ P-a.s. for n≤m. For every n, Xₙ is 𝓕ₙ-measurable and P-integrable; for all n≤m, E[Xₘ | 𝓕ₙ]=Xₙ almost surely. Real values with Borel sigma-algebra; integer times n≥0; a fixed probability space and filtration. No independent increments, boundedness, convergence or optional-stopping assumptions. Equality is pointwise in all supplied arguments; almost-sure equality and equality in distribution are distinct.",
    "source": [
      "urn:csabs:source/mathlib-pinned-stochastic-martingale"
    ],
    "sourceLocator": "MeasureTheory.Martingale; Martingale.integrable; martingale_const; Martingale.condExp_ae_eq",
    "sourceNote": "Adapted from the consulted pinned source to the explicit catalog carriers and equality conventions.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/AdaptedProcess"
    ],
    "specializationNote": "Instantiate AdaptedProcess at T=ℕ, E=ℝ with Borel sigma-algebra, keeping Ω, P and 𝓕. Add coordinate integrability and the conditional-mean identity.",
    "basisInstantiation": "For every n, Xₙ is 𝓕ₙ-measurable and P-integrable; for all n≤m, E[Xₘ | 𝓕ₙ]=Xₙ almost surely.",
    "leanFormulation": "abbrev Martingale {Ω : Type*} [m : _root_.MeasurableSpace Ω]\n    (P : ProbabilitySpace Ω) (f : Filtration ℕ m) :=\n  {X : StochasticProcess ℕ ℝ P // MeasureTheory.Martingale X.value f P.val}",
    "formulationSource": "urn:csabs:source/local-lean-StochasticProcesses",
    "formulationLocator": "Catalog.Martingale",
    "formulationScope": "model",
    "leanModelMapping": "Subtype of real StochasticProcess on ℕ satisfying MeasureTheory.Martingale. For real Borel values, strongly measurable adaptedness agrees with measurable adaptedness; the diagonal conditional-mean identity implies integrability via Martingale.integrable.",
    "leanModelLimitations": "Conditional-mean equality is almost sure at each pair of times; process representatives still have pointwise equality. No convergence, optional-stopping or representation theorem is registered."
  },
  {
    "id": "urn:csabs:operation/Martingale-at-time",
    "type": "Operation",
    "name": "at-time",
    "signature": "(n:ℕ) → {Y:Ω→ℝ | Y is 𝓕ₙ-measurable and P-integrable}",
    "description": "Return the integrable coordinate Xₙ, retaining its 𝓕ₙ-measurability. Process equality remains pointwise.",
    "concept": "urn:csabs:concept/Martingale",
    "precondition": "Fix the concept parameters; inputs lie in the signature domains and satisfy its displayed constraints.",
    "postcondition": "Return the integrable coordinate Xₙ, retaining its 𝓕ₙ-measurability. Process equality remains pointwise.",
    "totality": "total on ℕ; returns the chosen coordinate function with pointwise equality"
  },
  {
    "id": "urn:csabs:operation/Martingale-conditional-mean",
    "type": "Operation",
    "name": "conditional-mean",
    "signature": "{(n,m)∈ℕ² | n≤m} → L¹(Ω,𝓕ₙ,P;ℝ)",
    "description": "Return the almost-sure class of E[Xₘ|𝓕ₙ], which equals the class of Xₙ. Characterization: ∫_A E[Xₘ|𝓕ₙ]dP=∫_A XₘdP for every A∈𝓕ₙ; defined up to P-null sets, not by division by an event probability.",
    "concept": "urn:csabs:concept/Martingale",
    "precondition": "Fix the concept parameters; inputs lie in the signature domains and satisfy its displayed constraints.",
    "postcondition": "Return the almost-sure class of E[Xₘ|𝓕ₙ], which equals the class of Xₙ. Characterization: ∫_A E[Xₘ|𝓕ₙ]dP=∫_A XₘdP for every A∈𝓕ₙ; defined up to P-null sets, not by division by an event probability.",
    "totality": "total on the stated domain; L¹ outputs are almost-sure equivalence classes"
  },
  {
    "id": "urn:csabs:axiom/Martingale-basis",
    "type": "Axiom",
    "name": "basis",
    "statement": "For every n, Xₙ is 𝓕ₙ-measurable and P-integrable; for all n≤m, E[Xₘ | 𝓕ₙ]=Xₙ almost surely.",
    "formalStatement": "∀n: Xₙ is 𝓕ₙ-measurable ∧ ∫|Xₙ|dP<∞; ∀n≤m: E[Xₘ|𝓕ₙ]=Xₙ P-a.s.",
    "assumptions": [
      "(Ω,Σ,P) is a probability space; 𝓕 is an ℕ-indexed filtration in Σ; X:ℕ→Ω→ℝ with real Borel values."
    ],
    "appliesTo": [
      "urn:csabs:concept/Martingale"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "sourced defining constraint; not itself a theorem witness",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/mathlib-pinned-stochastic-martingale"
    ],
    "sourceLocator": "MeasureTheory.Martingale; Martingale.integrable; martingale_const; Martingale.condExp_ae_eq",
    "sourceNote": "Adapted from the consulted pinned source to the explicit catalog carriers and equality conventions.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:theorem/Martingale-model-satisfaction",
    "type": "Theorem",
    "name": "model-satisfaction",
    "statement": "For every probability space, filtration 𝓕 and c∈ℝ, Xₙ(ω)=c is an integrable real martingale.",
    "formalStatement": "For every probability space, filtration 𝓕 and c∈ℝ, Xₙ(ω)=c is an integrable real martingale.",
    "assumptions": [
      "Use the parameters and semantic conventions in the concept definition."
    ],
    "appliesTo": [
      "urn:csabs:concept/Martingale"
    ],
    "dependsOn": [
      "urn:csabs:axiom/Martingale-basis"
    ],
    "proofSketch": "Constant real coordinates are measurable and integrable because P is finite, and conditional expectation preserves constants. Use the supplied probability measure and martingale_const to construct the subtype; no target law is assumed.",
    "reviewStatus": "constructive Lean witness registered; verification requires a fresh compiler and axiom-audit report",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/mathlib-pinned-stochastic-martingale"
    ],
    "sourceLocator": "MeasureTheory.Martingale; Martingale.integrable; martingale_const; Martingale.condExp_ae_eq",
    "sourceNote": "Constructive model derived from the linked defining constraints and the cited library construction; the local Lean theorem separately checks the stated type.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {Ω : Type} [m : MeasurableSpace Ω] (P : Catalog.ProbabilitySpace Ω) (f : Catalog.Filtration ℕ m) (_c : ℝ), Nonempty (Catalog.Martingale P f)",
    "formulationSource": "urn:csabs:source/local-lean-StochasticProcesses",
    "formulationLocator": "Catalog.martingale_model_satisfaction",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "For every probability space, filtration 𝓕 and c∈ℝ, Xₙ(ω)=c is an integrable real martingale. The Nonempty inhabitant contains the defining constraints as checked proof fields; this witnesses model existence, not all properties of arbitrary processes.",
    "leanModelLimitations": "Constructive model satisfaction for the stated parameters only. No blanket proof of other catalog operations or derived results.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/Martingale-basis\": \"Satisfied by the concrete construction in the proof: Constant real coordinates are measurable and integrable because P is finite, and conditional expectation preserves constants. Use the supplied probability measure and martingale_const to construct the subtype; no target law is assumed.\"}"
  }
]
```
<!-- graph-record:end -->
