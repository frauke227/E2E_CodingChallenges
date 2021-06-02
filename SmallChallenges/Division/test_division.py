import pytest
from division import division


def test_division():
    assert division(1, 1) == 1.0
    assert division(25, 5) == 5.0
    assert division(456, 896) == 0.51
    assert division(1, 0) == 'This is not possible'
    assert division(4) == 'This is not possible'
