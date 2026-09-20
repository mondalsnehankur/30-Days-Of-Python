"""Practical combinations of the Day 17 concepts."""

from src.exception_handling import generic_handling
from src.packing import sum_all
from src.iteration_tools import zip_example


def safe_calculator(a, b, operation):
    try:
        if operation == "+":
            return a + b
        if operation == "-":
            return a - b
        if operation == "*":
            return a * b
        if operation == "/":
            return a / b
        raise ValueError("Unsupported operation")
    except (TypeError, ValueError, ZeroDivisionError) as error:
        return f"Calculation error: {error}"


def flexible_total(*values):
    return sum_all(*values)


def paired_inventory():
    return zip_example()


if __name__ == "__main__":
    print(safe_calculator(10, 2, "/"))
    print(safe_calculator(10, 0, "/"))
    print(safe_calculator(10, 2, "^"))
    print("Flexible total:", flexible_total(10, 20, 30, 40))
    print("Paired inventory:", paired_inventory())
    print("Generic exception example:", generic_handling(0))
