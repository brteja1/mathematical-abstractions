# Mathematical integers

The unbounded integers with exact arithmetic and the usual order.

**Notation:** (ℤ,+,−,×,<,0,1), with no finite range bound.

**Stable ID:** `urn:csabs:concept/MathematicalInteger`

**Categories:** Numeric computation, Algebra

**Kind:** Mathematical structure

**Related concepts:** [Fixed-width unsigned integer](FixedWidthUnsignedInteger.md), [Fixed-width signed integer](FixedWidthSignedInteger.md)

## Backlinks

- [Arbitrary Precision Integer](ArbitraryPrecisionInteger.md) — `requiresConcept`
- [Checked Integer](CheckedInteger.md) — `requiresConcept`
- [Fixed-width signed integer](FixedWidthSignedInteger.md) — `relatedConcept`
- [Fixed-width unsigned integer](FixedWidthUnsignedInteger.md) — `relatedConcept`
- [Floating-point type](FloatingPointType.md) — `relatedConcept`
- [Natural Number](NaturalNumber.md) — `requiresConcept`
- [Saturating Integer](SaturatingInteger.md) — `requiresConcept`

## Interface and scope

**axiomBasis:** Standard integers constructed from pairs of standard naturals modulo (a,b)~(c,d) iff a+d=c+b. Operations and order are induced by these pairs; exact unbounded arithmetic.

**basisKind:** derived-construction

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**verificationObligation:** Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

**provenanceStatus:** legacy-source-missing

## Operations

<a id="node-urn-csabs-operation-integer-add"></a>

### addition

`urn:csabs:operation/integer-add`

**signature:** + : ℤ×ℤ→ℤ

**description:** Exact unbounded integer addition.

<a id="node-urn-csabs-operation-integer-subtract"></a>

### subtraction

`urn:csabs:operation/integer-subtract`

**signature:** − : ℤ×ℤ→ℤ

**description:** Exact unbounded integer subtraction.

<a id="node-urn-csabs-operation-integer-multiply"></a>

### multiplication

`urn:csabs:operation/integer-multiply`

**signature:** × : ℤ×ℤ→ℤ

**description:** Exact unbounded integer multiplication.

<a id="node-urn-csabs-operation-integer-euclidean-divmod"></a>

### Euclidean divmod

`urn:csabs:operation/integer-euclidean-divmod`

**signature:** divmod : ℤ×(ℤ\{0})→ℤ×ℤ

**description:** Returns unique quotient q and remainder r such that a=bq+r and 0≤r<|b|.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-Integer-quotient"></a>

### quotient

`urn:csabs:axiom/Integer-quotient`

**statement:** An integer is a difference of two naturals modulo difference equality.

**formalStatement:** ℤ=(ℕ×ℕ)/~; (a,b)~(c,d) iff a+d=c+b

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Integer-pair-arithmetic"></a>

### pair-arithmetic

`urn:csabs:axiom/Integer-pair-arithmetic`

**statement:** Operations on difference classes are well-defined by these formulas.

**formalStatement:** [(a,b)]+[(c,d)]=[(a+c,b+d)]; −[(a,b)]=[(b,a)]; [(a,b)]·[(c,d)]=[(ac+bd,ad+bc)]

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Integer-order"></a>

### order

`urn:csabs:axiom/Integer-order`

**statement:** The order compares differences by cross addition.

**formalStatement:** [(a,b)]≤[(c,d)] iff a+d≤c+b; 0=[(0,0)]; 1=[(1,0)]

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

<a id="node-urn-csabs-law-integer-additive-abelian-group"></a>

### law/integer-additive-abelian-group

`urn:csabs:law/integer-additive-abelian-group`

**statement:** Integer addition is associative and commutative, has identity zero, and every integer has an additive inverse.

**formalStatement:** (ℤ,+,0) is an abelian group

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [quotient](Integer.md#node-urn-csabs-axiom-Integer-quotient); [pair-arithmetic](Integer.md#node-urn-csabs-axiom-Integer-pair-arithmetic); [order](Integer.md#node-urn-csabs-axiom-Integer-order)

**assumptions:** Use the explicit mathematical bases and typed carriers of the linked concepts.

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-law-integer-distributivity"></a>

### law/integer-distributivity

`urn:csabs:law/integer-distributivity`

**statement:** Integer multiplication distributes over addition.

**formalStatement:** a(b+c)=ab+ac

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [quotient](Integer.md#node-urn-csabs-axiom-Integer-quotient); [pair-arithmetic](Integer.md#node-urn-csabs-axiom-Integer-pair-arithmetic); [order](Integer.md#node-urn-csabs-axiom-Integer-order)

**assumptions:** Use the explicit mathematical bases and typed carriers of the linked concepts.

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-law-euclidean-division"></a>

### law/euclidean-division

`urn:csabs:law/euclidean-division`

**statement:** For b≠0 there are unique q,r with a=bq+r and 0≤r<|b|.

**formalStatement:** ∀a∈ℤ,b∈ℤ\{0} ∃!q,r∈ℤ: a=bq+r ∧ 0≤r<|b|

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [quotient](Integer.md#node-urn-csabs-axiom-Integer-quotient); [pair-arithmetic](Integer.md#node-urn-csabs-axiom-Integer-pair-arithmetic); [order](Integer.md#node-urn-csabs-axiom-Integer-order)

**assumptions:** Use the explicit mathematical bases and typed carriers of the linked concepts.

**provenanceStatus:** legacy-source-missing

## Theorems

<a id="node-urn-csabs-theorem-Integer-add-cancellation"></a>

### add-cancellation

`urn:csabs:theorem/Integer-add-cancellation`

**statement:** Exact integer addition satisfies cancellation.

**formalStatement:** a+b=a+c ⇒ b=c

**proofSketch:** Add the inverse of a on the left and simplify using the abelian-group laws of difference classes.

**assumptions:** The explicit basis, carriers, and side conditions stated for Integer apply.

**dependsOn:** [quotient](Integer.md#node-urn-csabs-axiom-Integer-quotient); [pair-arithmetic](Integer.md#node-urn-csabs-axiom-Integer-pair-arithmetic); [order](Integer.md#node-urn-csabs-axiom-Integer-order)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Concept provenance

Historical source gap retained; see `provenanceStatus` and the frozen baseline.

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/MathematicalInteger",
    "type": "Concept",
    "shortForm": "Integer",
    "fullName": "Mathematical integers",
    "category": [
      "urn:csabs:category/numeric-computation",
      "urn:csabs:category/algebra"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "The unbounded integers with exact arithmetic and the usual order.",
    "notation": "(ℤ,+,−,×,<,0,1), with no finite range bound.",
    "hasOperation": [
      "urn:csabs:operation/integer-add",
      "urn:csabs:operation/integer-subtract",
      "urn:csabs:operation/integer-multiply",
      "urn:csabs:operation/integer-euclidean-divmod"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/Integer-quotient",
      "urn:csabs:axiom/Integer-pair-arithmetic",
      "urn:csabs:axiom/Integer-order"
    ],
    "hasLaw": [
      "urn:csabs:law/integer-additive-abelian-group",
      "urn:csabs:law/integer-distributivity",
      "urn:csabs:law/euclidean-division"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/Integer-add-cancellation"
    ],
    "relatedConcept": [
      "urn:csabs:concept/FixedWidthUnsignedInteger",
      "urn:csabs:concept/FixedWidthSignedInteger"
    ],
    "coverageStatus": "basis-reviewed",
    "requiresConcept": [],
    "verificationObligation": [
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Standard integers constructed from pairs of standard naturals modulo (a,b)~(c,d) iff a+d=c+b. Operations and order are induced by these pairs; exact unbounded arithmetic.",
    "basisKind": "derived-construction",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:operation/integer-add",
    "type": "Operation",
    "name": "addition",
    "signature": "+ : ℤ×ℤ→ℤ",
    "description": "Exact unbounded integer addition.",
    "concept": "urn:csabs:concept/MathematicalInteger"
  },
  {
    "id": "urn:csabs:operation/integer-subtract",
    "type": "Operation",
    "name": "subtraction",
    "signature": "− : ℤ×ℤ→ℤ",
    "description": "Exact unbounded integer subtraction.",
    "concept": "urn:csabs:concept/MathematicalInteger"
  },
  {
    "id": "urn:csabs:operation/integer-multiply",
    "type": "Operation",
    "name": "multiplication",
    "signature": "× : ℤ×ℤ→ℤ",
    "description": "Exact unbounded integer multiplication.",
    "concept": "urn:csabs:concept/MathematicalInteger"
  },
  {
    "id": "urn:csabs:operation/integer-euclidean-divmod",
    "type": "Operation",
    "name": "Euclidean divmod",
    "signature": "divmod : ℤ×(ℤ\\{0})→ℤ×ℤ",
    "description": "Returns unique quotient q and remainder r such that a=bq+r and 0≤r<|b|.",
    "concept": "urn:csabs:concept/MathematicalInteger"
  },
  {
    "id": "urn:csabs:axiom/Integer-quotient",
    "type": "Axiom",
    "name": "quotient",
    "statement": "An integer is a difference of two naturals modulo difference equality.",
    "formalStatement": "ℤ=(ℕ×ℕ)/~; (a,b)~(c,d) iff a+d=c+b",
    "appliesTo": [
      "urn:csabs:concept/MathematicalInteger"
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
    "id": "urn:csabs:axiom/Integer-pair-arithmetic",
    "type": "Axiom",
    "name": "pair-arithmetic",
    "statement": "Operations on difference classes are well-defined by these formulas.",
    "formalStatement": "[(a,b)]+[(c,d)]=[(a+c,b+d)]; −[(a,b)]=[(b,a)]; [(a,b)]·[(c,d)]=[(ac+bd,ad+bc)]",
    "appliesTo": [
      "urn:csabs:concept/MathematicalInteger"
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
    "id": "urn:csabs:axiom/Integer-order",
    "type": "Axiom",
    "name": "order",
    "statement": "The order compares differences by cross addition.",
    "formalStatement": "[(a,b)]≤[(c,d)] iff a+d≤c+b; 0=[(0,0)]; 1=[(1,0)]",
    "appliesTo": [
      "urn:csabs:concept/MathematicalInteger"
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
    "id": "urn:csabs:law/integer-additive-abelian-group",
    "type": "Law",
    "statement": "Integer addition is associative and commutative, has identity zero, and every integer has an additive inverse.",
    "formalStatement": "(ℤ,+,0) is an abelian group",
    "appliesTo": [
      "urn:csabs:concept/MathematicalInteger"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/Integer-quotient",
      "urn:csabs:axiom/Integer-pair-arithmetic",
      "urn:csabs:axiom/Integer-order"
    ],
    "assumptions": [
      "Use the explicit mathematical bases and typed carriers of the linked concepts."
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:law/integer-distributivity",
    "type": "Law",
    "statement": "Integer multiplication distributes over addition.",
    "formalStatement": "a(b+c)=ab+ac",
    "appliesTo": [
      "urn:csabs:concept/MathematicalInteger"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/Integer-quotient",
      "urn:csabs:axiom/Integer-pair-arithmetic",
      "urn:csabs:axiom/Integer-order"
    ],
    "assumptions": [
      "Use the explicit mathematical bases and typed carriers of the linked concepts."
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:law/euclidean-division",
    "type": "Law",
    "statement": "For b≠0 there are unique q,r with a=bq+r and 0≤r<|b|.",
    "formalStatement": "∀a∈ℤ,b∈ℤ\\{0} ∃!q,r∈ℤ: a=bq+r ∧ 0≤r<|b|",
    "appliesTo": [
      "urn:csabs:concept/MathematicalInteger"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/Integer-quotient",
      "urn:csabs:axiom/Integer-pair-arithmetic",
      "urn:csabs:axiom/Integer-order"
    ],
    "assumptions": [
      "Use the explicit mathematical bases and typed carriers of the linked concepts."
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/Integer-add-cancellation",
    "type": "Theorem",
    "name": "add-cancellation",
    "statement": "Exact integer addition satisfies cancellation.",
    "formalStatement": "a+b=a+c ⇒ b=c",
    "proofSketch": "Add the inverse of a on the left and simplify using the abelian-group laws of difference classes.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for Integer apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/MathematicalInteger"
    ],
    "dependsOn": [
      "urn:csabs:axiom/Integer-quotient",
      "urn:csabs:axiom/Integer-pair-arithmetic",
      "urn:csabs:axiom/Integer-order"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
