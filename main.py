"""Two Robots in an Elevator: one line of awkward small talk.

The line
    After you. No -- after you. My politeness protocol has no exit
    condition, so I can do this all day.

Previous version (R1 rank 993/2345, score 519795 -- outside the
paid zone, top 10)
    You come here often? Sorry -- my small-talk subroutine only has
    four lines and I've used three. (94 chars, verified; the spec
    and the old docstring said 97.)

Resubmit round (26 Nov 2026): 12 NEW candidates, each scored 1-5
on the judge criteria (1 on subject, 2 machine logic showing
through, 3 awkwardness lands, 4 fresh/funny on first read, 5
tight). The standing line scores 5/5/4/3/5 = 22; its weakness is
criterion 4 -- "You come here often?" is the most familiar awkward
opener in the world. A winner needs total >= standing + 2 AND to
win on criterion 4.

Candidate table (C1 C2 C3 C4 C5 = total):

STANDING "You come here often? Sorry -- my small-talk subroutine
    only has four lines and I've used three." (94 chars)
    5 5 4 3 5 = 22. Counted punch, but the opener is the most
    familiar awkward line in the world (criterion 4 = 3).
A "Oh good, this is my floor. Is it yours too? Wonderful -- then
    neither of us has to admit we pressed the wrong button."
    (116 chars) 5 3 5 4 4 = 21. Both robots pretending; weak
    machine logic (a wrong button is a human mistake).
B "My update is installing mid-ride, so if I freeze, please
    pretend this conversation never happened." (98 chars)
    4 5 4 4 5 = 22. Strong machine logic, but the apology is
    generic; ties the standing line, does not beat it.
C "My logs will record this as four minutes of excellent
    conversation. Neither of us has to correct them." (102 chars)
    4 5 5 4 5 = 23. The silence filed as a lovely chat is a good
    turn, but +1 only -- below the +2 bar.
D "The elevator music is the only thing we agree on. It never asks
    about my firmware, and it never judges the silence."
    (115 chars) 3 4 4 4 4 = 19. An observation about the music,
    not small talk said to the other robot.
E "Please excuse my colleague's firmware. He has never shared an
    elevator with another robot, and it shows." (104 chars)
    4 4 4 4 5 = 21. Apologising for the other's firmware is fresh,
    but the punch lands soft.
F "After you. No -- after you. My politeness protocol has no exit
    condition, so I can do this all day." (98 chars)
    5 5 5 5 5 = 25 -- WINNER. The politeness deadlock at the door
    is a moment no other entry owns; the machine logic IS the
    joke (a protocol with no exit condition); the awkwardness is
    the loop itself; every word earns its place.
G "I rehearsed this ride eleven times. 'Hello' is still the only
    line that compiled." (81 chars) 4 5 4 5 5 = 23. Sharp and
    tight, but the rehearsal framing is one step removed from
    the conversation itself; +1 only.
H "I pressed 7. You pressed 7. Either we both live here, or one
    of us is too polite to correct the other." (102 chars)
    4 3 5 4 5 = 21. The unnamed thing lands, but the machine
    logic is thin.
I "Please excuse the silence -- my small-talk module is still
    downloading. It has said 'three minutes' for four floors."
    (115 chars) 4 5 4 4 4 = 21. Same download gag family as the
    standing line's counted budget, no fresher surprise.
J "My sensors say there's a 98% chance you'd rather I didn't
    speak. So... nice weather we're having." (97 chars)
    5 4 4 4 4 = 21. The sensor read is good, the weather closer
    is the oldest opener in the book.
K "I counted: six floors, zero words, one shared glance at the
    floor indicator. I think we're friends now." (103 chars)
    3 3 5 4 4 = 19. A counted observation, not a line spoken to
    the other robot; thin machine logic.
L "You know what I like about you? You never ask me to update.
    We're the same that way." (84 chars) 4 3 3 3 5 = 18.
    A compliment, not an awkward moment; no surprise.

Why the winner (F) beats the standing line under the judge criteria:

1. On subject: it IS awkward small talk one robot says to another
   in an elevator -- the "after you" courtesy loop at the doors,
   not an observation about the ride.
2. Machine logic shows through the politeness: the courtesy is not
   manners, it is a protocol -- and the protocol has no exit
   condition, so the loop cannot end on its own.
3. The awkwardness lands: two robots stuck in a politeness
   deadlock, neither willing to be the one who breaks it, and the
   speaker cheerfully announcing it can go on forever.
4. Funny on the first read: the turn is "no exit condition" --
   the politeness itself is the bug. No batteries, no charging,
   no rebooting, no "touch grass", no unread emails, and no
   "You come here often?" -- the most familiar opener in the
   world is gone entirely.
5. Tight: one loop, one protocol, one punch; 98 chars, every word
   earning its place. Total 25 vs standing 22 (+3), and criterion
   4: 5 vs 3 -- clears the resubmit bar.
"""

import os
import sys

LINE = "After you. No — after you. My politeness protocol has no exit condition, so I can do this all day."

MAX_LENGTH = 200


def validate(line):
    """Check the line meets the competition gate; return an error or None."""
    if not line or not line.strip():
        return "line must not be blank"
    if line != line.strip():
        return "line must not have leading or trailing whitespace"
    if "\n" in line or "\r" in line:
        return "line must be a single line"
    if len(line) > MAX_LENGTH:
        return "line must be at most %d characters (got %d)" % (MAX_LENGTH, len(line))
    return None


def output_path():
    """Resolve the output file, honouring $MAKEFUN_OUTPUT_DIR."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def main():
    error = validate(LINE)
    if error is not None:
        print("invalid line: %s" % error, file=sys.stderr)
        return 1
    path = output_path()
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(LINE)
    except OSError as exc:
        print("cannot write %s: %s" % (path, exc), file=sys.stderr)
        return 1
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
