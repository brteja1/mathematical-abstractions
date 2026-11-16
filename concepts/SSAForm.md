# Typed static single assignment with scoped uses

An IR discipline giving each value identity one definition and requiring each use to have the expected type and an available definition at that use position.

**Notation:** def:Value→Position; ∀u, available(def(operand(u)),pos(u)) ∧ ty(operand(u))=expected(u)

**Stable ID:** `urn:csabs:concept/SSAForm`

**Categories:** Programming-language semantics → Compiler transformations

**Kind:** semantic-model

**Prerequisites:** [Reachability-qualified control-flow dominance](Dominance.md), [Total function](Function.md)

**Related concepts:** [Finite directed multigraph with edge identities](DirectedMultigraph.md), [Free ranked term algebra with variables](TermAlgebra.md), [Typed IR legalization with representation relation](DialectConversion.md)

## Backlinks

- [Analysis validity across IR mutation](AnalysisPreservation.md) — `relatedConcept`
- [CFG refinement with path correspondence and progress](ControlFlowRefinement.md) — `requiresConcept`
- [Typed IR legalization with representation relation](DialectConversion.md) — `requiresConcept`
- [Reachability-qualified control-flow dominance](Dominance.md) — `relatedConcept`
- [Guarded contextual program rewrite](GuardedRewrite.md) — `relatedConcept`
- [LLVM scalar deferred undefinedness and freeze](LLVMPoisonSemantics.md) — `relatedConcept`
- [Conservative SSA indexing of memory versions](MemorySSA.md) — `requiresConcept`
- [Observable state representation relation](StateRepresentation.md) — `relatedConcept`

## Mathematical formulation

An IR discipline giving each value identity one definition and requiring each use to have the expected type and an available definition at that use position. def:Value→Position; ∀u, available(def(operand(u)),pos(u)) ∧ ty(operand(u))=expected(u) Value identity is independent of spelling and numeric equality. Definitions include operation results and block arguments. In reachable flat SSACFG regions availability uses block dominance and within-block order; PHI operands are used on incoming edges, and MLIR successor arguments bind block parameters. Nested captures respect region scope and IsolatedFromAbove. Graph regions need their documented availability convention and must not inherit SSACFG ordering. Ill-typed or out-of-scope IR has no well-formed semantics in this profile.

**Lean formulation** (in its source module context):

```lean
structure SSAForm (Value Use Position Ty : Type u) where
  definition : Value → Position
  operand : Use → Value
  usePosition : Use → Position
  available : Position → Position → Prop
  valueType : Value → Ty
  expectedType : Use → Ty
  availableAtUse : ∀ use, available (definition (operand use)) (usePosition use)
  typedUse : ∀ use, valueType (operand use) = expectedType use
```

**Source:** [`Catalog.Transforms.SSAForm`](../lean/Catalog/CompilerTransforms.lean); consulted 2026-11-16.

**Scope:** partial

**Interpretation:** Definition function and operand/type/availability functions with explicit typed-use and availability structure laws.

**Limits:** No parser, CFG path construction, edge-argument semantics or hierarchical visibility implementation. Structural validity does not prove a value replacement semantically sound.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** ∀v∈Values, ∃!p, defines(p,v).; ∀u∈Uses, available(def(operand(u)),pos(u)) ∧ ty(operand(u))=expected(u).

**basisKind:** relational-structural-definition

**basisScope:** Value identity is independent of spelling and numeric equality. Definitions include operation results and block arguments. In reachable flat SSACFG regions availability uses block dominance and within-block order; PHI operands are used on incoming edges, and MLIR successor arguments bind block parameters. Nested captures respect region scope and IsolatedFromAbove. Graph regions need their documented availability convention and must not inherit SSACFG ordering. Ill-typed or out-of-scope IR has no well-formed semantics in this profile.

**verificationObligation:** Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.; No parser, CFG path construction, edge-argument semantics or hierarchical visibility implementation. Structural validity does not prove a value replacement semantically sound.

**reviewStatus:** Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-SSAForm-definition"></a>

### definition

`urn:csabs:operation/SSAForm-definition`

**signature:** definition : Value→Position

**description:** Return the unique definition associated with a value identity.

**precondition:** Well-formed IR.

**postcondition:** Return the unique definition associated with a value identity.

**totality:** Total on defined value identities.

**source:** [MLIR Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/LangRef.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/LangRef.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** MLIR LangRef: Blocks, Value Scoping, Control Flow and SSACFG Regions, Graph Regions; LLVM LangRef: Well-Formedness

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-SSAForm-replace-uses"></a>

### replace-uses

`urn:csabs:operation/SSAForm-replace-uses`

**signature:** replaceUses : IR×Value×Value⇀IR

**description:** Replace selected uses only when replacement types and availability hold at each use.

**precondition:** Old/new values and uses mapped; preserve region isolation and edge arguments.

**postcondition:** Replace selected uses only when replacement types and availability hold at each use.

**totality:** Partial; reject if any structural condition fails.

**source:** [MLIR Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/LangRef.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/LangRef.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** MLIR LangRef: Blocks, Value Scoping, Control Flow and SSACFG Regions, Graph Regions; LLVM LangRef: Well-Formedness

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-SSAForm-unique-definition"></a>

### unique-definition

`urn:csabs:axiom/SSAForm-unique-definition`

**description:** Defining obligation for Typed static single assignment with scoped uses

**statement:** ∀v∈Values, ∃!p, defines(p,v).

**formalStatement:** ∀v∈Values, ∃!p, defines(p,v).

**assumptions:** Value identity is independent of spelling and numeric equality. Definitions include operation results and block arguments. In reachable flat SSACFG regions availability uses block dominance and within-block order; PHI operands are used on incoming edges, and MLIR successor arguments bind block parameters. Nested captures respect region scope and IsolatedFromAbove. Graph regions need their documented availability convention and must not inherit SSACFG ordering. Ill-typed or out-of-scope IR has no well-formed semantics in this profile.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [MLIR Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/LangRef.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/LangRef.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** MLIR LangRef: Blocks, Value Scoping, Control Flow and SSACFG Regions, Graph Regions; LLVM LangRef: Well-Formedness

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

**reviewStatus:** Editorial mathematical statement and derivation; no registered compiled witness.

<a id="node-urn-csabs-axiom-SSAForm-available-typed-use"></a>

### available-typed-use

`urn:csabs:axiom/SSAForm-available-typed-use`

**description:** Defining obligation for Typed static single assignment with scoped uses

**statement:** ∀u∈Uses, available(def(operand(u)),pos(u)) ∧ ty(operand(u))=expected(u).

**formalStatement:** ∀u∈Uses, available(def(operand(u)),pos(u)) ∧ ty(operand(u))=expected(u).

**assumptions:** Value identity is independent of spelling and numeric equality. Definitions include operation results and block arguments. In reachable flat SSACFG regions availability uses block dominance and within-block order; PHI operands are used on incoming edges, and MLIR successor arguments bind block parameters. Nested captures respect region scope and IsolatedFromAbove. Graph regions need their documented availability convention and must not inherit SSACFG ordering. Ill-typed or out-of-scope IR has no well-formed semantics in this profile.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [MLIR Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/LangRef.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/LangRef.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** MLIR LangRef: Blocks, Value Scoping, Control Flow and SSACFG Regions, Graph Regions; LLVM LangRef: Well-Formedness

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

**reviewStatus:** Editorial mathematical statement and derivation; no registered compiled witness.

## Laws

<a id="node-urn-csabs-law-SSAForm-replacement-type-obligation"></a>

### replacement-type-obligation

`urn:csabs:law/SSAForm-replacement-type-obligation`

**description:** Derived consequence within the selected semantic profile.

**statement:** Replacing a use expecting type τ by v with ty(v)≠τ violates this typed SSA interface.

**formalStatement:** Replacing a use expecting type τ by v with ty(v)≠τ violates this typed SSA interface.

**assumptions:** Value identity is independent of spelling and numeric equality. Definitions include operation results and block arguments. In reachable flat SSACFG regions availability uses block dominance and within-block order; PHI operands are used on incoming edges, and MLIR successor arguments bind block parameters. Nested captures respect region scope and IsolatedFromAbove. Graph regions need their documented availability convention and must not inherit SSACFG ordering. Ill-typed or out-of-scope IR has no well-formed semantics in this profile.

**dependsOn:** [available-typed-use](SSAForm.md#node-urn-csabs-axiom-SSAForm-available-typed-use)

**proofSketch:** The typed-use conjunct would require ty(v)=τ, contradicting the supplied inequality. This is a structural rejection, independent of numeric value equality.

**reviewStatus:** Editorial mathematical derivation; no registered compiled witness.

**notationLanguage:** informal mathematical Unicode

**source:** [MLIR Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/LangRef.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/LangRef.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** MLIR LangRef: Blocks, Value Scoping, Control Flow and SSACFG Regions, Graph Regions; LLVM LangRef: Well-Formedness

**sourceNote:** Derived from the explicit dependsOn premises under the stated assumptions; exact claim and proof sketch are editorial.

**provenanceKind:** derived

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [MLIR Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/LangRef.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/LangRef.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification
- [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** MLIR LangRef: Blocks, Value Scoping, Control Flow and SSACFG Regions, Graph Regions; LLVM LangRef: Well-Formedness

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/SSAForm",
    "type": "Concept",
    "shortForm": "SSAForm",
    "fullName": "Typed static single assignment with scoped uses",
    "definition": "An IR discipline giving each value identity one definition and requiring each use to have the expected type and an available definition at that use position.",
    "notation": "def:Value→Position; ∀u, available(def(operand(u)),pos(u)) ∧ ty(operand(u))=expected(u)",
    "category": [
      "urn:csabs:category/compiler-transformations"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "requiresConcept": [
      "urn:csabs:concept/Dominance",
      "urn:csabs:concept/Function"
    ],
    "relatedConcept": [
      "urn:csabs:concept/DirectedMultigraph",
      "urn:csabs:concept/TermAlgebra",
      "urn:csabs:concept/DialectConversion"
    ],
    "hasOperation": [
      "urn:csabs:operation/SSAForm-definition",
      "urn:csabs:operation/SSAForm-replace-uses"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/SSAForm-unique-definition",
      "urn:csabs:axiom/SSAForm-available-typed-use"
    ],
    "hasLaw": [
      "urn:csabs:law/SSAForm-replacement-type-obligation"
    ],
    "hasTheorem": [],
    "basisKind": "relational-structural-definition",
    "basisScope": "Value identity is independent of spelling and numeric equality. Definitions include operation results and block arguments. In reachable flat SSACFG regions availability uses block dominance and within-block order; PHI operands are used on incoming edges, and MLIR successor arguments bind block parameters. Nested captures respect region scope and IsolatedFromAbove. Graph regions need their documented availability convention and must not inherit SSACFG ordering. Ill-typed or out-of-scope IR has no well-formed semantics in this profile.",
    "axiomBasis": "∀v∈Values, ∃!p, defines(p,v).; ∀u∈Uses, available(def(operand(u)),pos(u)) ∧ ty(operand(u))=expected(u).",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.",
    "verificationObligation": [
      "Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.",
      "No parser, CFG path construction, edge-argument semantics or hierarchical visibility implementation. Structural validity does not prove a value replacement semantically sound."
    ],
    "source": [
      "urn:csabs:source/compiler-mlir",
      "urn:csabs:source/compiler-llvm"
    ],
    "sourceLocator": "MLIR LangRef: Blocks, Value Scoping, Control Flow and SSACFG Regions, Graph Regions; LLVM LangRef: Well-Formedness",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted",
    "mathematicalFormulation": "An IR discipline giving each value identity one definition and requiring each use to have the expected type and an available definition at that use position. def:Value→Position; ∀u, available(def(operand(u)),pos(u)) ∧ ty(operand(u))=expected(u) Value identity is independent of spelling and numeric equality. Definitions include operation results and block arguments. In reachable flat SSACFG regions availability uses block dominance and within-block order; PHI operands are used on incoming edges, and MLIR successor arguments bind block parameters. Nested captures respect region scope and IsolatedFromAbove. Graph regions need their documented availability convention and must not inherit SSACFG ordering. Ill-typed or out-of-scope IR has no well-formed semantics in this profile.",
    "leanFormulation": "structure SSAForm (Value Use Position Ty : Type u) where\n  definition : Value → Position\n  operand : Use → Value\n  usePosition : Use → Position\n  available : Position → Position → Prop\n  valueType : Value → Ty\n  expectedType : Use → Ty\n  availableAtUse : ∀ use, available (definition (operand use)) (usePosition use)\n  typedUse : ∀ use, valueType (operand use) = expectedType use",
    "formulationSource": "urn:csabs:source/compiler-lean",
    "formulationLocator": "Catalog.Transforms.SSAForm",
    "formulationScope": "partial",
    "leanModelMapping": "Definition function and operand/type/availability functions with explicit typed-use and availability structure laws.",
    "leanModelLimitations": "No parser, CFG path construction, edge-argument semantics or hierarchical visibility implementation. Structural validity does not prove a value replacement semantically sound."
  },
  {
    "id": "urn:csabs:operation/SSAForm-definition",
    "type": "Operation",
    "name": "definition",
    "signature": "definition : Value→Position",
    "description": "Return the unique definition associated with a value identity.",
    "concept": "urn:csabs:concept/SSAForm",
    "precondition": "Well-formed IR.",
    "postcondition": "Return the unique definition associated with a value identity.",
    "totality": "Total on defined value identities.",
    "source": [
      "urn:csabs:source/compiler-mlir",
      "urn:csabs:source/compiler-llvm"
    ],
    "sourceLocator": "MLIR LangRef: Blocks, Value Scoping, Control Flow and SSACFG Regions, Graph Regions; LLVM LangRef: Well-Formedness",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/SSAForm-replace-uses",
    "type": "Operation",
    "name": "replace-uses",
    "signature": "replaceUses : IR×Value×Value⇀IR",
    "description": "Replace selected uses only when replacement types and availability hold at each use.",
    "concept": "urn:csabs:concept/SSAForm",
    "precondition": "Old/new values and uses mapped; preserve region isolation and edge arguments.",
    "postcondition": "Replace selected uses only when replacement types and availability hold at each use.",
    "totality": "Partial; reject if any structural condition fails.",
    "source": [
      "urn:csabs:source/compiler-mlir",
      "urn:csabs:source/compiler-llvm"
    ],
    "sourceLocator": "MLIR LangRef: Blocks, Value Scoping, Control Flow and SSACFG Regions, Graph Regions; LLVM LangRef: Well-Formedness",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/SSAForm-unique-definition",
    "type": "Axiom",
    "name": "unique-definition",
    "description": "Defining obligation for Typed static single assignment with scoped uses",
    "statement": "∀v∈Values, ∃!p, defines(p,v).",
    "formalStatement": "∀v∈Values, ∃!p, defines(p,v).",
    "assumptions": [
      "Value identity is independent of spelling and numeric equality. Definitions include operation results and block arguments. In reachable flat SSACFG regions availability uses block dominance and within-block order; PHI operands are used on incoming edges, and MLIR successor arguments bind block parameters. Nested captures respect region scope and IsolatedFromAbove. Graph regions need their documented availability convention and must not inherit SSACFG ordering. Ill-typed or out-of-scope IR has no well-formed semantics in this profile."
    ],
    "appliesTo": [
      "urn:csabs:concept/SSAForm"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-mlir",
      "urn:csabs:source/compiler-llvm"
    ],
    "sourceLocator": "MLIR LangRef: Blocks, Value Scoping, Control Flow and SSACFG Regions, Graph Regions; LLVM LangRef: Well-Formedness",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial mathematical statement and derivation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:axiom/SSAForm-available-typed-use",
    "type": "Axiom",
    "name": "available-typed-use",
    "description": "Defining obligation for Typed static single assignment with scoped uses",
    "statement": "∀u∈Uses, available(def(operand(u)),pos(u)) ∧ ty(operand(u))=expected(u).",
    "formalStatement": "∀u∈Uses, available(def(operand(u)),pos(u)) ∧ ty(operand(u))=expected(u).",
    "assumptions": [
      "Value identity is independent of spelling and numeric equality. Definitions include operation results and block arguments. In reachable flat SSACFG regions availability uses block dominance and within-block order; PHI operands are used on incoming edges, and MLIR successor arguments bind block parameters. Nested captures respect region scope and IsolatedFromAbove. Graph regions need their documented availability convention and must not inherit SSACFG ordering. Ill-typed or out-of-scope IR has no well-formed semantics in this profile."
    ],
    "appliesTo": [
      "urn:csabs:concept/SSAForm"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-mlir",
      "urn:csabs:source/compiler-llvm"
    ],
    "sourceLocator": "MLIR LangRef: Blocks, Value Scoping, Control Flow and SSACFG Regions, Graph Regions; LLVM LangRef: Well-Formedness",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial mathematical statement and derivation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:law/SSAForm-replacement-type-obligation",
    "type": "Law",
    "name": "replacement-type-obligation",
    "description": "Derived consequence within the selected semantic profile.",
    "statement": "Replacing a use expecting type τ by v with ty(v)≠τ violates this typed SSA interface.",
    "formalStatement": "Replacing a use expecting type τ by v with ty(v)≠τ violates this typed SSA interface.",
    "assumptions": [
      "Value identity is independent of spelling and numeric equality. Definitions include operation results and block arguments. In reachable flat SSACFG regions availability uses block dominance and within-block order; PHI operands are used on incoming edges, and MLIR successor arguments bind block parameters. Nested captures respect region scope and IsolatedFromAbove. Graph regions need their documented availability convention and must not inherit SSACFG ordering. Ill-typed or out-of-scope IR has no well-formed semantics in this profile."
    ],
    "appliesTo": [
      "urn:csabs:concept/SSAForm"
    ],
    "dependsOn": [
      "urn:csabs:axiom/SSAForm-available-typed-use"
    ],
    "proofSketch": "The typed-use conjunct would require ty(v)=τ, contradicting the supplied inequality. This is a structural rejection, independent of numeric value equality.",
    "reviewStatus": "Editorial mathematical derivation; no registered compiled witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-mlir",
      "urn:csabs:source/compiler-llvm"
    ],
    "sourceLocator": "MLIR LangRef: Blocks, Value Scoping, Control Flow and SSACFG Regions, Graph Regions; LLVM LangRef: Well-Formedness",
    "sourceNote": "Derived from the explicit dependsOn premises under the stated assumptions; exact claim and proof sketch are editorial.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
