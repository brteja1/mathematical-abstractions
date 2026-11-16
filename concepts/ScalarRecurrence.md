# Scoped induction recurrence and trip-count facts

A recurrence interpretation for induction variables with explicit arithmetic width, loop scope, exit assumptions and unknown results, usable to justify strength reduction and iteration guards.

**Notation:** a(0)=a₀; a(n+1)=a(n)+d; exact profile a(n)=a₀+n·d

**Stable ID:** `urn:csabs:concept/ScalarRecurrence`

**Categories:** Programming-language semantics → Compiler transformations

**Kind:** semantic-model

**Prerequisites:** [Mathematical integers](Integer.md), [LLVM fixed-width integer operations and flags](LLVMIntegerSemantics.md)

**Related concepts:** [Sound abstract transfer and inductive dataflow facts](AbstractInterpretation.md), [Guarded loop event-domain correspondence](LoopIterationMapping.md)

## Backlinks

- [Analysis validity across IR mutation](AnalysisPreservation.md) — `relatedConcept`
- [LLVM fixed-width integer operations and flags](LLVMIntegerSemantics.md) — `relatedConcept`
- [Memory dependence and legal loop rescheduling](LoopDependence.md) — `relatedConcept`
- [Guarded loop event-domain correspondence](LoopIterationMapping.md) — `relatedConcept`

## Mathematical formulation

A recurrence interpretation for induction variables with explicit arithmetic width, loop scope, exit assumptions and unknown results, usable to justify strength reduction and iteration guards. a(0)=a₀; a(n+1)=a(n)+d; exact profile a(n)=a₀+n·d The selected Lean recurrence is exact affine integer arithmetic. LLVM SCEV is richer and may describe modular fixed-width recurrences; lifting to exact integers needs scope-valid nowrap/range premises. SCEV flags have analysis scopes and are not copied blindly as instruction flags. Multiple exits and zero-trip guards affect counts. getSmallConstantTripCount returning 0 denotes unknown/nonconstant, not a proof of zero executions. Mathematical trip=backedges+1 needs the appropriate entered-loop/exit hypothesis and representable count width.

**Lean formulation** (in its source module context):

```lean
structure ScalarRecurrence where
  start : Int
  stride : Int
```

**Source:** [`Catalog.LLVM.ScalarRecurrence`](../lean/Catalog/LLVMTransforms.lean); consulted 2026-11-16.

**Scope:** partial

**Interpretation:** Exact Int start/stride record and recurrenceValue definition; no fixed-width lifting is implicit.

**Limits:** No SCEV DAG, higher-order recurrence, exit solver, range/nowrap analysis, count sentinel adapter or correspondence to LLVM instructions.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** a(0)=a₀ ∧ ∀n∈ℕ,a(n+1)=a(n)+d.; Count facts and nowrap facts are valid only in their stated loop/exit/input scope; unknown count is not exact zero.

**basisKind:** relational-structural-definition

**basisScope:** The selected Lean recurrence is exact affine integer arithmetic. LLVM SCEV is richer and may describe modular fixed-width recurrences; lifting to exact integers needs scope-valid nowrap/range premises. SCEV flags have analysis scopes and are not copied blindly as instruction flags. Multiple exits and zero-trip guards affect counts. getSmallConstantTripCount returning 0 denotes unknown/nonconstant, not a proof of zero executions. Mathematical trip=backedges+1 needs the appropriate entered-loop/exit hypothesis and representable count width.

**verificationObligation:** Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.; No SCEV DAG, higher-order recurrence, exit solver, range/nowrap analysis, count sentinel adapter or correspondence to LLVM instructions.

**reviewStatus:** Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-ScalarRecurrence-evaluate"></a>

### evaluate

`urn:csabs:operation/ScalarRecurrence-evaluate`

**signature:** evaluate : Recurrence×ℕ→ℤ

**description:** Evaluate the exact affine recurrence a₀+n·d.

**precondition:** Exact-integer profile or justified no-wrap lifting.

**postcondition:** Evaluate the exact affine recurrence a₀+n·d.

**totality:** Total mathematical function.

**source:** [LLVM ScalarEvolution interfaces (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/include/llvm/Analysis/ScalarEvolution.h); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/include/llvm/Analysis/ScalarEvolution.h; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM Loop Terminology (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LoopTerminology.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LoopTerminology.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** ScalarEvolution.h: SCEV NoWrapFlags, AddRec scope, getTripCountFromExitCount, getSmallConstantTripCount; LoopTerminology: trip count

**sourceNote:** Adapted Scoped induction recurrence and trip-count facts from ScalarEvolution.h: SCEV NoWrapFlags, AddRec scope, getTripCountFromExitCount, getSmallConstantTripCount; LoopTerminology: trip count. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-ScalarRecurrence-trip-fact"></a>

### trip-fact

`urn:csabs:operation/ScalarRecurrence-trip-fact`

**signature:** tripFact : Loop×Exit→Option CountFact

**description:** Return a scoped exact/bounded count or unknown.

**precondition:** Exit feasibility, arithmetic and invariants established.

**postcondition:** Return a scoped exact/bounded count or unknown.

**totality:** Partial information; unknown is distinct from exact zero.

**source:** [LLVM ScalarEvolution interfaces (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/include/llvm/Analysis/ScalarEvolution.h); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/include/llvm/Analysis/ScalarEvolution.h; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM Loop Terminology (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LoopTerminology.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LoopTerminology.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** ScalarEvolution.h: SCEV NoWrapFlags, AddRec scope, getTripCountFromExitCount, getSmallConstantTripCount; LoopTerminology: trip count

**sourceNote:** Adapted Scoped induction recurrence and trip-count facts from ScalarEvolution.h: SCEV NoWrapFlags, AddRec scope, getTripCountFromExitCount, getSmallConstantTripCount; LoopTerminology: trip count. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-ScalarRecurrence-affine-definition"></a>

### affine-definition

`urn:csabs:axiom/ScalarRecurrence-affine-definition`

**description:** Defining obligation for Scoped induction recurrence and trip-count facts

**statement:** a(0)=a₀ ∧ ∀n∈ℕ,a(n+1)=a(n)+d.

**formalStatement:** a(0)=a₀ ∧ ∀n∈ℕ,a(n+1)=a(n)+d.

**assumptions:** The selected Lean recurrence is exact affine integer arithmetic. LLVM SCEV is richer and may describe modular fixed-width recurrences; lifting to exact integers needs scope-valid nowrap/range premises. SCEV flags have analysis scopes and are not copied blindly as instruction flags. Multiple exits and zero-trip guards affect counts. getSmallConstantTripCount returning 0 denotes unknown/nonconstant, not a proof of zero executions. Mathematical trip=backedges+1 needs the appropriate entered-loop/exit hypothesis and representable count width.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM ScalarEvolution interfaces (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/include/llvm/Analysis/ScalarEvolution.h); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/include/llvm/Analysis/ScalarEvolution.h; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM Loop Terminology (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LoopTerminology.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LoopTerminology.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** ScalarEvolution.h: SCEV NoWrapFlags, AddRec scope, getTripCountFromExitCount, getSmallConstantTripCount; LoopTerminology: trip count

**sourceNote:** Adapted Scoped induction recurrence and trip-count facts from ScalarEvolution.h: SCEV NoWrapFlags, AddRec scope, getTripCountFromExitCount, getSmallConstantTripCount; LoopTerminology: trip count. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

<a id="node-urn-csabs-axiom-ScalarRecurrence-count-scope"></a>

### count-scope

`urn:csabs:axiom/ScalarRecurrence-count-scope`

**description:** Defining obligation for Scoped induction recurrence and trip-count facts

**statement:** Count facts and nowrap facts are valid only in their stated loop/exit/input scope; unknown count is not exact zero.

**formalStatement:** Count facts and nowrap facts are valid only in their stated loop/exit/input scope; unknown count is not exact zero.

**assumptions:** The selected Lean recurrence is exact affine integer arithmetic. LLVM SCEV is richer and may describe modular fixed-width recurrences; lifting to exact integers needs scope-valid nowrap/range premises. SCEV flags have analysis scopes and are not copied blindly as instruction flags. Multiple exits and zero-trip guards affect counts. getSmallConstantTripCount returning 0 denotes unknown/nonconstant, not a proof of zero executions. Mathematical trip=backedges+1 needs the appropriate entered-loop/exit hypothesis and representable count width.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM ScalarEvolution interfaces (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/include/llvm/Analysis/ScalarEvolution.h); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/include/llvm/Analysis/ScalarEvolution.h; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM Loop Terminology (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LoopTerminology.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LoopTerminology.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** ScalarEvolution.h: SCEV NoWrapFlags, AddRec scope, getTripCountFromExitCount, getSmallConstantTripCount; LoopTerminology: trip count

**sourceNote:** Adapted Scoped induction recurrence and trip-count facts from ScalarEvolution.h: SCEV NoWrapFlags, AddRec scope, getTripCountFromExitCount, getSmallConstantTripCount; LoopTerminology: trip count. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

## Laws

<a id="node-urn-csabs-law-ScalarRecurrence-zero-stride"></a>

### zero-stride

`urn:csabs:law/ScalarRecurrence-zero-stride`

**description:** Derived consequence in the stated profile.

**statement:** For the exact affine profile, d=0 ⇒ ∀n,a(n)=a₀.

**formalStatement:** For the exact affine profile, d=0 ⇒ ∀n,a(n)=a₀.

**assumptions:** The selected Lean recurrence is exact affine integer arithmetic. LLVM SCEV is richer and may describe modular fixed-width recurrences; lifting to exact integers needs scope-valid nowrap/range premises. SCEV flags have analysis scopes and are not copied blindly as instruction flags. Multiple exits and zero-trip guards affect counts. getSmallConstantTripCount returning 0 denotes unknown/nonconstant, not a proof of zero executions. Mathematical trip=backedges+1 needs the appropriate entered-loop/exit hypothesis and representable count width.

**dependsOn:** [affine-definition](ScalarRecurrence.md#node-urn-csabs-axiom-ScalarRecurrence-affine-definition)

**proofSketch:** Induct on n. The base is a(0)=a₀; the step adds zero.

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM ScalarEvolution interfaces (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/include/llvm/Analysis/ScalarEvolution.h); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/include/llvm/Analysis/ScalarEvolution.h; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM Loop Terminology (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LoopTerminology.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LoopTerminology.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** ScalarEvolution.h: SCEV NoWrapFlags, AddRec scope, getTripCountFromExitCount, getSmallConstantTripCount; LoopTerminology: trip count

**sourceNote:** Catalog derivation from the explicit dependsOn premises; the cited source motivates the interface, not this exact editorial theorem name.

**provenanceKind:** derived

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [LLVM ScalarEvolution interfaces (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/include/llvm/Analysis/ScalarEvolution.h); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/include/llvm/Analysis/ScalarEvolution.h; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface
- [LLVM Loop Terminology (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LoopTerminology.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LoopTerminology.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** ScalarEvolution.h: SCEV NoWrapFlags, AddRec scope, getTripCountFromExitCount, getSmallConstantTripCount; LoopTerminology: trip count

**sourceNote:** Adapted Scoped induction recurrence and trip-count facts from ScalarEvolution.h: SCEV NoWrapFlags, AddRec scope, getTripCountFromExitCount, getSmallConstantTripCount; LoopTerminology: trip count. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/ScalarRecurrence",
    "type": "Concept",
    "shortForm": "ScalarRecurrence",
    "fullName": "Scoped induction recurrence and trip-count facts",
    "definition": "A recurrence interpretation for induction variables with explicit arithmetic width, loop scope, exit assumptions and unknown results, usable to justify strength reduction and iteration guards.",
    "notation": "a(0)=a₀; a(n+1)=a(n)+d; exact profile a(n)=a₀+n·d",
    "category": [
      "urn:csabs:category/compiler-transformations"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "requiresConcept": [
      "urn:csabs:concept/MathematicalInteger",
      "urn:csabs:concept/LLVMIntegerSemantics"
    ],
    "relatedConcept": [
      "urn:csabs:concept/AbstractInterpretation",
      "urn:csabs:concept/LoopIterationMapping"
    ],
    "hasOperation": [
      "urn:csabs:operation/ScalarRecurrence-evaluate",
      "urn:csabs:operation/ScalarRecurrence-trip-fact"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/ScalarRecurrence-affine-definition",
      "urn:csabs:axiom/ScalarRecurrence-count-scope"
    ],
    "hasLaw": [
      "urn:csabs:law/ScalarRecurrence-zero-stride"
    ],
    "hasTheorem": [],
    "basisKind": "relational-structural-definition",
    "basisScope": "The selected Lean recurrence is exact affine integer arithmetic. LLVM SCEV is richer and may describe modular fixed-width recurrences; lifting to exact integers needs scope-valid nowrap/range premises. SCEV flags have analysis scopes and are not copied blindly as instruction flags. Multiple exits and zero-trip guards affect counts. getSmallConstantTripCount returning 0 denotes unknown/nonconstant, not a proof of zero executions. Mathematical trip=backedges+1 needs the appropriate entered-loop/exit hypothesis and representable count width.",
    "axiomBasis": "a(0)=a₀ ∧ ∀n∈ℕ,a(n+1)=a(n)+d.; Count facts and nowrap facts are valid only in their stated loop/exit/input scope; unknown count is not exact zero.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.",
    "verificationObligation": [
      "Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.",
      "No SCEV DAG, higher-order recurrence, exit solver, range/nowrap analysis, count sentinel adapter or correspondence to LLVM instructions."
    ],
    "source": [
      "urn:csabs:source/compiler-scev",
      "urn:csabs:source/compiler-loops"
    ],
    "sourceLocator": "ScalarEvolution.h: SCEV NoWrapFlags, AddRec scope, getTripCountFromExitCount, getSmallConstantTripCount; LoopTerminology: trip count",
    "sourceNote": "Adapted Scoped induction recurrence and trip-count facts from ScalarEvolution.h: SCEV NoWrapFlags, AddRec scope, getTripCountFromExitCount, getSmallConstantTripCount; LoopTerminology: trip count. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "mathematicalFormulation": "A recurrence interpretation for induction variables with explicit arithmetic width, loop scope, exit assumptions and unknown results, usable to justify strength reduction and iteration guards. a(0)=a₀; a(n+1)=a(n)+d; exact profile a(n)=a₀+n·d The selected Lean recurrence is exact affine integer arithmetic. LLVM SCEV is richer and may describe modular fixed-width recurrences; lifting to exact integers needs scope-valid nowrap/range premises. SCEV flags have analysis scopes and are not copied blindly as instruction flags. Multiple exits and zero-trip guards affect counts. getSmallConstantTripCount returning 0 denotes unknown/nonconstant, not a proof of zero executions. Mathematical trip=backedges+1 needs the appropriate entered-loop/exit hypothesis and representable count width.",
    "leanFormulation": "structure ScalarRecurrence where\n  start : Int\n  stride : Int",
    "formulationSource": "urn:csabs:source/compiler-llvm-lean",
    "formulationLocator": "Catalog.LLVM.ScalarRecurrence",
    "formulationScope": "partial",
    "leanModelMapping": "Exact Int start/stride record and recurrenceValue definition; no fixed-width lifting is implicit.",
    "leanModelLimitations": "No SCEV DAG, higher-order recurrence, exit solver, range/nowrap analysis, count sentinel adapter or correspondence to LLVM instructions."
  },
  {
    "id": "urn:csabs:operation/ScalarRecurrence-evaluate",
    "type": "Operation",
    "name": "evaluate",
    "signature": "evaluate : Recurrence×ℕ→ℤ",
    "description": "Evaluate the exact affine recurrence a₀+n·d.",
    "concept": "urn:csabs:concept/ScalarRecurrence",
    "precondition": "Exact-integer profile or justified no-wrap lifting.",
    "postcondition": "Evaluate the exact affine recurrence a₀+n·d.",
    "totality": "Total mathematical function.",
    "source": [
      "urn:csabs:source/compiler-scev",
      "urn:csabs:source/compiler-loops"
    ],
    "sourceLocator": "ScalarEvolution.h: SCEV NoWrapFlags, AddRec scope, getTripCountFromExitCount, getSmallConstantTripCount; LoopTerminology: trip count",
    "sourceNote": "Adapted Scoped induction recurrence and trip-count facts from ScalarEvolution.h: SCEV NoWrapFlags, AddRec scope, getTripCountFromExitCount, getSmallConstantTripCount; LoopTerminology: trip count. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/ScalarRecurrence-trip-fact",
    "type": "Operation",
    "name": "trip-fact",
    "signature": "tripFact : Loop×Exit→Option CountFact",
    "description": "Return a scoped exact/bounded count or unknown.",
    "concept": "urn:csabs:concept/ScalarRecurrence",
    "precondition": "Exit feasibility, arithmetic and invariants established.",
    "postcondition": "Return a scoped exact/bounded count or unknown.",
    "totality": "Partial information; unknown is distinct from exact zero.",
    "source": [
      "urn:csabs:source/compiler-scev",
      "urn:csabs:source/compiler-loops"
    ],
    "sourceLocator": "ScalarEvolution.h: SCEV NoWrapFlags, AddRec scope, getTripCountFromExitCount, getSmallConstantTripCount; LoopTerminology: trip count",
    "sourceNote": "Adapted Scoped induction recurrence and trip-count facts from ScalarEvolution.h: SCEV NoWrapFlags, AddRec scope, getTripCountFromExitCount, getSmallConstantTripCount; LoopTerminology: trip count. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/ScalarRecurrence-affine-definition",
    "type": "Axiom",
    "name": "affine-definition",
    "description": "Defining obligation for Scoped induction recurrence and trip-count facts",
    "statement": "a(0)=a₀ ∧ ∀n∈ℕ,a(n+1)=a(n)+d.",
    "formalStatement": "a(0)=a₀ ∧ ∀n∈ℕ,a(n+1)=a(n)+d.",
    "assumptions": [
      "The selected Lean recurrence is exact affine integer arithmetic. LLVM SCEV is richer and may describe modular fixed-width recurrences; lifting to exact integers needs scope-valid nowrap/range premises. SCEV flags have analysis scopes and are not copied blindly as instruction flags. Multiple exits and zero-trip guards affect counts. getSmallConstantTripCount returning 0 denotes unknown/nonconstant, not a proof of zero executions. Mathematical trip=backedges+1 needs the appropriate entered-loop/exit hypothesis and representable count width."
    ],
    "appliesTo": [
      "urn:csabs:concept/ScalarRecurrence"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-scev",
      "urn:csabs:source/compiler-loops"
    ],
    "sourceLocator": "ScalarEvolution.h: SCEV NoWrapFlags, AddRec scope, getTripCountFromExitCount, getSmallConstantTripCount; LoopTerminology: trip count",
    "sourceNote": "Adapted Scoped induction recurrence and trip-count facts from ScalarEvolution.h: SCEV NoWrapFlags, AddRec scope, getTripCountFromExitCount, getSmallConstantTripCount; LoopTerminology: trip count. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:axiom/ScalarRecurrence-count-scope",
    "type": "Axiom",
    "name": "count-scope",
    "description": "Defining obligation for Scoped induction recurrence and trip-count facts",
    "statement": "Count facts and nowrap facts are valid only in their stated loop/exit/input scope; unknown count is not exact zero.",
    "formalStatement": "Count facts and nowrap facts are valid only in their stated loop/exit/input scope; unknown count is not exact zero.",
    "assumptions": [
      "The selected Lean recurrence is exact affine integer arithmetic. LLVM SCEV is richer and may describe modular fixed-width recurrences; lifting to exact integers needs scope-valid nowrap/range premises. SCEV flags have analysis scopes and are not copied blindly as instruction flags. Multiple exits and zero-trip guards affect counts. getSmallConstantTripCount returning 0 denotes unknown/nonconstant, not a proof of zero executions. Mathematical trip=backedges+1 needs the appropriate entered-loop/exit hypothesis and representable count width."
    ],
    "appliesTo": [
      "urn:csabs:concept/ScalarRecurrence"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-scev",
      "urn:csabs:source/compiler-loops"
    ],
    "sourceLocator": "ScalarEvolution.h: SCEV NoWrapFlags, AddRec scope, getTripCountFromExitCount, getSmallConstantTripCount; LoopTerminology: trip count",
    "sourceNote": "Adapted Scoped induction recurrence and trip-count facts from ScalarEvolution.h: SCEV NoWrapFlags, AddRec scope, getTripCountFromExitCount, getSmallConstantTripCount; LoopTerminology: trip count. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:law/ScalarRecurrence-zero-stride",
    "type": "Law",
    "name": "zero-stride",
    "description": "Derived consequence in the stated profile.",
    "statement": "For the exact affine profile, d=0 ⇒ ∀n,a(n)=a₀.",
    "formalStatement": "For the exact affine profile, d=0 ⇒ ∀n,a(n)=a₀.",
    "assumptions": [
      "The selected Lean recurrence is exact affine integer arithmetic. LLVM SCEV is richer and may describe modular fixed-width recurrences; lifting to exact integers needs scope-valid nowrap/range premises. SCEV flags have analysis scopes and are not copied blindly as instruction flags. Multiple exits and zero-trip guards affect counts. getSmallConstantTripCount returning 0 denotes unknown/nonconstant, not a proof of zero executions. Mathematical trip=backedges+1 needs the appropriate entered-loop/exit hypothesis and representable count width."
    ],
    "appliesTo": [
      "urn:csabs:concept/ScalarRecurrence"
    ],
    "dependsOn": [
      "urn:csabs:axiom/ScalarRecurrence-affine-definition"
    ],
    "proofSketch": "Induct on n. The base is a(0)=a₀; the step adds zero.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-scev",
      "urn:csabs:source/compiler-loops"
    ],
    "sourceLocator": "ScalarEvolution.h: SCEV NoWrapFlags, AddRec scope, getTripCountFromExitCount, getSmallConstantTripCount; LoopTerminology: trip count",
    "sourceNote": "Catalog derivation from the explicit dependsOn premises; the cited source motivates the interface, not this exact editorial theorem name.",
    "provenanceKind": "derived",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  }
]
```
<!-- graph-record:end -->
