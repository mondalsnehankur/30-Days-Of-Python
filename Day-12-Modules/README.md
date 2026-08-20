## 📚 Overview

Day 12 introduces **modules in Python** and explains how to organize reusable code into separate `.py` files. The lesson covers creating custom modules, importing functions and variables, renaming imports, and working with commonly used Python built-in modules.

The day also includes practical exercises involving random IDs, RGB colors, hexadecimal colors, and shuffled or unique random numbers.

---

## 🎯 Learning Objectives

By completing this day, you will learn how to:

- Understand what a Python module is.
- Create and use your own custom modules.
- Import complete modules using `import`.
- Import specific functions or variables using `from ... import ...`.
- Rename imported functions, variables, and modules using `as`.
- Work with commonly used built-in Python modules.
- Use the `os` module for operating-system operations.
- Use the `sys` module and command-line arguments.
- Perform statistical calculations using `statistics`.
- Perform mathematical operations using `math`.
- Work with predefined string constants using `string`.
- Generate random values using `random`.

---

## 🧩 Topics Covered

### 1. What is a Module?

A **module** is a Python file containing reusable code such as:

- Functions
- Variables
- Classes
- Constants
- Other Python statements

Modules help keep programs **organized, reusable, and maintainable**.

---

### 2. Creating a Custom Module

A module can be created simply by saving Python code in a `.py` file.

Example:

```python
# mymodule.py

def generate_full_name(firstname, lastname):
    return firstname + " " + lastname
