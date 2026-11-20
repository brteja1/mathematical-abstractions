# SQLite FTS5-style BM25 phrase and weighted-column profile

An exact-real adaptation of SQLite FTS5 BM25 over phrase hits and weighted columns, with unshifted raw IDF and its nonpositive-value replacement.

**Notation:** SQL(q,d)=−Σₚ IDF(p)·f(p,d)(k₁+1)/(f(p,d)+k₁(1−b+b|d|/avgdl))

**Stable ID:** `urn:csabs:concept/BM25FTS5`

**Categories:** Information theory

**Kind:** Mathematical structure

**Prerequisites:** [Finite set collection](FiniteSet.md), [Finite sequence (List datatype)](Sequence.md), [Finite score-ranked retrieval](RankedRetrieval.md)

**Related concepts:** [BM25 score model (positive-IDF, normalized single-field profile)](BM25.md)

## Backlinks

- [BM25 score model (positive-IDF, normalized single-field profile)](BM25.md) — `relatedConcept`
- [Finite score-ranked retrieval](RankedRetrieval.md) — `relatedConcept`

## Mathematical formulation

N=|C|; df(p)=|{d∈C : ∃c,occ(p,d,c)>0}|; raw=ln((N−df+.5)/(df+.5)); IDF=if raw≤0 then 10⁻⁶ else raw; f=Σc weight(c)occ(p,d,c). Finite nonempty corpus, at least one token per corpus document, finitely many columns, exact real arithmetic and token/phrase occurrence statistics supplied by the caller. Phrases may span multiple tokens within a column; matching and tokenization are external inputs. Default missing column weights are 1; extras are ignored. Use nonnegative finite real weights for scoring with the stated nonzero-denominator domain. k₁=6/5 and b=3/4. Document length sums tokens across all columns and average divides by corpus size. Raw log IDF is replaced by 10⁻⁶ exactly when nonpositive; a small positive raw IDF is retained. Query phrase occurrences retain multiplicity. SQL scores ascend; negated scores fit descending RankedRetrieval. No SQLite floating-point, tokenizer, SQL parser, NEAR, NOT or stable-tie behavior is proved. Empty phrase lists are mathematical extensions (AND universe, OR empty, score zero), not valid empty SQL MATCH syntax. Utility profile: Use supplied weight at column index, otherwise 1. Columns outside the schema are never summed.; f(p,d)=Σc weight(c)·occ(p,d,c); weights affect occurrence frequency, not document length or df.; raw=ln((N−df+.5)/(df+.5)); IDF=10⁻⁶ if raw≤0, otherwise raw. Do not use log(1+ratio), max(raw,epsilon), or the unclamped raw value.; Negative BM25 sum with k₁=1.2,b=.75 and numerator factor k₁+1; total token document length and corpus-wide average; lower score is better.; Candidates matching every listed phrase; restrict to corpus before ranking. Empty conjunction is the mathematical universe.; Candidates matching at least one listed phrase; empty disjunction is empty. Boolean candidate matching is separate from scoring.

**Lean formulation** (in its source module context):

```lean
structure BM25FTS5 (P : Type u) (D : Type v) (columns : Nat) where
  docs : Finset D
  nonempty : docs.Nonempty
  tokens : D → Fin columns → Nat
  positiveLength : ∀ d ∈ docs, 0 < ∑ c, tokens d c
  occurrences : P → D → Fin columns → Nat
```

**Source:** [`Catalog.BM25FTS5`](../lean/Catalog/FTS5Profile.lean); consulted 2026-11-20.

**Scope:** model

**Interpretation:** P phrase identities, D document identities, Fin n column indices, finite document set, natural token and phrase-occurrence counts, exact real weights/logarithms/scores. Statistics and tokenization are explicit inputs; negative SQL scores are mapped to descending relevance by negation.

**Limits:** Finite nonempty corpus, at least one token per corpus document, finitely many columns, exact real arithmetic and token/phrase occurrence statistics supplied by the caller. Phrases may span multiple tokens within a column; matching and tokenization are external inputs. Default missing column weights are 1; extras are ignored. Use nonnegative finite real weights for scoring with the stated nonzero-denominator domain. k₁=6/5 and b=3/4. Document length sums tokens across all columns and average divides by corpus size. Raw log IDF is replaced by 10⁻⁶ exactly when nonpositive; a small positive raw IDF is retained. Query phrase occurrences retain multiplicity. SQL scores ascend; negated scores fit descending RankedRetrieval. No SQLite floating-point, tokenizer, SQL parser, NEAR, NOT or stable-tie behavior is proved. Empty phrase lists are mathematical extensions (AND universe, OR empty, score zero), not valid empty SQL MATCH syntax.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Corpus/statistics profile and the explicit weighted-frequency, IDF-replacement and score definitions. Utility definitions are recorded separately; optional bottom, subtype and goal-relative conventions are conditional and do not strengthen the base carrier.

**basisKind:** defined-structure

**basisScope:** Finite nonempty corpus, at least one token per corpus document, finitely many columns, exact real arithmetic and token/phrase occurrence statistics supplied by the caller. Phrases may span multiple tokens within a column; matching and tokenization are external inputs. Default missing column weights are 1; extras are ignored. Use nonnegative finite real weights for scoring with the stated nonzero-denominator domain. k₁=6/5 and b=3/4. Document length sums tokens across all columns and average divides by corpus size. Raw log IDF is replaced by 10⁻⁶ exactly when nonpositive; a small positive raw IDF is retained. Query phrase occurrences retain multiplicity. SQL scores ascend; negated scores fit descending RankedRetrieval. No SQLite floating-point, tokenizer, SQL parser, NEAR, NOT or stable-tie behavior is proved. Empty phrase lists are mathematical extensions (AND universe, OR empty, score zero), not valid empty SQL MATCH syntax.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-BM25FTS5-column-weight"></a>

### column-weight

`urn:csabs:operation/BM25FTS5-column-weight`

**signature:** weight : Seq(ℝ)×ℕ→ℝ

**description:** Use supplied weight at column index, otherwise 1. Columns outside the schema are never summed.

**precondition:** Use the selected corpus, phrase-statistics and exact-real profile; scoring document lies in the corpus; weights nonnegative and denominator nonzero.

**postcondition:** Use supplied weight at column index, otherwise 1. Columns outside the schema are never summed.

**totality:** Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.

**source:** [SQLite FTS5 documentation and BM25 auxiliary implementation](https://www.sqlite.org/fts5.html); citation: SQLite project, FTS5 Extension §§3.7, 5.1.1; ext/fts5/fts5_aux.c, https://raw.githubusercontent.com/sqlite/sqlite/master/ext/fts5/fts5_aux.c, consulted 2026-11-20. This consultation URL is not a dependency pin.; accessedOn: 2026-11-20; sourceRole: Consulted primary documentation sections 3.7 and 5.1.1, and fts5_aux.c fts5Bm25GetData/fts5Bm25Function. Exact-real mathematical adaptation; no binary floating-point or tokenizer equivalence claim.

**sourceLocator:** SQLite FTS5 §§3.7 and 5.1.1; fts5_aux.c: fts5Bm25GetData, fts5Bm25Function

**sourceNote:** Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-BM25FTS5-phrase-frequency"></a>

### phrase-frequency

`urn:csabs:operation/BM25FTS5-phrase-frequency`

**signature:** frequency : Phrase×Document→ℝ

**description:** f(p,d)=Σc weight(c)·occ(p,d,c); weights affect occurrence frequency, not document length or df.

**precondition:** Use the selected corpus, phrase-statistics and exact-real profile; scoring document lies in the corpus; weights nonnegative and denominator nonzero.

**postcondition:** f(p,d)=Σc weight(c)·occ(p,d,c); weights affect occurrence frequency, not document length or df.

**totality:** Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.

**source:** [SQLite FTS5 documentation and BM25 auxiliary implementation](https://www.sqlite.org/fts5.html); citation: SQLite project, FTS5 Extension §§3.7, 5.1.1; ext/fts5/fts5_aux.c, https://raw.githubusercontent.com/sqlite/sqlite/master/ext/fts5/fts5_aux.c, consulted 2026-11-20. This consultation URL is not a dependency pin.; accessedOn: 2026-11-20; sourceRole: Consulted primary documentation sections 3.7 and 5.1.1, and fts5_aux.c fts5Bm25GetData/fts5Bm25Function. Exact-real mathematical adaptation; no binary floating-point or tokenizer equivalence claim.

**sourceLocator:** SQLite FTS5 §§3.7 and 5.1.1; fts5_aux.c: fts5Bm25GetData, fts5Bm25Function

**sourceNote:** Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-BM25FTS5-idf"></a>

### idf

`urn:csabs:operation/BM25FTS5-idf`

**signature:** idf : Phrase→ℝ

**description:** raw=ln((N−df+.5)/(df+.5)); IDF=10⁻⁶ if raw≤0, otherwise raw. Do not use log(1+ratio), max(raw,epsilon), or the unclamped raw value.

**precondition:** Use the selected corpus, phrase-statistics and exact-real profile; scoring document lies in the corpus; weights nonnegative and denominator nonzero.

**postcondition:** raw=ln((N−df+.5)/(df+.5)); IDF=10⁻⁶ if raw≤0, otherwise raw. Do not use log(1+ratio), max(raw,epsilon), or the unclamped raw value.

**totality:** Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.

**source:** [SQLite FTS5 documentation and BM25 auxiliary implementation](https://www.sqlite.org/fts5.html); citation: SQLite project, FTS5 Extension §§3.7, 5.1.1; ext/fts5/fts5_aux.c, https://raw.githubusercontent.com/sqlite/sqlite/master/ext/fts5/fts5_aux.c, consulted 2026-11-20. This consultation URL is not a dependency pin.; accessedOn: 2026-11-20; sourceRole: Consulted primary documentation sections 3.7 and 5.1.1, and fts5_aux.c fts5Bm25GetData/fts5Bm25Function. Exact-real mathematical adaptation; no binary floating-point or tokenizer equivalence claim.

**sourceLocator:** SQLite FTS5 §§3.7 and 5.1.1; fts5_aux.c: fts5Bm25GetData, fts5Bm25Function

**sourceNote:** Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-BM25FTS5-sql-score"></a>

### sql-score

`urn:csabs:operation/BM25FTS5-sql-score`

**signature:** sqlScore : Seq(Phrase)×Document→ℝ

**description:** Negative BM25 sum with k₁=1.2,b=.75 and numerator factor k₁+1; total token document length and corpus-wide average; lower score is better.

**precondition:** Use the selected corpus, phrase-statistics and exact-real profile; scoring document lies in the corpus; weights nonnegative and denominator nonzero.

**postcondition:** Negative BM25 sum with k₁=1.2,b=.75 and numerator factor k₁+1; total token document length and corpus-wide average; lower score is better.

**totality:** Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.

**source:** [SQLite FTS5 documentation and BM25 auxiliary implementation](https://www.sqlite.org/fts5.html); citation: SQLite project, FTS5 Extension §§3.7, 5.1.1; ext/fts5/fts5_aux.c, https://raw.githubusercontent.com/sqlite/sqlite/master/ext/fts5/fts5_aux.c, consulted 2026-11-20. This consultation URL is not a dependency pin.; accessedOn: 2026-11-20; sourceRole: Consulted primary documentation sections 3.7 and 5.1.1, and fts5_aux.c fts5Bm25GetData/fts5Bm25Function. Exact-real mathematical adaptation; no binary floating-point or tokenizer equivalence claim.

**sourceLocator:** SQLite FTS5 §§3.7 and 5.1.1; fts5_aux.c: fts5Bm25GetData, fts5Bm25Function

**sourceNote:** Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-BM25FTS5-phrase-and"></a>

### phrase-and

`urn:csabs:operation/BM25FTS5-phrase-and`

**signature:** phraseAND : Seq(Phrase)→Set(Document)

**description:** Candidates matching every listed phrase; restrict to corpus before ranking. Empty conjunction is the mathematical universe.

**precondition:** Use the selected corpus, phrase-statistics and exact-real profile; scoring document lies in the corpus; weights nonnegative and denominator nonzero.

**postcondition:** Candidates matching every listed phrase; restrict to corpus before ranking. Empty conjunction is the mathematical universe.

**totality:** Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.

**source:** [SQLite FTS5 documentation and BM25 auxiliary implementation](https://www.sqlite.org/fts5.html); citation: SQLite project, FTS5 Extension §§3.7, 5.1.1; ext/fts5/fts5_aux.c, https://raw.githubusercontent.com/sqlite/sqlite/master/ext/fts5/fts5_aux.c, consulted 2026-11-20. This consultation URL is not a dependency pin.; accessedOn: 2026-11-20; sourceRole: Consulted primary documentation sections 3.7 and 5.1.1, and fts5_aux.c fts5Bm25GetData/fts5Bm25Function. Exact-real mathematical adaptation; no binary floating-point or tokenizer equivalence claim.

**sourceLocator:** SQLite FTS5 §§3.7 and 5.1.1; fts5_aux.c: fts5Bm25GetData, fts5Bm25Function

**sourceNote:** Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-BM25FTS5-phrase-or"></a>

### phrase-or

`urn:csabs:operation/BM25FTS5-phrase-or`

**signature:** phraseOR : Seq(Phrase)→Set(Document)

**description:** Candidates matching at least one listed phrase; empty disjunction is empty. Boolean candidate matching is separate from scoring.

**precondition:** Use the selected corpus, phrase-statistics and exact-real profile; scoring document lies in the corpus; weights nonnegative and denominator nonzero.

**postcondition:** Candidates matching at least one listed phrase; empty disjunction is empty. Boolean candidate matching is separate from scoring.

**totality:** Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.

**source:** [SQLite FTS5 documentation and BM25 auxiliary implementation](https://www.sqlite.org/fts5.html); citation: SQLite project, FTS5 Extension §§3.7, 5.1.1; ext/fts5/fts5_aux.c, https://raw.githubusercontent.com/sqlite/sqlite/master/ext/fts5/fts5_aux.c, consulted 2026-11-20. This consultation URL is not a dependency pin.; accessedOn: 2026-11-20; sourceRole: Consulted primary documentation sections 3.7 and 5.1.1, and fts5_aux.c fts5Bm25GetData/fts5Bm25Function. Exact-real mathematical adaptation; no binary floating-point or tokenizer equivalence claim.

**sourceLocator:** SQLite FTS5 §§3.7 and 5.1.1; fts5_aux.c: fts5Bm25GetData, fts5Bm25Function

**sourceNote:** Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-BM25FTS5-utility-profile"></a>

### Explicit utility operation definitions

`urn:csabs:axiom/BM25FTS5-utility-profile`

**statement:** Use supplied weight at column index, otherwise 1. Columns outside the schema are never summed.; f(p,d)=Σc weight(c)·occ(p,d,c); weights affect occurrence frequency, not document length or df.; raw=ln((N−df+.5)/(df+.5)); IDF=10⁻⁶ if raw≤0, otherwise raw. Do not use log(1+ratio), max(raw,epsilon), or the unclamped raw value.; Negative BM25 sum with k₁=1.2,b=.75 and numerator factor k₁+1; total token document length and corpus-wide average; lower score is better.; Candidates matching every listed phrase; restrict to corpus before ranking. Empty conjunction is the mathematical universe.; Candidates matching at least one listed phrase; empty disjunction is empty. Boolean candidate matching is separate from scoring.

**formalStatement:** weight : Seq(ℝ)×ℕ→ℝ: Use supplied weight at column index, otherwise 1. Columns outside the schema are never summed.; frequency : Phrase×Document→ℝ: f(p,d)=Σc weight(c)·occ(p,d,c); weights affect occurrence frequency, not document length or df.; idf : Phrase→ℝ: raw=ln((N−df+.5)/(df+.5)); IDF=10⁻⁶ if raw≤0, otherwise raw. Do not use log(1+ratio), max(raw,epsilon), or the unclamped raw value.; sqlScore : Seq(Phrase)×Document→ℝ: Negative BM25 sum with k₁=1.2,b=.75 and numerator factor k₁+1; total token document length and corpus-wide average; lower score is better.; phraseAND : Seq(Phrase)→Set(Document): Candidates matching every listed phrase; restrict to corpus before ranking. Empty conjunction is the mathematical universe.; phraseOR : Seq(Phrase)→Set(Document): Candidates matching at least one listed phrase; empty disjunction is empty. Boolean candidate matching is separate from scoring.

**assumptions:** Finite nonempty corpus, at least one token per corpus document, finitely many columns, exact real arithmetic and token/phrase occurrence statistics supplied by the caller. Phrases may span multiple tokens within a column; matching and tokenization are external inputs. Default missing column weights are 1; extras are ignored. Use nonnegative finite real weights for scoring with the stated nonzero-denominator domain. k₁=6/5 and b=3/4. Document length sums tokens across all columns and average divides by corpus size. Raw log IDF is replaced by 10⁻⁶ exactly when nonpositive; a small positive raw IDF is retained. Query phrase occurrences retain multiplicity. SQL scores ascend; negated scores fit descending RankedRetrieval. No SQLite floating-point, tokenizer, SQL parser, NEAR, NOT or stable-tie behavior is proved. Empty phrase lists are mathematical extensions (AND universe, OR empty, score zero), not valid empty SQL MATCH syntax.

**ruleRole:** defining-rule

**reviewStatus:** Definitions of a selected extension, not new foundational axioms; individual model and result witnesses are separate.

**source:** [SQLite FTS5 documentation and BM25 auxiliary implementation](https://www.sqlite.org/fts5.html); citation: SQLite project, FTS5 Extension §§3.7, 5.1.1; ext/fts5/fts5_aux.c, https://raw.githubusercontent.com/sqlite/sqlite/master/ext/fts5/fts5_aux.c, consulted 2026-11-20. This consultation URL is not a dependency pin.; accessedOn: 2026-11-20; sourceRole: Consulted primary documentation sections 3.7 and 5.1.1, and fts5_aux.c fts5Bm25GetData/fts5Bm25Function. Exact-real mathematical adaptation; no binary floating-point or tokenizer equivalence claim.

**sourceLocator:** SQLite FTS5 §§3.7 and 5.1.1; fts5_aux.c: fts5Bm25GetData, fts5Bm25Function

**sourceNote:** Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.

**provenanceKind:** adapted

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-BM25FTS5-phrase-boolean-equations"></a>

### phrase-boolean-equations

`urn:csabs:theorem/BM25FTS5-phrase-boolean-equations`

**statement:** AND(p::ps)=hit(p)∩AND(ps), OR(p::ps)=hit(p)∪OR(ps), AND([])=universe and OR([])=empty.

**formalStatement:** AND(p::ps)=hit(p)∩AND(ps), OR(p::ps)=hit(p)∪OR(ps), AND([])=universe and OR([])=empty.

**proofSketch:** Expand universal/existential membership over a cons list; apply finite corpus restriction separately.

**assumptions:** Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles.

**dependsOn:** [Explicit utility operation definitions](BM25FTS5.md#node-urn-csabs-axiom-BM25FTS5-utility-profile); [Explicit utility operation definitions](RankedRetrieval.md#node-urn-csabs-axiom-RankedRetrieval-utility-profile)

**reviewStatus:** Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.

**source:** [SQLite FTS5 documentation and BM25 auxiliary implementation](https://www.sqlite.org/fts5.html); citation: SQLite project, FTS5 Extension §§3.7, 5.1.1; ext/fts5/fts5_aux.c, https://raw.githubusercontent.com/sqlite/sqlite/master/ext/fts5/fts5_aux.c, consulted 2026-11-20. This consultation URL is not a dependency pin.; accessedOn: 2026-11-20; sourceRole: Consulted primary documentation sections 3.7 and 5.1.1, and fts5_aux.c fts5Bm25GetData/fts5Bm25Function. Exact-real mathematical adaptation; no binary floating-point or tokenizer equivalence claim.; Catalog FTS5Profile Lean formulations and proofs; path: lean/Catalog/FTS5Profile.lean; accessedOn: 2026-11-20; sourceRole: Local formulation and derived-proof evidence. Independent mathematical provenance is linked separately.

**sourceLocator:** SQLite FTS5 §§3.7 and 5.1.1; fts5_aux.c: fts5Bm25GetData, fts5Bm25Function; Catalog.fts5_boolean

**sourceNote:** Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.

**provenanceKind:** derived

#### Mathematical formulation

AND(p::ps)=hit(p)∩AND(ps), OR(p::ps)=hit(p)∪OR(ps), AND([])=universe and OR([])=empty.

**Lean formulation** (in its source module context):

```lean
∀ {D : Type u} {P : Type v} (hit : P → D → Prop) (p : P) (ps : List P) (d : D), (d ∈ Catalog.phraseAND hit (p :: ps) ↔ hit p d ∧ d ∈ Catalog.phraseAND hit ps) ∧
    (d ∈ Catalog.phraseOR hit (p :: ps) ↔ hit p d ∨ d ∈ Catalog.phraseOR hit ps) ∧
    d ∈ Catalog.phraseAND hit [] ∧ d ∉ Catalog.phraseOR hit []
```

**Source:** [`Catalog.fts5_boolean`](../lean/Catalog/FTS5Profile.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** AND(p::ps)=hit(p)∩AND(ps), OR(p::ps)=hit(p)∪OR(ps), AND([])=universe and OR([])=empty. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.

**Limits:** Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/BM25FTS5-utility-profile": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.",
  "urn:csabs:axiom/RankedRetrieval-utility-profile": "The same mathematical predicate is shared with this concept; the state-step relation or phrase-hit predicate is explicitly instantiated."
}
```

<a id="node-urn-csabs-theorem-BM25FTS5-sql-ranking-direction"></a>

### sql-ranking-direction

`urn:csabs:theorem/BM25FTS5-sql-ranking-direction`

**statement:** −σ₁≥−σ₂ iff σ₁≤σ₂; descending negated SQL scores agree with ascending SQL scores.

**formalStatement:** −σ₁≥−σ₂ iff σ₁≤σ₂; descending negated SQL scores agree with ascending SQL scores.

**proofSketch:** Order reversal by real negation; identifier ties remain a separate RankedRetrieval convention.

**assumptions:** Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles.

**dependsOn:** [Explicit utility operation definitions](BM25FTS5.md#node-urn-csabs-axiom-BM25FTS5-utility-profile); [Explicit utility operation definitions](RankedRetrieval.md#node-urn-csabs-axiom-RankedRetrieval-utility-profile)

**reviewStatus:** Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.

**source:** [SQLite FTS5 documentation and BM25 auxiliary implementation](https://www.sqlite.org/fts5.html); citation: SQLite project, FTS5 Extension §§3.7, 5.1.1; ext/fts5/fts5_aux.c, https://raw.githubusercontent.com/sqlite/sqlite/master/ext/fts5/fts5_aux.c, consulted 2026-11-20. This consultation URL is not a dependency pin.; accessedOn: 2026-11-20; sourceRole: Consulted primary documentation sections 3.7 and 5.1.1, and fts5_aux.c fts5Bm25GetData/fts5Bm25Function. Exact-real mathematical adaptation; no binary floating-point or tokenizer equivalence claim.; Catalog FTS5Profile Lean formulations and proofs; path: lean/Catalog/FTS5Profile.lean; accessedOn: 2026-11-20; sourceRole: Local formulation and derived-proof evidence. Independent mathematical provenance is linked separately.

**sourceLocator:** SQLite FTS5 §§3.7 and 5.1.1; fts5_aux.c: fts5Bm25GetData, fts5Bm25Function; Catalog.fts5_rank_direction

**sourceNote:** Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.

**provenanceKind:** derived

#### Mathematical formulation

−σ₁≥−σ₂ iff σ₁≤σ₂; descending negated SQL scores agree with ascending SQL scores.

**Lean formulation** (in its source module context):

```lean
∀ (sql₁ sql₂ : ℝ), -sql₁ ≥ -sql₂ ↔ sql₁ ≤ sql₂
```

**Source:** [`Catalog.fts5_rank_direction`](../lean/Catalog/FTS5Profile.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** −σ₁≥−σ₂ iff σ₁≤σ₂; descending negated SQL scores agree with ascending SQL scores. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.

**Limits:** Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/BM25FTS5-utility-profile": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.",
  "urn:csabs:axiom/RankedRetrieval-utility-profile": "The same mathematical predicate is shared with this concept; the state-step relation or phrase-hit predicate is explicitly instantiated."
}
```

<a id="node-urn-csabs-theorem-BM25FTS5-default-column-weights"></a>

### default-column-weights

`urn:csabs:theorem/BM25FTS5-default-column-weights`

**statement:** With no explicit column weights, every column weight is 1.

**formalStatement:** With no explicit column weights, every column weight is 1.

**proofSketch:** Out-of-range optional list lookup returns the documented default.

**assumptions:** Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles.

**dependsOn:** [Explicit utility operation definitions](BM25FTS5.md#node-urn-csabs-axiom-BM25FTS5-utility-profile)

**reviewStatus:** Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.

**source:** [SQLite FTS5 documentation and BM25 auxiliary implementation](https://www.sqlite.org/fts5.html); citation: SQLite project, FTS5 Extension §§3.7, 5.1.1; ext/fts5/fts5_aux.c, https://raw.githubusercontent.com/sqlite/sqlite/master/ext/fts5/fts5_aux.c, consulted 2026-11-20. This consultation URL is not a dependency pin.; accessedOn: 2026-11-20; sourceRole: Consulted primary documentation sections 3.7 and 5.1.1, and fts5_aux.c fts5Bm25GetData/fts5Bm25Function. Exact-real mathematical adaptation; no binary floating-point or tokenizer equivalence claim.; Catalog FTS5Profile Lean formulations and proofs; path: lean/Catalog/FTS5Profile.lean; accessedOn: 2026-11-20; sourceRole: Local formulation and derived-proof evidence. Independent mathematical provenance is linked separately.

**sourceLocator:** SQLite FTS5 §§3.7 and 5.1.1; fts5_aux.c: fts5Bm25GetData, fts5Bm25Function; Catalog.fts5_default_weights

**sourceNote:** Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.

**provenanceKind:** derived

#### Mathematical formulation

With no explicit column weights, every column weight is 1.

**Lean formulation** (in its source module context):

```lean
∀ (c : Nat), Catalog.fts5Weight [] c = 1
```

**Source:** [`Catalog.fts5_default_weights`](../lean/Catalog/FTS5Profile.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** With no explicit column weights, every column weight is 1. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.

**Limits:** Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/BM25FTS5-utility-profile": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders."
}
```

<a id="node-urn-csabs-theorem-BM25FTS5-idf-replacement-cases"></a>

### idf-replacement-cases

`urn:csabs:theorem/BM25FTS5-idf-replacement-cases`

**statement:** Raw IDF≤0 gives IDF=10⁻⁶; raw IDF>0 retains raw IDF exactly.

**formalStatement:** Raw IDF≤0 gives IDF=10⁻⁶; raw IDF>0 retains raw IDF exactly.

**proofSketch:** Split the definition by the sign of raw IDF; positive values below epsilon are not raised.

**assumptions:** Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles.

**dependsOn:** [Explicit utility operation definitions](BM25FTS5.md#node-urn-csabs-axiom-BM25FTS5-utility-profile)

**reviewStatus:** Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.

**source:** [SQLite FTS5 documentation and BM25 auxiliary implementation](https://www.sqlite.org/fts5.html); citation: SQLite project, FTS5 Extension §§3.7, 5.1.1; ext/fts5/fts5_aux.c, https://raw.githubusercontent.com/sqlite/sqlite/master/ext/fts5/fts5_aux.c, consulted 2026-11-20. This consultation URL is not a dependency pin.; accessedOn: 2026-11-20; sourceRole: Consulted primary documentation sections 3.7 and 5.1.1, and fts5_aux.c fts5Bm25GetData/fts5Bm25Function. Exact-real mathematical adaptation; no binary floating-point or tokenizer equivalence claim.; Catalog FTS5Profile Lean formulations and proofs; path: lean/Catalog/FTS5Profile.lean; accessedOn: 2026-11-20; sourceRole: Local formulation and derived-proof evidence. Independent mathematical provenance is linked separately.

**sourceLocator:** SQLite FTS5 §§3.7 and 5.1.1; fts5_aux.c: fts5Bm25GetData, fts5Bm25Function; Catalog.fts5_idf_cases

**sourceNote:** Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.

**provenanceKind:** derived

#### Mathematical formulation

Raw IDF≤0 gives IDF=10⁻⁶; raw IDF>0 retains raw IDF exactly.

**Lean formulation** (in its source module context):

```lean
∀ {P D n} (m : Catalog.BM25FTS5 P D n) (p : P), (Catalog.fts5RawIDF m p ≤ 0 → Catalog.fts5IDF m p = 1/1000000) ∧
    (0 < Catalog.fts5RawIDF m p → Catalog.fts5IDF m p = Catalog.fts5RawIDF m p)
```

**Source:** [`Catalog.fts5_idf_cases`](../lean/Catalog/FTS5Profile.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** Raw IDF≤0 gives IDF=10⁻⁶; raw IDF>0 retains raw IDF exactly. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.

**Limits:** Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/BM25FTS5-utility-profile": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders."
}
```

<a id="node-urn-csabs-theorem-BM25FTS5-empty-query-score"></a>

### empty-query-score

`urn:csabs:theorem/BM25FTS5-empty-query-score`

**statement:** The exact-real empty-phrase-list score is zero.

**formalStatement:** The exact-real empty-phrase-list score is zero.

**proofSketch:** Empty sum and negation; no assertion that SQLite accepts an empty MATCH expression.

**assumptions:** Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles.

**dependsOn:** [Explicit utility operation definitions](BM25FTS5.md#node-urn-csabs-axiom-BM25FTS5-utility-profile)

**reviewStatus:** Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.

**source:** [SQLite FTS5 documentation and BM25 auxiliary implementation](https://www.sqlite.org/fts5.html); citation: SQLite project, FTS5 Extension §§3.7, 5.1.1; ext/fts5/fts5_aux.c, https://raw.githubusercontent.com/sqlite/sqlite/master/ext/fts5/fts5_aux.c, consulted 2026-11-20. This consultation URL is not a dependency pin.; accessedOn: 2026-11-20; sourceRole: Consulted primary documentation sections 3.7 and 5.1.1, and fts5_aux.c fts5Bm25GetData/fts5Bm25Function. Exact-real mathematical adaptation; no binary floating-point or tokenizer equivalence claim.; Catalog FTS5Profile Lean formulations and proofs; path: lean/Catalog/FTS5Profile.lean; accessedOn: 2026-11-20; sourceRole: Local formulation and derived-proof evidence. Independent mathematical provenance is linked separately.

**sourceLocator:** SQLite FTS5 §§3.7 and 5.1.1; fts5_aux.c: fts5Bm25GetData, fts5Bm25Function; Catalog.fts5_empty_query

**sourceNote:** Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.

**provenanceKind:** derived

#### Mathematical formulation

The exact-real empty-phrase-list score is zero.

**Lean formulation** (in its source module context):

```lean
∀ {P D n} (m : Catalog.BM25FTS5 P D n) (weights : List ℝ) (d : D), Catalog.fts5SQLScore m weights [] d = 0
```

**Source:** [`Catalog.fts5_empty_query`](../lean/Catalog/FTS5Profile.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** The exact-real empty-phrase-list score is zero. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.

**Limits:** Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/BM25FTS5-utility-profile": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders."
}
```

<a id="node-urn-csabs-theorem-BM25FTS5-score-equation"></a>

### score-equation

`urn:csabs:theorem/BM25FTS5-score-equation`

**statement:** SQL score is the negative sum of phrase terms IDF·f·(6/5+1)/(f+(6/5)(1−3/4+(3/4)|d|/avgdl)).

**formalStatement:** SQL score is the negative sum of phrase terms IDF·f·(6/5+1)/(f+(6/5)(1−3/4+(3/4)|d|/avgdl)).

**proofSketch:** Definitional expansion of the implemented mathematical score, independently reviewed against the consulted SQLite formula.

**assumptions:** Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles.

**dependsOn:** [Explicit utility operation definitions](BM25FTS5.md#node-urn-csabs-axiom-BM25FTS5-utility-profile)

**reviewStatus:** Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.

**source:** [SQLite FTS5 documentation and BM25 auxiliary implementation](https://www.sqlite.org/fts5.html); citation: SQLite project, FTS5 Extension §§3.7, 5.1.1; ext/fts5/fts5_aux.c, https://raw.githubusercontent.com/sqlite/sqlite/master/ext/fts5/fts5_aux.c, consulted 2026-11-20. This consultation URL is not a dependency pin.; accessedOn: 2026-11-20; sourceRole: Consulted primary documentation sections 3.7 and 5.1.1, and fts5_aux.c fts5Bm25GetData/fts5Bm25Function. Exact-real mathematical adaptation; no binary floating-point or tokenizer equivalence claim.; Catalog FTS5Profile Lean formulations and proofs; path: lean/Catalog/FTS5Profile.lean; accessedOn: 2026-11-20; sourceRole: Local formulation and derived-proof evidence. Independent mathematical provenance is linked separately.

**sourceLocator:** SQLite FTS5 §§3.7 and 5.1.1; fts5_aux.c: fts5Bm25GetData, fts5Bm25Function; Catalog.fts5_score_definition

**sourceNote:** Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.

**provenanceKind:** derived

#### Mathematical formulation

SQL score is the negative sum of phrase terms IDF·f·(6/5+1)/(f+(6/5)(1−3/4+(3/4)|d|/avgdl)).

**Lean formulation** (in its source module context):

```lean
∀ {P D n} (m : Catalog.BM25FTS5 P D n)
    (weights : List ℝ) (ps : List P) (d : D), Catalog.fts5SQLScore m weights ps d = - (ps.map (fun p =>
      let f := Catalog.fts5Frequency m weights p d
      Catalog.fts5IDF m p * (f * (6/5 + 1)) /
        (f + 6/5 * (1 - 3/4 + 3/4 * Catalog.fts5Length m d / Catalog.fts5Average m)))).sum
```

**Source:** [`Catalog.fts5_score_definition`](../lean/Catalog/FTS5Profile.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** SQL score is the negative sum of phrase terms IDF·f·(6/5+1)/(f+(6/5)(1−3/4+(3/4)|d|/avgdl)). Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.

**Limits:** Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/BM25FTS5-utility-profile": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders."
}
```

<a id="node-urn-csabs-theorem-BM25FTS5-model-satisfaction"></a>

### model-satisfaction

`urn:csabs:theorem/BM25FTS5-model-satisfaction`

**statement:** The one-document, one-column, one-token, one-phrase model satisfies nonempty corpus and positive length; default weights are one and empty-list score is zero.

**formalStatement:** The one-document, one-column, one-token, one-phrase model satisfies nonempty corpus and positive length; default weights are one and empty-list score is zero.

**proofSketch:** Construct finite statistics explicitly; discharge positivity and definitional score/weight properties. The separate score-equation witness covers the full general scoring definition.

**assumptions:** Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles.

**dependsOn:** [Explicit utility operation definitions](BM25FTS5.md#node-urn-csabs-axiom-BM25FTS5-utility-profile)

**reviewStatus:** Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.

**source:** [SQLite FTS5 documentation and BM25 auxiliary implementation](https://www.sqlite.org/fts5.html); citation: SQLite project, FTS5 Extension §§3.7, 5.1.1; ext/fts5/fts5_aux.c, https://raw.githubusercontent.com/sqlite/sqlite/master/ext/fts5/fts5_aux.c, consulted 2026-11-20. This consultation URL is not a dependency pin.; accessedOn: 2026-11-20; sourceRole: Consulted primary documentation sections 3.7 and 5.1.1, and fts5_aux.c fts5Bm25GetData/fts5Bm25Function. Exact-real mathematical adaptation; no binary floating-point or tokenizer equivalence claim.; Catalog FTS5Profile Lean formulations and proofs; path: lean/Catalog/FTS5Profile.lean; accessedOn: 2026-11-20; sourceRole: Local formulation and derived-proof evidence. Independent mathematical provenance is linked separately.

**sourceLocator:** SQLite FTS5 §§3.7 and 5.1.1; fts5_aux.c: fts5Bm25GetData, fts5Bm25Function; Catalog.fts5_model_satisfaction

**sourceNote:** Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.

**provenanceKind:** derived

#### Mathematical formulation

The one-document, one-column, one-token, one-phrase model satisfies nonempty corpus and positive length; default weights are one and empty-list score is zero.

**Lean formulation** (in its source module context):

```lean
Catalog.unitFTS5.docs.Nonempty ∧
    (∀ d ∈ Catalog.unitFTS5.docs, 0 < ∑ c, Catalog.unitFTS5.tokens d c) ∧
    (∀ c, Catalog.fts5Weight [] c = 1) ∧
    Catalog.fts5SQLScore Catalog.unitFTS5 [] [] () = 0
```

**Source:** [`Catalog.fts5_model_satisfaction`](../lean/Catalog/FTS5Profile.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** The one-document, one-column, one-token, one-phrase model satisfies nonempty corpus and positive length; default weights are one and empty-list score is zero. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.

**Limits:** Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/BM25FTS5-utility-profile": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders."
}
```

## Concept provenance

- [SQLite FTS5 documentation and BM25 auxiliary implementation](https://www.sqlite.org/fts5.html); citation: SQLite project, FTS5 Extension §§3.7, 5.1.1; ext/fts5/fts5_aux.c, https://raw.githubusercontent.com/sqlite/sqlite/master/ext/fts5/fts5_aux.c, consulted 2026-11-20. This consultation URL is not a dependency pin.; accessedOn: 2026-11-20; sourceRole: Consulted primary documentation sections 3.7 and 5.1.1, and fts5_aux.c fts5Bm25GetData/fts5Bm25Function. Exact-real mathematical adaptation; no binary floating-point or tokenizer equivalence claim.

**sourceLocator:** SQLite FTS5 §§3.7 and 5.1.1; fts5_aux.c: fts5Bm25GetData, fts5Bm25Function

**sourceNote:** Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/BM25FTS5",
    "type": "Concept",
    "shortForm": "BM25FTS5",
    "fullName": "SQLite FTS5-style BM25 phrase and weighted-column profile",
    "synonyms": [
      "FTS5 BM25 exact-real profile",
      "SQLite weighted phrase ranking"
    ],
    "category": [
      "urn:csabs:category/information-theory"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "An exact-real adaptation of SQLite FTS5 BM25 over phrase hits and weighted columns, with unshifted raw IDF and its nonpositive-value replacement.",
    "notation": "SQL(q,d)=−Σₚ IDF(p)·f(p,d)(k₁+1)/(f(p,d)+k₁(1−b+b|d|/avgdl))",
    "axiomBasis": "Corpus/statistics profile and the explicit weighted-frequency, IDF-replacement and score definitions. Utility definitions are recorded separately; optional bottom, subtype and goal-relative conventions are conditional and do not strengthen the base carrier.",
    "basisKind": "defined-structure",
    "basisScope": "Finite nonempty corpus, at least one token per corpus document, finitely many columns, exact real arithmetic and token/phrase occurrence statistics supplied by the caller. Phrases may span multiple tokens within a column; matching and tokenization are external inputs. Default missing column weights are 1; extras are ignored. Use nonnegative finite real weights for scoring with the stated nonzero-denominator domain. k₁=6/5 and b=3/4. Document length sums tokens across all columns and average divides by corpus size. Raw log IDF is replaced by 10⁻⁶ exactly when nonpositive; a small positive raw IDF is retained. Query phrase occurrences retain multiplicity. SQL scores ascend; negated scores fit descending RankedRetrieval. No SQLite floating-point, tokenizer, SQL parser, NEAR, NOT or stable-tie behavior is proved. Empty phrase lists are mathematical extensions (AND universe, OR empty, score zero), not valid empty SQL MATCH syntax.",
    "coverageStatus": "basis-reviewed",
    "requiresConcept": [
      "urn:csabs:concept/FiniteSet",
      "urn:csabs:concept/Sequence",
      "urn:csabs:concept/RankedRetrieval"
    ],
    "relatedConcept": [
      "urn:csabs:concept/BM25"
    ],
    "hasOperation": [
      "urn:csabs:operation/BM25FTS5-column-weight",
      "urn:csabs:operation/BM25FTS5-phrase-frequency",
      "urn:csabs:operation/BM25FTS5-idf",
      "urn:csabs:operation/BM25FTS5-sql-score",
      "urn:csabs:operation/BM25FTS5-phrase-and",
      "urn:csabs:operation/BM25FTS5-phrase-or"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/BM25FTS5-utility-profile"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/BM25FTS5-phrase-boolean-equations",
      "urn:csabs:theorem/BM25FTS5-sql-ranking-direction",
      "urn:csabs:theorem/BM25FTS5-default-column-weights",
      "urn:csabs:theorem/BM25FTS5-idf-replacement-cases",
      "urn:csabs:theorem/BM25FTS5-empty-query-score",
      "urn:csabs:theorem/BM25FTS5-score-equation",
      "urn:csabs:theorem/BM25FTS5-model-satisfaction"
    ],
    "mathematicalFormulation": "N=|C|; df(p)=|{d∈C : ∃c,occ(p,d,c)>0}|; raw=ln((N−df+.5)/(df+.5)); IDF=if raw≤0 then 10⁻⁶ else raw; f=Σc weight(c)occ(p,d,c). Finite nonempty corpus, at least one token per corpus document, finitely many columns, exact real arithmetic and token/phrase occurrence statistics supplied by the caller. Phrases may span multiple tokens within a column; matching and tokenization are external inputs. Default missing column weights are 1; extras are ignored. Use nonnegative finite real weights for scoring with the stated nonzero-denominator domain. k₁=6/5 and b=3/4. Document length sums tokens across all columns and average divides by corpus size. Raw log IDF is replaced by 10⁻⁶ exactly when nonpositive; a small positive raw IDF is retained. Query phrase occurrences retain multiplicity. SQL scores ascend; negated scores fit descending RankedRetrieval. No SQLite floating-point, tokenizer, SQL parser, NEAR, NOT or stable-tie behavior is proved. Empty phrase lists are mathematical extensions (AND universe, OR empty, score zero), not valid empty SQL MATCH syntax. Utility profile: Use supplied weight at column index, otherwise 1. Columns outside the schema are never summed.; f(p,d)=Σc weight(c)·occ(p,d,c); weights affect occurrence frequency, not document length or df.; raw=ln((N−df+.5)/(df+.5)); IDF=10⁻⁶ if raw≤0, otherwise raw. Do not use log(1+ratio), max(raw,epsilon), or the unclamped raw value.; Negative BM25 sum with k₁=1.2,b=.75 and numerator factor k₁+1; total token document length and corpus-wide average; lower score is better.; Candidates matching every listed phrase; restrict to corpus before ranking. Empty conjunction is the mathematical universe.; Candidates matching at least one listed phrase; empty disjunction is empty. Boolean candidate matching is separate from scoring.",
    "source": [
      "urn:csabs:source/sqlite-fts5-profile-2026-11-20"
    ],
    "sourceLocator": "SQLite FTS5 §§3.7 and 5.1.1; fts5_aux.c: fts5Bm25GetData, fts5Bm25Function",
    "sourceNote": "Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.",
    "provenanceKind": "adapted",
    "leanFormulation": "structure BM25FTS5 (P : Type u) (D : Type v) (columns : Nat) where\n  docs : Finset D\n  nonempty : docs.Nonempty\n  tokens : D → Fin columns → Nat\n  positiveLength : ∀ d ∈ docs, 0 < ∑ c, tokens d c\n  occurrences : P → D → Fin columns → Nat",
    "leanModelMapping": "P phrase identities, D document identities, Fin n column indices, finite document set, natural token and phrase-occurrence counts, exact real weights/logarithms/scores. Statistics and tokenization are explicit inputs; negative SQL scores are mapped to descending relevance by negation.",
    "leanModelLimitations": "Finite nonempty corpus, at least one token per corpus document, finitely many columns, exact real arithmetic and token/phrase occurrence statistics supplied by the caller. Phrases may span multiple tokens within a column; matching and tokenization are external inputs. Default missing column weights are 1; extras are ignored. Use nonnegative finite real weights for scoring with the stated nonzero-denominator domain. k₁=6/5 and b=3/4. Document length sums tokens across all columns and average divides by corpus size. Raw log IDF is replaced by 10⁻⁶ exactly when nonpositive; a small positive raw IDF is retained. Query phrase occurrences retain multiplicity. SQL scores ascend; negated scores fit descending RankedRetrieval. No SQLite floating-point, tokenizer, SQL parser, NEAR, NOT or stable-tie behavior is proved. Empty phrase lists are mathematical extensions (AND universe, OR empty, score zero), not valid empty SQL MATCH syntax.",
    "formulationScope": "model",
    "formulationSource": "urn:csabs:source/utility-lean-FTS5Profile",
    "formulationLocator": "Catalog.BM25FTS5"
  },
  {
    "id": "urn:csabs:operation/BM25FTS5-column-weight",
    "type": "Operation",
    "concept": "urn:csabs:concept/BM25FTS5",
    "name": "column-weight",
    "signature": "weight : Seq(ℝ)×ℕ→ℝ",
    "description": "Use supplied weight at column index, otherwise 1. Columns outside the schema are never summed.",
    "precondition": "Use the selected corpus, phrase-statistics and exact-real profile; scoring document lies in the corpus; weights nonnegative and denominator nonzero.",
    "postcondition": "Use supplied weight at column index, otherwise 1. Columns outside the schema are never summed.",
    "totality": "Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.",
    "source": [
      "urn:csabs:source/sqlite-fts5-profile-2026-11-20"
    ],
    "sourceLocator": "SQLite FTS5 §§3.7 and 5.1.1; fts5_aux.c: fts5Bm25GetData, fts5Bm25Function",
    "sourceNote": "Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/BM25FTS5-phrase-frequency",
    "type": "Operation",
    "concept": "urn:csabs:concept/BM25FTS5",
    "name": "phrase-frequency",
    "signature": "frequency : Phrase×Document→ℝ",
    "description": "f(p,d)=Σc weight(c)·occ(p,d,c); weights affect occurrence frequency, not document length or df.",
    "precondition": "Use the selected corpus, phrase-statistics and exact-real profile; scoring document lies in the corpus; weights nonnegative and denominator nonzero.",
    "postcondition": "f(p,d)=Σc weight(c)·occ(p,d,c); weights affect occurrence frequency, not document length or df.",
    "totality": "Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.",
    "source": [
      "urn:csabs:source/sqlite-fts5-profile-2026-11-20"
    ],
    "sourceLocator": "SQLite FTS5 §§3.7 and 5.1.1; fts5_aux.c: fts5Bm25GetData, fts5Bm25Function",
    "sourceNote": "Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/BM25FTS5-idf",
    "type": "Operation",
    "concept": "urn:csabs:concept/BM25FTS5",
    "name": "idf",
    "signature": "idf : Phrase→ℝ",
    "description": "raw=ln((N−df+.5)/(df+.5)); IDF=10⁻⁶ if raw≤0, otherwise raw. Do not use log(1+ratio), max(raw,epsilon), or the unclamped raw value.",
    "precondition": "Use the selected corpus, phrase-statistics and exact-real profile; scoring document lies in the corpus; weights nonnegative and denominator nonzero.",
    "postcondition": "raw=ln((N−df+.5)/(df+.5)); IDF=10⁻⁶ if raw≤0, otherwise raw. Do not use log(1+ratio), max(raw,epsilon), or the unclamped raw value.",
    "totality": "Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.",
    "source": [
      "urn:csabs:source/sqlite-fts5-profile-2026-11-20"
    ],
    "sourceLocator": "SQLite FTS5 §§3.7 and 5.1.1; fts5_aux.c: fts5Bm25GetData, fts5Bm25Function",
    "sourceNote": "Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/BM25FTS5-sql-score",
    "type": "Operation",
    "concept": "urn:csabs:concept/BM25FTS5",
    "name": "sql-score",
    "signature": "sqlScore : Seq(Phrase)×Document→ℝ",
    "description": "Negative BM25 sum with k₁=1.2,b=.75 and numerator factor k₁+1; total token document length and corpus-wide average; lower score is better.",
    "precondition": "Use the selected corpus, phrase-statistics and exact-real profile; scoring document lies in the corpus; weights nonnegative and denominator nonzero.",
    "postcondition": "Negative BM25 sum with k₁=1.2,b=.75 and numerator factor k₁+1; total token document length and corpus-wide average; lower score is better.",
    "totality": "Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.",
    "source": [
      "urn:csabs:source/sqlite-fts5-profile-2026-11-20"
    ],
    "sourceLocator": "SQLite FTS5 §§3.7 and 5.1.1; fts5_aux.c: fts5Bm25GetData, fts5Bm25Function",
    "sourceNote": "Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/BM25FTS5-phrase-and",
    "type": "Operation",
    "concept": "urn:csabs:concept/BM25FTS5",
    "name": "phrase-and",
    "signature": "phraseAND : Seq(Phrase)→Set(Document)",
    "description": "Candidates matching every listed phrase; restrict to corpus before ranking. Empty conjunction is the mathematical universe.",
    "precondition": "Use the selected corpus, phrase-statistics and exact-real profile; scoring document lies in the corpus; weights nonnegative and denominator nonzero.",
    "postcondition": "Candidates matching every listed phrase; restrict to corpus before ranking. Empty conjunction is the mathematical universe.",
    "totality": "Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.",
    "source": [
      "urn:csabs:source/sqlite-fts5-profile-2026-11-20"
    ],
    "sourceLocator": "SQLite FTS5 §§3.7 and 5.1.1; fts5_aux.c: fts5Bm25GetData, fts5Bm25Function",
    "sourceNote": "Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/BM25FTS5-phrase-or",
    "type": "Operation",
    "concept": "urn:csabs:concept/BM25FTS5",
    "name": "phrase-or",
    "signature": "phraseOR : Seq(Phrase)→Set(Document)",
    "description": "Candidates matching at least one listed phrase; empty disjunction is empty. Boolean candidate matching is separate from scoring.",
    "precondition": "Use the selected corpus, phrase-statistics and exact-real profile; scoring document lies in the corpus; weights nonnegative and denominator nonzero.",
    "postcondition": "Candidates matching at least one listed phrase; empty disjunction is empty. Boolean candidate matching is separate from scoring.",
    "totality": "Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.",
    "source": [
      "urn:csabs:source/sqlite-fts5-profile-2026-11-20"
    ],
    "sourceLocator": "SQLite FTS5 §§3.7 and 5.1.1; fts5_aux.c: fts5Bm25GetData, fts5Bm25Function",
    "sourceNote": "Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/BM25FTS5-utility-profile",
    "type": "Axiom",
    "name": "Explicit utility operation definitions",
    "statement": "Use supplied weight at column index, otherwise 1. Columns outside the schema are never summed.; f(p,d)=Σc weight(c)·occ(p,d,c); weights affect occurrence frequency, not document length or df.; raw=ln((N−df+.5)/(df+.5)); IDF=10⁻⁶ if raw≤0, otherwise raw. Do not use log(1+ratio), max(raw,epsilon), or the unclamped raw value.; Negative BM25 sum with k₁=1.2,b=.75 and numerator factor k₁+1; total token document length and corpus-wide average; lower score is better.; Candidates matching every listed phrase; restrict to corpus before ranking. Empty conjunction is the mathematical universe.; Candidates matching at least one listed phrase; empty disjunction is empty. Boolean candidate matching is separate from scoring.",
    "formalStatement": "weight : Seq(ℝ)×ℕ→ℝ: Use supplied weight at column index, otherwise 1. Columns outside the schema are never summed.; frequency : Phrase×Document→ℝ: f(p,d)=Σc weight(c)·occ(p,d,c); weights affect occurrence frequency, not document length or df.; idf : Phrase→ℝ: raw=ln((N−df+.5)/(df+.5)); IDF=10⁻⁶ if raw≤0, otherwise raw. Do not use log(1+ratio), max(raw,epsilon), or the unclamped raw value.; sqlScore : Seq(Phrase)×Document→ℝ: Negative BM25 sum with k₁=1.2,b=.75 and numerator factor k₁+1; total token document length and corpus-wide average; lower score is better.; phraseAND : Seq(Phrase)→Set(Document): Candidates matching every listed phrase; restrict to corpus before ranking. Empty conjunction is the mathematical universe.; phraseOR : Seq(Phrase)→Set(Document): Candidates matching at least one listed phrase; empty disjunction is empty. Boolean candidate matching is separate from scoring.",
    "assumptions": [
      "Finite nonempty corpus, at least one token per corpus document, finitely many columns, exact real arithmetic and token/phrase occurrence statistics supplied by the caller. Phrases may span multiple tokens within a column; matching and tokenization are external inputs. Default missing column weights are 1; extras are ignored. Use nonnegative finite real weights for scoring with the stated nonzero-denominator domain. k₁=6/5 and b=3/4. Document length sums tokens across all columns and average divides by corpus size. Raw log IDF is replaced by 10⁻⁶ exactly when nonpositive; a small positive raw IDF is retained. Query phrase occurrences retain multiplicity. SQL scores ascend; negated scores fit descending RankedRetrieval. No SQLite floating-point, tokenizer, SQL parser, NEAR, NOT or stable-tie behavior is proved. Empty phrase lists are mathematical extensions (AND universe, OR empty, score zero), not valid empty SQL MATCH syntax."
    ],
    "appliesTo": [
      "urn:csabs:concept/BM25FTS5"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Definitions of a selected extension, not new foundational axioms; individual model and result witnesses are separate.",
    "source": [
      "urn:csabs:source/sqlite-fts5-profile-2026-11-20"
    ],
    "sourceLocator": "SQLite FTS5 §§3.7 and 5.1.1; fts5_aux.c: fts5Bm25GetData, fts5Bm25Function",
    "sourceNote": "Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:theorem/BM25FTS5-phrase-boolean-equations",
    "type": "Theorem",
    "name": "phrase-boolean-equations",
    "statement": "AND(p::ps)=hit(p)∩AND(ps), OR(p::ps)=hit(p)∪OR(ps), AND([])=universe and OR([])=empty.",
    "formalStatement": "AND(p::ps)=hit(p)∩AND(ps), OR(p::ps)=hit(p)∪OR(ps), AND([])=universe and OR([])=empty.",
    "mathematicalFormulation": "AND(p::ps)=hit(p)∩AND(ps), OR(p::ps)=hit(p)∪OR(ps), AND([])=universe and OR([])=empty.",
    "proofSketch": "Expand universal/existential membership over a cons list; apply finite corpus restriction separately.",
    "assumptions": [
      "Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles."
    ],
    "appliesTo": [
      "urn:csabs:concept/BM25FTS5",
      "urn:csabs:concept/RankedRetrieval"
    ],
    "dependsOn": [
      "urn:csabs:axiom/BM25FTS5-utility-profile",
      "urn:csabs:axiom/RankedRetrieval-utility-profile"
    ],
    "reviewStatus": "Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.",
    "source": [
      "urn:csabs:source/sqlite-fts5-profile-2026-11-20",
      "urn:csabs:source/utility-lean-FTS5Profile"
    ],
    "sourceLocator": "SQLite FTS5 §§3.7 and 5.1.1; fts5_aux.c: fts5Bm25GetData, fts5Bm25Function; Catalog.fts5_boolean",
    "sourceNote": "Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {D : Type u} {P : Type v} (hit : P → D → Prop) (p : P) (ps : List P) (d : D), (d ∈ Catalog.phraseAND hit (p :: ps) ↔ hit p d ∧ d ∈ Catalog.phraseAND hit ps) ∧\n    (d ∈ Catalog.phraseOR hit (p :: ps) ↔ hit p d ∨ d ∈ Catalog.phraseOR hit ps) ∧\n    d ∈ Catalog.phraseAND hit [] ∧ d ∉ Catalog.phraseOR hit []",
    "leanModelMapping": "AND(p::ps)=hit(p)∩AND(ps), OR(p::ps)=hit(p)∪OR(ps), AND([])=universe and OR([])=empty. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.",
    "leanModelLimitations": "Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/BM25FTS5-utility-profile\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\", \"urn:csabs:axiom/RankedRetrieval-utility-profile\": \"The same mathematical predicate is shared with this concept; the state-step relation or phrase-hit predicate is explicitly instantiated.\"}",
    "formulationScope": "registered-witness-type",
    "formulationSource": "urn:csabs:source/utility-lean-FTS5Profile",
    "formulationLocator": "Catalog.fts5_boolean"
  },
  {
    "id": "urn:csabs:theorem/BM25FTS5-sql-ranking-direction",
    "type": "Theorem",
    "name": "sql-ranking-direction",
    "statement": "−σ₁≥−σ₂ iff σ₁≤σ₂; descending negated SQL scores agree with ascending SQL scores.",
    "formalStatement": "−σ₁≥−σ₂ iff σ₁≤σ₂; descending negated SQL scores agree with ascending SQL scores.",
    "mathematicalFormulation": "−σ₁≥−σ₂ iff σ₁≤σ₂; descending negated SQL scores agree with ascending SQL scores.",
    "proofSketch": "Order reversal by real negation; identifier ties remain a separate RankedRetrieval convention.",
    "assumptions": [
      "Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles."
    ],
    "appliesTo": [
      "urn:csabs:concept/BM25FTS5",
      "urn:csabs:concept/RankedRetrieval"
    ],
    "dependsOn": [
      "urn:csabs:axiom/BM25FTS5-utility-profile",
      "urn:csabs:axiom/RankedRetrieval-utility-profile"
    ],
    "reviewStatus": "Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.",
    "source": [
      "urn:csabs:source/sqlite-fts5-profile-2026-11-20",
      "urn:csabs:source/utility-lean-FTS5Profile"
    ],
    "sourceLocator": "SQLite FTS5 §§3.7 and 5.1.1; fts5_aux.c: fts5Bm25GetData, fts5Bm25Function; Catalog.fts5_rank_direction",
    "sourceNote": "Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ (sql₁ sql₂ : ℝ), -sql₁ ≥ -sql₂ ↔ sql₁ ≤ sql₂",
    "leanModelMapping": "−σ₁≥−σ₂ iff σ₁≤σ₂; descending negated SQL scores agree with ascending SQL scores. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.",
    "leanModelLimitations": "Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/BM25FTS5-utility-profile\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\", \"urn:csabs:axiom/RankedRetrieval-utility-profile\": \"The same mathematical predicate is shared with this concept; the state-step relation or phrase-hit predicate is explicitly instantiated.\"}",
    "formulationScope": "registered-witness-type",
    "formulationSource": "urn:csabs:source/utility-lean-FTS5Profile",
    "formulationLocator": "Catalog.fts5_rank_direction"
  },
  {
    "id": "urn:csabs:theorem/BM25FTS5-default-column-weights",
    "type": "Theorem",
    "name": "default-column-weights",
    "statement": "With no explicit column weights, every column weight is 1.",
    "formalStatement": "With no explicit column weights, every column weight is 1.",
    "mathematicalFormulation": "With no explicit column weights, every column weight is 1.",
    "proofSketch": "Out-of-range optional list lookup returns the documented default.",
    "assumptions": [
      "Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles."
    ],
    "appliesTo": [
      "urn:csabs:concept/BM25FTS5"
    ],
    "dependsOn": [
      "urn:csabs:axiom/BM25FTS5-utility-profile"
    ],
    "reviewStatus": "Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.",
    "source": [
      "urn:csabs:source/sqlite-fts5-profile-2026-11-20",
      "urn:csabs:source/utility-lean-FTS5Profile"
    ],
    "sourceLocator": "SQLite FTS5 §§3.7 and 5.1.1; fts5_aux.c: fts5Bm25GetData, fts5Bm25Function; Catalog.fts5_default_weights",
    "sourceNote": "Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ (c : Nat), Catalog.fts5Weight [] c = 1",
    "leanModelMapping": "With no explicit column weights, every column weight is 1. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.",
    "leanModelLimitations": "Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/BM25FTS5-utility-profile\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\"}",
    "formulationScope": "registered-witness-type",
    "formulationSource": "urn:csabs:source/utility-lean-FTS5Profile",
    "formulationLocator": "Catalog.fts5_default_weights"
  },
  {
    "id": "urn:csabs:theorem/BM25FTS5-idf-replacement-cases",
    "type": "Theorem",
    "name": "idf-replacement-cases",
    "statement": "Raw IDF≤0 gives IDF=10⁻⁶; raw IDF>0 retains raw IDF exactly.",
    "formalStatement": "Raw IDF≤0 gives IDF=10⁻⁶; raw IDF>0 retains raw IDF exactly.",
    "mathematicalFormulation": "Raw IDF≤0 gives IDF=10⁻⁶; raw IDF>0 retains raw IDF exactly.",
    "proofSketch": "Split the definition by the sign of raw IDF; positive values below epsilon are not raised.",
    "assumptions": [
      "Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles."
    ],
    "appliesTo": [
      "urn:csabs:concept/BM25FTS5"
    ],
    "dependsOn": [
      "urn:csabs:axiom/BM25FTS5-utility-profile"
    ],
    "reviewStatus": "Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.",
    "source": [
      "urn:csabs:source/sqlite-fts5-profile-2026-11-20",
      "urn:csabs:source/utility-lean-FTS5Profile"
    ],
    "sourceLocator": "SQLite FTS5 §§3.7 and 5.1.1; fts5_aux.c: fts5Bm25GetData, fts5Bm25Function; Catalog.fts5_idf_cases",
    "sourceNote": "Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {P D n} (m : Catalog.BM25FTS5 P D n) (p : P), (Catalog.fts5RawIDF m p ≤ 0 → Catalog.fts5IDF m p = 1/1000000) ∧\n    (0 < Catalog.fts5RawIDF m p → Catalog.fts5IDF m p = Catalog.fts5RawIDF m p)",
    "leanModelMapping": "Raw IDF≤0 gives IDF=10⁻⁶; raw IDF>0 retains raw IDF exactly. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.",
    "leanModelLimitations": "Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/BM25FTS5-utility-profile\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\"}",
    "formulationScope": "registered-witness-type",
    "formulationSource": "urn:csabs:source/utility-lean-FTS5Profile",
    "formulationLocator": "Catalog.fts5_idf_cases"
  },
  {
    "id": "urn:csabs:theorem/BM25FTS5-empty-query-score",
    "type": "Theorem",
    "name": "empty-query-score",
    "statement": "The exact-real empty-phrase-list score is zero.",
    "formalStatement": "The exact-real empty-phrase-list score is zero.",
    "mathematicalFormulation": "The exact-real empty-phrase-list score is zero.",
    "proofSketch": "Empty sum and negation; no assertion that SQLite accepts an empty MATCH expression.",
    "assumptions": [
      "Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles."
    ],
    "appliesTo": [
      "urn:csabs:concept/BM25FTS5"
    ],
    "dependsOn": [
      "urn:csabs:axiom/BM25FTS5-utility-profile"
    ],
    "reviewStatus": "Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.",
    "source": [
      "urn:csabs:source/sqlite-fts5-profile-2026-11-20",
      "urn:csabs:source/utility-lean-FTS5Profile"
    ],
    "sourceLocator": "SQLite FTS5 §§3.7 and 5.1.1; fts5_aux.c: fts5Bm25GetData, fts5Bm25Function; Catalog.fts5_empty_query",
    "sourceNote": "Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {P D n} (m : Catalog.BM25FTS5 P D n) (weights : List ℝ) (d : D), Catalog.fts5SQLScore m weights [] d = 0",
    "leanModelMapping": "The exact-real empty-phrase-list score is zero. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.",
    "leanModelLimitations": "Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/BM25FTS5-utility-profile\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\"}",
    "formulationScope": "registered-witness-type",
    "formulationSource": "urn:csabs:source/utility-lean-FTS5Profile",
    "formulationLocator": "Catalog.fts5_empty_query"
  },
  {
    "id": "urn:csabs:theorem/BM25FTS5-score-equation",
    "type": "Theorem",
    "name": "score-equation",
    "statement": "SQL score is the negative sum of phrase terms IDF·f·(6/5+1)/(f+(6/5)(1−3/4+(3/4)|d|/avgdl)).",
    "formalStatement": "SQL score is the negative sum of phrase terms IDF·f·(6/5+1)/(f+(6/5)(1−3/4+(3/4)|d|/avgdl)).",
    "mathematicalFormulation": "SQL score is the negative sum of phrase terms IDF·f·(6/5+1)/(f+(6/5)(1−3/4+(3/4)|d|/avgdl)).",
    "proofSketch": "Definitional expansion of the implemented mathematical score, independently reviewed against the consulted SQLite formula.",
    "assumptions": [
      "Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles."
    ],
    "appliesTo": [
      "urn:csabs:concept/BM25FTS5"
    ],
    "dependsOn": [
      "urn:csabs:axiom/BM25FTS5-utility-profile"
    ],
    "reviewStatus": "Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.",
    "source": [
      "urn:csabs:source/sqlite-fts5-profile-2026-11-20",
      "urn:csabs:source/utility-lean-FTS5Profile"
    ],
    "sourceLocator": "SQLite FTS5 §§3.7 and 5.1.1; fts5_aux.c: fts5Bm25GetData, fts5Bm25Function; Catalog.fts5_score_definition",
    "sourceNote": "Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {P D n} (m : Catalog.BM25FTS5 P D n)\n    (weights : List ℝ) (ps : List P) (d : D), Catalog.fts5SQLScore m weights ps d = - (ps.map (fun p =>\n      let f := Catalog.fts5Frequency m weights p d\n      Catalog.fts5IDF m p * (f * (6/5 + 1)) /\n        (f + 6/5 * (1 - 3/4 + 3/4 * Catalog.fts5Length m d / Catalog.fts5Average m)))).sum",
    "leanModelMapping": "SQL score is the negative sum of phrase terms IDF·f·(6/5+1)/(f+(6/5)(1−3/4+(3/4)|d|/avgdl)). Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.",
    "leanModelLimitations": "Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/BM25FTS5-utility-profile\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\"}",
    "formulationScope": "registered-witness-type",
    "formulationSource": "urn:csabs:source/utility-lean-FTS5Profile",
    "formulationLocator": "Catalog.fts5_score_definition"
  },
  {
    "id": "urn:csabs:theorem/BM25FTS5-model-satisfaction",
    "type": "Theorem",
    "name": "model-satisfaction",
    "statement": "The one-document, one-column, one-token, one-phrase model satisfies nonempty corpus and positive length; default weights are one and empty-list score is zero.",
    "formalStatement": "The one-document, one-column, one-token, one-phrase model satisfies nonempty corpus and positive length; default weights are one and empty-list score is zero.",
    "mathematicalFormulation": "The one-document, one-column, one-token, one-phrase model satisfies nonempty corpus and positive length; default weights are one and empty-list score is zero.",
    "proofSketch": "Construct finite statistics explicitly; discharge positivity and definitional score/weight properties. The separate score-equation witness covers the full general scoring definition.",
    "assumptions": [
      "Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles."
    ],
    "appliesTo": [
      "urn:csabs:concept/BM25FTS5"
    ],
    "dependsOn": [
      "urn:csabs:axiom/BM25FTS5-utility-profile"
    ],
    "reviewStatus": "Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.",
    "source": [
      "urn:csabs:source/sqlite-fts5-profile-2026-11-20",
      "urn:csabs:source/utility-lean-FTS5Profile"
    ],
    "sourceLocator": "SQLite FTS5 §§3.7 and 5.1.1; fts5_aux.c: fts5Bm25GetData, fts5Bm25Function; Catalog.fts5_model_satisfaction",
    "sourceNote": "Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.",
    "provenanceKind": "derived",
    "leanFormulation": "Catalog.unitFTS5.docs.Nonempty ∧\n    (∀ d ∈ Catalog.unitFTS5.docs, 0 < ∑ c, Catalog.unitFTS5.tokens d c) ∧\n    (∀ c, Catalog.fts5Weight [] c = 1) ∧\n    Catalog.fts5SQLScore Catalog.unitFTS5 [] [] () = 0",
    "leanModelMapping": "The one-document, one-column, one-token, one-phrase model satisfies nonempty corpus and positive length; default weights are one and empty-list score is zero. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.",
    "leanModelLimitations": "Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/BM25FTS5-utility-profile\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\"}",
    "formulationScope": "registered-witness-type",
    "formulationSource": "urn:csabs:source/utility-lean-FTS5Profile",
    "formulationLocator": "Catalog.fts5_model_satisfaction"
  }
]
```
<!-- graph-record:end -->
