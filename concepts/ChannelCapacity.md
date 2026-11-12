# Channel capacity (finite DMC, vanishing error)

Largest asymptotically achievable bit rate for unconstrained finite memoryless communication.

**Notation:** C(W)=sup{R: R achievable with Pe,n→0}

**Stable ID:** `urn:csabs:concept/ChannelCapacity`

**Categories:** Information theory

**Kind:** Function

**Prerequisites:** [Discrete memoryless channel (stationary finite profile)](DiscreteMemorylessChannel.md), [Mutual information (finite discrete profile)](MutualInformation.md)

**Related concepts:** [Finite block code (Hamming profile)](BlockCode.md), [Rate–distortion function (finite iid source, average cost)](RateDistortion.md)

## Backlinks

- [Finite block code (Hamming profile)](BlockCode.md) — `relatedConcept`
- [Rate–distortion function (finite iid source, average cost)](RateDistortion.md) — `relatedConcept`

## Mathematical formulation

The selected binding defines operationalCapacity(W)=sup{r∈ℝ | r≥0 ∧ Achievable(W,r)}. Achievable means positive-length channel-code sequences with liminf rate at least r and average decoding error tending to zero. Equality with sup\_p I(p,W) is a separate coding-theorem target.

**Lean formulation** (in its source module context):

```lean
def operationalCapacity (w : Channel A B) : ℝ :=
  sSup {r | 0 ≤ r ∧ Achievable w r}
```

**Source:** [`Catalog.Information.operationalCapacity`](../lean/Catalog/InformationTheoryStatements.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Supremum of nonnegative achievable rates, with explicit ChannelCode sequences, positive message counts, uniform-message average block error, positive block lengths and eventual lower-rate/vanishing-error criteria.

**Limits:** Shannon equality with the information expression and coding theorems are formulated but unproved.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Pe,n=(1/Mₙ)Σm Σ{yⁿ:gₙ(yⁿ)≠m}Wⁿ(yⁿ|fₙ(m)); R is achievable iff some code sequence has liminf log₂Mₙ/n≥R and Pe,n→0; C is the supremum of achievable R≥0.

**basisKind:** extensional-structural-definition

**basisScope:** Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. n≥1, Mₙ≥1 equiprobable messages, deterministic encoder [Mₙ]→Aⁿ and decoder Bⁿ→[Mₙ]; average block error. Achievable R means liminf log₂Mₙ/n≥R and Pe,n→0. No zero-error or finite-block guarantee.

**verificationObligation:** Map alphabets, exact arithmetic, equality, logarithm base, channel model and error criterion before use.; Retrieve explicit premises; category and specialization links do not inherit claims.

**reviewStatus:** Editorial mathematical review; Lean models are explicitly scoped and theorem sketches are not compiled proofs.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-ChannelCapacity-capacity"></a>

### capacity

`urn:csabs:operation/ChannelCapacity-capacity`

**signature:** C : DMC(A,B) → ℝ

**description:** Supremum of asymptotically achievable rates, measured in bits per use.

**precondition:** Inputs satisfy the concept profile.

**totality:** Total on the stated domain.

**postcondition:** Supremum of asymptotically achievable rates, measured in bits per use.

**source:** [Yury Polyanskiy, MIT 6.441 (2016), Chapter 16: Linear codes and channel capacity](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/f417578e714d472cb08d463825e45f03_MIT6_441S16_chapter_16.pdf); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §16.2 capacity definitions; Theorem 16.5 and Proposition 16.3

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-ChannelCapacity-achievable"></a>

### achievable

`urn:csabs:axiom/ChannelCapacity-achievable`

**statement:** Pe,n=(1/Mₙ)Σm Σ{yⁿ:gₙ(yⁿ)≠m}Wⁿ(yⁿ|fₙ(m)); R is achievable iff some code sequence has liminf log₂Mₙ/n≥R and Pe,n→0; C is the supremum of achievable R≥0.

**formalStatement:** Pe,n=(1/Mₙ)Σm Σ{yⁿ:gₙ(yⁿ)≠m}Wⁿ(yⁿ|fₙ(m)); R is achievable iff some code sequence has liminf log₂Mₙ/n≥R and Pe,n→0; C is the supremum of achievable R≥0.

**assumptions:** Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. n≥1, Mₙ≥1 equiprobable messages, deterministic encoder [Mₙ]→Aⁿ and decoder Bⁿ→[Mₙ]; average block error. Achievable R means liminf log₂Mₙ/n≥R and Pe,n→0. No zero-error or finite-block guarantee.

**ruleRole:** defining-rule

**reviewStatus:** Sourced structural definition, not an independent foundational axiom.

**source:** [Yury Polyanskiy, MIT 6.441 (2016), Chapter 16: Linear codes and channel capacity](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/f417578e714d472cb08d463825e45f03_MIT6_441S16_chapter_16.pdf); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §16.2 capacity definitions; Theorem 16.5 and Proposition 16.3

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-ChannelCapacity-shannon"></a>

### Shannon noisy-channel coding theorem

`urn:csabs:theorem/ChannelCapacity-shannon`

**statement:** C(W)=max{pX} I(X;Y), with joint law pX(x)W(y|x). Every 0≤R<C(W) is achievable; any vanishing-error code sequence has limsup log₂Mₙ/n≤C(W).

**formalStatement:** C(W)=max{pX} I(X;Y), with joint law pX(x)W(y|x). Every 0≤R<C(W) is achievable; any vanishing-error code sequence has limsup log₂Mₙ/n≤C(W).

**assumptions:** Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. n≥1, Mₙ≥1 equiprobable messages, deterministic encoder [Mₙ]→Aⁿ and decoder Bⁿ→[Mₙ]; average block error. Achievable R means liminf log₂Mₙ/n≥R and Pe,n→0. No zero-error or finite-block guarantee.; Finite stationary memoryless channel; unconstrained inputs, no feedback; average block error. This is an asymptotic existence result, not a decoder construction or a claim at R=C.

**dependsOn:** [achievable](ChannelCapacity.md#node-urn-csabs-axiom-ChannelCapacity-achievable); [product-law](DiscreteMemorylessChannel.md#node-urn-csabs-axiom-DiscreteMemorylessChannel-product-law); [Data processing inequality](MutualInformation.md#node-urn-csabs-theorem-MutualInformation-data-processing); [Fano inequality](ConditionalEntropy.md#node-urn-csabs-theorem-ConditionalEntropy-fano)

**proofSketch:** For achievability draw codewords iid from an input law with I>R and use information-density decoding and the law of large numbers. For the converse apply Fano, data processing, and I(Xⁿ;Yⁿ)≤Σi I(Xi;Yi)≤n maxp I.

**reviewStatus:** Editorial proof sketch; no registered Lean theorem witness.

**source:** [Yury Polyanskiy, MIT 6.441 (2016), Chapter 16: Linear codes and channel capacity](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/f417578e714d472cb08d463825e45f03_MIT6_441S16_chapter_16.pdf); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §16.2 capacity definitions; Theorem 16.5 and Proposition 16.3

**sourceNote:** Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.

**provenanceKind:** derived

## Concept provenance

- [Yury Polyanskiy, MIT 6.441 (2016), Chapter 16: Linear codes and channel capacity](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/f417578e714d472cb08d463825e45f03_MIT6_441S16_chapter_16.pdf); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §16.2 capacity definitions; Theorem 16.5 and Proposition 16.3

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/ChannelCapacity",
    "type": "Concept",
    "shortForm": "ChannelCapacity",
    "fullName": "Channel capacity (finite DMC, vanishing error)",
    "category": [
      "urn:csabs:category/information-theory"
    ],
    "kind": "urn:csabs:kind/function",
    "definition": "Largest asymptotically achievable bit rate for unconstrained finite memoryless communication.",
    "notation": "C(W)=sup{R: R achievable with Pe,n→0}",
    "requiresConcept": [
      "urn:csabs:concept/DiscreteMemorylessChannel",
      "urn:csabs:concept/MutualInformation"
    ],
    "relatedConcept": [
      "urn:csabs:concept/BlockCode",
      "urn:csabs:concept/RateDistortion"
    ],
    "hasOperation": [
      "urn:csabs:operation/ChannelCapacity-capacity"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/ChannelCapacity-achievable"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/ChannelCapacity-shannon"
    ],
    "axiomBasis": "Pe,n=(1/Mₙ)Σm Σ{yⁿ:gₙ(yⁿ)≠m}Wⁿ(yⁿ|fₙ(m)); R is achievable iff some code sequence has liminf log₂Mₙ/n≥R and Pe,n→0; C is the supremum of achievable R≥0.",
    "basisKind": "extensional-structural-definition",
    "basisScope": "Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. n≥1, Mₙ≥1 equiprobable messages, deterministic encoder [Mₙ]→Aⁿ and decoder Bⁿ→[Mₙ]; average block error. Achievable R means liminf log₂Mₙ/n≥R and Pe,n→0. No zero-error or finite-block guarantee.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial mathematical review; Lean models are explicitly scoped and theorem sketches are not compiled proofs.",
    "verificationObligation": [
      "Map alphabets, exact arithmetic, equality, logarithm base, channel model and error criterion before use.",
      "Retrieve explicit premises; category and specialization links do not inherit claims."
    ],
    "source": [
      "urn:csabs:source/mit-information-16"
    ],
    "sourceLocator": "§16.2 capacity definitions; Theorem 16.5 and Proposition 16.3",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted",
    "leanFormulation": "def operationalCapacity (w : Channel A B) : ℝ :=\n  sSup {r | 0 ≤ r ∧ Achievable w r}",
    "formulationSource": "urn:csabs:source/local-lean-InformationTheoryStatements",
    "formulationLocator": "Catalog.Information.operationalCapacity",
    "formulationScope": "model",
    "leanModelMapping": "Supremum of nonnegative achievable rates, with explicit ChannelCode sequences, positive message counts, uniform-message average block error, positive block lengths and eventual lower-rate/vanishing-error criteria.",
    "leanModelLimitations": "Shannon equality with the information expression and coding theorems are formulated but unproved.",
    "mathematicalFormulation": "The selected binding defines operationalCapacity(W)=sup{r∈ℝ | r≥0 ∧ Achievable(W,r)}. Achievable means positive-length channel-code sequences with liminf rate at least r and average decoding error tending to zero. Equality with sup_p I(p,W) is a separate coding-theorem target."
  },
  {
    "id": "urn:csabs:operation/ChannelCapacity-capacity",
    "type": "Operation",
    "name": "capacity",
    "signature": "C : DMC(A,B) → ℝ",
    "description": "Supremum of asymptotically achievable rates, measured in bits per use.",
    "concept": "urn:csabs:concept/ChannelCapacity",
    "precondition": "Inputs satisfy the concept profile.",
    "totality": "Total on the stated domain.",
    "postcondition": "Supremum of asymptotically achievable rates, measured in bits per use.",
    "source": [
      "urn:csabs:source/mit-information-16"
    ],
    "sourceLocator": "§16.2 capacity definitions; Theorem 16.5 and Proposition 16.3",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/ChannelCapacity-achievable",
    "type": "Axiom",
    "name": "achievable",
    "statement": "Pe,n=(1/Mₙ)Σm Σ{yⁿ:gₙ(yⁿ)≠m}Wⁿ(yⁿ|fₙ(m)); R is achievable iff some code sequence has liminf log₂Mₙ/n≥R and Pe,n→0; C is the supremum of achievable R≥0.",
    "formalStatement": "Pe,n=(1/Mₙ)Σm Σ{yⁿ:gₙ(yⁿ)≠m}Wⁿ(yⁿ|fₙ(m)); R is achievable iff some code sequence has liminf log₂Mₙ/n≥R and Pe,n→0; C is the supremum of achievable R≥0.",
    "assumptions": [
      "Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. n≥1, Mₙ≥1 equiprobable messages, deterministic encoder [Mₙ]→Aⁿ and decoder Bⁿ→[Mₙ]; average block error. Achievable R means liminf log₂Mₙ/n≥R and Pe,n→0. No zero-error or finite-block guarantee."
    ],
    "appliesTo": [
      "urn:csabs:concept/ChannelCapacity"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Sourced structural definition, not an independent foundational axiom.",
    "source": [
      "urn:csabs:source/mit-information-16"
    ],
    "sourceLocator": "§16.2 capacity definitions; Theorem 16.5 and Proposition 16.3",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:theorem/ChannelCapacity-shannon",
    "type": "Theorem",
    "name": "Shannon noisy-channel coding theorem",
    "statement": "C(W)=max{pX} I(X;Y), with joint law pX(x)W(y|x). Every 0≤R<C(W) is achievable; any vanishing-error code sequence has limsup log₂Mₙ/n≤C(W).",
    "formalStatement": "C(W)=max{pX} I(X;Y), with joint law pX(x)W(y|x). Every 0≤R<C(W) is achievable; any vanishing-error code sequence has limsup log₂Mₙ/n≤C(W).",
    "assumptions": [
      "Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. n≥1, Mₙ≥1 equiprobable messages, deterministic encoder [Mₙ]→Aⁿ and decoder Bⁿ→[Mₙ]; average block error. Achievable R means liminf log₂Mₙ/n≥R and Pe,n→0. No zero-error or finite-block guarantee.",
      "Finite stationary memoryless channel; unconstrained inputs, no feedback; average block error. This is an asymptotic existence result, not a decoder construction or a claim at R=C."
    ],
    "appliesTo": [
      "urn:csabs:concept/ChannelCapacity"
    ],
    "dependsOn": [
      "urn:csabs:axiom/ChannelCapacity-achievable",
      "urn:csabs:axiom/DiscreteMemorylessChannel-product-law",
      "urn:csabs:theorem/MutualInformation-data-processing",
      "urn:csabs:theorem/ConditionalEntropy-fano"
    ],
    "proofSketch": "For achievability draw codewords iid from an input law with I>R and use information-density decoding and the law of large numbers. For the converse apply Fano, data processing, and I(Xⁿ;Yⁿ)≤Σi I(Xi;Yi)≤n maxp I.",
    "reviewStatus": "Editorial proof sketch; no registered Lean theorem witness.",
    "source": [
      "urn:csabs:source/mit-information-16"
    ],
    "sourceLocator": "§16.2 capacity definitions; Theorem 16.5 and Proposition 16.3",
    "sourceNote": "Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
