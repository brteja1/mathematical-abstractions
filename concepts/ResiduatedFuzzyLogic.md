# Residuated fuzzy truth-value algebra (left-continuous t-norm profile)

A real-unit-interval truth-value algebra pairing a left-continuous t-norm with its right adjoint (residual implication); weak meet/join are min/max and negation is implication to zero. This is a semantic algebra, not a formula syntax or proof calculus.

**Notation:** a⇒b=max{c∈I:T(a,c)≤b}; T(a,c)≤b ⇔ c≤(a⇒b); ¬a=(a⇒0).

**Stable ID:** `urn:csabs:concept/ResiduatedFuzzyLogic`

**Categories:** Logic and proof → Fuzzy logic

**Kind:** Mathematical structure

**Prerequisites:** [Exact real number](RealNumber.md), [Total Order](TotalOrder.md)

**Specializes:** [Triangular norm (t-norm)](TNorm.md)

**Related concepts:** [Triangular conorm (t-conorm)](TConorm.md), [Propositional Logic](PropositionalLogic.md), [Lattice](Lattice.md)

## Mathematical formulation

a⇒b=max{c∈I:T(a,c)≤b}; T(a,c)≤b ⇔ c≤(a⇒b); ¬a=(a⇒0). Exact I=[0,1], real equality/order. Fix a left-continuous t-norm: for every a and nondecreasing sequence c\_n→c in I, T(a,c\_n)→T(a,c). Only degree 1 is designated true. No assumption of involutive negation, divisibility or Boolean excluded middle. Weak conjunction min differs from strong conjunction T.

**Lean formulation** (in its source module context):

```lean
structure ResiduatedFuzzyLogic extends TNorm where
  residuum : FuzzyDegree → FuzzyDegree → FuzzyDegree
  adjunction : ∀ a b c, combine a c ≤ b ↔ c ≤ residuum a b
```

**Source:** [`Catalog.ResiduatedFuzzyLogic`](../lean/Catalog/FuzzyLogic.lean); consulted 2026-11-15.

**Scope:** partial

**Interpretation:** Extends TNorm with residuum and explicit adjunction on bounded real degrees. Adjunction restricts combine to residuated t-norms; no independent arbitrary implication is admitted.

**Limits:** Partial interface: adjunction models the left-continuous profile, but its equivalence to the displayed sequential continuity condition, derived negation, min/max and designated-truth semantics are not separately formalized. No formula syntax, proof system or registered witnesses.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** The explicitly linked t-norm rules, left-continuity and residual adjunction. The residual is uniquely determined, not an arbitrary fuzzy implication. Left-continuity is sufficient for its existence; adjunction on the real interval also entails left-continuity.

**basisKind:** defined-structure

**basisScope:** The selected exact real profile and listed operations and results; no completeness claim.

**convention:** Exact I=[0,1], real equality/order. Fix a left-continuous t-norm: for every a and nondecreasing sequence c_n→c in I, T(a,c_n)→T(a,c). Only degree 1 is designated true. No assumption of involutive negation, divisibility or Boolean excluded middle. Weak conjunction min differs from strong conjunction T.

**specializationNote:** Retain I, real equality/order and strong conjunction T, forgetting residuum, designated truth and continuity. The defining t-norm laws are explicitly applicable below.

**verificationObligation:** Map equality, carriers, degree bounds and exact arithmetic to the target API. Rounded operations require separate law checks.; Specialization and prerequisites do not transfer claims automatically.

**reviewStatus:** Editorial mathematical review; Lean model coverage is separate from claim proof coverage.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-ResiduatedFuzzyLogic-conjunction"></a>

### conjunction

`urn:csabs:operation/ResiduatedFuzzyLogic-conjunction`

**signature:** I² → I

**description:** Return strong conjunction T(a,b); weak conjunction is separately min(a,b).

**precondition:** Arguments have the displayed types; all degree inputs are in the closed real unit interval.

**postcondition:** Return strong conjunction T(a,b); weak conjunction is separately min(a,b).

**totality:** total on the stated typed domain

<a id="node-urn-csabs-operation-ResiduatedFuzzyLogic-implication"></a>

### implication

`urn:csabs:operation/ResiduatedFuzzyLogic-implication`

**signature:** I² → I

**description:** Return the attained maximum max{c∈I:T(a,c)≤b}. The set is nonempty since T(a,0)=0; left-continuity ensures attainment. Without it, a supremum formula alone need not satisfy adjunction.

**precondition:** Arguments have the displayed types; all degree inputs are in the closed real unit interval.

**postcondition:** Return the attained maximum max{c∈I:T(a,c)≤b}. The set is nonempty since T(a,0)=0; left-continuity ensures attainment. Without it, a supremum formula alone need not satisfy adjunction.

**totality:** total on the stated typed domain

<a id="node-urn-csabs-operation-ResiduatedFuzzyLogic-negation"></a>

### negation

`urn:csabs:operation/ResiduatedFuzzyLogic-negation`

**signature:** I → I

**description:** Return a⇒0. This can differ from standard complement 1−a: Gödel and product negations are 0 for a>0 and 1 at a=0.

**precondition:** Arguments have the displayed types; all degree inputs are in the closed real unit interval.

**postcondition:** Return a⇒0. This can differ from standard complement 1−a: Gödel and product negations are 0 for a>0 and 1 at a=0.

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

<a id="node-urn-csabs-axiom-ResiduatedFuzzyLogic-left-continuity"></a>

### left-continuity

`urn:csabs:axiom/ResiduatedFuzzyLogic-left-continuity`

**statement:** Strong conjunction is left-continuous in each argument.

**description:** Strong conjunction is left-continuous in each argument.

**formalStatement:** For every a∈I and nondecreasing c_n∈I converging to c∈I, T(a,c_n)→T(a,c).

**assumptions:** Exact I=[0,1], real equality/order. Fix a left-continuous t-norm: for every a and nondecreasing sequence c_n→c in I, T(a,c_n)→T(a,c). Only degree 1 is designated true. No assumption of involutive negation, divisibility or Boolean excluded middle. Weak conjunction min differs from strong conjunction T.

**reviewStatus:** Editorial statement and derivation; no registered Lean proof witness.

**notationLanguage:** informal mathematical Unicode

**source:** [Thomas Vetterlein, Regular left-continuous t-norms](https://www.flll.jku.at/sites/default/files/u24/LstetigeTnormen.pdf); accessedOn: 2026-11-15; sourceRole: Consulted author manuscript, sections 1–2: left-continuity, residua and real-unit-interval algebras.

**sourceLocator:** §1 pp.1–2; §2 Definition 2.1 pp.2–3

**sourceNote:** Defining constraints adapted to the chosen typed interface.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-ResiduatedFuzzyLogic-residuation"></a>

### residuation

`urn:csabs:axiom/ResiduatedFuzzyLogic-residuation`

**statement:** Residual implication is the right adjoint of strong conjunction.

**description:** Residual implication is the right adjoint of strong conjunction.

**formalStatement:** ∀a,b,c∈I, T(a,c)≤b ⇔ c≤(a⇒b).

**assumptions:** Exact I=[0,1], real equality/order. Fix a left-continuous t-norm: for every a and nondecreasing sequence c_n→c in I, T(a,c_n)→T(a,c). Only degree 1 is designated true. No assumption of involutive negation, divisibility or Boolean excluded middle. Weak conjunction min differs from strong conjunction T.

**reviewStatus:** Editorial statement and derivation; no registered Lean proof witness.

**notationLanguage:** informal mathematical Unicode

**source:** [Thomas Vetterlein, Regular left-continuous t-norms](https://www.flll.jku.at/sites/default/files/u24/LstetigeTnormen.pdf); accessedOn: 2026-11-15; sourceRole: Consulted author manuscript, sections 1–2: left-continuity, residua and real-unit-interval algebras.

**sourceLocator:** §1 pp.1–2; §2 Definition 2.1 pp.2–3

**sourceNote:** Defining constraints adapted to the chosen typed interface.

**provenanceKind:** adapted

**ruleRole:** defining-rule

## Laws

<a id="node-urn-csabs-law-ResiduatedFuzzyLogic-graded-modus-ponens"></a>

### graded-modus-ponens

`urn:csabs:law/ResiduatedFuzzyLogic-graded-modus-ponens`

**statement:** Conjunction with implication cannot exceed the consequent.

**description:** Conjunction with implication cannot exceed the consequent.

**formalStatement:** T(a,a⇒b)≤b.

**assumptions:** Exact I=[0,1], real equality/order. Fix a left-continuous t-norm: for every a and nondecreasing sequence c_n→c in I, T(a,c_n)→T(a,c). Only degree 1 is designated true. No assumption of involutive negation, divisibility or Boolean excluded middle. Weak conjunction min differs from strong conjunction T.

**reviewStatus:** Editorial statement and derivation; no registered Lean proof witness.

**notationLanguage:** informal mathematical Unicode

**source:** [Thomas Vetterlein, Regular left-continuous t-norms](https://www.flll.jku.at/sites/default/files/u24/LstetigeTnormen.pdf); accessedOn: 2026-11-15; sourceRole: Consulted author manuscript, sections 1–2: left-continuity, residua and real-unit-interval algebras.

**sourceLocator:** §1 pp.1–2; §2 Definition 2.1 pp.2–3

**sourceNote:** Catalog derivation from the explicitly linked premises and elementary exact real arithmetic/order.

**provenanceKind:** derived

**dependsOn:** [residuation](ResiduatedFuzzyLogic.md#node-urn-csabs-axiom-ResiduatedFuzzyLogic-residuation)

**proofSketch:** Put c=a⇒b in adjunction and apply reflexivity of ≤.

## Theorems

<a id="node-urn-csabs-theorem-ResiduatedFuzzyLogic-implication-order"></a>

### implication-order

`urn:csabs:theorem/ResiduatedFuzzyLogic-implication-order`

**statement:** Fully true implication characterizes the degree order.

**description:** Fully true implication characterizes the degree order.

**formalStatement:** (a⇒b)=1 ⇔ a≤b.

**assumptions:** Exact I=[0,1], real equality/order. Fix a left-continuous t-norm: for every a and nondecreasing sequence c_n→c in I, T(a,c_n)→T(a,c). Only degree 1 is designated true. No assumption of involutive negation, divisibility or Boolean excluded middle. Weak conjunction min differs from strong conjunction T.

**reviewStatus:** Editorial statement and derivation; no registered Lean proof witness.

**notationLanguage:** informal mathematical Unicode

**source:** [Thomas Vetterlein, Regular left-continuous t-norms](https://www.flll.jku.at/sites/default/files/u24/LstetigeTnormen.pdf); accessedOn: 2026-11-15; sourceRole: Consulted author manuscript, sections 1–2: left-continuity, residua and real-unit-interval algebras.

**sourceLocator:** §1 pp.1–2; §2 Definition 2.1 pp.2–3

**sourceNote:** Catalog derivation from the explicitly linked premises and elementary exact real arithmetic/order.

**provenanceKind:** derived

**dependsOn:** [residuation](ResiduatedFuzzyLogic.md#node-urn-csabs-axiom-ResiduatedFuzzyLogic-residuation); [identity](TNorm.md#node-urn-csabs-axiom-TNorm-identity)

**proofSketch:** By adjunction T(a,1)≤b iff 1≤(a⇒b). The identity rewrites the left side to a≤b; codomain boundedness turns the right side into equality with 1.

## Concept provenance

- [Thomas Vetterlein, Regular left-continuous t-norms](https://www.flll.jku.at/sites/default/files/u24/LstetigeTnormen.pdf); accessedOn: 2026-11-15; sourceRole: Consulted author manuscript, sections 1–2: left-continuity, residua and real-unit-interval algebras.

**sourceLocator:** §1 pp.1–2; §2 Definition 2.1 pp.2–3

**sourceNote:** Adapted to exact real carriers and explicit catalog equality and definedness conventions.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/ResiduatedFuzzyLogic",
    "type": "Concept",
    "shortForm": "ResiduatedFuzzyLogic",
    "fullName": "Residuated fuzzy truth-value algebra (left-continuous t-norm profile)",
    "category": [
      "urn:csabs:category/fuzzy-logic"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "A real-unit-interval truth-value algebra pairing a left-continuous t-norm with its right adjoint (residual implication); weak meet/join are min/max and negation is implication to zero. This is a semantic algebra, not a formula syntax or proof calculus.",
    "notation": "a⇒b=max{c∈I:T(a,c)≤b}; T(a,c)≤b ⇔ c≤(a⇒b); ¬a=(a⇒0).",
    "mathematicalFormulation": "a⇒b=max{c∈I:T(a,c)≤b}; T(a,c)≤b ⇔ c≤(a⇒b); ¬a=(a⇒0). Exact I=[0,1], real equality/order. Fix a left-continuous t-norm: for every a and nondecreasing sequence c_n→c in I, T(a,c_n)→T(a,c). Only degree 1 is designated true. No assumption of involutive negation, divisibility or Boolean excluded middle. Weak conjunction min differs from strong conjunction T.",
    "convention": "Exact I=[0,1], real equality/order. Fix a left-continuous t-norm: for every a and nondecreasing sequence c_n→c in I, T(a,c_n)→T(a,c). Only degree 1 is designated true. No assumption of involutive negation, divisibility or Boolean excluded middle. Weak conjunction min differs from strong conjunction T.",
    "hasOperation": [
      "urn:csabs:operation/ResiduatedFuzzyLogic-conjunction",
      "urn:csabs:operation/ResiduatedFuzzyLogic-implication",
      "urn:csabs:operation/ResiduatedFuzzyLogic-negation"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/TNorm-associativity",
      "urn:csabs:axiom/TNorm-commutativity",
      "urn:csabs:axiom/TNorm-monotonicity",
      "urn:csabs:axiom/TNorm-identity",
      "urn:csabs:axiom/ResiduatedFuzzyLogic-left-continuity",
      "urn:csabs:axiom/ResiduatedFuzzyLogic-residuation"
    ],
    "hasLaw": [
      "urn:csabs:law/ResiduatedFuzzyLogic-graded-modus-ponens"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/ResiduatedFuzzyLogic-implication-order"
    ],
    "axiomBasis": "The explicitly linked t-norm rules, left-continuity and residual adjunction. The residual is uniquely determined, not an arbitrary fuzzy implication. Left-continuity is sufficient for its existence; adjunction on the real interval also entails left-continuity.",
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
      "urn:csabs:concept/PropositionalLogic",
      "urn:csabs:concept/Lattice"
    ],
    "source": [
      "urn:csabs:source/vetterlein-regular-left-continuous-tnorms"
    ],
    "sourceLocator": "§1 pp.1–2; §2 Definition 2.1 pp.2–3",
    "sourceNote": "Adapted to exact real carriers and explicit catalog equality and definedness conventions.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/TNorm"
    ],
    "specializationNote": "Retain I, real equality/order and strong conjunction T, forgetting residuum, designated truth and continuity. The defining t-norm laws are explicitly applicable below.",
    "leanFormulation": "structure ResiduatedFuzzyLogic extends TNorm where\n  residuum : FuzzyDegree → FuzzyDegree → FuzzyDegree\n  adjunction : ∀ a b c, combine a c ≤ b ↔ c ≤ residuum a b",
    "formulationSource": "urn:csabs:source/local-lean-FuzzyLogic",
    "formulationLocator": "Catalog.ResiduatedFuzzyLogic",
    "formulationScope": "partial",
    "leanModelMapping": "Extends TNorm with residuum and explicit adjunction on bounded real degrees. Adjunction restricts combine to residuated t-norms; no independent arbitrary implication is admitted.",
    "leanModelLimitations": "Partial interface: adjunction models the left-continuous profile, but its equivalence to the displayed sequential continuity condition, derived negation, min/max and designated-truth semantics are not separately formalized. No formula syntax, proof system or registered witnesses."
  },
  {
    "id": "urn:csabs:operation/ResiduatedFuzzyLogic-conjunction",
    "type": "Operation",
    "name": "conjunction",
    "signature": "I² → I",
    "description": "Return strong conjunction T(a,b); weak conjunction is separately min(a,b).",
    "concept": "urn:csabs:concept/ResiduatedFuzzyLogic",
    "precondition": "Arguments have the displayed types; all degree inputs are in the closed real unit interval.",
    "postcondition": "Return strong conjunction T(a,b); weak conjunction is separately min(a,b).",
    "totality": "total on the stated typed domain"
  },
  {
    "id": "urn:csabs:operation/ResiduatedFuzzyLogic-implication",
    "type": "Operation",
    "name": "implication",
    "signature": "I² → I",
    "description": "Return the attained maximum max{c∈I:T(a,c)≤b}. The set is nonempty since T(a,0)=0; left-continuity ensures attainment. Without it, a supremum formula alone need not satisfy adjunction.",
    "concept": "urn:csabs:concept/ResiduatedFuzzyLogic",
    "precondition": "Arguments have the displayed types; all degree inputs are in the closed real unit interval.",
    "postcondition": "Return the attained maximum max{c∈I:T(a,c)≤b}. The set is nonempty since T(a,0)=0; left-continuity ensures attainment. Without it, a supremum formula alone need not satisfy adjunction.",
    "totality": "total on the stated typed domain"
  },
  {
    "id": "urn:csabs:operation/ResiduatedFuzzyLogic-negation",
    "type": "Operation",
    "name": "negation",
    "signature": "I → I",
    "description": "Return a⇒0. This can differ from standard complement 1−a: Gödel and product negations are 0 for a>0 and 1 at a=0.",
    "concept": "urn:csabs:concept/ResiduatedFuzzyLogic",
    "precondition": "Arguments have the displayed types; all degree inputs are in the closed real unit interval.",
    "postcondition": "Return a⇒0. This can differ from standard complement 1−a: Gödel and product negations are 0 for a>0 and 1 at a=0.",
    "totality": "total on the stated typed domain"
  },
  {
    "id": "urn:csabs:axiom/TNorm-associativity",
    "type": "Axiom",
    "name": "associativity",
    "statement": "Conjunction is associative.",
    "description": "Conjunction is associative.",
    "formalStatement": "T(T(a,b),c)=T(a,T(b,c)).",
    "assumptions": [
      "I=[0,1]⊂ℝ with ordinary order and exact equality; T:I²→I is total. Continuity and idempotence are not assumed."
    ],
    "appliesTo": [
      "urn:csabs:concept/TNorm",
      "urn:csabs:concept/ResiduatedFuzzyLogic"
    ],
    "reviewStatus": "Editorial statement and derivation; no registered Lean proof witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/klement-mesiar-pap-2004-tnorms-i"
    ],
    "sourceLocator": "§2 Definition 2.1 pp.6–7",
    "sourceNote": "Defining constraints adapted to the chosen typed interface.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/TNorm-commutativity",
    "type": "Axiom",
    "name": "commutativity",
    "statement": "Conjunction is commutative.",
    "description": "Conjunction is commutative.",
    "formalStatement": "T(a,b)=T(b,a).",
    "assumptions": [
      "I=[0,1]⊂ℝ with ordinary order and exact equality; T:I²→I is total. Continuity and idempotence are not assumed."
    ],
    "appliesTo": [
      "urn:csabs:concept/TNorm",
      "urn:csabs:concept/ResiduatedFuzzyLogic"
    ],
    "reviewStatus": "Editorial statement and derivation; no registered Lean proof witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/klement-mesiar-pap-2004-tnorms-i"
    ],
    "sourceLocator": "§2 Definition 2.1 pp.6–7",
    "sourceNote": "Defining constraints adapted to the chosen typed interface.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/TNorm-monotonicity",
    "type": "Axiom",
    "name": "monotonicity",
    "statement": "Increasing either degree cannot reduce the result.",
    "description": "Increasing either degree cannot reduce the result.",
    "formalStatement": "a≤b ∧ c≤d ⇒ T(a,c)≤T(b,d).",
    "assumptions": [
      "I=[0,1]⊂ℝ with ordinary order and exact equality; T:I²→I is total. Continuity and idempotence are not assumed."
    ],
    "appliesTo": [
      "urn:csabs:concept/TNorm",
      "urn:csabs:concept/ResiduatedFuzzyLogic"
    ],
    "reviewStatus": "Editorial statement and derivation; no registered Lean proof witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/klement-mesiar-pap-2004-tnorms-i"
    ],
    "sourceLocator": "§2 Definition 2.1 pp.6–7",
    "sourceNote": "Defining constraints adapted to the chosen typed interface.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/TNorm-identity",
    "type": "Axiom",
    "name": "identity",
    "statement": "The truth degree 1 is a neutral element.",
    "description": "The truth degree 1 is a neutral element.",
    "formalStatement": "T(a,1)=a; T(1,a)=a.",
    "assumptions": [
      "I=[0,1]⊂ℝ with ordinary order and exact equality; T:I²→I is total. Continuity and idempotence are not assumed."
    ],
    "appliesTo": [
      "urn:csabs:concept/TNorm",
      "urn:csabs:concept/ResiduatedFuzzyLogic"
    ],
    "reviewStatus": "Editorial statement and derivation; no registered Lean proof witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/klement-mesiar-pap-2004-tnorms-i"
    ],
    "sourceLocator": "§2 Definition 2.1 pp.6–7",
    "sourceNote": "Defining constraints adapted to the chosen typed interface.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/ResiduatedFuzzyLogic-left-continuity",
    "type": "Axiom",
    "name": "left-continuity",
    "statement": "Strong conjunction is left-continuous in each argument.",
    "description": "Strong conjunction is left-continuous in each argument.",
    "formalStatement": "For every a∈I and nondecreasing c_n∈I converging to c∈I, T(a,c_n)→T(a,c).",
    "assumptions": [
      "Exact I=[0,1], real equality/order. Fix a left-continuous t-norm: for every a and nondecreasing sequence c_n→c in I, T(a,c_n)→T(a,c). Only degree 1 is designated true. No assumption of involutive negation, divisibility or Boolean excluded middle. Weak conjunction min differs from strong conjunction T."
    ],
    "appliesTo": [
      "urn:csabs:concept/ResiduatedFuzzyLogic"
    ],
    "reviewStatus": "Editorial statement and derivation; no registered Lean proof witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/vetterlein-regular-left-continuous-tnorms"
    ],
    "sourceLocator": "§1 pp.1–2; §2 Definition 2.1 pp.2–3",
    "sourceNote": "Defining constraints adapted to the chosen typed interface.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/ResiduatedFuzzyLogic-residuation",
    "type": "Axiom",
    "name": "residuation",
    "statement": "Residual implication is the right adjoint of strong conjunction.",
    "description": "Residual implication is the right adjoint of strong conjunction.",
    "formalStatement": "∀a,b,c∈I, T(a,c)≤b ⇔ c≤(a⇒b).",
    "assumptions": [
      "Exact I=[0,1], real equality/order. Fix a left-continuous t-norm: for every a and nondecreasing sequence c_n→c in I, T(a,c_n)→T(a,c). Only degree 1 is designated true. No assumption of involutive negation, divisibility or Boolean excluded middle. Weak conjunction min differs from strong conjunction T."
    ],
    "appliesTo": [
      "urn:csabs:concept/ResiduatedFuzzyLogic"
    ],
    "reviewStatus": "Editorial statement and derivation; no registered Lean proof witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/vetterlein-regular-left-continuous-tnorms"
    ],
    "sourceLocator": "§1 pp.1–2; §2 Definition 2.1 pp.2–3",
    "sourceNote": "Defining constraints adapted to the chosen typed interface.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:law/ResiduatedFuzzyLogic-graded-modus-ponens",
    "type": "Law",
    "name": "graded-modus-ponens",
    "statement": "Conjunction with implication cannot exceed the consequent.",
    "description": "Conjunction with implication cannot exceed the consequent.",
    "formalStatement": "T(a,a⇒b)≤b.",
    "assumptions": [
      "Exact I=[0,1], real equality/order. Fix a left-continuous t-norm: for every a and nondecreasing sequence c_n→c in I, T(a,c_n)→T(a,c). Only degree 1 is designated true. No assumption of involutive negation, divisibility or Boolean excluded middle. Weak conjunction min differs from strong conjunction T."
    ],
    "appliesTo": [
      "urn:csabs:concept/ResiduatedFuzzyLogic"
    ],
    "reviewStatus": "Editorial statement and derivation; no registered Lean proof witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/vetterlein-regular-left-continuous-tnorms"
    ],
    "sourceLocator": "§1 pp.1–2; §2 Definition 2.1 pp.2–3",
    "sourceNote": "Catalog derivation from the explicitly linked premises and elementary exact real arithmetic/order.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/ResiduatedFuzzyLogic-residuation"
    ],
    "proofSketch": "Put c=a⇒b in adjunction and apply reflexivity of ≤."
  },
  {
    "id": "urn:csabs:theorem/ResiduatedFuzzyLogic-implication-order",
    "type": "Theorem",
    "name": "implication-order",
    "statement": "Fully true implication characterizes the degree order.",
    "description": "Fully true implication characterizes the degree order.",
    "formalStatement": "(a⇒b)=1 ⇔ a≤b.",
    "assumptions": [
      "Exact I=[0,1], real equality/order. Fix a left-continuous t-norm: for every a and nondecreasing sequence c_n→c in I, T(a,c_n)→T(a,c). Only degree 1 is designated true. No assumption of involutive negation, divisibility or Boolean excluded middle. Weak conjunction min differs from strong conjunction T."
    ],
    "appliesTo": [
      "urn:csabs:concept/ResiduatedFuzzyLogic"
    ],
    "reviewStatus": "Editorial statement and derivation; no registered Lean proof witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/vetterlein-regular-left-continuous-tnorms"
    ],
    "sourceLocator": "§1 pp.1–2; §2 Definition 2.1 pp.2–3",
    "sourceNote": "Catalog derivation from the explicitly linked premises and elementary exact real arithmetic/order.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/ResiduatedFuzzyLogic-residuation",
      "urn:csabs:axiom/TNorm-identity"
    ],
    "proofSketch": "By adjunction T(a,1)≤b iff 1≤(a⇒b). The identity rewrites the left side to a≤b; codomain boundedness turns the right side into equality with 1."
  }
]
```
<!-- graph-record:end -->
