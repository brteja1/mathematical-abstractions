# Byte-addressed memory with typed access obligations

A memory state over addressed cells with allocation/lifetime, byte-range accesses and a separate target-dependent value encoding; uninitialized, poison and pointer metadata need explicit cell states.

**Notation:** load(m,R)=decode_T(m|R); store(m,R,v)=m[R←encode_T(v)] on valid ranges

**Stable ID:** `urn:csabs:concept/ByteMemory`

**Categories:** Programming-language semantics → Compiler transformations

**Kind:** semantic-model

**Prerequisites:** [Target-indexed storage and ABI layout](DataLayout.md), [Allocation-associated pointer provenance and lifetime](PointerProvenance.md)

**Related concepts:** [Finite allocated heap store](HeapStore.md), [Exclusive finite-heap separation predicates](HeapSeparation.md), [Scoped atomic execution graph and memory ordering](AtomicMemoryModel.md)

## Backlinks

- [Conservative alias and Mod/Ref query contract](AliasAnalysis.md) — `requiresConcept`
- [Scoped atomic execution graph and memory ordering](AtomicMemoryModel.md) — `relatedConcept`
- [Target-indexed storage and ABI layout](DataLayout.md) — `relatedConcept`
- [Conservative SSA indexing of memory versions](MemorySSA.md) — `relatedConcept`
- [Allocation-associated pointer provenance and lifetime](PointerProvenance.md) — `relatedConcept`
- [Lane-indexed vector execution and inactive-lane policy](PredicatedVectorSemantics.md) — `relatedConcept`
- [Observable state representation relation](StateRepresentation.md) — `relatedConcept`

## Mathematical formulation

A memory state over addressed cells with allocation/lifetime, byte-range accesses and a separate target-dependent value encoding; uninitialized, poison and pointer metadata need explicit cell states. load(m,R)=decode\_T(m|R); store(m,R,v)=m[R←encode\_T(v)] on valid ranges Non-atomic sequential byte memory unless the atomic model is explicitly composed. LLVM memory is untyped: load/store types choose size/alignment/interpretation, not disjoint type regions. Access validity includes live allocation, provenance, byte range and actual alignment. Padding, poison/undef, external pointer state and endianness cannot be replaced by ordinary integer bytes without justification. Volatile count/order is observable. memcpy overlap and memmove overlap have different preconditions; neither is a proof of arbitrary typed-value equality.

**Lean formulation** (in its source module context):

```lean
structure ByteMemory (Address Cell State : Type u) where
  allocated : State → Set Address
  alive : State → Set Address
  contents : State → Address → Cell
  read : State → List Address → List Cell
  readLaw : ∀ s addresses, read s addresses = addresses.map (contents s)
```

**Source:** [`Catalog.LLVM.ByteMemory`](../lean/Catalog/LLVMTransforms.lean); consulted 2026-11-16.

**Scope:** partial

**Interpretation:** Allocation/lifetime sets, cell contents and list-address reads, with readLaw identifying reads with mapped contents.

**Limits:** Lean exposes only the read interface; typed encoding, store/frame, pointer external state, poison bytes, allocation transitions, atomics and volatile semantics remain obligations.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** For an ordinary successful store to range R, every cell outside R is unchanged.; LLVM memory has no intrinsic pointee type; typed access changes size/alignment/interpretation rather than establishing TBAA facts.

**basisKind:** relational-structural-definition

**basisScope:** Non-atomic sequential byte memory unless the atomic model is explicitly composed. LLVM memory is untyped: load/store types choose size/alignment/interpretation, not disjoint type regions. Access validity includes live allocation, provenance, byte range and actual alignment. Padding, poison/undef, external pointer state and endianness cannot be replaced by ordinary integer bytes without justification. Volatile count/order is observable. memcpy overlap and memmove overlap have different preconditions; neither is a proof of arbitrary typed-value equality.

**verificationObligation:** Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.; Lean exposes only the read interface; typed encoding, store/frame, pointer external state, poison bytes, allocation transitions, atomics and volatile semantics remain obligations.

**reviewStatus:** Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-ByteMemory-load"></a>

### load

`urn:csabs:operation/ByteMemory-load`

**signature:** load : Memory×Ptr×Type⇀P(Value)

**description:** Read valid bytes and decode under the target layout and cell semantics.

**precondition:** Full range live, associated and aligned; atomic/volatile policy fixed.

**postcondition:** Read valid bytes and decode under the target layout and cell semantics.

**totality:** Partial/nondeterministic; invalid accesses explicit UB.

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** LangRef: Pointer Aliasing Rules, Object Lifetime, alloca, load, store, memcpy/memmove, volatile memory accesses

**sourceNote:** Adapted Byte-addressed memory with typed access obligations from LangRef: Pointer Aliasing Rules, Object Lifetime, alloca, load, store, memcpy/memmove, volatile memory accesses. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-ByteMemory-store"></a>

### store

`urn:csabs:operation/ByteMemory-store`

**signature:** store : Memory×Ptr×Type×Value⇀P(Memory)

**description:** Encode into the selected range, preserving disjoint cells for ordinary stores.

**precondition:** Valid range/encoding; no concurrent interference in this profile.

**postcondition:** Encode into the selected range, preserving disjoint cells for ordinary stores.

**totality:** Partial/nondeterministic.

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** LangRef: Pointer Aliasing Rules, Object Lifetime, alloca, load, store, memcpy/memmove, volatile memory accesses

**sourceNote:** Adapted Byte-addressed memory with typed access obligations from LangRef: Pointer Aliasing Rules, Object Lifetime, alloca, load, store, memcpy/memmove, volatile memory accesses. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-ByteMemory-range-frame"></a>

### range-frame

`urn:csabs:axiom/ByteMemory-range-frame`

**description:** Defining obligation for Byte-addressed memory with typed access obligations

**statement:** For an ordinary successful store to range R, every cell outside R is unchanged.

**formalStatement:** For an ordinary successful store to range R, every cell outside R is unchanged.

**assumptions:** Non-atomic sequential byte memory unless the atomic model is explicitly composed. LLVM memory is untyped: load/store types choose size/alignment/interpretation, not disjoint type regions. Access validity includes live allocation, provenance, byte range and actual alignment. Padding, poison/undef, external pointer state and endianness cannot be replaced by ordinary integer bytes without justification. Volatile count/order is observable. memcpy overlap and memmove overlap have different preconditions; neither is a proof of arbitrary typed-value equality.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** LangRef: Pointer Aliasing Rules, Object Lifetime, alloca, load, store, memcpy/memmove, volatile memory accesses

**sourceNote:** Adapted Byte-addressed memory with typed access obligations from LangRef: Pointer Aliasing Rules, Object Lifetime, alloca, load, store, memcpy/memmove, volatile memory accesses. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

<a id="node-urn-csabs-axiom-ByteMemory-untyped-access"></a>

### untyped-access

`urn:csabs:axiom/ByteMemory-untyped-access`

**description:** Defining obligation for Byte-addressed memory with typed access obligations

**statement:** LLVM memory has no intrinsic pointee type; typed access changes size/alignment/interpretation rather than establishing TBAA facts.

**formalStatement:** LLVM memory has no intrinsic pointee type; typed access changes size/alignment/interpretation rather than establishing TBAA facts.

**assumptions:** Non-atomic sequential byte memory unless the atomic model is explicitly composed. LLVM memory is untyped: load/store types choose size/alignment/interpretation, not disjoint type regions. Access validity includes live allocation, provenance, byte range and actual alignment. Padding, poison/undef, external pointer state and endianness cannot be replaced by ordinary integer bytes without justification. Volatile count/order is observable. memcpy overlap and memmove overlap have different preconditions; neither is a proof of arbitrary typed-value equality.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** LangRef: Pointer Aliasing Rules, Object Lifetime, alloca, load, store, memcpy/memmove, volatile memory accesses

**sourceNote:** Adapted Byte-addressed memory with typed access obligations from LangRef: Pointer Aliasing Rules, Object Lifetime, alloca, load, store, memcpy/memmove, volatile memory accesses. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

## Laws

<a id="node-urn-csabs-law-ByteMemory-disjoint-byte-frame"></a>

### disjoint-byte-frame

`urn:csabs:law/ByteMemory-disjoint-byte-frame`

**description:** Derived consequence in the stated profile.

**statement:** A store to R preserves a read of disjoint Q when validity/decoding remain unchanged and there are no volatile, atomic or external-state effects.

**formalStatement:** A store to R preserves a read of disjoint Q when validity/decoding remain unchanged and there are no volatile, atomic or external-state effects.

**assumptions:** Non-atomic sequential byte memory unless the atomic model is explicitly composed. LLVM memory is untyped: load/store types choose size/alignment/interpretation, not disjoint type regions. Access validity includes live allocation, provenance, byte range and actual alignment. Padding, poison/undef, external pointer state and endianness cannot be replaced by ordinary integer bytes without justification. Volatile count/order is observable. memcpy overlap and memmove overlap have different preconditions; neither is a proof of arbitrary typed-value equality.

**dependsOn:** [range-frame](ByteMemory.md#node-urn-csabs-axiom-ByteMemory-range-frame)

**proofSketch:** Every addressed cell of Q is outside R, so all cells supplied to the same decoder are unchanged.

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** LangRef: Pointer Aliasing Rules, Object Lifetime, alloca, load, store, memcpy/memmove, volatile memory accesses

**sourceNote:** Catalog derivation from the explicit dependsOn premises; the cited source motivates the interface, not this exact editorial theorem name.

**provenanceKind:** derived

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** LangRef: Pointer Aliasing Rules, Object Lifetime, alloca, load, store, memcpy/memmove, volatile memory accesses

**sourceNote:** Adapted Byte-addressed memory with typed access obligations from LangRef: Pointer Aliasing Rules, Object Lifetime, alloca, load, store, memcpy/memmove, volatile memory accesses. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/ByteMemory",
    "type": "Concept",
    "shortForm": "ByteMemory",
    "fullName": "Byte-addressed memory with typed access obligations",
    "definition": "A memory state over addressed cells with allocation/lifetime, byte-range accesses and a separate target-dependent value encoding; uninitialized, poison and pointer metadata need explicit cell states.",
    "notation": "load(m,R)=decode_T(m|R); store(m,R,v)=m[R←encode_T(v)] on valid ranges",
    "category": [
      "urn:csabs:category/compiler-transformations"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "requiresConcept": [
      "urn:csabs:concept/DataLayout",
      "urn:csabs:concept/PointerProvenance"
    ],
    "relatedConcept": [
      "urn:csabs:concept/HeapStore",
      "urn:csabs:concept/HeapSeparation",
      "urn:csabs:concept/AtomicMemoryModel"
    ],
    "hasOperation": [
      "urn:csabs:operation/ByteMemory-load",
      "urn:csabs:operation/ByteMemory-store"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/ByteMemory-range-frame",
      "urn:csabs:axiom/ByteMemory-untyped-access"
    ],
    "hasLaw": [
      "urn:csabs:law/ByteMemory-disjoint-byte-frame"
    ],
    "hasTheorem": [],
    "basisKind": "relational-structural-definition",
    "basisScope": "Non-atomic sequential byte memory unless the atomic model is explicitly composed. LLVM memory is untyped: load/store types choose size/alignment/interpretation, not disjoint type regions. Access validity includes live allocation, provenance, byte range and actual alignment. Padding, poison/undef, external pointer state and endianness cannot be replaced by ordinary integer bytes without justification. Volatile count/order is observable. memcpy overlap and memmove overlap have different preconditions; neither is a proof of arbitrary typed-value equality.",
    "axiomBasis": "For an ordinary successful store to range R, every cell outside R is unchanged.; LLVM memory has no intrinsic pointee type; typed access changes size/alignment/interpretation rather than establishing TBAA facts.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.",
    "verificationObligation": [
      "Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.",
      "Lean exposes only the read interface; typed encoding, store/frame, pointer external state, poison bytes, allocation transitions, atomics and volatile semantics remain obligations."
    ],
    "source": [
      "urn:csabs:source/compiler-llvm"
    ],
    "sourceLocator": "LangRef: Pointer Aliasing Rules, Object Lifetime, alloca, load, store, memcpy/memmove, volatile memory accesses",
    "sourceNote": "Adapted Byte-addressed memory with typed access obligations from LangRef: Pointer Aliasing Rules, Object Lifetime, alloca, load, store, memcpy/memmove, volatile memory accesses. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "mathematicalFormulation": "A memory state over addressed cells with allocation/lifetime, byte-range accesses and a separate target-dependent value encoding; uninitialized, poison and pointer metadata need explicit cell states. load(m,R)=decode_T(m|R); store(m,R,v)=m[R←encode_T(v)] on valid ranges Non-atomic sequential byte memory unless the atomic model is explicitly composed. LLVM memory is untyped: load/store types choose size/alignment/interpretation, not disjoint type regions. Access validity includes live allocation, provenance, byte range and actual alignment. Padding, poison/undef, external pointer state and endianness cannot be replaced by ordinary integer bytes without justification. Volatile count/order is observable. memcpy overlap and memmove overlap have different preconditions; neither is a proof of arbitrary typed-value equality.",
    "leanFormulation": "structure ByteMemory (Address Cell State : Type u) where\n  allocated : State → Set Address\n  alive : State → Set Address\n  contents : State → Address → Cell\n  read : State → List Address → List Cell\n  readLaw : ∀ s addresses, read s addresses = addresses.map (contents s)",
    "formulationSource": "urn:csabs:source/compiler-llvm-lean",
    "formulationLocator": "Catalog.LLVM.ByteMemory",
    "formulationScope": "partial",
    "leanModelMapping": "Allocation/lifetime sets, cell contents and list-address reads, with readLaw identifying reads with mapped contents.",
    "leanModelLimitations": "Lean exposes only the read interface; typed encoding, store/frame, pointer external state, poison bytes, allocation transitions, atomics and volatile semantics remain obligations."
  },
  {
    "id": "urn:csabs:operation/ByteMemory-load",
    "type": "Operation",
    "name": "load",
    "signature": "load : Memory×Ptr×Type⇀P(Value)",
    "description": "Read valid bytes and decode under the target layout and cell semantics.",
    "concept": "urn:csabs:concept/ByteMemory",
    "precondition": "Full range live, associated and aligned; atomic/volatile policy fixed.",
    "postcondition": "Read valid bytes and decode under the target layout and cell semantics.",
    "totality": "Partial/nondeterministic; invalid accesses explicit UB.",
    "source": [
      "urn:csabs:source/compiler-llvm"
    ],
    "sourceLocator": "LangRef: Pointer Aliasing Rules, Object Lifetime, alloca, load, store, memcpy/memmove, volatile memory accesses",
    "sourceNote": "Adapted Byte-addressed memory with typed access obligations from LangRef: Pointer Aliasing Rules, Object Lifetime, alloca, load, store, memcpy/memmove, volatile memory accesses. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/ByteMemory-store",
    "type": "Operation",
    "name": "store",
    "signature": "store : Memory×Ptr×Type×Value⇀P(Memory)",
    "description": "Encode into the selected range, preserving disjoint cells for ordinary stores.",
    "concept": "urn:csabs:concept/ByteMemory",
    "precondition": "Valid range/encoding; no concurrent interference in this profile.",
    "postcondition": "Encode into the selected range, preserving disjoint cells for ordinary stores.",
    "totality": "Partial/nondeterministic.",
    "source": [
      "urn:csabs:source/compiler-llvm"
    ],
    "sourceLocator": "LangRef: Pointer Aliasing Rules, Object Lifetime, alloca, load, store, memcpy/memmove, volatile memory accesses",
    "sourceNote": "Adapted Byte-addressed memory with typed access obligations from LangRef: Pointer Aliasing Rules, Object Lifetime, alloca, load, store, memcpy/memmove, volatile memory accesses. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/ByteMemory-range-frame",
    "type": "Axiom",
    "name": "range-frame",
    "description": "Defining obligation for Byte-addressed memory with typed access obligations",
    "statement": "For an ordinary successful store to range R, every cell outside R is unchanged.",
    "formalStatement": "For an ordinary successful store to range R, every cell outside R is unchanged.",
    "assumptions": [
      "Non-atomic sequential byte memory unless the atomic model is explicitly composed. LLVM memory is untyped: load/store types choose size/alignment/interpretation, not disjoint type regions. Access validity includes live allocation, provenance, byte range and actual alignment. Padding, poison/undef, external pointer state and endianness cannot be replaced by ordinary integer bytes without justification. Volatile count/order is observable. memcpy overlap and memmove overlap have different preconditions; neither is a proof of arbitrary typed-value equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/ByteMemory"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-llvm"
    ],
    "sourceLocator": "LangRef: Pointer Aliasing Rules, Object Lifetime, alloca, load, store, memcpy/memmove, volatile memory accesses",
    "sourceNote": "Adapted Byte-addressed memory with typed access obligations from LangRef: Pointer Aliasing Rules, Object Lifetime, alloca, load, store, memcpy/memmove, volatile memory accesses. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:axiom/ByteMemory-untyped-access",
    "type": "Axiom",
    "name": "untyped-access",
    "description": "Defining obligation for Byte-addressed memory with typed access obligations",
    "statement": "LLVM memory has no intrinsic pointee type; typed access changes size/alignment/interpretation rather than establishing TBAA facts.",
    "formalStatement": "LLVM memory has no intrinsic pointee type; typed access changes size/alignment/interpretation rather than establishing TBAA facts.",
    "assumptions": [
      "Non-atomic sequential byte memory unless the atomic model is explicitly composed. LLVM memory is untyped: load/store types choose size/alignment/interpretation, not disjoint type regions. Access validity includes live allocation, provenance, byte range and actual alignment. Padding, poison/undef, external pointer state and endianness cannot be replaced by ordinary integer bytes without justification. Volatile count/order is observable. memcpy overlap and memmove overlap have different preconditions; neither is a proof of arbitrary typed-value equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/ByteMemory"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-llvm"
    ],
    "sourceLocator": "LangRef: Pointer Aliasing Rules, Object Lifetime, alloca, load, store, memcpy/memmove, volatile memory accesses",
    "sourceNote": "Adapted Byte-addressed memory with typed access obligations from LangRef: Pointer Aliasing Rules, Object Lifetime, alloca, load, store, memcpy/memmove, volatile memory accesses. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:law/ByteMemory-disjoint-byte-frame",
    "type": "Law",
    "name": "disjoint-byte-frame",
    "description": "Derived consequence in the stated profile.",
    "statement": "A store to R preserves a read of disjoint Q when validity/decoding remain unchanged and there are no volatile, atomic or external-state effects.",
    "formalStatement": "A store to R preserves a read of disjoint Q when validity/decoding remain unchanged and there are no volatile, atomic or external-state effects.",
    "assumptions": [
      "Non-atomic sequential byte memory unless the atomic model is explicitly composed. LLVM memory is untyped: load/store types choose size/alignment/interpretation, not disjoint type regions. Access validity includes live allocation, provenance, byte range and actual alignment. Padding, poison/undef, external pointer state and endianness cannot be replaced by ordinary integer bytes without justification. Volatile count/order is observable. memcpy overlap and memmove overlap have different preconditions; neither is a proof of arbitrary typed-value equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/ByteMemory"
    ],
    "dependsOn": [
      "urn:csabs:axiom/ByteMemory-range-frame"
    ],
    "proofSketch": "Every addressed cell of Q is outside R, so all cells supplied to the same decoder are unchanged.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-llvm"
    ],
    "sourceLocator": "LangRef: Pointer Aliasing Rules, Object Lifetime, alloca, load, store, memcpy/memmove, volatile memory accesses",
    "sourceNote": "Catalog derivation from the explicit dependsOn premises; the cited source motivates the interface, not this exact editorial theorem name.",
    "provenanceKind": "derived",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  }
]
```
<!-- graph-record:end -->
