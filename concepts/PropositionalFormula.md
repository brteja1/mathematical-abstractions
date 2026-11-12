# Finite propositional formula syntax

The free finite formula syntax over a fixed set A of atoms with primitive falsity, negation and conjunction, before identifying logically equivalent formulas.

**Notation:** F(A)=μX.(A+1+X+X×X); ⊤:=¬⊥; p∨q:=¬(¬p∧¬q); p⇒q:=¬(p∧¬q); p↔q:=(p⇒q)∧(q⇒p)

**Stable ID:** `urn:csabs:concept/PropositionalFormula`

**Categories:** Logic and proof

**Kind:** Abstract data type

**Specializes:** [Free ranked term algebra with variables](TermAlgebra.md)

**Related concepts:** [Free ranked term algebra with variables](TermAlgebra.md), [Propositional Logic](PropositionalLogic.md)

## Backlinks

- [First-order formula syntax with named variables](FirstOrderFormula.md) — `relatedConcept`
- [Propositional Logic](PropositionalLogic.md) — `requiresConcept`
- [Classical propositional natural deduction](PropositionalNaturalDeduction.md) — `requiresConcept`
- [Normalized template constraints with atomic identity](TemplateConstraint.md) — `requiresConcept`

## Mathematical formulation

For atoms AP, formulas are the free inductive syntax φ ::= atom(p) | ⊥ | ¬φ | (φ∧φ). Equality is constructor equality of finite syntax trees, distinct from logical equivalence under all valuations.

**Lean formulation** (in its source module context):

```lean
inductive PropFormula (AP : Type u) where
  | atom : AP → PropFormula AP
  | bottom : PropFormula AP
  | neg : PropFormula AP → PropFormula AP
  | conj : PropFormula AP → PropFormula AP → PropFormula AP
```

**Source:** [`Catalog.PropFormula`](../lean/Catalog/Logic.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Raw finite syntax over arbitrary AP, primitive atom/bottom/neg/conj. Equality is constructor identity. The catalog macro connectives expand into this basis.

**Limits:** Compiled carrier and selected interface only. No new graph law or metatheorem is registered as a proof witness. In particular substitution-support, semantic correspondence, soundness, completeness, compactness and normal-form existence are editorial claims here; grammar/rule declarations do not prove them.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Free finite syntax on atom(a), ⊥, ¬p and p∧q; disjoint/injective constructors, structural induction and unique recursion; recursive atom support and simultaneous substitution.

**basisKind:** inductive-definition

**basisScope:** A is any set, possibly empty. Equality is raw constructor-tree identity. Finite formulas only; no binders or quotient by logical equivalence. All derived connective notation expands into ⊥, ¬, ∧.

**specializationNote:** Instantiate variables X=A and the ranked operation symbols with bottom of arity 0, negation of arity 1, and conjunction of arity 2. The carriers are identified by constructor-preserving tree translation; no semantic equations are imposed.

**verificationObligation:** Distinguish raw syntactic equality, alpha equivalence, semantic equivalence and derivability. Retrieve explicitly linked premises; prerequisite links do not inherit axioms.; Lean model bindings may expose only a partial interface; consult their limitations.

**reviewStatus:** Editorial source and mathematical interface review; no compiled proof witness asserted.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-PropositionalFormula-construct"></a>

### construct

`urn:csabs:operation/PropositionalFormula-construct`

**signature:** atom:A→F; bottom:1→F; neg:F→F; conj:F×F→F

**description:** Constructs a raw formula; different primitive constructors are disjoint and injective.

**precondition:** Inputs belong to the indicated carriers.

**totality:** Total on the stated domain.

**outcome:** Constructs a raw formula; different primitive constructors are disjoint and injective.

<a id="node-urn-csabs-operation-PropositionalFormula-atoms"></a>

### atoms

`urn:csabs:operation/PropositionalFormula-atoms`

**signature:** atoms:F→FiniteSet(A)

**description:** Returns all atoms occurring in the formula, ignoring multiplicity.

**precondition:** Inputs belong to the indicated carriers.

**totality:** Total on the stated domain.

**outcome:** Returns all atoms occurring in the formula, ignoring multiplicity.

<a id="node-urn-csabs-operation-PropositionalFormula-substitute"></a>

### substitute

`urn:csabs:operation/PropositionalFormula-substitute`

**signature:** subst:(A→F)×F→F

**description:** Simultaneously replaces each atom a by σ(a); does not recursively substitute inside inserted formulas.

**precondition:** Inputs belong to the indicated carriers.

**totality:** Total on the stated domain.

**outcome:** Simultaneously replaces each atom a by σ(a); does not recursively substitute inside inserted formulas.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-PropositionalFormula-free-syntax"></a>

### free-syntax

`urn:csabs:axiom/PropositionalFormula-free-syntax`

**statement:** Primitive constructors freely generate all finite formulas.

**formalStatement:** F is the least constructor-closed set; atom(a), ⊥, ¬p, p∧q are disjoint forms; atom, neg and conj are injective.

**assumptions:** A is any set, possibly empty. Equality is raw constructor-tree identity. Finite formulas only; no binders or quotient by logical equivalence. All derived connective notation expands into ⊥, ¬, ∧.

**reviewStatus:** Editorial source and mathematical interface review; no compiled proof witness asserted.

**notationLanguage:** informal mathematical Unicode

**ruleRole:** defining-rule

**source:** [Open Logic Text: Propositional Logic (revision 9620cc7, 2026-07-12)](https://builds.openlogicproject.org/content/propositional-logic/propositional-logic.pdf); accessedOn: 2026-11-08; sourceRole: Definitions, inference rules and metatheory; individual records specify exact locators and adaptations.

**sourceLocator:** §1.2 Definition 1.1; §1.3 Proposition 1.6

**sourceNote:** Selected presentation in catalog notation; finite raw syntax and the stated primitive basis are explicit choices. No executable proof is implied.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-PropositionalFormula-induction"></a>

### induction

`urn:csabs:axiom/PropositionalFormula-induction`

**statement:** Structural induction and recursion use exactly the primitive constructors.

**formalStatement:** P(⊥) ∧ (∀a,P(atom(a))) ∧ (∀p,P(p)⇒P(¬p)) ∧ (∀p q,P(p)∧P(q)⇒P(p∧q)) ⇒ ∀p∈F,P(p); constructor equations determine a unique recursive map.

**assumptions:** A is any set, possibly empty. Equality is raw constructor-tree identity. Finite formulas only; no binders or quotient by logical equivalence. All derived connective notation expands into ⊥, ¬, ∧.

**reviewStatus:** Editorial source and mathematical interface review; no compiled proof witness asserted.

**notationLanguage:** informal mathematical Unicode

**ruleRole:** defining-rule

**source:** [Open Logic Text: Propositional Logic (revision 9620cc7, 2026-07-12)](https://builds.openlogicproject.org/content/propositional-logic/propositional-logic.pdf); accessedOn: 2026-11-08; sourceRole: Definitions, inference rules and metatheory; individual records specify exact locators and adaptations.

**sourceLocator:** §1.3 Theorem 1.3; §1.1 discussion of inductive semantics

**sourceNote:** Selected presentation in catalog notation; finite raw syntax and the stated primitive basis are explicit choices. No executable proof is implied.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-PropositionalFormula-substitution"></a>

### substitution

`urn:csabs:axiom/PropositionalFormula-substitution`

**statement:** Substitution and atom support are defined recursively.

**formalStatement:** subst(σ,atom(a))=σ(a); subst(σ,⊥)=⊥; subst(σ,¬p)=¬subst(σ,p); subst(σ,p∧q)=subst(σ,p)∧subst(σ,q); atoms(atom(a))={a}; atoms(⊥)=∅; atoms(¬p)=atoms(p); atoms(p∧q)=atoms(p)∪atoms(q).

**assumptions:** A is any set, possibly empty. Equality is raw constructor-tree identity. Finite formulas only; no binders or quotient by logical equivalence. All derived connective notation expands into ⊥, ¬, ∧.

**reviewStatus:** Editorial source and mathematical interface review; no compiled proof witness asserted.

**notationLanguage:** informal mathematical Unicode

**ruleRole:** defining-rule

**source:** [Open Logic Text: Propositional Logic (revision 9620cc7, 2026-07-12)](https://builds.openlogicproject.org/content/propositional-logic/propositional-logic.pdf); accessedOn: 2026-11-08; sourceRole: Definitions, inference rules and metatheory; individual records specify exact locators and adaptations.

**sourceLocator:** §1.3 Definition 1.7; §1.2 inductive syntax

**sourceNote:** Uniform substitution is extended to an arbitrary simultaneous atom map; finite support is defined by the same syntax recursion.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-PropositionalFormula-substitution-identity"></a>

### substitution-identity

`urn:csabs:law/PropositionalFormula-substitution-identity`

**statement:** Replacing each atom by itself preserves raw syntax.

**formalStatement:** subst(atom,p)=p

**assumptions:** A is any set, possibly empty. Equality is raw constructor-tree identity. Finite formulas only; no binders or quotient by logical equivalence. All derived connective notation expands into ⊥, ¬, ∧.

**reviewStatus:** Editorial source and mathematical interface review; no compiled proof witness asserted.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [induction](PropositionalFormula.md#node-urn-csabs-axiom-PropositionalFormula-induction); [substitution](PropositionalFormula.md#node-urn-csabs-axiom-PropositionalFormula-substitution)

**proofSketch:** Induct on p. The atom and bottom cases compute; negation and conjunction follow by congruence.

**source:** [Open Logic Text: Propositional Logic (revision 9620cc7, 2026-07-12)](https://builds.openlogicproject.org/content/propositional-logic/propositional-logic.pdf); accessedOn: 2026-11-08; sourceRole: Definitions, inference rules and metatheory; individual records specify exact locators and adaptations.

**sourceLocator:** §1.3 Definition 1.7 and Theorem 1.3

**sourceNote:** Selected presentation in catalog notation; finite raw syntax and the stated primitive basis are explicit choices. No executable proof is implied.

**provenanceKind:** derived

## Theorems

<a id="node-urn-csabs-theorem-PropositionalFormula-substitution-composition"></a>

### substitution-composition

`urn:csabs:theorem/PropositionalFormula-substitution-composition`

**statement:** Successive simultaneous substitutions compose.

**formalStatement:** subst(τ,subst(σ,p))=subst((a↦subst(τ,σ(a))),p)

**assumptions:** A is any set, possibly empty. Equality is raw constructor-tree identity. Finite formulas only; no binders or quotient by logical equivalence. All derived connective notation expands into ⊥, ¬, ∧.

**reviewStatus:** Editorial source and mathematical interface review; no compiled proof witness asserted.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [induction](PropositionalFormula.md#node-urn-csabs-axiom-PropositionalFormula-induction); [substitution](PropositionalFormula.md#node-urn-csabs-axiom-PropositionalFormula-substitution)

**proofSketch:** Induct on p; at an atom both sides are subst(τ,σ(a)); all other constructors commute with substitution.

**source:** [Open Logic Text: Propositional Logic (revision 9620cc7, 2026-07-12)](https://builds.openlogicproject.org/content/propositional-logic/propositional-logic.pdf); accessedOn: 2026-11-08; sourceRole: Definitions, inference rules and metatheory; individual records specify exact locators and adaptations.

**sourceLocator:** §1.3 Definition 1.7 and Theorem 1.3

**sourceNote:** Selected presentation in catalog notation; finite raw syntax and the stated primitive basis are explicit choices. No executable proof is implied.

**provenanceKind:** derived

## Concept provenance

- [Open Logic Text: Propositional Logic (revision 9620cc7, 2026-07-12)](https://builds.openlogicproject.org/content/propositional-logic/propositional-logic.pdf); accessedOn: 2026-11-08; sourceRole: Definitions, inference rules and metatheory; individual records specify exact locators and adaptations.

**sourceLocator:** §1.2 Definition 1.1; §1.3 Theorem 1.3, Proposition 1.6 and Definition 1.7

**sourceNote:** Selected presentation in catalog notation; finite raw syntax and the stated primitive basis are explicit choices. No executable proof is implied.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/PropositionalFormula",
    "type": "Concept",
    "shortForm": "PropositionalFormula",
    "fullName": "Finite propositional formula syntax",
    "category": [
      "urn:csabs:category/logic"
    ],
    "kind": "urn:csabs:kind/abstract-data-type",
    "definition": "The free finite formula syntax over a fixed set A of atoms with primitive falsity, negation and conjunction, before identifying logically equivalent formulas.",
    "notation": "F(A)=μX.(A+1+X+X×X); ⊤:=¬⊥; p∨q:=¬(¬p∧¬q); p⇒q:=¬(p∧¬q); p↔q:=(p⇒q)∧(q⇒p)",
    "axiomBasis": "Free finite syntax on atom(a), ⊥, ¬p and p∧q; disjoint/injective constructors, structural induction and unique recursion; recursive atom support and simultaneous substitution.",
    "basisKind": "inductive-definition",
    "basisScope": "A is any set, possibly empty. Equality is raw constructor-tree identity. Finite formulas only; no binders or quotient by logical equivalence. All derived connective notation expands into ⊥, ¬, ∧.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source and mathematical interface review; no compiled proof witness asserted.",
    "verificationObligation": [
      "Distinguish raw syntactic equality, alpha equivalence, semantic equivalence and derivability. Retrieve explicitly linked premises; prerequisite links do not inherit axioms.",
      "Lean model bindings may expose only a partial interface; consult their limitations."
    ],
    "requiresConcept": [],
    "relatedConcept": [
      "urn:csabs:concept/TermAlgebra",
      "urn:csabs:concept/PropositionalLogic"
    ],
    "hasOperation": [
      "urn:csabs:operation/PropositionalFormula-construct",
      "urn:csabs:operation/PropositionalFormula-atoms",
      "urn:csabs:operation/PropositionalFormula-substitute"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/PropositionalFormula-free-syntax",
      "urn:csabs:axiom/PropositionalFormula-induction",
      "urn:csabs:axiom/PropositionalFormula-substitution"
    ],
    "hasLaw": [
      "urn:csabs:law/PropositionalFormula-substitution-identity"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/PropositionalFormula-substitution-composition"
    ],
    "source": [
      "urn:csabs:source/open-logic-propositional-2026"
    ],
    "sourceLocator": "§1.2 Definition 1.1; §1.3 Theorem 1.3, Proposition 1.6 and Definition 1.7",
    "sourceNote": "Selected presentation in catalog notation; finite raw syntax and the stated primitive basis are explicit choices. No executable proof is implied.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/TermAlgebra"
    ],
    "specializationNote": "Instantiate variables X=A and the ranked operation symbols with bottom of arity 0, negation of arity 1, and conjunction of arity 2. The carriers are identified by constructor-preserving tree translation; no semantic equations are imposed.",
    "leanFormulation": "inductive PropFormula (AP : Type u) where\n  | atom : AP → PropFormula AP\n  | bottom : PropFormula AP\n  | neg : PropFormula AP → PropFormula AP\n  | conj : PropFormula AP → PropFormula AP → PropFormula AP",
    "formulationSource": "urn:csabs:source/local-lean-Logic",
    "formulationLocator": "Catalog.PropFormula",
    "formulationScope": "model",
    "leanModelMapping": "Raw finite syntax over arbitrary AP, primitive atom/bottom/neg/conj. Equality is constructor identity. The catalog macro connectives expand into this basis.",
    "leanModelLimitations": "Compiled carrier and selected interface only. No new graph law or metatheorem is registered as a proof witness. In particular substitution-support, semantic correspondence, soundness, completeness, compactness and normal-form existence are editorial claims here; grammar/rule declarations do not prove them.",
    "mathematicalFormulation": "For atoms AP, formulas are the free inductive syntax φ ::= atom(p) | ⊥ | ¬φ | (φ∧φ). Equality is constructor equality of finite syntax trees, distinct from logical equivalence under all valuations."
  },
  {
    "id": "urn:csabs:operation/PropositionalFormula-construct",
    "type": "Operation",
    "name": "construct",
    "signature": "atom:A→F; bottom:1→F; neg:F→F; conj:F×F→F",
    "description": "Constructs a raw formula; different primitive constructors are disjoint and injective.",
    "concept": "urn:csabs:concept/PropositionalFormula",
    "precondition": "Inputs belong to the indicated carriers.",
    "totality": "Total on the stated domain.",
    "outcome": "Constructs a raw formula; different primitive constructors are disjoint and injective."
  },
  {
    "id": "urn:csabs:operation/PropositionalFormula-atoms",
    "type": "Operation",
    "name": "atoms",
    "signature": "atoms:F→FiniteSet(A)",
    "description": "Returns all atoms occurring in the formula, ignoring multiplicity.",
    "concept": "urn:csabs:concept/PropositionalFormula",
    "precondition": "Inputs belong to the indicated carriers.",
    "totality": "Total on the stated domain.",
    "outcome": "Returns all atoms occurring in the formula, ignoring multiplicity."
  },
  {
    "id": "urn:csabs:operation/PropositionalFormula-substitute",
    "type": "Operation",
    "name": "substitute",
    "signature": "subst:(A→F)×F→F",
    "description": "Simultaneously replaces each atom a by σ(a); does not recursively substitute inside inserted formulas.",
    "concept": "urn:csabs:concept/PropositionalFormula",
    "precondition": "Inputs belong to the indicated carriers.",
    "totality": "Total on the stated domain.",
    "outcome": "Simultaneously replaces each atom a by σ(a); does not recursively substitute inside inserted formulas."
  },
  {
    "id": "urn:csabs:axiom/PropositionalFormula-free-syntax",
    "type": "Axiom",
    "name": "free-syntax",
    "statement": "Primitive constructors freely generate all finite formulas.",
    "formalStatement": "F is the least constructor-closed set; atom(a), ⊥, ¬p, p∧q are disjoint forms; atom, neg and conj are injective.",
    "assumptions": [
      "A is any set, possibly empty. Equality is raw constructor-tree identity. Finite formulas only; no binders or quotient by logical equivalence. All derived connective notation expands into ⊥, ¬, ∧."
    ],
    "appliesTo": [
      "urn:csabs:concept/PropositionalFormula"
    ],
    "reviewStatus": "Editorial source and mathematical interface review; no compiled proof witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "defining-rule",
    "source": [
      "urn:csabs:source/open-logic-propositional-2026"
    ],
    "sourceLocator": "§1.2 Definition 1.1; §1.3 Proposition 1.6",
    "sourceNote": "Selected presentation in catalog notation; finite raw syntax and the stated primitive basis are explicit choices. No executable proof is implied.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/PropositionalFormula-induction",
    "type": "Axiom",
    "name": "induction",
    "statement": "Structural induction and recursion use exactly the primitive constructors.",
    "formalStatement": "P(⊥) ∧ (∀a,P(atom(a))) ∧ (∀p,P(p)⇒P(¬p)) ∧ (∀p q,P(p)∧P(q)⇒P(p∧q)) ⇒ ∀p∈F,P(p); constructor equations determine a unique recursive map.",
    "assumptions": [
      "A is any set, possibly empty. Equality is raw constructor-tree identity. Finite formulas only; no binders or quotient by logical equivalence. All derived connective notation expands into ⊥, ¬, ∧."
    ],
    "appliesTo": [
      "urn:csabs:concept/PropositionalFormula"
    ],
    "reviewStatus": "Editorial source and mathematical interface review; no compiled proof witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "defining-rule",
    "source": [
      "urn:csabs:source/open-logic-propositional-2026"
    ],
    "sourceLocator": "§1.3 Theorem 1.3; §1.1 discussion of inductive semantics",
    "sourceNote": "Selected presentation in catalog notation; finite raw syntax and the stated primitive basis are explicit choices. No executable proof is implied.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/PropositionalFormula-substitution",
    "type": "Axiom",
    "name": "substitution",
    "statement": "Substitution and atom support are defined recursively.",
    "formalStatement": "subst(σ,atom(a))=σ(a); subst(σ,⊥)=⊥; subst(σ,¬p)=¬subst(σ,p); subst(σ,p∧q)=subst(σ,p)∧subst(σ,q); atoms(atom(a))={a}; atoms(⊥)=∅; atoms(¬p)=atoms(p); atoms(p∧q)=atoms(p)∪atoms(q).",
    "assumptions": [
      "A is any set, possibly empty. Equality is raw constructor-tree identity. Finite formulas only; no binders or quotient by logical equivalence. All derived connective notation expands into ⊥, ¬, ∧."
    ],
    "appliesTo": [
      "urn:csabs:concept/PropositionalFormula"
    ],
    "reviewStatus": "Editorial source and mathematical interface review; no compiled proof witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "defining-rule",
    "source": [
      "urn:csabs:source/open-logic-propositional-2026"
    ],
    "sourceLocator": "§1.3 Definition 1.7; §1.2 inductive syntax",
    "sourceNote": "Uniform substitution is extended to an arbitrary simultaneous atom map; finite support is defined by the same syntax recursion.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/PropositionalFormula-substitution-identity",
    "type": "Law",
    "name": "substitution-identity",
    "statement": "Replacing each atom by itself preserves raw syntax.",
    "formalStatement": "subst(atom,p)=p",
    "assumptions": [
      "A is any set, possibly empty. Equality is raw constructor-tree identity. Finite formulas only; no binders or quotient by logical equivalence. All derived connective notation expands into ⊥, ¬, ∧."
    ],
    "appliesTo": [
      "urn:csabs:concept/PropositionalFormula"
    ],
    "reviewStatus": "Editorial source and mathematical interface review; no compiled proof witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/PropositionalFormula-induction",
      "urn:csabs:axiom/PropositionalFormula-substitution"
    ],
    "proofSketch": "Induct on p. The atom and bottom cases compute; negation and conjunction follow by congruence.",
    "source": [
      "urn:csabs:source/open-logic-propositional-2026"
    ],
    "sourceLocator": "§1.3 Definition 1.7 and Theorem 1.3",
    "sourceNote": "Selected presentation in catalog notation; finite raw syntax and the stated primitive basis are explicit choices. No executable proof is implied.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/PropositionalFormula-substitution-composition",
    "type": "Theorem",
    "name": "substitution-composition",
    "statement": "Successive simultaneous substitutions compose.",
    "formalStatement": "subst(τ,subst(σ,p))=subst((a↦subst(τ,σ(a))),p)",
    "assumptions": [
      "A is any set, possibly empty. Equality is raw constructor-tree identity. Finite formulas only; no binders or quotient by logical equivalence. All derived connective notation expands into ⊥, ¬, ∧."
    ],
    "appliesTo": [
      "urn:csabs:concept/PropositionalFormula"
    ],
    "reviewStatus": "Editorial source and mathematical interface review; no compiled proof witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/PropositionalFormula-induction",
      "urn:csabs:axiom/PropositionalFormula-substitution"
    ],
    "proofSketch": "Induct on p; at an atom both sides are subst(τ,σ(a)); all other constructors commute with substitution.",
    "source": [
      "urn:csabs:source/open-logic-propositional-2026"
    ],
    "sourceLocator": "§1.3 Definition 1.7 and Theorem 1.3",
    "sourceNote": "Selected presentation in catalog notation; finite raw syntax and the stated primitive basis are explicit choices. No executable proof is implied.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
