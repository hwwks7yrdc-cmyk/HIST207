"""Key passages.

Long pages are read by scanning first and reading second. These are the
lines a visitor should carry out of each room if they read nothing else.
The rule held here is that marking only works while it stays rare: at most
two marks in a work, one of them at most in the heavier weight, and one in
each room text. Every phrase must occur in the source text exactly as
written, and the build fails loudly when one does not, so the marks cannot
quietly stop matching when a sentence is edited.

  SOFT  the fact the passage turns on
  HARD  the sentence that states what is at stake, set heavier
"""

# ------------------------------------------------------------------ rooms
ROOM_KEYS = {
    "I": dict(
        hard=["who decides, by what standard, and for whom"],
        soft=["One organism is isolated, judged against a standard, and "
              "separated from everything it grew among"],
    ),
    "II": dict(
        hard=["a collection that controls access has to decide who counts "
              "as an owner"],
        soft=["Custody is a question of names, of records and of permission"],
    ),
    "III": dict(
        hard=["these zones of neglect keep producing more life than the "
              "managed ground does"],
        soft=["the margins around managed space where species collaborate "
              "without anyone's permission"],
    ),
}

# ------------------------------------------------------------------ works
# desc: one entry per paragraph index that carries a mark
# note: the mark inside "Why this room"
WORK_KEYS = {
    "paterson": dict(
        desc={0: dict(soft=["one writer has handed over a manuscript that "
                            "nobody is permitted to read"])},
        note=dict(hard=["the vault gesture stripped of everything except trust"]),
    ),
    "sonjasdotter": dict(
        desc={0: dict(soft=["judged impure by that standard, pushed out of "
                            "the fields and deposited in gene banks"]),
              1: dict(hard=["The purity standard, the film argues, was a "
                            "fiction, and current seed law still rests on it."])},
        note=dict(),
    ),
    "balkin": dict(
        desc={0: dict(soft=["ordinary objects contributed by people living in "
                            "places expected to disappear"])},
        note=dict(hard=["it asks what changes when nobody is deciding what "
                        "deserves keeping"]),
    ),
    "orlow": dict(
        desc={1: dict(soft=["projected as light rather than printed as labels"])},
        note=dict(hard=["Custody begins with naming."]),
    ),
    "sansour": dict(
        desc={0: dict(soft=["coated in ash as farmers have long preserved them"]),
              1: dict(hard=["Sansour keeps no record of who takes seeds or "
                            "where they are planted."])},
        note=dict(),
    ),
    "futurefarmers": dict(
        desc={1: dict(soft=["The route runs backwards along the paths the "
                            "grains originally travelled."])},
        note=dict(hard=["The work treats a seed as something you pass on."]),
    ),
    "alves": dict(
        desc={0: dict(hard=["Seeds that have waited two or three hundred "
                            "years come up."]),
              1: dict(soft=["a record of the city’s shipping routes"])},
        note=dict(),
    ),
    "okoyomon": dict(
        desc={0: dict(hard=["It did not stay where it was planted."]),
              1: dict(soft=["The plant was the artwork and also the thing the "
                            "institution had to keep alive and could not "
                            "fully control."])},
        note=dict(),
    ),
    "kiwanga": dict(
        desc={1: dict(hard=["The protocol then states that the flowers must "
                            "not be maintained."])},
        note=dict(soft=["It closes the exhibition by asking what preservation "
                        "was ever promising."]),
    ),
}

# ------------------------------------------------------------------ entrance
# The curatorial statement on the entrance page carries two marks, no more:
# the sentence that names the selection, and the sentence that names the axis.
INDEX_KEYS = {
    1: dict(hard=["Every such collection is a bet, and every bet is a selection."]),
    2: dict(soft=["A seed vault is a plantation answer to loss, and a careful one."]),
}
