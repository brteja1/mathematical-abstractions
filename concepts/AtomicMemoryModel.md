# Scoped atomic execution graph and memory ordering

An execution-graph interface retaining program order, reads-from, per-location modification order, synchronization and scope when validating concurrent-memory transformations.

**Notation:** Execution=(E,sb,rf,mo,sw,scope); hb=(sb∪sw)⁺; Allowed(execution)

**Stable ID:** `urn:csabs:concept/AtomicMemoryModel`

**Categories:** Programming-language semantics → Compiler transformations

**Kind:** semantic-model

**Prerequisites:** [Happens Before](HappensBefore.md), [Binary relation](Relation.md)

**Related concepts:** [Sequential Consistency](SequentialConsistency.md), [Byte-addressed memory with typed access obligations](ByteMemory.md), [Observable behavior refinement](BehaviorRefinement.md)

## Backlinks

- [Byte-addressed memory with typed access obligations](ByteMemory.md) — `relatedConcept`
- [Control-sensitive communicating thread instances](ConvergentExecution.md) — `relatedConcept`
- [Conservative resource effect summary](EffectSummary.md) — `relatedConcept`
- [Instrumented trace projection and runtime contract](RuntimeInstrumentation.md) — `relatedConcept`

## Mathematical formulation

An execution-graph interface retaining program order, reads-from, per-location modification order, synchronization and scope when validating concurrent-memory transformations. Execution=(E,sb,rf,mo,sw,scope); hb=(sb∪sw)⁺; Allowed(execution) LLVM 21.1.8 atomics and thread-creation environment. Modification order is per location; monotonic does not imply one total order across all locations. Acquire/release synchronization requires the actual reads-from/release-sequence and scope conditions, not only matching labels. Fences, cmpxchg success/failure orderings and RMW atomicity require instruction clauses. seq\_cst has additional constraints and does not impose sequential consistency on all non-seq\_cst events. Volatile is distinct from atomic. Permitted executions include races/UB according to LLVM, not an assumed data-race-free SC model. Cross-thread refinement compares sets of allowed executions/observations.

**Lean formulation** (in its source module context):

```lean
structure AtomicMemoryModel (Event : Type u) where
  programOrder : Event → Event → Prop
  synchronizesWith : Event → Event → Prop
  readsFrom : Event → Event → Prop
  modificationOrder : Event → Event → Prop
  allowed : Prop
```

**Source:** [`Catalog.LLVM.AtomicMemoryModel`](../lean/Catalog/LLVMTransforms.lean); consulted 2026-11-16.

**Scope:** partial

**Interpretation:** Raw execution-edge relations and allowed proposition; atomicHappensBefore computes the stated transitive closure.

**Limits:** No complete LLVM/C++ weak-memory axiomatization, read-value constraints, release sequences, scopes, fences, cmpxchg or race/UB model. Raw edges alone do not certify atomic transformations.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** hb is the transitive closure of the relevant single-thread program order and synchronizes-with edges.; Atomic correctness retains per-location modification order, actual synchronization and scopes; monotonic alone supplies no cross-location global order.

**basisKind:** relational-structural-definition

**basisScope:** LLVM 21.1.8 atomics and thread-creation environment. Modification order is per location; monotonic does not imply one total order across all locations. Acquire/release synchronization requires the actual reads-from/release-sequence and scope conditions, not only matching labels. Fences, cmpxchg success/failure orderings and RMW atomicity require instruction clauses. seq_cst has additional constraints and does not impose sequential consistency on all non-seq_cst events. Volatile is distinct from atomic. Permitted executions include races/UB according to LLVM, not an assumed data-race-free SC model. Cross-thread refinement compares sets of allowed executions/observations.

**verificationObligation:** Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.; No complete LLVM/C++ weak-memory axiomatization, read-value constraints, release sequences, scopes, fences, cmpxchg or race/UB model. Raw edges alone do not certify atomic transformations.

**reviewStatus:** Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-AtomicMemoryModel-allowed"></a>

### allowed

`urn:csabs:operation/AtomicMemoryModel-allowed`

**signature:** allowed : ExecutionGraph→Prop

**description:** Check all relevant consistency, atomicity, reads-from and scope constraints.

**precondition:** Runtime/thread/target memory profile fixed.

**postcondition:** Check all relevant consistency, atomicity, reads-from and scope constraints.

**totality:** Semantic predicate; bounded checking is scoped.

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM Atomic Instructions and Concurrency Guide (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Atomics.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Atomics.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** LangRef: Memory Model for Concurrent Operations, Atomic Memory Ordering Constraints, syncscope, volatile memory accesses; Atomics: Optimization outside atomic, Optimizer restrictions

**sourceNote:** Adapted Scoped atomic execution graph and memory ordering from LangRef: Memory Model for Concurrent Operations, Atomic Memory Ordering Constraints, syncscope, volatile memory accesses; Atomics: Optimization outside atomic, Optimizer restrictions. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-AtomicMemoryModel-happens-before"></a>

### happens-before

`urn:csabs:operation/AtomicMemoryModel-happens-before`

**signature:** hb : Event×Event→Prop

**description:** Take transitive closure of program-order and synchronizes-with edges in the selected thread/signal convention.

**precondition:** The underlying edge generation is semantically justified.

**postcondition:** Take transitive closure of program-order and synchronizes-with edges in the selected thread/signal convention.

**totality:** Total relation.

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM Atomic Instructions and Concurrency Guide (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Atomics.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Atomics.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** LangRef: Memory Model for Concurrent Operations, Atomic Memory Ordering Constraints, syncscope, volatile memory accesses; Atomics: Optimization outside atomic, Optimizer restrictions

**sourceNote:** Adapted Scoped atomic execution graph and memory ordering from LangRef: Memory Model for Concurrent Operations, Atomic Memory Ordering Constraints, syncscope, volatile memory accesses; Atomics: Optimization outside atomic, Optimizer restrictions. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-AtomicMemoryModel-hb-closure"></a>

### hb-closure

`urn:csabs:axiom/AtomicMemoryModel-hb-closure`

**description:** Defining obligation for Scoped atomic execution graph and memory ordering

**statement:** hb is the transitive closure of the relevant single-thread program order and synchronizes-with edges.

**formalStatement:** hb is the transitive closure of the relevant single-thread program order and synchronizes-with edges.

**assumptions:** LLVM 21.1.8 atomics and thread-creation environment. Modification order is per location; monotonic does not imply one total order across all locations. Acquire/release synchronization requires the actual reads-from/release-sequence and scope conditions, not only matching labels. Fences, cmpxchg success/failure orderings and RMW atomicity require instruction clauses. seq_cst has additional constraints and does not impose sequential consistency on all non-seq_cst events. Volatile is distinct from atomic. Permitted executions include races/UB according to LLVM, not an assumed data-race-free SC model. Cross-thread refinement compares sets of allowed executions/observations.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM Atomic Instructions and Concurrency Guide (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Atomics.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Atomics.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** LangRef: Memory Model for Concurrent Operations, Atomic Memory Ordering Constraints, syncscope, volatile memory accesses; Atomics: Optimization outside atomic, Optimizer restrictions

**sourceNote:** Adapted Scoped atomic execution graph and memory ordering from LangRef: Memory Model for Concurrent Operations, Atomic Memory Ordering Constraints, syncscope, volatile memory accesses; Atomics: Optimization outside atomic, Optimizer restrictions. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

<a id="node-urn-csabs-axiom-AtomicMemoryModel-ordering-scope"></a>

### ordering-scope

`urn:csabs:axiom/AtomicMemoryModel-ordering-scope`

**description:** Defining obligation for Scoped atomic execution graph and memory ordering

**statement:** Atomic correctness retains per-location modification order, actual synchronization and scopes; monotonic alone supplies no cross-location global order.

**formalStatement:** Atomic correctness retains per-location modification order, actual synchronization and scopes; monotonic alone supplies no cross-location global order.

**assumptions:** LLVM 21.1.8 atomics and thread-creation environment. Modification order is per location; monotonic does not imply one total order across all locations. Acquire/release synchronization requires the actual reads-from/release-sequence and scope conditions, not only matching labels. Fences, cmpxchg success/failure orderings and RMW atomicity require instruction clauses. seq_cst has additional constraints and does not impose sequential consistency on all non-seq_cst events. Volatile is distinct from atomic. Permitted executions include races/UB according to LLVM, not an assumed data-race-free SC model. Cross-thread refinement compares sets of allowed executions/observations.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM Atomic Instructions and Concurrency Guide (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Atomics.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Atomics.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** LangRef: Memory Model for Concurrent Operations, Atomic Memory Ordering Constraints, syncscope, volatile memory accesses; Atomics: Optimization outside atomic, Optimizer restrictions

**sourceNote:** Adapted Scoped atomic execution graph and memory ordering from LangRef: Memory Model for Concurrent Operations, Atomic Memory Ordering Constraints, syncscope, volatile memory accesses; Atomics: Optimization outside atomic, Optimizer restrictions. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

## Laws

<a id="node-urn-csabs-law-AtomicMemoryModel-synchronization-implies-hb"></a>

### synchronization-implies-hb

`urn:csabs:law/AtomicMemoryModel-synchronization-implies-hb`

**description:** Derived consequence in the stated profile.

**statement:** sw(a,b) ⇒ hb(a,b) for events in the selected model.

**formalStatement:** sw(a,b) ⇒ hb(a,b) for events in the selected model.

**assumptions:** LLVM 21.1.8 atomics and thread-creation environment. Modification order is per location; monotonic does not imply one total order across all locations. Acquire/release synchronization requires the actual reads-from/release-sequence and scope conditions, not only matching labels. Fences, cmpxchg success/failure orderings and RMW atomicity require instruction clauses. seq_cst has additional constraints and does not impose sequential consistency on all non-seq_cst events. Volatile is distinct from atomic. Permitted executions include races/UB according to LLVM, not an assumed data-race-free SC model. Cross-thread refinement compares sets of allowed executions/observations.

**dependsOn:** [hb-closure](AtomicMemoryModel.md#node-urn-csabs-axiom-AtomicMemoryModel-hb-closure)

**proofSketch:** A synchronizes-with edge belongs to the generating relation, hence to its transitive closure.

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM Atomic Instructions and Concurrency Guide (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Atomics.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Atomics.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** LangRef: Memory Model for Concurrent Operations, Atomic Memory Ordering Constraints, syncscope, volatile memory accesses; Atomics: Optimization outside atomic, Optimizer restrictions

**sourceNote:** Catalog derivation from the explicit dependsOn premises; the cited source motivates the interface, not this exact editorial theorem name.

**provenanceKind:** derived

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification
- [LLVM Atomic Instructions and Concurrency Guide (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Atomics.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Atomics.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** LangRef: Memory Model for Concurrent Operations, Atomic Memory Ordering Constraints, syncscope, volatile memory accesses; Atomics: Optimization outside atomic, Optimizer restrictions

**sourceNote:** Adapted Scoped atomic execution graph and memory ordering from LangRef: Memory Model for Concurrent Operations, Atomic Memory Ordering Constraints, syncscope, volatile memory accesses; Atomics: Optimization outside atomic, Optimizer restrictions. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/AtomicMemoryModel",
    "type": "Concept",
    "shortForm": "AtomicMemoryModel",
    "fullName": "Scoped atomic execution graph and memory ordering",
    "definition": "An execution-graph interface retaining program order, reads-from, per-location modification order, synchronization and scope when validating concurrent-memory transformations.",
    "notation": "Execution=(E,sb,rf,mo,sw,scope); hb=(sb∪sw)⁺; Allowed(execution)",
    "category": [
      "urn:csabs:category/compiler-transformations"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "requiresConcept": [
      "urn:csabs:concept/HappensBefore",
      "urn:csabs:concept/Relation"
    ],
    "relatedConcept": [
      "urn:csabs:concept/SequentialConsistency",
      "urn:csabs:concept/ByteMemory",
      "urn:csabs:concept/BehaviorRefinement"
    ],
    "hasOperation": [
      "urn:csabs:operation/AtomicMemoryModel-allowed",
      "urn:csabs:operation/AtomicMemoryModel-happens-before"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/AtomicMemoryModel-hb-closure",
      "urn:csabs:axiom/AtomicMemoryModel-ordering-scope"
    ],
    "hasLaw": [
      "urn:csabs:law/AtomicMemoryModel-synchronization-implies-hb"
    ],
    "hasTheorem": [],
    "basisKind": "relational-structural-definition",
    "basisScope": "LLVM 21.1.8 atomics and thread-creation environment. Modification order is per location; monotonic does not imply one total order across all locations. Acquire/release synchronization requires the actual reads-from/release-sequence and scope conditions, not only matching labels. Fences, cmpxchg success/failure orderings and RMW atomicity require instruction clauses. seq_cst has additional constraints and does not impose sequential consistency on all non-seq_cst events. Volatile is distinct from atomic. Permitted executions include races/UB according to LLVM, not an assumed data-race-free SC model. Cross-thread refinement compares sets of allowed executions/observations.",
    "axiomBasis": "hb is the transitive closure of the relevant single-thread program order and synchronizes-with edges.; Atomic correctness retains per-location modification order, actual synchronization and scopes; monotonic alone supplies no cross-location global order.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.",
    "verificationObligation": [
      "Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.",
      "No complete LLVM/C++ weak-memory axiomatization, read-value constraints, release sequences, scopes, fences, cmpxchg or race/UB model. Raw edges alone do not certify atomic transformations."
    ],
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-atomics"
    ],
    "sourceLocator": "LangRef: Memory Model for Concurrent Operations, Atomic Memory Ordering Constraints, syncscope, volatile memory accesses; Atomics: Optimization outside atomic, Optimizer restrictions",
    "sourceNote": "Adapted Scoped atomic execution graph and memory ordering from LangRef: Memory Model for Concurrent Operations, Atomic Memory Ordering Constraints, syncscope, volatile memory accesses; Atomics: Optimization outside atomic, Optimizer restrictions. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "mathematicalFormulation": "An execution-graph interface retaining program order, reads-from, per-location modification order, synchronization and scope when validating concurrent-memory transformations. Execution=(E,sb,rf,mo,sw,scope); hb=(sb∪sw)⁺; Allowed(execution) LLVM 21.1.8 atomics and thread-creation environment. Modification order is per location; monotonic does not imply one total order across all locations. Acquire/release synchronization requires the actual reads-from/release-sequence and scope conditions, not only matching labels. Fences, cmpxchg success/failure orderings and RMW atomicity require instruction clauses. seq_cst has additional constraints and does not impose sequential consistency on all non-seq_cst events. Volatile is distinct from atomic. Permitted executions include races/UB according to LLVM, not an assumed data-race-free SC model. Cross-thread refinement compares sets of allowed executions/observations.",
    "leanFormulation": "structure AtomicMemoryModel (Event : Type u) where\n  programOrder : Event → Event → Prop\n  synchronizesWith : Event → Event → Prop\n  readsFrom : Event → Event → Prop\n  modificationOrder : Event → Event → Prop\n  allowed : Prop",
    "formulationSource": "urn:csabs:source/compiler-llvm-lean",
    "formulationLocator": "Catalog.LLVM.AtomicMemoryModel",
    "formulationScope": "partial",
    "leanModelMapping": "Raw execution-edge relations and allowed proposition; atomicHappensBefore computes the stated transitive closure.",
    "leanModelLimitations": "No complete LLVM/C++ weak-memory axiomatization, read-value constraints, release sequences, scopes, fences, cmpxchg or race/UB model. Raw edges alone do not certify atomic transformations."
  },
  {
    "id": "urn:csabs:operation/AtomicMemoryModel-allowed",
    "type": "Operation",
    "name": "allowed",
    "signature": "allowed : ExecutionGraph→Prop",
    "description": "Check all relevant consistency, atomicity, reads-from and scope constraints.",
    "concept": "urn:csabs:concept/AtomicMemoryModel",
    "precondition": "Runtime/thread/target memory profile fixed.",
    "postcondition": "Check all relevant consistency, atomicity, reads-from and scope constraints.",
    "totality": "Semantic predicate; bounded checking is scoped.",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-atomics"
    ],
    "sourceLocator": "LangRef: Memory Model for Concurrent Operations, Atomic Memory Ordering Constraints, syncscope, volatile memory accesses; Atomics: Optimization outside atomic, Optimizer restrictions",
    "sourceNote": "Adapted Scoped atomic execution graph and memory ordering from LangRef: Memory Model for Concurrent Operations, Atomic Memory Ordering Constraints, syncscope, volatile memory accesses; Atomics: Optimization outside atomic, Optimizer restrictions. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/AtomicMemoryModel-happens-before",
    "type": "Operation",
    "name": "happens-before",
    "signature": "hb : Event×Event→Prop",
    "description": "Take transitive closure of program-order and synchronizes-with edges in the selected thread/signal convention.",
    "concept": "urn:csabs:concept/AtomicMemoryModel",
    "precondition": "The underlying edge generation is semantically justified.",
    "postcondition": "Take transitive closure of program-order and synchronizes-with edges in the selected thread/signal convention.",
    "totality": "Total relation.",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-atomics"
    ],
    "sourceLocator": "LangRef: Memory Model for Concurrent Operations, Atomic Memory Ordering Constraints, syncscope, volatile memory accesses; Atomics: Optimization outside atomic, Optimizer restrictions",
    "sourceNote": "Adapted Scoped atomic execution graph and memory ordering from LangRef: Memory Model for Concurrent Operations, Atomic Memory Ordering Constraints, syncscope, volatile memory accesses; Atomics: Optimization outside atomic, Optimizer restrictions. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/AtomicMemoryModel-hb-closure",
    "type": "Axiom",
    "name": "hb-closure",
    "description": "Defining obligation for Scoped atomic execution graph and memory ordering",
    "statement": "hb is the transitive closure of the relevant single-thread program order and synchronizes-with edges.",
    "formalStatement": "hb is the transitive closure of the relevant single-thread program order and synchronizes-with edges.",
    "assumptions": [
      "LLVM 21.1.8 atomics and thread-creation environment. Modification order is per location; monotonic does not imply one total order across all locations. Acquire/release synchronization requires the actual reads-from/release-sequence and scope conditions, not only matching labels. Fences, cmpxchg success/failure orderings and RMW atomicity require instruction clauses. seq_cst has additional constraints and does not impose sequential consistency on all non-seq_cst events. Volatile is distinct from atomic. Permitted executions include races/UB according to LLVM, not an assumed data-race-free SC model. Cross-thread refinement compares sets of allowed executions/observations."
    ],
    "appliesTo": [
      "urn:csabs:concept/AtomicMemoryModel"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-atomics"
    ],
    "sourceLocator": "LangRef: Memory Model for Concurrent Operations, Atomic Memory Ordering Constraints, syncscope, volatile memory accesses; Atomics: Optimization outside atomic, Optimizer restrictions",
    "sourceNote": "Adapted Scoped atomic execution graph and memory ordering from LangRef: Memory Model for Concurrent Operations, Atomic Memory Ordering Constraints, syncscope, volatile memory accesses; Atomics: Optimization outside atomic, Optimizer restrictions. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:axiom/AtomicMemoryModel-ordering-scope",
    "type": "Axiom",
    "name": "ordering-scope",
    "description": "Defining obligation for Scoped atomic execution graph and memory ordering",
    "statement": "Atomic correctness retains per-location modification order, actual synchronization and scopes; monotonic alone supplies no cross-location global order.",
    "formalStatement": "Atomic correctness retains per-location modification order, actual synchronization and scopes; monotonic alone supplies no cross-location global order.",
    "assumptions": [
      "LLVM 21.1.8 atomics and thread-creation environment. Modification order is per location; monotonic does not imply one total order across all locations. Acquire/release synchronization requires the actual reads-from/release-sequence and scope conditions, not only matching labels. Fences, cmpxchg success/failure orderings and RMW atomicity require instruction clauses. seq_cst has additional constraints and does not impose sequential consistency on all non-seq_cst events. Volatile is distinct from atomic. Permitted executions include races/UB according to LLVM, not an assumed data-race-free SC model. Cross-thread refinement compares sets of allowed executions/observations."
    ],
    "appliesTo": [
      "urn:csabs:concept/AtomicMemoryModel"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-atomics"
    ],
    "sourceLocator": "LangRef: Memory Model for Concurrent Operations, Atomic Memory Ordering Constraints, syncscope, volatile memory accesses; Atomics: Optimization outside atomic, Optimizer restrictions",
    "sourceNote": "Adapted Scoped atomic execution graph and memory ordering from LangRef: Memory Model for Concurrent Operations, Atomic Memory Ordering Constraints, syncscope, volatile memory accesses; Atomics: Optimization outside atomic, Optimizer restrictions. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:law/AtomicMemoryModel-synchronization-implies-hb",
    "type": "Law",
    "name": "synchronization-implies-hb",
    "description": "Derived consequence in the stated profile.",
    "statement": "sw(a,b) ⇒ hb(a,b) for events in the selected model.",
    "formalStatement": "sw(a,b) ⇒ hb(a,b) for events in the selected model.",
    "assumptions": [
      "LLVM 21.1.8 atomics and thread-creation environment. Modification order is per location; monotonic does not imply one total order across all locations. Acquire/release synchronization requires the actual reads-from/release-sequence and scope conditions, not only matching labels. Fences, cmpxchg success/failure orderings and RMW atomicity require instruction clauses. seq_cst has additional constraints and does not impose sequential consistency on all non-seq_cst events. Volatile is distinct from atomic. Permitted executions include races/UB according to LLVM, not an assumed data-race-free SC model. Cross-thread refinement compares sets of allowed executions/observations."
    ],
    "appliesTo": [
      "urn:csabs:concept/AtomicMemoryModel"
    ],
    "dependsOn": [
      "urn:csabs:axiom/AtomicMemoryModel-hb-closure"
    ],
    "proofSketch": "A synchronizes-with edge belongs to the generating relation, hence to its transitive closure.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-atomics"
    ],
    "sourceLocator": "LangRef: Memory Model for Concurrent Operations, Atomic Memory Ordering Constraints, syncscope, volatile memory accesses; Atomics: Optimization outside atomic, Optimizer restrictions",
    "sourceNote": "Catalog derivation from the explicit dependsOn premises; the cited source motivates the interface, not this exact editorial theorem name.",
    "provenanceKind": "derived",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  }
]
```
<!-- graph-record:end -->
