# Environment-indexed symbol resolution and reachability

A module interpretation parameterized by admissible link/runtime environments, retaining symbol resolution, interposition, identity and externally exposed roots for interprocedural transformations.

**Notation:** resolve:Module×Environment×Symbol→P(Definition); correctness quantifies over admitted environments

**Stable ID:** `urn:csabs:concept/SymbolLinkage`

**Categories:** Programming-language semantics → Compiler transformations

**Kind:** semantic-model

**Prerequisites:** [Binary relation](Relation.md), [Call-boundary behavior and effect contract](CallEffectContract.md)

**Related concepts:** [Observable state representation relation](StateRepresentation.md), [Observable behavior refinement](BehaviorRefinement.md)

## Backlinks

- [Call-boundary behavior and effect contract](CallEffectContract.md) — `relatedConcept`

## Mathematical formulation

A module interpretation parameterized by admissible link/runtime environments, retaining symbol resolution, interposition, identity and externally exposed roots for interprocedural transformations. resolve:Module×Environment×Symbol→P(Definition); correctness quantifies over admitted environments LLVM 21.1.8 module/link environment; open-world external references, callbacks, constructors/destructors, llvm.used/compiler.used and aliases/ifuncs affect roots. Internalization needs an explicit export/closed-world policy. Interposable/weak/ODR/available\_externally definitions obey different rules; same body text alone does not justify replacement of an overridable call. Function/global address identity and unnamed\_addr permissions matter to merging. LTO import/link environment changes require their own resolution assumptions. Removing an unreferenced internal SCC can be valid; absence of local references does not prove an exported symbol dead.

**Lean formulation** (in its source module context):

```lean
structure SymbolLinkage (Module Environment Symbol Definition : Type u) where
  admissible : Environment → Prop
  resolve : Module → Environment → Symbol → Set Definition
  exposed : Module → Symbol → Prop
```

**Source:** [`Catalog.LLVM.SymbolLinkage`](../lean/Catalog/LLVMTransforms.lean); consulted 2026-11-16.

**Scope:** partial

**Interpretation:** Environment-admissibility predicate, set-valued resolution and exposed-symbol relation.

**Limits:** No linker, COMDAT/ODR/interposition algorithm, root closure or whole-program callgraph proof. The environment must model platform ABI and runtime uses explicitly.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** A module transformation preserves behavior for every admitted link/runtime environment, with corresponding symbol resolution and exports.; Root reachability includes all admitted external/runtime references, not only direct calls inside the current module.

**basisKind:** relational-structural-definition

**basisScope:** LLVM 21.1.8 module/link environment; open-world external references, callbacks, constructors/destructors, llvm.used/compiler.used and aliases/ifuncs affect roots. Internalization needs an explicit export/closed-world policy. Interposable/weak/ODR/available_externally definitions obey different rules; same body text alone does not justify replacement of an overridable call. Function/global address identity and unnamed_addr permissions matter to merging. LTO import/link environment changes require their own resolution assumptions. Removing an unreferenced internal SCC can be valid; absence of local references does not prove an exported symbol dead.

**verificationObligation:** Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.; No linker, COMDAT/ODR/interposition algorithm, root closure or whole-program callgraph proof. The environment must model platform ABI and runtime uses explicitly.

**reviewStatus:** Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-SymbolLinkage-resolve"></a>

### resolve

`urn:csabs:operation/SymbolLinkage-resolve`

**signature:** resolve : Module×Environment×Symbol→P(Definition)

**description:** Resolve permitted definitions under linkage, visibility and preemption rules.

**precondition:** Admissible link/runtime environments stated.

**postcondition:** Resolve permitted definitions under linkage, visibility and preemption rules.

**totality:** Nondeterministic semantic relation.

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM Pass Reference (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Passes.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Passes.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** LangRef: Linkage Types, Visibility Styles, DLL Storage Classes, Runtime Preemption Specifiers, unnamed_addr; Passes: internalize, globaldce, constmerge, mergefunc, function-import

**sourceNote:** Adapted Environment-indexed symbol resolution and reachability from LangRef: Linkage Types, Visibility Styles, DLL Storage Classes, Runtime Preemption Specifiers, unnamed_addr; Passes: internalize, globaldce, constmerge, mergefunc, function-import. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-SymbolLinkage-roots"></a>

### roots

`urn:csabs:operation/SymbolLinkage-roots`

**signature:** roots : Module×Environment→P(Symbol)

**description:** Include external uses, used lists and runtime entry roots.

**precondition:** Export/runtime policy and address escapes accounted for.

**postcondition:** Include external uses, used lists and runtime entry roots.

**totality:** Conservative root set.

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM Pass Reference (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Passes.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Passes.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** LangRef: Linkage Types, Visibility Styles, DLL Storage Classes, Runtime Preemption Specifiers, unnamed_addr; Passes: internalize, globaldce, constmerge, mergefunc, function-import

**sourceNote:** Adapted Environment-indexed symbol resolution and reachability from LangRef: Linkage Types, Visibility Styles, DLL Storage Classes, Runtime Preemption Specifiers, unnamed_addr; Passes: internalize, globaldce, constmerge, mergefunc, function-import. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-SymbolLinkage-environment-quantifier"></a>

### environment-quantifier

`urn:csabs:axiom/SymbolLinkage-environment-quantifier`

**description:** Defining obligation for Environment-indexed symbol resolution and reachability

**statement:** A module transformation preserves behavior for every admitted link/runtime environment, with corresponding symbol resolution and exports.

**formalStatement:** A module transformation preserves behavior for every admitted link/runtime environment, with corresponding symbol resolution and exports.

**assumptions:** LLVM 21.1.8 module/link environment; open-world external references, callbacks, constructors/destructors, llvm.used/compiler.used and aliases/ifuncs affect roots. Internalization needs an explicit export/closed-world policy. Interposable/weak/ODR/available_externally definitions obey different rules; same body text alone does not justify replacement of an overridable call. Function/global address identity and unnamed_addr permissions matter to merging. LTO import/link environment changes require their own resolution assumptions. Removing an unreferenced internal SCC can be valid; absence of local references does not prove an exported symbol dead.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM Pass Reference (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Passes.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Passes.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** LangRef: Linkage Types, Visibility Styles, DLL Storage Classes, Runtime Preemption Specifiers, unnamed_addr; Passes: internalize, globaldce, constmerge, mergefunc, function-import

**sourceNote:** Adapted Environment-indexed symbol resolution and reachability from LangRef: Linkage Types, Visibility Styles, DLL Storage Classes, Runtime Preemption Specifiers, unnamed_addr; Passes: internalize, globaldce, constmerge, mergefunc, function-import. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

<a id="node-urn-csabs-axiom-SymbolLinkage-external-roots"></a>

### external-roots

`urn:csabs:axiom/SymbolLinkage-external-roots`

**description:** Defining obligation for Environment-indexed symbol resolution and reachability

**statement:** Root reachability includes all admitted external/runtime references, not only direct calls inside the current module.

**formalStatement:** Root reachability includes all admitted external/runtime references, not only direct calls inside the current module.

**assumptions:** LLVM 21.1.8 module/link environment; open-world external references, callbacks, constructors/destructors, llvm.used/compiler.used and aliases/ifuncs affect roots. Internalization needs an explicit export/closed-world policy. Interposable/weak/ODR/available_externally definitions obey different rules; same body text alone does not justify replacement of an overridable call. Function/global address identity and unnamed_addr permissions matter to merging. LTO import/link environment changes require their own resolution assumptions. Removing an unreferenced internal SCC can be valid; absence of local references does not prove an exported symbol dead.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM Pass Reference (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Passes.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Passes.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** LangRef: Linkage Types, Visibility Styles, DLL Storage Classes, Runtime Preemption Specifiers, unnamed_addr; Passes: internalize, globaldce, constmerge, mergefunc, function-import

**sourceNote:** Adapted Environment-indexed symbol resolution and reachability from LangRef: Linkage Types, Visibility Styles, DLL Storage Classes, Runtime Preemption Specifiers, unnamed_addr; Passes: internalize, globaldce, constmerge, mergefunc, function-import. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

## Laws

<a id="node-urn-csabs-law-SymbolLinkage-local-no-use-insufficient"></a>

### local-no-use-insufficient

`urn:csabs:law/SymbolLinkage-local-no-use-insufficient`

**description:** Derived consequence in the stated profile.

**statement:** No references inside the module alone does not establish an externally exposed definition is unreachable.

**formalStatement:** No references inside the module alone does not establish an externally exposed definition is unreachable.

**assumptions:** LLVM 21.1.8 module/link environment; open-world external references, callbacks, constructors/destructors, llvm.used/compiler.used and aliases/ifuncs affect roots. Internalization needs an explicit export/closed-world policy. Interposable/weak/ODR/available_externally definitions obey different rules; same body text alone does not justify replacement of an overridable call. Function/global address identity and unnamed_addr permissions matter to merging. LTO import/link environment changes require their own resolution assumptions. Removing an unreferenced internal SCC can be valid; absence of local references does not prove an exported symbol dead.

**dependsOn:** [external-roots](SymbolLinkage.md#node-urn-csabs-axiom-SymbolLinkage-external-roots)

**proofSketch:** An admitted external environment may call or reference the exposed symbol, producing a root not represented by local references.

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM Pass Reference (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Passes.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Passes.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** LangRef: Linkage Types, Visibility Styles, DLL Storage Classes, Runtime Preemption Specifiers, unnamed_addr; Passes: internalize, globaldce, constmerge, mergefunc, function-import

**sourceNote:** Catalog derivation from the explicit dependsOn premises; the cited source motivates the interface, not this exact editorial theorem name.

**provenanceKind:** derived

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification
- [LLVM Pass Reference (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/Passes.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/Passes.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** LangRef: Linkage Types, Visibility Styles, DLL Storage Classes, Runtime Preemption Specifiers, unnamed_addr; Passes: internalize, globaldce, constmerge, mergefunc, function-import

**sourceNote:** Adapted Environment-indexed symbol resolution and reachability from LangRef: Linkage Types, Visibility Styles, DLL Storage Classes, Runtime Preemption Specifiers, unnamed_addr; Passes: internalize, globaldce, constmerge, mergefunc, function-import. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/SymbolLinkage",
    "type": "Concept",
    "shortForm": "SymbolLinkage",
    "fullName": "Environment-indexed symbol resolution and reachability",
    "definition": "A module interpretation parameterized by admissible link/runtime environments, retaining symbol resolution, interposition, identity and externally exposed roots for interprocedural transformations.",
    "notation": "resolve:Module×Environment×Symbol→P(Definition); correctness quantifies over admitted environments",
    "category": [
      "urn:csabs:category/compiler-transformations"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "requiresConcept": [
      "urn:csabs:concept/Relation",
      "urn:csabs:concept/CallEffectContract"
    ],
    "relatedConcept": [
      "urn:csabs:concept/StateRepresentation",
      "urn:csabs:concept/BehaviorRefinement"
    ],
    "hasOperation": [
      "urn:csabs:operation/SymbolLinkage-resolve",
      "urn:csabs:operation/SymbolLinkage-roots"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/SymbolLinkage-environment-quantifier",
      "urn:csabs:axiom/SymbolLinkage-external-roots"
    ],
    "hasLaw": [
      "urn:csabs:law/SymbolLinkage-local-no-use-insufficient"
    ],
    "hasTheorem": [],
    "basisKind": "relational-structural-definition",
    "basisScope": "LLVM 21.1.8 module/link environment; open-world external references, callbacks, constructors/destructors, llvm.used/compiler.used and aliases/ifuncs affect roots. Internalization needs an explicit export/closed-world policy. Interposable/weak/ODR/available_externally definitions obey different rules; same body text alone does not justify replacement of an overridable call. Function/global address identity and unnamed_addr permissions matter to merging. LTO import/link environment changes require their own resolution assumptions. Removing an unreferenced internal SCC can be valid; absence of local references does not prove an exported symbol dead.",
    "axiomBasis": "A module transformation preserves behavior for every admitted link/runtime environment, with corresponding symbol resolution and exports.; Root reachability includes all admitted external/runtime references, not only direct calls inside the current module.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.",
    "verificationObligation": [
      "Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.",
      "No linker, COMDAT/ODR/interposition algorithm, root closure or whole-program callgraph proof. The environment must model platform ABI and runtime uses explicitly."
    ],
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-pass-reference"
    ],
    "sourceLocator": "LangRef: Linkage Types, Visibility Styles, DLL Storage Classes, Runtime Preemption Specifiers, unnamed_addr; Passes: internalize, globaldce, constmerge, mergefunc, function-import",
    "sourceNote": "Adapted Environment-indexed symbol resolution and reachability from LangRef: Linkage Types, Visibility Styles, DLL Storage Classes, Runtime Preemption Specifiers, unnamed_addr; Passes: internalize, globaldce, constmerge, mergefunc, function-import. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "mathematicalFormulation": "A module interpretation parameterized by admissible link/runtime environments, retaining symbol resolution, interposition, identity and externally exposed roots for interprocedural transformations. resolve:Module×Environment×Symbol→P(Definition); correctness quantifies over admitted environments LLVM 21.1.8 module/link environment; open-world external references, callbacks, constructors/destructors, llvm.used/compiler.used and aliases/ifuncs affect roots. Internalization needs an explicit export/closed-world policy. Interposable/weak/ODR/available_externally definitions obey different rules; same body text alone does not justify replacement of an overridable call. Function/global address identity and unnamed_addr permissions matter to merging. LTO import/link environment changes require their own resolution assumptions. Removing an unreferenced internal SCC can be valid; absence of local references does not prove an exported symbol dead.",
    "leanFormulation": "structure SymbolLinkage (Module Environment Symbol Definition : Type u) where\n  admissible : Environment → Prop\n  resolve : Module → Environment → Symbol → Set Definition\n  exposed : Module → Symbol → Prop",
    "formulationSource": "urn:csabs:source/compiler-llvm-lean",
    "formulationLocator": "Catalog.LLVM.SymbolLinkage",
    "formulationScope": "partial",
    "leanModelMapping": "Environment-admissibility predicate, set-valued resolution and exposed-symbol relation.",
    "leanModelLimitations": "No linker, COMDAT/ODR/interposition algorithm, root closure or whole-program callgraph proof. The environment must model platform ABI and runtime uses explicitly."
  },
  {
    "id": "urn:csabs:operation/SymbolLinkage-resolve",
    "type": "Operation",
    "name": "resolve",
    "signature": "resolve : Module×Environment×Symbol→P(Definition)",
    "description": "Resolve permitted definitions under linkage, visibility and preemption rules.",
    "concept": "urn:csabs:concept/SymbolLinkage",
    "precondition": "Admissible link/runtime environments stated.",
    "postcondition": "Resolve permitted definitions under linkage, visibility and preemption rules.",
    "totality": "Nondeterministic semantic relation.",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-pass-reference"
    ],
    "sourceLocator": "LangRef: Linkage Types, Visibility Styles, DLL Storage Classes, Runtime Preemption Specifiers, unnamed_addr; Passes: internalize, globaldce, constmerge, mergefunc, function-import",
    "sourceNote": "Adapted Environment-indexed symbol resolution and reachability from LangRef: Linkage Types, Visibility Styles, DLL Storage Classes, Runtime Preemption Specifiers, unnamed_addr; Passes: internalize, globaldce, constmerge, mergefunc, function-import. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/SymbolLinkage-roots",
    "type": "Operation",
    "name": "roots",
    "signature": "roots : Module×Environment→P(Symbol)",
    "description": "Include external uses, used lists and runtime entry roots.",
    "concept": "urn:csabs:concept/SymbolLinkage",
    "precondition": "Export/runtime policy and address escapes accounted for.",
    "postcondition": "Include external uses, used lists and runtime entry roots.",
    "totality": "Conservative root set.",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-pass-reference"
    ],
    "sourceLocator": "LangRef: Linkage Types, Visibility Styles, DLL Storage Classes, Runtime Preemption Specifiers, unnamed_addr; Passes: internalize, globaldce, constmerge, mergefunc, function-import",
    "sourceNote": "Adapted Environment-indexed symbol resolution and reachability from LangRef: Linkage Types, Visibility Styles, DLL Storage Classes, Runtime Preemption Specifiers, unnamed_addr; Passes: internalize, globaldce, constmerge, mergefunc, function-import. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/SymbolLinkage-environment-quantifier",
    "type": "Axiom",
    "name": "environment-quantifier",
    "description": "Defining obligation for Environment-indexed symbol resolution and reachability",
    "statement": "A module transformation preserves behavior for every admitted link/runtime environment, with corresponding symbol resolution and exports.",
    "formalStatement": "A module transformation preserves behavior for every admitted link/runtime environment, with corresponding symbol resolution and exports.",
    "assumptions": [
      "LLVM 21.1.8 module/link environment; open-world external references, callbacks, constructors/destructors, llvm.used/compiler.used and aliases/ifuncs affect roots. Internalization needs an explicit export/closed-world policy. Interposable/weak/ODR/available_externally definitions obey different rules; same body text alone does not justify replacement of an overridable call. Function/global address identity and unnamed_addr permissions matter to merging. LTO import/link environment changes require their own resolution assumptions. Removing an unreferenced internal SCC can be valid; absence of local references does not prove an exported symbol dead."
    ],
    "appliesTo": [
      "urn:csabs:concept/SymbolLinkage"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-pass-reference"
    ],
    "sourceLocator": "LangRef: Linkage Types, Visibility Styles, DLL Storage Classes, Runtime Preemption Specifiers, unnamed_addr; Passes: internalize, globaldce, constmerge, mergefunc, function-import",
    "sourceNote": "Adapted Environment-indexed symbol resolution and reachability from LangRef: Linkage Types, Visibility Styles, DLL Storage Classes, Runtime Preemption Specifiers, unnamed_addr; Passes: internalize, globaldce, constmerge, mergefunc, function-import. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:axiom/SymbolLinkage-external-roots",
    "type": "Axiom",
    "name": "external-roots",
    "description": "Defining obligation for Environment-indexed symbol resolution and reachability",
    "statement": "Root reachability includes all admitted external/runtime references, not only direct calls inside the current module.",
    "formalStatement": "Root reachability includes all admitted external/runtime references, not only direct calls inside the current module.",
    "assumptions": [
      "LLVM 21.1.8 module/link environment; open-world external references, callbacks, constructors/destructors, llvm.used/compiler.used and aliases/ifuncs affect roots. Internalization needs an explicit export/closed-world policy. Interposable/weak/ODR/available_externally definitions obey different rules; same body text alone does not justify replacement of an overridable call. Function/global address identity and unnamed_addr permissions matter to merging. LTO import/link environment changes require their own resolution assumptions. Removing an unreferenced internal SCC can be valid; absence of local references does not prove an exported symbol dead."
    ],
    "appliesTo": [
      "urn:csabs:concept/SymbolLinkage"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-pass-reference"
    ],
    "sourceLocator": "LangRef: Linkage Types, Visibility Styles, DLL Storage Classes, Runtime Preemption Specifiers, unnamed_addr; Passes: internalize, globaldce, constmerge, mergefunc, function-import",
    "sourceNote": "Adapted Environment-indexed symbol resolution and reachability from LangRef: Linkage Types, Visibility Styles, DLL Storage Classes, Runtime Preemption Specifiers, unnamed_addr; Passes: internalize, globaldce, constmerge, mergefunc, function-import. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:law/SymbolLinkage-local-no-use-insufficient",
    "type": "Law",
    "name": "local-no-use-insufficient",
    "description": "Derived consequence in the stated profile.",
    "statement": "No references inside the module alone does not establish an externally exposed definition is unreachable.",
    "formalStatement": "No references inside the module alone does not establish an externally exposed definition is unreachable.",
    "assumptions": [
      "LLVM 21.1.8 module/link environment; open-world external references, callbacks, constructors/destructors, llvm.used/compiler.used and aliases/ifuncs affect roots. Internalization needs an explicit export/closed-world policy. Interposable/weak/ODR/available_externally definitions obey different rules; same body text alone does not justify replacement of an overridable call. Function/global address identity and unnamed_addr permissions matter to merging. LTO import/link environment changes require their own resolution assumptions. Removing an unreferenced internal SCC can be valid; absence of local references does not prove an exported symbol dead."
    ],
    "appliesTo": [
      "urn:csabs:concept/SymbolLinkage"
    ],
    "dependsOn": [
      "urn:csabs:axiom/SymbolLinkage-external-roots"
    ],
    "proofSketch": "An admitted external environment may call or reference the exposed symbol, producing a root not represented by local references.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-pass-reference"
    ],
    "sourceLocator": "LangRef: Linkage Types, Visibility Styles, DLL Storage Classes, Runtime Preemption Specifiers, unnamed_addr; Passes: internalize, globaldce, constmerge, mergefunc, function-import",
    "sourceNote": "Catalog derivation from the explicit dependsOn premises; the cited source motivates the interface, not this exact editorial theorem name.",
    "provenanceKind": "derived",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  }
]
```
<!-- graph-record:end -->
