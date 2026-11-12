# Conditional probability given a positive-probability event

Event probability conditioned on a measurable event B of strictly positive probability, defined by normalizing the intersection probability.

**Notation:** P(A∣B)=P(A∩B)/P(B), A,B∈𝓕, P(B)>0

**Stable ID:** `urn:csabs:concept/ConditionalProbability`

**Categories:** Probability and stochastic models

**Kind:** Function

**Prerequisites:** [Probability space (normalized measure)](ProbabilitySpace.md)

## Backlinks

- [Bayesian network (finite discrete variables)](BayesianNetwork.md) — `requiresConcept`
- [Conditional entropy (finite discrete profile)](ConditionalEntropy.md) — `requiresConcept`
- [Markov chain (finite-state, discrete-time, time-homogeneous)](MarkovChain.md) — `requiresConcept`

## Mathematical formulation

For measurable E,G with P(G)>0, P(E|G)=P(E∩G)/P(G). The Lean arguments carry measurability and positive-denominator proofs; conditioning on null events is outside this interface.

**Lean formulation** (in its source module context):

```lean
noncomputable def ConditionalProbability {A : Type u} [_root_.MeasurableSpace A]
    (P : ProbabilitySpace A) (event givenEvent : _root_.Set A)
    (_ : MeasurableSet event) (_ : MeasurableSet givenEvent)
    (_ : 0 < P.val givenEvent) : ℝ :=
  (P.val (event ∩ givenEvent)).toReal / (P.val givenEvent).toReal
```

**Source:** [`Catalog.ConditionalProbability`](../lean/Catalog/Probability.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Real ratio of measurable intersection/event probabilities with explicit positive-denominator precondition.

**Limits:** Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

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
    "provenanceKind": "adapted",
    "leanFormulation": "noncomputable def ConditionalProbability {A : Type u} [_root_.MeasurableSpace A]\n    (P : ProbabilitySpace A) (event givenEvent : _root_.Set A)\n    (_ : MeasurableSet event) (_ : MeasurableSet givenEvent)\n    (_ : 0 < P.val givenEvent) : ℝ :=\n  (P.val (event ∩ givenEvent)).toReal / (P.val givenEvent).toReal",
    "formulationSource": "urn:csabs:source/local-lean-Probability",
    "formulationLocator": "Catalog.ConditionalProbability",
    "formulationScope": "model",
    "leanModelMapping": "Real ratio of measurable intersection/event probabilities with explicit positive-denominator precondition.",
    "leanModelLimitations": "Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.",
    "mathematicalFormulation": "For measurable E,G with P(G)>0, P(E|G)=P(E∩G)/P(G). The Lean arguments carry measurability and positive-denominator proofs; conditioning on null events is outside this interface."
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
