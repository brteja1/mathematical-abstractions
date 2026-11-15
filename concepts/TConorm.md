# Triangular conorm (t-conorm)

An associative, commutative, order-monotone binary operation on the real unit interval with neutral element 0; a truth-degree disjunction. It need not be the lattice maximum.

**Notation:** S:I²→I; I=[0,1]; e=0.

**Stable ID:** `urn:csabs:concept/TConorm`

**Categories:** Logic and proof → Fuzzy logic

**Kind:** Mathematical structure

**Prerequisites:** [Exact real number](RealNumber.md), [Total Order](TotalOrder.md)

**Specializes:** [Monoid](Monoid.md)

**Related concepts:** [Triangular norm (t-norm)](TNorm.md), [Fuzzy set (unit-interval membership, min/max profile)](FuzzySet.md)

## Backlinks

- [Residuated fuzzy truth-value algebra (left-continuous t-norm profile)](ResiduatedFuzzyLogic.md) — `relatedConcept`
- [Triangular norm (t-norm)](TNorm.md) — `relatedConcept`

## Mathematical formulation

S:I²→I; I=[0,1]; e=0. I=[0,1]⊂ℝ with ordinary order and exact equality; S:I²→I is total. Continuity and idempotence are not assumed.

**Lean formulation** (in its source module context):

```lean
structure TConorm where
  combine : FuzzyDegree → FuzzyDegree → FuzzyDegree
  commutative : ∀ a b, combine a b = combine b a
  associative : ∀ a b c, combine (combine a b) c = combine a (combine b c)
  monotone : ∀ a b c d, a ≤ b → c ≤ d → combine a c ≤ combine b d
  identity : ∀ a, combine a ⟨0, le_refl 0, zero_le_one⟩ = a
```

**Source:** [`Catalog.TConorm`](../lean/Catalog/FuzzyLogic.lean); consulted 2026-11-15.

**Scope:** partial

**Interpretation:** Structure on FuzzyDegree with combine and the four explicit conorm laws; 0 is the identity.

**Limits:** Partial interface: combine and defining laws only; the dual construction and sample conorms are not implemented in Lean. No registered witnesses.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Closed real-unit-interval operation with associativity, commutativity, monotonicity and neutral 0. Standard duality is a construction, not an extra axiom of arbitrary conorms.

**basisKind:** defined-structure

**basisScope:** The selected exact real profile and listed operations and results; no completeness claim.

**convention:** I=[0,1]⊂ℝ with ordinary order and exact equality; S:I²→I is total. Continuity and idempotence are not assumed.

**specializationNote:** Fix S, take monoid carrier I, multiplication S and identity 0. Ordinary real equality, associativity and neutrality supply this interface; no claim is inherited automatically.

**verificationObligation:** Map equality, carriers, degree bounds and exact arithmetic to the target API. Rounded operations require separate law checks.; Specialization and prerequisites do not transfer claims automatically.

**reviewStatus:** Editorial mathematical review; Lean model coverage is separate from claim proof coverage.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-TConorm-combine"></a>

### combine

`urn:csabs:operation/TConorm-combine`

**signature:** I² → I

**description:** Return S(a,b). Examples: max(a,b); probabilistic sum a+b−ab; bounded sum min(1,a+b).

**precondition:** Arguments have the displayed types; all degree inputs are in the closed real unit interval.

**postcondition:** Return S(a,b). Examples: max(a,b); probabilistic sum a+b−ab; bounded sum min(1,a+b).

**totality:** total on the stated typed domain

<a id="node-urn-csabs-operation-TConorm-dual"></a>

### dual

`urn:csabs:operation/TConorm-dual`

**signature:** TNorm → TConorm

**description:** Given T, return S(a,b)=1−T(1−a,1−b) with the standard involutive negation. This selects the dual conorm, not an arbitrary independently chosen conorm.

**precondition:** Arguments have the displayed types; all degree inputs are in the closed real unit interval.

**postcondition:** Given T, return S(a,b)=1−T(1−a,1−b) with the standard involutive negation. This selects the dual conorm, not an arbitrary independently chosen conorm.

**totality:** total on the stated typed domain

## Axioms and defining rules

<a id="node-urn-csabs-axiom-TConorm-associativity"></a>

### associativity

`urn:csabs:axiom/TConorm-associativity`

**statement:** Disjunction is associative.

**description:** Disjunction is associative.

**formalStatement:** S(S(a,b),c)=S(a,S(b,c)).

**assumptions:** I=[0,1]⊂ℝ with ordinary order and exact equality; S:I²→I is total. Continuity and idempotence are not assumed.

**reviewStatus:** Editorial statement and derivation; no registered Lean proof witness.

**notationLanguage:** informal mathematical Unicode

**source:** [Klement, Mesiar and Pap, Triangular norms. Position paper I (2004)](https://www.flll.jku.at/sites/default/files/44_2004_KMesPap_TNormsPosPaperI_FSSPrintedVersion.pdf); citation: Fuzzy Sets and Systems 143 (2004), 5–26. DOI: 10.1016/j.fss.2003.06.007.; accessedOn: 2026-11-15; sourceRole: Consulted research paper: triangular norms, conorms, duality and examples.

**sourceLocator:** §3 Definition 3.1 and (14)–(19) pp.10–11

**sourceNote:** Defining constraints adapted to the chosen typed interface.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-TConorm-commutativity"></a>

### commutativity

`urn:csabs:axiom/TConorm-commutativity`

**statement:** Disjunction is commutative.

**description:** Disjunction is commutative.

**formalStatement:** S(a,b)=S(b,a).

**assumptions:** I=[0,1]⊂ℝ with ordinary order and exact equality; S:I²→I is total. Continuity and idempotence are not assumed.

**reviewStatus:** Editorial statement and derivation; no registered Lean proof witness.

**notationLanguage:** informal mathematical Unicode

**source:** [Klement, Mesiar and Pap, Triangular norms. Position paper I (2004)](https://www.flll.jku.at/sites/default/files/44_2004_KMesPap_TNormsPosPaperI_FSSPrintedVersion.pdf); citation: Fuzzy Sets and Systems 143 (2004), 5–26. DOI: 10.1016/j.fss.2003.06.007.; accessedOn: 2026-11-15; sourceRole: Consulted research paper: triangular norms, conorms, duality and examples.

**sourceLocator:** §3 Definition 3.1 and (14)–(19) pp.10–11

**sourceNote:** Defining constraints adapted to the chosen typed interface.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-TConorm-monotonicity"></a>

### monotonicity

`urn:csabs:axiom/TConorm-monotonicity`

**statement:** Disjunction is monotone in both arguments.

**description:** Disjunction is monotone in both arguments.

**formalStatement:** a≤b ∧ c≤d ⇒ S(a,c)≤S(b,d).

**assumptions:** I=[0,1]⊂ℝ with ordinary order and exact equality; S:I²→I is total. Continuity and idempotence are not assumed.

**reviewStatus:** Editorial statement and derivation; no registered Lean proof witness.

**notationLanguage:** informal mathematical Unicode

**source:** [Klement, Mesiar and Pap, Triangular norms. Position paper I (2004)](https://www.flll.jku.at/sites/default/files/44_2004_KMesPap_TNormsPosPaperI_FSSPrintedVersion.pdf); citation: Fuzzy Sets and Systems 143 (2004), 5–26. DOI: 10.1016/j.fss.2003.06.007.; accessedOn: 2026-11-15; sourceRole: Consulted research paper: triangular norms, conorms, duality and examples.

**sourceLocator:** §3 Definition 3.1 and (14)–(19) pp.10–11

**sourceNote:** Defining constraints adapted to the chosen typed interface.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-TConorm-identity"></a>

### identity

`urn:csabs:axiom/TConorm-identity`

**statement:** The degree 0 is neutral.

**description:** The degree 0 is neutral.

**formalStatement:** S(a,0)=a; S(0,a)=a.

**assumptions:** I=[0,1]⊂ℝ with ordinary order and exact equality; S:I²→I is total. Continuity and idempotence are not assumed.

**reviewStatus:** Editorial statement and derivation; no registered Lean proof witness.

**notationLanguage:** informal mathematical Unicode

**source:** [Klement, Mesiar and Pap, Triangular norms. Position paper I (2004)](https://www.flll.jku.at/sites/default/files/44_2004_KMesPap_TNormsPosPaperI_FSSPrintedVersion.pdf); citation: Fuzzy Sets and Systems 143 (2004), 5–26. DOI: 10.1016/j.fss.2003.06.007.; accessedOn: 2026-11-15; sourceRole: Consulted research paper: triangular norms, conorms, duality and examples.

**sourceLocator:** §3 Definition 3.1 and (14)–(19) pp.10–11

**sourceNote:** Defining constraints adapted to the chosen typed interface.

**provenanceKind:** adapted

**ruleRole:** defining-rule

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-TConorm-bounds-and-one"></a>

### bounds-and-one

`urn:csabs:theorem/TConorm-bounds-and-one`

**statement:** Every conorm dominates each input and is absorbed by one.

**description:** Every conorm dominates each input and is absorbed by one.

**formalStatement:** max(a,b)≤S(a,b)≤1; S(a,1)=S(1,a)=1.

**assumptions:** I=[0,1]⊂ℝ with ordinary order and exact equality; S:I²→I is total. Continuity and idempotence are not assumed.

**reviewStatus:** Editorial statement and derivation; no registered Lean proof witness.

**notationLanguage:** informal mathematical Unicode

**source:** [Klement, Mesiar and Pap, Triangular norms. Position paper I (2004)](https://www.flll.jku.at/sites/default/files/44_2004_KMesPap_TNormsPosPaperI_FSSPrintedVersion.pdf); citation: Fuzzy Sets and Systems 143 (2004), 5–26. DOI: 10.1016/j.fss.2003.06.007.; accessedOn: 2026-11-15; sourceRole: Consulted research paper: triangular norms, conorms, duality and examples.

**sourceLocator:** §3 Definition 3.1 and (14)–(19) pp.10–11

**sourceNote:** Catalog derivation from the explicitly linked premises and elementary exact real arithmetic/order.

**provenanceKind:** derived

**dependsOn:** [monotonicity](TConorm.md#node-urn-csabs-axiom-TConorm-monotonicity); [identity](TConorm.md#node-urn-csabs-axiom-TConorm-identity)

**proofSketch:** Use S(a,b)≥S(a,0)=a and S(a,b)≥S(0,b)=b, then use the codomain upper bound and set an argument to 1.

<a id="node-urn-csabs-theorem-TConorm-standard-duality"></a>

### standard-duality

`urn:csabs:theorem/TConorm-standard-duality`

**statement:** Standard-negation duality constructs a t-conorm from any t-norm.

**description:** Standard-negation duality constructs a t-conorm from any t-norm.

**formalStatement:** S(a,b)=1−T(1−a,1−b) ⇒ S is associative, commutative, monotone and neutral at 0.

**assumptions:** I=[0,1]⊂ℝ with ordinary order and exact equality; S:I²→I is total. Continuity and idempotence are not assumed.

**reviewStatus:** Editorial statement and derivation; no registered Lean proof witness.

**notationLanguage:** informal mathematical Unicode

**source:** [Klement, Mesiar and Pap, Triangular norms. Position paper I (2004)](https://www.flll.jku.at/sites/default/files/44_2004_KMesPap_TNormsPosPaperI_FSSPrintedVersion.pdf); citation: Fuzzy Sets and Systems 143 (2004), 5–26. DOI: 10.1016/j.fss.2003.06.007.; accessedOn: 2026-11-15; sourceRole: Consulted research paper: triangular norms, conorms, duality and examples.

**sourceLocator:** §3 pp.10–11, equivalence (18)–(19)

**sourceNote:** Catalog derivation from the explicitly linked premises and elementary exact real arithmetic/order.

**provenanceKind:** derived

**dependsOn:** [associativity](TNorm.md#node-urn-csabs-axiom-TNorm-associativity); [commutativity](TNorm.md#node-urn-csabs-axiom-TNorm-commutativity); [monotonicity](TNorm.md#node-urn-csabs-axiom-TNorm-monotonicity); [identity](TNorm.md#node-urn-csabs-axiom-TNorm-identity)

**proofSketch:** Complement maps I to I and reverses order twice. Commutativity transfers directly. Nested complements cancel for associativity; T(1−a,1)=1−a gives S(a,0)=a.

## Concept provenance

- [Klement, Mesiar and Pap, Triangular norms. Position paper I (2004)](https://www.flll.jku.at/sites/default/files/44_2004_KMesPap_TNormsPosPaperI_FSSPrintedVersion.pdf); citation: Fuzzy Sets and Systems 143 (2004), 5–26. DOI: 10.1016/j.fss.2003.06.007.; accessedOn: 2026-11-15; sourceRole: Consulted research paper: triangular norms, conorms, duality and examples.

**sourceLocator:** §3 Definition 3.1 and (14)–(19) pp.10–11

**sourceNote:** Adapted to exact real carriers and explicit catalog equality and definedness conventions.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/TConorm",
    "type": "Concept",
    "shortForm": "TConorm",
    "fullName": "Triangular conorm (t-conorm)",
    "category": [
      "urn:csabs:category/fuzzy-logic"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "An associative, commutative, order-monotone binary operation on the real unit interval with neutral element 0; a truth-degree disjunction. It need not be the lattice maximum.",
    "notation": "S:I²→I; I=[0,1]; e=0.",
    "mathematicalFormulation": "S:I²→I; I=[0,1]; e=0. I=[0,1]⊂ℝ with ordinary order and exact equality; S:I²→I is total. Continuity and idempotence are not assumed.",
    "convention": "I=[0,1]⊂ℝ with ordinary order and exact equality; S:I²→I is total. Continuity and idempotence are not assumed.",
    "hasOperation": [
      "urn:csabs:operation/TConorm-combine",
      "urn:csabs:operation/TConorm-dual"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/TConorm-associativity",
      "urn:csabs:axiom/TConorm-commutativity",
      "urn:csabs:axiom/TConorm-monotonicity",
      "urn:csabs:axiom/TConorm-identity"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/TConorm-bounds-and-one",
      "urn:csabs:theorem/TConorm-standard-duality"
    ],
    "axiomBasis": "Closed real-unit-interval operation with associativity, commutativity, monotonicity and neutral 0. Standard duality is a construction, not an extra axiom of arbitrary conorms.",
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
      "urn:csabs:concept/TNorm",
      "urn:csabs:concept/FuzzySet"
    ],
    "source": [
      "urn:csabs:source/klement-mesiar-pap-2004-tnorms-i"
    ],
    "sourceLocator": "§3 Definition 3.1 and (14)–(19) pp.10–11",
    "sourceNote": "Adapted to exact real carriers and explicit catalog equality and definedness conventions.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/Monoid"
    ],
    "specializationNote": "Fix S, take monoid carrier I, multiplication S and identity 0. Ordinary real equality, associativity and neutrality supply this interface; no claim is inherited automatically.",
    "leanFormulation": "structure TConorm where\n  combine : FuzzyDegree → FuzzyDegree → FuzzyDegree\n  commutative : ∀ a b, combine a b = combine b a\n  associative : ∀ a b c, combine (combine a b) c = combine a (combine b c)\n  monotone : ∀ a b c d, a ≤ b → c ≤ d → combine a c ≤ combine b d\n  identity : ∀ a, combine a ⟨0, le_refl 0, zero_le_one⟩ = a",
    "formulationSource": "urn:csabs:source/local-lean-FuzzyLogic",
    "formulationLocator": "Catalog.TConorm",
    "formulationScope": "partial",
    "leanModelMapping": "Structure on FuzzyDegree with combine and the four explicit conorm laws; 0 is the identity.",
    "leanModelLimitations": "Partial interface: combine and defining laws only; the dual construction and sample conorms are not implemented in Lean. No registered witnesses."
  },
  {
    "id": "urn:csabs:operation/TConorm-combine",
    "type": "Operation",
    "name": "combine",
    "signature": "I² → I",
    "description": "Return S(a,b). Examples: max(a,b); probabilistic sum a+b−ab; bounded sum min(1,a+b).",
    "concept": "urn:csabs:concept/TConorm",
    "precondition": "Arguments have the displayed types; all degree inputs are in the closed real unit interval.",
    "postcondition": "Return S(a,b). Examples: max(a,b); probabilistic sum a+b−ab; bounded sum min(1,a+b).",
    "totality": "total on the stated typed domain"
  },
  {
    "id": "urn:csabs:operation/TConorm-dual",
    "type": "Operation",
    "name": "dual",
    "signature": "TNorm → TConorm",
    "description": "Given T, return S(a,b)=1−T(1−a,1−b) with the standard involutive negation. This selects the dual conorm, not an arbitrary independently chosen conorm.",
    "concept": "urn:csabs:concept/TConorm",
    "precondition": "Arguments have the displayed types; all degree inputs are in the closed real unit interval.",
    "postcondition": "Given T, return S(a,b)=1−T(1−a,1−b) with the standard involutive negation. This selects the dual conorm, not an arbitrary independently chosen conorm.",
    "totality": "total on the stated typed domain"
  },
  {
    "id": "urn:csabs:axiom/TConorm-associativity",
    "type": "Axiom",
    "name": "associativity",
    "statement": "Disjunction is associative.",
    "description": "Disjunction is associative.",
    "formalStatement": "S(S(a,b),c)=S(a,S(b,c)).",
    "assumptions": [
      "I=[0,1]⊂ℝ with ordinary order and exact equality; S:I²→I is total. Continuity and idempotence are not assumed."
    ],
    "appliesTo": [
      "urn:csabs:concept/TConorm"
    ],
    "reviewStatus": "Editorial statement and derivation; no registered Lean proof witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/klement-mesiar-pap-2004-tnorms-i"
    ],
    "sourceLocator": "§3 Definition 3.1 and (14)–(19) pp.10–11",
    "sourceNote": "Defining constraints adapted to the chosen typed interface.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/TConorm-commutativity",
    "type": "Axiom",
    "name": "commutativity",
    "statement": "Disjunction is commutative.",
    "description": "Disjunction is commutative.",
    "formalStatement": "S(a,b)=S(b,a).",
    "assumptions": [
      "I=[0,1]⊂ℝ with ordinary order and exact equality; S:I²→I is total. Continuity and idempotence are not assumed."
    ],
    "appliesTo": [
      "urn:csabs:concept/TConorm"
    ],
    "reviewStatus": "Editorial statement and derivation; no registered Lean proof witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/klement-mesiar-pap-2004-tnorms-i"
    ],
    "sourceLocator": "§3 Definition 3.1 and (14)–(19) pp.10–11",
    "sourceNote": "Defining constraints adapted to the chosen typed interface.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/TConorm-monotonicity",
    "type": "Axiom",
    "name": "monotonicity",
    "statement": "Disjunction is monotone in both arguments.",
    "description": "Disjunction is monotone in both arguments.",
    "formalStatement": "a≤b ∧ c≤d ⇒ S(a,c)≤S(b,d).",
    "assumptions": [
      "I=[0,1]⊂ℝ with ordinary order and exact equality; S:I²→I is total. Continuity and idempotence are not assumed."
    ],
    "appliesTo": [
      "urn:csabs:concept/TConorm"
    ],
    "reviewStatus": "Editorial statement and derivation; no registered Lean proof witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/klement-mesiar-pap-2004-tnorms-i"
    ],
    "sourceLocator": "§3 Definition 3.1 and (14)–(19) pp.10–11",
    "sourceNote": "Defining constraints adapted to the chosen typed interface.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/TConorm-identity",
    "type": "Axiom",
    "name": "identity",
    "statement": "The degree 0 is neutral.",
    "description": "The degree 0 is neutral.",
    "formalStatement": "S(a,0)=a; S(0,a)=a.",
    "assumptions": [
      "I=[0,1]⊂ℝ with ordinary order and exact equality; S:I²→I is total. Continuity and idempotence are not assumed."
    ],
    "appliesTo": [
      "urn:csabs:concept/TConorm"
    ],
    "reviewStatus": "Editorial statement and derivation; no registered Lean proof witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/klement-mesiar-pap-2004-tnorms-i"
    ],
    "sourceLocator": "§3 Definition 3.1 and (14)–(19) pp.10–11",
    "sourceNote": "Defining constraints adapted to the chosen typed interface.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:theorem/TConorm-bounds-and-one",
    "type": "Theorem",
    "name": "bounds-and-one",
    "statement": "Every conorm dominates each input and is absorbed by one.",
    "description": "Every conorm dominates each input and is absorbed by one.",
    "formalStatement": "max(a,b)≤S(a,b)≤1; S(a,1)=S(1,a)=1.",
    "assumptions": [
      "I=[0,1]⊂ℝ with ordinary order and exact equality; S:I²→I is total. Continuity and idempotence are not assumed."
    ],
    "appliesTo": [
      "urn:csabs:concept/TConorm"
    ],
    "reviewStatus": "Editorial statement and derivation; no registered Lean proof witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/klement-mesiar-pap-2004-tnorms-i"
    ],
    "sourceLocator": "§3 Definition 3.1 and (14)–(19) pp.10–11",
    "sourceNote": "Catalog derivation from the explicitly linked premises and elementary exact real arithmetic/order.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/TConorm-monotonicity",
      "urn:csabs:axiom/TConorm-identity"
    ],
    "proofSketch": "Use S(a,b)≥S(a,0)=a and S(a,b)≥S(0,b)=b, then use the codomain upper bound and set an argument to 1."
  },
  {
    "id": "urn:csabs:theorem/TConorm-standard-duality",
    "type": "Theorem",
    "name": "standard-duality",
    "statement": "Standard-negation duality constructs a t-conorm from any t-norm.",
    "description": "Standard-negation duality constructs a t-conorm from any t-norm.",
    "formalStatement": "S(a,b)=1−T(1−a,1−b) ⇒ S is associative, commutative, monotone and neutral at 0.",
    "assumptions": [
      "I=[0,1]⊂ℝ with ordinary order and exact equality; S:I²→I is total. Continuity and idempotence are not assumed."
    ],
    "appliesTo": [
      "urn:csabs:concept/TConorm"
    ],
    "reviewStatus": "Editorial statement and derivation; no registered Lean proof witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/klement-mesiar-pap-2004-tnorms-i"
    ],
    "sourceLocator": "§3 pp.10–11, equivalence (18)–(19)",
    "sourceNote": "Catalog derivation from the explicitly linked premises and elementary exact real arithmetic/order.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/TNorm-associativity",
      "urn:csabs:axiom/TNorm-commutativity",
      "urn:csabs:axiom/TNorm-monotonicity",
      "urn:csabs:axiom/TNorm-identity"
    ],
    "proofSketch": "Complement maps I to I and reverses order twice. Commutativity transfers directly. Nested complements cancel for associativity; T(1−a,1)=1−a gives S(a,0)=a."
  }
]
```
<!-- graph-record:end -->
