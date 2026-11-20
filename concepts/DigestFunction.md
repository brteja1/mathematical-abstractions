# Deterministic finite digest function

A total deterministic function from input values A to a fixed finite digest space D of cardinality n. Collisions are permitted; security properties require separate assumptions.

**Notation:** h : A → D; D ≅ Fin(n)

**Stable ID:** `urn:csabs:concept/DigestFunction`

**Categories:** Set theory and foundations

**Kind:** Function

**Prerequisites:** [Total function](Function.md), [Finite carrier with exhaustive enumeration](FiniteType.md)

**Related concepts:** [Pigeonhole Principle](PigeonholePrinciple.md)

## Backlinks

- [Digest with explicit collision freedom on a specified set](CollisionFreeDigest.md) — `requiresConcept`
- [Digest with explicit collision freedom on a specified set](CollisionFreeDigest.md) — `specializationOf`

## Mathematical formulation

Digest(A,n)=A→Fin(n), using exact input and output equality. Evaluate by h(x). No injectivity is included.

**Lean formulation** (in its source module context):

```lean
abbrev DigestFunction (A : Type) (n : Nat) := A → Fin n
```

**Source:** [`Catalog.DigestFunction`](../lean/Catalog/Digests.lean); consulted 2026-11-20.

**Scope:** model

**Interpretation:** A→Fin(n), n is the fixed digest-space cardinality; exact equality.

**Limits:** Exact mathematical equality and finite outputs only. No cryptographic security, collision search algorithm, implementation refinement, serialization correctness, or automatic proof of injectivity for a supplied hash and set.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Typed total single-valued evaluation h:A→Fin(n).

**basisKind:** defined-structure

**basisScope:** A is any carrier; D is a fixed finite set represented by Fin(n), n≥0. For bit digests of width w use n=2^w with an explicit encoding bijection. Equality is exact value equality. An empty A admits the empty function, including n=0; if A is inhabited then n must be positive. S may be empty or singleton, making injectivity vacuous, but this does not justify applications needing two distinct members. No overflow, rounding, randomness, state, concurrency or cost semantics. A key or seed must be fixed as part of h. Input serialization must preserve the equality being claimed.

**verificationObligation:** Supply the actual h, fixed output encoding and exact equality mapping.; For the scoped variant, prove collision freedom for the actual S; both compared inputs must belong to S.; Changing h, the seed/key, input encoding, or enlarging S requires new evidence. Subset restriction preserves the guarantee.; The model is noncryptographic; no probability bound or computational hardness claim follows.

**reviewStatus:** Sourced definitions and separately registered Lean theorem witnesses; inspect fresh verification evidence for proof status.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-DigestFunction-digest"></a>

### digest

`urn:csabs:operation/DigestFunction-digest`

**signature:** digest(h,x) : D; h:A→D; x:A

**description:** Evaluate the fixed deterministic digest function.

**precondition:** x∈A and h has the specified fixed output space. Membership in S is needed only for the equality-reflection law, not for evaluation.

**totality:** Total for every x:A once h exists.

**postcondition:** Returns exactly h(x)∈D.

**source:** [Mathlib pinned set-restricted injectivity and equality rules](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Set); citation: Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679: Data/Set/Operations.lean, Set.InjOn; Data/Set/Function.lean, Set.InjOn.eq_iff and Set.InjOn.mono. Apache-2.0.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; [NIST CSRC glossary: hash function and collision resistance](https://csrc.nist.gov/glossary/term/hash_function); citation: NIST CSRC Glossary, hash function, Definitions; collision resistance, Definitions (https://csrc.nist.gov/glossary/term/collision_resistance).; accessedOn: 2026-11-20; sourceRole: consulted-terminology-reference

**sourceLocator:** Typed function evaluation; NIST hash function Definitions

**sourceNote:** Abstracts fixed finite output evaluation without security assumptions.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-DigestFunction-total-evaluation"></a>

### total single-valued evaluation

`urn:csabs:axiom/DigestFunction-total-evaluation`

**statement:** Every input has exactly one digest in the fixed finite output space.

**formalStatement:** ∀x∈A, ∃!d∈D: d=h(x)

**assumptions:** h:A→D is a typed total function; D≅Fin(n).

**ruleRole:** defining-rule

**reviewStatus:** Structure constraint; concrete model evidence is a separate Theorem.

**source:** [Mathlib pinned set-restricted injectivity and equality rules](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Set); citation: Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679: Data/Set/Operations.lean, Set.InjOn; Data/Set/Function.lean, Set.InjOn.eq_iff and Set.InjOn.mono. Apache-2.0.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; [NIST CSRC glossary: hash function and collision resistance](https://csrc.nist.gov/glossary/term/hash_function); citation: NIST CSRC Glossary, hash function, Definitions; collision resistance, Definitions (https://csrc.nist.gov/glossary/term/collision_resistance).; accessedOn: 2026-11-20; sourceRole: consulted-terminology-reference

**sourceLocator:** Set.InjOn (Data/Set/Operations.lean); Set.InjOn.eq_iff and Set.InjOn.mono (Data/Set/Function.lean); NIST glossary Definitions

**sourceNote:** Constructed finite digest interface and explicit set-scoped injectivity profile. NIST supplies terminology and the distinction from computational collision resistance; Mathlib supplies the precise injectivity predicate and rules.

**provenanceKind:** adapted

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-DigestFunction-model-satisfaction"></a>

### model-satisfaction

`urn:csabs:theorem/DigestFunction-model-satisfaction`

**statement:** Total digest evaluation has a unique result, and the concrete modulo-two digest has distinct outputs for 0 and 1.

**formalStatement:** (∀ (A : Type) (n : Nat) (h : Catalog.DigestFunction A n) (x : A), ∃! d : Fin n, d = h x) ∧ Catalog.exampleDigest 0 ≠ Catalog.exampleDigest 1

**assumptions:** Uses the concrete exampleDigest(x)=x mod 2 and exampleDigestScope={x:ℕ | x<2}; injectivity is proved, not assumed.

**dependsOn:** [total single-valued evaluation](DigestFunction.md#node-urn-csabs-axiom-DigestFunction-total-evaluation)

**proofSketch:** Typed evaluation gives the unique witness h(x). Compute the two distinct concrete outputs.

**reviewStatus:** Registered Lean witness; verification status requires a fresh compiler and axiom-audit report.

**source:** [Mathlib pinned set-restricted injectivity and equality rules](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Set); citation: Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679: Data/Set/Operations.lean, Set.InjOn; Data/Set/Function.lean, Set.InjOn.eq_iff and Set.InjOn.mono. Apache-2.0.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; Catalog digest models and scoped-injectivity witnesses; path: lean/Catalog/Digests.lean; accessedOn: 2026-11-20; sourceRole: local-lean-formulation-and-proof

**sourceLocator:** Set.InjOn; Set.InjOn.eq_iff; Set.InjOn.mono; Catalog.digest_model_satisfaction

**sourceNote:** Derived for the finite digest profile with explicit premise mappings. Concrete model satisfaction is separate from the defining Axioms.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
(∀ (A : Type) (n : Nat) (h : Catalog.DigestFunction A n) (x : A), ∃! d : Fin n, d = h x) ∧ Catalog.exampleDigest 0 ≠ Catalog.exampleDigest 1
```

**Source:** [`Catalog.digest_model_satisfaction`](../lean/Catalog/Digests.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** Total digest evaluation has a unique result, and the concrete modulo-two digest has distinct outputs for 0 and 1.

**Limits:** Exact mathematical equality and finite outputs only. No cryptographic security, collision search algorithm, implementation refinement, serialization correctness, or automatic proof of injectivity for a supplied hash and set.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/DigestFunction-total-evaluation": "Proved obligation for exampleDigest and exampleDigestScope, not an assumed law field."
}
```

## Concept provenance

- [Mathlib pinned set-restricted injectivity and equality rules](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Set); citation: Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679: Data/Set/Operations.lean, Set.InjOn; Data/Set/Function.lean, Set.InjOn.eq_iff and Set.InjOn.mono. Apache-2.0.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference
- [NIST CSRC glossary: hash function and collision resistance](https://csrc.nist.gov/glossary/term/hash_function); citation: NIST CSRC Glossary, hash function, Definitions; collision resistance, Definitions (https://csrc.nist.gov/glossary/term/collision_resistance).; accessedOn: 2026-11-20; sourceRole: consulted-terminology-reference

**sourceLocator:** Set.InjOn (Data/Set/Operations.lean); Set.InjOn.eq_iff and Set.InjOn.mono (Data/Set/Function.lean); NIST glossary Definitions

**sourceNote:** Constructed finite digest interface and explicit set-scoped injectivity profile. NIST supplies terminology and the distinction from computational collision resistance; Mathlib supplies the precise injectivity predicate and rules.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/DigestFunction",
    "type": "Concept",
    "shortForm": "DigestFunction",
    "fullName": "Deterministic finite digest function",
    "synonyms": [
      "Finite-output hash function",
      "Deterministic digest map"
    ],
    "category": [
      "urn:csabs:category/foundations"
    ],
    "kind": "urn:csabs:kind/function",
    "definition": "A total deterministic function from input values A to a fixed finite digest space D of cardinality n. Collisions are permitted; security properties require separate assumptions.",
    "notation": "h : A → D; D ≅ Fin(n)",
    "requiresConcept": [
      "urn:csabs:concept/Function",
      "urn:csabs:concept/FiniteType"
    ],
    "relatedConcept": [
      "urn:csabs:concept/PigeonholePrinciple"
    ],
    "axiomBasis": "Typed total single-valued evaluation h:A→Fin(n).",
    "basisKind": "defined-structure",
    "basisScope": "A is any carrier; D is a fixed finite set represented by Fin(n), n≥0. For bit digests of width w use n=2^w with an explicit encoding bijection. Equality is exact value equality. An empty A admits the empty function, including n=0; if A is inhabited then n must be positive. S may be empty or singleton, making injectivity vacuous, but this does not justify applications needing two distinct members. No overflow, rounding, randomness, state, concurrency or cost semantics. A key or seed must be fixed as part of h. Input serialization must preserve the equality being claimed.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Sourced definitions and separately registered Lean theorem witnesses; inspect fresh verification evidence for proof status.",
    "verificationObligation": [
      "Supply the actual h, fixed output encoding and exact equality mapping.",
      "For the scoped variant, prove collision freedom for the actual S; both compared inputs must belong to S.",
      "Changing h, the seed/key, input encoding, or enlarging S requires new evidence. Subset restriction preserves the guarantee.",
      "The model is noncryptographic; no probability bound or computational hardness claim follows."
    ],
    "hasOperation": [
      "urn:csabs:operation/DigestFunction-digest"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/DigestFunction-total-evaluation"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/DigestFunction-model-satisfaction"
    ],
    "mathematicalFormulation": "Digest(A,n)=A→Fin(n), using exact input and output equality. Evaluate by h(x). No injectivity is included.",
    "source": [
      "urn:csabs:source/mathlib-scoped-digest",
      "urn:csabs:source/nist-hash-glossary-2026-11-20"
    ],
    "sourceLocator": "Set.InjOn (Data/Set/Operations.lean); Set.InjOn.eq_iff and Set.InjOn.mono (Data/Set/Function.lean); NIST glossary Definitions",
    "sourceNote": "Constructed finite digest interface and explicit set-scoped injectivity profile. NIST supplies terminology and the distinction from computational collision resistance; Mathlib supplies the precise injectivity predicate and rules.",
    "provenanceKind": "adapted",
    "leanFormulation": "abbrev DigestFunction (A : Type) (n : Nat) := A → Fin n",
    "formulationSource": "urn:csabs:source/lean-digests",
    "formulationLocator": "Catalog.DigestFunction",
    "formulationScope": "model",
    "leanModelMapping": "A→Fin(n), n is the fixed digest-space cardinality; exact equality.",
    "leanModelLimitations": "Exact mathematical equality and finite outputs only. No cryptographic security, collision search algorithm, implementation refinement, serialization correctness, or automatic proof of injectivity for a supplied hash and set."
  },
  {
    "id": "urn:csabs:operation/DigestFunction-digest",
    "type": "Operation",
    "concept": "urn:csabs:concept/DigestFunction",
    "name": "digest",
    "signature": "digest(h,x) : D; h:A→D; x:A",
    "description": "Evaluate the fixed deterministic digest function.",
    "precondition": "x∈A and h has the specified fixed output space. Membership in S is needed only for the equality-reflection law, not for evaluation.",
    "totality": "Total for every x:A once h exists.",
    "postcondition": "Returns exactly h(x)∈D.",
    "source": [
      "urn:csabs:source/mathlib-scoped-digest",
      "urn:csabs:source/nist-hash-glossary-2026-11-20"
    ],
    "sourceLocator": "Typed function evaluation; NIST hash function Definitions",
    "sourceNote": "Abstracts fixed finite output evaluation without security assumptions.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:theorem/DigestFunction-model-satisfaction",
    "type": "Theorem",
    "name": "model-satisfaction",
    "statement": "Total digest evaluation has a unique result, and the concrete modulo-two digest has distinct outputs for 0 and 1.",
    "formalStatement": "(∀ (A : Type) (n : Nat) (h : Catalog.DigestFunction A n) (x : A), ∃! d : Fin n, d = h x) ∧ Catalog.exampleDigest 0 ≠ Catalog.exampleDigest 1",
    "assumptions": [
      "Uses the concrete exampleDigest(x)=x mod 2 and exampleDigestScope={x:ℕ | x<2}; injectivity is proved, not assumed."
    ],
    "appliesTo": [
      "urn:csabs:concept/DigestFunction"
    ],
    "dependsOn": [
      "urn:csabs:axiom/DigestFunction-total-evaluation"
    ],
    "proofSketch": "Typed evaluation gives the unique witness h(x). Compute the two distinct concrete outputs.",
    "reviewStatus": "Registered Lean witness; verification status requires a fresh compiler and axiom-audit report.",
    "source": [
      "urn:csabs:source/mathlib-scoped-digest",
      "urn:csabs:source/lean-digests"
    ],
    "sourceLocator": "Set.InjOn; Set.InjOn.eq_iff; Set.InjOn.mono; Catalog.digest_model_satisfaction",
    "sourceNote": "Derived for the finite digest profile with explicit premise mappings. Concrete model satisfaction is separate from the defining Axioms.",
    "provenanceKind": "derived",
    "leanFormulation": "(∀ (A : Type) (n : Nat) (h : Catalog.DigestFunction A n) (x : A), ∃! d : Fin n, d = h x) ∧ Catalog.exampleDigest 0 ≠ Catalog.exampleDigest 1",
    "formulationSource": "urn:csabs:source/lean-digests",
    "formulationLocator": "Catalog.digest_model_satisfaction",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Total digest evaluation has a unique result, and the concrete modulo-two digest has distinct outputs for 0 and 1.",
    "leanModelLimitations": "Exact mathematical equality and finite outputs only. No cryptographic security, collision search algorithm, implementation refinement, serialization correctness, or automatic proof of injectivity for a supplied hash and set.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/DigestFunction-total-evaluation\": \"Proved obligation for exampleDigest and exampleDigestScope, not an assumed law field.\"}"
  }
]
```
<!-- graph-record:end -->
