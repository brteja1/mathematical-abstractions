# Diffie–Hellman key exchange (prime-order cyclic-group core)

Two parties combine private exponents and exchanged group elements to obtain the same shared group element; this is the algebraic core of unauthenticated key agreement.

**Notation:** A=g^a; B=g^b; Z=B^a=A^b=g^(ab).

**Stable ID:** `urn:csabs:concept/DiffieHellman`

**Categories:** Cryptography → Public-key cryptography

**Kind:** Mathematical construction

**Prerequisites:** [Group](Group.md)

## Backlinks

- [Elliptic curve Diffie–Hellman (validated full-point profile)](ECDH.md) — `requiresConcept`
- [Elliptic curve Diffie–Hellman (validated full-point profile)](ECDH.md) — `specializationOf`

## Mathematical formulation

The partial group interface stores g∈H and a natural subgroupOrder parameter; publicValue(a)=g^a for a∈ℕ. The model does not enforce that g generates a prime-order subgroup or that secrets/peer values are valid.

**Lean formulation** (in its source module context):

```lean
structure DiffieHellmanInterface (H : Type) [Group H] where
  generator : H
  subgroupOrder : Nat
```

**Source:** [`Catalog.DiffieHellmanInterface`](../lean/Catalog/Cryptography.lean); consulted 2026-11-12.

**Scope:** partial

**Interpretation:** Group H with an explicit generator and subgroupOrder; publicValue uses natural group power and Lean equality.

**Limits:** Does not enforce finite prime order, generator order, secret range, subgroup membership, sampling, shared-secret agreement, encodings, KDF or authentication.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** An explicit prime-order cyclic group, exponentiation by repeated group multiplication, public-key and shared-element equations, and public-input membership checks.

**basisKind:** defined-structure

**basisScope:** Fix a finite cyclic group H=⟨g⟩ of prime order q≥2 with identity 1_H. Secret scalars a,b range over S={1,…,q−1}; public inputs are H\{1_H}. Equality is group-element equality, independent of wire representation. Operations are deterministic for supplied scalars; independent uniform sampling on S is required for the selected key-generation model. No KDF, transcript authentication, key confirmation or wire encoding is specified. A finite-field instance has H≤𝔽_p×, q dividing p−1, and g of exact order q; ECDH supplies an additive instance.

**verificationObligation:** Map representations, equality, parameter validation and failure behavior explicitly. Exact arithmetic has no overflow or rounding. Functional equations do not establish cryptographic security, entropy quality, constant-time behavior or secret erasure.

**reviewStatus:** Editorial mathematics; no compiled claim witness or cryptographic security proof.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-DiffieHellman-public"></a>

### public

`urn:csabs:operation/DiffieHellman-public`

**source:** [RFC 2631: Diffie-Hellman Key Agreement Method](https://www.rfc-editor.org/rfc/rfc2631.txt); accessedOn: 2026-11-11; sourceRole: primary algorithm specification; [RFC 6090: Fundamental Elliptic Curve Cryptography Algorithms](https://www.rfc-editor.org/rfc/rfc6090.txt); accessedOn: 2026-11-11; sourceRole: primary algorithm specification

**sourceLocator:** RFC 2631 §§2.1.1, 2.1.5, 2.2; RFC 6090 §§2.2, 4, 10.2

**sourceNote:** Generalizes the finite-field equations to a cyclic group; restricts to prime order and nonzero secrets. Historical parameter sizes and SHA-1 KDF are not adopted.

**provenanceKind:** adapted

**signature:** public : S → H\{1_H}

**description:** Construct a public group element from a private exponent.

**precondition:** Valid common parameters and a∈S.

**postcondition:** public(a)=g^a.

**totality:** Total on the stated mathematical domain; malformed or out-of-domain external input is rejected without a result.

<a id="node-urn-csabs-operation-DiffieHellman-validate"></a>

### validate

`urn:csabs:operation/DiffieHellman-validate`

**source:** [RFC 2631: Diffie-Hellman Key Agreement Method](https://www.rfc-editor.org/rfc/rfc2631.txt); accessedOn: 2026-11-11; sourceRole: primary algorithm specification; [RFC 6090: Fundamental Elliptic Curve Cryptography Algorithms](https://www.rfc-editor.org/rfc/rfc6090.txt); accessedOn: 2026-11-11; sourceRole: primary algorithm specification

**sourceLocator:** RFC 2631 §§2.1.1, 2.1.5, 2.2; RFC 6090 §§2.2, 4, 10.2

**sourceNote:** Generalizes the finite-field equations to a cyclic group; restricts to prime order and nonzero secrets. Historical parameter sizes and SHA-1 KDF are not adopted.

**provenanceKind:** adapted

**signature:** validate : U → Bool

**description:** Validate a decoded candidate from an ambient carrier U containing H.

**precondition:** Parameters fixed; decoding has already succeeded.

**postcondition:** true iff Y∈H and Y≠1_H. For a finite-field instance: 2≤Y≤p−1 and Y^q≡1 mod p.

**totality:** Total on the stated mathematical domain; malformed or out-of-domain external input is rejected without a result.

<a id="node-urn-csabs-operation-DiffieHellman-share"></a>

### share

`urn:csabs:operation/DiffieHellman-share`

**source:** [RFC 2631: Diffie-Hellman Key Agreement Method](https://www.rfc-editor.org/rfc/rfc2631.txt); accessedOn: 2026-11-11; sourceRole: primary algorithm specification; [RFC 6090: Fundamental Elliptic Curve Cryptography Algorithms](https://www.rfc-editor.org/rfc/rfc6090.txt); accessedOn: 2026-11-11; sourceRole: primary algorithm specification

**sourceLocator:** RFC 2631 §§2.1.1, 2.1.5, 2.2; RFC 6090 §§2.2, 4, 10.2

**sourceNote:** Generalizes the finite-field equations to a cyclic group; restricts to prime order and nonzero secrets. Historical parameter sizes and SHA-1 KDF are not adopted.

**provenanceKind:** adapted

**signature:** share : S×(H\{1_H}) → H\{1_H}

**description:** Compute the shared group element with a validated peer public key.

**precondition:** a∈S; Y belongs to the same H and is nonidentity.

**postcondition:** share(a,Y)=Y^a.

**totality:** Total on the stated mathematical domain; malformed or out-of-domain external input is rejected without a result.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-DiffieHellman-group-power"></a>

### group-power

`urn:csabs:axiom/DiffieHellman-group-power`

**source:** [RFC 2631: Diffie-Hellman Key Agreement Method](https://www.rfc-editor.org/rfc/rfc2631.txt); accessedOn: 2026-11-11; sourceRole: primary algorithm specification; [RFC 6090: Fundamental Elliptic Curve Cryptography Algorithms](https://www.rfc-editor.org/rfc/rfc6090.txt); accessedOn: 2026-11-11; sourceRole: primary algorithm specification

**sourceLocator:** RFC 2631 §§2.1.1, 2.1.5, 2.2; RFC 6090 §§2.2, 4, 10.2

**sourceNote:** Generalizes the finite-field equations to a cyclic group; restricts to prime order and nonzero secrets. Historical parameter sizes and SHA-1 KDF are not adopted.

**provenanceKind:** adapted

**statement:** Powers are repeated multiplication in the selected cyclic group.

**formalStatement:** H is a group; ord(g)=q prime; H={g^i | 0≤i<q}; X^0=1_H; X^(i+1)=X^i·X (i≥0).

**assumptions:** Fix a finite cyclic group H=⟨g⟩ of prime order q≥2 with identity 1_H. Secret scalars a,b range over S={1,…,q−1}; public inputs are H\{1_H}. Equality is group-element equality, independent of wire representation. Operations are deterministic for supplied scalars; independent uniform sampling on S is required for the selected key-generation model. No KDF, transcript authentication, key confirmation or wire encoding is specified. A finite-field instance has H≤𝔽_p×, q dividing p−1, and g of exact order q; ECDH supplies an additive instance.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial statement and proof sketch; not machine-checked.

<a id="node-urn-csabs-axiom-DiffieHellman-exchange"></a>

### exchange

`urn:csabs:axiom/DiffieHellman-exchange`

**source:** [RFC 2631: Diffie-Hellman Key Agreement Method](https://www.rfc-editor.org/rfc/rfc2631.txt); accessedOn: 2026-11-11; sourceRole: primary algorithm specification; [RFC 6090: Fundamental Elliptic Curve Cryptography Algorithms](https://www.rfc-editor.org/rfc/rfc6090.txt); accessedOn: 2026-11-11; sourceRole: primary algorithm specification

**sourceLocator:** RFC 2631 §§2.1.1, 2.1.5, 2.2; RFC 6090 §§2.2, 4, 10.2

**sourceNote:** Generalizes the finite-field equations to a cyclic group; restricts to prime order and nonzero secrets. Historical parameter sizes and SHA-1 KDF are not adopted.

**provenanceKind:** adapted

**statement:** Public and shared values use the same group and exponent action.

**formalStatement:** public(a)=g^a; share(a,Y)=Y^a; validate(Y) ⇔ Y∈H\{1_H}.

**assumptions:** Fix a finite cyclic group H=⟨g⟩ of prime order q≥2 with identity 1_H. Secret scalars a,b range over S={1,…,q−1}; public inputs are H\{1_H}. Equality is group-element equality, independent of wire representation. Operations are deterministic for supplied scalars; independent uniform sampling on S is required for the selected key-generation model. No KDF, transcript authentication, key confirmation or wire encoding is specified. A finite-field instance has H≤𝔽_p×, q dividing p−1, and g of exact order q; ECDH supplies an additive instance.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial statement and proof sketch; not machine-checked.

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-DiffieHellman-agreement"></a>

### agreement

`urn:csabs:theorem/DiffieHellman-agreement`

**source:** [RFC 2631: Diffie-Hellman Key Agreement Method](https://www.rfc-editor.org/rfc/rfc2631.txt); accessedOn: 2026-11-11; sourceRole: primary algorithm specification; [RFC 6090: Fundamental Elliptic Curve Cryptography Algorithms](https://www.rfc-editor.org/rfc/rfc6090.txt); accessedOn: 2026-11-11; sourceRole: primary algorithm specification

**sourceLocator:** RFC 2631 §§2.1.1, 2.1.5, 2.2; RFC 6090 §§2.2, 4, 10.2

**sourceNote:** Editorial consequence of the explicitly linked premises. Generalizes the finite-field equations to a cyclic group; restricts to prime order and nonzero secrets. Historical parameter sizes and SHA-1 KDF are not adopted.

**provenanceKind:** derived

**statement:** Honest participants obtain the same nonidentity group element.

**formalStatement:** share(a,public(b))=g^(ab)=share(b,public(a))≠1_H.

**dependsOn:** [group-power](DiffieHellman.md#node-urn-csabs-axiom-DiffieHellman-group-power); [exchange](DiffieHellman.md#node-urn-csabs-axiom-DiffieHellman-exchange)

**proofSketch:** Associativity gives (g^b)^a=g^(ba); integer multiplication commutes. Since q is prime and neither a nor b is zero modulo q, q does not divide ab, so the result is nonidentity.

**assumptions:** Fix a finite cyclic group H=⟨g⟩ of prime order q≥2 with identity 1_H. Secret scalars a,b range over S={1,…,q−1}; public inputs are H\{1_H}. Equality is group-element equality, independent of wire representation. Operations are deterministic for supplied scalars; independent uniform sampling on S is required for the selected key-generation model. No KDF, transcript authentication, key confirmation or wire encoding is specified. A finite-field instance has H≤𝔽_p×, q dividing p−1, and g of exact order q; ECDH supplies an additive instance.

**ruleRole:** derived-result

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial statement and proof sketch; not machine-checked.

## Concept provenance

- [RFC 2631: Diffie-Hellman Key Agreement Method](https://www.rfc-editor.org/rfc/rfc2631.txt); accessedOn: 2026-11-11; sourceRole: primary algorithm specification
- [RFC 6090: Fundamental Elliptic Curve Cryptography Algorithms](https://www.rfc-editor.org/rfc/rfc6090.txt); accessedOn: 2026-11-11; sourceRole: primary algorithm specification

**sourceLocator:** RFC 2631 §§2.1.1, 2.1.5, 2.2; RFC 6090 §§2.2, 4, 10.2

**sourceNote:** Generalizes the finite-field equations to a cyclic group; restricts to prime order and nonzero secrets. Historical parameter sizes and SHA-1 KDF are not adopted.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/DiffieHellman",
    "type": "Concept",
    "shortForm": "DiffieHellman",
    "fullName": "Diffie–Hellman key exchange (prime-order cyclic-group core)",
    "definition": "Two parties combine private exponents and exchanged group elements to obtain the same shared group element; this is the algebraic core of unauthenticated key agreement.",
    "notation": "A=g^a; B=g^b; Z=B^a=A^b=g^(ab).",
    "category": [
      "urn:csabs:category/public-key-cryptography"
    ],
    "kind": "urn:csabs:kind/construction",
    "requiresConcept": [
      "urn:csabs:concept/Group"
    ],
    "axiomBasis": "An explicit prime-order cyclic group, exponentiation by repeated group multiplication, public-key and shared-element equations, and public-input membership checks.",
    "basisKind": "defined-structure",
    "basisScope": "Fix a finite cyclic group H=⟨g⟩ of prime order q≥2 with identity 1_H. Secret scalars a,b range over S={1,…,q−1}; public inputs are H\\{1_H}. Equality is group-element equality, independent of wire representation. Operations are deterministic for supplied scalars; independent uniform sampling on S is required for the selected key-generation model. No KDF, transcript authentication, key confirmation or wire encoding is specified. A finite-field instance has H≤𝔽_p×, q dividing p−1, and g of exact order q; ECDH supplies an additive instance.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial mathematics; no compiled claim witness or cryptographic security proof.",
    "verificationObligation": [
      "Map representations, equality, parameter validation and failure behavior explicitly. Exact arithmetic has no overflow or rounding. Functional equations do not establish cryptographic security, entropy quality, constant-time behavior or secret erasure."
    ],
    "source": [
      "urn:csabs:source/rfc2631",
      "urn:csabs:source/rfc6090"
    ],
    "sourceLocator": "RFC 2631 §§2.1.1, 2.1.5, 2.2; RFC 6090 §§2.2, 4, 10.2",
    "sourceNote": "Generalizes the finite-field equations to a cyclic group; restricts to prime order and nonzero secrets. Historical parameter sizes and SHA-1 KDF are not adopted.",
    "provenanceKind": "adapted",
    "hasOperation": [
      "urn:csabs:operation/DiffieHellman-public",
      "urn:csabs:operation/DiffieHellman-validate",
      "urn:csabs:operation/DiffieHellman-share"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/DiffieHellman-group-power",
      "urn:csabs:axiom/DiffieHellman-exchange"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/DiffieHellman-agreement"
    ],
    "hasLaw": [],
    "leanFormulation": "structure DiffieHellmanInterface (H : Type) [Group H] where\n  generator : H\n  subgroupOrder : Nat",
    "formulationSource": "urn:csabs:source/local-lean-Cryptography",
    "formulationLocator": "Catalog.DiffieHellmanInterface",
    "formulationScope": "partial",
    "leanModelMapping": "Group H with an explicit generator and subgroupOrder; publicValue uses natural group power and Lean equality.",
    "leanModelLimitations": "Does not enforce finite prime order, generator order, secret range, subgroup membership, sampling, shared-secret agreement, encodings, KDF or authentication.",
    "mathematicalFormulation": "The partial group interface stores g∈H and a natural subgroupOrder parameter; publicValue(a)=g^a for a∈ℕ. The model does not enforce that g generates a prime-order subgroup or that secrets/peer values are valid."
  },
  {
    "id": "urn:csabs:operation/DiffieHellman-public",
    "type": "Operation",
    "name": "public",
    "source": [
      "urn:csabs:source/rfc2631",
      "urn:csabs:source/rfc6090"
    ],
    "sourceLocator": "RFC 2631 §§2.1.1, 2.1.5, 2.2; RFC 6090 §§2.2, 4, 10.2",
    "sourceNote": "Generalizes the finite-field equations to a cyclic group; restricts to prime order and nonzero secrets. Historical parameter sizes and SHA-1 KDF are not adopted.",
    "provenanceKind": "adapted",
    "signature": "public : S → H\\{1_H}",
    "description": "Construct a public group element from a private exponent.",
    "precondition": "Valid common parameters and a∈S.",
    "postcondition": "public(a)=g^a.",
    "concept": "urn:csabs:concept/DiffieHellman",
    "totality": "Total on the stated mathematical domain; malformed or out-of-domain external input is rejected without a result."
  },
  {
    "id": "urn:csabs:operation/DiffieHellman-validate",
    "type": "Operation",
    "name": "validate",
    "source": [
      "urn:csabs:source/rfc2631",
      "urn:csabs:source/rfc6090"
    ],
    "sourceLocator": "RFC 2631 §§2.1.1, 2.1.5, 2.2; RFC 6090 §§2.2, 4, 10.2",
    "sourceNote": "Generalizes the finite-field equations to a cyclic group; restricts to prime order and nonzero secrets. Historical parameter sizes and SHA-1 KDF are not adopted.",
    "provenanceKind": "adapted",
    "signature": "validate : U → Bool",
    "description": "Validate a decoded candidate from an ambient carrier U containing H.",
    "precondition": "Parameters fixed; decoding has already succeeded.",
    "postcondition": "true iff Y∈H and Y≠1_H. For a finite-field instance: 2≤Y≤p−1 and Y^q≡1 mod p.",
    "concept": "urn:csabs:concept/DiffieHellman",
    "totality": "Total on the stated mathematical domain; malformed or out-of-domain external input is rejected without a result."
  },
  {
    "id": "urn:csabs:operation/DiffieHellman-share",
    "type": "Operation",
    "name": "share",
    "source": [
      "urn:csabs:source/rfc2631",
      "urn:csabs:source/rfc6090"
    ],
    "sourceLocator": "RFC 2631 §§2.1.1, 2.1.5, 2.2; RFC 6090 §§2.2, 4, 10.2",
    "sourceNote": "Generalizes the finite-field equations to a cyclic group; restricts to prime order and nonzero secrets. Historical parameter sizes and SHA-1 KDF are not adopted.",
    "provenanceKind": "adapted",
    "signature": "share : S×(H\\{1_H}) → H\\{1_H}",
    "description": "Compute the shared group element with a validated peer public key.",
    "precondition": "a∈S; Y belongs to the same H and is nonidentity.",
    "postcondition": "share(a,Y)=Y^a.",
    "concept": "urn:csabs:concept/DiffieHellman",
    "totality": "Total on the stated mathematical domain; malformed or out-of-domain external input is rejected without a result."
  },
  {
    "id": "urn:csabs:axiom/DiffieHellman-group-power",
    "type": "Axiom",
    "name": "group-power",
    "source": [
      "urn:csabs:source/rfc2631",
      "urn:csabs:source/rfc6090"
    ],
    "sourceLocator": "RFC 2631 §§2.1.1, 2.1.5, 2.2; RFC 6090 §§2.2, 4, 10.2",
    "sourceNote": "Generalizes the finite-field equations to a cyclic group; restricts to prime order and nonzero secrets. Historical parameter sizes and SHA-1 KDF are not adopted.",
    "provenanceKind": "adapted",
    "statement": "Powers are repeated multiplication in the selected cyclic group.",
    "formalStatement": "H is a group; ord(g)=q prime; H={g^i | 0≤i<q}; X^0=1_H; X^(i+1)=X^i·X (i≥0).",
    "appliesTo": [
      "urn:csabs:concept/DiffieHellman"
    ],
    "assumptions": [
      "Fix a finite cyclic group H=⟨g⟩ of prime order q≥2 with identity 1_H. Secret scalars a,b range over S={1,…,q−1}; public inputs are H\\{1_H}. Equality is group-element equality, independent of wire representation. Operations are deterministic for supplied scalars; independent uniform sampling on S is required for the selected key-generation model. No KDF, transcript authentication, key confirmation or wire encoding is specified. A finite-field instance has H≤𝔽_p×, q dividing p−1, and g of exact order q; ECDH supplies an additive instance."
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial statement and proof sketch; not machine-checked."
  },
  {
    "id": "urn:csabs:axiom/DiffieHellman-exchange",
    "type": "Axiom",
    "name": "exchange",
    "source": [
      "urn:csabs:source/rfc2631",
      "urn:csabs:source/rfc6090"
    ],
    "sourceLocator": "RFC 2631 §§2.1.1, 2.1.5, 2.2; RFC 6090 §§2.2, 4, 10.2",
    "sourceNote": "Generalizes the finite-field equations to a cyclic group; restricts to prime order and nonzero secrets. Historical parameter sizes and SHA-1 KDF are not adopted.",
    "provenanceKind": "adapted",
    "statement": "Public and shared values use the same group and exponent action.",
    "formalStatement": "public(a)=g^a; share(a,Y)=Y^a; validate(Y) ⇔ Y∈H\\{1_H}.",
    "appliesTo": [
      "urn:csabs:concept/DiffieHellman"
    ],
    "assumptions": [
      "Fix a finite cyclic group H=⟨g⟩ of prime order q≥2 with identity 1_H. Secret scalars a,b range over S={1,…,q−1}; public inputs are H\\{1_H}. Equality is group-element equality, independent of wire representation. Operations are deterministic for supplied scalars; independent uniform sampling on S is required for the selected key-generation model. No KDF, transcript authentication, key confirmation or wire encoding is specified. A finite-field instance has H≤𝔽_p×, q dividing p−1, and g of exact order q; ECDH supplies an additive instance."
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial statement and proof sketch; not machine-checked."
  },
  {
    "id": "urn:csabs:theorem/DiffieHellman-agreement",
    "type": "Theorem",
    "name": "agreement",
    "source": [
      "urn:csabs:source/rfc2631",
      "urn:csabs:source/rfc6090"
    ],
    "sourceLocator": "RFC 2631 §§2.1.1, 2.1.5, 2.2; RFC 6090 §§2.2, 4, 10.2",
    "sourceNote": "Editorial consequence of the explicitly linked premises. Generalizes the finite-field equations to a cyclic group; restricts to prime order and nonzero secrets. Historical parameter sizes and SHA-1 KDF are not adopted.",
    "provenanceKind": "derived",
    "statement": "Honest participants obtain the same nonidentity group element.",
    "formalStatement": "share(a,public(b))=g^(ab)=share(b,public(a))≠1_H.",
    "dependsOn": [
      "urn:csabs:axiom/DiffieHellman-group-power",
      "urn:csabs:axiom/DiffieHellman-exchange"
    ],
    "proofSketch": "Associativity gives (g^b)^a=g^(ba); integer multiplication commutes. Since q is prime and neither a nor b is zero modulo q, q does not divide ab, so the result is nonidentity.",
    "appliesTo": [
      "urn:csabs:concept/DiffieHellman"
    ],
    "assumptions": [
      "Fix a finite cyclic group H=⟨g⟩ of prime order q≥2 with identity 1_H. Secret scalars a,b range over S={1,…,q−1}; public inputs are H\\{1_H}. Equality is group-element equality, independent of wire representation. Operations are deterministic for supplied scalars; independent uniform sampling on S is required for the selected key-generation model. No KDF, transcript authentication, key confirmation or wire encoding is specified. A finite-field instance has H≤𝔽_p×, q dividing p−1, and g of exact order q; ECDH supplies an additive instance."
    ],
    "ruleRole": "derived-result",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial statement and proof sketch; not machine-checked."
  }
]
```
<!-- graph-record:end -->
