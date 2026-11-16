# Lane-indexed vector execution and inactive-lane policy

A vector interpretation with runtime lane count, mask and explicit vector length, retaining lane-specific values/poison, per-intrinsic inactive results and active-only memory effects.

**Notation:** Active(i)⇔0≤i<W ∧ i<EVL ∧ mask[i]; W=fixed or base·vscale

**Stable ID:** `urn:csabs:concept/PredicatedVectorSemantics`

**Categories:** Programming-language semantics → Compiler transformations

**Kind:** semantic-model

**Prerequisites:** [LLVM scalar deferred undefinedness and freeze](LLVMPoisonSemantics.md), [LLVM fixed-width integer operations and flags](LLVMIntegerSemantics.md), [LLVM floating-point environment and rewrite permissions](LLVMFloatingPointSemantics.md)

**Related concepts:** [Guarded loop event-domain correspondence](LoopIterationMapping.md), [Byte-addressed memory with typed access obligations](ByteMemory.md)

## Backlinks

- [Control-sensitive communicating thread instances](ConvergentExecution.md) — `relatedConcept`
- [LLVM floating-point environment and rewrite permissions](LLVMFloatingPointSemantics.md) — `relatedConcept`
- [LLVM scalar deferred undefinedness and freeze](LLVMPoisonSemantics.md) — `relatedConcept`
- [Memory dependence and legal loop rescheduling](LoopDependence.md) — `relatedConcept`
- [Guarded loop event-domain correspondence](LoopIterationMapping.md) — `relatedConcept`

## Mathematical formulation

A vector interpretation with runtime lane count, mask and explicit vector length, retaining lane-specific values/poison, per-intrinsic inactive results and active-only memory effects. Active(i)⇔0≤i<W ∧ i<EVL ∧ mask[i]; W=fixed or base·vscale LLVM 21.1.8 fixed/scalable vectors. Scalable vscale is a positive runtime factor, not the minimum width. For well-defined masks and EVL, active lanes have index<EVL and true mask. EVL>runtime width is UB for the documented VP family. Inactive result policy is opcode-specific: undef, poison or passthrough must follow that intrinsic; do not impose one universal policy. Shuffle poison masks produce poison lanes, not fresh ordinary values. Active-only memory intrinsics must not access masked-off invalid addresses. Ordinary select does not suppress evaluation of previously computed operands. Horizontal reductions and cross-lane operations need separate order/poison reasoning.

**Lean formulation** (in its source module context):

```lean
structure PredicatedVectorSemantics (Value : Type u) (width : Nat) where
  evl : Nat
  evlBound : evl ≤ width
  mask : Fin width → Bool
  inactiveResult : Fin width → Set Value
```

**Source:** [`Catalog.LLVM.PredicatedVectorSemantics`](../lean/Catalog/LLVMTransforms.lean); consulted 2026-11-16.

**Scope:** partial

**Interpretation:** Runtime width parameter, bounded EVL, Boolean mask and explicit inactive-result sets; activeLane gives the bounded mask condition.

**Limits:** No scalable vector runtime, poison-mask semantics, lane evaluator, shuffle/reduction implementation or memory-access proof. Boolean masks represent only the well-defined-mask subprofile.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** For a well-defined mask, Active(i)↔i<W ∧ i<EVL ∧ mask[i]=true.; Inactive result and memory-access behavior must follow the selected intrinsic; undef, poison and passthrough are distinct. EVL>W is UB for the documented VP family.

**basisKind:** relational-structural-definition

**basisScope:** LLVM 21.1.8 fixed/scalable vectors. Scalable vscale is a positive runtime factor, not the minimum width. For well-defined masks and EVL, active lanes have index<EVL and true mask. EVL>runtime width is UB for the documented VP family. Inactive result policy is opcode-specific: undef, poison or passthrough must follow that intrinsic; do not impose one universal policy. Shuffle poison masks produce poison lanes, not fresh ordinary values. Active-only memory intrinsics must not access masked-off invalid addresses. Ordinary select does not suppress evaluation of previously computed operands. Horizontal reductions and cross-lane operations need separate order/poison reasoning.

**verificationObligation:** Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.; No scalable vector runtime, poison-mask semantics, lane evaluator, shuffle/reduction implementation or memory-access proof. Boolean masks represent only the well-defined-mask subprofile.

**reviewStatus:** Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-PredicatedVectorSemantics-active"></a>

### active

`urn:csabs:operation/PredicatedVectorSemantics-active`

**signature:** active : RuntimeWidth×EVL×Mask×Lane→Prop

**description:** Select lanes below EVL whose well-defined mask is true.

**precondition:** EVL≤runtime width; legal vector types.

**postcondition:** Select lanes below EVL whose well-defined mask is true.

**totality:** Total predicate on valid parameters.

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM Auto-Vectorization (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Vectorizers.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Vectorizers.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** LangRef: Vector Type, extractelement/insertelement/shufflevector, Vector Predication Intrinsics and vp.select; Vectorizers: loop and SLP vectorizers, tails/runtime checks

**sourceNote:** Adapted Lane-indexed vector execution and inactive-lane policy from LangRef: Vector Type, extractelement/insertelement/shufflevector, Vector Predication Intrinsics and vp.select; Vectorizers: loop and SLP vectorizers, tails/runtime checks. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-PredicatedVectorSemantics-lane-result"></a>

### lane-result

`urn:csabs:operation/PredicatedVectorSemantics-lane-result`

**signature:** laneResult : Intrinsic×Lane×Args→P(Value)

**description:** Use active semantics or the exact opcode-specific inactive policy.

**precondition:** Mask/EVL definedness and per-lane poison rules mapped.

**postcondition:** Use active semantics or the exact opcode-specific inactive policy.

**totality:** Nondeterministic outcome relation.

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM Auto-Vectorization (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Vectorizers.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Vectorizers.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** LangRef: Vector Type, extractelement/insertelement/shufflevector, Vector Predication Intrinsics and vp.select; Vectorizers: loop and SLP vectorizers, tails/runtime checks

**sourceNote:** Adapted Lane-indexed vector execution and inactive-lane policy from LangRef: Vector Type, extractelement/insertelement/shufflevector, Vector Predication Intrinsics and vp.select; Vectorizers: loop and SLP vectorizers, tails/runtime checks. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-PredicatedVectorSemantics-memory-lanes"></a>

### memory-lanes

`urn:csabs:operation/PredicatedVectorSemantics-memory-lanes`

**signature:** memoryLanes : Intrinsic×Mask×EVL→P(Lane)

**description:** Select actual accesses for a masked/VP memory intrinsic.

**precondition:** Use intrinsic-specific active-access semantics.

**postcondition:** Select actual accesses for a masked/VP memory intrinsic.

**totality:** Total query for supported intrinsics.

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM Auto-Vectorization (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Vectorizers.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Vectorizers.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** LangRef: Vector Type, extractelement/insertelement/shufflevector, Vector Predication Intrinsics and vp.select; Vectorizers: loop and SLP vectorizers, tails/runtime checks

**sourceNote:** Adapted Lane-indexed vector execution and inactive-lane policy from LangRef: Vector Type, extractelement/insertelement/shufflevector, Vector Predication Intrinsics and vp.select; Vectorizers: loop and SLP vectorizers, tails/runtime checks. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-PredicatedVectorSemantics-active-definition"></a>

### active-definition

`urn:csabs:axiom/PredicatedVectorSemantics-active-definition`

**description:** Defining obligation for Lane-indexed vector execution and inactive-lane policy

**statement:** For a well-defined mask, Active(i)↔i<W ∧ i<EVL ∧ mask[i]=true.

**formalStatement:** For a well-defined mask, Active(i)↔i<W ∧ i<EVL ∧ mask[i]=true.

**assumptions:** LLVM 21.1.8 fixed/scalable vectors. Scalable vscale is a positive runtime factor, not the minimum width. For well-defined masks and EVL, active lanes have index<EVL and true mask. EVL>runtime width is UB for the documented VP family. Inactive result policy is opcode-specific: undef, poison or passthrough must follow that intrinsic; do not impose one universal policy. Shuffle poison masks produce poison lanes, not fresh ordinary values. Active-only memory intrinsics must not access masked-off invalid addresses. Ordinary select does not suppress evaluation of previously computed operands. Horizontal reductions and cross-lane operations need separate order/poison reasoning.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM Auto-Vectorization (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Vectorizers.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Vectorizers.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** LangRef: Vector Type, extractelement/insertelement/shufflevector, Vector Predication Intrinsics and vp.select; Vectorizers: loop and SLP vectorizers, tails/runtime checks

**sourceNote:** Adapted Lane-indexed vector execution and inactive-lane policy from LangRef: Vector Type, extractelement/insertelement/shufflevector, Vector Predication Intrinsics and vp.select; Vectorizers: loop and SLP vectorizers, tails/runtime checks. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

<a id="node-urn-csabs-axiom-PredicatedVectorSemantics-inactive-policy"></a>

### inactive-policy

`urn:csabs:axiom/PredicatedVectorSemantics-inactive-policy`

**description:** Defining obligation for Lane-indexed vector execution and inactive-lane policy

**statement:** Inactive result and memory-access behavior must follow the selected intrinsic; undef, poison and passthrough are distinct. EVL>W is UB for the documented VP family.

**formalStatement:** Inactive result and memory-access behavior must follow the selected intrinsic; undef, poison and passthrough are distinct. EVL>W is UB for the documented VP family.

**assumptions:** LLVM 21.1.8 fixed/scalable vectors. Scalable vscale is a positive runtime factor, not the minimum width. For well-defined masks and EVL, active lanes have index<EVL and true mask. EVL>runtime width is UB for the documented VP family. Inactive result policy is opcode-specific: undef, poison or passthrough must follow that intrinsic; do not impose one universal policy. Shuffle poison masks produce poison lanes, not fresh ordinary values. Active-only memory intrinsics must not access masked-off invalid addresses. Ordinary select does not suppress evaluation of previously computed operands. Horizontal reductions and cross-lane operations need separate order/poison reasoning.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM Auto-Vectorization (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Vectorizers.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Vectorizers.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** LangRef: Vector Type, extractelement/insertelement/shufflevector, Vector Predication Intrinsics and vp.select; Vectorizers: loop and SLP vectorizers, tails/runtime checks

**sourceNote:** Adapted Lane-indexed vector execution and inactive-lane policy from LangRef: Vector Type, extractelement/insertelement/shufflevector, Vector Predication Intrinsics and vp.select; Vectorizers: loop and SLP vectorizers, tails/runtime checks. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

## Laws

<a id="node-urn-csabs-law-PredicatedVectorSemantics-zero-evl"></a>

### zero-evl

`urn:csabs:law/PredicatedVectorSemantics-zero-evl`

**description:** Derived consequence in the stated profile.

**statement:** For well-defined masks and EVL=0, no lane is active.

**formalStatement:** For well-defined masks and EVL=0, no lane is active.

**assumptions:** LLVM 21.1.8 fixed/scalable vectors. Scalable vscale is a positive runtime factor, not the minimum width. For well-defined masks and EVL, active lanes have index<EVL and true mask. EVL>runtime width is UB for the documented VP family. Inactive result policy is opcode-specific: undef, poison or passthrough must follow that intrinsic; do not impose one universal policy. Shuffle poison masks produce poison lanes, not fresh ordinary values. Active-only memory intrinsics must not access masked-off invalid addresses. Ordinary select does not suppress evaluation of previously computed operands. Horizontal reductions and cross-lane operations need separate order/poison reasoning.

**dependsOn:** [active-definition](PredicatedVectorSemantics.md#node-urn-csabs-axiom-PredicatedVectorSemantics-active-definition)

**proofSketch:** No natural lane index is strictly below zero. This does not assign results to inactive lanes or legalize unsupported intrinsics.

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM Auto-Vectorization (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Vectorizers.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Vectorizers.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** LangRef: Vector Type, extractelement/insertelement/shufflevector, Vector Predication Intrinsics and vp.select; Vectorizers: loop and SLP vectorizers, tails/runtime checks

**sourceNote:** Catalog derivation from the explicit dependsOn premises; the cited source motivates the interface, not this exact editorial theorem name.

**provenanceKind:** derived

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification
- [LLVM Auto-Vectorization (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Vectorizers.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Vectorizers.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** LangRef: Vector Type, extractelement/insertelement/shufflevector, Vector Predication Intrinsics and vp.select; Vectorizers: loop and SLP vectorizers, tails/runtime checks

**sourceNote:** Adapted Lane-indexed vector execution and inactive-lane policy from LangRef: Vector Type, extractelement/insertelement/shufflevector, Vector Predication Intrinsics and vp.select; Vectorizers: loop and SLP vectorizers, tails/runtime checks. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/PredicatedVectorSemantics",
    "type": "Concept",
    "shortForm": "PredicatedVectorSemantics",
    "fullName": "Lane-indexed vector execution and inactive-lane policy",
    "definition": "A vector interpretation with runtime lane count, mask and explicit vector length, retaining lane-specific values/poison, per-intrinsic inactive results and active-only memory effects.",
    "notation": "Active(i)⇔0≤i<W ∧ i<EVL ∧ mask[i]; W=fixed or base·vscale",
    "category": [
      "urn:csabs:category/compiler-transformations"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "requiresConcept": [
      "urn:csabs:concept/LLVMPoisonSemantics",
      "urn:csabs:concept/LLVMIntegerSemantics",
      "urn:csabs:concept/LLVMFloatingPointSemantics"
    ],
    "relatedConcept": [
      "urn:csabs:concept/LoopIterationMapping",
      "urn:csabs:concept/ByteMemory"
    ],
    "hasOperation": [
      "urn:csabs:operation/PredicatedVectorSemantics-active",
      "urn:csabs:operation/PredicatedVectorSemantics-lane-result",
      "urn:csabs:operation/PredicatedVectorSemantics-memory-lanes"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/PredicatedVectorSemantics-active-definition",
      "urn:csabs:axiom/PredicatedVectorSemantics-inactive-policy"
    ],
    "hasLaw": [
      "urn:csabs:law/PredicatedVectorSemantics-zero-evl"
    ],
    "hasTheorem": [],
    "basisKind": "relational-structural-definition",
    "basisScope": "LLVM 21.1.8 fixed/scalable vectors. Scalable vscale is a positive runtime factor, not the minimum width. For well-defined masks and EVL, active lanes have index<EVL and true mask. EVL>runtime width is UB for the documented VP family. Inactive result policy is opcode-specific: undef, poison or passthrough must follow that intrinsic; do not impose one universal policy. Shuffle poison masks produce poison lanes, not fresh ordinary values. Active-only memory intrinsics must not access masked-off invalid addresses. Ordinary select does not suppress evaluation of previously computed operands. Horizontal reductions and cross-lane operations need separate order/poison reasoning.",
    "axiomBasis": "For a well-defined mask, Active(i)↔i<W ∧ i<EVL ∧ mask[i]=true.; Inactive result and memory-access behavior must follow the selected intrinsic; undef, poison and passthrough are distinct. EVL>W is UB for the documented VP family.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.",
    "verificationObligation": [
      "Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.",
      "No scalable vector runtime, poison-mask semantics, lane evaluator, shuffle/reduction implementation or memory-access proof. Boolean masks represent only the well-defined-mask subprofile."
    ],
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-vectors"
    ],
    "sourceLocator": "LangRef: Vector Type, extractelement/insertelement/shufflevector, Vector Predication Intrinsics and vp.select; Vectorizers: loop and SLP vectorizers, tails/runtime checks",
    "sourceNote": "Adapted Lane-indexed vector execution and inactive-lane policy from LangRef: Vector Type, extractelement/insertelement/shufflevector, Vector Predication Intrinsics and vp.select; Vectorizers: loop and SLP vectorizers, tails/runtime checks. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "mathematicalFormulation": "A vector interpretation with runtime lane count, mask and explicit vector length, retaining lane-specific values/poison, per-intrinsic inactive results and active-only memory effects. Active(i)⇔0≤i<W ∧ i<EVL ∧ mask[i]; W=fixed or base·vscale LLVM 21.1.8 fixed/scalable vectors. Scalable vscale is a positive runtime factor, not the minimum width. For well-defined masks and EVL, active lanes have index<EVL and true mask. EVL>runtime width is UB for the documented VP family. Inactive result policy is opcode-specific: undef, poison or passthrough must follow that intrinsic; do not impose one universal policy. Shuffle poison masks produce poison lanes, not fresh ordinary values. Active-only memory intrinsics must not access masked-off invalid addresses. Ordinary select does not suppress evaluation of previously computed operands. Horizontal reductions and cross-lane operations need separate order/poison reasoning.",
    "leanFormulation": "structure PredicatedVectorSemantics (Value : Type u) (width : Nat) where\n  evl : Nat\n  evlBound : evl ≤ width\n  mask : Fin width → Bool\n  inactiveResult : Fin width → Set Value",
    "formulationSource": "urn:csabs:source/compiler-llvm-lean",
    "formulationLocator": "Catalog.LLVM.PredicatedVectorSemantics",
    "formulationScope": "partial",
    "leanModelMapping": "Runtime width parameter, bounded EVL, Boolean mask and explicit inactive-result sets; activeLane gives the bounded mask condition.",
    "leanModelLimitations": "No scalable vector runtime, poison-mask semantics, lane evaluator, shuffle/reduction implementation or memory-access proof. Boolean masks represent only the well-defined-mask subprofile."
  },
  {
    "id": "urn:csabs:operation/PredicatedVectorSemantics-active",
    "type": "Operation",
    "name": "active",
    "signature": "active : RuntimeWidth×EVL×Mask×Lane→Prop",
    "description": "Select lanes below EVL whose well-defined mask is true.",
    "concept": "urn:csabs:concept/PredicatedVectorSemantics",
    "precondition": "EVL≤runtime width; legal vector types.",
    "postcondition": "Select lanes below EVL whose well-defined mask is true.",
    "totality": "Total predicate on valid parameters.",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-vectors"
    ],
    "sourceLocator": "LangRef: Vector Type, extractelement/insertelement/shufflevector, Vector Predication Intrinsics and vp.select; Vectorizers: loop and SLP vectorizers, tails/runtime checks",
    "sourceNote": "Adapted Lane-indexed vector execution and inactive-lane policy from LangRef: Vector Type, extractelement/insertelement/shufflevector, Vector Predication Intrinsics and vp.select; Vectorizers: loop and SLP vectorizers, tails/runtime checks. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/PredicatedVectorSemantics-lane-result",
    "type": "Operation",
    "name": "lane-result",
    "signature": "laneResult : Intrinsic×Lane×Args→P(Value)",
    "description": "Use active semantics or the exact opcode-specific inactive policy.",
    "concept": "urn:csabs:concept/PredicatedVectorSemantics",
    "precondition": "Mask/EVL definedness and per-lane poison rules mapped.",
    "postcondition": "Use active semantics or the exact opcode-specific inactive policy.",
    "totality": "Nondeterministic outcome relation.",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-vectors"
    ],
    "sourceLocator": "LangRef: Vector Type, extractelement/insertelement/shufflevector, Vector Predication Intrinsics and vp.select; Vectorizers: loop and SLP vectorizers, tails/runtime checks",
    "sourceNote": "Adapted Lane-indexed vector execution and inactive-lane policy from LangRef: Vector Type, extractelement/insertelement/shufflevector, Vector Predication Intrinsics and vp.select; Vectorizers: loop and SLP vectorizers, tails/runtime checks. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/PredicatedVectorSemantics-memory-lanes",
    "type": "Operation",
    "name": "memory-lanes",
    "signature": "memoryLanes : Intrinsic×Mask×EVL→P(Lane)",
    "description": "Select actual accesses for a masked/VP memory intrinsic.",
    "concept": "urn:csabs:concept/PredicatedVectorSemantics",
    "precondition": "Use intrinsic-specific active-access semantics.",
    "postcondition": "Select actual accesses for a masked/VP memory intrinsic.",
    "totality": "Total query for supported intrinsics.",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-vectors"
    ],
    "sourceLocator": "LangRef: Vector Type, extractelement/insertelement/shufflevector, Vector Predication Intrinsics and vp.select; Vectorizers: loop and SLP vectorizers, tails/runtime checks",
    "sourceNote": "Adapted Lane-indexed vector execution and inactive-lane policy from LangRef: Vector Type, extractelement/insertelement/shufflevector, Vector Predication Intrinsics and vp.select; Vectorizers: loop and SLP vectorizers, tails/runtime checks. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/PredicatedVectorSemantics-active-definition",
    "type": "Axiom",
    "name": "active-definition",
    "description": "Defining obligation for Lane-indexed vector execution and inactive-lane policy",
    "statement": "For a well-defined mask, Active(i)↔i<W ∧ i<EVL ∧ mask[i]=true.",
    "formalStatement": "For a well-defined mask, Active(i)↔i<W ∧ i<EVL ∧ mask[i]=true.",
    "assumptions": [
      "LLVM 21.1.8 fixed/scalable vectors. Scalable vscale is a positive runtime factor, not the minimum width. For well-defined masks and EVL, active lanes have index<EVL and true mask. EVL>runtime width is UB for the documented VP family. Inactive result policy is opcode-specific: undef, poison or passthrough must follow that intrinsic; do not impose one universal policy. Shuffle poison masks produce poison lanes, not fresh ordinary values. Active-only memory intrinsics must not access masked-off invalid addresses. Ordinary select does not suppress evaluation of previously computed operands. Horizontal reductions and cross-lane operations need separate order/poison reasoning."
    ],
    "appliesTo": [
      "urn:csabs:concept/PredicatedVectorSemantics"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-vectors"
    ],
    "sourceLocator": "LangRef: Vector Type, extractelement/insertelement/shufflevector, Vector Predication Intrinsics and vp.select; Vectorizers: loop and SLP vectorizers, tails/runtime checks",
    "sourceNote": "Adapted Lane-indexed vector execution and inactive-lane policy from LangRef: Vector Type, extractelement/insertelement/shufflevector, Vector Predication Intrinsics and vp.select; Vectorizers: loop and SLP vectorizers, tails/runtime checks. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:axiom/PredicatedVectorSemantics-inactive-policy",
    "type": "Axiom",
    "name": "inactive-policy",
    "description": "Defining obligation for Lane-indexed vector execution and inactive-lane policy",
    "statement": "Inactive result and memory-access behavior must follow the selected intrinsic; undef, poison and passthrough are distinct. EVL>W is UB for the documented VP family.",
    "formalStatement": "Inactive result and memory-access behavior must follow the selected intrinsic; undef, poison and passthrough are distinct. EVL>W is UB for the documented VP family.",
    "assumptions": [
      "LLVM 21.1.8 fixed/scalable vectors. Scalable vscale is a positive runtime factor, not the minimum width. For well-defined masks and EVL, active lanes have index<EVL and true mask. EVL>runtime width is UB for the documented VP family. Inactive result policy is opcode-specific: undef, poison or passthrough must follow that intrinsic; do not impose one universal policy. Shuffle poison masks produce poison lanes, not fresh ordinary values. Active-only memory intrinsics must not access masked-off invalid addresses. Ordinary select does not suppress evaluation of previously computed operands. Horizontal reductions and cross-lane operations need separate order/poison reasoning."
    ],
    "appliesTo": [
      "urn:csabs:concept/PredicatedVectorSemantics"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-vectors"
    ],
    "sourceLocator": "LangRef: Vector Type, extractelement/insertelement/shufflevector, Vector Predication Intrinsics and vp.select; Vectorizers: loop and SLP vectorizers, tails/runtime checks",
    "sourceNote": "Adapted Lane-indexed vector execution and inactive-lane policy from LangRef: Vector Type, extractelement/insertelement/shufflevector, Vector Predication Intrinsics and vp.select; Vectorizers: loop and SLP vectorizers, tails/runtime checks. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:law/PredicatedVectorSemantics-zero-evl",
    "type": "Law",
    "name": "zero-evl",
    "description": "Derived consequence in the stated profile.",
    "statement": "For well-defined masks and EVL=0, no lane is active.",
    "formalStatement": "For well-defined masks and EVL=0, no lane is active.",
    "assumptions": [
      "LLVM 21.1.8 fixed/scalable vectors. Scalable vscale is a positive runtime factor, not the minimum width. For well-defined masks and EVL, active lanes have index<EVL and true mask. EVL>runtime width is UB for the documented VP family. Inactive result policy is opcode-specific: undef, poison or passthrough must follow that intrinsic; do not impose one universal policy. Shuffle poison masks produce poison lanes, not fresh ordinary values. Active-only memory intrinsics must not access masked-off invalid addresses. Ordinary select does not suppress evaluation of previously computed operands. Horizontal reductions and cross-lane operations need separate order/poison reasoning."
    ],
    "appliesTo": [
      "urn:csabs:concept/PredicatedVectorSemantics"
    ],
    "dependsOn": [
      "urn:csabs:axiom/PredicatedVectorSemantics-active-definition"
    ],
    "proofSketch": "No natural lane index is strictly below zero. This does not assign results to inactive lanes or legalize unsupported intrinsics.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-vectors"
    ],
    "sourceLocator": "LangRef: Vector Type, extractelement/insertelement/shufflevector, Vector Predication Intrinsics and vp.select; Vectorizers: loop and SLP vectorizers, tails/runtime checks",
    "sourceNote": "Catalog derivation from the explicit dependsOn premises; the cited source motivates the interface, not this exact editorial theorem name.",
    "provenanceKind": "derived",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  }
]
```
<!-- graph-record:end -->
