"""Test methods in common."""

import pytest

from advent_of_code.common import random_with_N_digits


@pytest.mark.parametrize(
    "test_input,more_than,less_than",
    [
        (5, 100000, 9999),
        (2, 100, 9),
        (10, 10000000000, 999999999),
        (-1, 0, 0),
    ]
)
def test_random_with_N_return_int(test_input, more_than, less_than) -> None:
    """R-BICEP: Right."""
    result = random_with_N_digits(test_input)
    assert result <= more_than
    assert result >= less_than
