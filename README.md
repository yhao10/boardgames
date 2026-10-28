# Classic Board Games Offline

Twelve classic board games in one free Android app, played offline against the AI or a friend on one device:
Animal Chess (Jungle / Dou Shou Qi 斗兽棋), Chess, Xiangqi (Chinese Chess 象棋), Shogi (将棋), Gomoku (五子棋), Checkers,
Four in a Row, Chinese Checkers (跳棋), Luzhanqi (Army Chess 军棋), Ludo, Aeroplane Chess (飞行棋) and Yutnori (윷놀이).

- Website: https://yhao10.github.io/boardgames/
- Google Play: https://play.google.com/store/apps/details?id=com.yhao10.boardgames

This repository holds the website. `python3 build.py` regenerates the HTML, `sitemap.xml` and `robots.txt`.

The site is in seven languages: English at the root, and 简体中文, 繁體中文, 日本語, 한국어, Tiếng Việt and ไทย under
`zh-hans/`, `zh-hant/`, `ja/`, `ko/`, `vi/` and `th/`. Each page links its translations with `hreflang`.

- `content/<language>.py` holds each language's text. Edit these, then run `build.py`; never edit the generated HTML.
- `content/zh_hant.py` is generated: edit `zh_hans.py`, then run `python3 tools/make_zh_hant.py .` (needs `pip install opencc`).
- `content/app_rules.py` is the app's own in-game rule cards, exported with
  `python3 tools/extract_app_rules.py ~/boardgames .`. Re-run it when the app's rules text changes.
- `diagrams.py` draws the rule diagrams (Animal Chess, Luzhanqi, Aeroplane Chess, Yutnori) from the app's board data.
