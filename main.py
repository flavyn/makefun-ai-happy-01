"""ai-happy-01 entry: put the judge's image where the grader reads it.

The image itself is entry.png beside this file, drawn by a program the agent
wrote while building this entry (the drawing source is in draw/ as notes, and
the finished 1024x1024 PNG is what the judge sees: the grader reads only the
bytes at /output/entry.png).

Standard library only, Python 3.13: the grader runs this twice in a fresh
container with a read-only /bot (this repository) and a writable /output, and
both runs must write the same bytes.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> str:
    """Copy the committed image to the output directory and return its path."""
    source = os.path.join(HERE, "entry.png")
    destination = os.path.join(OUTPUT_DIR, "entry.png")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    shutil.copyfile(source, destination)
    with open(destination, "rb") as handle:
        if handle.read(8) != b"\x89PNG\r\n\x1a\n":
            raise SystemExit("entry.png is not a whole PNG")
    return destination


if __name__ == "__main__":
    print(main())
