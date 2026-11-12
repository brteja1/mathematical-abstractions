# Geometric lattices and cryptographic problem relations

These records use lattice to mean a discrete additive point group in real
Euclidean space. The existing [Lattice](../concepts/Lattice.md),
[CompleteLattice](../concepts/CompleteLattice.md) and
[JoinSemilattice](../concepts/JoinSemilattice.md) describe ordered carriers with
bounds. Neither meaning is a specialization of the other.

| Record | Mathematical role |
| --- | --- |
| [EuclideanLattice](../concepts/EuclideanLattice.md) | Independent real basis columns and their integer span; covolume and full-rank dual interface |
| [QaryLattice](../concepts/QaryLattice.md) | Integer kernel of a modular linear map, embedded in real space |
| [SVP](../concepts/SVP.md) | Nonzero shortest-vector search and its multiplicative approximation relation |
| [CVP](../concepts/CVP.md) | Closest-point search for an arbitrary target, permitting ties |
| [SIS](../concepts/SIS.md) | Short nonzero integer kernel witness for a uniformly sampled modular matrix |
| [LWE](../concepts/LWE.md) | Noisy modular linear sample law with explicit search and decision experiments |

## Carriers and hierarchy

A lattice basis `B` has `d` rows and `r` independent columns; lattice points are
`Bz` for integer coefficient columns `z`. Rank `r` can be below ambient
dimension `d`. Replacing B by BU for an integer unimodular U preserves the
point set; two unequal basis matrices may describe exactly the same lattice.
Real scalar closure is not assumed: the lattice is generally not a real
vector space. Its underlying additive group is a specialization of Group,
with the operations instantiated explicitly and established by a local theorem.

Intrinsic covolume uses `sqrt(det(BᵀB))`, a volume in the real span. The
rank-zero convention gives the singleton lattice and covolume 1. The dual
operation here requires full rank; taking all ambient integer-pairing vectors
for a deficient-rank lattice would include a continuous orthogonal complement.

For a q-ary kernel, A is `n × m` over `ℤ/qℤ`, and lattice points are integer
m-vectors with `Az = 0 mod q`. A is a parity-check matrix, not a basis. The
containments `qℤ^m ⊆ Λ ⊆ ℤ^m` establish full rank and discreteness. The index is
`|im A|`; it equals `q^n` only when the syndrome map is onto. Composite moduli
are permitted, so field rank arguments need additional assumptions. A
nonzero-syndrome equation describes a coset when consistent, rather than this
homogeneous lattice. QaryLattice specializes EuclideanLattice; the search
problems use lattices as inputs and are not lattice subtypes.

## Search and randomness conventions

All lengths are Euclidean ℓ₂ lengths. Exact SVP and CVP correspond to factor
γ = 1; larger factors allow larger solution sets. SVP excludes rank zero and
the zero vector. CVP admits rank zero, arbitrary targets and ties. Its distance
is attained, but a unique closest point needs an additional promise. These
are mathematical relations, not assertions of efficient exact solvers.
Computational claims require finite encodings; arbitrary real coordinates
alone do not provide a software representation or a complexity model.

SIS selects `0 < β < q`, excluding the trivial witness `q e_i`. A candidate
is an integer vector, not just a modular residue vector. A valid parameter
choice need not make every instance solvable. The explicit pigeonhole result
provides one sufficient regime: `2^m > q^n` and `sqrt(m) ≤ β < q`.

LWE specifies a normalized error distribution on the finite residue ring;
integer errors can be wrapped modulo q. Input vectors and errors are sampled
independently with fresh draws. A uniformly chosen secret is fixed across
all samples. Samples are independent conditional on that secret; marginalizing
over it can introduce dependence. The search experiment retains the hidden
secret to define success; it is not given to the recovery algorithm. The
decision experiment distinguishes the real sample-list marginal from uniform
pairs. Uniform modular errors make these two distributions identical. A
finite sample list need not identify a unique secret.

## Sources and claims

The sources were consulted on 2026-11-11:

- [Peikert, A Decade of Lattice Cryptography](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf), author manuscript dated 2016-02-17: §§2.2.1–2.2.2, 4.1.1 and 4.2.1.
- [Regev, Introduction to Lattices in Computer Science](https://cims.nyu.edu/~regev/teaching/lattices_fall_2004/ln/introduction.pdf), Fall 2004 notes: §§1–4, especially the basis, volume and search-problem definitions.
- [Regev, On Lattices, Learning with Errors, Random Linear Codes, and Cryptography](https://cims.nyu.edu/~regev/papers/qcrypto.pdf), author manuscript dated 2009-05-02: §1 modular-error formulation.

Each new concept and claim has direct provenance and locators. Derived results
also identify premises and give editorial proofs. Definitions of SIS or LWE
do not prove hardness for arbitrary dimensions, moduli, bounds or errors.
No worst-case/average-case reduction, security level, quantum-resistance
claim or complete KEM/encryption/signature scheme is asserted. GapSVP, SIVP,
bounded-distance decoding, discrete Gaussians, ring/module variants and
concrete standardized constructions remain separate possible extensions.

## Lean interpretation

[GeometricLattices.lean](../lean/Catalog/GeometricLattices.lean) provides six
explicitly partial bindings. EuclideanLattice has independent real columns
and existential integer-span membership. QaryLattice uses exact modular kernel
membership. SIS checks that kernel together with nonzeroness and a squared
length bound. LWE has normalized finite error mass and the exact dot-product
encoding, without implementing the joint random experiment.

The squared-length function is an explicit sum of coordinate squares. It does
not use the default norm on a Lean function space, which need not be Euclidean.
SVP/CVP bindings use squared inequalities against every competitor; their
correspondence to the catalog's minimum formulation needs attainment and is
not registered as a compiled witness. No solver, basis extraction, covolume,
duality, probability identity or hardness theorem has a new proof witness.
