# Predicate Logic

First-order formulas over a signature, interpreted in a nonempty domain with variable assignments and quantifiers.

**Notation:** M,ρ ⊨ ∀x φ iff ∀a∈D: M,ρ[x↦a] ⊨ φ

**Stable ID:** `urn:csabs:concept/PredicateLogic`

**Categories:** Logic and proof

**Kind:** semantic-model

**Prerequisites:** [Propositional Logic](PropositionalLogic.md)

## Backlinks

- [Functional dependency on a relational schema](FunctionalDependency.md) — `requiresConcept`
- [Hoare Triple](HoareTriple.md) — `requiresConcept`
- [Classical propositional modal logic K](ModalLogic.md) — `relatedConcept`
- [Predicate-restricted subtype](Subtype.md) — `requiresConcept`
- [Free ranked term algebra with variables](TermAlgebra.md) — `relatedConcept`

## Interface and scope

**axiomBasis:** Selected presentation: First-order formulas over a signature, interpreted in a nonempty domain with variable assignments and quantifiers. Governing rules: A first-order interpretation has a nonempty domain and total interpretations of function symbols. Quantifier semantics ranges over all domain values and respects variable assignments. Logical connectives are interpreted classically at each structure and assignment.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**verificationObligation:** Instantiate carrier, equality, and stated semantic conventions before using this entry.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

**provenanceStatus:** legacy-source-missing

## Operations

<a id="node-urn-csabs-operation-PredicateLogic-basis-satisfies"></a>

### satisfies

`urn:csabs:operation/PredicateLogic-basis-satisfies`

**signature:** satisfies : Structure×Assignment×Formula→Prop

**description:** Interprets first-order satisfaction; this is not a general decision algorithm.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-PredicateLogic-structure"></a>

### structure

`urn:csabs:axiom/PredicateLogic-structure`

**statement:** A first-order interpretation has a nonempty domain and total interpretations of function symbols.

**formalStatement:** D≠∅; f with arity n has f^M:D^n→D; R with arity n has R^M⊆D^n; equality is domain identity

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-PredicateLogic-quantifiers"></a>

### quantifiers

`urn:csabs:axiom/PredicateLogic-quantifiers`

**statement:** Quantifier semantics ranges over all domain values and respects variable assignments.

**formalStatement:** M,ρ⊨∀x φ iff ∀a∈D:M,ρ[x↦a]⊨φ; M,ρ⊨∃x φ iff ∃a∈D:M,ρ[x↦a]⊨φ

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-PredicateLogic-connectives"></a>

### connectives

`urn:csabs:axiom/PredicateLogic-connectives`

**statement:** Logical connectives are interpreted classically at each structure and assignment.

**formalStatement:** M,ρ⊨¬φ iff not(M,ρ⊨φ); M,ρ⊨φ∧ψ iff (M,ρ⊨φ and M,ρ⊨ψ); ∨,⇒ use classical Boolean semantics

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

<a id="node-urn-csabs-law-PredicateLogic-core"></a>

### law/PredicateLogic-core

`urn:csabs:law/PredicateLogic-core`

**statement:** Universal instantiation is sound for substitution free of variable capture.

**formalStatement:** ∀x φ ⇒ φ[t/x], when t is free for x in φ

**reviewStatus:** editorial-summary; not machine-proved

**assumptions:** Use the carrier and semantic convention in the linked concept definition.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [structure](PredicateLogic.md#node-urn-csabs-axiom-PredicateLogic-structure); [quantifiers](PredicateLogic.md#node-urn-csabs-axiom-PredicateLogic-quantifiers); [connectives](PredicateLogic.md#node-urn-csabs-axiom-PredicateLogic-connectives)

**provenanceStatus:** legacy-source-missing

## Theorems

<a id="node-urn-csabs-theorem-PredicateLogic-quantifier-duality"></a>

### quantifier-duality

`urn:csabs:theorem/PredicateLogic-quantifier-duality`

**statement:** Classical universal quantification is dual to existential quantification.

**formalStatement:** ∀x φ ↔ ¬∃x ¬φ

**proofSketch:** Unfold satisfaction and classical negation of an existential statement.

**assumptions:** The explicit basis, carriers, and side conditions stated for PredicateLogic apply.

**dependsOn:** [structure](PredicateLogic.md#node-urn-csabs-axiom-PredicateLogic-structure); [quantifiers](PredicateLogic.md#node-urn-csabs-axiom-PredicateLogic-quantifiers); [connectives](PredicateLogic.md#node-urn-csabs-axiom-PredicateLogic-connectives)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Concept provenance

Historical source gap retained; see `provenanceStatus` and the frozen baseline.

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
      "urn:csabs:operation/PredicateLogic-basis-satisfies"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/PredicateLogic-structure",
      "urn:csabs:axiom/PredicateLogic-quantifiers",
      "urn:csabs:axiom/PredicateLogic-connectives"
    ],
    "hasLaw": [
      "urn:csabs:law/PredicateLogic-core"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/PredicateLogic-quantifier-duality"
    ],
    "requiresConcept": [
      "urn:csabs:concept/PropositionalLogic"
    ],
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Instantiate carrier, equality, and stated semantic conventions before using this entry.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: First-order formulas over a signature, interpreted in a nonempty domain with variable assignments and quantifiers. Governing rules: A first-order interpretation has a nonempty domain and total interpretations of function symbols. Quantifier semantics ranges over all domain values and respects variable assignments. Logical connectives are interpreted classically at each structure and assignment.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:operation/PredicateLogic-basis-satisfies",
    "type": "Operation",
    "name": "satisfies",
    "signature": "satisfies : Structure×Assignment×Formula→Prop",
    "description": "Interprets first-order satisfaction; this is not a general decision algorithm.",
    "concept": "urn:csabs:concept/PredicateLogic"
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
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
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
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
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
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:law/PredicateLogic-core",
    "type": "Law",
    "statement": "Universal instantiation is sound for substitution free of variable capture.",
    "formalStatement": "∀x φ ⇒ φ[t/x], when t is free for x in φ",
    "appliesTo": [
      "urn:csabs:concept/PredicateLogic"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "assumptions": [
      "Use the carrier and semantic convention in the linked concept definition."
    ],
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/PredicateLogic-structure",
      "urn:csabs:axiom/PredicateLogic-quantifiers",
      "urn:csabs:axiom/PredicateLogic-connectives"
    ],
    "provenanceStatus": "legacy-source-missing"
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
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
