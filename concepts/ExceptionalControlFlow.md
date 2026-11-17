# Normal, exceptional and nonlocal control outcomes

An outcome algebra separating return, unwind, divergence and UB, with handlers/cleanups and nonlocal continuations preserved by transformations under an explicit exception personality.

**Notation:** Outcome=Return(Value)+Unwind(Exception)+Diverge+UB; invoke has normal and unwind continuations

**Stable ID:** `urn:csabs:concept/ExceptionalControlFlow`

**Categories:** Programming-language semantics → Compiler transformations

**Kind:** semantic-model

**Prerequisites:** [Sum Type](SumType.md), [CFG refinement with path correspondence and progress](ControlFlowRefinement.md)

**Related concepts:** [Call-boundary behavior and effect contract](CallEffectContract.md), [Instrumented trace projection and runtime contract](RuntimeInstrumentation.md)

## Backlinks

- [Call-boundary behavior and effect contract](CallEffectContract.md) — `relatedConcept`
- [Control-flow graph (single entry, single exit)](ControlFlowGraph.md) — `relatedConcept`
- [CFG refinement with path correspondence and progress](ControlFlowRefinement.md) — `relatedConcept`
- [Instrumented trace projection and runtime contract](RuntimeInstrumentation.md) — `relatedConcept`

## Mathematical formulation

An outcome algebra separating return, unwind, divergence and UB, with handlers/cleanups and nonlocal continuations preserved by transformations under an explicit exception personality. Outcome=Return(Value)+Unwind(Exception)+Diverge+UB; invoke has normal and unwind continuations Exception payloads, personality, handler selection and cleanup effects are observable as specified by the selected ABI. Itanium landingpads and Windows funclets are distinct profiles. nounwind is a semantic guarantee, not implied by memory-effect freedom. Replacing invoke by call or dropping unwind paths needs justified no-unwind behavior or an explicit unwindless contract change. setjmp/longjmp, callbr and deoptimization may use nonlocal continuations and are not modeled by ordinary Return alone. UB differs from unwinding and must not be caught as an exception.

**Lean formulation** (in its source module context):

```lean
inductive ExceptionalControlFlow (Value Exception : Type u) where
  | returned : Value → ExceptionalControlFlow Value Exception
  | unwound : Exception → ExceptionalControlFlow Value Exception
  | diverged : ExceptionalControlFlow Value Exception
  | immediateUB : ExceptionalControlFlow Value Exception
```

**Source:** [`Catalog.LLVM.ExceptionalControlFlow`](../lean/Catalog/LLVMTransforms.lean); consulted 2026-11-16.

**Scope:** partial

**Interpretation:** Tagged returned/unwound/diverged/immediateUB outcome carrier.

**Limits:** No personality evaluator, landingpad/funclet machine, cleanup stack, setjmp/longjmp or deoptimization implementation; only the outcome distinction is encoded.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Return, Unwind, Diverge and UB are distinct outcomes; no transform may equate them without the stated observational contract.; An invoke rewrite must preserve its normal and exceptional continuations and required cleanups unless no-unwind is proved or a different contract is explicitly selected.

**basisKind:** relational-structural-definition

**basisScope:** Exception payloads, personality, handler selection and cleanup effects are observable as specified by the selected ABI. Itanium landingpads and Windows funclets are distinct profiles. nounwind is a semantic guarantee, not implied by memory-effect freedom. Replacing invoke by call or dropping unwind paths needs justified no-unwind behavior or an explicit unwindless contract change. setjmp/longjmp, callbr and deoptimization may use nonlocal continuations and are not modeled by ordinary Return alone. UB differs from unwinding and must not be caught as an exception.

**verificationObligation:** Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.; No personality evaluator, landingpad/funclet machine, cleanup stack, setjmp/longjmp or deoptimization implementation; only the outcome distinction is encoded.

**reviewStatus:** Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-ExceptionalControlFlow-dispatch"></a>

### dispatch

`urn:csabs:operation/ExceptionalControlFlow-dispatch`

**signature:** dispatch : Personality×Exception×HandlerStack→Continuation

**description:** Choose the specified handler/cleanup path.

**precondition:** Personality and ABI handler state valid.

**postcondition:** Choose the specified handler/cleanup path.

**totality:** Partial on unsupported personalities.

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM Exception Handling (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/ExceptionHandling.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/ExceptionHandling.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** LangRef: invoke, landingpad, resume, catchswitch/catchpad/cleanuppad/catchret/cleanupret, funclet bundles; ExceptionHandling: Itanium, SJLJ, Windows runtime

**sourceNote:** Adapted Normal, exceptional and nonlocal control outcomes from LangRef: invoke, landingpad, resume, catchswitch/catchpad/cleanuppad/catchret/cleanupret, funclet bundles; ExceptionHandling: Itanium, SJLJ, Windows runtime. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-ExceptionalControlFlow-propagate"></a>

### propagate

`urn:csabs:operation/ExceptionalControlFlow-propagate`

**signature:** propagate : Outcome×Continuations→Outcome

**description:** Compose return/unwind with their corresponding continuations and cleanup effects.

**precondition:** Continuations preserve payloads, bundles and nesting rules.

**postcondition:** Compose return/unwind with their corresponding continuations and cleanup effects.

**totality:** Divergence and UB remain distinct outcomes.

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM Exception Handling (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/ExceptionHandling.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/ExceptionHandling.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** LangRef: invoke, landingpad, resume, catchswitch/catchpad/cleanuppad/catchret/cleanupret, funclet bundles; ExceptionHandling: Itanium, SJLJ, Windows runtime

**sourceNote:** Adapted Normal, exceptional and nonlocal control outcomes from LangRef: invoke, landingpad, resume, catchswitch/catchpad/cleanuppad/catchret/cleanupret, funclet bundles; ExceptionHandling: Itanium, SJLJ, Windows runtime. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-ExceptionalControlFlow-outcome-distinction"></a>

### outcome-distinction

`urn:csabs:axiom/ExceptionalControlFlow-outcome-distinction`

**description:** Defining obligation for Normal, exceptional and nonlocal control outcomes

**statement:** Return, Unwind, Diverge and UB are distinct outcomes; no transform may equate them without the stated observational contract.

**formalStatement:** Return, Unwind, Diverge and UB are distinct outcomes; no transform may equate them without the stated observational contract.

**assumptions:** Exception payloads, personality, handler selection and cleanup effects are observable as specified by the selected ABI. Itanium landingpads and Windows funclets are distinct profiles. nounwind is a semantic guarantee, not implied by memory-effect freedom. Replacing invoke by call or dropping unwind paths needs justified no-unwind behavior or an explicit unwindless contract change. setjmp/longjmp, callbr and deoptimization may use nonlocal continuations and are not modeled by ordinary Return alone. UB differs from unwinding and must not be caught as an exception.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM Exception Handling (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/ExceptionHandling.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/ExceptionHandling.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** LangRef: invoke, landingpad, resume, catchswitch/catchpad/cleanuppad/catchret/cleanupret, funclet bundles; ExceptionHandling: Itanium, SJLJ, Windows runtime

**sourceNote:** Adapted Normal, exceptional and nonlocal control outcomes from LangRef: invoke, landingpad, resume, catchswitch/catchpad/cleanuppad/catchret/cleanupret, funclet bundles; ExceptionHandling: Itanium, SJLJ, Windows runtime. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

<a id="node-urn-csabs-axiom-ExceptionalControlFlow-unwind-preservation"></a>

### unwind-preservation

`urn:csabs:axiom/ExceptionalControlFlow-unwind-preservation`

**description:** Defining obligation for Normal, exceptional and nonlocal control outcomes

**statement:** An invoke rewrite must preserve its normal and exceptional continuations and required cleanups unless no-unwind is proved or a different contract is explicitly selected.

**formalStatement:** An invoke rewrite must preserve its normal and exceptional continuations and required cleanups unless no-unwind is proved or a different contract is explicitly selected.

**assumptions:** Exception payloads, personality, handler selection and cleanup effects are observable as specified by the selected ABI. Itanium landingpads and Windows funclets are distinct profiles. nounwind is a semantic guarantee, not implied by memory-effect freedom. Replacing invoke by call or dropping unwind paths needs justified no-unwind behavior or an explicit unwindless contract change. setjmp/longjmp, callbr and deoptimization may use nonlocal continuations and are not modeled by ordinary Return alone. UB differs from unwinding and must not be caught as an exception.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM Exception Handling (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/ExceptionHandling.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/ExceptionHandling.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** LangRef: invoke, landingpad, resume, catchswitch/catchpad/cleanuppad/catchret/cleanupret, funclet bundles; ExceptionHandling: Itanium, SJLJ, Windows runtime

**sourceNote:** Adapted Normal, exceptional and nonlocal control outcomes from LangRef: invoke, landingpad, resume, catchswitch/catchpad/cleanuppad/catchret/cleanupret, funclet bundles; ExceptionHandling: Itanium, SJLJ, Windows runtime. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

## Laws

<a id="node-urn-csabs-law-ExceptionalControlFlow-nounwind-insufficient-for-return"></a>

### nounwind-insufficient-for-return

`urn:csabs:law/ExceptionalControlFlow-nounwind-insufficient-for-return`

**description:** Derived consequence in the stated profile.

**statement:** Excluding Unwind does not exclude Diverge or establish a return value.

**formalStatement:** Excluding Unwind does not exclude Diverge or establish a return value.

**assumptions:** Exception payloads, personality, handler selection and cleanup effects are observable as specified by the selected ABI. Itanium landingpads and Windows funclets are distinct profiles. nounwind is a semantic guarantee, not implied by memory-effect freedom. Replacing invoke by call or dropping unwind paths needs justified no-unwind behavior or an explicit unwindless contract change. setjmp/longjmp, callbr and deoptimization may use nonlocal continuations and are not modeled by ordinary Return alone. UB differs from unwinding and must not be caught as an exception.

**dependsOn:** [outcome-distinction](ExceptionalControlFlow.md#node-urn-csabs-axiom-ExceptionalControlFlow-outcome-distinction)

**proofSketch:** The outcome algebra retains Diverge independently of Unwind, so removing one alternative does not remove the other.

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM Exception Handling (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/ExceptionHandling.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/ExceptionHandling.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** LangRef: invoke, landingpad, resume, catchswitch/catchpad/cleanuppad/catchret/cleanupret, funclet bundles; ExceptionHandling: Itanium, SJLJ, Windows runtime

**sourceNote:** Catalog derivation from the explicit dependsOn premises; the cited source motivates the interface, not this exact editorial theorem name.

**provenanceKind:** derived

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification
- [LLVM Exception Handling (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/ExceptionHandling.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/ExceptionHandling.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** LangRef: invoke, landingpad, resume, catchswitch/catchpad/cleanuppad/catchret/cleanupret, funclet bundles; ExceptionHandling: Itanium, SJLJ, Windows runtime

**sourceNote:** Adapted Normal, exceptional and nonlocal control outcomes from LangRef: invoke, landingpad, resume, catchswitch/catchpad/cleanuppad/catchret/cleanupret, funclet bundles; ExceptionHandling: Itanium, SJLJ, Windows runtime. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/ExceptionalControlFlow",
    "type": "Concept",
    "shortForm": "ExceptionalControlFlow",
    "fullName": "Normal, exceptional and nonlocal control outcomes",
    "definition": "An outcome algebra separating return, unwind, divergence and UB, with handlers/cleanups and nonlocal continuations preserved by transformations under an explicit exception personality.",
    "notation": "Outcome=Return(Value)+Unwind(Exception)+Diverge+UB; invoke has normal and unwind continuations",
    "category": [
      "urn:csabs:category/compiler-transformations"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "requiresConcept": [
      "urn:csabs:concept/SumType",
      "urn:csabs:concept/ControlFlowRefinement"
    ],
    "relatedConcept": [
      "urn:csabs:concept/CallEffectContract",
      "urn:csabs:concept/RuntimeInstrumentation"
    ],
    "hasOperation": [
      "urn:csabs:operation/ExceptionalControlFlow-dispatch",
      "urn:csabs:operation/ExceptionalControlFlow-propagate"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/ExceptionalControlFlow-outcome-distinction",
      "urn:csabs:axiom/ExceptionalControlFlow-unwind-preservation"
    ],
    "hasLaw": [
      "urn:csabs:law/ExceptionalControlFlow-nounwind-insufficient-for-return"
    ],
    "hasTheorem": [],
    "basisKind": "relational-structural-definition",
    "basisScope": "Exception payloads, personality, handler selection and cleanup effects are observable as specified by the selected ABI. Itanium landingpads and Windows funclets are distinct profiles. nounwind is a semantic guarantee, not implied by memory-effect freedom. Replacing invoke by call or dropping unwind paths needs justified no-unwind behavior or an explicit unwindless contract change. setjmp/longjmp, callbr and deoptimization may use nonlocal continuations and are not modeled by ordinary Return alone. UB differs from unwinding and must not be caught as an exception.",
    "axiomBasis": "Return, Unwind, Diverge and UB are distinct outcomes; no transform may equate them without the stated observational contract.; An invoke rewrite must preserve its normal and exceptional continuations and required cleanups unless no-unwind is proved or a different contract is explicitly selected.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.",
    "verificationObligation": [
      "Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.",
      "No personality evaluator, landingpad/funclet machine, cleanup stack, setjmp/longjmp or deoptimization implementation; only the outcome distinction is encoded."
    ],
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-eh"
    ],
    "sourceLocator": "LangRef: invoke, landingpad, resume, catchswitch/catchpad/cleanuppad/catchret/cleanupret, funclet bundles; ExceptionHandling: Itanium, SJLJ, Windows runtime",
    "sourceNote": "Adapted Normal, exceptional and nonlocal control outcomes from LangRef: invoke, landingpad, resume, catchswitch/catchpad/cleanuppad/catchret/cleanupret, funclet bundles; ExceptionHandling: Itanium, SJLJ, Windows runtime. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "mathematicalFormulation": "An outcome algebra separating return, unwind, divergence and UB, with handlers/cleanups and nonlocal continuations preserved by transformations under an explicit exception personality. Outcome=Return(Value)+Unwind(Exception)+Diverge+UB; invoke has normal and unwind continuations Exception payloads, personality, handler selection and cleanup effects are observable as specified by the selected ABI. Itanium landingpads and Windows funclets are distinct profiles. nounwind is a semantic guarantee, not implied by memory-effect freedom. Replacing invoke by call or dropping unwind paths needs justified no-unwind behavior or an explicit unwindless contract change. setjmp/longjmp, callbr and deoptimization may use nonlocal continuations and are not modeled by ordinary Return alone. UB differs from unwinding and must not be caught as an exception.",
    "leanFormulation": "inductive ExceptionalControlFlow (Value Exception : Type u) where\n  | returned : Value → ExceptionalControlFlow Value Exception\n  | unwound : Exception → ExceptionalControlFlow Value Exception\n  | diverged : ExceptionalControlFlow Value Exception\n  | immediateUB : ExceptionalControlFlow Value Exception",
    "formulationSource": "urn:csabs:source/compiler-llvm-lean",
    "formulationLocator": "Catalog.LLVM.ExceptionalControlFlow",
    "formulationScope": "partial",
    "leanModelMapping": "Tagged returned/unwound/diverged/immediateUB outcome carrier.",
    "leanModelLimitations": "No personality evaluator, landingpad/funclet machine, cleanup stack, setjmp/longjmp or deoptimization implementation; only the outcome distinction is encoded."
  },
  {
    "id": "urn:csabs:operation/ExceptionalControlFlow-dispatch",
    "type": "Operation",
    "name": "dispatch",
    "signature": "dispatch : Personality×Exception×HandlerStack→Continuation",
    "description": "Choose the specified handler/cleanup path.",
    "concept": "urn:csabs:concept/ExceptionalControlFlow",
    "precondition": "Personality and ABI handler state valid.",
    "postcondition": "Choose the specified handler/cleanup path.",
    "totality": "Partial on unsupported personalities.",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-eh"
    ],
    "sourceLocator": "LangRef: invoke, landingpad, resume, catchswitch/catchpad/cleanuppad/catchret/cleanupret, funclet bundles; ExceptionHandling: Itanium, SJLJ, Windows runtime",
    "sourceNote": "Adapted Normal, exceptional and nonlocal control outcomes from LangRef: invoke, landingpad, resume, catchswitch/catchpad/cleanuppad/catchret/cleanupret, funclet bundles; ExceptionHandling: Itanium, SJLJ, Windows runtime. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/ExceptionalControlFlow-propagate",
    "type": "Operation",
    "name": "propagate",
    "signature": "propagate : Outcome×Continuations→Outcome",
    "description": "Compose return/unwind with their corresponding continuations and cleanup effects.",
    "concept": "urn:csabs:concept/ExceptionalControlFlow",
    "precondition": "Continuations preserve payloads, bundles and nesting rules.",
    "postcondition": "Compose return/unwind with their corresponding continuations and cleanup effects.",
    "totality": "Divergence and UB remain distinct outcomes.",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-eh"
    ],
    "sourceLocator": "LangRef: invoke, landingpad, resume, catchswitch/catchpad/cleanuppad/catchret/cleanupret, funclet bundles; ExceptionHandling: Itanium, SJLJ, Windows runtime",
    "sourceNote": "Adapted Normal, exceptional and nonlocal control outcomes from LangRef: invoke, landingpad, resume, catchswitch/catchpad/cleanuppad/catchret/cleanupret, funclet bundles; ExceptionHandling: Itanium, SJLJ, Windows runtime. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/ExceptionalControlFlow-outcome-distinction",
    "type": "Axiom",
    "name": "outcome-distinction",
    "description": "Defining obligation for Normal, exceptional and nonlocal control outcomes",
    "statement": "Return, Unwind, Diverge and UB are distinct outcomes; no transform may equate them without the stated observational contract.",
    "formalStatement": "Return, Unwind, Diverge and UB are distinct outcomes; no transform may equate them without the stated observational contract.",
    "assumptions": [
      "Exception payloads, personality, handler selection and cleanup effects are observable as specified by the selected ABI. Itanium landingpads and Windows funclets are distinct profiles. nounwind is a semantic guarantee, not implied by memory-effect freedom. Replacing invoke by call or dropping unwind paths needs justified no-unwind behavior or an explicit unwindless contract change. setjmp/longjmp, callbr and deoptimization may use nonlocal continuations and are not modeled by ordinary Return alone. UB differs from unwinding and must not be caught as an exception."
    ],
    "appliesTo": [
      "urn:csabs:concept/ExceptionalControlFlow"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-eh"
    ],
    "sourceLocator": "LangRef: invoke, landingpad, resume, catchswitch/catchpad/cleanuppad/catchret/cleanupret, funclet bundles; ExceptionHandling: Itanium, SJLJ, Windows runtime",
    "sourceNote": "Adapted Normal, exceptional and nonlocal control outcomes from LangRef: invoke, landingpad, resume, catchswitch/catchpad/cleanuppad/catchret/cleanupret, funclet bundles; ExceptionHandling: Itanium, SJLJ, Windows runtime. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:axiom/ExceptionalControlFlow-unwind-preservation",
    "type": "Axiom",
    "name": "unwind-preservation",
    "description": "Defining obligation for Normal, exceptional and nonlocal control outcomes",
    "statement": "An invoke rewrite must preserve its normal and exceptional continuations and required cleanups unless no-unwind is proved or a different contract is explicitly selected.",
    "formalStatement": "An invoke rewrite must preserve its normal and exceptional continuations and required cleanups unless no-unwind is proved or a different contract is explicitly selected.",
    "assumptions": [
      "Exception payloads, personality, handler selection and cleanup effects are observable as specified by the selected ABI. Itanium landingpads and Windows funclets are distinct profiles. nounwind is a semantic guarantee, not implied by memory-effect freedom. Replacing invoke by call or dropping unwind paths needs justified no-unwind behavior or an explicit unwindless contract change. setjmp/longjmp, callbr and deoptimization may use nonlocal continuations and are not modeled by ordinary Return alone. UB differs from unwinding and must not be caught as an exception."
    ],
    "appliesTo": [
      "urn:csabs:concept/ExceptionalControlFlow"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-eh"
    ],
    "sourceLocator": "LangRef: invoke, landingpad, resume, catchswitch/catchpad/cleanuppad/catchret/cleanupret, funclet bundles; ExceptionHandling: Itanium, SJLJ, Windows runtime",
    "sourceNote": "Adapted Normal, exceptional and nonlocal control outcomes from LangRef: invoke, landingpad, resume, catchswitch/catchpad/cleanuppad/catchret/cleanupret, funclet bundles; ExceptionHandling: Itanium, SJLJ, Windows runtime. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:law/ExceptionalControlFlow-nounwind-insufficient-for-return",
    "type": "Law",
    "name": "nounwind-insufficient-for-return",
    "description": "Derived consequence in the stated profile.",
    "statement": "Excluding Unwind does not exclude Diverge or establish a return value.",
    "formalStatement": "Excluding Unwind does not exclude Diverge or establish a return value.",
    "assumptions": [
      "Exception payloads, personality, handler selection and cleanup effects are observable as specified by the selected ABI. Itanium landingpads and Windows funclets are distinct profiles. nounwind is a semantic guarantee, not implied by memory-effect freedom. Replacing invoke by call or dropping unwind paths needs justified no-unwind behavior or an explicit unwindless contract change. setjmp/longjmp, callbr and deoptimization may use nonlocal continuations and are not modeled by ordinary Return alone. UB differs from unwinding and must not be caught as an exception."
    ],
    "appliesTo": [
      "urn:csabs:concept/ExceptionalControlFlow"
    ],
    "dependsOn": [
      "urn:csabs:axiom/ExceptionalControlFlow-outcome-distinction"
    ],
    "proofSketch": "The outcome algebra retains Diverge independently of Unwind, so removing one alternative does not remove the other.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-eh"
    ],
    "sourceLocator": "LangRef: invoke, landingpad, resume, catchswitch/catchpad/cleanuppad/catchret/cleanupret, funclet bundles; ExceptionHandling: Itanium, SJLJ, Windows runtime",
    "sourceNote": "Catalog derivation from the explicit dependsOn premises; the cited source motivates the interface, not this exact editorial theorem name.",
    "provenanceKind": "derived",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  }
]
```
<!-- graph-record:end -->
