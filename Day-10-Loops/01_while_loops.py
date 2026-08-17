# Day 10 - While Loops
# Covers: basic while loop, while-else, counting up/down.

print("=== Basic while loop ===")
count = 0
while count < 5:
    print(count)
    count += 1

print("\n=== While loop with else ===")
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("Loop ended. count =", count)

print("\n=== Count down ===")
count = 10
while count >= 0:
    print(count)
    count -= 1
