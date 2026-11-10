# Simulation

A relation between transition systems matching each step of the first with a step of the second; this entry uses strong simulation.

**Notation:** R⊆S×T; sRt∧s→s' ⇒ ∃t':t→t'∧s'Rt'

**Stable ID:** `urn:csabs:concept/Simulation`

**Categories:** Programming-language semantics, Behavior and transition systems

**Kind:** Relation

**Prerequisites:** [Transition System](TransitionSystem.md)

**Specializes:** [Binary relation](Relation.md)

## Backlinks

- [Behavioral subtyping with explicit history constraints](BehavioralSubtyping.md) — `relatedConcept`
- [Bisimulation](Bisimulation.md) — `requiresConcept`
- [Bisimulation](Bisimulation.md) — `specializationOf`
- [Action-labelled transition system with initial states](LabelledTransitionSystem.md) — `relatedConcept`

## Interface and scope

**axiomBasis:** Selected presentation: A relation between transition systems matching each step of the first with a step of the second; this entry uses strong simulation. Governing rules: Strong labeled simulation matches each labeled source transition with one identically labeled target transition.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**specializationNote:** Use the state sets of the two transition systems as the carriers of the relation; strong step matching is the additional constraint.

**verificationObligation:** Instantiate carrier, equality, and stated semantic conventions before using this entry.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

**provenanceStatus:** legacy-source-missing

## Operations

<a id="node-urn-csabs-operation-Simulation-basis-matches"></a>

### matches

`urn:csabs:operation/Simulation-basis-matches`

**signature:** matches : Relation×LTS×LTS→Prop

**description:** States strong labeled step matching.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-Simulation-step-matching"></a>

### step-matching

`urn:csabs:axiom/Simulation-step-matching`

**statement:** Strong labeled simulation matches each labeled source transition with one identically labeled target transition.

**formalStatement:** sRt ∧ s−a→s′ ⇒ ∃t′:t−a→t′ ∧ s′Rt′

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

<a id="node-urn-csabs-law-Simulation-core"></a>

### law/Simulation-core

`urn:csabs:law/Simulation-core`

**statement:** With related initial states and matching observable labels, simulated finite traces are preserved.

**formalStatement:** Traces_finite(S)⊆Traces_finite(T)

**reviewStatus:** editorial-summary; not machine-proved

**assumptions:** Use the carrier and semantic convention in the linked concept definition.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [step-matching](Simulation.md#node-urn-csabs-axiom-Simulation-step-matching)

**provenanceStatus:** legacy-source-missing

## Theorems

<a id="node-urn-csabs-theorem-Simulation-identity-simulation"></a>

### identity-simulation

`urn:csabs:theorem/Simulation-identity-simulation`

**statement:** A transition system strongly simulates itself by equality.

**formalStatement:** R={(s,s):s∈S} is a strong labeled simulation

**proofSketch:** Match each transition with itself.

**assumptions:** The explicit basis, carriers, and side conditions stated for Simulation apply.

**dependsOn:** [step-matching](Simulation.md#node-urn-csabs-axiom-Simulation-step-matching)

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
    "id": "urn:csabs:concept/Simulation",
    "type": "Concept",
    "shortForm": "Simulation",
    "fullName": "Simulation",
    "category": [
      "urn:csabs:category/programming-semantics",
      "urn:csabs:category/behavior"
    ],
    "kind": "urn:csabs:kind/relation",
    "definition": "A relation between transition systems matching each step of the first with a step of the second; this entry uses strong simulation.",
    "notation": "R⊆S×T; sRt∧s→s' ⇒ ∃t':t→t'∧s'Rt'",
    "hasOperation": [
      "urn:csabs:operation/Simulation-basis-matches"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/Simulation-step-matching"
    ],
    "hasLaw": [
      "urn:csabs:law/Simulation-core"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/Simulation-identity-simulation"
    ],
    "requiresConcept": [
      "urn:csabs:concept/TransitionSystem"
    ],
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Instantiate carrier, equality, and stated semantic conventions before using this entry.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: A relation between transition systems matching each step of the first with a step of the second; this entry uses strong simulation. Governing rules: Strong labeled simulation matches each labeled source transition with one identically labeled target transition.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "provenanceStatus": "legacy-source-missing",
    "specializationOf": [
      "urn:csabs:concept/Relation"
    ],
    "specializationNote": "Use the state sets of the two transition systems as the carriers of the relation; strong step matching is the additional constraint."
  },
  {
    "id": "urn:csabs:operation/Simulation-basis-matches",
    "type": "Operation",
    "name": "matches",
    "signature": "matches : Relation×LTS×LTS→Prop",
    "description": "States strong labeled step matching.",
    "concept": "urn:csabs:concept/Simulation"
  },
  {
    "id": "urn:csabs:axiom/Simulation-step-matching",
    "type": "Axiom",
    "name": "step-matching",
    "statement": "Strong labeled simulation matches each labeled source transition with one identically labeled target transition.",
    "formalStatement": "sRt ∧ s−a→s′ ⇒ ∃t′:t−a→t′ ∧ s′Rt′",
    "appliesTo": [
      "urn:csabs:concept/Simulation"
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
    "id": "urn:csabs:law/Simulation-core",
    "type": "Law",
    "statement": "With related initial states and matching observable labels, simulated finite traces are preserved.",
    "formalStatement": "Traces_finite(S)⊆Traces_finite(T)",
    "appliesTo": [
      "urn:csabs:concept/Simulation"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "assumptions": [
      "Use the carrier and semantic convention in the linked concept definition."
    ],
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/Simulation-step-matching"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/Simulation-identity-simulation",
    "type": "Theorem",
    "name": "identity-simulation",
    "statement": "A transition system strongly simulates itself by equality.",
    "formalStatement": "R={(s,s):s∈S} is a strong labeled simulation",
    "proofSketch": "Match each transition with itself.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for Simulation apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/Simulation"
    ],
    "dependsOn": [
      "urn:csabs:axiom/Simulation-step-matching"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
