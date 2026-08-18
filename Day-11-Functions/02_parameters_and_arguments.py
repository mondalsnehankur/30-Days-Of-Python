# Day 11 - Parameters and Arguments

def greetings(name):
    return name + ", welcome to Python!"

def add_ten(num):
    return num + 10

def square_number(x):
    return x * x

def area_of_circle(radius):
    pi = 3.14
    return pi * radius ** 2

def sum_of_numbers(n):
    total = 0
    for number in range(n + 1):
        total += number
    return total

print(greetings("Snehankur"))
print(add_ten(90))
print(square_number(5))
print(area_of_circle(10))
print(sum_of_numbers(10))

def generate_full_name(first_name, last_name):
    return first_name + " " + last_name

def sum_two_numbers(num_one, num_two):
    return num_one + num_two

print(generate_full_name("Python", "Learner"))
print(sum_two_numbers(1, 9))

# Keyword arguments
print(generate_full_name(last_name="Learner", first_name="Python"))
print(sum_two_numbers(num_two=3, num_one=2))
