#Write a function parse_int(value) that tries to convert a string to an integer and handles ValueError if the conversion fails.

def parse_int(value):
    try:
        return int(value)
    except ValueError:
        print("Value is not an integer")
        return None
