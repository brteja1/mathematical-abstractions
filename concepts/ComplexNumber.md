# Exact complex number

Pairs of exact real coordinates equipped with complex-field arithmetic.

**Notation:** ℂ=ℝ×ℝ; (a,b)=a+bi

**Stable ID:** `urn:csabs:concept/ComplexNumber`

**Categories:** Numeric computation

**Kind:** Numeric data type

**Prerequisites:** [Exact real number](RealNumber.md), [Field](Field.md), [Product Type](ProductType.md)

**Specializes:** [Field](Field.md)

## Mathematical formulation

ℂ=ℝ×ℝ with (a,b)+(c,d)=(a+c,b+d), (a,b)(c,d)=(ac−bd,ad+bc), and i=(0,1). Equality is equality of both real coordinates.

**Lean formulation** (in its source module context):

```lean
abbrev ComplexNumber := Complex
```

**Source:** [`Catalog.ComplexNumber`](../lean/Catalog/CoreData.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Complex with Real re/im, coordinate equality and the complex field instance. ℂ=ℝ×ℝ; (a,b)=a+bi. Equality is coordinate equality. No compatible linear ordered-field structure, floating-point rounding or branch convention for complex transcendental functions is assumed. Division requires nonzero pair.

**Limits:** Compiled carrier and selected interface interpretation. Some catalog operations are specified mathematically rather than wrapped as Lean declarations; no blanket proof of claims, algorithms, parsing, liveness or complexity. See individual witnesses.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** re(mk(a,b))=a ∧ im(mk(a,b))=b; z=w ⇔ re(z)=re(w) ∧ im(z)=im(w); mk(a,b)+mk(c,d)=mk(a+c,b+d); mk(a,b)·mk(c,d)=mk(ac-bd,ad+bc); 0=mk(0,0); 1=mk(1,0); i=mk(0,1)

**basisKind:** extensional-structural-definition

**basisScope:** Equality is coordinate equality. No compatible linear ordered-field structure, floating-point rounding or branch convention for complex transcendental functions is assumed. Division requires nonzero pair.

**specializationNote:** Instantiate Field at pairs of reals with the displayed complex addition/multiplication and nonzero inverse. ProductType describes the carrier, not the multiplication.

**verificationObligation:** Map carrier, equality, operation definedness and stated profile to the target API or proof context.; Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.; Model coverage does not establish every recorded claim or an implementation refinement.

**reviewStatus:** Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-ComplexNumber-construct"></a>

### construct

`urn:csabs:operation/ComplexNumber-construct`

**signature:** mk : ℝ×ℝ→ℂ

**description:** mk(a,b)=a+bi.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Equality is coordinate equality. No compatible linear ordered-field structure, floating-point rounding or branch convention for complex transcendental functions is assumed. Division requires nonzero pair.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** mk(a,b)=a+bi.

**source:** [Mathlib pinned definitions: Basic/Complex/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Basic/Complex/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Complex.re, Complex.im, Complex.eta, Complex.ext and field arithmetic

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-ComplexNumber-coordinates"></a>

### coordinates

`urn:csabs:operation/ComplexNumber-coordinates`

**signature:** re,im : ℂ→ℝ

**description:** Return first and second coordinate.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Equality is coordinate equality. No compatible linear ordered-field structure, floating-point rounding or branch convention for complex transcendental functions is assumed. Division requires nonzero pair.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Return first and second coordinate.

**source:** [Mathlib pinned definitions: Basic/Complex/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Basic/Complex/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Complex.re, Complex.im, Complex.eta, Complex.ext and field arithmetic

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-ComplexNumber-add"></a>

### add

`urn:csabs:operation/ComplexNumber-add`

**signature:** add : ℂ×ℂ→ℂ

**description:** (a,b)+(c,d)=(a+c,b+d).

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Equality is coordinate equality. No compatible linear ordered-field structure, floating-point rounding or branch convention for complex transcendental functions is assumed. Division requires nonzero pair.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** (a,b)+(c,d)=(a+c,b+d).

**source:** [Mathlib pinned definitions: Basic/Complex/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Basic/Complex/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Complex.re, Complex.im, Complex.eta, Complex.ext and field arithmetic

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-ComplexNumber-multiply"></a>

### multiply

`urn:csabs:operation/ComplexNumber-multiply`

**signature:** multiply : ℂ×ℂ→ℂ

**description:** (a,b)(c,d)=(ac-bd,ad+bc).

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Equality is coordinate equality. No compatible linear ordered-field structure, floating-point rounding or branch convention for complex transcendental functions is assumed. Division requires nonzero pair.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** (a,b)(c,d)=(ac-bd,ad+bc).

**source:** [Mathlib pinned definitions: Basic/Complex/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Basic/Complex/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Complex.re, Complex.im, Complex.eta, Complex.ext and field arithmetic

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-ComplexNumber-inverse"></a>

### inverse

`urn:csabs:operation/ComplexNumber-inverse`

**signature:** inverse : (ℂ∖{0})→ℂ

**description:** (a,b)⁻¹=(a/(a²+b²),-b/(a²+b²)).

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Equality is coordinate equality. No compatible linear ordered-field structure, floating-point rounding or branch convention for complex transcendental functions is assumed. Division requires nonzero pair.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** (a,b)⁻¹=(a/(a²+b²),-b/(a²+b²)).

**source:** [Mathlib pinned definitions: Basic/Complex/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Basic/Complex/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Complex.re, Complex.im, Complex.eta, Complex.ext and field arithmetic

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-ComplexNumber-coordinates"></a>

### coordinates

`urn:csabs:axiom/ComplexNumber-coordinates`

**statement:** Defining requirement: re(mk(a,b))=a ∧ im(mk(a,b))=b; z=w ⇔ re(z)=re(w) ∧ im(z)=im(w)

**formalStatement:** re(mk(a,b))=a ∧ im(mk(a,b))=b; z=w ⇔ re(z)=re(w) ∧ im(z)=im(w)

**assumptions:** Equality is coordinate equality. No compatible linear ordered-field structure, floating-point rounding or branch convention for complex transcendental functions is assumed. Division requires nonzero pair.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Mathlib pinned definitions: Basic/Complex/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Basic/Complex/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Complex.re, Complex.im, Complex.eta, Complex.ext and field arithmetic

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-ComplexNumber-arithmetic"></a>

### arithmetic

`urn:csabs:axiom/ComplexNumber-arithmetic`

**statement:** Defining requirement: mk(a,b)+mk(c,d)=mk(a+c,b+d); mk(a,b)·mk(c,d)=mk(ac-bd,ad+bc)

**formalStatement:** mk(a,b)+mk(c,d)=mk(a+c,b+d); mk(a,b)·mk(c,d)=mk(ac-bd,ad+bc)

**assumptions:** Equality is coordinate equality. No compatible linear ordered-field structure, floating-point rounding or branch convention for complex transcendental functions is assumed. Division requires nonzero pair.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Mathlib pinned definitions: Basic/Complex/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Basic/Complex/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Complex.re, Complex.im, Complex.eta, Complex.ext and field arithmetic

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-ComplexNumber-unit"></a>

### unit

`urn:csabs:axiom/ComplexNumber-unit`

**statement:** Defining requirement: 0=mk(0,0); 1=mk(1,0); i=mk(0,1)

**formalStatement:** 0=mk(0,0); 1=mk(1,0); i=mk(0,1)

**assumptions:** Equality is coordinate equality. No compatible linear ordered-field structure, floating-point rounding or branch convention for complex transcendental functions is assumed. Division requires nonzero pair.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Mathlib pinned definitions: Basic/Complex/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Basic/Complex/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Complex.re, Complex.im, Complex.eta, Complex.ext and field arithmetic

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-ComplexNumber-eta"></a>

### eta

`urn:csabs:law/ComplexNumber-eta`

**statement:** mk(re(z),im(z))=z

**formalStatement:** mk(re(z),im(z))=z

**assumptions:** Equality is coordinate equality. No compatible linear ordered-field structure, floating-point rounding or branch convention for complex transcendental functions is assumed. Division requires nonzero pair.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [coordinates](ComplexNumber.md#node-urn-csabs-axiom-ComplexNumber-coordinates)

**proofSketch:** Use coordinate extensionality and projection computation.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Mathlib pinned definitions: Basic/Complex/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Basic/Complex/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Complex.re, Complex.im, Complex.eta, Complex.ext and field arithmetic

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ (z : Catalog.ComplexNumber), Complex.mk z.re z.im = z
```

**Source:** [`Catalog.CoreDataProofs.complex_eta`](../lean/Catalog/CoreData.lean); consulted 2026-11-12.

**Scope:** registered-witness-type

**Interpretation:** Complex is the structure with Real re/im fields. mk and projections are the catalog constructor and coordinates; coordinate equality is Lean structure equality.

**Limits:** Only the displayed proposition for this explicit interpretation. No proof of all catalog claims or of a software implementation; informal/formal correspondence remains reviewed metadata.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/ComplexNumber-coordinates": "Interpreted premise: re(mk(a,b))=a ∧ im(mk(a,b))=b; z=w ⇔ re(z)=re(w) ∧ im(z)=im(w). Complex is the structure with Real re/im fields. mk and projections are the catalog constructor and coordinates; coordinate equality is Lean structure equality."
}
```

## Theorems

<a id="node-urn-csabs-theorem-ComplexNumber-imaginary-square"></a>

### imaginary-square

`urn:csabs:theorem/ComplexNumber-imaginary-square`

**statement:** i·i=-1

**formalStatement:** i·i=-1

**assumptions:** Equality is coordinate equality. No compatible linear ordered-field structure, floating-point rounding or branch convention for complex transcendental functions is assumed. Division requires nonzero pair.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [arithmetic](ComplexNumber.md#node-urn-csabs-axiom-ComplexNumber-arithmetic); [unit](ComplexNumber.md#node-urn-csabs-axiom-ComplexNumber-unit)

**proofSketch:** Insert i=(0,1) into multiplication and compute both real coordinates.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Mathlib pinned definitions: Basic/Complex/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Basic/Complex/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Complex.re, Complex.im, Complex.eta, Complex.ext and field arithmetic

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Concept provenance

- [Mathlib pinned definitions: Basic/Complex/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Basic/Complex/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Complex.re, Complex.im, Complex.eta, Complex.ext and field arithmetic

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/ComplexNumber",
    "type": "Concept",
    "shortForm": "ComplexNumber",
    "fullName": "Exact complex number",
    "category": [
      "urn:csabs:category/numeric-computation"
    ],
    "kind": "urn:csabs:kind/data-type",
    "definition": "Pairs of exact real coordinates equipped with complex-field arithmetic.",
    "notation": "ℂ=ℝ×ℝ; (a,b)=a+bi",
    "requiresConcept": [
      "urn:csabs:concept/RealNumber",
      "urn:csabs:concept/Field",
      "urn:csabs:concept/ProductType"
    ],
    "relatedConcept": [],
    "hasOperation": [
      "urn:csabs:operation/ComplexNumber-construct",
      "urn:csabs:operation/ComplexNumber-coordinates",
      "urn:csabs:operation/ComplexNumber-add",
      "urn:csabs:operation/ComplexNumber-multiply",
      "urn:csabs:operation/ComplexNumber-inverse"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/ComplexNumber-coordinates",
      "urn:csabs:axiom/ComplexNumber-arithmetic",
      "urn:csabs:axiom/ComplexNumber-unit"
    ],
    "hasLaw": [
      "urn:csabs:law/ComplexNumber-eta"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/ComplexNumber-imaginary-square"
    ],
    "axiomBasis": "re(mk(a,b))=a ∧ im(mk(a,b))=b; z=w ⇔ re(z)=re(w) ∧ im(z)=im(w); mk(a,b)+mk(c,d)=mk(a+c,b+d); mk(a,b)·mk(c,d)=mk(ac-bd,ad+bc); 0=mk(0,0); 1=mk(1,0); i=mk(0,1)",
    "basisKind": "extensional-structural-definition",
    "basisScope": "Equality is coordinate equality. No compatible linear ordered-field structure, floating-point rounding or branch convention for complex transcendental functions is assumed. Division requires nonzero pair.",
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Map carrier, equality, operation definedness and stated profile to the target API or proof context.",
      "Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.",
      "Model coverage does not establish every recorded claim or an implementation refinement."
    ],
    "reviewStatus": "Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.",
    "source": [
      "urn:csabs:source/mathlib-complex-core"
    ],
    "sourceLocator": "Complex.re, Complex.im, Complex.eta, Complex.ext and field arithmetic",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/Field"
    ],
    "specializationNote": "Instantiate Field at pairs of reals with the displayed complex addition/multiplication and nonzero inverse. ProductType describes the carrier, not the multiplication.",
    "leanFormulation": "abbrev ComplexNumber := Complex",
    "formulationSource": "urn:csabs:source/local-lean-CoreData",
    "formulationLocator": "Catalog.ComplexNumber",
    "formulationScope": "model",
    "leanModelMapping": "Complex with Real re/im, coordinate equality and the complex field instance. ℂ=ℝ×ℝ; (a,b)=a+bi. Equality is coordinate equality. No compatible linear ordered-field structure, floating-point rounding or branch convention for complex transcendental functions is assumed. Division requires nonzero pair.",
    "leanModelLimitations": "Compiled carrier and selected interface interpretation. Some catalog operations are specified mathematically rather than wrapped as Lean declarations; no blanket proof of claims, algorithms, parsing, liveness or complexity. See individual witnesses.",
    "mathematicalFormulation": "ℂ=ℝ×ℝ with (a,b)+(c,d)=(a+c,b+d), (a,b)(c,d)=(ac−bd,ad+bc), and i=(0,1). Equality is equality of both real coordinates."
  },
  {
    "id": "urn:csabs:operation/ComplexNumber-construct",
    "type": "Operation",
    "name": "construct",
    "signature": "mk : ℝ×ℝ→ℂ",
    "description": "mk(a,b)=a+bi.",
    "concept": "urn:csabs:concept/ComplexNumber",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Equality is coordinate equality. No compatible linear ordered-field structure, floating-point rounding or branch convention for complex transcendental functions is assumed. Division requires nonzero pair.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "mk(a,b)=a+bi.",
    "source": [
      "urn:csabs:source/mathlib-complex-core"
    ],
    "sourceLocator": "Complex.re, Complex.im, Complex.eta, Complex.ext and field arithmetic",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/ComplexNumber-coordinates",
    "type": "Operation",
    "name": "coordinates",
    "signature": "re,im : ℂ→ℝ",
    "description": "Return first and second coordinate.",
    "concept": "urn:csabs:concept/ComplexNumber",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Equality is coordinate equality. No compatible linear ordered-field structure, floating-point rounding or branch convention for complex transcendental functions is assumed. Division requires nonzero pair.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Return first and second coordinate.",
    "source": [
      "urn:csabs:source/mathlib-complex-core"
    ],
    "sourceLocator": "Complex.re, Complex.im, Complex.eta, Complex.ext and field arithmetic",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/ComplexNumber-add",
    "type": "Operation",
    "name": "add",
    "signature": "add : ℂ×ℂ→ℂ",
    "description": "(a,b)+(c,d)=(a+c,b+d).",
    "concept": "urn:csabs:concept/ComplexNumber",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Equality is coordinate equality. No compatible linear ordered-field structure, floating-point rounding or branch convention for complex transcendental functions is assumed. Division requires nonzero pair.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "(a,b)+(c,d)=(a+c,b+d).",
    "source": [
      "urn:csabs:source/mathlib-complex-core"
    ],
    "sourceLocator": "Complex.re, Complex.im, Complex.eta, Complex.ext and field arithmetic",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/ComplexNumber-multiply",
    "type": "Operation",
    "name": "multiply",
    "signature": "multiply : ℂ×ℂ→ℂ",
    "description": "(a,b)(c,d)=(ac-bd,ad+bc).",
    "concept": "urn:csabs:concept/ComplexNumber",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Equality is coordinate equality. No compatible linear ordered-field structure, floating-point rounding or branch convention for complex transcendental functions is assumed. Division requires nonzero pair.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "(a,b)(c,d)=(ac-bd,ad+bc).",
    "source": [
      "urn:csabs:source/mathlib-complex-core"
    ],
    "sourceLocator": "Complex.re, Complex.im, Complex.eta, Complex.ext and field arithmetic",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/ComplexNumber-inverse",
    "type": "Operation",
    "name": "inverse",
    "signature": "inverse : (ℂ∖{0})→ℂ",
    "description": "(a,b)⁻¹=(a/(a²+b²),-b/(a²+b²)).",
    "concept": "urn:csabs:concept/ComplexNumber",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Equality is coordinate equality. No compatible linear ordered-field structure, floating-point rounding or branch convention for complex transcendental functions is assumed. Division requires nonzero pair.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "(a,b)⁻¹=(a/(a²+b²),-b/(a²+b²)).",
    "source": [
      "urn:csabs:source/mathlib-complex-core"
    ],
    "sourceLocator": "Complex.re, Complex.im, Complex.eta, Complex.ext and field arithmetic",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/ComplexNumber-coordinates",
    "type": "Axiom",
    "name": "coordinates",
    "statement": "Defining requirement: re(mk(a,b))=a ∧ im(mk(a,b))=b; z=w ⇔ re(z)=re(w) ∧ im(z)=im(w)",
    "formalStatement": "re(mk(a,b))=a ∧ im(mk(a,b))=b; z=w ⇔ re(z)=re(w) ∧ im(z)=im(w)",
    "assumptions": [
      "Equality is coordinate equality. No compatible linear ordered-field structure, floating-point rounding or branch convention for complex transcendental functions is assumed. Division requires nonzero pair.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/ComplexNumber"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/mathlib-complex-core"
    ],
    "sourceLocator": "Complex.re, Complex.im, Complex.eta, Complex.ext and field arithmetic",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/ComplexNumber-arithmetic",
    "type": "Axiom",
    "name": "arithmetic",
    "statement": "Defining requirement: mk(a,b)+mk(c,d)=mk(a+c,b+d); mk(a,b)·mk(c,d)=mk(ac-bd,ad+bc)",
    "formalStatement": "mk(a,b)+mk(c,d)=mk(a+c,b+d); mk(a,b)·mk(c,d)=mk(ac-bd,ad+bc)",
    "assumptions": [
      "Equality is coordinate equality. No compatible linear ordered-field structure, floating-point rounding or branch convention for complex transcendental functions is assumed. Division requires nonzero pair.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/ComplexNumber"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/mathlib-complex-core"
    ],
    "sourceLocator": "Complex.re, Complex.im, Complex.eta, Complex.ext and field arithmetic",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/ComplexNumber-unit",
    "type": "Axiom",
    "name": "unit",
    "statement": "Defining requirement: 0=mk(0,0); 1=mk(1,0); i=mk(0,1)",
    "formalStatement": "0=mk(0,0); 1=mk(1,0); i=mk(0,1)",
    "assumptions": [
      "Equality is coordinate equality. No compatible linear ordered-field structure, floating-point rounding or branch convention for complex transcendental functions is assumed. Division requires nonzero pair.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/ComplexNumber"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/mathlib-complex-core"
    ],
    "sourceLocator": "Complex.re, Complex.im, Complex.eta, Complex.ext and field arithmetic",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/ComplexNumber-eta",
    "type": "Law",
    "name": "eta",
    "statement": "mk(re(z),im(z))=z",
    "formalStatement": "mk(re(z),im(z))=z",
    "assumptions": [
      "Equality is coordinate equality. No compatible linear ordered-field structure, floating-point rounding or branch convention for complex transcendental functions is assumed. Division requires nonzero pair.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/ComplexNumber"
    ],
    "dependsOn": [
      "urn:csabs:axiom/ComplexNumber-coordinates"
    ],
    "proofSketch": "Use coordinate extensionality and projection computation.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/mathlib-complex-core"
    ],
    "sourceLocator": "Complex.re, Complex.im, Complex.eta, Complex.ext and field arithmetic",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ (z : Catalog.ComplexNumber), Complex.mk z.re z.im = z",
    "formulationSource": "urn:csabs:source/local-lean-CoreData",
    "formulationLocator": "Catalog.CoreDataProofs.complex_eta",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Complex is the structure with Real re/im fields. mk and projections are the catalog constructor and coordinates; coordinate equality is Lean structure equality.",
    "leanModelLimitations": "Only the displayed proposition for this explicit interpretation. No proof of all catalog claims or of a software implementation; informal/formal correspondence remains reviewed metadata.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/ComplexNumber-coordinates\": \"Interpreted premise: re(mk(a,b))=a ∧ im(mk(a,b))=b; z=w ⇔ re(z)=re(w) ∧ im(z)=im(w). Complex is the structure with Real re/im fields. mk and projections are the catalog constructor and coordinates; coordinate equality is Lean structure equality.\"}"
  },
  {
    "id": "urn:csabs:theorem/ComplexNumber-imaginary-square",
    "type": "Theorem",
    "name": "imaginary-square",
    "statement": "i·i=-1",
    "formalStatement": "i·i=-1",
    "assumptions": [
      "Equality is coordinate equality. No compatible linear ordered-field structure, floating-point rounding or branch convention for complex transcendental functions is assumed. Division requires nonzero pair.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/ComplexNumber"
    ],
    "dependsOn": [
      "urn:csabs:axiom/ComplexNumber-arithmetic",
      "urn:csabs:axiom/ComplexNumber-unit"
    ],
    "proofSketch": "Insert i=(0,1) into multiplication and compute both real coordinates.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/mathlib-complex-core"
    ],
    "sourceLocator": "Complex.re, Complex.im, Complex.eta, Complex.ext and field arithmetic",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
