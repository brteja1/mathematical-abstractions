# Arithmetic mean of a finite real sample

The exact unweighted arithmetic mean of a nonempty finite multiset of real observations. Multiplicities contribute repeatedly, order is irrelevant, and the empty-sample result is undefined.

**Notation:** μ(S)=(Σ_{x∈S}x)/|S| for |S|>0; meanOption(∅)=none.

**Stable ID:** `urn:csabs:concept/ArithmeticMean`

**Categories:** Statistics → Descriptive statistics

**Kind:** Function

**Prerequisites:** [Multiset](Multiset.md), [Exact real number](RealNumber.md), [Partial function](PartialFunction.md)

**Specializes:** [Partial function](PartialFunction.md)

**Related concepts:** [Numeric sample median (midpoint convention)](Median.md), [Empirical mode set (all observed frequency maximizers)](Mode.md), [Finitely supported probability distribution](FiniteDistribution.md)

## Backlinks

- [Finitely supported probability distribution](FiniteDistribution.md) — `relatedConcept`
- [Numeric sample median (midpoint convention)](Median.md) — `relatedConcept`
- [Empirical mode set (all observed frequency maximizers)](Mode.md) — `relatedConcept`
- [Multiset](Multiset.md) — `relatedConcept`

## Mathematical formulation

For a finite multiset S of exact real observations, let N=|S| count repetitions and T=Σ\_{x∈S}x. If N>0, μ(S)=T/N; equivalently μ(S)=Σ\_{a∈supp(S)}c\_S(a)a/N. The partial statistic is undefined at N=0; its total Option encoding returns none there and some(T/N) otherwise. Input equality is multiset equality and output equality is exact real equality. Integer/rational observations may be embedded in ℝ; division is not integer truncation.

**Lean formulation** (in its source module context):

```lean
def ArithmeticMean (sample : _root_.Multiset ℝ) : Option ℝ :=
  if sample.card = 0 then none else some (sample.sum / (sample.card : ℝ))
```

**Source:** [`Catalog.ArithmeticMean`](../lean/Catalog/DescriptiveStatistics.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Multiset ℝ with exact sum and occurrence cardinality. ArithmeticMean returns Option ℝ; card=0 yields none before division, otherwise some(sum/card). The input quotient removes order but preserves multiplicity; no arithmetic rounding is modeled.

**Limits:** Exact selected finite-multiset interface. No floating-point error analysis, missing-data handling, weighted/population inference, complexity claim or numerical implementation refinement. Only individually registered results have compiled witnesses; the separately recorded theorem is not a registered proof.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** The stated finite-multiset definition, explicit empty behavior and selected output convention. Finite unweighted multiset of exact real observations, with repeated observations retained. N counts multiplicity; sum counts every occurrence. The mathematical mean requires N>0 and the model explicitly guards the totalized real division at zero. No NaNs, infinities, missing-value policy, rounding, overflow, weighted observations or probabilistic sampling assumptions are included.

**basisKind:** defined-function

**basisScope:** Selected unweighted finite-sample statistic, not all weighted/population/rounded or interpolation conventions.

**convention:** Finite unweighted multiset of exact real observations, with repeated observations retained. N counts multiplicity; sum counts every occurrence. The mathematical mean requires N>0 and the model explicitly guards the totalized real division at zero. No NaNs, infinities, missing-value policy, rounding, overflow, weighted observations or probabilistic sampling assumptions are included.

**specializationNote:** Instantiate the partial-function domain by Bag(ℝ) and codomain by ℝ. Definedness is exactly nonempty input; the total representation Bag(ℝ)→Option(ℝ) returns none on empty input and some(value) otherwise. The statistic has its own explicit defining rules; specialization does not transfer axioms.

**verificationObligation:** Map multiplicity, equality, empty/missing-data policy, exact numeric semantics and tie/interpolation conventions to the target API. A compiled abstract identity is not implementation refinement.

**reviewStatus:** Sourced mathematical formulation with a separate Lean model and individually mapped witnesses.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-ArithmeticMean-evaluate"></a>

### evaluate

`urn:csabs:operation/ArithmeticMean-evaluate`

**signature:** Bag(ℝ) → Option(ℝ)

**description:** Compute the exact finite-sample mean with explicit undefinedness.

**precondition:** A finite multiset of exact real observations.

**postcondition:** none exactly for S=∅; otherwise some((Σ_{x∈S}x)/|S|).

**totality:** total on the stated typed domain; Option represents mathematical undefinedness, not an arbitrary default value

## Axioms and defining rules

<a id="node-urn-csabs-axiom-ArithmeticMean-definition"></a>

### definition

`urn:csabs:axiom/ArithmeticMean-definition`

**statement:** The nonempty arithmetic mean divides the occurrence sum by the occurrence count; the empty result is undefined.

**formalStatement:** N=|S|; T=Σ_{x∈S}x; meanOption(S)=if N=0 then none else some(T/N); dom(μ)={S | |S|>0}.

**assumptions:** Finite unweighted multiset of exact real observations, with repeated observations retained. N counts multiplicity; sum counts every occurrence. The mathematical mean requires N>0 and the model explicitly guards the totalized real division at zero. No NaNs, infinities, missing-value policy, rounding, overflow, weighted observations or probabilistic sampling assumptions are included.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Sourced mathematical definition; compilation status belongs to separate Lean evidence.

**source:** [NIST/SEMATECH e-Handbook of Statistical Methods: §1.3.5.1 Measures of Location](https://www.itl.nist.gov/div898/handbook/eda/section3/eda351.htm); accessedOn: 2026-11-12; sourceRole: Consulted definitions of arithmetic mean, odd/even sample median and nonunique empirical modes; the catalog makes empty-data and tie conventions explicit.

**sourceLocator:** NIST §1.3.5.1, Definition of Location, item 1 (mean formula)

**sourceNote:** Adapts the finite-sample arithmetic mean to an order-independent real multiset and an explicit Option encoding of empty-sample undefinedness. No population expectation, grouped-bin approximation, geometric/harmonic mean or arbitrary sample weights are identified with this profile.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-ArithmeticMean-singleton"></a>

### singleton

`urn:csabs:law/ArithmeticMean-singleton`

**statement:** A singleton sample has its sole value as mean.

**formalStatement:** μ({x})=x, equivalently meanOption({x})=some(x).

**assumptions:** Finite unweighted multiset of exact real observations, with repeated observations retained. N counts multiplicity; sum counts every occurrence. The mathematical mean requires N>0 and the model explicitly guards the totalized real division at zero. No NaNs, infinities, missing-value policy, rounding, overflow, weighted observations or probabilistic sampling assumptions are included.

**dependsOn:** [definition](ArithmeticMean.md#node-urn-csabs-axiom-ArithmeticMean-definition)

**proofSketch:** The occurrence count is 1 and sum is x, so division gives x.

**ruleRole:** derived-result

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial mathematical statement; only separately mapped fresh Lean witnesses are compiler-verified.

**source:** [NIST/SEMATECH e-Handbook of Statistical Methods: §1.3.5.1 Measures of Location](https://www.itl.nist.gov/div898/handbook/eda/section3/eda351.htm); accessedOn: 2026-11-12; sourceRole: Consulted definitions of arithmetic mean, odd/even sample median and nonunique empirical modes; the catalog makes empty-data and tie conventions explicit.

**sourceLocator:** NIST §1.3.5.1, Definition of Location, item 1 (mean formula)

**sourceNote:** Derived from the linked finite-sample definition and exact count/order/arithmetic conventions. Adapts the finite-sample arithmetic mean to an order-independent real multiset and an explicit Option encoding of empty-sample undefinedness. No population expectation, grouped-bin approximation, geometric/harmonic mean or arbitrary sample weights are identified with this profile.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ (x : ℝ), Catalog.ArithmeticMean {x} = some x
```

**Source:** [`Catalog.DescriptiveStatisticsProofs.mean_singleton`](../lean/Catalog/DescriptiveStatistics.lean); consulted 2026-11-12.

**Scope:** registered-witness-type

**Interpretation:** Multiset ℝ with exact sum and occurrence cardinality. ArithmeticMean returns Option ℝ; card=0 yields none before division, otherwise some(sum/card). The input quotient removes order but preserves multiplicity; no arithmetic rounding is modeled.

**Limits:** Proves the displayed result under the selected exact carrier/equality/empty/tie conventions. No proof of an arbitrary software implementation, population claim or numerical stability bound.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/ArithmeticMean-definition": "Interpreted by the explicit data guard/count/sort definition: N=|S|; T=Σ_{x∈S}x; meanOption(S)=if N=0 then none else some(T/N); dom(μ)={S | |S|>0}."
}
```

<a id="node-urn-csabs-law-ArithmeticMean-balance"></a>

### balance

`urn:csabs:law/ArithmeticMean-balance`

**statement:** Multiplying a defined mean by its occurrence count recovers the occurrence sum.

**formalStatement:** meanOption(S)=some(m) ⇒ |S|·m=Σ_{x∈S}x.

**assumptions:** Finite unweighted multiset of exact real observations, with repeated observations retained. N counts multiplicity; sum counts every occurrence. The mathematical mean requires N>0 and the model explicitly guards the totalized real division at zero. No NaNs, infinities, missing-value policy, rounding, overflow, weighted observations or probabilistic sampling assumptions are included.

**dependsOn:** [definition](ArithmeticMean.md#node-urn-csabs-axiom-ArithmeticMean-definition)

**proofSketch:** A defined mean has N>0. Multiply m=T/N by nonzero N and cancel the denominator.

**ruleRole:** derived-result

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial mathematical statement; only separately mapped fresh Lean witnesses are compiler-verified.

**source:** [NIST/SEMATECH e-Handbook of Statistical Methods: §1.3.5.1 Measures of Location](https://www.itl.nist.gov/div898/handbook/eda/section3/eda351.htm); accessedOn: 2026-11-12; sourceRole: Consulted definitions of arithmetic mean, odd/even sample median and nonunique empirical modes; the catalog makes empty-data and tie conventions explicit.

**sourceLocator:** NIST §1.3.5.1, Definition of Location, item 1 (mean formula)

**sourceNote:** Derived from the linked finite-sample definition and exact count/order/arithmetic conventions. Adapts the finite-sample arithmetic mean to an order-independent real multiset and an explicit Option encoding of empty-sample undefinedness. No population expectation, grouped-bin approximation, geometric/harmonic mean or arbitrary sample weights are identified with this profile.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ (sample : Multiset ℝ) (m : ℝ), Catalog.ArithmeticMean sample = some m → (sample.card : ℝ) * m = sample.sum
```

**Source:** [`Catalog.DescriptiveStatisticsProofs.mean_balance`](../lean/Catalog/DescriptiveStatistics.lean); consulted 2026-11-12.

**Scope:** registered-witness-type

**Interpretation:** Multiset ℝ with exact sum and occurrence cardinality. ArithmeticMean returns Option ℝ; card=0 yields none before division, otherwise some(sum/card). The input quotient removes order but preserves multiplicity; no arithmetic rounding is modeled.

**Limits:** Proves the displayed result under the selected exact carrier/equality/empty/tie conventions. No proof of an arbitrary software implementation, population claim or numerical stability bound.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/ArithmeticMean-definition": "Interpreted by the explicit data guard/count/sort definition: N=|S|; T=Σ_{x∈S}x; meanOption(S)=if N=0 then none else some(T/N); dom(μ)={S | |S|>0}."
}
```

## Theorems

<a id="node-urn-csabs-theorem-ArithmeticMean-weighted-merge"></a>

### weighted-merge

`urn:csabs:theorem/ArithmeticMean-weighted-merge`

**statement:** The mean of two nonempty bags is the size-weighted mean of their means.

**formalStatement:** For n=|S|>0 and k=|T|>0: μ(S⊎T)=(nμ(S)+kμ(T))/(n+k).

**assumptions:** Finite unweighted multiset of exact real observations, with repeated observations retained. N counts multiplicity; sum counts every occurrence. The mathematical mean requires N>0 and the model explicitly guards the totalized real division at zero. No NaNs, infinities, missing-value policy, rounding, overflow, weighted observations or probabilistic sampling assumptions are included.

**dependsOn:** [definition](ArithmeticMean.md#node-urn-csabs-axiom-ArithmeticMean-definition); [union](Multiset.md#node-urn-csabs-operation-Multiset-union)

**proofSketch:** Multiset union adds multiplicities, so its size is n+k and its sum is sum(S)+sum(T). Apply the mean definition and replace each sum by its cardinality times its mean. Averaging the two means without size weights is generally incorrect; equal sample sizes are sufficient for the simple midpoint formula.

**ruleRole:** derived-result

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial mathematical statement; only separately mapped fresh Lean witnesses are compiler-verified.

**source:** [NIST/SEMATECH e-Handbook of Statistical Methods: §1.3.5.1 Measures of Location](https://www.itl.nist.gov/div898/handbook/eda/section3/eda351.htm); accessedOn: 2026-11-12; sourceRole: Consulted definitions of arithmetic mean, odd/even sample median and nonunique empirical modes; the catalog makes empty-data and tie conventions explicit.

**sourceLocator:** NIST §1.3.5.1, Definition of Location, item 1 (mean formula)

**sourceNote:** Derived from the linked finite-sample definition and exact count/order/arithmetic conventions. Adapts the finite-sample arithmetic mean to an order-independent real multiset and an explicit Option encoding of empty-sample undefinedness. No population expectation, grouped-bin approximation, geometric/harmonic mean or arbitrary sample weights are identified with this profile.

**provenanceKind:** derived

## Concept provenance

- [NIST/SEMATECH e-Handbook of Statistical Methods: §1.3.5.1 Measures of Location](https://www.itl.nist.gov/div898/handbook/eda/section3/eda351.htm); accessedOn: 2026-11-12; sourceRole: Consulted definitions of arithmetic mean, odd/even sample median and nonunique empirical modes; the catalog makes empty-data and tie conventions explicit.

**sourceLocator:** NIST §1.3.5.1, Definition of Location, item 1 (mean formula)

**sourceNote:** Adapts the finite-sample arithmetic mean to an order-independent real multiset and an explicit Option encoding of empty-sample undefinedness. No population expectation, grouped-bin approximation, geometric/harmonic mean or arbitrary sample weights are identified with this profile.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/ArithmeticMean",
    "type": "Concept",
    "shortForm": "ArithmeticMean",
    "fullName": "Arithmetic mean of a finite real sample",
    "synonyms": [
      "mean",
      "average",
      "unweighted sample mean"
    ],
    "category": [
      "urn:csabs:category/descriptive-statistics"
    ],
    "kind": "urn:csabs:kind/function",
    "definition": "The exact unweighted arithmetic mean of a nonempty finite multiset of real observations. Multiplicities contribute repeatedly, order is irrelevant, and the empty-sample result is undefined.",
    "notation": "μ(S)=(Σ_{x∈S}x)/|S| for |S|>0; meanOption(∅)=none.",
    "mathematicalFormulation": "For a finite multiset S of exact real observations, let N=|S| count repetitions and T=Σ_{x∈S}x. If N>0, μ(S)=T/N; equivalently μ(S)=Σ_{a∈supp(S)}c_S(a)a/N. The partial statistic is undefined at N=0; its total Option encoding returns none there and some(T/N) otherwise. Input equality is multiset equality and output equality is exact real equality. Integer/rational observations may be embedded in ℝ; division is not integer truncation.",
    "hasOperation": [
      "urn:csabs:operation/ArithmeticMean-evaluate"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/ArithmeticMean-definition"
    ],
    "hasLaw": [
      "urn:csabs:law/ArithmeticMean-singleton",
      "urn:csabs:law/ArithmeticMean-balance"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/ArithmeticMean-weighted-merge"
    ],
    "requiresConcept": [
      "urn:csabs:concept/Multiset",
      "urn:csabs:concept/RealNumber",
      "urn:csabs:concept/PartialFunction"
    ],
    "relatedConcept": [
      "urn:csabs:concept/Median",
      "urn:csabs:concept/Mode",
      "urn:csabs:concept/FiniteDistribution"
    ],
    "axiomBasis": "The stated finite-multiset definition, explicit empty behavior and selected output convention. Finite unweighted multiset of exact real observations, with repeated observations retained. N counts multiplicity; sum counts every occurrence. The mathematical mean requires N>0 and the model explicitly guards the totalized real division at zero. No NaNs, infinities, missing-value policy, rounding, overflow, weighted observations or probabilistic sampling assumptions are included.",
    "basisKind": "defined-function",
    "basisScope": "Selected unweighted finite-sample statistic, not all weighted/population/rounded or interpolation conventions.",
    "convention": "Finite unweighted multiset of exact real observations, with repeated observations retained. N counts multiplicity; sum counts every occurrence. The mathematical mean requires N>0 and the model explicitly guards the totalized real division at zero. No NaNs, infinities, missing-value policy, rounding, overflow, weighted observations or probabilistic sampling assumptions are included.",
    "coverageStatus": "basis-reviewed",
    "verificationObligation": "Map multiplicity, equality, empty/missing-data policy, exact numeric semantics and tie/interpolation conventions to the target API. A compiled abstract identity is not implementation refinement.",
    "reviewStatus": "Sourced mathematical formulation with a separate Lean model and individually mapped witnesses.",
    "source": [
      "urn:csabs:source/nist-measures-of-location"
    ],
    "sourceLocator": "NIST §1.3.5.1, Definition of Location, item 1 (mean formula)",
    "sourceNote": "Adapts the finite-sample arithmetic mean to an order-independent real multiset and an explicit Option encoding of empty-sample undefinedness. No population expectation, grouped-bin approximation, geometric/harmonic mean or arbitrary sample weights are identified with this profile.",
    "provenanceKind": "adapted",
    "leanFormulation": "def ArithmeticMean (sample : _root_.Multiset ℝ) : Option ℝ :=\n  if sample.card = 0 then none else some (sample.sum / (sample.card : ℝ))",
    "formulationSource": "urn:csabs:source/local-lean-DescriptiveStatistics",
    "formulationLocator": "Catalog.ArithmeticMean",
    "formulationScope": "model",
    "leanModelMapping": "Multiset ℝ with exact sum and occurrence cardinality. ArithmeticMean returns Option ℝ; card=0 yields none before division, otherwise some(sum/card). The input quotient removes order but preserves multiplicity; no arithmetic rounding is modeled.",
    "leanModelLimitations": "Exact selected finite-multiset interface. No floating-point error analysis, missing-data handling, weighted/population inference, complexity claim or numerical implementation refinement. Only individually registered results have compiled witnesses; the separately recorded theorem is not a registered proof.",
    "specializationOf": [
      "urn:csabs:concept/PartialFunction"
    ],
    "specializationNote": "Instantiate the partial-function domain by Bag(ℝ) and codomain by ℝ. Definedness is exactly nonempty input; the total representation Bag(ℝ)→Option(ℝ) returns none on empty input and some(value) otherwise. The statistic has its own explicit defining rules; specialization does not transfer axioms."
  },
  {
    "id": "urn:csabs:operation/ArithmeticMean-evaluate",
    "type": "Operation",
    "name": "evaluate",
    "concept": "urn:csabs:concept/ArithmeticMean",
    "signature": "Bag(ℝ) → Option(ℝ)",
    "description": "Compute the exact finite-sample mean with explicit undefinedness.",
    "precondition": "A finite multiset of exact real observations.",
    "postcondition": "none exactly for S=∅; otherwise some((Σ_{x∈S}x)/|S|).",
    "totality": "total on the stated typed domain; Option represents mathematical undefinedness, not an arbitrary default value"
  },
  {
    "id": "urn:csabs:axiom/ArithmeticMean-definition",
    "type": "Axiom",
    "name": "definition",
    "statement": "The nonempty arithmetic mean divides the occurrence sum by the occurrence count; the empty result is undefined.",
    "formalStatement": "N=|S|; T=Σ_{x∈S}x; meanOption(S)=if N=0 then none else some(T/N); dom(μ)={S | |S|>0}.",
    "assumptions": [
      "Finite unweighted multiset of exact real observations, with repeated observations retained. N counts multiplicity; sum counts every occurrence. The mathematical mean requires N>0 and the model explicitly guards the totalized real division at zero. No NaNs, infinities, missing-value policy, rounding, overflow, weighted observations or probabilistic sampling assumptions are included."
    ],
    "appliesTo": [
      "urn:csabs:concept/ArithmeticMean"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Sourced mathematical definition; compilation status belongs to separate Lean evidence.",
    "source": [
      "urn:csabs:source/nist-measures-of-location"
    ],
    "sourceLocator": "NIST §1.3.5.1, Definition of Location, item 1 (mean formula)",
    "sourceNote": "Adapts the finite-sample arithmetic mean to an order-independent real multiset and an explicit Option encoding of empty-sample undefinedness. No population expectation, grouped-bin approximation, geometric/harmonic mean or arbitrary sample weights are identified with this profile.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/ArithmeticMean-singleton",
    "type": "Law",
    "name": "singleton",
    "statement": "A singleton sample has its sole value as mean.",
    "formalStatement": "μ({x})=x, equivalently meanOption({x})=some(x).",
    "assumptions": [
      "Finite unweighted multiset of exact real observations, with repeated observations retained. N counts multiplicity; sum counts every occurrence. The mathematical mean requires N>0 and the model explicitly guards the totalized real division at zero. No NaNs, infinities, missing-value policy, rounding, overflow, weighted observations or probabilistic sampling assumptions are included."
    ],
    "appliesTo": [
      "urn:csabs:concept/ArithmeticMean"
    ],
    "dependsOn": [
      "urn:csabs:axiom/ArithmeticMean-definition"
    ],
    "proofSketch": "The occurrence count is 1 and sum is x, so division gives x.",
    "ruleRole": "derived-result",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial mathematical statement; only separately mapped fresh Lean witnesses are compiler-verified.",
    "source": [
      "urn:csabs:source/nist-measures-of-location"
    ],
    "sourceLocator": "NIST §1.3.5.1, Definition of Location, item 1 (mean formula)",
    "sourceNote": "Derived from the linked finite-sample definition and exact count/order/arithmetic conventions. Adapts the finite-sample arithmetic mean to an order-independent real multiset and an explicit Option encoding of empty-sample undefinedness. No population expectation, grouped-bin approximation, geometric/harmonic mean or arbitrary sample weights are identified with this profile.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ (x : ℝ), Catalog.ArithmeticMean {x} = some x",
    "formulationSource": "urn:csabs:source/local-lean-DescriptiveStatistics",
    "formulationLocator": "Catalog.DescriptiveStatisticsProofs.mean_singleton",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Multiset ℝ with exact sum and occurrence cardinality. ArithmeticMean returns Option ℝ; card=0 yields none before division, otherwise some(sum/card). The input quotient removes order but preserves multiplicity; no arithmetic rounding is modeled.",
    "leanModelLimitations": "Proves the displayed result under the selected exact carrier/equality/empty/tie conventions. No proof of an arbitrary software implementation, population claim or numerical stability bound.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/ArithmeticMean-definition\": \"Interpreted by the explicit data guard/count/sort definition: N=|S|; T=Σ_{x∈S}x; meanOption(S)=if N=0 then none else some(T/N); dom(μ)={S | |S|>0}.\"}"
  },
  {
    "id": "urn:csabs:law/ArithmeticMean-balance",
    "type": "Law",
    "name": "balance",
    "statement": "Multiplying a defined mean by its occurrence count recovers the occurrence sum.",
    "formalStatement": "meanOption(S)=some(m) ⇒ |S|·m=Σ_{x∈S}x.",
    "assumptions": [
      "Finite unweighted multiset of exact real observations, with repeated observations retained. N counts multiplicity; sum counts every occurrence. The mathematical mean requires N>0 and the model explicitly guards the totalized real division at zero. No NaNs, infinities, missing-value policy, rounding, overflow, weighted observations or probabilistic sampling assumptions are included."
    ],
    "appliesTo": [
      "urn:csabs:concept/ArithmeticMean"
    ],
    "dependsOn": [
      "urn:csabs:axiom/ArithmeticMean-definition"
    ],
    "proofSketch": "A defined mean has N>0. Multiply m=T/N by nonzero N and cancel the denominator.",
    "ruleRole": "derived-result",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial mathematical statement; only separately mapped fresh Lean witnesses are compiler-verified.",
    "source": [
      "urn:csabs:source/nist-measures-of-location"
    ],
    "sourceLocator": "NIST §1.3.5.1, Definition of Location, item 1 (mean formula)",
    "sourceNote": "Derived from the linked finite-sample definition and exact count/order/arithmetic conventions. Adapts the finite-sample arithmetic mean to an order-independent real multiset and an explicit Option encoding of empty-sample undefinedness. No population expectation, grouped-bin approximation, geometric/harmonic mean or arbitrary sample weights are identified with this profile.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ (sample : Multiset ℝ) (m : ℝ), Catalog.ArithmeticMean sample = some m → (sample.card : ℝ) * m = sample.sum",
    "formulationSource": "urn:csabs:source/local-lean-DescriptiveStatistics",
    "formulationLocator": "Catalog.DescriptiveStatisticsProofs.mean_balance",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Multiset ℝ with exact sum and occurrence cardinality. ArithmeticMean returns Option ℝ; card=0 yields none before division, otherwise some(sum/card). The input quotient removes order but preserves multiplicity; no arithmetic rounding is modeled.",
    "leanModelLimitations": "Proves the displayed result under the selected exact carrier/equality/empty/tie conventions. No proof of an arbitrary software implementation, population claim or numerical stability bound.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/ArithmeticMean-definition\": \"Interpreted by the explicit data guard/count/sort definition: N=|S|; T=Σ_{x∈S}x; meanOption(S)=if N=0 then none else some(T/N); dom(μ)={S | |S|>0}.\"}"
  },
  {
    "id": "urn:csabs:theorem/ArithmeticMean-weighted-merge",
    "type": "Theorem",
    "name": "weighted-merge",
    "statement": "The mean of two nonempty bags is the size-weighted mean of their means.",
    "formalStatement": "For n=|S|>0 and k=|T|>0: μ(S⊎T)=(nμ(S)+kμ(T))/(n+k).",
    "assumptions": [
      "Finite unweighted multiset of exact real observations, with repeated observations retained. N counts multiplicity; sum counts every occurrence. The mathematical mean requires N>0 and the model explicitly guards the totalized real division at zero. No NaNs, infinities, missing-value policy, rounding, overflow, weighted observations or probabilistic sampling assumptions are included."
    ],
    "appliesTo": [
      "urn:csabs:concept/ArithmeticMean"
    ],
    "dependsOn": [
      "urn:csabs:axiom/ArithmeticMean-definition",
      "urn:csabs:operation/Multiset-union"
    ],
    "proofSketch": "Multiset union adds multiplicities, so its size is n+k and its sum is sum(S)+sum(T). Apply the mean definition and replace each sum by its cardinality times its mean. Averaging the two means without size weights is generally incorrect; equal sample sizes are sufficient for the simple midpoint formula.",
    "ruleRole": "derived-result",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial mathematical statement; only separately mapped fresh Lean witnesses are compiler-verified.",
    "source": [
      "urn:csabs:source/nist-measures-of-location"
    ],
    "sourceLocator": "NIST §1.3.5.1, Definition of Location, item 1 (mean formula)",
    "sourceNote": "Derived from the linked finite-sample definition and exact count/order/arithmetic conventions. Adapts the finite-sample arithmetic mean to an order-independent real multiset and an explicit Option encoding of empty-sample undefinedness. No population expectation, grouped-bin approximation, geometric/harmonic mean or arbitrary sample weights are identified with this profile.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
