import pytest
from String import convert


def test_string():
    assert convert('A') == 'A'
    assert convert('Hallo') == 'HALLO'
    assert convert(12) == '12'
    assert convert('1234') == '1234'
    assert convert(True) == 'TRUE'
    assert convert(False) == 'FALSE'
