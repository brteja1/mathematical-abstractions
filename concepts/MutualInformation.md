# Mutual information (finite discrete profile)

Divergence of a joint law from the product of its marginals.

**Notation:** I(X;Y)=D(pXY∥pX⊗pY)

**Stable ID:** `urn:csabs:concept/MutualInformation`

**Categories:** Information theory

**Kind:** Function

**Prerequisites:** [Relative entropy (finite Kullback–Leibler divergence)](RelativeEntropy.md), [Conditional entropy (finite discrete profile)](ConditionalEntropy.md)

## Backlinks

- [Channel capacity (finite DMC, vanishing error)](ChannelCapacity.md) — `requiresConcept`
- [Rate–distortion function (finite iid source, average cost)](RateDistortion.md) — `requiresConcept`

## Mathematical formulation

For finite joint p with marginals p\_A,p\_B, I(A;B)=Σ\_{a,b}p(a,b)log₂(p(a,b)/(p\_A(a)p\_B(b))). Zero joint masses contribute 0; the unit is bits.

**Lean formulation** (in its source module context):

```lean
abbrev MutualInformation := @Information.mutualInformation
```

**Source:** [`Catalog.MutualInformation`](../lean/Catalog/InformationTheory.lean); consulted 2026-11-12.

**Scope:** partial

**Interpretation:** Finite joint law and marginal-product log ratio in bits.

**Limits:** Conditional mutual information operation and data processing theorem are not formalized. These are model bindings, not proofs of the catalog theorems.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** I(X;Y)=D(pXY∥pX⊗pY); I(X;Y|Z)=Σ{z:pZ(z)>0}pZ(z)D(pXY|z∥pX|z⊗pY|z).

**basisKind:** extensional-structural-definition

**basisScope:** Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding.

**verificationObligation:** Map alphabets, exact arithmetic, equality, logarithm base, channel model and error criterion before use.; Retrieve explicit premises; category and specialization links do not inherit claims.

**reviewStatus:** Editorial mathematical review; Lean models are explicitly scoped and theorem sketches are not compiled proofs.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-MutualInformation-mutual-information"></a>

### mutual-information

`urn:csabs:operation/MutualInformation-mutual-information`

**signature:** I : Dist(A×B) → ℝ

**description:** Evaluate divergence from the product marginals; finite because positive joint mass implies positive marginals.

**precondition:** Inputs satisfy the concept profile.

**totality:** Total on the stated domain.

**postcondition:** Evaluate divergence from the product marginals; finite because positive joint mass implies positive marginals.

**source:** [Yury Polyanskiy, MIT 6.441 (2016), Chapter 2: Information measures: mutual information](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/184197ca5d5418da2415d37e929860b9_MIT6_441S16_chapter_2.pdf); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** Definitions of mutual and conditional mutual information; Theorems 2.4–2.5

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-MutualInformation-conditional-mutual-information"></a>

### conditional-mutual-information

`urn:csabs:operation/MutualInformation-conditional-mutual-information`

**signature:** Icond : Dist(A×B×C) → ℝ

**description:** I(X;Y|Z)=Σ{z:pZ(z)>0}pZ(z)D(pXY|z∥pX|z⊗pY|z).

**precondition:** Inputs satisfy the concept profile.

**totality:** Total on the stated domain.

**postcondition:** I(X;Y|Z)=Σ{z:pZ(z)>0}pZ(z)D(pXY|z∥pX|z⊗pY|z).

**source:** [Yury Polyanskiy, MIT 6.441 (2016), Chapter 2: Information measures: mutual information](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/184197ca5d5418da2415d37e929860b9_MIT6_441S16_chapter_2.pdf); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** Definitions of mutual and conditional mutual information; Theorems 2.4–2.5

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-MutualInformation-information-equations"></a>

### information-equations

`urn:csabs:axiom/MutualInformation-information-equations`

**statement:** I(X;Y)=D(pXY∥pX⊗pY); I(X;Y|Z)=Σ{z:pZ(z)>0}pZ(z)D(pXY|z∥pX|z⊗pY|z).

**formalStatement:** I(X;Y)=D(pXY∥pX⊗pY); I(X;Y|Z)=Σ{z:pZ(z)>0}pZ(z)D(pXY|z∥pX|z⊗pY|z).

**assumptions:** Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding.

**ruleRole:** defining-rule

**reviewStatus:** Sourced structural definition, not an independent foundational axiom.

**source:** [Yury Polyanskiy, MIT 6.441 (2016), Chapter 2: Information measures: mutual information](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/184197ca5d5418da2415d37e929860b9_MIT6_441S16_chapter_2.pdf); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** Definitions of mutual and conditional mutual information; Theorems 2.4–2.5

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-MutualInformation-entropy-identity"></a>

### Mutual information entropy identities

`urn:csabs:theorem/MutualInformation-entropy-identity`

**statement:** I(X;Y)=H(X)+H(Y)−H(X,Y)=H(X)−H(X|Y); I(X;Y)≥0, with equality iff X and Y are independent.

**formalStatement:** I(X;Y)=H(X)+H(Y)−H(X,Y)=H(X)−H(X|Y); I(X;Y)≥0, with equality iff X and Y are independent.

**assumptions:** Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding.

**dependsOn:** [information-equations](MutualInformation.md#node-urn-csabs-axiom-MutualInformation-information-equations); [divergence-equation](RelativeEntropy.md#node-urn-csabs-axiom-RelativeEntropy-divergence-equation); [entropy-equation](ShannonEntropy.md#node-urn-csabs-axiom-ShannonEntropy-entropy-equation); [Entropy chain rule](ConditionalEntropy.md#node-urn-csabs-law-ConditionalEntropy-chain-rule); [Gibbs inequality](RelativeEntropy.md#node-urn-csabs-theorem-RelativeEntropy-gibbs)

**proofSketch:** Expand the divergence logarithm, sum each marginal term, apply the entropy chain rule and Gibbs inequality.

**reviewStatus:** Editorial proof sketch; no registered Lean theorem witness.

**source:** [Yury Polyanskiy, MIT 6.441 (2016), Chapter 2: Information measures: mutual information](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/184197ca5d5418da2415d37e929860b9_MIT6_441S16_chapter_2.pdf); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** Definitions of mutual and conditional mutual information; Theorems 2.4–2.5

**sourceNote:** Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.

**provenanceKind:** derived

<a id="node-urn-csabs-theorem-MutualInformation-data-processing"></a>

### Data processing inequality

`urn:csabs:theorem/MutualInformation-data-processing`

**statement:** If X→Y→Z is a Markov chain, then I(X;Z)≤I(X;Y).

**formalStatement:** If X→Y→Z is a Markov chain, then I(X;Z)≤I(X;Y).

**assumptions:** Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding.; Joint law factors as pX(x)W(y|x)V(z|y), including arbitrary rows on null events.

**dependsOn:** [information-equations](MutualInformation.md#node-urn-csabs-axiom-MutualInformation-information-equations); [Gibbs inequality](RelativeEntropy.md#node-urn-csabs-theorem-RelativeEntropy-gibbs); [Entropy chain rule](ConditionalEntropy.md#node-urn-csabs-law-ConditionalEntropy-chain-rule)

**proofSketch:** Expand I(X;Y,Z) in both orders. The Markov factorization makes I(X;Z|Y)=0; nonnegativity of I(X;Y|Z) yields the inequality.

**reviewStatus:** Editorial proof sketch; no registered Lean theorem witness.

**source:** [Yury Polyanskiy, MIT 6.441 (2016), Chapter 2: Information measures: mutual information](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/184197ca5d5418da2415d37e929860b9_MIT6_441S16_chapter_2.pdf); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** Theorem 2.5

**sourceNote:** Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.

**provenanceKind:** derived

## Concept provenance

- [Yury Polyanskiy, MIT 6.441 (2016), Chapter 2: Information measures: mutual information](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/184197ca5d5418da2415d37e929860b9_MIT6_441S16_chapter_2.pdf); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** Definitions of mutual and conditional mutual information; Theorems 2.4–2.5

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/MutualInformation",
    "type": "Concept",
    "shortForm": "MutualInformation",
    "fullName": "Mutual information (finite discrete profile)",
    "category": [
      "urn:csabs:category/information-theory"
    ],
    "kind": "urn:csabs:kind/function",
    "definition": "Divergence of a joint law from the product of its marginals.",
    "notation": "I(X;Y)=D(pXY∥pX⊗pY)",
    "requiresConcept": [
      "urn:csabs:concept/RelativeEntropy",
      "urn:csabs:concept/ConditionalEntropy"
    ],
    "relatedConcept": [],
    "hasOperation": [
      "urn:csabs:operation/MutualInformation-mutual-information",
      "urn:csabs:operation/MutualInformation-conditional-mutual-information"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/MutualInformation-information-equations"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/MutualInformation-entropy-identity",
      "urn:csabs:theorem/MutualInformation-data-processing"
    ],
    "axiomBasis": "I(X;Y)=D(pXY∥pX⊗pY); I(X;Y|Z)=Σ{z:pZ(z)>0}pZ(z)D(pXY|z∥pX|z⊗pY|z).",
    "basisKind": "extensional-structural-definition",
    "basisScope": "Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial mathematical review; Lean models are explicitly scoped and theorem sketches are not compiled proofs.",
    "verificationObligation": [
      "Map alphabets, exact arithmetic, equality, logarithm base, channel model and error criterion before use.",
      "Retrieve explicit premises; category and specialization links do not inherit claims."
    ],
    "source": [
      "urn:csabs:source/mit-information-2"
    ],
    "sourceLocator": "Definitions of mutual and conditional mutual information; Theorems 2.4–2.5",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted",
    "leanFormulation": "abbrev MutualInformation := @Information.mutualInformation",
    "formulationSource": "urn:csabs:source/local-lean-InformationTheory",
    "formulationLocator": "Catalog.MutualInformation",
    "formulationScope": "partial",
    "leanModelMapping": "Finite joint law and marginal-product log ratio in bits.",
    "leanModelLimitations": "Conditional mutual information operation and data processing theorem are not formalized. These are model bindings, not proofs of the catalog theorems.",
    "mathematicalFormulation": "For finite joint p with marginals p_A,p_B, I(A;B)=Σ_{a,b}p(a,b)log₂(p(a,b)/(p_A(a)p_B(b))). Zero joint masses contribute 0; the unit is bits."
  },
  {
    "id": "urn:csabs:operation/MutualInformation-mutual-information",
    "type": "Operation",
    "name": "mutual-information",
    "signature": "I : Dist(A×B) → ℝ",
    "description": "Evaluate divergence from the product marginals; finite because positive joint mass implies positive marginals.",
    "concept": "urn:csabs:concept/MutualInformation",
    "precondition": "Inputs satisfy the concept profile.",
    "totality": "Total on the stated domain.",
    "postcondition": "Evaluate divergence from the product marginals; finite because positive joint mass implies positive marginals.",
    "source": [
      "urn:csabs:source/mit-information-2"
    ],
    "sourceLocator": "Definitions of mutual and conditional mutual information; Theorems 2.4–2.5",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/MutualInformation-conditional-mutual-information",
    "type": "Operation",
    "name": "conditional-mutual-information",
    "signature": "Icond : Dist(A×B×C) → ℝ",
    "description": "I(X;Y|Z)=Σ{z:pZ(z)>0}pZ(z)D(pXY|z∥pX|z⊗pY|z).",
    "concept": "urn:csabs:concept/MutualInformation",
    "precondition": "Inputs satisfy the concept profile.",
    "totality": "Total on the stated domain.",
    "postcondition": "I(X;Y|Z)=Σ{z:pZ(z)>0}pZ(z)D(pXY|z∥pX|z⊗pY|z).",
    "source": [
      "urn:csabs:source/mit-information-2"
    ],
    "sourceLocator": "Definitions of mutual and conditional mutual information; Theorems 2.4–2.5",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/MutualInformation-information-equations",
    "type": "Axiom",
    "name": "information-equations",
    "statement": "I(X;Y)=D(pXY∥pX⊗pY); I(X;Y|Z)=Σ{z:pZ(z)>0}pZ(z)D(pXY|z∥pX|z⊗pY|z).",
    "formalStatement": "I(X;Y)=D(pXY∥pX⊗pY); I(X;Y|Z)=Σ{z:pZ(z)>0}pZ(z)D(pXY|z∥pX|z⊗pY|z).",
    "assumptions": [
      "Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding."
    ],
    "appliesTo": [
      "urn:csabs:concept/MutualInformation"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Sourced structural definition, not an independent foundational axiom.",
    "source": [
      "urn:csabs:source/mit-information-2"
    ],
    "sourceLocator": "Definitions of mutual and conditional mutual information; Theorems 2.4–2.5",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:theorem/MutualInformation-entropy-identity",
    "type": "Theorem",
    "name": "Mutual information entropy identities",
    "statement": "I(X;Y)=H(X)+H(Y)−H(X,Y)=H(X)−H(X|Y); I(X;Y)≥0, with equality iff X and Y are independent.",
    "formalStatement": "I(X;Y)=H(X)+H(Y)−H(X,Y)=H(X)−H(X|Y); I(X;Y)≥0, with equality iff X and Y are independent.",
    "assumptions": [
      "Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding."
    ],
    "appliesTo": [
      "urn:csabs:concept/MutualInformation"
    ],
    "dependsOn": [
      "urn:csabs:axiom/MutualInformation-information-equations",
      "urn:csabs:axiom/RelativeEntropy-divergence-equation",
      "urn:csabs:axiom/ShannonEntropy-entropy-equation",
      "urn:csabs:law/ConditionalEntropy-chain-rule",
      "urn:csabs:theorem/RelativeEntropy-gibbs"
    ],
    "proofSketch": "Expand the divergence logarithm, sum each marginal term, apply the entropy chain rule and Gibbs inequality.",
    "reviewStatus": "Editorial proof sketch; no registered Lean theorem witness.",
    "source": [
      "urn:csabs:source/mit-information-2"
    ],
    "sourceLocator": "Definitions of mutual and conditional mutual information; Theorems 2.4–2.5",
    "sourceNote": "Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/MutualInformation-data-processing",
    "type": "Theorem",
    "name": "Data processing inequality",
    "statement": "If X→Y→Z is a Markov chain, then I(X;Z)≤I(X;Y).",
    "formalStatement": "If X→Y→Z is a Markov chain, then I(X;Z)≤I(X;Y).",
    "assumptions": [
      "Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding.",
      "Joint law factors as pX(x)W(y|x)V(z|y), including arbitrary rows on null events."
    ],
    "appliesTo": [
      "urn:csabs:concept/MutualInformation"
    ],
    "dependsOn": [
      "urn:csabs:axiom/MutualInformation-information-equations",
      "urn:csabs:theorem/RelativeEntropy-gibbs",
      "urn:csabs:law/ConditionalEntropy-chain-rule"
    ],
    "proofSketch": "Expand I(X;Y,Z) in both orders. The Markov factorization makes I(X;Z|Y)=0; nonnegativity of I(X;Y|Z) yields the inequality.",
    "reviewStatus": "Editorial proof sketch; no registered Lean theorem witness.",
    "source": [
      "urn:csabs:source/mit-information-2"
    ],
    "sourceLocator": "Theorem 2.5",
    "sourceNote": "Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
