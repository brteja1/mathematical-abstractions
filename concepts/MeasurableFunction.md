# Measurable function

A total function between measurable spaces whose inverse images of measurable target sets are measurable in the source.

**Notation:** f:(X,Σ)→(Y,Τ); ∀B∈Τ:f⁻¹(B)∈Σ

**Stable ID:** `urn:csabs:concept/MeasurableFunction`

**Categories:** Measure theory

**Kind:** Function

**Prerequisites:** [Total function](Function.md), [Measurable space (sigma-algebra on a carrier)](MeasurableSpace.md)

**Specializes:** [Total function](Function.md)

## Backlinks

- [Random variable (measurable random element)](RandomVariable.md) — `requiresConcept`
- [Random variable (measurable random element)](RandomVariable.md) — `specializationOf`

## Interface and scope

**axiomBasis:** Total function with specified measurable source and target spaces and preservation of measurability under inverse image.

**basisKind:** defined-structure

**basisScope:** Measurable functions and composition; not almost-everywhere equivalence classes.

**specializationNote:** Forget source and target sigma-algebras, retaining the same total function.

**verificationObligation:** Equality is pointwise on the entire source, not merely almost everywhere. An empty source is allowed.; Use the stated carriers and equality. Specialization does not automatically transfer operations or claims.

**reviewStatus:** editorial interface review; not machine-proved

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-MeasurableFunction-preimage"></a>

### preimage

`urn:csabs:operation/MeasurableFunction-preimage`

**signature:** Τ → Σ; B ↦ {x∈X:f(x)∈B}

**description:** Take the inverse image of a measurable target set.

**precondition:** Inputs belong to the stated domains.

**postcondition:** Take the inverse image of a measurable target set.

**totality:** total on the stated domain

<a id="node-urn-csabs-operation-MeasurableFunction-compose"></a>

### compose

`urn:csabs:operation/MeasurableFunction-compose`

**signature:** Meas(Y,Z) × Meas(X,Y) → Meas(X,Z)

**description:** Compose compatible measurable maps.

**precondition:** Inputs belong to the stated domains.

**postcondition:** Compose compatible measurable maps.

**totality:** total on the stated domain

## Axioms and defining rules

<a id="node-urn-csabs-axiom-MeasurableFunction-preimage-measurability"></a>

### preimage-measurability

`urn:csabs:axiom/MeasurableFunction-preimage-measurability`

**statement:** Inverse images of measurable sets are measurable.

**formalStatement:** B∈Τ ⇒ {x∈X:f(x)∈B}∈Σ

**assumptions:** f:(X,Σ)→(Y,Τ); ∀B∈Τ:f⁻¹(B)∈Σ; Use the concept’s declared semantic conventions.

**reviewStatus:** editorial definition; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Mathlib: measurable spaces and measurable functions](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/MeasurableSpace/Defs.html); accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** Measurable

**sourceNote:** Defining constraint or equation adapted to the declared carriers and catalog notation.

**provenanceKind:** adapted

**ruleRole:** defining-rule

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-MeasurableFunction-composition"></a>

### composition

`urn:csabs:theorem/MeasurableFunction-composition`

**statement:** Composition preserves measurability.

**formalStatement:** f:(X,Σ)→(Y,Τ), g:(Y,Τ)→(Z,Υ) measurable ⇒ g∘f measurable

**assumptions:** f:(X,Σ)→(Y,Τ); ∀B∈Τ:f⁻¹(B)∈Σ; Use the concept’s declared semantic conventions.

**reviewStatus:** editorial derivation; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Mathlib: measurable spaces and measurable functions](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/MeasurableSpace/Defs.html); accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** Measurable.comp

**sourceNote:** Derived from the linked local premises; proof sketch gives the adaptation.

**provenanceKind:** derived

**dependsOn:** [preimage-measurability](MeasurableFunction.md#node-urn-csabs-axiom-MeasurableFunction-preimage-measurability); [preimage](MeasurableFunction.md#node-urn-csabs-operation-MeasurableFunction-preimage); [compose](MeasurableFunction.md#node-urn-csabs-operation-MeasurableFunction-compose)

**proofSketch:** For C∈Υ, (g∘f)⁻¹(C)=f⁻¹(g⁻¹(C)); apply the measurable inverse-image condition twice.

## Concept provenance

- [Mathlib: measurable spaces and measurable functions](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/MeasurableSpace/Defs.html); accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** Measurable; Measurable.comp (inverse-image formulation)

**sourceNote:** Interface adapted to the catalog notation and explicitly restricted to the stated scope.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/MeasurableFunction",
    "type": "Concept",
    "shortForm": "MeasurableFunction",
    "fullName": "Measurable function",
    "category": [
      "urn:csabs:category/measure-theory"
    ],
    "kind": "urn:csabs:kind/function",
    "definition": "A total function between measurable spaces whose inverse images of measurable target sets are measurable in the source.",
    "notation": "f:(X,Σ)→(Y,Τ); ∀B∈Τ:f⁻¹(B)∈Σ",
    "hasOperation": [
      "urn:csabs:operation/MeasurableFunction-preimage",
      "urn:csabs:operation/MeasurableFunction-compose"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/MeasurableFunction-preimage-measurability"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/MeasurableFunction-composition"
    ],
    "axiomBasis": "Total function with specified measurable source and target spaces and preservation of measurability under inverse image.",
    "basisKind": "defined-structure",
    "basisScope": "Measurable functions and composition; not almost-everywhere equivalence classes.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "editorial interface review; not machine-proved",
    "requiresConcept": [
      "urn:csabs:concept/Function",
      "urn:csabs:concept/MeasurableSpace"
    ],
    "verificationObligation": [
      "Equality is pointwise on the entire source, not merely almost everywhere. An empty source is allowed.",
      "Use the stated carriers and equality. Specialization does not automatically transfer operations or claims."
    ],
    "source": [
      "urn:csabs:source/mathlib-measurable-functions"
    ],
    "sourceLocator": "Measurable; Measurable.comp (inverse-image formulation)",
    "sourceNote": "Interface adapted to the catalog notation and explicitly restricted to the stated scope.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/Function"
    ],
    "specializationNote": "Forget source and target sigma-algebras, retaining the same total function."
  },
  {
    "id": "urn:csabs:operation/MeasurableFunction-preimage",
    "type": "Operation",
    "name": "preimage",
    "signature": "Τ → Σ; B ↦ {x∈X:f(x)∈B}",
    "description": "Take the inverse image of a measurable target set.",
    "concept": "urn:csabs:concept/MeasurableFunction",
    "precondition": "Inputs belong to the stated domains.",
    "postcondition": "Take the inverse image of a measurable target set.",
    "totality": "total on the stated domain"
  },
  {
    "id": "urn:csabs:operation/MeasurableFunction-compose",
    "type": "Operation",
    "name": "compose",
    "signature": "Meas(Y,Z) × Meas(X,Y) → Meas(X,Z)",
    "description": "Compose compatible measurable maps.",
    "concept": "urn:csabs:concept/MeasurableFunction",
    "precondition": "Inputs belong to the stated domains.",
    "postcondition": "Compose compatible measurable maps.",
    "totality": "total on the stated domain"
  },
  {
    "id": "urn:csabs:axiom/MeasurableFunction-preimage-measurability",
    "type": "Axiom",
    "name": "preimage-measurability",
    "statement": "Inverse images of measurable sets are measurable.",
    "formalStatement": "B∈Τ ⇒ {x∈X:f(x)∈B}∈Σ",
    "appliesTo": [
      "urn:csabs:concept/MeasurableFunction"
    ],
    "assumptions": [
      "f:(X,Σ)→(Y,Τ); ∀B∈Τ:f⁻¹(B)∈Σ",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial definition; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/mathlib-measurable-functions"
    ],
    "sourceLocator": "Measurable",
    "sourceNote": "Defining constraint or equation adapted to the declared carriers and catalog notation.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:theorem/MeasurableFunction-composition",
    "type": "Theorem",
    "name": "composition",
    "statement": "Composition preserves measurability.",
    "formalStatement": "f:(X,Σ)→(Y,Τ), g:(Y,Τ)→(Z,Υ) measurable ⇒ g∘f measurable",
    "appliesTo": [
      "urn:csabs:concept/MeasurableFunction"
    ],
    "assumptions": [
      "f:(X,Σ)→(Y,Τ); ∀B∈Τ:f⁻¹(B)∈Σ",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial derivation; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/mathlib-measurable-functions"
    ],
    "sourceLocator": "Measurable.comp",
    "sourceNote": "Derived from the linked local premises; proof sketch gives the adaptation.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/MeasurableFunction-preimage-measurability",
      "urn:csabs:operation/MeasurableFunction-preimage",
      "urn:csabs:operation/MeasurableFunction-compose"
    ],
    "proofSketch": "For C∈Υ, (g∘f)⁻¹(C)=f⁻¹(g⁻¹(C)); apply the measurable inverse-image condition twice."
  }
]
```
<!-- graph-record:end -->
