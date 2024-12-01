"""Test the Missing Stars Solution."""

import pytest

from advent_of_code.twenty_four.missing_stars import missing_stars_solution


def test_when_solution_formatted_string_then_pass() -> None:
    """R-BICEP: Right."""
    input_text = """3   4
4   3
2   5
1   3
3   9
3   3
"""
    result = missing_stars_solution(input_text)
    assert result == 11
    assert 0
