import challenge_2
import unittest


def test_power():
    assert challenge_2.power(7, 2) == 49
    assert challenge_2.power(2, 5) == 32
    assert challenge_2.power(3, 3) == 27