# Finite score-ranked retrieval

A finite candidate set scored for a query and returned in descending score order, with a fixed total order on identifiers resolving score ties.

**Notation:** rank(q,C)=sort C by (-s(q,d),d); top(k,q,C)=take(k,rank(q,C)).

**Stable ID:** `urn:csabs:concept/RankedRetrieval`

**Categories:** Information theory

**Kind:** Mathematical structure

**Prerequisites:** [Finite set collection](FiniteSet.md), [Total Order](TotalOrder.md), [Finite sequence (List datatype)](Sequence.md)

## Backlinks

- [BM25 score model (positive-IDF, normalized single-field profile)](BM25.md) — `requiresConcept`
- [BM25 score model (positive-IDF, normalized single-field profile)](BM25.md) — `specializationOf`

## Mathematical formulation

rank(q,C)=sort C by (-s(q,d),d); top(k,q,C)=take(k,rank(q,C)). Document identities D have exact equality and a fixed total order; C is a finite subset of D, possibly empty. Scores are exact real numbers, so NaN, infinities and rounding are excluded. The query carrier is arbitrary; for fixed q the scorer is D→ℝ. Higher scores precede lower ones; equal scores use ascending identifier order. Ranking returns every candidate exactly once, including zero or negative scores; top-k has length min(k,|C|), with k∈ℕ. No relevance threshold, retrieval-quality guarantee or probability calibration is assumed.

**Lean formulation** (in its source module context):

```lean
abbrev RankedRetrieval (D : Type u) := D → ℝ
```

**Source:** [`Catalog.RankedRetrieval`](../lean/Catalog/RetrievalDecisions.lean); consulted 2026-11-20.

**Scope:** model

**Interpretation:** For a fixed query, D→ℝ supplies scores; D has LinearOrder. retrievalKeys sorts the finite image d↦toLex(-score d,d) using exact lexicographic order. Document identities are the second coordinates.

**Limits:** Witness establishes sorted, duplicate-free key enumeration with exact finite-set membership. Projecting identifiers and taking prefixes are mathematical interface operations, without separate Lean witnesses for top-k length or relevance quality.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Finite candidate identity set; total real scoring; lexicographic descending-score/ascending-identifier ordering; exact permutation and prefix selection.

**basisKind:** defined-structure

**basisScope:** Document identities D have exact equality and a fixed total order; C is a finite subset of D, possibly empty. Scores are exact real numbers, so NaN, infinities and rounding are excluded. The query carrier is arbitrary; for fixed q the scorer is D→ℝ. Higher scores precede lower ones; equal scores use ascending identifier order. Ranking returns every candidate exactly once, including zero or negative scores; top-k has length min(k,|C|), with k∈ℕ. No relevance threshold, retrieval-quality guarantee or probability calibration is assumed.

**verificationObligation:** Instantiate the stated carrier, equality, operation and definedness conventions. Typed links do not transfer axioms.

**reviewStatus:** Editorial mathematical interface review; only individually registered witnesses have compiler evidence.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-RankedRetrieval-score"></a>

### score

`urn:csabs:operation/RankedRetrieval-score`

**signature:** score : Q×D→ℝ

**description:** Return the declared real score for the query and document.

**precondition:** Inputs belong to the displayed carriers.

**postcondition:** Return the declared real score for the query and document.

**totality:** Total on the stated typed domain; predicates and sets are mathematical, with no algorithmic complexity claim.

**source:** [Mathlib finite sorting, lexicographic order and cardinality at the pinned revision](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted Data/Finset/Sort.lean (sort, pairwise_sort, sort_nodup, sort_toFinset), Order/Prod/Lex/Basic.lean (toLex_le_toLex) and Data/Finset/Card.lean (card_le_card).

**sourceLocator:** Data/Finset/Sort.lean: sort, pairwise_sort, sort_nodup, sort_toFinset; Order/Prod/Lex/Basic.lean: toLex_le_toLex; pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679

**sourceNote:** Definition adapted to the explicitly stated catalog carrier and operations.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-RankedRetrieval-rank"></a>

### rank

`urn:csabs:operation/RankedRetrieval-rank`

**signature:** rank : Q×FinSet(D)→List(D)

**description:** Return every candidate exactly once in descending score order; use ascending document identity to break ties.

**precondition:** Inputs belong to the displayed carriers.

**postcondition:** Return every candidate exactly once in descending score order; use ascending document identity to break ties.

**totality:** Total on the stated typed domain; predicates and sets are mathematical, with no algorithmic complexity claim.

**source:** [Mathlib finite sorting, lexicographic order and cardinality at the pinned revision](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted Data/Finset/Sort.lean (sort, pairwise_sort, sort_nodup, sort_toFinset), Order/Prod/Lex/Basic.lean (toLex_le_toLex) and Data/Finset/Card.lean (card_le_card).

**sourceLocator:** Data/Finset/Sort.lean: sort, pairwise_sort, sort_nodup, sort_toFinset; Order/Prod/Lex/Basic.lean: toLex_le_toLex; pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679

**sourceNote:** Definition adapted to the explicitly stated catalog carrier and operations.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-RankedRetrieval-top-k"></a>

### top-k

`urn:csabs:operation/RankedRetrieval-top-k`

**signature:** top : ℕ×Q×FinSet(D)→List(D)

**description:** Take the first min(k,|C|) entries of rank; k=0 or C=∅ returns [].

**precondition:** Inputs belong to the displayed carriers.

**postcondition:** Take the first min(k,|C|) entries of rank; k=0 or C=∅ returns [].

**totality:** Total on the stated typed domain; predicates and sets are mathematical, with no algorithmic complexity claim.

**source:** [Mathlib finite sorting, lexicographic order and cardinality at the pinned revision](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted Data/Finset/Sort.lean (sort, pairwise_sort, sort_nodup, sort_toFinset), Order/Prod/Lex/Basic.lean (toLex_le_toLex) and Data/Finset/Card.lean (card_le_card).

**sourceLocator:** Data/Finset/Sort.lean: sort, pairwise_sort, sort_nodup, sort_toFinset; Order/Prod/Lex/Basic.lean: toLex_le_toLex; pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679

**sourceNote:** Definition adapted to the explicitly stated catalog carrier and operations.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-RankedRetrieval-ranking-definition"></a>

### ranking-definition

`urn:csabs:axiom/RankedRetrieval-ranking-definition`

**statement:** The result is the unique sorted permutation of the finite candidate set using score and identifier keys.

**description:** The result is the unique sorted permutation of the finite candidate set using score and identifier keys.

**formalStatement:** key_q(d)=(-score(q,d),d); rank(q,C) has no duplicates, underlying set C, and nondecreasing lexicographic keys; top(k,q,C)=take(k,rank(q,C)).

**assumptions:** Document identities D have exact equality and a fixed total order; C is a finite subset of D, possibly empty. Scores are exact real numbers, so NaN, infinities and rounding are excluded. The query carrier is arbitrary; for fixed q the scorer is D→ℝ. Higher scores precede lower ones; equal scores use ascending identifier order. Ranking returns every candidate exactly once, including zero or negative scores; top-k has length min(k,|C|), with k∈ℕ. No relevance threshold, retrieval-quality guarantee or probability calibration is assumed.

**reviewStatus:** Editorial statement; consult the separate Lean witness binding for exact proof scope.

**notationLanguage:** informal mathematical Unicode

**source:** [Mathlib finite sorting, lexicographic order and cardinality at the pinned revision](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted Data/Finset/Sort.lean (sort, pairwise_sort, sort_nodup, sort_toFinset), Order/Prod/Lex/Basic.lean (toLex_le_toLex) and Data/Finset/Card.lean (card_le_card).

**sourceLocator:** Data/Finset/Sort.lean: sort, pairwise_sort, sort_nodup, sort_toFinset; Order/Prod/Lex/Basic.lean: toLex_le_toLex; pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679

**sourceNote:** Definition adapted to the explicitly stated catalog carrier and operations.

**provenanceKind:** adapted

**ruleRole:** defining-rule

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-RankedRetrieval-finite-sorting-model-satisfaction"></a>

### finite-sorting-model-satisfaction

`urn:csabs:theorem/RankedRetrieval-finite-sorting-model-satisfaction`

**statement:** Finite lexicographic key sorting satisfies uniqueness of entries, ordered output and exact membership.

**description:** Finite lexicographic key sorting satisfies uniqueness of entries, ordered output and exact membership.

**formalStatement:** For every finite C and real scorer, sorting {(-s(d),d) | d∈C} yields a duplicate-free ordered list whose underlying set is exactly that key set.

**assumptions:** Document identities D have exact equality and a fixed total order; C is a finite subset of D, possibly empty. Scores are exact real numbers, so NaN, infinities and rounding are excluded. The query carrier is arbitrary; for fixed q the scorer is D→ℝ. Higher scores precede lower ones; equal scores use ascending identifier order. Ranking returns every candidate exactly once, including zero or negative scores; top-k has length min(k,|C|), with k∈ℕ. No relevance threshold, retrieval-quality guarantee or probability calibration is assumed.

**reviewStatus:** Editorial statement; consult the separate Lean witness binding for exact proof scope.

**notationLanguage:** informal mathematical Unicode

**source:** [Mathlib finite sorting, lexicographic order and cardinality at the pinned revision](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted Data/Finset/Sort.lean (sort, pairwise_sort, sort_nodup, sort_toFinset), Order/Prod/Lex/Basic.lean (toLex_le_toLex) and Data/Finset/Card.lean (card_le_card).

**sourceLocator:** Data/Finset/Sort.lean: sort, pairwise_sort, sort_nodup, sort_toFinset; Order/Prod/Lex/Basic.lean: toLex_le_toLex; pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679

**sourceNote:** Derived from the directly linked defining premises; Apply finite sorting membership, pairwise ordering and no-duplicate theorems. The key is injective because its second coordinate is the original document identity; identifiers recover an exact candidate permutation.

**provenanceKind:** derived

**dependsOn:** [ranking-definition](RankedRetrieval.md#node-urn-csabs-axiom-RankedRetrieval-ranking-definition)

**proofSketch:** Apply finite sorting membership, pairwise ordering and no-duplicate theorems. The key is injective because its second coordinate is the original document identity; identifiers recover an exact candidate permutation.

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {D : Type u} [LinearOrder D] (s : Finset D) (score : Catalog.RankedRetrieval D), (Catalog.retrievalKeys s score).Nodup ∧ (Catalog.retrievalKeys s score).Pairwise (· ≤ ·) ∧ (Catalog.retrievalKeys s score).toFinset = s.image (fun d => toLex (-score d, d))
```

**Source:** [`Catalog.retrieval_model_satisfaction`](../lean/Catalog/RetrievalDecisions.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** For a fixed query, D→ℝ supplies scores; D has LinearOrder. retrievalKeys sorts the finite image d↦toLex(-score d,d) using exact lexicographic order. Document identities are the second coordinates.

**Limits:** Proves the displayed Lean proposition only; semantic correspondence is reviewed metadata. No software implementation correctness or deductive-system completeness is asserted.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/RankedRetrieval-ranking-definition": "Direct defining premise interpreted using For a fixed query, D→ℝ supplies scores; D has LinearOrder. retrievalKeys sorts the finite image d↦toLex(-score d,d) using exact lexicographic order. Document identities are the second coordinates."
}
```

## Concept provenance

- [Mathlib finite sorting, lexicographic order and cardinality at the pinned revision](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted Data/Finset/Sort.lean (sort, pairwise_sort, sort_nodup, sort_toFinset), Order/Prod/Lex/Basic.lean (toLex_le_toLex) and Data/Finset/Card.lean (card_le_card).

**sourceLocator:** Data/Finset/Sort.lean: sort, pairwise_sort, sort_nodup, sort_toFinset; Order/Prod/Lex/Basic.lean: toLex_le_toLex; pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679

**sourceNote:** Definition adapted to the explicitly stated catalog carrier and operations.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/RankedRetrieval",
    "type": "Concept",
    "shortForm": "RankedRetrieval",
    "fullName": "Finite score-ranked retrieval",
    "definition": "A finite candidate set scored for a query and returned in descending score order, with a fixed total order on identifiers resolving score ties.",
    "notation": "rank(q,C)=sort C by (-s(q,d),d); top(k,q,C)=take(k,rank(q,C)).",
    "category": [
      "urn:csabs:category/information-theory"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "synonyms": [
      "Score-ranked retrieval",
      "Finite ranked search",
      "Deterministic top-k retrieval"
    ],
    "axiomBasis": "Finite candidate identity set; total real scoring; lexicographic descending-score/ascending-identifier ordering; exact permutation and prefix selection.",
    "basisKind": "defined-structure",
    "basisScope": "Document identities D have exact equality and a fixed total order; C is a finite subset of D, possibly empty. Scores are exact real numbers, so NaN, infinities and rounding are excluded. The query carrier is arbitrary; for fixed q the scorer is D→ℝ. Higher scores precede lower ones; equal scores use ascending identifier order. Ranking returns every candidate exactly once, including zero or negative scores; top-k has length min(k,|C|), with k∈ℕ. No relevance threshold, retrieval-quality guarantee or probability calibration is assumed.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial mathematical interface review; only individually registered witnesses have compiler evidence.",
    "verificationObligation": [
      "Instantiate the stated carrier, equality, operation and definedness conventions. Typed links do not transfer axioms."
    ],
    "mathematicalFormulation": "rank(q,C)=sort C by (-s(q,d),d); top(k,q,C)=take(k,rank(q,C)). Document identities D have exact equality and a fixed total order; C is a finite subset of D, possibly empty. Scores are exact real numbers, so NaN, infinities and rounding are excluded. The query carrier is arbitrary; for fixed q the scorer is D→ℝ. Higher scores precede lower ones; equal scores use ascending identifier order. Ranking returns every candidate exactly once, including zero or negative scores; top-k has length min(k,|C|), with k∈ℕ. No relevance threshold, retrieval-quality guarantee or probability calibration is assumed.",
    "hasOperation": [
      "urn:csabs:operation/RankedRetrieval-score",
      "urn:csabs:operation/RankedRetrieval-rank",
      "urn:csabs:operation/RankedRetrieval-top-k"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/RankedRetrieval-ranking-definition"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/RankedRetrieval-finite-sorting-model-satisfaction"
    ],
    "source": [
      "urn:csabs:source/mathlib-finite-ranking-pinned"
    ],
    "sourceLocator": "Data/Finset/Sort.lean: sort, pairwise_sort, sort_nodup, sort_toFinset; Order/Prod/Lex/Basic.lean: toLex_le_toLex; pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679",
    "sourceNote": "Definition adapted to the explicitly stated catalog carrier and operations.",
    "provenanceKind": "adapted",
    "requiresConcept": [
      "urn:csabs:concept/FiniteSet",
      "urn:csabs:concept/TotalOrder",
      "urn:csabs:concept/Sequence"
    ],
    "leanFormulation": "abbrev RankedRetrieval (D : Type u) := D → ℝ",
    "formulationSource": "urn:csabs:source/local-lean-RetrievalDecisions",
    "formulationLocator": "Catalog.RankedRetrieval",
    "formulationScope": "model",
    "leanModelMapping": "For a fixed query, D→ℝ supplies scores; D has LinearOrder. retrievalKeys sorts the finite image d↦toLex(-score d,d) using exact lexicographic order. Document identities are the second coordinates.",
    "leanModelLimitations": "Witness establishes sorted, duplicate-free key enumeration with exact finite-set membership. Projecting identifiers and taking prefixes are mathematical interface operations, without separate Lean witnesses for top-k length or relevance quality."
  },
  {
    "id": "urn:csabs:operation/RankedRetrieval-score",
    "type": "Operation",
    "name": "score",
    "signature": "score : Q×D→ℝ",
    "description": "Return the declared real score for the query and document.",
    "concept": "urn:csabs:concept/RankedRetrieval",
    "precondition": "Inputs belong to the displayed carriers.",
    "postcondition": "Return the declared real score for the query and document.",
    "totality": "Total on the stated typed domain; predicates and sets are mathematical, with no algorithmic complexity claim.",
    "source": [
      "urn:csabs:source/mathlib-finite-ranking-pinned"
    ],
    "sourceLocator": "Data/Finset/Sort.lean: sort, pairwise_sort, sort_nodup, sort_toFinset; Order/Prod/Lex/Basic.lean: toLex_le_toLex; pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679",
    "sourceNote": "Definition adapted to the explicitly stated catalog carrier and operations.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/RankedRetrieval-rank",
    "type": "Operation",
    "name": "rank",
    "signature": "rank : Q×FinSet(D)→List(D)",
    "description": "Return every candidate exactly once in descending score order; use ascending document identity to break ties.",
    "concept": "urn:csabs:concept/RankedRetrieval",
    "precondition": "Inputs belong to the displayed carriers.",
    "postcondition": "Return every candidate exactly once in descending score order; use ascending document identity to break ties.",
    "totality": "Total on the stated typed domain; predicates and sets are mathematical, with no algorithmic complexity claim.",
    "source": [
      "urn:csabs:source/mathlib-finite-ranking-pinned"
    ],
    "sourceLocator": "Data/Finset/Sort.lean: sort, pairwise_sort, sort_nodup, sort_toFinset; Order/Prod/Lex/Basic.lean: toLex_le_toLex; pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679",
    "sourceNote": "Definition adapted to the explicitly stated catalog carrier and operations.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/RankedRetrieval-top-k",
    "type": "Operation",
    "name": "top-k",
    "signature": "top : ℕ×Q×FinSet(D)→List(D)",
    "description": "Take the first min(k,|C|) entries of rank; k=0 or C=∅ returns [].",
    "concept": "urn:csabs:concept/RankedRetrieval",
    "precondition": "Inputs belong to the displayed carriers.",
    "postcondition": "Take the first min(k,|C|) entries of rank; k=0 or C=∅ returns [].",
    "totality": "Total on the stated typed domain; predicates and sets are mathematical, with no algorithmic complexity claim.",
    "source": [
      "urn:csabs:source/mathlib-finite-ranking-pinned"
    ],
    "sourceLocator": "Data/Finset/Sort.lean: sort, pairwise_sort, sort_nodup, sort_toFinset; Order/Prod/Lex/Basic.lean: toLex_le_toLex; pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679",
    "sourceNote": "Definition adapted to the explicitly stated catalog carrier and operations.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/RankedRetrieval-ranking-definition",
    "type": "Axiom",
    "name": "ranking-definition",
    "statement": "The result is the unique sorted permutation of the finite candidate set using score and identifier keys.",
    "description": "The result is the unique sorted permutation of the finite candidate set using score and identifier keys.",
    "formalStatement": "key_q(d)=(-score(q,d),d); rank(q,C) has no duplicates, underlying set C, and nondecreasing lexicographic keys; top(k,q,C)=take(k,rank(q,C)).",
    "assumptions": [
      "Document identities D have exact equality and a fixed total order; C is a finite subset of D, possibly empty. Scores are exact real numbers, so NaN, infinities and rounding are excluded. The query carrier is arbitrary; for fixed q the scorer is D→ℝ. Higher scores precede lower ones; equal scores use ascending identifier order. Ranking returns every candidate exactly once, including zero or negative scores; top-k has length min(k,|C|), with k∈ℕ. No relevance threshold, retrieval-quality guarantee or probability calibration is assumed."
    ],
    "appliesTo": [
      "urn:csabs:concept/RankedRetrieval"
    ],
    "reviewStatus": "Editorial statement; consult the separate Lean witness binding for exact proof scope.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/mathlib-finite-ranking-pinned"
    ],
    "sourceLocator": "Data/Finset/Sort.lean: sort, pairwise_sort, sort_nodup, sort_toFinset; Order/Prod/Lex/Basic.lean: toLex_le_toLex; pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679",
    "sourceNote": "Definition adapted to the explicitly stated catalog carrier and operations.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:theorem/RankedRetrieval-finite-sorting-model-satisfaction",
    "type": "Theorem",
    "name": "finite-sorting-model-satisfaction",
    "statement": "Finite lexicographic key sorting satisfies uniqueness of entries, ordered output and exact membership.",
    "description": "Finite lexicographic key sorting satisfies uniqueness of entries, ordered output and exact membership.",
    "formalStatement": "For every finite C and real scorer, sorting {(-s(d),d) | d∈C} yields a duplicate-free ordered list whose underlying set is exactly that key set.",
    "assumptions": [
      "Document identities D have exact equality and a fixed total order; C is a finite subset of D, possibly empty. Scores are exact real numbers, so NaN, infinities and rounding are excluded. The query carrier is arbitrary; for fixed q the scorer is D→ℝ. Higher scores precede lower ones; equal scores use ascending identifier order. Ranking returns every candidate exactly once, including zero or negative scores; top-k has length min(k,|C|), with k∈ℕ. No relevance threshold, retrieval-quality guarantee or probability calibration is assumed."
    ],
    "appliesTo": [
      "urn:csabs:concept/RankedRetrieval"
    ],
    "reviewStatus": "Editorial statement; consult the separate Lean witness binding for exact proof scope.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/mathlib-finite-ranking-pinned"
    ],
    "sourceLocator": "Data/Finset/Sort.lean: sort, pairwise_sort, sort_nodup, sort_toFinset; Order/Prod/Lex/Basic.lean: toLex_le_toLex; pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679",
    "sourceNote": "Derived from the directly linked defining premises; Apply finite sorting membership, pairwise ordering and no-duplicate theorems. The key is injective because its second coordinate is the original document identity; identifiers recover an exact candidate permutation.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/RankedRetrieval-ranking-definition"
    ],
    "proofSketch": "Apply finite sorting membership, pairwise ordering and no-duplicate theorems. The key is injective because its second coordinate is the original document identity; identifiers recover an exact candidate permutation.",
    "leanFormulation": "∀ {D : Type u} [LinearOrder D] (s : Finset D) (score : Catalog.RankedRetrieval D), (Catalog.retrievalKeys s score).Nodup ∧ (Catalog.retrievalKeys s score).Pairwise (· ≤ ·) ∧ (Catalog.retrievalKeys s score).toFinset = s.image (fun d => toLex (-score d, d))",
    "formulationSource": "urn:csabs:source/local-lean-RetrievalDecisions",
    "formulationLocator": "Catalog.retrieval_model_satisfaction",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "For a fixed query, D→ℝ supplies scores; D has LinearOrder. retrievalKeys sorts the finite image d↦toLex(-score d,d) using exact lexicographic order. Document identities are the second coordinates.",
    "leanModelLimitations": "Proves the displayed Lean proposition only; semantic correspondence is reviewed metadata. No software implementation correctness or deductive-system completeness is asserted.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/RankedRetrieval-ranking-definition\": \"Direct defining premise interpreted using For a fixed query, D→ℝ supplies scores; D has LinearOrder. retrievalKeys sorts the finite image d↦toLex(-score d,d) using exact lexicographic order. Document identities are the second coordinates.\"}"
  }
]
```
<!-- graph-record:end -->
