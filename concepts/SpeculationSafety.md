# Defined terminating silent speculation

A sufficient semantic condition for introducing execution on formerly unexecuted paths: evaluation is defined, terminates, and produces no observable effect in the newly executed states.

**Notation:** Safe(E) ⇔ ∀σ∈E, Defined(op,σ) ∧ Terminates(op,σ) ∧ Silent(op,σ)

**Stable ID:** `urn:csabs:concept/SpeculationSafety`

**Categories:** Programming-language semantics → Compiler transformations

**Kind:** semantic-model

**Prerequisites:** [Conservative resource effect summary](EffectSummary.md), [Observable behavior refinement](BehaviorRefinement.md)

**Related concepts:** [Hoare Triple](HoareTriple.md), [Termination Variant](TerminationVariant.md), [LLVM scalar deferred undefinedness and freeze](LLVMPoisonSemantics.md)

## Backlinks

- [Conservative resource effect summary](EffectSummary.md) — `relatedConcept`
- [LLVM scalar deferred undefinedness and freeze](LLVMPoisonSemantics.md) — `relatedConcept`

## Mathematical formulation

A sufficient semantic condition for introducing execution on formerly unexecuted paths: evaluation is defined, terminates, and produces no observable effect in the newly executed states. Safe(E) ⇔ ∀σ∈E, Defined(op,σ) ∧ Terminates(op,σ) ∧ Silent(op,σ) E is a sound overapproximation of reachable states newly executing the operation. All operands must already be available and defined as required. Silent means observationally unchanged state modulo permitted unobservable allocation/representation, not merely an empty memory-effects interface. Exceptions/non-local control and concurrency are excluded unless modeled. This is a sufficient condition; operations producing unused poison may be speculated if no immediate UB or observable effect results. Full motion also requires preserved values and dependence ordering.

**Lean formulation** (in its source module context):

```lean
def SpeculationSafety {State : Type u} (newlyExecuted : Set State)
    (defined terminates silent : State → Prop) : Prop :=
  ∀ s ∈ newlyExecuted, defined s ∧ terminates s ∧ silent s
```

**Source:** [`Catalog.Transforms.SpeculationSafety`](../lean/Catalog/CompilerTransforms.lean); consulted 2026-11-16.

**Scope:** partial

**Interpretation:** Predicate on supplied newly-executed states and defined/terminates/silent predicates.

**Limits:** Does not implement MLIR speculatability queries or prove code motion; reachability, operand availability and denotational adequacy remain external.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Safe(op,E) ↔ ∀σ∈E, Defined(op,σ) ∧ Terminates(op,σ) ∧ Silent(op,σ).; Unsigned scalar division by zero has immediate UB. For well-defined operands, divisor≠0 is sufficient to avoid this immediate-UB case; empty memory effects do not establish this guard.

**basisKind:** relational-structural-definition

**basisScope:** E is a sound overapproximation of reachable states newly executing the operation. All operands must already be available and defined as required. Silent means observationally unchanged state modulo permitted unobservable allocation/representation, not merely an empty memory-effects interface. Exceptions/non-local control and concurrency are excluded unless modeled. This is a sufficient condition; operations producing unused poison may be speculated if no immediate UB or observable effect results. Full motion also requires preserved values and dependence ordering.

**verificationObligation:** Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.; Does not implement MLIR speculatability queries or prove code motion; reachability, operand availability and denotational adequacy remain external.

**reviewStatus:** Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-SpeculationSafety-safe-to-introduce"></a>

### safe-to-introduce

`urn:csabs:operation/SpeculationSafety-safe-to-introduce`

**signature:** safeToIntroduce : Operation×P(State)→Prop

**description:** Require defined terminating silent evaluation in every newly executed state.

**precondition:** Sound reachability and operand-availability mapping.

**postcondition:** Require defined terminating silent evaluation in every newly executed state.

**totality:** Total semantic predicate; implementation query may return unknown.

**source:** [MLIR Side Effects and Speculation rationale (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/Rationale/SideEffectsAndSpeculation.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/Rationale/SideEffectsAndSpeculation.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM IR Undefined Behavior Manual (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** Side Effects and Speculation: Modeling; UB Manual: Immediate UB division-hoisting example

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-SpeculationSafety-new-path-obligation"></a>

### new-path-obligation

`urn:csabs:axiom/SpeculationSafety-new-path-obligation`

**description:** Defining obligation for Defined terminating silent speculation

**statement:** Safe(op,E) ↔ ∀σ∈E, Defined(op,σ) ∧ Terminates(op,σ) ∧ Silent(op,σ).

**formalStatement:** Safe(op,E) ↔ ∀σ∈E, Defined(op,σ) ∧ Terminates(op,σ) ∧ Silent(op,σ).

**assumptions:** E is a sound overapproximation of reachable states newly executing the operation. All operands must already be available and defined as required. Silent means observationally unchanged state modulo permitted unobservable allocation/representation, not merely an empty memory-effects interface. Exceptions/non-local control and concurrency are excluded unless modeled. This is a sufficient condition; operations producing unused poison may be speculated if no immediate UB or observable effect results. Full motion also requires preserved values and dependence ordering.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [MLIR Side Effects and Speculation rationale (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/Rationale/SideEffectsAndSpeculation.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/Rationale/SideEffectsAndSpeculation.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM IR Undefined Behavior Manual (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** Side Effects and Speculation: Modeling; UB Manual: Immediate UB division-hoisting example

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

**reviewStatus:** Editorial mathematical statement and derivation; no registered compiled witness.

<a id="node-urn-csabs-axiom-SpeculationSafety-division-guard"></a>

### division-guard

`urn:csabs:axiom/SpeculationSafety-division-guard`

**description:** Defining obligation for Defined terminating silent speculation

**statement:** Unsigned scalar division by zero has immediate UB. For well-defined operands, divisor≠0 is sufficient to avoid this immediate-UB case; empty memory effects do not establish this guard.

**formalStatement:** Unsigned scalar division by zero has immediate UB. For well-defined operands, divisor≠0 is sufficient to avoid this immediate-UB case; empty memory effects do not establish this guard.

**assumptions:** E is a sound overapproximation of reachable states newly executing the operation. All operands must already be available and defined as required. Silent means observationally unchanged state modulo permitted unobservable allocation/representation, not merely an empty memory-effects interface. Exceptions/non-local control and concurrency are excluded unless modeled. This is a sufficient condition; operations producing unused poison may be speculated if no immediate UB or observable effect results. Full motion also requires preserved values and dependence ordering.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [MLIR Side Effects and Speculation rationale (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/Rationale/SideEffectsAndSpeculation.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/Rationale/SideEffectsAndSpeculation.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM IR Undefined Behavior Manual (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** Side Effects and Speculation: Modeling; UB Manual: Immediate UB division-hoisting example

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

**reviewStatus:** Editorial mathematical statement and derivation; no registered compiled witness.

## Laws

<a id="node-urn-csabs-law-SpeculationSafety-no-new-executions"></a>

### no-new-executions

`urn:csabs:law/SpeculationSafety-no-new-executions`

**description:** Derived consequence within the selected semantic profile.

**statement:** E=∅ ⇒ Safe(op,E) for the new-path obligation only.

**formalStatement:** E=∅ ⇒ Safe(op,E) for the new-path obligation only.

**assumptions:** E is a sound overapproximation of reachable states newly executing the operation. All operands must already be available and defined as required. Silent means observationally unchanged state modulo permitted unobservable allocation/representation, not merely an empty memory-effects interface. Exceptions/non-local control and concurrency are excluded unless modeled. This is a sufficient condition; operations producing unused poison may be speculated if no immediate UB or observable effect results. Full motion also requires preserved values and dependence ordering.

**dependsOn:** [new-path-obligation](SpeculationSafety.md#node-urn-csabs-axiom-SpeculationSafety-new-path-obligation)

**proofSketch:** Universal quantification over an empty state set is true. Operand availability, original-path behavior and movement ordering remain separate obligations.

**reviewStatus:** Editorial mathematical derivation; no registered compiled witness.

**notationLanguage:** informal mathematical Unicode

**source:** [MLIR Side Effects and Speculation rationale (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/Rationale/SideEffectsAndSpeculation.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/Rationale/SideEffectsAndSpeculation.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM IR Undefined Behavior Manual (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** Side Effects and Speculation: Modeling; UB Manual: Immediate UB division-hoisting example

**sourceNote:** Derived from the explicit dependsOn premises under the stated assumptions; exact claim and proof sketch are editorial.

**provenanceKind:** derived

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [MLIR Side Effects and Speculation rationale (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/Rationale/SideEffectsAndSpeculation.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/Rationale/SideEffectsAndSpeculation.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification
- [LLVM IR Undefined Behavior Manual (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** Side Effects and Speculation: Modeling; UB Manual: Immediate UB division-hoisting example

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/SpeculationSafety",
    "type": "Concept",
    "shortForm": "SpeculationSafety",
    "fullName": "Defined terminating silent speculation",
    "definition": "A sufficient semantic condition for introducing execution on formerly unexecuted paths: evaluation is defined, terminates, and produces no observable effect in the newly executed states.",
    "notation": "Safe(E) ⇔ ∀σ∈E, Defined(op,σ) ∧ Terminates(op,σ) ∧ Silent(op,σ)",
    "category": [
      "urn:csabs:category/compiler-transformations"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "requiresConcept": [
      "urn:csabs:concept/EffectSummary",
      "urn:csabs:concept/BehaviorRefinement"
    ],
    "relatedConcept": [
      "urn:csabs:concept/HoareTriple",
      "urn:csabs:concept/TerminationVariant",
      "urn:csabs:concept/LLVMPoisonSemantics"
    ],
    "hasOperation": [
      "urn:csabs:operation/SpeculationSafety-safe-to-introduce"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/SpeculationSafety-new-path-obligation",
      "urn:csabs:axiom/SpeculationSafety-division-guard"
    ],
    "hasLaw": [
      "urn:csabs:law/SpeculationSafety-no-new-executions"
    ],
    "hasTheorem": [],
    "basisKind": "relational-structural-definition",
    "basisScope": "E is a sound overapproximation of reachable states newly executing the operation. All operands must already be available and defined as required. Silent means observationally unchanged state modulo permitted unobservable allocation/representation, not merely an empty memory-effects interface. Exceptions/non-local control and concurrency are excluded unless modeled. This is a sufficient condition; operations producing unused poison may be speculated if no immediate UB or observable effect results. Full motion also requires preserved values and dependence ordering.",
    "axiomBasis": "Safe(op,E) ↔ ∀σ∈E, Defined(op,σ) ∧ Terminates(op,σ) ∧ Silent(op,σ).; Unsigned scalar division by zero has immediate UB. For well-defined operands, divisor≠0 is sufficient to avoid this immediate-UB case; empty memory effects do not establish this guard.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.",
    "verificationObligation": [
      "Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.",
      "Does not implement MLIR speculatability queries or prove code motion; reachability, operand availability and denotational adequacy remain external."
    ],
    "source": [
      "urn:csabs:source/compiler-effects",
      "urn:csabs:source/compiler-ub"
    ],
    "sourceLocator": "Side Effects and Speculation: Modeling; UB Manual: Immediate UB division-hoisting example",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted",
    "mathematicalFormulation": "A sufficient semantic condition for introducing execution on formerly unexecuted paths: evaluation is defined, terminates, and produces no observable effect in the newly executed states. Safe(E) ⇔ ∀σ∈E, Defined(op,σ) ∧ Terminates(op,σ) ∧ Silent(op,σ) E is a sound overapproximation of reachable states newly executing the operation. All operands must already be available and defined as required. Silent means observationally unchanged state modulo permitted unobservable allocation/representation, not merely an empty memory-effects interface. Exceptions/non-local control and concurrency are excluded unless modeled. This is a sufficient condition; operations producing unused poison may be speculated if no immediate UB or observable effect results. Full motion also requires preserved values and dependence ordering.",
    "leanFormulation": "def SpeculationSafety {State : Type u} (newlyExecuted : Set State)\n    (defined terminates silent : State → Prop) : Prop :=\n  ∀ s ∈ newlyExecuted, defined s ∧ terminates s ∧ silent s",
    "formulationSource": "urn:csabs:source/compiler-lean",
    "formulationLocator": "Catalog.Transforms.SpeculationSafety",
    "formulationScope": "partial",
    "leanModelMapping": "Predicate on supplied newly-executed states and defined/terminates/silent predicates.",
    "leanModelLimitations": "Does not implement MLIR speculatability queries or prove code motion; reachability, operand availability and denotational adequacy remain external."
  },
  {
    "id": "urn:csabs:operation/SpeculationSafety-safe-to-introduce",
    "type": "Operation",
    "name": "safe-to-introduce",
    "signature": "safeToIntroduce : Operation×P(State)→Prop",
    "description": "Require defined terminating silent evaluation in every newly executed state.",
    "concept": "urn:csabs:concept/SpeculationSafety",
    "precondition": "Sound reachability and operand-availability mapping.",
    "postcondition": "Require defined terminating silent evaluation in every newly executed state.",
    "totality": "Total semantic predicate; implementation query may return unknown.",
    "source": [
      "urn:csabs:source/compiler-effects",
      "urn:csabs:source/compiler-ub"
    ],
    "sourceLocator": "Side Effects and Speculation: Modeling; UB Manual: Immediate UB division-hoisting example",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/SpeculationSafety-new-path-obligation",
    "type": "Axiom",
    "name": "new-path-obligation",
    "description": "Defining obligation for Defined terminating silent speculation",
    "statement": "Safe(op,E) ↔ ∀σ∈E, Defined(op,σ) ∧ Terminates(op,σ) ∧ Silent(op,σ).",
    "formalStatement": "Safe(op,E) ↔ ∀σ∈E, Defined(op,σ) ∧ Terminates(op,σ) ∧ Silent(op,σ).",
    "assumptions": [
      "E is a sound overapproximation of reachable states newly executing the operation. All operands must already be available and defined as required. Silent means observationally unchanged state modulo permitted unobservable allocation/representation, not merely an empty memory-effects interface. Exceptions/non-local control and concurrency are excluded unless modeled. This is a sufficient condition; operations producing unused poison may be speculated if no immediate UB or observable effect results. Full motion also requires preserved values and dependence ordering."
    ],
    "appliesTo": [
      "urn:csabs:concept/SpeculationSafety"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-effects",
      "urn:csabs:source/compiler-ub"
    ],
    "sourceLocator": "Side Effects and Speculation: Modeling; UB Manual: Immediate UB division-hoisting example",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial mathematical statement and derivation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:axiom/SpeculationSafety-division-guard",
    "type": "Axiom",
    "name": "division-guard",
    "description": "Defining obligation for Defined terminating silent speculation",
    "statement": "Unsigned scalar division by zero has immediate UB. For well-defined operands, divisor≠0 is sufficient to avoid this immediate-UB case; empty memory effects do not establish this guard.",
    "formalStatement": "Unsigned scalar division by zero has immediate UB. For well-defined operands, divisor≠0 is sufficient to avoid this immediate-UB case; empty memory effects do not establish this guard.",
    "assumptions": [
      "E is a sound overapproximation of reachable states newly executing the operation. All operands must already be available and defined as required. Silent means observationally unchanged state modulo permitted unobservable allocation/representation, not merely an empty memory-effects interface. Exceptions/non-local control and concurrency are excluded unless modeled. This is a sufficient condition; operations producing unused poison may be speculated if no immediate UB or observable effect results. Full motion also requires preserved values and dependence ordering."
    ],
    "appliesTo": [
      "urn:csabs:concept/SpeculationSafety"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-effects",
      "urn:csabs:source/compiler-ub"
    ],
    "sourceLocator": "Side Effects and Speculation: Modeling; UB Manual: Immediate UB division-hoisting example",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial mathematical statement and derivation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:law/SpeculationSafety-no-new-executions",
    "type": "Law",
    "name": "no-new-executions",
    "description": "Derived consequence within the selected semantic profile.",
    "statement": "E=∅ ⇒ Safe(op,E) for the new-path obligation only.",
    "formalStatement": "E=∅ ⇒ Safe(op,E) for the new-path obligation only.",
    "assumptions": [
      "E is a sound overapproximation of reachable states newly executing the operation. All operands must already be available and defined as required. Silent means observationally unchanged state modulo permitted unobservable allocation/representation, not merely an empty memory-effects interface. Exceptions/non-local control and concurrency are excluded unless modeled. This is a sufficient condition; operations producing unused poison may be speculated if no immediate UB or observable effect results. Full motion also requires preserved values and dependence ordering."
    ],
    "appliesTo": [
      "urn:csabs:concept/SpeculationSafety"
    ],
    "dependsOn": [
      "urn:csabs:axiom/SpeculationSafety-new-path-obligation"
    ],
    "proofSketch": "Universal quantification over an empty state set is true. Operand availability, original-path behavior and movement ordering remain separate obligations.",
    "reviewStatus": "Editorial mathematical derivation; no registered compiled witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-effects",
      "urn:csabs:source/compiler-ub"
    ],
    "sourceLocator": "Side Effects and Speculation: Modeling; UB Manual: Immediate UB division-hoisting example",
    "sourceNote": "Derived from the explicit dependsOn premises under the stated assumptions; exact claim and proof sketch are editorial.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
