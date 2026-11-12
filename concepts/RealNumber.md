# Exact real number

A complete Archimedean linearly ordered field extending the rational numbers.

**Notation:** ℝ

**Stable ID:** `urn:csabs:concept/RealNumber`

**Categories:** Numeric computation

**Kind:** Numeric data type

**Prerequisites:** [Exact rational number](RationalNumber.md), [Field](Field.md), [Total Order](TotalOrder.md)

**Specializes:** [Field](Field.md)

## Backlinks

- [Arithmetic mean of a finite real sample](ArithmeticMean.md) — `requiresConcept`
- [Cholesky decomposition (Hermitian positive definite, lower profile)](CholeskyDecomposition.md) — `requiresConcept`
- [Exact complex number](ComplexNumber.md) — `requiresConcept`
- [Numeric sample median (midpoint convention)](Median.md) — `requiresConcept`
- [Full QR decomposition (real or complex, rectangular)](QRDecomposition.md) — `requiresConcept`
- [Full singular value decomposition (rectangular real or complex SVD)](SVD.md) — `requiresConcept`
- [Finite real-weighted directed multigraph](WeightedDirectedGraph.md) — `requiresConcept`

## Mathematical formulation

ℝ is the exact complete ordered field interpretation. It has no floating-point rounding or finite-width overflow; field equality is exact real equality.

**Lean formulation** (in its source module context):

```lean
abbrev RealNumber := Real
```

**Source:** [`Catalog.RealNumber`](../lean/Catalog/CoreData.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Real and its conditionally complete linear ordered field; the graph sup operation corresponds to sSup only under nonempty/bounded hypotheses. ℝ. Classical exact real equality/order, generally noncomputable; no claim of a finite representation or decision algorithm. Supremum requires nonempty bounded-above set. Division requires nonzero divisor.

**Limits:** Compiled carrier and selected interface interpretation. Some catalog operations are specified mathematically rather than wrapped as Lean declarations; no blanket proof of claims, algorithms, parsing, liveness or complexity. See individual witnesses.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** ℝ is a field with linear order ≤; a≤b ⇒ a+c≤b+c; 0≤a ∧ 0≤b ⇒ 0≤a·b; 0<1; For nonempty bounded-above S, (∀s∈S,s≤sup(S)) ∧ (∀u,(∀s∈S,s≤u)⇒sup(S)≤u)

**basisKind:** extensional-structural-definition

**basisScope:** Classical exact real equality/order, generally noncomputable; no claim of a finite representation or decision algorithm. Supremum requires nonempty bounded-above set. Division requires nonzero divisor.

**specializationNote:** Instantiate Field with the exact real carrier and its ordered-field operations. Completeness is additional structure, not inherited from Field.

**verificationObligation:** Map carrier, equality, operation definedness and stated profile to the target API or proof context.; Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.; Model coverage does not establish every recorded claim or an implementation refinement.

**reviewStatus:** Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-RealNumber-arithmetic"></a>

### arithmetic

`urn:csabs:operation/RealNumber-arithmetic`

**signature:** add,multiply : ℝ×ℝ→ℝ; negate:ℝ→ℝ

**description:** Exact ordered-field operations.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Classical exact real equality/order, generally noncomputable; no claim of a finite representation or decision algorithm. Supremum requires nonempty bounded-above set. Division requires nonzero divisor.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Exact ordered-field operations.

**source:** [Mathlib pinned definitions: Algebra/Order/Archimedean/Real/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Algebra/Order/Archimedean/Real/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Real.exists_isLUB, Real.isLUB_sSup, ConditionallyCompleteLinearOrder instance

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-RealNumber-divide"></a>

### divide

`urn:csabs:operation/RealNumber-divide`

**signature:** divide : ℝ×(ℝ∖{0})→ℝ

**description:** Exact field division on nonzero divisors.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Classical exact real equality/order, generally noncomputable; no claim of a finite representation or decision algorithm. Supremum requires nonempty bounded-above set. Division requires nonzero divisor.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Exact field division on nonzero divisors.

**source:** [Mathlib pinned definitions: Algebra/Order/Archimedean/Real/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Algebra/Order/Archimedean/Real/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Real.exists_isLUB, Real.isLUB_sSup, ConditionallyCompleteLinearOrder instance

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-RealNumber-supremum"></a>

### supremum

`urn:csabs:operation/RealNumber-supremum`

**signature:** sup : {S⊆ℝ | S≠∅ ∧ S bounded above}→ℝ

**description:** Returns the least upper bound.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Classical exact real equality/order, generally noncomputable; no claim of a finite representation or decision algorithm. Supremum requires nonempty bounded-above set. Division requires nonzero divisor.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Returns the least upper bound.

**source:** [Mathlib pinned definitions: Algebra/Order/Archimedean/Real/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Algebra/Order/Archimedean/Real/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Real.exists_isLUB, Real.isLUB_sSup, ConditionallyCompleteLinearOrder instance

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-RealNumber-ordered-field"></a>

### ordered-field

`urn:csabs:axiom/RealNumber-ordered-field`

**statement:** Defining requirement: ℝ is a field with linear order ≤; a≤b ⇒ a+c≤b+c; 0≤a ∧ 0≤b ⇒ 0≤a·b; 0<1

**formalStatement:** ℝ is a field with linear order ≤; a≤b ⇒ a+c≤b+c; 0≤a ∧ 0≤b ⇒ 0≤a·b; 0<1

**assumptions:** Classical exact real equality/order, generally noncomputable; no claim of a finite representation or decision algorithm. Supremum requires nonempty bounded-above set. Division requires nonzero divisor.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Mathlib pinned definitions: Algebra/Order/Archimedean/Real/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Algebra/Order/Archimedean/Real/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Real.exists_isLUB, Real.isLUB_sSup, ConditionallyCompleteLinearOrder instance

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-RealNumber-completeness"></a>

### completeness

`urn:csabs:axiom/RealNumber-completeness`

**statement:** Defining requirement: For nonempty bounded-above S, (∀s∈S,s≤sup(S)) ∧ (∀u,(∀s∈S,s≤u)⇒sup(S)≤u)

**formalStatement:** For nonempty bounded-above S, (∀s∈S,s≤sup(S)) ∧ (∀u,(∀s∈S,s≤u)⇒sup(S)≤u)

**assumptions:** Classical exact real equality/order, generally noncomputable; no claim of a finite representation or decision algorithm. Supremum requires nonempty bounded-above set. Division requires nonzero divisor.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Mathlib pinned definitions: Algebra/Order/Archimedean/Real/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Algebra/Order/Archimedean/Real/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Real.exists_isLUB, Real.isLUB_sSup, ConditionallyCompleteLinearOrder instance

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-RealNumber-square-nonnegative"></a>

### square-nonnegative

`urn:csabs:law/RealNumber-square-nonnegative`

**statement:** ∀x:ℝ, 0≤x·x

**formalStatement:** ∀x:ℝ, 0≤x·x

**assumptions:** Classical exact real equality/order, generally noncomputable; no claim of a finite representation or decision algorithm. Supremum requires nonempty bounded-above set. Division requires nonzero divisor.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [ordered-field](RealNumber.md#node-urn-csabs-axiom-RealNumber-ordered-field)

**proofSketch:** If x≥0 apply order-compatible multiplication. Otherwise -x≥0 and (-x)(-x)=x·x by field laws.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Mathlib pinned definitions: Algebra/Order/Archimedean/Real/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Algebra/Order/Archimedean/Real/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Real.exists_isLUB, Real.isLUB_sSup, ConditionallyCompleteLinearOrder instance

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ (x : Catalog.RealNumber), 0 ≤ x * x
```

**Source:** [`Catalog.CoreDataProofs.real_square_nonnegative`](../lean/Catalog/CoreData.lean); consulted 2026-11-12.

**Scope:** registered-witness-type

**Interpretation:** Lean Real with its ordered-field operations and exact ≤; no floating-point instance. mul_self_nonneg derives the result from ordered-ring laws; completeness is not needed.

**Limits:** Only the displayed proposition for this explicit interpretation. No proof of all catalog claims or of a software implementation; informal/formal correspondence remains reviewed metadata.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/RealNumber-ordered-field": "Interpreted premise: ℝ is a field with linear order ≤; a≤b ⇒ a+c≤b+c; 0≤a ∧ 0≤b ⇒ 0≤a·b; 0<1. Lean Real with its ordered-field operations and exact ≤; no floating-point instance. mul_self_nonneg derives the result from ordered-ring laws; completeness is not needed."
}
```

## Theorems

<a id="node-urn-csabs-theorem-RealNumber-supremum-unique"></a>

### supremum-unique

`urn:csabs:theorem/RealNumber-supremum-unique`

**statement:** Any two least upper bounds of the same nonempty bounded-above S are equal

**formalStatement:** Any two least upper bounds of the same nonempty bounded-above S are equal

**assumptions:** Classical exact real equality/order, generally noncomputable; no claim of a finite representation or decision algorithm. Supremum requires nonempty bounded-above set. Division requires nonzero divisor.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [ordered-field](RealNumber.md#node-urn-csabs-axiom-RealNumber-ordered-field); [completeness](RealNumber.md#node-urn-csabs-axiom-RealNumber-completeness)

**proofSketch:** Each is at most the other by leastness; use order antisymmetry.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Mathlib pinned definitions: Algebra/Order/Archimedean/Real/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Algebra/Order/Archimedean/Real/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Real.exists_isLUB, Real.isLUB_sSup, ConditionallyCompleteLinearOrder instance

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Concept provenance

- [Mathlib pinned definitions: Algebra/Order/Archimedean/Real/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Algebra/Order/Archimedean/Real/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Real.exists_isLUB, Real.isLUB_sSup, ConditionallyCompleteLinearOrder instance

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/RealNumber",
    "type": "Concept",
    "shortForm": "RealNumber",
    "fullName": "Exact real number",
    "category": [
      "urn:csabs:category/numeric-computation"
    ],
    "kind": "urn:csabs:kind/data-type",
    "definition": "A complete Archimedean linearly ordered field extending the rational numbers.",
    "notation": "ℝ",
    "requiresConcept": [
      "urn:csabs:concept/RationalNumber",
      "urn:csabs:concept/Field",
      "urn:csabs:concept/TotalOrder"
    ],
    "relatedConcept": [],
    "hasOperation": [
      "urn:csabs:operation/RealNumber-arithmetic",
      "urn:csabs:operation/RealNumber-divide",
      "urn:csabs:operation/RealNumber-supremum"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/RealNumber-ordered-field",
      "urn:csabs:axiom/RealNumber-completeness"
    ],
    "hasLaw": [
      "urn:csabs:law/RealNumber-square-nonnegative"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/RealNumber-supremum-unique"
    ],
    "axiomBasis": "ℝ is a field with linear order ≤; a≤b ⇒ a+c≤b+c; 0≤a ∧ 0≤b ⇒ 0≤a·b; 0<1; For nonempty bounded-above S, (∀s∈S,s≤sup(S)) ∧ (∀u,(∀s∈S,s≤u)⇒sup(S)≤u)",
    "basisKind": "extensional-structural-definition",
    "basisScope": "Classical exact real equality/order, generally noncomputable; no claim of a finite representation or decision algorithm. Supremum requires nonempty bounded-above set. Division requires nonzero divisor.",
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Map carrier, equality, operation definedness and stated profile to the target API or proof context.",
      "Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.",
      "Model coverage does not establish every recorded claim or an implementation refinement."
    ],
    "reviewStatus": "Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.",
    "source": [
      "urn:csabs:source/mathlib-real-core"
    ],
    "sourceLocator": "Real.exists_isLUB, Real.isLUB_sSup, ConditionallyCompleteLinearOrder instance",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/Field"
    ],
    "specializationNote": "Instantiate Field with the exact real carrier and its ordered-field operations. Completeness is additional structure, not inherited from Field.",
    "leanFormulation": "abbrev RealNumber := Real",
    "formulationSource": "urn:csabs:source/local-lean-CoreData",
    "formulationLocator": "Catalog.RealNumber",
    "formulationScope": "model",
    "leanModelMapping": "Real and its conditionally complete linear ordered field; the graph sup operation corresponds to sSup only under nonempty/bounded hypotheses. ℝ. Classical exact real equality/order, generally noncomputable; no claim of a finite representation or decision algorithm. Supremum requires nonempty bounded-above set. Division requires nonzero divisor.",
    "leanModelLimitations": "Compiled carrier and selected interface interpretation. Some catalog operations are specified mathematically rather than wrapped as Lean declarations; no blanket proof of claims, algorithms, parsing, liveness or complexity. See individual witnesses.",
    "mathematicalFormulation": "ℝ is the exact complete ordered field interpretation. It has no floating-point rounding or finite-width overflow; field equality is exact real equality."
  },
  {
    "id": "urn:csabs:operation/RealNumber-arithmetic",
    "type": "Operation",
    "name": "arithmetic",
    "signature": "add,multiply : ℝ×ℝ→ℝ; negate:ℝ→ℝ",
    "description": "Exact ordered-field operations.",
    "concept": "urn:csabs:concept/RealNumber",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Classical exact real equality/order, generally noncomputable; no claim of a finite representation or decision algorithm. Supremum requires nonempty bounded-above set. Division requires nonzero divisor.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Exact ordered-field operations.",
    "source": [
      "urn:csabs:source/mathlib-real-core"
    ],
    "sourceLocator": "Real.exists_isLUB, Real.isLUB_sSup, ConditionallyCompleteLinearOrder instance",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/RealNumber-divide",
    "type": "Operation",
    "name": "divide",
    "signature": "divide : ℝ×(ℝ∖{0})→ℝ",
    "description": "Exact field division on nonzero divisors.",
    "concept": "urn:csabs:concept/RealNumber",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Classical exact real equality/order, generally noncomputable; no claim of a finite representation or decision algorithm. Supremum requires nonempty bounded-above set. Division requires nonzero divisor.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Exact field division on nonzero divisors.",
    "source": [
      "urn:csabs:source/mathlib-real-core"
    ],
    "sourceLocator": "Real.exists_isLUB, Real.isLUB_sSup, ConditionallyCompleteLinearOrder instance",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/RealNumber-supremum",
    "type": "Operation",
    "name": "supremum",
    "signature": "sup : {S⊆ℝ | S≠∅ ∧ S bounded above}→ℝ",
    "description": "Returns the least upper bound.",
    "concept": "urn:csabs:concept/RealNumber",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Classical exact real equality/order, generally noncomputable; no claim of a finite representation or decision algorithm. Supremum requires nonempty bounded-above set. Division requires nonzero divisor.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Returns the least upper bound.",
    "source": [
      "urn:csabs:source/mathlib-real-core"
    ],
    "sourceLocator": "Real.exists_isLUB, Real.isLUB_sSup, ConditionallyCompleteLinearOrder instance",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/RealNumber-ordered-field",
    "type": "Axiom",
    "name": "ordered-field",
    "statement": "Defining requirement: ℝ is a field with linear order ≤; a≤b ⇒ a+c≤b+c; 0≤a ∧ 0≤b ⇒ 0≤a·b; 0<1",
    "formalStatement": "ℝ is a field with linear order ≤; a≤b ⇒ a+c≤b+c; 0≤a ∧ 0≤b ⇒ 0≤a·b; 0<1",
    "assumptions": [
      "Classical exact real equality/order, generally noncomputable; no claim of a finite representation or decision algorithm. Supremum requires nonempty bounded-above set. Division requires nonzero divisor.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/RealNumber"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/mathlib-real-core"
    ],
    "sourceLocator": "Real.exists_isLUB, Real.isLUB_sSup, ConditionallyCompleteLinearOrder instance",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/RealNumber-completeness",
    "type": "Axiom",
    "name": "completeness",
    "statement": "Defining requirement: For nonempty bounded-above S, (∀s∈S,s≤sup(S)) ∧ (∀u,(∀s∈S,s≤u)⇒sup(S)≤u)",
    "formalStatement": "For nonempty bounded-above S, (∀s∈S,s≤sup(S)) ∧ (∀u,(∀s∈S,s≤u)⇒sup(S)≤u)",
    "assumptions": [
      "Classical exact real equality/order, generally noncomputable; no claim of a finite representation or decision algorithm. Supremum requires nonempty bounded-above set. Division requires nonzero divisor.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/RealNumber"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/mathlib-real-core"
    ],
    "sourceLocator": "Real.exists_isLUB, Real.isLUB_sSup, ConditionallyCompleteLinearOrder instance",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/RealNumber-square-nonnegative",
    "type": "Law",
    "name": "square-nonnegative",
    "statement": "∀x:ℝ, 0≤x·x",
    "formalStatement": "∀x:ℝ, 0≤x·x",
    "assumptions": [
      "Classical exact real equality/order, generally noncomputable; no claim of a finite representation or decision algorithm. Supremum requires nonempty bounded-above set. Division requires nonzero divisor.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/RealNumber"
    ],
    "dependsOn": [
      "urn:csabs:axiom/RealNumber-ordered-field"
    ],
    "proofSketch": "If x≥0 apply order-compatible multiplication. Otherwise -x≥0 and (-x)(-x)=x·x by field laws.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/mathlib-real-core"
    ],
    "sourceLocator": "Real.exists_isLUB, Real.isLUB_sSup, ConditionallyCompleteLinearOrder instance",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ (x : Catalog.RealNumber), 0 ≤ x * x",
    "formulationSource": "urn:csabs:source/local-lean-CoreData",
    "formulationLocator": "Catalog.CoreDataProofs.real_square_nonnegative",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Lean Real with its ordered-field operations and exact ≤; no floating-point instance. mul_self_nonneg derives the result from ordered-ring laws; completeness is not needed.",
    "leanModelLimitations": "Only the displayed proposition for this explicit interpretation. No proof of all catalog claims or of a software implementation; informal/formal correspondence remains reviewed metadata.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/RealNumber-ordered-field\": \"Interpreted premise: ℝ is a field with linear order ≤; a≤b ⇒ a+c≤b+c; 0≤a ∧ 0≤b ⇒ 0≤a·b; 0<1. Lean Real with its ordered-field operations and exact ≤; no floating-point instance. mul_self_nonneg derives the result from ordered-ring laws; completeness is not needed.\"}"
  },
  {
    "id": "urn:csabs:theorem/RealNumber-supremum-unique",
    "type": "Theorem",
    "name": "supremum-unique",
    "statement": "Any two least upper bounds of the same nonempty bounded-above S are equal",
    "formalStatement": "Any two least upper bounds of the same nonempty bounded-above S are equal",
    "assumptions": [
      "Classical exact real equality/order, generally noncomputable; no claim of a finite representation or decision algorithm. Supremum requires nonempty bounded-above set. Division requires nonzero divisor.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/RealNumber"
    ],
    "dependsOn": [
      "urn:csabs:axiom/RealNumber-ordered-field",
      "urn:csabs:axiom/RealNumber-completeness"
    ],
    "proofSketch": "Each is at most the other by leastness; use order antisymmetry.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/mathlib-real-core"
    ],
    "sourceLocator": "Real.exists_isLUB, Real.isLUB_sSup, ConditionallyCompleteLinearOrder instance",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
