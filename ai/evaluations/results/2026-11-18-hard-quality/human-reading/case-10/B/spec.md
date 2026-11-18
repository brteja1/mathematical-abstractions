# Persistent booking calendar

Import the six public functions from `calendar_api`. A state is an opaque value
returned by `empty`, `reserve`, or `merge`; clients must inspect it through the
public observers. Object identity, internal attributes, equality, serialization,
and mutation of private internals are not part of this API.

Inputs are nonempty string IDs and signed, arbitrary-size Python integer
endpoints. Validation of other Python types is outside the contract. Bookings
are half-open intervals: `[a,b)` contains time `t` precisely when `a <= t < b`.
Valid stored intervals satisfy `a < b`. There is no fixed calendar capacity or
machine-integer bound (ordinary available-memory limits still apply).

A state denotes a finite mapping from IDs to intervals. Distinct IDs may have
the same interval and count as distinct bookings. All operations preserve every
previously returned state's observations, including when an operation raises.
Observers have no side effects. No threading guarantees are specified.

## Public functions

- `empty()` returns the empty mapping.
- `reserve(state, booking_id, start, end)` first requires `start < end`, raising
  `ValueError` otherwise. If the ID is absent, return the mapping extended by
  that interval. If its interval is already exactly `(start,end)`, return an
  observationally identical state. If the ID has a different interval, raise
  `ValueError`. Overlap with other IDs is allowed.
- `merge(left, right)` returns their union by ID. Each shared ID must have
  exactly the same interval on both sides; otherwise raise `ValueError`.
  A shared compatible ID occurs once in the union. Compatible merge is
  observationally commutative, associative, and idempotent, with `empty()` as
  identity. Associativity applies when the input mappings are jointly compatible.
- `bookings(state)` returns a tuple of `(id,start,end)` tuples, ordered by
  Python's increasing string order on IDs. There is exactly one row per ID.
- `occupied(state, lo, hi)` raises `ValueError` for `lo > hi`, and returns `()`
  for `lo == hi`. Otherwise return a tuple of `(start,end)` tuples describing
  the union of all bookings intersected with `[lo,hi)`. Every returned span is
  nonempty and lies within the query; spans are in increasing start order.
  Consecutive spans have a strict gap: `previous_end < next_start`. Thus
  overlapping and adjacent spans coalesce, and spans are maximal in the query.
- `peak(state)` returns the maximum number of IDs covering any time, or zero
  for an empty state. At a shared endpoint, ending intervals no longer count
  and starting intervals do count. Identical intervals with different IDs each
  contribute one; replaying or merging the same ID does not increase the count.

Error messages identify invalid ordering or the conflicting ID; clients should
catch `ValueError` without depending on exact message text. A failed operation
returns no partially updated state. Outputs of observers are immutable tuples
(or an integer for `peak`) and may safely be retained across updates.
