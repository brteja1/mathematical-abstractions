# Requirement mapping

| Requirement | Public entry point and mechanism | Main test coverage |
| --- | --- | --- |
| Empty, persistent finite mapping | `empty`; immutable state rows | empty, persistence and retained observer results |
| Valid intervals, exact replay, ID conflicts | `reserve`; validate ordering, compare interval by ID | reservation errors, replay, overlap and duplicate intervals |
| Compatible ID union, conflict rejection, deduplication | `merge`; compare shared IDs before producing result | merge laws, late conflict, exhaustive pair unions |
| Stable ID ordering | `bookings`; canonical sorted rows | out-of-order insertion and oracle comparisons |
| Clipped maximal half-open union | `occupied`; clip, sort, coalesce overlaps and adjacency | boundary cases and small-domain coverage oracle |
| Half-open maximum multiplicity | `peak`; aggregate endpoint deltas, prefix sums | tied endpoints, distinct IDs, small-domain counting oracle |
| Signed arbitrary-size endpoints, no fixed capacity | All endpoint algorithms use Python integers; storage grows with inputs | huge offsets and a larger booking collection |

`test_calendar.py` uses only these public functions to observe states. The
catalog is reference material only; implementation and tests import no catalog
or third-party runtime.
