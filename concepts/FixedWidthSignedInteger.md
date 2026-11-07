# Fixed-width signed integer

A bounded signed integer with two’s-complement value range, modeled here by exact partial operations whose results must fit. Wrapping, trapping, and saturating variants need separate policies.

**Notation:** Common two's-complement range S_w={−2^{w−1},…,2^{w−1}−1}; overflow behavior is a parameter, not implied by representation.

**Stable ID:** `urn:csabs:concept/FixedWidthSignedInteger`

**Categories:** Numeric computation, Programming-language semantics

**Kind:** Numeric data type

**Related concepts:** [Mathematical integers](Integer.md)

## Backlinks

- [Fixed-width bit vector](BitVector.md) — `relatedConcept`
- [Mathematical integers](Integer.md) — `relatedConcept`

## Interface and scope

**axiomBasis:** Selected presentation: A bounded signed integer type with a specified value range and language-defined overflow, conversion, and representation semantics. Governing rules: The carrier range and overflow behavior are fixed by a width and a named arithmetic policy. The selected model has two's-complement range and exact arithmetic only when representable, leaving overflow undefined in the abstract partial operation. Signed division truncates toward zero when its exact integer quotient is in range.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**convention:** Do not assume signed overflow wraps; bind an entry to a named language/version for executable semantics.

**verificationObligation:** Prove each intermediate exact result fits, or bind a named overflow policy.; Account for promotions, narrowing, divide-by-zero, and the minimum-value divided by minus one.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

**provenanceStatus:** legacy-source-missing

## Operations

<a id="node-urn-csabs-operation-signed-add"></a>

### signed addition

`urn:csabs:operation/signed-add`

**signature:** add : S_w×S_w ⇀ S_w (exact, in-range model); other overflow policies require a variant

**description:** Adds values under a separately selected overflow policy.

**precondition:** The exact result is in S_w; otherwise behavior must be supplied by a named language/policy.

<a id="node-urn-csabs-operation-signed-subtract"></a>

### signed subtraction

`urn:csabs:operation/signed-subtract`

**signature:** subtract : S_w×S_w ⇀ S_w (exact, in-range model); other overflow policies require a variant

**description:** Subtracts values under a separately selected overflow policy.

**precondition:** The exact result is in S_w; otherwise behavior must be supplied by a named language/policy.

<a id="node-urn-csabs-operation-signed-multiply"></a>

### signed multiplication

`urn:csabs:operation/signed-multiply`

**signature:** multiply : S_w×S_w ⇀ S_w (exact, in-range model); other overflow policies require a variant

**description:** Multiplies values under a separately selected overflow policy.

**precondition:** The exact result is in S_w; otherwise behavior must be supplied by a named language/policy.

<a id="node-urn-csabs-operation-signed-divide"></a>

### signed division

`urn:csabs:operation/signed-divide`

**signature:** div : S_w×S_w⇀S_w

**description:** Division with language-specific rounding and exceptional cases.

**precondition:** divisor nonzero and exceptional quotient case excluded or specified

## Axioms and defining rules

<a id="node-urn-csabs-axiom-signed-width"></a>

### signed-width

`urn:csabs:axiom/signed-width`

**statement:** The carrier range and overflow behavior are fixed by a width and a named arithmetic policy.

**assumptions:** width w; encoding and overflow policy explicitly selected

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

**formalStatement:** The carrier range and overflow behavior are fixed by a width and a named arithmetic policy.

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-FixedWidthSignedInteger-exact-partial-model"></a>

### exact-partial-model

`urn:csabs:axiom/FixedWidthSignedInteger-exact-partial-model`

**statement:** The selected model has two's-complement range and exact arithmetic only when representable, leaving overflow undefined in the abstract partial operation.

**formalStatement:** w≥1; S_w={−2^(w−1),…,2^(w−1)−1}; op(x,y)=op_ℤ(x,y) iff op_ℤ(x,y)∈S_w, op∈{+,−,×}

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-FixedWidthSignedInteger-division"></a>

### division

`urn:csabs:axiom/FixedWidthSignedInteger-division`

**statement:** Signed division truncates toward zero when its exact integer quotient is in range.

**formalStatement:** div(x,y)=trunc(x/y); defined iff y≠0 and not(x=−2^(w−1) and y=−1)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-FixedWidthSignedInteger-exact-add-commutativity"></a>

### exact-add-commutativity

`urn:csabs:theorem/FixedWidthSignedInteger-exact-add-commutativity`

**statement:** In-range exact addition is symmetric in its inputs, including definedness.

**formalStatement:** add(x,y) defined iff add(y,x) defined; when defined add(x,y)=add(y,x)

**proofSketch:** The exact integer sums agree and therefore satisfy the same range predicate.

**assumptions:** The explicit basis, carriers, and side conditions stated for FixedWidthSignedInteger apply.

**dependsOn:** [signed-width](FixedWidthSignedInteger.md#node-urn-csabs-axiom-signed-width); [exact-partial-model](FixedWidthSignedInteger.md#node-urn-csabs-axiom-FixedWidthSignedInteger-exact-partial-model); [division](FixedWidthSignedInteger.md#node-urn-csabs-axiom-FixedWidthSignedInteger-division)

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
    "id": "urn:csabs:concept/FixedWidthSignedInteger",
    "type": "Concept",
    "shortForm": "FixedWidthSignedInteger",
    "fullName": "Fixed-width signed integer",
    "category": [
      "urn:csabs:category/numeric-computation",
      "urn:csabs:category/programming-semantics"
    ],
    "kind": "urn:csabs:kind/data-type",
    "definition": "A bounded signed integer with two’s-complement value range, modeled here by exact partial operations whose results must fit. Wrapping, trapping, and saturating variants need separate policies.",
    "notation": "Common two's-complement range S_w={−2^{w−1},…,2^{w−1}−1}; overflow behavior is a parameter, not implied by representation.",
    "hasOperation": [
      "urn:csabs:operation/signed-add",
      "urn:csabs:operation/signed-subtract",
      "urn:csabs:operation/signed-multiply",
      "urn:csabs:operation/signed-divide"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/signed-width",
      "urn:csabs:axiom/FixedWidthSignedInteger-exact-partial-model",
      "urn:csabs:axiom/FixedWidthSignedInteger-division"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/FixedWidthSignedInteger-exact-add-commutativity"
    ],
    "relatedConcept": [
      "urn:csabs:concept/MathematicalInteger"
    ],
    "convention": "Do not assume signed overflow wraps; bind an entry to a named language/version for executable semantics.",
    "coverageStatus": "basis-reviewed",
    "requiresConcept": [],
    "verificationObligation": [
      "Prove each intermediate exact result fits, or bind a named overflow policy.",
      "Account for promotions, narrowing, divide-by-zero, and the minimum-value divided by minus one.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: A bounded signed integer type with a specified value range and language-defined overflow, conversion, and representation semantics. Governing rules: The carrier range and overflow behavior are fixed by a width and a named arithmetic policy. The selected model has two's-complement range and exact arithmetic only when representable, leaving overflow undefined in the abstract partial operation. Signed division truncates toward zero when its exact integer quotient is in range.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:operation/signed-add",
    "type": "Operation",
    "name": "signed addition",
    "signature": "add : S_w×S_w ⇀ S_w (exact, in-range model); other overflow policies require a variant",
    "description": "Adds values under a separately selected overflow policy.",
    "concept": "urn:csabs:concept/FixedWidthSignedInteger",
    "precondition": "The exact result is in S_w; otherwise behavior must be supplied by a named language/policy."
  },
  {
    "id": "urn:csabs:operation/signed-subtract",
    "type": "Operation",
    "name": "signed subtraction",
    "signature": "subtract : S_w×S_w ⇀ S_w (exact, in-range model); other overflow policies require a variant",
    "description": "Subtracts values under a separately selected overflow policy.",
    "concept": "urn:csabs:concept/FixedWidthSignedInteger",
    "precondition": "The exact result is in S_w; otherwise behavior must be supplied by a named language/policy."
  },
  {
    "id": "urn:csabs:operation/signed-multiply",
    "type": "Operation",
    "name": "signed multiplication",
    "signature": "multiply : S_w×S_w ⇀ S_w (exact, in-range model); other overflow policies require a variant",
    "description": "Multiplies values under a separately selected overflow policy.",
    "concept": "urn:csabs:concept/FixedWidthSignedInteger",
    "precondition": "The exact result is in S_w; otherwise behavior must be supplied by a named language/policy."
  },
  {
    "id": "urn:csabs:operation/signed-divide",
    "type": "Operation",
    "name": "signed division",
    "signature": "div : S_w×S_w⇀S_w",
    "description": "Division with language-specific rounding and exceptional cases.",
    "precondition": "divisor nonzero and exceptional quotient case excluded or specified",
    "concept": "urn:csabs:concept/FixedWidthSignedInteger"
  },
  {
    "id": "urn:csabs:axiom/signed-width",
    "type": "Axiom",
    "statement": "The carrier range and overflow behavior are fixed by a width and a named arithmetic policy.",
    "assumptions": [
      "width w",
      "encoding and overflow policy explicitly selected"
    ],
    "appliesTo": [
      "urn:csabs:concept/FixedWidthSignedInteger"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law",
    "name": "signed-width",
    "formalStatement": "The carrier range and overflow behavior are fixed by a width and a named arithmetic policy.",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/FixedWidthSignedInteger-exact-partial-model",
    "type": "Axiom",
    "name": "exact-partial-model",
    "statement": "The selected model has two's-complement range and exact arithmetic only when representable, leaving overflow undefined in the abstract partial operation.",
    "formalStatement": "w≥1; S_w={−2^(w−1),…,2^(w−1)−1}; op(x,y)=op_ℤ(x,y) iff op_ℤ(x,y)∈S_w, op∈{+,−,×}",
    "appliesTo": [
      "urn:csabs:concept/FixedWidthSignedInteger"
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
    "id": "urn:csabs:axiom/FixedWidthSignedInteger-division",
    "type": "Axiom",
    "name": "division",
    "statement": "Signed division truncates toward zero when its exact integer quotient is in range.",
    "formalStatement": "div(x,y)=trunc(x/y); defined iff y≠0 and not(x=−2^(w−1) and y=−1)",
    "appliesTo": [
      "urn:csabs:concept/FixedWidthSignedInteger"
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
    "id": "urn:csabs:theorem/FixedWidthSignedInteger-exact-add-commutativity",
    "type": "Theorem",
    "name": "exact-add-commutativity",
    "statement": "In-range exact addition is symmetric in its inputs, including definedness.",
    "formalStatement": "add(x,y) defined iff add(y,x) defined; when defined add(x,y)=add(y,x)",
    "proofSketch": "The exact integer sums agree and therefore satisfy the same range predicate.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for FixedWidthSignedInteger apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/FixedWidthSignedInteger"
    ],
    "dependsOn": [
      "urn:csabs:axiom/signed-width",
      "urn:csabs:axiom/FixedWidthSignedInteger-exact-partial-model",
      "urn:csabs:axiom/FixedWidthSignedInteger-division"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
