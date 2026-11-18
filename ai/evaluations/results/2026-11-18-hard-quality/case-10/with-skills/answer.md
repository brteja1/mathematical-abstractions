# Delivery

Implemented the six public functions in `calendar_api.py`, with a standalone
contract in `spec.md`, requirement and catalog correspondence in `mapping.md`,
and standard-library tests in `test_calendar.py`.

States contain canonical immutable booking rows. Updates construct new data;
exact reservation replay can reuse the old state because equality is
observational. Merge checks ID conflicts in a temporary dictionary, so even a
late failure cannot alter either input. Overlapping bookings remain permitted.

Occupancy clips intervals to the window, then sorts and coalesces them. Peak
counts each booking separately and applies all changes at one endpoint together,
which respects half-open endpoints. Neither algorithm expands the time axis;
large signed integers need no special handling. Operations use finite growable
collections without a built-in capacity limit. Reservation and observations
favor simple code over optimized indexing; no performance promise was requested.

Validation run: `python3 -m unittest -v test_calendar.py` on Python 3.13.9.
All 9 test methods passed (see `test-results.txt`). Tests include 1,111 exhaustive
small calendars with 28 windows each, independent integer-cell count/coverage
oracles, 250 seeded branching operations with old-state rechecks, late merge
conflicts, endpoint ties, equal intervals under different IDs, negative and
150-digit-scale endpoints, and 300 simultaneous bookings. These target plausible
defects such as accidental mutation, overwrite-on-conflict, merge duplication,
closed-endpoint peaks, missed clipping, and failure to coalesce adjacency.
Static review against O1–O8 found no mismatch; hashes are in `evidence.json`.

The catalog checker passed with no errors. Focused standard-library queries were
used as mathematical reference. The ONTFS helper could not run because its
projection is missing; the catalog was left unchanged. Map and arbitrary integer
records have legacy citation gaps, retained in the mapping. The closed-interval
record was rejected as a half-open oracle. No Lean compilation or formal proof
was attempted or needed for the requested library. Passing tests and inspection
provide finite evidence, not a universal correctness proof. Input-type validation,
threading, and interpreter resource exhaustion were not tested or promised.
