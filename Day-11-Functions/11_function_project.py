# Day 11 - Mini Function Project: Calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def calculator():
    operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

    print("Simple Function-Based Calculator")
    print("Operations: +  -  *  /")

    first = float(input("Enter first number: "))
    operator = input("Enter operator: ")
    second = float(input("Enter second number: "))

    if operator not in operations:
        print("Invalid operator.")
        return

    try:
        print("Result:", operations[operator](first, second))
    except ZeroDivisionError as error:
        print(error)

if __name__ == "__main__":
    calculator()
