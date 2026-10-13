# -*- coding: utf-8 -*-
"""Individual artist statements.

The syllabus asks for "individual artist statements and artwork descriptions".
The artwork descriptions live in sitedata.py. This file holds the other half:
a paragraph on each artist's practice, and, where one could be sourced and
verified, a sentence in the artist's own words with a full citation.

Eight of the nine carry a verified quotation. Sonjasdotter does not: no direct
statement by her could be verified from a source we could read in full, so she
has none rather than a paraphrase dressed up as a quote.
"""

STATEMENT = {

"paterson": """Paterson works at scales that do not fit a human life. She has
broadcast Beethoven to the moon and back, mapped every dead star, made a light
bulb that simulates moonlight and buried a grain of sand carved to a
two-hundredth of a millimetre back inside the Sahara. The method is consistent:
take an enormous astronomical or geological fact, and find the one small object
or gesture that lets a person stand next to it. Her collaborators are usually
scientists, and the works are usually quiet. Future Library is the furthest she
has pushed the approach, because the audience it is made for has not been born.""",

"sonjasdotter": """Sonjasdotter is an artist and researcher who works through
cultivation itself rather than through images of it. Her long project Potato
Perspective began after she encountered the seed-sharing farmers of Navdanya in
India, and took the cultivated potato as a way to trace how modernisation
reorganised the relation between people and plants: Andean origins, EU variety
registration, genetic engineering, and property rights over crops. She grows,
propagates and exhibits the plants as the work. Cultivating Abundance continues
that line into film, following breeders who are returning archived grain to the
field.""",

"balkin": """Balkin makes work about the politics of land, air and atmosphere,
and about who is permitted to own them. This Is the Public Domain is a parcel of
California she has spent years trying to give to the public in perpetuity; Public
Smog is a park in the atmosphere built from emissions credits she purchased and
withheld from the market. The projects tend to run for years, to involve
bureaucracies rather than studios, and to end in documents. A People's Archive of
Sinking and Melting applies that patience to objects contributed by people living
in places expected to disappear.""",

"orlow": """Orlow works in film, sound, photography and installation, usually
across long research relationships with a particular place. Theatrum Botanicum
came out of several years of work between South Africa and Europe and treats
plants as political actors rather than scenery: the garden on Robben Island,
flower diplomacy under apartheid, bio-piracy, and the court case brought against
the healer Mafavuke Ngcobo. He is explicit that botanical collections are not
neutral, and equally explicit about the terms on which he works in places that
are not his own.""",

"sansour": """Sansour is an agricultural researcher and artist who founded the
Palestine Heirloom Seed Library in 2014 to find threatened Palestinian crop
varieties and return them to the field and to the table. The work is not
primarily exhibition work: it is seed-finding, growing, cooking and conversation,
carried by a travelling kitchen and a Traveling Seed Library as much as by any
gallery. The holdings are kept in jars coated in ash on the upper floor of a
courtyard house in Battir, in an open room, with no record of who takes what.""",

"futurefarmers": """Futurefarmers is a collective founded by Amy Franceschini in
1995, working between San Francisco and Ghent with farmers, scientists,
architects and engineers. The group builds situations rather than objects: a
windmill, a bakery, a boat, a shared meal, each one a device for getting people
into a room around a question about food and land. Seed Journey is the clearest
case, a sea voyage in a wooden rescue boat whose cargo of grain is unloaded and
discussed at every port rather than delivered anywhere.""",

"alves": """Alves is a Brazilian artist long based in Berlin whose work recovers
histories that official records leave out, often by going to the ground and
digging. Seeds of Change, begun in the late 1990s and continued across European
port cities, works from ballast flora: the seeds that travelled in the soil ships
carried for stability and tipped out at the other end. She germinates that soil
and reads what comes up as a record of the trade routes that produced it. She was
a founder of Brazil's Green Party and has worked on indigenous land rights
alongside the art.""",

"okoyomon": """Okoyomon is an artist and poet working between New York and
Frankfurt whose installations are living systems: soil, water, plants, insects
and sculpture left to carry on without the artist. They work with materials that
have their own histories of forced movement, and let those materials behave. In
Earthseed the material is kudzu, the vine introduced to Mississippi in 1876 and
used to hold soil eroded by cotton cultivation, which then spread far past what
anyone intended. The title comes from the religion invented in Octavia Butler's
Parable of the Sower.""",

"kiwanga": """Kiwanga trained in anthropology and comparative religion before
turning to art, and the method shows: her work starts in archives and ends in
materials chosen for what they carry historically. Flowers for Africa, Linear
Paintings and her work on the architecture of control all approach power through
objects that seem too ordinary to be political. She has described the question of
power asymmetry as the idea that pushes her most, and she is interested in what
the non-human world remembers of events that human documents record badly or not
at all.""",
}


# (quotation, full citation). Every one of these was read in its source.
QUOTE = {
"paterson": ("Looking through the lens of deep time inevitably changes how you "
             "see the present.",
             "Katie Paterson, interviewed by Susan Mansfield, Scottish Art News, "
             "The Fleming Collection, 28 July 2026"),

"balkin": ("The objects are artifacts of a decision to participate by "
           "contributing.",
           "Amy Balkin, in “What Will Have Been: Interviews on A People’s "
           "Archive of Sinking and Melting”, The Brooklyn Rail, June 2014"),

"orlow": ("Botanical gardens are often colonial archives, with plants from all "
          "over the world. There’s an epistemic violence in that.",
          "Uriel Orlow, quoted in “How Uriel Orlow Uses Plants to Tell Stories "
          "of Power”, Art Basel Stories"),

"alves": ("Celebrating the micro histories of plants and humans together.",
          "Maria Thereza Alves on Seeds of Change, University of Bristol, "
          "December 2016"),

"okoyomon": ("The kudzu is so far from home.",
             "Precious Okoyomon, in conversation with Hannah Black, published in "
             "MMK’s booklet for Earthseed, Frankfurt, 2020"),

"kiwanga": ("I think the natural world is a different kind of witness to human "
            "history.",
            "Kapwani Kiwanga, interviewed by Artnet News, 2021"),
}
# sansour and futurefarmers already carry a verified quote in sitedata.py,
# rendered in the main body of their entries.


if __name__ == "__main__":
    for k, v in STATEMENT.items():
        n = len(" ".join(v.split()).split())
        print(f"{k:16} {n:4} words   quote: {'yes' if k in QUOTE else 'no'}")
