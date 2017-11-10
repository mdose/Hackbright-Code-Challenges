"""Given a string, return True if it is a pangram, False otherwise.

For example::

    >>> is_pangram("The quick brown fox jumps over the lazy dog!")
    True

    >>> is_pangram("I love cats, but not mice")
    False
"""


def is_pangram(sentence):
    """Given a string, return True if it is a pangram, False otherwise."""
    # Final answer (most effectient using set comprehension):
    used = {char for char in sentence.lower() if char.isalpha()}
    return len(used) == 26

    # # Second try (more effectient):
    # alpha = set()
    # for char in sentence.lower():
    #     if char.isalpha():
    #         alpha.add(char)
    # return len(alpha) == 26

    # # First try:
    # alpha = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i' , 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
    # lower = sentence.lower()
    # for char in lower:
    #     if char in alpha:
    #         alpha.remove(char)
    # return not alpha

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YAY!\n"
