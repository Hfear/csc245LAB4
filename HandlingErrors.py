#Write a function safe_divide(a, b) that divides a by b, but catches the ZeroDivisionError
# and prints an error message instead of crashing.

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as err:
        print("Error class is:  ", type(err))
    finally:
        return

safe_divide(2,0)

safe_divide(2,2)