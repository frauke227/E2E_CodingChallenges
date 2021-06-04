import pytest
from challenge1 import multiples_sum


def test_multiples():
    assert multiples_sum(1, 10) == 23
    assert multiples_sum(1, 100) == 2318
    assert multiples_sum(1, 1000) == 233168
