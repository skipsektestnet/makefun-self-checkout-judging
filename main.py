"""The Self-Checkout Is Judging You: writes the line to /output/entry.txt.

Why this line: it speaks in the machine's own error voice, and turns the
familiar 'unexpected item' alert onto the shopper's dignity.
"""

import os

# The entry itself: one line, punch at the end, no explanation.
ENTRY = 'Unexpected item in the bagging area: your dignity. Please remove it, scan it separately, and pay extra for the embarrassment.'

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    # Guard: never submit a blank entry to the sealed gate.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote entry.txt", len(ENTRY), "chars")


if __name__ == "__main__":
    main()
