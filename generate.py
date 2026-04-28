#!/usr/bin/env python3
"""
Casino Arena — Programmatic Page Generator
Reads keywords.json + casinos.json + templates → generates pages/ + kasina/
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def load_json(filename):
    with open(os.path.join(BASE_DIR, 'data', filename), 'r', encoding='utf-8') as f:
        return json.load(f)


def load_file(filename):
    with open(os.path.join(BASE_DIR, filename), 'r', encoding='utf-8') as f:
        return f.read()


def stars_html(rating):
    full = int(rating)
    half = 1 if rating - full >= 0.3 else 0
    return '★' * full + ('½' if half else '') + '☆' * (5 - full - half)


def get_logo_ext(slug):
    """Find the actual logo file extension for a casino slug."""
    logos_dir = os.path.join(BASE_DIR, 'assets', 'images', 'casinos')
    for ext in ['png', 'jpg', 'webp', 'svg', 'ico', 'jpeg']:
        if os.path.exists(os.path.join(logos_dir, f'{slug}.{ext}')):
            return ext
    return 'svg'  # fallback


# ============================================================
# NAVIGATION HTML (Mega Menu)
# ============================================================
CHEVRON_SVG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path fill-rule="evenodd" d="M12.53 16.28a.75.75 0 0 1-1.06 0l-7.5-7.5a.75.75 0 0 1 1.06-1.06L12 14.69l6.97-6.97a.75.75 0 1 1 1.06 1.06l-7.5 7.5Z" clip-rule="evenodd"/></svg>'

NAV_HTML = f'''<!-- TOP BANNER -->
<div class="top-banner">
    🎰 Dnes bonus až 10 000 Kč + 200 free spinů — <a href="/nejlepsi-kasinovy-bonus/">Získat bonus →</a>
</div>
<!-- TOPBAR -->
<div class="topbar">
    <button class="hamburger" id="menuOpen">☰</button>
    <a href="/" class="topbar-logo"><img src="/assets/images/logo.svg" alt="Casinos Czech"></a>
    <div class="topbar-right">
        <input type="text" class="topbar-search" placeholder="Hledat...">
    </div>
</div>

<!-- SIDEBAR -->
<div class="sidebar-overlay" id="sidebarOverlay"></div>
<nav class="sidebar" id="sidebar">
    <div class="sidebar-header">
        <img src="/assets/images/logo.svg" alt="Casinos Czech" height="28">
        <button class="sidebar-close" id="menuClose">✕</button>
    </div>
    <ul class="sidebar-nav">
        <!-- KASINA -->
        <li>
            <div class="menu-heading">Kasina {CHEVRON_SVG}</div>
            <ul class="submenu">
                <li><a href="/nejlepsi-kasina-cz/">Nejlepší kasina</a></li>
                <li><a href="/nove-kasina-2026/">Nová kasina 2026</a></li>
                <li><a href="/kasina-ceska-licence/">Česká kasina</a></li>
                <li><a href="/bezpecna-kasina/">Bezpečná kasina</a></li>
                <li><a href="/kasino-bez-limitu/">Kasina bez limitu</a></li>
                <li><a href="/top-10-kasin/">Top 10 kasin</a></li>
                <!-- Sub: Platební metody -->
                <li>
                    <div class="sub-heading">Platební metody {CHEVRON_SVG}</div>
                    <ul class="sub-submenu">
                        <li><a href="/pruvodce/paysafecard-kasino/">PaySafeCard</a></li>
                        <li><a href="/pruvodce/bitcoin-kasino/">Bitcoin / Krypto</a></li>
                        <li><a href="/pruvodce/apple-pay-kasino/">Apple Pay</a></li>
                        <li><a href="/pruvodce/skrill-neteller-kasino/">Skrill & Neteller</a></li>
                        <li><a href="/pruvodce/bankovni-prevod-kasino/">Bankovní převod</a></li>
                    </ul>
                </li>
                <!-- Sub: Bonusy -->
                <li>
                    <div class="sub-heading">Bonusy {CHEVRON_SVG}</div>
                    <ul class="sub-submenu">
                        <li><a href="/nejlepsi-kasinovy-bonus/">Všechny bonusy</a></li>
                        <li><a href="/casino-bonusy-bez-vkladu/">Bez vkladu</a></li>
                        <li><a href="/free-spiny-dnes/">Free spiny</a></li>
                        <li><a href="/kasino-free-spiny/">Kasino free spiny</a></li>
                        <li><a href="/kasino-nizka-sazka/">Nízké sázky</a></li>
                    </ul>
                </li>
                <!-- Sub: Výhody -->
                <li>
                    <div class="sub-heading">Výhody {CHEVRON_SVG}</div>
                    <ul class="sub-submenu">
                        <li><a href="/mobilni-kasino/">Mobilní kasino</a></li>
                        <li><a href="/kasino-pro-zacatecniky/">Pro začátečníky</a></li>
                        <li><a href="/kasino-bez-limitu/">Bez limitu</a></li>
                        <li><a href="/kasino-na-penize/">Za skutečné peníze</a></li>
                    </ul>
                </li>
                <!-- Sub: Typ her -->
                <li>
                    <div class="sub-heading">Typ her {CHEVRON_SVG}</div>
                    <ul class="sub-submenu">
                        <li><a href="/sazeni-na-sport/">Sportovní sázky</a></li>
                        <li><a href="/live-kasino/">Live kasino</a></li>
                        <li><a href="/casino-vyherni-automaty/">Automaty</a></li>
                        <li><a href="/poker-online/">Poker</a></li>
                        <li><a href="/loterie-online/">Loterie</a></li>
                    </ul>
                </li>
            </ul>
        </li>
        <!-- HRY -->
        <li>
            <div class="menu-heading">Kasinové hry {CHEVRON_SVG}</div>
            <ul class="submenu">
                <li><a href="/casino-vyherni-automaty/">Výherní automaty</a></li>
                <li><a href="/automaty-zdarma/">Automaty zdarma</a></li>
                <li><a href="/live-kasino/">Live kasino</a></li>
                <li><a href="/poker-online/">Poker online</a></li>
                <li><a href="/jackpot-kasino/">Jackpot automaty</a></li>
                <li><a href="/rtp-automaty/">Vysoké RTP automaty</a></li>
                <li><a href="/volatilita-automaty/">Volatilita automatů</a></li>
            </ul>
        </li>
        <!-- PRŮVODCE -->
        <li>
            <div class="menu-heading">Průvodce {CHEVRON_SVG}</div>
            <ul class="submenu">
                <li><a href="/kasino-pro-zacatecniky/">Pro začátečníky</a></li>
                <li><a href="/legalni-kasina-cz/">Legální kasina v ČR</a></li>
                <li><a href="/online-hazard-cz/">Online hazard v ČR</a></li>
                <li><a href="/dane-z-vyhry/">Daně z výher</a></li>
                <li><a href="/sebeomezeni-hazard/">Odpovědné hraní</a></li>
            </ul>
        </li>
        <!-- FOURNISSEURS -->
        <li>
            <a href="/kasina/" class="menu-link">Recenze kasin</a>
        </li>
    </ul>
</nav>'''


AUTHOR_HTML = '''<div class="author-box">
    <div class="author-avatar">MN</div>
    <div class="author-info">
        <div class="author-name">Martin Novák <span>— Expert iGaming</span></div>
        <div class="author-meta">Aktualizováno {{date}} · {{read_time}} min čtení</div>
    </div>
</div>'''


# ============================================================
# FOOTER HTML
# ============================================================
FOOTER_HTML = '''<footer class="footer">
    <div class="container">
        <div class="footer-disclaimer">⚠️ Hazardní hry jsou určeny pouze pro osoby starší 18 let. Hrajte odpovědně. Pokud máte problém s hazardem, kontaktujte <a href="https://www.clvh.cz">www.clvh.cz</a></div>
        <div class="footer-grid">
            <div>
                <h4>Casino Arena</h4>
                <ul>
                    <li><a href="/">Domů</a></li>
                    <li><a href="/nejlepsi-kasina-cz/">Nejlepší Kasina</a></li>
                    <li><a href="/top-10-kasin/">Top 10 Kasin</a></li>
                </ul>
            </div>
            <div>
                <h4>Kasina</h4>
                <ul>
                    <li><a href="/kasina/synot-tip/">Synot Tip</a></li>
                    <li><a href="/kasina/fortuna/">Fortuna</a></li>
                    <li><a href="/kasina/bet365/">Bet365</a></li>
                    <li><a href="/kasina/tipsport/">Tipsport</a></li>
                    <li><a href="/kasina/pinnacle/">Pinnacle</a></li>
                    <li><a href="/kasina/888-casino/">888 Casino</a></li>
                </ul>
            </div>
            <div>
                <h4>Bonusy</h4>
                <ul>
                    <li><a href="/free-spiny-dnes/">Free Spiny Dnes</a></li>
                    <li><a href="/kasina-bez-vkladu/">Kasina Bez Vkladu</a></li>
                    <li><a href="/nejlepsi-kasinovy-bonus/">Nejlepší Bonusy</a></li>
                </ul>
            </div>
            <div>
                <h4>Informace</h4>
                <ul>
                    <li><a href="/kasino-pro-zacatecniky/">Pro Začátečníky</a></li>
                    <li><a href="/legalni-kasina-cz/">Legální Kasina</a></li>
                    <li><a href="/sebeomezeni-hazard/">Odpovědné Hraní</a></li>
                    <li><a href="https://www.clvh.cz">Pomoc s Hazardem</a></li>
                </ul>
            </div>
        </div>
        <div class="footer-bottom">
            <p>© 2026 CasinoArena.cz – Nezávislý průvodce online kasiny v České republice</p>
            <p>Všechna kasina v našem přehledu jsou licencovaná. Hrajte odpovědně. 18+</p>
        </div>
    </div>
</footer>'''


# ============================================================
# KEYWORD PAGE GENERATION
# ============================================================

def build_top_card(casino, rank):
    fs_feature = ''
    if casino['freeSpins'] > 0:
        fs_feature = f'<div class="top-card-feature"><span class="check">✔</span> {casino["freeSpins"]} free spinů zdarma</div>'

    bonus_amount = casino.get('bonusAmount', '')
    wagering = casino.get('wagering', '—')
    features_list = casino.get('features', [])
    review = casino.get('review', {})
    speed = review.get('withdrawalSpeed', 'Rychlý') if review else 'Rychlý'

    features_html = f'<div class="top-card-feature"><span class="check">✔</span> <a href="/kasina/{casino["slug"]}/">{rank}. {casino["name"]}</a></div>\n'
    for feat in features_list[:3]:
        features_html += f'<div class="top-card-feature"><span class="check">✔</span> {feat}</div>\n'
    if fs_feature:
        features_html += fs_feature

    bonus_sub = ''
    if casino['freeSpins'] > 0:
        bonus_sub = f'<div class="top-card-bonus-sub">+ {casino["freeSpins"]} free spinů</div>'

    return f'''<div class="top-card">
    <div class="top-card-left">
        <span class="top-card-rank">{rank}</span>
        <div class="top-card-logo"><img src="/assets/images/casinos/{casino["slug"]}.{get_logo_ext(casino["slug"])}" alt="{casino["name"]}"></div>
        <div class="top-card-rating"><span class="stars">{stars_html(casino["rating"])}</span> {casino["rating"]}/5</div>
        <div class="top-card-payment"><svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg> Výběr: {speed}</div>
    </div>
    <div class="top-card-center">
        {features_html}
    </div>
    <div class="top-card-right">
        <div>
            <div class="top-card-bonus">{casino["bonus"]}</div>
            {bonus_sub}
        </div>
        <a href="{casino["bonusUrl"]}" class="btn-cta" target="_blank" rel="nofollow noopener">Hrát nyní</a>
    </div>
</div>'''


def build_casino_tops(casinos):
    cards = '\n'.join(build_top_card(c, i) for i, c in enumerate(casinos, 1))
    return f'<div class="casino-tops">\n{cards}\n</div>'


def build_faq_html(faq_items):
    items = []
    for item in faq_items:
        items.append(f'''<div class="faq-item">
    <div class="faq-q"><span>{item["q"]}</span><span class="arrow">▼</span></div>
    <div class="faq-a">{item["a"]}</div>
</div>''')
    return '\n'.join(items)


def build_related_html(related_slugs, all_keywords):
    slug_to_title = {kw['slug']: kw['title'] for kw in all_keywords}
    pills = []
    for slug in related_slugs:
        title = slug_to_title.get(slug, slug)
        pills.append(f'<a href="/{slug}/" class="link-pill">{title}</a>')
    return '\n'.join(pills)


import re
from datetime import datetime

def build_breadcrumb(title, slug, parent=None, parent_title=None):
    bc = '<div class="breadcrumb"><span class="home-icon">🏠</span><a href="/">Domů</a>'
    if parent:
        bc += f'<span class="sep">›</span><a href="/{parent}/">{parent_title}</a>'
    bc += f'<span class="sep">›</span><span class="current">{title}</span></div>'
    return bc


def build_author_box(read_time=8):
    today = datetime.now().strftime('%d. %m. %Y')
    return AUTHOR_HTML.replace('{{date}}', today).replace('{{read_time}}', str(read_time))


def build_toc(seo_content):
    headings = re.findall(r'<h2>(.*?)</h2>', seo_content)
    if not headings:
        return ''
    items = ''
    for i, h in enumerate(headings):
        anchor = f'sec-{i+1}'
        items += f'<li><a href="#{anchor}">{h}</a></li>\n'
    toc = f'''<div class="toc" id="toc">
    <div class="toc-header" onclick="this.parentElement.classList.toggle('closed')">
        <span class="toc-title"><span class="icon">📑</span> Obsah článku</span>
        <span class="toc-toggle">▼</span>
    </div>
    <ol class="toc-list">{items}</ol>
</div>'''
    # Add IDs to h2 tags in content
    counter = [0]
    def add_id(m):
        counter[0] += 1
        return f'<h2 id="sec-{counter[0]}">{m.group(1)}</h2>'
    return toc, re.sub(r'<h2>(.*?)</h2>', add_id, seo_content)


def generate_keyword_page(keyword, casinos, template, all_keywords):
    casino_table = build_casino_tops(casinos)
    faq_html = build_faq_html(keyword.get('faq', []))
    related_html = build_related_html(keyword.get('related', []), all_keywords)
    breadcrumb = build_breadcrumb(keyword['title'], keyword['slug'])
    author_box = build_author_box(10)

    seo_content = keyword['seo_content']
    toc_result = build_toc(seo_content)
    if toc_result:
        toc_html, seo_content = toc_result
    else:
        toc_html = ''

    html = template
    html = html.replace('{{slug}}', keyword['slug'])
    html = html.replace('{{title}}', keyword['title'])
    html = html.replace('{{h1}}', keyword['h1'])
    html = html.replace('{{description}}', keyword['description'])
    html = html.replace('{{intro}}', keyword['intro'])
    html = html.replace('{{casino_cards}}', casino_table)
    html = html.replace('{{seo_content}}', seo_content)
    html = html.replace('{{faq_html}}', faq_html)
    html = html.replace('{{related_html}}', related_html)
    html = html.replace('{{nav_html}}', NAV_HTML)
    html = html.replace('{{footer_html}}', FOOTER_HTML)
    html = html.replace('{{breadcrumb}}', breadcrumb)
    html = html.replace('{{author_box}}', author_box)
    html = html.replace('{{toc}}', toc_html)

    return html


# ============================================================
# CASINO REVIEW PAGE GENERATION
# ============================================================

GAME_CATEGORIES = [
    ("🎰", "Automaty"),
    ("🃏", "Stolní hry"),
    ("🎥", "Live kasino"),
    ("⚡", "Crash hry"),
    ("🎯", "Mini hry"),
    ("🏀", "Sportovní sázky"),
    ("🎮", "eSport"),
    ("🎲", "Keno"),
    ("🃏", "Baccarat"),
    ("🎰", "Jackpoty"),
    ("🎪", "Game shows"),
    ("🃏", "Poker"),
    ("🎱", "Plinko"),
    ("💣", "Mines"),
    ("🎰", "Megaways"),
    ("🎫", "Stírací losy"),
]


def build_game_cats_html():
    items = []
    for icon, name in GAME_CATEGORIES:
        items.append(f'''<div class="game-cat">
            <span class="game-cat-icon">{icon}</span>
            <span class="game-cat-name">{name}</span>
        </div>''')
    return '\n'.join(items)


# Top preview carousels (game cats, payments, providers)
PREVIEW_GAME_CATS = [
    ("🃏", "BlackJack"), ("🎰", "Plinko"), ("🎯", "Ruleta"),
    ("🎴", "Stolní hry"), ("🎰", "Automaty"), ("🎥", "Live kasino"),
    ("⚡", "Crash game"), ("🎮", "Mini-hry"), ("🃏", "Video Poker"),
    ("🎲", "Baccarat"), ("🎫", "Bingo"), ("🎲", "Keno"),
    ("⚽", "Sportovní sázky"), ("🎮", "eSport"), ("🏆", "Turnaje"),
]


def build_preview_games_html():
    items = []
    for icon, name in PREVIEW_GAME_CATS:
        items.append(f'''<div class="preview-card">
            <span class="preview-card-icon">{icon}</span>
            <span class="preview-card-name">{name}</span>
        </div>''')
    return '\n'.join(items)


def build_preview_payments_html(methods):
    img_map = {
        "Visa": "visa.svg", "Mastercard": "mastercard.png",
        "Bankovní převod": "bankovni-prevod.svg", "Skrill": "skrill.svg",
        "Neteller": "neteller.svg", "PaySafeCard": "paysafecard.ico",
        "Apple Pay": "apple-pay.svg", "PayPal": "paypal.png",
        "MuchBetter": "muchbetter.ico",
    }
    emoji_map = {
        "Google Pay": "📱", "Hotovost (pobočky)": "💵", "Sportka Pay": "🎫",
        "Maestro": "💳", "Bitcoin": "₿", "Ethereum": "⟠",
        "USDT": "💲", "ecoPayz": "💰", "Jeton": "💰",
        "Trustly": "🏦", "Přímý bankovní převod": "🏦",
    }
    items = []
    for m in methods[:10]:
        if m in img_map:
            icon = f'<img src="/assets/images/payments/{img_map[m]}" alt="{m}" class="preview-card-img">'
        else:
            icon = f'<span class="preview-card-icon">{emoji_map.get(m, "💳")}</span>'
        items.append(f'''<div class="preview-card">
            {icon}
            <span class="preview-card-name">{m}</span>
        </div>''')
    return '\n'.join(items)


def build_preview_providers_html(providers):
    items = []
    for p in providers[:12]:
        items.append(f'''<div class="preview-card">
            <span class="preview-card-icon">🎮</span>
            <span class="preview-card-name">{p}</span>
        </div>''')
    return '\n'.join(items)


def build_bonus_pack_html(bonuses, min_deposit, wagering):
    """Main welcome pack tiers (first 3 bonuses)."""
    items = []
    for b in bonuses[:3]:
        # Extract numeric value if possible
        value = b.get('value', '')
        is_percent = '%' in value
        items.append(f'''<div class="bonus-tier">
            <div class="bonus-tier-title">{b["title"]}</div>
            <div class="bonus-tier-amount">
                <span class="bonus-tier-coin"></span>
                <span class="bonus-tier-value">{value}</span>
            </div>
            <div class="bonus-tier-meta">
                <span>Wager <strong>{wagering}</strong></span>
                <span>Min. vklad <strong>{min_deposit} Kč</strong></span>
            </div>
        </div>''')
    return '\n'.join(items)


def build_bonus_pack_alt_html(bonuses, min_deposit, wagering):
    """Alternative bonuses (4th and beyond)."""
    items = []
    for b in bonuses[3:5]:
        value = b.get('value', '')
        items.append(f'''<div class="bonus-tier">
            <div class="bonus-tier-title">{b["title"]}</div>
            <div class="bonus-tier-amount">
                <span class="bonus-tier-coin"></span>
                <span class="bonus-tier-value">{value}</span>
            </div>
            <div class="bonus-tier-meta">
                <span>Detail: <strong>{b.get("detail", "")}</strong></span>
            </div>
        </div>''')
    return '\n'.join(items) if items else '<p class="review-text" style="grid-column:1/-1;color:var(--text-muted);">Žádné alternativní bonusy v současné době.</p>'


def build_bonus_cards_html(bonuses):
    items = []
    for b in bonuses:
        items.append(f'''<div class="bonus-card">
            <div class="bonus-card-title">{b["title"]}</div>
            <div class="bonus-card-value">{b["value"]}</div>
            <div class="bonus-card-detail">{b["detail"]}</div>
        </div>''')
    return '\n'.join(items)


def build_payment_html(methods):
    # Map payment name -> image file in /assets/images/payments/
    img_map = {
        "Visa": "visa.svg",
        "Mastercard": "mastercard.png",
        "Bankovní převod": "bankovni-prevod.svg",
        "Skrill": "skrill.svg",
        "Neteller": "neteller.svg",
        "PaySafeCard": "paysafecard.ico",
        "Apple Pay": "apple-pay.svg",
        "PayPal": "paypal.png",
        "MuchBetter": "muchbetter.ico",
    }
    # Fallback emojis for methods without images
    emoji_map = {
        "Google Pay": "📱", "Hotovost (pobočky)": "💵",
        "Sportka Pay": "🎫", "Maestro": "💳", "Bitcoin": "₿",
        "Ethereum": "⟠", "USDT": "💲", "ecoPayz": "💰",
        "Jeton": "💰", "Trustly": "🏦",
        "Přímý bankovní převod": "🏦",
    }
    items = []
    for m in methods:
        if m in img_map:
            icon_html = f'<img src="/assets/images/payments/{img_map[m]}" alt="{m}" class="grid-item-img">'
        else:
            emoji = emoji_map.get(m, "💳")
            icon_html = f'<span class="grid-item-icon">{emoji}</span>'
        items.append(f'''<div class="grid-item">
            {icon_html}
            <span class="grid-item-name">{m}</span>
        </div>''')
    return '\n'.join(items)


def build_providers_html(providers):
    items = []
    for p in providers:
        items.append(f'''<div class="grid-item">
            <span class="grid-item-icon">🎮</span>
            <span class="grid-item-name">{p}</span>
        </div>''')
    return '\n'.join(items)


def build_advantages_html(advantages):
    items = []
    for a in advantages:
        items.append(f'''<div class="advantage-item">
            <span class="advantage-icon">✓</span>
            <span class="advantage-text">{a}</span>
        </div>''')
    return '\n'.join(items)


def build_review_faq_html(faq_items):
    items = []
    for item in faq_items:
        items.append(f'''<div class="faq-item">
            <div class="faq-q">{item["q"]}</div>
            <div class="faq-a">{item["a"]}</div>
        </div>''')
    return '\n'.join(items)


def build_similar_casinos_html(current_slug, all_casinos):
    items = []
    for c in all_casinos:
        if c['slug'] == current_slug:
            continue
        items.append(f'''<a href="/kasina/{c["slug"]}/" class="related-card">
            <div class="related-card-header">
                <div class="related-card-logo">
                    <img src="/assets/images/casinos/{c["slug"]}.{get_logo_ext(c["slug"])}" alt="{c["name"]}" width="60" height="40">
                </div>
                <div class="related-card-name">{c["name"]}</div>
                <div class="related-card-rating">{stars_html(c["rating"])} {c["rating"]}/5</div>
            </div>
            <div class="related-card-body">
                <div class="related-card-bonus">{c["bonus"]}</div>
                <span class="related-card-btn">Zobrazit recenzi →</span>
            </div>
        </a>''')
    return '\n'.join(items)


def build_pros_html(pros):
    return '\n'.join(f'<li>{p}</li>' for p in pros)


def build_cons_html(cons):
    return '\n'.join(f'<li>{c}</li>' for c in cons)


def build_introduction_extra(casino):
    """Generate additional intro paragraph for word count."""
    r = casino['review']
    return (f"Naši redaktoři otestovali {casino['name']} po dobu několika týdnů – od registrace "
            f"přes vklad, hraní až po výběr. V této recenzi vám představíme všechny aspekty, "
            f"které potřebujete vědět: od bonusové nabídky a výběru her, přes platební metody a rychlost výplat, "
            f"až po kvalitu zákaznické podpory. Zjistíte také, jaké jsou nejdůležitější výhody i případné nevýhody "
            f"této platformy a zda se vám vyplatí zaregistrovat. Hodnocení {casino['rating']}/5 odráží naši celkovou "
            f"spokojenost s tímto operátorem na základě objektivního testování.")


def build_atmosphere(casino):
    r = casino['review']
    return (f"Vizuální design {casino['name']} byl pečlivě navržen, aby poskytl hráčům prémiový "
            f"a moderní zážitek. Platforma kombinuje tmavé tóny s výraznými akcenty, což vytváří atmosféru "
            f"skutečného kamenného kasina v digitální podobě. Navigace je intuitivní – hlavní menu je vždy "
            f"po ruce, vyhledávání her funguje rychle a kategorie jsou logicky uspořádané. Mobilní verze "
            f"si zachovává plnou funkcionalitu desktopu a načítání je svižné i na pomalejších připojeních. "
            f"Celkově lze říci, že {casino['name']} klade velký důraz na uživatelský zážitek a tato investice "
            f"se odráží v plynulém průchodu celou platformou. Hráči, kteří hledají kasino s profesionálním "
            f"designem, budou s {casino['name']} velmi spokojeni.")


def build_payments_extra(casino):
    r = casino['review']
    return (f"Vklady v {casino['name']} jsou ve většině případů zpracovány okamžitě a bez jakýchkoliv poplatků. "
            f"Výběry probíhají v rozmezí {r['withdrawalSpeedDetail']} v závislosti na zvolené platební metodě. "
            f"E-peněženky jako Skrill a Neteller jsou nejrychlejší – výběr je často hotový do několika hodin. "
            f"Bankovní převody mohou trvat 1-3 pracovní dny. Minimální vklad činí {casino['minDeposit']} Kč, "
            f"což je dostupné i pro hráče s menším rozpočtem. Maximální výběr na transakci je {r['withdrawalRange'].split(' – ')[-1] if ' – ' in r['withdrawalRange'] else r['withdrawalRange']}.")


def build_providers_extra(casino):
    return (f"Spolupráce s {casino['review']['providerCount']}+ předními poskytovateli zaručuje, že {casino['name']} "
            f"nabízí jen nejkvalitnější a férové hry. Všechny tituly procházejí pravidelným auditem nezávislých "
            f"organizací, které ověřují férovost RNG (random number generator) a soulad s herními standardy. "
            f"Hráči se tak mohou spolehnout na to, že každá hra má deklarované RTP a výsledky jsou skutečně náhodné. "
            f"Mezi nejoblíbenějšími poskytovateli najdete Pragmatic Play s populárními sloty jako Sweet Bonanza nebo "
            f"Gates of Olympus, NetEnt s legendárními Starburst a Gonzo's Quest, či Evolution Gaming pro live kasino.")


def build_registration_intro(casino):
    return (f"Registrace na {casino['name']} je rychlá a jednoduchá – celý proces zabere obvykle méně než 5 minut. "
            f"Postupujte podle níže uvedených kroků a budete moci začít hrát s plným uvítacím bonusem. "
            f"Nezapomeňte mít připravené doklady totožnosti, které budete potřebovat pro KYC ověření.")


def generate_review_page(casino, template, all_casinos):
    r = casino['review']

    bonus_pack_headline = f"{r['bonusAmount']}"
    if r['freeSpinsCount'] != '—':
        bonus_pack_headline += f" + {r['freeSpinsCount']}"

    html = template
    replacements = {
        '{{casino_name}}': casino['name'],
        '{{casino_slug}}': casino['slug'],
        '{{casino_logo_url}}': f'/assets/images/casinos/{casino["slug"]}.{get_logo_ext(casino["slug"])}',
        '{{meta_description}}': r['metaDescription'],
        '{{rating}}': str(casino['rating']),
        '{{rating_stars}}': stars_html(casino['rating']),
        '{{review_count}}': str(r['reviewCount']),
        '{{bonus_amount}}': r['bonusAmount'],
        '{{free_spins_count}}': r['freeSpinsCount'],
        '{{withdrawal_speed}}': r['withdrawalSpeed'],
        '{{owner}}': r['owner'],
        '{{year_created}}': r['yearCreated'],
        '{{license}}': r['license'],
        '{{min_deposit}}': f"{casino['minDeposit']} Kč",
        '{{withdrawal_range}}': r['withdrawalRange'],
        '{{withdrawal_speed_detail}}': r['withdrawalSpeedDetail'],
        '{{czech_language}}': r['czechLanguage'],
        '{{mobile}}': r['mobile'],
        '{{introduction}}': r['introduction'],
        '{{bonus_intro}}': r['bonusIntro'],
        '{{bonus_cards_html}}': build_bonus_cards_html(r['bonuses']),
        '{{weekly_promo}}': r['weeklyPromo'],
        '{{vip_program}}': r['vipProgram'],
        '{{games_intro}}': r['gamesIntro'],
        '{{game_cats_html}}': build_game_cats_html(),
        '{{games_slots}}': r['gamesSlots'],
        '{{games_table}}': r['gamesTable'],
        '{{games_live}}': r['gamesLive'],
        '{{games_mini}}': r['gamesMini'],
        '{{payments_intro}}': r['paymentsIntro'],
        '{{payment_methods_html}}': build_payment_html(r['paymentMethods']),
        '{{payment_count}}': str(r['paymentCount']),
        '{{providers_intro}}': r['providersIntro'],
        '{{providers_html}}': build_providers_html(r['providers']),
        '{{provider_count}}': str(r['providerCount']),
        '{{advantages_html}}': build_advantages_html(r['advantages']),
        '{{bonus_headline}}': casino['bonus'],
        '{{bonus_url}}': casino['bonusUrl'],
        '{{pros_html}}': build_pros_html(r['pros']),
        '{{cons_html}}': build_cons_html(r['cons']),
        '{{support_text}}': r['supportText'],
        '{{faq_html}}': build_review_faq_html(r['faq']),
        '{{similar_casinos_html}}': build_similar_casinos_html(casino['slug'], all_casinos),
        '{{final_verdict}}': r['finalVerdict'],
        '{{nav_html}}': NAV_HTML,
        '{{footer_html}}': FOOTER_HTML,
        '{{author_box}}': build_author_box(12),
        '{{preview_games_html}}': build_preview_games_html(),
        '{{preview_payments_html}}': build_preview_payments_html(r['paymentMethods']),
        '{{preview_providers_html}}': build_preview_providers_html(r['providers']),
        '{{introduction_extra}}': build_introduction_extra(casino),
        '{{atmosphere}}': build_atmosphere(casino),
        '{{payments_extra}}': build_payments_extra(casino),
        '{{providers_extra}}': build_providers_extra(casino),
        '{{registration_intro}}': build_registration_intro(casino),
        '{{bonus_pack_headline}}': bonus_pack_headline,
        '{{bonus_pack_html}}': build_bonus_pack_html(r['bonuses'], casino['minDeposit'], r.get('wagering', casino.get('wagering', 'x30'))),
        '{{bonus_pack_alt_html}}': build_bonus_pack_alt_html(r['bonuses'], casino['minDeposit'], r.get('wagering', casino.get('wagering', 'x30'))),
    }

    for placeholder, value in replacements.items():
        html = html.replace(placeholder, value)

    return html


# ============================================================
# MAIN
# ============================================================

def main():
    print('🎰 Casino Arena — Generating pages...\n')

    casinos_data = load_json('casinos.json')
    keywords_data = load_json('keywords.json')
    template = load_file('template.html')
    review_template = load_file('casino-avis-template.html')

    casinos = casinos_data['casinos']
    keywords = keywords_data['keywords']

    # Generate keyword pages
    pages_dir = os.path.join(BASE_DIR, 'pages')
    os.makedirs(pages_dir, exist_ok=True)

    kw_count = 0
    for keyword in keywords:
        slug = keyword['slug']
        page_dir = os.path.join(pages_dir, slug)
        os.makedirs(page_dir, exist_ok=True)

        html = generate_keyword_page(keyword, casinos, template, keywords)
        output_path = os.path.join(page_dir, 'index.html')
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)

        kw_count += 1
        print(f'  ✓ /pages/{slug}/index.html')

    # Generate casino review pages
    kasina_dir = os.path.join(BASE_DIR, 'kasina')
    os.makedirs(kasina_dir, exist_ok=True)

    review_count = 0
    for casino in casinos:
        if 'review' not in casino:
            continue

        slug = casino['slug']
        page_dir = os.path.join(kasina_dir, slug)
        os.makedirs(page_dir, exist_ok=True)

        html = generate_review_page(casino, review_template, casinos)
        output_path = os.path.join(page_dir, 'index.html')
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)

        review_count += 1
        print(f'  ★ /kasina/{slug}/index.html')

    print(f'\n✅ Generated {kw_count} keyword pages in pages/')
    print(f'★ Generated {review_count} casino review pages in kasina/')
    print(f'📊 Casinos: {len(casinos)}')
    print(f'🔑 Keywords: {len(keywords)}')


if __name__ == '__main__':
    main()
