# Day 10 - for-else and pass

print("=== for-else ===")
for number in range(5):
    print(number)
else:
    print("The loop completed normally.")

print("\n=== for-else with break ===")
for number in range(10):
    print(number)
    if number == 5:
        break
else:
    # This does not execute because the loop was stopped by break.
    print("This will not be printed.")

print("\n=== pass ===")
for number in range(5):
    pass

print("pass allowed the loop body to remain empty.")
