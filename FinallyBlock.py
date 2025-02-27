#Modify safe_divide to include a finally block that prints "Division attempted".
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as err:
        print("Error class is:", type(err))
    finally:
        print("Division attempted")


safe_divide(2, 0)
safe_divide(2, 2)
