import pytest

from validate import valid, valid1 

def test_valid():
    assert valid("1234") ==  True
    assert valid("45135") == False
    assert valid("89abc1") == False
    assert valid(900876) == True
    assert valid(" 4983") == False

def test_valid1():
    assert valid1("1234") ==  True
    assert valid1("45135") == False
    assert valid1("89abc1") == False
    assert valid1(900876) == True
    assert valid1(" 4983") == False