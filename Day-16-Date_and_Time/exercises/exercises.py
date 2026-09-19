"""Practice exercises based on the datetime module concepts."""

from datetime import datetime, date


def exercise_1():
    now = datetime.now()

    print("1. Current information")
    print("Day:", now.day)
    print("Month:", now.month)
    print("Year:", now.year)
    print("Hour:", now.hour)
    print("Minute:", now.minute)
    print("Timestamp:", now.timestamp())


def exercise_2():
    now = datetime.now()
    print("\n2. Formatted date:")
    print(now.strftime("%m/%d/%Y, %H:%M:%S"))


def exercise_3():
    date_string = "5 December, 2019"
    converted = datetime.strptime(date_string, "%d %B, %Y")

    print("\n3. Converted string:")
    print(converted)


def exercise_4():
    today = date.today()
    new_year = date(today.year + 1, 1, 1)

    print("\n4. Difference between today and New Year:")
    print(new_year - today)


def exercise_5():
    epoch = datetime(1970, 1, 1)
    now = datetime.now()

    print("\n5. Difference from January 1, 1970:")
    print(now - epoch)


def exercise_6():
    applications = [
        "Time-series analysis",
        "Application activity timestamps",
        "Blog post timestamps",
        "Event scheduling",
        "Elapsed-time calculations",
    ]

    print("\n6. Practical applications:")
    for application in applications:
        print("-", application)


if __name__ == "__main__":
    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()
    exercise_5()
    exercise_6()
