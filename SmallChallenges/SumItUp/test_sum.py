import pytest
from sum import sum_it_up


def test_sum():
    assert sum_it_up(1, 1) == 2.0
    assert sum_it_up(2, 2.5) == 4.5
    assert sum_it_up(0.3, 0.1) == 0.4
    assert sum_it_up(3) == 3.0
    assert sum_it_up() == 0.0
    assert sum_it_up(4.77766786) == 4.77766786
