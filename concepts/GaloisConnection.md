# Galois Connection

Two maps between partially ordered sets related by an adjunction inequality.

**Notation:** α:C→A, γ:A→C; α(c)≤a iff c≤γ(a)

**Stable ID:** `urn:csabs:concept/GaloisConnection`

**Categories:** Order and fixed points

**Kind:** Mathematical structure

**Prerequisites:** [Partial Order](PartialOrder.md), [Monotone Function](MonotoneFunction.md)

## Mathematical formulation

For partial orders A,B and maps l:A→B,r:B→A, GC(l,r) ⇔ ∀a∈A,b∈B, l(a)≤b ↔ a≤r(b). The order relation on each side is its own carrier's order.

**Lean formulation** (in its source module context):

```lean
def GaloisConnection {A : Type u} {B : Type v}
    [_root_.PartialOrder A] [_root_.PartialOrder B] (l : A → B) (r : B → A) : Prop :=
  _root_.GaloisConnection l r
```

**Source:** [`Catalog.GaloisConnection`](../lean/Catalog/Order.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Adjunction equivalence l a <= b iff a <= r b on explicit partial orders.

**Limits:** Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Selected presentation: Two maps between partially ordered sets related by an adjunction inequality. Governing rules: The two total functions obey the adjunction equivalence on the specified partial orders.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**verificationObligation:** Instantiate carrier, equality, and stated semantic conventions before using this entry.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

**provenanceStatus:** legacy-source-missing

## Operations

<a id="node-urn-csabs-operation-GaloisConnection-abstraction"></a>

### abstraction

`urn:csabs:operation/GaloisConnection-abstraction`

**signature:** α : C→A

**description:** Maps a concrete element to its abstract approximation.

<a id="node-urn-csabs-operation-GaloisConnection-concretization"></a>

### concretization

`urn:csabs:operation/GaloisConnection-concretization`

**signature:** γ : A→C

**description:** Maps an abstract element to the corresponding concrete bound.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-GaloisConnection-adjunction"></a>

### adjunction

`urn:csabs:axiom/GaloisConnection-adjunction`

**statement:** The two total functions obey the adjunction equivalence on the specified partial orders.

**formalStatement:** α:C→A; γ:A→C; α(c)≤A a iff c≤C γ(a)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

<a id="node-urn-csabs-law-GaloisConnection-core"></a>

### law/GaloisConnection-core

`urn:csabs:law/GaloisConnection-core`

**statement:** The composite γ∘α is an extensive, monotone, idempotent closure operator.

**formalStatement:** c≤γα(c); γαγα(c)=γα(c)

**reviewStatus:** editorial-summary; not machine-proved

**assumptions:** Use the carrier and semantic convention in the linked concept definition.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [adjunction](GaloisConnection.md#node-urn-csabs-axiom-GaloisConnection-adjunction)

**provenanceStatus:** legacy-source-missing

## Theorems

<a id="node-urn-csabs-theorem-GaloisConnection-unit-counit"></a>

### unit-counit

`urn:csabs:theorem/GaloisConnection-unit-counit`

**statement:** An adjoint pair satisfies its unit and counit inequalities.

**formalStatement:** c≤γα(c); αγ(a)≤a

**proofSketch:** Apply the adjunction to the reflexive inequalities α(c)≤α(c) and γ(a)≤γ(a).

**assumptions:** The explicit basis, carriers, and side conditions stated for GaloisConnection apply.

**dependsOn:** [adjunction](GaloisConnection.md#node-urn-csabs-axiom-GaloisConnection-adjunction)

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
    "id": "urn:csabs:concept/GaloisConnection",
    "type": "Concept",
    "shortForm": "GaloisConnection",
    "fullName": "Galois Connection",
    "category": [
      "urn:csabs:category/order"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "Two maps between partially ordered sets related by an adjunction inequality.",
    "notation": "α:C→A, γ:A→C; α(c)≤a iff c≤γ(a)",
    "hasOperation": [
      "urn:csabs:operation/GaloisConnection-abstraction",
      "urn:csabs:operation/GaloisConnection-concretization"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/GaloisConnection-adjunction"
    ],
    "hasLaw": [
      "urn:csabs:law/GaloisConnection-core"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/GaloisConnection-unit-counit"
    ],
    "requiresConcept": [
      "urn:csabs:concept/PartialOrder",
      "urn:csabs:concept/MonotoneFunction"
    ],
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Instantiate carrier, equality, and stated semantic conventions before using this entry.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: Two maps between partially ordered sets related by an adjunction inequality. Governing rules: The two total functions obey the adjunction equivalence on the specified partial orders.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "provenanceStatus": "legacy-source-missing",
    "leanFormulation": "def GaloisConnection {A : Type u} {B : Type v}\n    [_root_.PartialOrder A] [_root_.PartialOrder B] (l : A → B) (r : B → A) : Prop :=\n  _root_.GaloisConnection l r",
    "formulationSource": "urn:csabs:source/local-lean-Order",
    "formulationLocator": "Catalog.GaloisConnection",
    "formulationScope": "model",
    "leanModelMapping": "Adjunction equivalence l a <= b iff a <= r b on explicit partial orders.",
    "leanModelLimitations": "Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.",
    "mathematicalFormulation": "For partial orders A,B and maps l:A→B,r:B→A, GC(l,r) ⇔ ∀a∈A,b∈B, l(a)≤b ↔ a≤r(b). The order relation on each side is its own carrier's order."
  },
  {
    "id": "urn:csabs:operation/GaloisConnection-abstraction",
    "type": "Operation",
    "name": "abstraction",
    "signature": "α : C→A",
    "description": "Maps a concrete element to its abstract approximation.",
    "concept": "urn:csabs:concept/GaloisConnection"
  },
  {
    "id": "urn:csabs:operation/GaloisConnection-concretization",
    "type": "Operation",
    "name": "concretization",
    "signature": "γ : A→C",
    "description": "Maps an abstract element to the corresponding concrete bound.",
    "concept": "urn:csabs:concept/GaloisConnection"
  },
  {
    "id": "urn:csabs:axiom/GaloisConnection-adjunction",
    "type": "Axiom",
    "name": "adjunction",
    "statement": "The two total functions obey the adjunction equivalence on the specified partial orders.",
    "formalStatement": "α:C→A; γ:A→C; α(c)≤A a iff c≤C γ(a)",
    "appliesTo": [
      "urn:csabs:concept/GaloisConnection"
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
    "id": "urn:csabs:law/GaloisConnection-core",
    "type": "Law",
    "statement": "The composite γ∘α is an extensive, monotone, idempotent closure operator.",
    "formalStatement": "c≤γα(c); γαγα(c)=γα(c)",
    "appliesTo": [
      "urn:csabs:concept/GaloisConnection"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "assumptions": [
      "Use the carrier and semantic convention in the linked concept definition."
    ],
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/GaloisConnection-adjunction"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/GaloisConnection-unit-counit",
    "type": "Theorem",
    "name": "unit-counit",
    "statement": "An adjoint pair satisfies its unit and counit inequalities.",
    "formalStatement": "c≤γα(c); αγ(a)≤a",
    "proofSketch": "Apply the adjunction to the reflexive inequalities α(c)≤α(c) and γ(a)≤γ(a).",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for GaloisConnection apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/GaloisConnection"
    ],
    "dependsOn": [
      "urn:csabs:axiom/GaloisConnection-adjunction"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
