# Markov chain (finite-state, discrete-time, time-homogeneous)

A stochastic process on a nonempty finite state set whose next-state distribution, conditional on any positive-probability history, depends only on the current state through a fixed row-stochastic matrix.

**Notation:** S finite nonempty; λ∈[0,1]^S, ∑ᵢλᵢ=1; K∈[0,1]^{S×S}, ∑ⱼKᵢⱼ=1; (Xₙ)ₙ≥0

**Stable ID:** `urn:csabs:concept/MarkovChain`

**Categories:** Probability and stochastic models, Linear and multilinear algebra

**Kind:** semantic-model

**Prerequisites:** [Probability space (normalized measure)](ProbabilitySpace.md), [Random variable (measurable random element)](RandomVariable.md), [Conditional probability given a positive-probability event](ConditionalProbability.md), [Finite rectangular matrix over a field](Matrix.md)

**Related concepts:** [Transition System](TransitionSystem.md), [Directed Graph](DirectedGraph.md)

## Interface and scope

**axiomBasis:** Normalized initial law, row-stochastic transition matrix, and the time-homogeneous Markov property on positive-probability histories.

**basisKind:** defined-structure

**basisScope:** Finite-state path laws and n-step distributions with row-vector convention. Continuous time and general-state kernels are outside scope.

**verificationObligation:** No irreducibility, aperiodicity, stationarity or convergence is assumed. Rows for unreachable states remain specified parameters.; A support graph records possible steps but does not retain their probabilities. K⁰ is the identity matrix.; Use the stated carriers and equality. Specialization does not automatically transfer operations or claims.

**reviewStatus:** editorial interface review; not machine-proved

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-MarkovChain-evolve"></a>

### evolve

`urn:csabs:operation/MarkovChain-evolve`

**signature:** Dist(S) × ℕ → Dist(S); (ν,n) ↦ νKⁿ

**description:** Advance a row distribution through n transitions; n=0 returns ν.

**precondition:** Inputs belong to the stated domains.

**postcondition:** Advance a row distribution through n transitions; n=0 returns ν.

**totality:** total on the stated domain

<a id="node-urn-csabs-operation-MarkovChain-path-probability"></a>

### path-probability

`urn:csabs:operation/MarkovChain-path-probability`

**signature:** S^{n+1} → [0,1]; (i₀,…,iₙ) ↦ λᵢ₀∏_{t=0}^{n−1}Kᵢₜᵢₜ₊₁

**description:** Evaluate a finite cylinder event; length-one path has probability λᵢ₀.

**precondition:** Inputs belong to the stated domains.

**postcondition:** Evaluate a finite cylinder event; length-one path has probability λᵢ₀.

**totality:** total on the stated domain

## Axioms and defining rules

<a id="node-urn-csabs-axiom-MarkovChain-stochastic-data"></a>

### stochastic-data

`urn:csabs:axiom/MarkovChain-stochastic-data`

**statement:** The initial distribution and each transition row are normalized nonnegative masses.

**formalStatement:** λᵢ≥0, ∑ᵢ∈Sλᵢ=1; Kᵢⱼ≥0, ∀i∈S:∑ⱼ∈SKᵢⱼ=1

**assumptions:** S finite nonempty; λ∈[0,1]^S, ∑ᵢλᵢ=1; K∈[0,1]^{S×S}, ∑ⱼKᵢⱼ=1; (Xₙ)ₙ≥0; Use the concept’s declared semantic conventions.

**reviewStatus:** editorial definition; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Cambridge Markov Chains course notes, hosted by Richard Weber](https://www.dpmms.cam.ac.uk/~rrw1/markov/M.pdf); citation: Markov Chains, Cambridge course notes; opening credits acknowledge material prepared by course lecturers, especially James Norris.; accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** §1.2 Definitions

**sourceNote:** Defining constraint or equation adapted to the declared carriers and catalog notation.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-MarkovChain-markov-property"></a>

### markov-property

`urn:csabs:axiom/MarkovChain-markov-property`

**statement:** The next state uses the current-state transition row on every positive-probability history.

**formalStatement:** P(X₀=i₀,…,Xₙ=iₙ)>0 ⇒ P(Xₙ₊₁=j∣X₀=i₀,…,Xₙ=iₙ)=Kᵢₙⱼ; P(X₀=i)=λᵢ

**assumptions:** S finite nonempty; λ∈[0,1]^S, ∑ᵢλᵢ=1; K∈[0,1]^{S×S}, ∑ⱼKᵢⱼ=1; (Xₙ)ₙ≥0; Use the concept’s declared semantic conventions.

**reviewStatus:** editorial definition; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Cambridge Markov Chains course notes, hosted by Richard Weber](https://www.dpmms.cam.ac.uk/~rrw1/markov/M.pdf); citation: Markov Chains, Cambridge course notes; opening credits acknowledge material prepared by course lecturers, especially James Norris.; accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** §1.2 Definitions

**sourceNote:** Defining constraint or equation adapted to the declared carriers and catalog notation.

**provenanceKind:** adapted

**ruleRole:** defining-rule

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-MarkovChain-path-law"></a>

### path-law

`urn:csabs:theorem/MarkovChain-path-law`

**statement:** A finite trajectory has the product probability specified by the initial law and transitions.

**formalStatement:** P(X₀=i₀,…,Xₙ=iₙ)=λᵢ₀∏_{t=0}^{n−1}Kᵢₜᵢₜ₊₁

**assumptions:** S finite nonempty; λ∈[0,1]^S, ∑ᵢλᵢ=1; K∈[0,1]^{S×S}, ∑ⱼKᵢⱼ=1; (Xₙ)ₙ≥0; Use the concept’s declared semantic conventions.

**reviewStatus:** editorial derivation; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Cambridge Markov Chains course notes, hosted by Richard Weber](https://www.dpmms.cam.ac.uk/~rrw1/markov/M.pdf); citation: Markov Chains, Cambridge course notes; opening credits acknowledge material prepared by course lecturers, especially James Norris.; accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** §1.2 Definitions, printed p. 2 (finite path law derived from the defining Markov property)

**sourceNote:** Derived from the linked local premises; proof sketch gives the adaptation.

**provenanceKind:** derived

**dependsOn:** [stochastic-data](MarkovChain.md#node-urn-csabs-axiom-MarkovChain-stochastic-data); [markov-property](MarkovChain.md#node-urn-csabs-axiom-MarkovChain-markov-property); [multiplication](ConditionalProbability.md#node-urn-csabs-theorem-ConditionalProbability-multiplication); [path-probability](MarkovChain.md#node-urn-csabs-operation-MarkovChain-path-probability); [monotonicity](MeasureSpace.md#node-urn-csabs-theorem-MeasureSpace-monotonicity)

**proofSketch:** Induct on the number of steps using the multiplication rule and Markov property when the prefix has positive probability. If the prefix has probability zero, its extension has probability zero by monotonicity; the inductive product is zero too.

<a id="node-urn-csabs-theorem-MarkovChain-n-step-law"></a>

### n-step-law

`urn:csabs:theorem/MarkovChain-n-step-law`

**statement:** The state distribution is the initial row law multiplied by the n-th matrix power.

**formalStatement:** ∀n∈ℕ,j∈S:P(Xₙ=j)=(λKⁿ)ⱼ; Kⁿ⁺ᵐ=KⁿKᵐ

**assumptions:** S finite nonempty; λ∈[0,1]^S, ∑ᵢλᵢ=1; K∈[0,1]^{S×S}, ∑ⱼKᵢⱼ=1; (Xₙ)ₙ≥0; Use the concept’s declared semantic conventions.

**reviewStatus:** editorial derivation; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Cambridge Markov Chains course notes, hosted by Richard Weber](https://www.dpmms.cam.ac.uk/~rrw1/markov/M.pdf); citation: Markov Chains, Cambridge course notes; opening credits acknowledge material prepared by course lecturers, especially James Norris.; accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** §1.5 The n-step transition matrix, printed p. 3; Chapman–Kolmogorov equations

**sourceNote:** Derived from the linked local premises; proof sketch gives the adaptation.

**provenanceKind:** derived

**dependsOn:** [path-law](MarkovChain.md#node-urn-csabs-theorem-MarkovChain-path-law); [evolve](MarkovChain.md#node-urn-csabs-operation-MarkovChain-evolve); [multiply-entry](Matrix.md#node-urn-csabs-axiom-Matrix-multiply-entry)

**proofSketch:** Sum the path law over intermediate states. Finite distributivity identifies the result with row-vector multiplication by Kⁿ. Splitting the finite paths at time n gives matrix multiplication KⁿKᵐ, including identity powers at time zero.

## Concept provenance

- [Cambridge Markov Chains course notes, hosted by Richard Weber](https://www.dpmms.cam.ac.uk/~rrw1/markov/M.pdf); citation: Markov Chains, Cambridge course notes; opening credits acknowledge material prepared by course lecturers, especially James Norris.; accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** §1.2 Definitions, printed p. 2; §1.5 The n-step transition matrix, printed p. 3

**sourceNote:** Interface adapted to the catalog notation and explicitly restricted to the stated scope.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/MarkovChain",
    "type": "Concept",
    "shortForm": "MarkovChain",
    "fullName": "Markov chain (finite-state, discrete-time, time-homogeneous)",
    "category": [
      "urn:csabs:category/probability",
      "urn:csabs:category/linear-algebra"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "definition": "A stochastic process on a nonempty finite state set whose next-state distribution, conditional on any positive-probability history, depends only on the current state through a fixed row-stochastic matrix.",
    "notation": "S finite nonempty; λ∈[0,1]^S, ∑ᵢλᵢ=1; K∈[0,1]^{S×S}, ∑ⱼKᵢⱼ=1; (Xₙ)ₙ≥0",
    "hasOperation": [
      "urn:csabs:operation/MarkovChain-evolve",
      "urn:csabs:operation/MarkovChain-path-probability"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/MarkovChain-stochastic-data",
      "urn:csabs:axiom/MarkovChain-markov-property"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/MarkovChain-path-law",
      "urn:csabs:theorem/MarkovChain-n-step-law"
    ],
    "axiomBasis": "Normalized initial law, row-stochastic transition matrix, and the time-homogeneous Markov property on positive-probability histories.",
    "basisKind": "defined-structure",
    "basisScope": "Finite-state path laws and n-step distributions with row-vector convention. Continuous time and general-state kernels are outside scope.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "editorial interface review; not machine-proved",
    "requiresConcept": [
      "urn:csabs:concept/ProbabilitySpace",
      "urn:csabs:concept/RandomVariable",
      "urn:csabs:concept/ConditionalProbability",
      "urn:csabs:concept/Matrix"
    ],
    "verificationObligation": [
      "No irreducibility, aperiodicity, stationarity or convergence is assumed. Rows for unreachable states remain specified parameters.",
      "A support graph records possible steps but does not retain their probabilities. K⁰ is the identity matrix.",
      "Use the stated carriers and equality. Specialization does not automatically transfer operations or claims."
    ],
    "source": [
      "urn:csabs:source/cambridge-markov-chains"
    ],
    "sourceLocator": "§1.2 Definitions, printed p. 2; §1.5 The n-step transition matrix, printed p. 3",
    "sourceNote": "Interface adapted to the catalog notation and explicitly restricted to the stated scope.",
    "provenanceKind": "adapted",
    "relatedConcept": [
      "urn:csabs:concept/TransitionSystem",
      "urn:csabs:concept/DirectedGraph"
    ]
  },
  {
    "id": "urn:csabs:operation/MarkovChain-evolve",
    "type": "Operation",
    "name": "evolve",
    "signature": "Dist(S) × ℕ → Dist(S); (ν,n) ↦ νKⁿ",
    "description": "Advance a row distribution through n transitions; n=0 returns ν.",
    "concept": "urn:csabs:concept/MarkovChain",
    "precondition": "Inputs belong to the stated domains.",
    "postcondition": "Advance a row distribution through n transitions; n=0 returns ν.",
    "totality": "total on the stated domain"
  },
  {
    "id": "urn:csabs:operation/MarkovChain-path-probability",
    "type": "Operation",
    "name": "path-probability",
    "signature": "S^{n+1} → [0,1]; (i₀,…,iₙ) ↦ λᵢ₀∏_{t=0}^{n−1}Kᵢₜᵢₜ₊₁",
    "description": "Evaluate a finite cylinder event; length-one path has probability λᵢ₀.",
    "concept": "urn:csabs:concept/MarkovChain",
    "precondition": "Inputs belong to the stated domains.",
    "postcondition": "Evaluate a finite cylinder event; length-one path has probability λᵢ₀.",
    "totality": "total on the stated domain"
  },
  {
    "id": "urn:csabs:axiom/MarkovChain-stochastic-data",
    "type": "Axiom",
    "name": "stochastic-data",
    "statement": "The initial distribution and each transition row are normalized nonnegative masses.",
    "formalStatement": "λᵢ≥0, ∑ᵢ∈Sλᵢ=1; Kᵢⱼ≥0, ∀i∈S:∑ⱼ∈SKᵢⱼ=1",
    "appliesTo": [
      "urn:csabs:concept/MarkovChain"
    ],
    "assumptions": [
      "S finite nonempty; λ∈[0,1]^S, ∑ᵢλᵢ=1; K∈[0,1]^{S×S}, ∑ⱼKᵢⱼ=1; (Xₙ)ₙ≥0",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial definition; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/cambridge-markov-chains"
    ],
    "sourceLocator": "§1.2 Definitions",
    "sourceNote": "Defining constraint or equation adapted to the declared carriers and catalog notation.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/MarkovChain-markov-property",
    "type": "Axiom",
    "name": "markov-property",
    "statement": "The next state uses the current-state transition row on every positive-probability history.",
    "formalStatement": "P(X₀=i₀,…,Xₙ=iₙ)>0 ⇒ P(Xₙ₊₁=j∣X₀=i₀,…,Xₙ=iₙ)=Kᵢₙⱼ; P(X₀=i)=λᵢ",
    "appliesTo": [
      "urn:csabs:concept/MarkovChain"
    ],
    "assumptions": [
      "S finite nonempty; λ∈[0,1]^S, ∑ᵢλᵢ=1; K∈[0,1]^{S×S}, ∑ⱼKᵢⱼ=1; (Xₙ)ₙ≥0",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial definition; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/cambridge-markov-chains"
    ],
    "sourceLocator": "§1.2 Definitions",
    "sourceNote": "Defining constraint or equation adapted to the declared carriers and catalog notation.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:theorem/MarkovChain-path-law",
    "type": "Theorem",
    "name": "path-law",
    "statement": "A finite trajectory has the product probability specified by the initial law and transitions.",
    "formalStatement": "P(X₀=i₀,…,Xₙ=iₙ)=λᵢ₀∏_{t=0}^{n−1}Kᵢₜᵢₜ₊₁",
    "appliesTo": [
      "urn:csabs:concept/MarkovChain"
    ],
    "assumptions": [
      "S finite nonempty; λ∈[0,1]^S, ∑ᵢλᵢ=1; K∈[0,1]^{S×S}, ∑ⱼKᵢⱼ=1; (Xₙ)ₙ≥0",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial derivation; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/cambridge-markov-chains"
    ],
    "sourceLocator": "§1.2 Definitions, printed p. 2 (finite path law derived from the defining Markov property)",
    "sourceNote": "Derived from the linked local premises; proof sketch gives the adaptation.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/MarkovChain-stochastic-data",
      "urn:csabs:axiom/MarkovChain-markov-property",
      "urn:csabs:theorem/ConditionalProbability-multiplication",
      "urn:csabs:operation/MarkovChain-path-probability",
      "urn:csabs:theorem/MeasureSpace-monotonicity"
    ],
    "proofSketch": "Induct on the number of steps using the multiplication rule and Markov property when the prefix has positive probability. If the prefix has probability zero, its extension has probability zero by monotonicity; the inductive product is zero too."
  },
  {
    "id": "urn:csabs:theorem/MarkovChain-n-step-law",
    "type": "Theorem",
    "name": "n-step-law",
    "statement": "The state distribution is the initial row law multiplied by the n-th matrix power.",
    "formalStatement": "∀n∈ℕ,j∈S:P(Xₙ=j)=(λKⁿ)ⱼ; Kⁿ⁺ᵐ=KⁿKᵐ",
    "appliesTo": [
      "urn:csabs:concept/MarkovChain"
    ],
    "assumptions": [
      "S finite nonempty; λ∈[0,1]^S, ∑ᵢλᵢ=1; K∈[0,1]^{S×S}, ∑ⱼKᵢⱼ=1; (Xₙ)ₙ≥0",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial derivation; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/cambridge-markov-chains"
    ],
    "sourceLocator": "§1.5 The n-step transition matrix, printed p. 3; Chapman–Kolmogorov equations",
    "sourceNote": "Derived from the linked local premises; proof sketch gives the adaptation.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:theorem/MarkovChain-path-law",
      "urn:csabs:operation/MarkovChain-evolve",
      "urn:csabs:axiom/Matrix-multiply-entry"
    ],
    "proofSketch": "Sum the path law over intermediate states. Finite distributivity identifies the result with row-vector multiplication by Kⁿ. Splitting the finite paths at time n gives matrix multiplication KⁿKᵐ, including identity powers at time zero."
  }
]
```
<!-- graph-record:end -->
