# Finite single-letter distortion measure

Nonnegative reconstruction cost, without metric axioms.

**Notation:** d:A×Â→ℝ≥0; dₙ(xⁿ,zⁿ)=(1/n)Σi d(xi,zi)

**Stable ID:** `urn:csabs:concept/DistortionMeasure`

**Categories:** Information theory → Coding theory → Source coding

**Kind:** Function

**Prerequisites:** [Finitely supported probability distribution](FiniteDistribution.md)

## Backlinks

- [Rate–distortion function (finite iid source, average cost)](RateDistortion.md) — `requiresConcept`

## Mathematical formulation

A single-letter distortion is d:A×B→ℝ with ∀a,b,d(a,b)≥0. No symmetry or triangle inequality is imposed. For positive n, block distortion is d\_n(x,y)=(1/n)Σ\_{i∈Fin(n)}d(x\_i,y\_i).

**Lean formulation** (in its source module context):

```lean
abbrev DistortionMeasure := Information.Cost
```

**Source:** [`Catalog.DistortionMeasure`](../lean/Catalog/InformationTheory.lean); consulted 2026-11-12.

**Scope:** partial

**Interpretation:** Exact real cost A→B→Real with nonnegativity, instantiated on finite nonempty alphabets.

**Limits:** Normalized block averaging and expectation operation omitted. These are model bindings, not proofs of the catalog theorems.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** d(a,z)≥0 and finite for all (a,z); for n≥1, dₙ(xⁿ,zⁿ)=(1/n)Σi d(xi,zi).

**basisKind:** extensional-structural-definition

**basisScope:** Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. Finite nonnegative costs, not +∞; A and Â can differ. No symmetry, separation or triangle inequality is assumed; n≥1 for normalized block distortion.

**verificationObligation:** Map alphabets, exact arithmetic, equality, logarithm base, channel model and error criterion before use.; Retrieve explicit premises; category and specialization links do not inherit claims.

**reviewStatus:** Editorial mathematical review; Lean models are explicitly scoped and theorem sketches are not compiled proofs.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-DistortionMeasure-block-distortion"></a>

### block-distortion

`urn:csabs:operation/DistortionMeasure-block-distortion`

**signature:** dblock : (A×Â→ℝ≥0)×Aⁿ×Âⁿ → ℝ≥0

**description:** Average the single-letter costs over n coordinates.

**precondition:** n≥1; finite nonnegative single-letter costs.

**totality:** Total on the stated domain.

**postcondition:** Average the single-letter costs over n coordinates.

**source:** [Yury Polyanskiy, MIT 6.441 (2016), Chapter 23: Rate-distortion theory](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/880c39878ba7dc35a5fbb35758d42a69_MIT6_441S16_chapter_23.pdf); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** Definition 23.1, separable distortion and average distortion

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-DistortionMeasure-separable-cost"></a>

### separable-cost

`urn:csabs:axiom/DistortionMeasure-separable-cost`

**statement:** d(a,z)≥0 and finite for all (a,z); for n≥1, dₙ(xⁿ,zⁿ)=(1/n)Σi d(xi,zi).

**formalStatement:** d(a,z)≥0 and finite for all (a,z); for n≥1, dₙ(xⁿ,zⁿ)=(1/n)Σi d(xi,zi).

**assumptions:** Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. Finite nonnegative costs, not +∞; A and Â can differ. No symmetry, separation or triangle inequality is assumed; n≥1 for normalized block distortion.

**ruleRole:** defining-rule

**reviewStatus:** Sourced structural definition, not an independent foundational axiom.

**source:** [Yury Polyanskiy, MIT 6.441 (2016), Chapter 23: Rate-distortion theory](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/880c39878ba7dc35a5fbb35758d42a69_MIT6_441S16_chapter_23.pdf); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** Definition 23.1, separable distortion and average distortion

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-DistortionMeasure-expected-block"></a>

### Expected separable distortion

`urn:csabs:law/DistortionMeasure-expected-block`

**statement:** E[dₙ(Xⁿ,Zⁿ)]=(1/n)Σi E[d(Xi,Zi)], without any independence requirement.

**formalStatement:** E[dₙ(Xⁿ,Zⁿ)]=(1/n)Σi E[d(Xi,Zi)], without any independence requirement.

**assumptions:** Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. Finite nonnegative costs, not +∞; A and Â can differ. No symmetry, separation or triangle inequality is assumed; n≥1 for normalized block distortion.

**dependsOn:** [separable-cost](DistortionMeasure.md#node-urn-csabs-axiom-DistortionMeasure-separable-cost)

**proofSketch:** Expand the finite expectation and interchange the finite sums.

**reviewStatus:** Editorial statement-to-Lean correspondence review; a full-claim witness is registered separately in lean/bindings.json. Consult a fresh verification report for compiler and axiom-audit evidence.

**source:** [Yury Polyanskiy, MIT 6.441 (2016), Chapter 23: Rate-distortion theory](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/880c39878ba7dc35a5fbb35758d42a69_MIT6_441S16_chapter_23.pdf); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** Definition 23.1, separable distortion and average distortion

**sourceNote:** Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ (A B : Type) [Fintype A] [Fintype B] (n : ℕ), 0 < n → ∀ (p : Catalog.Information.Law ((Fin n → A) × (Fin n → B))) (d : Catalog.Information.Cost A B), Catalog.Information.expectation p (fun xz => Catalog.Information.averageCost d xz.1 xz.2) = (∑ i, Catalog.Information.expectation p (fun xz => d.value (xz.1 i) (xz.2 i))) / n
```

**Source:** [`Catalog.Information.Verified.expectedBlock`](../lean/Catalog/InformationTheoryStatements.lean); consulted 2026-11-12.

**Scope:** registered-witness-type

**Interpretation:** Finite exact profile. E[dₙ(Xⁿ,Zⁿ)]=(1/n)Σi E[d(Xi,Zi)], without any independence requirement. The compiled Targets proposition supplies explicit carriers and hypotheses; the independently expanded expected type is retained here. Nat minima are used only under nontrivial-code assumptions; source and channel blocks use positive lengths.

**Limits:** Witness proves the entire expanded expected type; correspondence to the informal statement is a reviewed mapping. This does not prove other catalog targets or an implementation refinement.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/DistortionMeasure-separable-cost": "Explicit premise: d(a,z)≥0 and finite for all (a,z); for n≥1, dₙ(xⁿ,zⁿ)=(1/n)Σi d(xi,zi). Implemented by the normalized finite-law, exact finite-field, prefix-word or Hamming definitions and proved helper lemmas in InformationTheoryProofs/Statements; not introduced as a global axiom."
}
```

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [Yury Polyanskiy, MIT 6.441 (2016), Chapter 23: Rate-distortion theory](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/880c39878ba7dc35a5fbb35758d42a69_MIT6_441S16_chapter_23.pdf); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** Definition 23.1, separable distortion and average distortion

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/DistortionMeasure",
    "type": "Concept",
    "shortForm": "DistortionMeasure",
    "fullName": "Finite single-letter distortion measure",
    "category": [
      "urn:csabs:category/source-coding"
    ],
    "kind": "urn:csabs:kind/function",
    "definition": "Nonnegative reconstruction cost, without metric axioms.",
    "notation": "d:A×Â→ℝ≥0; dₙ(xⁿ,zⁿ)=(1/n)Σi d(xi,zi)",
    "requiresConcept": [
      "urn:csabs:concept/FiniteDistribution"
    ],
    "relatedConcept": [],
    "hasOperation": [
      "urn:csabs:operation/DistortionMeasure-block-distortion"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/DistortionMeasure-separable-cost"
    ],
    "hasLaw": [
      "urn:csabs:law/DistortionMeasure-expected-block"
    ],
    "hasTheorem": [],
    "axiomBasis": "d(a,z)≥0 and finite for all (a,z); for n≥1, dₙ(xⁿ,zⁿ)=(1/n)Σi d(xi,zi).",
    "basisKind": "extensional-structural-definition",
    "basisScope": "Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. Finite nonnegative costs, not +∞; A and Â can differ. No symmetry, separation or triangle inequality is assumed; n≥1 for normalized block distortion.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial mathematical review; Lean models are explicitly scoped and theorem sketches are not compiled proofs.",
    "verificationObligation": [
      "Map alphabets, exact arithmetic, equality, logarithm base, channel model and error criterion before use.",
      "Retrieve explicit premises; category and specialization links do not inherit claims."
    ],
    "source": [
      "urn:csabs:source/mit-information-23"
    ],
    "sourceLocator": "Definition 23.1, separable distortion and average distortion",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted",
    "leanFormulation": "abbrev DistortionMeasure := Information.Cost",
    "formulationSource": "urn:csabs:source/local-lean-InformationTheory",
    "formulationLocator": "Catalog.DistortionMeasure",
    "formulationScope": "partial",
    "leanModelMapping": "Exact real cost A→B→Real with nonnegativity, instantiated on finite nonempty alphabets.",
    "leanModelLimitations": "Normalized block averaging and expectation operation omitted. These are model bindings, not proofs of the catalog theorems.",
    "mathematicalFormulation": "A single-letter distortion is d:A×B→ℝ with ∀a,b,d(a,b)≥0. No symmetry or triangle inequality is imposed. For positive n, block distortion is d_n(x,y)=(1/n)Σ_{i∈Fin(n)}d(x_i,y_i)."
  },
  {
    "id": "urn:csabs:operation/DistortionMeasure-block-distortion",
    "type": "Operation",
    "name": "block-distortion",
    "signature": "dblock : (A×Â→ℝ≥0)×Aⁿ×Âⁿ → ℝ≥0",
    "description": "Average the single-letter costs over n coordinates.",
    "concept": "urn:csabs:concept/DistortionMeasure",
    "precondition": "n≥1; finite nonnegative single-letter costs.",
    "totality": "Total on the stated domain.",
    "postcondition": "Average the single-letter costs over n coordinates.",
    "source": [
      "urn:csabs:source/mit-information-23"
    ],
    "sourceLocator": "Definition 23.1, separable distortion and average distortion",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/DistortionMeasure-separable-cost",
    "type": "Axiom",
    "name": "separable-cost",
    "statement": "d(a,z)≥0 and finite for all (a,z); for n≥1, dₙ(xⁿ,zⁿ)=(1/n)Σi d(xi,zi).",
    "formalStatement": "d(a,z)≥0 and finite for all (a,z); for n≥1, dₙ(xⁿ,zⁿ)=(1/n)Σi d(xi,zi).",
    "assumptions": [
      "Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. Finite nonnegative costs, not +∞; A and Â can differ. No symmetry, separation or triangle inequality is assumed; n≥1 for normalized block distortion."
    ],
    "appliesTo": [
      "urn:csabs:concept/DistortionMeasure"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Sourced structural definition, not an independent foundational axiom.",
    "source": [
      "urn:csabs:source/mit-information-23"
    ],
    "sourceLocator": "Definition 23.1, separable distortion and average distortion",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/DistortionMeasure-expected-block",
    "type": "Law",
    "name": "Expected separable distortion",
    "statement": "E[dₙ(Xⁿ,Zⁿ)]=(1/n)Σi E[d(Xi,Zi)], without any independence requirement.",
    "formalStatement": "E[dₙ(Xⁿ,Zⁿ)]=(1/n)Σi E[d(Xi,Zi)], without any independence requirement.",
    "assumptions": [
      "Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. Finite nonnegative costs, not +∞; A and Â can differ. No symmetry, separation or triangle inequality is assumed; n≥1 for normalized block distortion."
    ],
    "appliesTo": [
      "urn:csabs:concept/DistortionMeasure"
    ],
    "dependsOn": [
      "urn:csabs:axiom/DistortionMeasure-separable-cost"
    ],
    "proofSketch": "Expand the finite expectation and interchange the finite sums.",
    "reviewStatus": "Editorial statement-to-Lean correspondence review; a full-claim witness is registered separately in lean/bindings.json. Consult a fresh verification report for compiler and axiom-audit evidence.",
    "source": [
      "urn:csabs:source/mit-information-23"
    ],
    "sourceLocator": "Definition 23.1, separable distortion and average distortion",
    "sourceNote": "Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ (A B : Type) [Fintype A] [Fintype B] (n : ℕ), 0 < n → ∀ (p : Catalog.Information.Law ((Fin n → A) × (Fin n → B))) (d : Catalog.Information.Cost A B), Catalog.Information.expectation p (fun xz => Catalog.Information.averageCost d xz.1 xz.2) = (∑ i, Catalog.Information.expectation p (fun xz => d.value (xz.1 i) (xz.2 i))) / n",
    "formulationSource": "urn:csabs:source/local-lean-InformationTheoryStatements",
    "formulationLocator": "Catalog.Information.Verified.expectedBlock",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Finite exact profile. E[dₙ(Xⁿ,Zⁿ)]=(1/n)Σi E[d(Xi,Zi)], without any independence requirement. The compiled Targets proposition supplies explicit carriers and hypotheses; the independently expanded expected type is retained here. Nat minima are used only under nontrivial-code assumptions; source and channel blocks use positive lengths.",
    "leanModelLimitations": "Witness proves the entire expanded expected type; correspondence to the informal statement is a reviewed mapping. This does not prove other catalog targets or an implementation refinement.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/DistortionMeasure-separable-cost\": \"Explicit premise: d(a,z)≥0 and finite for all (a,z); for n≥1, dₙ(xⁿ,zⁿ)=(1/n)Σi d(xi,zi). Implemented by the normalized finite-law, exact finite-field, prefix-word or Hamming definitions and proved helper lemmas in InformationTheoryProofs/Statements; not introduced as a global axiom.\"}"
  }
]
```
<!-- graph-record:end -->
