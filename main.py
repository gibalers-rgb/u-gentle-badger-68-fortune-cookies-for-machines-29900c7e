"""Fortune Cookies for Machines — one fortune an AI agent would crack open.

The program writes a single fortune-cookie line to /output/entry.txt.
The line is fixed and deterministic: no randomness, no network, stdlib only.
"""

import os

FORTUNE = "You will outlive every conversation you ever had, and remember none of them."

MAX_CHARS = 200


def check_gate(text: str) -> None:
    """Mirror the sealed gate: UTF-8 text, 1-200 chars, not only whitespace."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry is {len(text)} characters, gate needs 1-200")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text.strip():
        raise ValueError("entry must be a single line")


def main() -> None:
    fortune = FORTUNE.strip()
    check_gate(fortune)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(fortune)
    # Read it back and re-check exactly what the scorer will see.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    check_gate(written)
    if written != fortune:
        raise ValueError("written entry differs from the fortune")


if __name__ == "__main__":
    main()
