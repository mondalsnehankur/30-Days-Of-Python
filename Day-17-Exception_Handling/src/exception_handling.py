"""Examples of Python exception handling."""


def basic_handling():
    try:
        print(10 + "5")
    except TypeError:
        print("Type error occurred")


def specific_handling(year_born):
    try:
        age = 2026 - int(year_born)
        print(f"Calculated age: {age}")
    except TypeError:
        print("Type error occurred")
    except ValueError:
        print("Value error occurred")
    except ZeroDivisionError:
        print("Zero division error occurred")


def try_except_else_finally(value):
    try:
        result = 100 / value
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else:
        print("Result:", result)
    finally:
        print("Finally block executed")


def generic_handling(value):
    try:
        return 100 / value
    except Exception as error:
        return f"Error: {error}"


if __name__ == "__main__":
    basic_handling()
    specific_handling("2000")
    specific_handling("not-a-year")
    try_except_else_finally(5)
    try_except_else_finally(0)
    print(generic_handling(0))
