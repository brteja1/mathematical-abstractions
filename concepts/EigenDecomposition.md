# Eigendecomposition by a complete eigenbasis (diagonalization)

An exact similarity to a diagonal matrix, with a complete invertible eigenvector matrix V and an explicit inverse. The relation is defined only for matrices diagonalizable over the selected scalar field.

**Notation:** A=VΛV⁻¹; Λ=diag(λ₀,…,λ_{n−1}); VV⁻¹=V⁻¹V=I_n.

**Stable ID:** `urn:csabs:concept/EigenDecomposition`

**Categories:** Algebra → Linear and multilinear algebra → Matrix decompositions

**Kind:** Mathematical structure

**Prerequisites:** [Exact structured matrix decomposition witness](MatrixDecomposition.md)

**Specializes:** [Exact structured matrix decomposition witness](MatrixDecomposition.md)

**Related concepts:** [Full singular value decomposition (rectangular real or complex SVD)](SVD.md)

## Backlinks

- [Full singular value decomposition (rectangular real or complex SVD)](SVD.md) — `relatedConcept`

## Mathematical formulation

For a field F and A∈F^{n×n}, a witness consists of V,W∈F^{n×n} and λ∈F^n with WV=VW=I\_n and A=V diag(λ)W. Thus W=V⁻¹ and the columns of V form an eigenbasis. Existence is equivalent to diagonalizability over F, not invertibility of A. Eigenvalue order, eigenvector scale and bases within repeated eigenspaces are not normalized. A defective matrix may lack a witness even over ℂ; this is not a Schur decomposition.

**Lean formulation** (in its source module context):

```lean
structure EigenDecomposition {F : Type u} [Field F] {n : Nat} (A : Catalog.Matrix F n n) where
  vectors : Catalog.Matrix F n n
  inverse : Catalog.Matrix F n n
  eigenvalues : Fin n → F
  inverse_left : inverse * vectors = 1
  inverse_right : vectors * inverse = 1
  reconstructs : A = vectors * _root_.Matrix.diagonal eigenvalues * inverse
```

**Source:** [`Catalog.EigenDecomposition`](../lean/Catalog/MatrixDecompositions.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Field F, basis matrix vectors, an explicitly supplied two-sided inverse, scalar eigenvalues and exact similarity. No global diagonalizability or eigenvalue-existence axiom is introduced; a defective matrix has no such structure value.

**Limits:** Exact selected witness/carrier model and factor observations. No factor-finding algorithm, decidable equality on real/complex entries, floating-point error analysis or general numerical implementation refinement. Only individually registered claims have compiled witnesses; existence/uniqueness results are not proved by structure fields.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Selected exact factor-carrier constraints and reconstruction equation. F is a field; n≥0; all eigenvalues and eigenvectors lie in F. A witness requires a full invertible V, not merely one eigenpair or n eigenvalues counted with multiplicity. Equality is exact and retains chosen V,λ; the inverse is uniquely determined by V. No orthogonality is required for a general eigenbasis, and no rounded eigensolver is modeled.

**basisKind:** defined-structure

**basisScope:** This selected factorization profile, not all numerical algorithms, alternative shapes or consequences.

**convention:** F is a field; n≥0; all eigenvalues and eigenvectors lie in F. A witness requires a full invertible V, not merely one eigenpair or n eigenvalues counted with multiplicity. Equality is exact and retains chosen V,λ; the inverse is uniquely determined by V. No orthogonality is required for a general eigenbasis, and no rounded eigensolver is modeled.

**specializationNote:** Instantiate W with an invertible V and scalar diagonal λ (optionally storing its uniquely determined inverse W); reconstruction is ρ(V,λ)=V diag(λ)V⁻¹.

**verificationObligation:** Map factor dimensions, scalar field, adjoint/permutation conventions, equality and input guards before reusing equations in software. Approximate factors need a separately justified residual/error contract.

**reviewStatus:** Sourced mathematical interface with a separate compiled Lean interpretation and individually mapped witnesses.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-EigenDecomposition-factors"></a>

### factors

`urn:csabs:operation/EigenDecomposition-factors`

**signature:** Eigen(A) → F^{n×n}×F^n×F^{n×n}

**description:** Observe the eigenvector basis, ordered eigenvalues and inverse.

**precondition:** A valid eigendecomposition witness exists over F.

**postcondition:** The exact tuple (V,λ,W).

**totality:** total on the stated typed domain; no decision algorithm or factor-finding procedure is promised

<a id="node-urn-csabs-operation-EigenDecomposition-reconstruct"></a>

### reconstruct

`urn:csabs:operation/EigenDecomposition-reconstruct`

**signature:** F^{n×n}×F^n×F^{n×n} → F^{n×n}; (V,λ,W) ↦ V diag(λ)W

**description:** Reconstruct from an explicitly supplied inverse factor.

**precondition:** Matching square dimensions; validity additionally requires WV=VW=I.

**postcondition:** A for a valid witness; the raw expression remains total without computing an inverse.

**totality:** total on the stated typed domain; no decision algorithm or factor-finding procedure is promised

## Axioms and defining rules

<a id="node-urn-csabs-axiom-EigenDecomposition-factor-constraints"></a>

### factor-constraints

`urn:csabs:axiom/EigenDecomposition-factor-constraints`

**statement:** The basis change is invertible and the middle factor is diagonal over the chosen field.

**formalStatement:** V,W∈F^{n×n}; WV=VW=I_n; λ∈F^n; Λ=diag(λ).

**assumptions:** F is a field; n≥0; all eigenvalues and eigenvectors lie in F. A witness requires a full invertible V, not merely one eigenpair or n eigenvalues counted with multiplicity. Equality is exact and retains chosen V,λ; the inverse is uniquely determined by V. No orthogonality is required for a general eigenbasis, and no rounded eigensolver is modeled.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Mathematical definition; separate Lean evidence describes compiled interpretations.

**source:** [Interactive Linear Algebra: §5.4 Diagonalization](https://textbooks.math.gatech.edu/ila/diagonalization.html); accessedOn: 2026-11-12; sourceRole: Consulted mathematical definition and factorization exposition; numerical algorithm/storage details are outside the selected exact model.

**sourceLocator:** Interactive Linear Algebra §5.4.1, definition, Diagonalization Theorem and proof, non-uniqueness and shear/rotation examples

**sourceNote:** Adapts the real diagonalization equations and their algebraic proof to an arbitrary chosen field, explicitly retaining an inverse witness and field-relative existence. Extends the conventions to dimension zero. Does not substitute Schur triangularization for diagonalization.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-EigenDecomposition-reconstruction"></a>

### reconstruction

`urn:csabs:axiom/EigenDecomposition-reconstruction`

**statement:** The input is similar to the diagonal factor.

**formalStatement:** A=VΛW.

**assumptions:** F is a field; n≥0; all eigenvalues and eigenvectors lie in F. A witness requires a full invertible V, not merely one eigenpair or n eigenvalues counted with multiplicity. Equality is exact and retains chosen V,λ; the inverse is uniquely determined by V. No orthogonality is required for a general eigenbasis, and no rounded eigensolver is modeled.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Mathematical definition; separate Lean evidence describes compiled interpretations.

**source:** [Interactive Linear Algebra: §5.4 Diagonalization](https://textbooks.math.gatech.edu/ila/diagonalization.html); accessedOn: 2026-11-12; sourceRole: Consulted mathematical definition and factorization exposition; numerical algorithm/storage details are outside the selected exact model.

**sourceLocator:** Interactive Linear Algebra §5.4.1, definition, Diagonalization Theorem and proof, non-uniqueness and shear/rotation examples

**sourceNote:** Adapts the real diagonalization equations and their algebraic proof to an arbitrary chosen field, explicitly retaining an inverse witness and field-relative existence. Extends the conventions to dimension zero. Does not substitute Schur triangularization for diagonalization.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-EigenDecomposition-basis-equation"></a>

### basis-equation

`urn:csabs:law/EigenDecomposition-basis-equation`

**statement:** The input acts diagonally in the selected eigenbasis.

**formalStatement:** AV=VΛ.

**assumptions:** F is a field; n≥0; all eigenvalues and eigenvectors lie in F. A witness requires a full invertible V, not merely one eigenpair or n eigenvalues counted with multiplicity. Equality is exact and retains chosen V,λ; the inverse is uniquely determined by V. No orthogonality is required for a general eigenbasis, and no rounded eigensolver is modeled.

**ruleRole:** derived-result

**dependsOn:** [factor-constraints](EigenDecomposition.md#node-urn-csabs-axiom-EigenDecomposition-factor-constraints); [reconstruction](EigenDecomposition.md#node-urn-csabs-axiom-EigenDecomposition-reconstruction)

**proofSketch:** Multiply A=VΛW on the right by V and use WV=I. The column equations are Av_i=λ_i v_i.

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial mathematical statement; only separately registered fresh Lean witnesses are compiler-verified.

**source:** [Interactive Linear Algebra: §5.4 Diagonalization](https://textbooks.math.gatech.edu/ila/diagonalization.html); accessedOn: 2026-11-12; sourceRole: Consulted mathematical definition and factorization exposition; numerical algorithm/storage details are outside the selected exact model.

**sourceLocator:** Interactive Linear Algebra §5.4.1, definition, Diagonalization Theorem and proof, non-uniqueness and shear/rotation examples

**sourceNote:** Derives the selected result from the linked factor constraints/reconstruction, using exact matrix algebra. Adapts the real diagonalization equations and their algebraic proof to an arbitrary chosen field, explicitly retaining an inverse witness and field-relative existence. Extends the conventions to dimension zero. Does not substitute Schur triangularization for diagonalization.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {F : Type u} [Field F] {n : Nat} {A : Catalog.Matrix F n n} (d : Catalog.EigenDecomposition A), A * d.vectors = d.vectors * Matrix.diagonal d.eigenvalues
```

**Source:** [`Catalog.MatrixDecompositionProofs.eigen_basis_equation`](../lean/Catalog/MatrixDecompositions.lean); consulted 2026-11-12.

**Scope:** registered-witness-type

**Interpretation:** Field F, basis matrix vectors, an explicitly supplied two-sided inverse, scalar eigenvalues and exact similarity. No global diagonalizability or eigenvalue-existence axiom is introduced; a defective matrix has no such structure value.

**Limits:** Proves the displayed algebraic identity for a supplied valid witness, under the mapped exact scalar/dimension conventions. It does not prove factor existence/uniqueness, a numerical algorithm, stability or implementation conformance.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/EigenDecomposition-factor-constraints": "The corresponding explicit structure fields supply this premise: V,W∈F^{n×n}; WV=VW=I_n; λ∈F^n; Λ=diag(λ). The proof uses the unitary or inverse identities; unused triangular/order/positivity fields remain profile constraints.",
  "urn:csabs:axiom/EigenDecomposition-reconstruction": "The corresponding explicit structure fields supply this premise: A=VΛW. The proof uses the unitary or inverse identities; unused triangular/order/positivity fields remain profile constraints."
}
```

## Theorems

<a id="node-urn-csabs-theorem-EigenDecomposition-eigenbasis-criterion"></a>

### eigenbasis-criterion

`urn:csabs:theorem/EigenDecomposition-eigenbasis-criterion`

**statement:** A square matrix is diagonalizable over F exactly when it has an F-basis of eigenvectors.

**formalStatement:** (∃V,W,λ, WV=VW=I_n ∧ A=V diag(λ)W) ⇔ (∃basis (v_i)_{i<n} of F^n, ∃λ∈F^n, ∀i,Av_i=λ_i v_i).

**assumptions:** F is a field; n≥0; all eigenvalues and eigenvectors lie in F. A witness requires a full invertible V, not merely one eigenpair or n eigenvalues counted with multiplicity. Equality is exact and retains chosen V,λ; the inverse is uniquely determined by V. No orthogonality is required for a general eigenbasis, and no rounded eigensolver is modeled.

**ruleRole:** derived-result

**dependsOn:** [factor-constraints](EigenDecomposition.md#node-urn-csabs-axiom-EigenDecomposition-factor-constraints); [reconstruction](EigenDecomposition.md#node-urn-csabs-axiom-EigenDecomposition-reconstruction)

**proofSketch:** From a witness use the columns of invertible V and AV=VΛ. Conversely form V from the supplied basis, take its inverse W, assemble AV=VΛ columnwise and multiply by W. The argument is algebraic and does not require F to be algebraically closed.

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial mathematical statement; only separately registered fresh Lean witnesses are compiler-verified.

**source:** [Interactive Linear Algebra: §5.4 Diagonalization](https://textbooks.math.gatech.edu/ila/diagonalization.html); accessedOn: 2026-11-12; sourceRole: Consulted mathematical definition and factorization exposition; numerical algorithm/storage details are outside the selected exact model.

**sourceLocator:** Interactive Linear Algebra §5.4.1, definition, Diagonalization Theorem and proof, non-uniqueness and shear/rotation examples

**sourceNote:** Derives the selected result from the linked factor constraints/reconstruction, using exact matrix algebra. Adapts the real diagonalization equations and their algebraic proof to an arbitrary chosen field, explicitly retaining an inverse witness and field-relative existence. Extends the conventions to dimension zero. Does not substitute Schur triangularization for diagonalization.

**provenanceKind:** derived

## Concept provenance

- [Interactive Linear Algebra: §5.4 Diagonalization](https://textbooks.math.gatech.edu/ila/diagonalization.html); accessedOn: 2026-11-12; sourceRole: Consulted mathematical definition and factorization exposition; numerical algorithm/storage details are outside the selected exact model.

**sourceLocator:** Interactive Linear Algebra §5.4.1, definition, Diagonalization Theorem and proof, non-uniqueness and shear/rotation examples

**sourceNote:** Adapts the real diagonalization equations and their algebraic proof to an arbitrary chosen field, explicitly retaining an inverse witness and field-relative existence. Extends the conventions to dimension zero. Does not substitute Schur triangularization for diagonalization.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/EigenDecomposition",
    "type": "Concept",
    "shortForm": "EigenDecomposition",
    "fullName": "Eigendecomposition by a complete eigenbasis (diagonalization)",
    "category": [
      "urn:csabs:category/matrix-decompositions"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "An exact similarity to a diagonal matrix, with a complete invertible eigenvector matrix V and an explicit inverse. The relation is defined only for matrices diagonalizable over the selected scalar field.",
    "notation": "A=VΛV⁻¹; Λ=diag(λ₀,…,λ_{n−1}); VV⁻¹=V⁻¹V=I_n.",
    "mathematicalFormulation": "For a field F and A∈F^{n×n}, a witness consists of V,W∈F^{n×n} and λ∈F^n with WV=VW=I_n and A=V diag(λ)W. Thus W=V⁻¹ and the columns of V form an eigenbasis. Existence is equivalent to diagonalizability over F, not invertibility of A. Eigenvalue order, eigenvector scale and bases within repeated eigenspaces are not normalized. A defective matrix may lack a witness even over ℂ; this is not a Schur decomposition.",
    "hasOperation": [
      "urn:csabs:operation/EigenDecomposition-factors",
      "urn:csabs:operation/EigenDecomposition-reconstruct"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/EigenDecomposition-factor-constraints",
      "urn:csabs:axiom/EigenDecomposition-reconstruction"
    ],
    "hasLaw": [
      "urn:csabs:law/EigenDecomposition-basis-equation"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/EigenDecomposition-eigenbasis-criterion"
    ],
    "requiresConcept": [
      "urn:csabs:concept/MatrixDecomposition"
    ],
    "relatedConcept": [
      "urn:csabs:concept/SVD"
    ],
    "axiomBasis": "Selected exact factor-carrier constraints and reconstruction equation. F is a field; n≥0; all eigenvalues and eigenvectors lie in F. A witness requires a full invertible V, not merely one eigenpair or n eigenvalues counted with multiplicity. Equality is exact and retains chosen V,λ; the inverse is uniquely determined by V. No orthogonality is required for a general eigenbasis, and no rounded eigensolver is modeled.",
    "basisKind": "defined-structure",
    "basisScope": "This selected factorization profile, not all numerical algorithms, alternative shapes or consequences.",
    "convention": "F is a field; n≥0; all eigenvalues and eigenvectors lie in F. A witness requires a full invertible V, not merely one eigenpair or n eigenvalues counted with multiplicity. Equality is exact and retains chosen V,λ; the inverse is uniquely determined by V. No orthogonality is required for a general eigenbasis, and no rounded eigensolver is modeled.",
    "verificationObligation": "Map factor dimensions, scalar field, adjoint/permutation conventions, equality and input guards before reusing equations in software. Approximate factors need a separately justified residual/error contract.",
    "reviewStatus": "Sourced mathematical interface with a separate compiled Lean interpretation and individually mapped witnesses.",
    "coverageStatus": "basis-reviewed",
    "source": [
      "urn:csabs:source/ila-diagonalization"
    ],
    "sourceLocator": "Interactive Linear Algebra §5.4.1, definition, Diagonalization Theorem and proof, non-uniqueness and shear/rotation examples",
    "sourceNote": "Adapts the real diagonalization equations and their algebraic proof to an arbitrary chosen field, explicitly retaining an inverse witness and field-relative existence. Extends the conventions to dimension zero. Does not substitute Schur triangularization for diagonalization.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/MatrixDecomposition"
    ],
    "specializationNote": "Instantiate W with an invertible V and scalar diagonal λ (optionally storing its uniquely determined inverse W); reconstruction is ρ(V,λ)=V diag(λ)V⁻¹.",
    "leanFormulation": "structure EigenDecomposition {F : Type u} [Field F] {n : Nat} (A : Catalog.Matrix F n n) where\n  vectors : Catalog.Matrix F n n\n  inverse : Catalog.Matrix F n n\n  eigenvalues : Fin n → F\n  inverse_left : inverse * vectors = 1\n  inverse_right : vectors * inverse = 1\n  reconstructs : A = vectors * _root_.Matrix.diagonal eigenvalues * inverse",
    "formulationSource": "urn:csabs:source/local-lean-MatrixDecompositions",
    "formulationLocator": "Catalog.EigenDecomposition",
    "formulationScope": "model",
    "leanModelMapping": "Field F, basis matrix vectors, an explicitly supplied two-sided inverse, scalar eigenvalues and exact similarity. No global diagonalizability or eigenvalue-existence axiom is introduced; a defective matrix has no such structure value.",
    "leanModelLimitations": "Exact selected witness/carrier model and factor observations. No factor-finding algorithm, decidable equality on real/complex entries, floating-point error analysis or general numerical implementation refinement. Only individually registered claims have compiled witnesses; existence/uniqueness results are not proved by structure fields."
  },
  {
    "id": "urn:csabs:operation/EigenDecomposition-factors",
    "type": "Operation",
    "name": "factors",
    "concept": "urn:csabs:concept/EigenDecomposition",
    "signature": "Eigen(A) → F^{n×n}×F^n×F^{n×n}",
    "description": "Observe the eigenvector basis, ordered eigenvalues and inverse.",
    "precondition": "A valid eigendecomposition witness exists over F.",
    "postcondition": "The exact tuple (V,λ,W).",
    "totality": "total on the stated typed domain; no decision algorithm or factor-finding procedure is promised"
  },
  {
    "id": "urn:csabs:operation/EigenDecomposition-reconstruct",
    "type": "Operation",
    "name": "reconstruct",
    "concept": "urn:csabs:concept/EigenDecomposition",
    "signature": "F^{n×n}×F^n×F^{n×n} → F^{n×n}; (V,λ,W) ↦ V diag(λ)W",
    "description": "Reconstruct from an explicitly supplied inverse factor.",
    "precondition": "Matching square dimensions; validity additionally requires WV=VW=I.",
    "postcondition": "A for a valid witness; the raw expression remains total without computing an inverse.",
    "totality": "total on the stated typed domain; no decision algorithm or factor-finding procedure is promised"
  },
  {
    "id": "urn:csabs:axiom/EigenDecomposition-factor-constraints",
    "type": "Axiom",
    "name": "factor-constraints",
    "statement": "The basis change is invertible and the middle factor is diagonal over the chosen field.",
    "formalStatement": "V,W∈F^{n×n}; WV=VW=I_n; λ∈F^n; Λ=diag(λ).",
    "assumptions": [
      "F is a field; n≥0; all eigenvalues and eigenvectors lie in F. A witness requires a full invertible V, not merely one eigenpair or n eigenvalues counted with multiplicity. Equality is exact and retains chosen V,λ; the inverse is uniquely determined by V. No orthogonality is required for a general eigenbasis, and no rounded eigensolver is modeled."
    ],
    "appliesTo": [
      "urn:csabs:concept/EigenDecomposition"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Mathematical definition; separate Lean evidence describes compiled interpretations.",
    "source": [
      "urn:csabs:source/ila-diagonalization"
    ],
    "sourceLocator": "Interactive Linear Algebra §5.4.1, definition, Diagonalization Theorem and proof, non-uniqueness and shear/rotation examples",
    "sourceNote": "Adapts the real diagonalization equations and their algebraic proof to an arbitrary chosen field, explicitly retaining an inverse witness and field-relative existence. Extends the conventions to dimension zero. Does not substitute Schur triangularization for diagonalization.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/EigenDecomposition-reconstruction",
    "type": "Axiom",
    "name": "reconstruction",
    "statement": "The input is similar to the diagonal factor.",
    "formalStatement": "A=VΛW.",
    "assumptions": [
      "F is a field; n≥0; all eigenvalues and eigenvectors lie in F. A witness requires a full invertible V, not merely one eigenpair or n eigenvalues counted with multiplicity. Equality is exact and retains chosen V,λ; the inverse is uniquely determined by V. No orthogonality is required for a general eigenbasis, and no rounded eigensolver is modeled."
    ],
    "appliesTo": [
      "urn:csabs:concept/EigenDecomposition"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Mathematical definition; separate Lean evidence describes compiled interpretations.",
    "source": [
      "urn:csabs:source/ila-diagonalization"
    ],
    "sourceLocator": "Interactive Linear Algebra §5.4.1, definition, Diagonalization Theorem and proof, non-uniqueness and shear/rotation examples",
    "sourceNote": "Adapts the real diagonalization equations and their algebraic proof to an arbitrary chosen field, explicitly retaining an inverse witness and field-relative existence. Extends the conventions to dimension zero. Does not substitute Schur triangularization for diagonalization.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/EigenDecomposition-basis-equation",
    "type": "Law",
    "name": "basis-equation",
    "statement": "The input acts diagonally in the selected eigenbasis.",
    "formalStatement": "AV=VΛ.",
    "assumptions": [
      "F is a field; n≥0; all eigenvalues and eigenvectors lie in F. A witness requires a full invertible V, not merely one eigenpair or n eigenvalues counted with multiplicity. Equality is exact and retains chosen V,λ; the inverse is uniquely determined by V. No orthogonality is required for a general eigenbasis, and no rounded eigensolver is modeled."
    ],
    "appliesTo": [
      "urn:csabs:concept/EigenDecomposition"
    ],
    "ruleRole": "derived-result",
    "dependsOn": [
      "urn:csabs:axiom/EigenDecomposition-factor-constraints",
      "urn:csabs:axiom/EigenDecomposition-reconstruction"
    ],
    "proofSketch": "Multiply A=VΛW on the right by V and use WV=I. The column equations are Av_i=λ_i v_i.",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial mathematical statement; only separately registered fresh Lean witnesses are compiler-verified.",
    "source": [
      "urn:csabs:source/ila-diagonalization"
    ],
    "sourceLocator": "Interactive Linear Algebra §5.4.1, definition, Diagonalization Theorem and proof, non-uniqueness and shear/rotation examples",
    "sourceNote": "Derives the selected result from the linked factor constraints/reconstruction, using exact matrix algebra. Adapts the real diagonalization equations and their algebraic proof to an arbitrary chosen field, explicitly retaining an inverse witness and field-relative existence. Extends the conventions to dimension zero. Does not substitute Schur triangularization for diagonalization.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {F : Type u} [Field F] {n : Nat} {A : Catalog.Matrix F n n} (d : Catalog.EigenDecomposition A), A * d.vectors = d.vectors * Matrix.diagonal d.eigenvalues",
    "formulationSource": "urn:csabs:source/local-lean-MatrixDecompositions",
    "formulationLocator": "Catalog.MatrixDecompositionProofs.eigen_basis_equation",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Field F, basis matrix vectors, an explicitly supplied two-sided inverse, scalar eigenvalues and exact similarity. No global diagonalizability or eigenvalue-existence axiom is introduced; a defective matrix has no such structure value.",
    "leanModelLimitations": "Proves the displayed algebraic identity for a supplied valid witness, under the mapped exact scalar/dimension conventions. It does not prove factor existence/uniqueness, a numerical algorithm, stability or implementation conformance.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/EigenDecomposition-factor-constraints\": \"The corresponding explicit structure fields supply this premise: V,W∈F^{n×n}; WV=VW=I_n; λ∈F^n; Λ=diag(λ). The proof uses the unitary or inverse identities; unused triangular/order/positivity fields remain profile constraints.\", \"urn:csabs:axiom/EigenDecomposition-reconstruction\": \"The corresponding explicit structure fields supply this premise: A=VΛW. The proof uses the unitary or inverse identities; unused triangular/order/positivity fields remain profile constraints.\"}"
  },
  {
    "id": "urn:csabs:theorem/EigenDecomposition-eigenbasis-criterion",
    "type": "Theorem",
    "name": "eigenbasis-criterion",
    "statement": "A square matrix is diagonalizable over F exactly when it has an F-basis of eigenvectors.",
    "formalStatement": "(∃V,W,λ, WV=VW=I_n ∧ A=V diag(λ)W) ⇔ (∃basis (v_i)_{i<n} of F^n, ∃λ∈F^n, ∀i,Av_i=λ_i v_i).",
    "assumptions": [
      "F is a field; n≥0; all eigenvalues and eigenvectors lie in F. A witness requires a full invertible V, not merely one eigenpair or n eigenvalues counted with multiplicity. Equality is exact and retains chosen V,λ; the inverse is uniquely determined by V. No orthogonality is required for a general eigenbasis, and no rounded eigensolver is modeled."
    ],
    "appliesTo": [
      "urn:csabs:concept/EigenDecomposition"
    ],
    "ruleRole": "derived-result",
    "dependsOn": [
      "urn:csabs:axiom/EigenDecomposition-factor-constraints",
      "urn:csabs:axiom/EigenDecomposition-reconstruction"
    ],
    "proofSketch": "From a witness use the columns of invertible V and AV=VΛ. Conversely form V from the supplied basis, take its inverse W, assemble AV=VΛ columnwise and multiply by W. The argument is algebraic and does not require F to be algebraically closed.",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial mathematical statement; only separately registered fresh Lean witnesses are compiler-verified.",
    "source": [
      "urn:csabs:source/ila-diagonalization"
    ],
    "sourceLocator": "Interactive Linear Algebra §5.4.1, definition, Diagonalization Theorem and proof, non-uniqueness and shear/rotation examples",
    "sourceNote": "Derives the selected result from the linked factor constraints/reconstruction, using exact matrix algebra. Adapts the real diagonalization equations and their algebraic proof to an arbitrary chosen field, explicitly retaining an inverse witness and field-relative existence. Extends the conventions to dimension zero. Does not substitute Schur triangularization for diagonalization.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
