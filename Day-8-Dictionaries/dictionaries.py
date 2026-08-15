# ============================================================
# 30 DAYS OF PYTHON
# Day 8: Dictionaries
# ============================================================

# ============================================================
# 1. Creating a Dictionary
# ============================================================

# Empty dictionary
empty_dict = {}

print("Empty Dictionary:", empty_dict)

# Dictionary with initial values
dct = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3',
    'key4': 'value4'
}

print("Dictionary:", dct)

# Dictionary created using dict()
another_dict = dict(name='Snehankur', age=24, country='India')

print("Dictionary using dict():", another_dict)


# ============================================================
# 2. Creating a Dictionary with Different Data Types
# ============================================================

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

print("\nPerson Dictionary:")
print(person)


# ============================================================
# 3. Dictionary Length
# ============================================================

print("\nDictionary Length:")
print("Length of dct:", len(dct))
print("Length of person:", len(person))


# ============================================================
# 4. Accessing Dictionary Items
# ============================================================

print("\nAccessing Dictionary Items:")

print("First Name:", person['first_name'])
print("Last Name:", person['last_name'])
print("Country:", person['country'])
print("Skills:", person['skills'])
print("First Skill:", person['skills'][0])
print("Street:", person['address']['street'])

# Using get() to safely access a key
print("First Name using get():", person.get('first_name'))
print("Country using get():", person.get('country'))
print("Skills using get():", person.get('skills'))

# If key does not exist, get() returns None
print("City using get():", person.get('city'))


# ============================================================
# 5. Adding Items to a Dictionary
# ============================================================

person['job_title'] = 'Instructor'

print("\nAfter adding job title:")
print(person)

# Adding another key
person['city'] = 'Helsinki'

print("\nAfter adding city:")
print(person)

# Adding an item to the existing skills list
person['skills'].append('HTML')

print("\nAfter adding HTML to skills:")
print(person['skills'])


# ============================================================
# 6. Modifying Items in a Dictionary
# ============================================================

person['first_name'] = 'Eyob'
person['age'] = 252
person['country'] = 'Ethiopia'

print("\nAfter modifying dictionary items:")
print(person)


# ============================================================
# 7. Checking Keys in a Dictionary
# ============================================================

print("\nChecking Keys:")

print("'first_name' in person:", 'first_name' in person)
print("'country' in person:", 'country' in person)
print("'city' in person:", 'city' in person)
print("'salary' in person:", 'salary' in person)


# ============================================================
# 8. Removing Key-Value Pairs
# ============================================================

# Create a separate dictionary so that all removal
# operations can be demonstrated independently.

remove_demo = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True
}

print("\nOriginal dictionary for removal:")
print(remove_demo)


# pop()
removed_value = remove_demo.pop('first_name')

print("\nAfter pop('first_name'):")
print(remove_demo)
print("Removed value:", removed_value)


# popitem()
removed_item = remove_demo.popitem()

print("\nAfter popitem():")
print(remove_demo)
print("Removed item:", removed_item)


# del
del remove_demo['age']

print("\nAfter del remove_demo['age']:")
print(remove_demo)


# ============================================================
# 9. Changing Dictionary to a List of Items
# ============================================================

items_demo = {
    'name': 'Snehankur',
    'age': 24,
    'country': 'India'
}

items = items_demo.items()

print("\nDictionary Items:")
print(items)

# Converting dictionary items to an actual list
items_list = list(items)

print("\nItems as a list:")
print(items_list)


# ============================================================
# 10. Clearing a Dictionary
# ============================================================

clear_demo = {
    'name': 'Snehankur',
    'age': 24,
    'country': 'India'
}

print("\nBefore clear():")
print(clear_demo)

clear_demo.clear()

print("After clear():")
print(clear_demo)


# ============================================================
# 11. Deleting a Dictionary
# ============================================================

delete_demo = {
    'name': 'Snehankur',
    'age': 24
}

print("\nDictionary before deletion:")
print(delete_demo)

del delete_demo

print("Dictionary has been completely deleted.")


# ============================================================
# 12. Copying a Dictionary
# ============================================================

original_dict = {
    'name': 'Snehankur',
    'age': 24,
    'country': 'India'
}

copied_dict = original_dict.copy()

print("\nOriginal Dictionary:")
print(original_dict)

print("Copied Dictionary:")
print(copied_dict)

# Modify the copy
copied_dict['age'] = 25

print("\nAfter modifying copied dictionary:")
print("Original:", original_dict)
print("Copy:", copied_dict)


# ============================================================
# 13. Getting Dictionary Keys
# ============================================================

keys_demo = {
    'name': 'Snehankur',
    'age': 24,
    'country': 'India',
    'course': 'MCA'
}

keys = keys_demo.keys()

print("\nDictionary Keys:")
print(keys)

# Convert keys to a list
keys_list = list(keys)

print("Keys as a list:")
print(keys_list)


# ============================================================
# 14. Getting Dictionary Values
# ============================================================

values = keys_demo.values()

print("\nDictionary Values:")
print(values)

# Convert values to a list
values_list = list(values)

print("Values as a list:")
print(values_list)


# ============================================================
# 15. Iterating Through Dictionary Keys
# ============================================================

print("\nIterating Through Keys:")

for key in keys_demo:
    print(key)


# ============================================================
# 16. Iterating Through Dictionary Values
# ============================================================

print("\nIterating Through Values:")

for value in keys_demo.values():
    print(value)


# ============================================================
# 17. Iterating Through Key-Value Pairs
# ============================================================

print("\nIterating Through Key-Value Pairs:")

for key, value in keys_demo.items():
    print(key, ":", value)


# ============================================================
# 18. Complete Dictionary Example
# ============================================================

student = {
    'name': 'Snehankur',
    'age': 24,
    'course': 'MCA',
    'university': 'Christ University',
    'skills': ['Python', 'SQL', 'HTML', 'CSS'],
    'marks': {
        'Python': 90,
        'SQL': 85,
        'DBMS': 88
    }
}

print("\n================ STUDENT DICTIONARY ================")

print("Student:", student)

print("Name:", student['name'])
print("Course:", student['course'])
print("University:", student['university'])

print("Skills:", student['skills'])
print("First Skill:", student['skills'][0])

print("Python Marks:", student['marks']['Python'])

print("Number of Dictionary Items:", len(student))

# Add a new skill
student['skills'].append('Java')

# Add a new dictionary item
student['semester'] = 1

# Modify an existing value
student['age'] = 25

print("\nUpdated Student Dictionary:")
print(student)

# Check whether a key exists
print("\nChecking Keys:")
print("'semester' in student:", 'semester' in student)
print("'address' in student:", 'address' in student)

# Access using get()
print("\nUsing get():")
print(student.get('name'))
print(student.get('address'))

# Display keys
print("\nKeys:")
print(list(student.keys()))

# Display values
print("\nValues:")
print(list(student.values()))

# Display items
print("\nItems:")
print(list(student.items()))


# ============================================================
# END OF DAY 8
# ============================================================

print("\n====================================================")
print("Day 8 - Dictionaries Completed!")
print("====================================================")