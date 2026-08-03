# 🐍 Day 2 – Variables, Data Types & Type Conversion in Python

Welcome to **Day 2** of the **30 Days of Python** challenge!

In this lesson, we cover the fundamental building blocks of Python programming:

- Variables
- Basic Data Types
- Printing Output
- The `type()` Function
- Type Conversion (Casting)

---

# 📚 Table of Contents

- [Variables](#variables)
- [Python Data Types](#python-data-types)
- [Printing Variables](#printing-variables)
- [Getting Data Types](#getting-data-types)
- [Type Conversion](#type-conversion)
- [Code Examples](#code-examples)
  - [Example 1 - Variables](#example-1---variables)
  - [Example 2 - Data Types](#example-2---data-types)
  - [Example 3 - Type Conversion](#example-3---type-conversion)
- [Key Functions Used](#key-functions-used)
- [Summary](#summary)

---

# Variables

A **variable** is a named container used to store data.

### Syntax

```python
variable_name = value
```

### Example

```python
name = "John"
age = 20
height = 5.8
```

Variables can store different kinds of information such as text, numbers, lists, dictionaries, and more.

---

# Python Data Types

Python provides several built-in data types.

| Data Type | Description | Example |
|-----------|-------------|---------|
| `str` | Text/String | `"Hello"` |
| `int` | Integer | `25` |
| `float` | Decimal Number | `3.14` |
| `bool` | Boolean | `True` |
| `list` | Ordered Collection | `[1,2,3]` |
| `tuple` | Immutable Collection | `(1,2)` |
| `dict` | Key-Value Pair | `{"name":"John"}` |
| `complex` | Complex Number | `2+3j` |
| `set` | Unordered Unique Collection | `{1,2,3}` |

---

# Printing Variables

The `print()` function is used to display output.

```python
name = "Alice"
print(name)
```

Output

```
Alice
```

You can print multiple values together.

```python
print(name, age)
```

---

# Getting Data Types

Python provides the built-in `type()` function to determine the data type of any object.

Example

```python
print(type(10))
```

Output

```
<class 'int'>
```

---

# Type Conversion

Type conversion (also called **casting**) is the process of converting one data type into another.

Python provides several built-in conversion functions.

| Function | Converts To |
|-----------|-------------|
| `int()` | Integer |
| `float()` | Float |
| `str()` | String |
| `list()` | List |
| `tuple()` | Tuple |
| `set()` | Set |
| `dict()` | Dictionary (when applicable) |

Example

```python
age = "20"
age = int(age)
```

---

# Code Examples

## Example 1 - Variables

This example demonstrates:

- Variable declaration
- Different data types
- Printing variables
- Finding string length using `len()`
- Multiple variable assignment

```python
# Variables in Python

first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']

person_info = {
    'firstname': 'Asabeneh',
    'lastname': 'Yetayeh',
    'country': 'Finland',
    'city': 'Helsinki'
}

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name:', last_name)
print('Last name length:', len(last_name))
print('Country:', country)
print('City:', city)
print('Age:', age)
print('Married:', is_married)
print('Skills:', skills)
print('Person information:', person_info)

first_name, last_name, country, age, is_married = (
    'Asabeneh',
    'Yetayeh',
    'Helsink',
    250,
    True
)

print(first_name, last_name, country, age, is_married)
```

---

## Example 2 - Data Types

This example demonstrates how to identify the data type of different Python objects using the `type()` function.

```python
first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250

print(type('Asabeneh'))
print(type(first_name))
print(type(10))
print(type(3.14))
print(type(1 + 1j))
print(type(True))
print(type([1, 2, 3, 4]))
print(type({'name': 'Asabeneh'}))
print(type((1, 2)))
print(type(zip([1,2],[3,4])))
```

Expected Output

```
<class 'str'>
<class 'str'>
<class 'int'>
<class 'float'>
<class 'complex'>
<class 'bool'>
<class 'list'>
<class 'dict'>
<class 'tuple'>
<class 'zip'>
```

---

## Example 3 - Type Conversion

This example demonstrates converting values between different data types.

```python
# int → float
num_int = 10
num_float = float(num_int)

# float → int
gravity = 9.81
print(int(gravity))

# int → string
num_str = str(num_int)

# string → float
num_str = '10.6'
num_float = float(num_str)

# float → int
num_int = int(num_float)

# string → list
first_name = 'Asabeneh'
first_name_to_list = list(first_name)

print(first_name_to_list)
```

Output

```
10.0
9
10
10.6
10
['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']
```

---

# Key Functions Used

## `print()`

Displays output on the console.

```python
print("Hello World")
```

---

## `len()`

Returns the number of characters in a string or elements in a collection.

```python
name = "Python"

print(len(name))
```

Output

```
6
```

---

## `type()`

Returns the data type of an object.

```python
print(type(5))
```

Output

```
<class 'int'>
```

---

## `int()`

Converts a compatible value into an integer.

```python
int(9.81)
```

Output

```
9
```

---

## `float()`

Converts a value into a floating-point number.

```python
float(10)
```

Output

```
10.0
```

---

## `str()`

Converts a value into a string.

```python
str(100)
```

Output

```
'100'
```

---

## `list()`

Converts an iterable into a list.

```python
list("Python")
```

Output

```
['P', 'y', 't', 'h', 'o', 'n']
```

---

# Summary

In this lesson, you learned how to:

- ✅ Declare variables
- ✅ Store different types of values
- ✅ Print data using `print()`
- ✅ Find the length of strings using `len()`
- ✅ Identify data types using `type()`
- ✅ Assign multiple variables in one line
- ✅ Convert between different data types
- ✅ Convert strings into lists

These concepts form the foundation of Python programming and are essential before moving on to operators, strings, conditional statements, loops, functions, and object-oriented programming.

---

## 📁 Repository Structure

```
Day-01-Variables-and-DataTypes/
│
├── variables.py
├── data_types.py
├── type_conversion.py
└── README.md
```

---

## 🚀 Next Topic

➡️ **Python Operators**
- Arithmetic Operators
- Comparison Operators
- Logical Operators
- Assignment Operators
- Identity Operators
- Membership Operators
