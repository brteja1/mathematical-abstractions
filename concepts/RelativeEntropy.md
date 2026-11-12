# Relative entropy (finite Kullback–Leibler divergence)

Extended-real information divergence between two laws on the same alphabet.

**Notation:** D(p∥q)=Σx p(x)log₂(p(x)/q(x))

**Stable ID:** `urn:csabs:concept/RelativeEntropy`

**Categories:** Information theory

**Kind:** Function

**Prerequisites:** [Finitely supported probability distribution](FiniteDistribution.md)

**Related concepts:** [Shannon entropy (finite discrete profile)](ShannonEntropy.md)

## Backlinks

- [Mutual information (finite discrete profile)](MutualInformation.md) — `requiresConcept`
- [Shannon entropy (finite discrete profile)](ShannonEntropy.md) — `relatedConcept`

## Mathematical formulation

For normalized finite laws p,q on A, D(p∥q)=Σ\_a p(a)log₂(p(a)/q(a)) if supp(p)⊆supp(q); otherwise D=+∞. Terms with p(a)=0 contribute 0; the Lean result none encodes +∞.

**Lean formulation** (in its source module context):

```lean
abbrev RelativeEntropy := @Information.divergence
```

**Source:** [`Catalog.RelativeEntropy`](../lean/Catalog/InformationTheory.lean); consulted 2026-11-12.

**Scope:** partial

**Interpretation:** Two exact normalized finite laws; None denotes positive infinity on support mismatch; Some value is the finite KL sum in bits.

**Limits:** No Gibbs inequality witness; Option encoding of extended values needs API mapping. These are model bindings, not proofs of the catalog theorems.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** If supp(p)⊆supp(q), D(p∥q)=Σ{x:p(x)>0}p(x)log₂(p(x)/q(x)); otherwise D(p∥q)=+∞.

**basisKind:** extensional-structural-definition

**basisScope:** Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. A positive p(x) with q(x)=0 gives +∞; p(x)=0 contributes zero. This is not a metric.

**verificationObligation:** Map alphabets, exact arithmetic, equality, logarithm base, channel model and error criterion before use.; Retrieve explicit premises; category and specialization links do not inherit claims.

**reviewStatus:** Editorial mathematical review; Lean models are explicitly scoped and theorem sketches are not compiled proofs.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-RelativeEntropy-divergence"></a>

### divergence

`urn:csabs:operation/RelativeEntropy-divergence`

**signature:** D : Dist(A)×Dist(A) → ℝ∪{+∞}

**description:** Return +∞ on a support mismatch; otherwise sum over supp(p).

**precondition:** Inputs satisfy the concept profile.

**totality:** Total on the stated domain.

**postcondition:** Return +∞ on a support mismatch; otherwise sum over supp(p).

**source:** [Yury Polyanskiy, MIT 6.441 (2016), Chapter 1: Information measures: entropy and divergence](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/2243edffb30f57181ed97dcb77691580_MIT6_441S16_chapter_1.pdf); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §1.2, divergence definition and basic properties

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-RelativeEntropy-divergence-equation"></a>

### divergence-equation

`urn:csabs:axiom/RelativeEntropy-divergence-equation`

**statement:** If supp(p)⊆supp(q), D(p∥q)=Σ{x:p(x)>0}p(x)log₂(p(x)/q(x)); otherwise D(p∥q)=+∞.

**formalStatement:** If supp(p)⊆supp(q), D(p∥q)=Σ{x:p(x)>0}p(x)log₂(p(x)/q(x)); otherwise D(p∥q)=+∞.

**assumptions:** Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. A positive p(x) with q(x)=0 gives +∞; p(x)=0 contributes zero. This is not a metric.

**ruleRole:** defining-rule

**reviewStatus:** Sourced structural definition, not an independent foundational axiom.

**source:** [Yury Polyanskiy, MIT 6.441 (2016), Chapter 1: Information measures: entropy and divergence](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/2243edffb30f57181ed97dcb77691580_MIT6_441S16_chapter_1.pdf); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §1.2, divergence definition and basic properties

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-RelativeEntropy-gibbs"></a>

### Gibbs inequality

`urn:csabs:theorem/RelativeEntropy-gibbs`

**statement:** D(p∥q)≥0, with equality iff p=q.

**formalStatement:** D(p∥q)≥0, with equality iff p=q.

**assumptions:** Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. A positive p(x) with q(x)=0 gives +∞; p(x)=0 contributes zero. This is not a metric.

**dependsOn:** [divergence-equation](RelativeEntropy.md#node-urn-csabs-axiom-RelativeEntropy-divergence-equation)

**proofSketch:** For matching support use −log u≥(1−u)/ln 2 with u=q(x)/p(x), and sum; equality forces identical masses and no extra q mass. A support mismatch gives +∞.

**reviewStatus:** Editorial proof sketch; no registered Lean theorem witness.

**source:** [Yury Polyanskiy, MIT 6.441 (2016), Chapter 1: Information measures: entropy and divergence](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/2243edffb30f57181ed97dcb77691580_MIT6_441S16_chapter_1.pdf); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §1.2, divergence definition and basic properties

**sourceNote:** Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.

**provenanceKind:** derived

## Concept provenance

- [Yury Polyanskiy, MIT 6.441 (2016), Chapter 1: Information measures: entropy and divergence](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/2243edffb30f57181ed97dcb77691580_MIT6_441S16_chapter_1.pdf); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §1.2, divergence definition and basic properties

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/RelativeEntropy",
    "type": "Concept",
    "shortForm": "RelativeEntropy",
    "fullName": "Relative entropy (finite Kullback–Leibler divergence)",
    "category": [
      "urn:csabs:category/information-theory"
    ],
    "kind": "urn:csabs:kind/function",
    "definition": "Extended-real information divergence between two laws on the same alphabet.",
    "notation": "D(p∥q)=Σx p(x)log₂(p(x)/q(x))",
    "requiresConcept": [
      "urn:csabs:concept/FiniteDistribution"
    ],
    "relatedConcept": [
      "urn:csabs:concept/ShannonEntropy"
    ],
    "hasOperation": [
      "urn:csabs:operation/RelativeEntropy-divergence"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/RelativeEntropy-divergence-equation"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/RelativeEntropy-gibbs"
    ],
    "axiomBasis": "If supp(p)⊆supp(q), D(p∥q)=Σ{x:p(x)>0}p(x)log₂(p(x)/q(x)); otherwise D(p∥q)=+∞.",
    "basisKind": "extensional-structural-definition",
    "basisScope": "Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. A positive p(x) with q(x)=0 gives +∞; p(x)=0 contributes zero. This is not a metric.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial mathematical review; Lean models are explicitly scoped and theorem sketches are not compiled proofs.",
    "verificationObligation": [
      "Map alphabets, exact arithmetic, equality, logarithm base, channel model and error criterion before use.",
      "Retrieve explicit premises; category and specialization links do not inherit claims."
    ],
    "source": [
      "urn:csabs:source/mit-information-1"
    ],
    "sourceLocator": "§1.2, divergence definition and basic properties",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted",
    "leanFormulation": "abbrev RelativeEntropy := @Information.divergence",
    "formulationSource": "urn:csabs:source/local-lean-InformationTheory",
    "formulationLocator": "Catalog.RelativeEntropy",
    "formulationScope": "partial",
    "leanModelMapping": "Two exact normalized finite laws; None denotes positive infinity on support mismatch; Some value is the finite KL sum in bits.",
    "leanModelLimitations": "No Gibbs inequality witness; Option encoding of extended values needs API mapping. These are model bindings, not proofs of the catalog theorems.",
    "mathematicalFormulation": "For normalized finite laws p,q on A, D(p∥q)=Σ_a p(a)log₂(p(a)/q(a)) if supp(p)⊆supp(q); otherwise D=+∞. Terms with p(a)=0 contribute 0; the Lean result none encodes +∞."
  },
  {
    "id": "urn:csabs:operation/RelativeEntropy-divergence",
    "type": "Operation",
    "name": "divergence",
    "signature": "D : Dist(A)×Dist(A) → ℝ∪{+∞}",
    "description": "Return +∞ on a support mismatch; otherwise sum over supp(p).",
    "concept": "urn:csabs:concept/RelativeEntropy",
    "precondition": "Inputs satisfy the concept profile.",
    "totality": "Total on the stated domain.",
    "postcondition": "Return +∞ on a support mismatch; otherwise sum over supp(p).",
    "source": [
      "urn:csabs:source/mit-information-1"
    ],
    "sourceLocator": "§1.2, divergence definition and basic properties",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/RelativeEntropy-divergence-equation",
    "type": "Axiom",
    "name": "divergence-equation",
    "statement": "If supp(p)⊆supp(q), D(p∥q)=Σ{x:p(x)>0}p(x)log₂(p(x)/q(x)); otherwise D(p∥q)=+∞.",
    "formalStatement": "If supp(p)⊆supp(q), D(p∥q)=Σ{x:p(x)>0}p(x)log₂(p(x)/q(x)); otherwise D(p∥q)=+∞.",
    "assumptions": [
      "Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. A positive p(x) with q(x)=0 gives +∞; p(x)=0 contributes zero. This is not a metric."
    ],
    "appliesTo": [
      "urn:csabs:concept/RelativeEntropy"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Sourced structural definition, not an independent foundational axiom.",
    "source": [
      "urn:csabs:source/mit-information-1"
    ],
    "sourceLocator": "§1.2, divergence definition and basic properties",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:theorem/RelativeEntropy-gibbs",
    "type": "Theorem",
    "name": "Gibbs inequality",
    "statement": "D(p∥q)≥0, with equality iff p=q.",
    "formalStatement": "D(p∥q)≥0, with equality iff p=q.",
    "assumptions": [
      "Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. A positive p(x) with q(x)=0 gives +∞; p(x)=0 contributes zero. This is not a metric."
    ],
    "appliesTo": [
      "urn:csabs:concept/RelativeEntropy"
    ],
    "dependsOn": [
      "urn:csabs:axiom/RelativeEntropy-divergence-equation"
    ],
    "proofSketch": "For matching support use −log u≥(1−u)/ln 2 with u=q(x)/p(x), and sum; equality forces identical masses and no extra q mass. A support mismatch gives +∞.",
    "reviewStatus": "Editorial proof sketch; no registered Lean theorem witness.",
    "source": [
      "urn:csabs:source/mit-information-1"
    ],
    "sourceLocator": "§1.2, divergence definition and basic properties",
    "sourceNote": "Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
