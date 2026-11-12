# Elliptic curve cryptography group (prime-field short-Weierstrass profile)

The finite abelian point group and selected prime-order subgroup used as an algebraic foundation for elliptic curve cryptography. ECC names a family of schemes, not one encryption algorithm.

**Notation:** E(𝔽_p)={(x,y) | y²=x³+Ax+B}∪{O}; H=⟨G⟩; [k]P.

**Stable ID:** `urn:csabs:concept/ECC`

**Categories:** Cryptography → Public-key cryptography

**Kind:** Mathematical structure

**Prerequisites:** [Finite field (Galois field)](FiniteField.md), [Group](Group.md)

**Specializes:** [Group](Group.md)

## Backlinks

- [Elliptic curve Diffie–Hellman (validated full-point profile)](ECDH.md) — `requiresConcept`

## Mathematical formulation

The partial interpretation uses an abstract abelian additive group E with G∈E and subgroupOrder∈ℕ; publicPoint(a)=aG for a∈ℕ. Coordinates, curve nonsingularity and the exact order of G are not encoded.

**Lean formulation** (in its source module context):

```lean
structure ECCInterface (Point : Type) [AddCommGroup Point] where
  basePoint : Point
  subgroupOrder : Nat
```

**Source:** [`Catalog.ECCInterface`](../lean/Catalog/Cryptography.lean); consulted 2026-11-12.

**Scope:** partial

**Interpretation:** Abstract AddCommGroup Point with a basePoint and subgroupOrder; publicPoint uses natural scalar multiplication. Equality is Lean point equality; zero interprets O.

**Limits:** No field/affine representation, nonsingularity, selected subgroup, base-point order, coordinate equivalence or correspondence to the slope formulas is established.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Nonsingular point carrier, complete affine addition with exceptional cases, inverse, group laws and recursive scalar multiplication.

**basisKind:** defined-structure

**basisScope:** Fix prime p>3 and A,B∈𝔽_p with 4A³+27B²≠0. E includes O. Fix G∈E of prime order q≥2; H=⟨G⟩, h=|E|/q. E need not be cyclic. Equality is affine coordinate equality or O=O; equivalent projective encodings require a normalization/equivalence mapping. Scalar multiplication accepts k∈ℕ, including zero; addition and negation include O. All field arithmetic is exact modulo p. Other curve forms, characteristic 2 or 3, signatures and complete encryption protocols require separate instantiations.

**specializationNote:** Instantiate Group carrier by E(𝔽_p), multiplication by point addition, identity by O and inverse by point negation. The local group-laws record explicitly states applicability; FiniteField is a prerequisite, not a specialization parent.

**verificationObligation:** Map representations, equality, parameter validation and failure behavior explicitly. Exact arithmetic has no overflow or rounding. Functional equations do not establish cryptographic security, entropy quality, constant-time behavior or secret erasure.

**reviewStatus:** Editorial mathematics; no compiled claim witness or cryptographic security proof.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-ECC-add"></a>

### add

`urn:csabs:operation/ECC-add`

**source:** [RFC 6090: Fundamental Elliptic Curve Cryptography Algorithms](https://www.rfc-editor.org/rfc/rfc6090.txt); accessedOn: 2026-11-11; sourceRole: primary algorithm specification

**sourceLocator:** RFC 6090 §§2.2–2.3, 3, 3.3–3.3.1, 10.1, Appendix F.1

**sourceNote:** Uses additive notation for the RFC group operation; selects prime fields, short-Weierstrass form and a prime-order subgroup. No parameter-strength recommendation is implied.

**provenanceKind:** adapted

**signature:** add : E×E → E

**description:** Complete point addition on the fixed curve.

**precondition:** Both inputs are valid points of this same E.

**postcondition:** Use O as identity; inverse pairs give O; all remaining cases use the slope rule.

**totality:** Total on the stated mathematical domain; malformed or out-of-domain external input is rejected without a result.

<a id="node-urn-csabs-operation-ECC-negate"></a>

### negate

`urn:csabs:operation/ECC-negate`

**source:** [RFC 6090: Fundamental Elliptic Curve Cryptography Algorithms](https://www.rfc-editor.org/rfc/rfc6090.txt); accessedOn: 2026-11-11; sourceRole: primary algorithm specification

**sourceLocator:** RFC 6090 §§2.2–2.3, 3, 3.3–3.3.1, 10.1, Appendix F.1

**sourceNote:** Uses additive notation for the RFC group operation; selects prime fields, short-Weierstrass form and a prime-order subgroup. No parameter-strength recommendation is implied.

**provenanceKind:** adapted

**signature:** neg : E → E

**description:** Additive inverse of a point.

**precondition:** P∈E.

**postcondition:** −O=O; −(x,y)=(x,−y).

**totality:** Total on the stated mathematical domain; malformed or out-of-domain external input is rejected without a result.

<a id="node-urn-csabs-operation-ECC-scalar"></a>

### scalar

`urn:csabs:operation/ECC-scalar`

**source:** [RFC 6090: Fundamental Elliptic Curve Cryptography Algorithms](https://www.rfc-editor.org/rfc/rfc6090.txt); accessedOn: 2026-11-11; sourceRole: primary algorithm specification

**sourceLocator:** RFC 6090 §§2.2–2.3, 3, 3.3–3.3.1, 10.1, Appendix F.1

**sourceNote:** Uses additive notation for the RFC group operation; selects prime fields, short-Weierstrass form and a prime-order subgroup. No parameter-strength recommendation is implied.

**provenanceKind:** adapted

**signature:** smul : ℕ×E → E

**description:** Repeated point addition, with the empty sum defined.

**precondition:** k≥0; P∈E.

**postcondition:** [0]P=O; [k+1]P=[k]P+P.

**totality:** Total on the stated mathematical domain; malformed or out-of-domain external input is rejected without a result.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-ECC-carrier"></a>

### carrier

`urn:csabs:axiom/ECC-carrier`

**source:** [RFC 6090: Fundamental Elliptic Curve Cryptography Algorithms](https://www.rfc-editor.org/rfc/rfc6090.txt); accessedOn: 2026-11-11; sourceRole: primary algorithm specification

**sourceLocator:** RFC 6090 §§2.2–2.3, 3, 3.3–3.3.1, 10.1, Appendix F.1

**sourceNote:** Uses additive notation for the RFC group operation; selects prime fields, short-Weierstrass form and a prime-order subgroup. No parameter-strength recommendation is implied.

**provenanceKind:** adapted

**statement:** The chosen curve is nonsingular and includes its identity; G has prime order.

**formalStatement:** p>3 prime; 4A³+27B²≠0 in 𝔽_p; E={(x,y)∈𝔽_p² | y²=x³+Ax+B}∪{O}; ord(G)=q prime; H=⟨G⟩.

**assumptions:** Fix prime p>3 and A,B∈𝔽_p with 4A³+27B²≠0. E includes O. Fix G∈E of prime order q≥2; H=⟨G⟩, h=|E|/q. E need not be cyclic. Equality is affine coordinate equality or O=O; equivalent projective encodings require a normalization/equivalence mapping. Scalar multiplication accepts k∈ℕ, including zero; addition and negation include O. All field arithmetic is exact modulo p. Other curve forms, characteristic 2 or 3, signatures and complete encryption protocols require separate instantiations.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial statement and proof sketch; not machine-checked.

<a id="node-urn-csabs-axiom-ECC-addition"></a>

### addition

`urn:csabs:axiom/ECC-addition`

**source:** [RFC 6090: Fundamental Elliptic Curve Cryptography Algorithms](https://www.rfc-editor.org/rfc/rfc6090.txt); accessedOn: 2026-11-11; sourceRole: primary algorithm specification

**sourceLocator:** RFC 6090 §§2.2–2.3, 3, 3.3–3.3.1, 10.1, Appendix F.1

**sourceNote:** Uses additive notation for the RFC group operation; selects prime fields, short-Weierstrass form and a prime-order subgroup. No parameter-strength recommendation is implied.

**provenanceKind:** adapted

**statement:** The affine slope rule handles identity and vertical-tangent cases before division.

**formalStatement:** O+P=P+O=P; −O=O; −(x,y)=(x,−y). For affine P=(x₁,y₁), Q=(x₂,y₂): if Q=−P return O; otherwise s=(y₂−y₁)/(x₂−x₁) when x₁≠x₂, and s=(3x₁²+A)/(2y₁) when P=Q with y₁≠0; x₃=s²−x₁−x₂; y₃=s(x₁−x₃)−y₁; P+Q=(x₃,y₃).

**assumptions:** Fix prime p>3 and A,B∈𝔽_p with 4A³+27B²≠0. E includes O. Fix G∈E of prime order q≥2; H=⟨G⟩, h=|E|/q. E need not be cyclic. Equality is affine coordinate equality or O=O; equivalent projective encodings require a normalization/equivalence mapping. Scalar multiplication accepts k∈ℕ, including zero; addition and negation include O. All field arithmetic is exact modulo p. Other curve forms, characteristic 2 or 3, signatures and complete encryption protocols require separate instantiations.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial statement and proof sketch; not machine-checked.

<a id="node-urn-csabs-axiom-ECC-group-laws"></a>

### group-laws

`urn:csabs:axiom/ECC-group-laws`

**source:** [RFC 6090: Fundamental Elliptic Curve Cryptography Algorithms](https://www.rfc-editor.org/rfc/rfc6090.txt); accessedOn: 2026-11-11; sourceRole: primary algorithm specification

**sourceLocator:** RFC 6090 §§2.2–2.3, 3, 3.3–3.3.1, 10.1, Appendix F.1

**sourceNote:** Uses additive notation for the RFC group operation; selects prime fields, short-Weierstrass form and a prime-order subgroup. No parameter-strength recommendation is implied.

**provenanceKind:** adapted

**statement:** The selected point operation satisfies the abelian group interface.

**formalStatement:** P+Q∈E; (P+Q)+R=P+(Q+R); P+Q=Q+P; P+O=O+P=P; P+(−P)=(−P)+P=O.

**ruleRole:** structure-law

**assumptions:** Fix prime p>3 and A,B∈𝔽_p with 4A³+27B²≠0. E includes O. Fix G∈E of prime order q≥2; H=⟨G⟩, h=|E|/q. E need not be cyclic. Equality is affine coordinate equality or O=O; equivalent projective encodings require a normalization/equivalence mapping. Scalar multiplication accepts k∈ℕ, including zero; addition and negation include O. All field arithmetic is exact modulo p. Other curve forms, characteristic 2 or 3, signatures and complete encryption protocols require separate instantiations.

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial statement and proof sketch; not machine-checked.

<a id="node-urn-csabs-axiom-ECC-scalar-rule"></a>

### scalar-rule

`urn:csabs:axiom/ECC-scalar-rule`

**source:** [RFC 6090: Fundamental Elliptic Curve Cryptography Algorithms](https://www.rfc-editor.org/rfc/rfc6090.txt); accessedOn: 2026-11-11; sourceRole: primary algorithm specification

**sourceLocator:** RFC 6090 §§2.2–2.3, 3, 3.3–3.3.1, 10.1, Appendix F.1

**sourceNote:** Uses additive notation for the RFC group operation; selects prime fields, short-Weierstrass form and a prime-order subgroup. No parameter-strength recommendation is implied.

**provenanceKind:** adapted

**statement:** Natural scalar multiplication is the repeated group sum.

**formalStatement:** [0]P=O; [k+1]P=[k]P+P for k∈ℕ.

**assumptions:** Fix prime p>3 and A,B∈𝔽_p with 4A³+27B²≠0. E includes O. Fix G∈E of prime order q≥2; H=⟨G⟩, h=|E|/q. E need not be cyclic. Equality is affine coordinate equality or O=O; equivalent projective encodings require a normalization/equivalence mapping. Scalar multiplication accepts k∈ℕ, including zero; addition and negation include O. All field arithmetic is exact modulo p. Other curve forms, characteristic 2 or 3, signatures and complete encryption protocols require separate instantiations.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial statement and proof sketch; not machine-checked.

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-ECC-scalar-composition"></a>

### scalar-composition

`urn:csabs:theorem/ECC-scalar-composition`

**source:** [RFC 6090: Fundamental Elliptic Curve Cryptography Algorithms](https://www.rfc-editor.org/rfc/rfc6090.txt); accessedOn: 2026-11-11; sourceRole: primary algorithm specification

**sourceLocator:** RFC 6090 §§2.2–2.3, 3, 3.3–3.3.1, 10.1, Appendix F.1

**sourceNote:** Editorial consequence of the explicitly linked premises. Uses additive notation for the RFC group operation; selects prime fields, short-Weierstrass form and a prime-order subgroup. No parameter-strength recommendation is implied.

**provenanceKind:** derived

**statement:** Nested scalar multiplication multiplies scalars.

**formalStatement:** [a]([b]P)=[ab]P for a,b∈ℕ and P∈E.

**dependsOn:** [group-laws](ECC.md#node-urn-csabs-axiom-ECC-group-laws); [scalar-rule](ECC.md#node-urn-csabs-axiom-ECC-scalar-rule)

**proofSketch:** Induction and associativity first give [u+v]P=[u]P+[v]P. Induct on a, expanding the outer scalar recursion and combining the sums; the base is O.

**assumptions:** Fix prime p>3 and A,B∈𝔽_p with 4A³+27B²≠0. E includes O. Fix G∈E of prime order q≥2; H=⟨G⟩, h=|E|/q. E need not be cyclic. Equality is affine coordinate equality or O=O; equivalent projective encodings require a normalization/equivalence mapping. Scalar multiplication accepts k∈ℕ, including zero; addition and negation include O. All field arithmetic is exact modulo p. Other curve forms, characteristic 2 or 3, signatures and complete encryption protocols require separate instantiations.

**ruleRole:** derived-result

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial statement and proof sketch; not machine-checked.

## Concept provenance

- [RFC 6090: Fundamental Elliptic Curve Cryptography Algorithms](https://www.rfc-editor.org/rfc/rfc6090.txt); accessedOn: 2026-11-11; sourceRole: primary algorithm specification

**sourceLocator:** RFC 6090 §§2.2–2.3, 3, 3.3–3.3.1, 10.1, Appendix F.1

**sourceNote:** Uses additive notation for the RFC group operation; selects prime fields, short-Weierstrass form and a prime-order subgroup. No parameter-strength recommendation is implied.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/ECC",
    "type": "Concept",
    "shortForm": "ECC",
    "fullName": "Elliptic curve cryptography group (prime-field short-Weierstrass profile)",
    "definition": "The finite abelian point group and selected prime-order subgroup used as an algebraic foundation for elliptic curve cryptography. ECC names a family of schemes, not one encryption algorithm.",
    "notation": "E(𝔽_p)={(x,y) | y²=x³+Ax+B}∪{O}; H=⟨G⟩; [k]P.",
    "category": [
      "urn:csabs:category/public-key-cryptography"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "requiresConcept": [
      "urn:csabs:concept/FiniteField",
      "urn:csabs:concept/Group"
    ],
    "axiomBasis": "Nonsingular point carrier, complete affine addition with exceptional cases, inverse, group laws and recursive scalar multiplication.",
    "basisKind": "defined-structure",
    "basisScope": "Fix prime p>3 and A,B∈𝔽_p with 4A³+27B²≠0. E includes O. Fix G∈E of prime order q≥2; H=⟨G⟩, h=|E|/q. E need not be cyclic. Equality is affine coordinate equality or O=O; equivalent projective encodings require a normalization/equivalence mapping. Scalar multiplication accepts k∈ℕ, including zero; addition and negation include O. All field arithmetic is exact modulo p. Other curve forms, characteristic 2 or 3, signatures and complete encryption protocols require separate instantiations.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial mathematics; no compiled claim witness or cryptographic security proof.",
    "verificationObligation": [
      "Map representations, equality, parameter validation and failure behavior explicitly. Exact arithmetic has no overflow or rounding. Functional equations do not establish cryptographic security, entropy quality, constant-time behavior or secret erasure."
    ],
    "source": [
      "urn:csabs:source/rfc6090"
    ],
    "sourceLocator": "RFC 6090 §§2.2–2.3, 3, 3.3–3.3.1, 10.1, Appendix F.1",
    "sourceNote": "Uses additive notation for the RFC group operation; selects prime fields, short-Weierstrass form and a prime-order subgroup. No parameter-strength recommendation is implied.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/Group"
    ],
    "specializationNote": "Instantiate Group carrier by E(𝔽_p), multiplication by point addition, identity by O and inverse by point negation. The local group-laws record explicitly states applicability; FiniteField is a prerequisite, not a specialization parent.",
    "hasOperation": [
      "urn:csabs:operation/ECC-add",
      "urn:csabs:operation/ECC-negate",
      "urn:csabs:operation/ECC-scalar"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/ECC-carrier",
      "urn:csabs:axiom/ECC-addition",
      "urn:csabs:axiom/ECC-group-laws",
      "urn:csabs:axiom/ECC-scalar-rule"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/ECC-scalar-composition"
    ],
    "hasLaw": [],
    "leanFormulation": "structure ECCInterface (Point : Type) [AddCommGroup Point] where\n  basePoint : Point\n  subgroupOrder : Nat",
    "formulationSource": "urn:csabs:source/local-lean-Cryptography",
    "formulationLocator": "Catalog.ECCInterface",
    "formulationScope": "partial",
    "leanModelMapping": "Abstract AddCommGroup Point with a basePoint and subgroupOrder; publicPoint uses natural scalar multiplication. Equality is Lean point equality; zero interprets O.",
    "leanModelLimitations": "No field/affine representation, nonsingularity, selected subgroup, base-point order, coordinate equivalence or correspondence to the slope formulas is established.",
    "mathematicalFormulation": "The partial interpretation uses an abstract abelian additive group E with G∈E and subgroupOrder∈ℕ; publicPoint(a)=aG for a∈ℕ. Coordinates, curve nonsingularity and the exact order of G are not encoded."
  },
  {
    "id": "urn:csabs:operation/ECC-add",
    "type": "Operation",
    "name": "add",
    "source": [
      "urn:csabs:source/rfc6090"
    ],
    "sourceLocator": "RFC 6090 §§2.2–2.3, 3, 3.3–3.3.1, 10.1, Appendix F.1",
    "sourceNote": "Uses additive notation for the RFC group operation; selects prime fields, short-Weierstrass form and a prime-order subgroup. No parameter-strength recommendation is implied.",
    "provenanceKind": "adapted",
    "signature": "add : E×E → E",
    "description": "Complete point addition on the fixed curve.",
    "precondition": "Both inputs are valid points of this same E.",
    "postcondition": "Use O as identity; inverse pairs give O; all remaining cases use the slope rule.",
    "concept": "urn:csabs:concept/ECC",
    "totality": "Total on the stated mathematical domain; malformed or out-of-domain external input is rejected without a result."
  },
  {
    "id": "urn:csabs:operation/ECC-negate",
    "type": "Operation",
    "name": "negate",
    "source": [
      "urn:csabs:source/rfc6090"
    ],
    "sourceLocator": "RFC 6090 §§2.2–2.3, 3, 3.3–3.3.1, 10.1, Appendix F.1",
    "sourceNote": "Uses additive notation for the RFC group operation; selects prime fields, short-Weierstrass form and a prime-order subgroup. No parameter-strength recommendation is implied.",
    "provenanceKind": "adapted",
    "signature": "neg : E → E",
    "description": "Additive inverse of a point.",
    "precondition": "P∈E.",
    "postcondition": "−O=O; −(x,y)=(x,−y).",
    "concept": "urn:csabs:concept/ECC",
    "totality": "Total on the stated mathematical domain; malformed or out-of-domain external input is rejected without a result."
  },
  {
    "id": "urn:csabs:operation/ECC-scalar",
    "type": "Operation",
    "name": "scalar",
    "source": [
      "urn:csabs:source/rfc6090"
    ],
    "sourceLocator": "RFC 6090 §§2.2–2.3, 3, 3.3–3.3.1, 10.1, Appendix F.1",
    "sourceNote": "Uses additive notation for the RFC group operation; selects prime fields, short-Weierstrass form and a prime-order subgroup. No parameter-strength recommendation is implied.",
    "provenanceKind": "adapted",
    "signature": "smul : ℕ×E → E",
    "description": "Repeated point addition, with the empty sum defined.",
    "precondition": "k≥0; P∈E.",
    "postcondition": "[0]P=O; [k+1]P=[k]P+P.",
    "concept": "urn:csabs:concept/ECC",
    "totality": "Total on the stated mathematical domain; malformed or out-of-domain external input is rejected without a result."
  },
  {
    "id": "urn:csabs:axiom/ECC-carrier",
    "type": "Axiom",
    "name": "carrier",
    "source": [
      "urn:csabs:source/rfc6090"
    ],
    "sourceLocator": "RFC 6090 §§2.2–2.3, 3, 3.3–3.3.1, 10.1, Appendix F.1",
    "sourceNote": "Uses additive notation for the RFC group operation; selects prime fields, short-Weierstrass form and a prime-order subgroup. No parameter-strength recommendation is implied.",
    "provenanceKind": "adapted",
    "statement": "The chosen curve is nonsingular and includes its identity; G has prime order.",
    "formalStatement": "p>3 prime; 4A³+27B²≠0 in 𝔽_p; E={(x,y)∈𝔽_p² | y²=x³+Ax+B}∪{O}; ord(G)=q prime; H=⟨G⟩.",
    "appliesTo": [
      "urn:csabs:concept/ECC"
    ],
    "assumptions": [
      "Fix prime p>3 and A,B∈𝔽_p with 4A³+27B²≠0. E includes O. Fix G∈E of prime order q≥2; H=⟨G⟩, h=|E|/q. E need not be cyclic. Equality is affine coordinate equality or O=O; equivalent projective encodings require a normalization/equivalence mapping. Scalar multiplication accepts k∈ℕ, including zero; addition and negation include O. All field arithmetic is exact modulo p. Other curve forms, characteristic 2 or 3, signatures and complete encryption protocols require separate instantiations."
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial statement and proof sketch; not machine-checked."
  },
  {
    "id": "urn:csabs:axiom/ECC-addition",
    "type": "Axiom",
    "name": "addition",
    "source": [
      "urn:csabs:source/rfc6090"
    ],
    "sourceLocator": "RFC 6090 §§2.2–2.3, 3, 3.3–3.3.1, 10.1, Appendix F.1",
    "sourceNote": "Uses additive notation for the RFC group operation; selects prime fields, short-Weierstrass form and a prime-order subgroup. No parameter-strength recommendation is implied.",
    "provenanceKind": "adapted",
    "statement": "The affine slope rule handles identity and vertical-tangent cases before division.",
    "formalStatement": "O+P=P+O=P; −O=O; −(x,y)=(x,−y). For affine P=(x₁,y₁), Q=(x₂,y₂): if Q=−P return O; otherwise s=(y₂−y₁)/(x₂−x₁) when x₁≠x₂, and s=(3x₁²+A)/(2y₁) when P=Q with y₁≠0; x₃=s²−x₁−x₂; y₃=s(x₁−x₃)−y₁; P+Q=(x₃,y₃).",
    "appliesTo": [
      "urn:csabs:concept/ECC"
    ],
    "assumptions": [
      "Fix prime p>3 and A,B∈𝔽_p with 4A³+27B²≠0. E includes O. Fix G∈E of prime order q≥2; H=⟨G⟩, h=|E|/q. E need not be cyclic. Equality is affine coordinate equality or O=O; equivalent projective encodings require a normalization/equivalence mapping. Scalar multiplication accepts k∈ℕ, including zero; addition and negation include O. All field arithmetic is exact modulo p. Other curve forms, characteristic 2 or 3, signatures and complete encryption protocols require separate instantiations."
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial statement and proof sketch; not machine-checked."
  },
  {
    "id": "urn:csabs:axiom/ECC-group-laws",
    "type": "Axiom",
    "name": "group-laws",
    "source": [
      "urn:csabs:source/rfc6090"
    ],
    "sourceLocator": "RFC 6090 §§2.2–2.3, 3, 3.3–3.3.1, 10.1, Appendix F.1",
    "sourceNote": "Uses additive notation for the RFC group operation; selects prime fields, short-Weierstrass form and a prime-order subgroup. No parameter-strength recommendation is implied.",
    "provenanceKind": "adapted",
    "statement": "The selected point operation satisfies the abelian group interface.",
    "formalStatement": "P+Q∈E; (P+Q)+R=P+(Q+R); P+Q=Q+P; P+O=O+P=P; P+(−P)=(−P)+P=O.",
    "ruleRole": "structure-law",
    "appliesTo": [
      "urn:csabs:concept/ECC"
    ],
    "assumptions": [
      "Fix prime p>3 and A,B∈𝔽_p with 4A³+27B²≠0. E includes O. Fix G∈E of prime order q≥2; H=⟨G⟩, h=|E|/q. E need not be cyclic. Equality is affine coordinate equality or O=O; equivalent projective encodings require a normalization/equivalence mapping. Scalar multiplication accepts k∈ℕ, including zero; addition and negation include O. All field arithmetic is exact modulo p. Other curve forms, characteristic 2 or 3, signatures and complete encryption protocols require separate instantiations."
    ],
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial statement and proof sketch; not machine-checked."
  },
  {
    "id": "urn:csabs:axiom/ECC-scalar-rule",
    "type": "Axiom",
    "name": "scalar-rule",
    "source": [
      "urn:csabs:source/rfc6090"
    ],
    "sourceLocator": "RFC 6090 §§2.2–2.3, 3, 3.3–3.3.1, 10.1, Appendix F.1",
    "sourceNote": "Uses additive notation for the RFC group operation; selects prime fields, short-Weierstrass form and a prime-order subgroup. No parameter-strength recommendation is implied.",
    "provenanceKind": "adapted",
    "statement": "Natural scalar multiplication is the repeated group sum.",
    "formalStatement": "[0]P=O; [k+1]P=[k]P+P for k∈ℕ.",
    "appliesTo": [
      "urn:csabs:concept/ECC"
    ],
    "assumptions": [
      "Fix prime p>3 and A,B∈𝔽_p with 4A³+27B²≠0. E includes O. Fix G∈E of prime order q≥2; H=⟨G⟩, h=|E|/q. E need not be cyclic. Equality is affine coordinate equality or O=O; equivalent projective encodings require a normalization/equivalence mapping. Scalar multiplication accepts k∈ℕ, including zero; addition and negation include O. All field arithmetic is exact modulo p. Other curve forms, characteristic 2 or 3, signatures and complete encryption protocols require separate instantiations."
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial statement and proof sketch; not machine-checked."
  },
  {
    "id": "urn:csabs:theorem/ECC-scalar-composition",
    "type": "Theorem",
    "name": "scalar-composition",
    "source": [
      "urn:csabs:source/rfc6090"
    ],
    "sourceLocator": "RFC 6090 §§2.2–2.3, 3, 3.3–3.3.1, 10.1, Appendix F.1",
    "sourceNote": "Editorial consequence of the explicitly linked premises. Uses additive notation for the RFC group operation; selects prime fields, short-Weierstrass form and a prime-order subgroup. No parameter-strength recommendation is implied.",
    "provenanceKind": "derived",
    "statement": "Nested scalar multiplication multiplies scalars.",
    "formalStatement": "[a]([b]P)=[ab]P for a,b∈ℕ and P∈E.",
    "dependsOn": [
      "urn:csabs:axiom/ECC-group-laws",
      "urn:csabs:axiom/ECC-scalar-rule"
    ],
    "proofSketch": "Induction and associativity first give [u+v]P=[u]P+[v]P. Induct on a, expanding the outer scalar recursion and combining the sums; the base is O.",
    "appliesTo": [
      "urn:csabs:concept/ECC"
    ],
    "assumptions": [
      "Fix prime p>3 and A,B∈𝔽_p with 4A³+27B²≠0. E includes O. Fix G∈E of prime order q≥2; H=⟨G⟩, h=|E|/q. E need not be cyclic. Equality is affine coordinate equality or O=O; equivalent projective encodings require a normalization/equivalence mapping. Scalar multiplication accepts k∈ℕ, including zero; addition and negation include O. All field arithmetic is exact modulo p. Other curve forms, characteristic 2 or 3, signatures and complete encryption protocols require separate instantiations."
    ],
    "ruleRole": "derived-result",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial statement and proof sketch; not machine-checked."
  }
]
```
<!-- graph-record:end -->
