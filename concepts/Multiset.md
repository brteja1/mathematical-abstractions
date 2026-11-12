# Multiset

A finite collection represented by nonnegative multiplicities, with only finitely many nonzero counts.

**Notation:** m:A→ℕ; support(m) finite

**Stable ID:** `urn:csabs:concept/Multiset`

**Categories:** Data structures → Sets and mappings

**Kind:** Abstract data type

**Prerequisites:** [Set](Set.md), [Natural Number](NaturalNumber.md)

**Related concepts:** [Finite set collection](FiniteSet.md), [Ordered collection without duplicates](OrderedSet.md), [Arithmetic mean of a finite real sample](ArithmeticMean.md), [Numeric sample median (midpoint convention)](Median.md), [Empirical mode set (all observed frequency maximizers)](Mode.md)

## Backlinks

- [Arithmetic mean of a finite real sample](ArithmeticMean.md) — `requiresConcept`
- [Finite database relation under bag semantics](BagRelation.md) — `requiresConcept`
- [Finite database relation under bag semantics](BagRelation.md) — `specializationOf`
- [Finite database relation under set semantics](DatabaseRelation.md) — `relatedConcept`
- [Finite set collection](FiniteSet.md) — `relatedConcept`
- [Numeric sample median (midpoint convention)](Median.md) — `requiresConcept`
- [Empirical mode set (all observed frequency maximizers)](Mode.md) — `requiresConcept`
- [Ordered collection without duplicates](OrderedSet.md) — `relatedConcept`
- [Priority Queue](PriorityQueue.md) — `requiresConcept`

## Mathematical formulation

Multiset(A)=List(A)/permutation; equivalently a finite-support multiplicity μ:A→ℕ. Equality is pointwise multiplicity equality; union adds multiplicities and the empty multiset has μ=0.

**Lean formulation** (in its source module context):

```lean
abbrev Multiset (A : Type u) := _root_.Multiset A
```

**Source:** [`Catalog.Multiset`](../lean/Catalog/DataStructures.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Mathlib Multiset A, quotient of lists by permutation, equivalent finite multiplicity representation.

**Limits:** Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Selected presentation: A finite collection represented by nonnegative multiplicities, with only finitely many nonzero counts. Governing rules: A bag is a natural multiplicity function with finite support. Bags are equal exactly when multiplicities agree. Insertion, removal, and union are defined pointwise.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**verificationObligation:** Instantiate carrier, equality, and stated semantic conventions before using this entry.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

**provenanceStatus:** legacy-source-missing

## Operations

<a id="node-urn-csabs-operation-Multiset-count"></a>

### count

`urn:csabs:operation/Multiset-count`

**signature:** count : Bag(A)×A→ℕ

**description:** Returns multiplicity, zero when absent.

<a id="node-urn-csabs-operation-Multiset-insert"></a>

### insert

`urn:csabs:operation/Multiset-insert`

**signature:** insert : Bag(A)×A→Bag(A)

**description:** Increases the selected element's count by one.

<a id="node-urn-csabs-operation-Multiset-union"></a>

### union

`urn:csabs:operation/Multiset-union`

**signature:** ⊎ : Bag(A)×Bag(A)→Bag(A)

**description:** Adds the multiplicities pointwise.

<a id="node-urn-csabs-operation-Multiset-basis-empty"></a>

### empty

`urn:csabs:operation/Multiset-basis-empty`

**signature:** empty : Bag(A)

**description:** Returns the all-zero multiplicity function.

<a id="node-urn-csabs-operation-Multiset-basis-remove"></a>

### remove

`urn:csabs:operation/Multiset-basis-remove`

**signature:** remove : Bag(A)×A→Bag(A)

**description:** Subtracts one occurrence if present, leaving absent counts at zero.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-Multiset-finite-support"></a>

### finite-support

`urn:csabs:axiom/Multiset-finite-support`

**statement:** A bag is a natural multiplicity function with finite support.

**formalStatement:** Bag(A)={m:A→ℕ:support(m)={x:m(x)>0} is finite}

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Multiset-count-extensionality"></a>

### count-extensionality

`urn:csabs:axiom/Multiset-count-extensionality`

**statement:** Bags are equal exactly when multiplicities agree.

**formalStatement:** m=n iff ∀x:count(m,x)=count(n,x)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Multiset-operations"></a>

### operations

`urn:csabs:axiom/Multiset-operations`

**statement:** Insertion, removal, and union are defined pointwise.

**formalStatement:** count(empty,x)=0; count(insert(m,a),x)=count(m,x)+[x=a]; count(remove(m,a),x)=max(0,count(m,x)−[x=a]); count(m⊎n,x)=count(m,x)+count(n,x)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

<a id="node-urn-csabs-law-Multiset-core"></a>

### law/Multiset-core

`urn:csabs:law/Multiset-core`

**statement:** Multiset union adds multiplicities and is commutative.

**formalStatement:** (m⊎n)(x)=m(x)+n(x); m⊎n=n⊎m

**reviewStatus:** editorial-summary; not machine-proved

**assumptions:** Use the carrier and semantic convention in the linked concept definition.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [finite-support](Multiset.md#node-urn-csabs-axiom-Multiset-finite-support); [count-extensionality](Multiset.md#node-urn-csabs-axiom-Multiset-count-extensionality); [operations](Multiset.md#node-urn-csabs-axiom-Multiset-operations)

**provenanceStatus:** legacy-source-missing

## Theorems

<a id="node-urn-csabs-theorem-Multiset-union-identity"></a>

### union-identity

`urn:csabs:theorem/Multiset-union-identity`

**statement:** The empty multiset is an identity for multiset union.

**formalStatement:** m⊎empty=m=empty⊎m

**proofSketch:** Every element count is its original count plus zero; use count extensionality.

**assumptions:** The explicit basis, carriers, and side conditions stated for Multiset apply.

**dependsOn:** [finite-support](Multiset.md#node-urn-csabs-axiom-Multiset-finite-support); [count-extensionality](Multiset.md#node-urn-csabs-axiom-Multiset-count-extensionality); [operations](Multiset.md#node-urn-csabs-axiom-Multiset-operations)

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
    "id": "urn:csabs:concept/Multiset",
    "type": "Concept",
    "shortForm": "Multiset",
    "fullName": "Multiset",
    "category": [
      "urn:csabs:category/associative-collections"
    ],
    "kind": "urn:csabs:kind/abstract-data-type",
    "definition": "A finite collection represented by nonnegative multiplicities, with only finitely many nonzero counts.",
    "notation": "m:A→ℕ; support(m) finite",
    "hasOperation": [
      "urn:csabs:operation/Multiset-count",
      "urn:csabs:operation/Multiset-insert",
      "urn:csabs:operation/Multiset-union",
      "urn:csabs:operation/Multiset-basis-empty",
      "urn:csabs:operation/Multiset-basis-remove"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/Multiset-finite-support",
      "urn:csabs:axiom/Multiset-count-extensionality",
      "urn:csabs:axiom/Multiset-operations"
    ],
    "hasLaw": [
      "urn:csabs:law/Multiset-core"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/Multiset-union-identity"
    ],
    "requiresConcept": [
      "urn:csabs:concept/Set",
      "urn:csabs:concept/NaturalNumber"
    ],
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Instantiate carrier, equality, and stated semantic conventions before using this entry.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: A finite collection represented by nonnegative multiplicities, with only finitely many nonzero counts. Governing rules: A bag is a natural multiplicity function with finite support. Bags are equal exactly when multiplicities agree. Insertion, removal, and union are defined pointwise.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "provenanceStatus": "legacy-source-missing",
    "relatedConcept": [
      "urn:csabs:concept/FiniteSet",
      "urn:csabs:concept/OrderedSet",
      "urn:csabs:concept/ArithmeticMean",
      "urn:csabs:concept/Median",
      "urn:csabs:concept/Mode"
    ],
    "leanFormulation": "abbrev Multiset (A : Type u) := _root_.Multiset A",
    "formulationSource": "urn:csabs:source/local-lean-DataStructures",
    "formulationLocator": "Catalog.Multiset",
    "formulationScope": "model",
    "leanModelMapping": "Mathlib Multiset A, quotient of lists by permutation, equivalent finite multiplicity representation.",
    "leanModelLimitations": "Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.",
    "mathematicalFormulation": "Multiset(A)=List(A)/permutation; equivalently a finite-support multiplicity μ:A→ℕ. Equality is pointwise multiplicity equality; union adds multiplicities and the empty multiset has μ=0."
  },
  {
    "id": "urn:csabs:operation/Multiset-count",
    "type": "Operation",
    "name": "count",
    "signature": "count : Bag(A)×A→ℕ",
    "description": "Returns multiplicity, zero when absent.",
    "concept": "urn:csabs:concept/Multiset"
  },
  {
    "id": "urn:csabs:operation/Multiset-insert",
    "type": "Operation",
    "name": "insert",
    "signature": "insert : Bag(A)×A→Bag(A)",
    "description": "Increases the selected element's count by one.",
    "concept": "urn:csabs:concept/Multiset"
  },
  {
    "id": "urn:csabs:operation/Multiset-union",
    "type": "Operation",
    "name": "union",
    "signature": "⊎ : Bag(A)×Bag(A)→Bag(A)",
    "description": "Adds the multiplicities pointwise.",
    "concept": "urn:csabs:concept/Multiset"
  },
  {
    "id": "urn:csabs:operation/Multiset-basis-empty",
    "type": "Operation",
    "name": "empty",
    "signature": "empty : Bag(A)",
    "description": "Returns the all-zero multiplicity function.",
    "concept": "urn:csabs:concept/Multiset"
  },
  {
    "id": "urn:csabs:operation/Multiset-basis-remove",
    "type": "Operation",
    "name": "remove",
    "signature": "remove : Bag(A)×A→Bag(A)",
    "description": "Subtracts one occurrence if present, leaving absent counts at zero.",
    "concept": "urn:csabs:concept/Multiset"
  },
  {
    "id": "urn:csabs:law/Multiset-core",
    "type": "Law",
    "statement": "Multiset union adds multiplicities and is commutative.",
    "formalStatement": "(m⊎n)(x)=m(x)+n(x); m⊎n=n⊎m",
    "appliesTo": [
      "urn:csabs:concept/Multiset"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "assumptions": [
      "Use the carrier and semantic convention in the linked concept definition."
    ],
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/Multiset-finite-support",
      "urn:csabs:axiom/Multiset-count-extensionality",
      "urn:csabs:axiom/Multiset-operations"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/Multiset-union-identity",
    "type": "Theorem",
    "name": "union-identity",
    "statement": "The empty multiset is an identity for multiset union.",
    "formalStatement": "m⊎empty=m=empty⊎m",
    "proofSketch": "Every element count is its original count plus zero; use count extensionality.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for Multiset apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/Multiset"
    ],
    "dependsOn": [
      "urn:csabs:axiom/Multiset-finite-support",
      "urn:csabs:axiom/Multiset-count-extensionality",
      "urn:csabs:axiom/Multiset-operations"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
