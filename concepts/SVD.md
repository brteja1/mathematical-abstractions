# Full singular value decomposition (rectangular real or complex SVD)

An exact real/complex matrix factorization A=UΣVᴴ with full unitary factors and a rectangular diagonal matrix containing nonnegative, descending real singular values, including zero singular values.

**Notation:** A=UΣVᴴ; U∈F^{m×m}, V∈F^{n×n}; Σ∈F^{m×n}; σ₀≥⋯≥σ_{r−1}≥0, r=min(m,n).

**Stable ID:** `urn:csabs:concept/SVD`

**Categories:** Algebra → Linear and multilinear algebra → Matrix decompositions

**Kind:** Mathematical structure

**Prerequisites:** [Exact structured matrix decomposition witness](MatrixDecomposition.md), [Exact real number](RealNumber.md), [Exact complex number](ComplexNumber.md)

**Specializes:** [Exact structured matrix decomposition witness](MatrixDecomposition.md)

**Related concepts:** [Full QR decomposition (real or complex, rectangular)](QRDecomposition.md), [Eigendecomposition by a complete eigenbasis (diagonalization)](EigenDecomposition.md)

## Backlinks

- [Eigendecomposition by a complete eigenbasis (diagonalization)](EigenDecomposition.md) — `relatedConcept`
- [Full QR decomposition (real or complex, rectangular)](QRDecomposition.md) — `relatedConcept`

## Mathematical formulation

For F=ℝ or ℂ, r=min(m,n), U∈F^{m×m} and V∈F^{n×n} are unitary. Let σ:Fin(r)→ℝ be nonnegative and descending, and define Σ\_ij=σ\_i when i=j<r and 0 otherwise, embedding real values in F. A full SVD witness satisfies A=UΣVᴴ. Repeated/zero singular values allow nonunique vectors and phases; witness equality compares chosen factors. This is not a thin or truncated SVD.

**Lean formulation** (in its source module context):

```lean
structure SVD {F : Type u} [RCLike F] {m n : Nat} (A : Catalog.Matrix F m n) where
  left : Catalog.Matrix F m m
  right : Catalog.Matrix F n n
  singularValues : Fin (min m n) → ℝ
  nonnegative : ∀ i, 0 ≤ singularValues i
  descending : ∀ i j, i ≤ j → singularValues j ≤ singularValues i
  left_unitary_left : left.conjTranspose * left = 1
  left_unitary_right : left * left.conjTranspose = 1
  right_unitary_left : right.conjTranspose * right = 1
  right_unitary_right : right * right.conjTranspose = 1
  reconstructs : A = left * rectangularSingularDiagonal singularValues * right.conjTranspose
```

**Source:** [`Catalog.SVD`](../lean/Catalog/MatrixDecompositions.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** RCLike scalar F, full left and right unitary matrices, Fin(min m n)-indexed real singular values with nonnegativity/order proofs, rectangularSingularDiagonal and exact reconstruction. Adjoint is Matrix.conjTranspose, never plain transpose in the complex case.

**Limits:** Exact selected witness/carrier model and factor observations. No factor-finding algorithm, decidable equality on real/complex entries, floating-point error analysis or general numerical implementation refinement. Only individually registered claims have compiled witnesses; existence/uniqueness results are not proved by structure fields.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Selected exact factor-carrier constraints and reconstruction equation. F is ℝ or ℂ; m,n≥0 and r=min(m,n). Full square U,V are unitary on both sides; σ has r exact nonnegative descending real entries; Σ is the corresponding m×n rectangular diagonal. Zero dimensions, rank deficiency and repeated singular values are admitted. No rank threshold, approximation, tolerance or iterative algorithm is selected.

**basisKind:** defined-structure

**basisScope:** This selected factorization profile, not all numerical algorithms, alternative shapes or consequences.

**convention:** F is ℝ or ℂ; m,n≥0 and r=min(m,n). Full square U,V are unitary on both sides; σ has r exact nonnegative descending real entries; Σ is the corresponding m×n rectangular diagonal. Zero dimensions, rank deficiency and repeated singular values are admitted. No rank threshold, approximation, tolerance or iterative algorithm is selected.

**specializationNote:** Instantiate W with full unitary U,V and ordered nonnegative σ; define Σ from σ and ρ(U,σ,V)=UΣVᴴ.

**verificationObligation:** Map factor dimensions, scalar field, adjoint/permutation conventions, equality and input guards before reusing equations in software. Approximate factors need a separately justified residual/error contract.

**reviewStatus:** Sourced mathematical interface with a separate compiled Lean interpretation and individually mapped witnesses.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-SVD-factors"></a>

### factors

`urn:csabs:operation/SVD-factors`

**signature:** SVD(A) → F^{m×m}×ℝ^{min(m,n)}×F^{n×n}

**description:** Observe U, the ordered singular values and V.

**precondition:** Input is a valid full SVD witness.

**postcondition:** The exact ordered tuple (U,σ,V); the final factor is V, not Vᴴ.

**totality:** total on the stated typed domain; no decision algorithm or factor-finding procedure is promised

<a id="node-urn-csabs-operation-SVD-reconstruct"></a>

### reconstruct

`urn:csabs:operation/SVD-reconstruct`

**signature:** F^{m×m}×ℝ^{min(m,n)}×F^{n×n} → F^{m×n}; (U,σ,V) ↦ UΣ(σ)Vᴴ

**description:** Build the rectangular diagonal and reconstruct.

**precondition:** Matching finite dimensions; real σ embedded in F.

**postcondition:** A for a valid SVD witness.

**totality:** total on the stated typed domain; no decision algorithm or factor-finding procedure is promised

## Axioms and defining rules

<a id="node-urn-csabs-axiom-SVD-factor-constraints"></a>

### factor-constraints

`urn:csabs:axiom/SVD-factor-constraints`

**statement:** The full factors are unitary and the singular-value diagonal is real, ordered and nonnegative.

**formalStatement:** UᴴU=UUᴴ=I_m; VᴴV=VVᴴ=I_n; σ:Fin(min(m,n))→ℝ; ∀i,σ_i≥0; i≤j⇒σ_i≥σ_j; Σ_ij=if i=j<min(m,n) then σ_i else 0.

**assumptions:** F is ℝ or ℂ; m,n≥0 and r=min(m,n). Full square U,V are unitary on both sides; σ has r exact nonnegative descending real entries; Σ is the corresponding m×n rectangular diagonal. Zero dimensions, rank deficiency and repeated singular values are admitted. No rank threshold, approximation, tolerance or iterative algorithm is selected.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Mathematical definition; separate Lean evidence describes compiled interpretations.

**source:** [LAPACK Users’ Guide, Third Edition: Singular Value Decomposition](https://netlib.org/lapack/lug/node53.html); accessedOn: 2026-11-12; sourceRole: Consulted mathematical definition and factorization exposition; numerical algorithm/storage details are outside the selected exact model.

**sourceLocator:** LAPACK Users’ Guide §2.4.6, opening definition for real/complex SVD

**sourceNote:** Makes full factor dimensions and rectangular zero padding explicit, uses zero-based finite indices and includes the empty-dimensional case. Distinguishes r=min(m,n) from rank(A), so zero singular values are retained.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-SVD-reconstruction"></a>

### reconstruction

`urn:csabs:axiom/SVD-reconstruction`

**statement:** The SVD factors reconstruct the input with an adjoint on V.

**formalStatement:** A=UΣVᴴ.

**assumptions:** F is ℝ or ℂ; m,n≥0 and r=min(m,n). Full square U,V are unitary on both sides; σ has r exact nonnegative descending real entries; Σ is the corresponding m×n rectangular diagonal. Zero dimensions, rank deficiency and repeated singular values are admitted. No rank threshold, approximation, tolerance or iterative algorithm is selected.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Mathematical definition; separate Lean evidence describes compiled interpretations.

**source:** [LAPACK Users’ Guide, Third Edition: Singular Value Decomposition](https://netlib.org/lapack/lug/node53.html); accessedOn: 2026-11-12; sourceRole: Consulted mathematical definition and factorization exposition; numerical algorithm/storage details are outside the selected exact model.

**sourceLocator:** LAPACK Users’ Guide §2.4.6, opening definition for real/complex SVD

**sourceNote:** Makes full factor dimensions and rectangular zero padding explicit, uses zero-based finite indices and includes the empty-dimensional case. Distinguishes r=min(m,n) from rank(A), so zero singular values are retained.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-SVD-coordinates"></a>

### coordinates

`urn:csabs:law/SVD-coordinates`

**statement:** The singular-vector coordinate change yields the rectangular singular-value diagonal.

**formalStatement:** UᴴAV=Σ.

**assumptions:** F is ℝ or ℂ; m,n≥0 and r=min(m,n). Full square U,V are unitary on both sides; σ has r exact nonnegative descending real entries; Σ is the corresponding m×n rectangular diagonal. Zero dimensions, rank deficiency and repeated singular values are admitted. No rank threshold, approximation, tolerance or iterative algorithm is selected.

**ruleRole:** derived-result

**dependsOn:** [factor-constraints](SVD.md#node-urn-csabs-axiom-SVD-factor-constraints); [reconstruction](SVD.md#node-urn-csabs-axiom-SVD-reconstruction)

**proofSketch:** Substitute A=UΣVᴴ, reassociate, and cancel UᴴU=I and VᴴV=I. Ordering and nonnegativity are retained in the profile but not needed for this cancellation.

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial mathematical statement; only separately registered fresh Lean witnesses are compiler-verified.

**source:** [LAPACK Users’ Guide, Third Edition: Singular Value Decomposition](https://netlib.org/lapack/lug/node53.html); accessedOn: 2026-11-12; sourceRole: Consulted mathematical definition and factorization exposition; numerical algorithm/storage details are outside the selected exact model.

**sourceLocator:** LAPACK Users’ Guide §2.4.6, opening definition for real/complex SVD

**sourceNote:** Derives the selected result from the linked factor constraints/reconstruction, using exact matrix algebra. Makes full factor dimensions and rectangular zero padding explicit, uses zero-based finite indices and includes the empty-dimensional case. Distinguishes r=min(m,n) from rank(A), so zero singular values are retained.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {F : Type u} [RCLike F] {m n : Nat} {A : Catalog.Matrix F m n} (d : Catalog.SVD A), d.left.conjTranspose * A * d.right = Catalog.rectangularSingularDiagonal d.singularValues
```

**Source:** [`Catalog.MatrixDecompositionProofs.svd_coordinates`](../lean/Catalog/MatrixDecompositions.lean); consulted 2026-11-12.

**Scope:** registered-witness-type

**Interpretation:** RCLike scalar F, full left and right unitary matrices, Fin(min m n)-indexed real singular values with nonnegativity/order proofs, rectangularSingularDiagonal and exact reconstruction. Adjoint is Matrix.conjTranspose, never plain transpose in the complex case.

**Limits:** Proves the displayed algebraic identity for a supplied valid witness, under the mapped exact scalar/dimension conventions. It does not prove factor existence/uniqueness, a numerical algorithm, stability or implementation conformance.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/SVD-factor-constraints": "The corresponding explicit structure fields supply this premise: U*U=UU*=I_m; V*V=VV*=I_n; σ:Fin(min(m,n))→ℝ; ∀i,σ_i≥0; i≤j⇒σ_i≥σ_j; Σ_ij=if i=j<min(m,n) then σ_i else 0. The proof uses the unitary or inverse identities; unused triangular/order/positivity fields remain profile constraints.",
  "urn:csabs:axiom/SVD-reconstruction": "The corresponding explicit structure fields supply this premise: A=UΣV*. The proof uses the unitary or inverse identities; unused triangular/order/positivity fields remain profile constraints."
}
```

## Theorems

<a id="node-urn-csabs-theorem-SVD-existence"></a>

### existence

`urn:csabs:theorem/SVD-existence`

**statement:** Every real or complex rectangular matrix has a full SVD.

**formalStatement:** ∀A∈F^{m×n}, ∃U,σ,V satisfying the full SVD factor constraints and A=UΣVᴴ.

**assumptions:** F is ℝ or ℂ; m,n≥0 and r=min(m,n). Full square U,V are unitary on both sides; σ has r exact nonnegative descending real entries; Σ is the corresponding m×n rectangular diagonal. Zero dimensions, rank deficiency and repeated singular values are admitted. No rank threshold, approximation, tolerance or iterative algorithm is selected.

**ruleRole:** derived-result

**dependsOn:** [factor-constraints](SVD.md#node-urn-csabs-axiom-SVD-factor-constraints); [reconstruction](SVD.md#node-urn-csabs-axiom-SVD-reconstruction)

**proofSketch:** Diagonalize the Hermitian positive-semidefinite Gram matrix AᴴA, take nonnegative square roots of its eigenvalues, construct the corresponding nonzero left singular vectors and complete orthonormal bases on nullspaces. Sort σ and pad the rectangular diagonal with zeros; empty dimensions are vacuous. This proof sketch is not a registered existence witness.

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial mathematical statement; only separately registered fresh Lean witnesses are compiler-verified.

**source:** [LAPACK Users’ Guide, Third Edition: Singular Value Decomposition](https://netlib.org/lapack/lug/node53.html); accessedOn: 2026-11-12; sourceRole: Consulted mathematical definition and factorization exposition; numerical algorithm/storage details are outside the selected exact model.

**sourceLocator:** LAPACK Users’ Guide §2.4.6, opening definition for real/complex SVD

**sourceNote:** Derives the selected result from the linked factor constraints/reconstruction, using exact matrix algebra. Makes full factor dimensions and rectangular zero padding explicit, uses zero-based finite indices and includes the empty-dimensional case. Distinguishes r=min(m,n) from rank(A), so zero singular values are retained.

**provenanceKind:** derived

## Concept provenance

- [LAPACK Users’ Guide, Third Edition: Singular Value Decomposition](https://netlib.org/lapack/lug/node53.html); accessedOn: 2026-11-12; sourceRole: Consulted mathematical definition and factorization exposition; numerical algorithm/storage details are outside the selected exact model.

**sourceLocator:** LAPACK Users’ Guide §2.4.6, opening definition for real/complex SVD

**sourceNote:** Makes full factor dimensions and rectangular zero padding explicit, uses zero-based finite indices and includes the empty-dimensional case. Distinguishes r=min(m,n) from rank(A), so zero singular values are retained.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/SVD",
    "type": "Concept",
    "shortForm": "SVD",
    "fullName": "Full singular value decomposition (rectangular real or complex SVD)",
    "category": [
      "urn:csabs:category/matrix-decompositions"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "An exact real/complex matrix factorization A=UΣVᴴ with full unitary factors and a rectangular diagonal matrix containing nonnegative, descending real singular values, including zero singular values.",
    "notation": "A=UΣVᴴ; U∈F^{m×m}, V∈F^{n×n}; Σ∈F^{m×n}; σ₀≥⋯≥σ_{r−1}≥0, r=min(m,n).",
    "mathematicalFormulation": "For F=ℝ or ℂ, r=min(m,n), U∈F^{m×m} and V∈F^{n×n} are unitary. Let σ:Fin(r)→ℝ be nonnegative and descending, and define Σ_ij=σ_i when i=j<r and 0 otherwise, embedding real values in F. A full SVD witness satisfies A=UΣVᴴ. Repeated/zero singular values allow nonunique vectors and phases; witness equality compares chosen factors. This is not a thin or truncated SVD.",
    "hasOperation": [
      "urn:csabs:operation/SVD-factors",
      "urn:csabs:operation/SVD-reconstruct"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/SVD-factor-constraints",
      "urn:csabs:axiom/SVD-reconstruction"
    ],
    "hasLaw": [
      "urn:csabs:law/SVD-coordinates"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/SVD-existence"
    ],
    "requiresConcept": [
      "urn:csabs:concept/MatrixDecomposition",
      "urn:csabs:concept/RealNumber",
      "urn:csabs:concept/ComplexNumber"
    ],
    "relatedConcept": [
      "urn:csabs:concept/QRDecomposition",
      "urn:csabs:concept/EigenDecomposition"
    ],
    "axiomBasis": "Selected exact factor-carrier constraints and reconstruction equation. F is ℝ or ℂ; m,n≥0 and r=min(m,n). Full square U,V are unitary on both sides; σ has r exact nonnegative descending real entries; Σ is the corresponding m×n rectangular diagonal. Zero dimensions, rank deficiency and repeated singular values are admitted. No rank threshold, approximation, tolerance or iterative algorithm is selected.",
    "basisKind": "defined-structure",
    "basisScope": "This selected factorization profile, not all numerical algorithms, alternative shapes or consequences.",
    "convention": "F is ℝ or ℂ; m,n≥0 and r=min(m,n). Full square U,V are unitary on both sides; σ has r exact nonnegative descending real entries; Σ is the corresponding m×n rectangular diagonal. Zero dimensions, rank deficiency and repeated singular values are admitted. No rank threshold, approximation, tolerance or iterative algorithm is selected.",
    "verificationObligation": "Map factor dimensions, scalar field, adjoint/permutation conventions, equality and input guards before reusing equations in software. Approximate factors need a separately justified residual/error contract.",
    "reviewStatus": "Sourced mathematical interface with a separate compiled Lean interpretation and individually mapped witnesses.",
    "coverageStatus": "basis-reviewed",
    "source": [
      "urn:csabs:source/lapack-lug-svd"
    ],
    "sourceLocator": "LAPACK Users’ Guide §2.4.6, opening definition for real/complex SVD",
    "sourceNote": "Makes full factor dimensions and rectangular zero padding explicit, uses zero-based finite indices and includes the empty-dimensional case. Distinguishes r=min(m,n) from rank(A), so zero singular values are retained.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/MatrixDecomposition"
    ],
    "specializationNote": "Instantiate W with full unitary U,V and ordered nonnegative σ; define Σ from σ and ρ(U,σ,V)=UΣVᴴ.",
    "leanFormulation": "structure SVD {F : Type u} [RCLike F] {m n : Nat} (A : Catalog.Matrix F m n) where\n  left : Catalog.Matrix F m m\n  right : Catalog.Matrix F n n\n  singularValues : Fin (min m n) → ℝ\n  nonnegative : ∀ i, 0 ≤ singularValues i\n  descending : ∀ i j, i ≤ j → singularValues j ≤ singularValues i\n  left_unitary_left : left.conjTranspose * left = 1\n  left_unitary_right : left * left.conjTranspose = 1\n  right_unitary_left : right.conjTranspose * right = 1\n  right_unitary_right : right * right.conjTranspose = 1\n  reconstructs : A = left * rectangularSingularDiagonal singularValues * right.conjTranspose",
    "formulationSource": "urn:csabs:source/local-lean-MatrixDecompositions",
    "formulationLocator": "Catalog.SVD",
    "formulationScope": "model",
    "leanModelMapping": "RCLike scalar F, full left and right unitary matrices, Fin(min m n)-indexed real singular values with nonnegativity/order proofs, rectangularSingularDiagonal and exact reconstruction. Adjoint is Matrix.conjTranspose, never plain transpose in the complex case.",
    "leanModelLimitations": "Exact selected witness/carrier model and factor observations. No factor-finding algorithm, decidable equality on real/complex entries, floating-point error analysis or general numerical implementation refinement. Only individually registered claims have compiled witnesses; existence/uniqueness results are not proved by structure fields."
  },
  {
    "id": "urn:csabs:operation/SVD-factors",
    "type": "Operation",
    "name": "factors",
    "concept": "urn:csabs:concept/SVD",
    "signature": "SVD(A) → F^{m×m}×ℝ^{min(m,n)}×F^{n×n}",
    "description": "Observe U, the ordered singular values and V.",
    "precondition": "Input is a valid full SVD witness.",
    "postcondition": "The exact ordered tuple (U,σ,V); the final factor is V, not Vᴴ.",
    "totality": "total on the stated typed domain; no decision algorithm or factor-finding procedure is promised"
  },
  {
    "id": "urn:csabs:operation/SVD-reconstruct",
    "type": "Operation",
    "name": "reconstruct",
    "concept": "urn:csabs:concept/SVD",
    "signature": "F^{m×m}×ℝ^{min(m,n)}×F^{n×n} → F^{m×n}; (U,σ,V) ↦ UΣ(σ)Vᴴ",
    "description": "Build the rectangular diagonal and reconstruct.",
    "precondition": "Matching finite dimensions; real σ embedded in F.",
    "postcondition": "A for a valid SVD witness.",
    "totality": "total on the stated typed domain; no decision algorithm or factor-finding procedure is promised"
  },
  {
    "id": "urn:csabs:axiom/SVD-factor-constraints",
    "type": "Axiom",
    "name": "factor-constraints",
    "statement": "The full factors are unitary and the singular-value diagonal is real, ordered and nonnegative.",
    "formalStatement": "UᴴU=UUᴴ=I_m; VᴴV=VVᴴ=I_n; σ:Fin(min(m,n))→ℝ; ∀i,σ_i≥0; i≤j⇒σ_i≥σ_j; Σ_ij=if i=j<min(m,n) then σ_i else 0.",
    "assumptions": [
      "F is ℝ or ℂ; m,n≥0 and r=min(m,n). Full square U,V are unitary on both sides; σ has r exact nonnegative descending real entries; Σ is the corresponding m×n rectangular diagonal. Zero dimensions, rank deficiency and repeated singular values are admitted. No rank threshold, approximation, tolerance or iterative algorithm is selected."
    ],
    "appliesTo": [
      "urn:csabs:concept/SVD"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Mathematical definition; separate Lean evidence describes compiled interpretations.",
    "source": [
      "urn:csabs:source/lapack-lug-svd"
    ],
    "sourceLocator": "LAPACK Users’ Guide §2.4.6, opening definition for real/complex SVD",
    "sourceNote": "Makes full factor dimensions and rectangular zero padding explicit, uses zero-based finite indices and includes the empty-dimensional case. Distinguishes r=min(m,n) from rank(A), so zero singular values are retained.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/SVD-reconstruction",
    "type": "Axiom",
    "name": "reconstruction",
    "statement": "The SVD factors reconstruct the input with an adjoint on V.",
    "formalStatement": "A=UΣVᴴ.",
    "assumptions": [
      "F is ℝ or ℂ; m,n≥0 and r=min(m,n). Full square U,V are unitary on both sides; σ has r exact nonnegative descending real entries; Σ is the corresponding m×n rectangular diagonal. Zero dimensions, rank deficiency and repeated singular values are admitted. No rank threshold, approximation, tolerance or iterative algorithm is selected."
    ],
    "appliesTo": [
      "urn:csabs:concept/SVD"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Mathematical definition; separate Lean evidence describes compiled interpretations.",
    "source": [
      "urn:csabs:source/lapack-lug-svd"
    ],
    "sourceLocator": "LAPACK Users’ Guide §2.4.6, opening definition for real/complex SVD",
    "sourceNote": "Makes full factor dimensions and rectangular zero padding explicit, uses zero-based finite indices and includes the empty-dimensional case. Distinguishes r=min(m,n) from rank(A), so zero singular values are retained.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/SVD-coordinates",
    "type": "Law",
    "name": "coordinates",
    "statement": "The singular-vector coordinate change yields the rectangular singular-value diagonal.",
    "formalStatement": "UᴴAV=Σ.",
    "assumptions": [
      "F is ℝ or ℂ; m,n≥0 and r=min(m,n). Full square U,V are unitary on both sides; σ has r exact nonnegative descending real entries; Σ is the corresponding m×n rectangular diagonal. Zero dimensions, rank deficiency and repeated singular values are admitted. No rank threshold, approximation, tolerance or iterative algorithm is selected."
    ],
    "appliesTo": [
      "urn:csabs:concept/SVD"
    ],
    "ruleRole": "derived-result",
    "dependsOn": [
      "urn:csabs:axiom/SVD-factor-constraints",
      "urn:csabs:axiom/SVD-reconstruction"
    ],
    "proofSketch": "Substitute A=UΣVᴴ, reassociate, and cancel UᴴU=I and VᴴV=I. Ordering and nonnegativity are retained in the profile but not needed for this cancellation.",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial mathematical statement; only separately registered fresh Lean witnesses are compiler-verified.",
    "source": [
      "urn:csabs:source/lapack-lug-svd"
    ],
    "sourceLocator": "LAPACK Users’ Guide §2.4.6, opening definition for real/complex SVD",
    "sourceNote": "Derives the selected result from the linked factor constraints/reconstruction, using exact matrix algebra. Makes full factor dimensions and rectangular zero padding explicit, uses zero-based finite indices and includes the empty-dimensional case. Distinguishes r=min(m,n) from rank(A), so zero singular values are retained.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {F : Type u} [RCLike F] {m n : Nat} {A : Catalog.Matrix F m n} (d : Catalog.SVD A), d.left.conjTranspose * A * d.right = Catalog.rectangularSingularDiagonal d.singularValues",
    "formulationSource": "urn:csabs:source/local-lean-MatrixDecompositions",
    "formulationLocator": "Catalog.MatrixDecompositionProofs.svd_coordinates",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "RCLike scalar F, full left and right unitary matrices, Fin(min m n)-indexed real singular values with nonnegativity/order proofs, rectangularSingularDiagonal and exact reconstruction. Adjoint is Matrix.conjTranspose, never plain transpose in the complex case.",
    "leanModelLimitations": "Proves the displayed algebraic identity for a supplied valid witness, under the mapped exact scalar/dimension conventions. It does not prove factor existence/uniqueness, a numerical algorithm, stability or implementation conformance.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/SVD-factor-constraints\": \"The corresponding explicit structure fields supply this premise: U*U=UU*=I_m; V*V=VV*=I_n; σ:Fin(min(m,n))→ℝ; ∀i,σ_i≥0; i≤j⇒σ_i≥σ_j; Σ_ij=if i=j<min(m,n) then σ_i else 0. The proof uses the unitary or inverse identities; unused triangular/order/positivity fields remain profile constraints.\", \"urn:csabs:axiom/SVD-reconstruction\": \"The corresponding explicit structure fields supply this premise: A=UΣV*. The proof uses the unitary or inverse identities; unused triangular/order/positivity fields remain profile constraints.\"}"
  },
  {
    "id": "urn:csabs:theorem/SVD-existence",
    "type": "Theorem",
    "name": "existence",
    "statement": "Every real or complex rectangular matrix has a full SVD.",
    "formalStatement": "∀A∈F^{m×n}, ∃U,σ,V satisfying the full SVD factor constraints and A=UΣVᴴ.",
    "assumptions": [
      "F is ℝ or ℂ; m,n≥0 and r=min(m,n). Full square U,V are unitary on both sides; σ has r exact nonnegative descending real entries; Σ is the corresponding m×n rectangular diagonal. Zero dimensions, rank deficiency and repeated singular values are admitted. No rank threshold, approximation, tolerance or iterative algorithm is selected."
    ],
    "appliesTo": [
      "urn:csabs:concept/SVD"
    ],
    "ruleRole": "derived-result",
    "dependsOn": [
      "urn:csabs:axiom/SVD-factor-constraints",
      "urn:csabs:axiom/SVD-reconstruction"
    ],
    "proofSketch": "Diagonalize the Hermitian positive-semidefinite Gram matrix AᴴA, take nonnegative square roots of its eigenvalues, construct the corresponding nonzero left singular vectors and complete orthonormal bases on nullspaces. Sort σ and pad the rectangular diagonal with zeros; empty dimensions are vacuous. This proof sketch is not a registered existence witness.",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial mathematical statement; only separately registered fresh Lean witnesses are compiler-verified.",
    "source": [
      "urn:csabs:source/lapack-lug-svd"
    ],
    "sourceLocator": "LAPACK Users’ Guide §2.4.6, opening definition for real/complex SVD",
    "sourceNote": "Derives the selected result from the linked factor constraints/reconstruction, using exact matrix algebra. Makes full factor dimensions and rectangular zero padding explicit, uses zero-based finite indices and includes the empty-dimensional case. Distinguishes r=min(m,n) from rank(A), so zero singular values are retained.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
