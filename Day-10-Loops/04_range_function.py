# Day 10 - range()
# range(start, stop, step)
# The stop value is excluded.

print("=== range(stop) ===")
for number in range(11):
    print(number)

print("\n=== range(start, stop) ===")
for number in range(1, 11):
    print(number)

print("\n=== range(start, stop, step) ===")
for number in range(0, 11, 2):
    print(number)

print("\n=== Backward range ===")
for number in range(11, 0, -2):
    print(number)

print("\n=== Converting range to list ===")
print(list(range(11)))
print(list(range(0, 11, 2)))
