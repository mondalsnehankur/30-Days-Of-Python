# 📘 Day 9 — Conditionals

This folder contains the **Day 9** work from the **30 Days of Python** series.

The focus of Day 9 is **conditional execution in Python** using `if`, `elif`, `else`, nested conditions, and logical operators.

---

## 📚 Topics Covered

- If Condition
- If Else
- If Elif Else
- Short Hand If Else
- Nested Conditions
- If Condition with `and`
- If Condition with `or`
- Membership conditions using `in`
- User input with conditionals
- Practical conditional exercises

---

## 🧠 Theory

### 1. If Condition

The `if` statement is used to execute a block of code only when a condition is `True`.

```python
if condition:
    statement
```

Example:

```python
a = 3

if a > 0:
    print("A is a positive number")
```

---

### 2. If Else

`else` is executed when the `if` condition is `False`.

```python
if condition:
    statement_if_true
else:
    statement_if_false
```

Example:

```python
a = 3

if a < 0:
    print("A is a negative number")
else:
    print("A is a positive number")
```

---

### 3. If Elif Else

`elif` is used when there are multiple conditions to check.

```python
if condition1:
    statement1
elif condition2:
    statement2
else:
    statement3
```

Example:

```python
a = 0

if a > 0:
    print("A is a positive number")
elif a < 0:
    print("A is a negative number")
else:
    print("A is zero")
```

Python checks the conditions from top to bottom. Once a condition is `True`, its block is executed and the remaining conditions are skipped.

---

### 4. Short-Hand If Else

A conditional expression can be written in one line:

```python
statement_if_true if condition else statement_if_false
```

Example:

```python
a = 3

print("A is positive") if a > 0 else print("A is negative")
```

---

### 5. Nested Conditions

An `if` statement can be placed inside another `if` statement.

```python
if condition1:
    if condition2:
        statement
```

Example:

```python
a = 4

if a > 0:
    if a % 2 == 0:
        print("A is a positive and even integer")
```

Nested conditions are useful when one condition depends on another condition.

---

### 6. `and` Logical Operator

`and` requires **both conditions** to be `True`.

```python
if condition1 and condition2:
    statement
```

Example:

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")
```

---

### 7. `or` Logical Operator

`or` requires **at least one condition** to be `True`.

```python
if condition1 or condition2:
    statement
```

Example:

```python
user = "James"
access_level = 3

if user == "admin" or access_level >= 4:
    print("Access granted!")
else:
    print("Access denied!")
```

---

### 8. Membership Conditions

The `in` operator can be used to check whether an item exists in a sequence.

```python
fruits = ["banana", "orange", "mango"]

if "apple" in fruits:
    print("Apple exists")
else:
    print("Apple does not exist")
```

---

## 💻 Exercises

### Level 1

1. Get the user's age and determine whether they are old enough to learn to drive.
2. Compare the user's age with `my_age`.
3. Get two numbers and determine which one is greater, smaller, or equal.

### Level 2

1. Assign grades according to scores:
   - `90–100` → A
   - `80–89` → B
   - `70–79` → C
   - `60–69` → D
   - `0–59` → F
2. Determine the season from the month.
3. Check whether a fruit exists in a list and add it if it does not.

### Level 3

Using the given `person` dictionary:

1. Check whether the dictionary contains the `skills` key and print the middle skill.
2. Check whether the person has the `Python` skill.
3. Determine whether the person is a front-end, back-end, or full-stack developer.
4. Check whether the person is married and lives in Finland.

---

## 📁 Files

| File | Description |
|---|---|
| `day9_conditionals.py` | Complete Day 9 theory examples and exercises |
| `theory.py` | Short theory/syntax examples for Day 9 |
| `README.md` | Documentation for Day 9 |

---

## ▶️ How to Run

Make sure Python is installed.

Run the main file from the terminal:

```bash
python day9_conditionals.py
```

Or run the theory examples:

```bash
python theory.py
```

Some exercises use `input()`, so the program will ask for values in the terminal.

---

## 🔑 Important Concepts

### Condition Flow

```text
if
 ↓
condition True?
 ├── Yes → execute if block
 └── No
      ↓
    elif?
      ├── True → execute elif block
      └── False
           ↓
         else → execute else block
```

### Logical Operators

| Operator | Meaning |
|---|---|
| `and` | Both conditions must be true |
| `or` | At least one condition must be true |
| `not` | Reverses the Boolean result |

### Comparison Operators

| Operator | Meaning |
|---|---|
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |
| `==` | Equal to |
| `!=` | Not equal to |

---

## ⚠️ Important Python Rule: Indentation

Python uses indentation to define blocks of code.

Correct:

```python
if age >= 18:
    print("Eligible")
```

Incorrect:

```python
if age >= 18:
print("Eligible")
```

Usually, **4 spaces** are used for indentation.

---

## 🎯 Learning Outcome

After completing Day 9, you should be able to:

- Use `if`, `elif`, and `else`.
- Write nested conditional statements.
- Use `and` and `or` with conditions.
- Use comparison operators in decision-making.
- Use `in` to check membership.
- Accept user input and make decisions based on it.
- Write simple decision-making programs in Python.
- Combine multiple conditions to solve practical problems.

---

## 🗂️ Suggested Repository Structure

```text
30-Days-of-Python/
│
├── Day_01/
├── Day_02/
├── ...
├── Day_08/
│
├── Day_09/
│   ├── day9_conditionals.py
│   ├── theory.py
│   └── README.md
│
└── README.md
```

---

## 🚀 Progress

**Day 9 / 30 — Conditionals**

> Every conditional statement is a decision made by the program based on whether a condition is `True` or `False`.

