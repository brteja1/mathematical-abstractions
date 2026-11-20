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

A transition system is (S,I,→) with I⊆S and →⊆S×S. reachable(s) ⇔ ∃i∈I,i→\*s, where →\* is reflexive-transitive closure. Initial states and transition successors may be absent. Utility profile: enabled(s) iff ∃t,next(s,t); counts stuttering self-loops as transitions.; terminal(s) iff ¬enabled(s), without adding implicit stuttering.; goal(G,s) iff s∈G, an external designated predicate independent of enabledness.; deadlock(G,s) iff terminal(s) and s∉G; this chosen goal-relative convention distinguishes successful termination.; ∀i<|xs|,Q(xs[i])⇒∃j<i,P(xs[j]); strict earlier occurrence; Q at index zero violates precedence. Empty and Q-free traces satisfy it vacuously. Apply to valid finite state paths separately; no fairness or infinite-time claim.

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

**axiomBasis:** Selected presentation: States, initial states, and a transition relation describe allowed executions. Governing rules: A transition system has initial states and an arbitrary next-state relation; determinism and totality are additional properties. Reachable states are the least set containing the initial states and closed under Next. Utility definitions are recorded separately; optional bottom, subtype and goal-relative conventions are conditional and do not strengthen the base carrier.

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

<a id="node-urn-csabs-operation-TransitionSystem-enabled"></a>

### enabled

`urn:csabs:operation/TransitionSystem-enabled`

**signature:** enabled : S→Prop

**description:** enabled(s) iff ∃t,next(s,t); counts stuttering self-loops as transitions.

**precondition:** Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.

**postcondition:** enabled(s) iff ∃t,next(s,t); counts stuttering self-loops as transitions.

**totality:** Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.

**sourceLocator:** Logic/Relation.lean: terminal-state closure equality; constructed enabled/terminal/goal/deadlock and indexed finite-state-trace predicates

**sourceNote:** Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-TransitionSystem-terminal"></a>

### terminal

`urn:csabs:operation/TransitionSystem-terminal`

**signature:** terminal : S→Prop

**description:** terminal(s) iff ¬enabled(s), without adding implicit stuttering.

**precondition:** Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.

**postcondition:** terminal(s) iff ¬enabled(s), without adding implicit stuttering.

**totality:** Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.

**sourceLocator:** Logic/Relation.lean: terminal-state closure equality; constructed enabled/terminal/goal/deadlock and indexed finite-state-trace predicates

**sourceNote:** Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-TransitionSystem-goal"></a>

### goal

`urn:csabs:operation/TransitionSystem-goal`

**signature:** goal : Set(S)×S→Prop

**description:** goal(G,s) iff s∈G, an external designated predicate independent of enabledness.

**precondition:** Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.

**postcondition:** goal(G,s) iff s∈G, an external designated predicate independent of enabledness.

**totality:** Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.

**sourceLocator:** Logic/Relation.lean: terminal-state closure equality; constructed enabled/terminal/goal/deadlock and indexed finite-state-trace predicates

**sourceNote:** Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-TransitionSystem-deadlock"></a>

### deadlock

`urn:csabs:operation/TransitionSystem-deadlock`

**signature:** deadlock : Set(S)×S→Prop

**description:** deadlock(G,s) iff terminal(s) and s∉G; this chosen goal-relative convention distinguishes successful termination.

**precondition:** Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.

**postcondition:** deadlock(G,s) iff terminal(s) and s∉G; this chosen goal-relative convention distinguishes successful termination.

**totality:** Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.

**sourceLocator:** Logic/Relation.lean: terminal-state closure equality; constructed enabled/terminal/goal/deadlock and indexed finite-state-trace predicates

**sourceNote:** Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-TransitionSystem-finite-trace-precedence"></a>

### finite-trace-precedence

`urn:csabs:operation/TransitionSystem-finite-trace-precedence`

**signature:** precedes : (S→Prop)²×Seq(S)→Prop

**description:** ∀i<|xs|,Q(xs[i])⇒∃j<i,P(xs[j]); strict earlier occurrence; Q at index zero violates precedence. Empty and Q-free traces satisfy it vacuously. Apply to valid finite state paths separately; no fairness or infinite-time claim.

**precondition:** Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.

**postcondition:** ∀i<|xs|,Q(xs[i])⇒∃j<i,P(xs[j]); strict earlier occurrence; Q at index zero violates precedence. Empty and Q-free traces satisfy it vacuously. Apply to valid finite state paths separately; no fairness or infinite-time claim.

**totality:** Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.

**sourceLocator:** Logic/Relation.lean: terminal-state closure equality; constructed enabled/terminal/goal/deadlock and indexed finite-state-trace predicates

**sourceNote:** Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.

**provenanceKind:** adapted

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

<a id="node-urn-csabs-axiom-TransitionSystem-utility-profile"></a>

### Explicit utility operation definitions

`urn:csabs:axiom/TransitionSystem-utility-profile`

**statement:** enabled(s) iff ∃t,next(s,t); counts stuttering self-loops as transitions.; terminal(s) iff ¬enabled(s), without adding implicit stuttering.; goal(G,s) iff s∈G, an external designated predicate independent of enabledness.; deadlock(G,s) iff terminal(s) and s∉G; this chosen goal-relative convention distinguishes successful termination.; ∀i<|xs|,Q(xs[i])⇒∃j<i,P(xs[j]); strict earlier occurrence; Q at index zero violates precedence. Empty and Q-free traces satisfy it vacuously. Apply to valid finite state paths separately; no fairness or infinite-time claim.

**formalStatement:** enabled : S→Prop: enabled(s) iff ∃t,next(s,t); counts stuttering self-loops as transitions.; terminal : S→Prop: terminal(s) iff ¬enabled(s), without adding implicit stuttering.; goal : Set(S)×S→Prop: goal(G,s) iff s∈G, an external designated predicate independent of enabledness.; deadlock : Set(S)×S→Prop: deadlock(G,s) iff terminal(s) and s∉G; this chosen goal-relative convention distinguishes successful termination.; precedes : (S→Prop)²×Seq(S)→Prop: ∀i<|xs|,Q(xs[i])⇒∃j<i,P(xs[j]); strict earlier occurrence; Q at index zero violates precedence. Empty and Q-free traces satisfy it vacuously. Apply to valid finite state paths separately; no fairness or infinite-time claim.

**assumptions:** Base concept conventions remain unchanged. Optional profiles apply only under their explicitly stated additional hypotheses; identity equality, finite inputs and exact mathematics.

**ruleRole:** defining-rule

**reviewStatus:** Definitions of a selected extension, not new foundational axioms; individual model and result witnesses are separate.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.

**sourceLocator:** Logic/Relation.lean: terminal-state closure equality; constructed enabled/terminal/goal/deadlock and indexed finite-state-trace predicates

**sourceNote:** Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.

**provenanceKind:** adapted

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
      "urn:csabs:operation/TransitionSystem-post",
      "urn:csabs:operation/TransitionSystem-enabled",
      "urn:csabs:operation/TransitionSystem-terminal",
      "urn:csabs:operation/TransitionSystem-goal",
      "urn:csabs:operation/TransitionSystem-deadlock",
      "urn:csabs:operation/TransitionSystem-finite-trace-precedence"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/TransitionSystem-state-model",
      "urn:csabs:axiom/TransitionSystem-reachability",
      "urn:csabs:axiom/TransitionSystem-utility-profile"
    ],
    "hasLaw": [
      "urn:csabs:law/TransitionSystem-core"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/TransitionSystem-reachability-induction",
      "urn:csabs:theorem/TransitionSystem-terminal-enabled-equivalence",
      "urn:csabs:theorem/TransitionSystem-strict-precedence-initial"
    ],
    "requiresConcept": [
      "urn:csabs:concept/Relation"
    ],
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Instantiate carrier, equality, and stated semantic conventions before using this entry.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: States, initial states, and a transition relation describe allowed executions. Governing rules: A transition system has initial states and an arbitrary next-state relation; determinism and totality are additional properties. Reachable states are the least set containing the initial states and closed under Next. Utility definitions are recorded separately; optional bottom, subtype and goal-relative conventions are conditional and do not strengthen the base carrier.",
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
    "mathematicalFormulation": "A transition system is (S,I,→) with I⊆S and →⊆S×S. reachable(s) ⇔ ∃i∈I,i→*s, where →* is reflexive-transitive closure. Initial states and transition successors may be absent. Utility profile: enabled(s) iff ∃t,next(s,t); counts stuttering self-loops as transitions.; terminal(s) iff ¬enabled(s), without adding implicit stuttering.; goal(G,s) iff s∈G, an external designated predicate independent of enabledness.; deadlock(G,s) iff terminal(s) and s∉G; this chosen goal-relative convention distinguishes successful termination.; ∀i<|xs|,Q(xs[i])⇒∃j<i,P(xs[j]); strict earlier occurrence; Q at index zero violates precedence. Empty and Q-free traces satisfy it vacuously. Apply to valid finite state paths separately; no fairness or infinite-time claim."
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
    "id": "urn:csabs:operation/TransitionSystem-enabled",
    "type": "Operation",
    "concept": "urn:csabs:concept/TransitionSystem",
    "name": "enabled",
    "signature": "enabled : S→Prop",
    "description": "enabled(s) iff ∃t,next(s,t); counts stuttering self-loops as transitions.",
    "precondition": "Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.",
    "postcondition": "enabled(s) iff ∃t,next(s,t); counts stuttering self-loops as transitions.",
    "totality": "Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned"
    ],
    "sourceLocator": "Logic/Relation.lean: terminal-state closure equality; constructed enabled/terminal/goal/deadlock and indexed finite-state-trace predicates",
    "sourceNote": "Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/TransitionSystem-terminal",
    "type": "Operation",
    "concept": "urn:csabs:concept/TransitionSystem",
    "name": "terminal",
    "signature": "terminal : S→Prop",
    "description": "terminal(s) iff ¬enabled(s), without adding implicit stuttering.",
    "precondition": "Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.",
    "postcondition": "terminal(s) iff ¬enabled(s), without adding implicit stuttering.",
    "totality": "Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned"
    ],
    "sourceLocator": "Logic/Relation.lean: terminal-state closure equality; constructed enabled/terminal/goal/deadlock and indexed finite-state-trace predicates",
    "sourceNote": "Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/TransitionSystem-goal",
    "type": "Operation",
    "concept": "urn:csabs:concept/TransitionSystem",
    "name": "goal",
    "signature": "goal : Set(S)×S→Prop",
    "description": "goal(G,s) iff s∈G, an external designated predicate independent of enabledness.",
    "precondition": "Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.",
    "postcondition": "goal(G,s) iff s∈G, an external designated predicate independent of enabledness.",
    "totality": "Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned"
    ],
    "sourceLocator": "Logic/Relation.lean: terminal-state closure equality; constructed enabled/terminal/goal/deadlock and indexed finite-state-trace predicates",
    "sourceNote": "Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/TransitionSystem-deadlock",
    "type": "Operation",
    "concept": "urn:csabs:concept/TransitionSystem",
    "name": "deadlock",
    "signature": "deadlock : Set(S)×S→Prop",
    "description": "deadlock(G,s) iff terminal(s) and s∉G; this chosen goal-relative convention distinguishes successful termination.",
    "precondition": "Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.",
    "postcondition": "deadlock(G,s) iff terminal(s) and s∉G; this chosen goal-relative convention distinguishes successful termination.",
    "totality": "Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned"
    ],
    "sourceLocator": "Logic/Relation.lean: terminal-state closure equality; constructed enabled/terminal/goal/deadlock and indexed finite-state-trace predicates",
    "sourceNote": "Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/TransitionSystem-finite-trace-precedence",
    "type": "Operation",
    "concept": "urn:csabs:concept/TransitionSystem",
    "name": "finite-trace-precedence",
    "signature": "precedes : (S→Prop)²×Seq(S)→Prop",
    "description": "∀i<|xs|,Q(xs[i])⇒∃j<i,P(xs[j]); strict earlier occurrence; Q at index zero violates precedence. Empty and Q-free traces satisfy it vacuously. Apply to valid finite state paths separately; no fairness or infinite-time claim.",
    "precondition": "Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.",
    "postcondition": "∀i<|xs|,Q(xs[i])⇒∃j<i,P(xs[j]); strict earlier occurrence; Q at index zero violates precedence. Empty and Q-free traces satisfy it vacuously. Apply to valid finite state paths separately; no fairness or infinite-time claim.",
    "totality": "Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned"
    ],
    "sourceLocator": "Logic/Relation.lean: terminal-state closure equality; constructed enabled/terminal/goal/deadlock and indexed finite-state-trace predicates",
    "sourceNote": "Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.",
    "provenanceKind": "adapted"
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
    "id": "urn:csabs:axiom/TransitionSystem-utility-profile",
    "type": "Axiom",
    "name": "Explicit utility operation definitions",
    "statement": "enabled(s) iff ∃t,next(s,t); counts stuttering self-loops as transitions.; terminal(s) iff ¬enabled(s), without adding implicit stuttering.; goal(G,s) iff s∈G, an external designated predicate independent of enabledness.; deadlock(G,s) iff terminal(s) and s∉G; this chosen goal-relative convention distinguishes successful termination.; ∀i<|xs|,Q(xs[i])⇒∃j<i,P(xs[j]); strict earlier occurrence; Q at index zero violates precedence. Empty and Q-free traces satisfy it vacuously. Apply to valid finite state paths separately; no fairness or infinite-time claim.",
    "formalStatement": "enabled : S→Prop: enabled(s) iff ∃t,next(s,t); counts stuttering self-loops as transitions.; terminal : S→Prop: terminal(s) iff ¬enabled(s), without adding implicit stuttering.; goal : Set(S)×S→Prop: goal(G,s) iff s∈G, an external designated predicate independent of enabledness.; deadlock : Set(S)×S→Prop: deadlock(G,s) iff terminal(s) and s∉G; this chosen goal-relative convention distinguishes successful termination.; precedes : (S→Prop)²×Seq(S)→Prop: ∀i<|xs|,Q(xs[i])⇒∃j<i,P(xs[j]); strict earlier occurrence; Q at index zero violates precedence. Empty and Q-free traces satisfy it vacuously. Apply to valid finite state paths separately; no fairness or infinite-time claim.",
    "assumptions": [
      "Base concept conventions remain unchanged. Optional profiles apply only under their explicitly stated additional hypotheses; identity equality, finite inputs and exact mathematics."
    ],
    "appliesTo": [
      "urn:csabs:concept/TransitionSystem"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Definitions of a selected extension, not new foundational axioms; individual model and result witnesses are separate.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned"
    ],
    "sourceLocator": "Logic/Relation.lean: terminal-state closure equality; constructed enabled/terminal/goal/deadlock and indexed finite-state-trace predicates",
    "sourceNote": "Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.",
    "provenanceKind": "adapted"
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
