Completed [spec.md](spec.md), [checks.py](checks.py), and [answer.md](answer.md).

The specification preserves the original requests, demonstrates their conflicts, and labels changed promises as proposals. It includes state, API semantics, invariants, transitions, reconciliation, retention, and acceptance examples.

`python3 checks.py` passed: 189 reachable states, 2,646 transitions, plus counterexample and replay checks. Evidence limitations and the implementation-review checklist are documented in `answer.md`.