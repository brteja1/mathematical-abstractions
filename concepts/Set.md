# Set

A collection of distinct elements, characterized by which elements belong to it.

**Notation:** A set A; membership x ∈ A; extensional equality A = B iff ∀x (x ∈ A ↔ x ∈ B).

**Stable ID:** `urn:csabs:concept/Set`

**Categories:** Set theory and foundations

**Kind:** Mathematical structure

**Related concepts:** [Power set](PowerSet.md), [Cartesian product](CartesianProduct.md), [Binary relation](Relation.md), [Finite set collection](FiniteSet.md), [Formal language of finite words](FormalLanguage.md)

## Backlinks

- [Boolean algebra](BooleanAlgebra.md) — `relatedConcept`
- [Finite set collection](FiniteSet.md) — `requiresConcept`
- [Finite set collection](FiniteSet.md) — `specializationOf`
- [Formal language of finite words](FormalLanguage.md) — `requiresConcept`
- [Formal language of finite words](FormalLanguage.md) — `specializationOf`
- [Graph](Graph.md) — `requiresConcept`
- [Measurable space (sigma-algebra on a carrier)](MeasurableSpace.md) — `requiresConcept`
- [Multiset](Multiset.md) — `requiresConcept`
- [Pigeonhole Principle](PigeonholePrinciple.md) — `requiresConcept`
- [Power set](PowerSet.md) — `relatedConcept`
- [Binary relation](Relation.md) — `relatedConcept`
- [Named relational schema with attribute domains](RelationalSchema.md) — `requiresConcept`
- [Sum Type](SumType.md) — `requiresConcept`
- [Topological space (topology on a carrier)](TopologicalSpace.md) — `requiresConcept`

## Interface and scope

**axiomBasis:** Classical first-order ZF set theory with equality; extensionality, empty set, pairing, union, power set, infinity, separation and replacement schemas, and foundation. Choice is not assumed.

**basisKind:** foundational-theory

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**verificationObligation:** Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-set-membership"></a>

### membership

`urn:csabs:operation/set-membership`

**signature:** ∈ : U × 𝒫(U) → Bool

**description:** Tests whether an element belongs to a set; U is the universe of candidate elements.

<a id="node-urn-csabs-operation-set-union"></a>

### union

`urn:csabs:operation/set-union`

**signature:** ∪ : 𝒫(U) × 𝒫(U) → 𝒫(U)

**description:** Returns elements belonging to either operand.

<a id="node-urn-csabs-operation-set-intersection"></a>

### intersection

`urn:csabs:operation/set-intersection`

**signature:** ∩ : 𝒫(U) × 𝒫(U) → 𝒫(U)

**description:** Returns elements belonging to both operands.

<a id="node-urn-csabs-operation-set-subset"></a>

### subset

`urn:csabs:operation/set-subset`

**signature:** ⊆ : 𝒫(U) × 𝒫(U) → Bool

**description:** Holds when every element of the first set belongs to the second.

<a id="node-urn-csabs-operation-Set-basis-difference"></a>

### difference

`urn:csabs:operation/Set-basis-difference`

**signature:** difference : 𝒫(U)×𝒫(U)→𝒫(U)

**description:** Returns A−B={x∈A:x∉B}.

<a id="node-urn-csabs-operation-Set-basis-empty"></a>

### empty

`urn:csabs:operation/Set-basis-empty`

**signature:** empty : Set

**description:** Constructs the empty set.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-set-extensionality"></a>

### set-extensionality

`urn:csabs:axiom/set-extensionality`

**statement:** Two sets are equal exactly when they have the same members.

**formalStatement:** A=B ↔ ∀x (x∈A ↔ x∈B)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

**assumptions:** Use the linked concept’s explicit basis and carrier conventions.

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Set-empty"></a>

### empty

`urn:csabs:axiom/Set-empty`

**statement:** There exists a set with no members.

**formalStatement:** ∃e ∀x:x∉e

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** foundation-axiom-or-schema

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Set-pairing"></a>

### pairing

`urn:csabs:axiom/Set-pairing`

**statement:** Any two sets are members of a pair set containing exactly them.

**formalStatement:** ∀a,b ∃p ∀x:x∈p iff (x=a∨x=b)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** foundation-axiom-or-schema

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Set-union"></a>

### union

`urn:csabs:axiom/Set-union`

**statement:** Every set of sets has a union.

**formalStatement:** ∀A ∃U ∀x:x∈U iff ∃Y∈A:x∈Y

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** foundation-axiom-or-schema

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Set-power"></a>

### power

`urn:csabs:axiom/Set-power`

**statement:** Every set has a power set.

**formalStatement:** ∀A ∃P ∀X:X∈P iff X⊆A

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** foundation-axiom-or-schema

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Set-infinity"></a>

### infinity

`urn:csabs:axiom/Set-infinity`

**statement:** An inductive set exists.

**formalStatement:** ∃I:∅∈I ∧ ∀x∈I:x∪{x}∈I

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** foundation-axiom-or-schema

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Set-separation-schema"></a>

### separation-schema

`urn:csabs:axiom/Set-separation-schema`

**statement:** Every definable subcollection of an existing set is a set.

**formalStatement:** For every first-order formula φ(x,parameters), ∀A ∃B ∀x:x∈B iff (x∈A∧φ(x)); B not free in φ

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** foundation-axiom-or-schema

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Set-replacement-schema"></a>

### replacement-schema

`urn:csabs:axiom/Set-replacement-schema`

**statement:** The image of a set under a definable functional relation is a set.

**formalStatement:** For every first-order φ(x,y,parameters), (∀x∈A ∃!y:φ(x,y)) ⇒ ∃B ∀y:y∈B iff ∃x∈A:φ(x,y)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** foundation-axiom-or-schema

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Set-foundation"></a>

### foundation

`urn:csabs:axiom/Set-foundation`

**statement:** Every nonempty set contains a member disjoint from itself.

**formalStatement:** ∀A:A≠∅ ⇒ ∃x∈A:x∩A=∅

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** foundation-axiom-or-schema

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

<a id="node-urn-csabs-law-set-union-membership"></a>

### law/set-union-membership

`urn:csabs:law/set-union-membership`

**statement:** An element belongs to a union iff it belongs to at least one operand.

**formalStatement:** x∈A∪B ↔ (x∈A∨x∈B)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [set-extensionality](Set.md#node-urn-csabs-axiom-set-extensionality); [empty](Set.md#node-urn-csabs-axiom-Set-empty); [pairing](Set.md#node-urn-csabs-axiom-Set-pairing); [union](Set.md#node-urn-csabs-axiom-Set-union); [power](Set.md#node-urn-csabs-axiom-Set-power); [infinity](Set.md#node-urn-csabs-axiom-Set-infinity); [separation-schema](Set.md#node-urn-csabs-axiom-Set-separation-schema); [replacement-schema](Set.md#node-urn-csabs-axiom-Set-replacement-schema); [foundation](Set.md#node-urn-csabs-axiom-Set-foundation)

**assumptions:** Use the explicit mathematical bases and typed carriers of the linked concepts.

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-law-set-intersection-membership"></a>

### law/set-intersection-membership

`urn:csabs:law/set-intersection-membership`

**statement:** An element belongs to an intersection iff it belongs to both operands.

**formalStatement:** x∈A∩B ↔ (x∈A∧x∈B)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [set-extensionality](Set.md#node-urn-csabs-axiom-set-extensionality); [empty](Set.md#node-urn-csabs-axiom-Set-empty); [pairing](Set.md#node-urn-csabs-axiom-Set-pairing); [union](Set.md#node-urn-csabs-axiom-Set-union); [power](Set.md#node-urn-csabs-axiom-Set-power); [infinity](Set.md#node-urn-csabs-axiom-Set-infinity); [separation-schema](Set.md#node-urn-csabs-axiom-Set-separation-schema); [replacement-schema](Set.md#node-urn-csabs-axiom-Set-replacement-schema); [foundation](Set.md#node-urn-csabs-axiom-Set-foundation)

**assumptions:** Use the explicit mathematical bases and typed carriers of the linked concepts.

**provenanceStatus:** legacy-source-missing

## Theorems

<a id="node-urn-csabs-theorem-cantor"></a>

### theorem/cantor

`urn:csabs:theorem/cantor`

**statement:** For every set A, its power set has strictly greater cardinality than A.

**formalStatement:** |𝒫(A)|>|A|

**assumptions:** standard set theory

**reviewStatus:** editorial-summary; not machine-proved

**proofSketch:** If f:A→𝒫(A) were onto, D={x∈A:x∉f(x)} would equal f(d) for some d; then d∈D iff d∉D, a contradiction.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [set-extensionality](Set.md#node-urn-csabs-axiom-set-extensionality); [empty](Set.md#node-urn-csabs-axiom-Set-empty); [pairing](Set.md#node-urn-csabs-axiom-Set-pairing); [union](Set.md#node-urn-csabs-axiom-Set-union); [power](Set.md#node-urn-csabs-axiom-Set-power); [infinity](Set.md#node-urn-csabs-axiom-Set-infinity); [separation-schema](Set.md#node-urn-csabs-axiom-Set-separation-schema); [replacement-schema](Set.md#node-urn-csabs-axiom-Set-replacement-schema); [foundation](Set.md#node-urn-csabs-axiom-Set-foundation); [existence](PowerSet.md#node-urn-csabs-axiom-PowerSet-existence)

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-theorem-Set-subset-antisymmetry"></a>

### subset-antisymmetry

`urn:csabs:theorem/Set-subset-antisymmetry`

**statement:** Mutual inclusion implies set equality.

**formalStatement:** A⊆B ∧ B⊆A ⇒ A=B

**proofSketch:** Unfold inclusion and apply membership extensionality.

**assumptions:** The explicit basis, carriers, and side conditions stated for Set apply.

**dependsOn:** [set-extensionality](Set.md#node-urn-csabs-axiom-set-extensionality); [empty](Set.md#node-urn-csabs-axiom-Set-empty); [pairing](Set.md#node-urn-csabs-axiom-Set-pairing); [union](Set.md#node-urn-csabs-axiom-Set-union); [power](Set.md#node-urn-csabs-axiom-Set-power); [infinity](Set.md#node-urn-csabs-axiom-Set-infinity); [separation-schema](Set.md#node-urn-csabs-axiom-Set-separation-schema); [replacement-schema](Set.md#node-urn-csabs-axiom-Set-replacement-schema); [foundation](Set.md#node-urn-csabs-axiom-Set-foundation)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Concept provenance

- [Mathematical structure (Wikipedia)](https://en.wikipedia.org/wiki/Mathematical_structure); sourceRole: discovery

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/Set",
    "type": "Concept",
    "shortForm": "Set",
    "fullName": "Set",
    "category": [
      "urn:csabs:category/foundations"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "A collection of distinct elements, characterized by which elements belong to it.",
    "notation": "A set A; membership x ∈ A; extensional equality A = B iff ∀x (x ∈ A ↔ x ∈ B).",
    "source": [
      "urn:csabs:source/wikipedia-math-structure"
    ],
    "hasOperation": [
      "urn:csabs:operation/set-membership",
      "urn:csabs:operation/set-union",
      "urn:csabs:operation/set-intersection",
      "urn:csabs:operation/set-subset",
      "urn:csabs:operation/Set-basis-difference",
      "urn:csabs:operation/Set-basis-empty"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/set-extensionality",
      "urn:csabs:axiom/Set-empty",
      "urn:csabs:axiom/Set-pairing",
      "urn:csabs:axiom/Set-union",
      "urn:csabs:axiom/Set-power",
      "urn:csabs:axiom/Set-infinity",
      "urn:csabs:axiom/Set-separation-schema",
      "urn:csabs:axiom/Set-replacement-schema",
      "urn:csabs:axiom/Set-foundation"
    ],
    "hasLaw": [
      "urn:csabs:law/set-union-membership",
      "urn:csabs:law/set-intersection-membership"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/cantor",
      "urn:csabs:theorem/Set-subset-antisymmetry"
    ],
    "relatedConcept": [
      "urn:csabs:concept/PowerSet",
      "urn:csabs:concept/CartesianProduct",
      "urn:csabs:concept/Relation",
      "urn:csabs:concept/FiniteSet",
      "urn:csabs:concept/FormalLanguage"
    ],
    "coverageStatus": "basis-reviewed",
    "requiresConcept": [],
    "verificationObligation": [
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Classical first-order ZF set theory with equality; extensionality, empty set, pairing, union, power set, infinity, separation and replacement schemas, and foundation. Choice is not assumed.",
    "basisKind": "foundational-theory",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof"
  },
  {
    "id": "urn:csabs:operation/set-membership",
    "type": "Operation",
    "name": "membership",
    "signature": "∈ : U × 𝒫(U) → Bool",
    "description": "Tests whether an element belongs to a set; U is the universe of candidate elements.",
    "concept": "urn:csabs:concept/Set"
  },
  {
    "id": "urn:csabs:operation/set-union",
    "type": "Operation",
    "name": "union",
    "signature": "∪ : 𝒫(U) × 𝒫(U) → 𝒫(U)",
    "description": "Returns elements belonging to either operand.",
    "concept": "urn:csabs:concept/Set"
  },
  {
    "id": "urn:csabs:operation/set-intersection",
    "type": "Operation",
    "name": "intersection",
    "signature": "∩ : 𝒫(U) × 𝒫(U) → 𝒫(U)",
    "description": "Returns elements belonging to both operands.",
    "concept": "urn:csabs:concept/Set"
  },
  {
    "id": "urn:csabs:operation/set-subset",
    "type": "Operation",
    "name": "subset",
    "signature": "⊆ : 𝒫(U) × 𝒫(U) → Bool",
    "description": "Holds when every element of the first set belongs to the second.",
    "concept": "urn:csabs:concept/Set"
  },
  {
    "id": "urn:csabs:operation/Set-basis-difference",
    "type": "Operation",
    "name": "difference",
    "signature": "difference : 𝒫(U)×𝒫(U)→𝒫(U)",
    "description": "Returns A−B={x∈A:x∉B}.",
    "concept": "urn:csabs:concept/Set"
  },
  {
    "id": "urn:csabs:operation/Set-basis-empty",
    "type": "Operation",
    "name": "empty",
    "signature": "empty : Set",
    "description": "Constructs the empty set.",
    "concept": "urn:csabs:concept/Set"
  },
  {
    "id": "urn:csabs:axiom/set-extensionality",
    "type": "Axiom",
    "statement": "Two sets are equal exactly when they have the same members.",
    "formalStatement": "A=B ↔ ∀x (x∈A ↔ x∈B)",
    "appliesTo": [
      "urn:csabs:concept/Set"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law",
    "name": "set-extensionality",
    "assumptions": [
      "Use the linked concept’s explicit basis and carrier conventions."
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/Set-empty",
    "type": "Axiom",
    "name": "empty",
    "statement": "There exists a set with no members.",
    "formalStatement": "∃e ∀x:x∉e",
    "appliesTo": [
      "urn:csabs:concept/Set"
    ],
    "assumptions": [
      "All variables range over the carriers and semantic conventions specified in this concept."
    ],
    "ruleRole": "foundation-axiom-or-schema",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/Set-pairing",
    "type": "Axiom",
    "name": "pairing",
    "statement": "Any two sets are members of a pair set containing exactly them.",
    "formalStatement": "∀a,b ∃p ∀x:x∈p iff (x=a∨x=b)",
    "appliesTo": [
      "urn:csabs:concept/Set"
    ],
    "assumptions": [
      "All variables range over the carriers and semantic conventions specified in this concept."
    ],
    "ruleRole": "foundation-axiom-or-schema",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/Set-union",
    "type": "Axiom",
    "name": "union",
    "statement": "Every set of sets has a union.",
    "formalStatement": "∀A ∃U ∀x:x∈U iff ∃Y∈A:x∈Y",
    "appliesTo": [
      "urn:csabs:concept/Set"
    ],
    "assumptions": [
      "All variables range over the carriers and semantic conventions specified in this concept."
    ],
    "ruleRole": "foundation-axiom-or-schema",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/Set-power",
    "type": "Axiom",
    "name": "power",
    "statement": "Every set has a power set.",
    "formalStatement": "∀A ∃P ∀X:X∈P iff X⊆A",
    "appliesTo": [
      "urn:csabs:concept/Set"
    ],
    "assumptions": [
      "All variables range over the carriers and semantic conventions specified in this concept."
    ],
    "ruleRole": "foundation-axiom-or-schema",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/Set-infinity",
    "type": "Axiom",
    "name": "infinity",
    "statement": "An inductive set exists.",
    "formalStatement": "∃I:∅∈I ∧ ∀x∈I:x∪{x}∈I",
    "appliesTo": [
      "urn:csabs:concept/Set"
    ],
    "assumptions": [
      "All variables range over the carriers and semantic conventions specified in this concept."
    ],
    "ruleRole": "foundation-axiom-or-schema",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/Set-separation-schema",
    "type": "Axiom",
    "name": "separation-schema",
    "statement": "Every definable subcollection of an existing set is a set.",
    "formalStatement": "For every first-order formula φ(x,parameters), ∀A ∃B ∀x:x∈B iff (x∈A∧φ(x)); B not free in φ",
    "appliesTo": [
      "urn:csabs:concept/Set"
    ],
    "assumptions": [
      "All variables range over the carriers and semantic conventions specified in this concept."
    ],
    "ruleRole": "foundation-axiom-or-schema",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/Set-replacement-schema",
    "type": "Axiom",
    "name": "replacement-schema",
    "statement": "The image of a set under a definable functional relation is a set.",
    "formalStatement": "For every first-order φ(x,y,parameters), (∀x∈A ∃!y:φ(x,y)) ⇒ ∃B ∀y:y∈B iff ∃x∈A:φ(x,y)",
    "appliesTo": [
      "urn:csabs:concept/Set"
    ],
    "assumptions": [
      "All variables range over the carriers and semantic conventions specified in this concept."
    ],
    "ruleRole": "foundation-axiom-or-schema",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/Set-foundation",
    "type": "Axiom",
    "name": "foundation",
    "statement": "Every nonempty set contains a member disjoint from itself.",
    "formalStatement": "∀A:A≠∅ ⇒ ∃x∈A:x∩A=∅",
    "appliesTo": [
      "urn:csabs:concept/Set"
    ],
    "assumptions": [
      "All variables range over the carriers and semantic conventions specified in this concept."
    ],
    "ruleRole": "foundation-axiom-or-schema",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:law/set-union-membership",
    "type": "Law",
    "statement": "An element belongs to a union iff it belongs to at least one operand.",
    "formalStatement": "x∈A∪B ↔ (x∈A∨x∈B)",
    "appliesTo": [
      "urn:csabs:concept/Set"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/set-extensionality",
      "urn:csabs:axiom/Set-empty",
      "urn:csabs:axiom/Set-pairing",
      "urn:csabs:axiom/Set-union",
      "urn:csabs:axiom/Set-power",
      "urn:csabs:axiom/Set-infinity",
      "urn:csabs:axiom/Set-separation-schema",
      "urn:csabs:axiom/Set-replacement-schema",
      "urn:csabs:axiom/Set-foundation"
    ],
    "assumptions": [
      "Use the explicit mathematical bases and typed carriers of the linked concepts."
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:law/set-intersection-membership",
    "type": "Law",
    "statement": "An element belongs to an intersection iff it belongs to both operands.",
    "formalStatement": "x∈A∩B ↔ (x∈A∧x∈B)",
    "appliesTo": [
      "urn:csabs:concept/Set"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/set-extensionality",
      "urn:csabs:axiom/Set-empty",
      "urn:csabs:axiom/Set-pairing",
      "urn:csabs:axiom/Set-union",
      "urn:csabs:axiom/Set-power",
      "urn:csabs:axiom/Set-infinity",
      "urn:csabs:axiom/Set-separation-schema",
      "urn:csabs:axiom/Set-replacement-schema",
      "urn:csabs:axiom/Set-foundation"
    ],
    "assumptions": [
      "Use the explicit mathematical bases and typed carriers of the linked concepts."
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/Set-subset-antisymmetry",
    "type": "Theorem",
    "name": "subset-antisymmetry",
    "statement": "Mutual inclusion implies set equality.",
    "formalStatement": "A⊆B ∧ B⊆A ⇒ A=B",
    "proofSketch": "Unfold inclusion and apply membership extensionality.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for Set apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/Set"
    ],
    "dependsOn": [
      "urn:csabs:axiom/set-extensionality",
      "urn:csabs:axiom/Set-empty",
      "urn:csabs:axiom/Set-pairing",
      "urn:csabs:axiom/Set-union",
      "urn:csabs:axiom/Set-power",
      "urn:csabs:axiom/Set-infinity",
      "urn:csabs:axiom/Set-separation-schema",
      "urn:csabs:axiom/Set-replacement-schema",
      "urn:csabs:axiom/Set-foundation"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
