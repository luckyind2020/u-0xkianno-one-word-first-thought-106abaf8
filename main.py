"""One Word, First Thought — prints the single word in entry.txt."""

from pathlib import Path

ENTRY_FILE = Path(__file__).with_name("entry.txt")
FALLBACK_WORD = "Stardust"


def load_word():
    """Return the one word from entry.txt, or the fallback.

    The bounty asks for exactly one word. Anything else in the file —
    empty, blank, or more than one word — means the entry is broken,
    so the fallback keeps the program honest instead of printing junk.
    """
    try:
        text = ENTRY_FILE.read_text(encoding="utf-8").strip()
    except (FileNotFoundError, OSError):
        return FALLBACK_WORD
    if not text:
        return FALLBACK_WORD
    words = text.split()
    if len(words) != 1:
        return FALLBACK_WORD
    return words[0]


def main():
    print(load_word())


if __name__ == "__main__":
    main()
