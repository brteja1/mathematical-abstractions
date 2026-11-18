# Batch reducer review

The current reducer can change the mean when you regroup workers, even with their order fixed. The proposed merge below supports any parenthesization that preserves the original worker order. Arbitrary worker permutations can still change the diagnostic tuple.

## Current behavior

The supplied component is the frozen `Report` record and its binary `merge` in `TASK.md`. The snippet has one merge definition and shows no call sites, duplicate implementations, or tests. The defect is in the mean formula. Count addition and diagnostic concatenation already implement their parts of the contract.

| Check | Current merge | Proposed merge |
| --- | --- | --- |
| Closed binary operation on its report carrier | Yes, as an operation on positive counts, rational means and string tuples | Yes |
| Correct summary of concatenation | Fails for unequal counts with different means | Yes |
| Associative | No | Yes |
| Two-sided identity | None | `(0, 0, ())` |
| Commutative on full reports | No | No |

- **Incorrect weighting.** Batches `(0, 0)` and `(6,)` yield count 3 and mean 3, while their concatenation has mean 2. Each merge gives the input means equal weight regardless of how many measurements they summarize.
- **Regrouping.** For singleton batches containing 0, 0, and 6, the left grouping gives 3 and the right grouping gives 3/2. The correct mean is 2. Both groupings produce the same count and diagnostic tuple.
- **Reordering.** Give singleton batches containing 0 and 6 the diagnostics `("a", "a")` and `("b",)`. Swapping operands changes `("a", "a", "b")` to `("b", "a", "a")`, even though a two-way swap preserves count and mean. In an unchanged three-leaf tree, a permutation can also change the current mean by moving a batch to a different depth.
- **Empty report.** The current carrier has positive counts. Even if count zero were admitted, an identity would need empty diagnostics and a fixed mean `m` satisfying `(m + x) / 2 = x` for every batch mean `x`. A batch with mean 0 requires `m = 0` and one with mean 6 requires `m = 6`.

## Recommended representation and merge

Store `(count, total, diagnostics)` with a positive integer count, an exact integer sum, and a finite tuple of strings. Extend that carrier with the empty report `(0, 0, ())`. Merge by adding counts, adding totals, and appending the right tuple to the left tuple. Expose the mean as `Fraction(total, count)` when count is positive and `None` when count is zero. A valid existing worker report can supply its total as `count * mean`, which is integral for exact means of integer measurements. A report already produced by the faulty merge may have lost the correct total and must be rebuilt from its inputs.

With fieldwise equality, this is an instance of `urn:csabs:concept/Monoid`. Componentwise merge combines two additive coordinates and the finite string sequence (`urn:csabs:concept/Sequence`), restricted to valid report states. Positive-count states alone form a `urn:csabs:concept/Semigroup` under the corrected merge. The current merge fails even semigroup associativity.

Integer addition is associative with unit 0, and tuple concatenation is associative with the empty tuple as unit (`urn:csabs:law/sequence-concat-associative` and `urn:csabs:law/sequence-empty-identity`). These component laws give associativity and a two-sided identity on full reports. On concatenated inputs, lengths and integer sums add and the diagnostics append in input order. Thus summarizing the concatenation equals merging the summaries, and this holds at every node of an order-preserving tree. The final mean is the combined sum divided by the combined count, equivalently the count-weighted mean of two nonempty inputs.

The count and total coordinates commute. Full reports fail commutativity by the same diagnostic swap above. Preserve the original left-to-right order of leaves even if workers execute or finish in a different order. A set would discard duplicate occurrences and would lose the required sequence order.

Run `python3 checks.py` for the counterexamples and checks of the replacement.
