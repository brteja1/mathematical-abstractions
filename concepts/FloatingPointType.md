# Floating-point type

A finite numeric format with rounded operations and format-dependent exceptional values; it approximates real arithmetic and does not obey all real-number algebraic laws.

**Notation:** Format F(β,p,e_min,e_max,subnormals,rounding); fl(x) denotes rounding of exact x into F under the selected mode.

**Stable ID:** `urn:csabs:concept/FloatingPointType`

**Categories:** Numeric computation, Programming-language semantics

**Kind:** Numeric data type

**Related concepts:** [Mathematical integers](Integer.md)

## Backlinks

- [IEEE 754 binary128](Binary128.md) — `requiresConcept`
- [IEEE 754 binary128](Binary128.md) — `specializationOf`
- [IEEE 754 binary16](Binary16.md) — `requiresConcept`
- [IEEE 754 binary16](Binary16.md) — `specializationOf`
- [IEEE 754 binary32](Binary32.md) — `requiresConcept`
- [IEEE 754 binary32](Binary32.md) — `specializationOf`
- [IEEE 754 binary64](Binary64.md) — `requiresConcept`
- [IEEE 754 binary64](Binary64.md) — `specializationOf`

## Interface and scope

**axiomBasis:** Selected presentation: A finite numeric format with rounded operations and format-dependent exceptional values; it approximates real arithmetic and does not obey all real-number algebraic laws. Governing rules: The carrier and operations are determined by a specified radix, precision, exponent range, subnormal policy, rounding mode, and exceptional-value semantics. Numeric computation uses a specified format, rounding mode, operation, and exceptional-value/flag convention. For a finite exact result in the finite representable range, round returns a representable value according to the selected mode. IEEE-style operations classify invalid, divide-by-zero, overflow, underflow, and inexact; flags and result behavior are part of the environment.

**basisKind:** defined-structure

**basisScope:** Numeric-result interface for listed basic IEEE-style operations, with explicit representative rounding and exceptional rules. Complete NaN payload encodings, signaling-NaN bit layouts, trap handlers, and library transcendental functions are outside this interface.

**verificationObligation:** Specify rounding mode, format, exceptional values, and compiler reassociation/fusion behavior.; Define numerical tolerance or bit equality explicitly; parallel reduction trees can change rounded results.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-fp-add"></a>

### floating-point addition

`urn:csabs:operation/fp-add`

**signature:** add_F : F×F→F

**description:** Adds exactly then rounds under the format's active rounding and exception semantics.

<a id="node-urn-csabs-operation-fp-subtract"></a>

### floating-point subtraction

`urn:csabs:operation/fp-subtract`

**signature:** sub_F : F×F→F

**description:** Subtracts under the format's rounding and exceptional-value semantics.

<a id="node-urn-csabs-operation-fp-multiply"></a>

### floating-point multiplication

`urn:csabs:operation/fp-multiply`

**signature:** mul_F : F×F→F

**description:** Multiplies under the format's rounding and exceptional-value semantics.

<a id="node-urn-csabs-operation-fp-divide"></a>

### floating-point division

`urn:csabs:operation/fp-divide`

**signature:** div_F : F×F→F

**description:** Divides under the format's rounding, divide-by-zero, and invalid-operation semantics.

<a id="node-urn-csabs-operation-fp-compare"></a>

### floating-point comparison

`urn:csabs:operation/fp-compare`

**signature:** compare : F×F→Bool

**description:** Uses format comparison semantics; NaN is unordered and signed zeros compare numerically equal.

<a id="node-urn-csabs-operation-fp-convert"></a>

### format conversion

`urn:csabs:operation/fp-convert`

**signature:** convert : F₁→F₂

**description:** Converts between formats with specified rounding and exception behavior.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-fp-format-parameters"></a>

### fp-format-parameters

`urn:csabs:axiom/fp-format-parameters`

**statement:** The carrier and operations are determined by a specified radix, precision, exponent range, subnormal policy, rounding mode, and exceptional-value semantics.

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

**formalStatement:** The carrier and operations are determined by a specified radix, precision, exponent range, subnormal policy, rounding mode, and exceptional-value semantics.

**assumptions:** Use the linked concept’s explicit basis and carrier conventions.

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-FloatingPointType-environment"></a>

### environment

`urn:csabs:axiom/FloatingPointType-environment`

**statement:** Numeric computation uses a specified format, rounding mode, operation, and exceptional-value/flag convention.

**formalStatement:** Env=(β,p,e_min,e_max,subnormalPolicy,roundingMode,exceptionPolicy); β≥2, p≥2, e_min≤e_max

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-FloatingPointType-rounding"></a>

### rounding

`urn:csabs:axiom/FloatingPointType-rounding`

**statement:** For a finite exact result in the finite representable range, round returns a representable value according to the selected mode.

**formalStatement:** RN chooses nearest with declared ties; RD chooses greatest representable ≤z; RU chooses least representable ≥z; RZ chooses toward zero

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-FloatingPointType-exceptions"></a>

### exceptions

`urn:csabs:axiom/FloatingPointType-exceptions`

**statement:** IEEE-style operations classify invalid, divide-by-zero, overflow, underflow, and inexact; flags and result behavior are part of the environment.

**formalStatement:** NaN propagation, signed-zero rules, infinities, and exception flags follow the selected IEEE operation and rounding mode; a numeric result alone need not encode flags

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-FloatingPointType-nan-results"></a>

### nan-results

`urn:csabs:axiom/FloatingPointType-nan-results`

**statement:** Quiet NaN input propagates a NaN numeric result for the basic arithmetic operations; payload selection and signaling behavior are separate environment choices.

**formalStatement:** qNaN op x = NaN; x op qNaN = NaN, op∈{+,−,×,÷}

**assumptions:** IEEE-style operations, default nontrapping result behavior; formats and rounding modes specified by the environment.

**ruleRole:** semantic-operation-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-FloatingPointType-invalid-forms"></a>

### invalid-forms

`urn:csabs:axiom/FloatingPointType-invalid-forms`

**statement:** Invalid basic arithmetic forms return NaN in the default nontrapping environment.

**formalStatement:** ∞−∞, ∞+(−∞), 0×∞, ∞×0, 0/0, ∞/∞ produce NaN and signal invalid

**assumptions:** IEEE-style operations, default nontrapping result behavior; formats and rounding modes specified by the environment.

**ruleRole:** semantic-operation-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-FloatingPointType-infinite-operands"></a>

### infinite-operands

`urn:csabs:axiom/FloatingPointType-infinite-operands`

**statement:** Noninvalid infinity operations follow signs and affine infinity arithmetic.

**formalStatement:** finite x: x+(±∞)=±∞; nonzero finite x: (±∞)×x has sign xor; finite x/(±∞) is signed zero; (±∞)/nonzero finite x is signed infinity

**assumptions:** IEEE-style operations, default nontrapping result behavior; formats and rounding modes specified by the environment.

**ruleRole:** semantic-operation-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-FloatingPointType-divide-zero"></a>

### divide-zero

`urn:csabs:axiom/FloatingPointType-divide-zero`

**statement:** Nonzero finite division by signed zero yields signed infinity under default nontrapping semantics.

**formalStatement:** finite x≠0: x/(±0)=signed∞ with sign(x) xor sign(±0), signaling divideByZero

**assumptions:** IEEE-style operations, default nontrapping result behavior; formats and rounding modes specified by the environment.

**ruleRole:** semantic-operation-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-FloatingPointType-signed-zeros"></a>

### signed-zeros

`urn:csabs:axiom/FloatingPointType-signed-zeros`

**statement:** Zero encodings compare numerically equal while retaining signs relevant to division and products.

**formalStatement:** +0 == −0; sign(product or quotient)=xor of operand signs when defined; exact cancellation gives +0 except roundTowardNegative gives −0, with same-sign zero sums retaining their sign

**assumptions:** IEEE-style operations, default nontrapping result behavior; formats and rounding modes specified by the environment.

**ruleRole:** semantic-operation-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

<a id="node-urn-csabs-law-fp-rounding-model"></a>

### law/fp-rounding-model

`urn:csabs:law/fp-rounding-model`

**statement:** A basic operation returns the rounded exact result as specified by its format and active rounding mode, subject to exceptional cases.

**assumptions:** specific IEEE 754 operation and format; active rounding mode recorded

**source:** [IEEE 754-2019](https://standards.ieee.org/ieee/754/6210/); sourceRole: normative-standard

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [fp-format-parameters](FloatingPointType.md#node-urn-csabs-axiom-fp-format-parameters); [environment](FloatingPointType.md#node-urn-csabs-axiom-FloatingPointType-environment); [rounding](FloatingPointType.md#node-urn-csabs-axiom-FloatingPointType-rounding); [exceptions](FloatingPointType.md#node-urn-csabs-axiom-FloatingPointType-exceptions)

**formalStatement:** finite in-range exact result z of op ⇒ result_numeric=round_F(z); special inputs, overflow, flags, and traps use the explicitly selected IEEE environment

<a id="node-urn-csabs-law-fp-nonassociativity"></a>

### law/fp-nonassociativity

`urn:csabs:law/fp-nonassociativity`

**statement:** Floating-point addition and multiplication are not associative in general.

**formalStatement:** ∃a,b,c∈F: fl(fl(a+b)+c)≠fl(a+fl(b+c))

**assumptions:** a finite format with rounding

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [fp-format-parameters](FloatingPointType.md#node-urn-csabs-axiom-fp-format-parameters); [environment](FloatingPointType.md#node-urn-csabs-axiom-FloatingPointType-environment); [rounding](FloatingPointType.md#node-urn-csabs-axiom-FloatingPointType-rounding); [exceptions](FloatingPointType.md#node-urn-csabs-axiom-FloatingPointType-exceptions)

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-law-fp-nan-unordered"></a>

### law/fp-nan-unordered

`urn:csabs:law/fp-nan-unordered`

**statement:** Under IEEE ordered comparisons, comparisons involving NaN are false, including equality; NaN is unordered.

**assumptions:** IEEE comparison predicates

**source:** [IEEE 754-2019](https://standards.ieee.org/ieee/754/6210/); sourceRole: normative-standard

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [fp-format-parameters](FloatingPointType.md#node-urn-csabs-axiom-fp-format-parameters); [environment](FloatingPointType.md#node-urn-csabs-axiom-FloatingPointType-environment); [rounding](FloatingPointType.md#node-urn-csabs-axiom-FloatingPointType-rounding); [exceptions](FloatingPointType.md#node-urn-csabs-axiom-FloatingPointType-exceptions)

**formalStatement:** isNaN(x)∨isNaN(y) ⇒ ¬(x<y) ∧ ¬(x≤y) ∧ ¬(x=y) ∧ ¬(x≥y) ∧ ¬(x>y), for ordered numeric predicates

<a id="node-urn-csabs-law-fp-addition-counterexample"></a>

### law/fp-addition-counterexample

`urn:csabs:law/fp-addition-counterexample`

**statement:** In binary64, round-to-nearest ties-to-even addition can depend on parenthesization.

**formalStatement:** a=2^54, b=−2^54, c=1; fl(fl(a+b)+c)=1; fl(a+fl(b+c))=0

**assumptions:** IEEE binary64 operations rounded to binary64 after each addition; round-to-nearest ties-to-even; No reassociation or excess precision

**reviewStatus:** editorial-summary; not machine-proved

**proofSketch:** The exact sum b+c is halfway between two binary64 values and rounds to b. The first parenthesization first computes the exactly representable zero.

**dependsOn:** [fp-format-parameters](FloatingPointType.md#node-urn-csabs-axiom-fp-format-parameters); [environment](FloatingPointType.md#node-urn-csabs-axiom-FloatingPointType-environment); [rounding](FloatingPointType.md#node-urn-csabs-axiom-FloatingPointType-rounding); [exceptions](FloatingPointType.md#node-urn-csabs-axiom-FloatingPointType-exceptions)

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-law-fp-relative-error"></a>

### law/fp-relative-error

`urn:csabs:law/fp-relative-error`

**statement:** For rounding to nearest with unbounded-exponent idealization, or an in-range normal result without underflow or overflow, a rounded basic arithmetic result satisfies the relative-error model.

**formalStatement:** fl(z)=z(1+δ), |δ|≤u, u=β^(1−p)/2

**assumptions:** z is the exact arithmetic result; nearest rounding; Normal finite result regime; exceptional values excluded; β is the radix and p the precision

**reviewStatus:** editorial-summary; not machine-proved

**dependsOn:** [fp-format-parameters](FloatingPointType.md#node-urn-csabs-axiom-fp-format-parameters); [environment](FloatingPointType.md#node-urn-csabs-axiom-FloatingPointType-environment); [rounding](FloatingPointType.md#node-urn-csabs-axiom-FloatingPointType-rounding); [exceptions](FloatingPointType.md#node-urn-csabs-axiom-FloatingPointType-exceptions)

**provenanceStatus:** legacy-source-missing

## Theorems

<a id="node-urn-csabs-theorem-FloatingPointType-representable-rounding-fixed"></a>

### representable-rounding-fixed

`urn:csabs:theorem/FloatingPointType-representable-rounding-fixed`

**statement:** Rounding a finite exactly representable numeric value leaves that value unchanged.

**formalStatement:** z∈F finite ⇒ round_F(z)=z numerically

**proofSketch:** There is no approximation error to resolve; z is simultaneously nearest and each directed bound. Signed-zero encoding needs its separate sign rule.

**assumptions:** The explicit basis, carriers, and side conditions stated for FloatingPointType apply.

**dependsOn:** [fp-format-parameters](FloatingPointType.md#node-urn-csabs-axiom-fp-format-parameters); [environment](FloatingPointType.md#node-urn-csabs-axiom-FloatingPointType-environment); [rounding](FloatingPointType.md#node-urn-csabs-axiom-FloatingPointType-rounding); [exceptions](FloatingPointType.md#node-urn-csabs-axiom-FloatingPointType-exceptions)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Concept provenance

- [IEEE 754-2019](https://standards.ieee.org/ieee/754/6210/); sourceRole: normative-standard

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/FloatingPointType",
    "type": "Concept",
    "shortForm": "FloatingPointType",
    "fullName": "Floating-point type",
    "category": [
      "urn:csabs:category/numeric-computation",
      "urn:csabs:category/programming-semantics"
    ],
    "kind": "urn:csabs:kind/data-type",
    "definition": "A finite numeric format with rounded operations and format-dependent exceptional values; it approximates real arithmetic and does not obey all real-number algebraic laws.",
    "notation": "Format F(β,p,e_min,e_max,subnormals,rounding); fl(x) denotes rounding of exact x into F under the selected mode.",
    "source": [
      "urn:csabs:source/ieee754"
    ],
    "hasOperation": [
      "urn:csabs:operation/fp-add",
      "urn:csabs:operation/fp-subtract",
      "urn:csabs:operation/fp-multiply",
      "urn:csabs:operation/fp-divide",
      "urn:csabs:operation/fp-compare",
      "urn:csabs:operation/fp-convert"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/fp-format-parameters",
      "urn:csabs:axiom/FloatingPointType-environment",
      "urn:csabs:axiom/FloatingPointType-rounding",
      "urn:csabs:axiom/FloatingPointType-exceptions",
      "urn:csabs:axiom/FloatingPointType-nan-results",
      "urn:csabs:axiom/FloatingPointType-invalid-forms",
      "urn:csabs:axiom/FloatingPointType-infinite-operands",
      "urn:csabs:axiom/FloatingPointType-divide-zero",
      "urn:csabs:axiom/FloatingPointType-signed-zeros"
    ],
    "hasLaw": [
      "urn:csabs:law/fp-rounding-model",
      "urn:csabs:law/fp-nonassociativity",
      "urn:csabs:law/fp-nan-unordered",
      "urn:csabs:law/fp-addition-counterexample",
      "urn:csabs:law/fp-relative-error"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/FloatingPointType-representable-rounding-fixed"
    ],
    "relatedConcept": [
      "urn:csabs:concept/MathematicalInteger"
    ],
    "coverageStatus": "basis-reviewed",
    "requiresConcept": [],
    "verificationObligation": [
      "Specify rounding mode, format, exceptional values, and compiler reassociation/fusion behavior.",
      "Define numerical tolerance or bit equality explicitly; parallel reduction trees can change rounded results.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: A finite numeric format with rounded operations and format-dependent exceptional values; it approximates real arithmetic and does not obey all real-number algebraic laws. Governing rules: The carrier and operations are determined by a specified radix, precision, exponent range, subnormal policy, rounding mode, and exceptional-value semantics. Numeric computation uses a specified format, rounding mode, operation, and exceptional-value/flag convention. For a finite exact result in the finite representable range, round returns a representable value according to the selected mode. IEEE-style operations classify invalid, divide-by-zero, overflow, underflow, and inexact; flags and result behavior are part of the environment.",
    "basisKind": "defined-structure",
    "basisScope": "Numeric-result interface for listed basic IEEE-style operations, with explicit representative rounding and exceptional rules. Complete NaN payload encodings, signaling-NaN bit layouts, trap handlers, and library transcendental functions are outside this interface.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof"
  },
  {
    "id": "urn:csabs:operation/fp-add",
    "type": "Operation",
    "name": "floating-point addition",
    "signature": "add_F : F×F→F",
    "description": "Adds exactly then rounds under the format's active rounding and exception semantics.",
    "concept": "urn:csabs:concept/FloatingPointType"
  },
  {
    "id": "urn:csabs:operation/fp-subtract",
    "type": "Operation",
    "name": "floating-point subtraction",
    "signature": "sub_F : F×F→F",
    "description": "Subtracts under the format's rounding and exceptional-value semantics.",
    "concept": "urn:csabs:concept/FloatingPointType"
  },
  {
    "id": "urn:csabs:operation/fp-multiply",
    "type": "Operation",
    "name": "floating-point multiplication",
    "signature": "mul_F : F×F→F",
    "description": "Multiplies under the format's rounding and exceptional-value semantics.",
    "concept": "urn:csabs:concept/FloatingPointType"
  },
  {
    "id": "urn:csabs:operation/fp-divide",
    "type": "Operation",
    "name": "floating-point division",
    "signature": "div_F : F×F→F",
    "description": "Divides under the format's rounding, divide-by-zero, and invalid-operation semantics.",
    "concept": "urn:csabs:concept/FloatingPointType"
  },
  {
    "id": "urn:csabs:operation/fp-compare",
    "type": "Operation",
    "name": "floating-point comparison",
    "signature": "compare : F×F→Bool",
    "description": "Uses format comparison semantics; NaN is unordered and signed zeros compare numerically equal.",
    "concept": "urn:csabs:concept/FloatingPointType"
  },
  {
    "id": "urn:csabs:operation/fp-convert",
    "type": "Operation",
    "name": "format conversion",
    "signature": "convert : F₁→F₂",
    "description": "Converts between formats with specified rounding and exception behavior.",
    "concept": "urn:csabs:concept/FloatingPointType"
  },
  {
    "id": "urn:csabs:axiom/fp-format-parameters",
    "type": "Axiom",
    "statement": "The carrier and operations are determined by a specified radix, precision, exponent range, subnormal policy, rounding mode, and exceptional-value semantics.",
    "appliesTo": [
      "urn:csabs:concept/FloatingPointType"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law",
    "name": "fp-format-parameters",
    "formalStatement": "The carrier and operations are determined by a specified radix, precision, exponent range, subnormal policy, rounding mode, and exceptional-value semantics.",
    "assumptions": [
      "Use the linked concept’s explicit basis and carrier conventions."
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/FloatingPointType-environment",
    "type": "Axiom",
    "name": "environment",
    "statement": "Numeric computation uses a specified format, rounding mode, operation, and exceptional-value/flag convention.",
    "formalStatement": "Env=(β,p,e_min,e_max,subnormalPolicy,roundingMode,exceptionPolicy); β≥2, p≥2, e_min≤e_max",
    "appliesTo": [
      "urn:csabs:concept/FloatingPointType"
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
    "id": "urn:csabs:axiom/FloatingPointType-rounding",
    "type": "Axiom",
    "name": "rounding",
    "statement": "For a finite exact result in the finite representable range, round returns a representable value according to the selected mode.",
    "formalStatement": "RN chooses nearest with declared ties; RD chooses greatest representable ≤z; RU chooses least representable ≥z; RZ chooses toward zero",
    "appliesTo": [
      "urn:csabs:concept/FloatingPointType"
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
    "id": "urn:csabs:axiom/FloatingPointType-exceptions",
    "type": "Axiom",
    "name": "exceptions",
    "statement": "IEEE-style operations classify invalid, divide-by-zero, overflow, underflow, and inexact; flags and result behavior are part of the environment.",
    "formalStatement": "NaN propagation, signed-zero rules, infinities, and exception flags follow the selected IEEE operation and rounding mode; a numeric result alone need not encode flags",
    "appliesTo": [
      "urn:csabs:concept/FloatingPointType"
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
    "id": "urn:csabs:axiom/FloatingPointType-nan-results",
    "type": "Axiom",
    "name": "nan-results",
    "statement": "Quiet NaN input propagates a NaN numeric result for the basic arithmetic operations; payload selection and signaling behavior are separate environment choices.",
    "formalStatement": "qNaN op x = NaN; x op qNaN = NaN, op∈{+,−,×,÷}",
    "assumptions": [
      "IEEE-style operations, default nontrapping result behavior; formats and rounding modes specified by the environment."
    ],
    "ruleRole": "semantic-operation-rule",
    "appliesTo": [
      "urn:csabs:concept/FloatingPointType"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/FloatingPointType-invalid-forms",
    "type": "Axiom",
    "name": "invalid-forms",
    "statement": "Invalid basic arithmetic forms return NaN in the default nontrapping environment.",
    "formalStatement": "∞−∞, ∞+(−∞), 0×∞, ∞×0, 0/0, ∞/∞ produce NaN and signal invalid",
    "assumptions": [
      "IEEE-style operations, default nontrapping result behavior; formats and rounding modes specified by the environment."
    ],
    "ruleRole": "semantic-operation-rule",
    "appliesTo": [
      "urn:csabs:concept/FloatingPointType"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/FloatingPointType-infinite-operands",
    "type": "Axiom",
    "name": "infinite-operands",
    "statement": "Noninvalid infinity operations follow signs and affine infinity arithmetic.",
    "formalStatement": "finite x: x+(±∞)=±∞; nonzero finite x: (±∞)×x has sign xor; finite x/(±∞) is signed zero; (±∞)/nonzero finite x is signed infinity",
    "assumptions": [
      "IEEE-style operations, default nontrapping result behavior; formats and rounding modes specified by the environment."
    ],
    "ruleRole": "semantic-operation-rule",
    "appliesTo": [
      "urn:csabs:concept/FloatingPointType"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/FloatingPointType-divide-zero",
    "type": "Axiom",
    "name": "divide-zero",
    "statement": "Nonzero finite division by signed zero yields signed infinity under default nontrapping semantics.",
    "formalStatement": "finite x≠0: x/(±0)=signed∞ with sign(x) xor sign(±0), signaling divideByZero",
    "assumptions": [
      "IEEE-style operations, default nontrapping result behavior; formats and rounding modes specified by the environment."
    ],
    "ruleRole": "semantic-operation-rule",
    "appliesTo": [
      "urn:csabs:concept/FloatingPointType"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/FloatingPointType-signed-zeros",
    "type": "Axiom",
    "name": "signed-zeros",
    "statement": "Zero encodings compare numerically equal while retaining signs relevant to division and products.",
    "formalStatement": "+0 == −0; sign(product or quotient)=xor of operand signs when defined; exact cancellation gives +0 except roundTowardNegative gives −0, with same-sign zero sums retaining their sign",
    "assumptions": [
      "IEEE-style operations, default nontrapping result behavior; formats and rounding modes specified by the environment."
    ],
    "ruleRole": "semantic-operation-rule",
    "appliesTo": [
      "urn:csabs:concept/FloatingPointType"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:law/fp-rounding-model",
    "type": "Law",
    "statement": "A basic operation returns the rounded exact result as specified by its format and active rounding mode, subject to exceptional cases.",
    "assumptions": [
      "specific IEEE 754 operation and format",
      "active rounding mode recorded"
    ],
    "source": [
      "urn:csabs:source/ieee754"
    ],
    "appliesTo": [
      "urn:csabs:concept/FloatingPointType"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/fp-format-parameters",
      "urn:csabs:axiom/FloatingPointType-environment",
      "urn:csabs:axiom/FloatingPointType-rounding",
      "urn:csabs:axiom/FloatingPointType-exceptions"
    ],
    "formalStatement": "finite in-range exact result z of op ⇒ result_numeric=round_F(z); special inputs, overflow, flags, and traps use the explicitly selected IEEE environment"
  },
  {
    "id": "urn:csabs:law/fp-nonassociativity",
    "type": "Law",
    "statement": "Floating-point addition and multiplication are not associative in general.",
    "formalStatement": "∃a,b,c∈F: fl(fl(a+b)+c)≠fl(a+fl(b+c))",
    "assumptions": [
      "a finite format with rounding"
    ],
    "appliesTo": [
      "urn:csabs:concept/FloatingPointType"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/fp-format-parameters",
      "urn:csabs:axiom/FloatingPointType-environment",
      "urn:csabs:axiom/FloatingPointType-rounding",
      "urn:csabs:axiom/FloatingPointType-exceptions"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:law/fp-nan-unordered",
    "type": "Law",
    "statement": "Under IEEE ordered comparisons, comparisons involving NaN are false, including equality; NaN is unordered.",
    "assumptions": [
      "IEEE comparison predicates"
    ],
    "source": [
      "urn:csabs:source/ieee754"
    ],
    "appliesTo": [
      "urn:csabs:concept/FloatingPointType"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/fp-format-parameters",
      "urn:csabs:axiom/FloatingPointType-environment",
      "urn:csabs:axiom/FloatingPointType-rounding",
      "urn:csabs:axiom/FloatingPointType-exceptions"
    ],
    "formalStatement": "isNaN(x)∨isNaN(y) ⇒ ¬(x<y) ∧ ¬(x≤y) ∧ ¬(x=y) ∧ ¬(x≥y) ∧ ¬(x>y), for ordered numeric predicates"
  },
  {
    "id": "urn:csabs:law/fp-addition-counterexample",
    "type": "Law",
    "statement": "In binary64, round-to-nearest ties-to-even addition can depend on parenthesization.",
    "formalStatement": "a=2^54, b=−2^54, c=1; fl(fl(a+b)+c)=1; fl(a+fl(b+c))=0",
    "assumptions": [
      "IEEE binary64 operations rounded to binary64 after each addition",
      "round-to-nearest ties-to-even",
      "No reassociation or excess precision"
    ],
    "appliesTo": [
      "urn:csabs:concept/FloatingPointType"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "proofSketch": "The exact sum b+c is halfway between two binary64 values and rounds to b. The first parenthesization first computes the exactly representable zero.",
    "dependsOn": [
      "urn:csabs:axiom/fp-format-parameters",
      "urn:csabs:axiom/FloatingPointType-environment",
      "urn:csabs:axiom/FloatingPointType-rounding",
      "urn:csabs:axiom/FloatingPointType-exceptions"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:law/fp-relative-error",
    "type": "Law",
    "statement": "For rounding to nearest with unbounded-exponent idealization, or an in-range normal result without underflow or overflow, a rounded basic arithmetic result satisfies the relative-error model.",
    "formalStatement": "fl(z)=z(1+δ), |δ|≤u, u=β^(1−p)/2",
    "assumptions": [
      "z is the exact arithmetic result",
      "nearest rounding",
      "Normal finite result regime; exceptional values excluded",
      "β is the radix and p the precision"
    ],
    "appliesTo": [
      "urn:csabs:concept/FloatingPointType"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "dependsOn": [
      "urn:csabs:axiom/fp-format-parameters",
      "urn:csabs:axiom/FloatingPointType-environment",
      "urn:csabs:axiom/FloatingPointType-rounding",
      "urn:csabs:axiom/FloatingPointType-exceptions"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/FloatingPointType-representable-rounding-fixed",
    "type": "Theorem",
    "name": "representable-rounding-fixed",
    "statement": "Rounding a finite exactly representable numeric value leaves that value unchanged.",
    "formalStatement": "z∈F finite ⇒ round_F(z)=z numerically",
    "proofSketch": "There is no approximation error to resolve; z is simultaneously nearest and each directed bound. Signed-zero encoding needs its separate sign rule.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for FloatingPointType apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/FloatingPointType"
    ],
    "dependsOn": [
      "urn:csabs:axiom/fp-format-parameters",
      "urn:csabs:axiom/FloatingPointType-environment",
      "urn:csabs:axiom/FloatingPointType-rounding",
      "urn:csabs:axiom/FloatingPointType-exceptions"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
