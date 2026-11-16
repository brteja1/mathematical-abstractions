# Conservative alias and Mod/Ref query contract

A context-dependent analysis of memory locations comprising pointer and size, returning conservative alias and read/write effects rather than treating pointer names or types as disjointness proofs.

**Notation:** query(L₁,L₂)∈{NoAlias,MayAlias,PartialAlias,MustAlias}; L=(ptr,size,context)

**Stable ID:** `urn:csabs:concept/AliasAnalysis`

**Categories:** Programming-language semantics → Compiler transformations

**Kind:** semantic-model

**Prerequisites:** [Byte-addressed memory with typed access obligations](ByteMemory.md), [Sound abstract transfer and inductive dataflow facts](AbstractInterpretation.md)

**Related concepts:** [Conservative resource effect summary](EffectSummary.md), [Conservative SSA indexing of memory versions](MemorySSA.md)

## Backlinks

- [Analysis validity across IR mutation](AnalysisPreservation.md) — `relatedConcept`
- [Conservative resource effect summary](EffectSummary.md) — `relatedConcept`
- [Memory dependence and legal loop rescheduling](LoopDependence.md) — `relatedConcept`
- [Conservative SSA indexing of memory versions](MemorySSA.md) — `requiresConcept`
- [Allocation-associated pointer provenance and lifetime](PointerProvenance.md) — `relatedConcept`

## Mathematical formulation

A context-dependent analysis of memory locations comprising pointer and size, returning conservative alias and read/write effects rather than treating pointer names or types as disjointness proofs. query(L₁,L₂)∈{NoAlias,MayAlias,PartialAlias,MustAlias}; L=(ptr,size,context) LLVM 21.1.8 query context and relevant defined executions fixed. NoAlias excludes relevant immediate dependence under that context, including documented noalias exceptions; do not reinterpret every NoAlias result as unconditional numeric-range disjointness. MustAlias guarantees same start location, not equal sizes or pointer comparison. PartialAlias guarantees overlap under applicable query semantics. MayAlias is unknown and supplies no witness of actual aliasing. Mod/Ref effects are overapproximations and call-to-call queries can be asymmetric. Unknown sizes and unsupported cases remain conservative.

**Lean formulation** (in its source module context):

```lean
structure AliasAnalysis (Location : Type u) where
  possibleConflict : Location → Location → Prop
  query : Location → Location → AliasVerdict
  noAliasSound : ∀ x y, query x y = .noAlias → ¬ possibleConflict x y
```

**Source:** [`Catalog.LLVM.AliasAnalysis`](../lean/Catalog/LLVMTransforms.lean); consulted 2026-11-16.

**Scope:** partial

**Interpretation:** Four-way alias verdict and a supplied possible-conflict relation with a NoAlias soundness field.

**Limits:** No BasicAA/TBAA/scoped-noalias implementation, size geometry, positive-result laws or Mod/Ref evaluator in Lean; query context must be encoded by the client.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** alias(C,L₁,L₂)=NoAlias ⇒ no relevant immediate conflict in any admitted execution of C.; ActualModRef(C,I,L)⊆ReportedModRef(C,I,L); MayAlias gives no positive alias witness.

**basisKind:** relational-structural-definition

**basisScope:** LLVM 21.1.8 query context and relevant defined executions fixed. NoAlias excludes relevant immediate dependence under that context, including documented noalias exceptions; do not reinterpret every NoAlias result as unconditional numeric-range disjointness. MustAlias guarantees same start location, not equal sizes or pointer comparison. PartialAlias guarantees overlap under applicable query semantics. MayAlias is unknown and supplies no witness of actual aliasing. Mod/Ref effects are overapproximations and call-to-call queries can be asymmetric. Unknown sizes and unsupported cases remain conservative.

**verificationObligation:** Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.; No BasicAA/TBAA/scoped-noalias implementation, size geometry, positive-result laws or Mod/Ref evaluator in Lean; query context must be encoded by the client.

**reviewStatus:** Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-AliasAnalysis-alias"></a>

### alias

`urn:csabs:operation/AliasAnalysis-alias`

**signature:** alias : Context×Location×Location→AliasVerdict

**description:** Report a sound relation over queried ranges and executions.

**precondition:** Locations and values satisfy LLVM query restrictions.

**postcondition:** Report a sound relation over queried ranges and executions.

**totality:** Total conservative query.

**source:** [LLVM Alias Analysis (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/AliasAnalysis.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/AliasAnalysis.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** AliasAnalysis: Representation of Pointers, alias method, Must/May/No responses, getModRefInfo; LangRef: Pointer Aliasing Rules

**sourceNote:** Adapted Conservative alias and Mod/Ref query contract from AliasAnalysis: Representation of Pointers, alias method, Must/May/No responses, getModRefInfo; LangRef: Pointer Aliasing Rules. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-AliasAnalysis-modref"></a>

### modref

`urn:csabs:operation/AliasAnalysis-modref`

**signature:** modRef : Instruction×Location→P({Read,Write})

**description:** Overapproximate possible reads/writes relevant to the location.

**precondition:** Call bundles, attributes and alias context included.

**postcondition:** Overapproximate possible reads/writes relevant to the location.

**totality:** Total abstract query; unknown is top.

**source:** [LLVM Alias Analysis (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/AliasAnalysis.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/AliasAnalysis.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** AliasAnalysis: Representation of Pointers, alias method, Must/May/No responses, getModRefInfo; LangRef: Pointer Aliasing Rules

**sourceNote:** Adapted Conservative alias and Mod/Ref query contract from AliasAnalysis: Representation of Pointers, alias method, Must/May/No responses, getModRefInfo; LangRef: Pointer Aliasing Rules. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-AliasAnalysis-noalias-soundness"></a>

### noalias-soundness

`urn:csabs:axiom/AliasAnalysis-noalias-soundness`

**description:** Defining obligation for Conservative alias and Mod/Ref query contract

**statement:** alias(C,L₁,L₂)=NoAlias ⇒ no relevant immediate conflict in any admitted execution of C.

**formalStatement:** alias(C,L₁,L₂)=NoAlias ⇒ no relevant immediate conflict in any admitted execution of C.

**assumptions:** LLVM 21.1.8 query context and relevant defined executions fixed. NoAlias excludes relevant immediate dependence under that context, including documented noalias exceptions; do not reinterpret every NoAlias result as unconditional numeric-range disjointness. MustAlias guarantees same start location, not equal sizes or pointer comparison. PartialAlias guarantees overlap under applicable query semantics. MayAlias is unknown and supplies no witness of actual aliasing. Mod/Ref effects are overapproximations and call-to-call queries can be asymmetric. Unknown sizes and unsupported cases remain conservative.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Alias Analysis (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/AliasAnalysis.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/AliasAnalysis.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** AliasAnalysis: Representation of Pointers, alias method, Must/May/No responses, getModRefInfo; LangRef: Pointer Aliasing Rules

**sourceNote:** Adapted Conservative alias and Mod/Ref query contract from AliasAnalysis: Representation of Pointers, alias method, Must/May/No responses, getModRefInfo; LangRef: Pointer Aliasing Rules. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

<a id="node-urn-csabs-axiom-AliasAnalysis-modref-soundness"></a>

### modref-soundness

`urn:csabs:axiom/AliasAnalysis-modref-soundness`

**description:** Defining obligation for Conservative alias and Mod/Ref query contract

**statement:** ActualModRef(C,I,L)⊆ReportedModRef(C,I,L); MayAlias gives no positive alias witness.

**formalStatement:** ActualModRef(C,I,L)⊆ReportedModRef(C,I,L); MayAlias gives no positive alias witness.

**assumptions:** LLVM 21.1.8 query context and relevant defined executions fixed. NoAlias excludes relevant immediate dependence under that context, including documented noalias exceptions; do not reinterpret every NoAlias result as unconditional numeric-range disjointness. MustAlias guarantees same start location, not equal sizes or pointer comparison. PartialAlias guarantees overlap under applicable query semantics. MayAlias is unknown and supplies no witness of actual aliasing. Mod/Ref effects are overapproximations and call-to-call queries can be asymmetric. Unknown sizes and unsupported cases remain conservative.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Alias Analysis (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/AliasAnalysis.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/AliasAnalysis.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** AliasAnalysis: Representation of Pointers, alias method, Must/May/No responses, getModRefInfo; LangRef: Pointer Aliasing Rules

**sourceNote:** Adapted Conservative alias and Mod/Ref query contract from AliasAnalysis: Representation of Pointers, alias method, Must/May/No responses, getModRefInfo; LangRef: Pointer Aliasing Rules. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

## Laws

<a id="node-urn-csabs-law-AliasAnalysis-no-modref-excludes-write"></a>

### no-modref-excludes-write

`urn:csabs:law/AliasAnalysis-no-modref-excludes-write`

**description:** Derived consequence in the stated profile.

**statement:** ReportedModRef(C,I,L)=∅ ⇒ I has no relevant read or write effect on L in the admitted executions.

**formalStatement:** ReportedModRef(C,I,L)=∅ ⇒ I has no relevant read or write effect on L in the admitted executions.

**assumptions:** LLVM 21.1.8 query context and relevant defined executions fixed. NoAlias excludes relevant immediate dependence under that context, including documented noalias exceptions; do not reinterpret every NoAlias result as unconditional numeric-range disjointness. MustAlias guarantees same start location, not equal sizes or pointer comparison. PartialAlias guarantees overlap under applicable query semantics. MayAlias is unknown and supplies no witness of actual aliasing. Mod/Ref effects are overapproximations and call-to-call queries can be asymmetric. Unknown sizes and unsupported cases remain conservative.

**dependsOn:** [modref-soundness](AliasAnalysis.md#node-urn-csabs-axiom-AliasAnalysis-modref-soundness)

**proofSketch:** An actual effect would belong to the reported empty overapproximation, a contradiction. This is scoped to L and the query context.

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Alias Analysis (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/AliasAnalysis.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/AliasAnalysis.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface; [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** AliasAnalysis: Representation of Pointers, alias method, Must/May/No responses, getModRefInfo; LangRef: Pointer Aliasing Rules

**sourceNote:** Catalog derivation from the explicit dependsOn premises; the cited source motivates the interface, not this exact editorial theorem name.

**provenanceKind:** derived

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [LLVM Alias Analysis (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/AliasAnalysis.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/AliasAnalysis.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface
- [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** AliasAnalysis: Representation of Pointers, alias method, Must/May/No responses, getModRefInfo; LangRef: Pointer Aliasing Rules

**sourceNote:** Adapted Conservative alias and Mod/Ref query contract from AliasAnalysis: Representation of Pointers, alias method, Must/May/No responses, getModRefInfo; LangRef: Pointer Aliasing Rules. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/AliasAnalysis",
    "type": "Concept",
    "shortForm": "AliasAnalysis",
    "fullName": "Conservative alias and Mod/Ref query contract",
    "definition": "A context-dependent analysis of memory locations comprising pointer and size, returning conservative alias and read/write effects rather than treating pointer names or types as disjointness proofs.",
    "notation": "query(L₁,L₂)∈{NoAlias,MayAlias,PartialAlias,MustAlias}; L=(ptr,size,context)",
    "category": [
      "urn:csabs:category/compiler-transformations"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "requiresConcept": [
      "urn:csabs:concept/ByteMemory",
      "urn:csabs:concept/AbstractInterpretation"
    ],
    "relatedConcept": [
      "urn:csabs:concept/EffectSummary",
      "urn:csabs:concept/MemorySSA"
    ],
    "hasOperation": [
      "urn:csabs:operation/AliasAnalysis-alias",
      "urn:csabs:operation/AliasAnalysis-modref"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/AliasAnalysis-noalias-soundness",
      "urn:csabs:axiom/AliasAnalysis-modref-soundness"
    ],
    "hasLaw": [
      "urn:csabs:law/AliasAnalysis-no-modref-excludes-write"
    ],
    "hasTheorem": [],
    "basisKind": "relational-structural-definition",
    "basisScope": "LLVM 21.1.8 query context and relevant defined executions fixed. NoAlias excludes relevant immediate dependence under that context, including documented noalias exceptions; do not reinterpret every NoAlias result as unconditional numeric-range disjointness. MustAlias guarantees same start location, not equal sizes or pointer comparison. PartialAlias guarantees overlap under applicable query semantics. MayAlias is unknown and supplies no witness of actual aliasing. Mod/Ref effects are overapproximations and call-to-call queries can be asymmetric. Unknown sizes and unsupported cases remain conservative.",
    "axiomBasis": "alias(C,L₁,L₂)=NoAlias ⇒ no relevant immediate conflict in any admitted execution of C.; ActualModRef(C,I,L)⊆ReportedModRef(C,I,L); MayAlias gives no positive alias witness.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.",
    "verificationObligation": [
      "Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.",
      "No BasicAA/TBAA/scoped-noalias implementation, size geometry, positive-result laws or Mod/Ref evaluator in Lean; query context must be encoded by the client."
    ],
    "source": [
      "urn:csabs:source/compiler-alias",
      "urn:csabs:source/compiler-llvm"
    ],
    "sourceLocator": "AliasAnalysis: Representation of Pointers, alias method, Must/May/No responses, getModRefInfo; LangRef: Pointer Aliasing Rules",
    "sourceNote": "Adapted Conservative alias and Mod/Ref query contract from AliasAnalysis: Representation of Pointers, alias method, Must/May/No responses, getModRefInfo; LangRef: Pointer Aliasing Rules. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "mathematicalFormulation": "A context-dependent analysis of memory locations comprising pointer and size, returning conservative alias and read/write effects rather than treating pointer names or types as disjointness proofs. query(L₁,L₂)∈{NoAlias,MayAlias,PartialAlias,MustAlias}; L=(ptr,size,context) LLVM 21.1.8 query context and relevant defined executions fixed. NoAlias excludes relevant immediate dependence under that context, including documented noalias exceptions; do not reinterpret every NoAlias result as unconditional numeric-range disjointness. MustAlias guarantees same start location, not equal sizes or pointer comparison. PartialAlias guarantees overlap under applicable query semantics. MayAlias is unknown and supplies no witness of actual aliasing. Mod/Ref effects are overapproximations and call-to-call queries can be asymmetric. Unknown sizes and unsupported cases remain conservative.",
    "leanFormulation": "structure AliasAnalysis (Location : Type u) where\n  possibleConflict : Location → Location → Prop\n  query : Location → Location → AliasVerdict\n  noAliasSound : ∀ x y, query x y = .noAlias → ¬ possibleConflict x y",
    "formulationSource": "urn:csabs:source/compiler-llvm-lean",
    "formulationLocator": "Catalog.LLVM.AliasAnalysis",
    "formulationScope": "partial",
    "leanModelMapping": "Four-way alias verdict and a supplied possible-conflict relation with a NoAlias soundness field.",
    "leanModelLimitations": "No BasicAA/TBAA/scoped-noalias implementation, size geometry, positive-result laws or Mod/Ref evaluator in Lean; query context must be encoded by the client."
  },
  {
    "id": "urn:csabs:operation/AliasAnalysis-alias",
    "type": "Operation",
    "name": "alias",
    "signature": "alias : Context×Location×Location→AliasVerdict",
    "description": "Report a sound relation over queried ranges and executions.",
    "concept": "urn:csabs:concept/AliasAnalysis",
    "precondition": "Locations and values satisfy LLVM query restrictions.",
    "postcondition": "Report a sound relation over queried ranges and executions.",
    "totality": "Total conservative query.",
    "source": [
      "urn:csabs:source/compiler-alias",
      "urn:csabs:source/compiler-llvm"
    ],
    "sourceLocator": "AliasAnalysis: Representation of Pointers, alias method, Must/May/No responses, getModRefInfo; LangRef: Pointer Aliasing Rules",
    "sourceNote": "Adapted Conservative alias and Mod/Ref query contract from AliasAnalysis: Representation of Pointers, alias method, Must/May/No responses, getModRefInfo; LangRef: Pointer Aliasing Rules. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/AliasAnalysis-modref",
    "type": "Operation",
    "name": "modref",
    "signature": "modRef : Instruction×Location→P({Read,Write})",
    "description": "Overapproximate possible reads/writes relevant to the location.",
    "concept": "urn:csabs:concept/AliasAnalysis",
    "precondition": "Call bundles, attributes and alias context included.",
    "postcondition": "Overapproximate possible reads/writes relevant to the location.",
    "totality": "Total abstract query; unknown is top.",
    "source": [
      "urn:csabs:source/compiler-alias",
      "urn:csabs:source/compiler-llvm"
    ],
    "sourceLocator": "AliasAnalysis: Representation of Pointers, alias method, Must/May/No responses, getModRefInfo; LangRef: Pointer Aliasing Rules",
    "sourceNote": "Adapted Conservative alias and Mod/Ref query contract from AliasAnalysis: Representation of Pointers, alias method, Must/May/No responses, getModRefInfo; LangRef: Pointer Aliasing Rules. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/AliasAnalysis-noalias-soundness",
    "type": "Axiom",
    "name": "noalias-soundness",
    "description": "Defining obligation for Conservative alias and Mod/Ref query contract",
    "statement": "alias(C,L₁,L₂)=NoAlias ⇒ no relevant immediate conflict in any admitted execution of C.",
    "formalStatement": "alias(C,L₁,L₂)=NoAlias ⇒ no relevant immediate conflict in any admitted execution of C.",
    "assumptions": [
      "LLVM 21.1.8 query context and relevant defined executions fixed. NoAlias excludes relevant immediate dependence under that context, including documented noalias exceptions; do not reinterpret every NoAlias result as unconditional numeric-range disjointness. MustAlias guarantees same start location, not equal sizes or pointer comparison. PartialAlias guarantees overlap under applicable query semantics. MayAlias is unknown and supplies no witness of actual aliasing. Mod/Ref effects are overapproximations and call-to-call queries can be asymmetric. Unknown sizes and unsupported cases remain conservative."
    ],
    "appliesTo": [
      "urn:csabs:concept/AliasAnalysis"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-alias",
      "urn:csabs:source/compiler-llvm"
    ],
    "sourceLocator": "AliasAnalysis: Representation of Pointers, alias method, Must/May/No responses, getModRefInfo; LangRef: Pointer Aliasing Rules",
    "sourceNote": "Adapted Conservative alias and Mod/Ref query contract from AliasAnalysis: Representation of Pointers, alias method, Must/May/No responses, getModRefInfo; LangRef: Pointer Aliasing Rules. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:axiom/AliasAnalysis-modref-soundness",
    "type": "Axiom",
    "name": "modref-soundness",
    "description": "Defining obligation for Conservative alias and Mod/Ref query contract",
    "statement": "ActualModRef(C,I,L)⊆ReportedModRef(C,I,L); MayAlias gives no positive alias witness.",
    "formalStatement": "ActualModRef(C,I,L)⊆ReportedModRef(C,I,L); MayAlias gives no positive alias witness.",
    "assumptions": [
      "LLVM 21.1.8 query context and relevant defined executions fixed. NoAlias excludes relevant immediate dependence under that context, including documented noalias exceptions; do not reinterpret every NoAlias result as unconditional numeric-range disjointness. MustAlias guarantees same start location, not equal sizes or pointer comparison. PartialAlias guarantees overlap under applicable query semantics. MayAlias is unknown and supplies no witness of actual aliasing. Mod/Ref effects are overapproximations and call-to-call queries can be asymmetric. Unknown sizes and unsupported cases remain conservative."
    ],
    "appliesTo": [
      "urn:csabs:concept/AliasAnalysis"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-alias",
      "urn:csabs:source/compiler-llvm"
    ],
    "sourceLocator": "AliasAnalysis: Representation of Pointers, alias method, Must/May/No responses, getModRefInfo; LangRef: Pointer Aliasing Rules",
    "sourceNote": "Adapted Conservative alias and Mod/Ref query contract from AliasAnalysis: Representation of Pointers, alias method, Must/May/No responses, getModRefInfo; LangRef: Pointer Aliasing Rules. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:law/AliasAnalysis-no-modref-excludes-write",
    "type": "Law",
    "name": "no-modref-excludes-write",
    "description": "Derived consequence in the stated profile.",
    "statement": "ReportedModRef(C,I,L)=∅ ⇒ I has no relevant read or write effect on L in the admitted executions.",
    "formalStatement": "ReportedModRef(C,I,L)=∅ ⇒ I has no relevant read or write effect on L in the admitted executions.",
    "assumptions": [
      "LLVM 21.1.8 query context and relevant defined executions fixed. NoAlias excludes relevant immediate dependence under that context, including documented noalias exceptions; do not reinterpret every NoAlias result as unconditional numeric-range disjointness. MustAlias guarantees same start location, not equal sizes or pointer comparison. PartialAlias guarantees overlap under applicable query semantics. MayAlias is unknown and supplies no witness of actual aliasing. Mod/Ref effects are overapproximations and call-to-call queries can be asymmetric. Unknown sizes and unsupported cases remain conservative."
    ],
    "appliesTo": [
      "urn:csabs:concept/AliasAnalysis"
    ],
    "dependsOn": [
      "urn:csabs:axiom/AliasAnalysis-modref-soundness"
    ],
    "proofSketch": "An actual effect would belong to the reported empty overapproximation, a contradiction. This is scoped to L and the query context.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-alias",
      "urn:csabs:source/compiler-llvm"
    ],
    "sourceLocator": "AliasAnalysis: Representation of Pointers, alias method, Must/May/No responses, getModRefInfo; LangRef: Pointer Aliasing Rules",
    "sourceNote": "Catalog derivation from the explicit dependsOn premises; the cited source motivates the interface, not this exact editorial theorem name.",
    "provenanceKind": "derived",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  }
]
```
<!-- graph-record:end -->
