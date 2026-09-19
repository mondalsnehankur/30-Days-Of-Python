"""Basic operations with Python's datetime module."""

from datetime import datetime


def show_current_datetime():
    now = datetime.now()

    print("Current datetime:", now)
    print("Day:", now.day)
    print("Month:", now.month)
    print("Year:", now.year)
    print("Hour:", now.hour)
    print("Minute:", now.minute)
    print("Second:", now.second)
    print("Unix timestamp:", now.timestamp())


if __name__ == "__main__":
    show_current_datetime()
