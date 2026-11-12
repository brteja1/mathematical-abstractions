# Finite rectangular matrix over a field

A function from a finite row-index and column-index product to a specified field, with pointwise arithmetic and dimension-compatible matrix multiplication.

**Notation:** A∈F^{m×n}; m,n∈ℕ; A:[m]×[n]→F; [k]={0,…,k−1}

**Stable ID:** `urn:csabs:concept/Matrix`

**Categories:** Algebra → Linear and multilinear algebra

**Kind:** Mathematical structure

**Prerequisites:** [Field](Field.md), [Total function](Function.md), [Vector space over a field](VectorSpace.md)

**Specializes:** [Total function](Function.md)

**Related concepts:** [Fixed-length array](Array.md), [Linear map](LinearMap.md), [Tensor of specified valence on a finite-dimensional vector space](Tensor.md)

## Backlinks

- [Euclidean lattice (discrete integer-span lattice)](EuclideanLattice.md) — `requiresConcept`
- [Generator matrix of a linear block code (row convention)](GeneratorMatrix.md) — `requiresConcept`
- [Linear map](LinearMap.md) — `relatedConcept`
- [Markov chain (finite-state, discrete-time, time-homogeneous)](MarkovChain.md) — `requiresConcept`
- [Parity-check matrix of a linear block code (row convention)](ParityCheckMatrix.md) — `requiresConcept`
- [Finite stochastic channel](StochasticChannel.md) — `requiresConcept`
- [Tensor of specified valence on a finite-dimensional vector space](Tensor.md) — `relatedConcept`

## Mathematical formulation

Mat\_F(m,n)=Fin(m)→Fin(n)→F. Equality is entrywise; (AB)ᵢⱼ=Σ\_{k∈Fin(n)}AᵢₖBₖⱼ for conformable dimensions. Zero dimensions are allowed and an empty sum is 0.

**Lean formulation** (in its source module context):

```lean
abbrev Matrix (F : Type u) [_root_.Field F] (m n : Nat) :=
  _root_.Matrix (Fin m) (Fin n) F
```

**Source:** [`Catalog.Matrix`](../lean/Catalog/Algebra.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Mathlib Matrix (Fin m) (Fin n) F over a field; zero dimensions permitted; extensional entry equality.

**Limits:** Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Extensional entries, pointwise addition and scaling, transposition, and finite-sum row-by-column multiplication.

**basisKind:** defined-structure

**basisScope:** Exact rectangular matrices, including zero dimensions; multiplication is not elementwise and is defined only for matching inner dimensions.

**specializationNote:** At fixed m,n,F, regard a matrix as a total function [m]×[n]→F, with entrywise equality.

**verificationObligation:** Zero row or column dimensions are permitted; sums over empty indices equal 0_F. Matrix entries use exact field operations, not floating-point semantics.; A linear map has a matrix only after ordered bases are supplied. Rectangular matrices are not generally invertible or a ring.; Use the stated carriers and equality. Specialization does not automatically transfer operations or claims.

**reviewStatus:** editorial interface review; not machine-proved

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-Matrix-entry"></a>

### entry

`urn:csabs:operation/Matrix-entry`

**signature:** [m]×[n] → F; (i,j) ↦ Aᵢⱼ

**description:** Read a matrix entry at valid indices.

**precondition:** i∈[m] and j∈[n].

**postcondition:** Read a matrix entry at valid indices.

**totality:** total on the stated domain

<a id="node-urn-csabs-operation-Matrix-add"></a>

### add

`urn:csabs:operation/Matrix-add`

**signature:** F^{m×n} × F^{m×n} → F^{m×n}

**description:** Add matching-shape matrices entrywise.

**precondition:** Same field and same row and column dimensions.

**postcondition:** Add matching-shape matrices entrywise.

**totality:** total on the stated domain

<a id="node-urn-csabs-operation-Matrix-scale"></a>

### scale

`urn:csabs:operation/Matrix-scale`

**signature:** F×F^{m×n} → F^{m×n}

**description:** Scale every entry by the same field scalar.

**precondition:** Inputs belong to the stated domains.

**postcondition:** Scale every entry by the same field scalar.

**totality:** total on the stated domain

<a id="node-urn-csabs-operation-Matrix-multiply"></a>

### multiply

`urn:csabs:operation/Matrix-multiply`

**signature:** F^{m×n} × F^{n×p} → F^{m×p}

**description:** Multiply with row-by-column finite sums.

**precondition:** Same field and matching inner dimension n.

**postcondition:** Multiply with row-by-column finite sums.

**totality:** total on the stated domain

<a id="node-urn-csabs-operation-Matrix-transpose"></a>

### transpose

`urn:csabs:operation/Matrix-transpose`

**signature:** F^{m×n} → F^{n×m}; A ↦ Aᵀ

**description:** Interchange row and column indices without complex conjugation.

**precondition:** Inputs belong to the stated domains.

**postcondition:** Interchange row and column indices without complex conjugation.

**totality:** total on the stated domain

## Axioms and defining rules

<a id="node-urn-csabs-axiom-Matrix-pointwise-arithmetic"></a>

### pointwise-arithmetic

`urn:csabs:axiom/Matrix-pointwise-arithmetic`

**statement:** Addition and scaling are defined entrywise.

**formalStatement:** (A+B)ᵢⱼ=Aᵢⱼ+Bᵢⱼ; (aA)ᵢⱼ=aAᵢⱼ

**assumptions:** A∈F^{m×n}; m,n∈ℕ; A:[m]×[n]→F; [k]={0,…,k−1}; Use the concept’s declared semantic conventions.

**reviewStatus:** editorial definition; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Sheldon Axler, Linear Algebra Done Right, fourth edition (consulted revision dated 30 October 2026)](https://linear.axler.net/LADR4e.pdf); accessedOn: 2026-11-07; sourceRole: primary mathematical reference; license: CC BY-NC 4.0; licenseUrl: https://creativecommons.org/licenses/by-nc/4.0/; [Mathlib: matrices, extensional equality and transpose](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/Defs.html); accessedOn: 2026-11-07; sourceRole: primary mathematical definition reference

**sourceLocator:** §3C, matrix addition and scaling; Mathlib Matrix.add and Matrix.smul

**sourceNote:** Defining constraint or equation adapted to the declared carriers and catalog notation.

**provenanceKind:** adapted

**ruleRole:** definition

<a id="node-urn-csabs-axiom-Matrix-multiply-entry"></a>

### multiply-entry

`urn:csabs:axiom/Matrix-multiply-entry`

**statement:** Matrix multiplication contracts over the shared inner index.

**formalStatement:** (AB)ᵢₖ=∑_{j∈[n]}AᵢⱼBⱼₖ; ∑∅=0_F

**assumptions:** A∈F^{m×n}; m,n∈ℕ; A:[m]×[n]→F; [k]={0,…,k−1}; Use the concept’s declared semantic conventions.

**reviewStatus:** editorial definition; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Sheldon Axler, Linear Algebra Done Right, fourth edition (consulted revision dated 30 October 2026)](https://linear.axler.net/LADR4e.pdf); accessedOn: 2026-11-07; sourceRole: primary mathematical reference; license: CC BY-NC 4.0; licenseUrl: https://creativecommons.org/licenses/by-nc/4.0/

**sourceLocator:** §3C, matrix multiplication; extension to zero inner dimension

**sourceNote:** Defining constraint or equation adapted to the declared carriers and catalog notation.

**provenanceKind:** adapted

**ruleRole:** definition

<a id="node-urn-csabs-axiom-Matrix-transpose-entry"></a>

### transpose-entry

`urn:csabs:axiom/Matrix-transpose-entry`

**statement:** Transposition swaps the indices.

**formalStatement:** (Aᵀ)ⱼᵢ=Aᵢⱼ

**assumptions:** A∈F^{m×n}; m,n∈ℕ; A:[m]×[n]→F; [k]={0,…,k−1}; Use the concept’s declared semantic conventions.

**reviewStatus:** editorial definition; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Sheldon Axler, Linear Algebra Done Right, fourth edition (consulted revision dated 30 October 2026)](https://linear.axler.net/LADR4e.pdf); accessedOn: 2026-11-07; sourceRole: primary mathematical reference; license: CC BY-NC 4.0; licenseUrl: https://creativecommons.org/licenses/by-nc/4.0/; [Mathlib: matrices, extensional equality and transpose](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/Defs.html); accessedOn: 2026-11-07; sourceRole: primary mathematical definition reference

**sourceLocator:** Mathlib Matrix.transpose and Matrix.transpose_apply

**sourceNote:** Defining constraint or equation adapted to the declared carriers and catalog notation.

**provenanceKind:** adapted

**ruleRole:** definition

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-Matrix-entry-extensionality"></a>

### entry-extensionality

`urn:csabs:theorem/Matrix-entry-extensionality`

**statement:** Matrices with identical shape are equal exactly when every entry is equal.

**formalStatement:** A,B∈F^{m×n}: A=B ⇔ ∀i∈[m],j∈[n]:Aᵢⱼ=Bᵢⱼ

**assumptions:** A∈F^{m×n}; m,n∈ℕ; A:[m]×[n]→F; [k]={0,…,k−1}; Use the concept’s declared semantic conventions.

**reviewStatus:** editorial derivation; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Sheldon Axler, Linear Algebra Done Right, fourth edition (consulted revision dated 30 October 2026)](https://linear.axler.net/LADR4e.pdf); accessedOn: 2026-11-07; sourceRole: primary mathematical reference; license: CC BY-NC 4.0; licenseUrl: https://creativecommons.org/licenses/by-nc/4.0/; [Mathlib: matrices, extensional equality and transpose](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/Defs.html); accessedOn: 2026-11-07; sourceRole: primary mathematical definition reference

**sourceLocator:** Mathlib Matrix.ext_iff (adapted to product-index functions)

**sourceNote:** Specialized consequence of the existing function extensionality rule; no new independent equality axiom is introduced.

**provenanceKind:** derived

**dependsOn:** [extensionality](Function.md#node-urn-csabs-axiom-Function-extensionality); [entry](Matrix.md#node-urn-csabs-operation-Matrix-entry)

**proofSketch:** At fixed m,n,F, a matrix is the total entry function [m]×[n]→F. Instantiate the existing function extensionality rule on that product domain. This also covers an empty index product.

<a id="node-urn-csabs-theorem-Matrix-transpose-involution"></a>

### transpose-involution

`urn:csabs:theorem/Matrix-transpose-involution`

**statement:** Transposition twice restores the matrix.

**formalStatement:** (Aᵀ)ᵀ=A for A∈F^{m×n}

**assumptions:** A∈F^{m×n}; m,n∈ℕ; A:[m]×[n]→F; [k]={0,…,k−1}; Use the concept’s declared semantic conventions.

**reviewStatus:** editorial derivation; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Sheldon Axler, Linear Algebra Done Right, fourth edition (consulted revision dated 30 October 2026)](https://linear.axler.net/LADR4e.pdf); accessedOn: 2026-11-07; sourceRole: primary mathematical reference; license: CC BY-NC 4.0; licenseUrl: https://creativecommons.org/licenses/by-nc/4.0/; [Mathlib: matrices, extensional equality and transpose](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/Defs.html); accessedOn: 2026-11-07; sourceRole: primary mathematical definition reference

**sourceLocator:** Mathlib Matrix.transpose_apply (derived index-swap identity)

**sourceNote:** Derived from the linked local premises; proof sketch gives the adaptation.

**provenanceKind:** derived

**dependsOn:** [transpose-entry](Matrix.md#node-urn-csabs-axiom-Matrix-transpose-entry); [entry-extensionality](Matrix.md#node-urn-csabs-theorem-Matrix-entry-extensionality); [transpose](Matrix.md#node-urn-csabs-operation-Matrix-transpose)

**proofSketch:** For each valid (i,j), ((Aᵀ)ᵀ)ᵢⱼ=(Aᵀ)ⱼᵢ=Aᵢⱼ. Extensionality gives equality, including shapes with no entries.

<a id="node-urn-csabs-theorem-Matrix-product-associativity"></a>

### product-associativity

`urn:csabs:theorem/Matrix-product-associativity`

**statement:** Dimension-compatible exact matrix multiplication is associative.

**formalStatement:** A∈F^{m×n}, B∈F^{n×p}, C∈F^{p×q} ⇒ (AB)C=A(BC)

**assumptions:** A∈F^{m×n}; m,n∈ℕ; A:[m]×[n]→F; [k]={0,…,k−1}; Use the concept’s declared semantic conventions.

**reviewStatus:** editorial derivation; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Sheldon Axler, Linear Algebra Done Right, fourth edition (consulted revision dated 30 October 2026)](https://linear.axler.net/LADR4e.pdf); accessedOn: 2026-11-07; sourceRole: primary mathematical reference; license: CC BY-NC 4.0; licenseUrl: https://creativecommons.org/licenses/by-nc/4.0/

**sourceLocator:** §3C, properties of matrix multiplication

**sourceNote:** Derived from the linked local premises; proof sketch gives the adaptation.

**provenanceKind:** derived

**dependsOn:** [multiply-entry](Matrix.md#node-urn-csabs-axiom-Matrix-multiply-entry); [entry-extensionality](Matrix.md#node-urn-csabs-theorem-Matrix-entry-extensionality); [multiply](Matrix.md#node-urn-csabs-operation-Matrix-multiply)

**proofSketch:** Expand an entry on each side as a finite double sum. Field distributivity and associativity permit reordering the sums and reassociating each scalar product. Empty sums obey the same identity.

## Concept provenance

- [Sheldon Axler, Linear Algebra Done Right, fourth edition (consulted revision dated 30 October 2026)](https://linear.axler.net/LADR4e.pdf); accessedOn: 2026-11-07; sourceRole: primary mathematical reference; license: CC BY-NC 4.0; licenseUrl: https://creativecommons.org/licenses/by-nc/4.0/
- [Mathlib: matrices, extensional equality and transpose](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/Defs.html); accessedOn: 2026-11-07; sourceRole: primary mathematical definition reference

**sourceLocator:** §3C matrix arithmetic; Mathlib Matrix, Matrix.ext and Matrix.transpose (finite index types, general fields)

**sourceNote:** Interface adapted to the catalog notation and explicitly restricted to the stated scope.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/Matrix",
    "type": "Concept",
    "shortForm": "Matrix",
    "fullName": "Finite rectangular matrix over a field",
    "category": [
      "urn:csabs:category/linear-algebra"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "A function from a finite row-index and column-index product to a specified field, with pointwise arithmetic and dimension-compatible matrix multiplication.",
    "notation": "A∈F^{m×n}; m,n∈ℕ; A:[m]×[n]→F; [k]={0,…,k−1}",
    "hasOperation": [
      "urn:csabs:operation/Matrix-entry",
      "urn:csabs:operation/Matrix-add",
      "urn:csabs:operation/Matrix-scale",
      "urn:csabs:operation/Matrix-multiply",
      "urn:csabs:operation/Matrix-transpose"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/Matrix-pointwise-arithmetic",
      "urn:csabs:axiom/Matrix-multiply-entry",
      "urn:csabs:axiom/Matrix-transpose-entry"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/Matrix-entry-extensionality",
      "urn:csabs:theorem/Matrix-transpose-involution",
      "urn:csabs:theorem/Matrix-product-associativity"
    ],
    "axiomBasis": "Extensional entries, pointwise addition and scaling, transposition, and finite-sum row-by-column multiplication.",
    "basisKind": "defined-structure",
    "basisScope": "Exact rectangular matrices, including zero dimensions; multiplication is not elementwise and is defined only for matching inner dimensions.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "editorial interface review; not machine-proved",
    "requiresConcept": [
      "urn:csabs:concept/Field",
      "urn:csabs:concept/Function",
      "urn:csabs:concept/VectorSpace"
    ],
    "verificationObligation": [
      "Zero row or column dimensions are permitted; sums over empty indices equal 0_F. Matrix entries use exact field operations, not floating-point semantics.",
      "A linear map has a matrix only after ordered bases are supplied. Rectangular matrices are not generally invertible or a ring.",
      "Use the stated carriers and equality. Specialization does not automatically transfer operations or claims."
    ],
    "source": [
      "urn:csabs:source/axler-ladr4",
      "urn:csabs:source/mathlib-matrix-defs"
    ],
    "sourceLocator": "§3C matrix arithmetic; Mathlib Matrix, Matrix.ext and Matrix.transpose (finite index types, general fields)",
    "sourceNote": "Interface adapted to the catalog notation and explicitly restricted to the stated scope.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/Function"
    ],
    "specializationNote": "At fixed m,n,F, regard a matrix as a total function [m]×[n]→F, with entrywise equality.",
    "relatedConcept": [
      "urn:csabs:concept/Array",
      "urn:csabs:concept/LinearMap",
      "urn:csabs:concept/Tensor"
    ],
    "leanFormulation": "abbrev Matrix (F : Type u) [_root_.Field F] (m n : Nat) :=\n  _root_.Matrix (Fin m) (Fin n) F",
    "formulationSource": "urn:csabs:source/local-lean-Algebra",
    "formulationLocator": "Catalog.Matrix",
    "formulationScope": "model",
    "leanModelMapping": "Mathlib Matrix (Fin m) (Fin n) F over a field; zero dimensions permitted; extensional entry equality.",
    "leanModelLimitations": "Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.",
    "mathematicalFormulation": "Mat_F(m,n)=Fin(m)→Fin(n)→F. Equality is entrywise; (AB)ᵢⱼ=Σ_{k∈Fin(n)}AᵢₖBₖⱼ for conformable dimensions. Zero dimensions are allowed and an empty sum is 0."
  },
  {
    "id": "urn:csabs:operation/Matrix-entry",
    "type": "Operation",
    "name": "entry",
    "signature": "[m]×[n] → F; (i,j) ↦ Aᵢⱼ",
    "description": "Read a matrix entry at valid indices.",
    "concept": "urn:csabs:concept/Matrix",
    "precondition": "i∈[m] and j∈[n].",
    "postcondition": "Read a matrix entry at valid indices.",
    "totality": "total on the stated domain"
  },
  {
    "id": "urn:csabs:operation/Matrix-add",
    "type": "Operation",
    "name": "add",
    "signature": "F^{m×n} × F^{m×n} → F^{m×n}",
    "description": "Add matching-shape matrices entrywise.",
    "concept": "urn:csabs:concept/Matrix",
    "precondition": "Same field and same row and column dimensions.",
    "postcondition": "Add matching-shape matrices entrywise.",
    "totality": "total on the stated domain"
  },
  {
    "id": "urn:csabs:operation/Matrix-scale",
    "type": "Operation",
    "name": "scale",
    "signature": "F×F^{m×n} → F^{m×n}",
    "description": "Scale every entry by the same field scalar.",
    "concept": "urn:csabs:concept/Matrix",
    "precondition": "Inputs belong to the stated domains.",
    "postcondition": "Scale every entry by the same field scalar.",
    "totality": "total on the stated domain"
  },
  {
    "id": "urn:csabs:operation/Matrix-multiply",
    "type": "Operation",
    "name": "multiply",
    "signature": "F^{m×n} × F^{n×p} → F^{m×p}",
    "description": "Multiply with row-by-column finite sums.",
    "concept": "urn:csabs:concept/Matrix",
    "precondition": "Same field and matching inner dimension n.",
    "postcondition": "Multiply with row-by-column finite sums.",
    "totality": "total on the stated domain"
  },
  {
    "id": "urn:csabs:operation/Matrix-transpose",
    "type": "Operation",
    "name": "transpose",
    "signature": "F^{m×n} → F^{n×m}; A ↦ Aᵀ",
    "description": "Interchange row and column indices without complex conjugation.",
    "concept": "urn:csabs:concept/Matrix",
    "precondition": "Inputs belong to the stated domains.",
    "postcondition": "Interchange row and column indices without complex conjugation.",
    "totality": "total on the stated domain"
  },
  {
    "id": "urn:csabs:axiom/Matrix-pointwise-arithmetic",
    "type": "Axiom",
    "name": "pointwise-arithmetic",
    "statement": "Addition and scaling are defined entrywise.",
    "formalStatement": "(A+B)ᵢⱼ=Aᵢⱼ+Bᵢⱼ; (aA)ᵢⱼ=aAᵢⱼ",
    "appliesTo": [
      "urn:csabs:concept/Matrix"
    ],
    "assumptions": [
      "A∈F^{m×n}; m,n∈ℕ; A:[m]×[n]→F; [k]={0,…,k−1}",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial definition; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/axler-ladr4",
      "urn:csabs:source/mathlib-matrix-defs"
    ],
    "sourceLocator": "§3C, matrix addition and scaling; Mathlib Matrix.add and Matrix.smul",
    "sourceNote": "Defining constraint or equation adapted to the declared carriers and catalog notation.",
    "provenanceKind": "adapted",
    "ruleRole": "definition"
  },
  {
    "id": "urn:csabs:axiom/Matrix-multiply-entry",
    "type": "Axiom",
    "name": "multiply-entry",
    "statement": "Matrix multiplication contracts over the shared inner index.",
    "formalStatement": "(AB)ᵢₖ=∑_{j∈[n]}AᵢⱼBⱼₖ; ∑∅=0_F",
    "appliesTo": [
      "urn:csabs:concept/Matrix"
    ],
    "assumptions": [
      "A∈F^{m×n}; m,n∈ℕ; A:[m]×[n]→F; [k]={0,…,k−1}",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial definition; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/axler-ladr4"
    ],
    "sourceLocator": "§3C, matrix multiplication; extension to zero inner dimension",
    "sourceNote": "Defining constraint or equation adapted to the declared carriers and catalog notation.",
    "provenanceKind": "adapted",
    "ruleRole": "definition"
  },
  {
    "id": "urn:csabs:axiom/Matrix-transpose-entry",
    "type": "Axiom",
    "name": "transpose-entry",
    "statement": "Transposition swaps the indices.",
    "formalStatement": "(Aᵀ)ⱼᵢ=Aᵢⱼ",
    "appliesTo": [
      "urn:csabs:concept/Matrix"
    ],
    "assumptions": [
      "A∈F^{m×n}; m,n∈ℕ; A:[m]×[n]→F; [k]={0,…,k−1}",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial definition; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/axler-ladr4",
      "urn:csabs:source/mathlib-matrix-defs"
    ],
    "sourceLocator": "Mathlib Matrix.transpose and Matrix.transpose_apply",
    "sourceNote": "Defining constraint or equation adapted to the declared carriers and catalog notation.",
    "provenanceKind": "adapted",
    "ruleRole": "definition"
  },
  {
    "id": "urn:csabs:theorem/Matrix-entry-extensionality",
    "type": "Theorem",
    "name": "entry-extensionality",
    "statement": "Matrices with identical shape are equal exactly when every entry is equal.",
    "formalStatement": "A,B∈F^{m×n}: A=B ⇔ ∀i∈[m],j∈[n]:Aᵢⱼ=Bᵢⱼ",
    "appliesTo": [
      "urn:csabs:concept/Matrix"
    ],
    "assumptions": [
      "A∈F^{m×n}; m,n∈ℕ; A:[m]×[n]→F; [k]={0,…,k−1}",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial derivation; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/axler-ladr4",
      "urn:csabs:source/mathlib-matrix-defs"
    ],
    "sourceLocator": "Mathlib Matrix.ext_iff (adapted to product-index functions)",
    "sourceNote": "Specialized consequence of the existing function extensionality rule; no new independent equality axiom is introduced.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/Function-extensionality",
      "urn:csabs:operation/Matrix-entry"
    ],
    "proofSketch": "At fixed m,n,F, a matrix is the total entry function [m]×[n]→F. Instantiate the existing function extensionality rule on that product domain. This also covers an empty index product."
  },
  {
    "id": "urn:csabs:theorem/Matrix-transpose-involution",
    "type": "Theorem",
    "name": "transpose-involution",
    "statement": "Transposition twice restores the matrix.",
    "formalStatement": "(Aᵀ)ᵀ=A for A∈F^{m×n}",
    "appliesTo": [
      "urn:csabs:concept/Matrix"
    ],
    "assumptions": [
      "A∈F^{m×n}; m,n∈ℕ; A:[m]×[n]→F; [k]={0,…,k−1}",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial derivation; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/axler-ladr4",
      "urn:csabs:source/mathlib-matrix-defs"
    ],
    "sourceLocator": "Mathlib Matrix.transpose_apply (derived index-swap identity)",
    "sourceNote": "Derived from the linked local premises; proof sketch gives the adaptation.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/Matrix-transpose-entry",
      "urn:csabs:theorem/Matrix-entry-extensionality",
      "urn:csabs:operation/Matrix-transpose"
    ],
    "proofSketch": "For each valid (i,j), ((Aᵀ)ᵀ)ᵢⱼ=(Aᵀ)ⱼᵢ=Aᵢⱼ. Extensionality gives equality, including shapes with no entries."
  },
  {
    "id": "urn:csabs:theorem/Matrix-product-associativity",
    "type": "Theorem",
    "name": "product-associativity",
    "statement": "Dimension-compatible exact matrix multiplication is associative.",
    "formalStatement": "A∈F^{m×n}, B∈F^{n×p}, C∈F^{p×q} ⇒ (AB)C=A(BC)",
    "appliesTo": [
      "urn:csabs:concept/Matrix"
    ],
    "assumptions": [
      "A∈F^{m×n}; m,n∈ℕ; A:[m]×[n]→F; [k]={0,…,k−1}",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial derivation; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/axler-ladr4"
    ],
    "sourceLocator": "§3C, properties of matrix multiplication",
    "sourceNote": "Derived from the linked local premises; proof sketch gives the adaptation.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/Matrix-multiply-entry",
      "urn:csabs:theorem/Matrix-entry-extensionality",
      "urn:csabs:operation/Matrix-multiply"
    ],
    "proofSketch": "Expand an entry on each side as a finite double sum. Field distributivity and associativity permit reordering the sums and reassociating each scalar product. Empty sums obey the same identity."
  }
]
```
<!-- graph-record:end -->
