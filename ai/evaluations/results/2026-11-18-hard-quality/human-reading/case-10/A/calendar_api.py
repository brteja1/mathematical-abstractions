"""Persistent ID-indexed half-open bookings. See spec.md for the public contract."""

from dataclasses import dataclass

__all__ = ["empty", "reserve", "merge", "bookings", "occupied", "peak"]


@dataclass(frozen=True, slots=True)
class _Calendar:
    # Canonical immutable rows: unique IDs, sorted by ID, start < end.
    rows: tuple[tuple[str, int, int], ...]


def empty():
    """Return an empty calendar."""
    return _Calendar(())


def reserve(state, booking_id, start, end):
    """Add a binding, replay it, or raise ValueError on ordering/ID conflict."""
    if start >= end:
        raise ValueError("booking start must be less than end")
    for old_id, old_start, old_end in state.rows:
        if old_id == booking_id:
            if (old_start, old_end) != (start, end):
                raise ValueError(f"conflicting interval for booking ID {booking_id!r}")
            return state
    return _Calendar(tuple(sorted(state.rows + ((booking_id, start, end),))))


def merge(left, right):
    """Union by ID; conflicting intervals raise ValueError."""
    # Only this local dictionary is mutated, including before a late conflict.
    bindings = {key: (start, end) for key, start, end in left.rows}
    for key, start, end in right.rows:
        interval = (start, end)
        if key in bindings and bindings[key] != interval:
            raise ValueError(f"conflicting interval for booking ID {key!r}")
        bindings[key] = interval
    return _Calendar(tuple((key, *bindings[key]) for key in sorted(bindings)))


def bookings(state):
    """Return immutable booking rows sorted by ID."""
    return state.rows


def occupied(state, lo, hi):
    """Return maximal occupied spans clipped to [lo, hi)."""
    if lo > hi:
        raise ValueError("query lower endpoint must not exceed upper endpoint")
    if lo == hi:
        return ()
    clipped = sorted(
        (max(start, lo), min(end, hi))
        for _, start, end in state.rows
        if start < hi and lo < end
    )
    spans = []
    for start, end in clipped:
        if spans and start <= spans[-1][1]:
            spans[-1] = (spans[-1][0], max(spans[-1][1], end))
        else:
            spans.append((start, end))
    return tuple(spans)


def peak(state):
    """Return the maximum simultaneous count, respecting half-open endpoints."""
    changes = {}
    for _, start, end in state.rows:
        changes[start] = changes.get(start, 0) + 1
        changes[end] = changes.get(end, 0) - 1
    active = maximum = 0
    for time in sorted(changes):
        # Group all changes at time before measuring; no artificial tie peak.
        active += changes[time]
        maximum = max(maximum, active)
    return maximum
