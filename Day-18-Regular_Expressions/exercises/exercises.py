"""Completed exercises from Day 18: Regular Expressions."""

import re
from collections import Counter


PARAGRAPH = (
    "I love teaching. If you do not love teaching what else can you love. "
    "I love Python if you do not love something which can give you all the "
    "capabilities to develop an application what else can you love."
)

NOISY_SENTENCE = (
    "%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. "
    "There $is nothing; &as& mo@re rewarding as educa@ting &and& "
    "@emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting "
    "tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?"
)


def level_1_most_frequent_word():
    words = re.findall(r"[A-Za-z]+", PARAGRAPH)
    frequency = Counter(words)
    return frequency.most_common()


def level_1_particle_distance():
    text = (
        "The particle positions are -12, -4, -3, -1, 0, 4 and 8 "
        "on the horizontal x-axis."
    )

    points = [int(value) for value in re.findall(r"-?\d+", text)]
    return max(points) - min(points)


def level_2_is_valid_variable(name):
    pattern = r"^[A-Za-z_][A-Za-z0-9_]*$"
    return bool(re.fullmatch(pattern, name))


def level_3_clean_text(text):
    return re.sub(r"[^A-Za-z\s]", "", text)


def level_3_most_frequent_words(text):
    words = re.findall(r"[A-Za-z]+", text)
    return Counter(words).most_common(3)


if __name__ == "__main__":
    print("LEVEL 1 — Most frequent words")
    print(level_1_most_frequent_word())

    print("\nLEVEL 1 — Furthest particle distance")
    print(level_1_particle_distance())

    print("\nLEVEL 2 — Variable validation")
    for name in ["first_name", "first-name", "1first_name", "firstname"]:
        print(f"{name}: {level_2_is_valid_variable(name)}")

    print("\nLEVEL 3 — Cleaned text")
    cleaned = level_3_clean_text(NOISY_SENTENCE)
    print(cleaned)

    print("\nLEVEL 3 — Three most frequent words")
    print(level_3_most_frequent_words(cleaned))
