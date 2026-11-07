# Well Founded Relation

A relation for which every nonempty subset has a minimal element with respect to that relation.

**Notation:** ∀S⊆A, S≠∅ ⇒ ∃m∈S ∀x∈S: ¬(x R m)

**Stable ID:** `urn:csabs:concept/WellFoundedRelation`

**Categories:** Order and fixed points

**Kind:** Relation

**Prerequisites:** [Binary relation](Relation.md)

**Specializes:** [Binary relation](Relation.md)

## Backlinks

- [Termination Variant](TerminationVariant.md) — `requiresConcept`

## Interface and scope

**axiomBasis:** Selected presentation: A relation for which every nonempty subset has a minimal element with respect to that relation. Governing rules: Every nonempty subset has a predecessor-minimal member.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**specializationNote:** Use A=B and the same relation; well-foundedness is an additional constraint, not an assumption of reflexivity or totality.

**verificationObligation:** Instantiate carrier, equality, and stated semantic conventions before using this entry.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

**provenanceStatus:** legacy-source-missing

## Operations

<a id="node-urn-csabs-operation-WellFoundedRelation-basis-predecessor"></a>

### predecessor

`urn:csabs:operation/WellFoundedRelation-basis-predecessor`

**signature:** pred : A×A→Prop

**description:** Returns whether the first element is a predecessor of the second.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-WellFoundedRelation-minimal-element"></a>

### minimal-element

`urn:csabs:axiom/WellFoundedRelation-minimal-element`

**statement:** Every nonempty subset has a predecessor-minimal member.

**formalStatement:** ∀X⊆A:X≠∅ ⇒ ∃m∈X ∀x∈X:¬(x R m)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

<a id="node-urn-csabs-law-WellFoundedRelation-core"></a>

### law/WellFoundedRelation-core

`urn:csabs:law/WellFoundedRelation-core`

**statement:** Well-founded induction establishes a predicate by establishing it from all smaller cases.

**formalStatement:** [∀x ((∀y: yRx ⇒ P(y))⇒P(x))] ⇒ ∀x P(x)

**reviewStatus:** editorial-summary; not machine-proved

**assumptions:** Use the carrier and semantic convention in the linked concept definition.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [minimal-element](WellFoundedRelation.md#node-urn-csabs-axiom-WellFoundedRelation-minimal-element)

**provenanceStatus:** legacy-source-missing

## Theorems

<a id="node-urn-csabs-theorem-WellFoundedRelation-irreflexivity"></a>

### irreflexivity

`urn:csabs:theorem/WellFoundedRelation-irreflexivity`

**statement:** A well-founded relation has no self-edge.

**formalStatement:** ∀a:¬(a R a)

**proofSketch:** Apply the minimal-element property to the singleton containing a.

**assumptions:** The explicit basis, carriers, and side conditions stated for WellFoundedRelation apply.

**dependsOn:** [minimal-element](WellFoundedRelation.md#node-urn-csabs-axiom-WellFoundedRelation-minimal-element)

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
    "id": "urn:csabs:concept/WellFoundedRelation",
    "type": "Concept",
    "shortForm": "WellFoundedRelation",
    "fullName": "Well Founded Relation",
    "category": [
      "urn:csabs:category/order"
    ],
    "kind": "urn:csabs:kind/relation",
    "definition": "A relation for which every nonempty subset has a minimal element with respect to that relation.",
    "notation": "∀S⊆A, S≠∅ ⇒ ∃m∈S ∀x∈S: ¬(x R m)",
    "hasOperation": [
      "urn:csabs:operation/WellFoundedRelation-basis-predecessor"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/WellFoundedRelation-minimal-element"
    ],
    "hasLaw": [
      "urn:csabs:law/WellFoundedRelation-core"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/WellFoundedRelation-irreflexivity"
    ],
    "requiresConcept": [
      "urn:csabs:concept/Relation"
    ],
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Instantiate carrier, equality, and stated semantic conventions before using this entry.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: A relation for which every nonempty subset has a minimal element with respect to that relation. Governing rules: Every nonempty subset has a predecessor-minimal member.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "provenanceStatus": "legacy-source-missing",
    "specializationOf": [
      "urn:csabs:concept/Relation"
    ],
    "specializationNote": "Use A=B and the same relation; well-foundedness is an additional constraint, not an assumption of reflexivity or totality."
  },
  {
    "id": "urn:csabs:operation/WellFoundedRelation-basis-predecessor",
    "type": "Operation",
    "name": "predecessor",
    "signature": "pred : A×A→Prop",
    "description": "Returns whether the first element is a predecessor of the second.",
    "concept": "urn:csabs:concept/WellFoundedRelation"
  },
  {
    "id": "urn:csabs:axiom/WellFoundedRelation-minimal-element",
    "type": "Axiom",
    "name": "minimal-element",
    "statement": "Every nonempty subset has a predecessor-minimal member.",
    "formalStatement": "∀X⊆A:X≠∅ ⇒ ∃m∈X ∀x∈X:¬(x R m)",
    "appliesTo": [
      "urn:csabs:concept/WellFoundedRelation"
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
    "id": "urn:csabs:law/WellFoundedRelation-core",
    "type": "Law",
    "statement": "Well-founded induction establishes a predicate by establishing it from all smaller cases.",
    "formalStatement": "[∀x ((∀y: yRx ⇒ P(y))⇒P(x))] ⇒ ∀x P(x)",
    "appliesTo": [
      "urn:csabs:concept/WellFoundedRelation"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "assumptions": [
      "Use the carrier and semantic convention in the linked concept definition."
    ],
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/WellFoundedRelation-minimal-element"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/WellFoundedRelation-irreflexivity",
    "type": "Theorem",
    "name": "irreflexivity",
    "statement": "A well-founded relation has no self-edge.",
    "formalStatement": "∀a:¬(a R a)",
    "proofSketch": "Apply the minimal-element property to the singleton containing a.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for WellFoundedRelation apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/WellFoundedRelation"
    ],
    "dependsOn": [
      "urn:csabs:axiom/WellFoundedRelation-minimal-element"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
