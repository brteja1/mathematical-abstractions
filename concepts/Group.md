# Group

A monoid in which every element has a two-sided inverse.

**Notation:** (G,·,e), ∀x∈G ∃x⁻¹∈G: x·x⁻¹=x⁻¹·x=e.

**Stable ID:** `urn:csabs:concept/Group`

**Categories:** Algebra

**Kind:** Mathematical structure

**Prerequisites:** [Monoid](Monoid.md)

**Specializes:** [Monoid](Monoid.md)

## Backlinks

- [Diffie–Hellman key exchange (prime-order cyclic-group core)](DiffieHellman.md) — `requiresConcept`
- [Elliptic curve cryptography group (prime-field short-Weierstrass profile)](ECC.md) — `requiresConcept`
- [Elliptic curve cryptography group (prime-field short-Weierstrass profile)](ECC.md) — `specializationOf`
- [Euclidean lattice (discrete integer-span lattice)](EuclideanLattice.md) — `requiresConcept`
- [Euclidean lattice (discrete integer-span lattice)](EuclideanLattice.md) — `specializationOf`
- [Finite field (Galois field)](FiniteField.md) — `relatedConcept`
- [Vector space over a field](VectorSpace.md) — `requiresConcept`
- [Vector space over a field](VectorSpace.md) — `specializationOf`

## Mathematical formulation

A group is (G,·,1,inv) with associative multiplication, two-sided identity and ∀g, inv(g)·g=1=g·inv(g). Commutativity is not assumed; inverses are total.

**Lean formulation** (in its source module context):

```lean
abbrev Group (A : Type u) := _root_.Group A
```

**Source:** [`Catalog.Group`](../lean/Catalog/Algebra.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Mathlib Group; chosen inverse, associativity and two-sided unit/inverse equations. Nonempty follows from one.

**Limits:** Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Nonempty carrier with closed binary multiplication; associativity; two-sided identity; two-sided inverses. Multiplication need not commute.

**basisKind:** axiomatic-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**convention:**  Equality is equality of carrier elements; operations are exact. The empty carrier is excluded by the named constants.

**specializationNote:** Forget the inverse operation and retain the same carrier, multiplication and identity to obtain a Monoid. The one-element group is permitted; commutativity is not required.

**verificationObligation:** Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-group-product"></a>

### group operation

`urn:csabs:operation/group-product`

**signature:** · : G×G→G

**description:** Combines group elements.

**precondition:** Inputs belong to the stated carrier.

**definedness:** Total on the stated domain; exact algebraic arithmetic without rounding or overflow.

<a id="node-urn-csabs-operation-group-inverse"></a>

### inverse

`urn:csabs:operation/group-inverse`

**signature:** inv : G→G

**description:** Maps each element to its unique two-sided inverse.

**precondition:** Inputs belong to the stated carrier.

**definedness:** Total on the stated domain; exact algebraic arithmetic without rounding or overflow.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-group-inverses"></a>

### group-inverses

`urn:csabs:axiom/group-inverses`

**statement:** Every element has a two-sided inverse relative to the identity.

**formalStatement:** ∀x∈G ∃y∈G: x·y=y·x=e

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

**assumptions:** Use the linked concept’s explicit basis and carrier conventions.

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Group-closed-carrier"></a>

### closed-carrier

`urn:csabs:axiom/Group-closed-carrier`

**statement:** The binary operation is total on a nonempty carrier.

**formalStatement:** S≠∅; ·:S×S→S

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Group-associative"></a>

### associative

`urn:csabs:axiom/Group-associative`

**statement:** Multiplication is associative.

**formalStatement:** (x·y)·z=x·(y·z)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Group-identity"></a>

### identity

`urn:csabs:axiom/Group-identity`

**statement:** The identity is a two-sided unit.

**formalStatement:** e∈S; e·x=x; x·e=x

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Group-inverse"></a>

### inverse

`urn:csabs:axiom/Group-inverse`

**statement:** Every element has a two-sided inverse.

**formalStatement:** inv:S→S; inv(x)·x=e; x·inv(x)=e

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

<a id="node-urn-csabs-law-group-cancellation"></a>

### law/group-cancellation

`urn:csabs:law/group-cancellation`

**statement:** Group multiplication satisfies left and right cancellation.

**formalStatement:** ax=ay⇒x=y; xa=ya⇒x=y

**reviewStatus:** editorial-summary; not machine-proved

**proofSketch:** Multiply a common left factor by its inverse on the left, or a common right factor by its inverse on the right; use associativity and identity.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [group-inverses](Group.md#node-urn-csabs-axiom-group-inverses); [closed-carrier](Group.md#node-urn-csabs-axiom-Group-closed-carrier); [associative](Group.md#node-urn-csabs-axiom-Group-associative); [identity](Group.md#node-urn-csabs-axiom-Group-identity); [inverse](Group.md#node-urn-csabs-axiom-Group-inverse)

**assumptions:** Use the explicit mathematical bases and typed carriers of the linked concepts.

**provenanceStatus:** legacy-source-missing

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {A : Type u} [Catalog.Group A] (a x y : A), (a * x = a * y → x = y) ∧ (x * a = y * a → x = y)
```

**Source:** [`Catalog.Proofs.group_cancellation`](../lean/Catalog/Witnesses.lean); consulted 2026-11-12.

**Scope:** registered-witness-type

**Interpretation:** Mathlib Group; chosen inverse, associativity and two-sided unit/inverse equations. Nonempty follows from one.

**Limits:** Witness proves the explicit expectedType under its binders. Correspondence to the informal statement is reviewed metadata, not mechanically proved. Original citation gaps remain disclosed in the catalog.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/Group-associative": "Explicit interface premise: (x·y)·z=x·(y·z); interpreted by Catalog.Group. See the carrier/operation mapping; closure is enforced by typed operations and axioms are hypotheses carried by these structures, not new Lean axiom declarations.",
  "urn:csabs:axiom/Group-closed-carrier": "Explicit interface premise: S≠∅; ·:S×S→S; interpreted by Catalog.Group. See the carrier/operation mapping; closure is enforced by typed operations and axioms are hypotheses carried by these structures, not new Lean axiom declarations.",
  "urn:csabs:axiom/Group-identity": "Explicit interface premise: e∈S; e·x=x; x·e=x; interpreted by Catalog.Group. See the carrier/operation mapping; closure is enforced by typed operations and axioms are hypotheses carried by these structures, not new Lean axiom declarations.",
  "urn:csabs:axiom/Group-inverse": "Explicit interface premise: inv:S→S; inv(x)·x=e; x·inv(x)=e; interpreted by Catalog.Group. See the carrier/operation mapping; closure is enforced by typed operations and axioms are hypotheses carried by these structures, not new Lean axiom declarations.",
  "urn:csabs:axiom/group-inverses": "Explicit interface premise: ∀x∈G ∃y∈G: x·y=y·x=e; interpreted by Catalog.Group. See the carrier/operation mapping; closure is enforced by typed operations and axioms are hypotheses carried by these structures, not new Lean axiom declarations."
}
```

## Theorems

<a id="node-urn-csabs-theorem-lagrange"></a>

### theorem/lagrange

`urn:csabs:theorem/lagrange`

**statement:** The order of a subgroup divides the order of a finite group.

**formalStatement:** H≤G, |G|<∞ ⇒ |H| divides |G|

**assumptions:** G finite group; H subgroup

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [group-inverses](Group.md#node-urn-csabs-axiom-group-inverses); [closed-carrier](Group.md#node-urn-csabs-axiom-Group-closed-carrier); [associative](Group.md#node-urn-csabs-axiom-Group-associative); [identity](Group.md#node-urn-csabs-axiom-Group-identity); [inverse](Group.md#node-urn-csabs-axiom-Group-inverse)

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-theorem-Group-inverse-product"></a>

### inverse-product

`urn:csabs:theorem/Group-inverse-product`

**statement:** The inverse of a product reverses the factor order.

**formalStatement:** (xy)⁻¹=y⁻¹x⁻¹

**proofSketch:** Multiply xy by y⁻¹x⁻¹ on both sides and simplify; inverses are unique.

**assumptions:** The explicit basis, carriers, and side conditions stated for Group apply.

**dependsOn:** [group-inverses](Group.md#node-urn-csabs-axiom-group-inverses); [closed-carrier](Group.md#node-urn-csabs-axiom-Group-closed-carrier); [associative](Group.md#node-urn-csabs-axiom-Group-associative); [identity](Group.md#node-urn-csabs-axiom-Group-identity); [inverse](Group.md#node-urn-csabs-axiom-Group-inverse)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {A : Type u} [Catalog.Group A] (a b : A), (a * b)⁻¹ = b⁻¹ * a⁻¹
```

**Source:** [`Catalog.Proofs.group_inverse_product`](../lean/Catalog/Witnesses.lean); consulted 2026-11-12.

**Scope:** registered-witness-type

**Interpretation:** Mathlib Group; chosen inverse, associativity and two-sided unit/inverse equations. Nonempty follows from one.

**Limits:** Witness proves the explicit expectedType under its binders. Correspondence to the informal statement is reviewed metadata, not mechanically proved. Original citation gaps remain disclosed in the catalog.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/Group-associative": "Explicit interface premise: (x·y)·z=x·(y·z); interpreted by Catalog.Group. See the carrier/operation mapping; closure is enforced by typed operations and axioms are hypotheses carried by these structures, not new Lean axiom declarations.",
  "urn:csabs:axiom/Group-closed-carrier": "Explicit interface premise: S≠∅; ·:S×S→S; interpreted by Catalog.Group. See the carrier/operation mapping; closure is enforced by typed operations and axioms are hypotheses carried by these structures, not new Lean axiom declarations.",
  "urn:csabs:axiom/Group-identity": "Explicit interface premise: e∈S; e·x=x; x·e=x; interpreted by Catalog.Group. See the carrier/operation mapping; closure is enforced by typed operations and axioms are hypotheses carried by these structures, not new Lean axiom declarations.",
  "urn:csabs:axiom/Group-inverse": "Explicit interface premise: inv:S→S; inv(x)·x=e; x·inv(x)=e; interpreted by Catalog.Group. See the carrier/operation mapping; closure is enforced by typed operations and axioms are hypotheses carried by these structures, not new Lean axiom declarations.",
  "urn:csabs:axiom/group-inverses": "Explicit interface premise: ∀x∈G ∃y∈G: x·y=y·x=e; interpreted by Catalog.Group. See the carrier/operation mapping; closure is enforced by typed operations and axioms are hypotheses carried by these structures, not new Lean axiom declarations."
}
```

## Concept provenance

- [Mathlib group definitions](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Defs.html); sourceRole: reference-for-selected-basis
- [Mathlib: group definitions (consulted 2026-11-08)](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Defs.html); accessedOn: 2026-11-08; sourceRole: reference-for-selected-basis

**sourceLocator:** Group: one, mul, mul_assoc, one_mul, mul_one, inv, inv_mul_cancel; mul_inv_cancel

**sourceNote:** Selected algebraic interface; retain catalog conventions and stable identity.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/Group",
    "type": "Concept",
    "shortForm": "Group",
    "fullName": "Group",
    "category": [
      "urn:csabs:category/algebra"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "A monoid in which every element has a two-sided inverse.",
    "notation": "(G,·,e), ∀x∈G ∃x⁻¹∈G: x·x⁻¹=x⁻¹·x=e.",
    "hasOperation": [
      "urn:csabs:operation/group-product",
      "urn:csabs:operation/group-inverse"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/group-inverses",
      "urn:csabs:axiom/Group-closed-carrier",
      "urn:csabs:axiom/Group-associative",
      "urn:csabs:axiom/Group-identity",
      "urn:csabs:axiom/Group-inverse"
    ],
    "hasLaw": [
      "urn:csabs:law/group-cancellation"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/lagrange",
      "urn:csabs:theorem/Group-inverse-product"
    ],
    "specializationOf": [
      "urn:csabs:concept/Monoid"
    ],
    "coverageStatus": "basis-reviewed",
    "requiresConcept": [
      "urn:csabs:concept/Monoid"
    ],
    "verificationObligation": [
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Nonempty carrier with closed binary multiplication; associativity; two-sided identity; two-sided inverses. Multiplication need not commute.",
    "basisKind": "axiomatic-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "source": [
      "urn:csabs:source/mathlib-group",
      "urn:csabs:source/mathlib-group-defs-2026-11-08"
    ],
    "sourceLocator": "Group: one, mul, mul_assoc, one_mul, mul_one, inv, inv_mul_cancel; mul_inv_cancel",
    "sourceNote": "Selected algebraic interface; retain catalog conventions and stable identity.",
    "provenanceKind": "adapted",
    "convention": " Equality is equality of carrier elements; operations are exact. The empty carrier is excluded by the named constants.",
    "specializationNote": "Forget the inverse operation and retain the same carrier, multiplication and identity to obtain a Monoid. The one-element group is permitted; commutativity is not required.",
    "leanFormulation": "abbrev Group (A : Type u) := _root_.Group A",
    "formulationSource": "urn:csabs:source/local-lean-Algebra",
    "formulationLocator": "Catalog.Group",
    "formulationScope": "model",
    "leanModelMapping": "Mathlib Group; chosen inverse, associativity and two-sided unit/inverse equations. Nonempty follows from one.",
    "leanModelLimitations": "Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.",
    "mathematicalFormulation": "A group is (G,·,1,inv) with associative multiplication, two-sided identity and ∀g, inv(g)·g=1=g·inv(g). Commutativity is not assumed; inverses are total."
  },
  {
    "id": "urn:csabs:operation/group-product",
    "type": "Operation",
    "name": "group operation",
    "signature": "· : G×G→G",
    "description": "Combines group elements.",
    "concept": "urn:csabs:concept/Group",
    "precondition": "Inputs belong to the stated carrier.",
    "definedness": "Total on the stated domain; exact algebraic arithmetic without rounding or overflow."
  },
  {
    "id": "urn:csabs:operation/group-inverse",
    "type": "Operation",
    "name": "inverse",
    "signature": "inv : G→G",
    "description": "Maps each element to its unique two-sided inverse.",
    "concept": "urn:csabs:concept/Group",
    "precondition": "Inputs belong to the stated carrier.",
    "definedness": "Total on the stated domain; exact algebraic arithmetic without rounding or overflow."
  },
  {
    "id": "urn:csabs:axiom/group-inverses",
    "type": "Axiom",
    "statement": "Every element has a two-sided inverse relative to the identity.",
    "formalStatement": "∀x∈G ∃y∈G: x·y=y·x=e",
    "appliesTo": [
      "urn:csabs:concept/Group"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law",
    "name": "group-inverses",
    "assumptions": [
      "Use the linked concept’s explicit basis and carrier conventions."
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/Group-closed-carrier",
    "type": "Axiom",
    "name": "closed-carrier",
    "statement": "The binary operation is total on a nonempty carrier.",
    "formalStatement": "S≠∅; ·:S×S→S",
    "appliesTo": [
      "urn:csabs:concept/Group"
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
    "id": "urn:csabs:axiom/Group-associative",
    "type": "Axiom",
    "name": "associative",
    "statement": "Multiplication is associative.",
    "formalStatement": "(x·y)·z=x·(y·z)",
    "appliesTo": [
      "urn:csabs:concept/Group"
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
    "id": "urn:csabs:axiom/Group-identity",
    "type": "Axiom",
    "name": "identity",
    "statement": "The identity is a two-sided unit.",
    "formalStatement": "e∈S; e·x=x; x·e=x",
    "appliesTo": [
      "urn:csabs:concept/Group"
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
    "id": "urn:csabs:axiom/Group-inverse",
    "type": "Axiom",
    "name": "inverse",
    "statement": "Every element has a two-sided inverse.",
    "formalStatement": "inv:S→S; inv(x)·x=e; x·inv(x)=e",
    "appliesTo": [
      "urn:csabs:concept/Group"
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
    "id": "urn:csabs:law/group-cancellation",
    "type": "Law",
    "statement": "Group multiplication satisfies left and right cancellation.",
    "formalStatement": "ax=ay⇒x=y; xa=ya⇒x=y",
    "appliesTo": [
      "urn:csabs:concept/Group"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "proofSketch": "Multiply a common left factor by its inverse on the left, or a common right factor by its inverse on the right; use associativity and identity.",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/group-inverses",
      "urn:csabs:axiom/Group-closed-carrier",
      "urn:csabs:axiom/Group-associative",
      "urn:csabs:axiom/Group-identity",
      "urn:csabs:axiom/Group-inverse"
    ],
    "assumptions": [
      "Use the explicit mathematical bases and typed carriers of the linked concepts."
    ],
    "provenanceStatus": "legacy-source-missing",
    "leanFormulation": "∀ {A : Type u} [Catalog.Group A] (a x y : A), (a * x = a * y → x = y) ∧ (x * a = y * a → x = y)",
    "formulationSource": "urn:csabs:source/local-lean-Witnesses",
    "formulationLocator": "Catalog.Proofs.group_cancellation",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Mathlib Group; chosen inverse, associativity and two-sided unit/inverse equations. Nonempty follows from one.",
    "leanModelLimitations": "Witness proves the explicit expectedType under its binders. Correspondence to the informal statement is reviewed metadata, not mechanically proved. Original citation gaps remain disclosed in the catalog.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/Group-associative\": \"Explicit interface premise: (x·y)·z=x·(y·z); interpreted by Catalog.Group. See the carrier/operation mapping; closure is enforced by typed operations and axioms are hypotheses carried by these structures, not new Lean axiom declarations.\", \"urn:csabs:axiom/Group-closed-carrier\": \"Explicit interface premise: S≠∅; ·:S×S→S; interpreted by Catalog.Group. See the carrier/operation mapping; closure is enforced by typed operations and axioms are hypotheses carried by these structures, not new Lean axiom declarations.\", \"urn:csabs:axiom/Group-identity\": \"Explicit interface premise: e∈S; e·x=x; x·e=x; interpreted by Catalog.Group. See the carrier/operation mapping; closure is enforced by typed operations and axioms are hypotheses carried by these structures, not new Lean axiom declarations.\", \"urn:csabs:axiom/Group-inverse\": \"Explicit interface premise: inv:S→S; inv(x)·x=e; x·inv(x)=e; interpreted by Catalog.Group. See the carrier/operation mapping; closure is enforced by typed operations and axioms are hypotheses carried by these structures, not new Lean axiom declarations.\", \"urn:csabs:axiom/group-inverses\": \"Explicit interface premise: ∀x∈G ∃y∈G: x·y=y·x=e; interpreted by Catalog.Group. See the carrier/operation mapping; closure is enforced by typed operations and axioms are hypotheses carried by these structures, not new Lean axiom declarations.\"}"
  },
  {
    "id": "urn:csabs:theorem/lagrange",
    "type": "Theorem",
    "statement": "The order of a subgroup divides the order of a finite group.",
    "formalStatement": "H≤G, |G|<∞ ⇒ |H| divides |G|",
    "assumptions": [
      "G finite group",
      "H subgroup"
    ],
    "appliesTo": [
      "urn:csabs:concept/Group"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/group-inverses",
      "urn:csabs:axiom/Group-closed-carrier",
      "urn:csabs:axiom/Group-associative",
      "urn:csabs:axiom/Group-identity",
      "urn:csabs:axiom/Group-inverse"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/Group-inverse-product",
    "type": "Theorem",
    "name": "inverse-product",
    "statement": "The inverse of a product reverses the factor order.",
    "formalStatement": "(xy)⁻¹=y⁻¹x⁻¹",
    "proofSketch": "Multiply xy by y⁻¹x⁻¹ on both sides and simplify; inverses are unique.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for Group apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/Group"
    ],
    "dependsOn": [
      "urn:csabs:axiom/group-inverses",
      "urn:csabs:axiom/Group-closed-carrier",
      "urn:csabs:axiom/Group-associative",
      "urn:csabs:axiom/Group-identity",
      "urn:csabs:axiom/Group-inverse"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing",
    "leanFormulation": "∀ {A : Type u} [Catalog.Group A] (a b : A), (a * b)⁻¹ = b⁻¹ * a⁻¹",
    "formulationSource": "urn:csabs:source/local-lean-Witnesses",
    "formulationLocator": "Catalog.Proofs.group_inverse_product",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Mathlib Group; chosen inverse, associativity and two-sided unit/inverse equations. Nonempty follows from one.",
    "leanModelLimitations": "Witness proves the explicit expectedType under its binders. Correspondence to the informal statement is reviewed metadata, not mechanically proved. Original citation gaps remain disclosed in the catalog.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/Group-associative\": \"Explicit interface premise: (x·y)·z=x·(y·z); interpreted by Catalog.Group. See the carrier/operation mapping; closure is enforced by typed operations and axioms are hypotheses carried by these structures, not new Lean axiom declarations.\", \"urn:csabs:axiom/Group-closed-carrier\": \"Explicit interface premise: S≠∅; ·:S×S→S; interpreted by Catalog.Group. See the carrier/operation mapping; closure is enforced by typed operations and axioms are hypotheses carried by these structures, not new Lean axiom declarations.\", \"urn:csabs:axiom/Group-identity\": \"Explicit interface premise: e∈S; e·x=x; x·e=x; interpreted by Catalog.Group. See the carrier/operation mapping; closure is enforced by typed operations and axioms are hypotheses carried by these structures, not new Lean axiom declarations.\", \"urn:csabs:axiom/Group-inverse\": \"Explicit interface premise: inv:S→S; inv(x)·x=e; x·inv(x)=e; interpreted by Catalog.Group. See the carrier/operation mapping; closure is enforced by typed operations and axioms are hypotheses carried by these structures, not new Lean axiom declarations.\", \"urn:csabs:axiom/group-inverses\": \"Explicit interface premise: ∀x∈G ∃y∈G: x·y=y·x=e; interpreted by Catalog.Group. See the carrier/operation mapping; closure is enforced by typed operations and axioms are hypotheses carried by these structures, not new Lean axiom declarations.\"}"
  }
]
```
<!-- graph-record:end -->
