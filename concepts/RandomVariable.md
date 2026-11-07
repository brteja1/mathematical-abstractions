# Random variable (measurable random element)

A measurable function from a probability space to a specified measurable value space; its distribution is the pushforward probability measure.

**Notation:** X:(Ω,𝓕,P)→(E,𝓔); P_X(B)=P(X⁻¹(B))

**Stable ID:** `urn:csabs:concept/RandomVariable`

**Categories:** Probability and stochastic models, Measure theory

**Kind:** Function

**Prerequisites:** [Probability space (normalized measure)](ProbabilitySpace.md), [Measurable function](MeasurableFunction.md)

**Specializes:** [Measurable function](MeasurableFunction.md)

## Backlinks

- [Bayesian network (finite discrete variables)](BayesianNetwork.md) — `requiresConcept`
- [Markov chain (finite-state, discrete-time, time-homogeneous)](MarkovChain.md) — `requiresConcept`

## Interface and scope

**axiomBasis:** Use the MeasurableFunction interface with a ProbabilitySpace source. Define the law by inverse-image probabilities.

**basisKind:** defined-structure

**basisScope:** Random elements and their laws; densities and expectations require further assumptions and interfaces.

**basisInstantiation:** Instantiate MeasurableFunction at source (Ω,𝓕) and target (E,𝓔), and equip the source with P as a ProbabilitySpace. In particular, verify all target-measurable preimages are in 𝓕.

**specializationNote:** Use source measurable space (Ω,𝓕); P is extra source data. Retain the same measurable map.

**verificationObligation:** E may be any measurable space; real-valued random variables use the Borel sigma-algebra. Pointwise equality is distinct from equality almost surely and equality in distribution.; Use the stated carriers and equality. Specialization does not automatically transfer operations or claims.

**reviewStatus:** editorial interface review; not machine-proved

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-RandomVariable-law"></a>

### law

`urn:csabs:operation/RandomVariable-law`

**signature:** 𝓔 → [0,1]; B ↦ P_X(B)

**description:** Push forward P through X; target events need not have densities.

**precondition:** Inputs belong to the stated domains.

**postcondition:** Push forward P through X; target events need not have densities.

**totality:** total on the stated domain

## Axioms and defining rules

<a id="node-urn-csabs-axiom-RandomVariable-pushforward-definition"></a>

### pushforward-definition

`urn:csabs:axiom/RandomVariable-pushforward-definition`

**statement:** The distribution assigns a target event its preimage probability.

**formalStatement:** B∈𝓔 ⇒ P_X(B)=P({ω∈Ω:X(ω)∈B})

**assumptions:** X:(Ω,𝓕,P)→(E,𝓔); P_X(B)=P(X⁻¹(B)); Use the concept’s declared semantic conventions.

**reviewStatus:** editorial definition; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Mathlib: pushforward of a measure](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Measure/Map.html); accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** Measure.map_apply

**sourceNote:** Defining constraint or equation adapted to the declared carriers and catalog notation.

**provenanceKind:** adapted

**ruleRole:** defining-rule

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-RandomVariable-law-is-probability"></a>

### law-is-probability

`urn:csabs:theorem/RandomVariable-law-is-probability`

**statement:** The law of a random variable is a probability measure.

**formalStatement:** P_X(∅)=0; P_X(E)=1; disjoint Bₙ∈𝓔 ⇒ P_X(⋃ₙBₙ)=∑ₙP_X(Bₙ)

**assumptions:** X:(Ω,𝓕,P)→(E,𝓔); P_X(B)=P(X⁻¹(B)); Use the concept’s declared semantic conventions.

**reviewStatus:** editorial derivation; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Mathlib: pushforward of a measure](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Measure/Map.html); accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** Measure.map_apply; adapted normalization argument

**sourceNote:** Derived from the linked local premises; proof sketch gives the adaptation.

**provenanceKind:** derived

**dependsOn:** [pushforward-definition](RandomVariable.md#node-urn-csabs-axiom-RandomVariable-pushforward-definition); [preimage-measurability](MeasurableFunction.md#node-urn-csabs-axiom-MeasurableFunction-preimage-measurability); [empty](MeasureSpace.md#node-urn-csabs-axiom-MeasureSpace-empty); [sigma-additivity](MeasureSpace.md#node-urn-csabs-axiom-MeasureSpace-sigma-additivity); [normalization](ProbabilitySpace.md#node-urn-csabs-axiom-ProbabilitySpace-normalization)

**proofSketch:** Preimages preserve ∅, the full carrier, unions and disjointness. Apply the measurable-map condition and the source measure axioms at μ=P; normalization transfers because X⁻¹(E)=Ω.

## Concept provenance

- [Mathlib: pushforward of a measure](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Measure/Map.html); accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** Measure.map; Measure.map_apply (for a measurable map)

**sourceNote:** Interface adapted to the catalog notation and explicitly restricted to the stated scope.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/RandomVariable",
    "type": "Concept",
    "shortForm": "RandomVariable",
    "fullName": "Random variable (measurable random element)",
    "category": [
      "urn:csabs:category/probability",
      "urn:csabs:category/measure-theory"
    ],
    "kind": "urn:csabs:kind/function",
    "definition": "A measurable function from a probability space to a specified measurable value space; its distribution is the pushforward probability measure.",
    "notation": "X:(Ω,𝓕,P)→(E,𝓔); P_X(B)=P(X⁻¹(B))",
    "hasOperation": [
      "urn:csabs:operation/RandomVariable-law"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/RandomVariable-pushforward-definition"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/RandomVariable-law-is-probability"
    ],
    "axiomBasis": "Use the MeasurableFunction interface with a ProbabilitySpace source. Define the law by inverse-image probabilities.",
    "basisKind": "defined-structure",
    "basisScope": "Random elements and their laws; densities and expectations require further assumptions and interfaces.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "editorial interface review; not machine-proved",
    "requiresConcept": [
      "urn:csabs:concept/ProbabilitySpace",
      "urn:csabs:concept/MeasurableFunction"
    ],
    "verificationObligation": [
      "E may be any measurable space; real-valued random variables use the Borel sigma-algebra. Pointwise equality is distinct from equality almost surely and equality in distribution.",
      "Use the stated carriers and equality. Specialization does not automatically transfer operations or claims."
    ],
    "source": [
      "urn:csabs:source/mathlib-measure-map"
    ],
    "sourceLocator": "Measure.map; Measure.map_apply (for a measurable map)",
    "sourceNote": "Interface adapted to the catalog notation and explicitly restricted to the stated scope.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/MeasurableFunction"
    ],
    "specializationNote": "Use source measurable space (Ω,𝓕); P is extra source data. Retain the same measurable map.",
    "basisInstantiation": "Instantiate MeasurableFunction at source (Ω,𝓕) and target (E,𝓔), and equip the source with P as a ProbabilitySpace. In particular, verify all target-measurable preimages are in 𝓕."
  },
  {
    "id": "urn:csabs:operation/RandomVariable-law",
    "type": "Operation",
    "name": "law",
    "signature": "𝓔 → [0,1]; B ↦ P_X(B)",
    "description": "Push forward P through X; target events need not have densities.",
    "concept": "urn:csabs:concept/RandomVariable",
    "precondition": "Inputs belong to the stated domains.",
    "postcondition": "Push forward P through X; target events need not have densities.",
    "totality": "total on the stated domain"
  },
  {
    "id": "urn:csabs:axiom/RandomVariable-pushforward-definition",
    "type": "Axiom",
    "name": "pushforward-definition",
    "statement": "The distribution assigns a target event its preimage probability.",
    "formalStatement": "B∈𝓔 ⇒ P_X(B)=P({ω∈Ω:X(ω)∈B})",
    "appliesTo": [
      "urn:csabs:concept/RandomVariable"
    ],
    "assumptions": [
      "X:(Ω,𝓕,P)→(E,𝓔); P_X(B)=P(X⁻¹(B))",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial definition; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/mathlib-measure-map"
    ],
    "sourceLocator": "Measure.map_apply",
    "sourceNote": "Defining constraint or equation adapted to the declared carriers and catalog notation.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:theorem/RandomVariable-law-is-probability",
    "type": "Theorem",
    "name": "law-is-probability",
    "statement": "The law of a random variable is a probability measure.",
    "formalStatement": "P_X(∅)=0; P_X(E)=1; disjoint Bₙ∈𝓔 ⇒ P_X(⋃ₙBₙ)=∑ₙP_X(Bₙ)",
    "appliesTo": [
      "urn:csabs:concept/RandomVariable"
    ],
    "assumptions": [
      "X:(Ω,𝓕,P)→(E,𝓔); P_X(B)=P(X⁻¹(B))",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial derivation; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/mathlib-measure-map"
    ],
    "sourceLocator": "Measure.map_apply; adapted normalization argument",
    "sourceNote": "Derived from the linked local premises; proof sketch gives the adaptation.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/RandomVariable-pushforward-definition",
      "urn:csabs:axiom/MeasurableFunction-preimage-measurability",
      "urn:csabs:axiom/MeasureSpace-empty",
      "urn:csabs:axiom/MeasureSpace-sigma-additivity",
      "urn:csabs:axiom/ProbabilitySpace-normalization"
    ],
    "proofSketch": "Preimages preserve ∅, the full carrier, unions and disjointness. Apply the measurable-map condition and the source measure axioms at μ=P; normalization transfers because X⁻¹(E)=Ω."
  }
]
```
<!-- graph-record:end -->
