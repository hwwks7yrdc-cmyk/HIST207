# -*- coding: utf-8 -*-
"""Nine drawn diagrams, one per work.

Each one shows how that collection actually operates: what goes in, what is
filtered, who may take something out. They are original drawings in the
exhibition identity, inlined into the pages so the site's own typefaces apply.

Every figure in them comes from the verified entry for that work. Nothing here
invents a number.
"""

W, H = 1200, 540


def svg(slug, title, inner, h=H):
    return (f'<svg class="dg" viewBox="0 0 {W} {h}" role="img" '
            f'aria-labelledby="dgt-{slug}">'
            f'<title id="dgt-{slug}">{title}</title>'
            f'{inner}</svg>')


# ---------------------------------------------------------------- primitives
def box(x, y, w, h, live=False, r=2):
    c = "dg-live" if live else "dg-box"
    return f'<rect class="{c}" x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}"/>'


def lab(x, y, t, cls="dg-lab", anchor="start"):
    return f'<text class="{cls}" x="{x}" y="{y}" text-anchor="{anchor}">{t}</text>'


def arrow(x1, y1, x2, y2, live=False, dash=False):
    c = "dg-arrow dg-arrow--live" if live else "dg-arrow"
    if dash:
        c += " dg-arrow--dash"
    return (f'<path class="{c}" d="M{x1} {y1} L{x2} {y2}" '
            f'marker-end="url(#{"ah-live" if live else "ah"})"/>')


DEFS = ('<defs>'
        '<marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
        'markerHeight="7" orient="auto-start-reverse">'
        '<path class="dg-head" d="M0 0 L10 5 L0 10 z"/></marker>'
        '<marker id="ah-live" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
        'markerHeight="7" orient="auto-start-reverse">'
        '<path class="dg-head dg-head--live" d="M0 0 L10 5 L0 10 z"/></marker>'
        '</defs>')


# ================================================================ ROOM I
def paterson():
    """One hundred years as one hundred cells. Only the last one is readable."""
    p = [DEFS]
    x0, y0, cw, gap = 60, 200, 8.9, 2.0
    p.append(lab(60, 70, "One hundred years, one cell each", "dg-title"))
    p.append(lab(60, 104, "A manuscript arrives every year. None of them can be opened "
                          "until the final cell.", "dg-note"))
    deposited = 12          # 2014 through 2025 inclusive
    for i in range(100):
        x = x0 + i * (cw + gap)
        if i == 99:
            p.append(box(x, y0 - 14, cw, 88, live=True))
        else:
            p.append(box(x, y0, cw, 60, live=False))
            if i < deposited:
                p.append(f'<rect class="dg-fill" x="{x+1.6}" y="{y0+1.6}" '
                         f'width="{cw-3.2}" height="{56.8}"/>')
    p.append(f'<path class="dg-brace" d="M{x0} {y0+74} L{x0} {y0+84} '
             f'L{x0 + (deposited-1)*(cw+gap) + cw} {y0+84} '
             f'L{x0 + (deposited-1)*(cw+gap) + cw} {y0+74}"/>')
    p.append(lab(x0, y0 + 108, "12 manuscripts handed over so far"))
    p.append(lab(x0, y0 + 130, "sealed, unread, unreadable", "dg-lab dg-lab--dim"))
    p.append(lab(60, y0 - 28, "2014"))
    p.append(lab(x0 + 99 * (cw + gap) + cw, y0 - 28, "2114", anchor="end"))
    p.append(lab(x0 + 99 * (cw + gap) + cw, y0 + 108,
                 "the trees are felled and the hundred texts are printed",
                 "dg-lab dg-lab--live", anchor="end"))
    p.append(lab(60, 470, "1,000 spruce planted in Nordmarka · 1 room in the Deichman "
                          "library · 0 readers for 100 years", "dg-foot"))
    return svg("paterson", "A hundred-year timeline. One cell per year, twelve "
                           "manuscripts deposited so far, and a single moment of release in 2114.",
               "".join(p))


def sonjasdotter():
    """A purity standard sorts living practice into a gene bank, then a return."""
    p = [DEFS]
    p.append(lab(60, 62, "The standard that fills a gene bank", "dg-title"))
    p.append(lab(60, 92, "A rule written in the 1880s decides which plants count as "
                          "legitimate. The rest are archived.", "dg-note"))
    # the field, many different shapes
    import math
    p.append(lab(60, 170, "The field, before 1880"))
    seeds = [(0, 0), (1, 1), (2, 0), (3, 2), (4, 1), (0, 2), (1, 0), (2, 2), (3, 0),
             (4, 2), (0, 1), (2, 1)]
    for i, (cx, cy) in enumerate(seeds):
        x = 64 + cx * 34
        y = 196 + cy * 34
        rx = 7 + (i % 4) * 2.2
        ry = 6 + ((i + 2) % 3) * 2.6
        p.append(f'<ellipse class="dg-seed" cx="{x+12}" cy="{y+12}" rx="{rx}" ry="{ry}" '
                 f'transform="rotate({(i*37)%180} {x+12} {y+12})"/>')
    # the sieve
    p.append(arrow(240, 240, 330, 240))
    p.append(box(340, 150, 160, 190))
    p.append(lab(420, 186, "purity", "dg-lab", anchor="middle"))
    p.append(lab(420, 206, "standard", "dg-lab", anchor="middle"))
    p.append(lab(420, 232, "1880s", "dg-lab dg-lab--dim", anchor="middle"))
    for i in range(7):
        y = 258 + i * 11
        p.append(f'<line class="dg-sieve" x1="356" y1="{y}" x2="484" y2="{y}"/>')
    # accepted
    p.append(arrow(500, 200, 590, 200))
    p.append(lab(600, 176, "passes: one uniform variety"))
    for i in range(5):
        p.append(f'<ellipse class="dg-seed dg-seed--pure" cx="{612 + i*30}" cy="{204}" '
                 f'rx="10" ry="7"/>')
    p.append(lab(600, 238, "stays in cultivation", "dg-lab dg-lab--dim"))
    # rejected
    p.append(arrow(500, 290, 590, 290))
    p.append(lab(600, 300, "judged impure: everything else"))
    p.append(box(600, 318, 300, 96))
    p.append(lab(616, 348, "NORDIC GENE BANK"))
    p.append(lab(616, 374, "held at minus eighteen, alive, uncultivated",
                 "dg-lab dg-lab--dim"))
    # the return
    # the return runs back underneath, through empty ground
    p.append(f'<path class="dg-arrow dg-arrow--live dg-arrow--dash" '
             f'd="M596 372 H214 V314" marker-end="url(#ah-live)"/>')
    for k, line in enumerate(["Allkorn, and the breeder Hans Larsson,",
                              "asking for them back and growing them again"]):
        p.append(lab(238, 400 + k * 20, line, "dg-lab dg-lab--live"))
    p.append(lab(60, 470, "The film argues the purity standard was a fiction, and that "
                          "current seed law still rests on it.", "dg-foot"))
    return svg("sonjasdotter", "A sieve labelled purity standard sorts many different "
                               "seeds. One uniform variety passes into cultivation, the rest fall into a gene "
                               "bank, and a green dashed line carries some of them back out to the field.",
               "".join(p))


def balkin():
    """A collection with the filter removed."""
    p = [DEFS]
    p.append(lab(60, 70, "A deposit with the selection step removed", "dg-title"))
    p.append(lab(60, 104, "Nothing is chosen at the door. The ordering happens after "
                          "the objects have already been accepted.", "dg-note"))
    places = ["Kivalina, Alaska", "Dakar", "Nepal", "Venice", "Cuba",
              "Germany, 2013 floods", "New York, after Sandy"]
    for i, pl in enumerate(places):
        y = 160 + i * 38
        p.append(lab(60, y + 5, pl))
        p.append(arrow(250, y, 470, y))
    # the gate that isn't there
    p.append(f'<line class="dg-gateless" x1="500" y1="140" x2="500" y2="438"/>')
    p.append(lab(512, 132, "no gate here", "dg-lab dg-lab--live"))
    p.append(box(560, 150, 330, 288))
    p.append(lab(584, 186, "THE ARCHIVE"))
    for r in range(4):
        for c in range(6):
            p.append(box(584 + c * 48, 210 + r * 52, 36, 36, live=(r == 1 and c == 3)))
    p.append(lab(584, 418, "nothing over one kilogram", "dg-lab dg-lab--dim"))
    p.append(arrow(890, 294, 960, 294))
    p.append(lab(976, 280, "shown whole,"))
    p.append(lab(976, 302, "every object, every time"))
    p.append(lab(976, 344, "refused in total: 2", "dg-lab dg-lab--dim"))
    p.append(lab(976, 366, "both for misreading the brief", "dg-lab dg-lab--dim"))
    p.append(lab(60, 492, "Every label carries the contributing country’s status under "
                          "the UN climate convention.", "dg-foot"))
    return svg("balkin", "Seven places feed objects into an archive with no gate between "
                         "them and it. The archive is always shown whole, and only two submissions were "
                         "ever refused.", "".join(p))


# ================================================================ ROOM II
def orlow():
    """Two names for one plant. Only one of them gets filed."""
    p = [DEFS]
    p.append(lab(60, 70, "Which name gets a sheet", "dg-title"))
    p.append(lab(60, 104, "Custody begins at the moment of naming. One name enters the "
                          "record; the other has nowhere to go.", "dg-note"))
    p.append(box(60, 220, 150, 90))
    p.append(lab(135, 262, "one plant", "dg-lab", anchor="middle"))
    p.append(lab(135, 284, "growing", "dg-lab dg-lab--dim", anchor="middle"))
    # upper track: latin
    p.append(arrow(210, 250, 290, 182))
    p.append(box(300, 140, 210, 84))
    p.append(lab(320, 174, "Latin binomial"))
    p.append(lab(320, 198, "named by European botany", "dg-lab dg-lab--dim"))
    p.append(arrow(510, 182, 580, 182))
    p.append(box(590, 140, 190, 84))
    p.append(lab(610, 174, "herbarium sheet"))
    p.append(lab(610, 198, "dated, signed, filed", "dg-lab dg-lab--dim"))
    p.append(arrow(780, 182, 850, 182))
    p.append(box(860, 140, 190, 84))
    p.append(lab(880, 174, "findable"))
    p.append(lab(880, 198, "searchable for centuries", "dg-lab dg-lab--dim"))
    # lower track: the older name
    p.append(arrow(210, 280, 290, 348, live=True))
    p.append(box(300, 306, 210, 84, live=True))
    p.append(lab(320, 340, "the older name", "dg-lab dg-lab--onlive"))
    p.append(lab(320, 364, "spoken, not written down", "dg-lab dg-lab--onlive"))
    p.append(f'<path class="dg-arrow dg-arrow--dash" d="M510 348 L580 348"/>')
    p.append(f'<line class="dg-dead" x1="596" y1="320" x2="632" y2="376"/>')
    p.append(f'<line class="dg-dead" x1="632" y1="320" x2="596" y2="376"/>')
    p.append(lab(656, 342, "no sheet"))
    p.append(lab(656, 366, "filed as folklore, or not filed", "dg-lab dg-lab--dim"))
    p.append(lab(60, 470, "Orlow projects the older names as light rather than printing "
                          "them as labels, which is the only way they appear in a gallery at all.",
                 "dg-foot"))
    return svg("orlow", "One plant leads to two names. The Latin binomial gets a herbarium "
                        "sheet and stays findable. The older name reaches a dead end and is filed as "
                        "folklore, or not filed at all.", "".join(p))


def sansour():
    """The vault and the counter-vault, drawn side by side."""
    p = [DEFS]
    p.append(lab(60, 70, "The same library, minus the register", "dg-title"))
    p.append(lab(60, 104, "Every function of a seed bank is performed here. One is "
                          "refused.", "dg-note"))
    cols = [("A SEED VAULT", 60, False), ("BATTIR", 640, True)]
    rows = [("accepts material", True, True),
            ("keeps it alive", True, True),
            ("returns it on request", True, True),
            ("records who deposited", True, True),
            ("records who withdrew", True, False)]
    for title, ox, live in cols:
        p.append(box(ox, 140, 500, 300, live=False))
        p.append(lab(ox + 24, 178, title))
        for i, (t, a, b) in enumerate(rows):
            y = 212 + i * 44
            has = a if ox == 60 else b
            if has:
                p.append(f'<path class="dg-tick{" dg-tick--live" if live else ""}" '
                         f'd="M{ox+26} {y-4} l7 8 l14 -17"/>')
            else:
                p.append(f'<line class="dg-dead dg-dead--live" x1="{ox+26}" y1="{y-10}" '
                         f'x2="{ox+47}" y2="{y+8}"/>')
                p.append(f'<line class="dg-dead dg-dead--live" x1="{ox+47}" y1="{y-10}" '
                         f'x2="{ox+26}" y2="{y+8}"/>')
            cls = "dg-lab"
            if not has:
                cls = "dg-lab dg-lab--live"
            p.append(lab(ox + 66, y + 4, t, cls))
    p.append(lab(590, 300, "→", "dg-title", anchor="middle"))
    p.append(lab(60, 492, "About 47 heirloom varieties, in jars, coated in ash, on the "
                          "upper floor of a courtyard house. The door is open and nothing is written down.",
                 "dg-foot"))
    return svg("sansour", "Two columns compare a seed vault with the library in Battir. "
                          "They match on four functions. On the fifth, recording who withdrew, the vault "
                          "has a tick and Battir has a cross.", "".join(p))


def futurefarmers():
    """Seed kept by being carried and given away."""
    p = [DEFS]
    p.append(lab(60, 70, "Storage replaced by circulation", "dg-title"))
    p.append(lab(60, 104, "The grain is kept safe by being moved and handed over, not by "
                          "being held still.", "dg-note"))
    ports = [("Oslo", 110, 300, "September 2016, the RS‑10 Christiania leaves"),
             ("Vejle", 320, 250, "cargo unloaded, bread baked, people gather"),
             ("London", 530, 320, "cargo unloaded, the grain is discussed"),
             ("Cardiff", 740, 258, "cargo unloaded, the grain is discussed"),
             ("Antwerp", 950, 318, "cargo unloaded, the grain is discussed")]
    d = "M"
    for i, (n, x, y, _) in enumerate(ports):
        d += f"{x} {y} " + ("" if i == len(ports) - 1 else f"Q {x+55} {y-46} ")
    p.append(f'<path class="dg-route" d="{d}"/>')
    for i, (n, x, y, note) in enumerate(ports):
        p.append(f'<circle class="dg-port{" dg-port--live" if i == 0 else ""}" '
                 f'cx="{x}" cy="{y}" r="11"/>')
        p.append(lab(x, y - 28, n, "dg-lab dg-lab--big", anchor="middle"))
        ty = y + 44 if i % 2 == 0 else y + 44
        p.append(f'<line class="dg-tickline" x1="{x}" y1="{y+14}" x2="{x}" y2="{ty-18}"/>')
        for k, line in enumerate(_wrap(note, 22)):
            p.append(lab(x, ty + k * 18, line, "dg-lab dg-lab--dim", anchor="middle"))
    p.append(lab(60, 470, "A wooden rescue sailboat built in 1895 to a Colin Archer "
                          "design. The hold is the only store, and it is emptied at every port.",
                 "dg-foot"))
    return svg("futurefarmers", "A sailing route from Oslo through Vejle, London and "
                                "Cardiff to Antwerp. At every port the cargo is unloaded and discussed.",
               "".join(p))


def _wrap(t, n):
    out, line = [], ""
    for word in t.split():
        if len(line) + len(word) + 1 > n:
            out.append(line); line = word
        else:
            line = (line + " " + word).strip()
    if line:
        out.append(line)
    return out


# ================================================================ ROOM III
def alves():
    """Seed held by accident, in ballast, for two centuries."""
    p = [DEFS]
    p.append(lab(60, 70, "A store nobody intended to keep", "dg-title"))
    p.append(lab(60, 104, "Soil taken aboard as ballast carried seed across the Atlantic "
                          "and was tipped out at the destination.", "dg-note"))
    p.append(lab(60, 168, "loading port"))
    p.append(box(60, 186, 200, 60))
    p.append(lab(80, 222, "soil shovelled in as ballast", "dg-lab dg-lab--dim"))
    p.append(arrow(260, 216, 360, 216))
    p.append(lab(380, 168, "the crossing"))
    p.append(f'<path class="dg-wave" d="M372 224 q22 -14 44 0 t44 0 t44 0 t44 0"/>')
    p.append(arrow(560, 216, 650, 216))
    p.append(lab(670, 168, "Bristol harbour"))
    # strata
    y0 = 196
    for i, (h, cl) in enumerate([(26, "dg-strata"), (22, "dg-strata"), (30, "dg-strata"),
                                 (24, "dg-strata")]):
        p.append(f'<rect class="{cl}" x="670" y="{y0}" width="420" height="{h}"/>')
        y0 += h
    p.append(lab(1100, 212, "mud", "dg-lab dg-lab--dim", anchor="end"))
    for i, x in enumerate([712, 798, 884, 970, 1042]):
        p.append(f'<ellipse class="dg-seed dg-seed--buried" cx="{x}" cy="{236 + (i%3)*14}" '
                 f'rx="7" ry="5"/>')
    p.append(f'<line class="dg-timeline" x1="670" y1="326" x2="1090" y2="326"/>')
    p.append(lab(670, 352, "dumped, then dormant"))
    p.append(lab(1090, 352, "roughly two centuries", "dg-lab dg-lab--dim", anchor="end"))
    # the withdrawal
    p.append(f'<path class="dg-arrow dg-arrow--live" d="M700 326 L700 392" '
             f'marker-end="url(#ah-live)"/>')
    for k, line in enumerate(["Bristol, 2012: the artist excavates the",
                              "mud and lets it germinate on a floating garden"]):
        p.append(lab(722, 384 + k * 22, line, "dg-lab dg-lab--live"))
    p.append(lab(60, 470, "The plants that come up are a record of where the ships came "
                          "from, which is a record of the trade that sent them.", "dg-foot"))
    return svg("alves", "Soil loaded as ballast crosses the Atlantic, is dumped in Bristol "
                        "harbour and lies dormant in the mud for two centuries until the artist "
                        "excavates it and lets it germinate.", "".join(p))


def okoyomon():
    """The only collection that withdraws itself."""
    p = [DEFS]
    p.append(lab(60, 70, "A collection that leaves on its own", "dg-title"))
    p.append(lab(60, 104, "Nobody withdraws this material. It withdraws itself, over "
                          "whatever is nearest.", "dg-note"))
    stages = [("week 1", 2), ("week 4", 7), ("week 8", 16), ("the run of the show", 31)]
    for s, (title, filled) in enumerate(stages):
        ox = 60 + s * 290
        p.append(lab(ox, 168, title))
        k = 0
        for r in range(6):
            for c in range(6):
                live = k < filled
                p.append(box(ox + c * 36, 190 + r * 36, 28, 28, live=live))
                k += 1
        if s < 3:
            p.append(arrow(ox + 236, 292, ox + 272, 292))
    p.append(lab(60, 462, "Kudzu was introduced to Mississippi in 1876 and planted to hold "
                          "soil eroded by cotton. It did not stop where it was put.", "dg-foot"))
    p.append(lab(60, 492, "Okoyomon lets it grow over the room for the length of the "
                          "exhibition, and the institution agrees in advance not to cut it back.",
                 "dg-foot"))
    return svg("okoyomon", "Four grids showing the same room at week one, week four, week "
                           "eight and the end of the exhibition, with green cells spreading across it.",
               "".join(p))


def kiwanga():
    """Preservation refused, on a schedule."""
    p = [DEFS]
    p.append(lab(60, 70, "Decay as the instruction", "dg-title"))
    p.append(lab(60, 104, "The arrangement is rebuilt from an archival photograph, then "
                          "left alone. What a visitor sees depends on when they arrive.", "dg-note"))
    p.append(lab(60, 168, "the archival photograph"))
    p.append(box(60, 186, 150, 112))
    p.append(lab(78, 236, "a ceremony at", "dg-lab dg-lab--dim"))
    p.append(lab(78, 256, "which a country", "dg-lab dg-lab--dim"))
    p.append(lab(78, 276, "became independent", "dg-lab dg-lab--dim"))
    p.append(arrow(210, 242, 290, 242))
    p.append(box(300, 186, 170, 112))
    p.append(lab(318, 220, "a florist in the"))
    p.append(lab(318, 242, "host city rebuilds it"))
    p.append(lab(318, 274, "as closely as the record allows", "dg-lab dg-lab--dim"))
    p.append(arrow(470, 242, 550, 242))
    # the decay curve
    p.append(f'<path class="dg-curve" d="M570 200 C700 206 820 250 960 316 '
             f'C1030 350 1080 372 1120 380"/>')
    p.append(f'<line class="dg-axis" x1="570" y1="392" x2="1130" y2="392"/>')
    for i, (t, x) in enumerate([("opening day", 570), ("week two", 756),
                                ("week five", 942), ("closing", 1120)]):
        p.append(f'<line class="dg-tickline" x1="{x}" y1="392" x2="{x}" y2="402"/>')
        p.append(lab(x, 422, t, "dg-lab dg-lab--dim",
                     anchor="start" if i == 0 else ("end" if i == 3 else "middle")))
    for i, (x, y, r) in enumerate([(578, 196, 15), (756, 236, 11), (942, 304, 7),
                                   (1116, 378, 3.5)]):
        p.append(f'<circle class="dg-bloom{" dg-bloom--gone" if i == 3 else ""}" '
                 f'cx="{x}" cy="{y}" r="{r}"/>')
    p.append(lab(1130, 196, "nothing is", "dg-lab dg-lab--live", anchor="end"))
    p.append(lab(1130, 216, "watered, replaced", "dg-lab dg-lab--live", anchor="end"))
    p.append(lab(1130, 236, "or maintained", "dg-lab dg-lab--live", anchor="end"))
    p.append(lab(60, 492, "Sixteen arrangements have been made in the series, each one "
                          "tied to a different independence ceremony.", "dg-foot"))
    return svg("kiwanga", "A ceremony photograph is rebuilt by a florist, then a curve "
                          "shows the arrangement collapsing from opening day to closing, with nothing "
                          "watered or replaced.", "".join(p))


DIAGRAMS = {
    "paterson": paterson(),
    "sonjasdotter": sonjasdotter(),
    "balkin": balkin(),
    "orlow": orlow(),
    "sansour": sansour(),
    "futurefarmers": futurefarmers(),
    "alves": alves(),
    "okoyomon": okoyomon(),
    "kiwanga": kiwanga(),
}

CAPTIONS = {
    "paterson": "How the work is structured. Drawn for this exhibition.",
    "sonjasdotter": "How a gene bank fills up, and how Allkorn runs it backwards. "
                    "Drawn for this exhibition.",
    "balkin": "The same diagram as a seed vault, with the selection step taken out. "
              "Drawn for this exhibition.",
    "orlow": "What happens to each of a plant’s two names. Drawn for this exhibition.",
    "sansour": "Battir measured against a seed vault, function by function. "
               "Drawn for this exhibition.",
    "futurefarmers": "The voyage, and what happens in each port. Drawn for this exhibition.",
    "alves": "Two centuries of accidental storage. Drawn for this exhibition.",
    "okoyomon": "The room over the run of the exhibition. Drawn for this exhibition.",
    "kiwanga": "The schedule the work is built on. Drawn for this exhibition.",
}

if __name__ == "__main__":
    for k, v in DIAGRAMS.items():
        print(f"{k:16} {len(v):6} bytes")
