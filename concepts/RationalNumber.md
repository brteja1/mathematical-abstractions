# Exact rational number

The characteristic-zero field of fractions of the integers.

**Notation:** ℚ={m/n | m∈ℤ, n∈ℕ, n>0}

**Stable ID:** `urn:csabs:concept/RationalNumber`

**Categories:** Numeric computation

**Kind:** Numeric data type

**Prerequisites:** [Arbitrary Precision Integer](ArbitraryPrecisionInteger.md), [Field](Field.md)

**Specializes:** [Field](Field.md)

## Backlinks

- [Finite JSON document value (interoperable profile)](DocumentValue.md) — `requiresConcept`
- [Exact real number](RealNumber.md) — `requiresConcept`

## Interface and scope

**axiomBasis:** m/n=p/q ⇔ m·q=p·n, for n,q>0; m/n+p/q=(mq+pn)/(nq) ∧ (m/n)(p/q)=mp/(nq); Every rational has a unique coprime presentation m/n with n>0; fraction(0,1)=0

**basisKind:** extensional-structural-definition

**basisScope:** Exact unbounded arithmetic. Canonical fractions have positive coprime denominator. Division is exposed only for nonzero divisor; Lean has a total inverse at zero, used only under this precondition. No rounding or finite resource bounds.

**specializationNote:** Instantiate Field at ℚ with exact fraction addition/multiplication, 0/1 and 1/1; inverse and division restricted to nonzero inputs in this interface.

**verificationObligation:** Map carrier, equality, operation definedness and stated profile to the target API or proof context.; Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.; Model coverage does not establish every recorded claim or an implementation refinement.

**reviewStatus:** Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-RationalNumber-fraction"></a>

### fraction

`urn:csabs:operation/RationalNumber-fraction`

**signature:** fraction : ℤ×ℕ_{>0}→ℚ

**description:** Returns the value m/n, normalized for equality.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Exact unbounded arithmetic. Canonical fractions have positive coprime denominator. Division is exposed only for nonzero divisor; Lean has a total inverse at zero, used only under this precondition. No rounding or finite resource bounds.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Returns the value m/n, normalized for equality.

**source:** [Mathlib pinned definitions: Algebra/Field/Rat.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Algebra/Field/Rat.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Data/Rat/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Rat/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Rat.instField and Rat.num_div_den; imports Data.Rat.Defs; Rat normalized numerator/positive denominator; arithmetic definitions

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-RationalNumber-add"></a>

### add

`urn:csabs:operation/RationalNumber-add`

**signature:** add : ℚ×ℚ→ℚ

**description:** m/n+p/q=(mq+pn)/(nq).

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Exact unbounded arithmetic. Canonical fractions have positive coprime denominator. Division is exposed only for nonzero divisor; Lean has a total inverse at zero, used only under this precondition. No rounding or finite resource bounds.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** m/n+p/q=(mq+pn)/(nq).

**source:** [Mathlib pinned definitions: Algebra/Field/Rat.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Algebra/Field/Rat.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Data/Rat/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Rat/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Rat.instField and Rat.num_div_den; imports Data.Rat.Defs; Rat normalized numerator/positive denominator; arithmetic definitions

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-RationalNumber-multiply"></a>

### multiply

`urn:csabs:operation/RationalNumber-multiply`

**signature:** multiply : ℚ×ℚ→ℚ

**description:** (m/n)(p/q)=mp/(nq).

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Exact unbounded arithmetic. Canonical fractions have positive coprime denominator. Division is exposed only for nonzero divisor; Lean has a total inverse at zero, used only under this precondition. No rounding or finite resource bounds.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** (m/n)(p/q)=mp/(nq).

**source:** [Mathlib pinned definitions: Algebra/Field/Rat.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Algebra/Field/Rat.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Data/Rat/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Rat/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Rat.instField and Rat.num_div_den; imports Data.Rat.Defs; Rat normalized numerator/positive denominator; arithmetic definitions

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-RationalNumber-divide"></a>

### divide

`urn:csabs:operation/RationalNumber-divide`

**signature:** divide : ℚ×(ℚ∖{0})→ℚ

**description:** x/y=x·y⁻¹; defined only when y≠0.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Exact unbounded arithmetic. Canonical fractions have positive coprime denominator. Division is exposed only for nonzero divisor; Lean has a total inverse at zero, used only under this precondition. No rounding or finite resource bounds.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** x/y=x·y⁻¹; defined only when y≠0.

**source:** [Mathlib pinned definitions: Algebra/Field/Rat.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Algebra/Field/Rat.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Data/Rat/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Rat/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Rat.instField and Rat.num_div_den; imports Data.Rat.Defs; Rat normalized numerator/positive denominator; arithmetic definitions

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-RationalNumber-fraction-equality"></a>

### fraction-equality

`urn:csabs:axiom/RationalNumber-fraction-equality`

**statement:** Defining requirement: m/n=p/q ⇔ m·q=p·n, for n,q>0

**formalStatement:** m/n=p/q ⇔ m·q=p·n, for n,q>0

**assumptions:** Exact unbounded arithmetic. Canonical fractions have positive coprime denominator. Division is exposed only for nonzero divisor; Lean has a total inverse at zero, used only under this precondition. No rounding or finite resource bounds.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Mathlib pinned definitions: Algebra/Field/Rat.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Algebra/Field/Rat.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Data/Rat/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Rat/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Rat.instField and Rat.num_div_den; imports Data.Rat.Defs; Rat normalized numerator/positive denominator; arithmetic definitions

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-RationalNumber-arithmetic"></a>

### arithmetic

`urn:csabs:axiom/RationalNumber-arithmetic`

**statement:** Defining requirement: m/n+p/q=(mq+pn)/(nq) ∧ (m/n)(p/q)=mp/(nq)

**formalStatement:** m/n+p/q=(mq+pn)/(nq) ∧ (m/n)(p/q)=mp/(nq)

**assumptions:** Exact unbounded arithmetic. Canonical fractions have positive coprime denominator. Division is exposed only for nonzero divisor; Lean has a total inverse at zero, used only under this precondition. No rounding or finite resource bounds.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Mathlib pinned definitions: Algebra/Field/Rat.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Algebra/Field/Rat.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Data/Rat/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Rat/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Rat.instField and Rat.num_div_den; imports Data.Rat.Defs; Rat normalized numerator/positive denominator; arithmetic definitions

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-RationalNumber-fraction-universal"></a>

### fraction-universal

`urn:csabs:axiom/RationalNumber-fraction-universal`

**statement:** Defining requirement: Every rational has a unique coprime presentation m/n with n>0; fraction(0,1)=0

**formalStatement:** Every rational has a unique coprime presentation m/n with n>0; fraction(0,1)=0

**assumptions:** Exact unbounded arithmetic. Canonical fractions have positive coprime denominator. Division is exposed only for nonzero divisor; Lean has a total inverse at zero, used only under this precondition. No rounding or finite resource bounds.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Mathlib pinned definitions: Algebra/Field/Rat.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Algebra/Field/Rat.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Data/Rat/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Rat/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Rat.instField and Rat.num_div_den; imports Data.Rat.Defs; Rat normalized numerator/positive denominator; arithmetic definitions

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-RationalNumber-add-zero"></a>

### add-zero

`urn:csabs:law/RationalNumber-add-zero`

**statement:** ∀q:ℚ, q+0=q

**formalStatement:** ∀q:ℚ, q+0=q

**assumptions:** Exact unbounded arithmetic. Canonical fractions have positive coprime denominator. Division is exposed only for nonzero divisor; Lean has a total inverse at zero, used only under this precondition. No rounding or finite resource bounds.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [fraction-equality](RationalNumber.md#node-urn-csabs-axiom-RationalNumber-fraction-equality); [arithmetic](RationalNumber.md#node-urn-csabs-axiom-RationalNumber-arithmetic); [fraction-universal](RationalNumber.md#node-urn-csabs-axiom-RationalNumber-fraction-universal)

**proofSketch:** Write q=m/n; use the arithmetic formula with 0/1 and fraction equality.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Mathlib pinned definitions: Algebra/Field/Rat.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Algebra/Field/Rat.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Data/Rat/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Rat/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Rat.instField and Rat.num_div_den; imports Data.Rat.Defs; Rat normalized numerator/positive denominator; arithmetic definitions

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Theorems

<a id="node-urn-csabs-theorem-RationalNumber-commutative-addition"></a>

### commutative-addition

`urn:csabs:theorem/RationalNumber-commutative-addition`

**statement:** ∀x,y:ℚ, x+y=y+x

**formalStatement:** ∀x,y:ℚ, x+y=y+x

**assumptions:** Exact unbounded arithmetic. Canonical fractions have positive coprime denominator. Division is exposed only for nonzero divisor; Lean has a total inverse at zero, used only under this precondition. No rounding or finite resource bounds.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [fraction-equality](RationalNumber.md#node-urn-csabs-axiom-RationalNumber-fraction-equality); [arithmetic](RationalNumber.md#node-urn-csabs-axiom-RationalNumber-arithmetic); [fraction-universal](RationalNumber.md#node-urn-csabs-axiom-RationalNumber-fraction-universal)

**proofSketch:** Write both fractions over their product denominator and use integer addition/multiplication commutativity.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Mathlib pinned definitions: Algebra/Field/Rat.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Algebra/Field/Rat.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Data/Rat/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Rat/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Rat.instField and Rat.num_div_den; imports Data.Rat.Defs; Rat normalized numerator/positive denominator; arithmetic definitions

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Concept provenance

- [Mathlib pinned definitions: Algebra/Field/Rat.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Algebra/Field/Rat.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference
- [Mathlib pinned definitions: Data/Rat/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Rat/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Rat.instField and Rat.num_div_den; imports Data.Rat.Defs; Rat normalized numerator/positive denominator; arithmetic definitions

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/RationalNumber",
    "type": "Concept",
    "shortForm": "RationalNumber",
    "fullName": "Exact rational number",
    "category": [
      "urn:csabs:category/numeric-computation"
    ],
    "kind": "urn:csabs:kind/data-type",
    "definition": "The characteristic-zero field of fractions of the integers.",
    "notation": "ℚ={m/n | m∈ℤ, n∈ℕ, n>0}",
    "requiresConcept": [
      "urn:csabs:concept/ArbitraryPrecisionInteger",
      "urn:csabs:concept/Field"
    ],
    "relatedConcept": [],
    "hasOperation": [
      "urn:csabs:operation/RationalNumber-fraction",
      "urn:csabs:operation/RationalNumber-add",
      "urn:csabs:operation/RationalNumber-multiply",
      "urn:csabs:operation/RationalNumber-divide"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/RationalNumber-fraction-equality",
      "urn:csabs:axiom/RationalNumber-arithmetic",
      "urn:csabs:axiom/RationalNumber-fraction-universal"
    ],
    "hasLaw": [
      "urn:csabs:law/RationalNumber-add-zero"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/RationalNumber-commutative-addition"
    ],
    "axiomBasis": "m/n=p/q ⇔ m·q=p·n, for n,q>0; m/n+p/q=(mq+pn)/(nq) ∧ (m/n)(p/q)=mp/(nq); Every rational has a unique coprime presentation m/n with n>0; fraction(0,1)=0",
    "basisKind": "extensional-structural-definition",
    "basisScope": "Exact unbounded arithmetic. Canonical fractions have positive coprime denominator. Division is exposed only for nonzero divisor; Lean has a total inverse at zero, used only under this precondition. No rounding or finite resource bounds.",
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Map carrier, equality, operation definedness and stated profile to the target API or proof context.",
      "Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.",
      "Model coverage does not establish every recorded claim or an implementation refinement."
    ],
    "reviewStatus": "Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.",
    "source": [
      "urn:csabs:source/mathlib-rational-core",
      "urn:csabs:source/mathlib-rational-defs-core"
    ],
    "sourceLocator": "Rat.instField and Rat.num_div_den; imports Data.Rat.Defs; Rat normalized numerator/positive denominator; arithmetic definitions",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/Field"
    ],
    "specializationNote": "Instantiate Field at ℚ with exact fraction addition/multiplication, 0/1 and 1/1; inverse and division restricted to nonzero inputs in this interface."
  },
  {
    "id": "urn:csabs:operation/RationalNumber-fraction",
    "type": "Operation",
    "name": "fraction",
    "signature": "fraction : ℤ×ℕ_{>0}→ℚ",
    "description": "Returns the value m/n, normalized for equality.",
    "concept": "urn:csabs:concept/RationalNumber",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Exact unbounded arithmetic. Canonical fractions have positive coprime denominator. Division is exposed only for nonzero divisor; Lean has a total inverse at zero, used only under this precondition. No rounding or finite resource bounds.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Returns the value m/n, normalized for equality.",
    "source": [
      "urn:csabs:source/mathlib-rational-core",
      "urn:csabs:source/mathlib-rational-defs-core"
    ],
    "sourceLocator": "Rat.instField and Rat.num_div_den; imports Data.Rat.Defs; Rat normalized numerator/positive denominator; arithmetic definitions",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/RationalNumber-add",
    "type": "Operation",
    "name": "add",
    "signature": "add : ℚ×ℚ→ℚ",
    "description": "m/n+p/q=(mq+pn)/(nq).",
    "concept": "urn:csabs:concept/RationalNumber",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Exact unbounded arithmetic. Canonical fractions have positive coprime denominator. Division is exposed only for nonzero divisor; Lean has a total inverse at zero, used only under this precondition. No rounding or finite resource bounds.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "m/n+p/q=(mq+pn)/(nq).",
    "source": [
      "urn:csabs:source/mathlib-rational-core",
      "urn:csabs:source/mathlib-rational-defs-core"
    ],
    "sourceLocator": "Rat.instField and Rat.num_div_den; imports Data.Rat.Defs; Rat normalized numerator/positive denominator; arithmetic definitions",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/RationalNumber-multiply",
    "type": "Operation",
    "name": "multiply",
    "signature": "multiply : ℚ×ℚ→ℚ",
    "description": "(m/n)(p/q)=mp/(nq).",
    "concept": "urn:csabs:concept/RationalNumber",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Exact unbounded arithmetic. Canonical fractions have positive coprime denominator. Division is exposed only for nonzero divisor; Lean has a total inverse at zero, used only under this precondition. No rounding or finite resource bounds.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "(m/n)(p/q)=mp/(nq).",
    "source": [
      "urn:csabs:source/mathlib-rational-core",
      "urn:csabs:source/mathlib-rational-defs-core"
    ],
    "sourceLocator": "Rat.instField and Rat.num_div_den; imports Data.Rat.Defs; Rat normalized numerator/positive denominator; arithmetic definitions",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/RationalNumber-divide",
    "type": "Operation",
    "name": "divide",
    "signature": "divide : ℚ×(ℚ∖{0})→ℚ",
    "description": "x/y=x·y⁻¹; defined only when y≠0.",
    "concept": "urn:csabs:concept/RationalNumber",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Exact unbounded arithmetic. Canonical fractions have positive coprime denominator. Division is exposed only for nonzero divisor; Lean has a total inverse at zero, used only under this precondition. No rounding or finite resource bounds.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "x/y=x·y⁻¹; defined only when y≠0.",
    "source": [
      "urn:csabs:source/mathlib-rational-core",
      "urn:csabs:source/mathlib-rational-defs-core"
    ],
    "sourceLocator": "Rat.instField and Rat.num_div_den; imports Data.Rat.Defs; Rat normalized numerator/positive denominator; arithmetic definitions",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/RationalNumber-fraction-equality",
    "type": "Axiom",
    "name": "fraction-equality",
    "statement": "Defining requirement: m/n=p/q ⇔ m·q=p·n, for n,q>0",
    "formalStatement": "m/n=p/q ⇔ m·q=p·n, for n,q>0",
    "assumptions": [
      "Exact unbounded arithmetic. Canonical fractions have positive coprime denominator. Division is exposed only for nonzero divisor; Lean has a total inverse at zero, used only under this precondition. No rounding or finite resource bounds.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/RationalNumber"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/mathlib-rational-core",
      "urn:csabs:source/mathlib-rational-defs-core"
    ],
    "sourceLocator": "Rat.instField and Rat.num_div_den; imports Data.Rat.Defs; Rat normalized numerator/positive denominator; arithmetic definitions",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/RationalNumber-arithmetic",
    "type": "Axiom",
    "name": "arithmetic",
    "statement": "Defining requirement: m/n+p/q=(mq+pn)/(nq) ∧ (m/n)(p/q)=mp/(nq)",
    "formalStatement": "m/n+p/q=(mq+pn)/(nq) ∧ (m/n)(p/q)=mp/(nq)",
    "assumptions": [
      "Exact unbounded arithmetic. Canonical fractions have positive coprime denominator. Division is exposed only for nonzero divisor; Lean has a total inverse at zero, used only under this precondition. No rounding or finite resource bounds.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/RationalNumber"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/mathlib-rational-core",
      "urn:csabs:source/mathlib-rational-defs-core"
    ],
    "sourceLocator": "Rat.instField and Rat.num_div_den; imports Data.Rat.Defs; Rat normalized numerator/positive denominator; arithmetic definitions",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/RationalNumber-fraction-universal",
    "type": "Axiom",
    "name": "fraction-universal",
    "statement": "Defining requirement: Every rational has a unique coprime presentation m/n with n>0; fraction(0,1)=0",
    "formalStatement": "Every rational has a unique coprime presentation m/n with n>0; fraction(0,1)=0",
    "assumptions": [
      "Exact unbounded arithmetic. Canonical fractions have positive coprime denominator. Division is exposed only for nonzero divisor; Lean has a total inverse at zero, used only under this precondition. No rounding or finite resource bounds.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/RationalNumber"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/mathlib-rational-core",
      "urn:csabs:source/mathlib-rational-defs-core"
    ],
    "sourceLocator": "Rat.instField and Rat.num_div_den; imports Data.Rat.Defs; Rat normalized numerator/positive denominator; arithmetic definitions",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/RationalNumber-add-zero",
    "type": "Law",
    "name": "add-zero",
    "statement": "∀q:ℚ, q+0=q",
    "formalStatement": "∀q:ℚ, q+0=q",
    "assumptions": [
      "Exact unbounded arithmetic. Canonical fractions have positive coprime denominator. Division is exposed only for nonzero divisor; Lean has a total inverse at zero, used only under this precondition. No rounding or finite resource bounds.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/RationalNumber"
    ],
    "dependsOn": [
      "urn:csabs:axiom/RationalNumber-fraction-equality",
      "urn:csabs:axiom/RationalNumber-arithmetic",
      "urn:csabs:axiom/RationalNumber-fraction-universal"
    ],
    "proofSketch": "Write q=m/n; use the arithmetic formula with 0/1 and fraction equality.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/mathlib-rational-core",
      "urn:csabs:source/mathlib-rational-defs-core"
    ],
    "sourceLocator": "Rat.instField and Rat.num_div_den; imports Data.Rat.Defs; Rat normalized numerator/positive denominator; arithmetic definitions",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/RationalNumber-commutative-addition",
    "type": "Theorem",
    "name": "commutative-addition",
    "statement": "∀x,y:ℚ, x+y=y+x",
    "formalStatement": "∀x,y:ℚ, x+y=y+x",
    "assumptions": [
      "Exact unbounded arithmetic. Canonical fractions have positive coprime denominator. Division is exposed only for nonzero divisor; Lean has a total inverse at zero, used only under this precondition. No rounding or finite resource bounds.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/RationalNumber"
    ],
    "dependsOn": [
      "urn:csabs:axiom/RationalNumber-fraction-equality",
      "urn:csabs:axiom/RationalNumber-arithmetic",
      "urn:csabs:axiom/RationalNumber-fraction-universal"
    ],
    "proofSketch": "Write both fractions over their product denominator and use integer addition/multiplication commutativity.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/mathlib-rational-core",
      "urn:csabs:source/mathlib-rational-defs-core"
    ],
    "sourceLocator": "Rat.instField and Rat.num_div_den; imports Data.Rat.Defs; Rat normalized numerator/positive denominator; arithmetic definitions",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
