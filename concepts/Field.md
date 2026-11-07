# Field

A commutative unital ring with distinct zero and one in which each nonzero element has a multiplicative inverse.

**Notation:** (F,+,·,0,1), 0≠1; ∀x∈F\{0} ∃x⁻¹: x·x⁻¹=1.

**Stable ID:** `urn:csabs:concept/Field`

**Categories:** Algebra, Numeric computation

**Kind:** Mathematical structure

**Prerequisites:** [Unital ring (convention stated)](Ring.md)

**Specializes:** [Unital ring (convention stated)](Ring.md)

## Backlinks

- [Finite rectangular matrix over a field](Matrix.md) — `requiresConcept`
- [Modular Integer](ModularInteger.md) — `requiresConcept`
- [Vector space over a field](VectorSpace.md) — `requiresConcept`

## Interface and scope

**axiomBasis:** Unital field: total addition and multiplication; additive abelian group; multiplicative monoid; both distributivities. Multiplication commutative, 0≠1, every nonzero element invertible.

**basisKind:** axiomatic-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**verificationObligation:** Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

**provenanceStatus:** legacy-source-missing

## Operations

<a id="node-urn-csabs-operation-field-addition"></a>

### addition

`urn:csabs:operation/field-addition`

**signature:** + : F×F→F

**description:** Addition in the field's additive abelian group.

<a id="node-urn-csabs-operation-field-multiplication"></a>

### multiplication

`urn:csabs:operation/field-multiplication`

**signature:** · : F×F→F

**description:** Commutative field multiplication.

<a id="node-urn-csabs-operation-field-inverse"></a>

### multiplicative inverse

`urn:csabs:operation/field-inverse`

**signature:** inv : F\{0}→F

**description:** Returns the multiplicative inverse for nonzero inputs.

**precondition:** x ≠ 0

## Axioms and defining rules

<a id="node-urn-csabs-axiom-field-commutative-ring"></a>

### field-commutative-ring

`urn:csabs:axiom/field-commutative-ring`

**statement:** The ring operations satisfy the commutative unital ring laws and zero differs from one.

**formalStatement:** 0≠1

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

**assumptions:** Use the linked concept’s explicit basis and carrier conventions.

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-field-nonzero-inverses"></a>

### field-nonzero-inverses

`urn:csabs:axiom/field-nonzero-inverses`

**statement:** Every nonzero field element has a multiplicative inverse.

**formalStatement:** ∀x∈F\{0} ∃y∈F: xy=1

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

**assumptions:** Use the linked concept’s explicit basis and carrier conventions.

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Field-closure"></a>

### closure

`urn:csabs:axiom/Field-closure`

**statement:** The carrier contains the constants and is closed under both operations.

**formalStatement:** 0,1∈S; +,·:S×S→S

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Field-add-associative"></a>

### add-associative

`urn:csabs:axiom/Field-add-associative`

**statement:** Addition is associative.

**formalStatement:** (x+y)+z=x+(y+z)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Field-add-commutative"></a>

### add-commutative

`urn:csabs:axiom/Field-add-commutative`

**statement:** Addition commutes.

**formalStatement:** x+y=y+x

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Field-add-zero"></a>

### add-zero

`urn:csabs:axiom/Field-add-zero`

**statement:** Zero is the additive identity.

**formalStatement:** 0+x=x; x+0=x

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Field-mul-associative"></a>

### mul-associative

`urn:csabs:axiom/Field-mul-associative`

**statement:** Multiplication is associative.

**formalStatement:** (xy)z=x(yz)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Field-mul-unit"></a>

### mul-unit

`urn:csabs:axiom/Field-mul-unit`

**statement:** One is the multiplicative identity.

**formalStatement:** 1x=x; x1=x

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Field-distributive"></a>

### distributive

`urn:csabs:axiom/Field-distributive`

**statement:** Multiplication distributes over addition on both sides.

**formalStatement:** x(y+z)=xy+xz; (x+y)z=xz+yz

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Field-add-inverse"></a>

### add-inverse

`urn:csabs:axiom/Field-add-inverse`

**statement:** Every element has an additive inverse.

**formalStatement:** neg:S→S; x+neg(x)=0; neg(x)+x=0

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Field-nontrivial"></a>

### nontrivial

`urn:csabs:axiom/Field-nontrivial`

**statement:** Zero and one are distinct.

**formalStatement:** 0≠1

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Field-mul-commutative"></a>

### mul-commutative

`urn:csabs:axiom/Field-mul-commutative`

**statement:** Multiplication commutes.

**formalStatement:** xy=yx

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Field-nonzero-inverse"></a>

### nonzero-inverse

`urn:csabs:axiom/Field-nonzero-inverse`

**statement:** Nonzero elements admit inverses.

**formalStatement:** ∀x≠0 ∃y:xy=yx=1

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-Field-nonzero-cancellation"></a>

### nonzero-cancellation

`urn:csabs:theorem/Field-nonzero-cancellation`

**statement:** A nonzero multiplicative factor cancels.

**formalStatement:** a≠0 ∧ ax=ay ⇒ x=y

**proofSketch:** Multiply by the inverse of a and use associativity and the multiplicative identity.

**assumptions:** The explicit basis, carriers, and side conditions stated for Field apply.

**dependsOn:** [field-commutative-ring](Field.md#node-urn-csabs-axiom-field-commutative-ring); [field-nonzero-inverses](Field.md#node-urn-csabs-axiom-field-nonzero-inverses); [closure](Field.md#node-urn-csabs-axiom-Field-closure); [add-associative](Field.md#node-urn-csabs-axiom-Field-add-associative); [add-commutative](Field.md#node-urn-csabs-axiom-Field-add-commutative); [add-zero](Field.md#node-urn-csabs-axiom-Field-add-zero); [mul-associative](Field.md#node-urn-csabs-axiom-Field-mul-associative); [mul-unit](Field.md#node-urn-csabs-axiom-Field-mul-unit); [distributive](Field.md#node-urn-csabs-axiom-Field-distributive); [add-inverse](Field.md#node-urn-csabs-axiom-Field-add-inverse); [nontrivial](Field.md#node-urn-csabs-axiom-Field-nontrivial); [mul-commutative](Field.md#node-urn-csabs-axiom-Field-mul-commutative); [nonzero-inverse](Field.md#node-urn-csabs-axiom-Field-nonzero-inverse)

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
    "id": "urn:csabs:concept/Field",
    "type": "Concept",
    "shortForm": "Field",
    "fullName": "Field",
    "category": [
      "urn:csabs:category/algebra",
      "urn:csabs:category/numeric-computation"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "A commutative unital ring with distinct zero and one in which each nonzero element has a multiplicative inverse.",
    "notation": "(F,+,·,0,1), 0≠1; ∀x∈F\\{0} ∃x⁻¹: x·x⁻¹=1.",
    "hasOperation": [
      "urn:csabs:operation/field-addition",
      "urn:csabs:operation/field-multiplication",
      "urn:csabs:operation/field-inverse"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/field-commutative-ring",
      "urn:csabs:axiom/field-nonzero-inverses",
      "urn:csabs:axiom/Field-closure",
      "urn:csabs:axiom/Field-add-associative",
      "urn:csabs:axiom/Field-add-commutative",
      "urn:csabs:axiom/Field-add-zero",
      "urn:csabs:axiom/Field-mul-associative",
      "urn:csabs:axiom/Field-mul-unit",
      "urn:csabs:axiom/Field-distributive",
      "urn:csabs:axiom/Field-add-inverse",
      "urn:csabs:axiom/Field-nontrivial",
      "urn:csabs:axiom/Field-mul-commutative",
      "urn:csabs:axiom/Field-nonzero-inverse"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/Field-nonzero-cancellation"
    ],
    "specializationOf": [
      "urn:csabs:concept/Ring"
    ],
    "coverageStatus": "basis-reviewed",
    "requiresConcept": [
      "urn:csabs:concept/Ring"
    ],
    "verificationObligation": [
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Unital field: total addition and multiplication; additive abelian group; multiplicative monoid; both distributivities. Multiplication commutative, 0≠1, every nonzero element invertible.",
    "basisKind": "axiomatic-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:operation/field-addition",
    "type": "Operation",
    "name": "addition",
    "signature": "+ : F×F→F",
    "description": "Addition in the field's additive abelian group.",
    "concept": "urn:csabs:concept/Field"
  },
  {
    "id": "urn:csabs:operation/field-multiplication",
    "type": "Operation",
    "name": "multiplication",
    "signature": "· : F×F→F",
    "description": "Commutative field multiplication.",
    "concept": "urn:csabs:concept/Field"
  },
  {
    "id": "urn:csabs:operation/field-inverse",
    "type": "Operation",
    "name": "multiplicative inverse",
    "signature": "inv : F\\{0}→F",
    "description": "Returns the multiplicative inverse for nonzero inputs.",
    "precondition": "x ≠ 0",
    "concept": "urn:csabs:concept/Field"
  },
  {
    "id": "urn:csabs:axiom/field-commutative-ring",
    "type": "Axiom",
    "statement": "The ring operations satisfy the commutative unital ring laws and zero differs from one.",
    "formalStatement": "0≠1",
    "appliesTo": [
      "urn:csabs:concept/Field"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law",
    "name": "field-commutative-ring",
    "assumptions": [
      "Use the linked concept’s explicit basis and carrier conventions."
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/field-nonzero-inverses",
    "type": "Axiom",
    "statement": "Every nonzero field element has a multiplicative inverse.",
    "formalStatement": "∀x∈F\\{0} ∃y∈F: xy=1",
    "appliesTo": [
      "urn:csabs:concept/Field"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law",
    "name": "field-nonzero-inverses",
    "assumptions": [
      "Use the linked concept’s explicit basis and carrier conventions."
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/Field-closure",
    "type": "Axiom",
    "name": "closure",
    "statement": "The carrier contains the constants and is closed under both operations.",
    "formalStatement": "0,1∈S; +,·:S×S→S",
    "appliesTo": [
      "urn:csabs:concept/Field"
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
    "id": "urn:csabs:axiom/Field-add-associative",
    "type": "Axiom",
    "name": "add-associative",
    "statement": "Addition is associative.",
    "formalStatement": "(x+y)+z=x+(y+z)",
    "appliesTo": [
      "urn:csabs:concept/Field"
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
    "id": "urn:csabs:axiom/Field-add-commutative",
    "type": "Axiom",
    "name": "add-commutative",
    "statement": "Addition commutes.",
    "formalStatement": "x+y=y+x",
    "appliesTo": [
      "urn:csabs:concept/Field"
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
    "id": "urn:csabs:axiom/Field-add-zero",
    "type": "Axiom",
    "name": "add-zero",
    "statement": "Zero is the additive identity.",
    "formalStatement": "0+x=x; x+0=x",
    "appliesTo": [
      "urn:csabs:concept/Field"
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
    "id": "urn:csabs:axiom/Field-mul-associative",
    "type": "Axiom",
    "name": "mul-associative",
    "statement": "Multiplication is associative.",
    "formalStatement": "(xy)z=x(yz)",
    "appliesTo": [
      "urn:csabs:concept/Field"
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
    "id": "urn:csabs:axiom/Field-mul-unit",
    "type": "Axiom",
    "name": "mul-unit",
    "statement": "One is the multiplicative identity.",
    "formalStatement": "1x=x; x1=x",
    "appliesTo": [
      "urn:csabs:concept/Field"
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
    "id": "urn:csabs:axiom/Field-distributive",
    "type": "Axiom",
    "name": "distributive",
    "statement": "Multiplication distributes over addition on both sides.",
    "formalStatement": "x(y+z)=xy+xz; (x+y)z=xz+yz",
    "appliesTo": [
      "urn:csabs:concept/Field"
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
    "id": "urn:csabs:axiom/Field-add-inverse",
    "type": "Axiom",
    "name": "add-inverse",
    "statement": "Every element has an additive inverse.",
    "formalStatement": "neg:S→S; x+neg(x)=0; neg(x)+x=0",
    "appliesTo": [
      "urn:csabs:concept/Field"
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
    "id": "urn:csabs:axiom/Field-nontrivial",
    "type": "Axiom",
    "name": "nontrivial",
    "statement": "Zero and one are distinct.",
    "formalStatement": "0≠1",
    "appliesTo": [
      "urn:csabs:concept/Field"
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
    "id": "urn:csabs:axiom/Field-mul-commutative",
    "type": "Axiom",
    "name": "mul-commutative",
    "statement": "Multiplication commutes.",
    "formalStatement": "xy=yx",
    "appliesTo": [
      "urn:csabs:concept/Field"
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
    "id": "urn:csabs:axiom/Field-nonzero-inverse",
    "type": "Axiom",
    "name": "nonzero-inverse",
    "statement": "Nonzero elements admit inverses.",
    "formalStatement": "∀x≠0 ∃y:xy=yx=1",
    "appliesTo": [
      "urn:csabs:concept/Field"
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
    "id": "urn:csabs:theorem/Field-nonzero-cancellation",
    "type": "Theorem",
    "name": "nonzero-cancellation",
    "statement": "A nonzero multiplicative factor cancels.",
    "formalStatement": "a≠0 ∧ ax=ay ⇒ x=y",
    "proofSketch": "Multiply by the inverse of a and use associativity and the multiplicative identity.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for Field apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/Field"
    ],
    "dependsOn": [
      "urn:csabs:axiom/field-commutative-ring",
      "urn:csabs:axiom/field-nonzero-inverses",
      "urn:csabs:axiom/Field-closure",
      "urn:csabs:axiom/Field-add-associative",
      "urn:csabs:axiom/Field-add-commutative",
      "urn:csabs:axiom/Field-add-zero",
      "urn:csabs:axiom/Field-mul-associative",
      "urn:csabs:axiom/Field-mul-unit",
      "urn:csabs:axiom/Field-distributive",
      "urn:csabs:axiom/Field-add-inverse",
      "urn:csabs:axiom/Field-nontrivial",
      "urn:csabs:axiom/Field-mul-commutative",
      "urn:csabs:axiom/Field-nonzero-inverse"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
