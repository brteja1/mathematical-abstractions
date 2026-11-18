# Implementation review and evidence

The original requests cannot all be satisfied. R1 and R2 force an allowed execution with 20 outstanding units against a limit of 10. The 100 ms part of R5 lacks the timing assumptions necessary to guarantee it. Literal one-hour erasure of all request/release evidence cannot distinguish arbitrarily delayed retries from fresh requests. This last finding is conditional on complete information loss; it does not prohibit compaction that retains equivalent information.

The proposed contract in `spec.md` deliberately replaces R2 with authority at A and explicit unavailability at isolated B; replaces the R5 deadline with conditional eventual convergence; and replaces R6 with indefinite identity/terminal-state retention. These are recommendations, not silent reinterpretations or claims to meet the original promises. R1, R3, R4 and the eventual part of R5 are preserved with explicit API and progress semantics. No production service was implemented.

## Deliverables and reproduction

- `spec.md`: source goals G-ENV/R1–R6; findings F-CAP/F-TIME/F-GC/F-IDENTITY/F-ORDER; decisions D-*; implementable contract P-*; acceptance cases E1–E12; catalog mapping and check boundaries V-*.
- `checks.py`: standalone standard-library finite model, exhaustive BFS, targeted checks, and original-design counterexample traces. Run `python3 checks.py` from this directory.
- `checks-output.txt`: saved successful output, including Python version and SHA-256 hashes of TASK.md, spec.md and checks.py. Reproduce with `python3 checks.py > checks-output.txt`.

Python 3.13.9 completed the checks with exit status 0. The finite model explored **313 distinct reachable states, 3,504 action edges, and 2,848 self-loops**. All modeled safety assertions passed. From every one of these 313 states, an explicit quiescent delivery continuation reached replica agreement. This is a reachability/catch-up test, not universal temporal verification under fairness.

The complete finite domain is two replicas, two logical IDs, reserve amounts {6,10}, and at most four log events (one decision and at most one release per ID). There is no exploration depth cutoff. Reserve and release retries, duplicate delivery and delay can repeat indefinitely as self-loops. Delivery of any existing authoritative event permits all message orders; authentic sequence numbers abstract immutable event payloads. Isolated B's mutation attempt is a no-op with UNAVAILABLE. Forwarded B mutations share A's transition. This abstraction omits actual transport buffers and resource limits.

Separate targeted checks cover fresh amounts 1–10, exact capacity with two simultaneous outstanding IDs (6+4), over-capacity rejection (6+5), reclaimed capacity, fresh amount 11, invalid arguments, cross-ingress retries, amount conflicts in both serialization orders, repeated release, retry after release, unknown release, terminal rejection, and release-before-acceptance-event delivery. Empty initialization is checked and both successful and rejected requests are exercised, so the tested safety result is not obtained by forbidding all work.

## Findings and evidence boundaries

| Finding / clauses | Executed evidence | Conclusion and limit |
|---|---|---|
| F-CAP: R1, R2, G-ENV | Distinct x:10 and y:10 during partition; enumeration of all 100 pairs of required amounts yields 55 over-limit pairs. | Concrete violating required scenario, plus the indistinguishability argument in spec.md rules out satisfying both promises under the stated environment. No minimum unsatisfiable core claim. |
| F-TIME: R5 deadline, G-ENV | Heal at 0 ms; differing state persists at 100 ms; delivery at 101 ms. | Allowed finite schedule defeats an unconditional deadline. The script checks the schedule arithmetic; the information argument is manual. |
| F-GC: R4, literal R6, fresh acceptance semantics | Accept, release, erase all identity evidence at 3601 s, replay at 3602 s, observe resurrection. | Counterexample to naive TTL forgetting; broader information-loss argument is conditional and manual. |
| F-IDENTITY: R3 | Both same-ID/different-amount serialization orders produce conflict at A; B cannot classify while isolated. | Proposal's behavior tested; no assertion that R3 alone is impossible. Original cross-replica response deadline is unspecified. |
| F-ORDER: R4 | Naive stale-active overwrite resurrects; proposed sequence replay buffers #2 until #1 and ignores duplicates. | Failure of unordered overwrite, repaired in the finite model by prefix replay. |
| P-INVARIANTS / P-REPLAY | All reachable states satisfy capacity, permanent binding, terminal-phase and prefix-replay assertions. | Exhaustive only within the declared finite domain; not a production implementation proof. |
| D-ASSUMPTIONS / P-CONSISTENCY | 313 explicit drain continuations; written induction and fair-propagation arguments. | No automated LTL cycle/fairness verification, no wall-clock measurement, no guarantee under permanent partition. |
| P-LIFECYCLE / P-SNAPSHOT | Retry after retained release tested; baseline has no deletion action. | Storage growth and snapshot correctness require review; snapshots are specified but not included in the model. |

For unbounded operation, spec.md gives explicit engineering induction arguments for capacity, identity, terminality and ordered replay, and a conditional eventual-propagation argument. These are separate from finite experiment results and are not machine-checked proofs. The model's amount domain does not exercise every possible split of 10; targeted checks add 6+4, but neither is a completeness theorem for arbitrary IDs/amounts.

## Catalog and tooling provenance

Read and applied both requested skill entrypoints, plus their checking/reporting, backend-selection and Python explorer references. Used only focused dependency-free catalog queries:

```text
python3 catalog/scripts/catalog.py check
python3 catalog/scripts/catalog.py list --search transition
python3 catalog/scripts/catalog.py get LabelledTransitionSystem --sections operations axioms laws
python3 catalog/scripts/catalog.py get LinearTemporalLogic --sections operations axioms laws
python3 catalog/scripts/catalog.py get SafetyProperty --sections operations axioms laws
python3 catalog/scripts/catalog.py get LivenessProperty --sections operations axioms laws
python3 checks.py
```

Catalog check returned 264 concepts, 2,484 nodes and no errors. This validates catalog structure, not the service specification. V-MAP in spec.md gives stable operation/axiom IDs and the semantic mapping: labelled successors/finite paths become reserve/release/delivery transitions; temporal G/F notation states safety and conditional propagation obligations. No axiom is transferred through a specialization link. SafetyProperty and LivenessProperty records have a disclosed legacy source gap and are used only for classification. No catalog entry is claimed to prove this protocol.

Python enumeration was selected intentionally because the requested finite traces and safety checks fit a small explicit model. No solver installation, dependency change, Lean build, runtime modification or catalog edit was needed or performed. No tool blocker occurred in the chosen workflow. Availability of uninvoked Lean/TLA+/Alloy/Z3 tools was not tested and no results from them are claimed. No external browsing, other runs, evaluator keys or other agents were used.

## Implementation-review checklist

The following are review obligations for an eventual implementation; they are not checked-off claims about nonexistent production code.

- [ ] Obtain product approval for D-POLICY, D-TIMING and D-RETENTION. Verify that documentation explicitly advertises isolated-B unavailability, no 100 ms guarantee and growing metadata.
- [ ] Use only A as the mutation authority. Prevent B's stale state or a timeout path from issuing a reservation success. No failover is implicitly enabled.
- [ ] Serialize binding lookup, capacity check, map update and event append in one transaction; emit success afterward. Review actual locking and persistence behavior separately from model atomicity.
- [ ] Validate customer scope, exact ID equality, positive integer amounts and arithmetic safely. Support amount >10 as capacity rejection, without overflow. Specify practical payload limits before deployment if needed.
- [ ] Persist the first well-formed amount binding even on capacity rejection. Reject differing amounts in ACTIVE, RELEASED and REJECTED states. Keep retry processing free of additional capacity consumption.
- [ ] Preserve terminal capacity rejection and released status forever per ID. Expose historical acceptance after release without implying a fresh active promise.
- [ ] Apply each release once. Unknown-ID release must not create an unreviewed cancellation/tombstone policy. Check valid release while B has not yet learned the acceptance.
- [ ] Distinguish CAPACITY_REJECTED from UNAVAILABLE. Timeouts must not imply that a forwarded operation failed. Clients must retry the original ID/amount and handle delayed correlated responses.
- [ ] Replicate decisions and bindings as well as accepted/released state. Use contiguous sequence replay, buffer gaps, ignore old duplicates, and fail visibly on conflicting content for one sequence.
- [ ] Include the response sequence watermark and label B reads with their applied prefix. Route authoritative reads to A; ensure read-your-writes waits do not imply a bounded deadline.
- [ ] Retain equivalent complete identity/decision/release information during cache expiry and any snapshot/log compaction. Check atomic snapshot installation, monotone watermarks and stale snapshot rejection before enabling P-SNAPSHOT.
- [ ] Provision/archive the permanent index. A one-hour cleanup job must not erase deduplication facts. Any bounded-storage, epoch or client-watermark scheme requires a new reviewed contract.
- [ ] Establish fair local scheduling and eventual anti-entropy delivery/processing for the promised progress. Monitor catch-up backlog and storage; do not advertise a numerical SLA without a complete timing budget.
- [ ] Test real concurrency, resource failures, protocol integrity, long-delayed messages and snapshot behavior. The finite model does not cover real code, crash recovery, snapshots, performance or storage exhaustion.
