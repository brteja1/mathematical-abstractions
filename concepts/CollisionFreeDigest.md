# Digest with explicit collision freedom on a specified set

A deterministic finite digest h together with a specified set S of inputs and explicit evidence that h is injective on S. The assumption applies to pairs of members of S only.

**Notation:** h : A → D; S ⊆ A; ∀x,y∈S, h(x)=h(y) ⇒ x=y

**Stable ID:** `urn:csabs:concept/CollisionFreeDigest`

**Categories:** Set theory and foundations

**Kind:** Mathematical structure

**Prerequisites:** [Total function](Function.md), [Finite carrier with exhaustive enumeration](FiniteType.md), [Deterministic finite digest function](DigestFunction.md)

**Specializes:** [Deterministic finite digest function](DigestFunction.md)

**Related concepts:** [Pigeonhole Principle](PigeonholePrinciple.md)

## Mathematical formulation

ScopedDigest(A,n,S)={(h,p) | h:A→Fin(n), p:∀x∈S,∀y∈S,h(x)=h(y)⇒x=y}. Evidence is required to instantiate this profile; it is not obtained from cryptographic collision resistance.

**Lean formulation** (in its source module context):

```lean
structure CollisionFreeDigest (A : Type) (n : Nat) (S : Set A) where
  digest : DigestFunction A n
  collisionFree : Set.InjOn digest S
```

**Source:** [`Catalog.CollisionFreeDigest`](../lean/Catalog/Digests.lean); consulted 2026-11-20.

**Scope:** model

**Interpretation:** CollisionFreeDigest stores h:A→Fin(n) and Set.InjOn h S; both membership conditions remain explicit.

**Limits:** Exact mathematical equality and finite outputs only. No cryptographic security, collision search algorithm, implementation refinement, serialization correctness, or automatic proof of injectivity for a supplied hash and set.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Typed total single-valued evaluation plus Set.InjOn h S. Both constraints are explicit; no axiom inheritance is assumed.

**basisKind:** defined-structure

**basisScope:** A is any carrier; D is a fixed finite set represented by Fin(n), n≥0. For bit digests of width w use n=2^w with an explicit encoding bijection. Equality is exact value equality. An empty A admits the empty function, including n=0; if A is inhabited then n must be positive. S may be empty or singleton, making injectivity vacuous, but this does not justify applications needing two distinct members. No overflow, rounding, randomness, state, concurrency or cost semantics. A key or seed must be fixed as part of h. Input serialization must preserve the equality being claimed.

**specializationNote:** Forget the set-scoped injectivity evidence and retain the same h:A→Fin(n), carrier, output encoding and evaluation. The set is a parameter restricting the law, not the domain of h.

**verificationObligation:** Supply the actual h, fixed output encoding and exact equality mapping.; For the scoped variant, prove collision freedom for the actual S; both compared inputs must belong to S.; Changing h, the seed/key, input encoding, or enlarging S requires new evidence. Subset restriction preserves the guarantee.; The model is noncryptographic; no probability bound or computational hardness claim follows.

**reviewStatus:** Sourced definitions and separately registered Lean theorem witnesses; inspect fresh verification evidence for proof status.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-CollisionFreeDigest-digest"></a>

### digest

`urn:csabs:operation/CollisionFreeDigest-digest`

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

<a id="node-urn-csabs-axiom-CollisionFreeDigest-injective-on-set"></a>

### collision freedom on the specified set

`urn:csabs:axiom/CollisionFreeDigest-injective-on-set`

**statement:** Equal digests of two inputs in S imply equal inputs. This is an explicit assumption for the selected h and S.

**formalStatement:** ∀x∈S, ∀y∈S, h(x)=h(y) ⇒ x=y

**assumptions:** h:A→D and S⊆A are fixed.; No conclusion is provided if either input lies outside S.

**ruleRole:** structure-law

**reviewStatus:** Explicit model constraint; no universal collision-freedom assertion.

**source:** [Mathlib pinned set-restricted injectivity and equality rules](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Set); citation: Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679: Data/Set/Operations.lean, Set.InjOn; Data/Set/Function.lean, Set.InjOn.eq_iff and Set.InjOn.mono. Apache-2.0.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; [NIST CSRC glossary: hash function and collision resistance](https://csrc.nist.gov/glossary/term/hash_function); citation: NIST CSRC Glossary, hash function, Definitions; collision resistance, Definitions (https://csrc.nist.gov/glossary/term/collision_resistance).; accessedOn: 2026-11-20; sourceRole: consulted-terminology-reference

**sourceLocator:** Set.InjOn (Data/Set/Operations.lean); Set.InjOn.eq_iff and Set.InjOn.mono (Data/Set/Function.lean); NIST glossary Definitions

**sourceNote:** Constructed finite digest interface and explicit set-scoped injectivity profile. NIST supplies terminology and the distinction from computational collision resistance; Mathlib supplies the precise injectivity predicate and rules.

**provenanceKind:** adapted

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-CollisionFreeDigest-model-satisfaction"></a>

### model-satisfaction

`urn:csabs:theorem/CollisionFreeDigest-model-satisfaction`

**statement:** The modulo-two digest satisfies collision freedom on S={0,1}, with two distinct members, yet 0 and the out-of-scope input 2 collide.

**formalStatement:** Set.InjOn Catalog.exampleDigest Catalog.exampleDigestScope ∧ (0 ∈ Catalog.exampleDigestScope ∧ 1 ∈ Catalog.exampleDigestScope ∧ (0 : Nat) ≠ 1) ∧ (2 ∉ Catalog.exampleDigestScope ∧ Catalog.exampleDigest 0 = Catalog.exampleDigest 2)

**assumptions:** Uses the concrete exampleDigest(x)=x mod 2 and exampleDigestScope={x:ℕ | x<2}; injectivity is proved, not assumed.

**dependsOn:** [total single-valued evaluation](DigestFunction.md#node-urn-csabs-axiom-DigestFunction-total-evaluation); [collision freedom on the specified set](CollisionFreeDigest.md#node-urn-csabs-axiom-CollisionFreeDigest-injective-on-set)

**proofSketch:** For x,y<2, reduce x mod 2 and y mod 2 to x and y. Evaluate 0,1,2 to prove nonvacuity and the out-of-scope collision.

**reviewStatus:** Registered Lean witness; verification status requires a fresh compiler and axiom-audit report.

**source:** [Mathlib pinned set-restricted injectivity and equality rules](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Set); citation: Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679: Data/Set/Operations.lean, Set.InjOn; Data/Set/Function.lean, Set.InjOn.eq_iff and Set.InjOn.mono. Apache-2.0.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; Catalog digest models and scoped-injectivity witnesses; path: lean/Catalog/Digests.lean; accessedOn: 2026-11-20; sourceRole: local-lean-formulation-and-proof

**sourceLocator:** Set.InjOn; Set.InjOn.eq_iff; Set.InjOn.mono; Catalog.scoped_digest_model_satisfaction

**sourceNote:** Derived for the finite digest profile with explicit premise mappings. Concrete model satisfaction is separate from the defining Axioms.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
Set.InjOn Catalog.exampleDigest Catalog.exampleDigestScope ∧ (0 ∈ Catalog.exampleDigestScope ∧ 1 ∈ Catalog.exampleDigestScope ∧ (0 : Nat) ≠ 1) ∧ (2 ∉ Catalog.exampleDigestScope ∧ Catalog.exampleDigest 0 = Catalog.exampleDigest 2)
```

**Source:** [`Catalog.scoped_digest_model_satisfaction`](../lean/Catalog/Digests.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** The modulo-two digest satisfies collision freedom on S={0,1}, with two distinct members, yet 0 and the out-of-scope input 2 collide.

**Limits:** Exact mathematical equality and finite outputs only. No cryptographic security, collision search algorithm, implementation refinement, serialization correctness, or automatic proof of injectivity for a supplied hash and set.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/CollisionFreeDigest-injective-on-set": "Proved obligation for exampleDigest and exampleDigestScope, not an assumed law field.",
  "urn:csabs:axiom/DigestFunction-total-evaluation": "Proved obligation for exampleDigest and exampleDigestScope, not an assumed law field."
}
```

<a id="node-urn-csabs-theorem-CollisionFreeDigest-equality-reflection"></a>

### equality-reflection

`urn:csabs:theorem/CollisionFreeDigest-equality-reflection`

**statement:** For two inputs in S, digest equality is equivalent to input equality.

**formalStatement:** ∀ {A : Type} {n : Nat} {S : Set A} (h : Catalog.CollisionFreeDigest A n S) (x y : A), x ∈ S → y ∈ S → (h.digest x = h.digest y ↔ x = y)

**assumptions:** Fixed A,n,S and a supplied CollisionFreeDigest h; exactly the binders and side conditions in the formal statement.

**dependsOn:** [total single-valued evaluation](DigestFunction.md#node-urn-csabs-axiom-DigestFunction-total-evaluation); [collision freedom on the specified set](CollisionFreeDigest.md#node-urn-csabs-axiom-CollisionFreeDigest-injective-on-set)

**proofSketch:** Forward direction uses scoped injectivity and both membership proofs; reverse direction substitutes equal inputs.

**reviewStatus:** Registered Lean witness; verification status requires a fresh compiler and axiom-audit report.

**source:** [Mathlib pinned set-restricted injectivity and equality rules](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Set); citation: Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679: Data/Set/Operations.lean, Set.InjOn; Data/Set/Function.lean, Set.InjOn.eq_iff and Set.InjOn.mono. Apache-2.0.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; Catalog digest models and scoped-injectivity witnesses; path: lean/Catalog/Digests.lean; accessedOn: 2026-11-20; sourceRole: local-lean-formulation-and-proof

**sourceLocator:** Set.InjOn; Set.InjOn.eq_iff; Set.InjOn.mono; Catalog.scoped_digest_eq_iff

**sourceNote:** Derived for the finite digest profile with explicit premise mappings. Concrete model satisfaction is separate from the defining Axioms.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {A : Type} {n : Nat} {S : Set A} (h : Catalog.CollisionFreeDigest A n S) (x y : A), x ∈ S → y ∈ S → (h.digest x = h.digest y ↔ x = y)
```

**Source:** [`Catalog.scoped_digest_eq_iff`](../lean/Catalog/Digests.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** For two inputs in S, digest equality is equivalent to input equality.

**Limits:** Exact mathematical equality and finite outputs only. No cryptographic security, collision search algorithm, implementation refinement, serialization correctness, or automatic proof of injectivity for a supplied hash and set.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/CollisionFreeDigest-injective-on-set": "h.collisionFree is the explicit hypothesis; scoped membership is retained.",
  "urn:csabs:axiom/DigestFunction-total-evaluation": "Typed digest evaluation."
}
```

<a id="node-urn-csabs-theorem-CollisionFreeDigest-subset-restriction"></a>

### subset-restriction

`urn:csabs:theorem/CollisionFreeDigest-subset-restriction`

**statement:** Collision freedom on S remains valid on every subset T⊆S for the same digest.

**formalStatement:** ∀ {A : Type} {n : Nat} {S T : Set A} (h : Catalog.CollisionFreeDigest A n S), T ⊆ S → Set.InjOn h.digest T

**assumptions:** Fixed A,n,S and a supplied CollisionFreeDigest h; exactly the binders and side conditions in the formal statement.

**dependsOn:** [collision freedom on the specified set](CollisionFreeDigest.md#node-urn-csabs-axiom-CollisionFreeDigest-injective-on-set)

**proofSketch:** Map both T membership proofs into S, then apply scoped injectivity. This does not establish closure under unions or enlargement.

**reviewStatus:** Registered Lean witness; verification status requires a fresh compiler and axiom-audit report.

**source:** [Mathlib pinned set-restricted injectivity and equality rules](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Set); citation: Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679: Data/Set/Operations.lean, Set.InjOn; Data/Set/Function.lean, Set.InjOn.eq_iff and Set.InjOn.mono. Apache-2.0.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; Catalog digest models and scoped-injectivity witnesses; path: lean/Catalog/Digests.lean; accessedOn: 2026-11-20; sourceRole: local-lean-formulation-and-proof

**sourceLocator:** Set.InjOn; Set.InjOn.eq_iff; Set.InjOn.mono; Catalog.scoped_digest_subset

**sourceNote:** Derived for the finite digest profile with explicit premise mappings. Concrete model satisfaction is separate from the defining Axioms.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {A : Type} {n : Nat} {S T : Set A} (h : Catalog.CollisionFreeDigest A n S), T ⊆ S → Set.InjOn h.digest T
```

**Source:** [`Catalog.scoped_digest_subset`](../lean/Catalog/Digests.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** Collision freedom on S remains valid on every subset T⊆S for the same digest.

**Limits:** Exact mathematical equality and finite outputs only. No cryptographic security, collision search algorithm, implementation refinement, serialization correctness, or automatic proof of injectivity for a supplied hash and set.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/CollisionFreeDigest-injective-on-set": "h.collisionFree is the explicit hypothesis; scoped membership is retained."
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
    "id": "urn:csabs:concept/CollisionFreeDigest",
    "type": "Concept",
    "shortForm": "CollisionFreeDigest",
    "fullName": "Digest with explicit collision freedom on a specified set",
    "synonyms": [
      "Set-scoped collision-free hash",
      "Digest injective on a specified set"
    ],
    "category": [
      "urn:csabs:category/foundations"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "A deterministic finite digest h together with a specified set S of inputs and explicit evidence that h is injective on S. The assumption applies to pairs of members of S only.",
    "notation": "h : A → D; S ⊆ A; ∀x,y∈S, h(x)=h(y) ⇒ x=y",
    "requiresConcept": [
      "urn:csabs:concept/Function",
      "urn:csabs:concept/FiniteType",
      "urn:csabs:concept/DigestFunction"
    ],
    "relatedConcept": [
      "urn:csabs:concept/PigeonholePrinciple"
    ],
    "axiomBasis": "Typed total single-valued evaluation plus Set.InjOn h S. Both constraints are explicit; no axiom inheritance is assumed.",
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
      "urn:csabs:operation/CollisionFreeDigest-digest"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/DigestFunction-total-evaluation",
      "urn:csabs:axiom/CollisionFreeDigest-injective-on-set"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/CollisionFreeDigest-model-satisfaction",
      "urn:csabs:theorem/CollisionFreeDigest-equality-reflection",
      "urn:csabs:theorem/CollisionFreeDigest-subset-restriction"
    ],
    "mathematicalFormulation": "ScopedDigest(A,n,S)={(h,p) | h:A→Fin(n), p:∀x∈S,∀y∈S,h(x)=h(y)⇒x=y}. Evidence is required to instantiate this profile; it is not obtained from cryptographic collision resistance.",
    "source": [
      "urn:csabs:source/mathlib-scoped-digest",
      "urn:csabs:source/nist-hash-glossary-2026-11-20"
    ],
    "sourceLocator": "Set.InjOn (Data/Set/Operations.lean); Set.InjOn.eq_iff and Set.InjOn.mono (Data/Set/Function.lean); NIST glossary Definitions",
    "sourceNote": "Constructed finite digest interface and explicit set-scoped injectivity profile. NIST supplies terminology and the distinction from computational collision resistance; Mathlib supplies the precise injectivity predicate and rules.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/DigestFunction"
    ],
    "specializationNote": "Forget the set-scoped injectivity evidence and retain the same h:A→Fin(n), carrier, output encoding and evaluation. The set is a parameter restricting the law, not the domain of h.",
    "leanFormulation": "structure CollisionFreeDigest (A : Type) (n : Nat) (S : Set A) where\n  digest : DigestFunction A n\n  collisionFree : Set.InjOn digest S",
    "formulationSource": "urn:csabs:source/lean-digests",
    "formulationLocator": "Catalog.CollisionFreeDigest",
    "formulationScope": "model",
    "leanModelMapping": "CollisionFreeDigest stores h:A→Fin(n) and Set.InjOn h S; both membership conditions remain explicit.",
    "leanModelLimitations": "Exact mathematical equality and finite outputs only. No cryptographic security, collision search algorithm, implementation refinement, serialization correctness, or automatic proof of injectivity for a supplied hash and set."
  },
  {
    "id": "urn:csabs:operation/CollisionFreeDigest-digest",
    "type": "Operation",
    "concept": "urn:csabs:concept/CollisionFreeDigest",
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
    "id": "urn:csabs:axiom/DigestFunction-total-evaluation",
    "type": "Axiom",
    "name": "total single-valued evaluation",
    "statement": "Every input has exactly one digest in the fixed finite output space.",
    "formalStatement": "∀x∈A, ∃!d∈D: d=h(x)",
    "assumptions": [
      "h:A→D is a typed total function; D≅Fin(n)."
    ],
    "appliesTo": [
      "urn:csabs:concept/DigestFunction",
      "urn:csabs:concept/CollisionFreeDigest"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Structure constraint; concrete model evidence is a separate Theorem.",
    "source": [
      "urn:csabs:source/mathlib-scoped-digest",
      "urn:csabs:source/nist-hash-glossary-2026-11-20"
    ],
    "sourceLocator": "Set.InjOn (Data/Set/Operations.lean); Set.InjOn.eq_iff and Set.InjOn.mono (Data/Set/Function.lean); NIST glossary Definitions",
    "sourceNote": "Constructed finite digest interface and explicit set-scoped injectivity profile. NIST supplies terminology and the distinction from computational collision resistance; Mathlib supplies the precise injectivity predicate and rules.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/CollisionFreeDigest-injective-on-set",
    "type": "Axiom",
    "name": "collision freedom on the specified set",
    "statement": "Equal digests of two inputs in S imply equal inputs. This is an explicit assumption for the selected h and S.",
    "formalStatement": "∀x∈S, ∀y∈S, h(x)=h(y) ⇒ x=y",
    "assumptions": [
      "h:A→D and S⊆A are fixed.",
      "No conclusion is provided if either input lies outside S."
    ],
    "appliesTo": [
      "urn:csabs:concept/CollisionFreeDigest"
    ],
    "ruleRole": "structure-law",
    "reviewStatus": "Explicit model constraint; no universal collision-freedom assertion.",
    "source": [
      "urn:csabs:source/mathlib-scoped-digest",
      "urn:csabs:source/nist-hash-glossary-2026-11-20"
    ],
    "sourceLocator": "Set.InjOn (Data/Set/Operations.lean); Set.InjOn.eq_iff and Set.InjOn.mono (Data/Set/Function.lean); NIST glossary Definitions",
    "sourceNote": "Constructed finite digest interface and explicit set-scoped injectivity profile. NIST supplies terminology and the distinction from computational collision resistance; Mathlib supplies the precise injectivity predicate and rules.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:theorem/CollisionFreeDigest-model-satisfaction",
    "type": "Theorem",
    "name": "model-satisfaction",
    "statement": "The modulo-two digest satisfies collision freedom on S={0,1}, with two distinct members, yet 0 and the out-of-scope input 2 collide.",
    "formalStatement": "Set.InjOn Catalog.exampleDigest Catalog.exampleDigestScope ∧ (0 ∈ Catalog.exampleDigestScope ∧ 1 ∈ Catalog.exampleDigestScope ∧ (0 : Nat) ≠ 1) ∧ (2 ∉ Catalog.exampleDigestScope ∧ Catalog.exampleDigest 0 = Catalog.exampleDigest 2)",
    "assumptions": [
      "Uses the concrete exampleDigest(x)=x mod 2 and exampleDigestScope={x:ℕ | x<2}; injectivity is proved, not assumed."
    ],
    "appliesTo": [
      "urn:csabs:concept/CollisionFreeDigest"
    ],
    "dependsOn": [
      "urn:csabs:axiom/DigestFunction-total-evaluation",
      "urn:csabs:axiom/CollisionFreeDigest-injective-on-set"
    ],
    "proofSketch": "For x,y<2, reduce x mod 2 and y mod 2 to x and y. Evaluate 0,1,2 to prove nonvacuity and the out-of-scope collision.",
    "reviewStatus": "Registered Lean witness; verification status requires a fresh compiler and axiom-audit report.",
    "source": [
      "urn:csabs:source/mathlib-scoped-digest",
      "urn:csabs:source/lean-digests"
    ],
    "sourceLocator": "Set.InjOn; Set.InjOn.eq_iff; Set.InjOn.mono; Catalog.scoped_digest_model_satisfaction",
    "sourceNote": "Derived for the finite digest profile with explicit premise mappings. Concrete model satisfaction is separate from the defining Axioms.",
    "provenanceKind": "derived",
    "leanFormulation": "Set.InjOn Catalog.exampleDigest Catalog.exampleDigestScope ∧ (0 ∈ Catalog.exampleDigestScope ∧ 1 ∈ Catalog.exampleDigestScope ∧ (0 : Nat) ≠ 1) ∧ (2 ∉ Catalog.exampleDigestScope ∧ Catalog.exampleDigest 0 = Catalog.exampleDigest 2)",
    "formulationSource": "urn:csabs:source/lean-digests",
    "formulationLocator": "Catalog.scoped_digest_model_satisfaction",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "The modulo-two digest satisfies collision freedom on S={0,1}, with two distinct members, yet 0 and the out-of-scope input 2 collide.",
    "leanModelLimitations": "Exact mathematical equality and finite outputs only. No cryptographic security, collision search algorithm, implementation refinement, serialization correctness, or automatic proof of injectivity for a supplied hash and set.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/CollisionFreeDigest-injective-on-set\": \"Proved obligation for exampleDigest and exampleDigestScope, not an assumed law field.\", \"urn:csabs:axiom/DigestFunction-total-evaluation\": \"Proved obligation for exampleDigest and exampleDigestScope, not an assumed law field.\"}"
  },
  {
    "id": "urn:csabs:theorem/CollisionFreeDigest-equality-reflection",
    "type": "Theorem",
    "name": "equality-reflection",
    "statement": "For two inputs in S, digest equality is equivalent to input equality.",
    "formalStatement": "∀ {A : Type} {n : Nat} {S : Set A} (h : Catalog.CollisionFreeDigest A n S) (x y : A), x ∈ S → y ∈ S → (h.digest x = h.digest y ↔ x = y)",
    "assumptions": [
      "Fixed A,n,S and a supplied CollisionFreeDigest h; exactly the binders and side conditions in the formal statement."
    ],
    "appliesTo": [
      "urn:csabs:concept/CollisionFreeDigest"
    ],
    "dependsOn": [
      "urn:csabs:axiom/DigestFunction-total-evaluation",
      "urn:csabs:axiom/CollisionFreeDigest-injective-on-set"
    ],
    "proofSketch": "Forward direction uses scoped injectivity and both membership proofs; reverse direction substitutes equal inputs.",
    "reviewStatus": "Registered Lean witness; verification status requires a fresh compiler and axiom-audit report.",
    "source": [
      "urn:csabs:source/mathlib-scoped-digest",
      "urn:csabs:source/lean-digests"
    ],
    "sourceLocator": "Set.InjOn; Set.InjOn.eq_iff; Set.InjOn.mono; Catalog.scoped_digest_eq_iff",
    "sourceNote": "Derived for the finite digest profile with explicit premise mappings. Concrete model satisfaction is separate from the defining Axioms.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {A : Type} {n : Nat} {S : Set A} (h : Catalog.CollisionFreeDigest A n S) (x y : A), x ∈ S → y ∈ S → (h.digest x = h.digest y ↔ x = y)",
    "formulationSource": "urn:csabs:source/lean-digests",
    "formulationLocator": "Catalog.scoped_digest_eq_iff",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "For two inputs in S, digest equality is equivalent to input equality.",
    "leanModelLimitations": "Exact mathematical equality and finite outputs only. No cryptographic security, collision search algorithm, implementation refinement, serialization correctness, or automatic proof of injectivity for a supplied hash and set.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/CollisionFreeDigest-injective-on-set\": \"h.collisionFree is the explicit hypothesis; scoped membership is retained.\", \"urn:csabs:axiom/DigestFunction-total-evaluation\": \"Typed digest evaluation.\"}"
  },
  {
    "id": "urn:csabs:theorem/CollisionFreeDigest-subset-restriction",
    "type": "Theorem",
    "name": "subset-restriction",
    "statement": "Collision freedom on S remains valid on every subset T⊆S for the same digest.",
    "formalStatement": "∀ {A : Type} {n : Nat} {S T : Set A} (h : Catalog.CollisionFreeDigest A n S), T ⊆ S → Set.InjOn h.digest T",
    "assumptions": [
      "Fixed A,n,S and a supplied CollisionFreeDigest h; exactly the binders and side conditions in the formal statement."
    ],
    "appliesTo": [
      "urn:csabs:concept/CollisionFreeDigest"
    ],
    "dependsOn": [
      "urn:csabs:axiom/CollisionFreeDigest-injective-on-set"
    ],
    "proofSketch": "Map both T membership proofs into S, then apply scoped injectivity. This does not establish closure under unions or enlargement.",
    "reviewStatus": "Registered Lean witness; verification status requires a fresh compiler and axiom-audit report.",
    "source": [
      "urn:csabs:source/mathlib-scoped-digest",
      "urn:csabs:source/lean-digests"
    ],
    "sourceLocator": "Set.InjOn; Set.InjOn.eq_iff; Set.InjOn.mono; Catalog.scoped_digest_subset",
    "sourceNote": "Derived for the finite digest profile with explicit premise mappings. Concrete model satisfaction is separate from the defining Axioms.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {A : Type} {n : Nat} {S T : Set A} (h : Catalog.CollisionFreeDigest A n S), T ⊆ S → Set.InjOn h.digest T",
    "formulationSource": "urn:csabs:source/lean-digests",
    "formulationLocator": "Catalog.scoped_digest_subset",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Collision freedom on S remains valid on every subset T⊆S for the same digest.",
    "leanModelLimitations": "Exact mathematical equality and finite outputs only. No cryptographic security, collision search algorithm, implementation refinement, serialization correctness, or automatic proof of injectivity for a supplied hash and set.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/CollisionFreeDigest-injective-on-set\": \"h.collisionFree is the explicit hypothesis; scoped membership is retained.\"}"
  }
]
```
<!-- graph-record:end -->
