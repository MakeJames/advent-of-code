"""The solutions for day 2."""


def safe_reports(input_text: str) -> int:
    """Returns the number of 'reports' that are safe.

    Input provided contains 'reports',
    each 5 integers long
    and separated by a new line.
    Each integer in the string is separated by a space.

    Reports are safe when all 'levels' (integers)
    are either all increasing or all decreasing.
    Any two adjacent levels differ by at least one and at most three.

    Returns the number of safe reports
    """
    answer = 0

    reports = input_text.split("\n")

    for report in reports:

        if report == "":
            continue

        levels = [int(val) for val in report.split(" ")]
        safe = True

        direction = ""

        for level, next_level in zip(levels, levels[1:]):

            if level >= next_level:
                if direction == "ascending":
                    safe = False
                    break
                direction = "descending"

            if level <= next_level:
                if direction == "descending":
                    safe = False
                    break
                direction = "ascending"

            if max((level - next_level), (next_level - level)) > 3:
                safe = False
                break

        if safe is True:
            answer += 1

    return answer

    return 0
