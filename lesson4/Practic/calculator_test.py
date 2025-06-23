import pytest
from calculator import Calculator

calculator = Calculator()

def test_sum_positiv_nums():
    calculator = Calculator()
    res = calculator.sum(4,5)
    assert res == 9

def test_sum_negativ_nums():
    calculator = Calculator()
    res = calculator.sum(4,-5)
    assert res == -1

def test_div_zero_nums():
    calculator = Calculator()
    with pytest.raises(ArithmeticError):
         calculator.div(10,0)


def test_sum_negative_nums():
    calculator = Calculator()
    res = calculator.sum(-4,-5)
    assert res == -9

def test_sum_positive_nums():
    calculator = Calculator()
    res = calculator.sum(4,0)
    assert res == 4

def test_sum_null_nums():
    calculator = Calculator()
    res=calculator.sum(5,0)
    assert res == 5

def test_sum_float_nums():
    calculator = Calculator()
    res=calculator.sum(4.5,4.5)
    assert  res == 9

def test_div_nums():
    calculator = Calculator()
    res=calculator.div(10,2)
    assert  res == 5

def test_avg_nums():
    calculator = Calculator()
    nums=[1,2,3,4,5,6,7,8,9,5]
    res=calculator.avg(nums)
    assert res == 5
