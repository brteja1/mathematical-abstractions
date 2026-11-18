# Harder evaluations: artifact quality — 2026-11-18

Six fresh model runs produced comparable code and specification quality. The guided scheduler test suite had one concrete extra coverage advantage: it caught a capacity-eight defect that the baseline suite missed in a **post-hoc exploratory probe**. Neither these runs nor the first pilot establish a general skill advantage. Human comprehension has not been measured.

## Behavioral and test-quality results

| Evaluation | Without skills | With skills | Finding |
| --- | --- | --- | --- |
| Calendar implementation, independent contract checks | 18/18 passed | 18/18 passed | No observed behavioral advantage |
| Scheduler tests, correct implementations accepted | 2/2 | 2/2 | Both tolerate private representation and tie-order differences |
| Scheduler tests, ten predeclared faults with audited assertion failures | 10/10 | 10/10 | Same primary defect detection |
| Additional capacity-eight fault, selected after inspecting suites | Missed: suite passes | Detected: assertion fails | Useful extra coverage in this particular guided output; not a predeclared result |
| Quota specification | Main conflicts diagnosed; coherent proposed policy | Same, with a different proposed policy | No clear quality winner |
| Generated checks rerun independently | All pass | All pass | Passing checks support their declared bounds, not universal correctness |

Calendar checks include clipped/adjacent/nested intervals, endpoint ties, duplicate IDs versus distinct IDs sharing an interval, conflicting merges, large signed integers, persistence and seeded histories. Scheduler faults cover expiration, minimum priority, replacement, backwards time, rejection side effects, clone clock/aliasing, snapshot order and equal-time behavior. Both suites passed against the dictionary implementation and an opaque class-based implementation with a different legal tie policy; neither was falsely rejected.

For the capacity probe, a correct scheduler was changed to silently ignore new live jobs once eight IDs were present. Nine valid insertions independently confirmed the fault. The baseline suite still passed; the guided suite's 513-job scenario failed. This probe was motivated by a visible difference between the generated suites, so it is vulnerable to selection bias and **does not change the ten-fault primary score**. It supports a narrow statement about these artifacts, not reliable causal improvement across future generations. [Probe source and complete output](capacity-supplement.json) are retained.

## Code and specification quality

The following scores apply the frozen [quality rubric](frozen-evaluator/quality-rubric.md). They are unblinded editorial judgments by the suite author, not independent human-study results. Dimensions are reported separately; no total score is used. A blank dimension means it was not the task's target artifact.

| Case / dimension, 0–4 | Without skills | With skills | Reason |
| --- | --- | --- | --- |
| Calendar specification | 3 | 3 | Both are precise and standalone, including merge definedness and failure effects; neither includes a worked caller example in the spec itself |
| Calendar code maintainability | 4 | 4 | Small pure functions, immutable canonical state, clear conflict handling and grouped endpoint deltas; no framework or runtime catalog dependency |
| Calendar test maintainability | 4 | 4 | Public observers and independent small-domain oracles; baseline emphasizes exhaustive map pairs, treatment adds branching persistence histories |
| Calendar editorial readability | 3 | 3 | Important semantics are easy to locate; a short worked usage example would reduce newcomer reconstruction |
| Scheduler test maintainability | 3 | 3 | Strong named scenarios and independent histories, but failing subtests can continue with divergent model state and produce noisy cascading errors |
| Scheduler editorial readability | 3 | 3 | Purpose/oracles are explained; helpers and generated histories still require careful reading across contract, plan and tests |
| Quota specification | 4 | 4 | Original goals, conflicts, proposals, state, transitions, results, invariants, examples and limits are explicitly distinguished |
| Quota check maintainability | 3 | 3 | Runnable bounded models with honest limits; these are authored encodings plus checks, not independent proofs of the specification |
| Quota editorial readability | 3 | 3 | Stable clauses and acceptance examples help, but the long result/transition sections need multiple lookups; neither has a short end-to-end request walkthrough |

Concrete comparisons:

- **Calendar code:** both use a frozen private record and sorted immutable rows. The guided record has a fully typed row field and descriptive endpoint names. The baseline factors canonicalization into a reusable helper. Both coalesce adjacency for occupancy while grouping all equal-time changes before measuring peak. These are understandable implementations of the same observable contract, with no clear maintenance winner.
- **Calendar mapping:** treatment adds stable S1–S8 clauses, O1–O8 obligations, hashes and catalog correspondence. The baseline's shorter requirement/function/test table already covers the requested contract. The extra traceability is useful for audit work; it is not evidence that the executable library is better or easier for every reader.
- **Scheduler tests:** both model allowed ties by validating the returned row and then removing that actual row from the oracle. Both check jobs and logical time after rejection, and both observe cloned branches. The guided suite additionally stresses 513 distinct live jobs and permits unusual nonempty IDs. The baseline's plan is shorter. Test counts (12 versus 11) and history lengths are not quality scores.
- **Quota specification:** baseline proposes permanent 5/5 escrow shares and home-encoded IDs; treatment proposes a single mutation authority at A with an ordered replay log. Both explicitly sacrifice R2, replace the unsupported deadline, retain replay-protection metadata, distinguish stale copies from logical allocations, and define release-before-reserve behavior. These are different permitted product proposals, so neither is ranked simply for choosing escrow or a leader.
- **Quota evidence:** baseline's bounded local model reports 189 states plus separate cache-merge checks; treatment's network replay model reports 313 states. The modeled state spaces differ. Larger state counts do not imply stronger specifications. Both disclose finite bounds and separate protocol arguments from executable evidence.

## Human comprehension

[Anonymous reading packets](human-reading/README.md) contain each case's task, relevant artifacts, five concrete comprehension/change questions and blank response sheets. They ask readers to locate conflict rules, explain endpoint/tie semantics, find rollback and clone tests, or identify proposed availability/retention changes. Use accuracy, file/line evidence, time and confidence, with counterbalanced assignment.

**No reader has completed this trial.** Human accuracy/time fields in [quality-scores.csv](quality-scores.csv) are blank. Anonymous labels hide file paths and run metadata, but catalog references in the content may hint at the arm. The author's earlier scoring is not made blind by these labels. The current readability finding is an editorial comparison with concrete observations, not a measured human comprehension benefit.

## Execution, overhead and validity

Both arms requested **gpt-6.1-sol, medium reasoning**, explicitly using the user's configured model/settings. Each fresh ephemeral session used the same workspace sandbox and 480-second cap. The seeded schedule was recorded before generation: guided/baseline for case 10, baseline/guided for case 11, guided/baseline for case 12. There was one run per arm per case, no timeout, no model-output repair, and no reading of another run by an evaluated session visible in the traces. Common task/catalog inputs and skill files were verified unchanged. Actual backend revision was not emitted; host context and linked runtimes were not fully isolated.

| Case | Seconds, without / with | Reported output tokens, without / with | Completed shell commands, without / with |
| --- | --- | --- | --- |
| Calendar | 161.10 / 184.28 | 5,972 / 7,665 | 7 / 11 |
| Scheduler tests | 133.53 / 159.83 | 5,634 / 6,213 | 5 / 8 |
| Quota specification | 269.94 / 274.39 | 9,858 / 12,332 | 7 / 13 |

The guided runs took more time and emitted more output here. There are too few runs to estimate a reliable speed/cost effect. Cumulative input tokens and cache use are in the metadata; they include repeated context and are not unique prompt lengths or monetary cost. Baseline also had catalog access, so this tests the incremental skill instructions, not the combined value of the entire repository versus no mathematical tooling.

Two evaluator issues were discovered and fixed **after all six outputs and original grading data were collected**:

1. The frozen automatic mutation flag required both assertion failures and zero test errors. Genuine faults also caused later seeded subtests to error, so that flag misleadingly marked only 1/10 baseline and 0/10 guided as clean kills. All ten variants in both arms have actual contract-relevant assertion failures. [Assertion audit](assertion-audit.json) preserves witnesses and the original flags; [compressed raw metrics](metrics.raw.json.gz), raw variant logs and the [frozen evaluator](frozen-evaluator/quality_checks.py) preserve the original execution. The primary table uses the audited assertion evidence. Future grading retains the clean-run diagnostic but accepts a real assertion detection when correct controls pass; a regression test covers mixed assertion/error results. Import-only, syntax-only and error-only failures still do not count.
2. The original snapshot helper omitted ONTFS metadata and shapes while copying the Turtle projection. Guided cases 10/11 encountered a missing-projection check and used successful direct catalog queries. That is a harness limitation, not a mathematical defect. Future snapshots copy all three files equally; a fresh snapshot was checked successfully with an ONTFS/SPARQL query. The six runs were not silently replaced. These results therefore do not establish the efficacy of a fully configured ONTFS workflow.

Details are in [evaluator-corrections.json](evaluator-corrections.json). The original prompts, rubric and evaluator sources are archived with their pre-run hashes. Stronger evidence would require independent repeated runs, blind grading and actual readers, including preregistered capacity probes and a fully working snapshot.

## Inspect and reproduce

- Calendar: [baseline code](case-10/without-skills/calendar_api.py), [guided code](case-10/with-skills/calendar_api.py), [baseline spec](case-10/without-skills/spec.md), [guided spec](case-10/with-skills/spec.md).
- Scheduler: [baseline tests](case-11/without-skills/test_scheduler.py), [guided tests](case-11/with-skills/test_scheduler.py), [assertion witnesses](assertion-audit.json), [extra capacity probe](capacity-supplement.json).
- Quota: [baseline spec](case-12/without-skills/spec.md), [guided spec](case-12/with-skills/spec.md).
- [Run plan and frozen hashes](plan.json), [metrics](metrics.json), [dimension scores](quality-scores.csv), and raw events in each arm's directory. Full verbose grader output is retained compressed; smaller summaries link to the per-variant logs.

Generated checks can be rerun in each archived arm directory (`python3 -m unittest -v test_calendar`, `python3 -m unittest -v test_scheduler`, or `python3 checks.py`). The evaluator-only `quality_checks.py` in the source suite independently grades calendar artifacts and injects scheduler variants. Rerunning models incurs new model calls; rerunning these checks does not.
