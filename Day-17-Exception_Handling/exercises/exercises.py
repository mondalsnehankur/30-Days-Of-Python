"""Day 17 exercise from the provided reference material."""


def country_unpacking_exercise():
    names = [
        "Finland",
        "Sweden",
        "Norway",
        "Denmark",
        "Iceland",
        "Estonia",
        "Russia",
    ]

    # First five countries -> nordic_countries.
    *nordic_countries, es, ru = names

    print("Nordic countries:", nordic_countries)
    print("Estonia:", es)
    print("Russia:", ru)


if __name__ == "__main__":
    country_unpacking_exercise()
