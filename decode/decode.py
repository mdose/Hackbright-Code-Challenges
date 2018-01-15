"""Decode a string.

A valid code is a sequence of numbers and letter, always starting with a number
and ending with letter(s).

Each number tells you how many characters to skip before finding a good letter.
After each good letter should come the next next number.

For example, the string "hey" could be encoded by "0h1ae2bcy". This means
"skip 0, find the 'h', skip 1, find the 'e', skip 2, find the 'y'".

A single letter should work::

    >>> decode("0h")
    'h'

    >>> decode("2abh")
    'h'

Longer patterns should work::

    >>> decode("0h1ae2bcy")
    'hey'
"""


def decode(s):
    """Decode a string."""

    word = ""

    for i, char in enumerate(s):
        if char.isdigit():
            word = word + s[i + int(char) + 1]

        else:
            pass

    return word


# """ Alernate aolution to Decrypt string:

# Here's a simple strategy to encode a message: before each character of the message,
# add a digit and series of other characters. The digit should correspond to the
# number of characters that will precede the message's actual, meaningful character.
#
# For example, the word "hey" could be coded with "0h2abe1zy". To read the message, you would:
#
# skip 0, find the 'h'
# skip 2 ('a' and 'b'), find 'e'
# skip 1 ('z'), find 'y'
# Other examples:
#
# '2xyz' would be decoded as just 'z'
# '0h2zyi2467' would be decoded as 'hi7'
#
# Write a function named "decode", which takes a single parameter of a string encoded
# in this format. It should return the decoded word in string form. Demonstrate good
# coding practices (clear variable names, comments, etc). You may assume that coded
# strings are always legally encoded with this system. You may also assume that the
# digit for the number of characters to skip will just be a single digit, not a
# multi-digit number (that is, you'll never need to skip more than 9 characters)
# we welcome solutions that can handle multi-digit characters to skip.
# """

# def decode(encoded_msg):
#     decoded_msg = ""
#     index = 0
#     found_digit_last_time = False
#
#     while index < len(encoded_msg):
#         character = encoded_msg[index]
#         if character.isdigit() and not found_digit_last_time:
#             index += int(character)
#             found_digit_last_time = True
#         else:
#             decoded_msg += character
#             found_digit_last_time = False
#
#         index += 1
#
#     return decoded_msg
#
# # tests for diffent cases
# assert decode("0h1ji") == "hi"
# assert decode("0h1ae2vcl3chel2sho0 0w1yo1br3woil7sjiwiogd") == "hello world"
# assert decode("0h2abe1zy") == "hey"
# assert decode("2xyz") == "z"
# assert decode("0h2zyi2467") == "hi7"
# assert decode("1qh4cdfge267yo1w!") == "heyo!"
# assert decode("") == ""
# assert decode("hello") == "hello"
# assert decode("1234") == "3"
# assert decode("9") == ""


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; 0G1ar0e1ba0t2ab! ***\n"
