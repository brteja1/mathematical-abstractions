# Action-labelled transition system with initial states

States evolve through an arbitrary relation labelled by actions; a chosen initial-state set supports system-level executions.

**Notation:** T=(S,Act,I,→); I⊆S; →⊆S×Act×S

**Stable ID:** `urn:csabs:concept/LabelledTransitionSystem`

**Categories:** Behavior and transition systems, Programming-language semantics, Concurrency and distributed systems → Behavioral models

**Kind:** semantic-model

**Prerequisites:** [Transition System](TransitionSystem.md), [Binary relation](Relation.md), [Finite sequence (List datatype)](Sequence.md)

**Specializes:** [Transition System](TransitionSystem.md)

**Related concepts:** [Strong finite partial-trace equivalence](TraceEquivalence.md), [Nondeterministic finite automaton without epsilon moves](NFA.md), [Simulation](Simulation.md), [Bisimulation](Bisimulation.md)

## Backlinks

- [Lamport bakery lock protocol](LamportBakery.md) — `requiresConcept`
- [Lock with compatible access modes](Lock.md) — `requiresConcept`
- [Nondeterministic finite automaton without epsilon moves](NFA.md) — `requiresConcept`
- [Nondeterministic finite automaton without epsilon moves](NFA.md) — `specializationOf`
- [Strong finite partial-trace equivalence](TraceEquivalence.md) — `requiresConcept`
- [Transition System](TransitionSystem.md) — `relatedConcept`

## Mathematical formulation

An LTS is (S,Act,I,→) with I⊆S and →⊆S×Act×S. Finite traces from s are words a₁…a\_n labeling a path from s; the empty word is admitted by the reflexive path.

**Lean formulation** (in its source module context):

```lean
structure LabelledTransitionSystem (S : Type u) (Act : Type v) where
  initial : _root_.Set S
  step : S → Act → S → Prop
```

**Source:** [`Catalog.LabelledTransitionSystem`](../lean/Catalog/Graphs.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Initial states and S -> Act -> S -> Prop; finite paths include empty path.

**Limits:** Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Selected defining presentation: The labelled next-state relation may have zero, one, or many outcomes. Finite traces are the labels of finite paths, including the zero-step path.

**basisKind:** defined-structure

**basisScope:** States and actions use identity equality. State/action sets and branching may be infinite; transitions may deadlock or be nondeterministic. All actions, including a symbol called τ if present, are observable here; hiding requires a variant.

**specializationNote:** Forget action labels to obtain parent Next(s,t) iff ∃a∈Act:s —a→ t, with the same S and I. Parent post is the union of action-indexed post operations. No parent law is transferred implicitly.

**verificationObligation:** States and actions use identity equality. State/action sets and branching may be infinite; transitions may deadlock or be nondeterministic. All actions, including a symbol called τ if present, are observable here; hiding requires a variant.

**reviewStatus:** editorial review of defining basis and selected laws, theorems and proof principles; no machine-checked proof

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-LabelledTransitionSystem-postAction"></a>

### postAction

`urn:csabs:operation/LabelledTransitionSystem-postAction`

**signature:** post_a : 𝒫(S)→𝒫(S)

**description:** Returns states reachable in one a-labelled step.

**precondition:** Arguments belong to the carriers in the signature.

**totality:** total mathematical operation on the stated domain

**postcondition:** Returns states reachable in one a-labelled step.

<a id="node-urn-csabs-operation-LabelledTransitionSystem-traces"></a>

### traces

`urn:csabs:operation/LabelledTransitionSystem-traces`

**signature:** Tr : S→𝒫(Act*)

**description:** Returns all finite action words realizable from a state; it does not record termination or infinite behavior.

**precondition:** Arguments belong to the carriers in the signature.

**totality:** total mathematical operation on the stated domain

**postcondition:** Returns all finite action words realizable from a state; it does not record termination or infinite behavior.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-LabelledTransitionSystem-labelled-steps"></a>

### labelled-steps

`urn:csabs:axiom/LabelledTransitionSystem-labelled-steps`

**statement:** The labelled next-state relation may have zero, one, or many outcomes.

**description:** The labelled next-state relation may have zero, one, or many outcomes.

**formalStatement:** I⊆S; →⊆S×Act×S; post_a(X)={t:∃s∈X:s —a→ t}

**assumptions:** States and actions use identity equality. State/action sets and branching may be infinite; transitions may deadlock or be nondeterministic. All actions, including a symbol called τ if present, are observable here; hiding requires a variant.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Rob van Glabbeek: Modelling Concurrent Systems (2024), course notes](https://homepages.inf.ed.ac.uk/rvangla/MCS/notes.html); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Lecture 1, process graphs and LTSs; Lecture 2, trace semantics

**sourceNote:** Adapts the source process graph with one initial state to a possibly empty set of initial states. No successful-termination predicate is included. Local notation specifies the chosen defining presentation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-LabelledTransitionSystem-finite-paths"></a>

### finite-paths

`urn:csabs:axiom/LabelledTransitionSystem-finite-paths`

**statement:** Finite traces are the labels of finite paths, including the zero-step path.

**description:** Finite traces are the labels of finite paths, including the zero-step path.

**formalStatement:** w∈Tr(s) iff ∃n≥0,s₀,…,sₙ: s₀=s ∧ w=a₁…aₙ ∧ ∀1≤i≤n:sᵢ₋₁ —aᵢ→ sᵢ

**assumptions:** States and actions use identity equality. State/action sets and branching may be infinite; transitions may deadlock or be nondeterministic. All actions, including a symbol called τ if present, are observable here; hiding requires a variant.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Rob van Glabbeek: Modelling Concurrent Systems (2024), course notes](https://homepages.inf.ed.ac.uk/rvangla/MCS/notes.html); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Lecture 1, process graphs and LTSs; Lecture 2, trace semantics

**sourceNote:** Adapts the source process graph with one initial state to a possibly empty set of initial states. No successful-termination predicate is included. Local notation specifies the chosen defining presentation.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-LabelledTransitionSystem-post-union"></a>

### post-union

`urn:csabs:law/LabelledTransitionSystem-post-union`

**statement:** Action-indexed post distributes over arbitrary unions, including the empty union.

**description:** Action-indexed post distributes over arbitrary unions, including the empty union.

**formalStatement:** post_a(⋃_{j∈J}X_j)=⋃_{j∈J}post_a(X_j); post_a(∅)=∅

**assumptions:** States and actions use identity equality. State/action sets and branching may be infinite; transitions may deadlock or be nondeterministic. All actions, including a symbol called τ if present, are observable here; hiding requires a variant.

**ruleRole:** derived-result

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Rob van Glabbeek: Modelling Concurrent Systems (2024), course notes](https://homepages.inf.ed.ac.uk/rvangla/MCS/notes.html); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Lecture 1, process graphs and LTSs; Lecture 2, trace semantics

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** An outgoing a-step has a source in the union exactly when its source belongs to some X_j. With no sources there are no targets.

**dependsOn:** [labelled-steps](LabelledTransitionSystem.md#node-urn-csabs-axiom-LabelledTransitionSystem-labelled-steps)

<a id="node-urn-csabs-law-LabelledTransitionSystem-trace-first-step"></a>

### trace-first-step

`urn:csabs:law/LabelledTransitionSystem-trace-first-step`

**statement:** A nonempty trace decomposes into its first action and a residual trace.

**description:** A nonempty trace decomposes into its first action and a residual trace.

**formalStatement:** aw∈Tr(s) iff ∃t:(s —a→ t ∧ w∈Tr(t))

**assumptions:** States and actions use identity equality. State/action sets and branching may be infinite; transitions may deadlock or be nondeterministic. All actions, including a symbol called τ if present, are observable here; hiding requires a variant.

**ruleRole:** derived-result

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Rob van Glabbeek: Modelling Concurrent Systems (2024), course notes](https://homepages.inf.ed.ac.uk/rvangla/MCS/notes.html); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Lecture 1, process graphs and LTSs; Lecture 2, trace semantics

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** Split off the first transition of a witnessing path; conversely prefix a residual path with that transition.

**dependsOn:** [labelled-steps](LabelledTransitionSystem.md#node-urn-csabs-axiom-LabelledTransitionSystem-labelled-steps); [finite-paths](LabelledTransitionSystem.md#node-urn-csabs-axiom-LabelledTransitionSystem-finite-paths)

## Theorems

<a id="node-urn-csabs-theorem-LabelledTransitionSystem-prefix-closure"></a>

### prefix-closure

`urn:csabs:theorem/LabelledTransitionSystem-prefix-closure`

**statement:** Finite trace sets contain the empty word and are prefix closed.

**description:** Finite trace sets contain the empty word and are prefix closed.

**formalStatement:** ε∈Tr(s); uv∈Tr(s)⇒u∈Tr(s)

**assumptions:** States and actions use identity equality. State/action sets and branching may be infinite; transitions may deadlock or be nondeterministic. All actions, including a symbol called τ if present, are observable here; hiding requires a variant.

**ruleRole:** derived-result

**proofSketch:** The zero-step path witnesses ε. Truncate a path witnessing uv after |u| steps to witness u.

**dependsOn:** [labelled-steps](LabelledTransitionSystem.md#node-urn-csabs-axiom-LabelledTransitionSystem-labelled-steps); [finite-paths](LabelledTransitionSystem.md#node-urn-csabs-axiom-LabelledTransitionSystem-finite-paths)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Rob van Glabbeek: Modelling Concurrent Systems (2024), course notes](https://homepages.inf.ed.ac.uk/rvangla/MCS/notes.html); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Lecture 1, process graphs and LTSs; Lecture 2, trace semantics

**sourceNote:** Editorial derivation from the linked defining rules and operations, using the consulted source presentation; not attributed as a numbered source theorem.

**provenanceKind:** derived

<a id="node-urn-csabs-theorem-LabelledTransitionSystem-finite-path-induction"></a>

### finite-path-induction

`urn:csabs:theorem/LabelledTransitionSystem-finite-path-induction`

**statement:** Properties of labelled paths follow from zero-step and path-extension cases.

**description:** Properties of labelled paths follow from zero-step and path-extension cases.

**formalStatement:** [∀s:P(s,ε,s)] ∧ [∀s,w,t,a,u:(Path(s,w,t)∧P(s,w,t)∧t —a→ u⇒P(s,wa,u))] ⇒ ∀s,w,t:(Path(s,w,t)⇒P(s,w,t))

**assumptions:** States and actions use identity equality. State/action sets and branching may be infinite; transitions may deadlock or be nondeterministic. All actions, including a symbol called τ if present, are observable here; hiding requires a variant.; Path(s,w,t) records the start, full finite action word and endpoint; it is not an infinite path assertion.

**ruleRole:** proof-principle

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Rob van Glabbeek: Modelling Concurrent Systems (2024), course notes](https://homepages.inf.ed.ac.uk/rvangla/MCS/notes.html); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Lecture 1, process graphs and LTSs; Lecture 2, trace semantics

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** Path(s,w,t) denotes the endpoint-specific finite-path condition used in the trace definition. Induct on |w|; the base has identical endpoints, and removing the last transition supplies the shorter witness.

**dependsOn:** [labelled-steps](LabelledTransitionSystem.md#node-urn-csabs-axiom-LabelledTransitionSystem-labelled-steps); [finite-paths](LabelledTransitionSystem.md#node-urn-csabs-axiom-LabelledTransitionSystem-finite-paths); [induction-schema](NaturalNumber.md#node-urn-csabs-axiom-NaturalNumber-induction-schema)

## Concept provenance

- [Rob van Glabbeek: Modelling Concurrent Systems (2024), course notes](https://homepages.inf.ed.ac.uk/rvangla/MCS/notes.html); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Lecture 1, process graphs and LTSs; Lecture 2, trace semantics

**sourceNote:** Adapts the source process graph with one initial state to a possibly empty set of initial states. No successful-termination predicate is included.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/LabelledTransitionSystem",
    "type": "Concept",
    "shortForm": "LabelledTransitionSystem",
    "fullName": "Action-labelled transition system with initial states",
    "category": [
      "urn:csabs:category/behavior",
      "urn:csabs:category/programming-semantics",
      "urn:csabs:category/concurrent-behavior"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "definition": "States evolve through an arbitrary relation labelled by actions; a chosen initial-state set supports system-level executions.",
    "notation": "T=(S,Act,I,→); I⊆S; →⊆S×Act×S",
    "hasOperation": [
      "urn:csabs:operation/LabelledTransitionSystem-postAction",
      "urn:csabs:operation/LabelledTransitionSystem-traces"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/LabelledTransitionSystem-labelled-steps",
      "urn:csabs:axiom/LabelledTransitionSystem-finite-paths"
    ],
    "hasLaw": [
      "urn:csabs:law/LabelledTransitionSystem-post-union",
      "urn:csabs:law/LabelledTransitionSystem-trace-first-step"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/LabelledTransitionSystem-prefix-closure",
      "urn:csabs:theorem/LabelledTransitionSystem-finite-path-induction"
    ],
    "requiresConcept": [
      "urn:csabs:concept/TransitionSystem",
      "urn:csabs:concept/Relation",
      "urn:csabs:concept/Sequence"
    ],
    "relatedConcept": [
      "urn:csabs:concept/TraceEquivalence",
      "urn:csabs:concept/NFA",
      "urn:csabs:concept/Simulation",
      "urn:csabs:concept/Bisimulation"
    ],
    "coverageStatus": "basis-reviewed",
    "axiomBasis": "Selected defining presentation: The labelled next-state relation may have zero, one, or many outcomes. Finite traces are the labels of finite paths, including the zero-step path.",
    "basisKind": "defined-structure",
    "basisScope": "States and actions use identity equality. State/action sets and branching may be infinite; transitions may deadlock or be nondeterministic. All actions, including a symbol called τ if present, are observable here; hiding requires a variant.",
    "source": [
      "urn:csabs:source/vanglabbeek-mcs"
    ],
    "sourceLocator": "Lecture 1, process graphs and LTSs; Lecture 2, trace semantics",
    "sourceNote": "Adapts the source process graph with one initial state to a possibly empty set of initial states. No successful-termination predicate is included.",
    "provenanceKind": "adapted",
    "reviewStatus": "editorial review of defining basis and selected laws, theorems and proof principles; no machine-checked proof",
    "verificationObligation": [
      "States and actions use identity equality. State/action sets and branching may be infinite; transitions may deadlock or be nondeterministic. All actions, including a symbol called τ if present, are observable here; hiding requires a variant."
    ],
    "specializationOf": [
      "urn:csabs:concept/TransitionSystem"
    ],
    "specializationNote": "Forget action labels to obtain parent Next(s,t) iff ∃a∈Act:s —a→ t, with the same S and I. Parent post is the union of action-indexed post operations. No parent law is transferred implicitly.",
    "leanFormulation": "structure LabelledTransitionSystem (S : Type u) (Act : Type v) where\n  initial : _root_.Set S\n  step : S → Act → S → Prop",
    "formulationSource": "urn:csabs:source/local-lean-Graphs",
    "formulationLocator": "Catalog.LabelledTransitionSystem",
    "formulationScope": "model",
    "leanModelMapping": "Initial states and S -> Act -> S -> Prop; finite paths include empty path.",
    "leanModelLimitations": "Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.",
    "mathematicalFormulation": "An LTS is (S,Act,I,→) with I⊆S and →⊆S×Act×S. Finite traces from s are words a₁…a_n labeling a path from s; the empty word is admitted by the reflexive path."
  },
  {
    "id": "urn:csabs:operation/LabelledTransitionSystem-postAction",
    "type": "Operation",
    "name": "postAction",
    "signature": "post_a : 𝒫(S)→𝒫(S)",
    "description": "Returns states reachable in one a-labelled step.",
    "concept": "urn:csabs:concept/LabelledTransitionSystem",
    "precondition": "Arguments belong to the carriers in the signature.",
    "totality": "total mathematical operation on the stated domain",
    "postcondition": "Returns states reachable in one a-labelled step."
  },
  {
    "id": "urn:csabs:operation/LabelledTransitionSystem-traces",
    "type": "Operation",
    "name": "traces",
    "signature": "Tr : S→𝒫(Act*)",
    "description": "Returns all finite action words realizable from a state; it does not record termination or infinite behavior.",
    "concept": "urn:csabs:concept/LabelledTransitionSystem",
    "precondition": "Arguments belong to the carriers in the signature.",
    "totality": "total mathematical operation on the stated domain",
    "postcondition": "Returns all finite action words realizable from a state; it does not record termination or infinite behavior."
  },
  {
    "id": "urn:csabs:axiom/LabelledTransitionSystem-labelled-steps",
    "type": "Axiom",
    "name": "labelled-steps",
    "statement": "The labelled next-state relation may have zero, one, or many outcomes.",
    "description": "The labelled next-state relation may have zero, one, or many outcomes.",
    "formalStatement": "I⊆S; →⊆S×Act×S; post_a(X)={t:∃s∈X:s —a→ t}",
    "assumptions": [
      "States and actions use identity equality. State/action sets and branching may be infinite; transitions may deadlock or be nondeterministic. All actions, including a symbol called τ if present, are observable here; hiding requires a variant."
    ],
    "appliesTo": [
      "urn:csabs:concept/LabelledTransitionSystem"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/vanglabbeek-mcs"
    ],
    "sourceLocator": "Lecture 1, process graphs and LTSs; Lecture 2, trace semantics",
    "sourceNote": "Adapts the source process graph with one initial state to a possibly empty set of initial states. No successful-termination predicate is included. Local notation specifies the chosen defining presentation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/LabelledTransitionSystem-finite-paths",
    "type": "Axiom",
    "name": "finite-paths",
    "statement": "Finite traces are the labels of finite paths, including the zero-step path.",
    "description": "Finite traces are the labels of finite paths, including the zero-step path.",
    "formalStatement": "w∈Tr(s) iff ∃n≥0,s₀,…,sₙ: s₀=s ∧ w=a₁…aₙ ∧ ∀1≤i≤n:sᵢ₋₁ —aᵢ→ sᵢ",
    "assumptions": [
      "States and actions use identity equality. State/action sets and branching may be infinite; transitions may deadlock or be nondeterministic. All actions, including a symbol called τ if present, are observable here; hiding requires a variant."
    ],
    "appliesTo": [
      "urn:csabs:concept/LabelledTransitionSystem"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/vanglabbeek-mcs"
    ],
    "sourceLocator": "Lecture 1, process graphs and LTSs; Lecture 2, trace semantics",
    "sourceNote": "Adapts the source process graph with one initial state to a possibly empty set of initial states. No successful-termination predicate is included. Local notation specifies the chosen defining presentation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/LabelledTransitionSystem-post-union",
    "type": "Law",
    "name": "post-union",
    "statement": "Action-indexed post distributes over arbitrary unions, including the empty union.",
    "description": "Action-indexed post distributes over arbitrary unions, including the empty union.",
    "formalStatement": "post_a(⋃_{j∈J}X_j)=⋃_{j∈J}post_a(X_j); post_a(∅)=∅",
    "assumptions": [
      "States and actions use identity equality. State/action sets and branching may be infinite; transitions may deadlock or be nondeterministic. All actions, including a symbol called τ if present, are observable here; hiding requires a variant."
    ],
    "appliesTo": [
      "urn:csabs:concept/LabelledTransitionSystem"
    ],
    "ruleRole": "derived-result",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/vanglabbeek-mcs"
    ],
    "sourceLocator": "Lecture 1, process graphs and LTSs; Lecture 2, trace semantics",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "An outgoing a-step has a source in the union exactly when its source belongs to some X_j. With no sources there are no targets.",
    "dependsOn": [
      "urn:csabs:axiom/LabelledTransitionSystem-labelled-steps"
    ]
  },
  {
    "id": "urn:csabs:law/LabelledTransitionSystem-trace-first-step",
    "type": "Law",
    "name": "trace-first-step",
    "statement": "A nonempty trace decomposes into its first action and a residual trace.",
    "description": "A nonempty trace decomposes into its first action and a residual trace.",
    "formalStatement": "aw∈Tr(s) iff ∃t:(s —a→ t ∧ w∈Tr(t))",
    "assumptions": [
      "States and actions use identity equality. State/action sets and branching may be infinite; transitions may deadlock or be nondeterministic. All actions, including a symbol called τ if present, are observable here; hiding requires a variant."
    ],
    "appliesTo": [
      "urn:csabs:concept/LabelledTransitionSystem"
    ],
    "ruleRole": "derived-result",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/vanglabbeek-mcs"
    ],
    "sourceLocator": "Lecture 1, process graphs and LTSs; Lecture 2, trace semantics",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "Split off the first transition of a witnessing path; conversely prefix a residual path with that transition.",
    "dependsOn": [
      "urn:csabs:axiom/LabelledTransitionSystem-labelled-steps",
      "urn:csabs:axiom/LabelledTransitionSystem-finite-paths"
    ]
  },
  {
    "id": "urn:csabs:theorem/LabelledTransitionSystem-prefix-closure",
    "type": "Theorem",
    "name": "prefix-closure",
    "statement": "Finite trace sets contain the empty word and are prefix closed.",
    "description": "Finite trace sets contain the empty word and are prefix closed.",
    "formalStatement": "ε∈Tr(s); uv∈Tr(s)⇒u∈Tr(s)",
    "assumptions": [
      "States and actions use identity equality. State/action sets and branching may be infinite; transitions may deadlock or be nondeterministic. All actions, including a symbol called τ if present, are observable here; hiding requires a variant."
    ],
    "appliesTo": [
      "urn:csabs:concept/LabelledTransitionSystem"
    ],
    "ruleRole": "derived-result",
    "proofSketch": "The zero-step path witnesses ε. Truncate a path witnessing uv after |u| steps to witness u.",
    "dependsOn": [
      "urn:csabs:axiom/LabelledTransitionSystem-labelled-steps",
      "urn:csabs:axiom/LabelledTransitionSystem-finite-paths"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/vanglabbeek-mcs"
    ],
    "sourceLocator": "Lecture 1, process graphs and LTSs; Lecture 2, trace semantics",
    "sourceNote": "Editorial derivation from the linked defining rules and operations, using the consulted source presentation; not attributed as a numbered source theorem.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/LabelledTransitionSystem-finite-path-induction",
    "type": "Theorem",
    "name": "finite-path-induction",
    "statement": "Properties of labelled paths follow from zero-step and path-extension cases.",
    "description": "Properties of labelled paths follow from zero-step and path-extension cases.",
    "formalStatement": "[∀s:P(s,ε,s)] ∧ [∀s,w,t,a,u:(Path(s,w,t)∧P(s,w,t)∧t —a→ u⇒P(s,wa,u))] ⇒ ∀s,w,t:(Path(s,w,t)⇒P(s,w,t))",
    "assumptions": [
      "States and actions use identity equality. State/action sets and branching may be infinite; transitions may deadlock or be nondeterministic. All actions, including a symbol called τ if present, are observable here; hiding requires a variant.",
      "Path(s,w,t) records the start, full finite action word and endpoint; it is not an infinite path assertion."
    ],
    "appliesTo": [
      "urn:csabs:concept/LabelledTransitionSystem"
    ],
    "ruleRole": "proof-principle",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/vanglabbeek-mcs"
    ],
    "sourceLocator": "Lecture 1, process graphs and LTSs; Lecture 2, trace semantics",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "Path(s,w,t) denotes the endpoint-specific finite-path condition used in the trace definition. Induct on |w|; the base has identical endpoints, and removing the last transition supplies the shorter witness.",
    "dependsOn": [
      "urn:csabs:axiom/LabelledTransitionSystem-labelled-steps",
      "urn:csabs:axiom/LabelledTransitionSystem-finite-paths",
      "urn:csabs:axiom/NaturalNumber-induction-schema"
    ]
  }
]
```
<!-- graph-record:end -->
