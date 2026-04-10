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


# ============================================================
# NAVIGATION HTML (Mega Menu)
# ============================================================
NAV_HTML = '''<nav class="nav">
    <div class="container">
        <a href="/" class="nav-logo"><img src="/assets/images/logo.svg" alt="Casinos Czech" class="nav-logo-img"></a>
        <button class="nav-toggle" aria-label="Menu">☰</button>
        <ul class="nav-menu">
            <li>
                <a href="/kasina/">Kasina <span class="arrow-down">▼</span></a>
                <div class="mega-dropdown">
                    <div class="mega-dropdown-title">Kasina</div>
                    <ul>
                        <li><a href="/nejlepsi-kasina-cz/">Nejlepší kasina</a></li>
                        <li><a href="/nove-kasina-2026/">Nová kasina 2026</a></li>
                        <li><a href="/kasina-ceska-licence/">Česká kasina</a></li>
                        <li><a href="/bezpecna-kasina/">Bezpečná kasina</a></li>
                        <li><a href="/kasino-bez-limitu/">Kasina bez limitu</a></li>
                        <li><a href="/top-10-kasin/">Top 10 kasin</a></li>
                    </ul>
                </div>
            </li>
            <li>
                <a href="/nejlepsi-kasinovy-bonus/">Bonusy <span class="arrow-down">▼</span></a>
                <div class="mega-dropdown">
                    <div class="mega-dropdown-title">Bonusy & Akce</div>
                    <ul>
                        <li><a href="/nejlepsi-kasinovy-bonus/">Nejlepší bonusy</a></li>
                        <li><a href="/casino-bonusy-bez-vkladu/">Bonusy bez vkladu</a></li>
                        <li><a href="/free-spiny-dnes/">Free spiny dnes</a></li>
                        <li><a href="/kasino-free-spiny/">Kasino free spiny</a></li>
                        <li><a href="/kasino-nizka-sazka/">Nízké sázky</a></li>
                    </ul>
                </div>
            </li>
            <li>
                <a href="/casino-vyherni-automaty/">Hry <span class="arrow-down">▼</span></a>
                <div class="mega-dropdown mega-dropdown-wide">
                    <div class="mega-col">
                        <div class="mega-dropdown-title">Populární hry</div>
                        <ul>
                            <li><a href="/automaty-zdarma/">Automaty zdarma</a></li>
                            <li><a href="/casino-vyherni-automaty/">Výherní automaty</a></li>
                            <li><a href="/live-kasino/">Live kasino</a></li>
                            <li><a href="/poker-online/">Poker online</a></li>
                            <li><a href="/sazeni-na-sport/">Sportovní sázky</a></li>
                            <li><a href="/loterie-online/">Loterie online</a></li>
                        </ul>
                    </div>
                    <div class="mega-col">
                        <div class="mega-dropdown-title">Stolní & Mini hry</div>
                        <ul>
                            <li><a href="/rtp-automaty/">Vysoké RTP automaty</a></li>
                            <li><a href="/volatilita-automaty/">Volatilita automatů</a></li>
                            <li><a href="/jackpot-kasino/">Jackpot kasino</a></li>
                            <li><a href="/kasino-pro-zacatecniky/">Pro začátečníky</a></li>
                            <li><a href="/kasino-na-penize/">Kasino na peníze</a></li>
                        </ul>
                    </div>
                </div>
            </li>
            <li>
                <a href="/online-hazard-cz/">Info <span class="arrow-down">▼</span></a>
                <div class="mega-dropdown">
                    <div class="mega-dropdown-title">Průvodce</div>
                    <ul>
                        <li><a href="/legalni-kasina-cz/">Legální kasina v ČR</a></li>
                        <li><a href="/dane-z-vyhry/">Daně z výher</a></li>
                        <li><a href="/sebeomezeni-hazard/">Odpovědné hraní</a></li>
                        <li><a href="/online-hazard-cz/">Online hazard v ČR</a></li>
                    </ul>
                </div>
            </li>
        </ul>
    </div>
</nav>'''


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
        <div class="top-card-logo"><img src="/assets/images/casinos/{casino["slug"]}.svg" alt="{casino["name"]}"></div>
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


def generate_keyword_page(keyword, casinos, template, all_keywords):
    casino_table = build_casino_tops(casinos)
    faq_html = build_faq_html(keyword.get('faq', []))
    related_html = build_related_html(keyword.get('related', []), all_keywords)

    html = template
    html = html.replace('{{slug}}', keyword['slug'])
    html = html.replace('{{title}}', keyword['title'])
    html = html.replace('{{h1}}', keyword['h1'])
    html = html.replace('{{description}}', keyword['description'])
    html = html.replace('{{intro}}', keyword['intro'])
    html = html.replace('{{casino_cards}}', casino_table)
    html = html.replace('{{seo_content}}', keyword['seo_content'])
    html = html.replace('{{faq_html}}', faq_html)
    html = html.replace('{{related_html}}', related_html)
    html = html.replace('{{nav_html}}', NAV_HTML)
    html = html.replace('{{footer_html}}', FOOTER_HTML)

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
    icons = {
        "Visa": "💳", "Mastercard": "💳", "Bankovní převod": "🏦",
        "Skrill": "💰", "Neteller": "💰", "PaySafeCard": "🎫",
        "Apple Pay": "🍎", "Google Pay": "📱", "Hotovost (pobočky)": "💵",
        "Sportka Pay": "🎫", "Maestro": "💳", "Bitcoin": "₿",
        "Ethereum": "⟠", "USDT": "💲", "PayPal": "💳",
        "MuchBetter": "📱", "ecoPayz": "💰", "Jeton": "💰",
        "Trustly": "🏦", "Přímý bankovní převod": "🏦",
    }
    items = []
    for m in methods:
        icon = icons.get(m, "💳")
        items.append(f'''<div class="grid-item">
            <span class="grid-item-icon">{icon}</span>
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
                    <img src="/assets/images/casinos/{c["slug"]}.svg" alt="{c["name"]}" width="60" height="40">
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


def generate_review_page(casino, template, all_casinos):
    r = casino['review']

    html = template
    replacements = {
        '{{casino_name}}': casino['name'],
        '{{casino_slug}}': casino['slug'],
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
