# ============================================================
# 30 DAYS OF PYTHON
# Day 9: Conditionals
# ============================================================

# ============================================================
# 1. If Condition
# ============================================================

a = 3

if a > 0:
    print("A is a positive number")


# ============================================================
# 2. If Else
# ============================================================

a = 3

if a < 0:
    print("A is a negative number")
else:
    print("A is a positive number")


# ============================================================
# 3. If Elif Else
# ============================================================

a = 0

if a > 0:
    print("A is a positive number")
elif a < 0:
    print("A is a negative number")
else:
    print("A is zero")


# ============================================================
# 4. Short Hand If Else
# ============================================================

a = 3

print("A is positive") if a > 0 else print("A is negative")


# ============================================================
# 5. Nested Conditions
# ============================================================

a = 0

if a > 0:
    if a % 2 == 0:
        print("A is a positive and even integer")
    else:
        print("A is a positive number")
elif a == 0:
    print("A is zero")
else:
    print("A is a negative number")


# ============================================================
# 6. If Condition with AND Logical Operator
# ============================================================

a = 0

if a > 0 and a % 2 == 0:
    print("A is an even and positive integer")
elif a > 0 and a % 2 != 0:
    print("A is a positive integer")
elif a == 0:
    print("A is zero")
else:
    print("A is negative")


# ============================================================
# 7. If Condition with OR Logical Operator
# ============================================================

user = "James"
access_level = 3

if user == "admin" or access_level >= 4:
    print("Access granted!")
else:
    print("Access denied!")


# ============================================================
# EXERCISES: LEVEL 1
# ============================================================

# Exercise 1: Driving Age

age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to learn to drive.")
else:
    print(f"You need {18 - age} more years to learn to drive.")


# Exercise 2: Compare Your Age with My Age

my_age = 25
your_age = int(input("Enter your age: "))

if your_age > my_age:
    difference = your_age - my_age
    if difference == 1:
        print("You are 1 year older than me.")
    else:
        print(f"You are {difference} years older than me.")
elif your_age < my_age:
    difference = my_age - your_age
    if difference == 1:
        print("I am 1 year older than you.")
    else:
        print(f"I am {difference} years older than you.")
else:
    print("We are the same age.")


# Exercise 3: Compare Two Numbers

a = float(input("Enter number one: "))
b = float(input("Enter number two: "))

if a > b:
    print(f"{a:g} is greater than {b:g}")
elif a < b:
    print(f"{a:g} is smaller than {b:g}")
else:
    print(f"{a:g} is equal to {b:g}")


# ============================================================
# EXERCISES: LEVEL 2
# ============================================================

# Exercise 1: Grade Calculator

score = float(input("Enter your score: "))

if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score <= 89:
    print("Grade: B")
elif 70 <= score <= 79:
    print("Grade: C")
elif 60 <= score <= 69:
    print("Grade: D")
elif 0 <= score <= 59:
    print("Grade: F")
else:
    print("Invalid score.")


# Exercise 2: Season from Month

month = input("Enter the month: ").strip().lower()

if month in ["september", "october", "november"]:
    print("The season is Autumn.")
elif month in ["december", "january", "february"]:
    print("The season is Winter.")
elif month in ["march", "april", "may"]:
    print("The season is Spring.")
elif month in ["june", "july", "august"]:
    print("The season is Summer.")
else:
    print("Invalid month.")


# Exercise 3: Check and Add Fruit

fruits = ["banana", "orange", "mango", "lemon"]

fruit = input("Enter a fruit: ").strip().lower()

if fruit in fruits:
    print("That fruit already exists in the list.")
else:
    fruits.append(fruit)
    print("Modified list:", fruits)


# ============================================================
# EXERCISES: LEVEL 3
# ============================================================

person = {
    "first_name": "Asabeneh",
    "last_name": "Yetayeh",
    "age": 250,
    "country": "Finland",
    "is_married": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {
        "street": "Space street",
        "zipcode": "02210"
    }
}


# Exercise 1: Print Middle Skill

if "skills" in person:
    skills = person["skills"]
    middle_index = len(skills) // 2
    print("Middle skill:", skills[middle_index])


# Exercise 2: Check for Python Skill

if "skills" in person:
    print("Does the person have Python skill?", "Python" in person["skills"])


# Exercise 3: Determine Developer Title

if "skills" in person:
    skills = person["skills"]

    if skills == ["JavaScript", "React"]:
        print("He is a front end developer")
    elif all(skill in skills for skill in ["Node", "Python", "MongoDB"]):
        print("He is a backend developer")
    elif all(skill in skills for skill in ["React", "Node", "MongoDB"]):
        print("He is a fullstack developer")
    else:
        print("unknown title")


# Exercise 4: Married and Living in Finland

if person["is_married"] and person["country"] == "Finland":
    print(
        f"{person['first_name']} {person['last_name']} lives in "
        f"{person['country']} and is married."
    )
