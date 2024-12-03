"""The solutions for day 2."""

from typing import Tuple

def is_safe(row):
    inc = [row[i + 1] - row[i] for i in range(len(row) - 1)]
    if set(inc) <= {1, 2, 3} or set(inc) <= {-1, -2, -3}:
        return True
    return False


def safe_reports(input_text: str, dampener: bool=False) -> int:
    """Returns the number of 'reports' that are safe.

    Input provided contains 'reports',
    each 5 integers long
    and separated by a new line.
    Each integer in the string is separated by a space.

    Reports are safe when all 'levels' (integers)
    are either all increasing or all decreasing.
    Any two adjacent levels differ by at least one and at most three.

    Returns the number of safe reports.
    """

    data = [[int(y) for y in x.split(' ')] for x in input_text.rstrip().split('\n')]

    if dampener:
        return sum([any([is_safe(row[:i] + row[i + 1:]) for i in range(len(row))]) for row in data])
    return sum([is_safe(row) for row in data])
