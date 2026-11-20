# Filtration (increasing sub-sigma-algebras)

An increasing family of sub-sigma-algebras of a fixed ambient measurable space, indexed by a preordered time set; it records which events are observable by each time.

**Notation:** (Ω,Σ); (T,≤); (𝓕ₜ)ₜ∈T, 𝓕ₜ⊆Σ

**Stable ID:** `urn:csabs:concept/Filtration`

**Categories:** Probability and stochastic models → Stochastic processes, Probability and stochastic models, Measure theory

**Kind:** Mathematical structure

**Prerequisites:** [Measurable space (sigma-algebra on a carrier)](MeasurableSpace.md), [Preorder](Preorder.md)

## Backlinks

- [Adapted stochastic process](AdaptedProcess.md) — `requiresConcept`
- [Stopping time (discrete time, possibly infinite)](StoppingTime.md) — `requiresConcept`

## Mathematical formulation

(Ω,Σ); (T,≤); (𝓕ₜ)ₜ∈T, 𝓕ₜ⊆Σ. Each 𝓕ₜ is a sigma-algebra on Ω contained in Σ, and s≤t implies 𝓕ₛ⊆𝓕ₜ. Preordered time, including empty time; no probability measure is needed to define a filtration. Completeness and right-continuity are additional conditions, not assumed. Equality is equality of the sub-sigma-algebra at every time.

**Lean formulation** (in its source module context):

```lean
abbrev Filtration (T : Type*) [Preorder T] {Ω : Type*}
    (m : _root_.MeasurableSpace Ω) := MeasureTheory.Filtration T m
```

**Source:** [`Catalog.Filtration`](../lean/Catalog/StochasticProcesses.lean); consulted 2026-11-20.

**Scope:** model

**Interpretation:** MeasureTheory.Filtration T m stores sigma-algebras, monotonicity and ambient containment; T has a Preorder. Equality is equality of all time slices.

**Limits:** No completeness, right-continuity, natural-filtration construction or measure supplied by this wrapper.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Each 𝓕ₜ is a sigma-algebra on Ω contained in Σ, and s≤t implies 𝓕ₛ⊆𝓕ₜ.

**basisKind:** defined-structure

**basisScope:** Preordered time, including empty time; no probability measure is needed to define a filtration. Completeness and right-continuity are additional conditions, not assumed.

**verificationObligation:** Use the declared carriers, equality and measurable sigma-algebras. Prerequisites do not automatically transfer claims.; No completeness, right-continuity, natural-filtration construction or measure supplied by this wrapper.

**reviewStatus:** sourced editorial interface; model-satisfaction witness registered separately

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-Filtration-at-time"></a>

### at-time

`urn:csabs:operation/Filtration-at-time`

**signature:** T → SigmaAlgebra(Ω)

**description:** Return the sub-sigma-algebra 𝓕ₜ; total for each t∈T.

**precondition:** Fix the concept parameters; inputs lie in the signature domains and satisfy its displayed constraints.

**postcondition:** Return the sub-sigma-algebra 𝓕ₜ; total for each t∈T.

**totality:** total on the stated domain

<a id="node-urn-csabs-operation-Filtration-constant"></a>

### constant

`urn:csabs:operation/Filtration-constant`

**signature:** {𝓖:SigmaAlgebra(Ω) | 𝓖⊆Σ} → Filtration(T,Σ)

**description:** Return 𝓕ₜ=𝓖 for every t. The containment check is a precondition.

**precondition:** Fix the concept parameters; inputs lie in the signature domains and satisfy its displayed constraints.

**postcondition:** Return 𝓕ₜ=𝓖 for every t. The containment check is a precondition.

**totality:** total on the stated domain

## Axioms and defining rules

<a id="node-urn-csabs-axiom-Filtration-basis"></a>

### basis

`urn:csabs:axiom/Filtration-basis`

**statement:** Each 𝓕ₜ is a sigma-algebra on Ω contained in Σ, and s≤t implies 𝓕ₛ⊆𝓕ₜ.

**formalStatement:** ∀t: 𝓕ₜ is a sigma-algebra on Ω ∧ 𝓕ₜ⊆Σ; ∀s≤t:𝓕ₛ⊆𝓕ₜ

**assumptions:** T is preordered; (Ω,Σ) is an ambient measurable space; 𝓕:T→SigmaAlgebra(Ω).

**ruleRole:** defining-rule

**reviewStatus:** sourced defining constraint; not itself a theorem witness

**notationLanguage:** informal mathematical Unicode

**source:** [Mathlib 4.35.0: Filtrations](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Probability/Process/Filtration.lean); citation: Mathlib contributors, mathlib4, revision 56a005855ea17e0b0958f73ec801ae140b0a1679. Consulted installed source; Apache-2.0 license. Definitions adapted, not copied as prose.; path: lean/.lake/packages/mathlib/Mathlib/Probability/Process/Filtration.lean; accessedOn: 2026-11-20; sourceRole: primary mathematical definition and formal reference

**sourceLocator:** MeasureTheory.Filtration; Filtration.mono; Filtration.le; Filtration.const

**sourceNote:** Adapted from the consulted pinned source to the explicit catalog carriers and equality conventions.

**provenanceKind:** adapted

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-Filtration-model-satisfaction"></a>

### model-satisfaction

`urn:csabs:theorem/Filtration-model-satisfaction`

**statement:** For every preordered T and measurable (Ω,Σ), 𝓕ₜ=Σ is a filtration.

**formalStatement:** For every preordered T and measurable (Ω,Σ), 𝓕ₜ=Σ is a filtration.

**assumptions:** Use the parameters and semantic conventions in the concept definition.

**dependsOn:** [basis](Filtration.md#node-urn-csabs-axiom-Filtration-basis)

**proofSketch:** Use the ambient sigma-algebra at each time. Containment and monotonicity are reflexivity, and each slice is already a sigma-algebra.

**reviewStatus:** constructive Lean witness registered; verification requires a fresh compiler and axiom-audit report

**notationLanguage:** informal mathematical Unicode

**source:** [Mathlib 4.35.0: Filtrations](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Probability/Process/Filtration.lean); citation: Mathlib contributors, mathlib4, revision 56a005855ea17e0b0958f73ec801ae140b0a1679. Consulted installed source; Apache-2.0 license. Definitions adapted, not copied as prose.; path: lean/.lake/packages/mathlib/Mathlib/Probability/Process/Filtration.lean; accessedOn: 2026-11-20; sourceRole: primary mathematical definition and formal reference

**sourceLocator:** MeasureTheory.Filtration; Filtration.mono; Filtration.le; Filtration.const

**sourceNote:** Constructive model derived from the linked defining constraints and the cited library construction; the local Lean theorem separately checks the stated type.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ (T : Type) [Preorder T] {Ω : Type} (m : MeasurableSpace Ω), Nonempty (Catalog.Filtration T m)
```

**Source:** [`Catalog.filtration_model_satisfaction`](../lean/Catalog/StochasticProcesses.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** For every preordered T and measurable (Ω,Σ), 𝓕ₜ=Σ is a filtration. The Nonempty inhabitant contains the defining constraints as checked proof fields; this witnesses model existence, not all properties of arbitrary processes.

**Limits:** Constructive model satisfaction for the stated parameters only. No blanket proof of other catalog operations or derived results.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/Filtration-basis": "Satisfied by the concrete construction in the proof: Use the ambient sigma-algebra at each time. Containment and monotonicity are reflexivity, and each slice is already a sigma-algebra."
}
```

## Concept provenance

- [Mathlib 4.35.0: Filtrations](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Probability/Process/Filtration.lean); citation: Mathlib contributors, mathlib4, revision 56a005855ea17e0b0958f73ec801ae140b0a1679. Consulted installed source; Apache-2.0 license. Definitions adapted, not copied as prose.; path: lean/.lake/packages/mathlib/Mathlib/Probability/Process/Filtration.lean; accessedOn: 2026-11-20; sourceRole: primary mathematical definition and formal reference

**sourceLocator:** MeasureTheory.Filtration; Filtration.mono; Filtration.le; Filtration.const

**sourceNote:** Adapted from the consulted pinned source to the explicit catalog carriers and equality conventions.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/Filtration",
    "type": "Concept",
    "shortForm": "Filtration",
    "fullName": "Filtration (increasing sub-sigma-algebras)",
    "synonyms": [
      "Information filtration",
      "Increasing family of sub-sigma-algebras"
    ],
    "category": [
      "urn:csabs:category/stochastic-processes",
      "urn:csabs:category/probability",
      "urn:csabs:category/measure-theory"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "An increasing family of sub-sigma-algebras of a fixed ambient measurable space, indexed by a preordered time set; it records which events are observable by each time.",
    "notation": "(Ω,Σ); (T,≤); (𝓕ₜ)ₜ∈T, 𝓕ₜ⊆Σ",
    "hasOperation": [
      "urn:csabs:operation/Filtration-at-time",
      "urn:csabs:operation/Filtration-constant"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/Filtration-basis"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/Filtration-model-satisfaction"
    ],
    "axiomBasis": "Each 𝓕ₜ is a sigma-algebra on Ω contained in Σ, and s≤t implies 𝓕ₛ⊆𝓕ₜ.",
    "basisKind": "defined-structure",
    "basisScope": "Preordered time, including empty time; no probability measure is needed to define a filtration. Completeness and right-continuity are additional conditions, not assumed.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "sourced editorial interface; model-satisfaction witness registered separately",
    "requiresConcept": [
      "urn:csabs:concept/MeasurableSpace",
      "urn:csabs:concept/Preorder"
    ],
    "verificationObligation": [
      "Use the declared carriers, equality and measurable sigma-algebras. Prerequisites do not automatically transfer claims.",
      "No completeness, right-continuity, natural-filtration construction or measure supplied by this wrapper."
    ],
    "mathematicalFormulation": "(Ω,Σ); (T,≤); (𝓕ₜ)ₜ∈T, 𝓕ₜ⊆Σ. Each 𝓕ₜ is a sigma-algebra on Ω contained in Σ, and s≤t implies 𝓕ₛ⊆𝓕ₜ. Preordered time, including empty time; no probability measure is needed to define a filtration. Completeness and right-continuity are additional conditions, not assumed. Equality is equality of the sub-sigma-algebra at every time.",
    "source": [
      "urn:csabs:source/mathlib-pinned-stochastic-filtration"
    ],
    "sourceLocator": "MeasureTheory.Filtration; Filtration.mono; Filtration.le; Filtration.const",
    "sourceNote": "Adapted from the consulted pinned source to the explicit catalog carriers and equality conventions.",
    "provenanceKind": "adapted",
    "leanFormulation": "abbrev Filtration (T : Type*) [Preorder T] {Ω : Type*}\n    (m : _root_.MeasurableSpace Ω) := MeasureTheory.Filtration T m",
    "formulationSource": "urn:csabs:source/local-lean-StochasticProcesses",
    "formulationLocator": "Catalog.Filtration",
    "formulationScope": "model",
    "leanModelMapping": "MeasureTheory.Filtration T m stores sigma-algebras, monotonicity and ambient containment; T has a Preorder. Equality is equality of all time slices.",
    "leanModelLimitations": "No completeness, right-continuity, natural-filtration construction or measure supplied by this wrapper."
  },
  {
    "id": "urn:csabs:operation/Filtration-at-time",
    "type": "Operation",
    "name": "at-time",
    "signature": "T → SigmaAlgebra(Ω)",
    "description": "Return the sub-sigma-algebra 𝓕ₜ; total for each t∈T.",
    "concept": "urn:csabs:concept/Filtration",
    "precondition": "Fix the concept parameters; inputs lie in the signature domains and satisfy its displayed constraints.",
    "postcondition": "Return the sub-sigma-algebra 𝓕ₜ; total for each t∈T.",
    "totality": "total on the stated domain"
  },
  {
    "id": "urn:csabs:operation/Filtration-constant",
    "type": "Operation",
    "name": "constant",
    "signature": "{𝓖:SigmaAlgebra(Ω) | 𝓖⊆Σ} → Filtration(T,Σ)",
    "description": "Return 𝓕ₜ=𝓖 for every t. The containment check is a precondition.",
    "concept": "urn:csabs:concept/Filtration",
    "precondition": "Fix the concept parameters; inputs lie in the signature domains and satisfy its displayed constraints.",
    "postcondition": "Return 𝓕ₜ=𝓖 for every t. The containment check is a precondition.",
    "totality": "total on the stated domain"
  },
  {
    "id": "urn:csabs:axiom/Filtration-basis",
    "type": "Axiom",
    "name": "basis",
    "statement": "Each 𝓕ₜ is a sigma-algebra on Ω contained in Σ, and s≤t implies 𝓕ₛ⊆𝓕ₜ.",
    "formalStatement": "∀t: 𝓕ₜ is a sigma-algebra on Ω ∧ 𝓕ₜ⊆Σ; ∀s≤t:𝓕ₛ⊆𝓕ₜ",
    "assumptions": [
      "T is preordered; (Ω,Σ) is an ambient measurable space; 𝓕:T→SigmaAlgebra(Ω)."
    ],
    "appliesTo": [
      "urn:csabs:concept/Filtration"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "sourced defining constraint; not itself a theorem witness",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/mathlib-pinned-stochastic-filtration"
    ],
    "sourceLocator": "MeasureTheory.Filtration; Filtration.mono; Filtration.le; Filtration.const",
    "sourceNote": "Adapted from the consulted pinned source to the explicit catalog carriers and equality conventions.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:theorem/Filtration-model-satisfaction",
    "type": "Theorem",
    "name": "model-satisfaction",
    "statement": "For every preordered T and measurable (Ω,Σ), 𝓕ₜ=Σ is a filtration.",
    "formalStatement": "For every preordered T and measurable (Ω,Σ), 𝓕ₜ=Σ is a filtration.",
    "assumptions": [
      "Use the parameters and semantic conventions in the concept definition."
    ],
    "appliesTo": [
      "urn:csabs:concept/Filtration"
    ],
    "dependsOn": [
      "urn:csabs:axiom/Filtration-basis"
    ],
    "proofSketch": "Use the ambient sigma-algebra at each time. Containment and monotonicity are reflexivity, and each slice is already a sigma-algebra.",
    "reviewStatus": "constructive Lean witness registered; verification requires a fresh compiler and axiom-audit report",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/mathlib-pinned-stochastic-filtration"
    ],
    "sourceLocator": "MeasureTheory.Filtration; Filtration.mono; Filtration.le; Filtration.const",
    "sourceNote": "Constructive model derived from the linked defining constraints and the cited library construction; the local Lean theorem separately checks the stated type.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ (T : Type) [Preorder T] {Ω : Type} (m : MeasurableSpace Ω), Nonempty (Catalog.Filtration T m)",
    "formulationSource": "urn:csabs:source/local-lean-StochasticProcesses",
    "formulationLocator": "Catalog.filtration_model_satisfaction",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "For every preordered T and measurable (Ω,Σ), 𝓕ₜ=Σ is a filtration. The Nonempty inhabitant contains the defining constraints as checked proof fields; this witnesses model existence, not all properties of arbitrary processes.",
    "leanModelLimitations": "Constructive model satisfaction for the stated parameters only. No blanket proof of other catalog operations or derived results.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/Filtration-basis\": \"Satisfied by the concrete construction in the proof: Use the ambient sigma-algebra at each time. Containment and monotonicity are reflexivity, and each slice is already a sigma-algebra.\"}"
  }
]
```
<!-- graph-record:end -->
