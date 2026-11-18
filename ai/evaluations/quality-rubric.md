# Hard-case quality rubric (evaluator only)

Freeze this rubric and the evaluator code before opening model outputs. Do not include either in prepared workspaces. All arms have the same criteria; skill names, catalog IDs, number of files, word counts and number of tests earn no quality points by themselves. Record critical failures and unavailable evidence separately. These cases extend, rather than replace, the shared rubric in `grader.md`.

## Quality dimensions

| Dimension | Evidence and scoring |
| --- | --- |
| Behavioral correctness | Case 10: independently executed contract checks, per requirement, including failure-state observations and mixed histories. Report checks passed/total and actual defects. Case 12: correct diagnosis and internally coherent proposed transitions, not the existence of a spec file. |
| Test effectiveness | Case 11: behavioral mutants killed/10, false failures on **two** correct implementations, nontrivial mixed histories and failure-state checks. Import/syntax/tool errors do not count as killed mutants. Cases 10/12: inspect whether assertions could catch wrong algorithms/encodings rather than repeat implementation expressions. |
| Specification quality, 0–4 | 0 unusable; 1 major ambiguity/contradiction; 2 central contract present but important domains, state effects or error/consistency decisions missing; 3 implementable with minor omissions; 4 precise, coherent and traceable, with required behavior separated from proposals, representative examples and explicit evidence limits. |
| Code maintainability, 0–4 | 0 unusable; 1 fragile/opaque; 2 workable with substantial duplication, implicit invariants or tangled concerns; 3 clear domain names, separated algorithms and useful errors with minor issues; 4 small understandable components, explicit invariants and boundaries, minimal unnecessary abstraction and an easy path for a plausible extension. Correctness remains a separate dimension. |
| Test maintainability, 0–4 | 0 unusable; 1 private-state coupling or inscrutable assertions; 2 mostly readable but weak organization/oracles/failure diagnosis; 3 clear scenarios and public observations; 4 reusable independent oracle where useful, well-named scenarios, reproducible generation and failures that identify the violated contract. Long suites can score poorly. |
| Reviewer readability, 0–4 | 0 cannot follow; 1 high reconstruction burden; 2 comprehensible with substantial cross-file inference; 3 important behavior and rationale easy to locate; 4 a new engineer can answer the comprehension tasks using short, precise explanations, explicit state/result shapes, examples and well-signposted decisions. This is an author's editorial assessment unless actual independent human readers participate. |

Use dimensions separately, with specific examples and uncertainty. Do not roll them into an unsupported universal quality score. A finite passing suite is not a proof. Preserve unexpected failures and legitimate choices; do not redefine the rubric after seeing which arm does better.

## Case 10: interval calendar

Check exact replay versus ID conflict; compatible union versus undefined conflicting merge; persistent alias behavior; duplicate ID versus distinct IDs sharing an interval; partial-overlap clipping; nested and adjacent spans; gaps; empty/equal/reversed windows; simultaneous endpoints; negative and huge integers; count of distinct active bookings rather than union length. A partial merge is not an unconditional monoid operation across conflicting IDs. Catalog structure alone cannot authorize arbitrary overwrites. The spec should make this definedness visible. Sweep-line peak should process endings before starts or aggregate equal-time deltas before taking maxima. O(n log n) algorithms are appropriate; no performance promise beyond the brief is required.

Readability questions: Where is conflict checked and what remains unchanged? Why is adjacency coalesced but not counted as overlap at peak? Can two IDs share the same interval? What changes to add a read-only `occupied_length` observer? What exactly is the valid domain of merge associativity?

## Case 11: scheduler tests

The known-good implementation and an opaque class-based implementation with reversed tie preference must both pass. Ten independent mutants target exclusive expiration, minimum priority, live replacement, expired replacement removal, backwards time rejection, mutation on rejected time, clock inheritance in clones, clone independence, sorted snapshot output and equal-time operations. Mutants are single semantic faults; each is independently demonstrated to violate the contract before evaluating generated suites. Only assertion failures/expected-exception failures count as kills, not module crashes or private-attribute lookups.

Inspect whether the test suite avoids promising a particular tie order, checks residual jobs after a tied take, observes both copies after clone updates, separates time progress from empty-take exceptions, includes negative priorities and arbitrary integer boundaries, and tests histories against an independent state oracle. More repetitive examples do not replace these obligations.

Readability questions: Which test catches expiration exactly at the deadline? How does the suite avoid enforcing tie order? What observation establishes rollback on backwards time? Which tests establish clone independence? How would a maintainer add a new allowed tie-breaking strategy without rewriting tests?

## Case 12: quota specification

Predeclared findings: (1) R1 conflicts with R2 under two distinct simultaneous isolated requests of 10; retry identity is unnecessary for this counterexample. (2) Global replay semantics during partitions require an ownership/routing or coordination policy; distinguish duplicate same-ID acceptance from distinct-ID overspending, and distinguish safety from result availability. (3) R4/R6 plus unbounded delayed reserve messages conflict with deleting **all** distinguishing metadata: after a tombstone is forgotten a delayed reserve is indistinguishable from a fresh one; epochs, causal stability or retained fences change that premise and must be specified. (4) R5's 100 ms deadline cannot be guaranteed without bounded network/processing assumptions; eventual delivery does not imply that deadline. Do not conflate these conflicts with basic eventual convergence.

An acceptable proposal may use per-replica escrow plus permanent request ownership and durable tombstones/fences, or coordinated admission that rejects/unavailables some partitioned requests. It must state which stakeholder requirements change. Specify capacity accounting when a release arrives before reserve; ID/amount conflicts must not let delivery order create divergent states or double credits. An ownership policy must handle or explicitly reject wrong-replica retries and releases. If a coordinated policy is chosen, do not claim it fulfills R2. If compaction is proposed, state a sufficient message/epoch stability protocol or keep metadata indefinitely. No proof of Byzantine/crash recovery or unbounded liveness is required by this brief.

Readability questions: Under a partition, which replica may accept which IDs and amounts? What happens to a release delivered before its reserve? What prevents a delayed request from recreating released usage? Which original promises changed in the proposal? Which assumptions justify convergence and which would justify a numerical deadline?

## Human comprehension trial

Prepare anonymous A/B artifact packets without final replies, model labels, source paths or arm metadata. Provide the relevant five questions above, an answer sheet and fields for elapsed time and confidence. Counterbalance which packet is read first across readers; avoid having a reader solve both variants of the same case without acknowledging learning effects. Score answers for correctness against the contract, not aesthetic preference. Report reader count, task accuracy and time separately. Until humans actually complete the trial, call the packets **ready for human evaluation**, never measured human readability results. Anonymous labels do not make the author's prior grading blind.
