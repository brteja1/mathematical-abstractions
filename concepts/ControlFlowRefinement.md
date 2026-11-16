# CFG refinement with path correspondence and progress

A proof interface for CFG rewrites allowing finite source paths to match target steps while separately preserving initial/final observations, edge-carried values and infinite-execution behavior.

**Notation:** R(s,t) ∧ SafeS(s) ∧ t→t′ ⇒ ∃s′,s→*s′∧R(s′,t′); plus trace, initial/final and target-progress obligations

**Stable ID:** `urn:csabs:concept/ControlFlowRefinement`

**Categories:** Programming-language semantics → Compiler transformations

**Kind:** semantic-model

**Prerequisites:** [Observable behavior refinement](BehaviorRefinement.md), [Simulation](Simulation.md), [Typed static single assignment with scoped uses](SSAForm.md)

**Related concepts:** [Reachability-qualified control-flow dominance](Dominance.md), [Normal, exceptional and nonlocal control outcomes](ExceptionalControlFlow.md), [Control-sensitive communicating thread instances](ConvergentExecution.md)

## Backlinks

- [Control-sensitive communicating thread instances](ConvergentExecution.md) — `requiresConcept`
- [Normal, exceptional and nonlocal control outcomes](ExceptionalControlFlow.md) — `requiresConcept`
- [Guarded contextual program rewrite](GuardedRewrite.md) — `relatedConcept`
- [Guarded loop event-domain correspondence](LoopIterationMapping.md) — `requiresConcept`

## Mathematical formulation

A proof interface for CFG rewrites allowing finite source paths to match target steps while separately preserving initial/final observations, edge-carried values and infinite-execution behavior. R(s,t) ∧ SafeS(s) ∧ t→t′ ⇒ ∃s′,s→\*s′∧R(s′,t′); plus trace, initial/final and target-progress obligations Source/target operational CFG semantics include predecessor-edge PHI selection, conditions with undef/poison, exceptional exits and observable actions. Zero matched source steps are allowed only with a separate well-founded progress argument preventing unaccounted infinite target stuttering. Initial/final states, outputs and traces need matching; weak step matching alone is insufficient. Branch feasibility must come from sound facts. Unreachable instructions mean immediate UB when executed, not arbitrary permission to delete reachable predecessor effects. Blockaddress, indirectbr/callbr and convergence need explicit treatment. Apply this proof method on source-safe related states; require target progress (final or enabled) to exclude new stuck executions. Source UB is treated separately by the behavior-refinement convention.

**Lean formulation** (in its source module context):

```lean
structure ControlFlowRefinement (S T : Type u) where
  sourceStep : S → S → Prop
  targetStep : T → T → Prop
  sourceSafe : S → Prop
  related : S → T → Prop
  matchTargetStep : ∀ s t t', related s t → sourceSafe s → targetStep t t' →
    ∃ s', Relation.ReflTransGen sourceStep s s' ∧ related s' t'
```

**Source:** [`Catalog.LLVM.ControlFlowRefinement`](../lean/Catalog/LLVMTransforms.lean); consulted 2026-11-16.

**Scope:** partial

**Interpretation:** Related source/target states and target-step matching on source-safe states by reflexive-transitive source steps.

**Limits:** Lean contains only the safe-source step diagram; no initial/final/trace correspondence, target-progress or well-founded stuttering rank is encoded, so it proves no full CFG refinement theorem.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** R(s,t) ∧ SafeS(s) ∧ t→t′ ⇒ ∃s′, s→*s′ ∧ R(s′,t′), with corresponding observable traces.; For related source-safe states, the target is final or can step. Initial/final observations and traces match. Every zero-source-step target match is silent and decreases a well-founded stuttering rank for this proof method.

**basisKind:** relational-structural-definition

**basisScope:** Source/target operational CFG semantics include predecessor-edge PHI selection, conditions with undef/poison, exceptional exits and observable actions. Zero matched source steps are allowed only with a separate well-founded progress argument preventing unaccounted infinite target stuttering. Initial/final states, outputs and traces need matching; weak step matching alone is insufficient. Branch feasibility must come from sound facts. Unreachable instructions mean immediate UB when executed, not arbitrary permission to delete reachable predecessor effects. Blockaddress, indirectbr/callbr and convergence need explicit treatment. Apply this proof method on source-safe related states; require target progress (final or enabled) to exclude new stuck executions. Source UB is treated separately by the behavior-refinement convention.

**verificationObligation:** Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.; Lean contains only the safe-source step diagram; no initial/final/trace correspondence, target-progress or well-founded stuttering rank is encoded, so it proves no full CFG refinement theorem.

**reviewStatus:** Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-ControlFlowRefinement-relate"></a>

### relate

`urn:csabs:operation/ControlFlowRefinement-relate`

**signature:** relate : SourceState×TargetState→Prop

**description:** Relate states across different CFG shapes and edge-carried values.

**precondition:** State/observation mapping specified.

**postcondition:** Relate states across different CFG shapes and edge-carried values.

**totality:** Total predicate.

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM Pass Reference (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Passes.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Passes.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM Loop Terminology (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LoopTerminology.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LoopTerminology.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [CompCert Smallstep: backward simulation and well-founded stuttering](https://compcert.org/doc/html/compcert.common.Smallstep.html); accessedOn: 2026-11-16; sourceRole: consulted-primary-formal-semantics

**sourceLocator:** LangRef: br, switch, phi, unreachable; Passes: simplifycfg, jump-threading, break-crit-edges, lower-switch; LoopTerminology: irreducible control flow; CompCert Smallstep: bsim_properties, bsim_simulation and alternate backward simulation diagram

**sourceNote:** Adapts safe-source backward step matching, initial/final state matching, target progress and well-founded silent stuttering from CompCert; LLVM-specific PHI/control obligations come from the cited LLVM sections. The partial Lean interface encodes only safe-source step matching.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-ControlFlowRefinement-match-step"></a>

### match-step

`urn:csabs:operation/ControlFlowRefinement-match-step`

**signature:** matchStep : RelatedPair×TargetStep→P(SourcePath)

**description:** Find a finite corresponding source path preserving the relation.

**precondition:** Related source-safe states; output/trace matching, target progress and divergence rank checked separately.

**postcondition:** Find a finite corresponding source path preserving the relation.

**totality:** Proof relation; not an executable general decision procedure.

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM Pass Reference (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Passes.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Passes.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM Loop Terminology (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LoopTerminology.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LoopTerminology.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [CompCert Smallstep: backward simulation and well-founded stuttering](https://compcert.org/doc/html/compcert.common.Smallstep.html); accessedOn: 2026-11-16; sourceRole: consulted-primary-formal-semantics

**sourceLocator:** LangRef: br, switch, phi, unreachable; Passes: simplifycfg, jump-threading, break-crit-edges, lower-switch; LoopTerminology: irreducible control flow; CompCert Smallstep: bsim_properties, bsim_simulation and alternate backward simulation diagram

**sourceNote:** Adapts safe-source backward step matching, initial/final state matching, target progress and well-founded silent stuttering from CompCert; LLVM-specific PHI/control obligations come from the cited LLVM sections. The partial Lean interface encodes only safe-source step matching.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-ControlFlowRefinement-step-diagram"></a>

### step-diagram

`urn:csabs:axiom/ControlFlowRefinement-step-diagram`

**description:** Defining obligation for CFG refinement with path correspondence and progress

**statement:** R(s,t) ∧ SafeS(s) ∧ t→t′ ⇒ ∃s′, s→*s′ ∧ R(s′,t′), with corresponding observable traces.

**formalStatement:** R(s,t) ∧ SafeS(s) ∧ t→t′ ⇒ ∃s′, s→*s′ ∧ R(s′,t′), with corresponding observable traces.

**assumptions:** Source/target operational CFG semantics include predecessor-edge PHI selection, conditions with undef/poison, exceptional exits and observable actions. Zero matched source steps are allowed only with a separate well-founded progress argument preventing unaccounted infinite target stuttering. Initial/final states, outputs and traces need matching; weak step matching alone is insufficient. Branch feasibility must come from sound facts. Unreachable instructions mean immediate UB when executed, not arbitrary permission to delete reachable predecessor effects. Blockaddress, indirectbr/callbr and convergence need explicit treatment. Apply this proof method on source-safe related states; require target progress (final or enabled) to exclude new stuck executions. Source UB is treated separately by the behavior-refinement convention.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM Pass Reference (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Passes.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Passes.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM Loop Terminology (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LoopTerminology.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LoopTerminology.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [CompCert Smallstep: backward simulation and well-founded stuttering](https://compcert.org/doc/html/compcert.common.Smallstep.html); accessedOn: 2026-11-16; sourceRole: consulted-primary-formal-semantics

**sourceLocator:** LangRef: br, switch, phi, unreachable; Passes: simplifycfg, jump-threading, break-crit-edges, lower-switch; LoopTerminology: irreducible control flow; CompCert Smallstep: bsim_properties, bsim_simulation and alternate backward simulation diagram

**sourceNote:** Adapts safe-source backward step matching, initial/final state matching, target progress and well-founded silent stuttering from CompCert; LLVM-specific PHI/control obligations come from the cited LLVM sections. The partial Lean interface encodes only safe-source step matching.

**provenanceKind:** adapted

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

<a id="node-urn-csabs-axiom-ControlFlowRefinement-progress-obligation"></a>

### progress-obligation

`urn:csabs:axiom/ControlFlowRefinement-progress-obligation`

**description:** Defining obligation for CFG refinement with path correspondence and progress

**statement:** For related source-safe states, the target is final or can step. Initial/final observations and traces match. Every zero-source-step target match is silent and decreases a well-founded stuttering rank for this proof method.

**formalStatement:** For related source-safe states, the target is final or can step. Initial/final observations and traces match. Every zero-source-step target match is silent and decreases a well-founded stuttering rank for this proof method.

**assumptions:** Source/target operational CFG semantics include predecessor-edge PHI selection, conditions with undef/poison, exceptional exits and observable actions. Zero matched source steps are allowed only with a separate well-founded progress argument preventing unaccounted infinite target stuttering. Initial/final states, outputs and traces need matching; weak step matching alone is insufficient. Branch feasibility must come from sound facts. Unreachable instructions mean immediate UB when executed, not arbitrary permission to delete reachable predecessor effects. Blockaddress, indirectbr/callbr and convergence need explicit treatment. Apply this proof method on source-safe related states; require target progress (final or enabled) to exclude new stuck executions. Source UB is treated separately by the behavior-refinement convention.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM Pass Reference (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Passes.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Passes.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM Loop Terminology (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LoopTerminology.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LoopTerminology.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [CompCert Smallstep: backward simulation and well-founded stuttering](https://compcert.org/doc/html/compcert.common.Smallstep.html); accessedOn: 2026-11-16; sourceRole: consulted-primary-formal-semantics

**sourceLocator:** LangRef: br, switch, phi, unreachable; Passes: simplifycfg, jump-threading, break-crit-edges, lower-switch; LoopTerminology: irreducible control flow; CompCert Smallstep: bsim_properties, bsim_simulation and alternate backward simulation diagram

**sourceNote:** Adapts safe-source backward step matching, initial/final state matching, target progress and well-founded silent stuttering from CompCert; LLVM-specific PHI/control obligations come from the cited LLVM sections. The partial Lean interface encodes only safe-source step matching.

**provenanceKind:** adapted

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

## Laws

<a id="node-urn-csabs-law-ControlFlowRefinement-no-infinite-zero-step-match"></a>

### no-infinite-zero-step-match

`urn:csabs:law/ControlFlowRefinement-no-infinite-zero-step-match`

**description:** Derived consequence in the stated profile.

**statement:** For a target path matched to source-safe states under the well-founded rank obligation, the path cannot be infinite with only zero-source-step matches.

**formalStatement:** For a target path matched to source-safe states under the well-founded rank obligation, the path cannot be infinite with only zero-source-step matches.

**assumptions:** Source/target operational CFG semantics include predecessor-edge PHI selection, conditions with undef/poison, exceptional exits and observable actions. Zero matched source steps are allowed only with a separate well-founded progress argument preventing unaccounted infinite target stuttering. Initial/final states, outputs and traces need matching; weak step matching alone is insufficient. Branch feasibility must come from sound facts. Unreachable instructions mean immediate UB when executed, not arbitrary permission to delete reachable predecessor effects. Blockaddress, indirectbr/callbr and convergence need explicit treatment. Apply this proof method on source-safe related states; require target progress (final or enabled) to exclude new stuck executions. Source UB is treated separately by the behavior-refinement convention.

**dependsOn:** [progress-obligation](ControlFlowRefinement.md#node-urn-csabs-axiom-ControlFlowRefinement-progress-obligation)

**proofSketch:** Such a path would create an infinite strictly descending chain in a well-founded order.

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM Pass Reference (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Passes.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Passes.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM Loop Terminology (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LoopTerminology.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LoopTerminology.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [CompCert Smallstep: backward simulation and well-founded stuttering](https://compcert.org/doc/html/compcert.common.Smallstep.html); accessedOn: 2026-11-16; sourceRole: consulted-primary-formal-semantics

**sourceLocator:** LangRef: br, switch, phi, unreachable; Passes: simplifycfg, jump-threading, break-crit-edges, lower-switch; LoopTerminology: irreducible control flow; CompCert Smallstep: bsim_properties, bsim_simulation and alternate backward simulation diagram

**sourceNote:** Catalog derivation from the explicit dependsOn premises; the cited source motivates the interface, not this exact editorial theorem name.

**provenanceKind:** derived

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification
- [LLVM Pass Reference (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Passes.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Passes.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface
- [LLVM Loop Terminology (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LoopTerminology.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LoopTerminology.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface
- [CompCert Smallstep: backward simulation and well-founded stuttering](https://compcert.org/doc/html/compcert.common.Smallstep.html); accessedOn: 2026-11-16; sourceRole: consulted-primary-formal-semantics

**sourceLocator:** LangRef: br, switch, phi, unreachable; Passes: simplifycfg, jump-threading, break-crit-edges, lower-switch; LoopTerminology: irreducible control flow; CompCert Smallstep: bsim_properties, bsim_simulation and alternate backward simulation diagram

**sourceNote:** Adapts safe-source backward step matching, initial/final state matching, target progress and well-founded silent stuttering from CompCert; LLVM-specific PHI/control obligations come from the cited LLVM sections. The partial Lean interface encodes only safe-source step matching.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/ControlFlowRefinement",
    "type": "Concept",
    "shortForm": "ControlFlowRefinement",
    "fullName": "CFG refinement with path correspondence and progress",
    "definition": "A proof interface for CFG rewrites allowing finite source paths to match target steps while separately preserving initial/final observations, edge-carried values and infinite-execution behavior.",
    "notation": "R(s,t) ∧ SafeS(s) ∧ t→t′ ⇒ ∃s′,s→*s′∧R(s′,t′); plus trace, initial/final and target-progress obligations",
    "category": [
      "urn:csabs:category/compiler-transformations"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "requiresConcept": [
      "urn:csabs:concept/BehaviorRefinement",
      "urn:csabs:concept/Simulation",
      "urn:csabs:concept/SSAForm"
    ],
    "relatedConcept": [
      "urn:csabs:concept/Dominance",
      "urn:csabs:concept/ExceptionalControlFlow",
      "urn:csabs:concept/ConvergentExecution"
    ],
    "hasOperation": [
      "urn:csabs:operation/ControlFlowRefinement-relate",
      "urn:csabs:operation/ControlFlowRefinement-match-step"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/ControlFlowRefinement-step-diagram",
      "urn:csabs:axiom/ControlFlowRefinement-progress-obligation"
    ],
    "hasLaw": [
      "urn:csabs:law/ControlFlowRefinement-no-infinite-zero-step-match"
    ],
    "hasTheorem": [],
    "basisKind": "relational-structural-definition",
    "basisScope": "Source/target operational CFG semantics include predecessor-edge PHI selection, conditions with undef/poison, exceptional exits and observable actions. Zero matched source steps are allowed only with a separate well-founded progress argument preventing unaccounted infinite target stuttering. Initial/final states, outputs and traces need matching; weak step matching alone is insufficient. Branch feasibility must come from sound facts. Unreachable instructions mean immediate UB when executed, not arbitrary permission to delete reachable predecessor effects. Blockaddress, indirectbr/callbr and convergence need explicit treatment. Apply this proof method on source-safe related states; require target progress (final or enabled) to exclude new stuck executions. Source UB is treated separately by the behavior-refinement convention.",
    "axiomBasis": "R(s,t) ∧ SafeS(s) ∧ t→t′ ⇒ ∃s′, s→*s′ ∧ R(s′,t′), with corresponding observable traces.; For related source-safe states, the target is final or can step. Initial/final observations and traces match. Every zero-source-step target match is silent and decreases a well-founded stuttering rank for this proof method.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.",
    "verificationObligation": [
      "Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.",
      "Lean contains only the safe-source step diagram; no initial/final/trace correspondence, target-progress or well-founded stuttering rank is encoded, so it proves no full CFG refinement theorem."
    ],
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-pass-reference",
      "urn:csabs:source/compiler-loops",
      "urn:csabs:source/compiler-compcert-smallstep"
    ],
    "sourceLocator": "LangRef: br, switch, phi, unreachable; Passes: simplifycfg, jump-threading, break-crit-edges, lower-switch; LoopTerminology: irreducible control flow; CompCert Smallstep: bsim_properties, bsim_simulation and alternate backward simulation diagram",
    "sourceNote": "Adapts safe-source backward step matching, initial/final state matching, target progress and well-founded silent stuttering from CompCert; LLVM-specific PHI/control obligations come from the cited LLVM sections. The partial Lean interface encodes only safe-source step matching.",
    "provenanceKind": "adapted",
    "mathematicalFormulation": "A proof interface for CFG rewrites allowing finite source paths to match target steps while separately preserving initial/final observations, edge-carried values and infinite-execution behavior. R(s,t) ∧ SafeS(s) ∧ t→t′ ⇒ ∃s′,s→*s′∧R(s′,t′); plus trace, initial/final and target-progress obligations Source/target operational CFG semantics include predecessor-edge PHI selection, conditions with undef/poison, exceptional exits and observable actions. Zero matched source steps are allowed only with a separate well-founded progress argument preventing unaccounted infinite target stuttering. Initial/final states, outputs and traces need matching; weak step matching alone is insufficient. Branch feasibility must come from sound facts. Unreachable instructions mean immediate UB when executed, not arbitrary permission to delete reachable predecessor effects. Blockaddress, indirectbr/callbr and convergence need explicit treatment. Apply this proof method on source-safe related states; require target progress (final or enabled) to exclude new stuck executions. Source UB is treated separately by the behavior-refinement convention.",
    "leanFormulation": "structure ControlFlowRefinement (S T : Type u) where\n  sourceStep : S → S → Prop\n  targetStep : T → T → Prop\n  sourceSafe : S → Prop\n  related : S → T → Prop\n  matchTargetStep : ∀ s t t', related s t → sourceSafe s → targetStep t t' →\n    ∃ s', Relation.ReflTransGen sourceStep s s' ∧ related s' t'",
    "formulationSource": "urn:csabs:source/compiler-llvm-lean",
    "formulationLocator": "Catalog.LLVM.ControlFlowRefinement",
    "formulationScope": "partial",
    "leanModelMapping": "Related source/target states and target-step matching on source-safe states by reflexive-transitive source steps.",
    "leanModelLimitations": "Lean contains only the safe-source step diagram; no initial/final/trace correspondence, target-progress or well-founded stuttering rank is encoded, so it proves no full CFG refinement theorem."
  },
  {
    "id": "urn:csabs:operation/ControlFlowRefinement-relate",
    "type": "Operation",
    "name": "relate",
    "signature": "relate : SourceState×TargetState→Prop",
    "description": "Relate states across different CFG shapes and edge-carried values.",
    "concept": "urn:csabs:concept/ControlFlowRefinement",
    "precondition": "State/observation mapping specified.",
    "postcondition": "Relate states across different CFG shapes and edge-carried values.",
    "totality": "Total predicate.",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-pass-reference",
      "urn:csabs:source/compiler-loops",
      "urn:csabs:source/compiler-compcert-smallstep"
    ],
    "sourceLocator": "LangRef: br, switch, phi, unreachable; Passes: simplifycfg, jump-threading, break-crit-edges, lower-switch; LoopTerminology: irreducible control flow; CompCert Smallstep: bsim_properties, bsim_simulation and alternate backward simulation diagram",
    "sourceNote": "Adapts safe-source backward step matching, initial/final state matching, target progress and well-founded silent stuttering from CompCert; LLVM-specific PHI/control obligations come from the cited LLVM sections. The partial Lean interface encodes only safe-source step matching.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/ControlFlowRefinement-match-step",
    "type": "Operation",
    "name": "match-step",
    "signature": "matchStep : RelatedPair×TargetStep→P(SourcePath)",
    "description": "Find a finite corresponding source path preserving the relation.",
    "concept": "urn:csabs:concept/ControlFlowRefinement",
    "precondition": "Related source-safe states; output/trace matching, target progress and divergence rank checked separately.",
    "postcondition": "Find a finite corresponding source path preserving the relation.",
    "totality": "Proof relation; not an executable general decision procedure.",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-pass-reference",
      "urn:csabs:source/compiler-loops",
      "urn:csabs:source/compiler-compcert-smallstep"
    ],
    "sourceLocator": "LangRef: br, switch, phi, unreachable; Passes: simplifycfg, jump-threading, break-crit-edges, lower-switch; LoopTerminology: irreducible control flow; CompCert Smallstep: bsim_properties, bsim_simulation and alternate backward simulation diagram",
    "sourceNote": "Adapts safe-source backward step matching, initial/final state matching, target progress and well-founded silent stuttering from CompCert; LLVM-specific PHI/control obligations come from the cited LLVM sections. The partial Lean interface encodes only safe-source step matching.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/ControlFlowRefinement-step-diagram",
    "type": "Axiom",
    "name": "step-diagram",
    "description": "Defining obligation for CFG refinement with path correspondence and progress",
    "statement": "R(s,t) ∧ SafeS(s) ∧ t→t′ ⇒ ∃s′, s→*s′ ∧ R(s′,t′), with corresponding observable traces.",
    "formalStatement": "R(s,t) ∧ SafeS(s) ∧ t→t′ ⇒ ∃s′, s→*s′ ∧ R(s′,t′), with corresponding observable traces.",
    "assumptions": [
      "Source/target operational CFG semantics include predecessor-edge PHI selection, conditions with undef/poison, exceptional exits and observable actions. Zero matched source steps are allowed only with a separate well-founded progress argument preventing unaccounted infinite target stuttering. Initial/final states, outputs and traces need matching; weak step matching alone is insufficient. Branch feasibility must come from sound facts. Unreachable instructions mean immediate UB when executed, not arbitrary permission to delete reachable predecessor effects. Blockaddress, indirectbr/callbr and convergence need explicit treatment. Apply this proof method on source-safe related states; require target progress (final or enabled) to exclude new stuck executions. Source UB is treated separately by the behavior-refinement convention."
    ],
    "appliesTo": [
      "urn:csabs:concept/ControlFlowRefinement"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-pass-reference",
      "urn:csabs:source/compiler-loops",
      "urn:csabs:source/compiler-compcert-smallstep"
    ],
    "sourceLocator": "LangRef: br, switch, phi, unreachable; Passes: simplifycfg, jump-threading, break-crit-edges, lower-switch; LoopTerminology: irreducible control flow; CompCert Smallstep: bsim_properties, bsim_simulation and alternate backward simulation diagram",
    "sourceNote": "Adapts safe-source backward step matching, initial/final state matching, target progress and well-founded silent stuttering from CompCert; LLVM-specific PHI/control obligations come from the cited LLVM sections. The partial Lean interface encodes only safe-source step matching.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:axiom/ControlFlowRefinement-progress-obligation",
    "type": "Axiom",
    "name": "progress-obligation",
    "description": "Defining obligation for CFG refinement with path correspondence and progress",
    "statement": "For related source-safe states, the target is final or can step. Initial/final observations and traces match. Every zero-source-step target match is silent and decreases a well-founded stuttering rank for this proof method.",
    "formalStatement": "For related source-safe states, the target is final or can step. Initial/final observations and traces match. Every zero-source-step target match is silent and decreases a well-founded stuttering rank for this proof method.",
    "assumptions": [
      "Source/target operational CFG semantics include predecessor-edge PHI selection, conditions with undef/poison, exceptional exits and observable actions. Zero matched source steps are allowed only with a separate well-founded progress argument preventing unaccounted infinite target stuttering. Initial/final states, outputs and traces need matching; weak step matching alone is insufficient. Branch feasibility must come from sound facts. Unreachable instructions mean immediate UB when executed, not arbitrary permission to delete reachable predecessor effects. Blockaddress, indirectbr/callbr and convergence need explicit treatment. Apply this proof method on source-safe related states; require target progress (final or enabled) to exclude new stuck executions. Source UB is treated separately by the behavior-refinement convention."
    ],
    "appliesTo": [
      "urn:csabs:concept/ControlFlowRefinement"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-pass-reference",
      "urn:csabs:source/compiler-loops",
      "urn:csabs:source/compiler-compcert-smallstep"
    ],
    "sourceLocator": "LangRef: br, switch, phi, unreachable; Passes: simplifycfg, jump-threading, break-crit-edges, lower-switch; LoopTerminology: irreducible control flow; CompCert Smallstep: bsim_properties, bsim_simulation and alternate backward simulation diagram",
    "sourceNote": "Adapts safe-source backward step matching, initial/final state matching, target progress and well-founded silent stuttering from CompCert; LLVM-specific PHI/control obligations come from the cited LLVM sections. The partial Lean interface encodes only safe-source step matching.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:law/ControlFlowRefinement-no-infinite-zero-step-match",
    "type": "Law",
    "name": "no-infinite-zero-step-match",
    "description": "Derived consequence in the stated profile.",
    "statement": "For a target path matched to source-safe states under the well-founded rank obligation, the path cannot be infinite with only zero-source-step matches.",
    "formalStatement": "For a target path matched to source-safe states under the well-founded rank obligation, the path cannot be infinite with only zero-source-step matches.",
    "assumptions": [
      "Source/target operational CFG semantics include predecessor-edge PHI selection, conditions with undef/poison, exceptional exits and observable actions. Zero matched source steps are allowed only with a separate well-founded progress argument preventing unaccounted infinite target stuttering. Initial/final states, outputs and traces need matching; weak step matching alone is insufficient. Branch feasibility must come from sound facts. Unreachable instructions mean immediate UB when executed, not arbitrary permission to delete reachable predecessor effects. Blockaddress, indirectbr/callbr and convergence need explicit treatment. Apply this proof method on source-safe related states; require target progress (final or enabled) to exclude new stuck executions. Source UB is treated separately by the behavior-refinement convention."
    ],
    "appliesTo": [
      "urn:csabs:concept/ControlFlowRefinement"
    ],
    "dependsOn": [
      "urn:csabs:axiom/ControlFlowRefinement-progress-obligation"
    ],
    "proofSketch": "Such a path would create an infinite strictly descending chain in a well-founded order.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-pass-reference",
      "urn:csabs:source/compiler-loops",
      "urn:csabs:source/compiler-compcert-smallstep"
    ],
    "sourceLocator": "LangRef: br, switch, phi, unreachable; Passes: simplifycfg, jump-threading, break-crit-edges, lower-switch; LoopTerminology: irreducible control flow; CompCert Smallstep: bsim_properties, bsim_simulation and alternate backward simulation diagram",
    "sourceNote": "Catalog derivation from the explicit dependsOn premises; the cited source motivates the interface, not this exact editorial theorem name.",
    "provenanceKind": "derived",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  }
]
```
<!-- graph-record:end -->
