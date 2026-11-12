# Euclidean dual of a finite-field linear code

Orthogonal complement under the ordinary bilinear dot product.

**Notation:** C⊥={v∈𝔽qⁿ:∀c∈C,Σi vici=0}

**Stable ID:** `urn:csabs:concept/DualCode`

**Categories:** Information theory → Coding theory → Channel coding

**Kind:** Mathematical construction

**Prerequisites:** [Linear block code over a finite field](LinearBlockCode.md), [Vector space over a field](VectorSpace.md)

**Related concepts:** [Parity-check matrix of a linear block code (row convention)](ParityCheckMatrix.md)

## Backlinks

- [Parity-check matrix of a linear block code (row convention)](ParityCheckMatrix.md) — `relatedConcept`

## Mathematical formulation

For finite-field linear C≤F^n, C^⊥={v∈F^n | ∀x∈C,Σ\_i v\_i x\_i=0}. Orthogonality uses the bilinear dot product, without complex conjugation.

**Lean formulation** (in its source module context):

```lean
def dualSpace (c : Submodule F (Fin n → F)) : Submodule F (Fin n → F) where
  carrier := {v | ∀ x ∈ c, ∑ i, v i * x i = 0}
  zero_mem' := by simp
  add_mem' := by
    intro u v hu hv x hx
    simp only [Pi.add_apply, add_mul, Finset.sum_add_distrib]
    rw [hu x hx, hv x hx, add_zero]
  smul_mem' := by
    intro a v hv x hx
    simp only [Pi.smul_apply, smul_eq_mul, mul_assoc, ← Finset.mul_sum]
    rw [hv x hx, mul_zero]
```

**Source:** [`Catalog.Information.dualSpace`](../lean/Catalog/InformationTheoryStatements.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Submodule constructed by the ordinary bilinear dot-product orthogonality predicate. The compiled bridge to Mathlib orthogonal complements proves dimension and double-dual claims over any finite field, including characteristic two.

**Limits:** No Hermitian dual or decoding algorithm. Apply to the submodule of a positive-length LinearCode.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** C⊥={v:∀c∈C,Σi vici=0}; dot product is coordinatewise field multiplication followed by addition.

**basisKind:** extensional-structural-definition

**basisScope:** Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state. Finite field and ordinary bilinear dot product; not the Hermitian dual over a square field. k=0 and k=n are permitted.

**verificationObligation:** Map alphabets, exact arithmetic, equality, logarithm base, channel model and error criterion before use.; Retrieve explicit premises; category and specialization links do not inherit claims.

**reviewStatus:** Editorial mathematical review; Lean models are explicitly scoped and theorem sketches are not compiled proofs.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-DualCode-dual"></a>

### dual

`urn:csabs:operation/DualCode-dual`

**signature:** dual : LinearCode(𝔽q,n) → LinearCode(𝔽q,n)

**description:** Return the dot-product orthogonal complement.

**precondition:** Inputs satisfy the concept profile.

**totality:** Total on the stated domain.

**postcondition:** Return the dot-product orthogonal complement.

**source:** [Georg Böcherer, Lecture Notes on Channel Coding (2016)](https://arxiv.org/html/1607.00974v1); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §8.1 Definition 8.32; Propositions 8.35, 8.37 and 8.39

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-DualCode-orthogonal-complement"></a>

### orthogonal-complement

`urn:csabs:axiom/DualCode-orthogonal-complement`

**statement:** C⊥={v:∀c∈C,Σi vici=0}; dot product is coordinatewise field multiplication followed by addition.

**formalStatement:** C⊥={v:∀c∈C,Σi vici=0}; dot product is coordinatewise field multiplication followed by addition.

**assumptions:** Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state. Finite field and ordinary bilinear dot product; not the Hermitian dual over a square field. k=0 and k=n are permitted.

**ruleRole:** defining-rule

**reviewStatus:** Sourced structural definition, not an independent foundational axiom.

**source:** [Georg Böcherer, Lecture Notes on Channel Coding (2016)](https://arxiv.org/html/1607.00974v1); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §8.1 Definition 8.32; Propositions 8.35, 8.37 and 8.39

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-DualCode-dimension-involution"></a>

### Dual-code dimension and double dual

`urn:csabs:theorem/DualCode-dimension-involution`

**statement:** C⊥ is linear, dim(C⊥)=n−dim(C), and (C⊥)⊥=C.

**formalStatement:** C⊥ is linear, dim(C⊥)=n−dim(C), and (C⊥)⊥=C.

**assumptions:** Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state. Finite field and ordinary bilinear dot product; not the Hermitian dual over a square field. k=0 and k=n are permitted.

**dependsOn:** [orthogonal-complement](DualCode.md#node-urn-csabs-axiom-DualCode-orthogonal-complement); [subspace](LinearBlockCode.md#node-urn-csabs-axiom-LinearBlockCode-subspace)

**proofSketch:** Bilinearity gives closure. Nondegeneracy of the coordinate pairing gives the dimension formula via rank-nullity; C⊆(C⊥)⊥ and equal dimensions give equality.

**reviewStatus:** Editorial statement-to-Lean correspondence review; a full-claim witness is registered separately in lean/bindings.json. Consult a fresh verification report for compiler and axiom-audit evidence.

**source:** [Georg Böcherer, Lecture Notes on Channel Coding (2016)](https://arxiv.org/html/1607.00974v1); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §8.1 Definition 8.32; Propositions 8.35, 8.37 and 8.39

**sourceNote:** Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ (F : Type) [Field F] [Fintype F] (n : ℕ) (c : Catalog.Information.LinearCode F n), Module.finrank F (Catalog.Information.dualSpace c.space) = n - Module.finrank F c.space ∧ Catalog.Information.dualSpace (Catalog.Information.dualSpace c.space) = c.space
```

**Source:** [`Catalog.Information.Verified.dualDimension`](../lean/Catalog/InformationTheoryStatements.lean); consulted 2026-11-12.

**Scope:** registered-witness-type

**Interpretation:** Finite exact profile. C⊥ is linear, dim(C⊥)=n−dim(C), and (C⊥)⊥=C. The compiled Targets proposition supplies explicit carriers and hypotheses; the independently expanded expected type is retained here. Nat minima are used only under nontrivial-code assumptions; source and channel blocks use positive lengths.

**Limits:** Witness proves the entire expanded expected type; correspondence to the informal statement is a reviewed mapping. This does not prove other catalog targets or an implementation refinement.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/DualCode-orthogonal-complement": "Explicit premise: C⊥={v:∀c∈C,Σi vici=0}; dot product is coordinatewise field multiplication followed by addition. Implemented by the normalized finite-law, exact finite-field, prefix-word or Hamming definitions and proved helper lemmas in InformationTheoryProofs/Statements; not introduced as a global axiom.",
  "urn:csabs:axiom/LinearBlockCode-subspace": "Explicit premise: C⊆𝔽qⁿ, 0∈C, and for all a,b∈𝔽q and u,v∈C, au+bv∈C; k=dim𝔽q C. Implemented by the normalized finite-law, exact finite-field, prefix-word or Hamming definitions and proved helper lemmas in InformationTheoryProofs/Statements; not introduced as a global axiom."
}
```

## Concept provenance

- [Georg Böcherer, Lecture Notes on Channel Coding (2016)](https://arxiv.org/html/1607.00974v1); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §8.1 Definition 8.32; Propositions 8.35, 8.37 and 8.39

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/DualCode",
    "type": "Concept",
    "shortForm": "DualCode",
    "fullName": "Euclidean dual of a finite-field linear code",
    "category": [
      "urn:csabs:category/channel-coding"
    ],
    "kind": "urn:csabs:kind/construction",
    "definition": "Orthogonal complement under the ordinary bilinear dot product.",
    "notation": "C⊥={v∈𝔽qⁿ:∀c∈C,Σi vici=0}",
    "requiresConcept": [
      "urn:csabs:concept/LinearBlockCode",
      "urn:csabs:concept/VectorSpace"
    ],
    "relatedConcept": [
      "urn:csabs:concept/ParityCheckMatrix"
    ],
    "hasOperation": [
      "urn:csabs:operation/DualCode-dual"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/DualCode-orthogonal-complement"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/DualCode-dimension-involution"
    ],
    "axiomBasis": "C⊥={v:∀c∈C,Σi vici=0}; dot product is coordinatewise field multiplication followed by addition.",
    "basisKind": "extensional-structural-definition",
    "basisScope": "Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state. Finite field and ordinary bilinear dot product; not the Hermitian dual over a square field. k=0 and k=n are permitted.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial mathematical review; Lean models are explicitly scoped and theorem sketches are not compiled proofs.",
    "verificationObligation": [
      "Map alphabets, exact arithmetic, equality, logarithm base, channel model and error criterion before use.",
      "Retrieve explicit premises; category and specialization links do not inherit claims."
    ],
    "source": [
      "urn:csabs:source/boecherer-channel-coding"
    ],
    "sourceLocator": "§8.1 Definition 8.32; Propositions 8.35, 8.37 and 8.39",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted",
    "leanFormulation": "def dualSpace (c : Submodule F (Fin n → F)) : Submodule F (Fin n → F) where\n  carrier := {v | ∀ x ∈ c, ∑ i, v i * x i = 0}\n  zero_mem' := by simp\n  add_mem' := by\n    intro u v hu hv x hx\n    simp only [Pi.add_apply, add_mul, Finset.sum_add_distrib]\n    rw [hu x hx, hv x hx, add_zero]\n  smul_mem' := by\n    intro a v hv x hx\n    simp only [Pi.smul_apply, smul_eq_mul, mul_assoc, ← Finset.mul_sum]\n    rw [hv x hx, mul_zero]",
    "formulationSource": "urn:csabs:source/local-lean-InformationTheoryStatements",
    "formulationLocator": "Catalog.Information.dualSpace",
    "formulationScope": "model",
    "leanModelMapping": "Submodule constructed by the ordinary bilinear dot-product orthogonality predicate. The compiled bridge to Mathlib orthogonal complements proves dimension and double-dual claims over any finite field, including characteristic two.",
    "leanModelLimitations": "No Hermitian dual or decoding algorithm. Apply to the submodule of a positive-length LinearCode.",
    "mathematicalFormulation": "For finite-field linear C≤F^n, C^⊥={v∈F^n | ∀x∈C,Σ_i v_i x_i=0}. Orthogonality uses the bilinear dot product, without complex conjugation."
  },
  {
    "id": "urn:csabs:operation/DualCode-dual",
    "type": "Operation",
    "name": "dual",
    "signature": "dual : LinearCode(𝔽q,n) → LinearCode(𝔽q,n)",
    "description": "Return the dot-product orthogonal complement.",
    "concept": "urn:csabs:concept/DualCode",
    "precondition": "Inputs satisfy the concept profile.",
    "totality": "Total on the stated domain.",
    "postcondition": "Return the dot-product orthogonal complement.",
    "source": [
      "urn:csabs:source/boecherer-channel-coding"
    ],
    "sourceLocator": "§8.1 Definition 8.32; Propositions 8.35, 8.37 and 8.39",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/DualCode-orthogonal-complement",
    "type": "Axiom",
    "name": "orthogonal-complement",
    "statement": "C⊥={v:∀c∈C,Σi vici=0}; dot product is coordinatewise field multiplication followed by addition.",
    "formalStatement": "C⊥={v:∀c∈C,Σi vici=0}; dot product is coordinatewise field multiplication followed by addition.",
    "assumptions": [
      "Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state. Finite field and ordinary bilinear dot product; not the Hermitian dual over a square field. k=0 and k=n are permitted."
    ],
    "appliesTo": [
      "urn:csabs:concept/DualCode"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Sourced structural definition, not an independent foundational axiom.",
    "source": [
      "urn:csabs:source/boecherer-channel-coding"
    ],
    "sourceLocator": "§8.1 Definition 8.32; Propositions 8.35, 8.37 and 8.39",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:theorem/DualCode-dimension-involution",
    "type": "Theorem",
    "name": "Dual-code dimension and double dual",
    "statement": "C⊥ is linear, dim(C⊥)=n−dim(C), and (C⊥)⊥=C.",
    "formalStatement": "C⊥ is linear, dim(C⊥)=n−dim(C), and (C⊥)⊥=C.",
    "assumptions": [
      "Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state. Finite field and ordinary bilinear dot product; not the Hermitian dual over a square field. k=0 and k=n are permitted."
    ],
    "appliesTo": [
      "urn:csabs:concept/DualCode"
    ],
    "dependsOn": [
      "urn:csabs:axiom/DualCode-orthogonal-complement",
      "urn:csabs:axiom/LinearBlockCode-subspace"
    ],
    "proofSketch": "Bilinearity gives closure. Nondegeneracy of the coordinate pairing gives the dimension formula via rank-nullity; C⊆(C⊥)⊥ and equal dimensions give equality.",
    "reviewStatus": "Editorial statement-to-Lean correspondence review; a full-claim witness is registered separately in lean/bindings.json. Consult a fresh verification report for compiler and axiom-audit evidence.",
    "source": [
      "urn:csabs:source/boecherer-channel-coding"
    ],
    "sourceLocator": "§8.1 Definition 8.32; Propositions 8.35, 8.37 and 8.39",
    "sourceNote": "Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ (F : Type) [Field F] [Fintype F] (n : ℕ) (c : Catalog.Information.LinearCode F n), Module.finrank F (Catalog.Information.dualSpace c.space) = n - Module.finrank F c.space ∧ Catalog.Information.dualSpace (Catalog.Information.dualSpace c.space) = c.space",
    "formulationSource": "urn:csabs:source/local-lean-InformationTheoryStatements",
    "formulationLocator": "Catalog.Information.Verified.dualDimension",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Finite exact profile. C⊥ is linear, dim(C⊥)=n−dim(C), and (C⊥)⊥=C. The compiled Targets proposition supplies explicit carriers and hypotheses; the independently expanded expected type is retained here. Nat minima are used only under nontrivial-code assumptions; source and channel blocks use positive lengths.",
    "leanModelLimitations": "Witness proves the entire expanded expected type; correspondence to the informal statement is a reviewed mapping. This does not prove other catalog targets or an implementation refinement.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/DualCode-orthogonal-complement\": \"Explicit premise: C⊥={v:∀c∈C,Σi vici=0}; dot product is coordinatewise field multiplication followed by addition. Implemented by the normalized finite-law, exact finite-field, prefix-word or Hamming definitions and proved helper lemmas in InformationTheoryProofs/Statements; not introduced as a global axiom.\", \"urn:csabs:axiom/LinearBlockCode-subspace\": \"Explicit premise: C⊆𝔽qⁿ, 0∈C, and for all a,b∈𝔽q and u,v∈C, au+bv∈C; k=dim𝔽q C. Implemented by the normalized finite-law, exact finite-field, prefix-word or Hamming definitions and proved helper lemmas in InformationTheoryProofs/Statements; not introduced as a global axiom.\"}"
  }
]
```
<!-- graph-record:end -->
