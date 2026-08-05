# Python Strings – Complete Guide

A beginner-friendly Python program demonstrating string creation, manipulation, indexing, slicing, formatting, escape sequences, and commonly used string methods.

## 📌 Overview

This repository contains a comprehensive Python script covering the fundamentals of string handling. It introduces different ways to create strings, access characters, manipulate text, and use Python's built-in string methods.

This project is ideal for beginners learning Python and serves as a quick reference for string operations.

---

## ✨ Features

* String creation
* Single-line and multi-line strings
* String concatenation
* String length using `len()`
* Character unpacking
* Indexing and negative indexing
* String slicing
* Escape sequences
* String formatting using `format()`
* Common string methods
* Membership and validation methods

---

## 📂 Topics Covered

### 1. Creating Strings

Examples using:

* Single quotes
* Double quotes
* Triple quotes (multi-line strings)

Example:

```python
name = "Python"
message = 'Hello World'
```

---

### 2. String Concatenation

Combining multiple strings into one.

```python
full_name = first_name + " " + last_name
```

---

### 3. Finding String Length

Using the built-in `len()` function.

```python
print(len(full_name))
```

---

### 4. Character Unpacking

Assigning each character of a string to different variables.

```python
language = "Python"
a, b, c, d, e, f = language
```

---

### 5. String Indexing

Accessing individual characters using positive and negative indices.

Examples:

```python
language[0]
language[-1]
language[-2]
```

---

### 6. String Slicing

Extracting parts of a string.

Examples:

```python
language[0:3]
language[3:]
language[-3:]
language[0:6:2]
```

---

### 7. Escape Sequences

The program demonstrates:

| Escape Sequence | Description  |
| --------------- | ------------ |
| `\n`            | New line     |
| `\t`            | Tab space    |
| `\\`            | Backslash    |
| `\"`            | Double quote |

---

### 8. String Formatting

Using the `format()` method to insert values into strings.

Example:

```python
sentence = "I am {} {}".format(first_name, last_name)
```

---

## 🔧 String Methods Demonstrated

The program covers many frequently used string methods.

| Method           | Description                                    |
| ---------------- | ---------------------------------------------- |
| `capitalize()`   | Capitalizes the first letter                   |
| `count()`        | Counts occurrences of a substring              |
| `endswith()`     | Checks if string ends with a value             |
| `expandtabs()`   | Replaces tab characters with spaces            |
| `find()`         | Returns first index of a substring             |
| `format()`       | Formats strings                                |
| `isalnum()`      | Checks if all characters are alphanumeric      |
| `isalpha()`      | Checks if all characters are alphabetic        |
| `isdigit()`      | Checks if all characters are digits            |
| `isdecimal()`    | Checks for decimal characters                  |
| `isidentifier()` | Checks if string is a valid Python identifier  |
| `islower()`      | Checks if all letters are lowercase            |
| `isupper()`      | Checks if all letters are uppercase            |
| `isnumeric()`    | Checks for numeric characters                  |
| `join()`         | Joins iterable elements into a string          |
| `strip()`        | Removes leading and trailing characters/spaces |
| `replace()`      | Replaces a substring                           |
| `split()`        | Splits a string into a list                    |
| `title()`        | Converts to title case                         |
| `swapcase()`     | Swaps uppercase and lowercase letters          |
| `startswith()`   | Checks if string starts with a value           |

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/python-strings-guide.git
```

2. Move into the project folder:

```bash
cd python-strings-guide
```

3. Execute the script:

```bash
python strings.py
```

---

## 📚 Learning Outcomes

After completing this program, you will understand how to:

* Create strings in Python
* Access characters using indexing
* Slice strings efficiently
* Concatenate multiple strings
* Use escape sequences
* Format strings dynamically
* Apply Python's built-in string methods
* Validate string content
* Manipulate text for real-world applications

---

## 🛠 Requirements

* Python 3.x

---

## 🎯 Suitable For

* Python beginners
* Programming students
* Anyone learning string manipulation in Python
* Developers looking for a quick reference to Python string methods

---

## 📄 License

This project is open-source and intended for educational and learning purposes.
