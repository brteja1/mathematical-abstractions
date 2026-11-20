# Join semilattice

A partially ordered carrier with a least upper bound for each pair.

**Notation:** (S,≤,⊔)

**Stable ID:** `urn:csabs:concept/JoinSemilattice`

**Categories:** Order and fixed points

**Kind:** Mathematical structure

**Prerequisites:** [Partial Order](PartialOrder.md)

**Specializes:** [Partial Order](PartialOrder.md)

## Backlinks

- [Sound abstract transfer and inductive dataflow facts](AbstractInterpretation.md) — `requiresConcept`
- [Program side-effect algebra (total sequential effect-quantale profile)](EffectAlgebra.md) — `requiresConcept`
- [Program side-effect algebra (total sequential effect-quantale profile)](EffectAlgebra.md) — `specializationOf`
- [Idempotent semiring (additively idempotent, unital)](IdempotentSemiring.md) — `relatedConcept`
- [Lattice](Lattice.md) — `specializationOf`
- [Min-plus semiring (tropical semiring, min convention)](MinPlusSemiring.md) — `relatedConcept`
- [State-based CRDT replication algebra](StateBasedCRDT.md) — `requiresConcept`

## Mathematical formulation

A join semilattice is a partial order with x⊔y the least upper bound of x,y: x≤x⊔y, y≤x⊔y, and x≤z∧y≤z⇒x⊔y≤z. No bottom is required by this carrier. Utility profile: Optional least element ⊥ satisfying ∀a,⊥≤a. Not required by the base JoinSemilattice and not inferred from finite binary joins.; Fold binary join from ⊥; empty join is ⊥. Nonempty finite joins need no bottom but this total empty-capable operation does.

**Lean formulation** (in its source module context):

```lean
abbrev JoinSemilattice (A : Type u) := SemilatticeSup A
```

**Source:** [`Catalog.JoinSemilattice`](../lean/Catalog/CoreData.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** (S,≤,⊔). Binary joins only. A bottom element, meets, completeness or distributivity is additional structure. Equality is the carrier equality used by antisymmetry; empty carrier allowed.

**Limits:** Compiled carrier and selected interface interpretation. Some catalog operations are specified mathematically rather than wrapped as Lean declarations; no blanket proof of claims, algorithms, parsing, liveness or complexity. See individual witnesses.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** ≤ is reflexive, antisymmetric and transitive; x≤x⊔y ∧ y≤x⊔y; x≤z ∧ y≤z ⇒ x⊔y≤z Utility definitions are recorded separately; optional bottom, subtype and goal-relative conventions are conditional and do not strengthen the base carrier.

**basisKind:** extensional-structural-definition

**basisScope:** Binary joins only. A bottom element, meets, completeness or distributivity is additional structure. Equality is the carrier equality used by antisymmetry; empty carrier allowed.

**specializationNote:** Keep the same carrier and ≤; forget ⊔ to obtain PartialOrder. Binary joins add explicit upper-bound and leastness requirements.

**verificationObligation:** Map carrier, equality, operation definedness and stated profile to the target API or proof context.; Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.; Model coverage does not establish every recorded claim or an implementation refinement.

**reviewStatus:** Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-JoinSemilattice-order"></a>

### order

`urn:csabs:operation/JoinSemilattice-order`

**signature:** le : S×S→Prop

**description:** The given partial order.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Binary joins only. A bottom element, meets, completeness or distributivity is additional structure. Equality is the carrier equality used by antisymmetry; empty carrier allowed.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** The given partial order.

**source:** [Mathlib pinned definitions: Order/Defs/Lattice.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Order/Defs/Lattice.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** SemilatticeSup: PartialOrder, le_sup_left, le_sup_right, sup_le

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-JoinSemilattice-join"></a>

### join

`urn:csabs:operation/JoinSemilattice-join`

**signature:** join : S×S→S

**description:** Returns the least upper bound of its two operands.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Binary joins only. A bottom element, meets, completeness or distributivity is additional structure. Equality is the carrier equality used by antisymmetry; empty carrier allowed.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Returns the least upper bound of its two operands.

**source:** [Mathlib pinned definitions: Order/Defs/Lattice.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Order/Defs/Lattice.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** SemilatticeSup: PartialOrder, le_sup_left, le_sup_right, sup_le

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-JoinSemilattice-bottom-profile"></a>

### bottom-profile

`urn:csabs:operation/JoinSemilattice-bottom-profile`

**signature:** bottom : WithBottomJoinSemilattice(A)→A

**description:** Optional least element ⊥ satisfying ∀a,⊥≤a. Not required by the base JoinSemilattice and not inferred from finite binary joins.

**precondition:** Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.

**postcondition:** Optional least element ⊥ satisfying ∀a,⊥≤a. Not required by the base JoinSemilattice and not inferred from finite binary joins.

**totality:** Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.

**sourceLocator:** Order/Lattice.lean: sup_assoc and sup_le_iff; Order/BoundedOrder/Basic.lean: bottom; Order/Lattice/Nat.lean: Nat max/zero instance

**sourceNote:** Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-JoinSemilattice-join-all"></a>

### join-all

`urn:csabs:operation/JoinSemilattice-join-all`

**signature:** joinAll : WithBottomJoinSemilattice(A)×Seq(A)→A

**description:** Fold binary join from ⊥; empty join is ⊥. Nonempty finite joins need no bottom but this total empty-capable operation does.

**precondition:** Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.

**postcondition:** Fold binary join from ⊥; empty join is ⊥. Nonempty finite joins need no bottom but this total empty-capable operation does.

**totality:** Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.

**sourceLocator:** Order/Lattice.lean: sup_assoc and sup_le_iff; Order/BoundedOrder/Basic.lean: bottom; Order/Lattice/Nat.lean: Nat max/zero instance

**sourceNote:** Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-PartialOrder-reflexive"></a>

### reflexive

`urn:csabs:axiom/PartialOrder-reflexive`

**statement:** The order is reflexive.

**formalStatement:** ∀x∈A:x≤x

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-PartialOrder-transitive"></a>

### transitive

`urn:csabs:axiom/PartialOrder-transitive`

**statement:** The order is transitive.

**formalStatement:** x≤y ∧ y≤z ⇒ x≤z

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-PartialOrder-antisymmetric"></a>

### antisymmetric

`urn:csabs:axiom/PartialOrder-antisymmetric`

**statement:** Mutual ordering implies equality.

**formalStatement:** x≤y ∧ y≤x ⇒ x=y

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-JoinSemilattice-upper-bounds"></a>

### upper-bounds

`urn:csabs:axiom/JoinSemilattice-upper-bounds`

**statement:** Defining requirement: x≤x⊔y ∧ y≤x⊔y

**formalStatement:** x≤x⊔y ∧ y≤x⊔y

**assumptions:** Binary joins only. A bottom element, meets, completeness or distributivity is additional structure. Equality is the carrier equality used by antisymmetry; empty carrier allowed.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Mathlib pinned definitions: Order/Defs/Lattice.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Order/Defs/Lattice.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** SemilatticeSup: PartialOrder, le_sup_left, le_sup_right, sup_le

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-JoinSemilattice-leastness"></a>

### leastness

`urn:csabs:axiom/JoinSemilattice-leastness`

**statement:** Defining requirement: x≤z ∧ y≤z ⇒ x⊔y≤z

**formalStatement:** x≤z ∧ y≤z ⇒ x⊔y≤z

**assumptions:** Binary joins only. A bottom element, meets, completeness or distributivity is additional structure. Equality is the carrier equality used by antisymmetry; empty carrier allowed.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Mathlib pinned definitions: Order/Defs/Lattice.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Order/Defs/Lattice.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** SemilatticeSup: PartialOrder, le_sup_left, le_sup_right, sup_le

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-JoinSemilattice-utility-profile"></a>

### Explicit utility operation definitions

`urn:csabs:axiom/JoinSemilattice-utility-profile`

**statement:** Optional least element ⊥ satisfying ∀a,⊥≤a. Not required by the base JoinSemilattice and not inferred from finite binary joins.; Fold binary join from ⊥; empty join is ⊥. Nonempty finite joins need no bottom but this total empty-capable operation does.

**formalStatement:** bottom : WithBottomJoinSemilattice(A)→A: Optional least element ⊥ satisfying ∀a,⊥≤a. Not required by the base JoinSemilattice and not inferred from finite binary joins.; joinAll : WithBottomJoinSemilattice(A)×Seq(A)→A: Fold binary join from ⊥; empty join is ⊥. Nonempty finite joins need no bottom but this total empty-capable operation does.

**assumptions:** Base concept conventions remain unchanged. Optional profiles apply only under their explicitly stated additional hypotheses; identity equality, finite inputs and exact mathematics.

**ruleRole:** defining-rule

**reviewStatus:** Definitions of a selected extension, not new foundational axioms; individual model and result witnesses are separate.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.

**sourceLocator:** Order/Lattice.lean: sup_assoc and sup_le_iff; Order/BoundedOrder/Basic.lean: bottom; Order/Lattice/Nat.lean: Nat max/zero instance

**sourceNote:** Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-JoinSemilattice-commutativity"></a>

### commutativity

`urn:csabs:law/JoinSemilattice-commutativity`

**statement:** x⊔y=y⊔x

**formalStatement:** x⊔y=y⊔x

**assumptions:** Binary joins only. A bottom element, meets, completeness or distributivity is additional structure. Equality is the carrier equality used by antisymmetry; empty carrier allowed.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [reflexive](PartialOrder.md#node-urn-csabs-axiom-PartialOrder-reflexive); [transitive](PartialOrder.md#node-urn-csabs-axiom-PartialOrder-transitive); [antisymmetric](PartialOrder.md#node-urn-csabs-axiom-PartialOrder-antisymmetric); [upper-bounds](JoinSemilattice.md#node-urn-csabs-axiom-JoinSemilattice-upper-bounds); [leastness](JoinSemilattice.md#node-urn-csabs-axiom-JoinSemilattice-leastness)

**proofSketch:** Each join is an upper bound for both operands; use leastness in both directions and antisymmetry.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Mathlib pinned definitions: Order/Defs/Lattice.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Order/Defs/Lattice.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** SemilatticeSup: PartialOrder, le_sup_left, le_sup_right, sup_le

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {A : Type} [Catalog.JoinSemilattice A] (x y : A), x ⊔ y = y ⊔ x
```

**Source:** [`Catalog.CoreDataProofs.join_commutative`](../lean/Catalog/CoreData.lean); consulted 2026-11-12.

**Scope:** registered-witness-type

**Interpretation:** SemilatticeSup extends PartialOrder with binary sup and le_sup_left/le_sup_right/sup_le. Sup is catalog join, ≤ and equality retain their carrier meanings. sup_comm uses those order/leastness fields.

**Limits:** Only the displayed proposition for this explicit interpretation. No proof of all catalog claims or of a software implementation; informal/formal correspondence remains reviewed metadata.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/JoinSemilattice-leastness": "Interpreted premise: x≤z ∧ y≤z ⇒ x⊔y≤z. SemilatticeSup extends PartialOrder with binary sup and le_sup_left/le_sup_right/sup_le. Sup is catalog join, ≤ and equality retain their carrier meanings. sup_comm uses those order/leastness fields.",
  "urn:csabs:axiom/JoinSemilattice-upper-bounds": "Interpreted premise: x≤x⊔y ∧ y≤x⊔y. SemilatticeSup extends PartialOrder with binary sup and le_sup_left/le_sup_right/sup_le. Sup is catalog join, ≤ and equality retain their carrier meanings. sup_comm uses those order/leastness fields.",
  "urn:csabs:axiom/PartialOrder-antisymmetric": "Interpreted premise: x≤y ∧ y≤x ⇒ x=y. SemilatticeSup extends PartialOrder with binary sup and le_sup_left/le_sup_right/sup_le. Sup is catalog join, ≤ and equality retain their carrier meanings. sup_comm uses those order/leastness fields.",
  "urn:csabs:axiom/PartialOrder-reflexive": "Interpreted premise: ∀x∈A:x≤x. SemilatticeSup extends PartialOrder with binary sup and le_sup_left/le_sup_right/sup_le. Sup is catalog join, ≤ and equality retain their carrier meanings. sup_comm uses those order/leastness fields.",
  "urn:csabs:axiom/PartialOrder-transitive": "Interpreted premise: x≤y ∧ y≤z ⇒ x≤z. SemilatticeSup extends PartialOrder with binary sup and le_sup_left/le_sup_right/sup_le. Sup is catalog join, ≤ and equality retain their carrier meanings. sup_comm uses those order/leastness fields."
}
```

<a id="node-urn-csabs-law-JoinSemilattice-associativity"></a>

### associativity

`urn:csabs:law/JoinSemilattice-associativity`

**statement:** (a∨b)∨c=a∨(b∨c).

**formalStatement:** (a∨b)∨c=a∨(b∨c).

**proofSketch:** Use the least-upper-bound order laws via sup_assoc.

**assumptions:** Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles.

**dependsOn:** [Explicit utility operation definitions](JoinSemilattice.md#node-urn-csabs-axiom-JoinSemilattice-utility-profile); [upper-bounds](JoinSemilattice.md#node-urn-csabs-axiom-JoinSemilattice-upper-bounds); [leastness](JoinSemilattice.md#node-urn-csabs-axiom-JoinSemilattice-leastness)

**reviewStatus:** Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.; Catalog CollectionUtilities Lean formulations and proofs; path: lean/Catalog/CollectionUtilities.lean; accessedOn: 2026-11-20; sourceRole: Local formulation and derived-proof evidence. Independent mathematical provenance is linked separately.

**sourceLocator:** Order/Lattice.lean: sup_assoc and sup_le_iff; Order/BoundedOrder/Basic.lean: bottom; Order/Lattice/Nat.lean: Nat max/zero instance; Catalog.join_associative

**sourceNote:** Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.

**provenanceKind:** derived

#### Mathematical formulation

(a∨b)∨c=a∨(b∨c).

**Lean formulation** (in its source module context):

```lean
∀ {A : Type u} [SemilatticeSup A] (a b c : A), (a ⊔ b) ⊔ c = a ⊔ (b ⊔ c)
```

**Source:** [`Catalog.join_associative`](../lean/Catalog/CollectionUtilities.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** (a∨b)∨c=a∨(b∨c). Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.

**Limits:** Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/JoinSemilattice-leastness": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.",
  "urn:csabs:axiom/JoinSemilattice-upper-bounds": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.",
  "urn:csabs:axiom/JoinSemilattice-utility-profile": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders."
}
```

<a id="node-urn-csabs-law-JoinSemilattice-bottom-empty-identities"></a>

### bottom-empty-identities

`urn:csabs:law/JoinSemilattice-bottom-empty-identities`

**statement:** In the optional bottom profile, ⊥∨a=a=a∨⊥ and joinAll([])=⊥.

**formalStatement:** In the optional bottom profile, ⊥∨a=a=a∨⊥ and joinAll([])=⊥.

**proofSketch:** The least-element and join laws yield the binary identities; empty fold is definitional.

**assumptions:** Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles.

**dependsOn:** [Explicit utility operation definitions](JoinSemilattice.md#node-urn-csabs-axiom-JoinSemilattice-utility-profile)

**reviewStatus:** Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.; Catalog CollectionUtilities Lean formulations and proofs; path: lean/Catalog/CollectionUtilities.lean; accessedOn: 2026-11-20; sourceRole: Local formulation and derived-proof evidence. Independent mathematical provenance is linked separately.

**sourceLocator:** Order/Lattice.lean: sup_assoc and sup_le_iff; Order/BoundedOrder/Basic.lean: bottom; Order/Lattice/Nat.lean: Nat max/zero instance; Catalog.join_bottom_laws

**sourceNote:** Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.

**provenanceKind:** derived

#### Mathematical formulation

In the optional bottom profile, ⊥∨a=a=a∨⊥ and joinAll([])=⊥.

**Lean formulation** (in its source module context):

```lean
∀ {A : Type u} [SemilatticeSup A] [OrderBot A] (a : A), ⊥ ⊔ a = a ∧ a ⊔ ⊥ = a ∧ Catalog.joinAll ([] : List A) = ⊥
```

**Source:** [`Catalog.join_bottom_laws`](../lean/Catalog/CollectionUtilities.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** In the optional bottom profile, ⊥∨a=a=a∨⊥ and joinAll([])=⊥. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.

**Limits:** Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/JoinSemilattice-utility-profile": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders."
}
```

## Theorems

<a id="node-urn-csabs-theorem-JoinSemilattice-idempotence"></a>

### idempotence

`urn:csabs:theorem/JoinSemilattice-idempotence`

**statement:** x⊔x=x

**formalStatement:** x⊔x=x

**assumptions:** Binary joins only. A bottom element, meets, completeness or distributivity is additional structure. Equality is the carrier equality used by antisymmetry; empty carrier allowed.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [reflexive](PartialOrder.md#node-urn-csabs-axiom-PartialOrder-reflexive); [transitive](PartialOrder.md#node-urn-csabs-axiom-PartialOrder-transitive); [antisymmetric](PartialOrder.md#node-urn-csabs-axiom-PartialOrder-antisymmetric); [upper-bounds](JoinSemilattice.md#node-urn-csabs-axiom-JoinSemilattice-upper-bounds); [leastness](JoinSemilattice.md#node-urn-csabs-axiom-JoinSemilattice-leastness)

**proofSketch:** The join is above x; x is an upper bound of both copies. Use leastness and antisymmetry.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Mathlib pinned definitions: Order/Defs/Lattice.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Order/Defs/Lattice.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** SemilatticeSup: PartialOrder, le_sup_left, le_sup_right, sup_le

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {A : Type} [Catalog.JoinSemilattice A] (x : A), x ⊔ x = x
```

**Source:** [`Catalog.CoreDataProofs.join_idempotent`](../lean/Catalog/CoreData.lean); consulted 2026-11-12.

**Scope:** registered-witness-type

**Interpretation:** SemilatticeSup supplies the explicitly reused partial-order rules and upper-bound/leastness fields; sup_idem derives idempotence. Join is ⊔.

**Limits:** Only the displayed proposition for this explicit interpretation. No proof of all catalog claims or of a software implementation; informal/formal correspondence remains reviewed metadata.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/JoinSemilattice-leastness": "Interpreted premise: x≤z ∧ y≤z ⇒ x⊔y≤z. SemilatticeSup supplies the explicitly reused partial-order rules and upper-bound/leastness fields; sup_idem derives idempotence. Join is ⊔.",
  "urn:csabs:axiom/JoinSemilattice-upper-bounds": "Interpreted premise: x≤x⊔y ∧ y≤x⊔y. SemilatticeSup supplies the explicitly reused partial-order rules and upper-bound/leastness fields; sup_idem derives idempotence. Join is ⊔.",
  "urn:csabs:axiom/PartialOrder-antisymmetric": "Interpreted premise: x≤y ∧ y≤x ⇒ x=y. SemilatticeSup supplies the explicitly reused partial-order rules and upper-bound/leastness fields; sup_idem derives idempotence. Join is ⊔.",
  "urn:csabs:axiom/PartialOrder-reflexive": "Interpreted premise: ∀x∈A:x≤x. SemilatticeSup supplies the explicitly reused partial-order rules and upper-bound/leastness fields; sup_idem derives idempotence. Join is ⊔.",
  "urn:csabs:axiom/PartialOrder-transitive": "Interpreted premise: x≤y ∧ y≤z ⇒ x≤z. SemilatticeSup supplies the explicitly reused partial-order rules and upper-bound/leastness fields; sup_idem derives idempotence. Join is ⊔."
}
```

<a id="node-urn-csabs-theorem-JoinSemilattice-finite-join-lub"></a>

### finite-join-lub

`urn:csabs:theorem/JoinSemilattice-finite-join-lub`

**statement:** In the bottom profile, joinAll(xs)≤z iff every member a of xs satisfies a≤z.

**formalStatement:** In the bottom profile, joinAll(xs)≤z iff every member a of xs satisfies a≤z.

**proofSketch:** Induct over xs using sup_le_iff; the empty case uses the least-element property.

**assumptions:** Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles.

**dependsOn:** [Explicit utility operation definitions](JoinSemilattice.md#node-urn-csabs-axiom-JoinSemilattice-utility-profile); [leastness](JoinSemilattice.md#node-urn-csabs-axiom-JoinSemilattice-leastness)

**reviewStatus:** Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.; Catalog CollectionUtilities Lean formulations and proofs; path: lean/Catalog/CollectionUtilities.lean; accessedOn: 2026-11-20; sourceRole: Local formulation and derived-proof evidence. Independent mathematical provenance is linked separately.

**sourceLocator:** Order/Lattice.lean: sup_assoc and sup_le_iff; Order/BoundedOrder/Basic.lean: bottom; Order/Lattice/Nat.lean: Nat max/zero instance; Catalog.joinAll_lub

**sourceNote:** Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.

**provenanceKind:** derived

#### Mathematical formulation

In the bottom profile, joinAll(xs)≤z iff every member a of xs satisfies a≤z.

**Lean formulation** (in its source module context):

```lean
∀ {A : Type u} [SemilatticeSup A] [OrderBot A]
    (xs : List A) (z : A), Catalog.joinAll xs ≤ z ↔ ∀ a ∈ xs, a ≤ z
```

**Source:** [`Catalog.joinAll_lub`](../lean/Catalog/CollectionUtilities.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** In the bottom profile, joinAll(xs)≤z iff every member a of xs satisfies a≤z. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.

**Limits:** Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/JoinSemilattice-leastness": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.",
  "urn:csabs:axiom/JoinSemilattice-utility-profile": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders."
}
```

<a id="node-urn-csabs-theorem-JoinSemilattice-bottom-model-satisfaction"></a>

### bottom-model-satisfaction

`urn:csabs:theorem/JoinSemilattice-bottom-model-satisfaction`

**statement:** The natural-number max/zero model has joinAll([])=0 and joinAll([1,3,2])=3.

**formalStatement:** The natural-number max/zero model has joinAll([])=0 and joinAll([1,3,2])=3.

**proofSketch:** Evaluate concrete Nat max and zero; the pinned Nat instance supplies a nontrivial inhabited bottom semilattice.

**assumptions:** Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles.

**dependsOn:** [Explicit utility operation definitions](JoinSemilattice.md#node-urn-csabs-axiom-JoinSemilattice-utility-profile)

**reviewStatus:** Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.; Catalog CollectionUtilities Lean formulations and proofs; path: lean/Catalog/CollectionUtilities.lean; accessedOn: 2026-11-20; sourceRole: Local formulation and derived-proof evidence. Independent mathematical provenance is linked separately.

**sourceLocator:** Order/Lattice.lean: sup_assoc and sup_le_iff; Order/BoundedOrder/Basic.lean: bottom; Order/Lattice/Nat.lean: Nat max/zero instance; Catalog.join_bottom_model

**sourceNote:** Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.

**provenanceKind:** derived

#### Mathematical formulation

The natural-number max/zero model has joinAll([])=0 and joinAll([1,3,2])=3.

**Lean formulation** (in its source module context):

```lean
Catalog.joinAll ([] : List Nat) = 0 ∧ Catalog.joinAll [1, 3, 2] = 3
```

**Source:** [`Catalog.join_bottom_model`](../lean/Catalog/CollectionUtilities.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** The natural-number max/zero model has joinAll([])=0 and joinAll([1,3,2])=3. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.

**Limits:** Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/JoinSemilattice-utility-profile": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders."
}
```

## Concept provenance

- [Mathlib pinned definitions: Order/Defs/Lattice.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Order/Defs/Lattice.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** SemilatticeSup: PartialOrder, le_sup_left, le_sup_right, sup_le

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/JoinSemilattice",
    "type": "Concept",
    "shortForm": "JoinSemilattice",
    "fullName": "Join semilattice",
    "category": [
      "urn:csabs:category/order"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "A partially ordered carrier with a least upper bound for each pair.",
    "notation": "(S,≤,⊔)",
    "requiresConcept": [
      "urn:csabs:concept/PartialOrder"
    ],
    "relatedConcept": [],
    "hasOperation": [
      "urn:csabs:operation/JoinSemilattice-order",
      "urn:csabs:operation/JoinSemilattice-join",
      "urn:csabs:operation/JoinSemilattice-bottom-profile",
      "urn:csabs:operation/JoinSemilattice-join-all"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/PartialOrder-reflexive",
      "urn:csabs:axiom/PartialOrder-transitive",
      "urn:csabs:axiom/PartialOrder-antisymmetric",
      "urn:csabs:axiom/JoinSemilattice-upper-bounds",
      "urn:csabs:axiom/JoinSemilattice-leastness",
      "urn:csabs:axiom/JoinSemilattice-utility-profile"
    ],
    "hasLaw": [
      "urn:csabs:law/JoinSemilattice-commutativity",
      "urn:csabs:law/JoinSemilattice-associativity",
      "urn:csabs:law/JoinSemilattice-bottom-empty-identities"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/JoinSemilattice-idempotence",
      "urn:csabs:theorem/JoinSemilattice-finite-join-lub",
      "urn:csabs:theorem/JoinSemilattice-bottom-model-satisfaction"
    ],
    "axiomBasis": "≤ is reflexive, antisymmetric and transitive; x≤x⊔y ∧ y≤x⊔y; x≤z ∧ y≤z ⇒ x⊔y≤z Utility definitions are recorded separately; optional bottom, subtype and goal-relative conventions are conditional and do not strengthen the base carrier.",
    "basisKind": "extensional-structural-definition",
    "basisScope": "Binary joins only. A bottom element, meets, completeness or distributivity is additional structure. Equality is the carrier equality used by antisymmetry; empty carrier allowed.",
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Map carrier, equality, operation definedness and stated profile to the target API or proof context.",
      "Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.",
      "Model coverage does not establish every recorded claim or an implementation refinement."
    ],
    "reviewStatus": "Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.",
    "source": [
      "urn:csabs:source/mathlib-join-core"
    ],
    "sourceLocator": "SemilatticeSup: PartialOrder, le_sup_left, le_sup_right, sup_le",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/PartialOrder"
    ],
    "specializationNote": "Keep the same carrier and ≤; forget ⊔ to obtain PartialOrder. Binary joins add explicit upper-bound and leastness requirements.",
    "leanFormulation": "abbrev JoinSemilattice (A : Type u) := SemilatticeSup A",
    "formulationSource": "urn:csabs:source/local-lean-CoreData",
    "formulationLocator": "Catalog.JoinSemilattice",
    "formulationScope": "model",
    "leanModelMapping": "(S,≤,⊔). Binary joins only. A bottom element, meets, completeness or distributivity is additional structure. Equality is the carrier equality used by antisymmetry; empty carrier allowed.",
    "leanModelLimitations": "Compiled carrier and selected interface interpretation. Some catalog operations are specified mathematically rather than wrapped as Lean declarations; no blanket proof of claims, algorithms, parsing, liveness or complexity. See individual witnesses.",
    "mathematicalFormulation": "A join semilattice is a partial order with x⊔y the least upper bound of x,y: x≤x⊔y, y≤x⊔y, and x≤z∧y≤z⇒x⊔y≤z. No bottom is required by this carrier. Utility profile: Optional least element ⊥ satisfying ∀a,⊥≤a. Not required by the base JoinSemilattice and not inferred from finite binary joins.; Fold binary join from ⊥; empty join is ⊥. Nonempty finite joins need no bottom but this total empty-capable operation does."
  },
  {
    "id": "urn:csabs:operation/JoinSemilattice-order",
    "type": "Operation",
    "name": "order",
    "signature": "le : S×S→Prop",
    "description": "The given partial order.",
    "concept": "urn:csabs:concept/JoinSemilattice",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Binary joins only. A bottom element, meets, completeness or distributivity is additional structure. Equality is the carrier equality used by antisymmetry; empty carrier allowed.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "The given partial order.",
    "source": [
      "urn:csabs:source/mathlib-join-core"
    ],
    "sourceLocator": "SemilatticeSup: PartialOrder, le_sup_left, le_sup_right, sup_le",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/JoinSemilattice-join",
    "type": "Operation",
    "name": "join",
    "signature": "join : S×S→S",
    "description": "Returns the least upper bound of its two operands.",
    "concept": "urn:csabs:concept/JoinSemilattice",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Binary joins only. A bottom element, meets, completeness or distributivity is additional structure. Equality is the carrier equality used by antisymmetry; empty carrier allowed.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Returns the least upper bound of its two operands.",
    "source": [
      "urn:csabs:source/mathlib-join-core"
    ],
    "sourceLocator": "SemilatticeSup: PartialOrder, le_sup_left, le_sup_right, sup_le",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/JoinSemilattice-bottom-profile",
    "type": "Operation",
    "concept": "urn:csabs:concept/JoinSemilattice",
    "name": "bottom-profile",
    "signature": "bottom : WithBottomJoinSemilattice(A)→A",
    "description": "Optional least element ⊥ satisfying ∀a,⊥≤a. Not required by the base JoinSemilattice and not inferred from finite binary joins.",
    "precondition": "Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.",
    "postcondition": "Optional least element ⊥ satisfying ∀a,⊥≤a. Not required by the base JoinSemilattice and not inferred from finite binary joins.",
    "totality": "Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned"
    ],
    "sourceLocator": "Order/Lattice.lean: sup_assoc and sup_le_iff; Order/BoundedOrder/Basic.lean: bottom; Order/Lattice/Nat.lean: Nat max/zero instance",
    "sourceNote": "Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/JoinSemilattice-join-all",
    "type": "Operation",
    "concept": "urn:csabs:concept/JoinSemilattice",
    "name": "join-all",
    "signature": "joinAll : WithBottomJoinSemilattice(A)×Seq(A)→A",
    "description": "Fold binary join from ⊥; empty join is ⊥. Nonempty finite joins need no bottom but this total empty-capable operation does.",
    "precondition": "Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.",
    "postcondition": "Fold binary join from ⊥; empty join is ⊥. Nonempty finite joins need no bottom but this total empty-capable operation does.",
    "totality": "Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned"
    ],
    "sourceLocator": "Order/Lattice.lean: sup_assoc and sup_le_iff; Order/BoundedOrder/Basic.lean: bottom; Order/Lattice/Nat.lean: Nat max/zero instance",
    "sourceNote": "Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/PartialOrder-reflexive",
    "type": "Axiom",
    "name": "reflexive",
    "statement": "The order is reflexive.",
    "formalStatement": "∀x∈A:x≤x",
    "appliesTo": [
      "urn:csabs:concept/PartialOrder",
      "urn:csabs:concept/JoinSemilattice"
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
    "id": "urn:csabs:axiom/PartialOrder-transitive",
    "type": "Axiom",
    "name": "transitive",
    "statement": "The order is transitive.",
    "formalStatement": "x≤y ∧ y≤z ⇒ x≤z",
    "appliesTo": [
      "urn:csabs:concept/PartialOrder",
      "urn:csabs:concept/JoinSemilattice"
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
    "id": "urn:csabs:axiom/PartialOrder-antisymmetric",
    "type": "Axiom",
    "name": "antisymmetric",
    "statement": "Mutual ordering implies equality.",
    "formalStatement": "x≤y ∧ y≤x ⇒ x=y",
    "appliesTo": [
      "urn:csabs:concept/PartialOrder",
      "urn:csabs:concept/JoinSemilattice"
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
    "id": "urn:csabs:axiom/JoinSemilattice-upper-bounds",
    "type": "Axiom",
    "name": "upper-bounds",
    "statement": "Defining requirement: x≤x⊔y ∧ y≤x⊔y",
    "formalStatement": "x≤x⊔y ∧ y≤x⊔y",
    "assumptions": [
      "Binary joins only. A bottom element, meets, completeness or distributivity is additional structure. Equality is the carrier equality used by antisymmetry; empty carrier allowed.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/JoinSemilattice"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/mathlib-join-core"
    ],
    "sourceLocator": "SemilatticeSup: PartialOrder, le_sup_left, le_sup_right, sup_le",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/JoinSemilattice-leastness",
    "type": "Axiom",
    "name": "leastness",
    "statement": "Defining requirement: x≤z ∧ y≤z ⇒ x⊔y≤z",
    "formalStatement": "x≤z ∧ y≤z ⇒ x⊔y≤z",
    "assumptions": [
      "Binary joins only. A bottom element, meets, completeness or distributivity is additional structure. Equality is the carrier equality used by antisymmetry; empty carrier allowed.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/JoinSemilattice"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/mathlib-join-core"
    ],
    "sourceLocator": "SemilatticeSup: PartialOrder, le_sup_left, le_sup_right, sup_le",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/JoinSemilattice-utility-profile",
    "type": "Axiom",
    "name": "Explicit utility operation definitions",
    "statement": "Optional least element ⊥ satisfying ∀a,⊥≤a. Not required by the base JoinSemilattice and not inferred from finite binary joins.; Fold binary join from ⊥; empty join is ⊥. Nonempty finite joins need no bottom but this total empty-capable operation does.",
    "formalStatement": "bottom : WithBottomJoinSemilattice(A)→A: Optional least element ⊥ satisfying ∀a,⊥≤a. Not required by the base JoinSemilattice and not inferred from finite binary joins.; joinAll : WithBottomJoinSemilattice(A)×Seq(A)→A: Fold binary join from ⊥; empty join is ⊥. Nonempty finite joins need no bottom but this total empty-capable operation does.",
    "assumptions": [
      "Base concept conventions remain unchanged. Optional profiles apply only under their explicitly stated additional hypotheses; identity equality, finite inputs and exact mathematics."
    ],
    "appliesTo": [
      "urn:csabs:concept/JoinSemilattice"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Definitions of a selected extension, not new foundational axioms; individual model and result witnesses are separate.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned"
    ],
    "sourceLocator": "Order/Lattice.lean: sup_assoc and sup_le_iff; Order/BoundedOrder/Basic.lean: bottom; Order/Lattice/Nat.lean: Nat max/zero instance",
    "sourceNote": "Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/JoinSemilattice-commutativity",
    "type": "Law",
    "name": "commutativity",
    "statement": "x⊔y=y⊔x",
    "formalStatement": "x⊔y=y⊔x",
    "assumptions": [
      "Binary joins only. A bottom element, meets, completeness or distributivity is additional structure. Equality is the carrier equality used by antisymmetry; empty carrier allowed.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/JoinSemilattice"
    ],
    "dependsOn": [
      "urn:csabs:axiom/PartialOrder-reflexive",
      "urn:csabs:axiom/PartialOrder-transitive",
      "urn:csabs:axiom/PartialOrder-antisymmetric",
      "urn:csabs:axiom/JoinSemilattice-upper-bounds",
      "urn:csabs:axiom/JoinSemilattice-leastness"
    ],
    "proofSketch": "Each join is an upper bound for both operands; use leastness in both directions and antisymmetry.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/mathlib-join-core"
    ],
    "sourceLocator": "SemilatticeSup: PartialOrder, le_sup_left, le_sup_right, sup_le",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {A : Type} [Catalog.JoinSemilattice A] (x y : A), x ⊔ y = y ⊔ x",
    "formulationSource": "urn:csabs:source/local-lean-CoreData",
    "formulationLocator": "Catalog.CoreDataProofs.join_commutative",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "SemilatticeSup extends PartialOrder with binary sup and le_sup_left/le_sup_right/sup_le. Sup is catalog join, ≤ and equality retain their carrier meanings. sup_comm uses those order/leastness fields.",
    "leanModelLimitations": "Only the displayed proposition for this explicit interpretation. No proof of all catalog claims or of a software implementation; informal/formal correspondence remains reviewed metadata.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/JoinSemilattice-leastness\": \"Interpreted premise: x≤z ∧ y≤z ⇒ x⊔y≤z. SemilatticeSup extends PartialOrder with binary sup and le_sup_left/le_sup_right/sup_le. Sup is catalog join, ≤ and equality retain their carrier meanings. sup_comm uses those order/leastness fields.\", \"urn:csabs:axiom/JoinSemilattice-upper-bounds\": \"Interpreted premise: x≤x⊔y ∧ y≤x⊔y. SemilatticeSup extends PartialOrder with binary sup and le_sup_left/le_sup_right/sup_le. Sup is catalog join, ≤ and equality retain their carrier meanings. sup_comm uses those order/leastness fields.\", \"urn:csabs:axiom/PartialOrder-antisymmetric\": \"Interpreted premise: x≤y ∧ y≤x ⇒ x=y. SemilatticeSup extends PartialOrder with binary sup and le_sup_left/le_sup_right/sup_le. Sup is catalog join, ≤ and equality retain their carrier meanings. sup_comm uses those order/leastness fields.\", \"urn:csabs:axiom/PartialOrder-reflexive\": \"Interpreted premise: ∀x∈A:x≤x. SemilatticeSup extends PartialOrder with binary sup and le_sup_left/le_sup_right/sup_le. Sup is catalog join, ≤ and equality retain their carrier meanings. sup_comm uses those order/leastness fields.\", \"urn:csabs:axiom/PartialOrder-transitive\": \"Interpreted premise: x≤y ∧ y≤z ⇒ x≤z. SemilatticeSup extends PartialOrder with binary sup and le_sup_left/le_sup_right/sup_le. Sup is catalog join, ≤ and equality retain their carrier meanings. sup_comm uses those order/leastness fields.\"}"
  },
  {
    "id": "urn:csabs:law/JoinSemilattice-associativity",
    "type": "Law",
    "name": "associativity",
    "statement": "(a∨b)∨c=a∨(b∨c).",
    "formalStatement": "(a∨b)∨c=a∨(b∨c).",
    "mathematicalFormulation": "(a∨b)∨c=a∨(b∨c).",
    "proofSketch": "Use the least-upper-bound order laws via sup_assoc.",
    "assumptions": [
      "Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles."
    ],
    "appliesTo": [
      "urn:csabs:concept/JoinSemilattice"
    ],
    "dependsOn": [
      "urn:csabs:axiom/JoinSemilattice-utility-profile",
      "urn:csabs:axiom/JoinSemilattice-upper-bounds",
      "urn:csabs:axiom/JoinSemilattice-leastness"
    ],
    "reviewStatus": "Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned",
      "urn:csabs:source/utility-lean-CollectionUtilities"
    ],
    "sourceLocator": "Order/Lattice.lean: sup_assoc and sup_le_iff; Order/BoundedOrder/Basic.lean: bottom; Order/Lattice/Nat.lean: Nat max/zero instance; Catalog.join_associative",
    "sourceNote": "Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {A : Type u} [SemilatticeSup A] (a b c : A), (a ⊔ b) ⊔ c = a ⊔ (b ⊔ c)",
    "leanModelMapping": "(a∨b)∨c=a∨(b∨c). Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.",
    "leanModelLimitations": "Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/JoinSemilattice-leastness\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\", \"urn:csabs:axiom/JoinSemilattice-upper-bounds\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\", \"urn:csabs:axiom/JoinSemilattice-utility-profile\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\"}",
    "formulationScope": "registered-witness-type",
    "formulationSource": "urn:csabs:source/utility-lean-CollectionUtilities",
    "formulationLocator": "Catalog.join_associative"
  },
  {
    "id": "urn:csabs:law/JoinSemilattice-bottom-empty-identities",
    "type": "Law",
    "name": "bottom-empty-identities",
    "statement": "In the optional bottom profile, ⊥∨a=a=a∨⊥ and joinAll([])=⊥.",
    "formalStatement": "In the optional bottom profile, ⊥∨a=a=a∨⊥ and joinAll([])=⊥.",
    "mathematicalFormulation": "In the optional bottom profile, ⊥∨a=a=a∨⊥ and joinAll([])=⊥.",
    "proofSketch": "The least-element and join laws yield the binary identities; empty fold is definitional.",
    "assumptions": [
      "Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles."
    ],
    "appliesTo": [
      "urn:csabs:concept/JoinSemilattice"
    ],
    "dependsOn": [
      "urn:csabs:axiom/JoinSemilattice-utility-profile"
    ],
    "reviewStatus": "Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned",
      "urn:csabs:source/utility-lean-CollectionUtilities"
    ],
    "sourceLocator": "Order/Lattice.lean: sup_assoc and sup_le_iff; Order/BoundedOrder/Basic.lean: bottom; Order/Lattice/Nat.lean: Nat max/zero instance; Catalog.join_bottom_laws",
    "sourceNote": "Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {A : Type u} [SemilatticeSup A] [OrderBot A] (a : A), ⊥ ⊔ a = a ∧ a ⊔ ⊥ = a ∧ Catalog.joinAll ([] : List A) = ⊥",
    "leanModelMapping": "In the optional bottom profile, ⊥∨a=a=a∨⊥ and joinAll([])=⊥. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.",
    "leanModelLimitations": "Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/JoinSemilattice-utility-profile\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\"}",
    "formulationScope": "registered-witness-type",
    "formulationSource": "urn:csabs:source/utility-lean-CollectionUtilities",
    "formulationLocator": "Catalog.join_bottom_laws"
  },
  {
    "id": "urn:csabs:theorem/JoinSemilattice-idempotence",
    "type": "Theorem",
    "name": "idempotence",
    "statement": "x⊔x=x",
    "formalStatement": "x⊔x=x",
    "assumptions": [
      "Binary joins only. A bottom element, meets, completeness or distributivity is additional structure. Equality is the carrier equality used by antisymmetry; empty carrier allowed.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/JoinSemilattice"
    ],
    "dependsOn": [
      "urn:csabs:axiom/PartialOrder-reflexive",
      "urn:csabs:axiom/PartialOrder-transitive",
      "urn:csabs:axiom/PartialOrder-antisymmetric",
      "urn:csabs:axiom/JoinSemilattice-upper-bounds",
      "urn:csabs:axiom/JoinSemilattice-leastness"
    ],
    "proofSketch": "The join is above x; x is an upper bound of both copies. Use leastness and antisymmetry.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/mathlib-join-core"
    ],
    "sourceLocator": "SemilatticeSup: PartialOrder, le_sup_left, le_sup_right, sup_le",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {A : Type} [Catalog.JoinSemilattice A] (x : A), x ⊔ x = x",
    "formulationSource": "urn:csabs:source/local-lean-CoreData",
    "formulationLocator": "Catalog.CoreDataProofs.join_idempotent",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "SemilatticeSup supplies the explicitly reused partial-order rules and upper-bound/leastness fields; sup_idem derives idempotence. Join is ⊔.",
    "leanModelLimitations": "Only the displayed proposition for this explicit interpretation. No proof of all catalog claims or of a software implementation; informal/formal correspondence remains reviewed metadata.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/JoinSemilattice-leastness\": \"Interpreted premise: x≤z ∧ y≤z ⇒ x⊔y≤z. SemilatticeSup supplies the explicitly reused partial-order rules and upper-bound/leastness fields; sup_idem derives idempotence. Join is ⊔.\", \"urn:csabs:axiom/JoinSemilattice-upper-bounds\": \"Interpreted premise: x≤x⊔y ∧ y≤x⊔y. SemilatticeSup supplies the explicitly reused partial-order rules and upper-bound/leastness fields; sup_idem derives idempotence. Join is ⊔.\", \"urn:csabs:axiom/PartialOrder-antisymmetric\": \"Interpreted premise: x≤y ∧ y≤x ⇒ x=y. SemilatticeSup supplies the explicitly reused partial-order rules and upper-bound/leastness fields; sup_idem derives idempotence. Join is ⊔.\", \"urn:csabs:axiom/PartialOrder-reflexive\": \"Interpreted premise: ∀x∈A:x≤x. SemilatticeSup supplies the explicitly reused partial-order rules and upper-bound/leastness fields; sup_idem derives idempotence. Join is ⊔.\", \"urn:csabs:axiom/PartialOrder-transitive\": \"Interpreted premise: x≤y ∧ y≤z ⇒ x≤z. SemilatticeSup supplies the explicitly reused partial-order rules and upper-bound/leastness fields; sup_idem derives idempotence. Join is ⊔.\"}"
  },
  {
    "id": "urn:csabs:theorem/JoinSemilattice-finite-join-lub",
    "type": "Theorem",
    "name": "finite-join-lub",
    "statement": "In the bottom profile, joinAll(xs)≤z iff every member a of xs satisfies a≤z.",
    "formalStatement": "In the bottom profile, joinAll(xs)≤z iff every member a of xs satisfies a≤z.",
    "mathematicalFormulation": "In the bottom profile, joinAll(xs)≤z iff every member a of xs satisfies a≤z.",
    "proofSketch": "Induct over xs using sup_le_iff; the empty case uses the least-element property.",
    "assumptions": [
      "Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles."
    ],
    "appliesTo": [
      "urn:csabs:concept/JoinSemilattice"
    ],
    "dependsOn": [
      "urn:csabs:axiom/JoinSemilattice-utility-profile",
      "urn:csabs:axiom/JoinSemilattice-leastness"
    ],
    "reviewStatus": "Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned",
      "urn:csabs:source/utility-lean-CollectionUtilities"
    ],
    "sourceLocator": "Order/Lattice.lean: sup_assoc and sup_le_iff; Order/BoundedOrder/Basic.lean: bottom; Order/Lattice/Nat.lean: Nat max/zero instance; Catalog.joinAll_lub",
    "sourceNote": "Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {A : Type u} [SemilatticeSup A] [OrderBot A]\n    (xs : List A) (z : A), Catalog.joinAll xs ≤ z ↔ ∀ a ∈ xs, a ≤ z",
    "leanModelMapping": "In the bottom profile, joinAll(xs)≤z iff every member a of xs satisfies a≤z. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.",
    "leanModelLimitations": "Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/JoinSemilattice-leastness\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\", \"urn:csabs:axiom/JoinSemilattice-utility-profile\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\"}",
    "formulationScope": "registered-witness-type",
    "formulationSource": "urn:csabs:source/utility-lean-CollectionUtilities",
    "formulationLocator": "Catalog.joinAll_lub"
  },
  {
    "id": "urn:csabs:theorem/JoinSemilattice-bottom-model-satisfaction",
    "type": "Theorem",
    "name": "bottom-model-satisfaction",
    "statement": "The natural-number max/zero model has joinAll([])=0 and joinAll([1,3,2])=3.",
    "formalStatement": "The natural-number max/zero model has joinAll([])=0 and joinAll([1,3,2])=3.",
    "mathematicalFormulation": "The natural-number max/zero model has joinAll([])=0 and joinAll([1,3,2])=3.",
    "proofSketch": "Evaluate concrete Nat max and zero; the pinned Nat instance supplies a nontrivial inhabited bottom semilattice.",
    "assumptions": [
      "Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles."
    ],
    "appliesTo": [
      "urn:csabs:concept/JoinSemilattice"
    ],
    "dependsOn": [
      "urn:csabs:axiom/JoinSemilattice-utility-profile"
    ],
    "reviewStatus": "Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned",
      "urn:csabs:source/utility-lean-CollectionUtilities"
    ],
    "sourceLocator": "Order/Lattice.lean: sup_assoc and sup_le_iff; Order/BoundedOrder/Basic.lean: bottom; Order/Lattice/Nat.lean: Nat max/zero instance; Catalog.join_bottom_model",
    "sourceNote": "Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.",
    "provenanceKind": "derived",
    "leanFormulation": "Catalog.joinAll ([] : List Nat) = 0 ∧ Catalog.joinAll [1, 3, 2] = 3",
    "leanModelMapping": "The natural-number max/zero model has joinAll([])=0 and joinAll([1,3,2])=3. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.",
    "leanModelLimitations": "Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/JoinSemilattice-utility-profile\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\"}",
    "formulationScope": "registered-witness-type",
    "formulationSource": "urn:csabs:source/utility-lean-CollectionUtilities",
    "formulationLocator": "Catalog.join_bottom_model"
  }
]
```
<!-- graph-record:end -->
