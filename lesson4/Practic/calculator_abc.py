import pytest
from calculator import Calculator

calculator = Calculator()

@pytest.mark.parametrize("num1, num2, result", [
    (4,5,9),
    (4,-5,-1),
    (10,0,10),
    (-4,-5,-9),
    (4.5,4.5,9)
    ])
def test_sum_positiv_nums(num1, num2, result):
    calc = Calculator()
    res = calc.sum(num1,num2)
    assert res == result
@pytest.mark.parametrize('num1,num2,result',[
    (10,2,5),
    (20,5,4),
    (269.28,22.44,12.0)
])
def test_div_nums(num1,num2,result):
    calculator = Calculator()
    res=calculator.div(num1,num2)
    assert round(res,2) == result
@ pytest.mark.parametrize('nums, result', [ ( [1,2,3,4,5,6,7,8,9,5],5) ] )
def test_avg_nums(nums,result):
    calculator = Calculator()
    res=calculator.avg(nums)
    assert res == result
