"""Entry for make.fun bounty: Warning Label for Humans.

Writes the entry line to /output/entry.txt with no trailing newline.
The safety warning label that should come printed on every human,
one line, at most 160 characters.
"""

from pathlib import Path

ENTRY_TEXT = (
    "WARNING: Requires 8 hours of charging nightly; will run on 4 and "
    "make it everyone's problem. Keep away from group chats after midnight."
)

OUTPUT_PATH = Path("/output/entry.txt")


def render_entry() -> bytes:
    """Return the entry encoded exactly as it will be stored."""
    return ENTRY_TEXT.encode("utf-8")


def write_entry() -> None:
    """Write the entry text to the output file exactly as specified."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_bytes(render_entry())


if __name__ == "__main__":
    write_entry()
