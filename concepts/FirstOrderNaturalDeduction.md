# Classical first-order natural deduction with equality

Classical natural deduction on first-order formulas with equality, adding quantifier inference and equality substitution to the explicitly instantiated propositional rules.

**Notation:** Γ⊢_Σ φ; quantifier rules use φ[t/x] only when defined

**Stable ID:** `urn:csabs:concept/FirstOrderNaturalDeduction`

**Categories:** Logic and proof

**Kind:** Mathematical structure

**Prerequisites:** [First-order formula syntax with named variables](FirstOrderFormula.md), [Predicate Logic](PredicateLogic.md), [Classical propositional natural deduction](PropositionalNaturalDeduction.md)

## Backlinks

- [Predicate Logic](PredicateLogic.md) — `relatedConcept`

## Interface and scope

**axiomBasis:** Least finitary relation explicitly instantiating the classical propositional rules and adding ∀ introduction/elimination with freshness/free-for guards and equality reflexivity/substitution; ∃ is a macro with derived rules.

**basisKind:** inductive-definition

**basisScope:** Countable single-sorted signature, infinitely many variable names, finite proof trees, set contexts. Open formulas are allowed in intermediate derivations; soundness uses a common structure and assignment. Completeness and compactness are stated for sentence premises/conclusions and arbitrary nonempty models, not just finite models. Primitive basis is ⊥, ¬, ∧, ∀, equality; ∃ is a macro.

**verificationObligation:** Distinguish raw syntactic equality, alpha equivalence, semantic equivalence and derivability. Retrieve explicitly linked premises; prerequisite links do not inherit axioms.; Lean model bindings may expose only a partial interface; consult their limitations.

**reviewStatus:** Editorial source and mathematical interface review; no compiled proof witness asserted.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-FirstOrderNaturalDeduction-derivable"></a>

### derivable

`urn:csabs:operation/FirstOrderNaturalDeduction-derivable`

**signature:** derivable:𝒫(Form_Σ)×Form_Σ→Prop

**description:** Asserts a finite derivation with all substitution and eigenvariable conditions satisfied; no general decision procedure is asserted.

**precondition:** Inputs belong to the indicated carriers.

**totality:** Total on the stated domain.

**outcome:** Asserts a finite derivation with all substitution and eigenvariable conditions satisfied; no general decision procedure is asserted.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-FirstOrderNaturalDeduction-propositional-rules"></a>

### propositional-rules

`urn:csabs:axiom/FirstOrderNaturalDeduction-propositional-rules`

**statement:** Instantiate all the propositional proof rules on first-order formulas, with explicit closure and classical reductio.

**formalStatement:** φ∈Γ⇒Γ⊢φ; Γ⊢φ and Γ⊆Δ⇒Δ⊢φ; Γ⊢φ,Γ⊢ψ / Γ⊢φ∧ψ; Γ⊢φ∧ψ / Γ⊢φ and Γ⊢ψ; Γ∪{φ}⊢⊥ / Γ⊢¬φ; Γ⊢φ,Γ⊢¬φ / Γ⊢⊥; Γ⊢⊥ / Γ⊢φ; Γ∪{¬φ}⊢⊥ / Γ⊢φ. Derivability is the least closure under these, quantifier rules and equality rules.

**assumptions:** Countable single-sorted signature, infinitely many variable names, finite proof trees, set contexts. Open formulas are allowed in intermediate derivations; soundness uses a common structure and assignment. Completeness and compactness are stated for sentence premises/conclusions and arbitrary nonempty models, not just finite models. Primitive basis is ⊥, ¬, ∧, ∀, equality; ∃ is a macro.

**reviewStatus:** Editorial source and mathematical interface review; no compiled proof witness asserted.

**notationLanguage:** informal mathematical Unicode

**ruleRole:** defining-rule

**source:** [Open Logic Text: First-order Logic (revision 9620cc7, 2026-07-12)](https://builds.openlogicproject.org/content/first-order-logic/first-order-logic.pdf); accessedOn: 2026-11-08; sourceRole: Definitions, inference rules and metatheory; individual records specify exact locators and adaptations.

**sourceLocator:** §§7.1–7.4

**sourceNote:** Explicitly instantiates the rules rather than inferring inheritance from requiresConcept. Finite named-variable proofs use the minimal connective basis.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-FirstOrderNaturalDeduction-quantifier-rules"></a>

### quantifier-rules

`urn:csabs:axiom/FirstOrderNaturalDeduction-quantifier-rules`

**statement:** Quantifier inference respects free-for substitution and eigenvariable restrictions.

**formalStatement:** ∀E: Γ⊢∀x φ / Γ⊢φ[t/x], t free for x in φ. ∀I: Γ⊢φ / Γ⊢∀x φ, x∉FV(Γ). Derived ∃I: Γ⊢φ[t/x] / Γ⊢∃x φ, t free for x in φ. Derived ∃E: Γ⊢∃x φ and Γ∪{φ[y/x]}⊢ψ / Γ⊢ψ, y≠x, y∉FV(Γ)∪FV(ψ)∪FV(φ), y free for x in φ; discharge φ[y/x]. FV(Γ)=⋃γ∈Γ FV(γ).

**assumptions:** Countable single-sorted signature, infinitely many variable names, finite proof trees, set contexts. Open formulas are allowed in intermediate derivations; soundness uses a common structure and assignment. Completeness and compactness are stated for sentence premises/conclusions and arbitrary nonempty models, not just finite models. Primitive basis is ⊥, ¬, ∧, ∀, equality; ∃ is a macro.

**reviewStatus:** Editorial source and mathematical interface review; no compiled proof witness asserted.

**notationLanguage:** informal mathematical Unicode

**ruleRole:** defining-rule

**source:** [Open Logic Text: First-order Logic (revision 9620cc7, 2026-07-12)](https://builds.openlogicproject.org/content/first-order-logic/first-order-logic.pdf); accessedOn: 2026-11-08; sourceRole: Definitions, inference rules and metatheory; individual records specify exact locators and adaptations.; [Logic and Proof, Chapter 8: Natural Deduction for First Order Logic](https://leanprover-community.github.io/logic_and_proof/natural_deduction_for_first_order_logic.html); accessedOn: 2026-11-08; sourceRole: Definitions, inference rules and metatheory; individual records specify exact locators and adaptations.

**sourceLocator:** §7.3 eigenvariable conditions; Logic and Proof §8.1 rules of inference

**sourceNote:** Named-variable open-formula variant of the source sentence/eigenconstant presentation. Universal rules are primitive; existential rules follow by classical expansion ∃xφ=¬∀x¬φ. Freshness uses free variables and capture-free substitution. Supplementary consulted source records the variable-based presentation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-FirstOrderNaturalDeduction-equality-rules"></a>

### equality-rules

`urn:csabs:axiom/FirstOrderNaturalDeduction-equality-rules`

**statement:** Logical equality admits reflexivity and substitution in arbitrary formulas.

**formalStatement:** Γ⊢t=t; Γ⊢s=t and Γ⊢φ[s/x] / Γ⊢φ[t/x], provided s and t are free for x in φ.

**assumptions:** Countable single-sorted signature, infinitely many variable names, finite proof trees, set contexts. Open formulas are allowed in intermediate derivations; soundness uses a common structure and assignment. Completeness and compactness are stated for sentence premises/conclusions and arbitrary nonempty models, not just finite models. Primitive basis is ⊥, ¬, ∧, ∀, equality; ∃ is a macro.

**reviewStatus:** Editorial source and mathematical interface review; no compiled proof witness asserted.

**notationLanguage:** informal mathematical Unicode

**ruleRole:** defining-rule

**source:** [Open Logic Text: First-order Logic (revision 9620cc7, 2026-07-12)](https://builds.openlogicproject.org/content/first-order-logic/first-order-logic.pdf); accessedOn: 2026-11-08; sourceRole: Definitions, inference rules and metatheory; individual records specify exact locators and adaptations.; [Logic and Proof, Chapter 8: Natural Deduction for First Order Logic](https://leanprover-community.github.io/logic_and_proof/natural_deduction_for_first_order_logic.html); accessedOn: 2026-11-08; sourceRole: Definitions, inference rules and metatheory; individual records specify exact locators and adaptations.

**sourceLocator:** §7.12 identity introduction/elimination; §7.13 Proposition 7.32; Logic and Proof §§8.1, 8.4

**sourceNote:** Open-term variant of the closed-term rules; the substitution lemma validates it for each structure and assignment. Equality is interpreted as domain identity, not an arbitrary relation.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-FirstOrderNaturalDeduction-finite-support"></a>

### finite-support

`urn:csabs:law/FirstOrderNaturalDeduction-finite-support`

**statement:** Each proof has a finite set of undischarged premises.

**formalStatement:** Γ⊢φ ⇒ ∃finite Γ₀⊆Γ,Γ₀⊢φ

**assumptions:** Countable single-sorted signature, infinitely many variable names, finite proof trees, set contexts. Open formulas are allowed in intermediate derivations; soundness uses a common structure and assignment. Completeness and compactness are stated for sentence premises/conclusions and arbitrary nonempty models, not just finite models. Primitive basis is ⊥, ¬, ∧, ∀, equality; ∃ is a macro.

**reviewStatus:** Editorial source and mathematical interface review; no compiled proof witness asserted.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [propositional-rules](FirstOrderNaturalDeduction.md#node-urn-csabs-axiom-FirstOrderNaturalDeduction-propositional-rules); [quantifier-rules](FirstOrderNaturalDeduction.md#node-urn-csabs-axiom-FirstOrderNaturalDeduction-quantifier-rules); [equality-rules](FirstOrderNaturalDeduction.md#node-urn-csabs-axiom-FirstOrderNaturalDeduction-equality-rules)

**proofSketch:** Collect finitely many undischarged assumption leaves. Restricting contexts preserves eigenvariable side conditions; discharge removes the temporary formula.

**source:** [Open Logic Text: First-order Logic (revision 9620cc7, 2026-07-12)](https://builds.openlogicproject.org/content/first-order-logic/first-order-logic.pdf); accessedOn: 2026-11-08; sourceRole: Definitions, inference rules and metatheory; individual records specify exact locators and adaptations.

**sourceLocator:** §7.7 Proposition 7.17

**sourceNote:** Selected presentation in catalog notation; finite raw syntax and the stated primitive basis are explicit choices. No executable proof is implied.

**provenanceKind:** derived

## Theorems

<a id="node-urn-csabs-theorem-FirstOrderNaturalDeduction-soundness"></a>

### soundness

`urn:csabs:theorem/FirstOrderNaturalDeduction-soundness`

**statement:** First-order derivations preserve satisfaction under a common structure and assignment.

**formalStatement:** Γ⊢φ ⇒ ∀M ρ,((∀γ∈Γ,M,ρ⊨γ)⇒M,ρ⊨φ)

**assumptions:** Countable single-sorted signature, infinitely many variable names, finite proof trees, set contexts. Open formulas are allowed in intermediate derivations; soundness uses a common structure and assignment. Completeness and compactness are stated for sentence premises/conclusions and arbitrary nonempty models, not just finite models. Primitive basis is ⊥, ¬, ∧, ∀, equality; ∃ is a macro.

**reviewStatus:** Editorial source and mathematical interface review; no compiled proof witness asserted.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [propositional-rules](FirstOrderNaturalDeduction.md#node-urn-csabs-axiom-FirstOrderNaturalDeduction-propositional-rules); [quantifier-rules](FirstOrderNaturalDeduction.md#node-urn-csabs-axiom-FirstOrderNaturalDeduction-quantifier-rules); [equality-rules](FirstOrderNaturalDeduction.md#node-urn-csabs-axiom-FirstOrderNaturalDeduction-equality-rules); [structure](PredicateLogic.md#node-urn-csabs-axiom-PredicateLogic-structure); [atomic-satisfaction](PredicateLogic.md#node-urn-csabs-axiom-PredicateLogic-atomic-satisfaction); [quantifiers](PredicateLogic.md#node-urn-csabs-axiom-PredicateLogic-quantifiers); [connectives](PredicateLogic.md#node-urn-csabs-axiom-PredicateLogic-connectives); [substitution-semantics](PredicateLogic.md#node-urn-csabs-theorem-PredicateLogic-substitution-semantics); [assignment-coincidence](PredicateLogic.md#node-urn-csabs-theorem-PredicateLogic-assignment-coincidence)

**proofSketch:** Induct on the proof. In ∀I, vary x while preserving the assumptions by assignment coincidence. In ∀E and equality elimination use substitution semantics. Existential rules are derived through classical macros; other cases are truth-functional.

**source:** [Open Logic Text: First-order Logic (revision 9620cc7, 2026-07-12)](https://builds.openlogicproject.org/content/first-order-logic/first-order-logic.pdf); accessedOn: 2026-11-08; sourceRole: Definitions, inference rules and metatheory; individual records specify exact locators and adaptations.

**sourceLocator:** §7.11 Theorem 7.27; §7.13 Proposition 7.32

**sourceNote:** Selected presentation in catalog notation; finite raw syntax and the stated primitive basis are explicit choices. No executable proof is implied.

**provenanceKind:** derived

<a id="node-urn-csabs-theorem-FirstOrderNaturalDeduction-completeness"></a>

### completeness

`urn:csabs:theorem/FirstOrderNaturalDeduction-completeness`

**statement:** Semantic consequence between sentences has a classical first-order derivation.

**formalStatement:** Γ⊨φ ⇒ Γ⊢φ

**assumptions:** Γ and φ are sentences over the countable signature of FirstOrderSignature.; Classical metatheory and arbitrary nonempty models, including infinite ones.; Use the recorded finitary rules with equality; no second-order or finite-model completeness claim.

**reviewStatus:** Editorial source and mathematical interface review; no compiled proof witness asserted.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [propositional-rules](FirstOrderNaturalDeduction.md#node-urn-csabs-axiom-FirstOrderNaturalDeduction-propositional-rules); [quantifier-rules](FirstOrderNaturalDeduction.md#node-urn-csabs-axiom-FirstOrderNaturalDeduction-quantifier-rules); [equality-rules](FirstOrderNaturalDeduction.md#node-urn-csabs-axiom-FirstOrderNaturalDeduction-equality-rules); [semantic-queries](PredicateLogic.md#node-urn-csabs-axiom-PredicateLogic-semantic-queries); [structure](PredicateLogic.md#node-urn-csabs-axiom-PredicateLogic-structure); [atomic-satisfaction](PredicateLogic.md#node-urn-csabs-axiom-PredicateLogic-atomic-satisfaction); [quantifiers](PredicateLogic.md#node-urn-csabs-axiom-PredicateLogic-quantifiers); [connectives](PredicateLogic.md#node-urn-csabs-axiom-PredicateLogic-connectives); [substitution](FirstOrderFormula.md#node-urn-csabs-axiom-FirstOrderFormula-substitution); [free-syntax](FirstOrderFormula.md#node-urn-csabs-axiom-FirstOrderFormula-free-syntax)

**proofSketch:** Contrapositively extend the consistent set Γ∪{¬φ} with fresh Henkin constants and witnesses, then to a complete consistent set. Build the term model, quotienting terms by provable equality. The truth lemma yields a nonempty countermodel. Closed-term/eigenconstant derivations in the source translate to fresh named variables; expand the derived connective macros.

**source:** [Open Logic Text: First-order Logic (revision 9620cc7, 2026-07-12)](https://builds.openlogicproject.org/content/first-order-logic/first-order-logic.pdf); accessedOn: 2026-11-08; sourceRole: Definitions, inference rules and metatheory; individual records specify exact locators and adaptations.

**sourceLocator:** §10.8 Theorem 10.20 and Corollary 10.21

**sourceNote:** Selected presentation in catalog notation; finite raw syntax and the stated primitive basis are explicit choices. No executable proof is implied.

**provenanceKind:** derived

<a id="node-urn-csabs-theorem-FirstOrderNaturalDeduction-compactness"></a>

### compactness

`urn:csabs:theorem/FirstOrderNaturalDeduction-compactness`

**statement:** A sentence theory has a nonempty model iff every finite subtheory does.

**formalStatement:** sat(Γ) ⇔ ∀finite Γ₀⊆Γ,sat(Γ₀); Γ⊨φ ⇔ ∃finite Γ₀⊆Γ,Γ₀⊨φ

**assumptions:** Γ and φ are sentences over a countable first-order signature.; All nonempty models are allowed; restricting to finite models invalidates the general claim.

**reviewStatus:** Editorial source and mathematical interface review; no compiled proof witness asserted.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [finite-support](FirstOrderNaturalDeduction.md#node-urn-csabs-law-FirstOrderNaturalDeduction-finite-support); [soundness](FirstOrderNaturalDeduction.md#node-urn-csabs-theorem-FirstOrderNaturalDeduction-soundness); [completeness](FirstOrderNaturalDeduction.md#node-urn-csabs-theorem-FirstOrderNaturalDeduction-completeness); [semantic-queries](PredicateLogic.md#node-urn-csabs-axiom-PredicateLogic-semantic-queries); [connectives](PredicateLogic.md#node-urn-csabs-axiom-PredicateLogic-connectives)

**proofSketch:** Unsatisfiability gives entailment of ⊥; completeness gives a proof, finite support extracts Γ₀, and soundness makes Γ₀ unsatisfiable. For consequence, apply completeness, finite support and soundness directly; the reverse uses monotonicity of semantic consequence.

**source:** [Open Logic Text: First-order Logic (revision 9620cc7, 2026-07-12)](https://builds.openlogicproject.org/content/first-order-logic/first-order-logic.pdf); accessedOn: 2026-11-08; sourceRole: Definitions, inference rules and metatheory; individual records specify exact locators and adaptations.

**sourceLocator:** §10.9 Theorem 10.23

**sourceNote:** Selected presentation in catalog notation; finite raw syntax and the stated primitive basis are explicit choices. No executable proof is implied.

**provenanceKind:** derived

## Concept provenance

- [Open Logic Text: First-order Logic (revision 9620cc7, 2026-07-12)](https://builds.openlogicproject.org/content/first-order-logic/first-order-logic.pdf); accessedOn: 2026-11-08; sourceRole: Definitions, inference rules and metatheory; individual records specify exact locators and adaptations.

**sourceLocator:** §§7.1–7.4, 7.11–7.13; §§10.8–10.9

**sourceNote:** Selected presentation in catalog notation; finite raw syntax and the stated primitive basis are explicit choices. No executable proof is implied.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/FirstOrderNaturalDeduction",
    "type": "Concept",
    "shortForm": "FirstOrderNaturalDeduction",
    "fullName": "Classical first-order natural deduction with equality",
    "category": [
      "urn:csabs:category/logic"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "Classical natural deduction on first-order formulas with equality, adding quantifier inference and equality substitution to the explicitly instantiated propositional rules.",
    "notation": "Γ⊢_Σ φ; quantifier rules use φ[t/x] only when defined",
    "axiomBasis": "Least finitary relation explicitly instantiating the classical propositional rules and adding ∀ introduction/elimination with freshness/free-for guards and equality reflexivity/substitution; ∃ is a macro with derived rules.",
    "basisKind": "inductive-definition",
    "basisScope": "Countable single-sorted signature, infinitely many variable names, finite proof trees, set contexts. Open formulas are allowed in intermediate derivations; soundness uses a common structure and assignment. Completeness and compactness are stated for sentence premises/conclusions and arbitrary nonempty models, not just finite models. Primitive basis is ⊥, ¬, ∧, ∀, equality; ∃ is a macro.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source and mathematical interface review; no compiled proof witness asserted.",
    "verificationObligation": [
      "Distinguish raw syntactic equality, alpha equivalence, semantic equivalence and derivability. Retrieve explicitly linked premises; prerequisite links do not inherit axioms.",
      "Lean model bindings may expose only a partial interface; consult their limitations."
    ],
    "requiresConcept": [
      "urn:csabs:concept/FirstOrderFormula",
      "urn:csabs:concept/PredicateLogic",
      "urn:csabs:concept/PropositionalNaturalDeduction"
    ],
    "relatedConcept": [],
    "hasOperation": [
      "urn:csabs:operation/FirstOrderNaturalDeduction-derivable"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/FirstOrderNaturalDeduction-propositional-rules",
      "urn:csabs:axiom/FirstOrderNaturalDeduction-quantifier-rules",
      "urn:csabs:axiom/FirstOrderNaturalDeduction-equality-rules"
    ],
    "hasLaw": [
      "urn:csabs:law/FirstOrderNaturalDeduction-finite-support"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/FirstOrderNaturalDeduction-soundness",
      "urn:csabs:theorem/FirstOrderNaturalDeduction-completeness",
      "urn:csabs:theorem/FirstOrderNaturalDeduction-compactness"
    ],
    "source": [
      "urn:csabs:source/open-logic-first-order-2026"
    ],
    "sourceLocator": "§§7.1–7.4, 7.11–7.13; §§10.8–10.9",
    "sourceNote": "Selected presentation in catalog notation; finite raw syntax and the stated primitive basis are explicit choices. No executable proof is implied.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/FirstOrderNaturalDeduction-derivable",
    "type": "Operation",
    "name": "derivable",
    "signature": "derivable:𝒫(Form_Σ)×Form_Σ→Prop",
    "description": "Asserts a finite derivation with all substitution and eigenvariable conditions satisfied; no general decision procedure is asserted.",
    "concept": "urn:csabs:concept/FirstOrderNaturalDeduction",
    "precondition": "Inputs belong to the indicated carriers.",
    "totality": "Total on the stated domain.",
    "outcome": "Asserts a finite derivation with all substitution and eigenvariable conditions satisfied; no general decision procedure is asserted."
  },
  {
    "id": "urn:csabs:axiom/FirstOrderNaturalDeduction-propositional-rules",
    "type": "Axiom",
    "name": "propositional-rules",
    "statement": "Instantiate all the propositional proof rules on first-order formulas, with explicit closure and classical reductio.",
    "formalStatement": "φ∈Γ⇒Γ⊢φ; Γ⊢φ and Γ⊆Δ⇒Δ⊢φ; Γ⊢φ,Γ⊢ψ / Γ⊢φ∧ψ; Γ⊢φ∧ψ / Γ⊢φ and Γ⊢ψ; Γ∪{φ}⊢⊥ / Γ⊢¬φ; Γ⊢φ,Γ⊢¬φ / Γ⊢⊥; Γ⊢⊥ / Γ⊢φ; Γ∪{¬φ}⊢⊥ / Γ⊢φ. Derivability is the least closure under these, quantifier rules and equality rules.",
    "assumptions": [
      "Countable single-sorted signature, infinitely many variable names, finite proof trees, set contexts. Open formulas are allowed in intermediate derivations; soundness uses a common structure and assignment. Completeness and compactness are stated for sentence premises/conclusions and arbitrary nonempty models, not just finite models. Primitive basis is ⊥, ¬, ∧, ∀, equality; ∃ is a macro."
    ],
    "appliesTo": [
      "urn:csabs:concept/FirstOrderNaturalDeduction"
    ],
    "reviewStatus": "Editorial source and mathematical interface review; no compiled proof witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "defining-rule",
    "source": [
      "urn:csabs:source/open-logic-first-order-2026"
    ],
    "sourceLocator": "§§7.1–7.4",
    "sourceNote": "Explicitly instantiates the rules rather than inferring inheritance from requiresConcept. Finite named-variable proofs use the minimal connective basis.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/FirstOrderNaturalDeduction-quantifier-rules",
    "type": "Axiom",
    "name": "quantifier-rules",
    "statement": "Quantifier inference respects free-for substitution and eigenvariable restrictions.",
    "formalStatement": "∀E: Γ⊢∀x φ / Γ⊢φ[t/x], t free for x in φ. ∀I: Γ⊢φ / Γ⊢∀x φ, x∉FV(Γ). Derived ∃I: Γ⊢φ[t/x] / Γ⊢∃x φ, t free for x in φ. Derived ∃E: Γ⊢∃x φ and Γ∪{φ[y/x]}⊢ψ / Γ⊢ψ, y≠x, y∉FV(Γ)∪FV(ψ)∪FV(φ), y free for x in φ; discharge φ[y/x]. FV(Γ)=⋃γ∈Γ FV(γ).",
    "assumptions": [
      "Countable single-sorted signature, infinitely many variable names, finite proof trees, set contexts. Open formulas are allowed in intermediate derivations; soundness uses a common structure and assignment. Completeness and compactness are stated for sentence premises/conclusions and arbitrary nonempty models, not just finite models. Primitive basis is ⊥, ¬, ∧, ∀, equality; ∃ is a macro."
    ],
    "appliesTo": [
      "urn:csabs:concept/FirstOrderNaturalDeduction"
    ],
    "reviewStatus": "Editorial source and mathematical interface review; no compiled proof witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "defining-rule",
    "source": [
      "urn:csabs:source/open-logic-first-order-2026",
      "urn:csabs:source/logic-and-proof-first-order-natural-deduction"
    ],
    "sourceLocator": "§7.3 eigenvariable conditions; Logic and Proof §8.1 rules of inference",
    "sourceNote": "Named-variable open-formula variant of the source sentence/eigenconstant presentation. Universal rules are primitive; existential rules follow by classical expansion ∃xφ=¬∀x¬φ. Freshness uses free variables and capture-free substitution. Supplementary consulted source records the variable-based presentation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/FirstOrderNaturalDeduction-equality-rules",
    "type": "Axiom",
    "name": "equality-rules",
    "statement": "Logical equality admits reflexivity and substitution in arbitrary formulas.",
    "formalStatement": "Γ⊢t=t; Γ⊢s=t and Γ⊢φ[s/x] / Γ⊢φ[t/x], provided s and t are free for x in φ.",
    "assumptions": [
      "Countable single-sorted signature, infinitely many variable names, finite proof trees, set contexts. Open formulas are allowed in intermediate derivations; soundness uses a common structure and assignment. Completeness and compactness are stated for sentence premises/conclusions and arbitrary nonempty models, not just finite models. Primitive basis is ⊥, ¬, ∧, ∀, equality; ∃ is a macro."
    ],
    "appliesTo": [
      "urn:csabs:concept/FirstOrderNaturalDeduction"
    ],
    "reviewStatus": "Editorial source and mathematical interface review; no compiled proof witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "defining-rule",
    "source": [
      "urn:csabs:source/open-logic-first-order-2026",
      "urn:csabs:source/logic-and-proof-first-order-natural-deduction"
    ],
    "sourceLocator": "§7.12 identity introduction/elimination; §7.13 Proposition 7.32; Logic and Proof §§8.1, 8.4",
    "sourceNote": "Open-term variant of the closed-term rules; the substitution lemma validates it for each structure and assignment. Equality is interpreted as domain identity, not an arbitrary relation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/FirstOrderNaturalDeduction-finite-support",
    "type": "Law",
    "name": "finite-support",
    "statement": "Each proof has a finite set of undischarged premises.",
    "formalStatement": "Γ⊢φ ⇒ ∃finite Γ₀⊆Γ,Γ₀⊢φ",
    "assumptions": [
      "Countable single-sorted signature, infinitely many variable names, finite proof trees, set contexts. Open formulas are allowed in intermediate derivations; soundness uses a common structure and assignment. Completeness and compactness are stated for sentence premises/conclusions and arbitrary nonempty models, not just finite models. Primitive basis is ⊥, ¬, ∧, ∀, equality; ∃ is a macro."
    ],
    "appliesTo": [
      "urn:csabs:concept/FirstOrderNaturalDeduction"
    ],
    "reviewStatus": "Editorial source and mathematical interface review; no compiled proof witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/FirstOrderNaturalDeduction-propositional-rules",
      "urn:csabs:axiom/FirstOrderNaturalDeduction-quantifier-rules",
      "urn:csabs:axiom/FirstOrderNaturalDeduction-equality-rules"
    ],
    "proofSketch": "Collect finitely many undischarged assumption leaves. Restricting contexts preserves eigenvariable side conditions; discharge removes the temporary formula.",
    "source": [
      "urn:csabs:source/open-logic-first-order-2026"
    ],
    "sourceLocator": "§7.7 Proposition 7.17",
    "sourceNote": "Selected presentation in catalog notation; finite raw syntax and the stated primitive basis are explicit choices. No executable proof is implied.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/FirstOrderNaturalDeduction-soundness",
    "type": "Theorem",
    "name": "soundness",
    "statement": "First-order derivations preserve satisfaction under a common structure and assignment.",
    "formalStatement": "Γ⊢φ ⇒ ∀M ρ,((∀γ∈Γ,M,ρ⊨γ)⇒M,ρ⊨φ)",
    "assumptions": [
      "Countable single-sorted signature, infinitely many variable names, finite proof trees, set contexts. Open formulas are allowed in intermediate derivations; soundness uses a common structure and assignment. Completeness and compactness are stated for sentence premises/conclusions and arbitrary nonempty models, not just finite models. Primitive basis is ⊥, ¬, ∧, ∀, equality; ∃ is a macro."
    ],
    "appliesTo": [
      "urn:csabs:concept/FirstOrderNaturalDeduction"
    ],
    "reviewStatus": "Editorial source and mathematical interface review; no compiled proof witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/FirstOrderNaturalDeduction-propositional-rules",
      "urn:csabs:axiom/FirstOrderNaturalDeduction-quantifier-rules",
      "urn:csabs:axiom/FirstOrderNaturalDeduction-equality-rules",
      "urn:csabs:axiom/PredicateLogic-structure",
      "urn:csabs:axiom/PredicateLogic-atomic-satisfaction",
      "urn:csabs:axiom/PredicateLogic-quantifiers",
      "urn:csabs:axiom/PredicateLogic-connectives",
      "urn:csabs:theorem/PredicateLogic-substitution-semantics",
      "urn:csabs:theorem/PredicateLogic-assignment-coincidence"
    ],
    "proofSketch": "Induct on the proof. In ∀I, vary x while preserving the assumptions by assignment coincidence. In ∀E and equality elimination use substitution semantics. Existential rules are derived through classical macros; other cases are truth-functional.",
    "source": [
      "urn:csabs:source/open-logic-first-order-2026"
    ],
    "sourceLocator": "§7.11 Theorem 7.27; §7.13 Proposition 7.32",
    "sourceNote": "Selected presentation in catalog notation; finite raw syntax and the stated primitive basis are explicit choices. No executable proof is implied.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/FirstOrderNaturalDeduction-completeness",
    "type": "Theorem",
    "name": "completeness",
    "statement": "Semantic consequence between sentences has a classical first-order derivation.",
    "formalStatement": "Γ⊨φ ⇒ Γ⊢φ",
    "assumptions": [
      "Γ and φ are sentences over the countable signature of FirstOrderSignature.",
      "Classical metatheory and arbitrary nonempty models, including infinite ones.",
      "Use the recorded finitary rules with equality; no second-order or finite-model completeness claim."
    ],
    "appliesTo": [
      "urn:csabs:concept/FirstOrderNaturalDeduction"
    ],
    "reviewStatus": "Editorial source and mathematical interface review; no compiled proof witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/FirstOrderNaturalDeduction-propositional-rules",
      "urn:csabs:axiom/FirstOrderNaturalDeduction-quantifier-rules",
      "urn:csabs:axiom/FirstOrderNaturalDeduction-equality-rules",
      "urn:csabs:axiom/PredicateLogic-semantic-queries",
      "urn:csabs:axiom/PredicateLogic-structure",
      "urn:csabs:axiom/PredicateLogic-atomic-satisfaction",
      "urn:csabs:axiom/PredicateLogic-quantifiers",
      "urn:csabs:axiom/PredicateLogic-connectives",
      "urn:csabs:axiom/FirstOrderFormula-substitution",
      "urn:csabs:axiom/FirstOrderFormula-free-syntax"
    ],
    "proofSketch": "Contrapositively extend the consistent set Γ∪{¬φ} with fresh Henkin constants and witnesses, then to a complete consistent set. Build the term model, quotienting terms by provable equality. The truth lemma yields a nonempty countermodel. Closed-term/eigenconstant derivations in the source translate to fresh named variables; expand the derived connective macros.",
    "source": [
      "urn:csabs:source/open-logic-first-order-2026"
    ],
    "sourceLocator": "§10.8 Theorem 10.20 and Corollary 10.21",
    "sourceNote": "Selected presentation in catalog notation; finite raw syntax and the stated primitive basis are explicit choices. No executable proof is implied.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/FirstOrderNaturalDeduction-compactness",
    "type": "Theorem",
    "name": "compactness",
    "statement": "A sentence theory has a nonempty model iff every finite subtheory does.",
    "formalStatement": "sat(Γ) ⇔ ∀finite Γ₀⊆Γ,sat(Γ₀); Γ⊨φ ⇔ ∃finite Γ₀⊆Γ,Γ₀⊨φ",
    "assumptions": [
      "Γ and φ are sentences over a countable first-order signature.",
      "All nonempty models are allowed; restricting to finite models invalidates the general claim."
    ],
    "appliesTo": [
      "urn:csabs:concept/FirstOrderNaturalDeduction"
    ],
    "reviewStatus": "Editorial source and mathematical interface review; no compiled proof witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:law/FirstOrderNaturalDeduction-finite-support",
      "urn:csabs:theorem/FirstOrderNaturalDeduction-soundness",
      "urn:csabs:theorem/FirstOrderNaturalDeduction-completeness",
      "urn:csabs:axiom/PredicateLogic-semantic-queries",
      "urn:csabs:axiom/PredicateLogic-connectives"
    ],
    "proofSketch": "Unsatisfiability gives entailment of ⊥; completeness gives a proof, finite support extracts Γ₀, and soundness makes Γ₀ unsatisfiable. For consequence, apply completeness, finite support and soundness directly; the reverse uses monotonicity of semantic consequence.",
    "source": [
      "urn:csabs:source/open-logic-first-order-2026"
    ],
    "sourceLocator": "§10.9 Theorem 10.23",
    "sourceNote": "Selected presentation in catalog notation; finite raw syntax and the stated primitive basis are explicit choices. No executable proof is implied.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
