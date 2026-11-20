# Finite unique-hit decision table

A finite family of identifiable guarded rules, each carrying an outcome, with at most one matching rule for any input.

**Notation:** R finite; g_r:X→Prop; v:R→V; M(x)={r∈R:g_r(x)}; |M(x)|≤1.

**Stable ID:** `urn:csabs:concept/DecisionTable`

**Categories:** Programming-language semantics

**Kind:** Mathematical structure

**Prerequisites:** [Finite set collection](FiniteSet.md)

**Related concepts:** [Finite verdict-label coverage](VerdictCoverage.md)

## Backlinks

- [Ordered first-hit decision table](FirstHitDecisionTable.md) — `relatedConcept`
- [Finite verdict-label coverage](VerdictCoverage.md) — `relatedConcept`

## Mathematical formulation

R finite; g\_r:X→Prop; v:R→V; M(x)={r∈R:g\_r(x)}; |M(x)|≤1. Input carrier X and outcome carrier V may be arbitrary; R is a finite set of exact rule identities. Each rule guard is a total predicate, allowing Boolean or extended-entry conditions and irrelevant condition coordinates. This unique-hit profile requires disjoint guards; completeness is optional. An unmatched input has no decision, which is distinct from a matched rule whose outcome is itself an unknown/error value. Rule feasibility means ∃x∈X,g\_r(x); infeasible rules are excluded from coverage obligations. A finite test suite is a set of inputs, so duplicates do not increase coverage. Overlapping first-hit, priority or collect tables require explicit different hit policies. Matching a rule does not establish that the software returned the expected outcome.

**Lean formulation** (in its source module context):

```lean
structure DecisionTable (X : Type u) (R : Type v) (V : Type w) where
  rules : Finset R
  guard : R → X → Prop
  verdict : R → V
  uniqueHit : ∀ x, ∀ r ∈ rules, ∀ s ∈ rules, guard r x → guard s x → r = s
```

**Source:** [`Catalog.DecisionTable`](../lean/Catalog/RetrievalDecisions.lean); consulted 2026-11-20.

**Scope:** model

**Interpretation:** Finite rules : Finset R, guard : R→X→Prop, verdict : R→V and uniqueHit constraint. tableMatches, tableFeasible and tableExercised realize rule-set operations. booleanTable uses two Boolean identity guards and a common Unit verdict.

**Limits:** General uniqueHit is a structure constraint; the concrete Boolean partition model discharges it and is total on Bool. No chosen Option-valued evaluator, guard decision procedure or general completeness proof is supplied. Rule coverage witnesses do not prove software outcome correctness.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Finite identified rules with total guards and assigned outcomes; pairwise disjoint matching; partial decision on unmatched inputs; feasible and exercised rule sets and feasible-rule coverage.

**basisKind:** defined-structure

**basisScope:** Input carrier X and outcome carrier V may be arbitrary; R is a finite set of exact rule identities. Each rule guard is a total predicate, allowing Boolean or extended-entry conditions and irrelevant condition coordinates. This unique-hit profile requires disjoint guards; completeness is optional. An unmatched input has no decision, which is distinct from a matched rule whose outcome is itself an unknown/error value. Rule feasibility means ∃x∈X,g_r(x); infeasible rules are excluded from coverage obligations. A finite test suite is a set of inputs, so duplicates do not increase coverage. Overlapping first-hit, priority or collect tables require explicit different hit policies. Matching a rule does not establish that the software returned the expected outcome.

**verificationObligation:** Instantiate the stated carrier, equality, operation and definedness conventions. Typed links do not transfer axioms.

**reviewStatus:** Editorial mathematical interface review; only individually registered witnesses have compiler evidence.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-DecisionTable-matches"></a>

### matches

`urn:csabs:operation/DecisionTable-matches`

**signature:** M : X→FinSet(R)

**description:** Return exactly the rules whose guard holds; cardinality at most one.

**precondition:** Inputs belong to the displayed carriers.

**postcondition:** Return exactly the rules whose guard holds; cardinality at most one.

**totality:** Total on the stated typed domain; predicates and sets are mathematical, with no algorithmic complexity claim.

**source:** [ISTQB Certified Tester Foundation Level Syllabus v4.0.1 (2024-09-15)](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf); accessedOn: 2026-11-20; sourceRole: Consulted standard syllabus sections 4.2.1 and 4.2.3, printed pp.39-41: partitions, decision rules, feasibility and rule coverage. Verdict-label coverage is a catalog adaptation, not a named ISTQB criterion.

**sourceLocator:** §4.2.3 Decision table testing, printed p.41; §4.2.1 Equivalence partitioning, printed pp.39-40; unique-hit optional-partial profile is an explicit adaptation.

**sourceNote:** Definition adapted to the explicitly stated catalog carrier and operations.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-DecisionTable-decision"></a>

### decision

`urn:csabs:operation/DecisionTable-decision`

**signature:** decide : X⇀V

**description:** Defined iff a matching rule exists; return that unique rule outcome. No match is undefined, with Option(V) a possible representation.

**precondition:** Inputs belong to the displayed carriers.

**postcondition:** Defined iff a matching rule exists; return that unique rule outcome. No match is undefined, with Option(V) a possible representation.

**totality:** Total on the stated typed domain; predicates and sets are mathematical, with no algorithmic complexity claim.

**source:** [ISTQB Certified Tester Foundation Level Syllabus v4.0.1 (2024-09-15)](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf); accessedOn: 2026-11-20; sourceRole: Consulted standard syllabus sections 4.2.1 and 4.2.3, printed pp.39-41: partitions, decision rules, feasibility and rule coverage. Verdict-label coverage is a catalog adaptation, not a named ISTQB criterion.

**sourceLocator:** §4.2.3 Decision table testing, printed p.41; §4.2.1 Equivalence partitioning, printed pp.39-40; unique-hit optional-partial profile is an explicit adaptation.

**sourceNote:** Definition adapted to the explicitly stated catalog carrier and operations.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-DecisionTable-feasible-rules"></a>

### feasible-rules

`urn:csabs:operation/DecisionTable-feasible-rules`

**signature:** F : Table→FinSet(R)

**description:** F={r∈R | ∃x∈X,g_r(x)}. Mathematical feasibility may require an undecidable satisfiability check; no algorithm is assumed.

**precondition:** Inputs belong to the displayed carriers.

**postcondition:** F={r∈R | ∃x∈X,g_r(x)}. Mathematical feasibility may require an undecidable satisfiability check; no algorithm is assumed.

**totality:** Total on the stated typed domain; predicates and sets are mathematical, with no algorithmic complexity claim.

**source:** [ISTQB Certified Tester Foundation Level Syllabus v4.0.1 (2024-09-15)](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf); accessedOn: 2026-11-20; sourceRole: Consulted standard syllabus sections 4.2.1 and 4.2.3, printed pp.39-41: partitions, decision rules, feasibility and rule coverage. Verdict-label coverage is a catalog adaptation, not a named ISTQB criterion.

**sourceLocator:** §4.2.3 Decision table testing, printed p.41; §4.2.1 Equivalence partitioning, printed pp.39-40; unique-hit optional-partial profile is an explicit adaptation.

**sourceNote:** Definition adapted to the explicitly stated catalog carrier and operations.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-DecisionTable-exercised-rules"></a>

### exercised-rules

`urn:csabs:operation/DecisionTable-exercised-rules`

**signature:** E : FinSet(X)→FinSet(R)

**description:** E(S)={r∈R | ∃x∈S,g_r(x)}⊆F.

**precondition:** Inputs belong to the displayed carriers.

**postcondition:** E(S)={r∈R | ∃x∈S,g_r(x)}⊆F.

**totality:** Total on the stated typed domain; predicates and sets are mathematical, with no algorithmic complexity claim.

**source:** [ISTQB Certified Tester Foundation Level Syllabus v4.0.1 (2024-09-15)](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf); accessedOn: 2026-11-20; sourceRole: Consulted standard syllabus sections 4.2.1 and 4.2.3, printed pp.39-41: partitions, decision rules, feasibility and rule coverage. Verdict-label coverage is a catalog adaptation, not a named ISTQB criterion.

**sourceLocator:** §4.2.3 Decision table testing, printed p.41; §4.2.1 Equivalence partitioning, printed pp.39-40; unique-hit optional-partial profile is an explicit adaptation.

**sourceNote:** Definition adapted to the explicitly stated catalog carrier and operations.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-DecisionTable-rule-coverage"></a>

### rule-coverage

`urn:csabs:operation/DecisionTable-rule-coverage`

**signature:** coverage : FinSet(X)→Option(ℚ)

**description:** If F≠∅ return |E(S)|/|F|; otherwise return none. Full coverage means E(S)=F; it is vacuously true when F=∅, separately from the undefined ratio.

**precondition:** Inputs belong to the displayed carriers.

**postcondition:** If F≠∅ return |E(S)|/|F|; otherwise return none. Full coverage means E(S)=F; it is vacuously true when F=∅, separately from the undefined ratio.

**totality:** Total on the stated typed domain; predicates and sets are mathematical, with no algorithmic complexity claim.

**source:** [ISTQB Certified Tester Foundation Level Syllabus v4.0.1 (2024-09-15)](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf); accessedOn: 2026-11-20; sourceRole: Consulted standard syllabus sections 4.2.1 and 4.2.3, printed pp.39-41: partitions, decision rules, feasibility and rule coverage. Verdict-label coverage is a catalog adaptation, not a named ISTQB criterion.

**sourceLocator:** §4.2.3 Decision table testing, printed p.41; §4.2.1 Equivalence partitioning, printed pp.39-40; unique-hit optional-partial profile is an explicit adaptation.

**sourceNote:** Definition adapted to the explicitly stated catalog carrier and operations.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-DecisionTable-unique-hit-rules"></a>

### unique-hit-rules

`urn:csabs:axiom/DecisionTable-unique-hit-rules`

**statement:** Finite guarded rules have outcomes and never match simultaneously at one input.

**description:** Finite guarded rules have outcomes and never match simultaneously at one input.

**formalStatement:** R finite; g:R×X→Prop; v:R→V; ∀x,r,s∈R, g(r,x)∧g(s,x)⇒r=s; decision(x)=v(r) iff M(x)={r}; undefined iff M(x)=∅.

**assumptions:** Input carrier X and outcome carrier V may be arbitrary; R is a finite set of exact rule identities. Each rule guard is a total predicate, allowing Boolean or extended-entry conditions and irrelevant condition coordinates. This unique-hit profile requires disjoint guards; completeness is optional. An unmatched input has no decision, which is distinct from a matched rule whose outcome is itself an unknown/error value. Rule feasibility means ∃x∈X,g_r(x); infeasible rules are excluded from coverage obligations. A finite test suite is a set of inputs, so duplicates do not increase coverage. Overlapping first-hit, priority or collect tables require explicit different hit policies. Matching a rule does not establish that the software returned the expected outcome.

**reviewStatus:** Editorial statement; consult the separate Lean witness binding for exact proof scope.

**notationLanguage:** informal mathematical Unicode

**source:** [ISTQB Certified Tester Foundation Level Syllabus v4.0.1 (2024-09-15)](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf); accessedOn: 2026-11-20; sourceRole: Consulted standard syllabus sections 4.2.1 and 4.2.3, printed pp.39-41: partitions, decision rules, feasibility and rule coverage. Verdict-label coverage is a catalog adaptation, not a named ISTQB criterion.

**sourceLocator:** §4.2.3 Decision table testing, printed p.41; §4.2.1 Equivalence partitioning, printed pp.39-40; unique-hit optional-partial profile is an explicit adaptation.

**sourceNote:** Definition adapted to the explicitly stated catalog carrier and operations.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-DecisionTable-feasible-rule-coverage"></a>

### feasible-rule-coverage

`urn:csabs:axiom/DecisionTable-feasible-rule-coverage`

**statement:** Rule coverage counts exercised feasible rule identities.

**description:** Rule coverage counts exercised feasible rule identities.

**formalStatement:** F={r∈R:∃x,g(r,x)}; E(S)={r∈R:∃x∈S,g(r,x)}; full(S)⇔E(S)=F; fraction(S)=none if F=∅, otherwise some(|E(S)|/|F|).

**assumptions:** Input carrier X and outcome carrier V may be arbitrary; R is a finite set of exact rule identities. Each rule guard is a total predicate, allowing Boolean or extended-entry conditions and irrelevant condition coordinates. This unique-hit profile requires disjoint guards; completeness is optional. An unmatched input has no decision, which is distinct from a matched rule whose outcome is itself an unknown/error value. Rule feasibility means ∃x∈X,g_r(x); infeasible rules are excluded from coverage obligations. A finite test suite is a set of inputs, so duplicates do not increase coverage. Overlapping first-hit, priority or collect tables require explicit different hit policies. Matching a rule does not establish that the software returned the expected outcome.

**reviewStatus:** Editorial statement; consult the separate Lean witness binding for exact proof scope.

**notationLanguage:** informal mathematical Unicode

**source:** [ISTQB Certified Tester Foundation Level Syllabus v4.0.1 (2024-09-15)](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf); accessedOn: 2026-11-20; sourceRole: Consulted standard syllabus sections 4.2.1 and 4.2.3, printed pp.39-41: partitions, decision rules, feasibility and rule coverage. Verdict-label coverage is a catalog adaptation, not a named ISTQB criterion.

**sourceLocator:** §4.2.3 Decision table testing, printed p.41; §4.2.1 Equivalence partitioning, printed pp.39-40; unique-hit optional-partial profile is an explicit adaptation.

**sourceNote:** Definition adapted to the explicitly stated catalog carrier and operations.

**provenanceKind:** adapted

**ruleRole:** defining-rule

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-DecisionTable-boolean-partition-model-satisfaction"></a>

### boolean-partition-model-satisfaction

`urn:csabs:theorem/DecisionTable-boolean-partition-model-satisfaction`

**statement:** Two Boolean identity guards form a realizable complete unique-hit decision table.

**description:** Two Boolean identity guards form a realizable complete unique-hit decision table.

**formalStatement:** X=R={false,true}; g(r,x)⇔r=x; v(r)=unit. Each input matches exactly one rule; both rules are feasible.

**assumptions:** Input carrier X and outcome carrier V may be arbitrary; R is a finite set of exact rule identities. Each rule guard is a total predicate, allowing Boolean or extended-entry conditions and irrelevant condition coordinates. This unique-hit profile requires disjoint guards; completeness is optional. An unmatched input has no decision, which is distinct from a matched rule whose outcome is itself an unknown/error value. Rule feasibility means ∃x∈X,g_r(x); infeasible rules are excluded from coverage obligations. A finite test suite is a set of inputs, so duplicates do not increase coverage. Overlapping first-hit, priority or collect tables require explicit different hit policies. Matching a rule does not establish that the software returned the expected outcome.

**reviewStatus:** Editorial statement; consult the separate Lean witness binding for exact proof scope.

**notationLanguage:** informal mathematical Unicode

**source:** [ISTQB Certified Tester Foundation Level Syllabus v4.0.1 (2024-09-15)](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf); accessedOn: 2026-11-20; sourceRole: Consulted standard syllabus sections 4.2.1 and 4.2.3, printed pp.39-41: partitions, decision rules, feasibility and rule coverage. Verdict-label coverage is a catalog adaptation, not a named ISTQB criterion.

**sourceLocator:** §4.2.3 Decision table testing, printed p.41; §4.2.1 Equivalence partitioning, printed pp.39-40; unique-hit optional-partial profile is an explicit adaptation.

**sourceNote:** Derived from the directly linked defining premises; Equality guards are disjoint by transitivity of equality, and x itself is the matching rule. This model has two distinct inputs and two feasible rules, even though their verdicts coincide.

**provenanceKind:** derived

**dependsOn:** [unique-hit-rules](DecisionTable.md#node-urn-csabs-axiom-DecisionTable-unique-hit-rules)

**proofSketch:** Equality guards are disjoint by transitivity of equality, and x itself is the matching rule. This model has two distinct inputs and two feasible rules, even though their verdicts coincide.

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
(∀ x, ∀ r ∈ Catalog.booleanTable.rules, ∀ s ∈ Catalog.booleanTable.rules, Catalog.booleanTable.guard r x → Catalog.booleanTable.guard s x → r = s) ∧ (∀ x : Bool, ∃ r ∈ Catalog.booleanTable.rules, Catalog.booleanTable.guard r x)
```

**Source:** [`Catalog.decision_model_satisfaction`](../lean/Catalog/RetrievalDecisions.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** Finite rules : Finset R, guard : R→X→Prop, verdict : R→V and uniqueHit constraint. tableMatches, tableFeasible and tableExercised realize rule-set operations. booleanTable uses two Boolean identity guards and a common Unit verdict.

**Limits:** Proves the displayed Lean proposition only; semantic correspondence is reviewed metadata. No software implementation correctness or deductive-system completeness is asserted.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/DecisionTable-unique-hit-rules": "Direct defining premise interpreted using Finite rules : Finset R, guard : R→X→Prop, verdict : R→V and uniqueHit constraint. tableMatches, tableFeasible and tableExercised realize rule-set operations. booleanTable uses two Boolean identity guards and a common Unit verdict."
}
```

<a id="node-urn-csabs-theorem-DecisionTable-matching-rule-uniqueness"></a>

### matching-rule-uniqueness

`urn:csabs:theorem/DecisionTable-matching-rule-uniqueness`

**statement:** Any two matching rule identities are equal.

**description:** Any two matching rule identities are equal.

**formalStatement:** r,s∈M(x) ⇒ r=s.

**assumptions:** Input carrier X and outcome carrier V may be arbitrary; R is a finite set of exact rule identities. Each rule guard is a total predicate, allowing Boolean or extended-entry conditions and irrelevant condition coordinates. This unique-hit profile requires disjoint guards; completeness is optional. An unmatched input has no decision, which is distinct from a matched rule whose outcome is itself an unknown/error value. Rule feasibility means ∃x∈X,g_r(x); infeasible rules are excluded from coverage obligations. A finite test suite is a set of inputs, so duplicates do not increase coverage. Overlapping first-hit, priority or collect tables require explicit different hit policies. Matching a rule does not establish that the software returned the expected outcome.

**reviewStatus:** Editorial statement; consult the separate Lean witness binding for exact proof scope.

**notationLanguage:** informal mathematical Unicode

**source:** [ISTQB Certified Tester Foundation Level Syllabus v4.0.1 (2024-09-15)](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf); accessedOn: 2026-11-20; sourceRole: Consulted standard syllabus sections 4.2.1 and 4.2.3, printed pp.39-41: partitions, decision rules, feasibility and rule coverage. Verdict-label coverage is a catalog adaptation, not a named ISTQB criterion.

**sourceLocator:** §4.2.3 Decision table testing, printed p.41; §4.2.1 Equivalence partitioning, printed pp.39-40; unique-hit optional-partial profile is an explicit adaptation.

**sourceNote:** Derived from the directly linked defining premises; Unfold the matching filter and apply the unique-hit constraint. This derived theorem is conditional on that constraint; its nonvacuous realization is the separately constructed Boolean table.

**provenanceKind:** derived

**dependsOn:** [unique-hit-rules](DecisionTable.md#node-urn-csabs-axiom-DecisionTable-unique-hit-rules)

**proofSketch:** Unfold the matching filter and apply the unique-hit constraint. This derived theorem is conditional on that constraint; its nonvacuous realization is the separately constructed Boolean table.

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {X R V} (m : Catalog.DecisionTable X R V) (x : X) (r s : R), r ∈ Catalog.tableMatches m x → s ∈ Catalog.tableMatches m x → r = s
```

**Source:** [`Catalog.decision_matching_unique`](../lean/Catalog/RetrievalDecisions.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** Finite rules : Finset R, guard : R→X→Prop, verdict : R→V and uniqueHit constraint. tableMatches, tableFeasible and tableExercised realize rule-set operations. booleanTable uses two Boolean identity guards and a common Unit verdict.

**Limits:** Proves the displayed Lean proposition only; semantic correspondence is reviewed metadata. No software implementation correctness or deductive-system completeness is asserted.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/DecisionTable-unique-hit-rules": "Direct defining premise interpreted using Finite rules : Finset R, guard : R→X→Prop, verdict : R→V and uniqueHit constraint. tableMatches, tableFeasible and tableExercised realize rule-set operations. booleanTable uses two Boolean identity guards and a common Unit verdict."
}
```

## Concept provenance

- [ISTQB Certified Tester Foundation Level Syllabus v4.0.1 (2024-09-15)](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf); accessedOn: 2026-11-20; sourceRole: Consulted standard syllabus sections 4.2.1 and 4.2.3, printed pp.39-41: partitions, decision rules, feasibility and rule coverage. Verdict-label coverage is a catalog adaptation, not a named ISTQB criterion.

**sourceLocator:** §4.2.3 Decision table testing, printed p.41; §4.2.1 Equivalence partitioning, printed pp.39-40; unique-hit optional-partial profile is an explicit adaptation.

**sourceNote:** Definition adapted to the explicitly stated catalog carrier and operations.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/DecisionTable",
    "type": "Concept",
    "shortForm": "DecisionTable",
    "fullName": "Finite unique-hit decision table",
    "definition": "A finite family of identifiable guarded rules, each carrying an outcome, with at most one matching rule for any input.",
    "notation": "R finite; g_r:X→Prop; v:R→V; M(x)={r∈R:g_r(x)}; |M(x)|≤1.",
    "category": [
      "urn:csabs:category/programming-semantics"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "synonyms": [
      "Unique-hit decision table",
      "Disjoint guarded rule table",
      "Finite condition-action table (unique-hit)"
    ],
    "axiomBasis": "Finite identified rules with total guards and assigned outcomes; pairwise disjoint matching; partial decision on unmatched inputs; feasible and exercised rule sets and feasible-rule coverage.",
    "basisKind": "defined-structure",
    "basisScope": "Input carrier X and outcome carrier V may be arbitrary; R is a finite set of exact rule identities. Each rule guard is a total predicate, allowing Boolean or extended-entry conditions and irrelevant condition coordinates. This unique-hit profile requires disjoint guards; completeness is optional. An unmatched input has no decision, which is distinct from a matched rule whose outcome is itself an unknown/error value. Rule feasibility means ∃x∈X,g_r(x); infeasible rules are excluded from coverage obligations. A finite test suite is a set of inputs, so duplicates do not increase coverage. Overlapping first-hit, priority or collect tables require explicit different hit policies. Matching a rule does not establish that the software returned the expected outcome.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial mathematical interface review; only individually registered witnesses have compiler evidence.",
    "verificationObligation": [
      "Instantiate the stated carrier, equality, operation and definedness conventions. Typed links do not transfer axioms."
    ],
    "mathematicalFormulation": "R finite; g_r:X→Prop; v:R→V; M(x)={r∈R:g_r(x)}; |M(x)|≤1. Input carrier X and outcome carrier V may be arbitrary; R is a finite set of exact rule identities. Each rule guard is a total predicate, allowing Boolean or extended-entry conditions and irrelevant condition coordinates. This unique-hit profile requires disjoint guards; completeness is optional. An unmatched input has no decision, which is distinct from a matched rule whose outcome is itself an unknown/error value. Rule feasibility means ∃x∈X,g_r(x); infeasible rules are excluded from coverage obligations. A finite test suite is a set of inputs, so duplicates do not increase coverage. Overlapping first-hit, priority or collect tables require explicit different hit policies. Matching a rule does not establish that the software returned the expected outcome.",
    "hasOperation": [
      "urn:csabs:operation/DecisionTable-matches",
      "urn:csabs:operation/DecisionTable-decision",
      "urn:csabs:operation/DecisionTable-feasible-rules",
      "urn:csabs:operation/DecisionTable-exercised-rules",
      "urn:csabs:operation/DecisionTable-rule-coverage"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/DecisionTable-unique-hit-rules",
      "urn:csabs:axiom/DecisionTable-feasible-rule-coverage"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/DecisionTable-boolean-partition-model-satisfaction",
      "urn:csabs:theorem/DecisionTable-matching-rule-uniqueness"
    ],
    "source": [
      "urn:csabs:source/istqb-ctfl-4-0-1"
    ],
    "sourceLocator": "§4.2.3 Decision table testing, printed p.41; §4.2.1 Equivalence partitioning, printed pp.39-40; unique-hit optional-partial profile is an explicit adaptation.",
    "sourceNote": "Definition adapted to the explicitly stated catalog carrier and operations.",
    "provenanceKind": "adapted",
    "requiresConcept": [
      "urn:csabs:concept/FiniteSet"
    ],
    "relatedConcept": [
      "urn:csabs:concept/VerdictCoverage"
    ],
    "leanFormulation": "structure DecisionTable (X : Type u) (R : Type v) (V : Type w) where\n  rules : Finset R\n  guard : R → X → Prop\n  verdict : R → V\n  uniqueHit : ∀ x, ∀ r ∈ rules, ∀ s ∈ rules, guard r x → guard s x → r = s",
    "formulationSource": "urn:csabs:source/local-lean-RetrievalDecisions",
    "formulationLocator": "Catalog.DecisionTable",
    "formulationScope": "model",
    "leanModelMapping": "Finite rules : Finset R, guard : R→X→Prop, verdict : R→V and uniqueHit constraint. tableMatches, tableFeasible and tableExercised realize rule-set operations. booleanTable uses two Boolean identity guards and a common Unit verdict.",
    "leanModelLimitations": "General uniqueHit is a structure constraint; the concrete Boolean partition model discharges it and is total on Bool. No chosen Option-valued evaluator, guard decision procedure or general completeness proof is supplied. Rule coverage witnesses do not prove software outcome correctness."
  },
  {
    "id": "urn:csabs:operation/DecisionTable-matches",
    "type": "Operation",
    "name": "matches",
    "signature": "M : X→FinSet(R)",
    "description": "Return exactly the rules whose guard holds; cardinality at most one.",
    "concept": "urn:csabs:concept/DecisionTable",
    "precondition": "Inputs belong to the displayed carriers.",
    "postcondition": "Return exactly the rules whose guard holds; cardinality at most one.",
    "totality": "Total on the stated typed domain; predicates and sets are mathematical, with no algorithmic complexity claim.",
    "source": [
      "urn:csabs:source/istqb-ctfl-4-0-1"
    ],
    "sourceLocator": "§4.2.3 Decision table testing, printed p.41; §4.2.1 Equivalence partitioning, printed pp.39-40; unique-hit optional-partial profile is an explicit adaptation.",
    "sourceNote": "Definition adapted to the explicitly stated catalog carrier and operations.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/DecisionTable-decision",
    "type": "Operation",
    "name": "decision",
    "signature": "decide : X⇀V",
    "description": "Defined iff a matching rule exists; return that unique rule outcome. No match is undefined, with Option(V) a possible representation.",
    "concept": "urn:csabs:concept/DecisionTable",
    "precondition": "Inputs belong to the displayed carriers.",
    "postcondition": "Defined iff a matching rule exists; return that unique rule outcome. No match is undefined, with Option(V) a possible representation.",
    "totality": "Total on the stated typed domain; predicates and sets are mathematical, with no algorithmic complexity claim.",
    "source": [
      "urn:csabs:source/istqb-ctfl-4-0-1"
    ],
    "sourceLocator": "§4.2.3 Decision table testing, printed p.41; §4.2.1 Equivalence partitioning, printed pp.39-40; unique-hit optional-partial profile is an explicit adaptation.",
    "sourceNote": "Definition adapted to the explicitly stated catalog carrier and operations.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/DecisionTable-feasible-rules",
    "type": "Operation",
    "name": "feasible-rules",
    "signature": "F : Table→FinSet(R)",
    "description": "F={r∈R | ∃x∈X,g_r(x)}. Mathematical feasibility may require an undecidable satisfiability check; no algorithm is assumed.",
    "concept": "urn:csabs:concept/DecisionTable",
    "precondition": "Inputs belong to the displayed carriers.",
    "postcondition": "F={r∈R | ∃x∈X,g_r(x)}. Mathematical feasibility may require an undecidable satisfiability check; no algorithm is assumed.",
    "totality": "Total on the stated typed domain; predicates and sets are mathematical, with no algorithmic complexity claim.",
    "source": [
      "urn:csabs:source/istqb-ctfl-4-0-1"
    ],
    "sourceLocator": "§4.2.3 Decision table testing, printed p.41; §4.2.1 Equivalence partitioning, printed pp.39-40; unique-hit optional-partial profile is an explicit adaptation.",
    "sourceNote": "Definition adapted to the explicitly stated catalog carrier and operations.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/DecisionTable-exercised-rules",
    "type": "Operation",
    "name": "exercised-rules",
    "signature": "E : FinSet(X)→FinSet(R)",
    "description": "E(S)={r∈R | ∃x∈S,g_r(x)}⊆F.",
    "concept": "urn:csabs:concept/DecisionTable",
    "precondition": "Inputs belong to the displayed carriers.",
    "postcondition": "E(S)={r∈R | ∃x∈S,g_r(x)}⊆F.",
    "totality": "Total on the stated typed domain; predicates and sets are mathematical, with no algorithmic complexity claim.",
    "source": [
      "urn:csabs:source/istqb-ctfl-4-0-1"
    ],
    "sourceLocator": "§4.2.3 Decision table testing, printed p.41; §4.2.1 Equivalence partitioning, printed pp.39-40; unique-hit optional-partial profile is an explicit adaptation.",
    "sourceNote": "Definition adapted to the explicitly stated catalog carrier and operations.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/DecisionTable-rule-coverage",
    "type": "Operation",
    "name": "rule-coverage",
    "signature": "coverage : FinSet(X)→Option(ℚ)",
    "description": "If F≠∅ return |E(S)|/|F|; otherwise return none. Full coverage means E(S)=F; it is vacuously true when F=∅, separately from the undefined ratio.",
    "concept": "urn:csabs:concept/DecisionTable",
    "precondition": "Inputs belong to the displayed carriers.",
    "postcondition": "If F≠∅ return |E(S)|/|F|; otherwise return none. Full coverage means E(S)=F; it is vacuously true when F=∅, separately from the undefined ratio.",
    "totality": "Total on the stated typed domain; predicates and sets are mathematical, with no algorithmic complexity claim.",
    "source": [
      "urn:csabs:source/istqb-ctfl-4-0-1"
    ],
    "sourceLocator": "§4.2.3 Decision table testing, printed p.41; §4.2.1 Equivalence partitioning, printed pp.39-40; unique-hit optional-partial profile is an explicit adaptation.",
    "sourceNote": "Definition adapted to the explicitly stated catalog carrier and operations.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/DecisionTable-unique-hit-rules",
    "type": "Axiom",
    "name": "unique-hit-rules",
    "statement": "Finite guarded rules have outcomes and never match simultaneously at one input.",
    "description": "Finite guarded rules have outcomes and never match simultaneously at one input.",
    "formalStatement": "R finite; g:R×X→Prop; v:R→V; ∀x,r,s∈R, g(r,x)∧g(s,x)⇒r=s; decision(x)=v(r) iff M(x)={r}; undefined iff M(x)=∅.",
    "assumptions": [
      "Input carrier X and outcome carrier V may be arbitrary; R is a finite set of exact rule identities. Each rule guard is a total predicate, allowing Boolean or extended-entry conditions and irrelevant condition coordinates. This unique-hit profile requires disjoint guards; completeness is optional. An unmatched input has no decision, which is distinct from a matched rule whose outcome is itself an unknown/error value. Rule feasibility means ∃x∈X,g_r(x); infeasible rules are excluded from coverage obligations. A finite test suite is a set of inputs, so duplicates do not increase coverage. Overlapping first-hit, priority or collect tables require explicit different hit policies. Matching a rule does not establish that the software returned the expected outcome."
    ],
    "appliesTo": [
      "urn:csabs:concept/DecisionTable"
    ],
    "reviewStatus": "Editorial statement; consult the separate Lean witness binding for exact proof scope.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/istqb-ctfl-4-0-1"
    ],
    "sourceLocator": "§4.2.3 Decision table testing, printed p.41; §4.2.1 Equivalence partitioning, printed pp.39-40; unique-hit optional-partial profile is an explicit adaptation.",
    "sourceNote": "Definition adapted to the explicitly stated catalog carrier and operations.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/DecisionTable-feasible-rule-coverage",
    "type": "Axiom",
    "name": "feasible-rule-coverage",
    "statement": "Rule coverage counts exercised feasible rule identities.",
    "description": "Rule coverage counts exercised feasible rule identities.",
    "formalStatement": "F={r∈R:∃x,g(r,x)}; E(S)={r∈R:∃x∈S,g(r,x)}; full(S)⇔E(S)=F; fraction(S)=none if F=∅, otherwise some(|E(S)|/|F|).",
    "assumptions": [
      "Input carrier X and outcome carrier V may be arbitrary; R is a finite set of exact rule identities. Each rule guard is a total predicate, allowing Boolean or extended-entry conditions and irrelevant condition coordinates. This unique-hit profile requires disjoint guards; completeness is optional. An unmatched input has no decision, which is distinct from a matched rule whose outcome is itself an unknown/error value. Rule feasibility means ∃x∈X,g_r(x); infeasible rules are excluded from coverage obligations. A finite test suite is a set of inputs, so duplicates do not increase coverage. Overlapping first-hit, priority or collect tables require explicit different hit policies. Matching a rule does not establish that the software returned the expected outcome."
    ],
    "appliesTo": [
      "urn:csabs:concept/DecisionTable"
    ],
    "reviewStatus": "Editorial statement; consult the separate Lean witness binding for exact proof scope.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/istqb-ctfl-4-0-1"
    ],
    "sourceLocator": "§4.2.3 Decision table testing, printed p.41; §4.2.1 Equivalence partitioning, printed pp.39-40; unique-hit optional-partial profile is an explicit adaptation.",
    "sourceNote": "Definition adapted to the explicitly stated catalog carrier and operations.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:theorem/DecisionTable-boolean-partition-model-satisfaction",
    "type": "Theorem",
    "name": "boolean-partition-model-satisfaction",
    "statement": "Two Boolean identity guards form a realizable complete unique-hit decision table.",
    "description": "Two Boolean identity guards form a realizable complete unique-hit decision table.",
    "formalStatement": "X=R={false,true}; g(r,x)⇔r=x; v(r)=unit. Each input matches exactly one rule; both rules are feasible.",
    "assumptions": [
      "Input carrier X and outcome carrier V may be arbitrary; R is a finite set of exact rule identities. Each rule guard is a total predicate, allowing Boolean or extended-entry conditions and irrelevant condition coordinates. This unique-hit profile requires disjoint guards; completeness is optional. An unmatched input has no decision, which is distinct from a matched rule whose outcome is itself an unknown/error value. Rule feasibility means ∃x∈X,g_r(x); infeasible rules are excluded from coverage obligations. A finite test suite is a set of inputs, so duplicates do not increase coverage. Overlapping first-hit, priority or collect tables require explicit different hit policies. Matching a rule does not establish that the software returned the expected outcome."
    ],
    "appliesTo": [
      "urn:csabs:concept/DecisionTable"
    ],
    "reviewStatus": "Editorial statement; consult the separate Lean witness binding for exact proof scope.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/istqb-ctfl-4-0-1"
    ],
    "sourceLocator": "§4.2.3 Decision table testing, printed p.41; §4.2.1 Equivalence partitioning, printed pp.39-40; unique-hit optional-partial profile is an explicit adaptation.",
    "sourceNote": "Derived from the directly linked defining premises; Equality guards are disjoint by transitivity of equality, and x itself is the matching rule. This model has two distinct inputs and two feasible rules, even though their verdicts coincide.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/DecisionTable-unique-hit-rules"
    ],
    "proofSketch": "Equality guards are disjoint by transitivity of equality, and x itself is the matching rule. This model has two distinct inputs and two feasible rules, even though their verdicts coincide.",
    "leanFormulation": "(∀ x, ∀ r ∈ Catalog.booleanTable.rules, ∀ s ∈ Catalog.booleanTable.rules, Catalog.booleanTable.guard r x → Catalog.booleanTable.guard s x → r = s) ∧ (∀ x : Bool, ∃ r ∈ Catalog.booleanTable.rules, Catalog.booleanTable.guard r x)",
    "formulationSource": "urn:csabs:source/local-lean-RetrievalDecisions",
    "formulationLocator": "Catalog.decision_model_satisfaction",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Finite rules : Finset R, guard : R→X→Prop, verdict : R→V and uniqueHit constraint. tableMatches, tableFeasible and tableExercised realize rule-set operations. booleanTable uses two Boolean identity guards and a common Unit verdict.",
    "leanModelLimitations": "Proves the displayed Lean proposition only; semantic correspondence is reviewed metadata. No software implementation correctness or deductive-system completeness is asserted.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/DecisionTable-unique-hit-rules\": \"Direct defining premise interpreted using Finite rules : Finset R, guard : R→X→Prop, verdict : R→V and uniqueHit constraint. tableMatches, tableFeasible and tableExercised realize rule-set operations. booleanTable uses two Boolean identity guards and a common Unit verdict.\"}"
  },
  {
    "id": "urn:csabs:theorem/DecisionTable-matching-rule-uniqueness",
    "type": "Theorem",
    "name": "matching-rule-uniqueness",
    "statement": "Any two matching rule identities are equal.",
    "description": "Any two matching rule identities are equal.",
    "formalStatement": "r,s∈M(x) ⇒ r=s.",
    "assumptions": [
      "Input carrier X and outcome carrier V may be arbitrary; R is a finite set of exact rule identities. Each rule guard is a total predicate, allowing Boolean or extended-entry conditions and irrelevant condition coordinates. This unique-hit profile requires disjoint guards; completeness is optional. An unmatched input has no decision, which is distinct from a matched rule whose outcome is itself an unknown/error value. Rule feasibility means ∃x∈X,g_r(x); infeasible rules are excluded from coverage obligations. A finite test suite is a set of inputs, so duplicates do not increase coverage. Overlapping first-hit, priority or collect tables require explicit different hit policies. Matching a rule does not establish that the software returned the expected outcome."
    ],
    "appliesTo": [
      "urn:csabs:concept/DecisionTable"
    ],
    "reviewStatus": "Editorial statement; consult the separate Lean witness binding for exact proof scope.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/istqb-ctfl-4-0-1"
    ],
    "sourceLocator": "§4.2.3 Decision table testing, printed p.41; §4.2.1 Equivalence partitioning, printed pp.39-40; unique-hit optional-partial profile is an explicit adaptation.",
    "sourceNote": "Derived from the directly linked defining premises; Unfold the matching filter and apply the unique-hit constraint. This derived theorem is conditional on that constraint; its nonvacuous realization is the separately constructed Boolean table.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/DecisionTable-unique-hit-rules"
    ],
    "proofSketch": "Unfold the matching filter and apply the unique-hit constraint. This derived theorem is conditional on that constraint; its nonvacuous realization is the separately constructed Boolean table.",
    "leanFormulation": "∀ {X R V} (m : Catalog.DecisionTable X R V) (x : X) (r s : R), r ∈ Catalog.tableMatches m x → s ∈ Catalog.tableMatches m x → r = s",
    "formulationSource": "urn:csabs:source/local-lean-RetrievalDecisions",
    "formulationLocator": "Catalog.decision_matching_unique",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Finite rules : Finset R, guard : R→X→Prop, verdict : R→V and uniqueHit constraint. tableMatches, tableFeasible and tableExercised realize rule-set operations. booleanTable uses two Boolean identity guards and a common Unit verdict.",
    "leanModelLimitations": "Proves the displayed Lean proposition only; semantic correspondence is reviewed metadata. No software implementation correctness or deductive-system completeness is asserted.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/DecisionTable-unique-hit-rules\": \"Direct defining premise interpreted using Finite rules : Finset R, guard : R→X→Prop, verdict : R→V and uniqueHit constraint. tableMatches, tableFeasible and tableExercised realize rule-set operations. booleanTable uses two Boolean identity guards and a common Unit verdict.\"}"
  }
]
```
<!-- graph-record:end -->
