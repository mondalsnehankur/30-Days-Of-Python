# 📘 Day 19 — File Handling in Python

A complete, runnable project based on **Day 19: File Handling** from
[Asabeneh Yetayeh's 30 Days of Python](https://github.com/Asabeneh/30-Days-Of-Python).

This project covers:

- Opening, reading, writing, appending and deleting files
- `txt`, `json`, `csv`, `xlsx` and `xml` files
- JSON ↔ Python dictionary conversion
- CSV processing
- Excel file reading/writing with `openpyxl`
- XML parsing with `xml.etree.ElementTree`
- All Day 19 exercise levels with Python solutions
- Text analysis, word frequency and email extraction
- Text similarity using stop-word removal and Jaccard similarity
- Hacker News CSV analysis
- A downloader for the original Day 19 datasets

> **Note about datasets:** The original lesson references several large public datasets
> (speech transcripts, Hacker News data, Romeo and Juliet, etc.). They are not copied
> into this package in full. `download_data.py` can retrieve the original files from
> the upstream 30 Days of Python repository when internet access is available.
> Small local sample datasets are included so the project can still be demonstrated offline.

---

## 📁 Project Structure

```text
Day_19_File_Handling/
│
├── README.md
├── requirements.txt
├── .gitignore
├── download_data.py
├── run_all.py
│
├── examples/
│   └── file_handling_examples.py
│
├── solutions/
│   ├── __init__.py
│   └── day19_solutions.py
│
├── files/
│   ├── reading_file_example.txt
│   ├── writing_file_example.txt
│   ├── json_example.json
│   ├── csv_example.csv
│   └── xml_example.xml
│
└── data/
    ├── README.md
    ├── sample.txt
    ├── sample_emails.txt
    ├── sample_romeo_and_juliet.txt
    ├── sample_hacker_news.csv
    ├── sample_countries_data.json
    └── stop_words.py
```

---

## 🚀 Requirements

- Python **3.9+**
- `openpyxl`

Install the dependency:

```bash
pip install -r requirements.txt
```

No external package is required for TXT, JSON, CSV or XML processing.

---

## ▶️ Run the Project

From the project root:

```bash
python run_all.py
```

Run only the lesson examples:

```bash
python examples/file_handling_examples.py
```

Run only the exercise solutions:

```bash
python solutions/day19_solutions.py
```

---

# 1. File Handling

Python uses the built-in `open()` function to work with files.

```python
open("filename", "mode")
```

Common modes:

| Mode | Meaning |
|---|---|
| `r` | Read |
| `w` | Write and overwrite |
| `a` | Append |
| `x` | Create; error if file already exists |
| `t` | Text mode |
| `b` | Binary mode |

### Reading a complete file

```python
with open("files/reading_file_example.txt", "r", encoding="utf-8") as f:
    text = f.read()
    print(text)
```

### Reading a fixed number of characters

```python
with open("files/reading_file_example.txt", encoding="utf-8") as f:
    print(f.read(10))
```

### Reading one line

```python
with open("files/reading_file_example.txt", encoding="utf-8") as f:
    print(f.readline())
```

### Reading all lines

```python
with open("files/reading_file_example.txt", encoding="utf-8") as f:
    print(f.readlines())
```

### Reading lines without newline characters

```python
with open("files/reading_file_example.txt", encoding="utf-8") as f:
    print(f.read().splitlines())
```

Using `with` is recommended because Python automatically closes the file.

---

# 2. Writing and Updating Files

### Append

```python
with open("files/reading_file_example.txt", "a", encoding="utf-8") as f:
    f.write("\nThis line was appended.")
```

### Write

```python
with open("files/writing_file_example.txt", "w", encoding="utf-8") as f:
    f.write("This replaces the existing file content.")
```

---

# 3. Deleting Files

```python
import os

file_path = "files/example.txt"

if os.path.exists(file_path):
    os.remove(file_path)
else:
    print("The file does not exist.")
```

---

# 4. TXT Files

TXT files contain ordinary text.

```python
with open("files/reading_file_example.txt", encoding="utf-8") as f:
    text = f.read()
```

---

# 5. JSON Files

JSON (JavaScript Object Notation) is commonly used for structured data.

### JSON string → Python dictionary

```python
import json

person_json = '''
{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScript", "React", "Python"]
}
'''

person = json.loads(person_json)
print(person["name"])
```

### Python dictionary → JSON string

```python
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScript", "React", "Python"]
}

person_json = json.dumps(person, indent=4)
print(person_json)
```

### Save JSON

```python
with open("files/json_example.json", "w", encoding="utf-8") as f:
    json.dump(person, f, ensure_ascii=False, indent=4)
```

---

# 6. CSV Files

CSV means **Comma-Separated Values**.

```python
import csv

with open("files/csv_example.csv", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)

    for row in reader:
        print(row)
```

For structured CSV processing, `csv.DictReader` is also useful:

```python
with open("files/csv_example.csv", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(row["name"])
```

---

# 7. XLSX Files

This project uses `openpyxl`, which is a modern Python library for `.xlsx` files.

```python
from openpyxl import load_workbook

workbook = load_workbook("files/sample.xlsx")
sheet = workbook.active

for row in sheet.iter_rows(values_only=True):
    print(row)
```

The example workbook is generated automatically by `run_all.py` if it does not exist.

---

# 8. XML Files

Python's standard library can parse XML:

```python
import xml.etree.ElementTree as ET

tree = ET.parse("files/xml_example.xml")
root = tree.getroot()

print(root.tag)
print(root.attrib)

for child in root:
    print(child.tag)
```

---

# 💻 Exercises

## Level 1

### 1. Count lines and words

`count_lines_and_words()` reads a text source and returns:

```text
(lines, words)
```

The function accepts either a file path or a text string.

### 2. Ten most spoken languages

```python
most_spoken_languages("data/countries_data.json", 10)
```

Returns:

```text
[(count, language), ...]
```

### 3. Ten most populated countries

```python
most_populated_countries("data/countries_data.json", 10)
```

Returns dictionaries containing `country` and `population`.

---

## Level 2

### 4. Extract email addresses

```python
extract_emails("data/sample_emails.txt")
```

The implementation uses a regular expression and returns a list of addresses.

### 5. Most common words

```python
find_most_common_words("data/sample.txt", 10)
```

The function accepts either a file path or a string.

### 6. Frequent words in speeches

```python
find_most_frequent_words("data/obama_speech.txt", 10)
```

After downloading the original datasets, run the four speech analyses through:

```bash
python run_all.py
```

### 7. Text similarity

The solution contains:

- `clean_text()`
- `remove_support_words()`
- `check_text_similarity()`

The similarity metric used here is **Jaccard similarity**:

```text
|A ∩ B| / |A ∪ B|
```

This is a simple educational implementation, not a semantic NLP similarity model.

### 8. Romeo and Juliet

```python
find_most_common_words("data/sample_romeo_and_juliet.txt", 10)
```

### 9. Hacker News

The solution counts rows containing:

1. `python` / `Python`
2. `JavaScript` / `javascript` / `Javascript`
3. `Java` but not `JavaScript`

---

# ⬇️ Download the Original Datasets

Run:

```bash
python download_data.py
```

The script downloads the original Day 19 datasets into `data/`.

It attempts to retrieve:

- `countries_data.json`
- `obama_speech.txt`
- `michelle_obama_speech.txt`
- `donald_speech.txt`
- `melina_trump_speech.txt`
- `email_exchange_big.txt`
- `romeo_and_juliet.txt`
- `hacker_news.csv`
- `stop_words.py`

The URLs point to the upstream:

**Asabeneh/30-Days-Of-Python** repository.

If a dataset is unavailable or the network is blocked, the project continues to work with the included sample data.

---

# 🧪 Recommended Learning Order

1. Run `examples/file_handling_examples.py`
2. Read the TXT examples
3. Practice JSON
4. Practice CSV
5. Practice XLSX
6. Practice XML
7. Run Level 1 exercises
8. Run Level 2 exercises
9. Download the original datasets
10. Re-run the exercises with the original files
11. Modify the functions and test your own files

---

# 📌 Important Python Concepts Practiced

- `open()`
- Context managers (`with`)
- File modes
- `read()`
- `readline()`
- `readlines()`
- `splitlines()`
- `write()`
- `os.path.exists()`
- `os.remove()`
- `json.loads()`
- `json.dumps()`
- `json.load()`
- `json.dump()`
- `csv.reader()`
- `csv.DictReader()`
- `openpyxl`
- `xml.etree.ElementTree`
- Regular expressions
- `collections.Counter`
- Sorting with `key=`
- Sets and Jaccard similarity
- Functions and reusable modules
- Command-line execution

---

## Source

Lesson adapted from:

https://github.com/Asabeneh/30-Days-Of-Python

The original lesson is licensed under the terms of its upstream repository. This package is an educational implementation of the concepts and exercises.
