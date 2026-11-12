# Full QR decomposition (real or complex, rectangular)

An exact factorization of a real or complex rectangular matrix into a square orthogonal/unitary matrix Q and an upper-trapezoidal matrix R. Rank deficiency is admitted and factor phases are not normalized.

**Notation:** A=QR; Q∈F^{m×m}, R∈F^{m×n}; QᴴQ=QQᴴ=I_m; R_ij=0 for i>j.

**Stable ID:** `urn:csabs:concept/QRDecomposition`

**Categories:** Algebra → Linear and multilinear algebra → Matrix decompositions

**Kind:** Mathematical structure

**Prerequisites:** [Exact structured matrix decomposition witness](MatrixDecomposition.md), [Exact real number](RealNumber.md), [Exact complex number](ComplexNumber.md)

**Specializes:** [Exact structured matrix decomposition witness](MatrixDecomposition.md)

**Related concepts:** [Full singular value decomposition (rectangular real or complex SVD)](SVD.md)

## Backlinks

- [Full singular value decomposition (rectangular real or complex SVD)](SVD.md) — `relatedConcept`

## Mathematical formulation

For F=ℝ or ℂ and A∈F^{m×n}, a full QR witness has Q∈F^{m×m}, QᴴQ=QQᴴ=I\_m and R∈F^{m×n} with R\_ij=0 whenever i>j, satisfying A=QR. Superscript ᴴ denotes conjugate transpose, equal to transpose over ℝ. Rank-deficient and wide matrices are allowed. Reduced/thin QR and column-pivoted QR need explicit variants; no positive-diagonal normalization or uniqueness is selected.

**Lean formulation** (in its source module context):

```lean
structure QRDecomposition {F : Type u} [RCLike F] {m n : Nat} (A : Catalog.Matrix F m n) where
  orthogonal : Catalog.Matrix F m m
  upper : Catalog.Matrix F m n
  unitary_left : orthogonal.conjTranspose * orthogonal = 1
  unitary_right : orthogonal * orthogonal.conjTranspose = 1
  upper_trapezoidal : matrixUpper upper
  reconstructs : A = orthogonal * upper
```

**Source:** [`Catalog.QRDecomposition`](../lean/Catalog/MatrixDecompositions.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** RCLike scalar F with full square orthogonal field Q, both unitary equations, rectangular upper factor and upper-trapezoidal predicate, and exact A=Q*R. RCLike is instantiated by real or complex scalars.

**Limits:** Exact selected witness/carrier model and factor observations. No factor-finding algorithm, decidable equality on real/complex entries, floating-point error analysis or general numerical implementation refinement. Only individually registered claims have compiled witnesses; existence/uniqueness results are not proved by structure fields.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Selected exact factor-carrier constraints and reconstruction equation. F is ℝ or ℂ; m,n≥0; full square Q and full-shaped upper-trapezoidal R are used. Matrix equality is exact entrywise equality and witness equality retains Q,R. Empty dimensions and rank deficiency are admitted. No floating-point norm tolerance or choice of Householder/Givens/Gram–Schmidt algorithm is implied.

**basisKind:** defined-structure

**basisScope:** This selected factorization profile, not all numerical algorithms, alternative shapes or consequences.

**convention:** F is ℝ or ℂ; m,n≥0; full square Q and full-shaped upper-trapezoidal R are used. Matrix equality is exact entrywise equality and witness equality retains Q,R. Empty dimensions and rank deficiency are admitted. No floating-point norm tolerance or choice of Householder/Givens/Gram–Schmidt algorithm is implied.

**specializationNote:** Instantiate W with unitary Q∈F^{m×m} and upper-trapezoidal R∈F^{m×n}; the reconstruction map is ρ(Q,R)=QR.

**verificationObligation:** Map factor dimensions, scalar field, adjoint/permutation conventions, equality and input guards before reusing equations in software. Approximate factors need a separately justified residual/error contract.

**reviewStatus:** Sourced mathematical interface with a separate compiled Lean interpretation and individually mapped witnesses.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-QRDecomposition-factors"></a>

### factors

`urn:csabs:operation/QRDecomposition-factors`

**signature:** QR(A) → F^{m×m}×F^{m×n}

**description:** Observe the full unitary and upper-trapezoidal factors.

**precondition:** Input is a valid full QR witness.

**postcondition:** The exact ordered pair (Q,R).

**totality:** total on the stated typed domain; no decision algorithm or factor-finding procedure is promised

<a id="node-urn-csabs-operation-QRDecomposition-reconstruct"></a>

### reconstruct

`urn:csabs:operation/QRDecomposition-reconstruct`

**signature:** F^{m×m}×F^{m×n} → F^{m×n}; (Q,R) ↦ QR

**description:** Multiply the full-shaped factors.

**precondition:** Matching dimensions.

**postcondition:** A for a valid QR witness.

**totality:** total on the stated typed domain; no decision algorithm or factor-finding procedure is promised

## Axioms and defining rules

<a id="node-urn-csabs-axiom-QRDecomposition-factor-constraints"></a>

### factor-constraints

`urn:csabs:axiom/QRDecomposition-factor-constraints`

**statement:** Q is unitary and R is upper trapezoidal in the full rectangular profile.

**formalStatement:** QᴴQ=QQᴴ=I_m; R∈F^{m×n}; ∀i,j with i>j,R_ij=0.

**assumptions:** F is ℝ or ℂ; m,n≥0; full square Q and full-shaped upper-trapezoidal R are used. Matrix equality is exact entrywise equality and witness equality retains Q,R. Empty dimensions and rank deficiency are admitted. No floating-point norm tolerance or choice of Householder/Givens/Gram–Schmidt algorithm is implied.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Mathematical definition; separate Lean evidence describes compiled interpretations.

**source:** [LAPACK Users’ Guide, Third Edition: QR Factorization](https://netlib.org/lapack/lug/node40.html); accessedOn: 2026-11-12; sourceRole: Consulted mathematical definition and factorization exposition; numerical algorithm/storage details are outside the selected exact model.

**sourceLocator:** LAPACK Users’ Guide §2.4.2.1, full and reduced QR and the m<n case

**sourceNote:** Combines the source’s triangular block and zero padding into one m×n upper-trapezoidal R. Keeps full Q, covers both dimension orders, and extends the exact identities to zero dimensions. The selected relation has no pivoting or phase normalization.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-QRDecomposition-reconstruction"></a>

### reconstruction

`urn:csabs:axiom/QRDecomposition-reconstruction`

**statement:** The factors reconstruct the input.

**formalStatement:** A=QR.

**assumptions:** F is ℝ or ℂ; m,n≥0; full square Q and full-shaped upper-trapezoidal R are used. Matrix equality is exact entrywise equality and witness equality retains Q,R. Empty dimensions and rank deficiency are admitted. No floating-point norm tolerance or choice of Householder/Givens/Gram–Schmidt algorithm is implied.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Mathematical definition; separate Lean evidence describes compiled interpretations.

**source:** [LAPACK Users’ Guide, Third Edition: QR Factorization](https://netlib.org/lapack/lug/node40.html); accessedOn: 2026-11-12; sourceRole: Consulted mathematical definition and factorization exposition; numerical algorithm/storage details are outside the selected exact model.

**sourceLocator:** LAPACK Users’ Guide §2.4.2.1, full and reduced QR and the m<n case

**sourceNote:** Combines the source’s triangular block and zero padding into one m×n upper-trapezoidal R. Keeps full Q, covers both dimension orders, and extends the exact identities to zero dimensions. The selected relation has no pivoting or phase normalization.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-QRDecomposition-gram"></a>

### gram

`urn:csabs:law/QRDecomposition-gram`

**statement:** QR preserves the input Gram matrix in R.

**formalStatement:** AᴴA=RᴴR.

**assumptions:** F is ℝ or ℂ; m,n≥0; full square Q and full-shaped upper-trapezoidal R are used. Matrix equality is exact entrywise equality and witness equality retains Q,R. Empty dimensions and rank deficiency are admitted. No floating-point norm tolerance or choice of Householder/Givens/Gram–Schmidt algorithm is implied.

**ruleRole:** derived-result

**dependsOn:** [factor-constraints](QRDecomposition.md#node-urn-csabs-axiom-QRDecomposition-factor-constraints); [reconstruction](QRDecomposition.md#node-urn-csabs-axiom-QRDecomposition-reconstruction)

**proofSketch:** Substitute A=QR and use (QR)ᴴ=RᴴQᴴ, associativity and QᴴQ=I. No rank assumption is used.

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial mathematical statement; only separately registered fresh Lean witnesses are compiler-verified.

**source:** [LAPACK Users’ Guide, Third Edition: QR Factorization](https://netlib.org/lapack/lug/node40.html); accessedOn: 2026-11-12; sourceRole: Consulted mathematical definition and factorization exposition; numerical algorithm/storage details are outside the selected exact model.

**sourceLocator:** LAPACK Users’ Guide §2.4.2.1, full and reduced QR and the m<n case

**sourceNote:** Derives the selected result from the linked factor constraints/reconstruction, using exact matrix algebra. Combines the source’s triangular block and zero padding into one m×n upper-trapezoidal R. Keeps full Q, covers both dimension orders, and extends the exact identities to zero dimensions. The selected relation has no pivoting or phase normalization.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {F : Type u} [RCLike F] {m n : Nat} {A : Catalog.Matrix F m n} (d : Catalog.QRDecomposition A), A.conjTranspose * A = d.upper.conjTranspose * d.upper
```

**Source:** [`Catalog.MatrixDecompositionProofs.qr_gram`](../lean/Catalog/MatrixDecompositions.lean); consulted 2026-11-12.

**Scope:** registered-witness-type

**Interpretation:** RCLike scalar F with full square orthogonal field Q, both unitary equations, rectangular upper factor and upper-trapezoidal predicate, and exact A=Q*R. RCLike is instantiated by real or complex scalars.

**Limits:** Proves the displayed algebraic identity for a supplied valid witness, under the mapped exact scalar/dimension conventions. It does not prove factor existence/uniqueness, a numerical algorithm, stability or implementation conformance.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/QRDecomposition-factor-constraints": "The corresponding explicit structure fields supply this premise: Q*Q=QQ*=I_m; R∈F^{m×n}; ∀i,j with i>j,R_ij=0. The proof uses the unitary or inverse identities; unused triangular/order/positivity fields remain profile constraints.",
  "urn:csabs:axiom/QRDecomposition-reconstruction": "The corresponding explicit structure fields supply this premise: A=QR. The proof uses the unitary or inverse identities; unused triangular/order/positivity fields remain profile constraints."
}
```

## Theorems

<a id="node-urn-csabs-theorem-QRDecomposition-existence"></a>

### existence

`urn:csabs:theorem/QRDecomposition-existence`

**statement:** Every real or complex rectangular matrix has a full QR factorization.

**formalStatement:** ∀A∈F^{m×n}, ∃Q,R, QᴴQ=QQᴴ=I_m ∧ (∀i>j,R_ij=0) ∧ A=QR.

**assumptions:** F is ℝ or ℂ; m,n≥0; full square Q and full-shaped upper-trapezoidal R are used. Matrix equality is exact entrywise equality and witness equality retains Q,R. Empty dimensions and rank deficiency are admitted. No floating-point norm tolerance or choice of Householder/Givens/Gram–Schmidt algorithm is implied.

**ruleRole:** derived-result

**dependsOn:** [factor-constraints](QRDecomposition.md#node-urn-csabs-axiom-QRDecomposition-factor-constraints); [reconstruction](QRDecomposition.md#node-urn-csabs-axiom-QRDecomposition-reconstruction)

**proofSketch:** An orthogonal/unitary triangularization (for example successive reflectors) reduces the columns to upper-trapezoidal form; extend/combine the orthonormal transformations into full Q. Empty dimensions give the unique empty products. This is an editorial existence result, not a factor-finding implementation.

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial mathematical statement; only separately registered fresh Lean witnesses are compiler-verified.

**source:** [LAPACK Users’ Guide, Third Edition: QR Factorization](https://netlib.org/lapack/lug/node40.html); accessedOn: 2026-11-12; sourceRole: Consulted mathematical definition and factorization exposition; numerical algorithm/storage details are outside the selected exact model.

**sourceLocator:** LAPACK Users’ Guide §2.4.2.1, full and reduced QR and the m<n case

**sourceNote:** Derives the selected result from the linked factor constraints/reconstruction, using exact matrix algebra. Combines the source’s triangular block and zero padding into one m×n upper-trapezoidal R. Keeps full Q, covers both dimension orders, and extends the exact identities to zero dimensions. The selected relation has no pivoting or phase normalization.

**provenanceKind:** derived

## Concept provenance

- [LAPACK Users’ Guide, Third Edition: QR Factorization](https://netlib.org/lapack/lug/node40.html); accessedOn: 2026-11-12; sourceRole: Consulted mathematical definition and factorization exposition; numerical algorithm/storage details are outside the selected exact model.

**sourceLocator:** LAPACK Users’ Guide §2.4.2.1, full and reduced QR and the m<n case

**sourceNote:** Combines the source’s triangular block and zero padding into one m×n upper-trapezoidal R. Keeps full Q, covers both dimension orders, and extends the exact identities to zero dimensions. The selected relation has no pivoting or phase normalization.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/QRDecomposition",
    "type": "Concept",
    "shortForm": "QRDecomposition",
    "fullName": "Full QR decomposition (real or complex, rectangular)",
    "category": [
      "urn:csabs:category/matrix-decompositions"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "An exact factorization of a real or complex rectangular matrix into a square orthogonal/unitary matrix Q and an upper-trapezoidal matrix R. Rank deficiency is admitted and factor phases are not normalized.",
    "notation": "A=QR; Q∈F^{m×m}, R∈F^{m×n}; QᴴQ=QQᴴ=I_m; R_ij=0 for i>j.",
    "mathematicalFormulation": "For F=ℝ or ℂ and A∈F^{m×n}, a full QR witness has Q∈F^{m×m}, QᴴQ=QQᴴ=I_m and R∈F^{m×n} with R_ij=0 whenever i>j, satisfying A=QR. Superscript ᴴ denotes conjugate transpose, equal to transpose over ℝ. Rank-deficient and wide matrices are allowed. Reduced/thin QR and column-pivoted QR need explicit variants; no positive-diagonal normalization or uniqueness is selected.",
    "hasOperation": [
      "urn:csabs:operation/QRDecomposition-factors",
      "urn:csabs:operation/QRDecomposition-reconstruct"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/QRDecomposition-factor-constraints",
      "urn:csabs:axiom/QRDecomposition-reconstruction"
    ],
    "hasLaw": [
      "urn:csabs:law/QRDecomposition-gram"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/QRDecomposition-existence"
    ],
    "requiresConcept": [
      "urn:csabs:concept/MatrixDecomposition",
      "urn:csabs:concept/RealNumber",
      "urn:csabs:concept/ComplexNumber"
    ],
    "relatedConcept": [
      "urn:csabs:concept/SVD"
    ],
    "axiomBasis": "Selected exact factor-carrier constraints and reconstruction equation. F is ℝ or ℂ; m,n≥0; full square Q and full-shaped upper-trapezoidal R are used. Matrix equality is exact entrywise equality and witness equality retains Q,R. Empty dimensions and rank deficiency are admitted. No floating-point norm tolerance or choice of Householder/Givens/Gram–Schmidt algorithm is implied.",
    "basisKind": "defined-structure",
    "basisScope": "This selected factorization profile, not all numerical algorithms, alternative shapes or consequences.",
    "convention": "F is ℝ or ℂ; m,n≥0; full square Q and full-shaped upper-trapezoidal R are used. Matrix equality is exact entrywise equality and witness equality retains Q,R. Empty dimensions and rank deficiency are admitted. No floating-point norm tolerance or choice of Householder/Givens/Gram–Schmidt algorithm is implied.",
    "verificationObligation": "Map factor dimensions, scalar field, adjoint/permutation conventions, equality and input guards before reusing equations in software. Approximate factors need a separately justified residual/error contract.",
    "reviewStatus": "Sourced mathematical interface with a separate compiled Lean interpretation and individually mapped witnesses.",
    "coverageStatus": "basis-reviewed",
    "source": [
      "urn:csabs:source/lapack-lug-qr"
    ],
    "sourceLocator": "LAPACK Users’ Guide §2.4.2.1, full and reduced QR and the m<n case",
    "sourceNote": "Combines the source’s triangular block and zero padding into one m×n upper-trapezoidal R. Keeps full Q, covers both dimension orders, and extends the exact identities to zero dimensions. The selected relation has no pivoting or phase normalization.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/MatrixDecomposition"
    ],
    "specializationNote": "Instantiate W with unitary Q∈F^{m×m} and upper-trapezoidal R∈F^{m×n}; the reconstruction map is ρ(Q,R)=QR.",
    "leanFormulation": "structure QRDecomposition {F : Type u} [RCLike F] {m n : Nat} (A : Catalog.Matrix F m n) where\n  orthogonal : Catalog.Matrix F m m\n  upper : Catalog.Matrix F m n\n  unitary_left : orthogonal.conjTranspose * orthogonal = 1\n  unitary_right : orthogonal * orthogonal.conjTranspose = 1\n  upper_trapezoidal : matrixUpper upper\n  reconstructs : A = orthogonal * upper",
    "formulationSource": "urn:csabs:source/local-lean-MatrixDecompositions",
    "formulationLocator": "Catalog.QRDecomposition",
    "formulationScope": "model",
    "leanModelMapping": "RCLike scalar F with full square orthogonal field Q, both unitary equations, rectangular upper factor and upper-trapezoidal predicate, and exact A=Q*R. RCLike is instantiated by real or complex scalars.",
    "leanModelLimitations": "Exact selected witness/carrier model and factor observations. No factor-finding algorithm, decidable equality on real/complex entries, floating-point error analysis or general numerical implementation refinement. Only individually registered claims have compiled witnesses; existence/uniqueness results are not proved by structure fields."
  },
  {
    "id": "urn:csabs:operation/QRDecomposition-factors",
    "type": "Operation",
    "name": "factors",
    "concept": "urn:csabs:concept/QRDecomposition",
    "signature": "QR(A) → F^{m×m}×F^{m×n}",
    "description": "Observe the full unitary and upper-trapezoidal factors.",
    "precondition": "Input is a valid full QR witness.",
    "postcondition": "The exact ordered pair (Q,R).",
    "totality": "total on the stated typed domain; no decision algorithm or factor-finding procedure is promised"
  },
  {
    "id": "urn:csabs:operation/QRDecomposition-reconstruct",
    "type": "Operation",
    "name": "reconstruct",
    "concept": "urn:csabs:concept/QRDecomposition",
    "signature": "F^{m×m}×F^{m×n} → F^{m×n}; (Q,R) ↦ QR",
    "description": "Multiply the full-shaped factors.",
    "precondition": "Matching dimensions.",
    "postcondition": "A for a valid QR witness.",
    "totality": "total on the stated typed domain; no decision algorithm or factor-finding procedure is promised"
  },
  {
    "id": "urn:csabs:axiom/QRDecomposition-factor-constraints",
    "type": "Axiom",
    "name": "factor-constraints",
    "statement": "Q is unitary and R is upper trapezoidal in the full rectangular profile.",
    "formalStatement": "QᴴQ=QQᴴ=I_m; R∈F^{m×n}; ∀i,j with i>j,R_ij=0.",
    "assumptions": [
      "F is ℝ or ℂ; m,n≥0; full square Q and full-shaped upper-trapezoidal R are used. Matrix equality is exact entrywise equality and witness equality retains Q,R. Empty dimensions and rank deficiency are admitted. No floating-point norm tolerance or choice of Householder/Givens/Gram–Schmidt algorithm is implied."
    ],
    "appliesTo": [
      "urn:csabs:concept/QRDecomposition"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Mathematical definition; separate Lean evidence describes compiled interpretations.",
    "source": [
      "urn:csabs:source/lapack-lug-qr"
    ],
    "sourceLocator": "LAPACK Users’ Guide §2.4.2.1, full and reduced QR and the m<n case",
    "sourceNote": "Combines the source’s triangular block and zero padding into one m×n upper-trapezoidal R. Keeps full Q, covers both dimension orders, and extends the exact identities to zero dimensions. The selected relation has no pivoting or phase normalization.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/QRDecomposition-reconstruction",
    "type": "Axiom",
    "name": "reconstruction",
    "statement": "The factors reconstruct the input.",
    "formalStatement": "A=QR.",
    "assumptions": [
      "F is ℝ or ℂ; m,n≥0; full square Q and full-shaped upper-trapezoidal R are used. Matrix equality is exact entrywise equality and witness equality retains Q,R. Empty dimensions and rank deficiency are admitted. No floating-point norm tolerance or choice of Householder/Givens/Gram–Schmidt algorithm is implied."
    ],
    "appliesTo": [
      "urn:csabs:concept/QRDecomposition"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Mathematical definition; separate Lean evidence describes compiled interpretations.",
    "source": [
      "urn:csabs:source/lapack-lug-qr"
    ],
    "sourceLocator": "LAPACK Users’ Guide §2.4.2.1, full and reduced QR and the m<n case",
    "sourceNote": "Combines the source’s triangular block and zero padding into one m×n upper-trapezoidal R. Keeps full Q, covers both dimension orders, and extends the exact identities to zero dimensions. The selected relation has no pivoting or phase normalization.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/QRDecomposition-gram",
    "type": "Law",
    "name": "gram",
    "statement": "QR preserves the input Gram matrix in R.",
    "formalStatement": "AᴴA=RᴴR.",
    "assumptions": [
      "F is ℝ or ℂ; m,n≥0; full square Q and full-shaped upper-trapezoidal R are used. Matrix equality is exact entrywise equality and witness equality retains Q,R. Empty dimensions and rank deficiency are admitted. No floating-point norm tolerance or choice of Householder/Givens/Gram–Schmidt algorithm is implied."
    ],
    "appliesTo": [
      "urn:csabs:concept/QRDecomposition"
    ],
    "ruleRole": "derived-result",
    "dependsOn": [
      "urn:csabs:axiom/QRDecomposition-factor-constraints",
      "urn:csabs:axiom/QRDecomposition-reconstruction"
    ],
    "proofSketch": "Substitute A=QR and use (QR)ᴴ=RᴴQᴴ, associativity and QᴴQ=I. No rank assumption is used.",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial mathematical statement; only separately registered fresh Lean witnesses are compiler-verified.",
    "source": [
      "urn:csabs:source/lapack-lug-qr"
    ],
    "sourceLocator": "LAPACK Users’ Guide §2.4.2.1, full and reduced QR and the m<n case",
    "sourceNote": "Derives the selected result from the linked factor constraints/reconstruction, using exact matrix algebra. Combines the source’s triangular block and zero padding into one m×n upper-trapezoidal R. Keeps full Q, covers both dimension orders, and extends the exact identities to zero dimensions. The selected relation has no pivoting or phase normalization.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {F : Type u} [RCLike F] {m n : Nat} {A : Catalog.Matrix F m n} (d : Catalog.QRDecomposition A), A.conjTranspose * A = d.upper.conjTranspose * d.upper",
    "formulationSource": "urn:csabs:source/local-lean-MatrixDecompositions",
    "formulationLocator": "Catalog.MatrixDecompositionProofs.qr_gram",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "RCLike scalar F with full square orthogonal field Q, both unitary equations, rectangular upper factor and upper-trapezoidal predicate, and exact A=Q*R. RCLike is instantiated by real or complex scalars.",
    "leanModelLimitations": "Proves the displayed algebraic identity for a supplied valid witness, under the mapped exact scalar/dimension conventions. It does not prove factor existence/uniqueness, a numerical algorithm, stability or implementation conformance.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/QRDecomposition-factor-constraints\": \"The corresponding explicit structure fields supply this premise: Q*Q=QQ*=I_m; R∈F^{m×n}; ∀i,j with i>j,R_ij=0. The proof uses the unitary or inverse identities; unused triangular/order/positivity fields remain profile constraints.\", \"urn:csabs:axiom/QRDecomposition-reconstruction\": \"The corresponding explicit structure fields supply this premise: A=QR. The proof uses the unitary or inverse identities; unused triangular/order/positivity fields remain profile constraints.\"}"
  },
  {
    "id": "urn:csabs:theorem/QRDecomposition-existence",
    "type": "Theorem",
    "name": "existence",
    "statement": "Every real or complex rectangular matrix has a full QR factorization.",
    "formalStatement": "∀A∈F^{m×n}, ∃Q,R, QᴴQ=QQᴴ=I_m ∧ (∀i>j,R_ij=0) ∧ A=QR.",
    "assumptions": [
      "F is ℝ or ℂ; m,n≥0; full square Q and full-shaped upper-trapezoidal R are used. Matrix equality is exact entrywise equality and witness equality retains Q,R. Empty dimensions and rank deficiency are admitted. No floating-point norm tolerance or choice of Householder/Givens/Gram–Schmidt algorithm is implied."
    ],
    "appliesTo": [
      "urn:csabs:concept/QRDecomposition"
    ],
    "ruleRole": "derived-result",
    "dependsOn": [
      "urn:csabs:axiom/QRDecomposition-factor-constraints",
      "urn:csabs:axiom/QRDecomposition-reconstruction"
    ],
    "proofSketch": "An orthogonal/unitary triangularization (for example successive reflectors) reduces the columns to upper-trapezoidal form; extend/combine the orthonormal transformations into full Q. Empty dimensions give the unique empty products. This is an editorial existence result, not a factor-finding implementation.",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial mathematical statement; only separately registered fresh Lean witnesses are compiler-verified.",
    "source": [
      "urn:csabs:source/lapack-lug-qr"
    ],
    "sourceLocator": "LAPACK Users’ Guide §2.4.2.1, full and reduced QR and the m<n case",
    "sourceNote": "Derives the selected result from the linked factor constraints/reconstruction, using exact matrix algebra. Combines the source’s triangular block and zero padding into one m×n upper-trapezoidal R. Keeps full Q, covers both dimension orders, and extends the exact identities to zero dimensions. The selected relation has no pivoting or phase normalization.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
