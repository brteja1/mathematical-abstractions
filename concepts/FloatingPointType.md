# Floating-point type

A finite numeric format with rounded operations and format-dependent exceptional values; it approximates real arithmetic and does not obey all real-number algebraic laws.

**Notation:** Format F(β,p,e_min,e_max,subnormals,rounding); fl(x) denotes rounding of exact x into F under the selected mode. F_fin denotes finite encodings; val : F_fin→ℝ forgets zero sign. In finite error formulas x denotes val(x); numeric equality differs from encoding equality and IEEE predicates on NaNs.

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

## Mathematical formulation

For a supplied format f, the interface consists of rounding mode r, round:Mode×ℝ→Value(f)×Flags and run:Mode×Op×List(Value(f))→Value(f)×Flags. Value(f) distinguishes signed zeros, representable nonzero finite reals, signed infinities and NaN payloads. No correct-rounding or exception law constrains the supplied round/run functions yet.

**Lean formulation** (in its source module context):

```lean
structure FloatingPointType (format : FloatFormat) where
  rounding : RoundingMode
  round : RoundingMode → ℝ → FloatValue format × FloatFlags
  run : RoundingMode → FloatOperation → List (FloatValue format) →
    FloatValue format × FloatFlags
```

**Source:** [`Catalog.FloatingPointType`](../lean/Catalog/Numeric.lean); consulted 2026-11-12.

**Scope:** partial

**Interpretation:** Explicit format, representable finite values, signed zero, infinities, NaNs, rounding modes and result/flag execution interface.

**Limits:** No correctly-rounded arithmetic or exception/NaN payload specification has been proved; run and round are unconstrained client parameters. Not a complete IEEE model. Goldberg error metrics, guarded evaluation, sticky-flag union rule and numerical results are catalog-only; this model supplies no witnesses for them or the square-root interface.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Selected presentation: A finite numeric format with rounded operations and format-dependent exceptional values; it approximates real arithmetic and does not obey all real-number algebraic laws. Governing rules: The carrier and operations are determined by a specified radix, precision, exponent range, subnormal policy, rounding mode, and exceptional-value semantics. Numeric computation uses a specified format, rounding mode, operation, and exceptional-value/flag convention. For a finite exact result in the finite representable range, round returns a representable value according to the selected mode. IEEE-style operations classify invalid, divide-by-zero, overflow, underflow, and inexact; flags and result behavior are part of the environment. The radix grid and error-measure definitions below extend this presentation; the sticky-flags rule applies only to a default nontrapping environment.

**basisKind:** defined-structure

**basisScope:** Numeric-result interface for listed basic IEEE-style operations, with explicit representative rounding and exceptional rules. Complete NaN payload encodings, signaling-NaN bit layouts, trap handlers, and library transcendental functions are outside this interface. Error-analysis rules below use an explicitly selected even radix and p≥2. Guard-digit algorithms are conditional alternative evaluation models, not a weakening of correctly rounded IEEE operations. Error metrics are mathematical observations, not rounded computations in F.

**verificationObligation:** Specify rounding mode, format, exceptional values, and compiler reassociation/fusion behavior.; Define numerical tolerance or bit equality explicitly; parallel reduction trees can change rounded results.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.; Separate input/measurement error from operation rounding error; exact subtraction of stored operands need not approximate the intended real-data difference accurately.; Use absolute error near zero; the normal-range relative-error model does not extend uniformly through underflow. Goldberg calls unit roundoff machine epsilon; here u=β^(1−p)/2, while the gap above 1 is β^(1−p) when exponent 0 is available.; For each conditional result instantiate its grid, equality, rounding and exponent assumptions explicitly at Binary16/32/64/128; specialization alone transfers no axioms or theorems.; Fix every intermediate precision and rounding point; excess precision, double rounding and algebraic reassociation can invalidate an error analysis.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-fp-add"></a>

### floating-point addition

`urn:csabs:operation/fp-add`

**signature:** add_F : F×F→F

**description:** Adds exactly then rounds under the format's active rounding and exception semantics.

**precondition:** Fixed format and IEEE rounding/exception environment; F includes its declared special values. Numeric results alone omit flags and traps.

<a id="node-urn-csabs-operation-fp-subtract"></a>

### floating-point subtraction

`urn:csabs:operation/fp-subtract`

**signature:** sub_F : F×F→F

**description:** Subtracts under the format's rounding and exceptional-value semantics.

**precondition:** Fixed format and IEEE rounding/exception environment; F includes its declared special values. Numeric results alone omit flags and traps.

<a id="node-urn-csabs-operation-fp-multiply"></a>

### floating-point multiplication

`urn:csabs:operation/fp-multiply`

**signature:** mul_F : F×F→F

**description:** Multiplies under the format's rounding and exceptional-value semantics.

**precondition:** Fixed format and IEEE rounding/exception environment; F includes its declared special values. Numeric results alone omit flags and traps.

<a id="node-urn-csabs-operation-fp-divide"></a>

### floating-point division

`urn:csabs:operation/fp-divide`

**signature:** div_F : F×F→F

**description:** Divides under the format's rounding, divide-by-zero, and invalid-operation semantics.

**precondition:** Fixed format and IEEE rounding/exception environment; F includes its declared special values. Numeric results alone omit flags and traps.

<a id="node-urn-csabs-operation-fp-compare"></a>

### floating-point comparison

`urn:csabs:operation/fp-compare`

**signature:** compare_pred : F×F→Bool, pred∈{<,≤,=,≠,≥,>}

**description:** Selected IEEE numeric predicate: NaN makes <,≤,=,≥,> false and ≠ true; +0 and −0 compare equal. This is neither bit equality nor IEEE totalOrder.

**precondition:** Fixed format and IEEE rounding/exception environment; F includes its declared special values. Numeric results alone omit flags and traps.

<a id="node-urn-csabs-operation-fp-convert"></a>

### format conversion

`urn:csabs:operation/fp-convert`

**signature:** convert : F₁→F₂

**description:** Converts between formats with specified rounding and exception behavior.

**precondition:** Fixed format and IEEE rounding/exception environment; F includes its declared special values. Numeric results alone omit flags and traps.

<a id="node-urn-csabs-operation-fp-round"></a>

### real-to-format rounding

`urn:csabs:operation/fp-round`

**signature:** round_F : ℝ→F

**description:** Mathematical rounding to the selected format; overflow outcomes use the explicit environment, and an input real zero uses the declared zero-sign convention.

**precondition:** Format, rounding mode and overflow policy fixed; ℝ contains neither NaNs nor infinities.

<a id="node-urn-csabs-operation-fp-sqrt"></a>

### floating-point square root

`urn:csabs:operation/fp-sqrt`

**signature:** sqrt_F : F→F

**description:** For finite nonnegative x, rounds the exact nonnegative square root once; IEEE sqrt preserves signed zero, returns +∞ for +∞, and returns NaN with invalid for negative nonzero numeric inputs. NaN signaling follows the environment.

**precondition:** IEEE basic square-root interface, chosen format/mode and default nontrapping exceptional results.

<a id="node-urn-csabs-operation-fp-absolute-error"></a>

### absolute approximation error

`urn:csabs:operation/fp-absolute-error`

**signature:** absError : ℝ×ℝ→ℝ≥0

**description:** absError(a,z)=|a−z|, evaluated over exact reals, including z=0.

**precondition:** Finite numeric values interpreted in ℝ; excludes exceptional encodings.

<a id="node-urn-csabs-operation-fp-relative-error"></a>

### relative approximation error

`urn:csabs:operation/fp-relative-error`

**signature:** relError : ℝ×(ℝ∖{0})→ℝ≥0

**description:** relError(a,z)=|a−z|/|z|; undefined at exact target zero.

**precondition:** Finite real approximation a and nonzero exact real target z.

<a id="node-urn-csabs-operation-fp-ulp"></a>

### format spacing at a real value

`urn:csabs:operation/fp-ulp`

**signature:** ulp_F : [−maxFinite,maxFinite]→ℝ>0

**description:** For nonzero normal magnitude β^e≤|z|<β^(e+1), ulp_F(z)=β^(e−p+1); for |z|<β^e_min, including zero, use q=β^(e_min−p+1). At a power of β choose the interval starting there, not predecessor spacing.

**precondition:** Even radix β≥2, p≥2 and gradual underflow; the subnormal/zero branch is not defined for a format without subnormals.

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

**source:** [David Goldberg: What Every Computer Scientist Should Know About Floating-Point Arithmetic (Oracle edited reprint)](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html); citation: David Goldberg, ACM Computing Surveys 23(1), March 1991, pp. 5–48; edited reprint in Oracle Numerical Computation Guide, Appendix D, including later addendum.; accessedOn: 2026-11-08; sourceRole: consulted-expository-reference; historical IEEE discussion, not a replacement for IEEE 754-2019

**sourceLocator:** Floating-point Formats; Special Quantities; Rounding Modes

**sourceNote:** Format parameters and exceptional-value policies, expressed as an abstract interface.

**provenanceKind:** adapted

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

**source:** [David Goldberg: What Every Computer Scientist Should Know About Floating-Point Arithmetic (Oracle edited reprint)](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html); citation: David Goldberg, ACM Computing Surveys 23(1), March 1991, pp. 5–48; edited reprint in Oracle Numerical Computation Guide, Appendix D, including later addendum.; accessedOn: 2026-11-08; sourceRole: consulted-expository-reference; historical IEEE discussion, not a replacement for IEEE 754-2019

**sourceLocator:** Exactly Rounded Operations; Rounding Modes

**sourceNote:** Nearest and directed rounding definitions, restricted to the finite in-range domain.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-FloatingPointType-exceptions"></a>

### exceptions

`urn:csabs:axiom/FloatingPointType-exceptions`

**statement:** IEEE-style operations classify invalid, divide-by-zero, overflow, underflow, and inexact; flags and result behavior are part of the environment.

**formalStatement:** NaN propagation, signed-zero rules, infinities, and exception flags follow the selected IEEE operation and rounding mode; a numeric result alone need not encode flags

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [David Goldberg: What Every Computer Scientist Should Know About Floating-Point Arithmetic (Oracle edited reprint)](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html); citation: David Goldberg, ACM Computing Surveys 23(1), March 1991, pp. 5–48; edited reprint in Oracle Numerical Computation Guide, Appendix D, including later addendum.; accessedOn: 2026-11-08; sourceRole: consulted-expository-reference; historical IEEE discussion, not a replacement for IEEE 754-2019

**sourceLocator:** Exceptions, Flags and Trap Handlers; Table D-4

**sourceNote:** Five exception classes; numeric outcomes and environment state are separate.

**provenanceKind:** adapted

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

<a id="node-urn-csabs-axiom-fp-radix-grid"></a>

### radix finite-value grid

`urn:csabs:axiom/fp-radix-grid`

**statement:** Fix the numeric interpretation of normal values and, when enabled, gradual underflow.

**formalStatement:** Normal: x=±m·β^(e−p+1), β^(p−1)≤m<β^p, e_min≤e≤e_max, m,e integers. With subnormals: x=±kq, 1≤k<β^(p−1), q=β^(e_min−p+1). Include numeric zero; its encodings can have two signs. maxFinite=(β−β^(1−p))β^e_max.

**assumptions:** Even integer β≥2, integer p≥2 and e_min≤e_max; finite numeric values only; subnormal branch conditional on gradual underflow.

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** defining-rule

**source:** [David Goldberg: What Every Computer Scientist Should Know About Floating-Point Arithmetic (Oracle edited reprint)](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html); citation: David Goldberg, ACM Computing Surveys 23(1), March 1991, pp. 5–48; edited reprint in Oracle Numerical Computation Guide, Appendix D, including later addendum.; accessedOn: 2026-11-08; sourceRole: consulted-expository-reference; historical IEEE discussion, not a replacement for IEEE 754-2019

**sourceLocator:** Floating-point Formats; Denormalized Numbers

**sourceNote:** Integer-significand presentation of the normalized and subnormal grids; encoding layouts omitted.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-fp-error-measures"></a>

### error and unit-roundoff conventions

`urn:csabs:axiom/fp-error-measures`

**statement:** Choose exact-real absolute, relative and spacing measures before stating error bounds.

**formalStatement:** absError(a,z)=|a−z|; z≠0 ⇒ relError(a,z)=absError(a,z)/|z|; u=β^(1−p)/2. ulp_F uses the normal exponent interval of |z|, or q at subnormal/zero magnitudes. If e_min≤0≤e_max, successor_F(1)−1=β^(1−p)=2u.

**assumptions:** Finite real a,z; relative error undefined at zero; ulp_F convention as in operation fp-ulp; nearest rounding for the interpretation of u.

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** defining-rule

**source:** [David Goldberg: What Every Computer Scientist Should Know About Floating-Point Arithmetic (Oracle edited reprint)](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html); citation: David Goldberg, ACM Computing Surveys 23(1), March 1991, pp. 5–48; edited reprint in Oracle Numerical Computation Guide, Appendix D, including later addendum.; accessedOn: 2026-11-08; sourceRole: consulted-expository-reference; historical IEEE discussion, not a replacement for IEEE 754-2019

**sourceLocator:** Relative Error and Ulps, equations (1)–(3)

**sourceNote:** Separates the paper’s epsilon from the gap above 1; extends spacing through gradual underflow with a declared boundary convention.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-fp-sticky-flags"></a>

### sticky exception state

`urn:csabs:axiom/fp-sticky-flags`

**statement:** Default nontrapping arithmetic accumulates exception flags until explicitly cleared.

**formalStatement:** E={invalid,divideByZero,overflow,underflow,inexact}; raised⊆E; flags_after=flags_before∪raised, except explicit flag writes/clears.

**assumptions:** IEEE-style default nontrapping execution; flags treated as observable state distinct from numeric results; trap-handler behavior excluded.

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** semantic-operation-rule

**source:** [David Goldberg: What Every Computer Scientist Should Know About Floating-Point Arithmetic (Oracle edited reprint)](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html); citation: David Goldberg, ACM Computing Surveys 23(1), March 1991, pp. 5–48; edited reprint in Oracle Numerical Computation Guide, Appendix D, including later addendum.; accessedOn: 2026-11-08; sourceRole: consulted-expository-reference; historical IEEE discussion, not a replacement for IEEE 754-2019

**sourceLocator:** Exceptions, Flags and Trap Handlers; Table D-4

**sourceNote:** Models the sticky flag behavior without prescribing trap handlers or modern tininess-detection details.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-fp-rounding-model"></a>

### law/fp-rounding-model

`urn:csabs:law/fp-rounding-model`

**statement:** A basic operation returns the rounded exact result as specified by its format and active rounding mode, subject to exceptional cases.

**assumptions:** specific IEEE 754 operation and format; active rounding mode recorded

**source:** [IEEE 754-2019](https://standards.ieee.org/ieee/754/6210/); sourceRole: normative-standard; [David Goldberg: What Every Computer Scientist Should Know About Floating-Point Arithmetic (Oracle edited reprint)](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html); citation: David Goldberg, ACM Computing Surveys 23(1), March 1991, pp. 5–48; edited reprint in Oracle Numerical Computation Guide, Appendix D, including later addendum.; accessedOn: 2026-11-08; sourceRole: consulted-expository-reference; historical IEEE discussion, not a replacement for IEEE 754-2019

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [fp-format-parameters](FloatingPointType.md#node-urn-csabs-axiom-fp-format-parameters); [environment](FloatingPointType.md#node-urn-csabs-axiom-FloatingPointType-environment); [rounding](FloatingPointType.md#node-urn-csabs-axiom-FloatingPointType-rounding); [exceptions](FloatingPointType.md#node-urn-csabs-axiom-FloatingPointType-exceptions)

**formalStatement:** finite in-range exact result z of op ⇒ result_numeric=round_F(z); special inputs, overflow, flags, and traps use the explicitly selected IEEE environment

**sourceLocator:** Formats and Operations / Operations

**sourceNote:** Exact-then-round numeric semantics; existing normative IEEE source retained.

**provenanceKind:** adapted

<a id="node-urn-csabs-law-fp-nonassociativity"></a>

### law/fp-nonassociativity

`urn:csabs:law/fp-nonassociativity`

**statement:** Floating-point addition and multiplication are not associative in general.

**formalStatement:** In general ∃a,b,c∈F_fin: fl(fl(a+b)+c)≠fl(a+fl(b+c)); real-field reassociation is not a valid universal floating-point rule.

**assumptions:** A format admitting a counterexample, such as binary64 under nearest-even; each intermediate rounded in that format. This is not a theorem about every degenerate finite format.

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [fp-format-parameters](FloatingPointType.md#node-urn-csabs-axiom-fp-format-parameters); [environment](FloatingPointType.md#node-urn-csabs-axiom-FloatingPointType-environment); [rounding](FloatingPointType.md#node-urn-csabs-axiom-FloatingPointType-rounding); [exceptions](FloatingPointType.md#node-urn-csabs-axiom-FloatingPointType-exceptions)

**source:** [David Goldberg: What Every Computer Scientist Should Know About Floating-Point Arithmetic (Oracle edited reprint)](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html); citation: David Goldberg, ACM Computing Surveys 23(1), March 1991, pp. 5–48; edited reprint in Oracle Numerical Computation Guide, Appendix D, including later addendum.; accessedOn: 2026-11-08; sourceRole: consulted-expository-reference; historical IEEE discussion, not a replacement for IEEE 754-2019

**sourceLocator:** Systems Aspects / Optimizers

**sourceNote:** Failure of unrestricted algebraic reassociation; existential addition statement retained.

**provenanceKind:** adapted

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

**dependsOn:** [fp-format-parameters](FloatingPointType.md#node-urn-csabs-axiom-fp-format-parameters); [environment](FloatingPointType.md#node-urn-csabs-axiom-FloatingPointType-environment); [rounding](FloatingPointType.md#node-urn-csabs-axiom-FloatingPointType-rounding); [exceptions](FloatingPointType.md#node-urn-csabs-axiom-FloatingPointType-exceptions); [normal-grid](Binary64.md#node-urn-csabs-axiom-Binary64-normal-grid)

**source:** [David Goldberg: What Every Computer Scientist Should Know About Floating-Point Arithmetic (Oracle edited reprint)](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html); citation: David Goldberg, ACM Computing Surveys 23(1), March 1991, pp. 5–48; edited reprint in Oracle Numerical Computation Guide, Appendix D, including later addendum.; accessedOn: 2026-11-08; sourceRole: consulted-expository-reference; historical IEEE discussion, not a replacement for IEEE 754-2019

**sourceLocator:** Exactly Rounded Operations (nearest-even rule); Systems Aspects / Optimizers

**sourceNote:** Local binary64 instantiation of the parenthesization warning; powers of two and halfway rounding provide the derivation.

**provenanceKind:** derived

<a id="node-urn-csabs-law-fp-relative-error"></a>

### law/fp-relative-error

`urn:csabs:law/fp-relative-error`

**statement:** Nearest rounding of a nonzero exact value within the normal finite range satisfies a uniform relative-error bound.

**formalStatement:** fl(z)=z(1+δ), |δ|≤u, u=β^(1−p)/2

**assumptions:** z is the exact real result, z≠0, β^e_min≤|z|≤maxFinite; alternatively use an unbounded-exponent idealization.; Nearest rounding in an even radix β≥2 with p≥2; NaNs, infinities, overflow and the subnormal exact-result regime excluded.

**reviewStatus:** editorial-summary; not machine-proved

**dependsOn:** [fp-format-parameters](FloatingPointType.md#node-urn-csabs-axiom-fp-format-parameters); [environment](FloatingPointType.md#node-urn-csabs-axiom-FloatingPointType-environment); [rounding](FloatingPointType.md#node-urn-csabs-axiom-FloatingPointType-rounding); [exceptions](FloatingPointType.md#node-urn-csabs-axiom-FloatingPointType-exceptions)

**source:** [David Goldberg: What Every Computer Scientist Should Know About Floating-Point Arithmetic (Oracle edited reprint)](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html); citation: David Goldberg, ACM Computing Surveys 23(1), March 1991, pp. 5–48; edited reprint in Oracle Numerical Computation Guide, Appendix D, including later addendum.; accessedOn: 2026-11-08; sourceRole: consulted-expository-reference; historical IEEE discussion, not a replacement for IEEE 754-2019

**sourceLocator:** Relative Error and Ulps, equation (2); The Details / Rounding Error

**sourceNote:** Uses u for the paper’s epsilon and makes the nonzero normal exact-result restriction explicit.

**provenanceKind:** adapted

**proofSketch:** In each exponent interval, nearest rounding changes the result by at most half a grid step. Divide this absolute bound by |z|≥β^e to obtain u. Zero is handled separately as an exact representable value.

<a id="node-urn-csabs-law-fp-guard-not-correct-rounding"></a>

### one guard digit need not give correct rounding

`urn:csabs:law/fp-guard-not-correct-rounding`

**statement:** A local guarded error bound is weaker than exact-then-round semantics.

**formalStatement:** β=10,p=3: G(110,8.59)=102, while RN_3(110−8.59)=RN_3(101.41)=101.

**assumptions:** One-guard-digit alignment/truncation algorithm of fp-guard-digit-error; nearest final rounding; adequate exponent range.

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [radix finite-value grid](FloatingPointType.md#node-urn-csabs-axiom-fp-radix-grid); [error and unit-roundoff conventions](FloatingPointType.md#node-urn-csabs-axiom-fp-error-measures); [one-guard-digit subtraction bound](FloatingPointType.md#node-urn-csabs-theorem-fp-guard-digit-error)

**proofSketch:** Alignment truncates 8.59 to 8.5 at the working scale; 110−8.5=101.5 rounds to 102, whereas the exact difference rounds to 101.

**source:** [David Goldberg: What Every Computer Scientist Should Know About Floating-Point Arithmetic (Oracle edited reprint)](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html); citation: David Goldberg, ACM Computing Surveys 23(1), March 1991, pp. 5–48; edited reprint in Oracle Numerical Computation Guide, Appendix D, including later addendum.; accessedOn: 2026-11-08; sourceRole: consulted-expository-reference; historical IEEE discussion, not a replacement for IEEE 754-2019

**sourceLocator:** Guard Digits, example immediately before Theorem 2; Exactly Rounded Operations

**sourceNote:** Preserves the paper’s concrete distinction between guarded and correctly rounded operations.

**provenanceKind:** adapted

<a id="node-urn-csabs-law-fp-double-rounding-counterexample"></a>

### double rounding counterexample

`urn:csabs:law/fp-double-rounding-counterexample`

**statement:** Rounding through a wider intermediate format can change the final target-format value.

**formalStatement:** RN_2(RN_3(12.51))=RN_2(12.5)=12 ≠ 13=RN_2(12.51), radix 10.

**assumptions:** Decimal precision 3 then 2; nearest ties-to-even at both stages; exact real input 12.51 and adequate exponent ranges.

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [radix finite-value grid](FloatingPointType.md#node-urn-csabs-axiom-fp-radix-grid); [rounding](FloatingPointType.md#node-urn-csabs-axiom-FloatingPointType-rounding)

**proofSketch:** The first rounding creates a target halfway case; the even last digit selects 12, although direct rounding selects 13.

**source:** [David Goldberg: What Every Computer Scientist Should Know About Floating-Point Arithmetic (Oracle edited reprint)](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html); citation: David Goldberg, ACM Computing Surveys 23(1), March 1991, pp. 5–48; edited reprint in Oracle Numerical Computation Guide, Appendix D, including later addendum.; accessedOn: 2026-11-08; sourceRole: consulted-expository-reference; historical IEEE discussion, not a replacement for IEEE 754-2019

**sourceLocator:** The Details / Binary to Decimal Conversion, double-rounding example

**sourceNote:** A decimal counterexample; no assertion that every widening conversion fails.

**provenanceKind:** adapted

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

**source:** [David Goldberg: What Every Computer Scientist Should Know About Floating-Point Arithmetic (Oracle edited reprint)](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html); citation: David Goldberg, ACM Computing Surveys 23(1), March 1991, pp. 5–48; edited reprint in Oracle Numerical Computation Guide, Appendix D, including later addendum.; accessedOn: 2026-11-08; sourceRole: consulted-expository-reference; historical IEEE discussion, not a replacement for IEEE 754-2019

**sourceLocator:** Exactly Rounded Operations; Rounding Modes

**sourceNote:** Immediate consequence of the nearest/directed rounding definitions; numeric equality only.

**provenanceKind:** derived

<a id="node-urn-csabs-theorem-fp-nearest-absolute-error"></a>

### nearest rounding absolute bound

`urn:csabs:theorem/fp-nearest-absolute-error`

**statement:** Nearest rounding has at most half the declared spacing of absolute error, including the gradual-underflow region.

**formalStatement:** |RN_F(z)−z|≤ulp_F(z)/2; if |z|<β^e_min then |RN_F(z)−z|≤q/2.

**assumptions:** Finite exact z with |z|≤maxFinite; gradual underflow, nearest rounding and fp-ulp boundary convention.

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [radix finite-value grid](FloatingPointType.md#node-urn-csabs-axiom-fp-radix-grid); [error and unit-roundoff conventions](FloatingPointType.md#node-urn-csabs-axiom-fp-error-measures); [rounding](FloatingPointType.md#node-urn-csabs-axiom-FloatingPointType-rounding); [urn:csabs:law/fp-rounding-model](FloatingPointType.md#node-urn-csabs-law-fp-rounding-model)

**proofSketch:** Within an exponent interval adjacent grid points differ by ulp_F(z); nearest rounding is at most half that distance. The lower neighbor gap at an exponent boundary is smaller. Below the normal threshold the same argument uses the fixed step q.

**source:** [David Goldberg: What Every Computer Scientist Should Know About Floating-Point Arithmetic (Oracle edited reprint)](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html); citation: David Goldberg, ACM Computing Surveys 23(1), March 1991, pp. 5–48; edited reprint in Oracle Numerical Computation Guide, Appendix D, including later addendum.; accessedOn: 2026-11-08; sourceRole: consulted-expository-reference; historical IEEE discussion, not a replacement for IEEE 754-2019

**sourceLocator:** Relative Error and Ulps; Denormalized Numbers

**sourceNote:** Half-ulp nearest rounding extended to the uniform subnormal grid.

**provenanceKind:** derived

<a id="node-urn-csabs-theorem-fp-guard-digit-error"></a>

### one-guard-digit subtraction bound

`urn:csabs:theorem/fp-guard-digit-error`

**statement:** A specified guarded subtraction algorithm controls local error even during cancellation.

**formalStatement:** z=x−y≠0 ⇒ |G(x,y)−z|/|z|<2u.

**assumptions:** Exactly known finite stored operands; align significands, truncate the shifted smaller magnitude to p+1 digits, subtract, then round to nearest p digits.; Even radix β≥2, p≥2; unbounded exponents or all relevant nonzero values remain normal and finite. G is this algorithm, not a claim of correct rounding.

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [radix finite-value grid](FloatingPointType.md#node-urn-csabs-axiom-fp-radix-grid); [error and unit-roundoff conventions](FloatingPointType.md#node-urn-csabs-axiom-fp-error-measures)

**proofSketch:** Bound the discarded aligned tail and final nearest-rounding error as in Theorem 9; same-sign addition after sign reduction uses Theorem 10.

**source:** [David Goldberg: What Every Computer Scientist Should Know About Floating-Point Arithmetic (Oracle edited reprint)](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html); citation: David Goldberg, ACM Computing Surveys 23(1), March 1991, pp. 5–48; edited reprint in Oracle Numerical Computation Guide, Appendix D, including later addendum.; accessedOn: 2026-11-08; sourceRole: consulted-expository-reference; historical IEEE discussion, not a replacement for IEEE 754-2019

**sourceLocator:** Guard Digits, Theorem 2; The Details / Rounding Error, Theorems 9–10

**sourceNote:** States the algorithm and excludes exponent exceptions omitted in the idealized analysis.

**provenanceKind:** adapted

<a id="node-urn-csabs-theorem-fp-sterbenz-exact-subtraction"></a>

### Sterbenz exact subtraction

`urn:csabs:theorem/fp-sterbenz-exact-subtraction`

**statement:** Nearby nonnegative stored floating-point numbers can be subtracted without numeric rounding error.

**formalStatement:** x,y∈F_fin, 0≤y/2≤x≤2y ⇒ sub_F(x,y)=x−y numerically.

**assumptions:** One radix/precision for both operands; correctly rounded subtraction, or Goldberg’s one-guard-digit algorithm.; Gradual underflow enabled, or the exact nonzero difference remains in the normal range; finite inputs and numeric real equality; signed-zero encoding governed separately.

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [radix finite-value grid](FloatingPointType.md#node-urn-csabs-axiom-fp-radix-grid); [rounding](FloatingPointType.md#node-urn-csabs-axiom-FloatingPointType-rounding); [urn:csabs:law/fp-rounding-model](FloatingPointType.md#node-urn-csabs-law-fp-rounding-model)

**proofSketch:** Alignment requires at most one extra radix digit. The factor-two condition ensures cancellation leaves at most p significant digits, so the exact difference is representable. Gradual underflow preserves representability near zero; rounding then fixes it.

**source:** [David Goldberg: What Every Computer Scientist Should Know About Floating-Point Arithmetic (Oracle edited reprint)](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html); citation: David Goldberg, ACM Computing Surveys 23(1), March 1991, pp. 5–48; edited reprint in Oracle Numerical Computation Guide, Appendix D, including later addendum.; accessedOn: 2026-11-08; sourceRole: consulted-expository-reference; historical IEEE discussion, not a replacement for IEEE 754-2019

**sourceLocator:** The Details / Rounding Error, Theorem 11; Denormalized Numbers

**sourceNote:** Explicit nonnegative carriers and underflow conditions for the exact-subtraction lemma.

**provenanceKind:** adapted

<a id="node-urn-csabs-theorem-fp-gradual-underflow-zero-difference"></a>

### zero difference detects equal finite values

`urn:csabs:theorem/fp-gradual-underflow-zero-difference`

**statement:** Gradual underflow preserves the zero-difference equality test on finite operands.

**formalStatement:** sub_F(x,y)==0 ⇔ val(x)=val(y).

**assumptions:** Finite operands in the same radix grid, gradual underflow, correctly rounded subtraction in a nearest or directed mode.; Default nontrapping results; numeric equality identifies signed zeros; no flush-to-zero or denormals-are-zero; overflow may yield an infinity, which is nonzero.

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [radix finite-value grid](FloatingPointType.md#node-urn-csabs-axiom-fp-radix-grid); [rounding](FloatingPointType.md#node-urn-csabs-axiom-FloatingPointType-rounding); [urn:csabs:law/fp-rounding-model](FloatingPointType.md#node-urn-csabs-law-fp-rounding-model)

**proofSketch:** Every finite grid value is an integer multiple of q. Distinct inputs differ by at least q, so rounding cannot turn the difference into zero; equal numeric inputs have an exact zero difference.

**source:** [David Goldberg: What Every Computer Scientist Should Know About Floating-Point Arithmetic (Oracle edited reprint)](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html); citation: David Goldberg, ACM Computing Surveys 23(1), March 1991, pp. 5–48; edited reprint in Oracle Numerical Computation Guide, Appendix D, including later addendum.; accessedOn: 2026-11-08; sourceRole: consulted-expository-reference; historical IEEE discussion, not a replacement for IEEE 754-2019

**sourceLocator:** Denormalized Numbers, equation (10)

**sourceNote:** Excludes NaNs and infinities, for which the equivalence fails.

**provenanceKind:** derived

<a id="node-urn-csabs-theorem-fp-cancellation-input-error"></a>

### input-error amplification in subtraction

`urn:csabs:theorem/fp-cancellation-input-error`

**statement:** Even an exact subtraction of stored operands may expose large errors relative to the intended inputs.

**formalStatement:** x̂=x+Δx, ŷ=y+Δy, x≠y ⇒ |(x̂−ŷ)−(x−y)|/|x−y|≤(|Δx|+|Δy|)/|x−y|. If |Δx|≤η|x| and |Δy|≤η|y|, the bound is η(|x|+|y|)/|x−y|.

**assumptions:** Finite real inputs and perturbations; x≠y; this bound concerns input perturbation before any subtraction-rounding error.

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [error and unit-roundoff conventions](FloatingPointType.md#node-urn-csabs-axiom-fp-error-measures)

**proofSketch:** Subtract the two exact differences to obtain Δx−Δy, apply the real triangle inequality, and divide by |x−y|. Substitute the individual perturbation bounds for the second inequality.

**source:** [David Goldberg: What Every Computer Scientist Should Know About Floating-Point Arithmetic (Oracle edited reprint)](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html); citation: David Goldberg, ACM Computing Surveys 23(1), March 1991, pp. 5–48; edited reprint in Oracle Numerical Computation Guide, Appendix D, including later addendum.; accessedOn: 2026-11-08; sourceRole: consulted-expository-reference; historical IEEE discussion, not a replacement for IEEE 754-2019

**sourceLocator:** Cancellation; The Details / Rounding Error, equations (19)–(23)

**sourceNote:** Derives a precise perturbation bound for the paper’s distinction between benign and catastrophic cancellation.

**provenanceKind:** derived

<a id="node-urn-csabs-theorem-fp-nearest-even-iteration"></a>

### nearest-even subtract-add stability

`urn:csabs:theorem/fp-nearest-even-iteration`

**statement:** With the cited idealized arithmetic, repeated subtraction and addition of the same value stabilizes after one iteration.

**formalStatement:** T(t)=RN(RN(t−y)+y); x_0=x; x_(n+1)=T(x_n) ⇒ ∀n≥1, x_n=x_1 (and possibly x_1=x).

**assumptions:** Finite x,y in one even-radix precision-p grid; correctly rounded nearest ties-to-even after each operation.; Unbounded-exponent model, or a finite execution whose intermediates never underflow or overflow; no excess precision or reassociation; numeric equality.

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [radix finite-value grid](FloatingPointType.md#node-urn-csabs-axiom-fp-radix-grid); [rounding](FloatingPointType.md#node-urn-csabs-axiom-FloatingPointType-rounding)

**proofSketch:** Use the cited Theorem 5: either every iterate equals x or every positive-index iterate equals x_1. Both cases imply T(T(x))=T(x); its nearest-even tie rule is essential. This is a citation of that result, not an independent formal proof.

**source:** [David Goldberg: What Every Computer Scientist Should Know About Floating-Point Arithmetic (Oracle edited reprint)](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html); citation: David Goldberg, ACM Computing Surveys 23(1), March 1991, pp. 5–48; edited reprint in Oracle Numerical Computation Guide, Appendix D, including later addendum.; accessedOn: 2026-11-08; sourceRole: consulted-expository-reference; historical IEEE discussion, not a replacement for IEEE 754-2019

**sourceLocator:** Exactly Rounded Operations, Theorem 5 (Reiser and Knuth)

**sourceNote:** Restricts the cited result to its ordinary finite, nonexceptional regime.

**provenanceKind:** adapted

## Concept provenance

- [IEEE 754-2019](https://standards.ieee.org/ieee/754/6210/); sourceRole: normative-standard
- [David Goldberg: What Every Computer Scientist Should Know About Floating-Point Arithmetic (Oracle edited reprint)](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html); citation: David Goldberg, ACM Computing Surveys 23(1), March 1991, pp. 5–48; edited reprint in Oracle Numerical Computation Guide, Appendix D, including later addendum.; accessedOn: 2026-11-08; sourceRole: consulted-expository-reference; historical IEEE discussion, not a replacement for IEEE 754-2019

**sourceLocator:** Floating-point Formats; Relative Error and Ulps; The IEEE Standard; Systems Aspects

**sourceNote:** Extends the existing format abstraction with explicit finite-value grids, error measures and conditional numerical results. The historical reprint does not document binary16 or binary128 parameters.

**provenanceKind:** adapted

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
    "notation": "Format F(β,p,e_min,e_max,subnormals,rounding); fl(x) denotes rounding of exact x into F under the selected mode. F_fin denotes finite encodings; val : F_fin→ℝ forgets zero sign. In finite error formulas x denotes val(x); numeric equality differs from encoding equality and IEEE predicates on NaNs.",
    "source": [
      "urn:csabs:source/ieee754",
      "urn:csabs:source/goldberg-floating-point-oracle"
    ],
    "hasOperation": [
      "urn:csabs:operation/fp-add",
      "urn:csabs:operation/fp-subtract",
      "urn:csabs:operation/fp-multiply",
      "urn:csabs:operation/fp-divide",
      "urn:csabs:operation/fp-compare",
      "urn:csabs:operation/fp-convert",
      "urn:csabs:operation/fp-round",
      "urn:csabs:operation/fp-sqrt",
      "urn:csabs:operation/fp-absolute-error",
      "urn:csabs:operation/fp-relative-error",
      "urn:csabs:operation/fp-ulp"
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
      "urn:csabs:axiom/FloatingPointType-signed-zeros",
      "urn:csabs:axiom/fp-radix-grid",
      "urn:csabs:axiom/fp-error-measures",
      "urn:csabs:axiom/fp-sticky-flags"
    ],
    "hasLaw": [
      "urn:csabs:law/fp-rounding-model",
      "urn:csabs:law/fp-nonassociativity",
      "urn:csabs:law/fp-nan-unordered",
      "urn:csabs:law/fp-addition-counterexample",
      "urn:csabs:law/fp-relative-error",
      "urn:csabs:law/fp-guard-not-correct-rounding",
      "urn:csabs:law/fp-double-rounding-counterexample"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/FloatingPointType-representable-rounding-fixed",
      "urn:csabs:theorem/fp-nearest-absolute-error",
      "urn:csabs:theorem/fp-guard-digit-error",
      "urn:csabs:theorem/fp-sterbenz-exact-subtraction",
      "urn:csabs:theorem/fp-gradual-underflow-zero-difference",
      "urn:csabs:theorem/fp-cancellation-input-error",
      "urn:csabs:theorem/fp-nearest-even-iteration"
    ],
    "relatedConcept": [
      "urn:csabs:concept/MathematicalInteger"
    ],
    "coverageStatus": "basis-reviewed",
    "requiresConcept": [],
    "verificationObligation": [
      "Specify rounding mode, format, exceptional values, and compiler reassociation/fusion behavior.",
      "Define numerical tolerance or bit equality explicitly; parallel reduction trees can change rounded results.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.",
      "Separate input/measurement error from operation rounding error; exact subtraction of stored operands need not approximate the intended real-data difference accurately.",
      "Use absolute error near zero; the normal-range relative-error model does not extend uniformly through underflow. Goldberg calls unit roundoff machine epsilon; here u=β^(1−p)/2, while the gap above 1 is β^(1−p) when exponent 0 is available.",
      "For each conditional result instantiate its grid, equality, rounding and exponent assumptions explicitly at Binary16/32/64/128; specialization alone transfers no axioms or theorems.",
      "Fix every intermediate precision and rounding point; excess precision, double rounding and algebraic reassociation can invalidate an error analysis."
    ],
    "axiomBasis": "Selected presentation: A finite numeric format with rounded operations and format-dependent exceptional values; it approximates real arithmetic and does not obey all real-number algebraic laws. Governing rules: The carrier and operations are determined by a specified radix, precision, exponent range, subnormal policy, rounding mode, and exceptional-value semantics. Numeric computation uses a specified format, rounding mode, operation, and exceptional-value/flag convention. For a finite exact result in the finite representable range, round returns a representable value according to the selected mode. IEEE-style operations classify invalid, divide-by-zero, overflow, underflow, and inexact; flags and result behavior are part of the environment. The radix grid and error-measure definitions below extend this presentation; the sticky-flags rule applies only to a default nontrapping environment.",
    "basisKind": "defined-structure",
    "basisScope": "Numeric-result interface for listed basic IEEE-style operations, with explicit representative rounding and exceptional rules. Complete NaN payload encodings, signaling-NaN bit layouts, trap handlers, and library transcendental functions are outside this interface. Error-analysis rules below use an explicitly selected even radix and p≥2. Guard-digit algorithms are conditional alternative evaluation models, not a weakening of correctly rounded IEEE operations. Error metrics are mathematical observations, not rounded computations in F.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "sourceLocator": "Floating-point Formats; Relative Error and Ulps; The IEEE Standard; Systems Aspects",
    "sourceNote": "Extends the existing format abstraction with explicit finite-value grids, error measures and conditional numerical results. The historical reprint does not document binary16 or binary128 parameters.",
    "provenanceKind": "adapted",
    "leanFormulation": "structure FloatingPointType (format : FloatFormat) where\n  rounding : RoundingMode\n  round : RoundingMode → ℝ → FloatValue format × FloatFlags\n  run : RoundingMode → FloatOperation → List (FloatValue format) →\n    FloatValue format × FloatFlags",
    "formulationSource": "urn:csabs:source/local-lean-Numeric",
    "formulationLocator": "Catalog.FloatingPointType",
    "formulationScope": "partial",
    "leanModelMapping": "Explicit format, representable finite values, signed zero, infinities, NaNs, rounding modes and result/flag execution interface.",
    "leanModelLimitations": "No correctly-rounded arithmetic or exception/NaN payload specification has been proved; run and round are unconstrained client parameters. Not a complete IEEE model. Goldberg error metrics, guarded evaluation, sticky-flag union rule and numerical results are catalog-only; this model supplies no witnesses for them or the square-root interface.",
    "mathematicalFormulation": "For a supplied format f, the interface consists of rounding mode r, round:Mode×ℝ→Value(f)×Flags and run:Mode×Op×List(Value(f))→Value(f)×Flags. Value(f) distinguishes signed zeros, representable nonzero finite reals, signed infinities and NaN payloads. No correct-rounding or exception law constrains the supplied round/run functions yet."
  },
  {
    "id": "urn:csabs:operation/fp-add",
    "type": "Operation",
    "name": "floating-point addition",
    "signature": "add_F : F×F→F",
    "description": "Adds exactly then rounds under the format's active rounding and exception semantics.",
    "concept": "urn:csabs:concept/FloatingPointType",
    "precondition": "Fixed format and IEEE rounding/exception environment; F includes its declared special values. Numeric results alone omit flags and traps."
  },
  {
    "id": "urn:csabs:operation/fp-subtract",
    "type": "Operation",
    "name": "floating-point subtraction",
    "signature": "sub_F : F×F→F",
    "description": "Subtracts under the format's rounding and exceptional-value semantics.",
    "concept": "urn:csabs:concept/FloatingPointType",
    "precondition": "Fixed format and IEEE rounding/exception environment; F includes its declared special values. Numeric results alone omit flags and traps."
  },
  {
    "id": "urn:csabs:operation/fp-multiply",
    "type": "Operation",
    "name": "floating-point multiplication",
    "signature": "mul_F : F×F→F",
    "description": "Multiplies under the format's rounding and exceptional-value semantics.",
    "concept": "urn:csabs:concept/FloatingPointType",
    "precondition": "Fixed format and IEEE rounding/exception environment; F includes its declared special values. Numeric results alone omit flags and traps."
  },
  {
    "id": "urn:csabs:operation/fp-divide",
    "type": "Operation",
    "name": "floating-point division",
    "signature": "div_F : F×F→F",
    "description": "Divides under the format's rounding, divide-by-zero, and invalid-operation semantics.",
    "concept": "urn:csabs:concept/FloatingPointType",
    "precondition": "Fixed format and IEEE rounding/exception environment; F includes its declared special values. Numeric results alone omit flags and traps."
  },
  {
    "id": "urn:csabs:operation/fp-compare",
    "type": "Operation",
    "name": "floating-point comparison",
    "signature": "compare_pred : F×F→Bool, pred∈{<,≤,=,≠,≥,>}",
    "description": "Selected IEEE numeric predicate: NaN makes <,≤,=,≥,> false and ≠ true; +0 and −0 compare equal. This is neither bit equality nor IEEE totalOrder.",
    "concept": "urn:csabs:concept/FloatingPointType",
    "precondition": "Fixed format and IEEE rounding/exception environment; F includes its declared special values. Numeric results alone omit flags and traps."
  },
  {
    "id": "urn:csabs:operation/fp-convert",
    "type": "Operation",
    "name": "format conversion",
    "signature": "convert : F₁→F₂",
    "description": "Converts between formats with specified rounding and exception behavior.",
    "concept": "urn:csabs:concept/FloatingPointType",
    "precondition": "Fixed format and IEEE rounding/exception environment; F includes its declared special values. Numeric results alone omit flags and traps."
  },
  {
    "id": "urn:csabs:operation/fp-round",
    "type": "Operation",
    "name": "real-to-format rounding",
    "signature": "round_F : ℝ→F",
    "description": "Mathematical rounding to the selected format; overflow outcomes use the explicit environment, and an input real zero uses the declared zero-sign convention.",
    "precondition": "Format, rounding mode and overflow policy fixed; ℝ contains neither NaNs nor infinities.",
    "concept": "urn:csabs:concept/FloatingPointType"
  },
  {
    "id": "urn:csabs:operation/fp-sqrt",
    "type": "Operation",
    "name": "floating-point square root",
    "signature": "sqrt_F : F→F",
    "description": "For finite nonnegative x, rounds the exact nonnegative square root once; IEEE sqrt preserves signed zero, returns +∞ for +∞, and returns NaN with invalid for negative nonzero numeric inputs. NaN signaling follows the environment.",
    "precondition": "IEEE basic square-root interface, chosen format/mode and default nontrapping exceptional results.",
    "concept": "urn:csabs:concept/FloatingPointType"
  },
  {
    "id": "urn:csabs:operation/fp-absolute-error",
    "type": "Operation",
    "name": "absolute approximation error",
    "signature": "absError : ℝ×ℝ→ℝ≥0",
    "description": "absError(a,z)=|a−z|, evaluated over exact reals, including z=0.",
    "precondition": "Finite numeric values interpreted in ℝ; excludes exceptional encodings.",
    "concept": "urn:csabs:concept/FloatingPointType"
  },
  {
    "id": "urn:csabs:operation/fp-relative-error",
    "type": "Operation",
    "name": "relative approximation error",
    "signature": "relError : ℝ×(ℝ∖{0})→ℝ≥0",
    "description": "relError(a,z)=|a−z|/|z|; undefined at exact target zero.",
    "precondition": "Finite real approximation a and nonzero exact real target z.",
    "concept": "urn:csabs:concept/FloatingPointType"
  },
  {
    "id": "urn:csabs:operation/fp-ulp",
    "type": "Operation",
    "name": "format spacing at a real value",
    "signature": "ulp_F : [−maxFinite,maxFinite]→ℝ>0",
    "description": "For nonzero normal magnitude β^e≤|z|<β^(e+1), ulp_F(z)=β^(e−p+1); for |z|<β^e_min, including zero, use q=β^(e_min−p+1). At a power of β choose the interval starting there, not predecessor spacing.",
    "precondition": "Even radix β≥2, p≥2 and gradual underflow; the subnormal/zero branch is not defined for a format without subnormals.",
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
    "source": [
      "urn:csabs:source/goldberg-floating-point-oracle"
    ],
    "sourceLocator": "Floating-point Formats; Special Quantities; Rounding Modes",
    "sourceNote": "Format parameters and exceptional-value policies, expressed as an abstract interface.",
    "provenanceKind": "adapted"
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
    "source": [
      "urn:csabs:source/goldberg-floating-point-oracle"
    ],
    "sourceLocator": "Exactly Rounded Operations; Rounding Modes",
    "sourceNote": "Nearest and directed rounding definitions, restricted to the finite in-range domain.",
    "provenanceKind": "adapted"
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
    "source": [
      "urn:csabs:source/goldberg-floating-point-oracle"
    ],
    "sourceLocator": "Exceptions, Flags and Trap Handlers; Table D-4",
    "sourceNote": "Five exception classes; numeric outcomes and environment state are separate.",
    "provenanceKind": "adapted"
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
    "id": "urn:csabs:axiom/fp-radix-grid",
    "type": "Axiom",
    "name": "radix finite-value grid",
    "statement": "Fix the numeric interpretation of normal values and, when enabled, gradual underflow.",
    "formalStatement": "Normal: x=±m·β^(e−p+1), β^(p−1)≤m<β^p, e_min≤e≤e_max, m,e integers. With subnormals: x=±kq, 1≤k<β^(p−1), q=β^(e_min−p+1). Include numeric zero; its encodings can have two signs. maxFinite=(β−β^(1−p))β^e_max.",
    "assumptions": [
      "Even integer β≥2, integer p≥2 and e_min≤e_max; finite numeric values only; subnormal branch conditional on gradual underflow."
    ],
    "appliesTo": [
      "urn:csabs:concept/FloatingPointType"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "defining-rule",
    "source": [
      "urn:csabs:source/goldberg-floating-point-oracle"
    ],
    "sourceLocator": "Floating-point Formats; Denormalized Numbers",
    "sourceNote": "Integer-significand presentation of the normalized and subnormal grids; encoding layouts omitted.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/fp-error-measures",
    "type": "Axiom",
    "name": "error and unit-roundoff conventions",
    "statement": "Choose exact-real absolute, relative and spacing measures before stating error bounds.",
    "formalStatement": "absError(a,z)=|a−z|; z≠0 ⇒ relError(a,z)=absError(a,z)/|z|; u=β^(1−p)/2. ulp_F uses the normal exponent interval of |z|, or q at subnormal/zero magnitudes. If e_min≤0≤e_max, successor_F(1)−1=β^(1−p)=2u.",
    "assumptions": [
      "Finite real a,z; relative error undefined at zero; ulp_F convention as in operation fp-ulp; nearest rounding for the interpretation of u."
    ],
    "appliesTo": [
      "urn:csabs:concept/FloatingPointType"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "defining-rule",
    "source": [
      "urn:csabs:source/goldberg-floating-point-oracle"
    ],
    "sourceLocator": "Relative Error and Ulps, equations (1)–(3)",
    "sourceNote": "Separates the paper’s epsilon from the gap above 1; extends spacing through gradual underflow with a declared boundary convention.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/fp-sticky-flags",
    "type": "Axiom",
    "name": "sticky exception state",
    "statement": "Default nontrapping arithmetic accumulates exception flags until explicitly cleared.",
    "formalStatement": "E={invalid,divideByZero,overflow,underflow,inexact}; raised⊆E; flags_after=flags_before∪raised, except explicit flag writes/clears.",
    "assumptions": [
      "IEEE-style default nontrapping execution; flags treated as observable state distinct from numeric results; trap-handler behavior excluded."
    ],
    "appliesTo": [
      "urn:csabs:concept/FloatingPointType"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "semantic-operation-rule",
    "source": [
      "urn:csabs:source/goldberg-floating-point-oracle"
    ],
    "sourceLocator": "Exceptions, Flags and Trap Handlers; Table D-4",
    "sourceNote": "Models the sticky flag behavior without prescribing trap handlers or modern tininess-detection details.",
    "provenanceKind": "adapted"
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
      "urn:csabs:source/ieee754",
      "urn:csabs:source/goldberg-floating-point-oracle"
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
    "formalStatement": "finite in-range exact result z of op ⇒ result_numeric=round_F(z); special inputs, overflow, flags, and traps use the explicitly selected IEEE environment",
    "sourceLocator": "Formats and Operations / Operations",
    "sourceNote": "Exact-then-round numeric semantics; existing normative IEEE source retained.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/fp-nonassociativity",
    "type": "Law",
    "statement": "Floating-point addition and multiplication are not associative in general.",
    "formalStatement": "In general ∃a,b,c∈F_fin: fl(fl(a+b)+c)≠fl(a+fl(b+c)); real-field reassociation is not a valid universal floating-point rule.",
    "assumptions": [
      "A format admitting a counterexample, such as binary64 under nearest-even; each intermediate rounded in that format. This is not a theorem about every degenerate finite format."
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
    "source": [
      "urn:csabs:source/goldberg-floating-point-oracle"
    ],
    "sourceLocator": "Systems Aspects / Optimizers",
    "sourceNote": "Failure of unrestricted algebraic reassociation; existential addition statement retained.",
    "provenanceKind": "adapted"
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
      "urn:csabs:axiom/FloatingPointType-exceptions",
      "urn:csabs:axiom/Binary64-normal-grid"
    ],
    "source": [
      "urn:csabs:source/goldberg-floating-point-oracle"
    ],
    "sourceLocator": "Exactly Rounded Operations (nearest-even rule); Systems Aspects / Optimizers",
    "sourceNote": "Local binary64 instantiation of the parenthesization warning; powers of two and halfway rounding provide the derivation.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:law/fp-relative-error",
    "type": "Law",
    "statement": "Nearest rounding of a nonzero exact value within the normal finite range satisfies a uniform relative-error bound.",
    "formalStatement": "fl(z)=z(1+δ), |δ|≤u, u=β^(1−p)/2",
    "assumptions": [
      "z is the exact real result, z≠0, β^e_min≤|z|≤maxFinite; alternatively use an unbounded-exponent idealization.",
      "Nearest rounding in an even radix β≥2 with p≥2; NaNs, infinities, overflow and the subnormal exact-result regime excluded."
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
    "source": [
      "urn:csabs:source/goldberg-floating-point-oracle"
    ],
    "sourceLocator": "Relative Error and Ulps, equation (2); The Details / Rounding Error",
    "sourceNote": "Uses u for the paper’s epsilon and makes the nonzero normal exact-result restriction explicit.",
    "provenanceKind": "adapted",
    "proofSketch": "In each exponent interval, nearest rounding changes the result by at most half a grid step. Divide this absolute bound by |z|≥β^e to obtain u. Zero is handled separately as an exact representable value."
  },
  {
    "id": "urn:csabs:law/fp-guard-not-correct-rounding",
    "type": "Law",
    "name": "one guard digit need not give correct rounding",
    "statement": "A local guarded error bound is weaker than exact-then-round semantics.",
    "formalStatement": "β=10,p=3: G(110,8.59)=102, while RN_3(110−8.59)=RN_3(101.41)=101.",
    "assumptions": [
      "One-guard-digit alignment/truncation algorithm of fp-guard-digit-error; nearest final rounding; adequate exponent range."
    ],
    "appliesTo": [
      "urn:csabs:concept/FloatingPointType"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/fp-radix-grid",
      "urn:csabs:axiom/fp-error-measures",
      "urn:csabs:theorem/fp-guard-digit-error"
    ],
    "proofSketch": "Alignment truncates 8.59 to 8.5 at the working scale; 110−8.5=101.5 rounds to 102, whereas the exact difference rounds to 101.",
    "source": [
      "urn:csabs:source/goldberg-floating-point-oracle"
    ],
    "sourceLocator": "Guard Digits, example immediately before Theorem 2; Exactly Rounded Operations",
    "sourceNote": "Preserves the paper’s concrete distinction between guarded and correctly rounded operations.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/fp-double-rounding-counterexample",
    "type": "Law",
    "name": "double rounding counterexample",
    "statement": "Rounding through a wider intermediate format can change the final target-format value.",
    "formalStatement": "RN_2(RN_3(12.51))=RN_2(12.5)=12 ≠ 13=RN_2(12.51), radix 10.",
    "assumptions": [
      "Decimal precision 3 then 2; nearest ties-to-even at both stages; exact real input 12.51 and adequate exponent ranges."
    ],
    "appliesTo": [
      "urn:csabs:concept/FloatingPointType"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/fp-radix-grid",
      "urn:csabs:axiom/FloatingPointType-rounding"
    ],
    "proofSketch": "The first rounding creates a target halfway case; the even last digit selects 12, although direct rounding selects 13.",
    "source": [
      "urn:csabs:source/goldberg-floating-point-oracle"
    ],
    "sourceLocator": "The Details / Binary to Decimal Conversion, double-rounding example",
    "sourceNote": "A decimal counterexample; no assertion that every widening conversion fails.",
    "provenanceKind": "adapted"
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
    "source": [
      "urn:csabs:source/goldberg-floating-point-oracle"
    ],
    "sourceLocator": "Exactly Rounded Operations; Rounding Modes",
    "sourceNote": "Immediate consequence of the nearest/directed rounding definitions; numeric equality only.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/fp-nearest-absolute-error",
    "type": "Theorem",
    "name": "nearest rounding absolute bound",
    "statement": "Nearest rounding has at most half the declared spacing of absolute error, including the gradual-underflow region.",
    "formalStatement": "|RN_F(z)−z|≤ulp_F(z)/2; if |z|<β^e_min then |RN_F(z)−z|≤q/2.",
    "assumptions": [
      "Finite exact z with |z|≤maxFinite; gradual underflow, nearest rounding and fp-ulp boundary convention."
    ],
    "appliesTo": [
      "urn:csabs:concept/FloatingPointType"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/fp-radix-grid",
      "urn:csabs:axiom/fp-error-measures",
      "urn:csabs:axiom/FloatingPointType-rounding",
      "urn:csabs:law/fp-rounding-model"
    ],
    "proofSketch": "Within an exponent interval adjacent grid points differ by ulp_F(z); nearest rounding is at most half that distance. The lower neighbor gap at an exponent boundary is smaller. Below the normal threshold the same argument uses the fixed step q.",
    "source": [
      "urn:csabs:source/goldberg-floating-point-oracle"
    ],
    "sourceLocator": "Relative Error and Ulps; Denormalized Numbers",
    "sourceNote": "Half-ulp nearest rounding extended to the uniform subnormal grid.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/fp-guard-digit-error",
    "type": "Theorem",
    "name": "one-guard-digit subtraction bound",
    "statement": "A specified guarded subtraction algorithm controls local error even during cancellation.",
    "formalStatement": "z=x−y≠0 ⇒ |G(x,y)−z|/|z|<2u.",
    "assumptions": [
      "Exactly known finite stored operands; align significands, truncate the shifted smaller magnitude to p+1 digits, subtract, then round to nearest p digits.",
      "Even radix β≥2, p≥2; unbounded exponents or all relevant nonzero values remain normal and finite. G is this algorithm, not a claim of correct rounding."
    ],
    "appliesTo": [
      "urn:csabs:concept/FloatingPointType"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/fp-radix-grid",
      "urn:csabs:axiom/fp-error-measures"
    ],
    "proofSketch": "Bound the discarded aligned tail and final nearest-rounding error as in Theorem 9; same-sign addition after sign reduction uses Theorem 10.",
    "source": [
      "urn:csabs:source/goldberg-floating-point-oracle"
    ],
    "sourceLocator": "Guard Digits, Theorem 2; The Details / Rounding Error, Theorems 9–10",
    "sourceNote": "States the algorithm and excludes exponent exceptions omitted in the idealized analysis.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:theorem/fp-sterbenz-exact-subtraction",
    "type": "Theorem",
    "name": "Sterbenz exact subtraction",
    "statement": "Nearby nonnegative stored floating-point numbers can be subtracted without numeric rounding error.",
    "formalStatement": "x,y∈F_fin, 0≤y/2≤x≤2y ⇒ sub_F(x,y)=x−y numerically.",
    "assumptions": [
      "One radix/precision for both operands; correctly rounded subtraction, or Goldberg’s one-guard-digit algorithm.",
      "Gradual underflow enabled, or the exact nonzero difference remains in the normal range; finite inputs and numeric real equality; signed-zero encoding governed separately."
    ],
    "appliesTo": [
      "urn:csabs:concept/FloatingPointType"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/fp-radix-grid",
      "urn:csabs:axiom/FloatingPointType-rounding",
      "urn:csabs:law/fp-rounding-model"
    ],
    "proofSketch": "Alignment requires at most one extra radix digit. The factor-two condition ensures cancellation leaves at most p significant digits, so the exact difference is representable. Gradual underflow preserves representability near zero; rounding then fixes it.",
    "source": [
      "urn:csabs:source/goldberg-floating-point-oracle"
    ],
    "sourceLocator": "The Details / Rounding Error, Theorem 11; Denormalized Numbers",
    "sourceNote": "Explicit nonnegative carriers and underflow conditions for the exact-subtraction lemma.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:theorem/fp-gradual-underflow-zero-difference",
    "type": "Theorem",
    "name": "zero difference detects equal finite values",
    "statement": "Gradual underflow preserves the zero-difference equality test on finite operands.",
    "formalStatement": "sub_F(x,y)==0 ⇔ val(x)=val(y).",
    "assumptions": [
      "Finite operands in the same radix grid, gradual underflow, correctly rounded subtraction in a nearest or directed mode.",
      "Default nontrapping results; numeric equality identifies signed zeros; no flush-to-zero or denormals-are-zero; overflow may yield an infinity, which is nonzero."
    ],
    "appliesTo": [
      "urn:csabs:concept/FloatingPointType"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/fp-radix-grid",
      "urn:csabs:axiom/FloatingPointType-rounding",
      "urn:csabs:law/fp-rounding-model"
    ],
    "proofSketch": "Every finite grid value is an integer multiple of q. Distinct inputs differ by at least q, so rounding cannot turn the difference into zero; equal numeric inputs have an exact zero difference.",
    "source": [
      "urn:csabs:source/goldberg-floating-point-oracle"
    ],
    "sourceLocator": "Denormalized Numbers, equation (10)",
    "sourceNote": "Excludes NaNs and infinities, for which the equivalence fails.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/fp-cancellation-input-error",
    "type": "Theorem",
    "name": "input-error amplification in subtraction",
    "statement": "Even an exact subtraction of stored operands may expose large errors relative to the intended inputs.",
    "formalStatement": "x̂=x+Δx, ŷ=y+Δy, x≠y ⇒ |(x̂−ŷ)−(x−y)|/|x−y|≤(|Δx|+|Δy|)/|x−y|. If |Δx|≤η|x| and |Δy|≤η|y|, the bound is η(|x|+|y|)/|x−y|.",
    "assumptions": [
      "Finite real inputs and perturbations; x≠y; this bound concerns input perturbation before any subtraction-rounding error."
    ],
    "appliesTo": [
      "urn:csabs:concept/FloatingPointType"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/fp-error-measures"
    ],
    "proofSketch": "Subtract the two exact differences to obtain Δx−Δy, apply the real triangle inequality, and divide by |x−y|. Substitute the individual perturbation bounds for the second inequality.",
    "source": [
      "urn:csabs:source/goldberg-floating-point-oracle"
    ],
    "sourceLocator": "Cancellation; The Details / Rounding Error, equations (19)–(23)",
    "sourceNote": "Derives a precise perturbation bound for the paper’s distinction between benign and catastrophic cancellation.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/fp-nearest-even-iteration",
    "type": "Theorem",
    "name": "nearest-even subtract-add stability",
    "statement": "With the cited idealized arithmetic, repeated subtraction and addition of the same value stabilizes after one iteration.",
    "formalStatement": "T(t)=RN(RN(t−y)+y); x_0=x; x_(n+1)=T(x_n) ⇒ ∀n≥1, x_n=x_1 (and possibly x_1=x).",
    "assumptions": [
      "Finite x,y in one even-radix precision-p grid; correctly rounded nearest ties-to-even after each operation.",
      "Unbounded-exponent model, or a finite execution whose intermediates never underflow or overflow; no excess precision or reassociation; numeric equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/FloatingPointType"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/fp-radix-grid",
      "urn:csabs:axiom/FloatingPointType-rounding"
    ],
    "proofSketch": "Use the cited Theorem 5: either every iterate equals x or every positive-index iterate equals x_1. Both cases imply T(T(x))=T(x); its nearest-even tie rule is essential. This is a citation of that result, not an independent formal proof.",
    "source": [
      "urn:csabs:source/goldberg-floating-point-oracle"
    ],
    "sourceLocator": "Exactly Rounded Operations, Theorem 5 (Reiser and Knuth)",
    "sourceNote": "Restricts the cited result to its ordinary finite, nonexceptional regime.",
    "provenanceKind": "adapted"
  }
]
```
<!-- graph-record:end -->
