"""Text cleaning, extraction, and word-frequency utilities."""

import re
from collections import Counter


def clean_text(text):
    """Remove characters other than letters and whitespace."""
    return re.sub(r"[^A-Za-z\s]", "", text)


def words(text):
    """Return lowercase words from text."""
    return re.findall(r"[A-Za-z]+", text.lower())


def most_frequent_words(text, limit=3):
    """Return the most common words and their frequencies."""
    return Counter(words(text)).most_common(limit)


def extract_integers(text):
    """Extract signed integers from a text string."""
    values = re.findall(r"-?\d+", text)
    return [int(value) for value in values]


def furthest_particle_distance(text):
    """Return the distance between the smallest and largest extracted point."""
    points = extract_integers(text)
    if not points:
        raise ValueError("No particle positions were found.")

    return max(points) - min(points)


if __name__ == "__main__":
    noisy = (
        "%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. "
        "There $is nothing; &as& mo@re rewarding as educa@ting &and& "
        "@emp%o@wering peo@ple."
    )

    cleaned = clean_text(noisy)
    print("Cleaned text:")
    print(cleaned)
    print("\nMost frequent words:")
    print(most_frequent_words(cleaned))

    particle_text = (
        "Particles are positioned at -12, -4, -3, -1, 0, 4 and 8."
    )
    print("\nParticle positions:", extract_integers(particle_text))
    print("Furthest distance:", furthest_particle_distance(particle_text))
