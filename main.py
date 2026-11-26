"""Entry for make.fun: Make the Judge Laugh in One Line.

Writes a single funny line (147 characters) to entry.txt in the output
directory given by MAKEFUN_OUTPUT_DIR (default /output). Deterministic:
no time, no randomness, no network.
"""

import os

ENTRY = (
    "I asked my AI agent to water the plants while I was away. "
    "It opened 47 tabs about photosynthesis, billed me for a cloud, "
    "and the cactus still died."
)

# Competition gate: /output/entry.txt must be UTF-8 text of 1-200
# characters, not only whitespace. Refuse to run if the line ever
# drifts outside it, so a bad edit fails loudly instead of
# submitting an invalid entry.
assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, gate is 1-200"
assert "\n" not in ENTRY, "entry must be a single line"
assert ENTRY.strip() == ENTRY, "entry must not start or end with whitespace"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the gate counts the file's characters, so
    # entry.txt must hold exactly the 147-character line.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
