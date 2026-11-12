# Matrix decompositions

The catalog models exact factorization relations and chosen factor witnesses. It does not select a floating-point algorithm, iteration rule or failure tolerance. Start with the relevant concept and operations; retrieve a theorem or Lean witness only when its result is needed.

| Concept | Reconstruction | Factor constraints and domain |
| --- | --- | --- |
| [MatrixDecomposition](../concepts/MatrixDecomposition.md) | ρ(w)=A | Parameterized factor carrier W and total reconstruction map ρ; no existence promise for arbitrary ρ. |
| [LUDecomposition](../concepts/LUDecomposition.md) | PA=LU | Square matrix over a field; row permutation P, unit lower-triangular L, upper-triangular U, possibly singular. |
| [QRDecomposition](../concepts/QRDecomposition.md) | A=QR | Real/complex rectangular A; full square unitary Q and upper-trapezoidal R, without sign/phase normalization. |
| [SVD](../concepts/SVD.md) | A=UΣVᴴ | Real/complex rectangular A; full unitary U,V and descending nonnegative real singular values. |
| [EigenDecomposition](../concepts/EigenDecomposition.md) | A=V diag(λ)V⁻¹ | Square A with an invertible eigenbasis over the selected field; matrices lacking one have no witness. |
| [CholeskyDecomposition](../concepts/CholeskyDecomposition.md) | A=LLᴴ | Real symmetric/complex Hermitian positive-definite A; lower-triangular L with positive real diagonal. |

All five profiles specialize the generic witness by instantiating its factor carrier and reconstruction map. They depend on [Matrix](../concepts/Matrix.md); they are not subtypes of the matrix carrier, and hierarchy links do not transfer axioms. Their subject is nested under linear and multilinear algebra.

## Conventions that affect reuse

`ᴴ` denotes conjugate transpose, reducing to transpose over the reals. The selected LU permutation acts by `(PA)ᵢⱼ=A_{p(i),j}`. The [LAPACK guide](https://netlib.org/lapack/lug/node38.html) writes `A=PLU`; invert that permutation to use this catalog's `PA=LU` convention. An API's pivot indices need an explicit translation to the resulting permutation.

The [QR profile](https://netlib.org/lapack/lug/node40.html) keeps Q square and R of shape m×n, including zero padding when m>n. It includes rank deficiency and either dimension order. Thin/reduced QR and column-pivoted QR need explicit variants. An unnormalized full QR does not choose unique factors.

The [SVD profile](https://netlib.org/lapack/lug/node53.html) keeps full U:m×m, V:n×n and min(m,n) singular values, including zeros. This count is not rank(A). Truncated SVD, numerical rank thresholds and choices within repeated singular spaces are separate concerns. An API returning Vᴴ needs a corresponding mapping; the catalog's factor observer returns V.

[Eigendecomposition](https://textbooks.math.gatech.edu/ila/diagonalization.html) requires a complete eigenbasis over the chosen field. Invertibility alone is insufficient; a defective Jordan block has no witness. A real rotation can fail to diagonalize over the reals even when complex diagonalization is possible. This relation is not Schur triangularization, and a general eigenbasis need not be orthogonal.

[Cholesky's positive-diagonal normalization](https://nhigham.com/2020/08/11/what-is-a-cholesky-factorization/) selects a unique triangular factor for positive-definite inputs. Complex factors use the [Hermitian adjoint convention](https://netlib.org/lapack/lug/node38.html). Semidefinite, pivoted and LDLᴴ variants are outside this entry. The triangular factor generally differs from the Hermitian principal square root.

Dimensions may be zero: empty identity matrices and products have their usual shapes, empty square determinants are 1, and triangular/positivity conditions use empty quantification. These are explicit catalog adaptations. Equality is exact and retains chosen factors; real/complex equality is not assumed decidable. Rounded factors need a separately specified residual/error relation and input/failure contract.

## Selected results and Lean scope

The pinned [Lean module](../lean/Catalog/MatrixDecompositions.lean) defines the six exact witness structures and encodes triangularity, permutation action, unitary equations, sorted singular values, a two-sided eigenbasis inverse and Cholesky's quadratic-form/positive-diagonal guards. Structure fields are hypotheses about supplied factors; they do not construct factors or prove existence.

| Registered claim | Symbol in Catalog.MatrixDecompositionProofs | Result |
| --- | --- | --- |
| MatrixDecomposition-target-unique | target_unique | Equal factor values for fixed ρ give the same target. |
| LUDecomposition-unpermute | lu_unpermute | A=PᵀLU. |
| QRDecomposition-gram | qr_gram | AᴴA=RᴴR. |
| SVD-coordinates | svd_coordinates | UᴴAV=Σ. |
| EigenDecomposition-basis-equation | eigen_basis_equation | AV=V diag(λ). |
| CholeskyDecomposition-determinant | cholesky_determinant | det(A)=det(L)·conj(det(L)). |

The records separately state sourced QR/SVD existence, the eigenbasis criterion and Cholesky existence/uniqueness with editorial proof sketches. These four theorems have no registered Lean proof witnesses. No factor-finding algorithms, numerical stability theorems or software refinement proofs are supplied. Mathematical provenance and compiler evidence remain separate.

## Focused retrieval

Choose the command matching the current task; this is not a sequence to preload:

```sh
python3 scripts/catalog.py list --category matrix-decompositions
python3 scripts/catalog.py get QRDecomposition --sections operations
python3 scripts/agent_query.py node urn:csabs:law/QRDecomposition-gram
python3 scripts/agent_query.py node urn:csabs:law/QRDecomposition-gram --view lean
python3 scripts/lean.py get urn:csabs:law/QRDecomposition-gram
```

Only current successful compilation and axiom-audit evidence supports calling a witness verified. `make check-lean` checks metadata; `make test-lean` produces compiler evidence. Normal focused queries do not include theorem lists or Lean excerpts unless requested.
