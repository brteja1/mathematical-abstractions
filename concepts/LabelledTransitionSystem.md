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

- [Asymmetric coroutine with explicit resume/yield lifecycle](AsymmetricCoroutine.md) — `requiresConcept`
- [Asymmetric coroutine with explicit resume/yield lifecycle](AsymmetricCoroutine.md) — `specializationOf`
- [Single-thread cooperative scheduler with explicit waiting](CooperativeScheduler.md) — `requiresConcept`
- [Single-thread cooperative scheduler with explicit waiting](CooperativeScheduler.md) — `specializationOf`
- [Lamport bakery lock protocol](LamportBakery.md) — `requiresConcept`
- [Lock with compatible access modes](Lock.md) — `requiresConcept`
- [Mealy deterministic finite sequential transducer](MealyTransducer.md) — `relatedConcept`
- [Moore deterministic finite sequential transducer](MooreTransducer.md) — `relatedConcept`
- [Nondeterministic finite automaton without epsilon moves](NFA.md) — `requiresConcept`
- [Nondeterministic finite automaton without epsilon moves](NFA.md) — `specializationOf`
- [Strong finite partial-trace equivalence](TraceEquivalence.md) — `requiresConcept`
- [Transition System](TransitionSystem.md) — `relatedConcept`

## Mathematical formulation

An LTS is (S,Act,I,→) with I⊆S and →⊆S×Act×S. Finite traces from s are words a₁…a\_n labeling a path from s; the empty word is admitted by the reflexive path. Utility profile: enabled(s,a) iff ∃t,s —a→ t; enabledAny(s) iff ∃a,t,s —a→ t.; No outgoing labelled transition: ¬∃a,t,s —a→ t; internal labels count unless explicitly hidden by a separate model.; Membership in a designated goal set, independent of termination.; No outgoing labelled step and not in the designated goal set; no implicit stutter.; For a valid finite state path (initial state included), every Q-state has a strictly earlier P-state. State predicate, not a predicate on label words alone; empty and Q-free lists satisfy it vacuously.

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

**axiomBasis:** Selected defining presentation: The labelled next-state relation may have zero, one, or many outcomes. Finite traces are the labels of finite paths, including the zero-step path. Utility definitions are recorded separately; optional bottom, subtype and goal-relative conventions are conditional and do not strengthen the base carrier.

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

<a id="node-urn-csabs-operation-LabelledTransitionSystem-enabled-label"></a>

### enabled-label

`urn:csabs:operation/LabelledTransitionSystem-enabled-label`

**signature:** enabled : S×Label→Prop

**description:** enabled(s,a) iff ∃t,s —a→ t; enabledAny(s) iff ∃a,t,s —a→ t.

**precondition:** Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.

**postcondition:** enabled(s,a) iff ∃t,s —a→ t; enabledAny(s) iff ∃a,t,s —a→ t.

**totality:** Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.

**sourceLocator:** Logic/Relation.lean: terminal-state closure equality; constructed predicates for the erased labelled-step relation and finite-state traces

**sourceNote:** Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-LabelledTransitionSystem-terminal"></a>

### terminal

`urn:csabs:operation/LabelledTransitionSystem-terminal`

**signature:** terminal : S→Prop

**description:** No outgoing labelled transition: ¬∃a,t,s —a→ t; internal labels count unless explicitly hidden by a separate model.

**precondition:** Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.

**postcondition:** No outgoing labelled transition: ¬∃a,t,s —a→ t; internal labels count unless explicitly hidden by a separate model.

**totality:** Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.

**sourceLocator:** Logic/Relation.lean: terminal-state closure equality; constructed predicates for the erased labelled-step relation and finite-state traces

**sourceNote:** Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-LabelledTransitionSystem-goal"></a>

### goal

`urn:csabs:operation/LabelledTransitionSystem-goal`

**signature:** goal : Set(S)×S→Prop

**description:** Membership in a designated goal set, independent of termination.

**precondition:** Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.

**postcondition:** Membership in a designated goal set, independent of termination.

**totality:** Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.

**sourceLocator:** Logic/Relation.lean: terminal-state closure equality; constructed predicates for the erased labelled-step relation and finite-state traces

**sourceNote:** Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-LabelledTransitionSystem-deadlock"></a>

### deadlock

`urn:csabs:operation/LabelledTransitionSystem-deadlock`

**signature:** deadlock : Set(S)×S→Prop

**description:** No outgoing labelled step and not in the designated goal set; no implicit stutter.

**precondition:** Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.

**postcondition:** No outgoing labelled step and not in the designated goal set; no implicit stutter.

**totality:** Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.

**sourceLocator:** Logic/Relation.lean: terminal-state closure equality; constructed predicates for the erased labelled-step relation and finite-state traces

**sourceNote:** Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-LabelledTransitionSystem-finite-trace-precedence"></a>

### finite-trace-precedence

`urn:csabs:operation/LabelledTransitionSystem-finite-trace-precedence`

**signature:** precedes : (S→Prop)²×Seq(S)→Prop

**description:** For a valid finite state path (initial state included), every Q-state has a strictly earlier P-state. State predicate, not a predicate on label words alone; empty and Q-free lists satisfy it vacuously.

**precondition:** Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.

**postcondition:** For a valid finite state path (initial state included), every Q-state has a strictly earlier P-state. State predicate, not a predicate on label words alone; empty and Q-free lists satisfy it vacuously.

**totality:** Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.

**sourceLocator:** Logic/Relation.lean: terminal-state closure equality; constructed predicates for the erased labelled-step relation and finite-state traces

**sourceNote:** Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.

**provenanceKind:** adapted

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

<a id="node-urn-csabs-axiom-LabelledTransitionSystem-utility-profile"></a>

### Explicit utility operation definitions

`urn:csabs:axiom/LabelledTransitionSystem-utility-profile`

**statement:** enabled(s,a) iff ∃t,s —a→ t; enabledAny(s) iff ∃a,t,s —a→ t.; No outgoing labelled transition: ¬∃a,t,s —a→ t; internal labels count unless explicitly hidden by a separate model.; Membership in a designated goal set, independent of termination.; No outgoing labelled step and not in the designated goal set; no implicit stutter.; For a valid finite state path (initial state included), every Q-state has a strictly earlier P-state. State predicate, not a predicate on label words alone; empty and Q-free lists satisfy it vacuously.

**formalStatement:** enabled : S×Label→Prop: enabled(s,a) iff ∃t,s —a→ t; enabledAny(s) iff ∃a,t,s —a→ t.; terminal : S→Prop: No outgoing labelled transition: ¬∃a,t,s —a→ t; internal labels count unless explicitly hidden by a separate model.; goal : Set(S)×S→Prop: Membership in a designated goal set, independent of termination.; deadlock : Set(S)×S→Prop: No outgoing labelled step and not in the designated goal set; no implicit stutter.; precedes : (S→Prop)²×Seq(S)→Prop: For a valid finite state path (initial state included), every Q-state has a strictly earlier P-state. State predicate, not a predicate on label words alone; empty and Q-free lists satisfy it vacuously.

**assumptions:** Base concept conventions remain unchanged. Optional profiles apply only under their explicitly stated additional hypotheses; identity equality, finite inputs and exact mathematics.

**ruleRole:** defining-rule

**reviewStatus:** Definitions of a selected extension, not new foundational axioms; individual model and result witnesses are separate.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.

**sourceLocator:** Logic/Relation.lean: terminal-state closure equality; constructed predicates for the erased labelled-step relation and finite-state traces

**sourceNote:** Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.

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

<a id="node-urn-csabs-theorem-TransitionSystem-terminal-enabled-equivalence"></a>

### terminal-enabled-equivalence

`urn:csabs:theorem/TransitionSystem-terminal-enabled-equivalence`

**statement:** terminal(s) iff no outgoing successor exists; for an LTS use next(s,t) iff ∃label,step(s,label,t).

**formalStatement:** terminal(s) iff no outgoing successor exists; for an LTS use next(s,t) iff ∃label,step(s,label,t).

**proofSketch:** Unfold the terminal predicate; labelled enabledness is obtained by existential label erasure.

**assumptions:** Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles.

**dependsOn:** [Explicit utility operation definitions](TransitionSystem.md#node-urn-csabs-axiom-TransitionSystem-utility-profile); [Explicit utility operation definitions](LabelledTransitionSystem.md#node-urn-csabs-axiom-LabelledTransitionSystem-utility-profile)

**reviewStatus:** Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.; Catalog ReachabilityUtilities Lean formulations and proofs; path: lean/Catalog/ReachabilityUtilities.lean; accessedOn: 2026-11-20; sourceRole: Local formulation and derived-proof evidence. Independent mathematical provenance is linked separately.

**sourceLocator:** Logic/Relation.lean: terminal-state closure equality; constructed enabled/terminal/goal/deadlock and indexed finite-state-trace predicates; Catalog.terminal_enabled

**sourceNote:** Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.

**provenanceKind:** derived

#### Mathematical formulation

terminal(s) iff no outgoing successor exists; for an LTS use next(s,t) iff ∃label,step(s,label,t).

**Lean formulation** (in its source module context):

```lean
∀ {S : Type u} (next : S → S → Prop) (s : S), Catalog.terminal next s ↔ ¬ ∃ t, next s t
```

**Source:** [`Catalog.terminal_enabled`](../lean/Catalog/ReachabilityUtilities.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** terminal(s) iff no outgoing successor exists; for an LTS use next(s,t) iff ∃label,step(s,label,t). Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.

**Limits:** Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/LabelledTransitionSystem-utility-profile": "The same mathematical predicate is shared with this concept; the state-step relation or phrase-hit predicate is explicitly instantiated.",
  "urn:csabs:axiom/TransitionSystem-utility-profile": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders."
}
```

<a id="node-urn-csabs-theorem-TransitionSystem-strict-precedence-initial"></a>

### strict-precedence-initial

`urn:csabs:theorem/TransitionSystem-strict-precedence-initial`

**statement:** If every Q-state in a finite state trace has a strictly earlier P-state, the first state cannot satisfy Q.

**formalStatement:** If every Q-state in a finite state trace has a strictly earlier P-state, the first state cannot satisfy Q.

**proofSketch:** Index zero has no smaller natural-number index. Valid path and goal conditions are separate explicit predicates.

**assumptions:** Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles.

**dependsOn:** [Explicit utility operation definitions](TransitionSystem.md#node-urn-csabs-axiom-TransitionSystem-utility-profile); [Explicit utility operation definitions](LabelledTransitionSystem.md#node-urn-csabs-axiom-LabelledTransitionSystem-utility-profile)

**reviewStatus:** Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.; Catalog ReachabilityUtilities Lean formulations and proofs; path: lean/Catalog/ReachabilityUtilities.lean; accessedOn: 2026-11-20; sourceRole: Local formulation and derived-proof evidence. Independent mathematical provenance is linked separately.

**sourceLocator:** Logic/Relation.lean: terminal-state closure equality; constructed enabled/terminal/goal/deadlock and indexed finite-state-trace predicates; Catalog.tracePrecedes_initial

**sourceNote:** Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.

**provenanceKind:** derived

#### Mathematical formulation

If every Q-state in a finite state trace has a strictly earlier P-state, the first state cannot satisfy Q.

**Lean formulation** (in its source module context):

```lean
∀ {S : Type u} (p q : S → Prop) (a : S) (xs : List S)
    (_h : Catalog.tracePrecedes p q (a :: xs)), ¬ q a
```

**Source:** [`Catalog.tracePrecedes_initial`](../lean/Catalog/ReachabilityUtilities.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** If every Q-state in a finite state trace has a strictly earlier P-state, the first state cannot satisfy Q. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.

**Limits:** Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/LabelledTransitionSystem-utility-profile": "The same mathematical predicate is shared with this concept; the state-step relation or phrase-hit predicate is explicitly instantiated.",
  "urn:csabs:axiom/TransitionSystem-utility-profile": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders."
}
```

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
      "urn:csabs:operation/LabelledTransitionSystem-traces",
      "urn:csabs:operation/LabelledTransitionSystem-enabled-label",
      "urn:csabs:operation/LabelledTransitionSystem-terminal",
      "urn:csabs:operation/LabelledTransitionSystem-goal",
      "urn:csabs:operation/LabelledTransitionSystem-deadlock",
      "urn:csabs:operation/LabelledTransitionSystem-finite-trace-precedence"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/LabelledTransitionSystem-labelled-steps",
      "urn:csabs:axiom/LabelledTransitionSystem-finite-paths",
      "urn:csabs:axiom/LabelledTransitionSystem-utility-profile"
    ],
    "hasLaw": [
      "urn:csabs:law/LabelledTransitionSystem-post-union",
      "urn:csabs:law/LabelledTransitionSystem-trace-first-step"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/LabelledTransitionSystem-prefix-closure",
      "urn:csabs:theorem/LabelledTransitionSystem-finite-path-induction",
      "urn:csabs:theorem/TransitionSystem-terminal-enabled-equivalence",
      "urn:csabs:theorem/TransitionSystem-strict-precedence-initial"
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
    "axiomBasis": "Selected defining presentation: The labelled next-state relation may have zero, one, or many outcomes. Finite traces are the labels of finite paths, including the zero-step path. Utility definitions are recorded separately; optional bottom, subtype and goal-relative conventions are conditional and do not strengthen the base carrier.",
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
    "mathematicalFormulation": "An LTS is (S,Act,I,→) with I⊆S and →⊆S×Act×S. Finite traces from s are words a₁…a_n labeling a path from s; the empty word is admitted by the reflexive path. Utility profile: enabled(s,a) iff ∃t,s —a→ t; enabledAny(s) iff ∃a,t,s —a→ t.; No outgoing labelled transition: ¬∃a,t,s —a→ t; internal labels count unless explicitly hidden by a separate model.; Membership in a designated goal set, independent of termination.; No outgoing labelled step and not in the designated goal set; no implicit stutter.; For a valid finite state path (initial state included), every Q-state has a strictly earlier P-state. State predicate, not a predicate on label words alone; empty and Q-free lists satisfy it vacuously."
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
    "id": "urn:csabs:operation/LabelledTransitionSystem-enabled-label",
    "type": "Operation",
    "concept": "urn:csabs:concept/LabelledTransitionSystem",
    "name": "enabled-label",
    "signature": "enabled : S×Label→Prop",
    "description": "enabled(s,a) iff ∃t,s —a→ t; enabledAny(s) iff ∃a,t,s —a→ t.",
    "precondition": "Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.",
    "postcondition": "enabled(s,a) iff ∃t,s —a→ t; enabledAny(s) iff ∃a,t,s —a→ t.",
    "totality": "Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned"
    ],
    "sourceLocator": "Logic/Relation.lean: terminal-state closure equality; constructed predicates for the erased labelled-step relation and finite-state traces",
    "sourceNote": "Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/LabelledTransitionSystem-terminal",
    "type": "Operation",
    "concept": "urn:csabs:concept/LabelledTransitionSystem",
    "name": "terminal",
    "signature": "terminal : S→Prop",
    "description": "No outgoing labelled transition: ¬∃a,t,s —a→ t; internal labels count unless explicitly hidden by a separate model.",
    "precondition": "Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.",
    "postcondition": "No outgoing labelled transition: ¬∃a,t,s —a→ t; internal labels count unless explicitly hidden by a separate model.",
    "totality": "Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned"
    ],
    "sourceLocator": "Logic/Relation.lean: terminal-state closure equality; constructed predicates for the erased labelled-step relation and finite-state traces",
    "sourceNote": "Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/LabelledTransitionSystem-goal",
    "type": "Operation",
    "concept": "urn:csabs:concept/LabelledTransitionSystem",
    "name": "goal",
    "signature": "goal : Set(S)×S→Prop",
    "description": "Membership in a designated goal set, independent of termination.",
    "precondition": "Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.",
    "postcondition": "Membership in a designated goal set, independent of termination.",
    "totality": "Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned"
    ],
    "sourceLocator": "Logic/Relation.lean: terminal-state closure equality; constructed predicates for the erased labelled-step relation and finite-state traces",
    "sourceNote": "Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/LabelledTransitionSystem-deadlock",
    "type": "Operation",
    "concept": "urn:csabs:concept/LabelledTransitionSystem",
    "name": "deadlock",
    "signature": "deadlock : Set(S)×S→Prop",
    "description": "No outgoing labelled step and not in the designated goal set; no implicit stutter.",
    "precondition": "Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.",
    "postcondition": "No outgoing labelled step and not in the designated goal set; no implicit stutter.",
    "totality": "Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned"
    ],
    "sourceLocator": "Logic/Relation.lean: terminal-state closure equality; constructed predicates for the erased labelled-step relation and finite-state traces",
    "sourceNote": "Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/LabelledTransitionSystem-finite-trace-precedence",
    "type": "Operation",
    "concept": "urn:csabs:concept/LabelledTransitionSystem",
    "name": "finite-trace-precedence",
    "signature": "precedes : (S→Prop)²×Seq(S)→Prop",
    "description": "For a valid finite state path (initial state included), every Q-state has a strictly earlier P-state. State predicate, not a predicate on label words alone; empty and Q-free lists satisfy it vacuously.",
    "precondition": "Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.",
    "postcondition": "For a valid finite state path (initial state included), every Q-state has a strictly earlier P-state. State predicate, not a predicate on label words alone; empty and Q-free lists satisfy it vacuously.",
    "totality": "Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned"
    ],
    "sourceLocator": "Logic/Relation.lean: terminal-state closure equality; constructed predicates for the erased labelled-step relation and finite-state traces",
    "sourceNote": "Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.",
    "provenanceKind": "adapted"
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
    "id": "urn:csabs:axiom/LabelledTransitionSystem-utility-profile",
    "type": "Axiom",
    "name": "Explicit utility operation definitions",
    "statement": "enabled(s,a) iff ∃t,s —a→ t; enabledAny(s) iff ∃a,t,s —a→ t.; No outgoing labelled transition: ¬∃a,t,s —a→ t; internal labels count unless explicitly hidden by a separate model.; Membership in a designated goal set, independent of termination.; No outgoing labelled step and not in the designated goal set; no implicit stutter.; For a valid finite state path (initial state included), every Q-state has a strictly earlier P-state. State predicate, not a predicate on label words alone; empty and Q-free lists satisfy it vacuously.",
    "formalStatement": "enabled : S×Label→Prop: enabled(s,a) iff ∃t,s —a→ t; enabledAny(s) iff ∃a,t,s —a→ t.; terminal : S→Prop: No outgoing labelled transition: ¬∃a,t,s —a→ t; internal labels count unless explicitly hidden by a separate model.; goal : Set(S)×S→Prop: Membership in a designated goal set, independent of termination.; deadlock : Set(S)×S→Prop: No outgoing labelled step and not in the designated goal set; no implicit stutter.; precedes : (S→Prop)²×Seq(S)→Prop: For a valid finite state path (initial state included), every Q-state has a strictly earlier P-state. State predicate, not a predicate on label words alone; empty and Q-free lists satisfy it vacuously.",
    "assumptions": [
      "Base concept conventions remain unchanged. Optional profiles apply only under their explicitly stated additional hypotheses; identity equality, finite inputs and exact mathematics."
    ],
    "appliesTo": [
      "urn:csabs:concept/LabelledTransitionSystem"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Definitions of a selected extension, not new foundational axioms; individual model and result witnesses are separate.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned"
    ],
    "sourceLocator": "Logic/Relation.lean: terminal-state closure equality; constructed predicates for the erased labelled-step relation and finite-state traces",
    "sourceNote": "Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.",
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
  },
  {
    "id": "urn:csabs:theorem/TransitionSystem-terminal-enabled-equivalence",
    "type": "Theorem",
    "name": "terminal-enabled-equivalence",
    "statement": "terminal(s) iff no outgoing successor exists; for an LTS use next(s,t) iff ∃label,step(s,label,t).",
    "formalStatement": "terminal(s) iff no outgoing successor exists; for an LTS use next(s,t) iff ∃label,step(s,label,t).",
    "mathematicalFormulation": "terminal(s) iff no outgoing successor exists; for an LTS use next(s,t) iff ∃label,step(s,label,t).",
    "proofSketch": "Unfold the terminal predicate; labelled enabledness is obtained by existential label erasure.",
    "assumptions": [
      "Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles."
    ],
    "appliesTo": [
      "urn:csabs:concept/TransitionSystem",
      "urn:csabs:concept/LabelledTransitionSystem"
    ],
    "dependsOn": [
      "urn:csabs:axiom/TransitionSystem-utility-profile",
      "urn:csabs:axiom/LabelledTransitionSystem-utility-profile"
    ],
    "reviewStatus": "Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned",
      "urn:csabs:source/utility-lean-ReachabilityUtilities"
    ],
    "sourceLocator": "Logic/Relation.lean: terminal-state closure equality; constructed enabled/terminal/goal/deadlock and indexed finite-state-trace predicates; Catalog.terminal_enabled",
    "sourceNote": "Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {S : Type u} (next : S → S → Prop) (s : S), Catalog.terminal next s ↔ ¬ ∃ t, next s t",
    "leanModelMapping": "terminal(s) iff no outgoing successor exists; for an LTS use next(s,t) iff ∃label,step(s,label,t). Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.",
    "leanModelLimitations": "Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/LabelledTransitionSystem-utility-profile\": \"The same mathematical predicate is shared with this concept; the state-step relation or phrase-hit predicate is explicitly instantiated.\", \"urn:csabs:axiom/TransitionSystem-utility-profile\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\"}",
    "formulationScope": "registered-witness-type",
    "formulationSource": "urn:csabs:source/utility-lean-ReachabilityUtilities",
    "formulationLocator": "Catalog.terminal_enabled"
  },
  {
    "id": "urn:csabs:theorem/TransitionSystem-strict-precedence-initial",
    "type": "Theorem",
    "name": "strict-precedence-initial",
    "statement": "If every Q-state in a finite state trace has a strictly earlier P-state, the first state cannot satisfy Q.",
    "formalStatement": "If every Q-state in a finite state trace has a strictly earlier P-state, the first state cannot satisfy Q.",
    "mathematicalFormulation": "If every Q-state in a finite state trace has a strictly earlier P-state, the first state cannot satisfy Q.",
    "proofSketch": "Index zero has no smaller natural-number index. Valid path and goal conditions are separate explicit predicates.",
    "assumptions": [
      "Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles."
    ],
    "appliesTo": [
      "urn:csabs:concept/TransitionSystem",
      "urn:csabs:concept/LabelledTransitionSystem"
    ],
    "dependsOn": [
      "urn:csabs:axiom/TransitionSystem-utility-profile",
      "urn:csabs:axiom/LabelledTransitionSystem-utility-profile"
    ],
    "reviewStatus": "Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned",
      "urn:csabs:source/utility-lean-ReachabilityUtilities"
    ],
    "sourceLocator": "Logic/Relation.lean: terminal-state closure equality; constructed enabled/terminal/goal/deadlock and indexed finite-state-trace predicates; Catalog.tracePrecedes_initial",
    "sourceNote": "Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {S : Type u} (p q : S → Prop) (a : S) (xs : List S)\n    (_h : Catalog.tracePrecedes p q (a :: xs)), ¬ q a",
    "leanModelMapping": "If every Q-state in a finite state trace has a strictly earlier P-state, the first state cannot satisfy Q. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.",
    "leanModelLimitations": "Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/LabelledTransitionSystem-utility-profile\": \"The same mathematical predicate is shared with this concept; the state-step relation or phrase-hit predicate is explicitly instantiated.\", \"urn:csabs:axiom/TransitionSystem-utility-profile\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\"}",
    "formulationScope": "registered-witness-type",
    "formulationSource": "urn:csabs:source/utility-lean-ReachabilityUtilities",
    "formulationLocator": "Catalog.tracePrecedes_initial"
  }
]
```
<!-- graph-record:end -->
