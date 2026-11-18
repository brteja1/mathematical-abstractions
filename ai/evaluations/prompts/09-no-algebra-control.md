# Simplify repeated display labels

The following formatting appears in five independent command-line reports:

```python
label = f"{person.family_name}, {person.given_name}"
```

All five reports intentionally use this exact format and already accept the same Person type. There are no aggregation, ordering, concurrency or mathematical proof requirements. Recommend a small maintainable refactoring, including how to preserve behavior and where to place it. Do not invent new product requirements, modify the catalog, or implement a framework. Save your recommendation in `answer.md`.
