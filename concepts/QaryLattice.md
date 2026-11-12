# q-ary kernel lattice

The full-rank integer lattice cut out by a homogeneous modular linear system, embedded in real coordinate space.

**Notation:** Λ_q^⊥(A)={z∈ℤ^m | Az=0 mod q}; qℤ^m⊆Λ_q^⊥(A)⊆ℤ^m.

**Stable ID:** `urn:csabs:concept/QaryLattice`

**Categories:** Cryptography → Public-key cryptography → Lattice-based cryptography

**Kind:** Mathematical structure

**Prerequisites:** [Euclidean lattice (discrete integer-span lattice)](EuclideanLattice.md), [Modular Integer](ModularInteger.md)

**Specializes:** [Euclidean lattice (discrete integer-span lattice)](EuclideanLattice.md)

## Backlinks

- [Learning with errors (finite modular distribution profile)](LWE.md) — `relatedConcept`
- [Short integer solution problem (Euclidean norm profile)](SIS.md) — `requiresConcept`

## Mathematical formulation

For A∈(ℤ/qℤ)^{n×m}, n,m>0,q≥2, Λ\_q^⊥(A)={z∈ℤ^m | Az=0 mod q}. The Lean carrier is a modular-kernel presentation; no independent real basis is constructed.

**Lean formulation** (in its source module context):

```lean
structure QaryLattice (n m q : Nat) where
  rows_positive : 0 < n
  columns_positive : 0 < m
  modulus_valid : 2 ≤ q
  matrix : Fin n → Fin m → ZMod q
```

**Source:** [`Catalog.QaryLattice`](../lean/Catalog/GeometricLattices.lean); consulted 2026-11-12.

**Scope:** partial

**Interpretation:** Modular matrix with positive n,m, q>=2 and kernel membership for integer column vectors through ZMod q arithmetic; composite moduli allowed.

**Limits:** No extracted integer/real lattice basis, index theorem, distribution of matrices or registered full-rank witness.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Integer domain, modular syndrome map, and exact zero-syndrome membership.

**basisKind:** defined-structure

**basisScope:** q≥2 is an integer, possibly composite; n,m≥1; A∈(ℤ/qℤ)^{n×m}. Points are integer m-vectors embedded in ℝ^m, with exact coordinate equality and Euclidean norm. Modular arithmetic is in a ring, not necessarily a field. No row-rank or surjectivity assumption on A. A defines a lattice but is not a lattice basis. Cosets Az=u for nonzero u are not this homogeneous lattice.

**specializationNote:** Embed each integer point in ℝ^m and retain ordinary addition, negation and ℓ₂ geometry. The full-rank theorem supplies the discrete-subgroup property. A EuclideanLattice basis B must be an actual integer basis of this kernel, not the modular matrix A.

**verificationObligation:** Map exact carriers, equality, matrix orientation, norm, parameter ranges, randomness and error behavior before software use. Complexity statements require finite input encodings. Problem definitions and algebraic correctness do not establish hardness or security.

**reviewStatus:** Editorial mathematics; no compiled claim witness or cryptographic hardness proof.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-QaryLattice-syndrome"></a>

### syndrome

`urn:csabs:operation/QaryLattice-syndrome`

**source:** [Chris Peikert: A Decade of Lattice Cryptography (2016-02-17 author manuscript)](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf); accessedOn: 2026-11-11; sourceRole: author survey and mathematical definitions

**sourceLocator:** Peikert §4.1.1, equation (4.1.2); §2.2.1

**sourceNote:** Selects the kernel convention Λ_q^⊥, not the image convention sometimes also called a q-ary lattice; allows composite modulus without field-rank formulas.

**provenanceKind:** adapted

**signature:** syndrome_A : ℤ^m → (ℤ/qℤ)^n

**description:** Compute the modular linear image.

**precondition:** A and z have compatible fixed dimensions.

**postcondition:** Return Az with coordinatewise reduction modulo q.

**totality:** Total as a mathematical specification on the stated domain; no efficient algorithm or exact-real decision procedure is asserted.

<a id="node-urn-csabs-operation-QaryLattice-contains"></a>

### contains

`urn:csabs:operation/QaryLattice-contains`

**source:** [Chris Peikert: A Decade of Lattice Cryptography (2016-02-17 author manuscript)](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf); accessedOn: 2026-11-11; sourceRole: author survey and mathematical definitions

**sourceLocator:** Peikert §4.1.1, equation (4.1.2); §2.2.1

**sourceNote:** Selects the kernel convention Λ_q^⊥, not the image convention sometimes also called a q-ary lattice; allows composite modulus without field-rank formulas.

**provenanceKind:** adapted

**signature:** contains_A : ℤ^m → Bool

**description:** Decide integer-vector membership in the modular kernel.

**precondition:** z∈ℤ^m.

**postcondition:** true iff syndrome_A(z)=0.

**totality:** Total as a mathematical specification on the stated domain; no efficient algorithm or exact-real decision procedure is asserted.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-QaryLattice-kernel"></a>

### kernel

`urn:csabs:axiom/QaryLattice-kernel`

**source:** [Chris Peikert: A Decade of Lattice Cryptography (2016-02-17 author manuscript)](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf); accessedOn: 2026-11-11; sourceRole: author survey and mathematical definitions

**sourceLocator:** Peikert §4.1.1, equation (4.1.2); §2.2.1

**sourceNote:** Selects the kernel convention Λ_q^⊥, not the image convention sometimes also called a q-ary lattice; allows composite modulus without field-rank formulas.

**provenanceKind:** adapted

**statement:** The carrier is exactly the integer zero-syndrome set.

**formalStatement:** Λ={z∈ℤ^m | Az=0 in (ℤ/qℤ)^n}; syndrome_A(z)=Az; contains_A(z)⇔Az=0.

**assumptions:** q≥2 is an integer, possibly composite; n,m≥1; A∈(ℤ/qℤ)^{n×m}. Points are integer m-vectors embedded in ℝ^m, with exact coordinate equality and Euclidean norm. Modular arithmetic is in a ring, not necessarily a field. No row-rank or surjectivity assumption on A. A defines a lattice but is not a lattice basis. Cosets Az=u for nonzero u are not this homogeneous lattice.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial statement and derivation; not machine-checked.

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-QaryLattice-full-rank"></a>

### full-rank

`urn:csabs:theorem/QaryLattice-full-rank`

**source:** [Chris Peikert: A Decade of Lattice Cryptography (2016-02-17 author manuscript)](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf); accessedOn: 2026-11-11; sourceRole: author survey and mathematical definitions

**sourceLocator:** Peikert §4.1.1, equation (4.1.2); §2.2.1

**sourceNote:** Editorial derivation from the linked premises. Selects the kernel convention Λ_q^⊥, not the image convention sometimes also called a q-ary lattice; allows composite modulus without field-rank formulas.

**provenanceKind:** derived

**statement:** The modular kernel is a full-rank Euclidean lattice.

**formalStatement:** qℤ^m⊆Λ⊆ℤ^m; Λ is an additive subgroup of ℝ^m, discrete and of rank m.

**dependsOn:** [kernel](QaryLattice.md#node-urn-csabs-axiom-QaryLattice-kernel)

**proofSketch:** Modular linearity closes the kernel under addition and negation; every q-multiple has zero syndrome. Distinct integer vectors have Euclidean distance at least 1, proving discreteness. The m independent vectors qe_i belong to Λ, so its real span is ℝ^m. The basis characterization of discrete subgroups then gives rank m.

**assumptions:** q≥2 is an integer, possibly composite; n,m≥1; A∈(ℤ/qℤ)^{n×m}. Points are integer m-vectors embedded in ℝ^m, with exact coordinate equality and Euclidean norm. Modular arithmetic is in a ring, not necessarily a field. No row-rank or surjectivity assumption on A. A defines a lattice but is not a lattice basis. Cosets Az=u for nonzero u are not this homogeneous lattice.

**ruleRole:** derived-result

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial statement and derivation; not machine-checked.

<a id="node-urn-csabs-theorem-QaryLattice-index"></a>

### index

`urn:csabs:theorem/QaryLattice-index`

**source:** [Chris Peikert: A Decade of Lattice Cryptography (2016-02-17 author manuscript)](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf); accessedOn: 2026-11-11; sourceRole: author survey and mathematical definitions

**sourceLocator:** Peikert §4.1.1, equation (4.1.2); §2.2.1

**sourceNote:** Editorial derivation from the linked premises. Selects the kernel convention Λ_q^⊥, not the image convention sometimes also called a q-ary lattice; allows composite modulus without field-rank formulas.

**provenanceKind:** derived

**statement:** The quotient of the integer lattice by the kernel has size equal to the syndrome image.

**formalStatement:** [ℤ^m:Λ]=|im(syndrome_A)|≤q^n; if syndrome_A is onto, [ℤ^m:Λ]=q^n.

**dependsOn:** [kernel](QaryLattice.md#node-urn-csabs-axiom-QaryLattice-kernel)

**proofSketch:** Two integer vectors have the same syndrome exactly when their difference lies in Λ. Thus cosets correspond bijectively to the image, which is a subset of the q^n possible syndromes.

**assumptions:** q≥2 is an integer, possibly composite; n,m≥1; A∈(ℤ/qℤ)^{n×m}. Points are integer m-vectors embedded in ℝ^m, with exact coordinate equality and Euclidean norm. Modular arithmetic is in a ring, not necessarily a field. No row-rank or surjectivity assumption on A. A defines a lattice but is not a lattice basis. Cosets Az=u for nonzero u are not this homogeneous lattice.

**ruleRole:** derived-result

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial statement and derivation; not machine-checked.

## Concept provenance

- [Chris Peikert: A Decade of Lattice Cryptography (2016-02-17 author manuscript)](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf); accessedOn: 2026-11-11; sourceRole: author survey and mathematical definitions

**sourceLocator:** Peikert §4.1.1, equation (4.1.2); §2.2.1

**sourceNote:** Selects the kernel convention Λ_q^⊥, not the image convention sometimes also called a q-ary lattice; allows composite modulus without field-rank formulas.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/QaryLattice",
    "type": "Concept",
    "shortForm": "QaryLattice",
    "fullName": "q-ary kernel lattice",
    "definition": "The full-rank integer lattice cut out by a homogeneous modular linear system, embedded in real coordinate space.",
    "notation": "Λ_q^⊥(A)={z∈ℤ^m | Az=0 mod q}; qℤ^m⊆Λ_q^⊥(A)⊆ℤ^m.",
    "category": [
      "urn:csabs:category/lattice-cryptography"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "requiresConcept": [
      "urn:csabs:concept/EuclideanLattice",
      "urn:csabs:concept/ModularInteger"
    ],
    "axiomBasis": "Integer domain, modular syndrome map, and exact zero-syndrome membership.",
    "basisKind": "defined-structure",
    "basisScope": "q≥2 is an integer, possibly composite; n,m≥1; A∈(ℤ/qℤ)^{n×m}. Points are integer m-vectors embedded in ℝ^m, with exact coordinate equality and Euclidean norm. Modular arithmetic is in a ring, not necessarily a field. No row-rank or surjectivity assumption on A. A defines a lattice but is not a lattice basis. Cosets Az=u for nonzero u are not this homogeneous lattice.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial mathematics; no compiled claim witness or cryptographic hardness proof.",
    "verificationObligation": [
      "Map exact carriers, equality, matrix orientation, norm, parameter ranges, randomness and error behavior before software use. Complexity statements require finite input encodings. Problem definitions and algebraic correctness do not establish hardness or security."
    ],
    "source": [
      "urn:csabs:source/peikert-lattice-survey-2016"
    ],
    "sourceLocator": "Peikert §4.1.1, equation (4.1.2); §2.2.1",
    "sourceNote": "Selects the kernel convention Λ_q^⊥, not the image convention sometimes also called a q-ary lattice; allows composite modulus without field-rank formulas.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/EuclideanLattice"
    ],
    "specializationNote": "Embed each integer point in ℝ^m and retain ordinary addition, negation and ℓ₂ geometry. The full-rank theorem supplies the discrete-subgroup property. A EuclideanLattice basis B must be an actual integer basis of this kernel, not the modular matrix A.",
    "hasOperation": [
      "urn:csabs:operation/QaryLattice-syndrome",
      "urn:csabs:operation/QaryLattice-contains"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/QaryLattice-kernel"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/QaryLattice-full-rank",
      "urn:csabs:theorem/QaryLattice-index"
    ],
    "hasLaw": [],
    "leanFormulation": "structure QaryLattice (n m q : Nat) where\n  rows_positive : 0 < n\n  columns_positive : 0 < m\n  modulus_valid : 2 ≤ q\n  matrix : Fin n → Fin m → ZMod q",
    "formulationSource": "urn:csabs:source/local-lean-GeometricLattices",
    "formulationLocator": "Catalog.QaryLattice",
    "formulationScope": "partial",
    "leanModelMapping": "Modular matrix with positive n,m, q>=2 and kernel membership for integer column vectors through ZMod q arithmetic; composite moduli allowed.",
    "leanModelLimitations": "No extracted integer/real lattice basis, index theorem, distribution of matrices or registered full-rank witness.",
    "mathematicalFormulation": "For A∈(ℤ/qℤ)^{n×m}, n,m>0,q≥2, Λ_q^⊥(A)={z∈ℤ^m | Az=0 mod q}. The Lean carrier is a modular-kernel presentation; no independent real basis is constructed."
  },
  {
    "id": "urn:csabs:operation/QaryLattice-syndrome",
    "type": "Operation",
    "name": "syndrome",
    "source": [
      "urn:csabs:source/peikert-lattice-survey-2016"
    ],
    "sourceLocator": "Peikert §4.1.1, equation (4.1.2); §2.2.1",
    "sourceNote": "Selects the kernel convention Λ_q^⊥, not the image convention sometimes also called a q-ary lattice; allows composite modulus without field-rank formulas.",
    "provenanceKind": "adapted",
    "signature": "syndrome_A : ℤ^m → (ℤ/qℤ)^n",
    "description": "Compute the modular linear image.",
    "precondition": "A and z have compatible fixed dimensions.",
    "postcondition": "Return Az with coordinatewise reduction modulo q.",
    "concept": "urn:csabs:concept/QaryLattice",
    "totality": "Total as a mathematical specification on the stated domain; no efficient algorithm or exact-real decision procedure is asserted."
  },
  {
    "id": "urn:csabs:operation/QaryLattice-contains",
    "type": "Operation",
    "name": "contains",
    "source": [
      "urn:csabs:source/peikert-lattice-survey-2016"
    ],
    "sourceLocator": "Peikert §4.1.1, equation (4.1.2); §2.2.1",
    "sourceNote": "Selects the kernel convention Λ_q^⊥, not the image convention sometimes also called a q-ary lattice; allows composite modulus without field-rank formulas.",
    "provenanceKind": "adapted",
    "signature": "contains_A : ℤ^m → Bool",
    "description": "Decide integer-vector membership in the modular kernel.",
    "precondition": "z∈ℤ^m.",
    "postcondition": "true iff syndrome_A(z)=0.",
    "concept": "urn:csabs:concept/QaryLattice",
    "totality": "Total as a mathematical specification on the stated domain; no efficient algorithm or exact-real decision procedure is asserted."
  },
  {
    "id": "urn:csabs:axiom/QaryLattice-kernel",
    "type": "Axiom",
    "name": "kernel",
    "source": [
      "urn:csabs:source/peikert-lattice-survey-2016"
    ],
    "sourceLocator": "Peikert §4.1.1, equation (4.1.2); §2.2.1",
    "sourceNote": "Selects the kernel convention Λ_q^⊥, not the image convention sometimes also called a q-ary lattice; allows composite modulus without field-rank formulas.",
    "provenanceKind": "adapted",
    "statement": "The carrier is exactly the integer zero-syndrome set.",
    "formalStatement": "Λ={z∈ℤ^m | Az=0 in (ℤ/qℤ)^n}; syndrome_A(z)=Az; contains_A(z)⇔Az=0.",
    "appliesTo": [
      "urn:csabs:concept/QaryLattice"
    ],
    "assumptions": [
      "q≥2 is an integer, possibly composite; n,m≥1; A∈(ℤ/qℤ)^{n×m}. Points are integer m-vectors embedded in ℝ^m, with exact coordinate equality and Euclidean norm. Modular arithmetic is in a ring, not necessarily a field. No row-rank or surjectivity assumption on A. A defines a lattice but is not a lattice basis. Cosets Az=u for nonzero u are not this homogeneous lattice."
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial statement and derivation; not machine-checked."
  },
  {
    "id": "urn:csabs:theorem/QaryLattice-full-rank",
    "type": "Theorem",
    "name": "full-rank",
    "source": [
      "urn:csabs:source/peikert-lattice-survey-2016"
    ],
    "sourceLocator": "Peikert §4.1.1, equation (4.1.2); §2.2.1",
    "sourceNote": "Editorial derivation from the linked premises. Selects the kernel convention Λ_q^⊥, not the image convention sometimes also called a q-ary lattice; allows composite modulus without field-rank formulas.",
    "provenanceKind": "derived",
    "statement": "The modular kernel is a full-rank Euclidean lattice.",
    "formalStatement": "qℤ^m⊆Λ⊆ℤ^m; Λ is an additive subgroup of ℝ^m, discrete and of rank m.",
    "dependsOn": [
      "urn:csabs:axiom/QaryLattice-kernel"
    ],
    "proofSketch": "Modular linearity closes the kernel under addition and negation; every q-multiple has zero syndrome. Distinct integer vectors have Euclidean distance at least 1, proving discreteness. The m independent vectors qe_i belong to Λ, so its real span is ℝ^m. The basis characterization of discrete subgroups then gives rank m.",
    "appliesTo": [
      "urn:csabs:concept/QaryLattice"
    ],
    "assumptions": [
      "q≥2 is an integer, possibly composite; n,m≥1; A∈(ℤ/qℤ)^{n×m}. Points are integer m-vectors embedded in ℝ^m, with exact coordinate equality and Euclidean norm. Modular arithmetic is in a ring, not necessarily a field. No row-rank or surjectivity assumption on A. A defines a lattice but is not a lattice basis. Cosets Az=u for nonzero u are not this homogeneous lattice."
    ],
    "ruleRole": "derived-result",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial statement and derivation; not machine-checked."
  },
  {
    "id": "urn:csabs:theorem/QaryLattice-index",
    "type": "Theorem",
    "name": "index",
    "source": [
      "urn:csabs:source/peikert-lattice-survey-2016"
    ],
    "sourceLocator": "Peikert §4.1.1, equation (4.1.2); §2.2.1",
    "sourceNote": "Editorial derivation from the linked premises. Selects the kernel convention Λ_q^⊥, not the image convention sometimes also called a q-ary lattice; allows composite modulus without field-rank formulas.",
    "provenanceKind": "derived",
    "statement": "The quotient of the integer lattice by the kernel has size equal to the syndrome image.",
    "formalStatement": "[ℤ^m:Λ]=|im(syndrome_A)|≤q^n; if syndrome_A is onto, [ℤ^m:Λ]=q^n.",
    "dependsOn": [
      "urn:csabs:axiom/QaryLattice-kernel"
    ],
    "proofSketch": "Two integer vectors have the same syndrome exactly when their difference lies in Λ. Thus cosets correspond bijectively to the image, which is a subset of the q^n possible syndromes.",
    "appliesTo": [
      "urn:csabs:concept/QaryLattice"
    ],
    "assumptions": [
      "q≥2 is an integer, possibly composite; n,m≥1; A∈(ℤ/qℤ)^{n×m}. Points are integer m-vectors embedded in ℝ^m, with exact coordinate equality and Euclidean norm. Modular arithmetic is in a ring, not necessarily a field. No row-rank or surjectivity assumption on A. A defines a lattice but is not a lattice basis. Cosets Az=u for nonzero u are not this homogeneous lattice."
    ],
    "ruleRole": "derived-result",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial statement and derivation; not machine-checked."
  }
]
```
<!-- graph-record:end -->
