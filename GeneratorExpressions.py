#Use a generator expression to create an iterator that yields uppercase versions of words in a list. Iterate over it using a for loop.

listOfWords = ["hi", "hi i i", "hello ", "bye"]


ListToUpper = (Word.upper() for Word in listOfWords)

# Iterate over the generator using a for loop
for word in ListToUpper:
    print(word)
