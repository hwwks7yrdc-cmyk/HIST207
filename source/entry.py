# -*- coding: utf-8 -*-
"""The descent: the sequence that plays once when the entrance is opened.

The flight goes *down and in*, not out at the visitor. Svalbard is a tunnel
driven into a mountain, the entrance page already ends in a link that says
Descend, and the site already carries a depth gauge down its right edge. A
sequence that threw objects outward would be the one gesture in the whole
exhibition that moves in the wrong direction.

So the visitor travels forward along a corridor. Nine accessions pass to either
side, too briefly to study, which is the point: in a vault you do not get to
look at what is stored. Five questions come straight at the camera and the
visitor passes through them. The corridor ends at a door, and the door says
welcome.

The five questions are not written for the occasion. Four of them are the label
fields carried by all nine works, and the fifth is the one the exhibition ends
on. Asking them here means the entrance states the method before the visitor
has met a single artwork.

The sequence is scored in TIME, not in depth. The camera decelerates, so evenly
spaced objects would arrive in a rush and then leave a hole; depth is therefore
derived from the moment each object is wanted, by running the easing forwards.
"""

TRAVEL = 4700              # how far the camera moves, in px of Z
DURATION = 7.0             # seconds of flight
EASE = (.45, .03, .2, 1)   # slow to leave, steady, soft arrival
HOLD = 1.5                 # seconds the door is held before the page takes over
PERSPECTIVE = 900          # must match the CSS, or the fan-out is wrong

# Questions. Short enough to be read while passing through them.
# The first four are the label fields printed on every work in the exhibition.
QUESTIONS = [
    "What is kept?",
    "Who decides?",
    "Who may withdraw it?",
    "What was left out?",
    "And who is it for?",
]

# The corridor, scored in seconds from the first frame.
#   ("plate", slug, x, y, at) | ("ask", index, y, at) | ("ring", at)
# x and y are offsets in px at the object's own plane, so they fan outwards as
# the object approaches: an offset of 820 leaves the frame of a 1440 screen by
# the time the plate is level with the camera, which is what makes the corridor
# feel passed through rather than watched. Plates alternate sides and heights so
# it never settles into symmetry.
#
# Questions carry a y of their own, alternating above and below the centre
# line. The camera decelerates so sharply that the last two questions sit only
# a few hundred pixels apart in the corridor and are on screen together; dead
# centre they would print on top of each other, and staggered they read as
# what they are, one behind the other.
SCORE = [
    ("ring",  0.45),
    ("ring",  0.78),
    ("plate", "paterson",      -820, -150,  0.95),
    ("ring",  1.10),
    ("ask",   0,      0,  1.30),
    ("ring",  1.45),
    ("plate", "sonjasdotter",   880,  110,  1.62),
    ("plate", "balkin",        -760,  330,  1.78),
    ("ring",  1.95),
    ("ask",   1,   -118,  2.18),
    ("ring",  2.35),
    ("plate", "orlow",         -900,  255,  2.52),
    ("plate", "sansour",        840, -290,  2.68),
    ("ring",  2.85),
    ("ask",   2,    118,  3.06),
    ("ring",  3.24),
    ("plate", "futurefarmers",  870,  240,  3.42),
    ("plate", "alves",         -800, -300,  3.58),
    ("ring",  3.75),
    ("ask",   3,   -118,  3.96),
    ("ring",  4.14),
    ("plate", "okoyomon",      -860, -120,  4.32),
    ("plate", "kiwanga",        820,  330,  4.48),
    ("ring",  4.66),
    ("ask",   4,    126,  4.92),
    # the corridor empties and only the rings keep coming, so the approach to
    # the door still reads as movement
    ("ring",  5.22),
    ("ring",  5.62),
    ("ring",  6.05),
    ("ring",  6.52),
]

# When each kind of object appears and disappears, as a DISTANCE from the
# camera, never as a span of seconds.
#
# The camera decelerates, so a fixed number of seconds buys a great deal of
# corridor at the start and almost none at the end: objects late in the flight
# would wink on at the size they wink off at, and nothing would ever approach.
# Measured in distance instead, every object is seen through the same stretch
# of corridor and grows the same way, whenever it happens to arrive.
#
#   (far, near) = appears this far ahead, gone by this close.
VISIBLE = {
    "plate": (2100, 100),
    "ask":   (1300,  40),   # kept short so two questions never collide
    "ring":  (1750,  30),
}

# Short caption under each plate. Artist only: there is no time to read more.
PLATE_CAP = {
    "paterson":      "Katie Paterson",
    "sonjasdotter":  "Åsa Sonjasdotter",
    "balkin":        "Amy Balkin",
    "orlow":         "Uriel Orlow",
    "sansour":       "Vivien Sansour",
    "futurefarmers": "Futurefarmers",
    "alves":         "Maria Thereza Alves",
    "okoyomon":      "Precious Okoyomon",
    "kiwanga":       "Kapwani Kiwanga",
}

# The door is the one object the camera never reaches. It sits beyond the end of
# the travel, so the flight stops in front of it.
DOOR_Z = TRAVEL + 620
DOOR_IN = 4.58          # when it begins to resolve out of the dark
DOOR = {
    "kicker": "The door",
    "word":   "Welcome",
    "line":   "Nine works on seed banks and the keeping of living things.",
}


# ---------------------------------------------------------------------------
# timing
# ---------------------------------------------------------------------------

def _bez(t, a, b):
    """One axis of a cubic bezier from 0 to 1 with control values a and b."""
    u = 1 - t
    return 3 * u * u * t * a + 3 * u * t * t * b + t * t * t


def _t_for_x(x, x1, x2):
    """The bezier parameter at which the x axis reaches x."""
    lo, hi = 0.0, 1.0
    for _ in range(60):
        mid = (lo + hi) / 2
        if _bez(mid, x1, x2) < x:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def progress_at(sec, ease=EASE):
    """How much of the travel is behind the camera at `sec` seconds."""
    x1, y1, x2, y2 = ease
    f = max(0.0, min(1.0, sec / DURATION))
    return _bez(_t_for_x(f, x1, x2), y1, y2)


def depth_for(sec):
    """Where to put an object so the camera reaches it at `sec` seconds."""
    return round(progress_at(sec) * TRAVEL)


def _t_for_y(y, y1, y2):
    """The bezier parameter at which the y axis reaches y."""
    lo, hi = 0.0, 1.0
    for _ in range(60):
        mid = (lo + hi) / 2
        if _bez(mid, y1, y2) < y:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def seconds_to_depth(d, ease=EASE):
    """When the camera reaches depth d. The inverse of depth_for."""
    x1, y1, x2, y2 = ease
    if d <= 0:
        return 0.0
    if d >= TRAVEL:
        return DURATION
    return DURATION * _bez(_t_for_y(d / TRAVEL, y1, y2), x1, x2)


def window(kind, z):
    """(start, duration) of an object's fade, in seconds from the first frame.

    A start before zero is deliberate. It means the object is already part way
    into its approach on the opening frame, which is hidden under the stage's
    own fade up out of the dark.
    """
    far, near = VISIBLE[kind]
    begin = seconds_to_depth(z - far) if z > far else 0.0
    # objects that start on screen are given the lead-in they would have had
    if z <= far:
        begin = -(far - z) / far * 0.8
    end = seconds_to_depth(max(z - near, 0))
    return round(begin, 3), round(max(end - begin, 0.25), 3)


# The score's x and y are written for a 1440 by 900 window, and turned into
# window-relative lengths on the way out. In fixed pixels a plate set 820px
# to the side never enters a 390px phone screen at all: it is already past the
# frame before it is near enough to see. These are the bounds it is held
# between, so it neither vanishes on a phone nor drifts into the far corners of
# a very wide display.
REF_W, REF_H = 1440, 900
X_BOUND = (170, 920)
Y_BOUND = (60, 360)


def lateral(px):
    lo, hi = X_BOUND
    return (f"calc({'-' if px < 0 else ''}1 * "
            f"clamp({lo}px, {abs(px) / REF_W * 100:.1f}vw, {hi}px))")


def vertical(px):
    lo, hi = Y_BOUND
    return (f"calc({'-' if px < 0 else ''}1 * "
            f"clamp({lo}px, {abs(px) / REF_H * 100:.1f}vh, {hi}px))")


def scale_at(z):
    """How large the object appears, relative to its own size, at depth z."""
    return PERSPECTIVE / (PERSPECTIVE + z)


if __name__ == "__main__":
    print(f"{'object':26} {'passiert':>9} {'z':>6} {'ab':>8} {'Dauer':>7} {'wächst':>7}")
    for item in SCORE:
        kind, at = item[0], item[-1]
        name = {"plate": lambda: item[1], "ask": lambda: QUESTIONS[item[1]],
                "ring": lambda: "·"}[kind]()
        z = depth_for(at)
        b, d = window(kind, z)
        far, near = VISIBLE[kind]
        grow = scale_at(near) / scale_at(min(far, max(z, near)))
        print(f"{kind + ' ' + name:26} {at:8.2f}s {z:6} {b:7.2f}s {d:6.2f}s {grow:6.1f}x")
    print(f"door                          {'-':>8} {DOOR_Z:6} {DOOR_IN:7.2f}s")
    print(f"\nFlug {DURATION}s, danach {HOLD}s Halt, insgesamt {DURATION + HOLD}s")
    print(f"Tür steht am Ende bei {DOOR_Z - TRAVEL}px, erscheint "
          f"{scale_at(DOOR_Z - TRAVEL) * 100:.0f}% ihrer Eigengröße")
