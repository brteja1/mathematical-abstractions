# Hoare Triple

A partial-correctness contract: starting in a state satisfying P, every terminating execution of C ends in a state satisfying Q.

**Notation:** {P} C {Q} iff ∀s,t: P(s)∧C(s,t)⇒Q(t)

**Stable ID:** `urn:csabs:concept/HoareTriple`

**Categories:** Programming-language semantics

**Kind:** semantic-model

**Prerequisites:** [Predicate Logic](PredicateLogic.md), [Binary relation](Relation.md)

## Backlinks

- [Loop Invariant](LoopInvariant.md) — `requiresConcept`
- [Relational method contract with write effects](MethodContract.md) — `requiresConcept`
- [Weakest Precondition](WeakestPrecondition.md) — `requiresConcept`

## Interface and scope

**axiomBasis:** Selected presentation: A partial-correctness contract: starting in a state satisfying P, every terminating execution of C ends in a state satisfying Q. Governing rules: A Hoare triple constrains every normally terminating behavior; it does not require termination. Sequential command semantics joins the intermediate state.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**verificationObligation:** Partial correctness does not imply termination. State the command relation and treatment of faults.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-HoareTriple-basis-holds"></a>

### holds

`urn:csabs:operation/HoareTriple-basis-holds`

**signature:** holds : Predicate×Command×Predicate→Prop

**description:** Returns the partial-correctness assertion defined by terminating command executions.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-HoareTriple-partial-correctness"></a>

### partial-correctness

`urn:csabs:axiom/HoareTriple-partial-correctness`

**statement:** A Hoare triple constrains every normally terminating behavior; it does not require termination.

**formalStatement:** {P}C{Q} iff ∀s,t:(P(s)∧Exec_C(s,t))⇒Q(t)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-HoareTriple-command-composition"></a>

### command-composition

`urn:csabs:axiom/HoareTriple-command-composition`

**statement:** Sequential command semantics joins the intermediate state.

**formalStatement:** Exec_(C;D)(s,t) iff ∃m:Exec_C(s,m)∧Exec_D(m,t)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

<a id="node-urn-csabs-law-HoareTriple-core"></a>

### law/HoareTriple-core

`urn:csabs:law/HoareTriple-core`

**statement:** Sequential composition of partial-correctness triples is sound.

**formalStatement:** {P}C{R} ∧ {R}D{Q} ⇒ {P}C;D{Q}

**reviewStatus:** editorial-summary; not machine-proved

**assumptions:** Use the carrier and semantic convention in the linked concept definition.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [partial-correctness](HoareTriple.md#node-urn-csabs-axiom-HoareTriple-partial-correctness); [command-composition](HoareTriple.md#node-urn-csabs-axiom-HoareTriple-command-composition)

**provenanceStatus:** legacy-source-missing

## Theorems

<a id="node-urn-csabs-theorem-HoareTriple-consequence"></a>

### consequence

`urn:csabs:theorem/HoareTriple-consequence`

**statement:** Strengthening the precondition and weakening the postcondition preserves partial correctness.

**formalStatement:** P′⇒P; {P}C{Q}; Q⇒Q′ ⇒ {P′}C{Q′}

**proofSketch:** Compose the precondition implication, the triple definition, and the postcondition implication.

**assumptions:** The explicit basis, carriers, and side conditions stated for HoareTriple apply.

**dependsOn:** [partial-correctness](HoareTriple.md#node-urn-csabs-axiom-HoareTriple-partial-correctness); [command-composition](HoareTriple.md#node-urn-csabs-axiom-HoareTriple-command-composition)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Concept provenance

- [Software Foundations: Hoare Logic](https://softwarefoundations.cis.upenn.edu/plf-current/Hoare.html); sourceRole: reference-for-selected-basis

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/HoareTriple",
    "type": "Concept",
    "shortForm": "HoareTriple",
    "fullName": "Hoare Triple",
    "category": [
      "urn:csabs:category/programming-semantics"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "definition": "A partial-correctness contract: starting in a state satisfying P, every terminating execution of C ends in a state satisfying Q.",
    "notation": "{P} C {Q} iff ∀s,t: P(s)∧C(s,t)⇒Q(t)",
    "hasOperation": [
      "urn:csabs:operation/HoareTriple-basis-holds"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/HoareTriple-partial-correctness",
      "urn:csabs:axiom/HoareTriple-command-composition"
    ],
    "hasLaw": [
      "urn:csabs:law/HoareTriple-core"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/HoareTriple-consequence"
    ],
    "requiresConcept": [
      "urn:csabs:concept/PredicateLogic",
      "urn:csabs:concept/Relation"
    ],
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Partial correctness does not imply termination. State the command relation and treatment of faults.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: A partial-correctness contract: starting in a state satisfying P, every terminating execution of C ends in a state satisfying Q. Governing rules: A Hoare triple constrains every normally terminating behavior; it does not require termination. Sequential command semantics joins the intermediate state.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "source": [
      "urn:csabs:source/sf-hoare"
    ]
  },
  {
    "id": "urn:csabs:operation/HoareTriple-basis-holds",
    "type": "Operation",
    "name": "holds",
    "signature": "holds : Predicate×Command×Predicate→Prop",
    "description": "Returns the partial-correctness assertion defined by terminating command executions.",
    "concept": "urn:csabs:concept/HoareTriple"
  },
  {
    "id": "urn:csabs:axiom/HoareTriple-partial-correctness",
    "type": "Axiom",
    "name": "partial-correctness",
    "statement": "A Hoare triple constrains every normally terminating behavior; it does not require termination.",
    "formalStatement": "{P}C{Q} iff ∀s,t:(P(s)∧Exec_C(s,t))⇒Q(t)",
    "appliesTo": [
      "urn:csabs:concept/HoareTriple"
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
    "id": "urn:csabs:axiom/HoareTriple-command-composition",
    "type": "Axiom",
    "name": "command-composition",
    "statement": "Sequential command semantics joins the intermediate state.",
    "formalStatement": "Exec_(C;D)(s,t) iff ∃m:Exec_C(s,m)∧Exec_D(m,t)",
    "appliesTo": [
      "urn:csabs:concept/HoareTriple"
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
    "id": "urn:csabs:law/HoareTriple-core",
    "type": "Law",
    "statement": "Sequential composition of partial-correctness triples is sound.",
    "formalStatement": "{P}C{R} ∧ {R}D{Q} ⇒ {P}C;D{Q}",
    "appliesTo": [
      "urn:csabs:concept/HoareTriple"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "assumptions": [
      "Use the carrier and semantic convention in the linked concept definition."
    ],
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/HoareTriple-partial-correctness",
      "urn:csabs:axiom/HoareTriple-command-composition"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/HoareTriple-consequence",
    "type": "Theorem",
    "name": "consequence",
    "statement": "Strengthening the precondition and weakening the postcondition preserves partial correctness.",
    "formalStatement": "P′⇒P; {P}C{Q}; Q⇒Q′ ⇒ {P′}C{Q′}",
    "proofSketch": "Compose the precondition implication, the triple definition, and the postcondition implication.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for HoareTriple apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/HoareTriple"
    ],
    "dependsOn": [
      "urn:csabs:axiom/HoareTriple-partial-correctness",
      "urn:csabs:axiom/HoareTriple-command-composition"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
