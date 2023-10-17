import pytest
from MyCalc import MyCalc

@pytest.fixture
def my_calc():
    return MyCalc()

# Test cases for number addition
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-3, 1, -2),
    (0, 0, 0),
    (100, -50, 50)
])
def test_number_add_number(my_calc, a, b, expected):
    #rv437 and 10/16/23 num_add_num test case
    result = my_calc.add(a, b)
    assert result == expected

# Test cases for addition using 'ans'
@pytest.mark.parametrize("b, expected", [
    (3, 6),
    (-2, 1),
    (0, 3),
    (10, 13)
])
def test_ans_add_number(my_calc, b, expected):
     #rv437 and 10/16/23 ans_add_num test case
    my_calc.ans = 3
    result = my_calc.add("ans", b)
    assert result == expected

# Test cases for number subtraction
@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (1, -3, 4),
    (0, 0, 0),
    (-100, -50, -50)
])
def test_number_sub_number(my_calc, a, b, expected):
     #rv437 and 10/16/23 num_sub_num test case
    result = my_calc.subtract(a, b)
    assert result == expected

# Test cases for subtraction using 'ans'
@pytest.mark.parametrize("b, expected", [
    (2, 1),
    (-1, 4),
    (0, 3),
    (-5, 8)
])
def test_ans_sub_number(my_calc, b, expected):
    #rv437 and 10/16/23 ans_sub_num test case
    my_calc.ans = 3
    result = my_calc.subtract("ans", b)
    assert result == expected

# Test cases for number multiplication
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (-3, 1, -3),
    (0, 10, 0),
    (5, 0, 0)
])
def test_number_mult_number(my_calc, a, b, expected):
     #rv437 and 10/16/23 num_mult_num test case
    result = my_calc.multiply(a, b)
    assert result == expected

# Test cases for multiplication using 'ans'
@pytest.mark.parametrize("b, expected", [
    (3, 9),
    (-2, -6),
    (0, 0),
    (5, 15)
])
def test_ans_mult_number(my_calc, b, expected):
    #rv437 and 10/16/23 ans_mult_num test case
    my_calc.ans = 3
    result = my_calc.multiply("ans", b)
    assert result == expected

# Test cases for number division
@pytest.mark.parametrize("a, b, expected", [
    (6, 3, 2),
    (-9, 3, -3),
    (0, 10, 0),
    (100, 5, 20)
])
def test_number_div_number(my_calc, a, b, expected):
     #rv437 and 10/16/23 num_div_num test case
    result = my_calc.divide(a, b)
    assert result == expected

# Test cases for division using 'ans'
@pytest.mark.parametrize("b, expected", [
    (2, 1.5),
    (-2, -1.5),
    (5, 0.6),
    (0, "Cannot divide by zero.")
])
def test_ans_div_number(my_calc, b, expected):
    #rv437 and 10/16/23 ans_div_num test case
    my_calc.ans = 3
    result = my_calc.divide("ans", b)
    assert result == expected

if __name__ == '__main__':
    pytest.main()
