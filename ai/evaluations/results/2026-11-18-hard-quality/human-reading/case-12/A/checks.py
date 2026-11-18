#!/usr/bin/env python3
"""Finite executable evidence for spec.md; Python standard library only."""
from dataclasses import dataclass
from itertools import permutations


@dataclass(frozen=True)
class Record:
    amount: int
    decision: str
    phase: str
    version: int


def valid(r):
    return (type(r.amount) is int and r.amount > 0 and
            (r.decision, r.phase, r.version) in {
                ('ACCEPT', 'ACTIVE', 0), ('ACCEPT', 'RELEASED', 1),
                ('REJECT', 'REJECTED', 0)})


def merge(old, new):
    if not valid(new):
        raise ValueError('invalid record')
    if old is None:
        return new
    if old.amount != new.amount or old.decision != new.decision:
        raise ValueError('incompatible immutable fields')
    return max((old, new), key=lambda r: r.version)


class Home:
    def __init__(self, name):
        self.name = name
        self.records = {}
        self.cache = {}

    @property
    def usage(self):
        return sum(r.amount for r in self.records.values() if r.phase == 'ACTIVE')

    def reserve(self, key, amount):
        if type(amount) is not int or amount <= 0:
            return 'INVALID_INPUT'
        if key[0] != self.name:
            return 'ROUTE'
        old = self.records.get(key)
        if old:
            if old.amount != amount:
                return 'AMOUNT_CONFLICT'
            return {'ACTIVE': 'ACCEPTED', 'RELEASED': 'ALREADY_RELEASED',
                    'REJECTED': 'REJECTED_CAPACITY'}[old.phase]
        accepted = self.usage + amount <= 5
        self.records[key] = Record(amount, 'ACCEPT' if accepted else 'REJECT',
                                   'ACTIVE' if accepted else 'REJECTED', 0)
        return 'ACCEPTED' if accepted else 'REJECTED_CAPACITY'

    def release(self, key):
        if key[0] != self.name:
            return 'ROUTE'
        old = self.records.get(key)
        if old is None:
            return 'NOT_FOUND'
        if old.phase == 'REJECTED':
            return 'NOT_ACCEPTED'
        self.records[key] = Record(old.amount, 'ACCEPT', 'RELEASED', 1)
        return 'RELEASED'

    def receive(self, origin, key, record):
        if origin == self.name or origin != key[0] or origin not in {'A', 'B'}:
            raise ValueError('invalid origin')
        self.cache[key] = merge(self.cache.get(key), record)


def signature(home):
    return tuple(sorted(home.records.items()))


def counterexamples():
    # X-01: two independent R2-mandated decisions, distinct logical IDs.
    local_usage = {'A': 0, 'B': 0}
    for replica in ('A', 'B'):
        assert local_usage[replica] + 10 <= 10
        local_usage[replica] += 10
    assert sum(local_usage.values()) == 20
    print('X-01: partition -> A accepts x=10 -> B accepts y=10 -> total 20 > 10')

    # X-02: local-only dedup debits two independent physical ledgers.
    ledgers = {'A': {}, 'B': {}}
    for ledger in ledgers.values():
        ledger.setdefault('same-id', 3)
    assert sum(sum(x.values()) for x in ledgers.values()) == 6
    print('X-02: same ID=3 delivered at both homes -> naive ledgers debit 6')

    # X-04: timer-based complete forgetting plus fresh-ID admission.
    naive = {'x': 'ACTIVE'}
    naive['x'] = 'RELEASED'
    del naive['x']  # one hour later
    assert 'x' not in naive
    naive['x'] = 'ACTIVE'  # delayed original reserve
    assert naive['x'] == 'ACTIVE'
    print('X-04: accept x -> release x -> forget at 1h -> replay -> resurrect x')

    # X-03: finite admissible schedule; no network or processing time bounds.
    delivered_at_ms = 101
    b_view_at_100 = {}
    a_view_at_100 = {'x': 'ACTIVE'}
    assert delivered_at_ms > 100 and a_view_at_100 != b_view_at_100
    b_view_at_100.update(a_view_at_100)  # at 101 ms
    assert b_view_at_100 == a_view_at_100
    print('X-03: recovery t=0; first update t=101ms -> disagreement at t=100ms')


def acceptance_checks():
    a, b = Home('A'), Home('B')
    x, y = ('A', 'x'), ('B', 'y')
    assert a.reserve(x, 5) == b.reserve(y, 5) == 'ACCEPTED'
    assert a.usage + b.usage == 10
    assert b.reserve(x, 5) == 'ROUTE'
    assert a.reserve(x, 5) == 'ACCEPTED' and a.usage == 5
    assert a.reserve(x, 4) == 'AMOUNT_CONFLICT'
    assert b.release(x) == 'ROUTE'
    assert a.release(x) == a.release(x) == 'RELEASED'
    assert a.reserve(x, 5) == 'ALREADY_RELEASED'
    assert a.reserve(x, 4) == 'AMOUNT_CONFLICT' and a.usage == 0

    c = Home('A')
    assert c.reserve(('A', 'big'), 6) == 'REJECTED_CAPACITY'
    assert c.reserve(x, 5) == 'ACCEPTED'
    rejected = ('A', 'rejected')
    assert c.reserve(rejected, 1) == 'REJECTED_CAPACITY'
    c.release(x)
    assert c.reserve(rejected, 1) == 'REJECTED_CAPACITY'
    assert c.reserve(rejected, 2) == 'AMOUNT_CONFLICT'
    assert c.release(rejected) == 'NOT_ACCEPTED'
    assert c.reserve(('A', 'fresh'), 1) == 'ACCEPTED'
    unknown = ('A', 'unknown')
    assert c.release(unknown) == 'NOT_FOUND'
    assert c.reserve(unknown, 2) == 'ACCEPTED'
    for invalid in (0, -1, True, 1.5):
        before = signature(c)
        assert c.reserve(('A', 'invalid'), invalid) == 'INVALID_INPUT'
        assert signature(c) == before
    d = Home('A')
    assert d.reserve(x, 2) == 'ACCEPTED'
    assert d.reserve(x, 4) == 'AMOUNT_CONFLICT' and d.usage == 2
    print('E-02..E-10: capacity, routing, identity, sticky rejection and release checks pass')


def replication_checks():
    active = Record(3, 'ACCEPT', 'ACTIVE', 0)
    released = Record(3, 'ACCEPT', 'RELEASED', 1)
    # Six permutations, each containing duplicated old/new state.
    count = 0
    for schedule in set(permutations((active, active, released, released))):
        b = Home('B')
        seen_release = False
        for record in schedule:
            b.receive('A', ('A', 'x'), record)
            seen_release |= record == released
            if seen_release:
                assert b.cache[('A', 'x')] == released
            assert b.usage == 0
        assert b.cache[('A', 'x')] == released
        count += 1
    # Check compatible-chain join laws including absence.
    states = (None, active, released)
    def join(x, y):
        return x if y is None else merge(x, y)
    for x in states:
        assert join(x, x) == x
        for y in states:
            assert join(x, y) == join(y, x)
            for z in states:
                assert join(join(x, y), z) == join(x, join(y, z))
    b = Home('B')
    b.receive('A', ('A', 'x'), released)
    for bad in (Record(4, 'ACCEPT', 'RELEASED', 1),
                Record(3, 'REJECT', 'REJECTED', 0),
                Record(3, 'ACCEPT', 'ACTIVE', 2)):
        before = dict(b.cache)
        try:
            b.receive('A', ('A', 'x'), bad)
        except ValueError:
            pass
        else:
            raise AssertionError('incompatible replication was accepted')
        assert b.cache == before
    try:
        b.receive('B', ('A', 'x'), released)
    except ValueError:
        pass
    else:
        raise AssertionError('invalid origin accepted')
    # Quiescent two-way repair; duplicate full snapshots are harmless.
    a, b = Home('A'), Home('B')
    a.reserve(('A', 'x'), 3)
    a.release(('A', 'x'))
    b.reserve(('B', 'y'), 5)
    for _ in range(2):
        for key, record in a.records.items():
            b.receive('A', key, record)
        for key, record in b.records.items():
            a.receive('B', key, record)
    assert a.records | a.cache == b.records | b.cache
    # A stale ACTIVE cannot overwrite the authoritative release either.
    before = signature(a)
    try:
        a.receive('A', ('A', 'x'), active)
    except ValueError:
        pass
    else:
        raise AssertionError('home overwritten through replication')
    assert signature(a) == before
    print(f'E-11..E-14: {count} replay permutations, join laws, conflicts and repair pass')


def exhaustive_local_model():
    # Explore to a fixed point, not just a chosen trace depth. Finite abstraction:
    # one home, two IDs, reserve amounts 1..6, arbitrary retries and releases.
    initial = ()
    seen, pending = {initial}, [initial]
    edges = 0
    while pending:
        state = pending.pop()
        for key in (('A', 'x'), ('A', 'y')):
            for amount in (*range(1, 7), None):
                home = Home('A')
                home.records = dict(state)
                old = home.records.get(key)
                before_usage = home.usage
                if amount is None:
                    home.release(key)
                else:
                    home.reserve(key, amount)
                assert 0 <= home.usage <= 5
                if old is not None:
                    new = home.records[key]
                    assert new.amount == old.amount and new.decision == old.decision
                    if old.phase in ('RELEASED', 'REJECTED'):
                        assert new == old
                    if amount is not None:
                        assert home.usage == before_usage
                successor = signature(home)
                if successor not in seen:
                    seen.add(successor)
                    pending.append(successor)
                edges += 1
    # Each independent home obeys the same bound; sum of maxima bounds any pair.
    maximum = max(sum(r.amount for _, r in s if r.phase == 'ACTIVE') for s in seen)
    assert maximum == 5 and maximum + maximum <= 10
    print(f'Finite model: {len(seen)} reachable states, {edges} transitions; '
          'two IDs, amounts 1..6; local usage <=5, terminality, immutable identity pass')


if __name__ == '__main__':
    counterexamples()
    acceptance_checks()
    replication_checks()
    exhaustive_local_model()
    print('PASS: all finite checks. No unbounded proof or timing measurement claimed.')
