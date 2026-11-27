---
name: requirements-formalization
description: Turn stakeholder intent into traceable, explicit mathematical software requirements before implementation.
---

# Requirements Formalization

Preserve the supplied intent and source locators. Assign stable requirement IDs and label origins as human, external, derived or proposal. Extract required scenarios, admissible inputs, observable outputs/errors, state changes, progress, resource and environment promises. A suggested policy is not an accepted stakeholder requirement.

For substantial changes, review the draft requirements before mapping them to mathematical abstractions. Check that each required scenario specifies its starting conditions, trigger and observable outcome, including relevant failures and recovery. Check that stated performance and resource promises have measurable targets and operating conditions. Record gaps by requirement ID and source locator in the existing specification or review notes. Route material ambiguities through the clarification and validation process below. Record suggested thresholds or defaults as proposals.

Map each requirement through focused catalog queries to carriers, equality, operations, domains and assumptions. Write numbered normative clauses and examples, including empty/boundary cases, failures, divergence and concurrent observations when relevant. Separate definitions from assumptions and claims requiring evidence. A domain restriction must not quietly remove a required scenario.

Use specification-consistency for joint satisfiability, input/output coverage and nonvacuity. Retain contradictions and meaningful alternatives; ask only for decisions that block dependent work. Keep independently resolved work moving. Record a validation receipt for each requirement, with reviewer, rationale and pending/accepted/rejected status; never invent stakeholder acceptance. When authorized to formulate a proposal, label agent acceptance as a proposal review with its limited scope.

Deliver the source-to-clause mapping, specification, required scenarios, unresolved decisions and traceable obligations. For an authorized lifecycle task, record these in the shared obligation ledger; a standalone requirements task may retain them in its specification without creating a lifecycle ledger. Check reverse traceability: every source requirement and every normative clause must have an owner. The gate checks declared mappings and receipts, not whether natural language fully expresses the user's intent.

## Catalog and evidence discipline

Read and maintain the [catalog lookup log](../mathematical-tests/references/catalog-lookup-log.md) whenever querying the catalog. Record actual commands, retrieved IDs, target mappings and misses; cover every semantic domain touched, including preserved or copied flags/attributes. Keep indexed rationales for substantive decisions, consistency arguments and tests, linked to requirements, lookups and validation evidence. Deliver the task-local log and carry it through skill handoffs. Read every fetched claim in full using `--view full`; resolve all fetch truncation before relying on results. Never pipe a claim or concept fetch through `head`, `tail` or `cut`. Deliver derivations, consistency arguments and linked evidence under `mathematical-abstractions-formal-reasoning/`; maintain its project memory note and persistent agent-context routing for subsequent modifications.

Read the [shared lifecycle and ledger guide](../spec-driven-development/references/assurance.md) for the executable contract, commands, pilot and limits. Reuse existing target mappings; do not create competing specifications.

Retrieve mathematical facts only through `python3 <catalog>/scripts/catalog.py list --search TERM`, focused `get` sections, `scripts/agent_query.py node ID` or the bounded mathematical-tests helper. Here `<catalog>` is three directories above this skill directory. Follow necessary premises explicitly and resolve all fetch truncation. Do not browse catalog storage or generated exports for facts. Prerequisites and hierarchy confer no axioms or proof evidence.

Report required mathematical gaps before acquisition or dependent steps, including searched queries, candidates, mismatch and blocked work. Follow [catalog-use](../mathematical-tests/references/catalog-use.md) and [abstraction-acquisition](../abstraction-acquisition/SKILL.md). A retrieval/backend failure is a tooling blocker: resolve setup first and use a fallback only when the active skill permits it; do not treat it as absent mathematics. Do not silently continue on unsupported assumptions. Preserve provenance and pinned dependencies. Read the [formulation guide](../mathematical-tests/references/formulations.md) only when typed correspondence or witness evidence is needed.
