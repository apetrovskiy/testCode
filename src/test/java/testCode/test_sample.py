import pytest

test_data = [
    (1, 1)
]


@pytest.mark.parametrize("input,expected_result", test_data)
def test_sample(input: int, expected_result: int):
    assert expected_result == input
