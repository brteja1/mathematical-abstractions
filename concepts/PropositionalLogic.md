# Propositional Logic

Classical two-valued formulas built from atomic propositions and Boolean connectives, interpreted under valuations.

**Notation:** v:Atoms→{false,true}; v(¬p)=¬v(p)

**Stable ID:** `urn:csabs:concept/PropositionalLogic`

**Categories:** Logic and proof

**Kind:** semantic-model

**Prerequisites:** [Boolean algebra](BooleanAlgebra.md), [Finite propositional formula syntax](PropositionalFormula.md)

**Related concepts:** [Classical propositional modal logic K](ModalLogic.md), [Linear temporal logic on infinite discrete traces](LinearTemporalLogic.md), [Classical propositional natural deduction](PropositionalNaturalDeduction.md)

## Backlinks

- [Finite serial Kripke structure for model checking](KripkeStructure.md) — `requiresConcept`
- [Linear temporal logic on infinite discrete traces](LinearTemporalLogic.md) — `requiresConcept`
- [Classical propositional modal logic K](ModalLogic.md) — `requiresConcept`
- [Predicate Logic](PredicateLogic.md) — `requiresConcept`
- [Finite propositional formula syntax](PropositionalFormula.md) — `relatedConcept`
- [Classical propositional natural deduction](PropositionalNaturalDeduction.md) — `requiresConcept`

## Interface and scope

**axiomBasis:** Selected presentation: Classical two-valued formulas built from atomic propositions and Boolean connectives, interpreted under valuations. Governing rules: Boolean valuations interpret connectives by classical truth functions. Semantic consequence quantifies over all valuations.

**basisKind:** defined-structure

**basisScope:** Classical two-valued semantics of finite formulas. Primitive ⊥, ¬, ∧ use PropositionalFormula; ⊤, ∨, ⇒, ↔ are its macros. Atom set may be empty. Raw syntax equality and all-valuations equivalence are different. Infinite premise sets are permitted; truth-table algorithms below require finite total atom support.

**verificationObligation:** Instantiate carrier, equality, and stated semantic conventions before using this entry.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** Editorial source and mathematical interface review; no compiled proof witness asserted.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-PropositionalLogic-basis-evaluate"></a>

### evaluate

`urn:csabs:operation/PropositionalLogic-basis-evaluate`

**signature:** eval : Formula×Valuation→Bool

**description:** Recursively evaluates a formula under a Boolean assignment.

**precondition:** A finite well-formed formula and a total Boolean valuation on its atoms.

**totality:** Total; recursive evaluation on finite syntax.

**outcome:** A Boolean truth value.

<a id="node-urn-csabs-operation-PropositionalLogic-semantic-queries"></a>

### semantic-queries

`urn:csabs:operation/PropositionalLogic-semantic-queries`

**signature:** valid:Form→Prop; sat:𝒫(Form)→Prop; entails:𝒫(Form)×Form→Prop; equivalent:Form²→Prop

**description:** Defines semantic predicates; these signatures do not assert an algorithm for arbitrary premise sets.

**precondition:** Inputs belong to the indicated carriers.

**totality:** Total on the stated domain.

**outcome:** Defines semantic predicates; these signatures do not assert an algorithm for arbitrary premise sets.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-PropositionalLogic-truth-semantics"></a>

### truth-semantics

`urn:csabs:axiom/PropositionalLogic-truth-semantics`

**statement:** Boolean valuations interpret connectives by classical truth functions.

**formalStatement:** v(⊥)=false; v(⊤)=true; v(¬p)=not(v(p)); v(p∧q)=v(p) and v(q); v(p∨q)=v(p) or v(q); v(p⇒q)=not(v(p)) or v(q)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source and mathematical interface review; no compiled proof witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [Open Logic Text: Propositional Logic (revision 9620cc7, 2026-07-12)](https://builds.openlogicproject.org/content/propositional-logic/propositional-logic.pdf); accessedOn: 2026-11-08; sourceRole: Definitions, inference rules and metatheory; individual records specify exact locators and adaptations.

**sourceLocator:** §1.5, satisfaction under a valuation

**sourceNote:** Verified against the cited definitions. Existing stable ID and classical semantics retained; derived results follow from the explicitly linked premises.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-PropositionalLogic-entailment"></a>

### entailment

`urn:csabs:axiom/PropositionalLogic-entailment`

**statement:** Semantic consequence quantifies over all valuations.

**formalStatement:** Γ⊨φ iff ∀v: (∀ψ∈Γ:v(ψ)=true)⇒v(φ)=true

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source and mathematical interface review; no compiled proof witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [Open Logic Text: Propositional Logic (revision 9620cc7, 2026-07-12)](https://builds.openlogicproject.org/content/propositional-logic/propositional-logic.pdf); accessedOn: 2026-11-08; sourceRole: Definitions, inference rules and metatheory; individual records specify exact locators and adaptations.

**sourceLocator:** §1.6, semantic notions

**sourceNote:** Verified against the cited definitions. Existing stable ID and classical semantics retained; derived results follow from the explicitly linked premises.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-PropositionalLogic-semantic-queries"></a>

### semantic-queries

`urn:csabs:axiom/PropositionalLogic-semantic-queries`

**statement:** Validity, satisfiability and equivalence quantify over Boolean valuations.

**formalStatement:** valid(φ) ⇔ ∀v,eval(φ,v)=true; sat(Γ) ⇔ ∃v,∀ψ∈Γ,eval(ψ,v)=true; equivalent(φ,ψ) ⇔ ∀v,eval(φ,v)=eval(ψ,v); entails(Γ,φ) ⇔ Γ⊨φ.

**assumptions:** Classical two-valued semantics of finite formulas. Primitive ⊥, ¬, ∧ use PropositionalFormula; ⊤, ∨, ⇒, ↔ are its macros. Atom set may be empty. Raw syntax equality and all-valuations equivalence are different. Infinite premise sets are permitted; truth-table algorithms below require finite total atom support.

**reviewStatus:** Editorial source and mathematical interface review; no compiled proof witness asserted.

**notationLanguage:** informal mathematical Unicode

**ruleRole:** defining-rule

**source:** [Open Logic Text: Propositional Logic (revision 9620cc7, 2026-07-12)](https://builds.openlogicproject.org/content/propositional-logic/propositional-logic.pdf); accessedOn: 2026-11-08; sourceRole: Definitions, inference rules and metatheory; individual records specify exact locators and adaptations.

**sourceLocator:** §§1.5–1.6 satisfaction, tautology, entailment and satisfiability

**sourceNote:** Selected presentation in catalog notation; finite raw syntax and the stated primitive basis are explicit choices. No executable proof is implied.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-PropositionalLogic-core"></a>

### law/PropositionalLogic-core

`urn:csabs:law/PropositionalLogic-core`

**statement:** Modus ponens preserves truth.

**formalStatement:** v(p)=true ∧ v(p⇒q)=true ⇒ v(q)=true

**reviewStatus:** Editorial source and mathematical interface review; no compiled proof witness asserted.

**assumptions:** Use the carrier and semantic convention in the linked concept definition.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [truth-semantics](PropositionalLogic.md#node-urn-csabs-axiom-PropositionalLogic-truth-semantics); [entailment](PropositionalLogic.md#node-urn-csabs-axiom-PropositionalLogic-entailment)

**source:** [Open Logic Text: Propositional Logic (revision 9620cc7, 2026-07-12)](https://builds.openlogicproject.org/content/propositional-logic/propositional-logic.pdf); accessedOn: 2026-11-08; sourceRole: Definitions, inference rules and metatheory; individual records specify exact locators and adaptations.

**sourceLocator:** §1.5 truth function of implication; §1.6 entailment

**sourceNote:** Verified against the cited definitions. Existing stable ID and classical semantics retained; derived results follow from the explicitly linked premises.

**provenanceKind:** derived

**proofSketch:** If p is true, the truth condition of p⇒q reduces to the truth of q.

## Theorems

<a id="node-urn-csabs-theorem-PropositionalLogic-double-negation"></a>

### double-negation

`urn:csabs:theorem/PropositionalLogic-double-negation`

**statement:** Classical double negation preserves truth under every valuation.

**formalStatement:** ⊨¬¬p↔p

**proofSketch:** Check the two truth values of p.

**assumptions:** The explicit basis, carriers, and side conditions stated for PropositionalLogic apply.

**dependsOn:** [truth-semantics](PropositionalLogic.md#node-urn-csabs-axiom-PropositionalLogic-truth-semantics); [entailment](PropositionalLogic.md#node-urn-csabs-axiom-PropositionalLogic-entailment)

**reviewStatus:** Editorial source and mathematical interface review; no compiled proof witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [Open Logic Text: Propositional Logic (revision 9620cc7, 2026-07-12)](https://builds.openlogicproject.org/content/propositional-logic/propositional-logic.pdf); accessedOn: 2026-11-08; sourceRole: Definitions, inference rules and metatheory; individual records specify exact locators and adaptations.

**sourceLocator:** §1.5 truth function of negation

**sourceNote:** Verified against the cited definitions. Existing stable ID and classical semantics retained; derived results follow from the explicitly linked premises.

**provenanceKind:** derived

<a id="node-urn-csabs-theorem-PropositionalLogic-substitution-semantics"></a>

### substitution-semantics

`urn:csabs:theorem/PropositionalLogic-substitution-semantics`

**statement:** Evaluating a simultaneous substitution is the same as changing the valuation.

**formalStatement:** eval(subst(σ,φ),v)=eval(φ,(a↦eval(σ(a),v)))

**assumptions:** Classical two-valued semantics of finite formulas. Primitive ⊥, ¬, ∧ use PropositionalFormula; ⊤, ∨, ⇒, ↔ are its macros. Atom set may be empty. Raw syntax equality and all-valuations equivalence are different. Infinite premise sets are permitted; truth-table algorithms below require finite total atom support.

**reviewStatus:** Editorial source and mathematical interface review; no compiled proof witness asserted.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [induction](PropositionalFormula.md#node-urn-csabs-axiom-PropositionalFormula-induction); [substitution](PropositionalFormula.md#node-urn-csabs-axiom-PropositionalFormula-substitution); [truth-semantics](PropositionalLogic.md#node-urn-csabs-axiom-PropositionalLogic-truth-semantics)

**proofSketch:** Induct on φ. Atom and bottom cases compute; the negation and conjunction steps apply the induction hypotheses inside the truth functions.

**source:** [Open Logic Text: Propositional Logic (revision 9620cc7, 2026-07-12)](https://builds.openlogicproject.org/content/propositional-logic/propositional-logic.pdf); accessedOn: 2026-11-08; sourceRole: Definitions, inference rules and metatheory; individual records specify exact locators and adaptations.

**sourceLocator:** §1.3 Definition 1.7; §1.5 satisfaction

**sourceNote:** Selected presentation in catalog notation; finite raw syntax and the stated primitive basis are explicit choices. No executable proof is implied.

**provenanceKind:** derived

<a id="node-urn-csabs-theorem-PropositionalLogic-finite-truth-table"></a>

### finite-truth-table

`urn:csabs:theorem/PropositionalLogic-finite-truth-table`

**statement:** A finite premise set and conclusion have decidable semantic consequence via their finite support.

**formalStatement:** For finite Γ and S=atoms(φ)∪⋃ψ∈Γ atoms(ψ), Γ⊨φ iff every b:S→{false,true} satisfying Γ satisfies φ; there are 2^|S| rows.

**assumptions:** Classical two-valued semantics of finite formulas. Primitive ⊥, ¬, ∧ use PropositionalFormula; ⊤, ∨, ⇒, ↔ are its macros. Atom set may be empty. Raw syntax equality and all-valuations equivalence are different. Infinite premise sets are permitted; truth-table algorithms below require finite total atom support.

**reviewStatus:** Editorial source and mathematical interface review; no compiled proof witness asserted.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [induction](PropositionalFormula.md#node-urn-csabs-axiom-PropositionalFormula-induction); [substitution](PropositionalFormula.md#node-urn-csabs-axiom-PropositionalFormula-substitution); [truth-semantics](PropositionalLogic.md#node-urn-csabs-axiom-PropositionalLogic-truth-semantics); [entailment](PropositionalLogic.md#node-urn-csabs-axiom-PropositionalLogic-entailment)

**proofSketch:** Induct on syntax to show evaluation depends only on occurring atoms. S is finite, so enumerate its Boolean assignments. Every row extends to a valuation by assigning false elsewhere; every valuation restricts to a row.

**source:** [Open Logic Text: Propositional Logic (revision 9620cc7, 2026-07-12)](https://builds.openlogicproject.org/content/propositional-logic/propositional-logic.pdf); accessedOn: 2026-11-08; sourceRole: Definitions, inference rules and metatheory; individual records specify exact locators and adaptations.

**sourceLocator:** §§1.2–1.5 finite syntax and truth valuations

**sourceNote:** Derived finite-support enumeration argument, not a complexity or practical performance guarantee.

**provenanceKind:** derived

<a id="node-urn-csabs-theorem-PropositionalLogic-normal-forms"></a>

### normal-forms

`urn:csabs:theorem/PropositionalLogic-normal-forms`

**statement:** Every finite classical formula admits equivalent CNF and DNF without introducing new atoms.

**formalStatement:** ∃C,D: φ≡sem C≡sem D; C is a finite conjunction of finite disjunctions of literals; D is a finite disjunction of finite conjunctions of literals. Empty conjunction=⊤; empty disjunction=⊥; literals are a or ¬a for a∈atoms(φ).

**assumptions:** Classical two-valued semantics of finite formulas. Primitive ⊥, ¬, ∧ use PropositionalFormula; ⊤, ∨, ⇒, ↔ are its macros. Atom set may be empty. Raw syntax equality and all-valuations equivalence are different. Infinite premise sets are permitted; truth-table algorithms below require finite total atom support.

**reviewStatus:** Editorial source and mathematical interface review; no compiled proof witness asserted.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [induction](PropositionalFormula.md#node-urn-csabs-axiom-PropositionalFormula-induction); [substitution](PropositionalFormula.md#node-urn-csabs-axiom-PropositionalFormula-substitution); [truth-semantics](PropositionalLogic.md#node-urn-csabs-axiom-PropositionalLogic-truth-semantics); [semantic-queries](PropositionalLogic.md#node-urn-csabs-axiom-PropositionalLogic-semantic-queries)

**proofSketch:** Enumerate assignments on atoms(φ). For each true row form the conjunction of literals that fixes that row, then disjoin these minterms for DNF. For each false row form the disjunction false exactly at that row, then conjoin these clauses for CNF. This also handles zero atoms and constant formulas. Expand ∨ and ⊤ using the chosen macros.

**source:** [Open Logic Text: Propositional Logic (revision 9620cc7, 2026-07-12)](https://builds.openlogicproject.org/content/propositional-logic/propositional-logic.pdf); accessedOn: 2026-11-08; sourceRole: Definitions, inference rules and metatheory; individual records specify exact locators and adaptations.

**sourceLocator:** §1.3 induction on formulas; §1.5 Boolean valuations

**sourceNote:** Catalog derivation from consulted syntax and truth semantics, not a normal-form theorem attributed to the source. Output may grow exponentially; equivalence, rather than mere equisatisfiability, is asserted.

**provenanceKind:** derived

## Concept provenance

- [Open Logic Text: Propositional Logic (revision 9620cc7, 2026-07-12)](https://builds.openlogicproject.org/content/propositional-logic/propositional-logic.pdf); accessedOn: 2026-11-08; sourceRole: Definitions, inference rules and metatheory; individual records specify exact locators and adaptations.

**sourceLocator:** §§1.1–1.6: syntax, valuations and semantic notions

**sourceNote:** Verified against the cited definitions. Existing stable ID and classical semantics retained; derived results follow from the explicitly linked premises.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/PropositionalLogic",
    "type": "Concept",
    "shortForm": "PropositionalLogic",
    "fullName": "Propositional Logic",
    "category": [
      "urn:csabs:category/logic"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "definition": "Classical two-valued formulas built from atomic propositions and Boolean connectives, interpreted under valuations.",
    "notation": "v:Atoms→{false,true}; v(¬p)=¬v(p)",
    "hasOperation": [
      "urn:csabs:operation/PropositionalLogic-basis-evaluate",
      "urn:csabs:operation/PropositionalLogic-semantic-queries"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/PropositionalLogic-truth-semantics",
      "urn:csabs:axiom/PropositionalLogic-entailment",
      "urn:csabs:axiom/PropositionalLogic-semantic-queries"
    ],
    "hasLaw": [
      "urn:csabs:law/PropositionalLogic-core"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/PropositionalLogic-double-negation",
      "urn:csabs:theorem/PropositionalLogic-substitution-semantics",
      "urn:csabs:theorem/PropositionalLogic-finite-truth-table",
      "urn:csabs:theorem/PropositionalLogic-normal-forms"
    ],
    "requiresConcept": [
      "urn:csabs:concept/BooleanAlgebra",
      "urn:csabs:concept/PropositionalFormula"
    ],
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Instantiate carrier, equality, and stated semantic conventions before using this entry.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: Classical two-valued formulas built from atomic propositions and Boolean connectives, interpreted under valuations. Governing rules: Boolean valuations interpret connectives by classical truth functions. Semantic consequence quantifies over all valuations.",
    "basisKind": "defined-structure",
    "basisScope": "Classical two-valued semantics of finite formulas. Primitive ⊥, ¬, ∧ use PropositionalFormula; ⊤, ∨, ⇒, ↔ are its macros. Atom set may be empty. Raw syntax equality and all-valuations equivalence are different. Infinite premise sets are permitted; truth-table algorithms below require finite total atom support.",
    "reviewStatus": "Editorial source and mathematical interface review; no compiled proof witness asserted.",
    "relatedConcept": [
      "urn:csabs:concept/ModalLogic",
      "urn:csabs:concept/LinearTemporalLogic",
      "urn:csabs:concept/PropositionalNaturalDeduction"
    ],
    "source": [
      "urn:csabs:source/open-logic-propositional-2026"
    ],
    "sourceLocator": "§§1.1–1.6: syntax, valuations and semantic notions",
    "sourceNote": "Verified against the cited definitions. Existing stable ID and classical semantics retained; derived results follow from the explicitly linked premises.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/PropositionalLogic-basis-evaluate",
    "type": "Operation",
    "name": "evaluate",
    "signature": "eval : Formula×Valuation→Bool",
    "description": "Recursively evaluates a formula under a Boolean assignment.",
    "concept": "urn:csabs:concept/PropositionalLogic",
    "precondition": "A finite well-formed formula and a total Boolean valuation on its atoms.",
    "totality": "Total; recursive evaluation on finite syntax.",
    "outcome": "A Boolean truth value."
  },
  {
    "id": "urn:csabs:operation/PropositionalLogic-semantic-queries",
    "type": "Operation",
    "name": "semantic-queries",
    "signature": "valid:Form→Prop; sat:𝒫(Form)→Prop; entails:𝒫(Form)×Form→Prop; equivalent:Form²→Prop",
    "description": "Defines semantic predicates; these signatures do not assert an algorithm for arbitrary premise sets.",
    "concept": "urn:csabs:concept/PropositionalLogic",
    "precondition": "Inputs belong to the indicated carriers.",
    "totality": "Total on the stated domain.",
    "outcome": "Defines semantic predicates; these signatures do not assert an algorithm for arbitrary premise sets."
  },
  {
    "id": "urn:csabs:axiom/PropositionalLogic-truth-semantics",
    "type": "Axiom",
    "name": "truth-semantics",
    "statement": "Boolean valuations interpret connectives by classical truth functions.",
    "formalStatement": "v(⊥)=false; v(⊤)=true; v(¬p)=not(v(p)); v(p∧q)=v(p) and v(q); v(p∨q)=v(p) or v(q); v(p⇒q)=not(v(p)) or v(q)",
    "appliesTo": [
      "urn:csabs:concept/PropositionalLogic"
    ],
    "assumptions": [
      "All variables range over the carriers and semantic conventions specified in this concept."
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source and mathematical interface review; no compiled proof witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/open-logic-propositional-2026"
    ],
    "sourceLocator": "§1.5, satisfaction under a valuation",
    "sourceNote": "Verified against the cited definitions. Existing stable ID and classical semantics retained; derived results follow from the explicitly linked premises.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/PropositionalLogic-entailment",
    "type": "Axiom",
    "name": "entailment",
    "statement": "Semantic consequence quantifies over all valuations.",
    "formalStatement": "Γ⊨φ iff ∀v: (∀ψ∈Γ:v(ψ)=true)⇒v(φ)=true",
    "appliesTo": [
      "urn:csabs:concept/PropositionalLogic"
    ],
    "assumptions": [
      "All variables range over the carriers and semantic conventions specified in this concept."
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source and mathematical interface review; no compiled proof witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/open-logic-propositional-2026"
    ],
    "sourceLocator": "§1.6, semantic notions",
    "sourceNote": "Verified against the cited definitions. Existing stable ID and classical semantics retained; derived results follow from the explicitly linked premises.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/PropositionalLogic-semantic-queries",
    "type": "Axiom",
    "name": "semantic-queries",
    "statement": "Validity, satisfiability and equivalence quantify over Boolean valuations.",
    "formalStatement": "valid(φ) ⇔ ∀v,eval(φ,v)=true; sat(Γ) ⇔ ∃v,∀ψ∈Γ,eval(ψ,v)=true; equivalent(φ,ψ) ⇔ ∀v,eval(φ,v)=eval(ψ,v); entails(Γ,φ) ⇔ Γ⊨φ.",
    "assumptions": [
      "Classical two-valued semantics of finite formulas. Primitive ⊥, ¬, ∧ use PropositionalFormula; ⊤, ∨, ⇒, ↔ are its macros. Atom set may be empty. Raw syntax equality and all-valuations equivalence are different. Infinite premise sets are permitted; truth-table algorithms below require finite total atom support."
    ],
    "appliesTo": [
      "urn:csabs:concept/PropositionalLogic"
    ],
    "reviewStatus": "Editorial source and mathematical interface review; no compiled proof witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "defining-rule",
    "source": [
      "urn:csabs:source/open-logic-propositional-2026"
    ],
    "sourceLocator": "§§1.5–1.6 satisfaction, tautology, entailment and satisfiability",
    "sourceNote": "Selected presentation in catalog notation; finite raw syntax and the stated primitive basis are explicit choices. No executable proof is implied.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/PropositionalLogic-core",
    "type": "Law",
    "statement": "Modus ponens preserves truth.",
    "formalStatement": "v(p)=true ∧ v(p⇒q)=true ⇒ v(q)=true",
    "appliesTo": [
      "urn:csabs:concept/PropositionalLogic"
    ],
    "reviewStatus": "Editorial source and mathematical interface review; no compiled proof witness asserted.",
    "assumptions": [
      "Use the carrier and semantic convention in the linked concept definition."
    ],
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/PropositionalLogic-truth-semantics",
      "urn:csabs:axiom/PropositionalLogic-entailment"
    ],
    "source": [
      "urn:csabs:source/open-logic-propositional-2026"
    ],
    "sourceLocator": "§1.5 truth function of implication; §1.6 entailment",
    "sourceNote": "Verified against the cited definitions. Existing stable ID and classical semantics retained; derived results follow from the explicitly linked premises.",
    "provenanceKind": "derived",
    "proofSketch": "If p is true, the truth condition of p⇒q reduces to the truth of q."
  },
  {
    "id": "urn:csabs:theorem/PropositionalLogic-double-negation",
    "type": "Theorem",
    "name": "double-negation",
    "statement": "Classical double negation preserves truth under every valuation.",
    "formalStatement": "⊨¬¬p↔p",
    "proofSketch": "Check the two truth values of p.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for PropositionalLogic apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/PropositionalLogic"
    ],
    "dependsOn": [
      "urn:csabs:axiom/PropositionalLogic-truth-semantics",
      "urn:csabs:axiom/PropositionalLogic-entailment"
    ],
    "reviewStatus": "Editorial source and mathematical interface review; no compiled proof witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/open-logic-propositional-2026"
    ],
    "sourceLocator": "§1.5 truth function of negation",
    "sourceNote": "Verified against the cited definitions. Existing stable ID and classical semantics retained; derived results follow from the explicitly linked premises.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/PropositionalLogic-substitution-semantics",
    "type": "Theorem",
    "name": "substitution-semantics",
    "statement": "Evaluating a simultaneous substitution is the same as changing the valuation.",
    "formalStatement": "eval(subst(σ,φ),v)=eval(φ,(a↦eval(σ(a),v)))",
    "assumptions": [
      "Classical two-valued semantics of finite formulas. Primitive ⊥, ¬, ∧ use PropositionalFormula; ⊤, ∨, ⇒, ↔ are its macros. Atom set may be empty. Raw syntax equality and all-valuations equivalence are different. Infinite premise sets are permitted; truth-table algorithms below require finite total atom support."
    ],
    "appliesTo": [
      "urn:csabs:concept/PropositionalLogic"
    ],
    "reviewStatus": "Editorial source and mathematical interface review; no compiled proof witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/PropositionalFormula-induction",
      "urn:csabs:axiom/PropositionalFormula-substitution",
      "urn:csabs:axiom/PropositionalLogic-truth-semantics"
    ],
    "proofSketch": "Induct on φ. Atom and bottom cases compute; the negation and conjunction steps apply the induction hypotheses inside the truth functions.",
    "source": [
      "urn:csabs:source/open-logic-propositional-2026"
    ],
    "sourceLocator": "§1.3 Definition 1.7; §1.5 satisfaction",
    "sourceNote": "Selected presentation in catalog notation; finite raw syntax and the stated primitive basis are explicit choices. No executable proof is implied.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/PropositionalLogic-finite-truth-table",
    "type": "Theorem",
    "name": "finite-truth-table",
    "statement": "A finite premise set and conclusion have decidable semantic consequence via their finite support.",
    "formalStatement": "For finite Γ and S=atoms(φ)∪⋃ψ∈Γ atoms(ψ), Γ⊨φ iff every b:S→{false,true} satisfying Γ satisfies φ; there are 2^|S| rows.",
    "assumptions": [
      "Classical two-valued semantics of finite formulas. Primitive ⊥, ¬, ∧ use PropositionalFormula; ⊤, ∨, ⇒, ↔ are its macros. Atom set may be empty. Raw syntax equality and all-valuations equivalence are different. Infinite premise sets are permitted; truth-table algorithms below require finite total atom support."
    ],
    "appliesTo": [
      "urn:csabs:concept/PropositionalLogic"
    ],
    "reviewStatus": "Editorial source and mathematical interface review; no compiled proof witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/PropositionalFormula-induction",
      "urn:csabs:axiom/PropositionalFormula-substitution",
      "urn:csabs:axiom/PropositionalLogic-truth-semantics",
      "urn:csabs:axiom/PropositionalLogic-entailment"
    ],
    "proofSketch": "Induct on syntax to show evaluation depends only on occurring atoms. S is finite, so enumerate its Boolean assignments. Every row extends to a valuation by assigning false elsewhere; every valuation restricts to a row.",
    "source": [
      "urn:csabs:source/open-logic-propositional-2026"
    ],
    "sourceLocator": "§§1.2–1.5 finite syntax and truth valuations",
    "sourceNote": "Derived finite-support enumeration argument, not a complexity or practical performance guarantee.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/PropositionalLogic-normal-forms",
    "type": "Theorem",
    "name": "normal-forms",
    "statement": "Every finite classical formula admits equivalent CNF and DNF without introducing new atoms.",
    "formalStatement": "∃C,D: φ≡sem C≡sem D; C is a finite conjunction of finite disjunctions of literals; D is a finite disjunction of finite conjunctions of literals. Empty conjunction=⊤; empty disjunction=⊥; literals are a or ¬a for a∈atoms(φ).",
    "assumptions": [
      "Classical two-valued semantics of finite formulas. Primitive ⊥, ¬, ∧ use PropositionalFormula; ⊤, ∨, ⇒, ↔ are its macros. Atom set may be empty. Raw syntax equality and all-valuations equivalence are different. Infinite premise sets are permitted; truth-table algorithms below require finite total atom support."
    ],
    "appliesTo": [
      "urn:csabs:concept/PropositionalLogic"
    ],
    "reviewStatus": "Editorial source and mathematical interface review; no compiled proof witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/PropositionalFormula-induction",
      "urn:csabs:axiom/PropositionalFormula-substitution",
      "urn:csabs:axiom/PropositionalLogic-truth-semantics",
      "urn:csabs:axiom/PropositionalLogic-semantic-queries"
    ],
    "proofSketch": "Enumerate assignments on atoms(φ). For each true row form the conjunction of literals that fixes that row, then disjoin these minterms for DNF. For each false row form the disjunction false exactly at that row, then conjoin these clauses for CNF. This also handles zero atoms and constant formulas. Expand ∨ and ⊤ using the chosen macros.",
    "source": [
      "urn:csabs:source/open-logic-propositional-2026"
    ],
    "sourceLocator": "§1.3 induction on formulas; §1.5 Boolean valuations",
    "sourceNote": "Catalog derivation from consulted syntax and truth semantics, not a normal-form theorem attributed to the source. Output may grow exponentially; equivalence, rather than mere equisatisfiability, is asserted.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
