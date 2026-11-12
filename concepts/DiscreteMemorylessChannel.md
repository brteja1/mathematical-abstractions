# Discrete memoryless channel (stationary finite profile)

Repeated uses of one finite stochastic kernel with conditional product law.

**Notation:** Wⁿ(yⁿ|xⁿ)=∏i=1ⁿ W(yi|xi)

**Stable ID:** `urn:csabs:concept/DiscreteMemorylessChannel`

**Categories:** Information theory

**Kind:** semantic-model

**Prerequisites:** [Finite stochastic channel](StochasticChannel.md)

**Specializes:** [Finite stochastic channel](StochasticChannel.md)

## Backlinks

- [Channel capacity (finite DMC, vanishing error)](ChannelCapacity.md) — `requiresConcept`

## Mathematical formulation

For a stationary channel W and block length n, Wⁿ(y|x)=∏\_{i∈Fin(n)}W(y\_i|x\_i). This describes conditional output independence; it imposes no independence on input coordinates. For n=0 the empty product is 1.

**Lean formulation** (in its source module context):

```lean
abbrev DiscreteMemorylessChannel := @Information.blockKernel
```

**Source:** [`Catalog.DiscreteMemorylessChannel`](../lean/Catalog/InformationTheory.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Stationary n-fold product of a normalized finite kernel; blockLaw constructs the resulting law with proved normalization. n=0 uses the empty product; operational codes use n+1.

**Limits:** No feedback or input-cost constraints. Shannon coding targets remain unproved.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Each W(·|x) is normalized and nonnegative; Wⁿ(yⁿ|xⁿ)=∏i W(yi|xi).

**basisKind:** extensional-structural-definition

**basisScope:** Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. Stationary kernel; no feedback, channel state, input cost or intersymbol memory. n=0 has the empty product 1; codes use n≥1.

**specializationNote:** Retain the same one-use kernel A→Dist(B) and impose its stationary product extension; product behavior is an explicit defining rule.

**verificationObligation:** Map alphabets, exact arithmetic, equality, logarithm base, channel model and error criterion before use.; Retrieve explicit premises; category and specialization links do not inherit claims.

**reviewStatus:** Editorial mathematical review; Lean models are explicitly scoped and theorem sketches are not compiled proofs.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-DiscreteMemorylessChannel-block-kernel"></a>

### block-kernel

`urn:csabs:operation/DiscreteMemorylessChannel-block-kernel`

**signature:** block : Channel(A,B)×ℕ → Channel(Aⁿ,Bⁿ)

**description:** Return the n-fold conditional product kernel.

**precondition:** Inputs satisfy the concept profile.

**totality:** Total on the stated domain.

**postcondition:** Return the n-fold conditional product kernel.

**source:** [Yury Polyanskiy, MIT 6.441 (2016), Chapter 14: Channel coding](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/8d9b42a8d43e28ca4a75e09fb4a89371_MIT6_441S16_chapter_14.pdf); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** Channel coding setup and memoryless product channels

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-DiscreteMemorylessChannel-product-law"></a>

### product-law

`urn:csabs:axiom/DiscreteMemorylessChannel-product-law`

**statement:** Each W(·|x) is normalized and nonnegative; Wⁿ(yⁿ|xⁿ)=∏i W(yi|xi).

**formalStatement:** Each W(·|x) is normalized and nonnegative; Wⁿ(yⁿ|xⁿ)=∏i W(yi|xi).

**assumptions:** Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. Stationary kernel; no feedback, channel state, input cost or intersymbol memory. n=0 has the empty product 1; codes use n≥1.

**ruleRole:** defining-rule

**reviewStatus:** Sourced structural definition, not an independent foundational axiom.

**source:** [Yury Polyanskiy, MIT 6.441 (2016), Chapter 14: Channel coding](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/8d9b42a8d43e28ca4a75e09fb4a89371_MIT6_441S16_chapter_14.pdf); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** Channel coding setup and memoryless product channels

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-DiscreteMemorylessChannel-product-normalized"></a>

### Product channel normalization

`urn:csabs:law/DiscreteMemorylessChannel-product-normalized`

**statement:** For every xⁿ, Σyⁿ Wⁿ(yⁿ|xⁿ)=1.

**formalStatement:** For every xⁿ, Σyⁿ Wⁿ(yⁿ|xⁿ)=1.

**assumptions:** Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. Stationary kernel; no feedback, channel state, input cost or intersymbol memory. n=0 has the empty product 1; codes use n≥1.

**dependsOn:** [product-law](DiscreteMemorylessChannel.md#node-urn-csabs-axiom-DiscreteMemorylessChannel-product-law)

**proofSketch:** Factor the finite sum as a product of row sums, each equal to one; the empty product handles n=0.

**reviewStatus:** Editorial statement-to-Lean correspondence review; a full-claim witness is registered separately in lean/bindings.json. Consult a fresh verification report for compiler and axiom-audit evidence.

**source:** [Yury Polyanskiy, MIT 6.441 (2016), Chapter 14: Channel coding](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/8d9b42a8d43e28ca4a75e09fb4a89371_MIT6_441S16_chapter_14.pdf); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** Channel coding setup and memoryless product channels

**sourceNote:** Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ (A B : Type) [Fintype B] (w : Catalog.Information.Channel A B) (n : ℕ) (x : Fin n → A), (∑ y, Catalog.Information.blockKernel w n x y) = 1
```

**Source:** [`Catalog.Information.Verified.productNormalized`](../lean/Catalog/InformationTheoryStatements.lean); consulted 2026-11-12.

**Scope:** registered-witness-type

**Interpretation:** Finite exact profile. For every xⁿ, Σyⁿ Wⁿ(yⁿ|xⁿ)=1. The compiled Targets proposition supplies explicit carriers and hypotheses; the independently expanded expected type is retained here. Nat minima are used only under nontrivial-code assumptions; source and channel blocks use positive lengths.

**Limits:** Witness proves the entire expanded expected type; correspondence to the informal statement is a reviewed mapping. This does not prove other catalog targets or an implementation refinement.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/DiscreteMemorylessChannel-product-law": "Explicit premise: Each W(·|x) is normalized and nonnegative; Wⁿ(yⁿ|xⁿ)=∏i W(yi|xi). Implemented by the normalized finite-law, exact finite-field, prefix-word or Hamming definitions and proved helper lemmas in InformationTheoryProofs/Statements; not introduced as a global axiom."
}
```

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [Yury Polyanskiy, MIT 6.441 (2016), Chapter 14: Channel coding](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/8d9b42a8d43e28ca4a75e09fb4a89371_MIT6_441S16_chapter_14.pdf); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** Channel coding setup and memoryless product channels

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/DiscreteMemorylessChannel",
    "type": "Concept",
    "shortForm": "DiscreteMemorylessChannel",
    "fullName": "Discrete memoryless channel (stationary finite profile)",
    "category": [
      "urn:csabs:category/information-theory"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "definition": "Repeated uses of one finite stochastic kernel with conditional product law.",
    "notation": "Wⁿ(yⁿ|xⁿ)=∏i=1ⁿ W(yi|xi)",
    "requiresConcept": [
      "urn:csabs:concept/StochasticChannel"
    ],
    "relatedConcept": [],
    "hasOperation": [
      "urn:csabs:operation/DiscreteMemorylessChannel-block-kernel"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/DiscreteMemorylessChannel-product-law"
    ],
    "hasLaw": [
      "urn:csabs:law/DiscreteMemorylessChannel-product-normalized"
    ],
    "hasTheorem": [],
    "axiomBasis": "Each W(·|x) is normalized and nonnegative; Wⁿ(yⁿ|xⁿ)=∏i W(yi|xi).",
    "basisKind": "extensional-structural-definition",
    "basisScope": "Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. Stationary kernel; no feedback, channel state, input cost or intersymbol memory. n=0 has the empty product 1; codes use n≥1.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial mathematical review; Lean models are explicitly scoped and theorem sketches are not compiled proofs.",
    "verificationObligation": [
      "Map alphabets, exact arithmetic, equality, logarithm base, channel model and error criterion before use.",
      "Retrieve explicit premises; category and specialization links do not inherit claims."
    ],
    "source": [
      "urn:csabs:source/mit-information-14"
    ],
    "sourceLocator": "Channel coding setup and memoryless product channels",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/StochasticChannel"
    ],
    "specializationNote": "Retain the same one-use kernel A→Dist(B) and impose its stationary product extension; product behavior is an explicit defining rule.",
    "leanFormulation": "abbrev DiscreteMemorylessChannel := @Information.blockKernel",
    "formulationSource": "urn:csabs:source/local-lean-InformationTheory",
    "formulationLocator": "Catalog.DiscreteMemorylessChannel",
    "formulationScope": "model",
    "leanModelMapping": "Stationary n-fold product of a normalized finite kernel; blockLaw constructs the resulting law with proved normalization. n=0 uses the empty product; operational codes use n+1.",
    "leanModelLimitations": "No feedback or input-cost constraints. Shannon coding targets remain unproved.",
    "mathematicalFormulation": "For a stationary channel W and block length n, Wⁿ(y|x)=∏_{i∈Fin(n)}W(y_i|x_i). This describes conditional output independence; it imposes no independence on input coordinates. For n=0 the empty product is 1."
  },
  {
    "id": "urn:csabs:operation/DiscreteMemorylessChannel-block-kernel",
    "type": "Operation",
    "name": "block-kernel",
    "signature": "block : Channel(A,B)×ℕ → Channel(Aⁿ,Bⁿ)",
    "description": "Return the n-fold conditional product kernel.",
    "concept": "urn:csabs:concept/DiscreteMemorylessChannel",
    "precondition": "Inputs satisfy the concept profile.",
    "totality": "Total on the stated domain.",
    "postcondition": "Return the n-fold conditional product kernel.",
    "source": [
      "urn:csabs:source/mit-information-14"
    ],
    "sourceLocator": "Channel coding setup and memoryless product channels",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/DiscreteMemorylessChannel-product-law",
    "type": "Axiom",
    "name": "product-law",
    "statement": "Each W(·|x) is normalized and nonnegative; Wⁿ(yⁿ|xⁿ)=∏i W(yi|xi).",
    "formalStatement": "Each W(·|x) is normalized and nonnegative; Wⁿ(yⁿ|xⁿ)=∏i W(yi|xi).",
    "assumptions": [
      "Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. Stationary kernel; no feedback, channel state, input cost or intersymbol memory. n=0 has the empty product 1; codes use n≥1."
    ],
    "appliesTo": [
      "urn:csabs:concept/DiscreteMemorylessChannel"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Sourced structural definition, not an independent foundational axiom.",
    "source": [
      "urn:csabs:source/mit-information-14"
    ],
    "sourceLocator": "Channel coding setup and memoryless product channels",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/DiscreteMemorylessChannel-product-normalized",
    "type": "Law",
    "name": "Product channel normalization",
    "statement": "For every xⁿ, Σyⁿ Wⁿ(yⁿ|xⁿ)=1.",
    "formalStatement": "For every xⁿ, Σyⁿ Wⁿ(yⁿ|xⁿ)=1.",
    "assumptions": [
      "Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. Stationary kernel; no feedback, channel state, input cost or intersymbol memory. n=0 has the empty product 1; codes use n≥1."
    ],
    "appliesTo": [
      "urn:csabs:concept/DiscreteMemorylessChannel"
    ],
    "dependsOn": [
      "urn:csabs:axiom/DiscreteMemorylessChannel-product-law"
    ],
    "proofSketch": "Factor the finite sum as a product of row sums, each equal to one; the empty product handles n=0.",
    "reviewStatus": "Editorial statement-to-Lean correspondence review; a full-claim witness is registered separately in lean/bindings.json. Consult a fresh verification report for compiler and axiom-audit evidence.",
    "source": [
      "urn:csabs:source/mit-information-14"
    ],
    "sourceLocator": "Channel coding setup and memoryless product channels",
    "sourceNote": "Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ (A B : Type) [Fintype B] (w : Catalog.Information.Channel A B) (n : ℕ) (x : Fin n → A), (∑ y, Catalog.Information.blockKernel w n x y) = 1",
    "formulationSource": "urn:csabs:source/local-lean-InformationTheoryStatements",
    "formulationLocator": "Catalog.Information.Verified.productNormalized",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Finite exact profile. For every xⁿ, Σyⁿ Wⁿ(yⁿ|xⁿ)=1. The compiled Targets proposition supplies explicit carriers and hypotheses; the independently expanded expected type is retained here. Nat minima are used only under nontrivial-code assumptions; source and channel blocks use positive lengths.",
    "leanModelLimitations": "Witness proves the entire expanded expected type; correspondence to the informal statement is a reviewed mapping. This does not prove other catalog targets or an implementation refinement.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/DiscreteMemorylessChannel-product-law\": \"Explicit premise: Each W(·|x) is normalized and nonnegative; Wⁿ(yⁿ|xⁿ)=∏i W(yi|xi). Implemented by the normalized finite-law, exact finite-field, prefix-word or Hamming definitions and proved helper lemmas in InformationTheoryProofs/Statements; not introduced as a global axiom.\"}"
  }
]
```
<!-- graph-record:end -->
