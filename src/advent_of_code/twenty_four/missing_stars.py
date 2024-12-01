"""Missing Stars Solution."""


def missing_stars_solution(input_text: str) -> int:
    """Missing Stars.

    Function takes a string of space and new line separated numbers.
    The string contains two lists of numbers.
    Each line of the list contains items belonging to each list.

    The string must be split,
    converted to integers,
    each pair of numbers assigned to list A or B,
    sorted.

    Returns the difference between the two lists
    """
    lines = input_text.split("\n")
    A = []
    B = []
    answer = 0

    for line in lines:
        values = line.split("   ")
        if values[0] == "":
            continue
        if values[1] == "":
            continue

        A.append(int(values[0]))
        B.append(int(values[1]))

    assert len(A) == len(B)

    A.sort()
    B.sort()

    for a, b in zip(A, B):
        answer += max(a - b, b -a)

    return answer
