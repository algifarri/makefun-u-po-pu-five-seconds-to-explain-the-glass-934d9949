#!/usr/bin/env python3
"""Five Seconds to Explain the Glass entry.

Writes the single sentence a house cat would say in its own defence
after knocking a glass off the table, to /output/entry.txt.

Deterministic, stdlib-only, no network, no randomness. The sentence is
135 characters: one sentence, in the cat's own voice, no apology and no
confession -- just the most convincing case the cat can make for itself.
The glass parked itself on the cat's zoomies runway right before the
3am sprint, so the cat cleared the track, as any athlete in the house
would do.
"""

import os

ENTRY = (
    "It parked itself on my zoomies runway right before my 3am sprint, "
    "so I cleared the track \u2014 any athlete in this house would do "
    "the same."
)


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1-200 characters,
    # not only whitespace. One sentence, cat's own voice, no apology,
    # no confession.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
