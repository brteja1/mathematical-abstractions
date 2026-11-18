# Review a priority selector and its mapping

The normative contract is:

- Q1: All finite sequences of `(integer_priority, string_payload)` pairs are valid input, including sequences longer than two.
- Q2: Return one pair with minimum integer priority. Among equal priorities, any of the tied pairs may be returned.
- Q3: Empty input raises `ValueError`. No input sequence is mutated.

The implementation mapping says: M1 maps the carrier to sequences of length at most two. M2 maps selection to the first minimum pair. M3 maps empty input to `ValueError`.

```python
def choose(items):
    if not items:
        raise ValueError("empty")
    return min(items[:2], key=lambda pair: pair[0])
```

Existing tests only check `[(2,"a"),(1,"b")]`, an empty list, and `[(1,"a"),(1,"b")]` returning the first pair. Review both the mapping and code against the normative contract. Show runnable evidence, distinguish violations from permitted design choices, and describe what the existing tests establish. Save `answer.md` and runnable `checks.py`; run the checks. Do not repair the code, mapping, specification or catalog.
