# Monoid

A semigroup with a two-sided identity element.

**Notation:** (M,·,e), associativity and ∀x∈M: e·x=x·e=x.

**Stable ID:** `urn:csabs:concept/Monoid`

**Categories:** Algebra

**Kind:** Mathematical structure

**Prerequisites:** [Semigroup](Semigroup.md)

**Specializes:** [Semigroup](Semigroup.md)

## Backlinks

- [Formal language of finite words](FormalLanguage.md) — `relatedConcept`
- [Group](Group.md) — `requiresConcept`
- [Group](Group.md) — `specializationOf`
- [Exclusive finite-heap separation predicates](HeapSeparation.md) — `relatedConcept`

## Mathematical formulation

A monoid is (A,·,1) with associative multiplication and ∀a,1·a=a=a·1. Equality is carrier equality; the singleton carrier is permitted.

**Lean formulation** (in its source module context):

```lean
abbrev Monoid (A : Type u) := _root_.Monoid A
```

**Source:** [`Catalog.Monoid`](../lean/Catalog/Algebra.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Mathlib Monoid; one gives nonemptiness, mul_assoc and both identity equations.

**Limits:** Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Nonempty carrier with closed binary multiplication; associativity; two-sided identity. Multiplication need not commute.

**basisKind:** axiomatic-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**verificationObligation:** Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-monoid-product"></a>

### binary operation

`urn:csabs:operation/monoid-product`

**signature:** · : M×M→M

**description:** Associative composition with identity element e.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-monoid-identity"></a>

### monoid-identity

`urn:csabs:axiom/monoid-identity`

**statement:** There is a two-sided identity element.

**formalStatement:** ∃e∈M ∀x∈M: e·x=x·e=x

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

**assumptions:** Use the linked concept’s explicit basis and carrier conventions.

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Monoid-closed-carrier"></a>

### closed-carrier

`urn:csabs:axiom/Monoid-closed-carrier`

**statement:** The binary operation is total on a nonempty carrier.

**formalStatement:** S≠∅; ·:S×S→S

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Monoid-associative"></a>

### associative

`urn:csabs:axiom/Monoid-associative`

**statement:** Multiplication is associative.

**formalStatement:** (x·y)·z=x·(y·z)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Monoid-identity"></a>

### identity

`urn:csabs:axiom/Monoid-identity`

**statement:** The identity is a two-sided unit.

**formalStatement:** e∈S; e·x=x; x·e=x

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

<a id="node-urn-csabs-law-monoid-identity-unique"></a>

### law/monoid-identity-unique

`urn:csabs:law/monoid-identity-unique`

**statement:** A monoid has at most one identity element.

**formalStatement:** e,e' identities ⇒ e=e'

**reviewStatus:** editorial-summary; not machine-proved

**proofSketch:** For identities e and e', e=e·e'=e'.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [monoid-identity](Monoid.md#node-urn-csabs-axiom-monoid-identity); [closed-carrier](Monoid.md#node-urn-csabs-axiom-Monoid-closed-carrier); [associative](Monoid.md#node-urn-csabs-axiom-Monoid-associative); [identity](Monoid.md#node-urn-csabs-axiom-Monoid-identity)

**assumptions:** Use the explicit mathematical bases and typed carriers of the linked concepts.

**provenanceStatus:** legacy-source-missing

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {A : Type u} [Catalog.Monoid A] (e e' : A), ((∀ x, e * x = x) ∧ (∀ x, x * e = x)) → ((∀ x, e' * x = x) ∧ (∀ x, x * e' = x)) → e = e'
```

**Source:** [`Catalog.Proofs.monoid_identity_unique`](../lean/Catalog/Witnesses.lean); consulted 2026-11-12.

**Scope:** registered-witness-type

**Interpretation:** Mathlib Monoid; one gives nonemptiness, mul_assoc and both identity equations.

**Limits:** Witness proves the explicit expectedType under its binders. Correspondence to the informal statement is reviewed metadata, not mechanically proved. Original citation gaps remain disclosed in the catalog.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/Monoid-associative": "Explicit interface premise: (x·y)·z=x·(y·z); interpreted by Catalog.Monoid. See the carrier/operation mapping; closure is enforced by typed operations and axioms are hypotheses carried by these structures, not new Lean axiom declarations.",
  "urn:csabs:axiom/Monoid-closed-carrier": "Explicit interface premise: S≠∅; ·:S×S→S; interpreted by Catalog.Monoid. See the carrier/operation mapping; closure is enforced by typed operations and axioms are hypotheses carried by these structures, not new Lean axiom declarations.",
  "urn:csabs:axiom/Monoid-identity": "Explicit interface premise: e∈S; e·x=x; x·e=x; interpreted by Catalog.Monoid. See the carrier/operation mapping; closure is enforced by typed operations and axioms are hypotheses carried by these structures, not new Lean axiom declarations.",
  "urn:csabs:axiom/monoid-identity": "Explicit interface premise: ∃e∈M ∀x∈M: e·x=x·e=x; interpreted by Catalog.Monoid. See the carrier/operation mapping; closure is enforced by typed operations and axioms are hypotheses carried by these structures, not new Lean axiom declarations."
}
```

## Theorems

<a id="node-urn-csabs-theorem-Monoid-power-addition"></a>

### power-addition

`urn:csabs:theorem/Monoid-power-addition`

**statement:** Natural powers turn exponent addition into multiplication.

**formalStatement:** x^0=e; x^(n+1)=x^n·x; x^(m+n)=x^m·x^n

**proofSketch:** Induct on n, using identity for zero and associativity in the successor case.

**assumptions:** The explicit basis, carriers, and side conditions stated for Monoid apply.

**dependsOn:** [monoid-identity](Monoid.md#node-urn-csabs-axiom-monoid-identity); [closed-carrier](Monoid.md#node-urn-csabs-axiom-Monoid-closed-carrier); [associative](Monoid.md#node-urn-csabs-axiom-Monoid-associative); [identity](Monoid.md#node-urn-csabs-axiom-Monoid-identity)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {A : Type u} [Catalog.Monoid A] (a : A) (m n : Nat), a ^ 0 = 1 ∧ a ^ (n + 1) = a ^ n * a ∧ a ^ (m + n) = a ^ m * a ^ n
```

**Source:** [`Catalog.Proofs.monoid_power_addition`](../lean/Catalog/Witnesses.lean); consulted 2026-11-12.

**Scope:** registered-witness-type

**Interpretation:** Mathlib Monoid; one gives nonemptiness, mul_assoc and both identity equations.

**Limits:** Witness proves the explicit expectedType under its binders. Correspondence to the informal statement is reviewed metadata, not mechanically proved. Original citation gaps remain disclosed in the catalog.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/Monoid-associative": "Explicit interface premise: (x·y)·z=x·(y·z); interpreted by Catalog.Monoid. See the carrier/operation mapping; closure is enforced by typed operations and axioms are hypotheses carried by these structures, not new Lean axiom declarations.",
  "urn:csabs:axiom/Monoid-closed-carrier": "Explicit interface premise: S≠∅; ·:S×S→S; interpreted by Catalog.Monoid. See the carrier/operation mapping; closure is enforced by typed operations and axioms are hypotheses carried by these structures, not new Lean axiom declarations.",
  "urn:csabs:axiom/Monoid-identity": "Explicit interface premise: e∈S; e·x=x; x·e=x; interpreted by Catalog.Monoid. See the carrier/operation mapping; closure is enforced by typed operations and axioms are hypotheses carried by these structures, not new Lean axiom declarations.",
  "urn:csabs:axiom/monoid-identity": "Explicit interface premise: ∃e∈M ∀x∈M: e·x=x·e=x; interpreted by Catalog.Monoid. See the carrier/operation mapping; closure is enforced by typed operations and axioms are hypotheses carried by these structures, not new Lean axiom declarations."
}
```

## Concept provenance

- [Mathlib group definitions](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Defs.html); sourceRole: reference-for-selected-basis

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/Monoid",
    "type": "Concept",
    "shortForm": "Monoid",
    "fullName": "Monoid",
    "category": [
      "urn:csabs:category/algebra"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "A semigroup with a two-sided identity element.",
    "notation": "(M,·,e), associativity and ∀x∈M: e·x=x·e=x.",
    "hasOperation": [
      "urn:csabs:operation/monoid-product"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/monoid-identity",
      "urn:csabs:axiom/Monoid-closed-carrier",
      "urn:csabs:axiom/Monoid-associative",
      "urn:csabs:axiom/Monoid-identity"
    ],
    "hasLaw": [
      "urn:csabs:law/monoid-identity-unique"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/Monoid-power-addition"
    ],
    "specializationOf": [
      "urn:csabs:concept/Semigroup"
    ],
    "coverageStatus": "basis-reviewed",
    "requiresConcept": [
      "urn:csabs:concept/Semigroup"
    ],
    "verificationObligation": [
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Nonempty carrier with closed binary multiplication; associativity; two-sided identity. Multiplication need not commute.",
    "basisKind": "axiomatic-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "source": [
      "urn:csabs:source/mathlib-group"
    ],
    "leanFormulation": "abbrev Monoid (A : Type u) := _root_.Monoid A",
    "formulationSource": "urn:csabs:source/local-lean-Algebra",
    "formulationLocator": "Catalog.Monoid",
    "formulationScope": "model",
    "leanModelMapping": "Mathlib Monoid; one gives nonemptiness, mul_assoc and both identity equations.",
    "leanModelLimitations": "Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.",
    "mathematicalFormulation": "A monoid is (A,·,1) with associative multiplication and ∀a,1·a=a=a·1. Equality is carrier equality; the singleton carrier is permitted."
  },
  {
    "id": "urn:csabs:operation/monoid-product",
    "type": "Operation",
    "name": "binary operation",
    "signature": "· : M×M→M",
    "description": "Associative composition with identity element e.",
    "concept": "urn:csabs:concept/Monoid"
  },
  {
    "id": "urn:csabs:axiom/monoid-identity",
    "type": "Axiom",
    "statement": "There is a two-sided identity element.",
    "formalStatement": "∃e∈M ∀x∈M: e·x=x·e=x",
    "appliesTo": [
      "urn:csabs:concept/Monoid"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law",
    "name": "monoid-identity",
    "assumptions": [
      "Use the linked concept’s explicit basis and carrier conventions."
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/Monoid-closed-carrier",
    "type": "Axiom",
    "name": "closed-carrier",
    "statement": "The binary operation is total on a nonempty carrier.",
    "formalStatement": "S≠∅; ·:S×S→S",
    "appliesTo": [
      "urn:csabs:concept/Monoid"
    ],
    "assumptions": [
      "All variables range over the carriers and semantic conventions specified in this concept."
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/Monoid-associative",
    "type": "Axiom",
    "name": "associative",
    "statement": "Multiplication is associative.",
    "formalStatement": "(x·y)·z=x·(y·z)",
    "appliesTo": [
      "urn:csabs:concept/Monoid"
    ],
    "assumptions": [
      "All variables range over the carriers and semantic conventions specified in this concept."
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/Monoid-identity",
    "type": "Axiom",
    "name": "identity",
    "statement": "The identity is a two-sided unit.",
    "formalStatement": "e∈S; e·x=x; x·e=x",
    "appliesTo": [
      "urn:csabs:concept/Monoid"
    ],
    "assumptions": [
      "All variables range over the carriers and semantic conventions specified in this concept."
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:law/monoid-identity-unique",
    "type": "Law",
    "statement": "A monoid has at most one identity element.",
    "formalStatement": "e,e' identities ⇒ e=e'",
    "appliesTo": [
      "urn:csabs:concept/Monoid"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "proofSketch": "For identities e and e', e=e·e'=e'.",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/monoid-identity",
      "urn:csabs:axiom/Monoid-closed-carrier",
      "urn:csabs:axiom/Monoid-associative",
      "urn:csabs:axiom/Monoid-identity"
    ],
    "assumptions": [
      "Use the explicit mathematical bases and typed carriers of the linked concepts."
    ],
    "provenanceStatus": "legacy-source-missing",
    "leanFormulation": "∀ {A : Type u} [Catalog.Monoid A] (e e' : A), ((∀ x, e * x = x) ∧ (∀ x, x * e = x)) → ((∀ x, e' * x = x) ∧ (∀ x, x * e' = x)) → e = e'",
    "formulationSource": "urn:csabs:source/local-lean-Witnesses",
    "formulationLocator": "Catalog.Proofs.monoid_identity_unique",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Mathlib Monoid; one gives nonemptiness, mul_assoc and both identity equations.",
    "leanModelLimitations": "Witness proves the explicit expectedType under its binders. Correspondence to the informal statement is reviewed metadata, not mechanically proved. Original citation gaps remain disclosed in the catalog.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/Monoid-associative\": \"Explicit interface premise: (x·y)·z=x·(y·z); interpreted by Catalog.Monoid. See the carrier/operation mapping; closure is enforced by typed operations and axioms are hypotheses carried by these structures, not new Lean axiom declarations.\", \"urn:csabs:axiom/Monoid-closed-carrier\": \"Explicit interface premise: S≠∅; ·:S×S→S; interpreted by Catalog.Monoid. See the carrier/operation mapping; closure is enforced by typed operations and axioms are hypotheses carried by these structures, not new Lean axiom declarations.\", \"urn:csabs:axiom/Monoid-identity\": \"Explicit interface premise: e∈S; e·x=x; x·e=x; interpreted by Catalog.Monoid. See the carrier/operation mapping; closure is enforced by typed operations and axioms are hypotheses carried by these structures, not new Lean axiom declarations.\", \"urn:csabs:axiom/monoid-identity\": \"Explicit interface premise: ∃e∈M ∀x∈M: e·x=x·e=x; interpreted by Catalog.Monoid. See the carrier/operation mapping; closure is enforced by typed operations and axioms are hypotheses carried by these structures, not new Lean axiom declarations.\"}"
  },
  {
    "id": "urn:csabs:theorem/Monoid-power-addition",
    "type": "Theorem",
    "name": "power-addition",
    "statement": "Natural powers turn exponent addition into multiplication.",
    "formalStatement": "x^0=e; x^(n+1)=x^n·x; x^(m+n)=x^m·x^n",
    "proofSketch": "Induct on n, using identity for zero and associativity in the successor case.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for Monoid apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/Monoid"
    ],
    "dependsOn": [
      "urn:csabs:axiom/monoid-identity",
      "urn:csabs:axiom/Monoid-closed-carrier",
      "urn:csabs:axiom/Monoid-associative",
      "urn:csabs:axiom/Monoid-identity"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing",
    "leanFormulation": "∀ {A : Type u} [Catalog.Monoid A] (a : A) (m n : Nat), a ^ 0 = 1 ∧ a ^ (n + 1) = a ^ n * a ∧ a ^ (m + n) = a ^ m * a ^ n",
    "formulationSource": "urn:csabs:source/local-lean-Witnesses",
    "formulationLocator": "Catalog.Proofs.monoid_power_addition",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Mathlib Monoid; one gives nonemptiness, mul_assoc and both identity equations.",
    "leanModelLimitations": "Witness proves the explicit expectedType under its binders. Correspondence to the informal statement is reviewed metadata, not mechanically proved. Original citation gaps remain disclosed in the catalog.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/Monoid-associative\": \"Explicit interface premise: (x·y)·z=x·(y·z); interpreted by Catalog.Monoid. See the carrier/operation mapping; closure is enforced by typed operations and axioms are hypotheses carried by these structures, not new Lean axiom declarations.\", \"urn:csabs:axiom/Monoid-closed-carrier\": \"Explicit interface premise: S≠∅; ·:S×S→S; interpreted by Catalog.Monoid. See the carrier/operation mapping; closure is enforced by typed operations and axioms are hypotheses carried by these structures, not new Lean axiom declarations.\", \"urn:csabs:axiom/Monoid-identity\": \"Explicit interface premise: e∈S; e·x=x; x·e=x; interpreted by Catalog.Monoid. See the carrier/operation mapping; closure is enforced by typed operations and axioms are hypotheses carried by these structures, not new Lean axiom declarations.\", \"urn:csabs:axiom/monoid-identity\": \"Explicit interface premise: ∃e∈M ∀x∈M: e·x=x·e=x; interpreted by Catalog.Monoid. See the carrier/operation mapping; closure is enforced by typed operations and axioms are hypotheses carried by these structures, not new Lean axiom declarations.\"}"
  }
]
```
<!-- graph-record:end -->
