"""Return count number of prime numbers, starting at 2.

For example::

    >>> primes(0)
    []

    >>> primes(1)
    [2]

    >>> primes(5)
    [2, 3, 5, 7, 11]

"""


def primes(count):
    """Return count number of prime numbers, starting at 2."""
    prime_lst = []
    candidate = 2
    while count != 0:
        if is_prime(candidate):
            prime_lst.append(candidate)
            count -= 1
        candidate += 1
    return prime_lst

def is_prime(num):
    if num == 2:
        return True
    elif num < 2:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    return True

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT WORK!\n"
