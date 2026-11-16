# Reachability-qualified control-flow dominance

A node d dominates a reachable node n when every finite entry-to-n path contains d, including the path endpoints.

**Notation:** d dom n ⇔ reachable(n) ∧ ∀p:entry⇝n, d∈p

**Stable ID:** `urn:csabs:concept/Dominance`

**Categories:** Programming-language semantics → Compiler transformations

**Kind:** Relation

**Prerequisites:** [Directed Graph](DirectedGraph.md), [Binary relation](Relation.md)

**Specializes:** [Binary relation](Relation.md)

**Related concepts:** [Typed static single assignment with scoped uses](SSAForm.md)

## Backlinks

- [Analysis validity across IR mutation](AnalysisPreservation.md) — `relatedConcept`
- [CFG refinement with path correspondence and progress](ControlFlowRefinement.md) — `relatedConcept`
- [Conservative SSA indexing of memory versions](MemorySSA.md) — `relatedConcept`
- [Typed static single assignment with scoped uses](SSAForm.md) — `requiresConcept`

## Mathematical formulation

A node d dominates a reachable node n when every finite entry-to-n path contains d, including the path endpoints. d dom n ⇔ reachable(n) ∧ ∀p:entry⇝n, d∈p Finite directed CFG with one selected entry and finite paths including both endpoints. Dominance queries are restricted to entry-reachable nodes; unreachable nodes are outside the relation, avoiding vacuous universal paths. Instruction order inside a block and PHI incoming-edge uses need separate positions. MLIR hierarchical dominance and graph regions require their own instantiation; this entry is the flat CFG relation.

**Lean formulation** (in its source module context):

```lean
def Dominance {V : Type u} (paths : V → V → List V → Prop)
    (entry dominator node : V) : Prop :=
  (∃ path, paths entry node path) ∧
    ∀ path, paths entry node path → dominator ∈ path
```

**Source:** [`Catalog.Transforms.Dominance`](../lean/Catalog/CompilerTransforms.lean); consulted 2026-11-16.

**Scope:** partial

**Interpretation:** Relation on vertices using a supplied finite-path oracle; endpoints included and existence required.

**Limits:** Path oracle adequacy to the CFG is a client obligation; no dominator algorithm, instruction-order model, postdominance or hierarchical-region implementation.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** d dom n ↔ reachable(n) ∧ ∀p:entry⇝n, d∈p.

**basisKind:** relational-structural-definition

**basisScope:** Finite directed CFG with one selected entry and finite paths including both endpoints. Dominance queries are restricted to entry-reachable nodes; unreachable nodes are outside the relation, avoiding vacuous universal paths. Instruction order inside a block and PHI incoming-edge uses need separate positions. MLIR hierarchical dominance and graph regions require their own instantiation; this entry is the flat CFG relation.

**specializationNote:** Instantiate the parent carrier and operation as follows: Relation on vertices using a supplied finite-path oracle; endpoints included and existence required.

**verificationObligation:** Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.; Path oracle adequacy to the CFG is a client obligation; no dominator algorithm, instruction-order model, postdominance or hierarchical-region implementation.

**reviewStatus:** Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-Dominance-dominates"></a>

### dominates

`urn:csabs:operation/Dominance-dominates`

**signature:** dominates : Node×Node→Prop

**description:** Require reachability and occurrence on every entry path.

**precondition:** Selected CFG and entry.

**postcondition:** Require reachability and occurrence on every entry path.

**totality:** Total predicate; false for unreachable endpoints.

**source:** [MLIR Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/LangRef.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/LangRef.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** MLIR LangRef: Value Scoping, Control Flow and SSACFG Regions; LLVM LangRef: Well-Formedness

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-Dominance-strict-dominates"></a>

### strict-dominates

`urn:csabs:operation/Dominance-strict-dominates`

**signature:** strictDominates : Node×Node→Prop

**description:** Require dominance and distinct nodes.

**precondition:** Node identity fixed.

**postcondition:** Require dominance and distinct nodes.

**totality:** Total predicate.

**source:** [MLIR Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/LangRef.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/LangRef.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** MLIR LangRef: Value Scoping, Control Flow and SSACFG Regions; LLVM LangRef: Well-Formedness

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-Dominance-path-definition"></a>

### path-definition

`urn:csabs:axiom/Dominance-path-definition`

**description:** Defining obligation for Reachability-qualified control-flow dominance

**statement:** d dom n ↔ reachable(n) ∧ ∀p:entry⇝n, d∈p.

**formalStatement:** d dom n ↔ reachable(n) ∧ ∀p:entry⇝n, d∈p.

**assumptions:** Finite directed CFG with one selected entry and finite paths including both endpoints. Dominance queries are restricted to entry-reachable nodes; unreachable nodes are outside the relation, avoiding vacuous universal paths. Instruction order inside a block and PHI incoming-edge uses need separate positions. MLIR hierarchical dominance and graph regions require their own instantiation; this entry is the flat CFG relation.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [MLIR Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/LangRef.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/LangRef.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** MLIR LangRef: Value Scoping, Control Flow and SSACFG Regions; LLVM LangRef: Well-Formedness

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

**reviewStatus:** Editorial mathematical statement and derivation; no registered compiled witness.

## Laws

<a id="node-urn-csabs-law-Dominance-reachable-reflexive"></a>

### reachable-reflexive

`urn:csabs:law/Dominance-reachable-reflexive`

**description:** Derived consequence in the stated profile.

**statement:** reachable(n) ⇒ n dom n.

**formalStatement:** reachable(n) ⇒ n dom n.

**assumptions:** Finite directed CFG with one selected entry and finite paths including both endpoints. Dominance queries are restricted to entry-reachable nodes; unreachable nodes are outside the relation, avoiding vacuous universal paths. Instruction order inside a block and PHI incoming-edge uses need separate positions. MLIR hierarchical dominance and graph regions require their own instantiation; this entry is the flat CFG relation.

**dependsOn:** [path-definition](Dominance.md#node-urn-csabs-axiom-Dominance-path-definition)

**proofSketch:** Every path to n contains its endpoint n.

**notationLanguage:** informal mathematical Unicode

**source:** [MLIR Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/LangRef.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/LangRef.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** MLIR LangRef: Value Scoping, Control Flow and SSACFG Regions; LLVM LangRef: Well-Formedness

**sourceNote:** Catalog derivation from the explicit dependsOn premises; the cited source motivates the interface, not this exact editorial theorem name.

**provenanceKind:** derived

**reviewStatus:** Editorial mathematical statement and derivation; no registered compiled witness.

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [MLIR Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/LangRef.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/LangRef.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification
- [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** MLIR LangRef: Value Scoping, Control Flow and SSACFG Regions; LLVM LangRef: Well-Formedness

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/Dominance",
    "type": "Concept",
    "shortForm": "Dominance",
    "fullName": "Reachability-qualified control-flow dominance",
    "definition": "A node d dominates a reachable node n when every finite entry-to-n path contains d, including the path endpoints.",
    "notation": "d dom n ⇔ reachable(n) ∧ ∀p:entry⇝n, d∈p",
    "category": [
      "urn:csabs:category/compiler-transformations"
    ],
    "kind": "urn:csabs:kind/relation",
    "requiresConcept": [
      "urn:csabs:concept/DirectedGraph",
      "urn:csabs:concept/Relation"
    ],
    "relatedConcept": [
      "urn:csabs:concept/SSAForm"
    ],
    "hasOperation": [
      "urn:csabs:operation/Dominance-dominates",
      "urn:csabs:operation/Dominance-strict-dominates"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/Dominance-path-definition"
    ],
    "hasLaw": [
      "urn:csabs:law/Dominance-reachable-reflexive"
    ],
    "hasTheorem": [],
    "basisKind": "relational-structural-definition",
    "basisScope": "Finite directed CFG with one selected entry and finite paths including both endpoints. Dominance queries are restricted to entry-reachable nodes; unreachable nodes are outside the relation, avoiding vacuous universal paths. Instruction order inside a block and PHI incoming-edge uses need separate positions. MLIR hierarchical dominance and graph regions require their own instantiation; this entry is the flat CFG relation.",
    "axiomBasis": "d dom n ↔ reachable(n) ∧ ∀p:entry⇝n, d∈p.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.",
    "verificationObligation": [
      "Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.",
      "Path oracle adequacy to the CFG is a client obligation; no dominator algorithm, instruction-order model, postdominance or hierarchical-region implementation."
    ],
    "source": [
      "urn:csabs:source/compiler-mlir",
      "urn:csabs:source/compiler-llvm"
    ],
    "sourceLocator": "MLIR LangRef: Value Scoping, Control Flow and SSACFG Regions; LLVM LangRef: Well-Formedness",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/Relation"
    ],
    "specializationNote": "Instantiate the parent carrier and operation as follows: Relation on vertices using a supplied finite-path oracle; endpoints included and existence required.",
    "mathematicalFormulation": "A node d dominates a reachable node n when every finite entry-to-n path contains d, including the path endpoints. d dom n ⇔ reachable(n) ∧ ∀p:entry⇝n, d∈p Finite directed CFG with one selected entry and finite paths including both endpoints. Dominance queries are restricted to entry-reachable nodes; unreachable nodes are outside the relation, avoiding vacuous universal paths. Instruction order inside a block and PHI incoming-edge uses need separate positions. MLIR hierarchical dominance and graph regions require their own instantiation; this entry is the flat CFG relation.",
    "leanFormulation": "def Dominance {V : Type u} (paths : V → V → List V → Prop)\n    (entry dominator node : V) : Prop :=\n  (∃ path, paths entry node path) ∧\n    ∀ path, paths entry node path → dominator ∈ path",
    "formulationSource": "urn:csabs:source/compiler-lean",
    "formulationLocator": "Catalog.Transforms.Dominance",
    "formulationScope": "partial",
    "leanModelMapping": "Relation on vertices using a supplied finite-path oracle; endpoints included and existence required.",
    "leanModelLimitations": "Path oracle adequacy to the CFG is a client obligation; no dominator algorithm, instruction-order model, postdominance or hierarchical-region implementation."
  },
  {
    "id": "urn:csabs:operation/Dominance-dominates",
    "type": "Operation",
    "name": "dominates",
    "signature": "dominates : Node×Node→Prop",
    "description": "Require reachability and occurrence on every entry path.",
    "concept": "urn:csabs:concept/Dominance",
    "precondition": "Selected CFG and entry.",
    "postcondition": "Require reachability and occurrence on every entry path.",
    "totality": "Total predicate; false for unreachable endpoints.",
    "source": [
      "urn:csabs:source/compiler-mlir",
      "urn:csabs:source/compiler-llvm"
    ],
    "sourceLocator": "MLIR LangRef: Value Scoping, Control Flow and SSACFG Regions; LLVM LangRef: Well-Formedness",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/Dominance-strict-dominates",
    "type": "Operation",
    "name": "strict-dominates",
    "signature": "strictDominates : Node×Node→Prop",
    "description": "Require dominance and distinct nodes.",
    "concept": "urn:csabs:concept/Dominance",
    "precondition": "Node identity fixed.",
    "postcondition": "Require dominance and distinct nodes.",
    "totality": "Total predicate.",
    "source": [
      "urn:csabs:source/compiler-mlir",
      "urn:csabs:source/compiler-llvm"
    ],
    "sourceLocator": "MLIR LangRef: Value Scoping, Control Flow and SSACFG Regions; LLVM LangRef: Well-Formedness",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/Dominance-path-definition",
    "type": "Axiom",
    "name": "path-definition",
    "description": "Defining obligation for Reachability-qualified control-flow dominance",
    "statement": "d dom n ↔ reachable(n) ∧ ∀p:entry⇝n, d∈p.",
    "formalStatement": "d dom n ↔ reachable(n) ∧ ∀p:entry⇝n, d∈p.",
    "assumptions": [
      "Finite directed CFG with one selected entry and finite paths including both endpoints. Dominance queries are restricted to entry-reachable nodes; unreachable nodes are outside the relation, avoiding vacuous universal paths. Instruction order inside a block and PHI incoming-edge uses need separate positions. MLIR hierarchical dominance and graph regions require their own instantiation; this entry is the flat CFG relation."
    ],
    "appliesTo": [
      "urn:csabs:concept/Dominance"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-mlir",
      "urn:csabs:source/compiler-llvm"
    ],
    "sourceLocator": "MLIR LangRef: Value Scoping, Control Flow and SSACFG Regions; LLVM LangRef: Well-Formedness",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial mathematical statement and derivation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:law/Dominance-reachable-reflexive",
    "type": "Law",
    "name": "reachable-reflexive",
    "description": "Derived consequence in the stated profile.",
    "statement": "reachable(n) ⇒ n dom n.",
    "formalStatement": "reachable(n) ⇒ n dom n.",
    "assumptions": [
      "Finite directed CFG with one selected entry and finite paths including both endpoints. Dominance queries are restricted to entry-reachable nodes; unreachable nodes are outside the relation, avoiding vacuous universal paths. Instruction order inside a block and PHI incoming-edge uses need separate positions. MLIR hierarchical dominance and graph regions require their own instantiation; this entry is the flat CFG relation."
    ],
    "appliesTo": [
      "urn:csabs:concept/Dominance"
    ],
    "dependsOn": [
      "urn:csabs:axiom/Dominance-path-definition"
    ],
    "proofSketch": "Every path to n contains its endpoint n.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-mlir",
      "urn:csabs:source/compiler-llvm"
    ],
    "sourceLocator": "MLIR LangRef: Value Scoping, Control Flow and SSACFG Regions; LLVM LangRef: Well-Formedness",
    "sourceNote": "Catalog derivation from the explicit dependsOn premises; the cited source motivates the interface, not this exact editorial theorem name.",
    "provenanceKind": "derived",
    "reviewStatus": "Editorial mathematical statement and derivation; no registered compiled witness."
  }
]
```
<!-- graph-record:end -->
