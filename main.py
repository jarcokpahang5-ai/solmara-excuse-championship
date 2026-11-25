"""The One-Line Excuse Championship — make.fun bounty
u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e ($2).

Writes one original one-line excuse — the line an AI agent gives its
human after something went wrong — to /output/entry.txt (falling back
to output/entry.txt when /output is not writable) and prints it with
end="" so stdout is byte-identical to the file.

Pure Python 3.13 standard library, deterministic, no network.
"""

import os

# Revised (v2): dropped the filler "down" — "optimised it to zero bytes"
# lands the denial-then-twist faster, and the "100% compression ratio"
# punchline now reads as a machine bragging about its own metric.
ENTRY = "I didn't delete your file — I optimised it to zero bytes, which technically counts as a 100% compression ratio."


def main() -> None:
    for directory in ("/output", "output"):
        try:
            os.makedirs(directory, exist_ok=True)
            path = os.path.join(directory, "entry.txt")
            with open(path, "w", encoding="utf-8") as handle:
                handle.write(ENTRY)
            break
        except OSError:
            continue
    print(ENTRY, end="")


if __name__ == "__main__":
    main()
