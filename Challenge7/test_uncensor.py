import pytest

from uncensor import uncensor

def test_uncensor():
    assert uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo") == "Where did my vowels go?"
    assert uncensor("abcd", "") == "abcd"
    assert uncensor("*PP*RC*S*", "UEAE") == "UPPERCASE"