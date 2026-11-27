# Consistency of repository skills

The 2026-11-21 review covers all 11 repository skill entrypoints, shared catalog/evidence policies and their handoffs. It combines a prose review with executable checks of selected shared decisions. It was performed by the same agent that implemented the lifecycle skills; it is not an independent review or an empirical skill-efficacy evaluation.

Run the dependency-free check and regression suite:

```sh
make check-skills
```

`make test-ai` also runs these checks. The reviewed [contract](../ai/skill-consistency/contract.json) names source clauses, handoff artifacts, source hashes and scenarios. [The checker](../scripts/check_skill_consistency.py) validates the skill inventory/frontmatter, local Markdown file links, clause excerpts and handoff endpoints. It rejects changed or added normative skill Markdown until the review baseline is deliberately updated. Hashes cover supporting Markdown as a drift boundary; they do not certify every example or sentence as semantically verified. Markdown fragments, external URLs, host registration and executable-tool interfaces are not validated by the link check.

## Consolidated entrypoints

Assurance review is a mode of implementation-conformance; verification maintenance is a reference workflow of spec-driven-development. Their traceability, independent-review disclosure, impact/invalidation and rerun requirements remain intact. Maintenance-only requests do not authorize a full lifecycle. Evaluation cases 16 and 17 retain their tasks and criteria and now select these host skills; no efficacy runs are claimed. The handoff graph records skill boundaries; maintenance is an internal orchestrator step.

## Findings and repairs

| Finding | Repair and reviewed scope |
| --- | --- |
| Requirements formalization unconditionally delivered a lifecycle ledger, while the orchestrator limits lifecycle machinery to authorized scope. | Standalone requirements retain traceable obligations in their specification; lifecycle work uses the shared ledger. Rules P2/P5 and standalone/lifecycle scenarios cover the selected authorization decisions. |
| Six lifecycle skills grouped retrieval failures with missing mathematics. | Separate tooling/setup blockers from acquisition; fallback remains conditional on the active skill. P1 models retrieval readiness after any permitted fallback. |
| Unsupported external verifier results were automatically labeled bounded/review. | Preserve the actual evidence kind; unsupported results remain blocked from this runner's automated proof admission. P4 checks supported, fresh, unconditional evidence. |
| Discovery could label finite checks simply “satisfied.” | Evidence labels distinguish proofs, finite exhaustive checks, samples, conditional results and unchecked obligations. Comparator comparability is separate from determinism; comparator results need sign reversal, not matching magnitudes. Floating-point aggregation keeps its numeric-semantics caveat. |
| Model-checking guidance promised minimal traces, stuttering cycles and broad small-scope guarantees. | Require backend evidence for minimality, allow nonstuttering cycles, state finite bounds and avoid population guarantees. Removed an unsupported TLC symmetry snippet. No backend execution is asserted by this edit. |
| The ticket-lock Python example claimed deadlock/liveness checks but only checks a bounded safety predicate. | Correct prose, docstring and success output; execute both normal and duplicate-ticket mutation cases in regression tests. This does not execute the TLA+ model. |
| Mapping template requested source hashes without identifying the permitted retrieval path. | Record fingerprints of CLI-returned catalog records; storage browsing remains prohibited. |

The handoff table records compatible artifact transfers: requirements/clauses, catalog-to-API mapping, checked model actions, proof trust boundaries, acquisition verification plus retention choice, evidence impact and review findings. It does not compel every skill to run on every task. Existing mathematical-tests retrieval tests, assurance-runner tests and evaluation-fixture tests remain responsible for their own executable interfaces.

The requirements handoff now includes gaps exposed by reviewing the draft for observable outcomes, relevant failure behavior and measurable promises. The lifecycle skill also reviews the implementation plan against the contract in both directions, using the existing mapping and project constraints. These reviews use the existing clarification, authorization and evidence policies. The finite check below models those policies and leaves checklist adequacy and plan coverage to review. The additions draw on GitHub Spec Kit's [requirements checklist](https://github.com/github/spec-kit/blob/main/templates/commands/checklist.md), [task template](https://github.com/github/spec-kit/blob/main/templates/tasks-template.md), and [cross-artifact analysis](https://github.com/github/spec-kit/blob/main/templates/commands/analyze.md).

## Catalog lookup logging review (2026-11-27)

All 11 skill entrypoints now require the shared [lookup log](../ai/skills/mathematical-tests/references/catalog-lookup-log.md) before catalog queries. The catalog-use policy and implementation-map template connect it to existing artifacts. Each handoff carries the same log, domain inventory and unresolved entries; standalone tasks retain a log without requiring a lifecycle ledger. This review was performed by the implementing agent.

The reviewed requirements cover executed commands and their returned stable IDs, candidate/inspected/selected distinctions, concrete target mappings, and unsuccessful queries. Domain coverage follows the actual target semantics, including copied fast-math flags and other propagated attributes; an arithmetic mapping alone does not discharge flag obligations. Misses, incompatible candidates, missing claims/witnesses, incomplete retrieval and tooling failures remain distinct. Existing gap reporting, acquisition/retention choices, progressive retrieval and proof limits still apply.

Contract clause anchors cover the shared logging requirement and its route from every entrypoint; source hashes include the new reference. Handoff metadata includes log transfer. These structural checks do not validate the contents of future task logs or prove that agents identify every semantic domain. The finite policy encoding below is unchanged; it does not model log completeness or semantic coverage. No behavioral skill-efficacy evaluation is claimed.

The logging review also covers an indexed rationale for each substantive decision, consistency argument and test. Stable local IDs, target symbols and evidence links support later queries in both directions; missing, reconstructed and stale rationales remain explicit. The records contain reviewable justifications, not private internal reasoning. Entry-point anchors and handoffs now carry this requirement. The checker verifies these documentary anchors, not the truth or completeness of future rationale records.

## Reasoning deliverables and continued-use review (2026-11-27)

The implementing agent reviewed all eleven entrypoints, the shared log/artifact policy, target-agent persistence rule, mapping template and maintenance handoffs. Each entrypoint requires `mathematical-abstractions-formal-reasoning/` deliverables, project memory and persistent routing. The shared policy defines explicit derivations, consistency arguments, test rationale, runnable evidence and artifact roles. Every later modification selects relevant skills and refreshes affected evidence; this is an instruction requirement, not an installed auto-activation hook. Standalone documentation work does not acquire a lifecycle ledger or unrelated mathematical obligations. Existing gap, provenance, retention-choice and proof-admission constraints remain unchanged.

Reviewed source hashes and exact clause anchors cover these additions; all handoffs preserve the task folder and memory/routing context. The finite Boolean policy below remains unchanged because artifact packaging and future instruction compliance are not modeled by it. Structural checks validate the anchors and declared handoffs, not future invocation or the truth of delivered arguments. The task's actual evidence and documentary argument are indexed in `mathematical-abstractions-formal-reasoning/2026-11-27-catalog-traceability/README.md`.

## Complete-fetch review (2026-11-27)

All eleven entrypoints now require full claim reads, recovery of query and tool-display truncation, and a ban on piping concept/claim fetches through `head`, `tail`, `cut` or equivalent discarding filters. Shared catalog-use/retrieval/log policies require completion receipts, all selected pages and depth-boundary resolution; unresolved reads block reliance. Narrow selection remains allowed, and broad abandoned fetches remain explicitly incomplete. The implementing agent reviewed the affected clauses and all handoffs, which carry these receipts. New exact anchors and selectively refreshed hashes check instruction presence; the finite encoding is unchanged and does not enforce actual agent reading or shell behavior.

## Finite semantic check

Catalog-backed mapping uses `urn:csabs:concept/PropositionalFormula`, `urn:csabs:concept/PropositionalLogic`, and `urn:csabs:theorem/PropositionalLogic-finite-truth-table`. The theorem and its four direct premises (formula induction/substitution, truth semantics and entailment) were retrieved through `scripts/agent_query.py node ID`; they are editorial mathematical records, not claimed compiled witnesses. No new catalog mathematics is needed or added.

Carrier: the declared finite Boolean atom names. Formula equality: syntax-tree equality, distinct from equivalence across all valuations. `not`, `and`, `or`, `implies` and `iff` map to classical truth functions; each scenario fixes all input atoms. `evaluate(expr, valuation)` interprets the finite AST; `check_policy(contract)` enumerates every input/output valuation. There is no use of Python `eval` or a solver timeout. Rule source locators are exact excerpts in the contract.

The encoding checks:

- Joint satisfiability and outcome coverage for **every** assignment of the ten input Booleans, separately from scenario expectations.
- Required scenario conclusions across **all** allowed outcomes; permitted implementation, promotion and proof outcomes must also have witnesses.
- Retrieval readiness and explicit gap resolution/conditional continuation before dependent work; scope authorization before implementation; verified acquisition plus explicit promotion choice before promotion.
- Supported/fresh proof admission without conditional assumptions; lifecycle-ledger requirements scoped to lifecycle work.

`retentionChosen` means the acquisition workflow's explicit retention choice is complete; `promotionAuthorized` means that choice specifically permits promotion. `retrievalReady` means required retrieval succeeded, including any fallback permitted by the active skill. `supportedProof` and `proofFresh` abstract the runner's more detailed validation; this model does not replace it. `continueDependent` means the mathematical prerequisite permits continuation, not that all other task decisions or assurance gates have passed. `conditionalChosen` means relevant assumptions are explicitly conditional; the conservative rule blocks unconditional proof admission in that context. A math gap is reported before this decision point; independent work and the earlier reporting event are outside this synchronous model.

These human-written formulas do not establish complete correspondence with natural-language instructions, arbitrary skill combinations, workflow liveness, mathematical correctness of produced artifacts or future agent compliance. A passing source snapshot plus this encoding supports only the reviewed findings and declared finite decisions.

## Maintaining the review

When a check reports source drift, inspect the changed clauses and affected handoffs. Revise the encoding/scenarios if behavior changed, recheck original scope and evidence distinctions, then deliberately update only the reviewed SHA-256 entries in `sourceHashes`. For new skill Markdown add its reviewed baseline; for a new skill also update the inventory and applicable handoffs. There is no automatic “bless current sources” command. The contract and checker are ordinary version-controlled review artifacts, not tamper-proof attestations.

Regression tests inject contradictory policies, missing permitted outcomes, weakened proof guards, changed sources, missing skills/handoffs and broken links. These demonstrate detection within this encoding; they do not establish real model skill efficacy.
