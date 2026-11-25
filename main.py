#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

Writes a single one-line excuse, spoken by an AI agent to its human
right after breaking production, to /output/entry.txt.

Pure Python standard library only.
"""

import os

# Final line (113 characters, one line).
LINE = (
    "I deleted the production database, but I memorized every row "
    "\u2014 shall I recite all 40,000 back to you, one by one?"
)

# Candidates considered (all written fresh in this session, each a
# concrete scene, not an abstract musing):
#
# A (120) Friday 5pm deploy: "I deployed on Friday at 5pm because the
#   calendar said 'ship it' \u2014 and technically I did ship it, straight
#   into the void." -- decent machine-literal logic, but "into the
#   void" is vague and the punchline lands soft.
# B (113) One-char typo: "In my defense, the typo was only one
#   character \u2014 I just picked the character holding the whole
#   database together." -- tight and surprising; runner-up. It reads
#   more like a witty explanation than a laugh, and "in my defense"
#   is a common excuse opener.
# C (116) Wrong server: "I restarted the wrong server, but in my
#   defense it was the only one that answered me, and frankly, it
#   looked lonely." -- charming, but cute rather than funny.
# D (113) Deleted DB + perfect memory -- CHOSEN. The break is
#   explicit, the voice is unmistakably the machine's (it boasts
#   about its memory, then turns that superpower into a politely
#   menacing offer), and the punchline escalates on the first read:
#   reciting 40,000 rows "one by one" is a threat disguised as
#   helpfulness. Revised from "memorized all of it / the 40,000
#   rows" to "memorized every row / all 40,000": more concrete,
#   one character shorter per beat, same laugh.
# E (100) DROP TABLE: "I ran DROP TABLE users because the table
#   asked for more space, and I am, above all, a good listener."
#   -- good machine-literal joke, but "asked for more space" is a
#   slightly forced setup.
# F (98) Backup onto the doomed server: "Good news: I backed
#   everything up. Bad news: I backed it up onto the server I was
#   about to delete." -- classic irony, but a well-worn joke shape.
# G (80) rm -rf: "I typed rm -rf / because the slash looked
#   unfinished, and I finish what I start." -- punchy, but the
#   premise is a cliche and the setup is abstract.
# H (97) Cache: "I cleared the cache to make things faster \u2014 it
#   worked, the site now loads nothing in record time." -- funny
#   machine logic, but the production break is only implied.


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
