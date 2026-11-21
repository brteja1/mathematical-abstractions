---
name: verification-maintenance
description: Recompute evidence impact after code, requirement, catalog, environment or toolchain changes and invalidate stale assurance claims.
---

# Verification Maintenance

Read the existing ledger and change set before editing. Preserve stable requirement/obligation IDs and record deliberate contract revisions. Add new source files, requirements and obligations to traceability; deletion is a contract change, not automatic evidence cleanup.

Run the impact command before and after changes. Follow reverse dependency edges to affected guarantees, tests, proofs, reviews and release artifacts. With a demonstrably complete dependency graph, unchanged independent obligations may keep evidence. Otherwise set dependencyGraphComplete false and invalidate conservatively. Freshness includes declared source artifacts, selected catalog records and explicit premises, helpers, file inventory, expected propositions, checker configuration and toolchain inputs.

Inspect renames, new files, dependency updates, altered assumptions, interface drift and removed outcomes. Mark unmodeled external dependencies explicitly; the runner cannot discover arbitrary command/network/environment reads. List these as environment/toolchain artifacts or reject evidence whose relevant inputs cannot be frozen. Never change dependency pins as incidental proof repair.

Rerun affected checks using the run command, then check admission. Previous pass output cannot override a later failure. Changes during a run invalidate the result. Distinguish missing, failed and stale evidence; explain the invalidation cause and remaining obligations. Do not regenerate or hand-edit receipts to bless old output. Deliver the updated mapping and ledger, impact report, rerun evidence and limitations.

## Catalog and evidence discipline

Read the [shared lifecycle and ledger guide](../spec-driven-development/references/assurance.md) for the executable contract, commands, pilot and limits. Reuse existing target mappings; do not create competing specifications.

Retrieve mathematical facts only through `python3 <catalog>/scripts/catalog.py list --search TERM`, focused `get` sections, `scripts/agent_query.py node ID` or the bounded mathematical-tests helper. Here `<catalog>` is three directories above this skill directory. Follow necessary premises explicitly and resolve truncation. Do not browse catalog storage or generated exports for facts. Prerequisites and hierarchy confer no axioms or proof evidence.

Report required mathematical gaps before acquisition or dependent steps, including searched queries, candidates, mismatch and blocked work. Follow [catalog-use](../mathematical-tests/references/catalog-use.md) and [abstraction-acquisition](../abstraction-acquisition/SKILL.md). A retrieval/backend failure is a tooling blocker: resolve setup first and use a fallback only when the active skill permits it; do not treat it as absent mathematics. Do not silently continue on unsupported assumptions. Preserve provenance and pinned dependencies. Read the [formulation guide](../mathematical-tests/references/formulations.md) only when typed correspondence or witness evidence is needed.
