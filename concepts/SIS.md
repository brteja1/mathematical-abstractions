# Short integer solution problem (Euclidean norm profile)

The average-case modular-kernel search problem of finding a short nonzero integer vector with zero syndrome under a uniformly sampled modular matrix.

**Notation:** A←U((ℤ/qℤ)^{n×m}); find z∈ℤ^m\{0}: Az=0 mod q, ‖z‖₂≤β.

**Stable ID:** `urn:csabs:concept/SIS`

**Categories:** Cryptography → Public-key cryptography → Lattice-based cryptography

**Kind:** semantic-model

**Prerequisites:** [q-ary kernel lattice](QaryLattice.md), [Finitely supported probability distribution](FiniteDistribution.md)

**Related concepts:** [Shortest vector problem (Euclidean search relation)](SVP.md)

## Backlinks

- [Learning with errors (finite modular distribution profile)](LWE.md) — `relatedConcept`
- [Shortest vector problem (Euclidean search relation)](SVP.md) — `relatedConcept`

## Mathematical formulation

For A∈(ℤ/qℤ)^{n×m} with n,m>0,q≥2 and 0<β<q, admissible(z) ⇔ z∈ℤ^m∖{0} ∧ Az=0 mod q ∧ Σ\_i z\_i²≤β². This is the deterministic witness relation, without a random-instance or hardness claim.

**Lean formulation** (in its source module context):

```lean
structure SIS (n m q : Nat) where
  lattice : QaryLattice n m q
  bound : ℝ
  bound_positive : 0 < bound
  bound_nontrivial : bound < q
```

**Source:** [`Catalog.SIS`](../lean/Catalog/GeometricLattices.lean); consulted 2026-11-12.

**Scope:** partial

**Interpretation:** QaryLattice and real bound 0<beta<q; admissible uses a nonzero integer vector, zero syndrome and squared Euclidean bound.

**Limits:** Uniform average-case matrix sampling, collision/pigeonhole witnesses, solvers, success probabilities and hardness assumptions are not formalized.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Uniform modular-instance distribution and a short nonzero kernel-vector relation.

**basisKind:** defined-structure

**basisScope:** n,m≥1, integer q≥2 and real 0<β<q. A is fixed per instance, sampled with independent uniform entries for the average-case experiment. Output z uses integer coordinates, not just residues; z=q e_i would be trivial at β≥q, hence excluded by this profile. Norm is ℓ₂. No dimensional or bound assumptions guarantee a solution for every instance; the relation may be empty. Solver success probability, computational budget and parameter growth must be specified separately for a hardness assumption.

**verificationObligation:** Map exact carriers, equality, matrix orientation, norm, parameter ranges, randomness and error behavior before software use. Complexity statements require finite input encodings. Problem definitions and algebraic correctness do not establish hardness or security.

**reviewStatus:** Editorial mathematics; no compiled claim witness or cryptographic hardness proof.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-SIS-instance-law"></a>

### instance-law

`urn:csabs:operation/SIS-instance-law`

**source:** [Chris Peikert: A Decade of Lattice Cryptography (2016-02-17 author manuscript)](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf); accessedOn: 2026-11-11; sourceRole: author survey and mathematical definitions

**sourceLocator:** Peikert §4.1.1, Definition 4.1.1, observations after it, equations (4.1.1)–(4.1.2)

**sourceNote:** Selects Euclidean norm and the nontrivial β<q range. SIS is a bounded-length search problem on a q-ary lattice, not exact SVP and not a lattice subtype.

**provenanceKind:** adapted

**signature:** instanceLaw : (n,m,q) → Dist_fin((ℤ/qℤ)^{n×m})

**description:** Specify uniform average-case instances.

**precondition:** n,m≥1 and q≥2.

**postcondition:** Every matrix has probability q^(−nm); all entries are independent and uniform.

**totality:** Total as a mathematical specification on the stated domain; no efficient algorithm or exact-real decision procedure is asserted.

<a id="node-urn-csabs-operation-SIS-solution"></a>

### solution

`urn:csabs:operation/SIS-solution`

**source:** [Chris Peikert: A Decade of Lattice Cryptography (2016-02-17 author manuscript)](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf); accessedOn: 2026-11-11; sourceRole: author survey and mathematical definitions

**sourceLocator:** Peikert §4.1.1, Definition 4.1.1, observations after it, equations (4.1.1)–(4.1.2)

**sourceNote:** Selects Euclidean norm and the nontrivial β<q range. SIS is a bounded-length search problem on a q-ary lattice, not exact SVP and not a lattice subtype.

**provenanceKind:** adapted

**signature:** solution : A×(0,q)×ℤ^m → Bool

**description:** Check the short integer-kernel witness.

**precondition:** A has fixed dimensions and β is represented with an exact comparison model.

**postcondition:** true iff z≠0, Az=0 mod q and Σᵢzᵢ²≤β². An implementation with rational β can use exact squared comparisons.

**totality:** Total as a mathematical specification on the stated domain; no efficient algorithm or exact-real decision procedure is asserted.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-SIS-instance"></a>

### instance

`urn:csabs:axiom/SIS-instance`

**source:** [Chris Peikert: A Decade of Lattice Cryptography (2016-02-17 author manuscript)](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf); accessedOn: 2026-11-11; sourceRole: author survey and mathematical definitions

**sourceLocator:** Peikert §4.1.1, Definition 4.1.1, observations after it, equations (4.1.1)–(4.1.2)

**sourceNote:** Selects Euclidean norm and the nontrivial β<q range. SIS is a bounded-length search problem on a q-ary lattice, not exact SVP and not a lattice subtype.

**provenanceKind:** adapted

**statement:** The matrix distribution is uniform over all modular entries.

**formalStatement:** Pr[A=M]=q^(−nm) for M∈(ℤ/qℤ)^{n×m}.

**assumptions:** n,m≥1, integer q≥2 and real 0<β<q. A is fixed per instance, sampled with independent uniform entries for the average-case experiment. Output z uses integer coordinates, not just residues; z=q e_i would be trivial at β≥q, hence excluded by this profile. Norm is ℓ₂. No dimensional or bound assumptions guarantee a solution for every instance; the relation may be empty. Solver success probability, computational budget and parameter growth must be specified separately for a hardness assumption.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial statement and derivation; not machine-checked.

<a id="node-urn-csabs-axiom-SIS-relation"></a>

### relation

`urn:csabs:axiom/SIS-relation`

**source:** [Chris Peikert: A Decade of Lattice Cryptography (2016-02-17 author manuscript)](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf); accessedOn: 2026-11-11; sourceRole: author survey and mathematical definitions

**sourceLocator:** Peikert §4.1.1, Definition 4.1.1, observations after it, equations (4.1.1)–(4.1.2)

**sourceNote:** Selects Euclidean norm and the nontrivial β<q range. SIS is a bounded-length search problem on a q-ary lattice, not exact SVP and not a lattice subtype.

**provenanceKind:** adapted

**statement:** Admissible outputs are short nonzero integer kernel vectors.

**formalStatement:** SIS(A,β,z) ⇔ z∈ℤ^m ∧ z≠0 ∧ Az=0 mod q ∧ ‖z‖₂≤β; 0<β<q.

**assumptions:** n,m≥1, integer q≥2 and real 0<β<q. A is fixed per instance, sampled with independent uniform entries for the average-case experiment. Output z uses integer coordinates, not just residues; z=q e_i would be trivial at β≥q, hence excluded by this profile. Norm is ℓ₂. No dimensional or bound assumptions guarantee a solution for every instance; the relation may be empty. Solver success probability, computational budget and parameter growth must be specified separately for a hardness assumption.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial statement and derivation; not machine-checked.

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-SIS-collision-witness"></a>

### collision-witness

`urn:csabs:theorem/SIS-collision-witness`

**source:** [Chris Peikert: A Decade of Lattice Cryptography (2016-02-17 author manuscript)](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf); accessedOn: 2026-11-11; sourceRole: author survey and mathematical definitions

**sourceLocator:** Peikert §4.1.1, Definition 4.1.1, observations after it, equations (4.1.1)–(4.1.2)

**sourceNote:** Editorial derivation from the linked premises. Selects Euclidean norm and the nontrivial β<q range. SIS is a bounded-length search problem on a q-ary lattice, not exact SVP and not a lattice subtype.

**provenanceKind:** derived

**statement:** A collision on short binary inputs supplies an SIS witness when the bound permits it.

**formalStatement:** x,y∈{0,1}^m, x≠y, Ax=Ay mod q, √m≤β<q ⇒ SIS(A,β,x−y).

**dependsOn:** [relation](SIS.md#node-urn-csabs-axiom-SIS-relation); [kernel](QaryLattice.md#node-urn-csabs-axiom-QaryLattice-kernel)

**proofSketch:** z=x−y is nonzero, and modular linearity gives Az=0. Each integer coordinate lies in {−1,0,1}, so ‖z‖₂²≤m≤β².

**assumptions:** n,m≥1, integer q≥2 and real 0<β<q. A is fixed per instance, sampled with independent uniform entries for the average-case experiment. Output z uses integer coordinates, not just residues; z=q e_i would be trivial at β≥q, hence excluded by this profile. Norm is ℓ₂. No dimensional or bound assumptions guarantee a solution for every instance; the relation may be empty. Solver success probability, computational budget and parameter growth must be specified separately for a hardness assumption.

**ruleRole:** derived-result

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial statement and derivation; not machine-checked.

<a id="node-urn-csabs-theorem-SIS-binary-pigeonhole"></a>

### binary-pigeonhole

`urn:csabs:theorem/SIS-binary-pigeonhole`

**source:** [Chris Peikert: A Decade of Lattice Cryptography (2016-02-17 author manuscript)](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf); accessedOn: 2026-11-11; sourceRole: author survey and mathematical definitions

**sourceLocator:** Peikert §4.1.1, Definition 4.1.1, observations after it, equations (4.1.1)–(4.1.2)

**sourceNote:** Editorial derivation from the linked premises. Selects Euclidean norm and the nontrivial β<q range. SIS is a bounded-length search problem on a q-ary lattice, not exact SVP and not a lattice subtype.

**provenanceKind:** derived

**statement:** A sufficiently large binary domain guarantees a solution at the corresponding norm bound.

**formalStatement:** 2^m>q^n ∧ √m≤β<q ⇒ ∀A, ∃z, SIS(A,β,z).

**dependsOn:** [collision-witness](SIS.md#node-urn-csabs-theorem-SIS-collision-witness)

**proofSketch:** The map x↦Ax sends 2^m binary inputs to at most q^n syndromes. Pigeonhole yields distinct x,y with equal syndrome; apply collision-witness.

**assumptions:** n,m≥1, integer q≥2 and real 0<β<q. A is fixed per instance, sampled with independent uniform entries for the average-case experiment. Output z uses integer coordinates, not just residues; z=q e_i would be trivial at β≥q, hence excluded by this profile. Norm is ℓ₂. No dimensional or bound assumptions guarantee a solution for every instance; the relation may be empty. Solver success probability, computational budget and parameter growth must be specified separately for a hardness assumption.

**ruleRole:** derived-result

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial statement and derivation; not machine-checked.

## Concept provenance

- [Chris Peikert: A Decade of Lattice Cryptography (2016-02-17 author manuscript)](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf); accessedOn: 2026-11-11; sourceRole: author survey and mathematical definitions

**sourceLocator:** Peikert §4.1.1, Definition 4.1.1, observations after it, equations (4.1.1)–(4.1.2)

**sourceNote:** Selects Euclidean norm and the nontrivial β<q range. SIS is a bounded-length search problem on a q-ary lattice, not exact SVP and not a lattice subtype.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/SIS",
    "type": "Concept",
    "shortForm": "SIS",
    "fullName": "Short integer solution problem (Euclidean norm profile)",
    "definition": "The average-case modular-kernel search problem of finding a short nonzero integer vector with zero syndrome under a uniformly sampled modular matrix.",
    "notation": "A←U((ℤ/qℤ)^{n×m}); find z∈ℤ^m\\{0}: Az=0 mod q, ‖z‖₂≤β.",
    "category": [
      "urn:csabs:category/lattice-cryptography"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "requiresConcept": [
      "urn:csabs:concept/QaryLattice",
      "urn:csabs:concept/FiniteDistribution"
    ],
    "axiomBasis": "Uniform modular-instance distribution and a short nonzero kernel-vector relation.",
    "basisKind": "defined-structure",
    "basisScope": "n,m≥1, integer q≥2 and real 0<β<q. A is fixed per instance, sampled with independent uniform entries for the average-case experiment. Output z uses integer coordinates, not just residues; z=q e_i would be trivial at β≥q, hence excluded by this profile. Norm is ℓ₂. No dimensional or bound assumptions guarantee a solution for every instance; the relation may be empty. Solver success probability, computational budget and parameter growth must be specified separately for a hardness assumption.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial mathematics; no compiled claim witness or cryptographic hardness proof.",
    "verificationObligation": [
      "Map exact carriers, equality, matrix orientation, norm, parameter ranges, randomness and error behavior before software use. Complexity statements require finite input encodings. Problem definitions and algebraic correctness do not establish hardness or security."
    ],
    "source": [
      "urn:csabs:source/peikert-lattice-survey-2016"
    ],
    "sourceLocator": "Peikert §4.1.1, Definition 4.1.1, observations after it, equations (4.1.1)–(4.1.2)",
    "sourceNote": "Selects Euclidean norm and the nontrivial β<q range. SIS is a bounded-length search problem on a q-ary lattice, not exact SVP and not a lattice subtype.",
    "provenanceKind": "adapted",
    "relatedConcept": [
      "urn:csabs:concept/SVP"
    ],
    "hasOperation": [
      "urn:csabs:operation/SIS-instance-law",
      "urn:csabs:operation/SIS-solution"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/SIS-instance",
      "urn:csabs:axiom/SIS-relation"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/SIS-collision-witness",
      "urn:csabs:theorem/SIS-binary-pigeonhole"
    ],
    "hasLaw": [],
    "leanFormulation": "structure SIS (n m q : Nat) where\n  lattice : QaryLattice n m q\n  bound : ℝ\n  bound_positive : 0 < bound\n  bound_nontrivial : bound < q",
    "formulationSource": "urn:csabs:source/local-lean-GeometricLattices",
    "formulationLocator": "Catalog.SIS",
    "formulationScope": "partial",
    "leanModelMapping": "QaryLattice and real bound 0<beta<q; admissible uses a nonzero integer vector, zero syndrome and squared Euclidean bound.",
    "leanModelLimitations": "Uniform average-case matrix sampling, collision/pigeonhole witnesses, solvers, success probabilities and hardness assumptions are not formalized.",
    "mathematicalFormulation": "For A∈(ℤ/qℤ)^{n×m} with n,m>0,q≥2 and 0<β<q, admissible(z) ⇔ z∈ℤ^m∖{0} ∧ Az=0 mod q ∧ Σ_i z_i²≤β². This is the deterministic witness relation, without a random-instance or hardness claim."
  },
  {
    "id": "urn:csabs:operation/SIS-instance-law",
    "type": "Operation",
    "name": "instance-law",
    "source": [
      "urn:csabs:source/peikert-lattice-survey-2016"
    ],
    "sourceLocator": "Peikert §4.1.1, Definition 4.1.1, observations after it, equations (4.1.1)–(4.1.2)",
    "sourceNote": "Selects Euclidean norm and the nontrivial β<q range. SIS is a bounded-length search problem on a q-ary lattice, not exact SVP and not a lattice subtype.",
    "provenanceKind": "adapted",
    "signature": "instanceLaw : (n,m,q) → Dist_fin((ℤ/qℤ)^{n×m})",
    "description": "Specify uniform average-case instances.",
    "precondition": "n,m≥1 and q≥2.",
    "postcondition": "Every matrix has probability q^(−nm); all entries are independent and uniform.",
    "concept": "urn:csabs:concept/SIS",
    "totality": "Total as a mathematical specification on the stated domain; no efficient algorithm or exact-real decision procedure is asserted."
  },
  {
    "id": "urn:csabs:operation/SIS-solution",
    "type": "Operation",
    "name": "solution",
    "source": [
      "urn:csabs:source/peikert-lattice-survey-2016"
    ],
    "sourceLocator": "Peikert §4.1.1, Definition 4.1.1, observations after it, equations (4.1.1)–(4.1.2)",
    "sourceNote": "Selects Euclidean norm and the nontrivial β<q range. SIS is a bounded-length search problem on a q-ary lattice, not exact SVP and not a lattice subtype.",
    "provenanceKind": "adapted",
    "signature": "solution : A×(0,q)×ℤ^m → Bool",
    "description": "Check the short integer-kernel witness.",
    "precondition": "A has fixed dimensions and β is represented with an exact comparison model.",
    "postcondition": "true iff z≠0, Az=0 mod q and Σᵢzᵢ²≤β². An implementation with rational β can use exact squared comparisons.",
    "concept": "urn:csabs:concept/SIS",
    "totality": "Total as a mathematical specification on the stated domain; no efficient algorithm or exact-real decision procedure is asserted."
  },
  {
    "id": "urn:csabs:axiom/SIS-instance",
    "type": "Axiom",
    "name": "instance",
    "source": [
      "urn:csabs:source/peikert-lattice-survey-2016"
    ],
    "sourceLocator": "Peikert §4.1.1, Definition 4.1.1, observations after it, equations (4.1.1)–(4.1.2)",
    "sourceNote": "Selects Euclidean norm and the nontrivial β<q range. SIS is a bounded-length search problem on a q-ary lattice, not exact SVP and not a lattice subtype.",
    "provenanceKind": "adapted",
    "statement": "The matrix distribution is uniform over all modular entries.",
    "formalStatement": "Pr[A=M]=q^(−nm) for M∈(ℤ/qℤ)^{n×m}.",
    "appliesTo": [
      "urn:csabs:concept/SIS"
    ],
    "assumptions": [
      "n,m≥1, integer q≥2 and real 0<β<q. A is fixed per instance, sampled with independent uniform entries for the average-case experiment. Output z uses integer coordinates, not just residues; z=q e_i would be trivial at β≥q, hence excluded by this profile. Norm is ℓ₂. No dimensional or bound assumptions guarantee a solution for every instance; the relation may be empty. Solver success probability, computational budget and parameter growth must be specified separately for a hardness assumption."
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial statement and derivation; not machine-checked."
  },
  {
    "id": "urn:csabs:axiom/SIS-relation",
    "type": "Axiom",
    "name": "relation",
    "source": [
      "urn:csabs:source/peikert-lattice-survey-2016"
    ],
    "sourceLocator": "Peikert §4.1.1, Definition 4.1.1, observations after it, equations (4.1.1)–(4.1.2)",
    "sourceNote": "Selects Euclidean norm and the nontrivial β<q range. SIS is a bounded-length search problem on a q-ary lattice, not exact SVP and not a lattice subtype.",
    "provenanceKind": "adapted",
    "statement": "Admissible outputs are short nonzero integer kernel vectors.",
    "formalStatement": "SIS(A,β,z) ⇔ z∈ℤ^m ∧ z≠0 ∧ Az=0 mod q ∧ ‖z‖₂≤β; 0<β<q.",
    "appliesTo": [
      "urn:csabs:concept/SIS"
    ],
    "assumptions": [
      "n,m≥1, integer q≥2 and real 0<β<q. A is fixed per instance, sampled with independent uniform entries for the average-case experiment. Output z uses integer coordinates, not just residues; z=q e_i would be trivial at β≥q, hence excluded by this profile. Norm is ℓ₂. No dimensional or bound assumptions guarantee a solution for every instance; the relation may be empty. Solver success probability, computational budget and parameter growth must be specified separately for a hardness assumption."
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial statement and derivation; not machine-checked."
  },
  {
    "id": "urn:csabs:theorem/SIS-collision-witness",
    "type": "Theorem",
    "name": "collision-witness",
    "source": [
      "urn:csabs:source/peikert-lattice-survey-2016"
    ],
    "sourceLocator": "Peikert §4.1.1, Definition 4.1.1, observations after it, equations (4.1.1)–(4.1.2)",
    "sourceNote": "Editorial derivation from the linked premises. Selects Euclidean norm and the nontrivial β<q range. SIS is a bounded-length search problem on a q-ary lattice, not exact SVP and not a lattice subtype.",
    "provenanceKind": "derived",
    "statement": "A collision on short binary inputs supplies an SIS witness when the bound permits it.",
    "formalStatement": "x,y∈{0,1}^m, x≠y, Ax=Ay mod q, √m≤β<q ⇒ SIS(A,β,x−y).",
    "dependsOn": [
      "urn:csabs:axiom/SIS-relation",
      "urn:csabs:axiom/QaryLattice-kernel"
    ],
    "proofSketch": "z=x−y is nonzero, and modular linearity gives Az=0. Each integer coordinate lies in {−1,0,1}, so ‖z‖₂²≤m≤β².",
    "appliesTo": [
      "urn:csabs:concept/SIS"
    ],
    "assumptions": [
      "n,m≥1, integer q≥2 and real 0<β<q. A is fixed per instance, sampled with independent uniform entries for the average-case experiment. Output z uses integer coordinates, not just residues; z=q e_i would be trivial at β≥q, hence excluded by this profile. Norm is ℓ₂. No dimensional or bound assumptions guarantee a solution for every instance; the relation may be empty. Solver success probability, computational budget and parameter growth must be specified separately for a hardness assumption."
    ],
    "ruleRole": "derived-result",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial statement and derivation; not machine-checked."
  },
  {
    "id": "urn:csabs:theorem/SIS-binary-pigeonhole",
    "type": "Theorem",
    "name": "binary-pigeonhole",
    "source": [
      "urn:csabs:source/peikert-lattice-survey-2016"
    ],
    "sourceLocator": "Peikert §4.1.1, Definition 4.1.1, observations after it, equations (4.1.1)–(4.1.2)",
    "sourceNote": "Editorial derivation from the linked premises. Selects Euclidean norm and the nontrivial β<q range. SIS is a bounded-length search problem on a q-ary lattice, not exact SVP and not a lattice subtype.",
    "provenanceKind": "derived",
    "statement": "A sufficiently large binary domain guarantees a solution at the corresponding norm bound.",
    "formalStatement": "2^m>q^n ∧ √m≤β<q ⇒ ∀A, ∃z, SIS(A,β,z).",
    "dependsOn": [
      "urn:csabs:theorem/SIS-collision-witness"
    ],
    "proofSketch": "The map x↦Ax sends 2^m binary inputs to at most q^n syndromes. Pigeonhole yields distinct x,y with equal syndrome; apply collision-witness.",
    "appliesTo": [
      "urn:csabs:concept/SIS"
    ],
    "assumptions": [
      "n,m≥1, integer q≥2 and real 0<β<q. A is fixed per instance, sampled with independent uniform entries for the average-case experiment. Output z uses integer coordinates, not just residues; z=q e_i would be trivial at β≥q, hence excluded by this profile. Norm is ℓ₂. No dimensional or bound assumptions guarantee a solution for every instance; the relation may be empty. Solver success probability, computational budget and parameter growth must be specified separately for a hardness assumption."
    ],
    "ruleRole": "derived-result",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial statement and derivation; not machine-checked."
  }
]
```
<!-- graph-record:end -->
