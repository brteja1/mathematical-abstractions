# Observable behavior refinement (ObservationalRefinement)

A relation in which every target whole-program behavior is permitted by the source under the same admissible input and observation convention; nondeterminism may be reduced. Also called observational refinement (ObservationalRefinement); the existing stable ID is retained for this same behavior-inclusion relation.

**Notation:** S ⊒ T ⇔ ∀i∈I, Beh(T,i) ⊆ Beh(S,i)

**Stable ID:** `urn:csabs:concept/BehaviorRefinement`

**Categories:** Programming-language semantics → Compiler transformations

**Kind:** Relation

**Prerequisites:** [Binary relation](Relation.md), [Set](Set.md)

**Specializes:** [Binary relation](Relation.md)

**Related concepts:** [Simulation](Simulation.md), [Bisimulation](Bisimulation.md), [Strong finite partial-trace equivalence](TraceEquivalence.md), [LLVM scalar deferred undefinedness and freeze](LLVMPoisonSemantics.md), [Program side-effect algebra (total sequential effect-quantale profile)](EffectAlgebra.md), [Abstract rewrite system](RewriteSystem.md)

## Backlinks

- [Scoped atomic execution graph and memory ordering](AtomicMemoryModel.md) — `relatedConcept`
- [CFG refinement with path correspondence and progress](ControlFlowRefinement.md) — `requiresConcept`
- [Typed IR legalization with representation relation](DialectConversion.md) — `requiresConcept`
- [Guarded contextual program rewrite](GuardedRewrite.md) — `requiresConcept`
- [LLVM scalar deferred undefinedness and freeze](LLVMPoisonSemantics.md) — `requiresConcept`
- [Memory dependence and legal loop rescheduling](LoopDependence.md) — `relatedConcept`
- [Instrumented trace projection and runtime contract](RuntimeInstrumentation.md) — `requiresConcept`
- [Defined terminating silent speculation](SpeculationSafety.md) — `requiresConcept`
- [Observable state representation relation](StateRepresentation.md) — `requiresConcept`
- [Environment-indexed symbol resolution and reachability](SymbolLinkage.md) — `relatedConcept`
- [Per-instance transformation validation](TranslationValidation.md) — `requiresConcept`

## Mathematical formulation

A relation in which every target whole-program behavior is permitted by the source under the same admissible input and observation convention; nondeterminism may be reduced. S ⊒ T ⇔ ∀i∈I, Beh(T,i) ⊆ Beh(S,i) Beh maps programs and admissible inputs to sets of complete observable behaviors, including termination, divergence and relevant traces. Immediate UB is totalized to the universe of permitted behaviors, rather than the empty set. A total semantics is supplied; an empty behavior set must not silently stand for timeout, UB or unsupported syntax. Equality is equality of observations. The same semantics and input set must be used when composing refinements. This is whole-program inclusion; contextual replacement requires a separate context quantifier.

**Lean formulation** (in its source module context):

```lean
def BehaviorRefinement {P I O : Type u} (behaviors : P → I → Set O)
    (source target : P) : Prop :=
  ∀ i, behaviors target i ⊆ behaviors source i
```

**Source:** [`Catalog.Transforms.BehaviorRefinement`](../lean/Catalog/CompilerTransforms.lean); consulted 2026-11-16.

**Scope:** partial

**Interpretation:** Relation on P given by pointwise inclusion of supplied P → I → Set O; source first.

**Limits:** No executable IR semantics, memory model, contextual theorem or termination adequacy proof. The inclusion definition is exact only for the supplied behavior interpretation.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** S ⊒ T ↔ ∀i, Beh(T,i)⊆Beh(S,i).; S ≃ T ↔ (S ⊒ T ∧ T ⊒ S).

**basisKind:** relational-structural-definition

**basisScope:** Beh maps programs and admissible inputs to sets of complete observable behaviors, including termination, divergence and relevant traces. Immediate UB is totalized to the universe of permitted behaviors, rather than the empty set. A total semantics is supplied; an empty behavior set must not silently stand for timeout, UB or unsupported syntax. Equality is equality of observations. The same semantics and input set must be used when composing refinements. This is whole-program inclusion; contextual replacement requires a separate context quantifier.

**specializationNote:** Instantiate the parent carrier and operation as follows: Relation on P given by pointwise inclusion of supplied P → I → Set O; source first.

**verificationObligation:** Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.; No executable IR semantics, memory model, contextual theorem or termination adequacy proof. The inclusion definition is exact only for the supplied behavior interpretation.

**reviewStatus:** Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-BehaviorRefinement-refines"></a>

### refines

`urn:csabs:operation/BehaviorRefinement-refines`

**signature:** refines : Program×Program→Prop

**description:** Test semantic inclusion, with source first and target second.

**precondition:** Same observation and input universe.

**postcondition:** Test semantic inclusion, with source first and target second.

**totality:** Total predicate; generally undecidable.

**source:** [LLVM IR Undefined Behavior Manual (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [Alive2 official README](https://github.com/AliveToolkit/alive2/blob/master/README.md); accessedOn: 2026-11-16; sourceRole: consulted-primary-tool-documentation

**sourceLocator:** UB Manual: Introduction, Immediate UB, Time Travel; Alive2 README: standalone validation, removing nsw example

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-BehaviorRefinement-equivalent"></a>

### equivalent

`urn:csabs:operation/BehaviorRefinement-equivalent`

**signature:** equivalent : Program×Program→Prop

**description:** Require refinement in both directions.

**precondition:** Same semantics.

**postcondition:** Require refinement in both directions.

**totality:** Total predicate.

**source:** [LLVM IR Undefined Behavior Manual (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [Alive2 official README](https://github.com/AliveToolkit/alive2/blob/master/README.md); accessedOn: 2026-11-16; sourceRole: consulted-primary-tool-documentation

**sourceLocator:** UB Manual: Introduction, Immediate UB, Time Travel; Alive2 README: standalone validation, removing nsw example

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-BehaviorRefinement-inclusion"></a>

### inclusion

`urn:csabs:axiom/BehaviorRefinement-inclusion`

**description:** Defining obligation for Observable behavior refinement

**statement:** S ⊒ T ↔ ∀i, Beh(T,i)⊆Beh(S,i).

**formalStatement:** S ⊒ T ↔ ∀i, Beh(T,i)⊆Beh(S,i).

**assumptions:** Beh maps programs and admissible inputs to sets of complete observable behaviors, including termination, divergence and relevant traces. Immediate UB is totalized to the universe of permitted behaviors, rather than the empty set. A total semantics is supplied; an empty behavior set must not silently stand for timeout, UB or unsupported syntax. Equality is equality of observations. The same semantics and input set must be used when composing refinements. This is whole-program inclusion; contextual replacement requires a separate context quantifier.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM IR Undefined Behavior Manual (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [Alive2 official README](https://github.com/AliveToolkit/alive2/blob/master/README.md); accessedOn: 2026-11-16; sourceRole: consulted-primary-tool-documentation

**sourceLocator:** UB Manual: Introduction, Immediate UB, Time Travel; Alive2 README: standalone validation, removing nsw example

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

**reviewStatus:** Editorial mathematical statement and derivation; no registered compiled witness.

<a id="node-urn-csabs-axiom-BehaviorRefinement-equivalence"></a>

### equivalence

`urn:csabs:axiom/BehaviorRefinement-equivalence`

**description:** Defining obligation for Observable behavior refinement

**statement:** S ≃ T ↔ (S ⊒ T ∧ T ⊒ S).

**formalStatement:** S ≃ T ↔ (S ⊒ T ∧ T ⊒ S).

**assumptions:** Beh maps programs and admissible inputs to sets of complete observable behaviors, including termination, divergence and relevant traces. Immediate UB is totalized to the universe of permitted behaviors, rather than the empty set. A total semantics is supplied; an empty behavior set must not silently stand for timeout, UB or unsupported syntax. Equality is equality of observations. The same semantics and input set must be used when composing refinements. This is whole-program inclusion; contextual replacement requires a separate context quantifier.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM IR Undefined Behavior Manual (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [Alive2 official README](https://github.com/AliveToolkit/alive2/blob/master/README.md); accessedOn: 2026-11-16; sourceRole: consulted-primary-tool-documentation

**sourceLocator:** UB Manual: Introduction, Immediate UB, Time Travel; Alive2 README: standalone validation, removing nsw example

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

**reviewStatus:** Editorial mathematical statement and derivation; no registered compiled witness.

## Laws

<a id="node-urn-csabs-law-BehaviorRefinement-reflexive"></a>

### reflexive

`urn:csabs:law/BehaviorRefinement-reflexive`

**description:** Derived consequence in the stated profile.

**statement:** S ⊒ S.

**formalStatement:** S ⊒ S.

**assumptions:** Beh maps programs and admissible inputs to sets of complete observable behaviors, including termination, divergence and relevant traces. Immediate UB is totalized to the universe of permitted behaviors, rather than the empty set. A total semantics is supplied; an empty behavior set must not silently stand for timeout, UB or unsupported syntax. Equality is equality of observations. The same semantics and input set must be used when composing refinements. This is whole-program inclusion; contextual replacement requires a separate context quantifier.

**dependsOn:** [inclusion](BehaviorRefinement.md#node-urn-csabs-axiom-BehaviorRefinement-inclusion)

**proofSketch:** Every set is a subset of itself.

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM IR Undefined Behavior Manual (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [Alive2 official README](https://github.com/AliveToolkit/alive2/blob/master/README.md); accessedOn: 2026-11-16; sourceRole: consulted-primary-tool-documentation

**sourceLocator:** UB Manual: Introduction, Immediate UB, Time Travel; Alive2 README: standalone validation, removing nsw example

**sourceNote:** Catalog derivation from the explicit dependsOn premises; the cited source motivates the interface, not this exact editorial theorem name.

**provenanceKind:** derived

**reviewStatus:** Editorial mathematical statement and derivation; no registered compiled witness.

<a id="node-urn-csabs-law-BehaviorRefinement-transitive"></a>

### transitive

`urn:csabs:law/BehaviorRefinement-transitive`

**description:** Derived consequence in the stated profile.

**statement:** S ⊒ M ∧ M ⊒ T ⇒ S ⊒ T.

**formalStatement:** S ⊒ M ∧ M ⊒ T ⇒ S ⊒ T.

**assumptions:** Beh maps programs and admissible inputs to sets of complete observable behaviors, including termination, divergence and relevant traces. Immediate UB is totalized to the universe of permitted behaviors, rather than the empty set. A total semantics is supplied; an empty behavior set must not silently stand for timeout, UB or unsupported syntax. Equality is equality of observations. The same semantics and input set must be used when composing refinements. This is whole-program inclusion; contextual replacement requires a separate context quantifier.

**dependsOn:** [inclusion](BehaviorRefinement.md#node-urn-csabs-axiom-BehaviorRefinement-inclusion)

**proofSketch:** For each input and target behavior use the second inclusion followed by the first.

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM IR Undefined Behavior Manual (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [Alive2 official README](https://github.com/AliveToolkit/alive2/blob/master/README.md); accessedOn: 2026-11-16; sourceRole: consulted-primary-tool-documentation

**sourceLocator:** UB Manual: Introduction, Immediate UB, Time Travel; Alive2 README: standalone validation, removing nsw example

**sourceNote:** Catalog derivation from the explicit dependsOn premises; the cited source motivates the interface, not this exact editorial theorem name.

**provenanceKind:** derived

**reviewStatus:** Editorial mathematical statement and derivation; no registered compiled witness.

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [LLVM IR Undefined Behavior Manual (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification
- [Alive2 official README](https://github.com/AliveToolkit/alive2/blob/master/README.md); accessedOn: 2026-11-16; sourceRole: consulted-primary-tool-documentation

**sourceLocator:** UB Manual: Introduction, Immediate UB, Time Travel; Alive2 README: standalone validation, removing nsw example

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/BehaviorRefinement",
    "type": "Concept",
    "shortForm": "BehaviorRefinement",
    "fullName": "Observable behavior refinement (ObservationalRefinement)",
    "definition": "A relation in which every target whole-program behavior is permitted by the source under the same admissible input and observation convention; nondeterminism may be reduced. Also called observational refinement (ObservationalRefinement); the existing stable ID is retained for this same behavior-inclusion relation.",
    "notation": "S ⊒ T ⇔ ∀i∈I, Beh(T,i) ⊆ Beh(S,i)",
    "category": [
      "urn:csabs:category/compiler-transformations"
    ],
    "kind": "urn:csabs:kind/relation",
    "requiresConcept": [
      "urn:csabs:concept/Relation",
      "urn:csabs:concept/Set"
    ],
    "relatedConcept": [
      "urn:csabs:concept/Simulation",
      "urn:csabs:concept/Bisimulation",
      "urn:csabs:concept/TraceEquivalence",
      "urn:csabs:concept/LLVMPoisonSemantics",
      "urn:csabs:concept/EffectAlgebra",
      "urn:csabs:concept/RewriteSystem"
    ],
    "hasOperation": [
      "urn:csabs:operation/BehaviorRefinement-refines",
      "urn:csabs:operation/BehaviorRefinement-equivalent"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/BehaviorRefinement-inclusion",
      "urn:csabs:axiom/BehaviorRefinement-equivalence"
    ],
    "hasLaw": [
      "urn:csabs:law/BehaviorRefinement-reflexive",
      "urn:csabs:law/BehaviorRefinement-transitive"
    ],
    "hasTheorem": [],
    "basisKind": "relational-structural-definition",
    "basisScope": "Beh maps programs and admissible inputs to sets of complete observable behaviors, including termination, divergence and relevant traces. Immediate UB is totalized to the universe of permitted behaviors, rather than the empty set. A total semantics is supplied; an empty behavior set must not silently stand for timeout, UB or unsupported syntax. Equality is equality of observations. The same semantics and input set must be used when composing refinements. This is whole-program inclusion; contextual replacement requires a separate context quantifier.",
    "axiomBasis": "S ⊒ T ↔ ∀i, Beh(T,i)⊆Beh(S,i).; S ≃ T ↔ (S ⊒ T ∧ T ⊒ S).",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.",
    "verificationObligation": [
      "Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.",
      "No executable IR semantics, memory model, contextual theorem or termination adequacy proof. The inclusion definition is exact only for the supplied behavior interpretation."
    ],
    "source": [
      "urn:csabs:source/compiler-ub",
      "urn:csabs:source/compiler-alive"
    ],
    "sourceLocator": "UB Manual: Introduction, Immediate UB, Time Travel; Alive2 README: standalone validation, removing nsw example",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/Relation"
    ],
    "specializationNote": "Instantiate the parent carrier and operation as follows: Relation on P given by pointwise inclusion of supplied P → I → Set O; source first.",
    "mathematicalFormulation": "A relation in which every target whole-program behavior is permitted by the source under the same admissible input and observation convention; nondeterminism may be reduced. S ⊒ T ⇔ ∀i∈I, Beh(T,i) ⊆ Beh(S,i) Beh maps programs and admissible inputs to sets of complete observable behaviors, including termination, divergence and relevant traces. Immediate UB is totalized to the universe of permitted behaviors, rather than the empty set. A total semantics is supplied; an empty behavior set must not silently stand for timeout, UB or unsupported syntax. Equality is equality of observations. The same semantics and input set must be used when composing refinements. This is whole-program inclusion; contextual replacement requires a separate context quantifier.",
    "leanFormulation": "def BehaviorRefinement {P I O : Type u} (behaviors : P → I → Set O)\n    (source target : P) : Prop :=\n  ∀ i, behaviors target i ⊆ behaviors source i",
    "formulationSource": "urn:csabs:source/compiler-lean",
    "formulationLocator": "Catalog.Transforms.BehaviorRefinement",
    "formulationScope": "partial",
    "leanModelMapping": "Relation on P given by pointwise inclusion of supplied P → I → Set O; source first.",
    "leanModelLimitations": "No executable IR semantics, memory model, contextual theorem or termination adequacy proof. The inclusion definition is exact only for the supplied behavior interpretation."
  },
  {
    "id": "urn:csabs:operation/BehaviorRefinement-refines",
    "type": "Operation",
    "name": "refines",
    "signature": "refines : Program×Program→Prop",
    "description": "Test semantic inclusion, with source first and target second.",
    "concept": "urn:csabs:concept/BehaviorRefinement",
    "precondition": "Same observation and input universe.",
    "postcondition": "Test semantic inclusion, with source first and target second.",
    "totality": "Total predicate; generally undecidable.",
    "source": [
      "urn:csabs:source/compiler-ub",
      "urn:csabs:source/compiler-alive"
    ],
    "sourceLocator": "UB Manual: Introduction, Immediate UB, Time Travel; Alive2 README: standalone validation, removing nsw example",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/BehaviorRefinement-equivalent",
    "type": "Operation",
    "name": "equivalent",
    "signature": "equivalent : Program×Program→Prop",
    "description": "Require refinement in both directions.",
    "concept": "urn:csabs:concept/BehaviorRefinement",
    "precondition": "Same semantics.",
    "postcondition": "Require refinement in both directions.",
    "totality": "Total predicate.",
    "source": [
      "urn:csabs:source/compiler-ub",
      "urn:csabs:source/compiler-alive"
    ],
    "sourceLocator": "UB Manual: Introduction, Immediate UB, Time Travel; Alive2 README: standalone validation, removing nsw example",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/BehaviorRefinement-inclusion",
    "type": "Axiom",
    "name": "inclusion",
    "description": "Defining obligation for Observable behavior refinement",
    "statement": "S ⊒ T ↔ ∀i, Beh(T,i)⊆Beh(S,i).",
    "formalStatement": "S ⊒ T ↔ ∀i, Beh(T,i)⊆Beh(S,i).",
    "assumptions": [
      "Beh maps programs and admissible inputs to sets of complete observable behaviors, including termination, divergence and relevant traces. Immediate UB is totalized to the universe of permitted behaviors, rather than the empty set. A total semantics is supplied; an empty behavior set must not silently stand for timeout, UB or unsupported syntax. Equality is equality of observations. The same semantics and input set must be used when composing refinements. This is whole-program inclusion; contextual replacement requires a separate context quantifier."
    ],
    "appliesTo": [
      "urn:csabs:concept/BehaviorRefinement"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-ub",
      "urn:csabs:source/compiler-alive"
    ],
    "sourceLocator": "UB Manual: Introduction, Immediate UB, Time Travel; Alive2 README: standalone validation, removing nsw example",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial mathematical statement and derivation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:axiom/BehaviorRefinement-equivalence",
    "type": "Axiom",
    "name": "equivalence",
    "description": "Defining obligation for Observable behavior refinement",
    "statement": "S ≃ T ↔ (S ⊒ T ∧ T ⊒ S).",
    "formalStatement": "S ≃ T ↔ (S ⊒ T ∧ T ⊒ S).",
    "assumptions": [
      "Beh maps programs and admissible inputs to sets of complete observable behaviors, including termination, divergence and relevant traces. Immediate UB is totalized to the universe of permitted behaviors, rather than the empty set. A total semantics is supplied; an empty behavior set must not silently stand for timeout, UB or unsupported syntax. Equality is equality of observations. The same semantics and input set must be used when composing refinements. This is whole-program inclusion; contextual replacement requires a separate context quantifier."
    ],
    "appliesTo": [
      "urn:csabs:concept/BehaviorRefinement"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-ub",
      "urn:csabs:source/compiler-alive"
    ],
    "sourceLocator": "UB Manual: Introduction, Immediate UB, Time Travel; Alive2 README: standalone validation, removing nsw example",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial mathematical statement and derivation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:law/BehaviorRefinement-reflexive",
    "type": "Law",
    "name": "reflexive",
    "description": "Derived consequence in the stated profile.",
    "statement": "S ⊒ S.",
    "formalStatement": "S ⊒ S.",
    "assumptions": [
      "Beh maps programs and admissible inputs to sets of complete observable behaviors, including termination, divergence and relevant traces. Immediate UB is totalized to the universe of permitted behaviors, rather than the empty set. A total semantics is supplied; an empty behavior set must not silently stand for timeout, UB or unsupported syntax. Equality is equality of observations. The same semantics and input set must be used when composing refinements. This is whole-program inclusion; contextual replacement requires a separate context quantifier."
    ],
    "appliesTo": [
      "urn:csabs:concept/BehaviorRefinement"
    ],
    "dependsOn": [
      "urn:csabs:axiom/BehaviorRefinement-inclusion"
    ],
    "proofSketch": "Every set is a subset of itself.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-ub",
      "urn:csabs:source/compiler-alive"
    ],
    "sourceLocator": "UB Manual: Introduction, Immediate UB, Time Travel; Alive2 README: standalone validation, removing nsw example",
    "sourceNote": "Catalog derivation from the explicit dependsOn premises; the cited source motivates the interface, not this exact editorial theorem name.",
    "provenanceKind": "derived",
    "reviewStatus": "Editorial mathematical statement and derivation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:law/BehaviorRefinement-transitive",
    "type": "Law",
    "name": "transitive",
    "description": "Derived consequence in the stated profile.",
    "statement": "S ⊒ M ∧ M ⊒ T ⇒ S ⊒ T.",
    "formalStatement": "S ⊒ M ∧ M ⊒ T ⇒ S ⊒ T.",
    "assumptions": [
      "Beh maps programs and admissible inputs to sets of complete observable behaviors, including termination, divergence and relevant traces. Immediate UB is totalized to the universe of permitted behaviors, rather than the empty set. A total semantics is supplied; an empty behavior set must not silently stand for timeout, UB or unsupported syntax. Equality is equality of observations. The same semantics and input set must be used when composing refinements. This is whole-program inclusion; contextual replacement requires a separate context quantifier."
    ],
    "appliesTo": [
      "urn:csabs:concept/BehaviorRefinement"
    ],
    "dependsOn": [
      "urn:csabs:axiom/BehaviorRefinement-inclusion"
    ],
    "proofSketch": "For each input and target behavior use the second inclusion followed by the first.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-ub",
      "urn:csabs:source/compiler-alive"
    ],
    "sourceLocator": "UB Manual: Introduction, Immediate UB, Time Travel; Alive2 README: standalone validation, removing nsw example",
    "sourceNote": "Catalog derivation from the explicit dependsOn premises; the cited source motivates the interface, not this exact editorial theorem name.",
    "provenanceKind": "derived",
    "reviewStatus": "Editorial mathematical statement and derivation; no registered compiled witness."
  }
]
```
<!-- graph-record:end -->
