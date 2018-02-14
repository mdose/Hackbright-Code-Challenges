# Given a string, return True if sting is a palindrome
# Determine if string is the same backwards vs forwards
# Easiest way to do this without built-ins is via list slicing



def is_palindrome(word):
    """
    >>> is_palindrome('racecar')
    True

    >>> is_palindrome('rarecar')
    False
    """

    if word == word[::-1]:
        return True
    return False


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED!\n"
