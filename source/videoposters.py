"""Poster frames for the video panels.

Nothing of anybody's film is copied into this repository except one still
frame per video, which is the same position the exhibition already takes
on the photographs: a frame, credited, standing in for a work held
elsewhere. The moving image itself is never copied. It is streamed from
the server that published it, and only after the visitor presses play.
"""
import os
from PIL import Image

SRC = "/tmp/claude-0/-home-claude/3b54f73b-cc5f-55aa-8528-5e1336fb0b99/scratchpad/poster"
OUT = "/home/claude/site/assets/img"

# (source file, written name, target width)
PLATES = [
    ("raw-paterson-film.jpg",  "vid-paterson-film.jpg",  960),
    ("h-000350.jpg",           "vid-paterson-hand.jpg",  960),
    ("raw-sonjasdotter.jpg",   "vid-sonjasdotter.jpg",  1200),
    ("raw-sansour-v.jpg",      "vid-sansour.jpg",       1200),
    ("raw-kiwanga.jpg",        "vid-kiwanga.jpg",       1200),
    ("raw-okoyomon.jpg",       "vid-okoyomon.jpg",      1200),
]


def main():
    os.makedirs(OUT, exist_ok=True)
    total = 0
    for src, name, w in PLATES:
        im = Image.open(os.path.join(SRC, src)).convert("RGB")
        # every panel is 16:9, so centre-crop anything that is not
        tw, th = w, round(w * 9 / 16)
        sw, sh = im.size
        if abs(sw / sh - 16 / 9) > .01:
            if sw / sh > 16 / 9:
                nw = round(sh * 16 / 9)
                im = im.crop(((sw - nw) // 2, 0, (sw + nw) // 2, sh))
            else:
                nh = round(sw * 9 / 16)
                im = im.crop((0, (sh - nh) // 2, sw, (sh + nh) // 2))
        im = im.resize((tw, th), Image.LANCZOS)
        p = os.path.join(OUT, name)
        im.save(p, "JPEG", quality=78, optimize=True, progressive=True)
        n = os.path.getsize(p)
        total += n
        print(f"  {name:26} {tw}x{th}  {n/1024:6.1f} KB")
    print(f"  {'':26} {'':9} {total/1024:6.1f} KB total")


if __name__ == "__main__":
    main()
