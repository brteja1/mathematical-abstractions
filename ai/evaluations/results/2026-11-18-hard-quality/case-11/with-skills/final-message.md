Created `test_scheduler.py`, `test-plan.md`, and `answer.md`.

All 11 tests pass, including 2,400 seeded history steps covering replacement, expiration, atomic time errors, cloning, and allowed tie choices.

The ONTFS query was blocked by a missing projection; focused catalog queries succeeded. Production code and catalog remain unchanged.