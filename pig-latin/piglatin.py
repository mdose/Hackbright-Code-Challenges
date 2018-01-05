"""Turn a phrase into Pig Latin.

This takes a space-separated phrase and returns it in Pig Latin.

Rules:

1. If the word begins with a consonant (not a, e, i, o, u),
   move the first letter to the end and add 'ay'

2. If the word begins with a vowel, add 'yay' to the end

For example:

    >>> pig_latin('hello awesome programmer')
    'ellohay awesomeyay rogrammerpay'

"""

def pig_latin(phrase):
    """Turn a phrase into pig latin.

    There will be no uppercase letters or punctuation in the phrase.

        >>> pig_latin('hello awesome programmer')
        'ellohay awesomeyay rogrammerpay'
    """
    vowels = set(["a","e","i","o","u"])
    words = phrase.split(" ")
    pig_phrase = ""
    for word in words:
        if word[0] in vowels:
            pig_phrase = pig_phrase + word + "yay "
        else:
            first_ltr = word[0]
            pig_phrase = pig_phrase + word[1:len(word)] + first_ltr + "ay "
    return pig_phrase[0:-1]


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. REATGAY OBJAY!\n"
