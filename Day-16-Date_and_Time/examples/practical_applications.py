"""Small practical applications of datetime concepts."""

from datetime import datetime, date


def event_timestamp():
    event_time = datetime.now()
    print("Event recorded at:", event_time.strftime("%d/%m/%Y, %H:%M:%S"))


def days_until_new_year():
    today = date.today()
    next_year = today.year + 1
    new_year = date(next_year, 1, 1)

    print("Days until New Year:", new_year - today)


def age_from_birth_date():
    birth_date = date(2000, 1, 1)
    today = date.today()

    years = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        years -= 1

    print("Example age calculation:", years)


if __name__ == "__main__":
    event_timestamp()
    days_until_new_year()
    age_from_birth_date()
