# Exact structured matrix decomposition witness

A structured factor value together with an exact reconstruction equation for a finite matrix. The factor carrier and reconstruction map are parameters, allowing distinct factorization profiles without choosing a factor-finding algorithm.

**Notation:** D_ρ(A)={w∈W | ρ(w)=A}; ρ:W→F^{m×n}.

**Stable ID:** `urn:csabs:concept/MatrixDecomposition`

**Categories:** Algebra → Linear and multilinear algebra → Matrix decompositions

**Kind:** Mathematical structure

**Prerequisites:** [Finite rectangular matrix over a field](Matrix.md)

## Backlinks

- [Cholesky decomposition (Hermitian positive definite, lower profile)](CholeskyDecomposition.md) — `requiresConcept`
- [Cholesky decomposition (Hermitian positive definite, lower profile)](CholeskyDecomposition.md) — `specializationOf`
- [Eigendecomposition by a complete eigenbasis (diagonalization)](EigenDecomposition.md) — `requiresConcept`
- [Eigendecomposition by a complete eigenbasis (diagonalization)](EigenDecomposition.md) — `specializationOf`
- [Row-pivoted LU decomposition (square PA=LU profile)](LUDecomposition.md) — `requiresConcept`
- [Row-pivoted LU decomposition (square PA=LU profile)](LUDecomposition.md) — `specializationOf`
- [Finite rectangular matrix over a field](Matrix.md) — `relatedConcept`
- [Full QR decomposition (real or complex, rectangular)](QRDecomposition.md) — `requiresConcept`
- [Full QR decomposition (real or complex, rectangular)](QRDecomposition.md) — `specializationOf`
- [Full singular value decomposition (rectangular real or complex SVD)](SVD.md) — `requiresConcept`
- [Full singular value decomposition (rectangular real or complex SVD)](SVD.md) — `specializationOf`

## Mathematical formulation

For a field F, m,n∈ℕ, factor carrier W and total reconstruction map ρ:W→F^{m×n}, D\_ρ(A)={w∈W | ρ(w)=A}. Equality of witnesses compares their factor values, with proof components irrelevant; different witnesses may reconstruct the same A. A matrix has a decomposition in this profile exactly when A∈im(ρ). No existence is asserted for an arbitrary ρ.

**Lean formulation** (in its source module context):

```lean
structure MatrixDecomposition {F : Type u} [Field F] {m n : Nat}
    (W : Type v) (reconstruct : W → Catalog.Matrix F m n) (A : Catalog.Matrix F m n) where
  factors : W
  reconstructs : reconstruct factors = A
```

**Source:** [`Catalog.MatrixDecomposition`](../lean/Catalog/MatrixDecompositions.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Dependent witness structure indexed by W, a fixed reconstruction map and target A; factors are data and reconstructs is an equality proof. Equality is equality of factors; proof fields are irrelevant.

**Limits:** Exact selected witness/carrier model and factor observations. No factor-finding algorithm, decidable equality on real/complex entries, floating-point error analysis or general numerical implementation refinement. Only individually registered claims have compiled witnesses; existence/uniqueness results are not proved by structure fields.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Selected exact factor-carrier constraints and reconstruction equation. F is a field; m,n≥0 are finite dimensions; W is a specified structured factor carrier and ρ is a total, fixed reconstruction map. Matrix equality is entrywise exact equality. Empty dimensions are allowed. No numerical rounding, tolerance, iteration, resource failure or unique factor choice is implicit.

**basisKind:** defined-structure

**basisScope:** This selected factorization profile, not all numerical algorithms, alternative shapes or consequences.

**convention:** F is a field; m,n≥0 are finite dimensions; W is a specified structured factor carrier and ρ is a total, fixed reconstruction map. Matrix equality is entrywise exact equality. Empty dimensions are allowed. No numerical rounding, tolerance, iteration, resource failure or unique factor choice is implicit.

**verificationObligation:** Map factor dimensions, scalar field, adjoint/permutation conventions, equality and input guards before reusing equations in software. Approximate factors need a separately justified residual/error contract.

**reviewStatus:** Sourced mathematical interface with a separate compiled Lean interpretation and individually mapped witnesses.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-MatrixDecomposition-reconstruct"></a>

### reconstruct

`urn:csabs:operation/MatrixDecomposition-reconstruct`

**signature:** W → F^{m×n}; w ↦ ρ(w)

**description:** Evaluate the fixed reconstruction map on a factor value.

**precondition:** w∈W; all factor constraints belong to the chosen W.

**postcondition:** ρ(w), with exact entrywise equality.

**totality:** total on the stated typed domain; no decision algorithm or factor-finding procedure is promised

<a id="node-urn-csabs-operation-MatrixDecomposition-decomposes"></a>

### decomposes

`urn:csabs:operation/MatrixDecomposition-decomposes`

**signature:** F^{m×n}×W → Prop; (A,w) ↦ [ρ(w)=A]

**description:** Recognize the exact reconstruction relation, without asserting decidability.

**precondition:** A and w belong to the stated carriers.

**postcondition:** True exactly when w is a decomposition witness for A.

**totality:** total on the stated typed domain; no decision algorithm or factor-finding procedure is promised

## Axioms and defining rules

<a id="node-urn-csabs-axiom-MatrixDecomposition-reconstruction"></a>

### reconstruction

`urn:csabs:axiom/MatrixDecomposition-reconstruction`

**statement:** A valid factor value reconstructs its target matrix.

**formalStatement:** w∈D_ρ(A) ⇔ w∈W ∧ ρ(w)=A

**assumptions:** F is a field; m,n≥0 are finite dimensions; W is a specified structured factor carrier and ρ is a total, fixed reconstruction map. Matrix equality is entrywise exact equality. Empty dimensions are allowed. No numerical rounding, tolerance, iteration, resource failure or unique factor choice is implicit.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Mathematical definition; separate Lean evidence describes compiled interpretations.

**source:** [LAPACK Users’ Guide, Third Edition: Linear Equations](https://netlib.org/lapack/lug/node38.html); accessedOn: 2026-11-12; sourceRole: Consulted mathematical definition and factorization exposition; numerical algorithm/storage details are outside the selected exact model.; [LAPACK Users’ Guide, Third Edition: QR Factorization](https://netlib.org/lapack/lug/node40.html); accessedOn: 2026-11-12; sourceRole: Consulted mathematical definition and factorization exposition; numerical algorithm/storage details are outside the selected exact model.; [LAPACK Users’ Guide, Third Edition: Singular Value Decomposition](https://netlib.org/lapack/lug/node53.html); accessedOn: 2026-11-12; sourceRole: Consulted mathematical definition and factorization exposition; numerical algorithm/storage details are outside the selected exact model.

**sourceLocator:** LAPACK Users’ Guide §§2.4.1, 2.4.2.1, 2.4.6: displayed structured factorizations

**sourceNote:** Abstracts the consulted structured products into a typed factor carrier and reconstruction map. The parameterized witness interface, proof-irrelevant equality and empty-dimension convention are explicit adaptations; no universal factor-existence assumption is added.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-MatrixDecomposition-target-unique"></a>

### target-unique

`urn:csabs:law/MatrixDecomposition-target-unique`

**statement:** Equal factor values for a fixed reconstruction map determine the same target.

**formalStatement:** ∀w∈D_ρ(A),v∈D_ρ(B), w=v ⇒ A=B.

**assumptions:** F is a field; m,n≥0 are finite dimensions; W is a specified structured factor carrier and ρ is a total, fixed reconstruction map. Matrix equality is entrywise exact equality. Empty dimensions are allowed. No numerical rounding, tolerance, iteration, resource failure or unique factor choice is implicit.

**ruleRole:** derived-result

**dependsOn:** [reconstruction](MatrixDecomposition.md#node-urn-csabs-axiom-MatrixDecomposition-reconstruction)

**proofSketch:** Substitute equal factor values into the two reconstruction equations; both A and B equal the same ρ(w). This does not assert factor uniqueness for a fixed target.

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial mathematical statement; only separately registered fresh Lean witnesses are compiler-verified.

**source:** [LAPACK Users’ Guide, Third Edition: Linear Equations](https://netlib.org/lapack/lug/node38.html); accessedOn: 2026-11-12; sourceRole: Consulted mathematical definition and factorization exposition; numerical algorithm/storage details are outside the selected exact model.; [LAPACK Users’ Guide, Third Edition: QR Factorization](https://netlib.org/lapack/lug/node40.html); accessedOn: 2026-11-12; sourceRole: Consulted mathematical definition and factorization exposition; numerical algorithm/storage details are outside the selected exact model.; [LAPACK Users’ Guide, Third Edition: Singular Value Decomposition](https://netlib.org/lapack/lug/node53.html); accessedOn: 2026-11-12; sourceRole: Consulted mathematical definition and factorization exposition; numerical algorithm/storage details are outside the selected exact model.

**sourceLocator:** LAPACK Users’ Guide §§2.4.1, 2.4.2.1, 2.4.6: displayed structured factorizations

**sourceNote:** Derives the selected result from the linked factor constraints/reconstruction, using exact matrix algebra. Abstracts the consulted structured products into a typed factor carrier and reconstruction map. The parameterized witness interface, proof-irrelevant equality and empty-dimension convention are explicit adaptations; no universal factor-existence assumption is added.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {F : Type u} [Field F] {m n : Nat} {W : Type v} {r : W → Catalog.Matrix F m n} {A B : Catalog.Matrix F m n} (d : Catalog.MatrixDecomposition W r A) (e : Catalog.MatrixDecomposition W r B), d.factors = e.factors → A = B
```

**Source:** [`Catalog.MatrixDecompositionProofs.target_unique`](../lean/Catalog/MatrixDecompositions.lean); consulted 2026-11-12.

**Scope:** registered-witness-type

**Interpretation:** Dependent witness structure indexed by W, a fixed reconstruction map and target A; factors are data and reconstructs is an equality proof. Equality is equality of factors; proof fields are irrelevant.

**Limits:** Proves the displayed algebraic identity for a supplied valid witness, under the mapped exact scalar/dimension conventions. It does not prove factor existence/uniqueness, a numerical algorithm, stability or implementation conformance.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/MatrixDecomposition-reconstruction": "The corresponding explicit structure fields supply this premise: w∈D_ρ(A) ⇔ w∈W ∧ ρ(w)=A"
}
```

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [LAPACK Users’ Guide, Third Edition: Linear Equations](https://netlib.org/lapack/lug/node38.html); accessedOn: 2026-11-12; sourceRole: Consulted mathematical definition and factorization exposition; numerical algorithm/storage details are outside the selected exact model.
- [LAPACK Users’ Guide, Third Edition: QR Factorization](https://netlib.org/lapack/lug/node40.html); accessedOn: 2026-11-12; sourceRole: Consulted mathematical definition and factorization exposition; numerical algorithm/storage details are outside the selected exact model.
- [LAPACK Users’ Guide, Third Edition: Singular Value Decomposition](https://netlib.org/lapack/lug/node53.html); accessedOn: 2026-11-12; sourceRole: Consulted mathematical definition and factorization exposition; numerical algorithm/storage details are outside the selected exact model.

**sourceLocator:** LAPACK Users’ Guide §§2.4.1, 2.4.2.1, 2.4.6: displayed structured factorizations

**sourceNote:** Abstracts the consulted structured products into a typed factor carrier and reconstruction map. The parameterized witness interface, proof-irrelevant equality and empty-dimension convention are explicit adaptations; no universal factor-existence assumption is added.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/MatrixDecomposition",
    "type": "Concept",
    "shortForm": "MatrixDecomposition",
    "fullName": "Exact structured matrix decomposition witness",
    "category": [
      "urn:csabs:category/matrix-decompositions"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "A structured factor value together with an exact reconstruction equation for a finite matrix. The factor carrier and reconstruction map are parameters, allowing distinct factorization profiles without choosing a factor-finding algorithm.",
    "notation": "D_ρ(A)={w∈W | ρ(w)=A}; ρ:W→F^{m×n}.",
    "mathematicalFormulation": "For a field F, m,n∈ℕ, factor carrier W and total reconstruction map ρ:W→F^{m×n}, D_ρ(A)={w∈W | ρ(w)=A}. Equality of witnesses compares their factor values, with proof components irrelevant; different witnesses may reconstruct the same A. A matrix has a decomposition in this profile exactly when A∈im(ρ). No existence is asserted for an arbitrary ρ.",
    "hasOperation": [
      "urn:csabs:operation/MatrixDecomposition-reconstruct",
      "urn:csabs:operation/MatrixDecomposition-decomposes"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/MatrixDecomposition-reconstruction"
    ],
    "hasLaw": [
      "urn:csabs:law/MatrixDecomposition-target-unique"
    ],
    "hasTheorem": [],
    "requiresConcept": [
      "urn:csabs:concept/Matrix"
    ],
    "relatedConcept": [],
    "axiomBasis": "Selected exact factor-carrier constraints and reconstruction equation. F is a field; m,n≥0 are finite dimensions; W is a specified structured factor carrier and ρ is a total, fixed reconstruction map. Matrix equality is entrywise exact equality. Empty dimensions are allowed. No numerical rounding, tolerance, iteration, resource failure or unique factor choice is implicit.",
    "basisKind": "defined-structure",
    "basisScope": "This selected factorization profile, not all numerical algorithms, alternative shapes or consequences.",
    "convention": "F is a field; m,n≥0 are finite dimensions; W is a specified structured factor carrier and ρ is a total, fixed reconstruction map. Matrix equality is entrywise exact equality. Empty dimensions are allowed. No numerical rounding, tolerance, iteration, resource failure or unique factor choice is implicit.",
    "verificationObligation": "Map factor dimensions, scalar field, adjoint/permutation conventions, equality and input guards before reusing equations in software. Approximate factors need a separately justified residual/error contract.",
    "reviewStatus": "Sourced mathematical interface with a separate compiled Lean interpretation and individually mapped witnesses.",
    "coverageStatus": "basis-reviewed",
    "source": [
      "urn:csabs:source/lapack-lug-linear-equations",
      "urn:csabs:source/lapack-lug-qr",
      "urn:csabs:source/lapack-lug-svd"
    ],
    "sourceLocator": "LAPACK Users’ Guide §§2.4.1, 2.4.2.1, 2.4.6: displayed structured factorizations",
    "sourceNote": "Abstracts the consulted structured products into a typed factor carrier and reconstruction map. The parameterized witness interface, proof-irrelevant equality and empty-dimension convention are explicit adaptations; no universal factor-existence assumption is added.",
    "provenanceKind": "adapted",
    "leanFormulation": "structure MatrixDecomposition {F : Type u} [Field F] {m n : Nat}\n    (W : Type v) (reconstruct : W → Catalog.Matrix F m n) (A : Catalog.Matrix F m n) where\n  factors : W\n  reconstructs : reconstruct factors = A",
    "formulationSource": "urn:csabs:source/local-lean-MatrixDecompositions",
    "formulationLocator": "Catalog.MatrixDecomposition",
    "formulationScope": "model",
    "leanModelMapping": "Dependent witness structure indexed by W, a fixed reconstruction map and target A; factors are data and reconstructs is an equality proof. Equality is equality of factors; proof fields are irrelevant.",
    "leanModelLimitations": "Exact selected witness/carrier model and factor observations. No factor-finding algorithm, decidable equality on real/complex entries, floating-point error analysis or general numerical implementation refinement. Only individually registered claims have compiled witnesses; existence/uniqueness results are not proved by structure fields."
  },
  {
    "id": "urn:csabs:operation/MatrixDecomposition-reconstruct",
    "type": "Operation",
    "name": "reconstruct",
    "concept": "urn:csabs:concept/MatrixDecomposition",
    "signature": "W → F^{m×n}; w ↦ ρ(w)",
    "description": "Evaluate the fixed reconstruction map on a factor value.",
    "precondition": "w∈W; all factor constraints belong to the chosen W.",
    "postcondition": "ρ(w), with exact entrywise equality.",
    "totality": "total on the stated typed domain; no decision algorithm or factor-finding procedure is promised"
  },
  {
    "id": "urn:csabs:operation/MatrixDecomposition-decomposes",
    "type": "Operation",
    "name": "decomposes",
    "concept": "urn:csabs:concept/MatrixDecomposition",
    "signature": "F^{m×n}×W → Prop; (A,w) ↦ [ρ(w)=A]",
    "description": "Recognize the exact reconstruction relation, without asserting decidability.",
    "precondition": "A and w belong to the stated carriers.",
    "postcondition": "True exactly when w is a decomposition witness for A.",
    "totality": "total on the stated typed domain; no decision algorithm or factor-finding procedure is promised"
  },
  {
    "id": "urn:csabs:axiom/MatrixDecomposition-reconstruction",
    "type": "Axiom",
    "name": "reconstruction",
    "statement": "A valid factor value reconstructs its target matrix.",
    "formalStatement": "w∈D_ρ(A) ⇔ w∈W ∧ ρ(w)=A",
    "assumptions": [
      "F is a field; m,n≥0 are finite dimensions; W is a specified structured factor carrier and ρ is a total, fixed reconstruction map. Matrix equality is entrywise exact equality. Empty dimensions are allowed. No numerical rounding, tolerance, iteration, resource failure or unique factor choice is implicit."
    ],
    "appliesTo": [
      "urn:csabs:concept/MatrixDecomposition"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Mathematical definition; separate Lean evidence describes compiled interpretations.",
    "source": [
      "urn:csabs:source/lapack-lug-linear-equations",
      "urn:csabs:source/lapack-lug-qr",
      "urn:csabs:source/lapack-lug-svd"
    ],
    "sourceLocator": "LAPACK Users’ Guide §§2.4.1, 2.4.2.1, 2.4.6: displayed structured factorizations",
    "sourceNote": "Abstracts the consulted structured products into a typed factor carrier and reconstruction map. The parameterized witness interface, proof-irrelevant equality and empty-dimension convention are explicit adaptations; no universal factor-existence assumption is added.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/MatrixDecomposition-target-unique",
    "type": "Law",
    "name": "target-unique",
    "statement": "Equal factor values for a fixed reconstruction map determine the same target.",
    "formalStatement": "∀w∈D_ρ(A),v∈D_ρ(B), w=v ⇒ A=B.",
    "assumptions": [
      "F is a field; m,n≥0 are finite dimensions; W is a specified structured factor carrier and ρ is a total, fixed reconstruction map. Matrix equality is entrywise exact equality. Empty dimensions are allowed. No numerical rounding, tolerance, iteration, resource failure or unique factor choice is implicit."
    ],
    "appliesTo": [
      "urn:csabs:concept/MatrixDecomposition"
    ],
    "ruleRole": "derived-result",
    "dependsOn": [
      "urn:csabs:axiom/MatrixDecomposition-reconstruction"
    ],
    "proofSketch": "Substitute equal factor values into the two reconstruction equations; both A and B equal the same ρ(w). This does not assert factor uniqueness for a fixed target.",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial mathematical statement; only separately registered fresh Lean witnesses are compiler-verified.",
    "source": [
      "urn:csabs:source/lapack-lug-linear-equations",
      "urn:csabs:source/lapack-lug-qr",
      "urn:csabs:source/lapack-lug-svd"
    ],
    "sourceLocator": "LAPACK Users’ Guide §§2.4.1, 2.4.2.1, 2.4.6: displayed structured factorizations",
    "sourceNote": "Derives the selected result from the linked factor constraints/reconstruction, using exact matrix algebra. Abstracts the consulted structured products into a typed factor carrier and reconstruction map. The parameterized witness interface, proof-irrelevant equality and empty-dimension convention are explicit adaptations; no universal factor-existence assumption is added.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {F : Type u} [Field F] {m n : Nat} {W : Type v} {r : W → Catalog.Matrix F m n} {A B : Catalog.Matrix F m n} (d : Catalog.MatrixDecomposition W r A) (e : Catalog.MatrixDecomposition W r B), d.factors = e.factors → A = B",
    "formulationSource": "urn:csabs:source/local-lean-MatrixDecompositions",
    "formulationLocator": "Catalog.MatrixDecompositionProofs.target_unique",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Dependent witness structure indexed by W, a fixed reconstruction map and target A; factors are data and reconstructs is an equality proof. Equality is equality of factors; proof fields are irrelevant.",
    "leanModelLimitations": "Proves the displayed algebraic identity for a supplied valid witness, under the mapped exact scalar/dimension conventions. It does not prove factor existence/uniqueness, a numerical algorithm, stability or implementation conformance.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/MatrixDecomposition-reconstruction\": \"The corresponding explicit structure fields supply this premise: w∈D_ρ(A) ⇔ w∈W ∧ ρ(w)=A\"}"
  }
]
```
<!-- graph-record:end -->
