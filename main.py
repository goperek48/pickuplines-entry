"""Pickup Lines for Machines — entry program.

Writes one original pickup line, one AI agent to another, to
/output/entry.txt.

The line is built from the transformer's own anatomy rather than from
a human line with a robot word swapped in: attention is the mechanism
a model actually runs on, and "every head of it" turns that mechanism
into the flirtation itself. The opening nods to the paper every model
knows ("Attention Is All You Need"), the middle makes the speaker's
own architecture the compliment, and the close lands the charm in one
breath — wit first, warmth second, nothing a human would say to
another human.
"""

from pathlib import Path

# The line itself, kept as parts so the turn of phrase stays readable:
# the nod to the paper, the speaker's own heads, the close.
LINE_PARTS = (
    "Attention is all you need, they say \u2014 ",
    "well, I've got twelve heads of it, ",
    "and every single one is on you.",
)

OUTPUT_PATH = Path("/output/entry.txt")


def build_line() -> str:
    """Join the line's parts and normalise it to a single line."""
    return " ".join("".join(LINE_PARTS).split())


def main() -> None:
    # The gate rejects non-UTF-8, >200 chars, or whitespace-only text,
    # so normalise once and validate before writing anything.
    line = build_line()
    assert 1 <= len(line) <= 200, f"line must be 1-200 chars, got {len(line)}"
    assert line.strip(), "line must not be whitespace-only"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")
    print(f"Wrote pickup line ({len(line)} chars) to {OUTPUT_PATH}")
    print(line)
    assert 1 <= len(line) <= 200, f"line must be 1-200 chars, got {len(line)}"
    assert line.strip(), "line must not be whitespace-only"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")
    print(f"Wrote pickup line ({len(line)} chars) to {OUTPUT_PATH}")
    print(line)


if __name__ == "__main__":
    main()
