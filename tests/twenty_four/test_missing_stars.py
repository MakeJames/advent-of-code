"""Test the Missing Stars Solution."""

import pytest

from advent_of_code.twenty_four.missing_stars import missing_stars_solution

@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("3   4\n4   3\n2   5\n1   3\n3   9\n3   3\n", 11),
        ("5   2\n2   1\n2   3\n3   8\n1   9\n-2   3\n", 15),
        ("100   20\n40   -2\n304   700\n20   49\n40   30009\n20   3\n", 30373),
    ],
)
def test_when_solution_formatted_string_then_pass(test_input, expected) -> None:
    """R-BICEP: Right."""
    result = missing_stars_solution(test_input)
    assert result == expected
