"""Working with date and time objects."""

from datetime import date, time


def date_examples():
    specific_date = date(2020, 1, 1)
    today = date.today()

    print("Specific date:", specific_date)
    print("Today's date:", today)
    print("Current year:", today.year)
    print("Current month:", today.month)
    print("Current day:", today.day)


def time_examples():
    empty_time = time()
    standard_time = time(10, 30, 50)
    named_time = time(hour=10, minute=30, second=50)
    precise_time = time(10, 30, 50, 200555)

    print("\nDefault time:", empty_time)
    print("Standard time:", standard_time)
    print("Named arguments:", named_time)
    print("With microseconds:", precise_time)


if __name__ == "__main__":
    date_examples()
    time_examples()
