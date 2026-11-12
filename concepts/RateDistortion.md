# Rate–distortion function (finite iid source, average cost)

Minimum mutual information among reconstruction kernels meeting an expected distortion budget.

**Notation:** Rₚ(D)=inf{V: EₚV[d(X,Z)]≤D} IₚV(X;Z)

**Stable ID:** `urn:csabs:concept/RateDistortion`

**Categories:** Information theory → Coding theory → Source coding

**Kind:** Function

**Prerequisites:** [Finite single-letter distortion measure](DistortionMeasure.md), [Mutual information (finite discrete profile)](MutualInformation.md), [Finite stochastic channel](StochasticChannel.md)

**Related concepts:** [Channel capacity (finite DMC, vanishing error)](ChannelCapacity.md)

## Backlinks

- [Channel capacity (finite DMC, vanishing error)](ChannelCapacity.md) — `relatedConcept`

## Mathematical formulation

For finite source law p, nonnegative distortion d and budget D, R\_I(D)=inf{I(p,W) | W:A→Law(B), Σ\_{a,b}p(a)W(b|a)d(a,b)≤D}, valued in [0,+∞] with inf∅=+∞. The Lean binding uses ENNReal.ofReal on mutual information; nonnegativity and equality to operational rate are separate targets.

**Lean formulation** (in its source module context):

```lean
def informationRD (p : Law A) (d : Cost A B) (D : ℝ) : ℝ≥0∞ :=
  sInf {r | ∃ w : Channel A B, kernelCost p d w ≤ D ∧
    r = ENNReal.ofReal (mutualInformation (joint p w))}
```

**Source:** [`Catalog.Information.informationRD`](../lean/Catalog/InformationTheoryStatements.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Extended-nonnegative-real infimum of mutual information over actual normalized reconstruction kernels meeting kernelCost≤D; inf ∅=∞. Separate operationalRD uses iid source blocks, deterministic lossy codes and eventual upper bounds on rate and expected average distortion. Instantiate D≥0 and finite nonempty alphabets.

**Limits:** Monotonicity/convexity and Shannon rate-distortion equality are formulated but unproved. ENNReal.ofReal encodes nonnegative information values; general MI nonnegativity remains an explicit unproved target.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Rₚ(D)=inf{I(X;Z): pXZ(x,z)=p(x)V(z|x), V a normalized kernel, Σxz p(x)V(z|x)d(x,z)≤D}; inf ∅=+∞.

**basisKind:** extensional-structural-definition

**basisScope:** Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. Source law p fixed; finite nonnegative d; D≥0; infeasible infimum is +∞. Operational codes use iid source blocks and asymptotic expected average distortion, not an excess-distortion or worst-case criterion.

**verificationObligation:** Map alphabets, exact arithmetic, equality, logarithm base, channel model and error criterion before use.; Retrieve explicit premises; category and specialization links do not inherit claims.

**reviewStatus:** Editorial mathematical review; Lean models are explicitly scoped and theorem sketches are not compiled proofs.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-RateDistortion-rate-distortion"></a>

### rate-distortion

`urn:csabs:operation/RateDistortion-rate-distortion`

**signature:** R : Dist(A)×Cost(A,Â)×ℝ≥0 → ℝ∪{+∞}

**description:** Minimize mutual information over finite stochastic kernels V: A→Dist(Â) meeting the expected cost budget.

**precondition:** Inputs satisfy the concept profile.

**totality:** Total on the stated domain.

**postcondition:** Minimize mutual information over finite stochastic kernels V: A→Dist(Â) meeting the expected cost budget.

**source:** [Yury Polyanskiy, MIT 6.441 (2016), Chapter 23: Rate-distortion theory](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/880c39878ba7dc35a5fbb35758d42a69_MIT6_441S16_chapter_23.pdf); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** Theorem 23.2; Theorem 23.3; single-letter information distortion function

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-RateDistortion-constrained-information"></a>

### constrained-information

`urn:csabs:axiom/RateDistortion-constrained-information`

**statement:** Rₚ(D)=inf{I(X;Z): pXZ(x,z)=p(x)V(z|x), V a normalized kernel, Σxz p(x)V(z|x)d(x,z)≤D}; inf ∅=+∞.

**formalStatement:** Rₚ(D)=inf{I(X;Z): pXZ(x,z)=p(x)V(z|x), V a normalized kernel, Σxz p(x)V(z|x)d(x,z)≤D}; inf ∅=+∞.

**assumptions:** Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. Source law p fixed; finite nonnegative d; D≥0; infeasible infimum is +∞. Operational codes use iid source blocks and asymptotic expected average distortion, not an excess-distortion or worst-case criterion.

**ruleRole:** defining-rule

**reviewStatus:** Sourced structural definition, not an independent foundational axiom.

**source:** [Yury Polyanskiy, MIT 6.441 (2016), Chapter 23: Rate-distortion theory](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/880c39878ba7dc35a5fbb35758d42a69_MIT6_441S16_chapter_23.pdf); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** Theorem 23.2; Theorem 23.3; single-letter information distortion function

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-RateDistortion-monotone-convex"></a>

### Rate–distortion monotonicity and convexity

`urn:csabs:theorem/RateDistortion-monotone-convex`

**statement:** Rₚ is non-increasing and convex in D on its extended-real domain.

**formalStatement:** Rₚ is non-increasing and convex in D on its extended-real domain.

**assumptions:** Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. Source law p fixed; finite nonnegative d; D≥0; infeasible infimum is +∞. Operational codes use iid source blocks and asymptotic expected average distortion, not an excess-distortion or worst-case criterion.

**dependsOn:** [constrained-information](RateDistortion.md#node-urn-csabs-axiom-RateDistortion-constrained-information)

**proofSketch:** Increasing D enlarges the feasible set. Mix feasible kernels; distortion is affine and mutual information is convex in the reconstruction kernel for fixed p. Taking infima proves convexity.

**reviewStatus:** Editorial proof sketch; no registered Lean theorem witness.

**source:** [Yury Polyanskiy, MIT 6.441 (2016), Chapter 23: Rate-distortion theory](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/880c39878ba7dc35a5fbb35758d42a69_MIT6_441S16_chapter_23.pdf); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** Theorem 23.2; Theorem 23.3; single-letter information distortion function

**sourceNote:** Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.

**provenanceKind:** derived

<a id="node-urn-csabs-theorem-RateDistortion-shannon-lossy"></a>

### Shannon rate–distortion theorem

`urn:csabs:theorem/RateDistortion-shannon-lossy`

**statement:** For iid source p and D>Dmin=Σx p(x)minz d(x,z), Rₚ(D) equals inf{limsup log₂Mₙ/n: deterministic fₙ:Aⁿ→[Mₙ], gₙ:[Mₙ]→Âⁿ, limsup E[dₙ(Xⁿ,gₙ(fₙ(Xⁿ)))]≤D}.

**formalStatement:** For iid source p and D>Dmin=Σx p(x)minz d(x,z), Rₚ(D) equals inf{limsup log₂Mₙ/n: deterministic fₙ:Aⁿ→[Mₙ], gₙ:[Mₙ]→Âⁿ, limsup E[dₙ(Xⁿ,gₙ(fₙ(Xⁿ)))]≤D}.

**assumptions:** Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. Source law p fixed; finite nonnegative d; D≥0; infeasible infimum is +∞. Operational codes use iid source blocks and asymptotic expected average distortion, not an excess-distortion or worst-case criterion.; Finite alphabets, iid p, finite bounded costs; D>Dmin; deterministic fixed-length codes, expected distortion with asymptotic limsup. No boundary-Dmin achievability statement is recorded here.

**dependsOn:** [constrained-information](RateDistortion.md#node-urn-csabs-axiom-RateDistortion-constrained-information); [Expected separable distortion](DistortionMeasure.md#node-urn-csabs-law-DistortionMeasure-expected-block); [Data processing inequality](MutualInformation.md#node-urn-csabs-theorem-MutualInformation-data-processing); [Rate–distortion monotonicity and convexity](RateDistortion.md#node-urn-csabs-theorem-RateDistortion-monotone-convex)

**proofSketch:** The converse bounds log₂Mₙ below I(Xⁿ;Zⁿ), then uses iid single-letterization and convexity. Achievability uses a random reconstruction codebook from a feasible test channel, joint typicality and a bounded default reconstruction.

**reviewStatus:** Editorial proof sketch; no registered Lean theorem witness.

**source:** [Yury Polyanskiy, MIT 6.441 (2016), Chapter 23: Rate-distortion theory](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/880c39878ba7dc35a5fbb35758d42a69_MIT6_441S16_chapter_23.pdf); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements; [Yury Polyanskiy, MIT 6.441 (2016), Chapter 24: Rate-distortion achievability](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/aaa8d18ddecde45f97134d3f3dcee4a3_MIT6_441S16_chapter_24.pdf); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** Chapter 23 Theorem 23.2; Chapter 24 Theorem 24.2

**sourceNote:** Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.

**provenanceKind:** derived

## Concept provenance

- [Yury Polyanskiy, MIT 6.441 (2016), Chapter 23: Rate-distortion theory](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/880c39878ba7dc35a5fbb35758d42a69_MIT6_441S16_chapter_23.pdf); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** Theorem 23.2; Theorem 23.3; single-letter information distortion function

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/RateDistortion",
    "type": "Concept",
    "shortForm": "RateDistortion",
    "fullName": "Rate–distortion function (finite iid source, average cost)",
    "category": [
      "urn:csabs:category/source-coding"
    ],
    "kind": "urn:csabs:kind/function",
    "definition": "Minimum mutual information among reconstruction kernels meeting an expected distortion budget.",
    "notation": "Rₚ(D)=inf{V: EₚV[d(X,Z)]≤D} IₚV(X;Z)",
    "requiresConcept": [
      "urn:csabs:concept/DistortionMeasure",
      "urn:csabs:concept/MutualInformation",
      "urn:csabs:concept/StochasticChannel"
    ],
    "relatedConcept": [
      "urn:csabs:concept/ChannelCapacity"
    ],
    "hasOperation": [
      "urn:csabs:operation/RateDistortion-rate-distortion"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/RateDistortion-constrained-information"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/RateDistortion-monotone-convex",
      "urn:csabs:theorem/RateDistortion-shannon-lossy"
    ],
    "axiomBasis": "Rₚ(D)=inf{I(X;Z): pXZ(x,z)=p(x)V(z|x), V a normalized kernel, Σxz p(x)V(z|x)d(x,z)≤D}; inf ∅=+∞.",
    "basisKind": "extensional-structural-definition",
    "basisScope": "Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. Source law p fixed; finite nonnegative d; D≥0; infeasible infimum is +∞. Operational codes use iid source blocks and asymptotic expected average distortion, not an excess-distortion or worst-case criterion.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial mathematical review; Lean models are explicitly scoped and theorem sketches are not compiled proofs.",
    "verificationObligation": [
      "Map alphabets, exact arithmetic, equality, logarithm base, channel model and error criterion before use.",
      "Retrieve explicit premises; category and specialization links do not inherit claims."
    ],
    "source": [
      "urn:csabs:source/mit-information-23"
    ],
    "sourceLocator": "Theorem 23.2; Theorem 23.3; single-letter information distortion function",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted",
    "leanFormulation": "def informationRD (p : Law A) (d : Cost A B) (D : ℝ) : ℝ≥0∞ :=\n  sInf {r | ∃ w : Channel A B, kernelCost p d w ≤ D ∧\n    r = ENNReal.ofReal (mutualInformation (joint p w))}",
    "formulationSource": "urn:csabs:source/local-lean-InformationTheoryStatements",
    "formulationLocator": "Catalog.Information.informationRD",
    "formulationScope": "model",
    "leanModelMapping": "Extended-nonnegative-real infimum of mutual information over actual normalized reconstruction kernels meeting kernelCost≤D; inf ∅=∞. Separate operationalRD uses iid source blocks, deterministic lossy codes and eventual upper bounds on rate and expected average distortion. Instantiate D≥0 and finite nonempty alphabets.",
    "leanModelLimitations": "Monotonicity/convexity and Shannon rate-distortion equality are formulated but unproved. ENNReal.ofReal encodes nonnegative information values; general MI nonnegativity remains an explicit unproved target.",
    "mathematicalFormulation": "For finite source law p, nonnegative distortion d and budget D, R_I(D)=inf{I(p,W) | W:A→Law(B), Σ_{a,b}p(a)W(b|a)d(a,b)≤D}, valued in [0,+∞] with inf∅=+∞. The Lean binding uses ENNReal.ofReal on mutual information; nonnegativity and equality to operational rate are separate targets."
  },
  {
    "id": "urn:csabs:operation/RateDistortion-rate-distortion",
    "type": "Operation",
    "name": "rate-distortion",
    "signature": "R : Dist(A)×Cost(A,Â)×ℝ≥0 → ℝ∪{+∞}",
    "description": "Minimize mutual information over finite stochastic kernels V: A→Dist(Â) meeting the expected cost budget.",
    "concept": "urn:csabs:concept/RateDistortion",
    "precondition": "Inputs satisfy the concept profile.",
    "totality": "Total on the stated domain.",
    "postcondition": "Minimize mutual information over finite stochastic kernels V: A→Dist(Â) meeting the expected cost budget.",
    "source": [
      "urn:csabs:source/mit-information-23"
    ],
    "sourceLocator": "Theorem 23.2; Theorem 23.3; single-letter information distortion function",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/RateDistortion-constrained-information",
    "type": "Axiom",
    "name": "constrained-information",
    "statement": "Rₚ(D)=inf{I(X;Z): pXZ(x,z)=p(x)V(z|x), V a normalized kernel, Σxz p(x)V(z|x)d(x,z)≤D}; inf ∅=+∞.",
    "formalStatement": "Rₚ(D)=inf{I(X;Z): pXZ(x,z)=p(x)V(z|x), V a normalized kernel, Σxz p(x)V(z|x)d(x,z)≤D}; inf ∅=+∞.",
    "assumptions": [
      "Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. Source law p fixed; finite nonnegative d; D≥0; infeasible infimum is +∞. Operational codes use iid source blocks and asymptotic expected average distortion, not an excess-distortion or worst-case criterion."
    ],
    "appliesTo": [
      "urn:csabs:concept/RateDistortion"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Sourced structural definition, not an independent foundational axiom.",
    "source": [
      "urn:csabs:source/mit-information-23"
    ],
    "sourceLocator": "Theorem 23.2; Theorem 23.3; single-letter information distortion function",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:theorem/RateDistortion-monotone-convex",
    "type": "Theorem",
    "name": "Rate–distortion monotonicity and convexity",
    "statement": "Rₚ is non-increasing and convex in D on its extended-real domain.",
    "formalStatement": "Rₚ is non-increasing and convex in D on its extended-real domain.",
    "assumptions": [
      "Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. Source law p fixed; finite nonnegative d; D≥0; infeasible infimum is +∞. Operational codes use iid source blocks and asymptotic expected average distortion, not an excess-distortion or worst-case criterion."
    ],
    "appliesTo": [
      "urn:csabs:concept/RateDistortion"
    ],
    "dependsOn": [
      "urn:csabs:axiom/RateDistortion-constrained-information"
    ],
    "proofSketch": "Increasing D enlarges the feasible set. Mix feasible kernels; distortion is affine and mutual information is convex in the reconstruction kernel for fixed p. Taking infima proves convexity.",
    "reviewStatus": "Editorial proof sketch; no registered Lean theorem witness.",
    "source": [
      "urn:csabs:source/mit-information-23"
    ],
    "sourceLocator": "Theorem 23.2; Theorem 23.3; single-letter information distortion function",
    "sourceNote": "Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/RateDistortion-shannon-lossy",
    "type": "Theorem",
    "name": "Shannon rate–distortion theorem",
    "statement": "For iid source p and D>Dmin=Σx p(x)minz d(x,z), Rₚ(D) equals inf{limsup log₂Mₙ/n: deterministic fₙ:Aⁿ→[Mₙ], gₙ:[Mₙ]→Âⁿ, limsup E[dₙ(Xⁿ,gₙ(fₙ(Xⁿ)))]≤D}.",
    "formalStatement": "For iid source p and D>Dmin=Σx p(x)minz d(x,z), Rₚ(D) equals inf{limsup log₂Mₙ/n: deterministic fₙ:Aⁿ→[Mₙ], gₙ:[Mₙ]→Âⁿ, limsup E[dₙ(Xⁿ,gₙ(fₙ(Xⁿ)))]≤D}.",
    "assumptions": [
      "Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. Source law p fixed; finite nonnegative d; D≥0; infeasible infimum is +∞. Operational codes use iid source blocks and asymptotic expected average distortion, not an excess-distortion or worst-case criterion.",
      "Finite alphabets, iid p, finite bounded costs; D>Dmin; deterministic fixed-length codes, expected distortion with asymptotic limsup. No boundary-Dmin achievability statement is recorded here."
    ],
    "appliesTo": [
      "urn:csabs:concept/RateDistortion"
    ],
    "dependsOn": [
      "urn:csabs:axiom/RateDistortion-constrained-information",
      "urn:csabs:law/DistortionMeasure-expected-block",
      "urn:csabs:theorem/MutualInformation-data-processing",
      "urn:csabs:theorem/RateDistortion-monotone-convex"
    ],
    "proofSketch": "The converse bounds log₂Mₙ below I(Xⁿ;Zⁿ), then uses iid single-letterization and convexity. Achievability uses a random reconstruction codebook from a feasible test channel, joint typicality and a bounded default reconstruction.",
    "reviewStatus": "Editorial proof sketch; no registered Lean theorem witness.",
    "source": [
      "urn:csabs:source/mit-information-23",
      "urn:csabs:source/mit-information-24"
    ],
    "sourceLocator": "Chapter 23 Theorem 23.2; Chapter 24 Theorem 24.2",
    "sourceNote": "Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
