# Day 10 - Nested Loops
# A nested loop is a loop inside another loop.

print("=== Nested loop ===")
for row in range(3):
    for column in range(4):
        print(f"({row}, {column})")

print("\n=== 8 x 8 pattern ===")
for row in range(8):
    for column in range(8):
        print("#", end=" ")
    print()

print("\n=== Skills inside a dictionary ===")
person = {
    "name": "Student",
    "skills": ["Python", "SQL", "Git", "Machine Learning"]
}

for key in person:
    if key == "skills":
        for skill in person["skills"]:
            print(skill)
