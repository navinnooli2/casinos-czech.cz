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
    🎰 Bonus 10 000 Kč + 200 FS — <a href="/nejlepsi-kasinovy-bonus/">Získat →</a>
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
    <div class="author-avatar"><img src="/assets/images/author-mn.jpg" alt="Martin Novák"></div>
    <div class="author-info">
        <div class="author-name">Martin Novák <span>— Expert iGaming</span></div>
        <div class="author-meta">Aktualizováno {{date}} · {{read_time}} min čtení</div>
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
                    <li><a href="/kasino-pro-zacatecniky/">Náš tým</a></li>
                    <li><a href="/legalni-kasina-cz/">Právní podmínky</a></li>
                    <li><a href="#">Mapa stránek</a></li>
                    <li><a href="#">Kontakt</a></li>
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
    <button class="filter-sort">
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M3 18h6v-2H3v2zM3 6v2h18V6H3zm0 7h12v-2H3v2z"/></svg>
        Relevance
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M7 10l5 5 5-5z"/></svg>
    </button>
    <button class="filter-btn" onclick="openFilterModal()">
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M3 17v2h6v-2H3zM3 5v2h10V5H3zm10 16v-2h8v-2h-8v-2h-2v6h2zM7 9v2H3v2h4v2h2V9H7zm14 4v-2H11v2h10zm-6-4h2V7h4V5h-4V3h-2v6z"/></svg>
        Filtry
    </button>
</div>'''


AFFILIATE_PRIORITY = ['smash', '29black', 'goldzino', 'playjonny', 'roulettino']


def sort_casinos_with_priority(casinos):
    """Put affiliate casinos (m-traff) first, then sort rest by rating descending."""
    priority = [c for slug in AFFILIATE_PRIORITY for c in casinos if c['slug'] == slug]
    others = sorted([c for c in casinos if c['slug'] not in AFFILIATE_PRIORITY],
                    key=lambda x: x.get('rating', 0), reverse=True)
    return priority + others


def build_casino_tops(casinos):
    sorted_casinos = sort_casinos_with_priority(casinos)
    cards = '\n'.join(build_top_card(c, i) for i, c in enumerate(sorted_casinos, 1))
    return f'{FILTER_BAR_HTML}\n<div class="casino-tops">\n{cards}\n</div>\n{FILTER_MODAL_HTML}'


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
