# Day 11 - Returning Different Data Types

def return_string(first_name):
    return first_name

def return_number(num_one, num_two):
    return num_one + num_two

def calculate_age(current_year, birth_year):
    return current_year - birth_year

def is_even(number):
    return number % 2 == 0

def find_even_numbers(n):
    evens = []
    for number in range(n + 1):
        if number % 2 == 0:
            evens.append(number)
    return evens

print("String:", return_string("Python"))
print("Number:", return_number(2, 3))
print("Age:", calculate_age(2026, 2002))
print("10 is even:", is_even(10))
print("7 is even:", is_even(7))
print("Even numbers:", find_even_numbers(10))
