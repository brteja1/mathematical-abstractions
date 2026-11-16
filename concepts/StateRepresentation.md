# Observable state representation relation

A relation between different state carriers that retains relevant observations and identifies the invariant needed to replace storage, aggregate fields, stack frames or runtime values.

**Notation:** Rep(s,t) ⇒ ObsS(s)=ObsT(t); operation diagrams preserve Rep

**Stable ID:** `urn:csabs:concept/StateRepresentation`

**Categories:** Programming-language semantics → Compiler transformations

**Kind:** Relation

**Prerequisites:** [Binary relation](Relation.md), [Observable behavior refinement](BehaviorRefinement.md)

**Specializes:** [Binary relation](Relation.md)

**Related concepts:** [Byte-addressed memory with typed access obligations](ByteMemory.md), [Typed static single assignment with scoped uses](SSAForm.md), [Typed IR legalization with representation relation](DialectConversion.md), [Simulation](Simulation.md)

## Backlinks

- [Typed IR legalization with representation relation](DialectConversion.md) — `relatedConcept`
- [Instrumented trace projection and runtime contract](RuntimeInstrumentation.md) — `requiresConcept`
- [Environment-indexed symbol resolution and reachability](SymbolLinkage.md) — `relatedConcept`

## Mathematical formulation

A relation between different state carriers that retains relevant observations and identifies the invariant needed to replace storage, aggregate fields, stack frames or runtime values. Rep(s,t) ⇒ ObsS(s)=ObsT(t); operation diagrams preserve Rep Rep relates source and target representations rather than asserting concrete state equality. For memory-to-SSA, include path-dependent PHIs, uninitialized/poison choices and escape/lifetime conditions. For aggregate splitting, retain field byte offsets, padding observations, aliasing and pointer external state. For GC/coroutine lowering, frame/root/relocation and suspend/resume protocols are part of the invariant. Initial related states, operation preservation, outcomes and progress are separate obligations; an observation relation alone does not prove a transform.

**Lean formulation** (in its source module context):

```lean
structure StateRepresentation (S T Observation : Type u) where
  related : S → T → Prop
  sourceObserve : S → Observation
  targetObserve : T → Observation
  observationAgreement : ∀ s t, related s t → sourceObserve s = targetObserve t
```

**Source:** [`Catalog.LLVM.StateRepresentation`](../lean/Catalog/LLVMTransforms.lean); consulted 2026-11-16.

**Scope:** partial

**Interpretation:** Cross-carrier relation and source/target observation functions with observationAgreement.

**Limits:** No representation invariant implementation, memory promotion/SROA algorithm, operation simulation, GC relocation or coroutine frame proof. Observation agreement alone supplies no full refinement theorem.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Rep(s,t) ⇒ ObsS(s)=ObsT(t).; To establish a replacement, initial states and corresponding operations/outcomes must preserve Rep, with progress when stuttering is used.

**basisKind:** relational-structural-definition

**basisScope:** Rep relates source and target representations rather than asserting concrete state equality. For memory-to-SSA, include path-dependent PHIs, uninitialized/poison choices and escape/lifetime conditions. For aggregate splitting, retain field byte offsets, padding observations, aliasing and pointer external state. For GC/coroutine lowering, frame/root/relocation and suspend/resume protocols are part of the invariant. Initial related states, operation preservation, outcomes and progress are separate obligations; an observation relation alone does not prove a transform.

**specializationNote:** Instantiate the parent carrier and operation as follows: Cross-carrier relation and source/target observation functions with observationAgreement.

**verificationObligation:** Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.; No representation invariant implementation, memory promotion/SROA algorithm, operation simulation, GC relocation or coroutine frame proof. Observation agreement alone supplies no full refinement theorem.

**reviewStatus:** Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-StateRepresentation-represents"></a>

### represents

`urn:csabs:operation/StateRepresentation-represents`

**signature:** represents : SourceState×TargetState→Prop

**description:** Relate admissible storage/register/frame representations.

**precondition:** Invariant and observation map explicitly chosen.

**postcondition:** Relate admissible storage/register/frame representations.

**totality:** Total predicate.

**source:** [LLVM Pass Reference (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Passes.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Passes.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM GC Statepoints (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Statepoints.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Statepoints.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM Coroutines (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Coroutines.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Coroutines.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** Passes: mem2reg, reg2mem, sroa, argpromotion; LangRef: layout, load/store; Statepoints: relocation motivation; Coroutines: split frame representation

**sourceNote:** Adapted Observable state representation relation from Passes: mem2reg, reg2mem, sroa, argpromotion; LangRef: layout, load/store; Statepoints: relocation motivation; Coroutines: split frame representation. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-StateRepresentation-observe"></a>

### observe

`urn:csabs:operation/StateRepresentation-observe`

**signature:** observe : State→Observation

**description:** Project only observations admitted by the contract.

**precondition:** Include relevant memory identity, control and runtime effects.

**postcondition:** Project only observations admitted by the contract.

**totality:** Total function in the selected model.

**source:** [LLVM Pass Reference (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Passes.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Passes.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM GC Statepoints (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Statepoints.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Statepoints.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM Coroutines (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Coroutines.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Coroutines.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** Passes: mem2reg, reg2mem, sroa, argpromotion; LangRef: layout, load/store; Statepoints: relocation motivation; Coroutines: split frame representation

**sourceNote:** Adapted Observable state representation relation from Passes: mem2reg, reg2mem, sroa, argpromotion; LangRef: layout, load/store; Statepoints: relocation motivation; Coroutines: split frame representation. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-StateRepresentation-observation-agreement"></a>

### observation-agreement

`urn:csabs:axiom/StateRepresentation-observation-agreement`

**description:** Defining obligation for Observable state representation relation

**statement:** Rep(s,t) ⇒ ObsS(s)=ObsT(t).

**formalStatement:** Rep(s,t) ⇒ ObsS(s)=ObsT(t).

**assumptions:** Rep relates source and target representations rather than asserting concrete state equality. For memory-to-SSA, include path-dependent PHIs, uninitialized/poison choices and escape/lifetime conditions. For aggregate splitting, retain field byte offsets, padding observations, aliasing and pointer external state. For GC/coroutine lowering, frame/root/relocation and suspend/resume protocols are part of the invariant. Initial related states, operation preservation, outcomes and progress are separate obligations; an observation relation alone does not prove a transform.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Pass Reference (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Passes.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Passes.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM GC Statepoints (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Statepoints.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Statepoints.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM Coroutines (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Coroutines.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Coroutines.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** Passes: mem2reg, reg2mem, sroa, argpromotion; LangRef: layout, load/store; Statepoints: relocation motivation; Coroutines: split frame representation

**sourceNote:** Adapted Observable state representation relation from Passes: mem2reg, reg2mem, sroa, argpromotion; LangRef: layout, load/store; Statepoints: relocation motivation; Coroutines: split frame representation. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

<a id="node-urn-csabs-axiom-StateRepresentation-simulation-obligation"></a>

### simulation-obligation

`urn:csabs:axiom/StateRepresentation-simulation-obligation`

**description:** Defining obligation for Observable state representation relation

**statement:** To establish a replacement, initial states and corresponding operations/outcomes must preserve Rep, with progress when stuttering is used.

**formalStatement:** To establish a replacement, initial states and corresponding operations/outcomes must preserve Rep, with progress when stuttering is used.

**assumptions:** Rep relates source and target representations rather than asserting concrete state equality. For memory-to-SSA, include path-dependent PHIs, uninitialized/poison choices and escape/lifetime conditions. For aggregate splitting, retain field byte offsets, padding observations, aliasing and pointer external state. For GC/coroutine lowering, frame/root/relocation and suspend/resume protocols are part of the invariant. Initial related states, operation preservation, outcomes and progress are separate obligations; an observation relation alone does not prove a transform.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Pass Reference (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Passes.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Passes.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM GC Statepoints (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Statepoints.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Statepoints.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM Coroutines (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Coroutines.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Coroutines.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** Passes: mem2reg, reg2mem, sroa, argpromotion; LangRef: layout, load/store; Statepoints: relocation motivation; Coroutines: split frame representation

**sourceNote:** Adapted Observable state representation relation from Passes: mem2reg, reg2mem, sroa, argpromotion; LangRef: layout, load/store; Statepoints: relocation motivation; Coroutines: split frame representation. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

## Laws

<a id="node-urn-csabs-law-StateRepresentation-related-observable-consistency"></a>

### related-observable-consistency

`urn:csabs:law/StateRepresentation-related-observable-consistency`

**description:** Derived consequence in the stated profile.

**statement:** Rep(s,t₁) ∧ Rep(s,t₂) ⇒ ObsT(t₁)=ObsT(t₂).

**formalStatement:** Rep(s,t₁) ∧ Rep(s,t₂) ⇒ ObsT(t₁)=ObsT(t₂).

**assumptions:** Rep relates source and target representations rather than asserting concrete state equality. For memory-to-SSA, include path-dependent PHIs, uninitialized/poison choices and escape/lifetime conditions. For aggregate splitting, retain field byte offsets, padding observations, aliasing and pointer external state. For GC/coroutine lowering, frame/root/relocation and suspend/resume protocols are part of the invariant. Initial related states, operation preservation, outcomes and progress are separate obligations; an observation relation alone does not prove a transform.

**dependsOn:** [observation-agreement](StateRepresentation.md#node-urn-csabs-axiom-StateRepresentation-observation-agreement)

**proofSketch:** Both target observations equal ObsS(s), so equality follows by symmetry and transitivity. Concrete target states may still differ.

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Pass Reference (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Passes.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Passes.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM GC Statepoints (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Statepoints.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Statepoints.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM Coroutines (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Coroutines.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Coroutines.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** Passes: mem2reg, reg2mem, sroa, argpromotion; LangRef: layout, load/store; Statepoints: relocation motivation; Coroutines: split frame representation

**sourceNote:** Catalog derivation from the explicit dependsOn premises; the cited source motivates the interface, not this exact editorial theorem name.

**provenanceKind:** derived

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [LLVM Pass Reference (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Passes.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Passes.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface
- [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification
- [LLVM GC Statepoints (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Statepoints.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Statepoints.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface
- [LLVM Coroutines (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Coroutines.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Coroutines.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** Passes: mem2reg, reg2mem, sroa, argpromotion; LangRef: layout, load/store; Statepoints: relocation motivation; Coroutines: split frame representation

**sourceNote:** Adapted Observable state representation relation from Passes: mem2reg, reg2mem, sroa, argpromotion; LangRef: layout, load/store; Statepoints: relocation motivation; Coroutines: split frame representation. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/StateRepresentation",
    "type": "Concept",
    "shortForm": "StateRepresentation",
    "fullName": "Observable state representation relation",
    "definition": "A relation between different state carriers that retains relevant observations and identifies the invariant needed to replace storage, aggregate fields, stack frames or runtime values.",
    "notation": "Rep(s,t) ⇒ ObsS(s)=ObsT(t); operation diagrams preserve Rep",
    "category": [
      "urn:csabs:category/compiler-transformations"
    ],
    "kind": "urn:csabs:kind/relation",
    "requiresConcept": [
      "urn:csabs:concept/Relation",
      "urn:csabs:concept/BehaviorRefinement"
    ],
    "relatedConcept": [
      "urn:csabs:concept/ByteMemory",
      "urn:csabs:concept/SSAForm",
      "urn:csabs:concept/DialectConversion",
      "urn:csabs:concept/Simulation"
    ],
    "hasOperation": [
      "urn:csabs:operation/StateRepresentation-represents",
      "urn:csabs:operation/StateRepresentation-observe"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/StateRepresentation-observation-agreement",
      "urn:csabs:axiom/StateRepresentation-simulation-obligation"
    ],
    "hasLaw": [
      "urn:csabs:law/StateRepresentation-related-observable-consistency"
    ],
    "hasTheorem": [],
    "basisKind": "relational-structural-definition",
    "basisScope": "Rep relates source and target representations rather than asserting concrete state equality. For memory-to-SSA, include path-dependent PHIs, uninitialized/poison choices and escape/lifetime conditions. For aggregate splitting, retain field byte offsets, padding observations, aliasing and pointer external state. For GC/coroutine lowering, frame/root/relocation and suspend/resume protocols are part of the invariant. Initial related states, operation preservation, outcomes and progress are separate obligations; an observation relation alone does not prove a transform.",
    "axiomBasis": "Rep(s,t) ⇒ ObsS(s)=ObsT(t).; To establish a replacement, initial states and corresponding operations/outcomes must preserve Rep, with progress when stuttering is used.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.",
    "verificationObligation": [
      "Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.",
      "No representation invariant implementation, memory promotion/SROA algorithm, operation simulation, GC relocation or coroutine frame proof. Observation agreement alone supplies no full refinement theorem."
    ],
    "source": [
      "urn:csabs:source/compiler-pass-reference",
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-statepoints",
      "urn:csabs:source/compiler-coroutines"
    ],
    "sourceLocator": "Passes: mem2reg, reg2mem, sroa, argpromotion; LangRef: layout, load/store; Statepoints: relocation motivation; Coroutines: split frame representation",
    "sourceNote": "Adapted Observable state representation relation from Passes: mem2reg, reg2mem, sroa, argpromotion; LangRef: layout, load/store; Statepoints: relocation motivation; Coroutines: split frame representation. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/Relation"
    ],
    "specializationNote": "Instantiate the parent carrier and operation as follows: Cross-carrier relation and source/target observation functions with observationAgreement.",
    "mathematicalFormulation": "A relation between different state carriers that retains relevant observations and identifies the invariant needed to replace storage, aggregate fields, stack frames or runtime values. Rep(s,t) ⇒ ObsS(s)=ObsT(t); operation diagrams preserve Rep Rep relates source and target representations rather than asserting concrete state equality. For memory-to-SSA, include path-dependent PHIs, uninitialized/poison choices and escape/lifetime conditions. For aggregate splitting, retain field byte offsets, padding observations, aliasing and pointer external state. For GC/coroutine lowering, frame/root/relocation and suspend/resume protocols are part of the invariant. Initial related states, operation preservation, outcomes and progress are separate obligations; an observation relation alone does not prove a transform.",
    "leanFormulation": "structure StateRepresentation (S T Observation : Type u) where\n  related : S → T → Prop\n  sourceObserve : S → Observation\n  targetObserve : T → Observation\n  observationAgreement : ∀ s t, related s t → sourceObserve s = targetObserve t",
    "formulationSource": "urn:csabs:source/compiler-llvm-lean",
    "formulationLocator": "Catalog.LLVM.StateRepresentation",
    "formulationScope": "partial",
    "leanModelMapping": "Cross-carrier relation and source/target observation functions with observationAgreement.",
    "leanModelLimitations": "No representation invariant implementation, memory promotion/SROA algorithm, operation simulation, GC relocation or coroutine frame proof. Observation agreement alone supplies no full refinement theorem."
  },
  {
    "id": "urn:csabs:operation/StateRepresentation-represents",
    "type": "Operation",
    "name": "represents",
    "signature": "represents : SourceState×TargetState→Prop",
    "description": "Relate admissible storage/register/frame representations.",
    "concept": "urn:csabs:concept/StateRepresentation",
    "precondition": "Invariant and observation map explicitly chosen.",
    "postcondition": "Relate admissible storage/register/frame representations.",
    "totality": "Total predicate.",
    "source": [
      "urn:csabs:source/compiler-pass-reference",
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-statepoints",
      "urn:csabs:source/compiler-coroutines"
    ],
    "sourceLocator": "Passes: mem2reg, reg2mem, sroa, argpromotion; LangRef: layout, load/store; Statepoints: relocation motivation; Coroutines: split frame representation",
    "sourceNote": "Adapted Observable state representation relation from Passes: mem2reg, reg2mem, sroa, argpromotion; LangRef: layout, load/store; Statepoints: relocation motivation; Coroutines: split frame representation. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/StateRepresentation-observe",
    "type": "Operation",
    "name": "observe",
    "signature": "observe : State→Observation",
    "description": "Project only observations admitted by the contract.",
    "concept": "urn:csabs:concept/StateRepresentation",
    "precondition": "Include relevant memory identity, control and runtime effects.",
    "postcondition": "Project only observations admitted by the contract.",
    "totality": "Total function in the selected model.",
    "source": [
      "urn:csabs:source/compiler-pass-reference",
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-statepoints",
      "urn:csabs:source/compiler-coroutines"
    ],
    "sourceLocator": "Passes: mem2reg, reg2mem, sroa, argpromotion; LangRef: layout, load/store; Statepoints: relocation motivation; Coroutines: split frame representation",
    "sourceNote": "Adapted Observable state representation relation from Passes: mem2reg, reg2mem, sroa, argpromotion; LangRef: layout, load/store; Statepoints: relocation motivation; Coroutines: split frame representation. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/StateRepresentation-observation-agreement",
    "type": "Axiom",
    "name": "observation-agreement",
    "description": "Defining obligation for Observable state representation relation",
    "statement": "Rep(s,t) ⇒ ObsS(s)=ObsT(t).",
    "formalStatement": "Rep(s,t) ⇒ ObsS(s)=ObsT(t).",
    "assumptions": [
      "Rep relates source and target representations rather than asserting concrete state equality. For memory-to-SSA, include path-dependent PHIs, uninitialized/poison choices and escape/lifetime conditions. For aggregate splitting, retain field byte offsets, padding observations, aliasing and pointer external state. For GC/coroutine lowering, frame/root/relocation and suspend/resume protocols are part of the invariant. Initial related states, operation preservation, outcomes and progress are separate obligations; an observation relation alone does not prove a transform."
    ],
    "appliesTo": [
      "urn:csabs:concept/StateRepresentation"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-pass-reference",
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-statepoints",
      "urn:csabs:source/compiler-coroutines"
    ],
    "sourceLocator": "Passes: mem2reg, reg2mem, sroa, argpromotion; LangRef: layout, load/store; Statepoints: relocation motivation; Coroutines: split frame representation",
    "sourceNote": "Adapted Observable state representation relation from Passes: mem2reg, reg2mem, sroa, argpromotion; LangRef: layout, load/store; Statepoints: relocation motivation; Coroutines: split frame representation. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:axiom/StateRepresentation-simulation-obligation",
    "type": "Axiom",
    "name": "simulation-obligation",
    "description": "Defining obligation for Observable state representation relation",
    "statement": "To establish a replacement, initial states and corresponding operations/outcomes must preserve Rep, with progress when stuttering is used.",
    "formalStatement": "To establish a replacement, initial states and corresponding operations/outcomes must preserve Rep, with progress when stuttering is used.",
    "assumptions": [
      "Rep relates source and target representations rather than asserting concrete state equality. For memory-to-SSA, include path-dependent PHIs, uninitialized/poison choices and escape/lifetime conditions. For aggregate splitting, retain field byte offsets, padding observations, aliasing and pointer external state. For GC/coroutine lowering, frame/root/relocation and suspend/resume protocols are part of the invariant. Initial related states, operation preservation, outcomes and progress are separate obligations; an observation relation alone does not prove a transform."
    ],
    "appliesTo": [
      "urn:csabs:concept/StateRepresentation"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-pass-reference",
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-statepoints",
      "urn:csabs:source/compiler-coroutines"
    ],
    "sourceLocator": "Passes: mem2reg, reg2mem, sroa, argpromotion; LangRef: layout, load/store; Statepoints: relocation motivation; Coroutines: split frame representation",
    "sourceNote": "Adapted Observable state representation relation from Passes: mem2reg, reg2mem, sroa, argpromotion; LangRef: layout, load/store; Statepoints: relocation motivation; Coroutines: split frame representation. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:law/StateRepresentation-related-observable-consistency",
    "type": "Law",
    "name": "related-observable-consistency",
    "description": "Derived consequence in the stated profile.",
    "statement": "Rep(s,t₁) ∧ Rep(s,t₂) ⇒ ObsT(t₁)=ObsT(t₂).",
    "formalStatement": "Rep(s,t₁) ∧ Rep(s,t₂) ⇒ ObsT(t₁)=ObsT(t₂).",
    "assumptions": [
      "Rep relates source and target representations rather than asserting concrete state equality. For memory-to-SSA, include path-dependent PHIs, uninitialized/poison choices and escape/lifetime conditions. For aggregate splitting, retain field byte offsets, padding observations, aliasing and pointer external state. For GC/coroutine lowering, frame/root/relocation and suspend/resume protocols are part of the invariant. Initial related states, operation preservation, outcomes and progress are separate obligations; an observation relation alone does not prove a transform."
    ],
    "appliesTo": [
      "urn:csabs:concept/StateRepresentation"
    ],
    "dependsOn": [
      "urn:csabs:axiom/StateRepresentation-observation-agreement"
    ],
    "proofSketch": "Both target observations equal ObsS(s), so equality follows by symmetry and transitivity. Concrete target states may still differ.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-pass-reference",
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-statepoints",
      "urn:csabs:source/compiler-coroutines"
    ],
    "sourceLocator": "Passes: mem2reg, reg2mem, sroa, argpromotion; LangRef: layout, load/store; Statepoints: relocation motivation; Coroutines: split frame representation",
    "sourceNote": "Catalog derivation from the explicit dependsOn premises; the cited source motivates the interface, not this exact editorial theorem name.",
    "provenanceKind": "derived",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  }
]
```
<!-- graph-record:end -->
