# Abstraction Discovery Guide

This guide details techniques for analyzing unannotated code, recognizing structural signatures, and matching them to mathematical concepts in the catalog.

## Signature Recognition Matrix

Examine the public and internal methods of the target component to classify its primary operations:

| Signature / Pattern | Mathematical Archetype | Candidate Catalog Concepts | Key Verification Questions |
| :--- | :--- | :--- | :--- |
| `combine(a: T, b: T): T` | Closed binary operation | `urn:csabs:concept/Semigroup`<br>`urn:csabs:concept/Monoid` | Is it associative? Does an empty/neutral value `e` exist such that `combine(a, e) == a`? |
| `merge(s1: S, s2: S): S` | State reconciliation | `urn:csabs:concept/JoinSemilattice`<br>`urn:csabs:concept/StateBasedCRDT` | Is `merge(s, s) == s` (idempotent)? Is `merge(s1, s2) == merge(s2, s1)` (commutative)? Does state monotonically grow? |
| `compare(a: T, b: T): Int` | Total preorder / Strict weak order | `urn:csabs:concept/TotalOrder`<br>`urn:csabs:concept/Preorder` | Is `compare(a, b) == -compare(b, a)`? If `a < b` and `b < c`, is `a < c` (transitivity)? Does it handle NaN or edge values? |
| `step(state: S, event: E): S` | State transition function | `urn:csabs:concept/LabelledTransitionSystem`<br>`urn:csabs:concept/KripkeStructure` | Is the state transition total or partial? Are terminal/deadlock states explicitly handled? |
| `acquire(p: P): Bool`<br>`release(p: P): Unit` | Mutual exclusion / Access | `urn:csabs:concept/Lock`<br>`urn:csabs:concept/Mutex` | Can two distinct processes hold the lock simultaneously? Can a non-holder release? |
| `add(k: K, v: V): Collection` | Associative storage | `urn:csabs:concept/Multimap`<br>`urn:csabs:concept/Set` | How are duplicate keys or values resolved? Is key equality structural or reference-based? |

---

## Common Code Anti-Patterns & Mathematical Root Causes

### 1. Non-Associative Aggregation in Parallel Folds
* **Code Pattern:** Aggregating data across parallel threads, batches, or distributed workers using an ad-hoc reducer (e.g., streaming averages or floating-point additions).
* **Mathematical Cause:** The reduction operation violates the associativity law `urn:csabs:axiom/Monoid-associative` (`(x · y) · z == x · (y · z)`).
* **Consequence:** Results differ depending on thread scheduling, batch size, or partitioning.
* **Refactoring:** Decompose the state into an associative pair (e.g., storing `(sum, count)` instead of running `mean`), completing a true Monoid.

### 2. Missing Identity Element (The "Empty Collection" Trap)
* **Code Pattern:** A combination function that works on two elements but requires special-case guards (`if len(items) == 0 ... elif len(items) == 1 ...`) or raises an unhandled exception when an accumulator is empty.
* **Mathematical Cause:** The structure is at best a `Semigroup` lacking the identity axiom `urn:csabs:axiom/monoid-identity` (`e · x == x · e == x`).
* **Consequence:** Awkward client code, defensive null checks, and runtime crashes on empty streams.
* **Refactoring:** Identify or construct the neutral element `e` (e.g., `0` for addition, `1` for product, `[]` for lists, `∅` for sets) and elevate the component to a `Monoid`.

### 3. Faulty Comparators & Broken Transitivity
* **Code Pattern:** Implementing a comparator using integer subtraction:
  ```java
  int compare(A a, A b) { return a.val - b.val; } // Vulnerable to integer underflow/overflow
  ```
  or incomplete multi-field comparisons that fail to form a strict weak order.
* **Mathematical Cause:** Violates transitivity (`a < b ∧ b < c ⇒ a < c`) or irreflexivity in `urn:csabs:concept/TotalOrder`.
* **Consequence:** Standard sorting algorithms throw `IllegalArgumentException: Comparison method violates its general contract`, priority queues produce wrong orders, or binary searches loop infinitely.
* **Refactoring:** Use explicit three-way comparisons (`Integer.compare(a, b)`) and lexicographic composition.

### 4. Non-Idempotent or Non-Commutative Distributed Merge
* **Code Pattern:** Reconciling offline or concurrent client updates by appending to an un-deduplicated list or overwriting timestamps with unsynchronized clocks.
* **Mathematical Cause:** The merge function fails to satisfy the join-semilattice laws (`urn:csabs:concept/JoinSemilattice`):
  * Idempotence: `x ⊔ x = x`
  * Commutativity: `x ⊔ y = y ⊔ x`
  * Associativity: `(x ⊔ y) ⊔ z = x ⊔ (y ⊔ z)`
* **Consequence:** Replicas diverge permanently; re-transmissions duplicate data.
* **Refactoring:** Refactor the merge logic to implement a standard `StateBasedCRDT` (e.g., Observed-Remove Set or Grow-Only Counter).

---

## Discovery Checklist

When presenting an abstraction discovery report:
1. **Identify the Carrier:** What is the underlying domain type? What values are admissible?
2. **Define Observability & Equality:** How is equality determined (reference, structural, or semantic equivalence modulo irrelevant state)?
3. **Query Catalog Axioms:** Fetch the exact axioms governing the candidate concept using `scripts/catalog.py get ID --sections axioms laws`.
4. **Demonstrate Counterexamples:** If an algebraic law fails, provide concrete, reproducible inputs triggering the violation.
5. **Formulate the Remedy:** Provide clean, idiomatic refactoring recommendations that restore mathematical soundness without degrading performance.
