# Target-indexed storage and ABI layout

A target-indexed interpretation of sized IR types into storage size, allocation stride, alignment, field offsets and address-space-specific pointer/index widths.

**Notation:** Layout(T,AS)=(storeBytes,allocBytes,align,fieldOffsets,ptrBits,indexBits)

**Stable ID:** `urn:csabs:concept/DataLayout`

**Categories:** Programming-language semantics → Compiler transformations

**Kind:** semantic-model

**Prerequisites:** [Fixed-width bit vector](BitVector.md), [Mathematical integers](Integer.md)

**Related concepts:** [Integer quasi-affine index map](IntegerAffineMap.md), [Allocation-associated pointer provenance and lifetime](PointerProvenance.md), [Byte-addressed memory with typed access obligations](ByteMemory.md)

## Backlinks

- [Byte-addressed memory with typed access obligations](ByteMemory.md) — `requiresConcept`
- [Typed IR legalization with representation relation](DialectConversion.md) — `relatedConcept`
- [Allocation-associated pointer provenance and lifetime](PointerProvenance.md) — `requiresConcept`

## Mathematical formulation

A target-indexed interpretation of sized IR types into storage size, allocation stride, alignment, field offsets and address-space-specific pointer/index widths. Layout(T,AS)=(storeBytes,allocBytes,align,fieldOffsets,ptrBits,indexBits) LLVM 21.1.8 layout of sized types. Endianness, padding and ABI alignment are explicit. Store size and allocation stride are distinct. Scalable types require symbolic runtime vscale sizes, not a fixed host sizeof. Pointer representation width may differ from index width; index arithmetic updates low index-width bits. Non-integral pointer rules are separate. GEP computes an address without dereferencing it. Unsized types have no total allocation-size query.

**Lean formulation** (in its source module context):

```lean
structure DataLayout (Ty AddressSpace : Type u) where
  storeSize : Ty → Nat
  allocationSize : Ty → Nat
  abiAlignment : Ty → Nat
  pointerWidth : AddressSpace → Nat
  indexWidth : AddressSpace → Nat
  littleEndian : Bool
  sized : Ty → Prop
```

**Source:** [`Catalog.LLVM.DataLayout`](../lean/Catalog/LLVMTransforms.lean); consulted 2026-11-16.

**Scope:** partial

**Interpretation:** Sized-type predicate and store/allocation/alignment/pointer-width query functions; littleEndian is explicit.

**Limits:** No full layout parser, field-offset evaluator, scalable-size algebra, GEP flag checker or ABI implementation. The store/allocation constraint is an editorial obligation, not enforced by this raw Lean interface.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** GEP sequential indexing uses allocation stride and index-width arithmetic; struct indexing uses layout field offsets.; StoreBytes(T)≤AllocBytes(T); padding may make the inequality strict; neither is inferred from host sizeof.

**basisKind:** relational-structural-definition

**basisScope:** LLVM 21.1.8 layout of sized types. Endianness, padding and ABI alignment are explicit. Store size and allocation stride are distinct. Scalable types require symbolic runtime vscale sizes, not a fixed host sizeof. Pointer representation width may differ from index width; index arithmetic updates low index-width bits. Non-integral pointer rules are separate. GEP computes an address without dereferencing it. Unsized types have no total allocation-size query.

**verificationObligation:** Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.; No full layout parser, field-offset evaluator, scalable-size algebra, GEP flag checker or ABI implementation. The store/allocation constraint is an editorial obligation, not enforced by this raw Lean interface.

**reviewStatus:** Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-DataLayout-layout"></a>

### layout

`urn:csabs:operation/DataLayout-layout`

**signature:** layout : Target×SizedType→Layout

**description:** Compute target storage/stride/alignment and field offsets.

**precondition:** Type sized under the target, vscale policy explicit.

**postcondition:** Compute target storage/stride/alignment and field offsets.

**totality:** Partial on arbitrary IR types.

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM getelementptr FAQ (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/GetElementPtr.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/GetElementPtr.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** LangRef: Data Layout; getelementptr instruction, offset calculation; GEP FAQ: What is dereferenced by GEP?

**sourceNote:** Adapted Target-indexed storage and ABI layout from LangRef: Data Layout; getelementptr instruction, offset calculation; GEP FAQ: What is dereferenced by GEP?. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-DataLayout-gep-offset"></a>

### gep-offset

`urn:csabs:operation/DataLayout-gep-offset`

**signature:** gepOffset : Layout×Type×Indices→BitVector(indexBits)

**description:** Compute typed offsets with index-width arithmetic and allocation stride.

**precondition:** Legal GEP types/indices and flags validated separately.

**postcondition:** Compute typed offsets with index-width arithmetic and allocation stride.

**totality:** Total for well-formed unflagged offset computation.

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM getelementptr FAQ (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/GetElementPtr.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/GetElementPtr.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** LangRef: Data Layout; getelementptr instruction, offset calculation; GEP FAQ: What is dereferenced by GEP?

**sourceNote:** Adapted Target-indexed storage and ABI layout from LangRef: Data Layout; getelementptr instruction, offset calculation; GEP FAQ: What is dereferenced by GEP?. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-DataLayout-typed-offset"></a>

### typed-offset

`urn:csabs:axiom/DataLayout-typed-offset`

**description:** Defining obligation for Target-indexed storage and ABI layout

**statement:** GEP sequential indexing uses allocation stride and index-width arithmetic; struct indexing uses layout field offsets.

**formalStatement:** GEP sequential indexing uses allocation stride and index-width arithmetic; struct indexing uses layout field offsets.

**assumptions:** LLVM 21.1.8 layout of sized types. Endianness, padding and ABI alignment are explicit. Store size and allocation stride are distinct. Scalable types require symbolic runtime vscale sizes, not a fixed host sizeof. Pointer representation width may differ from index width; index arithmetic updates low index-width bits. Non-integral pointer rules are separate. GEP computes an address without dereferencing it. Unsized types have no total allocation-size query.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM getelementptr FAQ (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/GetElementPtr.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/GetElementPtr.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** LangRef: Data Layout; getelementptr instruction, offset calculation; GEP FAQ: What is dereferenced by GEP?

**sourceNote:** Adapted Target-indexed storage and ABI layout from LangRef: Data Layout; getelementptr instruction, offset calculation; GEP FAQ: What is dereferenced by GEP?. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

<a id="node-urn-csabs-axiom-DataLayout-storage-distinction"></a>

### storage-distinction

`urn:csabs:axiom/DataLayout-storage-distinction`

**description:** Defining obligation for Target-indexed storage and ABI layout

**statement:** StoreBytes(T)≤AllocBytes(T); padding may make the inequality strict; neither is inferred from host sizeof.

**formalStatement:** StoreBytes(T)≤AllocBytes(T); padding may make the inequality strict; neither is inferred from host sizeof.

**assumptions:** LLVM 21.1.8 layout of sized types. Endianness, padding and ABI alignment are explicit. Store size and allocation stride are distinct. Scalable types require symbolic runtime vscale sizes, not a fixed host sizeof. Pointer representation width may differ from index width; index arithmetic updates low index-width bits. Non-integral pointer rules are separate. GEP computes an address without dereferencing it. Unsized types have no total allocation-size query.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM getelementptr FAQ (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/GetElementPtr.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/GetElementPtr.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** LangRef: Data Layout; getelementptr instruction, offset calculation; GEP FAQ: What is dereferenced by GEP?

**sourceNote:** Adapted Target-indexed storage and ABI layout from LangRef: Data Layout; getelementptr instruction, offset calculation; GEP FAQ: What is dereferenced by GEP?. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

## Laws

<a id="node-urn-csabs-law-DataLayout-gep-not-load"></a>

### gep-not-load

`urn:csabs:law/DataLayout-gep-not-load`

**description:** Derived consequence in the stated profile.

**statement:** Computing an unflagged GEP does not itself read the addressed bytes.

**formalStatement:** Computing an unflagged GEP does not itself read the addressed bytes.

**assumptions:** LLVM 21.1.8 layout of sized types. Endianness, padding and ABI alignment are explicit. Store size and allocation stride are distinct. Scalable types require symbolic runtime vscale sizes, not a fixed host sizeof. Pointer representation width may differ from index width; index arithmetic updates low index-width bits. Non-integral pointer rules are separate. GEP computes an address without dereferencing it. Unsized types have no total allocation-size query.

**dependsOn:** [typed-offset](DataLayout.md#node-urn-csabs-axiom-DataLayout-typed-offset)

**proofSketch:** The offset rule computes a pointer; a later load/store carries independent access obligations. Additional GEP flags may still introduce poison.

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM getelementptr FAQ (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/GetElementPtr.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/GetElementPtr.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** LangRef: Data Layout; getelementptr instruction, offset calculation; GEP FAQ: What is dereferenced by GEP?

**sourceNote:** Catalog derivation from the explicit dependsOn premises; the cited source motivates the interface, not this exact editorial theorem name.

**provenanceKind:** derived

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification
- [LLVM getelementptr FAQ (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/GetElementPtr.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/GetElementPtr.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** LangRef: Data Layout; getelementptr instruction, offset calculation; GEP FAQ: What is dereferenced by GEP?

**sourceNote:** Adapted Target-indexed storage and ABI layout from LangRef: Data Layout; getelementptr instruction, offset calculation; GEP FAQ: What is dereferenced by GEP?. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/DataLayout",
    "type": "Concept",
    "shortForm": "DataLayout",
    "fullName": "Target-indexed storage and ABI layout",
    "definition": "A target-indexed interpretation of sized IR types into storage size, allocation stride, alignment, field offsets and address-space-specific pointer/index widths.",
    "notation": "Layout(T,AS)=(storeBytes,allocBytes,align,fieldOffsets,ptrBits,indexBits)",
    "category": [
      "urn:csabs:category/compiler-transformations"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "requiresConcept": [
      "urn:csabs:concept/BitVector",
      "urn:csabs:concept/MathematicalInteger"
    ],
    "relatedConcept": [
      "urn:csabs:concept/IntegerAffineMap",
      "urn:csabs:concept/PointerProvenance",
      "urn:csabs:concept/ByteMemory"
    ],
    "hasOperation": [
      "urn:csabs:operation/DataLayout-layout",
      "urn:csabs:operation/DataLayout-gep-offset"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/DataLayout-typed-offset",
      "urn:csabs:axiom/DataLayout-storage-distinction"
    ],
    "hasLaw": [
      "urn:csabs:law/DataLayout-gep-not-load"
    ],
    "hasTheorem": [],
    "basisKind": "relational-structural-definition",
    "basisScope": "LLVM 21.1.8 layout of sized types. Endianness, padding and ABI alignment are explicit. Store size and allocation stride are distinct. Scalable types require symbolic runtime vscale sizes, not a fixed host sizeof. Pointer representation width may differ from index width; index arithmetic updates low index-width bits. Non-integral pointer rules are separate. GEP computes an address without dereferencing it. Unsized types have no total allocation-size query.",
    "axiomBasis": "GEP sequential indexing uses allocation stride and index-width arithmetic; struct indexing uses layout field offsets.; StoreBytes(T)≤AllocBytes(T); padding may make the inequality strict; neither is inferred from host sizeof.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.",
    "verificationObligation": [
      "Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.",
      "No full layout parser, field-offset evaluator, scalable-size algebra, GEP flag checker or ABI implementation. The store/allocation constraint is an editorial obligation, not enforced by this raw Lean interface."
    ],
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-gep"
    ],
    "sourceLocator": "LangRef: Data Layout; getelementptr instruction, offset calculation; GEP FAQ: What is dereferenced by GEP?",
    "sourceNote": "Adapted Target-indexed storage and ABI layout from LangRef: Data Layout; getelementptr instruction, offset calculation; GEP FAQ: What is dereferenced by GEP?. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "mathematicalFormulation": "A target-indexed interpretation of sized IR types into storage size, allocation stride, alignment, field offsets and address-space-specific pointer/index widths. Layout(T,AS)=(storeBytes,allocBytes,align,fieldOffsets,ptrBits,indexBits) LLVM 21.1.8 layout of sized types. Endianness, padding and ABI alignment are explicit. Store size and allocation stride are distinct. Scalable types require symbolic runtime vscale sizes, not a fixed host sizeof. Pointer representation width may differ from index width; index arithmetic updates low index-width bits. Non-integral pointer rules are separate. GEP computes an address without dereferencing it. Unsized types have no total allocation-size query.",
    "leanFormulation": "structure DataLayout (Ty AddressSpace : Type u) where\n  storeSize : Ty → Nat\n  allocationSize : Ty → Nat\n  abiAlignment : Ty → Nat\n  pointerWidth : AddressSpace → Nat\n  indexWidth : AddressSpace → Nat\n  littleEndian : Bool\n  sized : Ty → Prop",
    "formulationSource": "urn:csabs:source/compiler-llvm-lean",
    "formulationLocator": "Catalog.LLVM.DataLayout",
    "formulationScope": "partial",
    "leanModelMapping": "Sized-type predicate and store/allocation/alignment/pointer-width query functions; littleEndian is explicit.",
    "leanModelLimitations": "No full layout parser, field-offset evaluator, scalable-size algebra, GEP flag checker or ABI implementation. The store/allocation constraint is an editorial obligation, not enforced by this raw Lean interface."
  },
  {
    "id": "urn:csabs:operation/DataLayout-layout",
    "type": "Operation",
    "name": "layout",
    "signature": "layout : Target×SizedType→Layout",
    "description": "Compute target storage/stride/alignment and field offsets.",
    "concept": "urn:csabs:concept/DataLayout",
    "precondition": "Type sized under the target, vscale policy explicit.",
    "postcondition": "Compute target storage/stride/alignment and field offsets.",
    "totality": "Partial on arbitrary IR types.",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-gep"
    ],
    "sourceLocator": "LangRef: Data Layout; getelementptr instruction, offset calculation; GEP FAQ: What is dereferenced by GEP?",
    "sourceNote": "Adapted Target-indexed storage and ABI layout from LangRef: Data Layout; getelementptr instruction, offset calculation; GEP FAQ: What is dereferenced by GEP?. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/DataLayout-gep-offset",
    "type": "Operation",
    "name": "gep-offset",
    "signature": "gepOffset : Layout×Type×Indices→BitVector(indexBits)",
    "description": "Compute typed offsets with index-width arithmetic and allocation stride.",
    "concept": "urn:csabs:concept/DataLayout",
    "precondition": "Legal GEP types/indices and flags validated separately.",
    "postcondition": "Compute typed offsets with index-width arithmetic and allocation stride.",
    "totality": "Total for well-formed unflagged offset computation.",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-gep"
    ],
    "sourceLocator": "LangRef: Data Layout; getelementptr instruction, offset calculation; GEP FAQ: What is dereferenced by GEP?",
    "sourceNote": "Adapted Target-indexed storage and ABI layout from LangRef: Data Layout; getelementptr instruction, offset calculation; GEP FAQ: What is dereferenced by GEP?. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/DataLayout-typed-offset",
    "type": "Axiom",
    "name": "typed-offset",
    "description": "Defining obligation for Target-indexed storage and ABI layout",
    "statement": "GEP sequential indexing uses allocation stride and index-width arithmetic; struct indexing uses layout field offsets.",
    "formalStatement": "GEP sequential indexing uses allocation stride and index-width arithmetic; struct indexing uses layout field offsets.",
    "assumptions": [
      "LLVM 21.1.8 layout of sized types. Endianness, padding and ABI alignment are explicit. Store size and allocation stride are distinct. Scalable types require symbolic runtime vscale sizes, not a fixed host sizeof. Pointer representation width may differ from index width; index arithmetic updates low index-width bits. Non-integral pointer rules are separate. GEP computes an address without dereferencing it. Unsized types have no total allocation-size query."
    ],
    "appliesTo": [
      "urn:csabs:concept/DataLayout"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-gep"
    ],
    "sourceLocator": "LangRef: Data Layout; getelementptr instruction, offset calculation; GEP FAQ: What is dereferenced by GEP?",
    "sourceNote": "Adapted Target-indexed storage and ABI layout from LangRef: Data Layout; getelementptr instruction, offset calculation; GEP FAQ: What is dereferenced by GEP?. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:axiom/DataLayout-storage-distinction",
    "type": "Axiom",
    "name": "storage-distinction",
    "description": "Defining obligation for Target-indexed storage and ABI layout",
    "statement": "StoreBytes(T)≤AllocBytes(T); padding may make the inequality strict; neither is inferred from host sizeof.",
    "formalStatement": "StoreBytes(T)≤AllocBytes(T); padding may make the inequality strict; neither is inferred from host sizeof.",
    "assumptions": [
      "LLVM 21.1.8 layout of sized types. Endianness, padding and ABI alignment are explicit. Store size and allocation stride are distinct. Scalable types require symbolic runtime vscale sizes, not a fixed host sizeof. Pointer representation width may differ from index width; index arithmetic updates low index-width bits. Non-integral pointer rules are separate. GEP computes an address without dereferencing it. Unsized types have no total allocation-size query."
    ],
    "appliesTo": [
      "urn:csabs:concept/DataLayout"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-gep"
    ],
    "sourceLocator": "LangRef: Data Layout; getelementptr instruction, offset calculation; GEP FAQ: What is dereferenced by GEP?",
    "sourceNote": "Adapted Target-indexed storage and ABI layout from LangRef: Data Layout; getelementptr instruction, offset calculation; GEP FAQ: What is dereferenced by GEP?. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:law/DataLayout-gep-not-load",
    "type": "Law",
    "name": "gep-not-load",
    "description": "Derived consequence in the stated profile.",
    "statement": "Computing an unflagged GEP does not itself read the addressed bytes.",
    "formalStatement": "Computing an unflagged GEP does not itself read the addressed bytes.",
    "assumptions": [
      "LLVM 21.1.8 layout of sized types. Endianness, padding and ABI alignment are explicit. Store size and allocation stride are distinct. Scalable types require symbolic runtime vscale sizes, not a fixed host sizeof. Pointer representation width may differ from index width; index arithmetic updates low index-width bits. Non-integral pointer rules are separate. GEP computes an address without dereferencing it. Unsized types have no total allocation-size query."
    ],
    "appliesTo": [
      "urn:csabs:concept/DataLayout"
    ],
    "dependsOn": [
      "urn:csabs:axiom/DataLayout-typed-offset"
    ],
    "proofSketch": "The offset rule computes a pointer; a later load/store carries independent access obligations. Additional GEP flags may still introduce poison.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-gep"
    ],
    "sourceLocator": "LangRef: Data Layout; getelementptr instruction, offset calculation; GEP FAQ: What is dereferenced by GEP?",
    "sourceNote": "Catalog derivation from the explicit dependsOn premises; the cited source motivates the interface, not this exact editorial theorem name.",
    "provenanceKind": "derived",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  }
]
```
<!-- graph-record:end -->
