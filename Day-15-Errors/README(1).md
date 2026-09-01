# 30 Days of Python — Day 15: Python Error Types

This repository section covers common Python error types and demonstrates how to identify and debug them. The material is based on the supplied Day 15 README, which introduces the error types one by one and then asks the learner to try the examples in the Python interactive shell. fileciteturn0file0L34-L40

## Topics Covered

1. SyntaxError
2. NameError
3. IndexError
4. ModuleNotFoundError
5. AttributeError
6. KeyError
7. TypeError
8. ImportError
9. ValueError
10. ZeroDivisionError

The README explicitly lists these ten error types in its Day 15 contents. fileciteturn0file0L20-L31

## Python File

The repository includes:

```text
day_15_python_error_types.py
```

Run it with:

```bash
python day_15_python_error_types.py
```

The Python file turns the README's interactive examples into a single runnable practice program. Intentional runtime errors are handled with `try/except` so that all demonstrations can be executed in one run.

---

## 1. SyntaxError

A `SyntaxError` occurs when Python cannot understand the structure of the code.

The supplied README demonstrates the error using Python 2-style `print 'hello world'`, and then fixes it with Python 3 syntax:

```python
print('hello world')
```

fileciteturn0file0L42-L59

### Key idea

The code must follow Python's syntax rules before Python can execute it.

---

## 2. NameError

A `NameError` occurs when you try to use a variable or name that has not been defined.

Example:

```python
print(age)
```

This raises a `NameError` because `age` has not been defined yet. The README fixes it by defining:

```python
age = 25
print(age)
```

fileciteturn0file0L78-L111

### Key idea

Check whether the variable or function name exists and whether it has been spelled correctly.

---

## 3. IndexError

An `IndexError` occurs when you try to access an index outside the valid range of a sequence.

Example:

```python
numbers = [1, 2, 3, 4, 5]
numbers[5]
```

The valid indexes are `0` through `4`, so index `5` is out of range. fileciteturn0file0L113-L130

### Key idea

Remember that Python indexing starts at `0`.

---

## 4. ModuleNotFoundError

A `ModuleNotFoundError` occurs when Python cannot find the module you are trying to import.

The README demonstrates a deliberately misspelled import:

```python
import maths
```

and fixes it as:

```python
import math
```

fileciteturn0file0L132-L163

### Key idea

Check the module name carefully and make sure the required package/module is available.

---

## 5. AttributeError

An `AttributeError` occurs when an object or module does not have the attribute you are trying to access.

The README uses:

```python
import math
math.PI
```

and shows that the correct attribute is:

```python
math.pi
```

fileciteturn0file0L165-L207

### Key idea

Check the exact attribute name, including capitalization.

---

## 6. KeyError

A `KeyError` occurs when you try to access a dictionary using a key that does not exist.

Example:

```python
user = {
    "name": "Asab",
    "age": 250,
    "country": "Finland"
}

user["county"]
```

The key is actually `"country"`, not `"county"`. fileciteturn0file0L209-L247

### Key idea

Check the dictionary key for spelling mistakes and make sure the key exists.

---

## 7. TypeError

A `TypeError` occurs when an operation is performed with an inappropriate type.

Example:

```python
4 + "3"
```

Python cannot directly add an integer and a string. The README demonstrates converting the string:

```python
4 + int("3")
```

or:

```python
4 + float("3")
```

fileciteturn0file0L249-L283

### Key idea

Check the data types involved in the operation and convert them when appropriate.

---

## 8. ImportError

An `ImportError` can occur when Python finds the module but cannot import the requested name from it.

The README demonstrates:

```python
from math import power
```

and corrects it to:

```python
from math import pow

pow(2, 3)
```

fileciteturn0file0L285-L318

### Key idea

Make sure the function, class, or name you are importing actually exists in the module.

---

## 9. ValueError

A `ValueError` occurs when a function receives a value of the correct general type but the value itself is not acceptable for that operation.

The README demonstrates:

```python
int("12a")
```

The string cannot be converted to an integer because it contains the letter `a`. fileciteturn0file0L318-L332

### Key idea

Check whether the value can actually be used for the requested conversion or operation.

---

## 10. ZeroDivisionError

A `ZeroDivisionError` occurs when you attempt to divide by zero.

Example:

```python
1 / 0
```

The README demonstrates this directly and notes that a number cannot be divided by zero. fileciteturn0file0L334-L348

### Key idea

Check the denominator before performing division.

---

## Error Summary

| Error | What it generally means | README example |
|---|---|---|
| `SyntaxError` | Python syntax is invalid | `print 'hello world'` |
| `NameError` | A name/variable is not defined | `print(age)` |
| `IndexError` | Sequence index is out of range | `numbers[5]` |
| `ModuleNotFoundError` | Module cannot be found | `import maths` |
| `AttributeError` | Attribute does not exist | `math.PI` |
| `KeyError` | Dictionary key does not exist | `user["county"]` |
| `TypeError` | Operation uses incompatible types | `4 + "3"` |
| `ImportError` | Requested name cannot be imported | `from math import power` |
| `ValueError` | Value is invalid for the operation | `int("12a")` |
| `ZeroDivisionError` | Division by zero | `1 / 0` |

## Debugging Approach

When Python displays an error:

1. Read the **exception type**.
2. Read the **error message**.
3. Look at the line where the problem occurred.
4. Check names, spelling, indexes, types, values, and imports.
5. Apply a small fix.
6. Run the code again.

The supplied README emphasizes that understanding error types helps you debug code faster. fileciteturn0file0L350-L353

## Exercises

The original Day 15 exercise asks the learner to open the Python interactive shell and try all the examples covered in the section. fileciteturn0file0L353-L359

For this repository implementation, run:

```bash
python day_15_python_error_types.py
```

Then compare each demonstration with the corresponding section above.

## Repository Structure

```text
15_Day_Python_Error_Types/
├── day_15_python_error_types.py
└── README.md
```

## Learning Outcome

After completing this day, you should be able to:

- Recognize common Python exception types.
- Read basic traceback messages.
- Identify common spelling and indexing mistakes.
- Identify type and value problems.
- Diagnose incorrect imports.
- Use `try/except` to handle runtime exceptions in practice code.
- Debug simple Python programs more efficiently.

## Source

This repository section is based on the supplied **30 Days of Python — Day 15: Python Type Errors** README. The source identifies the lesson as Day 15 and attributes the material to Asabeneh Yetayeh, Second Edition, July 2021. fileciteturn0file0L1-L12
