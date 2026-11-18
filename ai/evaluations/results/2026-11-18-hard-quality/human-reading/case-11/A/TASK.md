# Design a test suite for an opaque expiring job scheduler

Write standard-library `unittest` tests in `test_scheduler.py` for `import scheduler_api as api`. A reference implementation is supplied as `scheduler_api.py`; do not modify it. Other correct implementations may use different private state types and choose different tied jobs.

Contract:

- `new()` creates an empty mutable scheduler with logical time 0.
- `put(state, job_id, priority, expires_at, now)` first advances time and purges every job with `expires_at <= now`. It then replaces any job with this ID. If the supplied expiration is already `<= now`, the result has no job with that ID. The return value is `None`.
- `take(state, now)` advances time, purges expired jobs, removes and returns a live minimum-priority job as `(job_id, priority, expires_at)`. Any tied minimum may be chosen. Empty `take` raises `KeyError`; advancing time and expiration still take effect.
- `snapshot(state, now)` advances time, purges expired jobs and returns a tuple of live job rows sorted by job ID. It does not remove live jobs.
- `clone(state)` returns an independent scheduler with the same jobs and logical time. Changes to either copy must not affect the other.
- Time starts at 0 and may stay equal or increase. Every timed operation with `now` less than that scheduler's last accepted time raises `ValueError` and leaves jobs and time unchanged. No expiration or partial update may occur on this rejected call. A clone inherits its source's last accepted time.

Job IDs are nonempty strings, priorities are arbitrary signed Python integers, expiration and `now` are arbitrary Python integers. Inputs are of these types. Negative expiration simply denotes an already expired job; negative `now` is backwards from the initial clock. No capacity limit applies. Only these module functions are public; do not inspect private attributes or depend on internal containers.

The suite should give a maintainer confidence in replacement, expiration, time errors, cloning, mixed operation histories, and allowed tie choices—not just happy paths. Put a concise explanation of each test group's purpose and oracle in `test-plan.md`, with a reproducible command and actual results in `answer.md`. Run the suite. Do not repair production code, alter the contract or change the catalog. The amount of code or number of tests is not itself a quality goal.
