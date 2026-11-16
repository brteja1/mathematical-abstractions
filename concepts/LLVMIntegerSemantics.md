# LLVM fixed-width integer operations and flags

A versioned integer instruction profile over positive-width bit vectors with signed/unsigned interpretation, modular arithmetic, poison-producing flags and instruction-specific immediate UB.

**Notation:** add_w(x,y)=(x+y) mod 2ʷ; flags add operation-specific definedness constraints

**Stable ID:** `urn:csabs:concept/LLVMIntegerSemantics`

**Categories:** Programming-language semantics → Compiler transformations

**Kind:** semantic-model

**Prerequisites:** [Fixed-width bit vector](BitVector.md), [LLVM scalar deferred undefinedness and freeze](LLVMPoisonSemantics.md)

**Related concepts:** [Scoped induction recurrence and trip-count facts](ScalarRecurrence.md), [Guarded contextual program rewrite](GuardedRewrite.md)

## Backlinks

- [Scoped LLVM attribute, flag and metadata contract](LLVMAttributeContract.md) — `relatedConcept`
- [LLVM scalar deferred undefinedness and freeze](LLVMPoisonSemantics.md) — `relatedConcept`
- [Lane-indexed vector execution and inactive-lane policy](PredicatedVectorSemantics.md) — `requiresConcept`
- [Scoped induction recurrence and trip-count facts](ScalarRecurrence.md) — `requiresConcept`

## Mathematical formulation

A versioned integer instruction profile over positive-width bit vectors with signed/unsigned interpretation, modular arithmetic, poison-producing flags and instruction-specific immediate UB. add\_w(x,y)=(x+y) mod 2ʷ; flags add operation-specific definedness constraints LLVM 21.1.8 scalar iN with N>0; no host C++ overflow semantics. Unflagged add/sub/mul wrap modulo 2^N. nsw/nuw overflow yields poison; exact and shift flags follow each instruction. A shift count ≥N yields poison; integer division by zero and signed division INT\_MIN/-1 are immediate UB. Signed and unsigned comparisons/extensions differ. Undef/poison operands, disjoint/or flags and new cast flags require their instruction clauses. Arithmetic identities are directional refinements under these rules, not unconditional ring identities on all outcomes.

**Lean formulation** (in its source module context):

```lean
structure LLVMIntegerSemantics (Op : Type u) (width : Nat) where
  positiveWidth : 0 < width
  run : Op → BitVec width → BitVec width → Set (IntegerOutcome width)
```

**Source:** [`Catalog.LLVM.LLVMIntegerSemantics`](../lean/Catalog/LLVMTransforms.lean); consulted 2026-11-16.

**Scope:** partial

**Interpretation:** Positive width and client-supplied opcode evaluation to sets of tagged concrete/undef/poison or immediate-UB outcomes.

**Limits:** Lean supplies the typed outcome interface only; it does not implement opcodes, flags, casts, comparisons, undef choices or their arithmetic laws.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** For defined concrete operands, unflagged add/sub/mul are modulo 2^w; their nsw/nuw violations yield poison.; Shift count≥w yields poison; integer division by zero and signed INT_MIN/-1 division are immediate UB; exact flags impose instruction-specific poison conditions.

**basisKind:** relational-structural-definition

**basisScope:** LLVM 21.1.8 scalar iN with N>0; no host C++ overflow semantics. Unflagged add/sub/mul wrap modulo 2^N. nsw/nuw overflow yields poison; exact and shift flags follow each instruction. A shift count ≥N yields poison; integer division by zero and signed division INT_MIN/-1 are immediate UB. Signed and unsigned comparisons/extensions differ. Undef/poison operands, disjoint/or flags and new cast flags require their instruction clauses. Arithmetic identities are directional refinements under these rules, not unconditional ring identities on all outcomes.

**verificationObligation:** Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.; Lean supplies the typed outcome interface only; it does not implement opcodes, flags, casts, comparisons, undef choices or their arithmetic laws.

**reviewStatus:** Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-LLVMIntegerSemantics-evaluate"></a>

### evaluate

`urn:csabs:operation/LLVMIntegerSemantics-evaluate`

**signature:** evaluate : Opcode×Flags×BitVec(w)²→P(Outcome)

**description:** Evaluate the selected instruction with explicit poison and immediate-UB outcomes.

**precondition:** Positive width and opcode-specific flags/types valid.

**postcondition:** Evaluate the selected instruction with explicit poison and immediate-UB outcomes.

**totality:** Outcome relation; division cases explicit UB.

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM IR Undefined Behavior Manual (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** LangRef: add/sub/mul, udiv/sdiv, urem/srem, shl/lshr/ashr, trunc/zext/sext, icmp; UB Manual: Immediate and Deferred UB

**sourceNote:** Adapted LLVM fixed-width integer operations and flags from LangRef: add/sub/mul, udiv/sdiv, urem/srem, shl/lshr/ashr, trunc/zext/sext, icmp; UB Manual: Immediate and Deferred UB. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-LLVMIntegerSemantics-interpret"></a>

### interpret

`urn:csabs:operation/LLVMIntegerSemantics-interpret`

**signature:** interpret : {signed,unsigned}×BitVec(w)→ℤ

**description:** Choose two-complement signed or unsigned integer interpretation.

**precondition:** w>0.

**postcondition:** Choose two-complement signed or unsigned integer interpretation.

**totality:** Total function.

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM IR Undefined Behavior Manual (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** LangRef: add/sub/mul, udiv/sdiv, urem/srem, shl/lshr/ashr, trunc/zext/sext, icmp; UB Manual: Immediate and Deferred UB

**sourceNote:** Adapted LLVM fixed-width integer operations and flags from LangRef: add/sub/mul, udiv/sdiv, urem/srem, shl/lshr/ashr, trunc/zext/sext, icmp; UB Manual: Immediate and Deferred UB. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-LLVMIntegerSemantics-modular-arithmetic"></a>

### modular-arithmetic

`urn:csabs:axiom/LLVMIntegerSemantics-modular-arithmetic`

**description:** Defining obligation for LLVM fixed-width integer operations and flags

**statement:** For defined concrete operands, unflagged add/sub/mul are modulo 2^w; their nsw/nuw violations yield poison.

**formalStatement:** For defined concrete operands, unflagged add/sub/mul are modulo 2^w; their nsw/nuw violations yield poison.

**assumptions:** LLVM 21.1.8 scalar iN with N>0; no host C++ overflow semantics. Unflagged add/sub/mul wrap modulo 2^N. nsw/nuw overflow yields poison; exact and shift flags follow each instruction. A shift count ≥N yields poison; integer division by zero and signed division INT_MIN/-1 are immediate UB. Signed and unsigned comparisons/extensions differ. Undef/poison operands, disjoint/or flags and new cast flags require their instruction clauses. Arithmetic identities are directional refinements under these rules, not unconditional ring identities on all outcomes.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM IR Undefined Behavior Manual (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** LangRef: add/sub/mul, udiv/sdiv, urem/srem, shl/lshr/ashr, trunc/zext/sext, icmp; UB Manual: Immediate and Deferred UB

**sourceNote:** Adapted LLVM fixed-width integer operations and flags from LangRef: add/sub/mul, udiv/sdiv, urem/srem, shl/lshr/ashr, trunc/zext/sext, icmp; UB Manual: Immediate and Deferred UB. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

<a id="node-urn-csabs-axiom-LLVMIntegerSemantics-exceptional-cases"></a>

### exceptional-cases

`urn:csabs:axiom/LLVMIntegerSemantics-exceptional-cases`

**description:** Defining obligation for LLVM fixed-width integer operations and flags

**statement:** Shift count≥w yields poison; integer division by zero and signed INT_MIN/-1 division are immediate UB; exact flags impose instruction-specific poison conditions.

**formalStatement:** Shift count≥w yields poison; integer division by zero and signed INT_MIN/-1 division are immediate UB; exact flags impose instruction-specific poison conditions.

**assumptions:** LLVM 21.1.8 scalar iN with N>0; no host C++ overflow semantics. Unflagged add/sub/mul wrap modulo 2^N. nsw/nuw overflow yields poison; exact and shift flags follow each instruction. A shift count ≥N yields poison; integer division by zero and signed division INT_MIN/-1 are immediate UB. Signed and unsigned comparisons/extensions differ. Undef/poison operands, disjoint/or flags and new cast flags require their instruction clauses. Arithmetic identities are directional refinements under these rules, not unconditional ring identities on all outcomes.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM IR Undefined Behavior Manual (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** LangRef: add/sub/mul, udiv/sdiv, urem/srem, shl/lshr/ashr, trunc/zext/sext, icmp; UB Manual: Immediate and Deferred UB

**sourceNote:** Adapted LLVM fixed-width integer operations and flags from LangRef: add/sub/mul, udiv/sdiv, urem/srem, shl/lshr/ashr, trunc/zext/sext, icmp; UB Manual: Immediate and Deferred UB. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

## Laws

<a id="node-urn-csabs-law-LLVMIntegerSemantics-add-zero-concrete"></a>

### add-zero-concrete

`urn:csabs:law/LLVMIntegerSemantics-add-zero-concrete`

**description:** Derived consequence in the stated profile.

**statement:** For concrete x and unflagged addition, add_w(x,0)=x.

**formalStatement:** For concrete x and unflagged addition, add_w(x,0)=x.

**assumptions:** LLVM 21.1.8 scalar iN with N>0; no host C++ overflow semantics. Unflagged add/sub/mul wrap modulo 2^N. nsw/nuw overflow yields poison; exact and shift flags follow each instruction. A shift count ≥N yields poison; integer division by zero and signed division INT_MIN/-1 are immediate UB. Signed and unsigned comparisons/extensions differ. Undef/poison operands, disjoint/or flags and new cast flags require their instruction clauses. Arithmetic identities are directional refinements under these rules, not unconditional ring identities on all outcomes.

**dependsOn:** [modular-arithmetic](LLVMIntegerSemantics.md#node-urn-csabs-axiom-LLVMIntegerSemantics-modular-arithmetic)

**proofSketch:** x already represents a residue modulo 2^w; adding zero leaves that residue. This statement is scoped to concrete operands.

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM IR Undefined Behavior Manual (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** LangRef: add/sub/mul, udiv/sdiv, urem/srem, shl/lshr/ashr, trunc/zext/sext, icmp; UB Manual: Immediate and Deferred UB

**sourceNote:** Catalog derivation from the explicit dependsOn premises; the cited source motivates the interface, not this exact editorial theorem name.

**provenanceKind:** derived

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification
- [LLVM IR Undefined Behavior Manual (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** LangRef: add/sub/mul, udiv/sdiv, urem/srem, shl/lshr/ashr, trunc/zext/sext, icmp; UB Manual: Immediate and Deferred UB

**sourceNote:** Adapted LLVM fixed-width integer operations and flags from LangRef: add/sub/mul, udiv/sdiv, urem/srem, shl/lshr/ashr, trunc/zext/sext, icmp; UB Manual: Immediate and Deferred UB. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/LLVMIntegerSemantics",
    "type": "Concept",
    "shortForm": "LLVMIntegerSemantics",
    "fullName": "LLVM fixed-width integer operations and flags",
    "definition": "A versioned integer instruction profile over positive-width bit vectors with signed/unsigned interpretation, modular arithmetic, poison-producing flags and instruction-specific immediate UB.",
    "notation": "add_w(x,y)=(x+y) mod 2ʷ; flags add operation-specific definedness constraints",
    "category": [
      "urn:csabs:category/compiler-transformations"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "requiresConcept": [
      "urn:csabs:concept/BitVector",
      "urn:csabs:concept/LLVMPoisonSemantics"
    ],
    "relatedConcept": [
      "urn:csabs:concept/ScalarRecurrence",
      "urn:csabs:concept/GuardedRewrite"
    ],
    "hasOperation": [
      "urn:csabs:operation/LLVMIntegerSemantics-evaluate",
      "urn:csabs:operation/LLVMIntegerSemantics-interpret"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/LLVMIntegerSemantics-modular-arithmetic",
      "urn:csabs:axiom/LLVMIntegerSemantics-exceptional-cases"
    ],
    "hasLaw": [
      "urn:csabs:law/LLVMIntegerSemantics-add-zero-concrete"
    ],
    "hasTheorem": [],
    "basisKind": "relational-structural-definition",
    "basisScope": "LLVM 21.1.8 scalar iN with N>0; no host C++ overflow semantics. Unflagged add/sub/mul wrap modulo 2^N. nsw/nuw overflow yields poison; exact and shift flags follow each instruction. A shift count ≥N yields poison; integer division by zero and signed division INT_MIN/-1 are immediate UB. Signed and unsigned comparisons/extensions differ. Undef/poison operands, disjoint/or flags and new cast flags require their instruction clauses. Arithmetic identities are directional refinements under these rules, not unconditional ring identities on all outcomes.",
    "axiomBasis": "For defined concrete operands, unflagged add/sub/mul are modulo 2^w; their nsw/nuw violations yield poison.; Shift count≥w yields poison; integer division by zero and signed INT_MIN/-1 division are immediate UB; exact flags impose instruction-specific poison conditions.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.",
    "verificationObligation": [
      "Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.",
      "Lean supplies the typed outcome interface only; it does not implement opcodes, flags, casts, comparisons, undef choices or their arithmetic laws."
    ],
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-ub"
    ],
    "sourceLocator": "LangRef: add/sub/mul, udiv/sdiv, urem/srem, shl/lshr/ashr, trunc/zext/sext, icmp; UB Manual: Immediate and Deferred UB",
    "sourceNote": "Adapted LLVM fixed-width integer operations and flags from LangRef: add/sub/mul, udiv/sdiv, urem/srem, shl/lshr/ashr, trunc/zext/sext, icmp; UB Manual: Immediate and Deferred UB. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "mathematicalFormulation": "A versioned integer instruction profile over positive-width bit vectors with signed/unsigned interpretation, modular arithmetic, poison-producing flags and instruction-specific immediate UB. add_w(x,y)=(x+y) mod 2ʷ; flags add operation-specific definedness constraints LLVM 21.1.8 scalar iN with N>0; no host C++ overflow semantics. Unflagged add/sub/mul wrap modulo 2^N. nsw/nuw overflow yields poison; exact and shift flags follow each instruction. A shift count ≥N yields poison; integer division by zero and signed division INT_MIN/-1 are immediate UB. Signed and unsigned comparisons/extensions differ. Undef/poison operands, disjoint/or flags and new cast flags require their instruction clauses. Arithmetic identities are directional refinements under these rules, not unconditional ring identities on all outcomes.",
    "leanFormulation": "structure LLVMIntegerSemantics (Op : Type u) (width : Nat) where\n  positiveWidth : 0 < width\n  run : Op → BitVec width → BitVec width → Set (IntegerOutcome width)",
    "formulationSource": "urn:csabs:source/compiler-llvm-lean",
    "formulationLocator": "Catalog.LLVM.LLVMIntegerSemantics",
    "formulationScope": "partial",
    "leanModelMapping": "Positive width and client-supplied opcode evaluation to sets of tagged concrete/undef/poison or immediate-UB outcomes.",
    "leanModelLimitations": "Lean supplies the typed outcome interface only; it does not implement opcodes, flags, casts, comparisons, undef choices or their arithmetic laws."
  },
  {
    "id": "urn:csabs:operation/LLVMIntegerSemantics-evaluate",
    "type": "Operation",
    "name": "evaluate",
    "signature": "evaluate : Opcode×Flags×BitVec(w)²→P(Outcome)",
    "description": "Evaluate the selected instruction with explicit poison and immediate-UB outcomes.",
    "concept": "urn:csabs:concept/LLVMIntegerSemantics",
    "precondition": "Positive width and opcode-specific flags/types valid.",
    "postcondition": "Evaluate the selected instruction with explicit poison and immediate-UB outcomes.",
    "totality": "Outcome relation; division cases explicit UB.",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-ub"
    ],
    "sourceLocator": "LangRef: add/sub/mul, udiv/sdiv, urem/srem, shl/lshr/ashr, trunc/zext/sext, icmp; UB Manual: Immediate and Deferred UB",
    "sourceNote": "Adapted LLVM fixed-width integer operations and flags from LangRef: add/sub/mul, udiv/sdiv, urem/srem, shl/lshr/ashr, trunc/zext/sext, icmp; UB Manual: Immediate and Deferred UB. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/LLVMIntegerSemantics-interpret",
    "type": "Operation",
    "name": "interpret",
    "signature": "interpret : {signed,unsigned}×BitVec(w)→ℤ",
    "description": "Choose two-complement signed or unsigned integer interpretation.",
    "concept": "urn:csabs:concept/LLVMIntegerSemantics",
    "precondition": "w>0.",
    "postcondition": "Choose two-complement signed or unsigned integer interpretation.",
    "totality": "Total function.",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-ub"
    ],
    "sourceLocator": "LangRef: add/sub/mul, udiv/sdiv, urem/srem, shl/lshr/ashr, trunc/zext/sext, icmp; UB Manual: Immediate and Deferred UB",
    "sourceNote": "Adapted LLVM fixed-width integer operations and flags from LangRef: add/sub/mul, udiv/sdiv, urem/srem, shl/lshr/ashr, trunc/zext/sext, icmp; UB Manual: Immediate and Deferred UB. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/LLVMIntegerSemantics-modular-arithmetic",
    "type": "Axiom",
    "name": "modular-arithmetic",
    "description": "Defining obligation for LLVM fixed-width integer operations and flags",
    "statement": "For defined concrete operands, unflagged add/sub/mul are modulo 2^w; their nsw/nuw violations yield poison.",
    "formalStatement": "For defined concrete operands, unflagged add/sub/mul are modulo 2^w; their nsw/nuw violations yield poison.",
    "assumptions": [
      "LLVM 21.1.8 scalar iN with N>0; no host C++ overflow semantics. Unflagged add/sub/mul wrap modulo 2^N. nsw/nuw overflow yields poison; exact and shift flags follow each instruction. A shift count ≥N yields poison; integer division by zero and signed division INT_MIN/-1 are immediate UB. Signed and unsigned comparisons/extensions differ. Undef/poison operands, disjoint/or flags and new cast flags require their instruction clauses. Arithmetic identities are directional refinements under these rules, not unconditional ring identities on all outcomes."
    ],
    "appliesTo": [
      "urn:csabs:concept/LLVMIntegerSemantics"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-ub"
    ],
    "sourceLocator": "LangRef: add/sub/mul, udiv/sdiv, urem/srem, shl/lshr/ashr, trunc/zext/sext, icmp; UB Manual: Immediate and Deferred UB",
    "sourceNote": "Adapted LLVM fixed-width integer operations and flags from LangRef: add/sub/mul, udiv/sdiv, urem/srem, shl/lshr/ashr, trunc/zext/sext, icmp; UB Manual: Immediate and Deferred UB. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:axiom/LLVMIntegerSemantics-exceptional-cases",
    "type": "Axiom",
    "name": "exceptional-cases",
    "description": "Defining obligation for LLVM fixed-width integer operations and flags",
    "statement": "Shift count≥w yields poison; integer division by zero and signed INT_MIN/-1 division are immediate UB; exact flags impose instruction-specific poison conditions.",
    "formalStatement": "Shift count≥w yields poison; integer division by zero and signed INT_MIN/-1 division are immediate UB; exact flags impose instruction-specific poison conditions.",
    "assumptions": [
      "LLVM 21.1.8 scalar iN with N>0; no host C++ overflow semantics. Unflagged add/sub/mul wrap modulo 2^N. nsw/nuw overflow yields poison; exact and shift flags follow each instruction. A shift count ≥N yields poison; integer division by zero and signed division INT_MIN/-1 are immediate UB. Signed and unsigned comparisons/extensions differ. Undef/poison operands, disjoint/or flags and new cast flags require their instruction clauses. Arithmetic identities are directional refinements under these rules, not unconditional ring identities on all outcomes."
    ],
    "appliesTo": [
      "urn:csabs:concept/LLVMIntegerSemantics"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-ub"
    ],
    "sourceLocator": "LangRef: add/sub/mul, udiv/sdiv, urem/srem, shl/lshr/ashr, trunc/zext/sext, icmp; UB Manual: Immediate and Deferred UB",
    "sourceNote": "Adapted LLVM fixed-width integer operations and flags from LangRef: add/sub/mul, udiv/sdiv, urem/srem, shl/lshr/ashr, trunc/zext/sext, icmp; UB Manual: Immediate and Deferred UB. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:law/LLVMIntegerSemantics-add-zero-concrete",
    "type": "Law",
    "name": "add-zero-concrete",
    "description": "Derived consequence in the stated profile.",
    "statement": "For concrete x and unflagged addition, add_w(x,0)=x.",
    "formalStatement": "For concrete x and unflagged addition, add_w(x,0)=x.",
    "assumptions": [
      "LLVM 21.1.8 scalar iN with N>0; no host C++ overflow semantics. Unflagged add/sub/mul wrap modulo 2^N. nsw/nuw overflow yields poison; exact and shift flags follow each instruction. A shift count ≥N yields poison; integer division by zero and signed division INT_MIN/-1 are immediate UB. Signed and unsigned comparisons/extensions differ. Undef/poison operands, disjoint/or flags and new cast flags require their instruction clauses. Arithmetic identities are directional refinements under these rules, not unconditional ring identities on all outcomes."
    ],
    "appliesTo": [
      "urn:csabs:concept/LLVMIntegerSemantics"
    ],
    "dependsOn": [
      "urn:csabs:axiom/LLVMIntegerSemantics-modular-arithmetic"
    ],
    "proofSketch": "x already represents a residue modulo 2^w; adding zero leaves that residue. This statement is scoped to concrete operands.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-ub"
    ],
    "sourceLocator": "LangRef: add/sub/mul, udiv/sdiv, urem/srem, shl/lshr/ashr, trunc/zext/sext, icmp; UB Manual: Immediate and Deferred UB",
    "sourceNote": "Catalog derivation from the explicit dependsOn premises; the cited source motivates the interface, not this exact editorial theorem name.",
    "provenanceKind": "derived",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  }
]
```
<!-- graph-record:end -->
