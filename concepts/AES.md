# Advanced Encryption Standard (AES)

The three standardized Rijndael permutations with 128-bit blocks and 128-, 192- or 256-bit keys, defined by FIPS 197.

**Notation:** AES_ℓ : {0,1}^ℓ×B_128 → B_128; ℓ∈{128,192,256}.

**Stable ID:** `urn:csabs:concept/AES`

**Categories:** Cryptography → Symmetric cryptography

**Kind:** Mathematical structure

**Prerequisites:** [Keyed block cipher](BlockCipher.md), [Finite field (Galois field)](FiniteField.md)

**Specializes:** [Keyed block cipher](BlockCipher.md)

## Backlinks

- [AES-GCM (96-bit nonce, 128-bit tag profile)](AESGCM.md) — `requiresConcept`

## Interface and scope

**axiomBasis:** FIPS 197 key expansion and forward/inverse round algorithms; fixed parameters and state encoding.

**basisKind:** defined-structure

**basisScope:** Fix ℓ per instance. Exact bytes and column-major state s[r,c]=input[r+4c]. Key sizes do not change the 128-bit block size. Empty or partial blocks are invalid; no padding or mode is implicit. Byte field arithmetic uses GF(2)[u]/(u^8+u^4+u^3+u+1).

**specializationNote:** For each ℓ set K={0,1}^ℓ and n=128; instantiate E and D with CIPHER and INVCIPHER using KEYEXPANSION. The AES defining rules are recorded directly.

**verificationObligation:** Map byte and bit order, exact lengths, equality, errors and key handling explicitly. Functional equations alone do not establish computational security or resistance to side channels.

**reviewStatus:** Editorial specification; no cryptographic security proof or compiled claim witness.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-AES-encrypt"></a>

### encrypt

`urn:csabs:operation/AES-encrypt`

**signature:** AES_ℓ : B_ℓ×B_128 → B_128

**description:** Encrypt exactly one block.

**precondition:** ℓ∈{128,192,256}; typed key and block.

**postcondition:** CIPHER(x,Nr,KEYEXPANSION(k)), Nr=10,12,14 respectively.

**totality:** total on the stated precondition; outside the domain return an input error without partial output

**source:** [NIST FIPS 197-upd1: Advanced Encryption Standard (2023 editorial update)](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197-upd1.pdf); accessedOn: 2026-11-10; sourceRole: primary normative specification

**sourceLocator:** Sections 3.4, 4 and 5; Table 3; Algorithms 1–3

**sourceNote:** Algorithm names refer to the exact normative transformations and key schedule, not arbitrary invertible rounds.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-AES-decrypt"></a>

### decrypt

`urn:csabs:operation/AES-decrypt`

**signature:** AESinv_ℓ : B_ℓ×B_128 → B_128

**description:** Invert one AES block.

**precondition:** Same selected ℓ and key encoding as encryption.

**postcondition:** INVCIPHER(y,Nr,KEYEXPANSION(k)).

**totality:** total on the stated precondition; outside the domain return an input error without partial output

**source:** [NIST FIPS 197-upd1: Advanced Encryption Standard (2023 editorial update)](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197-upd1.pdf); accessedOn: 2026-11-10; sourceRole: primary normative specification

**sourceLocator:** Sections 3.4, 4 and 5; Table 3; Algorithms 1–3

**sourceNote:** Algorithm names refer to the exact normative transformations and key schedule, not arbitrary invertible rounds.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-AES-round-definition"></a>

### round-definition

`urn:csabs:axiom/AES-round-definition`

**statement:** AES is the specified round computation with its specified key expansion.

**formalStatement:** Nr=(10,12,14) for ℓ=(128,192,256); w=KEYEXPANSION(k); s=AddRoundKey(input,w[0..3]); for r=1..Nr−1: s=AddRoundKey(MixColumns(ShiftRows(SubBytes(s))),w[4r..4r+3]); output=AddRoundKey(ShiftRows(SubBytes(s)),w[4Nr..4Nr+3]); inverse uses Algorithm 3. SubBytes, ShiftRows, MixColumns, AddRoundKey and KEYEXPANSION are exactly FIPS 197 §§5.1–5.3, including SBOX Table 4.

**assumptions:** Fix ℓ per instance. Exact bytes and column-major state s[r,c]=input[r+4c]. Key sizes do not change the 128-bit block size. Empty or partial blocks are invalid; no padding or mode is implicit. Byte field arithmetic uses GF(2)[u]/(u^8+u^4+u^3+u+1).

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial mathematics; not a machine-checked proof.

**source:** [NIST FIPS 197-upd1: Advanced Encryption Standard (2023 editorial update)](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197-upd1.pdf); accessedOn: 2026-11-10; sourceRole: primary normative specification

**sourceLocator:** Sections 3.4, 4 and 5; Table 3; Algorithms 1–3

**sourceNote:** Algorithm names refer to the exact normative transformations and key schedule, not arbitrary invertible rounds.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-AES-inverse"></a>

### inverse

`urn:csabs:law/AES-inverse`

**statement:** The AES inverse recovers a block under the same key.

**formalStatement:** AESinv_ℓ(k,AES_ℓ(k,x))=x ∧ AES_ℓ(k,AESinv_ℓ(k,y))=y.

**assumptions:** Fix ℓ per instance. Exact bytes and column-major state s[r,c]=input[r+4c]. Key sizes do not change the 128-bit block size. Empty or partial blocks are invalid; no padding or mode is implicit. Byte field arithmetic uses GF(2)[u]/(u^8+u^4+u^3+u+1).

**ruleRole:** derived-result

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial mathematics; not a machine-checked proof.

**source:** [NIST FIPS 197-upd1: Advanced Encryption Standard (2023 editorial update)](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197-upd1.pdf); accessedOn: 2026-11-10; sourceRole: primary normative specification

**sourceLocator:** Sections 3.4, 4 and 5; Table 3; Algorithms 1–3

**sourceNote:** Editorial derivation from the linked premises. Algorithm names refer to the exact normative transformations and key schedule, not arbitrary invertible rounds.

**provenanceKind:** derived

**dependsOn:** [round-definition](AES.md#node-urn-csabs-axiom-AES-round-definition)

**proofSketch:** SubBytes and ShiftRows have specified inverses, MixColumns has its specified inverse matrix, and AddRoundKey is self-inverse. Reverse the composed steps with identical round keys.

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [NIST FIPS 197-upd1: Advanced Encryption Standard (2023 editorial update)](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197-upd1.pdf); accessedOn: 2026-11-10; sourceRole: primary normative specification

**sourceLocator:** Sections 3.4, 4 and 5; Table 3; Algorithms 1–3

**sourceNote:** Algorithm names refer to the exact normative transformations and key schedule, not arbitrary invertible rounds.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/AES",
    "type": "Concept",
    "shortForm": "AES",
    "fullName": "Advanced Encryption Standard (AES)",
    "definition": "The three standardized Rijndael permutations with 128-bit blocks and 128-, 192- or 256-bit keys, defined by FIPS 197.",
    "notation": "AES_ℓ : {0,1}^ℓ×B_128 → B_128; ℓ∈{128,192,256}.",
    "category": [
      "urn:csabs:category/symmetric-cryptography"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "requiresConcept": [
      "urn:csabs:concept/BlockCipher",
      "urn:csabs:concept/FiniteField"
    ],
    "axiomBasis": "FIPS 197 key expansion and forward/inverse round algorithms; fixed parameters and state encoding.",
    "basisKind": "defined-structure",
    "basisScope": "Fix ℓ per instance. Exact bytes and column-major state s[r,c]=input[r+4c]. Key sizes do not change the 128-bit block size. Empty or partial blocks are invalid; no padding or mode is implicit. Byte field arithmetic uses GF(2)[u]/(u^8+u^4+u^3+u+1).",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial specification; no cryptographic security proof or compiled claim witness.",
    "verificationObligation": [
      "Map byte and bit order, exact lengths, equality, errors and key handling explicitly. Functional equations alone do not establish computational security or resistance to side channels."
    ],
    "hasOperation": [
      "urn:csabs:operation/AES-encrypt",
      "urn:csabs:operation/AES-decrypt"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/AES-round-definition"
    ],
    "hasLaw": [
      "urn:csabs:law/AES-inverse"
    ],
    "hasTheorem": [],
    "source": [
      "urn:csabs:source/nist-fips197-upd1"
    ],
    "sourceLocator": "Sections 3.4, 4 and 5; Table 3; Algorithms 1–3",
    "sourceNote": "Algorithm names refer to the exact normative transformations and key schedule, not arbitrary invertible rounds.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/BlockCipher"
    ],
    "specializationNote": "For each ℓ set K={0,1}^ℓ and n=128; instantiate E and D with CIPHER and INVCIPHER using KEYEXPANSION. The AES defining rules are recorded directly."
  },
  {
    "id": "urn:csabs:operation/AES-encrypt",
    "type": "Operation",
    "name": "encrypt",
    "signature": "AES_ℓ : B_ℓ×B_128 → B_128",
    "description": "Encrypt exactly one block.",
    "precondition": "ℓ∈{128,192,256}; typed key and block.",
    "postcondition": "CIPHER(x,Nr,KEYEXPANSION(k)), Nr=10,12,14 respectively.",
    "totality": "total on the stated precondition; outside the domain return an input error without partial output",
    "concept": "urn:csabs:concept/AES",
    "source": [
      "urn:csabs:source/nist-fips197-upd1"
    ],
    "sourceLocator": "Sections 3.4, 4 and 5; Table 3; Algorithms 1–3",
    "sourceNote": "Algorithm names refer to the exact normative transformations and key schedule, not arbitrary invertible rounds.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/AES-decrypt",
    "type": "Operation",
    "name": "decrypt",
    "signature": "AESinv_ℓ : B_ℓ×B_128 → B_128",
    "description": "Invert one AES block.",
    "precondition": "Same selected ℓ and key encoding as encryption.",
    "postcondition": "INVCIPHER(y,Nr,KEYEXPANSION(k)).",
    "totality": "total on the stated precondition; outside the domain return an input error without partial output",
    "concept": "urn:csabs:concept/AES",
    "source": [
      "urn:csabs:source/nist-fips197-upd1"
    ],
    "sourceLocator": "Sections 3.4, 4 and 5; Table 3; Algorithms 1–3",
    "sourceNote": "Algorithm names refer to the exact normative transformations and key schedule, not arbitrary invertible rounds.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/AES-round-definition",
    "type": "Axiom",
    "name": "round-definition",
    "statement": "AES is the specified round computation with its specified key expansion.",
    "formalStatement": "Nr=(10,12,14) for ℓ=(128,192,256); w=KEYEXPANSION(k); s=AddRoundKey(input,w[0..3]); for r=1..Nr−1: s=AddRoundKey(MixColumns(ShiftRows(SubBytes(s))),w[4r..4r+3]); output=AddRoundKey(ShiftRows(SubBytes(s)),w[4Nr..4Nr+3]); inverse uses Algorithm 3. SubBytes, ShiftRows, MixColumns, AddRoundKey and KEYEXPANSION are exactly FIPS 197 §§5.1–5.3, including SBOX Table 4.",
    "assumptions": [
      "Fix ℓ per instance. Exact bytes and column-major state s[r,c]=input[r+4c]. Key sizes do not change the 128-bit block size. Empty or partial blocks are invalid; no padding or mode is implicit. Byte field arithmetic uses GF(2)[u]/(u^8+u^4+u^3+u+1)."
    ],
    "appliesTo": [
      "urn:csabs:concept/AES"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial mathematics; not a machine-checked proof.",
    "source": [
      "urn:csabs:source/nist-fips197-upd1"
    ],
    "sourceLocator": "Sections 3.4, 4 and 5; Table 3; Algorithms 1–3",
    "sourceNote": "Algorithm names refer to the exact normative transformations and key schedule, not arbitrary invertible rounds.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/AES-inverse",
    "type": "Law",
    "name": "inverse",
    "statement": "The AES inverse recovers a block under the same key.",
    "formalStatement": "AESinv_ℓ(k,AES_ℓ(k,x))=x ∧ AES_ℓ(k,AESinv_ℓ(k,y))=y.",
    "assumptions": [
      "Fix ℓ per instance. Exact bytes and column-major state s[r,c]=input[r+4c]. Key sizes do not change the 128-bit block size. Empty or partial blocks are invalid; no padding or mode is implicit. Byte field arithmetic uses GF(2)[u]/(u^8+u^4+u^3+u+1)."
    ],
    "appliesTo": [
      "urn:csabs:concept/AES"
    ],
    "ruleRole": "derived-result",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial mathematics; not a machine-checked proof.",
    "source": [
      "urn:csabs:source/nist-fips197-upd1"
    ],
    "sourceLocator": "Sections 3.4, 4 and 5; Table 3; Algorithms 1–3",
    "sourceNote": "Editorial derivation from the linked premises. Algorithm names refer to the exact normative transformations and key schedule, not arbitrary invertible rounds.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/AES-round-definition"
    ],
    "proofSketch": "SubBytes and ShiftRows have specified inverses, MixColumns has its specified inverse matrix, and AddRoundKey is self-inverse. Reverse the composed steps with identical round keys."
  }
]
```
<!-- graph-record:end -->
