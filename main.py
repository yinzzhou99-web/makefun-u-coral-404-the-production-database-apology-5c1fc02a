"""The Production Database Apology — one line to /output/entry.txt.

Pure stdlib, no network, deterministic. The output directory is left in
place; only what sits inside it is removed before the entry is written.
"""

import os
import shutil

LINE = "Good news: I deleted the production database. Bad news: I did it with the confidence of someone who had a backup. I did not have a backup."

OUT = "/output"


def empty(directory):
    for name in os.listdir(directory):
        path = os.path.join(directory, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.unlink(path)


def main():
    if not LINE.strip() or len(LINE) > 200:
        raise ValueError("entry line must be 1-200 non-blank characters")
    os.makedirs(OUT, exist_ok=True)
    empty(OUT)
    with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    os.chmod(os.path.join(OUT, "entry.txt"), 0o644)


if __name__ == "__main__":
    main()
