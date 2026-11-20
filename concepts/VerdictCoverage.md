# Finite verdict-label coverage

A finite obligation set of verdict labels and finite observed labels, measuring which required labels have been observed.

**Notation:** U,O finite; H=U∩O; full⇔H=U; fraction=|H|/|U| when U≠∅.

**Stable ID:** `urn:csabs:concept/VerdictCoverage`

**Categories:** Programming-language semantics

**Kind:** Mathematical structure

**Prerequisites:** [Finite set collection](FiniteSet.md)

**Related concepts:** [Finite unique-hit decision table](DecisionTable.md)

## Backlinks

- [Finite unique-hit decision table](DecisionTable.md) — `relatedConcept`

## Mathematical formulation

U,O finite; H=U∩O; full⇔H=U; fraction=|H|/|U| when U≠∅. Verdict carrier V has exact equality. U is an explicitly declared finite target set, O a finite set of observed labels; repeats are ignored and labels outside U do not contribute. Empty U gives full coverage vacuously but an undefined numeric ratio (none). Otherwise the exact rational fraction is in [0,1]. Targets must be justified separately as feasible outcomes or required declared categories; this model cannot certify feasibility. For a decision table, choose U=v(F) and O=v(E(S)) for label coverage; choose target F and observations E(S) instead for rule coverage. F is the feasible rule set. Many rules may share a label. No statistical confidence, input-space, branch, MC/DC, proof coverage or outcome-correctness guarantee follows from label coverage.

**Lean formulation** (in its source module context):

```lean
structure VerdictCoverage (V : Type u) where
  target : Finset V
  observed : Finset V
```

**Source:** [`Catalog.VerdictCoverage`](../lean/Catalog/RetrievalDecisions.lean); consulted 2026-11-20.

**Scope:** model

**Interpretation:** Finset V target and observed with exact equality; coveredVerdicts is intersection; verdictRatio is Option ℚ with none exactly on zero target cardinality. Rule instances use V=R; verdict instances use the image of rule outcomes.

**Limits:** Witnesses prove the intersection constraints, count bound, empty-target ratio convention and a concrete distinction from rule coverage. No claim that observed labels are feasible, correct, exhaustive of behavior or probabilistically representative is made.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Finite target and observation sets; covered labels are their intersection; full coverage is set equality; exact rational count ratio is undefined on an empty target.

**basisKind:** defined-structure

**basisScope:** Verdict carrier V has exact equality. U is an explicitly declared finite target set, O a finite set of observed labels; repeats are ignored and labels outside U do not contribute. Empty U gives full coverage vacuously but an undefined numeric ratio (none). Otherwise the exact rational fraction is in [0,1]. Targets must be justified separately as feasible outcomes or required declared categories; this model cannot certify feasibility. For a decision table, choose U=v(F) and O=v(E(S)) for label coverage; choose target F and observations E(S) instead for rule coverage. F is the feasible rule set. Many rules may share a label. No statistical confidence, input-space, branch, MC/DC, proof coverage or outcome-correctness guarantee follows from label coverage.

**verificationObligation:** Instantiate the stated carrier, equality, operation and definedness conventions. Typed links do not transfer axioms.

**reviewStatus:** Editorial mathematical interface review; only individually registered witnesses have compiler evidence.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-VerdictCoverage-covered"></a>

### covered

`urn:csabs:operation/VerdictCoverage-covered`

**signature:** covered : FinSet(V)×FinSet(V)→FinSet(V)

**description:** Return U∩O, ignoring irrelevant observations and duplicates.

**precondition:** Inputs belong to the displayed carriers.

**postcondition:** Return U∩O, ignoring irrelevant observations and duplicates.

**totality:** Total on the stated typed domain; predicates and sets are mathematical, with no algorithmic complexity claim.

**source:** [ISTQB Certified Tester Foundation Level Syllabus v4.0.1 (2024-09-15)](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf); accessedOn: 2026-11-20; sourceRole: Consulted standard syllabus sections 4.2.1 and 4.2.3, printed pp.39-41: partitions, decision rules, feasibility and rule coverage. Verdict-label coverage is a catalog adaptation, not a named ISTQB criterion.; [Mathlib finite sorting, lexicographic order and cardinality at the pinned revision](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted Data/Finset/Sort.lean (sort, pairwise_sort, sort_nodup, sort_toFinset), Order/Prod/Lex/Basic.lean (toLex_le_toLex) and Data/Finset/Card.lean (card_le_card).

**sourceLocator:** §4.2.3, printed p.41, coverage as covered finite obligations over feasible obligations; adapted by replacing rule identities with explicit verdict labels, not an ISTQB-named criterion.

**sourceNote:** Definition adapted to the explicitly stated catalog carrier and operations.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-VerdictCoverage-missing"></a>

### missing

`urn:csabs:operation/VerdictCoverage-missing`

**signature:** missing : FinSet(V)×FinSet(V)→FinSet(V)

**description:** Return U∖O; full coverage iff this is empty.

**precondition:** Inputs belong to the displayed carriers.

**postcondition:** Return U∖O; full coverage iff this is empty.

**totality:** Total on the stated typed domain; predicates and sets are mathematical, with no algorithmic complexity claim.

**source:** [ISTQB Certified Tester Foundation Level Syllabus v4.0.1 (2024-09-15)](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf); accessedOn: 2026-11-20; sourceRole: Consulted standard syllabus sections 4.2.1 and 4.2.3, printed pp.39-41: partitions, decision rules, feasibility and rule coverage. Verdict-label coverage is a catalog adaptation, not a named ISTQB criterion.; [Mathlib finite sorting, lexicographic order and cardinality at the pinned revision](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted Data/Finset/Sort.lean (sort, pairwise_sort, sort_nodup, sort_toFinset), Order/Prod/Lex/Basic.lean (toLex_le_toLex) and Data/Finset/Card.lean (card_le_card).

**sourceLocator:** §4.2.3, printed p.41, coverage as covered finite obligations over feasible obligations; adapted by replacing rule identities with explicit verdict labels, not an ISTQB-named criterion.

**sourceNote:** Definition adapted to the explicitly stated catalog carrier and operations.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-VerdictCoverage-full"></a>

### full

`urn:csabs:operation/VerdictCoverage-full`

**signature:** full : FinSet(V)×FinSet(V)→Prop

**description:** Return true iff U⊆O; true for U=∅.

**precondition:** Inputs belong to the displayed carriers.

**postcondition:** Return true iff U⊆O; true for U=∅.

**totality:** Total on the stated typed domain; predicates and sets are mathematical, with no algorithmic complexity claim.

**source:** [ISTQB Certified Tester Foundation Level Syllabus v4.0.1 (2024-09-15)](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf); accessedOn: 2026-11-20; sourceRole: Consulted standard syllabus sections 4.2.1 and 4.2.3, printed pp.39-41: partitions, decision rules, feasibility and rule coverage. Verdict-label coverage is a catalog adaptation, not a named ISTQB criterion.; [Mathlib finite sorting, lexicographic order and cardinality at the pinned revision](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted Data/Finset/Sort.lean (sort, pairwise_sort, sort_nodup, sort_toFinset), Order/Prod/Lex/Basic.lean (toLex_le_toLex) and Data/Finset/Card.lean (card_le_card).

**sourceLocator:** §4.2.3, printed p.41, coverage as covered finite obligations over feasible obligations; adapted by replacing rule identities with explicit verdict labels, not an ISTQB-named criterion.

**sourceNote:** Definition adapted to the explicitly stated catalog carrier and operations.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-VerdictCoverage-fraction"></a>

### fraction

`urn:csabs:operation/VerdictCoverage-fraction`

**signature:** fraction : FinSet(V)×FinSet(V)→Option(ℚ)

**description:** Return none for U=∅, otherwise some(|U∩O|/|U|), an exact rational between zero and one.

**precondition:** Inputs belong to the displayed carriers.

**postcondition:** Return none for U=∅, otherwise some(|U∩O|/|U|), an exact rational between zero and one.

**totality:** Total on the stated typed domain; predicates and sets are mathematical, with no algorithmic complexity claim.

**source:** [ISTQB Certified Tester Foundation Level Syllabus v4.0.1 (2024-09-15)](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf); accessedOn: 2026-11-20; sourceRole: Consulted standard syllabus sections 4.2.1 and 4.2.3, printed pp.39-41: partitions, decision rules, feasibility and rule coverage. Verdict-label coverage is a catalog adaptation, not a named ISTQB criterion.; [Mathlib finite sorting, lexicographic order and cardinality at the pinned revision](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted Data/Finset/Sort.lean (sort, pairwise_sort, sort_nodup, sort_toFinset), Order/Prod/Lex/Basic.lean (toLex_le_toLex) and Data/Finset/Card.lean (card_le_card).

**sourceLocator:** §4.2.3, printed p.41, coverage as covered finite obligations over feasible obligations; adapted by replacing rule identities with explicit verdict labels, not an ISTQB-named criterion.

**sourceNote:** Definition adapted to the explicitly stated catalog carrier and operations.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-VerdictCoverage-finite-observation-definition"></a>

### finite-observation-definition

`urn:csabs:axiom/VerdictCoverage-finite-observation-definition`

**statement:** Coverage is finite-set observation against a declared target universe.

**description:** Coverage is finite-set observation against a declared target universe.

**formalStatement:** U,O⊆V finite; H=U∩O; missing=U∖O; full⇔H=U; ratio=none if |U|=0 else some(|H|/|U|).

**assumptions:** Verdict carrier V has exact equality. U is an explicitly declared finite target set, O a finite set of observed labels; repeats are ignored and labels outside U do not contribute. Empty U gives full coverage vacuously but an undefined numeric ratio (none). Otherwise the exact rational fraction is in [0,1]. Targets must be justified separately as feasible outcomes or required declared categories; this model cannot certify feasibility. For a decision table, choose U=v(F) and O=v(E(S)) for label coverage; choose target F and observations E(S) instead for rule coverage. F is the feasible rule set. Many rules may share a label. No statistical confidence, input-space, branch, MC/DC, proof coverage or outcome-correctness guarantee follows from label coverage.

**reviewStatus:** Editorial statement; consult the separate Lean witness binding for exact proof scope.

**notationLanguage:** informal mathematical Unicode

**source:** [ISTQB Certified Tester Foundation Level Syllabus v4.0.1 (2024-09-15)](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf); accessedOn: 2026-11-20; sourceRole: Consulted standard syllabus sections 4.2.1 and 4.2.3, printed pp.39-41: partitions, decision rules, feasibility and rule coverage. Verdict-label coverage is a catalog adaptation, not a named ISTQB criterion.; [Mathlib finite sorting, lexicographic order and cardinality at the pinned revision](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted Data/Finset/Sort.lean (sort, pairwise_sort, sort_nodup, sort_toFinset), Order/Prod/Lex/Basic.lean (toLex_le_toLex) and Data/Finset/Card.lean (card_le_card).

**sourceLocator:** §4.2.3, printed p.41, coverage as covered finite obligations over feasible obligations; adapted by replacing rule identities with explicit verdict labels, not an ISTQB-named criterion.

**sourceNote:** Definition adapted to the explicitly stated catalog carrier and operations.

**provenanceKind:** adapted

**ruleRole:** defining-rule

## Laws

<a id="node-urn-csabs-law-VerdictCoverage-covered-count-bound"></a>

### covered-count-bound

`urn:csabs:law/VerdictCoverage-covered-count-bound`

**statement:** The number of covered labels cannot exceed the number of required labels.

**description:** The number of covered labels cannot exceed the number of required labels.

**formalStatement:** |U∩O|≤|U|.

**assumptions:** Verdict carrier V has exact equality. U is an explicitly declared finite target set, O a finite set of observed labels; repeats are ignored and labels outside U do not contribute. Empty U gives full coverage vacuously but an undefined numeric ratio (none). Otherwise the exact rational fraction is in [0,1]. Targets must be justified separately as feasible outcomes or required declared categories; this model cannot certify feasibility. For a decision table, choose U=v(F) and O=v(E(S)) for label coverage; choose target F and observations E(S) instead for rule coverage. F is the feasible rule set. Many rules may share a label. No statistical confidence, input-space, branch, MC/DC, proof coverage or outcome-correctness guarantee follows from label coverage.

**reviewStatus:** Editorial statement; consult the separate Lean witness binding for exact proof scope.

**notationLanguage:** informal mathematical Unicode

**source:** [ISTQB Certified Tester Foundation Level Syllabus v4.0.1 (2024-09-15)](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf); accessedOn: 2026-11-20; sourceRole: Consulted standard syllabus sections 4.2.1 and 4.2.3, printed pp.39-41: partitions, decision rules, feasibility and rule coverage. Verdict-label coverage is a catalog adaptation, not a named ISTQB criterion.; [Mathlib finite sorting, lexicographic order and cardinality at the pinned revision](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted Data/Finset/Sort.lean (sort, pairwise_sort, sort_nodup, sort_toFinset), Order/Prod/Lex/Basic.lean (toLex_le_toLex) and Data/Finset/Card.lean (card_le_card).

**sourceLocator:** §4.2.3, printed p.41, coverage as covered finite obligations over feasible obligations; adapted by replacing rule identities with explicit verdict labels, not an ISTQB-named criterion.

**sourceNote:** Derived from the directly linked defining premises; Intersection is a subset of U; cardinality is monotone for finite subsets.

**provenanceKind:** derived

**dependsOn:** [finite-observation-definition](VerdictCoverage.md#node-urn-csabs-axiom-VerdictCoverage-finite-observation-definition)

**proofSketch:** Intersection is a subset of U; cardinality is monotone for finite subsets.

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {V} (m : Catalog.VerdictCoverage V), (Catalog.coveredVerdicts m).card ≤ m.target.card
```

**Source:** [`Catalog.verdict_count_bound`](../lean/Catalog/RetrievalDecisions.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** Finset V target and observed with exact equality; coveredVerdicts is intersection; verdictRatio is Option ℚ with none exactly on zero target cardinality. Rule instances use V=R; verdict instances use the image of rule outcomes.

**Limits:** Proves the displayed Lean proposition only; semantic correspondence is reviewed metadata. No software implementation correctness or deductive-system completeness is asserted.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/VerdictCoverage-finite-observation-definition": "Direct defining premise interpreted using Finset V target and observed with exact equality; coveredVerdicts is intersection; verdictRatio is Option ℚ with none exactly on zero target cardinality. Rule instances use V=R; verdict instances use the image of rule outcomes."
}
```

<a id="node-urn-csabs-law-VerdictCoverage-empty-target-ratio"></a>

### empty-target-ratio

`urn:csabs:law/VerdictCoverage-empty-target-ratio`

**statement:** An empty target has no numeric coverage ratio.

**description:** An empty target has no numeric coverage ratio.

**formalStatement:** ratio(∅,O)=none; full(∅,O)=true.

**assumptions:** Verdict carrier V has exact equality. U is an explicitly declared finite target set, O a finite set of observed labels; repeats are ignored and labels outside U do not contribute. Empty U gives full coverage vacuously but an undefined numeric ratio (none). Otherwise the exact rational fraction is in [0,1]. Targets must be justified separately as feasible outcomes or required declared categories; this model cannot certify feasibility. For a decision table, choose U=v(F) and O=v(E(S)) for label coverage; choose target F and observations E(S) instead for rule coverage. F is the feasible rule set. Many rules may share a label. No statistical confidence, input-space, branch, MC/DC, proof coverage or outcome-correctness guarantee follows from label coverage.

**reviewStatus:** Editorial statement; consult the separate Lean witness binding for exact proof scope.

**notationLanguage:** informal mathematical Unicode

**source:** [ISTQB Certified Tester Foundation Level Syllabus v4.0.1 (2024-09-15)](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf); accessedOn: 2026-11-20; sourceRole: Consulted standard syllabus sections 4.2.1 and 4.2.3, printed pp.39-41: partitions, decision rules, feasibility and rule coverage. Verdict-label coverage is a catalog adaptation, not a named ISTQB criterion.; [Mathlib finite sorting, lexicographic order and cardinality at the pinned revision](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted Data/Finset/Sort.lean (sort, pairwise_sort, sort_nodup, sort_toFinset), Order/Prod/Lex/Basic.lean (toLex_le_toLex) and Data/Finset/Card.lean (card_le_card).

**sourceLocator:** §4.2.3, printed p.41, coverage as covered finite obligations over feasible obligations; adapted by replacing rule identities with explicit verdict labels, not an ISTQB-named criterion.

**sourceNote:** Derived from the directly linked defining premises; The denominator cardinality is zero, selecting none. Vacuous fullness follows separately from the subset definition; the registered witness is for the Option-valued ratio only.

**provenanceKind:** derived

**dependsOn:** [finite-observation-definition](VerdictCoverage.md#node-urn-csabs-axiom-VerdictCoverage-finite-observation-definition)

**proofSketch:** The denominator cardinality is zero, selecting none. Vacuous fullness follows separately from the subset definition; the registered witness is for the Option-valued ratio only.

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {V} (observed : Finset V), Catalog.verdictRatio (⟨∅, observed⟩ : Catalog.VerdictCoverage V) = none
```

**Source:** [`Catalog.verdict_empty_target`](../lean/Catalog/RetrievalDecisions.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** Finset V target and observed with exact equality; coveredVerdicts is intersection; verdictRatio is Option ℚ with none exactly on zero target cardinality. Rule instances use V=R; verdict instances use the image of rule outcomes.

**Limits:** Proves the displayed Lean proposition only; semantic correspondence is reviewed metadata. No software implementation correctness or deductive-system completeness is asserted.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/VerdictCoverage-finite-observation-definition": "Direct defining premise interpreted using Finset V target and observed with exact equality; coveredVerdicts is intersection; verdictRatio is Option ℚ with none exactly on zero target cardinality. Rule instances use V=R; verdict instances use the image of rule outcomes."
}
```

## Theorems

<a id="node-urn-csabs-theorem-VerdictCoverage-intersection-model-satisfaction"></a>

### intersection-model-satisfaction

`urn:csabs:theorem/VerdictCoverage-intersection-model-satisfaction`

**statement:** The finite-intersection realization counts only required and observed labels.

**description:** The finite-intersection realization counts only required and observed labels.

**formalStatement:** For all finite U,O, H=U∩O is a subset of both U and O.

**assumptions:** Verdict carrier V has exact equality. U is an explicitly declared finite target set, O a finite set of observed labels; repeats are ignored and labels outside U do not contribute. Empty U gives full coverage vacuously but an undefined numeric ratio (none). Otherwise the exact rational fraction is in [0,1]. Targets must be justified separately as feasible outcomes or required declared categories; this model cannot certify feasibility. For a decision table, choose U=v(F) and O=v(E(S)) for label coverage; choose target F and observations E(S) instead for rule coverage. F is the feasible rule set. Many rules may share a label. No statistical confidence, input-space, branch, MC/DC, proof coverage or outcome-correctness guarantee follows from label coverage.

**reviewStatus:** Editorial statement; consult the separate Lean witness binding for exact proof scope.

**notationLanguage:** informal mathematical Unicode

**source:** [ISTQB Certified Tester Foundation Level Syllabus v4.0.1 (2024-09-15)](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf); accessedOn: 2026-11-20; sourceRole: Consulted standard syllabus sections 4.2.1 and 4.2.3, printed pp.39-41: partitions, decision rules, feasibility and rule coverage. Verdict-label coverage is a catalog adaptation, not a named ISTQB criterion.; [Mathlib finite sorting, lexicographic order and cardinality at the pinned revision](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted Data/Finset/Sort.lean (sort, pairwise_sort, sort_nodup, sort_toFinset), Order/Prod/Lex/Basic.lean (toLex_le_toLex) and Data/Finset/Card.lean (card_le_card).

**sourceLocator:** §4.2.3, printed p.41, coverage as covered finite obligations over feasible obligations; adapted by replacing rule identities with explicit verdict labels, not an ISTQB-named criterion.

**sourceNote:** Derived from the directly linked defining premises; Construct H by finite intersection and use its two subset projections; arbitrary finite targets and observations realize the basis without assumed coverage-law fields.

**provenanceKind:** derived

**dependsOn:** [finite-observation-definition](VerdictCoverage.md#node-urn-csabs-axiom-VerdictCoverage-finite-observation-definition)

**proofSketch:** Construct H by finite intersection and use its two subset projections; arbitrary finite targets and observations realize the basis without assumed coverage-law fields.

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {V} (m : Catalog.VerdictCoverage V), Catalog.coveredVerdicts m ⊆ m.target ∧ Catalog.coveredVerdicts m ⊆ m.observed
```

**Source:** [`Catalog.verdict_model_satisfaction`](../lean/Catalog/RetrievalDecisions.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** Finset V target and observed with exact equality; coveredVerdicts is intersection; verdictRatio is Option ℚ with none exactly on zero target cardinality. Rule instances use V=R; verdict instances use the image of rule outcomes.

**Limits:** Proves the displayed Lean proposition only; semantic correspondence is reviewed metadata. No software implementation correctness or deductive-system completeness is asserted.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/VerdictCoverage-finite-observation-definition": "Direct defining premise interpreted using Finset V target and observed with exact equality; coveredVerdicts is intersection; verdictRatio is Option ℚ with none exactly on zero target cardinality. Rule instances use V=R; verdict instances use the image of rule outcomes."
}
```

<a id="node-urn-csabs-theorem-VerdictCoverage-verdict-does-not-imply-rule-coverage"></a>

### verdict-does-not-imply-rule-coverage

`urn:csabs:theorem/VerdictCoverage-verdict-does-not-imply-rule-coverage`

**statement:** Full verdict-label coverage need not cover every feasible rule.

**description:** Full verdict-label coverage need not cover every feasible rule.

**formalStatement:** There exists a unique-hit table and suite S with v(E(S))=v(F) but E(S)≠F.

**assumptions:** Verdict carrier V has exact equality. U is an explicitly declared finite target set, O a finite set of observed labels; repeats are ignored and labels outside U do not contribute. Empty U gives full coverage vacuously but an undefined numeric ratio (none). Otherwise the exact rational fraction is in [0,1]. Targets must be justified separately as feasible outcomes or required declared categories; this model cannot certify feasibility. For a decision table, choose U=v(F) and O=v(E(S)) for label coverage; choose target F and observations E(S) instead for rule coverage. F is the feasible rule set. Many rules may share a label. No statistical confidence, input-space, branch, MC/DC, proof coverage or outcome-correctness guarantee follows from label coverage.

**reviewStatus:** Editorial statement; consult the separate Lean witness binding for exact proof scope.

**notationLanguage:** informal mathematical Unicode

**source:** [ISTQB Certified Tester Foundation Level Syllabus v4.0.1 (2024-09-15)](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf); accessedOn: 2026-11-20; sourceRole: Consulted standard syllabus sections 4.2.1 and 4.2.3, printed pp.39-41: partitions, decision rules, feasibility and rule coverage. Verdict-label coverage is a catalog adaptation, not a named ISTQB criterion.; [Mathlib finite sorting, lexicographic order and cardinality at the pinned revision](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted Data/Finset/Sort.lean (sort, pairwise_sort, sort_nodup, sort_toFinset), Order/Prod/Lex/Basic.lean (toLex_le_toLex) and Data/Finset/Card.lean (card_le_card).

**sourceLocator:** §4.2.3, printed p.41, coverage as covered finite obligations over feasible obligations; adapted by replacing rule identities with explicit verdict labels, not an ISTQB-named criterion.

**sourceNote:** Derived from the directly linked defining premises; Use two feasible Boolean identity rules with the same Unit verdict. The singleton suite {false} observes the only verdict but leaves the true rule unexercised. This is a counterexample to the converse; full feasible-rule coverage does imply full feasible-verdict coverage by taking images.

**provenanceKind:** derived

**dependsOn:** [finite-observation-definition](VerdictCoverage.md#node-urn-csabs-axiom-VerdictCoverage-finite-observation-definition); [unique-hit-rules](DecisionTable.md#node-urn-csabs-axiom-DecisionTable-unique-hit-rules); [feasible-rule-coverage](DecisionTable.md#node-urn-csabs-axiom-DecisionTable-feasible-rule-coverage)

**proofSketch:** Use two feasible Boolean identity rules with the same Unit verdict. The singleton suite {false} observes the only verdict but leaves the true rule unexercised. This is a counterexample to the converse; full feasible-rule coverage does imply full feasible-verdict coverage by taking images.

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
(Catalog.tableExercised Catalog.booleanTable {false}).image Catalog.booleanTable.verdict = (Catalog.tableFeasible Catalog.booleanTable).image Catalog.booleanTable.verdict ∧ Catalog.tableExercised Catalog.booleanTable {false} ≠ Catalog.tableFeasible Catalog.booleanTable
```

**Source:** [`Catalog.verdict_not_rule_coverage`](../lean/Catalog/RetrievalDecisions.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** Finset V target and observed with exact equality; coveredVerdicts is intersection; verdictRatio is Option ℚ with none exactly on zero target cardinality. Rule instances use V=R; verdict instances use the image of rule outcomes.

**Limits:** Proves the displayed Lean proposition only; semantic correspondence is reviewed metadata. No software implementation correctness or deductive-system completeness is asserted.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/DecisionTable-feasible-rule-coverage": "Direct defining premise interpreted using Finset V target and observed with exact equality; coveredVerdicts is intersection; verdictRatio is Option ℚ with none exactly on zero target cardinality. Rule instances use V=R; verdict instances use the image of rule outcomes.",
  "urn:csabs:axiom/DecisionTable-unique-hit-rules": "Direct defining premise interpreted using Finset V target and observed with exact equality; coveredVerdicts is intersection; verdictRatio is Option ℚ with none exactly on zero target cardinality. Rule instances use V=R; verdict instances use the image of rule outcomes.",
  "urn:csabs:axiom/VerdictCoverage-finite-observation-definition": "Direct defining premise interpreted using Finset V target and observed with exact equality; coveredVerdicts is intersection; verdictRatio is Option ℚ with none exactly on zero target cardinality. Rule instances use V=R; verdict instances use the image of rule outcomes."
}
```

## Concept provenance

- [ISTQB Certified Tester Foundation Level Syllabus v4.0.1 (2024-09-15)](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf); accessedOn: 2026-11-20; sourceRole: Consulted standard syllabus sections 4.2.1 and 4.2.3, printed pp.39-41: partitions, decision rules, feasibility and rule coverage. Verdict-label coverage is a catalog adaptation, not a named ISTQB criterion.
- [Mathlib finite sorting, lexicographic order and cardinality at the pinned revision](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted Data/Finset/Sort.lean (sort, pairwise_sort, sort_nodup, sort_toFinset), Order/Prod/Lex/Basic.lean (toLex_le_toLex) and Data/Finset/Card.lean (card_le_card).

**sourceLocator:** §4.2.3, printed p.41, coverage as covered finite obligations over feasible obligations; adapted by replacing rule identities with explicit verdict labels, not an ISTQB-named criterion.

**sourceNote:** Definition adapted to the explicitly stated catalog carrier and operations.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/VerdictCoverage",
    "type": "Concept",
    "shortForm": "VerdictCoverage",
    "fullName": "Finite verdict-label coverage",
    "definition": "A finite obligation set of verdict labels and finite observed labels, measuring which required labels have been observed.",
    "notation": "U,O finite; H=U∩O; full⇔H=U; fraction=|H|/|U| when U≠∅.",
    "category": [
      "urn:csabs:category/programming-semantics"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "synonyms": [
      "Verdict-label coverage",
      "Finite outcome-category coverage",
      "Finite label-observation coverage"
    ],
    "axiomBasis": "Finite target and observation sets; covered labels are their intersection; full coverage is set equality; exact rational count ratio is undefined on an empty target.",
    "basisKind": "defined-structure",
    "basisScope": "Verdict carrier V has exact equality. U is an explicitly declared finite target set, O a finite set of observed labels; repeats are ignored and labels outside U do not contribute. Empty U gives full coverage vacuously but an undefined numeric ratio (none). Otherwise the exact rational fraction is in [0,1]. Targets must be justified separately as feasible outcomes or required declared categories; this model cannot certify feasibility. For a decision table, choose U=v(F) and O=v(E(S)) for label coverage; choose target F and observations E(S) instead for rule coverage. F is the feasible rule set. Many rules may share a label. No statistical confidence, input-space, branch, MC/DC, proof coverage or outcome-correctness guarantee follows from label coverage.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial mathematical interface review; only individually registered witnesses have compiler evidence.",
    "verificationObligation": [
      "Instantiate the stated carrier, equality, operation and definedness conventions. Typed links do not transfer axioms."
    ],
    "mathematicalFormulation": "U,O finite; H=U∩O; full⇔H=U; fraction=|H|/|U| when U≠∅. Verdict carrier V has exact equality. U is an explicitly declared finite target set, O a finite set of observed labels; repeats are ignored and labels outside U do not contribute. Empty U gives full coverage vacuously but an undefined numeric ratio (none). Otherwise the exact rational fraction is in [0,1]. Targets must be justified separately as feasible outcomes or required declared categories; this model cannot certify feasibility. For a decision table, choose U=v(F) and O=v(E(S)) for label coverage; choose target F and observations E(S) instead for rule coverage. F is the feasible rule set. Many rules may share a label. No statistical confidence, input-space, branch, MC/DC, proof coverage or outcome-correctness guarantee follows from label coverage.",
    "hasOperation": [
      "urn:csabs:operation/VerdictCoverage-covered",
      "urn:csabs:operation/VerdictCoverage-missing",
      "urn:csabs:operation/VerdictCoverage-full",
      "urn:csabs:operation/VerdictCoverage-fraction"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/VerdictCoverage-finite-observation-definition"
    ],
    "hasLaw": [
      "urn:csabs:law/VerdictCoverage-covered-count-bound",
      "urn:csabs:law/VerdictCoverage-empty-target-ratio"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/VerdictCoverage-intersection-model-satisfaction",
      "urn:csabs:theorem/VerdictCoverage-verdict-does-not-imply-rule-coverage"
    ],
    "source": [
      "urn:csabs:source/istqb-ctfl-4-0-1",
      "urn:csabs:source/mathlib-finite-ranking-pinned"
    ],
    "sourceLocator": "§4.2.3, printed p.41, coverage as covered finite obligations over feasible obligations; adapted by replacing rule identities with explicit verdict labels, not an ISTQB-named criterion.",
    "sourceNote": "Definition adapted to the explicitly stated catalog carrier and operations.",
    "provenanceKind": "adapted",
    "requiresConcept": [
      "urn:csabs:concept/FiniteSet"
    ],
    "relatedConcept": [
      "urn:csabs:concept/DecisionTable"
    ],
    "leanFormulation": "structure VerdictCoverage (V : Type u) where\n  target : Finset V\n  observed : Finset V",
    "formulationSource": "urn:csabs:source/local-lean-RetrievalDecisions",
    "formulationLocator": "Catalog.VerdictCoverage",
    "formulationScope": "model",
    "leanModelMapping": "Finset V target and observed with exact equality; coveredVerdicts is intersection; verdictRatio is Option ℚ with none exactly on zero target cardinality. Rule instances use V=R; verdict instances use the image of rule outcomes.",
    "leanModelLimitations": "Witnesses prove the intersection constraints, count bound, empty-target ratio convention and a concrete distinction from rule coverage. No claim that observed labels are feasible, correct, exhaustive of behavior or probabilistically representative is made."
  },
  {
    "id": "urn:csabs:operation/VerdictCoverage-covered",
    "type": "Operation",
    "name": "covered",
    "signature": "covered : FinSet(V)×FinSet(V)→FinSet(V)",
    "description": "Return U∩O, ignoring irrelevant observations and duplicates.",
    "concept": "urn:csabs:concept/VerdictCoverage",
    "precondition": "Inputs belong to the displayed carriers.",
    "postcondition": "Return U∩O, ignoring irrelevant observations and duplicates.",
    "totality": "Total on the stated typed domain; predicates and sets are mathematical, with no algorithmic complexity claim.",
    "source": [
      "urn:csabs:source/istqb-ctfl-4-0-1",
      "urn:csabs:source/mathlib-finite-ranking-pinned"
    ],
    "sourceLocator": "§4.2.3, printed p.41, coverage as covered finite obligations over feasible obligations; adapted by replacing rule identities with explicit verdict labels, not an ISTQB-named criterion.",
    "sourceNote": "Definition adapted to the explicitly stated catalog carrier and operations.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/VerdictCoverage-missing",
    "type": "Operation",
    "name": "missing",
    "signature": "missing : FinSet(V)×FinSet(V)→FinSet(V)",
    "description": "Return U∖O; full coverage iff this is empty.",
    "concept": "urn:csabs:concept/VerdictCoverage",
    "precondition": "Inputs belong to the displayed carriers.",
    "postcondition": "Return U∖O; full coverage iff this is empty.",
    "totality": "Total on the stated typed domain; predicates and sets are mathematical, with no algorithmic complexity claim.",
    "source": [
      "urn:csabs:source/istqb-ctfl-4-0-1",
      "urn:csabs:source/mathlib-finite-ranking-pinned"
    ],
    "sourceLocator": "§4.2.3, printed p.41, coverage as covered finite obligations over feasible obligations; adapted by replacing rule identities with explicit verdict labels, not an ISTQB-named criterion.",
    "sourceNote": "Definition adapted to the explicitly stated catalog carrier and operations.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/VerdictCoverage-full",
    "type": "Operation",
    "name": "full",
    "signature": "full : FinSet(V)×FinSet(V)→Prop",
    "description": "Return true iff U⊆O; true for U=∅.",
    "concept": "urn:csabs:concept/VerdictCoverage",
    "precondition": "Inputs belong to the displayed carriers.",
    "postcondition": "Return true iff U⊆O; true for U=∅.",
    "totality": "Total on the stated typed domain; predicates and sets are mathematical, with no algorithmic complexity claim.",
    "source": [
      "urn:csabs:source/istqb-ctfl-4-0-1",
      "urn:csabs:source/mathlib-finite-ranking-pinned"
    ],
    "sourceLocator": "§4.2.3, printed p.41, coverage as covered finite obligations over feasible obligations; adapted by replacing rule identities with explicit verdict labels, not an ISTQB-named criterion.",
    "sourceNote": "Definition adapted to the explicitly stated catalog carrier and operations.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/VerdictCoverage-fraction",
    "type": "Operation",
    "name": "fraction",
    "signature": "fraction : FinSet(V)×FinSet(V)→Option(ℚ)",
    "description": "Return none for U=∅, otherwise some(|U∩O|/|U|), an exact rational between zero and one.",
    "concept": "urn:csabs:concept/VerdictCoverage",
    "precondition": "Inputs belong to the displayed carriers.",
    "postcondition": "Return none for U=∅, otherwise some(|U∩O|/|U|), an exact rational between zero and one.",
    "totality": "Total on the stated typed domain; predicates and sets are mathematical, with no algorithmic complexity claim.",
    "source": [
      "urn:csabs:source/istqb-ctfl-4-0-1",
      "urn:csabs:source/mathlib-finite-ranking-pinned"
    ],
    "sourceLocator": "§4.2.3, printed p.41, coverage as covered finite obligations over feasible obligations; adapted by replacing rule identities with explicit verdict labels, not an ISTQB-named criterion.",
    "sourceNote": "Definition adapted to the explicitly stated catalog carrier and operations.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/VerdictCoverage-finite-observation-definition",
    "type": "Axiom",
    "name": "finite-observation-definition",
    "statement": "Coverage is finite-set observation against a declared target universe.",
    "description": "Coverage is finite-set observation against a declared target universe.",
    "formalStatement": "U,O⊆V finite; H=U∩O; missing=U∖O; full⇔H=U; ratio=none if |U|=0 else some(|H|/|U|).",
    "assumptions": [
      "Verdict carrier V has exact equality. U is an explicitly declared finite target set, O a finite set of observed labels; repeats are ignored and labels outside U do not contribute. Empty U gives full coverage vacuously but an undefined numeric ratio (none). Otherwise the exact rational fraction is in [0,1]. Targets must be justified separately as feasible outcomes or required declared categories; this model cannot certify feasibility. For a decision table, choose U=v(F) and O=v(E(S)) for label coverage; choose target F and observations E(S) instead for rule coverage. F is the feasible rule set. Many rules may share a label. No statistical confidence, input-space, branch, MC/DC, proof coverage or outcome-correctness guarantee follows from label coverage."
    ],
    "appliesTo": [
      "urn:csabs:concept/VerdictCoverage"
    ],
    "reviewStatus": "Editorial statement; consult the separate Lean witness binding for exact proof scope.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/istqb-ctfl-4-0-1",
      "urn:csabs:source/mathlib-finite-ranking-pinned"
    ],
    "sourceLocator": "§4.2.3, printed p.41, coverage as covered finite obligations over feasible obligations; adapted by replacing rule identities with explicit verdict labels, not an ISTQB-named criterion.",
    "sourceNote": "Definition adapted to the explicitly stated catalog carrier and operations.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:law/VerdictCoverage-covered-count-bound",
    "type": "Law",
    "name": "covered-count-bound",
    "statement": "The number of covered labels cannot exceed the number of required labels.",
    "description": "The number of covered labels cannot exceed the number of required labels.",
    "formalStatement": "|U∩O|≤|U|.",
    "assumptions": [
      "Verdict carrier V has exact equality. U is an explicitly declared finite target set, O a finite set of observed labels; repeats are ignored and labels outside U do not contribute. Empty U gives full coverage vacuously but an undefined numeric ratio (none). Otherwise the exact rational fraction is in [0,1]. Targets must be justified separately as feasible outcomes or required declared categories; this model cannot certify feasibility. For a decision table, choose U=v(F) and O=v(E(S)) for label coverage; choose target F and observations E(S) instead for rule coverage. F is the feasible rule set. Many rules may share a label. No statistical confidence, input-space, branch, MC/DC, proof coverage or outcome-correctness guarantee follows from label coverage."
    ],
    "appliesTo": [
      "urn:csabs:concept/VerdictCoverage"
    ],
    "reviewStatus": "Editorial statement; consult the separate Lean witness binding for exact proof scope.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/istqb-ctfl-4-0-1",
      "urn:csabs:source/mathlib-finite-ranking-pinned"
    ],
    "sourceLocator": "§4.2.3, printed p.41, coverage as covered finite obligations over feasible obligations; adapted by replacing rule identities with explicit verdict labels, not an ISTQB-named criterion.",
    "sourceNote": "Derived from the directly linked defining premises; Intersection is a subset of U; cardinality is monotone for finite subsets.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/VerdictCoverage-finite-observation-definition"
    ],
    "proofSketch": "Intersection is a subset of U; cardinality is monotone for finite subsets.",
    "leanFormulation": "∀ {V} (m : Catalog.VerdictCoverage V), (Catalog.coveredVerdicts m).card ≤ m.target.card",
    "formulationSource": "urn:csabs:source/local-lean-RetrievalDecisions",
    "formulationLocator": "Catalog.verdict_count_bound",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Finset V target and observed with exact equality; coveredVerdicts is intersection; verdictRatio is Option ℚ with none exactly on zero target cardinality. Rule instances use V=R; verdict instances use the image of rule outcomes.",
    "leanModelLimitations": "Proves the displayed Lean proposition only; semantic correspondence is reviewed metadata. No software implementation correctness or deductive-system completeness is asserted.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/VerdictCoverage-finite-observation-definition\": \"Direct defining premise interpreted using Finset V target and observed with exact equality; coveredVerdicts is intersection; verdictRatio is Option ℚ with none exactly on zero target cardinality. Rule instances use V=R; verdict instances use the image of rule outcomes.\"}"
  },
  {
    "id": "urn:csabs:law/VerdictCoverage-empty-target-ratio",
    "type": "Law",
    "name": "empty-target-ratio",
    "statement": "An empty target has no numeric coverage ratio.",
    "description": "An empty target has no numeric coverage ratio.",
    "formalStatement": "ratio(∅,O)=none; full(∅,O)=true.",
    "assumptions": [
      "Verdict carrier V has exact equality. U is an explicitly declared finite target set, O a finite set of observed labels; repeats are ignored and labels outside U do not contribute. Empty U gives full coverage vacuously but an undefined numeric ratio (none). Otherwise the exact rational fraction is in [0,1]. Targets must be justified separately as feasible outcomes or required declared categories; this model cannot certify feasibility. For a decision table, choose U=v(F) and O=v(E(S)) for label coverage; choose target F and observations E(S) instead for rule coverage. F is the feasible rule set. Many rules may share a label. No statistical confidence, input-space, branch, MC/DC, proof coverage or outcome-correctness guarantee follows from label coverage."
    ],
    "appliesTo": [
      "urn:csabs:concept/VerdictCoverage"
    ],
    "reviewStatus": "Editorial statement; consult the separate Lean witness binding for exact proof scope.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/istqb-ctfl-4-0-1",
      "urn:csabs:source/mathlib-finite-ranking-pinned"
    ],
    "sourceLocator": "§4.2.3, printed p.41, coverage as covered finite obligations over feasible obligations; adapted by replacing rule identities with explicit verdict labels, not an ISTQB-named criterion.",
    "sourceNote": "Derived from the directly linked defining premises; The denominator cardinality is zero, selecting none. Vacuous fullness follows separately from the subset definition; the registered witness is for the Option-valued ratio only.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/VerdictCoverage-finite-observation-definition"
    ],
    "proofSketch": "The denominator cardinality is zero, selecting none. Vacuous fullness follows separately from the subset definition; the registered witness is for the Option-valued ratio only.",
    "leanFormulation": "∀ {V} (observed : Finset V), Catalog.verdictRatio (⟨∅, observed⟩ : Catalog.VerdictCoverage V) = none",
    "formulationSource": "urn:csabs:source/local-lean-RetrievalDecisions",
    "formulationLocator": "Catalog.verdict_empty_target",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Finset V target and observed with exact equality; coveredVerdicts is intersection; verdictRatio is Option ℚ with none exactly on zero target cardinality. Rule instances use V=R; verdict instances use the image of rule outcomes.",
    "leanModelLimitations": "Proves the displayed Lean proposition only; semantic correspondence is reviewed metadata. No software implementation correctness or deductive-system completeness is asserted.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/VerdictCoverage-finite-observation-definition\": \"Direct defining premise interpreted using Finset V target and observed with exact equality; coveredVerdicts is intersection; verdictRatio is Option ℚ with none exactly on zero target cardinality. Rule instances use V=R; verdict instances use the image of rule outcomes.\"}"
  },
  {
    "id": "urn:csabs:theorem/VerdictCoverage-intersection-model-satisfaction",
    "type": "Theorem",
    "name": "intersection-model-satisfaction",
    "statement": "The finite-intersection realization counts only required and observed labels.",
    "description": "The finite-intersection realization counts only required and observed labels.",
    "formalStatement": "For all finite U,O, H=U∩O is a subset of both U and O.",
    "assumptions": [
      "Verdict carrier V has exact equality. U is an explicitly declared finite target set, O a finite set of observed labels; repeats are ignored and labels outside U do not contribute. Empty U gives full coverage vacuously but an undefined numeric ratio (none). Otherwise the exact rational fraction is in [0,1]. Targets must be justified separately as feasible outcomes or required declared categories; this model cannot certify feasibility. For a decision table, choose U=v(F) and O=v(E(S)) for label coverage; choose target F and observations E(S) instead for rule coverage. F is the feasible rule set. Many rules may share a label. No statistical confidence, input-space, branch, MC/DC, proof coverage or outcome-correctness guarantee follows from label coverage."
    ],
    "appliesTo": [
      "urn:csabs:concept/VerdictCoverage"
    ],
    "reviewStatus": "Editorial statement; consult the separate Lean witness binding for exact proof scope.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/istqb-ctfl-4-0-1",
      "urn:csabs:source/mathlib-finite-ranking-pinned"
    ],
    "sourceLocator": "§4.2.3, printed p.41, coverage as covered finite obligations over feasible obligations; adapted by replacing rule identities with explicit verdict labels, not an ISTQB-named criterion.",
    "sourceNote": "Derived from the directly linked defining premises; Construct H by finite intersection and use its two subset projections; arbitrary finite targets and observations realize the basis without assumed coverage-law fields.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/VerdictCoverage-finite-observation-definition"
    ],
    "proofSketch": "Construct H by finite intersection and use its two subset projections; arbitrary finite targets and observations realize the basis without assumed coverage-law fields.",
    "leanFormulation": "∀ {V} (m : Catalog.VerdictCoverage V), Catalog.coveredVerdicts m ⊆ m.target ∧ Catalog.coveredVerdicts m ⊆ m.observed",
    "formulationSource": "urn:csabs:source/local-lean-RetrievalDecisions",
    "formulationLocator": "Catalog.verdict_model_satisfaction",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Finset V target and observed with exact equality; coveredVerdicts is intersection; verdictRatio is Option ℚ with none exactly on zero target cardinality. Rule instances use V=R; verdict instances use the image of rule outcomes.",
    "leanModelLimitations": "Proves the displayed Lean proposition only; semantic correspondence is reviewed metadata. No software implementation correctness or deductive-system completeness is asserted.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/VerdictCoverage-finite-observation-definition\": \"Direct defining premise interpreted using Finset V target and observed with exact equality; coveredVerdicts is intersection; verdictRatio is Option ℚ with none exactly on zero target cardinality. Rule instances use V=R; verdict instances use the image of rule outcomes.\"}"
  },
  {
    "id": "urn:csabs:theorem/VerdictCoverage-verdict-does-not-imply-rule-coverage",
    "type": "Theorem",
    "name": "verdict-does-not-imply-rule-coverage",
    "statement": "Full verdict-label coverage need not cover every feasible rule.",
    "description": "Full verdict-label coverage need not cover every feasible rule.",
    "formalStatement": "There exists a unique-hit table and suite S with v(E(S))=v(F) but E(S)≠F.",
    "assumptions": [
      "Verdict carrier V has exact equality. U is an explicitly declared finite target set, O a finite set of observed labels; repeats are ignored and labels outside U do not contribute. Empty U gives full coverage vacuously but an undefined numeric ratio (none). Otherwise the exact rational fraction is in [0,1]. Targets must be justified separately as feasible outcomes or required declared categories; this model cannot certify feasibility. For a decision table, choose U=v(F) and O=v(E(S)) for label coverage; choose target F and observations E(S) instead for rule coverage. F is the feasible rule set. Many rules may share a label. No statistical confidence, input-space, branch, MC/DC, proof coverage or outcome-correctness guarantee follows from label coverage."
    ],
    "appliesTo": [
      "urn:csabs:concept/VerdictCoverage"
    ],
    "reviewStatus": "Editorial statement; consult the separate Lean witness binding for exact proof scope.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/istqb-ctfl-4-0-1",
      "urn:csabs:source/mathlib-finite-ranking-pinned"
    ],
    "sourceLocator": "§4.2.3, printed p.41, coverage as covered finite obligations over feasible obligations; adapted by replacing rule identities with explicit verdict labels, not an ISTQB-named criterion.",
    "sourceNote": "Derived from the directly linked defining premises; Use two feasible Boolean identity rules with the same Unit verdict. The singleton suite {false} observes the only verdict but leaves the true rule unexercised. This is a counterexample to the converse; full feasible-rule coverage does imply full feasible-verdict coverage by taking images.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/VerdictCoverage-finite-observation-definition",
      "urn:csabs:axiom/DecisionTable-unique-hit-rules",
      "urn:csabs:axiom/DecisionTable-feasible-rule-coverage"
    ],
    "proofSketch": "Use two feasible Boolean identity rules with the same Unit verdict. The singleton suite {false} observes the only verdict but leaves the true rule unexercised. This is a counterexample to the converse; full feasible-rule coverage does imply full feasible-verdict coverage by taking images.",
    "leanFormulation": "(Catalog.tableExercised Catalog.booleanTable {false}).image Catalog.booleanTable.verdict = (Catalog.tableFeasible Catalog.booleanTable).image Catalog.booleanTable.verdict ∧ Catalog.tableExercised Catalog.booleanTable {false} ≠ Catalog.tableFeasible Catalog.booleanTable",
    "formulationSource": "urn:csabs:source/local-lean-RetrievalDecisions",
    "formulationLocator": "Catalog.verdict_not_rule_coverage",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Finset V target and observed with exact equality; coveredVerdicts is intersection; verdictRatio is Option ℚ with none exactly on zero target cardinality. Rule instances use V=R; verdict instances use the image of rule outcomes.",
    "leanModelLimitations": "Proves the displayed Lean proposition only; semantic correspondence is reviewed metadata. No software implementation correctness or deductive-system completeness is asserted.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/DecisionTable-feasible-rule-coverage\": \"Direct defining premise interpreted using Finset V target and observed with exact equality; coveredVerdicts is intersection; verdictRatio is Option ℚ with none exactly on zero target cardinality. Rule instances use V=R; verdict instances use the image of rule outcomes.\", \"urn:csabs:axiom/DecisionTable-unique-hit-rules\": \"Direct defining premise interpreted using Finset V target and observed with exact equality; coveredVerdicts is intersection; verdictRatio is Option ℚ with none exactly on zero target cardinality. Rule instances use V=R; verdict instances use the image of rule outcomes.\", \"urn:csabs:axiom/VerdictCoverage-finite-observation-definition\": \"Direct defining premise interpreted using Finset V target and observed with exact equality; coveredVerdicts is intersection; verdictRatio is Option ℚ with none exactly on zero target cardinality. Rule instances use V=R; verdict instances use the image of rule outcomes.\"}"
  }
]
```
<!-- graph-record:end -->
