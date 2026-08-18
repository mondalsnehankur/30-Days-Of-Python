# Day 11 - Exercises: Level 2

import statistics

def evens_and_odds(number):
    if not isinstance(number, int) or number < 0:
        raise ValueError("Provide a non-negative integer.")
    evens = 0
    odds = 0
    for value in range(number + 1):
        if value % 2 == 0:
            evens += 1
        else:
            odds += 1
    return odds, evens

def factorial(number):
    if not isinstance(number, int) or number < 0:
        raise ValueError("Factorial requires a non-negative integer.")
    result = 1
    for value in range(1, number + 1):
        result *= value
    return result

def is_empty(value):
    return len(value) == 0

def calculate_mean(numbers):
    return statistics.mean(numbers)

def calculate_median(numbers):
    return statistics.median(numbers)

def calculate_mode(numbers):
    return statistics.mode(numbers)

def calculate_range(numbers):
    return max(numbers) - min(numbers)

def calculate_variance(numbers):
    return statistics.variance(numbers)

def calculate_std(numbers):
    return statistics.stdev(numbers)

def greet(name="Guest"):
    return "Hello, Guest!" if name == "Guest" else f"Hello, {name}!"

def show_args(**kwargs):
    parts = []
    for key, value in kwargs.items():
        parts.append(f"{key}: {value}")
    print("Received:", ", ".join(parts))

print("Odds and evens for 100:", evens_and_odds(100))
print("5! =", factorial(5))
print("Empty list:", is_empty([]))

data = [1, 2, 2, 3, 4]
print("Mean:", calculate_mean(data))
print("Median:", calculate_median(data))
print("Mode:", calculate_mode(data))
print("Range:", calculate_range(data))
print("Variance:", calculate_variance(data))
print("Standard deviation:", calculate_std(data))
print(greet())
print(greet("Alice"))
show_args(name="Alice", age=30, city="New York")
show_args(name="Bob", pet="Fluffy, the bunny")
