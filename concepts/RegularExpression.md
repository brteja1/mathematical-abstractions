# Classical regular expression of finite words

Finite free syntax built from empty language, empty word, literal symbols, union, concatenation and Kleene star, with a recursively defined finite-word language denotation.

**Notation:** r ::= ∅ | ε | a | r+r | r·r | r*; ⟦r⟧⊆Σ*

**Stable ID:** `urn:csabs:concept/RegularExpression`

**Categories:** Languages and computation

**Kind:** semantic-model

**Prerequisites:** [Formal language of finite words](FormalLanguage.md)

**Related concepts:** [Regular language over a finite alphabet](RegularLanguage.md)

## Mathematical formulation

Regex(Σ)=μX.(1+1+Σ+X²+X²+X); ⟦0⟧=∅; ⟦1⟧={ε}; ⟦a⟧={[a]}; ⟦r+s⟧=⟦r⟧∪⟦s⟧; ⟦r·s⟧={u++v | u∈⟦r⟧,v∈⟦s⟧}; ⟦r\*⟧={w₁++…++wₖ | k≥0,∀i,wᵢ∈⟦r⟧}.

**Lean formulation** (in its source module context):

```lean
abbrev RegularExpression (A : Type) [Fintype A] := _root_.RegularExpression A
```

**Source:** [`Catalog.RegularExpression`](../lean/Catalog/LanguageClasses.lean); consulted 2026-11-20.

**Scope:** model

**Interpretation:** Regex(Σ)=μX.(1+1+Σ+X²+X²+X); ⟦0⟧=∅; ⟦1⟧={ε}; ⟦a⟧={[a]}; ⟦r+s⟧=⟦r⟧∪⟦s⟧; ⟦r·s⟧={u++v | u∈⟦r⟧,v∈⟦s⟧}; ⟦r*⟧={w₁++…++wₖ | k≥0,∀i,wᵢ∈⟦r⟧}.

**Limits:** Finite fixed alphabet, possibly empty; finite words and finite expression trees. Syntax equality is exact constructor-tree equality; semantic equivalence is extensional equality of denoted languages and is a different relation. Star includes zero factors. Letter matching requires decidable exact equality. Whole-word matching; no substring search, wildcard interpretation, parser, captures, backreferences, lookaround, engine priority, or runtime bounds are specified. Regex-to-DFA equivalence is outside the registered witness scope. Selected mathematical profile only; no blanket software refinement, missing closure theorem or automata-equivalence proof. Verification requires fresh compiler and axiom-audit evidence.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Free inductive syntax with six disjoint injective constructors and structural recursion/induction. Denotation is defined recursively: empty is ∅, epsilon is {[]}, literal a is {[a]}, plus is union, comp is word-language concatenation, star is finite Kleene iteration.

**basisKind:** defined-structure

**basisScope:** Finite fixed alphabet, possibly empty; finite words and finite expression trees. Syntax equality is exact constructor-tree equality; semantic equivalence is extensional equality of denoted languages and is a different relation. Star includes zero factors. Letter matching requires decidable exact equality. Whole-word matching; no substring search, wildcard interpretation, parser, captures, backreferences, lookaround, engine priority, or runtime bounds are specified. Regex-to-DFA equivalence is outside the registered witness scope.

**verificationObligation:** Map finite alphabet, exact word equality, extensional language equality and constructor/grammar definedness explicitly.

**reviewStatus:** Sourced defining model; separately registered witness evidence requires fresh Lean audit.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-RegularExpression-construct"></a>

### expression constructors

`urn:csabs:operation/RegularExpression-construct`

**signature:** zero,epsilon:Regex(Σ); char:Σ→Regex(Σ); plus,comp:Regex(Σ)²→Regex(Σ); star:Regex(Σ)→Regex(Σ)

**description:** Build finite expression syntax, retaining constructor order and multiplicity.

**preconditions:** Finite input syntax; symbols in Σ.

**outcomes:** Exact constructor trees; no quotient by language equivalence.

**definedness:** Total on the stated mathematical domain.

**source:** [Mathlib classical regular expressions and derivative matching](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Computability/RegularExpressions.lean); citation: Pinned Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679, Mathlib/Computability/RegularExpressions.lean, Apache-2.0; consulted local pinned source.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference

**sourceLocator:** RegularExpression inductive constructors zero, epsilon, char, plus, comp, star; matches'; rmatch_iff_matches'

**sourceNote:** Restricts the generic pinned expression type to the catalog finite-alphabet profile; retains exact syntax separately from denotational equality. No automaton-equivalence witness is registered.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-RegularExpression-denote"></a>

### language denotation

`urn:csabs:operation/RegularExpression-denote`

**signature:** denote:Regex(Σ)→Lang(Σ)

**description:** Recursively interpret the six constructors.

**preconditions:** Classical finite-word profile.

**outcomes:** A language including ε for epsilon and every star; empty language and empty word remain distinct.

**definedness:** Total on the stated mathematical domain.

**source:** [Mathlib classical regular expressions and derivative matching](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Computability/RegularExpressions.lean); citation: Pinned Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679, Mathlib/Computability/RegularExpressions.lean, Apache-2.0; consulted local pinned source.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference

**sourceLocator:** RegularExpression inductive constructors zero, epsilon, char, plus, comp, star; matches'; rmatch_iff_matches'

**sourceNote:** Restricts the generic pinned expression type to the catalog finite-alphabet profile; retains exact syntax separately from denotational equality. No automaton-equivalence witness is registered.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-RegularExpression-fold"></a>

### structural eliminator

`urn:csabs:operation/RegularExpression-fold`

**signature:** fold: B×B×(Σ→B)×(B²→B)×(B²→B)×(B→B)→(Regex(Σ)→B)

**description:** Unique fold with the six constructor beta equations; structural induction supplies a proof case per constructor.

**preconditions:** Specified carrier B and handlers, no equations imposed on handlers.

**outcomes:** The unique constructor-preserving map into the selected algebra.

**definedness:** Total finite structural recursion; Lean uses generated recursor/induction principles.

**source:** [Mathlib classical regular expressions and derivative matching](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Computability/RegularExpressions.lean); citation: Pinned Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679, Mathlib/Computability/RegularExpressions.lean, Apache-2.0; consulted local pinned source.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference

**sourceLocator:** RegularExpression inductive constructors zero, epsilon, char, plus, comp, star; matches'; rmatch_iff_matches'

**sourceNote:** Restricts the generic pinned expression type to the catalog finite-alphabet profile; retains exact syntax separately from denotational equality. No automaton-equivalence witness is registered.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-RegularExpression-match"></a>

### whole-word Boolean matching

`urn:csabs:operation/RegularExpression-match`

**signature:** match:Regex(Σ)×Σ*→Bool

**description:** Decide exact membership by the pinned derivative matcher.

**preconditions:** Decidable equality of alphabet symbols.

**outcomes:** True iff the whole input word belongs to the denotation; no substring or priority semantics.

**definedness:** Total on the stated mathematical domain.

**source:** [Mathlib classical regular expressions and derivative matching](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Computability/RegularExpressions.lean); citation: Pinned Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679, Mathlib/Computability/RegularExpressions.lean, Apache-2.0; consulted local pinned source.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference

**sourceLocator:** RegularExpression inductive constructors zero, epsilon, char, plus, comp, star; matches'; rmatch_iff_matches'

**sourceNote:** Restricts the generic pinned expression type to the catalog finite-alphabet profile; retains exact syntax separately from denotational equality. No automaton-equivalence witness is registered.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-RegularExpression-defining-profile"></a>

### defining profile

`urn:csabs:axiom/RegularExpression-defining-profile`

**statement:** Free inductive syntax with six disjoint injective constructors and structural recursion/induction. Denotation is defined recursively: empty is ∅, epsilon is {[]}, literal a is {[a]}, plus is union, comp is word-language concatenation, star is finite Kleene iteration.

**formalStatement:** Regex(Σ)=μX.(1+1+Σ+X²+X²+X); ⟦0⟧=∅; ⟦1⟧={ε}; ⟦a⟧={[a]}; ⟦r+s⟧=⟦r⟧∪⟦s⟧; ⟦r·s⟧={u++v | u∈⟦r⟧,v∈⟦s⟧}; ⟦r*⟧={w₁++…++wₖ | k≥0,∀i,wᵢ∈⟦r⟧}.

**assumptions:** Finite fixed alphabet, possibly empty; finite words and finite expression trees. Syntax equality is exact constructor-tree equality; semantic equivalence is extensional equality of denoted languages and is a different relation. Star includes zero factors. Letter matching requires decidable exact equality. Whole-word matching; no substring search, wildcard interpretation, parser, captures, backreferences, lookaround, engine priority, or runtime bounds are specified. Regex-to-DFA equivalence is outside the registered witness scope.

**ruleRole:** defining-rule

**reviewStatus:** Sourced defining equations and carrier constraints; separately witnessed model satisfaction.

**source:** [Mathlib classical regular expressions and derivative matching](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Computability/RegularExpressions.lean); citation: Pinned Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679, Mathlib/Computability/RegularExpressions.lean, Apache-2.0; consulted local pinned source.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference

**sourceLocator:** RegularExpression inductive constructors zero, epsilon, char, plus, comp, star; matches'; rmatch_iff_matches'

**sourceNote:** Restricts the generic pinned expression type to the catalog finite-alphabet profile; retains exact syntax separately from denotational equality. No automaton-equivalence witness is registered.

**provenanceKind:** adapted

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-RegularExpression-model-satisfaction"></a>

### model-satisfaction

`urn:csabs:theorem/RegularExpression-model-satisfaction`

**statement:** Structural recursion interprets all six constructors as the empty language, singleton empty word, singleton letter, union, concatenation and finite Kleene iteration. Each equation is proved by reduction for the actual inductive syntax, without assumed language laws.

**formalStatement:** ∀ {A : Type} [Fintype A], (_root_.RegularExpression.zero : Catalog.RegularExpression A).matches' = 0 ∧ (_root_.RegularExpression.epsilon : Catalog.RegularExpression A).matches' = 1 ∧ (∀ a : A, (_root_.RegularExpression.char a).matches' = {[a]}) ∧ (∀ r s : Catalog.RegularExpression A, (r + s).matches' = r.matches' + s.matches') ∧ (∀ r s : Catalog.RegularExpression A, (r * s).matches' = r.matches' * s.matches') ∧ (∀ r : Catalog.RegularExpression A, r.star.matches' = KStar.kstar r.matches')

**assumptions:** Exactly the displayed typed binders; fixed finite alphabet and exact equality; matching additionally requires DecidableEq.

**dependsOn:** [defining profile](RegularExpression.md#node-urn-csabs-axiom-RegularExpression-defining-profile); [language-operations](FormalLanguage.md#node-urn-csabs-axiom-FormalLanguage-language-operations)

**proofSketch:** Structural recursion interprets all six constructors as the empty language, singleton empty word, singleton letter, union, concatenation and finite Kleene iteration. Each equation is proved by reduction for the actual inductive syntax, without assumed language laws.

**reviewStatus:** Registered witness; verified only by fresh compiler and axiom audit.

**source:** [Mathlib classical regular expressions and derivative matching](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Computability/RegularExpressions.lean); citation: Pinned Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679, Mathlib/Computability/RegularExpressions.lean, Apache-2.0; consulted local pinned source.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; Catalog language classes and regular-expression models and witnesses; path: lean/Catalog/LanguageClasses.lean; accessedOn: 2026-11-20; sourceRole: local-lean-formulation-and-proof

**sourceLocator:** RegularExpression inductive constructors zero, epsilon, char, plus, comp, star; matches'; rmatch_iff_matches'; Catalog.regex_model_satisfaction

**sourceNote:** Derived for the specified interpretation. Structural recursion interprets all six constructors as the empty language, singleton empty word, singleton letter, union, concatenation and finite Kleene iteration. Each equation is proved by reduction for the actual inductive syntax, without assumed language laws.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {A : Type} [Fintype A], (_root_.RegularExpression.zero : Catalog.RegularExpression A).matches' = 0 ∧ (_root_.RegularExpression.epsilon : Catalog.RegularExpression A).matches' = 1 ∧ (∀ a : A, (_root_.RegularExpression.char a).matches' = {[a]}) ∧ (∀ r s : Catalog.RegularExpression A, (r + s).matches' = r.matches' + s.matches') ∧ (∀ r s : Catalog.RegularExpression A, (r * s).matches' = r.matches' * s.matches') ∧ (∀ r : Catalog.RegularExpression A, r.star.matches' = KStar.kstar r.matches')
```

**Source:** [`Catalog.regex_model_satisfaction`](../lean/Catalog/LanguageClasses.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** Structural recursion interprets all six constructors as the empty language, singleton empty word, singleton letter, union, concatenation and finite Kleene iteration. Each equation is proved by reduction for the actual inductive syntax, without assumed language laws.

**Limits:** Selected mathematical profile only; no blanket software refinement, missing closure theorem or automata-equivalence proof. Verification requires fresh compiler and axiom-audit evidence.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/FormalLanguage-language-operations": "Instantiate exact finite words/languages and the finite-nonterminal grammar profile; these premises describe the interpretation, not hypotheses of their own satisfaction. Structural recursion interprets all six constructors as the empty language, singleton empty word, singleton letter, union, concatenation and finite Kleene iteration. Each equation is proved by reduction for the actual inductive syntax, without assumed language laws.",
  "urn:csabs:axiom/RegularExpression-defining-profile": "Instantiate exact finite words/languages and the finite-nonterminal grammar profile; these premises describe the interpretation, not hypotheses of their own satisfaction. Structural recursion interprets all six constructors as the empty language, singleton empty word, singleton letter, union, concatenation and finite Kleene iteration. Each equation is proved by reduction for the actual inductive syntax, without assumed language laws."
}
```

<a id="node-urn-csabs-theorem-RegularExpression-syntax-distinct"></a>

### syntax-distinct

`urn:csabs:theorem/RegularExpression-syntax-distinct`

**statement:** Disjoint constructors distinguish empty-language syntax from empty-word syntax.

**formalStatement:** ∀ {A : Type} [Fintype A] , (0 : Catalog.RegularExpression A) ≠ 1

**assumptions:** Exactly the displayed typed binders; fixed finite alphabet and exact equality; matching additionally requires DecidableEq.

**dependsOn:** [defining profile](RegularExpression.md#node-urn-csabs-axiom-RegularExpression-defining-profile); [language-operations](FormalLanguage.md#node-urn-csabs-axiom-FormalLanguage-language-operations)

**proofSketch:** Disjoint constructors distinguish empty-language syntax from empty-word syntax.

**reviewStatus:** Registered witness; verified only by fresh compiler and axiom audit.

**source:** [Mathlib classical regular expressions and derivative matching](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Computability/RegularExpressions.lean); citation: Pinned Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679, Mathlib/Computability/RegularExpressions.lean, Apache-2.0; consulted local pinned source.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; Catalog language classes and regular-expression models and witnesses; path: lean/Catalog/LanguageClasses.lean; accessedOn: 2026-11-20; sourceRole: local-lean-formulation-and-proof

**sourceLocator:** RegularExpression inductive constructors zero, epsilon, char, plus, comp, star; matches'; rmatch_iff_matches'; Catalog.regex_syntax_distinct

**sourceNote:** Derived for the specified interpretation. Disjoint constructors distinguish empty-language syntax from empty-word syntax.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {A : Type} [Fintype A] , (0 : Catalog.RegularExpression A) ≠ 1
```

**Source:** [`Catalog.regex_syntax_distinct`](../lean/Catalog/LanguageClasses.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** Disjoint constructors distinguish empty-language syntax from empty-word syntax.

**Limits:** Selected mathematical profile only; no blanket software refinement, missing closure theorem or automata-equivalence proof. Verification requires fresh compiler and axiom-audit evidence.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/FormalLanguage-language-operations": "Instantiate exact finite words/languages and the finite-nonterminal grammar profile; these premises describe the interpretation, not hypotheses of their own satisfaction. Disjoint constructors distinguish empty-language syntax from empty-word syntax.",
  "urn:csabs:axiom/RegularExpression-defining-profile": "Instantiate exact finite words/languages and the finite-nonterminal grammar profile; these premises describe the interpretation, not hypotheses of their own satisfaction. Disjoint constructors distinguish empty-language syntax from empty-word syntax."
}
```

<a id="node-urn-csabs-theorem-RegularExpression-semantic-union-idempotence"></a>

### semantic-union-idempotence

`urn:csabs:theorem/RegularExpression-semantic-union-idempotence`

**statement:** Language union is idempotent by extensional set membership. The syntax trees need not be equal.

**formalStatement:** ∀ {A : Type} [Fintype A] (r : Catalog.RegularExpression A), (r + r).matches' = r.matches'

**assumptions:** Exactly the displayed typed binders; fixed finite alphabet and exact equality; matching additionally requires DecidableEq.

**dependsOn:** [defining profile](RegularExpression.md#node-urn-csabs-axiom-RegularExpression-defining-profile); [language-operations](FormalLanguage.md#node-urn-csabs-axiom-FormalLanguage-language-operations); [union-membership](FormalLanguage.md#node-urn-csabs-axiom-FormalLanguage-union-membership)

**proofSketch:** Language union is idempotent by extensional set membership. The syntax trees need not be equal.

**reviewStatus:** Registered witness; verified only by fresh compiler and axiom audit.

**source:** [Mathlib classical regular expressions and derivative matching](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Computability/RegularExpressions.lean); citation: Pinned Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679, Mathlib/Computability/RegularExpressions.lean, Apache-2.0; consulted local pinned source.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; Catalog language classes and regular-expression models and witnesses; path: lean/Catalog/LanguageClasses.lean; accessedOn: 2026-11-20; sourceRole: local-lean-formulation-and-proof

**sourceLocator:** RegularExpression inductive constructors zero, epsilon, char, plus, comp, star; matches'; rmatch_iff_matches'; Catalog.regex_union_idempotent

**sourceNote:** Derived for the specified interpretation. Language union is idempotent by extensional set membership. The syntax trees need not be equal.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {A : Type} [Fintype A] (r : Catalog.RegularExpression A), (r + r).matches' = r.matches'
```

**Source:** [`Catalog.regex_union_idempotent`](../lean/Catalog/LanguageClasses.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** Language union is idempotent by extensional set membership. The syntax trees need not be equal.

**Limits:** Selected mathematical profile only; no blanket software refinement, missing closure theorem or automata-equivalence proof. Verification requires fresh compiler and axiom-audit evidence.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/FormalLanguage-language-operations": "Instantiate exact finite words/languages and the finite-nonterminal grammar profile; these premises describe the interpretation, not hypotheses of their own satisfaction. Language union is idempotent by extensional set membership. The syntax trees need not be equal.",
  "urn:csabs:axiom/FormalLanguage-union-membership": "Instantiate exact finite words/languages and the finite-nonterminal grammar profile; these premises describe the interpretation, not hypotheses of their own satisfaction. Language union is idempotent by extensional set membership. The syntax trees need not be equal.",
  "urn:csabs:axiom/RegularExpression-defining-profile": "Instantiate exact finite words/languages and the finite-nonterminal grammar profile; these premises describe the interpretation, not hypotheses of their own satisfaction. Language union is idempotent by extensional set membership. The syntax trees need not be equal."
}
```

<a id="node-urn-csabs-theorem-RegularExpression-semantic-concat-associativity"></a>

### semantic-concat-associativity

`urn:csabs:theorem/RegularExpression-semantic-concat-associativity`

**statement:** Language multiplication is associative because word append is associative; only denotational equality is claimed.

**formalStatement:** ∀ {A : Type} [Fintype A] (r s t : Catalog.RegularExpression A), ((r * s) * t).matches' = (r * (s * t)).matches'

**assumptions:** Exactly the displayed typed binders; fixed finite alphabet and exact equality; matching additionally requires DecidableEq.

**dependsOn:** [defining profile](RegularExpression.md#node-urn-csabs-axiom-RegularExpression-defining-profile); [language-operations](FormalLanguage.md#node-urn-csabs-axiom-FormalLanguage-language-operations); [concatenation-monoid](FormalLanguage.md#node-urn-csabs-law-FormalLanguage-concatenation-monoid)

**proofSketch:** Language multiplication is associative because word append is associative; only denotational equality is claimed.

**reviewStatus:** Registered witness; verified only by fresh compiler and axiom audit.

**source:** [Mathlib classical regular expressions and derivative matching](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Computability/RegularExpressions.lean); citation: Pinned Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679, Mathlib/Computability/RegularExpressions.lean, Apache-2.0; consulted local pinned source.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; Catalog language classes and regular-expression models and witnesses; path: lean/Catalog/LanguageClasses.lean; accessedOn: 2026-11-20; sourceRole: local-lean-formulation-and-proof

**sourceLocator:** RegularExpression inductive constructors zero, epsilon, char, plus, comp, star; matches'; rmatch_iff_matches'; Catalog.regex_concat_associative

**sourceNote:** Derived for the specified interpretation. Language multiplication is associative because word append is associative; only denotational equality is claimed.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {A : Type} [Fintype A] (r s t : Catalog.RegularExpression A), ((r * s) * t).matches' = (r * (s * t)).matches'
```

**Source:** [`Catalog.regex_concat_associative`](../lean/Catalog/LanguageClasses.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** Language multiplication is associative because word append is associative; only denotational equality is claimed.

**Limits:** Selected mathematical profile only; no blanket software refinement, missing closure theorem or automata-equivalence proof. Verification requires fresh compiler and axiom-audit evidence.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/FormalLanguage-language-operations": "Instantiate exact finite words/languages and the finite-nonterminal grammar profile; these premises describe the interpretation, not hypotheses of their own satisfaction. Language multiplication is associative because word append is associative; only denotational equality is claimed.",
  "urn:csabs:axiom/RegularExpression-defining-profile": "Instantiate exact finite words/languages and the finite-nonterminal grammar profile; these premises describe the interpretation, not hypotheses of their own satisfaction. Language multiplication is associative because word append is associative; only denotational equality is claimed.",
  "urn:csabs:law/FormalLanguage-concatenation-monoid": "Instantiate exact finite words/languages and the finite-nonterminal grammar profile; these premises describe the interpretation, not hypotheses of their own satisfaction. Language multiplication is associative because word append is associative; only denotational equality is claimed."
}
```

<a id="node-urn-csabs-theorem-RegularExpression-star-empty-word"></a>

### star-empty-word

`urn:csabs:theorem/RegularExpression-star-empty-word`

**statement:** The zero-factor word belongs to every Kleene star, even when the operand denotes the empty language.

**formalStatement:** ∀ {A : Type} [Fintype A] (r : Catalog.RegularExpression A), [] ∈ r.star.matches'

**assumptions:** Exactly the displayed typed binders; fixed finite alphabet and exact equality; matching additionally requires DecidableEq.

**dependsOn:** [defining profile](RegularExpression.md#node-urn-csabs-axiom-RegularExpression-defining-profile); [language-operations](FormalLanguage.md#node-urn-csabs-axiom-FormalLanguage-language-operations)

**proofSketch:** The zero-factor word belongs to every Kleene star, even when the operand denotes the empty language.

**reviewStatus:** Registered witness; verified only by fresh compiler and axiom audit.

**source:** [Mathlib classical regular expressions and derivative matching](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Computability/RegularExpressions.lean); citation: Pinned Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679, Mathlib/Computability/RegularExpressions.lean, Apache-2.0; consulted local pinned source.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; Catalog language classes and regular-expression models and witnesses; path: lean/Catalog/LanguageClasses.lean; accessedOn: 2026-11-20; sourceRole: local-lean-formulation-and-proof

**sourceLocator:** RegularExpression inductive constructors zero, epsilon, char, plus, comp, star; matches'; rmatch_iff_matches'; Catalog.regex_star_empty_word

**sourceNote:** Derived for the specified interpretation. The zero-factor word belongs to every Kleene star, even when the operand denotes the empty language.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {A : Type} [Fintype A] (r : Catalog.RegularExpression A), [] ∈ r.star.matches'
```

**Source:** [`Catalog.regex_star_empty_word`](../lean/Catalog/LanguageClasses.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** The zero-factor word belongs to every Kleene star, even when the operand denotes the empty language.

**Limits:** Selected mathematical profile only; no blanket software refinement, missing closure theorem or automata-equivalence proof. Verification requires fresh compiler and axiom-audit evidence.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/FormalLanguage-language-operations": "Instantiate exact finite words/languages and the finite-nonterminal grammar profile; these premises describe the interpretation, not hypotheses of their own satisfaction. The zero-factor word belongs to every Kleene star, even when the operand denotes the empty language.",
  "urn:csabs:axiom/RegularExpression-defining-profile": "Instantiate exact finite words/languages and the finite-nonterminal grammar profile; these premises describe the interpretation, not hypotheses of their own satisfaction. The zero-factor word belongs to every Kleene star, even when the operand denotes the empty language."
}
```

<a id="node-urn-csabs-theorem-RegularExpression-matching-correctness"></a>

### matching-correctness

`urn:csabs:theorem/RegularExpression-matching-correctness`

**statement:** Instantiate the pinned derivative-matcher correctness theorem; the result concerns whole finite words with exact decidable letter equality.

**formalStatement:** ∀ {A : Type} [Fintype A] [DecidableEq A] (r : Catalog.RegularExpression A) (w : List A), r.rmatch w = true ↔ w ∈ r.matches'

**assumptions:** Exactly the displayed typed binders; fixed finite alphabet and exact equality; matching additionally requires DecidableEq.

**dependsOn:** [defining profile](RegularExpression.md#node-urn-csabs-axiom-RegularExpression-defining-profile); [language-operations](FormalLanguage.md#node-urn-csabs-axiom-FormalLanguage-language-operations)

**proofSketch:** Instantiate the pinned derivative-matcher correctness theorem; the result concerns whole finite words with exact decidable letter equality.

**reviewStatus:** Registered witness; verified only by fresh compiler and axiom audit.

**source:** [Mathlib classical regular expressions and derivative matching](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Computability/RegularExpressions.lean); citation: Pinned Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679, Mathlib/Computability/RegularExpressions.lean, Apache-2.0; consulted local pinned source.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; Catalog language classes and regular-expression models and witnesses; path: lean/Catalog/LanguageClasses.lean; accessedOn: 2026-11-20; sourceRole: local-lean-formulation-and-proof

**sourceLocator:** RegularExpression inductive constructors zero, epsilon, char, plus, comp, star; matches'; rmatch_iff_matches'; Catalog.regex_match_correct

**sourceNote:** Derived for the specified interpretation. Instantiate the pinned derivative-matcher correctness theorem; the result concerns whole finite words with exact decidable letter equality.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {A : Type} [Fintype A] [DecidableEq A] (r : Catalog.RegularExpression A) (w : List A), r.rmatch w = true ↔ w ∈ r.matches'
```

**Source:** [`Catalog.regex_match_correct`](../lean/Catalog/LanguageClasses.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** Instantiate the pinned derivative-matcher correctness theorem; the result concerns whole finite words with exact decidable letter equality.

**Limits:** Selected mathematical profile only; no blanket software refinement, missing closure theorem or automata-equivalence proof. Verification requires fresh compiler and axiom-audit evidence.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/FormalLanguage-language-operations": "Instantiate exact finite words/languages and the finite-nonterminal grammar profile; these premises describe the interpretation, not hypotheses of their own satisfaction. Instantiate the pinned derivative-matcher correctness theorem; the result concerns whole finite words with exact decidable letter equality.",
  "urn:csabs:axiom/RegularExpression-defining-profile": "Instantiate exact finite words/languages and the finite-nonterminal grammar profile; these premises describe the interpretation, not hypotheses of their own satisfaction. Instantiate the pinned derivative-matcher correctness theorem; the result concerns whole finite words with exact decidable letter equality."
}
```

## Concept provenance

- [Mathlib classical regular expressions and derivative matching](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Computability/RegularExpressions.lean); citation: Pinned Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679, Mathlib/Computability/RegularExpressions.lean, Apache-2.0; consulted local pinned source.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference

**sourceLocator:** RegularExpression inductive constructors zero, epsilon, char, plus, comp, star; matches'; rmatch_iff_matches'

**sourceNote:** Restricts the generic pinned expression type to the catalog finite-alphabet profile; retains exact syntax separately from denotational equality. No automaton-equivalence witness is registered.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/RegularExpression",
    "type": "Concept",
    "shortForm": "RegularExpression",
    "fullName": "Classical regular expression of finite words",
    "synonyms": [
      "Classical regex syntax",
      "Kleene regular expression"
    ],
    "category": [
      "urn:csabs:category/languages-computation"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "definition": "Finite free syntax built from empty language, empty word, literal symbols, union, concatenation and Kleene star, with a recursively defined finite-word language denotation.",
    "notation": "r ::= ∅ | ε | a | r+r | r·r | r*; ⟦r⟧⊆Σ*",
    "requiresConcept": [
      "urn:csabs:concept/FormalLanguage"
    ],
    "relatedConcept": [
      "urn:csabs:concept/RegularLanguage"
    ],
    "axiomBasis": "Free inductive syntax with six disjoint injective constructors and structural recursion/induction. Denotation is defined recursively: empty is ∅, epsilon is {[]}, literal a is {[a]}, plus is union, comp is word-language concatenation, star is finite Kleene iteration.",
    "basisKind": "defined-structure",
    "basisScope": "Finite fixed alphabet, possibly empty; finite words and finite expression trees. Syntax equality is exact constructor-tree equality; semantic equivalence is extensional equality of denoted languages and is a different relation. Star includes zero factors. Letter matching requires decidable exact equality. Whole-word matching; no substring search, wildcard interpretation, parser, captures, backreferences, lookaround, engine priority, or runtime bounds are specified. Regex-to-DFA equivalence is outside the registered witness scope.",
    "mathematicalFormulation": "Regex(Σ)=μX.(1+1+Σ+X²+X²+X); ⟦0⟧=∅; ⟦1⟧={ε}; ⟦a⟧={[a]}; ⟦r+s⟧=⟦r⟧∪⟦s⟧; ⟦r·s⟧={u++v | u∈⟦r⟧,v∈⟦s⟧}; ⟦r*⟧={w₁++…++wₖ | k≥0,∀i,wᵢ∈⟦r⟧}.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Sourced defining model; separately registered witness evidence requires fresh Lean audit.",
    "verificationObligation": [
      "Map finite alphabet, exact word equality, extensional language equality and constructor/grammar definedness explicitly."
    ],
    "hasOperation": [
      "urn:csabs:operation/RegularExpression-construct",
      "urn:csabs:operation/RegularExpression-denote",
      "urn:csabs:operation/RegularExpression-fold",
      "urn:csabs:operation/RegularExpression-match"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/RegularExpression-defining-profile"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/RegularExpression-model-satisfaction",
      "urn:csabs:theorem/RegularExpression-syntax-distinct",
      "urn:csabs:theorem/RegularExpression-semantic-union-idempotence",
      "urn:csabs:theorem/RegularExpression-semantic-concat-associativity",
      "urn:csabs:theorem/RegularExpression-star-empty-word",
      "urn:csabs:theorem/RegularExpression-matching-correctness"
    ],
    "source": [
      "urn:csabs:source/language-acquisition-regex"
    ],
    "sourceLocator": "RegularExpression inductive constructors zero, epsilon, char, plus, comp, star; matches'; rmatch_iff_matches'",
    "sourceNote": "Restricts the generic pinned expression type to the catalog finite-alphabet profile; retains exact syntax separately from denotational equality. No automaton-equivalence witness is registered.",
    "provenanceKind": "adapted",
    "leanFormulation": "abbrev RegularExpression (A : Type) [Fintype A] := _root_.RegularExpression A",
    "formulationSource": "urn:csabs:source/language-acquisition-lean-models",
    "formulationLocator": "Catalog.RegularExpression",
    "formulationScope": "model",
    "leanModelMapping": "Regex(Σ)=μX.(1+1+Σ+X²+X²+X); ⟦0⟧=∅; ⟦1⟧={ε}; ⟦a⟧={[a]}; ⟦r+s⟧=⟦r⟧∪⟦s⟧; ⟦r·s⟧={u++v | u∈⟦r⟧,v∈⟦s⟧}; ⟦r*⟧={w₁++…++wₖ | k≥0,∀i,wᵢ∈⟦r⟧}.",
    "leanModelLimitations": "Finite fixed alphabet, possibly empty; finite words and finite expression trees. Syntax equality is exact constructor-tree equality; semantic equivalence is extensional equality of denoted languages and is a different relation. Star includes zero factors. Letter matching requires decidable exact equality. Whole-word matching; no substring search, wildcard interpretation, parser, captures, backreferences, lookaround, engine priority, or runtime bounds are specified. Regex-to-DFA equivalence is outside the registered witness scope. Selected mathematical profile only; no blanket software refinement, missing closure theorem or automata-equivalence proof. Verification requires fresh compiler and axiom-audit evidence."
  },
  {
    "id": "urn:csabs:operation/RegularExpression-construct",
    "type": "Operation",
    "name": "expression constructors",
    "signature": "zero,epsilon:Regex(Σ); char:Σ→Regex(Σ); plus,comp:Regex(Σ)²→Regex(Σ); star:Regex(Σ)→Regex(Σ)",
    "description": "Build finite expression syntax, retaining constructor order and multiplicity.",
    "preconditions": "Finite input syntax; symbols in Σ.",
    "outcomes": "Exact constructor trees; no quotient by language equivalence.",
    "definedness": "Total on the stated mathematical domain.",
    "concept": "urn:csabs:concept/RegularExpression",
    "appliesTo": [
      "urn:csabs:concept/RegularExpression"
    ],
    "source": [
      "urn:csabs:source/language-acquisition-regex"
    ],
    "sourceLocator": "RegularExpression inductive constructors zero, epsilon, char, plus, comp, star; matches'; rmatch_iff_matches'",
    "sourceNote": "Restricts the generic pinned expression type to the catalog finite-alphabet profile; retains exact syntax separately from denotational equality. No automaton-equivalence witness is registered.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/RegularExpression-denote",
    "type": "Operation",
    "name": "language denotation",
    "signature": "denote:Regex(Σ)→Lang(Σ)",
    "description": "Recursively interpret the six constructors.",
    "preconditions": "Classical finite-word profile.",
    "outcomes": "A language including ε for epsilon and every star; empty language and empty word remain distinct.",
    "definedness": "Total on the stated mathematical domain.",
    "concept": "urn:csabs:concept/RegularExpression",
    "appliesTo": [
      "urn:csabs:concept/RegularExpression"
    ],
    "source": [
      "urn:csabs:source/language-acquisition-regex"
    ],
    "sourceLocator": "RegularExpression inductive constructors zero, epsilon, char, plus, comp, star; matches'; rmatch_iff_matches'",
    "sourceNote": "Restricts the generic pinned expression type to the catalog finite-alphabet profile; retains exact syntax separately from denotational equality. No automaton-equivalence witness is registered.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/RegularExpression-fold",
    "type": "Operation",
    "name": "structural eliminator",
    "signature": "fold: B×B×(Σ→B)×(B²→B)×(B²→B)×(B→B)→(Regex(Σ)→B)",
    "description": "Unique fold with the six constructor beta equations; structural induction supplies a proof case per constructor.",
    "preconditions": "Specified carrier B and handlers, no equations imposed on handlers.",
    "outcomes": "The unique constructor-preserving map into the selected algebra.",
    "definedness": "Total finite structural recursion; Lean uses generated recursor/induction principles.",
    "concept": "urn:csabs:concept/RegularExpression",
    "appliesTo": [
      "urn:csabs:concept/RegularExpression"
    ],
    "source": [
      "urn:csabs:source/language-acquisition-regex"
    ],
    "sourceLocator": "RegularExpression inductive constructors zero, epsilon, char, plus, comp, star; matches'; rmatch_iff_matches'",
    "sourceNote": "Restricts the generic pinned expression type to the catalog finite-alphabet profile; retains exact syntax separately from denotational equality. No automaton-equivalence witness is registered.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/RegularExpression-match",
    "type": "Operation",
    "name": "whole-word Boolean matching",
    "signature": "match:Regex(Σ)×Σ*→Bool",
    "description": "Decide exact membership by the pinned derivative matcher.",
    "preconditions": "Decidable equality of alphabet symbols.",
    "outcomes": "True iff the whole input word belongs to the denotation; no substring or priority semantics.",
    "definedness": "Total on the stated mathematical domain.",
    "concept": "urn:csabs:concept/RegularExpression",
    "appliesTo": [
      "urn:csabs:concept/RegularExpression"
    ],
    "source": [
      "urn:csabs:source/language-acquisition-regex"
    ],
    "sourceLocator": "RegularExpression inductive constructors zero, epsilon, char, plus, comp, star; matches'; rmatch_iff_matches'",
    "sourceNote": "Restricts the generic pinned expression type to the catalog finite-alphabet profile; retains exact syntax separately from denotational equality. No automaton-equivalence witness is registered.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/RegularExpression-defining-profile",
    "type": "Axiom",
    "name": "defining profile",
    "statement": "Free inductive syntax with six disjoint injective constructors and structural recursion/induction. Denotation is defined recursively: empty is ∅, epsilon is {[]}, literal a is {[a]}, plus is union, comp is word-language concatenation, star is finite Kleene iteration.",
    "formalStatement": "Regex(Σ)=μX.(1+1+Σ+X²+X²+X); ⟦0⟧=∅; ⟦1⟧={ε}; ⟦a⟧={[a]}; ⟦r+s⟧=⟦r⟧∪⟦s⟧; ⟦r·s⟧={u++v | u∈⟦r⟧,v∈⟦s⟧}; ⟦r*⟧={w₁++…++wₖ | k≥0,∀i,wᵢ∈⟦r⟧}.",
    "assumptions": [
      "Finite fixed alphabet, possibly empty; finite words and finite expression trees. Syntax equality is exact constructor-tree equality; semantic equivalence is extensional equality of denoted languages and is a different relation. Star includes zero factors. Letter matching requires decidable exact equality. Whole-word matching; no substring search, wildcard interpretation, parser, captures, backreferences, lookaround, engine priority, or runtime bounds are specified. Regex-to-DFA equivalence is outside the registered witness scope."
    ],
    "appliesTo": [
      "urn:csabs:concept/RegularExpression"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Sourced defining equations and carrier constraints; separately witnessed model satisfaction.",
    "source": [
      "urn:csabs:source/language-acquisition-regex"
    ],
    "sourceLocator": "RegularExpression inductive constructors zero, epsilon, char, plus, comp, star; matches'; rmatch_iff_matches'",
    "sourceNote": "Restricts the generic pinned expression type to the catalog finite-alphabet profile; retains exact syntax separately from denotational equality. No automaton-equivalence witness is registered.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:theorem/RegularExpression-model-satisfaction",
    "type": "Theorem",
    "name": "model-satisfaction",
    "statement": "Structural recursion interprets all six constructors as the empty language, singleton empty word, singleton letter, union, concatenation and finite Kleene iteration. Each equation is proved by reduction for the actual inductive syntax, without assumed language laws.",
    "formalStatement": "∀ {A : Type} [Fintype A], (_root_.RegularExpression.zero : Catalog.RegularExpression A).matches' = 0 ∧ (_root_.RegularExpression.epsilon : Catalog.RegularExpression A).matches' = 1 ∧ (∀ a : A, (_root_.RegularExpression.char a).matches' = {[a]}) ∧ (∀ r s : Catalog.RegularExpression A, (r + s).matches' = r.matches' + s.matches') ∧ (∀ r s : Catalog.RegularExpression A, (r * s).matches' = r.matches' * s.matches') ∧ (∀ r : Catalog.RegularExpression A, r.star.matches' = KStar.kstar r.matches')",
    "assumptions": [
      "Exactly the displayed typed binders; fixed finite alphabet and exact equality; matching additionally requires DecidableEq."
    ],
    "appliesTo": [
      "urn:csabs:concept/RegularExpression"
    ],
    "dependsOn": [
      "urn:csabs:axiom/RegularExpression-defining-profile",
      "urn:csabs:axiom/FormalLanguage-language-operations"
    ],
    "proofSketch": "Structural recursion interprets all six constructors as the empty language, singleton empty word, singleton letter, union, concatenation and finite Kleene iteration. Each equation is proved by reduction for the actual inductive syntax, without assumed language laws.",
    "reviewStatus": "Registered witness; verified only by fresh compiler and axiom audit.",
    "source": [
      "urn:csabs:source/language-acquisition-regex",
      "urn:csabs:source/language-acquisition-lean-models"
    ],
    "sourceLocator": "RegularExpression inductive constructors zero, epsilon, char, plus, comp, star; matches'; rmatch_iff_matches'; Catalog.regex_model_satisfaction",
    "sourceNote": "Derived for the specified interpretation. Structural recursion interprets all six constructors as the empty language, singleton empty word, singleton letter, union, concatenation and finite Kleene iteration. Each equation is proved by reduction for the actual inductive syntax, without assumed language laws.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {A : Type} [Fintype A], (_root_.RegularExpression.zero : Catalog.RegularExpression A).matches' = 0 ∧ (_root_.RegularExpression.epsilon : Catalog.RegularExpression A).matches' = 1 ∧ (∀ a : A, (_root_.RegularExpression.char a).matches' = {[a]}) ∧ (∀ r s : Catalog.RegularExpression A, (r + s).matches' = r.matches' + s.matches') ∧ (∀ r s : Catalog.RegularExpression A, (r * s).matches' = r.matches' * s.matches') ∧ (∀ r : Catalog.RegularExpression A, r.star.matches' = KStar.kstar r.matches')",
    "formulationSource": "urn:csabs:source/language-acquisition-lean-models",
    "formulationLocator": "Catalog.regex_model_satisfaction",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Structural recursion interprets all six constructors as the empty language, singleton empty word, singleton letter, union, concatenation and finite Kleene iteration. Each equation is proved by reduction for the actual inductive syntax, without assumed language laws.",
    "leanModelLimitations": "Selected mathematical profile only; no blanket software refinement, missing closure theorem or automata-equivalence proof. Verification requires fresh compiler and axiom-audit evidence.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/FormalLanguage-language-operations\": \"Instantiate exact finite words/languages and the finite-nonterminal grammar profile; these premises describe the interpretation, not hypotheses of their own satisfaction. Structural recursion interprets all six constructors as the empty language, singleton empty word, singleton letter, union, concatenation and finite Kleene iteration. Each equation is proved by reduction for the actual inductive syntax, without assumed language laws.\", \"urn:csabs:axiom/RegularExpression-defining-profile\": \"Instantiate exact finite words/languages and the finite-nonterminal grammar profile; these premises describe the interpretation, not hypotheses of their own satisfaction. Structural recursion interprets all six constructors as the empty language, singleton empty word, singleton letter, union, concatenation and finite Kleene iteration. Each equation is proved by reduction for the actual inductive syntax, without assumed language laws.\"}"
  },
  {
    "id": "urn:csabs:theorem/RegularExpression-syntax-distinct",
    "type": "Theorem",
    "name": "syntax-distinct",
    "statement": "Disjoint constructors distinguish empty-language syntax from empty-word syntax.",
    "formalStatement": "∀ {A : Type} [Fintype A] , (0 : Catalog.RegularExpression A) ≠ 1",
    "assumptions": [
      "Exactly the displayed typed binders; fixed finite alphabet and exact equality; matching additionally requires DecidableEq."
    ],
    "appliesTo": [
      "urn:csabs:concept/RegularExpression"
    ],
    "dependsOn": [
      "urn:csabs:axiom/RegularExpression-defining-profile",
      "urn:csabs:axiom/FormalLanguage-language-operations"
    ],
    "proofSketch": "Disjoint constructors distinguish empty-language syntax from empty-word syntax.",
    "reviewStatus": "Registered witness; verified only by fresh compiler and axiom audit.",
    "source": [
      "urn:csabs:source/language-acquisition-regex",
      "urn:csabs:source/language-acquisition-lean-models"
    ],
    "sourceLocator": "RegularExpression inductive constructors zero, epsilon, char, plus, comp, star; matches'; rmatch_iff_matches'; Catalog.regex_syntax_distinct",
    "sourceNote": "Derived for the specified interpretation. Disjoint constructors distinguish empty-language syntax from empty-word syntax.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {A : Type} [Fintype A] , (0 : Catalog.RegularExpression A) ≠ 1",
    "formulationSource": "urn:csabs:source/language-acquisition-lean-models",
    "formulationLocator": "Catalog.regex_syntax_distinct",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Disjoint constructors distinguish empty-language syntax from empty-word syntax.",
    "leanModelLimitations": "Selected mathematical profile only; no blanket software refinement, missing closure theorem or automata-equivalence proof. Verification requires fresh compiler and axiom-audit evidence.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/FormalLanguage-language-operations\": \"Instantiate exact finite words/languages and the finite-nonterminal grammar profile; these premises describe the interpretation, not hypotheses of their own satisfaction. Disjoint constructors distinguish empty-language syntax from empty-word syntax.\", \"urn:csabs:axiom/RegularExpression-defining-profile\": \"Instantiate exact finite words/languages and the finite-nonterminal grammar profile; these premises describe the interpretation, not hypotheses of their own satisfaction. Disjoint constructors distinguish empty-language syntax from empty-word syntax.\"}"
  },
  {
    "id": "urn:csabs:theorem/RegularExpression-semantic-union-idempotence",
    "type": "Theorem",
    "name": "semantic-union-idempotence",
    "statement": "Language union is idempotent by extensional set membership. The syntax trees need not be equal.",
    "formalStatement": "∀ {A : Type} [Fintype A] (r : Catalog.RegularExpression A), (r + r).matches' = r.matches'",
    "assumptions": [
      "Exactly the displayed typed binders; fixed finite alphabet and exact equality; matching additionally requires DecidableEq."
    ],
    "appliesTo": [
      "urn:csabs:concept/RegularExpression"
    ],
    "dependsOn": [
      "urn:csabs:axiom/RegularExpression-defining-profile",
      "urn:csabs:axiom/FormalLanguage-language-operations",
      "urn:csabs:axiom/FormalLanguage-union-membership"
    ],
    "proofSketch": "Language union is idempotent by extensional set membership. The syntax trees need not be equal.",
    "reviewStatus": "Registered witness; verified only by fresh compiler and axiom audit.",
    "source": [
      "urn:csabs:source/language-acquisition-regex",
      "urn:csabs:source/language-acquisition-lean-models"
    ],
    "sourceLocator": "RegularExpression inductive constructors zero, epsilon, char, plus, comp, star; matches'; rmatch_iff_matches'; Catalog.regex_union_idempotent",
    "sourceNote": "Derived for the specified interpretation. Language union is idempotent by extensional set membership. The syntax trees need not be equal.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {A : Type} [Fintype A] (r : Catalog.RegularExpression A), (r + r).matches' = r.matches'",
    "formulationSource": "urn:csabs:source/language-acquisition-lean-models",
    "formulationLocator": "Catalog.regex_union_idempotent",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Language union is idempotent by extensional set membership. The syntax trees need not be equal.",
    "leanModelLimitations": "Selected mathematical profile only; no blanket software refinement, missing closure theorem or automata-equivalence proof. Verification requires fresh compiler and axiom-audit evidence.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/FormalLanguage-language-operations\": \"Instantiate exact finite words/languages and the finite-nonterminal grammar profile; these premises describe the interpretation, not hypotheses of their own satisfaction. Language union is idempotent by extensional set membership. The syntax trees need not be equal.\", \"urn:csabs:axiom/FormalLanguage-union-membership\": \"Instantiate exact finite words/languages and the finite-nonterminal grammar profile; these premises describe the interpretation, not hypotheses of their own satisfaction. Language union is idempotent by extensional set membership. The syntax trees need not be equal.\", \"urn:csabs:axiom/RegularExpression-defining-profile\": \"Instantiate exact finite words/languages and the finite-nonterminal grammar profile; these premises describe the interpretation, not hypotheses of their own satisfaction. Language union is idempotent by extensional set membership. The syntax trees need not be equal.\"}"
  },
  {
    "id": "urn:csabs:theorem/RegularExpression-semantic-concat-associativity",
    "type": "Theorem",
    "name": "semantic-concat-associativity",
    "statement": "Language multiplication is associative because word append is associative; only denotational equality is claimed.",
    "formalStatement": "∀ {A : Type} [Fintype A] (r s t : Catalog.RegularExpression A), ((r * s) * t).matches' = (r * (s * t)).matches'",
    "assumptions": [
      "Exactly the displayed typed binders; fixed finite alphabet and exact equality; matching additionally requires DecidableEq."
    ],
    "appliesTo": [
      "urn:csabs:concept/RegularExpression"
    ],
    "dependsOn": [
      "urn:csabs:axiom/RegularExpression-defining-profile",
      "urn:csabs:axiom/FormalLanguage-language-operations",
      "urn:csabs:law/FormalLanguage-concatenation-monoid"
    ],
    "proofSketch": "Language multiplication is associative because word append is associative; only denotational equality is claimed.",
    "reviewStatus": "Registered witness; verified only by fresh compiler and axiom audit.",
    "source": [
      "urn:csabs:source/language-acquisition-regex",
      "urn:csabs:source/language-acquisition-lean-models"
    ],
    "sourceLocator": "RegularExpression inductive constructors zero, epsilon, char, plus, comp, star; matches'; rmatch_iff_matches'; Catalog.regex_concat_associative",
    "sourceNote": "Derived for the specified interpretation. Language multiplication is associative because word append is associative; only denotational equality is claimed.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {A : Type} [Fintype A] (r s t : Catalog.RegularExpression A), ((r * s) * t).matches' = (r * (s * t)).matches'",
    "formulationSource": "urn:csabs:source/language-acquisition-lean-models",
    "formulationLocator": "Catalog.regex_concat_associative",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Language multiplication is associative because word append is associative; only denotational equality is claimed.",
    "leanModelLimitations": "Selected mathematical profile only; no blanket software refinement, missing closure theorem or automata-equivalence proof. Verification requires fresh compiler and axiom-audit evidence.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/FormalLanguage-language-operations\": \"Instantiate exact finite words/languages and the finite-nonterminal grammar profile; these premises describe the interpretation, not hypotheses of their own satisfaction. Language multiplication is associative because word append is associative; only denotational equality is claimed.\", \"urn:csabs:axiom/RegularExpression-defining-profile\": \"Instantiate exact finite words/languages and the finite-nonterminal grammar profile; these premises describe the interpretation, not hypotheses of their own satisfaction. Language multiplication is associative because word append is associative; only denotational equality is claimed.\", \"urn:csabs:law/FormalLanguage-concatenation-monoid\": \"Instantiate exact finite words/languages and the finite-nonterminal grammar profile; these premises describe the interpretation, not hypotheses of their own satisfaction. Language multiplication is associative because word append is associative; only denotational equality is claimed.\"}"
  },
  {
    "id": "urn:csabs:theorem/RegularExpression-star-empty-word",
    "type": "Theorem",
    "name": "star-empty-word",
    "statement": "The zero-factor word belongs to every Kleene star, even when the operand denotes the empty language.",
    "formalStatement": "∀ {A : Type} [Fintype A] (r : Catalog.RegularExpression A), [] ∈ r.star.matches'",
    "assumptions": [
      "Exactly the displayed typed binders; fixed finite alphabet and exact equality; matching additionally requires DecidableEq."
    ],
    "appliesTo": [
      "urn:csabs:concept/RegularExpression"
    ],
    "dependsOn": [
      "urn:csabs:axiom/RegularExpression-defining-profile",
      "urn:csabs:axiom/FormalLanguage-language-operations"
    ],
    "proofSketch": "The zero-factor word belongs to every Kleene star, even when the operand denotes the empty language.",
    "reviewStatus": "Registered witness; verified only by fresh compiler and axiom audit.",
    "source": [
      "urn:csabs:source/language-acquisition-regex",
      "urn:csabs:source/language-acquisition-lean-models"
    ],
    "sourceLocator": "RegularExpression inductive constructors zero, epsilon, char, plus, comp, star; matches'; rmatch_iff_matches'; Catalog.regex_star_empty_word",
    "sourceNote": "Derived for the specified interpretation. The zero-factor word belongs to every Kleene star, even when the operand denotes the empty language.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {A : Type} [Fintype A] (r : Catalog.RegularExpression A), [] ∈ r.star.matches'",
    "formulationSource": "urn:csabs:source/language-acquisition-lean-models",
    "formulationLocator": "Catalog.regex_star_empty_word",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "The zero-factor word belongs to every Kleene star, even when the operand denotes the empty language.",
    "leanModelLimitations": "Selected mathematical profile only; no blanket software refinement, missing closure theorem or automata-equivalence proof. Verification requires fresh compiler and axiom-audit evidence.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/FormalLanguage-language-operations\": \"Instantiate exact finite words/languages and the finite-nonterminal grammar profile; these premises describe the interpretation, not hypotheses of their own satisfaction. The zero-factor word belongs to every Kleene star, even when the operand denotes the empty language.\", \"urn:csabs:axiom/RegularExpression-defining-profile\": \"Instantiate exact finite words/languages and the finite-nonterminal grammar profile; these premises describe the interpretation, not hypotheses of their own satisfaction. The zero-factor word belongs to every Kleene star, even when the operand denotes the empty language.\"}"
  },
  {
    "id": "urn:csabs:theorem/RegularExpression-matching-correctness",
    "type": "Theorem",
    "name": "matching-correctness",
    "statement": "Instantiate the pinned derivative-matcher correctness theorem; the result concerns whole finite words with exact decidable letter equality.",
    "formalStatement": "∀ {A : Type} [Fintype A] [DecidableEq A] (r : Catalog.RegularExpression A) (w : List A), r.rmatch w = true ↔ w ∈ r.matches'",
    "assumptions": [
      "Exactly the displayed typed binders; fixed finite alphabet and exact equality; matching additionally requires DecidableEq."
    ],
    "appliesTo": [
      "urn:csabs:concept/RegularExpression"
    ],
    "dependsOn": [
      "urn:csabs:axiom/RegularExpression-defining-profile",
      "urn:csabs:axiom/FormalLanguage-language-operations"
    ],
    "proofSketch": "Instantiate the pinned derivative-matcher correctness theorem; the result concerns whole finite words with exact decidable letter equality.",
    "reviewStatus": "Registered witness; verified only by fresh compiler and axiom audit.",
    "source": [
      "urn:csabs:source/language-acquisition-regex",
      "urn:csabs:source/language-acquisition-lean-models"
    ],
    "sourceLocator": "RegularExpression inductive constructors zero, epsilon, char, plus, comp, star; matches'; rmatch_iff_matches'; Catalog.regex_match_correct",
    "sourceNote": "Derived for the specified interpretation. Instantiate the pinned derivative-matcher correctness theorem; the result concerns whole finite words with exact decidable letter equality.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {A : Type} [Fintype A] [DecidableEq A] (r : Catalog.RegularExpression A) (w : List A), r.rmatch w = true ↔ w ∈ r.matches'",
    "formulationSource": "urn:csabs:source/language-acquisition-lean-models",
    "formulationLocator": "Catalog.regex_match_correct",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Instantiate the pinned derivative-matcher correctness theorem; the result concerns whole finite words with exact decidable letter equality.",
    "leanModelLimitations": "Selected mathematical profile only; no blanket software refinement, missing closure theorem or automata-equivalence proof. Verification requires fresh compiler and axiom-audit evidence.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/FormalLanguage-language-operations\": \"Instantiate exact finite words/languages and the finite-nonterminal grammar profile; these premises describe the interpretation, not hypotheses of their own satisfaction. Instantiate the pinned derivative-matcher correctness theorem; the result concerns whole finite words with exact decidable letter equality.\", \"urn:csabs:axiom/RegularExpression-defining-profile\": \"Instantiate exact finite words/languages and the finite-nonterminal grammar profile; these premises describe the interpretation, not hypotheses of their own satisfaction. Instantiate the pinned derivative-matcher correctness theorem; the result concerns whole finite words with exact decidable letter equality.\"}"
  }
]
```
<!-- graph-record:end -->
