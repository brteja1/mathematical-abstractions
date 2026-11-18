# Persistent booking calendar specification — revision 1

This document specifies the public Python module `calendar_api.py` for sequential,
offline batch processing. No catalog package is needed at runtime.

## S1. Values and observations

A calendar represents a finite partial map B from nonempty string booking IDs to
pairs of signed, arbitrary-size Python integers (s,e), with s < e. The interval
is half-open: t is covered exactly when s <= t < e. Callers supply the stated
input types and nonempty IDs; other types and empty IDs are outside the contract.
States passed to functions are obtained from this API. IDs use Python string
value equality and sorting. Integers are exact; there is no fixed capacity or
machine-integer bound. Endpoint values have no prescribed units.

States are opaque. Two states are observationally equal when their ID-to-interval
maps agree, equivalently when `bookings` agrees. Object identity is unspecified.
Distinct IDs with equal intervals are distinct bookings.

## S2. Construction

`empty()` returns a state representing the map with no bindings.

## S3. Reservation

`reserve(state, booking_id, start, end)` returns a state representing B with the
specified binding added. It raises `ValueError` if start >= end. If the ID is
already present with exactly this pair, the result is observationally equal to
state. If that ID has a different pair, it raises `ValueError`. Every unrelated
binding is preserved. Error message wording and precedence between simultaneous
errors are unspecified.

## S4. Merge

`merge(left, right)` returns the union of both maps if every common ID has equal
endpoint pairs. Otherwise it raises `ValueError`. No binding is lost or counted
twice by ID. On compatible inputs, merge is observationally commutative,
associative, idempotent, and has `empty()` as identity. Associativity is asserted
for triples whose bindings are jointly compatible; it does not prescribe error
precedence for conflicting triples.

## S5. Booking observer

`bookings(state)` returns a tuple of `(id, start, end)` tuples, one per binding,
sorted by ID in ascending Python string order.

## S6. Occupancy observer

`occupied(state, lo, hi)` returns a tuple of `(start, end)` tuples representing
exactly the union of booking intervals intersected with [lo,hi). Each returned
span has start < end. Spans are sorted by start, and consecutive spans have a
strict gap: previous end < next start. Thus overlapping and adjacent occupied
spans coalesce into maximal spans. Return `()` for lo == hi. Raise `ValueError`
for lo > hi. A booking ending at lo or starting at hi contributes nothing.

## S7. Peak observer

`peak(state)` returns the integer maximum of the count
`#{id in dom(B) : B[id].start <= t < B[id].end}` over all times t; for an empty
calendar it returns zero. A booking ending at t is absent at t, while one
starting there is present. Identical intervals under distinct IDs contribute
separately. With integer endpoints, counts are constant between consecutive
endpoints, so considering endpoint times suffices.

## S8. Persistence and scope

Every operation preserves all observations of every previously obtained state,
including both merge operands and states involved in failed operations. Observers
have no state effects. Returned observations consist of immutable tuples and
values. There is no threading contract, serialization format, deletion API,
reservation-conflict policy for overlapping intervals, or performance guarantee.
The library imposes no capacity bound; actual interpreter memory and execution
resources remain finite. Validation for input types outside S1 is unspecified.
