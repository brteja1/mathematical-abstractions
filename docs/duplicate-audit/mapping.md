# Duplicate audit: semantic and implementation mapping

Mapping version 0.2; normative contract: [spec.md](spec.md), DA-01–DA-18.
Implementation: [audit_duplicates.py](../../scripts/audit_duplicates.py).
The original specification-stage baseline is retained in [context.json](context.json).
Current implementation/specification hashes and results are in
[implementation-evidence.json](implementation-evidence.json).

## Skills and retrieval

Applied repository workflows:

* [specification-consistency](../../ai/skills/specification-consistency/SKILL.md):
  clause IDs, input coverage, nonvacuity, bounded evidence and explicit omissions;
* [implementation-mapping](../../ai/skills/implementation-mapping/SKILL.md):
  carrier/equality/API obligations and separation of required behavior from design choices;
* [mathematical-tests](../../ai/skills/mathematical-tests/SKILL.md):
  expected pair sets, exact rational arithmetic, ordering and targeted failure cases;
* [implementation-conformance](../../ai/skills/implementation-conformance/SKILL.md):
  reverse traceability and review of code against every mapped obligation.

Retrieval used dependency-free `scripts/catalog.py` and `scripts/agent_query.py`
against authoritative records. `python3 scripts/catalog.py check` returned 265
concepts, 2507 nodes, no errors. No ONTFS projection was rebuilt or queried. The
selected mathematics already exists; this task introduces product definitions
(features, fingerprints, receipts), not missing mathematical catalog concepts.
No abstraction-acquisition or graph promotion is required. For implementation
testing, bounded ONTFS/SPARQL queries retrieved FiniteSet-carrier-extensionality
and TotalOrder-comparable individually; both returned one complete record with
no pagination or truncation. The production audit uses only captured Markdown
and standard-library code, independently of this test-design retrieval backend.

## Mathematical interpretation

| Concern | Specification meaning | Proposed representation | Limits |
| --- | --- | --- | --- |
| Finite map G | Unique IDs and authoritative JSON payloads | dict[str, JSONValue] plus source ownership | Validate before indexing; never silently overwrite duplicate IDs |
| Finite sets U,E,V and features | Extensional membership, no repeated pairs/tokens | set/frozenset of strings or 2-tuples | Exact string identity; normalization is evidence only |
| Candidate relation | A symmetric, irreflexive pair relation within each family | Canonical tuples with ordered endpoints | Not transitive; no equivalence-class union-find |
| Score | Exact rational weighted Jaccard followed by one floor | integer counts and fractions.Fraction | No learned probabilities or floating-point rounding |
| Rank | Lexicographic total order on (-score,ID,ID) | sorted tuples using Python str code-point order | Environment/normalization versions reported |
| Receipt context | Equality of canonical captured records within declared closure | Canonical JSON + SHA-256 | Computational collision-resistance assumption; no semantic proof |
| Review state | Total classification of missing/stale/current decisions | Explicit five-state result | No mutating state transition performed by the command |
| Environment | Stable finite inputs; sufficient resources; ordinary local I/O | Captured bytes, final manifest check, exclusive output creation | No adversarial filesystem transaction or performance guarantee |

## Selected catalog records and applicability

| Stable ID / locator | Task mapping | Premises and provenance |
| --- | --- | --- |
| `urn:csabs:concept/FiniteSet`, concepts/FiniteSet.md | U, E, feature sets and selected candidate sets are finite sets with exact element equality | Direct sources mathlib-finset-defs and mathlib-finset-insert; catalog editorial formulation |
| `urn:csabs:axiom/FiniteSet-carrier-extensionality` | Pair/set equality means equal members, independent of input enumeration | Finite carrier and identity equality; directly sourced as above |
| `urn:csabs:axiom/FiniteSet-constructors` | Empty selection and insertion of repeated selector/pair leave membership well-defined | Exact ID or tuple equality, no bag multiplicity; directly sourced as above |
| `urn:csabs:concept/Relation`, concepts/Relation.md | E and candidate pairs are subsets of typed products | Base relation imposes neither transitivity nor equivalence; legacy-source-missing retained |
| `urn:csabs:operation/relation-inverse` | Reversing pair presentation does not change canonical identity | Same-family distinct endpoints; relation concept's citation gap remains open |
| `urn:csabs:concept/TotalOrder`, concepts/TotalOrder.md | Rank keys use the explicit lexicographic order of integers then ID strings | Product-order instantiation is an editorial design argument, not a registered theorem witness |
| `urn:csabs:axiom/TotalOrder-comparable` | Every two rank keys are comparable | Chosen integer/code-point carriers; legacy-source-missing |
| `urn:csabs:axiom/TotalOrder-antisymmetric` | Equal keys identify the same canonical pair when score agrees | Unique stable IDs and canonical pair representation; legacy-source-missing |

No prerequisite/hierarchy edge transfers an axiom. These records name relevant
interfaces; the DA clauses independently define the command's behavior. No Lean
formulation or compiled catalog witness is relied upon, and finite checks do not
close any citation gap or prove refinement.

## Implementation obligations

The API names below resolve to the current implementation. Clause behavior is
unchanged from DA-P1. Test names and evidence limits are recorded in conformance.md.

| ID | Clauses / catalog mapping | Proposed API boundary | Required acceptance evidence |
| --- | --- | --- | --- |
| O-01 | DA-03,18 / finite-map uniqueness | Snapshot.__init__, Snapshot.verify; shared load_graph/validate captured-input hooks | Capture exact bytes, run existing validation, reject races and duplicate keys; AC-01,13,15,16 |
| O-02 | DA-04 / FiniteSet, Relation | Audit.iter_scored_pairs sorted-family combinations; Audit.build_report | Every eligible unordered pair once; no self/cross-family pairs; AC-02 |
| O-03 | DA-06–07 / FiniteSet | Audit.evidence_closure, Audit.build_report | Cycle-safe explicit closure; incremental/full restriction equality; AC-03,04 |
| O-04 | DA-08–09 / FiniteSet | normalize, tokens, Audit.extract_features | Pin Unicode behavior, preserve operators, distinguish empty evidence; AC-05,06 |
| O-05 | DA-09–10 / rational arithmetic | Audit.score_pair, Audit.iter_scored_pairs trigger predicates | Exact single-floor arithmetic and independent triggers; AC-06–08 |
| O-06 | DA-12–13 / map/tuple identity | read_aliases, read_registry | Schema validation, no silent pair conflicts, no graph modifications; AC-07,09,13 |
| O-07 | DA-06,14 / exact fingerprint observation | Audit.fingerprint, Audit.classify_review | Scope-local invalidation; stale reviews and confirmed duplicates stay visible; no transitive suppression; AC-04,09,10 |
| O-08 | DA-15 / TotalOrder | Audit.build_report heapq.nsmallest + exact rank key | Total deterministic ordering and honest prefix/counts; AC-11,12 |
| O-09 | DA-11,17 | Audit.endpoint/candidate/build_report, render_json, render_markdown | Full evidence and unknowns; byte reproducibility; semantic limits; AC-08,12,14,17 |
| O-10 | DA-16,18 | main, emit | Exit/error contract, no caches/network/locks; exclusive allowed report creation; AC-13,15,16 |
| O-11 | DA-05,07,16 | operation-wide contract | Required empty/valid inputs have outcomes in modeled resource environment; unknown/deleted selectors fail explicitly |
| O-12 | DA-01–02,14 | whole-program effects | No edits/merge/ID canonicalization, even on same_meaning receipts; AC-15,17 |

## Design decisions and unresolved evidence

| ID | Status | Decision / consequence |
| --- | --- | --- |
| D-01 | User requirement | Specification first, then implementation explicitly authorized |
| D-02 | Proposed design | Offline standard-library profile, not an embedding service; reproducible baseline for an experiment |
| D-03 | Proposed design | Include cross-role claims; preserve role differences to prevent unsafe consolidation |
| D-04 | Proposed design | Threshold 3000, limit 50 and DA-P1 weights are tunable hypotheses, not validated detector quality |
| D-05 | Proposed design | External alias input avoids an unrequested graph schema change |
| D-06 | Proposed design | Fingerprint explicit evidence closure; full record changes conservatively reopen reviews |
| D-07 | Proposed design | Quiet only reviewed distinctions; confirmed duplicates remain actionable |
| D-08 | Proposed design | Structural invalidity is an error; acknowledged legacy provenance gaps remain evidence |
| D-09 | Unmeasured | Runtime, precision/recall and reviewer burden require an implementation and independently labeled cases |
| D-10 | Future contract | Consolidation, retirement redirects, registry editing and deleted-ID impact analysis are outside 0.1 |

The user authorized implementing the specified experiment. D-02–D-08 are adopted
design choices for DA-P1; the detector's quality remains unmeasured (D-09).
Two implementation details clarify existing obligations: capture the validator's
policy inputs as well as the graph (DA-03/18), and expose their hashes separately;
retain full directly linked operation/axiom/source records in endpoint evidence
(DA-11). Concept locators target their existing page roots; stable fragments are
used only where the Markdown generator actually emits them. No source or dependency pin is changed. Heap selection bounds retained
candidate payloads by the requested limit while consuming every pair for counts.
The [DT-1 extension](TRIAGE.md) reuses the extracted iter_scored_pairs stream;
scoring, rank, receipts and audit report semantics remain DA-P1.

## Specification review findings

The following tensions were resolved in the proposed clauses before encoding:

* Quieting every reviewed pair would hide acknowledged, unresolved duplicates.
  DA-14 quiets only current distinctions and forces current confirmed duplicates
  and stale reviews within scope, even if scores have fallen below threshold.
* Comparing only changed endpoints against each other would miss old counterparts.
  DA-07 compares affected subjects against their entire family and expands impacts
  through the explicit review closure.
* Empty-set Jaccard=1 would reward absent evidence. DA-09 assigns empty unions 0.
* A top-k report without counts could falsely look exhaustive. DA-15 counts before
  truncation and supports the required zero-limit case.
* Content hashing cannot promise an atomic filesystem snapshot. DA-18 states the
  stable-input assumption and detects observed changes without claiming transactionality.

These were design repairs before implementation. The finite reference model
provides witnesses and input coverage within its declared bounds; its historical
limitations in evidence.json remain valid. Operational testing and code inspection
are separate evidence, recorded in conformance.md and implementation-evidence.json.

Run from the repository root:

```sh
python3 -B docs/duplicate-audit/check_model.py
```

This command only checks the proposed mathematical/reference model. It prints
results and writes no files. The retained evidence is produced separately during
specification work; rerun and compare its checks and input hashes after changes.
