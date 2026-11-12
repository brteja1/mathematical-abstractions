# Row-pivoted LU decomposition (square PA=LU profile)

An exact square-matrix factorization with an explicit row permutation, unit lower-triangular L and upper-triangular U. It includes singular upper factors and does not select a pivoting algorithm.

**Notation:** PA=LU; P_ij=1 if j=p(i), otherwise 0; L_ii=1; L_ij=0 for i<j; U_ij=0 for i>j.

**Stable ID:** `urn:csabs:concept/LUDecomposition`

**Categories:** Algebra → Linear and multilinear algebra → Matrix decompositions

**Kind:** Mathematical structure

**Prerequisites:** [Exact structured matrix decomposition witness](MatrixDecomposition.md)

**Specializes:** [Exact structured matrix decomposition witness](MatrixDecomposition.md)

## Mathematical formulation

For A∈F^{n×n}, choose a permutation p of {0,…,n−1}, P\_ij=1 when j=p(i) and 0 otherwise, unit lower-triangular L and upper-triangular U, with PA=LU. Thus (PA)\_ij=A\_{p(i),j} and A=PᵀLU. U may be singular. The unpivoted variant sets P=I and may fail even for invertible A; no unpivoted-existence guarantee follows here.

**Lean formulation** (in its source module context):

```lean
structure LUDecomposition {F : Type u} [Field F] {n : Nat} (A : Catalog.Matrix F n n) where
  permutation : Equiv.Perm (Fin n)
  lower : Catalog.Matrix F n n
  upper : Catalog.Matrix F n n
  lower_triangular : matrixLower lower
  unit_diagonal : ∀ i, lower i i = 1
  upper_triangular : matrixUpper upper
  reconstructs : rowPermute permutation A = lower * upper
```

**Source:** [`Catalog.LUDecomposition`](../lean/Catalog/MatrixDecompositions.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Equiv.Perm (Fin n), explicit lower and upper matrices, triangular/unit-diagonal proof fields and rowPermute p A = L*U. The helper rowPermute p A evaluates A(p i,j), fixing the permutation convention.

**Limits:** Exact selected witness/carrier model and factor observations. No factor-finding algorithm, decidable equality on real/complex entries, floating-point error analysis or general numerical implementation refinement. Only individually registered claims have compiled witnesses; existence/uniqueness results are not proved by structure fields.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Selected exact factor-carrier constraints and reconstruction equation. F is a field and n≥0. Permutations act on rows as A(p(i),j); Pᵀ=P⁻¹. L has exact unit diagonal; U may have zero pivots. Equality compares the chosen p,L,U, not merely their reconstructed matrix. No partial-pivot, complete-pivot, growth or rounding policy is selected.

**basisKind:** defined-structure

**basisScope:** This selected factorization profile, not all numerical algorithms, alternative shapes or consequences.

**convention:** F is a field and n≥0. Permutations act on rows as A(p(i),j); Pᵀ=P⁻¹. L has exact unit diagonal; U may have zero pivots. Equality compares the chosen p,L,U, not merely their reconstructed matrix. No partial-pivot, complete-pivot, growth or rounding policy is selected.

**specializationNote:** Instantiate W with triples (p,L,U) satisfying permutation/unit-lower/upper constraints and ρ(p,L,U)=rowPermute(p⁻¹,LU)=PᵀLU. This is a factor-witness specialization, not a specialization of the matrix carrier itself.

**verificationObligation:** Map factor dimensions, scalar field, adjoint/permutation conventions, equality and input guards before reusing equations in software. Approximate factors need a separately justified residual/error contract.

**reviewStatus:** Sourced mathematical interface with a separate compiled Lean interpretation and individually mapped witnesses.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-LUDecomposition-factors"></a>

### factors

`urn:csabs:operation/LUDecomposition-factors`

**signature:** LU(A) → Perm(Fin(n))×F^{n×n}×F^{n×n}

**description:** Observe the chosen permutation, lower factor and upper factor.

**precondition:** Input is a valid row-pivoted LU witness.

**postcondition:** The exact tuple (p,L,U); ordering is fixed.

**totality:** total on the stated typed domain; no decision algorithm or factor-finding procedure is promised

<a id="node-urn-csabs-operation-LUDecomposition-reconstruct"></a>

### reconstruct

`urn:csabs:operation/LUDecomposition-reconstruct`

**signature:** Perm(Fin(n))×F^{n×n}×F^{n×n} → F^{n×n}; (p,L,U) ↦ PᵀLU

**description:** Undo the row permutation after multiplying factors.

**precondition:** Tuple has matching square dimensions.

**postcondition:** A when the tuple satisfies the defining rules for A.

**totality:** total on the stated typed domain; no decision algorithm or factor-finding procedure is promised

## Axioms and defining rules

<a id="node-urn-csabs-axiom-LUDecomposition-factor-constraints"></a>

### factor-constraints

`urn:csabs:axiom/LUDecomposition-factor-constraints`

**statement:** The factors have their selected permutation and triangular structure.

**formalStatement:** p is a permutation of Fin(n); P_ij=δ_{p(i),j}; ∀i<j,L_ij=0; ∀i,L_ii=1; ∀i>j,U_ij=0.

**assumptions:** F is a field and n≥0. Permutations act on rows as A(p(i),j); Pᵀ=P⁻¹. L has exact unit diagonal; U may have zero pivots. Equality compares the chosen p,L,U, not merely their reconstructed matrix. No partial-pivot, complete-pivot, growth or rounding policy is selected.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Mathematical definition; separate Lean evidence describes compiled interpretations.

**source:** [LAPACK Users’ Guide, Third Edition: Linear Equations](https://netlib.org/lapack/lug/node38.html); accessedOn: 2026-11-12; sourceRole: Consulted mathematical definition and factorization exposition; numerical algorithm/storage details are outside the selected exact model.

**sourceLocator:** LAPACK Users’ Guide §2.4.1, general matrices: A=PLU; triangular solve discussion

**sourceNote:** Uses the inverse of the source’s permutation so the selected convention is PA=LU. Restricts the rectangular LAPACK interface to square matrices and adapts the algebraic witness to an arbitrary field. Includes empty matrices and singular U; does not identify pivot arrays with final permutation matrices.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-LUDecomposition-reconstruction"></a>

### reconstruction

`urn:csabs:axiom/LUDecomposition-reconstruction`

**statement:** The row-permuted input is the product of the triangular factors.

**formalStatement:** PA=LU, equivalently ∀i,j,A_{p(i),j}=Σ_k L_ik U_kj.

**assumptions:** F is a field and n≥0. Permutations act on rows as A(p(i),j); Pᵀ=P⁻¹. L has exact unit diagonal; U may have zero pivots. Equality compares the chosen p,L,U, not merely their reconstructed matrix. No partial-pivot, complete-pivot, growth or rounding policy is selected.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Mathematical definition; separate Lean evidence describes compiled interpretations.

**source:** [LAPACK Users’ Guide, Third Edition: Linear Equations](https://netlib.org/lapack/lug/node38.html); accessedOn: 2026-11-12; sourceRole: Consulted mathematical definition and factorization exposition; numerical algorithm/storage details are outside the selected exact model.

**sourceLocator:** LAPACK Users’ Guide §2.4.1, general matrices: A=PLU; triangular solve discussion

**sourceNote:** Uses the inverse of the source’s permutation so the selected convention is PA=LU. Restricts the rectangular LAPACK interface to square matrices and adapts the algebraic witness to an arbitrary field. Includes empty matrices and singular U; does not identify pivot arrays with final permutation matrices.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-LUDecomposition-unpermute"></a>

### unpermute

`urn:csabs:law/LUDecomposition-unpermute`

**statement:** Undoing the row permutation reconstructs the original matrix.

**formalStatement:** A=Pᵀ(LU), equivalently A_ij=(LU)_{p⁻¹(i),j}.

**assumptions:** F is a field and n≥0. Permutations act on rows as A(p(i),j); Pᵀ=P⁻¹. L has exact unit diagonal; U may have zero pivots. Equality compares the chosen p,L,U, not merely their reconstructed matrix. No partial-pivot, complete-pivot, growth or rounding policy is selected.

**ruleRole:** derived-result

**dependsOn:** [factor-constraints](LUDecomposition.md#node-urn-csabs-axiom-LUDecomposition-factor-constraints); [reconstruction](LUDecomposition.md#node-urn-csabs-axiom-LUDecomposition-reconstruction)

**proofSketch:** Evaluate PA=LU at row p⁻¹(i); the inverse-permutation law reduces A(p(p⁻¹(i)),j) to A(i,j).

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial mathematical statement; only separately registered fresh Lean witnesses are compiler-verified.

**source:** [LAPACK Users’ Guide, Third Edition: Linear Equations](https://netlib.org/lapack/lug/node38.html); accessedOn: 2026-11-12; sourceRole: Consulted mathematical definition and factorization exposition; numerical algorithm/storage details are outside the selected exact model.

**sourceLocator:** LAPACK Users’ Guide §2.4.1, general matrices: A=PLU; triangular solve discussion

**sourceNote:** Derives the selected result from the linked factor constraints/reconstruction, using exact matrix algebra. Uses the inverse of the source’s permutation so the selected convention is PA=LU. Restricts the rectangular LAPACK interface to square matrices and adapts the algebraic witness to an arbitrary field. Includes empty matrices and singular U; does not identify pivot arrays with final permutation matrices.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {F : Type u} [Field F] {n : Nat} {A : Catalog.Matrix F n n} (d : Catalog.LUDecomposition A), A = Catalog.rowPermute d.permutation.symm (d.lower * d.upper)
```

**Source:** [`Catalog.MatrixDecompositionProofs.lu_unpermute`](../lean/Catalog/MatrixDecompositions.lean); consulted 2026-11-12.

**Scope:** registered-witness-type

**Interpretation:** Equiv.Perm (Fin n), explicit lower and upper matrices, triangular/unit-diagonal proof fields and rowPermute p A = L*U. The helper rowPermute p A evaluates A(p i,j), fixing the permutation convention.

**Limits:** Proves the displayed algebraic identity for a supplied valid witness, under the mapped exact scalar/dimension conventions. It does not prove factor existence/uniqueness, a numerical algorithm, stability or implementation conformance.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/LUDecomposition-factor-constraints": "The corresponding explicit structure fields supply this premise: p is a permutation of Fin(n); P_ij=δ_{p(i),j}; ∀i<j,L_ij=0; ∀i,L_ii=1; ∀i>j,U_ij=0. The proof uses the unitary or inverse identities; unused triangular/order/positivity fields remain profile constraints.",
  "urn:csabs:axiom/LUDecomposition-reconstruction": "The corresponding explicit structure fields supply this premise: PA=LU, equivalently ∀i,j,A_{p(i),j}=Σ_k L_ik U_kj. The proof uses the unitary or inverse identities; unused triangular/order/positivity fields remain profile constraints."
}
```

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [LAPACK Users’ Guide, Third Edition: Linear Equations](https://netlib.org/lapack/lug/node38.html); accessedOn: 2026-11-12; sourceRole: Consulted mathematical definition and factorization exposition; numerical algorithm/storage details are outside the selected exact model.

**sourceLocator:** LAPACK Users’ Guide §2.4.1, general matrices: A=PLU; triangular solve discussion

**sourceNote:** Uses the inverse of the source’s permutation so the selected convention is PA=LU. Restricts the rectangular LAPACK interface to square matrices and adapts the algebraic witness to an arbitrary field. Includes empty matrices and singular U; does not identify pivot arrays with final permutation matrices.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/LUDecomposition",
    "type": "Concept",
    "shortForm": "LUDecomposition",
    "fullName": "Row-pivoted LU decomposition (square PA=LU profile)",
    "category": [
      "urn:csabs:category/matrix-decompositions"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "An exact square-matrix factorization with an explicit row permutation, unit lower-triangular L and upper-triangular U. It includes singular upper factors and does not select a pivoting algorithm.",
    "notation": "PA=LU; P_ij=1 if j=p(i), otherwise 0; L_ii=1; L_ij=0 for i<j; U_ij=0 for i>j.",
    "mathematicalFormulation": "For A∈F^{n×n}, choose a permutation p of {0,…,n−1}, P_ij=1 when j=p(i) and 0 otherwise, unit lower-triangular L and upper-triangular U, with PA=LU. Thus (PA)_ij=A_{p(i),j} and A=PᵀLU. U may be singular. The unpivoted variant sets P=I and may fail even for invertible A; no unpivoted-existence guarantee follows here.",
    "hasOperation": [
      "urn:csabs:operation/LUDecomposition-factors",
      "urn:csabs:operation/LUDecomposition-reconstruct"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/LUDecomposition-factor-constraints",
      "urn:csabs:axiom/LUDecomposition-reconstruction"
    ],
    "hasLaw": [
      "urn:csabs:law/LUDecomposition-unpermute"
    ],
    "hasTheorem": [],
    "requiresConcept": [
      "urn:csabs:concept/MatrixDecomposition"
    ],
    "relatedConcept": [],
    "axiomBasis": "Selected exact factor-carrier constraints and reconstruction equation. F is a field and n≥0. Permutations act on rows as A(p(i),j); Pᵀ=P⁻¹. L has exact unit diagonal; U may have zero pivots. Equality compares the chosen p,L,U, not merely their reconstructed matrix. No partial-pivot, complete-pivot, growth or rounding policy is selected.",
    "basisKind": "defined-structure",
    "basisScope": "This selected factorization profile, not all numerical algorithms, alternative shapes or consequences.",
    "convention": "F is a field and n≥0. Permutations act on rows as A(p(i),j); Pᵀ=P⁻¹. L has exact unit diagonal; U may have zero pivots. Equality compares the chosen p,L,U, not merely their reconstructed matrix. No partial-pivot, complete-pivot, growth or rounding policy is selected.",
    "verificationObligation": "Map factor dimensions, scalar field, adjoint/permutation conventions, equality and input guards before reusing equations in software. Approximate factors need a separately justified residual/error contract.",
    "reviewStatus": "Sourced mathematical interface with a separate compiled Lean interpretation and individually mapped witnesses.",
    "coverageStatus": "basis-reviewed",
    "source": [
      "urn:csabs:source/lapack-lug-linear-equations"
    ],
    "sourceLocator": "LAPACK Users’ Guide §2.4.1, general matrices: A=PLU; triangular solve discussion",
    "sourceNote": "Uses the inverse of the source’s permutation so the selected convention is PA=LU. Restricts the rectangular LAPACK interface to square matrices and adapts the algebraic witness to an arbitrary field. Includes empty matrices and singular U; does not identify pivot arrays with final permutation matrices.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/MatrixDecomposition"
    ],
    "specializationNote": "Instantiate W with triples (p,L,U) satisfying permutation/unit-lower/upper constraints and ρ(p,L,U)=rowPermute(p⁻¹,LU)=PᵀLU. This is a factor-witness specialization, not a specialization of the matrix carrier itself.",
    "leanFormulation": "structure LUDecomposition {F : Type u} [Field F] {n : Nat} (A : Catalog.Matrix F n n) where\n  permutation : Equiv.Perm (Fin n)\n  lower : Catalog.Matrix F n n\n  upper : Catalog.Matrix F n n\n  lower_triangular : matrixLower lower\n  unit_diagonal : ∀ i, lower i i = 1\n  upper_triangular : matrixUpper upper\n  reconstructs : rowPermute permutation A = lower * upper",
    "formulationSource": "urn:csabs:source/local-lean-MatrixDecompositions",
    "formulationLocator": "Catalog.LUDecomposition",
    "formulationScope": "model",
    "leanModelMapping": "Equiv.Perm (Fin n), explicit lower and upper matrices, triangular/unit-diagonal proof fields and rowPermute p A = L*U. The helper rowPermute p A evaluates A(p i,j), fixing the permutation convention.",
    "leanModelLimitations": "Exact selected witness/carrier model and factor observations. No factor-finding algorithm, decidable equality on real/complex entries, floating-point error analysis or general numerical implementation refinement. Only individually registered claims have compiled witnesses; existence/uniqueness results are not proved by structure fields."
  },
  {
    "id": "urn:csabs:operation/LUDecomposition-factors",
    "type": "Operation",
    "name": "factors",
    "concept": "urn:csabs:concept/LUDecomposition",
    "signature": "LU(A) → Perm(Fin(n))×F^{n×n}×F^{n×n}",
    "description": "Observe the chosen permutation, lower factor and upper factor.",
    "precondition": "Input is a valid row-pivoted LU witness.",
    "postcondition": "The exact tuple (p,L,U); ordering is fixed.",
    "totality": "total on the stated typed domain; no decision algorithm or factor-finding procedure is promised"
  },
  {
    "id": "urn:csabs:operation/LUDecomposition-reconstruct",
    "type": "Operation",
    "name": "reconstruct",
    "concept": "urn:csabs:concept/LUDecomposition",
    "signature": "Perm(Fin(n))×F^{n×n}×F^{n×n} → F^{n×n}; (p,L,U) ↦ PᵀLU",
    "description": "Undo the row permutation after multiplying factors.",
    "precondition": "Tuple has matching square dimensions.",
    "postcondition": "A when the tuple satisfies the defining rules for A.",
    "totality": "total on the stated typed domain; no decision algorithm or factor-finding procedure is promised"
  },
  {
    "id": "urn:csabs:axiom/LUDecomposition-factor-constraints",
    "type": "Axiom",
    "name": "factor-constraints",
    "statement": "The factors have their selected permutation and triangular structure.",
    "formalStatement": "p is a permutation of Fin(n); P_ij=δ_{p(i),j}; ∀i<j,L_ij=0; ∀i,L_ii=1; ∀i>j,U_ij=0.",
    "assumptions": [
      "F is a field and n≥0. Permutations act on rows as A(p(i),j); Pᵀ=P⁻¹. L has exact unit diagonal; U may have zero pivots. Equality compares the chosen p,L,U, not merely their reconstructed matrix. No partial-pivot, complete-pivot, growth or rounding policy is selected."
    ],
    "appliesTo": [
      "urn:csabs:concept/LUDecomposition"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Mathematical definition; separate Lean evidence describes compiled interpretations.",
    "source": [
      "urn:csabs:source/lapack-lug-linear-equations"
    ],
    "sourceLocator": "LAPACK Users’ Guide §2.4.1, general matrices: A=PLU; triangular solve discussion",
    "sourceNote": "Uses the inverse of the source’s permutation so the selected convention is PA=LU. Restricts the rectangular LAPACK interface to square matrices and adapts the algebraic witness to an arbitrary field. Includes empty matrices and singular U; does not identify pivot arrays with final permutation matrices.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/LUDecomposition-reconstruction",
    "type": "Axiom",
    "name": "reconstruction",
    "statement": "The row-permuted input is the product of the triangular factors.",
    "formalStatement": "PA=LU, equivalently ∀i,j,A_{p(i),j}=Σ_k L_ik U_kj.",
    "assumptions": [
      "F is a field and n≥0. Permutations act on rows as A(p(i),j); Pᵀ=P⁻¹. L has exact unit diagonal; U may have zero pivots. Equality compares the chosen p,L,U, not merely their reconstructed matrix. No partial-pivot, complete-pivot, growth or rounding policy is selected."
    ],
    "appliesTo": [
      "urn:csabs:concept/LUDecomposition"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Mathematical definition; separate Lean evidence describes compiled interpretations.",
    "source": [
      "urn:csabs:source/lapack-lug-linear-equations"
    ],
    "sourceLocator": "LAPACK Users’ Guide §2.4.1, general matrices: A=PLU; triangular solve discussion",
    "sourceNote": "Uses the inverse of the source’s permutation so the selected convention is PA=LU. Restricts the rectangular LAPACK interface to square matrices and adapts the algebraic witness to an arbitrary field. Includes empty matrices and singular U; does not identify pivot arrays with final permutation matrices.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/LUDecomposition-unpermute",
    "type": "Law",
    "name": "unpermute",
    "statement": "Undoing the row permutation reconstructs the original matrix.",
    "formalStatement": "A=Pᵀ(LU), equivalently A_ij=(LU)_{p⁻¹(i),j}.",
    "assumptions": [
      "F is a field and n≥0. Permutations act on rows as A(p(i),j); Pᵀ=P⁻¹. L has exact unit diagonal; U may have zero pivots. Equality compares the chosen p,L,U, not merely their reconstructed matrix. No partial-pivot, complete-pivot, growth or rounding policy is selected."
    ],
    "appliesTo": [
      "urn:csabs:concept/LUDecomposition"
    ],
    "ruleRole": "derived-result",
    "dependsOn": [
      "urn:csabs:axiom/LUDecomposition-factor-constraints",
      "urn:csabs:axiom/LUDecomposition-reconstruction"
    ],
    "proofSketch": "Evaluate PA=LU at row p⁻¹(i); the inverse-permutation law reduces A(p(p⁻¹(i)),j) to A(i,j).",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial mathematical statement; only separately registered fresh Lean witnesses are compiler-verified.",
    "source": [
      "urn:csabs:source/lapack-lug-linear-equations"
    ],
    "sourceLocator": "LAPACK Users’ Guide §2.4.1, general matrices: A=PLU; triangular solve discussion",
    "sourceNote": "Derives the selected result from the linked factor constraints/reconstruction, using exact matrix algebra. Uses the inverse of the source’s permutation so the selected convention is PA=LU. Restricts the rectangular LAPACK interface to square matrices and adapts the algebraic witness to an arbitrary field. Includes empty matrices and singular U; does not identify pivot arrays with final permutation matrices.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {F : Type u} [Field F] {n : Nat} {A : Catalog.Matrix F n n} (d : Catalog.LUDecomposition A), A = Catalog.rowPermute d.permutation.symm (d.lower * d.upper)",
    "formulationSource": "urn:csabs:source/local-lean-MatrixDecompositions",
    "formulationLocator": "Catalog.MatrixDecompositionProofs.lu_unpermute",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Equiv.Perm (Fin n), explicit lower and upper matrices, triangular/unit-diagonal proof fields and rowPermute p A = L*U. The helper rowPermute p A evaluates A(p i,j), fixing the permutation convention.",
    "leanModelLimitations": "Proves the displayed algebraic identity for a supplied valid witness, under the mapped exact scalar/dimension conventions. It does not prove factor existence/uniqueness, a numerical algorithm, stability or implementation conformance.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/LUDecomposition-factor-constraints\": \"The corresponding explicit structure fields supply this premise: p is a permutation of Fin(n); P_ij=δ_{p(i),j}; ∀i<j,L_ij=0; ∀i,L_ii=1; ∀i>j,U_ij=0. The proof uses the unitary or inverse identities; unused triangular/order/positivity fields remain profile constraints.\", \"urn:csabs:axiom/LUDecomposition-reconstruction\": \"The corresponding explicit structure fields supply this premise: PA=LU, equivalently ∀i,j,A_{p(i),j}=Σ_k L_ik U_kj. The proof uses the unitary or inverse identities; unused triangular/order/positivity fields remain profile constraints.\"}"
  }
]
```
<!-- graph-record:end -->
