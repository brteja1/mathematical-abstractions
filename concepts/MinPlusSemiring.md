# Min-plus semiring (tropical semiring, min convention)

The real min-plus algebra: minimum combines alternative costs and extended ordinary addition combines costs in sequence. Also called the tropical semiring in the min-plus convention; TropicalSemiring is an alias here, not a separate mathematical structure.

**Notation:** (ℝ ∪ {+∞}, min, +, +∞, 0)

**Stable ID:** `urn:csabs:concept/MinPlusSemiring`

**Categories:** Algebra, Order and fixed points

**Kind:** Mathematical structure

**Prerequisites:** [Idempotent semiring (additively idempotent, unital)](IdempotentSemiring.md)

**Specializes:** [Idempotent semiring (additively idempotent, unital)](IdempotentSemiring.md)

**Related concepts:** [Join semilattice](JoinSemilattice.md)

## Interface and scope

**axiomBasis:** Explicit unital semiring basis plus additive idempotence and the concrete carrier/operation/constant profile.

**basisKind:** extensional-structural-definition

**basisScope:** Exact extended reals with only +∞ adjoined; −∞ is excluded. Operations are total, deterministic, and have no rounding or overflow. Empty tropical sum is +∞; empty tropical product is ordinary 0. No infinite-sum or closure operation is specified.

**basisInstantiation:** R∞ = ℝ ∪ {+∞}

**convention:** Tropical may also mean max-plus; this entry fixes min-plus. Canonical semiring order is reverse numerical order, distinct from Mathlib MinTropical’s transported numerical ≤. Integer and nonnegative variants need explicit carrier restriction; adding −∞ needs a separate totality convention.

**specializationNote:** Instantiate the parent carrier with R∞, ⊕ with min, ⊗ with extended ordinary +, 0_S with +∞, and 1_S with ordinary 0. Equality is equality of extended real values.

**verificationObligation:** Map exact carrier values, equality, infinity, operations and constants explicitly before applying to software or proofs.; Shared semiring rules retain their disclosed historical citation gaps; the new entries and new claims have direct source links.

**reviewStatus:** Editorial mathematical review; no registered Lean proof witness for these claims.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-MinPlusSemiring-addition"></a>

### addition

`urn:csabs:operation/MinPlusSemiring-addition`

**signature:** ⊕ : R∞×R∞ → R∞

**description:** min(a,b)

**precondition:** Inputs belong to R∞ = ℝ ∪ {+∞}.

**totality:** Total, including +∞.

**postcondition:** min(a,b)

**source:** [G. L. Litvinov: The Maslov Dequantization, Idempotent and Tropical Mathematics: a Very Brief Introduction (ESI 1588, 2005)](https://www.esi.ac.at/preprints/esi1588.pdf); accessedOn: 2026-11-11; sourceRole: reference-for-selected-basis

**sourceLocator:** §2, printed pp. 3–4; §5, printed p. 6

**sourceNote:** Operation/constant interpretation under the stated convention.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-MinPlusSemiring-multiplication"></a>

### multiplication

`urn:csabs:operation/MinPlusSemiring-multiplication`

**signature:** ⊗ : R∞×R∞ → R∞

**description:** Extended ordinary a+b; +∞+a=a+(+∞)=+∞.

**precondition:** Inputs belong to R∞ = ℝ ∪ {+∞}.

**totality:** Total, including +∞.

**postcondition:** Extended ordinary a+b; +∞+a=a+(+∞)=+∞.

**source:** [G. L. Litvinov: The Maslov Dequantization, Idempotent and Tropical Mathematics: a Very Brief Introduction (ESI 1588, 2005)](https://www.esi.ac.at/preprints/esi1588.pdf); accessedOn: 2026-11-11; sourceRole: reference-for-selected-basis

**sourceLocator:** §2, printed pp. 3–4; §5, printed p. 6

**sourceNote:** Operation/constant interpretation under the stated convention.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-MinPlusSemiring-zero"></a>

### zero

`urn:csabs:operation/MinPlusSemiring-zero`

**signature:** zero : R∞

**description:** +∞

**precondition:** Inputs belong to R∞ = ℝ ∪ {+∞}.

**totality:** Total, including +∞.

**postcondition:** +∞

**source:** [G. L. Litvinov: The Maslov Dequantization, Idempotent and Tropical Mathematics: a Very Brief Introduction (ESI 1588, 2005)](https://www.esi.ac.at/preprints/esi1588.pdf); accessedOn: 2026-11-11; sourceRole: reference-for-selected-basis

**sourceLocator:** §2, printed pp. 3–4; §5, printed p. 6

**sourceNote:** Operation/constant interpretation under the stated convention.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-MinPlusSemiring-one"></a>

### one

`urn:csabs:operation/MinPlusSemiring-one`

**signature:** one : R∞

**description:** Ordinary real 0

**precondition:** Inputs belong to R∞ = ℝ ∪ {+∞}.

**totality:** Total, including +∞.

**postcondition:** Ordinary real 0

**source:** [G. L. Litvinov: The Maslov Dequantization, Idempotent and Tropical Mathematics: a Very Brief Introduction (ESI 1588, 2005)](https://www.esi.ac.at/preprints/esi1588.pdf); accessedOn: 2026-11-11; sourceRole: reference-for-selected-basis

**sourceLocator:** §2, printed pp. 3–4; §5, printed p. 6

**sourceNote:** Operation/constant interpretation under the stated convention.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-MinPlusSemiring-canonical-order"></a>

### canonical-order

`urn:csabs:operation/MinPlusSemiring-canonical-order`

**signature:** ≼ : R∞×R∞ → Prop

**description:** a ≼ b iff a ⊕ b = b; this is reverse numerical order for min-plus.

**precondition:** Inputs belong to R∞ = ℝ ∪ {+∞}.

**totality:** Total, including +∞.

**postcondition:** a ≼ b iff a ⊕ b = b; this is reverse numerical order for min-plus.

**source:** [G. L. Litvinov: The Maslov Dequantization, Idempotent and Tropical Mathematics: a Very Brief Introduction (ESI 1588, 2005)](https://www.esi.ac.at/preprints/esi1588.pdf); accessedOn: 2026-11-11; sourceRole: reference-for-selected-basis

**sourceLocator:** §2, printed pp. 3–4; §5, printed p. 6

**sourceNote:** Operation/constant interpretation under the stated convention.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-semiring-additive-monoid"></a>

### semiring-additive-monoid

`urn:csabs:axiom/semiring-additive-monoid`

**statement:** Addition forms a commutative monoid; additive inverses are not required.

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

**formalStatement:** Addition forms a commutative monoid; additive inverses are not required.

**assumptions:** Use the linked concept’s explicit basis and carrier conventions.

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-semiring-multiplicative-monoid"></a>

### semiring-multiplicative-monoid

`urn:csabs:axiom/semiring-multiplicative-monoid`

**statement:** Multiplication forms a monoid under the stated unital convention.

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

**formalStatement:** Multiplication forms a monoid under the stated unital convention.

**assumptions:** Use the linked concept’s explicit basis and carrier conventions.

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-semiring-distributivity"></a>

### semiring-distributivity

`urn:csabs:axiom/semiring-distributivity`

**statement:** Multiplication distributes over addition on both sides.

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

**formalStatement:** Multiplication distributes over addition on both sides.

**assumptions:** Use the linked concept’s explicit basis and carrier conventions.

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-semiring-zero-annihilation"></a>

### semiring-zero-annihilation

`urn:csabs:axiom/semiring-zero-annihilation`

**statement:** Zero annihilates multiplication.

**formalStatement:** 0·x=x·0=0

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

**assumptions:** Use the linked concept’s explicit basis and carrier conventions.

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-IdempotentSemiring-add-idempotent"></a>

### additive-idempotence

`urn:csabs:axiom/IdempotentSemiring-add-idempotent`

**statement:** Adding an element to itself leaves it unchanged.

**formalStatement:** ∀a∈S, a ⊕ a = a

**assumptions:** Total unital semiring operations and carrier equality; 0_S=1_S is permitted. Multiplication need not commute. Only finite sums/products are specified, with empty sum 0_S and empty product 1_S; no completeness or Kleene star is assumed.; All variables range over the stated carrier with its exact equality.

**reviewStatus:** Editorial mathematical review; no registered Lean proof witness for these claims.

**notationLanguage:** informal mathematical Unicode

**source:** [G. L. Litvinov: The Maslov Dequantization, Idempotent and Tropical Mathematics: a Very Brief Introduction (ESI 1588, 2005)](https://www.esi.ac.at/preprints/esi1588.pdf); accessedOn: 2026-11-11; sourceRole: reference-for-selected-basis

**sourceLocator:** §2, printed pp. 3–4; §5, printed p. 6

**sourceNote:** Definition under the stated catalog convention.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-MinPlusSemiring-profile"></a>

### min-plus-profile

`urn:csabs:axiom/MinPlusSemiring-profile`

**statement:** Fix the concrete carrier, equality, operations, and identities.

**formalStatement:** S=ℝ∪{+∞}; a⊕b=min(a,b); a⊗b=a+b; 0_S=+∞; 1_S=0; (+∞)+a=a+(+∞)=+∞

**assumptions:** Exact extended reals with only +∞ adjoined; −∞ is excluded. Operations are total, deterministic, and have no rounding or overflow. Empty tropical sum is +∞; empty tropical product is ordinary 0. No infinite-sum or closure operation is specified.; All variables range over the stated carrier with its exact equality.

**reviewStatus:** Editorial mathematical review; no registered Lean proof witness for these claims.

**notationLanguage:** informal mathematical Unicode

**source:** [Mathlib tropical algebra, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Algebra/Tropical/Basic.lean); path: lean/.lake/packages/mathlib/Mathlib/Algebra/Tropical/Basic.lean; accessedOn: 2026-11-11; sourceRole: formal-interface-reference; [G. L. Litvinov: The Maslov Dequantization, Idempotent and Tropical Mathematics: a Very Brief Introduction (ESI 1588, 2005)](https://www.esi.ac.at/preprints/esi1588.pdf); accessedOn: 2026-11-11; sourceRole: reference-for-selected-basis

**sourceLocator:** MinTropical: Zero, One, Add, Mul, untrop_add, untrop_mul, and CommSemiring instances

**sourceNote:** Concrete definitions interpreted on WithTop ℝ; exact equality; no −∞.

**provenanceKind:** adapted

**ruleRole:** defining-rule

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-MinPlusSemiring-canonical-order-reversed"></a>

### canonical-order-reversed

`urn:csabs:theorem/MinPlusSemiring-canonical-order-reversed`

**statement:** The canonical order reverses numerical order; tropical addition is its join.

**formalStatement:** a ≼ b ⇔ min(a,b)=b ⇔ b ≤num a; bottom≼=+∞; a ⊔≼ b=min(a,b)

**assumptions:** Exact extended reals with only +∞ adjoined; −∞ is excluded. Operations are total, deterministic, and have no rounding or overflow. Empty tropical sum is +∞; empty tropical product is ordinary 0. No infinite-sum or closure operation is specified.; All variables range over the stated carrier with its exact equality.

**reviewStatus:** Editorial mathematical review; no registered Lean proof witness for these claims.

**notationLanguage:** informal mathematical Unicode

**source:** [G. L. Litvinov: The Maslov Dequantization, Idempotent and Tropical Mathematics: a Very Brief Introduction (ESI 1588, 2005)](https://www.esi.ac.at/preprints/esi1588.pdf); accessedOn: 2026-11-11; sourceRole: reference-for-selected-basis

**sourceLocator:** §2, printed pp. 3–4; §5, printed p. 6

**sourceNote:** Editorial derivation from the explicitly linked basis.

**provenanceKind:** derived

**dependsOn:** [min-plus-profile](MinPlusSemiring.md#node-urn-csabs-axiom-MinPlusSemiring-profile); [canonical-order-and-join](IdempotentSemiring.md#node-urn-csabs-theorem-IdempotentSemiring-canonical-order)

**proofSketch:** In the extended numerical linear order, min(a,b)=b exactly when b≤num a. Apply the canonical-order theorem to the explicitly linked idempotent-semiring basis.

## Concept provenance

- [G. L. Litvinov: The Maslov Dequantization, Idempotent and Tropical Mathematics: a Very Brief Introduction (ESI 1588, 2005)](https://www.esi.ac.at/preprints/esi1588.pdf); accessedOn: 2026-11-11; sourceRole: reference-for-selected-basis

**sourceLocator:** §§1–3, printed pp. 2–5

**sourceNote:** Concrete real min-plus profile and terminology, with explicit infinity and exact-arithmetic conventions.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/MinPlusSemiring",
    "type": "Concept",
    "shortForm": "MinPlusSemiring",
    "fullName": "Min-plus semiring (tropical semiring, min convention)",
    "category": [
      "urn:csabs:category/algebra",
      "urn:csabs:category/order"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "The real min-plus algebra: minimum combines alternative costs and extended ordinary addition combines costs in sequence. Also called the tropical semiring in the min-plus convention; TropicalSemiring is an alias here, not a separate mathematical structure.",
    "notation": "(ℝ ∪ {+∞}, min, +, +∞, 0)",
    "specializationOf": [
      "urn:csabs:concept/IdempotentSemiring"
    ],
    "requiresConcept": [
      "urn:csabs:concept/IdempotentSemiring"
    ],
    "relatedConcept": [
      "urn:csabs:concept/JoinSemilattice"
    ],
    "specializationNote": "Instantiate the parent carrier with R∞, ⊕ with min, ⊗ with extended ordinary +, 0_S with +∞, and 1_S with ordinary 0. Equality is equality of extended real values.",
    "axiomBasis": "Explicit unital semiring basis plus additive idempotence and the concrete carrier/operation/constant profile.",
    "basisKind": "extensional-structural-definition",
    "basisScope": "Exact extended reals with only +∞ adjoined; −∞ is excluded. Operations are total, deterministic, and have no rounding or overflow. Empty tropical sum is +∞; empty tropical product is ordinary 0. No infinite-sum or closure operation is specified.",
    "basisInstantiation": "R∞ = ℝ ∪ {+∞}",
    "convention": "Tropical may also mean max-plus; this entry fixes min-plus. Canonical semiring order is reverse numerical order, distinct from Mathlib MinTropical’s transported numerical ≤. Integer and nonnegative variants need explicit carrier restriction; adding −∞ needs a separate totality convention.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial mathematical review; no registered Lean proof witness for these claims.",
    "verificationObligation": [
      "Map exact carrier values, equality, infinity, operations and constants explicitly before applying to software or proofs.",
      "Shared semiring rules retain their disclosed historical citation gaps; the new entries and new claims have direct source links."
    ],
    "hasOperation": [
      "urn:csabs:operation/MinPlusSemiring-addition",
      "urn:csabs:operation/MinPlusSemiring-multiplication",
      "urn:csabs:operation/MinPlusSemiring-zero",
      "urn:csabs:operation/MinPlusSemiring-one",
      "urn:csabs:operation/MinPlusSemiring-canonical-order"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/semiring-additive-monoid",
      "urn:csabs:axiom/semiring-multiplicative-monoid",
      "urn:csabs:axiom/semiring-distributivity",
      "urn:csabs:axiom/semiring-zero-annihilation",
      "urn:csabs:axiom/IdempotentSemiring-add-idempotent",
      "urn:csabs:axiom/MinPlusSemiring-profile"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/MinPlusSemiring-canonical-order-reversed"
    ],
    "source": [
      "urn:csabs:source/litvinov-esi1588"
    ],
    "sourceLocator": "§§1–3, printed pp. 2–5",
    "sourceNote": "Concrete real min-plus profile and terminology, with explicit infinity and exact-arithmetic conventions.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/MinPlusSemiring-addition",
    "type": "Operation",
    "name": "addition",
    "signature": "⊕ : R∞×R∞ → R∞",
    "description": "min(a,b)",
    "concept": "urn:csabs:concept/MinPlusSemiring",
    "precondition": "Inputs belong to R∞ = ℝ ∪ {+∞}.",
    "totality": "Total, including +∞.",
    "postcondition": "min(a,b)",
    "source": [
      "urn:csabs:source/litvinov-esi1588"
    ],
    "sourceLocator": "§2, printed pp. 3–4; §5, printed p. 6",
    "sourceNote": "Operation/constant interpretation under the stated convention.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/MinPlusSemiring-multiplication",
    "type": "Operation",
    "name": "multiplication",
    "signature": "⊗ : R∞×R∞ → R∞",
    "description": "Extended ordinary a+b; +∞+a=a+(+∞)=+∞.",
    "concept": "urn:csabs:concept/MinPlusSemiring",
    "precondition": "Inputs belong to R∞ = ℝ ∪ {+∞}.",
    "totality": "Total, including +∞.",
    "postcondition": "Extended ordinary a+b; +∞+a=a+(+∞)=+∞.",
    "source": [
      "urn:csabs:source/litvinov-esi1588"
    ],
    "sourceLocator": "§2, printed pp. 3–4; §5, printed p. 6",
    "sourceNote": "Operation/constant interpretation under the stated convention.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/MinPlusSemiring-zero",
    "type": "Operation",
    "name": "zero",
    "signature": "zero : R∞",
    "description": "+∞",
    "concept": "urn:csabs:concept/MinPlusSemiring",
    "precondition": "Inputs belong to R∞ = ℝ ∪ {+∞}.",
    "totality": "Total, including +∞.",
    "postcondition": "+∞",
    "source": [
      "urn:csabs:source/litvinov-esi1588"
    ],
    "sourceLocator": "§2, printed pp. 3–4; §5, printed p. 6",
    "sourceNote": "Operation/constant interpretation under the stated convention.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/MinPlusSemiring-one",
    "type": "Operation",
    "name": "one",
    "signature": "one : R∞",
    "description": "Ordinary real 0",
    "concept": "urn:csabs:concept/MinPlusSemiring",
    "precondition": "Inputs belong to R∞ = ℝ ∪ {+∞}.",
    "totality": "Total, including +∞.",
    "postcondition": "Ordinary real 0",
    "source": [
      "urn:csabs:source/litvinov-esi1588"
    ],
    "sourceLocator": "§2, printed pp. 3–4; §5, printed p. 6",
    "sourceNote": "Operation/constant interpretation under the stated convention.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/MinPlusSemiring-canonical-order",
    "type": "Operation",
    "name": "canonical-order",
    "signature": "≼ : R∞×R∞ → Prop",
    "description": "a ≼ b iff a ⊕ b = b; this is reverse numerical order for min-plus.",
    "concept": "urn:csabs:concept/MinPlusSemiring",
    "precondition": "Inputs belong to R∞ = ℝ ∪ {+∞}.",
    "totality": "Total, including +∞.",
    "postcondition": "a ≼ b iff a ⊕ b = b; this is reverse numerical order for min-plus.",
    "source": [
      "urn:csabs:source/litvinov-esi1588"
    ],
    "sourceLocator": "§2, printed pp. 3–4; §5, printed p. 6",
    "sourceNote": "Operation/constant interpretation under the stated convention.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/MinPlusSemiring-profile",
    "type": "Axiom",
    "name": "min-plus-profile",
    "statement": "Fix the concrete carrier, equality, operations, and identities.",
    "formalStatement": "S=ℝ∪{+∞}; a⊕b=min(a,b); a⊗b=a+b; 0_S=+∞; 1_S=0; (+∞)+a=a+(+∞)=+∞",
    "assumptions": [
      "Exact extended reals with only +∞ adjoined; −∞ is excluded. Operations are total, deterministic, and have no rounding or overflow. Empty tropical sum is +∞; empty tropical product is ordinary 0. No infinite-sum or closure operation is specified.",
      "All variables range over the stated carrier with its exact equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/MinPlusSemiring"
    ],
    "reviewStatus": "Editorial mathematical review; no registered Lean proof witness for these claims.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/mathlib-min-tropical-pinned",
      "urn:csabs:source/litvinov-esi1588"
    ],
    "sourceLocator": "MinTropical: Zero, One, Add, Mul, untrop_add, untrop_mul, and CommSemiring instances",
    "sourceNote": "Concrete definitions interpreted on WithTop ℝ; exact equality; no −∞.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:theorem/MinPlusSemiring-canonical-order-reversed",
    "type": "Theorem",
    "name": "canonical-order-reversed",
    "statement": "The canonical order reverses numerical order; tropical addition is its join.",
    "formalStatement": "a ≼ b ⇔ min(a,b)=b ⇔ b ≤num a; bottom≼=+∞; a ⊔≼ b=min(a,b)",
    "assumptions": [
      "Exact extended reals with only +∞ adjoined; −∞ is excluded. Operations are total, deterministic, and have no rounding or overflow. Empty tropical sum is +∞; empty tropical product is ordinary 0. No infinite-sum or closure operation is specified.",
      "All variables range over the stated carrier with its exact equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/MinPlusSemiring"
    ],
    "reviewStatus": "Editorial mathematical review; no registered Lean proof witness for these claims.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/litvinov-esi1588"
    ],
    "sourceLocator": "§2, printed pp. 3–4; §5, printed p. 6",
    "sourceNote": "Editorial derivation from the explicitly linked basis.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/MinPlusSemiring-profile",
      "urn:csabs:theorem/IdempotentSemiring-canonical-order"
    ],
    "proofSketch": "In the extended numerical linear order, min(a,b)=b exactly when b≤num a. Apply the canonical-order theorem to the explicitly linked idempotent-semiring basis."
  }
]
```
<!-- graph-record:end -->
