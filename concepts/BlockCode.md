# Finite block code (Hamming profile)

Nonempty codebook of fixed-length words, with encoding and decoding interfaces kept separate from the set.

**Notation:** ∅≠C⊆Σⁿ; M=|C|; dmin(C)=min{x≠y in C}dH(x,y)

**Stable ID:** `urn:csabs:concept/BlockCode`

**Categories:** Information theory → Coding theory → Channel coding

**Kind:** Mathematical structure

**Prerequisites:** [Hamming space (finite fixed-length words)](HammingSpace.md), [Finite set collection](FiniteSet.md), [Total function](Function.md)

**Related concepts:** [Channel capacity (finite DMC, vanishing error)](ChannelCapacity.md)

## Backlinks

- [Channel capacity (finite DMC, vanishing error)](ChannelCapacity.md) — `relatedConcept`
- [Linear block code over a finite field](LinearBlockCode.md) — `requiresConcept`
- [Linear block code over a finite field](LinearBlockCode.md) — `specializationOf`
- [Nonlinear finite-field block code](NonlinearBlockCode.md) — `requiresConcept`
- [Nonlinear finite-field block code](NonlinearBlockCode.md) — `specializationOf`

## Mathematical formulation

A block code is a nonempty finite C⊆A^n with n>0. Equality is set equality of codewords. The selected interface leaves minimum distance undefined when |C|<2.

**Lean formulation** (in its source module context):

```lean
abbrev BlockCode := Information.Code
```

**Source:** [`Catalog.BlockCode`](../lean/Catalog/InformationTheory.lean); consulted 2026-11-12.

**Scope:** partial

**Interpretation:** Nonempty Finset of Fin n→A with positive n. Instantiate a finite alphabet with at least two symbols.

**Limits:** Encoder bijection, nearest-set decoder, failure, distance distribution and partial dmin operations omitted. These are model bindings, not proofs of the catalog theorems.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** C is a nonempty subset of Σⁿ; encode is bijective onto C; nearest(C,y)=argmin{c∈C}dH(c,y); dmin is the distinct-pair minimum only when |C|≥2; δ is a supplied total map to C∪{failure}; Ai counts ordered pairs divided by |C|.

**basisKind:** extensional-structural-definition

**basisScope:** Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state. M≥1; dmin is undefined for M=1. An encoder is a chosen bijection [M]→C. A hard decoder may output a codeword or failure; ties are explicit. Rate is logq(M)/n symbols per use.

**verificationObligation:** Map alphabets, exact arithmetic, equality, logarithm base, channel model and error criterion before use.; Retrieve explicit premises; category and specialization links do not inherit claims.

**reviewStatus:** Editorial mathematical review; Lean models are explicitly scoped and theorem sketches are not compiled proofs.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-BlockCode-encode"></a>

### encode

`urn:csabs:operation/BlockCode-encode`

**signature:** encode : ([M]≃C)×[M] → C

**description:** Apply the chosen message-to-codeword bijection; C alone does not choose an encoding.

**precondition:** Inputs satisfy the concept profile.

**totality:** Total on the stated domain.

**postcondition:** Apply the chosen message-to-codeword bijection; C alone does not choose an encoding.

**source:** [Georg Böcherer, Lecture Notes on Channel Coding (2016)](https://arxiv.org/html/1607.00974v1); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** Chapter 1 §4 Block codes; Chapter 4 §14.1 minimum distance

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-BlockCode-nearest"></a>

### nearest

`urn:csabs:operation/BlockCode-nearest`

**signature:** nearest : C×Σⁿ → FinSet(C)

**description:** Return every c∈C minimizing dH(c,y); this set is nonempty and may contain ties.

**precondition:** Inputs satisfy the concept profile.

**totality:** Total on the stated domain.

**postcondition:** Return every c∈C minimizing dH(c,y); this set is nonempty and may contain ties.

**source:** [Georg Böcherer, Lecture Notes on Channel Coding (2016)](https://arxiv.org/html/1607.00974v1); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** Chapter 1 §4 Block codes; Chapter 4 §14.1 minimum distance

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-BlockCode-minimum-distance"></a>

### minimum-distance

`urn:csabs:operation/BlockCode-minimum-distance`

**signature:** dmin : {C:|C|≥2} → ℕ

**description:** Minimum pairwise distance over distinct codewords.

**precondition:** |C|≥2.

**totality:** Partial: undefined for singleton codebooks.

**postcondition:** Minimum pairwise distance over distinct codewords.

**source:** [Georg Böcherer, Lecture Notes on Channel Coding (2016)](https://arxiv.org/html/1607.00974v1); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** Chapter 1 §4 Block codes; Chapter 4 §14.1 minimum distance

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-BlockCode-decode"></a>

### decode

`urn:csabs:operation/BlockCode-decode`

**signature:** decode : (δ:Σⁿ→C∪{failure})×Σⁿ → C∪{failure}

**description:** Evaluate a supplied decoder; correctness needs a separate error-radius or channel criterion.

**precondition:** Inputs satisfy the concept profile.

**totality:** Total on the stated domain.

**postcondition:** Evaluate a supplied decoder; correctness needs a separate error-radius or channel criterion.

**source:** [Georg Böcherer, Lecture Notes on Channel Coding (2016)](https://arxiv.org/html/1607.00974v1); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** Chapter 1 §4 Block codes; Chapter 4 §14.1 minimum distance

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-BlockCode-distance-distribution"></a>

### distance-distribution

`urn:csabs:operation/BlockCode-distance-distribution`

**signature:** A : Code(Σ,n)×{0,…,n} → ℚ≥0

**description:** Ai=(1/|C|)|{(c,c′)∈C²:dH(c,c′)=i}|; A0=1. This counts ordered pairs and does not assume linearity.

**precondition:** Inputs satisfy the concept profile.

**totality:** Total on the stated domain.

**postcondition:** Ai=(1/|C|)|{(c,c′)∈C²:dH(c,c′)=i}|; A0=1. This counts ordered pairs and does not assume linearity.

**source:** [Georg Böcherer, Lecture Notes on Channel Coding (2016)](https://arxiv.org/html/1607.00974v1); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** Chapter 1 §4 Block codes; Chapter 4 §14.1 minimum distance

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-BlockCode-codebook"></a>

### codebook

`urn:csabs:axiom/BlockCode-codebook`

**statement:** C is a nonempty subset of Σⁿ; encode is bijective onto C; nearest(C,y)=argmin{c∈C}dH(c,y); dmin is the distinct-pair minimum only when |C|≥2; δ is a supplied total map to C∪{failure}; Ai counts ordered pairs divided by |C|.

**formalStatement:** C is a nonempty subset of Σⁿ; encode is bijective onto C; nearest(C,y)=argmin{c∈C}dH(c,y); dmin is the distinct-pair minimum only when |C|≥2; δ is a supplied total map to C∪{failure}; Ai counts ordered pairs divided by |C|.

**assumptions:** Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state. M≥1; dmin is undefined for M=1. An encoder is a chosen bijection [M]→C. A hard decoder may output a codeword or failure; ties are explicit. Rate is logq(M)/n symbols per use.

**ruleRole:** defining-rule

**reviewStatus:** Sourced structural definition, not an independent foundational axiom.

**source:** [Georg Böcherer, Lecture Notes on Channel Coding (2016)](https://arxiv.org/html/1607.00974v1); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** Chapter 1 §4 Block codes; Chapter 4 §14.1 minimum distance

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-BlockCode-unique-radius"></a>

### Minimum-distance unique-decoding theorem

`urn:csabs:theorem/BlockCode-unique-radius`

**statement:** For |C|≥2 and integer t≥0, the radius-t Hamming balls about all codewords are pairwise disjoint iff dmin(C)≥2t+1. In this case every corruption of at most t symbols has the original word as its unique nearest codeword.

**formalStatement:** For |C|≥2 and integer t≥0, the radius-t Hamming balls about all codewords are pairwise disjoint iff dmin(C)≥2t+1. In this case every corruption of at most t symbols has the original word as its unique nearest codeword.

**assumptions:** Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state. M≥1; dmin is undefined for M=1. An encoder is a chosen bijection [M]→C. A hard decoder may output a codeword or failure; ties are explicit. Rate is logq(M)/n symbols per use.; |C|≥2; arbitrary symbol substitutions, worst-case radius t, hard received words in Σⁿ.

**dependsOn:** [codebook](BlockCode.md#node-urn-csabs-axiom-BlockCode-codebook); [Hamming metric laws](HammingSpace.md#node-urn-csabs-law-HammingSpace-metric)

**proofSketch:** Triangle inequality gives disjointness when 2t<dmin. If two words differ in at most 2t places, split their differing coordinates to construct a received word within t of both; hence no decoder can always recover both.

**reviewStatus:** Editorial proof sketch; no registered Lean theorem witness.

**source:** [Georg Böcherer, Lecture Notes on Channel Coding (2016)](https://arxiv.org/html/1607.00974v1); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** Chapter 4 §14.1, correcting t errors

**sourceNote:** Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.

**provenanceKind:** derived

<a id="node-urn-csabs-theorem-BlockCode-hamming-bound"></a>

### Hamming sphere-packing bound

`urn:csabs:theorem/BlockCode-hamming-bound`

**statement:** For |C|≥2, d=dmin(C), t=floor((d−1)/2), M=|C|, M Σi=0ᵗ binom(n,i)(q−1)^i ≤ q^n.

**formalStatement:** For |C|≥2, d=dmin(C), t=floor((d−1)/2), M=|C|, M Σi=0ᵗ binom(n,i)(q−1)^i ≤ q^n.

**assumptions:** Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state. M≥1; dmin is undefined for M=1. An encoder is a chosen bijection [M]→C. A hard decoder may output a codeword or failure; ties are explicit. Rate is logq(M)/n symbols per use.; |C|≥2; no linearity hypothesis.

**dependsOn:** [Minimum-distance unique-decoding theorem](BlockCode.md#node-urn-csabs-theorem-BlockCode-unique-radius); [Hamming ball volume](HammingSpace.md#node-urn-csabs-theorem-HammingSpace-ball-volume)

**proofSketch:** The unique-decoding theorem gives disjoint radius-t balls. Each ball has the stated volume; all balls lie in the q^n-word ambient space.

**reviewStatus:** Editorial proof sketch; no registered Lean theorem witness.

**source:** [Venkatesan Guruswami, Introduction to Coding Theory, Notes 1 (CMU, January 2010)](https://www.cs.cmu.edu/~venkatg/teaching/codingtheory/notes/notes1.pdf); accessedOn: 2026-11-11; sourceRole: consulted lecturer-authored definitions and Hamming packing argument

**sourceLocator:** Notes 1, §3.1, Lemma 13 and preceding disjoint-ball argument (pp. 7–8); adapted from binary to q-ary words

**sourceNote:** Adapt the consulted binary packing argument to q-ary words by counting q−1 possible replacements at each changed coordinate. The linked premises and proof sketch state the extension.

**provenanceKind:** derived

<a id="node-urn-csabs-theorem-BlockCode-singleton"></a>

### Singleton bound

`urn:csabs:theorem/BlockCode-singleton`

**statement:** For |C|≥2 and d=dmin(C), |C|≤q^(n−d+1). For a linear [n,k,d]q code this yields d≤n−k+1.

**formalStatement:** For |C|≥2 and d=dmin(C), |C|≤q^(n−d+1). For a linear [n,k,d]q code this yields d≤n−k+1.

**assumptions:** Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state. M≥1; dmin is undefined for M=1. An encoder is a chosen bijection [M]→C. A hard decoder may output a codeword or failure; ties are explicit. Rate is logq(M)/n symbols per use.; |C|≥2; the dimension form additionally assumes the explicit linear-subspace profile and |C|=q^k.

**dependsOn:** [codebook](BlockCode.md#node-urn-csabs-axiom-BlockCode-codebook); [distance-equation](HammingSpace.md#node-urn-csabs-axiom-HammingSpace-distance-equation)

**proofSketch:** Puncture any d−1 coordinates. Two codewords cannot have identical remaining coordinates, since their original distance would be ≤d−1. The resulting injection into Σ^(n−d+1) gives the bound.

**reviewStatus:** Editorial proof sketch; no registered Lean theorem witness.

**source:** [Georg Böcherer, Lecture Notes on Channel Coding (2016)](https://arxiv.org/html/1607.00974v1); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §14.2 Theorem 14.4 (Singleton bound), including nonlinear codebooks

**sourceNote:** Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.

**provenanceKind:** derived

## Concept provenance

- [Georg Böcherer, Lecture Notes on Channel Coding (2016)](https://arxiv.org/html/1607.00974v1); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** Chapter 1 §4 Block codes; Chapter 4 §14.1 minimum distance

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/BlockCode",
    "type": "Concept",
    "shortForm": "BlockCode",
    "fullName": "Finite block code (Hamming profile)",
    "category": [
      "urn:csabs:category/channel-coding"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "Nonempty codebook of fixed-length words, with encoding and decoding interfaces kept separate from the set.",
    "notation": "∅≠C⊆Σⁿ; M=|C|; dmin(C)=min{x≠y in C}dH(x,y)",
    "requiresConcept": [
      "urn:csabs:concept/HammingSpace",
      "urn:csabs:concept/FiniteSet",
      "urn:csabs:concept/Function"
    ],
    "relatedConcept": [
      "urn:csabs:concept/ChannelCapacity"
    ],
    "hasOperation": [
      "urn:csabs:operation/BlockCode-encode",
      "urn:csabs:operation/BlockCode-nearest",
      "urn:csabs:operation/BlockCode-minimum-distance",
      "urn:csabs:operation/BlockCode-decode",
      "urn:csabs:operation/BlockCode-distance-distribution"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/BlockCode-codebook"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/BlockCode-unique-radius",
      "urn:csabs:theorem/BlockCode-hamming-bound",
      "urn:csabs:theorem/BlockCode-singleton"
    ],
    "axiomBasis": "C is a nonempty subset of Σⁿ; encode is bijective onto C; nearest(C,y)=argmin{c∈C}dH(c,y); dmin is the distinct-pair minimum only when |C|≥2; δ is a supplied total map to C∪{failure}; Ai counts ordered pairs divided by |C|.",
    "basisKind": "extensional-structural-definition",
    "basisScope": "Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state. M≥1; dmin is undefined for M=1. An encoder is a chosen bijection [M]→C. A hard decoder may output a codeword or failure; ties are explicit. Rate is logq(M)/n symbols per use.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial mathematical review; Lean models are explicitly scoped and theorem sketches are not compiled proofs.",
    "verificationObligation": [
      "Map alphabets, exact arithmetic, equality, logarithm base, channel model and error criterion before use.",
      "Retrieve explicit premises; category and specialization links do not inherit claims."
    ],
    "source": [
      "urn:csabs:source/boecherer-channel-coding"
    ],
    "sourceLocator": "Chapter 1 §4 Block codes; Chapter 4 §14.1 minimum distance",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted",
    "leanFormulation": "abbrev BlockCode := Information.Code",
    "formulationSource": "urn:csabs:source/local-lean-InformationTheory",
    "formulationLocator": "Catalog.BlockCode",
    "formulationScope": "partial",
    "leanModelMapping": "Nonempty Finset of Fin n→A with positive n. Instantiate a finite alphabet with at least two symbols.",
    "leanModelLimitations": "Encoder bijection, nearest-set decoder, failure, distance distribution and partial dmin operations omitted. These are model bindings, not proofs of the catalog theorems.",
    "mathematicalFormulation": "A block code is a nonempty finite C⊆A^n with n>0. Equality is set equality of codewords. The selected interface leaves minimum distance undefined when |C|<2."
  },
  {
    "id": "urn:csabs:operation/BlockCode-encode",
    "type": "Operation",
    "name": "encode",
    "signature": "encode : ([M]≃C)×[M] → C",
    "description": "Apply the chosen message-to-codeword bijection; C alone does not choose an encoding.",
    "concept": "urn:csabs:concept/BlockCode",
    "precondition": "Inputs satisfy the concept profile.",
    "totality": "Total on the stated domain.",
    "postcondition": "Apply the chosen message-to-codeword bijection; C alone does not choose an encoding.",
    "source": [
      "urn:csabs:source/boecherer-channel-coding"
    ],
    "sourceLocator": "Chapter 1 §4 Block codes; Chapter 4 §14.1 minimum distance",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/BlockCode-nearest",
    "type": "Operation",
    "name": "nearest",
    "signature": "nearest : C×Σⁿ → FinSet(C)",
    "description": "Return every c∈C minimizing dH(c,y); this set is nonempty and may contain ties.",
    "concept": "urn:csabs:concept/BlockCode",
    "precondition": "Inputs satisfy the concept profile.",
    "totality": "Total on the stated domain.",
    "postcondition": "Return every c∈C minimizing dH(c,y); this set is nonempty and may contain ties.",
    "source": [
      "urn:csabs:source/boecherer-channel-coding"
    ],
    "sourceLocator": "Chapter 1 §4 Block codes; Chapter 4 §14.1 minimum distance",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/BlockCode-minimum-distance",
    "type": "Operation",
    "name": "minimum-distance",
    "signature": "dmin : {C:|C|≥2} → ℕ",
    "description": "Minimum pairwise distance over distinct codewords.",
    "concept": "urn:csabs:concept/BlockCode",
    "precondition": "|C|≥2.",
    "totality": "Partial: undefined for singleton codebooks.",
    "postcondition": "Minimum pairwise distance over distinct codewords.",
    "source": [
      "urn:csabs:source/boecherer-channel-coding"
    ],
    "sourceLocator": "Chapter 1 §4 Block codes; Chapter 4 §14.1 minimum distance",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/BlockCode-decode",
    "type": "Operation",
    "name": "decode",
    "signature": "decode : (δ:Σⁿ→C∪{failure})×Σⁿ → C∪{failure}",
    "description": "Evaluate a supplied decoder; correctness needs a separate error-radius or channel criterion.",
    "concept": "urn:csabs:concept/BlockCode",
    "precondition": "Inputs satisfy the concept profile.",
    "totality": "Total on the stated domain.",
    "postcondition": "Evaluate a supplied decoder; correctness needs a separate error-radius or channel criterion.",
    "source": [
      "urn:csabs:source/boecherer-channel-coding"
    ],
    "sourceLocator": "Chapter 1 §4 Block codes; Chapter 4 §14.1 minimum distance",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/BlockCode-distance-distribution",
    "type": "Operation",
    "name": "distance-distribution",
    "signature": "A : Code(Σ,n)×{0,…,n} → ℚ≥0",
    "description": "Ai=(1/|C|)|{(c,c′)∈C²:dH(c,c′)=i}|; A0=1. This counts ordered pairs and does not assume linearity.",
    "concept": "urn:csabs:concept/BlockCode",
    "precondition": "Inputs satisfy the concept profile.",
    "totality": "Total on the stated domain.",
    "postcondition": "Ai=(1/|C|)|{(c,c′)∈C²:dH(c,c′)=i}|; A0=1. This counts ordered pairs and does not assume linearity.",
    "source": [
      "urn:csabs:source/boecherer-channel-coding"
    ],
    "sourceLocator": "Chapter 1 §4 Block codes; Chapter 4 §14.1 minimum distance",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/BlockCode-codebook",
    "type": "Axiom",
    "name": "codebook",
    "statement": "C is a nonempty subset of Σⁿ; encode is bijective onto C; nearest(C,y)=argmin{c∈C}dH(c,y); dmin is the distinct-pair minimum only when |C|≥2; δ is a supplied total map to C∪{failure}; Ai counts ordered pairs divided by |C|.",
    "formalStatement": "C is a nonempty subset of Σⁿ; encode is bijective onto C; nearest(C,y)=argmin{c∈C}dH(c,y); dmin is the distinct-pair minimum only when |C|≥2; δ is a supplied total map to C∪{failure}; Ai counts ordered pairs divided by |C|.",
    "assumptions": [
      "Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state. M≥1; dmin is undefined for M=1. An encoder is a chosen bijection [M]→C. A hard decoder may output a codeword or failure; ties are explicit. Rate is logq(M)/n symbols per use."
    ],
    "appliesTo": [
      "urn:csabs:concept/BlockCode"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Sourced structural definition, not an independent foundational axiom.",
    "source": [
      "urn:csabs:source/boecherer-channel-coding"
    ],
    "sourceLocator": "Chapter 1 §4 Block codes; Chapter 4 §14.1 minimum distance",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:theorem/BlockCode-unique-radius",
    "type": "Theorem",
    "name": "Minimum-distance unique-decoding theorem",
    "statement": "For |C|≥2 and integer t≥0, the radius-t Hamming balls about all codewords are pairwise disjoint iff dmin(C)≥2t+1. In this case every corruption of at most t symbols has the original word as its unique nearest codeword.",
    "formalStatement": "For |C|≥2 and integer t≥0, the radius-t Hamming balls about all codewords are pairwise disjoint iff dmin(C)≥2t+1. In this case every corruption of at most t symbols has the original word as its unique nearest codeword.",
    "assumptions": [
      "Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state. M≥1; dmin is undefined for M=1. An encoder is a chosen bijection [M]→C. A hard decoder may output a codeword or failure; ties are explicit. Rate is logq(M)/n symbols per use.",
      "|C|≥2; arbitrary symbol substitutions, worst-case radius t, hard received words in Σⁿ."
    ],
    "appliesTo": [
      "urn:csabs:concept/BlockCode",
      "urn:csabs:concept/LinearBlockCode",
      "urn:csabs:concept/NonlinearBlockCode"
    ],
    "dependsOn": [
      "urn:csabs:axiom/BlockCode-codebook",
      "urn:csabs:law/HammingSpace-metric"
    ],
    "proofSketch": "Triangle inequality gives disjointness when 2t<dmin. If two words differ in at most 2t places, split their differing coordinates to construct a received word within t of both; hence no decoder can always recover both.",
    "reviewStatus": "Editorial proof sketch; no registered Lean theorem witness.",
    "source": [
      "urn:csabs:source/boecherer-channel-coding"
    ],
    "sourceLocator": "Chapter 4 §14.1, correcting t errors",
    "sourceNote": "Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/BlockCode-hamming-bound",
    "type": "Theorem",
    "name": "Hamming sphere-packing bound",
    "statement": "For |C|≥2, d=dmin(C), t=floor((d−1)/2), M=|C|, M Σi=0ᵗ binom(n,i)(q−1)^i ≤ q^n.",
    "formalStatement": "For |C|≥2, d=dmin(C), t=floor((d−1)/2), M=|C|, M Σi=0ᵗ binom(n,i)(q−1)^i ≤ q^n.",
    "assumptions": [
      "Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state. M≥1; dmin is undefined for M=1. An encoder is a chosen bijection [M]→C. A hard decoder may output a codeword or failure; ties are explicit. Rate is logq(M)/n symbols per use.",
      "|C|≥2; no linearity hypothesis."
    ],
    "appliesTo": [
      "urn:csabs:concept/BlockCode",
      "urn:csabs:concept/LinearBlockCode",
      "urn:csabs:concept/NonlinearBlockCode"
    ],
    "dependsOn": [
      "urn:csabs:theorem/BlockCode-unique-radius",
      "urn:csabs:theorem/HammingSpace-ball-volume"
    ],
    "proofSketch": "The unique-decoding theorem gives disjoint radius-t balls. Each ball has the stated volume; all balls lie in the q^n-word ambient space.",
    "reviewStatus": "Editorial proof sketch; no registered Lean theorem witness.",
    "source": [
      "urn:csabs:source/guruswami-coding-introduction"
    ],
    "sourceLocator": "Notes 1, §3.1, Lemma 13 and preceding disjoint-ball argument (pp. 7–8); adapted from binary to q-ary words",
    "sourceNote": "Adapt the consulted binary packing argument to q-ary words by counting q−1 possible replacements at each changed coordinate. The linked premises and proof sketch state the extension.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/BlockCode-singleton",
    "type": "Theorem",
    "name": "Singleton bound",
    "statement": "For |C|≥2 and d=dmin(C), |C|≤q^(n−d+1). For a linear [n,k,d]q code this yields d≤n−k+1.",
    "formalStatement": "For |C|≥2 and d=dmin(C), |C|≤q^(n−d+1). For a linear [n,k,d]q code this yields d≤n−k+1.",
    "assumptions": [
      "Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state. M≥1; dmin is undefined for M=1. An encoder is a chosen bijection [M]→C. A hard decoder may output a codeword or failure; ties are explicit. Rate is logq(M)/n symbols per use.",
      "|C|≥2; the dimension form additionally assumes the explicit linear-subspace profile and |C|=q^k."
    ],
    "appliesTo": [
      "urn:csabs:concept/BlockCode",
      "urn:csabs:concept/LinearBlockCode",
      "urn:csabs:concept/NonlinearBlockCode"
    ],
    "dependsOn": [
      "urn:csabs:axiom/BlockCode-codebook",
      "urn:csabs:axiom/HammingSpace-distance-equation"
    ],
    "proofSketch": "Puncture any d−1 coordinates. Two codewords cannot have identical remaining coordinates, since their original distance would be ≤d−1. The resulting injection into Σ^(n−d+1) gives the bound.",
    "reviewStatus": "Editorial proof sketch; no registered Lean theorem witness.",
    "source": [
      "urn:csabs:source/boecherer-channel-coding"
    ],
    "sourceLocator": "§14.2 Theorem 14.4 (Singleton bound), including nonlinear codebooks",
    "sourceNote": "Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
