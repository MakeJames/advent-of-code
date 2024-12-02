"""Test the methods of the Nuclear Fusion plant, day 2."""

import pytest

from pathlib import Path

from advent_of_code.twenty_four.nuclear_fusion_plant import safe_reports


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            "7 6 4 2 1\n1 2 7 8 9\n9 7 6 2 1\n1 3 2 4 5\n8 6 4 4 1\n1 3 6 7 9\n",
            2,
        ),
        (
            "9 5 6 3 6\n4 5 7 8 10\n9 7 6 5 4\n4 4 4 4 4\n-1 -2 -3 -4 -6\n1 5 6 7 4\n",
            3,
        ),
        (
            "9 5 6 3 6\n4 5 7 8 10\n9 7 6 5 4\n4 4 4 4 4\n-1 -2 -3 -4 -6\n1 5 6 7 4\n",
            3,
        ),
    ],
)
def test_when_valid_input_return_correct(test_input, expected) -> None:
    """R-BICEP: Right."""
    result = safe_reports(test_input)
    assert result == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("nuclear_reports_1000_56.txt", 56),
        ("nuclear_reports_2000000_104626.txt", 104626),
        ("nuclear_reports_20000_1049.txt", 1049),
    ]
)
def test_nuclear_large_files_and_numbers(test_input: str, expected: int, benchmark) -> None:
    """R-BICEP: Performance."""
    test_file = Path(__file__).parent.joinpath("test_data", test_input)
    result = benchmark(safe_reports, test_file.read_text())

    assert result == expected
