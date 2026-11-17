# Conservative resource effect summary

An overapproximation of resources and actions an operation may affect, with unknown effects represented conservatively and stage order retained when relevant.

**Notation:** ActualEffects(op) ⊆ Summary(op); Unknown=⊤

**Stable ID:** `urn:csabs:concept/EffectSummary`

**Categories:** Programming-language semantics → Compiler transformations

**Kind:** semantic-model

**Prerequisites:** [Set](Set.md)

**Related concepts:** [Relational method contract with write effects](MethodContract.md), [Finite allocated heap store](HeapStore.md), [Defined terminating silent speculation](SpeculationSafety.md), [Memory dependence and legal loop rescheduling](LoopDependence.md), [Conservative alias and Mod/Ref query contract](AliasAnalysis.md), [Conservative SSA indexing of memory versions](MemorySSA.md), [Scoped atomic execution graph and memory ordering](AtomicMemoryModel.md), [Call-boundary behavior and effect contract](CallEffectContract.md), [Control-sensitive communicating thread instances](ConvergentExecution.md), [Program side-effect algebra (total sequential effect-quantale profile)](EffectAlgebra.md)

## Backlinks

- [Conservative alias and Mod/Ref query contract](AliasAnalysis.md) — `relatedConcept`
- [Call-boundary behavior and effect contract](CallEffectContract.md) — `requiresConcept`
- [Program side-effect algebra (total sequential effect-quantale profile)](EffectAlgebra.md) — `relatedConcept`
- [Guarded contextual program rewrite](GuardedRewrite.md) — `relatedConcept`
- [Memory dependence and legal loop rescheduling](LoopDependence.md) — `requiresConcept`
- [Defined terminating silent speculation](SpeculationSafety.md) — `requiresConcept`

## Mathematical formulation

An overapproximation of resources and actions an operation may affect, with unknown effects represented conservatively and stage order retained when relevant. ActualEffects(op) ⊆ Summary(op); Unknown=⊤ Effect events distinguish read, write, allocate and free on resource identities and optionally locations/stages. Distinct SSA operands may alias the same resource. Unknown interface information cannot be interpreted as an empty set. Effects here describe CFG-region behavior; graph-region conventions, volatile/atomic order, exceptions, synchronization and non-local control need additional semantics. Empty memory effects do not exclude UB or divergence.

**Lean formulation** (in its source module context):

```lean
structure EffectSummary (Op Resource : Type u) where
  actual : Op → Set Resource
  summary : Op → Set Resource
  sound : ∀ op, actual op ⊆ summary op
```

**Source:** [`Catalog.Transforms.EffectSummary`](../lean/Catalog/CompilerTransforms.lean); consulted 2026-11-16.

**Scope:** partial

**Interpretation:** Supplied actual and summary sets over a resource/event carrier with an inclusion law.

**Limits:** Lean omits event stages, alias algorithm and conflict calculus. Disjoint summaries alone do not prove arbitrary concurrent commutation or speculation.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** ∀op, ActualEffects(op)⊆Summary(op).; Summary(unknown)=AllEffectEvents; unknown≠empty.

**basisKind:** relational-structural-definition

**basisScope:** Effect events distinguish read, write, allocate and free on resource identities and optionally locations/stages. Distinct SSA operands may alias the same resource. Unknown interface information cannot be interpreted as an empty set. Effects here describe CFG-region behavior; graph-region conventions, volatile/atomic order, exceptions, synchronization and non-local control need additional semantics. Empty memory effects do not exclude UB or divergence.

**verificationObligation:** Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.; Lean omits event stages, alias algorithm and conflict calculus. Disjoint summaries alone do not prove arbitrary concurrent commutation or speculation.

**reviewStatus:** Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-EffectSummary-summarize"></a>

### summarize

`urn:csabs:operation/EffectSummary-summarize`

**signature:** summarize : Operation→P(EffectEvent)

**description:** Return an overapproximation, using top for unknown effects.

**precondition:** Resource/alias and recursive-region policy fixed.

**postcondition:** Return an overapproximation, using top for unknown effects.

**totality:** Total abstract query.

**source:** [MLIR Side Effects and Speculation rationale (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/Rationale/SideEffectsAndSpeculation.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/Rationale/SideEffectsAndSpeculation.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** Side Effects and Speculation: Categorization, Modeling, Examples

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-EffectSummary-conflicts"></a>

### conflicts

`urn:csabs:operation/EffectSummary-conflicts`

**signature:** conflicts : Summary×Summary→Prop

**description:** Conservatively detect potentially order-sensitive resource effects.

**precondition:** Sound alias information; unsupported effects conservatively conflict.

**postcondition:** Conservatively detect potentially order-sensitive resource effects.

**totality:** Total predicate.

**source:** [MLIR Side Effects and Speculation rationale (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/Rationale/SideEffectsAndSpeculation.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/Rationale/SideEffectsAndSpeculation.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** Side Effects and Speculation: Categorization, Modeling, Examples

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-EffectSummary-overapproximation"></a>

### overapproximation

`urn:csabs:axiom/EffectSummary-overapproximation`

**description:** Defining obligation for Conservative resource effect summary

**statement:** ∀op, ActualEffects(op)⊆Summary(op).

**formalStatement:** ∀op, ActualEffects(op)⊆Summary(op).

**assumptions:** Effect events distinguish read, write, allocate and free on resource identities and optionally locations/stages. Distinct SSA operands may alias the same resource. Unknown interface information cannot be interpreted as an empty set. Effects here describe CFG-region behavior; graph-region conventions, volatile/atomic order, exceptions, synchronization and non-local control need additional semantics. Empty memory effects do not exclude UB or divergence.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [MLIR Side Effects and Speculation rationale (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/Rationale/SideEffectsAndSpeculation.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/Rationale/SideEffectsAndSpeculation.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** Side Effects and Speculation: Categorization, Modeling, Examples

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

**reviewStatus:** Editorial mathematical statement and derivation; no registered compiled witness.

<a id="node-urn-csabs-axiom-EffectSummary-unknown-top"></a>

### unknown-top

`urn:csabs:axiom/EffectSummary-unknown-top`

**description:** Defining obligation for Conservative resource effect summary

**statement:** Summary(unknown)=AllEffectEvents; unknown≠empty.

**formalStatement:** Summary(unknown)=AllEffectEvents; unknown≠empty.

**assumptions:** Effect events distinguish read, write, allocate and free on resource identities and optionally locations/stages. Distinct SSA operands may alias the same resource. Unknown interface information cannot be interpreted as an empty set. Effects here describe CFG-region behavior; graph-region conventions, volatile/atomic order, exceptions, synchronization and non-local control need additional semantics. Empty memory effects do not exclude UB or divergence.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [MLIR Side Effects and Speculation rationale (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/Rationale/SideEffectsAndSpeculation.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/Rationale/SideEffectsAndSpeculation.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** Side Effects and Speculation: Categorization, Modeling, Examples

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

**reviewStatus:** Editorial mathematical statement and derivation; no registered compiled witness.

## Laws

<a id="node-urn-csabs-law-EffectSummary-empty-summary"></a>

### empty-summary

`urn:csabs:law/EffectSummary-empty-summary`

**description:** Derived consequence within the selected semantic profile.

**statement:** Summary(op)=∅ ⇒ ActualEffects(op)=∅ in the modeled resource universe.

**formalStatement:** Summary(op)=∅ ⇒ ActualEffects(op)=∅ in the modeled resource universe.

**assumptions:** Effect events distinguish read, write, allocate and free on resource identities and optionally locations/stages. Distinct SSA operands may alias the same resource. Unknown interface information cannot be interpreted as an empty set. Effects here describe CFG-region behavior; graph-region conventions, volatile/atomic order, exceptions, synchronization and non-local control need additional semantics. Empty memory effects do not exclude UB or divergence.

**dependsOn:** [overapproximation](EffectSummary.md#node-urn-csabs-axiom-EffectSummary-overapproximation)

**proofSketch:** The only subset of the empty set is empty. This conclusion says nothing about unmodeled UB, divergence or control effects.

**reviewStatus:** Editorial mathematical derivation; no registered compiled witness.

**notationLanguage:** informal mathematical Unicode

**source:** [MLIR Side Effects and Speculation rationale (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/Rationale/SideEffectsAndSpeculation.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/Rationale/SideEffectsAndSpeculation.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** Side Effects and Speculation: Categorization, Modeling, Examples

**sourceNote:** Derived from the explicit dependsOn premises under the stated assumptions; exact claim and proof sketch are editorial.

**provenanceKind:** derived

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [MLIR Side Effects and Speculation rationale (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/Rationale/SideEffectsAndSpeculation.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/Rationale/SideEffectsAndSpeculation.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** Side Effects and Speculation: Categorization, Modeling, Examples

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/EffectSummary",
    "type": "Concept",
    "shortForm": "EffectSummary",
    "fullName": "Conservative resource effect summary",
    "definition": "An overapproximation of resources and actions an operation may affect, with unknown effects represented conservatively and stage order retained when relevant.",
    "notation": "ActualEffects(op) ⊆ Summary(op); Unknown=⊤",
    "category": [
      "urn:csabs:category/compiler-transformations"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "requiresConcept": [
      "urn:csabs:concept/Set"
    ],
    "relatedConcept": [
      "urn:csabs:concept/MethodContract",
      "urn:csabs:concept/HeapStore",
      "urn:csabs:concept/SpeculationSafety",
      "urn:csabs:concept/LoopDependence",
      "urn:csabs:concept/AliasAnalysis",
      "urn:csabs:concept/MemorySSA",
      "urn:csabs:concept/AtomicMemoryModel",
      "urn:csabs:concept/CallEffectContract",
      "urn:csabs:concept/ConvergentExecution",
      "urn:csabs:concept/EffectAlgebra"
    ],
    "hasOperation": [
      "urn:csabs:operation/EffectSummary-summarize",
      "urn:csabs:operation/EffectSummary-conflicts"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/EffectSummary-overapproximation",
      "urn:csabs:axiom/EffectSummary-unknown-top"
    ],
    "hasLaw": [
      "urn:csabs:law/EffectSummary-empty-summary"
    ],
    "hasTheorem": [],
    "basisKind": "relational-structural-definition",
    "basisScope": "Effect events distinguish read, write, allocate and free on resource identities and optionally locations/stages. Distinct SSA operands may alias the same resource. Unknown interface information cannot be interpreted as an empty set. Effects here describe CFG-region behavior; graph-region conventions, volatile/atomic order, exceptions, synchronization and non-local control need additional semantics. Empty memory effects do not exclude UB or divergence.",
    "axiomBasis": "∀op, ActualEffects(op)⊆Summary(op).; Summary(unknown)=AllEffectEvents; unknown≠empty.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.",
    "verificationObligation": [
      "Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.",
      "Lean omits event stages, alias algorithm and conflict calculus. Disjoint summaries alone do not prove arbitrary concurrent commutation or speculation."
    ],
    "source": [
      "urn:csabs:source/compiler-effects"
    ],
    "sourceLocator": "Side Effects and Speculation: Categorization, Modeling, Examples",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted",
    "mathematicalFormulation": "An overapproximation of resources and actions an operation may affect, with unknown effects represented conservatively and stage order retained when relevant. ActualEffects(op) ⊆ Summary(op); Unknown=⊤ Effect events distinguish read, write, allocate and free on resource identities and optionally locations/stages. Distinct SSA operands may alias the same resource. Unknown interface information cannot be interpreted as an empty set. Effects here describe CFG-region behavior; graph-region conventions, volatile/atomic order, exceptions, synchronization and non-local control need additional semantics. Empty memory effects do not exclude UB or divergence.",
    "leanFormulation": "structure EffectSummary (Op Resource : Type u) where\n  actual : Op → Set Resource\n  summary : Op → Set Resource\n  sound : ∀ op, actual op ⊆ summary op",
    "formulationSource": "urn:csabs:source/compiler-lean",
    "formulationLocator": "Catalog.Transforms.EffectSummary",
    "formulationScope": "partial",
    "leanModelMapping": "Supplied actual and summary sets over a resource/event carrier with an inclusion law.",
    "leanModelLimitations": "Lean omits event stages, alias algorithm and conflict calculus. Disjoint summaries alone do not prove arbitrary concurrent commutation or speculation."
  },
  {
    "id": "urn:csabs:operation/EffectSummary-summarize",
    "type": "Operation",
    "name": "summarize",
    "signature": "summarize : Operation→P(EffectEvent)",
    "description": "Return an overapproximation, using top for unknown effects.",
    "concept": "urn:csabs:concept/EffectSummary",
    "precondition": "Resource/alias and recursive-region policy fixed.",
    "postcondition": "Return an overapproximation, using top for unknown effects.",
    "totality": "Total abstract query.",
    "source": [
      "urn:csabs:source/compiler-effects"
    ],
    "sourceLocator": "Side Effects and Speculation: Categorization, Modeling, Examples",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/EffectSummary-conflicts",
    "type": "Operation",
    "name": "conflicts",
    "signature": "conflicts : Summary×Summary→Prop",
    "description": "Conservatively detect potentially order-sensitive resource effects.",
    "concept": "urn:csabs:concept/EffectSummary",
    "precondition": "Sound alias information; unsupported effects conservatively conflict.",
    "postcondition": "Conservatively detect potentially order-sensitive resource effects.",
    "totality": "Total predicate.",
    "source": [
      "urn:csabs:source/compiler-effects"
    ],
    "sourceLocator": "Side Effects and Speculation: Categorization, Modeling, Examples",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/EffectSummary-overapproximation",
    "type": "Axiom",
    "name": "overapproximation",
    "description": "Defining obligation for Conservative resource effect summary",
    "statement": "∀op, ActualEffects(op)⊆Summary(op).",
    "formalStatement": "∀op, ActualEffects(op)⊆Summary(op).",
    "assumptions": [
      "Effect events distinguish read, write, allocate and free on resource identities and optionally locations/stages. Distinct SSA operands may alias the same resource. Unknown interface information cannot be interpreted as an empty set. Effects here describe CFG-region behavior; graph-region conventions, volatile/atomic order, exceptions, synchronization and non-local control need additional semantics. Empty memory effects do not exclude UB or divergence."
    ],
    "appliesTo": [
      "urn:csabs:concept/EffectSummary"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-effects"
    ],
    "sourceLocator": "Side Effects and Speculation: Categorization, Modeling, Examples",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial mathematical statement and derivation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:axiom/EffectSummary-unknown-top",
    "type": "Axiom",
    "name": "unknown-top",
    "description": "Defining obligation for Conservative resource effect summary",
    "statement": "Summary(unknown)=AllEffectEvents; unknown≠empty.",
    "formalStatement": "Summary(unknown)=AllEffectEvents; unknown≠empty.",
    "assumptions": [
      "Effect events distinguish read, write, allocate and free on resource identities and optionally locations/stages. Distinct SSA operands may alias the same resource. Unknown interface information cannot be interpreted as an empty set. Effects here describe CFG-region behavior; graph-region conventions, volatile/atomic order, exceptions, synchronization and non-local control need additional semantics. Empty memory effects do not exclude UB or divergence."
    ],
    "appliesTo": [
      "urn:csabs:concept/EffectSummary"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-effects"
    ],
    "sourceLocator": "Side Effects and Speculation: Categorization, Modeling, Examples",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial mathematical statement and derivation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:law/EffectSummary-empty-summary",
    "type": "Law",
    "name": "empty-summary",
    "description": "Derived consequence within the selected semantic profile.",
    "statement": "Summary(op)=∅ ⇒ ActualEffects(op)=∅ in the modeled resource universe.",
    "formalStatement": "Summary(op)=∅ ⇒ ActualEffects(op)=∅ in the modeled resource universe.",
    "assumptions": [
      "Effect events distinguish read, write, allocate and free on resource identities and optionally locations/stages. Distinct SSA operands may alias the same resource. Unknown interface information cannot be interpreted as an empty set. Effects here describe CFG-region behavior; graph-region conventions, volatile/atomic order, exceptions, synchronization and non-local control need additional semantics. Empty memory effects do not exclude UB or divergence."
    ],
    "appliesTo": [
      "urn:csabs:concept/EffectSummary"
    ],
    "dependsOn": [
      "urn:csabs:axiom/EffectSummary-overapproximation"
    ],
    "proofSketch": "The only subset of the empty set is empty. This conclusion says nothing about unmodeled UB, divergence or control effects.",
    "reviewStatus": "Editorial mathematical derivation; no registered compiled witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-effects"
    ],
    "sourceLocator": "Side Effects and Speculation: Categorization, Modeling, Examples",
    "sourceNote": "Derived from the explicit dependsOn premises under the stated assumptions; exact claim and proof sketch are editorial.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
