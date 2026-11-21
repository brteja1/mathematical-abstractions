---
name: assurance-review
description: Challenge specification-to-code assurance claims, traceability, nonvacuity, evidence freshness and trusted assumptions independently.
---

# Assurance Review

Review normative sources and the evidence ledger, not only the implementation author's summary. Preserve review scope; a review request does not authorize repairs. Query catalog semantics independently and compare them with requirement, API and proof mappings.

Check both directions: every requirement and normative clause has implementation/evidence obligations, and every claimed guarantee has a source and applicable evidence. Challenge hidden domain restrictions, impossible preconditions, absent permitted outcomes, incomplete initial states, aliases, numeric semantics, nondeterminism, fairness and environment promises. Distinguish legitimate implementation choices from violations and unspecified behavior.

Inspect expected proof propositions, direct premise mappings and actual checked artifacts. Look for assumed target laws, weakened postconditions, a separate model substituted for source code, unsupported axioms, stale fingerprints, mutable dependencies, ignored failures and evidence-kind inflation. Read check output and rerun appropriate checks; a passed ledger only reports declared local evidence.

Use independent scenarios, small counterexamples and a realistic mutant where appropriate. Separate demonstrated defects, ambiguities, bounded results, unchecked obligations and trusted assumptions. Reviewer identity and receipt authenticity are outside the local gate's threat model. If review is performed by the implementation author or same agent, disclose that limitation; do not claim independent human review or spawn reviewers without authorization.

Deliver findings with clause/obligation IDs, source locators, reproduction commands and consequence. State exactly what assurance claim is supported, and block stronger claims until their missing evidence is resolved.

## Catalog and evidence discipline

Read the [shared lifecycle and ledger guide](../spec-driven-development/references/assurance.md) for the executable contract, commands, pilot and limits. Reuse existing target mappings; do not create competing specifications.

Retrieve mathematical facts only through `python3 <catalog>/scripts/catalog.py list --search TERM`, focused `get` sections, `scripts/agent_query.py node ID` or the bounded mathematical-tests helper. Here `<catalog>` is three directories above this skill directory. Follow necessary premises explicitly and resolve truncation. Do not browse catalog storage or generated exports for facts. Prerequisites and hierarchy confer no axioms or proof evidence.

Report required mathematical gaps before acquisition or dependent steps, including searched queries, candidates, mismatch and blocked work. Follow [catalog-use](../mathematical-tests/references/catalog-use.md) and [abstraction-acquisition](../abstraction-acquisition/SKILL.md). A retrieval/backend failure is a tooling blocker: resolve setup first and use a fallback only when the active skill permits it; do not treat it as absent mathematics. Do not silently continue on unsupported assumptions. Preserve provenance and pinned dependencies. Read the [formulation guide](../mathematical-tests/references/formulations.md) only when typed correspondence or witness evidence is needed.
