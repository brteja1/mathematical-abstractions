# Arbitrary Precision Integer

An integer value with no fixed mathematical width; implementations may exhaust resources even though the value semantics is unbounded.

**Notation:** value ∈ ℤ; arithmetic exact when it returns normally

**Stable ID:** `urn:csabs:concept/ArbitraryPrecisionInteger`

**Categories:** Numeric computation

**Kind:** Numeric data type

**Prerequisites:** [Mathematical integers](Integer.md)

## Backlinks

- [Exact rational number](RationalNumber.md) — `requiresConcept`

## Interface and scope

**axiomBasis:** Selected presentation: An integer value with no fixed mathematical width; implementations may exhaust resources even though the value semantics is unbounded. Governing rules: The abstract value carrier is unbounded integers, independently of resource limits.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**verificationObligation:** Instantiate carrier, equality, and stated semantic conventions before using this entry.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

**provenanceStatus:** legacy-source-missing

## Operations

<a id="node-urn-csabs-operation-ArbitraryPrecisionInteger-add"></a>

### add

`urn:csabs:operation/ArbitraryPrecisionInteger-add`

**signature:** add : ℤ×ℤ→ℤ (value semantics)

**description:** Returns the exact sum on normal return; resource failures are separate operational outcomes.

<a id="node-urn-csabs-operation-ArbitraryPrecisionInteger-basis-subtract"></a>

### subtract

`urn:csabs:operation/ArbitraryPrecisionInteger-basis-subtract`

**signature:** sub : ℤ×ℤ→ℤ, on normal return

**description:** Exact subtraction on numeric values; resource failures belong to the operational model.

<a id="node-urn-csabs-operation-ArbitraryPrecisionInteger-basis-multiply"></a>

### multiply

`urn:csabs:operation/ArbitraryPrecisionInteger-basis-multiply`

**signature:** mul : ℤ×ℤ→ℤ, on normal return

**description:** Exact multiplication on numeric values; resource failures belong to the operational model.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-ArbitraryPrecisionInteger-value-semantics"></a>

### value-semantics

`urn:csabs:axiom/ArbitraryPrecisionInteger-value-semantics`

**statement:** The abstract value carrier is unbounded integers, independently of resource limits.

**formalStatement:** Values=ℤ; normalReturn(op(x,y)) ⇒ value(result)=op_ℤ(value(x),value(y)), op∈{+,−,×}

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

<a id="node-urn-csabs-law-ArbitraryPrecisionInteger-core"></a>

### law/ArbitraryPrecisionInteger-core

`urn:csabs:law/ArbitraryPrecisionInteger-core`

**statement:** Successful operations agree with mathematical integer operations.

**formalStatement:** value(add(x,y))=value(x)+value(y), on normal return

**reviewStatus:** editorial-summary; not machine-proved

**assumptions:** Use the carrier and semantic convention in the linked concept definition.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [value-semantics](ArbitraryPrecisionInteger.md#node-urn-csabs-axiom-ArbitraryPrecisionInteger-value-semantics)

**provenanceStatus:** legacy-source-missing

## Theorems

<a id="node-urn-csabs-theorem-ArbitraryPrecisionInteger-normal-return-cancellation"></a>

### normal-return-cancellation

`urn:csabs:theorem/ArbitraryPrecisionInteger-normal-return-cancellation`

**statement:** Successful addition by a fixed integer preserves injectivity of numeric values.

**formalStatement:** normal(add(a,b))=r ∧ normal(add(a,c))=s ∧ value(r)=value(s) ⇒ value(b)=value(c)

**proofSketch:** Exact normal-return semantics reduces the premise to integer addition cancellation.

**assumptions:** The explicit basis, carriers, and side conditions stated for ArbitraryPrecisionInteger apply.

**dependsOn:** [value-semantics](ArbitraryPrecisionInteger.md#node-urn-csabs-axiom-ArbitraryPrecisionInteger-value-semantics)

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
    "id": "urn:csabs:concept/ArbitraryPrecisionInteger",
    "type": "Concept",
    "shortForm": "ArbitraryPrecisionInteger",
    "fullName": "Arbitrary Precision Integer",
    "category": [
      "urn:csabs:category/numeric-computation"
    ],
    "kind": "urn:csabs:kind/data-type",
    "definition": "An integer value with no fixed mathematical width; implementations may exhaust resources even though the value semantics is unbounded.",
    "notation": "value ∈ ℤ; arithmetic exact when it returns normally",
    "hasOperation": [
      "urn:csabs:operation/ArbitraryPrecisionInteger-add",
      "urn:csabs:operation/ArbitraryPrecisionInteger-basis-subtract",
      "urn:csabs:operation/ArbitraryPrecisionInteger-basis-multiply"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/ArbitraryPrecisionInteger-value-semantics"
    ],
    "hasLaw": [
      "urn:csabs:law/ArbitraryPrecisionInteger-core"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/ArbitraryPrecisionInteger-normal-return-cancellation"
    ],
    "requiresConcept": [
      "urn:csabs:concept/MathematicalInteger"
    ],
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Instantiate carrier, equality, and stated semantic conventions before using this entry.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: An integer value with no fixed mathematical width; implementations may exhaust resources even though the value semantics is unbounded. Governing rules: The abstract value carrier is unbounded integers, independently of resource limits.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:operation/ArbitraryPrecisionInteger-add",
    "type": "Operation",
    "name": "add",
    "signature": "add : ℤ×ℤ→ℤ (value semantics)",
    "description": "Returns the exact sum on normal return; resource failures are separate operational outcomes.",
    "concept": "urn:csabs:concept/ArbitraryPrecisionInteger"
  },
  {
    "id": "urn:csabs:operation/ArbitraryPrecisionInteger-basis-subtract",
    "type": "Operation",
    "name": "subtract",
    "signature": "sub : ℤ×ℤ→ℤ, on normal return",
    "description": "Exact subtraction on numeric values; resource failures belong to the operational model.",
    "concept": "urn:csabs:concept/ArbitraryPrecisionInteger"
  },
  {
    "id": "urn:csabs:operation/ArbitraryPrecisionInteger-basis-multiply",
    "type": "Operation",
    "name": "multiply",
    "signature": "mul : ℤ×ℤ→ℤ, on normal return",
    "description": "Exact multiplication on numeric values; resource failures belong to the operational model.",
    "concept": "urn:csabs:concept/ArbitraryPrecisionInteger"
  },
  {
    "id": "urn:csabs:axiom/ArbitraryPrecisionInteger-value-semantics",
    "type": "Axiom",
    "name": "value-semantics",
    "statement": "The abstract value carrier is unbounded integers, independently of resource limits.",
    "formalStatement": "Values=ℤ; normalReturn(op(x,y)) ⇒ value(result)=op_ℤ(value(x),value(y)), op∈{+,−,×}",
    "appliesTo": [
      "urn:csabs:concept/ArbitraryPrecisionInteger"
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
    "id": "urn:csabs:law/ArbitraryPrecisionInteger-core",
    "type": "Law",
    "statement": "Successful operations agree with mathematical integer operations.",
    "formalStatement": "value(add(x,y))=value(x)+value(y), on normal return",
    "appliesTo": [
      "urn:csabs:concept/ArbitraryPrecisionInteger"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "assumptions": [
      "Use the carrier and semantic convention in the linked concept definition."
    ],
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/ArbitraryPrecisionInteger-value-semantics"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/ArbitraryPrecisionInteger-normal-return-cancellation",
    "type": "Theorem",
    "name": "normal-return-cancellation",
    "statement": "Successful addition by a fixed integer preserves injectivity of numeric values.",
    "formalStatement": "normal(add(a,b))=r ∧ normal(add(a,c))=s ∧ value(r)=value(s) ⇒ value(b)=value(c)",
    "proofSketch": "Exact normal-return semantics reduces the premise to integer addition cancellation.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for ArbitraryPrecisionInteger apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/ArbitraryPrecisionInteger"
    ],
    "dependsOn": [
      "urn:csabs:axiom/ArbitraryPrecisionInteger-value-semantics"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
