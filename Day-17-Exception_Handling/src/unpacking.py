"""Positional and dictionary argument unpacking."""


def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e


def unpack_list():
    numbers = [1, 2, 3, 4, 5]
    return sum_of_five_nums(*numbers)


def extended_unpacking():
    countries = ["Finland", "Sweden", "Norway", "Denmark", "Iceland"]
    first, second, *rest = countries
    return first, second, rest


def person_info(name, country, city, age):
    return f"{name} lives in {country}, {city}. Age: {age}."


def unpack_dictionary():
    person = {
        "name": "Asabeneh",
        "country": "Finland",
        "city": "Helsinki",
        "age": 250,
    }
    return person_info(**person)


if __name__ == "__main__":
    print("Sum:", unpack_list())
    print("Extended unpacking:", extended_unpacking())
    print(unpack_dictionary())
