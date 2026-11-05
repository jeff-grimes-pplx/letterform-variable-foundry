"""Shared drawing kit for Apertide recipes (symbols, marks, special letters)."""
from geometry import Drawing, Path

B = 'blade'
X = 520; C = 700; A = 740; D = -210


class Kit:
    def __init__(self, d, width, left, right, extra_kb=0, raw=False):
        self.d = d; self.kb = d.kb
        self.g = Drawing(d, width + extra_kb * d.kb, left, right)
        if raw:
            self.g.set_raw_width(width)
        g = self.g
        self.w = g.w; self.s = d.s; self.h = d.h; self.l = d.s / 2; self.r = g.w - d.s / 2; self.m = g.w / 2
        self.X, self.C, self.A, self.D = X, C, A, D
        self.xt = X + 10 - d.h / 2; self.ct = C + 12 - d.h / 2; self.xb = -10 + d.h / 2; self.cb = -12 + d.h / 2
        self.T = 0.60 - 0.05 * d.kb; self.R = 0.555; self.nib = d.s / 2

    # strokes --------------------------------------------------------------
    def st(self, path, scale=1.0, c0=None, c1=None, contrast=1.0):
        self.g.stroke(path, scale, contrast, True, c0, c1)

    def line(self, x0, y0, x1, y1, scale=1.0, c0=None, c1=None):
        self.g.stroke(Path().M(x0, y0).L(x1, y1), scale, 1.0, True, c0, c1)

    def vert(self, x, y0, y1, scale=1.0): self.g.line(x, y0, x, y1, scale)
    def bar(self, y, x0, x1, scale=1.0): self.g.line(x0, y, x1, y, scale)
    def dia(self, x0, y0, x1, y1, scale=0.95, cut1=0.0): self.g.diag(x0, y0, x1, y1, scale, cut1)
    def hw(self, x0, y0, x1, y1, scale=0.95): return self.g.diag_hw(x0, y0, x1, y1, scale)
    def dot(self, x, y, scale=1.06): self.g.dot(x, y, scale)
    def poly(self, pts): self.g.polygon(pts)

    def loop(self, left, bottom, right, top, over=10, scale=1.0, tension=None):
        return self.g.loop(left, bottom - over + self.h / 2 * scale, right, top + over - self.h / 2 * scale, scale, tension)

    def ring(self, cx, cy, rx, ry, scale=1.0):
        """Closed round stroke centred at (cx, cy) with centerline radii rx, ry."""
        return self.g.loop(cx - rx, cy - ry, cx + rx, cy + ry, scale, (0.555, 0.555, 0.555, 0.555))

    def hook_ry(self, rx, want):
        nib = self.nib
        lo = (nib * 1.08 * rx) ** 0.5; hi = rx * rx / (nib * 1.08) if rx > 0 else want
        return max(lo, min(hi, want)) if hi >= lo else lo

    def thin_for(self, rx):
        return 1.0 if rx >= self.nib * 1.12 else max(0.62, rx / (self.nib * 1.12))

    def anchor(self, name, x, y): self.g.anchor(name, x, y)
    def ellipse(self, cx, cy, rx, ry): self.g.ellipse(cx, cy, rx, ry)
