"""Integer volume and area checks for the fictional event."""
from fractions import Fraction as F


def check():
    requirement = 87 * 240 + 1000
    assert requirement == 21880
    assert 14 * 1500 < requirement <= 15 * 1500
    assert 15 * 1500 - 87 * 240 == 1620
    assert divmod(1620 - 1000, 240) == (2, 140)
    assert (15 * 1500 - 1000) // 250 == 86
    assert 15 * 1500 < 87 * 250 + 1000 <= 16 * 1500
    assert 14 * 1500 < 87 * 240 + 1200 <= 15 * 1500
    assert divmod(1620 - 1200, 240) == (1, 180)
    assert F(14, 10) * 1000 < 6 * 240
    usable = 6 * 4 - 6 * F(3, 2)
    assert usable == 15
    assert usable // 3 == 5
    print("11 explicit serving and layout checks passed.")


if __name__ == "__main__":
    check()
