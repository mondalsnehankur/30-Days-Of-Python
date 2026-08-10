# Python Lists

A beginner-friendly Python program demonstrating the fundamentals of **lists**, including creating, accessing, modifying, slicing, searching, adding, removing, copying, combining, sorting, and reversing list elements.

## 📌 Overview

Lists are one of the most commonly used data structures in Python. They are **ordered, mutable collections** that can store multiple values, including values of different data types.

This project provides practical examples of Python list operations using examples such as fruits, vegetables, countries, web technologies, numbers, and ages.

---

## ✨ Topics Covered

* Creating lists
* Empty lists
* Finding list length
* Accessing list elements
* Positive and negative indexing
* List slicing
* Modifying list elements
* Checking membership
* Adding elements
* Removing elements
* Copying lists
* Combining lists
* Extending lists
* Counting elements
* Finding element indexes
* Reversing lists
* Sorting lists

---

## 1. Creating Lists

A list can be created by placing elements inside square brackets `[]`.

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
```

An empty list can be created using:

```python
empty_list = list()
```

or:

```python
empty_list = []
```

---

## 2. Finding the Length of a List

The built-in `len()` function returns the number of elements in a list.

```python
fruits = ['banana', 'orange', 'mango', 'lemon']

print(len(fruits))
```

Output:

```text
4
```

---

## 3. Accessing List Elements

List elements can be accessed using their index.

```python
fruits = ['banana', 'orange', 'mango', 'lemon']

print(fruits[0])  # banana
print(fruits[1])  # orange
print(fruits[3])  # lemon
```

Python uses **zero-based indexing**, meaning the first element has index `0`.

| Index | Element |
| ----: | ------- |
|   `0` | banana  |
|   `1` | orange  |
|   `2` | mango   |
|   `3` | lemon   |

---

## 4. Negative Indexing

Negative indexes allow elements to be accessed from the end of the list.

```python
print(fruits[-1])  # lemon
print(fruits[-2])  # mango
```

Here:

* `-1` → Last element
* `-2` → Second-last element
* `-3` → Third-last element

---

## 5. List Slicing

Slicing extracts a portion of a list.

```python
fruits = ['banana', 'orange', 'mango', 'lemon']

print(fruits[0:4])
print(fruits[1:3])
print(fruits[1:])
```

The ending index is **not included**.

For example:

```python
fruits[1:3]
```

returns:

```text
['orange', 'mango']
```

---

## 6. Modifying List Elements

Lists are **mutable**, meaning their elements can be changed after creation.

```python
fruits = ['banana', 'orange', 'mango', 'lemon']

fruits[0] = 'avocado'
fruits[1] = 'apple'

print(fruits)
```

Output:

```text
['avocado', 'apple', 'mango', 'lemon']
```

> **Important:** To replace the last element, use `len(fruits) - 1` as the last valid index. Using `len(fruits)` causes an `IndexError`.

Correct:

```python
fruits[len(fruits) - 1] = 'lime'
```

---

## 7. Checking Membership

The `in` operator checks whether an element exists in a list.

```python
fruits = ['banana', 'orange', 'mango', 'lemon']

print('banana' in fruits)  # True
print('lime' in fruits)    # False
```

---

# 🔧 List Methods

## 8. `append()`

Adds a single element to the end of a list.

```python
fruits.append('apple')
```

Result:

```text
['banana', 'orange', 'mango', 'lemon', 'apple']
```

---

## 9. `insert()`

Adds an element at a specific index.

```python
fruits.insert(2, 'apple')
```

Result:

```text
['banana', 'orange', 'apple', 'mango', 'lemon']
```

### ⚠️ Correction in the Original Code

The following is incorrect:

```python
fruits.list(3, 'lime')
```

Python lists do not have a `list()` method.

The correct method is:

```python
fruits.insert(3, 'lime')
```

---

## 10. `remove()`

Removes the first occurrence of a specified value.

```python
fruits.remove('banana')
```

---

## 11. `pop()`

`pop()` removes and returns an element by index. If no index is provided, it removes the last element.

```python
fruits = ['banana', 'orange', 'mango', 'lemon']

fruits.pop()
```

Result:

```text
['banana', 'orange', 'mango']
```

To remove an element at a specific index:

```python
fruits.pop(0)
```

### ⚠️ Correction in the Original Code

The original code uses:

```python
fruits.remove()
fruits.remove(0)
```

These are incorrect for demonstrating `pop()`.

The correct code is:

```python
fruits.pop()
fruits.pop(0)
```

---

## 12. `del`

The `del` statement can remove an element using its index.

```python
del fruits[0]
```

It can also delete the entire list:

```python
del fruits
```

After deleting the list, attempting to access `fruits` results in:

```text
NameError
```

---

## 13. `clear()`

Removes all elements from a list while keeping the list itself.

```python
fruits = ['banana', 'orange', 'mango', 'lemon']

fruits.clear()

print(fruits)
```

Output:

```text
[]
```

---

## 14. `copy()`

Creates a copy of a list.

```python
fruits_copy = fruits.copy()
```

This is useful when you want a separate list rather than another reference to the same list.

---

## 15. Combining Lists with `+`

Two or more lists can be combined using the `+` operator.

```python
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5, -4, -3, -2, -1]

integers = negative_numbers + zero + positive_numbers
```

Result:

```text
[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
```

---

## 16. `extend()`

The `extend()` method adds all elements from another iterable to the existing list.

```python
num1 = [0, 1, 2, 3]
num2 = [4, 5, 6]

num1.extend(num2)
```

Result:

```text
[0, 1, 2, 3, 4, 5, 6]
```

### `+` vs `extend()`

| Operation             | Effect                      |
| --------------------- | --------------------------- |
| `list1 + list2`       | Creates a new combined list |
| `list1.extend(list2)` | Modifies `list1`            |

---

## 17. `count()`

Returns the number of times a particular element occurs.

```python
ages = [22, 19, 24, 25, 26, 24, 25, 24]

print(ages.count(24))
```

Output:

```text
3
```

---

## 18. `index()`

Returns the index of the first occurrence of an element.

```python
fruits = ['banana', 'orange', 'mango', 'lemon']

print(fruits.index('orange'))
```

Output:

```text
1
```

---

## 19. `reverse()`

Reverses the elements of a list **in place**.

```python
fruits = ['banana', 'orange', 'mango', 'lemon']

fruits.reverse()

print(fruits)
```

Result:

```text
['lemon', 'mango', 'orange', 'banana']
```

### ⚠️ Important

`reverse()` modifies the list and returns `None`.

Therefore, this:

```python
print(fruits.reverse())
```

prints:

```text
None
```

Instead, use:

```python
fruits.reverse()
print(fruits)
```

---

## 20. `sort()`

The `sort()` method sorts a list in ascending order.

```python
ages = [22, 19, 24, 25, 26, 24, 25, 24]

ages.sort()

print(ages)
```

To sort in descending order:

```python
ages.sort(reverse=True)
```

Example:

```text
Ascending:
[19, 22, 24, 24, 24, 25, 25, 26]

Descending:
[26, 25, 25, 24, 24, 24, 22, 19]
```

---

# 📊 List Methods Summary

| Method / Operator | Purpose                               |
| ----------------- | ------------------------------------- |
| `len()`           | Returns number of elements            |
| `append()`        | Adds an element to the end            |
| `insert()`        | Adds an element at a specific index   |
| `remove()`        | Removes a specific value              |
| `pop()`           | Removes and returns an element        |
| `del`             | Deletes an element or the entire list |
| `clear()`         | Removes all elements                  |
| `copy()`          | Creates a copy                        |
| `+`               | Combines lists                        |
| `extend()`        | Adds elements from another iterable   |
| `count()`         | Counts occurrences                    |
| `index()`         | Finds the first index                 |
| `reverse()`       | Reverses the list in place            |
| `sort()`          | Sorts the list                        |

---

## 🧠 Key Characteristics of Python Lists

Python lists are:

* **Ordered** — elements maintain their position.
* **Mutable** — elements can be changed.
* **Indexed** — elements can be accessed using indexes.
* **Allow duplicates** — the same value can occur multiple times.
* **Heterogeneous** — a list can contain different data types.

Example:

```python
example = [10, 'Python', 3.14, True]
```

---

## 📂 Project Structure

```text
Python-Lists/
│
├── lists.py
└── README.md
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/python-lists.git
```

### 2. Navigate to the project directory

```bash
cd python-lists
```

### 3. Run the Python program

```bash
python lists.py
```

---

## 📚 Learning Outcomes

After completing this program, you should understand:

* How to create Python lists
* How Python list indexing works
* How to use positive and negative indexes
* How to slice lists
* How to modify list elements
* How to add and remove elements
* How to combine and copy lists
* How to search lists
* How to reverse and sort lists
* The difference between `append()`, `insert()`, `remove()`, `pop()`, and `extend()`

---

## 🛠 Requirements

* Python 3.x
* No external libraries required

---

## 🎯 Suitable For

* Python beginners
* Students learning data structures
* Python programming practice
* LeetCode and DSA preparation
* Building a foundation for more advanced Python concepts

---

## 📄 License

This project is open-source and intended for educational and learning purposes.
