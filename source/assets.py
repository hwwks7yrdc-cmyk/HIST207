import os, shutil
from PIL import Image, ImageDraw, ImageFont

SRC = "/home/claude/ds/img"
OUT = "/home/claude/site/assets/img"
os.makedirs(OUT, exist_ok=True)

VAULT = (11, 26, 36)
FROST = (232, 238, 242)
ICE = (92, 122, 140)
GERM = (78, 140, 91)
DIM = (42, 63, 77)

G = "/usr/share/fonts/truetype/google-fonts/"
L = "/usr/share/fonts/truetype/liberation/"
F_SER = G + "Lora-Variable.ttf"
F_SAN = G + "Poppins-Medium.ttf"
F_MONO = L + "LiberationMono-Regular.ttf"


def prep(src, dst, w=1400):
    im = Image.open(os.path.join(SRC, src)).convert("RGB")
    if im.width > w:
        im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
    im.save(os.path.join(OUT, dst), "JPEG", quality=82, optimize=True, progressive=True)
    return im.size


def placeholder(dst, code, big, small, W=1400, H=900):
    im = Image.new("RGB", (W, H), VAULT)
    d = ImageDraw.Draw(im)
    # faint grid of sealed boxes
    cols, rows = 14, 9
    m = 56
    gx = 10
    cw = (W - 2 * m - (cols - 1) * gx) // cols
    ch = int(cw * 1.26)
    gy = 16
    gh = rows * ch + (rows - 1) * gy
    y0 = (H - gh) // 2
    live = (9, 3)
    for r in range(rows):
        for q in range(cols):
            x = m + q * (cw + gx); y = y0 + r * (ch + gy)
            if (q, r) == live:
                d.rectangle([x, y, x + cw, y + ch], fill=GERM)
            else:
                d.rectangle([x, y, x + cw, y + ch], outline=DIM, width=1)
                d.line([x + cw * .2, y + ch * .38, x + cw * .8, y + ch * .38], fill=DIM)
                d.line([x + cw * .2, y + ch * .58, x + cw * .6, y + ch * .58], fill=DIM)
    # stem out of the live cell
    lx = m + live[0] * (cw + gx) + cw // 2
    ly = y0 + live[1] * (ch + gy)
    d.line([lx, ly, lx + 3, ly - 70, lx - 2, ly - 150], fill=GERM, width=3, joint="curve")
    d.ellipse([lx - 26, ly - 112, lx - 2, ly - 92], fill=GERM)
    d.ellipse([lx + 2, ly - 142, lx + 26, ly - 122], fill=GERM)
    # scrim so text reads
    scrim = Image.new("RGBA", (W, H), (11, 26, 36, 190))
    im = Image.alpha_composite(im.convert("RGBA"), scrim).convert("RGB")
    d = ImageDraw.Draw(im)
    fb = ImageFont.truetype(F_SER, 108)
    fs = ImageFont.truetype(F_SER, 34)
    fc = ImageFont.truetype(F_MONO, 22)
    d.text((m + 18, H // 2 - 110), big, font=fb, fill=GERM)
    for i, ln in enumerate(small.split("\n")):
        d.text((m + 22, H // 2 + 36 + i * 46), ln, font=fs, fill=(189, 200, 210))
    d.text((m + 22, H - 86), code, font=fc, fill=ICE)
    fn = ImageFont.truetype(F_SAN, 18)
    d.text((W - m - 300, H - 84), "IMAGE TO BE SOURCED", font=fn, fill=DIM)
    im.save(os.path.join(OUT, dst), "JPEG", quality=86, optimize=True, progressive=True)


# ---- real photographs
print(prep("paterson.jpg", "paterson.jpg"))
print(prep("orlow.jpg", "orlow.jpg"))
print(prep("alves.jpg", "alves.jpg"))
print(prep("ff1.jpg", "futurefarmers.jpg"))
print(prep("kiw.jpg", "kiwanga.jpg"))
print(prep("son.jpg", "sonjasdotter-portrait.jpg", 700))

# ---- designed placeholders
placeholder("sonjasdotter.jpg", "DS – I – 02", "1880s",
            "the decade a purity standard began\nsending farmers’ grain into gene banks")
placeholder("balkin.jpg", "DS – I – 03", "0 rejected",
            "the archive is not curated;\neverything offered is accepted")
placeholder("sansour.jpg", "DS – II – 02", "no register",
            "the library keeps no record\nof who takes seeds")
placeholder("okoyomon.jpg", "DS – III – 02", "kudzu",
            "planted to hold the soil in place,\nit did not stay where it was planted")

# ---- design assets
os.makedirs("/home/claude/site/assets/design", exist_ok=True)
shutil.copy("/mnt/user-data/outputs/DuplicateSample_Poster_A2.pdf", "/home/claude/site/assets/design/poster-a2.pdf")
Image.open("/mnt/user-data/outputs/DuplicateSample_Poster_A2.png").convert("RGB").resize((900, 1273), Image.LANCZOS).save(
    "/home/claude/site/assets/design/poster.jpg", "JPEG", quality=85, optimize=True)
Image.open("/mnt/user-data/outputs/DuplicateSample_Promo_1080.png").convert("RGB").save(
    "/home/claude/site/assets/design/promo.jpg", "JPEG", quality=85, optimize=True)
print("assets done")
