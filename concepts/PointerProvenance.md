# Allocation-associated pointer provenance and lifetime

A pointer interpretation retaining allocation/address-space associations and derivation separately from numeric address bits, with lifetime and dereferenceability checked at access time.

**Notation:** associated:Ptr→P(Object); basedOn(p,q)⇒associated(q)⊆associated(p)

**Stable ID:** `urn:csabs:concept/PointerProvenance`

**Categories:** Programming-language semantics → Compiler transformations

**Kind:** semantic-model

**Prerequisites:** [Binary relation](Relation.md), [Target-indexed storage and ABI layout](DataLayout.md)

**Related concepts:** [Byte-addressed memory with typed access obligations](ByteMemory.md), [Conservative alias and Mod/Ref query contract](AliasAnalysis.md), [LLVM scalar deferred undefinedness and freeze](LLVMPoisonSemantics.md)

## Backlinks

- [Byte-addressed memory with typed access obligations](ByteMemory.md) — `requiresConcept`
- [Target-indexed storage and ABI layout](DataLayout.md) — `relatedConcept`
- [LLVM scalar deferred undefinedness and freeze](LLVMPoisonSemantics.md) — `relatedConcept`

## Mathematical formulation

A pointer interpretation retaining allocation/address-space associations and derivation separately from numeric address bits, with lifetime and dereferenceability checked at access time. associated:Ptr→P(Object); basedOn(p,q)⇒associated(q)⊆associated(p) LLVM 21.1.8 allocation-associated scalar pointers. Address equality alone does not supply provenance, dereferenceability or lifetime. GEP and bitcast retain relevant base associations; integer-derived pointers use the specified contributors, not arbitrary algebra on addresses. basedOn is transitive. Out-of-object addresses can be computed without granting access. Non-integral casts may depend on external state and must not be freely introduced. This model does not assume every pointer has exactly one allocation owner.

**Lean formulation** (in its source module context):

```lean
structure PointerProvenance (Ptr Object : Type u) where
  associated : Ptr → Set Object
  basedOn : Ptr → Ptr → Prop
  preservesAssociation : ∀ p q, basedOn p q → associated q ⊆ associated p
```

**Source:** [`Catalog.LLVM.PointerProvenance`](../lean/Catalog/LLVMTransforms.lean); consulted 2026-11-16.

**Scope:** partial

**Interpretation:** Pointer-to-object association sets and basedOn relation with an explicit association-preservation law.

**Limits:** No complete LLVM pointer model, capture analysis, allocation/lifetime transition system or non-integral external-state semantics; offset/address equality are not modeled in Lean.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** basedOn(p,q) ⇒ associated(q)⊆associated(p); basedOn is transitive.; A dereference requires live associated storage covering the whole accessed range; numeric address equality alone does not establish this.

**basisKind:** relational-structural-definition

**basisScope:** LLVM 21.1.8 allocation-associated scalar pointers. Address equality alone does not supply provenance, dereferenceability or lifetime. GEP and bitcast retain relevant base associations; integer-derived pointers use the specified contributors, not arbitrary algebra on addresses. basedOn is transitive. Out-of-object addresses can be computed without granting access. Non-integral casts may depend on external state and must not be freely introduced. This model does not assume every pointer has exactly one allocation owner.

**verificationObligation:** Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.; No complete LLVM pointer model, capture analysis, allocation/lifetime transition system or non-integral external-state semantics; offset/address equality are not modeled in Lean.

**reviewStatus:** Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-PointerProvenance-derive"></a>

### derive

`urn:csabs:operation/PointerProvenance-derive`

**signature:** derive : Ptr×Offset→Ptr

**description:** Derive an address retaining required associations and address-space rules.

**precondition:** Offset layout and GEP flags justified.

**postcondition:** Derive an address retaining required associations and address-space rules.

**totality:** Definedness depends on operation flags.

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM getelementptr FAQ (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/GetElementPtr.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/GetElementPtr.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** LangRef: Non-Integral Pointer Type, Object Lifetime, Pointer Aliasing Rules, Pointer Capture; GEP FAQ

**sourceNote:** Adapted Allocation-associated pointer provenance and lifetime from LangRef: Non-Integral Pointer Type, Object Lifetime, Pointer Aliasing Rules, Pointer Capture; GEP FAQ. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-PointerProvenance-can-access"></a>

### can-access

`urn:csabs:operation/PointerProvenance-can-access`

**signature:** canAccess : State×Ptr×Size×Alignment→Prop

**description:** Require association, live storage, valid byte range and alignment at the access.

**precondition:** Target and null/address-space rules fixed.

**postcondition:** Require association, live storage, valid byte range and alignment at the access.

**totality:** Total predicate; failed access may cause UB.

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM getelementptr FAQ (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/GetElementPtr.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/GetElementPtr.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** LangRef: Non-Integral Pointer Type, Object Lifetime, Pointer Aliasing Rules, Pointer Capture; GEP FAQ

**sourceNote:** Adapted Allocation-associated pointer provenance and lifetime from LangRef: Non-Integral Pointer Type, Object Lifetime, Pointer Aliasing Rules, Pointer Capture; GEP FAQ. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-PointerProvenance-association"></a>

### association

`urn:csabs:axiom/PointerProvenance-association`

**description:** Defining obligation for Allocation-associated pointer provenance and lifetime

**statement:** basedOn(p,q) ⇒ associated(q)⊆associated(p); basedOn is transitive.

**formalStatement:** basedOn(p,q) ⇒ associated(q)⊆associated(p); basedOn is transitive.

**assumptions:** LLVM 21.1.8 allocation-associated scalar pointers. Address equality alone does not supply provenance, dereferenceability or lifetime. GEP and bitcast retain relevant base associations; integer-derived pointers use the specified contributors, not arbitrary algebra on addresses. basedOn is transitive. Out-of-object addresses can be computed without granting access. Non-integral casts may depend on external state and must not be freely introduced. This model does not assume every pointer has exactly one allocation owner.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM getelementptr FAQ (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/GetElementPtr.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/GetElementPtr.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** LangRef: Non-Integral Pointer Type, Object Lifetime, Pointer Aliasing Rules, Pointer Capture; GEP FAQ

**sourceNote:** Adapted Allocation-associated pointer provenance and lifetime from LangRef: Non-Integral Pointer Type, Object Lifetime, Pointer Aliasing Rules, Pointer Capture; GEP FAQ. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

<a id="node-urn-csabs-axiom-PointerProvenance-access-lifetime"></a>

### access-lifetime

`urn:csabs:axiom/PointerProvenance-access-lifetime`

**description:** Defining obligation for Allocation-associated pointer provenance and lifetime

**statement:** A dereference requires live associated storage covering the whole accessed range; numeric address equality alone does not establish this.

**formalStatement:** A dereference requires live associated storage covering the whole accessed range; numeric address equality alone does not establish this.

**assumptions:** LLVM 21.1.8 allocation-associated scalar pointers. Address equality alone does not supply provenance, dereferenceability or lifetime. GEP and bitcast retain relevant base associations; integer-derived pointers use the specified contributors, not arbitrary algebra on addresses. basedOn is transitive. Out-of-object addresses can be computed without granting access. Non-integral casts may depend on external state and must not be freely introduced. This model does not assume every pointer has exactly one allocation owner.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM getelementptr FAQ (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/GetElementPtr.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/GetElementPtr.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** LangRef: Non-Integral Pointer Type, Object Lifetime, Pointer Aliasing Rules, Pointer Capture; GEP FAQ

**sourceNote:** Adapted Allocation-associated pointer provenance and lifetime from LangRef: Non-Integral Pointer Type, Object Lifetime, Pointer Aliasing Rules, Pointer Capture; GEP FAQ. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

## Laws

<a id="node-urn-csabs-law-PointerProvenance-same-address-insufficient"></a>

### same-address-insufficient

`urn:csabs:law/PointerProvenance-same-address-insufficient`

**description:** Derived consequence in the stated profile.

**statement:** From equal numeric addresses alone one cannot conclude the canAccess precondition.

**formalStatement:** From equal numeric addresses alone one cannot conclude the canAccess precondition.

**assumptions:** LLVM 21.1.8 allocation-associated scalar pointers. Address equality alone does not supply provenance, dereferenceability or lifetime. GEP and bitcast retain relevant base associations; integer-derived pointers use the specified contributors, not arbitrary algebra on addresses. basedOn is transitive. Out-of-object addresses can be computed without granting access. Non-integral casts may depend on external state and must not be freely introduced. This model does not assume every pointer has exactly one allocation owner.

**dependsOn:** [access-lifetime](PointerProvenance.md#node-urn-csabs-axiom-PointerProvenance-access-lifetime)

**proofSketch:** The access rule additionally requires association and live storage; address equality supplies neither premise.

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM getelementptr FAQ (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/GetElementPtr.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/GetElementPtr.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** LangRef: Non-Integral Pointer Type, Object Lifetime, Pointer Aliasing Rules, Pointer Capture; GEP FAQ

**sourceNote:** Catalog derivation from the explicit dependsOn premises; the cited source motivates the interface, not this exact editorial theorem name.

**provenanceKind:** derived

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification
- [LLVM getelementptr FAQ (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/GetElementPtr.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/GetElementPtr.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** LangRef: Non-Integral Pointer Type, Object Lifetime, Pointer Aliasing Rules, Pointer Capture; GEP FAQ

**sourceNote:** Adapted Allocation-associated pointer provenance and lifetime from LangRef: Non-Integral Pointer Type, Object Lifetime, Pointer Aliasing Rules, Pointer Capture; GEP FAQ. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/PointerProvenance",
    "type": "Concept",
    "shortForm": "PointerProvenance",
    "fullName": "Allocation-associated pointer provenance and lifetime",
    "definition": "A pointer interpretation retaining allocation/address-space associations and derivation separately from numeric address bits, with lifetime and dereferenceability checked at access time.",
    "notation": "associated:Ptr→P(Object); basedOn(p,q)⇒associated(q)⊆associated(p)",
    "category": [
      "urn:csabs:category/compiler-transformations"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "requiresConcept": [
      "urn:csabs:concept/Relation",
      "urn:csabs:concept/DataLayout"
    ],
    "relatedConcept": [
      "urn:csabs:concept/ByteMemory",
      "urn:csabs:concept/AliasAnalysis",
      "urn:csabs:concept/LLVMPoisonSemantics"
    ],
    "hasOperation": [
      "urn:csabs:operation/PointerProvenance-derive",
      "urn:csabs:operation/PointerProvenance-can-access"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/PointerProvenance-association",
      "urn:csabs:axiom/PointerProvenance-access-lifetime"
    ],
    "hasLaw": [
      "urn:csabs:law/PointerProvenance-same-address-insufficient"
    ],
    "hasTheorem": [],
    "basisKind": "relational-structural-definition",
    "basisScope": "LLVM 21.1.8 allocation-associated scalar pointers. Address equality alone does not supply provenance, dereferenceability or lifetime. GEP and bitcast retain relevant base associations; integer-derived pointers use the specified contributors, not arbitrary algebra on addresses. basedOn is transitive. Out-of-object addresses can be computed without granting access. Non-integral casts may depend on external state and must not be freely introduced. This model does not assume every pointer has exactly one allocation owner.",
    "axiomBasis": "basedOn(p,q) ⇒ associated(q)⊆associated(p); basedOn is transitive.; A dereference requires live associated storage covering the whole accessed range; numeric address equality alone does not establish this.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.",
    "verificationObligation": [
      "Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.",
      "No complete LLVM pointer model, capture analysis, allocation/lifetime transition system or non-integral external-state semantics; offset/address equality are not modeled in Lean."
    ],
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-gep"
    ],
    "sourceLocator": "LangRef: Non-Integral Pointer Type, Object Lifetime, Pointer Aliasing Rules, Pointer Capture; GEP FAQ",
    "sourceNote": "Adapted Allocation-associated pointer provenance and lifetime from LangRef: Non-Integral Pointer Type, Object Lifetime, Pointer Aliasing Rules, Pointer Capture; GEP FAQ. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "mathematicalFormulation": "A pointer interpretation retaining allocation/address-space associations and derivation separately from numeric address bits, with lifetime and dereferenceability checked at access time. associated:Ptr→P(Object); basedOn(p,q)⇒associated(q)⊆associated(p) LLVM 21.1.8 allocation-associated scalar pointers. Address equality alone does not supply provenance, dereferenceability or lifetime. GEP and bitcast retain relevant base associations; integer-derived pointers use the specified contributors, not arbitrary algebra on addresses. basedOn is transitive. Out-of-object addresses can be computed without granting access. Non-integral casts may depend on external state and must not be freely introduced. This model does not assume every pointer has exactly one allocation owner.",
    "leanFormulation": "structure PointerProvenance (Ptr Object : Type u) where\n  associated : Ptr → Set Object\n  basedOn : Ptr → Ptr → Prop\n  preservesAssociation : ∀ p q, basedOn p q → associated q ⊆ associated p",
    "formulationSource": "urn:csabs:source/compiler-llvm-lean",
    "formulationLocator": "Catalog.LLVM.PointerProvenance",
    "formulationScope": "partial",
    "leanModelMapping": "Pointer-to-object association sets and basedOn relation with an explicit association-preservation law.",
    "leanModelLimitations": "No complete LLVM pointer model, capture analysis, allocation/lifetime transition system or non-integral external-state semantics; offset/address equality are not modeled in Lean."
  },
  {
    "id": "urn:csabs:operation/PointerProvenance-derive",
    "type": "Operation",
    "name": "derive",
    "signature": "derive : Ptr×Offset→Ptr",
    "description": "Derive an address retaining required associations and address-space rules.",
    "concept": "urn:csabs:concept/PointerProvenance",
    "precondition": "Offset layout and GEP flags justified.",
    "postcondition": "Derive an address retaining required associations and address-space rules.",
    "totality": "Definedness depends on operation flags.",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-gep"
    ],
    "sourceLocator": "LangRef: Non-Integral Pointer Type, Object Lifetime, Pointer Aliasing Rules, Pointer Capture; GEP FAQ",
    "sourceNote": "Adapted Allocation-associated pointer provenance and lifetime from LangRef: Non-Integral Pointer Type, Object Lifetime, Pointer Aliasing Rules, Pointer Capture; GEP FAQ. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/PointerProvenance-can-access",
    "type": "Operation",
    "name": "can-access",
    "signature": "canAccess : State×Ptr×Size×Alignment→Prop",
    "description": "Require association, live storage, valid byte range and alignment at the access.",
    "concept": "urn:csabs:concept/PointerProvenance",
    "precondition": "Target and null/address-space rules fixed.",
    "postcondition": "Require association, live storage, valid byte range and alignment at the access.",
    "totality": "Total predicate; failed access may cause UB.",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-gep"
    ],
    "sourceLocator": "LangRef: Non-Integral Pointer Type, Object Lifetime, Pointer Aliasing Rules, Pointer Capture; GEP FAQ",
    "sourceNote": "Adapted Allocation-associated pointer provenance and lifetime from LangRef: Non-Integral Pointer Type, Object Lifetime, Pointer Aliasing Rules, Pointer Capture; GEP FAQ. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/PointerProvenance-association",
    "type": "Axiom",
    "name": "association",
    "description": "Defining obligation for Allocation-associated pointer provenance and lifetime",
    "statement": "basedOn(p,q) ⇒ associated(q)⊆associated(p); basedOn is transitive.",
    "formalStatement": "basedOn(p,q) ⇒ associated(q)⊆associated(p); basedOn is transitive.",
    "assumptions": [
      "LLVM 21.1.8 allocation-associated scalar pointers. Address equality alone does not supply provenance, dereferenceability or lifetime. GEP and bitcast retain relevant base associations; integer-derived pointers use the specified contributors, not arbitrary algebra on addresses. basedOn is transitive. Out-of-object addresses can be computed without granting access. Non-integral casts may depend on external state and must not be freely introduced. This model does not assume every pointer has exactly one allocation owner."
    ],
    "appliesTo": [
      "urn:csabs:concept/PointerProvenance"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-gep"
    ],
    "sourceLocator": "LangRef: Non-Integral Pointer Type, Object Lifetime, Pointer Aliasing Rules, Pointer Capture; GEP FAQ",
    "sourceNote": "Adapted Allocation-associated pointer provenance and lifetime from LangRef: Non-Integral Pointer Type, Object Lifetime, Pointer Aliasing Rules, Pointer Capture; GEP FAQ. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:axiom/PointerProvenance-access-lifetime",
    "type": "Axiom",
    "name": "access-lifetime",
    "description": "Defining obligation for Allocation-associated pointer provenance and lifetime",
    "statement": "A dereference requires live associated storage covering the whole accessed range; numeric address equality alone does not establish this.",
    "formalStatement": "A dereference requires live associated storage covering the whole accessed range; numeric address equality alone does not establish this.",
    "assumptions": [
      "LLVM 21.1.8 allocation-associated scalar pointers. Address equality alone does not supply provenance, dereferenceability or lifetime. GEP and bitcast retain relevant base associations; integer-derived pointers use the specified contributors, not arbitrary algebra on addresses. basedOn is transitive. Out-of-object addresses can be computed without granting access. Non-integral casts may depend on external state and must not be freely introduced. This model does not assume every pointer has exactly one allocation owner."
    ],
    "appliesTo": [
      "urn:csabs:concept/PointerProvenance"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-gep"
    ],
    "sourceLocator": "LangRef: Non-Integral Pointer Type, Object Lifetime, Pointer Aliasing Rules, Pointer Capture; GEP FAQ",
    "sourceNote": "Adapted Allocation-associated pointer provenance and lifetime from LangRef: Non-Integral Pointer Type, Object Lifetime, Pointer Aliasing Rules, Pointer Capture; GEP FAQ. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:law/PointerProvenance-same-address-insufficient",
    "type": "Law",
    "name": "same-address-insufficient",
    "description": "Derived consequence in the stated profile.",
    "statement": "From equal numeric addresses alone one cannot conclude the canAccess precondition.",
    "formalStatement": "From equal numeric addresses alone one cannot conclude the canAccess precondition.",
    "assumptions": [
      "LLVM 21.1.8 allocation-associated scalar pointers. Address equality alone does not supply provenance, dereferenceability or lifetime. GEP and bitcast retain relevant base associations; integer-derived pointers use the specified contributors, not arbitrary algebra on addresses. basedOn is transitive. Out-of-object addresses can be computed without granting access. Non-integral casts may depend on external state and must not be freely introduced. This model does not assume every pointer has exactly one allocation owner."
    ],
    "appliesTo": [
      "urn:csabs:concept/PointerProvenance"
    ],
    "dependsOn": [
      "urn:csabs:axiom/PointerProvenance-access-lifetime"
    ],
    "proofSketch": "The access rule additionally requires association and live storage; address equality supplies neither premise.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-llvm",
      "urn:csabs:source/compiler-gep"
    ],
    "sourceLocator": "LangRef: Non-Integral Pointer Type, Object Lifetime, Pointer Aliasing Rules, Pointer Capture; GEP FAQ",
    "sourceNote": "Catalog derivation from the explicit dependsOn premises; the cited source motivates the interface, not this exact editorial theorem name.",
    "provenanceKind": "derived",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  }
]
```
<!-- graph-record:end -->
