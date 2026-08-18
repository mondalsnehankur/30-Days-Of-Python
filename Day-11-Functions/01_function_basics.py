# Day 11 - Function Basics

def generate_full_name():
    first_name = "Python"
    last_name = "Learner"
    return first_name + " " + last_name

def add_two_numbers():
    return 2 + 3

print("Full name:", generate_full_name())
print("Sum:", add_two_numbers())

def function_without_return():
    print("This function has no explicit return statement.")

result = function_without_return()
print("Returned value:", result)
