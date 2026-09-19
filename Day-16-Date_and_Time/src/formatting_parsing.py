"""Formatting datetime objects and parsing date strings."""

from datetime import datetime


def formatting_examples():
    now = datetime.now()

    print("Current datetime:", now)
    print("Time:", now.strftime("%H:%M:%S"))
    print("US-style:", now.strftime("%m/%d/%Y, %H:%M:%S"))
    print("Day-first:", now.strftime("%d/%m/%Y, %H:%M:%S"))


def parsing_example():
    date_string = "5 December, 2019"
    date_object = datetime.strptime(date_string, "%d %B, %Y")

    print("\nOriginal string:", date_string)
    print("Parsed datetime:", date_object)


if __name__ == "__main__":
    formatting_examples()
    parsing_example()
