# Finite stochastic channel

A row-normalized probability kernel from input symbols to output symbols.

**Notation:** W:B←A; W(y|x)≥0; Σy W(y|x)=1

**Stable ID:** `urn:csabs:concept/StochasticChannel`

**Categories:** Information theory

**Kind:** semantic-model

**Prerequisites:** [Finitely supported probability distribution](FiniteDistribution.md), [Finite rectangular matrix over a field](Matrix.md)

## Backlinks

- [Discrete memoryless channel (stationary finite profile)](DiscreteMemorylessChannel.md) — `requiresConcept`
- [Discrete memoryless channel (stationary finite profile)](DiscreteMemorylessChannel.md) — `specializationOf`
- [Rate–distortion function (finite iid source, average cost)](RateDistortion.md) — `requiresConcept`

## Mathematical formulation

A finite-output channel is W:A→Law(B), i.e. W(b|a)≥0 and ∀a,Σ\_b W(b|a)=1. For input p, output q(b)=Σ\_a p(a)W(b|a). The kernel alone does not select an input distribution.

**Lean formulation** (in its source module context):

```lean
abbrev StochasticChannel := Information.Channel
```

**Source:** [`Catalog.StochasticChannel`](../lean/Catalog/InformationTheory.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** A→Law B with exact nonnegative normalized rows; outputMass/output compute the finite output distribution, whose nonnegativity and normalization are proved.

**Limits:** No random sampler, floating-point implementation or channel-memory model.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** W(y|x)≥0 and Σy W(y|x)=1 for every x; output(p,W)(y)=Σx p(x)W(y|x).

**basisKind:** extensional-structural-definition

**basisScope:** Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. Equality is entrywise kernel equality. One use is specified; memory assumptions require a separate profile.

**verificationObligation:** Map alphabets, exact arithmetic, equality, logarithm base, channel model and error criterion before use.; Retrieve explicit premises; category and specialization links do not inherit claims.

**reviewStatus:** Editorial mathematical review; Lean models are explicitly scoped and theorem sketches are not compiled proofs.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-StochasticChannel-output-law"></a>

### output-law

`urn:csabs:operation/StochasticChannel-output-law`

**signature:** output : Channel(A,B)×Dist(A) → Dist(B)

**description:** q(y)=Σx p(x)W(y|x).

**precondition:** Inputs satisfy the concept profile.

**totality:** Total on the stated domain.

**postcondition:** q(y)=Σx p(x)W(y|x).

**source:** [Georg Böcherer, Lecture Notes on Channel Coding (2016)](https://arxiv.org/html/1607.00974v1); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** Chapter 1 §1, channel model (1.1)

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-StochasticChannel-kernel"></a>

### kernel

`urn:csabs:axiom/StochasticChannel-kernel`

**statement:** W(y|x)≥0 and Σy W(y|x)=1 for every x; output(p,W)(y)=Σx p(x)W(y|x).

**formalStatement:** W(y|x)≥0 and Σy W(y|x)=1 for every x; output(p,W)(y)=Σx p(x)W(y|x).

**assumptions:** Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. Equality is entrywise kernel equality. One use is specified; memory assumptions require a separate profile.

**ruleRole:** defining-rule

**reviewStatus:** Sourced structural definition, not an independent foundational axiom.

**source:** [Georg Böcherer, Lecture Notes on Channel Coding (2016)](https://arxiv.org/html/1607.00974v1); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** Chapter 1 §1, channel model (1.1)

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-StochasticChannel-output-normalized"></a>

### Channel output normalization

`urn:csabs:law/StochasticChannel-output-normalized`

**statement:** Σy output(p,W)(y)=1 and output(p,W)(y)≥0.

**formalStatement:** Σy output(p,W)(y)=1 and output(p,W)(y)≥0.

**assumptions:** Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. Equality is entrywise kernel equality. One use is specified; memory assumptions require a separate profile.

**dependsOn:** [kernel](StochasticChannel.md#node-urn-csabs-axiom-StochasticChannel-kernel)

**proofSketch:** Swap the finite sums and use row normalization and Σx p(x)=1.

**reviewStatus:** Editorial statement-to-Lean correspondence review; a full-claim witness is registered separately in lean/bindings.json. Consult a fresh verification report for compiler and axiom-audit evidence.

**source:** [Georg Böcherer, Lecture Notes on Channel Coding (2016)](https://arxiv.org/html/1607.00974v1); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** Chapter 1 §1, channel model (1.1)

**sourceNote:** Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ (A B : Type) [Fintype A] [Fintype B] (p : Catalog.Information.Law A) (w : Catalog.Information.Channel A B), (∑ b, Catalog.Information.outputMass p w b) = 1 ∧ ∀ b, 0 ≤ Catalog.Information.outputMass p w b
```

**Source:** [`Catalog.Information.Verified.outputNormalized`](../lean/Catalog/InformationTheoryStatements.lean); consulted 2026-11-12.

**Scope:** registered-witness-type

**Interpretation:** Finite exact profile. Σy output(p,W)(y)=1 and output(p,W)(y)≥0. The compiled Targets proposition supplies explicit carriers and hypotheses; the independently expanded expected type is retained here. Nat minima are used only under nontrivial-code assumptions; source and channel blocks use positive lengths.

**Limits:** Witness proves the entire expanded expected type; correspondence to the informal statement is a reviewed mapping. This does not prove other catalog targets or an implementation refinement.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/StochasticChannel-kernel": "Explicit premise: W(y|x)≥0 and Σy W(y|x)=1 for every x; output(p,W)(y)=Σx p(x)W(y|x). Implemented by the normalized finite-law, exact finite-field, prefix-word or Hamming definitions and proved helper lemmas in InformationTheoryProofs/Statements; not introduced as a global axiom."
}
```

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [Georg Böcherer, Lecture Notes on Channel Coding (2016)](https://arxiv.org/html/1607.00974v1); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** Chapter 1 §1, channel model (1.1)

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/StochasticChannel",
    "type": "Concept",
    "shortForm": "StochasticChannel",
    "fullName": "Finite stochastic channel",
    "category": [
      "urn:csabs:category/information-theory"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "definition": "A row-normalized probability kernel from input symbols to output symbols.",
    "notation": "W:B←A; W(y|x)≥0; Σy W(y|x)=1",
    "requiresConcept": [
      "urn:csabs:concept/FiniteDistribution",
      "urn:csabs:concept/Matrix"
    ],
    "relatedConcept": [],
    "hasOperation": [
      "urn:csabs:operation/StochasticChannel-output-law"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/StochasticChannel-kernel"
    ],
    "hasLaw": [
      "urn:csabs:law/StochasticChannel-output-normalized"
    ],
    "hasTheorem": [],
    "axiomBasis": "W(y|x)≥0 and Σy W(y|x)=1 for every x; output(p,W)(y)=Σx p(x)W(y|x).",
    "basisKind": "extensional-structural-definition",
    "basisScope": "Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. Equality is entrywise kernel equality. One use is specified; memory assumptions require a separate profile.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial mathematical review; Lean models are explicitly scoped and theorem sketches are not compiled proofs.",
    "verificationObligation": [
      "Map alphabets, exact arithmetic, equality, logarithm base, channel model and error criterion before use.",
      "Retrieve explicit premises; category and specialization links do not inherit claims."
    ],
    "source": [
      "urn:csabs:source/boecherer-channel-coding"
    ],
    "sourceLocator": "Chapter 1 §1, channel model (1.1)",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted",
    "leanFormulation": "abbrev StochasticChannel := Information.Channel",
    "formulationSource": "urn:csabs:source/local-lean-InformationTheory",
    "formulationLocator": "Catalog.StochasticChannel",
    "formulationScope": "model",
    "leanModelMapping": "A→Law B with exact nonnegative normalized rows; outputMass/output compute the finite output distribution, whose nonnegativity and normalization are proved.",
    "leanModelLimitations": "No random sampler, floating-point implementation or channel-memory model.",
    "mathematicalFormulation": "A finite-output channel is W:A→Law(B), i.e. W(b|a)≥0 and ∀a,Σ_b W(b|a)=1. For input p, output q(b)=Σ_a p(a)W(b|a). The kernel alone does not select an input distribution."
  },
  {
    "id": "urn:csabs:operation/StochasticChannel-output-law",
    "type": "Operation",
    "name": "output-law",
    "signature": "output : Channel(A,B)×Dist(A) → Dist(B)",
    "description": "q(y)=Σx p(x)W(y|x).",
    "concept": "urn:csabs:concept/StochasticChannel",
    "precondition": "Inputs satisfy the concept profile.",
    "totality": "Total on the stated domain.",
    "postcondition": "q(y)=Σx p(x)W(y|x).",
    "source": [
      "urn:csabs:source/boecherer-channel-coding"
    ],
    "sourceLocator": "Chapter 1 §1, channel model (1.1)",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/StochasticChannel-kernel",
    "type": "Axiom",
    "name": "kernel",
    "statement": "W(y|x)≥0 and Σy W(y|x)=1 for every x; output(p,W)(y)=Σx p(x)W(y|x).",
    "formalStatement": "W(y|x)≥0 and Σy W(y|x)=1 for every x; output(p,W)(y)=Σx p(x)W(y|x).",
    "assumptions": [
      "Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. Equality is entrywise kernel equality. One use is specified; memory assumptions require a separate profile."
    ],
    "appliesTo": [
      "urn:csabs:concept/StochasticChannel"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Sourced structural definition, not an independent foundational axiom.",
    "source": [
      "urn:csabs:source/boecherer-channel-coding"
    ],
    "sourceLocator": "Chapter 1 §1, channel model (1.1)",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/StochasticChannel-output-normalized",
    "type": "Law",
    "name": "Channel output normalization",
    "statement": "Σy output(p,W)(y)=1 and output(p,W)(y)≥0.",
    "formalStatement": "Σy output(p,W)(y)=1 and output(p,W)(y)≥0.",
    "assumptions": [
      "Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. Equality is entrywise kernel equality. One use is specified; memory assumptions require a separate profile."
    ],
    "appliesTo": [
      "urn:csabs:concept/StochasticChannel"
    ],
    "dependsOn": [
      "urn:csabs:axiom/StochasticChannel-kernel"
    ],
    "proofSketch": "Swap the finite sums and use row normalization and Σx p(x)=1.",
    "reviewStatus": "Editorial statement-to-Lean correspondence review; a full-claim witness is registered separately in lean/bindings.json. Consult a fresh verification report for compiler and axiom-audit evidence.",
    "source": [
      "urn:csabs:source/boecherer-channel-coding"
    ],
    "sourceLocator": "Chapter 1 §1, channel model (1.1)",
    "sourceNote": "Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ (A B : Type) [Fintype A] [Fintype B] (p : Catalog.Information.Law A) (w : Catalog.Information.Channel A B), (∑ b, Catalog.Information.outputMass p w b) = 1 ∧ ∀ b, 0 ≤ Catalog.Information.outputMass p w b",
    "formulationSource": "urn:csabs:source/local-lean-InformationTheoryStatements",
    "formulationLocator": "Catalog.Information.Verified.outputNormalized",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Finite exact profile. Σy output(p,W)(y)=1 and output(p,W)(y)≥0. The compiled Targets proposition supplies explicit carriers and hypotheses; the independently expanded expected type is retained here. Nat minima are used only under nontrivial-code assumptions; source and channel blocks use positive lengths.",
    "leanModelLimitations": "Witness proves the entire expanded expected type; correspondence to the informal statement is a reviewed mapping. This does not prove other catalog targets or an implementation refinement.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/StochasticChannel-kernel\": \"Explicit premise: W(y|x)≥0 and Σy W(y|x)=1 for every x; output(p,W)(y)=Σx p(x)W(y|x). Implemented by the normalized finite-law, exact finite-field, prefix-word or Hamming definitions and proved helper lemmas in InformationTheoryProofs/Statements; not introduced as a global axiom.\"}"
  }
]
```
<!-- graph-record:end -->
