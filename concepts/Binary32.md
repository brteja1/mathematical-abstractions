# IEEE 754 binary32

A 32-bit IEEE binary interchange format with 24 binary significand digits for normal numbers, signed zeros, subnormals, infinities, and NaNs. Rounding mode and arithmetic environment must be supplied separately.

**Notation:** β=2; p=24; e_min=-126; e_max=127; normal x=(−1)^s(1+k·2^(1−p))·2^e, 0≤k<2^(p−1), e_min≤e≤e_max.

**Stable ID:** `urn:csabs:concept/Binary32`

**Categories:** Numeric computation

**Kind:** Numeric data type

**Prerequisites:** [Floating-point type](FloatingPointType.md)

**Specializes:** [Floating-point type](FloatingPointType.md)

## Mathematical formulation

The partial format instance has (width,radix,precision,e\_min,e\_max)=(32,2,24,−126,127), with subnormals enabled. Finite nonzero magnitudes are m·2^{e−23}, 0<m<2^{24}, −126≤e≤127, and m≥2^{23} unless e=−126. This instantiates the unconstrained FloatingPointType interface, without an arithmetic-correctness claim.

**Lean formulation** (in its source module context):

```lean
abbrev Binary32 := FloatingPointType binary32Format
```

**Source:** [`Catalog.Binary32`](../lean/Catalog/Numeric.lean); consulted 2026-11-12.

**Scope:** partial

**Interpretation:** FloatingPointType instance: 32 bits, radix 2, precision 24, exponents [-126,127], gradual underflow enabled.

**Limits:** No correctly-rounded arithmetic or exception/NaN payload specification has been proved; run and round are unconstrained client parameters. Not a complete IEEE model.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** IEEE binary interchange instance: bits=32, radix=2, precision=24, normal exponent range [-126,127], gradual underflow, signed zeros, infinities and NaNs. Rounding and flags are explicit environment parameters.

**basisKind:** parameter-instance

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**basisInstantiation:** Instantiate FloatingPointType at this node’s radix, precision and exponent parameters; use its numeric-result rounding and special-value rules with an explicitly chosen IEEE rounding mode and exception environment.

**specializationNote:** Instantiate FloatingPointType at this entry’s radix, precision and exponent range as specified by basisInstantiation; rounding and exception environment remain explicit parameters.

**verificationObligation:** Instantiate operations from FloatingPointType at this format; specify rounding, subnormal handling, and exceptions.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-Binary32-add"></a>

### add

`urn:csabs:operation/Binary32-add`

**signature:** add : Binary32×Binary32→Binary32 (numeric-result projection)

**description:** Instantiates IEEE + at Binary32 with an explicit rounding/exception environment; flags or traps are additional operational outcomes.

<a id="node-urn-csabs-operation-Binary32-subtract"></a>

### subtract

`urn:csabs:operation/Binary32-subtract`

**signature:** subtract : Binary32×Binary32→Binary32 (numeric-result projection)

**description:** Instantiates IEEE − at Binary32 with an explicit rounding/exception environment; flags or traps are additional operational outcomes.

<a id="node-urn-csabs-operation-Binary32-multiply"></a>

### multiply

`urn:csabs:operation/Binary32-multiply`

**signature:** multiply : Binary32×Binary32→Binary32 (numeric-result projection)

**description:** Instantiates IEEE × at Binary32 with an explicit rounding/exception environment; flags or traps are additional operational outcomes.

<a id="node-urn-csabs-operation-Binary32-divide"></a>

### divide

`urn:csabs:operation/Binary32-divide`

**signature:** divide : Binary32×Binary32→Binary32 (numeric-result projection)

**description:** Instantiates IEEE ÷ at Binary32 with an explicit rounding/exception environment; flags or traps are additional operational outcomes.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-Binary32-normal-grid"></a>

### normal-grid

`urn:csabs:axiom/Binary32-normal-grid`

**statement:** Normal finite values have the stated sign, significand and exponent grid.

**formalStatement:** x=(−1)^s(1+k·2^(1−24))·2^e; s∈{0,1}; 0≤k<2^(24−1); -126≤e≤127

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [David Goldberg: What Every Computer Scientist Should Know About Floating-Point Arithmetic (Oracle edited reprint)](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html); citation: David Goldberg, ACM Computing Surveys 23(1), March 1991, pp. 5–48; edited reprint in Oracle Numerical Computation Guide, Appendix D, including later addendum.; accessedOn: 2026-11-08; sourceRole: consulted-expository-reference; historical IEEE discussion, not a replacement for IEEE 754-2019

**sourceLocator:** Floating-point Formats; Base; Table D-1

**sourceNote:** Instantiates the normal binary grid using the consulted single/double precision parameters.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-Binary32-subnormal-grid"></a>

### subnormal-grid

`urn:csabs:axiom/Binary32-subnormal-grid`

**statement:** Subnormals use the minimum exponent and no implicit leading one.

**formalStatement:** x=(−1)^s·k·2^(-126−24+1); 1≤k<2^(24−1)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [David Goldberg: What Every Computer Scientist Should Know About Floating-Point Arithmetic (Oracle edited reprint)](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html); citation: David Goldberg, ACM Computing Surveys 23(1), March 1991, pp. 5–48; edited reprint in Oracle Numerical Computation Guide, Appendix D, including later addendum.; accessedOn: 2026-11-08; sourceRole: consulted-expository-reference; historical IEEE discussion, not a replacement for IEEE 754-2019

**sourceLocator:** Denormalized Numbers; Table D-1

**sourceNote:** Instantiates the subnormal binary grid at the existing single/double parameters.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-Binary32-special-values"></a>

### special-values

`urn:csabs:axiom/Binary32-special-values`

**statement:** Zero, infinities and NaNs are distinct encodings with IEEE numeric comparisons.

**formalStatement:** +0=−0 numerically, but sign bits differ; ±∞ ordered beyond finite values; NaN is unordered and NaN=NaN is false under IEEE numeric equality

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Binary32-rounded-operations"></a>

### rounded-operations

`urn:csabs:axiom/Binary32-rounded-operations`

**statement:** Basic operations instantiate the general IEEE environment at this format.

**formalStatement:** For op∈{+,−,×,÷,sqrt}, op_F uses this instance grid, the selected rounding mode, and IEEE special-value/flag rules

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

<a id="node-urn-csabs-law-Binary32-finite-grid"></a>

### law/Binary32-finite-grid

`urn:csabs:law/Binary32-finite-grid`

**statement:** The smallest positive subnormal is 2^(e_min−p+1), while the largest finite value is (2−2^(1−p))·2^e_max.

**formalStatement:** minSubnormal=2^(-149); maxFinite=(2−2^(-23))·2^127

**assumptions:** IEEE format with gradual underflow; subnormals not flushed to zero

**source:** [IEEE 754-2019](https://standards.ieee.org/ieee/754/6210/); sourceRole: normative-standard

**reviewStatus:** editorial-summary; not machine-proved

**dependsOn:** [normal-grid](Binary32.md#node-urn-csabs-axiom-Binary32-normal-grid); [subnormal-grid](Binary32.md#node-urn-csabs-axiom-Binary32-subnormal-grid); [special-values](Binary32.md#node-urn-csabs-axiom-Binary32-special-values); [rounded-operations](Binary32.md#node-urn-csabs-axiom-Binary32-rounded-operations)

## Theorems

<a id="node-urn-csabs-theorem-Binary32-exact-integers"></a>

### exact-small-integers

`urn:csabs:theorem/Binary32-exact-integers`

**statement:** Every integer with absolute value at most 2^p is exactly representable in this binary format.

**formalStatement:** z∈ℤ ∧ abs(z)≤2^24 ⇒ z exactly representable

**proofSketch:** An integer with at most p significant binary digits fits the significand; the endpoint 2^p has a single nonzero significand bit and a valid exponent.

**assumptions:** IEEE Binary32 format; its exponent range includes all required exponents up to p=24.

**dependsOn:** [normal-grid](Binary32.md#node-urn-csabs-axiom-Binary32-normal-grid); [subnormal-grid](Binary32.md#node-urn-csabs-axiom-Binary32-subnormal-grid); [special-values](Binary32.md#node-urn-csabs-axiom-Binary32-special-values); [rounded-operations](Binary32.md#node-urn-csabs-axiom-Binary32-rounded-operations)

**reviewStatus:** editorial-summary; not machine-proved

**provenanceStatus:** legacy-source-missing

## Concept provenance

- [IEEE 754-2019](https://standards.ieee.org/ieee/754/6210/); sourceRole: normative-standard
- [David Goldberg: What Every Computer Scientist Should Know About Floating-Point Arithmetic (Oracle edited reprint)](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html); citation: David Goldberg, ACM Computing Surveys 23(1), March 1991, pp. 5–48; edited reprint in Oracle Numerical Computation Guide, Appendix D, including later addendum.; accessedOn: 2026-11-08; sourceRole: consulted-expository-reference; historical IEEE discussion, not a replacement for IEEE 754-2019

**sourceLocator:** The IEEE Standard; Formats and Operations / Precision, Table D-1

**sourceNote:** Single/double parameters match this existing binary32/binary64 entry; retain the current normative standard reference.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/Binary32",
    "type": "Concept",
    "shortForm": "Binary32",
    "fullName": "IEEE 754 binary32",
    "category": [
      "urn:csabs:category/numeric-computation"
    ],
    "kind": "urn:csabs:kind/data-type",
    "definition": "A 32-bit IEEE binary interchange format with 24 binary significand digits for normal numbers, signed zeros, subnormals, infinities, and NaNs. Rounding mode and arithmetic environment must be supplied separately.",
    "notation": "β=2; p=24; e_min=-126; e_max=127; normal x=(−1)^s(1+k·2^(1−p))·2^e, 0≤k<2^(p−1), e_min≤e≤e_max.",
    "formatBits": 32,
    "radix": 2,
    "precision": 24,
    "minNormalExponent": -126,
    "maxNormalExponent": 127,
    "hasOperation": [
      "urn:csabs:operation/Binary32-add",
      "urn:csabs:operation/Binary32-subtract",
      "urn:csabs:operation/Binary32-multiply",
      "urn:csabs:operation/Binary32-divide"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/Binary32-normal-grid",
      "urn:csabs:axiom/Binary32-subnormal-grid",
      "urn:csabs:axiom/Binary32-special-values",
      "urn:csabs:axiom/Binary32-rounded-operations"
    ],
    "hasLaw": [
      "urn:csabs:law/Binary32-finite-grid"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/Binary32-exact-integers"
    ],
    "requiresConcept": [
      "urn:csabs:concept/FloatingPointType"
    ],
    "source": [
      "urn:csabs:source/ieee754",
      "urn:csabs:source/goldberg-floating-point-oracle"
    ],
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Instantiate operations from FloatingPointType at this format; specify rounding, subnormal handling, and exceptions.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "IEEE binary interchange instance: bits=32, radix=2, precision=24, normal exponent range [-126,127], gradual underflow, signed zeros, infinities and NaNs. Rounding and flags are explicit environment parameters.",
    "basisKind": "parameter-instance",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "basisInstantiation": "Instantiate FloatingPointType at this node’s radix, precision and exponent parameters; use its numeric-result rounding and special-value rules with an explicitly chosen IEEE rounding mode and exception environment.",
    "specializationOf": [
      "urn:csabs:concept/FloatingPointType"
    ],
    "specializationNote": "Instantiate FloatingPointType at this entry’s radix, precision and exponent range as specified by basisInstantiation; rounding and exception environment remain explicit parameters.",
    "sourceLocator": "The IEEE Standard; Formats and Operations / Precision, Table D-1",
    "sourceNote": "Single/double parameters match this existing binary32/binary64 entry; retain the current normative standard reference.",
    "provenanceKind": "adapted",
    "leanFormulation": "abbrev Binary32 := FloatingPointType binary32Format",
    "formulationSource": "urn:csabs:source/local-lean-Numeric",
    "formulationLocator": "Catalog.Binary32",
    "formulationScope": "partial",
    "leanModelMapping": "FloatingPointType instance: 32 bits, radix 2, precision 24, exponents [-126,127], gradual underflow enabled.",
    "leanModelLimitations": "No correctly-rounded arithmetic or exception/NaN payload specification has been proved; run and round are unconstrained client parameters. Not a complete IEEE model.",
    "mathematicalFormulation": "The partial format instance has (width,radix,precision,e_min,e_max)=(32,2,24,−126,127), with subnormals enabled. Finite nonzero magnitudes are m·2^{e−23}, 0<m<2^{24}, −126≤e≤127, and m≥2^{23} unless e=−126. This instantiates the unconstrained FloatingPointType interface, without an arithmetic-correctness claim."
  },
  {
    "id": "urn:csabs:operation/Binary32-add",
    "type": "Operation",
    "name": "add",
    "signature": "add : Binary32×Binary32→Binary32 (numeric-result projection)",
    "description": "Instantiates IEEE + at Binary32 with an explicit rounding/exception environment; flags or traps are additional operational outcomes.",
    "concept": "urn:csabs:concept/Binary32"
  },
  {
    "id": "urn:csabs:operation/Binary32-subtract",
    "type": "Operation",
    "name": "subtract",
    "signature": "subtract : Binary32×Binary32→Binary32 (numeric-result projection)",
    "description": "Instantiates IEEE − at Binary32 with an explicit rounding/exception environment; flags or traps are additional operational outcomes.",
    "concept": "urn:csabs:concept/Binary32"
  },
  {
    "id": "urn:csabs:operation/Binary32-multiply",
    "type": "Operation",
    "name": "multiply",
    "signature": "multiply : Binary32×Binary32→Binary32 (numeric-result projection)",
    "description": "Instantiates IEEE × at Binary32 with an explicit rounding/exception environment; flags or traps are additional operational outcomes.",
    "concept": "urn:csabs:concept/Binary32"
  },
  {
    "id": "urn:csabs:operation/Binary32-divide",
    "type": "Operation",
    "name": "divide",
    "signature": "divide : Binary32×Binary32→Binary32 (numeric-result projection)",
    "description": "Instantiates IEEE ÷ at Binary32 with an explicit rounding/exception environment; flags or traps are additional operational outcomes.",
    "concept": "urn:csabs:concept/Binary32"
  },
  {
    "id": "urn:csabs:axiom/Binary32-normal-grid",
    "type": "Axiom",
    "name": "normal-grid",
    "statement": "Normal finite values have the stated sign, significand and exponent grid.",
    "formalStatement": "x=(−1)^s(1+k·2^(1−24))·2^e; s∈{0,1}; 0≤k<2^(24−1); -126≤e≤127",
    "appliesTo": [
      "urn:csabs:concept/Binary32"
    ],
    "assumptions": [
      "All variables range over the carriers and semantic conventions specified in this concept."
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/goldberg-floating-point-oracle"
    ],
    "sourceLocator": "Floating-point Formats; Base; Table D-1",
    "sourceNote": "Instantiates the normal binary grid using the consulted single/double precision parameters.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/Binary32-subnormal-grid",
    "type": "Axiom",
    "name": "subnormal-grid",
    "statement": "Subnormals use the minimum exponent and no implicit leading one.",
    "formalStatement": "x=(−1)^s·k·2^(-126−24+1); 1≤k<2^(24−1)",
    "appliesTo": [
      "urn:csabs:concept/Binary32"
    ],
    "assumptions": [
      "All variables range over the carriers and semantic conventions specified in this concept."
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/goldberg-floating-point-oracle"
    ],
    "sourceLocator": "Denormalized Numbers; Table D-1",
    "sourceNote": "Instantiates the subnormal binary grid at the existing single/double parameters.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/Binary32-special-values",
    "type": "Axiom",
    "name": "special-values",
    "statement": "Zero, infinities and NaNs are distinct encodings with IEEE numeric comparisons.",
    "formalStatement": "+0=−0 numerically, but sign bits differ; ±∞ ordered beyond finite values; NaN is unordered and NaN=NaN is false under IEEE numeric equality",
    "appliesTo": [
      "urn:csabs:concept/Binary32"
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
    "id": "urn:csabs:axiom/Binary32-rounded-operations",
    "type": "Axiom",
    "name": "rounded-operations",
    "statement": "Basic operations instantiate the general IEEE environment at this format.",
    "formalStatement": "For op∈{+,−,×,÷,sqrt}, op_F uses this instance grid, the selected rounding mode, and IEEE special-value/flag rules",
    "appliesTo": [
      "urn:csabs:concept/Binary32"
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
    "id": "urn:csabs:law/Binary32-finite-grid",
    "type": "Law",
    "statement": "The smallest positive subnormal is 2^(e_min−p+1), while the largest finite value is (2−2^(1−p))·2^e_max.",
    "formalStatement": "minSubnormal=2^(-149); maxFinite=(2−2^(-23))·2^127",
    "assumptions": [
      "IEEE format with gradual underflow; subnormals not flushed to zero"
    ],
    "appliesTo": [
      "urn:csabs:concept/Binary32"
    ],
    "source": [
      "urn:csabs:source/ieee754"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "dependsOn": [
      "urn:csabs:axiom/Binary32-normal-grid",
      "urn:csabs:axiom/Binary32-subnormal-grid",
      "urn:csabs:axiom/Binary32-special-values",
      "urn:csabs:axiom/Binary32-rounded-operations"
    ]
  },
  {
    "id": "urn:csabs:theorem/Binary32-exact-integers",
    "type": "Theorem",
    "name": "exact-small-integers",
    "statement": "Every integer with absolute value at most 2^p is exactly representable in this binary format.",
    "formalStatement": "z∈ℤ ∧ abs(z)≤2^24 ⇒ z exactly representable",
    "proofSketch": "An integer with at most p significant binary digits fits the significand; the endpoint 2^p has a single nonzero significand bit and a valid exponent.",
    "assumptions": [
      "IEEE Binary32 format; its exponent range includes all required exponents up to p=24."
    ],
    "appliesTo": [
      "urn:csabs:concept/Binary32"
    ],
    "dependsOn": [
      "urn:csabs:axiom/Binary32-normal-grid",
      "urn:csabs:axiom/Binary32-subnormal-grid",
      "urn:csabs:axiom/Binary32-special-values",
      "urn:csabs:axiom/Binary32-rounded-operations"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
