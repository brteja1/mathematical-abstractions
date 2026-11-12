# Linear block code over a finite field

Codebook that is a vector subspace of a fixed finite-field word space.

**Notation:** C≤𝔽qⁿ; [n,k]q; k=dim𝔽q C

**Stable ID:** `urn:csabs:concept/LinearBlockCode`

**Categories:** Information theory → Coding theory → Channel coding

**Kind:** Mathematical structure

**Prerequisites:** [Finite block code (Hamming profile)](BlockCode.md), [Finite field (Galois field)](FiniteField.md), [Vector space over a field](VectorSpace.md), [Linear map](LinearMap.md)

**Specializes:** [Finite block code (Hamming profile)](BlockCode.md)

## Backlinks

- [Euclidean dual of a finite-field linear code](DualCode.md) — `requiresConcept`
- [Generator matrix of a linear block code (row convention)](GeneratorMatrix.md) — `requiresConcept`
- [Nonlinear finite-field block code](NonlinearBlockCode.md) — `requiresConcept`
- [Parity-check matrix of a linear block code (row convention)](ParityCheckMatrix.md) — `requiresConcept`

## Mathematical formulation

For a finite field F and n>0, a linear block code is an F-subspace C≤F^n, hence 0∈C and au+bv∈C for all u,v∈C,a,b∈F. The zero subspace is permitted.

**Lean formulation** (in its source module context):

```lean
abbrev LinearBlockCode := Information.LinearCode
```

**Source:** [`Catalog.LinearBlockCode`](../lean/Catalog/InformationTheory.lean); consulted 2026-11-12.

**Scope:** partial

**Interpretation:** Submodule F (Fin n→F) for a finite field F, with positive n. Equality is submodule extensional equality.

**Limits:** No weight, dimension, size or minimum-distance witnesses. These are model bindings, not proofs of the catalog theorems.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** C⊆𝔽qⁿ, 0∈C, and for all a,b∈𝔽q and u,v∈C, au+bv∈C; k=dim𝔽q C.

**basisKind:** extensional-structural-definition

**basisScope:** Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state. Σ is the fixed finite field 𝔽q, not ℤ/qℤ for composite q. 0≤k≤n; k=0 gives {0}, whose dmin is undefined. Arithmetic is exact.

**specializationNote:** Identify the alphabet with 𝔽q and retain the same subset C⊆𝔽qⁿ and Hamming distance; impose explicit zero/addition/scalar closure. Vector-space laws use coordinatewise field operations restricted to C.

**verificationObligation:** Map alphabets, exact arithmetic, equality, logarithm base, channel model and error criterion before use.; Retrieve explicit premises; category and specialization links do not inherit claims.

**reviewStatus:** Editorial mathematical review; Lean models are explicitly scoped and theorem sketches are not compiled proofs.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-LinearBlockCode-weight"></a>

### weight

`urn:csabs:operation/LinearBlockCode-weight`

**signature:** wt : C → ℕ

**description:** wt(c)=dH(c,0); zero belongs to C by the explicit closure rule.

**precondition:** Inputs satisfy the concept profile.

**totality:** Total on the stated domain.

**postcondition:** wt(c)=dH(c,0); zero belongs to C by the explicit closure rule.

**source:** [Georg Böcherer, Lecture Notes on Channel Coding (2016)](https://arxiv.org/html/1607.00974v1); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §6.3 Definition 6.15; §6.4 generator matrices; §7.1 minimum weight

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-LinearBlockCode-subspace"></a>

### subspace

`urn:csabs:axiom/LinearBlockCode-subspace`

**statement:** C⊆𝔽qⁿ, 0∈C, and for all a,b∈𝔽q and u,v∈C, au+bv∈C; k=dim𝔽q C.

**formalStatement:** C⊆𝔽qⁿ, 0∈C, and for all a,b∈𝔽q and u,v∈C, au+bv∈C; k=dim𝔽q C.

**assumptions:** Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state. Σ is the fixed finite field 𝔽q, not ℤ/qℤ for composite q. 0≤k≤n; k=0 gives {0}, whose dmin is undefined. Arithmetic is exact.

**ruleRole:** defining-rule

**reviewStatus:** Sourced structural definition, not an independent foundational axiom.

**source:** [Georg Böcherer, Lecture Notes on Channel Coding (2016)](https://arxiv.org/html/1607.00974v1); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §6.3 Definition 6.15; §6.4 generator matrices; §7.1 minimum weight

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-LinearBlockCode-cardinality"></a>

### Linear-code cardinality

`urn:csabs:theorem/LinearBlockCode-cardinality`

**statement:** |C|=q^k; the q-ary rate is k/n.

**formalStatement:** |C|=q^k; the q-ary rate is k/n.

**assumptions:** Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state. Σ is the fixed finite field 𝔽q, not ℤ/qℤ for composite q. 0≤k≤n; k=0 gives {0}, whose dmin is undefined. Arithmetic is exact.

**dependsOn:** [subspace](LinearBlockCode.md#node-urn-csabs-axiom-LinearBlockCode-subspace)

**proofSketch:** Choose a basis of C; unique coordinates give a bijection 𝔽qᵏ≃C.

**reviewStatus:** Editorial statement-to-Lean correspondence review; a full-claim witness is registered separately in lean/bindings.json. Consult a fresh verification report for compiler and axiom-audit evidence.

**source:** [Georg Böcherer, Lecture Notes on Channel Coding (2016)](https://arxiv.org/html/1607.00974v1); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §6.3 Definition 6.15; §6.4 generator matrices; §7.1 minimum weight

**sourceNote:** Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ (F : Type) [Field F] [Fintype F] (n : ℕ) (c : Catalog.Information.LinearCode F n), Nat.card c.space = (Fintype.card F)^(Module.finrank F c.space) ∧ Catalog.Information.qaryRate c = (Module.finrank F c.space : ℝ)/n
```

**Source:** [`Catalog.Information.Verified.linearCardinality`](../lean/Catalog/InformationTheoryStatements.lean); consulted 2026-11-12.

**Scope:** registered-witness-type

**Interpretation:** Finite exact profile. |C|=q^k; the q-ary rate is k/n. The compiled Targets proposition supplies explicit carriers and hypotheses; the independently expanded expected type is retained here. Nat minima are used only under nontrivial-code assumptions; source and channel blocks use positive lengths.

**Limits:** Witness proves the entire expanded expected type; correspondence to the informal statement is a reviewed mapping. This does not prove other catalog targets or an implementation refinement.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/LinearBlockCode-subspace": "Explicit premise: C⊆𝔽qⁿ, 0∈C, and for all a,b∈𝔽q and u,v∈C, au+bv∈C; k=dim𝔽q C. Implemented by the normalized finite-law, exact finite-field, prefix-word or Hamming definitions and proved helper lemmas in InformationTheoryProofs/Statements; not introduced as a global axiom."
}
```

<a id="node-urn-csabs-theorem-LinearBlockCode-distance-weight"></a>

### Minimum distance equals minimum nonzero weight

`urn:csabs:theorem/LinearBlockCode-distance-weight`

**statement:** If k≥1, dmin(C)=min{wt(c):c∈C,c≠0}.

**formalStatement:** If k≥1, dmin(C)=min{wt(c):c∈C,c≠0}.

**assumptions:** Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state. Σ is the fixed finite field 𝔽q, not ℤ/qℤ for composite q. 0≤k≤n; k=0 gives {0}, whose dmin is undefined. Arithmetic is exact.; k≥1, so at least two codewords exist.

**dependsOn:** [subspace](LinearBlockCode.md#node-urn-csabs-axiom-LinearBlockCode-subspace); [distance-equation](HammingSpace.md#node-urn-csabs-axiom-HammingSpace-distance-equation)

**proofSketch:** The distance dH(u,v) equals wt(u−v). Closure puts all nonzero differences in C, and every nonzero c is the difference c−0.

**reviewStatus:** Editorial statement-to-Lean correspondence review; a full-claim witness is registered separately in lean/bindings.json. Consult a fresh verification report for compiler and axiom-audit evidence.

**source:** [Georg Böcherer, Lecture Notes on Channel Coding (2016)](https://arxiv.org/html/1607.00974v1); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §6.3 Definition 6.15; §6.4 generator matrices; §7.1 minimum weight

**sourceNote:** Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ (F : Type) [Field F] [Fintype F] [DecidableEq F] (n : ℕ) (c : Catalog.Information.LinearCode F n), 0 < Module.finrank F c.space → Catalog.Information.pairMinimum (c.space : Set (Fin n → F)) = sInf (Catalog.Information.nonzeroWeights c)
```

**Source:** [`Catalog.Information.Verified.distanceWeight`](../lean/Catalog/InformationTheoryStatements.lean); consulted 2026-11-12.

**Scope:** registered-witness-type

**Interpretation:** Finite exact profile. If k≥1, dmin(C)=min{wt(c):c∈C,c≠0}. The compiled Targets proposition supplies explicit carriers and hypotheses; the independently expanded expected type is retained here. Nat minima are used only under nontrivial-code assumptions; source and channel blocks use positive lengths.

**Limits:** Witness proves the entire expanded expected type; correspondence to the informal statement is a reviewed mapping. This does not prove other catalog targets or an implementation refinement.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/HammingSpace-distance-equation": "Explicit premise: dH(x,y)=Σi 1{xi≠yi}; B(x,t)={y:dH(x,y)≤t}. Implemented by the normalized finite-law, exact finite-field, prefix-word or Hamming definitions and proved helper lemmas in InformationTheoryProofs/Statements; not introduced as a global axiom.",
  "urn:csabs:axiom/LinearBlockCode-subspace": "Explicit premise: C⊆𝔽qⁿ, 0∈C, and for all a,b∈𝔽q and u,v∈C, au+bv∈C; k=dim𝔽q C. Implemented by the normalized finite-law, exact finite-field, prefix-word or Hamming definitions and proved helper lemmas in InformationTheoryProofs/Statements; not introduced as a global axiom."
}
```

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

**sourceLocator:** §6.3 Definition 6.15; §6.4 generator matrices; §7.1 minimum weight

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/LinearBlockCode",
    "type": "Concept",
    "shortForm": "LinearBlockCode",
    "fullName": "Linear block code over a finite field",
    "category": [
      "urn:csabs:category/channel-coding"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "Codebook that is a vector subspace of a fixed finite-field word space.",
    "notation": "C≤𝔽qⁿ; [n,k]q; k=dim𝔽q C",
    "requiresConcept": [
      "urn:csabs:concept/BlockCode",
      "urn:csabs:concept/FiniteField",
      "urn:csabs:concept/VectorSpace",
      "urn:csabs:concept/LinearMap"
    ],
    "relatedConcept": [],
    "hasOperation": [
      "urn:csabs:operation/LinearBlockCode-weight"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/LinearBlockCode-subspace"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/LinearBlockCode-cardinality",
      "urn:csabs:theorem/LinearBlockCode-distance-weight",
      "urn:csabs:theorem/BlockCode-unique-radius",
      "urn:csabs:theorem/BlockCode-hamming-bound",
      "urn:csabs:theorem/BlockCode-singleton"
    ],
    "axiomBasis": "C⊆𝔽qⁿ, 0∈C, and for all a,b∈𝔽q and u,v∈C, au+bv∈C; k=dim𝔽q C.",
    "basisKind": "extensional-structural-definition",
    "basisScope": "Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state. Σ is the fixed finite field 𝔽q, not ℤ/qℤ for composite q. 0≤k≤n; k=0 gives {0}, whose dmin is undefined. Arithmetic is exact.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial mathematical review; Lean models are explicitly scoped and theorem sketches are not compiled proofs.",
    "verificationObligation": [
      "Map alphabets, exact arithmetic, equality, logarithm base, channel model and error criterion before use.",
      "Retrieve explicit premises; category and specialization links do not inherit claims."
    ],
    "source": [
      "urn:csabs:source/boecherer-channel-coding"
    ],
    "sourceLocator": "§6.3 Definition 6.15; §6.4 generator matrices; §7.1 minimum weight",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/BlockCode"
    ],
    "specializationNote": "Identify the alphabet with 𝔽q and retain the same subset C⊆𝔽qⁿ and Hamming distance; impose explicit zero/addition/scalar closure. Vector-space laws use coordinatewise field operations restricted to C.",
    "leanFormulation": "abbrev LinearBlockCode := Information.LinearCode",
    "formulationSource": "urn:csabs:source/local-lean-InformationTheory",
    "formulationLocator": "Catalog.LinearBlockCode",
    "formulationScope": "partial",
    "leanModelMapping": "Submodule F (Fin n→F) for a finite field F, with positive n. Equality is submodule extensional equality.",
    "leanModelLimitations": "No weight, dimension, size or minimum-distance witnesses. These are model bindings, not proofs of the catalog theorems.",
    "mathematicalFormulation": "For a finite field F and n>0, a linear block code is an F-subspace C≤F^n, hence 0∈C and au+bv∈C for all u,v∈C,a,b∈F. The zero subspace is permitted."
  },
  {
    "id": "urn:csabs:operation/LinearBlockCode-weight",
    "type": "Operation",
    "name": "weight",
    "signature": "wt : C → ℕ",
    "description": "wt(c)=dH(c,0); zero belongs to C by the explicit closure rule.",
    "concept": "urn:csabs:concept/LinearBlockCode",
    "precondition": "Inputs satisfy the concept profile.",
    "totality": "Total on the stated domain.",
    "postcondition": "wt(c)=dH(c,0); zero belongs to C by the explicit closure rule.",
    "source": [
      "urn:csabs:source/boecherer-channel-coding"
    ],
    "sourceLocator": "§6.3 Definition 6.15; §6.4 generator matrices; §7.1 minimum weight",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/LinearBlockCode-subspace",
    "type": "Axiom",
    "name": "subspace",
    "statement": "C⊆𝔽qⁿ, 0∈C, and for all a,b∈𝔽q and u,v∈C, au+bv∈C; k=dim𝔽q C.",
    "formalStatement": "C⊆𝔽qⁿ, 0∈C, and for all a,b∈𝔽q and u,v∈C, au+bv∈C; k=dim𝔽q C.",
    "assumptions": [
      "Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state. Σ is the fixed finite field 𝔽q, not ℤ/qℤ for composite q. 0≤k≤n; k=0 gives {0}, whose dmin is undefined. Arithmetic is exact."
    ],
    "appliesTo": [
      "urn:csabs:concept/LinearBlockCode"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Sourced structural definition, not an independent foundational axiom.",
    "source": [
      "urn:csabs:source/boecherer-channel-coding"
    ],
    "sourceLocator": "§6.3 Definition 6.15; §6.4 generator matrices; §7.1 minimum weight",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:theorem/LinearBlockCode-cardinality",
    "type": "Theorem",
    "name": "Linear-code cardinality",
    "statement": "|C|=q^k; the q-ary rate is k/n.",
    "formalStatement": "|C|=q^k; the q-ary rate is k/n.",
    "assumptions": [
      "Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state. Σ is the fixed finite field 𝔽q, not ℤ/qℤ for composite q. 0≤k≤n; k=0 gives {0}, whose dmin is undefined. Arithmetic is exact."
    ],
    "appliesTo": [
      "urn:csabs:concept/LinearBlockCode"
    ],
    "dependsOn": [
      "urn:csabs:axiom/LinearBlockCode-subspace"
    ],
    "proofSketch": "Choose a basis of C; unique coordinates give a bijection 𝔽qᵏ≃C.",
    "reviewStatus": "Editorial statement-to-Lean correspondence review; a full-claim witness is registered separately in lean/bindings.json. Consult a fresh verification report for compiler and axiom-audit evidence.",
    "source": [
      "urn:csabs:source/boecherer-channel-coding"
    ],
    "sourceLocator": "§6.3 Definition 6.15; §6.4 generator matrices; §7.1 minimum weight",
    "sourceNote": "Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ (F : Type) [Field F] [Fintype F] (n : ℕ) (c : Catalog.Information.LinearCode F n), Nat.card c.space = (Fintype.card F)^(Module.finrank F c.space) ∧ Catalog.Information.qaryRate c = (Module.finrank F c.space : ℝ)/n",
    "formulationSource": "urn:csabs:source/local-lean-InformationTheoryStatements",
    "formulationLocator": "Catalog.Information.Verified.linearCardinality",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Finite exact profile. |C|=q^k; the q-ary rate is k/n. The compiled Targets proposition supplies explicit carriers and hypotheses; the independently expanded expected type is retained here. Nat minima are used only under nontrivial-code assumptions; source and channel blocks use positive lengths.",
    "leanModelLimitations": "Witness proves the entire expanded expected type; correspondence to the informal statement is a reviewed mapping. This does not prove other catalog targets or an implementation refinement.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/LinearBlockCode-subspace\": \"Explicit premise: C⊆𝔽qⁿ, 0∈C, and for all a,b∈𝔽q and u,v∈C, au+bv∈C; k=dim𝔽q C. Implemented by the normalized finite-law, exact finite-field, prefix-word or Hamming definitions and proved helper lemmas in InformationTheoryProofs/Statements; not introduced as a global axiom.\"}"
  },
  {
    "id": "urn:csabs:theorem/LinearBlockCode-distance-weight",
    "type": "Theorem",
    "name": "Minimum distance equals minimum nonzero weight",
    "statement": "If k≥1, dmin(C)=min{wt(c):c∈C,c≠0}.",
    "formalStatement": "If k≥1, dmin(C)=min{wt(c):c∈C,c≠0}.",
    "assumptions": [
      "Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state. Σ is the fixed finite field 𝔽q, not ℤ/qℤ for composite q. 0≤k≤n; k=0 gives {0}, whose dmin is undefined. Arithmetic is exact.",
      "k≥1, so at least two codewords exist."
    ],
    "appliesTo": [
      "urn:csabs:concept/LinearBlockCode"
    ],
    "dependsOn": [
      "urn:csabs:axiom/LinearBlockCode-subspace",
      "urn:csabs:axiom/HammingSpace-distance-equation"
    ],
    "proofSketch": "The distance dH(u,v) equals wt(u−v). Closure puts all nonzero differences in C, and every nonzero c is the difference c−0.",
    "reviewStatus": "Editorial statement-to-Lean correspondence review; a full-claim witness is registered separately in lean/bindings.json. Consult a fresh verification report for compiler and axiom-audit evidence.",
    "source": [
      "urn:csabs:source/boecherer-channel-coding"
    ],
    "sourceLocator": "§6.3 Definition 6.15; §6.4 generator matrices; §7.1 minimum weight",
    "sourceNote": "Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ (F : Type) [Field F] [Fintype F] [DecidableEq F] (n : ℕ) (c : Catalog.Information.LinearCode F n), 0 < Module.finrank F c.space → Catalog.Information.pairMinimum (c.space : Set (Fin n → F)) = sInf (Catalog.Information.nonzeroWeights c)",
    "formulationSource": "urn:csabs:source/local-lean-InformationTheoryStatements",
    "formulationLocator": "Catalog.Information.Verified.distanceWeight",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Finite exact profile. If k≥1, dmin(C)=min{wt(c):c∈C,c≠0}. The compiled Targets proposition supplies explicit carriers and hypotheses; the independently expanded expected type is retained here. Nat minima are used only under nontrivial-code assumptions; source and channel blocks use positive lengths.",
    "leanModelLimitations": "Witness proves the entire expanded expected type; correspondence to the informal statement is a reviewed mapping. This does not prove other catalog targets or an implementation refinement.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/HammingSpace-distance-equation\": \"Explicit premise: dH(x,y)=Σi 1{xi≠yi}; B(x,t)={y:dH(x,y)≤t}. Implemented by the normalized finite-law, exact finite-field, prefix-word or Hamming definitions and proved helper lemmas in InformationTheoryProofs/Statements; not introduced as a global axiom.\", \"urn:csabs:axiom/LinearBlockCode-subspace\": \"Explicit premise: C⊆𝔽qⁿ, 0∈C, and for all a,b∈𝔽q and u,v∈C, au+bv∈C; k=dim𝔽q C. Implemented by the normalized finite-law, exact finite-field, prefix-word or Hamming definitions and proved helper lemmas in InformationTheoryProofs/Statements; not introduced as a global axiom.\"}"
  }
]
```
<!-- graph-record:end -->
