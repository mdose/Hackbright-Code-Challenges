# Implement a function that accepts two arguments: a message string, and a list/array of "bad words".
#
# The function should return true if the message string contains any item from the bad word list,
# otherwise it returns false.

def bad_word_filter(message, bad_words):
    """Implement me"""

# split the sting " "
# loop over each word
# check if word in bad words --> false
    words = message.split(" ")
    bad_words_set = set(bad_words)
    for word in words:
        if word in bad_words_set:
            return True
    return False

bad_words = ['jerk', 'butt', 'wuss', 'sucks']

print bad_word_filter('The bass jumped over the lazy fox.', bad_words) # false (contains no bad words)
print bad_word_filter('The bass is a lazy butt jerk', bad_words) # true
print bad_word_filter('The bass totally sucks!', bad_words) #true
