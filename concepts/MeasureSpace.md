# Measure space (nonnegative countably additive measure)

A measurable space with a nonnegative extended-real measure defined on its measurable sets.

**Notation:** (X,Σ,μ); μ:Σ→[0,∞]

**Stable ID:** `urn:csabs:concept/MeasureSpace`

**Categories:** Measure theory

**Kind:** Mathematical structure

**Prerequisites:** [Measurable space (sigma-algebra on a carrier)](MeasurableSpace.md)

**Specializes:** [Measurable space (sigma-algebra on a carrier)](MeasurableSpace.md)

## Backlinks

- [Probability space (normalized measure)](ProbabilitySpace.md) — `requiresConcept`
- [Probability space (normalized measure)](ProbabilitySpace.md) — `specializationOf`

## Mathematical formulation

A measure space is (Ω,Σ,μ), where μ:Σ→[0,+∞], μ(∅)=0, and μ(⋃\_n A\_n)=Σ\_n μ(A\_n) for pairwise disjoint measurable A\_n. Lean represents μ on all sets with measure-theoretic extension conventions.

**Lean formulation** (in its source module context):

```lean
abbrev MeasureSpace (A : Type u) := MeasureTheory.MeasureSpace A
```

**Source:** [`Catalog.MeasureSpace`](../lean/Catalog/Probability.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Mathlib MeasureSpace bundles sigma-algebra and nonnegative extended-real countably additive measure.

**Limits:** Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Specify (X,Σ) as a MeasurableSpace, μ(∅)=0, and countable additivity on disjoint measurable families.

**basisKind:** defined-structure

**basisScope:** Nonnegative measures; finite additivity and monotonicity. Signed measures, outer measures and completeness are separate conventions.

**basisInstantiation:** Instantiate MeasurableSpace at (X,Σ); its sigma-algebra closure requirements remain obligations. Add μ with the empty-set and disjoint-countable-additivity rules listed here.

**specializationNote:** Forget μ and retain exactly the same X and Σ.

**verificationObligation:** The value ∞ is permitted. Do not subtract ∞ from ∞. No completeness or sigma-finiteness is assumed.; Use the stated carriers and equality. Specialization does not automatically transfer operations or claims.

**reviewStatus:** editorial interface review; not machine-proved

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-MeasureSpace-measure"></a>

### measure

`urn:csabs:operation/MeasureSpace-measure`

**signature:** Σ → [0,∞]; E ↦ μ(E)

**description:** Evaluate the measure only on measurable sets.

**precondition:** Inputs belong to the stated domains.

**postcondition:** Evaluate the measure only on measurable sets.

**totality:** total on the stated domain

## Axioms and defining rules

<a id="node-urn-csabs-axiom-MeasureSpace-empty"></a>

### empty

`urn:csabs:axiom/MeasureSpace-empty`

**statement:** The empty set has zero measure.

**formalStatement:** μ(∅)=0

**assumptions:** (X,Σ,μ); μ:Σ→[0,∞]; Use the concept’s declared semantic conventions.

**reviewStatus:** editorial definition; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Sheldon Axler, Measure, Integration & Real Analysis (2020; consulted revision dated 12 June 2026)](https://measure.axler.net/MIRA.pdf); accessedOn: 2026-11-07; sourceRole: primary mathematical reference; license: CC BY-NC 4.0; licenseUrl: https://creativecommons.org/licenses/by-nc/4.0/

**sourceLocator:** §2C, Definition 2.54

**sourceNote:** Defining constraint or equation adapted to the declared carriers and catalog notation.

**provenanceKind:** adapted

**ruleRole:** structure-law

<a id="node-urn-csabs-axiom-MeasureSpace-sigma-additivity"></a>

### sigma-additivity

`urn:csabs:axiom/MeasureSpace-sigma-additivity`

**statement:** Disjoint measurable sets have additive measure over countable unions.

**formalStatement:** Eₙ∈Σ and Eᵢ∩Eⱼ=∅ for i≠j ⇒ μ(⋃ₙEₙ)=∑ₙμ(Eₙ)

**assumptions:** (X,Σ,μ); μ:Σ→[0,∞]; Use the concept’s declared semantic conventions.

**reviewStatus:** editorial definition; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Sheldon Axler, Measure, Integration & Real Analysis (2020; consulted revision dated 12 June 2026)](https://measure.axler.net/MIRA.pdf); accessedOn: 2026-11-07; sourceRole: primary mathematical reference; license: CC BY-NC 4.0; licenseUrl: https://creativecommons.org/licenses/by-nc/4.0/

**sourceLocator:** §2C, Definition 2.54

**sourceNote:** Defining constraint or equation adapted to the declared carriers and catalog notation.

**provenanceKind:** adapted

**ruleRole:** structure-law

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-MeasureSpace-finite-additivity"></a>

### finite-additivity

`urn:csabs:theorem/MeasureSpace-finite-additivity`

**statement:** Two disjoint measurable sets have additive measure.

**formalStatement:** A,B∈Σ and A∩B=∅ ⇒ μ(A∪B)=μ(A)+μ(B)

**assumptions:** (X,Σ,μ); μ:Σ→[0,∞]; Use the concept’s declared semantic conventions.

**reviewStatus:** editorial derivation; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Sheldon Axler, Measure, Integration & Real Analysis (2020; consulted revision dated 12 June 2026)](https://measure.axler.net/MIRA.pdf); accessedOn: 2026-11-07; sourceRole: primary mathematical reference; license: CC BY-NC 4.0; licenseUrl: https://creativecommons.org/licenses/by-nc/4.0/

**sourceLocator:** §2C, result 2.57

**sourceNote:** Derived from the linked local premises; proof sketch gives the adaptation.

**provenanceKind:** derived

**dependsOn:** [empty](MeasureSpace.md#node-urn-csabs-axiom-MeasureSpace-empty); [sigma-additivity](MeasureSpace.md#node-urn-csabs-axiom-MeasureSpace-sigma-additivity)

**proofSketch:** Apply countable additivity to the family A,B,∅,∅,… and use μ(∅)=0.

<a id="node-urn-csabs-theorem-MeasureSpace-monotonicity"></a>

### monotonicity

`urn:csabs:theorem/MeasureSpace-monotonicity`

**statement:** Measure is monotone on measurable sets.

**formalStatement:** A,B∈Σ and A⊆B ⇒ μ(A)≤μ(B)

**assumptions:** (X,Σ,μ); μ:Σ→[0,∞]; Use the concept’s declared semantic conventions.

**reviewStatus:** editorial derivation; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Sheldon Axler, Measure, Integration & Real Analysis (2020; consulted revision dated 12 June 2026)](https://measure.axler.net/MIRA.pdf); accessedOn: 2026-11-07; sourceRole: primary mathematical reference; license: CC BY-NC 4.0; licenseUrl: https://creativecommons.org/licenses/by-nc/4.0/

**sourceLocator:** §2C, result 2.57

**sourceNote:** Derived from the linked local premises; proof sketch gives the adaptation.

**provenanceKind:** derived

**dependsOn:** [finite-additivity](MeasureSpace.md#node-urn-csabs-theorem-MeasureSpace-finite-additivity); [complement](MeasurableSpace.md#node-urn-csabs-axiom-MeasurableSpace-complement); [countable-intersection](MeasurableSpace.md#node-urn-csabs-theorem-MeasurableSpace-countable-intersection); [measure](MeasureSpace.md#node-urn-csabs-operation-MeasureSpace-measure)

**proofSketch:** B=A⊔(B∖A). The difference is measurable by complement and intersection closure; finite additivity and μ(B∖A)≥0 give the inequality even for infinite values.

## Concept provenance

- [Sheldon Axler, Measure, Integration & Real Analysis (2020; consulted revision dated 12 June 2026)](https://measure.axler.net/MIRA.pdf); accessedOn: 2026-11-07; sourceRole: primary mathematical reference; license: CC BY-NC 4.0; licenseUrl: https://creativecommons.org/licenses/by-nc/4.0/

**sourceLocator:** §2C, Definitions 2.54 and 2.56; result 2.57

**sourceNote:** Interface adapted to the catalog notation and explicitly restricted to the stated scope.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/MeasureSpace",
    "type": "Concept",
    "shortForm": "MeasureSpace",
    "fullName": "Measure space (nonnegative countably additive measure)",
    "category": [
      "urn:csabs:category/measure-theory"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "A measurable space with a nonnegative extended-real measure defined on its measurable sets.",
    "notation": "(X,Σ,μ); μ:Σ→[0,∞]",
    "hasOperation": [
      "urn:csabs:operation/MeasureSpace-measure"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/MeasureSpace-empty",
      "urn:csabs:axiom/MeasureSpace-sigma-additivity"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/MeasureSpace-finite-additivity",
      "urn:csabs:theorem/MeasureSpace-monotonicity"
    ],
    "axiomBasis": "Specify (X,Σ) as a MeasurableSpace, μ(∅)=0, and countable additivity on disjoint measurable families.",
    "basisKind": "defined-structure",
    "basisScope": "Nonnegative measures; finite additivity and monotonicity. Signed measures, outer measures and completeness are separate conventions.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "editorial interface review; not machine-proved",
    "requiresConcept": [
      "urn:csabs:concept/MeasurableSpace"
    ],
    "verificationObligation": [
      "The value ∞ is permitted. Do not subtract ∞ from ∞. No completeness or sigma-finiteness is assumed.",
      "Use the stated carriers and equality. Specialization does not automatically transfer operations or claims."
    ],
    "source": [
      "urn:csabs:source/axler-mira"
    ],
    "sourceLocator": "§2C, Definitions 2.54 and 2.56; result 2.57",
    "sourceNote": "Interface adapted to the catalog notation and explicitly restricted to the stated scope.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/MeasurableSpace"
    ],
    "specializationNote": "Forget μ and retain exactly the same X and Σ.",
    "basisInstantiation": "Instantiate MeasurableSpace at (X,Σ); its sigma-algebra closure requirements remain obligations. Add μ with the empty-set and disjoint-countable-additivity rules listed here.",
    "leanFormulation": "abbrev MeasureSpace (A : Type u) := MeasureTheory.MeasureSpace A",
    "formulationSource": "urn:csabs:source/local-lean-Probability",
    "formulationLocator": "Catalog.MeasureSpace",
    "formulationScope": "model",
    "leanModelMapping": "Mathlib MeasureSpace bundles sigma-algebra and nonnegative extended-real countably additive measure.",
    "leanModelLimitations": "Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.",
    "mathematicalFormulation": "A measure space is (Ω,Σ,μ), where μ:Σ→[0,+∞], μ(∅)=0, and μ(⋃_n A_n)=Σ_n μ(A_n) for pairwise disjoint measurable A_n. Lean represents μ on all sets with measure-theoretic extension conventions."
  },
  {
    "id": "urn:csabs:operation/MeasureSpace-measure",
    "type": "Operation",
    "name": "measure",
    "signature": "Σ → [0,∞]; E ↦ μ(E)",
    "description": "Evaluate the measure only on measurable sets.",
    "concept": "urn:csabs:concept/MeasureSpace",
    "precondition": "Inputs belong to the stated domains.",
    "postcondition": "Evaluate the measure only on measurable sets.",
    "totality": "total on the stated domain"
  },
  {
    "id": "urn:csabs:axiom/MeasureSpace-empty",
    "type": "Axiom",
    "name": "empty",
    "statement": "The empty set has zero measure.",
    "formalStatement": "μ(∅)=0",
    "appliesTo": [
      "urn:csabs:concept/MeasureSpace"
    ],
    "assumptions": [
      "(X,Σ,μ); μ:Σ→[0,∞]",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial definition; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/axler-mira"
    ],
    "sourceLocator": "§2C, Definition 2.54",
    "sourceNote": "Defining constraint or equation adapted to the declared carriers and catalog notation.",
    "provenanceKind": "adapted",
    "ruleRole": "structure-law"
  },
  {
    "id": "urn:csabs:axiom/MeasureSpace-sigma-additivity",
    "type": "Axiom",
    "name": "sigma-additivity",
    "statement": "Disjoint measurable sets have additive measure over countable unions.",
    "formalStatement": "Eₙ∈Σ and Eᵢ∩Eⱼ=∅ for i≠j ⇒ μ(⋃ₙEₙ)=∑ₙμ(Eₙ)",
    "appliesTo": [
      "urn:csabs:concept/MeasureSpace"
    ],
    "assumptions": [
      "(X,Σ,μ); μ:Σ→[0,∞]",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial definition; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/axler-mira"
    ],
    "sourceLocator": "§2C, Definition 2.54",
    "sourceNote": "Defining constraint or equation adapted to the declared carriers and catalog notation.",
    "provenanceKind": "adapted",
    "ruleRole": "structure-law"
  },
  {
    "id": "urn:csabs:theorem/MeasureSpace-finite-additivity",
    "type": "Theorem",
    "name": "finite-additivity",
    "statement": "Two disjoint measurable sets have additive measure.",
    "formalStatement": "A,B∈Σ and A∩B=∅ ⇒ μ(A∪B)=μ(A)+μ(B)",
    "appliesTo": [
      "urn:csabs:concept/MeasureSpace"
    ],
    "assumptions": [
      "(X,Σ,μ); μ:Σ→[0,∞]",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial derivation; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/axler-mira"
    ],
    "sourceLocator": "§2C, result 2.57",
    "sourceNote": "Derived from the linked local premises; proof sketch gives the adaptation.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/MeasureSpace-empty",
      "urn:csabs:axiom/MeasureSpace-sigma-additivity"
    ],
    "proofSketch": "Apply countable additivity to the family A,B,∅,∅,… and use μ(∅)=0."
  },
  {
    "id": "urn:csabs:theorem/MeasureSpace-monotonicity",
    "type": "Theorem",
    "name": "monotonicity",
    "statement": "Measure is monotone on measurable sets.",
    "formalStatement": "A,B∈Σ and A⊆B ⇒ μ(A)≤μ(B)",
    "appliesTo": [
      "urn:csabs:concept/MeasureSpace"
    ],
    "assumptions": [
      "(X,Σ,μ); μ:Σ→[0,∞]",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial derivation; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/axler-mira"
    ],
    "sourceLocator": "§2C, result 2.57",
    "sourceNote": "Derived from the linked local premises; proof sketch gives the adaptation.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:theorem/MeasureSpace-finite-additivity",
      "urn:csabs:axiom/MeasurableSpace-complement",
      "urn:csabs:theorem/MeasurableSpace-countable-intersection",
      "urn:csabs:operation/MeasureSpace-measure"
    ],
    "proofSketch": "B=A⊔(B∖A). The difference is measurable by complement and intersection closure; finite additivity and μ(B∖A)≥0 give the inequality even for infinite values."
  }
]
```
<!-- graph-record:end -->
