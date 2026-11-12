# Euclidean lattice (discrete integer-span lattice)

A discrete additive subgroup of a finite-dimensional real Euclidean space, represented by integer combinations of a real-linearly independent ordered basis. This is the geometric meaning of lattice, distinct from an order-theoretic lattice.

**Notation:** B∈ℝ^{d×r}; Λ(B)=Bℤ^r={Σᵢ zᵢbᵢ | z∈ℤ^r}; 0≤r≤d.

**Stable ID:** `urn:csabs:concept/EuclideanLattice`

**Categories:** Geometry and manifolds, Algebra → Linear and multilinear algebra, Cryptography → Public-key cryptography → Lattice-based cryptography

**Kind:** Mathematical structure

**Prerequisites:** [Vector space over a field](VectorSpace.md), [Finite rectangular matrix over a field](Matrix.md), [Mathematical integers](Integer.md), [Group](Group.md)

**Specializes:** [Group](Group.md)

## Backlinks

- [Closest vector problem (Euclidean search relation)](CVP.md) — `requiresConcept`
- [q-ary kernel lattice](QaryLattice.md) — `requiresConcept`
- [q-ary kernel lattice](QaryLattice.md) — `specializationOf`
- [Shortest vector problem (Euclidean search relation)](SVP.md) — `requiresConcept`

## Mathematical formulation

For linearly independent b₁,…,b\_r∈ℝ^d, L(B)={Σ\_{j=1}^r z\_j b\_j | z∈ℤ^r}. The selected norm is squared Euclidean length ‖x‖²=Σ\_{i=1}^d x\_i²; rank zero gives {0}.

**Lean formulation** (in its source module context):

```lean
structure EuclideanLattice (d r : Nat) where
  basis : Fin r → (Fin d → ℝ)
  independent : LinearIndependent ℝ basis
```

**Source:** [`Catalog.EuclideanLattice`](../lean/Catalog/GeometricLattices.lean); consulted 2026-11-12.

**Scope:** partial

**Interpretation:** Independent finite real columns and an existential integer-combination membership predicate; vector equality is pointwise. Rank zero is allowed.

**Limits:** No covolume or dual operation, generated Group instance, discreteness proof, basis-change proof or catalog claim witness. A real coordinate function space is used with an explicit squared Euclidean norm, not its default Pi norm.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** An independent basis and its integer-span carrier; restricted ambient addition and negation; Euclidean metric and intrinsic Gram-determinant covolume.

**basisKind:** defined-structure

**basisScope:** Finite d,r∈ℕ with r≤d; B has r real-linearly independent columns. Vectors use coordinatewise equality in ℝ^d; lattice equality is equality of point sets, not basis matrices. Use exact real arithmetic and the Euclidean norm, with no overflow or rounding. Rank r may be below ambient dimension d. If r=0, Λ={0}, the coefficient tuple is empty, and intrinsic covolume is 1 by the empty determinant convention. Λ is closed under integer scaling, generally not under real scaling. Computational inputs need a chosen finite rational/integer representation or an explicit real-arithmetic model.

**specializationNote:** Use carrier Λ(B), Group multiplication x·y:=x+y, identity 0 and inverse −x. The additive-subgroup theorem explicitly establishes these laws on this carrier. VectorSpace describes the ambient space; Λ itself is generally not a real vector space. There is no specialization relationship to the order-theoretic Lattice concept.

**verificationObligation:** Map exact carriers, equality, matrix orientation, norm, parameter ranges, randomness and error behavior before software use. Complexity statements require finite input encodings. Problem definitions and algebraic correctness do not establish hardness or security.

**reviewStatus:** Editorial mathematics; no compiled claim witness or cryptographic hardness proof.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-EuclideanLattice-combine"></a>

### combine

`urn:csabs:operation/EuclideanLattice-combine`

**source:** [Chris Peikert: A Decade of Lattice Cryptography (2016-02-17 author manuscript)](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf); accessedOn: 2026-11-11; sourceRole: author survey and mathematical definitions; [Oded Regev: Lattices in Computer Science, Introduction (Fall 2004 lecture notes)](https://cims.nyu.edu/~regev/teaching/lattices_fall_2004/ln/introduction.pdf); accessedOn: 2026-11-11; sourceRole: author course notes with definitions and proofs

**sourceLocator:** Peikert §2.2.1; Regev Introduction §§1–3, Definitions 1 and 5, Theorem 5 and Corollary 6

**sourceNote:** Retains arbitrary finite rank, including a stated rank-zero convention. The Gram determinant measures volume in the span, not d-dimensional volume for r<d.

**provenanceKind:** adapted

**signature:** combine_B : ℤ^r → Λ(B)

**description:** Interpret integer coefficients as a lattice point.

**precondition:** B has the stated independent columns; z has length r.

**postcondition:** Return Bz=Σᵢzᵢbᵢ; the empty sum is zero.

**totality:** Total as a mathematical specification on the stated domain; no efficient algorithm or exact-real decision procedure is asserted.

<a id="node-urn-csabs-operation-EuclideanLattice-contains"></a>

### contains

`urn:csabs:operation/EuclideanLattice-contains`

**source:** [Chris Peikert: A Decade of Lattice Cryptography (2016-02-17 author manuscript)](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf); accessedOn: 2026-11-11; sourceRole: author survey and mathematical definitions; [Oded Regev: Lattices in Computer Science, Introduction (Fall 2004 lecture notes)](https://cims.nyu.edu/~regev/teaching/lattices_fall_2004/ln/introduction.pdf); accessedOn: 2026-11-11; sourceRole: author course notes with definitions and proofs

**sourceLocator:** Peikert §2.2.1; Regev Introduction §§1–3, Definitions 1 and 5, Theorem 5 and Corollary 6

**sourceNote:** Retains arbitrary finite rank, including a stated rank-zero convention. The Gram determinant measures volume in the span, not d-dimensional volume for r<d.

**provenanceKind:** adapted

**signature:** contains_B : ℝ^d → Prop

**description:** Exact lattice-membership predicate.

**precondition:** A valid basis B and a d-dimensional vector x.

**postcondition:** True iff ∃z∈ℤ^r, x=Bz.

**totality:** Total as a mathematical specification on the stated domain; no efficient algorithm or exact-real decision procedure is asserted.

<a id="node-urn-csabs-operation-EuclideanLattice-add"></a>

### add

`urn:csabs:operation/EuclideanLattice-add`

**source:** [Chris Peikert: A Decade of Lattice Cryptography (2016-02-17 author manuscript)](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf); accessedOn: 2026-11-11; sourceRole: author survey and mathematical definitions; [Oded Regev: Lattices in Computer Science, Introduction (Fall 2004 lecture notes)](https://cims.nyu.edu/~regev/teaching/lattices_fall_2004/ln/introduction.pdf); accessedOn: 2026-11-11; sourceRole: author course notes with definitions and proofs

**sourceLocator:** Peikert §2.2.1; Regev Introduction §§1–3, Definitions 1 and 5, Theorem 5 and Corollary 6

**sourceNote:** Retains arbitrary finite rank, including a stated rank-zero convention. The Gram determinant measures volume in the span, not d-dimensional volume for r<d.

**provenanceKind:** adapted

**signature:** add : Λ×Λ → Λ

**description:** Add lattice points using ambient vector addition.

**precondition:** Both points lie in the same Λ.

**postcondition:** Bz+Bw=B(z+w).

**totality:** Total as a mathematical specification on the stated domain; no efficient algorithm or exact-real decision procedure is asserted.

<a id="node-urn-csabs-operation-EuclideanLattice-negate"></a>

### negate

`urn:csabs:operation/EuclideanLattice-negate`

**source:** [Chris Peikert: A Decade of Lattice Cryptography (2016-02-17 author manuscript)](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf); accessedOn: 2026-11-11; sourceRole: author survey and mathematical definitions; [Oded Regev: Lattices in Computer Science, Introduction (Fall 2004 lecture notes)](https://cims.nyu.edu/~regev/teaching/lattices_fall_2004/ln/introduction.pdf); accessedOn: 2026-11-11; sourceRole: author course notes with definitions and proofs

**sourceLocator:** Peikert §2.2.1; Regev Introduction §§1–3, Definitions 1 and 5, Theorem 5 and Corollary 6

**sourceNote:** Retains arbitrary finite rank, including a stated rank-zero convention. The Gram determinant measures volume in the span, not d-dimensional volume for r<d.

**provenanceKind:** adapted

**signature:** neg : Λ → Λ

**description:** Take the ambient additive inverse.

**precondition:** x∈Λ.

**postcondition:** −Bz=B(−z).

**totality:** Total as a mathematical specification on the stated domain; no efficient algorithm or exact-real decision procedure is asserted.

<a id="node-urn-csabs-operation-EuclideanLattice-covolume"></a>

### covolume

`urn:csabs:operation/EuclideanLattice-covolume`

**source:** [Chris Peikert: A Decade of Lattice Cryptography (2016-02-17 author manuscript)](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf); accessedOn: 2026-11-11; sourceRole: author survey and mathematical definitions; [Oded Regev: Lattices in Computer Science, Introduction (Fall 2004 lecture notes)](https://cims.nyu.edu/~regev/teaching/lattices_fall_2004/ln/introduction.pdf); accessedOn: 2026-11-11; sourceRole: author course notes with definitions and proofs

**sourceLocator:** Peikert §2.2.1; Regev Introduction §§1–3, Definitions 1 and 5, Theorem 5 and Corollary 6

**sourceNote:** Retains arbitrary finite rank, including a stated rank-zero convention. The Gram determinant measures volume in the span, not d-dimensional volume for r<d.

**provenanceKind:** adapted

**signature:** covol : Basis(d,r) → ℝ_{>0}

**description:** Intrinsic volume of a fundamental parallelepiped in the real span.

**precondition:** B has r independent columns.

**postcondition:** sqrt(det(BᵀB)); if r=d this is |det B|; if r=0 it is 1.

**totality:** Total as a mathematical specification on the stated domain; no efficient algorithm or exact-real decision procedure is asserted.

<a id="node-urn-csabs-operation-EuclideanLattice-dual"></a>

### dual

`urn:csabs:operation/EuclideanLattice-dual`

**source:** [Chris Peikert: A Decade of Lattice Cryptography (2016-02-17 author manuscript)](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf); accessedOn: 2026-11-11; sourceRole: author survey and mathematical definitions; [Oded Regev: Lattices in Computer Science, Introduction (Fall 2004 lecture notes)](https://cims.nyu.edu/~regev/teaching/lattices_fall_2004/ln/introduction.pdf); accessedOn: 2026-11-11; sourceRole: author course notes with definitions and proofs

**sourceLocator:** Peikert §2.2.1; Regev Introduction §§1–3, Definitions 1 and 5, Theorem 5 and Corollary 6

**sourceNote:** Retains arbitrary finite rank, including a stated rank-zero convention. The Gram determinant measures volume in the span, not d-dimensional volume for r<d.

**provenanceKind:** adapted

**signature:** dual : FullRankLattice(d) → FullRankLattice(d)

**description:** Take the Euclidean dual of a full-rank lattice.

**precondition:** r=d; B is square and invertible.

**postcondition:** Λ*= {y∈ℝ^d | ∀x∈Λ, ⟨y,x⟩∈ℤ}=B^(−ᵀ)ℤ^d. This operation excludes r<d, whose ambient integer-pairing set can contain a continuous orthogonal complement.

**totality:** Total as a mathematical specification on the stated domain; no efficient algorithm or exact-real decision procedure is asserted.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-EuclideanLattice-integer-span"></a>

### integer-span

`urn:csabs:axiom/EuclideanLattice-integer-span`

**source:** [Chris Peikert: A Decade of Lattice Cryptography (2016-02-17 author manuscript)](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf); accessedOn: 2026-11-11; sourceRole: author survey and mathematical definitions; [Oded Regev: Lattices in Computer Science, Introduction (Fall 2004 lecture notes)](https://cims.nyu.edu/~regev/teaching/lattices_fall_2004/ln/introduction.pdf); accessedOn: 2026-11-11; sourceRole: author course notes with definitions and proofs

**sourceLocator:** Peikert §2.2.1; Regev Introduction §§1–3, Definitions 1 and 5, Theorem 5 and Corollary 6

**sourceNote:** Retains arbitrary finite rank, including a stated rank-zero convention. The Gram determinant measures volume in the span, not d-dimensional volume for r<d.

**provenanceKind:** adapted

**statement:** The basis is real-linearly independent and the carrier is exactly its integer span.

**formalStatement:** B:ℝ^{d×r}, rank_ℝ(B)=r; Λ={Bz | z∈ℤ^r}; addition and negation are restricted ambient vector operations.

**assumptions:** Finite d,r∈ℕ with r≤d; B has r real-linearly independent columns. Vectors use coordinatewise equality in ℝ^d; lattice equality is equality of point sets, not basis matrices. Use exact real arithmetic and the Euclidean norm, with no overflow or rounding. Rank r may be below ambient dimension d. If r=0, Λ={0}, the coefficient tuple is empty, and intrinsic covolume is 1 by the empty determinant convention. Λ is closed under integer scaling, generally not under real scaling. Computational inputs need a chosen finite rational/integer representation or an explicit real-arithmetic model.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial statement and derivation; not machine-checked.

<a id="node-urn-csabs-axiom-EuclideanLattice-metric-volume"></a>

### metric-volume

`urn:csabs:axiom/EuclideanLattice-metric-volume`

**source:** [Chris Peikert: A Decade of Lattice Cryptography (2016-02-17 author manuscript)](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf); accessedOn: 2026-11-11; sourceRole: author survey and mathematical definitions; [Oded Regev: Lattices in Computer Science, Introduction (Fall 2004 lecture notes)](https://cims.nyu.edu/~regev/teaching/lattices_fall_2004/ln/introduction.pdf); accessedOn: 2026-11-11; sourceRole: author course notes with definitions and proofs

**sourceLocator:** Peikert §2.2.1; Regev Introduction §§1–3, Definitions 1 and 5, Theorem 5 and Corollary 6

**sourceNote:** Retains arbitrary finite rank, including a stated rank-zero convention. The Gram determinant measures volume in the span, not d-dimensional volume for r<d.

**provenanceKind:** adapted

**statement:** The geometry uses the standard Euclidean norm and intrinsic volume.

**formalStatement:** ‖x‖₂=√(Σᵢxᵢ²); covol(B)=√det(BᵀB); det of the empty Gram matrix is 1.

**assumptions:** Finite d,r∈ℕ with r≤d; B has r real-linearly independent columns. Vectors use coordinatewise equality in ℝ^d; lattice equality is equality of point sets, not basis matrices. Use exact real arithmetic and the Euclidean norm, with no overflow or rounding. Rank r may be below ambient dimension d. If r=0, Λ={0}, the coefficient tuple is empty, and intrinsic covolume is 1 by the empty determinant convention. Λ is closed under integer scaling, generally not under real scaling. Computational inputs need a chosen finite rational/integer representation or an explicit real-arithmetic model.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial statement and derivation; not machine-checked.

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-EuclideanLattice-additive-subgroup"></a>

### additive-subgroup

`urn:csabs:theorem/EuclideanLattice-additive-subgroup`

**source:** [Chris Peikert: A Decade of Lattice Cryptography (2016-02-17 author manuscript)](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf); accessedOn: 2026-11-11; sourceRole: author survey and mathematical definitions; [Oded Regev: Lattices in Computer Science, Introduction (Fall 2004 lecture notes)](https://cims.nyu.edu/~regev/teaching/lattices_fall_2004/ln/introduction.pdf); accessedOn: 2026-11-11; sourceRole: author course notes with definitions and proofs

**sourceLocator:** Peikert §2.2.1; Regev Introduction §§1–3, Definitions 1 and 5, Theorem 5 and Corollary 6

**sourceNote:** Editorial derivation from the linked premises. Retains arbitrary finite rank, including a stated rank-zero convention. The Gram determinant measures volume in the span, not d-dimensional volume for r<d.

**provenanceKind:** derived

**statement:** The point carrier forms an abelian group under its restricted operations.

**formalStatement:** 0∈Λ; x,y∈Λ⇒x+y∈Λ ∧ −x∈Λ; (x+y)+z=x+(y+z); x+y=y+x; x+0=0+x=x; x+(−x)=(−x)+x=0.

**dependsOn:** [integer-span](EuclideanLattice.md#node-urn-csabs-axiom-EuclideanLattice-integer-span)

**proofSketch:** Use zero coefficients, coefficient addition and coefficient negation to show closure. The remaining equations are the real-vector additive group equations restricted to Λ.

**assumptions:** Finite d,r∈ℕ with r≤d; B has r real-linearly independent columns. Vectors use coordinatewise equality in ℝ^d; lattice equality is equality of point sets, not basis matrices. Use exact real arithmetic and the Euclidean norm, with no overflow or rounding. Rank r may be below ambient dimension d. If r=0, Λ={0}, the coefficient tuple is empty, and intrinsic covolume is 1 by the empty determinant convention. Λ is closed under integer scaling, generally not under real scaling. Computational inputs need a chosen finite rational/integer representation or an explicit real-arithmetic model.

**ruleRole:** derived-result

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial statement and derivation; not machine-checked.

<a id="node-urn-csabs-theorem-EuclideanLattice-bounded-finiteness"></a>

### bounded-finiteness

`urn:csabs:theorem/EuclideanLattice-bounded-finiteness`

**source:** [Chris Peikert: A Decade of Lattice Cryptography (2016-02-17 author manuscript)](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf); accessedOn: 2026-11-11; sourceRole: author survey and mathematical definitions; [Oded Regev: Lattices in Computer Science, Introduction (Fall 2004 lecture notes)](https://cims.nyu.edu/~regev/teaching/lattices_fall_2004/ln/introduction.pdf); accessedOn: 2026-11-11; sourceRole: author course notes with definitions and proofs

**sourceLocator:** Peikert §2.2.1; Regev Introduction §§1–3, Definitions 1 and 5, Theorem 5 and Corollary 6

**sourceNote:** Editorial derivation from the linked premises. Retains arbitrary finite rank, including a stated rank-zero convention. The Gram determinant measures volume in the span, not d-dimensional volume for r<d.

**provenanceKind:** derived

**statement:** Every bounded ball contains only finitely many lattice points.

**formalStatement:** ∀t∈ℝ^d, R≥0, {v∈Λ | ‖v−t‖₂≤R} is finite; Λ is discrete.

**dependsOn:** [integer-span](EuclideanLattice.md#node-urn-csabs-axiom-EuclideanLattice-integer-span); [metric-volume](EuclideanLattice.md#node-urn-csabs-axiom-EuclideanLattice-metric-volume)

**proofSketch:** For r>0 an injective linear map B between finite-dimensional Euclidean spaces has a constant c>0 with ‖Bz‖₂≥c‖z‖₂. A radius-R ball about t bounds ‖Bz‖₂ by R+‖t‖₂ and hence bounds every integer coordinate of z, leaving finitely many possibilities. At r=0 the carrier has one point. Local isolation follows from this finiteness, or the same positive lower bound.

**assumptions:** Finite d,r∈ℕ with r≤d; B has r real-linearly independent columns. Vectors use coordinatewise equality in ℝ^d; lattice equality is equality of point sets, not basis matrices. Use exact real arithmetic and the Euclidean norm, with no overflow or rounding. Rank r may be below ambient dimension d. If r=0, Λ={0}, the coefficient tuple is empty, and intrinsic covolume is 1 by the empty determinant convention. Λ is closed under integer scaling, generally not under real scaling. Computational inputs need a chosen finite rational/integer representation or an explicit real-arithmetic model.

**ruleRole:** derived-result

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial statement and derivation; not machine-checked.

<a id="node-urn-csabs-theorem-EuclideanLattice-unimodular-invariance"></a>

### unimodular-invariance

`urn:csabs:theorem/EuclideanLattice-unimodular-invariance`

**source:** [Chris Peikert: A Decade of Lattice Cryptography (2016-02-17 author manuscript)](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf); accessedOn: 2026-11-11; sourceRole: author survey and mathematical definitions; [Oded Regev: Lattices in Computer Science, Introduction (Fall 2004 lecture notes)](https://cims.nyu.edu/~regev/teaching/lattices_fall_2004/ln/introduction.pdf); accessedOn: 2026-11-11; sourceRole: author course notes with definitions and proofs

**sourceLocator:** Peikert §2.2.1; Regev Introduction §§1–3, Definitions 1 and 5, Theorem 5 and Corollary 6

**sourceNote:** Editorial derivation from the linked premises. Retains arbitrary finite rank, including a stated rank-zero convention. The Gram determinant measures volume in the span, not d-dimensional volume for r<d.

**provenanceKind:** derived

**statement:** A unimodular integer change of basis preserves the lattice and covolume.

**formalStatement:** U∈ℤ^{r×r}, det U=±1 ⇒ Λ(BU)=Λ(B) ∧ covol(BU)=covol(B).

**dependsOn:** [integer-span](EuclideanLattice.md#node-urn-csabs-axiom-EuclideanLattice-integer-span); [metric-volume](EuclideanLattice.md#node-urn-csabs-axiom-EuclideanLattice-metric-volume)

**proofSketch:** The adjugate formula makes U inverse integral, so Uℤ^r=ℤ^r. For the Gram matrix, det(UᵀBᵀBU)=det(U)²det(BᵀB); take the nonnegative square root. The empty-matrix case has determinant 1.

**assumptions:** Finite d,r∈ℕ with r≤d; B has r real-linearly independent columns. Vectors use coordinatewise equality in ℝ^d; lattice equality is equality of point sets, not basis matrices. Use exact real arithmetic and the Euclidean norm, with no overflow or rounding. Rank r may be below ambient dimension d. If r=0, Λ={0}, the coefficient tuple is empty, and intrinsic covolume is 1 by the empty determinant convention. Λ is closed under integer scaling, generally not under real scaling. Computational inputs need a chosen finite rational/integer representation or an explicit real-arithmetic model.

**ruleRole:** derived-result

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial statement and derivation; not machine-checked.

## Concept provenance

- [Chris Peikert: A Decade of Lattice Cryptography (2016-02-17 author manuscript)](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf); accessedOn: 2026-11-11; sourceRole: author survey and mathematical definitions
- [Oded Regev: Lattices in Computer Science, Introduction (Fall 2004 lecture notes)](https://cims.nyu.edu/~regev/teaching/lattices_fall_2004/ln/introduction.pdf); accessedOn: 2026-11-11; sourceRole: author course notes with definitions and proofs

**sourceLocator:** Peikert §2.2.1; Regev Introduction §§1–3, Definitions 1 and 5, Theorem 5 and Corollary 6

**sourceNote:** Retains arbitrary finite rank, including a stated rank-zero convention. The Gram determinant measures volume in the span, not d-dimensional volume for r<d.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/EuclideanLattice",
    "type": "Concept",
    "shortForm": "EuclideanLattice",
    "fullName": "Euclidean lattice (discrete integer-span lattice)",
    "definition": "A discrete additive subgroup of a finite-dimensional real Euclidean space, represented by integer combinations of a real-linearly independent ordered basis. This is the geometric meaning of lattice, distinct from an order-theoretic lattice.",
    "notation": "B∈ℝ^{d×r}; Λ(B)=Bℤ^r={Σᵢ zᵢbᵢ | z∈ℤ^r}; 0≤r≤d.",
    "category": [
      "urn:csabs:category/geometry",
      "urn:csabs:category/linear-algebra",
      "urn:csabs:category/lattice-cryptography"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "requiresConcept": [
      "urn:csabs:concept/VectorSpace",
      "urn:csabs:concept/Matrix",
      "urn:csabs:concept/MathematicalInteger",
      "urn:csabs:concept/Group"
    ],
    "axiomBasis": "An independent basis and its integer-span carrier; restricted ambient addition and negation; Euclidean metric and intrinsic Gram-determinant covolume.",
    "basisKind": "defined-structure",
    "basisScope": "Finite d,r∈ℕ with r≤d; B has r real-linearly independent columns. Vectors use coordinatewise equality in ℝ^d; lattice equality is equality of point sets, not basis matrices. Use exact real arithmetic and the Euclidean norm, with no overflow or rounding. Rank r may be below ambient dimension d. If r=0, Λ={0}, the coefficient tuple is empty, and intrinsic covolume is 1 by the empty determinant convention. Λ is closed under integer scaling, generally not under real scaling. Computational inputs need a chosen finite rational/integer representation or an explicit real-arithmetic model.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial mathematics; no compiled claim witness or cryptographic hardness proof.",
    "verificationObligation": [
      "Map exact carriers, equality, matrix orientation, norm, parameter ranges, randomness and error behavior before software use. Complexity statements require finite input encodings. Problem definitions and algebraic correctness do not establish hardness or security."
    ],
    "source": [
      "urn:csabs:source/peikert-lattice-survey-2016",
      "urn:csabs:source/regev-lattice-introduction-2004"
    ],
    "sourceLocator": "Peikert §2.2.1; Regev Introduction §§1–3, Definitions 1 and 5, Theorem 5 and Corollary 6",
    "sourceNote": "Retains arbitrary finite rank, including a stated rank-zero convention. The Gram determinant measures volume in the span, not d-dimensional volume for r<d.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/Group"
    ],
    "specializationNote": "Use carrier Λ(B), Group multiplication x·y:=x+y, identity 0 and inverse −x. The additive-subgroup theorem explicitly establishes these laws on this carrier. VectorSpace describes the ambient space; Λ itself is generally not a real vector space. There is no specialization relationship to the order-theoretic Lattice concept.",
    "hasOperation": [
      "urn:csabs:operation/EuclideanLattice-combine",
      "urn:csabs:operation/EuclideanLattice-contains",
      "urn:csabs:operation/EuclideanLattice-add",
      "urn:csabs:operation/EuclideanLattice-negate",
      "urn:csabs:operation/EuclideanLattice-covolume",
      "urn:csabs:operation/EuclideanLattice-dual"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/EuclideanLattice-integer-span",
      "urn:csabs:axiom/EuclideanLattice-metric-volume"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/EuclideanLattice-additive-subgroup",
      "urn:csabs:theorem/EuclideanLattice-bounded-finiteness",
      "urn:csabs:theorem/EuclideanLattice-unimodular-invariance"
    ],
    "hasLaw": [],
    "leanFormulation": "structure EuclideanLattice (d r : Nat) where\n  basis : Fin r → (Fin d → ℝ)\n  independent : LinearIndependent ℝ basis",
    "formulationSource": "urn:csabs:source/local-lean-GeometricLattices",
    "formulationLocator": "Catalog.EuclideanLattice",
    "formulationScope": "partial",
    "leanModelMapping": "Independent finite real columns and an existential integer-combination membership predicate; vector equality is pointwise. Rank zero is allowed.",
    "leanModelLimitations": "No covolume or dual operation, generated Group instance, discreteness proof, basis-change proof or catalog claim witness. A real coordinate function space is used with an explicit squared Euclidean norm, not its default Pi norm.",
    "mathematicalFormulation": "For linearly independent b₁,…,b_r∈ℝ^d, L(B)={Σ_{j=1}^r z_j b_j | z∈ℤ^r}. The selected norm is squared Euclidean length ‖x‖²=Σ_{i=1}^d x_i²; rank zero gives {0}."
  },
  {
    "id": "urn:csabs:operation/EuclideanLattice-combine",
    "type": "Operation",
    "name": "combine",
    "source": [
      "urn:csabs:source/peikert-lattice-survey-2016",
      "urn:csabs:source/regev-lattice-introduction-2004"
    ],
    "sourceLocator": "Peikert §2.2.1; Regev Introduction §§1–3, Definitions 1 and 5, Theorem 5 and Corollary 6",
    "sourceNote": "Retains arbitrary finite rank, including a stated rank-zero convention. The Gram determinant measures volume in the span, not d-dimensional volume for r<d.",
    "provenanceKind": "adapted",
    "signature": "combine_B : ℤ^r → Λ(B)",
    "description": "Interpret integer coefficients as a lattice point.",
    "precondition": "B has the stated independent columns; z has length r.",
    "postcondition": "Return Bz=Σᵢzᵢbᵢ; the empty sum is zero.",
    "concept": "urn:csabs:concept/EuclideanLattice",
    "totality": "Total as a mathematical specification on the stated domain; no efficient algorithm or exact-real decision procedure is asserted."
  },
  {
    "id": "urn:csabs:operation/EuclideanLattice-contains",
    "type": "Operation",
    "name": "contains",
    "source": [
      "urn:csabs:source/peikert-lattice-survey-2016",
      "urn:csabs:source/regev-lattice-introduction-2004"
    ],
    "sourceLocator": "Peikert §2.2.1; Regev Introduction §§1–3, Definitions 1 and 5, Theorem 5 and Corollary 6",
    "sourceNote": "Retains arbitrary finite rank, including a stated rank-zero convention. The Gram determinant measures volume in the span, not d-dimensional volume for r<d.",
    "provenanceKind": "adapted",
    "signature": "contains_B : ℝ^d → Prop",
    "description": "Exact lattice-membership predicate.",
    "precondition": "A valid basis B and a d-dimensional vector x.",
    "postcondition": "True iff ∃z∈ℤ^r, x=Bz.",
    "concept": "urn:csabs:concept/EuclideanLattice",
    "totality": "Total as a mathematical specification on the stated domain; no efficient algorithm or exact-real decision procedure is asserted."
  },
  {
    "id": "urn:csabs:operation/EuclideanLattice-add",
    "type": "Operation",
    "name": "add",
    "source": [
      "urn:csabs:source/peikert-lattice-survey-2016",
      "urn:csabs:source/regev-lattice-introduction-2004"
    ],
    "sourceLocator": "Peikert §2.2.1; Regev Introduction §§1–3, Definitions 1 and 5, Theorem 5 and Corollary 6",
    "sourceNote": "Retains arbitrary finite rank, including a stated rank-zero convention. The Gram determinant measures volume in the span, not d-dimensional volume for r<d.",
    "provenanceKind": "adapted",
    "signature": "add : Λ×Λ → Λ",
    "description": "Add lattice points using ambient vector addition.",
    "precondition": "Both points lie in the same Λ.",
    "postcondition": "Bz+Bw=B(z+w).",
    "concept": "urn:csabs:concept/EuclideanLattice",
    "totality": "Total as a mathematical specification on the stated domain; no efficient algorithm or exact-real decision procedure is asserted."
  },
  {
    "id": "urn:csabs:operation/EuclideanLattice-negate",
    "type": "Operation",
    "name": "negate",
    "source": [
      "urn:csabs:source/peikert-lattice-survey-2016",
      "urn:csabs:source/regev-lattice-introduction-2004"
    ],
    "sourceLocator": "Peikert §2.2.1; Regev Introduction §§1–3, Definitions 1 and 5, Theorem 5 and Corollary 6",
    "sourceNote": "Retains arbitrary finite rank, including a stated rank-zero convention. The Gram determinant measures volume in the span, not d-dimensional volume for r<d.",
    "provenanceKind": "adapted",
    "signature": "neg : Λ → Λ",
    "description": "Take the ambient additive inverse.",
    "precondition": "x∈Λ.",
    "postcondition": "−Bz=B(−z).",
    "concept": "urn:csabs:concept/EuclideanLattice",
    "totality": "Total as a mathematical specification on the stated domain; no efficient algorithm or exact-real decision procedure is asserted."
  },
  {
    "id": "urn:csabs:operation/EuclideanLattice-covolume",
    "type": "Operation",
    "name": "covolume",
    "source": [
      "urn:csabs:source/peikert-lattice-survey-2016",
      "urn:csabs:source/regev-lattice-introduction-2004"
    ],
    "sourceLocator": "Peikert §2.2.1; Regev Introduction §§1–3, Definitions 1 and 5, Theorem 5 and Corollary 6",
    "sourceNote": "Retains arbitrary finite rank, including a stated rank-zero convention. The Gram determinant measures volume in the span, not d-dimensional volume for r<d.",
    "provenanceKind": "adapted",
    "signature": "covol : Basis(d,r) → ℝ_{>0}",
    "description": "Intrinsic volume of a fundamental parallelepiped in the real span.",
    "precondition": "B has r independent columns.",
    "postcondition": "sqrt(det(BᵀB)); if r=d this is |det B|; if r=0 it is 1.",
    "concept": "urn:csabs:concept/EuclideanLattice",
    "totality": "Total as a mathematical specification on the stated domain; no efficient algorithm or exact-real decision procedure is asserted."
  },
  {
    "id": "urn:csabs:operation/EuclideanLattice-dual",
    "type": "Operation",
    "name": "dual",
    "source": [
      "urn:csabs:source/peikert-lattice-survey-2016",
      "urn:csabs:source/regev-lattice-introduction-2004"
    ],
    "sourceLocator": "Peikert §2.2.1; Regev Introduction §§1–3, Definitions 1 and 5, Theorem 5 and Corollary 6",
    "sourceNote": "Retains arbitrary finite rank, including a stated rank-zero convention. The Gram determinant measures volume in the span, not d-dimensional volume for r<d.",
    "provenanceKind": "adapted",
    "signature": "dual : FullRankLattice(d) → FullRankLattice(d)",
    "description": "Take the Euclidean dual of a full-rank lattice.",
    "precondition": "r=d; B is square and invertible.",
    "postcondition": "Λ*= {y∈ℝ^d | ∀x∈Λ, ⟨y,x⟩∈ℤ}=B^(−ᵀ)ℤ^d. This operation excludes r<d, whose ambient integer-pairing set can contain a continuous orthogonal complement.",
    "concept": "urn:csabs:concept/EuclideanLattice",
    "totality": "Total as a mathematical specification on the stated domain; no efficient algorithm or exact-real decision procedure is asserted."
  },
  {
    "id": "urn:csabs:axiom/EuclideanLattice-integer-span",
    "type": "Axiom",
    "name": "integer-span",
    "source": [
      "urn:csabs:source/peikert-lattice-survey-2016",
      "urn:csabs:source/regev-lattice-introduction-2004"
    ],
    "sourceLocator": "Peikert §2.2.1; Regev Introduction §§1–3, Definitions 1 and 5, Theorem 5 and Corollary 6",
    "sourceNote": "Retains arbitrary finite rank, including a stated rank-zero convention. The Gram determinant measures volume in the span, not d-dimensional volume for r<d.",
    "provenanceKind": "adapted",
    "statement": "The basis is real-linearly independent and the carrier is exactly its integer span.",
    "formalStatement": "B:ℝ^{d×r}, rank_ℝ(B)=r; Λ={Bz | z∈ℤ^r}; addition and negation are restricted ambient vector operations.",
    "appliesTo": [
      "urn:csabs:concept/EuclideanLattice"
    ],
    "assumptions": [
      "Finite d,r∈ℕ with r≤d; B has r real-linearly independent columns. Vectors use coordinatewise equality in ℝ^d; lattice equality is equality of point sets, not basis matrices. Use exact real arithmetic and the Euclidean norm, with no overflow or rounding. Rank r may be below ambient dimension d. If r=0, Λ={0}, the coefficient tuple is empty, and intrinsic covolume is 1 by the empty determinant convention. Λ is closed under integer scaling, generally not under real scaling. Computational inputs need a chosen finite rational/integer representation or an explicit real-arithmetic model."
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial statement and derivation; not machine-checked."
  },
  {
    "id": "urn:csabs:axiom/EuclideanLattice-metric-volume",
    "type": "Axiom",
    "name": "metric-volume",
    "source": [
      "urn:csabs:source/peikert-lattice-survey-2016",
      "urn:csabs:source/regev-lattice-introduction-2004"
    ],
    "sourceLocator": "Peikert §2.2.1; Regev Introduction §§1–3, Definitions 1 and 5, Theorem 5 and Corollary 6",
    "sourceNote": "Retains arbitrary finite rank, including a stated rank-zero convention. The Gram determinant measures volume in the span, not d-dimensional volume for r<d.",
    "provenanceKind": "adapted",
    "statement": "The geometry uses the standard Euclidean norm and intrinsic volume.",
    "formalStatement": "‖x‖₂=√(Σᵢxᵢ²); covol(B)=√det(BᵀB); det of the empty Gram matrix is 1.",
    "appliesTo": [
      "urn:csabs:concept/EuclideanLattice"
    ],
    "assumptions": [
      "Finite d,r∈ℕ with r≤d; B has r real-linearly independent columns. Vectors use coordinatewise equality in ℝ^d; lattice equality is equality of point sets, not basis matrices. Use exact real arithmetic and the Euclidean norm, with no overflow or rounding. Rank r may be below ambient dimension d. If r=0, Λ={0}, the coefficient tuple is empty, and intrinsic covolume is 1 by the empty determinant convention. Λ is closed under integer scaling, generally not under real scaling. Computational inputs need a chosen finite rational/integer representation or an explicit real-arithmetic model."
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial statement and derivation; not machine-checked."
  },
  {
    "id": "urn:csabs:theorem/EuclideanLattice-additive-subgroup",
    "type": "Theorem",
    "name": "additive-subgroup",
    "source": [
      "urn:csabs:source/peikert-lattice-survey-2016",
      "urn:csabs:source/regev-lattice-introduction-2004"
    ],
    "sourceLocator": "Peikert §2.2.1; Regev Introduction §§1–3, Definitions 1 and 5, Theorem 5 and Corollary 6",
    "sourceNote": "Editorial derivation from the linked premises. Retains arbitrary finite rank, including a stated rank-zero convention. The Gram determinant measures volume in the span, not d-dimensional volume for r<d.",
    "provenanceKind": "derived",
    "statement": "The point carrier forms an abelian group under its restricted operations.",
    "formalStatement": "0∈Λ; x,y∈Λ⇒x+y∈Λ ∧ −x∈Λ; (x+y)+z=x+(y+z); x+y=y+x; x+0=0+x=x; x+(−x)=(−x)+x=0.",
    "dependsOn": [
      "urn:csabs:axiom/EuclideanLattice-integer-span"
    ],
    "proofSketch": "Use zero coefficients, coefficient addition and coefficient negation to show closure. The remaining equations are the real-vector additive group equations restricted to Λ.",
    "appliesTo": [
      "urn:csabs:concept/EuclideanLattice"
    ],
    "assumptions": [
      "Finite d,r∈ℕ with r≤d; B has r real-linearly independent columns. Vectors use coordinatewise equality in ℝ^d; lattice equality is equality of point sets, not basis matrices. Use exact real arithmetic and the Euclidean norm, with no overflow or rounding. Rank r may be below ambient dimension d. If r=0, Λ={0}, the coefficient tuple is empty, and intrinsic covolume is 1 by the empty determinant convention. Λ is closed under integer scaling, generally not under real scaling. Computational inputs need a chosen finite rational/integer representation or an explicit real-arithmetic model."
    ],
    "ruleRole": "derived-result",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial statement and derivation; not machine-checked."
  },
  {
    "id": "urn:csabs:theorem/EuclideanLattice-bounded-finiteness",
    "type": "Theorem",
    "name": "bounded-finiteness",
    "source": [
      "urn:csabs:source/peikert-lattice-survey-2016",
      "urn:csabs:source/regev-lattice-introduction-2004"
    ],
    "sourceLocator": "Peikert §2.2.1; Regev Introduction §§1–3, Definitions 1 and 5, Theorem 5 and Corollary 6",
    "sourceNote": "Editorial derivation from the linked premises. Retains arbitrary finite rank, including a stated rank-zero convention. The Gram determinant measures volume in the span, not d-dimensional volume for r<d.",
    "provenanceKind": "derived",
    "statement": "Every bounded ball contains only finitely many lattice points.",
    "formalStatement": "∀t∈ℝ^d, R≥0, {v∈Λ | ‖v−t‖₂≤R} is finite; Λ is discrete.",
    "dependsOn": [
      "urn:csabs:axiom/EuclideanLattice-integer-span",
      "urn:csabs:axiom/EuclideanLattice-metric-volume"
    ],
    "proofSketch": "For r>0 an injective linear map B between finite-dimensional Euclidean spaces has a constant c>0 with ‖Bz‖₂≥c‖z‖₂. A radius-R ball about t bounds ‖Bz‖₂ by R+‖t‖₂ and hence bounds every integer coordinate of z, leaving finitely many possibilities. At r=0 the carrier has one point. Local isolation follows from this finiteness, or the same positive lower bound.",
    "appliesTo": [
      "urn:csabs:concept/EuclideanLattice"
    ],
    "assumptions": [
      "Finite d,r∈ℕ with r≤d; B has r real-linearly independent columns. Vectors use coordinatewise equality in ℝ^d; lattice equality is equality of point sets, not basis matrices. Use exact real arithmetic and the Euclidean norm, with no overflow or rounding. Rank r may be below ambient dimension d. If r=0, Λ={0}, the coefficient tuple is empty, and intrinsic covolume is 1 by the empty determinant convention. Λ is closed under integer scaling, generally not under real scaling. Computational inputs need a chosen finite rational/integer representation or an explicit real-arithmetic model."
    ],
    "ruleRole": "derived-result",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial statement and derivation; not machine-checked."
  },
  {
    "id": "urn:csabs:theorem/EuclideanLattice-unimodular-invariance",
    "type": "Theorem",
    "name": "unimodular-invariance",
    "source": [
      "urn:csabs:source/peikert-lattice-survey-2016",
      "urn:csabs:source/regev-lattice-introduction-2004"
    ],
    "sourceLocator": "Peikert §2.2.1; Regev Introduction §§1–3, Definitions 1 and 5, Theorem 5 and Corollary 6",
    "sourceNote": "Editorial derivation from the linked premises. Retains arbitrary finite rank, including a stated rank-zero convention. The Gram determinant measures volume in the span, not d-dimensional volume for r<d.",
    "provenanceKind": "derived",
    "statement": "A unimodular integer change of basis preserves the lattice and covolume.",
    "formalStatement": "U∈ℤ^{r×r}, det U=±1 ⇒ Λ(BU)=Λ(B) ∧ covol(BU)=covol(B).",
    "dependsOn": [
      "urn:csabs:axiom/EuclideanLattice-integer-span",
      "urn:csabs:axiom/EuclideanLattice-metric-volume"
    ],
    "proofSketch": "The adjugate formula makes U inverse integral, so Uℤ^r=ℤ^r. For the Gram matrix, det(UᵀBᵀBU)=det(U)²det(BᵀB); take the nonnegative square root. The empty-matrix case has determinant 1.",
    "appliesTo": [
      "urn:csabs:concept/EuclideanLattice"
    ],
    "assumptions": [
      "Finite d,r∈ℕ with r≤d; B has r real-linearly independent columns. Vectors use coordinatewise equality in ℝ^d; lattice equality is equality of point sets, not basis matrices. Use exact real arithmetic and the Euclidean norm, with no overflow or rounding. Rank r may be below ambient dimension d. If r=0, Λ={0}, the coefficient tuple is empty, and intrinsic covolume is 1 by the empty determinant convention. Λ is closed under integer scaling, generally not under real scaling. Computational inputs need a chosen finite rational/integer representation or an explicit real-arithmetic model."
    ],
    "ruleRole": "derived-result",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial statement and derivation; not machine-checked."
  }
]
```
<!-- graph-record:end -->
