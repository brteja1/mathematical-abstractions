# Termination Variant

A measure from states into a well-founded carrier that strictly decreases on each loop iteration or recursive call.

**Notation:** μ:S→W; next(s,t)⇒μ(t)≺μ(s)

**Stable ID:** `urn:csabs:concept/TerminationVariant`

**Categories:** Programming-language semantics

**Kind:** Function

**Prerequisites:** [Well Founded Relation](WellFoundedRelation.md)

## Interface and scope

**axiomBasis:** Selected presentation: A measure from states into a well-founded carrier that strictly decreases on each loop iteration or recursive call. Governing rules: The measure maps loop states to a specified well-founded strict relation. Each enabled iteration that finishes decreases the measure.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**verificationObligation:** Instantiate carrier, equality, and stated semantic conventions before using this entry.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.; Prove each enabled body execution terminates normally and every continuing iteration decreases the measure. A decreasing-on-return condition alone does not rule out divergence inside the body.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

**provenanceStatus:** legacy-source-missing

## Operations

<a id="node-urn-csabs-operation-TerminationVariant-basis-measure"></a>

### measure

`urn:csabs:operation/TerminationVariant-basis-measure`

**signature:** measure : State→W

**description:** Evaluates the well-founded measure at a state.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-TerminationVariant-well-founded-measure"></a>

### well-founded-measure

`urn:csabs:axiom/TerminationVariant-well-founded-measure`

**statement:** The measure maps loop states to a specified well-founded strict relation.

**formalStatement:** μ:S→W; ≺ is well-founded on W

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-TerminationVariant-strict-decrease"></a>

### strict-decrease

`urn:csabs:axiom/TerminationVariant-strict-decrease`

**statement:** Each enabled iteration that finishes decreases the measure.

**formalStatement:** I(s)∧b(s)∧Exec_C(s,t) ⇒ μ(t)≺μ(s)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

<a id="node-urn-csabs-law-TerminationVariant-core"></a>

### law/TerminationVariant-core

`urn:csabs:law/TerminationVariant-core`

**statement:** If every enabled iteration terminates normally and strictly decreases a well-founded measure, the loop cannot execute infinitely many iterations.

**formalStatement:** No infinite chain μ(s0)≻μ(s1)≻…

**reviewStatus:** editorial-summary; not machine-proved

**assumptions:** Well-founded codomain; Every enabled body execution terminates normally; Every continuing iteration strictly decreases the measure

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [well-founded-measure](TerminationVariant.md#node-urn-csabs-axiom-TerminationVariant-well-founded-measure); [strict-decrease](TerminationVariant.md#node-urn-csabs-axiom-TerminationVariant-strict-decrease)

**provenanceStatus:** legacy-source-missing

## Theorems

<a id="node-urn-csabs-theorem-TerminationVariant-natural-bound"></a>

### natural-bound

`urn:csabs:theorem/TerminationVariant-natural-bound`

**statement:** A natural-valued variant decreasing on each iteration bounds the number of completed iterations.

**formalStatement:** μ(s₀)=N; every iteration strictly decreases μ∈ℕ ⇒ at most N iterations

**proofSketch:** Each strict natural decrease reduces the measure by at least one and it cannot be negative; body termination is still a separate requirement.

**assumptions:** Natural-valued measure; Every continuing iteration strictly decreases the measure; Every enabled body execution terminates normally to conclude loop termination.

**dependsOn:** [well-founded-measure](TerminationVariant.md#node-urn-csabs-axiom-TerminationVariant-well-founded-measure); [strict-decrease](TerminationVariant.md#node-urn-csabs-axiom-TerminationVariant-strict-decrease)

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
    "id": "urn:csabs:concept/TerminationVariant",
    "type": "Concept",
    "shortForm": "TerminationVariant",
    "fullName": "Termination Variant",
    "category": [
      "urn:csabs:category/programming-semantics"
    ],
    "kind": "urn:csabs:kind/function",
    "definition": "A measure from states into a well-founded carrier that strictly decreases on each loop iteration or recursive call.",
    "notation": "μ:S→W; next(s,t)⇒μ(t)≺μ(s)",
    "hasOperation": [
      "urn:csabs:operation/TerminationVariant-basis-measure"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/TerminationVariant-well-founded-measure",
      "urn:csabs:axiom/TerminationVariant-strict-decrease"
    ],
    "hasLaw": [
      "urn:csabs:law/TerminationVariant-core"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/TerminationVariant-natural-bound"
    ],
    "requiresConcept": [
      "urn:csabs:concept/WellFoundedRelation"
    ],
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Instantiate carrier, equality, and stated semantic conventions before using this entry.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.",
      "Prove each enabled body execution terminates normally and every continuing iteration decreases the measure. A decreasing-on-return condition alone does not rule out divergence inside the body."
    ],
    "axiomBasis": "Selected presentation: A measure from states into a well-founded carrier that strictly decreases on each loop iteration or recursive call. Governing rules: The measure maps loop states to a specified well-founded strict relation. Each enabled iteration that finishes decreases the measure.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:operation/TerminationVariant-basis-measure",
    "type": "Operation",
    "name": "measure",
    "signature": "measure : State→W",
    "description": "Evaluates the well-founded measure at a state.",
    "concept": "urn:csabs:concept/TerminationVariant"
  },
  {
    "id": "urn:csabs:axiom/TerminationVariant-well-founded-measure",
    "type": "Axiom",
    "name": "well-founded-measure",
    "statement": "The measure maps loop states to a specified well-founded strict relation.",
    "formalStatement": "μ:S→W; ≺ is well-founded on W",
    "appliesTo": [
      "urn:csabs:concept/TerminationVariant"
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
    "id": "urn:csabs:axiom/TerminationVariant-strict-decrease",
    "type": "Axiom",
    "name": "strict-decrease",
    "statement": "Each enabled iteration that finishes decreases the measure.",
    "formalStatement": "I(s)∧b(s)∧Exec_C(s,t) ⇒ μ(t)≺μ(s)",
    "appliesTo": [
      "urn:csabs:concept/TerminationVariant"
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
    "id": "urn:csabs:law/TerminationVariant-core",
    "type": "Law",
    "statement": "If every enabled iteration terminates normally and strictly decreases a well-founded measure, the loop cannot execute infinitely many iterations.",
    "formalStatement": "No infinite chain μ(s0)≻μ(s1)≻…",
    "appliesTo": [
      "urn:csabs:concept/TerminationVariant"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "assumptions": [
      "Well-founded codomain",
      "Every enabled body execution terminates normally",
      "Every continuing iteration strictly decreases the measure"
    ],
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/TerminationVariant-well-founded-measure",
      "urn:csabs:axiom/TerminationVariant-strict-decrease"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/TerminationVariant-natural-bound",
    "type": "Theorem",
    "name": "natural-bound",
    "statement": "A natural-valued variant decreasing on each iteration bounds the number of completed iterations.",
    "formalStatement": "μ(s₀)=N; every iteration strictly decreases μ∈ℕ ⇒ at most N iterations",
    "proofSketch": "Each strict natural decrease reduces the measure by at least one and it cannot be negative; body termination is still a separate requirement.",
    "assumptions": [
      "Natural-valued measure",
      "Every continuing iteration strictly decreases the measure",
      "Every enabled body execution terminates normally to conclude loop termination."
    ],
    "appliesTo": [
      "urn:csabs:concept/TerminationVariant"
    ],
    "dependsOn": [
      "urn:csabs:axiom/TerminationVariant-well-founded-measure",
      "urn:csabs:axiom/TerminationVariant-strict-decrease"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
