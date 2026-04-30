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
    🎰 Smash Casino: 300% bonus 15 000 Kč + 250 FS — <a href="https://m-traff.net/HYcs2BV5?sub_id_1=smash" target="_blank" rel="nofollow noopener">Získat →</a>
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
    <a href="/autori/martin-novak/" class="author-avatar"><img src="/assets/images/author-mn.jpg" alt="Martin Novák"></a>
    <div class="author-info">
        <div class="author-name"><a href="/autori/martin-novak/">Martin Novák</a> <span>— Expert iGaming</span></div>
        <div class="author-meta">Aktualizováno {{date}} · {{read_time}} min čtení</div>
    </div>
    <div class="author-socials-mini">
        <a href="/autori/martin-novak/" title="Profil autora"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/></svg></a>
        <a href="/autori/martin-novak/" title="LinkedIn"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 0 1-2.063-2.065 2.063 2.063 0 1 1 2.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg></a>
        <a href="/autori/martin-novak/" title="X"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231 5.45-6.231Zm-1.161 17.52h1.833L7.084 4.126H5.117l11.966 15.644Z"/></svg></a>
    </div>
</div>'''


# ============================================================
# FOOTER HTML
# ============================================================
FOOTER_HTML = '''<footer class="footer">
    <div class="footer-inner">
        <div class="footer-grid">
            <div class="footer-col">
                <h4>Kasina</h4>
                <ul>
                    <li><a href="/nejlepsi-kasina-cz/">Nejlepší online kasina</a></li>
                    <li><a href="/nove-kasina-2026/">Nová kasina 2026</a></li>
                    <li><a href="/mobilni-kasino/">Mobilní kasina</a></li>
                    <li><a href="/live-kasino/">Live kasino</a></li>
                    <li><a href="/kasino-bez-limitu/">Kasina bez limitu</a></li>
                    <li><a href="/kasina-ceska-licence/">Kasina s českou licencí</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h4>Bonusy</h4>
                <ul>
                    <li><a href="/nejlepsi-kasinovy-bonus/">Uvítací bonusy</a></li>
                    <li><a href="/kasino-nizka-sazka/">Bonusy bez wager</a></li>
                    <li><a href="/free-spiny-dnes/">Free spiny</a></li>
                    <li><a href="/casino-bonusy-bez-vkladu/">Bonusy bez vkladu</a></li>
                    <li><a href="/kasino-free-spiny/">Promo kódy kasin</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h4>Hry kasina</h4>
                <ul>
                    <li><a href="/automaty-zdarma/">Výherní automaty</a></li>
                    <li><a href="/casino-vyherni-automaty/">Mini-hry kasina</a></li>
                    <li><a href="/jackpot-kasino/">Jackpot kasino</a></li>
                    <li><a href="/poker-online/">Poker online</a></li>
                    <li><a href="/sazeni-na-sport/">Sportovní sázky</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h4>Platby</h4>
                <ul>
                    <li><a href="/kasino-bez-limitu/">Okamžité výběry</a></li>
                    <li><a href="/kasino-nizka-sazka/">Vklad od 50 Kč</a></li>
                    <li><a href="#">Kasina PaySafeCard</a></li>
                    <li><a href="#">Kasina Apple Pay</a></li>
                    <li><a href="#">Kasina Bitcoin</a></li>
                    <li><a href="#">Kasina Skrill</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h4>O nás</h4>
                <ul>
                    <li><a href="/autori/martin-novak/">Náš tým</a></li>
                    <li><a href="/legalni-kasina-cz/">Právní podmínky</a></li>
                    <li><a href="/plan-stranek/">Plán stránek</a></li>
                    <li><a href="mailto:contact@casinos-czech.cz">Kontakt</a></li>
                    <li><a href="/sebeomezeni-hazard/">Odpovědné hraní</a></li>
                </ul>
            </div>
            <div class="footer-col footer-brand">
                <img src="/assets/images/logo.svg" alt="Casinos Czech">
                <p>Casinos Czech je 100% nezávislý a poskytuje objektivní hodnocení pro české hráče na základě reálných dat. Účtujeme si poplatky za reference a používáme partnerské odkazy, což znamená, že obdržíme provizi, pokud kliknete a vložíte u jedné ze značek uvedených na našem webu.</p>
                <p><strong>18+ • Hraní je rizikové: dluhy, izolace, závislost.</strong> Pro pomoc volejte <a href="tel:222514040">222 514 040</a> (linka neúčtovaná).</p>
                <div class="footer-socials">
                    <a href="#" aria-label="Facebook"><svg viewBox="0 0 24 24"><path d="M9.198 21.5h4v-8.01h3.604l.396-3.98h-4V7.5a1 1 0 0 1 1-1h3v-4h-3a5 5 0 0 0-5 5v2.01h-2l-.396 3.98h2.396v8.01Z"/></svg></a>
                    <a href="#" aria-label="X"><svg viewBox="0 0 24 24"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231 5.45-6.231Zm-1.161 17.52h1.833L7.084 4.126H5.117l11.966 15.644Z"/></svg></a>
                    <a href="#" aria-label="Instagram"><svg viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 1 0 0 12.324 6.162 6.162 0 0 0 0-12.324zM12 16a4 4 0 1 1 0-8 4 4 0 0 1 0 8zm6.406-11.845a1.44 1.44 0 1 0 0 2.881 1.44 1.44 0 0 0 0-2.881z"/></svg></a>
                    <a href="#" aria-label="YouTube"><svg viewBox="0 0 24 24"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg></a>
                    <a href="#" aria-label="LinkedIn"><svg viewBox="0 0 24 24"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 0 1-2.063-2.065 2.063 2.063 0 1 1 2.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg></a>
                </div>
            </div>
        </div>

        <div class="footer-trust">
            <div class="footer-trust-item"><span class="badge-18">18+</span> Pouze pro dospělé</div>
            <div class="footer-trust-item">📞 222 514 040 (CLVH)</div>
            <div class="footer-trust-item">🛡️ AddictAide</div>
            <div class="footer-trust-item"><span class="stars">★★★★★</span> Trustpilot</div>
            <div class="footer-trust-item">✅ GPWA Approved</div>
        </div>

        <div class="footer-bottom">
            <div><span class="dmca">DMCA</span> Protected · © 2026 casinos-czech.cz · Všechna práva vyhrazena</div>
            <div>Hraní hazardních her může být návykové · 18+</div>
        </div>
    </div>
</footer>'''


# ============================================================
# KEYWORD PAGE GENERATION
# ============================================================

def slugify(s):
    """Lowercase + remove accents + replace spaces with hyphens."""
    import unicodedata
    s = unicodedata.normalize('NFD', s).encode('ascii', 'ignore').decode('ascii')
    return s.lower().replace(' ', '-').replace("'", '').replace('.', '')


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

    # Use explicit filters from casinos.json (computed by update_filters.py)
    f = casino.get('filters', {})
    payments_slug = ','.join(f.get('payments', []))
    providers_slug = ','.join(f.get('providers', []))
    license_slug_val = f.get('license', '')
    no_deposit = 'true' if f.get('hasNoDeposit') else 'false'
    has_app = 'true' if f.get('hasApp') else 'false'
    has_vip = 'true' if f.get('hasVip') else 'false'
    has_sport = 'true' if f.get('hasSport') else 'false'
    has_esport = 'true' if f.get('hasEsport') else 'false'
    has_crypto = 'true' if f.get('hasCrypto') else 'false'
    has_cashback = 'true' if f.get('hasCashback') else 'false'
    speed_bucket = f.get('speed', '24h')
    wager_num = str(f.get('wagering', 0))

    import re
    bonus_num_match = re.search(r'(\d+[\s\d]*)', bonus_amount.replace(' ', ''))
    bonus_num = bonus_num_match.group(1).replace(' ', '') if bonus_num_match else '0'

    # Build details panel content
    license_str = review.get('license', 'N/A')
    year = review.get('yearCreated', 'N/A')
    provider_count = review.get('providerCount', 0)
    payment_count = review.get('paymentCount', 0)
    withdrawal_speed_detail = review.get('withdrawalSpeedDetail', speed)
    review_count = review.get('reviewCount', 0)
    intro_short = review.get('introduction', '')[:200] + '...' if review.get('introduction') else ''

    details_features = features_list[:4] if features_list else []
    details_features_html = ''.join(f'<div class="td-advantage"><span class="td-check">✅</span> {f}</div>' for f in details_features)

    return f'''<div class="top-card"
        data-brand="{casino['slug']}"
        data-rating="{casino['rating']}"
        data-min-deposit="{casino['minDeposit']}"
        data-free-spins="{casino['freeSpins']}"
        data-bonus-num="{bonus_num}"
        data-wagering="{wager_num}"
        data-speed="{speed_bucket}"
        data-payments="{payments_slug}"
        data-providers="{providers_slug}"
        data-license="{license_slug_val}"
        data-no-deposit="{no_deposit}"
        data-app="{has_app}"
        data-vip="{has_vip}"
        data-sport="{has_sport}"
        data-esport="{has_esport}"
        data-crypto="{has_crypto}"
        data-cashback="{has_cashback}">
    <div class="top-card-main">
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
    </div>
    <div class="top-card-details">
        <div class="td-grid">
            <div class="td-col-advantages">
                {details_features_html}
            </div>
            <div class="td-stat">
                <div class="td-stat-label">Hodnocení hráčů <span class="td-info">i</span></div>
                <div class="td-stat-value">{casino['rating']}/5</div>
                <div class="td-stat-sub">{review_count} hodnocení</div>
            </div>
            <div class="td-stat">
                <div class="td-stat-label">Měsíční max. výběr <span class="td-info">i</span></div>
                <div class="td-stat-value">{review.get('withdrawalRange', 'N/A').split('–')[-1].strip()}</div>
            </div>
            <div class="td-stat">
                <div class="td-stat-label">Wagering</div>
                <div class="td-stat-value">x{wager_num}</div>
                <div class="td-stat-sub">Min. vklad: {casino['minDeposit']} Kč</div>
            </div>
            <div class="td-stat">
                <div class="td-stat-label">Počet her</div>
                <div class="td-stat-value">{provider_count * 50}+</div>
                <div class="td-stat-sub">{provider_count} poskytovatelů</div>
            </div>
            <div class="td-stat">
                <div class="td-stat-label">Rychlost výběru <span class="td-info">i</span></div>
                <div class="td-stat-value">{withdrawal_speed_detail}</div>
            </div>
            <div class="td-stat">
                <div class="td-stat-label">Licence</div>
                <div class="td-stat-value">{license_str}</div>
                <div class="td-stat-sub">Rok založení: {year}</div>
            </div>
        </div>
        <div class="td-description">
            {intro_short}
        </div>
        <a href="/kasina/{casino['slug']}/" class="td-review-link">Recenze {casino['name']} ›</a>
    </div>
    <button class="top-card-toggle" onclick="this.closest('.top-card').classList.toggle('open'); this.querySelector('.toggle-text-show').classList.toggle('hidden'); this.querySelector('.toggle-text-hide').classList.toggle('hidden');">
        <span class="toggle-text-show">Zobrazit detaily</span>
        <span class="toggle-text-hide hidden">Skrýt detaily</span>
        <svg viewBox="0 0 24 24" fill="currentColor" class="toggle-arrow"><path d="M7 10l5 5 5-5z"/></svg>
    </button>
</div>'''


FILTER_MODAL_HTML = '''<div class="filter-modal-overlay" id="filterOverlay" onclick="closeFilterModal()"></div>
<div class="filter-modal" id="filterModal">
    <div class="filter-modal-header">
        <button class="filter-modal-close" onclick="closeFilterModal()">✕</button>
        <span class="filter-modal-title">Filtry kasin</span>
    </div>
    <div class="filter-modal-body">
        <div class="filter-group">
            <div class="filter-group-label">Platba:</div>
            <select class="filter-select" data-filter="payment">
                <option value="">Platební metoda</option>
                <option value="visa">Visa</option>
                <option value="mastercard">Mastercard</option>
                <option value="paysafecard">PaySafeCard</option>
                <option value="bitcoin">Bitcoin</option>
                <option value="apple-pay">Apple Pay</option>
                <option value="skrill">Skrill</option>
                <option value="neteller">Neteller</option>
                <option value="paypal">PayPal</option>
            </select>
            <select class="filter-select" data-filter="speed">
                <option value="">Rychlost výběru</option>
                <option value="instant">Okamžitý</option>
                <option value="12h">Do 12 hodin</option>
                <option value="24h">Do 24 hodin</option>
                <option value="48h">Do 48 hodin</option>
            </select>
            <select class="filter-select" data-filter="min-deposit">
                <option value="">Minimální vklad</option>
                <option value="50">Od 50 Kč</option>
                <option value="100">Od 100 Kč</option>
                <option value="200">Od 200 Kč</option>
                <option value="500">Od 500 Kč</option>
            </select>
        </div>
        <div class="filter-group">
            <div class="filter-group-label">Bonusy:</div>
            <div class="filter-checks">
                <label class="filter-check"><input type="checkbox" data-filter="free-spins"> Free Spiny</label>
                <label class="filter-check"><input type="checkbox" data-filter="no-deposit"> Bez vkladu</label>
                <label class="filter-check"><input type="checkbox" data-filter="cashback"> Cashback</label>
            </div>
            <select class="filter-select" data-filter="fs-count">
                <option value="">Počet free spinů</option>
                <option value="50">Min. 50 FS</option>
                <option value="100">Min. 100 FS</option>
                <option value="200">Min. 200 FS</option>
            </select>
        </div>
        <div class="filter-group">
            <div class="filter-group-label">Výhody:</div>
            <div class="filter-checks">
                <label class="filter-check"><input type="checkbox" data-filter="app"> Mobilní aplikace 📱</label>
                <label class="filter-check"><input type="checkbox" data-filter="vip"> VIP klub</label>
                <label class="filter-check"><input type="checkbox" data-filter="sport"> Sportovní sázky</label>
                <label class="filter-check"><input type="checkbox" data-filter="esport"> eSport</label>
                <label class="filter-check"><input type="checkbox" data-filter="crypto"> Krypto platby</label>
            </div>
        </div>
        <div class="filter-group">
            <div class="filter-group-label">Licence:</div>
            <select class="filter-select" data-filter="license">
                <option value="">Všechny licence</option>
                <option value="mf-cr">Česká licence (MF ČR)</option>
                <option value="mga">MGA (Malta)</option>
                <option value="ukgc">UKGC (UK)</option>
                <option value="curacao">Curaçao</option>
            </select>
        </div>
        <div class="filter-group">
            <div class="filter-group-label">Poskytovatel her:</div>
            <select class="filter-select" data-filter="provider">
                <option value="">Všichni poskytovatelé</option>
                <option value="pragmatic-play">Pragmatic Play</option>
                <option value="netent">NetEnt</option>
                <option value="playn-go">Play'n GO</option>
                <option value="evolution">Evolution</option>
                <option value="microgaming">Microgaming</option>
                <option value="novomatic">Novomatic</option>
                <option value="synot-games">Synot Games</option>
                <option value="yggdrasil">Yggdrasil</option>
                <option value="red-tiger">Red Tiger</option>
                <option value="hacksaw-gaming">Hacksaw Gaming</option>
                <option value="push-gaming">Push Gaming</option>
                <option value="big-time-gaming">Big Time Gaming</option>
                <option value="quickspin">Quickspin</option>
                <option value="thunderkick">Thunderkick</option>
                <option value="elk-studios">ELK Studios</option>
                <option value="spribe">Spribe</option>
                <option value="bgaming">BGaming</option>
                <option value="wazdan">Wazdan</option>
                <option value="relax-gaming">Relax Gaming</option>
            </select>
        </div>
        <div class="filter-group">
            <div class="filter-group-label">Značka kasina:</div>
            <select class="filter-select" data-filter="brand">
                <option value="">Všechny značky</option>
                <option value="smash">Smash Casino</option>
                <option value="29black">29Black</option>
                <option value="goldzino">Goldzino</option>
                <option value="playjonny">PlayJonny</option>
                <option value="roulettino">Roulettino</option>
                <option value="synot-tip">Synot Tip</option>
                <option value="fortuna">Fortuna</option>
                <option value="tipsport">Tipsport</option>
                <option value="chance">Chance</option>
                <option value="sazka">Sazka</option>
                <option value="bet365">Bet365</option>
                <option value="888-casino">888 Casino</option>
                <option value="pinnacle">Pinnacle</option>
                <option value="betano">Betano</option>
                <option value="forbes-casino">Forbes Casino</option>
            </select>
        </div>
    </div>
    <div class="filter-modal-footer">
        <button class="filter-clear" onclick="clearFilters()">Vymazat vše</button>
        <button class="filter-apply" onclick="applyFilters()">Použít</button>
    </div>
</div>'''


FILTER_BAR_HTML = '''<div class="filter-bar">
    <div class="sort-dropdown">
        <button class="filter-sort" id="sortToggle" onclick="toggleSort(event)">
            <svg viewBox="0 0 24 24" fill="currentColor"><path d="M3 18h6v-2H3v2zM3 6v2h18V6H3zm0 7h12v-2H3v2z"/></svg>
            <span id="sortLabel">Relevance</span>
            <svg viewBox="0 0 24 24" fill="currentColor"><path d="M7 10l5 5 5-5z"/></svg>
        </button>
        <div class="sort-menu" id="sortMenu">
            <button class="sort-option active" data-sort="relevance">⭐ Relevance</button>
            <button class="sort-option" data-sort="rating">🏆 Nejlepší hodnocení</button>
            <button class="sort-option" data-sort="bonus">💰 Nejvyšší bonus</button>
            <button class="sort-option" data-sort="fs">🎰 Nejvíce free spinů</button>
            <button class="sort-option" data-sort="deposit">💵 Nejnižší vklad</button>
            <button class="sort-option" data-sort="speed">⚡ Nejrychlejší výběr</button>
            <button class="sort-option" data-sort="wagering">📊 Nejnižší wagering</button>
        </div>
    </div>
    <button class="filter-btn" onclick="openFilterModal()">
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M3 17v2h6v-2H3zM3 5v2h10V5H3zm10 16v-2h8v-2h-8v-2h-2v6h2zM7 9v2H3v2h4v2h2V9H7zm14 4v-2H11v2h10zm-6-4h2V7h4V5h-4V3h-2v6z"/></svg>
        Filtry
    </button>
</div>'''


AFFILIATE_PRIORITY = [
    # New high-bonus affiliates first
    'betista',          # +370% — top tier
    'billionairespin',  # +255% NO wager
    'needforslots',     # 250 FS slot specialist
    # Existing affiliates
    'smash',
    '29black',
    'goldzino',
    'playjonny',
    'roulettino',
    # Remaining new affiliates alphabetically
    'bdmbet',
    'betify',
    'betriot',
    'cashed',
    'casinozer',
    'mafia-casino',
    'rabona-casino',
    'spinbara',
    'spinsy',
]


def sort_casinos_with_priority(casinos):
    """Put affiliate casinos (m-traff) first, then sort rest by rating descending."""
    priority = [c for slug in AFFILIATE_PRIORITY for c in casinos if c['slug'] == slug]
    others = sorted([c for c in casinos if c['slug'] not in AFFILIATE_PRIORITY],
                    key=lambda x: x.get('rating', 0), reverse=True)
    return priority + others


CASINOS_PER_PAGE = 8


def build_pagination(total_pages, current=1):
    """Build pagination buttons."""
    if total_pages <= 1:
        return ''
    items = []
    # Prev arrow
    items.append(f'<button class="pagination-btn" data-page="prev" {"aria-disabled=true" if current==1 else ""} title="Předchozí"><svg viewBox="0 0 24 24"><path d="M15.41 16.59L10.83 12l4.58-4.59L14 6l-6 6 6 6 1.41-1.41z"/></svg></button>')
    # Page numbers (max 6 visible at a time)
    for i in range(1, total_pages + 1):
        active = ' active' if i == current else ''
        items.append(f'<button class="pagination-btn{active}" data-page="{i}">{i}</button>')
    # Next arrow
    items.append(f'<button class="pagination-btn" data-page="next" {"aria-disabled=true" if current==total_pages else ""} title="Další"><svg viewBox="0 0 24 24"><path d="M8.59 16.59L13.17 12 8.59 7.41 10 6l6 6-6 6-1.41-1.41z"/></svg></button>')
    return f'<div class="pagination-wrap">{"".join(items)}</div>'


def build_thematic_internal_links(slug, casinos):
    """Build ONE thematic internal-links section based on the page slug."""
    s = (slug or '').lower()

    # Helper to render a list of casino links
    def cas_links(items):
        return ''.join(f'<a href="/kasina/{c["slug"]}/">{c["name"]}</a>' for c in items)

    # Helper for a list of (label, url) tuples
    def kw_links(items):
        return ''.join(f'<a href="{u}">{l}</a>' for l, u in items)

    sorted_by_rating = sorted(casinos, key=lambda c: c.get('rating', 0), reverse=True)
    affiliates = [c for c in casinos if c['slug'] in AFFILIATE_PRIORITY]
    cz_licensed = [c for c in casinos if c.get('review', {}).get('license', '').lower().startswith('mf')]
    international = [c for c in casinos if not c.get('review', {}).get('license', '').lower().startswith('mf')]
    with_fs = [c for c in casinos if c.get('freeSpins', 0) > 0]
    no_deposit = [c for c in casinos if 'bez vkladu' in c.get('bonus', '').lower()]
    new_2024_plus = [c for c in casinos if int(c.get('review', {}).get('yearCreated', '2010')) >= 2023]

    # NEJLEPŠÍ / TOP / ONLINE-KASINO
    if 'nejlepsi-kasina' in s or 'top-10-kasin' in s or 'online-kasino' in s:
        return f'<section class="internal-links-section"><h3>🏆 Všechna nejlepší online kasina v ČR</h3><div class="internal-links">{cas_links(sorted_by_rating)}</div></section>'

    # NOVÁ KASINA
    if 'nove-kasina' in s or 'nova-kasina' in s:
        listing = new_2024_plus + [c for c in sorted_by_rating if c not in new_2024_plus][:8]
        return f'<section class="internal-links-section"><h3>🆕 Nová kasina 2024-2026</h3><div class="internal-links">{cas_links(listing)}</div></section>'

    # BEZPEČNÁ / LEGÁLNÍ / ČESKÁ LICENCE
    if 'bezpecn' in s or 'legaln' in s or 'ceska-licence' in s or 'kasina-ceska' in s:
        return f'<section class="internal-links-section"><h3>🛡️ Kasina s českou licencí MF ČR</h3><div class="internal-links">{cas_links(cz_licensed)}</div></section>'

    # KASINO BEZ LIMITU
    if 'bez-limitu' in s:
        listing = [c for c in casinos if c['slug'] in ['pinnacle', '29black', 'smash', 'goldzino', 'bet365', 'mostbet', 'playjonny']]
        return f'<section class="internal-links-section"><h3>♾️ Kasina bez limitu výher a sázek</h3><div class="internal-links">{cas_links(listing)}</div></section>'

    # FREE SPINY (všechny varianty)
    if 'free-spiny' in s or 'free-spins' in s or 'freespiny' in s:
        return f'<section class="internal-links-section"><h3>🎰 Kasina s nejlepšími free spiny</h3><div class="internal-links">{cas_links(with_fs)}</div></section>'

    # BEZ VKLADU
    if 'bez-vkladu' in s:
        listing = no_deposit if no_deposit else sorted_by_rating[:12]
        return f'<section class="internal-links-section"><h3>💰 Kasina nabízející bonus bez vkladu</h3><div class="internal-links">{cas_links(listing)}</div></section>'

    # BONUSY (general)
    if 'bonus' in s or 'kasinovy-bonus' in s:
        return f'<section class="internal-links-section"><h3>🎁 Kasina s nejštědřejšími bonusy</h3><div class="internal-links">{cas_links(sorted_by_rating[:18])}</div></section>'

    # NÍZKÁ SÁZKA
    if 'nizka-sazka' in s or 'nizke' in s:
        listing = [c for c in casinos if c.get('minDeposit', 999) <= 100]
        return f'<section class="internal-links-section"><h3>💵 Kasina s nízkými sázkami a vklady</h3><div class="internal-links">{cas_links(listing)}</div></section>'

    # LIVE KASINO
    if 'live-kasino' in s or 'live-casino' in s:
        items = [
            ('Synot Tip Live', '/kasina/synot-tip/'), ('Fortuna Live', '/kasina/fortuna/'),
            ('Tipsport Live', '/kasina/tipsport/'), ('Bet365 Live', '/kasina/bet365/'),
            ('888 Live', '/kasina/888-casino/'), ('Smash Live', '/kasina/smash/'),
            ('29Black Live', '/kasina/29black/'), ('Roulettino', '/kasina/roulettino/'),
            ('Goldzino Live', '/kasina/goldzino/'), ('PlayJonny Live', '/kasina/playjonny/'),
            ('Live ruleta', '/kasina/roulettino/'), ('Live blackjack', '/kasina/synot-tip/'),
            ('Live baccarat', '/kasina/synot-tip/'), ('Live poker', '/poker-online/'),
            ('Game shows', '/live-kasino/'), ('Crazy Time', '/kasina/synot-tip/'),
            ('Monopoly Live', '/kasina/synot-tip/'), ('Dream Catcher', '/kasina/synot-tip/'),
        ]
        return f'<section class="internal-links-section"><h3>🎥 Kasina s nejlepším live kasinem</h3><div class="internal-links">{kw_links(items)}</div></section>'

    # AUTOMATY / SLOTY
    if 'automat' in s or 'slot' in s or 'vyherni' in s:
        items = [
            ('Aviator', '/hry/aviator/'), ('Plinko', '/hry/plinko/'), ('Mines', '/hry/mines/'),
            ('Chicken Road', '/hry/chicken-road/'), ('Tower Rush', '/hry/tower-rush/'),
            ('Spaceman', '/hry/spaceman/'), ('JetX', '/hry/jetx/'), ('Dice', '/hry/dice/'),
            ('Limbo', '/hry/limbo/'), ('Hi-Lo', '/hry/hilo/'),
            ('Výherní automaty', '/casino-vyherni-automaty/'), ('Automaty zdarma', '/automaty-zdarma/'),
            ('Vysoké RTP', '/vysoke-rtp-kasino/'), ('Volatilita', '/volatilita-automaty/'),
            ('RTP automatů', '/rtp-automaty/'), ('Jackpot', '/jackpot-kasino/'),
            ('Synot Tip sloty', '/kasina/synot-tip/'), ('Tipsport sloty', '/kasina/tipsport/'),
        ]
        return f'<section class="internal-links-section"><h3>🎰 Populární výherní automaty a poskytovatelé</h3><div class="internal-links">{kw_links(items)}</div></section>'

    # JACKPOT
    if 'jackpot' in s:
        return f'<section class="internal-links-section"><h3>💎 Kasina s nejvyššími jackpoty</h3><div class="internal-links">{cas_links(sorted_by_rating[:18])}</div></section>'

    # POKER
    if 'poker' in s:
        items = [
            ('Bet365 Poker', '/kasina/bet365/'), ('888 Casino Poker', '/kasina/888-casino/'),
            ('Synot Tip Poker', '/kasina/synot-tip/'), ('Fortuna Poker', '/kasina/fortuna/'),
            ('Tipsport Poker', '/kasina/tipsport/'), ('Pinnacle Poker', '/kasina/pinnacle/'),
            ('Texas Hold\'em', '/poker-online/'), ('Video poker', '/poker-online/'),
            ('Live poker', '/live-kasino/'), ('Cash games', '/poker-online/'),
            ('Turnaje poker', '/poker-online/'), ('Sit & Go', '/poker-online/'),
        ]
        return f'<section class="internal-links-section"><h3>🃏 Online poker v českých kasinech</h3><div class="internal-links">{kw_links(items)}</div></section>'

    # SPORTOVNÍ SÁZKY
    if 'sport' in s or 'sazen' in s:
        items = [
            ('Tipsport sázky', '/kasina/tipsport/'), ('Fortuna sázky', '/kasina/fortuna/'),
            ('Synot Tip sázky', '/kasina/synot-tip/'), ('Chance sázky', '/kasina/chance/'),
            ('Sazka sázky', '/kasina/sazka/'), ('Bet365 sázky', '/kasina/bet365/'),
            ('Betano sázky', '/kasina/betano/'), ('LuckyBet sázky', '/kasina/luckybet/'),
            ('DOXXbet sázky', '/kasina/doxxbet/'), ('Pinnacle sázky', '/kasina/pinnacle/'),
            ('Fotbalové sázky', '/sazeni-na-sport/'), ('Hokejové sázky', '/sazeni-na-sport/'),
            ('Tenis', '/sazeni-na-sport/'), ('NHL', '/sazeni-na-sport/'),
            ('NBA', '/sazeni-na-sport/'), ('eSport', '/sazeni-na-sport/'),
        ]
        return f'<section class="internal-links-section"><h3>⚽ Sportovní sázky v ČR</h3><div class="internal-links">{kw_links(items)}</div></section>'

    # MOBILNÍ
    if 'mobiln' in s:
        listing = [c for c in casinos if 'aplikac' in str(c.get('review', {}).get('mobile', '')).lower() or 'app' in str(c.get('review', {}).get('mobile', '')).lower() or sorted_by_rating.index(c) < 16] if False else sorted_by_rating[:18]
        return f'<section class="internal-links-section"><h3>📱 Nejlepší mobilní kasina a aplikace</h3><div class="internal-links">{cas_links(listing)}</div></section>'

    # PRO ZAČÁTEČNÍKY
    if 'zacatecnik' in s or 'pro-zacatecn' in s:
        items = [
            ('Synot Tip', '/kasina/synot-tip/'), ('Fortuna', '/kasina/fortuna/'),
            ('Tipsport', '/kasina/tipsport/'), ('Sazka', '/kasina/sazka/'),
            ('Pravidla blackjacku', '/casino-vyherni-automaty/'),
            ('Pravidla rulety', '/live-kasino/'), ('Pravidla pokeru', '/poker-online/'),
            ('Co je RTP', '/rtp-automaty/'), ('Co je volatilita', '/volatilita-automaty/'),
            ('Bonus bez vkladu', '/casino-bonusy-bez-vkladu/'),
            ('Wagering podmínky', '/nejlepsi-kasinovy-bonus/'),
            ('Free spiny', '/free-spiny-dnes/'), ('Bezpečná kasina', '/bezpecna-kasina/'),
            ('Odpovědné hraní', '/sebeomezeni-hazard/'),
        ]
        return f'<section class="internal-links-section"><h3>📚 Průvodce pro nové hráče</h3><div class="internal-links">{kw_links(items)}</div></section>'

    # KRYPTO / BITCOIN
    if 'crypto' in s or 'bitcoin' in s:
        items = [
            ('Smash Casino', '/kasina/smash/'), ('29Black', '/kasina/29black/'),
            ('Goldzino', '/kasina/goldzino/'), ('PlayJonny', '/kasina/playjonny/'),
            ('Pinnacle Crypto', '/kasina/pinnacle/'), ('Mostbet', '/kasina/mostbet/'),
            ('Bitcoin BTC', '/kasino-bez-limitu/'), ('Ethereum ETH', '/kasino-bez-limitu/'),
            ('USDT Tether', '/kasino-bez-limitu/'), ('Litecoin LTC', '/kasino-bez-limitu/'),
            ('Solana SOL', '/kasino-bez-limitu/'), ('Dogecoin DOGE', '/kasino-bez-limitu/'),
        ]
        return f'<section class="internal-links-section"><h3>₿ Kasina přijímající kryptoměny</h3><div class="internal-links">{kw_links(items)}</div></section>'

    # VYSOKÉ RTP
    if 'rtp' in s or 'volatilita' in s:
        return f'<section class="internal-links-section"><h3>📊 Kasina s nejvyšším RTP</h3><div class="internal-links">{cas_links(sorted_by_rating[:18])}</div></section>'

    # DAŇE / HAZARD CZ
    if 'hazard' in s or 'dane' in s:
        items = [
            ('Daně z výher', '/dane-z-vyhry/'), ('Online hazard ČR', '/online-hazard-cz/'),
            ('Legální kasina', '/legalni-kasina-cz/'), ('Česká licence', '/kasina-ceska-licence/'),
            ('Odpovědné hraní', '/sebeomezeni-hazard/'),
            ('Synot Tip', '/kasina/synot-tip/'), ('Fortuna', '/kasina/fortuna/'),
            ('Tipsport', '/kasina/tipsport/'), ('Chance', '/kasina/chance/'),
            ('Sazka', '/kasina/sazka/'), ('Forbes Casino', '/kasina/forbes-casino/'),
            ('Betano', '/kasina/betano/'), ('MerkurXtip', '/kasina/merkurxtip/'),
        ]
        return f'<section class="internal-links-section"><h3>⚖️ Legislativa a regulace hazardu v ČR</h3><div class="internal-links">{kw_links(items)}</div></section>'

    # SEBEOMEZENÍ
    if 'sebeomezeni' in s:
        items = [
            ('CLVH.cz', 'https://www.clvh.cz'), ('Linka pomoci 222 514 040', 'tel:222514040'),
            ('Bezpečná kasina', '/bezpecna-kasina/'), ('Legální kasina', '/legalni-kasina-cz/'),
            ('Daně z výher', '/dane-z-vyhry/'), ('Pro začátečníky', '/kasino-pro-zacatecniky/'),
        ]
        return f'<section class="internal-links-section"><h3>🛡️ Odpovědné hraní a pomoc</h3><div class="internal-links">{kw_links(items)}</div></section>'

    # KASINO-SPECIFIC PAGES (synot-tip-free-spins, fortuna-kasino, bet365-kasino, tipsport-free-spiny)
    for cas_slug in ['synot-tip', 'fortuna', 'bet365', 'tipsport']:
        if cas_slug in s:
            cas = next((c for c in casinos if c['slug'] == cas_slug), None)
            if cas:
                items = [
                    (f'Recenze {cas["name"]}', f'/kasina/{cas_slug}/'),
                    (f'{cas["name"]} bonus', '/nejlepsi-kasinovy-bonus/'),
                    (f'{cas["name"]} free spiny', '/free-spiny-dnes/'),
                    ('Nejlepší kasina', '/nejlepsi-kasina-cz/'),
                    ('Bezpečná kasina', '/bezpecna-kasina/'),
                    ('Live kasino', '/live-kasino/'),
                    ('Mobilní kasino', '/mobilni-kasino/'),
                    ('Aviator', '/hry/aviator/'),
                    ('Plinko', '/hry/plinko/'),
                ]
                return f'<section class="internal-links-section"><h3>🎰 Související odkazy {cas["name"]}</h3><div class="internal-links">{kw_links(items)}</div></section>'

    # LOTERIE
    if 'loterie' in s:
        items = [
            ('Sazka', '/kasina/sazka/'), ('Synot Tip Lotto', '/kasina/synot-tip/'),
            ('Fortuna Lotto', '/kasina/fortuna/'), ('Sportka', '/loterie-online/'),
            ('Euromiliony', '/loterie-online/'), ('Eurojackpot', '/loterie-online/'),
            ('Šťastných 10', '/loterie-online/'), ('Stírací losy', '/loterie-online/'),
            ('Keno', '/loterie-online/'),
        ]
        return f'<section class="internal-links-section"><h3>🎫 Online loterie a stírací losy</h3><div class="internal-links">{kw_links(items)}</div></section>'

    # FALLBACK : nejlepší kasina (default)
    return f'<section class="internal-links-section"><h3>🎰 Související kasina</h3><div class="internal-links">{cas_links(sorted_by_rating[:18])}</div></section>'


def build_casino_tops(casinos, slug=''):
    sorted_casinos = sort_casinos_with_priority(casinos)
    total = len(sorted_casinos)
    total_pages = (total + CASINOS_PER_PAGE - 1) // CASINOS_PER_PAGE

    cards = []
    for idx, c in enumerate(sorted_casinos, 1):
        page = ((idx - 1) // CASINOS_PER_PAGE) + 1
        card_html = build_top_card(c, idx)
        card_html = card_html.replace('<div class="top-card"', f'<div class="top-card" data-page="{page}"', 1)
        cards.append(card_html)

    cards_html = '\n'.join(cards)
    pagination_html = build_pagination(total_pages, 1)
    internal_links_html = build_thematic_internal_links(slug, casinos)

    return f'''{FILTER_BAR_HTML}
{pagination_html}
<div class="casino-tops" data-current-page="1" data-total-pages="{total_pages}">
{cards_html}
</div>
{pagination_html}
{internal_links_html}
{FILTER_MODAL_HTML}'''


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


def shorten_toc_label(heading_text):
    """Convert a long H2 into a short scannable label with emoji."""
    h = heading_text.lower()
    # Strip HTML
    h_clean = re.sub(r'<[^>]+>', '', h)

    # Match topics → short label + emoji
    mapping = [
        ('hodnoceni', '⭐ Hodnocení'), ('hodnotici', '⭐ Hodnocení'),
        ('nejlepsi', '🏆 Top kasina'), ('top kasin', '🏆 Top kasina'), ('top 5', '🏆 Top 5'), ('top 10', '🏆 Top 10'),
        ('bonus', '🎁 Bonusy'), ('promo', '🎁 Promo akce'),
        ('vyber', '⚡ Výběry'), ('rychlost', '⚡ Rychlost'),
        ('platb', '💳 Platby'),
        ('hry', '🎰 Hry'), ('automaty', '🎰 Automaty'), ('slot', '🎰 Sloty'),
        ('live', '🎥 Live kasino'),
        ('poker', '🃏 Poker'),
        ('mobiln', '📱 Mobilní'),
        ('podpor', '💬 Podpora'),
        ('licence', '📜 Licence'), ('legaln', '⚖️ Legalita'),
        ('bezpecn', '🛡️ Bezpečnost'),
        ('zakazn', '👤 Zákaznický servis'),
        ('regul', '⚖️ Regulace'),
        ('dane', '💰 Daně'),
        ('odpoved', '🛡️ Odpovědné hraní'), ('zavislost', '🛡️ Závislost'),
        ('faq', '❓ FAQ'), ('caste otaz', '❓ FAQ'),
        ('zaver', '🎯 Závěr'), ('verdict', '🎯 Verdikt'), ('verdikt', '🎯 Verdikt'),
        ('atmosf', '🎨 Atmosféra'), ('design', '🎨 Design'),
        ('registr', '📝 Registrace'),
        ('kryt', '₿ Krypto'), ('crypto', '₿ Krypto'), ('bitcoin', '₿ Bitcoin'),
        ('vip', '👑 VIP'),
        ('rtp', '📊 RTP'), ('volatilita', '📊 Volatilita'),
        ('jackpot', '💎 Jackpot'),
        ('ovi', '🆕 Novinky'), ('nove', '🆕 Nové'),
        ('porovn', '📊 Srovnání'), ('srovn', '📊 Srovnání'),
        ('tipy', '💡 Tipy'), ('strategi', '🎯 Strategie'),
        ('kriteri', '✅ Kritéria'),
        ('jak ', '📖 Jak na to'),
        ('proc', '❓ Proč'),
        ('co je', '❓ Co je'), ('co jso', '❓ Co jsou'),
        ('hist', '📚 Historie'),
        ('typ', '🔖 Typy'),
        ('rozdíl', '🔄 Rozdíly'),
        ('mýt', '💭 Mýty'),
        ('trend', '🚀 Trendy'),
        ('audit', '✅ Audit'), ('certifik', '✅ Certifikace'),
        ('mince', '₿ Mince'),
        ('bankroll', '💵 Bankroll'),
        ('limit', '🚫 Limity'),
        ('lotterie', '🎫 Loterie'), ('losy', '🎫 Losy'),
        ('sport', '⚽ Sport'), ('sazk', '⚽ Sázky'),
    ]
    for keyword, label in mapping:
        if keyword in h_clean:
            return label
    # Fallback: first 3 words
    words = h_clean.strip().split()[:3]
    return '📌 ' + ' '.join(words).capitalize()


def build_toc(seo_content):
    headings = re.findall(r'<h2[^>]*>(.*?)</h2>', seo_content, flags=re.DOTALL)
    if not headings:
        return ''
    items = ''
    for i, h in enumerate(headings):
        anchor = f'sec-{i+1}'
        short_label = shorten_toc_label(h)
        items += f'<li><a href="#{anchor}">{short_label}</a></li>\n'
    toc = f'''<div class="toc" id="toc">
    <div class="toc-header" onclick="this.parentElement.classList.toggle('closed')">
        <span class="toc-title"><span class="icon">📑</span> Obsah článku</span>
        <span class="toc-toggle">▼</span>
    </div>
    <ul class="toc-list">{items}</ul>
</div>'''
    counter = [0]
    def add_id(m):
        counter[0] += 1
        return f'<h2 id="sec-{counter[0]}">{m.group(1)}</h2>'
    return toc, re.sub(r'<h2(?!\s+id)>(.*?)</h2>', add_id, seo_content, flags=re.DOTALL)


HERO_ICON_SETS = {
    'crypto': ['₿', 'Ξ', '₮', '◎', 'Ł'],
    'bonus': ['🎁', '💰', '🎰', '⭐', '💎'],
    'free-spiny': ['🎰', '🎲', '⭐', '💫', '🎯'],
    'live': ['🎥', '🃏', '🎲', '🎯', '🎮'],
    'mobile': ['📱', '📲', '⚡', '✅', '🎮'],
    'new': ['🆕', '⭐', '🎰', '🚀', '✨'],
    'safe': ['🔒', '🛡️', '✅', '⚖️', '🎯'],
    'top': ['🏆', '🥇', '🥈', '🥉', '⭐'],
    'license': ['📜', '⚖️', '🇨🇿', '✅', '🛡️'],
    'sport': ['⚽', '🏀', '🎾', '🏈', '🥊'],
    'poker': ['🃏', '♠️', '♥️', '♦️', '♣️'],
    'jackpot': ['💰', '💎', '🏆', '🎰', '⭐'],
    'rtp': ['📊', '💹', '🎯', '⭐', '🎰'],
    'slots': ['🎰', '🍒', '🔔', '7️⃣', '⭐'],
    'default': ['🎰', '🎲', '🎯', '⭐', '🃏'],
}


def get_hero_icons(slug):
    """Pick icon set based on keyword slug."""
    s = slug.lower()
    if 'free-spiny' in s or 'free-spins' in s: return HERO_ICON_SETS['free-spiny']
    if 'bonus' in s: return HERO_ICON_SETS['bonus']
    if 'live' in s: return HERO_ICON_SETS['live']
    if 'mobiln' in s: return HERO_ICON_SETS['mobile']
    if 'nove' in s or 'nova' in s: return HERO_ICON_SETS['new']
    if 'bezpecn' in s or 'legaln' in s: return HERO_ICON_SETS['safe']
    if 'top' in s or 'nejlepsi' in s: return HERO_ICON_SETS['top']
    if 'licence' in s or 'ceska-licence' in s: return HERO_ICON_SETS['license']
    if 'sport' in s or 'sazen' in s: return HERO_ICON_SETS['sport']
    if 'poker' in s: return HERO_ICON_SETS['poker']
    if 'jackpot' in s: return HERO_ICON_SETS['jackpot']
    if 'rtp' in s or 'volatilita' in s: return HERO_ICON_SETS['rtp']
    if 'automat' in s or 'sloty' in s: return HERO_ICON_SETS['slots']
    return HERO_ICON_SETS['default']


def build_hero_icons_html(slug):
    icons = get_hero_icons(slug)
    return ''.join(f'<div class="hero-card-icon">{ic}</div>' for ic in icons)


def generate_keyword_page(keyword, casinos, template, all_keywords):
    casino_table = build_casino_tops(casinos, keyword.get('slug', ''))
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
    html = html.replace('{{casino_count}}', str(len(casinos)))
    html = html.replace('{{hero_icons}}', build_hero_icons_html(keyword['slug']))
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
            <h3 class="faq-q">{item["q"]}</h3>
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


def build_notre_avis_short(casino):
    """4-line synthetic intro for the notre-avis box."""
    r = casino['review']
    bonus_part = r['bonusAmount']
    if r['freeSpinsCount'] != '—':
        bonus_part += f" + {r['freeSpinsCount']}"
    return (f"<strong>{casino['name']}</strong> je online kasino fungující od roku {r['yearCreated']} "
            f"s licencí <strong>{r['license']}</strong>. Uvítací bonus <strong>{bonus_part}</strong> "
            f"při minimálním vkladu {casino['minDeposit']} Kč. Výběry jsou zpracovány "
            f"<strong>{r['withdrawalSpeedDetail'].lower()}</strong> a podpora je dostupná 24/7 v češtině. "
            f"Hodnocení <strong>{casino['rating']}/5</strong> na základě testování od {r['reviewCount']} hráčů.")


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


def build_pros_list_html(pros):
    """Pros with green badges."""
    items = []
    for p in pros:
        items.append(f'<li><span class="pros-cons-badge">✓</span><span>{p}</span></li>')
    return '\n'.join(items)


def build_cons_list_html(cons):
    """Cons with red badges."""
    items = []
    for c in cons:
        items.append(f'<li><span class="pros-cons-badge">✗</span><span>{c}</span></li>')
    return '\n'.join(items)


def build_bonus_details_html(bonuses, casino_url, wagering, min_deposit):
    """Bonus rows with table + button (1er dépôt, 2ème dépôt, etc.)"""
    items = []
    icons = ['🥇', '🥈', '🥉', '🎁']
    for i, b in enumerate(bonuses[:4]):
        icon = icons[i] if i < len(icons) else '🎁'
        title = b.get('title', f'Bonus {i+1}. vklad')
        value = b.get('value', '')
        detail = b.get('detail', '')
        items.append(f'''<div class="bonus-detail-row">
            <div class="bonus-detail-label"><span class="bonus-detail-icon">{icon}</span>{title}</div>
            <div class="bonus-detail-table">
                <div class="bonus-detail-cell"><span class="bonus-detail-cell-label">Hodnota</span><span class="bonus-detail-cell-value">{value}</span></div>
                <div class="bonus-detail-cell"><span class="bonus-detail-cell-label">Detail</span><span class="bonus-detail-cell-value">{detail[:30]}</span></div>
                <div class="bonus-detail-cell"><span class="bonus-detail-cell-label">Wager</span><span class="bonus-detail-cell-value">{wagering}</span></div>
            </div>
            <a href="{casino_url}" class="bonus-detail-cta" target="_blank" rel="nofollow noopener">Získat</a>
        </div>''')
    return '\n'.join(items)


def build_aside_providers_html(providers):
    """Provider grid for sidebar (8 items)."""
    items = []
    initials_map = {
        'Pragmatic Play': 'PP', 'NetEnt': 'NE', "Play'n GO": "P'G",
        'Evolution': 'EV', 'Microgaming': 'MG', 'Novomatic': 'NV',
        'Synot Games': 'SG', 'Yggdrasil': 'YG', 'Red Tiger': 'RT',
        'Hacksaw Gaming': 'HS', 'Push Gaming': 'PG', 'Big Time Gaming': 'BTG',
        'Quickspin': 'QS', 'Thunderkick': 'TK', 'ELK Studios': 'ELK',
        'Spribe': 'SP', 'BGaming': 'BG', 'Wazdan': 'WZ',
        'Relax Gaming': 'RG', 'Endorphina': 'EP', 'iSoftBet': 'iSB',
    }
    for p in providers[:8]:
        initials = initials_map.get(p, p[:2].upper())
        items.append(f'<div class="aside-grid-item"><span class="aside-grid-item-icon" style="font-size:0.78rem;font-weight:800;color:#22c55e;">{initials}</span>{p[:10]}</div>')
    return '\n'.join(items)


def build_aside_payments_html(methods):
    img_map = {
        "Visa": "visa.svg", "Mastercard": "mastercard.png",
        "Bankovní převod": "bankovni-prevod.svg", "Skrill": "skrill.svg",
        "Neteller": "neteller.svg", "PaySafeCard": "paysafecard.ico",
        "Apple Pay": "apple-pay.svg", "PayPal": "paypal.png",
        "MuchBetter": "muchbetter.ico",
    }
    emoji_map = {
        "Google Pay": "📱", "Bitcoin": "₿", "Ethereum": "⟠",
        "USDT": "💲", "Maestro": "💳", "ecoPayz": "💰",
    }
    items = []
    for m in methods[:8]:
        if m in img_map:
            inner = f'<img src="/assets/images/payments/{img_map[m]}" alt="{m}">'
            icon_class = 'aside-grid-item-icon payment-icon'
        else:
            inner = emoji_map.get(m, "💳")
            icon_class = 'aside-grid-item-icon'
        items.append(f'<div class="aside-grid-item"><span class="{icon_class}">{inner}</span>{m[:8]}</div>')
    return '\n'.join(items)


def generate_review_page(casino, template, all_casinos):
    r = casino['review']

    bonus_pack_headline = f"{r['bonusAmount']}"
    if r['freeSpinsCount'] != '—':
        bonus_pack_headline += f" + {r['freeSpinsCount']}"

    today = datetime.now().strftime('%d. %m. %Y')

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
        '{{today_date}}': today,
        '{{pros_list_html}}': build_pros_list_html(r['pros']),
        '{{cons_list_html}}': build_cons_list_html(r['cons']),
        '{{bonus_details_html}}': build_bonus_details_html(r['bonuses'], casino['bonusUrl'], r.get('wagering', casino.get('wagering', 'x30')), f"{casino['minDeposit']} Kč"),
        '{{aside_providers_html}}': build_aside_providers_html(r['providers']),
        '{{aside_payments_html}}': build_aside_payments_html(r['paymentMethods']),
        '{{notre_avis_short}}': build_notre_avis_short(casino),
        '{{gauge_value}}': str(round((casino['rating'] / 5) * 110, 1)),
        '{{rating_partner_1}}': str(round(casino['rating'] - 0.3, 1)),
        '{{rating_partner_2}}': str(round(casino['rating'] - 0.5, 1)),
    }

    for placeholder, value in replacements.items():
        html = html.replace(placeholder, value)

    return html


# ============================================================
# MINI-GAME PAGE GENERATION
# ============================================================

CATEGORY_LABELS = {
    'crash': 'Crash hra',
    'instant': 'Instant',
    'slot': 'Automat',
    'live': 'Live',
}


def generate_minigame_page(game, template, casino_lookup):
    """Generate single mini-game page."""
    rtp_num = float(game['rtp'].replace('%', '').replace(',', '.'))
    rtp_comparison = 'výborné (nad 97 %)' if rtp_num >= 97 else 'dobré' if rtp_num >= 96 else 'standardní'

    how_to_play_html = '\n'.join(f'<li><strong>Krok {i+1}:</strong> {step}</li>' for i, step in enumerate(game['how_to_play']))
    features_html = '\n'.join(f'<div class="minigame-feature">{f}</div>' for f in game['features'])
    tips_html = '\n'.join(f'<li>{tip}</li>' for tip in game['tips'])

    # Pick featured casino — prioritize affiliate casinos (m-traff)
    available_at = game.get('available_at', [])
    featured_slug = next((s for s in AFFILIATE_PRIORITY if s in available_at), None)
    if not featured_slug and available_at:
        featured_slug = available_at[0]

    if featured_slug and featured_slug in casino_lookup:
        fc = casino_lookup[featured_slug]
        featured_casino_url = fc['bonusUrl']
        featured_casino_name = fc['name']
        featured_casino_bonus = fc['bonus']
    else:
        featured_casino_url = '/kasina/'
        featured_casino_name = 'Doporučeném kasinu'
        featured_casino_bonus = 'Štědrý uvítací bonus'

    # Available casinos cards (full)
    available_html = '<div class="minigames-hub" style="grid-template-columns:repeat(auto-fit,minmax(220px,1fr));">'
    for slug in game.get('available_at', []):
        if slug in casino_lookup:
            c = casino_lookup[slug]
            ext = get_logo_ext(slug)
            available_html += f'''<a href="{c['bonusUrl']}" target="_blank" rel="nofollow noopener" class="minigame-card">
                <div class="minigame-card-thumb" style="--card-color:#1e293b;background:rgba(255,255,255,0.95);">
                    <img src="/assets/images/casinos/{slug}.{ext}" alt="{c['name']}" style="max-width:140px;max-height:80px;object-fit:contain;">
                </div>
                <div class="minigame-card-body">
                    <div class="minigame-card-name">{c['name']}</div>
                    <div class="minigame-card-provider">{c['bonus']}</div>
                    <div style="margin-top:10px;background:linear-gradient(135deg,#22c55e,#16a34a);color:#fff;padding:8px;border-radius:6px;text-align:center;font-weight:800;font-size:0.78rem;text-transform:uppercase;letter-spacing:0.3px;">Hrát {game['name']}</div>
                </div>
            </a>'''
    available_html += '</div>'

    # Sidebar CTA list
    cta_html = ''
    for slug in game.get('available_at', [])[:4]:
        if slug in casino_lookup:
            c = casino_lookup[slug]
            ext = get_logo_ext(slug)
            cta_html += f'''<a href="{c['bonusUrl']}" target="_blank" rel="nofollow noopener" class="minigame-cta-casino">
                <img src="/assets/images/casinos/{slug}.{ext}" alt="{c['name']}">
                <span class="minigame-cta-casino-name">{c['name']}</span>
                <span class="minigame-cta-casino-go">Hrát</span>
            </a>'''

    replacements = {
        '{{game_name}}': game['name'],
        '{{game_slug}}': game['slug'],
        '{{game_icon}}': game['icon'],
        '{{game_color}}': game['color'],
        '{{game_iframe}}': game['iframe'],
        '{{game_description}}': game['description'],
        '{{featured_casino_url}}': featured_casino_url,
        '{{featured_casino_name}}': featured_casino_name,
        '{{featured_casino_bonus}}': featured_casino_bonus,
        '{{provider}}': game['provider'],
        '{{rtp}}': game['rtp'],
        '{{rtp_comparison}}': rtp_comparison,
        '{{volatility}}': game['volatility'],
        '{{min_bet}}': game['min_bet'],
        '{{max_bet}}': game['max_bet'],
        '{{max_win}}': game['max_win'],
        '{{release}}': game['release'],
        '{{category_label}}': CATEGORY_LABELS.get(game['category'], game['category']),
        '{{how_to_play_html}}': how_to_play_html,
        '{{features_html}}': features_html,
        '{{tips_html}}': tips_html,
        '{{available_casinos_html}}': available_html,
        '{{available_casinos_cta_html}}': cta_html,
        '{{nav_html}}': NAV_HTML,
        '{{footer_html}}': FOOTER_HTML,
    }
    html = template
    for k, v in replacements.items():
        html = html.replace(k, v)
    return html


def generate_minigames_hub(minigames, template):
    """Generate the mini-games hub page."""
    cards_html = ''
    for game in minigames:
        cards_html += f'''<a href="/hry/{game['slug']}/" class="minigame-card" data-category="{game['category']}">
            <div class="minigame-card-thumb" style="--card-color:{game['color']};background:linear-gradient(135deg,{game['color']},rgba(0,0,0,0.5));">
                <span class="minigame-card-rtp">RTP {game['rtp']}</span>
                <span class="minigame-card-category">{CATEGORY_LABELS.get(game['category'], game['category'])}</span>
                <span class="minigame-card-icon">{game['icon']}</span>
            </div>
            <div class="minigame-card-body">
                <div class="minigame-card-name">{game['name']}</div>
                <div class="minigame-card-provider">{game['provider']}</div>
                <div class="minigame-card-stats">
                    <span>Min. <strong>{game['min_bet']}</strong></span>
                    <span>Max. výhra <strong>{game['max_win']}</strong></span>
                </div>
            </div>
        </a>'''

    replacements = {
        '{{minigame_cards}}': cards_html,
        '{{nav_html}}': NAV_HTML,
        '{{footer_html}}': FOOTER_HTML,
        '{{author_box}}': build_author_box(8),
    }
    html = template
    for k, v in replacements.items():
        html = html.replace(k, v)
    return html


# ============================================================
# MAIN
# ============================================================

def main():
    print('🎰 Casino Arena — Generating pages...\n')

    # Auto-regenerate filter DB before page generation
    try:
        import subprocess
        subprocess.run(['python', os.path.join(BASE_DIR, 'generate_filter_db.py')], check=False, capture_output=True)
        print('  🗄️  Refreshed casino-filters.json\n')
    except Exception:
        pass

    casinos_data = load_json('casinos.json')
    keywords_data = load_json('keywords.json')
    template = load_file('template.html')
    review_template = load_file('casino-avis-template.html')

    casinos = casinos_data['casinos']
    keywords = keywords_data['keywords']

    # Generate keyword pages
    # Write keyword pages to ROOT (not /pages/) so /X/ resolves correctly on server
    pages_dir = BASE_DIR
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

    # Generate mini-game pages
    try:
        minigames_data = load_json('mini_games.json')
        minigames = minigames_data['minigames']
        minigame_template = load_file('minigame-template.html')
        hub_template = load_file('minigames-hub-template.html')

        # Slug-to-casino lookup for affiliate links
        casino_lookup = {c['slug']: c for c in casinos}

        hry_dir = os.path.join(BASE_DIR, 'hry', 'mini-hry')
        os.makedirs(hry_dir, exist_ok=True)

        # Generate hub page
        hub_html = generate_minigames_hub(minigames, hub_template)
        with open(os.path.join(hry_dir, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(hub_html)
        print(f'  🎮 /hry/mini-hry/index.html')

        mg_count = 0
        for game in minigames:
            slug = game['slug']
            game_dir = os.path.join(BASE_DIR, 'hry', slug)
            os.makedirs(game_dir, exist_ok=True)
            html = generate_minigame_page(game, minigame_template, casino_lookup)
            with open(os.path.join(game_dir, 'index.html'), 'w', encoding='utf-8') as f:
                f.write(html)
            mg_count += 1
            print(f'  🎮 /hry/{slug}/index.html')

        print(f'🎮 Generated {mg_count} mini-game pages + 1 hub')
    except FileNotFoundError as e:
        print(f'  ⏭  Mini-games skipped: {e}')

    print(f'\n✅ Generated {kw_count} keyword pages in pages/')
    print(f'★ Generated {review_count} casino review pages in kasina/')
    print(f'📊 Casinos: {len(casinos)}')
    print(f'🔑 Keywords: {len(keywords)}')


if __name__ == '__main__':
    main()
