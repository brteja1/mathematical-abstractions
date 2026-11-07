# Checked Integer

An integer in a specified finite interval whose arithmetic explicitly returns an overflow outcome if the exact result is outside it.

**Notation:** I=[L,U]∩ℤ; add:I×I→I+{Overflow}

**Stable ID:** `urn:csabs:concept/CheckedInteger`

**Categories:** Numeric computation

**Kind:** Numeric data type

**Prerequisites:** [Mathematical integers](Integer.md), [Sum Type](SumType.md)

## Interface and scope

**axiomBasis:** Selected presentation: An integer in a specified finite interval whose arithmetic explicitly returns an overflow outcome if the exact result is outside it. Governing rules: The interval is finite and nonempty. A checked operation reports overflow exactly when the exact result does not fit.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**verificationObligation:** Instantiate carrier, equality, and stated semantic conventions before using this entry.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

**provenanceStatus:** legacy-source-missing

## Operations

<a id="node-urn-csabs-operation-CheckedInteger-add"></a>

### add

`urn:csabs:operation/CheckedInteger-add`

**signature:** add : I×I→Value(I)+{Overflow}

**description:** Returns exact sum if it fits and Overflow otherwise.

<a id="node-urn-csabs-operation-CheckedInteger-basis-subtract"></a>

### subtract

`urn:csabs:operation/CheckedInteger-basis-subtract`

**signature:** sub : I×I→Value(I)+{Overflow}

**description:** Returns exact subtraction when in range, Overflow otherwise.

<a id="node-urn-csabs-operation-CheckedInteger-basis-multiply"></a>

### multiply

`urn:csabs:operation/CheckedInteger-basis-multiply`

**signature:** mul : I×I→Value(I)+{Overflow}

**description:** Returns exact multiplication when in range, Overflow otherwise.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-CheckedInteger-bounds"></a>

### bounds

`urn:csabs:axiom/CheckedInteger-bounds`

**statement:** The interval is finite and nonempty.

**formalStatement:** L,U∈ℤ; L≤U; I={x∈ℤ:L≤x≤U}

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-CheckedInteger-overflow-contract"></a>

### overflow-contract

`urn:csabs:axiom/CheckedInteger-overflow-contract`

**statement:** A checked operation reports overflow exactly when the exact result does not fit.

**formalStatement:** checked_op(x,y)=Value(op_ℤ(x,y)) if L≤op_ℤ(x,y)≤U, otherwise Overflow, for op∈{+,−,×}

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

<a id="node-urn-csabs-law-CheckedInteger-core"></a>

### law/CheckedInteger-core

`urn:csabs:law/CheckedInteger-core`

**statement:** Successful checked addition agrees with exact integer addition.

**formalStatement:** L≤x+y≤U ⇒ add(x,y)=Value(x+y)

**reviewStatus:** editorial-summary; not machine-proved

**assumptions:** Use the carrier and semantic convention in the linked concept definition.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [bounds](CheckedInteger.md#node-urn-csabs-axiom-CheckedInteger-bounds); [overflow-contract](CheckedInteger.md#node-urn-csabs-axiom-CheckedInteger-overflow-contract)

**provenanceStatus:** legacy-source-missing

## Theorems

<a id="node-urn-csabs-theorem-CheckedInteger-failure-exactness"></a>

### failure-exactness

`urn:csabs:theorem/CheckedInteger-failure-exactness`

**statement:** Checked addition fails exactly when the exact integer sum is outside its interval.

**formalStatement:** add(x,y)=Overflow iff x+y<L ∨ U<x+y

**proofSketch:** Split on the bounds predicate in the defining contract.

**assumptions:** The explicit basis, carriers, and side conditions stated for CheckedInteger apply.

**dependsOn:** [bounds](CheckedInteger.md#node-urn-csabs-axiom-CheckedInteger-bounds); [overflow-contract](CheckedInteger.md#node-urn-csabs-axiom-CheckedInteger-overflow-contract)

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
    "id": "urn:csabs:concept/CheckedInteger",
    "type": "Concept",
    "shortForm": "CheckedInteger",
    "fullName": "Checked Integer",
    "category": [
      "urn:csabs:category/numeric-computation"
    ],
    "kind": "urn:csabs:kind/data-type",
    "definition": "An integer in a specified finite interval whose arithmetic explicitly returns an overflow outcome if the exact result is outside it.",
    "notation": "I=[L,U]∩ℤ; add:I×I→I+{Overflow}",
    "hasOperation": [
      "urn:csabs:operation/CheckedInteger-add",
      "urn:csabs:operation/CheckedInteger-basis-subtract",
      "urn:csabs:operation/CheckedInteger-basis-multiply"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/CheckedInteger-bounds",
      "urn:csabs:axiom/CheckedInteger-overflow-contract"
    ],
    "hasLaw": [
      "urn:csabs:law/CheckedInteger-core"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/CheckedInteger-failure-exactness"
    ],
    "requiresConcept": [
      "urn:csabs:concept/MathematicalInteger",
      "urn:csabs:concept/SumType"
    ],
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Instantiate carrier, equality, and stated semantic conventions before using this entry.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: An integer in a specified finite interval whose arithmetic explicitly returns an overflow outcome if the exact result is outside it. Governing rules: The interval is finite and nonempty. A checked operation reports overflow exactly when the exact result does not fit.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:operation/CheckedInteger-add",
    "type": "Operation",
    "name": "add",
    "signature": "add : I×I→Value(I)+{Overflow}",
    "description": "Returns exact sum if it fits and Overflow otherwise.",
    "concept": "urn:csabs:concept/CheckedInteger"
  },
  {
    "id": "urn:csabs:operation/CheckedInteger-basis-subtract",
    "type": "Operation",
    "name": "subtract",
    "signature": "sub : I×I→Value(I)+{Overflow}",
    "description": "Returns exact subtraction when in range, Overflow otherwise.",
    "concept": "urn:csabs:concept/CheckedInteger"
  },
  {
    "id": "urn:csabs:operation/CheckedInteger-basis-multiply",
    "type": "Operation",
    "name": "multiply",
    "signature": "mul : I×I→Value(I)+{Overflow}",
    "description": "Returns exact multiplication when in range, Overflow otherwise.",
    "concept": "urn:csabs:concept/CheckedInteger"
  },
  {
    "id": "urn:csabs:axiom/CheckedInteger-bounds",
    "type": "Axiom",
    "name": "bounds",
    "statement": "The interval is finite and nonempty.",
    "formalStatement": "L,U∈ℤ; L≤U; I={x∈ℤ:L≤x≤U}",
    "appliesTo": [
      "urn:csabs:concept/CheckedInteger"
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
    "id": "urn:csabs:axiom/CheckedInteger-overflow-contract",
    "type": "Axiom",
    "name": "overflow-contract",
    "statement": "A checked operation reports overflow exactly when the exact result does not fit.",
    "formalStatement": "checked_op(x,y)=Value(op_ℤ(x,y)) if L≤op_ℤ(x,y)≤U, otherwise Overflow, for op∈{+,−,×}",
    "appliesTo": [
      "urn:csabs:concept/CheckedInteger"
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
    "id": "urn:csabs:law/CheckedInteger-core",
    "type": "Law",
    "statement": "Successful checked addition agrees with exact integer addition.",
    "formalStatement": "L≤x+y≤U ⇒ add(x,y)=Value(x+y)",
    "appliesTo": [
      "urn:csabs:concept/CheckedInteger"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "assumptions": [
      "Use the carrier and semantic convention in the linked concept definition."
    ],
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/CheckedInteger-bounds",
      "urn:csabs:axiom/CheckedInteger-overflow-contract"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/CheckedInteger-failure-exactness",
    "type": "Theorem",
    "name": "failure-exactness",
    "statement": "Checked addition fails exactly when the exact integer sum is outside its interval.",
    "formalStatement": "add(x,y)=Overflow iff x+y<L ∨ U<x+y",
    "proofSketch": "Split on the bounds predicate in the defining contract.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for CheckedInteger apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/CheckedInteger"
    ],
    "dependsOn": [
      "urn:csabs:axiom/CheckedInteger-bounds",
      "urn:csabs:axiom/CheckedInteger-overflow-contract"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
