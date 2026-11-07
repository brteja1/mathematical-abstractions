# Measurable space (sigma-algebra on a carrier)

A carrier X equipped with a family Σ of measurable subsets closed under complement and countable union and containing the empty set.

**Notation:** (X,Σ); Σ⊆𝒫(X)

**Stable ID:** `urn:csabs:concept/MeasurableSpace`

**Categories:** Measure theory

**Kind:** Mathematical structure

**Prerequisites:** [Set](Set.md), [Power set](PowerSet.md)

## Backlinks

- [Measurable function](MeasurableFunction.md) — `requiresConcept`
- [Measure space (nonnegative countably additive measure)](MeasureSpace.md) — `requiresConcept`
- [Measure space (nonnegative countably additive measure)](MeasureSpace.md) — `specializationOf`
- [Topological space (topology on a carrier)](TopologicalSpace.md) — `relatedConcept`

## Interface and scope

**axiomBasis:** A sigma-algebra contains ∅, is closed under complement in X and under unions indexed by ℕ.

**basisKind:** defined-structure

**basisScope:** Sigma-algebra interface and countable-intersection closure; no measure is selected.

**verificationObligation:** X may be empty. Measurable sets use extensional set equality. Arbitrary uncountable unions need not be measurable.; Use the stated carriers and equality. Specialization does not automatically transfer operations or claims.

**reviewStatus:** editorial interface review; not machine-proved

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-MeasurableSpace-complement"></a>

### complement

`urn:csabs:operation/MeasurableSpace-complement`

**signature:** Σ → Σ; E ↦ X∖E

**description:** Complement relative to the fixed carrier X.

**precondition:** Inputs belong to the stated domains.

**postcondition:** Complement relative to the fixed carrier X.

**totality:** total on the stated domain

<a id="node-urn-csabs-operation-MeasurableSpace-countable-union"></a>

### countable-union

`urn:csabs:operation/MeasurableSpace-countable-union`

**signature:** (ℕ → Σ) → Σ; (Eₙ) ↦ ⋃ₙEₙ

**description:** Union of a countable measurable family; an empty union is ∅.

**precondition:** Inputs belong to the stated domains.

**postcondition:** Union of a countable measurable family; an empty union is ∅.

**totality:** total on the stated domain

## Axioms and defining rules

<a id="node-urn-csabs-axiom-MeasurableSpace-empty"></a>

### empty

`urn:csabs:axiom/MeasurableSpace-empty`

**statement:** The empty set is measurable.

**formalStatement:** ∅∈Σ

**assumptions:** (X,Σ); Σ⊆𝒫(X); Use the concept’s declared semantic conventions.

**reviewStatus:** editorial definition; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Sheldon Axler, Measure, Integration & Real Analysis (2020; consulted revision dated 12 June 2026)](https://measure.axler.net/MIRA.pdf); accessedOn: 2026-11-07; sourceRole: primary mathematical reference; license: CC BY-NC 4.0; licenseUrl: https://creativecommons.org/licenses/by-nc/4.0/

**sourceLocator:** §2B, Definition 2.23

**sourceNote:** Defining constraint or equation adapted to the declared carriers and catalog notation.

**provenanceKind:** adapted

**ruleRole:** structure-law

<a id="node-urn-csabs-axiom-MeasurableSpace-complement"></a>

### complement

`urn:csabs:axiom/MeasurableSpace-complement`

**statement:** Measurable sets have measurable complements.

**formalStatement:** E∈Σ ⇒ X∖E∈Σ

**assumptions:** (X,Σ); Σ⊆𝒫(X); Use the concept’s declared semantic conventions.

**reviewStatus:** editorial definition; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Sheldon Axler, Measure, Integration & Real Analysis (2020; consulted revision dated 12 June 2026)](https://measure.axler.net/MIRA.pdf); accessedOn: 2026-11-07; sourceRole: primary mathematical reference; license: CC BY-NC 4.0; licenseUrl: https://creativecommons.org/licenses/by-nc/4.0/

**sourceLocator:** §2B, Definition 2.23

**sourceNote:** Defining constraint or equation adapted to the declared carriers and catalog notation.

**provenanceKind:** adapted

**ruleRole:** structure-law

<a id="node-urn-csabs-axiom-MeasurableSpace-countable-union"></a>

### countable-union

`urn:csabs:axiom/MeasurableSpace-countable-union`

**statement:** A countable union of measurable sets is measurable.

**formalStatement:** (∀n∈ℕ:Eₙ∈Σ) ⇒ ⋃ₙEₙ∈Σ

**assumptions:** (X,Σ); Σ⊆𝒫(X); Use the concept’s declared semantic conventions.

**reviewStatus:** editorial definition; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Sheldon Axler, Measure, Integration & Real Analysis (2020; consulted revision dated 12 June 2026)](https://measure.axler.net/MIRA.pdf); accessedOn: 2026-11-07; sourceRole: primary mathematical reference; license: CC BY-NC 4.0; licenseUrl: https://creativecommons.org/licenses/by-nc/4.0/

**sourceLocator:** §2B, Definition 2.23

**sourceNote:** Defining constraint or equation adapted to the declared carriers and catalog notation.

**provenanceKind:** adapted

**ruleRole:** structure-law

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-MeasurableSpace-countable-intersection"></a>

### countable-intersection

`urn:csabs:theorem/MeasurableSpace-countable-intersection`

**statement:** A countable intersection of measurable sets is measurable.

**formalStatement:** (∀n∈ℕ:Eₙ∈Σ) ⇒ ⋂ₙEₙ∈Σ; ⋂∅=X

**assumptions:** (X,Σ); Σ⊆𝒫(X); Use the concept’s declared semantic conventions.

**reviewStatus:** editorial derivation; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Sheldon Axler, Measure, Integration & Real Analysis (2020; consulted revision dated 12 June 2026)](https://measure.axler.net/MIRA.pdf); accessedOn: 2026-11-07; sourceRole: primary mathematical reference; license: CC BY-NC 4.0; licenseUrl: https://creativecommons.org/licenses/by-nc/4.0/

**sourceLocator:** §2B, result 2.25

**sourceNote:** Derived from the linked local premises; proof sketch gives the adaptation.

**provenanceKind:** derived

**dependsOn:** [empty](MeasurableSpace.md#node-urn-csabs-axiom-MeasurableSpace-empty); [complement](MeasurableSpace.md#node-urn-csabs-axiom-MeasurableSpace-complement); [countable-union](MeasurableSpace.md#node-urn-csabs-axiom-MeasurableSpace-countable-union)

**proofSketch:** Complement each Eₙ, take their countable union, and complement again. The empty intersection is X, measurable as the complement of ∅.

## Concept provenance

- [Sheldon Axler, Measure, Integration & Real Analysis (2020; consulted revision dated 12 June 2026)](https://measure.axler.net/MIRA.pdf); accessedOn: 2026-11-07; sourceRole: primary mathematical reference; license: CC BY-NC 4.0; licenseUrl: https://creativecommons.org/licenses/by-nc/4.0/

**sourceLocator:** §2B, Definitions 2.23 and 2.26; result 2.25

**sourceNote:** Interface adapted to the catalog notation and explicitly restricted to the stated scope.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/MeasurableSpace",
    "type": "Concept",
    "shortForm": "MeasurableSpace",
    "fullName": "Measurable space (sigma-algebra on a carrier)",
    "category": [
      "urn:csabs:category/measure-theory"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "A carrier X equipped with a family Σ of measurable subsets closed under complement and countable union and containing the empty set.",
    "notation": "(X,Σ); Σ⊆𝒫(X)",
    "hasOperation": [
      "urn:csabs:operation/MeasurableSpace-complement",
      "urn:csabs:operation/MeasurableSpace-countable-union"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/MeasurableSpace-empty",
      "urn:csabs:axiom/MeasurableSpace-complement",
      "urn:csabs:axiom/MeasurableSpace-countable-union"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/MeasurableSpace-countable-intersection"
    ],
    "axiomBasis": "A sigma-algebra contains ∅, is closed under complement in X and under unions indexed by ℕ.",
    "basisKind": "defined-structure",
    "basisScope": "Sigma-algebra interface and countable-intersection closure; no measure is selected.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "editorial interface review; not machine-proved",
    "requiresConcept": [
      "urn:csabs:concept/Set",
      "urn:csabs:concept/PowerSet"
    ],
    "verificationObligation": [
      "X may be empty. Measurable sets use extensional set equality. Arbitrary uncountable unions need not be measurable.",
      "Use the stated carriers and equality. Specialization does not automatically transfer operations or claims."
    ],
    "source": [
      "urn:csabs:source/axler-mira"
    ],
    "sourceLocator": "§2B, Definitions 2.23 and 2.26; result 2.25",
    "sourceNote": "Interface adapted to the catalog notation and explicitly restricted to the stated scope.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/MeasurableSpace-complement",
    "type": "Operation",
    "name": "complement",
    "signature": "Σ → Σ; E ↦ X∖E",
    "description": "Complement relative to the fixed carrier X.",
    "concept": "urn:csabs:concept/MeasurableSpace",
    "precondition": "Inputs belong to the stated domains.",
    "postcondition": "Complement relative to the fixed carrier X.",
    "totality": "total on the stated domain"
  },
  {
    "id": "urn:csabs:operation/MeasurableSpace-countable-union",
    "type": "Operation",
    "name": "countable-union",
    "signature": "(ℕ → Σ) → Σ; (Eₙ) ↦ ⋃ₙEₙ",
    "description": "Union of a countable measurable family; an empty union is ∅.",
    "concept": "urn:csabs:concept/MeasurableSpace",
    "precondition": "Inputs belong to the stated domains.",
    "postcondition": "Union of a countable measurable family; an empty union is ∅.",
    "totality": "total on the stated domain"
  },
  {
    "id": "urn:csabs:axiom/MeasurableSpace-empty",
    "type": "Axiom",
    "name": "empty",
    "statement": "The empty set is measurable.",
    "formalStatement": "∅∈Σ",
    "appliesTo": [
      "urn:csabs:concept/MeasurableSpace"
    ],
    "assumptions": [
      "(X,Σ); Σ⊆𝒫(X)",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial definition; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/axler-mira"
    ],
    "sourceLocator": "§2B, Definition 2.23",
    "sourceNote": "Defining constraint or equation adapted to the declared carriers and catalog notation.",
    "provenanceKind": "adapted",
    "ruleRole": "structure-law"
  },
  {
    "id": "urn:csabs:axiom/MeasurableSpace-complement",
    "type": "Axiom",
    "name": "complement",
    "statement": "Measurable sets have measurable complements.",
    "formalStatement": "E∈Σ ⇒ X∖E∈Σ",
    "appliesTo": [
      "urn:csabs:concept/MeasurableSpace"
    ],
    "assumptions": [
      "(X,Σ); Σ⊆𝒫(X)",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial definition; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/axler-mira"
    ],
    "sourceLocator": "§2B, Definition 2.23",
    "sourceNote": "Defining constraint or equation adapted to the declared carriers and catalog notation.",
    "provenanceKind": "adapted",
    "ruleRole": "structure-law"
  },
  {
    "id": "urn:csabs:axiom/MeasurableSpace-countable-union",
    "type": "Axiom",
    "name": "countable-union",
    "statement": "A countable union of measurable sets is measurable.",
    "formalStatement": "(∀n∈ℕ:Eₙ∈Σ) ⇒ ⋃ₙEₙ∈Σ",
    "appliesTo": [
      "urn:csabs:concept/MeasurableSpace"
    ],
    "assumptions": [
      "(X,Σ); Σ⊆𝒫(X)",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial definition; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/axler-mira"
    ],
    "sourceLocator": "§2B, Definition 2.23",
    "sourceNote": "Defining constraint or equation adapted to the declared carriers and catalog notation.",
    "provenanceKind": "adapted",
    "ruleRole": "structure-law"
  },
  {
    "id": "urn:csabs:theorem/MeasurableSpace-countable-intersection",
    "type": "Theorem",
    "name": "countable-intersection",
    "statement": "A countable intersection of measurable sets is measurable.",
    "formalStatement": "(∀n∈ℕ:Eₙ∈Σ) ⇒ ⋂ₙEₙ∈Σ; ⋂∅=X",
    "appliesTo": [
      "urn:csabs:concept/MeasurableSpace"
    ],
    "assumptions": [
      "(X,Σ); Σ⊆𝒫(X)",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial derivation; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/axler-mira"
    ],
    "sourceLocator": "§2B, result 2.25",
    "sourceNote": "Derived from the linked local premises; proof sketch gives the adaptation.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/MeasurableSpace-empty",
      "urn:csabs:axiom/MeasurableSpace-complement",
      "urn:csabs:axiom/MeasurableSpace-countable-union"
    ],
    "proofSketch": "Complement each Eₙ, take their countable union, and complement again. The empty intersection is X, measurable as the complement of ∅."
  }
]
```
<!-- graph-record:end -->
