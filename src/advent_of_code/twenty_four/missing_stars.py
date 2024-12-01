"""Missing Stars Solution."""


def extract_lists(input_text: str):
    """Extract the two lists of numbers from the input text.

    The string must be split,
    converted to integers,
    each pair of numbers assigned to list A or B,
    sorted.

    Returns a pair of lists.
    """

    lines = input_text.split("\n")
    A = []
    B = []

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

    return A, B


def missing_stars_solution(input_text: str) -> int:
    """Missing Stars.

    Function takes a string of space and new line separated numbers.
    The string contains two lists of numbers.
    Each line of the list contains items belonging to each list.

    Returns the difference between the two lists
    """

    answer = 0

    A, B = extract_lists(input_text)

    for a, b in zip(A, B):
        answer += max(a - b, b -a)

    return answer


def similarity_score(input_text: str) -> int:
    """Missing Stars: part 2.

    Calculate the number of times an integer appears in a second list.
    Multiply it by the number of occurrences.

    Return the sum of the first list.
    """
    return 0
