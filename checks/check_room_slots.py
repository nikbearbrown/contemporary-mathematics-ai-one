"""Exact checks for the fictional room-booking cases; Python 3 standard library."""
from fractions import Fraction
from math import ceil, floor


def allocate(weights, slots):
    assert weights and all(w >= 0 for w in weights) and sum(weights) > 0
    assert 0 <= slots <= sum(weights)
    quotas = [Fraction(w * slots, sum(weights)) for w in weights]
    whole = list(map(floor, quotas))
    order = sorted(range(len(weights)), key=lambda i: (-(quotas[i] - whole[i]), i))
    result = whole.copy()
    for i in order[:slots - sum(whole)]:
        result[i] += 1
    assert sum(result) == slots
    assert all(floor(q) <= n <= ceil(q) for q, n in zip(quotas, result))
    assert all(n <= w for w, n in zip(weights, result))
    return result, [q - floor(q) for q in quotas]


def check():
    for slots, expected, residual, promised in [
        (4, [2, 1, 1], [2, 3, 4], [2, 1, 1]),
        (5, [3, 2, 0], [7, 6, 5], [2, 2, 1]),
    ]:
        observed, parts = allocate([5, 3, 1], slots)
        assert observed == expected
        assert parts == [Fraction(x, 9) for x in residual] and len(set(parts)) == 3
        assert [1 + v for v in allocate([4, 2, 0], slots - 3)[0]] == promised
    assert allocate([4, 3, 2], 6)[0] == [3, 2, 1]
    assert allocate([1, 1], 1)[1] == [Fraction(1, 2)] * 2
    print("8 explicit room-allocation checks passed; exact arithmetic and allocation invariants verified.")


if __name__ == "__main__":
    check()
