# Delivery and evidence

Implemented `calendar_api.py`, with the standalone contract in `spec.md`, a
requirement-to-function/test map in `mapping.md`, and standard-library tests in
`test_calendar.py`.

## Design

A private frozen state stores immutable `(id,start,end)` rows, sorted by ID.
Its invariant is unique IDs and strictly increasing interval endpoints within
each row. Public constructors preserve that invariant. Updates build temporary
local dictionaries and then a new tuple; they never mutate an existing state.
Conflicts can therefore be found after processing other rows without changing
either input. Exact reservation replay may return the same state; clients only
rely on its observations. Immutable observer outputs may also be retained.

Reservation and merge compare whole intervals under each ID. This preserves
identity even when multiple IDs have the same interval, and makes compatible
union idempotent. Overlap is permitted and never treated as an ID conflict.

`occupied` clips intervals to the query, drops nonintersections, sorts them, and
folds them into spans. After each fold step, the accumulated spans describe the
processed union and have strict gaps between them. Extending the last span for
both overlap and adjacency yields the required maximal spans.

`peak` sums start (+1) and end (-1) deltas at each distinct endpoint before
measuring the active count. After processing an endpoint the count describes
coverage up to the next endpoint. This avoids a transient, incorrect peak when
ends and starts coincide. Python integer arithmetic preserves huge signed
endpoints exactly; no timeline enumeration is used in the implementation.

For n bookings, reservation and merge take at most O(n log n) comparison steps
(where merge's n is the combined input size); occupied and peak also take
O(n log n), with O(n) temporary storage. Returning bookings is O(1). These are
structural bounds, not constant-time claims about arbitrarily large integers or
string comparisons. Repeated single insertions copy state data; this prioritizes
simple persistence over throughput. There is no fixed capacity constant.

## Actual verification

Ran `python3 -m unittest -v test_calendar` successfully: **10 tests, all passed**
(reported runtime 0.036 seconds). Tests inspect states only through public
functions. Evidence includes:

- All 100 ordered pairs of nonempty intervals drawn from endpoints -2 through
  2, including distinct IDs with identical intervals. A separate oracle
  enumerates integer unit cells for peak and all 28 query windows with endpoints
  -3 through 3. Integer endpoints make this an exact oracle on this small domain.
- All 256 ordered pairs of mappings on two IDs, each absent or assigned one of
  three intervals: expected conflicts, compatible unions, operand preservation,
  and commutativity are checked.
- Explicit clipping, gaps, adjacency, nesting, equal query endpoints, reversed
  query and reservation endpoints, both sorts of interval conflict, exact replay,
  merge identity/idempotence/associativity, retained outputs, persistent branches,
  and a conflict encountered after new compatible rows.
- Endpoint ties that would expose counting starts before ends, endpoints of
  magnitude `10**200`, and 300 distinct IDs sharing a single interval.

These checks target plausible errors such as interval-based deduplication,
concatenating merge results, overwriting ID conflicts, mutating inputs before a
failure, omitting clipping, failing to coalesce adjacency, and counting excluded
endpoints. They are executable evidence, not a formal proof or an exhaustive
check of all finite calendars.

## Scope and limitations

Only the Python standard library is required. A focused catalog query for
`interval` was run with `python3 catalog/scripts/catalog.py list --search
interval`; no catalog runtime or closed-interval semantics were imported into
the library. The pinned Lean project was not needed and no Lean proof is
claimed. No tool blockers occurred; catalog and shared runtimes were unchanged.

There is no validation guarantee for other Python types or IDs outside the
nonempty-string input domain. Private-state tampering, threading,
serialization, and resource/performance guarantees are outside this contract.
The tests cover finite examples and modest collection sizes, not memory
exhaustion or a throughput benchmark.
