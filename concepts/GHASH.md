# GHASH polynomial accumulator

The keyed polynomial accumulation over 128-bit blocks used inside GCM, with a fixed binary-field encoding.

**Notation:** GHASH_H(X₁∥…∥X_m)=Y_m; Y₀=0; Y_i=(Y_{i−1}⊕X_i)·H.

**Stable ID:** `urn:csabs:concept/GHASH`

**Categories:** Cryptography → Symmetric cryptography

**Kind:** Function

**Prerequisites:** [Finite field (Galois field)](FiniteField.md), [Fixed-width bit vector](BitVector.md), [Finite sequence (List datatype)](Sequence.md)

## Backlinks

- [Galois/Counter Mode (96-bit IV, 128-bit tag profile)](GCM.md) — `requiresConcept`

## Mathematical formulation

The partial interface stores H∈{0,1}^{128} and a supplied multiply:B×B→B. For a nonempty block list X₁,…,X\_m, Y₀=0 and Y\_i=multiply(Y\_{i−1} XOR X\_i,H). Correspondence of multiply to the NIST binary-field product is not encoded.

**Lean formulation** (in its source module context):

```lean
structure GHASHInterface where
  subkey : CryptoBits 128
  multiply : CryptoBits 128 → CryptoBits 128 → CryptoBits 128
```

**Source:** [`Catalog.GHASHInterface`](../lean/Catalog/Cryptography.lean); consulted 2026-11-12.

**Scope:** partial

**Interpretation:** 128-bit subkey, parameterized multiplication, and XOR Horner fold over an explicit head plus tail (nonempty sequence).

**Limits:** Multiplication has no field-law or polynomial-encoding constraint. No verified NIST multiplication, polynomial theorem or security bound.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Explicit field multiplication encoding and Horner recurrence.

**basisKind:** defined-structure

**basisScope:** H and each X_i are B_128; m≥1. The empty block sequence is outside this selected NIST Algorithm 2 domain. Zero H is permitted algebraically. Exact bit equality. Left-to-right bits b₀…b₁₂₇ encode Σ b_i u^i, so field one is 1∥0^127, not the rightmost-bit integer one. Reduction polynomial is u^128+u^7+u^2+u+1. No integer overflow or rounding.

**verificationObligation:** Map byte and bit order, exact lengths, equality, errors and key handling explicitly. Functional equations alone do not establish computational security or resistance to side channels.

**reviewStatus:** Editorial specification; no cryptographic security proof or compiled claim witness.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-GHASH-multiply"></a>

### multiply

`urn:csabs:operation/GHASH-multiply`

**signature:** mul : B_128×B_128 → B_128

**description:** Multiply encoded field elements.

**precondition:** Two exactly 128-bit strings with the specified coefficient order.

**postcondition:** Encode polynomial product reduced modulo u^128+u^7+u^2+u+1.

**totality:** total on the stated precondition; outside the domain return an input error without partial output

**source:** [NIST SP 800-38D: Galois/Counter Mode (GCM) and GMAC (2007)](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf); accessedOn: 2026-11-10; sourceRole: primary normative specification

**sourceLocator:** Sections 6.3–6.4, Algorithms 1–2

**sourceNote:** Separates GHASH from the complete GCM authentication encoding. GHASH itself is neither an unkeyed cryptographic hash nor a standalone authenticated-encryption scheme.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-GHASH-accumulate"></a>

### accumulate

`urn:csabs:operation/GHASH-accumulate`

**signature:** GHASH : B_128×(B_128)^+ → B_128

**description:** Accumulate a nonempty block sequence.

**precondition:** H∈B_128; m≥1 whole input blocks.

**postcondition:** Return Y_m from the defining recurrence; no implicit padding or length blocks.

**totality:** total on the stated precondition; outside the domain return an input error without partial output

**source:** [NIST SP 800-38D: Galois/Counter Mode (GCM) and GMAC (2007)](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf); accessedOn: 2026-11-10; sourceRole: primary normative specification

**sourceLocator:** Sections 6.3–6.4, Algorithms 1–2

**sourceNote:** Separates GHASH from the complete GCM authentication encoding. GHASH itself is neither an unkeyed cryptographic hash nor a standalone authenticated-encryption scheme.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-GHASH-field-encoding"></a>

### field-encoding

`urn:csabs:axiom/GHASH-field-encoding`

**statement:** Multiplication uses the specified binary polynomial field.

**formalStatement:** φ(b₀…b₁₂₇)=Σᵢ₌₀¹²⁷ b_i u^i; φ(X⊕Y)=φ(X)+φ(Y); φ(X·Y)=φ(X)φ(Y) mod (u^128+u^7+u^2+u+1).

**assumptions:** H and each X_i are B_128; m≥1. The empty block sequence is outside this selected NIST Algorithm 2 domain. Zero H is permitted algebraically. Exact bit equality. Left-to-right bits b₀…b₁₂₇ encode Σ b_i u^i, so field one is 1∥0^127, not the rightmost-bit integer one. Reduction polynomial is u^128+u^7+u^2+u+1. No integer overflow or rounding.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial mathematics; not a machine-checked proof.

**source:** [NIST SP 800-38D: Galois/Counter Mode (GCM) and GMAC (2007)](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf); accessedOn: 2026-11-10; sourceRole: primary normative specification

**sourceLocator:** Sections 6.3–6.4, Algorithms 1–2

**sourceNote:** Separates GHASH from the complete GCM authentication encoding. GHASH itself is neither an unkeyed cryptographic hash nor a standalone authenticated-encryption scheme.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-GHASH-recurrence"></a>

### recurrence

`urn:csabs:axiom/GHASH-recurrence`

**statement:** The accumulator starts at zero and folds blocks in order.

**formalStatement:** Y₀=0^128; Y_i=(Y_{i−1}⊕X_i)·H (1≤i≤m); GHASH_H(X₁∥…∥X_m)=Y_m.

**assumptions:** H and each X_i are B_128; m≥1. The empty block sequence is outside this selected NIST Algorithm 2 domain. Zero H is permitted algebraically. Exact bit equality. Left-to-right bits b₀…b₁₂₇ encode Σ b_i u^i, so field one is 1∥0^127, not the rightmost-bit integer one. Reduction polynomial is u^128+u^7+u^2+u+1. No integer overflow or rounding.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial mathematics; not a machine-checked proof.

**source:** [NIST SP 800-38D: Galois/Counter Mode (GCM) and GMAC (2007)](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf); accessedOn: 2026-11-10; sourceRole: primary normative specification

**sourceLocator:** Sections 6.3–6.4, Algorithms 1–2

**sourceNote:** Separates GHASH from the complete GCM authentication encoding. GHASH itself is neither an unkeyed cryptographic hash nor a standalone authenticated-encryption scheme.

**provenanceKind:** adapted

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-GHASH-polynomial"></a>

### polynomial

`urn:csabs:theorem/GHASH-polynomial`

**statement:** GHASH equals a polynomial in the hash subkey.

**formalStatement:** GHASH_H(X₁∥…∥X_m)=⊕ᵢ₌₁ᵐ X_i·H^(m−i+1).

**assumptions:** H and each X_i are B_128; m≥1. The empty block sequence is outside this selected NIST Algorithm 2 domain. Zero H is permitted algebraically. Exact bit equality. Left-to-right bits b₀…b₁₂₇ encode Σ b_i u^i, so field one is 1∥0^127, not the rightmost-bit integer one. Reduction polynomial is u^128+u^7+u^2+u+1. No integer overflow or rounding.

**ruleRole:** derived-result

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial mathematics; not a machine-checked proof.

**source:** [NIST SP 800-38D: Galois/Counter Mode (GCM) and GMAC (2007)](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf); accessedOn: 2026-11-10; sourceRole: primary normative specification

**sourceLocator:** Sections 6.3–6.4, Algorithms 1–2

**sourceNote:** Editorial derivation from the linked premises. Separates GHASH from the complete GCM authentication encoding. GHASH itself is neither an unkeyed cryptographic hash nor a standalone authenticated-encryption scheme.

**provenanceKind:** derived

**dependsOn:** [field-encoding](GHASH.md#node-urn-csabs-axiom-GHASH-field-encoding); [recurrence](GHASH.md#node-urn-csabs-axiom-GHASH-recurrence)

**proofSketch:** Induct on m. The one-block recurrence gives X₁H. Multiply the previous polynomial by H and add X_mH, using field distributivity.

## Concept provenance

- [NIST SP 800-38D: Galois/Counter Mode (GCM) and GMAC (2007)](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf); accessedOn: 2026-11-10; sourceRole: primary normative specification

**sourceLocator:** Sections 6.3–6.4, Algorithms 1–2

**sourceNote:** Separates GHASH from the complete GCM authentication encoding. GHASH itself is neither an unkeyed cryptographic hash nor a standalone authenticated-encryption scheme.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/GHASH",
    "type": "Concept",
    "shortForm": "GHASH",
    "fullName": "GHASH polynomial accumulator",
    "definition": "The keyed polynomial accumulation over 128-bit blocks used inside GCM, with a fixed binary-field encoding.",
    "notation": "GHASH_H(X₁∥…∥X_m)=Y_m; Y₀=0; Y_i=(Y_{i−1}⊕X_i)·H.",
    "category": [
      "urn:csabs:category/symmetric-cryptography"
    ],
    "kind": "urn:csabs:kind/function",
    "requiresConcept": [
      "urn:csabs:concept/FiniteField",
      "urn:csabs:concept/BitVector",
      "urn:csabs:concept/Sequence"
    ],
    "axiomBasis": "Explicit field multiplication encoding and Horner recurrence.",
    "basisKind": "defined-structure",
    "basisScope": "H and each X_i are B_128; m≥1. The empty block sequence is outside this selected NIST Algorithm 2 domain. Zero H is permitted algebraically. Exact bit equality. Left-to-right bits b₀…b₁₂₇ encode Σ b_i u^i, so field one is 1∥0^127, not the rightmost-bit integer one. Reduction polynomial is u^128+u^7+u^2+u+1. No integer overflow or rounding.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial specification; no cryptographic security proof or compiled claim witness.",
    "verificationObligation": [
      "Map byte and bit order, exact lengths, equality, errors and key handling explicitly. Functional equations alone do not establish computational security or resistance to side channels."
    ],
    "hasOperation": [
      "urn:csabs:operation/GHASH-multiply",
      "urn:csabs:operation/GHASH-accumulate"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/GHASH-field-encoding",
      "urn:csabs:axiom/GHASH-recurrence"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/GHASH-polynomial"
    ],
    "source": [
      "urn:csabs:source/nist-sp800-38d"
    ],
    "sourceLocator": "Sections 6.3–6.4, Algorithms 1–2",
    "sourceNote": "Separates GHASH from the complete GCM authentication encoding. GHASH itself is neither an unkeyed cryptographic hash nor a standalone authenticated-encryption scheme.",
    "provenanceKind": "adapted",
    "leanFormulation": "structure GHASHInterface where\n  subkey : CryptoBits 128\n  multiply : CryptoBits 128 → CryptoBits 128 → CryptoBits 128",
    "formulationSource": "urn:csabs:source/local-lean-Cryptography",
    "formulationLocator": "Catalog.GHASHInterface",
    "formulationScope": "partial",
    "leanModelMapping": "128-bit subkey, parameterized multiplication, and XOR Horner fold over an explicit head plus tail (nonempty sequence).",
    "leanModelLimitations": "Multiplication has no field-law or polynomial-encoding constraint. No verified NIST multiplication, polynomial theorem or security bound.",
    "mathematicalFormulation": "The partial interface stores H∈{0,1}^{128} and a supplied multiply:B×B→B. For a nonempty block list X₁,…,X_m, Y₀=0 and Y_i=multiply(Y_{i−1} XOR X_i,H). Correspondence of multiply to the NIST binary-field product is not encoded."
  },
  {
    "id": "urn:csabs:operation/GHASH-multiply",
    "type": "Operation",
    "name": "multiply",
    "signature": "mul : B_128×B_128 → B_128",
    "description": "Multiply encoded field elements.",
    "precondition": "Two exactly 128-bit strings with the specified coefficient order.",
    "postcondition": "Encode polynomial product reduced modulo u^128+u^7+u^2+u+1.",
    "totality": "total on the stated precondition; outside the domain return an input error without partial output",
    "concept": "urn:csabs:concept/GHASH",
    "source": [
      "urn:csabs:source/nist-sp800-38d"
    ],
    "sourceLocator": "Sections 6.3–6.4, Algorithms 1–2",
    "sourceNote": "Separates GHASH from the complete GCM authentication encoding. GHASH itself is neither an unkeyed cryptographic hash nor a standalone authenticated-encryption scheme.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/GHASH-accumulate",
    "type": "Operation",
    "name": "accumulate",
    "signature": "GHASH : B_128×(B_128)^+ → B_128",
    "description": "Accumulate a nonempty block sequence.",
    "precondition": "H∈B_128; m≥1 whole input blocks.",
    "postcondition": "Return Y_m from the defining recurrence; no implicit padding or length blocks.",
    "totality": "total on the stated precondition; outside the domain return an input error without partial output",
    "concept": "urn:csabs:concept/GHASH",
    "source": [
      "urn:csabs:source/nist-sp800-38d"
    ],
    "sourceLocator": "Sections 6.3–6.4, Algorithms 1–2",
    "sourceNote": "Separates GHASH from the complete GCM authentication encoding. GHASH itself is neither an unkeyed cryptographic hash nor a standalone authenticated-encryption scheme.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/GHASH-field-encoding",
    "type": "Axiom",
    "name": "field-encoding",
    "statement": "Multiplication uses the specified binary polynomial field.",
    "formalStatement": "φ(b₀…b₁₂₇)=Σᵢ₌₀¹²⁷ b_i u^i; φ(X⊕Y)=φ(X)+φ(Y); φ(X·Y)=φ(X)φ(Y) mod (u^128+u^7+u^2+u+1).",
    "assumptions": [
      "H and each X_i are B_128; m≥1. The empty block sequence is outside this selected NIST Algorithm 2 domain. Zero H is permitted algebraically. Exact bit equality. Left-to-right bits b₀…b₁₂₇ encode Σ b_i u^i, so field one is 1∥0^127, not the rightmost-bit integer one. Reduction polynomial is u^128+u^7+u^2+u+1. No integer overflow or rounding."
    ],
    "appliesTo": [
      "urn:csabs:concept/GHASH"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial mathematics; not a machine-checked proof.",
    "source": [
      "urn:csabs:source/nist-sp800-38d"
    ],
    "sourceLocator": "Sections 6.3–6.4, Algorithms 1–2",
    "sourceNote": "Separates GHASH from the complete GCM authentication encoding. GHASH itself is neither an unkeyed cryptographic hash nor a standalone authenticated-encryption scheme.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/GHASH-recurrence",
    "type": "Axiom",
    "name": "recurrence",
    "statement": "The accumulator starts at zero and folds blocks in order.",
    "formalStatement": "Y₀=0^128; Y_i=(Y_{i−1}⊕X_i)·H (1≤i≤m); GHASH_H(X₁∥…∥X_m)=Y_m.",
    "assumptions": [
      "H and each X_i are B_128; m≥1. The empty block sequence is outside this selected NIST Algorithm 2 domain. Zero H is permitted algebraically. Exact bit equality. Left-to-right bits b₀…b₁₂₇ encode Σ b_i u^i, so field one is 1∥0^127, not the rightmost-bit integer one. Reduction polynomial is u^128+u^7+u^2+u+1. No integer overflow or rounding."
    ],
    "appliesTo": [
      "urn:csabs:concept/GHASH"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial mathematics; not a machine-checked proof.",
    "source": [
      "urn:csabs:source/nist-sp800-38d"
    ],
    "sourceLocator": "Sections 6.3–6.4, Algorithms 1–2",
    "sourceNote": "Separates GHASH from the complete GCM authentication encoding. GHASH itself is neither an unkeyed cryptographic hash nor a standalone authenticated-encryption scheme.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:theorem/GHASH-polynomial",
    "type": "Theorem",
    "name": "polynomial",
    "statement": "GHASH equals a polynomial in the hash subkey.",
    "formalStatement": "GHASH_H(X₁∥…∥X_m)=⊕ᵢ₌₁ᵐ X_i·H^(m−i+1).",
    "assumptions": [
      "H and each X_i are B_128; m≥1. The empty block sequence is outside this selected NIST Algorithm 2 domain. Zero H is permitted algebraically. Exact bit equality. Left-to-right bits b₀…b₁₂₇ encode Σ b_i u^i, so field one is 1∥0^127, not the rightmost-bit integer one. Reduction polynomial is u^128+u^7+u^2+u+1. No integer overflow or rounding."
    ],
    "appliesTo": [
      "urn:csabs:concept/GHASH"
    ],
    "ruleRole": "derived-result",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial mathematics; not a machine-checked proof.",
    "source": [
      "urn:csabs:source/nist-sp800-38d"
    ],
    "sourceLocator": "Sections 6.3–6.4, Algorithms 1–2",
    "sourceNote": "Editorial derivation from the linked premises. Separates GHASH from the complete GCM authentication encoding. GHASH itself is neither an unkeyed cryptographic hash nor a standalone authenticated-encryption scheme.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/GHASH-field-encoding",
      "urn:csabs:axiom/GHASH-recurrence"
    ],
    "proofSketch": "Induct on m. The one-block recurrence gives X₁H. Multiply the previous polynomial by H and add X_mH, using field distributivity."
  }
]
```
<!-- graph-record:end -->
