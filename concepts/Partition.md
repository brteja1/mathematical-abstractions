# Partition of a set

A family of nonempty, pairwise disjoint subsets whose union is the entire carrier.

**Notation:** Π ⊆ 𝒫(A)\{∅}; ⋃Π=A; ∀X,Y∈Π, X≠Y⇒X∩Y=∅.

**Stable ID:** `urn:csabs:concept/Partition`

**Categories:** Set theory and foundations

**Kind:** Mathematical construction

## Backlinks

- [Disjoint-set union with representatives](DisjointSet.md) — `requiresConcept`
- [Equivalence relation](EquivalenceRelation.md) — `relatedConcept`

## Interface and scope

**axiomBasis:** Selected presentation: A family of nonempty, pairwise disjoint subsets whose union is the entire carrier. Governing rules: Every carrier element belongs to a block of the partition. Distinct blocks are pairwise disjoint and blocks are nonempty. Blocks are nonempty, disjoint, and cover the carrier, including the empty family when the carrier is empty.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**verificationObligation:** Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

**provenanceStatus:** legacy-source-missing

## Operations

<a id="node-urn-csabs-operation-Partition-basis-blockOf"></a>

### blockOf

`urn:csabs:operation/Partition-basis-blockOf`

**signature:** blockOf : A→Π

**description:** Returns the unique block containing a carrier element, using cover and disjointness; requires no computational decidability.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-partition-cover"></a>

### partition-cover

`urn:csabs:axiom/partition-cover`

**statement:** Every carrier element belongs to a block of the partition.

**formalStatement:** ⋃Π=A

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

**assumptions:** Use the linked concept’s explicit basis and carrier conventions.

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-partition-disjoint"></a>

### partition-disjoint

`urn:csabs:axiom/partition-disjoint`

**statement:** Distinct blocks are pairwise disjoint and blocks are nonempty.

**formalStatement:** ∀X,Y∈Π: X≠Y⇒X∩Y=∅; ∀X∈Π: X≠∅

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

**assumptions:** Use the linked concept’s explicit basis and carrier conventions.

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Partition-blocks"></a>

### blocks

`urn:csabs:axiom/Partition-blocks`

**statement:** Blocks are nonempty, disjoint, and cover the carrier, including the empty family when the carrier is empty.

**formalStatement:** Π⊆𝒫(A); ∅∉Π; ⋃Π=A; X,Y∈Π ∧ X≠Y ⇒ X∩Y=∅

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-equivalence-partition-correspondence"></a>

### theorem/equivalence-partition-correspondence

`urn:csabs:theorem/equivalence-partition-correspondence`

**statement:** Equivalence relations on A correspond bijectively to partitions of A by their equivalence classes.

**assumptions:** underlying carrier A fixed

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [equivalence-reflexive](EquivalenceRelation.md#node-urn-csabs-axiom-equivalence-reflexive); [equivalence-symmetric](EquivalenceRelation.md#node-urn-csabs-axiom-equivalence-symmetric); [equivalence-transitive](EquivalenceRelation.md#node-urn-csabs-axiom-equivalence-transitive); [class-definition](EquivalenceRelation.md#node-urn-csabs-axiom-EquivalenceRelation-class-definition); [partition-cover](Partition.md#node-urn-csabs-axiom-partition-cover); [partition-disjoint](Partition.md#node-urn-csabs-axiom-partition-disjoint); [blocks](Partition.md#node-urn-csabs-axiom-Partition-blocks)

**formalStatement:** Equiv(A) ≅ Partitions(A); R↦{[a]_R:a∈A}; Π↦{(a,b):∃B∈Π:a∈B∧b∈B}

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-theorem-Partition-unique-block"></a>

### unique-block

`urn:csabs:theorem/Partition-unique-block`

**statement:** Each carrier element is in exactly one partition block.

**formalStatement:** ∀a∈A ∃!X∈Π:a∈X

**proofSketch:** Cover gives existence; disjointness forbids membership in distinct blocks.

**assumptions:** The explicit basis, carriers, and side conditions stated for Partition apply.

**dependsOn:** [partition-cover](Partition.md#node-urn-csabs-axiom-partition-cover); [partition-disjoint](Partition.md#node-urn-csabs-axiom-partition-disjoint); [blocks](Partition.md#node-urn-csabs-axiom-Partition-blocks)

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
    "id": "urn:csabs:concept/Partition",
    "type": "Concept",
    "shortForm": "Partition",
    "fullName": "Partition of a set",
    "category": [
      "urn:csabs:category/foundations"
    ],
    "kind": "urn:csabs:kind/construction",
    "definition": "A family of nonempty, pairwise disjoint subsets whose union is the entire carrier.",
    "notation": "Π ⊆ 𝒫(A)\\{∅}; ⋃Π=A; ∀X,Y∈Π, X≠Y⇒X∩Y=∅.",
    "hasOperation": [
      "urn:csabs:operation/Partition-basis-blockOf"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/partition-cover",
      "urn:csabs:axiom/partition-disjoint",
      "urn:csabs:axiom/Partition-blocks"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/equivalence-partition-correspondence",
      "urn:csabs:theorem/Partition-unique-block"
    ],
    "coverageStatus": "basis-reviewed",
    "requiresConcept": [],
    "verificationObligation": [
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: A family of nonempty, pairwise disjoint subsets whose union is the entire carrier. Governing rules: Every carrier element belongs to a block of the partition. Distinct blocks are pairwise disjoint and blocks are nonempty. Blocks are nonempty, disjoint, and cover the carrier, including the empty family when the carrier is empty.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:operation/Partition-basis-blockOf",
    "type": "Operation",
    "name": "blockOf",
    "signature": "blockOf : A→Π",
    "description": "Returns the unique block containing a carrier element, using cover and disjointness; requires no computational decidability.",
    "concept": "urn:csabs:concept/Partition"
  },
  {
    "id": "urn:csabs:axiom/partition-cover",
    "type": "Axiom",
    "statement": "Every carrier element belongs to a block of the partition.",
    "formalStatement": "⋃Π=A",
    "appliesTo": [
      "urn:csabs:concept/Partition"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law",
    "name": "partition-cover",
    "assumptions": [
      "Use the linked concept’s explicit basis and carrier conventions."
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/partition-disjoint",
    "type": "Axiom",
    "statement": "Distinct blocks are pairwise disjoint and blocks are nonempty.",
    "formalStatement": "∀X,Y∈Π: X≠Y⇒X∩Y=∅; ∀X∈Π: X≠∅",
    "appliesTo": [
      "urn:csabs:concept/Partition"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law",
    "name": "partition-disjoint",
    "assumptions": [
      "Use the linked concept’s explicit basis and carrier conventions."
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/Partition-blocks",
    "type": "Axiom",
    "name": "blocks",
    "statement": "Blocks are nonempty, disjoint, and cover the carrier, including the empty family when the carrier is empty.",
    "formalStatement": "Π⊆𝒫(A); ∅∉Π; ⋃Π=A; X,Y∈Π ∧ X≠Y ⇒ X∩Y=∅",
    "appliesTo": [
      "urn:csabs:concept/Partition"
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
    "id": "urn:csabs:theorem/Partition-unique-block",
    "type": "Theorem",
    "name": "unique-block",
    "statement": "Each carrier element is in exactly one partition block.",
    "formalStatement": "∀a∈A ∃!X∈Π:a∈X",
    "proofSketch": "Cover gives existence; disjointness forbids membership in distinct blocks.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for Partition apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/Partition"
    ],
    "dependsOn": [
      "urn:csabs:axiom/partition-cover",
      "urn:csabs:axiom/partition-disjoint",
      "urn:csabs:axiom/Partition-blocks"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
