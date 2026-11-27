# Catalog lookup and decision log

Every repository skill that queries the catalog must maintain a durable task-local lookup log. Read this reference before the first query. Create or extend `mathematical-abstractions-formal-reasoning/<task-id>/catalog-lookup-log.md` in the target project, or index an existing equivalent artifact from that task folder. Keep it outside authoritative catalog records. Update it as queries run and before relying on their results; deliver its path even when the task stops at a gap. This is an agent-maintained artifact, not an automatic transcript emitted by the query tools.

## Deliverable folder and continued use

Deliver derivations and consistency arguments as inspectable artifacts under the target project's `mathematical-abstractions-formal-reasoning/<task-id>/` folder. Create the folder at task start, keep it current during work and deliver its index even when blocked. The folder title describes its purpose; individual files must identify their actual evidence kind. Informal derivations and documentary arguments remain distinct from compiled proofs.

Use this layout, reusing equivalent existing artifacts by explicit links rather than moving or duplicating authoritative files:

| Artifact | Required contents |
| --- | --- |
| `README.md` | Task scope, requirement/obligation IDs, target baseline and affected files, invoked skills and their actual locations, rationale index, dependency links, status, limits and task-specific query examples. |
| `catalog-lookup-log.md` | Executed queries, returned/inspected/selected IDs, mappings, domain inventory, misses and resolutions, as specified below. Explicitly record no queries when no catalog mathematics is needed. |
| `decisions.md` | Indexed substantive choices and reviewable justifications, authority, assumptions and consequences. |
| `derivations.md` | Explicit propositions, definitions, assumptions, mapped catalog premises, intermediate steps and conclusions; link runnable proof sources and compiler/audit results when present. Identify unsupported steps. |
| `consistency.md` | Clauses and their interpretations, explicit consistency arguments or counterexamples, required inputs/nonvacuity, models/encodings, solver commands/bounds and limits. |
| `tests.md` | Claim-to-assertion mappings, test/input/oracle rationale and actual execution evidence; distinguish newly authored tests from existing checks rerun. |
| `evidence/` | Actual retained outputs, models, counterexamples, proof/checker source references, versions and input fingerprints needed to reproduce results. |

Files may link existing detailed artifacts or contain a scoped not-applicable statement with its reason; do not invent a mathematical derivation, consistency claim or test merely to fill the layout. Include failed/inconclusive results. Existing source, mapping and assurance-ledger formats remain authoritative for their roles; the index connects them and does not replace executable admission or proof requirements. Do not copy secrets or unrelated environment output into evidence.

Maintain `mathematical-abstractions-formal-reasoning/PROJECT_MEMORY.md` as the target project's durable navigation note: explain each artifact's role, list task folders and requirement IDs, active decisions, gaps, evidence status and maintenance triggers. It records project knowledge, not a chat transcript. Link existing authoritative memory when the project already has one. Preserve earlier tasks and append supersession/invalidation links.

Before completing the initial task, persist the continued-use rule in the target project's `AGENTS.md` (or its established agent-context entrypoint) and link the memory note and actual installed skill locations. Require agents, before every subsequent modification, to read that note and the affected task index, select and read the relevant `SKILL.md` files, record the invocation/selection and apply their workflows. Reassess selection when the scope changes. If instructions cannot be written, report that persistence gap; do not claim future invocation is ensured. Persistent instructions are the enforcement mechanism here; no host auto-activation hook is installed.

For each subsequent modification, inspect affected derivations, arguments, mappings, lookups and tests before relying on them. Use the [verification-maintenance workflow](../../spec-driven-development/references/verification-maintenance.md), preserving its standalone/lifecycle scope. Record impact and stale dependencies, rerun affected checks, append superseding records and refresh the folder index and project memory. Documentation-only changes still record relevant skill selection and evidence impact; they need neither unrelated catalog queries nor a full lifecycle ledger. An unavailable required skill is a reported workflow gap, not a reason to silently skip it. This project-local persistence does not authorize edits to personal/global memory stores in later tasks.

## Scope and semantic coverage

Record the task, active skill, target revision/relevant local changes, catalog location/revision or fingerprints of CLI-returned records, and retrieval backend. Give log entries stable local IDs so mappings, gap reports and handoffs can reference them. Record later catalog/target changes without erasing earlier results.

Inventory every semantic domain touched by the requested analysis or change, with concrete target locators: specification clauses, API symbols, code paths/lines, model actions, proof obligations or test assertions. Include behavior that is preserved, copied, propagated or implicitly relied on, as well as newly computed behavior. Refine this inventory when inspection exposes additional semantics; do not stop at the main algorithm or the first matching concept.

For example, a compiler rewrite that copies fast-math flags onto rewritten instructions needs a separate lookup and target mapping for those flags and their applicability on the receiving instructions. A mapping for the arithmetic identity alone does not cover flag propagation. Record the actual flags, source and destination instruction kinds, compiler version, applicable conditions and preservation/justification obligation. Likewise inventory relevant numeric/poison semantics, attributes/metadata, memory/alias effects, control flow, exceptions, concurrency or target assumptions when the task touches them. These are inspection prompts, not a requirement to query unrelated domains.

Maintain a coverage table:

| Domain and concrete target locator | Lookup entry IDs | Selected catalog IDs and mapping/obligation reference | Status and remaining gap |
| --- | --- | --- | --- |
| Fill from actual target inspection | | | |

Every touched domain needs retrieved applicable semantics with an explicit target mapping, or an explicit unresolved gap. Explain exclusions against the task boundary; copied behavior is not an exclusion merely because it is unchanged. Coverage is a reviewed inventory, not a claim of mathematical completeness.

Follow the mandatory [complete-fetch and full-claim policy](catalog-use.md#complete-fetches-and-full-claim-reads). Record full-read completion and every truncation recovery; unresolved or abandoned fetches remain incomplete and cannot support dependent work.

## Record each command and result

Log every executed catalog command, including searches, focused concept/operation reads, full claim reads, premise/source/binding queries, availability checks, pagination, retries and permitted backend fallbacks. Distinguish planned commands from executed ones. For each entry retain:

- **Command:** exact invocation/arguments and working directory, backend/interpreter and relevant options (sections, view, budgets, offset/depth). Resolve placeholders to the values actually used. Record execution order and exit status or error.
- **Purpose/target:** semantic domain, question being resolved and concrete target locator or obligation ID.
- **IDs retrieved:** exact stable IDs returned, distinguishing search candidates from records actually inspected and concepts from operations/claims/premises. Short forms may accompany stable IDs. Preserve all returned IDs inline or in a linked bounded result artifact; do not equate returned candidates with selected evidence. Use an empty list when no IDs were returned. An availability check may return no record IDs without being a miss.
- **Outcome:** summarize the relevant result and selection/rejection rationale. Preserve truncation, pagination and depth/budget boundaries and link necessary follow-up entries. Never imply unreturned pages or unresolved premises were inspected.
- **Mapping:** for every relied-on ID, connect its carrier, equality/observations, operations, preconditions/assumptions, definedness and claimed outcomes to the target. Link an existing detailed mapping rather than duplicating it. Record differences, version constraints, partial interfaces and omitted obligations. Candidates not used need a disposition, not a fabricated target mapping.

A compact entry can use these fields:

```text
Lookup ID / active skill:
Command / cwd / backend / catalog baseline:
Purpose / domain / target locator:
Exit status / returned stable IDs / inspected IDs:
Selected IDs / rejected candidates and reasons:
Target mapping or mapping reference / applicability limits:
Outcome / result artifact / requested scope and view:
Full claim reads / query and display truncation / pages and depth boundaries / completion receipts:
Gap / blocked obligation / follow-up lookup or resolution:
```

Keep summaries bounded and preserve the actual returned semantic conditions. Obtain catalog facts and record fingerprints through the permitted CLI/helper; logging does not authorize storage browsing. A command transcript alone lacks the required target interpretation.

## Log misses and unresolved work

Retain unsuccessful lookups as well as successful ones. Distinguish:

- **Search miss:** command completed with no matching IDs; record the query and alternatives tried. One empty keyword search does not establish catalog absence.
- **Semantic mismatch:** candidates exist but their carriers, operations, assumptions or conclusions do not cover the target; record their IDs and the precise mismatch.
- **Missing operation/claim/proof evidence:** an interface exists but a required obligation or current witness is unavailable; record retrieved IDs and the unsupported requirement. A binding or editorial sketch is not a compiled witness.
- **Incomplete retrieval:** required records/premises remain behind pagination, truncation or budget/depth boundaries; record the boundary and required follow-up.
- **Tooling failure:** record the actual command/error and any permitted fallback or repair. Backend failure is not evidence that mathematics is absent.

For each unresolved need, record affected domain/target, blocked dependent work, next action and eventual resolution or explicit conditional status. Keep the original miss and link later successful queries/acquisition evidence; do not rewrite it as a successful original lookup. Apply the [catalog-use gap policy](catalog-use.md): report required gaps to the user before acquisition or further dependent steps. Logging a gap alone does not resolve it or authorize assumptions.

## Decision, argument and test traceability

Keep a reviewable rationale for every substantive task decision, consistency argument and test designed, changed, retained or removed. Link these records to the lookup entries instead of treating a command transcript as an explanation. This is an evidence-backed account of choices, assumptions and results, not a transcript of private internal reasoning. Record concise justifications as work proceeds; do not fabricate an earlier rationale after seeing the outcome. Mark later reconstruction explicitly and identify its supporting artifacts or missing evidence.

Use stable local IDs such as `DEC-001`, `ARG-001`, `TEST-001` and `GAP-001`, or reuse equivalent IDs already present in the task's specification, mapping or ledger. Keep lookup IDs distinct from catalog IDs. Include target and evidence revisions; use symbols and clause/test names alongside line locators so records remain discoverable after lines move. Ordinary formatting steps need no separate decision record, but substantive exclusions, assumptions, candidate rejection, copied semantics, implementation choices and verification choices do.

Maintain the rationale index in the task folder's `README.md` (or link an existing index from it), connecting the log to detailed records:

| Record ID and kind | Question or decision | Target symbols/clauses/tests and revision | Related lookup/catalog/decision/argument/test/gap IDs | Record/evidence locator | Status |
| --- | --- | --- | --- | --- | --- |
| Fill with actual records | | | | | |

For each **decision**, record the question/trigger, chosen action, applicable requirement or user authority, relied-on facts and lookup/mapping IDs, assumptions and applicability limits, and a concise explanation of why the choice meets the obligation. Include material alternatives actually considered and their rejection reasons; do not invent alternatives to fill a field. Record consequences, affected code/models/tests, and validation evidence or what remains unchecked. A choice to leave behavior unchanged or omit a test needs a rationale when it affects the task's assurance claims.

For each **consistency argument**, record the precise claim and clause/obligation IDs, carriers and semantic domains, premise IDs and their source/mapping, the explicit inference or encoding that connects those premises to the conclusion, required-input/nonvacuity checks, and the result's scope. Distinguish an editorial argument, solver result, bounded check, counterexample and compiled proof. Link the actual model/proof/command/output with versions, bounds and assumptions; preserve rejected, inconclusive and contradictory outcomes. A passing structural validator is not a semantic consistency argument.

For each **test**, record its file and stable test name/parameter case, the decision and requirement/obligation/catalog claim it addresses, the defect or counterexample it is intended to detect, why the setup/input/boundary is relevant, how the expected result is justified, and which assertions observe the claim. Identify the oracle's source and independence limits, definedness/preconditions, numeric comparison/tolerance or nondeterminism policy, and uncovered behavior. Link execution commands and actual results separately from test-design intent; mark unrun tests. For removal or merging, name the surviving test and the established overlapping claim-to-assertion coverage, or retain uncertainty. Do not imply that a test proves a universal law.

A compact detailed record can use:

```text
Record ID / kind / active skill / recorded order:
Question or claim / target revision and locators:
Decision or conclusion / status:
Requirement or user authority / premise and lookup IDs:
Semantic mapping / assumptions / applicability limits:
Justification or inference / considered alternatives and rejection reasons:
Affected artifacts / test names and claim-to-assertion mapping:
Evidence commands and artifact locators / actual results and scope:
Related records / remaining gaps / supersedes or invalidates:
```

Record dependencies in both directions through the index: a reader must be able to start with a changed symbol, a consistency claim or a test name and find its rationale and evidence, or start with a requirement/catalog claim and find its decisions, arguments and tests. Explicitly mark requirements with no evidence and artifacts with no justified obligation; resolve or report them before delivery. Reuse detailed existing mappings rather than duplicating them, but keep the index navigable without the chat history.

### Query after completion

Deliver the index path and a few task-specific example queries. Markdown headings, stable IDs and explicit links are sufficient for local lookup; no external service or lifecycle ledger is required. For a task folder `mathematical-abstractions-formal-reasoning/rewrite/`, for example:

```sh
rg -n -F 'DEC-001' 'mathematical-abstractions-formal-reasoning/rewrite/'
rg -n -F 'test_rewrite_flags' 'mathematical-abstractions-formal-reasoning/rewrite/'
rg -n -F 'fast-math' 'mathematical-abstractions-formal-reasoning/rewrite/'
```

Use the actual delivered paths and symbols in task-specific instructions. Follow the matched record's linked premises, mappings and execution evidence when answering why a choice was made. Distinguish the rationale recorded at the time from a new explanation; report absent or stale records as traceability gaps. Do not claim that these text searches perform semantic reasoning or automatically validate the links.

## Handoffs and delivery

Carry the same log, rationale index, linked decision/argument/test records, coverage inventory and unresolved entries through acquisition, mapping, testing, proof, review and maintenance handoffs. Each receiving skill appends its own queries and references existing entries only after checking their target/catalog applicability. Task-local acquired mathematics stays explicitly separate from catalog IDs; promotion must be followed by retrieval of the resulting catalog records.

Before delivery, compare the domain inventory with the actual target change/analysis, reconcile every relied-on ID with its lookup and mapping, and expose unresolved misses or unchecked domains. Check that every substantive decision, consistency argument and test in the delivered work has an indexed rationale and resolvable evidence links; mark stale dependents after target, premise or catalog changes and append superseding records rather than erasing history. Include the log/index path and example queries in the deliverables and gap reports. Standalone work needs this log but does not thereby require a lifecycle ledger. Logs support traceability; they do not establish semantic correctness, exhaustive retrieval or proof coverage.
