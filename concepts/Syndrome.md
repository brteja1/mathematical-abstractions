# Syndrome map of a linear block code

Linear check-value map that identifies error cosets relative to a chosen check matrix.

**Notation:** sH(y)=Hyᵀ∈𝔽q^(n−k)

**Stable ID:** `urn:csabs:concept/Syndrome`

**Categories:** Information theory → Coding theory → Channel coding

**Kind:** Function

**Prerequisites:** [Parity-check matrix of a linear block code (row convention)](ParityCheckMatrix.md), [Linear map](LinearMap.md)

## Mathematical formulation

For a supplied parity-check map h:F^n→F^{n−k}, syndrome(y)=h(y). The argument structure requires ker(h)=C and surjectivity; syndrome equality is ordinary vector equality.

**Lean formulation** (in its source module context):

```lean
abbrev Syndrome {F : Type} [Field F] [Fintype F] {n k : Nat}
    (h : ParityCheckMatrix F n k) := h.checkMap
```

**Source:** [`Catalog.Syndrome`](../lean/Catalog/InformationTheory.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Actual check linear map applied to finite-field received vectors; parity_coordinates identifies it with a concrete check-matrix product. The full zero/coset/error-invariance theorem is proved.

**Limits:** No error-leader selection or efficient error reconstruction.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** sH(y)=Hyᵀ, with H full rank and ker(H)=C.

**basisKind:** extensional-structural-definition

**basisScope:** Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state. Fix a full-rank check matrix H for C. Received words and additive errors are field vectors; syndrome equality is coordinate equality for this H.

**verificationObligation:** Map alphabets, exact arithmetic, equality, logarithm base, channel model and error criterion before use.; Retrieve explicit premises; category and specialization links do not inherit claims.

**reviewStatus:** Editorial mathematical review; Lean models are explicitly scoped and theorem sketches are not compiled proofs.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-Syndrome-syndrome"></a>

### syndrome

`urn:csabs:operation/Syndrome-syndrome`

**signature:** s : CheckMatrix(C)×𝔽qⁿ → 𝔽q^(n−k)

**description:** Compute Hyᵀ; this detects membership, not a unique error pattern.

**precondition:** Inputs satisfy the concept profile.

**totality:** Total on the stated domain.

**postcondition:** Compute Hyᵀ; this detects membership, not a unique error pattern.

**source:** [Georg Böcherer, Lecture Notes on Channel Coding (2016)](https://arxiv.org/html/1607.00974v1); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §8.3 cosets and §8.4 syndrome decoder

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-Syndrome-syndrome-equation"></a>

### syndrome-equation

`urn:csabs:axiom/Syndrome-syndrome-equation`

**statement:** sH(y)=Hyᵀ, with H full rank and ker(H)=C.

**formalStatement:** sH(y)=Hyᵀ, with H full rank and ker(H)=C.

**assumptions:** Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state. Fix a full-rank check matrix H for C. Received words and additive errors are field vectors; syndrome equality is coordinate equality for this H.

**ruleRole:** defining-rule

**reviewStatus:** Sourced structural definition, not an independent foundational axiom.

**source:** [Georg Böcherer, Lecture Notes on Channel Coding (2016)](https://arxiv.org/html/1607.00974v1); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §8.3 cosets and §8.4 syndrome decoder

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-Syndrome-coset-invariance"></a>

### Syndrome and coset theorem

`urn:csabs:theorem/Syndrome-coset-invariance`

**statement:** sH(y)=0 iff y∈C; sH(y)=sH(z) iff y−z∈C; if y=c+e with c∈C then sH(y)=sH(e).

**formalStatement:** sH(y)=0 iff y∈C; sH(y)=sH(z) iff y−z∈C; if y=c+e with c∈C then sH(y)=sH(e).

**assumptions:** Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state. Fix a full-rank check matrix H for C. Received words and additive errors are field vectors; syndrome equality is coordinate equality for this H.

**dependsOn:** [syndrome-equation](Syndrome.md#node-urn-csabs-axiom-Syndrome-syndrome-equation); [kernel](ParityCheckMatrix.md#node-urn-csabs-axiom-ParityCheckMatrix-kernel)

**proofSketch:** Use matrix linearity and ker(H)=C. Equal syndromes are equivalent to H(y−z)ᵀ=0.

**reviewStatus:** Editorial statement-to-Lean correspondence review; a full-claim witness is registered separately in lean/bindings.json. Consult a fresh verification report for compiler and axiom-audit evidence.

**source:** [Georg Böcherer, Lecture Notes on Channel Coding (2016)](https://arxiv.org/html/1607.00974v1); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §8.3 cosets and §8.4 syndrome decoder

**sourceNote:** Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ (F : Type) [Field F] [Fintype F] (n k : ℕ) (h : Catalog.Information.CheckMatrix F n k) (y z c e : Fin n → F), c ∈ h.code.space → (h.checkMap y = 0 ↔ y ∈ h.code.space) ∧ (h.checkMap y = h.checkMap z ↔ y-z ∈ h.code.space) ∧ h.checkMap (c+e) = h.checkMap e
```

**Source:** [`Catalog.Information.Verified.syndromeCoset`](../lean/Catalog/InformationTheoryStatements.lean); consulted 2026-11-12.

**Scope:** registered-witness-type

**Interpretation:** Finite exact profile. sH(y)=0 iff y∈C; sH(y)=sH(z) iff y−z∈C; if y=c+e with c∈C then sH(y)=sH(e). The compiled Targets proposition supplies explicit carriers and hypotheses; the independently expanded expected type is retained here. Nat minima are used only under nontrivial-code assumptions; source and channel blocks use positive lengths.

**Limits:** Witness proves the entire expanded expected type; correspondence to the informal statement is a reviewed mapping. This does not prove other catalog targets or an implementation refinement.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/ParityCheckMatrix-kernel": "Explicit premise: H has n−k independent rows; C=ker(x↦Hxᵀ). Implemented by the normalized finite-law, exact finite-field, prefix-word or Hamming definitions and proved helper lemmas in InformationTheoryProofs/Statements; not introduced as a global axiom.",
  "urn:csabs:axiom/Syndrome-syndrome-equation": "Explicit premise: sH(y)=Hyᵀ, with H full rank and ker(H)=C. Implemented by the normalized finite-law, exact finite-field, prefix-word or Hamming definitions and proved helper lemmas in InformationTheoryProofs/Statements; not introduced as a global axiom."
}
```

## Concept provenance

- [Georg Böcherer, Lecture Notes on Channel Coding (2016)](https://arxiv.org/html/1607.00974v1); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §8.3 cosets and §8.4 syndrome decoder

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/Syndrome",
    "type": "Concept",
    "shortForm": "Syndrome",
    "fullName": "Syndrome map of a linear block code",
    "category": [
      "urn:csabs:category/channel-coding"
    ],
    "kind": "urn:csabs:kind/function",
    "definition": "Linear check-value map that identifies error cosets relative to a chosen check matrix.",
    "notation": "sH(y)=Hyᵀ∈𝔽q^(n−k)",
    "requiresConcept": [
      "urn:csabs:concept/ParityCheckMatrix",
      "urn:csabs:concept/LinearMap"
    ],
    "relatedConcept": [],
    "hasOperation": [
      "urn:csabs:operation/Syndrome-syndrome"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/Syndrome-syndrome-equation"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/Syndrome-coset-invariance"
    ],
    "axiomBasis": "sH(y)=Hyᵀ, with H full rank and ker(H)=C.",
    "basisKind": "extensional-structural-definition",
    "basisScope": "Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state. Fix a full-rank check matrix H for C. Received words and additive errors are field vectors; syndrome equality is coordinate equality for this H.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial mathematical review; Lean models are explicitly scoped and theorem sketches are not compiled proofs.",
    "verificationObligation": [
      "Map alphabets, exact arithmetic, equality, logarithm base, channel model and error criterion before use.",
      "Retrieve explicit premises; category and specialization links do not inherit claims."
    ],
    "source": [
      "urn:csabs:source/boecherer-channel-coding"
    ],
    "sourceLocator": "§8.3 cosets and §8.4 syndrome decoder",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted",
    "leanFormulation": "abbrev Syndrome {F : Type} [Field F] [Fintype F] {n k : Nat}\n    (h : ParityCheckMatrix F n k) := h.checkMap",
    "formulationSource": "urn:csabs:source/local-lean-InformationTheory",
    "formulationLocator": "Catalog.Syndrome",
    "formulationScope": "model",
    "leanModelMapping": "Actual check linear map applied to finite-field received vectors; parity_coordinates identifies it with a concrete check-matrix product. The full zero/coset/error-invariance theorem is proved.",
    "leanModelLimitations": "No error-leader selection or efficient error reconstruction.",
    "mathematicalFormulation": "For a supplied parity-check map h:F^n→F^{n−k}, syndrome(y)=h(y). The argument structure requires ker(h)=C and surjectivity; syndrome equality is ordinary vector equality."
  },
  {
    "id": "urn:csabs:operation/Syndrome-syndrome",
    "type": "Operation",
    "name": "syndrome",
    "signature": "s : CheckMatrix(C)×𝔽qⁿ → 𝔽q^(n−k)",
    "description": "Compute Hyᵀ; this detects membership, not a unique error pattern.",
    "concept": "urn:csabs:concept/Syndrome",
    "precondition": "Inputs satisfy the concept profile.",
    "totality": "Total on the stated domain.",
    "postcondition": "Compute Hyᵀ; this detects membership, not a unique error pattern.",
    "source": [
      "urn:csabs:source/boecherer-channel-coding"
    ],
    "sourceLocator": "§8.3 cosets and §8.4 syndrome decoder",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/Syndrome-syndrome-equation",
    "type": "Axiom",
    "name": "syndrome-equation",
    "statement": "sH(y)=Hyᵀ, with H full rank and ker(H)=C.",
    "formalStatement": "sH(y)=Hyᵀ, with H full rank and ker(H)=C.",
    "assumptions": [
      "Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state. Fix a full-rank check matrix H for C. Received words and additive errors are field vectors; syndrome equality is coordinate equality for this H."
    ],
    "appliesTo": [
      "urn:csabs:concept/Syndrome"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Sourced structural definition, not an independent foundational axiom.",
    "source": [
      "urn:csabs:source/boecherer-channel-coding"
    ],
    "sourceLocator": "§8.3 cosets and §8.4 syndrome decoder",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:theorem/Syndrome-coset-invariance",
    "type": "Theorem",
    "name": "Syndrome and coset theorem",
    "statement": "sH(y)=0 iff y∈C; sH(y)=sH(z) iff y−z∈C; if y=c+e with c∈C then sH(y)=sH(e).",
    "formalStatement": "sH(y)=0 iff y∈C; sH(y)=sH(z) iff y−z∈C; if y=c+e with c∈C then sH(y)=sH(e).",
    "assumptions": [
      "Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state. Fix a full-rank check matrix H for C. Received words and additive errors are field vectors; syndrome equality is coordinate equality for this H."
    ],
    "appliesTo": [
      "urn:csabs:concept/Syndrome"
    ],
    "dependsOn": [
      "urn:csabs:axiom/Syndrome-syndrome-equation",
      "urn:csabs:axiom/ParityCheckMatrix-kernel"
    ],
    "proofSketch": "Use matrix linearity and ker(H)=C. Equal syndromes are equivalent to H(y−z)ᵀ=0.",
    "reviewStatus": "Editorial statement-to-Lean correspondence review; a full-claim witness is registered separately in lean/bindings.json. Consult a fresh verification report for compiler and axiom-audit evidence.",
    "source": [
      "urn:csabs:source/boecherer-channel-coding"
    ],
    "sourceLocator": "§8.3 cosets and §8.4 syndrome decoder",
    "sourceNote": "Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ (F : Type) [Field F] [Fintype F] (n k : ℕ) (h : Catalog.Information.CheckMatrix F n k) (y z c e : Fin n → F), c ∈ h.code.space → (h.checkMap y = 0 ↔ y ∈ h.code.space) ∧ (h.checkMap y = h.checkMap z ↔ y-z ∈ h.code.space) ∧ h.checkMap (c+e) = h.checkMap e",
    "formulationSource": "urn:csabs:source/local-lean-InformationTheoryStatements",
    "formulationLocator": "Catalog.Information.Verified.syndromeCoset",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Finite exact profile. sH(y)=0 iff y∈C; sH(y)=sH(z) iff y−z∈C; if y=c+e with c∈C then sH(y)=sH(e). The compiled Targets proposition supplies explicit carriers and hypotheses; the independently expanded expected type is retained here. Nat minima are used only under nontrivial-code assumptions; source and channel blocks use positive lengths.",
    "leanModelLimitations": "Witness proves the entire expanded expected type; correspondence to the informal statement is a reviewed mapping. This does not prove other catalog targets or an implementation refinement.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/ParityCheckMatrix-kernel\": \"Explicit premise: H has n−k independent rows; C=ker(x↦Hxᵀ). Implemented by the normalized finite-law, exact finite-field, prefix-word or Hamming definitions and proved helper lemmas in InformationTheoryProofs/Statements; not introduced as a global axiom.\", \"urn:csabs:axiom/Syndrome-syndrome-equation\": \"Explicit premise: sH(y)=Hyᵀ, with H full rank and ker(H)=C. Implemented by the normalized finite-law, exact finite-field, prefix-word or Hamming definitions and proved helper lemmas in InformationTheoryProofs/Statements; not introduced as a global axiom.\"}"
  }
]
```
<!-- graph-record:end -->
