"""Public-observer tests; O1–O8 and catalog correspondence are in mapping.md."""
import itertools
import random
import unittest

from calendar_api import empty, reserve, merge, bookings, occupied, peak


def build(rows):
    state = empty()
    for key, start, end in rows:
        state = reserve(state, key, start, end)
    return state


def model_observation(model, lo=-6, hi=7):
    """Independent bounded oracle: count each integer unit cell, no sweep/sort merge.

    All test endpoints are integers. A count on [t,t+1) is exactly the count
    at t; hence these cells determine the exact spans for the bounded window.
    """
    cells = [sum(a <= t < b for a, b in model.values()) for t in range(lo, hi)]
    spans = []
    run = None
    for t, count in zip(range(lo, hi), cells):
        if count and run is None:
            run = t
        elif not count and run is not None:
            spans.append((run, t))
            run = None
    if run is not None:
        spans.append((run, hi))
    rows = tuple(sorted((key, a, b) for key, (a, b) in model.items()))
    # Generated bookings lie inside this window, so this is the global peak.
    return rows, tuple(spans), max(cells, default=0)


def observe(state, lo=-6, hi=7):
    return bookings(state), occupied(state, lo, hi), peak(state)


class CalendarTests(unittest.TestCase):
    def test_empty_and_ordering(self):  # O1, O4, O5, O6
        self.assertEqual(observe(empty()), ((), (), 0))
        state = build([('z', 8, 10), ('A', -2, 0), ('a', 1, 2), ('ä', 3, 4)])
        self.assertEqual(bookings(state), (('A', -2, 0), ('a', 1, 2),
                                           ('z', 8, 10), ('ä', 3, 4)))
        self.assertIsInstance(bookings(state), tuple)
        self.assertTrue(all(isinstance(row, tuple) for row in bookings(state)))

    def test_replay_and_distinct_ids(self):  # O2, O6
        base = reserve(empty(), 'one', -3, 7)
        self.assertEqual(observe(reserve(base, 'one', -3, 7)), observe(base))
        two = reserve(base, 'two', -3, 7)
        self.assertEqual(peak(two), 2)
        self.assertEqual(occupied(two, -10, 10), ((-3, 7),))
        self.assertEqual(peak(merge(two, two)), 2)
        self.assertEqual(len(bookings(two)), 2)
        self.assertEqual(peak(base), 1)

    def test_errors_preserve_all_observations(self):  # O2, O3, O7
        left = build([('m', 0, 3), ('z', 5, 8)])
        # A compatible new key precedes the conflict in ID order.
        right = build([('a', -4, -2), ('z', 5, 9)])
        before = observe(left), observe(right)
        for a, b in [(3, 3), (4, 3), (-2, -9)]:
            with self.subTest(interval=(a, b)):
                with self.assertRaises(ValueError):
                    reserve(left, 'new', a, b)
                self.assertEqual((observe(left), observe(right)), before)
        for a, b in [(0, 4), (-1, 3), (-1, 4)]:
            with self.assertRaises(ValueError):
                reserve(left, 'm', a, b)
            self.assertEqual(observe(left), before[0])
        for a, b in [(left, right), (right, left)]:
            with self.assertRaises(ValueError):
                merge(a, b)
            self.assertEqual((observe(left), observe(right)), before)
        with self.assertRaises(ValueError):
            occupied(left, 3, 2)
        self.assertEqual(observe(left), before[0])
        self.assertEqual(bookings(reserve(left, 'new', 10, 11))[-1], ('z', 5, 8))

    def test_clipping_nesting_adjacency_and_gaps(self):  # O5
        state = build([('a', -10, -5), ('b', -5, 0), ('c', -4, -2),
                       ('d', 2, 8), ('e', 3, 4), ('f', 8, 11), ('g', 20, 22)])
        self.assertEqual(occupied(state, -7, 10), ((-7, 0), (2, 10)))
        self.assertEqual(occupied(state, 0, 2), ())
        self.assertEqual(occupied(state, 11, 20), ())
        self.assertEqual(occupied(state, -100, 100), ((-10, 0), (2, 11), (20, 22)))
        self.assertEqual(occupied(state, -3, -3), ())
        self.assertEqual(occupied(state, 30, 40), ())

    def test_peak_half_open_ties(self):  # O6
        adjacent = build([('a', -1, 0), ('b', 0, 1)])
        self.assertEqual(peak(adjacent), 1)
        self.assertEqual(occupied(adjacent, -1, 1), ((-1, 1),))
        ties = build([('a', -3, 0), ('b', -2, 0), ('c', 0, 2),
                      ('d', 0, 3), ('e', -1, 1)])
        self.assertEqual(peak(ties), 3)

    def test_merge_laws_on_jointly_compatible_states(self):  # O3
        a = build([('x', 0, 4), ('shared', -1, 1)])
        b = build([('y', 3, 7), ('shared', -1, 1)])
        c = build([('z', 7, 9), ('x', 0, 4)])
        expected = build([('x', 0, 4), ('y', 3, 7), ('z', 7, 9), ('shared', -1, 1)])
        self.assertEqual(observe(merge(a, b)), observe(merge(b, a)))
        self.assertEqual(observe(merge(merge(a, b), c)), observe(expected))
        self.assertEqual(observe(merge(a, merge(b, c))), observe(expected))
        for state in (a, b, c):
            self.assertEqual(observe(merge(state, state)), observe(state))
            self.assertEqual(observe(merge(empty(), state)), observe(state))
            self.assertEqual(observe(merge(state, empty())), observe(state))

    def test_arbitrary_integers_and_no_small_capacity(self):  # O8
        big = 10 ** 150
        state = build([('neg', -big, -big + 2), ('pos', big, big + 3)])
        self.assertEqual(occupied(state, -big - 1, big + 4),
                         ((-big, -big + 2), (big, big + 3)))
        self.assertEqual(occupied(state, big + 1, big + 2), ((big + 1, big + 2),))
        self.assertEqual(peak(state), 1)
        many = build([(str(i), -big, big) for i in range(300)])
        self.assertEqual(len(bookings(many)), 300)
        self.assertEqual(peak(many), 300)
        self.assertEqual(bookings(state), (('neg', -big, -big + 2), ('pos', big, big + 3)))

    def test_exhaustive_small_calendars_and_windows(self):  # O1–O6
        intervals = list(itertools.combinations(range(-2, 3), 2))
        # All ordered 0-, 1-, 2- and 3-ID assignments, including equal intervals.
        for size in range(4):
            for assignment in itertools.product(intervals, repeat=size):
                model = dict(zip(('a', 'b', 'c'), assignment))
                with self.subTest(model=model):
                    state = build([(key, *pair) for key, pair in model.items()])
                    self.assertEqual(observe(state), model_observation(model))
                    for lo, hi in itertools.combinations_with_replacement(range(-3, 4), 2):
                        self.assertEqual(occupied(state, lo, hi), model_observation(model, lo, hi)[1])

    def test_seeded_persistent_branching_histories(self):  # O1–O8
        rng = random.Random(20261118)
        versions = [(empty(), {})]
        for step in range(250):
            state, model = rng.choice(versions)
            before = observe(state)
            if rng.randrange(2):
                key = rng.choice(['a', 'b', 'c', 'd', 'e', 'f'])
                a, b = rng.randint(-5, 5), rng.randint(-5, 5)
                conflict = a >= b or (key in model and model[key] != (a, b))
                if conflict:
                    with self.assertRaises(ValueError, msg=f'seed step {step}'):
                        reserve(state, key, a, b)
                else:
                    new_model = dict(model)
                    new_model[key] = (a, b)
                    versions.append((reserve(state, key, a, b), new_model))
            else:
                other, other_model = rng.choice(versions)
                conflict = any(key in model and model[key] != value
                               for key, value in other_model.items())
                if conflict:
                    with self.assertRaises(ValueError, msg=f'seed step {step}'):
                        merge(state, other)
                else:
                    versions.append((merge(state, other), dict(model, **other_model)))
            self.assertEqual(observe(state), before)
            # Recheck every old version, including occupancy and peak, after errors too.
            for old, expected in versions:
                self.assertEqual(observe(old), model_observation(expected), f'seed step {step}')


if __name__ == '__main__':
    unittest.main()
