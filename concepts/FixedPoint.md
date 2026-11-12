# Fixed Point

An input left unchanged by a self-map; existence is an additional property of the map and carrier.

**Notation:** x∈Fix(f) iff f(x)=x

**Stable ID:** `urn:csabs:concept/FixedPoint`

**Categories:** Order and fixed points

**Kind:** principle

**Prerequisites:** [Total function](Function.md)

## Mathematical formulation

For f:A→A, Fix(f)={x∈A | f(x)=x}. The definition does not assert existence or uniqueness of a fixed point.

**Lean formulation** (in its source module context):

```lean
def FixedPoint {A : Type u} (f : A → A) (x : A) : Prop := f x = x
```

**Source:** [`Catalog.FixedPoint`](../lean/Catalog/Order.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Predicate f x = x for a total self-map; no existence claim.

**Limits:** Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Selected presentation: An input left unchanged by a self-map; existence is an additional property of the map and carrier. Governing rules: Being fixed means equality to the image under a total self-map.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**verificationObligation:** Instantiate carrier, equality, and stated semantic conventions before using this entry.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

**provenanceStatus:** legacy-source-missing

## Operations

<a id="node-urn-csabs-operation-FixedPoint-basis-fixed"></a>

### fixed

`urn:csabs:operation/FixedPoint-basis-fixed`

**signature:** fixed : (A→A)×A→Prop

**description:** Returns the proposition f(x)=x.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-FixedPoint-fixed-point-definition"></a>

### fixed-point-definition

`urn:csabs:axiom/FixedPoint-fixed-point-definition`

**statement:** Being fixed means equality to the image under a total self-map.

**formalStatement:** Fix(f)={x∈A:f(x)=x}, f:A→A

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

<a id="node-urn-csabs-law-FixedPoint-core"></a>

### law/FixedPoint-core

`urn:csabs:law/FixedPoint-core`

**statement:** Fixed points need not be unique.

**formalStatement:** id_A has every element of A as a fixed point

**reviewStatus:** editorial-summary; not machine-proved

**assumptions:** Use the carrier and semantic convention in the linked concept definition.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [fixed-point-definition](FixedPoint.md#node-urn-csabs-axiom-FixedPoint-fixed-point-definition)

**provenanceStatus:** legacy-source-missing

## Theorems

<a id="node-urn-csabs-theorem-FixedPoint-no-general-existence"></a>

### no-general-existence

`urn:csabs:theorem/FixedPoint-no-general-existence`

**statement:** An arbitrary self-map need not have a fixed point.

**formalStatement:** A={0,1}; f(0)=1; f(1)=0 ⇒ Fix(f)=∅

**proofSketch:** Exhaust the two inputs; neither equals its image.

**assumptions:** The explicit basis, carriers, and side conditions stated for FixedPoint apply.

**dependsOn:** [fixed-point-definition](FixedPoint.md#node-urn-csabs-axiom-FixedPoint-fixed-point-definition)

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
    "id": "urn:csabs:concept/FixedPoint",
    "type": "Concept",
    "shortForm": "FixedPoint",
    "fullName": "Fixed Point",
    "category": [
      "urn:csabs:category/order"
    ],
    "kind": "urn:csabs:kind/principle",
    "definition": "An input left unchanged by a self-map; existence is an additional property of the map and carrier.",
    "notation": "x∈Fix(f) iff f(x)=x",
    "hasOperation": [
      "urn:csabs:operation/FixedPoint-basis-fixed"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/FixedPoint-fixed-point-definition"
    ],
    "hasLaw": [
      "urn:csabs:law/FixedPoint-core"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/FixedPoint-no-general-existence"
    ],
    "requiresConcept": [
      "urn:csabs:concept/Function"
    ],
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Instantiate carrier, equality, and stated semantic conventions before using this entry.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: An input left unchanged by a self-map; existence is an additional property of the map and carrier. Governing rules: Being fixed means equality to the image under a total self-map.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "provenanceStatus": "legacy-source-missing",
    "leanFormulation": "def FixedPoint {A : Type u} (f : A → A) (x : A) : Prop := f x = x",
    "formulationSource": "urn:csabs:source/local-lean-Order",
    "formulationLocator": "Catalog.FixedPoint",
    "formulationScope": "model",
    "leanModelMapping": "Predicate f x = x for a total self-map; no existence claim.",
    "leanModelLimitations": "Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.",
    "mathematicalFormulation": "For f:A→A, Fix(f)={x∈A | f(x)=x}. The definition does not assert existence or uniqueness of a fixed point."
  },
  {
    "id": "urn:csabs:operation/FixedPoint-basis-fixed",
    "type": "Operation",
    "name": "fixed",
    "signature": "fixed : (A→A)×A→Prop",
    "description": "Returns the proposition f(x)=x.",
    "concept": "urn:csabs:concept/FixedPoint"
  },
  {
    "id": "urn:csabs:axiom/FixedPoint-fixed-point-definition",
    "type": "Axiom",
    "name": "fixed-point-definition",
    "statement": "Being fixed means equality to the image under a total self-map.",
    "formalStatement": "Fix(f)={x∈A:f(x)=x}, f:A→A",
    "appliesTo": [
      "urn:csabs:concept/FixedPoint"
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
    "id": "urn:csabs:law/FixedPoint-core",
    "type": "Law",
    "statement": "Fixed points need not be unique.",
    "formalStatement": "id_A has every element of A as a fixed point",
    "appliesTo": [
      "urn:csabs:concept/FixedPoint"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "assumptions": [
      "Use the carrier and semantic convention in the linked concept definition."
    ],
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/FixedPoint-fixed-point-definition"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/FixedPoint-no-general-existence",
    "type": "Theorem",
    "name": "no-general-existence",
    "statement": "An arbitrary self-map need not have a fixed point.",
    "formalStatement": "A={0,1}; f(0)=1; f(1)=0 ⇒ Fix(f)=∅",
    "proofSketch": "Exhaust the two inputs; neither equals its image.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for FixedPoint apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/FixedPoint"
    ],
    "dependsOn": [
      "urn:csabs:axiom/FixedPoint-fixed-point-definition"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
