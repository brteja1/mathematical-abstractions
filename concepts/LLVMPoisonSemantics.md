# LLVM scalar deferred undefinedness and freeze

A versioned scalar value profile distinguishing concrete values, per-use undef choices and poison, with immediate UB modeled at execution level and freeze choosing one stable concrete result per dynamic execution.

**Notation:** Value(A)=Concrete(A)+Undef+Poison; freeze(concrete a)=a; freeze(undef/poison) chooses a∈A

**Stable ID:** `urn:csabs:concept/LLVMPoisonSemantics`

**Categories:** Programming-language semantics → Compiler transformations

**Kind:** Numeric data type

**Prerequisites:** [Fixed-width bit vector](BitVector.md), [Observable behavior refinement (ObservationalRefinement)](BehaviorRefinement.md)

**Related concepts:** [Floating-point type](FloatingPointType.md), [Typed static single assignment with scoped uses](SSAForm.md), [Defined terminating silent speculation](SpeculationSafety.md), [LLVM fixed-width integer operations and flags](LLVMIntegerSemantics.md), [LLVM floating-point environment and rewrite permissions](LLVMFloatingPointSemantics.md), [Lane-indexed vector execution and inactive-lane policy](PredicatedVectorSemantics.md), [Allocation-associated pointer provenance and lifetime](PointerProvenance.md)

## Backlinks

- [Observable behavior refinement (ObservationalRefinement)](BehaviorRefinement.md) — `relatedConcept`
- [LLVM floating-point environment and rewrite permissions](LLVMFloatingPointSemantics.md) — `requiresConcept`
- [LLVM fixed-width integer operations and flags](LLVMIntegerSemantics.md) — `requiresConcept`
- [Allocation-associated pointer provenance and lifetime](PointerProvenance.md) — `relatedConcept`
- [Lane-indexed vector execution and inactive-lane policy](PredicatedVectorSemantics.md) — `requiresConcept`
- [Defined terminating silent speculation](SpeculationSafety.md) — `relatedConcept`

## Mathematical formulation

A versioned scalar value profile distinguishing concrete values, per-use undef choices and poison, with immediate UB modeled at execution level and freeze choosing one stable concrete result per dynamic execution. Value(A)=Concrete(A)+Undef+Poison; freeze(concrete a)=a; freeze(undef/poison) chooses a∈A LLVM 21.1.8 scalar non-pointer values on a nonempty carrier A; immediate UB is not a value constructor. Ordinary integer operations use fixed-width bit patterns; nsw/nuw overflow yields poison, unlike the catalog signed-integer undefined-overflow model. Undef may differ at each use. Poison propagation is instruction-specific: select is an exception; consuming poison in branch condition triggers immediate UB. Freeze uses one choice per dynamic execution, shared by all uses of that result, with independent choices across executions/instructions. Aggregates, pointer provenance/dereferenceability, vectors, fast-math, exact/inbounds flags and memory need separate profiles.

**Lean formulation** (in its source module context):

```lean
inductive LLVMPoisonSemantics (A : Type u) where
  | concrete : A → LLVMPoisonSemantics A
  | undef : LLVMPoisonSemantics A
  | poison : LLVMPoisonSemantics A
```

**Source:** [`Catalog.Transforms.LLVMPoisonSemantics`](../lean/Catalog/CompilerTransforms.lean); consulted 2026-11-16.

**Scope:** partial

**Interpretation:** Concrete/undef/poison tagged scalar carrier; freezeResult relation is supplied in the same module.

**Limits:** No immediate-UB evaluator, instruction semantics, branch implementation, choice store, vectors, pointers or LLVM memory model. The raw carrier alone is not a complete poison semantics.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** freeze(concrete(a))={a}; freeze(undef)=A; freeze(poison)=A; uses of the same dynamic freeze result share its chosen a.; Producing poison is deferred UB; branch(poison) triggers immediate UB. Propagation follows each instruction, including select exceptions.; Two uses of undef may choose different concrete values; two uses of the same dynamic freeze result may not.

**basisKind:** relational-structural-definition

**basisScope:** LLVM 21.1.8 scalar non-pointer values on a nonempty carrier A; immediate UB is not a value constructor. Ordinary integer operations use fixed-width bit patterns; nsw/nuw overflow yields poison, unlike the catalog signed-integer undefined-overflow model. Undef may differ at each use. Poison propagation is instruction-specific: select is an exception; consuming poison in branch condition triggers immediate UB. Freeze uses one choice per dynamic execution, shared by all uses of that result, with independent choices across executions/instructions. Aggregates, pointer provenance/dereferenceability, vectors, fast-math, exact/inbounds flags and memory need separate profiles.

**verificationObligation:** Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.; No immediate-UB evaluator, instruction semantics, branch implementation, choice store, vectors, pointers or LLVM memory model. The raw carrier alone is not a complete poison semantics.

**reviewStatus:** Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-LLVMPoisonSemantics-freeze"></a>

### freeze

`urn:csabs:operation/LLVMPoisonSemantics-freeze`

**signature:** freeze : Value(A)→P(A)

**description:** Preserve a concrete input; allow any concrete result for undef/poison, committing one result per dynamic execution.

**precondition:** Nonempty scalar carrier; dynamic instruction identity tracked.

**postcondition:** Preserve a concrete input; allow any concrete result for undef/poison, committing one result per dynamic execution.

**totality:** Nondeterministic total relation.

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM IR Undefined Behavior Manual (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** LLVM LangRef: Undefined Values, Poison Values, Well-Defined Values, freeze instruction; UB Manual: Immediate UB, Deferred UB, Undef Values

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-LLVMPoisonSemantics-branch"></a>

### branch

`urn:csabs:operation/LLVMPoisonSemantics-branch`

**signature:** branch : Value(Bool)⇀Successor

**description:** Select successor for a concrete condition; undef allows a per-use choice; poison triggers immediate UB.

**precondition:** SSA and successor arguments well formed.

**postcondition:** Select successor for a concrete condition; undef allows a per-use choice; poison triggers immediate UB.

**totality:** Partial execution with explicit UB outcome.

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM IR Undefined Behavior Manual (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** LLVM LangRef: Undefined Values, Poison Values, Well-Defined Values, freeze instruction; UB Manual: Immediate UB, Deferred UB, Undef Values

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-LLVMPoisonSemantics-freeze-choice"></a>

### freeze-choice

`urn:csabs:axiom/LLVMPoisonSemantics-freeze-choice`

**description:** Defining obligation for LLVM scalar deferred undefinedness and freeze

**statement:** freeze(concrete(a))={a}; freeze(undef)=A; freeze(poison)=A; uses of the same dynamic freeze result share its chosen a.

**formalStatement:** freeze(concrete(a))={a}; freeze(undef)=A; freeze(poison)=A; uses of the same dynamic freeze result share its chosen a.

**assumptions:** LLVM 21.1.8 scalar non-pointer values on a nonempty carrier A; immediate UB is not a value constructor. Ordinary integer operations use fixed-width bit patterns; nsw/nuw overflow yields poison, unlike the catalog signed-integer undefined-overflow model. Undef may differ at each use. Poison propagation is instruction-specific: select is an exception; consuming poison in branch condition triggers immediate UB. Freeze uses one choice per dynamic execution, shared by all uses of that result, with independent choices across executions/instructions. Aggregates, pointer provenance/dereferenceability, vectors, fast-math, exact/inbounds flags and memory need separate profiles.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM IR Undefined Behavior Manual (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** LLVM LangRef: Undefined Values, Poison Values, Well-Defined Values, freeze instruction; UB Manual: Immediate UB, Deferred UB, Undef Values

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

**reviewStatus:** Editorial mathematical statement and derivation; no registered compiled witness.

<a id="node-urn-csabs-axiom-LLVMPoisonSemantics-poison-not-immediate-ub"></a>

### poison-not-immediate-ub

`urn:csabs:axiom/LLVMPoisonSemantics-poison-not-immediate-ub`

**description:** Defining obligation for LLVM scalar deferred undefinedness and freeze

**statement:** Producing poison is deferred UB; branch(poison) triggers immediate UB. Propagation follows each instruction, including select exceptions.

**formalStatement:** Producing poison is deferred UB; branch(poison) triggers immediate UB. Propagation follows each instruction, including select exceptions.

**assumptions:** LLVM 21.1.8 scalar non-pointer values on a nonempty carrier A; immediate UB is not a value constructor. Ordinary integer operations use fixed-width bit patterns; nsw/nuw overflow yields poison, unlike the catalog signed-integer undefined-overflow model. Undef may differ at each use. Poison propagation is instruction-specific: select is an exception; consuming poison in branch condition triggers immediate UB. Freeze uses one choice per dynamic execution, shared by all uses of that result, with independent choices across executions/instructions. Aggregates, pointer provenance/dereferenceability, vectors, fast-math, exact/inbounds flags and memory need separate profiles.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM IR Undefined Behavior Manual (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** LLVM LangRef: Undefined Values, Poison Values, Well-Defined Values, freeze instruction; UB Manual: Immediate UB, Deferred UB, Undef Values

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

**reviewStatus:** Editorial mathematical statement and derivation; no registered compiled witness.

<a id="node-urn-csabs-axiom-LLVMPoisonSemantics-per-use-undef"></a>

### per-use-undef

`urn:csabs:axiom/LLVMPoisonSemantics-per-use-undef`

**description:** Defining obligation for LLVM scalar deferred undefinedness and freeze

**statement:** Two uses of undef may choose different concrete values; two uses of the same dynamic freeze result may not.

**formalStatement:** Two uses of undef may choose different concrete values; two uses of the same dynamic freeze result may not.

**assumptions:** LLVM 21.1.8 scalar non-pointer values on a nonempty carrier A; immediate UB is not a value constructor. Ordinary integer operations use fixed-width bit patterns; nsw/nuw overflow yields poison, unlike the catalog signed-integer undefined-overflow model. Undef may differ at each use. Poison propagation is instruction-specific: select is an exception; consuming poison in branch condition triggers immediate UB. Freeze uses one choice per dynamic execution, shared by all uses of that result, with independent choices across executions/instructions. Aggregates, pointer provenance/dereferenceability, vectors, fast-math, exact/inbounds flags and memory need separate profiles.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM IR Undefined Behavior Manual (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** LLVM LangRef: Undefined Values, Poison Values, Well-Defined Values, freeze instruction; UB Manual: Immediate UB, Deferred UB, Undef Values

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

**reviewStatus:** Editorial mathematical statement and derivation; no registered compiled witness.

## Laws

<a id="node-urn-csabs-law-LLVMPoisonSemantics-freeze-concrete-idempotent"></a>

### freeze-concrete-idempotent

`urn:csabs:law/LLVMPoisonSemantics-freeze-concrete-idempotent`

**description:** Derived consequence within the selected semantic profile.

**statement:** For a concrete scalar a, freeze(concrete(a))={a}; freezing that chosen concrete result again yields the same a.

**formalStatement:** For a concrete scalar a, freeze(concrete(a))={a}; freezing that chosen concrete result again yields the same a.

**assumptions:** LLVM 21.1.8 scalar non-pointer values on a nonempty carrier A; immediate UB is not a value constructor. Ordinary integer operations use fixed-width bit patterns; nsw/nuw overflow yields poison, unlike the catalog signed-integer undefined-overflow model. Undef may differ at each use. Poison propagation is instruction-specific: select is an exception; consuming poison in branch condition triggers immediate UB. Freeze uses one choice per dynamic execution, shared by all uses of that result, with independent choices across executions/instructions. Aggregates, pointer provenance/dereferenceability, vectors, fast-math, exact/inbounds flags and memory need separate profiles.

**dependsOn:** [freeze-choice](LLVMPoisonSemantics.md#node-urn-csabs-axiom-LLVMPoisonSemantics-freeze-choice)

**proofSketch:** Apply the concrete-input clause twice. This does not equate independent freezes of undef or poison.

**reviewStatus:** Editorial mathematical derivation; no registered compiled witness.

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM IR Undefined Behavior Manual (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** LLVM LangRef: Undefined Values, Poison Values, Well-Defined Values, freeze instruction; UB Manual: Immediate UB, Deferred UB, Undef Values

**sourceNote:** Derived from the explicit dependsOn premises under the stated assumptions; exact claim and proof sketch are editorial.

**provenanceKind:** derived

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification
- [LLVM IR Undefined Behavior Manual (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** LLVM LangRef: Undefined Values, Poison Values, Well-Defined Values, freeze instruction; UB Manual: Immediate UB, Deferred UB, Undef Values

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/LLVMPoisonSemantics",
    "type": "Concept",
    "shortForm": "LLVMPoisonSemantics",
    "fullName": "LLVM scalar deferred undefinedness and freeze",
    "definition": "A versioned scalar value profile distinguishing concrete values, per-use undef choices and poison, with immediate UB modeled at execution level and freeze choosing one stable concrete result per dynamic execution.",
    "notation": "Value(A)=Concrete(A)+Undef+Poison; freeze(concrete a)=a; freeze(undef/poison) chooses a∈A",
    "category": [
      "urn:csabs:category/compiler-transformations"
    ],
    "kind": "urn:csabs:kind/data-type",
    "requiresConcept": [
      "urn:csabs:concept/BitVector",
      "urn:csabs:concept/BehaviorRefinement"
    ],
    "relatedConcept": [
      "urn:csabs:concept/FloatingPointType",
      "urn:csabs:concept/SSAForm",
      "urn:csabs:concept/SpeculationSafety",
      "urn:csabs:concept/LLVMIntegerSemantics",
      "urn:csabs:concept/LLVMFloatingPointSemantics",
      "urn:csabs:concept/PredicatedVectorSemantics",
      "urn:csabs:concept/PointerProvenance"
    ],
    "hasOperation": [
      "urn:csabs:operation/LLVMPoisonSemantics-freeze",
      "urn:csabs:operation/LLVMPoisonSemantics-branch"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/LLVMPoisonSemantics-freeze-choice",
      "urn:csabs:axiom/LLVMPoisonSemantics-poison-not-immediate-ub",
      "urn:csabs:axiom/LLVMPoisonSemantics-per-use-undef"
    ],
    "hasLaw": [
      "urn:csabs:law/LLVMPoisonSemantics-freeze-concrete-idempotent"
    ],
    "hasTheorem": [],
    "basisKind": "relational-structural-definition",
    "basisScope": "LLVM 21.1.8 scalar non-pointer values on a nonempty carrier A; immediate UB is not a value constructor. Ordinary integer operations use fixed-width bit patterns; nsw/nuw overflow yields poison, unlike the catalog signed-integer undefined-overflow model. Undef may differ at each use. Poison propagation is instruction-specific: select is an exception; consuming poison in branch condition triggers immediate UB. Freeze uses one choice per dynamic execution, shared by all uses of that result, with independent choices across executions/instructions. Aggregates, pointer provenance/dereferenceability, vectors, fast-math, exact/inbounds flags and memory need separate profiles.",
    "axiomBasis": "freeze(concrete(a))={a}; freeze(undef)=A; freeze(poison)=A; uses of the same dynamic freeze result share its chosen a.; Producing poison is deferred UB; branch(poison) triggers immediate UB. Propagation follows each instruction, including select exceptions.; Two uses of undef may choose different concrete values; two uses of the same dynamic freeze result may not.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.",
    "verificationObligation": [
      "Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.",
      "No immediate-UB evaluator, instruction semantics, branch implementation, choice store, vectors, pointers or LLVM memory model. The raw carrier alone is not a complete poison semantics."
    ],
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-ub"
    ],
    "sourceLocator": "LLVM LangRef: Undefined Values, Poison Values, Well-Defined Values, freeze instruction; UB Manual: Immediate UB, Deferred UB, Undef Values",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted",
    "mathematicalFormulation": "A versioned scalar value profile distinguishing concrete values, per-use undef choices and poison, with immediate UB modeled at execution level and freeze choosing one stable concrete result per dynamic execution. Value(A)=Concrete(A)+Undef+Poison; freeze(concrete a)=a; freeze(undef/poison) chooses a∈A LLVM 21.1.8 scalar non-pointer values on a nonempty carrier A; immediate UB is not a value constructor. Ordinary integer operations use fixed-width bit patterns; nsw/nuw overflow yields poison, unlike the catalog signed-integer undefined-overflow model. Undef may differ at each use. Poison propagation is instruction-specific: select is an exception; consuming poison in branch condition triggers immediate UB. Freeze uses one choice per dynamic execution, shared by all uses of that result, with independent choices across executions/instructions. Aggregates, pointer provenance/dereferenceability, vectors, fast-math, exact/inbounds flags and memory need separate profiles.",
    "leanFormulation": "inductive LLVMPoisonSemantics (A : Type u) where\n  | concrete : A → LLVMPoisonSemantics A\n  | undef : LLVMPoisonSemantics A\n  | poison : LLVMPoisonSemantics A",
    "formulationSource": "urn:csabs:source/compiler-lean",
    "formulationLocator": "Catalog.Transforms.LLVMPoisonSemantics",
    "formulationScope": "partial",
    "leanModelMapping": "Concrete/undef/poison tagged scalar carrier; freezeResult relation is supplied in the same module.",
    "leanModelLimitations": "No immediate-UB evaluator, instruction semantics, branch implementation, choice store, vectors, pointers or LLVM memory model. The raw carrier alone is not a complete poison semantics."
  },
  {
    "id": "urn:csabs:operation/LLVMPoisonSemantics-freeze",
    "type": "Operation",
    "name": "freeze",
    "signature": "freeze : Value(A)→P(A)",
    "description": "Preserve a concrete input; allow any concrete result for undef/poison, committing one result per dynamic execution.",
    "concept": "urn:csabs:concept/LLVMPoisonSemantics",
    "precondition": "Nonempty scalar carrier; dynamic instruction identity tracked.",
    "postcondition": "Preserve a concrete input; allow any concrete result for undef/poison, committing one result per dynamic execution.",
    "totality": "Nondeterministic total relation.",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-ub"
    ],
    "sourceLocator": "LLVM LangRef: Undefined Values, Poison Values, Well-Defined Values, freeze instruction; UB Manual: Immediate UB, Deferred UB, Undef Values",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/LLVMPoisonSemantics-branch",
    "type": "Operation",
    "name": "branch",
    "signature": "branch : Value(Bool)⇀Successor",
    "description": "Select successor for a concrete condition; undef allows a per-use choice; poison triggers immediate UB.",
    "concept": "urn:csabs:concept/LLVMPoisonSemantics",
    "precondition": "SSA and successor arguments well formed.",
    "postcondition": "Select successor for a concrete condition; undef allows a per-use choice; poison triggers immediate UB.",
    "totality": "Partial execution with explicit UB outcome.",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-ub"
    ],
    "sourceLocator": "LLVM LangRef: Undefined Values, Poison Values, Well-Defined Values, freeze instruction; UB Manual: Immediate UB, Deferred UB, Undef Values",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/LLVMPoisonSemantics-freeze-choice",
    "type": "Axiom",
    "name": "freeze-choice",
    "description": "Defining obligation for LLVM scalar deferred undefinedness and freeze",
    "statement": "freeze(concrete(a))={a}; freeze(undef)=A; freeze(poison)=A; uses of the same dynamic freeze result share its chosen a.",
    "formalStatement": "freeze(concrete(a))={a}; freeze(undef)=A; freeze(poison)=A; uses of the same dynamic freeze result share its chosen a.",
    "assumptions": [
      "LLVM 21.1.8 scalar non-pointer values on a nonempty carrier A; immediate UB is not a value constructor. Ordinary integer operations use fixed-width bit patterns; nsw/nuw overflow yields poison, unlike the catalog signed-integer undefined-overflow model. Undef may differ at each use. Poison propagation is instruction-specific: select is an exception; consuming poison in branch condition triggers immediate UB. Freeze uses one choice per dynamic execution, shared by all uses of that result, with independent choices across executions/instructions. Aggregates, pointer provenance/dereferenceability, vectors, fast-math, exact/inbounds flags and memory need separate profiles."
    ],
    "appliesTo": [
      "urn:csabs:concept/LLVMPoisonSemantics"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-ub"
    ],
    "sourceLocator": "LLVM LangRef: Undefined Values, Poison Values, Well-Defined Values, freeze instruction; UB Manual: Immediate UB, Deferred UB, Undef Values",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial mathematical statement and derivation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:axiom/LLVMPoisonSemantics-poison-not-immediate-ub",
    "type": "Axiom",
    "name": "poison-not-immediate-ub",
    "description": "Defining obligation for LLVM scalar deferred undefinedness and freeze",
    "statement": "Producing poison is deferred UB; branch(poison) triggers immediate UB. Propagation follows each instruction, including select exceptions.",
    "formalStatement": "Producing poison is deferred UB; branch(poison) triggers immediate UB. Propagation follows each instruction, including select exceptions.",
    "assumptions": [
      "LLVM 21.1.8 scalar non-pointer values on a nonempty carrier A; immediate UB is not a value constructor. Ordinary integer operations use fixed-width bit patterns; nsw/nuw overflow yields poison, unlike the catalog signed-integer undefined-overflow model. Undef may differ at each use. Poison propagation is instruction-specific: select is an exception; consuming poison in branch condition triggers immediate UB. Freeze uses one choice per dynamic execution, shared by all uses of that result, with independent choices across executions/instructions. Aggregates, pointer provenance/dereferenceability, vectors, fast-math, exact/inbounds flags and memory need separate profiles."
    ],
    "appliesTo": [
      "urn:csabs:concept/LLVMPoisonSemantics"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-ub"
    ],
    "sourceLocator": "LLVM LangRef: Undefined Values, Poison Values, Well-Defined Values, freeze instruction; UB Manual: Immediate UB, Deferred UB, Undef Values",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial mathematical statement and derivation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:axiom/LLVMPoisonSemantics-per-use-undef",
    "type": "Axiom",
    "name": "per-use-undef",
    "description": "Defining obligation for LLVM scalar deferred undefinedness and freeze",
    "statement": "Two uses of undef may choose different concrete values; two uses of the same dynamic freeze result may not.",
    "formalStatement": "Two uses of undef may choose different concrete values; two uses of the same dynamic freeze result may not.",
    "assumptions": [
      "LLVM 21.1.8 scalar non-pointer values on a nonempty carrier A; immediate UB is not a value constructor. Ordinary integer operations use fixed-width bit patterns; nsw/nuw overflow yields poison, unlike the catalog signed-integer undefined-overflow model. Undef may differ at each use. Poison propagation is instruction-specific: select is an exception; consuming poison in branch condition triggers immediate UB. Freeze uses one choice per dynamic execution, shared by all uses of that result, with independent choices across executions/instructions. Aggregates, pointer provenance/dereferenceability, vectors, fast-math, exact/inbounds flags and memory need separate profiles."
    ],
    "appliesTo": [
      "urn:csabs:concept/LLVMPoisonSemantics"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-ub"
    ],
    "sourceLocator": "LLVM LangRef: Undefined Values, Poison Values, Well-Defined Values, freeze instruction; UB Manual: Immediate UB, Deferred UB, Undef Values",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial mathematical statement and derivation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:law/LLVMPoisonSemantics-freeze-concrete-idempotent",
    "type": "Law",
    "name": "freeze-concrete-idempotent",
    "description": "Derived consequence within the selected semantic profile.",
    "statement": "For a concrete scalar a, freeze(concrete(a))={a}; freezing that chosen concrete result again yields the same a.",
    "formalStatement": "For a concrete scalar a, freeze(concrete(a))={a}; freezing that chosen concrete result again yields the same a.",
    "assumptions": [
      "LLVM 21.1.8 scalar non-pointer values on a nonempty carrier A; immediate UB is not a value constructor. Ordinary integer operations use fixed-width bit patterns; nsw/nuw overflow yields poison, unlike the catalog signed-integer undefined-overflow model. Undef may differ at each use. Poison propagation is instruction-specific: select is an exception; consuming poison in branch condition triggers immediate UB. Freeze uses one choice per dynamic execution, shared by all uses of that result, with independent choices across executions/instructions. Aggregates, pointer provenance/dereferenceability, vectors, fast-math, exact/inbounds flags and memory need separate profiles."
    ],
    "appliesTo": [
      "urn:csabs:concept/LLVMPoisonSemantics"
    ],
    "dependsOn": [
      "urn:csabs:axiom/LLVMPoisonSemantics-freeze-choice"
    ],
    "proofSketch": "Apply the concrete-input clause twice. This does not equate independent freezes of undef or poison.",
    "reviewStatus": "Editorial mathematical derivation; no registered compiled witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-ub"
    ],
    "sourceLocator": "LLVM LangRef: Undefined Values, Poison Values, Well-Defined Values, freeze instruction; UB Manual: Immediate UB, Deferred UB, Undef Values",
    "sourceNote": "Derived from the explicit dependsOn premises under the stated assumptions; exact claim and proof sketch are editorial.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
