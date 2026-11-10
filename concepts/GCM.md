# Galois/Counter Mode (96-bit IV, 128-bit tag profile)

Authenticated encryption combining counter-mode use of a 128-bit block cipher with GHASH and a masked authentication tag.

**Notation:** GCM_E.seal(k,IV,A,P)=(C,T); GCM_E.open(k,IV,A,C,T)=P or FAIL.

**Stable ID:** `urn:csabs:concept/GCM`

**Categories:** Cryptography → Symmetric cryptography

**Kind:** Mathematical construction

**Prerequisites:** [Keyed block cipher](BlockCipher.md), [GHASH polynomial accumulator](GHASH.md), [Nonce-based authenticated encryption with associated data](AEAD.md)

**Specializes:** [Nonce-based authenticated encryption with associated data](AEAD.md)

## Backlinks

- [AES-GCM (96-bit nonce, 128-bit tag profile)](AESGCM.md) — `requiresConcept`
- [AES-GCM (96-bit nonce, 128-bit tag profile)](AESGCM.md) — `specializationOf`

## Interface and scope

**axiomBasis:** inc32 and GCTR; derivation of H and J₀; encoded GHASH input; tag calculation and authenticated decryption.

**basisKind:** defined-structure

**basisScope:** Selected byte-oriented 96-bit-IV, 128-bit-tag profile of SP 800-38D. Underlying block cipher E has 128-bit blocks. K is its key carrier; IV is exactly 12 bytes; 0≤|P|≤2^36−32 bytes and 0≤|A|≤2^61−1 bytes. Ciphertext has |P| bytes, tag has 16 bytes. len denotes bits in equations; |·| denotes bytes. Empty P and A are valid. Equality is exact bit strings; [x]_s is unsigned big-endian encoding, while GHASH has its own polynomial coefficient order. Other IV/tag lengths require explicit variants. No padding is added to the returned plaintext or ciphertext.

**specializationNote:** Instantiate N with 12-byte IVs and W with encoded pairs (C,T), T of length 16 bytes; flattening the pair into bytes requires a specified bijective encoding. Set the AEAD plaintext/AAD domains to the stated bounds. GCM rules are explicit and not inherited.

**verificationObligation:** Map byte and bit order, exact lengths, equality, errors and key handling explicitly. Functional equations alone do not establish computational security or resistance to side channels.; Track nonce allocation across concurrency, crash recovery and every sender using the key; random IV generation needs an explicit collision budget. Per-message length limits alone do not establish a safe key lifetime: account for total data, invocation count and failed verifications under §§8.2–8.3 and Appendix B.; No deterministic rejection theorem is asserted for arbitrary altered AAD/ciphertext/nonces: a changed input can collide in the tag function. GHASH alone provides no authentication. Tag verification must not release tentative plaintext. Replay prevention and constant-time behavior require additional implementation/protocol obligations.

**reviewStatus:** Editorial specification; no cryptographic security proof or compiled claim witness.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-GCM-inc32"></a>

### inc32

`urn:csabs:operation/GCM-inc32`

**signature:** inc32 : B_128 → B_128

**description:** Increment only the rightmost 32 bits modulo 2^32.

**precondition:** Exactly one block; rightmost word interpreted as unsigned big-endian.

**postcondition:** inc32(X)=MSB_96(X)∥[(int(LSB_32(X))+1) mod 2^32]_32.

**totality:** total on the stated precondition; outside the domain return an input error without partial output

**source:** [NIST SP 800-38D: Galois/Counter Mode (GCM) and GMAC (2007)](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf); accessedOn: 2026-11-10; sourceRole: primary normative specification

**sourceLocator:** Sections 5.1–5.2, 6.2, 6.5, 7.1–7.2, 8; Appendices A, B and D

**sourceNote:** Explicit restricted profile using detached (C,T) output. Nonce uniqueness is a usage obligation; computational security is not asserted as a defining equation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-GCM-gctr"></a>

### gctr

`urn:csabs:operation/GCM-gctr`

**signature:** GCTR : K×B_128×Bytes* → Bytes*

**description:** XOR input with encrypted successive counter blocks, truncating the final keystream block.

**precondition:** Typed key and initial block; at most 2^32−2 input blocks for this profile.

**postcondition:** GCTR(k,ICB,ε)=ε; block i uses E_k(inc32^(i−1)(ICB)); last block uses its leftmost len(X_i) bits.

**totality:** total on the stated precondition; outside the domain return an input error without partial output

**source:** [NIST SP 800-38D: Galois/Counter Mode (GCM) and GMAC (2007)](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf); accessedOn: 2026-11-10; sourceRole: primary normative specification

**sourceLocator:** Sections 5.1–5.2, 6.2, 6.5, 7.1–7.2, 8; Appendices A, B and D

**sourceNote:** Explicit restricted profile using detached (C,T) output. Nonce uniqueness is a usage obligation; computational security is not asserted as a defining equation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-GCM-seal"></a>

### seal

`urn:csabs:operation/GCM-seal`

**signature:** seal : K×B_96×A×P → C×B_128

**description:** Encrypt and compute a detached tag.

**precondition:** Profile lengths; nonce must be fresh under k for secure encryption.

**postcondition:** Return (C,T) using the defining encryption equations.

**totality:** total on the stated precondition; outside the domain return an input error without partial output

**source:** [NIST SP 800-38D: Galois/Counter Mode (GCM) and GMAC (2007)](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf); accessedOn: 2026-11-10; sourceRole: primary normative specification

**sourceLocator:** Sections 5.1–5.2, 6.2, 6.5, 7.1–7.2, 8; Appendices A, B and D

**sourceNote:** Explicit restricted profile using detached (C,T) output. Nonce uniqueness is a usage obligation; computational security is not asserted as a defining equation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-GCM-open"></a>

### open

`urn:csabs:operation/GCM-open`

**signature:** open : K×B_96×A×C×B_128 → P⊎{FAIL}

**description:** Verify the detached tag and decrypt.

**precondition:** Profile lengths and full 128-bit tag; reject invalid lengths without plaintext.

**postcondition:** Return GCTR(k,inc32(J₀),C) iff the computed tag equals T; otherwise FAIL; no plaintext is released on failure.

**totality:** total on the stated precondition; outside the domain return an input error without partial output

**source:** [NIST SP 800-38D: Galois/Counter Mode (GCM) and GMAC (2007)](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf); accessedOn: 2026-11-10; sourceRole: primary normative specification

**sourceLocator:** Sections 5.1–5.2, 6.2, 6.5, 7.1–7.2, 8; Appendices A, B and D

**sourceNote:** Explicit restricted profile using detached (C,T) output. Nonce uniqueness is a usage obligation; computational security is not asserted as a defining equation.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-GCM-counter-transform"></a>

### counter-transform

`urn:csabs:axiom/GCM-counter-transform`

**statement:** GCTR uses a reproducible XOR keystream and has an explicit empty case.

**formalStatement:** GCTR(k,ICB,ε)=ε; CB_i=inc32^(i−1)(ICB); Y_i=X_i⊕MSB_len(X_i)(E_k(CB_i)); output=Y₁∥…∥Y_m; inc32 preserves the first 96 bits and increments the last 32 modulo 2^32.

**assumptions:** Selected byte-oriented 96-bit-IV, 128-bit-tag profile of SP 800-38D. Underlying block cipher E has 128-bit blocks. K is its key carrier; IV is exactly 12 bytes; 0≤|P|≤2^36−32 bytes and 0≤|A|≤2^61−1 bytes. Ciphertext has |P| bytes, tag has 16 bytes. len denotes bits in equations; |·| denotes bytes. Empty P and A are valid. Equality is exact bit strings; [x]_s is unsigned big-endian encoding, while GHASH has its own polynomial coefficient order. Other IV/tag lengths require explicit variants. No padding is added to the returned plaintext or ciphertext.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial mathematics; not a machine-checked proof.

**source:** [NIST SP 800-38D: Galois/Counter Mode (GCM) and GMAC (2007)](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf); accessedOn: 2026-11-10; sourceRole: primary normative specification

**sourceLocator:** Sections 5.1–5.2, 6.2, 6.5, 7.1–7.2, 8; Appendices A, B and D

**sourceNote:** Explicit restricted profile using detached (C,T) output. Nonce uniqueness is a usage obligation; computational security is not asserted as a defining equation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-GCM-encryption"></a>

### encryption

`urn:csabs:axiom/GCM-encryption`

**statement:** Encryption binds AAD and ciphertext lengths into the tag.

**formalStatement:** H=E_k(0^128); J₀=IV∥0^31∥1; C=GCTR(k,inc32(J₀),P); v=(−len(A)) mod 128; u=(−len(C)) mod 128; S=GHASH_H(A∥0^v∥C∥0^u∥[len(A)]_64∥[len(C)]_64); T=E_k(J₀)⊕S; seal(k,IV,A,P)=(C,T).

**assumptions:** Selected byte-oriented 96-bit-IV, 128-bit-tag profile of SP 800-38D. Underlying block cipher E has 128-bit blocks. K is its key carrier; IV is exactly 12 bytes; 0≤|P|≤2^36−32 bytes and 0≤|A|≤2^61−1 bytes. Ciphertext has |P| bytes, tag has 16 bytes. len denotes bits in equations; |·| denotes bytes. Empty P and A are valid. Equality is exact bit strings; [x]_s is unsigned big-endian encoding, while GHASH has its own polynomial coefficient order. Other IV/tag lengths require explicit variants. No padding is added to the returned plaintext or ciphertext.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial mathematics; not a machine-checked proof.

**source:** [NIST SP 800-38D: Galois/Counter Mode (GCM) and GMAC (2007)](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf); accessedOn: 2026-11-10; sourceRole: primary normative specification

**sourceLocator:** Sections 5.1–5.2, 6.2, 6.5, 7.1–7.2, 8; Appendices A, B and D

**sourceNote:** Explicit restricted profile using detached (C,T) output. Nonce uniqueness is a usage obligation; computational security is not asserted as a defining equation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-GCM-authenticated-decryption"></a>

### authenticated-decryption

`urn:csabs:axiom/GCM-authenticated-decryption`

**statement:** Only a matching tag produces plaintext.

**formalStatement:** Recompute H,J₀,S from k,IV,A,C as in encryption; open(k,IV,A,C,T)=inl(GCTR(k,inc32(J₀),C)) if T=E_k(J₀)⊕S, else FAIL.

**assumptions:** Selected byte-oriented 96-bit-IV, 128-bit-tag profile of SP 800-38D. Underlying block cipher E has 128-bit blocks. K is its key carrier; IV is exactly 12 bytes; 0≤|P|≤2^36−32 bytes and 0≤|A|≤2^61−1 bytes. Ciphertext has |P| bytes, tag has 16 bytes. len denotes bits in equations; |·| denotes bytes. Empty P and A are valid. Equality is exact bit strings; [x]_s is unsigned big-endian encoding, while GHASH has its own polynomial coefficient order. Other IV/tag lengths require explicit variants. No padding is added to the returned plaintext or ciphertext.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial mathematics; not a machine-checked proof.

**source:** [NIST SP 800-38D: Galois/Counter Mode (GCM) and GMAC (2007)](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf); accessedOn: 2026-11-10; sourceRole: primary normative specification

**sourceLocator:** Sections 5.1–5.2, 6.2, 6.5, 7.1–7.2, 8; Appendices A, B and D

**sourceNote:** Explicit restricted profile using detached (C,T) output. Nonce uniqueness is a usage obligation; computational security is not asserted as a defining equation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-GCM-nonce-discipline"></a>

### nonce-discipline

`urn:csabs:axiom/GCM-nonce-discipline`

**statement:** Encryption invocations under a fixed key use distinct IVs in the selected deterministic uniqueness discipline.

**formalStatement:** For distinct encryption invocations i≠j: k_i=k_j ⇒ IV_i≠IV_j; this includes concurrent writers, restarts and devices sharing a key.

**assumptions:** Selected deterministic nonce discipline, stronger than SP 800-38D §8’s probabilistic collision requirement. Not a constraint on repeated decryption or the mathematical evaluation of seal.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial mathematics; not a machine-checked proof.

**source:** [NIST SP 800-38D: Galois/Counter Mode (GCM) and GMAC (2007)](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf); accessedOn: 2026-11-10; sourceRole: primary normative specification

**sourceLocator:** Section 8 and Appendix A

**sourceNote:** Explicit restricted profile using detached (C,T) output. Nonce uniqueness is a usage obligation; computational security is not asserted as a defining equation.

**provenanceKind:** adapted

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-GCM-round-trip"></a>

### round-trip

`urn:csabs:theorem/GCM-round-trip`

**statement:** GCM decryption recovers an honestly encrypted message.

**formalStatement:** seal(k,IV,A,P)=(C,T) ⇒ open(k,IV,A,C,T)=inl(P).

**assumptions:** Selected byte-oriented 96-bit-IV, 128-bit-tag profile of SP 800-38D. Underlying block cipher E has 128-bit blocks. K is its key carrier; IV is exactly 12 bytes; 0≤|P|≤2^36−32 bytes and 0≤|A|≤2^61−1 bytes. Ciphertext has |P| bytes, tag has 16 bytes. len denotes bits in equations; |·| denotes bytes. Empty P and A are valid. Equality is exact bit strings; [x]_s is unsigned big-endian encoding, while GHASH has its own polynomial coefficient order. Other IV/tag lengths require explicit variants. No padding is added to the returned plaintext or ciphertext.

**ruleRole:** derived-result

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial mathematics; not a machine-checked proof.

**source:** [NIST SP 800-38D: Galois/Counter Mode (GCM) and GMAC (2007)](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf); accessedOn: 2026-11-10; sourceRole: primary normative specification

**sourceLocator:** Sections 5.1–5.2, 6.2, 6.5, 7.1–7.2, 8; Appendices A, B and D

**sourceNote:** Editorial derivation from the linked premises. Explicit restricted profile using detached (C,T) output. Nonce uniqueness is a usage obligation; computational security is not asserted as a defining equation.

**provenanceKind:** derived

**dependsOn:** [counter-transform](GCM.md#node-urn-csabs-axiom-GCM-counter-transform); [encryption](GCM.md#node-urn-csabs-axiom-GCM-encryption); [authenticated-decryption](GCM.md#node-urn-csabs-axiom-GCM-authenticated-decryption)

**proofSketch:** The same IV gives the same J₀, counters and H. Recomputed S gives the original T. Applying GCTR twice XORs the same keystream twice, recovering every input byte, including the empty case. Freshness is unnecessary for this functional equality, but necessary for secure use.

<a id="node-urn-csabs-theorem-GCM-reused-nonce-xor"></a>

### reused-nonce-xor

`urn:csabs:theorem/GCM-reused-nonce-xor`

**statement:** Nonce reuse exposes the XOR of equal-length plaintexts.

**formalStatement:** seal(k,IV,A₁,P₁)=(C₁,T₁) ∧ seal(k,IV,A₂,P₂)=(C₂,T₂) ∧ len(P₁)=len(P₂) ⇒ C₁⊕C₂=P₁⊕P₂.

**assumptions:** Counterfactual repeated-IV evaluations of the deterministic encryption function; they violate the secure-use nonce discipline. Equal-length admissible plaintexts.

**ruleRole:** derived-result

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial mathematics; not a machine-checked proof.

**source:** [NIST SP 800-38D: Galois/Counter Mode (GCM) and GMAC (2007)](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf); accessedOn: 2026-11-10; sourceRole: primary normative specification

**sourceLocator:** Sections 6.5 and 7.1; Appendix A

**sourceNote:** Editorial derivation from the linked premises. Explicit restricted profile using detached (C,T) output. Nonce uniqueness is a usage obligation; computational security is not asserted as a defining equation.

**provenanceKind:** derived

**dependsOn:** [counter-transform](GCM.md#node-urn-csabs-axiom-GCM-counter-transform); [encryption](GCM.md#node-urn-csabs-axiom-GCM-encryption)

**proofSketch:** Both ciphertexts use the same counter keystream Z, independently of AAD. Cancel Z from (P₁⊕Z)⊕(P₂⊕Z). This is a confidentiality failure, not a proof of a complete authentication attack.

## Concept provenance

- [NIST SP 800-38D: Galois/Counter Mode (GCM) and GMAC (2007)](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf); accessedOn: 2026-11-10; sourceRole: primary normative specification

**sourceLocator:** Sections 5.1–5.2, 6.2, 6.5, 7.1–7.2, 8; Appendices A, B and D

**sourceNote:** Explicit restricted profile using detached (C,T) output. Nonce uniqueness is a usage obligation; computational security is not asserted as a defining equation.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/GCM",
    "type": "Concept",
    "shortForm": "GCM",
    "fullName": "Galois/Counter Mode (96-bit IV, 128-bit tag profile)",
    "definition": "Authenticated encryption combining counter-mode use of a 128-bit block cipher with GHASH and a masked authentication tag.",
    "notation": "GCM_E.seal(k,IV,A,P)=(C,T); GCM_E.open(k,IV,A,C,T)=P or FAIL.",
    "category": [
      "urn:csabs:category/symmetric-cryptography"
    ],
    "kind": "urn:csabs:kind/construction",
    "requiresConcept": [
      "urn:csabs:concept/BlockCipher",
      "urn:csabs:concept/GHASH",
      "urn:csabs:concept/AEAD"
    ],
    "axiomBasis": "inc32 and GCTR; derivation of H and J₀; encoded GHASH input; tag calculation and authenticated decryption.",
    "basisKind": "defined-structure",
    "basisScope": "Selected byte-oriented 96-bit-IV, 128-bit-tag profile of SP 800-38D. Underlying block cipher E has 128-bit blocks. K is its key carrier; IV is exactly 12 bytes; 0≤|P|≤2^36−32 bytes and 0≤|A|≤2^61−1 bytes. Ciphertext has |P| bytes, tag has 16 bytes. len denotes bits in equations; |·| denotes bytes. Empty P and A are valid. Equality is exact bit strings; [x]_s is unsigned big-endian encoding, while GHASH has its own polynomial coefficient order. Other IV/tag lengths require explicit variants. No padding is added to the returned plaintext or ciphertext.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial specification; no cryptographic security proof or compiled claim witness.",
    "verificationObligation": [
      "Map byte and bit order, exact lengths, equality, errors and key handling explicitly. Functional equations alone do not establish computational security or resistance to side channels.",
      "Track nonce allocation across concurrency, crash recovery and every sender using the key; random IV generation needs an explicit collision budget. Per-message length limits alone do not establish a safe key lifetime: account for total data, invocation count and failed verifications under §§8.2–8.3 and Appendix B.",
      "No deterministic rejection theorem is asserted for arbitrary altered AAD/ciphertext/nonces: a changed input can collide in the tag function. GHASH alone provides no authentication. Tag verification must not release tentative plaintext. Replay prevention and constant-time behavior require additional implementation/protocol obligations."
    ],
    "hasOperation": [
      "urn:csabs:operation/GCM-inc32",
      "urn:csabs:operation/GCM-gctr",
      "urn:csabs:operation/GCM-seal",
      "urn:csabs:operation/GCM-open"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/GCM-counter-transform",
      "urn:csabs:axiom/GCM-encryption",
      "urn:csabs:axiom/GCM-authenticated-decryption",
      "urn:csabs:axiom/GCM-nonce-discipline"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/GCM-round-trip",
      "urn:csabs:theorem/GCM-reused-nonce-xor"
    ],
    "source": [
      "urn:csabs:source/nist-sp800-38d"
    ],
    "sourceLocator": "Sections 5.1–5.2, 6.2, 6.5, 7.1–7.2, 8; Appendices A, B and D",
    "sourceNote": "Explicit restricted profile using detached (C,T) output. Nonce uniqueness is a usage obligation; computational security is not asserted as a defining equation.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/AEAD"
    ],
    "specializationNote": "Instantiate N with 12-byte IVs and W with encoded pairs (C,T), T of length 16 bytes; flattening the pair into bytes requires a specified bijective encoding. Set the AEAD plaintext/AAD domains to the stated bounds. GCM rules are explicit and not inherited."
  },
  {
    "id": "urn:csabs:operation/GCM-inc32",
    "type": "Operation",
    "name": "inc32",
    "signature": "inc32 : B_128 → B_128",
    "description": "Increment only the rightmost 32 bits modulo 2^32.",
    "precondition": "Exactly one block; rightmost word interpreted as unsigned big-endian.",
    "postcondition": "inc32(X)=MSB_96(X)∥[(int(LSB_32(X))+1) mod 2^32]_32.",
    "totality": "total on the stated precondition; outside the domain return an input error without partial output",
    "concept": "urn:csabs:concept/GCM",
    "source": [
      "urn:csabs:source/nist-sp800-38d"
    ],
    "sourceLocator": "Sections 5.1–5.2, 6.2, 6.5, 7.1–7.2, 8; Appendices A, B and D",
    "sourceNote": "Explicit restricted profile using detached (C,T) output. Nonce uniqueness is a usage obligation; computational security is not asserted as a defining equation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/GCM-gctr",
    "type": "Operation",
    "name": "gctr",
    "signature": "GCTR : K×B_128×Bytes* → Bytes*",
    "description": "XOR input with encrypted successive counter blocks, truncating the final keystream block.",
    "precondition": "Typed key and initial block; at most 2^32−2 input blocks for this profile.",
    "postcondition": "GCTR(k,ICB,ε)=ε; block i uses E_k(inc32^(i−1)(ICB)); last block uses its leftmost len(X_i) bits.",
    "totality": "total on the stated precondition; outside the domain return an input error without partial output",
    "concept": "urn:csabs:concept/GCM",
    "source": [
      "urn:csabs:source/nist-sp800-38d"
    ],
    "sourceLocator": "Sections 5.1–5.2, 6.2, 6.5, 7.1–7.2, 8; Appendices A, B and D",
    "sourceNote": "Explicit restricted profile using detached (C,T) output. Nonce uniqueness is a usage obligation; computational security is not asserted as a defining equation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/GCM-seal",
    "type": "Operation",
    "name": "seal",
    "signature": "seal : K×B_96×A×P → C×B_128",
    "description": "Encrypt and compute a detached tag.",
    "precondition": "Profile lengths; nonce must be fresh under k for secure encryption.",
    "postcondition": "Return (C,T) using the defining encryption equations.",
    "totality": "total on the stated precondition; outside the domain return an input error without partial output",
    "concept": "urn:csabs:concept/GCM",
    "source": [
      "urn:csabs:source/nist-sp800-38d"
    ],
    "sourceLocator": "Sections 5.1–5.2, 6.2, 6.5, 7.1–7.2, 8; Appendices A, B and D",
    "sourceNote": "Explicit restricted profile using detached (C,T) output. Nonce uniqueness is a usage obligation; computational security is not asserted as a defining equation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/GCM-open",
    "type": "Operation",
    "name": "open",
    "signature": "open : K×B_96×A×C×B_128 → P⊎{FAIL}",
    "description": "Verify the detached tag and decrypt.",
    "precondition": "Profile lengths and full 128-bit tag; reject invalid lengths without plaintext.",
    "postcondition": "Return GCTR(k,inc32(J₀),C) iff the computed tag equals T; otherwise FAIL; no plaintext is released on failure.",
    "totality": "total on the stated precondition; outside the domain return an input error without partial output",
    "concept": "urn:csabs:concept/GCM",
    "source": [
      "urn:csabs:source/nist-sp800-38d"
    ],
    "sourceLocator": "Sections 5.1–5.2, 6.2, 6.5, 7.1–7.2, 8; Appendices A, B and D",
    "sourceNote": "Explicit restricted profile using detached (C,T) output. Nonce uniqueness is a usage obligation; computational security is not asserted as a defining equation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/GCM-counter-transform",
    "type": "Axiom",
    "name": "counter-transform",
    "statement": "GCTR uses a reproducible XOR keystream and has an explicit empty case.",
    "formalStatement": "GCTR(k,ICB,ε)=ε; CB_i=inc32^(i−1)(ICB); Y_i=X_i⊕MSB_len(X_i)(E_k(CB_i)); output=Y₁∥…∥Y_m; inc32 preserves the first 96 bits and increments the last 32 modulo 2^32.",
    "assumptions": [
      "Selected byte-oriented 96-bit-IV, 128-bit-tag profile of SP 800-38D. Underlying block cipher E has 128-bit blocks. K is its key carrier; IV is exactly 12 bytes; 0≤|P|≤2^36−32 bytes and 0≤|A|≤2^61−1 bytes. Ciphertext has |P| bytes, tag has 16 bytes. len denotes bits in equations; |·| denotes bytes. Empty P and A are valid. Equality is exact bit strings; [x]_s is unsigned big-endian encoding, while GHASH has its own polynomial coefficient order. Other IV/tag lengths require explicit variants. No padding is added to the returned plaintext or ciphertext."
    ],
    "appliesTo": [
      "urn:csabs:concept/GCM"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial mathematics; not a machine-checked proof.",
    "source": [
      "urn:csabs:source/nist-sp800-38d"
    ],
    "sourceLocator": "Sections 5.1–5.2, 6.2, 6.5, 7.1–7.2, 8; Appendices A, B and D",
    "sourceNote": "Explicit restricted profile using detached (C,T) output. Nonce uniqueness is a usage obligation; computational security is not asserted as a defining equation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/GCM-encryption",
    "type": "Axiom",
    "name": "encryption",
    "statement": "Encryption binds AAD and ciphertext lengths into the tag.",
    "formalStatement": "H=E_k(0^128); J₀=IV∥0^31∥1; C=GCTR(k,inc32(J₀),P); v=(−len(A)) mod 128; u=(−len(C)) mod 128; S=GHASH_H(A∥0^v∥C∥0^u∥[len(A)]_64∥[len(C)]_64); T=E_k(J₀)⊕S; seal(k,IV,A,P)=(C,T).",
    "assumptions": [
      "Selected byte-oriented 96-bit-IV, 128-bit-tag profile of SP 800-38D. Underlying block cipher E has 128-bit blocks. K is its key carrier; IV is exactly 12 bytes; 0≤|P|≤2^36−32 bytes and 0≤|A|≤2^61−1 bytes. Ciphertext has |P| bytes, tag has 16 bytes. len denotes bits in equations; |·| denotes bytes. Empty P and A are valid. Equality is exact bit strings; [x]_s is unsigned big-endian encoding, while GHASH has its own polynomial coefficient order. Other IV/tag lengths require explicit variants. No padding is added to the returned plaintext or ciphertext."
    ],
    "appliesTo": [
      "urn:csabs:concept/GCM"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial mathematics; not a machine-checked proof.",
    "source": [
      "urn:csabs:source/nist-sp800-38d"
    ],
    "sourceLocator": "Sections 5.1–5.2, 6.2, 6.5, 7.1–7.2, 8; Appendices A, B and D",
    "sourceNote": "Explicit restricted profile using detached (C,T) output. Nonce uniqueness is a usage obligation; computational security is not asserted as a defining equation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/GCM-authenticated-decryption",
    "type": "Axiom",
    "name": "authenticated-decryption",
    "statement": "Only a matching tag produces plaintext.",
    "formalStatement": "Recompute H,J₀,S from k,IV,A,C as in encryption; open(k,IV,A,C,T)=inl(GCTR(k,inc32(J₀),C)) if T=E_k(J₀)⊕S, else FAIL.",
    "assumptions": [
      "Selected byte-oriented 96-bit-IV, 128-bit-tag profile of SP 800-38D. Underlying block cipher E has 128-bit blocks. K is its key carrier; IV is exactly 12 bytes; 0≤|P|≤2^36−32 bytes and 0≤|A|≤2^61−1 bytes. Ciphertext has |P| bytes, tag has 16 bytes. len denotes bits in equations; |·| denotes bytes. Empty P and A are valid. Equality is exact bit strings; [x]_s is unsigned big-endian encoding, while GHASH has its own polynomial coefficient order. Other IV/tag lengths require explicit variants. No padding is added to the returned plaintext or ciphertext."
    ],
    "appliesTo": [
      "urn:csabs:concept/GCM"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial mathematics; not a machine-checked proof.",
    "source": [
      "urn:csabs:source/nist-sp800-38d"
    ],
    "sourceLocator": "Sections 5.1–5.2, 6.2, 6.5, 7.1–7.2, 8; Appendices A, B and D",
    "sourceNote": "Explicit restricted profile using detached (C,T) output. Nonce uniqueness is a usage obligation; computational security is not asserted as a defining equation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/GCM-nonce-discipline",
    "type": "Axiom",
    "name": "nonce-discipline",
    "statement": "Encryption invocations under a fixed key use distinct IVs in the selected deterministic uniqueness discipline.",
    "formalStatement": "For distinct encryption invocations i≠j: k_i=k_j ⇒ IV_i≠IV_j; this includes concurrent writers, restarts and devices sharing a key.",
    "assumptions": [
      "Selected deterministic nonce discipline, stronger than SP 800-38D §8’s probabilistic collision requirement. Not a constraint on repeated decryption or the mathematical evaluation of seal."
    ],
    "appliesTo": [
      "urn:csabs:concept/GCM"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial mathematics; not a machine-checked proof.",
    "source": [
      "urn:csabs:source/nist-sp800-38d"
    ],
    "sourceLocator": "Section 8 and Appendix A",
    "sourceNote": "Explicit restricted profile using detached (C,T) output. Nonce uniqueness is a usage obligation; computational security is not asserted as a defining equation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:theorem/GCM-round-trip",
    "type": "Theorem",
    "name": "round-trip",
    "statement": "GCM decryption recovers an honestly encrypted message.",
    "formalStatement": "seal(k,IV,A,P)=(C,T) ⇒ open(k,IV,A,C,T)=inl(P).",
    "assumptions": [
      "Selected byte-oriented 96-bit-IV, 128-bit-tag profile of SP 800-38D. Underlying block cipher E has 128-bit blocks. K is its key carrier; IV is exactly 12 bytes; 0≤|P|≤2^36−32 bytes and 0≤|A|≤2^61−1 bytes. Ciphertext has |P| bytes, tag has 16 bytes. len denotes bits in equations; |·| denotes bytes. Empty P and A are valid. Equality is exact bit strings; [x]_s is unsigned big-endian encoding, while GHASH has its own polynomial coefficient order. Other IV/tag lengths require explicit variants. No padding is added to the returned plaintext or ciphertext."
    ],
    "appliesTo": [
      "urn:csabs:concept/GCM"
    ],
    "ruleRole": "derived-result",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial mathematics; not a machine-checked proof.",
    "source": [
      "urn:csabs:source/nist-sp800-38d"
    ],
    "sourceLocator": "Sections 5.1–5.2, 6.2, 6.5, 7.1–7.2, 8; Appendices A, B and D",
    "sourceNote": "Editorial derivation from the linked premises. Explicit restricted profile using detached (C,T) output. Nonce uniqueness is a usage obligation; computational security is not asserted as a defining equation.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/GCM-counter-transform",
      "urn:csabs:axiom/GCM-encryption",
      "urn:csabs:axiom/GCM-authenticated-decryption"
    ],
    "proofSketch": "The same IV gives the same J₀, counters and H. Recomputed S gives the original T. Applying GCTR twice XORs the same keystream twice, recovering every input byte, including the empty case. Freshness is unnecessary for this functional equality, but necessary for secure use."
  },
  {
    "id": "urn:csabs:theorem/GCM-reused-nonce-xor",
    "type": "Theorem",
    "name": "reused-nonce-xor",
    "statement": "Nonce reuse exposes the XOR of equal-length plaintexts.",
    "formalStatement": "seal(k,IV,A₁,P₁)=(C₁,T₁) ∧ seal(k,IV,A₂,P₂)=(C₂,T₂) ∧ len(P₁)=len(P₂) ⇒ C₁⊕C₂=P₁⊕P₂.",
    "assumptions": [
      "Counterfactual repeated-IV evaluations of the deterministic encryption function; they violate the secure-use nonce discipline. Equal-length admissible plaintexts."
    ],
    "appliesTo": [
      "urn:csabs:concept/GCM"
    ],
    "ruleRole": "derived-result",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial mathematics; not a machine-checked proof.",
    "source": [
      "urn:csabs:source/nist-sp800-38d"
    ],
    "sourceLocator": "Sections 6.5 and 7.1; Appendix A",
    "sourceNote": "Editorial derivation from the linked premises. Explicit restricted profile using detached (C,T) output. Nonce uniqueness is a usage obligation; computational security is not asserted as a defining equation.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/GCM-counter-transform",
      "urn:csabs:axiom/GCM-encryption"
    ],
    "proofSketch": "Both ciphertexts use the same counter keystream Z, independently of AAD. Cancel Z from (P₁⊕Z)⊕(P₂⊕Z). This is a confidentiality failure, not a proof of a complete authentication attack."
  }
]
```
<!-- graph-record:end -->
