# Parity-check matrix of a linear block code (row convention)

Full-row-rank matrix whose kernel is the specified code.

**Notation:** H∈𝔽q^((n−k)×n); C={c:Hcᵀ=0}

**Stable ID:** `urn:csabs:concept/ParityCheckMatrix`

**Categories:** Information theory → Coding theory → Channel coding

**Kind:** Mathematical structure

**Prerequisites:** [Linear block code over a finite field](LinearBlockCode.md), [Finite rectangular matrix over a field](Matrix.md), [Generator matrix of a linear block code (row convention)](GeneratorMatrix.md)

**Related concepts:** [Generator matrix of a linear block code (row convention)](GeneratorMatrix.md), [Euclidean dual of a finite-field linear code](DualCode.md)

## Backlinks

- [Euclidean dual of a finite-field linear code](DualCode.md) — `relatedConcept`
- [Generator matrix of a linear block code (row convention)](GeneratorMatrix.md) — `relatedConcept`
- [Syndrome map of a linear block code](Syndrome.md) — `requiresConcept`

## Mathematical formulation

The selected model is a surjective F-linear h:F^n→F^{n−k}, with k≤n and ker(h)=C. Its coordinate matrix H satisfies h(y)=Hy; independence of the n−k checks is expressed by surjectivity.

**Lean formulation** (in its source module context):

```lean
abbrev ParityCheckMatrix := Information.CheckMatrix
```

**Source:** [`Catalog.ParityCheckMatrix`](../lean/Catalog/InformationTheory.lean); consulted 2026-11-12.

**Scope:** partial

**Interpretation:** Surjective linear check map with code kernel; parityMatrix materializes the concrete matrix and parity_coordinates proves equality with matrix-vector multiplication. Both directions of full-rank generator/check orthogonality are proved.

**Limits:** Boolean checker operation is still represented through the zero comparison rather than a separate named Boolean API; no check-matrix construction algorithm.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** H has n−k independent rows; C=ker(x↦Hxᵀ).

**basisKind:** extensional-structural-definition

**basisScope:** Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state. 0≤k≤n; rows are checks; H has n−k independent rows. k=n permits a zero-row matrix. Check basis choices change syndrome coordinates, not C.

**verificationObligation:** Map alphabets, exact arithmetic, equality, logarithm base, channel model and error criterion before use.; Retrieve explicit premises; category and specialization links do not inherit claims.

**reviewStatus:** Editorial mathematical review; Lean models are explicitly scoped and theorem sketches are not compiled proofs.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-ParityCheckMatrix-check"></a>

### check

`urn:csabs:operation/ParityCheckMatrix-check`

**signature:** check : CheckMatrix(C)×𝔽qⁿ → Bool

**description:** Return true iff Hxᵀ=0.

**precondition:** Inputs satisfy the concept profile.

**totality:** Total on the stated domain.

**postcondition:** Return true iff Hxᵀ=0.

**source:** [Georg Böcherer, Lecture Notes on Channel Coding (2016)](https://arxiv.org/html/1607.00974v1); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §8.2 check matrix; Definition 8.41 and kernel characterization

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-ParityCheckMatrix-kernel"></a>

### kernel

`urn:csabs:axiom/ParityCheckMatrix-kernel`

**statement:** H has n−k independent rows; C=ker(x↦Hxᵀ).

**formalStatement:** H has n−k independent rows; C=ker(x↦Hxᵀ).

**assumptions:** Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state. 0≤k≤n; rows are checks; H has n−k independent rows. k=n permits a zero-row matrix. Check basis choices change syndrome coordinates, not C.

**ruleRole:** defining-rule

**reviewStatus:** Sourced structural definition, not an independent foundational axiom.

**source:** [Georg Böcherer, Lecture Notes on Channel Coding (2016)](https://arxiv.org/html/1607.00974v1); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §8.2 check matrix; Definition 8.41 and kernel characterization

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-ParityCheckMatrix-orthogonality"></a>

### Generator and parity-check orthogonality

`urn:csabs:theorem/ParityCheckMatrix-orthogonality`

**statement:** For a generator G of C and parity-check H of C, GHᵀ=0. Conversely, full ranks k and n−k and GHᵀ=0 imply rowspan(G)=ker(H).

**formalStatement:** For a generator G of C and parity-check H of C, GHᵀ=0. Conversely, full ranks k and n−k and GHᵀ=0 imply rowspan(G)=ker(H).

**assumptions:** Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state. 0≤k≤n; rows are checks; H has n−k independent rows. k=n permits a zero-row matrix. Check basis choices change syndrome coordinates, not C.

**dependsOn:** [kernel](ParityCheckMatrix.md#node-urn-csabs-axiom-ParityCheckMatrix-kernel); [row-basis](GeneratorMatrix.md#node-urn-csabs-axiom-GeneratorMatrix-row-basis)

**proofSketch:** Each generator row belongs to ker(H), giving the product equation. Conversely the product gives inclusion and rank-nullity gives equal dimension k.

**reviewStatus:** Editorial statement-to-Lean correspondence review; a full-claim witness is registered separately in lean/bindings.json. Consult a fresh verification report for compiler and axiom-audit evidence.

**source:** [Georg Böcherer, Lecture Notes on Channel Coding (2016)](https://arxiv.org/html/1607.00974v1); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §8.2 check matrix; Definition 8.41 and kernel characterization

**sourceNote:** Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ (F : Type) [Field F] [Fintype F] (n k : ℕ), (∀ (g : Catalog.Information.Generator F n k) (h : Catalog.Information.CheckMatrix F n k), g.code.space = h.code.space → ∀ m, h.checkMap (Catalog.Information.generatorEncode g m).val = 0) ∧ (∀ (G : (Fin k → F) →ₗ[F] (Fin n → F)) (H : (Fin n → F) →ₗ[F] (Fin (n-k) → F)), k ≤ n → Function.Injective G → Function.Surjective H → H.comp G = 0 → LinearMap.range G = LinearMap.ker H)
```

**Source:** [`Catalog.Information.Verified.checkOrthogonality`](../lean/Catalog/InformationTheoryStatements.lean); consulted 2026-11-12.

**Scope:** registered-witness-type

**Interpretation:** Finite exact profile. For a generator G of C and parity-check H of C, GHᵀ=0. Conversely, full ranks k and n−k and GHᵀ=0 imply rowspan(G)=ker(H). The compiled Targets proposition supplies explicit carriers and hypotheses; the independently expanded expected type is retained here. Nat minima are used only under nontrivial-code assumptions; source and channel blocks use positive lengths.

**Limits:** Witness proves the entire expanded expected type; correspondence to the informal statement is a reviewed mapping. This does not prove other catalog targets or an implementation refinement.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/GeneratorMatrix-row-basis": "Explicit premise: G has k linearly independent rows forming a basis of C, and encodeG(m)=mG. Implemented by the normalized finite-law, exact finite-field, prefix-word or Hamming definitions and proved helper lemmas in InformationTheoryProofs/Statements; not introduced as a global axiom.",
  "urn:csabs:axiom/ParityCheckMatrix-kernel": "Explicit premise: H has n−k independent rows; C=ker(x↦Hxᵀ). Implemented by the normalized finite-law, exact finite-field, prefix-word or Hamming definitions and proved helper lemmas in InformationTheoryProofs/Statements; not introduced as a global axiom."
}
```

## Concept provenance

- [Georg Böcherer, Lecture Notes on Channel Coding (2016)](https://arxiv.org/html/1607.00974v1); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §8.2 check matrix; Definition 8.41 and kernel characterization

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/ParityCheckMatrix",
    "type": "Concept",
    "shortForm": "ParityCheckMatrix",
    "fullName": "Parity-check matrix of a linear block code (row convention)",
    "category": [
      "urn:csabs:category/channel-coding"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "Full-row-rank matrix whose kernel is the specified code.",
    "notation": "H∈𝔽q^((n−k)×n); C={c:Hcᵀ=0}",
    "requiresConcept": [
      "urn:csabs:concept/LinearBlockCode",
      "urn:csabs:concept/Matrix",
      "urn:csabs:concept/GeneratorMatrix"
    ],
    "relatedConcept": [
      "urn:csabs:concept/GeneratorMatrix",
      "urn:csabs:concept/DualCode"
    ],
    "hasOperation": [
      "urn:csabs:operation/ParityCheckMatrix-check"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/ParityCheckMatrix-kernel"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/ParityCheckMatrix-orthogonality"
    ],
    "axiomBasis": "H has n−k independent rows; C=ker(x↦Hxᵀ).",
    "basisKind": "extensional-structural-definition",
    "basisScope": "Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state. 0≤k≤n; rows are checks; H has n−k independent rows. k=n permits a zero-row matrix. Check basis choices change syndrome coordinates, not C.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial mathematical review; Lean models are explicitly scoped and theorem sketches are not compiled proofs.",
    "verificationObligation": [
      "Map alphabets, exact arithmetic, equality, logarithm base, channel model and error criterion before use.",
      "Retrieve explicit premises; category and specialization links do not inherit claims."
    ],
    "source": [
      "urn:csabs:source/boecherer-channel-coding"
    ],
    "sourceLocator": "§8.2 check matrix; Definition 8.41 and kernel characterization",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted",
    "leanFormulation": "abbrev ParityCheckMatrix := Information.CheckMatrix",
    "formulationSource": "urn:csabs:source/local-lean-InformationTheory",
    "formulationLocator": "Catalog.ParityCheckMatrix",
    "formulationScope": "partial",
    "leanModelMapping": "Surjective linear check map with code kernel; parityMatrix materializes the concrete matrix and parity_coordinates proves equality with matrix-vector multiplication. Both directions of full-rank generator/check orthogonality are proved.",
    "leanModelLimitations": "Boolean checker operation is still represented through the zero comparison rather than a separate named Boolean API; no check-matrix construction algorithm.",
    "mathematicalFormulation": "The selected model is a surjective F-linear h:F^n→F^{n−k}, with k≤n and ker(h)=C. Its coordinate matrix H satisfies h(y)=Hy; independence of the n−k checks is expressed by surjectivity."
  },
  {
    "id": "urn:csabs:operation/ParityCheckMatrix-check",
    "type": "Operation",
    "name": "check",
    "signature": "check : CheckMatrix(C)×𝔽qⁿ → Bool",
    "description": "Return true iff Hxᵀ=0.",
    "concept": "urn:csabs:concept/ParityCheckMatrix",
    "precondition": "Inputs satisfy the concept profile.",
    "totality": "Total on the stated domain.",
    "postcondition": "Return true iff Hxᵀ=0.",
    "source": [
      "urn:csabs:source/boecherer-channel-coding"
    ],
    "sourceLocator": "§8.2 check matrix; Definition 8.41 and kernel characterization",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/ParityCheckMatrix-kernel",
    "type": "Axiom",
    "name": "kernel",
    "statement": "H has n−k independent rows; C=ker(x↦Hxᵀ).",
    "formalStatement": "H has n−k independent rows; C=ker(x↦Hxᵀ).",
    "assumptions": [
      "Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state. 0≤k≤n; rows are checks; H has n−k independent rows. k=n permits a zero-row matrix. Check basis choices change syndrome coordinates, not C."
    ],
    "appliesTo": [
      "urn:csabs:concept/ParityCheckMatrix"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Sourced structural definition, not an independent foundational axiom.",
    "source": [
      "urn:csabs:source/boecherer-channel-coding"
    ],
    "sourceLocator": "§8.2 check matrix; Definition 8.41 and kernel characterization",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:theorem/ParityCheckMatrix-orthogonality",
    "type": "Theorem",
    "name": "Generator and parity-check orthogonality",
    "statement": "For a generator G of C and parity-check H of C, GHᵀ=0. Conversely, full ranks k and n−k and GHᵀ=0 imply rowspan(G)=ker(H).",
    "formalStatement": "For a generator G of C and parity-check H of C, GHᵀ=0. Conversely, full ranks k and n−k and GHᵀ=0 imply rowspan(G)=ker(H).",
    "assumptions": [
      "Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state. 0≤k≤n; rows are checks; H has n−k independent rows. k=n permits a zero-row matrix. Check basis choices change syndrome coordinates, not C."
    ],
    "appliesTo": [
      "urn:csabs:concept/ParityCheckMatrix"
    ],
    "dependsOn": [
      "urn:csabs:axiom/ParityCheckMatrix-kernel",
      "urn:csabs:axiom/GeneratorMatrix-row-basis"
    ],
    "proofSketch": "Each generator row belongs to ker(H), giving the product equation. Conversely the product gives inclusion and rank-nullity gives equal dimension k.",
    "reviewStatus": "Editorial statement-to-Lean correspondence review; a full-claim witness is registered separately in lean/bindings.json. Consult a fresh verification report for compiler and axiom-audit evidence.",
    "source": [
      "urn:csabs:source/boecherer-channel-coding"
    ],
    "sourceLocator": "§8.2 check matrix; Definition 8.41 and kernel characterization",
    "sourceNote": "Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ (F : Type) [Field F] [Fintype F] (n k : ℕ), (∀ (g : Catalog.Information.Generator F n k) (h : Catalog.Information.CheckMatrix F n k), g.code.space = h.code.space → ∀ m, h.checkMap (Catalog.Information.generatorEncode g m).val = 0) ∧ (∀ (G : (Fin k → F) →ₗ[F] (Fin n → F)) (H : (Fin n → F) →ₗ[F] (Fin (n-k) → F)), k ≤ n → Function.Injective G → Function.Surjective H → H.comp G = 0 → LinearMap.range G = LinearMap.ker H)",
    "formulationSource": "urn:csabs:source/local-lean-InformationTheoryStatements",
    "formulationLocator": "Catalog.Information.Verified.checkOrthogonality",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Finite exact profile. For a generator G of C and parity-check H of C, GHᵀ=0. Conversely, full ranks k and n−k and GHᵀ=0 imply rowspan(G)=ker(H). The compiled Targets proposition supplies explicit carriers and hypotheses; the independently expanded expected type is retained here. Nat minima are used only under nontrivial-code assumptions; source and channel blocks use positive lengths.",
    "leanModelLimitations": "Witness proves the entire expanded expected type; correspondence to the informal statement is a reviewed mapping. This does not prove other catalog targets or an implementation refinement.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/GeneratorMatrix-row-basis\": \"Explicit premise: G has k linearly independent rows forming a basis of C, and encodeG(m)=mG. Implemented by the normalized finite-law, exact finite-field, prefix-word or Hamming definitions and proved helper lemmas in InformationTheoryProofs/Statements; not introduced as a global axiom.\", \"urn:csabs:axiom/ParityCheckMatrix-kernel\": \"Explicit premise: H has n−k independent rows; C=ker(x↦Hxᵀ). Implemented by the normalized finite-law, exact finite-field, prefix-word or Hamming definitions and proved helper lemmas in InformationTheoryProofs/Statements; not introduced as a global axiom.\"}"
  }
]
```
<!-- graph-record:end -->
