# Instrumented trace projection and runtime contract

A contract relating an instrumented/lowered program to source behavior by projecting explicitly designated runtime events while retaining required diagnostics, initialization and runtime protocol behavior.

**Notation:** erase:TargetEvent→List(SourceEvent); projectedTrace=flatMap(erase,targetTrace)

**Stable ID:** `urn:csabs:concept/RuntimeInstrumentation`

**Categories:** Programming-language semantics → Compiler transformations

**Kind:** semantic-model

**Prerequisites:** [Observable behavior refinement (ObservationalRefinement)](BehaviorRefinement.md), [Observable state representation relation](StateRepresentation.md), [Call-boundary behavior and effect contract](CallEffectContract.md)

**Related concepts:** [Normal, exceptional and nonlocal control outcomes](ExceptionalControlFlow.md), [Scoped atomic execution graph and memory ordering](AtomicMemoryModel.md)

## Backlinks

- [Normal, exceptional and nonlocal control outcomes](ExceptionalControlFlow.md) — `relatedConcept`

## Mathematical formulation

A contract relating an instrumented/lowered program to source behavior by projecting explicitly designated runtime events while retaining required diagnostics, initialization and runtime protocol behavior. erase:TargetEvent→List(SourceEvent); projectedTrace=flatMap(erase,targetTrace) Projection and input/runtime assumptions are explicit: added helper memory must be isolated, valid and initialized; helper calls may fail, throw or diverge unless excluded by a justified runtime contract. For valid source executions, project only agreed internal instrumentation events. On invalid source behavior sanitizer diagnostics may intentionally change observables; completeness of bug detection is a separate goal. Profiling counters/reports, synchronization and resource/timing effects are observable if the contract includes them. GC statepoints/stack maps and runtime relocations cannot be erased without their protocol invariant. An opt-instrumented pass is not automatically an ordinary behavior-preserving optimization.

**Lean formulation** (in its source module context):

```lean
structure RuntimeInstrumentation (SourceEvent TargetEvent : Type u) where
  erase : TargetEvent → List SourceEvent
  acceptedExecution : List TargetEvent → Prop
```

**Source:** [`Catalog.LLVM.RuntimeInstrumentation`](../lean/Catalog/LLVMTransforms.lean); consulted 2026-11-16.

**Scope:** partial

**Interpretation:** Per-event finite-list erasure and accepted-execution predicate; eraseInstrumentation is list flatMap.

**Limits:** No sanitizer/profiler/GC implementation, invalid-input detection proof, helper-runtime safety proof or infinite-trace projection. Semantic transparency requires extra runtime assumptions.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** project([e₁,…,eₙ])=erase(e₁)++…++erase(eₙ), including project([])=[].; For admitted source inputs and valid runtime executions, projected target behavior must be source-permitted, except explicitly specified diagnostic/contract-changing outcomes.

**basisKind:** relational-structural-definition

**basisScope:** Projection and input/runtime assumptions are explicit: added helper memory must be isolated, valid and initialized; helper calls may fail, throw or diverge unless excluded by a justified runtime contract. For valid source executions, project only agreed internal instrumentation events. On invalid source behavior sanitizer diagnostics may intentionally change observables; completeness of bug detection is a separate goal. Profiling counters/reports, synchronization and resource/timing effects are observable if the contract includes them. GC statepoints/stack maps and runtime relocations cannot be erased without their protocol invariant. An opt-instrumented pass is not automatically an ordinary behavior-preserving optimization.

**verificationObligation:** Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.; No sanitizer/profiler/GC implementation, invalid-input detection proof, helper-runtime safety proof or infinite-trace projection. Semantic transparency requires extra runtime assumptions.

**reviewStatus:** Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-RuntimeInstrumentation-project"></a>

### project

`urn:csabs:operation/RuntimeInstrumentation-project`

**signature:** project : TargetTrace→SourceTrace

**description:** Erase/map only events explicitly classified as internal by the selected runtime contract.

**precondition:** Public diagnostics/outputs and required protocol effects retained.

**postcondition:** Erase/map only events explicitly classified as internal by the selected runtime contract.

**totality:** Total trace function on supplied events.

**source:** [LLVM AddressSanitizer instrumentation implementation (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/lib/Transforms/Instrumentation/AddressSanitizer.cpp); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/lib/Transforms/Instrumentation/AddressSanitizer.cpp; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM instrumentation-profile lowering implementation (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/lib/Transforms/Instrumentation/InstrProfiling.cpp); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/lib/Transforms/Instrumentation/InstrProfiling.cpp; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM GC Statepoints (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Statepoints.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Statepoints.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** AddressSanitizer.cpp introduction; InstrProfiling.cpp introduction; Statepoints motivation; LangRef operand bundles

**sourceNote:** Adapted Instrumented trace projection and runtime contract from AddressSanitizer.cpp introduction; InstrProfiling.cpp introduction; Statepoints motivation; LangRef operand bundles. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-RuntimeInstrumentation-valid-runtime"></a>

### valid-runtime

`urn:csabs:operation/RuntimeInstrumentation-valid-runtime`

**signature:** validRuntime : Execution→Prop

**description:** Require helper, shadow-state, root/relocation and initialization invariants.

**precondition:** Exact instrumentation/runtime/target profile specified.

**postcondition:** Require helper, shadow-state, root/relocation and initialization invariants.

**totality:** Semantic predicate.

**source:** [LLVM AddressSanitizer instrumentation implementation (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/lib/Transforms/Instrumentation/AddressSanitizer.cpp); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/lib/Transforms/Instrumentation/AddressSanitizer.cpp; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM instrumentation-profile lowering implementation (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/lib/Transforms/Instrumentation/InstrProfiling.cpp); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/lib/Transforms/Instrumentation/InstrProfiling.cpp; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM GC Statepoints (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Statepoints.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Statepoints.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** AddressSanitizer.cpp introduction; InstrProfiling.cpp introduction; Statepoints motivation; LangRef operand bundles

**sourceNote:** Adapted Instrumented trace projection and runtime contract from AddressSanitizer.cpp introduction; InstrProfiling.cpp introduction; Statepoints motivation; LangRef operand bundles. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-RuntimeInstrumentation-projection"></a>

### projection

`urn:csabs:axiom/RuntimeInstrumentation-projection`

**description:** Defining obligation for Instrumented trace projection and runtime contract

**statement:** project([e₁,…,eₙ])=erase(e₁)++…++erase(eₙ), including project([])=[].

**formalStatement:** project([e₁,…,eₙ])=erase(e₁)++…++erase(eₙ), including project([])=[].

**assumptions:** Projection and input/runtime assumptions are explicit: added helper memory must be isolated, valid and initialized; helper calls may fail, throw or diverge unless excluded by a justified runtime contract. For valid source executions, project only agreed internal instrumentation events. On invalid source behavior sanitizer diagnostics may intentionally change observables; completeness of bug detection is a separate goal. Profiling counters/reports, synchronization and resource/timing effects are observable if the contract includes them. GC statepoints/stack maps and runtime relocations cannot be erased without their protocol invariant. An opt-instrumented pass is not automatically an ordinary behavior-preserving optimization.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM AddressSanitizer instrumentation implementation (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/lib/Transforms/Instrumentation/AddressSanitizer.cpp); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/lib/Transforms/Instrumentation/AddressSanitizer.cpp; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM instrumentation-profile lowering implementation (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/lib/Transforms/Instrumentation/InstrProfiling.cpp); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/lib/Transforms/Instrumentation/InstrProfiling.cpp; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM GC Statepoints (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Statepoints.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Statepoints.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** AddressSanitizer.cpp introduction; InstrProfiling.cpp introduction; Statepoints motivation; LangRef operand bundles

**sourceNote:** Adapted Instrumented trace projection and runtime contract from AddressSanitizer.cpp introduction; InstrProfiling.cpp introduction; Statepoints motivation; LangRef operand bundles. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

<a id="node-urn-csabs-axiom-RuntimeInstrumentation-runtime-refinement"></a>

### runtime-refinement

`urn:csabs:axiom/RuntimeInstrumentation-runtime-refinement`

**description:** Defining obligation for Instrumented trace projection and runtime contract

**statement:** For admitted source inputs and valid runtime executions, projected target behavior must be source-permitted, except explicitly specified diagnostic/contract-changing outcomes.

**formalStatement:** For admitted source inputs and valid runtime executions, projected target behavior must be source-permitted, except explicitly specified diagnostic/contract-changing outcomes.

**assumptions:** Projection and input/runtime assumptions are explicit: added helper memory must be isolated, valid and initialized; helper calls may fail, throw or diverge unless excluded by a justified runtime contract. For valid source executions, project only agreed internal instrumentation events. On invalid source behavior sanitizer diagnostics may intentionally change observables; completeness of bug detection is a separate goal. Profiling counters/reports, synchronization and resource/timing effects are observable if the contract includes them. GC statepoints/stack maps and runtime relocations cannot be erased without their protocol invariant. An opt-instrumented pass is not automatically an ordinary behavior-preserving optimization.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM AddressSanitizer instrumentation implementation (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/lib/Transforms/Instrumentation/AddressSanitizer.cpp); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/lib/Transforms/Instrumentation/AddressSanitizer.cpp; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM instrumentation-profile lowering implementation (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/lib/Transforms/Instrumentation/InstrProfiling.cpp); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/lib/Transforms/Instrumentation/InstrProfiling.cpp; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM GC Statepoints (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Statepoints.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Statepoints.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** AddressSanitizer.cpp introduction; InstrProfiling.cpp introduction; Statepoints motivation; LangRef operand bundles

**sourceNote:** Adapted Instrumented trace projection and runtime contract from AddressSanitizer.cpp introduction; InstrProfiling.cpp introduction; Statepoints motivation; LangRef operand bundles. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

## Laws

<a id="node-urn-csabs-law-RuntimeInstrumentation-projection-concatenation"></a>

### projection-concatenation

`urn:csabs:law/RuntimeInstrumentation-projection-concatenation`

**description:** Derived consequence in the stated profile.

**statement:** project(t₁++t₂)=project(t₁)++project(t₂).

**formalStatement:** project(t₁++t₂)=project(t₁)++project(t₂).

**assumptions:** Projection and input/runtime assumptions are explicit: added helper memory must be isolated, valid and initialized; helper calls may fail, throw or diverge unless excluded by a justified runtime contract. For valid source executions, project only agreed internal instrumentation events. On invalid source behavior sanitizer diagnostics may intentionally change observables; completeness of bug detection is a separate goal. Profiling counters/reports, synchronization and resource/timing effects are observable if the contract includes them. GC statepoints/stack maps and runtime relocations cannot be erased without their protocol invariant. An opt-instrumented pass is not automatically an ordinary behavior-preserving optimization.

**dependsOn:** [projection](RuntimeInstrumentation.md#node-urn-csabs-axiom-RuntimeInstrumentation-projection)

**proofSketch:** Expand flatMap over the concatenated finite lists, preserving event order. Infinite traces and termination need separate semantics.

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM AddressSanitizer instrumentation implementation (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/lib/Transforms/Instrumentation/AddressSanitizer.cpp); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/lib/Transforms/Instrumentation/AddressSanitizer.cpp; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM instrumentation-profile lowering implementation (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/lib/Transforms/Instrumentation/InstrProfiling.cpp); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/lib/Transforms/Instrumentation/InstrProfiling.cpp; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM GC Statepoints (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Statepoints.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Statepoints.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** AddressSanitizer.cpp introduction; InstrProfiling.cpp introduction; Statepoints motivation; LangRef operand bundles

**sourceNote:** Catalog derivation from the explicit dependsOn premises; the cited source motivates the interface, not this exact editorial theorem name.

**provenanceKind:** derived

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [LLVM AddressSanitizer instrumentation implementation (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/lib/Transforms/Instrumentation/AddressSanitizer.cpp); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/lib/Transforms/Instrumentation/AddressSanitizer.cpp; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface
- [LLVM instrumentation-profile lowering implementation (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/lib/Transforms/Instrumentation/InstrProfiling.cpp); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/lib/Transforms/Instrumentation/InstrProfiling.cpp; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface
- [LLVM GC Statepoints (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Statepoints.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Statepoints.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface
- [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** AddressSanitizer.cpp introduction; InstrProfiling.cpp introduction; Statepoints motivation; LangRef operand bundles

**sourceNote:** Adapted Instrumented trace projection and runtime contract from AddressSanitizer.cpp introduction; InstrProfiling.cpp introduction; Statepoints motivation; LangRef operand bundles. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/RuntimeInstrumentation",
    "type": "Concept",
    "shortForm": "RuntimeInstrumentation",
    "fullName": "Instrumented trace projection and runtime contract",
    "definition": "A contract relating an instrumented/lowered program to source behavior by projecting explicitly designated runtime events while retaining required diagnostics, initialization and runtime protocol behavior.",
    "notation": "erase:TargetEvent→List(SourceEvent); projectedTrace=flatMap(erase,targetTrace)",
    "category": [
      "urn:csabs:category/compiler-transformations"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "requiresConcept": [
      "urn:csabs:concept/BehaviorRefinement",
      "urn:csabs:concept/StateRepresentation",
      "urn:csabs:concept/CallEffectContract"
    ],
    "relatedConcept": [
      "urn:csabs:concept/ExceptionalControlFlow",
      "urn:csabs:concept/AtomicMemoryModel"
    ],
    "hasOperation": [
      "urn:csabs:operation/RuntimeInstrumentation-project",
      "urn:csabs:operation/RuntimeInstrumentation-valid-runtime"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/RuntimeInstrumentation-projection",
      "urn:csabs:axiom/RuntimeInstrumentation-runtime-refinement"
    ],
    "hasLaw": [
      "urn:csabs:law/RuntimeInstrumentation-projection-concatenation"
    ],
    "hasTheorem": [],
    "basisKind": "relational-structural-definition",
    "basisScope": "Projection and input/runtime assumptions are explicit: added helper memory must be isolated, valid and initialized; helper calls may fail, throw or diverge unless excluded by a justified runtime contract. For valid source executions, project only agreed internal instrumentation events. On invalid source behavior sanitizer diagnostics may intentionally change observables; completeness of bug detection is a separate goal. Profiling counters/reports, synchronization and resource/timing effects are observable if the contract includes them. GC statepoints/stack maps and runtime relocations cannot be erased without their protocol invariant. An opt-instrumented pass is not automatically an ordinary behavior-preserving optimization.",
    "axiomBasis": "project([e₁,…,eₙ])=erase(e₁)++…++erase(eₙ), including project([])=[].; For admitted source inputs and valid runtime executions, projected target behavior must be source-permitted, except explicitly specified diagnostic/contract-changing outcomes.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.",
    "verificationObligation": [
      "Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.",
      "No sanitizer/profiler/GC implementation, invalid-input detection proof, helper-runtime safety proof or infinite-trace projection. Semantic transparency requires extra runtime assumptions."
    ],
    "source": [
      "urn:csabs:source/compiler-asan",
      "urn:csabs:source/compiler-instrprof",
      "urn:csabs:source/compiler-statepoints",
      "urn:csabs:source/compiler-llvm"
    ],
    "sourceLocator": "AddressSanitizer.cpp introduction; InstrProfiling.cpp introduction; Statepoints motivation; LangRef operand bundles",
    "sourceNote": "Adapted Instrumented trace projection and runtime contract from AddressSanitizer.cpp introduction; InstrProfiling.cpp introduction; Statepoints motivation; LangRef operand bundles. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "mathematicalFormulation": "A contract relating an instrumented/lowered program to source behavior by projecting explicitly designated runtime events while retaining required diagnostics, initialization and runtime protocol behavior. erase:TargetEvent→List(SourceEvent); projectedTrace=flatMap(erase,targetTrace) Projection and input/runtime assumptions are explicit: added helper memory must be isolated, valid and initialized; helper calls may fail, throw or diverge unless excluded by a justified runtime contract. For valid source executions, project only agreed internal instrumentation events. On invalid source behavior sanitizer diagnostics may intentionally change observables; completeness of bug detection is a separate goal. Profiling counters/reports, synchronization and resource/timing effects are observable if the contract includes them. GC statepoints/stack maps and runtime relocations cannot be erased without their protocol invariant. An opt-instrumented pass is not automatically an ordinary behavior-preserving optimization.",
    "leanFormulation": "structure RuntimeInstrumentation (SourceEvent TargetEvent : Type u) where\n  erase : TargetEvent → List SourceEvent\n  acceptedExecution : List TargetEvent → Prop",
    "formulationSource": "urn:csabs:source/compiler-llvm-lean",
    "formulationLocator": "Catalog.LLVM.RuntimeInstrumentation",
    "formulationScope": "partial",
    "leanModelMapping": "Per-event finite-list erasure and accepted-execution predicate; eraseInstrumentation is list flatMap.",
    "leanModelLimitations": "No sanitizer/profiler/GC implementation, invalid-input detection proof, helper-runtime safety proof or infinite-trace projection. Semantic transparency requires extra runtime assumptions."
  },
  {
    "id": "urn:csabs:operation/RuntimeInstrumentation-project",
    "type": "Operation",
    "name": "project",
    "signature": "project : TargetTrace→SourceTrace",
    "description": "Erase/map only events explicitly classified as internal by the selected runtime contract.",
    "concept": "urn:csabs:concept/RuntimeInstrumentation",
    "precondition": "Public diagnostics/outputs and required protocol effects retained.",
    "postcondition": "Erase/map only events explicitly classified as internal by the selected runtime contract.",
    "totality": "Total trace function on supplied events.",
    "source": [
      "urn:csabs:source/compiler-asan",
      "urn:csabs:source/compiler-instrprof",
      "urn:csabs:source/compiler-statepoints",
      "urn:csabs:source/compiler-llvm"
    ],
    "sourceLocator": "AddressSanitizer.cpp introduction; InstrProfiling.cpp introduction; Statepoints motivation; LangRef operand bundles",
    "sourceNote": "Adapted Instrumented trace projection and runtime contract from AddressSanitizer.cpp introduction; InstrProfiling.cpp introduction; Statepoints motivation; LangRef operand bundles. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/RuntimeInstrumentation-valid-runtime",
    "type": "Operation",
    "name": "valid-runtime",
    "signature": "validRuntime : Execution→Prop",
    "description": "Require helper, shadow-state, root/relocation and initialization invariants.",
    "concept": "urn:csabs:concept/RuntimeInstrumentation",
    "precondition": "Exact instrumentation/runtime/target profile specified.",
    "postcondition": "Require helper, shadow-state, root/relocation and initialization invariants.",
    "totality": "Semantic predicate.",
    "source": [
      "urn:csabs:source/compiler-asan",
      "urn:csabs:source/compiler-instrprof",
      "urn:csabs:source/compiler-statepoints",
      "urn:csabs:source/compiler-llvm"
    ],
    "sourceLocator": "AddressSanitizer.cpp introduction; InstrProfiling.cpp introduction; Statepoints motivation; LangRef operand bundles",
    "sourceNote": "Adapted Instrumented trace projection and runtime contract from AddressSanitizer.cpp introduction; InstrProfiling.cpp introduction; Statepoints motivation; LangRef operand bundles. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/RuntimeInstrumentation-projection",
    "type": "Axiom",
    "name": "projection",
    "description": "Defining obligation for Instrumented trace projection and runtime contract",
    "statement": "project([e₁,…,eₙ])=erase(e₁)++…++erase(eₙ), including project([])=[].",
    "formalStatement": "project([e₁,…,eₙ])=erase(e₁)++…++erase(eₙ), including project([])=[].",
    "assumptions": [
      "Projection and input/runtime assumptions are explicit: added helper memory must be isolated, valid and initialized; helper calls may fail, throw or diverge unless excluded by a justified runtime contract. For valid source executions, project only agreed internal instrumentation events. On invalid source behavior sanitizer diagnostics may intentionally change observables; completeness of bug detection is a separate goal. Profiling counters/reports, synchronization and resource/timing effects are observable if the contract includes them. GC statepoints/stack maps and runtime relocations cannot be erased without their protocol invariant. An opt-instrumented pass is not automatically an ordinary behavior-preserving optimization."
    ],
    "appliesTo": [
      "urn:csabs:concept/RuntimeInstrumentation"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-asan",
      "urn:csabs:source/compiler-instrprof",
      "urn:csabs:source/compiler-statepoints",
      "urn:csabs:source/compiler-llvm"
    ],
    "sourceLocator": "AddressSanitizer.cpp introduction; InstrProfiling.cpp introduction; Statepoints motivation; LangRef operand bundles",
    "sourceNote": "Adapted Instrumented trace projection and runtime contract from AddressSanitizer.cpp introduction; InstrProfiling.cpp introduction; Statepoints motivation; LangRef operand bundles. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:axiom/RuntimeInstrumentation-runtime-refinement",
    "type": "Axiom",
    "name": "runtime-refinement",
    "description": "Defining obligation for Instrumented trace projection and runtime contract",
    "statement": "For admitted source inputs and valid runtime executions, projected target behavior must be source-permitted, except explicitly specified diagnostic/contract-changing outcomes.",
    "formalStatement": "For admitted source inputs and valid runtime executions, projected target behavior must be source-permitted, except explicitly specified diagnostic/contract-changing outcomes.",
    "assumptions": [
      "Projection and input/runtime assumptions are explicit: added helper memory must be isolated, valid and initialized; helper calls may fail, throw or diverge unless excluded by a justified runtime contract. For valid source executions, project only agreed internal instrumentation events. On invalid source behavior sanitizer diagnostics may intentionally change observables; completeness of bug detection is a separate goal. Profiling counters/reports, synchronization and resource/timing effects are observable if the contract includes them. GC statepoints/stack maps and runtime relocations cannot be erased without their protocol invariant. An opt-instrumented pass is not automatically an ordinary behavior-preserving optimization."
    ],
    "appliesTo": [
      "urn:csabs:concept/RuntimeInstrumentation"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-asan",
      "urn:csabs:source/compiler-instrprof",
      "urn:csabs:source/compiler-statepoints",
      "urn:csabs:source/compiler-llvm"
    ],
    "sourceLocator": "AddressSanitizer.cpp introduction; InstrProfiling.cpp introduction; Statepoints motivation; LangRef operand bundles",
    "sourceNote": "Adapted Instrumented trace projection and runtime contract from AddressSanitizer.cpp introduction; InstrProfiling.cpp introduction; Statepoints motivation; LangRef operand bundles. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:law/RuntimeInstrumentation-projection-concatenation",
    "type": "Law",
    "name": "projection-concatenation",
    "description": "Derived consequence in the stated profile.",
    "statement": "project(t₁++t₂)=project(t₁)++project(t₂).",
    "formalStatement": "project(t₁++t₂)=project(t₁)++project(t₂).",
    "assumptions": [
      "Projection and input/runtime assumptions are explicit: added helper memory must be isolated, valid and initialized; helper calls may fail, throw or diverge unless excluded by a justified runtime contract. For valid source executions, project only agreed internal instrumentation events. On invalid source behavior sanitizer diagnostics may intentionally change observables; completeness of bug detection is a separate goal. Profiling counters/reports, synchronization and resource/timing effects are observable if the contract includes them. GC statepoints/stack maps and runtime relocations cannot be erased without their protocol invariant. An opt-instrumented pass is not automatically an ordinary behavior-preserving optimization."
    ],
    "appliesTo": [
      "urn:csabs:concept/RuntimeInstrumentation"
    ],
    "dependsOn": [
      "urn:csabs:axiom/RuntimeInstrumentation-projection"
    ],
    "proofSketch": "Expand flatMap over the concatenated finite lists, preserving event order. Infinite traces and termination need separate semantics.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-asan",
      "urn:csabs:source/compiler-instrprof",
      "urn:csabs:source/compiler-statepoints",
      "urn:csabs:source/compiler-llvm"
    ],
    "sourceLocator": "AddressSanitizer.cpp introduction; InstrProfiling.cpp introduction; Statepoints motivation; LangRef operand bundles",
    "sourceNote": "Catalog derivation from the explicit dependsOn premises; the cited source motivates the interface, not this exact editorial theorem name.",
    "provenanceKind": "derived",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  }
]
```
<!-- graph-record:end -->
