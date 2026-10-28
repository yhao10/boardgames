"""Builds content/zh_hant.py from content/zh_hans.py: OpenCC s2twp, then Taiwan-specific fixes.

Needs OpenCC (pip install opencc).  Run after editing zh_hans.py:  python3 tools/make_zh_hant.py .
Put any Traditional-only wording in FIXES rather than editing zh_hant.py, or the next run loses it.
"""
import re
import sys
from pathlib import Path
import opencc

site = Path(sys.argv[1])
src = (site / "content" / "zh_hans.py").read_text(encoding="utf-8")
text = opencc.OpenCC("s2twp").convert(src)
FIXES = [
    ('"""簡體中文. content/zh_hant.py is converted from this file; keep the two in step."""',
     '"""繁體中文, converted from content/zh_hans.py with OpenCC (s2twp) and hand-fixed for Taiwan usage."""'),
    ('CODE = "zh-hans"', 'CODE = "zh-hant"'),
    ('HTML_LANG = "zh-Hans"', 'HTML_LANG = "zh-Hant"'),
    ('HREFLANG = "zh-Hans"', 'HREFLANG = "zh-Hant"'),
    ('OG_LOCALE = "zh_CN"', 'OG_LOCALE = "zh_TW"'),
    ('PLAY_HL = "zh-CN"', 'PLAY_HL = "zh-TW"'),
    ('LABEL = "簡體中文"', 'LABEL = "繁體中文"'),
    ('PREFIX = "zh-hans/"', 'PREFIX = "zh-hant/"'),
    ('BADGE = "google-play-badge-zh-cn.png"', 'BADGE = "google-play-badge-zh-tw.png"'),
    ('badge_alt="去 Google Play 商店下載"', 'badge_alt="立即從 Google Play 下載"'),
    ("同一個免費應用裡", "同一個免費 App 裡"),
    ("一個應用全部收齊", "一個 App 全部收齊"),
    ("在一部手機或平板上面對面", "在一支手機或平板上面對面"),
    ("一部手機", "一支手機"),
    ("地鐵裡", "捷運上"),
    ("安卓", "Android"),
    ("大多數棋類應用", "大多數棋類 App"),
    ('"十種：簡體中文、English', '"十種（中文介面為簡體字）：简体中文、English'),
    ("應用裡的其他棋", "App 裡的其他棋"),
    ("經典棋局裡的", "經典棋局中的"),
    ("Android應用經典棋局中的", "Android App 經典棋局中的"),
    ("十二款棋，一個應用", "十二款棋，一個 App"),
    ("由應用裁定每次碰子", "由 App 裁定每次碰子"),
    ("應用會提議和棋", "App 會提議和棋"),
    ("應用自動判和", "App 自動判和"),
    # Taiwan names: chess is 西洋棋, and xiangqi is simply 象棋.
    ("國際象棋", "西洋棋"),
    ('name="西洋棋", aka="Chess · 西洋棋"', 'name="西洋棋", aka="國際象棋 · Chess"'),
    ("中國象棋", "象棋"),
    ('name="象棋", aka="象棋 · Xiangqi · Chinese Chess"', 'name="象棋", aka="中國象棋 · Xiangqi · Chinese Chess"'),
    ("賬號", "帳號"),
    ("棋鍾", "棋鐘"),
    ("安裝包小", "安裝檔小"),
    ("彈窗廣告", "彈出式廣告"),
    ("側欄佈局", "側欄版面"),
    ("聯網", "連網"),
    ("一部裝置", "一台裝置"),
]
for old, new in FIXES:
    if old not in text:
        print(f"fix not found: {old!r}")
    text = text.replace(old, new)
# A space between Han characters and the Latin words Android / App, as Taiwan typesetting does.
text = re.sub(r"(Android|App)(?=[一-鿿])", r"\1 ", text)
text = re.sub(r"(?<=[一-鿿])(Android|App)", r" \1", text)
(site / "content" / "zh_hant.py").write_text(text, encoding="utf-8")
