"""
30 Days of Python - Day 15: Python Error Types
Complete practice file based on the accompanying README.

This file demonstrates:
- SyntaxError (shown as a comment because invalid syntax stops execution)
- NameError
- IndexError
- ModuleNotFoundError (shown as a comment)
- AttributeError
- KeyError
- TypeError
- ImportError (shown as a comment)
- ValueError
- ZeroDivisionError

Run:
    python day_15_python_error_types.py
"""


def demonstrate_name_error():
    print("\n--- NameError ---")
    try:
        print(age)
    except NameError as error:
        print(f"Caught NameError: {error}")

    age = 25
    print(f"After defining age: {age}")


def demonstrate_index_error():
    print("\n--- IndexError ---")
    numbers = [1, 2, 3, 4, 5]
    try:
        print(numbers[5])
    except IndexError as error:
        print(f"Caught IndexError: {error}")

    print(f"Valid last index: {numbers[4]}")


def demonstrate_module_not_found_error():
    print("\n--- ModuleNotFoundError ---")
    # The README demonstrates: import maths
    # That intentionally fails because the module name is misspelled.
    try:
        __import__("maths")
    except ModuleNotFoundError as error:
        print(f"Caught ModuleNotFoundError: {error}")

    import math
    print(f"Correct import works: math.pi = {math.pi}")


def demonstrate_attribute_error():
    print("\n--- AttributeError ---")
    import math

    try:
        print(math.PI)
    except AttributeError as error:
        print(f"Caught AttributeError: {error}")

    print(f"Correct attribute: math.pi = {math.pi}")


def demonstrate_key_error():
    print("\n--- KeyError ---")
    user = {"name": "Asab", "age": 250, "country": "Finland"}

    try:
        print(user["county"])
    except KeyError as error:
        print(f"Caught KeyError: {error}")

    print(f"Correct key: {user['country']}")


def demonstrate_type_error():
    print("\n--- TypeError ---")
    try:
        print(4 + "3")
    except TypeError as error:
        print(f"Caught TypeError: {error}")

    print(f"4 + int('3') = {4 + int('3')}")
    print(f"4 + float('3') = {4 + float('3')}")


def demonstrate_import_error():
    print("\n--- ImportError ---")
    # The README demonstrates:
    # from math import power
    # The correct function name is pow.
    try:
        from math import power
    except ImportError as error:
        print(f"Caught ImportError: {error}")

    from math import pow
    print(f"Correct import: pow(2, 3) = {pow(2, 3)}")


def demonstrate_value_error():
    print("\n--- ValueError ---")
    try:
        int("12a")
    except ValueError as error:
        print(f"Caught ValueError: {error}")


def demonstrate_zero_division_error():
    print("\n--- ZeroDivisionError ---")
    try:
        print(1 / 0)
    except ZeroDivisionError as error:
        print(f"Caught ZeroDivisionError: {error}")


def syntax_error_examples():
    print("\n--- SyntaxError ---")
    print("SyntaxError is a parsing error and cannot be caught by a normal")
    print("try/except around the invalid statement itself.")
    print("README example of invalid syntax: print 'hello world'")
    print("Correct Python 3 syntax: print('hello world')")


def main():
    print("=" * 60)
    print("30 DAYS OF PYTHON - DAY 15: PYTHON ERROR TYPES")
    print("=" * 60)

    syntax_error_examples()
    demonstrate_name_error()
    demonstrate_index_error()
    demonstrate_module_not_found_error()
    demonstrate_attribute_error()
    demonstrate_key_error()
    demonstrate_type_error()
    demonstrate_import_error()
    demonstrate_value_error()
    demonstrate_zero_division_error()

    print("\n" + "=" * 60)
    print("All Day 15 demonstrations completed.")
    print("=" * 60)


if __name__ == "__main__":
    main()
