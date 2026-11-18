#!/usr/bin/env python3
"""Finite model and counterexample traces for spec.md. Standard library only.
Run: python3 checks.py
No production service, LTL solver, or unbounded proof is implemented.
"""
from collections import deque
from dataclasses import dataclass, replace
from hashlib import sha256
from pathlib import Path
import platform

# Each record is None or (positive amount, phase); phase A/R/J means
# accepted-active / accepted-released / capacity-rejected. IDs are x=0,y=1.
# Events carry (ID index, amount, phase); their sequence is log position + 1.
@dataclass(frozen=True)
class State:
    m: tuple = (None, None)
    log: tuple = ()
    k: int = 0
    bm: tuple = (None, None)
    pending: tuple = ()  # authentic sequence numbers, not arbitrary payloads


def put(items, i, value):
    return items[:i] + (value,) + items[i + 1:]


def usage(m):
    return sum(r[0] for r in m if r is not None and r[1] == 'A')


def commit(s, i, amount, phase):
    return replace(s, m=put(s.m, i, (amount, phase)),
                   log=s.log + ((i, amount, phase),))


def reserve(s, i, amount):
    if i not in (0, 1) or type(amount) is not int or amount <= 0:
        return s, 'INVALID_ARGUMENT'
    old = s.m[i]
    if old:
        if old[0] != amount:
            return s, 'ID_AMOUNT_CONFLICT'
        return s, {'A': 'ACCEPTED_ACTIVE', 'R': 'ALREADY_RELEASED',
                   'J': 'CAPACITY_REJECTED'}[old[1]]
    phase = 'A' if usage(s.m) + amount <= 10 else 'J'
    return commit(s, i, amount, phase), (
        'ACCEPTED_ACTIVE' if phase == 'A' else 'CAPACITY_REJECTED')


def ingress(s, replica, connected, i, amount):
    if replica == 'B' and not connected:
        return s, 'UNAVAILABLE'
    return reserve(s, i, amount)


def release(s, i):
    if i not in (0, 1):
        return s, 'INVALID_ARGUMENT'
    old = s.m[i]
    if old is None or old[1] == 'J':
        return s, 'NOT_ACCEPTED'
    if old[1] == 'R':
        return s, 'RELEASED'
    return commit(s, i, old[0], 'R'), 'RELEASED'


def replay(log):
    m = (None, None)
    for i, amount, phase in log:
        m = put(m, i, (amount, phase))
    return m


def deliver(s, seq):
    assert 1 <= seq <= len(s.log)
    if seq <= s.k:
        return s
    pending = set(s.pending) | {seq}
    k, bm = s.k, s.bm
    while k + 1 in pending:
        k += 1
        pending.remove(k)
        i, amount, phase = s.log[k - 1]
        bm = put(bm, i, (amount, phase))
    return replace(s, k=k, bm=bm, pending=tuple(sorted(pending)))


def invariants(s):
    assert 0 <= usage(s.m) <= 10, s
    assert s.m == replay(s.log), s
    assert s.bm == replay(s.log[:s.k]), s
    assert 0 <= s.k <= len(s.log) <= 4
    assert all(s.k < seq <= len(s.log) for seq in s.pending)
    seen = {}
    for i, amount, phase in s.log:
        assert type(amount) is int and amount > 0
        if i in seen:
            assert seen[i] == (amount, 'A') and phase == 'R'
        else:
            assert phase in ('A', 'J')
        seen[i] = (amount, phase)


def successors(s):
    for i in (0, 1):
        for amount in (6, 10):
            t, result = reserve(s, i, amount)
            yield f'reserve({i},{amount}):{result}', t
        t, result = release(s, i)
        yield f'release({i}):{result}', t
    for seq in range(1, len(s.log) + 1):
        yield f'deliver({seq})', deliver(s, seq)
    # Explicit environment stutter and isolated-B mutation attempt.
    yield 'delay/stutter', s
    yield 'B isolated: UNAVAILABLE', ingress(s, 'B', False, 0, 6)[0]


def explore():
    initial = State()
    invariants(initial)  # nonempty initial-state set
    q, seen = deque([initial]), {initial}
    edges = self_loops = drained = 0
    while q:
        s = q.popleft()
        invariants(s)
        # Construct a permitted catch-up continuation after quiescence.
        # This is existence of a drain path, not universal temporal checking.
        caught_up = s
        for seq in range(1, len(s.log) + 1):
            caught_up = deliver(caught_up, seq)
        assert caught_up.bm == s.m and caught_up.k == len(s.log)
        drained += 1
        for action, t in successors(s):
            edges += 1
            invariants(t)
            for old, new in zip(s.m, t.m):
                if old:
                    assert new and new[0] == old[0], action
                    if old[1] in ('R', 'J'):
                        assert old == new, action
            if t == s:
                self_loops += 1
            if t not in seen:
                seen.add(t)
                q.append(t)
    print(f'Finite BFS PASS: {len(seen)} distinct/reachable states; '
          f'{edges} edges; {self_loops} self-loops; '
          f'{drained} quiescent drain paths checked.')
    print('Bounds: 2 replicas, 2 IDs, reserve amounts {6,10}, log <=4; '
          'no depth cutoff. No universal fair-liveness/deadlock check claimed.')


def original_counterexamples():
    # Enumerate the complete pair domain mandated by R2 from empty replicas.
    violations = [(a, b) for a in range(1, 11) for b in range(1, 11)
                  if a + b > 10]
    assert len(violations) == 55 and (10, 10) in violations
    print('F-CAP: partition empty A/B -> A accepts x:10 -> B accepts y:10 '
          '-> outstanding=20>10. 55/100 forced-success amount pairs violate R1.')
    # Partition end is not an upper bound on network delivery latency.
    end_ms, deadline_ms, delivery_ms = 0, 100, 101
    assert delivery_ms > end_ms + deadline_ms
    print('F-TIME: A has x, B empty; heal at 0 ms; B still empty at 100 ms; '
          'update delivered at 101 ms. Eventual delivery holds; deadline fails.')
    # Concrete unsafe TTL design, intentionally not the proposed model.
    record, active = None, False
    record, active = (10, 'A'), True
    record, active = (10, 'R'), False
    release_time_s = 1
    gc_time_s = release_time_s + 3600
    record = None  # naive complete erasure
    replay_time_s = gc_time_s + 1
    assert replay_time_s > gc_time_s and not active
    if record is None:  # unknown IDs treated as fresh
        record, active = (10, 'A'), True
    assert active
    print('F-GC: t=0 accept x:10; t=1 release x; t=3601 erase x; '
          't=3602 original reserve arrives -> x active again (R4 violation).')
    # Naive unordered reconciliation failure, separated from impossibility.
    b = 'RELEASED'
    b = 'ACTIVE'  # old acceptance blindly overwrites release
    assert b == 'ACTIVE'
    print('F-ORDER: unordered last-arrival overwrite RELEASED -> stale ACTIVE '
          'resurrects x; proposed prefix replay is checked separately.')


def examples():
    for amount in range(1, 11):
        s, result = reserve(State(), 0, amount)
        assert result == 'ACCEPTED_ACTIVE' and usage(s.m) == amount
    for invalid in (0, -1, 1.5, True, '1'):
        assert reserve(State(), 0, invalid) == (State(), 'INVALID_ARGUMENT')
    assert reserve(State(), 2, 1) == (State(), 'INVALID_ARGUMENT')
    s, result = reserve(State(), 0, 11)
    assert result == 'CAPACITY_REJECTED' and usage(s.m) == 0
    # Two different outstanding IDs, exact capacity, and release reclamation.
    s, _ = reserve(State(), 0, 6)
    t, result = reserve(s, 1, 4)
    assert result == 'ACCEPTED_ACTIVE' and usage(t.m) == 10
    t, _ = release(t, 0)
    assert usage(t.m) == 4
    t, result = reserve(s, 1, 5)
    assert result == 'CAPACITY_REJECTED' and usage(t.m) == 6
    s, _ = reserve(State(), 0, 10)
    s, _ = release(s, 0)
    s, result = reserve(s, 1, 10)
    assert result == 'ACCEPTED_ACTIVE' and usage(s.m) == 10
    # Cross-ingress retries, amount conflict, release and arbitrarily old retries.
    s, _ = reserve(State(), 0, 6)
    assert ingress(s, 'B', False, 0, 6) == (s, 'UNAVAILABLE')
    assert ingress(s, 'B', True, 0, 6) == (s, 'ACCEPTED_ACTIVE')
    assert ingress(s, 'B', True, 0, 7) == (s, 'ID_AMOUNT_CONFLICT')
    s, result = release(s, 0)
    assert result == 'RELEASED' and usage(s.m) == 0
    assert release(s, 0) == (s, 'RELEASED')
    assert reserve(s, 0, 6) == (s, 'ALREADY_RELEASED')
    assert reserve(s, 0, 7) == (s, 'ID_AMOUNT_CONFLICT')
    # Release event arrives first. Repeated delivery cannot resurrect it.
    t = deliver(s, 2)
    assert t.k == 0 and t.bm[0] is None and t.pending == (2,)
    t = deliver(t, 1)
    assert t.bm[0] == (6, 'R') and t.k == 2
    assert deliver(t, 1) == t and deliver(t, 2) == t
    # Terminal capacity rejection survives freed capacity.
    s, _ = reserve(State(), 0, 10)
    s, result = reserve(s, 1, 1)
    assert result == 'CAPACITY_REJECTED'
    s, _ = release(s, 0)
    assert reserve(s, 1, 1) == (s, 'CAPACITY_REJECTED')
    # Unknown release does not cancel future acceptance.
    assert release(State(), 0) == (State(), 'NOT_ACCEPTED')
    assert reserve(State(), 0, 1)[1] == 'ACCEPTED_ACTIVE'
    # Both serialization orders of conflicting same-ID requests.
    for first, second in ((6, 10), (10, 6)):
        s, _ = reserve(State(), 0, first)
        assert reserve(s, 0, second) == (s, 'ID_AMOUNT_CONFLICT')
    print('Targeted API/order checks PASS: fresh 1..10, invalid inputs, 11, '
          'cross-ingress retry/conflict, terminal release/rejection, '
          'out-of-order and duplicate replay, unknown release, conflict orders.')


def main():
    print('Backend: dependency-free Python explicit-state enumeration')
    print('Python:', platform.python_version())
    root = Path(__file__).resolve().parent
    for name in ('TASK.md', 'spec.md', 'checks.py'):
        print(f'SHA256 {name}: {sha256((root / name).read_bytes()).hexdigest()}')
    original_counterexamples()
    examples()
    explore()
    print('All expected counterexamples reproduced and proposed finite checks passed.')


if __name__ == '__main__':
    main()
