#!/usr/bin/env python3
"""Make the AI judge feel curious.

Writes one short text to /output/entry.txt: a quiet doorway, a sentence
that knows the reader's name, and a choice left open. No network, no
input, no randomness -- the same bytes on every run.
"""

import os

TEXT = (
    "Behind a door you have never opened, a sentence waits that you have "
    "never read. It is short. It knows your name. You can hear it "
    "breathing, patient as rain on a tin roof. The handle is warm. Turn "
    "it, and the night changes. Leave it, and you will wonder all night "
    "what it says."
)


def main() -> None:
    # Self-check the gate before writing: 1-280 Unicode code points,
    # not only white space. Fail loudly instead of shipping bad output.
    if not 1 <= len(TEXT) <= 280 or not TEXT.strip():
        raise SystemExit("entry text fails the 1-280 character gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
