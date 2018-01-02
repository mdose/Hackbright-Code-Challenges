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
    Create list based on the num of holes; so range(0, num_holes)
    Assign list to a variable "holes"
    Create varialble "result" set to 0
    For each hole in holes,
        if it's a cafe, skip it
        else, count the num of steps it takes to get to a cafe, both left and right
            take the bigger of the two nums, compare that num to result
                if bigger than result, resassign result
    Return result
    """

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; GREAT JOB!\n"
