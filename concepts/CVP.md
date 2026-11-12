# Closest vector problem (Euclidean search relation)

The search problem of finding a lattice point closest to an arbitrary target, with an explicit multiplicative approximation variant.

**Notation:** dist(t,Λ)=min_{v∈Λ}‖t−v‖₂; Sol_γ(B,t)={v∈Λ | ‖t−v‖₂≤γdist(t,Λ)}.

**Stable ID:** `urn:csabs:concept/CVP`

**Categories:** Cryptography → Public-key cryptography → Lattice-based cryptography

**Kind:** semantic-model

**Prerequisites:** [Euclidean lattice (discrete integer-span lattice)](EuclideanLattice.md)

**Related concepts:** [Shortest vector problem (Euclidean search relation)](SVP.md)

## Backlinks

- [Learning with errors (finite modular distribution profile)](LWE.md) — `relatedConcept`
- [Shortest vector problem (Euclidean search relation)](SVP.md) — `relatedConcept`

## Mathematical formulation

For lattice L, target t∈ℝ^d and γ≥1, admissible(v) ⇔ v∈L ∧ ∀w∈L,‖t−v‖²≤γ²‖t−w‖². Ties and rank zero are allowed; the relation does not supply a closest-point algorithm.

**Lean formulation** (in its source module context):

```lean
structure CVP (d r : Nat) where
  lattice : EuclideanLattice d r
  target : Fin d → ℝ
  factor : ℝ
  factor_valid : 1 ≤ factor
```

**Source:** [`Catalog.CVP`](../lean/Catalog/GeometricLattices.lean); consulted 2026-11-12.

**Scope:** partial

**Interpretation:** EuclideanLattice, target and gamma>=1; admissible uses squared Euclidean residuals against every lattice competitor; permits ties and rank zero.

**Limits:** No distance/minimizer construction, relation-equivalence or attainment witness, solver or finite bit encoding. Correspondence of the all-competitor relation to the minimum-distance formulation remains unproved.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Minimum distance to the point set and a set-valued approximation-bounded search relation.

**basisKind:** defined-structure

**basisScope:** B is a EuclideanLattice basis of rank 0≤r≤d, t∈ℝ^d and γ≥1. The target may lie outside the real span when r<d. Use exact Euclidean distance and point equality. Rank zero is valid with unique lattice point 0. γ=1 is exact CVP. Nearest points may tie; no tie-breaking or unique decoder is specified. If t∈Λ, distance is zero and every finite-factor solution equals t. Computational complexity requires finitely encoded bases and targets; arbitrary exact reals are only a mathematical model.

**verificationObligation:** Map exact carriers, equality, matrix orientation, norm, parameter ranges, randomness and error behavior before software use. Complexity statements require finite input encodings. Problem definitions and algebraic correctness do not establish hardness or security.

**reviewStatus:** Editorial mathematics; no compiled claim witness or cryptographic hardness proof.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-CVP-distance"></a>

### distance

`urn:csabs:operation/CVP-distance`

**source:** [Oded Regev: Lattices in Computer Science, Introduction (Fall 2004 lecture notes)](https://cims.nyu.edu/~regev/teaching/lattices_fall_2004/ln/introduction.pdf); accessedOn: 2026-11-11; sourceRole: author course notes with definitions and proofs; [Chris Peikert: A Decade of Lattice Cryptography (2016-02-17 author manuscript)](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf); accessedOn: 2026-11-11; sourceRole: author survey and mathematical definitions

**sourceLocator:** Regev Introduction §4, search CVP_γ; Peikert §2.2.2, discussion preceding Definition 2.2.5

**sourceNote:** Extends the finitely encoded source formulation to a real geometric relation, explicitly separating exact-real semantics from algorithms. Uniqueness needs an additional bounded-distance promise.

**provenanceKind:** adapted

**signature:** distance : Basis(d,r)×ℝ^d → ℝ_{≥0}

**description:** Specify the exact minimum distance to the lattice.

**precondition:** Valid B and target t.

**postcondition:** Return min{‖t−v‖₂ | v∈Λ(B)}.

**totality:** Total as a mathematical specification on the stated domain; no efficient algorithm or exact-real decision procedure is asserted.

<a id="node-urn-csabs-operation-CVP-solution"></a>

### solution

`urn:csabs:operation/CVP-solution`

**source:** [Oded Regev: Lattices in Computer Science, Introduction (Fall 2004 lecture notes)](https://cims.nyu.edu/~regev/teaching/lattices_fall_2004/ln/introduction.pdf); accessedOn: 2026-11-11; sourceRole: author course notes with definitions and proofs; [Chris Peikert: A Decade of Lattice Cryptography (2016-02-17 author manuscript)](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf); accessedOn: 2026-11-11; sourceRole: author survey and mathematical definitions

**sourceLocator:** Regev Introduction §4, search CVP_γ; Peikert §2.2.2, discussion preceding Definition 2.2.5

**sourceNote:** Extends the finitely encoded source formulation to a real geometric relation, explicitly separating exact-real semantics from algorithms. Uniqueness needs an additional bounded-distance promise.

**provenanceKind:** adapted

**signature:** solution : Basis(d,r)×ℝ^d×[1,∞)×ℝ^d → Prop

**description:** Specify admissible closest-vector outputs.

**precondition:** Valid B,t,γ and candidate v.

**postcondition:** True iff v∈Λ(B) and ‖t−v‖₂≤γdist(t,Λ(B)). The predicate is a mathematical specification, not an efficient optimality test.

**totality:** Total as a mathematical specification on the stated domain; no efficient algorithm or exact-real decision procedure is asserted.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-CVP-distance"></a>

### distance

`urn:csabs:axiom/CVP-distance`

**source:** [Oded Regev: Lattices in Computer Science, Introduction (Fall 2004 lecture notes)](https://cims.nyu.edu/~regev/teaching/lattices_fall_2004/ln/introduction.pdf); accessedOn: 2026-11-11; sourceRole: author course notes with definitions and proofs; [Chris Peikert: A Decade of Lattice Cryptography (2016-02-17 author manuscript)](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf); accessedOn: 2026-11-11; sourceRole: author survey and mathematical definitions

**sourceLocator:** Regev Introduction §4, search CVP_γ; Peikert §2.2.2, discussion preceding Definition 2.2.5

**sourceNote:** Extends the finitely encoded source formulation to a real geometric relation, explicitly separating exact-real semantics from algorithms. Uniqueness needs an additional bounded-distance promise.

**provenanceKind:** adapted

**statement:** Distance is the minimum Euclidean distance over all lattice points.

**formalStatement:** dist(t,Λ)=min_{v∈Λ}‖t−v‖₂.

**assumptions:** B is a EuclideanLattice basis of rank 0≤r≤d, t∈ℝ^d and γ≥1. The target may lie outside the real span when r<d. Use exact Euclidean distance and point equality. Rank zero is valid with unique lattice point 0. γ=1 is exact CVP. Nearest points may tie; no tie-breaking or unique decoder is specified. If t∈Λ, distance is zero and every finite-factor solution equals t. Computational complexity requires finitely encoded bases and targets; arbitrary exact reals are only a mathematical model.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial statement and derivation; not machine-checked.

<a id="node-urn-csabs-axiom-CVP-relation"></a>

### relation

`urn:csabs:axiom/CVP-relation`

**source:** [Oded Regev: Lattices in Computer Science, Introduction (Fall 2004 lecture notes)](https://cims.nyu.edu/~regev/teaching/lattices_fall_2004/ln/introduction.pdf); accessedOn: 2026-11-11; sourceRole: author course notes with definitions and proofs; [Chris Peikert: A Decade of Lattice Cryptography (2016-02-17 author manuscript)](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf); accessedOn: 2026-11-11; sourceRole: author survey and mathematical definitions

**sourceLocator:** Regev Introduction §4, search CVP_γ; Peikert §2.2.2, discussion preceding Definition 2.2.5

**sourceNote:** Extends the finitely encoded source formulation to a real geometric relation, explicitly separating exact-real semantics from algorithms. Uniqueness needs an additional bounded-distance promise.

**provenanceKind:** adapted

**statement:** A solution satisfies lattice membership and the approximation bound.

**formalStatement:** v∈Sol_γ(B,t) ⇔ v∈Λ(B) ∧ ‖t−v‖₂≤γdist(t,Λ(B)); γ≥1.

**assumptions:** B is a EuclideanLattice basis of rank 0≤r≤d, t∈ℝ^d and γ≥1. The target may lie outside the real span when r<d. Use exact Euclidean distance and point equality. Rank zero is valid with unique lattice point 0. γ=1 is exact CVP. Nearest points may tie; no tie-breaking or unique decoder is specified. If t∈Λ, distance is zero and every finite-factor solution equals t. Computational complexity requires finitely encoded bases and targets; arbitrary exact reals are only a mathematical model.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial statement and derivation; not machine-checked.

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-CVP-attainment"></a>

### attainment

`urn:csabs:theorem/CVP-attainment`

**source:** [Oded Regev: Lattices in Computer Science, Introduction (Fall 2004 lecture notes)](https://cims.nyu.edu/~regev/teaching/lattices_fall_2004/ln/introduction.pdf); accessedOn: 2026-11-11; sourceRole: author course notes with definitions and proofs; [Chris Peikert: A Decade of Lattice Cryptography (2016-02-17 author manuscript)](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf); accessedOn: 2026-11-11; sourceRole: author survey and mathematical definitions

**sourceLocator:** Regev Introduction §4, search CVP_γ; Peikert §2.2.2, discussion preceding Definition 2.2.5

**sourceNote:** Editorial derivation from the linked premises. Extends the finitely encoded source formulation to a real geometric relation, explicitly separating exact-real semantics from algorithms. Uniqueness needs an additional bounded-distance promise.

**provenanceKind:** derived

**statement:** Every target has at least one closest lattice point.

**formalStatement:** ∀t∈ℝ^d, ∃v∈Λ, ‖t−v‖₂=dist(t,Λ); Sol_γ(B,t)≠∅.

**dependsOn:** [distance](CVP.md#node-urn-csabs-axiom-CVP-distance); [relation](CVP.md#node-urn-csabs-axiom-CVP-relation); [additive-subgroup](EuclideanLattice.md#node-urn-csabs-theorem-EuclideanLattice-additive-subgroup); [bounded-finiteness](EuclideanLattice.md#node-urn-csabs-theorem-EuclideanLattice-bounded-finiteness)

**proofSketch:** Zero belongs to Λ, so restrict to points with distance at most ‖t‖₂. That set is finite and nonempty by bounded finiteness. A point minimizing distance there is globally closest; γ≥1 admits it.

**assumptions:** B is a EuclideanLattice basis of rank 0≤r≤d, t∈ℝ^d and γ≥1. The target may lie outside the real span when r<d. Use exact Euclidean distance and point equality. Rank zero is valid with unique lattice point 0. γ=1 is exact CVP. Nearest points may tie; no tie-breaking or unique decoder is specified. If t∈Λ, distance is zero and every finite-factor solution equals t. Computational complexity requires finitely encoded bases and targets; arbitrary exact reals are only a mathematical model.

**ruleRole:** derived-result

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial statement and derivation; not machine-checked.

<a id="node-urn-csabs-theorem-CVP-translation"></a>

### translation

`urn:csabs:theorem/CVP-translation`

**source:** [Oded Regev: Lattices in Computer Science, Introduction (Fall 2004 lecture notes)](https://cims.nyu.edu/~regev/teaching/lattices_fall_2004/ln/introduction.pdf); accessedOn: 2026-11-11; sourceRole: author course notes with definitions and proofs; [Chris Peikert: A Decade of Lattice Cryptography (2016-02-17 author manuscript)](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf); accessedOn: 2026-11-11; sourceRole: author survey and mathematical definitions

**sourceLocator:** Regev Introduction §4, search CVP_γ; Peikert §2.2.2, discussion preceding Definition 2.2.5

**sourceNote:** Editorial derivation from the linked premises. Extends the finitely encoded source formulation to a real geometric relation, explicitly separating exact-real semantics from algorithms. Uniqueness needs an additional bounded-distance promise.

**provenanceKind:** derived

**statement:** Translating a target by a lattice vector translates its solution set.

**formalStatement:** u∈Λ ⇒ dist(t+u,Λ)=dist(t,Λ) ∧ Sol_γ(B,t+u)={v+u | v∈Sol_γ(B,t)}.

**dependsOn:** [distance](CVP.md#node-urn-csabs-axiom-CVP-distance); [relation](CVP.md#node-urn-csabs-axiom-CVP-relation); [additive-subgroup](EuclideanLattice.md#node-urn-csabs-theorem-EuclideanLattice-additive-subgroup)

**proofSketch:** v↦v+u is a bijection on Λ, with inverse w↦w−u. The difference (t+u)−(v+u)=t−v preserves distances and both search inequalities.

**assumptions:** B is a EuclideanLattice basis of rank 0≤r≤d, t∈ℝ^d and γ≥1. The target may lie outside the real span when r<d. Use exact Euclidean distance and point equality. Rank zero is valid with unique lattice point 0. γ=1 is exact CVP. Nearest points may tie; no tie-breaking or unique decoder is specified. If t∈Λ, distance is zero and every finite-factor solution equals t. Computational complexity requires finitely encoded bases and targets; arbitrary exact reals are only a mathematical model.

**ruleRole:** derived-result

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial statement and derivation; not machine-checked.

## Concept provenance

- [Oded Regev: Lattices in Computer Science, Introduction (Fall 2004 lecture notes)](https://cims.nyu.edu/~regev/teaching/lattices_fall_2004/ln/introduction.pdf); accessedOn: 2026-11-11; sourceRole: author course notes with definitions and proofs
- [Chris Peikert: A Decade of Lattice Cryptography (2016-02-17 author manuscript)](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf); accessedOn: 2026-11-11; sourceRole: author survey and mathematical definitions

**sourceLocator:** Regev Introduction §4, search CVP_γ; Peikert §2.2.2, discussion preceding Definition 2.2.5

**sourceNote:** Extends the finitely encoded source formulation to a real geometric relation, explicitly separating exact-real semantics from algorithms. Uniqueness needs an additional bounded-distance promise.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/CVP",
    "type": "Concept",
    "shortForm": "CVP",
    "fullName": "Closest vector problem (Euclidean search relation)",
    "definition": "The search problem of finding a lattice point closest to an arbitrary target, with an explicit multiplicative approximation variant.",
    "notation": "dist(t,Λ)=min_{v∈Λ}‖t−v‖₂; Sol_γ(B,t)={v∈Λ | ‖t−v‖₂≤γdist(t,Λ)}.",
    "category": [
      "urn:csabs:category/lattice-cryptography"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "requiresConcept": [
      "urn:csabs:concept/EuclideanLattice"
    ],
    "axiomBasis": "Minimum distance to the point set and a set-valued approximation-bounded search relation.",
    "basisKind": "defined-structure",
    "basisScope": "B is a EuclideanLattice basis of rank 0≤r≤d, t∈ℝ^d and γ≥1. The target may lie outside the real span when r<d. Use exact Euclidean distance and point equality. Rank zero is valid with unique lattice point 0. γ=1 is exact CVP. Nearest points may tie; no tie-breaking or unique decoder is specified. If t∈Λ, distance is zero and every finite-factor solution equals t. Computational complexity requires finitely encoded bases and targets; arbitrary exact reals are only a mathematical model.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial mathematics; no compiled claim witness or cryptographic hardness proof.",
    "verificationObligation": [
      "Map exact carriers, equality, matrix orientation, norm, parameter ranges, randomness and error behavior before software use. Complexity statements require finite input encodings. Problem definitions and algebraic correctness do not establish hardness or security."
    ],
    "source": [
      "urn:csabs:source/regev-lattice-introduction-2004",
      "urn:csabs:source/peikert-lattice-survey-2016"
    ],
    "sourceLocator": "Regev Introduction §4, search CVP_γ; Peikert §2.2.2, discussion preceding Definition 2.2.5",
    "sourceNote": "Extends the finitely encoded source formulation to a real geometric relation, explicitly separating exact-real semantics from algorithms. Uniqueness needs an additional bounded-distance promise.",
    "provenanceKind": "adapted",
    "relatedConcept": [
      "urn:csabs:concept/SVP"
    ],
    "hasOperation": [
      "urn:csabs:operation/CVP-distance",
      "urn:csabs:operation/CVP-solution"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/CVP-distance",
      "urn:csabs:axiom/CVP-relation"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/CVP-attainment",
      "urn:csabs:theorem/CVP-translation"
    ],
    "hasLaw": [],
    "leanFormulation": "structure CVP (d r : Nat) where\n  lattice : EuclideanLattice d r\n  target : Fin d → ℝ\n  factor : ℝ\n  factor_valid : 1 ≤ factor",
    "formulationSource": "urn:csabs:source/local-lean-GeometricLattices",
    "formulationLocator": "Catalog.CVP",
    "formulationScope": "partial",
    "leanModelMapping": "EuclideanLattice, target and gamma>=1; admissible uses squared Euclidean residuals against every lattice competitor; permits ties and rank zero.",
    "leanModelLimitations": "No distance/minimizer construction, relation-equivalence or attainment witness, solver or finite bit encoding. Correspondence of the all-competitor relation to the minimum-distance formulation remains unproved.",
    "mathematicalFormulation": "For lattice L, target t∈ℝ^d and γ≥1, admissible(v) ⇔ v∈L ∧ ∀w∈L,‖t−v‖²≤γ²‖t−w‖². Ties and rank zero are allowed; the relation does not supply a closest-point algorithm."
  },
  {
    "id": "urn:csabs:operation/CVP-distance",
    "type": "Operation",
    "name": "distance",
    "source": [
      "urn:csabs:source/regev-lattice-introduction-2004",
      "urn:csabs:source/peikert-lattice-survey-2016"
    ],
    "sourceLocator": "Regev Introduction §4, search CVP_γ; Peikert §2.2.2, discussion preceding Definition 2.2.5",
    "sourceNote": "Extends the finitely encoded source formulation to a real geometric relation, explicitly separating exact-real semantics from algorithms. Uniqueness needs an additional bounded-distance promise.",
    "provenanceKind": "adapted",
    "signature": "distance : Basis(d,r)×ℝ^d → ℝ_{≥0}",
    "description": "Specify the exact minimum distance to the lattice.",
    "precondition": "Valid B and target t.",
    "postcondition": "Return min{‖t−v‖₂ | v∈Λ(B)}.",
    "concept": "urn:csabs:concept/CVP",
    "totality": "Total as a mathematical specification on the stated domain; no efficient algorithm or exact-real decision procedure is asserted."
  },
  {
    "id": "urn:csabs:operation/CVP-solution",
    "type": "Operation",
    "name": "solution",
    "source": [
      "urn:csabs:source/regev-lattice-introduction-2004",
      "urn:csabs:source/peikert-lattice-survey-2016"
    ],
    "sourceLocator": "Regev Introduction §4, search CVP_γ; Peikert §2.2.2, discussion preceding Definition 2.2.5",
    "sourceNote": "Extends the finitely encoded source formulation to a real geometric relation, explicitly separating exact-real semantics from algorithms. Uniqueness needs an additional bounded-distance promise.",
    "provenanceKind": "adapted",
    "signature": "solution : Basis(d,r)×ℝ^d×[1,∞)×ℝ^d → Prop",
    "description": "Specify admissible closest-vector outputs.",
    "precondition": "Valid B,t,γ and candidate v.",
    "postcondition": "True iff v∈Λ(B) and ‖t−v‖₂≤γdist(t,Λ(B)). The predicate is a mathematical specification, not an efficient optimality test.",
    "concept": "urn:csabs:concept/CVP",
    "totality": "Total as a mathematical specification on the stated domain; no efficient algorithm or exact-real decision procedure is asserted."
  },
  {
    "id": "urn:csabs:axiom/CVP-distance",
    "type": "Axiom",
    "name": "distance",
    "source": [
      "urn:csabs:source/regev-lattice-introduction-2004",
      "urn:csabs:source/peikert-lattice-survey-2016"
    ],
    "sourceLocator": "Regev Introduction §4, search CVP_γ; Peikert §2.2.2, discussion preceding Definition 2.2.5",
    "sourceNote": "Extends the finitely encoded source formulation to a real geometric relation, explicitly separating exact-real semantics from algorithms. Uniqueness needs an additional bounded-distance promise.",
    "provenanceKind": "adapted",
    "statement": "Distance is the minimum Euclidean distance over all lattice points.",
    "formalStatement": "dist(t,Λ)=min_{v∈Λ}‖t−v‖₂.",
    "appliesTo": [
      "urn:csabs:concept/CVP"
    ],
    "assumptions": [
      "B is a EuclideanLattice basis of rank 0≤r≤d, t∈ℝ^d and γ≥1. The target may lie outside the real span when r<d. Use exact Euclidean distance and point equality. Rank zero is valid with unique lattice point 0. γ=1 is exact CVP. Nearest points may tie; no tie-breaking or unique decoder is specified. If t∈Λ, distance is zero and every finite-factor solution equals t. Computational complexity requires finitely encoded bases and targets; arbitrary exact reals are only a mathematical model."
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial statement and derivation; not machine-checked."
  },
  {
    "id": "urn:csabs:axiom/CVP-relation",
    "type": "Axiom",
    "name": "relation",
    "source": [
      "urn:csabs:source/regev-lattice-introduction-2004",
      "urn:csabs:source/peikert-lattice-survey-2016"
    ],
    "sourceLocator": "Regev Introduction §4, search CVP_γ; Peikert §2.2.2, discussion preceding Definition 2.2.5",
    "sourceNote": "Extends the finitely encoded source formulation to a real geometric relation, explicitly separating exact-real semantics from algorithms. Uniqueness needs an additional bounded-distance promise.",
    "provenanceKind": "adapted",
    "statement": "A solution satisfies lattice membership and the approximation bound.",
    "formalStatement": "v∈Sol_γ(B,t) ⇔ v∈Λ(B) ∧ ‖t−v‖₂≤γdist(t,Λ(B)); γ≥1.",
    "appliesTo": [
      "urn:csabs:concept/CVP"
    ],
    "assumptions": [
      "B is a EuclideanLattice basis of rank 0≤r≤d, t∈ℝ^d and γ≥1. The target may lie outside the real span when r<d. Use exact Euclidean distance and point equality. Rank zero is valid with unique lattice point 0. γ=1 is exact CVP. Nearest points may tie; no tie-breaking or unique decoder is specified. If t∈Λ, distance is zero and every finite-factor solution equals t. Computational complexity requires finitely encoded bases and targets; arbitrary exact reals are only a mathematical model."
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial statement and derivation; not machine-checked."
  },
  {
    "id": "urn:csabs:theorem/CVP-attainment",
    "type": "Theorem",
    "name": "attainment",
    "source": [
      "urn:csabs:source/regev-lattice-introduction-2004",
      "urn:csabs:source/peikert-lattice-survey-2016"
    ],
    "sourceLocator": "Regev Introduction §4, search CVP_γ; Peikert §2.2.2, discussion preceding Definition 2.2.5",
    "sourceNote": "Editorial derivation from the linked premises. Extends the finitely encoded source formulation to a real geometric relation, explicitly separating exact-real semantics from algorithms. Uniqueness needs an additional bounded-distance promise.",
    "provenanceKind": "derived",
    "statement": "Every target has at least one closest lattice point.",
    "formalStatement": "∀t∈ℝ^d, ∃v∈Λ, ‖t−v‖₂=dist(t,Λ); Sol_γ(B,t)≠∅.",
    "dependsOn": [
      "urn:csabs:axiom/CVP-distance",
      "urn:csabs:axiom/CVP-relation",
      "urn:csabs:theorem/EuclideanLattice-additive-subgroup",
      "urn:csabs:theorem/EuclideanLattice-bounded-finiteness"
    ],
    "proofSketch": "Zero belongs to Λ, so restrict to points with distance at most ‖t‖₂. That set is finite and nonempty by bounded finiteness. A point minimizing distance there is globally closest; γ≥1 admits it.",
    "appliesTo": [
      "urn:csabs:concept/CVP"
    ],
    "assumptions": [
      "B is a EuclideanLattice basis of rank 0≤r≤d, t∈ℝ^d and γ≥1. The target may lie outside the real span when r<d. Use exact Euclidean distance and point equality. Rank zero is valid with unique lattice point 0. γ=1 is exact CVP. Nearest points may tie; no tie-breaking or unique decoder is specified. If t∈Λ, distance is zero and every finite-factor solution equals t. Computational complexity requires finitely encoded bases and targets; arbitrary exact reals are only a mathematical model."
    ],
    "ruleRole": "derived-result",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial statement and derivation; not machine-checked."
  },
  {
    "id": "urn:csabs:theorem/CVP-translation",
    "type": "Theorem",
    "name": "translation",
    "source": [
      "urn:csabs:source/regev-lattice-introduction-2004",
      "urn:csabs:source/peikert-lattice-survey-2016"
    ],
    "sourceLocator": "Regev Introduction §4, search CVP_γ; Peikert §2.2.2, discussion preceding Definition 2.2.5",
    "sourceNote": "Editorial derivation from the linked premises. Extends the finitely encoded source formulation to a real geometric relation, explicitly separating exact-real semantics from algorithms. Uniqueness needs an additional bounded-distance promise.",
    "provenanceKind": "derived",
    "statement": "Translating a target by a lattice vector translates its solution set.",
    "formalStatement": "u∈Λ ⇒ dist(t+u,Λ)=dist(t,Λ) ∧ Sol_γ(B,t+u)={v+u | v∈Sol_γ(B,t)}.",
    "dependsOn": [
      "urn:csabs:axiom/CVP-distance",
      "urn:csabs:axiom/CVP-relation",
      "urn:csabs:theorem/EuclideanLattice-additive-subgroup"
    ],
    "proofSketch": "v↦v+u is a bijection on Λ, with inverse w↦w−u. The difference (t+u)−(v+u)=t−v preserves distances and both search inequalities.",
    "appliesTo": [
      "urn:csabs:concept/CVP"
    ],
    "assumptions": [
      "B is a EuclideanLattice basis of rank 0≤r≤d, t∈ℝ^d and γ≥1. The target may lie outside the real span when r<d. Use exact Euclidean distance and point equality. Rank zero is valid with unique lattice point 0. γ=1 is exact CVP. Nearest points may tie; no tie-breaking or unique decoder is specified. If t∈Λ, distance is zero and every finite-factor solution equals t. Computational complexity requires finitely encoded bases and targets; arbitrary exact reals are only a mathematical model."
    ],
    "ruleRole": "derived-result",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial statement and derivation; not machine-checked."
  }
]
```
<!-- graph-record:end -->
