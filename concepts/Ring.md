# Unital ring (convention stated)

A set whose addition is an abelian group and whose multiplication is associative with identity and distributes over addition; multiplication need not be commutative.

**Notation:** (R,+,·,0,1): (R,+,0) abelian group; (R,·,1) monoid; distributivity; 0≠1 is not assumed unless stated.

**Stable ID:** `urn:csabs:concept/Ring`

**Categories:** Algebra

**Kind:** Mathematical structure

**Specializes:** [Semiring](Semiring.md)

## Backlinks

- [Field](Field.md) — `requiresConcept`
- [Field](Field.md) — `specializationOf`
- [Modular Integer](ModularInteger.md) — `requiresConcept`

## Interface and scope

**axiomBasis:** Unital ring: total addition and multiplication; additive abelian group; multiplicative monoid; both distributivities. Multiplication need not commute; 0=1 is permitted.

**basisKind:** axiomatic-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**convention:** Unital; this entry permits the zero ring unless a specific theorem excludes it.

**specializationNote:** Retain addition, multiplication, zero and one and forget additive inverse as named structure; both entries use the unital convention and permit zero=one.

**verificationObligation:** Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

**provenanceStatus:** legacy-source-missing

## Operations

<a id="node-urn-csabs-operation-ring-addition"></a>

### addition

`urn:csabs:operation/ring-addition`

**signature:** + : R×R→R

**description:** The abelian-group operation on ring elements.

<a id="node-urn-csabs-operation-ring-multiplication"></a>

### multiplication

`urn:csabs:operation/ring-multiplication`

**signature:** · : R×R→R

**description:** Associative ring multiplication with identity under this entry's convention.

<a id="node-urn-csabs-operation-ring-negation"></a>

### additive inverse

`urn:csabs:operation/ring-negation`

**signature:** − : R→R

**description:** Returns the additive inverse.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-ring-additive-abelian-group"></a>

### ring-additive-abelian-group

`urn:csabs:axiom/ring-additive-abelian-group`

**statement:** Ring addition forms an abelian group.

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

**formalStatement:** Ring addition forms an abelian group.

**assumptions:** Use the linked concept’s explicit basis and carrier conventions.

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-ring-multiplicative-monoid"></a>

### ring-multiplicative-monoid

`urn:csabs:axiom/ring-multiplicative-monoid`

**statement:** Ring multiplication is associative and has an identity under the unital convention.

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

**formalStatement:** Ring multiplication is associative and has an identity under the unital convention.

**assumptions:** Use the linked concept’s explicit basis and carrier conventions.

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-ring-distributivity"></a>

### ring-distributivity

`urn:csabs:axiom/ring-distributivity`

**statement:** Multiplication distributes over addition on both sides.

**formalStatement:** a(b+c)=ab+ac; (a+b)c=ac+bc

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

**assumptions:** Use the linked concept’s explicit basis and carrier conventions.

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Ring-closure"></a>

### closure

`urn:csabs:axiom/Ring-closure`

**statement:** The carrier contains the constants and is closed under both operations.

**formalStatement:** 0,1∈S; +,·:S×S→S

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Ring-add-associative"></a>

### add-associative

`urn:csabs:axiom/Ring-add-associative`

**statement:** Addition is associative.

**formalStatement:** (x+y)+z=x+(y+z)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Ring-add-commutative"></a>

### add-commutative

`urn:csabs:axiom/Ring-add-commutative`

**statement:** Addition commutes.

**formalStatement:** x+y=y+x

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Ring-add-zero"></a>

### add-zero

`urn:csabs:axiom/Ring-add-zero`

**statement:** Zero is the additive identity.

**formalStatement:** 0+x=x; x+0=x

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Ring-mul-associative"></a>

### mul-associative

`urn:csabs:axiom/Ring-mul-associative`

**statement:** Multiplication is associative.

**formalStatement:** (xy)z=x(yz)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Ring-mul-unit"></a>

### mul-unit

`urn:csabs:axiom/Ring-mul-unit`

**statement:** One is the multiplicative identity.

**formalStatement:** 1x=x; x1=x

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Ring-distributive"></a>

### distributive

`urn:csabs:axiom/Ring-distributive`

**statement:** Multiplication distributes over addition on both sides.

**formalStatement:** x(y+z)=xy+xz; (x+y)z=xz+yz

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Ring-add-inverse"></a>

### add-inverse

`urn:csabs:axiom/Ring-add-inverse`

**statement:** Every element has an additive inverse.

**formalStatement:** neg:S→S; x+neg(x)=0; neg(x)+x=0

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-Ring-zero-multiplication"></a>

### zero-multiplication

`urn:csabs:theorem/Ring-zero-multiplication`

**statement:** Zero annihilates ring multiplication.

**formalStatement:** 0x=0=x0

**proofSketch:** Distribute (0+0)x and cancel one 0x in the additive group; use the analogous right argument.

**assumptions:** The explicit basis, carriers, and side conditions stated for Ring apply.

**dependsOn:** [ring-additive-abelian-group](Ring.md#node-urn-csabs-axiom-ring-additive-abelian-group); [ring-multiplicative-monoid](Ring.md#node-urn-csabs-axiom-ring-multiplicative-monoid); [ring-distributivity](Ring.md#node-urn-csabs-axiom-ring-distributivity); [closure](Ring.md#node-urn-csabs-axiom-Ring-closure); [add-associative](Ring.md#node-urn-csabs-axiom-Ring-add-associative); [add-commutative](Ring.md#node-urn-csabs-axiom-Ring-add-commutative); [add-zero](Ring.md#node-urn-csabs-axiom-Ring-add-zero); [mul-associative](Ring.md#node-urn-csabs-axiom-Ring-mul-associative); [mul-unit](Ring.md#node-urn-csabs-axiom-Ring-mul-unit); [distributive](Ring.md#node-urn-csabs-axiom-Ring-distributive); [add-inverse](Ring.md#node-urn-csabs-axiom-Ring-add-inverse)

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
    "id": "urn:csabs:concept/Ring",
    "type": "Concept",
    "shortForm": "Ring",
    "fullName": "Unital ring (convention stated)",
    "category": [
      "urn:csabs:category/algebra"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "A set whose addition is an abelian group and whose multiplication is associative with identity and distributes over addition; multiplication need not be commutative.",
    "notation": "(R,+,·,0,1): (R,+,0) abelian group; (R,·,1) monoid; distributivity; 0≠1 is not assumed unless stated.",
    "hasOperation": [
      "urn:csabs:operation/ring-addition",
      "urn:csabs:operation/ring-multiplication",
      "urn:csabs:operation/ring-negation"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/ring-additive-abelian-group",
      "urn:csabs:axiom/ring-multiplicative-monoid",
      "urn:csabs:axiom/ring-distributivity",
      "urn:csabs:axiom/Ring-closure",
      "urn:csabs:axiom/Ring-add-associative",
      "urn:csabs:axiom/Ring-add-commutative",
      "urn:csabs:axiom/Ring-add-zero",
      "urn:csabs:axiom/Ring-mul-associative",
      "urn:csabs:axiom/Ring-mul-unit",
      "urn:csabs:axiom/Ring-distributive",
      "urn:csabs:axiom/Ring-add-inverse"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/Ring-zero-multiplication"
    ],
    "convention": "Unital; this entry permits the zero ring unless a specific theorem excludes it.",
    "coverageStatus": "basis-reviewed",
    "requiresConcept": [],
    "verificationObligation": [
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Unital ring: total addition and multiplication; additive abelian group; multiplicative monoid; both distributivities. Multiplication need not commute; 0=1 is permitted.",
    "basisKind": "axiomatic-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "provenanceStatus": "legacy-source-missing",
    "specializationOf": [
      "urn:csabs:concept/Semiring"
    ],
    "specializationNote": "Retain addition, multiplication, zero and one and forget additive inverse as named structure; both entries use the unital convention and permit zero=one."
  },
  {
    "id": "urn:csabs:operation/ring-addition",
    "type": "Operation",
    "name": "addition",
    "signature": "+ : R×R→R",
    "description": "The abelian-group operation on ring elements.",
    "concept": "urn:csabs:concept/Ring"
  },
  {
    "id": "urn:csabs:operation/ring-multiplication",
    "type": "Operation",
    "name": "multiplication",
    "signature": "· : R×R→R",
    "description": "Associative ring multiplication with identity under this entry's convention.",
    "concept": "urn:csabs:concept/Ring"
  },
  {
    "id": "urn:csabs:operation/ring-negation",
    "type": "Operation",
    "name": "additive inverse",
    "signature": "− : R→R",
    "description": "Returns the additive inverse.",
    "concept": "urn:csabs:concept/Ring"
  },
  {
    "id": "urn:csabs:axiom/ring-additive-abelian-group",
    "type": "Axiom",
    "statement": "Ring addition forms an abelian group.",
    "appliesTo": [
      "urn:csabs:concept/Ring"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law",
    "name": "ring-additive-abelian-group",
    "formalStatement": "Ring addition forms an abelian group.",
    "assumptions": [
      "Use the linked concept’s explicit basis and carrier conventions."
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/ring-multiplicative-monoid",
    "type": "Axiom",
    "statement": "Ring multiplication is associative and has an identity under the unital convention.",
    "appliesTo": [
      "urn:csabs:concept/Ring"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law",
    "name": "ring-multiplicative-monoid",
    "formalStatement": "Ring multiplication is associative and has an identity under the unital convention.",
    "assumptions": [
      "Use the linked concept’s explicit basis and carrier conventions."
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/ring-distributivity",
    "type": "Axiom",
    "statement": "Multiplication distributes over addition on both sides.",
    "formalStatement": "a(b+c)=ab+ac; (a+b)c=ac+bc",
    "appliesTo": [
      "urn:csabs:concept/Ring"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law",
    "name": "ring-distributivity",
    "assumptions": [
      "Use the linked concept’s explicit basis and carrier conventions."
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/Ring-closure",
    "type": "Axiom",
    "name": "closure",
    "statement": "The carrier contains the constants and is closed under both operations.",
    "formalStatement": "0,1∈S; +,·:S×S→S",
    "appliesTo": [
      "urn:csabs:concept/Ring"
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
    "id": "urn:csabs:axiom/Ring-add-associative",
    "type": "Axiom",
    "name": "add-associative",
    "statement": "Addition is associative.",
    "formalStatement": "(x+y)+z=x+(y+z)",
    "appliesTo": [
      "urn:csabs:concept/Ring"
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
    "id": "urn:csabs:axiom/Ring-add-commutative",
    "type": "Axiom",
    "name": "add-commutative",
    "statement": "Addition commutes.",
    "formalStatement": "x+y=y+x",
    "appliesTo": [
      "urn:csabs:concept/Ring"
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
    "id": "urn:csabs:axiom/Ring-add-zero",
    "type": "Axiom",
    "name": "add-zero",
    "statement": "Zero is the additive identity.",
    "formalStatement": "0+x=x; x+0=x",
    "appliesTo": [
      "urn:csabs:concept/Ring"
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
    "id": "urn:csabs:axiom/Ring-mul-associative",
    "type": "Axiom",
    "name": "mul-associative",
    "statement": "Multiplication is associative.",
    "formalStatement": "(xy)z=x(yz)",
    "appliesTo": [
      "urn:csabs:concept/Ring"
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
    "id": "urn:csabs:axiom/Ring-mul-unit",
    "type": "Axiom",
    "name": "mul-unit",
    "statement": "One is the multiplicative identity.",
    "formalStatement": "1x=x; x1=x",
    "appliesTo": [
      "urn:csabs:concept/Ring"
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
    "id": "urn:csabs:axiom/Ring-distributive",
    "type": "Axiom",
    "name": "distributive",
    "statement": "Multiplication distributes over addition on both sides.",
    "formalStatement": "x(y+z)=xy+xz; (x+y)z=xz+yz",
    "appliesTo": [
      "urn:csabs:concept/Ring"
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
    "id": "urn:csabs:axiom/Ring-add-inverse",
    "type": "Axiom",
    "name": "add-inverse",
    "statement": "Every element has an additive inverse.",
    "formalStatement": "neg:S→S; x+neg(x)=0; neg(x)+x=0",
    "appliesTo": [
      "urn:csabs:concept/Ring"
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
    "id": "urn:csabs:theorem/Ring-zero-multiplication",
    "type": "Theorem",
    "name": "zero-multiplication",
    "statement": "Zero annihilates ring multiplication.",
    "formalStatement": "0x=0=x0",
    "proofSketch": "Distribute (0+0)x and cancel one 0x in the additive group; use the analogous right argument.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for Ring apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/Ring"
    ],
    "dependsOn": [
      "urn:csabs:axiom/ring-additive-abelian-group",
      "urn:csabs:axiom/ring-multiplicative-monoid",
      "urn:csabs:axiom/ring-distributivity",
      "urn:csabs:axiom/Ring-closure",
      "urn:csabs:axiom/Ring-add-associative",
      "urn:csabs:axiom/Ring-add-commutative",
      "urn:csabs:axiom/Ring-add-zero",
      "urn:csabs:axiom/Ring-mul-associative",
      "urn:csabs:axiom/Ring-mul-unit",
      "urn:csabs:axiom/Ring-distributive",
      "urn:csabs:axiom/Ring-add-inverse"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
