# Finite field (Galois field)

A field with finitely many elements, also called a Galois field.

**Notation:** GF(q) = 𝔽_q; q = p^n, p prime, n ≥ 1.

**Stable ID:** `urn:csabs:concept/FiniteField`

**Categories:** Algebra, Numeric computation

**Kind:** Mathematical structure

**Prerequisites:** [Field](Field.md)

**Specializes:** [Field](Field.md)

**Related concepts:** [Group](Group.md), [Modular Integer](ModularInteger.md)

## Backlinks

- [Advanced Encryption Standard (AES)](AES.md) — `requiresConcept`
- [Elliptic curve cryptography group (prime-field short-Weierstrass profile)](ECC.md) — `requiresConcept`
- [GHASH polynomial accumulator](GHASH.md) — `requiresConcept`
- [Linear block code over a finite field](LinearBlockCode.md) — `requiresConcept`
- [Nonlinear finite-field block code](NonlinearBlockCode.md) — `requiresConcept`
- [RSA modular-exponentiation primitives (two-prime profile)](RSA.md) — `relatedConcept`

## Mathematical formulation

A finite field is a field F with finite carrier: 0≠1, commutative ring operations and inverses for nonzero elements, together with |F|<∞. No concrete residue encoding is selected by this model.

**Lean formulation** (in its source module context):

```lean
class FiniteField (A : Type u) extends _root_.Field A where
  carrier_finite : Finite A
```

**Source:** [`Catalog.FiniteField`](../lean/Catalog/Algebra.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Mathlib Field A with an explicit Finite A witness, equality of elements, and unchanged exact operations. Catalog inverse/division restrict Mathlib total operations to nonzero inputs.

**Limits:** No chosen size, polynomial basis or encoding. No proof witnesses for the new finite-field classification or Frobenius results.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** The explicitly linked field laws (commutative unital ring, 0 ≠ 1, inverses for nonzero elements) and finite carrier. Prime-power order is derived, not an extra axiom.

**basisKind:** axiomatic-structure

**basisScope:** Exact finite-field interface and selected classification results. No encoding or algorithms are fixed.

**convention:** Equality is carrier equality. Zero and one are distinct, so the carrier has at least two elements. Inversion and division are partial at zero. Arithmetic has no rounding or overflow.

**specializationNote:** Use the same carrier K and field operations; add finiteness. Field axioms are linked explicitly with applicability to K, rather than inherited.

**verificationObligation:** Choose an explicit field representation and an equality-preserving mapping before applying these laws to software. GF(p^n) is not the residue ring modulo p^n when n > 1.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-finite-field-addition"></a>

### addition

`urn:csabs:operation/finite-field-addition`

**signature:** + : K×K→K

**description:** Field sum.

**precondition:** a,b ∈ K

**definedness:** Total.

<a id="node-urn-csabs-operation-finite-field-multiplication"></a>

### multiplication

`urn:csabs:operation/finite-field-multiplication`

**signature:** · : K×K→K

**description:** Field product.

**precondition:** a,b ∈ K

**definedness:** Total.

<a id="node-urn-csabs-operation-finite-field-negation"></a>

### additive inverse

`urn:csabs:operation/finite-field-negation`

**signature:** neg : K→K

**description:** Returns b with a+b=0.

**precondition:** a ∈ K

**definedness:** Total.

<a id="node-urn-csabs-operation-finite-field-zero"></a>

### zero

`urn:csabs:operation/finite-field-zero`

**signature:** 0 : K

**description:** Additive identity.

**precondition:** None.

**definedness:** Constant.

<a id="node-urn-csabs-operation-finite-field-one"></a>

### one

`urn:csabs:operation/finite-field-one`

**signature:** 1 : K

**description:** Multiplicative identity distinct from zero.

**precondition:** None.

**definedness:** Constant.

<a id="node-urn-csabs-operation-finite-field-inverse"></a>

### multiplicative inverse

`urn:csabs:operation/finite-field-inverse`

**signature:** inv : K\{0}→K\{0}

**description:** Returns b with ab=1.

**precondition:** a ≠ 0

**definedness:** Undefined at zero.

<a id="node-urn-csabs-operation-finite-field-division"></a>

### division

`urn:csabs:operation/finite-field-division`

**signature:** / : K×(K\{0})→K

**description:** a/b = a·inv(b).

**precondition:** b ≠ 0

**definedness:** Undefined for zero divisor input b; otherwise total.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-field-commutative-ring"></a>

### field-commutative-ring

`urn:csabs:axiom/field-commutative-ring`

**statement:** The ring operations satisfy the commutative unital ring laws and zero differs from one.

**formalStatement:** 0≠1

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

**assumptions:** Use the linked concept’s explicit basis and carrier conventions.

**source:** [Mathlib: field definitions (consulted 2026-11-08)](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Field/Defs.html); accessedOn: 2026-11-08; sourceRole: reference-for-selected-basis

**sourceLocator:** Field and Semifield: commutative ring, nontriviality and nonzero inverses

**sourceNote:** Field structure law, instantiated on either F or the finite carrier K; no inheritance through specialization edges.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-field-nonzero-inverses"></a>

### field-nonzero-inverses

`urn:csabs:axiom/field-nonzero-inverses`

**statement:** Every nonzero field element has a multiplicative inverse.

**formalStatement:** ∀x∈F\{0} ∃y∈F: xy=1

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

**assumptions:** Use the linked concept’s explicit basis and carrier conventions.

**source:** [Mathlib: field definitions (consulted 2026-11-08)](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Field/Defs.html); accessedOn: 2026-11-08; sourceRole: reference-for-selected-basis

**sourceLocator:** Field and Semifield: commutative ring, nontriviality and nonzero inverses

**sourceNote:** Field structure law, instantiated on either F or the finite carrier K; no inheritance through specialization edges.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-Field-closure"></a>

### closure

`urn:csabs:axiom/Field-closure`

**statement:** The carrier contains the constants and is closed under both operations.

**formalStatement:** 0,1∈S; +,·:S×S→S

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Mathlib: field definitions (consulted 2026-11-08)](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Field/Defs.html); accessedOn: 2026-11-08; sourceRole: reference-for-selected-basis

**sourceLocator:** Field and Semifield: commutative ring, nontriviality and nonzero inverses

**sourceNote:** Field structure law, instantiated on either F or the finite carrier K; no inheritance through specialization edges.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-Field-add-associative"></a>

### add-associative

`urn:csabs:axiom/Field-add-associative`

**statement:** Addition is associative.

**formalStatement:** (x+y)+z=x+(y+z)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Mathlib: field definitions (consulted 2026-11-08)](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Field/Defs.html); accessedOn: 2026-11-08; sourceRole: reference-for-selected-basis

**sourceLocator:** Field and Semifield: commutative ring, nontriviality and nonzero inverses

**sourceNote:** Field structure law, instantiated on either F or the finite carrier K; no inheritance through specialization edges.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-Field-add-commutative"></a>

### add-commutative

`urn:csabs:axiom/Field-add-commutative`

**statement:** Addition commutes.

**formalStatement:** x+y=y+x

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Mathlib: field definitions (consulted 2026-11-08)](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Field/Defs.html); accessedOn: 2026-11-08; sourceRole: reference-for-selected-basis

**sourceLocator:** Field and Semifield: commutative ring, nontriviality and nonzero inverses

**sourceNote:** Field structure law, instantiated on either F or the finite carrier K; no inheritance through specialization edges.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-Field-add-zero"></a>

### add-zero

`urn:csabs:axiom/Field-add-zero`

**statement:** Zero is the additive identity.

**formalStatement:** 0+x=x; x+0=x

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Mathlib: field definitions (consulted 2026-11-08)](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Field/Defs.html); accessedOn: 2026-11-08; sourceRole: reference-for-selected-basis

**sourceLocator:** Field and Semifield: commutative ring, nontriviality and nonzero inverses

**sourceNote:** Field structure law, instantiated on either F or the finite carrier K; no inheritance through specialization edges.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-Field-mul-associative"></a>

### mul-associative

`urn:csabs:axiom/Field-mul-associative`

**statement:** Multiplication is associative.

**formalStatement:** (xy)z=x(yz)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Mathlib: field definitions (consulted 2026-11-08)](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Field/Defs.html); accessedOn: 2026-11-08; sourceRole: reference-for-selected-basis

**sourceLocator:** Field and Semifield: commutative ring, nontriviality and nonzero inverses

**sourceNote:** Field structure law, instantiated on either F or the finite carrier K; no inheritance through specialization edges.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-Field-mul-unit"></a>

### mul-unit

`urn:csabs:axiom/Field-mul-unit`

**statement:** One is the multiplicative identity.

**formalStatement:** 1x=x; x1=x

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Mathlib: field definitions (consulted 2026-11-08)](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Field/Defs.html); accessedOn: 2026-11-08; sourceRole: reference-for-selected-basis

**sourceLocator:** Field and Semifield: commutative ring, nontriviality and nonzero inverses

**sourceNote:** Field structure law, instantiated on either F or the finite carrier K; no inheritance through specialization edges.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-Field-distributive"></a>

### distributive

`urn:csabs:axiom/Field-distributive`

**statement:** Multiplication distributes over addition on both sides.

**formalStatement:** x(y+z)=xy+xz; (x+y)z=xz+yz

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Mathlib: field definitions (consulted 2026-11-08)](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Field/Defs.html); accessedOn: 2026-11-08; sourceRole: reference-for-selected-basis

**sourceLocator:** Field and Semifield: commutative ring, nontriviality and nonzero inverses

**sourceNote:** Field structure law, instantiated on either F or the finite carrier K; no inheritance through specialization edges.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-Field-add-inverse"></a>

### add-inverse

`urn:csabs:axiom/Field-add-inverse`

**statement:** Every element has an additive inverse.

**formalStatement:** neg:S→S; x+neg(x)=0; neg(x)+x=0

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Mathlib: field definitions (consulted 2026-11-08)](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Field/Defs.html); accessedOn: 2026-11-08; sourceRole: reference-for-selected-basis

**sourceLocator:** Field and Semifield: commutative ring, nontriviality and nonzero inverses

**sourceNote:** Field structure law, instantiated on either F or the finite carrier K; no inheritance through specialization edges.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-Field-nontrivial"></a>

### nontrivial

`urn:csabs:axiom/Field-nontrivial`

**statement:** Zero and one are distinct.

**formalStatement:** 0≠1

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Mathlib: field definitions (consulted 2026-11-08)](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Field/Defs.html); accessedOn: 2026-11-08; sourceRole: reference-for-selected-basis

**sourceLocator:** Field and Semifield: commutative ring, nontriviality and nonzero inverses

**sourceNote:** Field structure law, instantiated on either F or the finite carrier K; no inheritance through specialization edges.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-Field-mul-commutative"></a>

### mul-commutative

`urn:csabs:axiom/Field-mul-commutative`

**statement:** Multiplication commutes.

**formalStatement:** xy=yx

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Mathlib: field definitions (consulted 2026-11-08)](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Field/Defs.html); accessedOn: 2026-11-08; sourceRole: reference-for-selected-basis

**sourceLocator:** Field and Semifield: commutative ring, nontriviality and nonzero inverses

**sourceNote:** Field structure law, instantiated on either F or the finite carrier K; no inheritance through specialization edges.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-Field-nonzero-inverse"></a>

### nonzero-inverse

`urn:csabs:axiom/Field-nonzero-inverse`

**statement:** Nonzero elements admit inverses.

**formalStatement:** ∀x≠0 ∃y:xy=yx=1

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Mathlib: field definitions (consulted 2026-11-08)](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Field/Defs.html); accessedOn: 2026-11-08; sourceRole: reference-for-selected-basis

**sourceLocator:** Field and Semifield: commutative ring, nontriviality and nonzero inverses

**sourceNote:** Field structure law, instantiated on either F or the finite carrier K; no inheritance through specialization edges.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-FiniteField-finiteness"></a>

### finite carrier

`urn:csabs:axiom/FiniteField-finiteness`

**statement:** The field carrier is finite.

**formalStatement:** |K| < ∞

**assumptions:** K carries the explicitly linked field structure.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**source:** [Keith Conrad: Finite Fields](https://kconrad.math.uconn.edu/blurbs/galoistheory/finitefields.pdf); accessedOn: 2026-11-08; sourceRole: reference-for-selected-basis

**sourceLocator:** Section 1, definition and Theorem 1.5

**sourceNote:** Finiteness condition; prime-power order remains a derived result.

**provenanceKind:** adapted

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-FiniteField-prime-power-order"></a>

### prime-power order

`urn:csabs:theorem/FiniteField-prime-power-order`

**statement:** A finite field has characteristic p and order p^n for a prime p and n ≥ 1.

**formalStatement:** ∃ prime p, n≥1: char(K)=p ∧ |K|=p^n

**proofSketch:** The prime subfield is ℤ/pℤ; a finite basis of K over it counts p^n elements.

**assumptions:** K is a finite field.

**dependsOn:** [field-commutative-ring](Field.md#node-urn-csabs-axiom-field-commutative-ring); [field-nonzero-inverses](Field.md#node-urn-csabs-axiom-field-nonzero-inverses); [closure](Field.md#node-urn-csabs-axiom-Field-closure); [add-associative](Field.md#node-urn-csabs-axiom-Field-add-associative); [add-commutative](Field.md#node-urn-csabs-axiom-Field-add-commutative); [add-zero](Field.md#node-urn-csabs-axiom-Field-add-zero); [mul-associative](Field.md#node-urn-csabs-axiom-Field-mul-associative); [mul-unit](Field.md#node-urn-csabs-axiom-Field-mul-unit); [distributive](Field.md#node-urn-csabs-axiom-Field-distributive); [add-inverse](Field.md#node-urn-csabs-axiom-Field-add-inverse); [nontrivial](Field.md#node-urn-csabs-axiom-Field-nontrivial); [mul-commutative](Field.md#node-urn-csabs-axiom-Field-mul-commutative); [nonzero-inverse](Field.md#node-urn-csabs-axiom-Field-nonzero-inverse); [finite carrier](FiniteField.md#node-urn-csabs-axiom-FiniteField-finiteness)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Keith Conrad: Finite Fields](https://kconrad.math.uconn.edu/blurbs/galoistheory/finitefields.pdf); accessedOn: 2026-11-08; sourceRole: reference-for-selected-basis

**sourceLocator:** Theorem 1.5

**sourceNote:** Editorial restatement with informal proof outline; auxiliary field theory is stated in the sketch.

**provenanceKind:** derived

<a id="node-urn-csabs-theorem-FiniteField-existence-uniqueness"></a>

### existence and uniqueness up to isomorphism

`urn:csabs:theorem/FiniteField-existence-uniqueness`

**statement:** Every prime power is the size of a field, unique up to field isomorphism.

**formalStatement:** p prime ∧ n≥1 ⇒ ∃K, |K|=p^n; |K|=|L|=p^n ⇒ K≅L

**proofSketch:** In a splitting field of X^(p^n)−X over 𝔽_p the roots form a field. The derivative −1 gives exactly p^n roots. Uniqueness uses uniqueness of splitting fields.

**assumptions:** p is prime and n is a positive integer.; K and L in the uniqueness clause are finite fields.

**dependsOn:** [prime-power order](FiniteField.md#node-urn-csabs-theorem-FiniteField-prime-power-order)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [J. S. Milne: Fields and Galois Theory, version 5.10 (2022)](https://www.jmilne.org/math/CourseNotes/FT.pdf); accessedOn: 2026-11-08; sourceRole: reference-for-selected-basis

**sourceLocator:** Section 4, Proposition 4.20

**sourceNote:** Editorial restatement with informal proof outline; auxiliary field theory is stated in the sketch.

**provenanceKind:** derived

<a id="node-urn-csabs-theorem-FiniteField-frobenius"></a>

### Frobenius automorphism

`urn:csabs:theorem/FiniteField-frobenius`

**statement:** The p-th power map is an automorphism of GF(p^n) whose n-th iterate is identity.

**formalStatement:** Fr(a)=a^p; Fr(a+b)=Fr(a)+Fr(b); Fr(ab)=Fr(a)Fr(b); Fr^n=id_K

**proofSketch:** In characteristic p the binomial formula preserves addition. Powers preserve products; the map is injective, hence bijective on a finite carrier. Every element satisfies a^(p^n)=a.

**assumptions:** K is a field of order p^n with p prime and n≥1.

**dependsOn:** [prime-power order](FiniteField.md#node-urn-csabs-theorem-FiniteField-prime-power-order); [existence and uniqueness up to isomorphism](FiniteField.md#node-urn-csabs-theorem-FiniteField-existence-uniqueness)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [J. S. Milne: Fields and Galois Theory, version 5.10 (2022)](https://www.jmilne.org/math/CourseNotes/FT.pdf); accessedOn: 2026-11-08; sourceRole: reference-for-selected-basis

**sourceLocator:** Section 4, Proposition 4.20 and its preceding construction

**sourceNote:** Editorial restatement with informal proof outline; auxiliary field theory is stated in the sketch.

**provenanceKind:** derived

## Concept provenance

- [Keith Conrad: Finite Fields](https://kconrad.math.uconn.edu/blurbs/galoistheory/finitefields.pdf); accessedOn: 2026-11-08; sourceRole: reference-for-selected-basis

**sourceLocator:** Section 1, Theorems 1.1 and 1.5; warning after Example 1.4

**sourceNote:** Finite field definition and distinction from composite-modulus residue rings.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/FiniteField",
    "type": "Concept",
    "shortForm": "FiniteField",
    "fullName": "Finite field (Galois field)",
    "category": [
      "urn:csabs:category/algebra",
      "urn:csabs:category/numeric-computation"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "A field with finitely many elements, also called a Galois field.",
    "notation": "GF(q) = 𝔽_q; q = p^n, p prime, n ≥ 1.",
    "specializationOf": [
      "urn:csabs:concept/Field"
    ],
    "requiresConcept": [
      "urn:csabs:concept/Field"
    ],
    "relatedConcept": [
      "urn:csabs:concept/Group",
      "urn:csabs:concept/ModularInteger"
    ],
    "specializationNote": "Use the same carrier K and field operations; add finiteness. Field axioms are linked explicitly with applicability to K, rather than inherited.",
    "axiomBasis": "The explicitly linked field laws (commutative unital ring, 0 ≠ 1, inverses for nonzero elements) and finite carrier. Prime-power order is derived, not an extra axiom.",
    "basisKind": "axiomatic-structure",
    "basisScope": "Exact finite-field interface and selected classification results. No encoding or algorithms are fixed.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "convention": "Equality is carrier equality. Zero and one are distinct, so the carrier has at least two elements. Inversion and division are partial at zero. Arithmetic has no rounding or overflow.",
    "verificationObligation": [
      "Choose an explicit field representation and an equality-preserving mapping before applying these laws to software. GF(p^n) is not the residue ring modulo p^n when n > 1."
    ],
    "hasOperation": [
      "urn:csabs:operation/finite-field-addition",
      "urn:csabs:operation/finite-field-multiplication",
      "urn:csabs:operation/finite-field-negation",
      "urn:csabs:operation/finite-field-zero",
      "urn:csabs:operation/finite-field-one",
      "urn:csabs:operation/finite-field-inverse",
      "urn:csabs:operation/finite-field-division"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/field-commutative-ring",
      "urn:csabs:axiom/field-nonzero-inverses",
      "urn:csabs:axiom/Field-closure",
      "urn:csabs:axiom/Field-add-associative",
      "urn:csabs:axiom/Field-add-commutative",
      "urn:csabs:axiom/Field-add-zero",
      "urn:csabs:axiom/Field-mul-associative",
      "urn:csabs:axiom/Field-mul-unit",
      "urn:csabs:axiom/Field-distributive",
      "urn:csabs:axiom/Field-add-inverse",
      "urn:csabs:axiom/Field-nontrivial",
      "urn:csabs:axiom/Field-mul-commutative",
      "urn:csabs:axiom/Field-nonzero-inverse",
      "urn:csabs:axiom/FiniteField-finiteness"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/FiniteField-prime-power-order",
      "urn:csabs:theorem/FiniteField-existence-uniqueness",
      "urn:csabs:theorem/FiniteField-frobenius"
    ],
    "source": [
      "urn:csabs:source/conrad-finite-fields"
    ],
    "sourceLocator": "Section 1, Theorems 1.1 and 1.5; warning after Example 1.4",
    "sourceNote": "Finite field definition and distinction from composite-modulus residue rings.",
    "provenanceKind": "adapted",
    "leanFormulation": "class FiniteField (A : Type u) extends _root_.Field A where\n  carrier_finite : Finite A",
    "formulationSource": "urn:csabs:source/local-lean-Algebra",
    "formulationLocator": "Catalog.FiniteField",
    "formulationScope": "model",
    "leanModelMapping": "Mathlib Field A with an explicit Finite A witness, equality of elements, and unchanged exact operations. Catalog inverse/division restrict Mathlib total operations to nonzero inputs.",
    "leanModelLimitations": "No chosen size, polynomial basis or encoding. No proof witnesses for the new finite-field classification or Frobenius results.",
    "mathematicalFormulation": "A finite field is a field F with finite carrier: 0≠1, commutative ring operations and inverses for nonzero elements, together with |F|<∞. No concrete residue encoding is selected by this model."
  },
  {
    "id": "urn:csabs:operation/finite-field-addition",
    "type": "Operation",
    "name": "addition",
    "signature": "+ : K×K→K",
    "description": "Field sum.",
    "precondition": "a,b ∈ K",
    "definedness": "Total.",
    "concept": "urn:csabs:concept/FiniteField"
  },
  {
    "id": "urn:csabs:operation/finite-field-multiplication",
    "type": "Operation",
    "name": "multiplication",
    "signature": "· : K×K→K",
    "description": "Field product.",
    "precondition": "a,b ∈ K",
    "definedness": "Total.",
    "concept": "urn:csabs:concept/FiniteField"
  },
  {
    "id": "urn:csabs:operation/finite-field-negation",
    "type": "Operation",
    "name": "additive inverse",
    "signature": "neg : K→K",
    "description": "Returns b with a+b=0.",
    "precondition": "a ∈ K",
    "definedness": "Total.",
    "concept": "urn:csabs:concept/FiniteField"
  },
  {
    "id": "urn:csabs:operation/finite-field-zero",
    "type": "Operation",
    "name": "zero",
    "signature": "0 : K",
    "description": "Additive identity.",
    "precondition": "None.",
    "definedness": "Constant.",
    "concept": "urn:csabs:concept/FiniteField"
  },
  {
    "id": "urn:csabs:operation/finite-field-one",
    "type": "Operation",
    "name": "one",
    "signature": "1 : K",
    "description": "Multiplicative identity distinct from zero.",
    "precondition": "None.",
    "definedness": "Constant.",
    "concept": "urn:csabs:concept/FiniteField"
  },
  {
    "id": "urn:csabs:operation/finite-field-inverse",
    "type": "Operation",
    "name": "multiplicative inverse",
    "signature": "inv : K\\{0}→K\\{0}",
    "description": "Returns b with ab=1.",
    "precondition": "a ≠ 0",
    "definedness": "Undefined at zero.",
    "concept": "urn:csabs:concept/FiniteField"
  },
  {
    "id": "urn:csabs:operation/finite-field-division",
    "type": "Operation",
    "name": "division",
    "signature": "/ : K×(K\\{0})→K",
    "description": "a/b = a·inv(b).",
    "precondition": "b ≠ 0",
    "definedness": "Undefined for zero divisor input b; otherwise total.",
    "concept": "urn:csabs:concept/FiniteField"
  },
  {
    "id": "urn:csabs:axiom/FiniteField-finiteness",
    "type": "Axiom",
    "name": "finite carrier",
    "statement": "The field carrier is finite.",
    "formalStatement": "|K| < ∞",
    "assumptions": [
      "K carries the explicitly linked field structure."
    ],
    "appliesTo": [
      "urn:csabs:concept/FiniteField"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "source": [
      "urn:csabs:source/conrad-finite-fields"
    ],
    "sourceLocator": "Section 1, definition and Theorem 1.5",
    "sourceNote": "Finiteness condition; prime-power order remains a derived result.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:theorem/FiniteField-prime-power-order",
    "type": "Theorem",
    "name": "prime-power order",
    "statement": "A finite field has characteristic p and order p^n for a prime p and n ≥ 1.",
    "formalStatement": "∃ prime p, n≥1: char(K)=p ∧ |K|=p^n",
    "proofSketch": "The prime subfield is ℤ/pℤ; a finite basis of K over it counts p^n elements.",
    "assumptions": [
      "K is a finite field."
    ],
    "appliesTo": [
      "urn:csabs:concept/FiniteField"
    ],
    "dependsOn": [
      "urn:csabs:axiom/field-commutative-ring",
      "urn:csabs:axiom/field-nonzero-inverses",
      "urn:csabs:axiom/Field-closure",
      "urn:csabs:axiom/Field-add-associative",
      "urn:csabs:axiom/Field-add-commutative",
      "urn:csabs:axiom/Field-add-zero",
      "urn:csabs:axiom/Field-mul-associative",
      "urn:csabs:axiom/Field-mul-unit",
      "urn:csabs:axiom/Field-distributive",
      "urn:csabs:axiom/Field-add-inverse",
      "urn:csabs:axiom/Field-nontrivial",
      "urn:csabs:axiom/Field-mul-commutative",
      "urn:csabs:axiom/Field-nonzero-inverse",
      "urn:csabs:axiom/FiniteField-finiteness"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/conrad-finite-fields"
    ],
    "sourceLocator": "Theorem 1.5",
    "sourceNote": "Editorial restatement with informal proof outline; auxiliary field theory is stated in the sketch.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/FiniteField-existence-uniqueness",
    "type": "Theorem",
    "name": "existence and uniqueness up to isomorphism",
    "statement": "Every prime power is the size of a field, unique up to field isomorphism.",
    "formalStatement": "p prime ∧ n≥1 ⇒ ∃K, |K|=p^n; |K|=|L|=p^n ⇒ K≅L",
    "proofSketch": "In a splitting field of X^(p^n)−X over 𝔽_p the roots form a field. The derivative −1 gives exactly p^n roots. Uniqueness uses uniqueness of splitting fields.",
    "assumptions": [
      "p is prime and n is a positive integer.",
      "K and L in the uniqueness clause are finite fields."
    ],
    "appliesTo": [
      "urn:csabs:concept/FiniteField"
    ],
    "dependsOn": [
      "urn:csabs:theorem/FiniteField-prime-power-order"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/milne-fields-galois-5-10"
    ],
    "sourceLocator": "Section 4, Proposition 4.20",
    "sourceNote": "Editorial restatement with informal proof outline; auxiliary field theory is stated in the sketch.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/FiniteField-frobenius",
    "type": "Theorem",
    "name": "Frobenius automorphism",
    "statement": "The p-th power map is an automorphism of GF(p^n) whose n-th iterate is identity.",
    "formalStatement": "Fr(a)=a^p; Fr(a+b)=Fr(a)+Fr(b); Fr(ab)=Fr(a)Fr(b); Fr^n=id_K",
    "proofSketch": "In characteristic p the binomial formula preserves addition. Powers preserve products; the map is injective, hence bijective on a finite carrier. Every element satisfies a^(p^n)=a.",
    "assumptions": [
      "K is a field of order p^n with p prime and n≥1."
    ],
    "appliesTo": [
      "urn:csabs:concept/FiniteField"
    ],
    "dependsOn": [
      "urn:csabs:theorem/FiniteField-prime-power-order",
      "urn:csabs:theorem/FiniteField-existence-uniqueness"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/milne-fields-galois-5-10"
    ],
    "sourceLocator": "Section 4, Proposition 4.20 and its preceding construction",
    "sourceNote": "Editorial restatement with informal proof outline; auxiliary field theory is stated in the sketch.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
