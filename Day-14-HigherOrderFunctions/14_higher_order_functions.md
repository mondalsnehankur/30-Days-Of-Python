# 🐍 30 Days of Python — Day 14: Higher Order Functions

Complete Day 14 notes and exercise solutions based on the supplied **30 Days of Python: Day 14 - Higher Order Functions** README. citeturn0search2

## 📁 Repository Files

```text
14_Day_Higher_order_functions/
├── 14_higher_order_functions.py
├── 14_higher_order_functions.md
└── data/
    ├── countries.py
    └── countries-data.py
```

> `countries.py` and `countries-data.py` are external data files referenced by the original Day 14 exercises. The Level 3 solutions in the Python file expect `countries-data.py` at `data/countries-data.py`.

---

# 📘 Day 14 — Higher Order Functions

Python treats functions as **first-class objects**. This means that functions can be:

- Passed as arguments to other functions.
- Returned from other functions.
- Assigned to variables.
- Modified or wrapped by other functions.

The supplied Day 14 material focuses on higher-order functions, closures, decorators, and the built-in `map()`, `filter()`, and `reduce()` functions. fileciteturn0file0L38-L53

---

## 1. Higher Order Functions

A **higher-order function** is a function that either:

1. Takes another function as an argument, or
2. Returns another function as its result.

### Function as a parameter

```python
def sum_numbers(numbers):
    return sum(numbers)


def higher_order_function(function, values):
    result = function(values)
    return result


result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)
```

Output:

```text
15
```

Here, `sum_numbers` is passed into `higher_order_function` as an argument.

### Function as a return value

```python
def square(number):
    return number ** 2


def cube(number):
    return number ** 3


def absolute(number):
    if number >= 0:
        return number
    return -number


def function_selector(function_type):
    if function_type == "square":
        return square
    elif function_type == "cube":
        return cube
    elif function_type == "absolute":
        return absolute


result = function_selector("square")
print(result(3))

result = function_selector("cube")
print(result(3))

result = function_selector("absolute")
print(result(-3))
```

Output:

```text
9
27
3
```

The function `function_selector()` returns a different function depending on the argument supplied. fileciteturn0file0L68-L99

---

# 2. Python Closures

A **closure** occurs when a nested function remembers and can access a variable from its enclosing function even after the enclosing function has finished executing.

Basic structure:

```python
def outer_function():
    value = something

    def inner_function():
        return value

    return inner_function
```

### Example

```python
def add_ten():
    ten = 10

    def add(number):
        return number + ten

    return add


closure_result = add_ten()

print(closure_result(5))
print(closure_result(10))
```

Output:

```text
15
20
```

The inner `add()` function retains access to `ten`, creating a closure. fileciteturn0file0L101-L117

---

# 3. Python Decorators

A **decorator** allows us to add functionality to an existing function without changing the original function's implementation.

A decorator normally contains:

- An outer function that receives another function.
- An inner wrapper function.
- A returned wrapper.

The supplied material describes decorators as a design pattern for adding functionality to an existing object without modifying its structure. fileciteturn0file0L119-L125

## Creating a decorator

```python
def uppercase_decorator(function):
    def wrapper():
        func = function()
        return func.upper()

    return wrapper
```

It can be applied manually:

```python
def greeting():
    return "Welcome to Python"


greeting = uppercase_decorator(greeting)

print(greeting())
```

Output:

```text
WELCOME TO PYTHON
```

### Using `@` syntax

The same decorator can be applied more cleanly:

```python
@uppercase_decorator
def greeting():
    return "Welcome to Python"


print(greeting())
```

Output:

```text
WELCOME TO PYTHON
```

---

# 4. Multiple Decorators

More than one decorator can be applied to a function.

```python
def uppercase_decorator(function):
    def wrapper():
        return function().upper()

    return wrapper


def split_string_decorator(function):
    def wrapper():
        return function().split()

    return wrapper


@split_string_decorator
@uppercase_decorator
def greeting():
    return "Welcome to Python"


print(greeting())
```

Output:

```text
['WELCOME', 'TO', 'PYTHON']
```

The order matters. Decorators are applied from the bottom upward:

```text
greeting
   ↓
uppercase_decorator
   ↓
split_string_decorator
```

This matters because `.upper()` works on a string, while `.split()` produces a list. fileciteturn0file0L159-L187

---

# 5. Decorators Accepting Parameters

Decorators can also wrap functions that accept parameters.

```python
def decorator_with_parameters(function):
    def wrapper_accepting_parameters(first_name, last_name, country):
        function(first_name, last_name, country)
        print(f"I live in {country}")

    return wrapper_accepting_parameters


@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print(f"I am {first_name} {last_name}. I love to teach.")


print_full_name("Asabeneh", "Yetayeh", "Finland")
```

Output:

```text
I am Asabeneh Yetayeh. I love to teach.
I live in Finland
```

This follows the parameterized-decorator example in the supplied material. fileciteturn0file0L190-L206

---

# 6. Built-in Higher Order Functions

The three important built-in functions covered in Day 14 are:

| Function | Purpose | Returns |
|---|---|---|
| `map()` | Transform every item | A map iterator |
| `filter()` | Keep items satisfying a condition | A filter iterator |
| `reduce()` | Combine items into one result | A single value |

The original material specifically covers `map()`, `filter()`, and `reduce()`. fileciteturn0file0L209-L214

---

## 6.1 `map()`

### Syntax

```python
map(function, iterable)
```

`map()` applies a function to every item in an iterable.

### Example

```python
numbers = [1, 2, 3, 4, 5]

numbers_squared = map(lambda x: x ** 2, numbers)

print(list(numbers_squared))
```

Output:

```text
[1, 4, 9, 16, 25]
```

The same operation can be written using a normal function:

```python
def square(number):
    return number ** 2


numbers_squared = map(square, numbers)

print(list(numbers_squared))
```

The supplied examples also demonstrate converting strings to integers and converting names to uppercase with `map()`. fileciteturn0file0L214-L260

---

## 6.2 `filter()`

### Syntax

```python
filter(function, iterable)
```

`filter()` keeps only the items for which the function returns `True`.

### Example — even numbers

```python
numbers = [1, 2, 3, 4, 5]

even_numbers = filter(lambda number: number % 2 == 0, numbers)

print(list(even_numbers))
```

Output:

```text
[2, 4]
```

### Example — odd numbers

```python
odd_numbers = filter(lambda number: number % 2 != 0, numbers)

print(list(odd_numbers))
```

Output:

```text
[1, 3, 5]
```

The supplied material also demonstrates filtering names according to their length. fileciteturn0file0L262-L310

---

## 6.3 `reduce()`

`reduce()` is provided by Python's `functools` module.

Import it with:

```python
from functools import reduce
```

### Syntax

```python
reduce(function, iterable)
```

Unlike `map()` and `filter()`, `reduce()` combines the iterable into a single result.

### Example

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

total = reduce(lambda x, y: x + y, numbers)

print(total)
```

Output:

```text
15
```

The original example also demonstrates using `reduce()` to add values stored as strings. fileciteturn0file0L312-L324

---

# 💻 Exercises — Day 14

The original exercise data is:

```python
countries = [
    "Estonia",
    "Finland",
    "Sweden",
    "Denmark",
    "Norway",
    "Iceland",
]

names = [
    "Asabeneh",
    "Lidiya",
    "Ermias",
    "Abraham",
]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

These lists and the exercise structure are taken from the supplied Day 14 README. fileciteturn0file0L326-L330

---

# 🟢 Level 1 — Solutions

## 1. Difference between `map`, `filter`, and `reduce`

### `map()`

Transforms every item.

```python
list(map(lambda x: x ** 2, numbers))
```

### `filter()`

Keeps only items satisfying a condition.

```python
list(filter(lambda x: x % 2 == 0, numbers))
```

### `reduce()`

Combines items into one final value.

```python
reduce(lambda x, y: x + y, numbers)
```

In short:

```text
map    → transform
filter → select
reduce → combine
```

---

## 2. Difference between higher-order function, closure and decorator

| Concept | Meaning |
|---|---|
| Higher-order function | Takes a function as an argument or returns a function |
| Closure | Inner function remembers variables from its enclosing scope |
| Decorator | A function that wraps another function to add or modify behavior |

---

## 3. Define callback functions before `map`, `filter`, or `reduce`

```python
def square(number):
    return number ** 2


def is_even(number):
    return number % 2 == 0


def add(x, y):
    return x + y


mapped = list(map(square, numbers))
filtered = list(filter(is_even, numbers))
reduced = reduce(add, numbers)

print(mapped)
print(filtered)
print(reduced)
```

---

## 4. Print every country using a `for` loop

```python
for country in countries:
    print(country)
```

## 5. Print every name

```python
for name in names:
    print(name)
```

## 6. Print every number

```python
for number in numbers:
    print(number)
```

---

# 🟡 Level 2 — Solutions

## 1. Convert countries to uppercase

```python
result = list(map(str.upper, countries))
```

## 2. Square every number

```python
result = list(map(lambda number: number ** 2, numbers))
```

## 3. Convert names to uppercase

```python
result = list(map(str.upper, names))
```

## 4. Filter countries containing `land`

```python
result = list(
    filter(lambda country: "land" in country.lower(), countries)
)
```

## 5. Countries with exactly six characters

```python
result = list(
    filter(lambda country: len(country) == 6, countries)
)
```

## 6. Countries with six or more characters

```python
result = list(
    filter(lambda country: len(country) >= 6, countries)
)
```

## 7. Countries starting with `E`

```python
result = list(
    filter(lambda country: country.startswith("E"), countries)
)
```

## 8. Chain `map`, `filter`, and `reduce`

Python's built-in `map()` and `filter()` return iterators, so they can be chained and finally passed to `reduce()`.

```python
result = reduce(
    lambda x, y: x + y,
    filter(
        lambda x: x > 20,
        map(lambda x: x ** 2, numbers)
    ),
    0
)
```

For the supplied numbers, the squared values greater than 20 are:

```text
25, 36, 49, 64, 81, 100
```

Their sum is:

```text
355
```

## 9. `get_string_lists()`

```python
def get_string_lists(items):
    return list(filter(lambda item: isinstance(item, str), items))
```

Example:

```python
print(get_string_lists([1, "Python", 2, "Functions"]))
```

Output:

```text
['Python', 'Functions']
```

## 10. Sum numbers using `reduce()`

```python
result = reduce(lambda x, y: x + y, numbers)
```

Output:

```text
55
```

## 11. Concatenate countries using `reduce()`

```python
result = reduce(
    lambda result, country: f"{result}, {country}",
    countries
)

sentence = f"{result} are north European countries"
print(sentence)
```

Output:

```text
Estonia, Finland, Sweden, Denmark, Norway, Iceland are north European countries
```

## 12. `categorize_countries()`

```python
def categorize_countries(country_list, pattern):
    return list(
        filter(
            lambda country: pattern.lower() in country.lower(),
            country_list
        )
    )
```

Examples:

```python
print(categorize_countries(countries, "land"))
print(categorize_countries(countries, "ia"))
print(categorize_countries(countries, "island"))
print(categorize_countries(countries, "stan"))
```

The exercise asks for countries sharing common patterns such as `land`, `ia`, `island`, and `stan`. citeturn0search2

## 13. Count countries by starting letter

```python
from collections import Counter


def count_countries_by_first_letter(country_list):
    return dict(
        sorted(
            Counter(
                country[0].upper()
                for country in country_list
                if country
            ).items()
        )
    )
```

Example:

```python
print(count_countries_by_first_letter(countries))
```

## 14. First ten countries

```python
def get_first_ten_countries(country_list):
    return country_list[:10]
```

## 15. Last ten countries

```python
def get_last_ten_countries(country_list):
    return country_list[-10:]
```

The original repository provides a dedicated `countries.py` dataset for these country-list exercises. citeturn0search1

---

# 🔴 Level 3 — Solutions

Level 3 requires the `countries-data.py` dataset and asks for:

- Sorting countries by name.
- Sorting countries by capital.
- Sorting countries by population.
- Finding the ten most spoken languages.
- Finding the ten most populated countries. fileciteturn0file0L361-L366

The original repository's `countries-data.py` contains country dictionaries with fields such as `name`, `capital`, `languages`, and `population`. citeturn0search0

## 1. Sort countries by name

```python
sorted_by_name = sorted(
    countries_data,
    key=lambda country: country["name"]
)
```

## 2. Sort countries by capital

```python
sorted_by_capital = sorted(
    countries_data,
    key=lambda country: country["capital"]
)
```

## 3. Sort countries by population

```python
sorted_by_population = sorted(
    countries_data,
    key=lambda country: country["population"]
)
```

To see the largest populations first:

```python
sorted_by_population = sorted(
    countries_data,
    key=lambda country: country["population"],
    reverse=True
)
```

## 4. Ten most spoken languages

Each country may have more than one language, so count every language occurrence.

```python
from collections import Counter

language_counter = Counter()

for country in countries_data:
    for language in country["languages"]:
        language_counter[language] += 1

top_ten_languages = language_counter.most_common(10)

print(top_ten_languages)
```

## 5. Ten most populated countries

```python
top_ten_populated = sorted(
    countries_data,
    key=lambda country: country["population"],
    reverse=True
)[:10]

for country in top_ten_populated:
    print(country["name"], country["population"])
```

---

# ▶️ How to Run

From the repository directory:

```bash
python 14_higher_order_functions.py
```

If your system uses `python3`:

```bash
python3 14_higher_order_functions.py
```

The script runs the examples and Level 1/2 solutions automatically.

For Level 3, make sure the directory structure is:

```text
14_Day_Higher_order_functions/
├── 14_higher_order_functions.py
└── data/
    └── countries-data.py
```

---

# 🧠 Quick Revision

```text
Higher-order function
    ↓
Takes a function OR returns a function

Closure
    ↓
Inner function remembers outer variables

Decorator
    ↓
Wraps a function and adds/modifies behavior

map()
    ↓
Transform every item

filter()
    ↓
Keep selected items

reduce()
    ↓
Combine items into one result
```

### Most important syntax

```python
map(function, iterable)
filter(function, iterable)
reduce(function, iterable)
```

And:

```python
@decorator
def function():
    ...
```

---

## Source Scope

This repository version follows the supplied Day 14 README's topic structure and exercises. fileciteturn0file0L20-L35

The original Day 14 repository also identifies the topic as **Higher Order Functions** within the 30 Days of Python sequence. citeturn0search4
