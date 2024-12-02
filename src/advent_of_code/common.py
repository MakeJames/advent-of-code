"""Helper functions for generating test data."""


from pathlib import Path
from random import randint

from advent_of_code.twenty_four.missing_stars import missing_stars_solution


def random_with_N_digits(n: int) -> int:
    if n < 0:
        return 0

    start = 10**(n-1)
    end = (10**n)-1
    return randint(start, end)


def create_missing_stars_test_data(lines: int=25, digits: int=4) -> None:
    data = []
    print(f"Creating test data. Lines: {lines}, Digits: {digits}")
    if lines <= 0:
        raise ValueError("Number of lines must be a positive integer")
    if digits <= 0:
        raise ValueError("Number of digits must be a positive integer")
    for i in range(lines):
        first_int = random_with_N_digits(digits)
        second_int = random_with_N_digits(digits)
        data.append(f"{first_int}   {second_int}")

    test_string = "\n".join(data)
    result = missing_stars_solution(test_string)
    file_name = f"missing_stars_{lines}_{digits}_{result}.txt"

    file = Path(__file__).parent.parent.parent.joinpath("tests", "twenty_four",
                                                        "test_data", file_name)
    file.write_text(test_string)
    print(f"New test data written to '{file}'")
