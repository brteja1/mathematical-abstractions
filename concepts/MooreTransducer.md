# Moore deterministic finite sequential transducer

A deterministic finite-state input/output machine with total next-state and output maps; outputs are attached to states and include the initial state output.

**Notation:** (Q,I,O,q₀,δ,λ); δ:Q×I→Q; λ:Q→O

**Stable ID:** `urn:csabs:concept/MooreTransducer`

**Categories:** Behavior and transition systems

**Kind:** semantic-model

**Prerequisites:** [Finite sequence (List datatype)](Sequence.md), [Total function](Function.md)

**Related concepts:** [Deterministic finite automaton with total transition](DFA.md), [Action-labelled transition system with initial states](LabelledTransitionSystem.md), [Mealy deterministic finite sequential transducer](MealyTransducer.md)

## Backlinks

- [Mealy deterministic finite sequential transducer](MealyTransducer.md) — `relatedConcept`

## Mathematical formulation

For q₀,q₁,…,qₙ with qᵢ₊₁=δ(qᵢ,aᵢ), return final qₙ and [λ(q₀),…,λ(qₙ)].

**Lean formulation** (in its source module context):

```lean
structure MooreTransducer (Q I O : Type) [Fintype Q] [Fintype I] [Fintype O] where
  initial : Q
  next : Q → I → Q
  emit : Q → O
```

**Source:** [`Catalog.MooreTransducer`](../lean/Catalog/ReleaseSequenceModels.lean); consulted 2026-11-20.

**Scope:** model

**Interpretation:** For q₀,q₁,…,qₙ with qᵢ₊₁=δ(qᵢ,aᵢ), return final qₙ and [λ(q₀),…,λ(qₙ)].

**Limits:** Q,I,O are finite exact-equality sets; q₀∈Q makes Q nonempty. I may be empty. O is nonempty because λ:Q→O. Input words are finite, including ε; run from any q, default q₀. Pure deterministic total steps, unbounded word length, no ε-input transitions, nondeterminism, time, effects or accepting states. A run on n inputs has n+1 outputs; a convention suppressing the initial output needs an explicit mapping. Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Typed total δ and λ with a designated initial state. Word execution is primitive recursion: run(q,ε)=(q,[λ(q)]); run(q,a·xs) emits λ(q) then executes xs from δ(q,a).

**basisKind:** defined-structure

**basisScope:** Q,I,O are finite exact-equality sets; q₀∈Q makes Q nonempty. I may be empty. O is nonempty because λ:Q→O. Input words are finite, including ε; run from any q, default q₀. Pure deterministic total steps, unbounded word length, no ε-input transitions, nondeterminism, time, effects or accepting states. A run on n inputs has n+1 outputs; a convention suppressing the initial output needs an explicit mapping.

**verificationObligation:** Map exact carriers, equality, totality and the explicit profile conventions before use.; Model and theorem evidence does not establish a concrete software implementation refinement.

**reviewStatus:** Sourced model with separately registered Lean satisfaction and derived witnesses; verification requires fresh audit evidence.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-MooreTransducer-next"></a>

### next state

`urn:csabs:operation/MooreTransducer-next`

**signature:** next : Q×I→Q

**description:** Apply deterministic state transition.

**precondition:** Supplied machine; q∈Q and a∈I.

**postcondition:** Exactly δ(q,a).

**totality:** Total on the stated domain.

**source:** [MathWorks Stateflow: Overview of Mealy and Moore Machines](https://www.mathworks.com/help/stateflow/ug/overview-of-mealy-and-moore-machines.html); citation: R2026b, Semantics of Mealy and Moore Machines: next-state and output equations.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference

**sourceLocator:** Stateflow Semantics of Mealy and Moore Machines

**sourceNote:** Constructs a pure finite-word model from the documented transition/output signatures. Initial Moore emission is an explicit catalog convention, not a timing/effect model.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-MooreTransducer-emit"></a>

### output

`urn:csabs:operation/MooreTransducer-emit`

**signature:** emit : Q→O

**description:** Evaluate the machine output map.

**precondition:** A state.

**postcondition:** Exactly λ(q).

**totality:** Total on the stated domain.

**source:** [MathWorks Stateflow: Overview of Mealy and Moore Machines](https://www.mathworks.com/help/stateflow/ug/overview-of-mealy-and-moore-machines.html); citation: R2026b, Semantics of Mealy and Moore Machines: next-state and output equations.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference

**sourceLocator:** Stateflow Semantics of Mealy and Moore Machines

**sourceNote:** Constructs a pure finite-word model from the documented transition/output signatures. Initial Moore emission is an explicit catalog convention, not a timing/effect model.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-MooreTransducer-run"></a>

### run finite word

`urn:csabs:operation/MooreTransducer-run`

**signature:** run : Q×List(I)→Q×List(O)

**description:** Thread states through the word. Use q₀ for default execution.

**precondition:** q∈Q; finite input word.

**postcondition:** Return final state and n+1 outputs including λ(q) at the start.

**totality:** Total on the stated domain.

**source:** [MathWorks Stateflow: Overview of Mealy and Moore Machines](https://www.mathworks.com/help/stateflow/ug/overview-of-mealy-and-moore-machines.html); citation: R2026b, Semantics of Mealy and Moore Machines: next-state and output equations.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference

**sourceLocator:** Stateflow Semantics of Mealy and Moore Machines

**sourceNote:** Constructs a pure finite-word model from the documented transition/output signatures. Initial Moore emission is an explicit catalog convention, not a timing/effect model.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-MooreTransducer-as-mealy"></a>

### destination-output Mealy conversion

`urn:csabs:operation/MooreTransducer-as-mealy`

**signature:** asMealy : Moore(Q,I,O)→Mealy(Q,I,O)

**description:** Retain next/initial and set emission(q,a)=λ(δ(q,a)).

**precondition:** Total finite Moore machine.

**postcondition:** The Moore output is its initial output prepended to this Mealy output; no unqualified equal-word claim.

**totality:** Total on the stated domain.

**source:** [MathWorks Stateflow: Overview of Mealy and Moore Machines](https://www.mathworks.com/help/stateflow/ug/overview-of-mealy-and-moore-machines.html); citation: R2026b, Semantics of Mealy and Moore Machines: next-state and output equations.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference

**sourceLocator:** Stateflow Semantics of Mealy and Moore Machines

**sourceNote:** Constructs a pure finite-word model from the documented transition/output signatures. Initial Moore emission is an explicit catalog convention, not a timing/effect model.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-MooreTransducer-defining-profile"></a>

### defining profile

`urn:csabs:axiom/MooreTransducer-defining-profile`

**statement:** Typed total δ and λ with a designated initial state. Word execution is primitive recursion: run(q,ε)=(q,[λ(q)]); run(q,a·xs) emits λ(q) then executes xs from δ(q,a).

**formalStatement:** For q₀,q₁,…,qₙ with qᵢ₊₁=δ(qᵢ,aᵢ), return final qₙ and [λ(q₀),…,λ(qₙ)].

**assumptions:** Q,I,O are finite exact-equality sets; q₀∈Q makes Q nonempty. I may be empty. O is nonempty because λ:Q→O. Input words are finite, including ε; run from any q, default q₀. Pure deterministic total steps, unbounded word length, no ε-input transitions, nondeterminism, time, effects or accepting states. A run on n inputs has n+1 outputs; a convention suppressing the initial output needs an explicit mapping.

**ruleRole:** defining-rule

**reviewStatus:** Structure constraints; satisfaction is established separately for the selected model.

**source:** [MathWorks Stateflow: Overview of Mealy and Moore Machines](https://www.mathworks.com/help/stateflow/ug/overview-of-mealy-and-moore-machines.html); citation: R2026b, Semantics of Mealy and Moore Machines: next-state and output equations.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference

**sourceLocator:** Stateflow Semantics of Mealy and Moore Machines

**sourceNote:** Constructs a pure finite-word model from the documented transition/output signatures. Initial Moore emission is an explicit catalog convention, not a timing/effect model.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-MooreTransducer-output-length"></a>

### output-length

`urn:csabs:law/MooreTransducer-output-length`

**statement:** Induct on inputs; empty input has one output and each transition adds one.

**formalStatement:** ∀ {Q I O : Type} [Fintype Q] [Fintype I] [Fintype O] (m : Catalog.MooreTransducer Q I O) (q : Q) (xs : List I), (Catalog.mooreRun m q xs).2.length = xs.length + 1

**assumptions:** Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality.

**dependsOn:** [defining profile](MooreTransducer.md#node-urn-csabs-axiom-MooreTransducer-defining-profile); [induction](Sequence.md#node-urn-csabs-axiom-Sequence-induction); [length-recursion](Sequence.md#node-urn-csabs-axiom-Sequence-length-recursion)

**proofSketch:** Induct on inputs; empty input has one output and each transition adds one.

**reviewStatus:** Derived mathematical law; separately registered theorem supplies explicit proof evidence.

**source:** [MathWorks Stateflow: Overview of Mealy and Moore Machines](https://www.mathworks.com/help/stateflow/ug/overview-of-mealy-and-moore-machines.html); citation: R2026b, Semantics of Mealy and Moore Machines: next-state and output equations.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; Catalog release, sequence, transducer, schema, date and extension models and witnesses; path: lean/Catalog/ReleaseSequenceModels.lean; accessedOn: 2026-11-20; sourceRole: local-lean-formulation-and-proof

**sourceLocator:** Stateflow Semantics of Mealy and Moore Machines; Catalog.moore_length

**sourceNote:** Derived for the explicit selected model. Induct on inputs; empty input has one output and each transition adds one.

**provenanceKind:** derived

**ruleRole:** derived-law

<a id="node-urn-csabs-law-MooreTransducer-mealy-alignment"></a>

### mealy-alignment

`urn:csabs:law/MooreTransducer-mealy-alignment`

**statement:** Choose Mealy emission λ(δ(q,a)); induction shows equivalence after accounting for the Moore initial output.

**formalStatement:** ∀ {Q I O : Type} [Fintype Q] [Fintype I] [Fintype O] (m : Catalog.MooreTransducer Q I O) (q : Q) (xs : List I), (Catalog.mooreRun m q xs).2 = m.emit q :: (Catalog.mealyRun (Catalog.mooreAsMealy m) q xs).2

**assumptions:** Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality.

**dependsOn:** [defining profile](MooreTransducer.md#node-urn-csabs-axiom-MooreTransducer-defining-profile); [induction](Sequence.md#node-urn-csabs-axiom-Sequence-induction)

**proofSketch:** Choose Mealy emission λ(δ(q,a)); induction shows equivalence after accounting for the Moore initial output.

**reviewStatus:** Derived mathematical law; separately registered theorem supplies explicit proof evidence.

**source:** [MathWorks Stateflow: Overview of Mealy and Moore Machines](https://www.mathworks.com/help/stateflow/ug/overview-of-mealy-and-moore-machines.html); citation: R2026b, Semantics of Mealy and Moore Machines: next-state and output equations.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; Catalog release, sequence, transducer, schema, date and extension models and witnesses; path: lean/Catalog/ReleaseSequenceModels.lean; accessedOn: 2026-11-20; sourceRole: local-lean-formulation-and-proof

**sourceLocator:** Stateflow Semantics of Mealy and Moore Machines; Catalog.moore_mealy_alignment

**sourceNote:** Derived for the explicit selected model. Choose Mealy emission λ(δ(q,a)); induction shows equivalence after accounting for the Moore initial output.

**provenanceKind:** derived

**ruleRole:** derived-law

## Theorems

<a id="node-urn-csabs-theorem-MooreTransducer-run-equations"></a>

### run-equations

`urn:csabs:theorem/MooreTransducer-run-equations`

**statement:** Primitive recursion realizes the state-output convention including the initial state output.

**formalStatement:** ∀ {Q I O : Type} [Fintype Q] [Fintype I] [Fintype O] (m : Catalog.MooreTransducer Q I O) (q : Q), Catalog.mooreRun m q [] = (q, [m.emit q]) ∧ (∀ a xs, Catalog.mooreRun m q (a :: xs) = ((Catalog.mooreRun m (m.next q a) xs).1, m.emit q :: (Catalog.mooreRun m (m.next q a) xs).2))

**assumptions:** Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality.

**dependsOn:** [defining profile](MooreTransducer.md#node-urn-csabs-axiom-MooreTransducer-defining-profile)

**proofSketch:** Primitive recursion realizes the state-output convention including the initial state output.

**reviewStatus:** Separately registered Lean witness; require fresh compiler and axiom audit for verified status.

**source:** [MathWorks Stateflow: Overview of Mealy and Moore Machines](https://www.mathworks.com/help/stateflow/ug/overview-of-mealy-and-moore-machines.html); citation: R2026b, Semantics of Mealy and Moore Machines: next-state and output equations.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; Catalog release, sequence, transducer, schema, date and extension models and witnesses; path: lean/Catalog/ReleaseSequenceModels.lean; accessedOn: 2026-11-20; sourceRole: local-lean-formulation-and-proof

**sourceLocator:** Stateflow Semantics of Mealy and Moore Machines; Catalog.moore_equations

**sourceNote:** Derived for the explicit selected model. Primitive recursion realizes the state-output convention including the initial state output.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {Q I O : Type} [Fintype Q] [Fintype I] [Fintype O] (m : Catalog.MooreTransducer Q I O) (q : Q), Catalog.mooreRun m q [] = (q, [m.emit q]) ∧ (∀ a xs, Catalog.mooreRun m q (a :: xs) = ((Catalog.mooreRun m (m.next q a) xs).1, m.emit q :: (Catalog.mooreRun m (m.next q a) xs).2))
```

**Source:** [`Catalog.moore_equations`](../lean/Catalog/ReleaseSequenceModels.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** Primitive recursion realizes the state-output convention including the initial state output.

**Limits:** Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/MooreTransducer-defining-profile": "Proved constraint for the specified concrete interpretation or structural recursion; not a hypothesis asserting its own satisfaction. Primitive recursion realizes the state-output convention including the initial state output."
}
```

<a id="node-urn-csabs-theorem-MooreTransducer-model-satisfaction"></a>

### model-satisfaction

`urn:csabs:theorem/MooreTransducer-model-satisfaction`

**statement:** Construct a two-state total machine and evaluate its initial and subsequent outputs.

**formalStatement:** Catalog.mooreRun Catalog.boolMoore false [true, false] = (false, [false, true, false])

**assumptions:** Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality.

**dependsOn:** [defining profile](MooreTransducer.md#node-urn-csabs-axiom-MooreTransducer-defining-profile)

**proofSketch:** Construct a two-state total machine and evaluate its initial and subsequent outputs.

**reviewStatus:** Separately registered Lean witness; require fresh compiler and axiom audit for verified status.

**source:** [MathWorks Stateflow: Overview of Mealy and Moore Machines](https://www.mathworks.com/help/stateflow/ug/overview-of-mealy-and-moore-machines.html); citation: R2026b, Semantics of Mealy and Moore Machines: next-state and output equations.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; Catalog release, sequence, transducer, schema, date and extension models and witnesses; path: lean/Catalog/ReleaseSequenceModels.lean; accessedOn: 2026-11-20; sourceRole: local-lean-formulation-and-proof

**sourceLocator:** Stateflow Semantics of Mealy and Moore Machines; Catalog.moore_model_satisfaction

**sourceNote:** Derived for the explicit selected model. Construct a two-state total machine and evaluate its initial and subsequent outputs.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
Catalog.mooreRun Catalog.boolMoore false [true, false] = (false, [false, true, false])
```

**Source:** [`Catalog.moore_model_satisfaction`](../lean/Catalog/ReleaseSequenceModels.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** Construct a two-state total machine and evaluate its initial and subsequent outputs.

**Limits:** Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/MooreTransducer-defining-profile": "Proved constraint for the specified concrete interpretation or structural recursion; not a hypothesis asserting its own satisfaction. Construct a two-state total machine and evaluate its initial and subsequent outputs."
}
```

<a id="node-urn-csabs-theorem-MooreTransducer-output-length"></a>

### output-length

`urn:csabs:theorem/MooreTransducer-output-length`

**statement:** Induct on inputs; empty input has one output and each transition adds one.

**formalStatement:** ∀ {Q I O : Type} [Fintype Q] [Fintype I] [Fintype O] (m : Catalog.MooreTransducer Q I O) (q : Q) (xs : List I), (Catalog.mooreRun m q xs).2.length = xs.length + 1

**assumptions:** Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality.

**dependsOn:** [defining profile](MooreTransducer.md#node-urn-csabs-axiom-MooreTransducer-defining-profile); [induction](Sequence.md#node-urn-csabs-axiom-Sequence-induction); [length-recursion](Sequence.md#node-urn-csabs-axiom-Sequence-length-recursion)

**proofSketch:** Induct on inputs; empty input has one output and each transition adds one.

**reviewStatus:** Separately registered Lean witness; require fresh compiler and axiom audit for verified status.

**source:** [MathWorks Stateflow: Overview of Mealy and Moore Machines](https://www.mathworks.com/help/stateflow/ug/overview-of-mealy-and-moore-machines.html); citation: R2026b, Semantics of Mealy and Moore Machines: next-state and output equations.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; Catalog release, sequence, transducer, schema, date and extension models and witnesses; path: lean/Catalog/ReleaseSequenceModels.lean; accessedOn: 2026-11-20; sourceRole: local-lean-formulation-and-proof

**sourceLocator:** Stateflow Semantics of Mealy and Moore Machines; Catalog.moore_length

**sourceNote:** Derived for the explicit selected model. Induct on inputs; empty input has one output and each transition adds one.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {Q I O : Type} [Fintype Q] [Fintype I] [Fintype O] (m : Catalog.MooreTransducer Q I O) (q : Q) (xs : List I), (Catalog.mooreRun m q xs).2.length = xs.length + 1
```

**Source:** [`Catalog.moore_length`](../lean/Catalog/ReleaseSequenceModels.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** Induct on inputs; empty input has one output and each transition adds one.

**Limits:** Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/MooreTransducer-defining-profile": "Proved constraint for the specified concrete interpretation or structural recursion; not a hypothesis asserting its own satisfaction. Induct on inputs; empty input has one output and each transition adds one.",
  "urn:csabs:axiom/Sequence-induction": "Existing finite-list induction, concatenation or length premise, instantiated with exact List equality; no editing behavior is inferred from it.",
  "urn:csabs:axiom/Sequence-length-recursion": "Existing finite-list induction, concatenation or length premise, instantiated with exact List equality; no editing behavior is inferred from it."
}
```

<a id="node-urn-csabs-theorem-MooreTransducer-mealy-alignment"></a>

### mealy-alignment

`urn:csabs:theorem/MooreTransducer-mealy-alignment`

**statement:** Choose Mealy emission λ(δ(q,a)); induction shows equivalence after accounting for the Moore initial output.

**formalStatement:** ∀ {Q I O : Type} [Fintype Q] [Fintype I] [Fintype O] (m : Catalog.MooreTransducer Q I O) (q : Q) (xs : List I), (Catalog.mooreRun m q xs).2 = m.emit q :: (Catalog.mealyRun (Catalog.mooreAsMealy m) q xs).2

**assumptions:** Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality.

**dependsOn:** [defining profile](MooreTransducer.md#node-urn-csabs-axiom-MooreTransducer-defining-profile); [induction](Sequence.md#node-urn-csabs-axiom-Sequence-induction)

**proofSketch:** Choose Mealy emission λ(δ(q,a)); induction shows equivalence after accounting for the Moore initial output.

**reviewStatus:** Separately registered Lean witness; require fresh compiler and axiom audit for verified status.

**source:** [MathWorks Stateflow: Overview of Mealy and Moore Machines](https://www.mathworks.com/help/stateflow/ug/overview-of-mealy-and-moore-machines.html); citation: R2026b, Semantics of Mealy and Moore Machines: next-state and output equations.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; Catalog release, sequence, transducer, schema, date and extension models and witnesses; path: lean/Catalog/ReleaseSequenceModels.lean; accessedOn: 2026-11-20; sourceRole: local-lean-formulation-and-proof

**sourceLocator:** Stateflow Semantics of Mealy and Moore Machines; Catalog.moore_mealy_alignment

**sourceNote:** Derived for the explicit selected model. Choose Mealy emission λ(δ(q,a)); induction shows equivalence after accounting for the Moore initial output.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {Q I O : Type} [Fintype Q] [Fintype I] [Fintype O] (m : Catalog.MooreTransducer Q I O) (q : Q) (xs : List I), (Catalog.mooreRun m q xs).2 = m.emit q :: (Catalog.mealyRun (Catalog.mooreAsMealy m) q xs).2
```

**Source:** [`Catalog.moore_mealy_alignment`](../lean/Catalog/ReleaseSequenceModels.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** Choose Mealy emission λ(δ(q,a)); induction shows equivalence after accounting for the Moore initial output.

**Limits:** Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/MooreTransducer-defining-profile": "Proved constraint for the specified concrete interpretation or structural recursion; not a hypothesis asserting its own satisfaction. Choose Mealy emission λ(δ(q,a)); induction shows equivalence after accounting for the Moore initial output.",
  "urn:csabs:axiom/Sequence-induction": "Existing finite-list induction, concatenation or length premise, instantiated with exact List equality; no editing behavior is inferred from it."
}
```

## Concept provenance

- [MathWorks Stateflow: Overview of Mealy and Moore Machines](https://www.mathworks.com/help/stateflow/ug/overview-of-mealy-and-moore-machines.html); citation: R2026b, Semantics of Mealy and Moore Machines: next-state and output equations.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference

**sourceLocator:** Stateflow Semantics of Mealy and Moore Machines

**sourceNote:** Constructs a pure finite-word model from the documented transition/output signatures. Initial Moore emission is an explicit catalog convention, not a timing/effect model.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/MooreTransducer",
    "type": "Concept",
    "shortForm": "MooreTransducer",
    "fullName": "Moore deterministic finite sequential transducer",
    "synonyms": [
      "Moore machine",
      "State-output finite sequential transducer"
    ],
    "category": [
      "urn:csabs:category/behavior"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "definition": "A deterministic finite-state input/output machine with total next-state and output maps; outputs are attached to states and include the initial state output.",
    "notation": "(Q,I,O,q₀,δ,λ); δ:Q×I→Q; λ:Q→O",
    "requiresConcept": [
      "urn:csabs:concept/Sequence",
      "urn:csabs:concept/Function"
    ],
    "relatedConcept": [
      "urn:csabs:concept/DFA",
      "urn:csabs:concept/LabelledTransitionSystem",
      "urn:csabs:concept/MealyTransducer"
    ],
    "axiomBasis": "Typed total δ and λ with a designated initial state. Word execution is primitive recursion: run(q,ε)=(q,[λ(q)]); run(q,a·xs) emits λ(q) then executes xs from δ(q,a).",
    "basisKind": "defined-structure",
    "basisScope": "Q,I,O are finite exact-equality sets; q₀∈Q makes Q nonempty. I may be empty. O is nonempty because λ:Q→O. Input words are finite, including ε; run from any q, default q₀. Pure deterministic total steps, unbounded word length, no ε-input transitions, nondeterminism, time, effects or accepting states. A run on n inputs has n+1 outputs; a convention suppressing the initial output needs an explicit mapping.",
    "mathematicalFormulation": "For q₀,q₁,…,qₙ with qᵢ₊₁=δ(qᵢ,aᵢ), return final qₙ and [λ(q₀),…,λ(qₙ)].",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Sourced model with separately registered Lean satisfaction and derived witnesses; verification requires fresh audit evidence.",
    "verificationObligation": [
      "Map exact carriers, equality, totality and the explicit profile conventions before use.",
      "Model and theorem evidence does not establish a concrete software implementation refinement."
    ],
    "hasOperation": [
      "urn:csabs:operation/MooreTransducer-next",
      "urn:csabs:operation/MooreTransducer-emit",
      "urn:csabs:operation/MooreTransducer-run",
      "urn:csabs:operation/MooreTransducer-as-mealy"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/MooreTransducer-defining-profile"
    ],
    "hasLaw": [
      "urn:csabs:law/MooreTransducer-output-length",
      "urn:csabs:law/MooreTransducer-mealy-alignment"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/MooreTransducer-run-equations",
      "urn:csabs:theorem/MooreTransducer-model-satisfaction",
      "urn:csabs:theorem/MooreTransducer-output-length",
      "urn:csabs:theorem/MooreTransducer-mealy-alignment"
    ],
    "source": [
      "urn:csabs:source/seven-transducer"
    ],
    "sourceLocator": "Stateflow Semantics of Mealy and Moore Machines",
    "sourceNote": "Constructs a pure finite-word model from the documented transition/output signatures. Initial Moore emission is an explicit catalog convention, not a timing/effect model.",
    "provenanceKind": "adapted",
    "leanFormulation": "structure MooreTransducer (Q I O : Type) [Fintype Q] [Fintype I] [Fintype O] where\n  initial : Q\n  next : Q → I → Q\n  emit : Q → O",
    "formulationSource": "urn:csabs:source/seven-lean-models",
    "formulationLocator": "Catalog.MooreTransducer",
    "formulationScope": "model",
    "leanModelMapping": "For q₀,q₁,…,qₙ with qᵢ₊₁=δ(qᵢ,aᵢ), return final qₙ and [λ(q₀),…,λ(qₙ)].",
    "leanModelLimitations": "Q,I,O are finite exact-equality sets; q₀∈Q makes Q nonempty. I may be empty. O is nonempty because λ:Q→O. Input words are finite, including ε; run from any q, default q₀. Pure deterministic total steps, unbounded word length, no ε-input transitions, nondeterminism, time, effects or accepting states. A run on n inputs has n+1 outputs; a convention suppressing the initial output needs an explicit mapping. Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit."
  },
  {
    "id": "urn:csabs:operation/MooreTransducer-next",
    "type": "Operation",
    "concept": "urn:csabs:concept/MooreTransducer",
    "name": "next state",
    "signature": "next : Q×I→Q",
    "description": "Apply deterministic state transition.",
    "precondition": "Supplied machine; q∈Q and a∈I.",
    "postcondition": "Exactly δ(q,a).",
    "totality": "Total on the stated domain.",
    "source": [
      "urn:csabs:source/seven-transducer"
    ],
    "sourceLocator": "Stateflow Semantics of Mealy and Moore Machines",
    "sourceNote": "Constructs a pure finite-word model from the documented transition/output signatures. Initial Moore emission is an explicit catalog convention, not a timing/effect model.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/MooreTransducer-emit",
    "type": "Operation",
    "concept": "urn:csabs:concept/MooreTransducer",
    "name": "output",
    "signature": "emit : Q→O",
    "description": "Evaluate the machine output map.",
    "precondition": "A state.",
    "postcondition": "Exactly λ(q).",
    "totality": "Total on the stated domain.",
    "source": [
      "urn:csabs:source/seven-transducer"
    ],
    "sourceLocator": "Stateflow Semantics of Mealy and Moore Machines",
    "sourceNote": "Constructs a pure finite-word model from the documented transition/output signatures. Initial Moore emission is an explicit catalog convention, not a timing/effect model.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/MooreTransducer-run",
    "type": "Operation",
    "concept": "urn:csabs:concept/MooreTransducer",
    "name": "run finite word",
    "signature": "run : Q×List(I)→Q×List(O)",
    "description": "Thread states through the word. Use q₀ for default execution.",
    "precondition": "q∈Q; finite input word.",
    "postcondition": "Return final state and n+1 outputs including λ(q) at the start.",
    "totality": "Total on the stated domain.",
    "source": [
      "urn:csabs:source/seven-transducer"
    ],
    "sourceLocator": "Stateflow Semantics of Mealy and Moore Machines",
    "sourceNote": "Constructs a pure finite-word model from the documented transition/output signatures. Initial Moore emission is an explicit catalog convention, not a timing/effect model.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/MooreTransducer-as-mealy",
    "type": "Operation",
    "concept": "urn:csabs:concept/MooreTransducer",
    "name": "destination-output Mealy conversion",
    "signature": "asMealy : Moore(Q,I,O)→Mealy(Q,I,O)",
    "description": "Retain next/initial and set emission(q,a)=λ(δ(q,a)).",
    "precondition": "Total finite Moore machine.",
    "postcondition": "The Moore output is its initial output prepended to this Mealy output; no unqualified equal-word claim.",
    "totality": "Total on the stated domain.",
    "source": [
      "urn:csabs:source/seven-transducer"
    ],
    "sourceLocator": "Stateflow Semantics of Mealy and Moore Machines",
    "sourceNote": "Constructs a pure finite-word model from the documented transition/output signatures. Initial Moore emission is an explicit catalog convention, not a timing/effect model.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/MooreTransducer-defining-profile",
    "type": "Axiom",
    "name": "defining profile",
    "statement": "Typed total δ and λ with a designated initial state. Word execution is primitive recursion: run(q,ε)=(q,[λ(q)]); run(q,a·xs) emits λ(q) then executes xs from δ(q,a).",
    "formalStatement": "For q₀,q₁,…,qₙ with qᵢ₊₁=δ(qᵢ,aᵢ), return final qₙ and [λ(q₀),…,λ(qₙ)].",
    "assumptions": [
      "Q,I,O are finite exact-equality sets; q₀∈Q makes Q nonempty. I may be empty. O is nonempty because λ:Q→O. Input words are finite, including ε; run from any q, default q₀. Pure deterministic total steps, unbounded word length, no ε-input transitions, nondeterminism, time, effects or accepting states. A run on n inputs has n+1 outputs; a convention suppressing the initial output needs an explicit mapping."
    ],
    "appliesTo": [
      "urn:csabs:concept/MooreTransducer"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Structure constraints; satisfaction is established separately for the selected model.",
    "source": [
      "urn:csabs:source/seven-transducer"
    ],
    "sourceLocator": "Stateflow Semantics of Mealy and Moore Machines",
    "sourceNote": "Constructs a pure finite-word model from the documented transition/output signatures. Initial Moore emission is an explicit catalog convention, not a timing/effect model.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/MooreTransducer-output-length",
    "type": "Law",
    "name": "output-length",
    "statement": "Induct on inputs; empty input has one output and each transition adds one.",
    "formalStatement": "∀ {Q I O : Type} [Fintype Q] [Fintype I] [Fintype O] (m : Catalog.MooreTransducer Q I O) (q : Q) (xs : List I), (Catalog.mooreRun m q xs).2.length = xs.length + 1",
    "assumptions": [
      "Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/MooreTransducer"
    ],
    "dependsOn": [
      "urn:csabs:axiom/MooreTransducer-defining-profile",
      "urn:csabs:axiom/Sequence-induction",
      "urn:csabs:axiom/Sequence-length-recursion"
    ],
    "proofSketch": "Induct on inputs; empty input has one output and each transition adds one.",
    "reviewStatus": "Derived mathematical law; separately registered theorem supplies explicit proof evidence.",
    "source": [
      "urn:csabs:source/seven-transducer",
      "urn:csabs:source/seven-lean-models"
    ],
    "sourceLocator": "Stateflow Semantics of Mealy and Moore Machines; Catalog.moore_length",
    "sourceNote": "Derived for the explicit selected model. Induct on inputs; empty input has one output and each transition adds one.",
    "provenanceKind": "derived",
    "ruleRole": "derived-law"
  },
  {
    "id": "urn:csabs:law/MooreTransducer-mealy-alignment",
    "type": "Law",
    "name": "mealy-alignment",
    "statement": "Choose Mealy emission λ(δ(q,a)); induction shows equivalence after accounting for the Moore initial output.",
    "formalStatement": "∀ {Q I O : Type} [Fintype Q] [Fintype I] [Fintype O] (m : Catalog.MooreTransducer Q I O) (q : Q) (xs : List I), (Catalog.mooreRun m q xs).2 = m.emit q :: (Catalog.mealyRun (Catalog.mooreAsMealy m) q xs).2",
    "assumptions": [
      "Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/MooreTransducer"
    ],
    "dependsOn": [
      "urn:csabs:axiom/MooreTransducer-defining-profile",
      "urn:csabs:axiom/Sequence-induction"
    ],
    "proofSketch": "Choose Mealy emission λ(δ(q,a)); induction shows equivalence after accounting for the Moore initial output.",
    "reviewStatus": "Derived mathematical law; separately registered theorem supplies explicit proof evidence.",
    "source": [
      "urn:csabs:source/seven-transducer",
      "urn:csabs:source/seven-lean-models"
    ],
    "sourceLocator": "Stateflow Semantics of Mealy and Moore Machines; Catalog.moore_mealy_alignment",
    "sourceNote": "Derived for the explicit selected model. Choose Mealy emission λ(δ(q,a)); induction shows equivalence after accounting for the Moore initial output.",
    "provenanceKind": "derived",
    "ruleRole": "derived-law"
  },
  {
    "id": "urn:csabs:theorem/MooreTransducer-run-equations",
    "type": "Theorem",
    "name": "run-equations",
    "statement": "Primitive recursion realizes the state-output convention including the initial state output.",
    "formalStatement": "∀ {Q I O : Type} [Fintype Q] [Fintype I] [Fintype O] (m : Catalog.MooreTransducer Q I O) (q : Q), Catalog.mooreRun m q [] = (q, [m.emit q]) ∧ (∀ a xs, Catalog.mooreRun m q (a :: xs) = ((Catalog.mooreRun m (m.next q a) xs).1, m.emit q :: (Catalog.mooreRun m (m.next q a) xs).2))",
    "assumptions": [
      "Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/MooreTransducer"
    ],
    "dependsOn": [
      "urn:csabs:axiom/MooreTransducer-defining-profile"
    ],
    "proofSketch": "Primitive recursion realizes the state-output convention including the initial state output.",
    "reviewStatus": "Separately registered Lean witness; require fresh compiler and axiom audit for verified status.",
    "source": [
      "urn:csabs:source/seven-transducer",
      "urn:csabs:source/seven-lean-models"
    ],
    "sourceLocator": "Stateflow Semantics of Mealy and Moore Machines; Catalog.moore_equations",
    "sourceNote": "Derived for the explicit selected model. Primitive recursion realizes the state-output convention including the initial state output.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {Q I O : Type} [Fintype Q] [Fintype I] [Fintype O] (m : Catalog.MooreTransducer Q I O) (q : Q), Catalog.mooreRun m q [] = (q, [m.emit q]) ∧ (∀ a xs, Catalog.mooreRun m q (a :: xs) = ((Catalog.mooreRun m (m.next q a) xs).1, m.emit q :: (Catalog.mooreRun m (m.next q a) xs).2))",
    "formulationSource": "urn:csabs:source/seven-lean-models",
    "formulationLocator": "Catalog.moore_equations",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Primitive recursion realizes the state-output convention including the initial state output.",
    "leanModelLimitations": "Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/MooreTransducer-defining-profile\": \"Proved constraint for the specified concrete interpretation or structural recursion; not a hypothesis asserting its own satisfaction. Primitive recursion realizes the state-output convention including the initial state output.\"}"
  },
  {
    "id": "urn:csabs:theorem/MooreTransducer-model-satisfaction",
    "type": "Theorem",
    "name": "model-satisfaction",
    "statement": "Construct a two-state total machine and evaluate its initial and subsequent outputs.",
    "formalStatement": "Catalog.mooreRun Catalog.boolMoore false [true, false] = (false, [false, true, false])",
    "assumptions": [
      "Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/MooreTransducer"
    ],
    "dependsOn": [
      "urn:csabs:axiom/MooreTransducer-defining-profile"
    ],
    "proofSketch": "Construct a two-state total machine and evaluate its initial and subsequent outputs.",
    "reviewStatus": "Separately registered Lean witness; require fresh compiler and axiom audit for verified status.",
    "source": [
      "urn:csabs:source/seven-transducer",
      "urn:csabs:source/seven-lean-models"
    ],
    "sourceLocator": "Stateflow Semantics of Mealy and Moore Machines; Catalog.moore_model_satisfaction",
    "sourceNote": "Derived for the explicit selected model. Construct a two-state total machine and evaluate its initial and subsequent outputs.",
    "provenanceKind": "derived",
    "leanFormulation": "Catalog.mooreRun Catalog.boolMoore false [true, false] = (false, [false, true, false])",
    "formulationSource": "urn:csabs:source/seven-lean-models",
    "formulationLocator": "Catalog.moore_model_satisfaction",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Construct a two-state total machine and evaluate its initial and subsequent outputs.",
    "leanModelLimitations": "Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/MooreTransducer-defining-profile\": \"Proved constraint for the specified concrete interpretation or structural recursion; not a hypothesis asserting its own satisfaction. Construct a two-state total machine and evaluate its initial and subsequent outputs.\"}"
  },
  {
    "id": "urn:csabs:theorem/MooreTransducer-output-length",
    "type": "Theorem",
    "name": "output-length",
    "statement": "Induct on inputs; empty input has one output and each transition adds one.",
    "formalStatement": "∀ {Q I O : Type} [Fintype Q] [Fintype I] [Fintype O] (m : Catalog.MooreTransducer Q I O) (q : Q) (xs : List I), (Catalog.mooreRun m q xs).2.length = xs.length + 1",
    "assumptions": [
      "Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/MooreTransducer"
    ],
    "dependsOn": [
      "urn:csabs:axiom/MooreTransducer-defining-profile",
      "urn:csabs:axiom/Sequence-induction",
      "urn:csabs:axiom/Sequence-length-recursion"
    ],
    "proofSketch": "Induct on inputs; empty input has one output and each transition adds one.",
    "reviewStatus": "Separately registered Lean witness; require fresh compiler and axiom audit for verified status.",
    "source": [
      "urn:csabs:source/seven-transducer",
      "urn:csabs:source/seven-lean-models"
    ],
    "sourceLocator": "Stateflow Semantics of Mealy and Moore Machines; Catalog.moore_length",
    "sourceNote": "Derived for the explicit selected model. Induct on inputs; empty input has one output and each transition adds one.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {Q I O : Type} [Fintype Q] [Fintype I] [Fintype O] (m : Catalog.MooreTransducer Q I O) (q : Q) (xs : List I), (Catalog.mooreRun m q xs).2.length = xs.length + 1",
    "formulationSource": "urn:csabs:source/seven-lean-models",
    "formulationLocator": "Catalog.moore_length",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Induct on inputs; empty input has one output and each transition adds one.",
    "leanModelLimitations": "Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/MooreTransducer-defining-profile\": \"Proved constraint for the specified concrete interpretation or structural recursion; not a hypothesis asserting its own satisfaction. Induct on inputs; empty input has one output and each transition adds one.\", \"urn:csabs:axiom/Sequence-induction\": \"Existing finite-list induction, concatenation or length premise, instantiated with exact List equality; no editing behavior is inferred from it.\", \"urn:csabs:axiom/Sequence-length-recursion\": \"Existing finite-list induction, concatenation or length premise, instantiated with exact List equality; no editing behavior is inferred from it.\"}"
  },
  {
    "id": "urn:csabs:theorem/MooreTransducer-mealy-alignment",
    "type": "Theorem",
    "name": "mealy-alignment",
    "statement": "Choose Mealy emission λ(δ(q,a)); induction shows equivalence after accounting for the Moore initial output.",
    "formalStatement": "∀ {Q I O : Type} [Fintype Q] [Fintype I] [Fintype O] (m : Catalog.MooreTransducer Q I O) (q : Q) (xs : List I), (Catalog.mooreRun m q xs).2 = m.emit q :: (Catalog.mealyRun (Catalog.mooreAsMealy m) q xs).2",
    "assumptions": [
      "Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/MooreTransducer"
    ],
    "dependsOn": [
      "urn:csabs:axiom/MooreTransducer-defining-profile",
      "urn:csabs:axiom/Sequence-induction"
    ],
    "proofSketch": "Choose Mealy emission λ(δ(q,a)); induction shows equivalence after accounting for the Moore initial output.",
    "reviewStatus": "Separately registered Lean witness; require fresh compiler and axiom audit for verified status.",
    "source": [
      "urn:csabs:source/seven-transducer",
      "urn:csabs:source/seven-lean-models"
    ],
    "sourceLocator": "Stateflow Semantics of Mealy and Moore Machines; Catalog.moore_mealy_alignment",
    "sourceNote": "Derived for the explicit selected model. Choose Mealy emission λ(δ(q,a)); induction shows equivalence after accounting for the Moore initial output.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {Q I O : Type} [Fintype Q] [Fintype I] [Fintype O] (m : Catalog.MooreTransducer Q I O) (q : Q) (xs : List I), (Catalog.mooreRun m q xs).2 = m.emit q :: (Catalog.mealyRun (Catalog.mooreAsMealy m) q xs).2",
    "formulationSource": "urn:csabs:source/seven-lean-models",
    "formulationLocator": "Catalog.moore_mealy_alignment",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Choose Mealy emission λ(δ(q,a)); induction shows equivalence after accounting for the Moore initial output.",
    "leanModelLimitations": "Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/MooreTransducer-defining-profile\": \"Proved constraint for the specified concrete interpretation or structural recursion; not a hypothesis asserting its own satisfaction. Choose Mealy emission λ(δ(q,a)); induction shows equivalence after accounting for the Moore initial output.\", \"urn:csabs:axiom/Sequence-induction\": \"Existing finite-list induction, concatenation or length premise, instantiated with exact List equality; no editing behavior is inferred from it.\"}"
  }
]
```
<!-- graph-record:end -->
