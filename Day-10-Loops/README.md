# 30 Days of Python — Day 10: Loops

This repository contains my practice code for **Day 10: Loops** from the 30 Days of Python learning material.

The source material covers Python's two main loop types — `while` and `for` — along with `break`, `continue`, `range()`, nested loops, `for-else`, and `pass`. fileciteturn0file0L38-L43

## Topics Covered

- While loop
- While loop with `else`
- For loop
- Iterating over:
  - Lists
  - Tuples
  - Strings
  - Dictionaries
  - Sets
- `break`
- `continue`
- `range()`
- Nested `for` loops
- `for-else`
- `pass`
- Loop patterns
- Even and odd number filtering
- Summation using loops
- Searching using `for-else`
- Reversing a list using a loop
- Practical loop applications

The original learning material explicitly introduces `while` and `for` as the two loop types and then develops these variations. fileciteturn0file0L40-L43

## Repository Structure

```text
Day_10_Loops/
│
├── 01_while_loops.py
├── 02_break_continue.py
├── 03_for_loops.py
├── 04_range_function.py
├── 05_nested_loops.py
├── 06_for_else_and_pass.py
├── 07_loop_patterns_exercises.py
├── 08_loop_applications.py
└── README.md
```

## 1. While Loops

A `while` loop repeatedly executes a block of code while its condition remains true.

```python
count = 0

while count < 5:
    print(count)
    count += 1
```

A `while` loop can also have an `else` block. The `else` executes when the loop finishes normally. fileciteturn0file0L45-L65

```python
count = 0

while count < 5:
    print(count)
    count += 1
else:
    print("Loop ended")
```

## 2. For Loops

A `for` loop is used to iterate over a sequence such as a list, tuple, dictionary, set, or string. fileciteturn0file0L138-L142

```python
numbers = [0, 1, 2, 3, 4]

for number in numbers:
    print(number)
```

### String

```python
language = "Python"

for letter in language:
    print(letter)
```

### Tuple

```python
numbers = (0, 1, 2, 3, 4)

for number in numbers:
    print(number)
```

### Dictionary

```python
person = {
    "name": "Student",
    "age": 24
}

for key in person:
    print(key)

for key, value in person.items():
    print(key, value)
```

### Set

```python
companies = {"Google", "Microsoft", "Apple"}

for company in companies:
    print(company)
```

The supplied material demonstrates these different iterable types with `for` loops. fileciteturn0file0L140-L155 fileciteturn0file0L169-L190 fileciteturn0file0L194-L222

## 3. break

`break` immediately stops the loop.

```python
for number in range(10):
    if number == 5:
        break
    print(number)
```

The original lesson describes `break` as a way to stop a loop before it is completed. fileciteturn0file0L241-L264

## 4. continue

`continue` skips the current iteration and moves to the next iteration.

```python
for number in range(10):
    if number == 5:
        continue
    print(number)
```

The source material demonstrates this behavior for both `while` and `for` loops. fileciteturn0file0L114-L136 fileciteturn0file0L266-L288

## 5. range()

The general form is:

```python
range(start, stop, step)
```

The `stop` value is not included.

Examples:

```python
range(10)
range(1, 11)
range(0, 11, 2)
range(11, 0, -2)
```

The lesson covers one-, two-, and three-argument forms of `range()` and backward iteration with a negative step. fileciteturn0file0L290-L319

## 6. Nested Loops

A nested loop is a loop inside another loop.

```python
for row in range(3):
    for column in range(4):
        print(row, column)
```

Nested loops are useful for grids, tables, patterns, and multidimensional data. The supplied material also demonstrates a nested loop for iterating through a dictionary's list of skills. fileciteturn0file0L323-L355

## 7. for-else

Python allows an `else` block after a `for` loop.

```python
for number in range(5):
    print(number)
else:
    print("Loop ended")
```

The `else` executes when the loop completes normally. If the loop is terminated using `break`, the `else` block is skipped.

```python
for number in range(10):
    if number == 5:
        break
else:
    print("Completed normally")
```

The source material introduces `for-else` specifically for executing code when the loop ends. fileciteturn0file0L355-L375

## 8. pass

`pass` does nothing. It is useful as a placeholder when Python requires a statement but no action is currently needed.

```python
for number in range(5):
    pass
```

The supplied lesson presents `pass` as a placeholder for code that may be added later. fileciteturn0file0L376-L385

## Practice Exercises Included

The exercise file implements the main Day 10 exercises, including:

1. Iterating from 0 to 10 with `for`
2. Iterating from 0 to 10 with `while`
3. Counting down from 10 to 0
4. Creating a seven-row `#` triangle
5. Creating an 8 × 8 pattern
6. Printing square values from 0 to 10
7. Iterating through a list of technologies
8. Printing even numbers from 0 to 100
9. Printing odd numbers from 0 to 100
10. Calculating the sum from 0 to 100
11. Calculating separate sums of even and odd numbers
12. Reversing a list using a loop

These correspond to the Level 1 and Level 2 loop exercises in the supplied material. fileciteturn0file0L389-L454

## Expected Results

The Day 10 exercises establish these important results:

```text
Sum of numbers from 0 to 100 = 5050
Sum of even numbers from 0 to 100 = 2550
Sum of odd numbers from 0 to 100 = 2500
```

## How to Run

Make sure Python is installed, then open a terminal in this directory.

Run any file with:

```bash
python 01_while_loops.py
```

For example:

```bash
python 07_loop_patterns_exercises.py
```

## Learning Notes

The main idea behind loops is **repetition**.

Use:

- `while` when repetition depends mainly on a condition.
- `for` when iterating over a sequence or a known range.
- `break` when the loop must stop immediately.
- `continue` when the current iteration should be skipped.
- `range()` when generating a sequence of numbers for iteration.
- Nested loops when one repeated operation must occur inside another.
- `for-else` when an action should occur only if the loop finishes without `break`.
- `pass` when a syntactically valid placeholder is required.

## Day 10 Progress

- [x] While loops
- [x] While-else
- [x] For loops
- [x] List iteration
- [x] Tuple iteration
- [x] String iteration
- [x] Dictionary iteration
- [x] Set iteration
- [x] Break
- [x] Continue
- [x] Range
- [x] Nested loops
- [x] For-else
- [x] Pass
- [x] Loop exercises
- [x] Practical loop examples

---

**Part of my Python learning journey — 30 Days of Python.**
