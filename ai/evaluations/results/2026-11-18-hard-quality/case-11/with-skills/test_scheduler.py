"""Public-contract tests; no assumptions about scheduler representation or ties."""
import random
import unittest

import scheduler_api as api


class SchedulerTests(unittest.TestCase):
    def put(self, state, job, priority, expiration, now):
        self.assertIsNone(api.put(state, job, priority, expiration, now))

    def test_new_and_independent_instances(self):
        a, b = api.new(), api.new()
        self.assertEqual(api.snapshot(a, 0), ())
        with self.assertRaises(KeyError):
            api.take(a, 0)
        self.put(a, 'a', 4, 8, 0)
        self.assertEqual(api.snapshot(b, 0), ())
        self.assertEqual(api.take(a, 0), ('a', 4, 8))
        self.assertEqual(api.snapshot(a, 0), ())

    def test_replacement_updates_all_fields_and_expired_put_deletes(self):
        s = api.new()
        self.put(s, 'same', -8, 100, 0)
        self.put(s, 'other', 0, 100, 0)
        self.put(s, 'same', 9, 4, 1)
        self.assertEqual(api.snapshot(s, 1), (('other', 0, 100), ('same', 9, 4)))
        self.assertEqual(api.take(s, 1), ('other', 0, 100))
        self.assertEqual(api.take(s, 1), ('same', 9, 4))
        self.put(s, 'same', 3, 50, 1)
        self.put(s, 'same', -20, 1, 1)
        self.assertEqual(api.snapshot(s, 1), ())
        self.put(s, 'missing', 8, -100, 1)
        self.assertEqual(api.snapshot(s, 1), ())
        self.put(s, 'same', 7, 10, 1)
        self.put(s, 'same', 6, 20, 2)
        self.assertEqual(api.snapshot(s, 10), (('same', 6, 20),))

    def test_expiration_boundary_for_every_timed_operation(self):
        for operation in ('put', 'take', 'snapshot'):
            with self.subTest(operation=operation):
                s = api.new()
                for row in [('past', -100, 4), ('edge', -99, 5),
                            ('live', 2, 6), ('later', 3, 100)]:
                    self.put(s, *row, 0)
                self.assertEqual(len(api.snapshot(s, 4)), 3)
                if operation == 'put':
                    self.put(s, 'new', 4, 100, 5)
                    expected = (('later', 3, 100), ('live', 2, 6), ('new', 4, 100))
                elif operation == 'take':
                    self.assertEqual(api.take(s, 5), ('live', 2, 6))
                    expected = (('later', 3, 100),)
                else:
                    expected = (('later', 3, 100), ('live', 2, 6))
                    self.assertEqual(api.snapshot(s, 5), expected)
                self.assertEqual(api.snapshot(s, 5), expected)
                self.assertEqual(api.snapshot(s, 100), ())

    def test_snapshot_order_persistence_and_detached_result(self):
        s = api.new()
        rows = [('z', -4, 20), ('a', 5, 30), ('A', 7, 20), ('é', 1, 40)]
        for row in rows:
            self.put(s, *row, 0)
        saved = api.snapshot(s, 0)
        expected = tuple(sorted(rows))
        self.assertEqual(saved, expected)
        self.assertIsInstance(saved, tuple)
        self.assertEqual(api.snapshot(s, 0), expected)
        self.assertEqual(api.take(s, 0), ('z', -4, 20))
        self.put(s, 'a', -10, 50, 0)
        api.snapshot(s, 50)
        self.assertEqual(saved, expected)

    def test_arbitrary_integers_and_nonempty_string_ids(self):
        s = api.new()
        huge = 10 ** 100
        rows = [('10', huge, huge + 9), ('2', -huge, huge + 8),
                (' ', 0, huge + 7), ('\x00', -huge + 1, huge + 6)]
        for row in rows:
            self.put(s, *row, 0)
        self.put(s, 'expired', -huge * 2, -huge, 0)
        self.assertEqual(api.snapshot(s, huge), tuple(sorted(rows)))
        for row in sorted(rows, key=lambda r: r[1]):
            self.assertEqual(api.take(s, huge), row)
        self.assertEqual(api.snapshot(s, huge + 10), ())

    def test_ties_allow_any_minimum_and_preserve_exact_remainder(self):
        s = api.new()
        remaining = {name: (name, p, 20) for name, p in
                     [('z', -3), ('a', -3), ('m', -3), ('x', 0), ('b', 0)]}
        for row in reversed(list(remaining.values())):
            self.put(s, *row, 0)
        while remaining:
            allowed = [r for r in remaining.values()
                       if r[1] == min(x[1] for x in remaining.values())]
            got = api.take(s, 0)
            self.assertIn(got, allowed)
            del remaining[got[0]]
            self.assertEqual(api.snapshot(s, 0), tuple(sorted(remaining.values())))
        with self.assertRaises(KeyError):
            api.take(s, 0)

    def test_backwards_operations_are_atomic_and_initial_clock_is_zero(self):
        for operation in ('put', 'take', 'snapshot'):
            for populated in (False, True):
                with self.subTest(operation=operation, populated=populated):
                    s = api.new()
                    with self.assertRaises(ValueError):
                        self.invoke(operation, s, -1)
                    self.assertEqual(api.snapshot(s, 0), ())
                    if populated:
                        self.put(s, 'keep', 2, 12, 0)
                        self.put(s, 'other', 1, 30, 0)
                    before = api.snapshot(s, 10)
                    with self.assertRaises(ValueError):
                        # Would replace keep with an expired row if partly applied.
                        self.invoke(operation, s, 3)
                    with self.assertRaises(ValueError):
                        api.snapshot(s, 9)  # Detect a clock rolled back by rejection.
                    self.assertEqual(api.snapshot(s, 10), before)
                    self.assertEqual(api.snapshot(s, 12),
                                     (('other', 1, 30),) if populated else ())

    @staticmethod
    def invoke(operation, state, now):
        if operation == 'put':
            return api.put(state, 'keep', -100, 0, now)
        return getattr(api, operation)(state, now)

    def test_empty_take_and_expired_put_still_advance_time(self):
        for cause in ('empty_take', 'expired_take', 'expired_put', 'snapshot'):
            with self.subTest(cause=cause):
                s = api.new()
                if cause == 'expired_take':
                    self.put(s, 'gone', 0, 5, 0)
                if cause.endswith('take'):
                    with self.assertRaises(KeyError):
                        api.take(s, 10)
                elif cause == 'expired_put':
                    self.put(s, 'gone', 0, -5, 10)
                else:
                    self.assertEqual(api.snapshot(s, 10), ())
                with self.assertRaises(ValueError):
                    self.put(s, 'illegal', 1, 50, 9)
                self.assertEqual(api.snapshot(s, 10), ())
                c = api.clone(s)
                with self.assertRaises(ValueError):
                    api.take(c, 9)
                self.put(c, 'ok', 0, 20, 10)
                self.assertEqual(api.snapshot(s, 10), ())

    def test_clone_preserves_clock_and_is_independent_in_both_directions(self):
        s = api.new()
        self.put(s, 'a', 1, 20, 7)
        self.put(s, 'b', 2, 40, 7)
        c = api.clone(s)
        d = api.clone(c)
        for state in (s, c, d):
            with self.assertRaises(ValueError):
                api.snapshot(state, 6)
            self.assertEqual(api.snapshot(state, 7), (('a', 1, 20), ('b', 2, 40)))
        self.put(s, 'a', -2, 50, 7)
        self.assertEqual(api.take(c, 7), ('a', 1, 20))
        self.put(c, 'b', 10, 60, 8)
        self.assertEqual(api.snapshot(s, 20), (('a', -2, 50), ('b', 2, 40)))
        self.assertEqual(api.snapshot(c, 8), (('b', 10, 60),))
        self.assertEqual(api.snapshot(d, 7), (('a', 1, 20), ('b', 2, 40)))
        api.snapshot(c, 100)
        self.assertEqual(api.take(d, 7), ('a', 1, 20))
        self.assertEqual(api.take(s, 20), ('a', -2, 50))

    def test_many_jobs_without_capacity_limit(self):
        s = api.new()
        rows = [(f'job-{i:04d}', (i * 37) % 101 - 50, 1000 + i)
                for i in range(513)]
        for row in rows:
            self.put(s, *row, 0)
        self.assertEqual(api.snapshot(s, 0), tuple(sorted(rows)))
        remaining = {r[0]: r for r in rows}
        while remaining:
            got = api.take(s, 0)
            self.assertIn(got, list(remaining.values()))
            self.assertEqual(got[1], min(r[1] for r in remaining.values()))
            del remaining[got[0]]
        self.assertEqual(api.snapshot(s, 0), ())

    def test_seeded_branching_histories(self):
        # List-based oracle; only a valid observed tie choice updates its model.
        for seed in (0, 1, 7, 23, 101, 2026, 65537, 99991):
            rng = random.Random(seed)
            states = [[api.new(), 0, []]]
            for step in range(300):
                index = rng.randrange(len(states))
                state, clock, rows = states[index]
                op = rng.choice(('put', 'put', 'take', 'snapshot', 'clone'))
                with self.subTest(seed=seed, step=step, branch=index, operation=op):
                    if op == 'clone':
                        copy = [api.clone(state), clock, rows[:]]
                        if len(states) < 8:
                            states.append(copy)
                        else:
                            states[(index + 1) % len(states)] = copy
                        self.assertEqual(api.snapshot(copy[0], clock), tuple(sorted(rows)))
                        continue
                    now = clock + rng.choice((-5, -1, 0, 0, 1, 2, 7))
                    job = rng.choice(('a', 'b', 'c', '10', '2', 'é', ' '))
                    priority = rng.choice((-10**80, -3, 0, 0, 1, 10**80))
                    expiration = rng.choice((-10**80, 0, now - 1, now, now + 1,
                                             now + 5, now + 100, 10**80))
                    def call():
                        if op == 'put':
                            return api.put(state, job, priority, expiration, now)
                        return getattr(api, op)(state, now)
                    if now < clock:
                        with self.assertRaises(ValueError):
                            call()
                        with self.assertRaises(ValueError):
                            api.snapshot(state, clock - 1)
                    else:
                        live = [r for r in rows if r[2] > now]
                        if op == 'put':
                            self.assertIsNone(call())
                            live = [r for r in live if r[0] != job]
                            if expiration > now:
                                live.append((job, priority, expiration))
                        elif op == 'snapshot':
                            self.assertEqual(call(), tuple(sorted(live)))
                        elif live:
                            got = call()
                            allowed = [r for r in live if r[1] == min(x[1] for x in live)]
                            self.assertIn(got, allowed)
                            live.remove(got)
                        else:
                            with self.assertRaises(KeyError):
                                call()
                        states[index][1:] = [now, live]
                    # Observe every branch, catching aliases and unintended cross-effects.
                    for branch, accepted, expected in states:
                        self.assertEqual(api.snapshot(branch, accepted), tuple(sorted(expected)))


if __name__ == '__main__':
    unittest.main()
