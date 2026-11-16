# Guarded loop event-domain correspondence

A correspondence between active source and transformed dynamic loop events, separating coverage and uniqueness from schedule, value and dependence preservation.

**Notation:** f:Dtarget→Dsource is bijective on active events; schedule/value obligations are separate

**Stable ID:** `urn:csabs:concept/LoopIterationMapping`

**Categories:** Programming-language semantics → Compiler transformations

**Kind:** semantic-model

**Prerequisites:** [Memory dependence and legal loop rescheduling](LoopDependence.md), [CFG refinement with path correspondence and progress](ControlFlowRefinement.md)

**Related concepts:** [Scoped induction recurrence and trip-count facts](ScalarRecurrence.md), [Integer quasi-affine index map](IntegerAffineMap.md), [Lane-indexed vector execution and inactive-lane policy](PredicatedVectorSemantics.md)

## Backlinks

- [Memory dependence and legal loop rescheduling](LoopDependence.md) — `relatedConcept`
- [Lane-indexed vector execution and inactive-lane policy](PredicatedVectorSemantics.md) — `relatedConcept`
- [Scoped induction recurrence and trip-count facts](ScalarRecurrence.md) — `relatedConcept`

## Mathematical formulation

A correspondence between active source and transformed dynamic loop events, separating coverage and uniqueness from schedule, value and dependence preservation. f:Dtarget→Dsource is bijective on active events; schedule/value obligations are separate Events include statement identity, loop iteration and lane/unroll slot, including tails and multi-exit control. Zero-trip loops have empty body-event domains. Runtime-guarded versions must each map only their admitted input domain and dispatch must select a correct version. A bijection is a sufficient domain-preservation method for pure rescheduling/unrolling, not a requirement for every valid transformation: dead-event elimination, reductions or idiom replacement require a different refinement relation. Trip count and backedge count differ and unknown is not zero. Dependence ordering, values, exits, divergence and effects remain separate.

**Lean formulation** (in its source module context):

```lean
structure LoopIterationMapping (S T : Type u) where
  sourceActive : Set S
  targetActive : Set T
  original : T → S
  mapsActive : ∀ t ∈ targetActive, original t ∈ sourceActive
  covers : ∀ s ∈ sourceActive, ∃ t ∈ targetActive, original t = s
  unique : ∀ t ∈ targetActive, ∀ t' ∈ targetActive, original t = original t' → t = t'
```

**Source:** [`Catalog.LLVM.LoopIterationMapping`](../lean/Catalog/LLVMTransforms.lean); consulted 2026-11-16.

**Scope:** partial

**Interpretation:** Active source/target sets, original-event map and explicit active/injective/covering laws.

**Limits:** No schedule, loop exit, scalar-value, recurrence, runtime-dispatch or dependence proof. Bijection is not presented as a complete characterization of loop correctness.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** f maps active target events into active source events, is injective there, and covers every active source event.; Every admitted source input must dispatch to a transformed version whose guard and event correspondence hold, including zero-trip/tail cases.

**basisKind:** relational-structural-definition

**basisScope:** Events include statement identity, loop iteration and lane/unroll slot, including tails and multi-exit control. Zero-trip loops have empty body-event domains. Runtime-guarded versions must each map only their admitted input domain and dispatch must select a correct version. A bijection is a sufficient domain-preservation method for pure rescheduling/unrolling, not a requirement for every valid transformation: dead-event elimination, reductions or idiom replacement require a different refinement relation. Trip count and backedge count differ and unknown is not zero. Dependence ordering, values, exits, divergence and effects remain separate.

**verificationObligation:** Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.; No schedule, loop exit, scalar-value, recurrence, runtime-dispatch or dependence proof. Bijection is not presented as a complete characterization of loop correctness.

**reviewStatus:** Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-LoopIterationMapping-original-event"></a>

### original-event

`urn:csabs:operation/LoopIterationMapping-original-event`

**signature:** originalEvent : Dtarget→Dsource

**description:** Associate each active transformed event with its original statement/iteration.

**precondition:** Relevant runtime guard and tail domain fixed.

**postcondition:** Associate each active transformed event with its original statement/iteration.

**totality:** Total on active target events.

**source:** [LLVM Loop Terminology (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LoopTerminology.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LoopTerminology.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM Pass Reference (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Passes.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Passes.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM Auto-Vectorization (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Vectorizers.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Vectorizers.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** LoopTerminology: header/preheader/latch/exits, Loop Simplify Form, LCSSA; Passes: loop-unroll, unroll-and-jam, loop-deletion; Vectorizers: epilogue vectorization/runtime checks

**sourceNote:** Adapted Guarded loop event-domain correspondence from LoopTerminology: header/preheader/latch/exits, Loop Simplify Form, LCSSA; Passes: loop-unroll, unroll-and-jam, loop-deletion; Vectorizers: epilogue vectorization/runtime checks. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-LoopIterationMapping-covers"></a>

### covers

`urn:csabs:operation/LoopIterationMapping-covers`

**signature:** covers : EventMapping→Prop

**description:** Require every source event exactly once for bijective transformations.

**precondition:** No intentional elimination/aggregation in this profile.

**postcondition:** Require every source event exactly once for bijective transformations.

**totality:** Total predicate.

**source:** [LLVM Loop Terminology (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LoopTerminology.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LoopTerminology.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM Pass Reference (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Passes.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Passes.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM Auto-Vectorization (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Vectorizers.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Vectorizers.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** LoopTerminology: header/preheader/latch/exits, Loop Simplify Form, LCSSA; Passes: loop-unroll, unroll-and-jam, loop-deletion; Vectorizers: epilogue vectorization/runtime checks

**sourceNote:** Adapted Guarded loop event-domain correspondence from LoopTerminology: header/preheader/latch/exits, Loop Simplify Form, LCSSA; Passes: loop-unroll, unroll-and-jam, loop-deletion; Vectorizers: epilogue vectorization/runtime checks. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-LoopIterationMapping-bijection"></a>

### bijection

`urn:csabs:axiom/LoopIterationMapping-bijection`

**description:** Defining obligation for Guarded loop event-domain correspondence

**statement:** f maps active target events into active source events, is injective there, and covers every active source event.

**formalStatement:** f maps active target events into active source events, is injective there, and covers every active source event.

**assumptions:** Events include statement identity, loop iteration and lane/unroll slot, including tails and multi-exit control. Zero-trip loops have empty body-event domains. Runtime-guarded versions must each map only their admitted input domain and dispatch must select a correct version. A bijection is a sufficient domain-preservation method for pure rescheduling/unrolling, not a requirement for every valid transformation: dead-event elimination, reductions or idiom replacement require a different refinement relation. Trip count and backedge count differ and unknown is not zero. Dependence ordering, values, exits, divergence and effects remain separate.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Loop Terminology (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LoopTerminology.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LoopTerminology.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM Pass Reference (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Passes.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Passes.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM Auto-Vectorization (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Vectorizers.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Vectorizers.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** LoopTerminology: header/preheader/latch/exits, Loop Simplify Form, LCSSA; Passes: loop-unroll, unroll-and-jam, loop-deletion; Vectorizers: epilogue vectorization/runtime checks

**sourceNote:** Adapted Guarded loop event-domain correspondence from LoopTerminology: header/preheader/latch/exits, Loop Simplify Form, LCSSA; Passes: loop-unroll, unroll-and-jam, loop-deletion; Vectorizers: epilogue vectorization/runtime checks. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

<a id="node-urn-csabs-axiom-LoopIterationMapping-guarded-partition"></a>

### guarded-partition

`urn:csabs:axiom/LoopIterationMapping-guarded-partition`

**description:** Defining obligation for Guarded loop event-domain correspondence

**statement:** Every admitted source input must dispatch to a transformed version whose guard and event correspondence hold, including zero-trip/tail cases.

**formalStatement:** Every admitted source input must dispatch to a transformed version whose guard and event correspondence hold, including zero-trip/tail cases.

**assumptions:** Events include statement identity, loop iteration and lane/unroll slot, including tails and multi-exit control. Zero-trip loops have empty body-event domains. Runtime-guarded versions must each map only their admitted input domain and dispatch must select a correct version. A bijection is a sufficient domain-preservation method for pure rescheduling/unrolling, not a requirement for every valid transformation: dead-event elimination, reductions or idiom replacement require a different refinement relation. Trip count and backedge count differ and unknown is not zero. Dependence ordering, values, exits, divergence and effects remain separate.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Loop Terminology (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LoopTerminology.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LoopTerminology.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM Pass Reference (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Passes.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Passes.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM Auto-Vectorization (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Vectorizers.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Vectorizers.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** LoopTerminology: header/preheader/latch/exits, Loop Simplify Form, LCSSA; Passes: loop-unroll, unroll-and-jam, loop-deletion; Vectorizers: epilogue vectorization/runtime checks

**sourceNote:** Adapted Guarded loop event-domain correspondence from LoopTerminology: header/preheader/latch/exits, Loop Simplify Form, LCSSA; Passes: loop-unroll, unroll-and-jam, loop-deletion; Vectorizers: epilogue vectorization/runtime checks. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

## Laws

<a id="node-urn-csabs-law-LoopIterationMapping-empty-domain-preservation"></a>

### empty-domain-preservation

`urn:csabs:law/LoopIterationMapping-empty-domain-preservation`

**description:** Derived consequence in the stated profile.

**statement:** For a bijective event mapping, Dsource=∅ iff Dtarget=∅.

**formalStatement:** For a bijective event mapping, Dsource=∅ iff Dtarget=∅.

**assumptions:** Events include statement identity, loop iteration and lane/unroll slot, including tails and multi-exit control. Zero-trip loops have empty body-event domains. Runtime-guarded versions must each map only their admitted input domain and dispatch must select a correct version. A bijection is a sufficient domain-preservation method for pure rescheduling/unrolling, not a requirement for every valid transformation: dead-event elimination, reductions or idiom replacement require a different refinement relation. Trip count and backedge count differ and unknown is not zero. Dependence ordering, values, exits, divergence and effects remain separate.

**dependsOn:** [bijection](LoopIterationMapping.md#node-urn-csabs-axiom-LoopIterationMapping-bijection)

**proofSketch:** If Dsource is empty, active-target mapping rules out any target event. If Dtarget is empty, source coverage rules out any source event.

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Loop Terminology (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LoopTerminology.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LoopTerminology.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM Pass Reference (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Passes.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Passes.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM Auto-Vectorization (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Vectorizers.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Vectorizers.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** LoopTerminology: header/preheader/latch/exits, Loop Simplify Form, LCSSA; Passes: loop-unroll, unroll-and-jam, loop-deletion; Vectorizers: epilogue vectorization/runtime checks

**sourceNote:** Catalog derivation from the explicit dependsOn premises; the cited source motivates the interface, not this exact editorial theorem name.

**provenanceKind:** derived

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [LLVM Loop Terminology (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LoopTerminology.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LoopTerminology.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface
- [LLVM Pass Reference (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Passes.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Passes.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface
- [LLVM Auto-Vectorization (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Vectorizers.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Vectorizers.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** LoopTerminology: header/preheader/latch/exits, Loop Simplify Form, LCSSA; Passes: loop-unroll, unroll-and-jam, loop-deletion; Vectorizers: epilogue vectorization/runtime checks

**sourceNote:** Adapted Guarded loop event-domain correspondence from LoopTerminology: header/preheader/latch/exits, Loop Simplify Form, LCSSA; Passes: loop-unroll, unroll-and-jam, loop-deletion; Vectorizers: epilogue vectorization/runtime checks. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/LoopIterationMapping",
    "type": "Concept",
    "shortForm": "LoopIterationMapping",
    "fullName": "Guarded loop event-domain correspondence",
    "definition": "A correspondence between active source and transformed dynamic loop events, separating coverage and uniqueness from schedule, value and dependence preservation.",
    "notation": "f:Dtarget→Dsource is bijective on active events; schedule/value obligations are separate",
    "category": [
      "urn:csabs:category/compiler-transformations"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "requiresConcept": [
      "urn:csabs:concept/LoopDependence",
      "urn:csabs:concept/ControlFlowRefinement"
    ],
    "relatedConcept": [
      "urn:csabs:concept/ScalarRecurrence",
      "urn:csabs:concept/IntegerAffineMap",
      "urn:csabs:concept/PredicatedVectorSemantics"
    ],
    "hasOperation": [
      "urn:csabs:operation/LoopIterationMapping-original-event",
      "urn:csabs:operation/LoopIterationMapping-covers"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/LoopIterationMapping-bijection",
      "urn:csabs:axiom/LoopIterationMapping-guarded-partition"
    ],
    "hasLaw": [
      "urn:csabs:law/LoopIterationMapping-empty-domain-preservation"
    ],
    "hasTheorem": [],
    "basisKind": "relational-structural-definition",
    "basisScope": "Events include statement identity, loop iteration and lane/unroll slot, including tails and multi-exit control. Zero-trip loops have empty body-event domains. Runtime-guarded versions must each map only their admitted input domain and dispatch must select a correct version. A bijection is a sufficient domain-preservation method for pure rescheduling/unrolling, not a requirement for every valid transformation: dead-event elimination, reductions or idiom replacement require a different refinement relation. Trip count and backedge count differ and unknown is not zero. Dependence ordering, values, exits, divergence and effects remain separate.",
    "axiomBasis": "f maps active target events into active source events, is injective there, and covers every active source event.; Every admitted source input must dispatch to a transformed version whose guard and event correspondence hold, including zero-trip/tail cases.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.",
    "verificationObligation": [
      "Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.",
      "No schedule, loop exit, scalar-value, recurrence, runtime-dispatch or dependence proof. Bijection is not presented as a complete characterization of loop correctness."
    ],
    "source": [
      "urn:csabs:source/compiler-loops",
      "urn:csabs:source/compiler-pass-reference",
      "urn:csabs:source/compiler-vectors"
    ],
    "sourceLocator": "LoopTerminology: header/preheader/latch/exits, Loop Simplify Form, LCSSA; Passes: loop-unroll, unroll-and-jam, loop-deletion; Vectorizers: epilogue vectorization/runtime checks",
    "sourceNote": "Adapted Guarded loop event-domain correspondence from LoopTerminology: header/preheader/latch/exits, Loop Simplify Form, LCSSA; Passes: loop-unroll, unroll-and-jam, loop-deletion; Vectorizers: epilogue vectorization/runtime checks. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "mathematicalFormulation": "A correspondence between active source and transformed dynamic loop events, separating coverage and uniqueness from schedule, value and dependence preservation. f:Dtarget→Dsource is bijective on active events; schedule/value obligations are separate Events include statement identity, loop iteration and lane/unroll slot, including tails and multi-exit control. Zero-trip loops have empty body-event domains. Runtime-guarded versions must each map only their admitted input domain and dispatch must select a correct version. A bijection is a sufficient domain-preservation method for pure rescheduling/unrolling, not a requirement for every valid transformation: dead-event elimination, reductions or idiom replacement require a different refinement relation. Trip count and backedge count differ and unknown is not zero. Dependence ordering, values, exits, divergence and effects remain separate.",
    "leanFormulation": "structure LoopIterationMapping (S T : Type u) where\n  sourceActive : Set S\n  targetActive : Set T\n  original : T → S\n  mapsActive : ∀ t ∈ targetActive, original t ∈ sourceActive\n  covers : ∀ s ∈ sourceActive, ∃ t ∈ targetActive, original t = s\n  unique : ∀ t ∈ targetActive, ∀ t' ∈ targetActive, original t = original t' → t = t'",
    "formulationSource": "urn:csabs:source/compiler-llvm-lean",
    "formulationLocator": "Catalog.LLVM.LoopIterationMapping",
    "formulationScope": "partial",
    "leanModelMapping": "Active source/target sets, original-event map and explicit active/injective/covering laws.",
    "leanModelLimitations": "No schedule, loop exit, scalar-value, recurrence, runtime-dispatch or dependence proof. Bijection is not presented as a complete characterization of loop correctness."
  },
  {
    "id": "urn:csabs:operation/LoopIterationMapping-original-event",
    "type": "Operation",
    "name": "original-event",
    "signature": "originalEvent : Dtarget→Dsource",
    "description": "Associate each active transformed event with its original statement/iteration.",
    "concept": "urn:csabs:concept/LoopIterationMapping",
    "precondition": "Relevant runtime guard and tail domain fixed.",
    "postcondition": "Associate each active transformed event with its original statement/iteration.",
    "totality": "Total on active target events.",
    "source": [
      "urn:csabs:source/compiler-loops",
      "urn:csabs:source/compiler-pass-reference",
      "urn:csabs:source/compiler-vectors"
    ],
    "sourceLocator": "LoopTerminology: header/preheader/latch/exits, Loop Simplify Form, LCSSA; Passes: loop-unroll, unroll-and-jam, loop-deletion; Vectorizers: epilogue vectorization/runtime checks",
    "sourceNote": "Adapted Guarded loop event-domain correspondence from LoopTerminology: header/preheader/latch/exits, Loop Simplify Form, LCSSA; Passes: loop-unroll, unroll-and-jam, loop-deletion; Vectorizers: epilogue vectorization/runtime checks. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/LoopIterationMapping-covers",
    "type": "Operation",
    "name": "covers",
    "signature": "covers : EventMapping→Prop",
    "description": "Require every source event exactly once for bijective transformations.",
    "concept": "urn:csabs:concept/LoopIterationMapping",
    "precondition": "No intentional elimination/aggregation in this profile.",
    "postcondition": "Require every source event exactly once for bijective transformations.",
    "totality": "Total predicate.",
    "source": [
      "urn:csabs:source/compiler-loops",
      "urn:csabs:source/compiler-pass-reference",
      "urn:csabs:source/compiler-vectors"
    ],
    "sourceLocator": "LoopTerminology: header/preheader/latch/exits, Loop Simplify Form, LCSSA; Passes: loop-unroll, unroll-and-jam, loop-deletion; Vectorizers: epilogue vectorization/runtime checks",
    "sourceNote": "Adapted Guarded loop event-domain correspondence from LoopTerminology: header/preheader/latch/exits, Loop Simplify Form, LCSSA; Passes: loop-unroll, unroll-and-jam, loop-deletion; Vectorizers: epilogue vectorization/runtime checks. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/LoopIterationMapping-bijection",
    "type": "Axiom",
    "name": "bijection",
    "description": "Defining obligation for Guarded loop event-domain correspondence",
    "statement": "f maps active target events into active source events, is injective there, and covers every active source event.",
    "formalStatement": "f maps active target events into active source events, is injective there, and covers every active source event.",
    "assumptions": [
      "Events include statement identity, loop iteration and lane/unroll slot, including tails and multi-exit control. Zero-trip loops have empty body-event domains. Runtime-guarded versions must each map only their admitted input domain and dispatch must select a correct version. A bijection is a sufficient domain-preservation method for pure rescheduling/unrolling, not a requirement for every valid transformation: dead-event elimination, reductions or idiom replacement require a different refinement relation. Trip count and backedge count differ and unknown is not zero. Dependence ordering, values, exits, divergence and effects remain separate."
    ],
    "appliesTo": [
      "urn:csabs:concept/LoopIterationMapping"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-loops",
      "urn:csabs:source/compiler-pass-reference",
      "urn:csabs:source/compiler-vectors"
    ],
    "sourceLocator": "LoopTerminology: header/preheader/latch/exits, Loop Simplify Form, LCSSA; Passes: loop-unroll, unroll-and-jam, loop-deletion; Vectorizers: epilogue vectorization/runtime checks",
    "sourceNote": "Adapted Guarded loop event-domain correspondence from LoopTerminology: header/preheader/latch/exits, Loop Simplify Form, LCSSA; Passes: loop-unroll, unroll-and-jam, loop-deletion; Vectorizers: epilogue vectorization/runtime checks. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:axiom/LoopIterationMapping-guarded-partition",
    "type": "Axiom",
    "name": "guarded-partition",
    "description": "Defining obligation for Guarded loop event-domain correspondence",
    "statement": "Every admitted source input must dispatch to a transformed version whose guard and event correspondence hold, including zero-trip/tail cases.",
    "formalStatement": "Every admitted source input must dispatch to a transformed version whose guard and event correspondence hold, including zero-trip/tail cases.",
    "assumptions": [
      "Events include statement identity, loop iteration and lane/unroll slot, including tails and multi-exit control. Zero-trip loops have empty body-event domains. Runtime-guarded versions must each map only their admitted input domain and dispatch must select a correct version. A bijection is a sufficient domain-preservation method for pure rescheduling/unrolling, not a requirement for every valid transformation: dead-event elimination, reductions or idiom replacement require a different refinement relation. Trip count and backedge count differ and unknown is not zero. Dependence ordering, values, exits, divergence and effects remain separate."
    ],
    "appliesTo": [
      "urn:csabs:concept/LoopIterationMapping"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-loops",
      "urn:csabs:source/compiler-pass-reference",
      "urn:csabs:source/compiler-vectors"
    ],
    "sourceLocator": "LoopTerminology: header/preheader/latch/exits, Loop Simplify Form, LCSSA; Passes: loop-unroll, unroll-and-jam, loop-deletion; Vectorizers: epilogue vectorization/runtime checks",
    "sourceNote": "Adapted Guarded loop event-domain correspondence from LoopTerminology: header/preheader/latch/exits, Loop Simplify Form, LCSSA; Passes: loop-unroll, unroll-and-jam, loop-deletion; Vectorizers: epilogue vectorization/runtime checks. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:law/LoopIterationMapping-empty-domain-preservation",
    "type": "Law",
    "name": "empty-domain-preservation",
    "description": "Derived consequence in the stated profile.",
    "statement": "For a bijective event mapping, Dsource=∅ iff Dtarget=∅.",
    "formalStatement": "For a bijective event mapping, Dsource=∅ iff Dtarget=∅.",
    "assumptions": [
      "Events include statement identity, loop iteration and lane/unroll slot, including tails and multi-exit control. Zero-trip loops have empty body-event domains. Runtime-guarded versions must each map only their admitted input domain and dispatch must select a correct version. A bijection is a sufficient domain-preservation method for pure rescheduling/unrolling, not a requirement for every valid transformation: dead-event elimination, reductions or idiom replacement require a different refinement relation. Trip count and backedge count differ and unknown is not zero. Dependence ordering, values, exits, divergence and effects remain separate."
    ],
    "appliesTo": [
      "urn:csabs:concept/LoopIterationMapping"
    ],
    "dependsOn": [
      "urn:csabs:axiom/LoopIterationMapping-bijection"
    ],
    "proofSketch": "If Dsource is empty, active-target mapping rules out any target event. If Dtarget is empty, source coverage rules out any source event.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-loops",
      "urn:csabs:source/compiler-pass-reference",
      "urn:csabs:source/compiler-vectors"
    ],
    "sourceLocator": "LoopTerminology: header/preheader/latch/exits, Loop Simplify Form, LCSSA; Passes: loop-unroll, unroll-and-jam, loop-deletion; Vectorizers: epilogue vectorization/runtime checks",
    "sourceNote": "Catalog derivation from the explicit dependsOn premises; the cited source motivates the interface, not this exact editorial theorem name.",
    "provenanceKind": "derived",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  }
]
```
<!-- graph-record:end -->
