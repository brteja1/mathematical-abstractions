# Saturating Integer

A bounded integer whose arithmetic clamps exact results to the nearest bound when they leave the interval.

**Notation:** sat(z)=min(U,max(L,z)); x⊕y=sat(x+y)

**Stable ID:** `urn:csabs:concept/SaturatingInteger`

**Categories:** Numeric computation

**Kind:** Numeric data type

**Prerequisites:** [Mathematical integers](Integer.md)

## Interface and scope

**axiomBasis:** Selected presentation: A bounded integer whose arithmetic clamps exact results to the nearest bound when they leave the interval. Governing rules: Clamping projects integers onto a finite nonempty interval. Saturating arithmetic computes exactly and then clamps.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**verificationObligation:** Instantiate carrier, equality, and stated semantic conventions before using this entry.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

**provenanceStatus:** legacy-source-missing

## Operations

<a id="node-urn-csabs-operation-SaturatingInteger-add"></a>

### add

`urn:csabs:operation/SaturatingInteger-add`

**signature:** add : I×I→I

**description:** Clamps the exact sum to the selected interval.

<a id="node-urn-csabs-operation-SaturatingInteger-basis-subtract"></a>

### subtract

`urn:csabs:operation/SaturatingInteger-basis-subtract`

**signature:** sub : I×I→I

**description:** Clamps exact integer subtraction to [L,U].

<a id="node-urn-csabs-operation-SaturatingInteger-basis-multiply"></a>

### multiply

`urn:csabs:operation/SaturatingInteger-basis-multiply`

**signature:** mul : I×I→I

**description:** Clamps exact integer multiplication to [L,U].

## Axioms and defining rules

<a id="node-urn-csabs-axiom-SaturatingInteger-clamp"></a>

### clamp

`urn:csabs:axiom/SaturatingInteger-clamp`

**statement:** Clamping projects integers onto a finite nonempty interval.

**formalStatement:** L,U∈ℤ; L≤U; sat(z)=min(U,max(L,z))

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-SaturatingInteger-arithmetic"></a>

### arithmetic

`urn:csabs:axiom/SaturatingInteger-arithmetic`

**statement:** Saturating arithmetic computes exactly and then clamps.

**formalStatement:** x⊕y=sat(x+y); x⊖y=sat(x−y); x⊗y=sat(x·y)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

<a id="node-urn-csabs-law-SaturatingInteger-core"></a>

### law/SaturatingInteger-core

`urn:csabs:law/SaturatingInteger-core`

**statement:** Saturation is idempotent.

**formalStatement:** sat(sat(z))=sat(z)

**reviewStatus:** editorial-summary; not machine-proved

**assumptions:** Use the carrier and semantic convention in the linked concept definition.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [clamp](SaturatingInteger.md#node-urn-csabs-axiom-SaturatingInteger-clamp); [arithmetic](SaturatingInteger.md#node-urn-csabs-axiom-SaturatingInteger-arithmetic)

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-law-signed-saturation-nonassociative"></a>

### law/signed-saturation-nonassociative

`urn:csabs:law/signed-saturation-nonassociative`

**statement:** Saturating addition over signed bounded intervals need not be associative.

**formalStatement:** I=[−10,10]; (10⊕10)⊕(−10)=0; 10⊕(10⊕(−10))=10

**assumptions:** sat(z)=min(10,max(−10,z))

**reviewStatus:** editorial-summary; not machine-proved

**dependsOn:** [clamp](SaturatingInteger.md#node-urn-csabs-axiom-SaturatingInteger-clamp); [arithmetic](SaturatingInteger.md#node-urn-csabs-axiom-SaturatingInteger-arithmetic)

**provenanceStatus:** legacy-source-missing

## Theorems

<a id="node-urn-csabs-theorem-SaturatingInteger-monotone-clamp"></a>

### monotone-clamp

`urn:csabs:theorem/SaturatingInteger-monotone-clamp`

**statement:** Clamping preserves the ordinary integer order.

**formalStatement:** a≤b ⇒ sat(a)≤sat(b)

**proofSketch:** Minimum and maximum with fixed constants are each monotone.

**assumptions:** The explicit basis, carriers, and side conditions stated for SaturatingInteger apply.

**dependsOn:** [clamp](SaturatingInteger.md#node-urn-csabs-axiom-SaturatingInteger-clamp); [arithmetic](SaturatingInteger.md#node-urn-csabs-axiom-SaturatingInteger-arithmetic)

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
    "id": "urn:csabs:concept/SaturatingInteger",
    "type": "Concept",
    "shortForm": "SaturatingInteger",
    "fullName": "Saturating Integer",
    "category": [
      "urn:csabs:category/numeric-computation"
    ],
    "kind": "urn:csabs:kind/data-type",
    "definition": "A bounded integer whose arithmetic clamps exact results to the nearest bound when they leave the interval.",
    "notation": "sat(z)=min(U,max(L,z)); x⊕y=sat(x+y)",
    "hasOperation": [
      "urn:csabs:operation/SaturatingInteger-add",
      "urn:csabs:operation/SaturatingInteger-basis-subtract",
      "urn:csabs:operation/SaturatingInteger-basis-multiply"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/SaturatingInteger-clamp",
      "urn:csabs:axiom/SaturatingInteger-arithmetic"
    ],
    "hasLaw": [
      "urn:csabs:law/SaturatingInteger-core",
      "urn:csabs:law/signed-saturation-nonassociative"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/SaturatingInteger-monotone-clamp"
    ],
    "requiresConcept": [
      "urn:csabs:concept/MathematicalInteger"
    ],
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Instantiate carrier, equality, and stated semantic conventions before using this entry.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: A bounded integer whose arithmetic clamps exact results to the nearest bound when they leave the interval. Governing rules: Clamping projects integers onto a finite nonempty interval. Saturating arithmetic computes exactly and then clamps.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:operation/SaturatingInteger-add",
    "type": "Operation",
    "name": "add",
    "signature": "add : I×I→I",
    "description": "Clamps the exact sum to the selected interval.",
    "concept": "urn:csabs:concept/SaturatingInteger"
  },
  {
    "id": "urn:csabs:operation/SaturatingInteger-basis-subtract",
    "type": "Operation",
    "name": "subtract",
    "signature": "sub : I×I→I",
    "description": "Clamps exact integer subtraction to [L,U].",
    "concept": "urn:csabs:concept/SaturatingInteger"
  },
  {
    "id": "urn:csabs:operation/SaturatingInteger-basis-multiply",
    "type": "Operation",
    "name": "multiply",
    "signature": "mul : I×I→I",
    "description": "Clamps exact integer multiplication to [L,U].",
    "concept": "urn:csabs:concept/SaturatingInteger"
  },
  {
    "id": "urn:csabs:axiom/SaturatingInteger-clamp",
    "type": "Axiom",
    "name": "clamp",
    "statement": "Clamping projects integers onto a finite nonempty interval.",
    "formalStatement": "L,U∈ℤ; L≤U; sat(z)=min(U,max(L,z))",
    "appliesTo": [
      "urn:csabs:concept/SaturatingInteger"
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
    "id": "urn:csabs:axiom/SaturatingInteger-arithmetic",
    "type": "Axiom",
    "name": "arithmetic",
    "statement": "Saturating arithmetic computes exactly and then clamps.",
    "formalStatement": "x⊕y=sat(x+y); x⊖y=sat(x−y); x⊗y=sat(x·y)",
    "appliesTo": [
      "urn:csabs:concept/SaturatingInteger"
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
    "id": "urn:csabs:law/SaturatingInteger-core",
    "type": "Law",
    "statement": "Saturation is idempotent.",
    "formalStatement": "sat(sat(z))=sat(z)",
    "appliesTo": [
      "urn:csabs:concept/SaturatingInteger"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "assumptions": [
      "Use the carrier and semantic convention in the linked concept definition."
    ],
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/SaturatingInteger-clamp",
      "urn:csabs:axiom/SaturatingInteger-arithmetic"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:law/signed-saturation-nonassociative",
    "type": "Law",
    "statement": "Saturating addition over signed bounded intervals need not be associative.",
    "formalStatement": "I=[−10,10]; (10⊕10)⊕(−10)=0; 10⊕(10⊕(−10))=10",
    "assumptions": [
      "sat(z)=min(10,max(−10,z))"
    ],
    "appliesTo": [
      "urn:csabs:concept/SaturatingInteger"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "dependsOn": [
      "urn:csabs:axiom/SaturatingInteger-clamp",
      "urn:csabs:axiom/SaturatingInteger-arithmetic"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/SaturatingInteger-monotone-clamp",
    "type": "Theorem",
    "name": "monotone-clamp",
    "statement": "Clamping preserves the ordinary integer order.",
    "formalStatement": "a≤b ⇒ sat(a)≤sat(b)",
    "proofSketch": "Minimum and maximum with fixed constants are each monotone.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for SaturatingInteger apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/SaturatingInteger"
    ],
    "dependsOn": [
      "urn:csabs:axiom/SaturatingInteger-clamp",
      "urn:csabs:axiom/SaturatingInteger-arithmetic"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
