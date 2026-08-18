# 30 Days of Python — Day 11: Functions

This repository contains my practice and exercise solutions for **Day 11: Functions** from the 30 Days of Python learning material.

## Topics Covered

- Defining and calling functions
- Functions without parameters
- Parameters and arguments
- Multiple parameters
- Keyword arguments
- `return`
- Returning strings, numbers, booleans and lists
- Default parameters
- Arbitrary positional arguments: `*args`
- Arbitrary keyword arguments: `**kwargs`
- Dictionary unpacking with `**`
- Passing functions as parameters
- Mathematical functions
- List-processing functions
- Statistical functions
- Prime-number checking
- Python variable-name validation
- Function-based problem solving
- A small function-based calculator

## Repository Structure

```text
Day_11_Functions/
├── 01_function_basics.py
├── 02_parameters_and_arguments.py
├── 03_return_values.py
├── 04_default_parameters.py
├── 05_arbitrary_arguments.py
├── 06_kwargs_and_dictionary_unpacking.py
├── 07_function_as_parameter.py
├── 08_function_exercises_level_1.py
├── 09_function_exercises_level_2.py
├── 10_function_exercises_level_3.py
├── 11_function_project.py
└── README.md
```

## 1. Defining a Function

A function is a reusable block of code designed to perform a particular task.

Python uses the `def` keyword:

```python
def function_name():
    # code
    pass
```

The function body executes when the function is called.

```python
def greet():
    print("Hello!")

greet()
```

## 2. Functions Without Parameters

```python
def add_two_numbers():
    return 2 + 3

print(add_two_numbers())
```

## 3. Parameters and Arguments

Parameters are variables in the function definition. Arguments are the actual values passed during the call.

```python
def add_two_numbers(num_one, num_two):
    return num_one + num_two

print(add_two_numbers(2, 3))
```

## 4. Keyword Arguments

```python
def generate_full_name(first_name, last_name):
    return first_name + " " + last_name

print(generate_full_name(
    last_name="Learner",
    first_name="Python"
))
```

## 5. Return Values

A function returns a value with `return`.

```python
def square_number(number):
    return number * number

result = square_number(5)
print(result)
```

If a function has no explicit `return`, Python returns `None`.

## 6. Returning Different Data Types

Functions can return strings, numbers, booleans, lists, and other Python objects.

```python
def is_even(number):
    return number % 2 == 0
```

```python
def find_even_numbers(n):
    evens = []

    for number in range(n + 1):
        if number % 2 == 0:
            evens.append(number)

    return evens
```

## 7. Default Parameters

```python
def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet())
print(greet("Alice"))
```

The default value is used when the caller does not provide that argument.

## 8. Arbitrary Positional Arguments — `*args`

`*args` collects an arbitrary number of positional arguments.

```python
def sum_all_nums(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total

print(sum_all_nums(1, 2, 3))
print(sum_all_nums(1, 2, 3, 4, 5))
```

Inside the function, `numbers` is a tuple.

## 9. Arbitrary Keyword Arguments — `**kwargs`

`**kwargs` collects arbitrary keyword arguments into a dictionary.

```python
def show_args(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

show_args(name="Alice", age=30, city="New York")
```

## 10. Dictionary Unpacking

A dictionary can be unpacked into keyword arguments with `**`.

```python
def greet(name, location):
    return f"Hello {name} from {location}"

data = {
    "name": "Alice",
    "location": "New York"
}

print(greet(**data))
```

The dictionary keys must match the function parameter names.

## 11. Passing a Function as a Parameter

Functions can be passed to other functions.

```python
def square(number):
    return number ** 2

def apply_function(function, value):
    return function(value)

print(apply_function(square, 5))
```

This is used in the repository to demonstrate higher-order function behavior.

## 12. Mathematical Functions

The Level 1 exercises include:

- Area of a circle
- Celsius to Fahrenheit conversion
- Linear-equation slope
- Quadratic-equation solutions
- Sum of numbers
- Sum of even numbers
- Sum of odd numbers

Example:

```python
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32
```

## 13. List-Processing Functions

```python
def reverse_list(items):
    result = []

    for index in range(len(items) - 1, -1, -1):
        result.append(items[index])

    return result
```

Other examples included are functions for printing, capitalizing, adding and removing list items.

## 14. Statistical Functions

The Level 2 exercises include:

- Mean
- Median
- Mode
- Range
- Variance
- Standard deviation

The repository uses Python's standard-library `statistics` module.

```python
import statistics

def calculate_mean(numbers):
    return statistics.mean(numbers)
```

## 15. Factorial

A factorial can be calculated using a loop inside a function.

```python
def factorial(number):
    result = 1

    for value in range(1, number + 1):
        result *= value

    return result
```

## 16. Even and Odd Counting

```python
def evens_and_odds(number):
    evens = 0
    odds = 0

    for value in range(number + 1):
        if value % 2 == 0:
            evens += 1
        else:
            odds += 1

    return odds, evens
```

For `100`, the result is:

```text
Number of odds = 50
Number of evens = 51
```

## 17. Level 3 Functions

The Level 3 exercise file includes functions for:

- Checking whether a number is prime
- Checking whether list items are unique
- Checking whether all list items have the same data type
- Checking whether a string is a valid Python variable name

Example:

```python
def is_prime(number):
    if number < 2:
        return False

    divisor = 2

    while divisor * divisor <= number:
        if number % divisor == 0:
            return False

        divisor += 1

    return True
```

## 18. Mini Function Project

`11_function_project.py` contains a small calculator.

It demonstrates how functions can be stored in a dictionary:

```python
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
```

The selected function is then called according to the operator.

This combines:

- Functions
- Parameters
- Return values
- Dictionaries
- Functions as objects
- Exception handling
- `if __name__ == "__main__"`

## How to Run

Open a terminal inside the repository directory.

Run an individual file:

```bash
python 01_function_basics.py
```

Run the exercises:

```bash
python 08_function_exercises_level_1.py
python 09_function_exercises_level_2.py
python 10_function_exercises_level_3.py
```

Run the calculator:

```bash
python 11_function_project.py
```

## Learning Progress

- [x] Defining functions
- [x] Calling functions
- [x] Parameters
- [x] Arguments
- [x] Multiple parameters
- [x] Keyword arguments
- [x] Return values
- [x] Default parameters
- [x] `*args`
- [x] `**kwargs`
- [x] Dictionary unpacking
- [x] Functions as parameters
- [x] Mathematical functions
- [x] List-processing functions
- [x] Statistical functions
- [x] Level 1 exercises
- [x] Level 2 exercises
- [x] Level 3 exercises
- [x] Mini function project

---

**Part of my Python learning journey — 30 Days of Python.**
