# Python Exception Handling, Packing, Unpacking & Iteration

A structured Python learning project based on the provided **30 Days of Python — Day 17: Exception Handling** material.

The reference covers exception handling with `try`, `except`, `else`, and `finally`, argument packing and unpacking with `*` and `**`, spreading, `enumerate()`, `zip()`, and a country-unpacking exercise.

## Concepts Covered

- Exception handling
- `try` and `except`
- Specific exception types
- `TypeError`
- `ValueError`
- `ZeroDivisionError`
- `else`
- `finally`
- `except Exception as e`
- List/tuple unpacking with `*`
- Dictionary unpacking with `**`
- Packing arbitrary positional arguments with `*args`
- Packing arbitrary keyword arguments with `**kwargs`
- Spreading lists with `*`
- `enumerate()`
- `zip()`

## Project Structure

```text
python_exception_handling_project/
│
├── README.md
│
├── src/
│   ├── exception_handling.py
│   ├── unpacking.py
│   ├── packing.py
│   └── iteration_tools.py
│
├── examples/
│   └── practical_examples.py
│
└── exercises/
    └── exercises.py
```

## Requirements

- Python 3.x
- No external packages are required.

Everything uses Python's standard library.

## How to Run

From the project directory:

```bash
python src/exception_handling.py
```

```bash
python src/unpacking.py
```

```bash
python src/packing.py
```

```bash
python src/iteration_tools.py
```

```bash
python examples/practical_examples.py
```

```bash
python exercises/exercises.py
```

## 1. Exception Handling

Python uses `try` and `except` to handle exceptions in a controlled way.

Basic structure:

```python
try:
    # code that may raise an exception
except:
    # code executed when an exception occurs
```

The project demonstrates more specific exception handling:

```python
try:
    # risky operation
except TypeError:
    # handle type-related errors
except ValueError:
    # handle invalid values
except ZeroDivisionError:
    # handle division by zero
```

### `else`

The `else` block runs when the `try` block completes successfully.

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Operation successful")
```

### `finally`

The `finally` block runs whether an exception occurs or not.

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This always runs")
```

### Generic exception handling

The reference also demonstrates:

```python
try:
    # operation
except Exception as e:
    print(e)
```

Specific exception types are preferable when the expected error is known because they make error handling clearer.

## 2. Argument Unpacking

The `*` operator can unpack elements from a list or tuple into separate positional arguments.

```python
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

numbers = [1, 2, 3, 4, 5]

print(sum_of_five_nums(*numbers))
```

Without `*`, the entire list is passed as one argument.

### Extended unpacking

Python also supports collecting remaining elements:

```python
countries = [
    "Finland",
    "Sweden",
    "Norway",
    "Denmark",
    "Iceland"
]

first, second, *rest = countries
```

## 3. Dictionary Unpacking

The `**` operator unpacks dictionary key-value pairs into keyword arguments.

```python
def person_info(name, country, city, age):
    return f"{name} lives in {country}, {city}. Age: {age}"

person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "age": 250
}

print(person_info(**person))
```

The dictionary keys must correspond to the function's parameter names.

## 4. Packing Arguments

Packing is useful when a function should accept an arbitrary number of arguments.

### `*args`

```python
def sum_all(*args):
    total = 0

    for value in args:
        total += value

    return total

print(sum_all(1, 2, 3))
print(sum_all(1, 2, 3, 4, 5))
```

Inside the function, `args` behaves like a tuple.

### `**kwargs`

`**kwargs` collects arbitrary keyword arguments into a dictionary.

```python
def show_person(**kwargs):
    for key, value in kwargs.items():
        print(key, "=", value)

show_person(
    name="Asabeneh",
    country="Finland",
    city="Helsinki"
)
```

Inside the function, `kwargs` behaves like a dictionary.

## 5. Spreading

The `*` operator can also be used to combine list elements into another list.

```python
first = [1, 2, 3]
second = [4, 5, 6]

combined = [0, *first, *second]

print(combined)
```

This creates a new list containing the elements of both source lists.

## 6. `enumerate()`

`enumerate()` provides both the index and the item while iterating through a sequence.

```python
countries = ["Finland", "Sweden", "Norway"]

for index, country in enumerate(countries):
    print(index, country)
```

This is useful when the position of an item is needed during iteration.

## 7. `zip()`

`zip()` combines corresponding elements from multiple iterables.

```python
fruits = ["banana", "orange", "mango"]
vegetables = ["Tomato", "Potato", "Cabbage"]

for fruit, vegetable in zip(fruits, vegetables):
    print(fruit, vegetable)
```

It is useful when related lists need to be processed together.

## 8. Practical Applications

These concepts are useful for:

- Handling invalid user input
- Preventing programs from terminating unexpectedly
- Passing collections into functions
- Writing functions with flexible numbers of arguments
- Combining sequences
- Tracking indexes while iterating
- Processing related datasets together
- Building more robust Python applications

## Important Distinction

| Concept | Main Purpose |
|---|---|
| `try/except` | Handle exceptions |
| `else` | Run when `try` succeeds |
| `finally` | Run regardless of success/failure |
| `*list` | Unpack positional values |
| `**dict` | Unpack keyword values |
| `*args` | Pack arbitrary positional arguments |
| `**kwargs` | Pack arbitrary keyword arguments |
| `[*a, *b]` | Spread/merge iterable elements |
| `enumerate()` | Get index + value |
| `zip()` | Process corresponding items together |

## Exercise

The provided source contains this exercise:

Given:

```python
names = [
    "Finland",
    "Sweden",
    "Norway",
    "Denmark",
    "Iceland",
    "Estonia",
    "Russia"
]
```

Unpack the first five countries into `nordic_countries`, and store Estonia and Russia in `es` and `ru`, respectively.

A solution is included in `exercises/exercises.py`.

## Learning Flow

Recommended order:

1. Understand what an exception is.
2. Learn `try` and `except`.
3. Learn specific exception types.
4. Understand `else` and `finally`.
5. Learn positional unpacking with `*`.
6. Learn dictionary unpacking with `**`.
7. Learn `*args` and `**kwargs`.
8. Understand list spreading.
9. Learn `enumerate()`.
10. Learn `zip()`.
11. Complete the exercise.

## Reference

This project is based on the provided **30 Days of Python — Day 17: Exception Handling** material by **Asabeneh Yetayeh**, Second Edition, July 2021. The source explicitly covers exception handling, packing/unpacking, spreading, `enumerate`, `zip`, and the Day 17 exercise.
