# Propositional Logic

Classical two-valued formulas built from atomic propositions and Boolean connectives, interpreted under valuations.

**Notation:** v:Atoms→{false,true}; v(¬p)=¬v(p)

**Stable ID:** `urn:csabs:concept/PropositionalLogic`

**Categories:** Logic and proof

**Kind:** semantic-model

**Prerequisites:** [Boolean algebra](BooleanAlgebra.md)

**Related concepts:** [Classical propositional modal logic K](ModalLogic.md), [Linear temporal logic on infinite discrete traces](LinearTemporalLogic.md)

## Backlinks

- [Finite serial Kripke structure for model checking](KripkeStructure.md) — `requiresConcept`
- [Linear temporal logic on infinite discrete traces](LinearTemporalLogic.md) — `requiresConcept`
- [Classical propositional modal logic K](ModalLogic.md) — `requiresConcept`
- [Predicate Logic](PredicateLogic.md) — `requiresConcept`

## Interface and scope

**axiomBasis:** Selected presentation: Classical two-valued formulas built from atomic propositions and Boolean connectives, interpreted under valuations. Governing rules: Boolean valuations interpret connectives by classical truth functions. Semantic consequence quantifies over all valuations.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**verificationObligation:** Instantiate carrier, equality, and stated semantic conventions before using this entry.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

**provenanceStatus:** legacy-source-missing

## Operations

<a id="node-urn-csabs-operation-PropositionalLogic-basis-evaluate"></a>

### evaluate

`urn:csabs:operation/PropositionalLogic-basis-evaluate`

**signature:** eval : Formula×Valuation→Bool

**description:** Recursively evaluates a formula under a Boolean assignment.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-PropositionalLogic-truth-semantics"></a>

### truth-semantics

`urn:csabs:axiom/PropositionalLogic-truth-semantics`

**statement:** Boolean valuations interpret connectives by classical truth functions.

**formalStatement:** v(⊥)=false; v(⊤)=true; v(¬p)=not(v(p)); v(p∧q)=v(p) and v(q); v(p∨q)=v(p) or v(q); v(p⇒q)=not(v(p)) or v(q)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-PropositionalLogic-entailment"></a>

### entailment

`urn:csabs:axiom/PropositionalLogic-entailment`

**statement:** Semantic consequence quantifies over all valuations.

**formalStatement:** Γ⊨φ iff ∀v: (∀ψ∈Γ:v(ψ)=true)⇒v(φ)=true

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

<a id="node-urn-csabs-law-PropositionalLogic-core"></a>

### law/PropositionalLogic-core

`urn:csabs:law/PropositionalLogic-core`

**statement:** Modus ponens preserves truth.

**formalStatement:** v(p)=true ∧ v(p⇒q)=true ⇒ v(q)=true

**reviewStatus:** editorial-summary; not machine-proved

**assumptions:** Use the carrier and semantic convention in the linked concept definition.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [truth-semantics](PropositionalLogic.md#node-urn-csabs-axiom-PropositionalLogic-truth-semantics); [entailment](PropositionalLogic.md#node-urn-csabs-axiom-PropositionalLogic-entailment)

**provenanceStatus:** legacy-source-missing

## Theorems

<a id="node-urn-csabs-theorem-PropositionalLogic-double-negation"></a>

### double-negation

`urn:csabs:theorem/PropositionalLogic-double-negation`

**statement:** Classical double negation preserves truth under every valuation.

**formalStatement:** ⊨¬¬p↔p

**proofSketch:** Check the two truth values of p.

**assumptions:** The explicit basis, carriers, and side conditions stated for PropositionalLogic apply.

**dependsOn:** [truth-semantics](PropositionalLogic.md#node-urn-csabs-axiom-PropositionalLogic-truth-semantics); [entailment](PropositionalLogic.md#node-urn-csabs-axiom-PropositionalLogic-entailment)

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
      "urn:csabs:operation/PropositionalLogic-basis-evaluate"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/PropositionalLogic-truth-semantics",
      "urn:csabs:axiom/PropositionalLogic-entailment"
    ],
    "hasLaw": [
      "urn:csabs:law/PropositionalLogic-core"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/PropositionalLogic-double-negation"
    ],
    "requiresConcept": [
      "urn:csabs:concept/BooleanAlgebra"
    ],
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Instantiate carrier, equality, and stated semantic conventions before using this entry.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: Classical two-valued formulas built from atomic propositions and Boolean connectives, interpreted under valuations. Governing rules: Boolean valuations interpret connectives by classical truth functions. Semantic consequence quantifies over all valuations.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "provenanceStatus": "legacy-source-missing",
    "relatedConcept": [
      "urn:csabs:concept/ModalLogic",
      "urn:csabs:concept/LinearTemporalLogic"
    ]
  },
  {
    "id": "urn:csabs:operation/PropositionalLogic-basis-evaluate",
    "type": "Operation",
    "name": "evaluate",
    "signature": "eval : Formula×Valuation→Bool",
    "description": "Recursively evaluates a formula under a Boolean assignment.",
    "concept": "urn:csabs:concept/PropositionalLogic"
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
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
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
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:law/PropositionalLogic-core",
    "type": "Law",
    "statement": "Modus ponens preserves truth.",
    "formalStatement": "v(p)=true ∧ v(p⇒q)=true ⇒ v(q)=true",
    "appliesTo": [
      "urn:csabs:concept/PropositionalLogic"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "assumptions": [
      "Use the carrier and semantic convention in the linked concept definition."
    ],
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/PropositionalLogic-truth-semantics",
      "urn:csabs:axiom/PropositionalLogic-entailment"
    ],
    "provenanceStatus": "legacy-source-missing"
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
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
