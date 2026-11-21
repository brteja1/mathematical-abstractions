---
name: implementation-refinement
description: Establish explicitly scoped refinement evidence for the actual implementation, with reviewed semantics, executable proof checks and trust boundaries.
---

# Implementation Refinement

Start from a versioned implementation mapping and normative clause IDs. Retrieve only the catalog interfaces and claims needed for the refinement. Define the representation relation, invariant, equality/observations, input domain and allowed outcomes, including errors and divergence. Constructor establishment, preservation, operation simulation and required progress are separate obligations.

Identify which artifact the verifier actually checks. A theorem about a separate mathematical model does not establish a relation to executable code. For this repository's narrow lean-source-v1 profile, the function and theorem are in the same Lean source and the theorem's expected type names that function. Review the expected proposition and its mapping independently of the proof. The runner compiles it in the pinned Lean project, checks theorem identity and audits transitive axioms. It does not prove generated native code, a Python port, foreign calls or runtime behavior.

For other languages, retain actual source hashes, verifier/version/configuration, semantics and source correspondence. When no supported proof profile exists, retain the external verifier result with its actual evidence kind and scope, but mark it unsupported for automated proof admission. Record a bounded check as bounded and an inspection as review; do not downgrade an external proof merely because this runner cannot validate it. Report the unsupported proof gate; do not relabel a zero-exit command as a proof. Universal refinement needs a justified semantics and correspondence for all required inputs/outcomes, not only examples or assumed law fields.

Run the proof, audit, independent examples and a behavior-changing mutation. A failed or stale check blocks admission. Report excluded language/runtime features and environment assumptions. Use mathematical-tests for API tests and implementation-conformance to challenge the mapping; do not weaken the specification to make proofs pass.

## Catalog and evidence discipline

Read the [shared lifecycle and ledger guide](../spec-driven-development/references/assurance.md) for the executable contract, commands, pilot and limits. Reuse existing target mappings; do not create competing specifications.

Retrieve mathematical facts only through `python3 <catalog>/scripts/catalog.py list --search TERM`, focused `get` sections, `scripts/agent_query.py node ID` or the bounded mathematical-tests helper. Here `<catalog>` is three directories above this skill directory. Follow necessary premises explicitly and resolve truncation. Do not browse catalog storage or generated exports for facts. Prerequisites and hierarchy confer no axioms or proof evidence.

Report required mathematical gaps before acquisition or dependent steps, including searched queries, candidates, mismatch and blocked work. Follow [catalog-use](../mathematical-tests/references/catalog-use.md) and [abstraction-acquisition](../abstraction-acquisition/SKILL.md). A retrieval/backend failure is a tooling blocker: resolve setup first and use a fallback only when the active skill permits it; do not treat it as absent mathematics. Do not silently continue on unsupported assumptions. Preserve provenance and pinned dependencies. Read the [formulation guide](../mathematical-tests/references/formulations.md) only when typed correspondence or witness evidence is needed.
