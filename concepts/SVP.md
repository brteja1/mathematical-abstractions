# Shortest vector problem (Euclidean search relation)

The search problem of selecting a nonzero lattice vector of minimum Euclidean length, with an explicit approximation-factor variant.

**Notation:** λ₁(Λ)=min_{v∈Λ\{0}}‖v‖₂; Sol_γ(B)={v∈Λ\{0} | ‖v‖₂≤γλ₁(Λ)}.

**Stable ID:** `urn:csabs:concept/SVP`

**Categories:** Cryptography → Public-key cryptography → Lattice-based cryptography

**Kind:** semantic-model

**Prerequisites:** [Euclidean lattice (discrete integer-span lattice)](EuclideanLattice.md)

**Related concepts:** [Closest vector problem (Euclidean search relation)](CVP.md), [Short integer solution problem (Euclidean norm profile)](SIS.md)

## Backlinks

- [Closest vector problem (Euclidean search relation)](CVP.md) — `relatedConcept`
- [Short integer solution problem (Euclidean norm profile)](SIS.md) — `relatedConcept`

## Mathematical formulation

For positive-rank L⊆ℝ^d and γ≥1, admissible(v) ⇔ v∈L∖{0} ∧ ∀w∈L∖{0},‖v‖²≤γ²‖w‖². γ=1 gives the exact shortest-vector relation; existence and algorithms are separate obligations.

**Lean formulation** (in its source module context):

```lean
structure SVP (d r : Nat) where
  lattice : EuclideanLattice d r
  rank_positive : 0 < r
  factor : ℝ
  factor_valid : 1 ≤ factor
```

**Source:** [`Catalog.SVP`](../lean/Catalog/GeometricLattices.lean); consulted 2026-11-12.

**Scope:** partial

**Interpretation:** Positive-rank EuclideanLattice and gamma>=1; admissible is membership, nonzeroness and the squared Euclidean bound against every nonzero competitor.

**Limits:** No lambda_1 construction, minimizer existence or relation-equivalence witness, solver, finite bit encoding or complexity bound. The all-competitor relation corresponds to the catalog minimum relation using its editorial attainment result, which is not compiled here.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** The nonzero minimum length and the approximation-bounded solution predicate.

**basisKind:** defined-structure

**basisScope:** B is a EuclideanLattice basis with 1≤r≤d; γ∈ℝ, γ≥1. Use exact ℓ₂ norm and point equality. Exclude rank zero because no nonzero vector exists. γ=1 is exact SVP. Multiple shortest vectors, including opposite signs, are allowed. This is a search relation, not a single-valued solver or a decision/promise problem. Complexity interpretations use finitely encoded rational/integer bases and a specified encoding for γ.

**verificationObligation:** Map exact carriers, equality, matrix orientation, norm, parameter ranges, randomness and error behavior before software use. Complexity statements require finite input encodings. Problem definitions and algebraic correctness do not establish hardness or security.

**reviewStatus:** Editorial mathematics; no compiled claim witness or cryptographic hardness proof.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-SVP-minimum"></a>

### minimum

`urn:csabs:operation/SVP-minimum`

**source:** [Chris Peikert: A Decade of Lattice Cryptography (2016-02-17 author manuscript)](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf); accessedOn: 2026-11-11; sourceRole: author survey and mathematical definitions; [Oded Regev: Lattices in Computer Science, Introduction (Fall 2004 lecture notes)](https://cims.nyu.edu/~regev/teaching/lattices_fall_2004/ln/introduction.pdf); accessedOn: 2026-11-11; sourceRole: author course notes with definitions and proofs

**sourceLocator:** Peikert §2.2.2, Definitions 2.2.1–2.2.2; Regev Introduction §3, Claim 7, and §4

**sourceNote:** Selects ℓ₂ search-SVP and its γ variant. GapSVP and SIVP are distinct problems and are not silently identified with this relation.

**provenanceKind:** adapted

**signature:** minimumLength : PositiveRankBasis → ℝ_{>0}

**description:** Specify the shortest nonzero vector length.

**precondition:** r≥1.

**postcondition:** Return λ₁(Λ)=min{‖v‖₂ | v∈Λ, v≠0}.

**totality:** Total as a mathematical specification on the stated domain; no efficient algorithm or exact-real decision procedure is asserted.

<a id="node-urn-csabs-operation-SVP-solution"></a>

### solution

`urn:csabs:operation/SVP-solution`

**source:** [Chris Peikert: A Decade of Lattice Cryptography (2016-02-17 author manuscript)](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf); accessedOn: 2026-11-11; sourceRole: author survey and mathematical definitions; [Oded Regev: Lattices in Computer Science, Introduction (Fall 2004 lecture notes)](https://cims.nyu.edu/~regev/teaching/lattices_fall_2004/ln/introduction.pdf); accessedOn: 2026-11-11; sourceRole: author course notes with definitions and proofs

**sourceLocator:** Peikert §2.2.2, Definitions 2.2.1–2.2.2; Regev Introduction §3, Claim 7, and §4

**sourceNote:** Selects ℓ₂ search-SVP and its γ variant. GapSVP and SIVP are distinct problems and are not silently identified with this relation.

**provenanceKind:** adapted

**signature:** solution : PositiveRankBasis×[1,∞)×ℝ^d → Prop

**description:** Specify whether a candidate is an admissible search output.

**precondition:** Valid B, γ≥1 and a d-dimensional candidate v.

**postcondition:** True iff v∈Λ, v≠0 and ‖v‖₂≤γλ₁(Λ). This mathematical predicate is not an efficient certificate verifier.

**totality:** Total as a mathematical specification on the stated domain; no efficient algorithm or exact-real decision procedure is asserted.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-SVP-minimum"></a>

### minimum

`urn:csabs:axiom/SVP-minimum`

**source:** [Chris Peikert: A Decade of Lattice Cryptography (2016-02-17 author manuscript)](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf); accessedOn: 2026-11-11; sourceRole: author survey and mathematical definitions; [Oded Regev: Lattices in Computer Science, Introduction (Fall 2004 lecture notes)](https://cims.nyu.edu/~regev/teaching/lattices_fall_2004/ln/introduction.pdf); accessedOn: 2026-11-11; sourceRole: author course notes with definitions and proofs

**sourceLocator:** Peikert §2.2.2, Definitions 2.2.1–2.2.2; Regev Introduction §3, Claim 7, and §4

**sourceNote:** Selects ℓ₂ search-SVP and its γ variant. GapSVP and SIVP are distinct problems and are not silently identified with this relation.

**provenanceKind:** adapted

**statement:** λ₁ denotes the minimum nonzero Euclidean length.

**formalStatement:** λ₁(Λ)=min{‖v‖₂ | v∈Λ\{0}}.

**assumptions:** B is a EuclideanLattice basis with 1≤r≤d; γ∈ℝ, γ≥1. Use exact ℓ₂ norm and point equality. Exclude rank zero because no nonzero vector exists. γ=1 is exact SVP. Multiple shortest vectors, including opposite signs, are allowed. This is a search relation, not a single-valued solver or a decision/promise problem. Complexity interpretations use finitely encoded rational/integer bases and a specified encoding for γ.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial statement and derivation; not machine-checked.

<a id="node-urn-csabs-axiom-SVP-relation"></a>

### relation

`urn:csabs:axiom/SVP-relation`

**source:** [Chris Peikert: A Decade of Lattice Cryptography (2016-02-17 author manuscript)](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf); accessedOn: 2026-11-11; sourceRole: author survey and mathematical definitions; [Oded Regev: Lattices in Computer Science, Introduction (Fall 2004 lecture notes)](https://cims.nyu.edu/~regev/teaching/lattices_fall_2004/ln/introduction.pdf); accessedOn: 2026-11-11; sourceRole: author course notes with definitions and proofs

**sourceLocator:** Peikert §2.2.2, Definitions 2.2.1–2.2.2; Regev Introduction §3, Claim 7, and §4

**sourceNote:** Selects ℓ₂ search-SVP and its γ variant. GapSVP and SIVP are distinct problems and are not silently identified with this relation.

**provenanceKind:** adapted

**statement:** Solutions are nonzero lattice points satisfying the chosen approximation bound.

**formalStatement:** v∈Sol_γ(B) ⇔ v∈Λ(B) ∧ v≠0 ∧ ‖v‖₂≤γλ₁(Λ(B)); γ≥1.

**assumptions:** B is a EuclideanLattice basis with 1≤r≤d; γ∈ℝ, γ≥1. Use exact ℓ₂ norm and point equality. Exclude rank zero because no nonzero vector exists. γ=1 is exact SVP. Multiple shortest vectors, including opposite signs, are allowed. This is a search relation, not a single-valued solver or a decision/promise problem. Complexity interpretations use finitely encoded rational/integer bases and a specified encoding for γ.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial statement and derivation; not machine-checked.

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-SVP-attainment"></a>

### attainment

`urn:csabs:theorem/SVP-attainment`

**source:** [Chris Peikert: A Decade of Lattice Cryptography (2016-02-17 author manuscript)](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf); accessedOn: 2026-11-11; sourceRole: author survey and mathematical definitions; [Oded Regev: Lattices in Computer Science, Introduction (Fall 2004 lecture notes)](https://cims.nyu.edu/~regev/teaching/lattices_fall_2004/ln/introduction.pdf); accessedOn: 2026-11-11; sourceRole: author course notes with definitions and proofs

**sourceLocator:** Peikert §2.2.2, Definitions 2.2.1–2.2.2; Regev Introduction §3, Claim 7, and §4

**sourceNote:** Editorial derivation from the linked premises. Selects ℓ₂ search-SVP and its γ variant. GapSVP and SIVP are distinct problems and are not silently identified with this relation.

**provenanceKind:** derived

**statement:** For every permitted basis, the positive minimum is attained and the search relation is nonempty.

**formalStatement:** ∃v∈Λ\{0}, 0<‖v‖₂=λ₁(Λ); Sol_γ(B)≠∅ for γ≥1.

**dependsOn:** [minimum](SVP.md#node-urn-csabs-axiom-SVP-minimum); [relation](SVP.md#node-urn-csabs-axiom-SVP-relation); [integer-span](EuclideanLattice.md#node-urn-csabs-axiom-EuclideanLattice-integer-span); [bounded-finiteness](EuclideanLattice.md#node-urn-csabs-theorem-EuclideanLattice-bounded-finiteness)

**proofSketch:** Choose any nonzero basis column b. The finite nonempty set of nonzero points of norm at most ‖b‖₂ has a least norm, positive by nonzeroness. Any shorter point would also be in that set. An exact minimizer satisfies every γ≥1 bound.

**assumptions:** B is a EuclideanLattice basis with 1≤r≤d; γ∈ℝ, γ≥1. Use exact ℓ₂ norm and point equality. Exclude rank zero because no nonzero vector exists. γ=1 is exact SVP. Multiple shortest vectors, including opposite signs, are allowed. This is a search relation, not a single-valued solver or a decision/promise problem. Complexity interpretations use finitely encoded rational/integer bases and a specified encoding for γ.

**ruleRole:** derived-result

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial statement and derivation; not machine-checked.

<a id="node-urn-csabs-theorem-SVP-approximation-monotonicity"></a>

### approximation-monotonicity

`urn:csabs:theorem/SVP-approximation-monotonicity`

**source:** [Chris Peikert: A Decade of Lattice Cryptography (2016-02-17 author manuscript)](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf); accessedOn: 2026-11-11; sourceRole: author survey and mathematical definitions; [Oded Regev: Lattices in Computer Science, Introduction (Fall 2004 lecture notes)](https://cims.nyu.edu/~regev/teaching/lattices_fall_2004/ln/introduction.pdf); accessedOn: 2026-11-11; sourceRole: author course notes with definitions and proofs

**sourceLocator:** Peikert §2.2.2, Definitions 2.2.1–2.2.2; Regev Introduction §3, Claim 7, and §4

**sourceNote:** Editorial derivation from the linked premises. Selects ℓ₂ search-SVP and its γ variant. GapSVP and SIVP are distinct problems and are not silently identified with this relation.

**provenanceKind:** derived

**statement:** Increasing the approximation factor can only enlarge the solution set.

**formalStatement:** 1≤γ≤δ ⇒ Sol_γ(B)⊆Sol_δ(B).

**dependsOn:** [minimum](SVP.md#node-urn-csabs-axiom-SVP-minimum); [relation](SVP.md#node-urn-csabs-axiom-SVP-relation); [attainment](SVP.md#node-urn-csabs-theorem-SVP-attainment)

**proofSketch:** λ₁ is positive, hence γλ₁≤δλ₁. Membership and nonzeroness do not depend on the approximation factor.

**assumptions:** B is a EuclideanLattice basis with 1≤r≤d; γ∈ℝ, γ≥1. Use exact ℓ₂ norm and point equality. Exclude rank zero because no nonzero vector exists. γ=1 is exact SVP. Multiple shortest vectors, including opposite signs, are allowed. This is a search relation, not a single-valued solver or a decision/promise problem. Complexity interpretations use finitely encoded rational/integer bases and a specified encoding for γ.

**ruleRole:** derived-result

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial statement and derivation; not machine-checked.

## Concept provenance

- [Chris Peikert: A Decade of Lattice Cryptography (2016-02-17 author manuscript)](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf); accessedOn: 2026-11-11; sourceRole: author survey and mathematical definitions
- [Oded Regev: Lattices in Computer Science, Introduction (Fall 2004 lecture notes)](https://cims.nyu.edu/~regev/teaching/lattices_fall_2004/ln/introduction.pdf); accessedOn: 2026-11-11; sourceRole: author course notes with definitions and proofs

**sourceLocator:** Peikert §2.2.2, Definitions 2.2.1–2.2.2; Regev Introduction §3, Claim 7, and §4

**sourceNote:** Selects ℓ₂ search-SVP and its γ variant. GapSVP and SIVP are distinct problems and are not silently identified with this relation.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/SVP",
    "type": "Concept",
    "shortForm": "SVP",
    "fullName": "Shortest vector problem (Euclidean search relation)",
    "definition": "The search problem of selecting a nonzero lattice vector of minimum Euclidean length, with an explicit approximation-factor variant.",
    "notation": "λ₁(Λ)=min_{v∈Λ\\{0}}‖v‖₂; Sol_γ(B)={v∈Λ\\{0} | ‖v‖₂≤γλ₁(Λ)}.",
    "category": [
      "urn:csabs:category/lattice-cryptography"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "requiresConcept": [
      "urn:csabs:concept/EuclideanLattice"
    ],
    "axiomBasis": "The nonzero minimum length and the approximation-bounded solution predicate.",
    "basisKind": "defined-structure",
    "basisScope": "B is a EuclideanLattice basis with 1≤r≤d; γ∈ℝ, γ≥1. Use exact ℓ₂ norm and point equality. Exclude rank zero because no nonzero vector exists. γ=1 is exact SVP. Multiple shortest vectors, including opposite signs, are allowed. This is a search relation, not a single-valued solver or a decision/promise problem. Complexity interpretations use finitely encoded rational/integer bases and a specified encoding for γ.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial mathematics; no compiled claim witness or cryptographic hardness proof.",
    "verificationObligation": [
      "Map exact carriers, equality, matrix orientation, norm, parameter ranges, randomness and error behavior before software use. Complexity statements require finite input encodings. Problem definitions and algebraic correctness do not establish hardness or security."
    ],
    "source": [
      "urn:csabs:source/peikert-lattice-survey-2016",
      "urn:csabs:source/regev-lattice-introduction-2004"
    ],
    "sourceLocator": "Peikert §2.2.2, Definitions 2.2.1–2.2.2; Regev Introduction §3, Claim 7, and §4",
    "sourceNote": "Selects ℓ₂ search-SVP and its γ variant. GapSVP and SIVP are distinct problems and are not silently identified with this relation.",
    "provenanceKind": "adapted",
    "relatedConcept": [
      "urn:csabs:concept/CVP",
      "urn:csabs:concept/SIS"
    ],
    "hasOperation": [
      "urn:csabs:operation/SVP-minimum",
      "urn:csabs:operation/SVP-solution"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/SVP-minimum",
      "urn:csabs:axiom/SVP-relation"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/SVP-attainment",
      "urn:csabs:theorem/SVP-approximation-monotonicity"
    ],
    "hasLaw": [],
    "leanFormulation": "structure SVP (d r : Nat) where\n  lattice : EuclideanLattice d r\n  rank_positive : 0 < r\n  factor : ℝ\n  factor_valid : 1 ≤ factor",
    "formulationSource": "urn:csabs:source/local-lean-GeometricLattices",
    "formulationLocator": "Catalog.SVP",
    "formulationScope": "partial",
    "leanModelMapping": "Positive-rank EuclideanLattice and gamma>=1; admissible is membership, nonzeroness and the squared Euclidean bound against every nonzero competitor.",
    "leanModelLimitations": "No lambda_1 construction, minimizer existence or relation-equivalence witness, solver, finite bit encoding or complexity bound. The all-competitor relation corresponds to the catalog minimum relation using its editorial attainment result, which is not compiled here.",
    "mathematicalFormulation": "For positive-rank L⊆ℝ^d and γ≥1, admissible(v) ⇔ v∈L∖{0} ∧ ∀w∈L∖{0},‖v‖²≤γ²‖w‖². γ=1 gives the exact shortest-vector relation; existence and algorithms are separate obligations."
  },
  {
    "id": "urn:csabs:operation/SVP-minimum",
    "type": "Operation",
    "name": "minimum",
    "source": [
      "urn:csabs:source/peikert-lattice-survey-2016",
      "urn:csabs:source/regev-lattice-introduction-2004"
    ],
    "sourceLocator": "Peikert §2.2.2, Definitions 2.2.1–2.2.2; Regev Introduction §3, Claim 7, and §4",
    "sourceNote": "Selects ℓ₂ search-SVP and its γ variant. GapSVP and SIVP are distinct problems and are not silently identified with this relation.",
    "provenanceKind": "adapted",
    "signature": "minimumLength : PositiveRankBasis → ℝ_{>0}",
    "description": "Specify the shortest nonzero vector length.",
    "precondition": "r≥1.",
    "postcondition": "Return λ₁(Λ)=min{‖v‖₂ | v∈Λ, v≠0}.",
    "concept": "urn:csabs:concept/SVP",
    "totality": "Total as a mathematical specification on the stated domain; no efficient algorithm or exact-real decision procedure is asserted."
  },
  {
    "id": "urn:csabs:operation/SVP-solution",
    "type": "Operation",
    "name": "solution",
    "source": [
      "urn:csabs:source/peikert-lattice-survey-2016",
      "urn:csabs:source/regev-lattice-introduction-2004"
    ],
    "sourceLocator": "Peikert §2.2.2, Definitions 2.2.1–2.2.2; Regev Introduction §3, Claim 7, and §4",
    "sourceNote": "Selects ℓ₂ search-SVP and its γ variant. GapSVP and SIVP are distinct problems and are not silently identified with this relation.",
    "provenanceKind": "adapted",
    "signature": "solution : PositiveRankBasis×[1,∞)×ℝ^d → Prop",
    "description": "Specify whether a candidate is an admissible search output.",
    "precondition": "Valid B, γ≥1 and a d-dimensional candidate v.",
    "postcondition": "True iff v∈Λ, v≠0 and ‖v‖₂≤γλ₁(Λ). This mathematical predicate is not an efficient certificate verifier.",
    "concept": "urn:csabs:concept/SVP",
    "totality": "Total as a mathematical specification on the stated domain; no efficient algorithm or exact-real decision procedure is asserted."
  },
  {
    "id": "urn:csabs:axiom/SVP-minimum",
    "type": "Axiom",
    "name": "minimum",
    "source": [
      "urn:csabs:source/peikert-lattice-survey-2016",
      "urn:csabs:source/regev-lattice-introduction-2004"
    ],
    "sourceLocator": "Peikert §2.2.2, Definitions 2.2.1–2.2.2; Regev Introduction §3, Claim 7, and §4",
    "sourceNote": "Selects ℓ₂ search-SVP and its γ variant. GapSVP and SIVP are distinct problems and are not silently identified with this relation.",
    "provenanceKind": "adapted",
    "statement": "λ₁ denotes the minimum nonzero Euclidean length.",
    "formalStatement": "λ₁(Λ)=min{‖v‖₂ | v∈Λ\\{0}}.",
    "appliesTo": [
      "urn:csabs:concept/SVP"
    ],
    "assumptions": [
      "B is a EuclideanLattice basis with 1≤r≤d; γ∈ℝ, γ≥1. Use exact ℓ₂ norm and point equality. Exclude rank zero because no nonzero vector exists. γ=1 is exact SVP. Multiple shortest vectors, including opposite signs, are allowed. This is a search relation, not a single-valued solver or a decision/promise problem. Complexity interpretations use finitely encoded rational/integer bases and a specified encoding for γ."
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial statement and derivation; not machine-checked."
  },
  {
    "id": "urn:csabs:axiom/SVP-relation",
    "type": "Axiom",
    "name": "relation",
    "source": [
      "urn:csabs:source/peikert-lattice-survey-2016",
      "urn:csabs:source/regev-lattice-introduction-2004"
    ],
    "sourceLocator": "Peikert §2.2.2, Definitions 2.2.1–2.2.2; Regev Introduction §3, Claim 7, and §4",
    "sourceNote": "Selects ℓ₂ search-SVP and its γ variant. GapSVP and SIVP are distinct problems and are not silently identified with this relation.",
    "provenanceKind": "adapted",
    "statement": "Solutions are nonzero lattice points satisfying the chosen approximation bound.",
    "formalStatement": "v∈Sol_γ(B) ⇔ v∈Λ(B) ∧ v≠0 ∧ ‖v‖₂≤γλ₁(Λ(B)); γ≥1.",
    "appliesTo": [
      "urn:csabs:concept/SVP"
    ],
    "assumptions": [
      "B is a EuclideanLattice basis with 1≤r≤d; γ∈ℝ, γ≥1. Use exact ℓ₂ norm and point equality. Exclude rank zero because no nonzero vector exists. γ=1 is exact SVP. Multiple shortest vectors, including opposite signs, are allowed. This is a search relation, not a single-valued solver or a decision/promise problem. Complexity interpretations use finitely encoded rational/integer bases and a specified encoding for γ."
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial statement and derivation; not machine-checked."
  },
  {
    "id": "urn:csabs:theorem/SVP-attainment",
    "type": "Theorem",
    "name": "attainment",
    "source": [
      "urn:csabs:source/peikert-lattice-survey-2016",
      "urn:csabs:source/regev-lattice-introduction-2004"
    ],
    "sourceLocator": "Peikert §2.2.2, Definitions 2.2.1–2.2.2; Regev Introduction §3, Claim 7, and §4",
    "sourceNote": "Editorial derivation from the linked premises. Selects ℓ₂ search-SVP and its γ variant. GapSVP and SIVP are distinct problems and are not silently identified with this relation.",
    "provenanceKind": "derived",
    "statement": "For every permitted basis, the positive minimum is attained and the search relation is nonempty.",
    "formalStatement": "∃v∈Λ\\{0}, 0<‖v‖₂=λ₁(Λ); Sol_γ(B)≠∅ for γ≥1.",
    "dependsOn": [
      "urn:csabs:axiom/SVP-minimum",
      "urn:csabs:axiom/SVP-relation",
      "urn:csabs:axiom/EuclideanLattice-integer-span",
      "urn:csabs:theorem/EuclideanLattice-bounded-finiteness"
    ],
    "proofSketch": "Choose any nonzero basis column b. The finite nonempty set of nonzero points of norm at most ‖b‖₂ has a least norm, positive by nonzeroness. Any shorter point would also be in that set. An exact minimizer satisfies every γ≥1 bound.",
    "appliesTo": [
      "urn:csabs:concept/SVP"
    ],
    "assumptions": [
      "B is a EuclideanLattice basis with 1≤r≤d; γ∈ℝ, γ≥1. Use exact ℓ₂ norm and point equality. Exclude rank zero because no nonzero vector exists. γ=1 is exact SVP. Multiple shortest vectors, including opposite signs, are allowed. This is a search relation, not a single-valued solver or a decision/promise problem. Complexity interpretations use finitely encoded rational/integer bases and a specified encoding for γ."
    ],
    "ruleRole": "derived-result",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial statement and derivation; not machine-checked."
  },
  {
    "id": "urn:csabs:theorem/SVP-approximation-monotonicity",
    "type": "Theorem",
    "name": "approximation-monotonicity",
    "source": [
      "urn:csabs:source/peikert-lattice-survey-2016",
      "urn:csabs:source/regev-lattice-introduction-2004"
    ],
    "sourceLocator": "Peikert §2.2.2, Definitions 2.2.1–2.2.2; Regev Introduction §3, Claim 7, and §4",
    "sourceNote": "Editorial derivation from the linked premises. Selects ℓ₂ search-SVP and its γ variant. GapSVP and SIVP are distinct problems and are not silently identified with this relation.",
    "provenanceKind": "derived",
    "statement": "Increasing the approximation factor can only enlarge the solution set.",
    "formalStatement": "1≤γ≤δ ⇒ Sol_γ(B)⊆Sol_δ(B).",
    "dependsOn": [
      "urn:csabs:axiom/SVP-minimum",
      "urn:csabs:axiom/SVP-relation",
      "urn:csabs:theorem/SVP-attainment"
    ],
    "proofSketch": "λ₁ is positive, hence γλ₁≤δλ₁. Membership and nonzeroness do not depend on the approximation factor.",
    "appliesTo": [
      "urn:csabs:concept/SVP"
    ],
    "assumptions": [
      "B is a EuclideanLattice basis with 1≤r≤d; γ∈ℝ, γ≥1. Use exact ℓ₂ norm and point equality. Exclude rank zero because no nonzero vector exists. γ=1 is exact SVP. Multiple shortest vectors, including opposite signs, are allowed. This is a search relation, not a single-valued solver or a decision/promise problem. Complexity interpretations use finitely encoded rational/integer bases and a specified encoding for γ."
    ],
    "ruleRole": "derived-result",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial statement and derivation; not machine-checked."
  }
]
```
<!-- graph-record:end -->
