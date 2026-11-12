# Mean, median and mode

These entries describe deterministic statistics of finite samples. No random-sampling, population inference, missing-data policy or floating-point error model is assumed. Data use multisets: repetitions count, but input order does not.

| Concept | Selected mathematical profile | Empty sample |
| --- | --- | --- |
| [ArithmeticMean](../concepts/ArithmeticMean.md) | Sum of exact real observations divided by their occurrence count. | Undefined, represented by `none`. |
| [Median](../concepts/Median.md) | Middle sorted observation for odd size; arithmetic midpoint of the two central observations for even size. | Undefined, represented by `none`. |
| [Mode](../concepts/Mode.md) | Finite set of all observed values attaining the greatest occurrence count, including ties. | Empty set. |

These are distinct functions, linked as related concepts under Statistics → Descriptive statistics. None specializes another. Mean and median instantiate [PartialFunction](../concepts/PartialFunction.md) on real multisets with domain restricted to nonempty inputs; the complete mode set instantiates [Function](../concepts/Function.md) from multisets to finite sets. These links do not transfer axioms. Mean and median require numeric data in this profile; mode also supports categorical values with a specified equality policy. The concepts link to the existing [Multiset](../concepts/Multiset.md), [FiniteSet](../concepts/FiniteSet.md), [RealNumber](../concepts/RealNumber.md) and, where relevant, [FiniteDistribution](../concepts/FiniteDistribution.md) entries.

## Formulas and conventions

Let S be a finite multiset, N its cardinality including repetitions, and c_S(a) the occurrence count of a. For nonempty real data,

```text
mean(S) = (Σ over all occurrences x in S of x) / N
        = (Σ over distinct observed a of c_S(a)·a) / N
```

For the sorted real observations y₀≤⋯≤y_{N−1}, let lo=⌊(N−1)/2⌋ and hi=⌊N/2⌋. The numeric median is `(y_lo+y_hi)/2`. The two indices coincide for odd N. In an even sample the result can lie between observed values. Lower/upper medians, median intervals and quantile interpolation methods need explicit variants. These formulas follow the [NIST definitions of mean and median](https://www.itl.nist.gov/div898/handbook/eda/section3/eda351.htm), with explicit multiset and empty-data conventions.

The selected empirical mode set is

```text
M(S) = {a in support(S) | for every b in support(S), c_S(b) ≤ c_S(a)}.
```

The [NIST definition](https://www.itl.nist.gov/div898/handbook/eda/section3/eda351.htm) allows nonunique modes. This catalog makes the tie policy precise: all tied maxima are returned. Thus all-distinct data return every observed value as a maximizer. APIs that report “no mode” when nothing repeats, require a unique winner, or select one tied value have different contracts. Only observed candidates participate, so empty data return the empty set rather than every unobserved count-zero value. Histogram/KDE and population-density modes are outside this exact occurrence-count profile.

For example, the multiset {1,1,4,10} has mean 4, median 5/2 and mode set {1}. The categorical sample {red,red,blue,blue,green} has mode set {red,blue}. Exact mathematical equality must be mapped to any software-specific case folding, equivalence classes, NaNs, rounding or missing-value conventions before using these equations as oracles.

Integer-valued observations do not imply integer division: the mean and even-sample median can be nonintegral. A general weighted mean, geometric/harmonic mean, grouped-bin midpoint estimate or population expectation is not the unweighted sample arithmetic mean. An empirical distribution with mass c_S(a)/N recovers the finite sample frequencies, but arbitrary distributions and inference require their own explicit assumptions.

## Lean models and evidence

[Catalog/DescriptiveStatistics.lean](../lean/Catalog/DescriptiveStatistics.lean) defines exact real `ArithmeticMean` and `Median` with Option guards, proof-bounded central indices after multiset sorting, and a generic finite-set `Mode` filter. Mode requires `DecidableEq` on its carrier; no numeric ordering on categorical values is imposed. These semantic definitions use exact reals/classical machinery and are not claimed to be efficient floating-point implementations.

Six laws have independently mapped expected types and registered Lean witnesses:

| Claim | Symbol in Catalog.DescriptiveStatisticsProofs |
| --- | --- |
| ArithmeticMean-singleton | mean_singleton |
| ArithmeticMean-balance | mean_balance |
| Median-singleton | median_singleton |
| Median-pair | median_pair |
| Mode-singleton | mode_singleton |
| Mode-nonempty | mode_nonempty |

The records also state a size-weighted mean merge formula, bounds by the median's central observations, and the strict-count characterization of a unique mode. Those three theorem statements have editorial derivations and no registered Lean witnesses. A structure/model binding, source citation or displayed equation alone is not a proof. Current compiler and axiom-audit evidence is available through `scripts/lean.py get ID`; no software implementation refinement or population theorem is asserted.

## Retrieve only what the task needs

Choose a command for the current task rather than loading this entire family or all theorems:

```sh
python3 scripts/catalog.py list --category descriptive-statistics
python3 scripts/catalog.py get Median --sections operations
python3 scripts/agent_query.py node urn:csabs:law/Median-pair
python3 scripts/agent_query.py node urn:csabs:law/Median-pair --view lean
python3 scripts/lean.py get urn:csabs:law/Median-pair
```

Focused views preserve preconditions, sample/tie conventions and source-gap metadata. Fetch theorems only when their result is needed and Lean material only when typed interpretation or proof reuse affects the task.
