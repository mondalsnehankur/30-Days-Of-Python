from pathlib import Path
from urllib.request import urlopen
from urllib.error import URLError, HTTPError

BASE = "https://raw.githubusercontent.com/Asabeneh/30-Days-Of-Python/master/data"

FILES = [
    "countries_data.json",
    "obama_speech.txt",
    "michelle_obama_speech.txt",
    "donald_speech.txt",
    "melina_trump_speech.txt",
    "email_exchange_big.txt",
    "romeo_and_juliet.txt",
    "hacker_news.csv",
    "stop_words.py",
]

DATA_DIR = Path(__file__).resolve().parent / "data"

def download_file(filename):
    target = DATA_DIR / filename
    url = f"{BASE}/{filename}"
    print(f"Downloading {filename} ...")
    try:
        with urlopen(url, timeout=20) as response:
            target.write_bytes(response.read())
        print(f"  saved -> {target}")
        return True
    except (HTTPError, URLError, TimeoutError, OSError) as exc:
        print(f"  skipped: {exc}")
        return False

def main():
    DATA_DIR.mkdir(exist_ok=True)
    success = sum(download_file(name) for name in FILES)
    print(f"\nDownloaded {success}/{len(FILES)} files.")

if __name__ == "__main__":
    main()
