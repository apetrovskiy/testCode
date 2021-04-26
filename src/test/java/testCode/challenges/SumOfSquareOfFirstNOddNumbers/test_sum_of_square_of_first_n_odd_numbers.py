import pytest
from typing import List
from src.main.java.testCode.challenges.SumOfSquareOfFirstNOddNumbers. \
    sum_of_square_of_first_n_odd_numbers \
    import sum_of_square_of_first_n_odd_numbers


test_data = [
    (3,35)
]


@pytest.mark.parametrize("input_number,expected_result", test_data)
def test_sum_of_square_of_first_n_odd_numbers(
        input_number:int, expected_result: int):
    assert expected_result == sum_of_square_of_first_n_odd_numbers(input_number)
