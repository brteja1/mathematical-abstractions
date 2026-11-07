# Power set

The set containing exactly all subsets of a given set.

**Notation:** 𝒫(A) = {X | X ⊆ A}.

**Stable ID:** `urn:csabs:concept/PowerSet`

**Categories:** Set theory and foundations

**Kind:** Mathematical construction

**Related concepts:** [Set](Set.md)

## Backlinks

- [Measurable space (sigma-algebra on a carrier)](MeasurableSpace.md) — `requiresConcept`
- [Nondeterministic finite automaton without epsilon moves](NFA.md) — `requiresConcept`
- [Set](Set.md) — `relatedConcept`
- [Topological space (topology on a carrier)](TopologicalSpace.md) — `requiresConcept`

## Interface and scope

**axiomBasis:** Selected presentation: The set containing exactly all subsets of a given set. Governing rules: There is a set containing exactly the subsets of every given set.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**verificationObligation:** Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

**provenanceStatus:** legacy-source-missing

## Operations

<a id="node-urn-csabs-operation-powerset-membership"></a>

### subset membership

`urn:csabs:operation/powerset-membership`

**signature:** X ∈ 𝒫(A) iff X ⊆ A

**description:** Tests whether a candidate set is a member of the power set.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-PowerSet-existence"></a>

### existence

`urn:csabs:axiom/PowerSet-existence`

**statement:** There is a set containing exactly the subsets of every given set.

**formalStatement:** ∀A ∃P ∀X: X∈P iff X⊆A

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

<a id="node-urn-csabs-law-powerset-membership"></a>

### law/powerset-membership

`urn:csabs:law/powerset-membership`

**statement:** A set belongs to the power set exactly when it is a subset of the carrier.

**formalStatement:** X∈𝒫(A) ↔ X⊆A

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [existence](PowerSet.md#node-urn-csabs-axiom-PowerSet-existence)

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

<a id="node-urn-csabs-theorem-PowerSet-monotonicity"></a>

### monotonicity

`urn:csabs:theorem/PowerSet-monotonicity`

**statement:** Power set is monotone under inclusion.

**formalStatement:** A⊆B ⇒ 𝒫(A)⊆𝒫(B)

**proofSketch:** Every subset of A is a subset of B by transitivity of inclusion.

**assumptions:** The explicit basis, carriers, and side conditions stated for PowerSet apply.

**dependsOn:** [existence](PowerSet.md#node-urn-csabs-axiom-PowerSet-existence)

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
    "id": "urn:csabs:concept/PowerSet",
    "type": "Concept",
    "shortForm": "PowerSet",
    "fullName": "Power set",
    "category": [
      "urn:csabs:category/foundations"
    ],
    "kind": "urn:csabs:kind/construction",
    "definition": "The set containing exactly all subsets of a given set.",
    "notation": "𝒫(A) = {X | X ⊆ A}.",
    "hasOperation": [
      "urn:csabs:operation/powerset-membership"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/PowerSet-existence"
    ],
    "hasLaw": [
      "urn:csabs:law/powerset-membership"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/cantor",
      "urn:csabs:theorem/PowerSet-monotonicity"
    ],
    "specializationOf": [],
    "coverageStatus": "basis-reviewed",
    "requiresConcept": [],
    "verificationObligation": [
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: The set containing exactly all subsets of a given set. Governing rules: There is a set containing exactly the subsets of every given set.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "provenanceStatus": "legacy-source-missing",
    "relatedConcept": [
      "urn:csabs:concept/Set"
    ]
  },
  {
    "id": "urn:csabs:operation/powerset-membership",
    "type": "Operation",
    "name": "subset membership",
    "signature": "X ∈ 𝒫(A) iff X ⊆ A",
    "description": "Tests whether a candidate set is a member of the power set.",
    "concept": "urn:csabs:concept/PowerSet"
  },
  {
    "id": "urn:csabs:axiom/PowerSet-existence",
    "type": "Axiom",
    "name": "existence",
    "statement": "There is a set containing exactly the subsets of every given set.",
    "formalStatement": "∀A ∃P ∀X: X∈P iff X⊆A",
    "appliesTo": [
      "urn:csabs:concept/PowerSet"
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
    "id": "urn:csabs:law/powerset-membership",
    "type": "Law",
    "statement": "A set belongs to the power set exactly when it is a subset of the carrier.",
    "formalStatement": "X∈𝒫(A) ↔ X⊆A",
    "appliesTo": [
      "urn:csabs:concept/PowerSet"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/PowerSet-existence"
    ],
    "assumptions": [
      "Use the explicit mathematical bases and typed carriers of the linked concepts."
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/cantor",
    "type": "Theorem",
    "statement": "For every set A, its power set has strictly greater cardinality than A.",
    "formalStatement": "|𝒫(A)|>|A|",
    "assumptions": [
      "standard set theory"
    ],
    "appliesTo": [
      "urn:csabs:concept/Set",
      "urn:csabs:concept/PowerSet"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "proofSketch": "If f:A→𝒫(A) were onto, D={x∈A:x∉f(x)} would equal f(d) for some d; then d∈D iff d∉D, a contradiction.",
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
      "urn:csabs:axiom/Set-foundation",
      "urn:csabs:axiom/PowerSet-existence"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/PowerSet-monotonicity",
    "type": "Theorem",
    "name": "monotonicity",
    "statement": "Power set is monotone under inclusion.",
    "formalStatement": "A⊆B ⇒ 𝒫(A)⊆𝒫(B)",
    "proofSketch": "Every subset of A is a subset of B by transitivity of inclusion.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for PowerSet apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/PowerSet"
    ],
    "dependsOn": [
      "urn:csabs:axiom/PowerSet-existence"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
