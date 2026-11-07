# Semigroup

A set with a closed associative binary operation.

**Notation:** (S,·), with ∀x,y,z∈S: (x·y)·z=x·(y·z).

**Stable ID:** `urn:csabs:concept/Semigroup`

**Categories:** Algebra

**Kind:** Mathematical structure

## Backlinks

- [Monoid](Monoid.md) — `requiresConcept`
- [Monoid](Monoid.md) — `specializationOf`

## Interface and scope

**axiomBasis:** Nonempty carrier with closed binary multiplication; associativity. Multiplication need not commute.

**basisKind:** axiomatic-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**verificationObligation:** Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-semigroup-product"></a>

### binary operation

`urn:csabs:operation/semigroup-product`

**signature:** · : S×S→S

**description:** Combines two carrier elements; closure is required.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-semigroup-closure"></a>

### semigroup-closure

`urn:csabs:axiom/semigroup-closure`

**statement:** Combining two carrier elements yields a carrier element.

**formalStatement:** ∀x,y∈S: x·y∈S

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

**assumptions:** Use the linked concept’s explicit basis and carrier conventions.

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-semigroup-associativity"></a>

### semigroup-associativity

`urn:csabs:axiom/semigroup-associativity`

**statement:** The binary operation is associative.

**formalStatement:** ∀x,y,z∈S: (x·y)·z=x·(y·z)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

**assumptions:** Use the linked concept’s explicit basis and carrier conventions.

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Semigroup-closed-carrier"></a>

### closed-carrier

`urn:csabs:axiom/Semigroup-closed-carrier`

**statement:** The binary operation is total on a nonempty carrier.

**formalStatement:** S≠∅; ·:S×S→S

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Semigroup-associative"></a>

### associative

`urn:csabs:axiom/Semigroup-associative`

**statement:** Multiplication is associative.

**formalStatement:** (x·y)·z=x·(y·z)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-Semigroup-four-factor-reassociation"></a>

### four-factor-reassociation

`urn:csabs:theorem/Semigroup-four-factor-reassociation`

**statement:** All parenthesizations of four ordered factors agree.

**formalStatement:** ((ab)c)d=(ab)(cd)=a(b(cd))

**proofSketch:** Apply associativity repeatedly without exchanging factors.

**assumptions:** The explicit basis, carriers, and side conditions stated for Semigroup apply.

**dependsOn:** [semigroup-closure](Semigroup.md#node-urn-csabs-axiom-semigroup-closure); [semigroup-associativity](Semigroup.md#node-urn-csabs-axiom-semigroup-associativity); [closed-carrier](Semigroup.md#node-urn-csabs-axiom-Semigroup-closed-carrier); [associative](Semigroup.md#node-urn-csabs-axiom-Semigroup-associative)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Concept provenance

- [Mathlib group definitions](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Defs.html); sourceRole: reference-for-selected-basis

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/Semigroup",
    "type": "Concept",
    "shortForm": "Semigroup",
    "fullName": "Semigroup",
    "category": [
      "urn:csabs:category/algebra"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "A set with a closed associative binary operation.",
    "notation": "(S,·), with ∀x,y,z∈S: (x·y)·z=x·(y·z).",
    "hasOperation": [
      "urn:csabs:operation/semigroup-product"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/semigroup-closure",
      "urn:csabs:axiom/semigroup-associativity",
      "urn:csabs:axiom/Semigroup-closed-carrier",
      "urn:csabs:axiom/Semigroup-associative"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/Semigroup-four-factor-reassociation"
    ],
    "specializationOf": [],
    "coverageStatus": "basis-reviewed",
    "requiresConcept": [],
    "verificationObligation": [
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Nonempty carrier with closed binary multiplication; associativity. Multiplication need not commute.",
    "basisKind": "axiomatic-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "source": [
      "urn:csabs:source/mathlib-group"
    ]
  },
  {
    "id": "urn:csabs:operation/semigroup-product",
    "type": "Operation",
    "name": "binary operation",
    "signature": "· : S×S→S",
    "description": "Combines two carrier elements; closure is required.",
    "concept": "urn:csabs:concept/Semigroup"
  },
  {
    "id": "urn:csabs:axiom/semigroup-closure",
    "type": "Axiom",
    "statement": "Combining two carrier elements yields a carrier element.",
    "formalStatement": "∀x,y∈S: x·y∈S",
    "appliesTo": [
      "urn:csabs:concept/Semigroup"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law",
    "name": "semigroup-closure",
    "assumptions": [
      "Use the linked concept’s explicit basis and carrier conventions."
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/semigroup-associativity",
    "type": "Axiom",
    "statement": "The binary operation is associative.",
    "formalStatement": "∀x,y,z∈S: (x·y)·z=x·(y·z)",
    "appliesTo": [
      "urn:csabs:concept/Semigroup"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law",
    "name": "semigroup-associativity",
    "assumptions": [
      "Use the linked concept’s explicit basis and carrier conventions."
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/Semigroup-closed-carrier",
    "type": "Axiom",
    "name": "closed-carrier",
    "statement": "The binary operation is total on a nonempty carrier.",
    "formalStatement": "S≠∅; ·:S×S→S",
    "appliesTo": [
      "urn:csabs:concept/Semigroup"
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
    "id": "urn:csabs:axiom/Semigroup-associative",
    "type": "Axiom",
    "name": "associative",
    "statement": "Multiplication is associative.",
    "formalStatement": "(x·y)·z=x·(y·z)",
    "appliesTo": [
      "urn:csabs:concept/Semigroup"
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
    "id": "urn:csabs:theorem/Semigroup-four-factor-reassociation",
    "type": "Theorem",
    "name": "four-factor-reassociation",
    "statement": "All parenthesizations of four ordered factors agree.",
    "formalStatement": "((ab)c)d=(ab)(cd)=a(b(cd))",
    "proofSketch": "Apply associativity repeatedly without exchanging factors.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for Semigroup apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/Semigroup"
    ],
    "dependsOn": [
      "urn:csabs:axiom/semigroup-closure",
      "urn:csabs:axiom/semigroup-associativity",
      "urn:csabs:axiom/Semigroup-closed-carrier",
      "urn:csabs:axiom/Semigroup-associative"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
