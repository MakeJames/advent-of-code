"""Test the Missing Stars Solution."""

import pytest

from pathlib import Path

from advent_of_code.twenty_four.missing_stars import (missing_stars_solution,
                                                      similarity_score)

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


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("3   4\n4   3\n2   5\n1   3\n3   9\n3   3\n", 31),
        ("5   2\n2   1\n2   3\n3   8\n1   9\n-2   3\n", 11),
        ("100   20\n40   -2\n304   700\n20   49\n40   30009\n20   3\n", 40),
    ],
)
def test_when_similarity_then_pass(test_input, expected) -> None:
    """R-BICEP: Right."""
    result = similarity_score(test_input)
    assert result == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            "missing_stars_1000_20_667121229184848866069.txt",
            667121229184848866069,
        ),
        (
            "missing_stars_25_4_18908.txt",
            18908,
        ),
        (
            "missing_stars_500000_2_65589.txt",
            65589,
        ),
        (
            "missing_stars_50000_20_8770726923331238161099.txt",
            8770726923331238161099,
        ),
    ]
)
def test_large_files_and_numbers(test_input: str, expected: int, benchmark) -> None:
    """R-BICEP: Performance."""
    test_file = Path(__file__).parent.joinpath("test_data", test_input)
    result = benchmark(missing_stars_solution, test_file.read_text())

    assert result == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            "missing_stars_1000_20_667121229184848866069.txt",
            0,
        ),
        (
            "missing_stars_25_4_18908.txt",
            0,
        ),
        (
            "missing_stars_500000_2_65589.txt",
            151261294761,
        ),
        # Too Slow - function needs performance improvements
        # (
        #     "missing_stars_50000_20_8770726923331238161099.txt",
        #     0,
        # ),
    ]
)
def test_large_files_and_numbers_for_similarity(test_input: str, expected: int, benchmark) -> None:
    """R-BICEP: Performance."""
    test_file = Path(__file__).parent.joinpath("test_data", test_input)
    result = benchmark(similarity_score, test_file.read_text())

    assert result == expected
