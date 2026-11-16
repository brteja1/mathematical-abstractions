# LLVM floating-point environment and rewrite permissions

A versioned floating-point contract retaining bit-level exceptional values, environment effects and per-instruction fast-math permissions independently of exact-real algebra.

**Notation:** eval(op,env,args)⊆Value×Env; rewrite permitted by exact flag/environment contract

**Stable ID:** `urn:csabs:concept/LLVMFloatingPointSemantics`

**Categories:** Programming-language semantics → Compiler transformations

**Kind:** semantic-model

**Prerequisites:** [Floating-point type](FloatingPointType.md), [LLVM scalar deferred undefinedness and freeze](LLVMPoisonSemantics.md)

**Related concepts:** [Guarded contextual program rewrite](GuardedRewrite.md), [Lane-indexed vector execution and inactive-lane policy](PredicatedVectorSemantics.md)

## Backlinks

- [Scoped LLVM attribute, flag and metadata contract](LLVMAttributeContract.md) — `relatedConcept`
- [LLVM scalar deferred undefinedness and freeze](LLVMPoisonSemantics.md) — `relatedConcept`
- [Lane-indexed vector execution and inactive-lane policy](PredicatedVectorSemantics.md) — `requiresConcept`

## Mathematical formulation

A versioned floating-point contract retaining bit-level exceptional values, environment effects and per-instruction fast-math permissions independently of exact-real algebra. eval(op,env,args)⊆Value×Env; rewrite permitted by exact flag/environment contract LLVM 21.1.8 default FP assumes round-to-nearest, disabled traps, unobservable status flags and specified denormal environment. Constrained intrinsics/strictfp require explicit rounding and exception modes. NaNs, infinities and signed zeros are represented; value equality must match permitted observations. nnan/ninf violations produce poison. nsz permits ignoring zero sign without asserting -0 is poison. contract permits suitable contraction but not arbitrary reassociation; reassoc is distinct. Rewrite-based permissions must cover all participating instructions, generally retaining their common permissions. Approximation needs the relevant afn/arcp/intrinsic contract; a generic error bound is not invented.

**Lean formulation** (in its source module context):

```lean
structure LLVMFloatingPointSemantics (Op Value Env : Type u) where
  isNaN : Value → Prop
  isInfinity : Value → Prop
  run : Op → Env → List Value → Set (Value × Env)
  permittedRewrite : Op → Op → Prop
```

**Source:** [`Catalog.LLVM.LLVMFloatingPointSemantics`](../lean/Catalog/LLVMTransforms.lean); consulted 2026-11-16.

**Scope:** partial

**Interpretation:** Abstract value/environment carriers, NaN/infinity predicates, outcome relation and a permittedRewrite relation.

**Limits:** No implemented IEEE arithmetic, bit encodings, NaN payload propagation, constrained-FP engine or complete fast-math semantics; value/exception/permission predicates are client supplied.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Rewrite-based flags must authorize the whole participating expression; contract alone does not authorize arbitrary reassociation.; FP results and observable exception/rounding effects must follow the selected default or constrained environment; exact-real equality is insufficient.

**basisKind:** relational-structural-definition

**basisScope:** LLVM 21.1.8 default FP assumes round-to-nearest, disabled traps, unobservable status flags and specified denormal environment. Constrained intrinsics/strictfp require explicit rounding and exception modes. NaNs, infinities and signed zeros are represented; value equality must match permitted observations. nnan/ninf violations produce poison. nsz permits ignoring zero sign without asserting -0 is poison. contract permits suitable contraction but not arbitrary reassociation; reassoc is distinct. Rewrite-based permissions must cover all participating instructions, generally retaining their common permissions. Approximation needs the relevant afn/arcp/intrinsic contract; a generic error bound is not invented.

**verificationObligation:** Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.; No implemented IEEE arithmetic, bit encodings, NaN payload propagation, constrained-FP engine or complete fast-math semantics; value/exception/permission predicates are client supplied.

**reviewStatus:** Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-LLVMFloatingPointSemantics-evaluate"></a>

### evaluate

`urn:csabs:operation/LLVMFloatingPointSemantics-evaluate`

**signature:** evaluate : Op×Environment×Args→P(Value×Environment)

**description:** Return format/environment-correct results and permitted exception effects.

**precondition:** Exact opcode, format, denormal and constrained modes fixed.

**postcondition:** Return format/environment-correct results and permitted exception effects.

**totality:** Operation-specific outcome relation.

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** LangRef: Floating-Point Environment, Fast-Math Flags and Rewrite-based flags, constrained floating-point intrinsics

**sourceNote:** Adapted LLVM floating-point environment and rewrite permissions from LangRef: Floating-Point Environment, Fast-Math Flags and Rewrite-based flags, constrained floating-point intrinsics. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-LLVMFloatingPointSemantics-permitted-rewrite"></a>

### permitted-rewrite

`urn:csabs:operation/LLVMFloatingPointSemantics-permitted-rewrite`

**signature:** permittedRewrite : Expression×Expression×Flags→Prop

**description:** Check every required flag and environment condition for the whole rewrite.

**precondition:** All participating operations and downstream observations accounted for.

**postcondition:** Check every required flag and environment condition for the whole rewrite.

**totality:** Total semantic predicate, generally undecidable.

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** LangRef: Floating-Point Environment, Fast-Math Flags and Rewrite-based flags, constrained floating-point intrinsics

**sourceNote:** Adapted LLVM floating-point environment and rewrite permissions from LangRef: Floating-Point Environment, Fast-Math Flags and Rewrite-based flags, constrained floating-point intrinsics. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-LLVMFloatingPointSemantics-permission-scope"></a>

### permission-scope

`urn:csabs:axiom/LLVMFloatingPointSemantics-permission-scope`

**description:** Defining obligation for LLVM floating-point environment and rewrite permissions

**statement:** Rewrite-based flags must authorize the whole participating expression; contract alone does not authorize arbitrary reassociation.

**formalStatement:** Rewrite-based flags must authorize the whole participating expression; contract alone does not authorize arbitrary reassociation.

**assumptions:** LLVM 21.1.8 default FP assumes round-to-nearest, disabled traps, unobservable status flags and specified denormal environment. Constrained intrinsics/strictfp require explicit rounding and exception modes. NaNs, infinities and signed zeros are represented; value equality must match permitted observations. nnan/ninf violations produce poison. nsz permits ignoring zero sign without asserting -0 is poison. contract permits suitable contraction but not arbitrary reassociation; reassoc is distinct. Rewrite-based permissions must cover all participating instructions, generally retaining their common permissions. Approximation needs the relevant afn/arcp/intrinsic contract; a generic error bound is not invented.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** LangRef: Floating-Point Environment, Fast-Math Flags and Rewrite-based flags, constrained floating-point intrinsics

**sourceNote:** Adapted LLVM floating-point environment and rewrite permissions from LangRef: Floating-Point Environment, Fast-Math Flags and Rewrite-based flags, constrained floating-point intrinsics. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

<a id="node-urn-csabs-axiom-LLVMFloatingPointSemantics-environment-observations"></a>

### environment-observations

`urn:csabs:axiom/LLVMFloatingPointSemantics-environment-observations`

**description:** Defining obligation for LLVM floating-point environment and rewrite permissions

**statement:** FP results and observable exception/rounding effects must follow the selected default or constrained environment; exact-real equality is insufficient.

**formalStatement:** FP results and observable exception/rounding effects must follow the selected default or constrained environment; exact-real equality is insufficient.

**assumptions:** LLVM 21.1.8 default FP assumes round-to-nearest, disabled traps, unobservable status flags and specified denormal environment. Constrained intrinsics/strictfp require explicit rounding and exception modes. NaNs, infinities and signed zeros are represented; value equality must match permitted observations. nnan/ninf violations produce poison. nsz permits ignoring zero sign without asserting -0 is poison. contract permits suitable contraction but not arbitrary reassociation; reassoc is distinct. Rewrite-based permissions must cover all participating instructions, generally retaining their common permissions. Approximation needs the relevant afn/arcp/intrinsic contract; a generic error bound is not invented.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** LangRef: Floating-Point Environment, Fast-Math Flags and Rewrite-based flags, constrained floating-point intrinsics

**sourceNote:** Adapted LLVM floating-point environment and rewrite permissions from LangRef: Floating-Point Environment, Fast-Math Flags and Rewrite-based flags, constrained floating-point intrinsics. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

## Laws

<a id="node-urn-csabs-law-LLVMFloatingPointSemantics-contraction-not-reassociation"></a>

### contraction-not-reassociation

`urn:csabs:law/LLVMFloatingPointSemantics-contraction-not-reassociation`

**description:** Derived consequence in the stated profile.

**statement:** A rewrite requiring reassociation cannot be justified solely by a contract flag.

**formalStatement:** A rewrite requiring reassociation cannot be justified solely by a contract flag.

**assumptions:** LLVM 21.1.8 default FP assumes round-to-nearest, disabled traps, unobservable status flags and specified denormal environment. Constrained intrinsics/strictfp require explicit rounding and exception modes. NaNs, infinities and signed zeros are represented; value equality must match permitted observations. nnan/ninf violations produce poison. nsz permits ignoring zero sign without asserting -0 is poison. contract permits suitable contraction but not arbitrary reassociation; reassoc is distinct. Rewrite-based permissions must cover all participating instructions, generally retaining their common permissions. Approximation needs the relevant afn/arcp/intrinsic contract; a generic error bound is not invented.

**dependsOn:** [permission-scope](LLVMFloatingPointSemantics.md#node-urn-csabs-axiom-LLVMFloatingPointSemantics-permission-scope)

**proofSketch:** The defining permissions distinguish contraction from reassociation, so the needed permission is not supplied.

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** LangRef: Floating-Point Environment, Fast-Math Flags and Rewrite-based flags, constrained floating-point intrinsics

**sourceNote:** Catalog derivation from the explicit dependsOn premises; the cited source motivates the interface, not this exact editorial theorem name.

**provenanceKind:** derived

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** LangRef: Floating-Point Environment, Fast-Math Flags and Rewrite-based flags, constrained floating-point intrinsics

**sourceNote:** Adapted LLVM floating-point environment and rewrite permissions from LangRef: Floating-Point Environment, Fast-Math Flags and Rewrite-based flags, constrained floating-point intrinsics. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/LLVMFloatingPointSemantics",
    "type": "Concept",
    "shortForm": "LLVMFloatingPointSemantics",
    "fullName": "LLVM floating-point environment and rewrite permissions",
    "definition": "A versioned floating-point contract retaining bit-level exceptional values, environment effects and per-instruction fast-math permissions independently of exact-real algebra.",
    "notation": "eval(op,env,args)⊆Value×Env; rewrite permitted by exact flag/environment contract",
    "category": [
      "urn:csabs:category/compiler-transformations"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "requiresConcept": [
      "urn:csabs:concept/FloatingPointType",
      "urn:csabs:concept/LLVMPoisonSemantics"
    ],
    "relatedConcept": [
      "urn:csabs:concept/GuardedRewrite",
      "urn:csabs:concept/PredicatedVectorSemantics"
    ],
    "hasOperation": [
      "urn:csabs:operation/LLVMFloatingPointSemantics-evaluate",
      "urn:csabs:operation/LLVMFloatingPointSemantics-permitted-rewrite"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/LLVMFloatingPointSemantics-permission-scope",
      "urn:csabs:axiom/LLVMFloatingPointSemantics-environment-observations"
    ],
    "hasLaw": [
      "urn:csabs:law/LLVMFloatingPointSemantics-contraction-not-reassociation"
    ],
    "hasTheorem": [],
    "basisKind": "relational-structural-definition",
    "basisScope": "LLVM 21.1.8 default FP assumes round-to-nearest, disabled traps, unobservable status flags and specified denormal environment. Constrained intrinsics/strictfp require explicit rounding and exception modes. NaNs, infinities and signed zeros are represented; value equality must match permitted observations. nnan/ninf violations produce poison. nsz permits ignoring zero sign without asserting -0 is poison. contract permits suitable contraction but not arbitrary reassociation; reassoc is distinct. Rewrite-based permissions must cover all participating instructions, generally retaining their common permissions. Approximation needs the relevant afn/arcp/intrinsic contract; a generic error bound is not invented.",
    "axiomBasis": "Rewrite-based flags must authorize the whole participating expression; contract alone does not authorize arbitrary reassociation.; FP results and observable exception/rounding effects must follow the selected default or constrained environment; exact-real equality is insufficient.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.",
    "verificationObligation": [
      "Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.",
      "No implemented IEEE arithmetic, bit encodings, NaN payload propagation, constrained-FP engine or complete fast-math semantics; value/exception/permission predicates are client supplied."
    ],
    "source": [
      "urn:csabs:source/compiler-llvm"
    ],
    "sourceLocator": "LangRef: Floating-Point Environment, Fast-Math Flags and Rewrite-based flags, constrained floating-point intrinsics",
    "sourceNote": "Adapted LLVM floating-point environment and rewrite permissions from LangRef: Floating-Point Environment, Fast-Math Flags and Rewrite-based flags, constrained floating-point intrinsics. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "mathematicalFormulation": "A versioned floating-point contract retaining bit-level exceptional values, environment effects and per-instruction fast-math permissions independently of exact-real algebra. eval(op,env,args)⊆Value×Env; rewrite permitted by exact flag/environment contract LLVM 21.1.8 default FP assumes round-to-nearest, disabled traps, unobservable status flags and specified denormal environment. Constrained intrinsics/strictfp require explicit rounding and exception modes. NaNs, infinities and signed zeros are represented; value equality must match permitted observations. nnan/ninf violations produce poison. nsz permits ignoring zero sign without asserting -0 is poison. contract permits suitable contraction but not arbitrary reassociation; reassoc is distinct. Rewrite-based permissions must cover all participating instructions, generally retaining their common permissions. Approximation needs the relevant afn/arcp/intrinsic contract; a generic error bound is not invented.",
    "leanFormulation": "structure LLVMFloatingPointSemantics (Op Value Env : Type u) where\n  isNaN : Value → Prop\n  isInfinity : Value → Prop\n  run : Op → Env → List Value → Set (Value × Env)\n  permittedRewrite : Op → Op → Prop",
    "formulationSource": "urn:csabs:source/compiler-llvm-lean",
    "formulationLocator": "Catalog.LLVM.LLVMFloatingPointSemantics",
    "formulationScope": "partial",
    "leanModelMapping": "Abstract value/environment carriers, NaN/infinity predicates, outcome relation and a permittedRewrite relation.",
    "leanModelLimitations": "No implemented IEEE arithmetic, bit encodings, NaN payload propagation, constrained-FP engine or complete fast-math semantics; value/exception/permission predicates are client supplied."
  },
  {
    "id": "urn:csabs:operation/LLVMFloatingPointSemantics-evaluate",
    "type": "Operation",
    "name": "evaluate",
    "signature": "evaluate : Op×Environment×Args→P(Value×Environment)",
    "description": "Return format/environment-correct results and permitted exception effects.",
    "concept": "urn:csabs:concept/LLVMFloatingPointSemantics",
    "precondition": "Exact opcode, format, denormal and constrained modes fixed.",
    "postcondition": "Return format/environment-correct results and permitted exception effects.",
    "totality": "Operation-specific outcome relation.",
    "source": [
      "urn:csabs:source/compiler-llvm"
    ],
    "sourceLocator": "LangRef: Floating-Point Environment, Fast-Math Flags and Rewrite-based flags, constrained floating-point intrinsics",
    "sourceNote": "Adapted LLVM floating-point environment and rewrite permissions from LangRef: Floating-Point Environment, Fast-Math Flags and Rewrite-based flags, constrained floating-point intrinsics. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/LLVMFloatingPointSemantics-permitted-rewrite",
    "type": "Operation",
    "name": "permitted-rewrite",
    "signature": "permittedRewrite : Expression×Expression×Flags→Prop",
    "description": "Check every required flag and environment condition for the whole rewrite.",
    "concept": "urn:csabs:concept/LLVMFloatingPointSemantics",
    "precondition": "All participating operations and downstream observations accounted for.",
    "postcondition": "Check every required flag and environment condition for the whole rewrite.",
    "totality": "Total semantic predicate, generally undecidable.",
    "source": [
      "urn:csabs:source/compiler-llvm"
    ],
    "sourceLocator": "LangRef: Floating-Point Environment, Fast-Math Flags and Rewrite-based flags, constrained floating-point intrinsics",
    "sourceNote": "Adapted LLVM floating-point environment and rewrite permissions from LangRef: Floating-Point Environment, Fast-Math Flags and Rewrite-based flags, constrained floating-point intrinsics. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/LLVMFloatingPointSemantics-permission-scope",
    "type": "Axiom",
    "name": "permission-scope",
    "description": "Defining obligation for LLVM floating-point environment and rewrite permissions",
    "statement": "Rewrite-based flags must authorize the whole participating expression; contract alone does not authorize arbitrary reassociation.",
    "formalStatement": "Rewrite-based flags must authorize the whole participating expression; contract alone does not authorize arbitrary reassociation.",
    "assumptions": [
      "LLVM 21.1.8 default FP assumes round-to-nearest, disabled traps, unobservable status flags and specified denormal environment. Constrained intrinsics/strictfp require explicit rounding and exception modes. NaNs, infinities and signed zeros are represented; value equality must match permitted observations. nnan/ninf violations produce poison. nsz permits ignoring zero sign without asserting -0 is poison. contract permits suitable contraction but not arbitrary reassociation; reassoc is distinct. Rewrite-based permissions must cover all participating instructions, generally retaining their common permissions. Approximation needs the relevant afn/arcp/intrinsic contract; a generic error bound is not invented."
    ],
    "appliesTo": [
      "urn:csabs:concept/LLVMFloatingPointSemantics"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-llvm"
    ],
    "sourceLocator": "LangRef: Floating-Point Environment, Fast-Math Flags and Rewrite-based flags, constrained floating-point intrinsics",
    "sourceNote": "Adapted LLVM floating-point environment and rewrite permissions from LangRef: Floating-Point Environment, Fast-Math Flags and Rewrite-based flags, constrained floating-point intrinsics. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:axiom/LLVMFloatingPointSemantics-environment-observations",
    "type": "Axiom",
    "name": "environment-observations",
    "description": "Defining obligation for LLVM floating-point environment and rewrite permissions",
    "statement": "FP results and observable exception/rounding effects must follow the selected default or constrained environment; exact-real equality is insufficient.",
    "formalStatement": "FP results and observable exception/rounding effects must follow the selected default or constrained environment; exact-real equality is insufficient.",
    "assumptions": [
      "LLVM 21.1.8 default FP assumes round-to-nearest, disabled traps, unobservable status flags and specified denormal environment. Constrained intrinsics/strictfp require explicit rounding and exception modes. NaNs, infinities and signed zeros are represented; value equality must match permitted observations. nnan/ninf violations produce poison. nsz permits ignoring zero sign without asserting -0 is poison. contract permits suitable contraction but not arbitrary reassociation; reassoc is distinct. Rewrite-based permissions must cover all participating instructions, generally retaining their common permissions. Approximation needs the relevant afn/arcp/intrinsic contract; a generic error bound is not invented."
    ],
    "appliesTo": [
      "urn:csabs:concept/LLVMFloatingPointSemantics"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-llvm"
    ],
    "sourceLocator": "LangRef: Floating-Point Environment, Fast-Math Flags and Rewrite-based flags, constrained floating-point intrinsics",
    "sourceNote": "Adapted LLVM floating-point environment and rewrite permissions from LangRef: Floating-Point Environment, Fast-Math Flags and Rewrite-based flags, constrained floating-point intrinsics. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:law/LLVMFloatingPointSemantics-contraction-not-reassociation",
    "type": "Law",
    "name": "contraction-not-reassociation",
    "description": "Derived consequence in the stated profile.",
    "statement": "A rewrite requiring reassociation cannot be justified solely by a contract flag.",
    "formalStatement": "A rewrite requiring reassociation cannot be justified solely by a contract flag.",
    "assumptions": [
      "LLVM 21.1.8 default FP assumes round-to-nearest, disabled traps, unobservable status flags and specified denormal environment. Constrained intrinsics/strictfp require explicit rounding and exception modes. NaNs, infinities and signed zeros are represented; value equality must match permitted observations. nnan/ninf violations produce poison. nsz permits ignoring zero sign without asserting -0 is poison. contract permits suitable contraction but not arbitrary reassociation; reassoc is distinct. Rewrite-based permissions must cover all participating instructions, generally retaining their common permissions. Approximation needs the relevant afn/arcp/intrinsic contract; a generic error bound is not invented."
    ],
    "appliesTo": [
      "urn:csabs:concept/LLVMFloatingPointSemantics"
    ],
    "dependsOn": [
      "urn:csabs:axiom/LLVMFloatingPointSemantics-permission-scope"
    ],
    "proofSketch": "The defining permissions distinguish contraction from reassociation, so the needed permission is not supplied.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-llvm"
    ],
    "sourceLocator": "LangRef: Floating-Point Environment, Fast-Math Flags and Rewrite-based flags, constrained floating-point intrinsics",
    "sourceNote": "Catalog derivation from the explicit dependsOn premises; the cited source motivates the interface, not this exact editorial theorem name.",
    "provenanceKind": "derived",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  }
]
```
<!-- graph-record:end -->
