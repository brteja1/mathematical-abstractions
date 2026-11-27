# Verification maintenance

Use the catalog and gap-handling policies in the parent [skill](../SKILL.md). Read the [shared ledger guide](assurance.md) when inspecting executable admission, freshness or proof-profile evidence.

Before any modification, read `mathematical-abstractions-formal-reasoning/PROJECT_MEMORY.md`, the affected task index and the relevant skill entrypoints; record invoked skill paths and the selection rationale. Follow the [shared artifact policy](../../mathematical-tests/references/catalog-lookup-log.md#deliverable-folder-and-continued-use). For standalone work without a ledger, retain a task-local impact record linking changed inputs to affected derivations, consistency arguments, mappings, lookups and tests. Mark stale evidence, rerun applicable checks and update the index and memory; do not create a lifecycle ledger solely for maintenance. The ledger commands below apply when a ledger exists.

Read the existing ledger, when present, and change set before editing. Preserve stable requirement/obligation IDs and record deliberate contract revisions. Add new source files, requirements and obligations to traceability; deletion is a contract change, not automatic evidence cleanup.

Run the impact command before and after changes. Follow reverse dependency edges to affected guarantees, tests, proofs, reviews and release artifacts. With a demonstrably complete dependency graph, unchanged independent obligations may keep evidence. Otherwise set dependencyGraphComplete false and invalidate conservatively. Freshness includes declared source artifacts, selected catalog records and explicit premises, helpers, file inventory, expected propositions, checker configuration and toolchain inputs.

Inspect renames, new files, dependency updates, altered assumptions, interface drift and removed outcomes. Mark unmodeled external dependencies explicitly; the runner cannot discover arbitrary command/network/environment reads. List these as environment/toolchain artifacts or reject evidence whose relevant inputs cannot be frozen. Never change dependency pins as incidental proof repair.

Rerun affected checks using the run command, then check admission. Previous pass output cannot override a later failure. Changes during a run invalidate the result. Distinguish missing, failed and stale evidence; explain the invalidation cause and remaining obligations. Do not regenerate or hand-edit receipts to bless old output. Deliver the updated mapping and ledger, impact report, rerun evidence and limitations.

Deliver updated reasoning artifacts and project memory alongside the existing mapping/ledger when applicable. Preserve historical results and link their replacements; persistent agent-context routing must continue to require relevant skill invocation for later changes.
