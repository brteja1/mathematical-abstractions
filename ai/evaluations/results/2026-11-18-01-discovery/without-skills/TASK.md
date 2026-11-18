# Review a batch reducer

We combine worker reports in a tree. Each report summarizes a nonempty batch of integer measurements. We want the combined count and mean to match processing the concatenated batches. Diagnostic strings must retain their original order and multiplicity; changing these diagnostics to a set would break callers. The current implementation uses exact rational arithmetic:

```python
from dataclasses import dataclass
from fractions import Fraction

@dataclass(frozen=True)
class Report:
    count: int
    mean: Fraction
    diagnostics: tuple[str, ...]

def merge(a: Report, b: Report) -> Report:
    return Report(a.count + b.count, (a.mean + b.mean) / 2,
                  a.diagnostics + b.diagnostics)
```

The team proposes regrouping this reduction and then freely reordering workers. Review whether that is valid. Give runnable counterexamples for any defects, explain the mathematical structure that actually fits, and recommend a representation and merge rule that preserve the contract, including a useful empty report. Keep the review in `answer.md`; put executable checks in `checks.py` and run them. Do not modify the supplied implementation or the catalog.
