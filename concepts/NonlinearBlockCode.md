# Nonlinear finite-field block code

Finite-field codebook that is not a vector subspace under the specified symbol identification.

**Notation:** ∅≠C⊆𝔽qⁿ; C is not an 𝔽q-subspace

**Stable ID:** `urn:csabs:concept/NonlinearBlockCode`

**Categories:** Information theory → Coding theory → Channel coding

**Kind:** Mathematical structure

**Prerequisites:** [Finite block code (Hamming profile)](BlockCode.md), [Finite field (Galois field)](FiniteField.md), [Linear block code over a finite field](LinearBlockCode.md)

**Specializes:** [Finite block code (Hamming profile)](BlockCode.md)

## Mathematical formulation

For finite field F and n>0, the selected nonlinear code is a nonempty finite C⊆F^n with ¬∃S≤F^n,carrier(S)=C. This excludes every linear subspace, rather than merely omitting a supplied linear structure.

**Lean formulation** (in its source module context):

```lean
abbrev NonlinearBlockCode := Information.NonlinearCode
```

**Source:** [`Catalog.NonlinearBlockCode`](../lean/Catalog/InformationTheory.lean); consulted 2026-11-12.

**Scope:** partial

**Interpretation:** Nonempty finite field codebook together with failure to coincide with any submodule, with pointwise word equality.

**Limits:** No chosen nonlinearity witness or decoding operations; finite-field alphabet identification must be supplied. These are model bindings, not proofs of the catalog theorems.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** C is a nonempty subset of 𝔽qⁿ and ¬(0∈C ∧ ∀a,b∈𝔽q ∀u,v∈C, au+bv∈C).

**basisKind:** extensional-structural-definition

**basisScope:** Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state. Linearity is relative to the chosen field alphabet and origin. A nonlinear code can be affine. Nonlinearity is a property of the codebook, not decoder complexity or a nonlinear implementation of a linear encoder.

**specializationNote:** Use the same finite-field words and Hamming metric, imposing failure of subspace closure. Linear and nonlinear codebooks partition this fixed-field block-code profile; arbitrary alphabets have no intrinsic linearity.

**verificationObligation:** Map alphabets, exact arithmetic, equality, logarithm base, channel model and error criterion before use.; Retrieve explicit premises; category and specialization links do not inherit claims.

**reviewStatus:** Editorial mathematical review; Lean models are explicitly scoped and theorem sketches are not compiled proofs.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-NonlinearBlockCode-nonlinearity-witness"></a>

### nonlinearity-witness

`urn:csabs:operation/NonlinearBlockCode-nonlinearity-witness`

**signature:** witness : NonlinearCode(𝔽q,n) → Witness

**description:** Return either evidence 0∉C or a,b∈𝔽q and u,v∈C with au+bv∉C; multiple witnesses are allowed.

**precondition:** Nonempty finite codebook with fixed finite field and failure of subspace structure.

**totality:** Set-valued specification; no preferred witness or efficient algorithm.

**postcondition:** Return either evidence 0∉C or a,b∈𝔽q and u,v∈C with au+bv∉C; multiple witnesses are allowed.

**source:** [Georg Böcherer, Lecture Notes on Channel Coding (2016)](https://arxiv.org/html/1607.00974v1); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §6.3 linear-code definition; complementary finite-field profile derived here

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-NonlinearBlockCode-not-subspace"></a>

### not-subspace

`urn:csabs:axiom/NonlinearBlockCode-not-subspace`

**statement:** C is a nonempty subset of 𝔽qⁿ and ¬(0∈C ∧ ∀a,b∈𝔽q ∀u,v∈C, au+bv∈C).

**formalStatement:** C is a nonempty subset of 𝔽qⁿ and ¬(0∈C ∧ ∀a,b∈𝔽q ∀u,v∈C, au+bv∈C).

**assumptions:** Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state. Linearity is relative to the chosen field alphabet and origin. A nonlinear code can be affine. Nonlinearity is a property of the codebook, not decoder complexity or a nonlinear implementation of a linear encoder.

**ruleRole:** defining-rule

**reviewStatus:** Sourced structural definition, not an independent foundational axiom.

**source:** [Georg Böcherer, Lecture Notes on Channel Coding (2016)](https://arxiv.org/html/1607.00974v1); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §6.3 linear-code definition; complementary finite-field profile derived here

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-NonlinearBlockCode-witness-exists"></a>

### Nonlinearity witness characterization

`urn:csabs:theorem/NonlinearBlockCode-witness-exists`

**statement:** C is nonlinear iff 0∉C or there exist a,b∈𝔽q and u,v∈C with au+bv∉C.

**formalStatement:** C is nonlinear iff 0∉C or there exist a,b∈𝔽q and u,v∈C with au+bv∉C.

**assumptions:** Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state. Linearity is relative to the chosen field alphabet and origin. A nonlinear code can be affine. Nonlinearity is a property of the codebook, not decoder complexity or a nonlinear implementation of a linear encoder.

**dependsOn:** [not-subspace](NonlinearBlockCode.md#node-urn-csabs-axiom-NonlinearBlockCode-not-subspace); [subspace](LinearBlockCode.md#node-urn-csabs-axiom-LinearBlockCode-subspace)

**proofSketch:** Negate the explicit subspace criterion using classical logic; no new algebraic axiom is needed.

**reviewStatus:** Editorial statement-to-Lean correspondence review; a full-claim witness is registered separately in lean/bindings.json. Consult a fresh verification report for compiler and axiom-audit evidence.

**source:** [Georg Böcherer, Lecture Notes on Channel Coding (2016)](https://arxiv.org/html/1607.00974v1); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §6.3 Definition 6.15; logical complement of the defining closure criterion

**sourceNote:** Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ (F : Type) [Field F] (n : ℕ) (C : Set (Fin n → F)), (¬ ∃ S : Submodule F (Fin n → F), (S : Set (Fin n → F)) = C) ↔ Catalog.Information.NonlinearWitness C
```

**Source:** [`Catalog.Information.Verified.nonlinearWitness`](../lean/Catalog/InformationTheoryStatements.lean); consulted 2026-11-12.

**Scope:** registered-witness-type

**Interpretation:** Finite exact profile. C is nonlinear iff 0∉C or there exist a,b∈𝔽q and u,v∈C with au+bv∉C. The compiled Targets proposition supplies explicit carriers and hypotheses; the independently expanded expected type is retained here. Nat minima are used only under nontrivial-code assumptions; source and channel blocks use positive lengths.

**Limits:** Witness proves the entire expanded expected type; correspondence to the informal statement is a reviewed mapping. This does not prove other catalog targets or an implementation refinement.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/LinearBlockCode-subspace": "Explicit premise: C⊆𝔽qⁿ, 0∈C, and for all a,b∈𝔽q and u,v∈C, au+bv∈C; k=dim𝔽q C. Implemented by the normalized finite-law, exact finite-field, prefix-word or Hamming definitions and proved helper lemmas in InformationTheoryProofs/Statements; not introduced as a global axiom.",
  "urn:csabs:axiom/NonlinearBlockCode-not-subspace": "Explicit premise: C is a nonempty subset of 𝔽qⁿ and ¬(0∈C ∧ ∀a,b∈𝔽q ∀u,v∈C, au+bv∈C). Implemented by the normalized finite-law, exact finite-field, prefix-word or Hamming definitions and proved helper lemmas in InformationTheoryProofs/Statements; not introduced as a global axiom."
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

**sourceLocator:** §6.3 linear-code definition; complementary finite-field profile derived here

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/NonlinearBlockCode",
    "type": "Concept",
    "shortForm": "NonlinearBlockCode",
    "fullName": "Nonlinear finite-field block code",
    "category": [
      "urn:csabs:category/channel-coding"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "Finite-field codebook that is not a vector subspace under the specified symbol identification.",
    "notation": "∅≠C⊆𝔽qⁿ; C is not an 𝔽q-subspace",
    "requiresConcept": [
      "urn:csabs:concept/BlockCode",
      "urn:csabs:concept/FiniteField",
      "urn:csabs:concept/LinearBlockCode"
    ],
    "relatedConcept": [],
    "hasOperation": [
      "urn:csabs:operation/NonlinearBlockCode-nonlinearity-witness"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/NonlinearBlockCode-not-subspace"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/NonlinearBlockCode-witness-exists",
      "urn:csabs:theorem/BlockCode-unique-radius",
      "urn:csabs:theorem/BlockCode-hamming-bound",
      "urn:csabs:theorem/BlockCode-singleton"
    ],
    "axiomBasis": "C is a nonempty subset of 𝔽qⁿ and ¬(0∈C ∧ ∀a,b∈𝔽q ∀u,v∈C, au+bv∈C).",
    "basisKind": "extensional-structural-definition",
    "basisScope": "Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state. Linearity is relative to the chosen field alphabet and origin. A nonlinear code can be affine. Nonlinearity is a property of the codebook, not decoder complexity or a nonlinear implementation of a linear encoder.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial mathematical review; Lean models are explicitly scoped and theorem sketches are not compiled proofs.",
    "verificationObligation": [
      "Map alphabets, exact arithmetic, equality, logarithm base, channel model and error criterion before use.",
      "Retrieve explicit premises; category and specialization links do not inherit claims."
    ],
    "source": [
      "urn:csabs:source/boecherer-channel-coding"
    ],
    "sourceLocator": "§6.3 linear-code definition; complementary finite-field profile derived here",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/BlockCode"
    ],
    "specializationNote": "Use the same finite-field words and Hamming metric, imposing failure of subspace closure. Linear and nonlinear codebooks partition this fixed-field block-code profile; arbitrary alphabets have no intrinsic linearity.",
    "leanFormulation": "abbrev NonlinearBlockCode := Information.NonlinearCode",
    "formulationSource": "urn:csabs:source/local-lean-InformationTheory",
    "formulationLocator": "Catalog.NonlinearBlockCode",
    "formulationScope": "partial",
    "leanModelMapping": "Nonempty finite field codebook together with failure to coincide with any submodule, with pointwise word equality.",
    "leanModelLimitations": "No chosen nonlinearity witness or decoding operations; finite-field alphabet identification must be supplied. These are model bindings, not proofs of the catalog theorems.",
    "mathematicalFormulation": "For finite field F and n>0, the selected nonlinear code is a nonempty finite C⊆F^n with ¬∃S≤F^n,carrier(S)=C. This excludes every linear subspace, rather than merely omitting a supplied linear structure."
  },
  {
    "id": "urn:csabs:operation/NonlinearBlockCode-nonlinearity-witness",
    "type": "Operation",
    "name": "nonlinearity-witness",
    "signature": "witness : NonlinearCode(𝔽q,n) → Witness",
    "description": "Return either evidence 0∉C or a,b∈𝔽q and u,v∈C with au+bv∉C; multiple witnesses are allowed.",
    "concept": "urn:csabs:concept/NonlinearBlockCode",
    "precondition": "Nonempty finite codebook with fixed finite field and failure of subspace structure.",
    "totality": "Set-valued specification; no preferred witness or efficient algorithm.",
    "postcondition": "Return either evidence 0∉C or a,b∈𝔽q and u,v∈C with au+bv∉C; multiple witnesses are allowed.",
    "source": [
      "urn:csabs:source/boecherer-channel-coding"
    ],
    "sourceLocator": "§6.3 linear-code definition; complementary finite-field profile derived here",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/NonlinearBlockCode-not-subspace",
    "type": "Axiom",
    "name": "not-subspace",
    "statement": "C is a nonempty subset of 𝔽qⁿ and ¬(0∈C ∧ ∀a,b∈𝔽q ∀u,v∈C, au+bv∈C).",
    "formalStatement": "C is a nonempty subset of 𝔽qⁿ and ¬(0∈C ∧ ∀a,b∈𝔽q ∀u,v∈C, au+bv∈C).",
    "assumptions": [
      "Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state. Linearity is relative to the chosen field alphabet and origin. A nonlinear code can be affine. Nonlinearity is a property of the codebook, not decoder complexity or a nonlinear implementation of a linear encoder."
    ],
    "appliesTo": [
      "urn:csabs:concept/NonlinearBlockCode"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Sourced structural definition, not an independent foundational axiom.",
    "source": [
      "urn:csabs:source/boecherer-channel-coding"
    ],
    "sourceLocator": "§6.3 linear-code definition; complementary finite-field profile derived here",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:theorem/NonlinearBlockCode-witness-exists",
    "type": "Theorem",
    "name": "Nonlinearity witness characterization",
    "statement": "C is nonlinear iff 0∉C or there exist a,b∈𝔽q and u,v∈C with au+bv∉C.",
    "formalStatement": "C is nonlinear iff 0∉C or there exist a,b∈𝔽q and u,v∈C with au+bv∉C.",
    "assumptions": [
      "Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state. Linearity is relative to the chosen field alphabet and origin. A nonlinear code can be affine. Nonlinearity is a property of the codebook, not decoder complexity or a nonlinear implementation of a linear encoder."
    ],
    "appliesTo": [
      "urn:csabs:concept/NonlinearBlockCode"
    ],
    "dependsOn": [
      "urn:csabs:axiom/NonlinearBlockCode-not-subspace",
      "urn:csabs:axiom/LinearBlockCode-subspace"
    ],
    "proofSketch": "Negate the explicit subspace criterion using classical logic; no new algebraic axiom is needed.",
    "reviewStatus": "Editorial statement-to-Lean correspondence review; a full-claim witness is registered separately in lean/bindings.json. Consult a fresh verification report for compiler and axiom-audit evidence.",
    "source": [
      "urn:csabs:source/boecherer-channel-coding"
    ],
    "sourceLocator": "§6.3 Definition 6.15; logical complement of the defining closure criterion",
    "sourceNote": "Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ (F : Type) [Field F] (n : ℕ) (C : Set (Fin n → F)), (¬ ∃ S : Submodule F (Fin n → F), (S : Set (Fin n → F)) = C) ↔ Catalog.Information.NonlinearWitness C",
    "formulationSource": "urn:csabs:source/local-lean-InformationTheoryStatements",
    "formulationLocator": "Catalog.Information.Verified.nonlinearWitness",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Finite exact profile. C is nonlinear iff 0∉C or there exist a,b∈𝔽q and u,v∈C with au+bv∉C. The compiled Targets proposition supplies explicit carriers and hypotheses; the independently expanded expected type is retained here. Nat minima are used only under nontrivial-code assumptions; source and channel blocks use positive lengths.",
    "leanModelLimitations": "Witness proves the entire expanded expected type; correspondence to the informal statement is a reviewed mapping. This does not prove other catalog targets or an implementation refinement.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/LinearBlockCode-subspace\": \"Explicit premise: C⊆𝔽qⁿ, 0∈C, and for all a,b∈𝔽q and u,v∈C, au+bv∈C; k=dim𝔽q C. Implemented by the normalized finite-law, exact finite-field, prefix-word or Hamming definitions and proved helper lemmas in InformationTheoryProofs/Statements; not introduced as a global axiom.\", \"urn:csabs:axiom/NonlinearBlockCode-not-subspace\": \"Explicit premise: C is a nonempty subset of 𝔽qⁿ and ¬(0∈C ∧ ∀a,b∈𝔽q ∀u,v∈C, au+bv∈C). Implemented by the normalized finite-law, exact finite-field, prefix-word or Hamming definitions and proved helper lemmas in InformationTheoryProofs/Statements; not introduced as a global axiom.\"}"
  }
]
```
<!-- graph-record:end -->
