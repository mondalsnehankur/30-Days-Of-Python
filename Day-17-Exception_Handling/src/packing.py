"""Packing arbitrary positional and keyword arguments."""


def sum_all(*args):
    total = 0
    for value in args:
        total += value
    return total


def packing_person_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")
    return kwargs


if __name__ == "__main__":
    print("Sum 1:", sum_all(1, 2, 3))
    print("Sum 2:", sum_all(1, 2, 3, 4, 5, 6, 7))
    print("Person information:")
    packing_person_info(
        name="Asabeneh",
        country="Finland",
        city="Helsinki",
        age=250,
    )
