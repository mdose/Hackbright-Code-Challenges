"""Count items in a list recursively.

For example:

        >>> count_recursively([])
        0

        >>> count_recursively([1, 2, 3])
        3

"""


def count_recursively(lst):
    """Return number of items in a list, using recursion."""

    if not lst:
        return 0

    return 1 + count_recursively(lst[1:])

    # NOTE: tail call optimized tricks the compiler under the hood to "cheat"
    # and make a while loop; keeps track of the returns before doing the recursive
    # call. Also lst slice at the begining is most effectient (accounting for linked
    # lists and not mutating the lst given)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GO YOU!\n"
