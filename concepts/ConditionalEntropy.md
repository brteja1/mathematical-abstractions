# Conditional entropy (finite discrete profile)

Average entropy of conditional laws under a joint distribution.

**Notation:** H(X|Y)=Σ{y:pY(y)>0}pY(y)H(pX|y)

**Stable ID:** `urn:csabs:concept/ConditionalEntropy`

**Categories:** Information theory

**Kind:** Function

**Prerequisites:** [Shannon entropy (finite discrete profile)](ShannonEntropy.md), [Conditional probability given a positive-probability event](ConditionalProbability.md)

## Backlinks

- [Mutual information (finite discrete profile)](MutualInformation.md) — `requiresConcept`

## Mathematical formulation

For a finite joint law p on A×B and p\_B(b)=Σ\_a p(a,b), H(A|B)=−Σ\_{a,b}p(a,b)log₂(p(a,b)/p\_B(b)). Terms of zero joint mass contribute 0, including zero marginal cases.

**Lean formulation** (in its source module context):

```lean
abbrev ConditionalEntropy := @Information.conditionalEntropy
```

**Source:** [`Catalog.ConditionalEntropy`](../lean/Catalog/InformationTheory.lean); consulted 2026-11-12.

**Scope:** partial

**Interpretation:** Finite normalized joint Law; conditional entropy is a joint-mass weighted log ratio using the Y marginal. Null joint masses vanish.

**Limits:** Conditional laws and chain-rule correspondence unproved. These are model bindings, not proofs of the catalog theorems.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** For pY(y)>0, pX|y(x)=p(x,y)/pY(y); H(X|Y)=Σ{y:pY(y)>0}pY(y)H(pX|y).

**basisKind:** extensional-structural-definition

**basisScope:** Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. Null conditioning events are omitted; conditional laws on them are arbitrary.

**verificationObligation:** Map alphabets, exact arithmetic, equality, logarithm base, channel model and error criterion before use.; Retrieve explicit premises; category and specialization links do not inherit claims.

**reviewStatus:** Editorial mathematical review; Lean models are explicitly scoped and theorem sketches are not compiled proofs.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-ConditionalEntropy-conditional-entropy"></a>

### conditional-entropy

`urn:csabs:operation/ConditionalEntropy-conditional-entropy`

**signature:** Hcond : Dist(A×B) → ℝ

**description:** Average H(pX|y) over positive-mass y.

**precondition:** Inputs satisfy the concept profile.

**totality:** Total on the stated domain.

**postcondition:** Average H(pX|y) over positive-mass y.

**source:** [Yury Polyanskiy, MIT 6.441 (2016), Chapter 1: Information measures: entropy and divergence](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/2243edffb30f57181ed97dcb77691580_MIT6_441S16_chapter_1.pdf); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §1.1 Definition 1.3 and Theorem 1.1

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-ConditionalEntropy-conditional-equation"></a>

### conditional-equation

`urn:csabs:axiom/ConditionalEntropy-conditional-equation`

**statement:** For pY(y)>0, pX|y(x)=p(x,y)/pY(y); H(X|Y)=Σ{y:pY(y)>0}pY(y)H(pX|y).

**formalStatement:** For pY(y)>0, pX|y(x)=p(x,y)/pY(y); H(X|Y)=Σ{y:pY(y)>0}pY(y)H(pX|y).

**assumptions:** Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. Null conditioning events are omitted; conditional laws on them are arbitrary.

**ruleRole:** defining-rule

**reviewStatus:** Sourced structural definition, not an independent foundational axiom.

**source:** [Yury Polyanskiy, MIT 6.441 (2016), Chapter 1: Information measures: entropy and divergence](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/2243edffb30f57181ed97dcb77691580_MIT6_441S16_chapter_1.pdf); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §1.1 Definition 1.3 and Theorem 1.1

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-ConditionalEntropy-chain-rule"></a>

### Entropy chain rule

`urn:csabs:law/ConditionalEntropy-chain-rule`

**statement:** H(X,Y)=H(Y)+H(X|Y).

**formalStatement:** H(X,Y)=H(Y)+H(X|Y).

**assumptions:** Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. Null conditioning events are omitted; conditional laws on them are arbitrary.

**dependsOn:** [entropy-equation](ShannonEntropy.md#node-urn-csabs-axiom-ShannonEntropy-entropy-equation); [conditional-equation](ConditionalEntropy.md#node-urn-csabs-axiom-ConditionalEntropy-conditional-equation)

**proofSketch:** Factor positive joint masses as pY(y)pX|y(x), split the logarithm, and sum.

**reviewStatus:** Editorial statement-to-Lean correspondence review; a full-claim witness is registered separately in lean/bindings.json. Consult a fresh verification report for compiler and axiom-audit evidence.

**source:** [Yury Polyanskiy, MIT 6.441 (2016), Chapter 1: Information measures: entropy and divergence](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/2243edffb30f57181ed97dcb77691580_MIT6_441S16_chapter_1.pdf); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §1.1 Definition 1.3 and Theorem 1.1

**sourceNote:** Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ (A B : Type) [Fintype A] [Fintype B] (p : Catalog.Information.Law (A×B)), Catalog.Information.entropy p = Catalog.Information.entropy (Catalog.Information.marginalY p) + Catalog.Information.conditionalEntropy p
```

**Source:** [`Catalog.Information.Verified.chainRule`](../lean/Catalog/InformationTheoryStatements.lean); consulted 2026-11-12.

**Scope:** registered-witness-type

**Interpretation:** Finite exact profile. H(X,Y)=H(Y)+H(X|Y). The compiled Targets proposition supplies explicit carriers and hypotheses; the independently expanded expected type is retained here. Nat minima are used only under nontrivial-code assumptions; source and channel blocks use positive lengths.

**Limits:** Witness proves the entire expanded expected type; correspondence to the informal statement is a reviewed mapping. This does not prove other catalog targets or an implementation refinement.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/ConditionalEntropy-conditional-equation": "Explicit premise: For pY(y)>0, pX|y(x)=p(x,y)/pY(y); H(X|Y)=Σ{y:pY(y)>0}pY(y)H(pX|y). Implemented by the normalized finite-law, exact finite-field, prefix-word or Hamming definitions and proved helper lemmas in InformationTheoryProofs/Statements; not introduced as a global axiom.",
  "urn:csabs:axiom/ShannonEntropy-entropy-equation": "Explicit premise: H(p)=−Σ{x | p(x)>0} p(x)log₂p(x). Implemented by the normalized finite-law, exact finite-field, prefix-word or Hamming definitions and proved helper lemmas in InformationTheoryProofs/Statements; not introduced as a global axiom."
}
```

## Theorems

<a id="node-urn-csabs-theorem-ConditionalEntropy-conditioning-reduces"></a>

### Conditioning reduces entropy

`urn:csabs:theorem/ConditionalEntropy-conditioning-reduces`

**statement:** 0≤H(X|Y)≤H(X); equality H(X|Y)=H(X) iff X and Y are independent.

**formalStatement:** 0≤H(X|Y)≤H(X); equality H(X|Y)=H(X) iff X and Y are independent.

**assumptions:** Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. Null conditioning events are omitted; conditional laws on them are arbitrary.

**dependsOn:** [Mutual information entropy identities](MutualInformation.md#node-urn-csabs-theorem-MutualInformation-entropy-identity); [conditional-equation](ConditionalEntropy.md#node-urn-csabs-axiom-ConditionalEntropy-conditional-equation)

**proofSketch:** Conditional entropies are averages of nonnegative entropies; use H(X)−H(X|Y)=I(X;Y) and its equality case.

**reviewStatus:** Editorial proof sketch; no registered Lean theorem witness.

**source:** [Yury Polyanskiy, MIT 6.441 (2016), Chapter 2: Information measures: mutual information](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/184197ca5d5418da2415d37e929860b9_MIT6_441S16_chapter_2.pdf); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** Corollary 2.4

**sourceNote:** Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.

**provenanceKind:** derived

<a id="node-urn-csabs-theorem-ConditionalEntropy-fano"></a>

### Fano inequality

`urn:csabs:theorem/ConditionalEntropy-fano`

**statement:** For X with |A|=m≥2, estimate X̂=g(Y)∈A, and Pe=Pr[X̂≠X], H(X|Y)≤h₂(Pe)+Pe log₂(m−1), where h₂(u)=−u log₂u−(1−u)log₂(1−u).

**formalStatement:** For X with |A|=m≥2, estimate X̂=g(Y)∈A, and Pe=Pr[X̂≠X], H(X|Y)≤h₂(Pe)+Pe log₂(m−1), where h₂(u)=−u log₂u−(1−u)log₂(1−u).

**assumptions:** Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. Null conditioning events are omitted; conditional laws on them are arbitrary.; m≥2; deterministic estimator; average error under the specified joint law.

**dependsOn:** [Entropy chain rule](ConditionalEntropy.md#node-urn-csabs-law-ConditionalEntropy-chain-rule); [Entropy bounds and maximizing distribution](ShannonEntropy.md#node-urn-csabs-theorem-ShannonEntropy-entropy-bounds); [Conditioning reduces entropy](ConditionalEntropy.md#node-urn-csabs-theorem-ConditionalEntropy-conditioning-reduces)

**proofSketch:** Introduce E=1{X̂≠X}. Chain the conditional entropy of (E,X) given Y. E contributes at most h₂(Pe), and on error X has at most m−1 possibilities.

**reviewStatus:** Editorial proof sketch; no registered Lean theorem witness.

**source:** [Yury Polyanskiy, MIT 6.441 (2016), Chapter 5: Probability of error and entropy rate](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/b208f091f76052d60eda895dc8d13e97_MIT6_441S16_chapter_5.pdf); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §5.3 Theorem 5.3

**sourceNote:** Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.

**provenanceKind:** derived

## Concept provenance

- [Yury Polyanskiy, MIT 6.441 (2016), Chapter 1: Information measures: entropy and divergence](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/2243edffb30f57181ed97dcb77691580_MIT6_441S16_chapter_1.pdf); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §1.1 Definition 1.3 and Theorem 1.1

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/ConditionalEntropy",
    "type": "Concept",
    "shortForm": "ConditionalEntropy",
    "fullName": "Conditional entropy (finite discrete profile)",
    "category": [
      "urn:csabs:category/information-theory"
    ],
    "kind": "urn:csabs:kind/function",
    "definition": "Average entropy of conditional laws under a joint distribution.",
    "notation": "H(X|Y)=Σ{y:pY(y)>0}pY(y)H(pX|y)",
    "requiresConcept": [
      "urn:csabs:concept/ShannonEntropy",
      "urn:csabs:concept/ConditionalProbability"
    ],
    "relatedConcept": [],
    "hasOperation": [
      "urn:csabs:operation/ConditionalEntropy-conditional-entropy"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/ConditionalEntropy-conditional-equation"
    ],
    "hasLaw": [
      "urn:csabs:law/ConditionalEntropy-chain-rule"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/ConditionalEntropy-conditioning-reduces",
      "urn:csabs:theorem/ConditionalEntropy-fano"
    ],
    "axiomBasis": "For pY(y)>0, pX|y(x)=p(x,y)/pY(y); H(X|Y)=Σ{y:pY(y)>0}pY(y)H(pX|y).",
    "basisKind": "extensional-structural-definition",
    "basisScope": "Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. Null conditioning events are omitted; conditional laws on them are arbitrary.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial mathematical review; Lean models are explicitly scoped and theorem sketches are not compiled proofs.",
    "verificationObligation": [
      "Map alphabets, exact arithmetic, equality, logarithm base, channel model and error criterion before use.",
      "Retrieve explicit premises; category and specialization links do not inherit claims."
    ],
    "source": [
      "urn:csabs:source/mit-information-1"
    ],
    "sourceLocator": "§1.1 Definition 1.3 and Theorem 1.1",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted",
    "leanFormulation": "abbrev ConditionalEntropy := @Information.conditionalEntropy",
    "formulationSource": "urn:csabs:source/local-lean-InformationTheory",
    "formulationLocator": "Catalog.ConditionalEntropy",
    "formulationScope": "partial",
    "leanModelMapping": "Finite normalized joint Law; conditional entropy is a joint-mass weighted log ratio using the Y marginal. Null joint masses vanish.",
    "leanModelLimitations": "Conditional laws and chain-rule correspondence unproved. These are model bindings, not proofs of the catalog theorems.",
    "mathematicalFormulation": "For a finite joint law p on A×B and p_B(b)=Σ_a p(a,b), H(A|B)=−Σ_{a,b}p(a,b)log₂(p(a,b)/p_B(b)). Terms of zero joint mass contribute 0, including zero marginal cases."
  },
  {
    "id": "urn:csabs:operation/ConditionalEntropy-conditional-entropy",
    "type": "Operation",
    "name": "conditional-entropy",
    "signature": "Hcond : Dist(A×B) → ℝ",
    "description": "Average H(pX|y) over positive-mass y.",
    "concept": "urn:csabs:concept/ConditionalEntropy",
    "precondition": "Inputs satisfy the concept profile.",
    "totality": "Total on the stated domain.",
    "postcondition": "Average H(pX|y) over positive-mass y.",
    "source": [
      "urn:csabs:source/mit-information-1"
    ],
    "sourceLocator": "§1.1 Definition 1.3 and Theorem 1.1",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/ConditionalEntropy-conditional-equation",
    "type": "Axiom",
    "name": "conditional-equation",
    "statement": "For pY(y)>0, pX|y(x)=p(x,y)/pY(y); H(X|Y)=Σ{y:pY(y)>0}pY(y)H(pX|y).",
    "formalStatement": "For pY(y)>0, pX|y(x)=p(x,y)/pY(y); H(X|Y)=Σ{y:pY(y)>0}pY(y)H(pX|y).",
    "assumptions": [
      "Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. Null conditioning events are omitted; conditional laws on them are arbitrary."
    ],
    "appliesTo": [
      "urn:csabs:concept/ConditionalEntropy"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Sourced structural definition, not an independent foundational axiom.",
    "source": [
      "urn:csabs:source/mit-information-1"
    ],
    "sourceLocator": "§1.1 Definition 1.3 and Theorem 1.1",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/ConditionalEntropy-chain-rule",
    "type": "Law",
    "name": "Entropy chain rule",
    "statement": "H(X,Y)=H(Y)+H(X|Y).",
    "formalStatement": "H(X,Y)=H(Y)+H(X|Y).",
    "assumptions": [
      "Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. Null conditioning events are omitted; conditional laws on them are arbitrary."
    ],
    "appliesTo": [
      "urn:csabs:concept/ConditionalEntropy"
    ],
    "dependsOn": [
      "urn:csabs:axiom/ShannonEntropy-entropy-equation",
      "urn:csabs:axiom/ConditionalEntropy-conditional-equation"
    ],
    "proofSketch": "Factor positive joint masses as pY(y)pX|y(x), split the logarithm, and sum.",
    "reviewStatus": "Editorial statement-to-Lean correspondence review; a full-claim witness is registered separately in lean/bindings.json. Consult a fresh verification report for compiler and axiom-audit evidence.",
    "source": [
      "urn:csabs:source/mit-information-1"
    ],
    "sourceLocator": "§1.1 Definition 1.3 and Theorem 1.1",
    "sourceNote": "Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ (A B : Type) [Fintype A] [Fintype B] (p : Catalog.Information.Law (A×B)), Catalog.Information.entropy p = Catalog.Information.entropy (Catalog.Information.marginalY p) + Catalog.Information.conditionalEntropy p",
    "formulationSource": "urn:csabs:source/local-lean-InformationTheoryStatements",
    "formulationLocator": "Catalog.Information.Verified.chainRule",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Finite exact profile. H(X,Y)=H(Y)+H(X|Y). The compiled Targets proposition supplies explicit carriers and hypotheses; the independently expanded expected type is retained here. Nat minima are used only under nontrivial-code assumptions; source and channel blocks use positive lengths.",
    "leanModelLimitations": "Witness proves the entire expanded expected type; correspondence to the informal statement is a reviewed mapping. This does not prove other catalog targets or an implementation refinement.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/ConditionalEntropy-conditional-equation\": \"Explicit premise: For pY(y)>0, pX|y(x)=p(x,y)/pY(y); H(X|Y)=Σ{y:pY(y)>0}pY(y)H(pX|y). Implemented by the normalized finite-law, exact finite-field, prefix-word or Hamming definitions and proved helper lemmas in InformationTheoryProofs/Statements; not introduced as a global axiom.\", \"urn:csabs:axiom/ShannonEntropy-entropy-equation\": \"Explicit premise: H(p)=−Σ{x | p(x)>0} p(x)log₂p(x). Implemented by the normalized finite-law, exact finite-field, prefix-word or Hamming definitions and proved helper lemmas in InformationTheoryProofs/Statements; not introduced as a global axiom.\"}"
  },
  {
    "id": "urn:csabs:theorem/ConditionalEntropy-conditioning-reduces",
    "type": "Theorem",
    "name": "Conditioning reduces entropy",
    "statement": "0≤H(X|Y)≤H(X); equality H(X|Y)=H(X) iff X and Y are independent.",
    "formalStatement": "0≤H(X|Y)≤H(X); equality H(X|Y)=H(X) iff X and Y are independent.",
    "assumptions": [
      "Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. Null conditioning events are omitted; conditional laws on them are arbitrary."
    ],
    "appliesTo": [
      "urn:csabs:concept/ConditionalEntropy"
    ],
    "dependsOn": [
      "urn:csabs:theorem/MutualInformation-entropy-identity",
      "urn:csabs:axiom/ConditionalEntropy-conditional-equation"
    ],
    "proofSketch": "Conditional entropies are averages of nonnegative entropies; use H(X)−H(X|Y)=I(X;Y) and its equality case.",
    "reviewStatus": "Editorial proof sketch; no registered Lean theorem witness.",
    "source": [
      "urn:csabs:source/mit-information-2"
    ],
    "sourceLocator": "Corollary 2.4",
    "sourceNote": "Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/ConditionalEntropy-fano",
    "type": "Theorem",
    "name": "Fano inequality",
    "statement": "For X with |A|=m≥2, estimate X̂=g(Y)∈A, and Pe=Pr[X̂≠X], H(X|Y)≤h₂(Pe)+Pe log₂(m−1), where h₂(u)=−u log₂u−(1−u)log₂(1−u).",
    "formalStatement": "For X with |A|=m≥2, estimate X̂=g(Y)∈A, and Pe=Pr[X̂≠X], H(X|Y)≤h₂(Pe)+Pe log₂(m−1), where h₂(u)=−u log₂u−(1−u)log₂(1−u).",
    "assumptions": [
      "Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. Null conditioning events are omitted; conditional laws on them are arbitrary.",
      "m≥2; deterministic estimator; average error under the specified joint law."
    ],
    "appliesTo": [
      "urn:csabs:concept/ConditionalEntropy"
    ],
    "dependsOn": [
      "urn:csabs:law/ConditionalEntropy-chain-rule",
      "urn:csabs:theorem/ShannonEntropy-entropy-bounds",
      "urn:csabs:theorem/ConditionalEntropy-conditioning-reduces"
    ],
    "proofSketch": "Introduce E=1{X̂≠X}. Chain the conditional entropy of (E,X) given Y. E contributes at most h₂(Pe), and on error X has at most m−1 possibilities.",
    "reviewStatus": "Editorial proof sketch; no registered Lean theorem witness.",
    "source": [
      "urn:csabs:source/mit-information-5"
    ],
    "sourceLocator": "§5.3 Theorem 5.3",
    "sourceNote": "Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
