"""Does a string have balanced parentheses?

For example::

   >>> has_balanced_parens("()")
   True

   >>> has_balanced_parens("(Oh Noes!)(")
   False

   >>> has_balanced_parens("((There's a bonus open paren here.)")
   False

   >>> has_balanced_parens(")")
   False

   >>> has_balanced_parens("(")
   False

   >>> has_balanced_parens("(This has (too many closes.) ) )")
   False

If you receive a string with no parentheses, consider it balanced::

   >>> has_balanced_parens("Hey...there are no parens here!")
   True
"""


def has_balanced_parens(phrase):
    """Does a string have balanced parentheses?"""
    counter = 0
    for char in phrase:
        if char == "(":
            counter += 1
        elif char == ")":
            counter -= 1
        if counter == -1:
            return False
    return (counter == 0)

# Alternate solution to the problem from a coding interview:

# def is_balanced(sequence):
    # if sequence == "":
    #     raise Exception("Error")
    # open_paran = 0
    # closed_paran = 0
    # for char in sequence:
    #     if char == "(":
    #         open_paran += 1
    #     if char ==")":
    #         closed_paran += 1
    #             if closed_paran > open_paran:
    #                 return False
    # if open_paran == closed_paran:
    #     return True
    # else:
    #     return False
    #
    # s = ""
    # try:
    #     if is_balanced(s):
    #         print "balanced"
    #     else:
    #         print "not balanced"
    # except Exception:
    #     print "Invalid input"



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU CAUGHT ALL THE STRAY PARENS!\n"
