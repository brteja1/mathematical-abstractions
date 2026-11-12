# Elliptic curve Diffie–Hellman (validated full-point profile)

Diffie–Hellman key agreement instantiated in the prime-order subgroup of the selected elliptic curve group, returning a shared point.

**Notation:** Q_a=[a]G; Q_b=[b]G; Z=[a]Q_b=[b]Q_a.

**Stable ID:** `urn:csabs:concept/ECDH`

**Categories:** Cryptography → Public-key cryptography

**Kind:** Mathematical construction

**Prerequisites:** [Diffie–Hellman key exchange (prime-order cyclic-group core)](DiffieHellman.md), [Elliptic curve cryptography group (prime-field short-Weierstrass profile)](ECC.md)

**Specializes:** [Diffie–Hellman key exchange (prime-order cyclic-group core)](DiffieHellman.md)

## Mathematical formulation

For the partial abstract point-group interface, sharedPoint(a,Q)=aQ. The carrier supplies a base-point interface but no peer-validation predicate, secret-range guard or key-derivation function.

**Lean formulation** (in its source module context):

```lean
structure ECDHInterface (Point : Type) [AddCommGroup Point] where
  curve : ECCInterface Point
```

**Source:** [`Catalog.ECDHInterface`](../lean/Catalog/Cryptography.lean); consulted 2026-11-12.

**Scope:** partial

**Interpretation:** ECCInterface Point under AddCommGroup; sharedPoint uses natural scalar multiplication of a supplied peer point.

**Limits:** No validation, prime-order or nonzero-scalar restrictions, full-point encoding, agreement witness, KDF or authentication. A supplied abstract group is not a verified curve implementation.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Explicit DiffieHellman instantiation by the ECC subgroup, nonidentity subgroup validation and point scalar multiplication.

**basisKind:** defined-structure

**basisScope:** Use the ECC prime-field short-Weierstrass profile and fixed H=⟨G⟩ of prime order q. Scalars a,b∈S={1,…,q−1}; independent uniform scalar sampling is a separate key-generation obligation. Validate peer points as nonidentity members of the same H. Return full points with exact point equality. No cofactor multiplication, x-only encoding, compact output, KDF or transcript authentication is included; those need explicit profiles. The curve identity is a valid group element but an invalid public key.

**specializationNote:** Instantiate H by ⟨G⟩, identity by O and exponentiation by scalar multiplication; preserve secret scalar domain and nonidentity public-key validation. ECC supplies the algebraic component, not a parent protocol.

**verificationObligation:** Map representations, equality, parameter validation and failure behavior explicitly. Exact arithmetic has no overflow or rounding. Functional equations do not establish cryptographic security, entropy quality, constant-time behavior or secret erasure.

**reviewStatus:** Editorial mathematics; no compiled claim witness or cryptographic security proof.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-ECDH-public"></a>

### public

`urn:csabs:operation/ECDH-public`

**source:** [RFC 6090: Fundamental Elliptic Curve Cryptography Algorithms](https://www.rfc-editor.org/rfc/rfc6090.txt); accessedOn: 2026-11-11; sourceRole: primary algorithm specification

**sourceLocator:** RFC 6090 §§3.3, 4–4.2, 10.1–10.3

**sourceNote:** Selects full-point output with strict subgroup membership; the RFC compact-output option is excluded. Curve membership alone is insufficient when h>1.

**provenanceKind:** adapted

**signature:** public : S → H\{O}

**description:** Construct the public curve point.

**precondition:** Common validated curve/subgroup parameters; a∈S.

**postcondition:** Return [a]G.

**totality:** Total on the stated mathematical domain; malformed or out-of-domain external input is rejected without a result.

<a id="node-urn-csabs-operation-ECDH-validate"></a>

### validate

`urn:csabs:operation/ECDH-validate`

**source:** [RFC 6090: Fundamental Elliptic Curve Cryptography Algorithms](https://www.rfc-editor.org/rfc/rfc6090.txt); accessedOn: 2026-11-11; sourceRole: primary algorithm specification

**sourceLocator:** RFC 6090 §§3.3, 4–4.2, 10.1–10.3

**sourceNote:** Selects full-point output with strict subgroup membership; the RFC compact-output option is excluded. Curve membership alone is insufficient when h>1.

**provenanceKind:** adapted

**signature:** validate : E → Bool

**description:** Validate a decoded point on the fixed curve for this subgroup.

**precondition:** Strict decoding has already checked coordinates, parameter identity and the curve equation.

**postcondition:** true iff Q≠O and Q∈H. The test [q]Q=O alone requires an additional uniqueness-of-q-subgroup argument to replace membership in H.

**totality:** Total on the stated mathematical domain; malformed or out-of-domain external input is rejected without a result.

<a id="node-urn-csabs-operation-ECDH-share"></a>

### share

`urn:csabs:operation/ECDH-share`

**source:** [RFC 6090: Fundamental Elliptic Curve Cryptography Algorithms](https://www.rfc-editor.org/rfc/rfc6090.txt); accessedOn: 2026-11-11; sourceRole: primary algorithm specification

**sourceLocator:** RFC 6090 §§3.3, 4–4.2, 10.1–10.3

**sourceNote:** Selects full-point output with strict subgroup membership; the RFC compact-output option is excluded. Curve membership alone is insufficient when h>1.

**provenanceKind:** adapted

**signature:** share : S×(H\{O}) → H\{O}

**description:** Compute a full shared point with a validated peer.

**precondition:** a∈S; validate(Q)=true.

**postcondition:** Return [a]Q.

**totality:** Total on the stated mathematical domain; malformed or out-of-domain external input is rejected without a result.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-ECDH-instantiation"></a>

### instantiation

`urn:csabs:axiom/ECDH-instantiation`

**source:** [RFC 6090: Fundamental Elliptic Curve Cryptography Algorithms](https://www.rfc-editor.org/rfc/rfc6090.txt); accessedOn: 2026-11-11; sourceRole: primary algorithm specification

**sourceLocator:** RFC 6090 §§3.3, 4–4.2, 10.1–10.3

**sourceNote:** Selects full-point output with strict subgroup membership; the RFC compact-output option is excluded. Curve membership alone is insufficient when h>1.

**provenanceKind:** adapted

**statement:** Use the additive ECC subgroup for the DH group and power action.

**formalStatement:** DiffieHellman.H:=ECC.H; g:=G; 1_H:=O; X·Y:=X+Y; X^k:=[k]X; public(a)=[a]G; share(a,Q)=[a]Q; validate(Q)⇔Q∈H\{O}.

**assumptions:** Use the ECC prime-field short-Weierstrass profile and fixed H=⟨G⟩ of prime order q. Scalars a,b∈S={1,…,q−1}; independent uniform scalar sampling is a separate key-generation obligation. Validate peer points as nonidentity members of the same H. Return full points with exact point equality. No cofactor multiplication, x-only encoding, compact output, KDF or transcript authentication is included; those need explicit profiles. The curve identity is a valid group element but an invalid public key.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial statement and proof sketch; not machine-checked.

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-ECDH-agreement"></a>

### agreement

`urn:csabs:theorem/ECDH-agreement`

**source:** [RFC 6090: Fundamental Elliptic Curve Cryptography Algorithms](https://www.rfc-editor.org/rfc/rfc6090.txt); accessedOn: 2026-11-11; sourceRole: primary algorithm specification

**sourceLocator:** RFC 6090 §§3.3, 4–4.2, 10.1–10.3

**sourceNote:** Editorial consequence of the explicitly linked premises. Selects full-point output with strict subgroup membership; the RFC compact-output option is excluded. Curve membership alone is insufficient when h>1.

**provenanceKind:** derived

**statement:** Both parties obtain the same nonidentity shared point.

**formalStatement:** share(a,public(b))=[ab]G=share(b,public(a))≠O.

**dependsOn:** [instantiation](ECDH.md#node-urn-csabs-axiom-ECDH-instantiation); [carrier](ECC.md#node-urn-csabs-axiom-ECC-carrier); [scalar-composition](ECC.md#node-urn-csabs-theorem-ECC-scalar-composition); [agreement](DiffieHellman.md#node-urn-csabs-theorem-DiffieHellman-agreement)

**proofSketch:** The instantiation maps the DH agreement premises to the explicit ECC subgroup. Scalar composition gives [a]([b]G)=[ab]G=[ba]G. Since G has prime order q and q divides neither secret, the point is not O.

**assumptions:** Use the ECC prime-field short-Weierstrass profile and fixed H=⟨G⟩ of prime order q. Scalars a,b∈S={1,…,q−1}; independent uniform scalar sampling is a separate key-generation obligation. Validate peer points as nonidentity members of the same H. Return full points with exact point equality. No cofactor multiplication, x-only encoding, compact output, KDF or transcript authentication is included; those need explicit profiles. The curve identity is a valid group element but an invalid public key.

**ruleRole:** derived-result

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial statement and proof sketch; not machine-checked.

## Concept provenance

- [RFC 6090: Fundamental Elliptic Curve Cryptography Algorithms](https://www.rfc-editor.org/rfc/rfc6090.txt); accessedOn: 2026-11-11; sourceRole: primary algorithm specification

**sourceLocator:** RFC 6090 §§3.3, 4–4.2, 10.1–10.3

**sourceNote:** Selects full-point output with strict subgroup membership; the RFC compact-output option is excluded. Curve membership alone is insufficient when h>1.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/ECDH",
    "type": "Concept",
    "shortForm": "ECDH",
    "fullName": "Elliptic curve Diffie–Hellman (validated full-point profile)",
    "definition": "Diffie–Hellman key agreement instantiated in the prime-order subgroup of the selected elliptic curve group, returning a shared point.",
    "notation": "Q_a=[a]G; Q_b=[b]G; Z=[a]Q_b=[b]Q_a.",
    "category": [
      "urn:csabs:category/public-key-cryptography"
    ],
    "kind": "urn:csabs:kind/construction",
    "requiresConcept": [
      "urn:csabs:concept/DiffieHellman",
      "urn:csabs:concept/ECC"
    ],
    "axiomBasis": "Explicit DiffieHellman instantiation by the ECC subgroup, nonidentity subgroup validation and point scalar multiplication.",
    "basisKind": "defined-structure",
    "basisScope": "Use the ECC prime-field short-Weierstrass profile and fixed H=⟨G⟩ of prime order q. Scalars a,b∈S={1,…,q−1}; independent uniform scalar sampling is a separate key-generation obligation. Validate peer points as nonidentity members of the same H. Return full points with exact point equality. No cofactor multiplication, x-only encoding, compact output, KDF or transcript authentication is included; those need explicit profiles. The curve identity is a valid group element but an invalid public key.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial mathematics; no compiled claim witness or cryptographic security proof.",
    "verificationObligation": [
      "Map representations, equality, parameter validation and failure behavior explicitly. Exact arithmetic has no overflow or rounding. Functional equations do not establish cryptographic security, entropy quality, constant-time behavior or secret erasure."
    ],
    "source": [
      "urn:csabs:source/rfc6090"
    ],
    "sourceLocator": "RFC 6090 §§3.3, 4–4.2, 10.1–10.3",
    "sourceNote": "Selects full-point output with strict subgroup membership; the RFC compact-output option is excluded. Curve membership alone is insufficient when h>1.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/DiffieHellman"
    ],
    "specializationNote": "Instantiate H by ⟨G⟩, identity by O and exponentiation by scalar multiplication; preserve secret scalar domain and nonidentity public-key validation. ECC supplies the algebraic component, not a parent protocol.",
    "hasOperation": [
      "urn:csabs:operation/ECDH-public",
      "urn:csabs:operation/ECDH-validate",
      "urn:csabs:operation/ECDH-share"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/ECDH-instantiation"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/ECDH-agreement"
    ],
    "hasLaw": [],
    "leanFormulation": "structure ECDHInterface (Point : Type) [AddCommGroup Point] where\n  curve : ECCInterface Point",
    "formulationSource": "urn:csabs:source/local-lean-Cryptography",
    "formulationLocator": "Catalog.ECDHInterface",
    "formulationScope": "partial",
    "leanModelMapping": "ECCInterface Point under AddCommGroup; sharedPoint uses natural scalar multiplication of a supplied peer point.",
    "leanModelLimitations": "No validation, prime-order or nonzero-scalar restrictions, full-point encoding, agreement witness, KDF or authentication. A supplied abstract group is not a verified curve implementation.",
    "mathematicalFormulation": "For the partial abstract point-group interface, sharedPoint(a,Q)=aQ. The carrier supplies a base-point interface but no peer-validation predicate, secret-range guard or key-derivation function."
  },
  {
    "id": "urn:csabs:operation/ECDH-public",
    "type": "Operation",
    "name": "public",
    "source": [
      "urn:csabs:source/rfc6090"
    ],
    "sourceLocator": "RFC 6090 §§3.3, 4–4.2, 10.1–10.3",
    "sourceNote": "Selects full-point output with strict subgroup membership; the RFC compact-output option is excluded. Curve membership alone is insufficient when h>1.",
    "provenanceKind": "adapted",
    "signature": "public : S → H\\{O}",
    "description": "Construct the public curve point.",
    "precondition": "Common validated curve/subgroup parameters; a∈S.",
    "postcondition": "Return [a]G.",
    "concept": "urn:csabs:concept/ECDH",
    "totality": "Total on the stated mathematical domain; malformed or out-of-domain external input is rejected without a result."
  },
  {
    "id": "urn:csabs:operation/ECDH-validate",
    "type": "Operation",
    "name": "validate",
    "source": [
      "urn:csabs:source/rfc6090"
    ],
    "sourceLocator": "RFC 6090 §§3.3, 4–4.2, 10.1–10.3",
    "sourceNote": "Selects full-point output with strict subgroup membership; the RFC compact-output option is excluded. Curve membership alone is insufficient when h>1.",
    "provenanceKind": "adapted",
    "signature": "validate : E → Bool",
    "description": "Validate a decoded point on the fixed curve for this subgroup.",
    "precondition": "Strict decoding has already checked coordinates, parameter identity and the curve equation.",
    "postcondition": "true iff Q≠O and Q∈H. The test [q]Q=O alone requires an additional uniqueness-of-q-subgroup argument to replace membership in H.",
    "concept": "urn:csabs:concept/ECDH",
    "totality": "Total on the stated mathematical domain; malformed or out-of-domain external input is rejected without a result."
  },
  {
    "id": "urn:csabs:operation/ECDH-share",
    "type": "Operation",
    "name": "share",
    "source": [
      "urn:csabs:source/rfc6090"
    ],
    "sourceLocator": "RFC 6090 §§3.3, 4–4.2, 10.1–10.3",
    "sourceNote": "Selects full-point output with strict subgroup membership; the RFC compact-output option is excluded. Curve membership alone is insufficient when h>1.",
    "provenanceKind": "adapted",
    "signature": "share : S×(H\\{O}) → H\\{O}",
    "description": "Compute a full shared point with a validated peer.",
    "precondition": "a∈S; validate(Q)=true.",
    "postcondition": "Return [a]Q.",
    "concept": "urn:csabs:concept/ECDH",
    "totality": "Total on the stated mathematical domain; malformed or out-of-domain external input is rejected without a result."
  },
  {
    "id": "urn:csabs:axiom/ECDH-instantiation",
    "type": "Axiom",
    "name": "instantiation",
    "source": [
      "urn:csabs:source/rfc6090"
    ],
    "sourceLocator": "RFC 6090 §§3.3, 4–4.2, 10.1–10.3",
    "sourceNote": "Selects full-point output with strict subgroup membership; the RFC compact-output option is excluded. Curve membership alone is insufficient when h>1.",
    "provenanceKind": "adapted",
    "statement": "Use the additive ECC subgroup for the DH group and power action.",
    "formalStatement": "DiffieHellman.H:=ECC.H; g:=G; 1_H:=O; X·Y:=X+Y; X^k:=[k]X; public(a)=[a]G; share(a,Q)=[a]Q; validate(Q)⇔Q∈H\\{O}.",
    "appliesTo": [
      "urn:csabs:concept/ECDH"
    ],
    "assumptions": [
      "Use the ECC prime-field short-Weierstrass profile and fixed H=⟨G⟩ of prime order q. Scalars a,b∈S={1,…,q−1}; independent uniform scalar sampling is a separate key-generation obligation. Validate peer points as nonidentity members of the same H. Return full points with exact point equality. No cofactor multiplication, x-only encoding, compact output, KDF or transcript authentication is included; those need explicit profiles. The curve identity is a valid group element but an invalid public key."
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial statement and proof sketch; not machine-checked."
  },
  {
    "id": "urn:csabs:theorem/ECDH-agreement",
    "type": "Theorem",
    "name": "agreement",
    "source": [
      "urn:csabs:source/rfc6090"
    ],
    "sourceLocator": "RFC 6090 §§3.3, 4–4.2, 10.1–10.3",
    "sourceNote": "Editorial consequence of the explicitly linked premises. Selects full-point output with strict subgroup membership; the RFC compact-output option is excluded. Curve membership alone is insufficient when h>1.",
    "provenanceKind": "derived",
    "statement": "Both parties obtain the same nonidentity shared point.",
    "formalStatement": "share(a,public(b))=[ab]G=share(b,public(a))≠O.",
    "dependsOn": [
      "urn:csabs:axiom/ECDH-instantiation",
      "urn:csabs:axiom/ECC-carrier",
      "urn:csabs:theorem/ECC-scalar-composition",
      "urn:csabs:theorem/DiffieHellman-agreement"
    ],
    "proofSketch": "The instantiation maps the DH agreement premises to the explicit ECC subgroup. Scalar composition gives [a]([b]G)=[ab]G=[ba]G. Since G has prime order q and q divides neither secret, the point is not O.",
    "appliesTo": [
      "urn:csabs:concept/ECDH"
    ],
    "assumptions": [
      "Use the ECC prime-field short-Weierstrass profile and fixed H=⟨G⟩ of prime order q. Scalars a,b∈S={1,…,q−1}; independent uniform scalar sampling is a separate key-generation obligation. Validate peer points as nonidentity members of the same H. Return full points with exact point equality. No cofactor multiplication, x-only encoding, compact output, KDF or transcript authentication is included; those need explicit profiles. The curve identity is a valid group element but an invalid public key."
    ],
    "ruleRole": "derived-result",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial statement and proof sketch; not machine-checked."
  }
]
```
<!-- graph-record:end -->
