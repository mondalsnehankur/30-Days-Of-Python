# Day 10 - Practical Loop Applications

print("=== Find the first multiple of 7 greater than 20 ===")
for number in range(21, 101):
    if number % 7 == 0:
        print("Found:", number)
        break

print("\n=== Print numbers except multiples of 3 ===")
for number in range(1, 21):
    if number % 3 == 0:
        continue
    print(number, end=" ")
print()

print("\n=== Search a list using for-else ===")
names = ["Amit", "Riya", "Snehankur", "Rahul"]
target = "Snehankur"

for name in names:
    if name == target:
        print("Found:", target)
        break
else:
    print("Name not found.")

print("\n=== Multiplication table ===")
number = 7
for multiplier in range(1, 11):
    print(f"{number} x {multiplier} = {number * multiplier}")
