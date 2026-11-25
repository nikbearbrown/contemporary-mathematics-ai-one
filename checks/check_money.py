"""Exact checks for the fictional event decision and budgeting examples."""
from fractions import Fraction as F


def net_outdoor(dry, credit=0):
    return dry * (360 - 240) + (1 - dry) * (70 - 240 + credit)


def check():
    assert 360 - 240 == 120 and 70 - 240 == -170
    assert 200 - 175 == 25
    assert net_outdoor(F(3, 4)) == F(95, 2)
    assert net_outdoor(F(39, 58)) == 25
    assert net_outdoor(F(1, 2)) == -25
    assert net_outdoor(F(2, 3)) == F(70, 3)
    assert 70 - 240 + 80 == -90
    assert net_outdoor(F(3, 4), credit=80) == F(135, 2)
    assert [240 + n * 24 for n in range(4)] == [240, 264, 288, 312]
    values = [240 * F(11, 10) ** n for n in range(4)]
    assert values == [240, 264, F(1452, 5), F(7986, 25)]
    assert (values[2] - 240) / 240 == F(21, 100)
    assert (values[3] - 240) / 240 == F(331, 1000)
    print("12 explicit probability and budgeting checks passed.")


if __name__ == "__main__":
    check()
