"""Test the methods of the Nuclear Fusion plant, day 2."""

import pytest

from advent_of_code.twenty_four.nuclear_fusion_plant import safe_reports


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            "7 6 4 2 1\n1 2 7 8 9\n9 7 6 2 1\n1 3 2 4 5\n8 6 4 4 1\n1 3 6 7 9\n",
            2,
        ),
    ],
)
def test_when_valid_input_return_correct(test_input, expected) -> None:
    """R-BICEP: Right."""
    result = safe_reports(test_input)
    assert result == expected
