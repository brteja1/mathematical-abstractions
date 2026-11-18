"""Public-API contract tests; run with python3 -m unittest -v test_scheduler."""

import random
import unittest

import scheduler_api as api


class SchedulerTests(unittest.TestCase):
    def test_new_instances_and_initial_clock(self):
        a, b = api.new(), api.new()
        for state in (a, b):
            for operation in (
                lambda: api.put(state, "negative", 1, 10, -1),
                lambda: api.take(state, -1),
                lambda: api.snapshot(state, -1),
            ):
                with self.assertRaises(ValueError):
                    operation()
            self.assertEqual(api.snapshot(state, 0), ())
            with self.assertRaises(KeyError):
                api.take(state, 0)
        self.assertIsNone(api.put(a, "a", 0, 10, 0))
        self.assertEqual(api.snapshot(b, 0), ())

    def test_snapshot_order_shape_and_no_removal(self):
        state = api.new()
        rows = [("é", -2, 30), ("a", 9, 40), ("A", 2, 20),
                ("aa", 0, 50), ("10", -3, 60), ("2", 4, 70)]
        for row in rows:
            self.assertIsNone(api.put(state, *row, 0))
        expected = tuple(sorted(rows))
        for _ in range(3):
            result = api.snapshot(state, 0)
            self.assertIsInstance(result, tuple)
            self.assertTrue(all(isinstance(row, tuple) for row in result))
            self.assertEqual(result, expected)
        saved = api.snapshot(state, 0)
        api.take(state, 0)
        api.put(state, "new", 1, 80, 0)
        self.assertEqual(saved, expected)

    def test_replacement_changes_priority_and_expiration(self):
        state = api.new()
        api.put(state, "x", -100, 100, 0)
        api.put(state, "y", 0, 100, 0)
        self.assertIsNone(api.put(state, "x", 100, 5, 0))
        self.assertEqual(api.take(state, 0), ("y", 0, 100))
        self.assertEqual(api.snapshot(state, 5), ())
        api.put(state, "x", 10, 6, 5)
        api.put(state, "x", -10, 100, 5)
        self.assertEqual(api.snapshot(state, 6), (("x", -10, 100),))
        self.assertEqual(api.take(state, 6), ("x", -10, 100))
        with self.assertRaises(KeyError):
            api.take(state, 6)

    def test_expired_put_deletes_existing_id(self):
        for expiration in (-10**100, -1, 0, 4, 5):
            with self.subTest(expiration=expiration):
                state = api.new()
                api.put(state, "x", -9, 100, 0)
                api.put(state, "keep", 2, 100, 0)
                self.assertIsNone(api.put(state, "x", -20, expiration, 5))
                self.assertIsNone(api.put(state, "absent", 0, expiration, 5))
                self.assertEqual(api.snapshot(state, 5), (("keep", 2, 100),))

    def test_every_timed_operation_purges_at_boundary(self):
        for kind in ("put", "take", "snapshot"):
            with self.subTest(kind=kind):
                state = api.new()
                for row in (("expired", -100, 4), ("boundary", -50, 5),
                            ("live", 0, 6), ("later", 1, 9)):
                    api.put(state, *row, 0)
                if kind == "put":
                    api.put(state, "fresh", 3, 10, 5)
                    expected = (("fresh", 3, 10), ("later", 1, 9), ("live", 0, 6))
                elif kind == "take":
                    self.assertEqual(api.take(state, 5), ("live", 0, 6))
                    expected = (("later", 1, 9),)
                else:
                    expected = (("later", 1, 9), ("live", 0, 6))
                    self.assertEqual(api.snapshot(state, 5), expected)
                self.assertEqual(api.snapshot(state, 5), expected)

    def test_empty_take_still_advances_clock(self):
        for initially_expiring in (False, True):
            with self.subTest(initially_expiring=initially_expiring):
                state = api.new()
                if initially_expiring:
                    api.put(state, "gone", 1, 7, 0)
                with self.assertRaises(KeyError):
                    api.take(state, 7)
                self.assert_rejects_all(state, 6)
                self.assertEqual(api.snapshot(state, 7), ())
                api.put(state, "new", 0, 8, 7)
                self.assertEqual(api.take(state, 7), ("new", 0, 8))

    def assert_rejects_all(self, state, now):
        with self.assertRaises(ValueError):
            api.put(state, "probe", -1000, 10000, now)
        with self.assertRaises(ValueError):
            api.take(state, now)
        with self.assertRaises(ValueError):
            api.snapshot(state, now)

    def test_backward_calls_are_atomic(self):
        for kind in ("replace", "expired_replace", "insert", "take", "snapshot"):
            with self.subTest(kind=kind):
                state = api.new()
                rows = (("x", -2, 11), ("y", 4, 100))
                for row in rows:
                    api.put(state, *row, 10)
                with self.assertRaises(ValueError):
                    if kind == "replace":
                        api.put(state, "x", 99, 200, 5)
                    elif kind == "expired_replace":
                        api.put(state, "x", 99, 0, 5)
                    elif kind == "insert":
                        api.put(state, "z", -99, 200, 5)
                    elif kind == "take":
                        api.take(state, 5)
                    else:
                        api.snapshot(state, 5)
                # Probe before a valid call can reset an incorrectly lowered clock.
                self.assert_rejects_all(state, 9)
                self.assertEqual(api.snapshot(state, 10), rows)
                self.assertEqual(api.take(state, 10), rows[0])

    def test_ties_allow_any_minimum_and_remove_once(self):
        state = api.new()
        remaining = {("a", -7, 10), ("b", -7, 20), ("c", -7, 30)}
        for row in sorted(remaining):
            api.put(state, *row, 0)
        api.put(state, "higher", -6, 40, 0)
        while remaining:
            row = api.take(state, 0)
            self.assertIn(row, remaining)
            remaining.remove(row)
            self.assertEqual(api.snapshot(state, 0),
                             tuple(sorted(remaining | {("higher", -6, 40)})))
        self.assertEqual(api.take(state, 0), ("higher", -6, 40))
        with self.assertRaises(KeyError):
            api.take(state, 0)

    def test_arbitrary_integer_magnitudes(self):
        state = api.new()
        huge = 10**100
        rows = (("low", -huge, huge + 1), ("zero", 0, huge + 2),
                ("high", huge, huge + 3))
        for row in rows:
            api.put(state, *row, huge)
        for row in rows:
            self.assertEqual(api.take(state, huge), row)
        api.put(state, "boundary", 0, huge + 1, huge)
        self.assertEqual(api.snapshot(state, huge + 1), ())
        self.assert_rejects_all(state, huge)

    def test_clone_jobs_clocks_and_bidirectional_independence(self):
        source = api.new()
        api.put(source, "soon", -1, 8, 5)
        api.put(source, "long", 1, 100, 5)
        copy = api.clone(source)
        self.assert_rejects_all(copy, 4)
        api.put(copy, "long", -5, 90, 5)
        api.put(copy, "copy", 2, 100, 5)
        self.assertEqual(api.take(source, 5), ("soon", -1, 8))
        api.put(source, "source", 3, 100, 10)
        self.assertEqual(api.snapshot(copy, 5),
                         (("copy", 2, 100), ("long", -5, 90), ("soon", -1, 8)))
        self.assertEqual(api.snapshot(copy, 8), (("copy", 2, 100), ("long", -5, 90)))
        self.assertEqual(api.snapshot(source, 10), (("long", 1, 100), ("source", 3, 100)))
        api.take(copy, 20)
        self.assertEqual(api.snapshot(source, 10), (("long", 1, 100), ("source", 3, 100)))

    def test_clone_empty_clock_and_clone_of_clone(self):
        source = api.new()
        with self.assertRaises(KeyError):
            api.take(source, 20)
        copy = api.clone(source)
        third = api.clone(copy)
        for state in (source, copy, third):
            self.assert_rejects_all(state, 19)
            self.assertEqual(api.snapshot(state, 20), ())
        api.put(third, "third", 0, 50, 20)
        api.snapshot(copy, 40)
        api.put(source, "source", 1, 50, 20)
        self.assertEqual(api.snapshot(third, 20), (("third", 0, 50),))
        self.assertEqual(api.snapshot(source, 20), (("source", 1, 50),))
        self.assertEqual(api.snapshot(copy, 40), ())

    def test_reproducible_mixed_histories(self):
        # Model rows use a list. Tied takes update it using the actual valid choice.
        for seed in (0, 17, 103, 20261118):
            rng = random.Random(seed)
            states = [(api.new(), [], 0)]
            for step in range(240):
                index = rng.randrange(len(states))
                state, rows, clock = states[index]
                kind = rng.choice(("put", "put", "put", "take", "snapshot", "clone"))
                with self.subTest(seed=seed, step=step, state=index, operation=kind):
                    if kind == "clone":
                        copy = api.clone(state)
                        self.assert_rejects_all(copy, clock - 1)
                        self.assertEqual(api.snapshot(copy, clock), tuple(sorted(rows)))
                        if len(states) < 8:
                            states.append((copy, list(rows), clock))
                    else:
                        now = clock + rng.choice((-3, -1, 0, 0, 0, 1, 2, 8))
                        job_id = rng.choice(("a", "b", "c", "A", "10", "é"))
                        priority = rng.choice((-10**80, -3, -1, 0, 0, 1, 3, 10**80))
                        expiration = rng.choice((-10**80, 0, now - 1, now, now + 1,
                                                 now + 4, now + 50, 10**80))

                        def call():
                            if kind == "put":
                                return api.put(state, job_id, priority, expiration, now)
                            if kind == "take":
                                return api.take(state, now)
                            return api.snapshot(state, now)

                        if now < clock:
                            with self.assertRaises(ValueError):
                                call()
                        else:
                            rows = [row for row in rows if row[2] > now]
                            clock = now
                            if kind == "put":
                                self.assertIsNone(call())
                                rows = [row for row in rows if row[0] != job_id]
                                if expiration > now:
                                    rows.append((job_id, priority, expiration))
                            elif kind == "take":
                                if rows:
                                    result = call()
                                    self.assertIsInstance(result, tuple)
                                    minimum = min(row[1] for row in rows)
                                    self.assertIn(result, [row for row in rows if row[1] == minimum])
                                    rows.remove(result)
                                else:
                                    with self.assertRaises(KeyError):
                                        call()
                            else:
                                self.assertEqual(call(), tuple(sorted(rows)))
                        states[index] = (state, rows, clock)
                    # Observe every branch, exposing accidental aliasing of jobs or clocks.
                    for observed, expected, time in states:
                        self.assert_rejects_all(observed, time - 1)
                        self.assertEqual(api.snapshot(observed, time), tuple(sorted(expected)))


if __name__ == "__main__":
    unittest.main()
