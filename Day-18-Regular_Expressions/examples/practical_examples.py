"""Practical applications of regular expressions."""

import re
from pathlib import Path


def extract_years(text):
    """Extract four-digit years."""
    return re.findall(r"\b\d{4}\b", text)


def find_emails(text):
    """Extract basic email-like patterns."""
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    return re.findall(pattern, text)


def clean_percent_symbols(text):
    """Remove percent signs from noisy text."""
    return re.sub(r"%", "", text)


def validate_python_variable(name):
    """Validate the basic Python identifier pattern from the exercise."""
    return bool(re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", name))


def split_lines(text):
    """Split text into separate lines."""
    return re.split(r"\n", text)


if __name__ == "__main__":
    sample = (
        "The project started in 2019 and was revised in 2021. "
        "Contact test@example.com for details."
    )

    print("Years:", extract_years(sample))
    print("Emails:", find_emails(sample))
    print("Valid variable:", validate_python_variable("first_name"))
    print("Invalid variable:", validate_python_variable("1first_name"))
    print("Lines:", split_lines("one\ntwo\nthree"))

    noisy = "%I a%m a% student."
    print("Cleaned:", clean_percent_symbols(noisy))
