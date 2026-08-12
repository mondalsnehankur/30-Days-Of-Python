# ============================================================
# DAY 6 - TUPLES
# 30 Days of Python
# ============================================================

# A tuple is an ordered and immutable collection.
# Tuples are generally written using parentheses ().

# ============================================================
# 1. CREATING A TUPLE
# ============================================================

# Empty tuple
empty_tuple = ()
print("Empty tuple:", empty_tuple)

# Empty tuple using tuple()
empty_tuple_2 = tuple()
print("Empty tuple using tuple():", empty_tuple_2)

# Tuple with values
fruits = ('banana', 'orange', 'mango', 'lemon')
print("Fruits:", fruits)

# Tuple containing different data types
mixed_tuple = ('Python', 30, 3.14, True)
print("Mixed tuple:", mixed_tuple)

# Single-item tuple
single_item = ('Python',)
print("Single-item tuple:", single_item)


# ============================================================
# 2. TUPLE LENGTH
# ============================================================

print("\n--- Tuple Length ---")

print("Number of fruits:", len(fruits))


# ============================================================
# 3. ACCESSING TUPLE ITEMS
# ============================================================

print("\n--- Accessing Tuple Items ---")

# Positive indexing
first_fruit = fruits[0]
second_fruit = fruits[1]

print("First fruit:", first_fruit)
print("Second fruit:", second_fruit)

# Last item using length
last_index = len(fruits) - 1
last_fruit = fruits[last_index]

print("Last fruit:", last_fruit)


# ============================================================
# 4. NEGATIVE INDEXING
# ============================================================

print("\n--- Negative Indexing ---")

print("First fruit:", fruits[-4])
print("Second fruit:", fruits[-3])
print("Second-last fruit:", fruits[-2])
print("Last fruit:", fruits[-1])


# ============================================================
# 5. SLICING TUPLES
# ============================================================

print("\n--- Tuple Slicing ---")

# Positive slicing
all_fruits = fruits[0:4]
print("All fruits:", all_fruits)

all_fruits = fruits[0:]
print("All fruits:", all_fruits)

orange_mango = fruits[1:3]
print("Orange and mango:", orange_mango)

orange_to_end = fruits[1:]
print("Orange to the end:", orange_to_end)

# Negative slicing
all_fruits = fruits[-4:]
print("All fruits using negative slicing:", all_fruits)

orange_mango = fruits[-3:-1]
print("Orange and mango:", orange_mango)

orange_to_end = fruits[-3:]
print("Orange to the end:", orange_to_end)


# ============================================================
# 6. TUPLES ARE IMMUTABLE
# ============================================================

print("\n--- Tuple Immutability ---")

print("Original tuple:", fruits)

# The following operation is NOT allowed:
#
# fruits[0] = 'apple'
#
# It would produce:
# TypeError: 'tuple' object does not support item assignment


# ============================================================
# 7. CHANGING TUPLE TO LIST
# ============================================================

print("\n--- Tuple to List and Back ---")

fruits = ('banana', 'orange', 'mango', 'lemon')

# Convert tuple to list
fruits_list = list(fruits)

print("Tuple converted to list:", fruits_list)

# Modify the list
fruits_list[0] = 'apple'

print("Modified list:", fruits_list)

# Convert list back to tuple
fruits = tuple(fruits_list)

print("List converted back to tuple:", fruits)


# ============================================================
# 8. CHECKING ITEMS IN A TUPLE
# ============================================================

print("\n--- Checking Items ---")

print("'orange' in fruits:", 'orange' in fruits)
print("'apple' in fruits:", 'apple' in fruits)
print("'banana' not in fruits:", 'banana' not in fruits)


# ============================================================
# 9. JOINING TUPLES
# ============================================================

print("\n--- Joining Tuples ---")

fruits = ('banana', 'orange', 'mango', 'lemon')

vegetables = (
    'Tomato',
    'Potato',
    'Cabbage',
    'Onion',
    'Carrot'
)

# Join tuples using +
fruits_and_vegetables = fruits + vegetables

print("Fruits:", fruits)
print("Vegetables:", vegetables)
print("Fruits and vegetables:", fruits_and_vegetables)


# ============================================================
# 10. TUPLE REPETITION
# ============================================================

print("\n--- Tuple Repetition ---")

numbers = (1, 2, 3)

repeated_numbers = numbers * 3

print("Original tuple:", numbers)
print("Repeated tuple:", repeated_numbers)


# ============================================================
# 11. COUNT()
# ============================================================

print("\n--- count() ---")

numbers = (1, 2, 3, 2, 4, 2, 5)

print("Tuple:", numbers)
print("Number of times 2 occurs:", numbers.count(2))


# ============================================================
# 12. INDEX()
# ============================================================

print("\n--- index() ---")

fruits = ('banana', 'orange', 'mango', 'lemon')

print("Index of orange:", fruits.index('orange'))
print("Index of mango:", fruits.index('mango'))


# ============================================================
# 13. DELETING A TUPLE
# ============================================================

print("\n--- Deleting a Tuple ---")

temporary_tuple = ('Python', 'Java', 'C++')

print("Before deletion:", temporary_tuple)

del temporary_tuple

print("The tuple has been deleted.")

# The following would produce a NameError:
#
# print(temporary_tuple)


# ============================================================
# 14. NESTED TUPLES
# ============================================================

print("\n--- Nested Tuples ---")

student = (
    ('Snehankur', 'Mondal'),
    ('MCA', 'Python'),
    (2026, 2028)
)

print("Student information:", student)

print("Name:", student[0])
print("Course:", student[1])
print("Course name:", student[1][0])


# ============================================================
# 15. TUPLE UNPACKING
# ============================================================

print("\n--- Tuple Unpacking ---")

person = ('Snehankur', 'Mondal', 24)

first_name, last_name, age = person

print("First name:", first_name)
print("Last name:", last_name)
print("Age:", age)


# ============================================================
# 16. BUILT-IN FUNCTIONS WITH TUPLES
# ============================================================

print("\n--- Built-in Functions ---")

numbers = (10, 20, 30, 40, 50)

print("Tuple:", numbers)
print("Length:", len(numbers))
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Sum:", sum(numbers))


# ============================================================
# 17. CONVERTING LIST TO TUPLE
# ============================================================

print("\n--- List to Tuple ---")

languages = ['Python', 'Java', 'C++', 'JavaScript']

languages_tuple = tuple(languages)

print("Original list:", languages)
print("Converted tuple:", languages_tuple)


# ============================================================
# 18. TUPLE COMPARISON
# ============================================================

print("\n--- Tuple Comparison ---")

tuple_1 = (1, 2, 3)
tuple_2 = (1, 2, 3)
tuple_3 = (1, 2, 4)

print("tuple_1 == tuple_2:", tuple_1 == tuple_2)
print("tuple_1 == tuple_3:", tuple_1 == tuple_3)


# ============================================================
# END OF DAY 6
# ============================================================

print("\n========================================")
print("Day 6 - Tuples completed!")
print("========================================")