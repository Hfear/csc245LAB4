#Write a function repeat_phrase that repeats a phrase a given number of times, with a default of 2.

def repeat_phrase(phrase, times):
    if times == None:
        times = 2
    for _ in range(times):
        print(phrase)

repeat_phrase(phrase=input("Enter the phrase: "), times=2 )