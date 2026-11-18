from dataclasses import dataclass
from fractions import Fraction
from functools import reduce


# Supplied implementation, reproduced verbatim.
@dataclass(frozen=True)
class Report:
    count: int
    mean: Fraction
    diagnostics: tuple[str, ...]

def merge(a: Report, b: Report) -> Report:
    return Report(a.count + b.count, (a.mean + b.mean) / 2,
                  a.diagnostics + b.diagnostics)


@dataclass(frozen=True)
class Summary:
    count: int
    total: int
    diagnostics: tuple[str, ...]

    @property
    def mean(self) -> Fraction | None:
        return Fraction(self.total, self.count) if self.count else None


EMPTY = Summary(0, 0, ())


def summarize(values: tuple[int, ...], diagnostics: tuple[str, ...]) -> Summary:
    return Summary(len(values), sum(values), diagnostics)


def combine(a: Summary, b: Summary) -> Summary:
    return Summary(a.count + b.count, a.total + b.total,
                   a.diagnostics + b.diagnostics)


def main() -> None:
    # Unequal-size batches (0,) and (3, 3).
    a = Report(1, Fraction(0), ("a",))
    b = Report(2, Fraction(3), ("b",))
    assert merge(a, b) == Report(3, Fraction(3, 2), ("a", "b"))
    assert merge(a, b).mean != Fraction(sum((0, 3, 3)), 3)

    # Three singleton batches expose regrouping independently of batch size.
    b = Report(1, Fraction(0), ("b",))
    c = Report(1, Fraction(4), ("c",))
    assert merge(merge(a, b), c) == Report(3, Fraction(2), ("a", "b", "c"))
    assert merge(a, merge(b, c)) == Report(3, Fraction(1), ("a", "b", "c"))

    assert merge(a, b) == Report(2, Fraction(0), ("a", "b"))
    assert merge(b, a) == Report(2, Fraction(0), ("b", "a"))
    assert merge(a, b) != merge(b, a)

    # Signed, unequal-size batches with a repeated diagnostic.
    values_a, values_b, values_c = (-2,), (3, 3), (1, 2)
    x = summarize(values_a, ("retry", "a"))
    y = summarize(values_b, ("retry",))
    z = summarize(values_c, ("c",))
    expected = summarize(values_a + values_b + values_c,
                         ("retry", "a", "retry", "c"))
    assert combine(combine(x, y), z) == expected
    assert combine(x, combine(y, z)) == expected
    assert reduce(combine, (x, y, z), EMPTY) == expected
    assert (expected.count, expected.mean) == (5, Fraction(7, 5))

    swapped = combine(y, x)
    original = combine(x, y)
    assert (swapped.count, swapped.mean) == (original.count, original.mean)
    assert swapped.diagnostics == ("retry", "retry", "a")
    assert swapped != original

    for summary in (EMPTY, x, y, z, expected):
        assert combine(EMPTY, summary) == summary == combine(summary, EMPTY)
    assert reduce(combine, (), EMPTY) == EMPTY
    assert EMPTY.mean is None
    print("All reducer checks passed.")


if __name__ == "__main__":
    main()
