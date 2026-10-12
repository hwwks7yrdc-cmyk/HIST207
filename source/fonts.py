import os
from fontTools.ttLib import TTFont
from fontTools.subset import Subsetter, Options
from fontTools.varLib.instancer import instantiateVariableFont

G = "/usr/share/fonts/truetype/google-fonts/"
OUT = "/home/claude/site/assets/fonts"
os.makedirs(OUT, exist_ok=True)

# Latin-1 + the few extras the site actually uses
CHARS = ("".join(chr(c) for c in range(0x20, 0x7F))
         + "Ååéèêøöüäßóíá"
           "–—‘’“”…· ×→")


def make(src, dst, axes=None):
    f = TTFont(G + src)
    if axes:
        f = instantiateVariableFont(f, axes, inplace=True, updateFontNames=False)
    o = Options()
    o.layout_features = ["kern", "liga", "calt", "ccmp", "locl", "mark", "mkmk"]
    o.drop_tables += ["DSIG"]
    o.name_IDs = ["*"]
    o.notdef_outline = True
    s = Subsetter(options=o)
    s.populate(text=CHARS)
    s.subset(f)
    f.flavor = "woff2"
    f.save(os.path.join(OUT, dst))
    return os.path.getsize(os.path.join(OUT, dst))


print("lora-400", make("Lora-Variable.ttf", "lora-400.woff2", {"wght": 400}))
print("lora-500", make("Lora-Variable.ttf", "lora-500.woff2", {"wght": 500}))
print("lora-it", make("Lora-Italic-Variable.ttf", "lora-italic-400.woff2", {"wght": 400}))
print("pop-400", make("Poppins-Regular.ttf", "poppins-400.woff2"))
print("pop-500", make("Poppins-Medium.ttf", "poppins-500.woff2"))
