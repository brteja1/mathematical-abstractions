# Conditional probability given a positive-probability event

Event probability conditioned on a measurable event B of strictly positive probability, defined by normalizing the intersection probability.

**Notation:** P(A∣B)=P(A∩B)/P(B), A,B∈𝓕, P(B)>0

**Stable ID:** `urn:csabs:concept/ConditionalProbability`

**Categories:** Probability and stochastic models

**Kind:** Function

**Prerequisites:** [Probability space (normalized measure)](ProbabilitySpace.md)

## Backlinks

- [Bayesian network (finite discrete variables)](BayesianNetwork.md) — `requiresConcept`
- [Markov chain (finite-state, discrete-time, time-homogeneous)](MarkovChain.md) — `requiresConcept`

## Interface and scope

**axiomBasis:** Define conditioning by the ratio P(A∩B)/P(B) only when P(B)>0.

**basisKind:** defined-structure

**basisScope:** Event conditioning, multiplication rule and Bayes rule. Conditioning on null events or sigma-algebras requires a separate interface.

**verificationObligation:** Undefined at P(B)=0; no arbitrary zero-denominator convention. Use finite real probabilities.; Use the stated carriers and equality. Specialization does not automatically transfer operations or claims.

**reviewStatus:** editorial interface review; not machine-proved

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-ConditionalProbability-condition"></a>

### condition

`urn:csabs:operation/ConditionalProbability-condition`

**signature:** {(A,B)∈𝓕²:P(B)>0} → [0,1]

**description:** Return P(A∩B)/P(B).

**precondition:** A,B∈𝓕 and P(B)>0.

**postcondition:** Return P(A∩B)/P(B).

**totality:** partial on 𝓕²; total on pairs with P(B)>0

## Axioms and defining rules

<a id="node-urn-csabs-axiom-ConditionalProbability-ratio"></a>

### ratio

`urn:csabs:axiom/ConditionalProbability-ratio`

**statement:** Conditioning on a positive-probability event is normalized intersection probability.

**formalStatement:** P(B)>0 ⇒ P(A∣B)=P(A∩B)/P(B)

**assumptions:** P(A∣B)=P(A∩B)/P(B), A,B∈𝓕, P(B)>0; Use the concept’s declared semantic conventions.

**reviewStatus:** editorial definition; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Stanford CS228 notes: Probability Review](https://ermongroup.github.io/cs228-notes/preliminaries/probabilityreview/); accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** §3.4 Conditional distributions

**sourceNote:** Defining constraint or equation adapted to the declared carriers and catalog notation.

**provenanceKind:** adapted

**ruleRole:** defining-rule

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-ConditionalProbability-multiplication"></a>

### multiplication

`urn:csabs:theorem/ConditionalProbability-multiplication`

**statement:** Conditional probability reconstructs the joint event probability.

**formalStatement:** A,B∈𝓕 and P(B)>0 ⇒ P(A∩B)=P(A∣B)P(B)

**assumptions:** P(A∣B)=P(A∩B)/P(B), A,B∈𝓕, P(B)>0; Use the concept’s declared semantic conventions.

**reviewStatus:** editorial derivation; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Stanford CS228 notes: Probability Review](https://ermongroup.github.io/cs228-notes/preliminaries/probabilityreview/); accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** §3.5 Chain rule

**sourceNote:** Derived from the linked local premises; proof sketch gives the adaptation.

**provenanceKind:** derived

**dependsOn:** [ratio](ConditionalProbability.md#node-urn-csabs-axiom-ConditionalProbability-ratio)

**proofSketch:** Multiply the defining ratio by the positive finite denominator P(B).

<a id="node-urn-csabs-theorem-ConditionalProbability-bayes"></a>

### bayes

`urn:csabs:theorem/ConditionalProbability-bayes`

**statement:** Bayes rule exchanges the conditioned and conditioning events.

**formalStatement:** A,B∈𝓕 and P(A)>0 and P(B)>0 ⇒ P(A∣B)=P(B∣A)P(A)/P(B)

**assumptions:** P(A∣B)=P(A∩B)/P(B), A,B∈𝓕, P(B)>0; Use the concept’s declared semantic conventions.

**reviewStatus:** editorial derivation; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Stanford CS228 notes: Probability Review](https://ermongroup.github.io/cs228-notes/preliminaries/probabilityreview/); accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** §3.6 Bayes’ rule

**sourceNote:** Derived from the linked local premises; proof sketch gives the adaptation.

**provenanceKind:** derived

**dependsOn:** [ratio](ConditionalProbability.md#node-urn-csabs-axiom-ConditionalProbability-ratio); [multiplication](ConditionalProbability.md#node-urn-csabs-theorem-ConditionalProbability-multiplication)

**proofSketch:** Apply the multiplication rule to P(B∩A), use A∩B=B∩A, and divide by P(B)>0.

## Concept provenance

- [Stanford CS228 notes: Probability Review](https://ermongroup.github.io/cs228-notes/preliminaries/probabilityreview/); accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** §3.4 Conditional distributions; §3.6 Bayes’ rule (adapted to events)

**sourceNote:** Interface adapted to the catalog notation and explicitly restricted to the stated scope.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/ConditionalProbability",
    "type": "Concept",
    "shortForm": "ConditionalProbability",
    "fullName": "Conditional probability given a positive-probability event",
    "category": [
      "urn:csabs:category/probability"
    ],
    "kind": "urn:csabs:kind/function",
    "definition": "Event probability conditioned on a measurable event B of strictly positive probability, defined by normalizing the intersection probability.",
    "notation": "P(A∣B)=P(A∩B)/P(B), A,B∈𝓕, P(B)>0",
    "hasOperation": [
      "urn:csabs:operation/ConditionalProbability-condition"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/ConditionalProbability-ratio"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/ConditionalProbability-multiplication",
      "urn:csabs:theorem/ConditionalProbability-bayes"
    ],
    "axiomBasis": "Define conditioning by the ratio P(A∩B)/P(B) only when P(B)>0.",
    "basisKind": "defined-structure",
    "basisScope": "Event conditioning, multiplication rule and Bayes rule. Conditioning on null events or sigma-algebras requires a separate interface.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "editorial interface review; not machine-proved",
    "requiresConcept": [
      "urn:csabs:concept/ProbabilitySpace"
    ],
    "verificationObligation": [
      "Undefined at P(B)=0; no arbitrary zero-denominator convention. Use finite real probabilities.",
      "Use the stated carriers and equality. Specialization does not automatically transfer operations or claims."
    ],
    "source": [
      "urn:csabs:source/cs228-probability-review"
    ],
    "sourceLocator": "§3.4 Conditional distributions; §3.6 Bayes’ rule (adapted to events)",
    "sourceNote": "Interface adapted to the catalog notation and explicitly restricted to the stated scope.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/ConditionalProbability-condition",
    "type": "Operation",
    "name": "condition",
    "signature": "{(A,B)∈𝓕²:P(B)>0} → [0,1]",
    "description": "Return P(A∩B)/P(B).",
    "concept": "urn:csabs:concept/ConditionalProbability",
    "precondition": "A,B∈𝓕 and P(B)>0.",
    "postcondition": "Return P(A∩B)/P(B).",
    "totality": "partial on 𝓕²; total on pairs with P(B)>0"
  },
  {
    "id": "urn:csabs:axiom/ConditionalProbability-ratio",
    "type": "Axiom",
    "name": "ratio",
    "statement": "Conditioning on a positive-probability event is normalized intersection probability.",
    "formalStatement": "P(B)>0 ⇒ P(A∣B)=P(A∩B)/P(B)",
    "appliesTo": [
      "urn:csabs:concept/ConditionalProbability"
    ],
    "assumptions": [
      "P(A∣B)=P(A∩B)/P(B), A,B∈𝓕, P(B)>0",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial definition; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/cs228-probability-review"
    ],
    "sourceLocator": "§3.4 Conditional distributions",
    "sourceNote": "Defining constraint or equation adapted to the declared carriers and catalog notation.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:theorem/ConditionalProbability-multiplication",
    "type": "Theorem",
    "name": "multiplication",
    "statement": "Conditional probability reconstructs the joint event probability.",
    "formalStatement": "A,B∈𝓕 and P(B)>0 ⇒ P(A∩B)=P(A∣B)P(B)",
    "appliesTo": [
      "urn:csabs:concept/ConditionalProbability"
    ],
    "assumptions": [
      "P(A∣B)=P(A∩B)/P(B), A,B∈𝓕, P(B)>0",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial derivation; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/cs228-probability-review"
    ],
    "sourceLocator": "§3.5 Chain rule",
    "sourceNote": "Derived from the linked local premises; proof sketch gives the adaptation.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/ConditionalProbability-ratio"
    ],
    "proofSketch": "Multiply the defining ratio by the positive finite denominator P(B)."
  },
  {
    "id": "urn:csabs:theorem/ConditionalProbability-bayes",
    "type": "Theorem",
    "name": "bayes",
    "statement": "Bayes rule exchanges the conditioned and conditioning events.",
    "formalStatement": "A,B∈𝓕 and P(A)>0 and P(B)>0 ⇒ P(A∣B)=P(B∣A)P(A)/P(B)",
    "appliesTo": [
      "urn:csabs:concept/ConditionalProbability"
    ],
    "assumptions": [
      "P(A∣B)=P(A∩B)/P(B), A,B∈𝓕, P(B)>0",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial derivation; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/cs228-probability-review"
    ],
    "sourceLocator": "§3.6 Bayes’ rule",
    "sourceNote": "Derived from the linked local premises; proof sketch gives the adaptation.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/ConditionalProbability-ratio",
      "urn:csabs:theorem/ConditionalProbability-multiplication"
    ],
    "proofSketch": "Apply the multiplication rule to P(B∩A), use A∩B=B∩A, and divide by P(B)>0."
  }
]
```
<!-- graph-record:end -->
