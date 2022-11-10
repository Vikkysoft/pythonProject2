import challenge_5
import unittest


def test_is_palindrome():
    assert challenge_5.is_palindrome("radar") == print("The string is palindrome")
    assert challenge_5.is_palindrome("dad") == print("The string is palindrome")
    assert challenge_5.is_palindrome("testify") == print("The string is not palindrome")
