# Monotone Function

A function between ordered sets that preserves their order.

**Notation:** f:A→B; x≤A y ⇒ f(x)≤B f(y)

**Stable ID:** `urn:csabs:concept/MonotoneFunction`

**Categories:** Order and fixed points

**Kind:** Function

**Prerequisites:** [Total function](Function.md), [Partial Order](PartialOrder.md)

**Specializes:** [Total function](Function.md)

## Backlinks

- [Closure Operator](ClosureOperator.md) — `specializationOf`
- [Galois Connection](GaloisConnection.md) — `requiresConcept`

## Mathematical formulation

For preorders A,B, Mon(A,B)={f:A→B | ∀a,a′,a≤a′⇒f(a)≤f(a′)}. Equality of these maps is pointwise carrier equality.

**Lean formulation** (in its source module context):

```lean
abbrev MonotoneFunction (A : Type u) (B : Type v)
    [_root_.Preorder A] [_root_.Preorder B] := A →o B
```

**Source:** [`Catalog.MonotoneFunction`](../lean/Catalog/Order.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Mathlib OrderHom A B, packaging a total map and monotonicity.

**Limits:** Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Selected presentation: A function between ordered sets that preserves their order. Governing rules: A total function preserves the specified orders on its source and target.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**specializationNote:** Forget the order-preservation requirement and retain the same total function, domain and codomain.

**verificationObligation:** Instantiate carrier, equality, and stated semantic conventions before using this entry.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

**provenanceStatus:** legacy-source-missing

## Operations

<a id="node-urn-csabs-operation-MonotoneFunction-application"></a>

### application

`urn:csabs:operation/MonotoneFunction-application`

**signature:** f : A→B

**description:** Applies an order-preserving function.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-MonotoneFunction-order-preservation"></a>

### order-preservation

`urn:csabs:axiom/MonotoneFunction-order-preservation`

**statement:** A total function preserves the specified orders on its source and target.

**formalStatement:** f:A→B; x≤A y ⇒ f(x)≤B f(y)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

<a id="node-urn-csabs-law-MonotoneFunction-core"></a>

### law/MonotoneFunction-core

`urn:csabs:law/MonotoneFunction-core`

**statement:** Composition of monotone functions is monotone.

**formalStatement:** f,g monotone ⇒ g∘f monotone

**reviewStatus:** editorial-summary; not machine-proved

**assumptions:** Use the carrier and semantic convention in the linked concept definition.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [order-preservation](MonotoneFunction.md#node-urn-csabs-axiom-MonotoneFunction-order-preservation)

**provenanceStatus:** legacy-source-missing

## Theorems

<a id="node-urn-csabs-theorem-MonotoneFunction-identity-monotone"></a>

### identity-monotone

`urn:csabs:theorem/MonotoneFunction-identity-monotone`

**statement:** The identity map is order preserving.

**formalStatement:** x≤y ⇒ id(x)≤id(y)

**proofSketch:** Identity leaves each side of the original inequality unchanged.

**assumptions:** The explicit basis, carriers, and side conditions stated for MonotoneFunction apply.

**dependsOn:** [order-preservation](MonotoneFunction.md#node-urn-csabs-axiom-MonotoneFunction-order-preservation)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Concept provenance

Historical source gap retained; see `provenanceStatus` and the frozen baseline.

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/MonotoneFunction",
    "type": "Concept",
    "shortForm": "MonotoneFunction",
    "fullName": "Monotone Function",
    "category": [
      "urn:csabs:category/order"
    ],
    "kind": "urn:csabs:kind/function",
    "definition": "A function between ordered sets that preserves their order.",
    "notation": "f:A→B; x≤A y ⇒ f(x)≤B f(y)",
    "hasOperation": [
      "urn:csabs:operation/MonotoneFunction-application"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/MonotoneFunction-order-preservation"
    ],
    "hasLaw": [
      "urn:csabs:law/MonotoneFunction-core"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/MonotoneFunction-identity-monotone"
    ],
    "requiresConcept": [
      "urn:csabs:concept/Function",
      "urn:csabs:concept/PartialOrder"
    ],
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Instantiate carrier, equality, and stated semantic conventions before using this entry.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: A function between ordered sets that preserves their order. Governing rules: A total function preserves the specified orders on its source and target.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "provenanceStatus": "legacy-source-missing",
    "specializationOf": [
      "urn:csabs:concept/Function"
    ],
    "specializationNote": "Forget the order-preservation requirement and retain the same total function, domain and codomain.",
    "leanFormulation": "abbrev MonotoneFunction (A : Type u) (B : Type v)\n    [_root_.Preorder A] [_root_.Preorder B] := A →o B",
    "formulationSource": "urn:csabs:source/local-lean-Order",
    "formulationLocator": "Catalog.MonotoneFunction",
    "formulationScope": "model",
    "leanModelMapping": "Mathlib OrderHom A B, packaging a total map and monotonicity.",
    "leanModelLimitations": "Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.",
    "mathematicalFormulation": "For preorders A,B, Mon(A,B)={f:A→B | ∀a,a′,a≤a′⇒f(a)≤f(a′)}. Equality of these maps is pointwise carrier equality."
  },
  {
    "id": "urn:csabs:operation/MonotoneFunction-application",
    "type": "Operation",
    "name": "application",
    "signature": "f : A→B",
    "description": "Applies an order-preserving function.",
    "concept": "urn:csabs:concept/MonotoneFunction"
  },
  {
    "id": "urn:csabs:axiom/MonotoneFunction-order-preservation",
    "type": "Axiom",
    "name": "order-preservation",
    "statement": "A total function preserves the specified orders on its source and target.",
    "formalStatement": "f:A→B; x≤A y ⇒ f(x)≤B f(y)",
    "appliesTo": [
      "urn:csabs:concept/MonotoneFunction"
    ],
    "assumptions": [
      "All variables range over the carriers and semantic conventions specified in this concept."
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:law/MonotoneFunction-core",
    "type": "Law",
    "statement": "Composition of monotone functions is monotone.",
    "formalStatement": "f,g monotone ⇒ g∘f monotone",
    "appliesTo": [
      "urn:csabs:concept/MonotoneFunction"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "assumptions": [
      "Use the carrier and semantic convention in the linked concept definition."
    ],
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/MonotoneFunction-order-preservation"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/MonotoneFunction-identity-monotone",
    "type": "Theorem",
    "name": "identity-monotone",
    "statement": "The identity map is order preserving.",
    "formalStatement": "x≤y ⇒ id(x)≤id(y)",
    "proofSketch": "Identity leaves each side of the original inequality unchanged.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for MonotoneFunction apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/MonotoneFunction"
    ],
    "dependsOn": [
      "urn:csabs:axiom/MonotoneFunction-order-preservation"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
