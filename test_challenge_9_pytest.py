import challenge_9
import unittest


def test_convert_to_upper_case():
    assert challenge_9.convert_to_upper_case("testify automation school") == None
    assert challenge_9.convert_to_upper_case("i have a dog") == print("I HAVE A DOG")
    assert challenge_9.convert_to_upper_case("i serve a living god") == print("I SERVE A LIVING GOD")
