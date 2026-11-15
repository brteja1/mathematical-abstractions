# Triangular norm (t-norm)

An associative, commutative, order-monotone binary operation on the real unit interval with neutral element 1; a reusable truth-degree conjunction.

**Notation:** T:I²→I; I=[0,1]; e=1.

**Stable ID:** `urn:csabs:concept/TNorm`

**Categories:** Logic and proof → Fuzzy logic

**Kind:** Mathematical structure

**Prerequisites:** [Exact real number](RealNumber.md), [Total Order](TotalOrder.md)

**Specializes:** [Monoid](Monoid.md)

**Related concepts:** [Triangular conorm (t-conorm)](TConorm.md), [Fuzzy set (unit-interval membership, min/max profile)](FuzzySet.md)

## Backlinks

- [Residuated fuzzy truth-value algebra (left-continuous t-norm profile)](ResiduatedFuzzyLogic.md) — `specializationOf`
- [Triangular conorm (t-conorm)](TConorm.md) — `relatedConcept`

## Mathematical formulation

T:I²→I; I=[0,1]; e=1. I=[0,1]⊂ℝ with ordinary order and exact equality; T:I²→I is total. Continuity and idempotence are not assumed.

**Lean formulation** (in its source module context):

```lean
structure TNorm where
  combine : FuzzyDegree → FuzzyDegree → FuzzyDegree
  commutative : ∀ a b, combine a b = combine b a
  associative : ∀ a b c, combine (combine a b) c = combine a (combine b c)
  monotone : ∀ a b c d, a ≤ b → c ≤ d → combine a c ≤ combine b d
  identity : ∀ a, combine a ⟨1, zero_le_one, le_refl 1⟩ = a
```

**Source:** [`Catalog.TNorm`](../lean/Catalog/FuzzyLogic.lean); consulted 2026-11-15.

**Scope:** model

**Interpretation:** Structure on the bounded real subtype with combine and the four explicit structure laws. Equality is subtype equality, equivalent to real equality.

**Limits:** No instance construction or general t-norm theorem witnesses are registered; min/product/Łukasiewicz are documented examples, not separately proved Lean instances.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Closed real-unit-interval operation with associativity, commutativity, monotonicity and neutral 1. No continuity axiom.

**basisKind:** defined-structure

**basisScope:** The selected exact real profile and listed operations and results; no completeness claim.

**convention:** I=[0,1]⊂ℝ with ordinary order and exact equality; T:I²→I is total. Continuity and idempotence are not assumed.

**specializationNote:** Fix one t-norm T, take monoid carrier I=[0,1], multiplication T and identity 1; ordinary real equality, associativity and neutrality instantiate the monoid interface. Monotonicity and commutativity are additional constraints.

**verificationObligation:** Map equality, carriers, degree bounds and exact arithmetic to the target API. Rounded operations require separate law checks.; Specialization and prerequisites do not transfer claims automatically.

**reviewStatus:** Editorial mathematical review; Lean model coverage is separate from claim proof coverage.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-TNorm-combine"></a>

### combine

`urn:csabs:operation/TNorm-combine`

**signature:** I² → I

**description:** Return T(a,b) in I. Examples: Gödel min(a,b); product ab; Łukasiewicz max(0,a+b−1). Different choices are distinct instances.

**precondition:** Arguments have the displayed types; all degree inputs are in the closed real unit interval.

**postcondition:** Return T(a,b) in I. Examples: Gödel min(a,b); product ab; Łukasiewicz max(0,a+b−1). Different choices are distinct instances.

**totality:** total on the stated typed domain

## Axioms and defining rules

<a id="node-urn-csabs-axiom-TNorm-associativity"></a>

### associativity

`urn:csabs:axiom/TNorm-associativity`

**statement:** Conjunction is associative.

**description:** Conjunction is associative.

**formalStatement:** T(T(a,b),c)=T(a,T(b,c)).

**assumptions:** I=[0,1]⊂ℝ with ordinary order and exact equality; T:I²→I is total. Continuity and idempotence are not assumed.

**reviewStatus:** Editorial statement and derivation; no registered Lean proof witness.

**notationLanguage:** informal mathematical Unicode

**source:** [Klement, Mesiar and Pap, Triangular norms. Position paper I (2004)](https://www.flll.jku.at/sites/default/files/44_2004_KMesPap_TNormsPosPaperI_FSSPrintedVersion.pdf); citation: Fuzzy Sets and Systems 143 (2004), 5–26. DOI: 10.1016/j.fss.2003.06.007.; accessedOn: 2026-11-15; sourceRole: Consulted research paper: triangular norms, conorms, duality and examples.

**sourceLocator:** §2 Definition 2.1 pp.6–7

**sourceNote:** Defining constraints adapted to the chosen typed interface.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-TNorm-commutativity"></a>

### commutativity

`urn:csabs:axiom/TNorm-commutativity`

**statement:** Conjunction is commutative.

**description:** Conjunction is commutative.

**formalStatement:** T(a,b)=T(b,a).

**assumptions:** I=[0,1]⊂ℝ with ordinary order and exact equality; T:I²→I is total. Continuity and idempotence are not assumed.

**reviewStatus:** Editorial statement and derivation; no registered Lean proof witness.

**notationLanguage:** informal mathematical Unicode

**source:** [Klement, Mesiar and Pap, Triangular norms. Position paper I (2004)](https://www.flll.jku.at/sites/default/files/44_2004_KMesPap_TNormsPosPaperI_FSSPrintedVersion.pdf); citation: Fuzzy Sets and Systems 143 (2004), 5–26. DOI: 10.1016/j.fss.2003.06.007.; accessedOn: 2026-11-15; sourceRole: Consulted research paper: triangular norms, conorms, duality and examples.

**sourceLocator:** §2 Definition 2.1 pp.6–7

**sourceNote:** Defining constraints adapted to the chosen typed interface.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-TNorm-monotonicity"></a>

### monotonicity

`urn:csabs:axiom/TNorm-monotonicity`

**statement:** Increasing either degree cannot reduce the result.

**description:** Increasing either degree cannot reduce the result.

**formalStatement:** a≤b ∧ c≤d ⇒ T(a,c)≤T(b,d).

**assumptions:** I=[0,1]⊂ℝ with ordinary order and exact equality; T:I²→I is total. Continuity and idempotence are not assumed.

**reviewStatus:** Editorial statement and derivation; no registered Lean proof witness.

**notationLanguage:** informal mathematical Unicode

**source:** [Klement, Mesiar and Pap, Triangular norms. Position paper I (2004)](https://www.flll.jku.at/sites/default/files/44_2004_KMesPap_TNormsPosPaperI_FSSPrintedVersion.pdf); citation: Fuzzy Sets and Systems 143 (2004), 5–26. DOI: 10.1016/j.fss.2003.06.007.; accessedOn: 2026-11-15; sourceRole: Consulted research paper: triangular norms, conorms, duality and examples.

**sourceLocator:** §2 Definition 2.1 pp.6–7

**sourceNote:** Defining constraints adapted to the chosen typed interface.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-TNorm-identity"></a>

### identity

`urn:csabs:axiom/TNorm-identity`

**statement:** The truth degree 1 is a neutral element.

**description:** The truth degree 1 is a neutral element.

**formalStatement:** T(a,1)=a; T(1,a)=a.

**assumptions:** I=[0,1]⊂ℝ with ordinary order and exact equality; T:I²→I is total. Continuity and idempotence are not assumed.

**reviewStatus:** Editorial statement and derivation; no registered Lean proof witness.

**notationLanguage:** informal mathematical Unicode

**source:** [Klement, Mesiar and Pap, Triangular norms. Position paper I (2004)](https://www.flll.jku.at/sites/default/files/44_2004_KMesPap_TNormsPosPaperI_FSSPrintedVersion.pdf); citation: Fuzzy Sets and Systems 143 (2004), 5–26. DOI: 10.1016/j.fss.2003.06.007.; accessedOn: 2026-11-15; sourceRole: Consulted research paper: triangular norms, conorms, duality and examples.

**sourceLocator:** §2 Definition 2.1 pp.6–7

**sourceNote:** Defining constraints adapted to the chosen typed interface.

**provenanceKind:** adapted

**ruleRole:** defining-rule

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-TNorm-bounds-and-zero"></a>

### bounds-and-zero

`urn:csabs:theorem/TNorm-bounds-and-zero`

**statement:** Every t-norm is bounded by each input and annihilated by zero.

**description:** Every t-norm is bounded by each input and annihilated by zero.

**formalStatement:** 0≤T(a,b)≤min(a,b); T(a,0)=T(0,a)=0.

**assumptions:** I=[0,1]⊂ℝ with ordinary order and exact equality; T:I²→I is total. Continuity and idempotence are not assumed.

**reviewStatus:** Editorial statement and derivation; no registered Lean proof witness.

**notationLanguage:** informal mathematical Unicode

**source:** [Klement, Mesiar and Pap, Triangular norms. Position paper I (2004)](https://www.flll.jku.at/sites/default/files/44_2004_KMesPap_TNormsPosPaperI_FSSPrintedVersion.pdf); citation: Fuzzy Sets and Systems 143 (2004), 5–26. DOI: 10.1016/j.fss.2003.06.007.; accessedOn: 2026-11-15; sourceRole: Consulted research paper: triangular norms, conorms, duality and examples.

**sourceLocator:** §2 Definition 2.1 pp.6–7

**sourceNote:** Catalog derivation from the explicitly linked premises and elementary exact real arithmetic/order.

**provenanceKind:** derived

**dependsOn:** [monotonicity](TNorm.md#node-urn-csabs-axiom-TNorm-monotonicity); [identity](TNorm.md#node-urn-csabs-axiom-TNorm-identity)

**proofSketch:** Since b≤1, T(a,b)≤T(a,1)=a; likewise T(a,b)≤T(1,b)=b. Codomain supplies the lower bound. Set either argument to zero.

## Concept provenance

- [Klement, Mesiar and Pap, Triangular norms. Position paper I (2004)](https://www.flll.jku.at/sites/default/files/44_2004_KMesPap_TNormsPosPaperI_FSSPrintedVersion.pdf); citation: Fuzzy Sets and Systems 143 (2004), 5–26. DOI: 10.1016/j.fss.2003.06.007.; accessedOn: 2026-11-15; sourceRole: Consulted research paper: triangular norms, conorms, duality and examples.

**sourceLocator:** §2 Definition 2.1 pp.6–7

**sourceNote:** Adapted to exact real carriers and explicit catalog equality and definedness conventions.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/TNorm",
    "type": "Concept",
    "shortForm": "TNorm",
    "fullName": "Triangular norm (t-norm)",
    "category": [
      "urn:csabs:category/fuzzy-logic"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "An associative, commutative, order-monotone binary operation on the real unit interval with neutral element 1; a reusable truth-degree conjunction.",
    "notation": "T:I²→I; I=[0,1]; e=1.",
    "mathematicalFormulation": "T:I²→I; I=[0,1]; e=1. I=[0,1]⊂ℝ with ordinary order and exact equality; T:I²→I is total. Continuity and idempotence are not assumed.",
    "convention": "I=[0,1]⊂ℝ with ordinary order and exact equality; T:I²→I is total. Continuity and idempotence are not assumed.",
    "hasOperation": [
      "urn:csabs:operation/TNorm-combine"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/TNorm-associativity",
      "urn:csabs:axiom/TNorm-commutativity",
      "urn:csabs:axiom/TNorm-monotonicity",
      "urn:csabs:axiom/TNorm-identity"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/TNorm-bounds-and-zero"
    ],
    "axiomBasis": "Closed real-unit-interval operation with associativity, commutativity, monotonicity and neutral 1. No continuity axiom.",
    "basisKind": "defined-structure",
    "basisScope": "The selected exact real profile and listed operations and results; no completeness claim.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial mathematical review; Lean model coverage is separate from claim proof coverage.",
    "verificationObligation": [
      "Map equality, carriers, degree bounds and exact arithmetic to the target API. Rounded operations require separate law checks.",
      "Specialization and prerequisites do not transfer claims automatically."
    ],
    "requiresConcept": [
      "urn:csabs:concept/RealNumber",
      "urn:csabs:concept/TotalOrder"
    ],
    "relatedConcept": [
      "urn:csabs:concept/TConorm",
      "urn:csabs:concept/FuzzySet"
    ],
    "source": [
      "urn:csabs:source/klement-mesiar-pap-2004-tnorms-i"
    ],
    "sourceLocator": "§2 Definition 2.1 pp.6–7",
    "sourceNote": "Adapted to exact real carriers and explicit catalog equality and definedness conventions.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/Monoid"
    ],
    "specializationNote": "Fix one t-norm T, take monoid carrier I=[0,1], multiplication T and identity 1; ordinary real equality, associativity and neutrality instantiate the monoid interface. Monotonicity and commutativity are additional constraints.",
    "leanFormulation": "structure TNorm where\n  combine : FuzzyDegree → FuzzyDegree → FuzzyDegree\n  commutative : ∀ a b, combine a b = combine b a\n  associative : ∀ a b c, combine (combine a b) c = combine a (combine b c)\n  monotone : ∀ a b c d, a ≤ b → c ≤ d → combine a c ≤ combine b d\n  identity : ∀ a, combine a ⟨1, zero_le_one, le_refl 1⟩ = a",
    "formulationSource": "urn:csabs:source/local-lean-FuzzyLogic",
    "formulationLocator": "Catalog.TNorm",
    "formulationScope": "model",
    "leanModelMapping": "Structure on the bounded real subtype with combine and the four explicit structure laws. Equality is subtype equality, equivalent to real equality.",
    "leanModelLimitations": "No instance construction or general t-norm theorem witnesses are registered; min/product/Łukasiewicz are documented examples, not separately proved Lean instances."
  },
  {
    "id": "urn:csabs:operation/TNorm-combine",
    "type": "Operation",
    "name": "combine",
    "signature": "I² → I",
    "description": "Return T(a,b) in I. Examples: Gödel min(a,b); product ab; Łukasiewicz max(0,a+b−1). Different choices are distinct instances.",
    "concept": "urn:csabs:concept/TNorm",
    "precondition": "Arguments have the displayed types; all degree inputs are in the closed real unit interval.",
    "postcondition": "Return T(a,b) in I. Examples: Gödel min(a,b); product ab; Łukasiewicz max(0,a+b−1). Different choices are distinct instances.",
    "totality": "total on the stated typed domain"
  },
  {
    "id": "urn:csabs:theorem/TNorm-bounds-and-zero",
    "type": "Theorem",
    "name": "bounds-and-zero",
    "statement": "Every t-norm is bounded by each input and annihilated by zero.",
    "description": "Every t-norm is bounded by each input and annihilated by zero.",
    "formalStatement": "0≤T(a,b)≤min(a,b); T(a,0)=T(0,a)=0.",
    "assumptions": [
      "I=[0,1]⊂ℝ with ordinary order and exact equality; T:I²→I is total. Continuity and idempotence are not assumed."
    ],
    "appliesTo": [
      "urn:csabs:concept/TNorm"
    ],
    "reviewStatus": "Editorial statement and derivation; no registered Lean proof witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/klement-mesiar-pap-2004-tnorms-i"
    ],
    "sourceLocator": "§2 Definition 2.1 pp.6–7",
    "sourceNote": "Catalog derivation from the explicitly linked premises and elementary exact real arithmetic/order.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/TNorm-monotonicity",
      "urn:csabs:axiom/TNorm-identity"
    ],
    "proofSketch": "Since b≤1, T(a,b)≤T(a,1)=a; likewise T(a,b)≤T(1,b)=b. Codomain supplies the lower bound. Set either argument to zero."
  }
]
```
<!-- graph-record:end -->
