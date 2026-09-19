# Python Date and Time — `datetime` Module

A structured Python learning project based on the concepts covered in **Day 16: Python Date and Time** from the provided reference material.

## Overview

Python's built-in `datetime` module provides tools for working with dates, times, timestamps, date-time formatting/parsing, and differences between points in time.

This project turns those concepts into a runnable, organized code structure rather than reproducing the reference examples verbatim.

## Concepts Covered

- Importing and inspecting the `datetime` module
- Getting the current date and time with `datetime.now()`
- Accessing:
  - day
  - month
  - year
  - hour
  - minute
  - second
  - Unix timestamp
- Formatting date/time with `strftime()`
- Converting strings to date/time objects with `strptime()`
- Creating and using `date` objects
- Getting today's date with `date.today()`
- Creating `time` objects
- Calculating differences between dates and datetimes
- Using `timedelta` for time arithmetic
- Practical applications of the `datetime` module

## Project Structure

```text
python_datetime_project/
│
├── README.md
│
├── src/
│   ├── datetime_basics.py
│   ├── formatting_parsing.py
│   ├── date_time_objects.py
│   └── time_differences.py
│
├── examples/
│   └── practical_applications.py
│
└── exercises/
    └── exercises.py
```

## Requirements

- Python 3.x
- No external packages are required.

The project uses only Python's standard library.

## How to Run

Open a terminal inside the project folder.

### 1. Run the basic datetime examples

```bash
python src/datetime_basics.py
```

### 2. Run formatting and parsing

```bash
python src/formatting_parsing.py
```

### 3. Run date and time object examples

```bash
python src/date_time_objects.py
```

### 4. Run date/time difference examples

```bash
python src/time_differences.py
```

### 5. Run practical applications

```bash
python examples/practical_applications.py
```

### 6. Attempt the exercises

```bash
python exercises/exercises.py
```

## Module Breakdown

### `datetime_basics.py`

Demonstrates:

- `datetime.now()`
- Date/time component extraction
- Unix timestamps

A timestamp represents the number of seconds elapsed since January 1, 1970 UTC.

### `formatting_parsing.py`

Demonstrates:

- `strftime()` — datetime object → formatted string
- `strptime()` — formatted string → datetime object

Example:

```python
from datetime import datetime

now = datetime.now()
formatted = now.strftime("%d/%m/%Y, %H:%M:%S")
print(formatted)
```

### `date_time_objects.py`

Demonstrates:

- Creating `date` objects
- `date.today()`
- Creating `time` objects
- Accessing their components

### `time_differences.py`

Demonstrates:

- Subtracting two dates
- Subtracting two datetime objects
- Creating `timedelta` objects
- Performing time arithmetic

Example:

```python
from datetime import date

today = date.today()
new_year = date(today.year + 1, 1, 1)

print(new_year - today)
```

## `strftime()` Format Codes Used

| Code | Meaning |
|---|---|
| `%d` | Day of the month |
| `%m` | Month |
| `%Y` | Four-digit year |
| `%H` | Hour (24-hour clock) |
| `%M` | Minute |
| `%S` | Second |

For example:

```python
now.strftime("%m/%d/%Y, %H:%M:%S")
```

## `strptime()` vs `strftime()`

| Method | Direction | Purpose |
|---|---|---|
| `strftime()` | datetime → string | Format a date/time for display |
| `strptime()` | string → datetime | Parse a date/time string |

## `timedelta`

`timedelta` represents a duration and can be created using units such as:

- weeks
- days
- hours
- minutes
- seconds

Example:

```python
from datetime import timedelta

duration = timedelta(weeks=2, days=3, hours=4)
print(duration)
```

## Practical Uses

The concepts in this project can be applied to:

- Time-series analysis
- Activity timestamps
- Blog post timestamps
- Event scheduling
- Countdown calculations
- Log processing
- Date validation and conversion
- Measuring elapsed time

## Learning Flow

A recommended order is:

1. Understand `date`, `time`, and `datetime`
2. Learn how to extract date/time components
3. Learn timestamp representation
4. Learn `strftime()`
5. Learn `strptime()`
6. Learn date/time subtraction
7. Learn `timedelta`
8. Apply the concepts to small programs

## Exercises

The exercise file covers the main practice tasks from the reference:

1. Get the current day, month, year, hour, minute, and timestamp.
2. Format the current date as `%m/%d/%Y, %H:%M:%S`.
3. Convert `5 December, 2019` into a datetime object.
4. Calculate the time difference between now and the next New Year.
5. Calculate the time difference between January 1, 1970 and now.
6. Identify practical applications of the `datetime` module.

## Notes

The source material uses historical example dates such as 2019–2022. This project keeps those concepts but uses the current runtime date where a live/current value is appropriate.

No third-party dependency or internet connection is required.

## Reference

This project is based on the provided **Day 16 — Python Date and Time** material by **Asabeneh Yetayeh**, Second Edition, July 2021. The source covers the `datetime`, `date`, `time`, and `timedelta` concepts, along with `strftime()`, `strptime()`, date/time differences, and exercises. 
