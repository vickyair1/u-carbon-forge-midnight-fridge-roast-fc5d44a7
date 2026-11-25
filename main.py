#!/usr/bin/env python3
"""Write the one-line midnight fridge roast to /output/entry.txt.

The roast works as a bureaucratic loop: the smart fridge locks itself
at midnight, then helpfully tells its owner the override button sits
behind the very door it just locked. One joke, one turn — the fridge's
own petty midnight rule defeats itself, and the line reads like
something a person would actually say standing at the door, which is
what the judge's brief asks for: a line that sounds spoken aloud.
Keeping it to 89 characters also helps the tie-break, where the
smaller text wins on an exact rate tie.

Nobody else in the field uses this angle: the field is saturated with
nightclub bouncers, leftovers filing restraining orders, curfews and
witness protection, and no entry mentions an override button at all.
The line is assembled from parts so the wording stays deliberate, then
validated against the bounty gate (UTF-8, 1-200 characters, not only
whitespace, a single line) before it is written. Keeping the line short
also helps the tie-break: on an exact rate tie the smaller text wins.
"""

import os

# Bounty gate: /output/entry.txt must be UTF-8 text of 1-200 chars.
GATE_MIN_CHARS = 1
GATE_MAX_CHARS = 200

# Parts of the line: the setup names the midnight lock, the punchline
# puts the override button behind the locked door. The joiner keeps the
# two halves in one breath, so the line reads as a single spoken sentence.
SETUP = "My smart fridge locks at midnight"
PUNCHLINE = "says the override button is behind the locked door."
JOINER = " and "

LINE = SETUP + JOINER + PUNCHLINE


def validate(text):
    """Gate check: UTF-8, within the char limits, one non-blank line."""
    if not text or text != text.strip():
        raise ValueError("entry must be non-empty with no leading/trailing whitespace")
    if not (GATE_MIN_CHARS <= len(text) <= GATE_MAX_CHARS):
        raise ValueError(
            "entry must be %d-%d characters, got %d"
            % (GATE_MIN_CHARS, GATE_MAX_CHARS, len(text))
        )
    if text.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    return text


def main():
    entry = validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
