# Predicate Logic

First-order formulas over a signature, interpreted in a nonempty domain with variable assignments and quantifiers.

**Notation:** M,ρ ⊨ ∀x φ iff ∀a∈D: M,ρ[x↦a] ⊨ φ

**Stable ID:** `urn:csabs:concept/PredicateLogic`

**Categories:** Logic and proof

**Kind:** semantic-model

**Prerequisites:** [Propositional Logic](PropositionalLogic.md), [First-order formula syntax with named variables](FirstOrderFormula.md)

**Related concepts:** [Classical first-order natural deduction with equality](FirstOrderNaturalDeduction.md)

## Backlinks

- [First-order formula syntax with named variables](FirstOrderFormula.md) — `relatedConcept`
- [Classical first-order natural deduction with equality](FirstOrderNaturalDeduction.md) — `requiresConcept`
- [Functional dependency on a relational schema](FunctionalDependency.md) — `requiresConcept`
- [Hoare Triple](HoareTriple.md) — `requiresConcept`
- [Classical propositional modal logic K](ModalLogic.md) — `relatedConcept`
- [Predicate-restricted subtype](Subtype.md) — `requiresConcept`
- [Free ranked term algebra with variables](TermAlgebra.md) — `relatedConcept`

## Interface and scope

**axiomBasis:** Selected presentation: First-order formulas over a signature, interpreted in a nonempty domain with variable assignments and quantifiers. Governing rules: A first-order interpretation has a nonempty domain and total interpretations of function symbols. Quantifier semantics ranges over all domain values and respects variable assignments. Logical connectives are interpreted classically at each structure and assignment.

**basisKind:** defined-structure

**basisScope:** Classical single-sorted first-order semantics with domain D≠∅, total function symbols, arbitrary relations and equality as actual domain identity. Formula syntax may use the named-variable profile in FirstOrderFormula; ∃, ∨, ⇒, ↔ and ⊤ may be expanded as classical macros. Semantic queries are predicates, not general decision procedures. Sentence metatheorems below use the countable signature profile explicitly.

**verificationObligation:** Instantiate carrier, equality, and stated semantic conventions before using this entry.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** Editorial source and mathematical interface review; no compiled proof witness asserted.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-PredicateLogic-basis-satisfies"></a>

### satisfies

`urn:csabs:operation/PredicateLogic-basis-satisfies`

**signature:** satisfies : Structure×Assignment×Formula→Prop

**description:** Interprets first-order satisfaction; this is not a general decision algorithm.

**precondition:** Well-formed formula over M's signature; nonempty D; total assignment ρ:V→D.

**totality:** A total semantic relation, not a computability assertion.

**outcome:** The satisfaction proposition M,ρ⊨φ.

<a id="node-urn-csabs-operation-PredicateLogic-term-value"></a>

### term-value

`urn:csabs:operation/PredicateLogic-term-value`

**signature:** value:Structure×Assignment×Term→D; update:Assignment×V×D→Assignment

**description:** Evaluates terms recursively and updates one variable assignment.

**precondition:** Structure M has nonempty domain D and total interpretations; terms and assignments have the indicated types.

**totality:** Total on the stated domain.

**outcome:** Evaluates terms recursively and updates one variable assignment.

<a id="node-urn-csabs-operation-PredicateLogic-semantic-queries"></a>

### semantic-queries

`urn:csabs:operation/PredicateLogic-semantic-queries`

**signature:** valid:Sentence→Prop; sat:𝒫(Sentence)→Prop; entails:𝒫(Sentence)×Sentence→Prop; equivalent:Form²→Prop

**description:** Defines model-based queries; equivalence of open formulas uses the same structure and assignment.

**precondition:** Inputs belong to the indicated carriers.

**totality:** Total on the stated domain.

**outcome:** Defines model-based queries; equivalence of open formulas uses the same structure and assignment.

**formalStatement:** For sentences φ, M⊨φ ⇔ ∀ρ,M,ρ⊨φ; M⊨Γ ⇔ ∀ψ∈Γ,M⊨ψ; Γ⊨φ ⇔ ∀M,(M⊨Γ⇒M⊨φ); sat(Γ) ⇔ ∃M,M⊨Γ; valid(φ) ⇔ ∅⊨φ; equivalent(φ,ψ) ⇔ ∀M ρ,(M,ρ⊨φ ⇔ M,ρ⊨ψ).

## Axioms and defining rules

<a id="node-urn-csabs-axiom-PredicateLogic-structure"></a>

### structure

`urn:csabs:axiom/PredicateLogic-structure`

**statement:** A first-order interpretation has a nonempty domain and total interpretations of function symbols.

**formalStatement:** D≠∅; f with arity n has f^M:D^n→D; R with arity n has R^M⊆D^n; equality is domain identity

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source and mathematical interface review; no compiled proof witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [Open Logic Text: First-order Logic (revision 9620cc7, 2026-07-12)](https://builds.openlogicproject.org/content/first-order-logic/first-order-logic.pdf); accessedOn: 2026-11-08; sourceRole: Definitions, inference rules and metatheory; individual records specify exact locators and adaptations.

**sourceLocator:** §3.2, Definition 3.1; §3.4, Definition 3.8

**sourceNote:** Verified against the cited definitions. Existing stable ID and classical semantics retained; derived results follow from the explicitly linked premises.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-PredicateLogic-quantifiers"></a>

### quantifiers

`urn:csabs:axiom/PredicateLogic-quantifiers`

**statement:** Quantifier semantics ranges over all domain values and respects variable assignments.

**formalStatement:** M,ρ⊨∀x φ iff ∀a∈D:M,ρ[x↦a]⊨φ; M,ρ⊨∃x φ iff ∃a∈D:M,ρ[x↦a]⊨φ

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source and mathematical interface review; no compiled proof witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [Open Logic Text: First-order Logic (revision 9620cc7, 2026-07-12)](https://builds.openlogicproject.org/content/first-order-logic/first-order-logic.pdf); accessedOn: 2026-11-08; sourceRole: Definitions, inference rules and metatheory; individual records specify exact locators and adaptations.

**sourceLocator:** §3.4, Definition 3.11

**sourceNote:** Verified against the cited definitions. Existing stable ID and classical semantics retained; derived results follow from the explicitly linked premises.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-PredicateLogic-connectives"></a>

### connectives

`urn:csabs:axiom/PredicateLogic-connectives`

**statement:** Logical connectives are interpreted classically at each structure and assignment.

**formalStatement:** M,ρ⊨¬φ iff not(M,ρ⊨φ); M,ρ⊨φ∧ψ iff (M,ρ⊨φ and M,ρ⊨ψ); ∨,⇒ use classical Boolean semantics

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source and mathematical interface review; no compiled proof witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [Open Logic Text: First-order Logic (revision 9620cc7, 2026-07-12)](https://builds.openlogicproject.org/content/first-order-logic/first-order-logic.pdf); accessedOn: 2026-11-08; sourceRole: Definitions, inference rules and metatheory; individual records specify exact locators and adaptations.

**sourceLocator:** §3.4, Definition 3.11

**sourceNote:** Verified against the cited definitions. Existing stable ID and classical semantics retained; derived results follow from the explicitly linked premises.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-PredicateLogic-atomic-satisfaction"></a>

### atomic-satisfaction

`urn:csabs:axiom/PredicateLogic-atomic-satisfaction`

**statement:** Assignments evaluate terms and atomic formulas; updating changes one variable only.

**formalStatement:** value(M,ρ,x)=ρ(x); value(M,ρ,f(ts))=f^M(value(M,ρ,ts)); ρ[x↦a](y)=a if y=x else ρ(y); M,ρ⊨R(ts) iff value(M,ρ,ts)∈R^M; M,ρ⊨t=u iff value(M,ρ,t)=value(M,ρ,u); M,ρ⊭⊥.

**assumptions:** Classical single-sorted first-order semantics with domain D≠∅, total function symbols, arbitrary relations and equality as actual domain identity. Formula syntax may use the named-variable profile in FirstOrderFormula; ∃, ∨, ⇒, ↔ and ⊤ may be expanded as classical macros. Semantic queries are predicates, not general decision procedures. Sentence metatheorems below use the countable signature profile explicitly.

**reviewStatus:** Editorial source and mathematical interface review; no compiled proof witness asserted.

**notationLanguage:** informal mathematical Unicode

**ruleRole:** defining-rule

**source:** [Open Logic Text: First-order Logic (revision 9620cc7, 2026-07-12)](https://builds.openlogicproject.org/content/first-order-logic/first-order-logic.pdf); accessedOn: 2026-11-08; sourceRole: Definitions, inference rules and metatheory; individual records specify exact locators and adaptations.

**sourceLocator:** §3.4 Definitions 3.7–3.11

**sourceNote:** Selected presentation in catalog notation; finite raw syntax and the stated primitive basis are explicit choices. No executable proof is implied.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-PredicateLogic-semantic-queries"></a>

### semantic-queries

`urn:csabs:axiom/PredicateLogic-semantic-queries`

**statement:** Sentence consequence and satisfiability range over all structures of the fixed signature.

**formalStatement:** For sentences φ, M⊨φ ⇔ ∀ρ,M,ρ⊨φ; M⊨Γ ⇔ ∀ψ∈Γ,M⊨ψ; Γ⊨φ ⇔ ∀M,(M⊨Γ⇒M⊨φ); sat(Γ) ⇔ ∃M,M⊨Γ; valid(φ) ⇔ ∅⊨φ; equivalent(φ,ψ) ⇔ ∀M ρ,(M,ρ⊨φ ⇔ M,ρ⊨ψ).

**assumptions:** Γ and φ in sat, valid and entails are sentences of one fixed signature; equivalent also admits open formulas.; All structures have nonempty domains; ρ is total.

**reviewStatus:** Editorial source and mathematical interface review; no compiled proof witness asserted.

**notationLanguage:** informal mathematical Unicode

**ruleRole:** defining-rule

**source:** [Open Logic Text: First-order Logic (revision 9620cc7, 2026-07-12)](https://builds.openlogicproject.org/content/first-order-logic/first-order-logic.pdf); accessedOn: 2026-11-08; sourceRole: Definitions, inference rules and metatheory; individual records specify exact locators and adaptations.

**sourceLocator:** §3.5 Definitions 3.16–3.17; §3.7 Definitions 3.24–3.26

**sourceNote:** Selected presentation in catalog notation; finite raw syntax and the stated primitive basis are explicit choices. No executable proof is implied.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-PredicateLogic-core"></a>

### law/PredicateLogic-core

`urn:csabs:law/PredicateLogic-core`

**statement:** Universal instantiation is sound for substitution free of variable capture.

**formalStatement:** ∀x φ ⇒ φ[t/x], when t is free for x in φ

**reviewStatus:** Editorial source and mathematical interface review; no compiled proof witness asserted.

**assumptions:** Use the carrier and semantic convention in the linked concept definition.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [structure](PredicateLogic.md#node-urn-csabs-axiom-PredicateLogic-structure); [quantifiers](PredicateLogic.md#node-urn-csabs-axiom-PredicateLogic-quantifiers); [connectives](PredicateLogic.md#node-urn-csabs-axiom-PredicateLogic-connectives); [substitution-semantics](PredicateLogic.md#node-urn-csabs-theorem-PredicateLogic-substitution-semantics)

**source:** [Open Logic Text: First-order Logic (revision 9620cc7, 2026-07-12)](https://builds.openlogicproject.org/content/first-order-logic/first-order-logic.pdf); accessedOn: 2026-11-08; sourceRole: Definitions, inference rules and metatheory; individual records specify exact locators and adaptations.

**sourceLocator:** §2.9, Definitions 2.38 and 2.40; §3.6, Proposition 3.23; §7.3 universal elimination

**sourceNote:** Verified against the cited definitions. Existing stable ID and classical semantics retained; derived results follow from the explicitly linked premises.

**provenanceKind:** derived

**proofSketch:** Evaluate t in M under ρ; apply universal satisfaction at this element and the capture-free substitution lemma.

<a id="node-urn-csabs-law-PredicateLogic-sentence-assignment-independent"></a>

### sentence-assignment-independent

`urn:csabs:law/PredicateLogic-sentence-assignment-independent`

**statement:** A sentence has the same truth value under every assignment.

**formalStatement:** FV(φ)=∅ ⇒ (M,ρ⊨φ ⇔ M,ρ′⊨φ)

**assumptions:** Classical single-sorted first-order semantics with domain D≠∅, total function symbols, arbitrary relations and equality as actual domain identity. Formula syntax may use the named-variable profile in FirstOrderFormula; ∃, ∨, ⇒, ↔ and ⊤ may be expanded as classical macros. Semantic queries are predicates, not general decision procedures. Sentence metatheorems below use the countable signature profile explicitly.

**reviewStatus:** Editorial source and mathematical interface review; no compiled proof witness asserted.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [assignment-coincidence](PredicateLogic.md#node-urn-csabs-theorem-PredicateLogic-assignment-coincidence); [free-variables](FirstOrderFormula.md#node-urn-csabs-axiom-FirstOrderFormula-free-variables)

**proofSketch:** Apply assignment coincidence: agreement on an empty free-variable set is vacuous.

**source:** [Open Logic Text: First-order Logic (revision 9620cc7, 2026-07-12)](https://builds.openlogicproject.org/content/first-order-logic/first-order-logic.pdf); accessedOn: 2026-11-08; sourceRole: Definitions, inference rules and metatheory; individual records specify exact locators and adaptations.

**sourceLocator:** §3.5 Corollary 3.15

**sourceNote:** Selected presentation in catalog notation; finite raw syntax and the stated primitive basis are explicit choices. No executable proof is implied.

**provenanceKind:** derived

## Theorems

<a id="node-urn-csabs-theorem-PredicateLogic-quantifier-duality"></a>

### quantifier-duality

`urn:csabs:theorem/PredicateLogic-quantifier-duality`

**statement:** Classical universal quantification is dual to existential quantification.

**formalStatement:** ∀x φ ↔ ¬∃x ¬φ

**proofSketch:** Unfold satisfaction and classical negation of an existential statement.

**assumptions:** The explicit basis, carriers, and side conditions stated for PredicateLogic apply.

**dependsOn:** [structure](PredicateLogic.md#node-urn-csabs-axiom-PredicateLogic-structure); [quantifiers](PredicateLogic.md#node-urn-csabs-axiom-PredicateLogic-quantifiers); [connectives](PredicateLogic.md#node-urn-csabs-axiom-PredicateLogic-connectives)

**reviewStatus:** Editorial source and mathematical interface review; no compiled proof witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [Open Logic Text: First-order Logic (revision 9620cc7, 2026-07-12)](https://builds.openlogicproject.org/content/first-order-logic/first-order-logic.pdf); accessedOn: 2026-11-08; sourceRole: Definitions, inference rules and metatheory; individual records specify exact locators and adaptations.

**sourceLocator:** §3.4, Definition 3.11, universal/existential satisfaction and negation

**sourceNote:** Verified against the cited definitions. Existing stable ID and classical semantics retained; derived results follow from the explicitly linked premises.

**provenanceKind:** derived

<a id="node-urn-csabs-theorem-PredicateLogic-substitution-semantics"></a>

### substitution-semantics

`urn:csabs:theorem/PredicateLogic-substitution-semantics`

**statement:** Capture-free syntactic substitution agrees with semantic assignment update.

**formalStatement:** value(M,ρ,s[t/x])=value(M,ρ[x↦value(M,ρ,t)],s); M,ρ⊨φ[t/x] ⇔ M,ρ[x↦value(M,ρ,t)]⊨φ.

**assumptions:** t is free for x in φ.; M, ρ, terms and formulas have the typed carriers of PredicateLogic and FirstOrderFormula.

**reviewStatus:** Editorial source and mathematical interface review; no compiled proof witness asserted.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [substitution](FirstOrderFormula.md#node-urn-csabs-axiom-FirstOrderFormula-substitution); [free-syntax](FirstOrderFormula.md#node-urn-csabs-axiom-FirstOrderFormula-free-syntax); [structure](PredicateLogic.md#node-urn-csabs-axiom-PredicateLogic-structure); [atomic-satisfaction](PredicateLogic.md#node-urn-csabs-axiom-PredicateLogic-atomic-satisfaction); [quantifiers](PredicateLogic.md#node-urn-csabs-axiom-PredicateLogic-quantifiers); [connectives](PredicateLogic.md#node-urn-csabs-axiom-PredicateLogic-connectives); [induction](TermAlgebra.md#node-urn-csabs-axiom-TermAlgebra-induction)

**proofSketch:** Prove the term equality by term induction. Induct on φ for satisfaction, using the term equality in atomic cases. Under a different quantifier, the free-for condition prevents capture and ensures the relevant updates commute; a binder for x stops substitution.

**source:** [Open Logic Text: First-order Logic (revision 9620cc7, 2026-07-12)](https://builds.openlogicproject.org/content/first-order-logic/first-order-logic.pdf); accessedOn: 2026-11-08; sourceRole: Definitions, inference rules and metatheory; individual records specify exact locators and adaptations.

**sourceLocator:** §3.6 Propositions 3.22–3.23; §2.9 Definition 2.40

**sourceNote:** Selected presentation in catalog notation; finite raw syntax and the stated primitive basis are explicit choices. No executable proof is implied.

**provenanceKind:** derived

<a id="node-urn-csabs-theorem-PredicateLogic-assignment-coincidence"></a>

### assignment-coincidence

`urn:csabs:theorem/PredicateLogic-assignment-coincidence`

**statement:** Truth depends only on the free variables of a formula.

**formalStatement:** (∀x∈FV(φ),ρ(x)=ρ′(x)) ⇒ (M,ρ⊨φ ⇔ M,ρ′⊨φ)

**assumptions:** Classical single-sorted first-order semantics with domain D≠∅, total function symbols, arbitrary relations and equality as actual domain identity. Formula syntax may use the named-variable profile in FirstOrderFormula; ∃, ∨, ⇒, ↔ and ⊤ may be expanded as classical macros. Semantic queries are predicates, not general decision procedures. Sentence metatheorems below use the countable signature profile explicitly.

**reviewStatus:** Editorial source and mathematical interface review; no compiled proof witness asserted.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [free-syntax](FirstOrderFormula.md#node-urn-csabs-axiom-FirstOrderFormula-free-syntax); [free-variables](FirstOrderFormula.md#node-urn-csabs-axiom-FirstOrderFormula-free-variables); [atomic-satisfaction](PredicateLogic.md#node-urn-csabs-axiom-PredicateLogic-atomic-satisfaction); [quantifiers](PredicateLogic.md#node-urn-csabs-axiom-PredicateLogic-quantifiers); [connectives](PredicateLogic.md#node-urn-csabs-axiom-PredicateLogic-connectives); [induction](TermAlgebra.md#node-urn-csabs-axiom-TermAlgebra-induction)

**proofSketch:** Prove term evaluation depends on its variables by induction. Induct on the formula. At ∀x update both assignments to the same arbitrary element; they then agree on the free variables of the body.

**source:** [Open Logic Text: First-order Logic (revision 9620cc7, 2026-07-12)](https://builds.openlogicproject.org/content/first-order-logic/first-order-logic.pdf); accessedOn: 2026-11-08; sourceRole: Definitions, inference rules and metatheory; individual records specify exact locators and adaptations.

**sourceLocator:** §3.5 Proposition 3.14

**sourceNote:** Selected presentation in catalog notation; finite raw syntax and the stated primitive basis are explicit choices. No executable proof is implied.

**provenanceKind:** derived

## Concept provenance

- [Open Logic Text: First-order Logic (revision 9620cc7, 2026-07-12)](https://builds.openlogicproject.org/content/first-order-logic/first-order-logic.pdf); accessedOn: 2026-11-08; sourceRole: Definitions, inference rules and metatheory; individual records specify exact locators and adaptations.

**sourceLocator:** §§2.2–2.3 and 3.2–3.4: languages, structures and satisfaction

**sourceNote:** Verified against the cited definitions. Existing stable ID and classical semantics retained; derived results follow from the explicitly linked premises.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/PredicateLogic",
    "type": "Concept",
    "shortForm": "PredicateLogic",
    "fullName": "Predicate Logic",
    "category": [
      "urn:csabs:category/logic"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "definition": "First-order formulas over a signature, interpreted in a nonempty domain with variable assignments and quantifiers.",
    "notation": "M,ρ ⊨ ∀x φ iff ∀a∈D: M,ρ[x↦a] ⊨ φ",
    "hasOperation": [
      "urn:csabs:operation/PredicateLogic-basis-satisfies",
      "urn:csabs:operation/PredicateLogic-term-value",
      "urn:csabs:operation/PredicateLogic-semantic-queries"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/PredicateLogic-structure",
      "urn:csabs:axiom/PredicateLogic-quantifiers",
      "urn:csabs:axiom/PredicateLogic-connectives",
      "urn:csabs:axiom/PredicateLogic-atomic-satisfaction",
      "urn:csabs:axiom/PredicateLogic-semantic-queries"
    ],
    "hasLaw": [
      "urn:csabs:law/PredicateLogic-core",
      "urn:csabs:law/PredicateLogic-sentence-assignment-independent"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/PredicateLogic-quantifier-duality",
      "urn:csabs:theorem/PredicateLogic-substitution-semantics",
      "urn:csabs:theorem/PredicateLogic-assignment-coincidence"
    ],
    "requiresConcept": [
      "urn:csabs:concept/PropositionalLogic",
      "urn:csabs:concept/FirstOrderFormula"
    ],
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Instantiate carrier, equality, and stated semantic conventions before using this entry.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: First-order formulas over a signature, interpreted in a nonempty domain with variable assignments and quantifiers. Governing rules: A first-order interpretation has a nonempty domain and total interpretations of function symbols. Quantifier semantics ranges over all domain values and respects variable assignments. Logical connectives are interpreted classically at each structure and assignment.",
    "basisKind": "defined-structure",
    "basisScope": "Classical single-sorted first-order semantics with domain D≠∅, total function symbols, arbitrary relations and equality as actual domain identity. Formula syntax may use the named-variable profile in FirstOrderFormula; ∃, ∨, ⇒, ↔ and ⊤ may be expanded as classical macros. Semantic queries are predicates, not general decision procedures. Sentence metatheorems below use the countable signature profile explicitly.",
    "reviewStatus": "Editorial source and mathematical interface review; no compiled proof witness asserted.",
    "source": [
      "urn:csabs:source/open-logic-first-order-2026"
    ],
    "sourceLocator": "§§2.2–2.3 and 3.2–3.4: languages, structures and satisfaction",
    "sourceNote": "Verified against the cited definitions. Existing stable ID and classical semantics retained; derived results follow from the explicitly linked premises.",
    "provenanceKind": "adapted",
    "relatedConcept": [
      "urn:csabs:concept/FirstOrderNaturalDeduction"
    ]
  },
  {
    "id": "urn:csabs:operation/PredicateLogic-basis-satisfies",
    "type": "Operation",
    "name": "satisfies",
    "signature": "satisfies : Structure×Assignment×Formula→Prop",
    "description": "Interprets first-order satisfaction; this is not a general decision algorithm.",
    "concept": "urn:csabs:concept/PredicateLogic",
    "precondition": "Well-formed formula over M's signature; nonempty D; total assignment ρ:V→D.",
    "totality": "A total semantic relation, not a computability assertion.",
    "outcome": "The satisfaction proposition M,ρ⊨φ."
  },
  {
    "id": "urn:csabs:operation/PredicateLogic-term-value",
    "type": "Operation",
    "name": "term-value",
    "signature": "value:Structure×Assignment×Term→D; update:Assignment×V×D→Assignment",
    "description": "Evaluates terms recursively and updates one variable assignment.",
    "concept": "urn:csabs:concept/PredicateLogic",
    "precondition": "Structure M has nonempty domain D and total interpretations; terms and assignments have the indicated types.",
    "totality": "Total on the stated domain.",
    "outcome": "Evaluates terms recursively and updates one variable assignment."
  },
  {
    "id": "urn:csabs:operation/PredicateLogic-semantic-queries",
    "type": "Operation",
    "name": "semantic-queries",
    "signature": "valid:Sentence→Prop; sat:𝒫(Sentence)→Prop; entails:𝒫(Sentence)×Sentence→Prop; equivalent:Form²→Prop",
    "description": "Defines model-based queries; equivalence of open formulas uses the same structure and assignment.",
    "concept": "urn:csabs:concept/PredicateLogic",
    "precondition": "Inputs belong to the indicated carriers.",
    "totality": "Total on the stated domain.",
    "outcome": "Defines model-based queries; equivalence of open formulas uses the same structure and assignment.",
    "formalStatement": "For sentences φ, M⊨φ ⇔ ∀ρ,M,ρ⊨φ; M⊨Γ ⇔ ∀ψ∈Γ,M⊨ψ; Γ⊨φ ⇔ ∀M,(M⊨Γ⇒M⊨φ); sat(Γ) ⇔ ∃M,M⊨Γ; valid(φ) ⇔ ∅⊨φ; equivalent(φ,ψ) ⇔ ∀M ρ,(M,ρ⊨φ ⇔ M,ρ⊨ψ)."
  },
  {
    "id": "urn:csabs:axiom/PredicateLogic-structure",
    "type": "Axiom",
    "name": "structure",
    "statement": "A first-order interpretation has a nonempty domain and total interpretations of function symbols.",
    "formalStatement": "D≠∅; f with arity n has f^M:D^n→D; R with arity n has R^M⊆D^n; equality is domain identity",
    "appliesTo": [
      "urn:csabs:concept/PredicateLogic"
    ],
    "assumptions": [
      "All variables range over the carriers and semantic conventions specified in this concept."
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source and mathematical interface review; no compiled proof witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/open-logic-first-order-2026"
    ],
    "sourceLocator": "§3.2, Definition 3.1; §3.4, Definition 3.8",
    "sourceNote": "Verified against the cited definitions. Existing stable ID and classical semantics retained; derived results follow from the explicitly linked premises.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/PredicateLogic-quantifiers",
    "type": "Axiom",
    "name": "quantifiers",
    "statement": "Quantifier semantics ranges over all domain values and respects variable assignments.",
    "formalStatement": "M,ρ⊨∀x φ iff ∀a∈D:M,ρ[x↦a]⊨φ; M,ρ⊨∃x φ iff ∃a∈D:M,ρ[x↦a]⊨φ",
    "appliesTo": [
      "urn:csabs:concept/PredicateLogic"
    ],
    "assumptions": [
      "All variables range over the carriers and semantic conventions specified in this concept."
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source and mathematical interface review; no compiled proof witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/open-logic-first-order-2026"
    ],
    "sourceLocator": "§3.4, Definition 3.11",
    "sourceNote": "Verified against the cited definitions. Existing stable ID and classical semantics retained; derived results follow from the explicitly linked premises.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/PredicateLogic-connectives",
    "type": "Axiom",
    "name": "connectives",
    "statement": "Logical connectives are interpreted classically at each structure and assignment.",
    "formalStatement": "M,ρ⊨¬φ iff not(M,ρ⊨φ); M,ρ⊨φ∧ψ iff (M,ρ⊨φ and M,ρ⊨ψ); ∨,⇒ use classical Boolean semantics",
    "appliesTo": [
      "urn:csabs:concept/PredicateLogic"
    ],
    "assumptions": [
      "All variables range over the carriers and semantic conventions specified in this concept."
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source and mathematical interface review; no compiled proof witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/open-logic-first-order-2026"
    ],
    "sourceLocator": "§3.4, Definition 3.11",
    "sourceNote": "Verified against the cited definitions. Existing stable ID and classical semantics retained; derived results follow from the explicitly linked premises.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/PredicateLogic-atomic-satisfaction",
    "type": "Axiom",
    "name": "atomic-satisfaction",
    "statement": "Assignments evaluate terms and atomic formulas; updating changes one variable only.",
    "formalStatement": "value(M,ρ,x)=ρ(x); value(M,ρ,f(ts))=f^M(value(M,ρ,ts)); ρ[x↦a](y)=a if y=x else ρ(y); M,ρ⊨R(ts) iff value(M,ρ,ts)∈R^M; M,ρ⊨t=u iff value(M,ρ,t)=value(M,ρ,u); M,ρ⊭⊥.",
    "assumptions": [
      "Classical single-sorted first-order semantics with domain D≠∅, total function symbols, arbitrary relations and equality as actual domain identity. Formula syntax may use the named-variable profile in FirstOrderFormula; ∃, ∨, ⇒, ↔ and ⊤ may be expanded as classical macros. Semantic queries are predicates, not general decision procedures. Sentence metatheorems below use the countable signature profile explicitly."
    ],
    "appliesTo": [
      "urn:csabs:concept/PredicateLogic"
    ],
    "reviewStatus": "Editorial source and mathematical interface review; no compiled proof witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "defining-rule",
    "source": [
      "urn:csabs:source/open-logic-first-order-2026"
    ],
    "sourceLocator": "§3.4 Definitions 3.7–3.11",
    "sourceNote": "Selected presentation in catalog notation; finite raw syntax and the stated primitive basis are explicit choices. No executable proof is implied.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/PredicateLogic-semantic-queries",
    "type": "Axiom",
    "name": "semantic-queries",
    "statement": "Sentence consequence and satisfiability range over all structures of the fixed signature.",
    "formalStatement": "For sentences φ, M⊨φ ⇔ ∀ρ,M,ρ⊨φ; M⊨Γ ⇔ ∀ψ∈Γ,M⊨ψ; Γ⊨φ ⇔ ∀M,(M⊨Γ⇒M⊨φ); sat(Γ) ⇔ ∃M,M⊨Γ; valid(φ) ⇔ ∅⊨φ; equivalent(φ,ψ) ⇔ ∀M ρ,(M,ρ⊨φ ⇔ M,ρ⊨ψ).",
    "assumptions": [
      "Γ and φ in sat, valid and entails are sentences of one fixed signature; equivalent also admits open formulas.",
      "All structures have nonempty domains; ρ is total."
    ],
    "appliesTo": [
      "urn:csabs:concept/PredicateLogic"
    ],
    "reviewStatus": "Editorial source and mathematical interface review; no compiled proof witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "defining-rule",
    "source": [
      "urn:csabs:source/open-logic-first-order-2026"
    ],
    "sourceLocator": "§3.5 Definitions 3.16–3.17; §3.7 Definitions 3.24–3.26",
    "sourceNote": "Selected presentation in catalog notation; finite raw syntax and the stated primitive basis are explicit choices. No executable proof is implied.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/PredicateLogic-core",
    "type": "Law",
    "statement": "Universal instantiation is sound for substitution free of variable capture.",
    "formalStatement": "∀x φ ⇒ φ[t/x], when t is free for x in φ",
    "appliesTo": [
      "urn:csabs:concept/PredicateLogic"
    ],
    "reviewStatus": "Editorial source and mathematical interface review; no compiled proof witness asserted.",
    "assumptions": [
      "Use the carrier and semantic convention in the linked concept definition."
    ],
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/PredicateLogic-structure",
      "urn:csabs:axiom/PredicateLogic-quantifiers",
      "urn:csabs:axiom/PredicateLogic-connectives",
      "urn:csabs:theorem/PredicateLogic-substitution-semantics"
    ],
    "source": [
      "urn:csabs:source/open-logic-first-order-2026"
    ],
    "sourceLocator": "§2.9, Definitions 2.38 and 2.40; §3.6, Proposition 3.23; §7.3 universal elimination",
    "sourceNote": "Verified against the cited definitions. Existing stable ID and classical semantics retained; derived results follow from the explicitly linked premises.",
    "provenanceKind": "derived",
    "proofSketch": "Evaluate t in M under ρ; apply universal satisfaction at this element and the capture-free substitution lemma."
  },
  {
    "id": "urn:csabs:law/PredicateLogic-sentence-assignment-independent",
    "type": "Law",
    "name": "sentence-assignment-independent",
    "statement": "A sentence has the same truth value under every assignment.",
    "formalStatement": "FV(φ)=∅ ⇒ (M,ρ⊨φ ⇔ M,ρ′⊨φ)",
    "assumptions": [
      "Classical single-sorted first-order semantics with domain D≠∅, total function symbols, arbitrary relations and equality as actual domain identity. Formula syntax may use the named-variable profile in FirstOrderFormula; ∃, ∨, ⇒, ↔ and ⊤ may be expanded as classical macros. Semantic queries are predicates, not general decision procedures. Sentence metatheorems below use the countable signature profile explicitly."
    ],
    "appliesTo": [
      "urn:csabs:concept/PredicateLogic"
    ],
    "reviewStatus": "Editorial source and mathematical interface review; no compiled proof witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:theorem/PredicateLogic-assignment-coincidence",
      "urn:csabs:axiom/FirstOrderFormula-free-variables"
    ],
    "proofSketch": "Apply assignment coincidence: agreement on an empty free-variable set is vacuous.",
    "source": [
      "urn:csabs:source/open-logic-first-order-2026"
    ],
    "sourceLocator": "§3.5 Corollary 3.15",
    "sourceNote": "Selected presentation in catalog notation; finite raw syntax and the stated primitive basis are explicit choices. No executable proof is implied.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/PredicateLogic-quantifier-duality",
    "type": "Theorem",
    "name": "quantifier-duality",
    "statement": "Classical universal quantification is dual to existential quantification.",
    "formalStatement": "∀x φ ↔ ¬∃x ¬φ",
    "proofSketch": "Unfold satisfaction and classical negation of an existential statement.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for PredicateLogic apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/PredicateLogic"
    ],
    "dependsOn": [
      "urn:csabs:axiom/PredicateLogic-structure",
      "urn:csabs:axiom/PredicateLogic-quantifiers",
      "urn:csabs:axiom/PredicateLogic-connectives"
    ],
    "reviewStatus": "Editorial source and mathematical interface review; no compiled proof witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/open-logic-first-order-2026"
    ],
    "sourceLocator": "§3.4, Definition 3.11, universal/existential satisfaction and negation",
    "sourceNote": "Verified against the cited definitions. Existing stable ID and classical semantics retained; derived results follow from the explicitly linked premises.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/PredicateLogic-substitution-semantics",
    "type": "Theorem",
    "name": "substitution-semantics",
    "statement": "Capture-free syntactic substitution agrees with semantic assignment update.",
    "formalStatement": "value(M,ρ,s[t/x])=value(M,ρ[x↦value(M,ρ,t)],s); M,ρ⊨φ[t/x] ⇔ M,ρ[x↦value(M,ρ,t)]⊨φ.",
    "assumptions": [
      "t is free for x in φ.",
      "M, ρ, terms and formulas have the typed carriers of PredicateLogic and FirstOrderFormula."
    ],
    "appliesTo": [
      "urn:csabs:concept/PredicateLogic"
    ],
    "reviewStatus": "Editorial source and mathematical interface review; no compiled proof witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/FirstOrderFormula-substitution",
      "urn:csabs:axiom/FirstOrderFormula-free-syntax",
      "urn:csabs:axiom/PredicateLogic-structure",
      "urn:csabs:axiom/PredicateLogic-atomic-satisfaction",
      "urn:csabs:axiom/PredicateLogic-quantifiers",
      "urn:csabs:axiom/PredicateLogic-connectives",
      "urn:csabs:axiom/TermAlgebra-induction"
    ],
    "proofSketch": "Prove the term equality by term induction. Induct on φ for satisfaction, using the term equality in atomic cases. Under a different quantifier, the free-for condition prevents capture and ensures the relevant updates commute; a binder for x stops substitution.",
    "source": [
      "urn:csabs:source/open-logic-first-order-2026"
    ],
    "sourceLocator": "§3.6 Propositions 3.22–3.23; §2.9 Definition 2.40",
    "sourceNote": "Selected presentation in catalog notation; finite raw syntax and the stated primitive basis are explicit choices. No executable proof is implied.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/PredicateLogic-assignment-coincidence",
    "type": "Theorem",
    "name": "assignment-coincidence",
    "statement": "Truth depends only on the free variables of a formula.",
    "formalStatement": "(∀x∈FV(φ),ρ(x)=ρ′(x)) ⇒ (M,ρ⊨φ ⇔ M,ρ′⊨φ)",
    "assumptions": [
      "Classical single-sorted first-order semantics with domain D≠∅, total function symbols, arbitrary relations and equality as actual domain identity. Formula syntax may use the named-variable profile in FirstOrderFormula; ∃, ∨, ⇒, ↔ and ⊤ may be expanded as classical macros. Semantic queries are predicates, not general decision procedures. Sentence metatheorems below use the countable signature profile explicitly."
    ],
    "appliesTo": [
      "urn:csabs:concept/PredicateLogic"
    ],
    "reviewStatus": "Editorial source and mathematical interface review; no compiled proof witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/FirstOrderFormula-free-syntax",
      "urn:csabs:axiom/FirstOrderFormula-free-variables",
      "urn:csabs:axiom/PredicateLogic-atomic-satisfaction",
      "urn:csabs:axiom/PredicateLogic-quantifiers",
      "urn:csabs:axiom/PredicateLogic-connectives",
      "urn:csabs:axiom/TermAlgebra-induction"
    ],
    "proofSketch": "Prove term evaluation depends on its variables by induction. Induct on the formula. At ∀x update both assignments to the same arbitrary element; they then agree on the free variables of the body.",
    "source": [
      "urn:csabs:source/open-logic-first-order-2026"
    ],
    "sourceLocator": "§3.5 Proposition 3.14",
    "sourceNote": "Selected presentation in catalog notation; finite raw syntax and the stated primitive basis are explicit choices. No executable proof is implied.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
