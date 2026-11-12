# Probability space (normalized measure)

A measure space whose entire sample space has measure one; measurable subsets are events and their measures are probabilities.

**Notation:** (Ω,𝓕,P); P:𝓕→[0,1]; P(Ω)=1

**Stable ID:** `urn:csabs:concept/ProbabilitySpace`

**Categories:** Probability and stochastic models, Measure theory

**Kind:** Mathematical structure

**Prerequisites:** [Measure space (nonnegative countably additive measure)](MeasureSpace.md)

**Specializes:** [Measure space (nonnegative countably additive measure)](MeasureSpace.md)

## Backlinks

- [Bayesian network (finite discrete variables)](BayesianNetwork.md) — `requiresConcept`
- [Conditional probability given a positive-probability event](ConditionalProbability.md) — `requiresConcept`
- [Finitely supported probability distribution](FiniteDistribution.md) — `requiresConcept`
- [Markov chain (finite-state, discrete-time, time-homogeneous)](MarkovChain.md) — `requiresConcept`
- [Random variable (measurable random element)](RandomVariable.md) — `requiresConcept`

## Mathematical formulation

For a measurable Ω, a probability measure P satisfies P(Ω)=1 and the measure axioms. The Lean binding is the probability-measure carrier on the supplied measurable space; normalization excludes an empty Ω.

**Lean formulation** (in its source module context):

```lean
abbrev ProbabilitySpace (A : Type u) [_root_.MeasurableSpace A] := ProbabilityMeasure A
```

**Source:** [`Catalog.ProbabilitySpace`](../lean/Catalog/Probability.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Mathlib ProbabilityMeasure, carrying a measure and normalization proof on the supplied measurable carrier.

**Limits:** Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Instantiate the MeasureSpace interface with μ=P and impose the single additional normalization P(Ω)=1.

**basisKind:** defined-structure

**basisScope:** Kolmogorov probability on a sigma-algebra, event complements and bounds. No assumption that every subset is measurable.

**basisInstantiation:** Instantiate MeasureSpace at X=Ω, Σ=𝓕, μ=P, retaining its nonnegative countably additive measure requirements. Add normalization P(Ω)=1.

**specializationNote:** Use X=Ω, Σ=𝓕 and μ=P; normalization is the extra constraint.

**verificationObligation:** Ω must be nonempty because P(∅)=0 and P(Ω)=1. Events are sets, not individual outcomes unless their singletons are measurable.; Use the stated carriers and equality. Specialization does not automatically transfer operations or claims.

**reviewStatus:** editorial interface review; not machine-proved

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-ProbabilitySpace-probability"></a>

### probability

`urn:csabs:operation/ProbabilitySpace-probability`

**signature:** 𝓕 → [0,1]; A ↦ P(A)

**description:** Return the normalized measure of an event.

**precondition:** Inputs belong to the stated domains.

**postcondition:** Return the normalized measure of an event.

**totality:** total on the stated domain

## Axioms and defining rules

<a id="node-urn-csabs-axiom-ProbabilitySpace-normalization"></a>

### normalization

`urn:csabs:axiom/ProbabilitySpace-normalization`

**statement:** The total sample space has probability one.

**formalStatement:** P(Ω)=1

**assumptions:** (Ω,𝓕,P); P:𝓕→[0,1]; P(Ω)=1; Use the concept’s declared semantic conventions.

**reviewStatus:** editorial definition; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Mathlib: probability measures](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Measure/Typeclasses/Probability.html); accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** IsProbabilityMeasure

**sourceNote:** Defining constraint or equation adapted to the declared carriers and catalog notation.

**provenanceKind:** adapted

**ruleRole:** structure-law

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-ProbabilitySpace-complement"></a>

### complement

`urn:csabs:theorem/ProbabilitySpace-complement`

**statement:** An event and its complement have probabilities summing to one.

**formalStatement:** A∈𝓕 ⇒ P(Ω∖A)=1−P(A)

**assumptions:** (Ω,𝓕,P); P:𝓕→[0,1]; P(Ω)=1; Use the concept’s declared semantic conventions.

**reviewStatus:** editorial derivation; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Mathlib: probability measures](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Measure/Typeclasses/Probability.html); accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** prob_add_prob_compl; prob_compl_eq_one_sub

**sourceNote:** Derived from the linked local premises; proof sketch gives the adaptation.

**provenanceKind:** derived

**dependsOn:** [normalization](ProbabilitySpace.md#node-urn-csabs-axiom-ProbabilitySpace-normalization); [finite-additivity](MeasureSpace.md#node-urn-csabs-theorem-MeasureSpace-finite-additivity); [complement](MeasurableSpace.md#node-urn-csabs-axiom-MeasurableSpace-complement)

**proofSketch:** Instantiate finite additivity at μ=P and the disjoint partition Ω=A⊔(Ω∖A). Normalization makes both terms finite, so subtraction is valid.

<a id="node-urn-csabs-theorem-ProbabilitySpace-event-bounds"></a>

### event-bounds

`urn:csabs:theorem/ProbabilitySpace-event-bounds`

**statement:** Every event probability lies between zero and one.

**formalStatement:** A∈𝓕 ⇒ 0≤P(A)≤1

**assumptions:** (Ω,𝓕,P); P:𝓕→[0,1]; P(Ω)=1; Use the concept’s declared semantic conventions.

**reviewStatus:** editorial derivation; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Mathlib: probability measures](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Measure/Typeclasses/Probability.html); accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** prob_le_one

**sourceNote:** Derived from the linked local premises; proof sketch gives the adaptation.

**provenanceKind:** derived

**dependsOn:** [normalization](ProbabilitySpace.md#node-urn-csabs-axiom-ProbabilitySpace-normalization); [monotonicity](MeasureSpace.md#node-urn-csabs-theorem-MeasureSpace-monotonicity)

**proofSketch:** P is nonnegative by its measure codomain. Apply measure monotonicity to A⊆Ω and use normalization.

## Concept provenance

- [Mathlib: probability measures](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Measure/Typeclasses/Probability.html); accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** IsProbabilityMeasure; prob_add_prob_compl; nonempty_of_isProbabilityMeasure

**sourceNote:** Interface adapted to the catalog notation and explicitly restricted to the stated scope.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/ProbabilitySpace",
    "type": "Concept",
    "shortForm": "ProbabilitySpace",
    "fullName": "Probability space (normalized measure)",
    "category": [
      "urn:csabs:category/probability",
      "urn:csabs:category/measure-theory"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "A measure space whose entire sample space has measure one; measurable subsets are events and their measures are probabilities.",
    "notation": "(Ω,𝓕,P); P:𝓕→[0,1]; P(Ω)=1",
    "hasOperation": [
      "urn:csabs:operation/ProbabilitySpace-probability"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/ProbabilitySpace-normalization"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/ProbabilitySpace-complement",
      "urn:csabs:theorem/ProbabilitySpace-event-bounds"
    ],
    "axiomBasis": "Instantiate the MeasureSpace interface with μ=P and impose the single additional normalization P(Ω)=1.",
    "basisKind": "defined-structure",
    "basisScope": "Kolmogorov probability on a sigma-algebra, event complements and bounds. No assumption that every subset is measurable.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "editorial interface review; not machine-proved",
    "requiresConcept": [
      "urn:csabs:concept/MeasureSpace"
    ],
    "verificationObligation": [
      "Ω must be nonempty because P(∅)=0 and P(Ω)=1. Events are sets, not individual outcomes unless their singletons are measurable.",
      "Use the stated carriers and equality. Specialization does not automatically transfer operations or claims."
    ],
    "source": [
      "urn:csabs:source/mathlib-probability-measure"
    ],
    "sourceLocator": "IsProbabilityMeasure; prob_add_prob_compl; nonempty_of_isProbabilityMeasure",
    "sourceNote": "Interface adapted to the catalog notation and explicitly restricted to the stated scope.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/MeasureSpace"
    ],
    "specializationNote": "Use X=Ω, Σ=𝓕 and μ=P; normalization is the extra constraint.",
    "basisInstantiation": "Instantiate MeasureSpace at X=Ω, Σ=𝓕, μ=P, retaining its nonnegative countably additive measure requirements. Add normalization P(Ω)=1.",
    "leanFormulation": "abbrev ProbabilitySpace (A : Type u) [_root_.MeasurableSpace A] := ProbabilityMeasure A",
    "formulationSource": "urn:csabs:source/local-lean-Probability",
    "formulationLocator": "Catalog.ProbabilitySpace",
    "formulationScope": "model",
    "leanModelMapping": "Mathlib ProbabilityMeasure, carrying a measure and normalization proof on the supplied measurable carrier.",
    "leanModelLimitations": "Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.",
    "mathematicalFormulation": "For a measurable Ω, a probability measure P satisfies P(Ω)=1 and the measure axioms. The Lean binding is the probability-measure carrier on the supplied measurable space; normalization excludes an empty Ω."
  },
  {
    "id": "urn:csabs:operation/ProbabilitySpace-probability",
    "type": "Operation",
    "name": "probability",
    "signature": "𝓕 → [0,1]; A ↦ P(A)",
    "description": "Return the normalized measure of an event.",
    "concept": "urn:csabs:concept/ProbabilitySpace",
    "precondition": "Inputs belong to the stated domains.",
    "postcondition": "Return the normalized measure of an event.",
    "totality": "total on the stated domain"
  },
  {
    "id": "urn:csabs:axiom/ProbabilitySpace-normalization",
    "type": "Axiom",
    "name": "normalization",
    "statement": "The total sample space has probability one.",
    "formalStatement": "P(Ω)=1",
    "appliesTo": [
      "urn:csabs:concept/ProbabilitySpace"
    ],
    "assumptions": [
      "(Ω,𝓕,P); P:𝓕→[0,1]; P(Ω)=1",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial definition; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/mathlib-probability-measure"
    ],
    "sourceLocator": "IsProbabilityMeasure",
    "sourceNote": "Defining constraint or equation adapted to the declared carriers and catalog notation.",
    "provenanceKind": "adapted",
    "ruleRole": "structure-law"
  },
  {
    "id": "urn:csabs:theorem/ProbabilitySpace-complement",
    "type": "Theorem",
    "name": "complement",
    "statement": "An event and its complement have probabilities summing to one.",
    "formalStatement": "A∈𝓕 ⇒ P(Ω∖A)=1−P(A)",
    "appliesTo": [
      "urn:csabs:concept/ProbabilitySpace"
    ],
    "assumptions": [
      "(Ω,𝓕,P); P:𝓕→[0,1]; P(Ω)=1",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial derivation; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/mathlib-probability-measure"
    ],
    "sourceLocator": "prob_add_prob_compl; prob_compl_eq_one_sub",
    "sourceNote": "Derived from the linked local premises; proof sketch gives the adaptation.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/ProbabilitySpace-normalization",
      "urn:csabs:theorem/MeasureSpace-finite-additivity",
      "urn:csabs:axiom/MeasurableSpace-complement"
    ],
    "proofSketch": "Instantiate finite additivity at μ=P and the disjoint partition Ω=A⊔(Ω∖A). Normalization makes both terms finite, so subtraction is valid."
  },
  {
    "id": "urn:csabs:theorem/ProbabilitySpace-event-bounds",
    "type": "Theorem",
    "name": "event-bounds",
    "statement": "Every event probability lies between zero and one.",
    "formalStatement": "A∈𝓕 ⇒ 0≤P(A)≤1",
    "appliesTo": [
      "urn:csabs:concept/ProbabilitySpace"
    ],
    "assumptions": [
      "(Ω,𝓕,P); P:𝓕→[0,1]; P(Ω)=1",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial derivation; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/mathlib-probability-measure"
    ],
    "sourceLocator": "prob_le_one",
    "sourceNote": "Derived from the linked local premises; proof sketch gives the adaptation.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/ProbabilitySpace-normalization",
      "urn:csabs:theorem/MeasureSpace-monotonicity"
    ],
    "proofSketch": "P is nonnegative by its measure codomain. Apply measure monotonicity to A⊆Ω and use normalization."
  }
]
```
<!-- graph-record:end -->
