# Memory dependence and legal loop rescheduling

A relation on dynamic access events with equal modeled locations, at least one write and source execution order; a legal sequential rescheduling preserves every required dependence.

**Notation:** Dep(x,y)⇔x,y∈D ∧ loc(x)=loc(y) ∧ (W(x)∨W(y)) ∧ x≺src y; Dep(x,y)⇒θ(x)≺lexθ(y)

**Stable ID:** `urn:csabs:concept/LoopDependence`

**Categories:** Programming-language semantics → Compiler transformations

**Kind:** Relation

**Prerequisites:** [Integer quasi-affine index map](IntegerAffineMap.md), [Binary relation](Relation.md), [Conservative resource effect summary](EffectSummary.md)

**Specializes:** [Binary relation](Relation.md)

**Related concepts:** [Observable behavior refinement (ObservationalRefinement)](BehaviorRefinement.md), [Directed Graph](DirectedGraph.md), [Guarded loop event-domain correspondence](LoopIterationMapping.md), [Scoped induction recurrence and trip-count facts](ScalarRecurrence.md), [Conservative alias and Mod/Ref query contract](AliasAnalysis.md), [Lane-indexed vector execution and inactive-lane policy](PredicatedVectorSemantics.md)

## Backlinks

- [Conservative resource effect summary](EffectSummary.md) — `relatedConcept`
- [Integer quasi-affine index map](IntegerAffineMap.md) — `relatedConcept`
- [Guarded loop event-domain correspondence](LoopIterationMapping.md) — `requiresConcept`

## Mathematical formulation

A relation on dynamic access events with equal modeled locations, at least one write and source execution order; a legal sequential rescheduling preserves every required dependence. Dep(x,y)⇔x,y∈D ∧ loc(x)=loc(y) ∧ (W(x)∨W(y)) ∧ x≺src y; Dep(x,y)⇒θ(x)≺lexθ(y) Finite dynamic event domain D with original total order, modeled byte/resource locations and read/write kinds. Event identity includes statement, iteration and intra-statement order. Conservative may-alias enlarges dependencies. Empty iteration spaces impose no memory dependence. RAW, WAR and WAW are ordered; RAR has no write and is not a required memory-order edge in this profile. Affine access equality is a useful decidable subcase under supported constraints. Analysis Failure is unknown, not NoDependence. Sequential schedule legality additionally requires a bijection of events (no deletion/duplication), preservation of computations, scalar/SSA/control dependencies, and all other observable effects. Reduction reassociation, floating-point rounding and parallel/concurrent schedules need extra laws.

**Lean formulation** (in its source module context):

```lean
structure LoopDependence (Event Address Time : Type u) where
  active : Set Event
  address : Event → Address
  writes : Event → Prop
  before : Event → Event → Prop
  schedule : Event → Time
  timeBefore : Time → Time → Prop
```

**Source:** [`Catalog.Transforms.LoopDependence`](../lean/Catalog/CompilerTransforms.lean); consulted 2026-11-16.

**Scope:** partial

**Interpretation:** Access-event carrier with location, write, active and source-order functions; preservesDependence supplies timestamp-order obligation.

**Limits:** No affine dependence solver, byte-range alias implementation or theorem proving full loop transformation correctness. The memory-order condition alone omits scalar/control effects.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Dep(x,y) ↔ x,y∈D ∧ loc(x)=loc(y) ∧ (W(x)∨W(y)) ∧ x≺src y.; MemoryOrderLegal(θ) ↔ ∀x,y, Dep(x,y)⇒θ(x)≺lexθ(y).

**basisKind:** relational-structural-definition

**basisScope:** Finite dynamic event domain D with original total order, modeled byte/resource locations and read/write kinds. Event identity includes statement, iteration and intra-statement order. Conservative may-alias enlarges dependencies. Empty iteration spaces impose no memory dependence. RAW, WAR and WAW are ordered; RAR has no write and is not a required memory-order edge in this profile. Affine access equality is a useful decidable subcase under supported constraints. Analysis Failure is unknown, not NoDependence. Sequential schedule legality additionally requires a bijection of events (no deletion/duplication), preservation of computations, scalar/SSA/control dependencies, and all other observable effects. Reduction reassociation, floating-point rounding and parallel/concurrent schedules need extra laws.

**specializationNote:** Instantiate the parent carrier and operation as follows: Access-event carrier with location, write, active and source-order functions; preservesDependence supplies timestamp-order obligation.

**verificationObligation:** Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.; No affine dependence solver, byte-range alias implementation or theorem proving full loop transformation correctness. The memory-order condition alone omits scalar/control effects.

**reviewStatus:** Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-LoopDependence-dependent"></a>

### dependent

`urn:csabs:operation/LoopDependence-dependent`

**signature:** dependent : Event×Event→Prop

**description:** Determine ordered conflicting accesses in the specified location model.

**precondition:** Active events, original order and sound aliasing model supplied.

**postcondition:** Determine ordered conflicting accesses in the specified location model.

**totality:** Total semantic predicate; implementation analysis can be unknown.

**source:** [MLIR Affine dependence analysis interface (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/include/mlir/Dialect/Affine/Analysis/AffineAnalysis.h); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/include/mlir/Dialect/Affine/Analysis/AffineAnalysis.h; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [MLIR Affine dialect (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/Dialects/Affine.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/Dialects/Affine.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** AffineAnalysis.h: DependenceComponent, DependenceResult, checkMemrefAccessDependence; Affine dialect: affine maps and integer sets

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-LoopDependence-legal-schedule"></a>

### legal-schedule

`urn:csabs:operation/LoopDependence-legal-schedule`

**signature:** legalSchedule : (Event→Time)→Prop

**description:** Require strict ordered timestamps on every required dependence.

**precondition:** Complete dependence set and event/computation preservation separately established.

**postcondition:** Require strict ordered timestamps on every required dependence.

**totality:** Total predicate; timestamps may tie only where other execution obligations allow.

**source:** [MLIR Affine dependence analysis interface (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/include/mlir/Dialect/Affine/Analysis/AffineAnalysis.h); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/include/mlir/Dialect/Affine/Analysis/AffineAnalysis.h; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [MLIR Affine dialect (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/Dialects/Affine.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/Dialects/Affine.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** AffineAnalysis.h: DependenceComponent, DependenceResult, checkMemrefAccessDependence; Affine dialect: affine maps and integer sets

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-LoopDependence-conflict-definition"></a>

### conflict-definition

`urn:csabs:axiom/LoopDependence-conflict-definition`

**description:** Defining obligation for Memory dependence and legal loop rescheduling

**statement:** Dep(x,y) ↔ x,y∈D ∧ loc(x)=loc(y) ∧ (W(x)∨W(y)) ∧ x≺src y.

**formalStatement:** Dep(x,y) ↔ x,y∈D ∧ loc(x)=loc(y) ∧ (W(x)∨W(y)) ∧ x≺src y.

**assumptions:** Finite dynamic event domain D with original total order, modeled byte/resource locations and read/write kinds. Event identity includes statement, iteration and intra-statement order. Conservative may-alias enlarges dependencies. Empty iteration spaces impose no memory dependence. RAW, WAR and WAW are ordered; RAR has no write and is not a required memory-order edge in this profile. Affine access equality is a useful decidable subcase under supported constraints. Analysis Failure is unknown, not NoDependence. Sequential schedule legality additionally requires a bijection of events (no deletion/duplication), preservation of computations, scalar/SSA/control dependencies, and all other observable effects. Reduction reassociation, floating-point rounding and parallel/concurrent schedules need extra laws.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [MLIR Affine dependence analysis interface (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/include/mlir/Dialect/Affine/Analysis/AffineAnalysis.h); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/include/mlir/Dialect/Affine/Analysis/AffineAnalysis.h; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [MLIR Affine dialect (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/Dialects/Affine.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/Dialects/Affine.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** AffineAnalysis.h: DependenceComponent, DependenceResult, checkMemrefAccessDependence; Affine dialect: affine maps and integer sets

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

**reviewStatus:** Editorial mathematical statement and derivation; no registered compiled witness.

<a id="node-urn-csabs-axiom-LoopDependence-schedule-order"></a>

### schedule-order

`urn:csabs:axiom/LoopDependence-schedule-order`

**description:** Defining obligation for Memory dependence and legal loop rescheduling

**statement:** MemoryOrderLegal(θ) ↔ ∀x,y, Dep(x,y)⇒θ(x)≺lexθ(y).

**formalStatement:** MemoryOrderLegal(θ) ↔ ∀x,y, Dep(x,y)⇒θ(x)≺lexθ(y).

**assumptions:** Finite dynamic event domain D with original total order, modeled byte/resource locations and read/write kinds. Event identity includes statement, iteration and intra-statement order. Conservative may-alias enlarges dependencies. Empty iteration spaces impose no memory dependence. RAW, WAR and WAW are ordered; RAR has no write and is not a required memory-order edge in this profile. Affine access equality is a useful decidable subcase under supported constraints. Analysis Failure is unknown, not NoDependence. Sequential schedule legality additionally requires a bijection of events (no deletion/duplication), preservation of computations, scalar/SSA/control dependencies, and all other observable effects. Reduction reassociation, floating-point rounding and parallel/concurrent schedules need extra laws.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [MLIR Affine dependence analysis interface (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/include/mlir/Dialect/Affine/Analysis/AffineAnalysis.h); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/include/mlir/Dialect/Affine/Analysis/AffineAnalysis.h; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [MLIR Affine dialect (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/Dialects/Affine.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/Dialects/Affine.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** AffineAnalysis.h: DependenceComponent, DependenceResult, checkMemrefAccessDependence; Affine dialect: affine maps and integer sets

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

**reviewStatus:** Editorial mathematical statement and derivation; no registered compiled witness.

## Laws

<a id="node-urn-csabs-law-LoopDependence-read-read-no-conflict"></a>

### read-read-no-conflict

`urn:csabs:law/LoopDependence-read-read-no-conflict`

**description:** Derived consequence within the selected semantic profile.

**statement:** If x and y are both read-only then ¬Dep(x,y) in this memory-order profile, even when loc(x)=loc(y).

**formalStatement:** If x and y are both read-only then ¬Dep(x,y) in this memory-order profile, even when loc(x)=loc(y).

**assumptions:** Finite dynamic event domain D with original total order, modeled byte/resource locations and read/write kinds. Event identity includes statement, iteration and intra-statement order. Conservative may-alias enlarges dependencies. Empty iteration spaces impose no memory dependence. RAW, WAR and WAW are ordered; RAR has no write and is not a required memory-order edge in this profile. Affine access equality is a useful decidable subcase under supported constraints. Analysis Failure is unknown, not NoDependence. Sequential schedule legality additionally requires a bijection of events (no deletion/duplication), preservation of computations, scalar/SSA/control dependencies, and all other observable effects. Reduction reassociation, floating-point rounding and parallel/concurrent schedules need extra laws.

**dependsOn:** [conflict-definition](LoopDependence.md#node-urn-csabs-axiom-LoopDependence-conflict-definition)

**proofSketch:** Both W(x) and W(y) are false, so their disjunction in the dependence definition is false. Volatile/atomic/control ordering is outside this profile.

**reviewStatus:** Editorial mathematical derivation; no registered compiled witness.

**notationLanguage:** informal mathematical Unicode

**source:** [MLIR Affine dependence analysis interface (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/include/mlir/Dialect/Affine/Analysis/AffineAnalysis.h); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/include/mlir/Dialect/Affine/Analysis/AffineAnalysis.h; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [MLIR Affine dialect (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/Dialects/Affine.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/Dialects/Affine.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** AffineAnalysis.h: DependenceComponent, DependenceResult, checkMemrefAccessDependence; Affine dialect: affine maps and integer sets

**sourceNote:** Derived from the explicit dependsOn premises under the stated assumptions; exact claim and proof sketch are editorial.

**provenanceKind:** derived

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [MLIR Affine dependence analysis interface (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/include/mlir/Dialect/Affine/Analysis/AffineAnalysis.h); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/include/mlir/Dialect/Affine/Analysis/AffineAnalysis.h; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification
- [MLIR Affine dialect (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/Dialects/Affine.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/Dialects/Affine.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** AffineAnalysis.h: DependenceComponent, DependenceResult, checkMemrefAccessDependence; Affine dialect: affine maps and integer sets

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/LoopDependence",
    "type": "Concept",
    "shortForm": "LoopDependence",
    "fullName": "Memory dependence and legal loop rescheduling",
    "definition": "A relation on dynamic access events with equal modeled locations, at least one write and source execution order; a legal sequential rescheduling preserves every required dependence.",
    "notation": "Dep(x,y)⇔x,y∈D ∧ loc(x)=loc(y) ∧ (W(x)∨W(y)) ∧ x≺src y; Dep(x,y)⇒θ(x)≺lexθ(y)",
    "category": [
      "urn:csabs:category/compiler-transformations"
    ],
    "kind": "urn:csabs:kind/relation",
    "requiresConcept": [
      "urn:csabs:concept/IntegerAffineMap",
      "urn:csabs:concept/Relation",
      "urn:csabs:concept/EffectSummary"
    ],
    "relatedConcept": [
      "urn:csabs:concept/BehaviorRefinement",
      "urn:csabs:concept/DirectedGraph",
      "urn:csabs:concept/LoopIterationMapping",
      "urn:csabs:concept/ScalarRecurrence",
      "urn:csabs:concept/AliasAnalysis",
      "urn:csabs:concept/PredicatedVectorSemantics"
    ],
    "hasOperation": [
      "urn:csabs:operation/LoopDependence-dependent",
      "urn:csabs:operation/LoopDependence-legal-schedule"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/LoopDependence-conflict-definition",
      "urn:csabs:axiom/LoopDependence-schedule-order"
    ],
    "hasLaw": [
      "urn:csabs:law/LoopDependence-read-read-no-conflict"
    ],
    "hasTheorem": [],
    "basisKind": "relational-structural-definition",
    "basisScope": "Finite dynamic event domain D with original total order, modeled byte/resource locations and read/write kinds. Event identity includes statement, iteration and intra-statement order. Conservative may-alias enlarges dependencies. Empty iteration spaces impose no memory dependence. RAW, WAR and WAW are ordered; RAR has no write and is not a required memory-order edge in this profile. Affine access equality is a useful decidable subcase under supported constraints. Analysis Failure is unknown, not NoDependence. Sequential schedule legality additionally requires a bijection of events (no deletion/duplication), preservation of computations, scalar/SSA/control dependencies, and all other observable effects. Reduction reassociation, floating-point rounding and parallel/concurrent schedules need extra laws.",
    "axiomBasis": "Dep(x,y) ↔ x,y∈D ∧ loc(x)=loc(y) ∧ (W(x)∨W(y)) ∧ x≺src y.; MemoryOrderLegal(θ) ↔ ∀x,y, Dep(x,y)⇒θ(x)≺lexθ(y).",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.",
    "verificationObligation": [
      "Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.",
      "No affine dependence solver, byte-range alias implementation or theorem proving full loop transformation correctness. The memory-order condition alone omits scalar/control effects."
    ],
    "source": [
      "urn:csabs:source/compiler-dependence",
      "urn:csabs:source/compiler-affine"
    ],
    "sourceLocator": "AffineAnalysis.h: DependenceComponent, DependenceResult, checkMemrefAccessDependence; Affine dialect: affine maps and integer sets",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/Relation"
    ],
    "specializationNote": "Instantiate the parent carrier and operation as follows: Access-event carrier with location, write, active and source-order functions; preservesDependence supplies timestamp-order obligation.",
    "mathematicalFormulation": "A relation on dynamic access events with equal modeled locations, at least one write and source execution order; a legal sequential rescheduling preserves every required dependence. Dep(x,y)⇔x,y∈D ∧ loc(x)=loc(y) ∧ (W(x)∨W(y)) ∧ x≺src y; Dep(x,y)⇒θ(x)≺lexθ(y) Finite dynamic event domain D with original total order, modeled byte/resource locations and read/write kinds. Event identity includes statement, iteration and intra-statement order. Conservative may-alias enlarges dependencies. Empty iteration spaces impose no memory dependence. RAW, WAR and WAW are ordered; RAR has no write and is not a required memory-order edge in this profile. Affine access equality is a useful decidable subcase under supported constraints. Analysis Failure is unknown, not NoDependence. Sequential schedule legality additionally requires a bijection of events (no deletion/duplication), preservation of computations, scalar/SSA/control dependencies, and all other observable effects. Reduction reassociation, floating-point rounding and parallel/concurrent schedules need extra laws.",
    "leanFormulation": "structure LoopDependence (Event Address Time : Type u) where\n  active : Set Event\n  address : Event → Address\n  writes : Event → Prop\n  before : Event → Event → Prop\n  schedule : Event → Time\n  timeBefore : Time → Time → Prop",
    "formulationSource": "urn:csabs:source/compiler-lean",
    "formulationLocator": "Catalog.Transforms.LoopDependence",
    "formulationScope": "partial",
    "leanModelMapping": "Access-event carrier with location, write, active and source-order functions; preservesDependence supplies timestamp-order obligation.",
    "leanModelLimitations": "No affine dependence solver, byte-range alias implementation or theorem proving full loop transformation correctness. The memory-order condition alone omits scalar/control effects."
  },
  {
    "id": "urn:csabs:operation/LoopDependence-dependent",
    "type": "Operation",
    "name": "dependent",
    "signature": "dependent : Event×Event→Prop",
    "description": "Determine ordered conflicting accesses in the specified location model.",
    "concept": "urn:csabs:concept/LoopDependence",
    "precondition": "Active events, original order and sound aliasing model supplied.",
    "postcondition": "Determine ordered conflicting accesses in the specified location model.",
    "totality": "Total semantic predicate; implementation analysis can be unknown.",
    "source": [
      "urn:csabs:source/compiler-dependence",
      "urn:csabs:source/compiler-affine"
    ],
    "sourceLocator": "AffineAnalysis.h: DependenceComponent, DependenceResult, checkMemrefAccessDependence; Affine dialect: affine maps and integer sets",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/LoopDependence-legal-schedule",
    "type": "Operation",
    "name": "legal-schedule",
    "signature": "legalSchedule : (Event→Time)→Prop",
    "description": "Require strict ordered timestamps on every required dependence.",
    "concept": "urn:csabs:concept/LoopDependence",
    "precondition": "Complete dependence set and event/computation preservation separately established.",
    "postcondition": "Require strict ordered timestamps on every required dependence.",
    "totality": "Total predicate; timestamps may tie only where other execution obligations allow.",
    "source": [
      "urn:csabs:source/compiler-dependence",
      "urn:csabs:source/compiler-affine"
    ],
    "sourceLocator": "AffineAnalysis.h: DependenceComponent, DependenceResult, checkMemrefAccessDependence; Affine dialect: affine maps and integer sets",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/LoopDependence-conflict-definition",
    "type": "Axiom",
    "name": "conflict-definition",
    "description": "Defining obligation for Memory dependence and legal loop rescheduling",
    "statement": "Dep(x,y) ↔ x,y∈D ∧ loc(x)=loc(y) ∧ (W(x)∨W(y)) ∧ x≺src y.",
    "formalStatement": "Dep(x,y) ↔ x,y∈D ∧ loc(x)=loc(y) ∧ (W(x)∨W(y)) ∧ x≺src y.",
    "assumptions": [
      "Finite dynamic event domain D with original total order, modeled byte/resource locations and read/write kinds. Event identity includes statement, iteration and intra-statement order. Conservative may-alias enlarges dependencies. Empty iteration spaces impose no memory dependence. RAW, WAR and WAW are ordered; RAR has no write and is not a required memory-order edge in this profile. Affine access equality is a useful decidable subcase under supported constraints. Analysis Failure is unknown, not NoDependence. Sequential schedule legality additionally requires a bijection of events (no deletion/duplication), preservation of computations, scalar/SSA/control dependencies, and all other observable effects. Reduction reassociation, floating-point rounding and parallel/concurrent schedules need extra laws."
    ],
    "appliesTo": [
      "urn:csabs:concept/LoopDependence"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-dependence",
      "urn:csabs:source/compiler-affine"
    ],
    "sourceLocator": "AffineAnalysis.h: DependenceComponent, DependenceResult, checkMemrefAccessDependence; Affine dialect: affine maps and integer sets",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial mathematical statement and derivation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:axiom/LoopDependence-schedule-order",
    "type": "Axiom",
    "name": "schedule-order",
    "description": "Defining obligation for Memory dependence and legal loop rescheduling",
    "statement": "MemoryOrderLegal(θ) ↔ ∀x,y, Dep(x,y)⇒θ(x)≺lexθ(y).",
    "formalStatement": "MemoryOrderLegal(θ) ↔ ∀x,y, Dep(x,y)⇒θ(x)≺lexθ(y).",
    "assumptions": [
      "Finite dynamic event domain D with original total order, modeled byte/resource locations and read/write kinds. Event identity includes statement, iteration and intra-statement order. Conservative may-alias enlarges dependencies. Empty iteration spaces impose no memory dependence. RAW, WAR and WAW are ordered; RAR has no write and is not a required memory-order edge in this profile. Affine access equality is a useful decidable subcase under supported constraints. Analysis Failure is unknown, not NoDependence. Sequential schedule legality additionally requires a bijection of events (no deletion/duplication), preservation of computations, scalar/SSA/control dependencies, and all other observable effects. Reduction reassociation, floating-point rounding and parallel/concurrent schedules need extra laws."
    ],
    "appliesTo": [
      "urn:csabs:concept/LoopDependence"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-dependence",
      "urn:csabs:source/compiler-affine"
    ],
    "sourceLocator": "AffineAnalysis.h: DependenceComponent, DependenceResult, checkMemrefAccessDependence; Affine dialect: affine maps and integer sets",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial mathematical statement and derivation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:law/LoopDependence-read-read-no-conflict",
    "type": "Law",
    "name": "read-read-no-conflict",
    "description": "Derived consequence within the selected semantic profile.",
    "statement": "If x and y are both read-only then ¬Dep(x,y) in this memory-order profile, even when loc(x)=loc(y).",
    "formalStatement": "If x and y are both read-only then ¬Dep(x,y) in this memory-order profile, even when loc(x)=loc(y).",
    "assumptions": [
      "Finite dynamic event domain D with original total order, modeled byte/resource locations and read/write kinds. Event identity includes statement, iteration and intra-statement order. Conservative may-alias enlarges dependencies. Empty iteration spaces impose no memory dependence. RAW, WAR and WAW are ordered; RAR has no write and is not a required memory-order edge in this profile. Affine access equality is a useful decidable subcase under supported constraints. Analysis Failure is unknown, not NoDependence. Sequential schedule legality additionally requires a bijection of events (no deletion/duplication), preservation of computations, scalar/SSA/control dependencies, and all other observable effects. Reduction reassociation, floating-point rounding and parallel/concurrent schedules need extra laws."
    ],
    "appliesTo": [
      "urn:csabs:concept/LoopDependence"
    ],
    "dependsOn": [
      "urn:csabs:axiom/LoopDependence-conflict-definition"
    ],
    "proofSketch": "Both W(x) and W(y) are false, so their disjunction in the dependence definition is false. Volatile/atomic/control ordering is outside this profile.",
    "reviewStatus": "Editorial mathematical derivation; no registered compiled witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-dependence",
      "urn:csabs:source/compiler-affine"
    ],
    "sourceLocator": "AffineAnalysis.h: DependenceComponent, DependenceResult, checkMemrefAccessDependence; Affine dialect: affine maps and integer sets",
    "sourceNote": "Derived from the explicit dependsOn premises under the stated assumptions; exact claim and proof sketch are editorial.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
