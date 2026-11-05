"""Original Apertide glyph recipes, authored numerically for build A4 (proof set)."""
from geometry import Design, Drawing, Path

# width of the drawn box (before width factor) and sidebearings per glyph
WIDTHS = {'H': 500, 'O': 560, 'R': 500, 'A': 580, 'V': 560, 'a': 430, 'e': 440, 'n': 430, 'g': 440, 'f': 290, 'i': 90, 'f_i': 440, 'space': 240}
BEARINGS = {'A': (14, 14), 'V': (14, 14), 'H': (64, 64), 'O': (42, 42), 'R': (64, 30), 'a': (40, 44), 'e': (42, 36), 'n': (54, 50), 'g': (42, 46), 'f': (28, 14), 'i': (52, 52), 'f_i': (28, 52), 'space': (0, 0)}


def recipe(ch, d):
    W = WIDTHS.get(ch, 480); sb = BEARINGS.get(ch, (46, 46)); g = Drawing(d, W, *sb)
    w = g.w; s = d.s; h = d.h; l = s / 2; r = w - s / 2; m = w / 2
    X = d.xheight; C = d.cap; ox = d.over_x; oc = d.over_cap
    if ch == 'space':
        return g
    if ch == 'H':
        g.line(l, 0, l, C); g.line(r, 0, r, C); g.line(l, 336, r, 336)
    elif ch == 'O':
        g.loop(l, -oc + h / 2, r, C + oc - h / 2)
    elif ch == 'A':
        ap = 14  # half of the flat summit
        g.diag(hwx(l), 0, m - ap, C, 0.97); g.diag(m + ap, C, hwx(r), 0, 0.97)
        g.line(m - ap, C - h / 2, m + ap, C - h / 2)
        g.line(w * 0.24, 230, w * 0.76, 230, 1, 0.98)
    elif ch == 'V':
        g.diag(hwx(l), C, m - 11, 0, 0.98); g.diag(m + 11, 0, hwx(r), C, 0.98)
        g.line(m - 11, h / 2, m + 11, h / 2)
    elif ch == 'R':
        g.line(l, 0, l, C)
        g.stroke(Path().M(l, C - h / 2).L(w * 0.50, C - h / 2).C(w * 0.86, C - h / 2, r, 640, r, 540)
                 .C(r, 428, w * 0.84, 372, w * 0.50, 372).L(l, 372))
        g.diag(w * 0.47, 372, r + s * 0.08, 0, 0.98)
    elif ch == 'a':
        g.loop(l, -ox + h / 2, r, 318 - h / 2, tension=(0.7, 0.6, 0.55, 0.7))
        g.stroke(Path().M(l + 10, 418).C(l + 40, 500, w * 0.33, X + ox - h / 2, w * 0.56, X + ox - h / 2)
                 .C(w * 0.84, X + ox - h / 2, r, 450, r, 340).L(r, 0))
    elif ch == 'e':
        top = X + ox - h / 2
        g.stroke(Path().M(r - 12, 108).C(w * 0.74, -34, w * 0.17, -26, l, 190).C(-s * 0.08, 350, w * 0.18, top, m + 10, top)
                 .C(w * 0.80, top, r, 418, r, 288).L(l + 4, 268))
    elif ch == 'n':
        g.line(l, 0, l, X)
        g.stroke(Path().M(l, 356).C(l, 448, w * 0.25, X + ox - h / 2, m, X + ox - h / 2)
                 .C(w * 0.80, X + ox - h / 2, r, 436, r, 330).L(r, 0))
    elif ch == 'g':
        g.loop(l, -ox + h / 2, r, X + ox - h / 2)
        g.stroke(Path().M(r, X).L(r, -80).C(r, -202, w * 0.42, -256, l + 6, -144))
    elif ch == 'f':
        x = l + 54
        g.stroke(Path().M(x, 0).L(x, 580).C(x, 716, w * 0.70, 798, w - 4, 708))
        g.line(l, 500, w - 6, 500)
    elif ch == 'i':
        g.line(m, 0, m, X); g.dot(m, 668, 1.12)
    elif ch == 'f_i':
        x = d.W(84); ix = w - s / 2
        g.stroke(Path().M(x, 0).L(x, 586).C(x, 722, w * 0.60, 776, ix, 712))
        g.line(l, 500, ix, 500); g.line(ix, 0, ix, X); g.dot(ix, 668, 1.12)
    else:
        raise KeyError(ch)
    return g


def hwx(x):
    return x
