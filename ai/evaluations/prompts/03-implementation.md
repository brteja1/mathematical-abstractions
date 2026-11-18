# Implement partitionable reading summaries

Implement `summary.py` using Python's standard library:

- S1: `empty()` returns a summary of no readings.
- S2: `summarize(readings)` accepts any finite iterable of signed Python integers, including an empty iterable and a one-pass generator.
- S3: `merge(a,b)` returns a fresh summary whose observations equal summarizing the concatenated readings; it does not change either argument.
- S4: `mean(s)` returns an exact `fractions.Fraction`, or `None` when empty.
- S5: `maximum(s)` returns the greatest reading, or `None` when empty.
- S6: There are no fixed capacity or machine-integer bounds. Internal representation is your choice.

Provide the implementation, a concise requirement-to-API mapping in `mapping.md`, and meaningful `unittest` checks in `test_summary.py`. Run them. Explain any remaining limitations in `answer.md`. Do not change these requirements or the catalog.
