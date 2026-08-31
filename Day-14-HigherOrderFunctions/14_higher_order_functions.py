"""
30 Days of Python - Day 14
Higher Order Functions

Complete solutions and examples for the Day 14 README exercises.

Topics covered:
- Higher-order functions
- Functions as parameters
- Functions as return values
- Closures
- Decorators
- Multiple decorators
- Decorators with parameters
- map()
- filter()
- reduce()
- Day 14 exercises: Levels 1, 2 and 3

Level 3 uses the original 30 Days of Python countries-data.py file.
Place it at:
    data/countries-data.py

The source file defines a variable named `countries_data`.
"""

from functools import reduce
from collections import Counter
from pathlib import Path
import importlib.util


# ============================================================
# 1. HIGHER ORDER FUNCTIONS
# ============================================================

def sum_numbers(numbers):
    """Return the sum of numbers."""
    return sum(numbers)


def higher_order_function(function, values):
    """Accept a function as an argument and apply it to values."""
    return function(values)


def square(number):
    return number ** 2


def cube(number):
    return number ** 3


def absolute(number):
    return number if number >= 0 else -number


def function_selector(function_type):
    """Return a function based on the requested operation."""
    functions = {
        "square": square,
        "cube": cube,
        "absolute": absolute,
    }
    return functions.get(function_type)


# ============================================================
# 2. PYTHON CLOSURES
# ============================================================

def add_ten():
    """Return a closure that adds 10 to its argument."""
    ten = 10

    def add(number):
        return number + ten

    return add


# ============================================================
# 3. PYTHON DECORATORS
# ============================================================

def uppercase_decorator(function):
    """Convert the decorated function's returned string to uppercase."""

    def wrapper():
        return function().upper()

    return wrapper


@uppercase_decorator
def greeting():
    return "Welcome to Python"


def split_string_decorator(function):
    """Split the decorated function's returned string into words."""

    def wrapper():
        return function().split()

    return wrapper


@split_string_decorator
@uppercase_decorator
def decorated_greeting():
    return "Welcome to Python"


def decorator_with_parameters(function):
    """Decorator for a function accepting three positional arguments."""

    def wrapper_accepting_parameters(first_name, last_name, country):
        function(first_name, last_name, country)
        print(f"I live in {country}")

    return wrapper_accepting_parameters


@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print(f"I am {first_name} {last_name}. I love to teach.")


# ============================================================
# 4. BUILT-IN HIGHER ORDER FUNCTIONS
# ============================================================

def demonstrate_map():
    numbers = [1, 2, 3, 4, 5]

    numbers_squared = list(map(square, numbers))
    numbers_squared_lambda = list(map(lambda x: x ** 2, numbers))

    numbers_str = ["1", "2", "3", "4", "5"]
    numbers_int = list(map(int, numbers_str))

    names = ["Asabeneh", "Lidiya", "Ermias", "Abraham"]
    names_upper = list(map(str.upper, names))

    return {
        "squares": numbers_squared,
        "squares_lambda": numbers_squared_lambda,
        "strings_to_int": numbers_int,
        "uppercase_names": names_upper,
    }


def is_even(number):
    return number % 2 == 0


def is_odd(number):
    return number % 2 != 0


def is_name_long(name):
    return len(name) > 7


def demonstrate_filter():
    numbers = [1, 2, 3, 4, 5]
    names = ["Asabeneh", "Lidiya", "Ermias", "Abraham"]

    return {
        "even_numbers": list(filter(is_even, numbers)),
        "odd_numbers": list(filter(is_odd, numbers)),
        "long_names": list(filter(is_name_long, names)),
    }


def add_two_numbers(x, y):
    return int(x) + int(y)


def demonstrate_reduce():
    numbers_str = ["1", "2", "3", "4", "5"]
    return reduce(add_two_numbers, numbers_str)


# ============================================================
# 5. DAY 14 EXERCISES - DATA
# ============================================================

countries = [
    "Estonia",
    "Finland",
    "Sweden",
    "Denmark",
    "Norway",
    "Iceland",
]

names = ["Asabeneh", "Lidiya", "Ermias", "Abraham"]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# ============================================================
# LEVEL 1
# ============================================================

def level_1_for_loops():
    """Print every country, name and number using for loops."""
    print("Countries:")
    for country in countries:
        print(country)

    print("\nNames:")
    for name in names:
        print(name)

    print("\nNumbers:")
    for number in numbers:
        print(number)


def level_1_call_function_examples():
    """Use named functions with map, filter and reduce."""
    mapped = list(map(square, numbers))
    filtered = list(filter(is_even, numbers))
    reduced = reduce(lambda x, y: x + y, numbers)

    return mapped, filtered, reduced


# ============================================================
# LEVEL 2
# ============================================================

def countries_uppercase(country_list):
    """Return countries converted to uppercase using map."""
    return list(map(str.upper, country_list))


def numbers_squared(number_list):
    """Return squares of numbers using map."""
    return list(map(lambda number: number ** 2, number_list))


def names_uppercase(name_list):
    """Return names converted to uppercase using map."""
    return list(map(str.upper, name_list))


def countries_containing_land(country_list):
    """Return countries containing 'land'."""
    return list(filter(lambda country: "land" in country.lower(), country_list))


def countries_exactly_six_characters(country_list):
    """Return countries with exactly six characters."""
    return list(filter(lambda country: len(country) == 6, country_list))


def countries_six_or_more_characters(country_list):
    """Return countries with six or more characters."""
    return list(filter(lambda country: len(country) >= 6, country_list))


def countries_starting_with_e(country_list):
    """Return countries beginning with E."""
    return list(filter(lambda country: country.startswith("E"), country_list))


def chain_map_filter_reduce(number_list):
    """
    Chain map, filter and reduce:
    1. Square each number.
    2. Keep only values greater than 20.
    3. Add the remaining values.
    """
    squared = map(lambda number: number ** 2, number_list)
    filtered = filter(lambda number: number > 20, squared)
    return reduce(lambda x, y: x + y, filtered, 0)


def get_string_lists(items):
    """Return only string items from a list."""
    return list(filter(lambda item: isinstance(item, str), items))


def sum_with_reduce(number_list):
    """Sum all numbers using reduce."""
    return reduce(lambda x, y: x + y, number_list, 0)


def concatenate_countries(country_list):
    """Create the required North European countries sentence using reduce."""
    country_text = reduce(
        lambda result, country: f"{result}, {country}",
        country_list,
    )
    return f"{country_text} are north European countries"


def categorize_countries(country_list, pattern):
    """Return countries containing the requested pattern."""
    return list(filter(lambda country: pattern.lower() in country.lower(), country_list))


def count_countries_by_first_letter(country_list):
    """
    Return a dictionary where each key is the starting letter
    and each value is the number of countries beginning with it.
    """
    return dict(
        sorted(
            Counter(country[0].upper() for country in country_list if country).items()
        )
    )


def get_first_ten_countries(country_list):
    """Return the first ten countries."""
    return country_list[:10]


def get_last_ten_countries(country_list):
    """Return the last ten countries."""
    return country_list[-10:]


# ============================================================
# LEVEL 3 - COUNTRIES DATA
# ============================================================

def load_countries_data():
    """
    Load countries_data from data/countries-data.py.

    The original challenge stores the data as a Python file rather
    than a JSON file, so importlib is used to load it safely by path.
    """
    data_path = Path(__file__).resolve().parent / "data" / "countries-data.py"

    if not data_path.exists():
        raise FileNotFoundError(
            "countries-data.py was not found. Place the original file at "
            "'data/countries-data.py' relative to this script."
        )

    spec = importlib.util.spec_from_file_location("countries_data_module", data_path)
    if spec is None or spec.loader is None:
        raise ImportError("Could not create an import specification for countries-data.py.")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    if not hasattr(module, "countries_data"):
        raise AttributeError(
            "countries-data.py does not contain the expected 'countries_data' variable."
        )

    return module.countries_data


def sort_countries_by_name(country_data):
    """Sort country dictionaries alphabetically by country name."""
    return sorted(country_data, key=lambda country: country.get("name", ""))


def sort_countries_by_capital(country_data):
    """Sort country dictionaries alphabetically by capital."""
    return sorted(country_data, key=lambda country: country.get("capital", ""))


def sort_countries_by_population(country_data):
    """Sort country dictionaries by population, smallest first."""
    return sorted(country_data, key=lambda country: country.get("population", 0))


def top_ten_spoken_languages(country_data):
    """
    Return the ten most frequently occurring languages.

    Each country may contain multiple languages, so every language
    occurrence is counted across all countries.
    """
    language_counter = Counter()

    for country in country_data:
        for language in country.get("languages", []):
            language_counter[language] += 1

    return language_counter.most_common(10)


def top_ten_populated_countries(country_data):
    """Return the ten countries with the largest populations."""
    return sorted(
        country_data,
        key=lambda country: country.get("population", 0),
        reverse=True,
    )[:10]


# ============================================================
# DEMONSTRATION
# ============================================================

def main():
    print("=" * 60)
    print("30 DAYS OF PYTHON - DAY 14")
    print("HIGHER ORDER FUNCTIONS")
    print("=" * 60)

    # Higher-order function: function as a parameter
    print("\n1. Function as a parameter:")
    print(higher_order_function(sum_numbers, [1, 2, 3, 4, 5]))

    # Higher-order function: function as a return value
    print("\n2. Function as a return value:")
    selected_square = function_selector("square")
    selected_cube = function_selector("cube")
    selected_absolute = function_selector("absolute")
    print(selected_square(3))
    print(selected_cube(3))
    print(selected_absolute(-3))

    # Closure
    print("\n3. Closure:")
    add_ten_function = add_ten()
    print(add_ten_function(5))
    print(add_ten_function(10))

    # Decorator
    print("\n4. Decorator:")
    print(greeting())

    # Multiple decorators
    print("\n5. Multiple decorators:")
    print(decorated_greeting())

    # Decorator accepting parameters
    print("\n6. Decorator with parameters:")
    print_full_name("Asabeneh", "Yetayeh", "Finland")

    # Built-in higher-order functions
    print("\n7. map():")
    print(demonstrate_map())

    print("\n8. filter():")
    print(demonstrate_filter())

    print("\n9. reduce():")
    print(demonstrate_reduce())

    # Level 1
    print("\n10. Level 1:")
    print(level_1_call_function_examples())

    # Level 2
    print("\n11. Level 2:")
    print("Uppercase countries:", countries_uppercase(countries))
    print("Squared numbers:", numbers_squared(numbers))
    print("Uppercase names:", names_uppercase(names))
    print("Countries containing 'land':", countries_containing_land(countries))
    print("Countries with exactly 6 characters:",
          countries_exactly_six_characters(countries))
    print("Countries with 6+ characters:",
          countries_six_or_more_characters(countries))
    print("Countries starting with E:", countries_starting_with_e(countries))
    print("Chained map/filter/reduce:", chain_map_filter_reduce(numbers))
    print("Only strings:", get_string_lists([1, "Python", 2, "Functions", 3]))
    print("Sum using reduce:", sum_with_reduce(numbers))
    print("Country sentence:", concatenate_countries(countries))
    print("Countries containing 'ia':", categorize_countries(countries, "ia"))
    print("Countries by first letter:", count_countries_by_first_letter(countries))
    print("First ten:", get_first_ten_countries(countries))
    print("Last ten:", get_last_ten_countries(countries))

    # Level 3
    print("\n12. Level 3:")
    try:
        country_data = load_countries_data()

        print("First 5 countries sorted by name:")
        for country in sort_countries_by_name(country_data)[:5]:
            print(country.get("name"))

        print("\nFirst 5 countries sorted by capital:")
        for country in sort_countries_by_capital(country_data)[:5]:
            print(country.get("name"), "-", country.get("capital"))

        print("\nFirst 5 countries sorted by population:")
        for country in sort_countries_by_population(country_data)[:5]:
            print(country.get("name"), "-", country.get("population"))

        print("\nTen most spoken languages:")
        print(top_ten_spoken_languages(country_data))

        print("\nTen most populated countries:")
        for country in top_ten_populated_countries(country_data):
            print(country.get("name"), "-", country.get("population"))

    except (FileNotFoundError, ImportError, AttributeError) as error:
        print(f"Level 3 data not loaded: {error}")


if __name__ == "__main__":
    main()
