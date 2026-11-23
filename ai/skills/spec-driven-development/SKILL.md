---
name: spec-driven-development
description: Coordinate requirements, consistency, implementation, composition, proofs, tests and assurance maintenance using a task-local evidence ledger. Use its maintenance workflow to update evidence after changes.
---

# Spec Driven Development

Determine requested scope and inspect the target instructions and existing contracts. Do not turn a small edit into an unsolicited formalization project. For an authorized lifecycle task, create or extend one versioned task-local ledger, with artifacts beside the target software and outside authoritative catalog records.

Route intent to requirements-formalization, conflicts to specification-consistency, representation/API decisions to implementation-mapping, and required mathematical gaps to abstraction-acquisition after reporting them. Resolve blocking decisions without repeatedly requesting approval already granted. Implementation is authorized only within the user's requested scope and resolved contract.

For multi-step lifecycle changes, review the implementation plan after mapping and before coding. Reuse the target project's plan or task list when available. Map each task to its requirement or obligation IDs, or to the tasks that need it for shared setup. Record task dependencies, applicable project constraints and compatibility guarantees. Group work into independently verifiable increments where feasible and identify the check for each increment. Verify that every in-scope implementation and evidence obligation has planned work, and that every task is justified by the contract or an explicit prerequisite. Resolve blocking gaps in the plan or route contract questions through the existing validation workflow. Continue independently resolved work within scope.

Implement resolved obligations. Use compositional-verification for component connections, implementation-refinement for actual source correspondence, mathematical-tests for behavior tests and formal-model-checking for concurrent models. Run supported executable checks and retain their exact inputs and scope. Tests, bounded exploration, review and proof are different evidence kinds.

Before delivery, use implementation-conformance in assurance review mode to challenge the contract and result. Follow the [verification maintenance workflow](references/verification-maintenance.md) after each meaningful change. Admit only when every declared required check has fresh successful evidence, requirements have honest validation receipts and blocking decisions are resolved. Unsupported proof profiles and missing mathematics remain blockers, not assumed success.

Deliver the specification/mapping, implementation, ledger, runnable evidence, remaining decisions and precise trust boundary. Do not promise correctness relative to unstated human intent or uncontrolled deployment environments. This orchestrator coordinates existing tools; it does not supply a universal verification backend.

## Maintenance-only scope

For a request to refresh evidence or assess change impact, read [verification maintenance](references/verification-maintenance.md) and the existing ledger/change set. Perform the requested impact and rerun work without restarting requirements formalization or expanding into a full lifecycle task. Report absent traceability or unresolved inputs explicitly.

## Catalog and evidence discipline

Read the [shared lifecycle and ledger guide](../spec-driven-development/references/assurance.md) for the executable contract, commands, pilot and limits. Reuse existing target mappings; do not create competing specifications.

Retrieve mathematical facts only through `python3 <catalog>/scripts/catalog.py list --search TERM`, focused `get` sections, `scripts/agent_query.py node ID` or the bounded mathematical-tests helper. Here `<catalog>` is three directories above this skill directory. Follow necessary premises explicitly and resolve truncation. Do not browse catalog storage or generated exports for facts. Prerequisites and hierarchy confer no axioms or proof evidence.

Report required mathematical gaps before acquisition or dependent steps, including searched queries, candidates, mismatch and blocked work. Follow [catalog-use](../mathematical-tests/references/catalog-use.md) and [abstraction-acquisition](../abstraction-acquisition/SKILL.md). A retrieval/backend failure is a tooling blocker: resolve setup first and use a fallback only when the active skill permits it; do not treat it as absent mathematics. Do not silently continue on unsupported assumptions. Preserve provenance and pinned dependencies. Read the [formulation guide](../mathematical-tests/references/formulations.md) only when typed correspondence or witness evidence is needed.
