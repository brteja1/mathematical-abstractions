# Fixed-width unsigned integer

A fixed-width unsigned integer with canonical values 0 through 2^w−1 and wrapping addition, subtraction and multiplication modulo 2^w.

**Notation:** U_w={0,…,2^w−1}; wrapping add(x,y)=(x+y) mod 2^w.

**Stable ID:** `urn:csabs:concept/FixedWidthUnsignedInteger`

**Categories:** Numeric computation, Programming-language semantics

**Kind:** Numeric data type

**Related concepts:** [Mathematical integers](Integer.md)

## Backlinks

- [Fixed-width bit vector](BitVector.md) — `relatedConcept`
- [Mathematical integers](Integer.md) — `relatedConcept`

## Mathematical formulation

For w>0, U\_w={0,…,2^w−1}. The selected BitVec interpretation uses (x+y) mod 2^w and (xy) mod 2^w. Equality is value equality at fixed width.

**Lean formulation** (in its source module context):

```lean
abbrev FixedWidthUnsignedInteger (width : Nat) (_ : 0 < width) := BitVec width
```

**Source:** [`Catalog.FixedWidthUnsignedInteger`](../lean/Catalog/Numeric.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Lean BitVec width with explicit positive-width proof; modulo 2^width arithmetic and unsigned natural quotient/remainder. Zero-divisor behavior of totalized library operations is outside catalog definedness.

**Limits:** Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Selected presentation: A w-bit unsigned numeric type whose values are residues represented by integers from zero through 2^w−1; arithmetic semantics must specify wrapping or another overflow policy. Governing rules: The carrier consists of exactly w-bit unsigned values with wrapping arithmetic modulo 2^w in this abstract model. This entry fixes wrapping semantics and canonical unsigned representatives. Unsigned quotient and remainder are natural division, not modular inverse.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**verificationObligation:** Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

**provenanceStatus:** legacy-source-missing

## Operations

<a id="node-urn-csabs-operation-unsigned-add"></a>

### wrapping addition

`urn:csabs:operation/unsigned-add`

**signature:** add : U_w×U_w→U_w; add(x,y)=(x+y) mod 2^w

**description:** Adds modulo the carrier size.

<a id="node-urn-csabs-operation-unsigned-subtract"></a>

### wrapping subtraction

`urn:csabs:operation/unsigned-subtract`

**signature:** sub : U_w×U_w→U_w; sub(x,y)=(x−y) mod 2^w

**description:** Subtracts modulo the carrier size.

<a id="node-urn-csabs-operation-unsigned-multiply"></a>

### wrapping multiplication

`urn:csabs:operation/unsigned-multiply`

**signature:** mul : U_w×U_w→U_w; mul(x,y)=xy mod 2^w

**description:** Multiplies modulo the carrier size.

<a id="node-urn-csabs-operation-unsigned-compare"></a>

### unsigned comparison

`urn:csabs:operation/unsigned-compare`

**signature:** <u : U_w×U_w→Bool

**description:** Compares the canonical representatives as natural numbers.

<a id="node-urn-csabs-operation-unsigned-shift"></a>

### logical left shift

`urn:csabs:operation/unsigned-shift`

**signature:** shl : U_w×ℕ→U_w; shl(x,k)=(x·2^k) mod 2^w

**description:** Mathematical total zero-filled shift, with result zero when k≥w. Programming-language shift-count rules require separate refinement.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-unsigned-width"></a>

### unsigned-width

`urn:csabs:axiom/unsigned-width`

**statement:** The carrier consists of exactly w-bit unsigned values with wrapping arithmetic modulo 2^w in this abstract model.

**formalStatement:** U_w={0,…,2^w−1}; arithmetic modulo 2^w

**assumptions:** w is a positive integer; wrapping semantics selected

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-FixedWidthUnsignedInteger-wrapping"></a>

### wrapping

`urn:csabs:axiom/FixedWidthUnsignedInteger-wrapping`

**statement:** This entry fixes wrapping semantics and canonical unsigned representatives.

**formalStatement:** w∈ℕ,w≥1; U_w={0,…,2^w−1}; x⊕y=(x+y) mod 2^w; x⊖y=(x−y) mod 2^w; x⊗y=xy mod 2^w

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-FixedWidthUnsignedInteger-division"></a>

### division

`urn:csabs:axiom/FixedWidthUnsignedInteger-division`

**statement:** Unsigned quotient and remainder are natural division, not modular inverse.

**formalStatement:** y≠0 ⇒ div(x,y)=⌊x/y⌋ and rem(x,y)=x−y·div(x,y)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

<a id="node-urn-csabs-law-unsigned-modular-arithmetic"></a>

### law/unsigned-modular-arithmetic

`urn:csabs:law/unsigned-modular-arithmetic`

**statement:** Unsigned addition and multiplication wrap modulo 2^w.

**formalStatement:** x⊕y=(x+y) mod 2^w; x⊗y=xy mod 2^w

**assumptions:** wrapping unsigned model

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [unsigned-width](FixedWidthUnsignedInteger.md#node-urn-csabs-axiom-unsigned-width); [wrapping](FixedWidthUnsignedInteger.md#node-urn-csabs-axiom-FixedWidthUnsignedInteger-wrapping); [division](FixedWidthUnsignedInteger.md#node-urn-csabs-axiom-FixedWidthUnsignedInteger-division)

**provenanceStatus:** legacy-source-missing

## Theorems

<a id="node-urn-csabs-theorem-FixedWidthUnsignedInteger-modular-increment-inverse"></a>

### modular-increment-inverse

`urn:csabs:theorem/FixedWidthUnsignedInteger-modular-increment-inverse`

**statement:** Subtracting one undoes a wrapping increment.

**formalStatement:** (x⊕1)⊖1=x for w≥1

**proofSketch:** Congruence modulo 2^w yields x; canonical representatives in the carrier are unique.

**assumptions:** The explicit basis, carriers, and side conditions stated for FixedWidthUnsignedInteger apply.

**dependsOn:** [unsigned-width](FixedWidthUnsignedInteger.md#node-urn-csabs-axiom-unsigned-width); [wrapping](FixedWidthUnsignedInteger.md#node-urn-csabs-axiom-FixedWidthUnsignedInteger-wrapping); [division](FixedWidthUnsignedInteger.md#node-urn-csabs-axiom-FixedWidthUnsignedInteger-division)

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
    "id": "urn:csabs:concept/FixedWidthUnsignedInteger",
    "type": "Concept",
    "shortForm": "FixedWidthUnsignedInteger",
    "fullName": "Fixed-width unsigned integer",
    "category": [
      "urn:csabs:category/numeric-computation",
      "urn:csabs:category/programming-semantics"
    ],
    "kind": "urn:csabs:kind/data-type",
    "definition": "A fixed-width unsigned integer with canonical values 0 through 2^w−1 and wrapping addition, subtraction and multiplication modulo 2^w.",
    "notation": "U_w={0,…,2^w−1}; wrapping add(x,y)=(x+y) mod 2^w.",
    "hasOperation": [
      "urn:csabs:operation/unsigned-add",
      "urn:csabs:operation/unsigned-subtract",
      "urn:csabs:operation/unsigned-multiply",
      "urn:csabs:operation/unsigned-compare",
      "urn:csabs:operation/unsigned-shift"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/unsigned-width",
      "urn:csabs:axiom/FixedWidthUnsignedInteger-wrapping",
      "urn:csabs:axiom/FixedWidthUnsignedInteger-division"
    ],
    "hasLaw": [
      "urn:csabs:law/unsigned-modular-arithmetic"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/FixedWidthUnsignedInteger-modular-increment-inverse"
    ],
    "relatedConcept": [
      "urn:csabs:concept/MathematicalInteger"
    ],
    "coverageStatus": "basis-reviewed",
    "requiresConcept": [],
    "verificationObligation": [
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: A w-bit unsigned numeric type whose values are residues represented by integers from zero through 2^w−1; arithmetic semantics must specify wrapping or another overflow policy. Governing rules: The carrier consists of exactly w-bit unsigned values with wrapping arithmetic modulo 2^w in this abstract model. This entry fixes wrapping semantics and canonical unsigned representatives. Unsigned quotient and remainder are natural division, not modular inverse.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "provenanceStatus": "legacy-source-missing",
    "leanFormulation": "abbrev FixedWidthUnsignedInteger (width : Nat) (_ : 0 < width) := BitVec width",
    "formulationSource": "urn:csabs:source/local-lean-Numeric",
    "formulationLocator": "Catalog.FixedWidthUnsignedInteger",
    "formulationScope": "model",
    "leanModelMapping": "Lean BitVec width with explicit positive-width proof; modulo 2^width arithmetic and unsigned natural quotient/remainder. Zero-divisor behavior of totalized library operations is outside catalog definedness.",
    "leanModelLimitations": "Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.",
    "mathematicalFormulation": "For w>0, U_w={0,…,2^w−1}. The selected BitVec interpretation uses (x+y) mod 2^w and (xy) mod 2^w. Equality is value equality at fixed width."
  },
  {
    "id": "urn:csabs:operation/unsigned-add",
    "type": "Operation",
    "name": "wrapping addition",
    "signature": "add : U_w×U_w→U_w; add(x,y)=(x+y) mod 2^w",
    "description": "Adds modulo the carrier size.",
    "concept": "urn:csabs:concept/FixedWidthUnsignedInteger"
  },
  {
    "id": "urn:csabs:operation/unsigned-subtract",
    "type": "Operation",
    "name": "wrapping subtraction",
    "signature": "sub : U_w×U_w→U_w; sub(x,y)=(x−y) mod 2^w",
    "description": "Subtracts modulo the carrier size.",
    "concept": "urn:csabs:concept/FixedWidthUnsignedInteger"
  },
  {
    "id": "urn:csabs:operation/unsigned-multiply",
    "type": "Operation",
    "name": "wrapping multiplication",
    "signature": "mul : U_w×U_w→U_w; mul(x,y)=xy mod 2^w",
    "description": "Multiplies modulo the carrier size.",
    "concept": "urn:csabs:concept/FixedWidthUnsignedInteger"
  },
  {
    "id": "urn:csabs:operation/unsigned-compare",
    "type": "Operation",
    "name": "unsigned comparison",
    "signature": "<u : U_w×U_w→Bool",
    "description": "Compares the canonical representatives as natural numbers.",
    "concept": "urn:csabs:concept/FixedWidthUnsignedInteger"
  },
  {
    "id": "urn:csabs:operation/unsigned-shift",
    "type": "Operation",
    "name": "logical left shift",
    "signature": "shl : U_w×ℕ→U_w; shl(x,k)=(x·2^k) mod 2^w",
    "description": "Mathematical total zero-filled shift, with result zero when k≥w. Programming-language shift-count rules require separate refinement.",
    "concept": "urn:csabs:concept/FixedWidthUnsignedInteger"
  },
  {
    "id": "urn:csabs:axiom/unsigned-width",
    "type": "Axiom",
    "statement": "The carrier consists of exactly w-bit unsigned values with wrapping arithmetic modulo 2^w in this abstract model.",
    "formalStatement": "U_w={0,…,2^w−1}; arithmetic modulo 2^w",
    "assumptions": [
      "w is a positive integer",
      "wrapping semantics selected"
    ],
    "appliesTo": [
      "urn:csabs:concept/FixedWidthUnsignedInteger"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law",
    "name": "unsigned-width",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/FixedWidthUnsignedInteger-wrapping",
    "type": "Axiom",
    "name": "wrapping",
    "statement": "This entry fixes wrapping semantics and canonical unsigned representatives.",
    "formalStatement": "w∈ℕ,w≥1; U_w={0,…,2^w−1}; x⊕y=(x+y) mod 2^w; x⊖y=(x−y) mod 2^w; x⊗y=xy mod 2^w",
    "appliesTo": [
      "urn:csabs:concept/FixedWidthUnsignedInteger"
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
    "id": "urn:csabs:axiom/FixedWidthUnsignedInteger-division",
    "type": "Axiom",
    "name": "division",
    "statement": "Unsigned quotient and remainder are natural division, not modular inverse.",
    "formalStatement": "y≠0 ⇒ div(x,y)=⌊x/y⌋ and rem(x,y)=x−y·div(x,y)",
    "appliesTo": [
      "urn:csabs:concept/FixedWidthUnsignedInteger"
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
    "id": "urn:csabs:law/unsigned-modular-arithmetic",
    "type": "Law",
    "statement": "Unsigned addition and multiplication wrap modulo 2^w.",
    "formalStatement": "x⊕y=(x+y) mod 2^w; x⊗y=xy mod 2^w",
    "assumptions": [
      "wrapping unsigned model"
    ],
    "appliesTo": [
      "urn:csabs:concept/FixedWidthUnsignedInteger"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/unsigned-width",
      "urn:csabs:axiom/FixedWidthUnsignedInteger-wrapping",
      "urn:csabs:axiom/FixedWidthUnsignedInteger-division"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/FixedWidthUnsignedInteger-modular-increment-inverse",
    "type": "Theorem",
    "name": "modular-increment-inverse",
    "statement": "Subtracting one undoes a wrapping increment.",
    "formalStatement": "(x⊕1)⊖1=x for w≥1",
    "proofSketch": "Congruence modulo 2^w yields x; canonical representatives in the carrier are unique.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for FixedWidthUnsignedInteger apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/FixedWidthUnsignedInteger"
    ],
    "dependsOn": [
      "urn:csabs:axiom/unsigned-width",
      "urn:csabs:axiom/FixedWidthUnsignedInteger-wrapping",
      "urn:csabs:axiom/FixedWidthUnsignedInteger-division"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
