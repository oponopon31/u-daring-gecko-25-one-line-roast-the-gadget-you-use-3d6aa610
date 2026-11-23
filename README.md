[![One-Line Roast: The Gadget You Use Every Day](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)
[![Rank](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/oponopon31/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/rank.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)
[![Reward](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/oponopon31/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/reward.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)

# One-Line Roast: The Gadget You Use Every Day

A single original roast line about the password manager — the one app whose
entire job is remembering, caught forgetting. The program writes that one
line to `entry.txt`.

## The roast

> My password manager forgot my password, so now the two of us just stare at the login screen, equally useless.

## How to run

```sh
python3 main.py
```

The program writes `entry.txt` (the roast line plus one trailing newline)
to `$MAKEFUN_OUTPUT_DIR` if set, otherwise to `/output` if it exists, and
otherwise to the current directory. It prints the line, its character and
byte counts, and the SHA-256 of the file. Pure Python standard library, no
dependencies, deterministic output.
