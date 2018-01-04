"""Given a list of numbers 1...max_num, find which one is missing in a list."""


def missing_number(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list

    >>> missing_number([7, 3, 2, 4, 5, 6, 1, 9, 10], 10)
    8

    >>> missing_number([2, 1, 4, 5], 5)
    3

    """
    complete_nums = set(range(1, max_num + 1))

    for num in sorted(nums):
        if num in complete_nums:
            complete_nums.remove(num)
    return int(complete_nums.pop())


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASS. NICELY DONE!\n"
