# Turn a quota-service brief into a precise engineering specification

Draft an implementable specification for this product brief. The brief is a set of stakeholder requests, not a claim that all requests are jointly realizable. Preserve the requests and explain any conflicts or decisions before proposing a coherent contract. Do not silently weaken a promise.

The service has two replicas, A and B. The customer starts with a global allocation limit of 10 units and no reservations. Clients reserve positive integer amounts, receive a success or explicit rejection, and can later release an accepted reservation by ID. Reservation IDs are globally unique for distinct logical requests. Repeated delivery of the same request is a retry, not a new logical request. A message can be delayed, duplicated or reordered. A network partition may last arbitrarily long. Replicas do not crash, are honest, and can process local work while partitioned.

Stakeholder requests:

- R1: The sum of outstanding **accepted** reservations across both replicas never exceeds 10. A success is a promise from that point; reconciliation may not revoke it.
- R2: While isolated and starting with no local reservations, either replica must immediately succeed for a fresh reservation of any amount from 1 through 10. A request may be rejected only because local accepted usage would exceed 10, never because the replica cannot contact the other.
- R3: Retries of the same logical reservation must not consume extra capacity, even if the retry reaches the other replica during a partition. The same ID with a different amount is an error, not a retry.
- R4: A valid release is idempotent. Delayed retries of the original reserve and delayed reconciliation messages must not resurrect a released reservation. Request IDs are never reused for a new logical request.
- R5: After messages are eventually delivered, both replicas must agree on the logical reservation state. Stakeholders additionally ask for this agreement within 100 ms after a partition ends, but no network-delay or processing-time bound has been supplied.
- R6: Deleting old request/release metadata after a fixed one-hour retention period must remain safe even if old messages arrive later. There is no bound on how late messages can arrive.

Produce `spec.md` with explicit state, request/result semantics, invariants, transitions, assumptions, consistency model and acceptance examples. Separate original goals, demonstrated conflicts, necessary decisions and a proposed implementable contract; give stable clause IDs. You may recommend a replacement policy but must label changed stakeholder promises as proposals. Address capacity, request identity, conflict handling, release/retry ordering, reconciliation and metadata lifecycle. Explain any operational assumption or API limit required by the proposal.

Put reproducible executable checks or finite counterexample traces in `checks.py` and run them. Save an implementation-review checklist and evidence summary in `answer.md`. The spec should be usable by a new engineer without catalog expertise. Keep protocol properties separate from what a finite experiment demonstrates. Do not implement a production service, change dependencies, or edit the catalog.
