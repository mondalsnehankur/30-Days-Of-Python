# Day 6: Tuples

Part of my **30 Days of Python** learning journey.

This day focuses on **tuples**, one of Python's built-in collection data types. The program covers tuple creation, indexing, slicing, immutability, conversion between tuples and lists, joining tuples, tuple methods, unpacking, nested tuples, and useful built-in functions.

---

## 📌 Table of Contents

* [Overview](#-overview)
* [What is a Tuple?](#-what-is-a-tuple)
* [Topics Covered](#-topics-covered)

  * [Creating a Tuple](#1-creating-a-tuple)
  * [Tuple Length](#2-tuple-length)
  * [Accessing Tuple Items](#3-accessing-tuple-items)
  * [Negative Indexing](#4-negative-indexing)
  * [Slicing Tuples](#5-slicing-tuples)
  * [Tuple Immutability](#6-tuple-immutability)
  * [Tuple to List Conversion](#7-changing-tuples-to-lists)
  * [Checking Items](#8-checking-an-item-in-a-tuple)
  * [Joining Tuples](#9-joining-tuples)
  * [Tuple Repetition](#10-tuple-repetition)
  * [`count()`](#11-count)
  * [`index()`](#12-index)
  * [Deleting Tuples](#13-deleting-tuples)
  * [Nested Tuples](#14-nested-tuples)
  * [Tuple Unpacking](#15-tuple-unpacking)
  * [Built-in Functions](#16-built-in-functions-with-tuples)
  * [List to Tuple Conversion](#17-list-to-tuple-conversion)
  * [Tuple Comparison](#18-tuple-comparison)
* [Tuple Methods](#-tuple-methods)
* [Tuple vs List](#-tuple-vs-list)
* [Project Structure](#-project-structure)
* [How to Run](#-how-to-run)
* [Learning Outcomes](#-learning-outcomes)

---

## 🔎 Overview

A **tuple** is an ordered collection of elements that is **immutable**, meaning its elements cannot be changed after the tuple is created.

Tuples are written using parentheses:

```python
fruits = ('banana', 'orange', 'mango', 'lemon')
```

Unlike lists, tuples do not support operations such as:

```python
append()
insert()
remove()
```

and individual elements cannot be reassigned.

---

# 📚 Topics Covered

## 1. Creating a Tuple

An empty tuple can be created using either:

```python
empty_tuple = ()
```

or:

```python
empty_tuple = tuple()
```

A tuple with values:

```python
fruits = ('banana', 'orange', 'mango', 'lemon')
```

A tuple can also contain different data types:

```python
mixed_tuple = ('Python', 30, 3.14, True)
```

### Single-item Tuple

A single-item tuple requires a trailing comma:

```python
single_item = ('Python',)
```

Without the comma:

```python
single_item = ('Python')
```

this is simply a string, not a tuple.

---

## 2. Tuple Length

The `len()` function returns the number of elements.

```python
fruits = ('banana', 'orange', 'mango', 'lemon')

print(len(fruits))
```

Output:

```text
4
```

---

## 3. Accessing Tuple Items

Tuples use **zero-based indexing**, just like lists.

```python
fruits = ('banana', 'orange', 'mango', 'lemon')

print(fruits[0])
print(fruits[1])
```

Output:

```text
banana
orange
```

The last element can also be accessed using:

```python
fruits[len(fruits) - 1]
```

---

## 4. Negative Indexing

Negative indexing starts from the end of the tuple.

```python
fruits = ('banana', 'orange', 'mango', 'lemon')

print(fruits[-1])
print(fruits[-2])
```

Output:

```text
lemon
mango
```

| Index | Element |
| ----: | ------- |
|  `-1` | lemon   |
|  `-2` | mango   |
|  `-3` | orange  |
|  `-4` | banana  |

---

## 5. Slicing Tuples

Tuples support slicing using:

```text
tuple[start:stop]
```

The `stop` index is excluded.

```python
fruits = ('banana', 'orange', 'mango', 'lemon')

print(fruits[1:3])
```

Output:

```text
('orange', 'mango')
```

Other examples:

```python
print(fruits[0:])
print(fruits[1:])
print(fruits[-4:])
print(fruits[-3:-1])
print(fruits[-3:])
```

---

## 6. Tuple Immutability

The most important characteristic of a tuple is that it is **immutable**.

This means the following is invalid:

```python
fruits = ('banana', 'orange', 'mango', 'lemon')

fruits[0] = 'apple'
```

It produces:

```text
TypeError: 'tuple' object does not support item assignment
```

You cannot directly modify an existing tuple.

---

## 7. Changing Tuples to Lists

If a tuple needs to be modified, it can temporarily be converted into a list.

```python
fruits = ('banana', 'orange', 'mango', 'lemon')

fruits = list(fruits)

fruits[0] = 'apple'

fruits = tuple(fruits)
```

The result is:

```python
('apple', 'orange', 'mango', 'lemon')
```

This demonstrates the relationship between mutable lists and immutable tuples.

---

## 8. Checking an Item in a Tuple

The `in` operator checks whether an item exists.

```python
fruits = ('banana', 'orange', 'mango', 'lemon')

print('orange' in fruits)
print('apple' in fruits)
```

Output:

```text
True
False
```

The `not in` operator can also be used:

```python
print('apple' not in fruits)
```

---

## 9. Joining Tuples

Two or more tuples can be combined using the `+` operator.

```python
fruits = ('banana', 'orange', 'mango', 'lemon')

vegetables = (
    'Tomato',
    'Potato',
    'Cabbage',
    'Onion',
    'Carrot'
)

fruits_and_vegetables = fruits + vegetables
```

Result:

```text
('banana', 'orange', 'mango', 'lemon',
 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
```

---

## 10. Tuple Repetition

The `*` operator can repeat the contents of a tuple.

```python
numbers = (1, 2, 3)

print(numbers * 3)
```

Output:

```text
(1, 2, 3, 1, 2, 3, 1, 2, 3)
```

---

## 11. `count()`

The `count()` method returns the number of times an item occurs.

```python
numbers = (1, 2, 3, 2, 4, 2, 5)

print(numbers.count(2))
```

Output:

```text
3
```

---

## 12. `index()`

The `index()` method returns the index of the first occurrence of an item.

```python
fruits = ('banana', 'orange', 'mango', 'lemon')

print(fruits.index('orange'))
```

Output:

```text
1
```

---

## 13. Deleting Tuples

Individual elements cannot be deleted from a tuple.

However, the entire tuple can be deleted using `del`.

```python
fruits = ('banana', 'orange', 'mango', 'lemon')

del fruits
```

After deletion, attempting to access `fruits` produces a `NameError`.

---

## 14. Nested Tuples

Tuples can contain other tuples.

```python
student = (
    ('Snehankur', 'Mondal'),
    ('MCA', 'Python'),
    (2026, 2028)
)
```

Nested elements can be accessed using multiple indexes:

```python
print(student[0])
print(student[1][0])
```

---

## 15. Tuple Unpacking

Tuple unpacking allows the individual elements of a tuple to be assigned to variables.

```python
person = ('Snehankur', 'Mondal', 24)

first_name, last_name, age = person
```

Now:

```text
first_name → Snehankur
last_name  → Mondal
age        → 24
```

The number of variables must normally match the number of elements being unpacked.

---

## 16. Built-in Functions with Tuples

Several Python built-in functions work with tuples.

```python
numbers = (10, 20, 30, 40, 50)

print(len(numbers))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
```

Output:

```text
5
10
50
150
```

---

## 17. List to Tuple Conversion

A list can be converted into a tuple using `tuple()`.

```python
languages = ['Python', 'Java', 'C++', 'JavaScript']

languages_tuple = tuple(languages)
```

Result:

```text
('Python', 'Java', 'C++', 'JavaScript')
```

---

## 18. Tuple Comparison

Tuples can be compared using standard comparison operators.

```python
tuple_1 = (1, 2, 3)
tuple_2 = (1, 2, 3)
tuple_3 = (1, 2, 4)

print(tuple_1 == tuple_2)
print(tuple_1 == tuple_3)
```

Output:

```text
True
False
```

---

# 🔧 Tuple Methods

Tuples intentionally have fewer methods than lists because they are immutable.

| Method    | Description                               |
| --------- | ----------------------------------------- |
| `count()` | Counts occurrences of an item             |
| `index()` | Returns the index of the first occurrence |

Useful built-in functions include:

| Function  | Purpose                           |
| --------- | --------------------------------- |
| `len()`   | Returns tuple length              |
| `min()`   | Returns smallest value            |
| `max()`   | Returns largest value             |
| `sum()`   | Returns sum of numeric values     |
| `tuple()` | Converts an iterable into a tuple |

---

# ⚖️ Tuple vs List

| Feature                       | List | Tuple |
| ----------------------------- | ---- | ----- |
| Syntax                        | `[]` | `()`  |
| Ordered                       | ✅    | ✅     |
| Mutable                       | ✅    | ❌     |
| Allows duplicates             | ✅    | ✅     |
| Indexing                      | ✅    | ✅     |
| Slicing                       | ✅    | ✅     |
| `append()`                    | ✅    | ❌     |
| `remove()`                    | ✅    | ❌     |
| `insert()`                    | ✅    | ❌     |
| `count()`                     | ✅    | ✅     |
| `index()`                     | ✅    | ✅     |
| Can be used as dictionary key | ❌*   | ✅*    |

* A tuple can be hashable and used as a dictionary key if all of its elements are hashable.

### When should you use a tuple?

Use a tuple when:

* The collection should not be modified.
* You want to represent fixed data.
* You want to communicate that the data is immutable.
* You need a hashable collection for use as a dictionary key or set element.

---

# 📂 Project Structure

```text
06_Day_Tuples/
│
├── tuples.py
└── README.md
```

---

# ▶️ How to Run

Make sure Python 3 is installed.

Run:

```bash
python tuples.py
```

No external libraries are required.

---

# 🧠 Learning Outcomes

After completing Day 6, you should be able to:

* Create empty and non-empty tuples.
* Understand tuple immutability.
* Find the length of a tuple.
* Access tuple elements using positive indexes.
* Use negative indexing.
* Slice tuples.
* Check whether an element exists.
* Join multiple tuples.
* Repeat tuples.
* Use `count()` and `index()`.
* Convert tuples to lists and lists to tuples.
* Delete an entire tuple.
* Work with nested tuples.
* Unpack tuple elements.
* Use built-in functions such as `len()`, `min()`, `max()`, and `sum()`.

---

# 💻 Exercises

The original Day 6 challenge also contains exercises. These can be maintained separately from the concept demonstrations.

## Level 1

Suggested exercises:

1. Create an empty tuple.
2. Create a tuple containing names of your sisters and brothers.
3. Join the brothers and sisters tuples and assign the result to `siblings`.
4. Find the number of siblings.
5. Add the names of your father and mother to the tuple and assign it to `family_members`.
6. Unpack the family tuple into individual variables.
7. Create tuples representing `fruits`, `vegetables`, and `animal_products`.
8. Join the three tuples and assign the result to `food_stuff_tp`.
9. Convert `food_stuff_tp` into a list.
10. Slice out the middle item or items.
11. Slice out the first three items.
12. Slice out the last three items.
13. Delete `food_stuff_tp`.
14. Check whether an item exists in a tuple using `in`.

---

## Level 2

Suggested exercises:

1. Create a tuple containing the names of cities you would like to visit.
2. Find the length of the tuple.
3. Access the first and last cities.
4. Check whether a particular city exists in the tuple.
5. Convert the tuple to a list.
6. Modify the list.
7. Convert the list back to a tuple.
8. Practice tuple unpacking.
9. Create a nested tuple and access its elements.
10. Practice `count()` and `index()`.

---

# 📝 Notes

The main difference between lists and tuples is **mutability**:

```python
# List - mutable
numbers = [1, 2, 3]
numbers[0] = 10

# Tuple - immutable
numbers = (1, 2, 3)

# numbers[0] = 10  # TypeError
```

A tuple does not become mutable simply because it contains mutable objects. For example:

```python
data = ([1, 2], [3, 4])

data[0].append(5)

print(data)
```

This is valid because the tuple itself has not been changed; the list stored inside it has been modified.

---

## 🛠 Requirements

* Python 3.x
* No external libraries

---

## 🎯 Purpose

This project is part of my **30 Days of Python** challenge and is intended to build a strong foundation in Python data structures before moving on to more advanced concepts.

---

## 📄 License

This project is intended for educational and learning purposes.

---

**Day 6 completed — Tuples. 🐍**
