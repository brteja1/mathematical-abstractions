# Relational method contract with write effects

A receiver-and-argument method specification separating a precondition, normal/exceptional outcomes and a prestate-indexed set of permitted writes.

**Notation:** K=(P,Q,W); input i=(receiver,args)∈I; σ:Loc→Val; o∈Outcome=Return(R)⊎Throw(E); τ=(σ′,o,writes); Q:State×I×State×Outcome→Prop; W:State×I→𝒫(Loc)

**Stable ID:** `urn:csabs:concept/MethodContract`

**Categories:** Programming-language semantics → Object-oriented semantics

**Kind:** semantic-model

**Prerequisites:** [Hoare Triple](HoareTriple.md), [Binary relation](Relation.md)

**Related concepts:** [Sequential object heap with reference identity](ObjectHeap.md), [Visible-state object invariant protocol](ObjectInvariant.md), [Behavioral subtyping with explicit history constraints](BehavioralSubtyping.md)

## Backlinks

- [Behavioral subtyping with explicit history constraints](BehavioralSubtyping.md) — `requiresConcept`
- [Exclusive finite-heap separation predicates](HeapSeparation.md) — `relatedConcept`
- [Visible-state object invariant protocol](ObjectInvariant.md) — `relatedConcept`

## Mathematical formulation

A contract is (Pre,Post,Writable). For state s,input i and trace (s′,o,W), allows ⇔ Pre(s,i)∧Post(s,i,s′,o)∧W⊆Writable(s,i)∧∀l∉W,s′(l)=s(l). Execution satisfaction quantifies over all traces from Pre; a separate covered predicate requires some allowed trace for each admissible input.

**Lean formulation** (in its source module context):

```lean
structure MethodContract (L : Type u) (V : Type v) (I : Type w) (O : Type x) where
  pre : Store L V → I → Prop
  post : Store L V → I → Store L V → O → Prop
  writable : Store L V → I → Set L
```

**Source:** [`Catalog.OOP.MethodContract`](../lean/Catalog/ObjectOrientation.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Pre/post/writable predicates over fixed-domain total stores; trace after-state, outcome and all writes; allows, satisfies and covered match the selected relational profile. Instantiate Outcome with Sum Result Exception.

**Limits:** Allocation, faults outside the outcome carrier, execution instrumentation correctness and termination are not modeled. Preconditions may be empty and coverage is separate.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Selected defining rules: allows(K,σ,i,(σ′,o,w)) ⇔ P(σ,i) ∧ Q(σ,i,σ′,o) ∧ w⊆W(σ,i) ∧ (∀l∉w, σ′(l)=σ(l)). satisfies(Exec,K) ⇔ ∀σ,i,τ, P(σ,i) ∧ τ∈Exec(σ,i) ⇒ allows(K,σ,i,τ). No terminating trace is required. covered(K) ⇔ ∀σ,i, P(σ,i) ⇒ ∃τ, allows(K,σ,i,τ). Preconditions and required input domains must be checked separately for nonvacuity.

**basisKind:** extensional-structural-definition

**basisScope:** Sequential partial correctness over a fixed location universe Loc and total stores σ. Invocation input retains its prestate receiver/arguments. Allocation/deallocation and local stack variables are outside this fixed-domain profile; a heap model needs an explicit lifting. Each terminating trace records every write, including assignments that restore or retain the old value; read footprints are unconstrained. Q separately specifies exceptional outcomes. Divergence, faults outside Outcome, termination and existence of outcomes require separate obligations. Contract equality is extensional in P,Q,W.

**verificationObligation:** Instantiate carriers, equality, definedness and the stated semantic profile before using these records.; Catalog validation checks structure, not source entailment or target implementation conformance.

**reviewStatus:** Editorial source and interface review; Lean model bindings and individual proof witnesses are separate.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-MethodContract-allows"></a>

### allows

`urn:csabs:operation/MethodContract-allows`

**signature:** allows : K×State×I×Trace→Prop

**description:** allows(K,σ,i,(σ′,o,w)) iff P(σ,i) ∧ Q(σ,i,σ′,o) ∧ w⊆W(σ,i) ∧ ∀l∉w, σ′(l)=σ(l).

**precondition:** Typed inputs in the stated semantic profile.

**postcondition:** allows(K,σ,i,(σ′,o,w)) iff P(σ,i) ∧ Q(σ,i,σ′,o) ∧ w⊆W(σ,i) ∧ ∀l∉w, σ′(l)=σ(l).

**totality:** Total mathematical operation.

**source:** [OpenJML tutorial: Postconditions](https://www.openjml.org/tutorial/Postconditions); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference; [OpenJML tutorial: Specifying Exceptions](https://www.openjml.org/tutorial/SpecifyingExceptions); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference; [OpenJML tutorial: Frame Conditions](https://www.openjml.org/tutorial/FrameConditions); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** OpenJML Postconditions, requires/ensures and result; Specifying Exceptions, signals/signals_only; Frame Conditions, permitted writes and pre-state evaluation

**sourceNote:** A language-independent relational adaptation, not a JML parser or full semantics. Records write events so unchanged final values alone cannot discharge an assignable clause.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-MethodContract-satisfies"></a>

### satisfies

`urn:csabs:operation/MethodContract-satisfies`

**signature:** satisfies : Exec×K→Prop

**description:** Every terminating trace in Exec(σ,i) satisfies allows(K,σ,i,τ) whenever P(σ,i); calls outside P are unconstrained. Exec must record every actual write.

**precondition:** Typed inputs in the stated semantic profile.

**postcondition:** Every terminating trace in Exec(σ,i) satisfies allows(K,σ,i,τ) whenever P(σ,i); calls outside P are unconstrained. Exec must record every actual write.

**totality:** Total mathematical operation.

**source:** [OpenJML tutorial: Postconditions](https://www.openjml.org/tutorial/Postconditions); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference; [OpenJML tutorial: Specifying Exceptions](https://www.openjml.org/tutorial/SpecifyingExceptions); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference; [OpenJML tutorial: Frame Conditions](https://www.openjml.org/tutorial/FrameConditions); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** OpenJML Postconditions, requires/ensures and result; Specifying Exceptions, signals/signals_only; Frame Conditions, permitted writes and pre-state evaluation

**sourceNote:** A language-independent relational adaptation, not a JML parser or full semantics. Records write events so unchanged final values alone cannot discharge an assignable clause.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-MethodContract-input-coverage"></a>

### input-coverage

`urn:csabs:operation/MethodContract-input-coverage`

**signature:** covered : K→Prop

**description:** covered(K) iff ∀σ,i, P(σ,i) ⇒ ∃τ, allows(K,σ,i,τ); this is outcome feasibility, not actual implementation termination.

**precondition:** Typed inputs in the stated semantic profile.

**postcondition:** covered(K) iff ∀σ,i, P(σ,i) ⇒ ∃τ, allows(K,σ,i,τ); this is outcome feasibility, not actual implementation termination.

**totality:** Total mathematical operation.

**source:** [OpenJML tutorial: Postconditions](https://www.openjml.org/tutorial/Postconditions); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference; [OpenJML tutorial: Specifying Exceptions](https://www.openjml.org/tutorial/SpecifyingExceptions); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference; [OpenJML tutorial: Frame Conditions](https://www.openjml.org/tutorial/FrameConditions); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** OpenJML Postconditions, requires/ensures and result; Specifying Exceptions, signals/signals_only; Frame Conditions, permitted writes and pre-state evaluation

**sourceNote:** A language-independent relational adaptation, not a JML parser or full semantics. Records write events so unchanged final values alone cannot discharge an assignable clause.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-MethodContract-outcome-and-effect"></a>

### outcome-and-effect

`urn:csabs:axiom/MethodContract-outcome-and-effect`

**statement:** allows(K,σ,i,(σ′,o,w)) ⇔ P(σ,i) ∧ Q(σ,i,σ′,o) ∧ w⊆W(σ,i) ∧ (∀l∉w, σ′(l)=σ(l)).

**formalStatement:** allows(K,σ,i,(σ′,o,w)) ⇔ P(σ,i) ∧ Q(σ,i,σ′,o) ∧ w⊆W(σ,i) ∧ (∀l∉w, σ′(l)=σ(l)).

**assumptions:** Sequential partial correctness over a fixed location universe Loc and total stores σ. Invocation input retains its prestate receiver/arguments. Allocation/deallocation and local stack variables are outside this fixed-domain profile; a heap model needs an explicit lifting. Each terminating trace records every write, including assignments that restore or retain the old value; read footprints are unconstrained. Q separately specifies exceptional outcomes. Divergence, faults outside Outcome, termination and existence of outcomes require separate obligations. Contract equality is extensional in P,Q,W.; Variables have the carriers declared in the notation and operation signatures.

**reviewStatus:** Editorial mathematical statement; no compiled witness asserted by this record.

**notationLanguage:** informal mathematical Unicode

**source:** [OpenJML tutorial: Postconditions](https://www.openjml.org/tutorial/Postconditions); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference; [OpenJML tutorial: Specifying Exceptions](https://www.openjml.org/tutorial/SpecifyingExceptions); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference; [OpenJML tutorial: Frame Conditions](https://www.openjml.org/tutorial/FrameConditions); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** OpenJML Postconditions, requires/ensures and result; Specifying Exceptions, signals/signals_only; Frame Conditions, permitted writes and pre-state evaluation

**sourceNote:** A language-independent relational adaptation, not a JML parser or full semantics. Records write events so unchanged final values alone cannot discharge an assignable clause.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-MethodContract-partial-satisfaction"></a>

### partial-satisfaction

`urn:csabs:axiom/MethodContract-partial-satisfaction`

**statement:** satisfies(Exec,K) ⇔ ∀σ,i,τ, P(σ,i) ∧ τ∈Exec(σ,i) ⇒ allows(K,σ,i,τ). No terminating trace is required.

**formalStatement:** satisfies(Exec,K) ⇔ ∀σ,i,τ, P(σ,i) ∧ τ∈Exec(σ,i) ⇒ allows(K,σ,i,τ). No terminating trace is required.

**assumptions:** Sequential partial correctness over a fixed location universe Loc and total stores σ. Invocation input retains its prestate receiver/arguments. Allocation/deallocation and local stack variables are outside this fixed-domain profile; a heap model needs an explicit lifting. Each terminating trace records every write, including assignments that restore or retain the old value; read footprints are unconstrained. Q separately specifies exceptional outcomes. Divergence, faults outside Outcome, termination and existence of outcomes require separate obligations. Contract equality is extensional in P,Q,W.; Variables have the carriers declared in the notation and operation signatures.

**reviewStatus:** Editorial mathematical statement; no compiled witness asserted by this record.

**notationLanguage:** informal mathematical Unicode

**source:** [OpenJML tutorial: Postconditions](https://www.openjml.org/tutorial/Postconditions); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference; [OpenJML tutorial: Specifying Exceptions](https://www.openjml.org/tutorial/SpecifyingExceptions); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference; [OpenJML tutorial: Frame Conditions](https://www.openjml.org/tutorial/FrameConditions); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** OpenJML Postconditions, requires/ensures and result; Specifying Exceptions, signals/signals_only; Frame Conditions, permitted writes and pre-state evaluation

**sourceNote:** A language-independent relational adaptation, not a JML parser or full semantics. Records write events so unchanged final values alone cannot discharge an assignable clause.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-MethodContract-outcome-coverage"></a>

### outcome-coverage

`urn:csabs:axiom/MethodContract-outcome-coverage`

**statement:** covered(K) ⇔ ∀σ,i, P(σ,i) ⇒ ∃τ, allows(K,σ,i,τ). Preconditions and required input domains must be checked separately for nonvacuity.

**formalStatement:** covered(K) ⇔ ∀σ,i, P(σ,i) ⇒ ∃τ, allows(K,σ,i,τ). Preconditions and required input domains must be checked separately for nonvacuity.

**assumptions:** Sequential partial correctness over a fixed location universe Loc and total stores σ. Invocation input retains its prestate receiver/arguments. Allocation/deallocation and local stack variables are outside this fixed-domain profile; a heap model needs an explicit lifting. Each terminating trace records every write, including assignments that restore or retain the old value; read footprints are unconstrained. Q separately specifies exceptional outcomes. Divergence, faults outside Outcome, termination and existence of outcomes require separate obligations. Contract equality is extensional in P,Q,W.; Variables have the carriers declared in the notation and operation signatures.

**reviewStatus:** Editorial mathematical statement; no compiled witness asserted by this record.

**notationLanguage:** informal mathematical Unicode

**source:** [OpenJML tutorial: Postconditions](https://www.openjml.org/tutorial/Postconditions); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference; [OpenJML tutorial: Specifying Exceptions](https://www.openjml.org/tutorial/SpecifyingExceptions); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference; [OpenJML tutorial: Frame Conditions](https://www.openjml.org/tutorial/FrameConditions); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** OpenJML Postconditions, requires/ensures and result; Specifying Exceptions, signals/signals_only; Frame Conditions, permitted writes and pre-state evaluation

**sourceNote:** A language-independent relational adaptation, not a JML parser or full semantics. Records write events so unchanged final values alone cannot discharge an assignable clause.

**provenanceKind:** adapted

**ruleRole:** defining-rule

## Laws

<a id="node-urn-csabs-law-MethodContract-frame-observation"></a>

### frame-observation

`urn:csabs:law/MethodContract-frame-observation`

**statement:** allows(K,σ,i,(σ′,o,w)) ∧ l∉W(σ,i) ⇒ σ′(l)=σ(l).

**formalStatement:** allows(K,σ,i,(σ′,o,w)) ∧ l∉W(σ,i) ⇒ σ′(l)=σ(l).

**assumptions:** Sequential partial correctness over a fixed location universe Loc and total stores σ. Invocation input retains its prestate receiver/arguments. Allocation/deallocation and local stack variables are outside this fixed-domain profile; a heap model needs an explicit lifting. Each terminating trace records every write, including assignments that restore or retain the old value; read footprints are unconstrained. Q separately specifies exceptional outcomes. Divergence, faults outside Outcome, termination and existence of outcomes require separate obligations. Contract equality is extensional in P,Q,W.; Variables have the carriers declared in the notation and operation signatures.

**reviewStatus:** Editorial mathematical statement; no compiled witness asserted by this record.

**notationLanguage:** informal mathematical Unicode

**source:** [OpenJML tutorial: Postconditions](https://www.openjml.org/tutorial/Postconditions); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference; [OpenJML tutorial: Specifying Exceptions](https://www.openjml.org/tutorial/SpecifyingExceptions); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference; [OpenJML tutorial: Frame Conditions](https://www.openjml.org/tutorial/FrameConditions); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** OpenJML Postconditions, requires/ensures and result; Specifying Exceptions, signals/signals_only; Frame Conditions, permitted writes and pre-state evaluation

**sourceNote:** Catalog derivation from the linked premises in this explicitly scoped model; the cited source supplies the underlying definitions. This is not a claim of executable proof.

**provenanceKind:** derived

**dependsOn:** [outcome-and-effect](MethodContract.md#node-urn-csabs-axiom-MethodContract-outcome-and-effect)

**proofSketch:** Since w is a subset of W, l outside W is outside w; apply the no-write observation equation. The converse need not hold for write events.

<a id="node-urn-csabs-law-MethodContract-empty-execution-vacuity"></a>

### empty-execution-vacuity

`urn:csabs:law/MethodContract-empty-execution-vacuity`

**statement:** (∀σ,i, Exec(σ,i)=∅) ⇒ satisfies(Exec,K), even if covered(K) is false.

**formalStatement:** (∀σ,i, Exec(σ,i)=∅) ⇒ satisfies(Exec,K), even if covered(K) is false.

**assumptions:** Sequential partial correctness over a fixed location universe Loc and total stores σ. Invocation input retains its prestate receiver/arguments. Allocation/deallocation and local stack variables are outside this fixed-domain profile; a heap model needs an explicit lifting. Each terminating trace records every write, including assignments that restore or retain the old value; read footprints are unconstrained. Q separately specifies exceptional outcomes. Divergence, faults outside Outcome, termination and existence of outcomes require separate obligations. Contract equality is extensional in P,Q,W.; Variables have the carriers declared in the notation and operation signatures.

**reviewStatus:** Editorial mathematical statement; no compiled witness asserted by this record.

**notationLanguage:** informal mathematical Unicode

**source:** [OpenJML tutorial: Postconditions](https://www.openjml.org/tutorial/Postconditions); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference; [OpenJML tutorial: Specifying Exceptions](https://www.openjml.org/tutorial/SpecifyingExceptions); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference; [OpenJML tutorial: Frame Conditions](https://www.openjml.org/tutorial/FrameConditions); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** OpenJML Postconditions, requires/ensures and result; Specifying Exceptions, signals/signals_only; Frame Conditions, permitted writes and pre-state evaluation

**sourceNote:** Catalog derivation from the linked premises in this explicitly scoped model; the cited source supplies the underlying definitions. This is not a claim of executable proof.

**provenanceKind:** derived

**dependsOn:** [partial-satisfaction](MethodContract.md#node-urn-csabs-axiom-MethodContract-partial-satisfaction); [outcome-coverage](MethodContract.md#node-urn-csabs-axiom-MethodContract-outcome-coverage)

**proofSketch:** The satisfaction implication has no execution witnesses. Coverage independently quantifies possible permitted traces, so it does not follow from vacuous satisfaction.

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [OpenJML tutorial: Postconditions](https://www.openjml.org/tutorial/Postconditions); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference
- [OpenJML tutorial: Specifying Exceptions](https://www.openjml.org/tutorial/SpecifyingExceptions); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference
- [OpenJML tutorial: Frame Conditions](https://www.openjml.org/tutorial/FrameConditions); accessedOn: 2026-11-10; sourceRole: consulted-definition-and-semantics-reference

**sourceLocator:** OpenJML Postconditions, requires/ensures and result; Specifying Exceptions, signals/signals_only; Frame Conditions, permitted writes and pre-state evaluation

**sourceNote:** A language-independent relational adaptation, not a JML parser or full semantics. Records write events so unchanged final values alone cannot discharge an assignable clause.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/MethodContract",
    "type": "Concept",
    "shortForm": "MethodContract",
    "fullName": "Relational method contract with write effects",
    "category": [
      "urn:csabs:category/object-oriented-semantics"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "definition": "A receiver-and-argument method specification separating a precondition, normal/exceptional outcomes and a prestate-indexed set of permitted writes.",
    "notation": "K=(P,Q,W); input i=(receiver,args)∈I; σ:Loc→Val; o∈Outcome=Return(R)⊎Throw(E); τ=(σ′,o,writes); Q:State×I×State×Outcome→Prop; W:State×I→𝒫(Loc)",
    "requiresConcept": [
      "urn:csabs:concept/HoareTriple",
      "urn:csabs:concept/Relation"
    ],
    "relatedConcept": [
      "urn:csabs:concept/ObjectHeap",
      "urn:csabs:concept/ObjectInvariant",
      "urn:csabs:concept/BehavioralSubtyping"
    ],
    "hasOperation": [
      "urn:csabs:operation/MethodContract-allows",
      "urn:csabs:operation/MethodContract-satisfies",
      "urn:csabs:operation/MethodContract-input-coverage"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/MethodContract-outcome-and-effect",
      "urn:csabs:axiom/MethodContract-partial-satisfaction",
      "urn:csabs:axiom/MethodContract-outcome-coverage"
    ],
    "hasLaw": [
      "urn:csabs:law/MethodContract-frame-observation",
      "urn:csabs:law/MethodContract-empty-execution-vacuity"
    ],
    "hasTheorem": [],
    "basisKind": "extensional-structural-definition",
    "basisScope": "Sequential partial correctness over a fixed location universe Loc and total stores σ. Invocation input retains its prestate receiver/arguments. Allocation/deallocation and local stack variables are outside this fixed-domain profile; a heap model needs an explicit lifting. Each terminating trace records every write, including assignments that restore or retain the old value; read footprints are unconstrained. Q separately specifies exceptional outcomes. Divergence, faults outside Outcome, termination and existence of outcomes require separate obligations. Contract equality is extensional in P,Q,W.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source and interface review; Lean model bindings and individual proof witnesses are separate.",
    "verificationObligation": [
      "Instantiate carriers, equality, definedness and the stated semantic profile before using these records.",
      "Catalog validation checks structure, not source entailment or target implementation conformance."
    ],
    "source": [
      "urn:csabs:source/oop-jml-postconditions",
      "urn:csabs:source/oop-jml-exceptions",
      "urn:csabs:source/oop-jml-frames"
    ],
    "sourceLocator": "OpenJML Postconditions, requires/ensures and result; Specifying Exceptions, signals/signals_only; Frame Conditions, permitted writes and pre-state evaluation",
    "sourceNote": "A language-independent relational adaptation, not a JML parser or full semantics. Records write events so unchanged final values alone cannot discharge an assignable clause.",
    "provenanceKind": "adapted",
    "axiomBasis": "Selected defining rules: allows(K,σ,i,(σ′,o,w)) ⇔ P(σ,i) ∧ Q(σ,i,σ′,o) ∧ w⊆W(σ,i) ∧ (∀l∉w, σ′(l)=σ(l)). satisfies(Exec,K) ⇔ ∀σ,i,τ, P(σ,i) ∧ τ∈Exec(σ,i) ⇒ allows(K,σ,i,τ). No terminating trace is required. covered(K) ⇔ ∀σ,i, P(σ,i) ⇒ ∃τ, allows(K,σ,i,τ). Preconditions and required input domains must be checked separately for nonvacuity.",
    "leanFormulation": "structure MethodContract (L : Type u) (V : Type v) (I : Type w) (O : Type x) where\n  pre : Store L V → I → Prop\n  post : Store L V → I → Store L V → O → Prop\n  writable : Store L V → I → Set L",
    "formulationSource": "urn:csabs:source/local-lean-ObjectOrientation",
    "formulationLocator": "Catalog.OOP.MethodContract",
    "formulationScope": "model",
    "leanModelMapping": "Pre/post/writable predicates over fixed-domain total stores; trace after-state, outcome and all writes; allows, satisfies and covered match the selected relational profile. Instantiate Outcome with Sum Result Exception.",
    "leanModelLimitations": "Allocation, faults outside the outcome carrier, execution instrumentation correctness and termination are not modeled. Preconditions may be empty and coverage is separate.",
    "mathematicalFormulation": "A contract is (Pre,Post,Writable). For state s,input i and trace (s′,o,W), allows ⇔ Pre(s,i)∧Post(s,i,s′,o)∧W⊆Writable(s,i)∧∀l∉W,s′(l)=s(l). Execution satisfaction quantifies over all traces from Pre; a separate covered predicate requires some allowed trace for each admissible input."
  },
  {
    "id": "urn:csabs:operation/MethodContract-allows",
    "type": "Operation",
    "name": "allows",
    "signature": "allows : K×State×I×Trace→Prop",
    "description": "allows(K,σ,i,(σ′,o,w)) iff P(σ,i) ∧ Q(σ,i,σ′,o) ∧ w⊆W(σ,i) ∧ ∀l∉w, σ′(l)=σ(l).",
    "concept": "urn:csabs:concept/MethodContract",
    "precondition": "Typed inputs in the stated semantic profile.",
    "postcondition": "allows(K,σ,i,(σ′,o,w)) iff P(σ,i) ∧ Q(σ,i,σ′,o) ∧ w⊆W(σ,i) ∧ ∀l∉w, σ′(l)=σ(l).",
    "totality": "Total mathematical operation.",
    "source": [
      "urn:csabs:source/oop-jml-postconditions",
      "urn:csabs:source/oop-jml-exceptions",
      "urn:csabs:source/oop-jml-frames"
    ],
    "sourceLocator": "OpenJML Postconditions, requires/ensures and result; Specifying Exceptions, signals/signals_only; Frame Conditions, permitted writes and pre-state evaluation",
    "sourceNote": "A language-independent relational adaptation, not a JML parser or full semantics. Records write events so unchanged final values alone cannot discharge an assignable clause.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/MethodContract-satisfies",
    "type": "Operation",
    "name": "satisfies",
    "signature": "satisfies : Exec×K→Prop",
    "description": "Every terminating trace in Exec(σ,i) satisfies allows(K,σ,i,τ) whenever P(σ,i); calls outside P are unconstrained. Exec must record every actual write.",
    "concept": "urn:csabs:concept/MethodContract",
    "precondition": "Typed inputs in the stated semantic profile.",
    "postcondition": "Every terminating trace in Exec(σ,i) satisfies allows(K,σ,i,τ) whenever P(σ,i); calls outside P are unconstrained. Exec must record every actual write.",
    "totality": "Total mathematical operation.",
    "source": [
      "urn:csabs:source/oop-jml-postconditions",
      "urn:csabs:source/oop-jml-exceptions",
      "urn:csabs:source/oop-jml-frames"
    ],
    "sourceLocator": "OpenJML Postconditions, requires/ensures and result; Specifying Exceptions, signals/signals_only; Frame Conditions, permitted writes and pre-state evaluation",
    "sourceNote": "A language-independent relational adaptation, not a JML parser or full semantics. Records write events so unchanged final values alone cannot discharge an assignable clause.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/MethodContract-input-coverage",
    "type": "Operation",
    "name": "input-coverage",
    "signature": "covered : K→Prop",
    "description": "covered(K) iff ∀σ,i, P(σ,i) ⇒ ∃τ, allows(K,σ,i,τ); this is outcome feasibility, not actual implementation termination.",
    "concept": "urn:csabs:concept/MethodContract",
    "precondition": "Typed inputs in the stated semantic profile.",
    "postcondition": "covered(K) iff ∀σ,i, P(σ,i) ⇒ ∃τ, allows(K,σ,i,τ); this is outcome feasibility, not actual implementation termination.",
    "totality": "Total mathematical operation.",
    "source": [
      "urn:csabs:source/oop-jml-postconditions",
      "urn:csabs:source/oop-jml-exceptions",
      "urn:csabs:source/oop-jml-frames"
    ],
    "sourceLocator": "OpenJML Postconditions, requires/ensures and result; Specifying Exceptions, signals/signals_only; Frame Conditions, permitted writes and pre-state evaluation",
    "sourceNote": "A language-independent relational adaptation, not a JML parser or full semantics. Records write events so unchanged final values alone cannot discharge an assignable clause.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/MethodContract-outcome-and-effect",
    "type": "Axiom",
    "name": "outcome-and-effect",
    "statement": "allows(K,σ,i,(σ′,o,w)) ⇔ P(σ,i) ∧ Q(σ,i,σ′,o) ∧ w⊆W(σ,i) ∧ (∀l∉w, σ′(l)=σ(l)).",
    "formalStatement": "allows(K,σ,i,(σ′,o,w)) ⇔ P(σ,i) ∧ Q(σ,i,σ′,o) ∧ w⊆W(σ,i) ∧ (∀l∉w, σ′(l)=σ(l)).",
    "assumptions": [
      "Sequential partial correctness over a fixed location universe Loc and total stores σ. Invocation input retains its prestate receiver/arguments. Allocation/deallocation and local stack variables are outside this fixed-domain profile; a heap model needs an explicit lifting. Each terminating trace records every write, including assignments that restore or retain the old value; read footprints are unconstrained. Q separately specifies exceptional outcomes. Divergence, faults outside Outcome, termination and existence of outcomes require separate obligations. Contract equality is extensional in P,Q,W.",
      "Variables have the carriers declared in the notation and operation signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/MethodContract"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled witness asserted by this record.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/oop-jml-postconditions",
      "urn:csabs:source/oop-jml-exceptions",
      "urn:csabs:source/oop-jml-frames"
    ],
    "sourceLocator": "OpenJML Postconditions, requires/ensures and result; Specifying Exceptions, signals/signals_only; Frame Conditions, permitted writes and pre-state evaluation",
    "sourceNote": "A language-independent relational adaptation, not a JML parser or full semantics. Records write events so unchanged final values alone cannot discharge an assignable clause.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/MethodContract-partial-satisfaction",
    "type": "Axiom",
    "name": "partial-satisfaction",
    "statement": "satisfies(Exec,K) ⇔ ∀σ,i,τ, P(σ,i) ∧ τ∈Exec(σ,i) ⇒ allows(K,σ,i,τ). No terminating trace is required.",
    "formalStatement": "satisfies(Exec,K) ⇔ ∀σ,i,τ, P(σ,i) ∧ τ∈Exec(σ,i) ⇒ allows(K,σ,i,τ). No terminating trace is required.",
    "assumptions": [
      "Sequential partial correctness over a fixed location universe Loc and total stores σ. Invocation input retains its prestate receiver/arguments. Allocation/deallocation and local stack variables are outside this fixed-domain profile; a heap model needs an explicit lifting. Each terminating trace records every write, including assignments that restore or retain the old value; read footprints are unconstrained. Q separately specifies exceptional outcomes. Divergence, faults outside Outcome, termination and existence of outcomes require separate obligations. Contract equality is extensional in P,Q,W.",
      "Variables have the carriers declared in the notation and operation signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/MethodContract"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled witness asserted by this record.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/oop-jml-postconditions",
      "urn:csabs:source/oop-jml-exceptions",
      "urn:csabs:source/oop-jml-frames"
    ],
    "sourceLocator": "OpenJML Postconditions, requires/ensures and result; Specifying Exceptions, signals/signals_only; Frame Conditions, permitted writes and pre-state evaluation",
    "sourceNote": "A language-independent relational adaptation, not a JML parser or full semantics. Records write events so unchanged final values alone cannot discharge an assignable clause.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/MethodContract-outcome-coverage",
    "type": "Axiom",
    "name": "outcome-coverage",
    "statement": "covered(K) ⇔ ∀σ,i, P(σ,i) ⇒ ∃τ, allows(K,σ,i,τ). Preconditions and required input domains must be checked separately for nonvacuity.",
    "formalStatement": "covered(K) ⇔ ∀σ,i, P(σ,i) ⇒ ∃τ, allows(K,σ,i,τ). Preconditions and required input domains must be checked separately for nonvacuity.",
    "assumptions": [
      "Sequential partial correctness over a fixed location universe Loc and total stores σ. Invocation input retains its prestate receiver/arguments. Allocation/deallocation and local stack variables are outside this fixed-domain profile; a heap model needs an explicit lifting. Each terminating trace records every write, including assignments that restore or retain the old value; read footprints are unconstrained. Q separately specifies exceptional outcomes. Divergence, faults outside Outcome, termination and existence of outcomes require separate obligations. Contract equality is extensional in P,Q,W.",
      "Variables have the carriers declared in the notation and operation signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/MethodContract"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled witness asserted by this record.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/oop-jml-postconditions",
      "urn:csabs:source/oop-jml-exceptions",
      "urn:csabs:source/oop-jml-frames"
    ],
    "sourceLocator": "OpenJML Postconditions, requires/ensures and result; Specifying Exceptions, signals/signals_only; Frame Conditions, permitted writes and pre-state evaluation",
    "sourceNote": "A language-independent relational adaptation, not a JML parser or full semantics. Records write events so unchanged final values alone cannot discharge an assignable clause.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:law/MethodContract-frame-observation",
    "type": "Law",
    "name": "frame-observation",
    "statement": "allows(K,σ,i,(σ′,o,w)) ∧ l∉W(σ,i) ⇒ σ′(l)=σ(l).",
    "formalStatement": "allows(K,σ,i,(σ′,o,w)) ∧ l∉W(σ,i) ⇒ σ′(l)=σ(l).",
    "assumptions": [
      "Sequential partial correctness over a fixed location universe Loc and total stores σ. Invocation input retains its prestate receiver/arguments. Allocation/deallocation and local stack variables are outside this fixed-domain profile; a heap model needs an explicit lifting. Each terminating trace records every write, including assignments that restore or retain the old value; read footprints are unconstrained. Q separately specifies exceptional outcomes. Divergence, faults outside Outcome, termination and existence of outcomes require separate obligations. Contract equality is extensional in P,Q,W.",
      "Variables have the carriers declared in the notation and operation signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/MethodContract"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled witness asserted by this record.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/oop-jml-postconditions",
      "urn:csabs:source/oop-jml-exceptions",
      "urn:csabs:source/oop-jml-frames"
    ],
    "sourceLocator": "OpenJML Postconditions, requires/ensures and result; Specifying Exceptions, signals/signals_only; Frame Conditions, permitted writes and pre-state evaluation",
    "sourceNote": "Catalog derivation from the linked premises in this explicitly scoped model; the cited source supplies the underlying definitions. This is not a claim of executable proof.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/MethodContract-outcome-and-effect"
    ],
    "proofSketch": "Since w is a subset of W, l outside W is outside w; apply the no-write observation equation. The converse need not hold for write events."
  },
  {
    "id": "urn:csabs:law/MethodContract-empty-execution-vacuity",
    "type": "Law",
    "name": "empty-execution-vacuity",
    "statement": "(∀σ,i, Exec(σ,i)=∅) ⇒ satisfies(Exec,K), even if covered(K) is false.",
    "formalStatement": "(∀σ,i, Exec(σ,i)=∅) ⇒ satisfies(Exec,K), even if covered(K) is false.",
    "assumptions": [
      "Sequential partial correctness over a fixed location universe Loc and total stores σ. Invocation input retains its prestate receiver/arguments. Allocation/deallocation and local stack variables are outside this fixed-domain profile; a heap model needs an explicit lifting. Each terminating trace records every write, including assignments that restore or retain the old value; read footprints are unconstrained. Q separately specifies exceptional outcomes. Divergence, faults outside Outcome, termination and existence of outcomes require separate obligations. Contract equality is extensional in P,Q,W.",
      "Variables have the carriers declared in the notation and operation signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/MethodContract"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled witness asserted by this record.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/oop-jml-postconditions",
      "urn:csabs:source/oop-jml-exceptions",
      "urn:csabs:source/oop-jml-frames"
    ],
    "sourceLocator": "OpenJML Postconditions, requires/ensures and result; Specifying Exceptions, signals/signals_only; Frame Conditions, permitted writes and pre-state evaluation",
    "sourceNote": "Catalog derivation from the linked premises in this explicitly scoped model; the cited source supplies the underlying definitions. This is not a claim of executable proof.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/MethodContract-partial-satisfaction",
      "urn:csabs:axiom/MethodContract-outcome-coverage"
    ],
    "proofSketch": "The satisfaction implication has no execution witnesses. Coverage independently quantifies possible permitted traces, so it does not follow from vacuous satisfaction."
  }
]
```
<!-- graph-record:end -->
