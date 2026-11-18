"""Public-API tests; the small-domain oracle enumerates unit cells."""
import itertools
import unittest

from calendar_api import empty, reserve, merge, bookings, occupied, peak


def build(rows):
    state = empty()
    for key, a, b in rows:
        state = reserve(state, key, a, b)
    return state


def observe(state):
    return (bookings(state), peak(state),
            tuple(occupied(state, lo, hi)
                  for lo in range(-3, 5) for hi in range(lo, 5)))


def cell_oracle(rows, lo, hi):
    """For integer endpoints, each unit cell has a constant coverage count."""
    cells = [x for x in range(lo, hi)
             if any(a <= x < b for _, a, b in rows)]
    spans = []
    for x in cells:
        if spans and spans[-1][1] == x:
            spans[-1] = (spans[-1][0], x + 1)
        else:
            spans.append((x, x + 1))
    return tuple(spans)


class CalendarTests(unittest.TestCase):
    def test_empty_and_query_ordering(self):
        state = empty()
        self.assertEqual(bookings(state), ())
        self.assertEqual(peak(state), 0)
        self.assertEqual(occupied(state, -10, 10), ())
        self.assertEqual(occupied(state, 2, 2), ())
        before = observe(state)
        with self.assertRaisesRegex(ValueError, 'lo'):
            occupied(state, 3, -1)
        self.assertEqual(observe(state), before)

    def test_reserve_sort_replay_and_errors(self):
        state = build([('z', 1, 5), ('A', -2, 3), ('a', 1, 5)])
        self.assertEqual(bookings(state), (('A', -2, 3), ('a', 1, 5), ('z', 1, 5)))
        self.assertEqual(peak(state), 3)
        before = observe(state)
        self.assertEqual(observe(reserve(state, 'z', 1, 5)), before)
        for key, a, b in [('z', 1, 6), ('z', 0, 5),
                          ('new', 3, 3), ('new', 4, -4), ('z', 5, 1)]:
            with self.subTest(key=key, a=a, b=b):
                with self.assertRaises(ValueError):
                    reserve(state, key, a, b)
                self.assertEqual(observe(state), before)

    def test_clipping_adjacency_containment_and_gaps(self):
        state = build([('a', -10, -5), ('b', -5, 0), ('c', -8, -6),
                       ('d', 2, 6), ('e', 4, 9), ('f', 12, 13)])
        for lo, hi, expected in [
            (-20, 20, ((-10, 0), (2, 9), (12, 13))),
            (-7, 5, ((-7, 0), (2, 5))),
            (0, 2, ()), (-5, 0, ((-5, 0),)),
            (9, 12, ()), (3, 4, ((3, 4),)), (4, 4, ())]:
            with self.subTest(lo=lo, hi=hi):
                self.assertEqual(occupied(state, lo, hi), expected)

    def test_peak_half_open_ties_and_distinct_ids(self):
        state = build([('a', -5, 0), ('b', -5, 0),
                       ('c', 0, 5), ('d', 0, 5)])
        self.assertEqual(peak(state), 2)
        self.assertEqual(occupied(state, -6, 6), ((-5, 5),))
        state = reserve(state, 'bridge', -1, 1)
        self.assertEqual(peak(state), 3)
        self.assertEqual(peak(merge(state, state)), 3)
        self.assertEqual(peak(build([('outer', 0, 10), ('inner', 2, 8),
                                     ('deep', 3, 4)])), 3)

    def test_persistent_branches_and_retained_outputs(self):
        base = build([('base', -1, 2)])
        saved = observe(base)
        rows = bookings(base)
        spans = occupied(base, -3, 4)
        left = reserve(base, 'left', -2, 0)
        right = reserve(base, 'right', 1, 3)
        left_before, right_before = observe(left), observe(right)
        joined = merge(left, right)
        self.assertEqual(bookings(joined),
                         (('base', -1, 2), ('left', -2, 0), ('right', 1, 3)))
        self.assertEqual(observe(base), saved)
        self.assertEqual(observe(left), left_before)
        self.assertEqual(observe(right), right_before)
        self.assertEqual(rows, (('base', -1, 2),))
        self.assertEqual(spans, ((-1, 2),))
        self.assertIsInstance(rows, tuple)
        self.assertTrue(all(isinstance(row, tuple) for row in rows))
        self.assertIsInstance(spans, tuple)
        self.assertTrue(all(isinstance(span, tuple) for span in spans))

    def test_merge_laws(self):
        a = build([('x', 0, 3), ('a', -2, 1)])
        b = build([('x', 0, 3), ('b', 2, 4)])
        c = build([('c', 0, 3)])
        self.assertEqual(observe(merge(a, b)), observe(merge(b, a)))
        self.assertEqual(observe(merge(merge(a, b), c)),
                         observe(merge(a, merge(b, c))))
        self.assertEqual(observe(merge(a, a)), observe(a))
        self.assertEqual(observe(merge(a, empty())), observe(a))
        self.assertEqual(observe(merge(empty(), a)), observe(a))
        joined = merge(a, b)
        self.assertEqual(observe(merge(joined, b)), observe(joined))

    def test_merge_conflict_after_compatible_rows_preserves_both(self):
        left = build([('shared', 0, 2), ('z-conflict', 2, 4)])
        right = build([('a-new', -3, 0), ('shared', 0, 2),
                       ('z-conflict', 2, 5)])
        before = (observe(left), observe(right))
        for x, y in [(left, right), (right, left)]:
            with self.assertRaisesRegex(ValueError, 'z-conflict'):
                merge(x, y)
            self.assertEqual((observe(left), observe(right)), before)

    def test_exhaustive_small_observer_oracle(self):
        intervals = list(itertools.combinations(range(-2, 3), 2))
        # Every ordered pair, including identical intervals under distinct IDs.
        for first, second in itertools.product(intervals, repeat=2):
            rows = [('z', *first), ('a', *second)]
            state = build(rows)
            with self.subTest(first=first, second=second):
                self.assertEqual(bookings(state), tuple(sorted(rows)))
                expected_peak = max(sum(a <= x < b for _, a, b in rows)
                                    for x in range(-2, 3))
                self.assertEqual(peak(state), expected_peak)
                for lo in range(-3, 4):
                    for hi in range(lo, 4):
                        self.assertEqual(occupied(state, lo, hi),
                                         cell_oracle(rows, lo, hi))

    def test_exhaustive_small_merge_oracle(self):
        # Each ID is absent or assigned one of three intervals on each side.
        choices = [None, (-2, 0), (0, 2), (-1, 2)]
        maps = [dict((key, value) for key, value in zip(('a', 'b'), values)
                     if value is not None)
                for values in itertools.product(choices, repeat=2)]
        for left_map, right_map in itertools.product(maps, repeat=2):
            left = build([(k, *v) for k, v in left_map.items()])
            right = build([(k, *v) for k, v in right_map.items()])
            before = observe(left), observe(right)
            conflict = any(left_map[k] != right_map[k]
                           for k in left_map.keys() & right_map.keys())
            with self.subTest(left=left_map, right=right_map):
                if conflict:
                    with self.assertRaises(ValueError):
                        merge(left, right)
                else:
                    expected = left_map | right_map
                    result = merge(left, right)
                    self.assertEqual(bookings(result),
                                     tuple((k, *expected[k]) for k in sorted(expected)))
                    self.assertEqual(observe(result), observe(merge(right, left)))
                self.assertEqual((observe(left), observe(right)), before)

    def test_huge_signed_endpoints_and_larger_collection(self):
        huge = 10 ** 200
        state = build([('negative', -huge, -huge + 3),
                       ('positive', huge, huge + 7),
                       ('adjacent', huge + 7, huge + 9)])
        self.assertEqual(occupied(state, -huge - 1, huge + 10),
                         ((-huge, -huge + 3), (huge, huge + 9)))
        self.assertEqual(occupied(state, huge + 1, huge + 8),
                         ((huge + 1, huge + 8),))
        self.assertEqual(peak(state), 1)
        dense = build([(f'id-{i:04}', -huge, huge) for i in range(300)])
        self.assertEqual(len(bookings(dense)), 300)
        self.assertEqual(peak(dense), 300)
        self.assertEqual(occupied(dense, -1, 1), ((-1, 1),))
        self.assertEqual(bookings(merge(dense, dense)), bookings(dense))


if __name__ == '__main__':
    unittest.main()
