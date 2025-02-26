#Write a function apply_function that takes a function
# and a value as arguments and applies the function to the value.
#Test it with apply_function(lambda x: x.upper(), "hello").

def apply_function(funct, value):
    return print(funct(value))

apply_function(lambda x: x.upper(), "hello")