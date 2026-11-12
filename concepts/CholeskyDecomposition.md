# Cholesky decomposition (Hermitian positive definite, lower profile)

An exact factorization A=LLᴴ of a real symmetric or complex Hermitian positive-definite matrix, with lower-triangular L and strictly positive real diagonal. Semidefinite and indefinite variants are outside this profile.

**Notation:** A=LLᴴ; Aᴴ=A; xᴴAx>0 for x≠0; L_ij=0 for i<j; L_ii∈ℝ_{>0}.

**Stable ID:** `urn:csabs:concept/CholeskyDecomposition`

**Categories:** Algebra → Linear and multilinear algebra → Matrix decompositions

**Kind:** Mathematical structure

**Prerequisites:** [Exact structured matrix decomposition witness](MatrixDecomposition.md), [Exact real number](RealNumber.md), [Exact complex number](ComplexNumber.md)

**Specializes:** [Exact structured matrix decomposition witness](MatrixDecomposition.md)

## Mathematical formulation

For F=ℝ or ℂ and A∈F^{n×n}, require Aᴴ=A and Re(xᴴAx)>0 for every nonzero x∈F^n. A lower Cholesky witness is L∈F^{n×n} with L\_ij=0 for i<j, each L\_ii a strictly positive real embedded in F, and A=LLᴴ. The diagonal normalization fixes the factor uniquely. This is a triangular factorization, not the Hermitian principal square root A^{1/2}; positive-semidefinite, pivoted and LDLᴴ variants require separate contracts.

**Lean formulation** (in its source module context):

```lean
structure CholeskyDecomposition {F : Type u} [RCLike F] {n : Nat}
    (A : Catalog.Matrix F n n) where
  lower : Catalog.Matrix F n n
  positive_definite : matrixHermitianPositiveDefinite A
  lower_triangular : matrixLower lower
  positive_real_diagonal : ∀ i, ∃ r : ℝ, 0 < r ∧ lower i i = (r : F)
  reconstructs : A = lower * lower.conjTranspose
```

**Source:** [`Catalog.CholeskyDecomposition`](../lean/Catalog/MatrixDecompositions.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** RCLike F, explicit exact Hermitian/quadratic-form positive-definiteness guard, a lower-triangular factor with each diagonal entry equal to a positive real, and exact A=L*L.conjTranspose. Positivity is supplied as a structure hypothesis, not a theorem fabricated by the model.

**Limits:** Exact selected witness/carrier model and factor observations. No factor-finding algorithm, decidable equality on real/complex entries, floating-point error analysis or general numerical implementation refinement. Only individually registered claims have compiled witnesses; existence/uniqueness results are not proved by structure fields.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Selected exact factor-carrier constraints and reconstruction equation. F is ℝ or ℂ and n≥0. A is Hermitian positive definite, tested by its exact quadratic form; complex diagonal entries of L are positive reals, not merely numbers with positive real part. Witness equality is entrywise equality of L. For n=0, positivity/triangular conditions are vacuous, the empty factor is unique and det(A)=1. Numerical failure tolerances and roundoff are outside this exact profile.

**basisKind:** defined-structure

**basisScope:** This selected factorization profile, not all numerical algorithms, alternative shapes or consequences.

**convention:** F is ℝ or ℂ and n≥0. A is Hermitian positive definite, tested by its exact quadratic form; complex diagonal entries of L are positive reals, not merely numbers with positive real part. Witness equality is entrywise equality of L. For n=0, positivity/triangular conditions are vacuous, the empty factor is unique and det(A)=1. Numerical failure tolerances and roundoff are outside this exact profile.

**specializationNote:** Instantiate W with lower-triangular L having positive real diagonal and ρ(L)=LLᴴ. The input guard is Hermitian positive definiteness; it is not inherited from the generic reconstruction relation.

**verificationObligation:** Map factor dimensions, scalar field, adjoint/permutation conventions, equality and input guards before reusing equations in software. Approximate factors need a separately justified residual/error contract.

**reviewStatus:** Sourced mathematical interface with a separate compiled Lean interpretation and individually mapped witnesses.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-CholeskyDecomposition-factor"></a>

### factor

`urn:csabs:operation/CholeskyDecomposition-factor`

**signature:** Cholesky(A) → F^{n×n}

**description:** Observe the normalized lower Cholesky factor.

**precondition:** A valid witness for a Hermitian positive-definite A.

**postcondition:** L, with lower-triangular structure and positive real diagonal.

**totality:** total on the stated typed domain; no decision algorithm or factor-finding procedure is promised

<a id="node-urn-csabs-operation-CholeskyDecomposition-reconstruct"></a>

### reconstruct

`urn:csabs:operation/CholeskyDecomposition-reconstruct`

**signature:** F^{n×n} → F^{n×n}; L ↦ LLᴴ

**description:** Multiply a matrix by its adjoint.

**precondition:** Finite square dimensions; no inverse or square root is evaluated.

**postcondition:** A for a valid Cholesky witness.

**totality:** total on the stated typed domain; no decision algorithm or factor-finding procedure is promised

## Axioms and defining rules

<a id="node-urn-csabs-axiom-CholeskyDecomposition-factor-constraints"></a>

### factor-constraints

`urn:csabs:axiom/CholeskyDecomposition-factor-constraints`

**statement:** The input is Hermitian positive definite and the lower factor has positive real diagonal.

**formalStatement:** Aᴴ=A; ∀x≠0,Re(xᴴAx)>0; ∀i<j,L_ij=0; ∀i,∃r_i∈ℝ_{>0},L_ii=r_i.

**assumptions:** F is ℝ or ℂ and n≥0. A is Hermitian positive definite, tested by its exact quadratic form; complex diagonal entries of L are positive reals, not merely numbers with positive real part. Witness equality is entrywise equality of L. For n=0, positivity/triangular conditions are vacuous, the empty factor is unique and det(A)=1. Numerical failure tolerances and roundoff are outside this exact profile.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Mathematical definition; separate Lean evidence describes compiled interpretations.

**source:** [Nicholas J. Higham: What Is a Cholesky Factorization? (2020-08-11)](https://nhigham.com/2020/08/11/what-is-a-cholesky-factorization/); accessedOn: 2026-11-12; sourceRole: Consulted mathematical definition and factorization exposition; numerical algorithm/storage details are outside the selected exact model.; [LAPACK Users’ Guide, Third Edition: Linear Equations](https://netlib.org/lapack/lug/node38.html); accessedOn: 2026-11-12; sourceRole: Consulted mathematical definition and factorization exposition; numerical algorithm/storage details are outside the selected exact model.

**sourceLocator:** Higham, opening definition and existence/uniqueness induction, determinant identity; LAPACK Users’ Guide §2.4.1, Hermitian Cholesky A=LL^H

**sourceNote:** Chooses lower L rather than Higham’s upper R, and extends the real transpose identities to conjugate transpose using the consulted LAPACK Hermitian profile. Adds explicit positive-real diagonal normalization, exact quadratic-form domain and empty-dimension convention. Does not import numerical stability bounds into the exact interface.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-CholeskyDecomposition-reconstruction"></a>

### reconstruction

`urn:csabs:axiom/CholeskyDecomposition-reconstruction`

**statement:** The lower factor and its adjoint reconstruct the input.

**formalStatement:** A=LLᴴ.

**assumptions:** F is ℝ or ℂ and n≥0. A is Hermitian positive definite, tested by its exact quadratic form; complex diagonal entries of L are positive reals, not merely numbers with positive real part. Witness equality is entrywise equality of L. For n=0, positivity/triangular conditions are vacuous, the empty factor is unique and det(A)=1. Numerical failure tolerances and roundoff are outside this exact profile.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Mathematical definition; separate Lean evidence describes compiled interpretations.

**source:** [Nicholas J. Higham: What Is a Cholesky Factorization? (2020-08-11)](https://nhigham.com/2020/08/11/what-is-a-cholesky-factorization/); accessedOn: 2026-11-12; sourceRole: Consulted mathematical definition and factorization exposition; numerical algorithm/storage details are outside the selected exact model.; [LAPACK Users’ Guide, Third Edition: Linear Equations](https://netlib.org/lapack/lug/node38.html); accessedOn: 2026-11-12; sourceRole: Consulted mathematical definition and factorization exposition; numerical algorithm/storage details are outside the selected exact model.

**sourceLocator:** Higham, opening definition and existence/uniqueness induction, determinant identity; LAPACK Users’ Guide §2.4.1, Hermitian Cholesky A=LL^H

**sourceNote:** Chooses lower L rather than Higham’s upper R, and extends the real transpose identities to conjugate transpose using the consulted LAPACK Hermitian profile. Adds explicit positive-real diagonal normalization, exact quadratic-form domain and empty-dimension convention. Does not import numerical stability bounds into the exact interface.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-CholeskyDecomposition-determinant"></a>

### determinant

`urn:csabs:law/CholeskyDecomposition-determinant`

**statement:** The determinant factors as a scalar times its conjugate.

**formalStatement:** det(A)=det(L)·conj(det(L)); over ℝ, det(A)=det(L)^2.

**assumptions:** F is ℝ or ℂ and n≥0. A is Hermitian positive definite, tested by its exact quadratic form; complex diagonal entries of L are positive reals, not merely numbers with positive real part. Witness equality is entrywise equality of L. For n=0, positivity/triangular conditions are vacuous, the empty factor is unique and det(A)=1. Numerical failure tolerances and roundoff are outside this exact profile.

**ruleRole:** derived-result

**dependsOn:** [reconstruction](CholeskyDecomposition.md#node-urn-csabs-axiom-CholeskyDecomposition-reconstruction)

**proofSketch:** Apply determinant multiplicativity to A=LLᴴ and use det(Lᴴ)=conj(det(L)). The real case has trivial conjugation. The compiled witness states the conjugate-product identity, whose real specialization is the displayed square.

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial mathematical statement; only separately registered fresh Lean witnesses are compiler-verified.

**source:** [Nicholas J. Higham: What Is a Cholesky Factorization? (2020-08-11)](https://nhigham.com/2020/08/11/what-is-a-cholesky-factorization/); accessedOn: 2026-11-12; sourceRole: Consulted mathematical definition and factorization exposition; numerical algorithm/storage details are outside the selected exact model.; [LAPACK Users’ Guide, Third Edition: Linear Equations](https://netlib.org/lapack/lug/node38.html); accessedOn: 2026-11-12; sourceRole: Consulted mathematical definition and factorization exposition; numerical algorithm/storage details are outside the selected exact model.

**sourceLocator:** Higham, opening definition and existence/uniqueness induction, determinant identity; LAPACK Users’ Guide §2.4.1, Hermitian Cholesky A=LL^H

**sourceNote:** Derives the selected result from the linked factor constraints/reconstruction, using exact matrix algebra. Chooses lower L rather than Higham’s upper R, and extends the real transpose identities to conjugate transpose using the consulted LAPACK Hermitian profile. Adds explicit positive-real diagonal normalization, exact quadratic-form domain and empty-dimension convention. Does not import numerical stability bounds into the exact interface.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {F : Type u} [RCLike F] {n : Nat} {A : Catalog.Matrix F n n} (d : Catalog.CholeskyDecomposition A), A.det = d.lower.det * star d.lower.det
```

**Source:** [`Catalog.MatrixDecompositionProofs.cholesky_determinant`](../lean/Catalog/MatrixDecompositions.lean); consulted 2026-11-12.

**Scope:** registered-witness-type

**Interpretation:** RCLike F, explicit exact Hermitian/quadratic-form positive-definiteness guard, a lower-triangular factor with each diagonal entry equal to a positive real, and exact A=L*L.conjTranspose. Positivity is supplied as a structure hypothesis, not a theorem fabricated by the model.

**Limits:** Proves the displayed algebraic identity for a supplied valid witness, under the mapped exact scalar/dimension conventions. It does not prove factor existence/uniqueness, a numerical algorithm, stability or implementation conformance.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/CholeskyDecomposition-reconstruction": "The corresponding explicit structure fields supply this premise: A=LL*."
}
```

## Theorems

<a id="node-urn-csabs-theorem-CholeskyDecomposition-existence-uniqueness"></a>

### existence-uniqueness

`urn:csabs:theorem/CholeskyDecomposition-existence-uniqueness`

**statement:** Every Hermitian positive-definite matrix has exactly one lower Cholesky factor with positive real diagonal.

**formalStatement:** Aᴴ=A ∧ (∀x≠0,Re(xᴴAx)>0) ⇒ ∃!L, lower(L) ∧ (∀i,L_ii∈ℝ_{>0}) ∧ A=LLᴴ.

**assumptions:** F is ℝ or ℂ and n≥0. A is Hermitian positive definite, tested by its exact quadratic form; complex diagonal entries of L are positive reals, not merely numbers with positive real part. Witness equality is entrywise equality of L. For n=0, positivity/triangular conditions are vacuous, the empty factor is unique and det(A)=1. Numerical failure tolerances and roundoff are outside this exact profile.

**ruleRole:** derived-result

**dependsOn:** [factor-constraints](CholeskyDecomposition.md#node-urn-csabs-axiom-CholeskyDecomposition-factor-constraints); [reconstruction](CholeskyDecomposition.md#node-urn-csabs-axiom-CholeskyDecomposition-reconstruction)

**proofSketch:** Induct on dimension using the leading positive-definite principal block. Solve for the off-diagonal block with its already invertible triangular factor and take the unique positive square root of the positive Schur complement. The same recurrence forces uniqueness; dimension zero is the empty base case. In the complex case replace transpose by adjoint.

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial mathematical statement; only separately registered fresh Lean witnesses are compiler-verified.

**source:** [Nicholas J. Higham: What Is a Cholesky Factorization? (2020-08-11)](https://nhigham.com/2020/08/11/what-is-a-cholesky-factorization/); accessedOn: 2026-11-12; sourceRole: Consulted mathematical definition and factorization exposition; numerical algorithm/storage details are outside the selected exact model.; [LAPACK Users’ Guide, Third Edition: Linear Equations](https://netlib.org/lapack/lug/node38.html); accessedOn: 2026-11-12; sourceRole: Consulted mathematical definition and factorization exposition; numerical algorithm/storage details are outside the selected exact model.

**sourceLocator:** Higham, opening definition and existence/uniqueness induction, determinant identity; LAPACK Users’ Guide §2.4.1, Hermitian Cholesky A=LL^H

**sourceNote:** Derives the selected result from the linked factor constraints/reconstruction, using exact matrix algebra. Chooses lower L rather than Higham’s upper R, and extends the real transpose identities to conjugate transpose using the consulted LAPACK Hermitian profile. Adds explicit positive-real diagonal normalization, exact quadratic-form domain and empty-dimension convention. Does not import numerical stability bounds into the exact interface.

**provenanceKind:** derived

## Concept provenance

- [Nicholas J. Higham: What Is a Cholesky Factorization? (2020-08-11)](https://nhigham.com/2020/08/11/what-is-a-cholesky-factorization/); accessedOn: 2026-11-12; sourceRole: Consulted mathematical definition and factorization exposition; numerical algorithm/storage details are outside the selected exact model.
- [LAPACK Users’ Guide, Third Edition: Linear Equations](https://netlib.org/lapack/lug/node38.html); accessedOn: 2026-11-12; sourceRole: Consulted mathematical definition and factorization exposition; numerical algorithm/storage details are outside the selected exact model.

**sourceLocator:** Higham, opening definition and existence/uniqueness induction, determinant identity; LAPACK Users’ Guide §2.4.1, Hermitian Cholesky A=LL^H

**sourceNote:** Chooses lower L rather than Higham’s upper R, and extends the real transpose identities to conjugate transpose using the consulted LAPACK Hermitian profile. Adds explicit positive-real diagonal normalization, exact quadratic-form domain and empty-dimension convention. Does not import numerical stability bounds into the exact interface.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/CholeskyDecomposition",
    "type": "Concept",
    "shortForm": "CholeskyDecomposition",
    "fullName": "Cholesky decomposition (Hermitian positive definite, lower profile)",
    "category": [
      "urn:csabs:category/matrix-decompositions"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "An exact factorization A=LLᴴ of a real symmetric or complex Hermitian positive-definite matrix, with lower-triangular L and strictly positive real diagonal. Semidefinite and indefinite variants are outside this profile.",
    "notation": "A=LLᴴ; Aᴴ=A; xᴴAx>0 for x≠0; L_ij=0 for i<j; L_ii∈ℝ_{>0}.",
    "mathematicalFormulation": "For F=ℝ or ℂ and A∈F^{n×n}, require Aᴴ=A and Re(xᴴAx)>0 for every nonzero x∈F^n. A lower Cholesky witness is L∈F^{n×n} with L_ij=0 for i<j, each L_ii a strictly positive real embedded in F, and A=LLᴴ. The diagonal normalization fixes the factor uniquely. This is a triangular factorization, not the Hermitian principal square root A^{1/2}; positive-semidefinite, pivoted and LDLᴴ variants require separate contracts.",
    "hasOperation": [
      "urn:csabs:operation/CholeskyDecomposition-factor",
      "urn:csabs:operation/CholeskyDecomposition-reconstruct"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/CholeskyDecomposition-factor-constraints",
      "urn:csabs:axiom/CholeskyDecomposition-reconstruction"
    ],
    "hasLaw": [
      "urn:csabs:law/CholeskyDecomposition-determinant"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/CholeskyDecomposition-existence-uniqueness"
    ],
    "requiresConcept": [
      "urn:csabs:concept/MatrixDecomposition",
      "urn:csabs:concept/RealNumber",
      "urn:csabs:concept/ComplexNumber"
    ],
    "relatedConcept": [],
    "axiomBasis": "Selected exact factor-carrier constraints and reconstruction equation. F is ℝ or ℂ and n≥0. A is Hermitian positive definite, tested by its exact quadratic form; complex diagonal entries of L are positive reals, not merely numbers with positive real part. Witness equality is entrywise equality of L. For n=0, positivity/triangular conditions are vacuous, the empty factor is unique and det(A)=1. Numerical failure tolerances and roundoff are outside this exact profile.",
    "basisKind": "defined-structure",
    "basisScope": "This selected factorization profile, not all numerical algorithms, alternative shapes or consequences.",
    "convention": "F is ℝ or ℂ and n≥0. A is Hermitian positive definite, tested by its exact quadratic form; complex diagonal entries of L are positive reals, not merely numbers with positive real part. Witness equality is entrywise equality of L. For n=0, positivity/triangular conditions are vacuous, the empty factor is unique and det(A)=1. Numerical failure tolerances and roundoff are outside this exact profile.",
    "verificationObligation": "Map factor dimensions, scalar field, adjoint/permutation conventions, equality and input guards before reusing equations in software. Approximate factors need a separately justified residual/error contract.",
    "reviewStatus": "Sourced mathematical interface with a separate compiled Lean interpretation and individually mapped witnesses.",
    "coverageStatus": "basis-reviewed",
    "source": [
      "urn:csabs:source/higham-cholesky",
      "urn:csabs:source/lapack-lug-linear-equations"
    ],
    "sourceLocator": "Higham, opening definition and existence/uniqueness induction, determinant identity; LAPACK Users’ Guide §2.4.1, Hermitian Cholesky A=LL^H",
    "sourceNote": "Chooses lower L rather than Higham’s upper R, and extends the real transpose identities to conjugate transpose using the consulted LAPACK Hermitian profile. Adds explicit positive-real diagonal normalization, exact quadratic-form domain and empty-dimension convention. Does not import numerical stability bounds into the exact interface.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/MatrixDecomposition"
    ],
    "specializationNote": "Instantiate W with lower-triangular L having positive real diagonal and ρ(L)=LLᴴ. The input guard is Hermitian positive definiteness; it is not inherited from the generic reconstruction relation.",
    "leanFormulation": "structure CholeskyDecomposition {F : Type u} [RCLike F] {n : Nat}\n    (A : Catalog.Matrix F n n) where\n  lower : Catalog.Matrix F n n\n  positive_definite : matrixHermitianPositiveDefinite A\n  lower_triangular : matrixLower lower\n  positive_real_diagonal : ∀ i, ∃ r : ℝ, 0 < r ∧ lower i i = (r : F)\n  reconstructs : A = lower * lower.conjTranspose",
    "formulationSource": "urn:csabs:source/local-lean-MatrixDecompositions",
    "formulationLocator": "Catalog.CholeskyDecomposition",
    "formulationScope": "model",
    "leanModelMapping": "RCLike F, explicit exact Hermitian/quadratic-form positive-definiteness guard, a lower-triangular factor with each diagonal entry equal to a positive real, and exact A=L*L.conjTranspose. Positivity is supplied as a structure hypothesis, not a theorem fabricated by the model.",
    "leanModelLimitations": "Exact selected witness/carrier model and factor observations. No factor-finding algorithm, decidable equality on real/complex entries, floating-point error analysis or general numerical implementation refinement. Only individually registered claims have compiled witnesses; existence/uniqueness results are not proved by structure fields."
  },
  {
    "id": "urn:csabs:operation/CholeskyDecomposition-factor",
    "type": "Operation",
    "name": "factor",
    "concept": "urn:csabs:concept/CholeskyDecomposition",
    "signature": "Cholesky(A) → F^{n×n}",
    "description": "Observe the normalized lower Cholesky factor.",
    "precondition": "A valid witness for a Hermitian positive-definite A.",
    "postcondition": "L, with lower-triangular structure and positive real diagonal.",
    "totality": "total on the stated typed domain; no decision algorithm or factor-finding procedure is promised"
  },
  {
    "id": "urn:csabs:operation/CholeskyDecomposition-reconstruct",
    "type": "Operation",
    "name": "reconstruct",
    "concept": "urn:csabs:concept/CholeskyDecomposition",
    "signature": "F^{n×n} → F^{n×n}; L ↦ LLᴴ",
    "description": "Multiply a matrix by its adjoint.",
    "precondition": "Finite square dimensions; no inverse or square root is evaluated.",
    "postcondition": "A for a valid Cholesky witness.",
    "totality": "total on the stated typed domain; no decision algorithm or factor-finding procedure is promised"
  },
  {
    "id": "urn:csabs:axiom/CholeskyDecomposition-factor-constraints",
    "type": "Axiom",
    "name": "factor-constraints",
    "statement": "The input is Hermitian positive definite and the lower factor has positive real diagonal.",
    "formalStatement": "Aᴴ=A; ∀x≠0,Re(xᴴAx)>0; ∀i<j,L_ij=0; ∀i,∃r_i∈ℝ_{>0},L_ii=r_i.",
    "assumptions": [
      "F is ℝ or ℂ and n≥0. A is Hermitian positive definite, tested by its exact quadratic form; complex diagonal entries of L are positive reals, not merely numbers with positive real part. Witness equality is entrywise equality of L. For n=0, positivity/triangular conditions are vacuous, the empty factor is unique and det(A)=1. Numerical failure tolerances and roundoff are outside this exact profile."
    ],
    "appliesTo": [
      "urn:csabs:concept/CholeskyDecomposition"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Mathematical definition; separate Lean evidence describes compiled interpretations.",
    "source": [
      "urn:csabs:source/higham-cholesky",
      "urn:csabs:source/lapack-lug-linear-equations"
    ],
    "sourceLocator": "Higham, opening definition and existence/uniqueness induction, determinant identity; LAPACK Users’ Guide §2.4.1, Hermitian Cholesky A=LL^H",
    "sourceNote": "Chooses lower L rather than Higham’s upper R, and extends the real transpose identities to conjugate transpose using the consulted LAPACK Hermitian profile. Adds explicit positive-real diagonal normalization, exact quadratic-form domain and empty-dimension convention. Does not import numerical stability bounds into the exact interface.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/CholeskyDecomposition-reconstruction",
    "type": "Axiom",
    "name": "reconstruction",
    "statement": "The lower factor and its adjoint reconstruct the input.",
    "formalStatement": "A=LLᴴ.",
    "assumptions": [
      "F is ℝ or ℂ and n≥0. A is Hermitian positive definite, tested by its exact quadratic form; complex diagonal entries of L are positive reals, not merely numbers with positive real part. Witness equality is entrywise equality of L. For n=0, positivity/triangular conditions are vacuous, the empty factor is unique and det(A)=1. Numerical failure tolerances and roundoff are outside this exact profile."
    ],
    "appliesTo": [
      "urn:csabs:concept/CholeskyDecomposition"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Mathematical definition; separate Lean evidence describes compiled interpretations.",
    "source": [
      "urn:csabs:source/higham-cholesky",
      "urn:csabs:source/lapack-lug-linear-equations"
    ],
    "sourceLocator": "Higham, opening definition and existence/uniqueness induction, determinant identity; LAPACK Users’ Guide §2.4.1, Hermitian Cholesky A=LL^H",
    "sourceNote": "Chooses lower L rather than Higham’s upper R, and extends the real transpose identities to conjugate transpose using the consulted LAPACK Hermitian profile. Adds explicit positive-real diagonal normalization, exact quadratic-form domain and empty-dimension convention. Does not import numerical stability bounds into the exact interface.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/CholeskyDecomposition-determinant",
    "type": "Law",
    "name": "determinant",
    "statement": "The determinant factors as a scalar times its conjugate.",
    "formalStatement": "det(A)=det(L)·conj(det(L)); over ℝ, det(A)=det(L)^2.",
    "assumptions": [
      "F is ℝ or ℂ and n≥0. A is Hermitian positive definite, tested by its exact quadratic form; complex diagonal entries of L are positive reals, not merely numbers with positive real part. Witness equality is entrywise equality of L. For n=0, positivity/triangular conditions are vacuous, the empty factor is unique and det(A)=1. Numerical failure tolerances and roundoff are outside this exact profile."
    ],
    "appliesTo": [
      "urn:csabs:concept/CholeskyDecomposition"
    ],
    "ruleRole": "derived-result",
    "dependsOn": [
      "urn:csabs:axiom/CholeskyDecomposition-reconstruction"
    ],
    "proofSketch": "Apply determinant multiplicativity to A=LLᴴ and use det(Lᴴ)=conj(det(L)). The real case has trivial conjugation. The compiled witness states the conjugate-product identity, whose real specialization is the displayed square.",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial mathematical statement; only separately registered fresh Lean witnesses are compiler-verified.",
    "source": [
      "urn:csabs:source/higham-cholesky",
      "urn:csabs:source/lapack-lug-linear-equations"
    ],
    "sourceLocator": "Higham, opening definition and existence/uniqueness induction, determinant identity; LAPACK Users’ Guide §2.4.1, Hermitian Cholesky A=LL^H",
    "sourceNote": "Derives the selected result from the linked factor constraints/reconstruction, using exact matrix algebra. Chooses lower L rather than Higham’s upper R, and extends the real transpose identities to conjugate transpose using the consulted LAPACK Hermitian profile. Adds explicit positive-real diagonal normalization, exact quadratic-form domain and empty-dimension convention. Does not import numerical stability bounds into the exact interface.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {F : Type u} [RCLike F] {n : Nat} {A : Catalog.Matrix F n n} (d : Catalog.CholeskyDecomposition A), A.det = d.lower.det * star d.lower.det",
    "formulationSource": "urn:csabs:source/local-lean-MatrixDecompositions",
    "formulationLocator": "Catalog.MatrixDecompositionProofs.cholesky_determinant",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "RCLike F, explicit exact Hermitian/quadratic-form positive-definiteness guard, a lower-triangular factor with each diagonal entry equal to a positive real, and exact A=L*L.conjTranspose. Positivity is supplied as a structure hypothesis, not a theorem fabricated by the model.",
    "leanModelLimitations": "Proves the displayed algebraic identity for a supplied valid witness, under the mapped exact scalar/dimension conventions. It does not prove factor existence/uniqueness, a numerical algorithm, stability or implementation conformance.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/CholeskyDecomposition-reconstruction\": \"The corresponding explicit structure fields supply this premise: A=LL*.\"}"
  },
  {
    "id": "urn:csabs:theorem/CholeskyDecomposition-existence-uniqueness",
    "type": "Theorem",
    "name": "existence-uniqueness",
    "statement": "Every Hermitian positive-definite matrix has exactly one lower Cholesky factor with positive real diagonal.",
    "formalStatement": "Aᴴ=A ∧ (∀x≠0,Re(xᴴAx)>0) ⇒ ∃!L, lower(L) ∧ (∀i,L_ii∈ℝ_{>0}) ∧ A=LLᴴ.",
    "assumptions": [
      "F is ℝ or ℂ and n≥0. A is Hermitian positive definite, tested by its exact quadratic form; complex diagonal entries of L are positive reals, not merely numbers with positive real part. Witness equality is entrywise equality of L. For n=0, positivity/triangular conditions are vacuous, the empty factor is unique and det(A)=1. Numerical failure tolerances and roundoff are outside this exact profile."
    ],
    "appliesTo": [
      "urn:csabs:concept/CholeskyDecomposition"
    ],
    "ruleRole": "derived-result",
    "dependsOn": [
      "urn:csabs:axiom/CholeskyDecomposition-factor-constraints",
      "urn:csabs:axiom/CholeskyDecomposition-reconstruction"
    ],
    "proofSketch": "Induct on dimension using the leading positive-definite principal block. Solve for the off-diagonal block with its already invertible triangular factor and take the unique positive square root of the positive Schur complement. The same recurrence forces uniqueness; dimension zero is the empty base case. In the complex case replace transpose by adjoint.",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial mathematical statement; only separately registered fresh Lean witnesses are compiler-verified.",
    "source": [
      "urn:csabs:source/higham-cholesky",
      "urn:csabs:source/lapack-lug-linear-equations"
    ],
    "sourceLocator": "Higham, opening definition and existence/uniqueness induction, determinant identity; LAPACK Users’ Guide §2.4.1, Hermitian Cholesky A=LL^H",
    "sourceNote": "Derives the selected result from the linked factor constraints/reconstruction, using exact matrix algebra. Chooses lower L rather than Higham’s upper R, and extends the real transpose identities to conjugate transpose using the consulted LAPACK Hermitian profile. Adds explicit positive-real diagonal normalization, exact quadratic-form domain and empty-dimension convention. Does not import numerical stability bounds into the exact interface.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
