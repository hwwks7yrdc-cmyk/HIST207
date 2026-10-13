# -*- coding: utf-8 -*-
"""Prepares the real project material for the site.

Everything here is documentation of the works themselves, taken from the
artists' own sites, their distributors, or the institutions that showed them.
Nothing in this file is drawn or generated.
"""
import os
from PIL import Image

SRC = "/tmp/claude-0/media"
DST = "/home/claude/site/assets/img"

# (source file, output name, max width)
PLATES = [
    # --- Paterson, from futurelibrary.no ------------------------------------
    ("pat-3.jpg",                               "paterson.jpg",       1600),
    ("pat-author-elif_handover.jpg",            "paterson-2.jpg",     1200),
    ("pat-author-margaretatwoodcertificate.png","paterson-3.jpg",      900),
    ("pat-artwork-slider3-2.jpg",               "paterson-4.jpg",      900),
    # --- Sonjasdotter, stills from Filmform ---------------------------------
    ("son-6383.jpg",                            "sonjasdotter.jpg",   1600),
    ("son-6385.jpg",                            "sonjasdotter-2.jpg", 1600),
    ("son-6386.jpg",                            "sonjasdotter-3.jpg", 1600),
    ("son-6384.jpg",                            "sonjasdotter-4.jpg", 1600),
    # --- Balkin, from Southern Exposure -------------------------------------
    ("bal-newyorkcollection_sinkingandmelting_1024_0.jpg", "balkin.jpg", 1280),
    ("bal-3images.jpg",                         "balkin-2.jpg",       1024),
    ("bal-Nepal.jpg",                           "balkin-3.jpg",       1024),
    # --- Orlow, from urielorlow.net -----------------------------------------
    ("orl-what-plants-.jpg",                    "orlow.jpg",          1600),
    ("orl-Uriel-Orlow-.jpg",                    "orlow-2.jpg",        1060),
    ("orl-uriel-orlow-.jpg",                    "orlow-3.jpg",        1060),
    ("orl-tb-durban001.jpg",                    "orlow-4.jpg",        1060),
    # --- Sansour, from A Field -----------------------------------------------
    ("san-Vivien-San.jpg",                      "sansour.jpg",        1600),
    ("san-Seed-Packe.jpg",                      "sansour-2.jpg",       920),
    ("san-Vivien-lea.jpg",                      "sansour-3.jpg",       920),
    # --- Futurefarmers, from the Seed Journey logbook ------------------------
    ("ff-14930731.jpg",                         "futurefarmers-2.jpg", 750),
    ("ff-14925592.jpg",                         "futurefarmers-3.jpg", 750),
    ("ff-15209350.jpg",                         "futurefarmers-4.jpg", 750),
    # --- Alves, from mariatherezaalves.org -----------------------------------
    ("alv-1_.jpg",                              "alves-2.jpg",        1600),
    ("alv-16.jpg",                              "alves-3.jpg",         640),
    ("alv-23.jpg",                              "alves-4.jpg",        1600),
    ("alv-9_.jpg",                              "alves-5.jpg",         708),
    # --- Okoyomon: the plant, not the installation ---------------------------
    ("kudzu.jpg",                               "okoyomon-2.jpg",     1600),
]

if __name__ == "__main__":
    os.makedirs(DST, exist_ok=True)
    total = 0
    for src, out, mw in PLATES:
        p = os.path.join(SRC, src)
        if not os.path.isfile(p):
            print(f"  FEHLT   {src}")
            continue
        im = Image.open(p).convert("RGB")
        if im.width > mw:
            im = im.resize((mw, round(im.height * mw / im.width)), Image.LANCZOS)
        o = os.path.join(DST, out)
        im.save(o, "JPEG", quality=82, optimize=True, progressive=True)
        kb = os.path.getsize(o) // 1024
        total += kb
        print(f"  {out:24} {im.size[0]}x{im.size[1]}  {kb} KB")
    print(f"\n{total} KB insgesamt")
