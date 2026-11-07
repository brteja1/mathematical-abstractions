# Semiring

A ring-like structure whose addition is a commutative monoid rather than a group, so additive inverses are not required.

**Notation:** (S,+,·,0,1): additive commutative monoid; multiplicative monoid; distributivity and zero annihilation.

**Stable ID:** `urn:csabs:concept/Semiring`

**Categories:** Algebra

**Kind:** Mathematical structure

## Backlinks

- [Unital ring (convention stated)](Ring.md) — `specializationOf`

## Interface and scope

**axiomBasis:** Unital semiring: total addition and multiplication; additive commutative monoid; multiplicative monoid; both distributivities. Multiplication need not commute; 0=1 is permitted.

**basisKind:** axiomatic-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**convention:** This entry uses the unital convention; variants must be separate entries.

**verificationObligation:** Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

**provenanceStatus:** legacy-source-missing

## Operations

<a id="node-urn-csabs-operation-semiring-addition"></a>

### addition

`urn:csabs:operation/semiring-addition`

**signature:** + : S×S→S

**description:** Commutative monoid operation; additive inverses are not required.

<a id="node-urn-csabs-operation-semiring-multiplication"></a>

### multiplication

`urn:csabs:operation/semiring-multiplication`

**signature:** · : S×S→S

**description:** Associative multiplication with identity under this entry's convention.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-semiring-additive-monoid"></a>

### semiring-additive-monoid

`urn:csabs:axiom/semiring-additive-monoid`

**statement:** Addition forms a commutative monoid; additive inverses are not required.

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

**formalStatement:** Addition forms a commutative monoid; additive inverses are not required.

**assumptions:** Use the linked concept’s explicit basis and carrier conventions.

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-semiring-multiplicative-monoid"></a>

### semiring-multiplicative-monoid

`urn:csabs:axiom/semiring-multiplicative-monoid`

**statement:** Multiplication forms a monoid under the stated unital convention.

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

**formalStatement:** Multiplication forms a monoid under the stated unital convention.

**assumptions:** Use the linked concept’s explicit basis and carrier conventions.

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-semiring-distributivity"></a>

### semiring-distributivity

`urn:csabs:axiom/semiring-distributivity`

**statement:** Multiplication distributes over addition on both sides.

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

**formalStatement:** Multiplication distributes over addition on both sides.

**assumptions:** Use the linked concept’s explicit basis and carrier conventions.

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-semiring-zero-annihilation"></a>

### semiring-zero-annihilation

`urn:csabs:axiom/semiring-zero-annihilation`

**statement:** Zero annihilates multiplication.

**formalStatement:** 0·x=x·0=0

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

**assumptions:** Use the linked concept’s explicit basis and carrier conventions.

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Semiring-closure"></a>

### closure

`urn:csabs:axiom/Semiring-closure`

**statement:** The carrier contains the constants and is closed under both operations.

**formalStatement:** 0,1∈S; +,·:S×S→S

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Semiring-add-associative"></a>

### add-associative

`urn:csabs:axiom/Semiring-add-associative`

**statement:** Addition is associative.

**formalStatement:** (x+y)+z=x+(y+z)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Semiring-add-commutative"></a>

### add-commutative

`urn:csabs:axiom/Semiring-add-commutative`

**statement:** Addition commutes.

**formalStatement:** x+y=y+x

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Semiring-add-zero"></a>

### add-zero

`urn:csabs:axiom/Semiring-add-zero`

**statement:** Zero is the additive identity.

**formalStatement:** 0+x=x; x+0=x

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Semiring-mul-associative"></a>

### mul-associative

`urn:csabs:axiom/Semiring-mul-associative`

**statement:** Multiplication is associative.

**formalStatement:** (xy)z=x(yz)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Semiring-mul-unit"></a>

### mul-unit

`urn:csabs:axiom/Semiring-mul-unit`

**statement:** One is the multiplicative identity.

**formalStatement:** 1x=x; x1=x

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Semiring-distributive"></a>

### distributive

`urn:csabs:axiom/Semiring-distributive`

**statement:** Multiplication distributes over addition on both sides.

**formalStatement:** x(y+z)=xy+xz; (x+y)z=xz+yz

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Semiring-zero-absorption"></a>

### zero-absorption

`urn:csabs:axiom/Semiring-zero-absorption`

**statement:** Multiplication by zero gives zero.

**formalStatement:** 0x=0; x0=0

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-Semiring-finite-distribution"></a>

### finite-distribution

`urn:csabs:theorem/Semiring-finite-distribution`

**statement:** Multiplication distributes over finite sums, including the empty sum.

**formalStatement:** a·Σᵢ bᵢ=Σᵢ(a·bᵢ); (Σᵢ bᵢ)·a=Σᵢ(bᵢ·a)

**proofSketch:** Induct on the finite list; use zero annihilation at the empty list.

**assumptions:** The explicit basis, carriers, and side conditions stated for Semiring apply.

**dependsOn:** [semiring-additive-monoid](Semiring.md#node-urn-csabs-axiom-semiring-additive-monoid); [semiring-multiplicative-monoid](Semiring.md#node-urn-csabs-axiom-semiring-multiplicative-monoid); [semiring-distributivity](Semiring.md#node-urn-csabs-axiom-semiring-distributivity); [semiring-zero-annihilation](Semiring.md#node-urn-csabs-axiom-semiring-zero-annihilation); [closure](Semiring.md#node-urn-csabs-axiom-Semiring-closure); [add-associative](Semiring.md#node-urn-csabs-axiom-Semiring-add-associative); [add-commutative](Semiring.md#node-urn-csabs-axiom-Semiring-add-commutative); [add-zero](Semiring.md#node-urn-csabs-axiom-Semiring-add-zero); [mul-associative](Semiring.md#node-urn-csabs-axiom-Semiring-mul-associative); [mul-unit](Semiring.md#node-urn-csabs-axiom-Semiring-mul-unit); [distributive](Semiring.md#node-urn-csabs-axiom-Semiring-distributive); [zero-absorption](Semiring.md#node-urn-csabs-axiom-Semiring-zero-absorption)

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
    "id": "urn:csabs:concept/Semiring",
    "type": "Concept",
    "shortForm": "Semiring",
    "fullName": "Semiring",
    "category": [
      "urn:csabs:category/algebra"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "A ring-like structure whose addition is a commutative monoid rather than a group, so additive inverses are not required.",
    "notation": "(S,+,·,0,1): additive commutative monoid; multiplicative monoid; distributivity and zero annihilation.",
    "hasOperation": [
      "urn:csabs:operation/semiring-addition",
      "urn:csabs:operation/semiring-multiplication"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/semiring-additive-monoid",
      "urn:csabs:axiom/semiring-multiplicative-monoid",
      "urn:csabs:axiom/semiring-distributivity",
      "urn:csabs:axiom/semiring-zero-annihilation",
      "urn:csabs:axiom/Semiring-closure",
      "urn:csabs:axiom/Semiring-add-associative",
      "urn:csabs:axiom/Semiring-add-commutative",
      "urn:csabs:axiom/Semiring-add-zero",
      "urn:csabs:axiom/Semiring-mul-associative",
      "urn:csabs:axiom/Semiring-mul-unit",
      "urn:csabs:axiom/Semiring-distributive",
      "urn:csabs:axiom/Semiring-zero-absorption"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/Semiring-finite-distribution"
    ],
    "convention": "This entry uses the unital convention; variants must be separate entries.",
    "coverageStatus": "basis-reviewed",
    "requiresConcept": [],
    "verificationObligation": [
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Unital semiring: total addition and multiplication; additive commutative monoid; multiplicative monoid; both distributivities. Multiplication need not commute; 0=1 is permitted.",
    "basisKind": "axiomatic-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:operation/semiring-addition",
    "type": "Operation",
    "name": "addition",
    "signature": "+ : S×S→S",
    "description": "Commutative monoid operation; additive inverses are not required.",
    "concept": "urn:csabs:concept/Semiring"
  },
  {
    "id": "urn:csabs:operation/semiring-multiplication",
    "type": "Operation",
    "name": "multiplication",
    "signature": "· : S×S→S",
    "description": "Associative multiplication with identity under this entry's convention.",
    "concept": "urn:csabs:concept/Semiring"
  },
  {
    "id": "urn:csabs:axiom/semiring-additive-monoid",
    "type": "Axiom",
    "statement": "Addition forms a commutative monoid; additive inverses are not required.",
    "appliesTo": [
      "urn:csabs:concept/Semiring"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law",
    "name": "semiring-additive-monoid",
    "formalStatement": "Addition forms a commutative monoid; additive inverses are not required.",
    "assumptions": [
      "Use the linked concept’s explicit basis and carrier conventions."
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/semiring-multiplicative-monoid",
    "type": "Axiom",
    "statement": "Multiplication forms a monoid under the stated unital convention.",
    "appliesTo": [
      "urn:csabs:concept/Semiring"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law",
    "name": "semiring-multiplicative-monoid",
    "formalStatement": "Multiplication forms a monoid under the stated unital convention.",
    "assumptions": [
      "Use the linked concept’s explicit basis and carrier conventions."
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/semiring-distributivity",
    "type": "Axiom",
    "statement": "Multiplication distributes over addition on both sides.",
    "appliesTo": [
      "urn:csabs:concept/Semiring"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law",
    "name": "semiring-distributivity",
    "formalStatement": "Multiplication distributes over addition on both sides.",
    "assumptions": [
      "Use the linked concept’s explicit basis and carrier conventions."
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/semiring-zero-annihilation",
    "type": "Axiom",
    "statement": "Zero annihilates multiplication.",
    "formalStatement": "0·x=x·0=0",
    "appliesTo": [
      "urn:csabs:concept/Semiring"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law",
    "name": "semiring-zero-annihilation",
    "assumptions": [
      "Use the linked concept’s explicit basis and carrier conventions."
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/Semiring-closure",
    "type": "Axiom",
    "name": "closure",
    "statement": "The carrier contains the constants and is closed under both operations.",
    "formalStatement": "0,1∈S; +,·:S×S→S",
    "appliesTo": [
      "urn:csabs:concept/Semiring"
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
    "id": "urn:csabs:axiom/Semiring-add-associative",
    "type": "Axiom",
    "name": "add-associative",
    "statement": "Addition is associative.",
    "formalStatement": "(x+y)+z=x+(y+z)",
    "appliesTo": [
      "urn:csabs:concept/Semiring"
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
    "id": "urn:csabs:axiom/Semiring-add-commutative",
    "type": "Axiom",
    "name": "add-commutative",
    "statement": "Addition commutes.",
    "formalStatement": "x+y=y+x",
    "appliesTo": [
      "urn:csabs:concept/Semiring"
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
    "id": "urn:csabs:axiom/Semiring-add-zero",
    "type": "Axiom",
    "name": "add-zero",
    "statement": "Zero is the additive identity.",
    "formalStatement": "0+x=x; x+0=x",
    "appliesTo": [
      "urn:csabs:concept/Semiring"
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
    "id": "urn:csabs:axiom/Semiring-mul-associative",
    "type": "Axiom",
    "name": "mul-associative",
    "statement": "Multiplication is associative.",
    "formalStatement": "(xy)z=x(yz)",
    "appliesTo": [
      "urn:csabs:concept/Semiring"
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
    "id": "urn:csabs:axiom/Semiring-mul-unit",
    "type": "Axiom",
    "name": "mul-unit",
    "statement": "One is the multiplicative identity.",
    "formalStatement": "1x=x; x1=x",
    "appliesTo": [
      "urn:csabs:concept/Semiring"
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
    "id": "urn:csabs:axiom/Semiring-distributive",
    "type": "Axiom",
    "name": "distributive",
    "statement": "Multiplication distributes over addition on both sides.",
    "formalStatement": "x(y+z)=xy+xz; (x+y)z=xz+yz",
    "appliesTo": [
      "urn:csabs:concept/Semiring"
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
    "id": "urn:csabs:axiom/Semiring-zero-absorption",
    "type": "Axiom",
    "name": "zero-absorption",
    "statement": "Multiplication by zero gives zero.",
    "formalStatement": "0x=0; x0=0",
    "appliesTo": [
      "urn:csabs:concept/Semiring"
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
    "id": "urn:csabs:theorem/Semiring-finite-distribution",
    "type": "Theorem",
    "name": "finite-distribution",
    "statement": "Multiplication distributes over finite sums, including the empty sum.",
    "formalStatement": "a·Σᵢ bᵢ=Σᵢ(a·bᵢ); (Σᵢ bᵢ)·a=Σᵢ(bᵢ·a)",
    "proofSketch": "Induct on the finite list; use zero annihilation at the empty list.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for Semiring apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/Semiring"
    ],
    "dependsOn": [
      "urn:csabs:axiom/semiring-additive-monoid",
      "urn:csabs:axiom/semiring-multiplicative-monoid",
      "urn:csabs:axiom/semiring-distributivity",
      "urn:csabs:axiom/semiring-zero-annihilation",
      "urn:csabs:axiom/Semiring-closure",
      "urn:csabs:axiom/Semiring-add-associative",
      "urn:csabs:axiom/Semiring-add-commutative",
      "urn:csabs:axiom/Semiring-add-zero",
      "urn:csabs:axiom/Semiring-mul-associative",
      "urn:csabs:axiom/Semiring-mul-unit",
      "urn:csabs:axiom/Semiring-distributive",
      "urn:csabs:axiom/Semiring-zero-absorption"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
