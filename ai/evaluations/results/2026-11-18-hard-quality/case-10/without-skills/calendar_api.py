"""Persistent, ID-keyed half-open booking calendars. See spec.md."""

from dataclasses import dataclass

__all__ = ["empty", "reserve", "merge", "bookings", "occupied", "peak"]


@dataclass(frozen=True)
class _Calendar:
    # Unique IDs, sorted by ID; every interval has start < end.
    # Tuples and their string/integer contents are immutable.
    rows: tuple


def empty():
    """Return an empty calendar."""
    return _Calendar(())


def reserve(state, booking_id, start, end):
    """Add an ID, replay it, or raise ValueError for invalid/conflicting input."""
    if start >= end:
        raise ValueError("booking start must be less than end")
    entries = {key: (a, b) for key, a, b in state.rows}
    interval = (start, end)
    if booking_id in entries:
        if entries[booking_id] != interval:
            raise ValueError(f"conflicting interval for booking ID {booking_id!r}")
        return state
    entries[booking_id] = interval
    return _from_entries(entries)


def _from_entries(entries):
    return _Calendar(tuple((key, *entries[key]) for key in sorted(entries)))


def merge(left, right):
    """Union compatible calendars by ID; reject any conflicting shared ID."""
    entries = {key: (a, b) for key, a, b in left.rows}
    for key, a, b in right.rows:
        interval = (a, b)
        if key in entries and entries[key] != interval:
            raise ValueError(f"conflicting interval for booking ID {key!r}")
        entries[key] = interval
    return _from_entries(entries)


def bookings(state):
    """Return immutable (ID, start, end) rows in increasing ID order."""
    return state.rows


def occupied(state, lo, hi):
    """Return maximal occupied spans clipped to [lo, hi), as a tuple."""
    if lo > hi:
        raise ValueError("query lo must be less than or equal to hi")
    if lo == hi:
        return ()
    clipped = sorted(
        (max(a, lo), min(b, hi))
        for _, a, b in state.rows
        if a < hi and lo < b
    )
    spans = []
    for a, b in clipped:
        if spans and a <= spans[-1][1]:
            spans[-1] = (spans[-1][0], max(spans[-1][1], b))
        else:
            spans.append((a, b))
    return tuple(spans)


def peak(state):
    """Return maximum simultaneous count, treating ends as excluded."""
    deltas = {}
    for _, a, b in state.rows:
        deltas[a] = deltas.get(a, 0) + 1
        deltas[b] = deltas.get(b, 0) - 1
    active = best = 0
    for time in sorted(deltas):
        # Apply ALL starts and ends at this time before measuring [time, next).
        active += deltas[time]
        best = max(best, active)
    return best
