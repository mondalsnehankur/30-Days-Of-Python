# Day 10 - break and continue
# Covers break and continue with while and for loops.

print("=== break in while loop ===")
count = 0
while count < 10:
    print(count)
    count += 1
    if count == 5:
        break

print("\n=== continue in while loop ===")
count = 0
while count < 6:
    count += 1
    if count == 3:
        continue
    print(count)

print("\n=== break in for loop ===")
for number in range(10):
    print(number)
    if number == 5:
        break

print("\n=== continue in for loop ===")
for number in range(10):
    if number == 5:
        continue
    print(number)
