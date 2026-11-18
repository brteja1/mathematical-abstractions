# Scheduler test plan

The oracle is the public contract in `TASK.md`. Tests import only `scheduler_api`'s five public functions and never inspect scheduler state. Equality is exact Python tuple/string/integer equality; snapshots must be tuples ordered by Python string job ID. Tests have no external dependencies.

## Groups and oracles

| Tests | Purpose and oracle |
| --- | --- |
| `new_and_independent_instances` | Empty construction, singleton removal, empty `KeyError`, independent fresh schedulers, and `put` returning `None`; direct expected rows. |
| `replacement_updates_all_fields_and_expired_put_deletes` | Replacement changes priority and expiration without duplicate IDs, stale old expiration cannot remove a replacement, expired replacement deletes the existing ID, and expired absent insertion is a no-op on jobs. Exact snapshots and removals. |
| `expiration_boundary_for_every_timed_operation` | Each timed operation purges all expired rows, including nonselected jobs; expiration equal to now is dead and expiration one step later is live. Exact before/after rows at successive times. |
| `snapshot_order_persistence_and_detached_result` | ID sorting differs from priority and insertion order; repeated observations preserve live jobs and previously returned tuples keep their value after mutations and expiration. |
| `arbitrary_integers_and_nonempty_string_ids` | Signed priorities and times/expirations beyond fixed-width ranges, negative expiration, numeric-looking strings, whitespace, Unicode and NUL IDs; exact integer ordering and rows. No assumptions about normalization or machine word size. |
| `ties_allow_any_minimum_and_preserve_exact_remainder` | Return must belong to the set of currently minimal rows, with exactly that row removed. Drain all jobs and check empty behavior. No tie order is required. |
| `backwards_operations_are_atomic_and_initial_clock_is_zero` | All timed operations reject negative initial time and later backwards time, on empty and populated states. Compare jobs at the last accepted time; a second rejected observation just below that clock detects rollback. An attempted expired replacement must not delete a live job. Later expiration verifies retained fields. |
| `empty_take_and_expired_put_still_advance_time` | Empty/expiration-induced failing takes, expired puts and empty snapshots commit their accepted time. Earlier puts fail and insert nothing; clones inherit the committed clock, including after `KeyError`. |
| `clone_preserves_clock_and_is_independent_in_both_directions` | Clone and clone-of-clone inherit jobs/time. Replacements, removals, expiration and time advances on each branch cannot affect others. Branches may keep different accepted clocks. |
| `many_jobs_without_capacity_limit` | Insert 513 distinct jobs with tied priorities, compare the full snapshot, then check membership/minimality and exact-once removal through exhaustion. Finite capacity stress, not proof of unbounded storage. |
| `seeded_branching_histories` | Eight fixed seeds × 300 steps, up to eight retained branches. A separate list-of-rows model checks mixed replacement, expiration, valid/invalid/equal time, snapshots, takes, and cloning. Rejected calls preserve model jobs/time; accepted empty takes advance model time. Only after validating a take against all allowed minima does the model remove its actual returned row. Every retained branch is observed after each timed step to detect cross-branch mutation. Failure subtests identify seed, step, branch and operation; the prefix is reproduced by rerunning that seed. |

## Catalog mapping and applicability

Focused retrieval commands:

```sh
python3 catalog/scripts/catalog.py check
python3 catalog/scripts/catalog.py list --search PriorityQueue
python3 catalog/scripts/catalog.py get PriorityQueue --sections operations axioms laws
```

Selected concept: `urn:csabs:concept/PriorityQueue`. Selected claims:

- `urn:csabs:axiom/PriorityQueue-bag-model`: a finite bag with totally ordered keys.
- `urn:csabs:axiom/PriorityQueue-insert`: insertion adds exactly one occurrence, applied only to a fresh ID with live expiration after time advancement.
- `urn:csabs:axiom/PriorityQueue-minimum-removal`: for a nonempty bag, return any minimal item and remove exactly its occurrence.

All three claims and the concept report `provenanceStatus: legacy-source-missing`; the claims report editorial summaries, not machine proofs. These are mathematical design guidance, with the task contract independently establishing the software obligations. No theorem or Lean witness is used, and no proof or repaired citation is claimed.

The finite bag consists of live `(job_id, priority, expires_at)` rows with unique IDs, with key `row[1]` in the total order of arbitrary Python integers. `PriorityQueue-basis-empty` maps to `api.new()` observed by `api.snapshot(state, 0)`. `PriorityQueue-insert` maps to a live, fresh-ID `api.put` through its before/after observations; its mathematical result is a state, whereas the mutable API returns `None`. `PriorityQueue-extractMin` maps to `api.take`, returning the row and mutating the observed remainder. `api.snapshot` is the contract-specific observer: exact ID-sorted tuple equality represents bag equality because IDs are unique.

For extraction, first apply the contract's accepted time advance and expiration filter, then apply minimum-removal only when the live bag is nonempty. Empty extraction is mathematically undefined; its `KeyError` and clock effects come exclusively from the task contract. Ties are relational: compare the returned row against all minima, then compare the remainder after deleting that specific row. Constructors, mutations, observations and partial results used by these properties are all covered by this mapping.

Replacement, deletion by expired put, time monotonicity, atomic rejection, sorted observation and `api.clone` are additional contract-defined transitions, not consequences of a plain priority queue. Clone copies the oracle list and clock; independence is judged by later public observations. No general bag-insertion law is applied to replacement or expired insertion. Sequential execution and exact integers are assumed; stability, FIFO tie order, concurrency, performance guarantees and invalid input types are outside scope. No additional mathematical abstraction is needed for the explicit task-defined transition model.

## Retrieval limitation

The prescribed ONTFS wrapper attempt was:

```sh
python3 catalog/ai/skills/mathematical-tests/scripts/query.py search priority --limit 4 --max-chars 5000
```

It exited 1: `Test context error: ONTFS projection is missing. Run scripts/ontology.py build with the same --directory.` The catalog integrity check succeeded (264 concepts, 2,484 nodes, no errors). Focused dependency-free `catalog.py` retrieval succeeded. The catalog was left unchanged as required; no ONTFS query success is claimed.

These finite examples and histories provide regression evidence, not universal correctness or a refinement proof.
