# Ordered first-hit decision table

A finite ordered list of total Boolean guards and outcomes; evaluation returns the outcome of the first true guard and none when every guard is false. Overlapping guards are permitted.

**Notation:** R=[(gᵢ,vᵢ)]; gᵢ:X→Bool; eval:R×X→Option(V)

**Stable ID:** `urn:csabs:concept/FirstHitDecisionTable`

**Categories:** Relational data modelling

**Kind:** semantic-model

**Prerequisites:** [Finite sequence (List datatype)](Sequence.md), [Total function](Function.md)

**Related concepts:** [Finite unique-hit decision table](DecisionTable.md)

## Mathematical formulation

eval(R,x)=some(vᵢ) for i=min{j<|R| | gⱼ(x)=true}, or none when that set is empty.

**Lean formulation** (in its source module context):

```lean
abbrev FirstHitDecisionTable (X V : Type) := List ((X → Bool) × V)
```

**Source:** [`Catalog.FirstHitDecisionTable`](../lean/Catalog/ReleaseSequenceModels.lean); consulted 2026-11-20.

**Scope:** model

**Interpretation:** eval(R,x)=some(vᵢ) for i=min{j<|R| | gⱼ(x)=true}, or none when that set is empty.

**Limits:** X,V arbitrary exact-equality carriers; rules retain list position even when repeated. Guards are total and pure. Empty table yields none, and no-match differs from any returned outcome. No implicit default, unique-hit constraint, output-priority sorting, effects, guard exceptions, or inferred coverage/feasibility. A final always-true rule explicitly encodes a default. Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** eval([],x)=none; eval((g,v)::rs,x)=some(v) if g(x)=true, otherwise eval(rs,x). Finite order is semantically significant.

**basisKind:** defined-structure

**basisScope:** X,V arbitrary exact-equality carriers; rules retain list position even when repeated. Guards are total and pure. Empty table yields none, and no-match differs from any returned outcome. No implicit default, unique-hit constraint, output-priority sorting, effects, guard exceptions, or inferred coverage/feasibility. A final always-true rule explicitly encodes a default.

**verificationObligation:** Map exact carriers, equality, totality and the explicit profile conventions before use.; Model and theorem evidence does not establish a concrete software implementation refinement.

**reviewStatus:** Sourced model with separately registered Lean satisfaction and derived witnesses; verification requires fresh audit evidence.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-FirstHitDecisionTable-evaluate"></a>

### first-hit evaluation

`urn:csabs:operation/FirstHitDecisionTable-evaluate`

**signature:** eval : List((X→Bool)×V)×X→Option(V)

**description:** Evaluate rules in list order and stop at the first true guard.

**precondition:** Guards are pure total Boolean functions; no unique-hit requirement.

**postcondition:** some(v) for the earliest matching rule, otherwise none.

**totality:** Total on the stated domain.

**source:** [OMG Decision Model and Notation 1.5](https://www.omg.org/spec/DMN/1.5/PDF); citation: Decision Model and Notation v1.5, §8.2.11.1, FIRST hit policy.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference

**sourceLocator:** DMN 1.5 §8.2.11.1 FIRST hit policy

**sourceNote:** Adapts FIRST to an ordered list with explicit Option no-match; DMN output expressions are represented by fixed outcomes. For input-dependent outcomes instantiate V as a suitable total outcome function with an explicit application mapping.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-FirstHitDecisionTable-defining-profile"></a>

### defining profile

`urn:csabs:axiom/FirstHitDecisionTable-defining-profile`

**statement:** eval([],x)=none; eval((g,v)::rs,x)=some(v) if g(x)=true, otherwise eval(rs,x). Finite order is semantically significant.

**formalStatement:** eval(R,x)=some(vᵢ) for i=min{j<|R| | gⱼ(x)=true}, or none when that set is empty.

**assumptions:** X,V arbitrary exact-equality carriers; rules retain list position even when repeated. Guards are total and pure. Empty table yields none, and no-match differs from any returned outcome. No implicit default, unique-hit constraint, output-priority sorting, effects, guard exceptions, or inferred coverage/feasibility. A final always-true rule explicitly encodes a default.

**ruleRole:** defining-rule

**reviewStatus:** Structure constraints; satisfaction is established separately for the selected model.

**source:** [OMG Decision Model and Notation 1.5](https://www.omg.org/spec/DMN/1.5/PDF); citation: Decision Model and Notation v1.5, §8.2.11.1, FIRST hit policy.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference

**sourceLocator:** DMN 1.5 §8.2.11.1 FIRST hit policy

**sourceNote:** Adapts FIRST to an ordered list with explicit Option no-match; DMN output expressions are represented by fixed outcomes. For input-dependent outcomes instantiate V as a suitable total outcome function with an explicit application mapping.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-FirstHitDecisionTable-ordered-append"></a>

### ordered-append

`urn:csabs:law/FirstHitDecisionTable-ordered-append`

**statement:** Induct on the left table. A matching rule suppresses all later rules; otherwise recur.

**formalStatement:** ∀ {X V : Type} (a b : Catalog.FirstHitDecisionTable X V) (x : X), Catalog.firstHit (a ++ b) x = (Catalog.firstHit a x).or (Catalog.firstHit b x)

**assumptions:** Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality.

**dependsOn:** [defining profile](FirstHitDecisionTable.md#node-urn-csabs-axiom-FirstHitDecisionTable-defining-profile); [induction](Sequence.md#node-urn-csabs-axiom-Sequence-induction); [concat-recursion](Sequence.md#node-urn-csabs-axiom-Sequence-concat-recursion)

**proofSketch:** Induct on the left table. A matching rule suppresses all later rules; otherwise recur.

**reviewStatus:** Derived mathematical law; separately registered theorem supplies explicit proof evidence.

**source:** [OMG Decision Model and Notation 1.5](https://www.omg.org/spec/DMN/1.5/PDF); citation: Decision Model and Notation v1.5, §8.2.11.1, FIRST hit policy.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; Catalog release, sequence, transducer, schema, date and extension models and witnesses; path: lean/Catalog/ReleaseSequenceModels.lean; accessedOn: 2026-11-20; sourceRole: local-lean-formulation-and-proof

**sourceLocator:** DMN 1.5 §8.2.11.1 FIRST hit policy; Catalog.first_hit_append

**sourceNote:** Derived for the explicit selected model. Induct on the left table. A matching rule suppresses all later rules; otherwise recur.

**provenanceKind:** derived

**ruleRole:** derived-law

<a id="node-urn-csabs-law-FirstHitDecisionTable-no-match"></a>

### no-match

`urn:csabs:law/FirstHitDecisionTable-no-match`

**statement:** Induct on the ordered rule list and split on its head guard.

**formalStatement:** ∀ {X V : Type} (rs : Catalog.FirstHitDecisionTable X V) (x : X), Catalog.firstHit rs x = none ↔ ∀ r ∈ rs, r.1 x = false

**assumptions:** Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality.

**dependsOn:** [defining profile](FirstHitDecisionTable.md#node-urn-csabs-axiom-FirstHitDecisionTable-defining-profile); [induction](Sequence.md#node-urn-csabs-axiom-Sequence-induction)

**proofSketch:** Induct on the ordered rule list and split on its head guard.

**reviewStatus:** Derived mathematical law; separately registered theorem supplies explicit proof evidence.

**source:** [OMG Decision Model and Notation 1.5](https://www.omg.org/spec/DMN/1.5/PDF); citation: Decision Model and Notation v1.5, §8.2.11.1, FIRST hit policy.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; Catalog release, sequence, transducer, schema, date and extension models and witnesses; path: lean/Catalog/ReleaseSequenceModels.lean; accessedOn: 2026-11-20; sourceRole: local-lean-formulation-and-proof

**sourceLocator:** DMN 1.5 §8.2.11.1 FIRST hit policy; Catalog.first_hit_none

**sourceNote:** Derived for the explicit selected model. Induct on the ordered rule list and split on its head guard.

**provenanceKind:** derived

**ruleRole:** derived-law

<a id="node-urn-csabs-law-FirstHitDecisionTable-first-match-selection"></a>

### first-match-selection

`urn:csabs:law/FirstHitDecisionTable-first-match-selection`

**statement:** All preceding rules yield none; append composition then selects the current true guard independently of later rules.

**formalStatement:** ∀ {X V : Type} (before after : Catalog.FirstHitDecisionTable X V) (g : X → Bool) (v : V) (x : X), (∀ r ∈ before, r.1 x = false) → g x = true → Catalog.firstHit (before ++ (g,v) :: after) x = some v

**assumptions:** Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality.

**dependsOn:** [defining profile](FirstHitDecisionTable.md#node-urn-csabs-axiom-FirstHitDecisionTable-defining-profile); [induction](Sequence.md#node-urn-csabs-axiom-Sequence-induction); [concat-recursion](Sequence.md#node-urn-csabs-axiom-Sequence-concat-recursion)

**proofSketch:** All preceding rules yield none; append composition then selects the current true guard independently of later rules.

**reviewStatus:** Derived mathematical law; separately registered theorem supplies explicit proof evidence.

**source:** [OMG Decision Model and Notation 1.5](https://www.omg.org/spec/DMN/1.5/PDF); citation: Decision Model and Notation v1.5, §8.2.11.1, FIRST hit policy.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; Catalog release, sequence, transducer, schema, date and extension models and witnesses; path: lean/Catalog/ReleaseSequenceModels.lean; accessedOn: 2026-11-20; sourceRole: local-lean-formulation-and-proof

**sourceLocator:** DMN 1.5 §8.2.11.1 FIRST hit policy; Catalog.first_hit_selection

**sourceNote:** Derived for the explicit selected model. All preceding rules yield none; append composition then selects the current true guard independently of later rules.

**provenanceKind:** derived

**ruleRole:** derived-law

## Theorems

<a id="node-urn-csabs-theorem-FirstHitDecisionTable-model-satisfaction"></a>

### model-satisfaction

`urn:csabs:theorem/FirstHitDecisionTable-model-satisfaction`

**statement:** Compute overlapping guards and the empty table; the first rule wins even when a later guard is also true.

**formalStatement:** Catalog.firstHit [(fun _ : Bool => true, 1), (fun _ => true, 2)] false = some 1 ∧ Catalog.firstHit ([] : Catalog.FirstHitDecisionTable Bool Nat) false = none

**assumptions:** Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality.

**dependsOn:** [defining profile](FirstHitDecisionTable.md#node-urn-csabs-axiom-FirstHitDecisionTable-defining-profile)

**proofSketch:** Compute overlapping guards and the empty table; the first rule wins even when a later guard is also true.

**reviewStatus:** Separately registered Lean witness; require fresh compiler and axiom audit for verified status.

**source:** [OMG Decision Model and Notation 1.5](https://www.omg.org/spec/DMN/1.5/PDF); citation: Decision Model and Notation v1.5, §8.2.11.1, FIRST hit policy.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; Catalog release, sequence, transducer, schema, date and extension models and witnesses; path: lean/Catalog/ReleaseSequenceModels.lean; accessedOn: 2026-11-20; sourceRole: local-lean-formulation-and-proof

**sourceLocator:** DMN 1.5 §8.2.11.1 FIRST hit policy; Catalog.first_hit_model_satisfaction

**sourceNote:** Derived for the explicit selected model. Compute overlapping guards and the empty table; the first rule wins even when a later guard is also true.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
Catalog.firstHit [(fun _ : Bool => true, 1), (fun _ => true, 2)] false = some 1 ∧ Catalog.firstHit ([] : Catalog.FirstHitDecisionTable Bool Nat) false = none
```

**Source:** [`Catalog.first_hit_model_satisfaction`](../lean/Catalog/ReleaseSequenceModels.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** Compute overlapping guards and the empty table; the first rule wins even when a later guard is also true.

**Limits:** Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/FirstHitDecisionTable-defining-profile": "Proved constraint for the specified concrete interpretation or structural recursion; not a hypothesis asserting its own satisfaction. Compute overlapping guards and the empty table; the first rule wins even when a later guard is also true."
}
```

<a id="node-urn-csabs-theorem-FirstHitDecisionTable-ordered-append"></a>

### ordered-append

`urn:csabs:theorem/FirstHitDecisionTable-ordered-append`

**statement:** Induct on the left table. A matching rule suppresses all later rules; otherwise recur.

**formalStatement:** ∀ {X V : Type} (a b : Catalog.FirstHitDecisionTable X V) (x : X), Catalog.firstHit (a ++ b) x = (Catalog.firstHit a x).or (Catalog.firstHit b x)

**assumptions:** Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality.

**dependsOn:** [defining profile](FirstHitDecisionTable.md#node-urn-csabs-axiom-FirstHitDecisionTable-defining-profile); [induction](Sequence.md#node-urn-csabs-axiom-Sequence-induction); [concat-recursion](Sequence.md#node-urn-csabs-axiom-Sequence-concat-recursion)

**proofSketch:** Induct on the left table. A matching rule suppresses all later rules; otherwise recur.

**reviewStatus:** Separately registered Lean witness; require fresh compiler and axiom audit for verified status.

**source:** [OMG Decision Model and Notation 1.5](https://www.omg.org/spec/DMN/1.5/PDF); citation: Decision Model and Notation v1.5, §8.2.11.1, FIRST hit policy.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; Catalog release, sequence, transducer, schema, date and extension models and witnesses; path: lean/Catalog/ReleaseSequenceModels.lean; accessedOn: 2026-11-20; sourceRole: local-lean-formulation-and-proof

**sourceLocator:** DMN 1.5 §8.2.11.1 FIRST hit policy; Catalog.first_hit_append

**sourceNote:** Derived for the explicit selected model. Induct on the left table. A matching rule suppresses all later rules; otherwise recur.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {X V : Type} (a b : Catalog.FirstHitDecisionTable X V) (x : X), Catalog.firstHit (a ++ b) x = (Catalog.firstHit a x).or (Catalog.firstHit b x)
```

**Source:** [`Catalog.first_hit_append`](../lean/Catalog/ReleaseSequenceModels.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** Induct on the left table. A matching rule suppresses all later rules; otherwise recur.

**Limits:** Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/FirstHitDecisionTable-defining-profile": "Proved constraint for the specified concrete interpretation or structural recursion; not a hypothesis asserting its own satisfaction. Induct on the left table. A matching rule suppresses all later rules; otherwise recur.",
  "urn:csabs:axiom/Sequence-concat-recursion": "Existing finite-list induction, concatenation or length premise, instantiated with exact List equality; no editing behavior is inferred from it.",
  "urn:csabs:axiom/Sequence-induction": "Existing finite-list induction, concatenation or length premise, instantiated with exact List equality; no editing behavior is inferred from it."
}
```

<a id="node-urn-csabs-theorem-FirstHitDecisionTable-no-match"></a>

### no-match

`urn:csabs:theorem/FirstHitDecisionTable-no-match`

**statement:** Induct on the ordered rule list and split on its head guard.

**formalStatement:** ∀ {X V : Type} (rs : Catalog.FirstHitDecisionTable X V) (x : X), Catalog.firstHit rs x = none ↔ ∀ r ∈ rs, r.1 x = false

**assumptions:** Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality.

**dependsOn:** [defining profile](FirstHitDecisionTable.md#node-urn-csabs-axiom-FirstHitDecisionTable-defining-profile); [induction](Sequence.md#node-urn-csabs-axiom-Sequence-induction)

**proofSketch:** Induct on the ordered rule list and split on its head guard.

**reviewStatus:** Separately registered Lean witness; require fresh compiler and axiom audit for verified status.

**source:** [OMG Decision Model and Notation 1.5](https://www.omg.org/spec/DMN/1.5/PDF); citation: Decision Model and Notation v1.5, §8.2.11.1, FIRST hit policy.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; Catalog release, sequence, transducer, schema, date and extension models and witnesses; path: lean/Catalog/ReleaseSequenceModels.lean; accessedOn: 2026-11-20; sourceRole: local-lean-formulation-and-proof

**sourceLocator:** DMN 1.5 §8.2.11.1 FIRST hit policy; Catalog.first_hit_none

**sourceNote:** Derived for the explicit selected model. Induct on the ordered rule list and split on its head guard.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {X V : Type} (rs : Catalog.FirstHitDecisionTable X V) (x : X), Catalog.firstHit rs x = none ↔ ∀ r ∈ rs, r.1 x = false
```

**Source:** [`Catalog.first_hit_none`](../lean/Catalog/ReleaseSequenceModels.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** Induct on the ordered rule list and split on its head guard.

**Limits:** Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/FirstHitDecisionTable-defining-profile": "Proved constraint for the specified concrete interpretation or structural recursion; not a hypothesis asserting its own satisfaction. Induct on the ordered rule list and split on its head guard.",
  "urn:csabs:axiom/Sequence-induction": "Existing finite-list induction, concatenation or length premise, instantiated with exact List equality; no editing behavior is inferred from it."
}
```

<a id="node-urn-csabs-theorem-FirstHitDecisionTable-first-match-selection"></a>

### first-match-selection

`urn:csabs:theorem/FirstHitDecisionTable-first-match-selection`

**statement:** All preceding rules yield none; append composition then selects the current true guard independently of later rules.

**formalStatement:** ∀ {X V : Type} (before after : Catalog.FirstHitDecisionTable X V) (g : X → Bool) (v : V) (x : X), (∀ r ∈ before, r.1 x = false) → g x = true → Catalog.firstHit (before ++ (g,v) :: after) x = some v

**assumptions:** Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality.

**dependsOn:** [defining profile](FirstHitDecisionTable.md#node-urn-csabs-axiom-FirstHitDecisionTable-defining-profile); [induction](Sequence.md#node-urn-csabs-axiom-Sequence-induction); [concat-recursion](Sequence.md#node-urn-csabs-axiom-Sequence-concat-recursion)

**proofSketch:** All preceding rules yield none; append composition then selects the current true guard independently of later rules.

**reviewStatus:** Separately registered Lean witness; require fresh compiler and axiom audit for verified status.

**source:** [OMG Decision Model and Notation 1.5](https://www.omg.org/spec/DMN/1.5/PDF); citation: Decision Model and Notation v1.5, §8.2.11.1, FIRST hit policy.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; Catalog release, sequence, transducer, schema, date and extension models and witnesses; path: lean/Catalog/ReleaseSequenceModels.lean; accessedOn: 2026-11-20; sourceRole: local-lean-formulation-and-proof

**sourceLocator:** DMN 1.5 §8.2.11.1 FIRST hit policy; Catalog.first_hit_selection

**sourceNote:** Derived for the explicit selected model. All preceding rules yield none; append composition then selects the current true guard independently of later rules.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {X V : Type} (before after : Catalog.FirstHitDecisionTable X V) (g : X → Bool) (v : V) (x : X), (∀ r ∈ before, r.1 x = false) → g x = true → Catalog.firstHit (before ++ (g,v) :: after) x = some v
```

**Source:** [`Catalog.first_hit_selection`](../lean/Catalog/ReleaseSequenceModels.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** All preceding rules yield none; append composition then selects the current true guard independently of later rules.

**Limits:** Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/FirstHitDecisionTable-defining-profile": "Proved constraint for the specified concrete interpretation or structural recursion; not a hypothesis asserting its own satisfaction. All preceding rules yield none; append composition then selects the current true guard independently of later rules.",
  "urn:csabs:axiom/Sequence-concat-recursion": "Existing finite-list induction, concatenation or length premise, instantiated with exact List equality; no editing behavior is inferred from it.",
  "urn:csabs:axiom/Sequence-induction": "Existing finite-list induction, concatenation or length premise, instantiated with exact List equality; no editing behavior is inferred from it."
}
```

## Concept provenance

- [OMG Decision Model and Notation 1.5](https://www.omg.org/spec/DMN/1.5/PDF); citation: Decision Model and Notation v1.5, §8.2.11.1, FIRST hit policy.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference

**sourceLocator:** DMN 1.5 §8.2.11.1 FIRST hit policy

**sourceNote:** Adapts FIRST to an ordered list with explicit Option no-match; DMN output expressions are represented by fixed outcomes. For input-dependent outcomes instantiate V as a suitable total outcome function with an explicit application mapping.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/FirstHitDecisionTable",
    "type": "Concept",
    "shortForm": "FirstHitDecisionTable",
    "fullName": "Ordered first-hit decision table",
    "synonyms": [
      "FIRST-hit decision table",
      "First-matching-rule table"
    ],
    "category": [
      "urn:csabs:category/data-modelling"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "definition": "A finite ordered list of total Boolean guards and outcomes; evaluation returns the outcome of the first true guard and none when every guard is false. Overlapping guards are permitted.",
    "notation": "R=[(gᵢ,vᵢ)]; gᵢ:X→Bool; eval:R×X→Option(V)",
    "requiresConcept": [
      "urn:csabs:concept/Sequence",
      "urn:csabs:concept/Function"
    ],
    "relatedConcept": [
      "urn:csabs:concept/DecisionTable"
    ],
    "axiomBasis": "eval([],x)=none; eval((g,v)::rs,x)=some(v) if g(x)=true, otherwise eval(rs,x). Finite order is semantically significant.",
    "basisKind": "defined-structure",
    "basisScope": "X,V arbitrary exact-equality carriers; rules retain list position even when repeated. Guards are total and pure. Empty table yields none, and no-match differs from any returned outcome. No implicit default, unique-hit constraint, output-priority sorting, effects, guard exceptions, or inferred coverage/feasibility. A final always-true rule explicitly encodes a default.",
    "mathematicalFormulation": "eval(R,x)=some(vᵢ) for i=min{j<|R| | gⱼ(x)=true}, or none when that set is empty.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Sourced model with separately registered Lean satisfaction and derived witnesses; verification requires fresh audit evidence.",
    "verificationObligation": [
      "Map exact carriers, equality, totality and the explicit profile conventions before use.",
      "Model and theorem evidence does not establish a concrete software implementation refinement."
    ],
    "hasOperation": [
      "urn:csabs:operation/FirstHitDecisionTable-evaluate"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/FirstHitDecisionTable-defining-profile"
    ],
    "hasLaw": [
      "urn:csabs:law/FirstHitDecisionTable-ordered-append",
      "urn:csabs:law/FirstHitDecisionTable-no-match",
      "urn:csabs:law/FirstHitDecisionTable-first-match-selection"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/FirstHitDecisionTable-model-satisfaction",
      "urn:csabs:theorem/FirstHitDecisionTable-ordered-append",
      "urn:csabs:theorem/FirstHitDecisionTable-no-match",
      "urn:csabs:theorem/FirstHitDecisionTable-first-match-selection"
    ],
    "source": [
      "urn:csabs:source/seven-dmn"
    ],
    "sourceLocator": "DMN 1.5 §8.2.11.1 FIRST hit policy",
    "sourceNote": "Adapts FIRST to an ordered list with explicit Option no-match; DMN output expressions are represented by fixed outcomes. For input-dependent outcomes instantiate V as a suitable total outcome function with an explicit application mapping.",
    "provenanceKind": "adapted",
    "leanFormulation": "abbrev FirstHitDecisionTable (X V : Type) := List ((X → Bool) × V)",
    "formulationSource": "urn:csabs:source/seven-lean-models",
    "formulationLocator": "Catalog.FirstHitDecisionTable",
    "formulationScope": "model",
    "leanModelMapping": "eval(R,x)=some(vᵢ) for i=min{j<|R| | gⱼ(x)=true}, or none when that set is empty.",
    "leanModelLimitations": "X,V arbitrary exact-equality carriers; rules retain list position even when repeated. Guards are total and pure. Empty table yields none, and no-match differs from any returned outcome. No implicit default, unique-hit constraint, output-priority sorting, effects, guard exceptions, or inferred coverage/feasibility. A final always-true rule explicitly encodes a default. Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit."
  },
  {
    "id": "urn:csabs:operation/FirstHitDecisionTable-evaluate",
    "type": "Operation",
    "concept": "urn:csabs:concept/FirstHitDecisionTable",
    "name": "first-hit evaluation",
    "signature": "eval : List((X→Bool)×V)×X→Option(V)",
    "description": "Evaluate rules in list order and stop at the first true guard.",
    "precondition": "Guards are pure total Boolean functions; no unique-hit requirement.",
    "postcondition": "some(v) for the earliest matching rule, otherwise none.",
    "totality": "Total on the stated domain.",
    "source": [
      "urn:csabs:source/seven-dmn"
    ],
    "sourceLocator": "DMN 1.5 §8.2.11.1 FIRST hit policy",
    "sourceNote": "Adapts FIRST to an ordered list with explicit Option no-match; DMN output expressions are represented by fixed outcomes. For input-dependent outcomes instantiate V as a suitable total outcome function with an explicit application mapping.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/FirstHitDecisionTable-defining-profile",
    "type": "Axiom",
    "name": "defining profile",
    "statement": "eval([],x)=none; eval((g,v)::rs,x)=some(v) if g(x)=true, otherwise eval(rs,x). Finite order is semantically significant.",
    "formalStatement": "eval(R,x)=some(vᵢ) for i=min{j<|R| | gⱼ(x)=true}, or none when that set is empty.",
    "assumptions": [
      "X,V arbitrary exact-equality carriers; rules retain list position even when repeated. Guards are total and pure. Empty table yields none, and no-match differs from any returned outcome. No implicit default, unique-hit constraint, output-priority sorting, effects, guard exceptions, or inferred coverage/feasibility. A final always-true rule explicitly encodes a default."
    ],
    "appliesTo": [
      "urn:csabs:concept/FirstHitDecisionTable"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Structure constraints; satisfaction is established separately for the selected model.",
    "source": [
      "urn:csabs:source/seven-dmn"
    ],
    "sourceLocator": "DMN 1.5 §8.2.11.1 FIRST hit policy",
    "sourceNote": "Adapts FIRST to an ordered list with explicit Option no-match; DMN output expressions are represented by fixed outcomes. For input-dependent outcomes instantiate V as a suitable total outcome function with an explicit application mapping.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/FirstHitDecisionTable-ordered-append",
    "type": "Law",
    "name": "ordered-append",
    "statement": "Induct on the left table. A matching rule suppresses all later rules; otherwise recur.",
    "formalStatement": "∀ {X V : Type} (a b : Catalog.FirstHitDecisionTable X V) (x : X), Catalog.firstHit (a ++ b) x = (Catalog.firstHit a x).or (Catalog.firstHit b x)",
    "assumptions": [
      "Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/FirstHitDecisionTable"
    ],
    "dependsOn": [
      "urn:csabs:axiom/FirstHitDecisionTable-defining-profile",
      "urn:csabs:axiom/Sequence-induction",
      "urn:csabs:axiom/Sequence-concat-recursion"
    ],
    "proofSketch": "Induct on the left table. A matching rule suppresses all later rules; otherwise recur.",
    "reviewStatus": "Derived mathematical law; separately registered theorem supplies explicit proof evidence.",
    "source": [
      "urn:csabs:source/seven-dmn",
      "urn:csabs:source/seven-lean-models"
    ],
    "sourceLocator": "DMN 1.5 §8.2.11.1 FIRST hit policy; Catalog.first_hit_append",
    "sourceNote": "Derived for the explicit selected model. Induct on the left table. A matching rule suppresses all later rules; otherwise recur.",
    "provenanceKind": "derived",
    "ruleRole": "derived-law"
  },
  {
    "id": "urn:csabs:law/FirstHitDecisionTable-no-match",
    "type": "Law",
    "name": "no-match",
    "statement": "Induct on the ordered rule list and split on its head guard.",
    "formalStatement": "∀ {X V : Type} (rs : Catalog.FirstHitDecisionTable X V) (x : X), Catalog.firstHit rs x = none ↔ ∀ r ∈ rs, r.1 x = false",
    "assumptions": [
      "Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/FirstHitDecisionTable"
    ],
    "dependsOn": [
      "urn:csabs:axiom/FirstHitDecisionTable-defining-profile",
      "urn:csabs:axiom/Sequence-induction"
    ],
    "proofSketch": "Induct on the ordered rule list and split on its head guard.",
    "reviewStatus": "Derived mathematical law; separately registered theorem supplies explicit proof evidence.",
    "source": [
      "urn:csabs:source/seven-dmn",
      "urn:csabs:source/seven-lean-models"
    ],
    "sourceLocator": "DMN 1.5 §8.2.11.1 FIRST hit policy; Catalog.first_hit_none",
    "sourceNote": "Derived for the explicit selected model. Induct on the ordered rule list and split on its head guard.",
    "provenanceKind": "derived",
    "ruleRole": "derived-law"
  },
  {
    "id": "urn:csabs:law/FirstHitDecisionTable-first-match-selection",
    "type": "Law",
    "name": "first-match-selection",
    "statement": "All preceding rules yield none; append composition then selects the current true guard independently of later rules.",
    "formalStatement": "∀ {X V : Type} (before after : Catalog.FirstHitDecisionTable X V) (g : X → Bool) (v : V) (x : X), (∀ r ∈ before, r.1 x = false) → g x = true → Catalog.firstHit (before ++ (g,v) :: after) x = some v",
    "assumptions": [
      "Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/FirstHitDecisionTable"
    ],
    "dependsOn": [
      "urn:csabs:axiom/FirstHitDecisionTable-defining-profile",
      "urn:csabs:axiom/Sequence-induction",
      "urn:csabs:axiom/Sequence-concat-recursion"
    ],
    "proofSketch": "All preceding rules yield none; append composition then selects the current true guard independently of later rules.",
    "reviewStatus": "Derived mathematical law; separately registered theorem supplies explicit proof evidence.",
    "source": [
      "urn:csabs:source/seven-dmn",
      "urn:csabs:source/seven-lean-models"
    ],
    "sourceLocator": "DMN 1.5 §8.2.11.1 FIRST hit policy; Catalog.first_hit_selection",
    "sourceNote": "Derived for the explicit selected model. All preceding rules yield none; append composition then selects the current true guard independently of later rules.",
    "provenanceKind": "derived",
    "ruleRole": "derived-law"
  },
  {
    "id": "urn:csabs:theorem/FirstHitDecisionTable-model-satisfaction",
    "type": "Theorem",
    "name": "model-satisfaction",
    "statement": "Compute overlapping guards and the empty table; the first rule wins even when a later guard is also true.",
    "formalStatement": "Catalog.firstHit [(fun _ : Bool => true, 1), (fun _ => true, 2)] false = some 1 ∧ Catalog.firstHit ([] : Catalog.FirstHitDecisionTable Bool Nat) false = none",
    "assumptions": [
      "Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/FirstHitDecisionTable"
    ],
    "dependsOn": [
      "urn:csabs:axiom/FirstHitDecisionTable-defining-profile"
    ],
    "proofSketch": "Compute overlapping guards and the empty table; the first rule wins even when a later guard is also true.",
    "reviewStatus": "Separately registered Lean witness; require fresh compiler and axiom audit for verified status.",
    "source": [
      "urn:csabs:source/seven-dmn",
      "urn:csabs:source/seven-lean-models"
    ],
    "sourceLocator": "DMN 1.5 §8.2.11.1 FIRST hit policy; Catalog.first_hit_model_satisfaction",
    "sourceNote": "Derived for the explicit selected model. Compute overlapping guards and the empty table; the first rule wins even when a later guard is also true.",
    "provenanceKind": "derived",
    "leanFormulation": "Catalog.firstHit [(fun _ : Bool => true, 1), (fun _ => true, 2)] false = some 1 ∧ Catalog.firstHit ([] : Catalog.FirstHitDecisionTable Bool Nat) false = none",
    "formulationSource": "urn:csabs:source/seven-lean-models",
    "formulationLocator": "Catalog.first_hit_model_satisfaction",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Compute overlapping guards and the empty table; the first rule wins even when a later guard is also true.",
    "leanModelLimitations": "Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/FirstHitDecisionTable-defining-profile\": \"Proved constraint for the specified concrete interpretation or structural recursion; not a hypothesis asserting its own satisfaction. Compute overlapping guards and the empty table; the first rule wins even when a later guard is also true.\"}"
  },
  {
    "id": "urn:csabs:theorem/FirstHitDecisionTable-ordered-append",
    "type": "Theorem",
    "name": "ordered-append",
    "statement": "Induct on the left table. A matching rule suppresses all later rules; otherwise recur.",
    "formalStatement": "∀ {X V : Type} (a b : Catalog.FirstHitDecisionTable X V) (x : X), Catalog.firstHit (a ++ b) x = (Catalog.firstHit a x).or (Catalog.firstHit b x)",
    "assumptions": [
      "Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/FirstHitDecisionTable"
    ],
    "dependsOn": [
      "urn:csabs:axiom/FirstHitDecisionTable-defining-profile",
      "urn:csabs:axiom/Sequence-induction",
      "urn:csabs:axiom/Sequence-concat-recursion"
    ],
    "proofSketch": "Induct on the left table. A matching rule suppresses all later rules; otherwise recur.",
    "reviewStatus": "Separately registered Lean witness; require fresh compiler and axiom audit for verified status.",
    "source": [
      "urn:csabs:source/seven-dmn",
      "urn:csabs:source/seven-lean-models"
    ],
    "sourceLocator": "DMN 1.5 §8.2.11.1 FIRST hit policy; Catalog.first_hit_append",
    "sourceNote": "Derived for the explicit selected model. Induct on the left table. A matching rule suppresses all later rules; otherwise recur.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {X V : Type} (a b : Catalog.FirstHitDecisionTable X V) (x : X), Catalog.firstHit (a ++ b) x = (Catalog.firstHit a x).or (Catalog.firstHit b x)",
    "formulationSource": "urn:csabs:source/seven-lean-models",
    "formulationLocator": "Catalog.first_hit_append",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Induct on the left table. A matching rule suppresses all later rules; otherwise recur.",
    "leanModelLimitations": "Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/FirstHitDecisionTable-defining-profile\": \"Proved constraint for the specified concrete interpretation or structural recursion; not a hypothesis asserting its own satisfaction. Induct on the left table. A matching rule suppresses all later rules; otherwise recur.\", \"urn:csabs:axiom/Sequence-concat-recursion\": \"Existing finite-list induction, concatenation or length premise, instantiated with exact List equality; no editing behavior is inferred from it.\", \"urn:csabs:axiom/Sequence-induction\": \"Existing finite-list induction, concatenation or length premise, instantiated with exact List equality; no editing behavior is inferred from it.\"}"
  },
  {
    "id": "urn:csabs:theorem/FirstHitDecisionTable-no-match",
    "type": "Theorem",
    "name": "no-match",
    "statement": "Induct on the ordered rule list and split on its head guard.",
    "formalStatement": "∀ {X V : Type} (rs : Catalog.FirstHitDecisionTable X V) (x : X), Catalog.firstHit rs x = none ↔ ∀ r ∈ rs, r.1 x = false",
    "assumptions": [
      "Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/FirstHitDecisionTable"
    ],
    "dependsOn": [
      "urn:csabs:axiom/FirstHitDecisionTable-defining-profile",
      "urn:csabs:axiom/Sequence-induction"
    ],
    "proofSketch": "Induct on the ordered rule list and split on its head guard.",
    "reviewStatus": "Separately registered Lean witness; require fresh compiler and axiom audit for verified status.",
    "source": [
      "urn:csabs:source/seven-dmn",
      "urn:csabs:source/seven-lean-models"
    ],
    "sourceLocator": "DMN 1.5 §8.2.11.1 FIRST hit policy; Catalog.first_hit_none",
    "sourceNote": "Derived for the explicit selected model. Induct on the ordered rule list and split on its head guard.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {X V : Type} (rs : Catalog.FirstHitDecisionTable X V) (x : X), Catalog.firstHit rs x = none ↔ ∀ r ∈ rs, r.1 x = false",
    "formulationSource": "urn:csabs:source/seven-lean-models",
    "formulationLocator": "Catalog.first_hit_none",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Induct on the ordered rule list and split on its head guard.",
    "leanModelLimitations": "Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/FirstHitDecisionTable-defining-profile\": \"Proved constraint for the specified concrete interpretation or structural recursion; not a hypothesis asserting its own satisfaction. Induct on the ordered rule list and split on its head guard.\", \"urn:csabs:axiom/Sequence-induction\": \"Existing finite-list induction, concatenation or length premise, instantiated with exact List equality; no editing behavior is inferred from it.\"}"
  },
  {
    "id": "urn:csabs:theorem/FirstHitDecisionTable-first-match-selection",
    "type": "Theorem",
    "name": "first-match-selection",
    "statement": "All preceding rules yield none; append composition then selects the current true guard independently of later rules.",
    "formalStatement": "∀ {X V : Type} (before after : Catalog.FirstHitDecisionTable X V) (g : X → Bool) (v : V) (x : X), (∀ r ∈ before, r.1 x = false) → g x = true → Catalog.firstHit (before ++ (g,v) :: after) x = some v",
    "assumptions": [
      "Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/FirstHitDecisionTable"
    ],
    "dependsOn": [
      "urn:csabs:axiom/FirstHitDecisionTable-defining-profile",
      "urn:csabs:axiom/Sequence-induction",
      "urn:csabs:axiom/Sequence-concat-recursion"
    ],
    "proofSketch": "All preceding rules yield none; append composition then selects the current true guard independently of later rules.",
    "reviewStatus": "Separately registered Lean witness; require fresh compiler and axiom audit for verified status.",
    "source": [
      "urn:csabs:source/seven-dmn",
      "urn:csabs:source/seven-lean-models"
    ],
    "sourceLocator": "DMN 1.5 §8.2.11.1 FIRST hit policy; Catalog.first_hit_selection",
    "sourceNote": "Derived for the explicit selected model. All preceding rules yield none; append composition then selects the current true guard independently of later rules.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {X V : Type} (before after : Catalog.FirstHitDecisionTable X V) (g : X → Bool) (v : V) (x : X), (∀ r ∈ before, r.1 x = false) → g x = true → Catalog.firstHit (before ++ (g,v) :: after) x = some v",
    "formulationSource": "urn:csabs:source/seven-lean-models",
    "formulationLocator": "Catalog.first_hit_selection",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "All preceding rules yield none; append composition then selects the current true guard independently of later rules.",
    "leanModelLimitations": "Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/FirstHitDecisionTable-defining-profile\": \"Proved constraint for the specified concrete interpretation or structural recursion; not a hypothesis asserting its own satisfaction. All preceding rules yield none; append composition then selects the current true guard independently of later rules.\", \"urn:csabs:axiom/Sequence-concat-recursion\": \"Existing finite-list induction, concatenation or length premise, instantiated with exact List equality; no editing behavior is inferred from it.\", \"urn:csabs:axiom/Sequence-induction\": \"Existing finite-list induction, concatenation or length premise, instantiated with exact List equality; no editing behavior is inferred from it.\"}"
  }
]
```
<!-- graph-record:end -->
