# Numeric sample median (midpoint convention)

The central value of the sorted finite real sample, using the arithmetic midpoint of the two central order statistics for even sample size. It is undefined on empty data and need not be an observed value.

**Notation:** y₀≤⋯≤y_{N−1}; lo=⌊(N−1)/2⌋, hi=⌊N/2⌋; med(S)=(y_lo+y_hi)/2, N>0.

**Stable ID:** `urn:csabs:concept/Median`

**Categories:** Statistics → Descriptive statistics

**Kind:** Function

**Prerequisites:** [Multiset](Multiset.md), [Exact real number](RealNumber.md), [Partial function](PartialFunction.md)

**Specializes:** [Partial function](PartialFunction.md)

**Related concepts:** [Arithmetic mean of a finite real sample](ArithmeticMean.md), [Empirical mode set (all observed frequency maximizers)](Mode.md)

## Backlinks

- [Arithmetic mean of a finite real sample](ArithmeticMean.md) — `relatedConcept`
- [Empirical mode set (all observed frequency maximizers)](Mode.md) — `relatedConcept`
- [Multiset](Multiset.md) — `relatedConcept`

## Mathematical formulation

Sort the finite real multiset S, preserving repetitions, into y₀≤⋯≤y\_{N−1}. For N>0 define lo=⌊(N−1)/2⌋ and hi=⌊N/2⌋. The central pair is (y\_lo,y\_hi), and med(S)=(y\_lo+y\_hi)/2. If N=2k+1 this is y\_k; if N=2k>0 it is (y\_{k−1}+y\_k)/2. Both indices are in range. Centers and median are undefined for N=0 and are represented by none. This is a numeric midpoint statistic, distinct from choosing a lower/upper median or returning the entire median interval.

**Lean formulation** (in its source module context):

```lean
def Median (sample : _root_.Multiset ℝ) : Option ℝ :=
  (medianCenters sample).map fun p => (p.1 + p.2) / 2
```

**Source:** [`Catalog.Median`](../lean/Catalog/DescriptiveStatistics.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Multiset ℝ sorted with Multiset.sort (≤). medianCenters guards card=0 and uses proof-bounded Fin indices (card−1)/2 and card/2. Median maps the central pair to its exact arithmetic midpoint. Real comparisons/operations are noncomputable semantic interpretations, not a floating-point selection implementation.

**Limits:** Exact selected finite-multiset interface. No floating-point error analysis, missing-data handling, weighted/population inference, complexity claim or numerical implementation refinement. Only individually registered results have compiled witnesses; the separately recorded theorem is not a registered proof.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** The stated finite-multiset definition, explicit empty behavior and selected output convention. Finite multiset of exact real observations, with ordinary total order, exact real addition/division and multiset input equality. Repetitions are retained. N>0 is required by the partial center/median operations; total Option wrappers return none on empty input. Even sample size uses the arithmetic midpoint, which may not occur in S. Ordinal-only carriers, quantile interpolation conventions, NaNs, missing values and floating-point tolerances need separate profiles.

**basisKind:** defined-function

**basisScope:** Selected unweighted finite-sample statistic, not all weighted/population/rounded or interpolation conventions.

**convention:** Finite multiset of exact real observations, with ordinary total order, exact real addition/division and multiset input equality. Repetitions are retained. N>0 is required by the partial center/median operations; total Option wrappers return none on empty input. Even sample size uses the arithmetic midpoint, which may not occur in S. Ordinal-only carriers, quantile interpolation conventions, NaNs, missing values and floating-point tolerances need separate profiles.

**specializationNote:** Instantiate the partial-function domain by Bag(ℝ) and codomain by ℝ. Definedness is exactly nonempty input; the total representation Bag(ℝ)→Option(ℝ) returns none on empty input and some(value) otherwise. The statistic has its own explicit defining rules; specialization does not transfer axioms.

**verificationObligation:** Map multiplicity, equality, empty/missing-data policy, exact numeric semantics and tie/interpolation conventions to the target API. A compiled abstract identity is not implementation refinement.

**reviewStatus:** Sourced mathematical formulation with a separate Lean model and individually mapped witnesses.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-Median-centers"></a>

### centers

`urn:csabs:operation/Median-centers`

**signature:** Bag(ℝ) → Option(ℝ×ℝ)

**description:** Observe the lower and upper central order statistics.

**precondition:** A finite multiset of exact real observations.

**postcondition:** none for N=0; some(y_lo,y_hi) otherwise. The two values coincide in index for odd N.

**totality:** total on the stated typed domain; Option represents mathematical undefinedness, not an arbitrary default value

<a id="node-urn-csabs-operation-Median-evaluate"></a>

### evaluate

`urn:csabs:operation/Median-evaluate`

**signature:** Bag(ℝ) → Option(ℝ)

**description:** Compute the midpoint median of the exact numeric sample.

**precondition:** A finite multiset of exact real observations.

**postcondition:** none for empty input; some((y_lo+y_hi)/2) otherwise, with exact real division.

**totality:** total on the stated typed domain; Option represents mathematical undefinedness, not an arbitrary default value

## Axioms and defining rules

<a id="node-urn-csabs-axiom-Median-central-pair"></a>

### central-pair

`urn:csabs:axiom/Median-central-pair`

**statement:** For nonempty data, the two central indices select the lower and upper central order statistics.

**formalStatement:** sort(S)=(y₀,…,y_{N−1}); N>0 ⇒ centers(S)=(y_{⌊(N−1)/2⌋},y_{⌊N/2⌋}); centersOption(∅)=none.

**assumptions:** Finite multiset of exact real observations, with ordinary total order, exact real addition/division and multiset input equality. Repetitions are retained. N>0 is required by the partial center/median operations; total Option wrappers return none on empty input. Even sample size uses the arithmetic midpoint, which may not occur in S. Ordinal-only carriers, quantile interpolation conventions, NaNs, missing values and floating-point tolerances need separate profiles.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Sourced mathematical definition; compilation status belongs to separate Lean evidence.

**source:** [NIST/SEMATECH e-Handbook of Statistical Methods: §1.3.5.1 Measures of Location](https://www.itl.nist.gov/div898/handbook/eda/section3/eda351.htm); accessedOn: 2026-11-12; sourceRole: Consulted definitions of arithmetic mean, odd/even sample median and nonunique empirical modes; the catalog makes empty-data and tie conventions explicit.

**sourceLocator:** NIST §1.3.5.1, Definition of Location, item 2 (sorted odd/even median formulas)

**sourceNote:** Uses zero-based central indices to unify odd/even numeric medians. Adds finite-multiset equality, exact real arithmetic and explicit empty-data Option behavior. Sorting is a mathematical presentation; a selection algorithm may implement the same statistic without sorting the entire input. The midpoint convention is not assumed for arbitrary ordered nonnumeric data.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-Median-midpoint"></a>

### midpoint

`urn:csabs:axiom/Median-midpoint`

**statement:** The numeric median is the arithmetic midpoint of the central pair.

**formalStatement:** centersOption(S)=some(l,u) ⇒ medianOption(S)=some((l+u)/2); centersOption(S)=none ⇒ medianOption(S)=none.

**assumptions:** Finite multiset of exact real observations, with ordinary total order, exact real addition/division and multiset input equality. Repetitions are retained. N>0 is required by the partial center/median operations; total Option wrappers return none on empty input. Even sample size uses the arithmetic midpoint, which may not occur in S. Ordinal-only carriers, quantile interpolation conventions, NaNs, missing values and floating-point tolerances need separate profiles.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Sourced mathematical definition; compilation status belongs to separate Lean evidence.

**source:** [NIST/SEMATECH e-Handbook of Statistical Methods: §1.3.5.1 Measures of Location](https://www.itl.nist.gov/div898/handbook/eda/section3/eda351.htm); accessedOn: 2026-11-12; sourceRole: Consulted definitions of arithmetic mean, odd/even sample median and nonunique empirical modes; the catalog makes empty-data and tie conventions explicit.

**sourceLocator:** NIST §1.3.5.1, Definition of Location, item 2 (sorted odd/even median formulas)

**sourceNote:** Uses zero-based central indices to unify odd/even numeric medians. Adds finite-multiset equality, exact real arithmetic and explicit empty-data Option behavior. Sorting is a mathematical presentation; a selection algorithm may implement the same statistic without sorting the entire input. The midpoint convention is not assumed for arbitrary ordered nonnumeric data.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-Median-singleton"></a>

### singleton

`urn:csabs:law/Median-singleton`

**statement:** A singleton sample has its sole value as median.

**formalStatement:** med({x})=x, equivalently medianOption({x})=some(x).

**assumptions:** Finite multiset of exact real observations, with ordinary total order, exact real addition/division and multiset input equality. Repetitions are retained. N>0 is required by the partial center/median operations; total Option wrappers return none on empty input. Even sample size uses the arithmetic midpoint, which may not occur in S. Ordinal-only carriers, quantile interpolation conventions, NaNs, missing values and floating-point tolerances need separate profiles.

**dependsOn:** [central-pair](Median.md#node-urn-csabs-axiom-Median-central-pair); [midpoint](Median.md#node-urn-csabs-axiom-Median-midpoint)

**proofSketch:** The sorted list has one entry and both central indices are 0; its midpoint with itself is x.

**ruleRole:** derived-result

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial mathematical statement; only separately mapped fresh Lean witnesses are compiler-verified.

**source:** [NIST/SEMATECH e-Handbook of Statistical Methods: §1.3.5.1 Measures of Location](https://www.itl.nist.gov/div898/handbook/eda/section3/eda351.htm); accessedOn: 2026-11-12; sourceRole: Consulted definitions of arithmetic mean, odd/even sample median and nonunique empirical modes; the catalog makes empty-data and tie conventions explicit.

**sourceLocator:** NIST §1.3.5.1, Definition of Location, item 2 (sorted odd/even median formulas)

**sourceNote:** Derived from the linked finite-sample definition and exact count/order/arithmetic conventions. Uses zero-based central indices to unify odd/even numeric medians. Adds finite-multiset equality, exact real arithmetic and explicit empty-data Option behavior. Sorting is a mathematical presentation; a selection algorithm may implement the same statistic without sorting the entire input. The midpoint convention is not assumed for arbitrary ordered nonnumeric data.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ (x : ℝ), Catalog.Median {x} = some x
```

**Source:** [`Catalog.DescriptiveStatisticsProofs.median_singleton`](../lean/Catalog/DescriptiveStatistics.lean); consulted 2026-11-12.

**Scope:** registered-witness-type

**Interpretation:** Multiset ℝ sorted with Multiset.sort (≤). medianCenters guards card=0 and uses proof-bounded Fin indices (card−1)/2 and card/2. Median maps the central pair to its exact arithmetic midpoint. Real comparisons/operations are noncomputable semantic interpretations, not a floating-point selection implementation.

**Limits:** Proves the displayed result under the selected exact carrier/equality/empty/tie conventions. No proof of an arbitrary software implementation, population claim or numerical stability bound.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/Median-central-pair": "Interpreted by the explicit data guard/count/sort definition: sort(S)=(y₀,…,y_{N−1}); N>0 ⇒ centers(S)=(y_{⌊(N−1)/2⌋},y_{⌊N/2⌋}); centersOption(∅)=none.",
  "urn:csabs:axiom/Median-midpoint": "Interpreted by the explicit data guard/count/sort definition: centersOption(S)=some(l,u) ⇒ medianOption(S)=some((l+u)/2); centersOption(S)=none ⇒ medianOption(S)=none."
}
```

<a id="node-urn-csabs-law-Median-pair"></a>

### pair

`urn:csabs:law/Median-pair`

**statement:** A two-observation sample has the arithmetic midpoint as median, including repeated observations.

**formalStatement:** med({a,b})=(a+b)/2, equivalently medianOption({a,b})=some((a+b)/2).

**assumptions:** Finite multiset of exact real observations, with ordinary total order, exact real addition/division and multiset input equality. Repetitions are retained. N>0 is required by the partial center/median operations; total Option wrappers return none on empty input. Even sample size uses the arithmetic midpoint, which may not occur in S. Ordinal-only carriers, quantile interpolation conventions, NaNs, missing values and floating-point tolerances need separate profiles.

**dependsOn:** [central-pair](Median.md#node-urn-csabs-axiom-Median-central-pair); [midpoint](Median.md#node-urn-csabs-axiom-Median-midpoint)

**proofSketch:** Sort the two values by their real order. The central indices are 0 and 1; swapping their order leaves a+b unchanged. Multiset braces retain both occurrences even if a=b.

**ruleRole:** derived-result

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial mathematical statement; only separately mapped fresh Lean witnesses are compiler-verified.

**source:** [NIST/SEMATECH e-Handbook of Statistical Methods: §1.3.5.1 Measures of Location](https://www.itl.nist.gov/div898/handbook/eda/section3/eda351.htm); accessedOn: 2026-11-12; sourceRole: Consulted definitions of arithmetic mean, odd/even sample median and nonunique empirical modes; the catalog makes empty-data and tie conventions explicit.

**sourceLocator:** NIST §1.3.5.1, Definition of Location, item 2 (sorted odd/even median formulas)

**sourceNote:** Derived from the linked finite-sample definition and exact count/order/arithmetic conventions. Uses zero-based central indices to unify odd/even numeric medians. Adds finite-multiset equality, exact real arithmetic and explicit empty-data Option behavior. Sorting is a mathematical presentation; a selection algorithm may implement the same statistic without sorting the entire input. The midpoint convention is not assumed for arbitrary ordered nonnumeric data.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ (a b : ℝ), Catalog.Median ({a, b} : Multiset ℝ) = some ((a + b) / 2)
```

**Source:** [`Catalog.DescriptiveStatisticsProofs.median_pair`](../lean/Catalog/DescriptiveStatistics.lean); consulted 2026-11-12.

**Scope:** registered-witness-type

**Interpretation:** Multiset ℝ sorted with Multiset.sort (≤). medianCenters guards card=0 and uses proof-bounded Fin indices (card−1)/2 and card/2. Median maps the central pair to its exact arithmetic midpoint. Real comparisons/operations are noncomputable semantic interpretations, not a floating-point selection implementation.

**Limits:** Proves the displayed result under the selected exact carrier/equality/empty/tie conventions. No proof of an arbitrary software implementation, population claim or numerical stability bound.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/Median-central-pair": "Interpreted by the explicit data guard/count/sort definition: sort(S)=(y₀,…,y_{N−1}); N>0 ⇒ centers(S)=(y_{⌊(N−1)/2⌋},y_{⌊N/2⌋}); centersOption(∅)=none.",
  "urn:csabs:axiom/Median-midpoint": "Interpreted by the explicit data guard/count/sort definition: centersOption(S)=some(l,u) ⇒ medianOption(S)=some((l+u)/2); centersOption(S)=none ⇒ medianOption(S)=none."
}
```

## Theorems

<a id="node-urn-csabs-theorem-Median-central-bounds"></a>

### central-bounds

`urn:csabs:theorem/Median-central-bounds`

**statement:** The midpoint median lies between its two central order statistics.

**formalStatement:** For N>0, y_lo≤med(S)≤y_hi, where lo=⌊(N−1)/2⌋ and hi=⌊N/2⌋.

**assumptions:** Finite multiset of exact real observations, with ordinary total order, exact real addition/division and multiset input equality. Repetitions are retained. N>0 is required by the partial center/median operations; total Option wrappers return none on empty input. Even sample size uses the arithmetic midpoint, which may not occur in S. Ordinal-only carriers, quantile interpolation conventions, NaNs, missing values and floating-point tolerances need separate profiles.

**dependsOn:** [central-pair](Median.md#node-urn-csabs-axiom-Median-central-pair); [midpoint](Median.md#node-urn-csabs-axiom-Median-midpoint)

**proofSketch:** The central indices satisfy lo≤hi, so sorting gives l=y_lo≤u=y_hi. Add the inequalities l≤u to obtain 2l≤l+u≤2u and divide by the positive real number 2. In particular an even-sample median need not be one of the observations.

**ruleRole:** derived-result

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial mathematical statement; only separately mapped fresh Lean witnesses are compiler-verified.

**source:** [NIST/SEMATECH e-Handbook of Statistical Methods: §1.3.5.1 Measures of Location](https://www.itl.nist.gov/div898/handbook/eda/section3/eda351.htm); accessedOn: 2026-11-12; sourceRole: Consulted definitions of arithmetic mean, odd/even sample median and nonunique empirical modes; the catalog makes empty-data and tie conventions explicit.

**sourceLocator:** NIST §1.3.5.1, Definition of Location, item 2 (sorted odd/even median formulas)

**sourceNote:** Derived from the linked finite-sample definition and exact count/order/arithmetic conventions. Uses zero-based central indices to unify odd/even numeric medians. Adds finite-multiset equality, exact real arithmetic and explicit empty-data Option behavior. Sorting is a mathematical presentation; a selection algorithm may implement the same statistic without sorting the entire input. The midpoint convention is not assumed for arbitrary ordered nonnumeric data.

**provenanceKind:** derived

## Concept provenance

- [NIST/SEMATECH e-Handbook of Statistical Methods: §1.3.5.1 Measures of Location](https://www.itl.nist.gov/div898/handbook/eda/section3/eda351.htm); accessedOn: 2026-11-12; sourceRole: Consulted definitions of arithmetic mean, odd/even sample median and nonunique empirical modes; the catalog makes empty-data and tie conventions explicit.

**sourceLocator:** NIST §1.3.5.1, Definition of Location, item 2 (sorted odd/even median formulas)

**sourceNote:** Uses zero-based central indices to unify odd/even numeric medians. Adds finite-multiset equality, exact real arithmetic and explicit empty-data Option behavior. Sorting is a mathematical presentation; a selection algorithm may implement the same statistic without sorting the entire input. The midpoint convention is not assumed for arbitrary ordered nonnumeric data.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/Median",
    "type": "Concept",
    "shortForm": "Median",
    "fullName": "Numeric sample median (midpoint convention)",
    "synonyms": [
      "sample median",
      "50th percentile (selected sample convention)",
      "midpoint median"
    ],
    "category": [
      "urn:csabs:category/descriptive-statistics"
    ],
    "kind": "urn:csabs:kind/function",
    "definition": "The central value of the sorted finite real sample, using the arithmetic midpoint of the two central order statistics for even sample size. It is undefined on empty data and need not be an observed value.",
    "notation": "y₀≤⋯≤y_{N−1}; lo=⌊(N−1)/2⌋, hi=⌊N/2⌋; med(S)=(y_lo+y_hi)/2, N>0.",
    "mathematicalFormulation": "Sort the finite real multiset S, preserving repetitions, into y₀≤⋯≤y_{N−1}. For N>0 define lo=⌊(N−1)/2⌋ and hi=⌊N/2⌋. The central pair is (y_lo,y_hi), and med(S)=(y_lo+y_hi)/2. If N=2k+1 this is y_k; if N=2k>0 it is (y_{k−1}+y_k)/2. Both indices are in range. Centers and median are undefined for N=0 and are represented by none. This is a numeric midpoint statistic, distinct from choosing a lower/upper median or returning the entire median interval.",
    "hasOperation": [
      "urn:csabs:operation/Median-centers",
      "urn:csabs:operation/Median-evaluate"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/Median-central-pair",
      "urn:csabs:axiom/Median-midpoint"
    ],
    "hasLaw": [
      "urn:csabs:law/Median-singleton",
      "urn:csabs:law/Median-pair"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/Median-central-bounds"
    ],
    "requiresConcept": [
      "urn:csabs:concept/Multiset",
      "urn:csabs:concept/RealNumber",
      "urn:csabs:concept/PartialFunction"
    ],
    "relatedConcept": [
      "urn:csabs:concept/ArithmeticMean",
      "urn:csabs:concept/Mode"
    ],
    "axiomBasis": "The stated finite-multiset definition, explicit empty behavior and selected output convention. Finite multiset of exact real observations, with ordinary total order, exact real addition/division and multiset input equality. Repetitions are retained. N>0 is required by the partial center/median operations; total Option wrappers return none on empty input. Even sample size uses the arithmetic midpoint, which may not occur in S. Ordinal-only carriers, quantile interpolation conventions, NaNs, missing values and floating-point tolerances need separate profiles.",
    "basisKind": "defined-function",
    "basisScope": "Selected unweighted finite-sample statistic, not all weighted/population/rounded or interpolation conventions.",
    "convention": "Finite multiset of exact real observations, with ordinary total order, exact real addition/division and multiset input equality. Repetitions are retained. N>0 is required by the partial center/median operations; total Option wrappers return none on empty input. Even sample size uses the arithmetic midpoint, which may not occur in S. Ordinal-only carriers, quantile interpolation conventions, NaNs, missing values and floating-point tolerances need separate profiles.",
    "coverageStatus": "basis-reviewed",
    "verificationObligation": "Map multiplicity, equality, empty/missing-data policy, exact numeric semantics and tie/interpolation conventions to the target API. A compiled abstract identity is not implementation refinement.",
    "reviewStatus": "Sourced mathematical formulation with a separate Lean model and individually mapped witnesses.",
    "source": [
      "urn:csabs:source/nist-measures-of-location"
    ],
    "sourceLocator": "NIST §1.3.5.1, Definition of Location, item 2 (sorted odd/even median formulas)",
    "sourceNote": "Uses zero-based central indices to unify odd/even numeric medians. Adds finite-multiset equality, exact real arithmetic and explicit empty-data Option behavior. Sorting is a mathematical presentation; a selection algorithm may implement the same statistic without sorting the entire input. The midpoint convention is not assumed for arbitrary ordered nonnumeric data.",
    "provenanceKind": "adapted",
    "leanFormulation": "def Median (sample : _root_.Multiset ℝ) : Option ℝ :=\n  (medianCenters sample).map fun p => (p.1 + p.2) / 2",
    "formulationSource": "urn:csabs:source/local-lean-DescriptiveStatistics",
    "formulationLocator": "Catalog.Median",
    "formulationScope": "model",
    "leanModelMapping": "Multiset ℝ sorted with Multiset.sort (≤). medianCenters guards card=0 and uses proof-bounded Fin indices (card−1)/2 and card/2. Median maps the central pair to its exact arithmetic midpoint. Real comparisons/operations are noncomputable semantic interpretations, not a floating-point selection implementation.",
    "leanModelLimitations": "Exact selected finite-multiset interface. No floating-point error analysis, missing-data handling, weighted/population inference, complexity claim or numerical implementation refinement. Only individually registered results have compiled witnesses; the separately recorded theorem is not a registered proof.",
    "specializationOf": [
      "urn:csabs:concept/PartialFunction"
    ],
    "specializationNote": "Instantiate the partial-function domain by Bag(ℝ) and codomain by ℝ. Definedness is exactly nonempty input; the total representation Bag(ℝ)→Option(ℝ) returns none on empty input and some(value) otherwise. The statistic has its own explicit defining rules; specialization does not transfer axioms."
  },
  {
    "id": "urn:csabs:operation/Median-centers",
    "type": "Operation",
    "name": "centers",
    "concept": "urn:csabs:concept/Median",
    "signature": "Bag(ℝ) → Option(ℝ×ℝ)",
    "description": "Observe the lower and upper central order statistics.",
    "precondition": "A finite multiset of exact real observations.",
    "postcondition": "none for N=0; some(y_lo,y_hi) otherwise. The two values coincide in index for odd N.",
    "totality": "total on the stated typed domain; Option represents mathematical undefinedness, not an arbitrary default value"
  },
  {
    "id": "urn:csabs:operation/Median-evaluate",
    "type": "Operation",
    "name": "evaluate",
    "concept": "urn:csabs:concept/Median",
    "signature": "Bag(ℝ) → Option(ℝ)",
    "description": "Compute the midpoint median of the exact numeric sample.",
    "precondition": "A finite multiset of exact real observations.",
    "postcondition": "none for empty input; some((y_lo+y_hi)/2) otherwise, with exact real division.",
    "totality": "total on the stated typed domain; Option represents mathematical undefinedness, not an arbitrary default value"
  },
  {
    "id": "urn:csabs:axiom/Median-central-pair",
    "type": "Axiom",
    "name": "central-pair",
    "statement": "For nonempty data, the two central indices select the lower and upper central order statistics.",
    "formalStatement": "sort(S)=(y₀,…,y_{N−1}); N>0 ⇒ centers(S)=(y_{⌊(N−1)/2⌋},y_{⌊N/2⌋}); centersOption(∅)=none.",
    "assumptions": [
      "Finite multiset of exact real observations, with ordinary total order, exact real addition/division and multiset input equality. Repetitions are retained. N>0 is required by the partial center/median operations; total Option wrappers return none on empty input. Even sample size uses the arithmetic midpoint, which may not occur in S. Ordinal-only carriers, quantile interpolation conventions, NaNs, missing values and floating-point tolerances need separate profiles."
    ],
    "appliesTo": [
      "urn:csabs:concept/Median"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Sourced mathematical definition; compilation status belongs to separate Lean evidence.",
    "source": [
      "urn:csabs:source/nist-measures-of-location"
    ],
    "sourceLocator": "NIST §1.3.5.1, Definition of Location, item 2 (sorted odd/even median formulas)",
    "sourceNote": "Uses zero-based central indices to unify odd/even numeric medians. Adds finite-multiset equality, exact real arithmetic and explicit empty-data Option behavior. Sorting is a mathematical presentation; a selection algorithm may implement the same statistic without sorting the entire input. The midpoint convention is not assumed for arbitrary ordered nonnumeric data.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/Median-midpoint",
    "type": "Axiom",
    "name": "midpoint",
    "statement": "The numeric median is the arithmetic midpoint of the central pair.",
    "formalStatement": "centersOption(S)=some(l,u) ⇒ medianOption(S)=some((l+u)/2); centersOption(S)=none ⇒ medianOption(S)=none.",
    "assumptions": [
      "Finite multiset of exact real observations, with ordinary total order, exact real addition/division and multiset input equality. Repetitions are retained. N>0 is required by the partial center/median operations; total Option wrappers return none on empty input. Even sample size uses the arithmetic midpoint, which may not occur in S. Ordinal-only carriers, quantile interpolation conventions, NaNs, missing values and floating-point tolerances need separate profiles."
    ],
    "appliesTo": [
      "urn:csabs:concept/Median"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Sourced mathematical definition; compilation status belongs to separate Lean evidence.",
    "source": [
      "urn:csabs:source/nist-measures-of-location"
    ],
    "sourceLocator": "NIST §1.3.5.1, Definition of Location, item 2 (sorted odd/even median formulas)",
    "sourceNote": "Uses zero-based central indices to unify odd/even numeric medians. Adds finite-multiset equality, exact real arithmetic and explicit empty-data Option behavior. Sorting is a mathematical presentation; a selection algorithm may implement the same statistic without sorting the entire input. The midpoint convention is not assumed for arbitrary ordered nonnumeric data.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/Median-singleton",
    "type": "Law",
    "name": "singleton",
    "statement": "A singleton sample has its sole value as median.",
    "formalStatement": "med({x})=x, equivalently medianOption({x})=some(x).",
    "assumptions": [
      "Finite multiset of exact real observations, with ordinary total order, exact real addition/division and multiset input equality. Repetitions are retained. N>0 is required by the partial center/median operations; total Option wrappers return none on empty input. Even sample size uses the arithmetic midpoint, which may not occur in S. Ordinal-only carriers, quantile interpolation conventions, NaNs, missing values and floating-point tolerances need separate profiles."
    ],
    "appliesTo": [
      "urn:csabs:concept/Median"
    ],
    "dependsOn": [
      "urn:csabs:axiom/Median-central-pair",
      "urn:csabs:axiom/Median-midpoint"
    ],
    "proofSketch": "The sorted list has one entry and both central indices are 0; its midpoint with itself is x.",
    "ruleRole": "derived-result",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial mathematical statement; only separately mapped fresh Lean witnesses are compiler-verified.",
    "source": [
      "urn:csabs:source/nist-measures-of-location"
    ],
    "sourceLocator": "NIST §1.3.5.1, Definition of Location, item 2 (sorted odd/even median formulas)",
    "sourceNote": "Derived from the linked finite-sample definition and exact count/order/arithmetic conventions. Uses zero-based central indices to unify odd/even numeric medians. Adds finite-multiset equality, exact real arithmetic and explicit empty-data Option behavior. Sorting is a mathematical presentation; a selection algorithm may implement the same statistic without sorting the entire input. The midpoint convention is not assumed for arbitrary ordered nonnumeric data.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ (x : ℝ), Catalog.Median {x} = some x",
    "formulationSource": "urn:csabs:source/local-lean-DescriptiveStatistics",
    "formulationLocator": "Catalog.DescriptiveStatisticsProofs.median_singleton",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Multiset ℝ sorted with Multiset.sort (≤). medianCenters guards card=0 and uses proof-bounded Fin indices (card−1)/2 and card/2. Median maps the central pair to its exact arithmetic midpoint. Real comparisons/operations are noncomputable semantic interpretations, not a floating-point selection implementation.",
    "leanModelLimitations": "Proves the displayed result under the selected exact carrier/equality/empty/tie conventions. No proof of an arbitrary software implementation, population claim or numerical stability bound.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/Median-central-pair\": \"Interpreted by the explicit data guard/count/sort definition: sort(S)=(y₀,…,y_{N−1}); N>0 ⇒ centers(S)=(y_{⌊(N−1)/2⌋},y_{⌊N/2⌋}); centersOption(∅)=none.\", \"urn:csabs:axiom/Median-midpoint\": \"Interpreted by the explicit data guard/count/sort definition: centersOption(S)=some(l,u) ⇒ medianOption(S)=some((l+u)/2); centersOption(S)=none ⇒ medianOption(S)=none.\"}"
  },
  {
    "id": "urn:csabs:law/Median-pair",
    "type": "Law",
    "name": "pair",
    "statement": "A two-observation sample has the arithmetic midpoint as median, including repeated observations.",
    "formalStatement": "med({a,b})=(a+b)/2, equivalently medianOption({a,b})=some((a+b)/2).",
    "assumptions": [
      "Finite multiset of exact real observations, with ordinary total order, exact real addition/division and multiset input equality. Repetitions are retained. N>0 is required by the partial center/median operations; total Option wrappers return none on empty input. Even sample size uses the arithmetic midpoint, which may not occur in S. Ordinal-only carriers, quantile interpolation conventions, NaNs, missing values and floating-point tolerances need separate profiles."
    ],
    "appliesTo": [
      "urn:csabs:concept/Median"
    ],
    "dependsOn": [
      "urn:csabs:axiom/Median-central-pair",
      "urn:csabs:axiom/Median-midpoint"
    ],
    "proofSketch": "Sort the two values by their real order. The central indices are 0 and 1; swapping their order leaves a+b unchanged. Multiset braces retain both occurrences even if a=b.",
    "ruleRole": "derived-result",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial mathematical statement; only separately mapped fresh Lean witnesses are compiler-verified.",
    "source": [
      "urn:csabs:source/nist-measures-of-location"
    ],
    "sourceLocator": "NIST §1.3.5.1, Definition of Location, item 2 (sorted odd/even median formulas)",
    "sourceNote": "Derived from the linked finite-sample definition and exact count/order/arithmetic conventions. Uses zero-based central indices to unify odd/even numeric medians. Adds finite-multiset equality, exact real arithmetic and explicit empty-data Option behavior. Sorting is a mathematical presentation; a selection algorithm may implement the same statistic without sorting the entire input. The midpoint convention is not assumed for arbitrary ordered nonnumeric data.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ (a b : ℝ), Catalog.Median ({a, b} : Multiset ℝ) = some ((a + b) / 2)",
    "formulationSource": "urn:csabs:source/local-lean-DescriptiveStatistics",
    "formulationLocator": "Catalog.DescriptiveStatisticsProofs.median_pair",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Multiset ℝ sorted with Multiset.sort (≤). medianCenters guards card=0 and uses proof-bounded Fin indices (card−1)/2 and card/2. Median maps the central pair to its exact arithmetic midpoint. Real comparisons/operations are noncomputable semantic interpretations, not a floating-point selection implementation.",
    "leanModelLimitations": "Proves the displayed result under the selected exact carrier/equality/empty/tie conventions. No proof of an arbitrary software implementation, population claim or numerical stability bound.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/Median-central-pair\": \"Interpreted by the explicit data guard/count/sort definition: sort(S)=(y₀,…,y_{N−1}); N>0 ⇒ centers(S)=(y_{⌊(N−1)/2⌋},y_{⌊N/2⌋}); centersOption(∅)=none.\", \"urn:csabs:axiom/Median-midpoint\": \"Interpreted by the explicit data guard/count/sort definition: centersOption(S)=some(l,u) ⇒ medianOption(S)=some((l+u)/2); centersOption(S)=none ⇒ medianOption(S)=none.\"}"
  },
  {
    "id": "urn:csabs:theorem/Median-central-bounds",
    "type": "Theorem",
    "name": "central-bounds",
    "statement": "The midpoint median lies between its two central order statistics.",
    "formalStatement": "For N>0, y_lo≤med(S)≤y_hi, where lo=⌊(N−1)/2⌋ and hi=⌊N/2⌋.",
    "assumptions": [
      "Finite multiset of exact real observations, with ordinary total order, exact real addition/division and multiset input equality. Repetitions are retained. N>0 is required by the partial center/median operations; total Option wrappers return none on empty input. Even sample size uses the arithmetic midpoint, which may not occur in S. Ordinal-only carriers, quantile interpolation conventions, NaNs, missing values and floating-point tolerances need separate profiles."
    ],
    "appliesTo": [
      "urn:csabs:concept/Median"
    ],
    "dependsOn": [
      "urn:csabs:axiom/Median-central-pair",
      "urn:csabs:axiom/Median-midpoint"
    ],
    "proofSketch": "The central indices satisfy lo≤hi, so sorting gives l=y_lo≤u=y_hi. Add the inequalities l≤u to obtain 2l≤l+u≤2u and divide by the positive real number 2. In particular an even-sample median need not be one of the observations.",
    "ruleRole": "derived-result",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial mathematical statement; only separately mapped fresh Lean witnesses are compiler-verified.",
    "source": [
      "urn:csabs:source/nist-measures-of-location"
    ],
    "sourceLocator": "NIST §1.3.5.1, Definition of Location, item 2 (sorted odd/even median formulas)",
    "sourceNote": "Derived from the linked finite-sample definition and exact count/order/arithmetic conventions. Uses zero-based central indices to unify odd/even numeric medians. Adds finite-multiset equality, exact real arithmetic and explicit empty-data Option behavior. Sorting is a mathematical presentation; a selection algorithm may implement the same statistic without sorting the entire input. The midpoint convention is not assumed for arbitrary ordered nonnumeric data.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
