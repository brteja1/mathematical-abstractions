# Conservative SSA indexing of memory versions

An intraprocedural virtual def-use graph over whole-memory versions using MemoryDef, MemoryUse, MemoryPhi and liveOnEntry, supporting conservative clobber queries with alias refinement.

**Notation:** ActualClobber(use)⊆CandidateClobber(use); kind∈{Def,Use,Phi,Entry}

**Stable ID:** `urn:csabs:concept/MemorySSA`

**Categories:** Programming-language semantics → Compiler transformations

**Kind:** semantic-model

**Prerequisites:** [Typed static single assignment with scoped uses](SSAForm.md), [Conservative alias and Mod/Ref query contract](AliasAnalysis.md)

**Related concepts:** [Analysis validity across IR mutation](AnalysisPreservation.md), [Byte-addressed memory with typed access obligations](ByteMemory.md), [Reachability-qualified control-flow dominance](Dominance.md)

## Backlinks

- [Conservative alias and Mod/Ref query contract](AliasAnalysis.md) — `relatedConcept`
- [Analysis validity across IR mutation](AnalysisPreservation.md) — `relatedConcept`
- [Conservative resource effect summary](EffectSummary.md) — `relatedConcept`

## Mathematical formulation

An intraprocedural virtual def-use graph over whole-memory versions using MemoryDef, MemoryUse, MemoryPhi and liveOnEntry, supporting conservative clobber queries with alias refinement. ActualClobber(use)⊆CandidateClobber(use); kind∈{Def,Use,Phi,Entry} MemorySSA is an analysis, not executable scalar SSA or a concrete memory model. Def includes ordering constraints, such as acquire loads and fences, not only writes. Phi merges may-reach versions rather than scalar must-definitions. liveOnEntry denotes a version before function entry, not a single concrete initialized value. Clobber results require correct AA, dominance and updater state. A clobber candidate is not proof that a write must occur; absence of candidates requires a sound query and context.

**Lean formulation** (in its source module context):

```lean
structure MemorySSA (Access : Type u) where
  kind : Access → MemoryAccessKind
  concreteClobber : Access → Access → Prop
  candidate : Access → Access → Prop
  conservative : ∀ d use, concreteClobber d use → candidate d use
```

**Source:** [`Catalog.LLVM.MemorySSA`](../lean/Catalog/LLVMTransforms.lean); consulted 2026-11-16.

**Scope:** partial

**Interpretation:** Access-kind tag and actual/candidate clobber relations with conservative inclusion.

**Limits:** No graph construction, dominance/PHI verifier, walker, updater, alias integration or concrete loaded-value equality proof.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** ActualClobber(use)⊆CandidateClobber(use).; MemoryDef creates a version for writes or ordering; MemoryUse observes; MemoryPhi merges may-reach versions; liveOnEntry is the entry version.

**basisKind:** relational-structural-definition

**basisScope:** MemorySSA is an analysis, not executable scalar SSA or a concrete memory model. Def includes ordering constraints, such as acquire loads and fences, not only writes. Phi merges may-reach versions rather than scalar must-definitions. liveOnEntry denotes a version before function entry, not a single concrete initialized value. Clobber results require correct AA, dominance and updater state. A clobber candidate is not proof that a write must occur; absence of candidates requires a sound query and context.

**verificationObligation:** Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.; No graph construction, dominance/PHI verifier, walker, updater, alias integration or concrete loaded-value equality proof.

**reviewStatus:** Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-MemorySSA-clobbers"></a>

### clobbers

`urn:csabs:operation/MemorySSA-clobbers`

**signature:** clobbers : Access×Location→P(MemoryDef)

**description:** Conservatively find memory versions that can clobber the queried access.

**precondition:** Fresh graph and sound alias queries.

**postcondition:** Conservatively find memory versions that can clobber the queried access.

**totality:** Conservative abstract query.

**source:** [LLVM MemorySSA (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/MemorySSA.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/MemorySSA.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** MemorySSA: Structure, MemoryDef/MemoryPhi/MemoryUse/liveOnEntry, walker, Precision

**sourceNote:** Adapted Conservative SSA indexing of memory versions from MemorySSA: Structure, MemoryDef/MemoryPhi/MemoryUse/liveOnEntry, walker, Precision. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-MemorySSA-update"></a>

### update

`urn:csabs:operation/MemorySSA-update`

**signature:** update : MemorySSA×IRMutation⇀MemorySSA

**description:** Restore graph validity after memory/CFG edits or invalidate the analysis.

**precondition:** Mutation effects and all affected edges known.

**postcondition:** Restore graph validity after memory/CFG edits or invalidate the analysis.

**totality:** Partial; no unsupported silent reuse.

**source:** [LLVM MemorySSA (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/MemorySSA.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/MemorySSA.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** MemorySSA: Structure, MemoryDef/MemoryPhi/MemoryUse/liveOnEntry, walker, Precision

**sourceNote:** Adapted Conservative SSA indexing of memory versions from MemorySSA: Structure, MemoryDef/MemoryPhi/MemoryUse/liveOnEntry, walker, Precision. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-MemorySSA-candidate-soundness"></a>

### candidate-soundness

`urn:csabs:axiom/MemorySSA-candidate-soundness`

**description:** Defining obligation for Conservative SSA indexing of memory versions

**statement:** ActualClobber(use)⊆CandidateClobber(use).

**formalStatement:** ActualClobber(use)⊆CandidateClobber(use).

**assumptions:** MemorySSA is an analysis, not executable scalar SSA or a concrete memory model. Def includes ordering constraints, such as acquire loads and fences, not only writes. Phi merges may-reach versions rather than scalar must-definitions. liveOnEntry denotes a version before function entry, not a single concrete initialized value. Clobber results require correct AA, dominance and updater state. A clobber candidate is not proof that a write must occur; absence of candidates requires a sound query and context.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM MemorySSA (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/MemorySSA.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/MemorySSA.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** MemorySSA: Structure, MemoryDef/MemoryPhi/MemoryUse/liveOnEntry, walker, Precision

**sourceNote:** Adapted Conservative SSA indexing of memory versions from MemorySSA: Structure, MemoryDef/MemoryPhi/MemoryUse/liveOnEntry, walker, Precision. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

<a id="node-urn-csabs-axiom-MemorySSA-version-kinds"></a>

### version-kinds

`urn:csabs:axiom/MemorySSA-version-kinds`

**description:** Defining obligation for Conservative SSA indexing of memory versions

**statement:** MemoryDef creates a version for writes or ordering; MemoryUse observes; MemoryPhi merges may-reach versions; liveOnEntry is the entry version.

**formalStatement:** MemoryDef creates a version for writes or ordering; MemoryUse observes; MemoryPhi merges may-reach versions; liveOnEntry is the entry version.

**assumptions:** MemorySSA is an analysis, not executable scalar SSA or a concrete memory model. Def includes ordering constraints, such as acquire loads and fences, not only writes. Phi merges may-reach versions rather than scalar must-definitions. liveOnEntry denotes a version before function entry, not a single concrete initialized value. Clobber results require correct AA, dominance and updater state. A clobber candidate is not proof that a write must occur; absence of candidates requires a sound query and context.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM MemorySSA (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/MemorySSA.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/MemorySSA.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** MemorySSA: Structure, MemoryDef/MemoryPhi/MemoryUse/liveOnEntry, walker, Precision

**sourceNote:** Adapted Conservative SSA indexing of memory versions from MemorySSA: Structure, MemoryDef/MemoryPhi/MemoryUse/liveOnEntry, walker, Precision. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

## Laws

<a id="node-urn-csabs-law-MemorySSA-candidate-absence"></a>

### candidate-absence

`urn:csabs:law/MemorySSA-candidate-absence`

**description:** Derived consequence in the stated profile.

**statement:** CandidateClobber(use)=∅ ⇒ ActualClobber(use)=∅ within the query scope.

**formalStatement:** CandidateClobber(use)=∅ ⇒ ActualClobber(use)=∅ within the query scope.

**assumptions:** MemorySSA is an analysis, not executable scalar SSA or a concrete memory model. Def includes ordering constraints, such as acquire loads and fences, not only writes. Phi merges may-reach versions rather than scalar must-definitions. liveOnEntry denotes a version before function entry, not a single concrete initialized value. Clobber results require correct AA, dominance and updater state. A clobber candidate is not proof that a write must occur; absence of candidates requires a sound query and context.

**dependsOn:** [candidate-soundness](MemorySSA.md#node-urn-csabs-axiom-MemorySSA-candidate-soundness)

**proofSketch:** By subset inclusion, an actual clobber would have to belong to the empty candidate set. This does not itself establish redundant-load equivalence.

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM MemorySSA (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/MemorySSA.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/MemorySSA.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** MemorySSA: Structure, MemoryDef/MemoryPhi/MemoryUse/liveOnEntry, walker, Precision

**sourceNote:** Catalog derivation from the explicit dependsOn premises; the cited source motivates the interface, not this exact editorial theorem name.

**provenanceKind:** derived

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [LLVM MemorySSA (21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/MemorySSA.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/MemorySSA.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-interface

**sourceLocator:** MemorySSA: Structure, MemoryDef/MemoryPhi/MemoryUse/liveOnEntry, walker, Precision

**sourceNote:** Adapted Conservative SSA indexing of memory versions from MemorySSA: Structure, MemoryDef/MemoryPhi/MemoryUse/liveOnEntry, walker, Precision. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/MemorySSA",
    "type": "Concept",
    "shortForm": "MemorySSA",
    "fullName": "Conservative SSA indexing of memory versions",
    "definition": "An intraprocedural virtual def-use graph over whole-memory versions using MemoryDef, MemoryUse, MemoryPhi and liveOnEntry, supporting conservative clobber queries with alias refinement.",
    "notation": "ActualClobber(use)⊆CandidateClobber(use); kind∈{Def,Use,Phi,Entry}",
    "category": [
      "urn:csabs:category/compiler-transformations"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "requiresConcept": [
      "urn:csabs:concept/SSAForm",
      "urn:csabs:concept/AliasAnalysis"
    ],
    "relatedConcept": [
      "urn:csabs:concept/AnalysisPreservation",
      "urn:csabs:concept/ByteMemory",
      "urn:csabs:concept/Dominance"
    ],
    "hasOperation": [
      "urn:csabs:operation/MemorySSA-clobbers",
      "urn:csabs:operation/MemorySSA-update"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/MemorySSA-candidate-soundness",
      "urn:csabs:axiom/MemorySSA-version-kinds"
    ],
    "hasLaw": [
      "urn:csabs:law/MemorySSA-candidate-absence"
    ],
    "hasTheorem": [],
    "basisKind": "relational-structural-definition",
    "basisScope": "MemorySSA is an analysis, not executable scalar SSA or a concrete memory model. Def includes ordering constraints, such as acquire loads and fences, not only writes. Phi merges may-reach versions rather than scalar must-definitions. liveOnEntry denotes a version before function entry, not a single concrete initialized value. Clobber results require correct AA, dominance and updater state. A clobber candidate is not proof that a write must occur; absence of candidates requires a sound query and context.",
    "axiomBasis": "ActualClobber(use)⊆CandidateClobber(use).; MemoryDef creates a version for writes or ordering; MemoryUse observes; MemoryPhi merges may-reach versions; liveOnEntry is the entry version.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.",
    "verificationObligation": [
      "Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.",
      "No graph construction, dominance/PHI verifier, walker, updater, alias integration or concrete loaded-value equality proof."
    ],
    "source": [
      "urn:csabs:source/compiler-memoryssa"
    ],
    "sourceLocator": "MemorySSA: Structure, MemoryDef/MemoryPhi/MemoryUse/liveOnEntry, walker, Precision",
    "sourceNote": "Adapted Conservative SSA indexing of memory versions from MemorySSA: Structure, MemoryDef/MemoryPhi/MemoryUse/liveOnEntry, walker, Precision. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "mathematicalFormulation": "An intraprocedural virtual def-use graph over whole-memory versions using MemoryDef, MemoryUse, MemoryPhi and liveOnEntry, supporting conservative clobber queries with alias refinement. ActualClobber(use)⊆CandidateClobber(use); kind∈{Def,Use,Phi,Entry} MemorySSA is an analysis, not executable scalar SSA or a concrete memory model. Def includes ordering constraints, such as acquire loads and fences, not only writes. Phi merges may-reach versions rather than scalar must-definitions. liveOnEntry denotes a version before function entry, not a single concrete initialized value. Clobber results require correct AA, dominance and updater state. A clobber candidate is not proof that a write must occur; absence of candidates requires a sound query and context.",
    "leanFormulation": "structure MemorySSA (Access : Type u) where\n  kind : Access → MemoryAccessKind\n  concreteClobber : Access → Access → Prop\n  candidate : Access → Access → Prop\n  conservative : ∀ d use, concreteClobber d use → candidate d use",
    "formulationSource": "urn:csabs:source/compiler-llvm-lean",
    "formulationLocator": "Catalog.LLVM.MemorySSA",
    "formulationScope": "partial",
    "leanModelMapping": "Access-kind tag and actual/candidate clobber relations with conservative inclusion.",
    "leanModelLimitations": "No graph construction, dominance/PHI verifier, walker, updater, alias integration or concrete loaded-value equality proof."
  },
  {
    "id": "urn:csabs:operation/MemorySSA-clobbers",
    "type": "Operation",
    "name": "clobbers",
    "signature": "clobbers : Access×Location→P(MemoryDef)",
    "description": "Conservatively find memory versions that can clobber the queried access.",
    "concept": "urn:csabs:concept/MemorySSA",
    "precondition": "Fresh graph and sound alias queries.",
    "postcondition": "Conservatively find memory versions that can clobber the queried access.",
    "totality": "Conservative abstract query.",
    "source": [
      "urn:csabs:source/compiler-memoryssa"
    ],
    "sourceLocator": "MemorySSA: Structure, MemoryDef/MemoryPhi/MemoryUse/liveOnEntry, walker, Precision",
    "sourceNote": "Adapted Conservative SSA indexing of memory versions from MemorySSA: Structure, MemoryDef/MemoryPhi/MemoryUse/liveOnEntry, walker, Precision. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/MemorySSA-update",
    "type": "Operation",
    "name": "update",
    "signature": "update : MemorySSA×IRMutation⇀MemorySSA",
    "description": "Restore graph validity after memory/CFG edits or invalidate the analysis.",
    "concept": "urn:csabs:concept/MemorySSA",
    "precondition": "Mutation effects and all affected edges known.",
    "postcondition": "Restore graph validity after memory/CFG edits or invalidate the analysis.",
    "totality": "Partial; no unsupported silent reuse.",
    "source": [
      "urn:csabs:source/compiler-memoryssa"
    ],
    "sourceLocator": "MemorySSA: Structure, MemoryDef/MemoryPhi/MemoryUse/liveOnEntry, walker, Precision",
    "sourceNote": "Adapted Conservative SSA indexing of memory versions from MemorySSA: Structure, MemoryDef/MemoryPhi/MemoryUse/liveOnEntry, walker, Precision. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/MemorySSA-candidate-soundness",
    "type": "Axiom",
    "name": "candidate-soundness",
    "description": "Defining obligation for Conservative SSA indexing of memory versions",
    "statement": "ActualClobber(use)⊆CandidateClobber(use).",
    "formalStatement": "ActualClobber(use)⊆CandidateClobber(use).",
    "assumptions": [
      "MemorySSA is an analysis, not executable scalar SSA or a concrete memory model. Def includes ordering constraints, such as acquire loads and fences, not only writes. Phi merges may-reach versions rather than scalar must-definitions. liveOnEntry denotes a version before function entry, not a single concrete initialized value. Clobber results require correct AA, dominance and updater state. A clobber candidate is not proof that a write must occur; absence of candidates requires a sound query and context."
    ],
    "appliesTo": [
      "urn:csabs:concept/MemorySSA"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-memoryssa"
    ],
    "sourceLocator": "MemorySSA: Structure, MemoryDef/MemoryPhi/MemoryUse/liveOnEntry, walker, Precision",
    "sourceNote": "Adapted Conservative SSA indexing of memory versions from MemorySSA: Structure, MemoryDef/MemoryPhi/MemoryUse/liveOnEntry, walker, Precision. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:axiom/MemorySSA-version-kinds",
    "type": "Axiom",
    "name": "version-kinds",
    "description": "Defining obligation for Conservative SSA indexing of memory versions",
    "statement": "MemoryDef creates a version for writes or ordering; MemoryUse observes; MemoryPhi merges may-reach versions; liveOnEntry is the entry version.",
    "formalStatement": "MemoryDef creates a version for writes or ordering; MemoryUse observes; MemoryPhi merges may-reach versions; liveOnEntry is the entry version.",
    "assumptions": [
      "MemorySSA is an analysis, not executable scalar SSA or a concrete memory model. Def includes ordering constraints, such as acquire loads and fences, not only writes. Phi merges may-reach versions rather than scalar must-definitions. liveOnEntry denotes a version before function entry, not a single concrete initialized value. Clobber results require correct AA, dominance and updater state. A clobber candidate is not proof that a write must occur; absence of candidates requires a sound query and context."
    ],
    "appliesTo": [
      "urn:csabs:concept/MemorySSA"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-memoryssa"
    ],
    "sourceLocator": "MemorySSA: Structure, MemoryDef/MemoryPhi/MemoryUse/liveOnEntry, walker, Precision",
    "sourceNote": "Adapted Conservative SSA indexing of memory versions from MemorySSA: Structure, MemoryDef/MemoryPhi/MemoryUse/liveOnEntry, walker, Precision. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:law/MemorySSA-candidate-absence",
    "type": "Law",
    "name": "candidate-absence",
    "description": "Derived consequence in the stated profile.",
    "statement": "CandidateClobber(use)=∅ ⇒ ActualClobber(use)=∅ within the query scope.",
    "formalStatement": "CandidateClobber(use)=∅ ⇒ ActualClobber(use)=∅ within the query scope.",
    "assumptions": [
      "MemorySSA is an analysis, not executable scalar SSA or a concrete memory model. Def includes ordering constraints, such as acquire loads and fences, not only writes. Phi merges may-reach versions rather than scalar must-definitions. liveOnEntry denotes a version before function entry, not a single concrete initialized value. Clobber results require correct AA, dominance and updater state. A clobber candidate is not proof that a write must occur; absence of candidates requires a sound query and context."
    ],
    "appliesTo": [
      "urn:csabs:concept/MemorySSA"
    ],
    "dependsOn": [
      "urn:csabs:axiom/MemorySSA-candidate-soundness"
    ],
    "proofSketch": "By subset inclusion, an actual clobber would have to belong to the empty candidate set. This does not itself establish redundant-load equivalence.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-memoryssa"
    ],
    "sourceLocator": "MemorySSA: Structure, MemoryDef/MemoryPhi/MemoryUse/liveOnEntry, walker, Precision",
    "sourceNote": "Catalog derivation from the explicit dependsOn premises; the cited source motivates the interface, not this exact editorial theorem name.",
    "provenanceKind": "derived",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  }
]
```
<!-- graph-record:end -->
