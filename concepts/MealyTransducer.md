# Mealy deterministic finite sequential transducer

A deterministic finite-state input/output machine with total next-state and output maps; outputs are attached to state/input transitions.

**Notation:** (Q,I,O,q₀,δ,λ); δ:Q×I→Q; λ:Q×I→O

**Stable ID:** `urn:csabs:concept/MealyTransducer`

**Categories:** Behavior and transition systems

**Kind:** semantic-model

**Prerequisites:** [Finite sequence (List datatype)](Sequence.md), [Total function](Function.md)

**Related concepts:** [Deterministic finite automaton with total transition](DFA.md), [Action-labelled transition system with initial states](LabelledTransitionSystem.md), [Moore deterministic finite sequential transducer](MooreTransducer.md)

## Backlinks

- [Moore deterministic finite sequential transducer](MooreTransducer.md) — `relatedConcept`

## Mathematical formulation

For q₀,q₁,…,qₙ with qᵢ₊₁=δ(qᵢ,aᵢ), return final qₙ and [λ(q₀,a₀),…,λ(qₙ₋₁,aₙ₋₁)].

**Lean formulation** (in its source module context):

```lean
structure MealyTransducer (Q I O : Type) [Fintype Q] [Fintype I] [Fintype O] where
  initial : Q
  next : Q → I → Q
  emit : Q → I → O
```

**Source:** [`Catalog.MealyTransducer`](../lean/Catalog/ReleaseSequenceModels.lean); consulted 2026-11-20.

**Scope:** model

**Interpretation:** For q₀,q₁,…,qₙ with qᵢ₊₁=δ(qᵢ,aᵢ), return final qₙ and [λ(q₀,a₀),…,λ(qₙ₋₁,aₙ₋₁)].

**Limits:** Q,I,O are finite exact-equality sets; q₀∈Q makes Q nonempty. I may be empty. O may be empty only when Q×I is empty. Input words are finite, including ε; run from any q, default q₀. Pure deterministic total steps, unbounded word length, no ε-input transitions, nondeterminism, time, effects or accepting states. A run on n inputs has n outputs. Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Typed total δ and λ with a designated initial state. Word execution is primitive recursion: run(q,ε)=(q,[]); run(q,a·xs) emits λ(q,a) then executes xs from δ(q,a).

**basisKind:** defined-structure

**basisScope:** Q,I,O are finite exact-equality sets; q₀∈Q makes Q nonempty. I may be empty. O may be empty only when Q×I is empty. Input words are finite, including ε; run from any q, default q₀. Pure deterministic total steps, unbounded word length, no ε-input transitions, nondeterminism, time, effects or accepting states. A run on n inputs has n outputs.

**verificationObligation:** Map exact carriers, equality, totality and the explicit profile conventions before use.; Model and theorem evidence does not establish a concrete software implementation refinement.

**reviewStatus:** Sourced model with separately registered Lean satisfaction and derived witnesses; verification requires fresh audit evidence.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-MealyTransducer-next"></a>

### next state

`urn:csabs:operation/MealyTransducer-next`

**signature:** next : Q×I→Q

**description:** Apply deterministic state transition.

**precondition:** Supplied machine; q∈Q and a∈I.

**postcondition:** Exactly δ(q,a).

**totality:** Total on the stated domain.

**source:** [MathWorks Stateflow: Overview of Mealy and Moore Machines](https://www.mathworks.com/help/stateflow/ug/overview-of-mealy-and-moore-machines.html); citation: R2026b, Semantics of Mealy and Moore Machines: next-state and output equations.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference

**sourceLocator:** Stateflow Semantics of Mealy and Moore Machines

**sourceNote:** Constructs a pure finite-word model from the documented transition/output signatures. Initial Moore emission is an explicit catalog convention, not a timing/effect model.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-MealyTransducer-emit"></a>

### output

`urn:csabs:operation/MealyTransducer-emit`

**signature:** emit : Q×I→O

**description:** Evaluate the machine output map.

**precondition:** A state and input.

**postcondition:** Exactly λ(q) or λ(q,a), according to this transition-output profile.

**totality:** Total on the stated domain.

**source:** [MathWorks Stateflow: Overview of Mealy and Moore Machines](https://www.mathworks.com/help/stateflow/ug/overview-of-mealy-and-moore-machines.html); citation: R2026b, Semantics of Mealy and Moore Machines: next-state and output equations.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference

**sourceLocator:** Stateflow Semantics of Mealy and Moore Machines

**sourceNote:** Constructs a pure finite-word model from the documented transition/output signatures. Initial Moore emission is an explicit catalog convention, not a timing/effect model.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-MealyTransducer-run"></a>

### run finite word

`urn:csabs:operation/MealyTransducer-run`

**signature:** run : Q×List(I)→Q×List(O)

**description:** Thread states through the word. Use q₀ for default execution.

**precondition:** q∈Q; finite input word.

**postcondition:** Return final state and n transition outputs.

**totality:** Total on the stated domain.

**source:** [MathWorks Stateflow: Overview of Mealy and Moore Machines](https://www.mathworks.com/help/stateflow/ug/overview-of-mealy-and-moore-machines.html); citation: R2026b, Semantics of Mealy and Moore Machines: next-state and output equations.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference

**sourceLocator:** Stateflow Semantics of Mealy and Moore Machines

**sourceNote:** Constructs a pure finite-word model from the documented transition/output signatures. Initial Moore emission is an explicit catalog convention, not a timing/effect model.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-MealyTransducer-defining-profile"></a>

### defining profile

`urn:csabs:axiom/MealyTransducer-defining-profile`

**statement:** Typed total δ and λ with a designated initial state. Word execution is primitive recursion: run(q,ε)=(q,[]); run(q,a·xs) emits λ(q,a) then executes xs from δ(q,a).

**formalStatement:** For q₀,q₁,…,qₙ with qᵢ₊₁=δ(qᵢ,aᵢ), return final qₙ and [λ(q₀,a₀),…,λ(qₙ₋₁,aₙ₋₁)].

**assumptions:** Q,I,O are finite exact-equality sets; q₀∈Q makes Q nonempty. I may be empty. O may be empty only when Q×I is empty. Input words are finite, including ε; run from any q, default q₀. Pure deterministic total steps, unbounded word length, no ε-input transitions, nondeterminism, time, effects or accepting states. A run on n inputs has n outputs.

**ruleRole:** defining-rule

**reviewStatus:** Structure constraints; satisfaction is established separately for the selected model.

**source:** [MathWorks Stateflow: Overview of Mealy and Moore Machines](https://www.mathworks.com/help/stateflow/ug/overview-of-mealy-and-moore-machines.html); citation: R2026b, Semantics of Mealy and Moore Machines: next-state and output equations.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference

**sourceLocator:** Stateflow Semantics of Mealy and Moore Machines

**sourceNote:** Constructs a pure finite-word model from the documented transition/output signatures. Initial Moore emission is an explicit catalog convention, not a timing/effect model.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-MealyTransducer-output-length"></a>

### output-length

`urn:csabs:law/MealyTransducer-output-length`

**statement:** Induct on inputs; each step prepends exactly one output.

**formalStatement:** ∀ {Q I O : Type} [Fintype Q] [Fintype I] [Fintype O] (m : Catalog.MealyTransducer Q I O) (q : Q) (xs : List I), (Catalog.mealyRun m q xs).2.length = xs.length

**assumptions:** Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality.

**dependsOn:** [defining profile](MealyTransducer.md#node-urn-csabs-axiom-MealyTransducer-defining-profile); [induction](Sequence.md#node-urn-csabs-axiom-Sequence-induction); [length-recursion](Sequence.md#node-urn-csabs-axiom-Sequence-length-recursion)

**proofSketch:** Induct on inputs; each step prepends exactly one output.

**reviewStatus:** Derived mathematical law; separately registered theorem supplies explicit proof evidence.

**source:** [MathWorks Stateflow: Overview of Mealy and Moore Machines](https://www.mathworks.com/help/stateflow/ug/overview-of-mealy-and-moore-machines.html); citation: R2026b, Semantics of Mealy and Moore Machines: next-state and output equations.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; Catalog release, sequence, transducer, schema, date and extension models and witnesses; path: lean/Catalog/ReleaseSequenceModels.lean; accessedOn: 2026-11-20; sourceRole: local-lean-formulation-and-proof

**sourceLocator:** Stateflow Semantics of Mealy and Moore Machines; Catalog.mealy_length

**sourceNote:** Derived for the explicit selected model. Induct on inputs; each step prepends exactly one output.

**provenanceKind:** derived

**ruleRole:** derived-law

<a id="node-urn-csabs-law-MealyTransducer-word-composition"></a>

### word-composition

`urn:csabs:law/MealyTransducer-word-composition`

**statement:** Induct on the first input word, threading its final state into the second run.

**formalStatement:** ∀ {Q I O : Type} [Fintype Q] [Fintype I] [Fintype O] (m : Catalog.MealyTransducer Q I O) (q : Q) (xs ys : List I), Catalog.mealyRun m q (xs ++ ys) = ((Catalog.mealyRun m (Catalog.mealyRun m q xs).1 ys).1, (Catalog.mealyRun m q xs).2 ++ (Catalog.mealyRun m (Catalog.mealyRun m q xs).1 ys).2)

**assumptions:** Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality.

**dependsOn:** [defining profile](MealyTransducer.md#node-urn-csabs-axiom-MealyTransducer-defining-profile); [induction](Sequence.md#node-urn-csabs-axiom-Sequence-induction); [concat-recursion](Sequence.md#node-urn-csabs-axiom-Sequence-concat-recursion)

**proofSketch:** Induct on the first input word, threading its final state into the second run.

**reviewStatus:** Derived mathematical law; separately registered theorem supplies explicit proof evidence.

**source:** [MathWorks Stateflow: Overview of Mealy and Moore Machines](https://www.mathworks.com/help/stateflow/ug/overview-of-mealy-and-moore-machines.html); citation: R2026b, Semantics of Mealy and Moore Machines: next-state and output equations.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; Catalog release, sequence, transducer, schema, date and extension models and witnesses; path: lean/Catalog/ReleaseSequenceModels.lean; accessedOn: 2026-11-20; sourceRole: local-lean-formulation-and-proof

**sourceLocator:** Stateflow Semantics of Mealy and Moore Machines; Catalog.mealy_append

**sourceNote:** Derived for the explicit selected model. Induct on the first input word, threading its final state into the second run.

**provenanceKind:** derived

**ruleRole:** derived-law

## Theorems

<a id="node-urn-csabs-theorem-MealyTransducer-run-equations"></a>

### run-equations

`urn:csabs:theorem/MealyTransducer-run-equations`

**statement:** Primitive recursion on finite input words realizes the selected total transition/output equations.

**formalStatement:** ∀ {Q I O : Type} [Fintype Q] [Fintype I] [Fintype O] (m : Catalog.MealyTransducer Q I O) (q : Q), Catalog.mealyRun m q [] = (q, []) ∧ (∀ a xs, Catalog.mealyRun m q (a :: xs) = ((Catalog.mealyRun m (m.next q a) xs).1, m.emit q a :: (Catalog.mealyRun m (m.next q a) xs).2))

**assumptions:** Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality.

**dependsOn:** [defining profile](MealyTransducer.md#node-urn-csabs-axiom-MealyTransducer-defining-profile)

**proofSketch:** Primitive recursion on finite input words realizes the selected total transition/output equations.

**reviewStatus:** Separately registered Lean witness; require fresh compiler and axiom audit for verified status.

**source:** [MathWorks Stateflow: Overview of Mealy and Moore Machines](https://www.mathworks.com/help/stateflow/ug/overview-of-mealy-and-moore-machines.html); citation: R2026b, Semantics of Mealy and Moore Machines: next-state and output equations.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; Catalog release, sequence, transducer, schema, date and extension models and witnesses; path: lean/Catalog/ReleaseSequenceModels.lean; accessedOn: 2026-11-20; sourceRole: local-lean-formulation-and-proof

**sourceLocator:** Stateflow Semantics of Mealy and Moore Machines; Catalog.mealy_equations

**sourceNote:** Derived for the explicit selected model. Primitive recursion on finite input words realizes the selected total transition/output equations.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {Q I O : Type} [Fintype Q] [Fintype I] [Fintype O] (m : Catalog.MealyTransducer Q I O) (q : Q), Catalog.mealyRun m q [] = (q, []) ∧ (∀ a xs, Catalog.mealyRun m q (a :: xs) = ((Catalog.mealyRun m (m.next q a) xs).1, m.emit q a :: (Catalog.mealyRun m (m.next q a) xs).2))
```

**Source:** [`Catalog.mealy_equations`](../lean/Catalog/ReleaseSequenceModels.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** Primitive recursion on finite input words realizes the selected total transition/output equations.

**Limits:** Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/MealyTransducer-defining-profile": "Proved constraint for the specified concrete interpretation or structural recursion; not a hypothesis asserting its own satisfaction. Primitive recursion on finite input words realizes the selected total transition/output equations."
}
```

<a id="node-urn-csabs-theorem-MealyTransducer-model-satisfaction"></a>

### model-satisfaction

`urn:csabs:theorem/MealyTransducer-model-satisfaction`

**statement:** Construct a two-state, two-input, two-output total machine and evaluate a nonempty word; no assumed machine laws.

**formalStatement:** Catalog.mealyRun Catalog.boolMealy false [true, false] = (false, [true, true])

**assumptions:** Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality.

**dependsOn:** [defining profile](MealyTransducer.md#node-urn-csabs-axiom-MealyTransducer-defining-profile)

**proofSketch:** Construct a two-state, two-input, two-output total machine and evaluate a nonempty word; no assumed machine laws.

**reviewStatus:** Separately registered Lean witness; require fresh compiler and axiom audit for verified status.

**source:** [MathWorks Stateflow: Overview of Mealy and Moore Machines](https://www.mathworks.com/help/stateflow/ug/overview-of-mealy-and-moore-machines.html); citation: R2026b, Semantics of Mealy and Moore Machines: next-state and output equations.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; Catalog release, sequence, transducer, schema, date and extension models and witnesses; path: lean/Catalog/ReleaseSequenceModels.lean; accessedOn: 2026-11-20; sourceRole: local-lean-formulation-and-proof

**sourceLocator:** Stateflow Semantics of Mealy and Moore Machines; Catalog.mealy_model_satisfaction

**sourceNote:** Derived for the explicit selected model. Construct a two-state, two-input, two-output total machine and evaluate a nonempty word; no assumed machine laws.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
Catalog.mealyRun Catalog.boolMealy false [true, false] = (false, [true, true])
```

**Source:** [`Catalog.mealy_model_satisfaction`](../lean/Catalog/ReleaseSequenceModels.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** Construct a two-state, two-input, two-output total machine and evaluate a nonempty word; no assumed machine laws.

**Limits:** Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/MealyTransducer-defining-profile": "Proved constraint for the specified concrete interpretation or structural recursion; not a hypothesis asserting its own satisfaction. Construct a two-state, two-input, two-output total machine and evaluate a nonempty word; no assumed machine laws."
}
```

<a id="node-urn-csabs-theorem-MealyTransducer-output-length"></a>

### output-length

`urn:csabs:theorem/MealyTransducer-output-length`

**statement:** Induct on inputs; each step prepends exactly one output.

**formalStatement:** ∀ {Q I O : Type} [Fintype Q] [Fintype I] [Fintype O] (m : Catalog.MealyTransducer Q I O) (q : Q) (xs : List I), (Catalog.mealyRun m q xs).2.length = xs.length

**assumptions:** Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality.

**dependsOn:** [defining profile](MealyTransducer.md#node-urn-csabs-axiom-MealyTransducer-defining-profile); [induction](Sequence.md#node-urn-csabs-axiom-Sequence-induction); [length-recursion](Sequence.md#node-urn-csabs-axiom-Sequence-length-recursion)

**proofSketch:** Induct on inputs; each step prepends exactly one output.

**reviewStatus:** Separately registered Lean witness; require fresh compiler and axiom audit for verified status.

**source:** [MathWorks Stateflow: Overview of Mealy and Moore Machines](https://www.mathworks.com/help/stateflow/ug/overview-of-mealy-and-moore-machines.html); citation: R2026b, Semantics of Mealy and Moore Machines: next-state and output equations.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; Catalog release, sequence, transducer, schema, date and extension models and witnesses; path: lean/Catalog/ReleaseSequenceModels.lean; accessedOn: 2026-11-20; sourceRole: local-lean-formulation-and-proof

**sourceLocator:** Stateflow Semantics of Mealy and Moore Machines; Catalog.mealy_length

**sourceNote:** Derived for the explicit selected model. Induct on inputs; each step prepends exactly one output.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {Q I O : Type} [Fintype Q] [Fintype I] [Fintype O] (m : Catalog.MealyTransducer Q I O) (q : Q) (xs : List I), (Catalog.mealyRun m q xs).2.length = xs.length
```

**Source:** [`Catalog.mealy_length`](../lean/Catalog/ReleaseSequenceModels.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** Induct on inputs; each step prepends exactly one output.

**Limits:** Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/MealyTransducer-defining-profile": "Proved constraint for the specified concrete interpretation or structural recursion; not a hypothesis asserting its own satisfaction. Induct on inputs; each step prepends exactly one output.",
  "urn:csabs:axiom/Sequence-induction": "Existing finite-list induction, concatenation or length premise, instantiated with exact List equality; no editing behavior is inferred from it.",
  "urn:csabs:axiom/Sequence-length-recursion": "Existing finite-list induction, concatenation or length premise, instantiated with exact List equality; no editing behavior is inferred from it."
}
```

<a id="node-urn-csabs-theorem-MealyTransducer-word-composition"></a>

### word-composition

`urn:csabs:theorem/MealyTransducer-word-composition`

**statement:** Induct on the first input word, threading its final state into the second run.

**formalStatement:** ∀ {Q I O : Type} [Fintype Q] [Fintype I] [Fintype O] (m : Catalog.MealyTransducer Q I O) (q : Q) (xs ys : List I), Catalog.mealyRun m q (xs ++ ys) = ((Catalog.mealyRun m (Catalog.mealyRun m q xs).1 ys).1, (Catalog.mealyRun m q xs).2 ++ (Catalog.mealyRun m (Catalog.mealyRun m q xs).1 ys).2)

**assumptions:** Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality.

**dependsOn:** [defining profile](MealyTransducer.md#node-urn-csabs-axiom-MealyTransducer-defining-profile); [induction](Sequence.md#node-urn-csabs-axiom-Sequence-induction); [concat-recursion](Sequence.md#node-urn-csabs-axiom-Sequence-concat-recursion)

**proofSketch:** Induct on the first input word, threading its final state into the second run.

**reviewStatus:** Separately registered Lean witness; require fresh compiler and axiom audit for verified status.

**source:** [MathWorks Stateflow: Overview of Mealy and Moore Machines](https://www.mathworks.com/help/stateflow/ug/overview-of-mealy-and-moore-machines.html); citation: R2026b, Semantics of Mealy and Moore Machines: next-state and output equations.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; Catalog release, sequence, transducer, schema, date and extension models and witnesses; path: lean/Catalog/ReleaseSequenceModels.lean; accessedOn: 2026-11-20; sourceRole: local-lean-formulation-and-proof

**sourceLocator:** Stateflow Semantics of Mealy and Moore Machines; Catalog.mealy_append

**sourceNote:** Derived for the explicit selected model. Induct on the first input word, threading its final state into the second run.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {Q I O : Type} [Fintype Q] [Fintype I] [Fintype O] (m : Catalog.MealyTransducer Q I O) (q : Q) (xs ys : List I), Catalog.mealyRun m q (xs ++ ys) = ((Catalog.mealyRun m (Catalog.mealyRun m q xs).1 ys).1, (Catalog.mealyRun m q xs).2 ++ (Catalog.mealyRun m (Catalog.mealyRun m q xs).1 ys).2)
```

**Source:** [`Catalog.mealy_append`](../lean/Catalog/ReleaseSequenceModels.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** Induct on the first input word, threading its final state into the second run.

**Limits:** Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/MealyTransducer-defining-profile": "Proved constraint for the specified concrete interpretation or structural recursion; not a hypothesis asserting its own satisfaction. Induct on the first input word, threading its final state into the second run.",
  "urn:csabs:axiom/Sequence-concat-recursion": "Existing finite-list induction, concatenation or length premise, instantiated with exact List equality; no editing behavior is inferred from it.",
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
    "id": "urn:csabs:concept/MealyTransducer",
    "type": "Concept",
    "shortForm": "MealyTransducer",
    "fullName": "Mealy deterministic finite sequential transducer",
    "synonyms": [
      "Mealy machine",
      "Transition-output finite sequential transducer"
    ],
    "category": [
      "urn:csabs:category/behavior"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "definition": "A deterministic finite-state input/output machine with total next-state and output maps; outputs are attached to state/input transitions.",
    "notation": "(Q,I,O,q₀,δ,λ); δ:Q×I→Q; λ:Q×I→O",
    "requiresConcept": [
      "urn:csabs:concept/Sequence",
      "urn:csabs:concept/Function"
    ],
    "relatedConcept": [
      "urn:csabs:concept/DFA",
      "urn:csabs:concept/LabelledTransitionSystem",
      "urn:csabs:concept/MooreTransducer"
    ],
    "axiomBasis": "Typed total δ and λ with a designated initial state. Word execution is primitive recursion: run(q,ε)=(q,[]); run(q,a·xs) emits λ(q,a) then executes xs from δ(q,a).",
    "basisKind": "defined-structure",
    "basisScope": "Q,I,O are finite exact-equality sets; q₀∈Q makes Q nonempty. I may be empty. O may be empty only when Q×I is empty. Input words are finite, including ε; run from any q, default q₀. Pure deterministic total steps, unbounded word length, no ε-input transitions, nondeterminism, time, effects or accepting states. A run on n inputs has n outputs.",
    "mathematicalFormulation": "For q₀,q₁,…,qₙ with qᵢ₊₁=δ(qᵢ,aᵢ), return final qₙ and [λ(q₀,a₀),…,λ(qₙ₋₁,aₙ₋₁)].",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Sourced model with separately registered Lean satisfaction and derived witnesses; verification requires fresh audit evidence.",
    "verificationObligation": [
      "Map exact carriers, equality, totality and the explicit profile conventions before use.",
      "Model and theorem evidence does not establish a concrete software implementation refinement."
    ],
    "hasOperation": [
      "urn:csabs:operation/MealyTransducer-next",
      "urn:csabs:operation/MealyTransducer-emit",
      "urn:csabs:operation/MealyTransducer-run"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/MealyTransducer-defining-profile"
    ],
    "hasLaw": [
      "urn:csabs:law/MealyTransducer-output-length",
      "urn:csabs:law/MealyTransducer-word-composition"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/MealyTransducer-run-equations",
      "urn:csabs:theorem/MealyTransducer-model-satisfaction",
      "urn:csabs:theorem/MealyTransducer-output-length",
      "urn:csabs:theorem/MealyTransducer-word-composition"
    ],
    "source": [
      "urn:csabs:source/seven-transducer"
    ],
    "sourceLocator": "Stateflow Semantics of Mealy and Moore Machines",
    "sourceNote": "Constructs a pure finite-word model from the documented transition/output signatures. Initial Moore emission is an explicit catalog convention, not a timing/effect model.",
    "provenanceKind": "adapted",
    "leanFormulation": "structure MealyTransducer (Q I O : Type) [Fintype Q] [Fintype I] [Fintype O] where\n  initial : Q\n  next : Q → I → Q\n  emit : Q → I → O",
    "formulationSource": "urn:csabs:source/seven-lean-models",
    "formulationLocator": "Catalog.MealyTransducer",
    "formulationScope": "model",
    "leanModelMapping": "For q₀,q₁,…,qₙ with qᵢ₊₁=δ(qᵢ,aᵢ), return final qₙ and [λ(q₀,a₀),…,λ(qₙ₋₁,aₙ₋₁)].",
    "leanModelLimitations": "Q,I,O are finite exact-equality sets; q₀∈Q makes Q nonempty. I may be empty. O may be empty only when Q×I is empty. Input words are finite, including ε; run from any q, default q₀. Pure deterministic total steps, unbounded word length, no ε-input transitions, nondeterminism, time, effects or accepting states. A run on n inputs has n outputs. Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit."
  },
  {
    "id": "urn:csabs:operation/MealyTransducer-next",
    "type": "Operation",
    "concept": "urn:csabs:concept/MealyTransducer",
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
    "id": "urn:csabs:operation/MealyTransducer-emit",
    "type": "Operation",
    "concept": "urn:csabs:concept/MealyTransducer",
    "name": "output",
    "signature": "emit : Q×I→O",
    "description": "Evaluate the machine output map.",
    "precondition": "A state and input.",
    "postcondition": "Exactly λ(q) or λ(q,a), according to this transition-output profile.",
    "totality": "Total on the stated domain.",
    "source": [
      "urn:csabs:source/seven-transducer"
    ],
    "sourceLocator": "Stateflow Semantics of Mealy and Moore Machines",
    "sourceNote": "Constructs a pure finite-word model from the documented transition/output signatures. Initial Moore emission is an explicit catalog convention, not a timing/effect model.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/MealyTransducer-run",
    "type": "Operation",
    "concept": "urn:csabs:concept/MealyTransducer",
    "name": "run finite word",
    "signature": "run : Q×List(I)→Q×List(O)",
    "description": "Thread states through the word. Use q₀ for default execution.",
    "precondition": "q∈Q; finite input word.",
    "postcondition": "Return final state and n transition outputs.",
    "totality": "Total on the stated domain.",
    "source": [
      "urn:csabs:source/seven-transducer"
    ],
    "sourceLocator": "Stateflow Semantics of Mealy and Moore Machines",
    "sourceNote": "Constructs a pure finite-word model from the documented transition/output signatures. Initial Moore emission is an explicit catalog convention, not a timing/effect model.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/MealyTransducer-defining-profile",
    "type": "Axiom",
    "name": "defining profile",
    "statement": "Typed total δ and λ with a designated initial state. Word execution is primitive recursion: run(q,ε)=(q,[]); run(q,a·xs) emits λ(q,a) then executes xs from δ(q,a).",
    "formalStatement": "For q₀,q₁,…,qₙ with qᵢ₊₁=δ(qᵢ,aᵢ), return final qₙ and [λ(q₀,a₀),…,λ(qₙ₋₁,aₙ₋₁)].",
    "assumptions": [
      "Q,I,O are finite exact-equality sets; q₀∈Q makes Q nonempty. I may be empty. O may be empty only when Q×I is empty. Input words are finite, including ε; run from any q, default q₀. Pure deterministic total steps, unbounded word length, no ε-input transitions, nondeterminism, time, effects or accepting states. A run on n inputs has n outputs."
    ],
    "appliesTo": [
      "urn:csabs:concept/MealyTransducer"
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
    "id": "urn:csabs:law/MealyTransducer-output-length",
    "type": "Law",
    "name": "output-length",
    "statement": "Induct on inputs; each step prepends exactly one output.",
    "formalStatement": "∀ {Q I O : Type} [Fintype Q] [Fintype I] [Fintype O] (m : Catalog.MealyTransducer Q I O) (q : Q) (xs : List I), (Catalog.mealyRun m q xs).2.length = xs.length",
    "assumptions": [
      "Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/MealyTransducer"
    ],
    "dependsOn": [
      "urn:csabs:axiom/MealyTransducer-defining-profile",
      "urn:csabs:axiom/Sequence-induction",
      "urn:csabs:axiom/Sequence-length-recursion"
    ],
    "proofSketch": "Induct on inputs; each step prepends exactly one output.",
    "reviewStatus": "Derived mathematical law; separately registered theorem supplies explicit proof evidence.",
    "source": [
      "urn:csabs:source/seven-transducer",
      "urn:csabs:source/seven-lean-models"
    ],
    "sourceLocator": "Stateflow Semantics of Mealy and Moore Machines; Catalog.mealy_length",
    "sourceNote": "Derived for the explicit selected model. Induct on inputs; each step prepends exactly one output.",
    "provenanceKind": "derived",
    "ruleRole": "derived-law"
  },
  {
    "id": "urn:csabs:law/MealyTransducer-word-composition",
    "type": "Law",
    "name": "word-composition",
    "statement": "Induct on the first input word, threading its final state into the second run.",
    "formalStatement": "∀ {Q I O : Type} [Fintype Q] [Fintype I] [Fintype O] (m : Catalog.MealyTransducer Q I O) (q : Q) (xs ys : List I), Catalog.mealyRun m q (xs ++ ys) = ((Catalog.mealyRun m (Catalog.mealyRun m q xs).1 ys).1, (Catalog.mealyRun m q xs).2 ++ (Catalog.mealyRun m (Catalog.mealyRun m q xs).1 ys).2)",
    "assumptions": [
      "Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/MealyTransducer"
    ],
    "dependsOn": [
      "urn:csabs:axiom/MealyTransducer-defining-profile",
      "urn:csabs:axiom/Sequence-induction",
      "urn:csabs:axiom/Sequence-concat-recursion"
    ],
    "proofSketch": "Induct on the first input word, threading its final state into the second run.",
    "reviewStatus": "Derived mathematical law; separately registered theorem supplies explicit proof evidence.",
    "source": [
      "urn:csabs:source/seven-transducer",
      "urn:csabs:source/seven-lean-models"
    ],
    "sourceLocator": "Stateflow Semantics of Mealy and Moore Machines; Catalog.mealy_append",
    "sourceNote": "Derived for the explicit selected model. Induct on the first input word, threading its final state into the second run.",
    "provenanceKind": "derived",
    "ruleRole": "derived-law"
  },
  {
    "id": "urn:csabs:theorem/MealyTransducer-run-equations",
    "type": "Theorem",
    "name": "run-equations",
    "statement": "Primitive recursion on finite input words realizes the selected total transition/output equations.",
    "formalStatement": "∀ {Q I O : Type} [Fintype Q] [Fintype I] [Fintype O] (m : Catalog.MealyTransducer Q I O) (q : Q), Catalog.mealyRun m q [] = (q, []) ∧ (∀ a xs, Catalog.mealyRun m q (a :: xs) = ((Catalog.mealyRun m (m.next q a) xs).1, m.emit q a :: (Catalog.mealyRun m (m.next q a) xs).2))",
    "assumptions": [
      "Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/MealyTransducer"
    ],
    "dependsOn": [
      "urn:csabs:axiom/MealyTransducer-defining-profile"
    ],
    "proofSketch": "Primitive recursion on finite input words realizes the selected total transition/output equations.",
    "reviewStatus": "Separately registered Lean witness; require fresh compiler and axiom audit for verified status.",
    "source": [
      "urn:csabs:source/seven-transducer",
      "urn:csabs:source/seven-lean-models"
    ],
    "sourceLocator": "Stateflow Semantics of Mealy and Moore Machines; Catalog.mealy_equations",
    "sourceNote": "Derived for the explicit selected model. Primitive recursion on finite input words realizes the selected total transition/output equations.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {Q I O : Type} [Fintype Q] [Fintype I] [Fintype O] (m : Catalog.MealyTransducer Q I O) (q : Q), Catalog.mealyRun m q [] = (q, []) ∧ (∀ a xs, Catalog.mealyRun m q (a :: xs) = ((Catalog.mealyRun m (m.next q a) xs).1, m.emit q a :: (Catalog.mealyRun m (m.next q a) xs).2))",
    "formulationSource": "urn:csabs:source/seven-lean-models",
    "formulationLocator": "Catalog.mealy_equations",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Primitive recursion on finite input words realizes the selected total transition/output equations.",
    "leanModelLimitations": "Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/MealyTransducer-defining-profile\": \"Proved constraint for the specified concrete interpretation or structural recursion; not a hypothesis asserting its own satisfaction. Primitive recursion on finite input words realizes the selected total transition/output equations.\"}"
  },
  {
    "id": "urn:csabs:theorem/MealyTransducer-model-satisfaction",
    "type": "Theorem",
    "name": "model-satisfaction",
    "statement": "Construct a two-state, two-input, two-output total machine and evaluate a nonempty word; no assumed machine laws.",
    "formalStatement": "Catalog.mealyRun Catalog.boolMealy false [true, false] = (false, [true, true])",
    "assumptions": [
      "Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/MealyTransducer"
    ],
    "dependsOn": [
      "urn:csabs:axiom/MealyTransducer-defining-profile"
    ],
    "proofSketch": "Construct a two-state, two-input, two-output total machine and evaluate a nonempty word; no assumed machine laws.",
    "reviewStatus": "Separately registered Lean witness; require fresh compiler and axiom audit for verified status.",
    "source": [
      "urn:csabs:source/seven-transducer",
      "urn:csabs:source/seven-lean-models"
    ],
    "sourceLocator": "Stateflow Semantics of Mealy and Moore Machines; Catalog.mealy_model_satisfaction",
    "sourceNote": "Derived for the explicit selected model. Construct a two-state, two-input, two-output total machine and evaluate a nonempty word; no assumed machine laws.",
    "provenanceKind": "derived",
    "leanFormulation": "Catalog.mealyRun Catalog.boolMealy false [true, false] = (false, [true, true])",
    "formulationSource": "urn:csabs:source/seven-lean-models",
    "formulationLocator": "Catalog.mealy_model_satisfaction",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Construct a two-state, two-input, two-output total machine and evaluate a nonempty word; no assumed machine laws.",
    "leanModelLimitations": "Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/MealyTransducer-defining-profile\": \"Proved constraint for the specified concrete interpretation or structural recursion; not a hypothesis asserting its own satisfaction. Construct a two-state, two-input, two-output total machine and evaluate a nonempty word; no assumed machine laws.\"}"
  },
  {
    "id": "urn:csabs:theorem/MealyTransducer-output-length",
    "type": "Theorem",
    "name": "output-length",
    "statement": "Induct on inputs; each step prepends exactly one output.",
    "formalStatement": "∀ {Q I O : Type} [Fintype Q] [Fintype I] [Fintype O] (m : Catalog.MealyTransducer Q I O) (q : Q) (xs : List I), (Catalog.mealyRun m q xs).2.length = xs.length",
    "assumptions": [
      "Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/MealyTransducer"
    ],
    "dependsOn": [
      "urn:csabs:axiom/MealyTransducer-defining-profile",
      "urn:csabs:axiom/Sequence-induction",
      "urn:csabs:axiom/Sequence-length-recursion"
    ],
    "proofSketch": "Induct on inputs; each step prepends exactly one output.",
    "reviewStatus": "Separately registered Lean witness; require fresh compiler and axiom audit for verified status.",
    "source": [
      "urn:csabs:source/seven-transducer",
      "urn:csabs:source/seven-lean-models"
    ],
    "sourceLocator": "Stateflow Semantics of Mealy and Moore Machines; Catalog.mealy_length",
    "sourceNote": "Derived for the explicit selected model. Induct on inputs; each step prepends exactly one output.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {Q I O : Type} [Fintype Q] [Fintype I] [Fintype O] (m : Catalog.MealyTransducer Q I O) (q : Q) (xs : List I), (Catalog.mealyRun m q xs).2.length = xs.length",
    "formulationSource": "urn:csabs:source/seven-lean-models",
    "formulationLocator": "Catalog.mealy_length",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Induct on inputs; each step prepends exactly one output.",
    "leanModelLimitations": "Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/MealyTransducer-defining-profile\": \"Proved constraint for the specified concrete interpretation or structural recursion; not a hypothesis asserting its own satisfaction. Induct on inputs; each step prepends exactly one output.\", \"urn:csabs:axiom/Sequence-induction\": \"Existing finite-list induction, concatenation or length premise, instantiated with exact List equality; no editing behavior is inferred from it.\", \"urn:csabs:axiom/Sequence-length-recursion\": \"Existing finite-list induction, concatenation or length premise, instantiated with exact List equality; no editing behavior is inferred from it.\"}"
  },
  {
    "id": "urn:csabs:theorem/MealyTransducer-word-composition",
    "type": "Theorem",
    "name": "word-composition",
    "statement": "Induct on the first input word, threading its final state into the second run.",
    "formalStatement": "∀ {Q I O : Type} [Fintype Q] [Fintype I] [Fintype O] (m : Catalog.MealyTransducer Q I O) (q : Q) (xs ys : List I), Catalog.mealyRun m q (xs ++ ys) = ((Catalog.mealyRun m (Catalog.mealyRun m q xs).1 ys).1, (Catalog.mealyRun m q xs).2 ++ (Catalog.mealyRun m (Catalog.mealyRun m q xs).1 ys).2)",
    "assumptions": [
      "Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/MealyTransducer"
    ],
    "dependsOn": [
      "urn:csabs:axiom/MealyTransducer-defining-profile",
      "urn:csabs:axiom/Sequence-induction",
      "urn:csabs:axiom/Sequence-concat-recursion"
    ],
    "proofSketch": "Induct on the first input word, threading its final state into the second run.",
    "reviewStatus": "Separately registered Lean witness; require fresh compiler and axiom audit for verified status.",
    "source": [
      "urn:csabs:source/seven-transducer",
      "urn:csabs:source/seven-lean-models"
    ],
    "sourceLocator": "Stateflow Semantics of Mealy and Moore Machines; Catalog.mealy_append",
    "sourceNote": "Derived for the explicit selected model. Induct on the first input word, threading its final state into the second run.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {Q I O : Type} [Fintype Q] [Fintype I] [Fintype O] (m : Catalog.MealyTransducer Q I O) (q : Q) (xs ys : List I), Catalog.mealyRun m q (xs ++ ys) = ((Catalog.mealyRun m (Catalog.mealyRun m q xs).1 ys).1, (Catalog.mealyRun m q xs).2 ++ (Catalog.mealyRun m (Catalog.mealyRun m q xs).1 ys).2)",
    "formulationSource": "urn:csabs:source/seven-lean-models",
    "formulationLocator": "Catalog.mealy_append",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Induct on the first input word, threading its final state into the second run.",
    "leanModelLimitations": "Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/MealyTransducer-defining-profile\": \"Proved constraint for the specified concrete interpretation or structural recursion; not a hypothesis asserting its own satisfaction. Induct on the first input word, threading its final state into the second run.\", \"urn:csabs:axiom/Sequence-concat-recursion\": \"Existing finite-list induction, concatenation or length premise, instantiated with exact List equality; no editing behavior is inferred from it.\", \"urn:csabs:axiom/Sequence-induction\": \"Existing finite-list induction, concatenation or length premise, instantiated with exact List equality; no editing behavior is inferred from it.\"}"
  }
]
```
<!-- graph-record:end -->
