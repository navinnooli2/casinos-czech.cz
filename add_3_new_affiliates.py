#!/usr/bin/env python3
"""Add Wyns + Spinania casinos and convert mafia-casino to m-traff affiliate."""

import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(BASE, 'data', 'casinos.json')

NEW_AFFILIATES = [
    {
        "id": "wyns", "name": "Wyns", "slug": "wyns",
        "rating": 4.5, "bonus": "Bonus 100% až 5 000 Kč + 200 free spinů",
        "bonusAmount": "5 000 Kč", "wagering": "x30",
        "bonusUrl": "https://m-traff.net/HYcs2BV5?sub_id_1=wyns",
        "freeSpins": 200, "minDeposit": 100,
        "description": "Moderní online kasino s rozsáhlou nabídkou her a štědrým uvítacím bonusem.",
        "features": ["3 000+ her", "Live kasino", "Krypto platby", "Mobilní aplikace"],
        "filters": {
            "rating": 4.5, "minDeposit": 100, "freeSpins": 200, "wagering": 30,
            "speed": "24h", "license": "curacao", "country": "international", "language": "cs",
            "payments": ["visa", "mastercard", "skrill", "neteller", "paysafecard", "apple-pay", "bitcoin", "ethereum", "usdt", "muchbetter"],
            "providers": ["pragmatic-play", "netent", "playn-go", "evolution", "microgaming", "hacksaw-gaming", "push-gaming", "yggdrasil", "spribe", "bgaming", "wazdan", "relax-gaming", "quickspin", "thunderkick", "big-time-gaming", "red-tiger", "endorphina", "nolimit-city", "elk-studios", "booongo"],
            "providerCount": 50, "paymentCount": 10,
            "hasNoDeposit": False, "hasFreeSpins": True, "hasCashback": True, "hasReload": True,
            "hasVipBonus": True, "hasSportBonus": False, "hasApp": True, "hasVip": True,
            "hasSport": True, "hasEsport": True, "hasLive": True, "hasCrypto": True,
            "hasPayPal": False, "hasApplePay": True, "hasInstantWithdraw": False,
            "hasLowDeposit": True, "hasLowWager": True, "isAffiliate": True
        },
        "review": {
            "metaDescription": "Wyns kasino recenze 2026 – 100% bonus až 5 000 Kč + 200 free spinů. Hodnocení her, plateb a podpory.",
            "reviewCount": 287, "bonusAmount": "5 000 Kč", "freeSpinsCount": "200 FS",
            "withdrawalSpeed": "24h", "owner": "Wyns N.V.", "yearCreated": "2024",
            "license": "Curaçao", "withdrawalRange": "100 Kč – 300 000 Kč",
            "withdrawalSpeedDetail": "Do 24 hodin", "czechLanguage": "Ano", "mobile": "Ano + Aplikace",
            "introduction": "Wyns je moderní online kasino, které vstoupilo na trh v roce 2024 s ambiciózním přístupem. Nabízí přes 3 000 her od předních poskytovatelů, štědré bonusy a podporu kryptoměn.",
            "bonusIntro": "Wyns nabízí atraktivní uvítací bonus 100% na první vklad až do 5 000 Kč plus 200 free spinů na nejpopulárnější automaty.",
            "bonuses": [
                {"title": "1. vklad", "value": "100%", "detail": "Až 5 000 Kč, x30 protočení"},
                {"title": "Free spiny", "value": "200 FS", "detail": "Na vybrané automaty"},
                {"title": "Reload bonus", "value": "50%", "detail": "Až 2 000 Kč"},
                {"title": "Cashback", "value": "10%", "detail": "Týdenní vrácení ztrát"}
            ],
            "weeklyPromo": "Pravidelné turnaje s prize poolem až 200 000 Kč, denní úkoly s odměnami a páteční reload bonusy.",
            "vipProgram": "VIP klub se 6 úrovněmi nabízí osobního manažera, exkluzivní bonusy a rychlejší výběry.",
            "gamesIntro": "Wyns má 3 000+ her od 50+ poskytovatelů včetně exkluzivních titulů.",
            "gamesSlots": "Více než 2 500 automatů od Pragmatic Play, NetEnt, Play'n GO, Hacksaw Gaming a dalších.",
            "gamesTable": "Kompletní nabídka stolních her – ruleta, blackjack, baccarat a poker.",
            "gamesLive": "Live kasino od Evolution s desítkami stolů 24/7.",
            "gamesMini": "Aviator, Plinko, Mines, Spaceman a další crash hry od Spribe a BGaming.",
            "paymentsIntro": "Wyns podporuje hlavní platební metody včetně kryptoměn. Výběry do 24 hodin.",
            "paymentMethods": ["Visa", "Mastercard", "Skrill", "Neteller", "PaySafeCard", "Apple Pay", "Bitcoin", "Ethereum", "USDT", "MuchBetter"],
            "paymentCount": 10,
            "providersIntro": "Wyns spolupracuje s 50+ poskytovateli her.",
            "providers": ["Pragmatic Play", "NetEnt", "Play'n GO", "Evolution", "Microgaming", "Hacksaw Gaming", "Push Gaming", "Yggdrasil", "Spribe", "BGaming", "Wazdan", "Relax Gaming", "Quickspin", "Thunderkick", "Big Time Gaming", "Red Tiger", "Endorphina", "Nolimit City", "ELK Studios", "Booongo"],
            "providerCount": 50,
            "advantages": [
                "Více než 3 000 her od 50+ poskytovatelů",
                "Štědrý uvítací bonus 5 000 Kč + 200 FS",
                "Rychlé výběry do 24 hodin",
                "Podpora kryptoměn (BTC, ETH, USDT)",
                "Mobilní aplikace pro iOS i Android",
                "VIP program s 6 úrovněmi"
            ],
            "pros": ["3 000+ her", "Bonus 5 000 Kč + 200 FS", "Krypto platby", "Mobilní aplikace", "VIP program", "Cashback 10%"],
            "cons": ["Curaçao licence", "Wagering x30", "Bez PayPal"],
            "supportText": "Zákaznická podpora dostupná 24/7 přes live chat a email v češtině. Odpověď do 2 minut.",
            "faq": [
                {"q": "Jaký je uvítací bonus?", "a": "100% bonus na první vklad až 5 000 Kč + 200 free spinů."},
                {"q": "Mohu platit kryptoměnami?", "a": "Ano, Wyns přijímá Bitcoin, Ethereum a USDT."},
                {"q": "Jak rychle probíhají výběry?", "a": "E-peněženky do 24 hodin, karty 1-3 dny."},
                {"q": "Má Wyns mobilní aplikaci?", "a": "Ano, pro iOS i Android s plnou funkcionalitou."},
                {"q": "Je Wyns bezpečné?", "a": "Ano, má licenci Curaçao a používá SSL šifrování."}
            ],
            "finalVerdict": "Wyns je solidní moderní kasino s širokou nabídkou her, štědrým bonusem a podporou kryptoměn. Doporučujeme jako kvalitní volbu pro české hráče."
        }
    },
    {
        "id": "spinania", "name": "Spinania", "slug": "spinania",
        "rating": 4.4, "bonus": "Bonus 150% až 4 500 Kč + 250 free spinů",
        "bonusAmount": "4 500 Kč", "wagering": "x35",
        "bonusUrl": "https://m-traff.net/HYcs2BV5?sub_id_1=spinania",
        "freeSpins": 250, "minDeposit": 100,
        "description": "Slot-zaměřené kasino s exkluzivními free spiny a širokou nabídkou automatů.",
        "features": ["Slot specialista", "250 FS uvítací", "Týdenní turnaje", "Bez wager bonusy"],
        "filters": {
            "rating": 4.4, "minDeposit": 100, "freeSpins": 250, "wagering": 35,
            "speed": "24h", "license": "curacao", "country": "international", "language": "cs",
            "payments": ["visa", "mastercard", "skrill", "neteller", "paysafecard", "apple-pay", "bitcoin", "muchbetter"],
            "providers": ["pragmatic-play", "netent", "playn-go", "microgaming", "hacksaw-gaming", "push-gaming", "yggdrasil", "spribe", "bgaming", "wazdan", "relax-gaming", "quickspin", "thunderkick", "big-time-gaming", "red-tiger", "endorphina", "nolimit-city", "elk-studios"],
            "providerCount": 45, "paymentCount": 8,
            "hasNoDeposit": False, "hasFreeSpins": True, "hasCashback": True, "hasReload": True,
            "hasVipBonus": True, "hasSportBonus": False, "hasApp": True, "hasVip": True,
            "hasSport": False, "hasEsport": False, "hasLive": True, "hasCrypto": True,
            "hasPayPal": False, "hasApplePay": True, "hasInstantWithdraw": False,
            "hasLowDeposit": True, "hasLowWager": False, "isAffiliate": True
        },
        "review": {
            "metaDescription": "Spinania kasino recenze 2026 – 150% bonus až 4 500 Kč + 250 free spinů. Slot specialista pro české hráče.",
            "reviewCount": 198, "bonusAmount": "4 500 Kč", "freeSpinsCount": "250 FS",
            "withdrawalSpeed": "24h", "owner": "Spinania N.V.", "yearCreated": "2024",
            "license": "Curaçao", "withdrawalRange": "100 Kč – 250 000 Kč",
            "withdrawalSpeedDetail": "Do 24 hodin", "czechLanguage": "Ano", "mobile": "Ano (web)",
            "introduction": "Spinania je specializované online kasino zaměřené na automaty a free spiny. Nabízí jednu z nejštědřejších uvítacích nabídek free spinů na trhu (250 FS).",
            "bonusIntro": "Spinania vítá hráče balíčkem 150% až 4 500 Kč + 250 free spinů – jedna z nejvyšších nabídek FS v ČR.",
            "bonuses": [
                {"title": "1. vklad", "value": "150%", "detail": "Až 4 500 Kč, x35"},
                {"title": "Free spiny", "value": "250 FS", "detail": "Na top sloty"},
                {"title": "Reload", "value": "75%", "detail": "Každý víkend"},
                {"title": "Cashback", "value": "12%", "detail": "Bez wager"}
            ],
            "weeklyPromo": "Spinania pořádá týdenní slot turnaje s prize poolem 100 000 Kč, denní free spiny pro VIP a víkendové reload bonusy.",
            "vipProgram": "Slot VIP Club s 5 úrovněmi nabízí free spiny každý den, vyšší cashback a osobního VIP manažera.",
            "gamesIntro": "Spinania má pečlivě vybranou kolekci 2 500+ slotů od top poskytovatelů.",
            "gamesSlots": "Více než 2 200 automatů – fokus na megaways, jackpoty a klasické sloty od Pragmatic Play, NetEnt, Hacksaw Gaming.",
            "gamesTable": "Menší výběr stolních her – ruleta, blackjack a baccarat.",
            "gamesLive": "Live kasino od Evolution a Pragmatic Play Live s game shows.",
            "gamesMini": "Crash hry, Plinko, Mines a další moderní formáty.",
            "paymentsIntro": "Spinania podporuje hlavní platební metody včetně kryptoměn.",
            "paymentMethods": ["Visa", "Mastercard", "Skrill", "Neteller", "PaySafeCard", "Apple Pay", "Bitcoin", "MuchBetter"],
            "paymentCount": 8,
            "providersIntro": "Spinania pracuje s 45+ poskytovateli specializovanými na sloty.",
            "providers": ["Pragmatic Play", "NetEnt", "Play'n GO", "Microgaming", "Hacksaw Gaming", "Push Gaming", "Yggdrasil", "Spribe", "BGaming", "Wazdan", "Relax Gaming", "Quickspin", "Thunderkick", "Big Time Gaming", "Red Tiger", "Endorphina", "Nolimit City", "ELK Studios"],
            "providerCount": 45,
            "advantages": [
                "Štědrý uvítací bonus 250 free spinů",
                "Specializace na automaty s 2 500+ tituly",
                "Týdenní slot turnaje s prize poolem",
                "Cashback 12% bez wagering",
                "Podpora kryptoměn",
                "Rychlé výběry do 24 hodin"
            ],
            "pros": ["250 FS uvítací", "Cashback bez wager", "2 500+ slotů", "Týdenní turnaje", "Krypto platby", "Plně česky"],
            "cons": ["Curaçao licence", "Méně stolních her", "Wagering x35"],
            "supportText": "Zákaznická podpora 24/7 přes live chat v češtině. Specializovaní agenti pro slot dotazy.",
            "faq": [
                {"q": "Jaký je uvítací bonus?", "a": "150% bonus až 4 500 Kč + 250 free spinů."},
                {"q": "Co je 'cashback bez wager'?", "a": "12% z čistých ztrát se vám týdně vrátí jako reálné peníze, bez nutnosti protáčení."},
                {"q": "Mohu hrát na mobilu?", "a": "Ano, plně responzivní webová verze pro iOS i Android."},
                {"q": "Které sloty jsou nejlepší?", "a": "Doporučujeme Sweet Bonanza, Gates of Olympus a Book of Dead s vysokým RTP."},
                {"q": "Mohu platit Bitcoinem?", "a": "Ano, Spinania přijímá Bitcoin a další hlavní kryptoměny."}
            ],
            "finalVerdict": "Spinania je ideální volba pro fanoušky automatů. S 250 free spiny uvítacím balíčkem, cashbackem bez wagering a 2 500+ sloty je to top kasino pro slot enthusiast."
        }
    }
]


def main():
    with open(PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    existing_ids = {c['id'] for c in data['casinos']}
    added = 0

    # Add Wyns and Spinania
    for new_casino in NEW_AFFILIATES:
        if new_casino['id'] in existing_ids:
            print(f'  ⏭ {new_casino["id"]} already exists')
            continue
        data['casinos'].append(new_casino)
        added += 1
        print(f'  ✓ Added {new_casino["name"]} ({new_casino["slug"]}) — m-traff affiliate')

    # Convert mafia-casino to m-traff affiliate
    for casino in data['casinos']:
        if casino['slug'] == 'mafia-casino':
            old_url = casino.get('bonusUrl', '')
            new_url = 'https://m-traff.net/HYcs2BV5?sub_id_1=mafia'
            if old_url != new_url:
                casino['bonusUrl'] = new_url
                if 'filters' in casino:
                    casino['filters']['url'] = new_url
                    casino['filters']['isAffiliate'] = True
                print(f'  🔧 mafia-casino: {old_url} → {new_url}')

    with open(PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f'\n✅ Total casinos: {len(data["casinos"])} (+{added} new)')
    print(f'✅ mafia-casino is now m-traff affiliate')


if __name__ == '__main__':
    main()
