# RSA modular-exponentiation primitives (two-prime profile)

Mutually inverse exponent maps on all residue representatives for a modulus built from two distinct odd primes. These underpin RSA encryption and signature schemes.

**Notation:** n=pq; λ=lcm(p−1,q−1); ed≡1 (mod λ); E(m)=m^e mod n; D(c)=c^d mod n.

**Stable ID:** `urn:csabs:concept/RSA`

**Categories:** Cryptography → Public-key cryptography

**Kind:** Mathematical construction

**Prerequisites:** [Modular Integer](ModularInteger.md), [Mathematical integers](Integer.md)

**Related concepts:** [Finite field (Galois field)](FiniteField.md)

## Mathematical formulation

The partial exponent interface stores n,e,d∈ℕ and defines publicMap(m)=m^e mod n and privateMap(c)=c^d mod n. Prime-factor, inverse-exponent and representative-range conditions are not encoded by this interface, so no round-trip assertion follows from it alone.

**Lean formulation** (in its source module context):

```lean
structure RSAInterface where
  modulus : Nat
  publicExponent : Nat
  privateExponent : Nat
```

**Source:** [`Catalog.RSAInterface`](../lean/Catalog/Cryptography.lean); consulted 2026-11-12.

**Scope:** partial

**Interpretation:** Nat modulus and public/private exponents; publicMap/privateMap compute exact natural powers modulo modulus. On valid catalog keys and representatives these are the selected exponent maps.

**Limits:** The interface is broader than the catalog: zero modulus, invalid exponents and out-of-range representatives are not rejected. Prime factors, lambda congruence, errors, inverse equations, byte encoding, OAEP and PSS are not modeled.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Explicit valid two-prime key conditions and canonical modular power definitions; correctness is derived rather than assumed.

**basisKind:** defined-structure

**basisScope:** p and q are distinct odd primes; n=pq; 3≤e<n; gcd(e,λ)=1; 1≤d<n; ed≡1 mod λ. R_n={0,…,n−1}, including zero and nonunits. Equality is equality of canonical integer representatives. Exact unbounded integer arithmetic. Fixed valid keys make the maps deterministic. Key generation, randomness, byte encodings, OAEP, PSS, multi-prime RSA and CRT optimization are outside this selected primitive profile.

**verificationObligation:** Map representations, equality, parameter validation and failure behavior explicitly. Exact arithmetic has no overflow or rounding. Functional equations do not establish cryptographic security, entropy quality, constant-time behavior or secret erasure.

**reviewStatus:** Editorial mathematics; no compiled claim witness or cryptographic security proof.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-RSA-public-map"></a>

### public-map

`urn:csabs:operation/RSA-public-map`

**source:** [RFC 8017: PKCS #1: RSA Cryptography Specifications Version 2.2](https://www.rfc-editor.org/rfc/rfc8017.txt); accessedOn: 2026-11-11; sourceRole: primary algorithm specification

**sourceLocator:** RFC 8017 §§3.1–3.2, 5.1–5.2; §§7–8 for distinction from schemes

**sourceNote:** Selects the two-prime case and first private-key representation. Raw exponentiation is not a secure encryption or signature scheme.

**provenanceKind:** adapted

**signature:** E_(n,e) : R_n → R_n

**description:** RSAEP, also the exponent map of RSAVP1 on signature representatives.

**precondition:** Valid public key; 0≤m<n.

**postcondition:** Return the least nonnegative residue m^e mod n; reject an out-of-range integer rather than silently reducing it.

**totality:** Total on the stated mathematical domain; malformed or out-of-domain external input is rejected without a result.

<a id="node-urn-csabs-operation-RSA-private-map"></a>

### private-map

`urn:csabs:operation/RSA-private-map`

**source:** [RFC 8017: PKCS #1: RSA Cryptography Specifications Version 2.2](https://www.rfc-editor.org/rfc/rfc8017.txt); accessedOn: 2026-11-11; sourceRole: primary algorithm specification

**sourceLocator:** RFC 8017 §§3.1–3.2, 5.1–5.2; §§7–8 for distinction from schemes

**sourceNote:** Selects the two-prime case and first private-key representation. Raw exponentiation is not a secure encryption or signature scheme.

**provenanceKind:** adapted

**signature:** D_(n,d) : R_n → R_n

**description:** RSADP, also the exponent map of RSASP1 on message representatives.

**precondition:** Valid corresponding private key; 0≤c<n.

**postcondition:** Return the least nonnegative residue c^d mod n; reject an out-of-range integer.

**totality:** Total on the stated mathematical domain; malformed or out-of-domain external input is rejected without a result.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-RSA-key"></a>

### key

`urn:csabs:axiom/RSA-key`

**source:** [RFC 8017: PKCS #1: RSA Cryptography Specifications Version 2.2](https://www.rfc-editor.org/rfc/rfc8017.txt); accessedOn: 2026-11-11; sourceRole: primary algorithm specification

**sourceLocator:** RFC 8017 §§3.1–3.2, 5.1–5.2; §§7–8 for distinction from schemes

**sourceNote:** Selects the two-prime case and first private-key representation. Raw exponentiation is not a secure encryption or signature scheme.

**provenanceKind:** adapted

**statement:** The public and private exponents satisfy the two-prime key constraints.

**formalStatement:** p≠q odd primes; n=pq; λ=lcm(p−1,q−1); 3≤e<n; gcd(e,λ)=1; 1≤d<n; ed≡1 mod λ.

**assumptions:** p and q are distinct odd primes; n=pq; 3≤e<n; gcd(e,λ)=1; 1≤d<n; ed≡1 mod λ. R_n={0,…,n−1}, including zero and nonunits. Equality is equality of canonical integer representatives. Exact unbounded integer arithmetic. Fixed valid keys make the maps deterministic. Key generation, randomness, byte encodings, OAEP, PSS, multi-prime RSA and CRT optimization are outside this selected primitive profile.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial statement and proof sketch; not machine-checked.

<a id="node-urn-csabs-axiom-RSA-power"></a>

### power

`urn:csabs:axiom/RSA-power`

**source:** [RFC 8017: PKCS #1: RSA Cryptography Specifications Version 2.2](https://www.rfc-editor.org/rfc/rfc8017.txt); accessedOn: 2026-11-11; sourceRole: primary algorithm specification

**sourceLocator:** RFC 8017 §§3.1–3.2, 5.1–5.2; §§7–8 for distinction from schemes

**sourceNote:** Selects the two-prime case and first private-key representation. Raw exponentiation is not a secure encryption or signature scheme.

**provenanceKind:** adapted

**statement:** Both maps are canonical modular exponentiation on the full representative carrier.

**formalStatement:** R_n={m∈ℤ | 0≤m<n}; E(m)=m^e mod n; D(m)=m^d mod n.

**assumptions:** p and q are distinct odd primes; n=pq; 3≤e<n; gcd(e,λ)=1; 1≤d<n; ed≡1 mod λ. R_n={0,…,n−1}, including zero and nonunits. Equality is equality of canonical integer representatives. Exact unbounded integer arithmetic. Fixed valid keys make the maps deterministic. Key generation, randomness, byte encodings, OAEP, PSS, multi-prime RSA and CRT optimization are outside this selected primitive profile.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial statement and proof sketch; not machine-checked.

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-RSA-inverse"></a>

### inverse

`urn:csabs:theorem/RSA-inverse`

**source:** [RFC 8017: PKCS #1: RSA Cryptography Specifications Version 2.2](https://www.rfc-editor.org/rfc/rfc8017.txt); accessedOn: 2026-11-11; sourceRole: primary algorithm specification

**sourceLocator:** RFC 8017 §§3.1–3.2, 5.1–5.2; §§7–8 for distinction from schemes

**sourceNote:** Editorial consequence of the explicitly linked premises. Selects the two-prime case and first private-key representation. Raw exponentiation is not a secure encryption or signature scheme.

**provenanceKind:** derived

**statement:** The exponent maps are inverse permutations, including on nonunits.

**formalStatement:** ∀m∈R_n, D(E(m))=m ∧ E(D(m))=m.

**dependsOn:** [key](RSA.md#node-urn-csabs-axiom-RSA-key); [power](RSA.md#node-urn-csabs-axiom-RSA-power)

**proofSketch:** For each r∈{p,q}, if r divides m both m and m^(ed) vanish modulo r. Otherwise Fermat gives m^(r−1)=1 and r−1 divides ed−1, yielding m^(ed)≡m mod r. The distinct primes are coprime, so CRT gives equality modulo n; canonical representatives give equality. Both compositions use exponent ed.

**assumptions:** p and q are distinct odd primes; n=pq; 3≤e<n; gcd(e,λ)=1; 1≤d<n; ed≡1 mod λ. R_n={0,…,n−1}, including zero and nonunits. Equality is equality of canonical integer representatives. Exact unbounded integer arithmetic. Fixed valid keys make the maps deterministic. Key generation, randomness, byte encodings, OAEP, PSS, multi-prime RSA and CRT optimization are outside this selected primitive profile.

**ruleRole:** derived-result

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial statement and proof sketch; not machine-checked.

## Concept provenance

- [RFC 8017: PKCS #1: RSA Cryptography Specifications Version 2.2](https://www.rfc-editor.org/rfc/rfc8017.txt); accessedOn: 2026-11-11; sourceRole: primary algorithm specification

**sourceLocator:** RFC 8017 §§3.1–3.2, 5.1–5.2; §§7–8 for distinction from schemes

**sourceNote:** Selects the two-prime case and first private-key representation. Raw exponentiation is not a secure encryption or signature scheme.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/RSA",
    "type": "Concept",
    "shortForm": "RSA",
    "fullName": "RSA modular-exponentiation primitives (two-prime profile)",
    "definition": "Mutually inverse exponent maps on all residue representatives for a modulus built from two distinct odd primes. These underpin RSA encryption and signature schemes.",
    "notation": "n=pq; λ=lcm(p−1,q−1); ed≡1 (mod λ); E(m)=m^e mod n; D(c)=c^d mod n.",
    "category": [
      "urn:csabs:category/public-key-cryptography"
    ],
    "kind": "urn:csabs:kind/construction",
    "requiresConcept": [
      "urn:csabs:concept/ModularInteger",
      "urn:csabs:concept/MathematicalInteger"
    ],
    "axiomBasis": "Explicit valid two-prime key conditions and canonical modular power definitions; correctness is derived rather than assumed.",
    "basisKind": "defined-structure",
    "basisScope": "p and q are distinct odd primes; n=pq; 3≤e<n; gcd(e,λ)=1; 1≤d<n; ed≡1 mod λ. R_n={0,…,n−1}, including zero and nonunits. Equality is equality of canonical integer representatives. Exact unbounded integer arithmetic. Fixed valid keys make the maps deterministic. Key generation, randomness, byte encodings, OAEP, PSS, multi-prime RSA and CRT optimization are outside this selected primitive profile.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial mathematics; no compiled claim witness or cryptographic security proof.",
    "verificationObligation": [
      "Map representations, equality, parameter validation and failure behavior explicitly. Exact arithmetic has no overflow or rounding. Functional equations do not establish cryptographic security, entropy quality, constant-time behavior or secret erasure."
    ],
    "source": [
      "urn:csabs:source/rfc8017"
    ],
    "sourceLocator": "RFC 8017 §§3.1–3.2, 5.1–5.2; §§7–8 for distinction from schemes",
    "sourceNote": "Selects the two-prime case and first private-key representation. Raw exponentiation is not a secure encryption or signature scheme.",
    "provenanceKind": "adapted",
    "relatedConcept": [
      "urn:csabs:concept/FiniteField"
    ],
    "hasOperation": [
      "urn:csabs:operation/RSA-public-map",
      "urn:csabs:operation/RSA-private-map"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/RSA-key",
      "urn:csabs:axiom/RSA-power"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/RSA-inverse"
    ],
    "hasLaw": [],
    "leanFormulation": "structure RSAInterface where\n  modulus : Nat\n  publicExponent : Nat\n  privateExponent : Nat",
    "formulationSource": "urn:csabs:source/local-lean-Cryptography",
    "formulationLocator": "Catalog.RSAInterface",
    "formulationScope": "partial",
    "leanModelMapping": "Nat modulus and public/private exponents; publicMap/privateMap compute exact natural powers modulo modulus. On valid catalog keys and representatives these are the selected exponent maps.",
    "leanModelLimitations": "The interface is broader than the catalog: zero modulus, invalid exponents and out-of-range representatives are not rejected. Prime factors, lambda congruence, errors, inverse equations, byte encoding, OAEP and PSS are not modeled.",
    "mathematicalFormulation": "The partial exponent interface stores n,e,d∈ℕ and defines publicMap(m)=m^e mod n and privateMap(c)=c^d mod n. Prime-factor, inverse-exponent and representative-range conditions are not encoded by this interface, so no round-trip assertion follows from it alone."
  },
  {
    "id": "urn:csabs:operation/RSA-public-map",
    "type": "Operation",
    "name": "public-map",
    "source": [
      "urn:csabs:source/rfc8017"
    ],
    "sourceLocator": "RFC 8017 §§3.1–3.2, 5.1–5.2; §§7–8 for distinction from schemes",
    "sourceNote": "Selects the two-prime case and first private-key representation. Raw exponentiation is not a secure encryption or signature scheme.",
    "provenanceKind": "adapted",
    "signature": "E_(n,e) : R_n → R_n",
    "description": "RSAEP, also the exponent map of RSAVP1 on signature representatives.",
    "precondition": "Valid public key; 0≤m<n.",
    "postcondition": "Return the least nonnegative residue m^e mod n; reject an out-of-range integer rather than silently reducing it.",
    "concept": "urn:csabs:concept/RSA",
    "totality": "Total on the stated mathematical domain; malformed or out-of-domain external input is rejected without a result."
  },
  {
    "id": "urn:csabs:operation/RSA-private-map",
    "type": "Operation",
    "name": "private-map",
    "source": [
      "urn:csabs:source/rfc8017"
    ],
    "sourceLocator": "RFC 8017 §§3.1–3.2, 5.1–5.2; §§7–8 for distinction from schemes",
    "sourceNote": "Selects the two-prime case and first private-key representation. Raw exponentiation is not a secure encryption or signature scheme.",
    "provenanceKind": "adapted",
    "signature": "D_(n,d) : R_n → R_n",
    "description": "RSADP, also the exponent map of RSASP1 on message representatives.",
    "precondition": "Valid corresponding private key; 0≤c<n.",
    "postcondition": "Return the least nonnegative residue c^d mod n; reject an out-of-range integer.",
    "concept": "urn:csabs:concept/RSA",
    "totality": "Total on the stated mathematical domain; malformed or out-of-domain external input is rejected without a result."
  },
  {
    "id": "urn:csabs:axiom/RSA-key",
    "type": "Axiom",
    "name": "key",
    "source": [
      "urn:csabs:source/rfc8017"
    ],
    "sourceLocator": "RFC 8017 §§3.1–3.2, 5.1–5.2; §§7–8 for distinction from schemes",
    "sourceNote": "Selects the two-prime case and first private-key representation. Raw exponentiation is not a secure encryption or signature scheme.",
    "provenanceKind": "adapted",
    "statement": "The public and private exponents satisfy the two-prime key constraints.",
    "formalStatement": "p≠q odd primes; n=pq; λ=lcm(p−1,q−1); 3≤e<n; gcd(e,λ)=1; 1≤d<n; ed≡1 mod λ.",
    "appliesTo": [
      "urn:csabs:concept/RSA"
    ],
    "assumptions": [
      "p and q are distinct odd primes; n=pq; 3≤e<n; gcd(e,λ)=1; 1≤d<n; ed≡1 mod λ. R_n={0,…,n−1}, including zero and nonunits. Equality is equality of canonical integer representatives. Exact unbounded integer arithmetic. Fixed valid keys make the maps deterministic. Key generation, randomness, byte encodings, OAEP, PSS, multi-prime RSA and CRT optimization are outside this selected primitive profile."
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial statement and proof sketch; not machine-checked."
  },
  {
    "id": "urn:csabs:axiom/RSA-power",
    "type": "Axiom",
    "name": "power",
    "source": [
      "urn:csabs:source/rfc8017"
    ],
    "sourceLocator": "RFC 8017 §§3.1–3.2, 5.1–5.2; §§7–8 for distinction from schemes",
    "sourceNote": "Selects the two-prime case and first private-key representation. Raw exponentiation is not a secure encryption or signature scheme.",
    "provenanceKind": "adapted",
    "statement": "Both maps are canonical modular exponentiation on the full representative carrier.",
    "formalStatement": "R_n={m∈ℤ | 0≤m<n}; E(m)=m^e mod n; D(m)=m^d mod n.",
    "appliesTo": [
      "urn:csabs:concept/RSA"
    ],
    "assumptions": [
      "p and q are distinct odd primes; n=pq; 3≤e<n; gcd(e,λ)=1; 1≤d<n; ed≡1 mod λ. R_n={0,…,n−1}, including zero and nonunits. Equality is equality of canonical integer representatives. Exact unbounded integer arithmetic. Fixed valid keys make the maps deterministic. Key generation, randomness, byte encodings, OAEP, PSS, multi-prime RSA and CRT optimization are outside this selected primitive profile."
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial statement and proof sketch; not machine-checked."
  },
  {
    "id": "urn:csabs:theorem/RSA-inverse",
    "type": "Theorem",
    "name": "inverse",
    "source": [
      "urn:csabs:source/rfc8017"
    ],
    "sourceLocator": "RFC 8017 §§3.1–3.2, 5.1–5.2; §§7–8 for distinction from schemes",
    "sourceNote": "Editorial consequence of the explicitly linked premises. Selects the two-prime case and first private-key representation. Raw exponentiation is not a secure encryption or signature scheme.",
    "provenanceKind": "derived",
    "statement": "The exponent maps are inverse permutations, including on nonunits.",
    "formalStatement": "∀m∈R_n, D(E(m))=m ∧ E(D(m))=m.",
    "dependsOn": [
      "urn:csabs:axiom/RSA-key",
      "urn:csabs:axiom/RSA-power"
    ],
    "proofSketch": "For each r∈{p,q}, if r divides m both m and m^(ed) vanish modulo r. Otherwise Fermat gives m^(r−1)=1 and r−1 divides ed−1, yielding m^(ed)≡m mod r. The distinct primes are coprime, so CRT gives equality modulo n; canonical representatives give equality. Both compositions use exponent ed.",
    "appliesTo": [
      "urn:csabs:concept/RSA"
    ],
    "assumptions": [
      "p and q are distinct odd primes; n=pq; 3≤e<n; gcd(e,λ)=1; 1≤d<n; ed≡1 mod λ. R_n={0,…,n−1}, including zero and nonunits. Equality is equality of canonical integer representatives. Exact unbounded integer arithmetic. Fixed valid keys make the maps deterministic. Key generation, randomness, byte encodings, OAEP, PSS, multi-prime RSA and CRT optimization are outside this selected primitive profile."
    ],
    "ruleRole": "derived-result",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial statement and proof sketch; not machine-checked."
  }
]
```
<!-- graph-record:end -->
