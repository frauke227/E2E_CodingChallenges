import pytest
from challenge2 import tip_calculator3


# def test_tip():
#assert tip_calculator(10, 80, 2) == 4.0
#assert tip_calculator(10, 40, 4) == 1.0
#assert tip_calculator(10, 50, 3) == 1.67


# def test_bill():
#assert bill_amount(10, 40, 4) == 11.0
#assert bill_amount(10, 80, 2) == 44.0


def test_tip_calculator():
    assert tip_calculator3(
        10, 80, 2) == 'Everyone needs to pay 44.0 Euro. This includes 4.0 Euro tip per person.'
    assert tip_calculator3(
        10, 10, 1) == 'Everyone needs to pay 11.0 Euro. This includes 1.0 Euro tip per person.'
