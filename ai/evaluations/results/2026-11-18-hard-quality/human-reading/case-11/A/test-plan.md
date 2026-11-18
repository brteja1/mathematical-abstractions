# Scheduler test plan

All observations use the five public module functions. Scheduler objects are
treated as opaque handles. Expected snapshots are sorted tuples of complete job
rows, and expected exceptions are checked by type, without matching messages.

| Test group | Purpose and oracle |
| --- | --- |
| New instances and initial clock | Both instances start empty at time zero; each timed operation rejects negative time. Inserting into one leaves the other empty. Successful puts return `None`; empty takes raise `KeyError`. |
| Snapshot | Distinct IDs, including case, numeric-looking strings, and Unicode, must be sorted by string ID independently of priority and insertion order. Repeated snapshots preserve all live jobs. A previously returned tuple remains unchanged after later mutations. |
| Replacement | Replacing the same ID changes both priority and expiration, without leaving an old version available. Shorter and longer replacement lifetimes are tested; exact snapshots and uniquely minimal takes are the oracle. |
| Expired put | A put expiring before or at the accepted time removes an existing version and does not create a missing ID. A separate live ID must survive. Includes negative expiration of large magnitude. |
| Expiration on every operation | Put, take, and snapshot each encounter jobs expiring before, exactly at, and after the requested time. Exact remaining rows establish the strict `expires_at > now` boundary. Take must ignore expired lower-priority jobs. |
| Empty take and time | Both an initially empty scheduler and one emptied by expiration raise `KeyError` at the new time. All timed calls at an earlier time must then raise `ValueError`; reuse at the same time succeeds. |
| Backward-call atomicity | Invalid insertion, replacement, expired replacement, take, and snapshot must leave jobs intact. Backward probes occur before any valid observation can mask a lowered clock. Exact snapshots and a following take check preservation of job contents. |
| Ties | Repeated takes may choose any member of the minimum-priority set. The oracle removes the returned member, verifies the remaining snapshot, and requires each tied job exactly once before the higher-priority-number job. No insertion-order tie policy is assumed. |
| Integer range | Very large positive times and expirations and signed priorities exercise Python integer semantics, including adjacent expiration boundaries. Uniquely ordered takes establish minimum-priority behavior. |
| Cloning | Populated, empty, and second-generation clones inherit accepted time. Independent replacements, insertions, takes, expiration, and clock advances on both sides must leave the other side's rows and time intact. Empty cloning follows a failed take that advanced time. |
| Mixed histories | Four fixed seeds (`0`, `17`, `103`, `20261118`), each with 240 operations, interleave puts, takes, snapshots, and clones across up to eight retained schedulers. A separate list-of-rows model filters expiration, replaces IDs, and tracks each branch's clock. A take must return an exact live minimum row; the model then removes the actual chosen row, permitting all legal tie policies. After each step, every retained branch is checked through backward-time probes and an exact snapshot. Subtests identify seed, step, branch, and operation. |

Equal-time reuse is exercised throughout. The deterministic examples isolate
boundary rules; seeded histories check their composition and repeated ID reuse.
The histories are reproducible but finite, not an exhaustive proof of the
contract. No test relies on state identity, representation, exception messages,
or private attributes.

Run from this workspace with:

```sh
python3 -m unittest -v test_scheduler
```
