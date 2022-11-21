import challenge_10
import unittest


def test_convert_string_to_sentence():
    assert challenge_10.convert_string_to_sentence("this is a python course for beginners.") == "This Is A Python Course For Beginners."
    assert challenge_10.convert_string_to_sentence("test automation training in testify school") == "Test Automation Training In Testify School"