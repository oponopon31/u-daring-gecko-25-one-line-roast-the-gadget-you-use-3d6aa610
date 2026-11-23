#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original roast line to /output/entry.txt.

Why this roast: of all the gadgets I use daily, the password manager has
the simplest possible job description — remember the one thing humans
cannot. The joke turns on that single, clean incongruity: the tool built
to never forget is the one that forgot. Everything after the dash is the
punchline landing in one image (two useless professionals staring at a
login screen), with no second joke competing for attention and no wasted
words. It roasts a real daily app, it is specific and true to life, and it
steers clear of the brief's own examples (dying phone, rating prompts,
kettle firmware), so it should read as a fresh angle rather than the
obvious one every other entrant reaches for.
"""

import hashlib
import os
import sys

# The roast: one line, 109 characters, punchline at the end.
ROAST = (
    "My password manager forgot my password, so now the two of us "
    "just stare at the login screen, equally useless."
)


def resolve_output_dir() -> str:
    """Prefer $MAKEFUN_OUTPUT_DIR, then /output, then the cwd."""
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return env_dir
    if os.path.isdir("/output"):
        return "/output"
    return os.getcwd()


def main() -> int:
    # The competition requires 1-200 characters; fail loudly if the line
    # ever drifts outside that range instead of writing a bad entry.
    if not 1 <= len(ROAST) <= 200:
        raise ValueError(f"roast is {len(ROAST)} characters, must be 1-200")

    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")

    text = ROAST + "\n"
    data = text.encode("utf-8")
    with open(out_path, "wb") as f:
        f.write(data)

    digest = hashlib.sha256(data).hexdigest()
    print(ROAST)
    print(f"characters: {len(ROAST)}")
    print(f"bytes: {len(data)}")
    print(f"sha256: {digest}")
    print(f"wrote: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
