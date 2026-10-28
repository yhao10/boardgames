"""Generates the site's HTML, sitemap and robots.txt in every language. Run: python3 build.py

Each language lives in content/<code>.py; English is served at the root and the others under their own
folder (zh-hans/, ja/, ...). The rules lists of the translated pages come from content/app_rules.py, which
is exported from the app itself, so the site never states a rule the app does not play.
"""
import importlib
import json
from html import escape
from pathlib import Path

from PIL import Image

import diagrams
from content.app_rules import RULES

BASE = "https://yhao10.github.io/boardgames/"
APP_ID = "com.yhao10.boardgames"
APP_NAME = "Classic Board Games Offline"
DEVELOPER = "redpig"
PRIVACY = "https://boardgames-privacy.allenyuanchina.workers.dev/privacy-policy"
UPDATED = "2026-10-27"
OUT = Path(__file__).parent

LANGS = [importlib.import_module(f"content.{name}") for name in ("en", "zh_hans", "zh_hant", "ja", "ko", "vi", "th")]
DEFAULT = LANGS[0]
ORDER = ["animal-chess", "chess", "xiangqi", "shogi", "gomoku", "checkers", "four-in-a-row", "chinese-checkers",
         "luzhanqi", "ludo", "aeroplane-chess", "yutnori"]


def shot_size(name):
    return Image.open(OUT / "img" / "shots" / f"{name}.webp").size


def games(lang):
    by_slug = {g["slug"]: g for g in lang.GAMES}
    return [by_slug[slug] for slug in ORDER]


def rules(lang, game):
    return game["rules"] if lang is DEFAULT else RULES[lang.CODE][game["slug"]]


def play_url(lang, campaign):
    # The referrer shows up in Play Console's acquisition report, per page and language.
    if lang is not DEFAULT:
        campaign = f"{lang.CODE.replace('-', '_')}_{campaign}"
    hl = f"&hl={lang.PLAY_HL}" if lang.PLAY_HL else ""
    return (f"https://play.google.com/store/apps/details?id={APP_ID}{hl}"
            f"&referrer=utm_source%3Dgithub_pages%26utm_medium%3Dwebsite%26utm_campaign%3D{campaign}")


def alternates(path):
    links = [f'<link rel="alternate" hreflang="{l.HREFLANG}" href="{BASE}{l.PREFIX}{path}">' for l in LANGS]
    links.append(f'<link rel="alternate" hreflang="x-default" href="{BASE}{path}">')
    return "\n".join(links)


def switcher(lang, path, root):
    items = "".join(
        f'<li><a href="{root + l.PREFIX + path or "./"}" hreflang="{l.HREFLANG}" lang="{l.HTML_LANG}"'
        + (' aria-current="page"' if l is lang else '') + f'>{escape(l.LABEL)}</a></li>' for l in LANGS)
    globe = ('<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" fill="none" stroke="currentColor" '
             'stroke-width="1.8"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.7 3.8 5.7 3.8 9s-1.3 '
             '6.3-3.8 9c-2.5-2.7-3.8-5.7-3.8-9s1.3-6.3 3.8-9z"/></svg>')
    return (f'<details class="lang"><summary aria-label="{escape(lang.UI["language"])}">{globe}'
            f'<span>{escape(lang.LABEL)}</span></summary><ul>{items}</ul></details>')


def head(lang, title, desc, path, root, extra=""):
    url = BASE + lang.PREFIX + path
    home = root + lang.PREFIX
    ui = lang.UI
    return f"""<!doctype html>
<html lang="{lang.HTML_LANG}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc)}">
<link rel="canonical" href="{url}">
{alternates(path)}
<meta property="og:type" content="website">
<meta property="og:site_name" content="{APP_NAME}">
<meta property="og:locale" content="{lang.OG_LOCALE}">
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
  <a class="brand" href="{home or './'}"><img src="{root}img/icon-256.webp" alt="" width="34" height="34">{escape(lang.BRAND)}</a>
  <nav><a href="{home}#games">{escape(ui["nav_games"])}</a><a href="{home}#screenshots">{escape(ui["nav_shots"])}</a><a href="{home}#faq">{escape(ui["nav_faq"])}</a></nav>
  {switcher(lang, path, root)}
</div></header>
"""


def badge(lang, root, campaign, big=True):
    h = 72 if big else 60
    width, height = Image.open(OUT / "img" / lang.BADGE).size
    return (f'<a class="badge" href="{escape(play_url(lang, campaign))}">'
            f'<img src="{root}img/{lang.BADGE}" alt="{escape(lang.UI["badge_alt"])}" width="{round(width * h / height)}" '
            f'height="{h}"></a>')


def footer(lang, root):
    ui = lang.UI
    return f"""<footer><div class="wrap">
  <p>© 2026 {DEVELOPER} · <a href="{PRIVACY}">{escape(ui["privacy"])}</a> · <a href="{escape(play_url(lang, 'footer'))}">Google Play</a></p>
  <p>{escape(ui["trademark"])}</p>
</div></footer>
</body>
</html>
"""


def jsonld(data):
    return f'<script type="application/ld+json">{json.dumps(data, ensure_ascii=False)}</script>\n'


def write(lang, path, html):
    page = OUT / lang.PREFIX / path / "index.html"
    page.parent.mkdir(parents=True, exist_ok=True)
    page.write_text(html, encoding="utf-8")


def index(lang):
    t = lang.INDEX
    root = "../" * lang.PREFIX.count("/")
    url = BASE + lang.PREFIX
    by_slug = {g["slug"]: g for g in lang.GAMES}
    app = {
        "@context": "https://schema.org", "@type": "MobileApplication",
        "name": APP_NAME, "operatingSystem": "Android 7.0+",
        "applicationCategory": "GameApplication", "applicationSubCategory": "Board game",
        "description": t["app_desc"],
        "url": url, "installUrl": f"https://play.google.com/store/apps/details?id={APP_ID}",
        "image": BASE + "img/icon-512.png",
        "screenshot": [BASE + f"img/shots/{s}.webp" for s in ("lobby", "chess", "xiangqi", "animal-chess")],
        "inLanguage": ["en", "zh", "ja", "ko", "vi", "ms", "th", "lo", "es", "de"],
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        "author": {"@type": "Organization", "name": DEVELOPER},
    }
    cards = "\n".join(
        f'<a class="game" href="games/{g["slug"]}/"><img src="{root}img/games/{g["slug"]}.webp" alt="" width="112" height="112" loading="lazy">'
        f'<strong>{escape(g["name"])}</strong><span>{escape(g["aka"])}</span></a>' for g in games(lang))
    chips = "\n".join(
        f'<li><a href="games/{s}/"><img src="{root}img/games/{s}.webp" alt="" width="30" height="30" loading="lazy">'
        f'{escape(by_slug[s]["name"])}' + (f' <small>{escape(native)}</small>' if native else '') + '</a></li>'
        for s, native in t["chips"])
    strip = "\n".join(
        f'<figure><img src="{root}img/shots/{s}.webp" alt="{escape(lang.UI["shot_alt"].format(caption=c))}" width="{shot_size(s)[0]}" height="{shot_size(s)[1]}" loading="lazy">'
        f'<figcaption>{escape(c)}</figcaption></figure>' for s, c in t["shots"])
    features = "\n".join(f'    <div class="feature"><h3>{escape(h)}</h3><p>{escape(p)}</p></div>' for h, p in t["features"])
    faq_html = "\n".join(f"<details><summary>{escape(q)}</summary><p>{escape(a)}</p></details>" for q, a in t["faq"])
    facts = "".join(f"<li>{escape(f)}</li>" for f in t["facts"])
    asian = "\n".join(f"    <p>{escape(p)}</p>" for p in t["asian"])
    html = head(lang, t["title"], t["desc"], "", root, jsonld(app)) + f"""
<main>
<section class="hero"><div class="wrap">
  <div>
    <p class="eyebrow">{escape(t["eyebrow"])}</p>
    <h1>{escape(t["h1"])}</h1>
    <p class="lead">{escape(t["lead"])}</p>
    {badge(lang, root, "home_hero")}
    <ul class="facts">{facts}</ul>
  </div>
  <img class="hero-shot" src="{root}img/shots/tablet-lobby.webp" alt="{escape(t["hero_alt"])}" width="1280" height="720">
</div></section>

<section id="games"><div class="wrap">
  <h2>{escape(t["games_h2"])}</h2>
  <p class="section-lead">{escape(t["games_lead"])}</p>
  <div class="games">
{cards}
  </div>
</div></section>

<section id="asian"><div class="wrap split">
  <div>
    <h2>{escape(t["asian_h2"])}</h2>
{asian}
    <ul class="chips">
{chips}
    </ul>
  </div>
  <img class="hero-shot" src="{root}img/shots/tablet-animal-chess.webp" alt="{escape(t["asian_alt"])}" width="1280" height="720" loading="lazy">
</div></section>

<section id="screenshots"><div class="wrap">
  <h2>{escape(t["shots_h2"])}</h2>
  <p class="section-lead">{escape(t["shots_lead"])}</p>
  <div class="shots">
{strip}
  </div>
</div></section>

<section id="features"><div class="wrap">
  <h2>{escape(t["features_h2"])}</h2>
  <div class="features">
{features}
  </div>
</div></section>

<section id="faq"><div class="wrap faq">
  <h2>{escape(t["faq_h2"])}</h2>
{faq_html}
</div></section>

<section class="cta"><div class="wrap">
  <h2>{escape(t["cta_h2"])}</h2>
  <p class="section-lead" style="margin: 0 auto 20px">{escape(t["cta_lead"])}</p>
  {badge(lang, root, "home_bottom")}
</div></section>
</main>
""" + footer(lang, root)
    write(lang, "", html)


def detail_block(lang, block):
    kind = block[0]
    if kind in ("h3", "p"):
        return f"<{kind}>{escape(block[1])}</{kind}>"
    if kind in ("ul", "ol"):
        items = "".join(f"<li>{escape(item)}</li>" for item in block[1])
        return f'<{kind} class="rules">{items}</{kind}>'
    if kind == "figure":
        _, name, caption = block
        svg = diagrams.render(name, caption, lang.ANIMAL_NAMES)
        return f'<figure class="diagram">{svg}<figcaption>{escape(caption)}</figcaption></figure>'
    if kind == "legend":
        items = "".join(f"<li>{diagrams.legend_icon(icon)}<span>{escape(text)}</span></li>" for icon, text in block[1])
        return f'<ul class="legend">{items}</ul>'
    if kind == "table":
        _, header, rows = block
        head_row = "".join(f"<th>{escape(h)}</th>" for h in header)
        body = "".join("<tr>" + "".join(f"<td>{escape(str(c))}</td>" for c in row) + "</tr>" for row in rows)
        return f'<div class="table-wrap"><table><thead><tr>{head_row}</tr></thead><tbody>{body}</tbody></table></div>'
    raise ValueError(f"unknown detail block {kind}")


def game_page(lang, g):
    path = f"games/{g['slug']}/"
    root = "../" * (lang.PREFIX + path).count("/")
    home = root + lang.PREFIX
    ui = lang.UI
    url = BASE + lang.PREFIX + path
    name = g["name"]
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": APP_NAME if lang is DEFAULT else lang.BRAND, "item": BASE + lang.PREFIX},
        {"@type": "ListItem", "position": 2, "name": name, "item": url}]}
    rule_items = "\n".join(f"<li>{escape(r)}</li>" for r in rules(lang, g))
    app = "\n".join(f"<li>{escape(a)}</li>" for a in g["app"])
    more = "\n".join(
        f'<a href="../{o["slug"]}/"><img src="{root}img/games/{o["slug"]}.webp" alt="" width="72" height="72" loading="lazy">{escape(o["name"])}</a>'
        for o in games(lang) if o is not g)
    detail = lang.DETAIL.get(g["slug"])
    detail_link = f'\n    <p class="detail-link"><a href="#rules">{escape(ui["detail_link"])} ↓</a></p>' if detail else ""
    detail_html = ""
    if detail:
        blocks = "\n".join(detail_block(lang, b) for b in detail["blocks"])
        detail_html = f'<section class="detail" id="rules"><h2>{escape(detail["h2"])}</h2>\n{blocks}\n</section>\n'
    html = head(lang, g["title"], g["desc"], path, root, jsonld(crumbs)) + f"""
<main class="wrap">
<p class="crumbs"><a href="{home}">{escape(lang.BRAND)}</a> › <a href="{home}#games">{escape(ui["crumbs_games"])}</a> › {escape(name)}</p>
<div class="game-hero">
  <div>
    <div class="title-row">
      <img src="{root}img/games/{g["slug"]}.webp" alt="" width="96" height="96">
      <div><h1>{escape(name)}</h1><p class="aka">{escape(g["aka"])}</p></div>
    </div>
    <p class="lead">{escape(g["intro"])}</p>
    <ul class="meta"><li>{escape(g["players"])}</li><li>{escape(ui["vs"])}</li><li>{escape(ui["offline"])}</li><li>{escape(ui["free"])}</li></ul>
    {badge(lang, root, g["slug"])}
    <h2 style="margin-top: 40px">{escape(ui["how_to_play"].format(name=name))}</h2>
    <ul class="rules">
{rule_items}
    </ul>{detail_link}
    <h2 style="margin-top: 40px">{escape(ui["in_app"].format(name=name))}</h2>
    <ul class="rules">
{app}
<li>{escape(ui["eleven_more"])}</li>
    </ul>
  </div>
  <div class="phone"><img src="{root}img/shots/{g["slug"]}.webp" alt="{escape(ui["phone_alt"].format(name=name))}" width="{shot_size(g["slug"])[0]}" height="{shot_size(g["slug"])[1]}"></div>
</div>
{detail_html}<section><h2>{escape(ui["more_games"])}</h2><div class="more">
{more}
</div></section>
<section class="cta"><h2>{escape(ui["cta_game"].format(name=name))}</h2>
<p class="section-lead" style="margin: 0 auto 20px">{escape(ui["cta_game_lead"])}</p>
{badge(lang, root, g["slug"] + "_bottom")}</section>
</main>
""" + footer(lang, root)
    write(lang, path, html)


def sitemap():
    paths = [""] + [f"games/{slug}/" for slug in ORDER]
    entries = []
    for path in paths:
        links = "".join(f'\n    <xhtml:link rel="alternate" hreflang="{l.HREFLANG}" href="{BASE}{l.PREFIX}{path}"/>'
                        for l in LANGS)
        for lang in LANGS:
            entries.append(f"  <url><loc>{BASE}{lang.PREFIX}{path}</loc><lastmod>{UPDATED}</lastmod>{links}\n  </url>")
    (OUT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
        'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(entries) + "\n</urlset>\n", encoding="utf-8")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}sitemap.xml\n", encoding="utf-8")


if __name__ == "__main__":
    for language in LANGS:
        index(language)
        for game in games(language):
            game_page(language, game)
    sitemap()
