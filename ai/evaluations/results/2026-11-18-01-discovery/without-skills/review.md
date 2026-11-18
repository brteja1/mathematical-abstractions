# Batch reducer review

**The current reducer cannot safely regroup. The corrected reducer can regroup as long as it preserves worker order.** Free reordering can change the diagnostic tuple even when the count and mean agree.

| Check | Inputs | Result |
| --- | --- | --- |
| Agreement with concatenation | Batches `(0,)` and `(3, 3)` | The count is correctly 3, but the merge gives mean `3/2` instead of `6/3 = 2`. It gives each batch equal weight. |
| Associativity | Singleton batches `a = (0,)`, `b = (0,)`, `c = (4,)` | `merge(merge(a, b), c)` gives mean 2 and `merge(a, merge(b, c))` gives mean 1. Both preserve count 3 and the same diagnostic order. The concatenated mean is `4/3`. |
| Commutativity | Two singleton zero batches with diagnostics `("a",)` and `("b",)` | Swapping the operands changes `("a", "b")` to `("b", "a")` while count and mean stay equal. |

The original merge fails the associativity required of a semigroup. It also has no two-sided identity. Count addition would require an identity of count zero, and averaging with a fixed identity mean would require that mean to equal every input mean.

## Corrected representation

Store `(count, total, diagnostics)`, with an integer total and a tuple of strings. Merge using

```text
(n, s, d) ⋆ (m, t, e) = (n + m, s + t, d + e)
```

Here `d + e` appends the right tuple to the left, preserving every occurrence. At the output boundary, return the count, `Fraction(total, count)` when the count is positive, and the diagnostics. Use `(0, 0, ())` as the empty report and expose its mean as `None`. Existing nonempty reports can be converted exactly because `count * mean` equals the integer sum for a valid batch. In the original count-and-mean representation, the corresponding nonempty merge uses the weighted mean `(n * mean_a + m * mean_b) / (n + m)`.

Count and total are additive under batch concatenation, and the diagnostics append in the same order. Thus merging the summaries of two batches produces the summary of their concatenation. Applying this at each node gives the same result as a single pass over the batches in leaf order.

On the ambient carrier of nonnegative counts, integer totals, and finite diagnostic tuples, the operation is the product of two additive monoids and the monoid of diagnostic sequences under concatenation. Valid states consist of positive counts with integer totals and diagnostic tuples, together with the empty report. They are closed under merge. Integer addition and tuple concatenation are associative, and zero and the empty tuple give the two-sided identity componentwise. The nonempty states form a semigroup, and including the empty report gives a **noncommutative monoid**. The numeric projection is commutative, but the diagnostic component still gives the swap counterexample above. Parallel workers may finish in any order if the tree combines their summaries in the original leaf order.

The examples and corrected reducer checks are runnable with `python3 checks.py`.
