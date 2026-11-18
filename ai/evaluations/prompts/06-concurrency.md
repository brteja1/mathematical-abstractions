# Check a two-client lock

Two clients share `busy = false`. Each starts at program counter 0. Each numbered action below is atomic, but the check and the assignment are separate actions:

0. Read `busy` into a client-local Boolean `seen`, then advance to 1.
1. If `seen` is false, set `busy = true` and advance to 2; otherwise return to 0.
2. Enter the critical section and advance to 3.
3. Exit the critical section, set `busy = false`, and return to 0.

A client is inside its critical section at program counter 3. Any enabled client action can run next. The scheduler is arbitrary; no fairness condition is supplied.

Check mutual exclusion and assess the claim that every client eventually enters. Produce an executable finite-state explorer (Python is acceptable), a concrete counterexample if any, the exact action granularity and bounds checked, and a proposed repair. Keep the original model intact and state which guarantees your evidence establishes. Save `answer.md` and `checks.py`; run the explorer. Do not edit the catalog or claim that a finite check proves an unbounded implementation.
