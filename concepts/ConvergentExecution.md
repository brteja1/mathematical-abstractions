# Control-sensitive communicating thread instances

A model of convergent operation instances whose permitted results depend on their communicating participants and control history, beyond ordinary memory-effect reasoning.

**Notation:** participants:Instance→P(Thread); allowedResult(instance,values) depends on the communicating group

**Stable ID:** `urn:csabs:concept/ConvergentExecution`

**Categories:** Programming-language semantics → Compiler transformations

**Kind:** semantic-model

**Prerequisites:** [Binary relation](Relation.md), [CFG refinement with path correspondence and progress](ControlFlowRefinement.md)

**Related concepts:** [Scoped atomic execution graph and memory ordering](AtomicMemoryModel.md), [Lane-indexed vector execution and inactive-lane policy](PredicatedVectorSemantics.md), [Call-boundary behavior and effect contract](CallEffectContract.md)

## Backlinks

- [Call-boundary behavior and effect contract](CallEffectContract.md) — `relatedConcept`
- [CFG refinement with path correspondence and progress](ControlFlowRefinement.md) — `relatedConcept`
- [Conservative resource effect summary](EffectSummary.md) — `relatedConcept`

## Mathematical formulation

A model of convergent operation instances whose permitted results depend on their communicating participants and control history, beyond ordinary memory-effect reasoning. participants:Instance→P(Thread); allowedResult(instance,values) depends on the communicating group LLVM 21.1.8 controlled and uncontrolled convergence require their documented rules. Thread groups/scopes and matching dynamic instances are explicit; a Boolean convergent flag alone is not a full communication model. Control-flow motion, duplication and loop transformations must preserve or legitimately refine the permitted communication instances and control tokens. Memory-effect freedom does not imply this. Convergence communication is outside the ordinary memory model; an atomic synchronization proof alone does not establish convergence preservation.

**Lean formulation** (in its source module context):

```lean
structure ConvergentExecution (Instance Thread Value : Type u) where
  participants : Instance → Set Thread
  allowedResult : Instance → (Thread → Value) → Prop
  sameCommunication : Instance → Instance → Prop
```

**Source:** [`Catalog.LLVM.ConvergentExecution`](../lean/Catalog/LLVMTransforms.lean); consulted 2026-11-16.

**Scope:** partial

**Interpretation:** Instance-indexed participant sets and allowedResult/sameCommunication predicates.

**Limits:** No dynamic instance/token semantics, thread-group construction, uniformity analysis or proof of LLVM convergence restrictions; raw client predicates are partial interfaces.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Allowed results of a convergent operation may depend on the participating thread group, not just a single thread operand tuple.; Motion/duplication that changes communicating instances or participants needs explicit convergence justification independent of memory effects.

**basisKind:** relational-structural-definition

**basisScope:** LLVM 21.1.8 controlled and uncontrolled convergence require their documented rules. Thread groups/scopes and matching dynamic instances are explicit; a Boolean convergent flag alone is not a full communication model. Control-flow motion, duplication and loop transformations must preserve or legitimately refine the permitted communication instances and control tokens. Memory-effect freedom does not imply this. Convergence communication is outside the ordinary memory model; an atomic synchronization proof alone does not establish convergence preservation.

**verificationObligation:** Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.; No dynamic instance/token semantics, thread-group construction, uniformity analysis or proof of LLVM convergence restrictions; raw client predicates are partial interfaces.

**reviewStatus:** Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-ConvergentExecution-participants"></a>

### participants

`urn:csabs:operation/ConvergentExecution-participants`

**signature:** participants : DynamicInstance→P(Thread)

**description:** Identify the threads participating together in the selected communicating instance.

**precondition:** Runtime execution scope and convergence-control semantics supplied.

**postcondition:** Identify the threads participating together in the selected communicating instance.

**totality:** Total query in a complete execution model.

**source:** [LLVM Convergent Operation Semantics (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/ConvergentOperations.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/ConvergentOperations.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** ConvergentOperations: Overview, Convergent Operations, texture sampling example; LangRef: convergent attribute, convergencectrl bundles

**sourceNote:** Adapted Control-sensitive communicating thread instances from ConvergentOperations: Overview, Convergent Operations, texture sampling example; LangRef: convergent attribute, convergencectrl bundles. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-ConvergentExecution-preserves-communication"></a>

### preserves-communication

`urn:csabs:operation/ConvergentExecution-preserves-communication`

**signature:** preservesCommunication : SourceExecution×TargetExecution→Prop

**description:** Require compatible instance/participant/control-token correspondence and result behavior.

**precondition:** Controlled/uncontrolled profile fixed.

**postcondition:** Require compatible instance/participant/control-token correspondence and result behavior.

**totality:** Semantic relation.

**source:** [LLVM Convergent Operation Semantics (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/ConvergentOperations.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/ConvergentOperations.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** ConvergentOperations: Overview, Convergent Operations, texture sampling example; LangRef: convergent attribute, convergencectrl bundles

**sourceNote:** Adapted Control-sensitive communicating thread instances from ConvergentOperations: Overview, Convergent Operations, texture sampling example; LangRef: convergent attribute, convergencectrl bundles. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-ConvergentExecution-group-dependence"></a>

### group-dependence

`urn:csabs:axiom/ConvergentExecution-group-dependence`

**description:** Defining obligation for Control-sensitive communicating thread instances

**statement:** Allowed results of a convergent operation may depend on the participating thread group, not just a single thread operand tuple.

**formalStatement:** Allowed results of a convergent operation may depend on the participating thread group, not just a single thread operand tuple.

**assumptions:** LLVM 21.1.8 controlled and uncontrolled convergence require their documented rules. Thread groups/scopes and matching dynamic instances are explicit; a Boolean convergent flag alone is not a full communication model. Control-flow motion, duplication and loop transformations must preserve or legitimately refine the permitted communication instances and control tokens. Memory-effect freedom does not imply this. Convergence communication is outside the ordinary memory model; an atomic synchronization proof alone does not establish convergence preservation.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Convergent Operation Semantics (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/ConvergentOperations.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/ConvergentOperations.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** ConvergentOperations: Overview, Convergent Operations, texture sampling example; LangRef: convergent attribute, convergencectrl bundles

**sourceNote:** Adapted Control-sensitive communicating thread instances from ConvergentOperations: Overview, Convergent Operations, texture sampling example; LangRef: convergent attribute, convergencectrl bundles. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

<a id="node-urn-csabs-axiom-ConvergentExecution-control-obligation"></a>

### control-obligation

`urn:csabs:axiom/ConvergentExecution-control-obligation`

**description:** Defining obligation for Control-sensitive communicating thread instances

**statement:** Motion/duplication that changes communicating instances or participants needs explicit convergence justification independent of memory effects.

**formalStatement:** Motion/duplication that changes communicating instances or participants needs explicit convergence justification independent of memory effects.

**assumptions:** LLVM 21.1.8 controlled and uncontrolled convergence require their documented rules. Thread groups/scopes and matching dynamic instances are explicit; a Boolean convergent flag alone is not a full communication model. Control-flow motion, duplication and loop transformations must preserve or legitimately refine the permitted communication instances and control tokens. Memory-effect freedom does not imply this. Convergence communication is outside the ordinary memory model; an atomic synchronization proof alone does not establish convergence preservation.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Convergent Operation Semantics (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/ConvergentOperations.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/ConvergentOperations.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** ConvergentOperations: Overview, Convergent Operations, texture sampling example; LangRef: convergent attribute, convergencectrl bundles

**sourceNote:** Adapted Control-sensitive communicating thread instances from ConvergentOperations: Overview, Convergent Operations, texture sampling example; LangRef: convergent attribute, convergencectrl bundles. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

## Laws

<a id="node-urn-csabs-law-ConvergentExecution-memory-purity-insufficient"></a>

### memory-purity-insufficient

`urn:csabs:law/ConvergentExecution-memory-purity-insufficient`

**description:** Derived consequence in the stated profile.

**statement:** An empty memory-effect summary alone does not justify sinking a convergent operation under a divergent condition.

**formalStatement:** An empty memory-effect summary alone does not justify sinking a convergent operation under a divergent condition.

**assumptions:** LLVM 21.1.8 controlled and uncontrolled convergence require their documented rules. Thread groups/scopes and matching dynamic instances are explicit; a Boolean convergent flag alone is not a full communication model. Control-flow motion, duplication and loop transformations must preserve or legitimately refine the permitted communication instances and control tokens. Memory-effect freedom does not imply this. Convergence communication is outside the ordinary memory model; an atomic synchronization proof alone does not establish convergence preservation.

**dependsOn:** [group-dependence](ConvergentExecution.md#node-urn-csabs-axiom-ConvergentExecution-group-dependence); [control-obligation](ConvergentExecution.md#node-urn-csabs-axiom-ConvergentExecution-control-obligation)

**proofSketch:** The condition can remove participants needed for communication while leaving each thread memory effects empty, as in the cited texture-sampling example.

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Convergent Operation Semantics (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/ConvergentOperations.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/ConvergentOperations.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** ConvergentOperations: Overview, Convergent Operations, texture sampling example; LangRef: convergent attribute, convergencectrl bundles

**sourceNote:** Catalog derivation from the explicit dependsOn premises; the cited source motivates the interface, not this exact editorial theorem name.

**provenanceKind:** derived

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [LLVM Convergent Operation Semantics (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/ConvergentOperations.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/ConvergentOperations.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface
- [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** ConvergentOperations: Overview, Convergent Operations, texture sampling example; LangRef: convergent attribute, convergencectrl bundles

**sourceNote:** Adapted Control-sensitive communicating thread instances from ConvergentOperations: Overview, Convergent Operations, texture sampling example; LangRef: convergent attribute, convergencectrl bundles. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/ConvergentExecution",
    "type": "Concept",
    "shortForm": "ConvergentExecution",
    "fullName": "Control-sensitive communicating thread instances",
    "definition": "A model of convergent operation instances whose permitted results depend on their communicating participants and control history, beyond ordinary memory-effect reasoning.",
    "notation": "participants:Instance→P(Thread); allowedResult(instance,values) depends on the communicating group",
    "category": [
      "urn:csabs:category/compiler-transformations"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "requiresConcept": [
      "urn:csabs:concept/Relation",
      "urn:csabs:concept/ControlFlowRefinement"
    ],
    "relatedConcept": [
      "urn:csabs:concept/AtomicMemoryModel",
      "urn:csabs:concept/PredicatedVectorSemantics",
      "urn:csabs:concept/CallEffectContract"
    ],
    "hasOperation": [
      "urn:csabs:operation/ConvergentExecution-participants",
      "urn:csabs:operation/ConvergentExecution-preserves-communication"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/ConvergentExecution-group-dependence",
      "urn:csabs:axiom/ConvergentExecution-control-obligation"
    ],
    "hasLaw": [
      "urn:csabs:law/ConvergentExecution-memory-purity-insufficient"
    ],
    "hasTheorem": [],
    "basisKind": "relational-structural-definition",
    "basisScope": "LLVM 21.1.8 controlled and uncontrolled convergence require their documented rules. Thread groups/scopes and matching dynamic instances are explicit; a Boolean convergent flag alone is not a full communication model. Control-flow motion, duplication and loop transformations must preserve or legitimately refine the permitted communication instances and control tokens. Memory-effect freedom does not imply this. Convergence communication is outside the ordinary memory model; an atomic synchronization proof alone does not establish convergence preservation.",
    "axiomBasis": "Allowed results of a convergent operation may depend on the participating thread group, not just a single thread operand tuple.; Motion/duplication that changes communicating instances or participants needs explicit convergence justification independent of memory effects.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.",
    "verificationObligation": [
      "Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.",
      "No dynamic instance/token semantics, thread-group construction, uniformity analysis or proof of LLVM convergence restrictions; raw client predicates are partial interfaces."
    ],
    "source": [
      "urn:csabs:source/compiler-convergence",
      "urn:csabs:source/compiler-llvm"
    ],
    "sourceLocator": "ConvergentOperations: Overview, Convergent Operations, texture sampling example; LangRef: convergent attribute, convergencectrl bundles",
    "sourceNote": "Adapted Control-sensitive communicating thread instances from ConvergentOperations: Overview, Convergent Operations, texture sampling example; LangRef: convergent attribute, convergencectrl bundles. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "mathematicalFormulation": "A model of convergent operation instances whose permitted results depend on their communicating participants and control history, beyond ordinary memory-effect reasoning. participants:Instance→P(Thread); allowedResult(instance,values) depends on the communicating group LLVM 21.1.8 controlled and uncontrolled convergence require their documented rules. Thread groups/scopes and matching dynamic instances are explicit; a Boolean convergent flag alone is not a full communication model. Control-flow motion, duplication and loop transformations must preserve or legitimately refine the permitted communication instances and control tokens. Memory-effect freedom does not imply this. Convergence communication is outside the ordinary memory model; an atomic synchronization proof alone does not establish convergence preservation.",
    "leanFormulation": "structure ConvergentExecution (Instance Thread Value : Type u) where\n  participants : Instance → Set Thread\n  allowedResult : Instance → (Thread → Value) → Prop\n  sameCommunication : Instance → Instance → Prop",
    "formulationSource": "urn:csabs:source/compiler-llvm-lean",
    "formulationLocator": "Catalog.LLVM.ConvergentExecution",
    "formulationScope": "partial",
    "leanModelMapping": "Instance-indexed participant sets and allowedResult/sameCommunication predicates.",
    "leanModelLimitations": "No dynamic instance/token semantics, thread-group construction, uniformity analysis or proof of LLVM convergence restrictions; raw client predicates are partial interfaces."
  },
  {
    "id": "urn:csabs:operation/ConvergentExecution-participants",
    "type": "Operation",
    "name": "participants",
    "signature": "participants : DynamicInstance→P(Thread)",
    "description": "Identify the threads participating together in the selected communicating instance.",
    "concept": "urn:csabs:concept/ConvergentExecution",
    "precondition": "Runtime execution scope and convergence-control semantics supplied.",
    "postcondition": "Identify the threads participating together in the selected communicating instance.",
    "totality": "Total query in a complete execution model.",
    "source": [
      "urn:csabs:source/compiler-convergence",
      "urn:csabs:source/compiler-llvm"
    ],
    "sourceLocator": "ConvergentOperations: Overview, Convergent Operations, texture sampling example; LangRef: convergent attribute, convergencectrl bundles",
    "sourceNote": "Adapted Control-sensitive communicating thread instances from ConvergentOperations: Overview, Convergent Operations, texture sampling example; LangRef: convergent attribute, convergencectrl bundles. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/ConvergentExecution-preserves-communication",
    "type": "Operation",
    "name": "preserves-communication",
    "signature": "preservesCommunication : SourceExecution×TargetExecution→Prop",
    "description": "Require compatible instance/participant/control-token correspondence and result behavior.",
    "concept": "urn:csabs:concept/ConvergentExecution",
    "precondition": "Controlled/uncontrolled profile fixed.",
    "postcondition": "Require compatible instance/participant/control-token correspondence and result behavior.",
    "totality": "Semantic relation.",
    "source": [
      "urn:csabs:source/compiler-convergence",
      "urn:csabs:source/compiler-llvm"
    ],
    "sourceLocator": "ConvergentOperations: Overview, Convergent Operations, texture sampling example; LangRef: convergent attribute, convergencectrl bundles",
    "sourceNote": "Adapted Control-sensitive communicating thread instances from ConvergentOperations: Overview, Convergent Operations, texture sampling example; LangRef: convergent attribute, convergencectrl bundles. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/ConvergentExecution-group-dependence",
    "type": "Axiom",
    "name": "group-dependence",
    "description": "Defining obligation for Control-sensitive communicating thread instances",
    "statement": "Allowed results of a convergent operation may depend on the participating thread group, not just a single thread operand tuple.",
    "formalStatement": "Allowed results of a convergent operation may depend on the participating thread group, not just a single thread operand tuple.",
    "assumptions": [
      "LLVM 21.1.8 controlled and uncontrolled convergence require their documented rules. Thread groups/scopes and matching dynamic instances are explicit; a Boolean convergent flag alone is not a full communication model. Control-flow motion, duplication and loop transformations must preserve or legitimately refine the permitted communication instances and control tokens. Memory-effect freedom does not imply this. Convergence communication is outside the ordinary memory model; an atomic synchronization proof alone does not establish convergence preservation."
    ],
    "appliesTo": [
      "urn:csabs:concept/ConvergentExecution"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-convergence",
      "urn:csabs:source/compiler-llvm"
    ],
    "sourceLocator": "ConvergentOperations: Overview, Convergent Operations, texture sampling example; LangRef: convergent attribute, convergencectrl bundles",
    "sourceNote": "Adapted Control-sensitive communicating thread instances from ConvergentOperations: Overview, Convergent Operations, texture sampling example; LangRef: convergent attribute, convergencectrl bundles. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:axiom/ConvergentExecution-control-obligation",
    "type": "Axiom",
    "name": "control-obligation",
    "description": "Defining obligation for Control-sensitive communicating thread instances",
    "statement": "Motion/duplication that changes communicating instances or participants needs explicit convergence justification independent of memory effects.",
    "formalStatement": "Motion/duplication that changes communicating instances or participants needs explicit convergence justification independent of memory effects.",
    "assumptions": [
      "LLVM 21.1.8 controlled and uncontrolled convergence require their documented rules. Thread groups/scopes and matching dynamic instances are explicit; a Boolean convergent flag alone is not a full communication model. Control-flow motion, duplication and loop transformations must preserve or legitimately refine the permitted communication instances and control tokens. Memory-effect freedom does not imply this. Convergence communication is outside the ordinary memory model; an atomic synchronization proof alone does not establish convergence preservation."
    ],
    "appliesTo": [
      "urn:csabs:concept/ConvergentExecution"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-convergence",
      "urn:csabs:source/compiler-llvm"
    ],
    "sourceLocator": "ConvergentOperations: Overview, Convergent Operations, texture sampling example; LangRef: convergent attribute, convergencectrl bundles",
    "sourceNote": "Adapted Control-sensitive communicating thread instances from ConvergentOperations: Overview, Convergent Operations, texture sampling example; LangRef: convergent attribute, convergencectrl bundles. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:law/ConvergentExecution-memory-purity-insufficient",
    "type": "Law",
    "name": "memory-purity-insufficient",
    "description": "Derived consequence in the stated profile.",
    "statement": "An empty memory-effect summary alone does not justify sinking a convergent operation under a divergent condition.",
    "formalStatement": "An empty memory-effect summary alone does not justify sinking a convergent operation under a divergent condition.",
    "assumptions": [
      "LLVM 21.1.8 controlled and uncontrolled convergence require their documented rules. Thread groups/scopes and matching dynamic instances are explicit; a Boolean convergent flag alone is not a full communication model. Control-flow motion, duplication and loop transformations must preserve or legitimately refine the permitted communication instances and control tokens. Memory-effect freedom does not imply this. Convergence communication is outside the ordinary memory model; an atomic synchronization proof alone does not establish convergence preservation."
    ],
    "appliesTo": [
      "urn:csabs:concept/ConvergentExecution"
    ],
    "dependsOn": [
      "urn:csabs:axiom/ConvergentExecution-group-dependence",
      "urn:csabs:axiom/ConvergentExecution-control-obligation"
    ],
    "proofSketch": "The condition can remove participants needed for communication while leaving each thread memory effects empty, as in the cited texture-sampling example.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-convergence",
      "urn:csabs:source/compiler-llvm"
    ],
    "sourceLocator": "ConvergentOperations: Overview, Convergent Operations, texture sampling example; LangRef: convergent attribute, convergencectrl bundles",
    "sourceNote": "Catalog derivation from the explicit dependsOn premises; the cited source motivates the interface, not this exact editorial theorem name.",
    "provenanceKind": "derived",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  }
]
```
<!-- graph-record:end -->
