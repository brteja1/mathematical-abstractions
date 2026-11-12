# Transition System

States, initial states, and a transition relation describe allowed executions.

**Notation:** T=(S,I,→); I⊆S; →⊆S×S

**Stable ID:** `urn:csabs:concept/TransitionSystem`

**Categories:** Programming-language semantics, Behavior and transition systems

**Kind:** semantic-model

**Prerequisites:** [Binary relation](Relation.md)

**Related concepts:** [Action-labelled transition system with initial states](LabelledTransitionSystem.md), [Finite serial Kripke structure for model checking](KripkeStructure.md)

## Backlinks

- [Context-free grammar of finite words](ContextFreeGrammar.md) — `requiresConcept`
- [Finite serial Kripke structure for model checking](KripkeStructure.md) — `requiresConcept`
- [Finite serial Kripke structure for model checking](KripkeStructure.md) — `specializationOf`
- [Action-labelled transition system with initial states](LabelledTransitionSystem.md) — `requiresConcept`
- [Action-labelled transition system with initial states](LabelledTransitionSystem.md) — `specializationOf`
- [Liveness Property](LivenessProperty.md) — `requiresConcept`
- [Markov chain (finite-state, discrete-time, time-homogeneous)](MarkovChain.md) — `relatedConcept`
- [Visible-state object invariant protocol](ObjectInvariant.md) — `requiresConcept`
- [Safety Property](SafetyProperty.md) — `requiresConcept`
- [Simulation](Simulation.md) — `requiresConcept`
- [Deterministic one-tape Turing machine](TuringMachine.md) — `requiresConcept`
- [VHDL generic elaboration and static structural generation](VHDLGenericElaboration.md) — `relatedConcept`

## Mathematical formulation

A transition system is (S,I,→) with I⊆S and →⊆S×S. reachable(s) ⇔ ∃i∈I,i→\*s, where →\* is reflexive-transitive closure. Initial states and transition successors may be absent.

**Lean formulation** (in its source module context):

```lean
structure TransitionSystem (S : Type u) where
  initial : _root_.Set S
  next : S → S → Prop
```

**Source:** [`Catalog.TransitionSystem`](../lean/Catalog/Graphs.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Initial-state set and arbitrary binary next relation; reachable via ReflTransGen from an initial state.

**Limits:** Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Selected presentation: States, initial states, and a transition relation describe allowed executions. Governing rules: A transition system has initial states and an arbitrary next-state relation; determinism and totality are additional properties. Reachable states are the least set containing the initial states and closed under Next.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**verificationObligation:** Instantiate carrier, equality, and stated semantic conventions before using this entry.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

**provenanceStatus:** legacy-source-missing

## Operations

<a id="node-urn-csabs-operation-TransitionSystem-post"></a>

### post

`urn:csabs:operation/TransitionSystem-post`

**signature:** post : 𝒫(S)→𝒫(S)

**description:** Returns all one-step successors of any state in the input subset.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-TransitionSystem-state-model"></a>

### state-model

`urn:csabs:axiom/TransitionSystem-state-model`

**statement:** A transition system has initial states and an arbitrary next-state relation; determinism and totality are additional properties.

**formalStatement:** I⊆S; Next⊆S×S

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-TransitionSystem-reachability"></a>

### reachability

`urn:csabs:axiom/TransitionSystem-reachability`

**statement:** Reachable states are the least set containing the initial states and closed under Next.

**formalStatement:** Reach=μX.(I∪post(X)); post(X)={t∈S:∃s∈X:Next(s,t)}

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

<a id="node-urn-csabs-law-TransitionSystem-core"></a>

### law/TransitionSystem-core

`urn:csabs:law/TransitionSystem-core`

**statement:** Inductive invariants hold in every reachable state.

**formalStatement:** I⊆P ∧ (s∈P∧s→t⇒t∈P) ⇒ Reach(I)⊆P

**reviewStatus:** editorial-summary; not machine-proved

**assumptions:** Use the carrier and semantic convention in the linked concept definition.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [state-model](TransitionSystem.md#node-urn-csabs-axiom-TransitionSystem-state-model); [reachability](TransitionSystem.md#node-urn-csabs-axiom-TransitionSystem-reachability)

**provenanceStatus:** legacy-source-missing

## Theorems

<a id="node-urn-csabs-theorem-TransitionSystem-reachability-induction"></a>

### reachability-induction

`urn:csabs:theorem/TransitionSystem-reachability-induction`

**statement:** Reachable states satisfy every predicate containing the initial states and preserved by each transition.

**formalStatement:** I⊆P ∧ post(P)⊆P ⇒ Reach⊆P

**proofSketch:** Induct on the finite number of transitions witnessing reachability.

**assumptions:** The explicit basis, carriers, and side conditions stated for TransitionSystem apply.

**dependsOn:** [state-model](TransitionSystem.md#node-urn-csabs-axiom-TransitionSystem-state-model); [reachability](TransitionSystem.md#node-urn-csabs-axiom-TransitionSystem-reachability)

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
    "id": "urn:csabs:concept/TransitionSystem",
    "type": "Concept",
    "shortForm": "TransitionSystem",
    "fullName": "Transition System",
    "category": [
      "urn:csabs:category/programming-semantics",
      "urn:csabs:category/behavior"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "definition": "States, initial states, and a transition relation describe allowed executions.",
    "notation": "T=(S,I,→); I⊆S; →⊆S×S",
    "hasOperation": [
      "urn:csabs:operation/TransitionSystem-post"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/TransitionSystem-state-model",
      "urn:csabs:axiom/TransitionSystem-reachability"
    ],
    "hasLaw": [
      "urn:csabs:law/TransitionSystem-core"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/TransitionSystem-reachability-induction"
    ],
    "requiresConcept": [
      "urn:csabs:concept/Relation"
    ],
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Instantiate carrier, equality, and stated semantic conventions before using this entry.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: States, initial states, and a transition relation describe allowed executions. Governing rules: A transition system has initial states and an arbitrary next-state relation; determinism and totality are additional properties. Reachable states are the least set containing the initial states and closed under Next.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "provenanceStatus": "legacy-source-missing",
    "relatedConcept": [
      "urn:csabs:concept/LabelledTransitionSystem",
      "urn:csabs:concept/KripkeStructure"
    ],
    "leanFormulation": "structure TransitionSystem (S : Type u) where\n  initial : _root_.Set S\n  next : S → S → Prop",
    "formulationSource": "urn:csabs:source/local-lean-Graphs",
    "formulationLocator": "Catalog.TransitionSystem",
    "formulationScope": "model",
    "leanModelMapping": "Initial-state set and arbitrary binary next relation; reachable via ReflTransGen from an initial state.",
    "leanModelLimitations": "Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.",
    "mathematicalFormulation": "A transition system is (S,I,→) with I⊆S and →⊆S×S. reachable(s) ⇔ ∃i∈I,i→*s, where →* is reflexive-transitive closure. Initial states and transition successors may be absent."
  },
  {
    "id": "urn:csabs:operation/TransitionSystem-post",
    "type": "Operation",
    "name": "post",
    "signature": "post : 𝒫(S)→𝒫(S)",
    "description": "Returns all one-step successors of any state in the input subset.",
    "concept": "urn:csabs:concept/TransitionSystem"
  },
  {
    "id": "urn:csabs:axiom/TransitionSystem-state-model",
    "type": "Axiom",
    "name": "state-model",
    "statement": "A transition system has initial states and an arbitrary next-state relation; determinism and totality are additional properties.",
    "formalStatement": "I⊆S; Next⊆S×S",
    "appliesTo": [
      "urn:csabs:concept/TransitionSystem"
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
    "id": "urn:csabs:axiom/TransitionSystem-reachability",
    "type": "Axiom",
    "name": "reachability",
    "statement": "Reachable states are the least set containing the initial states and closed under Next.",
    "formalStatement": "Reach=μX.(I∪post(X)); post(X)={t∈S:∃s∈X:Next(s,t)}",
    "appliesTo": [
      "urn:csabs:concept/TransitionSystem"
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
    "id": "urn:csabs:law/TransitionSystem-core",
    "type": "Law",
    "statement": "Inductive invariants hold in every reachable state.",
    "formalStatement": "I⊆P ∧ (s∈P∧s→t⇒t∈P) ⇒ Reach(I)⊆P",
    "appliesTo": [
      "urn:csabs:concept/TransitionSystem"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "assumptions": [
      "Use the carrier and semantic convention in the linked concept definition."
    ],
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/TransitionSystem-state-model",
      "urn:csabs:axiom/TransitionSystem-reachability"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/TransitionSystem-reachability-induction",
    "type": "Theorem",
    "name": "reachability-induction",
    "statement": "Reachable states satisfy every predicate containing the initial states and preserved by each transition.",
    "formalStatement": "I⊆P ∧ post(P)⊆P ⇒ Reach⊆P",
    "proofSketch": "Induct on the finite number of transitions witnessing reachability.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for TransitionSystem apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/TransitionSystem"
    ],
    "dependsOn": [
      "urn:csabs:axiom/TransitionSystem-state-model",
      "urn:csabs:axiom/TransitionSystem-reachability"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
