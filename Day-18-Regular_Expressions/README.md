# Python Regular Expressions — `re` Module

A structured Python learning project based on **30 Days of Python — Day 18: Regular Expressions** by Asabeneh Yetayeh.

The project organizes the main concepts from the reference material into reusable Python files, practical examples, and completed exercises.

## Topics Covered

- Regular expressions and pattern matching
- Python's `re` module
- `re.match()`
- `re.search()`
- `re.findall()`
- `re.sub()`
- `re.split()`
- Raw regular-expression strings
- Case-insensitive matching with `re.I`
- Character sets
- Escape sequences
- `\d` and `\D`
- `.`
- `^`
- `$`
- `*`
- `+`
- `?`
- Quantifiers such as `{3}`, `{3,}`, and `{3,8}`
- Alternation with `|`
- Capturing/grouping with `()`
- Negated character sets
- Cleaning text using regular expressions
- Extracting numbers from text
- Validating Python variable names
- Finding frequent words

## Project Structure

```text
python_regular_expressions_project/
│
├── README.md
│
├── src/
│   ├── regex_methods.py
│   ├── regex_patterns.py
│   └── text_processing.py
│
├── examples/
│   └── practical_examples.py
│
└── exercises/
    └── exercises.py
```

## Requirements

- Python 3.x
- No external packages are required.

The project uses Python's built-in `re` module and other standard-library modules only.

## How to Run

From the project directory:

```bash
python src/regex_methods.py
```

```bash
python src/regex_patterns.py
```

```bash
python src/text_processing.py
```

```bash
python examples/practical_examples.py
```

```bash
python exercises/exercises.py
```

## 1. The `re` Module

Regular expressions are patterns used to search, identify, extract, replace, or split text.

Import the module with:

```python
import re
```

## 2. Main `re` Methods

| Method | Purpose |
|---|---|
| `re.match()` | Searches for a match at the beginning of a string |
| `re.search()` | Searches for the first match anywhere in the string |
| `re.findall()` | Returns all matches as a list |
| `re.split()` | Splits text at matching positions |
| `re.sub()` | Replaces matching text |

### `re.match()`

```python
import re

text = "I love to teach Python"
match = re.match("I love to teach", text, re.I)

if match:
    print(match.span())
    print(match.group())
```

`match()` only succeeds when the pattern occurs at the beginning of the string.

### `re.search()`

```python
match = re.search("Python", text, re.I)
```

Unlike `match()`, `search()` can locate the pattern anywhere in the string.

### `re.findall()`

```python
matches = re.findall("python", text, re.I)
```

This returns every matching occurrence as a list.

### `re.sub()`

```python
cleaned = re.sub("%", "", text)
```

This replaces matching occurrences with the supplied replacement string.

### `re.split()`

```python
parts = re.split(r"\n", text)
```

This splits the string wherever the regular-expression pattern matches.

## 3. Writing Regular-Expression Patterns

Raw strings are commonly used for regular expressions:

```python
pattern = r"\d+"
```

The `r` prefix prevents Python from interpreting backslashes as ordinary string escape sequences before the regular-expression engine receives them.

## 4. Character Sets

Square brackets define a set of possible characters.

| Pattern | Meaning |
|---|---|
| `[a-c]` | `a`, `b`, or `c` |
| `[a-z]` | Lowercase letters |
| `[A-Z]` | Uppercase letters |
| `[0-3]` | Digits 0 through 3 |
| `[0-9]` | Any digit |
| `[A-Za-z0-9]` | Letter or digit |

Example:

```python
re.findall(r"[Aa]pple", text)
```

This can match both `Apple` and `apple`.

## 5. Important Regex Symbols

| Pattern | Meaning |
|---|---|
| `\d` | Digit |
| `\D` | Non-digit |
| `.` | Any character except newline |
| `^` | Start of string |
| `$` | End of string |
| `*` | Zero or more occurrences |
| `+` | One or more occurrences |
| `?` | Zero or one occurrence |
| `{3}` | Exactly 3 occurrences |
| `{3,}` | At least 3 occurrences |
| `{3,8}` | 3 to 8 occurrences |
| `\|` | Either/or |
| `()` | Group/capture |
| `[^...]` | Characters not in the set |

## 6. Examples of Quantifiers

### One or more digits

```python
re.findall(r"\d+", text)
```

This extracts complete runs of digits rather than individual digits.

### Exactly four digits

```python
re.findall(r"\d{4}", text)
```

This can be used to find four-digit years such as `2019` and `2021`.

### Optional character

```python
re.findall(r"[Ee]-?mail", text)
```

The hyphen may occur zero or one time, allowing forms such as:

```text
email
Email
e-mail
E-mail
```

## 7. Start and End Anchors

`^` matches the beginning of a string:

```python
re.findall(r"^This", text)
```

`$` matches the end of a string:

```python
re.findall(r"love$", text)
```

When `^` is placed inside a character set, it means negation:

```python
r"[^A-Za-z ]+"
```

This can be used to identify characters that are not letters or spaces.

## 8. Case-Insensitive Matching

The reference demonstrates `re.I`:

```python
re.findall(r"python", text, re.I)
```

This allows both uppercase and lowercase forms to match.

## 9. Practical Applications

Regular expressions can be used for:

- Extracting numbers
- Detecting keywords
- Cleaning noisy text
- Validating identifiers
- Finding repeated patterns
- Replacing unwanted characters
- Splitting structured text
- Basic input validation
- Text preprocessing

## Exercises Included

The project implements the exercises from the supplied Day 18 material:

### Level 1

1. Find the most frequent word in the supplied paragraph.
2. Extract particle positions from text and calculate the distance between the two furthest particles.

### Level 2

3. Validate whether strings such as these are valid Python variable names:

```text
first_name  -> True
first-name  -> False
1first_name -> False
firstname   -> True
```

### Level 3

4. Clean the supplied noisy sentence using regular expressions.
5. Count and display the three most frequent words in the cleaned text.

The original exercise requirements are retained from the reference material. fileciteturn2file0L418-L489

## Learning Flow

Recommended order:

1. Understand what a regular expression is.
2. Learn `import re`.
3. Learn `match()`, `search()`, and `findall()`.
4. Learn `sub()` and `split()`.
5. Learn raw regex strings.
6. Learn character sets.
7. Learn escape sequences.
8. Learn quantifiers.
9. Learn anchors.
10. Practice text cleaning and validation.
11. Complete the exercises.

## Important Difference Between the Main Methods

```text
match()   -> beginning of string
search()  -> first match anywhere
findall() -> all matches
sub()     -> replace matches
split()   -> split around matches
```

## Reference

This project is based on the supplied **30 Days Of Python: Day 18 - Regular Expressions** material by **Asabeneh Yetayeh**. The source introduces the `re` module and its core methods, regex pattern construction, character sets, quantifiers, anchors, replacement, splitting, and exercises. fileciteturn2file0L44-L70
