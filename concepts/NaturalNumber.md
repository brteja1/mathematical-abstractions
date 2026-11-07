# Natural Number

The nonnegative integers with zero and successor, supporting exact finite counting and induction.

**Notation:** ℕ={0,1,2,…}; succ(n)=n+1

**Stable ID:** `urn:csabs:concept/NaturalNumber`

**Categories:** Numeric computation

**Kind:** Mathematical structure

**Prerequisites:** [Mathematical integers](Integer.md)

## Backlinks

- [Finite ordered binary tree with node labels](BinaryTree.md) — `requiresConcept`
- [Multiset](Multiset.md) — `requiresConcept`
- [Structural Induction](StructuralInduction.md) — `requiresConcept`

## Interface and scope

**axiomBasis:** Selected presentation: The nonnegative integers with zero and successor, supporting exact finite counting and induction. Governing rules: Zero is a natural and successor is closed, injective, and never zero. Induction is a schema over predicates on the standard natural numbers. Addition and multiplication are defined by primitive recursion.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**verificationObligation:** Instantiate carrier, equality, and stated semantic conventions before using this entry.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-NaturalNumber-successor"></a>

### successor

`urn:csabs:operation/NaturalNumber-successor`

**signature:** succ : ℕ→ℕ

**description:** Returns the next natural number.

<a id="node-urn-csabs-operation-NaturalNumber-basis-zero"></a>

### zero

`urn:csabs:operation/NaturalNumber-basis-zero`

**signature:** zero : ℕ

**description:** Constructs zero.

<a id="node-urn-csabs-operation-NaturalNumber-basis-add"></a>

### add

`urn:csabs:operation/NaturalNumber-basis-add`

**signature:** add : ℕ×ℕ→ℕ

**description:** Adds by the stated successor recursion.

<a id="node-urn-csabs-operation-NaturalNumber-basis-multiply"></a>

### multiply

`urn:csabs:operation/NaturalNumber-basis-multiply`

**signature:** mul : ℕ×ℕ→ℕ

**description:** Multiplies by the stated recursion.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-NaturalNumber-constructors"></a>

### constructors

`urn:csabs:axiom/NaturalNumber-constructors`

**statement:** Zero is a natural and successor is closed, injective, and never zero.

**formalStatement:** 0∈ℕ; S:ℕ→ℕ; S(n)≠0; S(n)=S(m)⇒n=m

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-NaturalNumber-induction-schema"></a>

### induction-schema

`urn:csabs:axiom/NaturalNumber-induction-schema`

**statement:** Induction is a schema over predicates on the standard natural numbers.

**formalStatement:** P(0)∧(∀n:P(n)⇒P(S(n))) ⇒ ∀n:P(n)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-NaturalNumber-arithmetic-recursion"></a>

### arithmetic-recursion

`urn:csabs:axiom/NaturalNumber-arithmetic-recursion`

**statement:** Addition and multiplication are defined by primitive recursion.

**formalStatement:** a+0=a; a+S(b)=S(a+b); a·0=0; a·S(b)=a·b+a

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

<a id="node-urn-csabs-law-NaturalNumber-core"></a>

### law/NaturalNumber-core

`urn:csabs:law/NaturalNumber-core`

**statement:** Mathematical induction proves predicates for all naturals.

**formalStatement:** P(0) ∧ (∀n P(n)⇒P(n+1)) ⇒ ∀n P(n)

**reviewStatus:** editorial-summary; not machine-proved

**assumptions:** Use the carrier and semantic convention in the linked concept definition.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [constructors](NaturalNumber.md#node-urn-csabs-axiom-NaturalNumber-constructors); [induction-schema](NaturalNumber.md#node-urn-csabs-axiom-NaturalNumber-induction-schema); [arithmetic-recursion](NaturalNumber.md#node-urn-csabs-axiom-NaturalNumber-arithmetic-recursion)

**provenanceStatus:** legacy-source-missing

## Theorems

<a id="node-urn-csabs-theorem-NaturalNumber-zero-addition"></a>

### zero-addition

`urn:csabs:theorem/NaturalNumber-zero-addition`

**statement:** Adding zero on the left preserves every natural number.

**formalStatement:** 0+n=n

**proofSketch:** Induct on n using the addition recursion equations.

**assumptions:** The explicit basis, carriers, and side conditions stated for NaturalNumber apply.

**dependsOn:** [constructors](NaturalNumber.md#node-urn-csabs-axiom-NaturalNumber-constructors); [induction-schema](NaturalNumber.md#node-urn-csabs-axiom-NaturalNumber-induction-schema); [arithmetic-recursion](NaturalNumber.md#node-urn-csabs-axiom-NaturalNumber-arithmetic-recursion)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Concept provenance

- [Lean reference: natural numbers](https://lean-lang.org/doc/reference/latest/Basic-Types/Natural-Numbers/); sourceRole: reference-for-selected-basis

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/NaturalNumber",
    "type": "Concept",
    "shortForm": "NaturalNumber",
    "fullName": "Natural Number",
    "category": [
      "urn:csabs:category/numeric-computation"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "The nonnegative integers with zero and successor, supporting exact finite counting and induction.",
    "notation": "ℕ={0,1,2,…}; succ(n)=n+1",
    "hasOperation": [
      "urn:csabs:operation/NaturalNumber-successor",
      "urn:csabs:operation/NaturalNumber-basis-zero",
      "urn:csabs:operation/NaturalNumber-basis-add",
      "urn:csabs:operation/NaturalNumber-basis-multiply"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/NaturalNumber-constructors",
      "urn:csabs:axiom/NaturalNumber-induction-schema",
      "urn:csabs:axiom/NaturalNumber-arithmetic-recursion"
    ],
    "hasLaw": [
      "urn:csabs:law/NaturalNumber-core"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/NaturalNumber-zero-addition"
    ],
    "requiresConcept": [
      "urn:csabs:concept/MathematicalInteger"
    ],
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Instantiate carrier, equality, and stated semantic conventions before using this entry.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: The nonnegative integers with zero and successor, supporting exact finite counting and induction. Governing rules: Zero is a natural and successor is closed, injective, and never zero. Induction is a schema over predicates on the standard natural numbers. Addition and multiplication are defined by primitive recursion.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "source": [
      "urn:csabs:source/lean-nat"
    ]
  },
  {
    "id": "urn:csabs:operation/NaturalNumber-successor",
    "type": "Operation",
    "name": "successor",
    "signature": "succ : ℕ→ℕ",
    "description": "Returns the next natural number.",
    "concept": "urn:csabs:concept/NaturalNumber"
  },
  {
    "id": "urn:csabs:operation/NaturalNumber-basis-zero",
    "type": "Operation",
    "name": "zero",
    "signature": "zero : ℕ",
    "description": "Constructs zero.",
    "concept": "urn:csabs:concept/NaturalNumber"
  },
  {
    "id": "urn:csabs:operation/NaturalNumber-basis-add",
    "type": "Operation",
    "name": "add",
    "signature": "add : ℕ×ℕ→ℕ",
    "description": "Adds by the stated successor recursion.",
    "concept": "urn:csabs:concept/NaturalNumber"
  },
  {
    "id": "urn:csabs:operation/NaturalNumber-basis-multiply",
    "type": "Operation",
    "name": "multiply",
    "signature": "mul : ℕ×ℕ→ℕ",
    "description": "Multiplies by the stated recursion.",
    "concept": "urn:csabs:concept/NaturalNumber"
  },
  {
    "id": "urn:csabs:axiom/NaturalNumber-constructors",
    "type": "Axiom",
    "name": "constructors",
    "statement": "Zero is a natural and successor is closed, injective, and never zero.",
    "formalStatement": "0∈ℕ; S:ℕ→ℕ; S(n)≠0; S(n)=S(m)⇒n=m",
    "appliesTo": [
      "urn:csabs:concept/NaturalNumber"
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
    "id": "urn:csabs:axiom/NaturalNumber-induction-schema",
    "type": "Axiom",
    "name": "induction-schema",
    "statement": "Induction is a schema over predicates on the standard natural numbers.",
    "formalStatement": "P(0)∧(∀n:P(n)⇒P(S(n))) ⇒ ∀n:P(n)",
    "appliesTo": [
      "urn:csabs:concept/NaturalNumber"
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
    "id": "urn:csabs:axiom/NaturalNumber-arithmetic-recursion",
    "type": "Axiom",
    "name": "arithmetic-recursion",
    "statement": "Addition and multiplication are defined by primitive recursion.",
    "formalStatement": "a+0=a; a+S(b)=S(a+b); a·0=0; a·S(b)=a·b+a",
    "appliesTo": [
      "urn:csabs:concept/NaturalNumber"
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
    "id": "urn:csabs:law/NaturalNumber-core",
    "type": "Law",
    "statement": "Mathematical induction proves predicates for all naturals.",
    "formalStatement": "P(0) ∧ (∀n P(n)⇒P(n+1)) ⇒ ∀n P(n)",
    "appliesTo": [
      "urn:csabs:concept/NaturalNumber"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "assumptions": [
      "Use the carrier and semantic convention in the linked concept definition."
    ],
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/NaturalNumber-constructors",
      "urn:csabs:axiom/NaturalNumber-induction-schema",
      "urn:csabs:axiom/NaturalNumber-arithmetic-recursion"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/NaturalNumber-zero-addition",
    "type": "Theorem",
    "name": "zero-addition",
    "statement": "Adding zero on the left preserves every natural number.",
    "formalStatement": "0+n=n",
    "proofSketch": "Induct on n using the addition recursion equations.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for NaturalNumber apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/NaturalNumber"
    ],
    "dependsOn": [
      "urn:csabs:axiom/NaturalNumber-constructors",
      "urn:csabs:axiom/NaturalNumber-induction-schema",
      "urn:csabs:axiom/NaturalNumber-arithmetic-recursion"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
