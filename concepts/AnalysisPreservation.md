# Analysis validity across IR mutation

A relation connecting valid analysis facts before and after a transformation: a cached fact may be retained only when preserved, soundly updated, or recomputed for the new IR.

**Notation:** Valid(ir,a) ⇒ Valid(T(ir),update(a)); preserve unchanged uses update=id

**Stable ID:** `urn:csabs:concept/AnalysisPreservation`

**Categories:** Programming-language semantics → Compiler transformations

**Kind:** Relation

**Prerequisites:** [Binary relation](Relation.md), [Total function](Function.md)

**Related concepts:** [Sound abstract transfer and inductive dataflow facts](AbstractInterpretation.md), [Reachability-qualified control-flow dominance](Dominance.md), [Typed static single assignment with scoped uses](SSAForm.md), [Conservative SSA indexing of memory versions](MemorySSA.md), [Conservative alias and Mod/Ref query contract](AliasAnalysis.md), [Scoped induction recurrence and trip-count facts](ScalarRecurrence.md)

## Backlinks

- [Sound abstract transfer and inductive dataflow facts](AbstractInterpretation.md) — `relatedConcept`
- [Scoped LLVM attribute, flag and metadata contract](LLVMAttributeContract.md) — `relatedConcept`
- [Conservative SSA indexing of memory versions](MemorySSA.md) — `relatedConcept`

## Mathematical formulation

A relation connecting valid analysis facts before and after a transformation: a cached fact may be retained only when preserved, soundly updated, or recomputed for the new IR. Valid(ir,a) ⇒ Valid(T(ir),update(a)); preserve unchanged uses update=id Analysis results are indexed by the exact IR unit/revision and transitively dependent facts. Valid need not mean equality to a unique computed result: conservative summaries may remain sound. PreservedAnalyses is a declaration by the pass, not independent evidence. Deleting/replacing IR units also invalidates cache identities; a coherent update must account for dependent results and enclosing/contained units. Keeping the CFG unchanged may preserve CFG-only analyses but not arbitrary value/effect analyses.

**Lean formulation** (in its source module context):

```lean
structure AnalysisPreservation (IR Result : Type u) where
  valid : IR → Result → Prop
  transform : IR → IR
  update : Result → Result
  preserved : ∀ ir result, valid ir result → valid (transform ir) (update result)
```

**Source:** [`Catalog.Transforms.AnalysisPreservation`](../lean/Catalog/CompilerTransforms.lean); consulted 2026-11-16.

**Scope:** partial

**Interpretation:** IR-indexed validity relation, transform and update functions with an explicit preservation law.

**Limits:** No LLVM pass-manager/cache implementation or automatic invalidation proof. The preservation field is a client hypothesis, not verification of a pass declaration.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** ∀ir,a, Valid(ir,a) ⇒ Valid(T(ir),update(a)).; Retaining a unchanged requires Valid(ir,a)⇒Valid(T(ir),a); pass declarations alone do not establish this implication.

**basisKind:** relational-structural-definition

**basisScope:** Analysis results are indexed by the exact IR unit/revision and transitively dependent facts. Valid need not mean equality to a unique computed result: conservative summaries may remain sound. PreservedAnalyses is a declaration by the pass, not independent evidence. Deleting/replacing IR units also invalidates cache identities; a coherent update must account for dependent results and enclosing/contained units. Keeping the CFG unchanged may preserve CFG-only analyses but not arbitrary value/effect analyses.

**verificationObligation:** Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.; No LLVM pass-manager/cache implementation or automatic invalidation proof. The preservation field is a client hypothesis, not verification of a pass declaration.

**reviewStatus:** Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-AnalysisPreservation-preserves"></a>

### preserves

`urn:csabs:operation/AnalysisPreservation-preserves`

**signature:** preserves : Transform×Analysis→Prop

**description:** Require validity of retained facts on the transformed IR.

**precondition:** Analysis dependency and identity scopes specified.

**postcondition:** Require validity of retained facts on the transformed IR.

**totality:** Total semantic predicate.

**source:** [LLVM New Pass Manager (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/NewPassManager.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/NewPassManager.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** New Pass Manager: Analysis Invalidation, PreservedAnalyses, updating dominators and CFG analyses

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-AnalysisPreservation-update"></a>

### update

`urn:csabs:operation/AnalysisPreservation-update`

**signature:** update : IR×Result×Mutation⇀Result

**description:** Update cached facts with a validity justification or invalidate them.

**precondition:** Old result valid for the old IR revision.

**postcondition:** Update cached facts with a validity justification or invalidate them.

**totality:** Partial; unsupported update requires invalidation/recomputation.

**source:** [LLVM New Pass Manager (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/NewPassManager.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/NewPassManager.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** New Pass Manager: Analysis Invalidation, PreservedAnalyses, updating dominators and CFG analyses

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-AnalysisPreservation-validity-transport"></a>

### validity-transport

`urn:csabs:axiom/AnalysisPreservation-validity-transport`

**description:** Defining obligation for Analysis validity across IR mutation

**statement:** ∀ir,a, Valid(ir,a) ⇒ Valid(T(ir),update(a)).

**formalStatement:** ∀ir,a, Valid(ir,a) ⇒ Valid(T(ir),update(a)).

**assumptions:** Analysis results are indexed by the exact IR unit/revision and transitively dependent facts. Valid need not mean equality to a unique computed result: conservative summaries may remain sound. PreservedAnalyses is a declaration by the pass, not independent evidence. Deleting/replacing IR units also invalidates cache identities; a coherent update must account for dependent results and enclosing/contained units. Keeping the CFG unchanged may preserve CFG-only analyses but not arbitrary value/effect analyses.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM New Pass Manager (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/NewPassManager.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/NewPassManager.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** New Pass Manager: Analysis Invalidation, PreservedAnalyses, updating dominators and CFG analyses

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

**reviewStatus:** Editorial mathematical statement and derivation; no registered compiled witness.

<a id="node-urn-csabs-axiom-AnalysisPreservation-unchanged-cache"></a>

### unchanged-cache

`urn:csabs:axiom/AnalysisPreservation-unchanged-cache`

**description:** Defining obligation for Analysis validity across IR mutation

**statement:** Retaining a unchanged requires Valid(ir,a)⇒Valid(T(ir),a); pass declarations alone do not establish this implication.

**formalStatement:** Retaining a unchanged requires Valid(ir,a)⇒Valid(T(ir),a); pass declarations alone do not establish this implication.

**assumptions:** Analysis results are indexed by the exact IR unit/revision and transitively dependent facts. Valid need not mean equality to a unique computed result: conservative summaries may remain sound. PreservedAnalyses is a declaration by the pass, not independent evidence. Deleting/replacing IR units also invalidates cache identities; a coherent update must account for dependent results and enclosing/contained units. Keeping the CFG unchanged may preserve CFG-only analyses but not arbitrary value/effect analyses.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM New Pass Manager (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/NewPassManager.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/NewPassManager.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** New Pass Manager: Analysis Invalidation, PreservedAnalyses, updating dominators and CFG analyses

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

**reviewStatus:** Editorial mathematical statement and derivation; no registered compiled witness.

## Laws

<a id="node-urn-csabs-law-AnalysisPreservation-identity-preserves"></a>

### identity-preserves

`urn:csabs:law/AnalysisPreservation-identity-preserves`

**description:** Derived consequence within the selected semantic profile.

**statement:** The identity IR transformation with identity result update preserves every analysis-validity relation.

**formalStatement:** The identity IR transformation with identity result update preserves every analysis-validity relation.

**assumptions:** Analysis results are indexed by the exact IR unit/revision and transitively dependent facts. Valid need not mean equality to a unique computed result: conservative summaries may remain sound. PreservedAnalyses is a declaration by the pass, not independent evidence. Deleting/replacing IR units also invalidates cache identities; a coherent update must account for dependent results and enclosing/contained units. Keeping the CFG unchanged may preserve CFG-only analyses but not arbitrary value/effect analyses.

**dependsOn:** [validity-transport](AnalysisPreservation.md#node-urn-csabs-axiom-AnalysisPreservation-validity-transport)

**proofSketch:** Substitute T=id and update=id; the implication reduces to Valid(ir,a)⇒Valid(ir,a).

**reviewStatus:** Editorial mathematical derivation; no registered compiled witness.

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM New Pass Manager (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/NewPassManager.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/NewPassManager.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** New Pass Manager: Analysis Invalidation, PreservedAnalyses, updating dominators and CFG analyses

**sourceNote:** Derived from the explicit dependsOn premises under the stated assumptions; exact claim and proof sketch are editorial.

**provenanceKind:** derived

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [LLVM New Pass Manager (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/NewPassManager.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/NewPassManager.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** New Pass Manager: Analysis Invalidation, PreservedAnalyses, updating dominators and CFG analyses

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/AnalysisPreservation",
    "type": "Concept",
    "shortForm": "AnalysisPreservation",
    "fullName": "Analysis validity across IR mutation",
    "definition": "A relation connecting valid analysis facts before and after a transformation: a cached fact may be retained only when preserved, soundly updated, or recomputed for the new IR.",
    "notation": "Valid(ir,a) ⇒ Valid(T(ir),update(a)); preserve unchanged uses update=id",
    "category": [
      "urn:csabs:category/compiler-transformations"
    ],
    "kind": "urn:csabs:kind/relation",
    "requiresConcept": [
      "urn:csabs:concept/Relation",
      "urn:csabs:concept/Function"
    ],
    "relatedConcept": [
      "urn:csabs:concept/AbstractInterpretation",
      "urn:csabs:concept/Dominance",
      "urn:csabs:concept/SSAForm",
      "urn:csabs:concept/MemorySSA",
      "urn:csabs:concept/AliasAnalysis",
      "urn:csabs:concept/ScalarRecurrence"
    ],
    "hasOperation": [
      "urn:csabs:operation/AnalysisPreservation-preserves",
      "urn:csabs:operation/AnalysisPreservation-update"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/AnalysisPreservation-validity-transport",
      "urn:csabs:axiom/AnalysisPreservation-unchanged-cache"
    ],
    "hasLaw": [
      "urn:csabs:law/AnalysisPreservation-identity-preserves"
    ],
    "hasTheorem": [],
    "basisKind": "relational-structural-definition",
    "basisScope": "Analysis results are indexed by the exact IR unit/revision and transitively dependent facts. Valid need not mean equality to a unique computed result: conservative summaries may remain sound. PreservedAnalyses is a declaration by the pass, not independent evidence. Deleting/replacing IR units also invalidates cache identities; a coherent update must account for dependent results and enclosing/contained units. Keeping the CFG unchanged may preserve CFG-only analyses but not arbitrary value/effect analyses.",
    "axiomBasis": "∀ir,a, Valid(ir,a) ⇒ Valid(T(ir),update(a)).; Retaining a unchanged requires Valid(ir,a)⇒Valid(T(ir),a); pass declarations alone do not establish this implication.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.",
    "verificationObligation": [
      "Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.",
      "No LLVM pass-manager/cache implementation or automatic invalidation proof. The preservation field is a client hypothesis, not verification of a pass declaration."
    ],
    "source": [
      "urn:csabs:source/compiler-passes"
    ],
    "sourceLocator": "New Pass Manager: Analysis Invalidation, PreservedAnalyses, updating dominators and CFG analyses",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted",
    "mathematicalFormulation": "A relation connecting valid analysis facts before and after a transformation: a cached fact may be retained only when preserved, soundly updated, or recomputed for the new IR. Valid(ir,a) ⇒ Valid(T(ir),update(a)); preserve unchanged uses update=id Analysis results are indexed by the exact IR unit/revision and transitively dependent facts. Valid need not mean equality to a unique computed result: conservative summaries may remain sound. PreservedAnalyses is a declaration by the pass, not independent evidence. Deleting/replacing IR units also invalidates cache identities; a coherent update must account for dependent results and enclosing/contained units. Keeping the CFG unchanged may preserve CFG-only analyses but not arbitrary value/effect analyses.",
    "leanFormulation": "structure AnalysisPreservation (IR Result : Type u) where\n  valid : IR → Result → Prop\n  transform : IR → IR\n  update : Result → Result\n  preserved : ∀ ir result, valid ir result → valid (transform ir) (update result)",
    "formulationSource": "urn:csabs:source/compiler-lean",
    "formulationLocator": "Catalog.Transforms.AnalysisPreservation",
    "formulationScope": "partial",
    "leanModelMapping": "IR-indexed validity relation, transform and update functions with an explicit preservation law.",
    "leanModelLimitations": "No LLVM pass-manager/cache implementation or automatic invalidation proof. The preservation field is a client hypothesis, not verification of a pass declaration."
  },
  {
    "id": "urn:csabs:operation/AnalysisPreservation-preserves",
    "type": "Operation",
    "name": "preserves",
    "signature": "preserves : Transform×Analysis→Prop",
    "description": "Require validity of retained facts on the transformed IR.",
    "concept": "urn:csabs:concept/AnalysisPreservation",
    "precondition": "Analysis dependency and identity scopes specified.",
    "postcondition": "Require validity of retained facts on the transformed IR.",
    "totality": "Total semantic predicate.",
    "source": [
      "urn:csabs:source/compiler-passes"
    ],
    "sourceLocator": "New Pass Manager: Analysis Invalidation, PreservedAnalyses, updating dominators and CFG analyses",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/AnalysisPreservation-update",
    "type": "Operation",
    "name": "update",
    "signature": "update : IR×Result×Mutation⇀Result",
    "description": "Update cached facts with a validity justification or invalidate them.",
    "concept": "urn:csabs:concept/AnalysisPreservation",
    "precondition": "Old result valid for the old IR revision.",
    "postcondition": "Update cached facts with a validity justification or invalidate them.",
    "totality": "Partial; unsupported update requires invalidation/recomputation.",
    "source": [
      "urn:csabs:source/compiler-passes"
    ],
    "sourceLocator": "New Pass Manager: Analysis Invalidation, PreservedAnalyses, updating dominators and CFG analyses",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/AnalysisPreservation-validity-transport",
    "type": "Axiom",
    "name": "validity-transport",
    "description": "Defining obligation for Analysis validity across IR mutation",
    "statement": "∀ir,a, Valid(ir,a) ⇒ Valid(T(ir),update(a)).",
    "formalStatement": "∀ir,a, Valid(ir,a) ⇒ Valid(T(ir),update(a)).",
    "assumptions": [
      "Analysis results are indexed by the exact IR unit/revision and transitively dependent facts. Valid need not mean equality to a unique computed result: conservative summaries may remain sound. PreservedAnalyses is a declaration by the pass, not independent evidence. Deleting/replacing IR units also invalidates cache identities; a coherent update must account for dependent results and enclosing/contained units. Keeping the CFG unchanged may preserve CFG-only analyses but not arbitrary value/effect analyses."
    ],
    "appliesTo": [
      "urn:csabs:concept/AnalysisPreservation"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-passes"
    ],
    "sourceLocator": "New Pass Manager: Analysis Invalidation, PreservedAnalyses, updating dominators and CFG analyses",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial mathematical statement and derivation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:axiom/AnalysisPreservation-unchanged-cache",
    "type": "Axiom",
    "name": "unchanged-cache",
    "description": "Defining obligation for Analysis validity across IR mutation",
    "statement": "Retaining a unchanged requires Valid(ir,a)⇒Valid(T(ir),a); pass declarations alone do not establish this implication.",
    "formalStatement": "Retaining a unchanged requires Valid(ir,a)⇒Valid(T(ir),a); pass declarations alone do not establish this implication.",
    "assumptions": [
      "Analysis results are indexed by the exact IR unit/revision and transitively dependent facts. Valid need not mean equality to a unique computed result: conservative summaries may remain sound. PreservedAnalyses is a declaration by the pass, not independent evidence. Deleting/replacing IR units also invalidates cache identities; a coherent update must account for dependent results and enclosing/contained units. Keeping the CFG unchanged may preserve CFG-only analyses but not arbitrary value/effect analyses."
    ],
    "appliesTo": [
      "urn:csabs:concept/AnalysisPreservation"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-passes"
    ],
    "sourceLocator": "New Pass Manager: Analysis Invalidation, PreservedAnalyses, updating dominators and CFG analyses",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial mathematical statement and derivation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:law/AnalysisPreservation-identity-preserves",
    "type": "Law",
    "name": "identity-preserves",
    "description": "Derived consequence within the selected semantic profile.",
    "statement": "The identity IR transformation with identity result update preserves every analysis-validity relation.",
    "formalStatement": "The identity IR transformation with identity result update preserves every analysis-validity relation.",
    "assumptions": [
      "Analysis results are indexed by the exact IR unit/revision and transitively dependent facts. Valid need not mean equality to a unique computed result: conservative summaries may remain sound. PreservedAnalyses is a declaration by the pass, not independent evidence. Deleting/replacing IR units also invalidates cache identities; a coherent update must account for dependent results and enclosing/contained units. Keeping the CFG unchanged may preserve CFG-only analyses but not arbitrary value/effect analyses."
    ],
    "appliesTo": [
      "urn:csabs:concept/AnalysisPreservation"
    ],
    "dependsOn": [
      "urn:csabs:axiom/AnalysisPreservation-validity-transport"
    ],
    "proofSketch": "Substitute T=id and update=id; the implication reduces to Valid(ir,a)⇒Valid(ir,a).",
    "reviewStatus": "Editorial mathematical derivation; no registered compiled witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-passes"
    ],
    "sourceLocator": "New Pass Manager: Analysis Invalidation, PreservedAnalyses, updating dominators and CFG analyses",
    "sourceNote": "Derived from the explicit dependsOn premises under the stated assumptions; exact claim and proof sketch are editorial.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
