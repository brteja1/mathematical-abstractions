# Shannon entropy (finite discrete profile)

Expected self-information of a finite distribution.

**Notation:** H(p)=−Σx p(x)log₂p(x)

**Stable ID:** `urn:csabs:concept/ShannonEntropy`

**Categories:** Information theory

**Kind:** Function

**Prerequisites:** [Finitely supported probability distribution](FiniteDistribution.md), [Random variable (measurable random element)](RandomVariable.md)

**Related concepts:** [Relative entropy (finite Kullback–Leibler divergence)](RelativeEntropy.md)

## Backlinks

- [Conditional entropy (finite discrete profile)](ConditionalEntropy.md) — `requiresConcept`
- [Relative entropy (finite Kullback–Leibler divergence)](RelativeEntropy.md) — `relatedConcept`

## Mathematical formulation

For a finite normalized law p:A→ℝ≥0, H(p)=−Σ\_a p(a)log₂p(a), using 0·log₂0=0. Values are exact reals and the unit is bits.

**Lean formulation** (in its source module context):

```lean
abbrev ShannonEntropy := @Information.entropy
```

**Source:** [`Catalog.ShannonEntropy`](../lean/Catalog/InformationTheory.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Exact normalized real Law on a finite alphabet; entropy is the negative sum of mass times log base 2.

**Limits:** No entropy inequalities or source coding theorem witness. These are model bindings, not proofs of the catalog theorems.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** H(p)=−Σ{x | p(x)>0} p(x)log₂p(x).

**basisKind:** extensional-structural-definition

**basisScope:** Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding.

**verificationObligation:** Map alphabets, exact arithmetic, equality, logarithm base, channel model and error criterion before use.; Retrieve explicit premises; category and specialization links do not inherit claims.

**reviewStatus:** Editorial mathematical review; Lean models are explicitly scoped and theorem sketches are not compiled proofs.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-ShannonEntropy-entropy"></a>

### entropy

`urn:csabs:operation/ShannonEntropy-entropy`

**signature:** H : Dist(A) → ℝ

**description:** Evaluate the finite entropy sum, omitting zero masses.

**precondition:** Inputs satisfy the concept profile.

**totality:** Total on the stated domain.

**postcondition:** Evaluate the finite entropy sum, omitting zero masses.

**source:** [Yury Polyanskiy, MIT 6.441 (2016), Chapter 1: Information measures: entropy and divergence](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/2243edffb30f57181ed97dcb77691580_MIT6_441S16_chapter_1.pdf); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §1.1, Definitions 1.1–1.2 and Theorem 1.1

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-ShannonEntropy-entropy-equation"></a>

### entropy-equation

`urn:csabs:axiom/ShannonEntropy-entropy-equation`

**statement:** H(p)=−Σ{x | p(x)>0} p(x)log₂p(x).

**formalStatement:** H(p)=−Σ{x | p(x)>0} p(x)log₂p(x).

**assumptions:** Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding.

**ruleRole:** defining-rule

**reviewStatus:** Sourced structural definition, not an independent foundational axiom.

**source:** [Yury Polyanskiy, MIT 6.441 (2016), Chapter 1: Information measures: entropy and divergence](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/2243edffb30f57181ed97dcb77691580_MIT6_441S16_chapter_1.pdf); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §1.1, Definitions 1.1–1.2 and Theorem 1.1

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-ShannonEntropy-entropy-bounds"></a>

### Entropy bounds and maximizing distribution

`urn:csabs:theorem/ShannonEntropy-entropy-bounds`

**statement:** 0≤H(p)≤log₂|A|; H(p)=0 iff p is a point mass; H(p)=log₂|A| iff p is uniform.

**formalStatement:** 0≤H(p)≤log₂|A|; H(p)=0 iff p is a point mass; H(p)=log₂|A| iff p is uniform.

**assumptions:** Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding.

**dependsOn:** [entropy-equation](ShannonEntropy.md#node-urn-csabs-axiom-ShannonEntropy-entropy-equation)

**proofSketch:** Nonnegative summands give the lower bound and its equality case. Apply the logarithm inequality to p versus the uniform distribution for the upper bound and equality.

**reviewStatus:** Editorial proof sketch; no registered Lean theorem witness.

**source:** [Yury Polyanskiy, MIT 6.441 (2016), Chapter 1: Information measures: entropy and divergence](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/2243edffb30f57181ed97dcb77691580_MIT6_441S16_chapter_1.pdf); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §1.1, Definitions 1.1–1.2 and Theorem 1.1

**sourceNote:** Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.

**provenanceKind:** derived

<a id="node-urn-csabs-theorem-ShannonEntropy-source-coding"></a>

### Shannon fixed-length source coding theorem

`urn:csabs:theorem/ShannonEntropy-source-coding`

**statement:** For iid X₁,…,Xₙ∼p and R>H(p), there are encoders fₙ:Aⁿ→[Mₙ] and decoders gₙ with limsup log₂(Mₙ)/n≤R and Pr[gₙ(fₙ(Xⁿ))≠Xⁿ]→0. Any such vanishing-error sequence has liminf log₂(Mₙ)/n≥H(p).

**formalStatement:** For iid X₁,…,Xₙ∼p and R>H(p), there are encoders fₙ:Aⁿ→[Mₙ] and decoders gₙ with limsup log₂(Mₙ)/n≤R and Pr[gₙ(fₙ(Xⁿ))≠Xⁿ]→0. Any such vanishing-error sequence has liminf log₂(Mₙ)/n≥H(p).

**assumptions:** Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding.; Source symbols are independent and identically distributed; Mₙ≥1; average block error, unconstrained deterministic compression.

**dependsOn:** [entropy-equation](ShannonEntropy.md#node-urn-csabs-axiom-ShannonEntropy-entropy-equation)

**proofSketch:** Encode a typical set and declare errors outside it; its probability tends to one by the law of large numbers for self-information. Conversely any set of ≤Mₙ recovered words below the entropy rate has vanishing probability.

**reviewStatus:** Editorial proof sketch; no registered Lean theorem witness.

**source:** [Yury Polyanskiy, MIT 6.441 (2016), Chapter 7: Fixed-length almost lossless compression](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/85014cb1add9f415ef38f60f678f16b2_MIT6_441S16_chapter_7.pdf); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §7.1, fixed-length compression bounds and iid specialization

**sourceNote:** Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.

**provenanceKind:** derived

## Concept provenance

- [Yury Polyanskiy, MIT 6.441 (2016), Chapter 1: Information measures: entropy and divergence](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/2243edffb30f57181ed97dcb77691580_MIT6_441S16_chapter_1.pdf); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §1.1, Definitions 1.1–1.2 and Theorem 1.1

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/ShannonEntropy",
    "type": "Concept",
    "shortForm": "ShannonEntropy",
    "fullName": "Shannon entropy (finite discrete profile)",
    "category": [
      "urn:csabs:category/information-theory"
    ],
    "kind": "urn:csabs:kind/function",
    "definition": "Expected self-information of a finite distribution.",
    "notation": "H(p)=−Σx p(x)log₂p(x)",
    "requiresConcept": [
      "urn:csabs:concept/FiniteDistribution",
      "urn:csabs:concept/RandomVariable"
    ],
    "relatedConcept": [
      "urn:csabs:concept/RelativeEntropy"
    ],
    "hasOperation": [
      "urn:csabs:operation/ShannonEntropy-entropy"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/ShannonEntropy-entropy-equation"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/ShannonEntropy-entropy-bounds",
      "urn:csabs:theorem/ShannonEntropy-source-coding"
    ],
    "axiomBasis": "H(p)=−Σ{x | p(x)>0} p(x)log₂p(x).",
    "basisKind": "extensional-structural-definition",
    "basisScope": "Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial mathematical review; Lean models are explicitly scoped and theorem sketches are not compiled proofs.",
    "verificationObligation": [
      "Map alphabets, exact arithmetic, equality, logarithm base, channel model and error criterion before use.",
      "Retrieve explicit premises; category and specialization links do not inherit claims."
    ],
    "source": [
      "urn:csabs:source/mit-information-1"
    ],
    "sourceLocator": "§1.1, Definitions 1.1–1.2 and Theorem 1.1",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted",
    "leanFormulation": "abbrev ShannonEntropy := @Information.entropy",
    "formulationSource": "urn:csabs:source/local-lean-InformationTheory",
    "formulationLocator": "Catalog.ShannonEntropy",
    "formulationScope": "model",
    "leanModelMapping": "Exact normalized real Law on a finite alphabet; entropy is the negative sum of mass times log base 2.",
    "leanModelLimitations": "No entropy inequalities or source coding theorem witness. These are model bindings, not proofs of the catalog theorems.",
    "mathematicalFormulation": "For a finite normalized law p:A→ℝ≥0, H(p)=−Σ_a p(a)log₂p(a), using 0·log₂0=0. Values are exact reals and the unit is bits."
  },
  {
    "id": "urn:csabs:operation/ShannonEntropy-entropy",
    "type": "Operation",
    "name": "entropy",
    "signature": "H : Dist(A) → ℝ",
    "description": "Evaluate the finite entropy sum, omitting zero masses.",
    "concept": "urn:csabs:concept/ShannonEntropy",
    "precondition": "Inputs satisfy the concept profile.",
    "totality": "Total on the stated domain.",
    "postcondition": "Evaluate the finite entropy sum, omitting zero masses.",
    "source": [
      "urn:csabs:source/mit-information-1"
    ],
    "sourceLocator": "§1.1, Definitions 1.1–1.2 and Theorem 1.1",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/ShannonEntropy-entropy-equation",
    "type": "Axiom",
    "name": "entropy-equation",
    "statement": "H(p)=−Σ{x | p(x)>0} p(x)log₂p(x).",
    "formalStatement": "H(p)=−Σ{x | p(x)>0} p(x)log₂p(x).",
    "assumptions": [
      "Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding."
    ],
    "appliesTo": [
      "urn:csabs:concept/ShannonEntropy"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Sourced structural definition, not an independent foundational axiom.",
    "source": [
      "urn:csabs:source/mit-information-1"
    ],
    "sourceLocator": "§1.1, Definitions 1.1–1.2 and Theorem 1.1",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:theorem/ShannonEntropy-entropy-bounds",
    "type": "Theorem",
    "name": "Entropy bounds and maximizing distribution",
    "statement": "0≤H(p)≤log₂|A|; H(p)=0 iff p is a point mass; H(p)=log₂|A| iff p is uniform.",
    "formalStatement": "0≤H(p)≤log₂|A|; H(p)=0 iff p is a point mass; H(p)=log₂|A| iff p is uniform.",
    "assumptions": [
      "Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding."
    ],
    "appliesTo": [
      "urn:csabs:concept/ShannonEntropy"
    ],
    "dependsOn": [
      "urn:csabs:axiom/ShannonEntropy-entropy-equation"
    ],
    "proofSketch": "Nonnegative summands give the lower bound and its equality case. Apply the logarithm inequality to p versus the uniform distribution for the upper bound and equality.",
    "reviewStatus": "Editorial proof sketch; no registered Lean theorem witness.",
    "source": [
      "urn:csabs:source/mit-information-1"
    ],
    "sourceLocator": "§1.1, Definitions 1.1–1.2 and Theorem 1.1",
    "sourceNote": "Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/ShannonEntropy-source-coding",
    "type": "Theorem",
    "name": "Shannon fixed-length source coding theorem",
    "statement": "For iid X₁,…,Xₙ∼p and R>H(p), there are encoders fₙ:Aⁿ→[Mₙ] and decoders gₙ with limsup log₂(Mₙ)/n≤R and Pr[gₙ(fₙ(Xⁿ))≠Xⁿ]→0. Any such vanishing-error sequence has liminf log₂(Mₙ)/n≥H(p).",
    "formalStatement": "For iid X₁,…,Xₙ∼p and R>H(p), there are encoders fₙ:Aⁿ→[Mₙ] and decoders gₙ with limsup log₂(Mₙ)/n≤R and Pr[gₙ(fₙ(Xⁿ))≠Xⁿ]→0. Any such vanishing-error sequence has liminf log₂(Mₙ)/n≥H(p).",
    "assumptions": [
      "Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding.",
      "Source symbols are independent and identically distributed; Mₙ≥1; average block error, unconstrained deterministic compression."
    ],
    "appliesTo": [
      "urn:csabs:concept/ShannonEntropy"
    ],
    "dependsOn": [
      "urn:csabs:axiom/ShannonEntropy-entropy-equation"
    ],
    "proofSketch": "Encode a typical set and declare errors outside it; its probability tends to one by the law of large numbers for self-information. Conversely any set of ≤Mₙ recovered words below the entropy rate has vanishing probability.",
    "reviewStatus": "Editorial proof sketch; no registered Lean theorem witness.",
    "source": [
      "urn:csabs:source/mit-information-7"
    ],
    "sourceLocator": "§7.1, fixed-length compression bounds and iid specialization",
    "sourceNote": "Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
