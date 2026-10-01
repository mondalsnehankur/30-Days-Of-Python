from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from examples.file_handling_examples import xlsx_examples
from solutions.day19_solutions import run_all_exercises

if __name__ == "__main__":
    print("=" * 60)
    print("DAY 19 — FILE HANDLING")
    print("=" * 60)

    print("\nRunning lesson examples...\n")
    from examples.file_handling_examples import (
        text_examples, write_examples, json_examples,
        csv_examples, xml_examples, deletion_example
    )

    text_examples()
    write_examples()
    json_examples()
    csv_examples()
    xlsx_examples()
    xml_examples()
    deletion_example()

    print("\n" + "=" * 60)
    run_all_exercises()
