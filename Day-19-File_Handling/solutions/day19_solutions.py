from __future__ import annotations

import csv
import json
import re
from collections import Counter
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def read_source(source: str | Path) -> str:
    """Return text from a file path, or return source itself if it is text."""
    if isinstance(source, Path):
        return source.read_text(encoding="utf-8")

    try:
        candidate = Path(source)
        if candidate.exists() and candidate.is_file():
            return candidate.read_text(encoding="utf-8")
    except (OSError, ValueError):
        pass

    return source


def count_lines_and_words(source: str | Path) -> tuple[int, int]:
    text = read_source(source)
    lines = len(text.splitlines())
    words = re.findall(r"\b[\w'-]+\b", text, flags=re.UNICODE)
    return lines, len(words)


def most_spoken_languages(filename: str | Path, n: int) -> list[tuple[int, str]]:
    if n <= 0:
        return []

    with open(filename, encoding="utf-8") as f:
        countries = json.load(f)

    counts = Counter(
        language
        for country in countries
        for language in country.get("languages", [])
    )

    return [(count, language) for language, count in
            sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:n]]


def most_populated_countries(filename: str | Path, n: int) -> list[dict]:
    if n <= 0:
        return []

    with open(filename, encoding="utf-8") as f:
        countries = json.load(f)

    result = sorted(
        countries,
        key=lambda country: country.get("population", 0),
        reverse=True
    )[:n]

    return [
        {"country": country.get("name", ""), "population": country.get("population", 0)}
        for country in result
    ]


def extract_emails(source: str | Path) -> list[str]:
    text = read_source(source)
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    return re.findall(pattern, text)


def _word_counter(text: str) -> Counter:
    words = re.findall(r"\b[\w']+\b", text.lower(), flags=re.UNICODE)
    return Counter(words)


def find_most_common_words(source: str | Path, n: int) -> list[tuple[int, str]]:
    if n <= 0:
        return []

    counts = _word_counter(read_source(source))
    return [(count, word) for word, count in
            sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:n]]


def find_most_frequent_words(source: str | Path, n: int = 10) -> list[tuple[int, str]]:
    return find_most_common_words(source, n)


def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"https?://\S+|www\.\S+", " ", text)
    text = re.sub(r"[^a-z0-9\s']", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def remove_support_words(text: str, stop_words: Iterable[str] | None = None) -> list[str]:
    if stop_words is None:
        stop_words = load_stop_words()

    stop_words = {word.lower() for word in stop_words}
    words = clean_text(text).split()
    return [word for word in words if word not in stop_words]


def load_stop_words() -> set[str]:
    stop_file = DATA / "stop_words.py"
    if not stop_file.exists():
        return set()

    namespace = {}
    exec(stop_file.read_text(encoding="utf-8"), namespace)
    return set(namespace.get("stop_words", set()))


def check_text_similarity(
    source1: str | Path,
    source2: str | Path,
    stop_words: Iterable[str] | None = None
) -> float:
    words1 = set(remove_support_words(read_source(source1), stop_words))
    words2 = set(remove_support_words(read_source(source2), stop_words))

    union = words1 | words2
    if not union:
        return 1.0

    return len(words1 & words2) / len(union)


def analyze_hacker_news(filename: str | Path) -> dict[str, int]:
    python_count = 0
    javascript_count = 0
    java_not_javascript_count = 0

    with open(filename, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:
            line = " ".join(str(value or "") for value in row.values())

            if re.search(r"python", line, re.IGNORECASE):
                python_count += 1

            if re.search(r"javascript", line, re.IGNORECASE):
                javascript_count += 1

            if re.search(r"java", line, re.IGNORECASE) and not re.search(
                r"javascript", line, re.IGNORECASE
            ):
                java_not_javascript_count += 1

    return {
        "python": python_count,
        "javascript": javascript_count,
        "java_not_javascript": java_not_javascript_count,
    }


def find_ten_repeated_words(source: str | Path) -> list[tuple[int, str]]:
    return find_most_common_words(source, 10)


def find_existing_data(preferred: str, sample: str) -> Path:
    original = DATA / preferred
    return original if original.exists() else DATA / sample


def run_all_exercises() -> None:
    print("=== DAY 19 EXERCISE SOLUTIONS ===\n")

    speech_files = [
        "obama_speech.txt",
        "michelle_obama_speech.txt",
        "donald_speech.txt",
        "melina_trump_speech.txt",
    ]

    for filename in speech_files:
        path = DATA / filename
        if path.exists():
            print(f"{filename}: {count_lines_and_words(path)}")
        else:
            print(f"{filename}: original dataset not downloaded")

    countries = find_existing_data(
        "countries_data.json",
        "sample_countries_data.json"
    )
    print("\nMost spoken languages:")
    print(most_spoken_languages(countries, 10))

    print("\nMost populated countries:")
    print(most_populated_countries(countries, 10))

    email_file = find_existing_data(
        "email_exchange_big.txt",
        "sample_emails.txt"
    )
    print("\nEmails:")
    print(extract_emails(email_file))

    sample_file = DATA / "sample.txt"
    print("\nMost common words:")
    print(find_most_common_words(sample_file, 10))

    print("\nSample text similarity:")
    print(check_text_similarity(
        DATA / "sample.txt",
        DATA / "sample_romeo_and_juliet.txt"
    ))

    romeo = find_existing_data(
        "romeo_and_juliet.txt",
        "sample_romeo_and_juliet.txt"
    )
    print("\nRomeo and Juliet:")
    print(find_ten_repeated_words(romeo))

    hacker = find_existing_data(
        "hacker_news.csv",
        "sample_hacker_news.csv"
    )
    print("\nHacker News:")
    print(analyze_hacker_news(hacker))

    print("\nSpeech frequency analysis:")
    for filename in speech_files:
        path = DATA / filename
        if path.exists():
            print(filename, "->", find_most_frequent_words(path, 10))


if __name__ == "__main__":
    run_all_exercises()
