"""Board diagrams for the detailed rules, as inline SVG.

Every diagram is drawn from the same board data the app plays on (the geometry helpers below copy
the app's LuzhanqiGame, JungleGame, AeroplaneBoard and Yutnori rules), and carries no words: pieces
show ranks or one-character names, places are marked with circled numbers, and the caption under
each figure says what they mean in the page's language.
"""
from html import escape

INK = "#2b2d27"
WOOD = "#efdcae"
WOOD_LINE = "#b8975a"
RED = "#c0392b"
BLUE = "#2c6fb7"
WATER = "#86c5e3"
GOLD = "#d99a26"
CREAM = "#fff8e6"
OK = "#2e8b57"


def _svg(width, height, label, body):
    return (f'<svg viewBox="0 0 {width} {height}" role="img" aria-label="{escape(label)}" '
            f'xmlns="http://www.w3.org/2000/svg" font-family="system-ui, sans-serif">{body}</svg>')


def _arrowhead(marker_id, colour):
    return (f'<marker id="{marker_id}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" '
            f'orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="{colour}"/></marker>')


def _badge(x, y, number, r=10):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="{INK}"/>'
            f'<text x="{x}" y="{y}" fill="#fff" font-size="{r + 2}" font-weight="700" text-anchor="middle" '
            f'dominant-baseline="central">{number}</text>')


def _piece(x, y, colour, label, r=17):
    size = 17 if len(str(label)) == 1 else 13
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="{CREAM}" stroke="{colour}" stroke-width="3"/>'
            f'<text x="{x}" y="{y}" fill="{colour}" font-size="{size}" font-weight="700" text-anchor="middle" '
            f'dominant-baseline="central">{escape(str(label))}</text>')


# ---------------------------------------------------------------- Animal Chess (JungleGame)

JUNGLE_COLS, JUNGLE_ROWS = 7, 9
# (x, y, side, rank); rank 8 is the Elephant and 1 the Rat. Red starts on rows 0-2, at the top.
JUNGLE_SETUP = [(0, 0, "R", 7), (6, 0, "R", 6), (1, 1, "R", 3), (5, 1, "R", 2), (0, 2, "R", 1), (2, 2, "R", 5),
                (4, 2, "R", 4), (6, 2, "R", 8),
                (0, 8, "B", 6), (6, 8, "B", 7), (1, 7, "B", 2), (5, 7, "B", 3), (0, 6, "B", 8), (2, 6, "B", 4),
                (4, 6, "B", 5), (6, 6, "B", 1)]


def _jungle_water(x, y):
    return 3 <= y <= 5 and x in (1, 2, 4, 5)


def _jungle_trap(x, y):
    return (x, y) in ((2, 0), (4, 0), (3, 1), (2, 8), (4, 8), (3, 7))


def _jungle_den(x, y):
    return (x, y) in ((3, 0), (3, 8))


def _jungle_cells(rows, cell, pad):
    out = []
    for row_index, y in enumerate(rows):
        for x in range(JUNGLE_COLS):
            left, top = pad + x * cell, pad + row_index * cell
            fill = WATER if _jungle_water(x, y) else "#e6c88a" if _jungle_trap(x, y) or _jungle_den(x, y) else WOOD
            out.append(f'<rect x="{left}" y="{top}" width="{cell}" height="{cell}" fill="{fill}" stroke="{WOOD_LINE}"/>')
            cx, cy = left + cell / 2, top + cell / 2
            if _jungle_trap(x, y):
                d = cell * 0.26
                out.append(f'<path d="M{cx - d} {cy - d}L{cx + d} {cy + d}M{cx + d} {cy - d}L{cx - d} {cy + d}" '
                           f'stroke="#9c6b2c" stroke-width="2.5" stroke-linecap="round"/>')
            if _jungle_den(x, y):
                r = cell * 0.3
                out.append(f'<path d="M{cx - r} {cy + r * .7}A{r} {r} 0 0 1 {cx + r} {cy + r * .7}Z" fill="#6f4f26"/>')
            if _jungle_water(x, y):
                w = cell * 0.3
                out.append(f'<path d="M{cx - w} {cy}q{w / 2} -5 {w} 0t{w} 0" stroke="#fff" stroke-opacity=".7" '
                           f'stroke-width="2" fill="none"/>')
    return out


def jungle_board(label, names=None):
    """The opening position. names maps rank (1-8) to a one-character piece name; ranks show without it."""
    cell, pad = 46, 10
    body = _jungle_cells(range(JUNGLE_ROWS), cell, pad)
    for x, y, side, rank in JUNGLE_SETUP:
        body.append(_piece(pad + x * cell + cell / 2, pad + y * cell + cell / 2, RED if side == "R" else BLUE,
                           (names or {}).get(rank, rank)))
    return _svg(JUNGLE_COLS * cell + 2 * pad, JUNGLE_ROWS * cell + 2 * pad, label, "".join(body))


def jungle_river(label, names=None):
    """Rows 2-6 only: ① a Lion jumps the river lengthwise, ② a Tiger jumps it crosswise, ③ a Rat blocks a jump."""
    cell, pad, first = 46, 10, 2
    names = names or {}

    def centre(x, y):
        return pad + x * cell + cell / 2, pad + (y - first) * cell + cell / 2

    body = [f'<defs>{_arrowhead("jr-ok", OK)}{_arrowhead("jr-no", RED)}</defs>']
    body += _jungle_cells(range(first, 7), cell, pad)
    for (x1, y1), (x2, y2), colour, marker in (((1, 2), (1, 6), OK, "jr-ok"), ((3, 4), (6, 4), OK, "jr-ok"),
                                               ((6, 3), (3, 3), RED, "jr-no")):
        (ax, ay), (bx, by) = centre(x1, y1), centre(x2, y2)
        dx, dy = (bx > ax) - (bx < ax), (by > ay) - (by < ay)
        body.append(f'<path d="M{ax + dx * 19} {ay + dy * 19}L{bx - dx * 8} {by - dy * 8}" stroke="{colour}" '
                    f'stroke-width="3.5" stroke-dasharray="7 5" fill="none" marker-end="url(#{marker})"/>')
    for x, y, side, rank in ((1, 2, "R", 7), (3, 4, "B", 6), (6, 3, "B", 7), (5, 3, "R", 1)):
        cx, cy = centre(x, y)
        body.append(_piece(cx, cy, RED if side == "R" else BLUE, names.get(rank, rank)))
    for (x, y), number in (((1, 6), 1), ((6, 4), 2)):
        cx, cy = centre(x, y)
        body.append(f'<circle cx="{cx}" cy="{cy}" r="9" fill="none" stroke="{OK}" stroke-width="3"/>')
        body.append(_badge(cx + 14, cy - 14, number, 9))
    cx, cy = centre(4, 3)
    body.append(f'<path d="M{cx - 8} {cy - 8}L{cx + 8} {cy + 8}M{cx + 8} {cy - 8}L{cx - 8} {cy + 8}" stroke="{RED}" '
                f'stroke-width="4" stroke-linecap="round"/>')
    rx, ry = centre(5, 3)
    body.append(_badge(rx + 14, ry - 16, 3, 9))
    return _svg(JUNGLE_COLS * cell + 2 * pad, 5 * cell + 2 * pad, label, "".join(body))


# ---------------------------------------------------------------- Luzhanqi (LuzhanqiGame)

LZ_COLS, LZ_ROWS = 5, 12


def lz_camp(x, y):
    if y >= 6:
        y = 11 - y
    return (y == 2 and x in (1, 3)) or (y == 3 and x == 2) or (y == 4 and x in (1, 3))


def lz_headquarters(x, y):
    return y in (0, 11) and x in (1, 3)


def lz_road(a, b):
    (x1, y1), (x2, y2) = a, b
    dx, dy = abs(x1 - x2), abs(y1 - y2)
    if dx + dy == 1:
        if {y1, y2} == {5, 6}:
            return x1 in (0, 2, 4)
        return True
    return dx == 1 and dy == 1 and (lz_camp(*a) or lz_camp(*b))


def lz_rail(a, b):
    (x1, y1), (x2, y2) = a, b
    if abs(x1 - x2) + abs(y1 - y2) != 1 or not lz_road(a, b):
        return False
    if y1 == y2:
        return y1 in (1, 5, 6, 10)
    return x1 == x2 and x1 in (0, 4) and min(y1, y2) >= 1 and max(y1, y2) <= 10


def _lz_xy(x, y):
    return 34 + x * 64, 24 + y * 42 + (36 if y >= 6 else 0)


def _rail(x1, y1, x2, y2):
    return (f'<path d="M{x1} {y1}L{x2} {y2}" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>'
            f'<path d="M{x1} {y1}L{x2} {y2}" stroke="#fff" stroke-width="2.5" stroke-dasharray="6 6"/>')


def _road(x1, y1, x2, y2):
    return f'<path d="M{x1} {y1}L{x2} {y2}" stroke="#8a7550" stroke-width="2"/>'


def _mountain(x, y):
    return (f'<path d="M{x - 15} {y + 9}L{x - 5} {y - 7}L{x + 1} {y + 2}L{x + 6} {y - 4}L{x + 15} {y + 9}Z" '
            f'fill="#8f7a52"/>')


def _post(x, y, colour):
    return f'<rect x="{x - 18}" y="{y - 10}" width="36" height="20" rx="4" fill="{CREAM}" stroke="{colour}" stroke-width="2"/>'


def _camp(x, y):
    return f'<circle cx="{x}" cy="{y}" r="14" fill="#cfe3c4" stroke="#3f7a52" stroke-width="2"/>'


def _hq(x, y, colour):
    return (f'<path d="M{x - 21} {y + 11}V{y - 4}Q{x} {y - 18} {x + 21} {y - 4}V{y + 11}Z" fill="#f2d38a" '
            f'stroke="{colour}" stroke-width="2"/>')


def luzhanqi_board(label):
    """The empty board, red half on top: ① headquarters, ② camps, ③ the three crossings of the front."""
    points = [(x, y) for y in range(LZ_ROWS) for x in range(LZ_COLS)]
    roads, rails = [], []
    for i, a in enumerate(points):
        for b in points[i + 1:]:
            if not lz_road(a, b):
                continue
            (x1, y1), (x2, y2) = _lz_xy(*a), _lz_xy(*b)
            (rails if lz_rail(a, b) else roads).append((x1, y1, x2, y2))
    body = [_road(*r) for r in roads] + [_rail(*r) for r in rails]
    mid = (_lz_xy(0, 5)[1] + _lz_xy(0, 6)[1]) / 2
    body += [_mountain(_lz_xy(x, 0)[0], mid) for x in (1, 3)]
    for x, y in points:
        cx, cy = _lz_xy(x, y)
        colour = RED if y < 6 else BLUE
        body.append(_hq(cx, cy, colour) if lz_headquarters(x, y) else _camp(cx, cy) if lz_camp(x, y)
                    else _post(cx, cy, colour))
    hx, hy = _lz_xy(1, 0)
    cx, cy = _lz_xy(1, 2)
    fx, fy = _lz_xy(4, 5)
    body += [_badge(hx + 26, hy - 6, 1, 9), _badge(cx + 19, cy - 13, 2, 9), _badge(fx + 25, mid, 3, 9)]
    width, height = _lz_xy(4, 11)
    return _svg(width + 46, height + 26, label, "".join(body))


def legend_icon(kind):
    """A small swatch for the HTML legend under the Luzhanqi board."""
    parts = {"rail": _rail(4, 11, 40, 11), "road": _road(4, 11, 40, 11), "post": _post(22, 11, INK),
             "camp": _camp(22, 11), "hq": _hq(22, 11, INK), "mountain": _mountain(22, 12)}
    return f'<svg viewBox="0 0 44 22" width="44" height="22" aria-hidden="true">{parts[kind]}</svg>'


# ---------------------------------------------------------------- Aeroplane Chess (AeroplaneBoard)

# Along any colour's route the cells cycle through the four colours, starting with its own.
ROUTE_COLOURS = ["#d94b3d", "#e8b630", "#3d7fd9", "#3fa65a"]


def aeroplane_route(label):
    """One colour's route laid out as a ribbon: ① a same-colour jump, ② a jump onto the flight cell that
    then flies twelve cells and jumps once more, ③ the home stretch and the goal."""
    step, size, left = 30, 26, 52
    rows_y = [40, 112, 184, 256]

    def cell_xy(p):
        if p <= 12:
            return left + (p - 1) * step, rows_y[0]
        if p <= 24:
            return left + (24 - p) * step, rows_y[1]
        return left + (p - 25) * step, rows_y[2]

    def centre(p):
        x, y = cell_xy(p)
        return x + size / 2, y + size / 2

    body = [f'<defs>{_arrowhead("ar-j", INK)}{_arrowhead("ar-f", RED)}</defs>']
    # Launch pad, then the ribbon of route cells 1-36.
    body.append(f'<rect x="8" y="{rows_y[0]}" width="{size}" height="{size}" rx="13" fill="none" stroke="{RED}" '
                f'stroke-width="2" stroke-dasharray="4 3"/>')
    body.append(f'<text x="21" y="{rows_y[0] + 13}" font-size="11" text-anchor="middle" dominant-baseline="central" '
                f'fill="{INK}">0</text>')
    for p in range(1, 37):
        x, y = cell_xy(p)
        own = (p - 1) % 4 == 0
        body.append(f'<rect x="{x}" y="{y}" width="{size}" height="{size}" rx="4" fill="{ROUTE_COLOURS[(p - 1) % 4]}"'
                    + (f' stroke="{INK}" stroke-width="2.5"' if own else '') + '/>')
        body.append(f'<text x="{x + size / 2}" y="{y + size / 2}" font-size="11" font-weight="{700 if own else 400}" '
                    f'text-anchor="middle" dominant-baseline="central" fill="#fff">{p}</text>')
    # The ribbon's turns.
    for a, b, side in ((12, 13, 1), (24, 25, -1)):
        (ax, ay), (bx, by) = centre(a), centre(b)
        body.append(f'<path d="M{ax + side * 15} {ay}h{side * 8}V{by}h{-side * 8}" stroke="#b9ab8a" stroke-width="2" '
                    f'fill="none"/>')
    flight_x, flight_y = cell_xy(17)
    body.append(f'<rect x="{flight_x - 3}" y="{flight_y - 3}" width="{size + 6}" height="{size + 6}" rx="6" '
                f'fill="none" stroke="{RED}" stroke-width="2.5" stroke-dasharray="5 3"/>')

    def hop(a, b, above, marker="ar-j", colour=INK, dash=""):
        (ax, ay), (bx, by) = centre(a), centre(b)
        edge = -size / 2 if above else size / 2
        lift = -26 if above else 26
        return (f'<path d="M{ax} {ay + edge}Q{(ax + bx) / 2} {ay + edge + lift} {bx} {by + edge}" stroke="{colour}" '
                f'stroke-width="2.5" fill="none" {dash} marker-end="url(#{marker})"/>')

    body.append(hop(5, 9, True))
    body.append(hop(13, 17, True))
    (fx, fy), (tx, ty) = centre(17), centre(29)
    body.append(f'<path d="M{fx} {fy + size / 2}C{fx} {fy + 60} {tx} {ty - 60} {tx} {ty - size / 2 - 2}" '
                f'stroke="{RED}" stroke-width="3" stroke-dasharray="7 5" fill="none" marker-end="url(#ar-f)"/>')
    body.append(hop(29, 33, False))
    x5, y5 = cell_xy(5)
    x13, y13 = cell_xy(13)
    body += [_badge(x5 - 4, y5 - 14, 1, 9), _badge(x13 + size - 1, y13 - 13, 2, 9)]
    # ... 49, the six home-stretch cells and the goal.
    y = rows_y[3]
    body.append(f'<text x="{left + 6}" y="{y + 13}" font-size="18" text-anchor="middle" dominant-baseline="central" '
                f'fill="{INK}">…</text>')
    for i, p in enumerate(range(49, 56)):
        x = left + (i + 1) * step
        home = p >= 50
        body.append(f'<rect x="{x}" y="{y}" width="{size}" height="{size}" rx="4" '
                    f'fill="{"#f3b3aa" if home else ROUTE_COLOURS[0]}" stroke="{RED if home else INK}" '
                    f'stroke-width="{2 if home else 2.5}"/>')
        body.append(f'<text x="{x + size / 2}" y="{y + size / 2}" font-size="11" text-anchor="middle" '
                    f'dominant-baseline="central" fill="{RED if home else "#fff"}" font-weight="700">{p}</text>')
    gx = left + 8 * step + size / 2
    body.append(f'<circle cx="{gx}" cy="{y + size / 2}" r="15" fill="{GOLD}" stroke="{INK}" stroke-width="2"/>')
    body.append(f'<text x="{gx}" y="{y + size / 2}" font-size="11" font-weight="700" text-anchor="middle" '
                f'dominant-baseline="central" fill="#fff">56</text>')
    body.append(_badge(left + 2 * step + size / 2, y - 12, 3, 9))
    return _svg(left + 12 * step + 12, rows_y[3] + size + 14, label, "".join(body))


# ---------------------------------------------------------------- Yutnori (ArcadeModels.Yutnori)

def _yut_points():
    """Node number -> (x, y) on a 300-unit board, with the start corner (node 0) bottom right."""
    o, s = 40, 300
    p = {0: (o + s, o + s), 5: (o + s, o), 10: (o, o), 15: (o, o + s), 22: (o + s / 2, o + s / 2)}
    for i in range(1, 5):
        p[i] = (o + s, o + s - i * s / 5)
        p[5 + i] = (o + s - i * s / 5, o)
        p[10 + i] = (o, o + i * s / 5)
        p[15 + i] = (o + i * s / 5, o + s)
    for i, n in enumerate((20, 21)):          # corner 5 towards the centre
        p[n] = (o + s - (i + 1) * s / 6, o + (i + 1) * s / 6)
    for i, n in enumerate((23, 24)):          # centre on towards corner 15
        p[n] = (o + s / 2 - (i + 1) * s / 6, o + s / 2 + (i + 1) * s / 6)
    for i, n in enumerate((25, 26)):          # corner 10 towards the centre
        p[n] = (o + (i + 1) * s / 6, o + (i + 1) * s / 6)
    for i, n in enumerate((27, 28)):          # centre on towards the start corner
        p[n] = (o + s / 2 + (i + 1) * s / 6, o + s / 2 + (i + 1) * s / 6)
    return p


def yutnori_board(label):
    """The board: ① start and finish corner, ② and ③ the corners with a shortcut, ④ the centre."""
    p = _yut_points()
    o, s = 40, 300
    body = [f'<defs>{_arrowhead("yt-a", "#8a6a3a")}</defs>',
            f'<rect x="{o}" y="{o}" width="{s}" height="{s}" fill="none" stroke="#8a6a3a" stroke-width="3"/>',
            f'<path d="M{o + s} {o}L{o} {o + s}M{o} {o}L{o + s} {o + s}" stroke="{GOLD}" stroke-width="4"/>']
    # Direction of travel: up the right side, then anticlockwise.
    for (x1, y1), (x2, y2) in ((p[2], p[3]), (p[7], p[8]), (p[12], p[13]), (p[17], p[18])):
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        dx, dy = (x2 - x1) / 6, (y2 - y1) / 6
        side = 20
        ox, oy = (side if x1 == x2 and x1 > o + 1 else -side if x1 == x2 else 0,
                  side if y1 == y2 and y1 > o + 1 else -side if y1 == y2 else 0)
        body.append(f'<path d="M{mx - dx + ox} {my - dy + oy}L{mx + dx + ox} {my + dy + oy}" stroke="#8a6a3a" '
                    f'stroke-width="2.5" marker-end="url(#yt-a)"/>')
    for n, (x, y) in p.items():
        big = n in (0, 5, 10, 15, 22)
        body.append(f'<circle cx="{x}" cy="{y}" r="{14 if big else 9}" fill="{GOLD if big else "#7a5530"}" '
                    f'stroke="#fff" stroke-width="2"/>')
    for n, number, (dx, dy) in ((0, 1, (16, 18)), (5, 2, (16, -18)), (10, 3, (-16, -18)), (22, 4, (0, -26))):
        x, y = p[n]
        body.append(_badge(x + dx, y + dy, number, 10))
    return _svg(o * 2 + s, o * 2 + s, label, "".join(body))


DIAGRAMS = {"jungle_board": jungle_board, "jungle_river": jungle_river, "luzhanqi_board": luzhanqi_board,
            "aeroplane_route": aeroplane_route, "yutnori_board": yutnori_board}


def render(name, label, names=None):
    function = DIAGRAMS[name]
    return function(label, names) if name.startswith("jungle") else function(label)
