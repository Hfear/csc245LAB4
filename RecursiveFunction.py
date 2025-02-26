#Write a recursive function countdown(n) that prints numbers from n to 0. Test it with countdown(5).

def countdown(n):
    if n > 0:
        print(n)
        countdown(n-1)


    return


countdown(5)
