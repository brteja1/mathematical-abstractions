# Empirical mode set (all observed frequency maximizers)

The finite set of observed values with maximal occurrence count in a finite multiset. Every tied maximizer is retained, including all observed values when their counts are all equal. It applies to categorical as well as numeric observations.

**Notation:** M(S)={a∈supp(S) | ∀b∈supp(S),c_S(b)≤c_S(a)}; M(∅)=∅.

**Stable ID:** `urn:csabs:concept/Mode`

**Categories:** Statistics → Descriptive statistics

**Kind:** Function

**Prerequisites:** [Multiset](Multiset.md), [Finite set collection](FiniteSet.md), [Total function](Function.md)

**Specializes:** [Total function](Function.md)

**Related concepts:** [Arithmetic mean of a finite real sample](ArithmeticMean.md), [Numeric sample median (midpoint convention)](Median.md), [Finitely supported probability distribution](FiniteDistribution.md)

## Backlinks

- [Arithmetic mean of a finite real sample](ArithmeticMean.md) — `relatedConcept`
- [Finitely supported probability distribution](FiniteDistribution.md) — `relatedConcept`
- [Numeric sample median (midpoint convention)](Median.md) — `relatedConcept`
- [Multiset](Multiset.md) — `relatedConcept`

## Mathematical formulation

For a finite multiset S on a carrier A with genuine equality, let c\_S(a)∈ℕ be its occurrence count and supp(S)={a | c\_S(a)>0}. Define M(S)={a∈supp(S) | ∀b∈supp(S),c\_S(b)≤c\_S(a)}. The output is a finite set, not a chosen representative. M(∅)=∅; every nonempty finite sample has at least one maximizer. All ties are included, so if every observation is distinct, M(S)=supp(S). Conventions declaring no mode for all-distinct/uniform samples, or selecting one tie winner, are different variants. No arithmetic or ordering on A is needed.

**Lean formulation** (in its source module context):

```lean
def Mode {A : Type u} [DecidableEq A] (sample : _root_.Multiset A) : Finset A := by
  classical
  exact sample.toFinset.filter (fun a => ∀ b ∈ sample, sample.count b ≤ sample.count a)
```

**Source:** [`Catalog.Mode`](../lean/Catalog/DescriptiveStatistics.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** For A with DecidableEq, Mode filters sample.toFinset by the universal maximum-count condition over observed sample values. Output is Finset A, with every tied maximizer retained and no ordering assumption on A. The semantic definition uses classical decidability for the bounded predicate; it is not a claimed efficient frequency-table implementation.

**Limits:** Exact selected finite-multiset interface. No floating-point error analysis, missing-data handling, weighted/population inference, complexity claim or numerical implementation refinement. Only individually registered results have compiled witnesses; the separately recorded theorem is not a registered proof.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** The stated finite-multiset definition, explicit empty behavior and selected output convention. Finite multiset of observations on a carrier A with an equality relation; the Lean count/filter interface requires DecidableEq A. Counts include repetitions and input order is irrelevant. Output equality is extensional finite-set equality. Only observed values are candidates, so empty input returns the empty set instead of treating all unobserved count-zero values as modes. All tied maxima are returned; there is no no-repetition threshold, tie-break order, histogram binning, kernel density, population-density mode or NaN equivalence policy.

**basisKind:** defined-function

**basisScope:** Selected unweighted finite-sample statistic, not all weighted/population/rounded or interpolation conventions.

**convention:** Finite multiset of observations on a carrier A with an equality relation; the Lean count/filter interface requires DecidableEq A. Counts include repetitions and input order is irrelevant. Output equality is extensional finite-set equality. Only observed values are candidates, so empty input returns the empty set instead of treating all unobserved count-zero values as modes. All tied maxima are returned; there is no no-repetition threshold, tie-break order, histogram binning, kernel density, population-density mode or NaN equivalence policy.

**specializationNote:** Instantiate the total-function domain by Bag(A) and codomain by FinSet(A). Returning the entire frequency-maximizer set makes the result deterministic even when several values tie; it does not choose a single modal observation.

**verificationObligation:** Map multiplicity, equality, empty/missing-data policy, exact numeric semantics and tie/interpolation conventions to the target API. A compiled abstract identity is not implementation refinement.

**reviewStatus:** Sourced mathematical formulation with a separate Lean model and individually mapped witnesses.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-Mode-evaluate"></a>

### evaluate

`urn:csabs:operation/Mode-evaluate`

**signature:** Bag(A) → FinSet(A); S ↦ M(S)

**description:** Return every observed value whose occurrence count is maximal.

**precondition:** Finite multiset with equality on A; no numeric values or order are required.

**postcondition:** The full maximizer set, empty exactly for empty input under this profile.

**totality:** total on the stated typed domain; Option represents mathematical undefinedness, not an arbitrary default value

<a id="node-urn-csabs-operation-Mode-isMode"></a>

### isMode

`urn:csabs:operation/Mode-isMode`

**signature:** Bag(A)×A → Prop; (S,a) ↦ [a∈M(S)]

**description:** Test membership in the empirical mode relation.

**precondition:** Same value carrier and equality policy.

**postcondition:** True exactly for observed maximum-count values; false for all a when S is empty.

**totality:** total on the stated typed domain; Option represents mathematical undefinedness, not an arbitrary default value

## Axioms and defining rules

<a id="node-urn-csabs-axiom-Mode-maximizer-set"></a>

### maximizer-set

`urn:csabs:axiom/Mode-maximizer-set`

**statement:** Modes are exactly observed frequency maximizers, retaining all ties.

**formalStatement:** M(S)={a∈supp(S) | ∀b∈supp(S),c_S(b)≤c_S(a)}; supp(S)={a | c_S(a)>0}; M(∅)=∅.

**assumptions:** Finite multiset of observations on a carrier A with an equality relation; the Lean count/filter interface requires DecidableEq A. Counts include repetitions and input order is irrelevant. Output equality is extensional finite-set equality. Only observed values are candidates, so empty input returns the empty set instead of treating all unobserved count-zero values as modes. All tied maxima are returned; there is no no-repetition threshold, tie-break order, histogram binning, kernel density, population-density mode or NaN equivalence policy.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Sourced mathematical definition; compilation status belongs to separate Lean evidence.

**source:** [NIST/SEMATECH e-Handbook of Statistical Methods: §1.3.5.1 Measures of Location](https://www.itl.nist.gov/div898/handbook/eda/section3/eda351.htm); accessedOn: 2026-11-12; sourceRole: Consulted definitions of arithmetic mean, odd/even sample median and nonunique empirical modes; the catalog makes empty-data and tie conventions explicit.

**sourceLocator:** NIST §1.3.5.1, Definition of Location, item 3 and the following continuous-data caveat

**sourceNote:** Adapts greatest observed frequency and nonuniqueness to an explicit finite argmax set. Chooses inclusion of all equal-frequency/all-distinct observations and empty output on an empty sample; these policies are stated rather than inferred from the word mode. Generalizes frequency counting to categorical carriers; excludes the source’s separate histogram midpoint approximation.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-Mode-singleton"></a>

### singleton

`urn:csabs:law/Mode-singleton`

**statement:** The only value in a singleton sample is its sole mode.

**formalStatement:** M({x})={x}.

**assumptions:** Finite multiset of observations on a carrier A with an equality relation; the Lean count/filter interface requires DecidableEq A. Counts include repetitions and input order is irrelevant. Output equality is extensional finite-set equality. Only observed values are candidates, so empty input returns the empty set instead of treating all unobserved count-zero values as modes. All tied maxima are returned; there is no no-repetition threshold, tie-break order, histogram binning, kernel density, population-density mode or NaN equivalence policy.

**dependsOn:** [maximizer-set](Mode.md#node-urn-csabs-axiom-Mode-maximizer-set)

**proofSketch:** The support is {x}, whose count is 1; the only required count comparison is reflexive.

**ruleRole:** derived-result

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial mathematical statement; only separately mapped fresh Lean witnesses are compiler-verified.

**source:** [NIST/SEMATECH e-Handbook of Statistical Methods: §1.3.5.1 Measures of Location](https://www.itl.nist.gov/div898/handbook/eda/section3/eda351.htm); accessedOn: 2026-11-12; sourceRole: Consulted definitions of arithmetic mean, odd/even sample median and nonunique empirical modes; the catalog makes empty-data and tie conventions explicit.

**sourceLocator:** NIST §1.3.5.1, Definition of Location, item 3 and the following continuous-data caveat

**sourceNote:** Derived from the linked finite-sample definition and exact count/order/arithmetic conventions. Adapts greatest observed frequency and nonuniqueness to an explicit finite argmax set. Chooses inclusion of all equal-frequency/all-distinct observations and empty output on an empty sample; these policies are stated rather than inferred from the word mode. Generalizes frequency counting to categorical carriers; excludes the source’s separate histogram midpoint approximation.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {A : Type u} [DecidableEq A] (x : A), Catalog.Mode {x} = {x}
```

**Source:** [`Catalog.DescriptiveStatisticsProofs.mode_singleton`](../lean/Catalog/DescriptiveStatistics.lean); consulted 2026-11-12.

**Scope:** registered-witness-type

**Interpretation:** For A with DecidableEq, Mode filters sample.toFinset by the universal maximum-count condition over observed sample values. Output is Finset A, with every tied maximizer retained and no ordering assumption on A. The semantic definition uses classical decidability for the bounded predicate; it is not a claimed efficient frequency-table implementation.

**Limits:** Proves the displayed result under the selected exact carrier/equality/empty/tie conventions. No proof of an arbitrary software implementation, population claim or numerical stability bound.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/Mode-maximizer-set": "Interpreted by the explicit data guard/count/sort definition: M(S)={a∈supp(S) | ∀b∈supp(S),c_S(b)≤c_S(a)}; supp(S)={a | c_S(a)>0}; M(∅)=∅."
}
```

<a id="node-urn-csabs-law-Mode-nonempty"></a>

### nonempty

`urn:csabs:law/Mode-nonempty`

**statement:** A nonempty finite sample always has a mode in the all-maximizers profile.

**formalStatement:** S≠∅ ⇒ M(S)≠∅.

**assumptions:** Finite multiset of observations on a carrier A with an equality relation; the Lean count/filter interface requires DecidableEq A. Counts include repetitions and input order is irrelevant. Output equality is extensional finite-set equality. Only observed values are candidates, so empty input returns the empty set instead of treating all unobserved count-zero values as modes. All tied maxima are returned; there is no no-repetition threshold, tie-break order, histogram binning, kernel density, population-density mode or NaN equivalence policy.

**dependsOn:** [maximizer-set](Mode.md#node-urn-csabs-axiom-Mode-maximizer-set)

**proofSketch:** The observed support is finite and nonempty, so the natural-valued occurrence-count function attains a maximum there. A maximizing observed value satisfies the defining mode predicate. This includes all-distinct data by the chosen policy.

**ruleRole:** derived-result

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial mathematical statement; only separately mapped fresh Lean witnesses are compiler-verified.

**source:** [NIST/SEMATECH e-Handbook of Statistical Methods: §1.3.5.1 Measures of Location](https://www.itl.nist.gov/div898/handbook/eda/section3/eda351.htm); accessedOn: 2026-11-12; sourceRole: Consulted definitions of arithmetic mean, odd/even sample median and nonunique empirical modes; the catalog makes empty-data and tie conventions explicit.

**sourceLocator:** NIST §1.3.5.1, Definition of Location, item 3 and the following continuous-data caveat

**sourceNote:** Derived from the linked finite-sample definition and exact count/order/arithmetic conventions. Adapts greatest observed frequency and nonuniqueness to an explicit finite argmax set. Chooses inclusion of all equal-frequency/all-distinct observations and empty output on an empty sample; these policies are stated rather than inferred from the word mode. Generalizes frequency counting to categorical carriers; excludes the source’s separate histogram midpoint approximation.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {A : Type u} [DecidableEq A] (sample : Multiset A), sample ≠ 0 → (Catalog.Mode sample).Nonempty
```

**Source:** [`Catalog.DescriptiveStatisticsProofs.mode_nonempty`](../lean/Catalog/DescriptiveStatistics.lean); consulted 2026-11-12.

**Scope:** registered-witness-type

**Interpretation:** For A with DecidableEq, Mode filters sample.toFinset by the universal maximum-count condition over observed sample values. Output is Finset A, with every tied maximizer retained and no ordering assumption on A. The semantic definition uses classical decidability for the bounded predicate; it is not a claimed efficient frequency-table implementation.

**Limits:** Proves the displayed result under the selected exact carrier/equality/empty/tie conventions. No proof of an arbitrary software implementation, population claim or numerical stability bound.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/Mode-maximizer-set": "Interpreted by the explicit data guard/count/sort definition: M(S)={a∈supp(S) | ∀b∈supp(S),c_S(b)≤c_S(a)}; supp(S)={a | c_S(a)>0}; M(∅)=∅."
}
```

## Theorems

<a id="node-urn-csabs-theorem-Mode-unique-maximum"></a>

### unique-maximum

`urn:csabs:theorem/Mode-unique-maximum`

**statement:** The mode set is a singleton exactly when one observed value has strictly greater count than every other observed value.

**formalStatement:** M(S)={a} ⇔ a∈supp(S) ∧ ∀b∈supp(S),b≠a ⇒ c_S(b)<c_S(a).

**assumptions:** Finite multiset of observations on a carrier A with an equality relation; the Lean count/filter interface requires DecidableEq A. Counts include repetitions and input order is irrelevant. Output equality is extensional finite-set equality. Only observed values are candidates, so empty input returns the empty set instead of treating all unobserved count-zero values as modes. All tied maxima are returned; there is no no-repetition threshold, tie-break order, histogram binning, kernel density, population-density mode or NaN equivalence policy.

**dependsOn:** [maximizer-set](Mode.md#node-urn-csabs-axiom-Mode-maximizer-set)

**proofSketch:** A strictly highest count makes a a maximizer and excludes every other observed b. Conversely, if M(S)={a}, then a is observed and dominates all counts; equality of another observed count with c_S(a) would make that value another member of M(S), contradicting singleton output.

**ruleRole:** derived-result

**notationLanguage:** informal mathematical Unicode

**reviewStatus:** Editorial mathematical statement; only separately mapped fresh Lean witnesses are compiler-verified.

**source:** [NIST/SEMATECH e-Handbook of Statistical Methods: §1.3.5.1 Measures of Location](https://www.itl.nist.gov/div898/handbook/eda/section3/eda351.htm); accessedOn: 2026-11-12; sourceRole: Consulted definitions of arithmetic mean, odd/even sample median and nonunique empirical modes; the catalog makes empty-data and tie conventions explicit.

**sourceLocator:** NIST §1.3.5.1, Definition of Location, item 3 and the following continuous-data caveat

**sourceNote:** Derived from the linked finite-sample definition and exact count/order/arithmetic conventions. Adapts greatest observed frequency and nonuniqueness to an explicit finite argmax set. Chooses inclusion of all equal-frequency/all-distinct observations and empty output on an empty sample; these policies are stated rather than inferred from the word mode. Generalizes frequency counting to categorical carriers; excludes the source’s separate histogram midpoint approximation.

**provenanceKind:** derived

## Concept provenance

- [NIST/SEMATECH e-Handbook of Statistical Methods: §1.3.5.1 Measures of Location](https://www.itl.nist.gov/div898/handbook/eda/section3/eda351.htm); accessedOn: 2026-11-12; sourceRole: Consulted definitions of arithmetic mean, odd/even sample median and nonunique empirical modes; the catalog makes empty-data and tie conventions explicit.

**sourceLocator:** NIST §1.3.5.1, Definition of Location, item 3 and the following continuous-data caveat

**sourceNote:** Adapts greatest observed frequency and nonuniqueness to an explicit finite argmax set. Chooses inclusion of all equal-frequency/all-distinct observations and empty output on an empty sample; these policies are stated rather than inferred from the word mode. Generalizes frequency counting to categorical carriers; excludes the source’s separate histogram midpoint approximation.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/Mode",
    "type": "Concept",
    "shortForm": "Mode",
    "fullName": "Empirical mode set (all observed frequency maximizers)",
    "synonyms": [
      "mode",
      "sample modes",
      "modal set",
      "frequency argmax"
    ],
    "category": [
      "urn:csabs:category/descriptive-statistics"
    ],
    "kind": "urn:csabs:kind/function",
    "definition": "The finite set of observed values with maximal occurrence count in a finite multiset. Every tied maximizer is retained, including all observed values when their counts are all equal. It applies to categorical as well as numeric observations.",
    "notation": "M(S)={a∈supp(S) | ∀b∈supp(S),c_S(b)≤c_S(a)}; M(∅)=∅.",
    "mathematicalFormulation": "For a finite multiset S on a carrier A with genuine equality, let c_S(a)∈ℕ be its occurrence count and supp(S)={a | c_S(a)>0}. Define M(S)={a∈supp(S) | ∀b∈supp(S),c_S(b)≤c_S(a)}. The output is a finite set, not a chosen representative. M(∅)=∅; every nonempty finite sample has at least one maximizer. All ties are included, so if every observation is distinct, M(S)=supp(S). Conventions declaring no mode for all-distinct/uniform samples, or selecting one tie winner, are different variants. No arithmetic or ordering on A is needed.",
    "hasOperation": [
      "urn:csabs:operation/Mode-evaluate",
      "urn:csabs:operation/Mode-isMode"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/Mode-maximizer-set"
    ],
    "hasLaw": [
      "urn:csabs:law/Mode-singleton",
      "urn:csabs:law/Mode-nonempty"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/Mode-unique-maximum"
    ],
    "requiresConcept": [
      "urn:csabs:concept/Multiset",
      "urn:csabs:concept/FiniteSet",
      "urn:csabs:concept/Function"
    ],
    "relatedConcept": [
      "urn:csabs:concept/ArithmeticMean",
      "urn:csabs:concept/Median",
      "urn:csabs:concept/FiniteDistribution"
    ],
    "axiomBasis": "The stated finite-multiset definition, explicit empty behavior and selected output convention. Finite multiset of observations on a carrier A with an equality relation; the Lean count/filter interface requires DecidableEq A. Counts include repetitions and input order is irrelevant. Output equality is extensional finite-set equality. Only observed values are candidates, so empty input returns the empty set instead of treating all unobserved count-zero values as modes. All tied maxima are returned; there is no no-repetition threshold, tie-break order, histogram binning, kernel density, population-density mode or NaN equivalence policy.",
    "basisKind": "defined-function",
    "basisScope": "Selected unweighted finite-sample statistic, not all weighted/population/rounded or interpolation conventions.",
    "convention": "Finite multiset of observations on a carrier A with an equality relation; the Lean count/filter interface requires DecidableEq A. Counts include repetitions and input order is irrelevant. Output equality is extensional finite-set equality. Only observed values are candidates, so empty input returns the empty set instead of treating all unobserved count-zero values as modes. All tied maxima are returned; there is no no-repetition threshold, tie-break order, histogram binning, kernel density, population-density mode or NaN equivalence policy.",
    "coverageStatus": "basis-reviewed",
    "verificationObligation": "Map multiplicity, equality, empty/missing-data policy, exact numeric semantics and tie/interpolation conventions to the target API. A compiled abstract identity is not implementation refinement.",
    "reviewStatus": "Sourced mathematical formulation with a separate Lean model and individually mapped witnesses.",
    "source": [
      "urn:csabs:source/nist-measures-of-location"
    ],
    "sourceLocator": "NIST §1.3.5.1, Definition of Location, item 3 and the following continuous-data caveat",
    "sourceNote": "Adapts greatest observed frequency and nonuniqueness to an explicit finite argmax set. Chooses inclusion of all equal-frequency/all-distinct observations and empty output on an empty sample; these policies are stated rather than inferred from the word mode. Generalizes frequency counting to categorical carriers; excludes the source’s separate histogram midpoint approximation.",
    "provenanceKind": "adapted",
    "leanFormulation": "def Mode {A : Type u} [DecidableEq A] (sample : _root_.Multiset A) : Finset A := by\n  classical\n  exact sample.toFinset.filter (fun a => ∀ b ∈ sample, sample.count b ≤ sample.count a)",
    "formulationSource": "urn:csabs:source/local-lean-DescriptiveStatistics",
    "formulationLocator": "Catalog.Mode",
    "formulationScope": "model",
    "leanModelMapping": "For A with DecidableEq, Mode filters sample.toFinset by the universal maximum-count condition over observed sample values. Output is Finset A, with every tied maximizer retained and no ordering assumption on A. The semantic definition uses classical decidability for the bounded predicate; it is not a claimed efficient frequency-table implementation.",
    "leanModelLimitations": "Exact selected finite-multiset interface. No floating-point error analysis, missing-data handling, weighted/population inference, complexity claim or numerical implementation refinement. Only individually registered results have compiled witnesses; the separately recorded theorem is not a registered proof.",
    "specializationOf": [
      "urn:csabs:concept/Function"
    ],
    "specializationNote": "Instantiate the total-function domain by Bag(A) and codomain by FinSet(A). Returning the entire frequency-maximizer set makes the result deterministic even when several values tie; it does not choose a single modal observation."
  },
  {
    "id": "urn:csabs:operation/Mode-evaluate",
    "type": "Operation",
    "name": "evaluate",
    "concept": "urn:csabs:concept/Mode",
    "signature": "Bag(A) → FinSet(A); S ↦ M(S)",
    "description": "Return every observed value whose occurrence count is maximal.",
    "precondition": "Finite multiset with equality on A; no numeric values or order are required.",
    "postcondition": "The full maximizer set, empty exactly for empty input under this profile.",
    "totality": "total on the stated typed domain; Option represents mathematical undefinedness, not an arbitrary default value"
  },
  {
    "id": "urn:csabs:operation/Mode-isMode",
    "type": "Operation",
    "name": "isMode",
    "concept": "urn:csabs:concept/Mode",
    "signature": "Bag(A)×A → Prop; (S,a) ↦ [a∈M(S)]",
    "description": "Test membership in the empirical mode relation.",
    "precondition": "Same value carrier and equality policy.",
    "postcondition": "True exactly for observed maximum-count values; false for all a when S is empty.",
    "totality": "total on the stated typed domain; Option represents mathematical undefinedness, not an arbitrary default value"
  },
  {
    "id": "urn:csabs:axiom/Mode-maximizer-set",
    "type": "Axiom",
    "name": "maximizer-set",
    "statement": "Modes are exactly observed frequency maximizers, retaining all ties.",
    "formalStatement": "M(S)={a∈supp(S) | ∀b∈supp(S),c_S(b)≤c_S(a)}; supp(S)={a | c_S(a)>0}; M(∅)=∅.",
    "assumptions": [
      "Finite multiset of observations on a carrier A with an equality relation; the Lean count/filter interface requires DecidableEq A. Counts include repetitions and input order is irrelevant. Output equality is extensional finite-set equality. Only observed values are candidates, so empty input returns the empty set instead of treating all unobserved count-zero values as modes. All tied maxima are returned; there is no no-repetition threshold, tie-break order, histogram binning, kernel density, population-density mode or NaN equivalence policy."
    ],
    "appliesTo": [
      "urn:csabs:concept/Mode"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Sourced mathematical definition; compilation status belongs to separate Lean evidence.",
    "source": [
      "urn:csabs:source/nist-measures-of-location"
    ],
    "sourceLocator": "NIST §1.3.5.1, Definition of Location, item 3 and the following continuous-data caveat",
    "sourceNote": "Adapts greatest observed frequency and nonuniqueness to an explicit finite argmax set. Chooses inclusion of all equal-frequency/all-distinct observations and empty output on an empty sample; these policies are stated rather than inferred from the word mode. Generalizes frequency counting to categorical carriers; excludes the source’s separate histogram midpoint approximation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/Mode-singleton",
    "type": "Law",
    "name": "singleton",
    "statement": "The only value in a singleton sample is its sole mode.",
    "formalStatement": "M({x})={x}.",
    "assumptions": [
      "Finite multiset of observations on a carrier A with an equality relation; the Lean count/filter interface requires DecidableEq A. Counts include repetitions and input order is irrelevant. Output equality is extensional finite-set equality. Only observed values are candidates, so empty input returns the empty set instead of treating all unobserved count-zero values as modes. All tied maxima are returned; there is no no-repetition threshold, tie-break order, histogram binning, kernel density, population-density mode or NaN equivalence policy."
    ],
    "appliesTo": [
      "urn:csabs:concept/Mode"
    ],
    "dependsOn": [
      "urn:csabs:axiom/Mode-maximizer-set"
    ],
    "proofSketch": "The support is {x}, whose count is 1; the only required count comparison is reflexive.",
    "ruleRole": "derived-result",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial mathematical statement; only separately mapped fresh Lean witnesses are compiler-verified.",
    "source": [
      "urn:csabs:source/nist-measures-of-location"
    ],
    "sourceLocator": "NIST §1.3.5.1, Definition of Location, item 3 and the following continuous-data caveat",
    "sourceNote": "Derived from the linked finite-sample definition and exact count/order/arithmetic conventions. Adapts greatest observed frequency and nonuniqueness to an explicit finite argmax set. Chooses inclusion of all equal-frequency/all-distinct observations and empty output on an empty sample; these policies are stated rather than inferred from the word mode. Generalizes frequency counting to categorical carriers; excludes the source’s separate histogram midpoint approximation.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {A : Type u} [DecidableEq A] (x : A), Catalog.Mode {x} = {x}",
    "formulationSource": "urn:csabs:source/local-lean-DescriptiveStatistics",
    "formulationLocator": "Catalog.DescriptiveStatisticsProofs.mode_singleton",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "For A with DecidableEq, Mode filters sample.toFinset by the universal maximum-count condition over observed sample values. Output is Finset A, with every tied maximizer retained and no ordering assumption on A. The semantic definition uses classical decidability for the bounded predicate; it is not a claimed efficient frequency-table implementation.",
    "leanModelLimitations": "Proves the displayed result under the selected exact carrier/equality/empty/tie conventions. No proof of an arbitrary software implementation, population claim or numerical stability bound.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/Mode-maximizer-set\": \"Interpreted by the explicit data guard/count/sort definition: M(S)={a∈supp(S) | ∀b∈supp(S),c_S(b)≤c_S(a)}; supp(S)={a | c_S(a)>0}; M(∅)=∅.\"}"
  },
  {
    "id": "urn:csabs:law/Mode-nonempty",
    "type": "Law",
    "name": "nonempty",
    "statement": "A nonempty finite sample always has a mode in the all-maximizers profile.",
    "formalStatement": "S≠∅ ⇒ M(S)≠∅.",
    "assumptions": [
      "Finite multiset of observations on a carrier A with an equality relation; the Lean count/filter interface requires DecidableEq A. Counts include repetitions and input order is irrelevant. Output equality is extensional finite-set equality. Only observed values are candidates, so empty input returns the empty set instead of treating all unobserved count-zero values as modes. All tied maxima are returned; there is no no-repetition threshold, tie-break order, histogram binning, kernel density, population-density mode or NaN equivalence policy."
    ],
    "appliesTo": [
      "urn:csabs:concept/Mode"
    ],
    "dependsOn": [
      "urn:csabs:axiom/Mode-maximizer-set"
    ],
    "proofSketch": "The observed support is finite and nonempty, so the natural-valued occurrence-count function attains a maximum there. A maximizing observed value satisfies the defining mode predicate. This includes all-distinct data by the chosen policy.",
    "ruleRole": "derived-result",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial mathematical statement; only separately mapped fresh Lean witnesses are compiler-verified.",
    "source": [
      "urn:csabs:source/nist-measures-of-location"
    ],
    "sourceLocator": "NIST §1.3.5.1, Definition of Location, item 3 and the following continuous-data caveat",
    "sourceNote": "Derived from the linked finite-sample definition and exact count/order/arithmetic conventions. Adapts greatest observed frequency and nonuniqueness to an explicit finite argmax set. Chooses inclusion of all equal-frequency/all-distinct observations and empty output on an empty sample; these policies are stated rather than inferred from the word mode. Generalizes frequency counting to categorical carriers; excludes the source’s separate histogram midpoint approximation.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {A : Type u} [DecidableEq A] (sample : Multiset A), sample ≠ 0 → (Catalog.Mode sample).Nonempty",
    "formulationSource": "urn:csabs:source/local-lean-DescriptiveStatistics",
    "formulationLocator": "Catalog.DescriptiveStatisticsProofs.mode_nonempty",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "For A with DecidableEq, Mode filters sample.toFinset by the universal maximum-count condition over observed sample values. Output is Finset A, with every tied maximizer retained and no ordering assumption on A. The semantic definition uses classical decidability for the bounded predicate; it is not a claimed efficient frequency-table implementation.",
    "leanModelLimitations": "Proves the displayed result under the selected exact carrier/equality/empty/tie conventions. No proof of an arbitrary software implementation, population claim or numerical stability bound.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/Mode-maximizer-set\": \"Interpreted by the explicit data guard/count/sort definition: M(S)={a∈supp(S) | ∀b∈supp(S),c_S(b)≤c_S(a)}; supp(S)={a | c_S(a)>0}; M(∅)=∅.\"}"
  },
  {
    "id": "urn:csabs:theorem/Mode-unique-maximum",
    "type": "Theorem",
    "name": "unique-maximum",
    "statement": "The mode set is a singleton exactly when one observed value has strictly greater count than every other observed value.",
    "formalStatement": "M(S)={a} ⇔ a∈supp(S) ∧ ∀b∈supp(S),b≠a ⇒ c_S(b)<c_S(a).",
    "assumptions": [
      "Finite multiset of observations on a carrier A with an equality relation; the Lean count/filter interface requires DecidableEq A. Counts include repetitions and input order is irrelevant. Output equality is extensional finite-set equality. Only observed values are candidates, so empty input returns the empty set instead of treating all unobserved count-zero values as modes. All tied maxima are returned; there is no no-repetition threshold, tie-break order, histogram binning, kernel density, population-density mode or NaN equivalence policy."
    ],
    "appliesTo": [
      "urn:csabs:concept/Mode"
    ],
    "dependsOn": [
      "urn:csabs:axiom/Mode-maximizer-set"
    ],
    "proofSketch": "A strictly highest count makes a a maximizer and excludes every other observed b. Conversely, if M(S)={a}, then a is observed and dominates all counts; equality of another observed count with c_S(a) would make that value another member of M(S), contradicting singleton output.",
    "ruleRole": "derived-result",
    "notationLanguage": "informal mathematical Unicode",
    "reviewStatus": "Editorial mathematical statement; only separately mapped fresh Lean witnesses are compiler-verified.",
    "source": [
      "urn:csabs:source/nist-measures-of-location"
    ],
    "sourceLocator": "NIST §1.3.5.1, Definition of Location, item 3 and the following continuous-data caveat",
    "sourceNote": "Derived from the linked finite-sample definition and exact count/order/arithmetic conventions. Adapts greatest observed frequency and nonuniqueness to an explicit finite argmax set. Chooses inclusion of all equal-frequency/all-distinct observations and empty output on an empty sample; these policies are stated rather than inferred from the word mode. Generalizes frequency counting to categorical carriers; excludes the source’s separate histogram midpoint approximation.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
