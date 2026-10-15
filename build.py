"""Generates the site's HTML, sitemap and robots.txt. Run: python3 build.py"""
import json
from html import escape
from pathlib import Path

from PIL import Image

BASE = "https://yhao10.github.io/boardgames/"
APP_ID = "com.yhao10.boardgames"
APP_NAME = "Classic Board Games Offline"
DEVELOPER = "redpig"
PRIVACY = "https://boardgames-privacy.allenyuanchina.workers.dev/privacy-policy"
UPDATED = "2026-10-15"
LANGUAGES = ["English", "简体中文", "日本語", "한국어", "Tiếng Việt", "Bahasa Melayu", "ไทย", "ລາວ", "Español", "Deutsch"]
OUT = Path(__file__).parent


def shot_size(name):
    return Image.open(OUT / "img" / "shots" / f"{name}.webp").size


def play_url(campaign):
    # The referrer shows up in Play Console's acquisition report, per page.
    return (f"https://play.google.com/store/apps/details?id={APP_ID}"
            f"&referrer=utm_source%3Dgithub_pages%26utm_medium%3Dwebsite%26utm_campaign%3D{campaign}")


GAMES = [
    dict(slug="chess", name="Chess", aka="International chess", players="2 players",
         title="Chess Offline – Play vs AI or a Friend, Free for Android",
         desc="Play chess offline on Android against an AI with three levels, or with a friend on the same phone. Free, no account and no Wi-Fi needed.",
         intro="The world's classic strategy game: two armies of sixteen pieces and one goal, to checkmate the enemy king. Learn the moves in an afternoon, then spend years getting better.",
         rules=["Each side has a king, a queen, two rooks, two bishops, two knights and eight pawns.",
                "White moves first and the players alternate, one move each.",
                "Capture by moving onto the square of an enemy piece.",
                "Castling, en passant and pawn promotion are all part of the game.",
                "Checkmate the opposing king to win; a stalemate is a draw."],
         app=["Play the computer at Easy, Normal or Expert, or a friend on one device.",
              "The AI opens from a built-in chess opening book, then thinks for itself.",
              "Optional chess clock, undo, and a replay of the whole game."]),
    dict(slug="xiangqi", name="Xiangqi", aka="Chinese Chess · 象棋", players="2 players",
         title="Xiangqi (Chinese Chess 象棋) Offline – Free Android App",
         desc="Play Xiangqi, Chinese Chess (象棋), offline on Android against an AI with a real opening book or with a friend on one phone. Free, no sign-in.",
         intro="Chinese Chess is played on the points of a 9×10 board split by a river. Generals stay inside their palace, cannons leap to capture, and one soldier across the river can decide the game.",
         rules=["Each side has a general, two advisors, two elephants, two horses, two chariots, two cannons and five soldiers.",
                "Pieces stand on the intersections, not in the squares. Red moves first.",
                "The general and advisors never leave the palace, and elephants never cross the river.",
                "A cannon moves like a chariot but captures by jumping over exactly one piece.",
                "A horse is blocked by a piece beside it, and the two generals may never face each other on an open file.",
                "Checkmate or stalemate the enemy general to win."],
         app=["Traditional Chinese-character pieces on a wooden board.",
              "The AI plays real Xiangqi openings from a built-in opening book.",
              "Play the computer or a friend on one device, fully offline."]),
    dict(slug="shogi", name="Shogi", aka="Japanese Chess · 将棋", players="2 players",
         title="Shogi (Japanese Chess 将棋) Offline vs AI – Free Android App",
         desc="Play Shogi, Japanese Chess (将棋), offline on Android against an AI that knows its openings, or with a friend on one device. Free, no account.",
         intro="Japanese chess on a 9×9 board, where nothing you capture is lost for good: take an enemy piece and you can drop it back onto the board as your own.",
         rules=["Each side has twenty pieces: a king, a rook, a bishop, two gold and two silver generals, two knights, two lances and nine pawns.",
                "Sente moves first.",
                "Captured pieces go to your hand, and on a later turn you may drop one onto an empty square instead of moving.",
                "Most pieces may promote when they move into, within or out of the last three ranks.",
                "Checkmate the enemy king to win."],
         app=["Traditional kanji pieces.",
              "The AI plays known openings from a built-in joseki book.",
              "Play the computer or a friend on one device."]),
    dict(slug="gomoku", name="Gomoku", aka="Five in a Row · 五子棋 · 五目並べ", players="2 players",
         title="Gomoku (Five in a Row 五子棋) Offline – Free Android App",
         desc="Play Gomoku, Five in a Row (五子棋), offline on Android against the AI or a friend. Black and white stones on a 15×15 board. Free, no Wi-Fi needed.",
         intro="Black and white stones on a 15×15 board. A minute to learn and a lifetime to master: the first player to make an unbroken line of five wins.",
         rules=["Black places first, then the players take turns putting one stone on an empty intersection.",
                "Stones never move and are never captured.",
                "Five of your stones in a row, across, down or diagonally, wins the game.",
                "Block your opponent's open threes and fours before they turn into five."],
         app=["A 15×15 wooden board with classic black and white stones.",
              "Three AI levels for a quick game on a break or a real fight.",
              "Two players can share one phone."]),
    dict(slug="checkers", name="Checkers", aka="English Draughts · American Checkers", players="2 players",
         title="Checkers (English Draughts) Offline vs AI – Free Android App",
         desc="Play checkers, English draughts, offline on Android against the AI or a friend on one phone. Classic 8×8 rules, free, no account.",
         intro="The 8×8 classic of diagonal moves and jumping captures, and the race to be crowned king.",
         rules=["Each player starts with twelve pieces on the dark squares.",
                "Pieces move one square diagonally forward.",
                "Capture by jumping an adjacent enemy piece into the empty square beyond. Jumps can be chained, and capturing is compulsory.",
                "A piece that reaches the far row is crowned and may then move backwards too.",
                "Win by capturing all of your opponent's pieces or leaving them no move."],
         app=["English / American checkers rules.",
              "Choose your colour and play the AI or a friend.",
              "Undo a move or replay the game from the start."]),
    dict(slug="four-in-a-row", name="Four in a Row", aka="The drop-disc line game", players="2 players",
         title="Four in a Row Offline – Play vs AI or a Friend on Android",
         desc="Play Four in a Row offline on Android: drop discs into a 7×6 grid and connect four before the AI or your friend does. Free, no Wi-Fi needed.",
         intro="Drop coloured discs into a grid seven columns wide and six rows high, and be the first to line up four.",
         rules=["Take turns dropping a disc into any column; it falls to the lowest empty space.",
                "Four of your discs in a line, across, down or diagonally, wins.",
                "If the grid fills up with no line of four, the game is drawn."],
         app=["Play the computer at three levels or a friend on one phone.",
              "Quick games, perfect for a short break."]),
    dict(slug="chinese-checkers", name="Chinese Checkers", aka="Star Halma · 跳棋", players="2, 3, 4 or 6 players",
         title="Chinese Checkers (跳棋) Offline – 2 to 6 Players on Android",
         desc="Play Chinese Checkers (跳棋) offline on Android with 2, 3, 4 or 6 players: friends on one device, the AI, or both. Free, no account needed.",
         intro="Race your marbles across a six-pointed star. Hop over any marble, yours or an opponent's, and chain hops together to cross the board in a single turn.",
         rules=["Each player starts with ten marbles in one point of the star.",
                "On your turn, step to a neighbouring empty hole, or hop over an adjacent marble into the empty hole beyond.",
                "Hops can be chained in one turn, and nothing is ever captured.",
                "The first player to move all ten marbles into the opposite point wins."],
         app=["2, 3, 4 or 6 players on one device.",
              "Any seat can be a person or the AI."]),
    dict(slug="animal-chess", name="Animal Chess", aka="Jungle · Dou Shou Qi · 斗兽棋", players="2 players",
         title="Animal Chess (Jungle, Dou Shou Qi 斗兽棋) Offline – Android",
         desc="Play Animal Chess, also called Jungle or Dou Shou Qi (斗兽棋), offline on Android against the AI or a friend. The childhood classic, free, no Wi-Fi needed.",
         intro="The childhood classic from China: eight animals a side on a 7×9 board with two rivers, traps and a den. The elephant rules the jungle, except that the tiny rat can bring it down.",
         rules=["From strongest to weakest: Elephant, Lion, Tiger, Leopard, Wolf, Dog, Cat, Rat.",
                "Animals move one square up, down, left or right, and capture an enemy of equal or lower rank.",
                "The Rat can capture the Elephant, but the Elephant cannot capture the Rat.",
                "Only the Rat may swim. Lions and Tigers leap across the river, unless a Rat in the water blocks the way.",
                "An enemy standing in one of your traps loses its rank, so any of your animals can take it.",
                "Walk into the opponent's den, or capture every enemy animal, to win."],
         app=["Every piece shows its rank, and a Ranks button explains them all.",
              "Play the AI at three levels or a friend on one device."]),
    dict(slug="luzhanqi", name="Luzhanqi", aka="Army Chess · Land Battle Chess · 陆战棋 · 军棋", players="2 players",
         title="Luzhanqi (Army Chess 军棋) Offline vs AI – Free Android App",
         desc="Play Luzhanqi, Chinese Army Chess (军棋 / 陆战棋), offline on Android: Hidden, Open and Flip rules against the AI. Free, no account needed.",
         intro="Chinese Army Chess: deploy twenty-five pieces with their ranks hidden, probe the enemy lines, and bluff your way to the opposing flag.",
         rules=["Each side deploys twenty-five pieces: officers from Field Marshal down to Engineer, plus bombs, landmines and a flag.",
                "When two pieces meet, the higher rank wins, and equal ranks remove each other.",
                "A bomb destroys whatever it meets, and itself with it.",
                "Landmines and the flag never move. Only an engineer can clear a landmine without being lost.",
                "Railways carry pieces a long way in a straight line, and engineers can turn corners on them. A piece in a camp cannot be attacked.",
                "Capture the enemy flag to win."],
         app=["Three ways to play: Hidden, Open and Flip.",
              "Arrange your own deployment or start from a random setup.",
              "The app settles every battle, so hidden ranks stay hidden with no referee needed."]),
    dict(slug="ludo", name="Ludo", aka="The family race game", players="2, 3 or 4 players",
         title="Ludo Offline – 2 to 4 Players vs AI or Friends on Android",
         desc="Play Ludo offline on Android with 2, 3 or 4 players: family and friends on one phone, the AI, or both. Free, no sign-in, no Wi-Fi needed.",
         intro="Roll the die, bring your four tokens out, run them round the board and get them all home before anyone else.",
         rules=["Roll a six to bring a token out of your yard.",
                "Move a token forward by the number you roll.",
                "Land on an opponent's token to send it back to its yard; tokens on safe squares cannot be captured.",
                "Get all four tokens home first to win."],
         app=["2, 3 or 4 players on one device.",
              "Any seat can be a person or the AI."]),
    dict(slug="aeroplane-chess", name="Aeroplane Chess", aka="Flying Chess · 飞行棋", players="2, 3 or 4 players",
         title="Aeroplane Chess (Flying Chess 飞行棋) Offline – Android",
         desc="Play Aeroplane Chess, Flying Chess (飞行棋), offline on Android with 2 to 4 players and the AI. Jumps, shortcut flights and captures. Free.",
         intro="China's favourite take on the Ludo race, with planes instead of tokens, and jumps and shortcut flights that can turn the game around in a single roll.",
         rules=["Roll a six to take a plane off from its hangar.",
                "Land on a square of your own colour to jump ahead to the next one.",
                "Some squares launch a shortcut flight straight across the board.",
                "Land on an opponent's plane to send it back to its hangar.",
                "Overshoot the finish and you bounce back. Fly all four planes home first to win."],
         app=["2, 3 or 4 players on one device.",
              "Any seat can be a person or the AI."]),
    dict(slug="yutnori", name="Yutnori", aka="Yut Nori · 윷놀이", players="2 players",
         title="Yutnori (윷놀이) Offline – Play Yut Nori vs AI on Android",
         desc="Play Yutnori (Yut Nori, 윷놀이), the traditional Korean stick-throwing game, offline on Android against the AI or a friend. Free, no account.",
         intro="Korea's traditional New Year game. Throw four yut sticks, race your markers around the board, and cut through the middle on the corner shortcuts.",
         rules=["Throw four sticks. The result moves you one to five spaces: Do (1), Gae (2), Geol (3), Yut (4) or Mo (5).",
                "Throwing Yut or Mo, or capturing an opponent's marker, earns another throw.",
                "Stop on a corner and you can take the diagonal shortcut through the centre.",
                "Markers that share a point travel together as a stack.",
                "Land on an opponent to send their markers back to the start. Bring all four markers home first to win."],
         app=["Four markers per side; tap the sticks to throw.",
              "Play the AI or a friend on one device."]),
]
GAMES.sort(key=lambda g: g["slug"] != "animal-chess")
BY_SLUG = {g["slug"]: g for g in GAMES}
ASIAN = {"animal-chess": "斗兽棋", "xiangqi": "象棋", "shogi": "将棋", "gomoku": "五子棋",
         "luzhanqi": "军棋", "aeroplane-chess": "飞行棋", "yutnori": "윷놀이"}


def head(title, desc, url, root, extra=""):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{APP_NAME}">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}img/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0b2822">
<link rel="icon" type="image/png" sizes="32x32" href="{root}img/favicon-32.png">
<link rel="apple-touch-icon" href="{root}img/apple-touch-icon.png">
<link rel="stylesheet" href="{root}style.css">
{extra}</head>
<body>
<header class="top"><div class="wrap">
  <a class="brand" href="{root or './'}"><img src="{root}img/icon-256.webp" alt="" width="34" height="34">Classic Board Games</a>
  <nav><a href="{root}#games">Games</a><a href="{root}#screenshots">Screenshots</a><a href="{root}#faq">FAQ</a></nav>
</div></header>
"""


def badge(root, campaign, big=True):
    h = 72 if big else 60
    return (f'<a class="badge" href="{escape(play_url(campaign))}">'
            f'<img src="{root}img/google-play-badge.png" alt="Get it on Google Play" width="{round(646 * h / 250)}" height="{h}"></a>')


def footer(root):
    return f"""<footer><div class="wrap">
  <p>© 2026 {DEVELOPER} · <a href="{PRIVACY}">Privacy policy</a> · <a href="{escape(play_url('footer'))}">Google Play</a></p>
  <p>Google Play and the Google Play logo are trademarks of Google LLC.</p>
</div></footer>
</body>
</html>
"""


def jsonld(data):
    return f'<script type="application/ld+json">{json.dumps(data, ensure_ascii=False)}</script>\n'


def index():
    app = {
        "@context": "https://schema.org", "@type": "MobileApplication",
        "name": APP_NAME, "operatingSystem": "Android 7.0+",
        "applicationCategory": "GameApplication", "applicationSubCategory": "Board game",
        "description": "Twelve classic board games in one app, played offline against the AI or a friend.",
        "url": BASE, "installUrl": f"https://play.google.com/store/apps/details?id={APP_ID}",
        "image": BASE + "img/icon-512.png",
        "screenshot": [BASE + f"img/shots/{s}.webp" for s in ("lobby", "chess", "xiangqi", "animal-chess")],
        "inLanguage": ["en", "zh", "ja", "ko", "vi", "ms", "th", "lo", "es", "de"],
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        "author": {"@type": "Organization", "name": DEVELOPER},
    }
    title = "Classic Board Games Offline – Animal Chess, Chess, Xiangqi, Shogi & more"
    desc = ("12 classic board games in one free Android app: Animal Chess (Dou Shou Qi), Chess, Xiangqi, Shogi, "
            "Gomoku, Luzhanqi, Yutnori, Ludo and more. Play offline against the AI or a friend.")
    cards = "\n".join(
        f'<a class="game" href="games/{g["slug"]}/"><img src="img/games/{g["slug"]}.webp" alt="" width="112" height="112" loading="lazy">'
        f'<strong>{escape(g["name"])}</strong><span>{escape(g["aka"])}</span></a>' for g in GAMES)
    chips = "\n".join(
        f'<li><a href="games/{s}/"><img src="img/games/{s}.webp" alt="" width="30" height="30" loading="lazy">'
        f'{escape(BY_SLUG[s]["name"])} <small>{native}</small></a></li>' for s, native in ASIAN.items())
    shots = [("lobby", "Twelve games, one lobby"), ("chess", "Chess"), ("xiangqi", "Xiangqi"), ("animal-chess", "Animal Chess"),
             ("luzhanqi", "Luzhanqi deployment"), ("gomoku", "Gomoku"), ("ludo", "Ludo"), ("yutnori", "Yutnori"),
             ("shogi", "Shogi"), ("chinese-checkers", "Chinese Checkers")]
    strip = "\n".join(
        f'<figure><img src="img/shots/{s}.webp" alt="{escape(c)} in Classic Board Games Offline" width="{shot_size(s)[0]}" height="{shot_size(s)[1]}" loading="lazy">'
        f'<figcaption>{escape(c)}</figcaption></figure>' for s, c in shots)
    faq = [
        ("Is it free?", "Yes. All twelve games, the Easy and Normal AI, and two-player games on one device are free and unlimited. "
                        "Optional short ads add extra Undo and Load uses, and a one-time Premium purchase unlocks the Expert AI, "
                        "unlimited Undo and Load, and removes all ads. There is no subscription."),
        ("Does it work offline?", "Yes. Every game and the AI run on your phone, so you can play on a plane, on the subway or anywhere "
                                  "without a signal. Only ads and purchases use the internet."),
        ("Can two people play on one phone?", "Yes. Every game supports pass-and-play on one device. Ludo and Aeroplane Chess take up to "
                                               "four players and Chinese Checkers up to six, and any seat can be a person or the AI."),
        ("Do I need an account?", "No. There is no account and no sign-in."),
        ("Which languages does it support?", "Ten: " + ", ".join(LANGUAGES) + "."),
        ("Which devices does it run on?", "Android 7.0 or newer, on phones and tablets. Tablets get their own layout with a side panel "
                                           "rather than a stretched phone screen."),
    ]
    faq_html = "\n".join(f"<details><summary>{escape(q)}</summary><p>{escape(a)}</p></details>" for q, a in faq)
    html = head(title, desc, BASE, "", jsonld(app)) + f"""
<main>
<section class="hero"><div class="wrap">
  <div>
    <p class="eyebrow">Free board games for Android</p>
    <h1>Classic Board Games Offline</h1>
    <p class="lead">Twelve board games from East and West in one small app: Animal Chess (Dou Shou Qi), Chess,
      Xiangqi, Shogi, Gomoku, Luzhanqi, Yutnori, Ludo and more. Play the AI or a friend on one device, with no internet and no sign-in.</p>
    {badge("", "home_hero")}
    <ul class="facts"><li>12 games</li><li>Works offline</li><li>3 AI levels</li><li>2–6 players on one device</li><li>10 languages</li></ul>
  </div>
  <img class="hero-shot" src="img/shots/tablet-lobby.webp" alt="The Classic Board Games lobby with all twelve games" width="1280" height="720">
</div></section>

<section id="games"><div class="wrap">
  <h2>Twelve games, one app</h2>
  <p class="section-lead">Every game has its real rules, a computer opponent with three levels, and a two-player mode for
    playing face to face on one phone or tablet. Pick one to read the rules.</p>
  <div class="games">
{cards}
  </div>
</div></section>

<section id="asian"><div class="wrap split">
  <div>
    <h2>The Asian board games you grew up with</h2>
    <p>Most board game apps stop at Chess and Ludo. This one also brings the games played on kitchen tables, school desks and
      New Year floors across Asia: Chinese Chess and Japanese Shogi, Gomoku, the Animal Chess every child in China knows,
      the bluffing battles of Army Chess, the Flying Chess race, and Korea's Yutnori.</p>
    <p>They are hard to find in one place, and harder to find with an opponent who knows the rules. Here each one has a
      computer player that does, and it plays without an internet connection.</p>
    <ul class="chips">
{chips}
    </ul>
  </div>
  <img class="hero-shot" src="img/shots/tablet-animal-chess.webp" alt="Animal Chess (Dou Shou Qi) on a tablet" width="1280" height="720" loading="lazy">
</div></section>

<section id="screenshots"><div class="wrap">
  <h2>Screenshots</h2>
  <p class="section-lead">Wooden boards, traditional pieces and a calm green table, on phones and tablets.</p>
  <div class="shots">
{strip}
  </div>
</div></section>

<section id="features"><div class="wrap">
  <h2>Built to stay out of your way</h2>
  <div class="features">
    <div class="feature"><h3>Play the AI or a friend</h3><p>Easy, Normal and Expert AI. Two players on one device, up to four in Ludo
      and Aeroplane Chess and six in Chinese Checkers. Any seat can be a person or the AI, even AI against AI.</p></div>
    <div class="feature"><h3>Offline, no account</h3><p>The games and the AI run on your device. No account, no sign-in, a small
      download and light on battery.</p></div>
    <div class="feature"><h3>Undo, replay, save</h3><p>Take back a move, replay a finished game from the start, keep a separate save
      for every game, and add an optional chess clock.</p></div>
    <div class="feature"><h3>No pop-up ads</h3><p>One small banner on the result screen, and rewarded ads only when you choose to watch
      one. A one-time Premium purchase removes all of it.</p></div>
    <div class="feature"><h3>Phone and tablet</h3><p>A real tablet layout with a side panel, not a stretched phone screen, and ten
      interface languages.</p></div>
  </div>
</div></section>

<section id="faq"><div class="wrap faq">
  <h2>Questions</h2>
{faq_html}
</div></section>

<section class="cta"><div class="wrap">
  <h2>Ready for a game?</h2>
  <p class="section-lead" style="margin: 0 auto 20px">Free on Google Play for Android phones and tablets.</p>
  {badge("", "home_bottom")}
</div></section>
</main>
""" + footer("")
    (OUT / "index.html").write_text(html, encoding="utf-8")


def game_page(g):
    root = "../../"
    url = f"{BASE}games/{g['slug']}/"
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": APP_NAME, "item": BASE},
        {"@type": "ListItem", "position": 2, "name": g["name"], "item": url}]}
    rules = "\n".join(f"<li>{escape(r)}</li>" for r in g["rules"])
    app = "\n".join(f"<li>{escape(a)}</li>" for a in g["app"])
    more = "\n".join(
        f'<a href="../{o["slug"]}/"><img src="{root}img/games/{o["slug"]}.webp" alt="" width="72" height="72" loading="lazy">{escape(o["name"])}</a>'
        for o in GAMES if o is not g)
    html = head(g["title"], g["desc"], url, root, jsonld(crumbs)) + f"""
<main class="wrap">
<p class="crumbs"><a href="{root}">Classic Board Games</a> › <a href="{root}#games">Games</a> › {escape(g["name"])}</p>
<div class="game-hero">
  <div>
    <div class="title-row">
      <img src="{root}img/games/{g["slug"]}.webp" alt="" width="96" height="96">
      <div><h1>{escape(g["name"])}</h1><p class="aka">{escape(g["aka"])}</p></div>
    </div>
    <p class="lead">{escape(g["intro"])}</p>
    <ul class="meta"><li>{escape(g["players"])}</li><li>vs AI or a friend</li><li>Works offline</li><li>Free</li></ul>
    {badge(root, g["slug"])}
    <h2 style="margin-top: 40px">How to play {escape(g["name"])}</h2>
    <ul class="rules">
{rules}
    </ul>
    <h2 style="margin-top: 40px">{escape(g["name"])} in Classic Board Games Offline</h2>
    <ul class="rules">
{app}
<li>Eleven more classic board games in the same free app, all playable offline.</li>
    </ul>
  </div>
  <div class="phone"><img src="{root}img/shots/{g["slug"]}.webp" alt="{escape(g["name"])} in Classic Board Games Offline on Android" width="{shot_size(g["slug"])[0]}" height="{shot_size(g["slug"])[1]}"></div>
</div>
<section><h2>More games in the app</h2><div class="more">
{more}
</div></section>
<section class="cta"><h2>Play {escape(g["name"])} for free</h2>
<p class="section-lead" style="margin: 0 auto 20px">On Android phones and tablets, with no internet needed.</p>
{badge(root, g["slug"] + "_bottom")}</section>
</main>
""" + footer(root)
    page = OUT / "games" / g["slug"] / "index.html"
    page.parent.mkdir(parents=True, exist_ok=True)
    page.write_text(html, encoding="utf-8")


def sitemap():
    urls = [BASE] + [f"{BASE}games/{g['slug']}/" for g in GAMES]
    body = "\n".join(f"  <url><loc>{u}</loc><lastmod>{UPDATED}</lastmod></url>" for u in urls)
    (OUT / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{body}\n</urlset>\n',
        encoding="utf-8")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}sitemap.xml\n", encoding="utf-8")


if __name__ == "__main__":
    index()
    for game in GAMES:
        game_page(game)
    sitemap()
