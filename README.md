# Duplicate Sample

An online exhibition on seed banks and the keeping of living things.

Curated by Tim Maurice Steiner, Qing Guo and Seble Getaneh for ARTS / HIST 207,
History of Art and Science, Duke Kunshan University, taught by Prof. Rui Hu.

Nine contemporary works, all made or iterated after 2010, arranged in three rooms
around Anna Tsing's distinction between the plantation and the unruly edge.

---

## Publishing this on GitHub Pages

The site is plain HTML, CSS and JavaScript. There is no build step, no package
manager and no dependency to install. What is in this folder is what gets served.

### Once, to put it online

1. Sign in at <https://github.com> and click **New repository**.
   Name it `duplicate-sample`. Set it to **Public**. Do not add a README,
   a .gitignore or a licence, because this folder already has what it needs.
2. On the empty repository page choose **uploading an existing file**.
3. Drag in the **contents** of this folder, not the folder itself: the five
   `.html` files, `README.md`, `.nojekyll`, and the whole `assets` folder.
   If the browser upload refuses to take the folder, zip nothing and instead use
   the command line version below.
4. Click **Commit changes**.
5. Go to **Settings**, then **Pages** in the left sidebar.
   Under *Build and deployment*, set **Source** to `Deploy from a branch`,
   **Branch** to `main` and the folder to `/ (root)`. Click **Save**.
6. Wait about a minute and reload the Settings page. The live address appears at
   the top: `https://<your-username>.github.io/duplicate-sample/`

### Or, from a terminal

```bash
cd path/to/this/folder
git init
git add .
git commit -m "Duplicate Sample"
git branch -M main
git remote add origin https://github.com/<your-username>/duplicate-sample.git
git push -u origin main
```

Then do step 5 above.

### Updating it later

Edit the file, commit, push. GitHub republishes within a minute. If a change does
not show up, hold Shift and reload, because the browser caches the stylesheet.

### Two things that will break it if removed

- **`.nojekyll`** is an empty file that tells GitHub not to run the pages through
  its blog engine first. Without it, folders beginning with an underscore are
  dropped. Keep it even though it looks like nothing.
- **Relative paths.** Every link is relative (`assets/style.css`, not
  `/assets/style.css`), which is what lets the site work inside a project
  subfolder. If you move files between folders, the links need the same move.

---

## What is in here

```
index.html        the entrance: title, curatorial statement, Tsing, the three rooms
room-i.html       Deposit    · Paterson, Sonjasdotter, Balkin
room-ii.html      Custody    · Orlow, Sansour, Futurefarmers
room-iii.html     Thaw       · Alves, Okoyomon, Kiwanga
register.html     all nine accessions as a filterable inventory
withdrawal.html   the request form; writes a slip, stores nothing
colophon.html     credits, image rights, visual identity, references
assets/style.css  the whole design system, one file
assets/site.js    three behaviours: the label reveal, the depth marker, a page flag
assets/fonts/     Lora and Poppins, subsetted to woff2, 68 KB in total
assets/img/       work images, the documentation galleries, the one designed
                  placeholder, and the small copies: tun-*.jpg for the descent,
                  tile-*.jpg for the nine preview tiles
assets/design/    the poster and the promotional image
source/           sitedata.py and build_site.py, which generate the seven pages;
                  artists.py, the nine artist statements; diagrams.py, the nine drawn
                  figures; extras.py, the nine curators' notes and the further images;
                  entry.py, the score of the entry sequence; and the scripts that made
                  the files: assets.py, fonts.py, media.py, entryplates.py
.nojekyll         keep
```

The whole site is about 4.9 MB. Opening the entrance loads roughly 1.2 MB of
that, most of it the nine photographs in the preview wall, which arrive behind
the entry sequence while it is playing.

## Decisions worth knowing before you edit

**Type is self-hosted, not called from Google Fonts.** Google Fonts is not
reachable from mainland China, and part of the audience for this exhibition is in
Kunshan. The two typefaces are subsetted to the characters the site actually uses
and served from `assets/fonts/`. The site makes no third-party request at all, so
it loads the same way everywhere and sets no cookies. If you add text in a script
these subsets do not cover, the characters will fall back to a system font: the
subset is Latin-1 plus a short list of punctuation. Regenerating it needs
`fontTools` and `brotli`.

**The content lives in one Python file.** Every page was generated from
`source/sitedata.py` by `source/build_site.py`, both of which travel with the repository.
Editing the HTML by hand is fine for a typo. For anything structural, edit
`source/sitedata.py` and run `python3 source/build_site.py`, or the five pages will
drift apart. The generators are served alongside the site and do nothing there;
they are in the repository so the next person can rebuild it.

`assets.py` and `fonts.py` were run once, in the environment where the site was
assembled. They need the original source photographs and a local copy of the two
typefaces, so they will not run as they stand on another machine. They are here
as a record of how `assets/img/` and `assets/fonts/` were produced.

**JavaScript is optional for reading.** With it off, the two hidden label fields
are shown open by a `<noscript>` rule, and every page stays fully readable. The
register loses its filters but still lists all nine rows, and the wall in Room II
still scrolls by swipe or trackpad because that is native browser behaviour, not
script. The entry sequence ships with `hidden` on it and simply never appears.
Only the withdrawal slip needs script to do its job.

**The entry sequence is a corridor, and it is scored in `source/entry.py`.**
The entrance opens on a descent: nine accessions pass to either side, five
questions come straight at the camera, and the corridor ends at a door that says
welcome. Four of the five questions are the label fields printed on every work,
which is what keeps the sequence part of the argument rather than decoration.

Things worth knowing before changing it:

- The score is written in *seconds*, and depth is derived from it. The camera
  decelerates, so evenly spaced objects would arrive in a rush and then leave a
  hole. Edit `SCORE`, not the depths.
- Visibility is measured in *distance*, not seconds, for the same reason. An
  object that is given a fixed number of seconds late in the flight winks on at
  the size it winks off at and never appears to approach. See `VISIBLE`.
- The flight is on each object's own `translate`, never on one container. Moving
  a single stage forward is the obvious construction and it fails: once the
  stage's own plane crosses the camera the browser stops drawing the entire
  subtree, and the corridor empties halfway through.
- Lateral offsets are written for a 1440 by 900 window and converted to
  window-relative lengths. In fixed pixels nothing is ever visible on a phone.
- It plays once per visitor, keyed `ds.descent.v1` in `localStorage`, and never
  on a deep link into the page. `index.html#descend` replays it, which is what
  makes it usable in a live presentation; the colophon carries that link.
- Under `prefers-reduced-motion: reduce` there is no flight at all. The same five
  questions and the same door are held still for three seconds.

**The slip stores nothing and must keep storing nothing.** Everything typed into
`withdrawal.html` stays in the visitor's own browser. There is no endpoint, no
third-party form service and no analytics anywhere on this site. That is a
curatorial position, stated on the page itself, not an oversight to be fixed by
wiring up a form handler later.

**The visit record** is the one thing kept, under the key `ds.opened.v1` in
`localStorage`: which of the eighteen closed label fields this visitor has opened.
It never leaves their device and is read back only to show the count. Every call
is wrapped, so a browser with storage blocked simply shows no count.

**Motion respects the system setting.** Everything that animates is disabled
under `prefers-reduced-motion: reduce`.

## Images and rights

All works belong to their artists. Images are reproduced for a student exhibition
and credited to artist and source on the page where they appear and again in the
colophon. Four works carry a designed placeholder in the exhibition identity
rather than a borrowed photograph, because no image has been cleared for them yet:
Sonjasdotter, Balkin, Sansour and Okoyomon. Each placeholder says so on its face
and in its caption. Replacing one means dropping a file with the same name into
`assets/img/` and deleting the `Image to be sourced.` sentence from that work's
caption in `sitedata.py`.

Lora and Poppins are used under the SIL Open Font License 1.1.


---

## One slot waiting for files

The templates already handle these. Drop the file in, rebuild or not, and it appears.
Nothing breaks while they are empty.

**1. The entrance photograph is in place.** `assets/img/svalbard.jpg` is the vault
entrance by Bjoertvedt, from Wikimedia Commons, CC BY-SA 3.0. The credit sits on the
entrance itself and again in the colophon, and it names both the photographer and
*Perpetual Repercussion* by Dyveke Sanne, the mirrored work above the door. If you
ever replace this file, carry both credits over.

**2. Further images per work.** Eight of the nine works now carry a gallery of
documentation taken from the artists' own sites, their distributors, or the
institutions that showed the work. These live in `EXTRA` in `source/extras.py` as
`("filename.jpg", "alt text", "caption with its own credit")`, with the file in
`assets/img/`. Entries whose file is missing are skipped, so you can list one
before you have it.

The one gap left is an installation view of Precious Okoyomon's *Earthseed*. Its
page carries a designed card plus a photograph of kudzu that is captioned as what
it is: the plant, not the installation.

**Everything in a gallery must be documentation of the work.** The drawn figures
are ours, and they sit last on every page under the heading "A reading, not a
document", with a dashed frame and a caption saying no part of them comes from the
artist. Do not move a figure up into the documentation, and do not add a generic
image to a gallery to pad it out.
