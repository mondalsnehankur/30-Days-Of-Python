"""Examples of regular-expression patterns and metacharacters."""

import re


def character_sets():
    text = (
        "Apple and banana are fruits. An apple a day keeps the doctor away. "
        "Banana is also popular."
    )

    print("[Aa]pple:", re.findall(r"[Aa]pple", text))
    print("[Bb]anana:", re.findall(r"[Bb]anana", text))
    print("[A-Za-z0-9]:", re.findall(r"[A-Za-z0-9]+", text))


def digit_patterns():
    text = (
        "This regular expression example was made on December 6, "
        "2019 and revised on July 8, 2021"
    )

    print(r"\d:", re.findall(r"\d", text))
    print(r"\d+:", re.findall(r"\d+", text))
    print(r"\d{4}:", re.findall(r"\d{4}", text))
    print(r"\d{1,4}:", re.findall(r"\d{1,4}", text))


def optional_character():
    text = "email Email e-mail E-mail"
    print(r"[Ee]-?mail:", re.findall(r"[Ee]-?mail", text))


def anchors_and_negation():
    text = "This regular expression example ends here"
    print(r"^This:", re.findall(r"^This", text))
    print(r"[^A-Za-z ]+:", re.findall(r"[^A-Za-z ]+", "Hello, 123!"))


def quantifiers():
    text = "aa a aaa aaaaa"
    print(r"a*:", re.findall(r"a*", text))
    print(r"a+:", re.findall(r"a+", text))
    print(r"a{3}:", re.findall(r"a{3}", text))


if __name__ == "__main__":
    character_sets()
    digit_patterns()
    optional_character()
    anchors_and_negation()
    quantifiers()
