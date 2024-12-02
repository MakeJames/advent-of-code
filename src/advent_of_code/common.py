"""Helper functions for generating test data."""


from pathlib import Path
from random import randint, random

from advent_of_code.twenty_four.missing_stars import missing_stars_solution
from advent_of_code.twenty_four.nuclear_fusion_plant import safe_reports


def random_int(start: int, stop: int) -> int:
    return randint(start, stop)

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


def create_nuclear_reports_test_data(reports: int) -> None:
    test_reports = []

    for i in range(reports):
        report = []
        val = random_int(-100000, 200000)

        for i in range(5):
            report.append(f"{val}")
            new_vals = [val, (val + random_int(0, 7))]
            if random() == 1:
                new_vals = [val, (val - random_int(0, 7))]
            if random() == 1:
                new_vals = [val, (val * random_int(1, 3))]
            if random() == 1:
                new_vals = [val, int(val / random_int(1, 3))]
            val = random_int(min(new_vals), max(new_vals))

        print(report)
        test_reports.append(" ".join(report))

    test_string = "\n".join(test_reports)
    result = safe_reports(test_string)
    file_name = f"nuclear_reports_{reports}_{result}.txt"

    file = Path(__file__).parent.parent.parent.joinpath("tests", "twenty_four",
                                                        "test_data", file_name)
    file.write_text(test_string)
    print(f"New test data written to '{file}'")
