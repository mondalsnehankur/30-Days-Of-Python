# 📘 30 Days of Python

## Day 8: Dictionaries

This repository is a **30 Days of Python** learning journey.
**Day 8** focuses on **Dictionaries in Python** and covers their creation, accessing and modifying elements, adding and removing items, copying, iterating, and working with dictionary methods.

---

## 📌 Topics Covered

* Creating a Dictionary
* Creating Dictionaries with Different Data Types
* Finding Dictionary Length
* Accessing Dictionary Items
* Using `get()` to Access Values Safely
* Adding Items to a Dictionary
* Modifying Dictionary Items
* Checking Whether a Key Exists
* Removing Key-Value Pairs
* Converting Dictionary Items to a List
* Clearing a Dictionary
* Deleting a Dictionary
* Copying a Dictionary
* Getting Dictionary Keys
* Getting Dictionary Values
* Iterating Through Dictionary Keys
* Iterating Through Dictionary Values
* Iterating Through Key-Value Pairs
* Working with Nested Dictionaries
* Working with Lists Inside Dictionaries
* Complete Student Dictionary Example

---

## 🧠 What is a Dictionary?

A **dictionary** in Python is a collection of data stored in **key-value pairs**.

Each value is associated with a unique key, allowing data to be accessed using the key instead of an index.

### Basic Syntax

```python
dictionary = {
    "key": "value"
}
```

### Example

```python
person = {
    "name": "Snehankur",
    "age": 24,
    "country": "India"
}
```

Here:

* `"name"`, `"age"`, and `"country"` are **keys**
* `"Snehankur"`, `24`, and `"India"` are **values**

---

# 📂 Code Structure

The Day 8 program is divided into the following sections:

```text
Day 8 - Dictionaries
│
├── 1. Creating a Dictionary
├── 2. Creating a Dictionary with Different Data Types
├── 3. Dictionary Length
├── 4. Accessing Dictionary Items
├── 5. Adding Items
├── 6. Modifying Items
├── 7. Checking Keys
├── 8. Removing Key-Value Pairs
├── 9. Dictionary to List
├── 10. Clearing a Dictionary
├── 11. Deleting a Dictionary
├── 12. Copying a Dictionary
├── 13. Getting Dictionary Keys
├── 14. Getting Dictionary Values
├── 15. Iterating Through Keys
├── 16. Iterating Through Values
├── 17. Iterating Through Key-Value Pairs
└── 18. Complete Dictionary Example
```

---

# 1. Creating a Dictionary

An empty dictionary can be created using `{}`.

```python
empty_dict = {}

print(empty_dict)
```

A dictionary can also be created with initial key-value pairs:

```python
dct = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}
```

Another way is to use the `dict()` constructor:

```python
another_dict = dict(
    name="Snehankur",
    age=24,
    country="India"
)
```

### Output

```text
Empty Dictionary: {}
Dictionary: {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
Dictionary using dict(): {'name': 'Snehankur', 'age': 24, 'country': 'India'}
```

---

# 2. Dictionary with Different Data Types

Python dictionaries can contain different types of values.

A value can be:

* String
* Integer
* Boolean
* List
* Another dictionary
* And other Python objects

Example:

```python
person = {
    "first_name": "Asabeneh",
    "last_name": "Yetayeh",
    "age": 250,
    "country": "Finland",
    "is_married": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {
        "street": "Space street",
        "zipcode": "02210"
    }
}
```

This example also demonstrates **nested data structures**.

The `address` value is itself a dictionary, while `skills` contains a list.

---

# 3. Dictionary Length

The `len()` function returns the number of key-value pairs in a dictionary.

```python
print(len(dct))
print(len(person))
```

For example:

```python
student = {
    "name": "Snehankur",
    "age": 24,
    "course": "MCA"
}

print(len(student))
```

### Output

```text
3
```

---

# 4. Accessing Dictionary Items

Dictionary values can be accessed using their keys.

```python
print(person["first_name"])
print(person["country"])
```

Unlike lists, dictionaries are not accessed using numeric indexes. Instead, the associated key is used.

### Accessing Nested Values

For a dictionary containing a list:

```python
print(person["skills"][0])
```

For a dictionary inside another dictionary:

```python
print(person["address"]["street"])
```

---

## Using `get()`

The `get()` method provides another way to access dictionary values.

```python
print(person.get("first_name"))
```

One important advantage of `get()` is that it does not raise a `KeyError` when the key does not exist.

```python
print(person.get("city"))
```

### Output

```text
None
```

This makes `get()` useful when working with optional or uncertain keys.

---

# 5. Adding Items to a Dictionary

A new key-value pair can be added simply by assigning a value to a new key.

```python
person["job_title"] = "Instructor"
person["city"] = "Helsinki"
```

The dictionary is automatically updated.

### Adding to a List Inside a Dictionary

Since `skills` is a list, normal list methods can be used:

```python
person["skills"].append("HTML")
```

This adds `"HTML"` to the existing skills list.

---

# 6. Modifying Dictionary Items

Existing values can be modified by assigning a new value to an existing key.

```python
person["first_name"] = "Eyob"
person["age"] = 252
person["country"] = "Ethiopia"
```

The keys remain the same, but their associated values change.

---

# 7. Checking Keys in a Dictionary

The `in` operator can be used to check whether a key exists.

```python
print("first_name" in person)
print("country" in person)
print("salary" in person)
```

### Example Output

```text
True
True
False
```

This is useful when you need to check for a key before accessing its value.

---

# 8. Removing Key-Value Pairs

Python provides several ways to remove dictionary items.

## `pop()`

`pop()` removes a specific key and returns its value.

```python
removed_value = remove_demo.pop("first_name")
```

The removed value can then be stored in a variable.

---

## `popitem()`

`popitem()` removes and returns the **last inserted key-value pair**.

```python
removed_item = remove_demo.popitem()
```

The returned value is a tuple containing the key and value.

Example:

```text
('is_married', True)
```

---

## `del`

The `del` statement can remove a specific key-value pair.

```python
del remove_demo["age"]
```

Unlike `pop()`, `del` does not return the removed value.

---

# 9. Converting Dictionary Items to a List

The `items()` method returns a view containing the dictionary's key-value pairs.

```python
items = items_demo.items()
```

It can be converted into an actual list:

```python
items_list = list(items)
```

### Example

```python
items_demo = {
    "name": "Snehankur",
    "age": 24,
    "country": "India"
}

print(list(items_demo.items()))
```

### Output

```text
[('name', 'Snehankur'), ('age', 24), ('country', 'India')]
```

Each dictionary item is represented as a tuple:

```text
(key, value)
```

---

# 10. Clearing a Dictionary

The `clear()` method removes all items from a dictionary while keeping the dictionary itself.

```python
clear_demo.clear()
```

Before:

```python
{
    "name": "Snehankur",
    "age": 24,
    "country": "India"
}
```

After:

```python
{}
```

---

# 11. Deleting a Dictionary

The `del` statement can also be used to delete the entire dictionary.

```python
del delete_demo
```

After deletion, the variable `delete_demo` no longer exists.

Attempting to access it afterward will result in a `NameError`.

---

# 12. Copying a Dictionary

The `copy()` method creates a copy of a dictionary.

```python
original_dict = {
    "name": "Snehankur",
    "age": 24,
    "country": "India"
}

copied_dict = original_dict.copy()
```

The copied dictionary can be modified independently for this simple example:

```python
copied_dict["age"] = 25
```

The original dictionary remains:

```text
{'name': 'Snehankur', 'age': 24, 'country': 'India'}
```

while the copied dictionary becomes:

```text
{'name': 'Snehankur', 'age': 25, 'country': 'India'}
```

> **Note:** `copy()` performs a **shallow copy**. If a dictionary contains mutable nested objects such as lists or dictionaries, changes to those nested objects can still be shared between the copies.

---

# 13. Getting Dictionary Keys

The `keys()` method returns a view containing all dictionary keys.

```python
keys = keys_demo.keys()
```

It can be converted into a list:

```python
keys_list = list(keys)
```

Example:

```python
print(list(keys_demo.keys()))
```

### Output

```text
['name', 'age', 'country', 'course']
```

---

# 14. Getting Dictionary Values

The `values()` method returns a view containing all values.

```python
values = keys_demo.values()
```

It can also be converted into a list:

```python
values_list = list(values)
```

Example:

```python
print(list(keys_demo.values()))
```

### Output

```text
['Snehankur', 24, 'India', 'MCA']
```

---

# 15. Iterating Through Dictionary Keys

A dictionary can be directly iterated over using a `for` loop.

```python
for key in keys_demo:
    print(key)
```

By default, iterating over a dictionary iterates through its keys.

Equivalent form:

```python
for key in keys_demo.keys():
    print(key)
```

---

# 16. Iterating Through Dictionary Values

The `values()` method can be used to iterate through all values.

```python
for value in keys_demo.values():
    print(value)
```

This accesses only the values, not the keys.

---

# 17. Iterating Through Key-Value Pairs

The `items()` method is useful when both the key and value are required.

```python
for key, value in keys_demo.items():
    print(key, ":", value)
```

### Example Output

```text
name : Snehankur
age : 24
country : India
course : MCA
```

This is one of the most commonly used patterns when working with dictionaries.

---

# 18. Complete Dictionary Example

The final section combines several dictionary concepts into a practical **student record**.

```python
student = {
    "name": "Snehankur",
    "age": 24,
    "course": "MCA",
    "university": "Christ University",
    "skills": ["Python", "SQL", "HTML", "CSS"],
    "marks": {
        "Python": 90,
        "SQL": 85,
        "DBMS": 88
    }
}
```

This dictionary demonstrates:

* Strings
* Integers
* Lists
* Nested dictionaries
* Dictionary access
* List access
* Adding values
* Modifying values
* Checking keys
* `get()`
* `keys()`
* `values()`
* `items()`

---

## Accessing Student Information

```python
print(student["name"])
print(student["course"])
print(student["university"])
```

### Accessing a List

```python
print(student["skills"])
print(student["skills"][0])
```

### Accessing a Nested Dictionary

```python
print(student["marks"]["Python"])
```

This accesses the `"Python"` key inside the nested `"marks"` dictionary.

---

## Updating the Student Dictionary

A new skill can be added to the existing list:

```python
student["skills"].append("Java")
```

A new key-value pair can be added:

```python
student["semester"] = 1
```

An existing value can be modified:

```python
student["age"] = 25
```

---

## Checking Keys

```python
print("semester" in student)
print("address" in student)
```

Expected output:

```text
True
False
```

---

## Using `get()`

```python
print(student.get("name"))
print(student.get("address"))
```

Expected output:

```text
Snehankur
None
```

---

## Displaying Keys, Values, and Items

### Keys

```python
print(list(student.keys()))
```

### Values

```python
print(list(student.values()))
```

### Key-Value Pairs

```python
print(list(student.items()))
```

---

# 🔑 Important Dictionary Methods

| Method / Operation  | Purpose                           |
| ------------------- | --------------------------------- |
| `{}`                | Creates an empty dictionary       |
| `dict()`            | Creates a dictionary              |
| `len()`             | Returns number of key-value pairs |
| `dict[key]`         | Accesses a value                  |
| `get()`             | Safely accesses a value           |
| `dict[key] = value` | Adds or modifies an item          |
| `in`                | Checks whether a key exists       |
| `pop()`             | Removes a specified key           |
| `popitem()`         | Removes the last key-value pair   |
| `del`               | Deletes an item or dictionary     |
| `clear()`           | Removes all items                 |
| `copy()`            | Creates a shallow copy            |
| `keys()`            | Returns dictionary keys           |
| `values()`          | Returns dictionary values         |
| `items()`           | Returns key-value pairs           |

---

# ⚡ Quick Reference

### Create

```python
student = {
    "name": "Snehankur",
    "age": 24
}
```

### Access

```python
student["name"]
```

### Safe Access

```python
student.get("name")
```

### Add

```python
student["course"] = "MCA"
```

### Modify

```python
student["age"] = 25
```

### Check

```python
"name" in student
```

### Remove

```python
student.pop("age")
```

### Keys

```python
student.keys()
```

### Values

```python
student.values()
```

### Items

```python
student.items()
```

### Iterate

```python
for key, value in student.items():
    print(key, value)
```

### Clear

```python
student.clear()
```

### Copy

```python
new_student = student.copy()
```

---

# 🧩 Key Concepts Learned

By completing Day 8, the following concepts were practiced:

* Dictionaries store data using **key-value pairs**.
* Dictionary values can contain different Python data types.
* Dictionaries can contain **lists and nested dictionaries**.
* Dictionary values can be accessed using keys.
* `get()` provides safer access to potentially missing keys.
* New items can be added using assignment.
* Existing values can be modified using assignment.
* The `in` operator checks whether a key exists.
* `pop()`, `popitem()`, and `del` can remove dictionary data.
* `clear()` removes all dictionary contents.
* `copy()` creates a shallow copy.
* `keys()`, `values()`, and `items()` provide different views of dictionary data.
* Dictionaries can be easily traversed using `for` loops.

---

# ▶️ How to Run

Make sure Python is installed on your system.

Run the Day 8 program using:

```bash
python day_08_dictionaries.py
```

If your system uses `python3`:

```bash
python3 day_08_dictionaries.py
```

---

# 📁 Suggested Repository Structure

```text
30-Days-of-Python/
│
├── Day-01/
├── Day-02/
├── Day-03/
├── Day-04/
├── Day-05/
├── Day-06/
├── Day-07/
│
├── Day-08/
│   ├── day_08_dictionaries.py
│   └── README.md
│
├── Day-09/
├── ...
└── README.md
```

---

# 🎯 Day 8 Completion

**Day 8 — Dictionaries ✅**

The program demonstrates the fundamental operations required to work effectively with Python dictionaries, including creation, access, modification, deletion, copying, iteration, and nested data structures.

---

## 📚 Next

Continue to **Day 9** to learn the next Python concept in the 30 Days of Python journey.

---

**Part of the [30 Days of Python](../README.md) learning journey.**

**Language:** Python 🐍
**Day:** 8 / 30
**Topic:** Dictionaries
