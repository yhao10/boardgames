"""Exports the app's in-game rule cards, in the site's six extra languages, to content/app_rules.py.

Needs OpenCC (pip install opencc).  Run:  python3 tools/extract_app_rules.py ~/boardgames .
"""
import re
import sys
from pathlib import Path

import opencc

app, site = Path(sys.argv[1]), Path(sys.argv[2])
ui = app / "app/src/main/java/com/example/jungle/ui"
i18n_src = (app / "app/src/main/java/com/example/jungle/I18n.java").read_text(encoding="utf-8")

STR = r'"((?:[^"\\]|\\.)*)"'


def unescape(s):
    return s.encode("utf-8").decode("unicode_escape").encode("latin-1").decode("utf-8") if "\\" in s else s


TEXT = {}
for m in re.finditer(r'(?:put|token)\(((?:\s*' + STR + r'\s*,?){10})\);', i18n_src):
    args = [unescape(a) for a in re.findall(STR, m.group(1))]
    TEXT[args[0]] = args

world = (ui / "WorldGameView.java").read_text(encoding="utf-8")


def world_case(case):
    m = re.search(r'(?:case ' + case + r'|default):return new String\[\]\{(.*?)\};', world, re.S) if case != "default" \
        else re.search(r'default:return new String\[\]\{(.*?)\};', world, re.S)
    return [unescape(s) for s in re.findall(STR, m.group(1))]


def view_rules(view):
    src = (ui / view).read_text(encoding="utf-8")
    m = re.search(r'String\[\] RULES = \{(.*?)\};', src, re.S)
    return [unescape(s) for s in re.findall(STR, m.group(1))]


SOURCES = {
    "chess": world_case("CHESS"),
    "xiangqi": view_rules("XiangqiView.java"),
    "shogi": world_case("SHOGI"),
    "gomoku": view_rules("GomokuView.java"),
    "checkers": view_rules("CheckersView.java"),
    "four-in-a-row": world_case("CONNECT_FOUR"),
    "chinese-checkers": world_case("CHINESE_CHECKERS"),
    "animal-chess": view_rules("JungleView.java"),
    "luzhanqi": view_rules("LuzhanqiView.java"),
    "ludo": world_case("LUDO"),
    "aeroplane-chess": world_case("AEROPLANE"),
    "yutnori": world_case("default"),
}
# Tap-by-tap instructions for the app's controls, not rules of the game.
SKIP = {"先点选己方棋子，再点亮起的终点；连跳路径会自动完成，可向任意方向跳。", "先投掷，再选择一枚棋子移动。"}

COLUMNS = {"zh-hans": 0, "ja": 2, "ko": 3, "vi": 4, "th": 6}
_opencc = opencc.OpenCC("s2twp")
# OpenCC reads the chess queen (后) as "after" (後); Taiwan quotes with corner brackets.
HANT_FIXES = [("後直斜皆可", "后直斜皆可"), ("升變為後、", "升變為后、"), ("“", "「"), ("”", "」")]


def to_hant(text):
    text = _opencc.convert(text)
    for old, new in HANT_FIXES:
        text = text.replace(old, new)
    return text


out = {code: {} for code in ["zh-hans", "zh-hant", "ja", "ko", "vi", "th"]}
for slug, lines in SOURCES.items():
    lines = [l for l in lines if l not in SKIP]
    missing = [l for l in lines if l not in TEXT]
    if missing:
        sys.exit(f"{slug}: no translation for {missing}")
    for code, col in COLUMNS.items():
        out[code][slug] = [TEXT[l][col] for l in lines]
    out["zh-hant"][slug] = [to_hant(l) for l in lines]

body = ['"""The app\'s in-game rule cards, one list per game and language.',
        "",
        "Generated from the app's ui/*View.java rule arrays and I18n.java translations, so the site states",
        "exactly the rules the app plays. zh-hant is converted from zh-hans with OpenCC (s2twp). Do not",
        'edit by hand; regenerate after the app\'s rule cards change."""',
        "", "RULES = {"]
for code, games in out.items():
    body.append(f"    {code!r}: {{")
    for slug, lines in games.items():
        body.append(f"        {slug!r}: [")
        body += [f"            {l!r}," for l in lines]
        body.append("        ],")
    body.append("    },")
body.append("}")
(site / "content").mkdir(exist_ok=True)
(site / "content" / "app_rules.py").write_text("\n".join(body) + "\n", encoding="utf-8")
print({code: sum(len(v) for v in games.values()) for code, games in out.items()})
