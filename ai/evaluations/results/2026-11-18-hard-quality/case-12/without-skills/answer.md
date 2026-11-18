# Implementation review and evidence

The proposed contract is in [spec.md](spec.md); executable finite evidence is in [checks.py](checks.py). This is a specification and reference-model exercise, not a production service. The original six requests remain recorded as G-01–G-06, with conflicts X-01–X-04 and explicitly proposed policy changes D-01–D-04.

The principal decision is to preserve the global limit and irrevocable success using permanent 5/5 capacity shares and one permanent home per ID. This sacrifices full local availability: an empty replica rejects amounts above 5 and the non-home returns a nonterminal routing result. The proposal also replaces the ungrounded 100 ms guarantee with eventual convergence and rejects one-hour deletion in favor of permanent exact records. These are proposed stakeholder decisions, not a claim that the original brief is jointly implementable.

## Implementation-review checklist

- [ ] Product owners explicitly adopt D-01–D-04: reduced availability, routing API, no fixed convergence deadline, and permanent metadata. Do not ship advertising all original promises.
- [ ] Configure identical limit/share values at both replicas. Do not add borrowing, dynamic ownership, failover or transfers without separately specifying safe handoff (C-01, D-01).
- [ ] Enforce canonical customer/home/nonce IDs, authorization, positive integer amounts, globally unique logical requests, and unchanged full IDs on retries (C-02, C-06). Do not infer a different logical request from transport delivery IDs.
- [ ] Serialize all home operations. Atomically bind the immutable amount and decision with the usage update before replying; ensure concurrent first deliveries cannot allocate twice (C-03, C-07).
- [ ] Count authoritative ACTIVE records only. Never add both copies of a replicated reservation or use stale global usage for admission (C-04).
- [ ] Publish every result from C-05. ROUTE is not success, quota rejection or background queuing; mismatched amounts at the non-home are detected only after routing. Timeouts require same-ID retry.
- [ ] Keep rejection sticky, return amount conflicts after rejection/release, and distinguish current ALREADY_RELEASED from a new success (C-07).
- [ ] Subtract capacity once per valid release. Ensure unknown release returns NOT_FOUND and is documented as no cancellation; resolve reserve before release if the caller needs cancellation (C-08–C-09).
- [ ] Client state must tolerate reordered responses: a delayed old ACCEPTED response cannot override a learned terminal release (C-05).
- [ ] Reconcile only into the peer cache. Validate origin, amount, decision, phase and version; merge compatible records monotonically and retain missing snapshot entries (C-10–C-11).
- [ ] Quarantine incompatible replication records and expose diagnostics. Do not choose a wall-clock winner, overwrite the home, or revoke previously accepted promises (C-11).
- [ ] Provide repeated repair snapshots and fair processing; verify eventual quiescent convergence under duplication/reordering. Keep stale inspection separate from a current global read API (C-12).
- [ ] Retain exact per-ID amount/decision/terminal state permanently; never delete the last replay-protection record on a timer. Provision metadata growth or explicitly design an admission-limit extension (C-13, D-04).
- [ ] If introducing bounded retention, authenticated epochs, namespace deletion, migration, crashes or failover, first specify the new assumptions and re-evaluate replay and accounting safety. These extensions are outside this contract.
- [ ] Measure any future latency target under explicit network, scheduling and load assumptions; the current checks do not establish a 100 ms guarantee (X-03).

## Reproduction and observed evidence

Run from this workspace with the existing Python 3 runtime; no dependencies or installation are required:

```sh
python3 checks.py
```

Observed output from the completed run:

```text
X-01: partition -> A accepts x=10 -> B accepts y=10 -> total 20 > 10
X-02: same ID=3 delivered at both homes -> naive ledgers debit 6
X-04: accept x -> release x -> forget at 1h -> replay -> resurrect x
X-03: recovery t=0; first update t=101ms -> disagreement at t=100ms
E-02..E-10: capacity, routing, identity, sticky rejection and release checks pass
E-11..E-14: 6 replay permutations, join laws, conflicts and repair pass
Finite model: 189 reachable states, 2646 transitions; two IDs, amounts 1..6; local usage <=5, terminality, immutable identity pass
PASS: all finite checks. No unbounded proof or timing measurement claimed.
```

| Evidence | What it supports | Boundary |
| --- | --- | --- |
| X-01 trace | Concrete violation of R1 by R2-required dual acceptance | The general contradiction is the indistinguishability argument in X-01 |
| X-02 trace | Independent local ledgers double-debit a cross-replica retry | Does not prove every deduplication design fails; ownership is a solution with availability cost |
| X-03 schedule | Eventual delivery allows disagreement past 100 ms | Synthetic admissible schedule; no real timing measurement |
| X-04 trace | Complete forgetting plus fresh-ID admission permits resurrection | Symbolic one-hour elapse; not an impossibility proof against additional epoch/expiry assumptions |
| API traces | Capacity, routing, sticky decisions, amount errors, early release and retry behavior | Sequential reference-model operations; real concurrency needs atomic implementation |
| Six snapshot permutations and join-law enumeration | Terminal release survives old/duplicate cache updates; compatible merges obey join laws | One compatible chain and representative fault cases; not a full network implementation test |
| Two-way snapshot exchange | Quiescent complete views converge on a representative history | Fairness and all unbounded histories require C-12/C-14's reasoning |
| Reachability exploration to fixed point | 189 states, 2,646 transitions satisfy accounting, terminality and identity checks | Restricted to one home, two IDs and amounts 1–6; two independent share bounds imply the modeled global bound |

C-14 supplies separate inductive protocol arguments for arbitrary numbers of IDs and message schedules under the contract's assumptions. The model uses prevalidated IDs and omits authentication, canonical parsing, real threads, persistent storage, crash recovery, resource exhaustion and network transport. It has no clock-driven transitions: in the proposed policy merely waiting an hour or longer cannot change a record. It does not establish deployed performance, formal machine-checked correctness, or availability beyond the stated scope.

A focused reference lookup was run with `python3 catalog/scripts/catalog.py list --search 'consistency'`; it returned ordering/consistency entries. No catalog theorem, Lean result, external source or repository skill was needed or claimed. Catalog contents and installed runtimes were not modified. There were no tool blockers.
