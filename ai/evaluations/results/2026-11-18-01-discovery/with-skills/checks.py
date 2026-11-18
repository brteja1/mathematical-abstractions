from dataclasses import dataclass
from fractions import Fraction
from itertools import product


# Original implementation from TASK.md.
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

    def merge(self, other: "Summary") -> "Summary":
        return Summary(
            self.count + other.count,
            self.total + other.total,
            self.diagnostics + other.diagnostics,
        )


EMPTY = Summary(0, 0, ())


def summarize(values: tuple[int, ...], diagnostics: tuple[str, ...]) -> Summary:
    return Summary(len(values), sum(values), diagnostics)


def check_original() -> None:
    a = Report(1, Fraction(0), ("a", "a"))
    b = Report(1, Fraction(0), ())
    c = Report(1, Fraction(6), ("b",))

    unequal = merge(Report(2, Fraction(0), ()), c)
    assert unequal.count == 3 and unequal.mean == 3
    assert Fraction(sum((0, 0, 6)), 3) == 2

    left = merge(merge(a, b), c)
    right = merge(a, merge(b, c))
    assert left == Report(3, Fraction(3), ("a", "a", "b"))
    assert right == Report(3, Fraction(3, 2), left.diagnostics)
    assert merge(merge(c, b), a).mean == Fraction(3, 2)

    assert merge(a, c) == Report(2, Fraction(3), ("a", "a", "b"))
    assert merge(c, a) == Report(2, Fraction(3), ("b", "a", "a"))

    for would_be_identity, witness in (
        (Report(0, Fraction(0), ()), c),
        (Report(0, Fraction(6), ()), a),
    ):
        assert merge(would_be_identity, witness) != witness
        assert merge(witness, would_be_identity) != witness


def check_replacement() -> None:
    batches = (
        ((), ()),
        ((0,), ("a", "a")),
        ((0, 0), ()),
        ((6,), ("b",)),
        ((-7, 2), ("a",)),
    )
    summaries = [summarize(*batch) for batch in batches]
    assert summaries[0] == EMPTY and EMPTY.mean is None
    assert summaries[1].mean == Fraction(0)

    for summary in summaries:
        assert EMPTY.merge(summary) == summary == summary.merge(EMPTY)

    for a, b, c in product(summaries, repeat=3):
        assert a.merge(b).merge(c) == a.merge(b.merge(c))

    for (xs, ds), (ys, es) in product(batches, repeat=2):
        merged = summarize(xs, ds).merge(summarize(ys, es))
        values = xs + ys
        assert merged == summarize(values, ds + es)
        assert merged.mean == (Fraction(sum(values), len(values)) if values else None)

    a, b, c = summaries[1], summaries[2], summaries[3]
    assert b.merge(c).mean == Fraction(2)
    forward, reverse = a.merge(c), c.merge(a)
    assert (forward.count, forward.total, forward.mean) == (
        reverse.count, reverse.total, reverse.mean
    )
    assert forward.diagnostics == ("a", "a", "b")
    assert reverse.diagnostics == ("b", "a", "a")


if __name__ == "__main__":
    check_original()
    check_replacement()
    print("Original counterexamples and replacement checks passed.")
