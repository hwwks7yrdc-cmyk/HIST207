# -*- coding: utf-8 -*-
"""Generates the Duplicate Sample static site into /home/claude/site."""
import os, html, shutil
from PIL import Image
import sitedata as S
import diagrams as DG
import extras as EX
import artists as AR
import entry as EN

IMGDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "site", "assets", "img")
if not os.path.isdir(IMGDIR):
    IMGDIR = "/home/claude/site/assets/img"


def imgsize(name):
    try:
        with Image.open(os.path.join(IMGDIR, name)) as im:
            return im.size
    except Exception:
        return (1400, 900)

OUT = "/home/claude/site"
os.makedirs(OUT, exist_ok=True)

NAV = [("index.html", "Entrance"), ("room-i.html", "Deposit"),
       ("room-ii.html", "Custody"), ("room-iii.html", "Thaw"),
       ("register.html", "Register"), ("team.html", "Team"),
       ("colophon.html", "Colophon")]


def head(title, desc, current, tone="light", extra=""):
    nav = "".join(
        '<a href="{h}"{c}>{t}</a>'.format(h=h, t=t, c=' aria-current="page"' if h == current else "")
        for h, t in NAV)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="author" content="{html.escape(S.TEAM)}">
<meta property="og:type" content="website">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="assets/design/promo.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0b1a24">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preload" href="assets/fonts/lora-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/style.css">
<noscript><style>.field__v{{grid-template-rows:1fr!important}}.reveal{{display:none}}
.hero__again{{display:none}}</style></noscript>
{extra}</head>
<body data-tone="{tone}">
<a class="skip" href="#main">Skip to the exhibition</a>
<header class="bar{' bar--over' if tone in ('hero','dark') else ''}">
  <a class="bar__mark" href="index.html">Duplicate <em>Sample</em></a>
  <nav aria-label="Exhibition">{nav}</nav>
</header>
"""


DEPTH = """<div class="depth" aria-hidden="true">
  <span class="depth__label">depth</span>
  <span class="depth__track">
    <i class="depth__notch" style="top:0"></i>
    <i class="depth__notch" style="top:50%"></i>
    <i class="depth__notch" style="top:100%"></i>
    <i class="depth__fill"></i>
  </span>
  <span class="depth__seen" data-seen hidden><b>0</b>/18</span>
</div>"""


def foot():
    return f"""<footer class="foot">
  <div class="wrap">
    <p><strong>Duplicate Sample.</strong> {html.escape(S.STRAP)}<br>
    Curated by {html.escape(S.TEAM)} for {html.escape(S.COURSE)}, taught by Prof. Rui Hu.</p>
    <div class="foot__row">
      <span>A student exhibition. All works are reproduced for coursework and credited to artist and source.</span>
      <span><a href="colophon.html">Colophon, credits and references</a></span>
    </div>
  </div>
</footer>
<script src="assets/site.js"></script>
</body>
</html>
"""


# ---------------------------------------------------------------- hero motif
def hero_svg():
    cols, rows = 13, 8
    cw, ch, gx, gy = 96, 120, 18, 26
    W = cols * cw + (cols - 1) * gx
    H = rows * ch + (rows - 1) * gy
    live = (7, 2)
    cells = []
    for r in range(rows):
        for q in range(cols):
            x = q * (cw + gx); y = r * (ch + gy)
            if (q, r) == live:
                cells.append(f'<rect class="cell-live" x="{x}" y="{y}" width="{cw}" height="{ch}"/>')
                cells.append(f'<line class="cell-live-line" x1="{x+18}" y1="{y+46}" x2="{x+cw-18}" y2="{y+46}"/>')
                cells.append(f'<line class="cell-live-line" x1="{x+18}" y1="{y+74}" x2="{x+cw-36}" y2="{y+74}"/>')
            else:
                cells.append(f'<rect class="cell" x="{x}" y="{y}" width="{cw}" height="{ch}"/>')
                cells.append(f'<line class="cell-line" x1="{x+18}" y1="{y+46}" x2="{x+cw-18}" y2="{y+46}"/>')
                cells.append(f'<line class="cell-line" x1="{x+18}" y1="{y+74}" x2="{x+cw-36}" y2="{y+74}"/>')
    lx = live[0] * (cw + gx) + cw / 2
    ly = live[1] * (ch + gy)
    stem = (f'<path class="stem" d="M{lx} {ly} C{lx+14} {ly-62} {lx-14} {ly-124} {lx+4} {ly-196}"/>'
            f'<ellipse class="leaf leaf--a" cx="{lx-26}" cy="{ly-96}" rx="20" ry="11" '
            f'transform="rotate(-24 {lx-26} {ly-96})"/>'
            f'<ellipse class="leaf leaf--b" cx="{lx+30}" cy="{ly-148}" rx="20" ry="11" '
            f'transform="rotate(22 {lx+30} {ly-148})"/>')
    return f"""<svg class="hero__grid" viewBox="0 -210 {W} {H+210}" preserveAspectRatio="xMidYMid slice"
   role="img" aria-label="A field of sealed storage boxes, one of them open with a seedling growing out of it.">
  <defs>
    <linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0b1a24" stop-opacity="0"/>
      <stop offset="52%" stop-color="#0b1a24" stop-opacity=".55"/>
      <stop offset="100%" stop-color="#0b1a24" stop-opacity=".97"/>
    </linearGradient>
  </defs>
  <g>{''.join(cells)}</g>
  {stem}
  <rect x="0" y="-210" width="{W}" height="{H+210}" fill="url(#fade)"/>
</svg>"""


def hero_sprout():
    """Three sealed boxes, one of them open, with the seedling growing out of it.

    The drawn field of 104 boxes behind the title was hidden the moment a
    photograph of the vault was cleared, because a drawn field fights a
    photograph of the real thing. That hid the seedling with it, and the
    seedling is the only mark in the identity that sets something living
    against something sealed.

    It comes back at the size of a caption rather than a background: three
    accessions on the snow beside the door, and the one in the middle has
    opened. One box alone would read as a green panel, because nothing around
    it would be shut.

    Same classes as the grid, so the growth animation and the reduced-motion
    rule that stops it both apply without a second set of rules. Only the
    colours are restated, because strokes mixed for a dark flat ground
    disappear against a photograph.
    """
    cw, ch, gx = 96, 120, 18
    live = 1                                   # the middle one
    parts = []
    for i in range(3):
        x = i * (cw + gx)
        k = "cell-live" if i == live else "cell"
        parts.append(f'<rect class="{k}" x="{x}" y="0" width="{cw}" height="{ch}"/>')
        parts.append(f'<line class="{k}-line" x1="{x + 18}" y1="46" x2="{x + cw - 18}" y2="46"/>')
        parts.append(f'<line class="{k}-line" x1="{x + 18}" y1="74" x2="{x + cw - 36}" y2="74"/>')
    lx = live * (cw + gx) + cw / 2
    parts.append(f'<path class="stem" d="M{lx} 0 C{lx + 14} -62 {lx - 14} -124 {lx + 4} -196"/>')
    parts.append(f'<ellipse class="leaf leaf--a" cx="{lx - 26}" cy="-96" rx="21" ry="11.5" '
                 f'transform="rotate(-24 {lx - 26} -96)"/>')
    parts.append(f'<ellipse class="leaf leaf--b" cx="{lx + 30}" cy="-148" rx="21" ry="11.5" '
                 f'transform="rotate(22 {lx + 30} -148)"/>')
    w = 3 * cw + 2 * gx
    return f"""<svg class="hero__sprout" viewBox="-14 -216 {w + 28} {ch + 232}"
   role="img" aria-label="Three sealed storage boxes, the middle one open with a seedling growing out of it.">
  {''.join(parts)}
</svg>"""


# ---------------------------------------------------------------- index
def descent():
    """The entry sequence, laid out in 3D depth.

    Everything is computed here and handed to CSS as custom properties, so the
    stylesheet holds no numbers that belong to the score and the script holds
    none at all. The whole block ships with `hidden` on it: with JavaScript off
    it never appears, and the entrance behaves exactly as it did before.

    Each object gets three numbers. --z is how far down the corridor it sits;
    --in and --dur are when its fade starts and how long it runs, both derived
    from the distance at which that kind of object should appear and vanish
    rather than from a span of seconds. Negative starts are deliberate: the
    object is already part way into its approach on the opening frame, under
    the stage's own fade up out of the dark.
    """
    parts = []
    for item in EN.SCORE:
        kind, at = item[0], item[-1]
        z = EN.depth_for(at)
        begin, dur = EN.window(kind, z)
        base = f'--z:{z};--in:{begin}s;--dur:{dur}s'
        if kind == "ring":
            parts.append(f'<i class="tun__ring" style="{base}"></i>')
        elif kind == "ask":
            q = EN.QUESTIONS[item[1]]
            off = f';--y:{EN.vertical(item[2])}' if item[2] else ""
            parts.append(f'<p class="tun__ask" style="{base}{off}">{html.escape(q)}</p>')
        else:
            slug, x, y = item[1], item[2], item[3]
            cap = EN.PLATE_CAP[slug]
            parts.append(
                f'<figure class="tun__plate" '
                f'style="{base};--x:{EN.lateral(x)};--y:{EN.vertical(y)}">'
                f'<img src="assets/img/tun-{slug}.jpg" alt="" width="420" height="300" '
                f'decoding="async">'
                f'<figcaption>{html.escape(cap)}</figcaption></figure>')

    # the door, the one object the camera never reaches
    d = EN.DOOR
    parts.append(f"""<div class="tun__door" style="--z:{EN.DOOR_Z};--in:{EN.DOOR_IN}s">
      <p class="tun__k">{html.escape(d['kicker'])}</p>
      <p class="tun__word">{html.escape(d['word'])}</p>
      <p class="tun__line">{html.escape(d['line'])}</p>
    </div>""")

    # the still version, for anyone who has asked their system to reduce motion:
    # the same five questions and the same door, held still
    still = "".join(f"<li>{html.escape(q)}</li>" for q in EN.QUESTIONS)

    return f"""<div class="tun" id="descent" hidden
     style="--travel:{EN.TRAVEL}px;--dur-fly:{EN.DURATION}s"
     role="dialog" aria-label="Entry sequence">
  <div class="tun__space" aria-hidden="true"><div class="tun__stage">{''.join(parts)}</div></div>
  <div class="tun__still" aria-hidden="true">
    <ol>{still}</ol>
    <p class="tun__still-door">{html.escape(d['word'])}</p>
  </div>
  <button class="tun__skip" type="button">Skip<span> the descent</span></button>
</div>
"""


def build_index():
    rooms_html = ""
    for r in S.ROOMS:
        works = [w for w in S.WORKS if w["room"] == r["n"]]
        items = "".join(f"<li>{html.escape(w['artist'])}</li>" for w in works)
        rooms_html += f"""<a class="room-card" href="{r['slug']}.html">
      <span class="room-card__n">Room {r['n']}</span>
      <h3>{r['name']}</h3>
      <p>{html.escape(r['line'])}</p>
      <ul>{items}</ul>
      <span class="room-card__go">Enter &rarr;</span>
    </a>"""

    statement = "".join(f"<p>{t}</p>" for t in S.STATEMENT)
    facts = "".join(f"<div><dt>{html.escape(k)}</dt><dd>{html.escape(v)}</dd></div>" for k, v in S.VAULT_FACTS)
    q1, c1 = S.TSING[0]
    q2, c2 = S.TSING[1]
    q3, c3 = S.TSING[2]

    body = f"""{descent()}
{DEPTH}
<main id="main">

<section class="hero{' hero--photo' if has_asset('img/svalbard.jpg') else ''}">
  {anchor_image("hero")}
  {hero_svg()}
  {hero_sprout() if has_asset('img/svalbard.jpg') else ''}
  <div class="hero__inner">
    <h1><span>Duplicate</span><span class="it">Sample</span></h1>
    <p class="hero__strap">{html.escape(S.STRAP)}</p>
    <div class="hero__mark"></div>
    <div class="hero__meta">
      <span>Nine artists</span><span>Three rooms</span>
      <span>{html.escape(S.COURSE)}</span>
    </div>
    <div class="hero__cues">
      <a class="hero__scroll" href="#statement"><span></span>Descend</a>
      <!-- the entry sequence plays once per visitor, so the way back to it has to
           be somewhere a visitor will actually look, not only in the colophon -->
      <a class="hero__again" href="index.html#descend">Replay the entry</a>
    </div>
    {'<p class="hero__credit">Svalbard Global Seed Vault, Spitsbergen. Photograph by Bjoertvedt, CC BY-SA 3.0, via Wikimedia Commons. The mirrored work above the entrance is <cite>Perpetual Repercussion</cite> by Dyveke Sanne.</p>' if has_asset('img/svalbard.jpg') else ''}
  </div>
</section>

<section class="band" id="statement">
  <div class="wrap">
    <div class="cols cols--side">
      <div>
        <p class="kicker">Curatorial statement</p>
        <div class="lede--run narrow">{statement}</div>
      </div>
      <aside>
        <p class="kicker">The reference point</p>
        <h3>Svalbard Global Seed Vault</h3>
        <p class="muted">Not an artwork, and not exhibited as one. It is the practice the nine works are
        arranged around.</p>
        <dl class="facts">{facts}</dl>
      </aside>
    </div>
  </div>
</section>

{preview_wall()}

<section class="band dark">
  <div class="wrap">
    <p class="kicker">The idea the exhibition runs on</p>
    <h2>The plantation, and the unruly edge</h2>
    <div class="cols cols--2">
      <div>
        <p class="muted">Anna Tsing begins from a single claim, and the whole essay follows from it.</p>
        <blockquote class="pull"><p>&ldquo;{html.escape(q1)}&rdquo;</p><footer>{html.escape(c1)}</footer></blockquote>
        <p class="muted" style="margin-top:2rem">From there she describes two opposed ways of living with other
        species. The first is the plantation: it isolates one organism, standardises it, strips away its
        relationships, and organises who has access. She points out that this is not natural and had to be learned.</p>
        <blockquote class="pull"><p>&ldquo;{html.escape(q2)}&rdquo;</p><footer>{html.escape(c2)}</footer></blockquote>
      </div>
      <div>
        <p class="muted">Against it she sets the unruly edge: the margin around managed space, where species
        collaborate without anyone&rsquo;s permission. She makes a strong empirical claim about it.</p>
        <blockquote class="pull"><p>&ldquo;{html.escape(q3)}&rdquo;</p><footer>{html.escape(c3)}</footer></blockquote>
        <p class="muted" style="margin-top:2rem">Read through Tsing, a seed vault is a plantation answer to loss,
        and a careful one. It isolates a sample, holds it at a fixed temperature, separates it from the soil and
        the people it came from, and controls who may take it out. That is a description of a method, not an
        accusation: the method works, and it has saved material that would otherwise be gone.</p>
        <p class="muted">It is also one method among several. This exhibition sets it beside the others.</p>
      </div>
    </div>
  </div>
</section>

<section class="band--tight">
  <div class="wrap">
    <p class="kicker">The descent</p>
    <figure class="planwrap">
      {floorplan()}
      <figcaption>Three chambers, nine slots. Click a slot to go straight to that work,
      or take the rooms in order below.</figcaption>
    </figure>
  </div>
  <div class="rooms">{rooms_html}</div>
</section>

<section class="band">
  <div class="wrap">
    <div class="cols cols--side">
      <div>
        <p class="kicker">How to read the exhibition</p>
        <h2>Every work carries the same label</h2>
        <p class="lede">Four lines, identical on all nine pages. What is kept. Who deposited it. Who may
        withdraw it. What was left out.</p>
        <p class="muted">The first two are open. The last two are hidden until you click, so that retrieving the
        political content of a collection is a small act you perform rather than a sentence you are handed. By
        the third or fourth work you will be reading the fields before the picture, which is the point.</p>
        <p class="muted">A thin rule down the right edge shows how deep you have gone. There is no menu inside a
        room. The only way through is down.</p>
      </div>
      <div>
        <dl class="label" style="position:static">
          <p class="label__h">The label <span class="code">DS &ndash; II &ndash; 02</span></p>
          <div class="field"><dt>What is kept</dt>
            <dd>About forty-seven heirloom varieties, in jars, coated in ash.</dd></div>
          <div class="field"><dt>Who deposited it</dt>
            <dd>Farmers across the West Bank, and the artist.</dd></div>
          <div class="field field--hidden" data-open="false">
            <dt>Who may withdraw it <button class="reveal" type="button">reveal</button></dt>
            <dd class="field__v"><span>Anyone who comes to the house in Battir. No record is kept.</span></dd></div>
          <div class="field field--hidden" data-open="false">
            <dt>What was left out <button class="reveal" type="button">reveal</button></dt>
            <dd class="field__v"><span>No accession list exists, so nothing can be audited, including loss.</span></dd></div>
          <p class="label__foot">Try it. This is the live label from Room II.</p>
        </dl>
      </div>
    </div>
  </div>
</section>

<section class="onward">
  <div class="wrap">
    <a href="room-i.html">
      <div class="onward__row">
        <div>
          <p class="onward__k">Begin &middot; Room I</p>
          <h2>Deposit</h2>
          <p>What is selected, purified and put away.</p>
        </div>
        <span class="onward__arrow">&darr;</span>
      </div>
    </a>
  </div>
</section>

</main>"""
    return head("Duplicate Sample · seed banks and the keeping of living things",
                S.STRAP + ". Nine contemporary artists, three rooms, an online exhibition for ARTS / HIST 207.",
                "index.html", tone="hero") + body + foot()


# ---------------------------------------------------------------- a work
def work_html(w, r):
    ph = w.get("placeholder")
    label = ""
    for i, (k, v) in enumerate(w["label"]):
        if i < 2:
            label += (f'<div class="field"><dt>{html.escape(k)}</dt>'
                      f'<dd>{html.escape(v)}</dd></div>')
        else:
            ask = ""
            if i == 2:
                ask = (f'<a class="field__ask" href="withdrawal.html?work={w["slug"]}">'
                       f'Make a request &rarr;</a>')
            label += (f'<div class="field field--hidden" data-open="false" '
                      f'data-key="{w["slug"]}-{i}">'
                      f'<dt>{html.escape(k)} <button class="reveal" type="button">reveal</button></dt>'
                      f'<dd class="field__v"><span>{html.escape(v)}{ask}</span></dd></div>')

    quote = ""
    if w.get("quote"):
        qt, qa = w["quote"]
        quote = (f'<blockquote class="pull" style="margin:2rem 0 0">'
                 f'<p>&ldquo;{html.escape(qt)}&rdquo;</p>'
                 f'<footer>{html.escape(qa)}</footer></blockquote>')

    desc = "".join(f"<p>{html.escape(d) if '<' not in d else d}</p>" for d in w["desc"])
    link = ""

    iw, ih = imgsize(w["img"])
    held = " work__fig--held" if iw < 1300 else ""

    return f"""<article class="work" id="{w['slug']}">
  <figure class="work__fig{held}">
    <img src="assets/img/{w['img']}" alt="{html.escape(w['alt'])}"
         width="{iw}" height="{ih}" loading="lazy" decoding="async">
    <figcaption>{w['caption']}</figcaption>
  </figure>
  <div class="work__body">
    <div class="wrap">
      <div class="work__head">
        <span class="code">{w['code']}</span>
        <span class="work__room">Room {r['n']} &middot; {r['name']}</span>
      </div>
      <div class="cols cols--side">
        <div>
          <h2>{html.escape(w['artist'])}</h2>
          <p class="work__title"><cite>{html.escape(w['work'])}</cite>, {html.escape(w['date'])}</p>
          <p class="work__meta"><span>{html.escape(w['born'])}</span><span>{html.escape(w['medium'])}</span></p>
          {desc}
          {quote}
          <div class="work__note"><b>Why this room</b>{html.escape(w['note'])}</div>
          {link}
        </div>
        <aside>
          <dl class="label">
            <p class="label__h">The label <span class="code">{w['code']}</span></p>
            {label}
          </dl>
        </aside>
      </div>
    </div>
  </div>
  {dossier(w)}
</article>"""


# ---------------------------------------------------------------- room page
def build_room(i):
    r = S.ROOMS[i]
    works = [w for w in S.WORKS if w["room"] == r["n"]]
    listing = "".join(
        f"<li><b>{html.escape(w['artist'])}</b>, <cite>{html.escape(w['work'])}</cite>, {html.escape(w['date'])}</li>"
        for w in works)

    if i + 1 < len(S.ROOMS):
        nxt = S.ROOMS[i + 1]
        onward = f"""<section class="onward">
  <div class="wrap"><a href="{nxt['slug']}.html"><div class="onward__row"><div>
    <p class="onward__k">Continue &middot; Room {nxt['n']}</p>
    <h2>{nxt['name']}</h2><p>{html.escape(nxt['line'])}</p>
  </div><span class="onward__arrow">&darr;</span></div></a></div>
</section>"""
    else:
        onward = """<section class="onward">
  <div class="wrap"><a href="index.html"><div class="onward__row"><div>
    <p class="onward__k">The cold room &middot; the way out</p>
    <h2>Return to the door</h2>
    <p>Syria made the first withdrawal from Svalbard in 2015, after the gene bank in Aleppo
    was damaged. The vault did exactly what it was built to do.</p>
  </div><span class="onward__arrow">&uarr;</span></div></a></div>
</section>"""

    body = f"""{DEPTH}
<main id="main">

<section class="threshold">
  <div class="wrap">
    <p class="threshold__n">Room {r['n']}</p>
    <h1>{r['name']}</h1>
    <p class="threshold__line">{html.escape(r['line'])}</p>
    <p class="threshold__text">{html.escape(r['text'])}</p>
    <ul class="threshold__list">{listing}</ul>
  </div>
</section>

{wall(r, works) if r['n'] == "II" else ""}

{''.join(work_html(w, r) for w in works)}

{onward}
</main>"""
    return head(f"{r['name']} · Room {r['n']} · Duplicate Sample",
                f"Room {r['n']} of Duplicate Sample. {r['line']}",
                f"{r['slug']}.html", tone="dark") + body + foot()


# ---------------------------------------------------------------- colophon
def build_colophon():
    refs = "".join(f"<li>{t}</li>" for t in S.REFERENCES)
    credits = ""
    for w in S.WORKS:
        cap = w["caption"].replace("Image to be sourced. ", "")
        if w.get("placeholder"):
            line = (f"<cite>{html.escape(w['work'])}</cite>, {html.escape(w['date'])}. "
                    f"No image has been cleared, so the page carries a designed placeholder "
                    f"in the exhibition identity. {cap}")
        else:
            line = f"{cap} Reproduced from the artist&rsquo;s own documentation."
        credits += f"<div><dt>{html.escape(w['artist'])}</dt><dd>{line}</dd></div>"

    body = f"""{DEPTH}
<main id="main">
<section class="band">
  <div class="wrap">
    <p class="kicker">Colophon</p>
    <h2>How this exhibition was made</h2>
    <div class="cols cols--side" style="margin-top:2rem">
      <div class="narrow">
        <p class="lede">Duplicate Sample was curated by {html.escape(S.TEAM)} for {html.escape(S.COURSE)},
        taught by Prof. Rui Hu.</p>
        <p class="muted">The exhibition is a static site of linked pages. We chose pages over a
        three-dimensional environment because these works already reach their audiences as documentation,
        and we would rather present that documentation clearly than rebuild it inside a game engine. The
        precedent is <cite>WE=LINK: Ten Easy Pieces</cite>, curated by Zhang Ga at Chronus Art Center
        Shanghai in 2020 with Rhizome and Art Center Nabi, which presented network-native commissions as
        web pages.</p>
        <p class="muted">The spatial design is the descent: three rooms passed through in order, a
        threshold panel between each, one work per screen, and a depth marker down the right edge. There
        is no menu inside a room.</p>
        <p class="muted">Under every work sits a dossier, so the exhibition holds its own material rather
        than sending visitors away to find it. Each one carries a diagram drawn for this show setting out
        how that particular collection operates, a paragraph on the artist&rsquo;s practice with their own
        words where a source could be verified, and a curators&rsquo; note written to be read aloud. The
        artist&rsquo;s own site appears at the end of the dossier as somewhere to go afterwards, not as the
        only way to see anything.</p>
        <p class="muted">The nine diagrams are original drawings by the curators. Every figure in them
        comes from the verified entry for that work: the twelve manuscripts deposited so far, the
        forty-seven varieties in Battir, the sixteen floral arrangements, the two refused submissions.
        None of them invents a number.</p>
        <p class="muted">The site is hand-written HTML, CSS and JavaScript with no framework and no build
        step, hosted on GitHub Pages. Type is self-hosted, so the pages load without a single third-party
        request. Total weight is under two megabytes.</p>
        <p class="muted">Four things on the site ask something of the visitor rather than only showing
        them something. The <a href="index.html#statement">plan</a> on the entrance lets anyone enter at
        a particular work instead of walking the rooms in order. Every label keeps two of its four fields
        shut until they are opened, and the site counts how many of the eighteen a visitor has opened,
        reporting it at the end. The <a href="register.html">register</a> lays all nine accessions out as
        an inventory that can be filtered by who is permitted to withdraw, which is where the collection
        splits into three groups of three. The <a href="withdrawal.html">withdrawal slip</a> lets a
        visitor write a formal request for any of the material and keep it.</p>
        <p class="muted">That last one stores nothing. Everything typed into it stays in the visitor&rsquo;s
        own browser and is gone when the window closes. A real vault that accepts requests necessarily
        keeps a register of everyone who asked, and that register is a form of control in its own right.
        Declining to keep one is the only position this exhibition can take that a seed bank cannot.</p>
      </div>
      <div>
        <p class="kicker">Team</p>
        <dl class="facts">
          <div><dt>Research and texts</dt><dd>Tim Maurice Steiner</dd></div>
          <div><dt>Design and identity</dt><dd>Qing Guo</dd></div>
          <div><dt>Build and media</dt><dd>Seble Getaneh</dd></div>
          <div><dt>Selection</dt><dd>All three</dd></div>
        </dl>
      </div>
    </div>
  </div>
</section>

<section class="band dark">
  <div class="wrap">
    <p class="kicker">Visual identity</p>
    <h2>The storage box, not the seedling</h2>
    <div class="cols cols--side" style="margin-top:2rem">
      <div>
        <p class="muted">The identity is drawn from the storage box and the accession label. Everything is
        cold and rectilinear except one element, which is alive and out of place. Green appears on roughly
        five per cent of any screen, and it marks only the thing that is alive or escaping.</p>
        <ul class="swatches" style="margin-top:1.8rem">
          <li><i style="background:#0b1a24"></i>#0B1A24</li>
          <li><i style="background:#e8eef2"></i>#E8EEF2</li>
          <li><i style="background:#5c7a8c"></i>#5C7A8C</li>
          <li><i style="background:#4e8c5b"></i>#4E8C5B</li>
        </ul>
        <p class="muted">Display and reading type is Lora; labels, field names and accession codes are set
        in Poppins and a monospace. Both typefaces are used under the SIL Open Font License and are served
        from this site.</p>
        <p class="muted">Every work runs under a code in the form DS&ndash;I&ndash;01, which gives the
        exhibition an inventory and lets the team refer to works without ambiguity.</p>
        <p class="muted">The entrance opens with a descent down a corridor, past the nine
        accessions, through the four questions every label in the exhibition asks and the one
        it ends on. It plays on every arrival and can be skipped at any point, with the button
        on screen or with a single key. <a href="index.html#descend">Play it again</a>.</p>
      </div>
      <div class="assets">
        <figure>
          <img src="assets/design/poster.jpg" alt="The exhibition poster: the title in a large serif over a grid of sealed boxes, one of them green with a seedling." width="900" height="1273" loading="lazy">
          <figcaption>Poster, A2. <a href="assets/design/poster-a2.pdf">Print PDF</a></figcaption>
        </figure>
        <figure>
          <img src="assets/design/promo.jpg" alt="The square promotional image, carrying the same grid motif." width="1080" height="1080" loading="lazy">
          <figcaption>Promotional image, 1080&times;1080</figcaption>
        </figure>
      </div>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <p class="kicker">Image credits and rights</p>
    <h2>Where each image comes from</h2>
    <p class="muted narrow" style="margin-top:1.4rem">All works remain the property of their artists. Images
    are reproduced here for a student exhibition and are credited to artist and source on the page where they
    appear. Where no image has yet been cleared, the page carries a designed placeholder in the exhibition
    identity rather than a borrowed photograph. Eight of the nine now carry a gallery of documentation of the
    work itself, taken from the artist\u2019s own site, their distributor or the institution that showed it,
    and credited image by image. Only Precious Okoyomon\u2019s <cite>Earthseed</cite> still waits for a cleared
    installation view. The nine diagrams, the nine curators\u2019 notes, the poster and the one remaining
    placeholder card were made for this exhibition by the curators, and the diagrams are marked on every page
    as our reading rather than material from the artist.</p>
    <p class="muted narrow">Six of the nine pages link a recording of the artist speaking about the work:
    a public radio programme, a symposium a gallery recorded and published itself, and three podcasts. None
    of it was made by us and none of it is copied here. Each one is named, dated and linked, and plays on the
    site that published it, which is also why no player is embedded: this exhibition makes no third-party
    request of any kind. Katie Paterson’s page carries a sentence quoted from NPR’s own published
    transcript; the other recordings have no transcript, so they are linked and described rather than quoted.
    Three works carry no recording. Åsa Sonjasdotter’s film has its own sound, and the excerpt
    Filmform publishes is already linked on her page; for Maria Thereza Alves and Futurefarmers every
    published interview we could find is in print. We would rather leave those three empty than fill them
    with a recording about something else.</p>
    <p class="muted narrow">The photograph at the entrance is of the Svalbard Global Seed Vault on
    Spitsbergen, by Bjoertvedt, published on Wikimedia Commons under a Creative Commons
    Attribution-ShareAlike 3.0 licence. The mirrored work above the vault door is
    <cite>Perpetual Repercussion</cite> by Dyveke Sanne, and we name it here because an exhibition about
    who may hold what should not let an artwork pass as an architectural detail.</p>
    <dl class="facts" style="margin-top:2rem">{credits}</dl>
  </div>
</section>

<section class="band" style="background:var(--soft)">
  <div class="wrap">
    <p class="kicker">References</p>
    <h2>Sources</h2>
    <ul class="reflist" style="margin-top:1.6rem">{refs}</ul>
  </div>
</section>
</main>"""
    return head("Colophon · Duplicate Sample",
                "Credits, image rights, visual identity and references for the exhibition Duplicate Sample.",
                "colophon.html") + body + foot()


# ---------------------------------------------------------------- favicon
FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <rect width="64" height="64" fill="#0b1a24"/>
  <g fill="none" stroke="#2a3f4d" stroke-width="2">
    <rect x="6" y="34" width="14" height="20"/><rect x="44" y="34" width="14" height="20"/>
  </g>
  <rect x="25" y="34" width="14" height="20" fill="#4e8c5b"/>
  <path d="M32 34 C35 25 29 18 33 9" fill="none" stroke="#4e8c5b" stroke-width="3" stroke-linecap="round"/>
  <ellipse cx="25" cy="21" rx="6" ry="3.4" fill="#4e8c5b" transform="rotate(-25 25 21)"/>
</svg>
"""

# ---------------------------------------------------------------- floor plan
def floorplan():
    """A drawn plan of the three chambers. Each slot links to its work."""
    W, H = 1200, 520
    chambers = [(40, 40), (430, 160), (820, 280)]      # top-left of each room
    cw, ch = 340, 200
    parts = []

    # corridors between chambers, drawn first so the rooms sit on top
    for i in range(len(chambers) - 1):
        x1 = chambers[i][0] + cw
        y1 = chambers[i][1] + ch / 2
        x2 = chambers[i + 1][0]
        y2 = chambers[i + 1][1] + ch / 2
        parts.append(f'<path class="pl-link" d="M{x1} {y1} H{(x1+x2)/2} V{y2} H{x2}"/>')

    # the way in
    parts.append(f'<path class="pl-link" d="M0 {40 + ch/2} H40"/>')
    parts.append(f'<text class="pl-note" x="4" y="{40 + ch/2 - 14}">in</text>')
    parts.append(f'<path class="pl-link pl-link--out" d="M{820+cw} {280+ch/2} H{W}"/>')
    parts.append(f'<text class="pl-note" x="{W-28}" y="{280 + ch/2 - 14}">out</text>')

    for r, (ox, oy) in zip(S.ROOMS, chambers):
        works = [w for w in S.WORKS if w["room"] == r["n"]]
        parts.append(f'<rect class="pl-room" x="{ox}" y="{oy}" width="{cw}" height="{ch}"/>')
        parts.append(f'<text class="pl-n" x="{ox+16}" y="{oy+30}">Room {r["n"]}</text>')
        parts.append(f'<text class="pl-name" x="{ox+16}" y="{oy+ch-16}">{r["name"]}</text>')
        for j, w in enumerate(works):
            sx = ox + 18 + j * 108
            sy = oy + 50
            surname = w["artist"].split()[-1]
            parts.append(
                f'<a class="pl-slot" href="{r["slug"]}.html#{w["slug"]}" '
                f'aria-label="Room {r["n"]}, {html.escape(w["artist"])}, '
                f'{html.escape(w["work"])}">'
                f'<title>{html.escape(w["artist"])}, {html.escape(w["work"])}</title>'
                f'<rect x="{sx}" y="{sy}" width="100" height="84" rx="2"/>'
                f'<text class="pl-code" x="{sx+10}" y="{sy+24}">{w["code"].split("–")[-1].strip()}</text>'
                f'<text class="pl-who" x="{sx+10}" y="{sy+70}">{html.escape(surname)}</text>'
                f'</a>')

    return (f'<svg class="plan" viewBox="0 0 {W} {H}" role="group" '
            f'aria-label="Plan of the three rooms. Nine slots, each linking to a work.">'
            + "".join(parts) + "</svg>")


# A curatorial reading of the withdrawal field, not a string match. Three groups,
# and the exhibition happens to split evenly across them.
ACCESS = {
    "orlow": "open", "sansour": "open", "futurefarmers": "open",
    "sonjasdotter": "named", "alves": "named", "kiwanga": "named",
    "paterson": "none", "balkin": "none", "okoyomon": "none",
}
ACCESS_LABEL = {"open": "Anyone may take it",
                "named": "Only named parties",
                "none": "No one takes anything out"}


# ---------------------------------------------------------------- preview wall
def preview_wall():
    """Nine tiles, one per work, so the entrance shows what is actually inside
    before anyone commits to the descent."""
    tiles = ""
    for w in S.WORKS:
        r = next(x for x in S.ROOMS if x["n"] == w["room"])
        # the tile is drawn at about 480px, so it takes the small copy made by
        # entryplates.py and falls back to the full image if that is missing
        small = "tile-" + w["slug"] + ".jpg"
        src = small if has_asset("img/" + small) else w["img"]
        iw, ih = imgsize(src)
        tiles += f"""<a class="tile" href="{r['slug']}.html#{w['slug']}">
      <img src="assets/img/{src}" alt="" width="{iw}" height="{ih}"
           loading="lazy" decoding="async">
      <span class="tile__v">
        <span class="code">{w['code']}</span>
        <b>{html.escape(w['artist'])}</b>
        <i>{html.escape(w['work'])}</i>
      </span>
    </a>"""
    return f"""<section class="preview" aria-label="The nine works">
  <div class="wrap">
    <p class="kicker">What is inside</p>
    <h2>Nine collections, and the rules each one runs on</h2>
  </div>
  <div class="tiles">{tiles}</div>
  <div class="wrap">
    <p class="preview__note">One of the nine is shown here by a designed card rather than
    a photograph, because no installation view of it has been cleared. Its page says so on
    its face.</p>
  </div>
</section>"""


# ---------------------------------------------------------------- the anchor image
def anchor_image(kind):
    """The vault photograph, if one has been cleared. Until then the drawn motif
    stands in its place, and the colophon records what is missing."""
    if has_asset("img/svalbard.jpg"):
        iw, ih = imgsize("svalbard.jpg")
        return (f'<img class="anchorimg" src="assets/img/svalbard.jpg" alt="The entrance '
                f'to the Svalbard Global Seed Vault, cut into the mountainside above '
                f'Longyearbyen." width="{iw}" height="{ih}" '
                f'{"fetchpriority=\'high\'" if kind == "hero" else "loading=\'lazy\'"}>')
    return ""


# ---------------------------------------------------------------- dossier
def has_asset(rel):
    return os.path.isfile(os.path.join(OUT, "assets", rel))


def dossier(w):
    """What the exhibition holds on this work beyond the opening photograph.
    Documentation of the work comes first. The drawn figure comes last and is
    marked as what it is: our reading, not material from the project."""
    slug = w["slug"]
    parts = []

    # 1. further documentation of the work itself
    extra = [e for e in EX.EXTRA.get(slug, []) if has_asset("img/" + e[0])]
    if extra:
        figs = ""
        for fn, alt, cap in extra:
            iw, ih = imgsize(fn)
            figs += (f'<figure class="gal__f"><img src="assets/img/{fn}" '
                     f'alt="{html.escape(alt)}" width="{iw}" height="{ih}" '
                     f'loading="lazy" decoding="async">'
                     f'<figcaption>{cap}</figcaption></figure>')
        parts.append(f"""<section class="dos__item">
      <p class="dos__k">More of the work <span>{len(extra) + 1} images in total</span></p>
      <div class="gal">{figs}</div>
    </section>""")

    # 2. the artist: practice, and their own words where a source could be verified
    q = ""
    if slug in AR.QUOTE:
        qt, qc = AR.QUOTE[slug]
        q = (f'<blockquote class="dos__said"><p>&ldquo;{html.escape(qt)}&rdquo;</p>'
             f'<footer>{html.escape(qc)}</footer></blockquote>')
    parts.append(f"""<section class="dos__item">
      <p class="dos__k">The artist</p>
      <div class="dos__bio">
        <p class="dos__who">{html.escape(w["artist"])} &middot; {html.escape(w["born"])}</p>
        <p>{html.escape(" ".join(AR.STATEMENT[slug].split()))}</p>
        {q}
      </div>
    </section>""")

    # 3. film, sound and archives held by the project itself
    src = EX.SOURCE_MEDIA.get(slug, [])
    if src:
        items = "".join(f'<li><a href="{u}" rel="noopener">{html.escape(t)}</a></li>'
                        for t, u in src)
        parts.append(f"""<section class="dos__item">
      <p class="dos__k">Held by the project <span>film, sound and archives, at the source</span></p>
      <ul class="dos__src">{items}</ul>
    </section>""")

    # 3b. the artist speaking, recorded and published by somebody else.
    # Named, dated and linked, never copied: none of it is ours, and the site
    # makes no third-party request, so each one plays where it was published.
    hear = EX.LISTEN.get(slug, [])
    if hear:
        items = ""
        for h in hear:
            said = ""
            if h["quote"]:
                said = (f'<blockquote class="dos__said"><p>&ldquo;'
                        f'{html.escape(h["quote"])}&rdquo;</p>'
                        f'<footer>{html.escape(h["said"])}</footer></blockquote>')
            items += (f'<li><a href="{h["url"]}" rel="noopener">'
                      f'{html.escape(h["label"])}</a>'
                      f'<span class="dos__hear-what">{h["what"]}</span>{said}</li>')
        parts.append(f"""<section class="dos__item">
      <p class="dos__k">The artist, recorded <span>published elsewhere, and played there</span></p>
      <ul class="dos__hear">{items}</ul>
    </section>""")

    # 4. the curators' note
    parts.append(f"""<section class="dos__item">
      <p class="dos__k">Curators\u2019 note</p>
      <blockquote class="dos__script"><p>{html.escape(EX.script(slug))}</p></blockquote>
    </section>""")

    # 5. last, and clearly ours rather than the artist's
    parts.append(f"""<section class="dos__item dos__item--ours">
      <p class="dos__k">A reading, not a document <span>drawn by the curators</span></p>
      <figure class="dos__dia">
        {DG.DIAGRAMS[slug]}
        <figcaption>{DG.CAPTIONS[slug]} It is our interpretation of how the
        collection operates, and no part of it comes from the artist.</figcaption>
      </figure>
    </section>""")

    link = ""
    if w.get("link"):
        lt, lu = w["link"]
        link = (f'<p class="dos__away">Afterwards, the artist\u2019s own record of the work: '
                f'<a href="{lu}" rel="noopener">{html.escape(lt)}</a></p>')

    return f"""<div class="dos">
    <div class="wrap">
      <div class="dos__grid">{"".join(parts)}</div>
      {link}
    </div>
  </div>"""


# ---------------------------------------------------------------- the wall
def wall(r, works):
    """Room II hangs its three works along one continuous wall you move across,
    before the same three appear in full below. Native horizontal scroll with
    snapping, so a trackpad, a wheel, a swipe and the arrow keys all work."""
    plates = ""
    for w in works:
        iw, ih = imgsize(w["img"])
        plates += f"""<a class="plate" href="#{w['slug']}">
        <span class="plate__img"><img src="assets/img/{w['img']}"
          alt="" width="{iw}" height="{ih}" loading="lazy" decoding="async"></span>
        <span class="plate__cap">
          <span class="code">{w['code']}</span>
          <b>{html.escape(w['artist'])}</b>
          <i>{html.escape(w['work'])}</i>
          <em>Read the entry &darr;</em>
        </span>
      </a>"""
    return f"""<section class="wall" aria-label="The wall of Room {r['n']}">
  <div class="wall__lead">
    <p class="kicker">The wall</p>
    <p>Three collections hung along one wall. Move across it, then read them in order below.</p>
    <p class="wall__hint" aria-hidden="true">scroll sideways &rarr;</p>
  </div>
  <div class="wall__track" tabindex="0" role="group"
       aria-label="Three works, scrolls horizontally">{plates}</div>
</section>"""


# ---------------------------------------------------------------- register
def build_register():
    rows = ""
    for w in S.WORKS:
        r = next(x for x in S.ROOMS if x["n"] == w["room"])
        withdraw = w["label"][2][1]
        left = w["label"][3][1]
        open_access = ACCESS[w["slug"]]
        rows += f"""<tr data-room="{w['room']}" data-access="{open_access}">
      <td class="reg__code"><span class="code">{w['code']}</span></td>
      <td class="reg__who"><a href="{r['slug']}.html#{w['slug']}">{html.escape(w['artist'])}</a>
        <span><cite>{html.escape(w['work'])}</cite>, {html.escape(w['date'])}</span></td>
      <td class="reg__room"><span class="tag">Room {w['room']} &middot; {r['name']}</span></td>
      <td>{html.escape(w['label'][0][1])}</td>
      <td>{html.escape(withdraw)}
        <span class="tag tag--{open_access}">{ACCESS_LABEL[open_access]}</span></td>
      <td class="reg__out">{html.escape(left)}</td>
    </tr>"""

    body = f"""{DEPTH}
<main id="main">
<section class="band">
  <div class="wrap">
    <p class="kicker">The register</p>
    <h2>Nine accessions</h2>
    <p class="lede narrow">The same four fields that sit beside every work, laid out as the
    inventory they imitate. Nothing is hidden here. The rooms make you open each one; this page
    hands you all of them at once, which is a different kind of reading.</p>
    <p class="muted narrow">Filter by who is permitted to withdraw and the nine works fall into
    three groups of three. That split is the exhibition\u2019s actual argument, visible here in a
    way it is not when you walk the rooms one work at a time.</p>

    <div class="reg__bar">
      <div class="chips" role="group" aria-label="Filter by room">
        <button class="chip" data-filter="room" data-value="all" aria-pressed="true">All rooms</button>
        <button class="chip" data-filter="room" data-value="I" aria-pressed="false">I &middot; Deposit</button>
        <button class="chip" data-filter="room" data-value="II" aria-pressed="false">II &middot; Custody</button>
        <button class="chip" data-filter="room" data-value="III" aria-pressed="false">III &middot; Thaw</button>
      </div>
      <div class="chips" role="group" aria-label="Filter by access">
        <button class="chip" data-filter="access" data-value="all" aria-pressed="true">Any access</button>
        <button class="chip" data-filter="access" data-value="open" aria-pressed="false">Anyone may take it</button>
        <button class="chip" data-filter="access" data-value="named" aria-pressed="false">Only named parties</button>
        <button class="chip" data-filter="access" data-value="none" aria-pressed="false">No one takes anything out</button>
      </div>
      <p class="reg__count" data-count aria-live="polite">Nine of nine</p>
    </div>

    <div class="reg__scroll">
      <table class="reg">
        <thead><tr>
          <th scope="col">Accession</th><th scope="col">Artist and work</th><th scope="col">Room</th>
          <th scope="col">What is kept</th><th scope="col">Who may withdraw it</th>
          <th scope="col">What was left out</th>
        </tr></thead>
        <tbody>{rows}</tbody>
      </table>
    </div>
    <p class="reg__empty" data-empty hidden>Nothing in the collection matches both filters.</p>

    <div class="reg__after">
      <p class="muted" data-progress hidden></p>
      <p class="muted">A request for any of these can be written on the
      <a href="withdrawal.html">withdrawal slip</a>. This site keeps no record of who asks,
      which is the one thing a real vault would never allow.</p>
    </div>
  </div>
</section>
</main>"""
    return head("The register \u00b7 Duplicate Sample",
                "All nine works in the exhibition as an inventory, filterable by room and by access.",
                "register.html") + body + foot()


# ---------------------------------------------------------------- withdrawal
def build_withdrawal():
    opts = ""
    for w in S.WORKS:
        r = next(x for x in S.ROOMS if x["n"] == w["room"])
        opts += (f'<option value="{w["slug"]}" data-code="{w["code"]}" '
                 f'data-room="Room {w["room"]} &middot; {r["name"]}" '
                 f'data-kept="{html.escape(w["label"][0][1], quote=True)}" '
                 f'data-rule="{html.escape(w["label"][2][1], quote=True)}">'
                 f'{w["code"]} &middot; {html.escape(w["artist"])}, '
                 f'{html.escape(w["work"])}</option>')

    body = f"""{DEPTH}
<main id="main">
<section class="band">
  <div class="wrap">
    <p class="kicker">Withdrawal</p>
    <h2>Request material from the collection</h2>
    <div class="cols cols--side" style="margin-top:2rem">
      <div class="narrow">
        <p class="lede">Every collection in this exhibition decides who may take something out.
        This form is where you ask.</p>
        <p class="muted">Fill it in and the slip below is written in the exhibition&rsquo;s own
        accession format. You can print it or download it and keep it.</p>
        <p class="muted"><b>Nothing you type is sent anywhere or stored.</b> It stays in this
        browser window and is gone when you close it. That is deliberate. A vault that accepts
        requests keeps a register of everyone who asked, and that register is itself a form of
        control. This exhibition refuses to keep one, which is the one liberty a real seed bank
        could never take.</p>

        <form class="slipform" id="slipform" novalidate>
          <p class="fieldrow">
            <label for="f-work">Material requested</label>
            <select id="f-work" name="work" required>{opts}</select>
          </p>
          <p class="fieldrow">
            <label for="f-name">Requested by</label>
            <input id="f-name" name="name" type="text" autocomplete="name"
                   placeholder="Your name" required>
          </p>
          <p class="fieldrow">
            <label for="f-aff">On behalf of</label>
            <input id="f-aff" name="aff" type="text" autocomplete="organization"
                   placeholder="An institution, a farm, a household, or nobody">
          </p>
          <p class="fieldrow">
            <label for="f-why">Purpose of the withdrawal</label>
            <textarea id="f-why" name="why" rows="4"
              placeholder="What you intend to do with the material, and when you would return it"
              required></textarea>
          </p>
          <p class="fieldrow fieldrow--check">
            <input id="f-ack" name="ack" type="checkbox">
            <label for="f-ack">I accept that the depositor may refuse without giving a reason.</label>
          </p>
          <p class="slipform__go">
            <button class="btn" type="submit">Write the slip</button>
            <button class="btn btn--ghost" type="reset">Clear</button>
          </p>
        </form>
      </div>

      <aside>
        <article class="slip" id="slip" aria-live="polite">
          <header class="slip__head">
            <span class="code" data-s="code">DS &ndash; &nbsp; &ndash; &nbsp;</span>
            <span class="slip__kind">Withdrawal request</span>
          </header>
          <h3 class="slip__title" data-s="title">No material selected</h3>
          <dl class="slip__fields">
            <div><dt>Room</dt><dd data-s="room">&mdash;</dd></div>
            <div><dt>What is kept</dt><dd data-s="kept">&mdash;</dd></div>
            <div><dt>Standing rule</dt><dd data-s="rule">&mdash;</dd></div>
            <div><dt>Requested by</dt><dd data-s="name">&mdash;</dd></div>
            <div><dt>On behalf of</dt><dd data-s="aff">&mdash;</dd></div>
            <div><dt>Purpose</dt><dd data-s="why">&mdash;</dd></div>
            <div><dt>Terms accepted</dt><dd data-s="ack">Not accepted</dd></div>
            <div><dt>Raised</dt><dd data-s="when">&mdash;</dd></div>
          </dl>
          <footer class="slip__foot">
            <p>Duplicate Sample &middot; an online exhibition on seed banks and the keeping of
            living things. No record of this request is held by the exhibition.</p>
            <p class="slip__sign"><span></span>Signature of the depositor, if ever given</p>
          </footer>
        </article>
        <p class="slip__go">
          <button class="btn" type="button" data-print disabled>Print</button>
          <button class="btn btn--ghost" type="button" data-download disabled>Download</button>
        </p>
      </aside>
    </div>
  </div>
</section>
</main>"""
    return head("Withdrawal slip \u00b7 Duplicate Sample",
                "Request material from one of the nine collections. Nothing is stored.",
                "withdrawal.html") + body + foot()


# ---------------------------------------------------------------- team
# Who did what. Three strands as the team set them out in the proposal, with
# the one change that happened in execution: the site build moved from Seble to
# Tim. The selection of the nine works was a joint decision and is credited as
# one, not split into halves nobody could verify.
STRANDS = [
    ("Tim Maurice Steiner", "Research, texts and the site", [
        "Artist research, and the nine work descriptions",
        "The four-line label carried by every work",
        "The curatorial statement",
        "The build of this site, and its deployment",
    ]),
    ("Qing Guo", "Design and identity", [
        "The poster, A2, and the square promotional image",
        "Palette and typography",
        "The page template and the threshold panels",
    ]),
    ("Seble Getaneh", "Media and verification", [
        "Image preparation, sourcing and credits",
        "Link checking across the exhibition",
    ]),
]

TOGETHER = [
    ("The nine works", "Chosen together by Tim Maurice Steiner and Seble Getaneh."),
    ("Every deliverable", "Reviewed by all three before it went into the exhibition."),
]


def build_team():
    strands = ""
    for i, (who, strand, items) in enumerate(STRANDS, 1):
        li = "".join(f"<li>{html.escape(t)}</li>" for t in items)
        strands += f"""<section class="strand">
      <p class="strand__n">{i:02d}</p>
      <div>
        <h3>{html.escape(who)}</h3>
        <p class="strand__role">{html.escape(strand)}</p>
        <ul>{li}</ul>
      </div>
    </section>"""
    shared = "".join(
        f"<div><dt>{html.escape(k)}</dt><dd>{html.escape(v)}</dd></div>"
        for k, v in TOGETHER)

    body = f"""{DEPTH}
<main id="main">
<section class="band">
  <div class="wrap">
    <p class="kicker">Team</p>
    <h2>Who did what</h2>
    <p class="lede narrow" style="margin-top:1.4rem">Three strands, and one decision taken
    together. An exhibition that asks who selected, who holds and who may withdraw should be
    able to answer the same questions about itself.</p>

    <div class="strands">{strands}</div>

    <dl class="facts facts--wide">{shared}</dl>

    <p class="muted narrow" style="margin-top:2.4rem">{html.escape(S.COURSE)}, taught by
    Prof. Rui Hu, autumn 2026. The division above is the one the team worked to. The sequence
    was to confirm the nine works, write one page end to end as the specimen, build the
    template from it, draft the other eight, then assemble and check.</p>
  </div>
</section>
</main>"""
    return head("Team \u00b7 Duplicate Sample",
                "Who did what: three strands and one decision taken together.",
                "team.html") + body + foot()


if __name__ == "__main__":
    open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(build_index())
    for i, r in enumerate(S.ROOMS):
        open(os.path.join(OUT, r["slug"] + ".html"), "w", encoding="utf-8").write(build_room(i))
    open(os.path.join(OUT, "colophon.html"), "w", encoding="utf-8").write(build_colophon())
    open(os.path.join(OUT, "register.html"), "w", encoding="utf-8").write(build_register())
    open(os.path.join(OUT, "team.html"), "w", encoding="utf-8").write(build_team())
    open(os.path.join(OUT, "withdrawal.html"), "w", encoding="utf-8").write(build_withdrawal())
    open(os.path.join(OUT, "assets", "favicon.svg"), "w", encoding="utf-8").write(FAVICON)
    open(os.path.join(OUT, ".nojekyll"), "w").write("")
    print("pages built:", sorted(f for f in os.listdir(OUT) if f.endswith(".html")))