#!/usr/bin/env python3
"""Add 12 new m-traff affiliate casinos to casinos.json.

Casinos: betista, needforslots, billionairespin, bdmbet, mafia-casino,
betify, spinsy, cashed, spinbara, betriot, casinozer, rabona-casino.
"""

import json
import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(BASE, 'data', 'casinos.json')

AFF_BASE = "https://m-traff.net/HYcs2BV5?sub_id_1="


def slugify(s: str) -> str:
    s = s.lower()
    # Czech accent normalization basics
    repl = {
        'á': 'a', 'č': 'c', 'ď': 'd', 'é': 'e', 'ě': 'e', 'í': 'i',
        'ň': 'n', 'ó': 'o', 'ř': 'r', 'š': 's', 'ť': 't', 'ú': 'u',
        'ů': 'u', 'ý': 'y', 'ž': 'z', "'": '', '’': '', '(': '', ')': '',
    }
    for k, v in repl.items():
        s = s.replace(k, v)
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return s


def build_filters(casino: dict) -> dict:
    review = casino['review']
    bonus_lower = casino['bonus'].lower()
    speed = review.get('withdrawalSpeed', '24h')
    license_str = review.get('license', '').lower()
    if 'mf' in license_str or 'ministerstvo' in license_str:
        license_key = 'mf-cr'
    elif 'curaç' in license_str or 'curacao' in license_str:
        license_key = 'curacao'
    elif 'mga' in license_str:
        license_key = 'mga'
    else:
        license_key = slugify(license_str) or 'curacao'

    payments = [slugify(p) for p in review.get('paymentMethods', [])]
    providers = [slugify(p) for p in review.get('providers', [])]

    has_no_deposit = 'bez vkladu' in bonus_lower or 'no deposit' in bonus_lower
    has_free_spins = casino.get('freeSpins', 0) > 0
    has_cashback = any(
        'cashback' in (b.get('title', '') + ' ' + b.get('detail', '')).lower()
        for b in review.get('bonuses', [])
    )
    has_app = 'aplikace' in review.get('mobile', '').lower() or 'app' in review.get('mobile', '').lower()
    has_vip = bool(review.get('vipProgram'))
    has_sport = any(
        'sport' in (b.get('title', '') + ' ' + b.get('detail', '')).lower() or
        'sázk' in (b.get('title', '') + ' ' + b.get('detail', '')).lower()
        for b in review.get('bonuses', [])
    ) or 'sport' in casino.get('description', '').lower()
    has_esport = 'esport' in casino.get('description', '').lower() or any(
        'esport' in (b.get('title', '') + ' ' + b.get('detail', '')).lower()
        for b in review.get('bonuses', [])
    )
    has_crypto = any(p in providers for p in ['bitcoin', 'ethereum', 'usdt', 'litecoin']) or \
                 any('bitcoin' in p or 'ethereum' in p or 'usdt' in p for p in payments)

    wager_str = casino.get('wagering', 'x35').lower().replace('x', '').strip()
    try:
        wager_int = int(wager_str)
    except ValueError:
        wager_int = 0

    return {
        'rating': casino['rating'],
        'minDeposit': casino['minDeposit'],
        'freeSpins': casino['freeSpins'],
        'wagering': wager_int,
        'speed': speed,
        'license': license_key,
        'payments': payments,
        'providers': providers,
        'hasNoDeposit': has_no_deposit,
        'hasFreeSpins': has_free_spins,
        'hasCashback': has_cashback,
        'hasApp': has_app,
        'hasVip': has_vip,
        'hasSport': has_sport,
        'hasEsport': has_esport,
        'hasCrypto': has_crypto,
    }


# Common payment + provider pools (varied per casino)
CORE_PROVIDERS = [
    'Pragmatic Play', 'NetEnt', "Play'n GO", 'Evolution', 'Microgaming',
    'Hacksaw Gaming', 'Push Gaming', 'Nolimit City', 'ELK Studios',
    'Yggdrasil', 'Spribe', 'BGaming', 'Wazdan', 'Relax Gaming',
    'Quickspin', 'Thunderkick', 'Big Time Gaming', 'Red Tiger',
    'Endorphina', 'Booongo',
]
EXTRA_PROVIDERS = [
    'Habanero', 'Betsoft', 'Playson', 'iSoftBet', 'Kalamba',
    'Spinomenal', 'Stakelogic', 'Blueprint', 'Print Studios',
    'Ezugi', 'Pragmatic Play Live', 'Authentic Gaming',
]


NEW = [
    # 1. Betista — premium top tier
    {
        "id": "betista", "name": "Betista", "slug": "betista",
        "rating": 4.5,
        "bonus": "Mega bonus +370% až 3 700 € + 100 free spinů",
        "bonusAmount": "3 700 €", "wagering": "x35",
        "bonusUrl": AFF_BASE + "betista", "freeSpins": 100, "minDeposit": 10,
        "description": "Prémiové online kasino s jedním z nejvyšších uvítacích bonusů na trhu – až 370 % match a 100 free spinů.",
        "features": ["Bonus +370 %", "Min. vklad 10 €", "VIP program", "Live kasino"],
        "review": {
            "metaDescription": "Betista casino recenze 2026 – +370 % bonus až 3 700 € + 100 free spinů. Hodnocení her, plateb, podpory a VIP programu.",
            "reviewCount": 624, "bonusAmount": "3 700 €", "freeSpinsCount": "100 FS",
            "withdrawalSpeed": "24h",
            "owner": "Betista Group N.V.", "yearCreated": "2024",
            "license": "Curaçao", "withdrawalRange": "10 € – 50 000 €",
            "withdrawalSpeedDetail": "Do 24 hodin", "czechLanguage": "Ano", "mobile": "Ano (web)",
            "introduction": "Betista je prémiové online kasino, které vstoupilo na trh v roce 2024 a okamžitě upoutalo pozornost díky jednomu z nejvyšších uvítacích balíčků v branži. Nabízí celkem 370 % bonus na vklad až do 3 700 €, doplněný 100 free spiny na top sloty. Platforma je plně lokalizovaná do češtiny, podporuje euro i CZK a obsahuje přes 4 000 her od více než 50 předních poskytovatelů. Betista cílí na zkušené hráče i začátečníky – nabízí nízký minimální vklad 10 €, široký výběr automatů, klasických stolních her a propracované live kasino od Evolution Gaming. Kromě toho se může pochlubit moderním přehledným designem, plně responzivním mobilním webem a 24/7 zákaznickou podporou s živým chatem v češtině.",
            "bonusIntro": "Uvítací balíček Betista patří mezi nejštědřejší v Evropě. Jako nový hráč můžete získat 370 % match přes první tři vklady – maximum bonusu je 3 700 €, plus k tomu obdržíte 100 free spinů na vybrané sloty. Bonus má férové podmínky protočení x35.",
            "bonuses": [
                {"title": "1. vklad", "value": "+150%", "detail": "Až 1 500 €, x35"},
                {"title": "2. vklad", "value": "+120%", "detail": "Až 1 200 €, x35"},
                {"title": "3. vklad", "value": "+100%", "detail": "Až 1 000 € + 100 FS"},
                {"title": "Cashback VIP", "value": "15%", "detail": "Týdenní vrácení ztrát"}
            ],
            "weeklyPromo": "Betista pořádá pravidelné turnaje s prize poolem až 100 000 €, denní mise s odměnami ve free spinech, páteční reload bonusy 50 % a víkendové cashback akce. Loyalty program odměňuje každou sázku body, které lze vyměnit za bonusy.",
            "vipProgram": "Betista VIP Club nabízí sedm úrovní – od Bronze po Diamond Elite. Postupem získáváte přístup k vyšším cashback procentům, osobnímu VIP manažerovi, exkluzivním turnajům, narozeninovým bonusům a rychlejším výběrům.",
            "gamesIntro": "Betista nabízí přes 4 000 her od více než 50 poskytovatelů – jeden z nejširších katalogů na trhu s důrazem na nejnovější hity.",
            "gamesSlots": "Více než 3 500 automatů od Pragmatic Play, NetEnt, Play'n GO, Nolimit City, Hacksaw Gaming a Push Gaming. Megaways, jackpoty, klasické tříválcové automaty i nejnovější releasy. RTP 96–98 %.",
            "gamesTable": "Stolní hry zahrnují desítky variant rulety, blackjacku, baccaratu a pokeru. K dispozici jsou i méně tradiční tituly jako Sic Bo, Dragon Tiger nebo Casino Hold'em.",
            "gamesLive": "Live kasino od Evolution Gaming a Pragmatic Play Live nabízí HD streaming z reálných studií. Crazy Time, Mega Ball, Lightning Roulette, Speed Baccarat a desítky dalších stolů 24/7.",
            "gamesMini": "Crash games (Aviator, JetX, Spaceman), Plinko, Mines, Hi-Lo a Dice od Spribe, Turbo Games a BGaming. Rychlá zábava s vysokým potenciálem výher.",
            "paymentsIntro": "Betista podporuje všechny hlavní platební metody včetně kryptoměn. Vklady jsou okamžité, výběry zpracovány do 24 hodin.",
            "paymentMethods": ["Visa", "Mastercard", "Skrill", "Neteller", "PaySafeCard", "Apple Pay", "Bitcoin", "Ethereum", "USDT", "MuchBetter", "Bankovní převod"],
            "paymentCount": 11,
            "providersIntro": "Betista spolupracuje s 50+ předními výrobci her. Kvalita a férovost jsou garantovány nezávislými audity.",
            "providers": CORE_PROVIDERS + ['Habanero', 'Betsoft', 'Playson', 'iSoftBet', 'Stakelogic', 'Pragmatic Play Live', 'Ezugi'],
            "providerCount": 27,
            "advantages": [
                "Jeden z nejvyšších uvítacích bonusů na trhu – +370 % až 3 700 €",
                "Nízký minimální vklad pouhých 10 €",
                "Více než 4 000 her od 50+ poskytovatelů",
                "Podpora kryptoměn (Bitcoin, Ethereum, USDT)",
                "VIP program se sedmi úrovněmi a osobním manažerem",
                "Plně česká platforma s 24/7 live chatem"
            ],
            "pros": ["Bonus +370 % / 3 700 €", "Min. vklad 10 €", "4 000+ her", "Kryptoměny", "VIP Club 7 úrovní", "Live chat 24/7"],
            "cons": ["Curaçao licence (ne MF ČR)", "Wagering x35 přes 3 vklady", "Nemá nativní mobilní aplikaci"],
            "supportText": "Zákaznická podpora Betista je dostupná 24/7 přes live chat, email (support@betista.com) a v rámci VIP programu i telefonicky. Plně v češtině. Live chat odpovídá obvykle do 2 minut, k dispozici je rozsáhlé centrum nápovědy s návody a FAQ.",
            "faq": [
                {"q": "Jaký je uvítací bonus Betista?", "a": "Až +370 % bonus rozprostřený do tří vkladů – maximum 3 700 € + 100 free spinů na třetí vklad."},
                {"q": "Jaký je minimální vklad?", "a": "Pouhých 10 €, což je jeden z nejnižších limitů na trhu."},
                {"q": "Jak rychle jsou výběry?", "a": "E-peněženky a kryptoměny do 24 hodin, karty 1–3 dny, bankovní převody 2–5 dnů."},
                {"q": "Mohu platit Bitcoinem?", "a": "Ano, Betista přijímá Bitcoin, Ethereum, USDT a další kryptoměny s okamžitými vklady."},
                {"q": "Je Betista bezpečné?", "a": "Ano, kasino má licenci Curaçao, používá SSL šifrování a hry jsou pravidelně auditované."}
            ],
            "finalVerdict": "Betista je vynikající volba pro hráče, kteří hledají maximální uvítací bonus, široký výběr her a moderní platformu. S +370 % bonusem až 3 700 €, 100 free spiny, podporou kryptoměn a VIP programem se sedmi úrovněmi nabízí prémiový zážitek na nejvyšší úrovni."
        }
    },
    # 2. Needforslots — slot focused
    {
        "id": "needforslots", "name": "Needforslots", "slug": "needforslots",
        "rating": 4.3,
        "bonus": "+100% až 1 500 € + 250 free spinů",
        "bonusAmount": "1 500 €", "wagering": "x35",
        "bonusUrl": AFF_BASE + "needforslots", "freeSpins": 250, "minDeposit": 20,
        "description": "Online kasino zaměřené na automaty s obrovským katalogem 5 000+ slotů a 250 free spinů v uvítacím balíčku.",
        "features": ["5 000+ slotů", "250 free spinů", "Slot turnaje", "Megaways"],
        "review": {
            "metaDescription": "Needforslots casino recenze 2026 – +100 % bonus až 1 500 € + 250 free spinů. Specializace na sloty s 5 000+ tituly.",
            "reviewCount": 412, "bonusAmount": "1 500 €", "freeSpinsCount": "250 FS",
            "withdrawalSpeed": "24h",
            "owner": "NFS Gaming Ltd.", "yearCreated": "2023",
            "license": "Curaçao", "withdrawalRange": "20 € – 30 000 €",
            "withdrawalSpeedDetail": "Do 24 hodin", "czechLanguage": "Ano", "mobile": "Ano (web)",
            "introduction": "Needforslots je specializované online kasino z roku 2023 zaměřené primárně na automaty a sloty. Jeho katalog s více než 5 000 tituly je jeden z největších na trhu, přičemž důraz je kladen na megaways, bonus buy a nejnovější hity. Platforma je plně přeložena do češtiny, podporuje euro i CZK a nabízí jeden z nejlepších uvítacích balíčků pro fanoušky slotů – 100 % bonus na vklad až 1 500 € a 250 free spinů. Needforslots se vyznačuje rychlými výběry do 24 hodin, podporou populárních platebních metod včetně kryptoměn a 24/7 live chatem v češtině. Pro hráče, kteří milují automaty a hledají nejširší výběr, je tato značka jasnou volbou.",
            "bonusIntro": "Needforslots vítá nové hráče silným balíčkem orientovaným na sloty – 100 % bonus na první vklad až 1 500 € a celkem 250 free spinů rozprostřených do prvních pěti dní. Wagering x35 je férový vzhledem k velikosti bonusu.",
            "bonuses": [
                {"title": "1. vklad", "value": "+100%", "detail": "Až 1 500 €, x35"},
                {"title": "Free spiny", "value": "250 FS", "detail": "50 FS denně po 5 dní"},
                {"title": "Reload Mon/Wed", "value": "50%", "detail": "Až 500 € pondělí a středa"},
                {"title": "Slot Cashback", "value": "10%", "detail": "Týdenní bez wagering"}
            ],
            "weeklyPromo": "Needforslots pořádá týdenní slot turnaje s prize poolem až 50 000 €, denní 'Drops & Wins' od Pragmatic Play, exkluzivní free spin promo na nové sloty a měsíční Hall of Fame žebříček nejaktivnějších hráčů.",
            "vipProgram": "NFS Slot Club má 6 úrovní specializovaných pro fanoušky automatů. Každá úroveň přidává vyšší cashback, exkluzivní free spin balíčky, narozeninové bonusy a osobního VIP manažera od úrovně 4 výše.",
            "gamesIntro": "Needforslots má jeden z nejširších slot katalogů v Evropě – přes 5 000 automatů od 60+ poskytovatelů, plus dostatečný výběr stolních her a live kasina pro variabilitu.",
            "gamesSlots": "Více než 5 000 automatů včetně všech populárních hitů: Sweet Bonanza, Gates of Olympus, Big Bass Bonanza, Book of Dead, Money Train 4, Reactoonz, Wanted Dead or a Wild a další. Megaways, hold & win, bonus buy, jackpoty.",
            "gamesTable": "Klasická nabídka stolních her – ruleta evropská/francouzská/americká, blackjack, baccarat a poker. Limity od 1 € do 5 000 € na sázku.",
            "gamesLive": "Live kasino od Evolution Gaming a Pragmatic Play Live – ruleta, blackjack, baccarat, Crazy Time, Mega Ball, Sweet Bonanza Candyland a další game shows.",
            "gamesMini": "Aviator, JetX, Spaceman, Plinko, Mines a Dice od Spribe a Turbo Games. Rychlá zábava pro chvíle mezi sloty.",
            "paymentsIntro": "Needforslots podporuje všechny hlavní platební metody. Výběry jsou zpracovány do 24 hodin pro většinu metod.",
            "paymentMethods": ["Visa", "Mastercard", "Skrill", "Neteller", "PaySafeCard", "Apple Pay", "Bitcoin", "USDT", "MuchBetter", "Bankovní převod"],
            "paymentCount": 10,
            "providersIntro": "Needforslots spolupracuje s 60+ slot studii včetně všech předních značek a několika exkluzivních partnerů.",
            "providers": CORE_PROVIDERS + ['Habanero', 'Betsoft', 'Playson', 'Spinomenal', 'Stakelogic', 'Blueprint', 'Print Studios'],
            "providerCount": 27,
            "advantages": [
                "Jeden z největších slot katalogů – přes 5 000 automatů",
                "Štědrý uvítací balíček 250 free spinů + bonus 1 500 €",
                "Týdenní slot turnaje s prize poolem až 50 000 €",
                "Specializovaný NFS Slot Club s 6 úrovněmi",
                "Podpora kryptoměn (Bitcoin, USDT)",
                "Plně česká platforma s 24/7 podporou"
            ],
            "pros": ["5 000+ slotů", "250 free spinů uvítacích", "Slot turnaje", "Cashback bez wager", "Kryptoměny", "Plně česky"],
            "cons": ["Curaçao licence", "Užší nabídka stolních her", "Min. vklad 20 €"],
            "supportText": "Zákaznická podpora Needforslots je dostupná 24/7 přes live chat a email. Plně v češtině. Live chat odpovídá obvykle do 3 minut. K dispozici je obsáhlé FAQ s odpověďmi na nejčastější dotazy.",
            "faq": [
                {"q": "Kolik free spinů dostanu jako nový hráč?", "a": "Celkem 250 free spinů rozdělených na 5 dní po 50 FS, plus 100 % bonus do 1 500 € na první vklad."},
                {"q": "Jaký je největší slot v nabídce?", "a": "Megaways tituly jako Bonanza Megaways, jackpoty Mega Moolah a viral hity Sweet Bonanza a Gates of Olympus."},
                {"q": "Jak rychlé jsou výběry?", "a": "E-peněženky a kryptoměny do 24 hodin, karty a bankovní převody 1–3 dny."},
                {"q": "Pořádáte slot turnaje?", "a": "Ano, každý týden najdete 5+ slot turnajů s prize poolem až 50 000 €."},
                {"q": "Mohu hrát na mobilu?", "a": "Ano, mobilní web je plně responzivní a všechny sloty jsou dostupné na iOS i Androidu."}
            ],
            "finalVerdict": "Needforslots je rájem pro fanoušky automatů. S 5 000+ sloty, 250 free spiny v uvítacím balíčku, specializovaným Slot Clubem a týdenními turnaji nabízí perfektní zážitek pro každého slot hráče. Bonus 1 500 € a férový wagering jen umocňují atraktivitu této značky."
        }
    },
    # 3. BillionaireSpin — high roller, NO wager
    {
        "id": "billionairespin", "name": "BillionaireSpin", "slug": "billionairespin",
        "rating": 4.4,
        "bonus": "+255% až 2 500 € + 250 free spinů (BEZ wagering)",
        "bonusAmount": "2 500 €", "wagering": "Bez wagering",
        "bonusUrl": AFF_BASE + "billionairespin", "freeSpins": 250, "minDeposit": 20,
        "description": "Luxusní high-roller kasino s 255% bonusem a unikátní nabídkou bonusů BEZ wagering požadavků.",
        "features": ["Bonus bez wager", "+255 %", "High-roller VIP", "Kryptoměny"],
        "review": {
            "metaDescription": "BillionaireSpin recenze 2026 – +255 % bonus až 2 500 € + 250 free spinů BEZ wagering. Luxusní high-roller kasino.",
            "reviewCount": 287, "bonusAmount": "2 500 €", "freeSpinsCount": "250 FS",
            "withdrawalSpeed": "12h",
            "owner": "BillionaireSpin Ltd.", "yearCreated": "2024",
            "license": "Curaçao", "withdrawalRange": "20 € – 100 000 €",
            "withdrawalSpeedDetail": "Do 12 hodin", "czechLanguage": "Ano", "mobile": "Ano (web)",
            "introduction": "BillionaireSpin je luxusní high-roller kasino s prémiovým zlatým designem inspirovaným světem milionářů. Otevřelo brány v roce 2024 a okamžitě upoutalo pozornost díky unikátnímu bonusovému modelu – 255 % bonus a 250 free spinů BEZ wagering požadavků. To znamená, že vyhrané prostředky můžete okamžitě vybrat, což je v branži skutečná rarita. Platforma je plně česká, podporuje kryptoměny a nabízí přes 3 500 her od 50+ předních poskytovatelů. BillionaireSpin cílí především na zkušené hráče a high-rollery, ale díky nízkému minimálnímu vkladu 20 € je přístupné i pro začátečníky.",
            "bonusIntro": "BillionaireSpin přepisuje pravidla bonusů. Nabízí 255 % match na první vklad až 2 500 € a 250 free spinů – vše BEZ wagering požadavků. Vaše výhry jsou okamžitě vyplatitelné jako reálné peníze.",
            "bonuses": [
                {"title": "1. vklad", "value": "+255%", "detail": "Až 2 500 €, BEZ wager"},
                {"title": "Free spiny", "value": "250 FS", "detail": "BEZ wagering požadavků"},
                {"title": "High-roller", "value": "+200%", "detail": "Pro vklady 1 000+ €"},
                {"title": "VIP Cashback", "value": "20%", "detail": "Týdenní bez wager"}
            ],
            "weeklyPromo": "BillionaireSpin pořádá exkluzivní VIP turnaje s prize poolem až 500 000 €, weekly drops s garantovanými výhrami v hodnotě 100 000 €, daily missions a high-stakes víkendové eventy.",
            "vipProgram": "Billionaire Club je VIP program na pozvání pro nejaktivnější hráče. Členové získají osobního VIP manažera, exkluzivní bonusy bez wager, vyšší cashback (až 25 %), prioritní výběry během 1 hodiny, narozeninové dárky a pozvánky na luxusní eventy.",
            "gamesIntro": "BillionaireSpin nabízí pečlivě vybranou kolekci přes 3 500 prémiových her s důrazem na high-stakes možnosti a vysoké RTP.",
            "gamesSlots": "Přes 3 000 automatů od top poskytovatelů. Vysoké RTP 96–99 %, vysoké limity sázek pro high-rollery (až 1 000 € na spin) a exkluzivní jackpotová síť.",
            "gamesTable": "Široká nabídka stolních her s vysokými limity – ruleta, blackjack, baccarat, poker s limity od 100 € do 100 000 € na sázku.",
            "gamesLive": "Live kasino s VIP stoly, salon privé sekcí a exkluzivními high-stakes stoly. Provozováno Evolution Gaming s vlastními BillionaireSpin branded stoly.",
            "gamesMini": "Aviator, Spaceman, Plinko, Mines a další moderní hry. High-roller varianty s vyššími limity sázek.",
            "paymentsIntro": "BillionaireSpin podporuje všechny hlavní platební metody včetně kryptoměn. Výběry zpracovány do 12 hodin (VIP do 1 hodiny).",
            "paymentMethods": ["Visa", "Mastercard", "Skrill", "Neteller", "Bitcoin", "Ethereum", "USDT", "MuchBetter", "Apple Pay", "Bankovní převod"],
            "paymentCount": 10,
            "providersIntro": "BillionaireSpin spolupracuje s nejprestižnějšími poskytovateli her. Kvalita a vysoké RTP jsou prioritou.",
            "providers": CORE_PROVIDERS + ['Habanero', 'Betsoft', 'Stakelogic', 'Blueprint', 'Pragmatic Play Live', 'Authentic Gaming', 'Ezugi'],
            "providerCount": 27,
            "advantages": [
                "Unikátní bonus BEZ wagering – výhry jsou okamžitě vyplatitelné",
                "Velmi vysoký uvítací bonus +255 % až 2 500 €",
                "Nejrychlejší výběry na trhu – do 12 hodin (VIP do 1h)",
                "High-roller VIP program s exkluzivními výhodami",
                "Podpora kryptoměn (Bitcoin, Ethereum, USDT)",
                "Vysoké limity sázek až 1 000 € na spin"
            ],
            "pros": ["Bonus BEZ wager!", "+255 % až 2 500 €", "Výběry 12h", "High-roller stoly", "Kryptoměny", "Plně česky"],
            "cons": ["Curaçao licence", "Spíše pro pokročilé hráče", "Min. vklad 20 €"],
            "supportText": "Zákaznická podpora BillionaireSpin je dostupná 24/7 přes live chat, email a VIP telefonickou linku. Plně v češtině. Standardní odpověď do 2 minut, VIP klienti mají dedikovanou prioritní podporu s manažerem.",
            "faq": [
                {"q": "Co znamená 'bonus bez wagering'?", "a": "Výhry z uvítacího bonusu i 250 FS jsou okamžitě vyplatitelné jako reálné peníze – nemusíte nic protáčet."},
                {"q": "Jak se dostat do Billionaire Club?", "a": "Klub je na pozvání. Aktivní hráči s vysokými obraty jsou kontaktováni VIP manažerem."},
                {"q": "Mohu platit Bitcoinem?", "a": "Ano, BillionaireSpin přijímá Bitcoin, Ethereum, USDT a další kryptoměny s okamžitými vklady."},
                {"q": "Jak rychlé jsou opravdu výběry?", "a": "Standardně do 12 hodin, kryptoměny obvykle do 1 hodiny, VIP klienti mají prioritu (do 1 hodiny)."},
                {"q": "Je BillionaireSpin bezpečný?", "a": "Ano, kasino má licenci Curaçao, SSL šifrování a hry jsou pravidelně auditované."}
            ],
            "finalVerdict": "BillionaireSpin přepisuje pravidla bonusů. Unikátní +255 % bonus a 250 free spinů BEZ wagering požadavků z něj činí jednoho z nejatraktivnějších operátorů na trhu. Pokud hledáte luxusní high-roller zážitek s férovými podmínkami, rychlými výběry a podporou kryptoměn, BillionaireSpin je jasná volba."
        }
    },
    # 4. BDMBet — crypto + sports
    {
        "id": "bdmbet", "name": "BDMBet", "slug": "bdmbet",
        "rating": 4.2,
        "bonus": "+100% až 450 € + 250 free spinů",
        "bonusAmount": "450 €", "wagering": "x35",
        "bonusUrl": AFF_BASE + "bdmbet", "freeSpins": 250, "minDeposit": 20,
        "description": "Hybridní platforma kasino + sportovní sázky se silnou podporou kryptoměn a stovkami free spinů v uvítacím balíčku.",
        "features": ["Kasino + sport", "Kryptoměny", "250 FS", "Live betting"],
        "review": {
            "metaDescription": "BDMBet recenze 2026 – +100 % bonus až 450 € + 250 free spinů. Hybridní kasino + sport s podporou kryptoměn.",
            "reviewCount": 198, "bonusAmount": "450 €", "freeSpinsCount": "250 FS",
            "withdrawalSpeed": "24h",
            "owner": "BDMBet N.V.", "yearCreated": "2024",
            "license": "Curaçao", "withdrawalRange": "20 € – 25 000 €",
            "withdrawalSpeedDetail": "Do 24 hodin", "czechLanguage": "Ano", "mobile": "Ano (web)",
            "introduction": "BDMBet je moderní hybridní platforma, která spojuje online kasino se sportovní sázkovou kanceláří. Otevřelo se v roce 2024 a rychle si získalo oblibu díky silné podpoře kryptoměn (Bitcoin, Ethereum, USDT, Litecoin), širokému výběru her a štědrému uvítacímu balíčku 100 % až 450 € + 250 free spinů. Sportovní sekce nabízí desítky disciplín, live betting a virtuální sporty. Platforma je plně lokalizovaná do češtiny a podporuje 24/7 zákaznickou podporu.",
            "bonusIntro": "BDMBet vítá nové hráče dvojitou nabídkou – samostatné bonusy pro kasino a sport. Kasinový balíček nabízí 100 % bonus až 450 € a 250 free spinů, sportovní bonus je 100 % až 200 € na první sázku.",
            "bonuses": [
                {"title": "Kasino bonus", "value": "+100%", "detail": "Až 450 €, x35"},
                {"title": "Free spiny", "value": "250 FS", "detail": "Na vybrané sloty"},
                {"title": "Sport bonus", "value": "+100%", "detail": "Až 200 € freebet"},
                {"title": "Crypto cashback", "value": "10%", "detail": "Pro kryptoměnové vklady"}
            ],
            "weeklyPromo": "BDMBet pořádá týdenní slot turnaje, daily drops & wins s 1 000 000 € v cenách měsíčně, sportovní akumulátorové boosty, free bet pátky a víkendové reload bonusy.",
            "vipProgram": "BDM VIP Club má 5 úrovní s rostoucími výhodami – vyšší cashback (až 15 %), exkluzivní bonusy, free bety, narozeninové dárky a osobní VIP manažer od úrovně 3 výše.",
            "gamesIntro": "BDMBet nabízí přes 3 000 kasinových her a kompletní sportovní sekci s tisíci eventy denně.",
            "gamesSlots": "Více než 2 500 automatů od Pragmatic Play, NetEnt, Play'n GO, Hacksaw Gaming, Push Gaming a dalších. Klasické sloty, megaways, jackpoty.",
            "gamesTable": "Stolní hry – ruleta, blackjack, baccarat, poker, video poker. Limity sázek od 0,50 € do 5 000 €.",
            "gamesLive": "Live kasino od Evolution Gaming a Pragmatic Play Live. Crazy Time, Lightning Roulette, Mega Ball a desítky standardních stolů 24/7.",
            "gamesMini": "Crash games (Aviator, Spaceman), Plinko, Mines, Dice, Hi-Lo. Plus virtuální sporty a esports betting v sportovní sekci.",
            "paymentsIntro": "BDMBet podporuje hlavní platební metody se silným důrazem na kryptoměny. Výběry zpracovány do 24 hodin (kryptoměny okamžitě).",
            "paymentMethods": ["Visa", "Mastercard", "Skrill", "Neteller", "Bitcoin", "Ethereum", "USDT", "Litecoin", "MuchBetter", "Bankovní převod"],
            "paymentCount": 10,
            "providersIntro": "BDMBet spolupracuje s 50+ předními poskytovateli kasinových her a špičkovými dodavateli sportovních dat.",
            "providers": CORE_PROVIDERS + ['Habanero', 'Betsoft', 'Playson', 'Spinomenal', 'iSoftBet', 'Ezugi', 'Pragmatic Play Live'],
            "providerCount": 27,
            "advantages": [
                "Hybridní platforma – kasino i sportovní sázky na jednom účtu",
                "Silná podpora kryptoměn (Bitcoin, Ethereum, USDT, Litecoin)",
                "Štědrý balíček 100 % bonus + 250 free spinů",
                "Live betting na tisíce eventů denně",
                "Crypto cashback 10 % pro kryptoměnové vklady",
                "Plně česká platforma s 24/7 podporou"
            ],
            "pros": ["Kasino + sport", "4 kryptoměny", "250 FS uvítacích", "Live betting", "Crypto cashback", "České UI"],
            "cons": ["Curaçao licence", "Užší nabídka live kasina", "Mobilní web místo aplikace"],
            "supportText": "Zákaznická podpora BDMBet je dostupná 24/7 přes live chat a email (support@bdmbet.com). Plně v češtině. Live chat odpovídá obvykle do 3 minut.",
            "faq": [
                {"q": "Mohu platit kryptoměnami?", "a": "Ano, BDMBet podporuje Bitcoin, Ethereum, USDT a Litecoin s okamžitými vklady i výběry."},
                {"q": "Mám oddělené účty pro kasino a sport?", "a": "Ne, je to jeden hybridní účet – peníze můžete volně přesouvat mezi kasinem a sportem."},
                {"q": "Jak funguje crypto cashback?", "a": "Pokud platíte kryptoměnou, vrátí se vám 10 % z čistých ztrát týdně automaticky."},
                {"q": "Mají BDMBet live betting?", "a": "Ano, tisíce sportovních eventů denně s live sázením a streamingem."},
                {"q": "Jaký je minimální vklad?", "a": "20 € pro fiat měny i kryptoměny."}
            ],
            "finalVerdict": "BDMBet je ideální volba pro hráče, kteří chtějí kombinaci kasina a sportovních sázek s plnou podporou kryptoměn. Štědrý uvítací balíček 100 % + 250 FS, crypto cashback a live betting na tisíce eventů z něj činí jeden z nejlepších hybridních operátorů na trhu."
        }
    },
    # 5. Mafia Casino — dark theme
    {
        "id": "mafia-casino", "name": "Mafia Casino", "slug": "mafia-casino",
        "rating": 4.1,
        "bonus": "+100% až 500 € + 200 free spinů",
        "bonusAmount": "500 €", "wagering": "x35",
        "bonusUrl": AFF_BASE + "mafia-casino", "freeSpins": 200, "minDeposit": 20,
        "description": "Online kasino s atmosférou tajné podzemní herny a stylizovaným designem inspirovaným klasickými mafiánskými filmy.",
        "features": ["Stylový design", "200 FS", "VIP Family", "Live kasino"],
        "review": {
            "metaDescription": "Mafia Casino recenze 2026 – +100 % bonus až 500 € + 200 free spinů. Stylové online kasino s atmosférou podzemní herny.",
            "reviewCount": 234, "bonusAmount": "500 €", "freeSpinsCount": "200 FS",
            "withdrawalSpeed": "24-48h",
            "owner": "Mafia Gaming N.V.", "yearCreated": "2024",
            "license": "Curaçao", "withdrawalRange": "20 € – 30 000 €",
            "withdrawalSpeedDetail": "24-48 hodin", "czechLanguage": "Ano", "mobile": "Ano (web)",
            "introduction": "Mafia Casino je netradiční online kasino s temnou atmosférou inspirovanou klasickými mafiánskými filmy a underground hernami. Spuštěné v roce 2024 nabízí nejen unikátní stylizaci, ale také kvalitní herní katalog (přes 3 000 her) a štědrý uvítací bonus 100 % až 500 € + 200 free spinů. Tematický design se prolíná do celého rozhraní – VIP program se nazývá 'Family', turnaje 'Heists' a věrnostní úrovně mají jména po legendárních postavách. Kasino je plně lokalizované do češtiny a nabízí 24/7 podporu.",
            "bonusIntro": "Vstupte do Family stylovým bonusem – 100 % match na první vklad až 500 € plus 200 free spinů na vybrané sloty. Wagering x35 je férový pro takový balíček.",
            "bonuses": [
                {"title": "1. vklad", "value": "+100%", "detail": "Až 500 €, x35"},
                {"title": "Free spiny", "value": "200 FS", "detail": "Na Book of Dead"},
                {"title": "Reload Heist", "value": "75%", "detail": "Páteční reload"},
                {"title": "Family Cashback", "value": "12%", "detail": "Týdenní pro Family"}
            ],
            "weeklyPromo": "Mafia Casino pořádá weekly 'Heist' turnaje s prize poolem až 50 000 €, daily 'Hit Job' mise s odměnami v free spinech, páteční Family Reload bonusy a víkendové cashback eventy.",
            "vipProgram": "Mafia Family je věrnostní program s 6 úrovněmi pojmenovanými po slavných postavách (Soldier, Capo, Underboss, Boss, Don, Godfather). Postupem získáváte rostoucí cashback, exkluzivní bonusy, narozeninové dárky a osobního Consigliere (VIP manažera) od úrovně Capo výše.",
            "gamesIntro": "Mafia Casino nabízí přes 3 000 her od 40+ poskytovatelů s důrazem na temné, mafiánsky laděné a klasické sloty.",
            "gamesSlots": "Přes 2 500 automatů včetně tematických hitů (Goodfellas-style, Vegas), populárních titulů Pragmatic Play, NetEnt, Play'n GO a megaways slotů.",
            "gamesTable": "Stolní hry zahrnují ruletu, blackjack, baccarat a poker. K dispozici je i mafiánsky laděný 'Underground Poker' room s vyššími limity.",
            "gamesLive": "Live kasino od Evolution Gaming a Pragmatic Play Live – stylizované 'Speakeasy' VIP stoly, ruleta, blackjack, Crazy Time a další game shows.",
            "gamesMini": "Crash games (Aviator, Spaceman), Plinko, Mines a Dice. Plus exkluzivní 'Heist' tematické mini-hry s vlastními příběhy.",
            "paymentsIntro": "Mafia Casino podporuje hlavní platební metody. Výběry zpracovány do 24-48 hodin.",
            "paymentMethods": ["Visa", "Mastercard", "Skrill", "Neteller", "PaySafeCard", "Apple Pay", "Bitcoin", "USDT", "MuchBetter", "Bankovní převod"],
            "paymentCount": 10,
            "providersIntro": "Mafia Casino spolupracuje s 40+ předními poskytovateli her – kvalita Family je prioritou.",
            "providers": CORE_PROVIDERS + ['Habanero', 'Betsoft', 'Playson', 'iSoftBet', 'Pragmatic Play Live'],
            "providerCount": 25,
            "advantages": [
                "Unikátní stylizace mafiánské tematiky napříč celou platformou",
                "Štědrý uvítací bonus 100 % až 500 € + 200 free spinů",
                "Family VIP program s 6 úrovněmi a osobním Consigliere",
                "Týdenní 'Heist' turnaje s prize poolem až 50 000 €",
                "Podpora kryptoměn (Bitcoin, USDT)",
                "Plně česká platforma s 24/7 podporou"
            ],
            "pros": ["Tematický design", "200 FS uvítacích", "Family VIP program", "Heist turnaje", "Kryptoměny", "České UI"],
            "cons": ["Curaçao licence", "Tematický styl není pro každého", "Min. vklad 20 €"],
            "supportText": "Zákaznická podpora Mafia Casino je dostupná 24/7 přes live chat a email. Plně v češtině. Live chat odpovídá obvykle do 4 minut. Family členové mají prioritní podporu.",
            "faq": [
                {"q": "Co je Family VIP program?", "a": "6úrovňový věrnostní program s názvy postav (Soldier až Godfather). Vyšší úrovně získávají vyšší cashback a osobního Consigliere."},
                {"q": "Co jsou Heist turnaje?", "a": "Týdenní slot turnaje s tematickým názvem 'Heist' a prize poolem až 50 000 €."},
                {"q": "Mohu platit kryptoměnou?", "a": "Ano, Mafia Casino podporuje Bitcoin a USDT s okamžitými vklady."},
                {"q": "Je platforma vhodná pro začátečníky?", "a": "Ano, minimální vklad 20 € a wagering x35 je férový pro nové hráče."},
                {"q": "Jak rychle jsou výběry?", "a": "E-peněženky a kryptoměny do 24 hodin, karty a bankovní převody 24-48 hodin."}
            ],
            "finalVerdict": "Mafia Casino je stylová volba pro hráče, kteří hledají něco netradičního. Tematická stylizace inspirovaná světem mafiánských filmů, štědrý bonus 500 € + 200 FS a Family VIP program nabízí jedinečný zážitek. Vstupte do Family a užijte si hru s nádechem temného glamouru."
        }
    },
    # 6. Betify — sports betting focus
    {
        "id": "betify", "name": "Betify", "slug": "betify",
        "rating": 4.3,
        "bonus": "+100% až 1 000 € na sportovní sázky",
        "bonusAmount": "1 000 €", "wagering": "x30",
        "bonusUrl": AFF_BASE + "betify", "freeSpins": 0, "minDeposit": 20,
        "description": "Specializovaná sportovní sázková platforma s tisíci eventů denně, live streamingem a doplňkovou kasinovou nabídkou.",
        "features": ["Specialista na sport", "Live streaming", "Tisíce eventů denně", "Kasino"],
        "review": {
            "metaDescription": "Betify recenze 2026 – +100 % bonus až 1 000 € na sportovní sázky. Specializovaná sportovní platforma s live streamingem.",
            "reviewCount": 345, "bonusAmount": "1 000 €", "freeSpinsCount": "0",
            "withdrawalSpeed": "24h",
            "owner": "Betify Group", "yearCreated": "2023",
            "license": "Curaçao", "withdrawalRange": "20 € – 50 000 €",
            "withdrawalSpeedDetail": "Do 24 hodin", "czechLanguage": "Ano", "mobile": "Ano (web)",
            "introduction": "Betify je sportovní sázková platforma s vedlejší kasinovou sekcí, která vstoupila na trh v roce 2023. Zaměřuje se primárně na sportovní fanoušky a nabízí jednu z nejširších nabídek sportovních eventů – tisíce zápasů denně z více než 30 sportů včetně fotbalu, tenisu, hokeje, basketbalu, esportu a virtuálních sportů. Klíčovými přednostmi jsou live betting s in-play streamingem, kompetitivní kurzy a uvítací bonus 100 % až 1 000 € specificky pro sportovní sázky. Kasinová sekce s 1 500+ hrami slouží jako doplněk pro hráče, kteří chtějí občasnou změnu.",
            "bonusIntro": "Betify se primárně zaměřuje na sport, takže uvítací bonus je freebet – 100 % match na první sázku až do 1 000 €. Wagering x30 je nutno protočit na sázkách s kurzem 1.50+.",
            "bonuses": [
                {"title": "Sport bonus", "value": "+100%", "detail": "Až 1 000 € freebet, x30"},
                {"title": "Akumulátor boost", "value": "+10–50%", "detail": "Pro 5+ tipů"},
                {"title": "Cashback sport", "value": "10%", "detail": "Týdenní pro sport"},
                {"title": "Casino bonus", "value": "+50%", "detail": "Až 200 € pro kasino"}
            ],
            "weeklyPromo": "Betify pořádá speciální akce na největší sportovní eventy – Champions League, NBA, NHL playoffs, tenisové grandslamy. Pravidelné akumulátorové boosty, free bet pátky, cashback víkendy a virtuální sport turnaje.",
            "vipProgram": "Betify Pro Club má 5 úrovní pro nejaktivnější sázkaře. Členové získají vyšší cashback (až 15 %), free bety, exkluzivní akumulátorové boosty, osobního VIP manažera a vyšší limity na sázky.",
            "gamesIntro": "Betify nabízí jeden z nejširších sportovních katalogů (30+ sportů, tisíce eventů denně) plus 1 500+ kasinových her jako doplněk.",
            "gamesSlots": "Více než 1 200 automatů od Pragmatic Play, NetEnt, Play'n GO a dalších. Důraz na populární tituly a sport-tematizované sloty.",
            "gamesTable": "Stolní hry – ruleta, blackjack, baccarat, poker. Limity od 1 € do 2 500 €.",
            "gamesLive": "Live kasino od Evolution Gaming – ruleta, blackjack, baccarat a populární game shows. Plus live streaming sportovních eventů přímo v platformě.",
            "gamesMini": "Aviator, Plinko, Dice a virtuální sporty (fotbal, koně, greyhoundy, motorky). Esports betting na CS:GO, LoL, Dota 2 a další.",
            "paymentsIntro": "Betify podporuje hlavní platební metody. Výběry zpracovány do 24 hodin.",
            "paymentMethods": ["Visa", "Mastercard", "Skrill", "Neteller", "PaySafeCard", "Apple Pay", "Bitcoin", "MuchBetter", "Bankovní převod"],
            "paymentCount": 9,
            "providersIntro": "Betify spolupracuje se špičkovými poskytovateli sportovních dat (BetRadar, SportRadar) a 30+ kasinovými studii.",
            "providers": CORE_PROVIDERS + ['Habanero', 'Betsoft', 'Playson', 'iSoftBet'],
            "providerCount": 24,
            "advantages": [
                "Specializace na sport – tisíce eventů denně z 30+ sportů",
                "Live betting s in-play streamingem zdarma",
                "Esports a virtuální sporty pro non-stop akci",
                "Akumulátorové boosty až +50 % pro 5+ tipů",
                "Štědrý sport freebet 100 % až 1 000 €",
                "Plně česká platforma s 24/7 podporou"
            ],
            "pros": ["Specialista na sport", "Live streaming", "Esports + virtual", "Akumulátor boosty", "Live betting", "Plně česky"],
            "cons": ["Žádné free spiny v uvítacím", "Užší kasinová nabídka", "Curaçao licence"],
            "supportText": "Zákaznická podpora Betify je dostupná 24/7 přes live chat a email. Tým má specializované znalosti sportovních sázek. Live chat odpovídá obvykle do 3 minut, plně v češtině.",
            "faq": [
                {"q": "Mohu sázet na živé eventy?", "a": "Ano, Betify nabízí live betting na tisíce eventů denně s integrovaným streamingem."},
                {"q": "Co je akumulátorový boost?", "a": "Pokud máte 5 a více tipů v jednom tiketu, váš výhrnek je navýšen o 10–50 % v závislosti na počtu tipů."},
                {"q": "Sázíte na esports?", "a": "Ano, populární disciplíny jako CS:GO, LoL, Dota 2, Valorant, Overwatch a další."},
                {"q": "Mohu sázet z mobilu?", "a": "Ano, mobilní web je plně responzivní a optimalizovaný pro sázení v cestě."},
                {"q": "Jaké jsou limity sázek?", "a": "Od 0,50 € do 5 000 € na tiket pro standardní hráče, VIP klienti mají vyšší limity."}
            ],
            "finalVerdict": "Betify je top volba pro fanoušky sportu. S tisíci eventů denně, live streamingem, esports sekcí a štědrým freebet bonusem 1 000 € patří mezi nejatraktivnější sportovní platformy na trhu. Pokud hledáte specializovanou sportovní platformu s českou podporou, Betify nabízí všechno, co potřebujete."
        }
    },
    # 7. Spinsy — bright slots theme
    {
        "id": "spinsy", "name": "Spinsy", "slug": "spinsy",
        "rating": 4.2,
        "bonus": "+100% až 500 € + 200 free spinů",
        "bonusAmount": "500 €", "wagering": "x35",
        "bonusUrl": AFF_BASE + "spinsy", "freeSpins": 200, "minDeposit": 20,
        "description": "Barevné a hravé online kasino s důrazem na zábavu, denní mise a 200 free spinů v uvítacím balíčku.",
        "features": ["Hravé UI", "200 FS", "Daily missions", "3 000+ her"],
        "review": {
            "metaDescription": "Spinsy recenze 2026 – +100 % bonus až 500 € + 200 free spinů. Barevné kasino s denními misemi a gamifikací.",
            "reviewCount": 178, "bonusAmount": "500 €", "freeSpinsCount": "200 FS",
            "withdrawalSpeed": "24h",
            "owner": "Spinsy Gaming Ltd.", "yearCreated": "2024",
            "license": "Curaçao", "withdrawalRange": "20 € – 25 000 €",
            "withdrawalSpeedDetail": "Do 24 hodin", "czechLanguage": "Ano", "mobile": "Ano (web)",
            "introduction": "Spinsy je barevné a hravé online kasino, které vstoupilo na trh v roce 2024 s důrazem na pozitivní atmosféru, jednoduchost a gamifikaci. Růžovo-fialový design, jasné ikony a intuitivní rozhraní z něj činí ideální volbu pro hráče, kteří chtějí kasino bez zbytečného balastu. Nabízí přes 3 000 her od 40+ poskytovatelů, denní mise s odměnami a štědrý uvítací bonus 100 % až 500 € + 200 free spinů. Spinsy je plně lokalizované do češtiny a podporuje 24/7 zákaznickou podporu.",
            "bonusIntro": "Spinsy láká nové hráče přívětivým uvítacím balíčkem – 100 % bonus na první vklad až 500 € + 200 free spinů. Wagering x35 je standardní a férový.",
            "bonuses": [
                {"title": "1. vklad", "value": "+100%", "detail": "Až 500 €, x35"},
                {"title": "Free spiny", "value": "200 FS", "detail": "Po 20 FS denně"},
                {"title": "Reload bonus", "value": "50%", "detail": "Páteční až 200 €"},
                {"title": "Cashback", "value": "10%", "detail": "Týdenní vrácení"}
            ],
            "weeklyPromo": "Spinsy pořádá daily missions s odměnami v free spinech, weekly slot turnaje s prize poolem 25 000 €, páteční reload bonusy a víkendové cashback akce. Plus speciální 'Spinsy Drops' s náhodnými výhrami pro aktivní hráče.",
            "vipProgram": "Spinsy Loyalty Club má 5 úrovní s rostoucími výhodami – vyšší cashback, exkluzivní free spiny, narozeninové dárky a od úrovně 4 osobní VIP manažer.",
            "gamesIntro": "Spinsy nabízí přes 3 000 her od 40+ poskytovatelů. Důraz na nejnovější sloty a populární hity.",
            "gamesSlots": "Více než 2 500 automatů od Pragmatic Play, NetEnt, Play'n GO, Hacksaw Gaming, Push Gaming a dalších. Klasické sloty, megaways, jackpoty.",
            "gamesTable": "Stolní hry – ruleta, blackjack, baccarat, poker. Limity od 0,50 € do 2 500 €.",
            "gamesLive": "Live kasino od Evolution Gaming a Pragmatic Play Live. Crazy Time, Lightning Roulette, Mega Ball a desítky standardních stolů.",
            "gamesMini": "Crash games (Aviator, Spaceman), Plinko, Mines, Dice a Hi-Lo. Plus exkluzivní Spinsy mini-hry s gamifikací.",
            "paymentsIntro": "Spinsy podporuje hlavní platební metody. Výběry zpracovány do 24 hodin.",
            "paymentMethods": ["Visa", "Mastercard", "Skrill", "Neteller", "PaySafeCard", "Apple Pay", "Bitcoin", "MuchBetter", "Bankovní převod"],
            "paymentCount": 9,
            "providersIntro": "Spinsy spolupracuje s 40+ poskytovateli her, kteří garantují kvalitu a férovost.",
            "providers": CORE_PROVIDERS + ['Habanero', 'Betsoft', 'Playson', 'iSoftBet'],
            "providerCount": 24,
            "advantages": [
                "Hravé a barevné rozhraní s pozitivní atmosférou",
                "Daily missions s odměnami v free spinech",
                "Štědrý uvítací bonus 500 € + 200 FS",
                "Více než 3 000 her od 40+ poskytovatelů",
                "Cashback 10 % týdně",
                "Plně česká platforma s 24/7 podporou"
            ],
            "pros": ["Hravý design", "200 FS uvítacích", "Daily missions", "Cashback týdně", "3 000+ her", "Plně česky"],
            "cons": ["Curaçao licence", "Bez nativní mobilní aplikace", "Min. vklad 20 €"],
            "supportText": "Zákaznická podpora Spinsy je dostupná 24/7 přes live chat a email. Plně v češtině. Live chat odpovídá obvykle do 3 minut.",
            "faq": [
                {"q": "Co jsou daily missions?", "a": "Denní úkoly (např. odehrát 20 spinů, vyhrát na live ruletě) s odměnami ve free spinech nebo bonusech."},
                {"q": "Jak jsou rozděleny free spiny?", "a": "200 FS dostáváte po 20 FS denně po dobu 10 dnů – pravidelný přísun zábavy."},
                {"q": "Mohu platit kryptoměnou?", "a": "Ano, Spinsy podporuje Bitcoin s okamžitými vklady."},
                {"q": "Je platforma vhodná pro začátečníky?", "a": "Ano, intuitivní rozhraní, nízký vklad 20 € a hravý styl jsou přívětivé pro nové hráče."},
                {"q": "Jak rychle jsou výběry?", "a": "E-peněženky a kryptoměny do 24 hodin, karty a bankovní převody 1–3 dny."}
            ],
            "finalVerdict": "Spinsy je přívětivá volba pro hráče, kteří hledají hravé a jednoduché kasino bez zbytečné komplikovanosti. Daily missions, 200 free spinů uvítacích a moderní rozhraní z něj činí skvělou platformu pro každodenní zábavu. Pokud chcete kasino, kde se cítíte vítáni, Spinsy je jasná volba."
        }
    },
    # 8. Cashed — crash games focus
    {
        "id": "cashed", "name": "Cashed", "slug": "cashed",
        "rating": 4.3,
        "bonus": "+100% až 500 € + 200 free spinů",
        "bonusAmount": "500 €", "wagering": "x35",
        "bonusUrl": AFF_BASE + "cashed", "freeSpins": 200, "minDeposit": 20,
        "description": "Specializované kasino zaměřené na crash games (Aviator, JetX, Spaceman) s nejširší nabídkou těchto rychlých her na trhu.",
        "features": ["Crash games specialista", "Aviator + 50 dalších", "Live multiplayer", "Tournament leaderboards"],
        "review": {
            "metaDescription": "Cashed casino recenze 2026 – +100 % bonus až 500 € + 200 free spinů. Specialista na crash games (Aviator, JetX, Spaceman).",
            "reviewCount": 198, "bonusAmount": "500 €", "freeSpinsCount": "200 FS",
            "withdrawalSpeed": "24h",
            "owner": "Cashed Group", "yearCreated": "2024",
            "license": "Curaçao", "withdrawalRange": "20 € – 30 000 €",
            "withdrawalSpeedDetail": "Do 24 hodin", "czechLanguage": "Ano", "mobile": "Ano (web)",
            "introduction": "Cashed je unikátní specializované kasino, které vstoupilo na trh v roce 2024 s primárním zaměřením na crash games – kategorii rychlých multiplayer her, kterou pomohl popularizovat slavný Aviator. Cashed nabízí jednu z nejširších kolekcí těchto her na trhu (50+ titulů včetně Aviator, JetX, Spaceman, Plinko, Mines, Dice a dalších), doplněnou kompletní kasinovou nabídkou s 2 500+ sloty, stolními hrami a live kasinem. Klíčovou předností jsou multiplayer turnaje, denní leaderboardy s odměnami a komunita vášnivých crash hráčů.",
            "bonusIntro": "Cashed vítá nové hráče bonusem 100 % až 500 € + 200 free spinů. Bonus lze použít i na crash games – Aviator a JetX přispívají 50 % k wagering požadavkům.",
            "bonuses": [
                {"title": "1. vklad", "value": "+100%", "detail": "Až 500 €, x35"},
                {"title": "Free spiny", "value": "200 FS", "detail": "Na vybrané sloty"},
                {"title": "Crash bonus", "value": "+50%", "detail": "Pro hraní crash games"},
                {"title": "Cashback", "value": "12%", "detail": "Týdenní pro crash"}
            ],
            "weeklyPromo": "Cashed pořádá denní crash turnaje s prize poolem 5 000 €, weekly leaderboard s top 100 hráči, speciální Aviator akce, JetX víkendové výzvy a měsíční Hall of Fame s nejvyššími multiplikátory.",
            "vipProgram": "Cashed VIP Multiplier má 6 úrovní inspirovaných crash multiplikátory (1.5x až 50x). Každá úroveň přidává vyšší cashback, exkluzivní bonusy a osobního VIP manažera od úrovně 10x výše.",
            "gamesIntro": "Cashed nabízí největší výběr crash games na trhu (50+) a kompletní kasinovou nabídku s 2 500+ tituly.",
            "gamesSlots": "Přes 2 000 automatů od Pragmatic Play, NetEnt, Play'n GO a dalších. Doplňková nabídka pro hráče, kteří si chtějí odpočinout od crash games.",
            "gamesTable": "Standardní nabídka stolních her – ruleta, blackjack, baccarat, poker.",
            "gamesLive": "Live kasino od Evolution Gaming s ruletou, blackjackem, baccaratem a populárními game shows.",
            "gamesMini": "Hlavní specialita – přes 50 crash games včetně Aviator, JetX, Spaceman, Plinko, Mines, Dice, Hi-Lo, Crash Royale, Cap'n Crash a dalších od Spribe, Turbo Games, BGaming, SmartSoft Gaming a dalších.",
            "paymentsIntro": "Cashed podporuje hlavní platební metody. Výběry zpracovány do 24 hodin (kryptoměny okamžitě).",
            "paymentMethods": ["Visa", "Mastercard", "Skrill", "Neteller", "Bitcoin", "Ethereum", "USDT", "MuchBetter", "Apple Pay", "Bankovní převod"],
            "paymentCount": 10,
            "providersIntro": "Cashed spolupracuje se všemi předními poskytovateli crash games i klasických kasinových studií.",
            "providers": CORE_PROVIDERS + ['Habanero', 'Betsoft', 'Playson', 'Spinomenal', 'Pragmatic Play Live'],
            "providerCount": 25,
            "advantages": [
                "Největší výběr crash games v Evropě (50+ titulů)",
                "Denní turnaje s prize poolem 5 000 €",
                "Multiplayer atmosféra s live leaderboardy",
                "VIP Multiplier program inspirovaný crash hrami",
                "Podpora kryptoměn (Bitcoin, Ethereum, USDT)",
                "Plně česká platforma s 24/7 podporou"
            ],
            "pros": ["50+ crash games", "Denní turnaje", "Live leaderboardy", "Kryptoměny", "Multiplayer", "Plně česky"],
            "cons": ["Užší fokus (crash > sloty)", "Curaçao licence", "Bez sportovních sázek"],
            "supportText": "Zákaznická podpora Cashed je dostupná 24/7 přes live chat a email. Tým má specializované znalosti crash games. Live chat odpovídá obvykle do 3 minut, plně v češtině.",
            "faq": [
                {"q": "Kolik crash games nabízíte?", "a": "Více než 50 titulů včetně Aviator, JetX, Spaceman, Plinko, Mines a dalších."},
                {"q": "Jsou crash games férové?", "a": "Ano, všechny crash games používají Provably Fair technologii – výsledek lze ověřit."},
                {"q": "Co je VIP Multiplier?", "a": "Náš věrnostní program s 6 úrovněmi pojmenovanými po crash multiplikátorech (1.5x až 50x)."},
                {"q": "Mohu hrát multiplayer Aviator?", "a": "Ano, Aviator a další crash games jsou multiplayer s live leaderboardem."},
                {"q": "Jak rychlé jsou výběry?", "a": "E-peněženky a kryptoměny do 24 hodin, karty 1–3 dny."}
            ],
            "finalVerdict": "Cashed je rájem pro fanoušky crash games. S 50+ tituly, denními turnaji, live leaderboardy a unikátním VIP Multiplier programem nabízí specialistický zážitek, který nikde jinde nenajdete. Pokud milujete Aviator, JetX nebo Spaceman, Cashed je jasná volba."
        }
    },
    # 9. Spinbara — modern slots
    {
        "id": "spinbara", "name": "Spinbara", "slug": "spinbara",
        "rating": 4.1,
        "bonus": "+100% až 500 € + 200 free spinů",
        "bonusAmount": "500 €", "wagering": "x35",
        "bonusUrl": AFF_BASE + "spinbara", "freeSpins": 200, "minDeposit": 20,
        "description": "Moderní online kasino s minimalistickým designem, prémiovým výběrem nejnovějších slotů a rychlou platformou.",
        "features": ["Minimalistický design", "Nejnovější sloty", "Rychlá platforma", "200 FS"],
        "review": {
            "metaDescription": "Spinbara casino recenze 2026 – +100 % bonus až 500 € + 200 free spinů. Moderní kasino s minimalistickým designem.",
            "reviewCount": 156, "bonusAmount": "500 €", "freeSpinsCount": "200 FS",
            "withdrawalSpeed": "24h",
            "owner": "Spinbara Ltd.", "yearCreated": "2024",
            "license": "Curaçao", "withdrawalRange": "20 € – 25 000 €",
            "withdrawalSpeedDetail": "Do 24 hodin", "czechLanguage": "Ano", "mobile": "Ano (web)",
            "introduction": "Spinbara je moderní online kasino s elegantním minimalistickým designem, které vstoupilo na trh v roce 2024. Jeho silnou stránkou je čistota uživatelského rozhraní, rychlost načítání a kurátorovaný výběr nejnovějších slotů od top studií. S přes 2 800 hrami od 35+ poskytovatelů, štědrým uvítacím bonusem 100 % až 500 € + 200 free spinů a 24/7 podporou v češtině je Spinbara skvělou volbou pro hráče, kteří preferují kvalitu před kvantitou.",
            "bonusIntro": "Spinbara nabízí klasický férový uvítací balíček – 100 % bonus na první vklad až 500 € + 200 free spinů s wagering x35.",
            "bonuses": [
                {"title": "1. vklad", "value": "+100%", "detail": "Až 500 €, x35"},
                {"title": "Free spiny", "value": "200 FS", "detail": "Po 25 FS denně 8 dní"},
                {"title": "Reload weekend", "value": "60%", "detail": "Sobota a neděle"},
                {"title": "Cashback", "value": "10%", "detail": "Týdenní vrácení"}
            ],
            "weeklyPromo": "Spinbara pořádá weekly slot turnaje s prize poolem 20 000 €, daily 'New Game' free spiny na nejnovější releasy, víkendové reload bonusy a měsíční jackpot drops.",
            "vipProgram": "Spinbara Elite má 5 úrovní pro nejaktivnější hráče. Členové získají vyšší cashback, exkluzivní free spin balíčky, narozeninové dárky a osobní VIP manažer od úrovně 4.",
            "gamesIntro": "Spinbara nabízí přes 2 800 her od 35+ poskytovatelů. Důraz na nejnovější releasy a kvalitu.",
            "gamesSlots": "Více než 2 300 automatů od Pragmatic Play, NetEnt, Play'n GO, Hacksaw Gaming, Push Gaming, Nolimit City a dalších. Nejnovější releasy obvykle dostupné v den vydání.",
            "gamesTable": "Stolní hry – ruleta, blackjack, baccarat, poker s limity od 0,50 € do 2 500 €.",
            "gamesLive": "Live kasino od Evolution Gaming a Pragmatic Play Live – klasické stoly i moderní game shows jako Crazy Time a Mega Ball.",
            "gamesMini": "Crash games (Aviator, Spaceman), Plinko, Mines a Dice od Spribe a Turbo Games.",
            "paymentsIntro": "Spinbara podporuje hlavní platební metody. Výběry zpracovány do 24 hodin.",
            "paymentMethods": ["Visa", "Mastercard", "Skrill", "Neteller", "PaySafeCard", "Apple Pay", "Bitcoin", "USDT", "MuchBetter", "Bankovní převod"],
            "paymentCount": 10,
            "providersIntro": "Spinbara spolupracuje s 35+ předními poskytovateli her – kvalita je prioritou.",
            "providers": CORE_PROVIDERS + ['Habanero', 'Betsoft', 'Playson', 'Spinomenal'],
            "providerCount": 24,
            "advantages": [
                "Elegantní minimalistický design s rychlým načítáním",
                "Kurátorovaný výběr nejnovějších slotů",
                "Štědrý uvítací bonus 500 € + 200 FS",
                "Daily 'New Game' free spiny na nejnovější tituly",
                "Podpora kryptoměn (Bitcoin, USDT)",
                "Plně česká platforma s 24/7 podporou"
            ],
            "pros": ["Moderní design", "Nejnovější sloty", "200 FS uvítacích", "Rychlé výběry 24h", "Kryptoměny", "Plně česky"],
            "cons": ["Curaçao licence", "Užší celkový katalog (2 800)", "Bez sportovních sázek"],
            "supportText": "Zákaznická podpora Spinbara je dostupná 24/7 přes live chat a email. Plně v češtině. Live chat odpovídá obvykle do 3 minut.",
            "faq": [
                {"q": "Jaký design má Spinbara?", "a": "Moderní minimalistický s tmavým módem, čistými ikonami a rychlým načítáním."},
                {"q": "Kolik slotů nabízíte?", "a": "Více než 2 300 automatů od 30+ studií, včetně nejnovějších releasů."},
                {"q": "Mohu platit kryptoměnou?", "a": "Ano, Spinbara podporuje Bitcoin a USDT s okamžitými vklady."},
                {"q": "Jak rychlé jsou výběry?", "a": "E-peněženky a kryptoměny do 24 hodin, karty a bankovní převody 1–3 dny."},
                {"q": "Mají daily promotions?", "a": "Ano, daily 'New Game' free spiny na nejnovější releasy a další denní akce."}
            ],
            "finalVerdict": "Spinbara je elegantní volba pro hráče, kteří hledají moderní kasino s důrazem na kvalitu. Minimalistický design, kurátorovaný výběr nejnovějších slotů a férový uvítací bonus 500 € + 200 FS z něj činí skvělou platformu pro náročné hráče."
        }
    },
    # 10. BetRiot — energetic
    {
        "id": "betriot", "name": "BetRiot", "slug": "betriot",
        "rating": 4.2,
        "bonus": "+100% až 500 € + 200 free spinů",
        "bonusAmount": "500 €", "wagering": "x35",
        "bonusUrl": AFF_BASE + "betriot", "freeSpins": 200, "minDeposit": 20,
        "description": "Energická a divoká online kasino platforma s živým designem, agresivním marketingem a štědrými bonusy.",
        "features": ["Energický design", "Tournaments", "200 FS", "Live kasino"],
        "review": {
            "metaDescription": "BetRiot recenze 2026 – +100 % bonus až 500 € + 200 free spinů. Energická online kasino platforma s živým designem.",
            "reviewCount": 234, "bonusAmount": "500 €", "freeSpinsCount": "200 FS",
            "withdrawalSpeed": "24-48h",
            "owner": "BetRiot N.V.", "yearCreated": "2024",
            "license": "Curaçao", "withdrawalRange": "20 € – 30 000 €",
            "withdrawalSpeedDetail": "24-48 hodin", "czechLanguage": "Ano", "mobile": "Ano (web)",
            "introduction": "BetRiot je energická online kasino platforma s živým oranžovo-červeným designem, která vstoupila na trh v roce 2024. Cílí na mladší publikum, sportovní fanoušky a hráče, kteří hledají dynamickou atmosféru. Nabízí přes 3 000 her od 40+ poskytovatelů, štědrý uvítací balíček 100 % až 500 € + 200 free spinů, sportovní sekci s tisíci eventů denně a 24/7 podporu v češtině.",
            "bonusIntro": "BetRiot vítá nové hráče divokým balíčkem – 100 % bonus na první vklad až 500 € + 200 free spinů. Wagering x35 je standardní.",
            "bonuses": [
                {"title": "1. vklad", "value": "+100%", "detail": "Až 500 €, x35"},
                {"title": "Free spiny", "value": "200 FS", "detail": "Na vybrané sloty"},
                {"title": "Sport bonus", "value": "+50%", "detail": "Až 100 € freebet"},
                {"title": "Riot Cashback", "value": "10%", "detail": "Týdenní vrácení"}
            ],
            "weeklyPromo": "BetRiot pořádá weekly 'Riot Tournament' s prize poolem 30 000 €, daily missions s odměnami v free spinech, sportovní akumulátorové boosty a měsíční eventy s exkluzivními cenami.",
            "vipProgram": "Riot Squad VIP má 6 úrovní s rostoucími výhodami – vyšší cashback, exkluzivní bonusy, narozeninové dárky a osobní VIP manažer od úrovně 4.",
            "gamesIntro": "BetRiot nabízí přes 3 000 kasinových her plus kompletní sportovní sekci pro fanoušky sázení.",
            "gamesSlots": "Více než 2 500 automatů od Pragmatic Play, NetEnt, Play'n GO, Hacksaw Gaming a dalších. Důraz na populární tituly a megaways sloty.",
            "gamesTable": "Stolní hry – ruleta, blackjack, baccarat, poker. Limity od 0,50 € do 3 000 €.",
            "gamesLive": "Live kasino od Evolution Gaming a Pragmatic Play Live – ruleta, blackjack, Crazy Time, Mega Ball a další game shows 24/7.",
            "gamesMini": "Crash games (Aviator, Spaceman, JetX), Plinko, Mines a Dice. Plus virtuální sporty a esports betting.",
            "paymentsIntro": "BetRiot podporuje hlavní platební metody. Výběry zpracovány do 24-48 hodin.",
            "paymentMethods": ["Visa", "Mastercard", "Skrill", "Neteller", "PaySafeCard", "Apple Pay", "Bitcoin", "USDT", "MuchBetter", "Bankovní převod"],
            "paymentCount": 10,
            "providersIntro": "BetRiot spolupracuje s 40+ poskytovateli her, kteří garantují kvalitu a férovost.",
            "providers": CORE_PROVIDERS + ['Habanero', 'Betsoft', 'Playson', 'iSoftBet', 'Pragmatic Play Live'],
            "providerCount": 25,
            "advantages": [
                "Energický a živý design s pozitivní atmosférou",
                "Hybridní platforma kasino + sport",
                "Štědrý uvítací bonus 500 € + 200 FS",
                "Riot Tournament s prize poolem 30 000 € týdně",
                "Podpora kryptoměn (Bitcoin, USDT)",
                "Plně česká platforma s 24/7 podporou"
            ],
            "pros": ["Hybrid kasino + sport", "200 FS uvítacích", "Riot Tournaments", "Kryptoměny", "Daily missions", "Plně česky"],
            "cons": ["Curaçao licence", "Výběry až 48h", "Tematický styl není pro každého"],
            "supportText": "Zákaznická podpora BetRiot je dostupná 24/7 přes live chat a email. Plně v češtině. Live chat odpovídá obvykle do 4 minut.",
            "faq": [
                {"q": "Co je Riot Tournament?", "a": "Týdenní slot turnaj s prize poolem 30 000 € a top 200 hráči v žebříčku."},
                {"q": "Mohu sázet na sport?", "a": "Ano, BetRiot je hybridní platforma s plnou sportovní sázkovou kanceláří."},
                {"q": "Mohu platit kryptoměnou?", "a": "Ano, Bitcoin a USDT jsou podporovány s okamžitými vklady."},
                {"q": "Jaké jsou Daily missions?", "a": "Denní úkoly (např. odehrát X spinů, vyhrát na live ruletě) s odměnami v free spinech nebo bonusech."},
                {"q": "Jak rychlé jsou výběry?", "a": "E-peněženky a kryptoměny do 24 hodin, karty a bankovní převody 24-48 hodin."}
            ],
            "finalVerdict": "BetRiot je energická volba pro hráče, kteří chtějí dynamickou atmosféru a hybridní platformu kasino + sport. Štědrý uvítací bonus 500 € + 200 FS, Riot Tournament a daily missions z něj činí skvělou platformu pro každodenní zábavu. Pokud hledáte něco živého a moderního, BetRiot je jasná volba."
        }
    },
    # 11. Casinozer — French-style brand
    {
        "id": "casinozer", "name": "Casinozer", "slug": "casinozer",
        "rating": 4.4,
        "bonus": "+100% až 500 € s nízkým wagering",
        "bonusAmount": "500 €", "wagering": "x35",
        "bonusUrl": AFF_BASE + "casinozer", "freeSpins": 0, "minDeposit": 20,
        "description": "Etablované online kasino s francouzským stylem, prémiovým živým kasinem a sportovní sázkovou kanceláří.",
        "features": ["Francouzský styl", "Prémiové live", "Sport + kasino", "Etablovaná značka"],
        "review": {
            "metaDescription": "Casinozer recenze 2026 – +100 % bonus až 500 €. Etablované online kasino s francouzským stylem a prémiovým živým kasinem.",
            "reviewCount": 567, "bonusAmount": "500 €", "freeSpinsCount": "0",
            "withdrawalSpeed": "24h",
            "owner": "Casinozer Group", "yearCreated": "2023",
            "license": "Curaçao", "withdrawalRange": "20 € – 50 000 €",
            "withdrawalSpeedDetail": "Do 24 hodin", "czechLanguage": "Ano", "mobile": "Ano (web)",
            "introduction": "Casinozer je etablované online kasino se silným francouzským stylem, které vstoupilo na trh v roce 2023 a rychle si získalo loajální základnu hráčů. Nabízí prémiové živé kasino, kompletní sportovní sázkovou kancelář a přes 3 500 kasinových her od 50+ předních poskytovatelů. Klíčovými přednostmi jsou kvalitní lokalizace (včetně češtiny), elegantní design ve francouzském stylu a štědrý uvítací bonus 100 % až 500 €. Casinozer cílí na zkušené hráče a fanoušky live kasina.",
            "bonusIntro": "Casinozer vítá nové hráče klasickým balíčkem – 100 % bonus na první vklad až 500 €. Wagering x35 je férový a bonus lze použít na všechny hry kromě jackpotových slotů.",
            "bonuses": [
                {"title": "1. vklad", "value": "+100%", "detail": "Až 500 €, x35"},
                {"title": "2. vklad", "value": "+50%", "detail": "Až 300 €"},
                {"title": "Sport bonus", "value": "+100%", "detail": "Až 100 € freebet"},
                {"title": "Cashback VIP", "value": "15%", "detail": "Týdenní pro VIP"}
            ],
            "weeklyPromo": "Casinozer pořádá weekly slot turnaje s prize poolem 40 000 €, daily live kasino challenges, páteční reload bonusy 50 % a měsíční sportovní eventy s vylepšenými kurzy.",
            "vipProgram": "Casinozer Élite je VIP program s 6 úrovněmi pojmenovanými po francouzských karetních hodnotách (od As po Roi). Vyšší úrovně získávají vyšší cashback, exkluzivní bonusy, osobního VIP manažera a pozvánky na luxusní eventy.",
            "gamesIntro": "Casinozer nabízí přes 3 500 kasinových her od 50+ poskytovatelů plus kompletní sportovní sázkovou kancelář.",
            "gamesSlots": "Více než 3 000 automatů od Pragmatic Play, NetEnt, Play'n GO, Microgaming, Yggdrasil, Red Tiger a dalších. Klasické sloty, megaways, jackpoty.",
            "gamesTable": "Široká nabídka stolních her – ruleta evropská/francouzská/americká, blackjack, baccarat, poker, video poker. Vysoké limity pro pokročilé hráče.",
            "gamesLive": "Prémiové živé kasino od Evolution Gaming, Pragmatic Play Live, Authentic Gaming a Ezugi. Francouzská ruleta s českými dealery v primárním čase.",
            "gamesMini": "Crash games (Aviator, Spaceman), Plinko, Mines a Dice. Plus virtuální sporty (fotbal, koně, motorky) v sportovní sekci.",
            "paymentsIntro": "Casinozer podporuje hlavní platební metody. Výběry zpracovány do 24 hodin.",
            "paymentMethods": ["Visa", "Mastercard", "Skrill", "Neteller", "PaySafeCard", "Apple Pay", "Bitcoin", "MuchBetter", "Bankovní převod"],
            "paymentCount": 9,
            "providersIntro": "Casinozer spolupracuje s 50+ předními poskytovateli her – francouzský důraz na kvalitu a eleganci.",
            "providers": CORE_PROVIDERS + ['Habanero', 'Betsoft', 'Playson', 'iSoftBet', 'Pragmatic Play Live', 'Authentic Gaming', 'Ezugi'],
            "providerCount": 27,
            "advantages": [
                "Etablovaná značka s francouzským stylem a 2 lety na trhu",
                "Prémiové živé kasino s českými dealery",
                "Hybridní platforma kasino + sport",
                "Élite VIP program se 6 úrovněmi",
                "Štědrý uvítací bonus 500 € + reload",
                "Plně česká platforma s 24/7 podporou"
            ],
            "pros": ["Etablovaná značka", "Francouzský styl", "Prémiové live kasino", "Sport + kasino", "České dealery", "Plně česky"],
            "cons": ["Bez free spinů v uvítacím", "Curaçao licence", "Bez nativní mobilní aplikace"],
            "supportText": "Zákaznická podpora Casinozer je dostupná 24/7 přes live chat, email a telefon. Plně v češtině. Live chat odpovídá obvykle do 2 minut.",
            "faq": [
                {"q": "Mají Casinozer české dealery?", "a": "Ano, francouzská ruleta a blackjack mají české dealery v primárním čase (18-24h)."},
                {"q": "Mohu sázet na sport?", "a": "Ano, Casinozer je hybridní platforma s plnou sportovní sázkovou kanceláří."},
                {"q": "Co je Élite VIP program?", "a": "6úrovňový věrnostní program s francouzskými názvy karetních hodnot. Vyšší úrovně získávají vyšší cashback a osobního manažera."},
                {"q": "Mohu platit kryptoměnou?", "a": "Ano, Bitcoin je podporován s okamžitými vklady."},
                {"q": "Jak rychlé jsou výběry?", "a": "E-peněženky a kryptoměny do 24 hodin, karty a bankovní převody 1–3 dny."}
            ],
            "finalVerdict": "Casinozer je elegantní volba pro hráče, kteří hledají etablovanou značku s francouzským stylem a kvalitním živým kasinem. Prémiové stoly s českými dealery, Élite VIP program a hybridní platforma kasino + sport z něj činí všestrannou nabídku pro náročné hráče."
        }
    },
    # 12. Rabona Casino — football theme
    {
        "id": "rabona-casino", "name": "Rabona Casino", "slug": "rabona-casino",
        "rating": 4.3,
        "bonus": "+100% až 500 € + 200 free spinů",
        "bonusAmount": "500 €", "wagering": "x35",
        "bonusUrl": AFF_BASE + "rabona-casino", "freeSpins": 200, "minDeposit": 20,
        "description": "Online kasino s fotbalovou tematikou, sportovní sázkovou kanceláří a štědrým uvítacím balíčkem pro všechny fanoušky sportu.",
        "features": ["Fotbalové téma", "Sport + kasino", "200 FS", "Live betting"],
        "review": {
            "metaDescription": "Rabona Casino recenze 2026 – +100 % bonus až 500 € + 200 free spinů. Kasino s fotbalovou tematikou a sportovní sázkovou kanceláří.",
            "reviewCount": 412, "bonusAmount": "500 €", "freeSpinsCount": "200 FS",
            "withdrawalSpeed": "24h",
            "owner": "Rabona Group", "yearCreated": "2023",
            "license": "Curaçao", "withdrawalRange": "20 € – 30 000 €",
            "withdrawalSpeedDetail": "Do 24 hodin", "czechLanguage": "Ano", "mobile": "Ano (web)",
            "introduction": "Rabona Casino je unikátní online platforma s fotbalovou tematikou pojmenovaná po slavném finte (rabona kop). Spuštěná v roce 2023, kombinuje plnohodnotné online kasino se sportovní sázkovou kanceláří se silným důrazem na fotbal. Nabízí přes 3 000 kasinových her od 40+ poskytovatelů, tisíce sportovních eventů denně a štědrý uvítací balíček 100 % až 500 € + 200 free spinů. Tematické prvky se prolínají do celého rozhraní – VIP program 'Champions League', turnaje 'Cup' a věrnostní úrovně pojmenované po slavných pozicích.",
            "bonusIntro": "Rabona vítá nové hráče dvojitým balíčkem – 100 % bonus na první vklad až 500 € + 200 free spinů pro kasino, plus 100 % freebet až 100 € pro sport. Wagering x35 je férový.",
            "bonuses": [
                {"title": "Kasino bonus", "value": "+100%", "detail": "Až 500 €, x35"},
                {"title": "Free spiny", "value": "200 FS", "detail": "Na vybrané sloty"},
                {"title": "Sport freebet", "value": "+100%", "detail": "Až 100 €"},
                {"title": "Cup Cashback", "value": "10%", "detail": "Týdenní vrácení"}
            ],
            "weeklyPromo": "Rabona pořádá weekly 'Cup' turnaje s prize poolem 25 000 €, daily fotbalové akumulátorové boosty, free bet pátky pro hlavní fotbalové ligy a víkendové cashback eventy.",
            "vipProgram": "Champions League VIP je věrnostní program s 6 úrovněmi pojmenovanými po fotbalových rolích (Player, Captain, Manager, Coach, Director, President). Vyšší úrovně získávají vyšší cashback, exkluzivní bonusy a osobního VIP manažera od úrovně Coach.",
            "gamesIntro": "Rabona nabízí přes 3 000 kasinových her od 40+ poskytovatelů plus kompletní sportovní sekci s důrazem na fotbal.",
            "gamesSlots": "Více než 2 500 automatů včetně tematických fotbalových slotů (Football Glory, World Cup, Football Studio) a všech populárních hitů od Pragmatic Play, NetEnt a dalších.",
            "gamesTable": "Stolní hry – ruleta, blackjack, baccarat, poker. Limity od 0,50 € do 2 500 €.",
            "gamesLive": "Live kasino od Evolution Gaming a Pragmatic Play Live – Football Studio, Crazy Time, Lightning Roulette a desítky standardních stolů.",
            "gamesMini": "Crash games (Aviator, Spaceman), Plinko, Mines, Dice. Plus virtuální sporty (zejména virtuální fotbal) a esports betting.",
            "paymentsIntro": "Rabona podporuje hlavní platební metody. Výběry zpracovány do 24 hodin.",
            "paymentMethods": ["Visa", "Mastercard", "Skrill", "Neteller", "PaySafeCard", "Apple Pay", "Bitcoin", "USDT", "MuchBetter", "Bankovní převod"],
            "paymentCount": 10,
            "providersIntro": "Rabona spolupracuje s 40+ poskytovateli her a předními sportovními datovými partnery (BetRadar).",
            "providers": CORE_PROVIDERS + ['Habanero', 'Betsoft', 'Playson', 'iSoftBet', 'Pragmatic Play Live'],
            "providerCount": 25,
            "advantages": [
                "Unikátní fotbalová tematika napříč celou platformou",
                "Hybridní kasino + sport s důrazem na fotbal",
                "Champions League VIP program se 6 úrovněmi",
                "Štědrý balíček 500 € + 200 FS + 100 € sport freebet",
                "Live betting na tisíce fotbalových eventů",
                "Plně česká platforma s 24/7 podporou"
            ],
            "pros": ["Fotbalové téma", "Hybrid kasino + sport", "200 FS uvítacích", "Champions League VIP", "Live betting", "Plně česky"],
            "cons": ["Curaçao licence", "Tematika není pro nefotbalové hráče", "Bez nativní aplikace"],
            "supportText": "Zákaznická podpora Rabona je dostupná 24/7 přes live chat a email. Plně v češtině. Live chat odpovídá obvykle do 3 minut.",
            "faq": [
                {"q": "Co znamená 'Rabona'?", "a": "Rabona je slavný fotbalový fint, kde hráč kopne míč protiopačnou nohou za stojnou nohou. Inspirace pro značku."},
                {"q": "Mohu sázet na fotbal?", "a": "Ano, Rabona nabízí jednu z nejširších nabídek fotbalových sázek – Premier League, La Liga, Bundesliga, Serie A, Champions League a stovky dalších."},
                {"q": "Co je Champions League VIP?", "a": "6úrovňový věrnostní program s fotbalovými názvy. Vyšší úrovně získávají vyšší cashback a osobního manažera."},
                {"q": "Mohu platit kryptoměnou?", "a": "Ano, Bitcoin a USDT jsou podporovány s okamžitými vklady."},
                {"q": "Mají live betting?", "a": "Ano, tisíce sportovních eventů denně s in-play sázením."}
            ],
            "finalVerdict": "Rabona Casino je perfektní volba pro fanoušky fotbalu, kteří chtějí kombinovat sportovní sázky s kasinovou zábavou. Tematická stylizace, štědrý hybridní balíček 500 € + 200 FS + 100 € freebet a Champions League VIP program z něj činí jedinečnou platformu pro každého fotbalového nadšence."
        }
    },
]


def main():
    with open(PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    existing_ids = {c['id'] for c in data['casinos']}
    existing_slugs = {c['slug'] for c in data['casinos']}
    added = 0

    for casino in NEW:
        if casino['id'] in existing_ids or casino['slug'] in existing_slugs:
            print(f'  -> {casino["id"]} already exists, skipping')
            continue
        # Compute filters from data
        casino['filters'] = build_filters(casino)
        data['casinos'].append(casino)
        added += 1
        print(f'  + Added {casino["name"]} ({casino["slug"]}) - rating {casino["rating"]}')

    with open(PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Validate
    with open(PATH, 'r', encoding='utf-8') as f:
        validated = json.load(f)

    print(f'\nDone. Total casinos: {len(validated["casinos"])} (+{added} new)')


if __name__ == '__main__':
    main()
