#Modify join_words to accept an arbitrary number of words and return them concatenated
# into a single string with spaces. Implement this using both a regular function and a
# lambda function.

def join_words(words):
    return ' '.join(words)

joinedWords = lambda words: ' '.join(words)