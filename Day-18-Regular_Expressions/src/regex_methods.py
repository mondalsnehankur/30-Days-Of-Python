"""Core methods from Python's re module."""

import re


TEXT = """Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language."""


def match_example():
    match = re.match(r"I recommend", TEXT, re.I)
    return match.group() if match else None


def search_example():
    match = re.search(r"first", TEXT, re.I)
    return match.group() if match else None


def findall_example():
    return re.findall(r"python", TEXT, re.I)


def replace_example():
    return re.sub(r"Python", "JavaScript", TEXT, flags=re.I)


def split_example():
    return re.split(r"\n", TEXT)


if __name__ == "__main__":
    print("match():", match_example())
    print("search():", search_example())
    print("findall():", findall_example())
    print("sub():", replace_example())
    print("split():", split_example())
