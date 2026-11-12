# Bisimulation

A relation that matches transitions in both directions, with observations preserved where present; this entry uses strong bisimulation.

**Notation:** R and R⁻¹ are simulations

**Stable ID:** `urn:csabs:concept/Bisimulation`

**Categories:** Programming-language semantics, Behavior and transition systems

**Kind:** Relation

**Prerequisites:** [Simulation](Simulation.md)

**Specializes:** [Simulation](Simulation.md)

## Backlinks

- [Action-labelled transition system with initial states](LabelledTransitionSystem.md) — `relatedConcept`
- [Strong finite partial-trace equivalence](TraceEquivalence.md) — `relatedConcept`

## Mathematical formulation

R⊆S×T is a strong bisimulation iff Simulation(S,T,R) ∧ Simulation(T,S,R⁻¹), with identical visible action labels on matched steps. No silent-step quotient is implicit.

**Lean formulation** (in its source module context):

```lean
def Bisimulation {S : Type u} {T : Type v} {Act : Type w}
    (s : LabelledTransitionSystem S Act) (t : LabelledTransitionSystem T Act)
    (r : S → T → Prop) : Prop :=
  Simulation s t r ∧ Simulation t s (fun y x => r x y)
```

**Source:** [`Catalog.Bisimulation`](../lean/Catalog/Graphs.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Strong forward and reverse simulations; use labelled observations if observation preservation is needed.

**Limits:** Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Selected presentation: A relation that matches transitions in both directions, with observations preserved where present; this entry uses strong bisimulation. Governing rules: Strong labeled bisimulation matches transitions in both directions.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**specializationNote:** Keep the same relation and source-to-target orientation; require both it and its converse to match strong steps, retaining any observation constraints.

**verificationObligation:** Instantiate carrier, equality, and stated semantic conventions before using this entry.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

**provenanceStatus:** legacy-source-missing

## Operations

<a id="node-urn-csabs-operation-Bisimulation-basis-matchesBoth"></a>

### matchesBoth

`urn:csabs:operation/Bisimulation-basis-matchesBoth`

**signature:** matchesBoth : Relation×LTS×LTS→Prop

**description:** States strong labeled step matching in both directions.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-Bisimulation-two-way-step-matching"></a>

### two-way-step-matching

`urn:csabs:axiom/Bisimulation-two-way-step-matching`

**statement:** Strong labeled bisimulation matches transitions in both directions.

**formalStatement:** sRt ⇒ [(s−a→s′ ⇒ ∃t′:t−a→t′∧s′Rt′) ∧ (t−a→t′ ⇒ ∃s′:s−a→s′∧s′Rt′)]

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

<a id="node-urn-csabs-law-Bisimulation-core"></a>

### law/Bisimulation-core

`urn:csabs:law/Bisimulation-core`

**statement:** Bisimilar states cannot be distinguished by finite transition observations.

**formalStatement:** s≈t ⇒ same matching finite labeled traces

**reviewStatus:** editorial-summary; not machine-proved

**assumptions:** Use the carrier and semantic convention in the linked concept definition.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [two-way-step-matching](Bisimulation.md#node-urn-csabs-axiom-Bisimulation-two-way-step-matching)

**provenanceStatus:** legacy-source-missing

## Theorems

<a id="node-urn-csabs-theorem-Bisimulation-inverse-bisimulation"></a>

### inverse-bisimulation

`urn:csabs:theorem/Bisimulation-inverse-bisimulation`

**statement:** The inverse of a bisimulation is a bisimulation.

**formalStatement:** R bisimulation ⇒ R⁻¹ bisimulation

**proofSketch:** The two matching clauses exchange roles under inversion.

**assumptions:** The explicit basis, carriers, and side conditions stated for Bisimulation apply.

**dependsOn:** [two-way-step-matching](Bisimulation.md#node-urn-csabs-axiom-Bisimulation-two-way-step-matching)

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
    "id": "urn:csabs:concept/Bisimulation",
    "type": "Concept",
    "shortForm": "Bisimulation",
    "fullName": "Bisimulation",
    "category": [
      "urn:csabs:category/programming-semantics",
      "urn:csabs:category/behavior"
    ],
    "kind": "urn:csabs:kind/relation",
    "definition": "A relation that matches transitions in both directions, with observations preserved where present; this entry uses strong bisimulation.",
    "notation": "R and R⁻¹ are simulations",
    "hasOperation": [
      "urn:csabs:operation/Bisimulation-basis-matchesBoth"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/Bisimulation-two-way-step-matching"
    ],
    "hasLaw": [
      "urn:csabs:law/Bisimulation-core"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/Bisimulation-inverse-bisimulation"
    ],
    "requiresConcept": [
      "urn:csabs:concept/Simulation"
    ],
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Instantiate carrier, equality, and stated semantic conventions before using this entry.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: A relation that matches transitions in both directions, with observations preserved where present; this entry uses strong bisimulation. Governing rules: Strong labeled bisimulation matches transitions in both directions.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "provenanceStatus": "legacy-source-missing",
    "specializationOf": [
      "urn:csabs:concept/Simulation"
    ],
    "specializationNote": "Keep the same relation and source-to-target orientation; require both it and its converse to match strong steps, retaining any observation constraints.",
    "leanFormulation": "def Bisimulation {S : Type u} {T : Type v} {Act : Type w}\n    (s : LabelledTransitionSystem S Act) (t : LabelledTransitionSystem T Act)\n    (r : S → T → Prop) : Prop :=\n  Simulation s t r ∧ Simulation t s (fun y x => r x y)",
    "formulationSource": "urn:csabs:source/local-lean-Graphs",
    "formulationLocator": "Catalog.Bisimulation",
    "formulationScope": "model",
    "leanModelMapping": "Strong forward and reverse simulations; use labelled observations if observation preservation is needed.",
    "leanModelLimitations": "Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.",
    "mathematicalFormulation": "R⊆S×T is a strong bisimulation iff Simulation(S,T,R) ∧ Simulation(T,S,R⁻¹), with identical visible action labels on matched steps. No silent-step quotient is implicit."
  },
  {
    "id": "urn:csabs:operation/Bisimulation-basis-matchesBoth",
    "type": "Operation",
    "name": "matchesBoth",
    "signature": "matchesBoth : Relation×LTS×LTS→Prop",
    "description": "States strong labeled step matching in both directions.",
    "concept": "urn:csabs:concept/Bisimulation"
  },
  {
    "id": "urn:csabs:axiom/Bisimulation-two-way-step-matching",
    "type": "Axiom",
    "name": "two-way-step-matching",
    "statement": "Strong labeled bisimulation matches transitions in both directions.",
    "formalStatement": "sRt ⇒ [(s−a→s′ ⇒ ∃t′:t−a→t′∧s′Rt′) ∧ (t−a→t′ ⇒ ∃s′:s−a→s′∧s′Rt′)]",
    "appliesTo": [
      "urn:csabs:concept/Bisimulation"
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
    "id": "urn:csabs:law/Bisimulation-core",
    "type": "Law",
    "statement": "Bisimilar states cannot be distinguished by finite transition observations.",
    "formalStatement": "s≈t ⇒ same matching finite labeled traces",
    "appliesTo": [
      "urn:csabs:concept/Bisimulation"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "assumptions": [
      "Use the carrier and semantic convention in the linked concept definition."
    ],
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/Bisimulation-two-way-step-matching"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/Bisimulation-inverse-bisimulation",
    "type": "Theorem",
    "name": "inverse-bisimulation",
    "statement": "The inverse of a bisimulation is a bisimulation.",
    "formalStatement": "R bisimulation ⇒ R⁻¹ bisimulation",
    "proofSketch": "The two matching clauses exchange roles under inversion.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for Bisimulation apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/Bisimulation"
    ],
    "dependsOn": [
      "urn:csabs:axiom/Bisimulation-two-way-step-matching"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
