# Day 10 - Loop Exercises
# Based on the Day 10 exercises in the supplied learning material.

print("=== 1. Iterate 0 to 10 using for ===")
for number in range(11):
    print(number, end=" ")
print()

print("\n=== 2. Iterate 0 to 10 using while ===")
number = 0
while number <= 10:
    print(number, end=" ")
    number += 1
print()

print("\n=== 3. Iterate 10 to 0 using for ===")
for number in range(10, -1, -1):
    print(number, end=" ")
print()

print("\n=== 4. Iterate 10 to 0 using while ===")
number = 10
while number >= 0:
    print(number, end=" ")
    number -= 1
print()

print("\n=== 5. Seven-row triangle ===")
for row in range(1, 8):
    print("#" * row)

print("\n=== 6. 8 x 8 grid ===")
for row in range(8):
    for column in range(8):
        print("#", end=" ")
    print()

print("\n=== 7. Square table from 0 to 10 ===")
for number in range(11):
    print(f"{number} x {number} = {number * number}")

print("\n=== 8. Iterate through a list ===")
items = ["Python", "Numpy", "Pandas", "Django", "Flask"]
for item in items:
    print(item)

print("\n=== 9. Even numbers from 0 to 100 ===")
for number in range(101):
    if number % 2 == 0:
        print(number, end=" ")
print()

print("\n=== 10. Odd numbers from 0 to 100 ===")
for number in range(101):
    if number % 2 != 0:
        print(number, end=" ")
print()

print("\n=== 11. Sum of numbers from 0 to 100 ===")
total = 0
for number in range(101):
    total += number
print("Sum =", total)

print("\n=== 12. Sum of evens and odds ===")
even_sum = 0
odd_sum = 0

for number in range(101):
    if number % 2 == 0:
        even_sum += number
    else:
        odd_sum += number

print("Even sum =", even_sum)
print("Odd sum =", odd_sum)

print("\n=== 13. Reverse a list using a loop ===")
fruits = ["banana", "orange", "mango", "lemon"]
reversed_fruits = []

for index in range(len(fruits) - 1, -1, -1):
    reversed_fruits.append(fruits[index])

print(reversed_fruits)
