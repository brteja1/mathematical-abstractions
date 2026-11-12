# Finite carrier with exhaustive enumeration

A carrier A equipped with an exhaustive duplicate-free finite set of all its values.

**Notation:** Finite(A) ⇔ ∃U∈FinSet(A), ∀a:A, a∈U

**Stable ID:** `urn:csabs:concept/FiniteType`

**Categories:** Types and semantics

**Kind:** Numeric data type

**Prerequisites:** [Finite set collection](FiniteSet.md), [Natural Number](NaturalNumber.md)

## Backlinks

- [Finite directed multigraph with edge identities](DirectedMultigraph.md) — `requiresConcept`
- [Union Find (disjoint-set union with representatives)](DisjointSet.md) — `requiresConcept`

## Mathematical formulation

A finite-type structure on A supplies an enumeration E containing each a∈A exactly once. |A| is the enumeration cardinality; the empty type is permitted.

**Lean formulation** (in its source module context):

```lean
abbrev FiniteType (A : Type u) := Fintype A
```

**Source:** [`Catalog.FiniteType`](../lean/Catalog/CoreData.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Catalog.FiniteType A is Fintype A evidence, bundling a Finset enumeration and completeness proof; A remains the actual value carrier. Finite(A) ⇔ ∃U∈FinSet(A), ∀a:A, a∈U. The empty carrier is permitted. Enumeration has no observable order; finiteness is evidence about A, not a finite collection drawn from a possibly infinite carrier. Equality of evidence is proof irrelevant in the Lean model.

**Limits:** Compiled carrier and selected interface interpretation. Some catalog operations are specified mathematically rather than wrapped as Lean declarations; no blanket proof of claims, algorithms, parsing, liveness or complexity. See individual witnesses.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** ∀a:A, a∈universe_A; universe_A is a finite set; equality is set equality; card_A=|universe_A|

**basisKind:** extensional-structural-definition

**basisScope:** The empty carrier is permitted. Enumeration has no observable order; finiteness is evidence about A, not a finite collection drawn from a possibly infinite carrier. Equality of evidence is proof irrelevant in the Lean model.

**verificationObligation:** Map carrier, equality, operation definedness and stated profile to the target API or proof context.; Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.; Model coverage does not establish every recorded claim or an implementation refinement.

**reviewStatus:** Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-FiniteType-universe"></a>

### universe

`urn:csabs:operation/FiniteType-universe`

**signature:** universe_A : FinSet(A)

**description:** Returns all values of A, without duplicates.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. The empty carrier is permitted. Enumeration has no observable order; finiteness is evidence about A, not a finite collection drawn from a possibly infinite carrier. Equality of evidence is proof irrelevant in the Lean model.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Returns all values of A, without duplicates.

**source:** [Mathlib pinned definitions: Data/Fintype/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Fintype/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Fintype.elems and Fintype.complete

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-FiniteType-cardinality"></a>

### cardinality

`urn:csabs:operation/FiniteType-cardinality`

**signature:** card_A : ℕ

**description:** card_A=|universe_A|.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. The empty carrier is permitted. Enumeration has no observable order; finiteness is evidence about A, not a finite collection drawn from a possibly infinite carrier. Equality of evidence is proof irrelevant in the Lean model.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** card_A=|universe_A|.

**source:** [Mathlib pinned definitions: Data/Fintype/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Fintype/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Fintype.elems and Fintype.complete

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-FiniteType-exhaustive"></a>

### exhaustive

`urn:csabs:axiom/FiniteType-exhaustive`

**statement:** Defining requirement: ∀a:A, a∈universe_A

**formalStatement:** ∀a:A, a∈universe_A

**assumptions:** The empty carrier is permitted. Enumeration has no observable order; finiteness is evidence about A, not a finite collection drawn from a possibly infinite carrier. Equality of evidence is proof irrelevant in the Lean model.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Mathlib pinned definitions: Data/Fintype/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Fintype/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Fintype.elems and Fintype.complete

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-FiniteType-finite-enumeration"></a>

### finite-enumeration

`urn:csabs:axiom/FiniteType-finite-enumeration`

**statement:** Defining requirement: universe_A is a finite set; equality is set equality

**formalStatement:** universe_A is a finite set; equality is set equality

**assumptions:** The empty carrier is permitted. Enumeration has no observable order; finiteness is evidence about A, not a finite collection drawn from a possibly infinite carrier. Equality of evidence is proof irrelevant in the Lean model.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Mathlib pinned definitions: Data/Fintype/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Fintype/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Fintype.elems and Fintype.complete

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-FiniteType-card-definition"></a>

### card-definition

`urn:csabs:axiom/FiniteType-card-definition`

**statement:** Defining requirement: card_A=|universe_A|

**formalStatement:** card_A=|universe_A|

**assumptions:** The empty carrier is permitted. Enumeration has no observable order; finiteness is evidence about A, not a finite collection drawn from a possibly infinite carrier. Equality of evidence is proof irrelevant in the Lean model.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Mathlib pinned definitions: Data/Fintype/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Fintype/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Fintype.elems and Fintype.complete

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-FiniteType-enumeration-unique"></a>

### enumeration-unique

`urn:csabs:law/FiniteType-enumeration-unique`

**statement:** (∀a:A, a∈U) ⇒ U=universe_A, for U∈FinSet(A)

**formalStatement:** (∀a:A, a∈U) ⇒ U=universe_A, for U∈FinSet(A)

**assumptions:** The empty carrier is permitted. Enumeration has no observable order; finiteness is evidence about A, not a finite collection drawn from a possibly infinite carrier. Equality of evidence is proof irrelevant in the Lean model.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [exhaustive](FiniteType.md#node-urn-csabs-axiom-FiniteType-exhaustive); [finite-enumeration](FiniteType.md#node-urn-csabs-axiom-FiniteType-finite-enumeration)

**proofSketch:** Both sets contain exactly the values of A; use set extensionality.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Mathlib pinned definitions: Data/Fintype/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Fintype/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Fintype.elems and Fintype.complete

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Theorems

<a id="node-urn-csabs-theorem-FiniteType-zero-cardinality"></a>

### zero-cardinality

`urn:csabs:theorem/FiniteType-zero-cardinality`

**statement:** card_A=0 ⇔ A has no values

**formalStatement:** card_A=0 ⇔ A has no values

**assumptions:** The empty carrier is permitted. Enumeration has no observable order; finiteness is evidence about A, not a finite collection drawn from a possibly infinite carrier. Equality of evidence is proof irrelevant in the Lean model.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [exhaustive](FiniteType.md#node-urn-csabs-axiom-FiniteType-exhaustive); [finite-enumeration](FiniteType.md#node-urn-csabs-axiom-FiniteType-finite-enumeration); [card-definition](FiniteType.md#node-urn-csabs-axiom-FiniteType-card-definition)

**proofSketch:** A finite set has size zero iff empty; use exhaustiveness.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Mathlib pinned definitions: Data/Fintype/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Fintype/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Fintype.elems and Fintype.complete

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Concept provenance

- [Mathlib pinned definitions: Data/Fintype/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Fintype/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Fintype.elems and Fintype.complete

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/FiniteType",
    "type": "Concept",
    "shortForm": "FiniteType",
    "fullName": "Finite carrier with exhaustive enumeration",
    "category": [
      "urn:csabs:category/types"
    ],
    "kind": "urn:csabs:kind/data-type",
    "definition": "A carrier A equipped with an exhaustive duplicate-free finite set of all its values.",
    "notation": "Finite(A) ⇔ ∃U∈FinSet(A), ∀a:A, a∈U",
    "requiresConcept": [
      "urn:csabs:concept/FiniteSet",
      "urn:csabs:concept/NaturalNumber"
    ],
    "relatedConcept": [],
    "hasOperation": [
      "urn:csabs:operation/FiniteType-universe",
      "urn:csabs:operation/FiniteType-cardinality"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/FiniteType-exhaustive",
      "urn:csabs:axiom/FiniteType-finite-enumeration",
      "urn:csabs:axiom/FiniteType-card-definition"
    ],
    "hasLaw": [
      "urn:csabs:law/FiniteType-enumeration-unique"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/FiniteType-zero-cardinality"
    ],
    "axiomBasis": "∀a:A, a∈universe_A; universe_A is a finite set; equality is set equality; card_A=|universe_A|",
    "basisKind": "extensional-structural-definition",
    "basisScope": "The empty carrier is permitted. Enumeration has no observable order; finiteness is evidence about A, not a finite collection drawn from a possibly infinite carrier. Equality of evidence is proof irrelevant in the Lean model.",
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Map carrier, equality, operation definedness and stated profile to the target API or proof context.",
      "Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.",
      "Model coverage does not establish every recorded claim or an implementation refinement."
    ],
    "reviewStatus": "Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.",
    "source": [
      "urn:csabs:source/mathlib-finite-core"
    ],
    "sourceLocator": "Fintype.elems and Fintype.complete",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted",
    "leanFormulation": "abbrev FiniteType (A : Type u) := Fintype A",
    "formulationSource": "urn:csabs:source/local-lean-CoreData",
    "formulationLocator": "Catalog.FiniteType",
    "formulationScope": "model",
    "leanModelMapping": "Catalog.FiniteType A is Fintype A evidence, bundling a Finset enumeration and completeness proof; A remains the actual value carrier. Finite(A) ⇔ ∃U∈FinSet(A), ∀a:A, a∈U. The empty carrier is permitted. Enumeration has no observable order; finiteness is evidence about A, not a finite collection drawn from a possibly infinite carrier. Equality of evidence is proof irrelevant in the Lean model.",
    "leanModelLimitations": "Compiled carrier and selected interface interpretation. Some catalog operations are specified mathematically rather than wrapped as Lean declarations; no blanket proof of claims, algorithms, parsing, liveness or complexity. See individual witnesses.",
    "mathematicalFormulation": "A finite-type structure on A supplies an enumeration E containing each a∈A exactly once. |A| is the enumeration cardinality; the empty type is permitted."
  },
  {
    "id": "urn:csabs:operation/FiniteType-universe",
    "type": "Operation",
    "name": "universe",
    "signature": "universe_A : FinSet(A)",
    "description": "Returns all values of A, without duplicates.",
    "concept": "urn:csabs:concept/FiniteType",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. The empty carrier is permitted. Enumeration has no observable order; finiteness is evidence about A, not a finite collection drawn from a possibly infinite carrier. Equality of evidence is proof irrelevant in the Lean model.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Returns all values of A, without duplicates.",
    "source": [
      "urn:csabs:source/mathlib-finite-core"
    ],
    "sourceLocator": "Fintype.elems and Fintype.complete",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/FiniteType-cardinality",
    "type": "Operation",
    "name": "cardinality",
    "signature": "card_A : ℕ",
    "description": "card_A=|universe_A|.",
    "concept": "urn:csabs:concept/FiniteType",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. The empty carrier is permitted. Enumeration has no observable order; finiteness is evidence about A, not a finite collection drawn from a possibly infinite carrier. Equality of evidence is proof irrelevant in the Lean model.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "card_A=|universe_A|.",
    "source": [
      "urn:csabs:source/mathlib-finite-core"
    ],
    "sourceLocator": "Fintype.elems and Fintype.complete",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/FiniteType-exhaustive",
    "type": "Axiom",
    "name": "exhaustive",
    "statement": "Defining requirement: ∀a:A, a∈universe_A",
    "formalStatement": "∀a:A, a∈universe_A",
    "assumptions": [
      "The empty carrier is permitted. Enumeration has no observable order; finiteness is evidence about A, not a finite collection drawn from a possibly infinite carrier. Equality of evidence is proof irrelevant in the Lean model.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/FiniteType"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/mathlib-finite-core"
    ],
    "sourceLocator": "Fintype.elems and Fintype.complete",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/FiniteType-finite-enumeration",
    "type": "Axiom",
    "name": "finite-enumeration",
    "statement": "Defining requirement: universe_A is a finite set; equality is set equality",
    "formalStatement": "universe_A is a finite set; equality is set equality",
    "assumptions": [
      "The empty carrier is permitted. Enumeration has no observable order; finiteness is evidence about A, not a finite collection drawn from a possibly infinite carrier. Equality of evidence is proof irrelevant in the Lean model.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/FiniteType"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/mathlib-finite-core"
    ],
    "sourceLocator": "Fintype.elems and Fintype.complete",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/FiniteType-card-definition",
    "type": "Axiom",
    "name": "card-definition",
    "statement": "Defining requirement: card_A=|universe_A|",
    "formalStatement": "card_A=|universe_A|",
    "assumptions": [
      "The empty carrier is permitted. Enumeration has no observable order; finiteness is evidence about A, not a finite collection drawn from a possibly infinite carrier. Equality of evidence is proof irrelevant in the Lean model.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/FiniteType"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/mathlib-finite-core"
    ],
    "sourceLocator": "Fintype.elems and Fintype.complete",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/FiniteType-enumeration-unique",
    "type": "Law",
    "name": "enumeration-unique",
    "statement": "(∀a:A, a∈U) ⇒ U=universe_A, for U∈FinSet(A)",
    "formalStatement": "(∀a:A, a∈U) ⇒ U=universe_A, for U∈FinSet(A)",
    "assumptions": [
      "The empty carrier is permitted. Enumeration has no observable order; finiteness is evidence about A, not a finite collection drawn from a possibly infinite carrier. Equality of evidence is proof irrelevant in the Lean model.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/FiniteType"
    ],
    "dependsOn": [
      "urn:csabs:axiom/FiniteType-exhaustive",
      "urn:csabs:axiom/FiniteType-finite-enumeration"
    ],
    "proofSketch": "Both sets contain exactly the values of A; use set extensionality.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/mathlib-finite-core"
    ],
    "sourceLocator": "Fintype.elems and Fintype.complete",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/FiniteType-zero-cardinality",
    "type": "Theorem",
    "name": "zero-cardinality",
    "statement": "card_A=0 ⇔ A has no values",
    "formalStatement": "card_A=0 ⇔ A has no values",
    "assumptions": [
      "The empty carrier is permitted. Enumeration has no observable order; finiteness is evidence about A, not a finite collection drawn from a possibly infinite carrier. Equality of evidence is proof irrelevant in the Lean model.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/FiniteType"
    ],
    "dependsOn": [
      "urn:csabs:axiom/FiniteType-exhaustive",
      "urn:csabs:axiom/FiniteType-finite-enumeration",
      "urn:csabs:axiom/FiniteType-card-definition"
    ],
    "proofSketch": "A finite set has size zero iff empty; use exhaustiveness.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/mathlib-finite-core"
    ],
    "sourceLocator": "Fintype.elems and Fintype.complete",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
