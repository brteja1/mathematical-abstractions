# Two-replica quota service specification

## Original goals (not an agreed implementable contract)

**G-01 (R1).** Starting with no reservations, total outstanding accepted allocation across A and B must always be at most 10. Acceptance is irrevocable except for a client release; reconciliation cannot withdraw success.

**G-02 (R2).** Either isolated replica, with no local reservations, must immediately accept every fresh integer amount 1–10. Rejection is allowed only when local accepted usage would exceed 10, never because the other replica is unreachable.

**G-03 (R3).** A logical request has one globally unique ID. Duplicate delivery, including delivery to the other isolated replica, must not consume capacity twice. A different amount under the same ID is an error.

**G-04 (R4).** Releasing an accepted reservation is idempotent. Neither delayed reserve retries nor reconciliation may resurrect it. IDs are never reused.

**G-05 (R5).** Eventually delivered messages must lead to agreement on logical state. Stakeholders also request agreement within 100 ms of partition recovery, without supplied latency or processing bounds.

**G-06 (R6).** Request/release metadata should be deletable after one hour while remaining safe against arbitrarily late messages.

## Demonstrated conflicts and limits

**X-01 (capacity versus availability).** Partition initially empty A and B. Send distinct IDs x and y, each for 10, to A and B respectively. Each replica's local history is indistinguishable from a run in which it alone receives a request, so G-02 requires two successes. Outstanding accepted usage becomes 20, contradicting G-01. No retry, release, failure, or reconciliation is needed. Irrevocability rules out repairing this by later revocation. Unique IDs alone do not solve this contradiction.

**X-02 (cross-replica identity).** A local check-then-insert at each replica is not global deduplication. Sending the same ID to both isolated replicas can debit both local ledgers. Distinct amounts under one ID also cannot be authoritatively classified by two replicas that have not exchanged their observations. Choosing a winner after two incompatible successes cannot preserve both promises. A protocol needs an authority or a stronger coordination/identity assumption, separately from capacity allocation.

**X-03 (deadline).** After partition recovery, delay all inter-replica messages for 101 ms; this is permitted even though they are eventually delivered. B cannot distinguish a run with an unseen A acceptance from one without it. Exact agreement by 100 ms cannot be guaranteed. “Partition ended” means connectivity is restored, not that every outstanding message has arrived. A deterministic deadline needs bounds on delivery, scheduling, processing, backlog and retry/discovery time.

**X-04 (forgetting).** Accept x, release x, then erase all evidence of x after an hour. An arbitrarily late reserve(x) is now indistinguishable from a first delivery of a fresh ID; treating it as fresh resurrects x. A delayed old acceptance record can do the same if a release marker is forgotten. Never reusing an ID does not prevent replay of that ID. Retaining a permanent exact replay filter or epoch fence is still retaining metadata; arbitrary random IDs do not themselves certify age. Complete forgetting with ordinary fresh-ID acceptance needs extra information, such as enforceable message expiry and authenticated ID epochs, or a bound on replay lifetime. None was supplied.

## Necessary decisions and proposed replacement policy

**D-01 (proposal; replaces G-02).** Prioritize G-01 and irrevocable acceptance. Permanently allocate 5 units to A and 5 to B. Each replica may accept only within its own share. There is no borrowing, share transfer, failover, ownership migration or reconfiguration in this version. Thus unused capacity can be stranded. An empty A rejects 6–10, even if B is empty. Local processing is available during partitions only for IDs owned by that replica; this explicitly changes R2.

**D-02 (proposal; clarifies G-03/API and weakens universal completion availability).** Each ID has one permanent home, encoded in the canonical ID. Only that home decides requests. The other replica returns a routing result, including during partitions, without a final reservation decision. Clients must reach the home to complete the request. This adds a result beyond the brief's success/explicit-rejection pair. It preserves single logical allocation and amount-conflict checking at the authority; it does not promise immediate cross-replica retry completion or conflict detection at the non-home.

**D-03 (proposal; replaces deadline portion of G-05).** Guarantee eventual convergence under fair eventual communication and processing. Treat 100 ms as an uncommitted performance target until explicit bounds and a load envelope exist. Do not advertise it as a safety property or SLA.

**D-04 (proposal; replaces G-06).** Retain each ID's amount, decision and terminal release marker for the customer's entire namespace lifetime. No one-hour deletion is allowed. Historical log entries may be compacted into the exact current per-ID record; the last record may not be deleted. Unlimited lifetime fresh requests require unbounded metadata storage in this model. A finite deployment must provision storage or publish an explicit storage admission limit that rejects new IDs before mutation, while still servicing existing-ID retries/releases. Such an operational rejection further weakens R2 and must not masquerade as quota exhaustion. This version assumes sufficient metadata storage and has no time-based GC.

## Implementable contract

### Assumptions and state

**C-01 (execution).** Two honest, noncrashing replicas start empty and agree on limit 10, shares (5,5), identity format and protocol version. Each replica serializes home operations and applies each transition atomically with its usage update and record creation. No response claiming acceptance precedes that transition. No persistence/crash recovery or Byzantine protection is claimed. If crashes are later introduced, durable atomic records and recovery of ownership/accounting require a new design review. Messages may be duplicated, reordered or delayed without bound.

**C-02 (identity and authorization).** IDs are canonical tuples `(customer_namespace, home, nonce)`, with home exactly A or B. Clients generate a new globally unique nonce for each distinct logical request in that home; retries preserve the entire tuple and amount. A different tuple is a different request. All examples refer to one customer. Validate canonical form and customer authorization before state access. Only authorized customer callers may reserve or release IDs in that namespace. ID uniqueness is an assumption from the brief, not a probabilistic guarantee of this protocol. Aliases and alternate encodings are invalid; clients may not switch home for a retry.

**C-03 (authoritative state).** At home h, `M_h[id]` is absent or an immutable-amount record `(amount, decision, phase, version)`. Valid records are:

| Decision | Phase | Version | Meaning |
| --- | --- | --- | --- |
| ACCEPT | ACTIVE | 0 | Capacity reserved |
| ACCEPT | RELEASED | 1 | Previously accepted, now terminal |
| REJECT | REJECTED | 0 | Sticky capacity rejection |

`amount` is a positive integer; amounts over 5 are recordable rejections. `U_h = sum(amount for ACTIVE records in M_h)` is stored or derived atomically. A rejection remains rejected even after capacity becomes free. Unknown-release and invalid-input results do not create records. No other state or version is valid. Both replicas also hold a read-only cache of the other home's records; it cannot decide requests or authorize capacity. Every ID's record has exactly one writer.

**C-04 (global meaning and invariants).** Logical state is the union of the two authoritative maps, keyed by full ID, not the sum of two replicated views. “Outstanding” means ACCEPT/ACTIVE until the home processes a valid release. The invariants are: (a) `0 <= U_h <= 5`; (b) `U_A + U_B <= 10`; (c) at most one decision and one immutable amount per ID; (d) RELEASED and REJECTED are terminal; (e) every ACCEPT response corresponds to one authoritative acceptance and no reconciliation can revoke it. A stale cache is not a current global ledger. After releases and new allocations, combining stale cache entries can even overestimate usage above 10; it is not evidence of actual over-allocation.

### API and transitions

**C-05 (results and transport).** Requests are `Reserve(id, amount)` and `Release(id)`. Results always identify the full ID. Reserve results are `ACCEPTED(amount)`, `REJECTED_CAPACITY(amount)`, `ALREADY_RELEASED(amount, originally_accepted=true)`, `AMOUNT_CONFLICT(bound_amount)`, `INVALID_INPUT`, or `ROUTE(home)`. Release results are `RELEASED(amount, already_released=bool)`, `NOT_FOUND`, `NOT_ACCEPTED`, `INVALID_INPUT`, or `ROUTE(home)`. Authorization failures are `UNAUTHORIZED` with no mutation. Results have no promised wall-clock completion bound. Responses can be lost; a timeout is an unknown outcome and the client retries the same ID. ROUTE is nonterminal and has no allocation effect; the client calls the home itself. No background acceptance is triggered by ROUTE. Clients must not translate it into acceptance or a quota rejection. Concurrent or reordered responses describe the operation at its processing time: an old ACCEPTED response arriving after RELEASED does not reactivate the reservation. Clients tracking one ID keep a learned terminal release state.

**C-06 (dispatch and input validation).** Validate authorization, canonical ID, and, for reserve, a positive integer amount (excluding booleans and fractional values). Invalid requests have no effect. Valid requests received at a non-home return ROUTE even if a cache contains that ID. A non-home never asserts acceptance, release, NOT_FOUND or amount conflict from its cache. Thus malformed input is rejected before routing and a well-formed conflicting amount is checked only at the home. This is an explicit API limitation of D-02.

**C-07 (reserve at home, in order).**

1. If a record exists and amounts differ, return AMOUNT_CONFLICT without mutation, including for RELEASED and REJECTED records.
2. If a matching record exists, return ACCEPTED for ACTIVE, ALREADY_RELEASED for RELEASED, or the original REJECTED_CAPACITY for REJECTED. Never debit again.
3. Otherwise atomically test `U_h + amount <= 5`. If true, create ACCEPT/ACTIVE/version 0, add amount to usage and return ACCEPTED. Otherwise create REJECT/REJECTED/version 0 and return REJECTED_CAPACITY. Both outcomes permanently bind this ID to this amount.

A capacity rejection can be retried as a new logical request only with a fresh ID. Invalid input binds nothing. If different amounts race at the home, the first serialized valid reserve binds the amount, even if rejected; the other receives AMOUNT_CONFLICT. There is no reconciliation winner selection between incompatible accepted records.

**C-08 (release at home).** For absent ID return NOT_FOUND. For REJECTED return NOT_ACCEPTED. For ACTIVE atomically change to ACCEPT/RELEASED/version 1, subtract the immutable amount once and return RELEASED with `already_released=false`. For RELEASED return RELEASED with `already_released=true`, without changing usage. Release has no amount parameter. A valid release of an accepted ID always finds its original home record, since it is never deleted. Release sent to the other replica routes under C-06.

**C-09 (ordering semantics).** Reserve and release for one home follow its atomic processing order. A release processed before the first acceptance returns NOT_FOUND and does not cancel a future reservation; it is not a valid release of an already accepted reservation. A client that wants cancellation must first resolve reserve's outcome, then release at the home and receive RELEASED (retrying as needed). The original request can arrive much later after an early NOT_FOUND. Once a valid release has happened, every matching delayed reserve returns ALREADY_RELEASED, every conflicting reserve returns AMOUNT_CONFLICT, and all duplicate releases are harmless. Releases do not depend on the other replica having observed the acceptance.

### Reconciliation, consistency and lifecycle

**C-10 (replication).** Each home periodically sends all its current records to the peer, including rejection and release records. Repeat full snapshots indefinitely (incremental optimizations may be added only with equivalent repair). A snapshot may be processed per entry; it need not be an atomic global snapshot. Entries carry origin home and full ID. A replica accepts replication only for the peer's home namespace into the peer cache, never into its own authoritative map or usage counter. Missing entries in a snapshot do not delete entries. Thus a late old snapshot is not a replacement of the entire cache.

**C-11 (merge).** For one ID, absent is older than any valid record, and ACCEPT/ACTIVE/version 0 is older than its same-amount ACCEPT/RELEASED/version 1. Merge takes the newer record; identical entries are no-ops. REJECTED has no successor. A different amount, different immutable decision, illegal version, invalid origin or same-version/different-content entry is a protocol fault: reject/quarantine the entry and raise an operational diagnostic, never resolve it with timestamps or revoke a success. Honest execution from C-01 cannot generate these conflicts. No order is defined between incompatible records. Release dominance applies only within a compatible record chain; a blind “largest version wins” is insufficient.

**C-12 (consistency and liveness).** Home operations are linearizable at their atomic transitions (or atomic lookup for a no-op result). There is no global strongly consistent snapshot/read API. Optional cache inspection is explicitly stale, identifies origin/version, and cannot drive admission or releases. After communication becomes fair, repeated snapshots and eventual processing ensure that each committed record eventually reaches the peer at that or a later version. Once writes stop, both complete views converge to exactly the same logical state. With ongoing writes, promise per-record eventual visibility, not simultaneous equality of both views at every instant. Arbitrarily long partitions have no liveness guarantee across homes. Local operations require fair local scheduling but do not await the peer. Convergence assumes the replication worker and network give each finite pending update eventual service; merely delivering a subset of messages is insufficient.

**C-13 (retention).** Keep the current home record and replicated peer record permanently, including rejected amounts and release tombstones. Losing the cache can be repaired from the home under the noncrash model, but a timer must not discard live replay protection at the home. No expiration of responses, messages or tombstones is assumed. Explicitly prohibiting old retries without an enforceable fence does not justify GC. Namespace destruction, epoch rollover, bounded metadata and deletion compliance are outside this version, and require a separately specified replay-safe policy before use.

**C-14 (safety and convergence arguments).** Initially each usage is zero. The sole increment checks its home bound, duplicate reserve never increments, and a valid release subtracts once. Induction on serialized home transitions gives each usage bound; fixed shares sum to 10, proving G-01 for all message schedules. Permanent ownership and immutable records give at-most-once allocation and amount conflicts. The only successor of ACTIVE is terminal RELEASED, and cache merging never writes home state, proving no resurrection. On each compatible per-ID chain, merge is associative, commutative and idempotent and retains the maximum delivered version. Fair repeated dissemination therefore yields C-12. These are protocol arguments under assumptions, not claims established for all executions by the finite checks.

## Acceptance examples

All IDs below have the stated home; start each row from empty maps unless a sequence is given. “Accept” means a home ACCEPTED result.

| ID | Scenario | Required result / evidence |
| --- | --- | --- |
| E-01 | Partition; distinct A:x=10 and B:y=10 under original R2 | Both must accept under R2, giving 20: X-01 counterexample, not behavior of the proposal |
| E-02 | Partition; A:x=5 and B:y=5 | Both accept; global outstanding 10 |
| E-03 | Empty A; reserve A:x=6 | REJECTED_CAPACITY despite unused B capacity: declared R2 change |
| E-04 | A accepts A:x=3; retry at B; retry at A | B returns ROUTE(A); A returns ACCEPTED; A usage remains 3 |
| E-05 | A accepts A:x=3; retry A:x=4, including via B | Home returns AMOUNT_CONFLICT; B only routes; usage stays 3 |
| E-06 | Accept A:x=5; reject A:y=1; release x; retry y=1 | Release frees 5; y stays rejected; fresh A:z=1 can accept |
| E-07 | Accept A:x=5; release twice; retry reserve(x,5); receive old ACTIVE at B after RELEASED | Usage zero; release is idempotent; reserve returns ALREADY_RELEASED; B keeps RELEASED |
| E-08 | Release unknown A:x; later reserve A:x=2 | NOT_FOUND then ACCEPTED; early release was not cancellation |
| E-09 | Accept/release A:x=2; retry x=3 | AMOUNT_CONFLICT; original amount is retained after release |
| E-10 | Concurrent A:x=2 and A:x=4 | First home operation binds; second is AMOUNT_CONFLICT; only one debit |
| E-11 | Deliver duplicates and all permutations of ACTIVE, RELEASED snapshots | After RELEASED has arrived, cache remains RELEASED, usage never changes through cache merge |
| E-12 | Partition ends; messages delayed 101 ms then delivered | No promised agreement at 100 ms; eventual quiescent agreement |
| E-13 | Release x; advance more than one hour; old reserve or ACTIVE arrives | Retained record prevents resurrection; clocks do not change decisions |
| E-14 | Feed a same-ID/different-amount or contradictory-decision replication entry | Protocol fault, no overwrite or usage change |

## Verification boundary

**V-01.** `python3 checks.py` runs dependency-free finite traces and bounded state exploration tied to these clauses. It is a small reference model and a regression aid, not a production implementation, proof assistant result, network test, or performance measurement. The X-01 and X-04 traces are concrete failures of alternative policies. The X-03 schedule demonstrates an absent timing premise; it does not measure a deployment. The inductive arguments in C-14 cover unbounded schedules only subject to C-01–C-13.
