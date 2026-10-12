# -*- coding: utf-8 -*-
TITLE = "Duplicate Sample"
STRAP = "An online exhibition on seed banks and the keeping of living things"
TEAM = "Tim Maurice Steiner, Qing Guo and Seble Getaneh"
COURSE = "ARTS / HIST 207 · History of Art and Science · Duke Kunshan University"

ROOMS = [
    dict(n="I", slug="room-i", name="Deposit",
         line="What is selected, purified and put away.",
         text="A plantation begins by choosing. One organism is isolated, judged against a standard, "
              "and separated from everything it grew among. A seed vault begins the same way. The three "
              "works in this room are all acts of putting away, and each one asks a different question "
              "about the moment of choosing: who decides, by what standard, and for whom."),
    dict(n="II", slug="room-ii", name="Custody",
         line="Who holds the material, under what names and on what terms.",
         text="Once a thing is kept, somebody holds it. Custody is a question of names, of records and "
              "of permission. It is also where the plantation form shows itself most plainly, because a "
              "collection that controls access has to decide who counts as an owner. The three works here "
              "answer that in three incompatible ways."),
    dict(n="III", slug="room-iii", name="Thaw",
         line="What returns, what escapes, what refuses to be kept.",
         text="Tsing calls them unruly edges: the margins around managed space where species collaborate "
              "without anyone's permission. She argues that these zones of neglect keep producing more life "
              "than the managed ground does. This room is the edge. Material that nobody preserved turns out "
              "to have survived, and material that was managed gets away."),
]

WORKS = [
# ---------------------------------------------------------------- ROOM I
dict(room="I", code="DS – I – 01", slug="paterson", img="paterson.jpg",
     alt="A young spruce sapling marked with a pink ribbon, growing in the Nordmarka forest outside Oslo.",
     caption="Katie Paterson, <cite>Future Library</cite>, 2014–2114, Nordmarka forest, Oslo. Courtesy the artist.",
     artist="Katie Paterson", work="Future Library", date="2014–2114",
     born="Born 1981 in Glasgow; lives and works in Scotland.",
     medium="One thousand spruce trees, one hundred unread manuscripts, a purpose-built room.",
     desc=["In 2014 Paterson planted a thousand spruce saplings in Nordmarka forest outside Oslo. "
           "Every year since, one writer has handed over a manuscript that nobody is permitted to read. "
           "Margaret Atwood wrote the first.",
           "The texts are held in a silent room lined with wood from the clearing, inside the Deichman "
           "library in Bjørvika, where visitors can see the sealed manuscripts but not open them. In 2114 "
           "the trees will be felled and the hundred texts printed on their paper. Paterson will be dead by "
           "then, as will every contributor and almost everyone who has ever stood in the room."],
     note="The purest deposit in the exhibition. Nothing about the work can be experienced now except the "
          "promise, and the promise depends entirely on an institution and a forest both surviving a century. "
          "It is the vault gesture stripped of everything except trust.",
     label=[("What is kept", "One hundred manuscripts, unread, and the thousand trees that will print them."),
            ("Who deposited it", "One writer each year since 2014, beginning with Margaret Atwood."),
            ("Who may withdraw it", "Nobody, until 2114. The Deichman library in Oslo holds them in trust."),
            ("What was left out", "Everything those writers wrote on the other three hundred and sixty-four days.")],
     link=("futurelibrary.no", "https://www.futurelibrary.no/"),
     ),
dict(room="I", code="DS – I – 02", slug="sonjasdotter", img="sonjasdotter.jpg", placeholder=True,
     alt="Design placeholder in the exhibition identity: a grid of sealed storage boxes, one of them open and green.",
     caption="Image to be sourced. A still from <cite>Cultivating Abundance</cite> is available through Filmform, Stockholm.",
     artist="Åsa Sonjasdotter", work="Cultivating Abundance", date="2022",
     born="Born 1966 in Sweden; lives and works in Berlin.",
     medium="Film, 64 minutes, colour, Swedish with subtitles. Distributed by Filmform.",
     desc=["The film returns to the 1880s, when the Swedish Seed Association developed a breeding method "
           "built on ideas of genetic purity and originality. Varieties bred by farmers over generations were "
           "judged impure by that standard, pushed out of the fields and deposited in gene banks.",
           "Sonjasdotter follows the plant breeder Hans Larsson and the seed alliance Allkorn as they bring "
           "those grains back into cultivation. She cuts gelatin-silver glass plates and moving images found in "
           "a cold store barn together with footage of the breeders at work. The purity standard, the film "
           "argues, was a fiction, and current seed law still rests on it."],
     note="This is the work that explains how a gene bank fills up. A standard of purity decides which plants "
          "are legitimate, the rest are archived, and a living practice becomes a stored sample. Sonjasdotter "
          "then films the reversal.",
     label=[("What is kept", "Peasant-bred grain varieties, held in Nordic gene banks."),
            ("Who deposited it", "Breeders who judged them impure by the standard set in the 1880s."),
            ("Who may withdraw it", "Researchers, and since Allkorn, farmers who ask to grow them again."),
            ("What was left out", "The fields they came from, and the practice of breeding inside them.")],
     link=("filmform.com", "https://www.filmform.com/works/5840-cultivating-abundance"),
     ),
dict(room="I", code="DS – I – 03", slug="balkin", img="balkin.jpg", placeholder=True,
     alt="Design placeholder in the exhibition identity: a grid of sealed storage boxes, one of them open and green.",
     caption="Image to be sourced. Installation views are held by Southern Exposure, San Francisco.",
     artist="Amy Balkin", work="A People’s Archive of Sinking and Melting", date="2012–ongoing",
     born="Born 1967; lives and works in San Francisco.",
     medium="Collection of contributed objects, vitrines, museum labels.",
     desc=["A growing collection of ordinary objects contributed by people living in places expected to "
           "disappear through climate change and the political and economic pressures that come with it. A tuna "
           "can, a sweet wrapper, a plastic toy bird, a bottle cap, a flag, a dollar bill soaked in a flooded "
           "office, water from Venice.",
           "Contributions have arrived from Kivalina in Alaska, Dakar, Nepal, Venice, Cuba, Germany after the "
           "2013 floods and New York after Sandy. Nothing weighs more than a kilogram. Each object is catalogued "
           "as though it were a historical artefact, and its label carries the contributing country’s status "
           "under the UN climate convention."],
     note="A deposit with the selection step removed. The archive is not curated, everything offered is "
          "accepted, and the whole of it is always shown. Set beside a seed vault, it asks what changes when "
          "nobody is deciding what deserves keeping.",
     label=[("What is kept", "Ordinary objects from places expected to disappear. Nothing over a kilogram."),
            ("Who deposited it", "Anyone. Individuals, consulates, passers-by in each host city."),
            ("Who may withdraw it", "No one withdraws. The whole archive is always shown together."),
            ("What was left out", "Almost nothing. Two submissions were refused for misreading the brief.")],
     link=("archiveofsinkingandmelting.org", "https://archiveofsinkingandmelting.org/"),
     ),
# ---------------------------------------------------------------- ROOM II
dict(room="II", code="DS – II – 01", slug="orlow", img="orlow.jpg",
     alt="A darkened gallery with overhead projectors casting botanical drawings onto hanging translucent sheets.",
     caption="Uriel Orlow, <cite>What Plants Were Called Before They Had a Name</cite>, since 2015, installation view. Courtesy the artist.",
     artist="Uriel Orlow", work="Theatrum Botanicum", date="2015–2018",
     born="Born 1973 in Zurich; lives and works in London, Lisbon and Zurich.",
     medium="Films, sound works, photographs, slide projection and installation.",
     desc=["A body of work made between South Africa and Europe that treats the botanical world as a stage "
           "for politics. It covers plant migration and bio-piracy, flower diplomacy during apartheid, the "
           "garden that Mandela and his fellow prisoners planted on Robben Island, and the court case brought "
           "against the traditional healer Mafavuke Ngcobo.",
           "The element shown here is <cite>What Plants Were Called Before They Had a Name</cite>, in which "
           "names carried by plants in South African languages before European botany renamed them are "
           "projected as light rather than printed as labels."],
     note="Custody begins with naming. A plant that enters a collection under a Latin binomial enters as "
          "science; the same plant under its older name is filed as folklore, or not filed at all. Orlow shows "
          "the renaming as an act with a date and an author.",
     label=[("What is kept", "Names that plants carried before European botany renamed them."),
            ("Who deposited it", "Speakers of South African languages, over many generations."),
            ("Who may withdraw it", "Anyone, in principle. The renaming made the older names hard to find."),
            ("What was left out", "The Latin binomial got a herbarium sheet. The older name got none.")],
     link=("urielorlow.net", "https://urielorlow.net/project/theatrum-botanicum/"),
     ),
dict(room="II", code="DS – II – 02", slug="sansour", img="sansour.jpg", placeholder=True,
     alt="Design placeholder in the exhibition identity: a grid of sealed storage boxes, one of them open and green.",
     caption="Image to be sourced. Photographs of the library in Battir are held by the Palestine Heirloom Seed Library.",
     artist="Vivien Sansour", work="Palestine Heirloom Seed Library", date="2014–ongoing",
     born="Born 1978 in Jerusalem; works in Battir, Palestine.",
     medium="Seed library, jars, ash, field work, travelling kitchen.",
     desc=["Sansour founded the library to find threatened Palestinian crop varieties and return them to the "
           "field and to the table. Around forty-seven heirloom varieties are kept in jars, coated in ash as "
           "farmers have long preserved them, on the upper floor of a traditional courtyard house in Battir.",
           "Among them are jazar ahmar, a purple carrot cooked in tamarind, baladi tomatoes, Jadu’i watermelons "
           "and yakteen gourds. The library is an open room where farmers and neighbours come and go. Sansour "
           "keeps no record of who takes seeds or where they are planted."],
     quote=("I don’t track the seeds; they become a part of people’s lives. I wanted the seeds to stay free. "
            "They don’t belong to me, they belong to themselves.",
            "Vivien Sansour, quoted in Shannon Lee, “Vivien Sansour Plants Seeds of Hope for Palestine”, "
            "Asian American Arts Alliance, 18 December 2023"),
     note="The counter-vault, and the work the whole exhibition turns on. It performs every function of a seed "
          "bank and refuses the one that defines it: the register of who may withdraw. Set against Svalbard, it "
          "makes custody visible as a choice rather than a necessity.",
     label=[("What is kept", "About forty-seven heirloom varieties, in jars, coated in ash."),
            ("Who deposited it", "Farmers across the West Bank, and the artist."),
            ("Who may withdraw it", "Anyone who comes to the house in Battir. No record is kept."),
            ("What was left out", "No accession list exists, so nothing can be audited, including loss.")],
     link=("viviensansour.com", "https://viviensansour.com/Palestine-Heirloom"),
     ),
dict(room="II", code="DS – II – 03", slug="futurefarmers", img="futurefarmers.jpg",
     alt="A group gathered around a long table in a barn, with grain, rope and bottles laid out in front of them.",
     caption="Futurefarmers, <cite>Seed Journey</cite>, 2016–ongoing, image from the voyage logbook. Courtesy Futurefarmers.",
     artist="Futurefarmers", work="Seed Journey", date="2016–ongoing",
     born="Collective founded in 1995 by Amy Franceschini; based in San Francisco and Ghent.",
     medium="Sea voyage, cargo of grain seed, logbook, public gatherings.",
     desc=["In September 2016 a wooden rescue sailboat, the RS‑10 Christiania, built in 1895 to a Colin Archer "
           "design, left the port of Oslo carrying seed grain. It sailed to Vejle, London, Cardiff and Antwerp, "
           "then on through Jersey, San Sebastián and Santander, with Mallorca, Bethlehem and Istanbul ahead.",
           "The crew rotates between artists, anthropologists, biologists, bakers, farmers and sailors, who "
           "unload and discuss the cargo at harbours, barns, museums and social centres along the way. The route "
           "runs backwards along the paths the grains originally travelled."],
     quote=("Seed Journey moves people, ideas and seeds through time and space. The crew’s interests will "
            "influence the route, but ultimately grains are the compass.",
            "Futurefarmers, project text, futurefarmers.com"),
     note="Custody as hospitality instead of control. The seeds are neither frozen nor owned; they move, they "
          "are handed over at each port, and the itinerary is allowed to change. The work treats a seed as "
          "something you pass on.",
     label=[("What is kept", "Seed grain, in the hold of an 1895 rescue boat."),
            ("Who deposited it", "Seed savers and breeders along the route, beginning in Oslo."),
            ("Who may withdraw it", "Every port the boat reaches. The cargo is unloaded and discussed."),
            ("What was left out", "The fixed itinerary. The crew is allowed to change the route.")],
     link=("futurefarmers.com", "https://futurefarmers.com/seedjourney"),
     ),
# ---------------------------------------------------------------- ROOM III
dict(room="III", code="DS – III – 01", slug="alves", img="alves.jpg",
     alt="A framed documentation panel combining a harbour map, archival notices and photographs of excavation sites.",
     caption="Maria Thereza Alves, <cite>Seeds of Change</cite>, 1999–ongoing, documentation panel. Courtesy the artist.",
     artist="Maria Thereza Alves", work="Seeds of Change: A Floating Ballast Seed Garden", date="Bristol, 2012; series begun 1999",
     born="Born 1961 in São Paulo; lives and works in Berlin and Naples.",
     medium="Barge, ballast soil, germinated plants. Made with the designer Gitta Gschwendtner.",
     desc=["Sailing ships carried soil, sand and rubble as ballast, taking it on in one port and tipping it out "
           "in the next. Alves locates that soil in harbour cities, excavates it, and germinates whatever is "
           "still dormant inside. Seeds that have waited two or three hundred years come up.",
           "For Bristol she worked with the designer Gitta Gschwendtner to build a garden on a barge moored in "
           "the harbour, planted entirely from ballast seed, so that the flora growing there is a record of the "
           "city’s shipping routes and of the trade that ran along them."],
     note="Thaw in its most literal form. Nobody deposited these seeds and nobody kept them. They survived in "
          "the dark by accident and returned as evidence, which is what Tsing means when she says that zones of "
          "neglect keep producing what no collection could.",
     label=[("What is kept", "Seeds carried as ship ballast and tipped out in foreign harbours."),
            ("Who deposited it", "Nobody. The soil was waste, and the seeds happened to be in it."),
            ("Who may withdraw it", "The artist, by excavating the mud and letting it germinate."),
            ("What was left out", "Any record of what the ballast held. The garden is now the record.")],
     link=("mariatherezaalves.org", "https://www.mariatherezaalves.org/works/seeds-of-change-a-floating-ballast-seed-garden-bristol"),
     ),
dict(room="III", code="DS – III – 02", slug="okoyomon", img="okoyomon.jpg", placeholder=True,
     alt="Design placeholder in the exhibition identity: a grid of sealed storage boxes, one of them open and green.",
     caption="Image to be sourced. Installation views of <cite>Earthseed</cite> are held by MMK Frankfurt.",
     artist="Precious Okoyomon", work="Earthseed", date="MMK Frankfurt, 2020",
     born="Born 1993 in London; raised in Ohio and Nigeria; lives and works in New York.",
     medium="Living kudzu, soil, sugar cane, water, lamb’s wool sculptures.",
     desc=["Okoyomon filled a museum with kudzu, a vine brought from Japan to the United States and planted "
           "across the South to hold eroding soil in place. It did not stay where it was planted. It now covers "
           "abandoned land across the region and is treated as a pest.",
           "In the gallery the vine was allowed to grow over walls and floor for the run of the exhibition, "
           "through soil and sugar cane, around figures made of lamb’s wool. The plant was the artwork and also "
           "the thing the institution had to keep alive and could not fully control."],
     note="A species introduced to solve a problem, which then escaped the terms of its introduction. Okoyomon "
          "reads that history alongside the forced movement of people, and lets the plant take the building. It "
          "is the clearest case of the feral in the exhibition.",
     label=[("What is kept", "Living kudzu, soil and sugar cane, in a museum for the run of a show."),
            ("Who deposited it", "Introduced to the United States from Japan, to hold eroding soil."),
            ("Who may withdraw it", "The plant withdraws itself. It grows over whatever is nearest."),
            ("What was left out", "Any plan for what the institution does when the exhibition closes.")],
     link=("mmk.art", "https://www.mmk.art/en/"),
     ),
dict(room="III", code="DS – III – 03", slug="kiwanga", img="kiwanga.jpg",
     alt="A long garland of fresh green foliage hung in a swag across the white walls of a gallery.",
     caption="Kapwani Kiwanga, <cite>Flowers for Africa: Union of South Africa</cite>, 2017, installation view. Courtesy the artist and Goodman Gallery.",
     artist="Kapwani Kiwanga", work="Flowers for Africa", date="2013–ongoing",
     born="Born 1978 in Hamilton, Canada; lives and works in Paris.",
     medium="Fresh floral arrangements made to a written protocol. Sixteen to date.",
     desc=["Kiwanga searches archives for photographs of the ceremonies at which African countries became "
           "independent, and looks at the flowers. She identifies each arrangement, takes the image to a florist "
           "in the exhibiting city, and has it recreated as closely as the record allows: a buttonhole, a table "
           "bouquet, an archway.",
           "The protocol then states that the flowers must not be maintained. They wilt and collapse over the "
           "run of the show, and what a visitor sees depends entirely on when they arrive."],
     note="An archive that cannot be kept. Kiwanga reconstructs a document and then lets it decay on schedule, "
          "which is the exact opposite of the cold chain. It closes the exhibition by asking what preservation "
          "was ever promising.",
     label=[("What is kept", "Floral arrangements from the ceremonies at which countries became independent."),
            ("Who deposited it", "The photographer who happened to record the room, and the archive that filed it."),
            ("Who may withdraw it", "A florist in each host city, working from the archival image."),
            ("What was left out", "The protocol forbids maintenance. What you see depends on when you arrive.")],
     link=("goodman-gallery.com", "https://goodman-gallery.com/artists/kapwani-kiwanga"),
     ),
]

STATEMENT = [
 "Inside a mountain on Spitsbergen, in a chamber held below freezing, sit boxes of seeds sent by gene banks "
 "around the world. Each is a duplicate, a second copy kept elsewhere in case the first is lost. "
 "<em>Duplicate Sample</em> gathers nine contemporary artists who work with this practice of keeping living "
 "things against a future nobody can see: seed libraries, gene banks, botanical collections, archives of "
 "material that is still alive.",

 "Every such collection is a bet, and every bet is a selection. Somebody decided which varieties were worth "
 "the cold and which were left in the field, whose agriculture counted as heritage and whose counted as "
 "subsistence, who may withdraw a sample and on what terms. The exhibition holds two readings of the same "
 "rooms without settling between them. These places are genuine safeguards, built by people who expect to be "
 "useful. They are also monuments to an expected loss, and arrangements of power over who may hold what.",

 "Anna Tsing describes two ways of living with other species. The plantation isolates one organism, purifies "
 "it, severs its relationships and controls access to it. The unruly edge is the margin where species "
 "collaborate without permission, and where, as she puts it, zones of neglect keep producing more life than "
 "any managed ground does. A seed vault is a plantation answer to loss, and a careful one. The works here are "
 "arranged along that axis.",

 "The first room is about selecting and putting away. The second is about who holds the material, under what "
 "names and on what terms. The third is about what returns, what escapes and what refuses to be kept. Every "
 "work carries the same four-line label: what is kept, who deposited it, who may withdraw it, and what was "
 "left out. The last two are revealed on a click, so that looking behind the result is something you do.",
]

TSING = [
 ("Human nature is an interspecies relationship.", "Tsing 2012, p. 141"),
 ("Because plantations have shaped how contemporary agribusiness is organised, we tend to think of such "
  "arrangements as the only way to grow crops. But this arrangement had to be naturalised until we learned to "
  "take the alienation of people from their crops for granted.", "Tsing 2012, p. 148"),
 ("Evolutionary process in zones of neglect continues to produce more useful species and species interactions "
  "by many orders of magnitude.", "Tsing 2012, p. 151"),
]

VAULT_FACTS = [
 ("Opened", "26 February 2008, in a sandstone mountain outside Longyearbyen on Spitsbergen."),
 ("Owned by", "Norway, and managed with the Crop Trust and NordGen."),
 ("Held at", "Minus eighteen degrees, inside permafrost."),
 ("The rule", "Each depositor keeps ownership. Only the depositor may withdraw."),
 ("First withdrawal", "Syria, in 2015, after the gene bank in Aleppo was damaged."),
]

REFERENCES = [
 "Tsing, Anna. 2012. “Unruly Edges: Mushrooms as Companion Species.” <em>Environmental Humanities</em> 1: 141–154.",
 "Fowler, Cary. 2016. <em>Seeds on Ice: Svalbard and the Global Seed Vault</em>. Westport, CT: Prospecta Press.",
 "Crop Trust. 2020. <em>Svalbard Global Seed Vault: Annual Report</em>. Bonn: Global Crop Diversity Trust.",
 "Orlow, Uriel. 2018. <em>Theatrum Botanicum</em>. Edited by Shela Sheikh and Uriel Orlow. Berlin: Sternberg Press.",
 "Lee, Shannon. 2023. “Vivien Sansour Plants Seeds of Hope for Palestine.” <em>The Amp</em>, Asian American Arts Alliance, 18 December.",
 "Zhang, Ga, ed. 2020. <em>WE=LINK: Ten Easy Pieces</em>. Shanghai: Chronus Art Center, with Rhizome and Art Center Nabi.",
 "Tsing, Anna, Jennifer Deger, Alder Keleman Saxena and Feifei Zhou. 2020. <em>Feral Atlas: The More-Than-Human Anthropocene</em>. Stanford University Press.",
]
