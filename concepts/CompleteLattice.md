# Complete Lattice

A partially ordered set in which every subset, including the empty subset, has a supremum and an infimum.

**Notation:** ∀S⊆L: sup S and inf S exist

**Stable ID:** `urn:csabs:concept/CompleteLattice`

**Categories:** Order and fixed points

**Kind:** Mathematical structure

**Prerequisites:** [Lattice](Lattice.md)

**Specializes:** [Lattice](Lattice.md)

## Mathematical formulation

A complete lattice has sup(S) and inf(S) for every S⊆A, with sup(S)≤x ⇔ ∀s∈S,s≤x and x≤inf(S) ⇔ ∀s∈S,x≤s. In particular sup(∅)=⊥ and inf(∅)=⊤.

**Lean formulation** (in its source module context):

```lean
abbrev CompleteLattice (A : Type u) := _root_.CompleteLattice A
```

**Source:** [`Catalog.CompleteLattice`](../lean/Catalog/Order.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Mathlib CompleteLattice, including sup/inf of the empty subset.

**Limits:** Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Selected presentation: A partially ordered set in which every subset, including the empty subset, has a supremum and an infimum. Governing rules: The underlying relation is a partial order. Every subset, including empty, has a least upper bound. Every subset, including empty, has a greatest lower bound.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**specializationNote:** Instantiate meet and join as infimum and supremum of pairs on the same carrier. Bounds of the empty subset also supply top and bottom.

**verificationObligation:** Instantiate carrier, equality, and stated semantic conventions before using this entry.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

**provenanceStatus:** legacy-source-missing

## Operations

<a id="node-urn-csabs-operation-CompleteLattice-supremum"></a>

### supremum

`urn:csabs:operation/CompleteLattice-supremum`

**signature:** sup : 𝒫(L)→L

**description:** Returns the least upper bound, including bottom for the empty subset.

<a id="node-urn-csabs-operation-CompleteLattice-infimum"></a>

### infimum

`urn:csabs:operation/CompleteLattice-infimum`

**signature:** inf : 𝒫(L)→L

**description:** Returns the greatest lower bound, including top for the empty subset.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-CompleteLattice-partial-order"></a>

### partial-order

`urn:csabs:axiom/CompleteLattice-partial-order`

**statement:** The underlying relation is a partial order.

**formalStatement:** x≤x; x≤y∧y≤z⇒x≤z; x≤y∧y≤x⇒x=y

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-CompleteLattice-supremum"></a>

### supremum

`urn:csabs:axiom/CompleteLattice-supremum`

**statement:** Every subset, including empty, has a least upper bound.

**formalStatement:** sup(X)≤z iff ∀x∈X:x≤z; ∀x∈X:x≤sup(X)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-CompleteLattice-infimum"></a>

### infimum

`urn:csabs:axiom/CompleteLattice-infimum`

**statement:** Every subset, including empty, has a greatest lower bound.

**formalStatement:** z≤inf(X) iff ∀x∈X:z≤x; ∀x∈X:inf(X)≤x

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-law-CompleteLattice-core"></a>

### law/CompleteLattice-core

`urn:csabs:law/CompleteLattice-core`

**statement:** Every monotone self-map has a least and a greatest fixed point (Knaster–Tarski).

**formalStatement:** f monotone ⇒ Fix(f) is a complete lattice under the inherited order

**reviewStatus:** editorial-summary; not machine-proved

**assumptions:** Use the carrier and semantic convention in the linked concept definition.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [partial-order](CompleteLattice.md#node-urn-csabs-axiom-CompleteLattice-partial-order); [supremum](CompleteLattice.md#node-urn-csabs-axiom-CompleteLattice-supremum); [infimum](CompleteLattice.md#node-urn-csabs-axiom-CompleteLattice-infimum)

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-theorem-CompleteLattice-empty-extrema"></a>

### empty-extrema

`urn:csabs:theorem/CompleteLattice-empty-extrema`

**statement:** The empty supremum is bottom and the empty infimum is top.

**formalStatement:** ⊥=sup(∅); ⊤=inf(∅); ∀x:⊥≤x≤⊤

**proofSketch:** The bound conditions for an empty family hold vacuously.

**assumptions:** The explicit basis, carriers, and side conditions stated for CompleteLattice apply.

**dependsOn:** [partial-order](CompleteLattice.md#node-urn-csabs-axiom-CompleteLattice-partial-order); [supremum](CompleteLattice.md#node-urn-csabs-axiom-CompleteLattice-supremum); [infimum](CompleteLattice.md#node-urn-csabs-axiom-CompleteLattice-infimum)

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
    "id": "urn:csabs:concept/CompleteLattice",
    "type": "Concept",
    "shortForm": "CompleteLattice",
    "fullName": "Complete Lattice",
    "category": [
      "urn:csabs:category/order"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "A partially ordered set in which every subset, including the empty subset, has a supremum and an infimum.",
    "notation": "∀S⊆L: sup S and inf S exist",
    "hasOperation": [
      "urn:csabs:operation/CompleteLattice-supremum",
      "urn:csabs:operation/CompleteLattice-infimum"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/CompleteLattice-partial-order",
      "urn:csabs:axiom/CompleteLattice-supremum",
      "urn:csabs:axiom/CompleteLattice-infimum"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:law/CompleteLattice-core",
      "urn:csabs:theorem/CompleteLattice-empty-extrema"
    ],
    "requiresConcept": [
      "urn:csabs:concept/Lattice"
    ],
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Instantiate carrier, equality, and stated semantic conventions before using this entry.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: A partially ordered set in which every subset, including the empty subset, has a supremum and an infimum. Governing rules: The underlying relation is a partial order. Every subset, including empty, has a least upper bound. Every subset, including empty, has a greatest lower bound.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "provenanceStatus": "legacy-source-missing",
    "specializationOf": [
      "urn:csabs:concept/Lattice"
    ],
    "specializationNote": "Instantiate meet and join as infimum and supremum of pairs on the same carrier. Bounds of the empty subset also supply top and bottom.",
    "leanFormulation": "abbrev CompleteLattice (A : Type u) := _root_.CompleteLattice A",
    "formulationSource": "urn:csabs:source/local-lean-Order",
    "formulationLocator": "Catalog.CompleteLattice",
    "formulationScope": "model",
    "leanModelMapping": "Mathlib CompleteLattice, including sup/inf of the empty subset.",
    "leanModelLimitations": "Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.",
    "mathematicalFormulation": "A complete lattice has sup(S) and inf(S) for every S⊆A, with sup(S)≤x ⇔ ∀s∈S,s≤x and x≤inf(S) ⇔ ∀s∈S,x≤s. In particular sup(∅)=⊥ and inf(∅)=⊤."
  },
  {
    "id": "urn:csabs:operation/CompleteLattice-supremum",
    "type": "Operation",
    "name": "supremum",
    "signature": "sup : 𝒫(L)→L",
    "description": "Returns the least upper bound, including bottom for the empty subset.",
    "concept": "urn:csabs:concept/CompleteLattice"
  },
  {
    "id": "urn:csabs:operation/CompleteLattice-infimum",
    "type": "Operation",
    "name": "infimum",
    "signature": "inf : 𝒫(L)→L",
    "description": "Returns the greatest lower bound, including top for the empty subset.",
    "concept": "urn:csabs:concept/CompleteLattice"
  },
  {
    "id": "urn:csabs:axiom/CompleteLattice-partial-order",
    "type": "Axiom",
    "name": "partial-order",
    "statement": "The underlying relation is a partial order.",
    "formalStatement": "x≤x; x≤y∧y≤z⇒x≤z; x≤y∧y≤x⇒x=y",
    "appliesTo": [
      "urn:csabs:concept/CompleteLattice"
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
    "id": "urn:csabs:axiom/CompleteLattice-supremum",
    "type": "Axiom",
    "name": "supremum",
    "statement": "Every subset, including empty, has a least upper bound.",
    "formalStatement": "sup(X)≤z iff ∀x∈X:x≤z; ∀x∈X:x≤sup(X)",
    "appliesTo": [
      "urn:csabs:concept/CompleteLattice"
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
    "id": "urn:csabs:axiom/CompleteLattice-infimum",
    "type": "Axiom",
    "name": "infimum",
    "statement": "Every subset, including empty, has a greatest lower bound.",
    "formalStatement": "z≤inf(X) iff ∀x∈X:z≤x; ∀x∈X:inf(X)≤x",
    "appliesTo": [
      "urn:csabs:concept/CompleteLattice"
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
    "id": "urn:csabs:law/CompleteLattice-core",
    "type": "Theorem",
    "statement": "Every monotone self-map has a least and a greatest fixed point (Knaster–Tarski).",
    "formalStatement": "f monotone ⇒ Fix(f) is a complete lattice under the inherited order",
    "appliesTo": [
      "urn:csabs:concept/CompleteLattice"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "assumptions": [
      "Use the carrier and semantic convention in the linked concept definition."
    ],
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/CompleteLattice-partial-order",
      "urn:csabs:axiom/CompleteLattice-supremum",
      "urn:csabs:axiom/CompleteLattice-infimum"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/CompleteLattice-empty-extrema",
    "type": "Theorem",
    "name": "empty-extrema",
    "statement": "The empty supremum is bottom and the empty infimum is top.",
    "formalStatement": "⊥=sup(∅); ⊤=inf(∅); ∀x:⊥≤x≤⊤",
    "proofSketch": "The bound conditions for an empty family hold vacuously.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for CompleteLattice apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/CompleteLattice"
    ],
    "dependsOn": [
      "urn:csabs:axiom/CompleteLattice-partial-order",
      "urn:csabs:axiom/CompleteLattice-supremum",
      "urn:csabs:axiom/CompleteLattice-infimum"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
