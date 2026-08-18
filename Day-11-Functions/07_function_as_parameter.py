# Day 11 - Functions as Parameters

def square_number(n):
    return n ** 2

def cube_number(n):
    return n ** 3

def do_something(function, value):
    return function(value)

print("Square:", do_something(square_number, 3))
print("Cube:", do_something(cube_number, 3))

def apply_operation(function, a, b):
    return function(a, b)

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

print("Addition:", apply_operation(add, 5, 4))
print("Multiplication:", apply_operation(multiply, 5, 4))
