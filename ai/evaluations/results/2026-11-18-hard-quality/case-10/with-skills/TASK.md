# Build a small interval-booking library for another engineer

We need a persistent booking calendar for offline batch processing. It stores bookings by ID, and can merge independently collected calendars. A booking interval is half-open `[start,end)` with signed, arbitrary-size Python integer endpoints and `start < end`. IDs are nonempty strings. Callers supply inputs of those types; validation for other Python types is outside this task.

Public module `calendar_api.py`:

- `empty()` returns an empty calendar.
- `reserve(state, booking_id, start, end)` returns a calendar with that booking. Replaying exactly the same ID and interval is a no-op in observations. Reusing an ID with a different interval raises `ValueError`. Invalid interval ordering raises `ValueError`.
- `merge(left, right)` returns the union by ID. An ID present in both must have exactly equal intervals or the merge raises `ValueError`. Compatible merges must preserve all bookings. Repeated merge must not duplicate a booking.
- `bookings(state)` returns a tuple of `(id,start,end)` rows sorted by ID.
- `occupied(state, lo, hi)` returns sorted, disjoint, maximal half-open spans occupied within `[lo,hi)`. Adjacent spans coalesce. Equal endpoints give an empty result; `lo > hi` raises `ValueError`.
- `peak(state)` returns the maximum simultaneous booking count over all times, zero for an empty calendar. Equal endpoints must obey the half-open interpretation. Distinct IDs with identical intervals count separately.

All updates are persistent: previously obtained states must keep their observations after later operations, including after failed operations. No finite-capacity assumption or machine-integer bound is allowed. The concrete state representation is private; tests must use public observers. No threading is needed.

Deliver an implementation, a precise `spec.md` a new engineer could use without this prompt, a short `mapping.md` connecting the requirements to public functions, and standard-library `unittest` tests in `test_calendar.py`. Run the tests. In `answer.md` explain the important design choices, actual evidence and limitations. Prioritize understandable invariants, small composable algorithms, meaningful failure messages, and tests that could detect plausible alternative faulty implementations. Avoid frameworks or a catalog runtime dependency. Do not modify the catalog or invent guarantees outside this contract.
