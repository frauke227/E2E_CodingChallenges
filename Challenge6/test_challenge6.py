import pytest

from challenge6 import neutralise

def test_neutralise():
    assert neutralise("--++--", "++--++") == "000000"
    assert neutralise("-+-+-+", "-+-+-+") == "-+-+-+"
    assert neutralise("-++-", "-+-+") == "-+00"