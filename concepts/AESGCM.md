# AES-GCM (96-bit nonce, 128-bit tag profile)

The selected GCM profile instantiated with AES-128, AES-192 or AES-256, with explicit detached and combined wire encodings.

**Notation:** AESGCM_ℓ=GCM_{AES_ℓ}; ℓ∈{128,192,256}; combined output W=C∥T.

**Stable ID:** `urn:csabs:concept/AESGCM`

**Categories:** Cryptography → Symmetric cryptography

**Kind:** Mathematical construction

**Prerequisites:** [Advanced Encryption Standard (AES)](AES.md), [Galois/Counter Mode (96-bit IV, 128-bit tag profile)](GCM.md)

**Specializes:** [Galois/Counter Mode (96-bit IV, 128-bit tag profile)](GCM.md)

## Interface and scope

**axiomBasis:** Explicit AES instantiation of the GCM equations and unambiguous fixed-length trailing tag encoding.

**basisKind:** defined-structure

**basisScope:** Selected byte-oriented 96-bit-IV, 128-bit-tag profile of SP 800-38D. Underlying block cipher E has 128-bit blocks. K is its key carrier; IV is exactly 12 bytes; 0≤|P|≤2^36−32 bytes and 0≤|A|≤2^61−1 bytes. Ciphertext has |P| bytes, tag has 16 bytes. len denotes bits in equations; |·| denotes bytes. Empty P and A are valid. Equality is exact bit strings; [x]_s is unsigned big-endian encoding, while GHASH has its own polynomial coefficient order. Other IV/tag lengths require explicit variants. No padding is added to the returned plaintext or ciphertext. Fix AES key length ℓ per instance. This entry uses the NIST plaintext ceiling 2^36−32 bytes; it does not adopt RFC 5116’s one-byte-larger listed P_MAX.

**specializationNote:** Set the underlying keyed block permutation E_k to the exact AES_ℓ(k,−), with ℓ=128,192 or 256. Preserve IV, AAD, plaintext, length encoding, counter order and tag equations. AES is a component prerequisite, not a parent of this authenticated-encryption construction.

**verificationObligation:** Map byte and bit order, exact lengths, equality, errors and key handling explicitly. Functional equations alone do not establish computational security or resistance to side channels.

**reviewStatus:** Editorial specification; no cryptographic security proof or compiled claim witness.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-AESGCM-seal"></a>

### seal

`urn:csabs:operation/AESGCM-seal`

**signature:** seal_ℓ : B_ℓ×B_96×A×P → C×B_128

**description:** Use AES in the selected GCM profile.

**precondition:** ℓ∈{128,192,256}, typed key and profile lengths; fresh nonce for secure use.

**postcondition:** GCM_{AES_ℓ}.seal(k,IV,A,P).

**totality:** total on the stated precondition; outside the domain return an input error without partial output

**source:** [NIST FIPS 197-upd1: Advanced Encryption Standard (2023 editorial update)](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197-upd1.pdf); accessedOn: 2026-11-10; sourceRole: primary normative specification; [NIST SP 800-38D: Galois/Counter Mode (GCM) and GMAC (2007)](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf); accessedOn: 2026-11-10; sourceRole: primary normative specification; [RFC 5116: An Interface and Algorithms for Authenticated Encryption](https://www.rfc-editor.org/rfc/rfc5116.html); accessedOn: 2026-11-10; sourceRole: primary normative specification

**sourceLocator:** FIPS 197 §5/Table 3; SP 800-38D §§5–7; RFC 5116 §§5.1–5.2

**sourceNote:** Covers all three NIST AES key sizes. RFC AEAD_AES_128_GCM and AEAD_AES_256_GCM identify the 128/256-bit instances; no RFC 5116 registry identity is asserted for AES-192. Uses the stricter NIST message limit.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-AESGCM-open"></a>

### open

`urn:csabs:operation/AESGCM-open`

**signature:** open_ℓ : B_ℓ×B_96×A×C×B_128 → P⊎{FAIL}

**description:** Authenticate and decrypt with the same selected AES key size.

**precondition:** Exact profile lengths and tag; invalid inputs yield an error or FAIL without plaintext.

**postcondition:** GCM_{AES_ℓ}.open(k,IV,A,C,T).

**totality:** total on the stated precondition; outside the domain return an input error without partial output

**source:** [NIST FIPS 197-upd1: Advanced Encryption Standard (2023 editorial update)](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197-upd1.pdf); accessedOn: 2026-11-10; sourceRole: primary normative specification; [NIST SP 800-38D: Galois/Counter Mode (GCM) and GMAC (2007)](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf); accessedOn: 2026-11-10; sourceRole: primary normative specification; [RFC 5116: An Interface and Algorithms for Authenticated Encryption](https://www.rfc-editor.org/rfc/rfc5116.html); accessedOn: 2026-11-10; sourceRole: primary normative specification

**sourceLocator:** FIPS 197 §5/Table 3; SP 800-38D §§5–7; RFC 5116 §§5.1–5.2

**sourceNote:** Covers all three NIST AES key sizes. RFC AEAD_AES_128_GCM and AEAD_AES_256_GCM identify the 128/256-bit instances; no RFC 5116 registry identity is asserted for AES-192. Uses the stricter NIST message limit.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-AESGCM-pack"></a>

### pack

`urn:csabs:operation/AESGCM-pack`

**signature:** pack : C×B_128 → W

**description:** Append the detached tag to ciphertext.

**precondition:** C meets the selected plaintext byte limit; tag has exactly 16 bytes.

**postcondition:** W=C∥T; |W|=|C|+16 bytes.

**totality:** total on the stated precondition; outside the domain return an input error without partial output

**source:** [NIST FIPS 197-upd1: Advanced Encryption Standard (2023 editorial update)](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197-upd1.pdf); accessedOn: 2026-11-10; sourceRole: primary normative specification; [NIST SP 800-38D: Galois/Counter Mode (GCM) and GMAC (2007)](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf); accessedOn: 2026-11-10; sourceRole: primary normative specification; [RFC 5116: An Interface and Algorithms for Authenticated Encryption](https://www.rfc-editor.org/rfc/rfc5116.html); accessedOn: 2026-11-10; sourceRole: primary normative specification

**sourceLocator:** FIPS 197 §5/Table 3; SP 800-38D §§5–7; RFC 5116 §§5.1–5.2

**sourceNote:** Covers all three NIST AES key sizes. RFC AEAD_AES_128_GCM and AEAD_AES_256_GCM identify the 128/256-bit instances; no RFC 5116 registry identity is asserted for AES-192. Uses the stricter NIST message limit.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-AESGCM-unpack"></a>

### unpack

`urn:csabs:operation/AESGCM-unpack`

**signature:** unpack : W ⇀ C×B_128

**description:** Split off the final 16 bytes as the tag.

**precondition:** 16≤|W|≤2^36−16 bytes.

**postcondition:** C is all but the last 16 bytes; T is the last 16 bytes. A 16-byte W represents empty ciphertext with a tag; shorter input is rejected.

**totality:** total on the stated precondition; outside the domain return an input error without partial output

**source:** [NIST FIPS 197-upd1: Advanced Encryption Standard (2023 editorial update)](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197-upd1.pdf); accessedOn: 2026-11-10; sourceRole: primary normative specification; [NIST SP 800-38D: Galois/Counter Mode (GCM) and GMAC (2007)](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf); accessedOn: 2026-11-10; sourceRole: primary normative specification; [RFC 5116: An Interface and Algorithms for Authenticated Encryption](https://www.rfc-editor.org/rfc/rfc5116.html); accessedOn: 2026-11-10; sourceRole: primary normative specification

**sourceLocator:** FIPS 197 §5/Table 3; SP 800-38D §§5–7; RFC 5116 §§5.1–5.2

**sourceNote:** Covers all three NIST AES key sizes. RFC AEAD_AES_128_GCM and AEAD_AES_256_GCM identify the 128/256-bit instances; no RFC 5116 registry identity is asserted for AES-192. Uses the stricter NIST message limit.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-AESGCM-instantiation"></a>

### instantiation

`urn:csabs:axiom/AESGCM-instantiation`

**statement:** AES-GCM fixes the GCM primitive to the selected AES permutation.

**formalStatement:** E_k(x)=AES_ℓ(k,x); seal_ℓ=GCM_{AES_ℓ}.seal; open_ℓ=GCM_{AES_ℓ}.open; ℓ∈{128,192,256}.

**assumptions:** Selected byte-oriented 96-bit-IV, 128-bit-tag profile of SP 800-38D. Underlying block cipher E has 128-bit blocks. K is its key carrier; IV is exactly 12 bytes; 0≤|P|≤2^36−32 bytes and 0≤|A|≤2^61−1 bytes. Ciphertext has |P| bytes, tag has 16 bytes. len denotes bits in equations; |·| denotes bytes. Empty P and A are valid. Equality is exact bit strings; [x]_s is unsigned big-endian encoding, while GHASH has its own polynomial coefficient order. Other IV/tag lengths require explicit variants. No padding is added to the returned plaintext or ciphertext. Fix AES key length ℓ per instance. This entry uses the NIST plaintext ceiling 2^36−32 bytes; it does not adopt RFC 5116’s one-byte-larger listed P_MAX.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial mathematics; not a machine-checked proof.

**source:** [NIST FIPS 197-upd1: Advanced Encryption Standard (2023 editorial update)](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197-upd1.pdf); accessedOn: 2026-11-10; sourceRole: primary normative specification; [NIST SP 800-38D: Galois/Counter Mode (GCM) and GMAC (2007)](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf); accessedOn: 2026-11-10; sourceRole: primary normative specification; [RFC 5116: An Interface and Algorithms for Authenticated Encryption](https://www.rfc-editor.org/rfc/rfc5116.html); accessedOn: 2026-11-10; sourceRole: primary normative specification

**sourceLocator:** FIPS 197 §5/Table 3; SP 800-38D §§5–7; RFC 5116 §§5.1–5.2

**sourceNote:** Covers all three NIST AES key sizes. RFC AEAD_AES_128_GCM and AEAD_AES_256_GCM identify the 128/256-bit instances; no RFC 5116 registry identity is asserted for AES-192. Uses the stricter NIST message limit.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-AESGCM-combined-encoding"></a>

### combined-encoding

`urn:csabs:axiom/AESGCM-combined-encoding`

**statement:** Combined output contains ciphertext followed by a full tag.

**formalStatement:** pack(C,T)=C∥T; unpack(W)=(prefix_(|W|−16)(W),suffix_16(W)); |pack(C,T)|=|C|+16 bytes; |W|<16 is invalid.

**assumptions:** Selected byte-oriented 96-bit-IV, 128-bit-tag profile of SP 800-38D. Underlying block cipher E has 128-bit blocks. K is its key carrier; IV is exactly 12 bytes; 0≤|P|≤2^36−32 bytes and 0≤|A|≤2^61−1 bytes. Ciphertext has |P| bytes, tag has 16 bytes. len denotes bits in equations; |·| denotes bytes. Empty P and A are valid. Equality is exact bit strings; [x]_s is unsigned big-endian encoding, while GHASH has its own polynomial coefficient order. Other IV/tag lengths require explicit variants. No padding is added to the returned plaintext or ciphertext. Fix AES key length ℓ per instance. This entry uses the NIST plaintext ceiling 2^36−32 bytes; it does not adopt RFC 5116’s one-byte-larger listed P_MAX.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial mathematics; not a machine-checked proof.

**source:** [NIST FIPS 197-upd1: Advanced Encryption Standard (2023 editorial update)](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197-upd1.pdf); accessedOn: 2026-11-10; sourceRole: primary normative specification; [NIST SP 800-38D: Galois/Counter Mode (GCM) and GMAC (2007)](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf); accessedOn: 2026-11-10; sourceRole: primary normative specification; [RFC 5116: An Interface and Algorithms for Authenticated Encryption](https://www.rfc-editor.org/rfc/rfc5116.html); accessedOn: 2026-11-10; sourceRole: primary normative specification

**sourceLocator:** FIPS 197 §5/Table 3; SP 800-38D §§5–7; RFC 5116 §§5.1–5.2

**sourceNote:** Covers all three NIST AES key sizes. RFC AEAD_AES_128_GCM and AEAD_AES_256_GCM identify the 128/256-bit instances; no RFC 5116 registry identity is asserted for AES-192. Uses the stricter NIST message limit.

**provenanceKind:** adapted

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-AESGCM-round-trip"></a>

### round-trip

`urn:csabs:theorem/AESGCM-round-trip`

**statement:** The AES instantiation retains the functional GCM round-trip equation.

**formalStatement:** seal_ℓ(k,IV,A,P)=(C,T) ⇒ open_ℓ(k,IV,A,C,T)=inl(P).

**assumptions:** Selected byte-oriented 96-bit-IV, 128-bit-tag profile of SP 800-38D. Underlying block cipher E has 128-bit blocks. K is its key carrier; IV is exactly 12 bytes; 0≤|P|≤2^36−32 bytes and 0≤|A|≤2^61−1 bytes. Ciphertext has |P| bytes, tag has 16 bytes. len denotes bits in equations; |·| denotes bytes. Empty P and A are valid. Equality is exact bit strings; [x]_s is unsigned big-endian encoding, while GHASH has its own polynomial coefficient order. Other IV/tag lengths require explicit variants. No padding is added to the returned plaintext or ciphertext. Fix AES key length ℓ per instance. This entry uses the NIST plaintext ceiling 2^36−32 bytes; it does not adopt RFC 5116’s one-byte-larger listed P_MAX.

**ruleRole:** derived-result

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial mathematics; not a machine-checked proof.

**source:** [NIST FIPS 197-upd1: Advanced Encryption Standard (2023 editorial update)](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197-upd1.pdf); accessedOn: 2026-11-10; sourceRole: primary normative specification; [NIST SP 800-38D: Galois/Counter Mode (GCM) and GMAC (2007)](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf); accessedOn: 2026-11-10; sourceRole: primary normative specification; [RFC 5116: An Interface and Algorithms for Authenticated Encryption](https://www.rfc-editor.org/rfc/rfc5116.html); accessedOn: 2026-11-10; sourceRole: primary normative specification

**sourceLocator:** FIPS 197 §5/Table 3; SP 800-38D §§5–7; RFC 5116 §§5.1–5.2

**sourceNote:** Editorial derivation from the linked premises. Covers all three NIST AES key sizes. RFC AEAD_AES_128_GCM and AEAD_AES_256_GCM identify the 128/256-bit instances; no RFC 5116 registry identity is asserted for AES-192. Uses the stricter NIST message limit.

**provenanceKind:** derived

**dependsOn:** [instantiation](AESGCM.md#node-urn-csabs-axiom-AESGCM-instantiation); [round-trip](GCM.md#node-urn-csabs-theorem-GCM-round-trip)

**proofSketch:** Substitute AES_ℓ for the underlying 128-bit block cipher in the GCM round-trip theorem. AES block invertibility is not needed by GCM, which uses only the forward primitive.

## Concept provenance

- [NIST FIPS 197-upd1: Advanced Encryption Standard (2023 editorial update)](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197-upd1.pdf); accessedOn: 2026-11-10; sourceRole: primary normative specification
- [NIST SP 800-38D: Galois/Counter Mode (GCM) and GMAC (2007)](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf); accessedOn: 2026-11-10; sourceRole: primary normative specification
- [RFC 5116: An Interface and Algorithms for Authenticated Encryption](https://www.rfc-editor.org/rfc/rfc5116.html); accessedOn: 2026-11-10; sourceRole: primary normative specification

**sourceLocator:** FIPS 197 §5/Table 3; SP 800-38D §§5–7; RFC 5116 §§5.1–5.2

**sourceNote:** Covers all three NIST AES key sizes. RFC AEAD_AES_128_GCM and AEAD_AES_256_GCM identify the 128/256-bit instances; no RFC 5116 registry identity is asserted for AES-192. Uses the stricter NIST message limit.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/AESGCM",
    "type": "Concept",
    "shortForm": "AESGCM",
    "fullName": "AES-GCM (96-bit nonce, 128-bit tag profile)",
    "definition": "The selected GCM profile instantiated with AES-128, AES-192 or AES-256, with explicit detached and combined wire encodings.",
    "notation": "AESGCM_ℓ=GCM_{AES_ℓ}; ℓ∈{128,192,256}; combined output W=C∥T.",
    "category": [
      "urn:csabs:category/symmetric-cryptography"
    ],
    "kind": "urn:csabs:kind/construction",
    "requiresConcept": [
      "urn:csabs:concept/AES",
      "urn:csabs:concept/GCM"
    ],
    "axiomBasis": "Explicit AES instantiation of the GCM equations and unambiguous fixed-length trailing tag encoding.",
    "basisKind": "defined-structure",
    "basisScope": "Selected byte-oriented 96-bit-IV, 128-bit-tag profile of SP 800-38D. Underlying block cipher E has 128-bit blocks. K is its key carrier; IV is exactly 12 bytes; 0≤|P|≤2^36−32 bytes and 0≤|A|≤2^61−1 bytes. Ciphertext has |P| bytes, tag has 16 bytes. len denotes bits in equations; |·| denotes bytes. Empty P and A are valid. Equality is exact bit strings; [x]_s is unsigned big-endian encoding, while GHASH has its own polynomial coefficient order. Other IV/tag lengths require explicit variants. No padding is added to the returned plaintext or ciphertext. Fix AES key length ℓ per instance. This entry uses the NIST plaintext ceiling 2^36−32 bytes; it does not adopt RFC 5116’s one-byte-larger listed P_MAX.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial specification; no cryptographic security proof or compiled claim witness.",
    "verificationObligation": [
      "Map byte and bit order, exact lengths, equality, errors and key handling explicitly. Functional equations alone do not establish computational security or resistance to side channels."
    ],
    "hasOperation": [
      "urn:csabs:operation/AESGCM-seal",
      "urn:csabs:operation/AESGCM-open",
      "urn:csabs:operation/AESGCM-pack",
      "urn:csabs:operation/AESGCM-unpack"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/AESGCM-instantiation",
      "urn:csabs:axiom/AESGCM-combined-encoding"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/AESGCM-round-trip"
    ],
    "source": [
      "urn:csabs:source/nist-fips197-upd1",
      "urn:csabs:source/nist-sp800-38d",
      "urn:csabs:source/rfc5116"
    ],
    "sourceLocator": "FIPS 197 §5/Table 3; SP 800-38D §§5–7; RFC 5116 §§5.1–5.2",
    "sourceNote": "Covers all three NIST AES key sizes. RFC AEAD_AES_128_GCM and AEAD_AES_256_GCM identify the 128/256-bit instances; no RFC 5116 registry identity is asserted for AES-192. Uses the stricter NIST message limit.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/GCM"
    ],
    "specializationNote": "Set the underlying keyed block permutation E_k to the exact AES_ℓ(k,−), with ℓ=128,192 or 256. Preserve IV, AAD, plaintext, length encoding, counter order and tag equations. AES is a component prerequisite, not a parent of this authenticated-encryption construction."
  },
  {
    "id": "urn:csabs:operation/AESGCM-seal",
    "type": "Operation",
    "name": "seal",
    "signature": "seal_ℓ : B_ℓ×B_96×A×P → C×B_128",
    "description": "Use AES in the selected GCM profile.",
    "precondition": "ℓ∈{128,192,256}, typed key and profile lengths; fresh nonce for secure use.",
    "postcondition": "GCM_{AES_ℓ}.seal(k,IV,A,P).",
    "totality": "total on the stated precondition; outside the domain return an input error without partial output",
    "concept": "urn:csabs:concept/AESGCM",
    "source": [
      "urn:csabs:source/nist-fips197-upd1",
      "urn:csabs:source/nist-sp800-38d",
      "urn:csabs:source/rfc5116"
    ],
    "sourceLocator": "FIPS 197 §5/Table 3; SP 800-38D §§5–7; RFC 5116 §§5.1–5.2",
    "sourceNote": "Covers all three NIST AES key sizes. RFC AEAD_AES_128_GCM and AEAD_AES_256_GCM identify the 128/256-bit instances; no RFC 5116 registry identity is asserted for AES-192. Uses the stricter NIST message limit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/AESGCM-open",
    "type": "Operation",
    "name": "open",
    "signature": "open_ℓ : B_ℓ×B_96×A×C×B_128 → P⊎{FAIL}",
    "description": "Authenticate and decrypt with the same selected AES key size.",
    "precondition": "Exact profile lengths and tag; invalid inputs yield an error or FAIL without plaintext.",
    "postcondition": "GCM_{AES_ℓ}.open(k,IV,A,C,T).",
    "totality": "total on the stated precondition; outside the domain return an input error without partial output",
    "concept": "urn:csabs:concept/AESGCM",
    "source": [
      "urn:csabs:source/nist-fips197-upd1",
      "urn:csabs:source/nist-sp800-38d",
      "urn:csabs:source/rfc5116"
    ],
    "sourceLocator": "FIPS 197 §5/Table 3; SP 800-38D §§5–7; RFC 5116 §§5.1–5.2",
    "sourceNote": "Covers all three NIST AES key sizes. RFC AEAD_AES_128_GCM and AEAD_AES_256_GCM identify the 128/256-bit instances; no RFC 5116 registry identity is asserted for AES-192. Uses the stricter NIST message limit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/AESGCM-pack",
    "type": "Operation",
    "name": "pack",
    "signature": "pack : C×B_128 → W",
    "description": "Append the detached tag to ciphertext.",
    "precondition": "C meets the selected plaintext byte limit; tag has exactly 16 bytes.",
    "postcondition": "W=C∥T; |W|=|C|+16 bytes.",
    "totality": "total on the stated precondition; outside the domain return an input error without partial output",
    "concept": "urn:csabs:concept/AESGCM",
    "source": [
      "urn:csabs:source/nist-fips197-upd1",
      "urn:csabs:source/nist-sp800-38d",
      "urn:csabs:source/rfc5116"
    ],
    "sourceLocator": "FIPS 197 §5/Table 3; SP 800-38D §§5–7; RFC 5116 §§5.1–5.2",
    "sourceNote": "Covers all three NIST AES key sizes. RFC AEAD_AES_128_GCM and AEAD_AES_256_GCM identify the 128/256-bit instances; no RFC 5116 registry identity is asserted for AES-192. Uses the stricter NIST message limit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/AESGCM-unpack",
    "type": "Operation",
    "name": "unpack",
    "signature": "unpack : W ⇀ C×B_128",
    "description": "Split off the final 16 bytes as the tag.",
    "precondition": "16≤|W|≤2^36−16 bytes.",
    "postcondition": "C is all but the last 16 bytes; T is the last 16 bytes. A 16-byte W represents empty ciphertext with a tag; shorter input is rejected.",
    "totality": "total on the stated precondition; outside the domain return an input error without partial output",
    "concept": "urn:csabs:concept/AESGCM",
    "source": [
      "urn:csabs:source/nist-fips197-upd1",
      "urn:csabs:source/nist-sp800-38d",
      "urn:csabs:source/rfc5116"
    ],
    "sourceLocator": "FIPS 197 §5/Table 3; SP 800-38D §§5–7; RFC 5116 §§5.1–5.2",
    "sourceNote": "Covers all three NIST AES key sizes. RFC AEAD_AES_128_GCM and AEAD_AES_256_GCM identify the 128/256-bit instances; no RFC 5116 registry identity is asserted for AES-192. Uses the stricter NIST message limit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/AESGCM-instantiation",
    "type": "Axiom",
    "name": "instantiation",
    "statement": "AES-GCM fixes the GCM primitive to the selected AES permutation.",
    "formalStatement": "E_k(x)=AES_ℓ(k,x); seal_ℓ=GCM_{AES_ℓ}.seal; open_ℓ=GCM_{AES_ℓ}.open; ℓ∈{128,192,256}.",
    "assumptions": [
      "Selected byte-oriented 96-bit-IV, 128-bit-tag profile of SP 800-38D. Underlying block cipher E has 128-bit blocks. K is its key carrier; IV is exactly 12 bytes; 0≤|P|≤2^36−32 bytes and 0≤|A|≤2^61−1 bytes. Ciphertext has |P| bytes, tag has 16 bytes. len denotes bits in equations; |·| denotes bytes. Empty P and A are valid. Equality is exact bit strings; [x]_s is unsigned big-endian encoding, while GHASH has its own polynomial coefficient order. Other IV/tag lengths require explicit variants. No padding is added to the returned plaintext or ciphertext. Fix AES key length ℓ per instance. This entry uses the NIST plaintext ceiling 2^36−32 bytes; it does not adopt RFC 5116’s one-byte-larger listed P_MAX."
    ],
    "appliesTo": [
      "urn:csabs:concept/AESGCM"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial mathematics; not a machine-checked proof.",
    "source": [
      "urn:csabs:source/nist-fips197-upd1",
      "urn:csabs:source/nist-sp800-38d",
      "urn:csabs:source/rfc5116"
    ],
    "sourceLocator": "FIPS 197 §5/Table 3; SP 800-38D §§5–7; RFC 5116 §§5.1–5.2",
    "sourceNote": "Covers all three NIST AES key sizes. RFC AEAD_AES_128_GCM and AEAD_AES_256_GCM identify the 128/256-bit instances; no RFC 5116 registry identity is asserted for AES-192. Uses the stricter NIST message limit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/AESGCM-combined-encoding",
    "type": "Axiom",
    "name": "combined-encoding",
    "statement": "Combined output contains ciphertext followed by a full tag.",
    "formalStatement": "pack(C,T)=C∥T; unpack(W)=(prefix_(|W|−16)(W),suffix_16(W)); |pack(C,T)|=|C|+16 bytes; |W|<16 is invalid.",
    "assumptions": [
      "Selected byte-oriented 96-bit-IV, 128-bit-tag profile of SP 800-38D. Underlying block cipher E has 128-bit blocks. K is its key carrier; IV is exactly 12 bytes; 0≤|P|≤2^36−32 bytes and 0≤|A|≤2^61−1 bytes. Ciphertext has |P| bytes, tag has 16 bytes. len denotes bits in equations; |·| denotes bytes. Empty P and A are valid. Equality is exact bit strings; [x]_s is unsigned big-endian encoding, while GHASH has its own polynomial coefficient order. Other IV/tag lengths require explicit variants. No padding is added to the returned plaintext or ciphertext. Fix AES key length ℓ per instance. This entry uses the NIST plaintext ceiling 2^36−32 bytes; it does not adopt RFC 5116’s one-byte-larger listed P_MAX."
    ],
    "appliesTo": [
      "urn:csabs:concept/AESGCM"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial mathematics; not a machine-checked proof.",
    "source": [
      "urn:csabs:source/nist-fips197-upd1",
      "urn:csabs:source/nist-sp800-38d",
      "urn:csabs:source/rfc5116"
    ],
    "sourceLocator": "FIPS 197 §5/Table 3; SP 800-38D §§5–7; RFC 5116 §§5.1–5.2",
    "sourceNote": "Covers all three NIST AES key sizes. RFC AEAD_AES_128_GCM and AEAD_AES_256_GCM identify the 128/256-bit instances; no RFC 5116 registry identity is asserted for AES-192. Uses the stricter NIST message limit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:theorem/AESGCM-round-trip",
    "type": "Theorem",
    "name": "round-trip",
    "statement": "The AES instantiation retains the functional GCM round-trip equation.",
    "formalStatement": "seal_ℓ(k,IV,A,P)=(C,T) ⇒ open_ℓ(k,IV,A,C,T)=inl(P).",
    "assumptions": [
      "Selected byte-oriented 96-bit-IV, 128-bit-tag profile of SP 800-38D. Underlying block cipher E has 128-bit blocks. K is its key carrier; IV is exactly 12 bytes; 0≤|P|≤2^36−32 bytes and 0≤|A|≤2^61−1 bytes. Ciphertext has |P| bytes, tag has 16 bytes. len denotes bits in equations; |·| denotes bytes. Empty P and A are valid. Equality is exact bit strings; [x]_s is unsigned big-endian encoding, while GHASH has its own polynomial coefficient order. Other IV/tag lengths require explicit variants. No padding is added to the returned plaintext or ciphertext. Fix AES key length ℓ per instance. This entry uses the NIST plaintext ceiling 2^36−32 bytes; it does not adopt RFC 5116’s one-byte-larger listed P_MAX."
    ],
    "appliesTo": [
      "urn:csabs:concept/AESGCM"
    ],
    "ruleRole": "derived-result",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial mathematics; not a machine-checked proof.",
    "source": [
      "urn:csabs:source/nist-fips197-upd1",
      "urn:csabs:source/nist-sp800-38d",
      "urn:csabs:source/rfc5116"
    ],
    "sourceLocator": "FIPS 197 §5/Table 3; SP 800-38D §§5–7; RFC 5116 §§5.1–5.2",
    "sourceNote": "Editorial derivation from the linked premises. Covers all three NIST AES key sizes. RFC AEAD_AES_128_GCM and AEAD_AES_256_GCM identify the 128/256-bit instances; no RFC 5116 registry identity is asserted for AES-192. Uses the stricter NIST message limit.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/AESGCM-instantiation",
      "urn:csabs:theorem/GCM-round-trip"
    ],
    "proofSketch": "Substitute AES_ℓ for the underlying 128-bit block cipher in the GCM round-trip theorem. AES block invertibility is not needed by GCM, which uses only the forward primitive."
  }
]
```
<!-- graph-record:end -->
