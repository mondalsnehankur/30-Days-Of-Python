"""
30 Days of Python - Day 13: List Comprehension
Author: Snehankur Mondal
Topic: List Comprehension and Lambda Functions

This file contains:
1. List comprehension examples
2. Lambda function examples
3. Day 13 exercises with solutions
"""

# ============================================================
# LIST COMPREHENSION
# ============================================================

print("=" * 60)
print("LIST COMPREHENSION")
print("=" * 60)

# Example 1: Convert a string to a list of characters
language = "Python"

lst = list(language)
print("\nExample 1 - Using list():")
print(type(lst))
print(lst)

lst = [i for i in language]
print("\nExample 1 - Using list comprehension:")
print(type(lst))
print(lst)


# Example 2: Generate numbers
numbers = [i for i in range(11)]
print("\nExample 2 - Numbers from 0 to 10:")
print(numbers)

# Mathematical operation during iteration
squares = [i * i for i in range(11)]
print("\nSquares:")
print(squares)

# Create a list of tuples
numbers = [(i, i * i) for i in range(11)]
print("\nNumber and square tuples:")
print(numbers)


# Example 3: List comprehension with conditions
even_numbers = [i for i in range(21) if i % 2 == 0]
print("\nEven numbers:")
print(even_numbers)

odd_numbers = [i for i in range(21) if i % 2 != 0]
print("\nOdd numbers:")
print(odd_numbers)

numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print("\nPositive even numbers:")
print(positive_even_numbers)


# Flatten a two-dimensional list
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]

print("\nFlattened list:")
print(flattened_list)


# ============================================================
# LAMBDA FUNCTIONS
# ============================================================

print("\n" + "=" * 60)
print("LAMBDA FUNCTIONS")
print("=" * 60)

# Named function
def add_two_nums(a, b):
    return a + b


print("\nNamed function:")
print(add_two_nums(2, 3))

# Equivalent lambda function
add_two_nums = lambda a, b: a + b

print("\nLambda function:")
print(add_two_nums(2, 3))


# Self-invoking lambda function
result = (lambda a, b: a + b)(2, 3)
print("\nSelf-invoking lambda:")
print(result)

# Square and cube
square = lambda x: x ** 2
print("\nSquare of 3:")
print(square(3))

cube = lambda x: x ** 3
print("\nCube of 3:")
print(cube(3))

# Multiple variables
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print("\nMultiple-variable lambda:")
print(multiple_variable(5, 5, 3))


# ============================================================
# LAMBDA FUNCTION INSIDE ANOTHER FUNCTION
# ============================================================

def power(x):
    return lambda n: x ** n


cube = power(2)(3)
print("\n2 raised to the power 3:")
print(cube)

two_power_of_five = power(2)(5)
print("\n2 raised to the power 5:")
print(two_power_of_five)


# ============================================================
# EXERCISES: DAY 13
# ============================================================

print("\n" + "=" * 60)
print("EXERCISES: DAY 13")
print("=" * 60)


# Exercise 1
# Filter only negative numbers and zero
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

negative_and_zero = [i for i in numbers if i <= 0]

print("\nExercise 1:")
print(negative_and_zero)


# Exercise 2
# Flatten a list of lists
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flattened_list = [number for row in list_of_lists for number in row]

print("\nExercise 2:")
print(flattened_list)


# Exercise 3
# Create tuples containing:
# (n, 1, n, n^2, n^3, n^4, n^5)
power_tuples = [
    (i, 1, i, i ** 2, i ** 3, i ** 4, i ** 5)
    for i in range(11)
]

print("\nExercise 3:")
for item in power_tuples:
    print(item)


# Exercise 4
# Convert countries and cities into:
# ['COUNTRY', 'COUN', 'CITY']
countries = [
    [("Finland", "Helsinki")],
    [("Sweden", "Stockholm")],
    [("Norway", "Oslo")]
]

country_city_list = [
    [country.upper(), country[:3].upper(), city.upper()]
    for country_group in countries
    for country, city in country_group
]

print("\nExercise 4:")
print(country_city_list)


# Exercise 5
# Convert countries into a list of dictionaries
country_dicts = [
    {"country": country.upper(), "city": city.upper()}
    for country_group in countries
    for country, city in country_group
]

print("\nExercise 5:")
print(country_dicts)


# Exercise 6
# Convert names into a list of concatenated strings
names = [
    [("Asabeneh", "Yetayeh")],
    [("David", "Smith")],
    [("Donald", "Trump")],
    [("Bill", "Gates")]
]

full_names = [
    f"{first_name} {last_name}"
    for name_group in names
    for first_name, last_name in name_group
]

print("\nExercise 6:")
print(full_names)


# Exercise 7
# Lambda functions for slope and y-intercept.
#
# For a line:
# y = mx + c
#
# Given two points (x1, y1) and (x2, y2):
#
# slope (m) = (y2 - y1) / (x2 - x1)
# y-intercept (c) = y1 - m*x1

slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)

y_intercept = lambda x1, y1, x2, y2: (
    y1 - slope(x1, y1, x2, y2) * x1
)

x1, y1 = 2, 3
x2, y2 = 6, 11

m = slope(x1, y1, x2, y2)
c = y_intercept(x1, y1, x2, y2)

print("\nExercise 7:")
print("Slope:", m)
print("Y-intercept:", c)
print(f"Equation: y = {m}x + {c}")


print("\n" + "=" * 60)
print("DAY 13 COMPLETED")
print("=" * 60)
