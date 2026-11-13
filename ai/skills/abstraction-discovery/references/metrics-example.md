# Abstraction Discovery: Metrics Aggregator Example

This reference demonstrates the discovery process on an unannotated Python metrics aggregation class. It shows how examining signatures and testing algebraic laws uncovers subtle bugs and guides principled refactoring.

## 1. The Original Unannotated Code

```python
class MetricsReport:
    """Telemetry report aggregated across microservice workers."""
    def __init__(self, count, mean_latency, errors):
        self.count = count
        self.mean_latency = mean_latency
        self.errors = errors  # list of error strings

    def merge(self, other):
        """Ad-hoc combination of two reports."""
        new_count = self.count + other.count
        # Naive averaging of means
        new_mean = (self.mean_latency + other.mean_latency) / 2.0
        new_errors = self.errors + other.errors
        return MetricsReport(new_count, new_mean, new_errors)
```

---

## 2. Abstraction Discovery Analysis

### Step A: Operational Signature
The method `merge(self, other) -> MetricsReport` is a closed binary operation `(M, M) -> M`.

### Step B: Catalog Retrieval
Query candidate concepts for binary combinations:
```sh
python3 scripts/catalog.py list --search monoid
python3 scripts/catalog.py get Monoid --sections operations axioms laws
```
Candidate: **`urn:csabs:concept/Monoid`**
* Carrier: `MetricsReport`
* Operation: `merge` (binary product `urn:csabs:operation/monoid-product`)
* Expected Laws:
  * Associativity: `(a.merge(b)).merge(c) == a.merge(b.merge(c))` (`urn:csabs:axiom/Monoid-associative`)
  * Identity: `∃e: e.merge(a) == a.merge(e) == a` (`urn:csabs:axiom/monoid-identity`)
  * Commutativity (desirable for distributed aggregation): `a.merge(b) == b.merge(a)`

### Step C: Testing the Laws & Exposing Violations

#### Violation 1: Broken Associativity (Mean Latency Calculation)
* Test case: Three worker batches with different counts:
  * Batch 1: `count=100, mean=10.0`
  * Batch 2: `count=100, mean=10.0`
  * Batch 3: `count=1, mean=100.0`
* Evaluation:
  * `(Batch1 + Batch2) + Batch3`:
    * Step 1: `(10.0 + 10.0) / 2.0 = 10.0`
    * Step 2: `(10.0 + 100.0) / 2.0 = 55.0`
  * `Batch1 + (Batch2 + Batch3)`:
    * Step 1: `(10.0 + 100.0) / 2.0 = 55.0`
    * Step 2: `(10.0 + 55.0) / 2.0 = 32.5`
* **Result:** `55.0 != 32.5`. The merge is **non-associative**. Parallel reduction will produce non-deterministic results depending on the tree reduction order.

#### Violation 2: Missing Identity Element
* Calling `merge` on an empty or uninitialized batch raises errors or distorts the mean (dividing `(0 + mean)/2`). There is no identity report `e` such that `e.merge(m) == m`.

#### Violation 3: Order-Dependent Error Append
* Concatenating `errors = self.errors + other.errors` makes `merge` non-commutative and causes duplicate errors across retry loops.

---

## 3. Principled Refactoring

Restructure the state into an algebraic **Monoid**:
1. Store total latency sum (`sum_latency`) and `count` rather than `mean_latency`.
2. Use a set or deduplicated structure for `errors`.
3. Provide an explicit identity element `MetricsReport.empty()`.

```python
from dataclasses import dataclass
from typing import FrozenSet

@dataclass(frozen=True)
class PrincipledMetricsReport:
    """
    A verified Monoid under merge.
    Catalog concept: urn:csabs:concept/Monoid
    """
    count: int
    sum_latency: float
    errors: FrozenSet[str]

    @property
    def mean_latency(self) -> float:
        return self.sum_latency / self.count if self.count > 0 else 0.0

    @classmethod
    def empty(cls) -> "PrincipledMetricsReport":
        """Identity element (urn:csabs:axiom/monoid-identity)."""
        return cls(count=0, sum_latency=0.0, errors=frozenset())

    def merge(self, other: "PrincipledMetricsReport") -> "PrincipledMetricsReport":
        """
        Associative, commutative binary combination.
        Satisfies urn:csabs:axiom/Monoid-associative.
        """
        return PrincipledMetricsReport(
            count=self.count + other.count,
            sum_latency=self.sum_latency + other.sum_latency,
            errors=self.errors | other.errors
        )
```

### Verification of Satisfied Laws

```python
def test_monoid_laws():
    e = PrincipledMetricsReport.empty()
    m1 = PrincipledMetricsReport(count=100, sum_latency=1000.0, errors=frozenset(["timeout"]))
    m2 = PrincipledMetricsReport(count=50, sum_latency=600.0, errors=frozenset(["404"]))
    m3 = PrincipledMetricsReport(count=1, sum_latency=100.0, errors=frozenset(["timeout"]))

    # 1. Identity law
    assert e.merge(m1) == m1
    assert m1.merge(e) == m1

    # 2. Associativity law
    left = (m1.merge(m2)).merge(m3)
    right = m1.merge(m2.merge(m3))
    assert left == right
    assert left.mean_latency == right.mean_latency

    # 3. Commutativity law
    assert m1.merge(m2) == m2.merge(m1)
    print("All monoid laws verified successfully.")

if __name__ == "__main__":
    test_monoid_laws()
```
