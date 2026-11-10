# Fixed-width bit vector

A sequence of exactly w bits, with bitwise operations and optional signed or unsigned interpretations for arithmetic and comparison.

**Notation:** BV_w={0,1}^w; concat, extract, and bitwise operators are defined over bit positions.

**Stable ID:** `urn:csabs:concept/BitVector`

**Categories:** Numeric computation, Programming-language semantics

**Kind:** Numeric data type

**Related concepts:** [Fixed-width unsigned integer](FixedWidthUnsignedInteger.md), [Fixed-width signed integer](FixedWidthSignedInteger.md)

## Backlinks

- [Keyed block cipher](BlockCipher.md) — `requiresConcept`
- [GHASH polynomial accumulator](GHASH.md) — `requiresConcept`

## Interface and scope

**axiomBasis:** Selected presentation: A sequence of exactly w bits, with bitwise operations and optional signed or unsigned interpretations for arithmetic and comparison. Governing rules: Every value contains exactly w bits. Bit vectors are fixed-length maps into two bit values. Bitwise Boolean operations are defined independently at every index. Logical shifts use zero fill and return zero for counts at least the width; this convention is not a programming-language shift rule.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**verificationObligation:** Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

**provenanceStatus:** legacy-source-missing

## Operations

<a id="node-urn-csabs-operation-bitvector-and"></a>

### bitwise and

`urn:csabs:operation/bitvector-and`

**signature:** ∧ᵦ : BV_w×BV_w→BV_w

**description:** Computes conjunction independently at each bit position.

<a id="node-urn-csabs-operation-bitvector-or"></a>

### bitwise or

`urn:csabs:operation/bitvector-or`

**signature:** ∨ᵦ : BV_w×BV_w→BV_w

**description:** Computes disjunction independently at each bit position.

<a id="node-urn-csabs-operation-bitvector-xor"></a>

### bitwise xor

`urn:csabs:operation/bitvector-xor`

**signature:** ⊕ᵦ : BV_w×BV_w→BV_w

**description:** Computes exclusive-or independently at each bit position.

<a id="node-urn-csabs-operation-bitvector-not"></a>

### bitwise complement

`urn:csabs:operation/bitvector-not`

**signature:** ¬ᵦ : BV_w→BV_w

**description:** Flips every bit in the fixed-width vector.

<a id="node-urn-csabs-operation-bitvector-shift"></a>

### logical left shift

`urn:csabs:operation/bitvector-shift`

**signature:** shl : BV_w×ℕ→BV_w

**description:** Zero-filled logical left shift; for count at least w the result is the zero vector. Bit index zero is least significant.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-bitvector-width"></a>

### bitvector-width

`urn:csabs:axiom/bitvector-width`

**statement:** Every value contains exactly w bits.

**formalStatement:** BV_w={0,1}^w

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

**assumptions:** Use the linked concept’s explicit basis and carrier conventions.

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-BitVector-extensionality"></a>

### extensionality

`urn:csabs:axiom/BitVector-extensionality`

**statement:** Bit vectors are fixed-length maps into two bit values.

**formalStatement:** BV_w={b:Index(w)→{0,1}}; b=c iff ∀i<w:b(i)=c(i)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-BitVector-boolean-operations"></a>

### boolean-operations

`urn:csabs:axiom/BitVector-boolean-operations`

**statement:** Bitwise Boolean operations are defined independently at every index.

**formalStatement:** (x AND y)(i)=x(i)∧y(i); (x OR y)(i)=x(i)∨y(i); (x XOR y)(i)=x(i)⊕y(i); (NOT x)(i)=1−x(i)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-BitVector-logical-shifts"></a>

### logical-shifts

`urn:csabs:axiom/BitVector-logical-shifts`

**statement:** Logical shifts use zero fill and return zero for counts at least the width; this convention is not a programming-language shift rule.

**formalStatement:** shl(b,k)(i)=b(i−k) if k≤i<w else 0; lshr(b,k)(i)=b(i+k) if i+k<w else 0; k∈ℕ, index 0 is least significant

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-BitVector-xor-self"></a>

### xor-self

`urn:csabs:theorem/BitVector-xor-self`

**statement:** A vector XOR itself is the zero vector.

**formalStatement:** b XOR b=0_w

**proofSketch:** Each bit XOR itself is zero; conclude vector equality by extensionality.

**assumptions:** The explicit basis, carriers, and side conditions stated for BitVector apply.

**dependsOn:** [bitvector-width](BitVector.md#node-urn-csabs-axiom-bitvector-width); [extensionality](BitVector.md#node-urn-csabs-axiom-BitVector-extensionality); [boolean-operations](BitVector.md#node-urn-csabs-axiom-BitVector-boolean-operations); [logical-shifts](BitVector.md#node-urn-csabs-axiom-BitVector-logical-shifts)

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
    "id": "urn:csabs:concept/BitVector",
    "type": "Concept",
    "shortForm": "BitVector",
    "fullName": "Fixed-width bit vector",
    "category": [
      "urn:csabs:category/numeric-computation",
      "urn:csabs:category/programming-semantics"
    ],
    "kind": "urn:csabs:kind/data-type",
    "definition": "A sequence of exactly w bits, with bitwise operations and optional signed or unsigned interpretations for arithmetic and comparison.",
    "notation": "BV_w={0,1}^w; concat, extract, and bitwise operators are defined over bit positions.",
    "hasOperation": [
      "urn:csabs:operation/bitvector-and",
      "urn:csabs:operation/bitvector-or",
      "urn:csabs:operation/bitvector-xor",
      "urn:csabs:operation/bitvector-not",
      "urn:csabs:operation/bitvector-shift"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/bitvector-width",
      "urn:csabs:axiom/BitVector-extensionality",
      "urn:csabs:axiom/BitVector-boolean-operations",
      "urn:csabs:axiom/BitVector-logical-shifts"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/BitVector-xor-self"
    ],
    "relatedConcept": [
      "urn:csabs:concept/FixedWidthUnsignedInteger",
      "urn:csabs:concept/FixedWidthSignedInteger"
    ],
    "coverageStatus": "basis-reviewed",
    "requiresConcept": [],
    "verificationObligation": [
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: A sequence of exactly w bits, with bitwise operations and optional signed or unsigned interpretations for arithmetic and comparison. Governing rules: Every value contains exactly w bits. Bit vectors are fixed-length maps into two bit values. Bitwise Boolean operations are defined independently at every index. Logical shifts use zero fill and return zero for counts at least the width; this convention is not a programming-language shift rule.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:operation/bitvector-and",
    "type": "Operation",
    "name": "bitwise and",
    "signature": "∧ᵦ : BV_w×BV_w→BV_w",
    "description": "Computes conjunction independently at each bit position.",
    "concept": "urn:csabs:concept/BitVector"
  },
  {
    "id": "urn:csabs:operation/bitvector-or",
    "type": "Operation",
    "name": "bitwise or",
    "signature": "∨ᵦ : BV_w×BV_w→BV_w",
    "description": "Computes disjunction independently at each bit position.",
    "concept": "urn:csabs:concept/BitVector"
  },
  {
    "id": "urn:csabs:operation/bitvector-xor",
    "type": "Operation",
    "name": "bitwise xor",
    "signature": "⊕ᵦ : BV_w×BV_w→BV_w",
    "description": "Computes exclusive-or independently at each bit position.",
    "concept": "urn:csabs:concept/BitVector"
  },
  {
    "id": "urn:csabs:operation/bitvector-not",
    "type": "Operation",
    "name": "bitwise complement",
    "signature": "¬ᵦ : BV_w→BV_w",
    "description": "Flips every bit in the fixed-width vector.",
    "concept": "urn:csabs:concept/BitVector"
  },
  {
    "id": "urn:csabs:operation/bitvector-shift",
    "type": "Operation",
    "name": "logical left shift",
    "signature": "shl : BV_w×ℕ→BV_w",
    "description": "Zero-filled logical left shift; for count at least w the result is the zero vector. Bit index zero is least significant.",
    "concept": "urn:csabs:concept/BitVector"
  },
  {
    "id": "urn:csabs:axiom/bitvector-width",
    "type": "Axiom",
    "statement": "Every value contains exactly w bits.",
    "formalStatement": "BV_w={0,1}^w",
    "appliesTo": [
      "urn:csabs:concept/BitVector"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law",
    "name": "bitvector-width",
    "assumptions": [
      "Use the linked concept’s explicit basis and carrier conventions."
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/BitVector-extensionality",
    "type": "Axiom",
    "name": "extensionality",
    "statement": "Bit vectors are fixed-length maps into two bit values.",
    "formalStatement": "BV_w={b:Index(w)→{0,1}}; b=c iff ∀i<w:b(i)=c(i)",
    "appliesTo": [
      "urn:csabs:concept/BitVector"
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
    "id": "urn:csabs:axiom/BitVector-boolean-operations",
    "type": "Axiom",
    "name": "boolean-operations",
    "statement": "Bitwise Boolean operations are defined independently at every index.",
    "formalStatement": "(x AND y)(i)=x(i)∧y(i); (x OR y)(i)=x(i)∨y(i); (x XOR y)(i)=x(i)⊕y(i); (NOT x)(i)=1−x(i)",
    "appliesTo": [
      "urn:csabs:concept/BitVector"
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
    "id": "urn:csabs:axiom/BitVector-logical-shifts",
    "type": "Axiom",
    "name": "logical-shifts",
    "statement": "Logical shifts use zero fill and return zero for counts at least the width; this convention is not a programming-language shift rule.",
    "formalStatement": "shl(b,k)(i)=b(i−k) if k≤i<w else 0; lshr(b,k)(i)=b(i+k) if i+k<w else 0; k∈ℕ, index 0 is least significant",
    "appliesTo": [
      "urn:csabs:concept/BitVector"
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
    "id": "urn:csabs:theorem/BitVector-xor-self",
    "type": "Theorem",
    "name": "xor-self",
    "statement": "A vector XOR itself is the zero vector.",
    "formalStatement": "b XOR b=0_w",
    "proofSketch": "Each bit XOR itself is zero; conclude vector equality by extensionality.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for BitVector apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/BitVector"
    ],
    "dependsOn": [
      "urn:csabs:axiom/bitvector-width",
      "urn:csabs:axiom/BitVector-extensionality",
      "urn:csabs:axiom/BitVector-boolean-operations",
      "urn:csabs:axiom/BitVector-logical-shifts"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
