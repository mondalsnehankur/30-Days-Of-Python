# 30 Days of Python — Day 7: Sets

## 📘 Day 7 — Sets

This folder contains my **Day 7** work from the **30 Days of Python** challenge.

The topic covered in this section is **Sets in Python**, including creating sets, modifying sets, set operations, and mathematical relationships between sets.

---

## 📚 Topics Covered

* Creating a Set
* Getting Set's Length
* Accessing Items in a Set
* Checking an Item
* Adding Items to a Set
* Removing Items from a Set
* Clearing Items in a Set
* Deleting a Set
* Converting a List to a Set
* Joining Sets
* Union
* Update
* Intersection
* Subset
* Superset
* Difference
* Symmetric Difference
* Disjoint Sets
* Practical Set Operations

---

## 🔹 What is a Set?

A **set** is an unordered collection of unique elements.

Unlike lists and tuples:

* Sets do not allow duplicate elements.
* Sets are unordered.
* Sets do not support indexing.
* Sets are mutable.
* Sets support mathematical operations such as union, intersection, difference, and symmetric difference.

Example:

```python
fruits = {'banana', 'orange', 'mango', 'lemon'}
```

Duplicate values are automatically removed:

```python
numbers = {1, 2, 2, 3, 3, 4}

print(numbers)
```

Output:

```text
{1, 2, 3, 4}
```

> The order of elements displayed in a set should not be relied upon.

---

# 1. Creating a Set

An empty set can be created using `set()`.

```python
empty_set = set()
```

An important distinction:

```python
empty_set = {}
```

creates an **empty dictionary**, not an empty set.

A set with values can be created using curly braces:

```python
fruits = {'banana', 'orange', 'mango', 'lemon'}
```

---

# 2. Getting Set's Length

The `len()` function returns the number of elements in a set.

```python
fruits = {'banana', 'orange', 'mango', 'lemon'}

print(len(fruits))
```

Output:

```text
4
```

---

# 3. Accessing Items in a Set

Sets are unordered and do not have indexes.

Therefore, this is not valid:

```python
fruits[0]
```

Instead, use a loop:

```python
for fruit in fruits:
    print(fruit)
```

---

# 4. Checking an Item

The `in` operator can be used to check whether an element exists in a set.

```python
fruits = {'banana', 'orange', 'mango', 'lemon'}

print('mango' in fruits)
```

Output:

```text
True
```

Example:

```python
print('apple' in fruits)
```

Output:

```text
False
```

---

# 5. Adding Items to a Set

## `add()`

The `add()` method adds a single element.

```python
fruits = {'banana', 'orange', 'mango', 'lemon'}

fruits.add('lime')

print(fruits)
```

---

## `update()`

The `update()` method adds multiple elements.

```python
fruits = {'banana', 'orange', 'mango', 'lemon'}

vegetables = {
    'tomato',
    'potato',
    'cabbage'
}

fruits.update(vegetables)

print(fruits)
```

---

# 6. Removing Items from a Set

## `remove()`

`remove()` removes a specific element.

```python
fruits.remove('banana')
```

If the element does not exist, `remove()` raises a `KeyError`.

---

## `discard()`

`discard()` also removes an element, but does not raise an error if the element is absent.

```python
fruits.discard('apple')
```

---

## `pop()`

`pop()` removes and returns an arbitrary element.

```python
removed_item = fruits.pop()

print(removed_item)
```

Because sets are unordered, you should not assume which element will be removed.

---

# 7. Clearing Items in a Set

The `clear()` method removes all elements from a set.

```python
fruits = {'banana', 'orange', 'mango', 'lemon'}

fruits.clear()

print(fruits)
```

Output:

```text
set()
```

The set still exists; it is simply empty.

---

# 8. Deleting a Set

The `del` keyword deletes the set itself.

```python
fruits = {'banana', 'orange', 'mango', 'lemon'}

del fruits
```

After deletion, attempting to access `fruits` results in:

```text
NameError
```

---

# 9. Converting a List to a Set

A list can be converted into a set using `set()`.

This is particularly useful for removing duplicates.

```python
fruits = [
    'banana',
    'orange',
    'mango',
    'orange',
    'banana'
]

fruits = set(fruits)

print(fruits)
```

The duplicate values are removed automatically.

### Important

Since sets are unordered, the resulting order should not be relied upon.

---

# 10. Joining Sets — Union

Union combines all unique elements from two sets.

## Using `union()`

```python
fruits = {'banana', 'orange', 'mango', 'lemon'}

vegetables = {
    'tomato',
    'potato',
    'cabbage'
}

result = fruits.union(vegetables)

print(result)
```

## Using `|`

The same operation can be performed using the `|` operator.

```python
result = fruits | vegetables
```

Mathematically:

```text
A ∪ B
```

---

# 11. Update

Unlike `union()`, which creates a new set, `update()` modifies the original set.

```python
fruits = {'banana', 'orange', 'mango'}

vegetables = {'tomato', 'potato'}

fruits.update(vegetables)

print(fruits)
```

The elements of `vegetables` are added directly to `fruits`.

---

# 12. Intersection

Intersection returns elements that are common to both sets.

## Using `intersection()`

```python
whole_numbers = {
    0, 1, 2, 3, 4,
    5, 6, 7, 8, 9, 10
}

even_numbers = {
    0, 2, 4, 6, 8, 10
}

result = whole_numbers.intersection(even_numbers)

print(result)
```

Output:

```text
{0, 2, 4, 6, 8, 10}
```

## Using `&`

```python
result = whole_numbers & even_numbers
```

Mathematically:

```text
A ∩ B
```

---

# 13. Subset

A set is a **subset** of another set if every element of the first set exists in the second set.

```python
whole_numbers = {
    0, 1, 2, 3, 4,
    5, 6, 7, 8, 9, 10
}

even_numbers = {
    0, 2, 4, 6, 8, 10
}

print(even_numbers.issubset(whole_numbers))
```

Output:

```text
True
```

The operator `<=` can also be used:

```python
print(even_numbers <= whole_numbers)
```

---

# 14. Superset

A set is a **superset** if it contains all elements of another set.

```python
print(whole_numbers.issuperset(even_numbers))
```

Output:

```text
True
```

The `>=` operator can also be used:

```python
print(whole_numbers >= even_numbers)
```

### Relationship

If:

```text
B ⊆ A
```

then:

```text
A ⊇ B
```

---

# 15. Difference

Difference returns the elements that exist in one set but not in the other.

```python
whole_numbers = {
    0, 1, 2, 3, 4,
    5, 6, 7, 8, 9, 10
}

even_numbers = {
    0, 2, 4, 6, 8, 10
}

print(whole_numbers.difference(even_numbers))
```

Output:

```text
{1, 3, 5, 7, 9}
```

The `-` operator can also be used:

```python
print(whole_numbers - even_numbers)
```

Mathematically:

```text
A − B
```

means elements present in `A` but not in `B`.

---

# 16. Symmetric Difference

Symmetric difference returns elements that belong to either set, but **not both**.

It can be represented mathematically as:

```text
(A − B) ∪ (B − A)
```

Example:

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.symmetric_difference(B))
```

Output:

```text
{1, 2, 5, 6}
```

The `^` operator can also be used:

```python
print(A ^ B)
```

---

# 17. Disjoint Sets

Two sets are **disjoint** if they have no elements in common.

The `isdisjoint()` method checks this.

```python
even_numbers = {0, 2, 4, 6, 8}

odd_numbers = {1, 3, 5, 7, 9}

print(even_numbers.isdisjoint(odd_numbers))
```

Output:

```text
True
```

Because no number exists in both sets.

Example with overlapping sets:

```python
A = {1, 2, 3}
B = {3, 4, 5}

print(A.isdisjoint(B))
```

Output:

```text
False
```

because `3` is common to both sets.

---

# 📊 Set Operations Quick Reference

| Operation            | Method                   | Operator |
| -------------------- | ------------------------ | -------- |
| Union                | `union()`                | `\|`     |
| Intersection         | `intersection()`         | `&`      |
| Difference           | `difference()`           | `-`      |
| Symmetric Difference | `symmetric_difference()` | `^`      |
| Subset               | `issubset()`             | `<=`     |
| Superset             | `issuperset()`           | `>=`     |
| Disjoint             | `isdisjoint()`           | —        |

---

# 🔬 Practical Example

The program also contains a practical example involving students enrolled in Python and Java courses.

```python
python_students = {
    'Snehankur',
    'Rahul',
    'Ankit',
    'Priya',
    'Neha'
}

java_students = {
    'Rahul',
    'Ankit',
    'Riya',
    'Neha'
}
```

### Students in either course

```python
python_students | java_students
```

### Students in both courses

```python
python_students & java_students
```

### Students only in Python

```python
python_students - java_students
```

### Students only in Java

```python
java_students - python_students
```

### Students in exactly one course

```python
python_students ^ java_students
```

This demonstrates how Python sets can be used for real-world data comparison.

---

# 🧠 Important Concepts Learned

Through this program, the following Python concepts are practiced:

* Set creation
* Set uniqueness
* Set length
* Iteration
* Membership operators
* `add()`
* `update()`
* `remove()`
* `discard()`
* `pop()`
* `clear()`
* `del`
* List-to-set conversion
* Union
* Intersection
* Difference
* Symmetric difference
* Subsets
* Supersets
* Disjoint sets
* Set operators

---

# 📂 Project Structure

```text
07_Day_Sets/
│
├── day7_sets.py
└── README.md
```

---

# ▶️ How to Run

Make sure Python is installed.

Run the program using:

```bash
python day7_sets.py
```

For systems where `python3` is required:

```bash
python3 day7_sets.py
```

---

# ⚠️ Important Notes

### Sets do not support indexing

This is invalid:

```python
fruits[0]
```

Use iteration instead:

```python
for fruit in fruits:
    print(fruit)
```

### Sets contain unique elements

```python
numbers = {1, 1, 2, 2, 3}
```

becomes:

```text
{1, 2, 3}
```

### `remove()` vs `discard()`

| Method      | Missing item      |
| ----------- | ----------------- |
| `remove()`  | Raises `KeyError` |
| `discard()` | Does nothing      |

### `clear()` vs `del`

```python
fruits.clear()
```

empties the set but keeps the variable.

```python
del fruits
```

deletes the variable itself.

---

# 💻 Exercises

The original Day 7 challenge contains exercises at three levels:

* Exercises — Level 1
* Exercises — Level 2
* Exercises — Level 3

These can be added as separate practice solutions after completing the concepts demonstrated in `day7_sets.py`.

---

# 🎯 Learning Outcome

After completing Day 7, I can:

* Create and manipulate Python sets.
* Remove duplicate values from collections.
* Check membership efficiently.
* Add and remove set elements.
* Perform mathematical set operations.
* Find common and unique elements between collections.
* Determine subset and superset relationships.
* Determine whether two sets are disjoint.
* Apply set operations to practical programming problems.

---

# 🌕 Day 7 Completed

**30 Days of Python — Day 7: Sets**

> One more day completed and one step further in the journey of learning Python.

---
