import challenge_9
import unittest


def test_convert_to_upper_case():
    assert challenge_9.convert_to_upper_case("testify") == "TESTIFY"
    assert challenge_9.convert_to_upper_case("i have a dog") == "I HAVE A DOG"
    assert challenge_9.convert_to_upper_case("i serve a living god") == "I SERVE A LIVING GOD"
