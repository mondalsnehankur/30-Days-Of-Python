# Day 10 - For Loops
# A for loop iterates over sequences such as lists, tuples,
# dictionaries, sets, and strings.

print("=== For loop over a list ===")
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:
    print(number)

print("\n=== For loop over a string ===")
language = "Python"
for letter in language:
    print(letter)

print("\n=== For loop using indexes ===")
for index in range(len(language)):
    print(language[index])

print("\n=== For loop over a tuple ===")
numbers_tuple = (0, 1, 2, 3, 4, 5)
for number in numbers_tuple:
    print(number)

print("\n=== For loop over a dictionary ===")
person = {
    "first_name": "Asabeneh",
    "last_name": "Yetayeh",
    "age": 250,
    "country": "Finland"
}

for key in person:
    print(key)

print("\nKeys and values:")
for key, value in person.items():
    print(key, value)

print("\n=== For loop over a set ===")
companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
for company in companies:
    print(company)
