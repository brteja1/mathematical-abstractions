# Semantic triage experiment: contract and mapping

Version DT-1, 2026-11-20. This stage consumes DA-P1 candidates; it does not change
DA-P1 scores, human receipts, mathematical records or source/proof status.

## Normative experiment contract

**DT-01 — Scope.** Preparation runs the existing authoritative snapshot/preflight
and DA-P1 pair selector. Select either the first N actionable pairs in exact audit
rank order (default 50) or explicitly all pairs. Preserve the qualified/actionable,
selected and unselected counts. A report must distinguish not-selected pairs from
selected-but-unreviewed pairs; neither is a successful semantic review.

**DT-02 — Source capsules.** Extract a reusable capsule per selected record from
readable mathematical fields, scope, assumptions, operations, direct axioms,
direct premises, owner scope and direct source metadata. Do not invent absent
carriers/equality or infer laws through hierarchy. List links not expanded in the
packet. Cache the source-derived capsule by DT version and DA review fingerprint.
These are source extracts, not a claim that natural-language mathematics has been
parsed into an executable theory. Do not preload Lean proof text.

**DT-03 — Freshness.** A plan binds the current catalog digest, aliases/registry
hashes and candidate fingerprints. Subsequent operations verify that snapshot.
Each packet binds canonical pair, capsules, source extracts, rule hints and prompt
version. Review cache keys additionally bind reviewer identity/version and stage.
Changes to context, aliases, prompt or reviewer invalidate reuse. Immutable cache
objects must have their content hash verified; conflicting imports require a new
reviewer version, not overwriting earlier judgments. Refreshing a plan may retain
old content-addressed caches, but stale plan operations must fail explicitly.

**DT-04 — Rule hints.** Deterministic hints may report an explicitly documented
specialization, equal nonempty normalized statement text, different claim roles,
or differing explicit scopes/assumptions. These are observable evidence, not
mathematical verdicts. They never merge records, skip required AI review or
authorize suppression. Pair relations are not closed transitively.

**DT-05 — Review protocol.** A reviewer receives only the original packet and the
versioned instructions, not expected evaluation labels or a previous review's
decision. Return `decision` from same_meaning/specialization/semantic_variant/
distinct/insufficient_evidence, a concise `rationale`, `mapping` strings for
carriers/equality/operations/assumptions, a `differences` string list,
`missingContext` ID list, and `evidence` entries {recordId,field,quote}. Every
evidence quote must be an exact nonempty substring of a string leaf of that
packet field. Evidence must cover both endpoint records. Structural validation
checks citations exist, not that they entail the classification. No model
confidence number is interpreted as proof or calibrated probability.

**DT-06 — Runner and imports.** Support an explicit trusted model-adapter argv
array (JSON), with canonical JSON request on stdin and one JSON result on stdout;
do not invoke a shell or silently select a cloud service. Require reviewer ID and
version. Per-run budgets bound attempted pairs; per-call timeout and character
limits are explicit. Oversized context is unresolved, never silently truncated.
Adapter failures/malformed results are recorded as failures and can be retried;
they are not classifications. The adapter is a user-configured trusted program,
not a filesystem sandbox. Imported assistant-session results follow the identical
validation/cache protocol, with truthful identity/version and provenance. They
must not be labeled human decisions or independent ground truth.

**DT-07 — Independent checks.** Same-meaning proposals always remain actionable.
An optional independent stage uses the original packet, not the primary verdict.
Preserve both judgments and reviewer metadata. Agreement is additional evidence,
not a proof or merge authorization; conflicting verdicts are escalated. Do not
label the same reviewer identity/version as independent. Any review with requested
missing context is unresolved. A source gap remains a source gap.

**DT-08 — Reports.** Generate Markdown with proposed duplicates, unresolved cases,
and expandable suggested distinctions, using explanations and actual record links.
Clearly show model-reviewed, failed, pending, not-selected and total counts.
Keep all machine proposals in a separate JSON artifact. DT-1 does not automatically
quiet DA-P1 candidates or write human receipts. Suggested distinctions may be
collapsed for readability, but must remain counted and inspectable. Catalog edits
and migrations require separately reviewable changes.

**DT-09 — Evaluation.** An optional labels file contains pair, expectedDecision,
and labeler/independence provenance. It is read only by evaluation, never sent to
the reviewer. Report coverage, exact agreement, a confusion table and precision
among predicted distinctions/duplicates with their denominators. Missing results
are unreviewed, not correct predictions. Synthetic fixture checks and labels
written by the reviewing assistant are not independent accuracy evidence. No
automatic-suppression policy is enabled by DT-1, even after a successful fixture
test. Independent labels are needed before proposing such a later policy.

**DT-10 — Storage/effects.** All writes occur in an explicitly selected tool-owned
workspace outside the audit's protected graph directories, hidden paths and inputs.
Create a marker only in a new/empty directory. Reject foreign nonempty workspaces
and symlink files/directories. Use exclusive immutable-cache writes and atomic
replacement of only the tool's named mutable outputs. Never write catalog data,
human receipts, Lean bindings, runtime RDF or another workspace. Source files are
captured and rechecked before committing a new plan/review/report. External model
effects/costs cannot be rolled back. No network is used by the default prepare,
export, import, report or evaluate commands.

**DT-11 — CLI.** `scripts/triage_duplicates.py` has prepare/export/import/review/
report/evaluate subcommands, each requiring `--workspace`. Preparation accepts
`--limit N` or `--all`, `--threshold`, `--aliases`, `--registry`. Review requires
`--review-command` as JSON argv, `--reviewer-id`, `--reviewer-version`; accepts
`--stage primary|independent`, `--budget` (default 10), `--timeout` (default 45
seconds), `--max-input-chars` (default 40000). Export/import accept the same
reviewer identity/stage to make assistant-session work reproducible. A successful
command returns 0, invalid/stale input 2, and I/O/resource/adapter failure 3;
review failures are retained and reported. Partial progress never implies full
coverage. Current-assistant pilot reviews are explicitly requested by the user.

**DT-12 — Verification.** Test pair-locality, freshness, capsule reuse, citation
validation, budget/resume, timeout/failure handling, independent-stage isolation,
report coverage/link safety, workspace protection, calibration label separation
and exact metric denominators. Preserve a small actual pilot and reproducible
test evidence. No universal mathematical-equivalence proof is claimed.

## Implementation mapping

| Obligation | Clauses | API | Evidence |
| --- | --- | --- | --- |
| T-01 | DT-01,04 | existing Audit.iter_scored_pairs; prepare | Audit-regression membership/order tests; selection counts |
| T-02 | DT-02–03 | capsule, packet, cache keys | Exact source extracts, visited-context limits, source-fingerprint changes |
| T-03 | DT-05–07 | validate_review, import_reviews, run_reviews | Quote/endpoint coverage, missing context, immutable imports, independent isolation |
| T-04 | DT-06 | run_reviews adapter boundary | Trusted synthetic adapter, timeout/error injection, budget/resume |
| T-05 | DT-08 | build_report | Exact partition of scope; human-readable evidence and real links |
| T-06 | DT-09 | evaluate | Independent hand-calculated metric oracle and missing-result cases |
| T-07 | DT-03,10–11 | workspace, snapshot validation, storage helpers | Stale/foreign/symlink/protected-input checks |

Reuse the repository specification-consistency, implementation-mapping,
mathematical-tests and implementation-conformance skills. Retrieve existing
FiniteSet/Relation/TotalOrder semantics for exact identities, nontransitive pair
relations and ordering, as in mapping.md. DT-1 adds product protocol definitions,
not new mathematical catalog claims. The production pipeline uses authoritative
Markdown; bounded ONTFS retrieval is used only for test rationale. Neither a
claim's source citation nor a passing test makes an AI judgment a proof.

The initial pilot is this assistant's review of ten high-ranked pairs. Its
classifications are machine proposals, with no independent calibration or
second-review evidence. Synthetic protocol/evaluation fixtures must be reported
separately from actual pilot results and future independently labeled studies.
