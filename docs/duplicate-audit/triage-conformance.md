# Semantic triage conformance and pilot

Contract: DT-1, [DT-01–DT-12](triage-spec.md). Implementations:
`scripts/triage_duplicates.py` and the shared `Audit.iter_scored_pairs` stream.
This work used the repository specification-consistency, implementation-mapping,
mathematical-tests and implementation-conformance skills. Current hashes and
executed commands are recorded in triage-evidence.json.

## Actual pilot

The user chose this assistant as the initial reviewer. Ten ranked pairs were
exported with their source records, owner scopes and direct context. This
assistant read those packets and supplied rationale, carrier/equality/operation/
assumption mappings and exact citations, then imported the ten results through
the production validation/cache protocol. No other model service was invoked.
The exact model version was not exposed and is explicitly recorded as unavailable.

Results: five distinct-law comparisons and five floating-point-format variants;
zero duplicate proposals, zero unresolved/failed cases in the ten reviewed pairs.
The 5,528 unselected candidates remain unreviewed. The report is
[triage-pilot/report.md](triage-pilot/report.md); machine provenance and evidence
are retained in that workspace. The pilot is a ranked convenience sample, not a
random sample, independent calibration set, or precision/recall measurement.
Automatic suppression is disabled and human receipts are unchanged.

## Obligation review

| Obligation | Evidence and semantic mapping | Scope/limits |
| --- | --- | --- |
| T-01 | Original DA acceptance tests plus shared selector extraction; unchanged 5,538 candidate count and exact score/order; selected/unselected count tests | DA-P1 heuristics preserved, not semantic equivalence detection |
| T-02 | Exact source capsules, per-record fingerprint cache, source-change/corruption tests and explicit unexpanded-context markers | No guessed carrier extraction, inherited laws or Lean proof preload |
| T-03 | Both-endpoint quote checks, complete semantic mappings, immutable/idempotent imports, independence/disagreement/missing-context tests | Citation existence is checked, source entailment and real reviewer independence are not proved |
| T-04 | Synthetic executable adapters test stdin/stdout protocol, budget/resume, malformed output, timeout and oversized-context failure | Fixture execution is not model-quality evidence; adapter is trusted, stdout captured before size checking |
| T-05 | Markdown report tests for correct count partitions, relative links, collapsed distinctions, unresolved/duplicate actions and second-review failures | No 5,538-pair review is claimed; JSON is optional detailed evidence rather than the required review interface |
| T-06 | Independent hand-calculated metric oracle: coverage 3/4, exact 1/3, retain precision 1/2, duplicate precision 0/1 | Labels are synthetic fixtures; no independent accuracy claim or automatic suppression enabled |
| T-07 | Plan hash/version/snapshot checks, immutable cached payload hashes, foreign/symlink/protected-workspace tests | Hashes detect accidental drift, not malicious provenance forgery; no adversarial filesystem transaction guarantee |

Tests map to FiniteSet exact ID/tuple membership, Relation without transitive
candidate equivalence, and TotalOrder exact ranking, using the existing audit
mapping. The FiniteSet axiom was retrieved through a bounded ONTFS query with one
complete record and no truncation. The production tools use captured authoritative
Markdown independently of ONTFS. Relation/TotalOrder citation gaps are preserved;
no new graph facts, source claims, Lean witnesses or dependency pins were added.

## Issues addressed during review

* Candidate enumeration is shared with the audit instead of reimplementing its
  score/receipt rules in the triage layer.
* Source capsules retain full selected assumptions/scope text; missing fields and
  unexpanded context are explicit. Oversized requests fail rather than clip it.
* The independent stage cannot use the declared primary identity/version; a later
  primary selection also cannot re-label its own earlier result as independent.
  Both missing context and independent failures remain visible.
* Imported results cannot call themselves human receipts. Labels are not sent to
  model adapters. Exact quotes must cover both original endpoint records.
* Export bundles and cache objects are content-addressed and immutable; mutable
  reports and plans are atomic workspace-local outputs. Conflicting review
  imports require a different reviewer version.
* An integrity hash and coverage checks prevent accidentally edited plans from
  silently changing which records were reviewed. Data/tool/policy drift requires
  prepare again, while identical effective packets may reuse past judgments.

No remaining violation was identified within this inspected and tested scope.
This is finite software evidence, not a universal refinement proof, mathematical
model-equivalence proof, or independently measured detector efficacy. Synthetic
adapters do not establish that a particular external model service is configured
or working. The current assistant pilot validates only the actual ten packet
reviews and the resulting report/import workflow.
