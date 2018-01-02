"""Lazy lemmings.

Find the farthest any single lemming needs to travel for food.

    >>> furthest(3, [0, 1, 2])
    0

    >>> furthest(3, [2])
    2

    >>> furthest(3, [0])
    2

    >>> furthest(6, [2, 4])
    2

    >>> furthest(7, [0, 6])
    3
"""


def furthest(num_holes, cafes):
    """Find longest distance between a hole and a cafe."""

    """Pseudocode:
    Create list based on the num of holes; range(num_holes)
    Assign list to a variable "holes"
    Create varialble "result" set to 0
    For each hole in holes,
        if it's a cafe, skip it
        else, count the num of steps it takes to get to a cafe, both left and right
            take the smaller of the two nums, compare that num to result
                if bigger than result, resassign result
    Return result
    """

    holes = range(num_holes)
    result = 0

    for hole in holes:
        if hole in cafes:
            continue

        left = count_steps_left(hole, cafes)
        right = count_steps_right(hole, cafes)
        counter = min([x for x in [left, right] if x is not None])

        if counter > result:
            result = counter

    return result

def count_steps_left(hole, cafes):
    """Count the steps left to nearest cafe; Return None if no cafe to the left"""

    counter = None
    for cafe in cafes:
        if cafe < hole:
            counter = hole - cafe
    return counter

def count_steps_right(hole, cafes):
    """Count the steps right to nearest cafe; Return None if no cafe to the right"""

    for cafe in cafes:
        if cafe > hole:
            return cafe - hole

    return None

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; GREAT JOB!\n"
