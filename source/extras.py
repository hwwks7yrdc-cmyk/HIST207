# -*- coding: utf-8 -*-
"""The curators' notes, and slots for further images.

AUDIO holds one short text per work, written to be read aloud in about forty
seconds and published on the page as the curators' note for that work. The name
of the dict is historical: the exhibition carries these as wall text, not as
recordings.

EXTRA holds further images per work: (filename, alt text, caption). A file is
only rendered if it is actually present in assets/img/, so the team can add
material without touching the templates.
"""

AUDIO = {
"paterson": """
Stand in the Silent Room in Oslo and there is nothing to read. A hundred
manuscripts, or the twelve that exist so far, sit behind glass in drawers with
the author's name and the year on them, and nothing else. You cannot open them.
Neither can the librarians. Paterson has made a collection whose entire value
sits in a year none of us will see, and which depends on a public library and a
forest both outlasting everyone now alive. That is the deposit in its purest
form. It asks for trust and offers nothing back inside a human lifetime.
""",

"sonjasdotter": """
A gene bank does not fill up by accident. In the eighteen eighties the Swedish
Seed Association settled on a method built around purity and originality, and
grain that farmers had bred over generations failed that test. It left the
fields and went into storage, alive but uncultivated, which is a strange way to
survive. Sonjasdotter films the reversal: the breeder Hans Larsson and the seed
alliance Allkorn asking for those grains back and putting them in the ground
again. Her argument is that the purity standard was always a fiction, and that
seed law still rests on it.
""",

"balkin": """
Everything in this collection was handed over by someone who lives in a place
expected to disappear. A tuna can. A plastic toy bird. A bottle cap. A dollar
bill that was soaked when an office flooded. Nothing weighs more than a
kilogram, and nothing is refused, which makes it the opposite of a seed vault:
no expert decides what deserves keeping. Each object is catalogued like a
historical artefact, and its label carries the contributing country's status
under the United Nations climate convention, so the politics sits on the label
rather than underneath it.
""",

"orlow": """
Custody starts earlier than most people think. It starts at the moment of
naming. A plant that enters a collection under a Latin binomial enters as
science: it gets a herbarium sheet, a date, a collector, a place in a filing
system that will still be searchable in two hundred years. The same plant under
the name its neighbours used gets filed as folklore, or is not filed at all.
Orlow projects those older names as light rather than printing them as labels,
which is close to the only way they appear in a gallery at all.
""",

"sansour": """
This is the work the exhibition turns on. On the upper floor of a courtyard
house in Battir there are jars of seed coated in ash, about forty-seven
varieties: a purple carrot cooked in tamarind, baladi tomatoes, Jadu'i
watermelons. It accepts material, keeps it alive and gives it back on request,
which is everything a seed bank does. It refuses one thing. Nobody writes down
who took what. Sansour has said she wanted the seeds to stay free, that they do
not belong to her, they belong to themselves. Set against Svalbard, that single
refusal makes custody look like a choice rather than a necessity.
""",

"futurefarmers": """
In September two thousand and sixteen a wooden rescue boat built in eighteen
ninety-five left Oslo with grain seed in the hold, and sailed to Vejle, London,
Cardiff and Antwerp. At every port the cargo came out, and people gathered
around it, and the grain was discussed and handed on. It is a storage strategy
that works by the exact opposite of storage. Nothing is held at a fixed
temperature and nothing stays still. The seed survives because it keeps moving
and keeps being given to somebody else.
""",

"alves": """
Ships once took on soil as ballast to steady themselves, and tipped it out at
the other end. Inside that soil were seeds, and in the mud of Bristol harbour
some of them waited roughly two centuries without anybody intending to keep
them. Alves excavated that mud and let it germinate on a floating garden. What
grows is a record of where the ships came from, which is a record of the trade
that sent them. It is the only collection here that nobody built, and it is
still a perfectly good archive.
""",

"okoyomon": """
Kudzu arrived in the United States as an ornamental and was then planted at
scale to hold eroding soil in place, which it did, and then it kept going. In
Okoyomon's installation it is allowed to grow over the room for the length of
the exhibition, and the institution agrees in advance not to cut it back. Every
other collection in this show has somebody deciding what comes out and when.
This one withdraws itself, over whatever is nearest, on a schedule nobody
controls.
""",

"kiwanga": """
Kiwanga works from photographs of the ceremonies at which African countries
became independent, and in those photographs there are flowers. She identifies
the arrangement, takes the image to a florist in whichever city is hosting the
show, and has it rebuilt as closely as the record allows. Then the protocol
says: do not maintain it. It wilts and collapses over the run of the
exhibition, so what you see depends entirely on when you came. It is the exact
opposite of a cold chain, and it closes the show by asking what preservation
was ever promising.
""",
}

# (filename in assets/img/, alt text, caption). Rendered only if the file exists.
EXTRA = {
    "paterson": [],
    "sonjasdotter": [],
    "balkin": [],
    "orlow": [],
    "sansour": [],
    "futurefarmers": [],
    "alves": [],
    "okoyomon": [],
    "kiwanga": [],
}


def script(slug):
    return " ".join(AUDIO[slug].split())


if __name__ == "__main__":
    for k in AUDIO:
        t = script(k)
        print(f"{k:16} {len(t.split()):4} words  ~{len(t.split())/2.4:4.0f} sec")
