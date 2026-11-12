# Hamming space (finite fixed-length words)

Finite word space equipped with the number of unequal coordinates.

**Notation:** (Σⁿ,dH); dH(x,y)=|{i:xi≠yi}|

**Stable ID:** `urn:csabs:concept/HammingSpace`

**Categories:** Information theory → Coding theory → Channel coding

**Kind:** Mathematical structure

**Prerequisites:** [Finite set collection](FiniteSet.md), [Finite sequence (List datatype)](Sequence.md)

## Backlinks

- [Finite block code (Hamming profile)](BlockCode.md) — `requiresConcept`

## Mathematical formulation

For words x,y∈A^n, d\_H(x,y)=|{i∈Fin(n) | x\_i≠y\_i}|. No field operations are needed; coordinate equality is decidable in the Lean evaluator, and n=0 is allowed.

**Lean formulation** (in its source module context):

```lean
abbrev HammingSpace := @Information.hamming
```

**Source:** [`Catalog.HammingSpace`](../lean/Catalog/InformationTheory.lean); consulted 2026-11-12.

**Scope:** partial

**Interpretation:** Fin n→A words and Nat count of unequal coordinates, with decidable symbol equality. Instantiate n≥1 and finite alphabet of size at least two.

**Limits:** Hamming balls and metric-law witnesses omitted. These are model bindings, not proofs of the catalog theorems.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** dH(x,y)=Σi 1{xi≠yi}; B(x,t)={y:dH(x,y)≤t}.

**basisKind:** extensional-structural-definition

**basisScope:** Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state.

**verificationObligation:** Map alphabets, exact arithmetic, equality, logarithm base, channel model and error criterion before use.; Retrieve explicit premises; category and specialization links do not inherit claims.

**reviewStatus:** Editorial mathematical review; Lean models are explicitly scoped and theorem sketches are not compiled proofs.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-HammingSpace-distance"></a>

### distance

`urn:csabs:operation/HammingSpace-distance`

**signature:** dH : Σⁿ×Σⁿ → ℕ

**description:** Count coordinates with unequal symbols.

**precondition:** Inputs satisfy the concept profile.

**totality:** Total on the stated domain.

**postcondition:** Count coordinates with unequal symbols.

**source:** [Georg Böcherer, Lecture Notes on Channel Coding (2016)](https://arxiv.org/html/1607.00974v1); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §7.1 Hamming geometry

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-HammingSpace-ball"></a>

### ball

`urn:csabs:operation/HammingSpace-ball`

**signature:** ball : Σⁿ×ℕ → FinSet(Σⁿ)

**description:** B(x,t)={y:dH(x,y)≤t}; a radius t≥n gives the entire space.

**precondition:** Inputs satisfy the concept profile.

**totality:** Total on the stated domain.

**postcondition:** B(x,t)={y:dH(x,y)≤t}; a radius t≥n gives the entire space.

**source:** [Georg Böcherer, Lecture Notes on Channel Coding (2016)](https://arxiv.org/html/1607.00974v1); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §7.1 Hamming geometry

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-HammingSpace-distance-equation"></a>

### distance-equation

`urn:csabs:axiom/HammingSpace-distance-equation`

**statement:** dH(x,y)=Σi 1{xi≠yi}; B(x,t)={y:dH(x,y)≤t}.

**formalStatement:** dH(x,y)=Σi 1{xi≠yi}; B(x,t)={y:dH(x,y)≤t}.

**assumptions:** Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state.

**ruleRole:** defining-rule

**reviewStatus:** Sourced structural definition, not an independent foundational axiom.

**source:** [Georg Böcherer, Lecture Notes on Channel Coding (2016)](https://arxiv.org/html/1607.00974v1); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §7.1 Hamming geometry

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-HammingSpace-metric"></a>

### Hamming metric laws

`urn:csabs:law/HammingSpace-metric`

**statement:** dH(x,y)≥0; dH(x,y)=0 iff x=y; dH(x,y)=dH(y,x); dH(x,z)≤dH(x,y)+dH(y,z).

**formalStatement:** dH(x,y)≥0; dH(x,y)=0 iff x=y; dH(x,y)=dH(y,x); dH(x,z)≤dH(x,y)+dH(y,z).

**assumptions:** Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state.

**dependsOn:** [distance-equation](HammingSpace.md#node-urn-csabs-axiom-HammingSpace-distance-equation)

**proofSketch:** For the triangle inequality each coordinate with xi≠zi has xi≠yi or yi≠zi. Sum the indicator inequalities; the other properties follow coordinatewise.

**reviewStatus:** Editorial statement-to-Lean correspondence review; a full-claim witness is registered separately in lean/bindings.json. Consult a fresh verification report for compiler and axiom-audit evidence.

**source:** [Georg Böcherer, Lecture Notes on Channel Coding (2016)](https://arxiv.org/html/1607.00974v1); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §7.1 Hamming geometry

**sourceNote:** Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ (X : Type) [DecidableEq X] (n : ℕ) (x y z : Fin n → X), 0 ≤ Catalog.Information.hamming x y ∧ (Catalog.Information.hamming x y = 0 ↔ x=y) ∧ Catalog.Information.hamming x y = Catalog.Information.hamming y x ∧ Catalog.Information.hamming x z ≤ Catalog.Information.hamming x y + Catalog.Information.hamming y z
```

**Source:** [`Catalog.Information.Verified.hammingMetric`](../lean/Catalog/InformationTheoryStatements.lean); consulted 2026-11-12.

**Scope:** registered-witness-type

**Interpretation:** Finite exact profile. dH(x,y)≥0; dH(x,y)=0 iff x=y; dH(x,y)=dH(y,x); dH(x,z)≤dH(x,y)+dH(y,z). The compiled Targets proposition supplies explicit carriers and hypotheses; the independently expanded expected type is retained here. Nat minima are used only under nontrivial-code assumptions; source and channel blocks use positive lengths.

**Limits:** Witness proves the entire expanded expected type; correspondence to the informal statement is a reviewed mapping. This does not prove other catalog targets or an implementation refinement.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/HammingSpace-distance-equation": "Explicit premise: dH(x,y)=Σi 1{xi≠yi}; B(x,t)={y:dH(x,y)≤t}. Implemented by the normalized finite-law, exact finite-field, prefix-word or Hamming definitions and proved helper lemmas in InformationTheoryProofs/Statements; not introduced as a global axiom."
}
```

## Theorems

<a id="node-urn-csabs-theorem-HammingSpace-ball-volume"></a>

### Hamming ball volume

`urn:csabs:theorem/HammingSpace-ball-volume`

**statement:** For 0≤t≤n, |B(x,t)|=Σi=0ᵗ binom(n,i)(q−1)^i.

**formalStatement:** For 0≤t≤n, |B(x,t)|=Σi=0ᵗ binom(n,i)(q−1)^i.

**assumptions:** Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state.

**dependsOn:** [distance-equation](HammingSpace.md#node-urn-csabs-axiom-HammingSpace-distance-equation)

**proofSketch:** Choose the i changed positions and one of q−1 replacement symbols at each position; the disjoint shells partition the ball.

**reviewStatus:** Editorial proof sketch; no registered Lean theorem witness.

**source:** [Venkatesan Guruswami, Introduction to Coding Theory, Notes 1 (CMU, January 2010)](https://www.cs.cmu.edu/~venkatg/teaching/codingtheory/notes/notes1.pdf); accessedOn: 2026-11-11; sourceRole: consulted lecturer-authored definitions and Hamming packing argument

**sourceLocator:** Notes 1, §3.1, Lemma 13 and preceding disjoint-ball argument (pp. 7–8); adapted from binary to q-ary words

**sourceNote:** Adapt the consulted binary packing argument to q-ary words by counting q−1 possible replacements at each changed coordinate. The linked premises and proof sketch state the extension.

**provenanceKind:** derived

## Concept provenance

- [Georg Böcherer, Lecture Notes on Channel Coding (2016)](https://arxiv.org/html/1607.00974v1); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §7.1 Hamming geometry

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/HammingSpace",
    "type": "Concept",
    "shortForm": "HammingSpace",
    "fullName": "Hamming space (finite fixed-length words)",
    "category": [
      "urn:csabs:category/channel-coding"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "Finite word space equipped with the number of unequal coordinates.",
    "notation": "(Σⁿ,dH); dH(x,y)=|{i:xi≠yi}|",
    "requiresConcept": [
      "urn:csabs:concept/FiniteSet",
      "urn:csabs:concept/Sequence"
    ],
    "relatedConcept": [],
    "hasOperation": [
      "urn:csabs:operation/HammingSpace-distance",
      "urn:csabs:operation/HammingSpace-ball"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/HammingSpace-distance-equation"
    ],
    "hasLaw": [
      "urn:csabs:law/HammingSpace-metric"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/HammingSpace-ball-volume"
    ],
    "axiomBasis": "dH(x,y)=Σi 1{xi≠yi}; B(x,t)={y:dH(x,y)≤t}.",
    "basisKind": "extensional-structural-definition",
    "basisScope": "Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial mathematical review; Lean models are explicitly scoped and theorem sketches are not compiled proofs.",
    "verificationObligation": [
      "Map alphabets, exact arithmetic, equality, logarithm base, channel model and error criterion before use.",
      "Retrieve explicit premises; category and specialization links do not inherit claims."
    ],
    "source": [
      "urn:csabs:source/boecherer-channel-coding"
    ],
    "sourceLocator": "§7.1 Hamming geometry",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted",
    "leanFormulation": "abbrev HammingSpace := @Information.hamming",
    "formulationSource": "urn:csabs:source/local-lean-InformationTheory",
    "formulationLocator": "Catalog.HammingSpace",
    "formulationScope": "partial",
    "leanModelMapping": "Fin n→A words and Nat count of unequal coordinates, with decidable symbol equality. Instantiate n≥1 and finite alphabet of size at least two.",
    "leanModelLimitations": "Hamming balls and metric-law witnesses omitted. These are model bindings, not proofs of the catalog theorems.",
    "mathematicalFormulation": "For words x,y∈A^n, d_H(x,y)=|{i∈Fin(n) | x_i≠y_i}|. No field operations are needed; coordinate equality is decidable in the Lean evaluator, and n=0 is allowed."
  },
  {
    "id": "urn:csabs:operation/HammingSpace-distance",
    "type": "Operation",
    "name": "distance",
    "signature": "dH : Σⁿ×Σⁿ → ℕ",
    "description": "Count coordinates with unequal symbols.",
    "concept": "urn:csabs:concept/HammingSpace",
    "precondition": "Inputs satisfy the concept profile.",
    "totality": "Total on the stated domain.",
    "postcondition": "Count coordinates with unequal symbols.",
    "source": [
      "urn:csabs:source/boecherer-channel-coding"
    ],
    "sourceLocator": "§7.1 Hamming geometry",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/HammingSpace-ball",
    "type": "Operation",
    "name": "ball",
    "signature": "ball : Σⁿ×ℕ → FinSet(Σⁿ)",
    "description": "B(x,t)={y:dH(x,y)≤t}; a radius t≥n gives the entire space.",
    "concept": "urn:csabs:concept/HammingSpace",
    "precondition": "Inputs satisfy the concept profile.",
    "totality": "Total on the stated domain.",
    "postcondition": "B(x,t)={y:dH(x,y)≤t}; a radius t≥n gives the entire space.",
    "source": [
      "urn:csabs:source/boecherer-channel-coding"
    ],
    "sourceLocator": "§7.1 Hamming geometry",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/HammingSpace-distance-equation",
    "type": "Axiom",
    "name": "distance-equation",
    "statement": "dH(x,y)=Σi 1{xi≠yi}; B(x,t)={y:dH(x,y)≤t}.",
    "formalStatement": "dH(x,y)=Σi 1{xi≠yi}; B(x,t)={y:dH(x,y)≤t}.",
    "assumptions": [
      "Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state."
    ],
    "appliesTo": [
      "urn:csabs:concept/HammingSpace"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Sourced structural definition, not an independent foundational axiom.",
    "source": [
      "urn:csabs:source/boecherer-channel-coding"
    ],
    "sourceLocator": "§7.1 Hamming geometry",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/HammingSpace-metric",
    "type": "Law",
    "name": "Hamming metric laws",
    "statement": "dH(x,y)≥0; dH(x,y)=0 iff x=y; dH(x,y)=dH(y,x); dH(x,z)≤dH(x,y)+dH(y,z).",
    "formalStatement": "dH(x,y)≥0; dH(x,y)=0 iff x=y; dH(x,y)=dH(y,x); dH(x,z)≤dH(x,y)+dH(y,z).",
    "assumptions": [
      "Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state."
    ],
    "appliesTo": [
      "urn:csabs:concept/HammingSpace"
    ],
    "dependsOn": [
      "urn:csabs:axiom/HammingSpace-distance-equation"
    ],
    "proofSketch": "For the triangle inequality each coordinate with xi≠zi has xi≠yi or yi≠zi. Sum the indicator inequalities; the other properties follow coordinatewise.",
    "reviewStatus": "Editorial statement-to-Lean correspondence review; a full-claim witness is registered separately in lean/bindings.json. Consult a fresh verification report for compiler and axiom-audit evidence.",
    "source": [
      "urn:csabs:source/boecherer-channel-coding"
    ],
    "sourceLocator": "§7.1 Hamming geometry",
    "sourceNote": "Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ (X : Type) [DecidableEq X] (n : ℕ) (x y z : Fin n → X), 0 ≤ Catalog.Information.hamming x y ∧ (Catalog.Information.hamming x y = 0 ↔ x=y) ∧ Catalog.Information.hamming x y = Catalog.Information.hamming y x ∧ Catalog.Information.hamming x z ≤ Catalog.Information.hamming x y + Catalog.Information.hamming y z",
    "formulationSource": "urn:csabs:source/local-lean-InformationTheoryStatements",
    "formulationLocator": "Catalog.Information.Verified.hammingMetric",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Finite exact profile. dH(x,y)≥0; dH(x,y)=0 iff x=y; dH(x,y)=dH(y,x); dH(x,z)≤dH(x,y)+dH(y,z). The compiled Targets proposition supplies explicit carriers and hypotheses; the independently expanded expected type is retained here. Nat minima are used only under nontrivial-code assumptions; source and channel blocks use positive lengths.",
    "leanModelLimitations": "Witness proves the entire expanded expected type; correspondence to the informal statement is a reviewed mapping. This does not prove other catalog targets or an implementation refinement.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/HammingSpace-distance-equation\": \"Explicit premise: dH(x,y)=Σi 1{xi≠yi}; B(x,t)={y:dH(x,y)≤t}. Implemented by the normalized finite-law, exact finite-field, prefix-word or Hamming definitions and proved helper lemmas in InformationTheoryProofs/Statements; not introduced as a global axiom.\"}"
  },
  {
    "id": "urn:csabs:theorem/HammingSpace-ball-volume",
    "type": "Theorem",
    "name": "Hamming ball volume",
    "statement": "For 0≤t≤n, |B(x,t)|=Σi=0ᵗ binom(n,i)(q−1)^i.",
    "formalStatement": "For 0≤t≤n, |B(x,t)|=Σi=0ᵗ binom(n,i)(q−1)^i.",
    "assumptions": [
      "Finite alphabet Σ with q=|Σ|≥2; fixed n≥1; words have exactly n coordinates; exact symbol equality. No insertions, deletions, soft decisions or concurrent state."
    ],
    "appliesTo": [
      "urn:csabs:concept/HammingSpace"
    ],
    "dependsOn": [
      "urn:csabs:axiom/HammingSpace-distance-equation"
    ],
    "proofSketch": "Choose the i changed positions and one of q−1 replacement symbols at each position; the disjoint shells partition the ball.",
    "reviewStatus": "Editorial proof sketch; no registered Lean theorem witness.",
    "source": [
      "urn:csabs:source/guruswami-coding-introduction"
    ],
    "sourceLocator": "Notes 1, §3.1, Lemma 13 and preceding disjoint-ball argument (pp. 7–8); adapted from binary to q-ary words",
    "sourceNote": "Adapt the consulted binary packing argument to q-ary words by counting q−1 possible replacements at each changed coordinate. The linked premises and proof sketch state the extension.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
