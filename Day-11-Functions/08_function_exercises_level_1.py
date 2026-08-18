# Day 11 - Exercises: Level 1

import math

def add_two_numbers(a, b):
    return a + b

def area_of_circle(radius):
    return math.pi * radius * radius

def add_all_nums(*numbers):
    total = 0
    for number in numbers:
        if not isinstance(number, (int, float)):
            raise TypeError("All arguments must be numbers.")
        total += number
    return total

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def check_season(month):
    month = month.strip().lower()
    seasons = {
        "Autumn": {"september", "october", "november"},
        "Winter": {"december", "january", "february"},
        "Spring": {"march", "april", "may"},
        "Summer": {"june", "july", "august"},
    }
    for season, months in seasons.items():
        if month in months:
            return season
    return "Invalid month"

def calculate_slope(x1, y1, x2, y2):
    if x2 == x1:
        raise ValueError("Slope is undefined for a vertical line.")
    return (y2 - y1) / (x2 - x1)

def solve_quadratic_eqn(a, b, c):
    if a == 0:
        raise ValueError("a must not be zero.")
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        return ((-b + math.sqrt(discriminant)) / (2 * a),
                (-b - math.sqrt(discriminant)) / (2 * a))
    if discriminant == 0:
        return (-b / (2 * a),)
    real = -b / (2 * a)
    imaginary = math.sqrt(-discriminant) / (2 * a)
    return (complex(real, imaginary), complex(real, -imaginary))

def print_list(items):
    for item in items:
        print(item)

def reverse_list(items):
    result = []
    for index in range(len(items) - 1, -1, -1):
        result.append(items[index])
    return result

def capitalize_list_items(items):
    return [str(item).capitalize() for item in items]

def add_item(items, item):
    result = items.copy()
    result.append(item)
    return result

def remove_item(items, item):
    result = items.copy()
    if item in result:
        result.remove(item)
    return result

def sum_of_numbers(n):
    total = 0
    for number in range(n + 1):
        total += number
    return total

def sum_of_odds(n):
    return sum(number for number in range(n + 1) if number % 2 != 0)

def sum_of_even(n):
    return sum(number for number in range(n + 1) if number % 2 == 0)

print("Add:", add_two_numbers(5, 7))
print("Circle area:", area_of_circle(5))
print("Sum all:", add_all_nums(1, 2, 3, 4))
print("100 C in F:", convert_celsius_to_fahrenheit(100))
print("Season:", check_season("January"))
print("Slope:", calculate_slope(1, 2, 3, 6))
print("Quadratic roots:", solve_quadratic_eqn(1, -3, 2))
print("Reverse:", reverse_list([1, 2, 3, 4, 5]))
print("Capitalized:", capitalize_list_items(["python", "django", "flask"]))
print("Added:", add_item(["Potato", "Tomato"], "Mango"))
print("Removed:", remove_item(["Potato", "Tomato", "Mango"], "Tomato"))
print("Sum 5:", sum_of_numbers(5))
print("Sum odds 10:", sum_of_odds(10))
print("Sum evens 10:", sum_of_even(10))
