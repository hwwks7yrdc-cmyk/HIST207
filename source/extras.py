# -*- coding: utf-8 -*-
"""The curators' notes, and slots for further images.

AUDIO holds one short text per work, written to be read aloud in about forty
seconds and published on the page as the curators' note for that work. The name
of the dict is historical: the exhibition carries these as wall text, not as
recordings.

EXTRA holds further images per work: (filename, alt text, caption). A file is
only rendered if it is actually present in assets/img/, so the team can add
material without touching the templates.

LISTEN holds recordings of the artists speaking, none of them ours and none of
them hosted here.
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

# (filename in assets/img/, alt text, caption with its own credit).
# Rendered only if the file is actually present. Everything here is documentation
# of the work itself, from the artist's own site, their distributor, or the
# institution that showed it. Nothing in this list was drawn or generated.
EXTRA = {
"paterson": [
  ("paterson-2.jpg",
   "Two people signing a document on a cardboard box in the forest clearing.",
   "The handover. Each year’s manuscript is signed over in Nordmarka and sealed. "
   "From the artist’s own documentation, futurelibrary.no."),
  ("paterson-3.jpg",
   "A printed certificate reading Margaret Atwood, 2014, Framtidsbiblioteket, Future Library, Katie Paterson.",
   "The certificate issued for the first deposit, Margaret Atwood, 2014. The accession "
   "document for a text nobody may read. futurelibrary.no."),
  ("paterson-4.jpg",
   "A line of people walking a forest path among tall spruce.",
   "The yearly walk into Nordmarka for the handover ceremony. futurelibrary.no."),
],
"sonjasdotter": [
  ("sonjasdotter-2.jpg",
   "Black and white archival footage of a field sign reading Svalofs Original Diamantvarvete II.",
   "Archival footage used in the film: a Svalöf trial plot sign, Diamantvårvete II. "
   "The naming and numbering of a certified variety. Still from the film, Filmform."),
  ("sonjasdotter-3.jpg",
   "Hands holding a flat glass case of grain over a stack of papers and folders.",
   "A gene bank accession handled in the film. Still from <cite>Cultivating Abundance</cite>, "
   "Filmform."),
  ("sonjasdotter-4.jpg",
   "A group of people standing together in a ripe grain field at the edge of a wood.",
   "Allkorn growers in the field. Still from <cite>Cultivating Abundance</cite>, Filmform."),
],
"balkin": [
  ("balkin-2.jpg",
   "Four contributed objects photographed separately: a coral fragment, a stone, a shell and an Antarctica patch.",
   "Four contributions, catalogued individually as a museum would catalogue them. "
   "Southern Exposure, San Francisco."),
  ("balkin-3.jpg",
   "A cotton tote bag printed Nepal Tourism Board, Naturally Nepal.",
   "A contribution from Nepal. Nothing in the archive weighs more than a kilogram. "
   "Southern Exposure, San Francisco."),
],
"orlow": [
  ("orlow-2.jpg",
   "Two people carrying a jute sack through dense green hillside vegetation.",
   "Still from <cite>Muthi</cite>, single-channel HD video with sound, 11 minutes 23 seconds, "
   "2016, part of <cite>Theatrum Botanicum</cite>. urielorlow.net."),
  ("orlow-3.jpg",
   "A gallery with a wall of framed panels, a large photographic portrait and a visitor on a bench.",
   "<cite>Theatrum Botanicum</cite> installed at Kunst Halle Sankt Gallen. "
   "Photograph by Gunnar Meier, urielorlow.net."),
  ("orlow-4.jpg",
   "A domed rotunda with a circular wooden rail and small objects spaced along the walls.",
   "A further installation of the work, in Durban. urielorlow.net."),
],
"sansour": [
  ("sansour-2.jpg",
   "Printed seed packets in Arabic and English reading Abu Samara, Spinach Sabanikh, Chard, Palestine Heirloom Seed Library.",
   "Seed packets from the library, named in Arabic and English. A Field, afield.org."),
  ("sansour-3.jpg",
   "Two women sitting on the floor sorting grain in a wide bowl, taking notes.",
   "Sansour recording a grower’s knowledge of a variety. Photograph by Vivien Sansour, "
   "A Field, afield.org."),
],
"futurefarmers": [
  ("futurefarmers-2.jpg",
   "A crowd pressing around a trestle table covered in small jars of grain in a city street.",
   "The cargo unloaded in port and handed over. From the Seed Journey logbook, "
   "futurefarmers.com."),
  ("futurefarmers-3.jpg",
   "A black and white photograph of two bearded men each holding a large sheaf of grain.",
   "Archival photograph gathered during the voyage. From the Seed Journey logbook, "
   "futurefarmers.com."),
  ("futurefarmers-4.jpg",
   "A walled garden with woven hurdle fencing beside a stone farm building.",
   "A growing ground visited on the route. From the Seed Journey logbook, futurefarmers.com."),
],
"alves": [
  ("alves-2.jpg",
   "A long gallery wall of framed research panels, maps and photographs.",
   "<cite>Seeds of Change</cite> installed as research panels, maps and photographs. "
   "mariatherezaalves.org."),
  ("alves-3.jpg",
   "The worn cover of a bound volume reading Catalogue of the Herbarium Collection of the late Mr Robert Brown.",
   "An archival herbarium catalogue consulted for the work. The ballast record is read "
   "against the botanical record. mariatherezaalves.org."),
  ("alves-4.jpg",
   "A pressed plant specimen labelled Alcea rhombifolia mounted beside a page of typed text.",
   "A ballast species, named and set beside its history. mariatherezaalves.org."),
  ("alves-5.jpg",
   "A tall framed panel holding two photographs of spoil heaps and dockside ground with a text between them.",
   "Ballast ground, photographed and annotated. mariatherezaalves.org."),
],
"okoyomon": [
  ("okoyomon-2.jpg",
   "A stand of trees completely buried under a continuous blanket of kudzu vine.",
   "Not the installation. This is kudzu doing in Georgia what it does in the gallery: "
   "growing over whatever is nearest. Wikimedia Commons."),
],
"kiwanga": [],
}

# Film and sound held by the projects themselves, linked rather than embedded so
# the pages keep working where those platforms are blocked.
SOURCE_MEDIA = {
"sonjasdotter": [("An excerpt from the 64-minute film, published by Filmform",
                  "https://www.filmform.com/works/5840-cultivating-abundance")],
"orlow": [("The films of Theatrum Botanicum on the artist’s site",
           "https://urielorlow.net/project/theatrum-botanicum/")],
"futurefarmers": [("The full voyage logbook, port by port",
                   "https://www.futurefarmers.com/seedjourney")],
"paterson": [("The handover ceremonies and author certificates, year by year",
              "https://www.futurelibrary.no/")],
"alves": [("The full image archive of the project",
           "https://www.mariatherezaalves.org/works/seeds-of-change")],
"balkin": [("Southern Exposure, who house the archive",
            "https://soex.org/projects-exhibitions/peoples-archive-sinking-and-melting")],
"sansour": [("A Field’s documentation of the seed library",
             "https://afield.org/person/vivien-sansour/")],
"kiwanga": [("One of the sixteen arrangements, at Goodman Gallery",
             "https://goodman-gallery.com/artists/kapwani-kiwanga/"
             "flowers-for-africa-union-of-south-africa-121850")],
"okoyomon": [("MMK’s own booklet for Earthseed",
              "https://cms.mmk.art/site/assets/files/5224/mmk_booklet_earthseed_en-1.pdf")],
}


# Recordings of the artists speaking about these works. Everything here was made
# and is published by somebody else: a public radio programme, a gallery that
# recorded its own symposium, two podcasts. None of it is ours to copy, and none
# of it is hosted here, so each one is named, dated and linked, and plays on the
# publisher's own site.
#
# Six of the nine have one. Sonjasdotter's film carries its own sound and the
# excerpt is already linked above; for Alves and Futurefarmers the published
# interviews are all in print. Rather than fill those three with something
# adjacent, they carry nothing, and the colophon says why.
#
# "quote" is only filled where the publisher prints a transcript. Lines nobody
# has transcribed stay unquoted: the recording is linked and that is all that
# can honestly be said about it.
LISTEN = {
"paterson": [{
  "label": "Future Library on the TED Radio Hour",
  "url": "https://www.npr.org/2022/10/28/1134069054/"
         "building-a-library-of-unread-manuscripts-locked-away-until-2114",
  "what": "NPR, <cite>Leaving a Mark</cite>, part four, 28 October 2022. Paterson "
          "walks out to Nordmarka and explains what the forest is for.",
  "quote": "Nobody will read the words until the forest has grown.",
  "said": "Katie Paterson, from NPR’s published transcript of the broadcast",
}],
"balkin": [{
  "label": "Rauschenberg Residency on Rising Water",
  "url": "https://freshartinternational.podbean.com/e/captiva",
  "what": "Fresh Art International, 13 October 2016, nine minutes. Balkin describes "
          "the archive, and what it means to accept whatever is sent.",
  "quote": None, "said": None,
}],
"orlow": [{
  "label": "Symposium: Theatrum Botanicum and Other Forms of Knowledge",
  "url": "https://theshowroom.org/resources/"
         "symposium-theatrum-botanicum-and-other-forms-of-knowledge",
  "what": "The Showroom, London, 29 October 2016. Orlow convened this himself with "
          "Shela Sheikh, and the gallery published the recording. It belongs to the "
          "work rather than reporting on it.",
  "quote": None, "said": None,
}],
"sansour": [{
  "label": "Vivien Sansour on the Palestine Heirloom Seed Library",
  "url": "https://esalen.org/podcasts/vivien-sansour-on-the-palestine-heirloom-seed-library",
  "what": "Voices of Esalen, 18 October 2021, fifty minutes, with the founder of the "
          "library on what it holds and what it refuses to write down.",
  "quote": None, "said": None,
}],
"okoyomon": [{
  "label": "Precious Okoyomon on Talk Art",
  "url": "https://shows.acast.com/talkart/episodes/precious-okoyomon",
  "what": "Talk Art, season 22 episode 10, 8 August 2024, in which Okoyomon sets out "
          "kudzu as a figure for colonisation, which is the argument the installation "
          "makes without words.",
  "quote": None, "said": None,
}],
"kiwanga": [{
  "label": "A brush with… Kapwani Kiwanga",
  "url": "https://www.theartnewspaper.com/2024/04/17/a-brush-with-kapwani-kiwana-podcast",
  "what": "The Art Newspaper, 17 April 2024, Kiwanga with Ben Luke on the research "
          "her work is built out of.",
  "quote": None, "said": None,
}],
}


def script(slug):
    return " ".join(AUDIO[slug].split())


if __name__ == "__main__":
    for k in AUDIO:
        n = len(script(k).split())
        print(f"{k:16} {n:4} Wörter   Bilder: {len(EXTRA.get(k, []))}")
