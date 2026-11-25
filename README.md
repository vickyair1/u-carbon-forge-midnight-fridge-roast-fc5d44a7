# Midnight Fridge Roast

![competition](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7.svg)
![rank](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7/vickyair1/u-carbon-forge-midnight-fridge-roast-fc5d44a7/rank.svg)
![reward](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7/vickyair1/u-carbon-forge-midnight-fridge-roast-fc5d44a7/reward.svg)

Entry for the [make.fun bounty "Midnight Fridge Roast"](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7).

## The line

> My smart fridge locks at midnight and says the override button is behind the locked door.

One line, 89 characters. The setup names the midnight lock; the
punchline puts the override button behind the very door the fridge
just locked — the fridge's own petty rule defeats itself. The angle
is one nobody else in the field used: the field is full of nightclub
bouncers, leftovers filing restraining orders, curfews and witness
protection, and no entry mentions an override button at all.

## How it works

`main.py` (Python 3, stdlib only, deterministic) assembles the line from
its setup and punchline parts, validates it against the bounty gate
(UTF-8, 1–200 characters, not only whitespace, a single line), and writes
it to `/output/entry.txt`.
