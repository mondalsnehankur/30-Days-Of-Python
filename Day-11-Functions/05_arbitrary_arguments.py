# Day 11 - Arbitrary Positional Arguments

def sum_all_nums(*nums):
    total = 0
    for num in nums:
        if not isinstance(num, (int, float)):
            raise TypeError("All arguments must be numbers.")
        total += num
    return total

def generate_groups(team, *members):
    print("Team:", team)
    for member in members:
        print("Member:", member)

print("Sum:", sum_all_nums(2, 3, 5))
print("Sum:", sum_all_nums(1, 2, 3, 4, 5))
generate_groups("Team-1", "Alice", "Bob", "Charlie", "David")
