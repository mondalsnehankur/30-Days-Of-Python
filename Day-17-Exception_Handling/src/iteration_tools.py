"""Examples of spreading, enumerate, and zip."""


def spreading_example():
    first = [1, 2, 3]
    second = [4, 5, 6, 7]
    return [0, *first, *second]


def enumerate_example():
    countries = ["Finland", "Sweden", "Norway", "Denmark", "Iceland"]

    for index, country in enumerate(countries):
        print(index, country)


def find_country(target):
    countries = ["Finland", "Sweden", "Norway", "Denmark", "Iceland"]

    for index, country in enumerate(countries):
        if country == target:
            return index

    return None


def zip_example():
    fruits = ["banana", "orange", "mango", "lemon", "lime"]
    vegetables = ["Tomato", "Potato", "Cabbage", "Onion", "Carrot"]

    return [
        {"fruit": fruit, "veg": vegetable}
        for fruit, vegetable in zip(fruits, vegetables)
    ]


if __name__ == "__main__":
    print("Spread:", spreading_example())
    enumerate_example()
    print("Finland index:", find_country("Finland"))
    print("Zipped data:", zip_example())
