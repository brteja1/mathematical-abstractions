# Generator matrix of a linear block code (row convention)

Full-row-rank matrix whose row span is the specified code.

**Notation:** G∈𝔽q^(k×n); C={mG:m∈𝔽qᵏ}

**Stable ID:** `urn:csabs:concept/GeneratorMatrix`

**Categories:** Information theory → Coding theory → Channel coding

**Kind:** Mathematical structure

**Prerequisites:** [Linear block code over a finite field](LinearBlockCode.md), [Finite rectangular matrix over a field](Matrix.md)

**Related concepts:** [Parity-check matrix of a linear block code (row convention)](ParityCheckMatrix.md)

## Backlinks

- [Parity-check matrix of a linear block code (row convention)](ParityCheckMatrix.md) — `relatedConcept`
- [Parity-check matrix of a linear block code (row convention)](ParityCheckMatrix.md) — `requiresConcept`

## Mathematical formulation

The selected model stores a basis (g\_i)\_{i∈Fin(k)} of C≤F^n. Its coordinate matrix is G\_ij=(g\_i)\_j and encoding is enc(m)=Σ\_i m\_i g\_i, equivalently the row-vector product mG. The abstract basis carrier and concrete matrix are linked by a separate coordinate theorem.

**Lean formulation** (in its source module context):

```lean
abbrev GeneratorMatrix := Information.Generator
```

**Source:** [`Catalog.GeneratorMatrix`](../lean/Catalog/InformationTheory.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** A finite row basis of the exact code subspace, its inverse coordinate linear equivalence, and an explicit generatorMatrix with a compiled coordinate equation identifying encoding with mG.

**Limits:** No efficient basis-finding algorithm or runtime representation refinement.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** G has k linearly independent rows forming a basis of C, and encodeG(m)=mG.

**basisKind:** extensional-structural-definition

**basisScope:** Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state. Finite field; 0≤k≤n; row-vector encoding. k=0 uses the unique empty message and produces 0. G is a representation of C, not a canonical object.

**verificationObligation:** Map alphabets, exact arithmetic, equality, logarithm base, channel model and error criterion before use.; Retrieve explicit premises; category and specialization links do not inherit claims.

**reviewStatus:** Editorial mathematical review; Lean models are explicitly scoped and theorem sketches are not compiled proofs.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-GeneratorMatrix-linear-encode"></a>

### linear-encode

`urn:csabs:operation/GeneratorMatrix-linear-encode`

**signature:** encodeG : Generator(C)×𝔽qᵏ → C

**description:** Return the row-vector product mG.

**precondition:** Inputs satisfy the concept profile.

**totality:** Total on the stated domain.

**postcondition:** Return the row-vector product mG.

**source:** [Georg Böcherer, Lecture Notes on Channel Coding (2016)](https://arxiv.org/html/1607.00974v1); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §6.4 Definition 6.17 and generator encoding

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-GeneratorMatrix-row-basis"></a>

### row-basis

`urn:csabs:axiom/GeneratorMatrix-row-basis`

**statement:** G has k linearly independent rows forming a basis of C, and encodeG(m)=mG.

**formalStatement:** G has k linearly independent rows forming a basis of C, and encodeG(m)=mG.

**assumptions:** Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state. Finite field; 0≤k≤n; row-vector encoding. k=0 uses the unique empty message and produces 0. G is a representation of C, not a canonical object.

**ruleRole:** defining-rule

**reviewStatus:** Sourced structural definition, not an independent foundational axiom.

**source:** [Georg Böcherer, Lecture Notes on Channel Coding (2016)](https://arxiv.org/html/1607.00974v1); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §6.4 Definition 6.17 and generator encoding

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-GeneratorMatrix-encoding-isomorphism"></a>

### Generator encoding is a linear bijection

`urn:csabs:theorem/GeneratorMatrix-encoding-isomorphism`

**statement:** m↦mG is a linear bijection 𝔽qᵏ≃C.

**formalStatement:** m↦mG is a linear bijection 𝔽qᵏ≃C.

**assumptions:** Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state. Finite field; 0≤k≤n; row-vector encoding. k=0 uses the unique empty message and produces 0. G is a representation of C, not a canonical object.

**dependsOn:** [row-basis](GeneratorMatrix.md#node-urn-csabs-axiom-GeneratorMatrix-row-basis)

**proofSketch:** Independent rows give trivial kernel; spanning gives surjectivity; matrix multiplication is linear.

**reviewStatus:** Editorial statement-to-Lean correspondence review; a full-claim witness is registered separately in lean/bindings.json. Consult a fresh verification report for compiler and axiom-audit evidence.

**source:** [Georg Böcherer, Lecture Notes on Channel Coding (2016)](https://arxiv.org/html/1607.00974v1); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §6.4 Definition 6.17 and generator encoding

**sourceNote:** Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ (F : Type) [Field F] [Fintype F] (n k : ℕ) (g : Catalog.Information.Generator F n k), Function.Bijective (Catalog.Information.generatorEncode g) ∧ (∀ x y, Catalog.Information.generatorEncode g (x+y) = Catalog.Information.generatorEncode g x + Catalog.Information.generatorEncode g y) ∧ (∀ (a : F) x, Catalog.Information.generatorEncode g (a • x) = a • Catalog.Information.generatorEncode g x)
```

**Source:** [`Catalog.Information.Verified.generatorIsomorphism`](../lean/Catalog/InformationTheoryStatements.lean); consulted 2026-11-12.

**Scope:** registered-witness-type

**Interpretation:** Finite exact profile. m↦mG is a linear bijection 𝔽qᵏ≃C. The compiled Targets proposition supplies explicit carriers and hypotheses; the independently expanded expected type is retained here. Nat minima are used only under nontrivial-code assumptions; source and channel blocks use positive lengths.

**Limits:** Witness proves the entire expanded expected type; correspondence to the informal statement is a reviewed mapping. This does not prove other catalog targets or an implementation refinement.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/GeneratorMatrix-row-basis": "Explicit premise: G has k linearly independent rows forming a basis of C, and encodeG(m)=mG. Implemented by the normalized finite-law, exact finite-field, prefix-word or Hamming definitions and proved helper lemmas in InformationTheoryProofs/Statements; not introduced as a global axiom."
}
```

## Concept provenance

- [Georg Böcherer, Lecture Notes on Channel Coding (2016)](https://arxiv.org/html/1607.00974v1); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §6.4 Definition 6.17 and generator encoding

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/GeneratorMatrix",
    "type": "Concept",
    "shortForm": "GeneratorMatrix",
    "fullName": "Generator matrix of a linear block code (row convention)",
    "category": [
      "urn:csabs:category/channel-coding"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "Full-row-rank matrix whose row span is the specified code.",
    "notation": "G∈𝔽q^(k×n); C={mG:m∈𝔽qᵏ}",
    "requiresConcept": [
      "urn:csabs:concept/LinearBlockCode",
      "urn:csabs:concept/Matrix"
    ],
    "relatedConcept": [
      "urn:csabs:concept/ParityCheckMatrix"
    ],
    "hasOperation": [
      "urn:csabs:operation/GeneratorMatrix-linear-encode"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/GeneratorMatrix-row-basis"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/GeneratorMatrix-encoding-isomorphism"
    ],
    "axiomBasis": "G has k linearly independent rows forming a basis of C, and encodeG(m)=mG.",
    "basisKind": "extensional-structural-definition",
    "basisScope": "Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state. Finite field; 0≤k≤n; row-vector encoding. k=0 uses the unique empty message and produces 0. G is a representation of C, not a canonical object.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial mathematical review; Lean models are explicitly scoped and theorem sketches are not compiled proofs.",
    "verificationObligation": [
      "Map alphabets, exact arithmetic, equality, logarithm base, channel model and error criterion before use.",
      "Retrieve explicit premises; category and specialization links do not inherit claims."
    ],
    "source": [
      "urn:csabs:source/boecherer-channel-coding"
    ],
    "sourceLocator": "§6.4 Definition 6.17 and generator encoding",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted",
    "leanFormulation": "abbrev GeneratorMatrix := Information.Generator",
    "formulationSource": "urn:csabs:source/local-lean-InformationTheory",
    "formulationLocator": "Catalog.GeneratorMatrix",
    "formulationScope": "model",
    "leanModelMapping": "A finite row basis of the exact code subspace, its inverse coordinate linear equivalence, and an explicit generatorMatrix with a compiled coordinate equation identifying encoding with mG.",
    "leanModelLimitations": "No efficient basis-finding algorithm or runtime representation refinement.",
    "mathematicalFormulation": "The selected model stores a basis (g_i)_{i∈Fin(k)} of C≤F^n. Its coordinate matrix is G_ij=(g_i)_j and encoding is enc(m)=Σ_i m_i g_i, equivalently the row-vector product mG. The abstract basis carrier and concrete matrix are linked by a separate coordinate theorem."
  },
  {
    "id": "urn:csabs:operation/GeneratorMatrix-linear-encode",
    "type": "Operation",
    "name": "linear-encode",
    "signature": "encodeG : Generator(C)×𝔽qᵏ → C",
    "description": "Return the row-vector product mG.",
    "concept": "urn:csabs:concept/GeneratorMatrix",
    "precondition": "Inputs satisfy the concept profile.",
    "totality": "Total on the stated domain.",
    "postcondition": "Return the row-vector product mG.",
    "source": [
      "urn:csabs:source/boecherer-channel-coding"
    ],
    "sourceLocator": "§6.4 Definition 6.17 and generator encoding",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/GeneratorMatrix-row-basis",
    "type": "Axiom",
    "name": "row-basis",
    "statement": "G has k linearly independent rows forming a basis of C, and encodeG(m)=mG.",
    "formalStatement": "G has k linearly independent rows forming a basis of C, and encodeG(m)=mG.",
    "assumptions": [
      "Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state. Finite field; 0≤k≤n; row-vector encoding. k=0 uses the unique empty message and produces 0. G is a representation of C, not a canonical object."
    ],
    "appliesTo": [
      "urn:csabs:concept/GeneratorMatrix"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Sourced structural definition, not an independent foundational axiom.",
    "source": [
      "urn:csabs:source/boecherer-channel-coding"
    ],
    "sourceLocator": "§6.4 Definition 6.17 and generator encoding",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:theorem/GeneratorMatrix-encoding-isomorphism",
    "type": "Theorem",
    "name": "Generator encoding is a linear bijection",
    "statement": "m↦mG is a linear bijection 𝔽qᵏ≃C.",
    "formalStatement": "m↦mG is a linear bijection 𝔽qᵏ≃C.",
    "assumptions": [
      "Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state. Finite field; 0≤k≤n; row-vector encoding. k=0 uses the unique empty message and produces 0. G is a representation of C, not a canonical object."
    ],
    "appliesTo": [
      "urn:csabs:concept/GeneratorMatrix"
    ],
    "dependsOn": [
      "urn:csabs:axiom/GeneratorMatrix-row-basis"
    ],
    "proofSketch": "Independent rows give trivial kernel; spanning gives surjectivity; matrix multiplication is linear.",
    "reviewStatus": "Editorial statement-to-Lean correspondence review; a full-claim witness is registered separately in lean/bindings.json. Consult a fresh verification report for compiler and axiom-audit evidence.",
    "source": [
      "urn:csabs:source/boecherer-channel-coding"
    ],
    "sourceLocator": "§6.4 Definition 6.17 and generator encoding",
    "sourceNote": "Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ (F : Type) [Field F] [Fintype F] (n k : ℕ) (g : Catalog.Information.Generator F n k), Function.Bijective (Catalog.Information.generatorEncode g) ∧ (∀ x y, Catalog.Information.generatorEncode g (x+y) = Catalog.Information.generatorEncode g x + Catalog.Information.generatorEncode g y) ∧ (∀ (a : F) x, Catalog.Information.generatorEncode g (a • x) = a • Catalog.Information.generatorEncode g x)",
    "formulationSource": "urn:csabs:source/local-lean-InformationTheoryStatements",
    "formulationLocator": "Catalog.Information.Verified.generatorIsomorphism",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Finite exact profile. m↦mG is a linear bijection 𝔽qᵏ≃C. The compiled Targets proposition supplies explicit carriers and hypotheses; the independently expanded expected type is retained here. Nat minima are used only under nontrivial-code assumptions; source and channel blocks use positive lengths.",
    "leanModelLimitations": "Witness proves the entire expanded expected type; correspondence to the informal statement is a reviewed mapping. This does not prove other catalog targets or an implementation refinement.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/GeneratorMatrix-row-basis\": \"Explicit premise: G has k linearly independent rows forming a basis of C, and encodeG(m)=mG. Implemented by the normalized finite-law, exact finite-field, prefix-word or Hamming definitions and proved helper lemmas in InformationTheoryProofs/Statements; not introduced as a global axiom.\"}"
  }
]
```
<!-- graph-record:end -->
