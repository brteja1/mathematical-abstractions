# Nonce-based authenticated encryption with associated data

A deterministic nonce-based interface that encrypts a plaintext while authenticating it and additional unencrypted data, and decrypts to a plaintext or a distinct failure result.

**Notation:** seal : K×N×A×P → W; open : K×N×A×W → P⊎{FAIL}.

**Stable ID:** `urn:csabs:concept/AEAD`

**Categories:** Cryptography → Symmetric cryptography

**Kind:** semantic-model

**Prerequisites:** [Finite sequence (List datatype)](Sequence.md), [Option Type](OptionType.md)

## Backlinks

- [Galois/Counter Mode (96-bit IV, 128-bit tag profile)](GCM.md) — `requiresConcept`
- [Galois/Counter Mode (96-bit IV, 128-bit tag profile)](GCM.md) — `specializationOf`

## Interface and scope

**axiomBasis:** Algorithm-specific admissible domains; deterministic seal/open; correctness and all-or-failure output.

**basisKind:** defined-structure

**basisScope:** Selected deterministic, externally supplied nonempty-nonce profile of RFC 5116; randomized/stateful zero-nonce variants are excluded. K,N,A,P,W are algorithm-defined byte-string domains; A and P admit empty strings. Equality is exact bytes. FAIL is distinct from the successful empty plaintext. Nonces must be distinct for encryption under one key across all writers; repetition during decryption is allowed.

**verificationObligation:** Map byte and bit order, exact lengths, equality, errors and key handling explicitly. Functional equations alone do not establish computational security or resistance to side channels.; Correctness and a failure output do not imply unforgeability: a separate adversary model, key-generation assumptions and quantitative bounds are needed. Do not assume every changed nonce, AAD, ciphertext or tag necessarily causes rejection; collisions and successful forgery have nonzero probability. Anti-replay is a protocol obligation.

**reviewStatus:** Editorial specification; no cryptographic security proof or compiled claim witness.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-AEAD-seal"></a>

### seal

`urn:csabs:operation/AEAD-seal`

**signature:** seal : K×N×A×P → W

**description:** Encrypt and authenticate the provided inputs.

**precondition:** Admissible key/nonce/data lengths; a fresh nonce for secure use under k.

**postcondition:** Return the complete authenticated ciphertext W; associated data is not encrypted.

**totality:** total on the stated precondition; outside the domain return an input error without partial output

**source:** [RFC 5116: An Interface and Algorithms for Authenticated Encryption](https://www.rfc-editor.org/rfc/rfc5116.html); accessedOn: 2026-11-10; sourceRole: primary normative specification

**sourceLocator:** Sections 1.2, 2.1, 2.2, 3.1 and 4

**sourceNote:** Restricts the general RFC interface to deterministic nonce-based algorithms; W includes the authentication tag and its encoding is algorithm-specific.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-AEAD-open"></a>

### open

`urn:csabs:operation/AEAD-open`

**signature:** open : K×N×A×W → P⊎{FAIL}

**description:** Authenticate and decrypt, returning no partial plaintext on failure.

**precondition:** Admissible inputs; malformed encodings produce an input error or FAIL without plaintext.

**postcondition:** Return P on successful authentication; otherwise FAIL. No caller-visible tentative plaintext.

**totality:** total on the stated precondition; outside the domain return an input error without partial output

**source:** [RFC 5116: An Interface and Algorithms for Authenticated Encryption](https://www.rfc-editor.org/rfc/rfc5116.html); accessedOn: 2026-11-10; sourceRole: primary normative specification

**sourceLocator:** Sections 1.2, 2.1, 2.2, 3.1 and 4

**sourceNote:** Restricts the general RFC interface to deterministic nonce-based algorithms; W includes the authentication tag and its encoding is algorithm-specific.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-AEAD-correctness"></a>

### correctness

`urn:csabs:axiom/AEAD-correctness`

**statement:** An honestly produced authenticated ciphertext decrypts correctly.

**formalStatement:** open(k,n,a,seal(k,n,a,p))=inl(p).

**assumptions:** Selected deterministic, externally supplied nonempty-nonce profile of RFC 5116; randomized/stateful zero-nonce variants are excluded. K,N,A,P,W are algorithm-defined byte-string domains; A and P admit empty strings. Equality is exact bytes. FAIL is distinct from the successful empty plaintext. Nonces must be distinct for encryption under one key across all writers; repetition during decryption is allowed.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial mathematics; not a machine-checked proof.

**source:** [RFC 5116: An Interface and Algorithms for Authenticated Encryption](https://www.rfc-editor.org/rfc/rfc5116.html); accessedOn: 2026-11-10; sourceRole: primary normative specification

**sourceLocator:** Sections 1.2, 2.1, 2.2, 3.1 and 4

**sourceNote:** Restricts the general RFC interface to deterministic nonce-based algorithms; W includes the authentication tag and its encoding is algorithm-specific.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-AEAD-failure-interface"></a>

### failure-interface

`urn:csabs:axiom/AEAD-failure-interface`

**statement:** Authentication failure is a distinct result with no plaintext output.

**formalStatement:** open(k,n,a,w)∈{inl(p) | p∈P}∪{FAIL}; FAIL≠inl(ε).

**assumptions:** Selected deterministic, externally supplied nonempty-nonce profile of RFC 5116; randomized/stateful zero-nonce variants are excluded. K,N,A,P,W are algorithm-defined byte-string domains; A and P admit empty strings. Equality is exact bytes. FAIL is distinct from the successful empty plaintext. Nonces must be distinct for encryption under one key across all writers; repetition during decryption is allowed.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial mathematics; not a machine-checked proof.

**source:** [RFC 5116: An Interface and Algorithms for Authenticated Encryption](https://www.rfc-editor.org/rfc/rfc5116.html); accessedOn: 2026-11-10; sourceRole: primary normative specification

**sourceLocator:** Sections 1.2, 2.1, 2.2, 3.1 and 4

**sourceNote:** Restricts the general RFC interface to deterministic nonce-based algorithms; W includes the authentication tag and its encoding is algorithm-specific.

**provenanceKind:** adapted

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-AEAD-fixed-input-injective"></a>

### fixed-input-injective

`urn:csabs:theorem/AEAD-fixed-input-injective`

**statement:** For fixed key, nonce and associated data, seal is injective in plaintext.

**formalStatement:** seal(k,n,a,p)=seal(k,n,a,q) ⇒ p=q.

**assumptions:** Admissible deterministic AEAD inputs and the correctness equation. This compares mathematical evaluations; it does not authorize nonce reuse in encryption.

**ruleRole:** derived-result

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial mathematics; not a machine-checked proof.

**source:** [RFC 5116: An Interface and Algorithms for Authenticated Encryption](https://www.rfc-editor.org/rfc/rfc5116.html); accessedOn: 2026-11-10; sourceRole: primary normative specification

**sourceLocator:** Sections 2.1–2.2

**sourceNote:** Editorial consequence of deterministic authenticated decryption and correctness; this is not an unforgeability claim.

**provenanceKind:** derived

**dependsOn:** [correctness](AEAD.md#node-urn-csabs-axiom-AEAD-correctness)

**proofSketch:** Apply open(k,n,a,−) to both sides. Correctness gives inl(p)=inl(q); injectivity of the successful-result constructor gives p=q.

## Concept provenance

- [RFC 5116: An Interface and Algorithms for Authenticated Encryption](https://www.rfc-editor.org/rfc/rfc5116.html); accessedOn: 2026-11-10; sourceRole: primary normative specification

**sourceLocator:** Sections 1.2, 2.1, 2.2, 3.1 and 4

**sourceNote:** Restricts the general RFC interface to deterministic nonce-based algorithms; W includes the authentication tag and its encoding is algorithm-specific.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/AEAD",
    "type": "Concept",
    "shortForm": "AEAD",
    "fullName": "Nonce-based authenticated encryption with associated data",
    "definition": "A deterministic nonce-based interface that encrypts a plaintext while authenticating it and additional unencrypted data, and decrypts to a plaintext or a distinct failure result.",
    "notation": "seal : K×N×A×P → W; open : K×N×A×W → P⊎{FAIL}.",
    "category": [
      "urn:csabs:category/symmetric-cryptography"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "requiresConcept": [
      "urn:csabs:concept/Sequence",
      "urn:csabs:concept/OptionType"
    ],
    "axiomBasis": "Algorithm-specific admissible domains; deterministic seal/open; correctness and all-or-failure output.",
    "basisKind": "defined-structure",
    "basisScope": "Selected deterministic, externally supplied nonempty-nonce profile of RFC 5116; randomized/stateful zero-nonce variants are excluded. K,N,A,P,W are algorithm-defined byte-string domains; A and P admit empty strings. Equality is exact bytes. FAIL is distinct from the successful empty plaintext. Nonces must be distinct for encryption under one key across all writers; repetition during decryption is allowed.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial specification; no cryptographic security proof or compiled claim witness.",
    "verificationObligation": [
      "Map byte and bit order, exact lengths, equality, errors and key handling explicitly. Functional equations alone do not establish computational security or resistance to side channels.",
      "Correctness and a failure output do not imply unforgeability: a separate adversary model, key-generation assumptions and quantitative bounds are needed. Do not assume every changed nonce, AAD, ciphertext or tag necessarily causes rejection; collisions and successful forgery have nonzero probability. Anti-replay is a protocol obligation."
    ],
    "hasOperation": [
      "urn:csabs:operation/AEAD-seal",
      "urn:csabs:operation/AEAD-open"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/AEAD-correctness",
      "urn:csabs:axiom/AEAD-failure-interface"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/AEAD-fixed-input-injective"
    ],
    "source": [
      "urn:csabs:source/rfc5116"
    ],
    "sourceLocator": "Sections 1.2, 2.1, 2.2, 3.1 and 4",
    "sourceNote": "Restricts the general RFC interface to deterministic nonce-based algorithms; W includes the authentication tag and its encoding is algorithm-specific.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/AEAD-seal",
    "type": "Operation",
    "name": "seal",
    "signature": "seal : K×N×A×P → W",
    "description": "Encrypt and authenticate the provided inputs.",
    "precondition": "Admissible key/nonce/data lengths; a fresh nonce for secure use under k.",
    "postcondition": "Return the complete authenticated ciphertext W; associated data is not encrypted.",
    "totality": "total on the stated precondition; outside the domain return an input error without partial output",
    "concept": "urn:csabs:concept/AEAD",
    "source": [
      "urn:csabs:source/rfc5116"
    ],
    "sourceLocator": "Sections 1.2, 2.1, 2.2, 3.1 and 4",
    "sourceNote": "Restricts the general RFC interface to deterministic nonce-based algorithms; W includes the authentication tag and its encoding is algorithm-specific.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/AEAD-open",
    "type": "Operation",
    "name": "open",
    "signature": "open : K×N×A×W → P⊎{FAIL}",
    "description": "Authenticate and decrypt, returning no partial plaintext on failure.",
    "precondition": "Admissible inputs; malformed encodings produce an input error or FAIL without plaintext.",
    "postcondition": "Return P on successful authentication; otherwise FAIL. No caller-visible tentative plaintext.",
    "totality": "total on the stated precondition; outside the domain return an input error without partial output",
    "concept": "urn:csabs:concept/AEAD",
    "source": [
      "urn:csabs:source/rfc5116"
    ],
    "sourceLocator": "Sections 1.2, 2.1, 2.2, 3.1 and 4",
    "sourceNote": "Restricts the general RFC interface to deterministic nonce-based algorithms; W includes the authentication tag and its encoding is algorithm-specific.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/AEAD-correctness",
    "type": "Axiom",
    "name": "correctness",
    "statement": "An honestly produced authenticated ciphertext decrypts correctly.",
    "formalStatement": "open(k,n,a,seal(k,n,a,p))=inl(p).",
    "assumptions": [
      "Selected deterministic, externally supplied nonempty-nonce profile of RFC 5116; randomized/stateful zero-nonce variants are excluded. K,N,A,P,W are algorithm-defined byte-string domains; A and P admit empty strings. Equality is exact bytes. FAIL is distinct from the successful empty plaintext. Nonces must be distinct for encryption under one key across all writers; repetition during decryption is allowed."
    ],
    "appliesTo": [
      "urn:csabs:concept/AEAD"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial mathematics; not a machine-checked proof.",
    "source": [
      "urn:csabs:source/rfc5116"
    ],
    "sourceLocator": "Sections 1.2, 2.1, 2.2, 3.1 and 4",
    "sourceNote": "Restricts the general RFC interface to deterministic nonce-based algorithms; W includes the authentication tag and its encoding is algorithm-specific.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/AEAD-failure-interface",
    "type": "Axiom",
    "name": "failure-interface",
    "statement": "Authentication failure is a distinct result with no plaintext output.",
    "formalStatement": "open(k,n,a,w)∈{inl(p) | p∈P}∪{FAIL}; FAIL≠inl(ε).",
    "assumptions": [
      "Selected deterministic, externally supplied nonempty-nonce profile of RFC 5116; randomized/stateful zero-nonce variants are excluded. K,N,A,P,W are algorithm-defined byte-string domains; A and P admit empty strings. Equality is exact bytes. FAIL is distinct from the successful empty plaintext. Nonces must be distinct for encryption under one key across all writers; repetition during decryption is allowed."
    ],
    "appliesTo": [
      "urn:csabs:concept/AEAD"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial mathematics; not a machine-checked proof.",
    "source": [
      "urn:csabs:source/rfc5116"
    ],
    "sourceLocator": "Sections 1.2, 2.1, 2.2, 3.1 and 4",
    "sourceNote": "Restricts the general RFC interface to deterministic nonce-based algorithms; W includes the authentication tag and its encoding is algorithm-specific.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:theorem/AEAD-fixed-input-injective",
    "type": "Theorem",
    "name": "fixed-input-injective",
    "statement": "For fixed key, nonce and associated data, seal is injective in plaintext.",
    "formalStatement": "seal(k,n,a,p)=seal(k,n,a,q) ⇒ p=q.",
    "assumptions": [
      "Admissible deterministic AEAD inputs and the correctness equation. This compares mathematical evaluations; it does not authorize nonce reuse in encryption."
    ],
    "appliesTo": [
      "urn:csabs:concept/AEAD"
    ],
    "ruleRole": "derived-result",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial mathematics; not a machine-checked proof.",
    "source": [
      "urn:csabs:source/rfc5116"
    ],
    "sourceLocator": "Sections 2.1–2.2",
    "sourceNote": "Editorial consequence of deterministic authenticated decryption and correctness; this is not an unforgeability claim.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/AEAD-correctness"
    ],
    "proofSketch": "Apply open(k,n,a,−) to both sides. Correctness gives inl(p)=inl(q); injectivity of the successful-result constructor gives p=q."
  }
]
```
<!-- graph-record:end -->
