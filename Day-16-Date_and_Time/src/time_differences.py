"""Calculating differences between dates and using timedelta."""

from datetime import date, datetime, timedelta


def date_difference():
    today = date(2019, 12, 5)
    new_year = date(2020, 1, 1)

    difference = new_year - today

    print("Date difference:", difference)


def datetime_difference():
    first = datetime(2019, 12, 5, 0, 59, 0)
    second = datetime(2020, 1, 1, 0, 0, 0)

    difference = second - first

    print("Datetime difference:", difference)


def timedelta_example():
    first = timedelta(weeks=12, days=10, hours=4, seconds=20)
    second = timedelta(days=7, hours=5, minutes=3, seconds=30)

    result = first - second

    print("Timedelta result:", result)


if __name__ == "__main__":
    date_difference()
    datetime_difference()
    timedelta_example()
