# ============================================================

# 30 DAYS OF PYTHON

# DAY 7: SETS

# ============================================================

# A set is an unordered collection of unique elements.

# Sets do not support indexing because they are unordered.

# ============================================================

# 1. CREATING A SET

# ============================================================

# Creating an empty set

empty_set = set()
print("Empty set:", empty_set)

# Creating a set with initial values

fruits = {'banana', 'orange', 'mango', 'lemon'}
print("Fruits:", fruits)

# Duplicate elements are automatically removed

numbers = {1, 2, 2, 3, 3, 4, 5}
print("Set with duplicates removed:", numbers)

# ============================================================

# 2. GETTING SET'S LENGTH

# ============================================================

print("Number of fruits:", len(fruits))

# ============================================================

# 3. ACCESSING ITEMS IN A SET

# ============================================================

# Sets are unordered and unindexed.

# Therefore, we use a loop to access their elements.

print("\nItems in the fruits set:")

for fruit in fruits:
print(fruit)

# ============================================================

# 4. CHECKING AN ITEM

# ============================================================

print("\nChecking items:")

print("Is mango in fruits?", 'mango' in fruits)
print("Is apple in fruits?", 'apple' in fruits)

# ============================================================

# 5. ADDING ITEMS TO A SET

# ============================================================

# add() adds a single item

fruits.add('lime')

print("\nAfter adding lime:")
print(fruits)

# update() adds multiple items

vegetables = {
'tomato',
'potato',
'cabbage',
'onion',
'carrot'
}

fruits.update(vegetables)

print("\nAfter update():")
print(fruits)

# ============================================================

# 6. REMOVING ITEMS FROM A SET

# ============================================================

fruits = {'banana', 'orange', 'mango', 'lemon'}

# remove() removes a specific item.

# It raises KeyError if the item does not exist.

fruits.remove('banana')

print("\nAfter remove('banana'):")
print(fruits)

# discard() removes an item if it exists.

# It does not raise an error if the item is absent.

fruits.discard('apple')

print("\nAfter discard('apple'):")
print(fruits)

# pop() removes and returns an arbitrary item

removed_item = fruits.pop()

print("\nItem removed using pop():", removed_item)
print("Set after pop():", fruits)

# ============================================================

# 7. CLEARING ITEMS IN A SET

# ============================================================

fruits = {'banana', 'orange', 'mango', 'lemon'}

fruits.clear()

print("\nAfter clear():")
print(fruits)

# ============================================================

# 8. DELETING A SET

# ============================================================

fruits = {'banana', 'orange', 'mango', 'lemon'}

del fruits

print("\nThe fruits set has been deleted.")

# Uncomment the following line to see NameError:

# print(fruits)

# ============================================================

# 9. CONVERTING LIST TO SET

# ============================================================

fruits_list = [
'banana',
'orange',
'mango',
'lemon',
'orange',
'banana'
]

print("\nOriginal list:")
print(fruits_list)

fruits_set = set(fruits_list)

print("Converted set:")
print(fruits_set)

# ============================================================

# 10. JOINING SETS - UNION

# ============================================================

fruits = {
'banana',
'orange',
'mango',
'lemon'
}

vegetables = {
'tomato',
'potato',
'cabbage',
'onion',
'carrot'
}

# Using union()

all_food = fruits.union(vegetables)

print("\nUnion using union():")
print(all_food)

# Using | operator

all_food = fruits | vegetables

print("\nUnion using |:")
print(all_food)

# ============================================================

# 11. UPDATE

# ============================================================

fruits = {
'banana',
'orange',
'mango',
'lemon'
}

vegetables = {
'tomato',
'potato',
'cabbage',
'onion',
'carrot'
}

fruits.update(vegetables)

print("\nAfter update():")
print(fruits)

# ============================================================

# 12. FINDING INTERSECTION ITEMS

# ============================================================

whole_numbers = {
0, 1, 2, 3, 4,
5, 6, 7, 8, 9, 10
}

even_numbers = {
0, 2, 4, 6, 8, 10
}

# Using intersection()

common_numbers = whole_numbers.intersection(even_numbers)

print("\nIntersection using intersection():")
print(common_numbers)

# Using & operator

common_numbers = whole_numbers & even_numbers

print("\nIntersection using &:")
print(common_numbers)

# Example using words

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}

print("\nCommon letters:")
print(python.intersection(dragon))

# ============================================================

# 13. CHECKING SUBSET

# ============================================================

whole_numbers = {
0, 1, 2, 3, 4,
5, 6, 7, 8, 9, 10
}

even_numbers = {
0, 2, 4, 6, 8, 10
}

print("\nIs even_numbers a subset of whole_numbers?")
print(even_numbers.issubset(whole_numbers))

# Using <= operator

print("Using <=:", even_numbers <= whole_numbers)

# ============================================================

# 14. CHECKING SUPERSET

# ============================================================

print("\nIs whole_numbers a superset of even_numbers?")
print(whole_numbers.issuperset(even_numbers))

# Using >= operator

print("Using >=:", whole_numbers >= even_numbers)

# ============================================================

# 15. DIFFERENCE BETWEEN TWO SETS

# ============================================================

whole_numbers = {
0, 1, 2, 3, 4,
5, 6, 7, 8, 9, 10
}

even_numbers = {
0, 2, 4, 6, 8, 10
}

difference = whole_numbers.difference(even_numbers)

print("\nWhole numbers - even numbers:")
print(difference)

# Using - operator

difference = whole_numbers - even_numbers

print("Using - operator:")
print(difference)

# Reverse difference

print("\nEven numbers - whole numbers:")
print(even_numbers - whole_numbers)

# Example using words

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}

print("\nPython - Dragon:")
print(python - dragon)

print("Dragon - Python:")
print(dragon - python)

# ============================================================

# 16. SYMMETRIC DIFFERENCE

# ============================================================

whole_numbers = {
0, 1, 2, 3, 4,
5, 6, 7, 8, 9, 10
}

some_numbers = {
1, 2, 3, 4, 5
}

# Using symmetric_difference()

result = whole_numbers.symmetric_difference(some_numbers)

print("\nSymmetric difference:")
print(result)

# Using ^ operator

result = whole_numbers ^ some_numbers

print("Using ^ operator:")
print(result)

# Example using words

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}

print("\nPython ^ Dragon:")
print(python ^ dragon)

# ============================================================

# 17. CHECKING DISJOINT SETS

# ============================================================

even_numbers = {
0, 2, 4, 6, 8
}

odd_numbers = {
1, 3, 5, 7, 9
}

print("\nAre even and odd numbers disjoint?")
print(even_numbers.isdisjoint(odd_numbers))

# Sets with common elements

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}

print("\nAre Python and Dragon disjoint?")
print(python.isdisjoint(dragon))

# ============================================================

# 18. PRACTICAL EXAMPLE

# ============================================================

python_students = {
'Snehankur',
'Rahul',
'Ankit',
'Priya',
'Neha'
}

java_students = {
'Rahul',
'Ankit',
'Riya',
'Neha'
}

print("\n================================")
print("STUDENT COURSE ANALYSIS")
print("================================")

# Students in either course

print("\nStudents in either Python or Java:")
print(python_students | java_students)

# Students in both courses

print("\nStudents in both Python and Java:")
print(python_students & java_students)

# Students only in Python

print("\nStudents only in Python:")
print(python_students - java_students)

# Students only in Java

print("\nStudents only in Java:")
print(java_students - python_students)

# Students in exactly one course

print("\nStudents in exactly one course:")
print(python_students ^ java_students)

# Subset check

print("\nAre Java students a subset of Python students?")
print(java_students.issubset(python_students))

# Superset check

print("\nAre Python students a superset of Java students?")
print(python_students.issuperset(java_students))

# Disjoint check

print("\nAre Python and Java students disjoint?")
print(python_students.isdisjoint(java_students))

# ============================================================

# END OF DAY 7

# ============================================================

print("\n================================")
print("Day 7 - Sets Completed!")
print("================================")
