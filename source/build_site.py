# -*- coding: utf-8 -*-
"""Generates the Duplicate Sample static site.

Run it from anywhere: python3 source/build_site.py
It writes the five pages and assets/favicon.svg into the folder above this one.
"""
import os, sys, html, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
OUT = os.path.dirname(HERE)

import sitedata as S
os.makedirs(OUT, exist_ok=True)

NAV = [("index.html", "Entrance"), ("room-i.html", "Deposit"),
       ("room-ii.html", "Custody"), ("room-iii.html", "Thaw"),
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
<noscript><style>.field__v{{grid-template-rows:1fr!important}}.reveal{{display:none}}</style></noscript>
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


# ---------------------------------------------------------------- index
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

    body = f"""{DEPTH}
<main id="main">

<section class="hero">
  {hero_svg()}
  <div class="hero__inner">
    <h1><span>Duplicate</span><span class="it">Sample</span></h1>
    <p class="hero__strap">{html.escape(S.STRAP)}</p>
    <div class="hero__mark"></div>
    <div class="hero__meta">
      <span>Nine artists</span><span>Three rooms</span>
      <span>{html.escape(S.COURSE)}</span>
    </div>
    <a class="hero__scroll" href="#statement"><span></span>Descend</a>
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
            label += (f'<div class="field field--hidden" data-open="false">'
                      f'<dt>{html.escape(k)} <button class="reveal" type="button">reveal</button></dt>'
                      f'<dd class="field__v"><span>{html.escape(v)}</span></dd></div>')

    quote = ""
    if w.get("quote"):
        qt, qa = w["quote"]
        quote = (f'<blockquote class="pull" style="margin:2rem 0 0">'
                 f'<p>&ldquo;{html.escape(qt)}&rdquo;</p>'
                 f'<footer>{html.escape(qa)}</footer></blockquote>')

    desc = "".join(f"<p>{html.escape(d) if '<' not in d else d}</p>" for d in w["desc"])
    link = ""
    if w.get("link"):
        lt, lu = w["link"]
        link = (f'<p class="work__link">The work online: '
                f'<a href="{lu}" rel="noopener">{html.escape(lt)}</a></p>')

    return f"""<article class="work" id="{w['slug']}">
  <figure class="work__fig">
    <img src="assets/img/{w['img']}" alt="{html.escape(w['alt'])}"
         width="1400" height="900" loading="lazy" decoding="async">
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
        <p class="muted">The site is hand-written HTML, CSS and JavaScript with no framework and no build
        step, hosted on GitHub Pages. Type is self-hosted, so the pages load without a single third-party
        request. Total weight is under two megabytes.</p>
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
    identity rather than a borrowed photograph.</p>
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

if __name__ == "__main__":
    open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(build_index())
    for i, r in enumerate(S.ROOMS):
        open(os.path.join(OUT, r["slug"] + ".html"), "w", encoding="utf-8").write(build_room(i))
    open(os.path.join(OUT, "colophon.html"), "w", encoding="utf-8").write(build_colophon())
    open(os.path.join(OUT, "assets", "favicon.svg"), "w", encoding="utf-8").write(FAVICON)
    open(os.path.join(OUT, ".nojekyll"), "w").write("")
    print("pages built:", sorted(f for f in os.listdir(OUT) if f.endswith(".html")))
