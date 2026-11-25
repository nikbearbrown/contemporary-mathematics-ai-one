"""Independent tallies for small fictional vote profiles."""
from collections import Counter
from fractions import Fraction


def count(ballots, active):
    tally = Counter({candidate: 0 for candidate in active})
    for ranking in ballots:
        tally[next((candidate for candidate in ranking if candidate in active), None)] += 1
    assert sum(tally.values()) == len(ballots)
    return tally


def expand(*args):
    return [ranking for copies, ranking in args for _ in range(copies)]


def winner(tally):
    high = max(tally.values())
    return {item for item, votes in tally.items() if votes == high}


def check():
    original = expand((5, "ABC"), (4, "CBA"), (3, "BCA"))
    first = count(original, "ABC")
    assert winner(first) == {"A"} and first == {"A": 5, "B": 3, "C": 4}
    assert min(first, key=first.__getitem__) == "B"
    assert count(original, "AC") == {"A": 5, "C": 7}
    assert count(original, "AB") == {"A": 5, "B": 7}
    assert count(original, "BC") == {"B": 8, "C": 4}
    cyclic = expand((1, "ABC"), (1, "BCA"), (1, "CAB"))
    assert [winner(count(cyclic, pair)) for pair in ("AB", "BC", "AC")] == [{"A"}, {"B"}, {"C"}]
    incomplete = original[:-1] + ["B"]
    assert count(incomplete, "ABC") == first
    final = count(incomplete, "AC")
    assert final == {"A": 5, "C": 6, None: 1}
    assert Fraction(final["C"], len(incomplete) - final[None]) > Fraction(1, 2)
    assert Fraction(final["C"], len(incomplete)) == Fraction(1, 2)
    assert count(original[:-1] + ["BAC"], "AC") == {"A": 6, "C": 6}
    library = expand((6, "RTS"), (5, "STR"), (4, "TRS"))
    assert min(count(library, "RST"), key=count(library, "RST").__getitem__) == "T"
    assert count(library, "RS") == {"R": 10, "S": 5}
    assert count(library, "RT") == {"R": 6, "T": 9}
    assert count(library, "ST") == {"S": 5, "T": 10}
    print("15 explicit ballot checks passed, plus ballot-count conservation in each tally.")


if __name__ == "__main__":
    check()
