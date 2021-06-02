# Test Palindromechecker

import pytest
from challenge3 import isPalindrome


def test_palindrome():
    assert isPalindrome("LOL") == True
    assert isPalindrome(121) == True
    assert isPalindrome("Frauke") == False
    assert isPalindrome(12345) == False
    assert isPalindrome("Anna") == True
    assert isPalindrome("Ann a") == True
