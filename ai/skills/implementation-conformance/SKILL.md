---
name: implementation-conformance
description: Review software against a catalog-based specification and implementation mapping, using traceable obligations, code inspection and executable evidence. Use to assess generated or existing code; passing catalog validation is not implementation conformance.
---

# Review implementation conformance

Compare actual software behavior with its normative specification and explicit implementation mapping. Deliver scoped findings with reproducible evidence and unchecked obligations. A request for review alone does not authorize repairs or changing requirements.

## Establish the review baseline

Read the target project's instructions, specification, mapping, relevant implementation and tests. Record revisions/hashes and relevant uncommitted changes. Check that selected catalog records still match the mapping's recorded baseline; changed semantics require review, not automatic fingerprint refresh.

If no mapping exists, construct the minimum explicit interpretation needed using [implementation-mapping](../implementation-mapping/SKILL.md) and its [template](../implementation-mapping/assets/implementation-map.md). Keep provisional assumptions visible. Compare the mapping itself against the normative clauses before using it as an oracle; an incorrect mapping can make incorrect code appear conformant. Do not assume an earlier consistency review occurred or passed.

Resolve `<catalog>` to the checkout containing this skill. Retrieve only disputed or needed records through absolute paths:

```sh
python3 <catalog>/scripts/catalog.py get Stack --sections operations axioms laws sources
python3 <catalog>/scripts/agent_query.py node urn:csabs:law/stack-push-pop
```

These commands use authoritative Markdown and Python's standard library. For ONTFS queries use the existing [bounded retrieval guide](../mathematical-tests/references/retrieval.md); report the backend, follow needed premises, and respect truncation and source freshness. Never transfer axioms through prerequisites or specialization links. Preserve legacy provenance gaps and distinguish editorial claims from fresh compiled witnesses.

## Inspect every selected obligation

Build an obligation-to-evidence table using the mapping's stable local IDs. Mark each as supported within stated scope, violated, blocked by ambiguity, or unchecked. A missing implementation or test is not automatically a semantic contradiction.

Check constructor establishment of the representation invariant, operation preservation, the abstraction function/relation, equality and observability, admissible inputs and allowed outcomes. Inspect error paths and state after failures, aliasing, numeric boundaries, empty cases, capacity and totality where relevant. Include required inputs that the code rejects even when happy-path equations pass. Do not infer total correctness or progress from partial-correctness assertions.

For nondeterministic behavior, compare all possible implementation outcomes to the permitted set; one matching trace is insufficient, while choosing a subset can be valid. Concurrent conformance needs the specified history relation, ordering and scheduler/fairness assumptions; sequential tests alone cannot establish it. Do not add liveness, fairness or performance promises absent from the contract.

The [worked stack example](../implementation-mapping/references/stack-example.md) shows why a representation invariant and passing local laws can coexist with a required-domain violation.

## Construct and run evidence

Use focused inspection for direct mismatches, [mathematical-tests](../mathematical-tests/SKILL.md) for executable properties, and an independent abstract reference model for operation sequences when useful. Annotate generated tests with obligation IDs, catalog claim IDs and the exact observation/assertion mapping. Exercise preconditions on nonempty valid domains; do not make failing requirements disappear through filters or assumptions. Test invalid inputs against the product's error contract.

Run relevant existing tests and any justified checks in the target project's environment. Retain commands, tool versions, code/specification/mapping hashes, results, bounds and minimized counterexamples or seeds. An unavailable backend, timeout, `unknown` or unexecuted test is unchecked/inconclusive evidence. Finite enumeration is exhaustive only for its declared finite model; samples do not establish universal conformance.

For requested formal refinement, inspect the actual concrete-to-abstract encoding and prove the mapped obligations in the chosen assistant. Follow this catalog's `lean/README.md` when using its Lean project and keep pins unchanged. Require fresh compiler and axiom-audit evidence; neither a model binding nor an abstract theorem proves target-code correspondence. State any gap between encoded code and executed software.

## Report and handle requested repairs

For each finding give severity based on actual consequence, specification clause/locator, mapping obligation, catalog IDs, code location, triggering input/trace, expected versus actual observations, and the evidence scope. Separate implementation defects, mapping defects, ambiguities, specification conflicts and unchecked obligations. Route actual requirement conflicts to [specification-consistency](../specification-consistency/SKILL.md); a defect in one implementation does not show the specification is impossible.

Summarize covered and unchecked obligations without equating a count to completeness. Report citation gaps separately from behavioral findings. Do not call an entire implementation verified based on selected passing tests or abstract Lean witnesses.

When repair is requested, fix behavior consistent with the normative contract, update the mapping when representation changes, and rerun affected checks. Do not weaken requirements or alter tests to accept the defect. Keep review artifacts in the target project or requested scratch location; catalog edits and proof promotion are separate tasks. Skills in `ai/skills/` require explicit reading or host registration for discovery.
