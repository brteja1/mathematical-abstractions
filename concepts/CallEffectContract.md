# Call-boundary behavior and effect contract

A relational contract for calls including argument/state preconditions, possible outcomes, effects and calling-convention obligations, with independent termination and unwind guarantees.

**Notation:** Pre(args,σ) ∧ Call(args,σ,out,σ′) ⇒ AllowedEffect(σ,σ′) ∧ Post(args,out,σ′)

**Stable ID:** `urn:csabs:concept/CallEffectContract`

**Categories:** Programming-language semantics → Compiler transformations

**Kind:** semantic-model

**Prerequisites:** [Relational method contract with write effects](MethodContract.md), [Conservative resource effect summary](EffectSummary.md)

**Related concepts:** [Normal, exceptional and nonlocal control outcomes](ExceptionalControlFlow.md), [Scoped LLVM attribute, flag and metadata contract](LLVMAttributeContract.md), [Environment-indexed symbol resolution and reachability](SymbolLinkage.md), [Control-sensitive communicating thread instances](ConvergentExecution.md)

## Backlinks

- [Control-sensitive communicating thread instances](ConvergentExecution.md) — `relatedConcept`
- [Typed IR legalization with representation relation](DialectConversion.md) — `relatedConcept`
- [Program side-effect algebra (total sequential effect-quantale profile)](EffectAlgebra.md) — `relatedConcept`
- [Conservative resource effect summary](EffectSummary.md) — `relatedConcept`
- [Normal, exceptional and nonlocal control outcomes](ExceptionalControlFlow.md) — `relatedConcept`
- [Scoped LLVM attribute, flag and metadata contract](LLVMAttributeContract.md) — `requiresConcept`
- [Instrumented trace projection and runtime contract](RuntimeInstrumentation.md) — `requiresConcept`
- [Environment-indexed symbol resolution and reachability](SymbolLinkage.md) — `requiresConcept`

## Mathematical formulation

A relational contract for calls including argument/state preconditions, possible outcomes, effects and calling-convention obligations, with independent termination and unwind guarantees. Pre(args,σ) ∧ Call(args,σ,out,σ′) ⇒ AllowedEffect(σ,σ′) ∧ Post(args,out,σ′) Callee identity can depend on linkage/dynamic dispatch. Input/output representation includes ABI attributes, varargs, byval/sret and alignment where applicable. memory(none)/readonly does not imply nounwind, termination, determinism or safe duplication. unknown calls and unknown operand bundles have conservative effects. Inlining preserves normal, exceptional and deoptimization continuations plus fresh stack/local identities; tail/musttail and recursion have separate conditions. Libcall simplification also needs target-library behavior, errno/FP effects and interposition assumptions.

**Lean formulation** (in its source module context):

```lean
structure CallEffectContract (Input Output State : Type u) where
  precondition : Input → State → Prop
  outcome : Input → State → Output → State → Prop
  allowedEffect : State → State → Prop
  effectSound : ∀ i s o t, precondition i s → outcome i s o t → allowedEffect s t
```

**Source:** [`Catalog.LLVM.CallEffectContract`](../lean/Catalog/LLVMTransforms.lean); consulted 2026-11-16.

**Scope:** partial

**Interpretation:** Precondition, full outcome relation and allowed-effect relation with effectSound.

**Limits:** No evaluator, ABI, stack, determinism, termination, exception, bundle or external-library model. Outcome types must explicitly include all relevant behaviors.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** For admitted inputs, each call outcome satisfies the declared postcondition and allowed-effect relation.; A memory-effect restriction alone does not entail return, nounwind, deterministic results, speculatability or duplicability.

**basisKind:** relational-structural-definition

**basisScope:** Callee identity can depend on linkage/dynamic dispatch. Input/output representation includes ABI attributes, varargs, byval/sret and alignment where applicable. memory(none)/readonly does not imply nounwind, termination, determinism or safe duplication. unknown calls and unknown operand bundles have conservative effects. Inlining preserves normal, exceptional and deoptimization continuations plus fresh stack/local identities; tail/musttail and recursion have separate conditions. Libcall simplification also needs target-library behavior, errno/FP effects and interposition assumptions.

**verificationObligation:** Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.; No evaluator, ABI, stack, determinism, termination, exception, bundle or external-library model. Outcome types must explicitly include all relevant behaviors.

**reviewStatus:** Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-CallEffectContract-invoke"></a>

### invoke

`urn:csabs:operation/CallEffectContract-invoke`

**signature:** invoke : Callee×Args×State→P(Outcome×State)

**description:** Relate admitted inputs to all allowed returns/unwinds/divergence and memory effects.

**precondition:** ABI/callsite attributes and operand bundles honored.

**postcondition:** Relate admitted inputs to all allowed returns/unwinds/divergence and memory effects.

**totality:** Potentially nondeterministic and nonterminating.

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM Pass Reference (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Passes.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Passes.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** LangRef: Calling Conventions, Parameter Attributes, Function Attributes, call/invoke, Operand Bundles; Passes: inline, argpromotion, tailcallelim

**sourceNote:** Adapted Call-boundary behavior and effect contract from LangRef: Calling Conventions, Parameter Attributes, Function Attributes, call/invoke, Operand Bundles; Passes: inline, argpromotion, tailcallelim. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-CallEffectContract-substitute-body"></a>

### substitute-body

`urn:csabs:operation/CallEffectContract-substitute-body`

**signature:** substituteBody : CallSite×Body⇀IR

**description:** Instantiate a body preserving call-boundary observations and continuations.

**precondition:** Binding, stack identity, ABI, linkage and attributes justified.

**postcondition:** Instantiate a body preserving call-boundary observations and continuations.

**totality:** Partial transformation.

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM Pass Reference (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Passes.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Passes.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** LangRef: Calling Conventions, Parameter Attributes, Function Attributes, call/invoke, Operand Bundles; Passes: inline, argpromotion, tailcallelim

**sourceNote:** Adapted Call-boundary behavior and effect contract from LangRef: Calling Conventions, Parameter Attributes, Function Attributes, call/invoke, Operand Bundles; Passes: inline, argpromotion, tailcallelim. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-CallEffectContract-effect-postcondition"></a>

### effect-postcondition

`urn:csabs:axiom/CallEffectContract-effect-postcondition`

**description:** Defining obligation for Call-boundary behavior and effect contract

**statement:** For admitted inputs, each call outcome satisfies the declared postcondition and allowed-effect relation.

**formalStatement:** For admitted inputs, each call outcome satisfies the declared postcondition and allowed-effect relation.

**assumptions:** Callee identity can depend on linkage/dynamic dispatch. Input/output representation includes ABI attributes, varargs, byval/sret and alignment where applicable. memory(none)/readonly does not imply nounwind, termination, determinism or safe duplication. unknown calls and unknown operand bundles have conservative effects. Inlining preserves normal, exceptional and deoptimization continuations plus fresh stack/local identities; tail/musttail and recursion have separate conditions. Libcall simplification also needs target-library behavior, errno/FP effects and interposition assumptions.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM Pass Reference (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Passes.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Passes.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** LangRef: Calling Conventions, Parameter Attributes, Function Attributes, call/invoke, Operand Bundles; Passes: inline, argpromotion, tailcallelim

**sourceNote:** Adapted Call-boundary behavior and effect contract from LangRef: Calling Conventions, Parameter Attributes, Function Attributes, call/invoke, Operand Bundles; Passes: inline, argpromotion, tailcallelim. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

<a id="node-urn-csabs-axiom-CallEffectContract-independent-guarantees"></a>

### independent-guarantees

`urn:csabs:axiom/CallEffectContract-independent-guarantees`

**description:** Defining obligation for Call-boundary behavior and effect contract

**statement:** A memory-effect restriction alone does not entail return, nounwind, deterministic results, speculatability or duplicability.

**formalStatement:** A memory-effect restriction alone does not entail return, nounwind, deterministic results, speculatability or duplicability.

**assumptions:** Callee identity can depend on linkage/dynamic dispatch. Input/output representation includes ABI attributes, varargs, byval/sret and alignment where applicable. memory(none)/readonly does not imply nounwind, termination, determinism or safe duplication. unknown calls and unknown operand bundles have conservative effects. Inlining preserves normal, exceptional and deoptimization continuations plus fresh stack/local identities; tail/musttail and recursion have separate conditions. Libcall simplification also needs target-library behavior, errno/FP effects and interposition assumptions.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM Pass Reference (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Passes.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Passes.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** LangRef: Calling Conventions, Parameter Attributes, Function Attributes, call/invoke, Operand Bundles; Passes: inline, argpromotion, tailcallelim

**sourceNote:** Adapted Call-boundary behavior and effect contract from LangRef: Calling Conventions, Parameter Attributes, Function Attributes, call/invoke, Operand Bundles; Passes: inline, argpromotion, tailcallelim. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

## Laws

<a id="node-urn-csabs-law-CallEffectContract-readnone-not-removable"></a>

### readnone-not-removable

`urn:csabs:law/CallEffectContract-readnone-not-removable`

**description:** Derived consequence in the stated profile.

**statement:** A memory(none) fact alone cannot justify deleting an otherwise observable or nonterminating call.

**formalStatement:** A memory(none) fact alone cannot justify deleting an otherwise observable or nonterminating call.

**assumptions:** Callee identity can depend on linkage/dynamic dispatch. Input/output representation includes ABI attributes, varargs, byval/sret and alignment where applicable. memory(none)/readonly does not imply nounwind, termination, determinism or safe duplication. unknown calls and unknown operand bundles have conservative effects. Inlining preserves normal, exceptional and deoptimization continuations plus fresh stack/local identities; tail/musttail and recursion have separate conditions. Libcall simplification also needs target-library behavior, errno/FP effects and interposition assumptions.

**dependsOn:** [independent-guarantees](CallEffectContract.md#node-urn-csabs-axiom-CallEffectContract-independent-guarantees)

**proofSketch:** Deletion requires termination/control/result obligations that the memory-effect premise does not provide.

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM Pass Reference (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Passes.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Passes.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** LangRef: Calling Conventions, Parameter Attributes, Function Attributes, call/invoke, Operand Bundles; Passes: inline, argpromotion, tailcallelim

**sourceNote:** Catalog derivation from the explicit dependsOn premises; the cited source motivates the interface, not this exact editorial theorem name.

**provenanceKind:** derived

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification
- [LLVM Pass Reference (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Passes.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Passes.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** LangRef: Calling Conventions, Parameter Attributes, Function Attributes, call/invoke, Operand Bundles; Passes: inline, argpromotion, tailcallelim

**sourceNote:** Adapted Call-boundary behavior and effect contract from LangRef: Calling Conventions, Parameter Attributes, Function Attributes, call/invoke, Operand Bundles; Passes: inline, argpromotion, tailcallelim. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/CallEffectContract",
    "type": "Concept",
    "shortForm": "CallEffectContract",
    "fullName": "Call-boundary behavior and effect contract",
    "definition": "A relational contract for calls including argument/state preconditions, possible outcomes, effects and calling-convention obligations, with independent termination and unwind guarantees.",
    "notation": "Pre(args,σ) ∧ Call(args,σ,out,σ′) ⇒ AllowedEffect(σ,σ′) ∧ Post(args,out,σ′)",
    "category": [
      "urn:csabs:category/compiler-transformations"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "requiresConcept": [
      "urn:csabs:concept/MethodContract",
      "urn:csabs:concept/EffectSummary"
    ],
    "relatedConcept": [
      "urn:csabs:concept/ExceptionalControlFlow",
      "urn:csabs:concept/LLVMAttributeContract",
      "urn:csabs:concept/SymbolLinkage",
      "urn:csabs:concept/ConvergentExecution"
    ],
    "hasOperation": [
      "urn:csabs:operation/CallEffectContract-invoke",
      "urn:csabs:operation/CallEffectContract-substitute-body"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/CallEffectContract-effect-postcondition",
      "urn:csabs:axiom/CallEffectContract-independent-guarantees"
    ],
    "hasLaw": [
      "urn:csabs:law/CallEffectContract-readnone-not-removable"
    ],
    "hasTheorem": [],
    "basisKind": "relational-structural-definition",
    "basisScope": "Callee identity can depend on linkage/dynamic dispatch. Input/output representation includes ABI attributes, varargs, byval/sret and alignment where applicable. memory(none)/readonly does not imply nounwind, termination, determinism or safe duplication. unknown calls and unknown operand bundles have conservative effects. Inlining preserves normal, exceptional and deoptimization continuations plus fresh stack/local identities; tail/musttail and recursion have separate conditions. Libcall simplification also needs target-library behavior, errno/FP effects and interposition assumptions.",
    "axiomBasis": "For admitted inputs, each call outcome satisfies the declared postcondition and allowed-effect relation.; A memory-effect restriction alone does not entail return, nounwind, deterministic results, speculatability or duplicability.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.",
    "verificationObligation": [
      "Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.",
      "No evaluator, ABI, stack, determinism, termination, exception, bundle or external-library model. Outcome types must explicitly include all relevant behaviors."
    ],
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-pass-reference"
    ],
    "sourceLocator": "LangRef: Calling Conventions, Parameter Attributes, Function Attributes, call/invoke, Operand Bundles; Passes: inline, argpromotion, tailcallelim",
    "sourceNote": "Adapted Call-boundary behavior and effect contract from LangRef: Calling Conventions, Parameter Attributes, Function Attributes, call/invoke, Operand Bundles; Passes: inline, argpromotion, tailcallelim. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "mathematicalFormulation": "A relational contract for calls including argument/state preconditions, possible outcomes, effects and calling-convention obligations, with independent termination and unwind guarantees. Pre(args,σ) ∧ Call(args,σ,out,σ′) ⇒ AllowedEffect(σ,σ′) ∧ Post(args,out,σ′) Callee identity can depend on linkage/dynamic dispatch. Input/output representation includes ABI attributes, varargs, byval/sret and alignment where applicable. memory(none)/readonly does not imply nounwind, termination, determinism or safe duplication. unknown calls and unknown operand bundles have conservative effects. Inlining preserves normal, exceptional and deoptimization continuations plus fresh stack/local identities; tail/musttail and recursion have separate conditions. Libcall simplification also needs target-library behavior, errno/FP effects and interposition assumptions.",
    "leanFormulation": "structure CallEffectContract (Input Output State : Type u) where\n  precondition : Input → State → Prop\n  outcome : Input → State → Output → State → Prop\n  allowedEffect : State → State → Prop\n  effectSound : ∀ i s o t, precondition i s → outcome i s o t → allowedEffect s t",
    "formulationSource": "urn:csabs:source/compiler-llvm-lean",
    "formulationLocator": "Catalog.LLVM.CallEffectContract",
    "formulationScope": "partial",
    "leanModelMapping": "Precondition, full outcome relation and allowed-effect relation with effectSound.",
    "leanModelLimitations": "No evaluator, ABI, stack, determinism, termination, exception, bundle or external-library model. Outcome types must explicitly include all relevant behaviors."
  },
  {
    "id": "urn:csabs:operation/CallEffectContract-invoke",
    "type": "Operation",
    "name": "invoke",
    "signature": "invoke : Callee×Args×State→P(Outcome×State)",
    "description": "Relate admitted inputs to all allowed returns/unwinds/divergence and memory effects.",
    "concept": "urn:csabs:concept/CallEffectContract",
    "precondition": "ABI/callsite attributes and operand bundles honored.",
    "postcondition": "Relate admitted inputs to all allowed returns/unwinds/divergence and memory effects.",
    "totality": "Potentially nondeterministic and nonterminating.",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-pass-reference"
    ],
    "sourceLocator": "LangRef: Calling Conventions, Parameter Attributes, Function Attributes, call/invoke, Operand Bundles; Passes: inline, argpromotion, tailcallelim",
    "sourceNote": "Adapted Call-boundary behavior and effect contract from LangRef: Calling Conventions, Parameter Attributes, Function Attributes, call/invoke, Operand Bundles; Passes: inline, argpromotion, tailcallelim. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/CallEffectContract-substitute-body",
    "type": "Operation",
    "name": "substitute-body",
    "signature": "substituteBody : CallSite×Body⇀IR",
    "description": "Instantiate a body preserving call-boundary observations and continuations.",
    "concept": "urn:csabs:concept/CallEffectContract",
    "precondition": "Binding, stack identity, ABI, linkage and attributes justified.",
    "postcondition": "Instantiate a body preserving call-boundary observations and continuations.",
    "totality": "Partial transformation.",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-pass-reference"
    ],
    "sourceLocator": "LangRef: Calling Conventions, Parameter Attributes, Function Attributes, call/invoke, Operand Bundles; Passes: inline, argpromotion, tailcallelim",
    "sourceNote": "Adapted Call-boundary behavior and effect contract from LangRef: Calling Conventions, Parameter Attributes, Function Attributes, call/invoke, Operand Bundles; Passes: inline, argpromotion, tailcallelim. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/CallEffectContract-effect-postcondition",
    "type": "Axiom",
    "name": "effect-postcondition",
    "description": "Defining obligation for Call-boundary behavior and effect contract",
    "statement": "For admitted inputs, each call outcome satisfies the declared postcondition and allowed-effect relation.",
    "formalStatement": "For admitted inputs, each call outcome satisfies the declared postcondition and allowed-effect relation.",
    "assumptions": [
      "Callee identity can depend on linkage/dynamic dispatch. Input/output representation includes ABI attributes, varargs, byval/sret and alignment where applicable. memory(none)/readonly does not imply nounwind, termination, determinism or safe duplication. unknown calls and unknown operand bundles have conservative effects. Inlining preserves normal, exceptional and deoptimization continuations plus fresh stack/local identities; tail/musttail and recursion have separate conditions. Libcall simplification also needs target-library behavior, errno/FP effects and interposition assumptions."
    ],
    "appliesTo": [
      "urn:csabs:concept/CallEffectContract"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-pass-reference"
    ],
    "sourceLocator": "LangRef: Calling Conventions, Parameter Attributes, Function Attributes, call/invoke, Operand Bundles; Passes: inline, argpromotion, tailcallelim",
    "sourceNote": "Adapted Call-boundary behavior and effect contract from LangRef: Calling Conventions, Parameter Attributes, Function Attributes, call/invoke, Operand Bundles; Passes: inline, argpromotion, tailcallelim. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:axiom/CallEffectContract-independent-guarantees",
    "type": "Axiom",
    "name": "independent-guarantees",
    "description": "Defining obligation for Call-boundary behavior and effect contract",
    "statement": "A memory-effect restriction alone does not entail return, nounwind, deterministic results, speculatability or duplicability.",
    "formalStatement": "A memory-effect restriction alone does not entail return, nounwind, deterministic results, speculatability or duplicability.",
    "assumptions": [
      "Callee identity can depend on linkage/dynamic dispatch. Input/output representation includes ABI attributes, varargs, byval/sret and alignment where applicable. memory(none)/readonly does not imply nounwind, termination, determinism or safe duplication. unknown calls and unknown operand bundles have conservative effects. Inlining preserves normal, exceptional and deoptimization continuations plus fresh stack/local identities; tail/musttail and recursion have separate conditions. Libcall simplification also needs target-library behavior, errno/FP effects and interposition assumptions."
    ],
    "appliesTo": [
      "urn:csabs:concept/CallEffectContract"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-pass-reference"
    ],
    "sourceLocator": "LangRef: Calling Conventions, Parameter Attributes, Function Attributes, call/invoke, Operand Bundles; Passes: inline, argpromotion, tailcallelim",
    "sourceNote": "Adapted Call-boundary behavior and effect contract from LangRef: Calling Conventions, Parameter Attributes, Function Attributes, call/invoke, Operand Bundles; Passes: inline, argpromotion, tailcallelim. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:law/CallEffectContract-readnone-not-removable",
    "type": "Law",
    "name": "readnone-not-removable",
    "description": "Derived consequence in the stated profile.",
    "statement": "A memory(none) fact alone cannot justify deleting an otherwise observable or nonterminating call.",
    "formalStatement": "A memory(none) fact alone cannot justify deleting an otherwise observable or nonterminating call.",
    "assumptions": [
      "Callee identity can depend on linkage/dynamic dispatch. Input/output representation includes ABI attributes, varargs, byval/sret and alignment where applicable. memory(none)/readonly does not imply nounwind, termination, determinism or safe duplication. unknown calls and unknown operand bundles have conservative effects. Inlining preserves normal, exceptional and deoptimization continuations plus fresh stack/local identities; tail/musttail and recursion have separate conditions. Libcall simplification also needs target-library behavior, errno/FP effects and interposition assumptions."
    ],
    "appliesTo": [
      "urn:csabs:concept/CallEffectContract"
    ],
    "dependsOn": [
      "urn:csabs:axiom/CallEffectContract-independent-guarantees"
    ],
    "proofSketch": "Deletion requires termination/control/result obligations that the memory-effect premise does not provide.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-pass-reference"
    ],
    "sourceLocator": "LangRef: Calling Conventions, Parameter Attributes, Function Attributes, call/invoke, Operand Bundles; Passes: inline, argpromotion, tailcallelim",
    "sourceNote": "Catalog derivation from the explicit dependsOn premises; the cited source motivates the interface, not this exact editorial theorem name.",
    "provenanceKind": "derived",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  }
]
```
<!-- graph-record:end -->
