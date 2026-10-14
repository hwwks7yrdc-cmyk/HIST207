# -*- coding: utf-8 -*-
"""Small copies of the work images for the entrance page.

The entrance should not pull a megabyte of full-size photographs before it can
play. It makes two sets of smaller copies, each cropped to a common frame. The plates that fly down the corridor are never drawn
wider than about 280 pixels, and the nine preview tiles below the statement are
drawn at about 480. Before this, both pulled the full-size work photographs, so
the entrance spent 1.3 MB on images it then displayed at a fifth of their size.

Source is assets/img, so this runs from the published site and needs nothing
from outside. Output goes back into assets/img as tun-<slug>.jpg and
tile-<slug>.jpg.
"""
import os
from PIL import Image
import entry as EN

IMG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "site", "assets", "img")

W, H = 420, 300          # the corridor plate, in source pixels
TW, TH = 760, 507        # the preview tile, at about 1.6x its drawn size
QUALITY = 74
VAULT = (11, 26, 36)     # --vault, so a letterboxed plate has no visible edge

# Works whose opening image is a designed placeholder card rather than a
# photograph are fitted whole instead of cropped. Cropping a card cuts its
# words in half, and the card is the honest object for that work: it says on
# its face that no photograph has been cleared.
CONTAIN = {"okoyomon"}


def plate(slug, w=W, h=H, prefix="tun-", quality=QUALITY):
    src = os.path.join(IMG, slug + ".jpg")
    if not os.path.isfile(src):
        return None
    im = Image.open(src).convert("RGB")
    if slug in CONTAIN:
        im.thumbnail((w, h), Image.LANCZOS)
        card = Image.new("RGB", (w, h), VAULT)
        card.paste(im, ((w - im.width) // 2, (h - im.height) // 2))
        im = card
        out = os.path.join(IMG, prefix + slug + ".jpg")
        im.save(out, "JPEG", quality=quality, optimize=True, progressive=True)
        return out
    W, H = w, h
    # otherwise cover-crop to the frame, taking the middle
    target = W / H
    have = im.width / im.height
    if have > target:
        nw = round(im.height * target)
        im = im.crop(((im.width - nw) // 2, 0, (im.width - nw) // 2 + nw, im.height))
    else:
        nh = round(im.width / target)
        top = round((im.height - nh) * 0.42)      # a little above centre
        im = im.crop((0, top, im.width, top + nh))
    im = im.resize((W, H), Image.LANCZOS)
    out = os.path.join(IMG, prefix + slug + ".jpg")
    im.save(out, "JPEG", quality=quality, optimize=True, progressive=True)
    return out


if __name__ == "__main__":
    slugs = [i[1] for i in EN.SCORE if i[0] == "plate"]
    for label, w, h, pre, q in (("Korridor", W, H, "tun-", QUALITY),
                                ("Kacheln", TW, TH, "tile-", 78)):
        total = 0
        print(f"\n{label}:")
        for s in slugs:
            o = plate(s, w, h, pre, q)
            if not o:
                print(f"  FEHLT  {s}.jpg")
                continue
            kb = os.path.getsize(o) / 1024
            total += kb
            print(f"  {os.path.basename(o):26} {w}x{h}  {kb:5.1f} KB")
        print(f"  {total:.0f} KB zusammen")
