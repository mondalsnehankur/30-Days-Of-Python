# Day 11 - Exercises: Level 3

import keyword

def is_prime(number):
    if number < 2:
        return False
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1
    return True

def all_items_unique(items):
    return len(items) == len(set(items))

def same_data_type(items):
    if not items:
        return True
    first_type = type(items[0])
    for item in items:
        if type(item) is not first_type:
            return False
    return True

def is_valid_python_variable(name):
    return isinstance(name, str) and name.isidentifier() and not keyword.iskeyword(name)

print("17 is prime:", is_prime(17))
print("20 is prime:", is_prime(20))
print("Unique:", all_items_unique([1, 2, 3, 4]))
print("Unique:", all_items_unique([1, 2, 2, 4]))
print("Same data type:", same_data_type([1, 2, 3]))
print("Same data type:", same_data_type([1, "2", 3]))
print("Valid variable:", is_valid_python_variable("student_name"))
print("Valid variable:", is_valid_python_variable("2student"))
print("Valid variable:", is_valid_python_variable("class"))
