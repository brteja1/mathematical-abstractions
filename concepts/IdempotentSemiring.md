# Idempotent semiring (additively idempotent, unital)

A unital semiring whose addition is idempotent. Its canonical order is defined by a ≼ b iff a ⊕ b = b.

**Notation:** (S, ⊕, ⊗, 0_S, 1_S), a ⊕ a = a

**Stable ID:** `urn:csabs:concept/IdempotentSemiring`

**Categories:** Algebra, Order and fixed points

**Kind:** Mathematical structure

**Prerequisites:** [Semiring](Semiring.md)

**Specializes:** [Semiring](Semiring.md)

**Related concepts:** [Join semilattice](JoinSemilattice.md)

## Backlinks

- [Min-plus semiring (tropical semiring, min convention)](MinPlusSemiring.md) — `requiresConcept`
- [Min-plus semiring (tropical semiring, min convention)](MinPlusSemiring.md) — `specializationOf`

## Mathematical formulation

An idempotent semiring is a semiring S with ∀a∈S,a+a=a. Its canonical relation is a≼b ⇔ a+b=b. The selected unital convention allows 0=1.

**Lean formulation** (in its source module context):

```lean
class IdempotentSemiring (A : Type u) extends _root_.Semiring A where
  add_idem (a : A) : a + a = a
```

**Source:** [`Catalog.IdempotentSemiring`](../lean/Catalog/Algebra.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Catalog.IdempotentSemiring A extends Mathlib Semiring A with the structural law ∀ a, a+a=a. Same carrier equality and total operations; zero=one allowed. canonicalSemiringOrder a b is a+b=b.

**Limits:** Carrier and interface binding only. No registered witness for the new canonical-order theorems; the graph statements and source correspondence remain editorial.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Explicit unital semiring basis plus additive idempotence.

**basisKind:** axiomatic-structure

**basisScope:** Total unital semiring operations and carrier equality; 0_S=1_S is permitted. Multiplication need not commute. Only finite sums/products are specified, with empty sum 0_S and empty product 1_S; no completeness or Kleene star is assumed.

**basisInstantiation:** S with carrier equality

**convention:** Idempotent means addition, not multiplication. Adapted from Litvinov §2 to the catalog unital convention, allowing 0_S=1_S unlike the source’s nontrivial-zero convention. The canonical order is additional defined structure, not an arbitrary supplied order.

**specializationNote:** Retain the Semiring carrier, operations and constants and add additive idempotence. The shared semiring basis is linked with explicit applicability; no axioms are inferred from the hierarchy.

**verificationObligation:** Map exact carrier values, equality, infinity, operations and constants explicitly before applying to software or proofs.; Shared semiring rules retain their disclosed historical citation gaps; the new entries and new claims have direct source links.

**reviewStatus:** Editorial mathematical review; no registered Lean proof witness for these claims.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-IdempotentSemiring-addition"></a>

### addition

`urn:csabs:operation/IdempotentSemiring-addition`

**signature:** ⊕ : S×S → S

**description:** Semiring addition.

**precondition:** Inputs belong to S with carrier equality.

**totality:** Total on the stated carrier.

**postcondition:** Semiring addition.

**source:** [G. L. Litvinov: The Maslov Dequantization, Idempotent and Tropical Mathematics: a Very Brief Introduction (ESI 1588, 2005)](https://www.esi.ac.at/preprints/esi1588.pdf); accessedOn: 2026-11-11; sourceRole: reference-for-selected-basis

**sourceLocator:** §2, printed pp. 3–4; §5, printed p. 6

**sourceNote:** Operation/constant interpretation under the stated convention.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-IdempotentSemiring-multiplication"></a>

### multiplication

`urn:csabs:operation/IdempotentSemiring-multiplication`

**signature:** ⊗ : S×S → S

**description:** Semiring multiplication; not necessarily commutative.

**precondition:** Inputs belong to S with carrier equality.

**totality:** Total on the stated carrier.

**postcondition:** Semiring multiplication; not necessarily commutative.

**source:** [G. L. Litvinov: The Maslov Dequantization, Idempotent and Tropical Mathematics: a Very Brief Introduction (ESI 1588, 2005)](https://www.esi.ac.at/preprints/esi1588.pdf); accessedOn: 2026-11-11; sourceRole: reference-for-selected-basis

**sourceLocator:** §2, printed pp. 3–4; §5, printed p. 6

**sourceNote:** Operation/constant interpretation under the stated convention.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-IdempotentSemiring-zero"></a>

### zero

`urn:csabs:operation/IdempotentSemiring-zero`

**signature:** zero : S

**description:** The additive identity and multiplicative annihilator 0_S.

**precondition:** Inputs belong to S with carrier equality.

**totality:** Total on the stated carrier.

**postcondition:** The additive identity and multiplicative annihilator 0_S.

**source:** [G. L. Litvinov: The Maslov Dequantization, Idempotent and Tropical Mathematics: a Very Brief Introduction (ESI 1588, 2005)](https://www.esi.ac.at/preprints/esi1588.pdf); accessedOn: 2026-11-11; sourceRole: reference-for-selected-basis

**sourceLocator:** §2, printed pp. 3–4; §5, printed p. 6

**sourceNote:** Operation/constant interpretation under the stated convention.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-IdempotentSemiring-one"></a>

### one

`urn:csabs:operation/IdempotentSemiring-one`

**signature:** one : S

**description:** The multiplicative identity 1_S.

**precondition:** Inputs belong to S with carrier equality.

**totality:** Total on the stated carrier.

**postcondition:** The multiplicative identity 1_S.

**source:** [G. L. Litvinov: The Maslov Dequantization, Idempotent and Tropical Mathematics: a Very Brief Introduction (ESI 1588, 2005)](https://www.esi.ac.at/preprints/esi1588.pdf); accessedOn: 2026-11-11; sourceRole: reference-for-selected-basis

**sourceLocator:** §2, printed pp. 3–4; §5, printed p. 6

**sourceNote:** Operation/constant interpretation under the stated convention.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-IdempotentSemiring-canonical-order"></a>

### canonical-order

`urn:csabs:operation/IdempotentSemiring-canonical-order`

**signature:** ≼ : S×S → Prop

**description:** a ≼ b iff a ⊕ b = b.

**precondition:** Inputs belong to S with carrier equality.

**totality:** Total on the stated carrier.

**postcondition:** a ≼ b iff a ⊕ b = b.

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

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-IdempotentSemiring-canonical-order"></a>

### canonical-order-and-join

`urn:csabs:theorem/IdempotentSemiring-canonical-order`

**statement:** The canonical order is a partial order with bottom 0_S and binary join ⊕.

**formalStatement:** a ≼ b ⇔ a ⊕ b = b; ≼ is reflexive, antisymmetric and transitive; 0_S ≼ a; a ≼ a⊕b ∧ b ≼ a⊕b; (a ≼ c ∧ b ≼ c) ⇒ a⊕b ≼ c

**assumptions:** Total unital semiring operations and carrier equality; 0_S=1_S is permitted. Multiplication need not commute. Only finite sums/products are specified, with empty sum 0_S and empty product 1_S; no completeness or Kleene star is assumed.; All variables range over the stated carrier with its exact equality.

**reviewStatus:** Editorial mathematical review; no registered Lean proof witness for these claims.

**notationLanguage:** informal mathematical Unicode

**source:** [G. L. Litvinov: The Maslov Dequantization, Idempotent and Tropical Mathematics: a Very Brief Introduction (ESI 1588, 2005)](https://www.esi.ac.at/preprints/esi1588.pdf); accessedOn: 2026-11-11; sourceRole: reference-for-selected-basis

**sourceLocator:** §2, printed pp. 3–4; §5, printed p. 6

**sourceNote:** Editorial derivation from the explicitly linked basis.

**provenanceKind:** derived

**dependsOn:** [semiring-additive-monoid](Semiring.md#node-urn-csabs-axiom-semiring-additive-monoid); [additive-idempotence](IdempotentSemiring.md#node-urn-csabs-axiom-IdempotentSemiring-add-idempotent)

**proofSketch:** Idempotence gives reflexivity; commutativity gives antisymmetry. If a⊕b=b and b⊕c=c, associativity gives a⊕c=(a⊕b)⊕c=b⊕c=c. The additive identity gives bottom. Associativity and idempotence give both upper bounds; associativity and the two assumed order equations give leastness.

## Concept provenance

- [G. L. Litvinov: The Maslov Dequantization, Idempotent and Tropical Mathematics: a Very Brief Introduction (ESI 1588, 2005)](https://www.esi.ac.at/preprints/esi1588.pdf); accessedOn: 2026-11-11; sourceRole: reference-for-selected-basis

**sourceLocator:** §2, printed p. 3; §5, printed p. 6

**sourceNote:** Additive idempotence and canonical order, adapted to the existing unital semiring convention.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/IdempotentSemiring",
    "type": "Concept",
    "shortForm": "IdempotentSemiring",
    "fullName": "Idempotent semiring (additively idempotent, unital)",
    "category": [
      "urn:csabs:category/algebra",
      "urn:csabs:category/order"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "A unital semiring whose addition is idempotent. Its canonical order is defined by a ≼ b iff a ⊕ b = b.",
    "notation": "(S, ⊕, ⊗, 0_S, 1_S), a ⊕ a = a",
    "specializationOf": [
      "urn:csabs:concept/Semiring"
    ],
    "requiresConcept": [
      "urn:csabs:concept/Semiring"
    ],
    "relatedConcept": [
      "urn:csabs:concept/JoinSemilattice"
    ],
    "specializationNote": "Retain the Semiring carrier, operations and constants and add additive idempotence. The shared semiring basis is linked with explicit applicability; no axioms are inferred from the hierarchy.",
    "axiomBasis": "Explicit unital semiring basis plus additive idempotence.",
    "basisKind": "axiomatic-structure",
    "basisScope": "Total unital semiring operations and carrier equality; 0_S=1_S is permitted. Multiplication need not commute. Only finite sums/products are specified, with empty sum 0_S and empty product 1_S; no completeness or Kleene star is assumed.",
    "basisInstantiation": "S with carrier equality",
    "convention": "Idempotent means addition, not multiplication. Adapted from Litvinov §2 to the catalog unital convention, allowing 0_S=1_S unlike the source’s nontrivial-zero convention. The canonical order is additional defined structure, not an arbitrary supplied order.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial mathematical review; no registered Lean proof witness for these claims.",
    "verificationObligation": [
      "Map exact carrier values, equality, infinity, operations and constants explicitly before applying to software or proofs.",
      "Shared semiring rules retain their disclosed historical citation gaps; the new entries and new claims have direct source links."
    ],
    "hasOperation": [
      "urn:csabs:operation/IdempotentSemiring-addition",
      "urn:csabs:operation/IdempotentSemiring-multiplication",
      "urn:csabs:operation/IdempotentSemiring-zero",
      "urn:csabs:operation/IdempotentSemiring-one",
      "urn:csabs:operation/IdempotentSemiring-canonical-order"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/semiring-additive-monoid",
      "urn:csabs:axiom/semiring-multiplicative-monoid",
      "urn:csabs:axiom/semiring-distributivity",
      "urn:csabs:axiom/semiring-zero-annihilation",
      "urn:csabs:axiom/IdempotentSemiring-add-idempotent"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/IdempotentSemiring-canonical-order"
    ],
    "source": [
      "urn:csabs:source/litvinov-esi1588"
    ],
    "sourceLocator": "§2, printed p. 3; §5, printed p. 6",
    "sourceNote": "Additive idempotence and canonical order, adapted to the existing unital semiring convention.",
    "provenanceKind": "adapted",
    "leanFormulation": "class IdempotentSemiring (A : Type u) extends _root_.Semiring A where\n  add_idem (a : A) : a + a = a",
    "formulationSource": "urn:csabs:source/local-lean-Algebra",
    "formulationLocator": "Catalog.IdempotentSemiring",
    "formulationScope": "model",
    "leanModelMapping": "Catalog.IdempotentSemiring A extends Mathlib Semiring A with the structural law ∀ a, a+a=a. Same carrier equality and total operations; zero=one allowed. canonicalSemiringOrder a b is a+b=b.",
    "leanModelLimitations": "Carrier and interface binding only. No registered witness for the new canonical-order theorems; the graph statements and source correspondence remain editorial.",
    "mathematicalFormulation": "An idempotent semiring is a semiring S with ∀a∈S,a+a=a. Its canonical relation is a≼b ⇔ a+b=b. The selected unital convention allows 0=1."
  },
  {
    "id": "urn:csabs:operation/IdempotentSemiring-addition",
    "type": "Operation",
    "name": "addition",
    "signature": "⊕ : S×S → S",
    "description": "Semiring addition.",
    "concept": "urn:csabs:concept/IdempotentSemiring",
    "precondition": "Inputs belong to S with carrier equality.",
    "totality": "Total on the stated carrier.",
    "postcondition": "Semiring addition.",
    "source": [
      "urn:csabs:source/litvinov-esi1588"
    ],
    "sourceLocator": "§2, printed pp. 3–4; §5, printed p. 6",
    "sourceNote": "Operation/constant interpretation under the stated convention.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/IdempotentSemiring-multiplication",
    "type": "Operation",
    "name": "multiplication",
    "signature": "⊗ : S×S → S",
    "description": "Semiring multiplication; not necessarily commutative.",
    "concept": "urn:csabs:concept/IdempotentSemiring",
    "precondition": "Inputs belong to S with carrier equality.",
    "totality": "Total on the stated carrier.",
    "postcondition": "Semiring multiplication; not necessarily commutative.",
    "source": [
      "urn:csabs:source/litvinov-esi1588"
    ],
    "sourceLocator": "§2, printed pp. 3–4; §5, printed p. 6",
    "sourceNote": "Operation/constant interpretation under the stated convention.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/IdempotentSemiring-zero",
    "type": "Operation",
    "name": "zero",
    "signature": "zero : S",
    "description": "The additive identity and multiplicative annihilator 0_S.",
    "concept": "urn:csabs:concept/IdempotentSemiring",
    "precondition": "Inputs belong to S with carrier equality.",
    "totality": "Total on the stated carrier.",
    "postcondition": "The additive identity and multiplicative annihilator 0_S.",
    "source": [
      "urn:csabs:source/litvinov-esi1588"
    ],
    "sourceLocator": "§2, printed pp. 3–4; §5, printed p. 6",
    "sourceNote": "Operation/constant interpretation under the stated convention.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/IdempotentSemiring-one",
    "type": "Operation",
    "name": "one",
    "signature": "one : S",
    "description": "The multiplicative identity 1_S.",
    "concept": "urn:csabs:concept/IdempotentSemiring",
    "precondition": "Inputs belong to S with carrier equality.",
    "totality": "Total on the stated carrier.",
    "postcondition": "The multiplicative identity 1_S.",
    "source": [
      "urn:csabs:source/litvinov-esi1588"
    ],
    "sourceLocator": "§2, printed pp. 3–4; §5, printed p. 6",
    "sourceNote": "Operation/constant interpretation under the stated convention.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/IdempotentSemiring-canonical-order",
    "type": "Operation",
    "name": "canonical-order",
    "signature": "≼ : S×S → Prop",
    "description": "a ≼ b iff a ⊕ b = b.",
    "concept": "urn:csabs:concept/IdempotentSemiring",
    "precondition": "Inputs belong to S with carrier equality.",
    "totality": "Total on the stated carrier.",
    "postcondition": "a ≼ b iff a ⊕ b = b.",
    "source": [
      "urn:csabs:source/litvinov-esi1588"
    ],
    "sourceLocator": "§2, printed pp. 3–4; §5, printed p. 6",
    "sourceNote": "Operation/constant interpretation under the stated convention.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/semiring-additive-monoid",
    "type": "Axiom",
    "statement": "Addition forms a commutative monoid; additive inverses are not required.",
    "appliesTo": [
      "urn:csabs:concept/Semiring",
      "urn:csabs:concept/IdempotentSemiring",
      "urn:csabs:concept/MinPlusSemiring"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law",
    "name": "semiring-additive-monoid",
    "formalStatement": "Addition forms a commutative monoid; additive inverses are not required.",
    "assumptions": [
      "Use the linked concept’s explicit basis and carrier conventions."
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/semiring-multiplicative-monoid",
    "type": "Axiom",
    "statement": "Multiplication forms a monoid under the stated unital convention.",
    "appliesTo": [
      "urn:csabs:concept/Semiring",
      "urn:csabs:concept/IdempotentSemiring",
      "urn:csabs:concept/MinPlusSemiring"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law",
    "name": "semiring-multiplicative-monoid",
    "formalStatement": "Multiplication forms a monoid under the stated unital convention.",
    "assumptions": [
      "Use the linked concept’s explicit basis and carrier conventions."
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/semiring-distributivity",
    "type": "Axiom",
    "statement": "Multiplication distributes over addition on both sides.",
    "appliesTo": [
      "urn:csabs:concept/Semiring",
      "urn:csabs:concept/IdempotentSemiring",
      "urn:csabs:concept/MinPlusSemiring"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law",
    "name": "semiring-distributivity",
    "formalStatement": "Multiplication distributes over addition on both sides.",
    "assumptions": [
      "Use the linked concept’s explicit basis and carrier conventions."
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/semiring-zero-annihilation",
    "type": "Axiom",
    "statement": "Zero annihilates multiplication.",
    "formalStatement": "0·x=x·0=0",
    "appliesTo": [
      "urn:csabs:concept/Semiring",
      "urn:csabs:concept/IdempotentSemiring",
      "urn:csabs:concept/MinPlusSemiring"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law",
    "name": "semiring-zero-annihilation",
    "assumptions": [
      "Use the linked concept’s explicit basis and carrier conventions."
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/IdempotentSemiring-add-idempotent",
    "type": "Axiom",
    "name": "additive-idempotence",
    "statement": "Adding an element to itself leaves it unchanged.",
    "formalStatement": "∀a∈S, a ⊕ a = a",
    "assumptions": [
      "Total unital semiring operations and carrier equality; 0_S=1_S is permitted. Multiplication need not commute. Only finite sums/products are specified, with empty sum 0_S and empty product 1_S; no completeness or Kleene star is assumed.",
      "All variables range over the stated carrier with its exact equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/IdempotentSemiring",
      "urn:csabs:concept/MinPlusSemiring"
    ],
    "reviewStatus": "Editorial mathematical review; no registered Lean proof witness for these claims.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/litvinov-esi1588"
    ],
    "sourceLocator": "§2, printed pp. 3–4; §5, printed p. 6",
    "sourceNote": "Definition under the stated catalog convention.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:theorem/IdempotentSemiring-canonical-order",
    "type": "Theorem",
    "name": "canonical-order-and-join",
    "statement": "The canonical order is a partial order with bottom 0_S and binary join ⊕.",
    "formalStatement": "a ≼ b ⇔ a ⊕ b = b; ≼ is reflexive, antisymmetric and transitive; 0_S ≼ a; a ≼ a⊕b ∧ b ≼ a⊕b; (a ≼ c ∧ b ≼ c) ⇒ a⊕b ≼ c",
    "assumptions": [
      "Total unital semiring operations and carrier equality; 0_S=1_S is permitted. Multiplication need not commute. Only finite sums/products are specified, with empty sum 0_S and empty product 1_S; no completeness or Kleene star is assumed.",
      "All variables range over the stated carrier with its exact equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/IdempotentSemiring"
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
      "urn:csabs:axiom/semiring-additive-monoid",
      "urn:csabs:axiom/IdempotentSemiring-add-idempotent"
    ],
    "proofSketch": "Idempotence gives reflexivity; commutativity gives antisymmetry. If a⊕b=b and b⊕c=c, associativity gives a⊕c=(a⊕b)⊕c=b⊕c=c. The additive identity gives bottom. Associativity and idempotence give both upper bounds; associativity and the two assumed order equations give leastness."
  }
]
```
<!-- graph-record:end -->
