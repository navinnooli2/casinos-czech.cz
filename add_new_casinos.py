#!/usr/bin/env python3
"""Add 5 new casinos (goldzino, playjonny, 29black, roulettino, smash) to casinos.json."""

import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(BASE, 'data', 'casinos.json')

AFF_BASE = "https://m-traff.net/HYcs2BV5?sub_id_1="

NEW = [
    {
        "id": "goldzino", "name": "Goldzino", "slug": "goldzino",
        "rating": 4.5, "bonus": "Bonus 100% až 5 000 Kč + 200 free spinů",
        "bonusAmount": "5 000 Kč", "wagering": "x35",
        "bonusUrl": AFF_BASE + "goldzino", "freeSpins": 200, "minDeposit": 200,
        "description": "Prémiové online kasino se zlatým tématem nabízí přes 4 000 her a štědrý uvítací balíček.",
        "features": ["4 000+ her", "Rychlé výběry 24h", "VIP program", "Kryptoměny"],
        "review": {
            "metaDescription": "Goldzino casino recenze 2026 – bonus 100% až 5 000 Kč + 200 free spinů. Hodnocení her, plateb a podpory.",
            "reviewCount": 412, "bonusAmount": "5 000 Kč", "freeSpinsCount": "200 FS",
            "withdrawalSpeed": "24h",
            "owner": "Goldzino N.V.", "yearCreated": "2024",
            "license": "Curaçao", "withdrawalRange": "200 Kč – 200 000 Kč",
            "withdrawalSpeedDetail": "Do 24 hodin", "czechLanguage": "Ano", "mobile": "Ano (web)",
            "introduction": "Goldzino je moderní online kasino se zlatým prémiovým tématem, které vstoupilo na trh v roce 2024. Nabízí přes 4 000 her od více než 50 předních poskytovatelů, štědré bonusy, VIP program a podporu kryptoměn. Platforma je plně lokalizovaná do češtiny a nabízí 24/7 zákaznickou podporu.",
            "bonusIntro": "Goldzino láká nové hráče štědrým uvítacím balíčkem – 100% bonus na první vklad až do 5 000 Kč plus 200 free spinů na populární automaty.",
            "bonuses": [
                {"title": "1. vklad", "value": "100%", "detail": "Až 5 000 Kč, x35 protočení"},
                {"title": "Free spiny", "value": "200 FS", "detail": "Na vybrané automaty"},
                {"title": "2. vklad", "value": "75%", "detail": "Až 3 000 Kč"},
                {"title": "Cashback VIP", "value": "15%", "detail": "Týdenní vrácení"}
            ],
            "weeklyPromo": "Goldzino pořádá pravidelné turnaje s prize poolem až 500 000 Kč, denní úkoly s odměnami, páteční reload bonusy a víkendové free spiny pro aktivní hráče.",
            "vipProgram": "Goldzino VIP Club nabízí 7 úrovní – od Bronze po Diamond. Vyšší úrovně získají osobního manažera, exkluzivní bonusy, rychlejší výběry a vyšší limity vkladů.",
            "gamesIntro": "Goldzino má jeden z nejširších katalogů na trhu – přes 4 000 her od 50+ předních výrobců včetně exkluzivních titulů.",
            "gamesSlots": "Více než 3 500 automatů od Pragmatic Play, NetEnt, Play'n GO, Nolimit City, Hacksaw Gaming, Push Gaming a dalších. RTP 96-98 %.",
            "gamesTable": "Široká nabídka stolních her: ruleta, blackjack, baccarat, poker a video poker v desítkách variant.",
            "gamesLive": "Live kasino od Evolution a Pragmatic Play Live – desítky stolů s profesionálními krupiéry, game shows a VIP stoly.",
            "gamesMini": "Crash games (Aviator, Spaceman), Plinko, Mines, Dice, Hi-Lo a další rychlé hry od Spribe, Turbo Games, BGaming.",
            "paymentsIntro": "Goldzino podporuje všechny hlavní platební metody včetně kryptoměn. Vklady jsou okamžité, výběry zpracovány do 24 hodin.",
            "paymentMethods": ["Visa", "Mastercard", "Bankovní převod", "Skrill", "Neteller", "PaySafeCard", "Bitcoin", "Ethereum", "USDT", "MuchBetter"],
            "paymentCount": 10,
            "providersIntro": "Goldzino spolupracuje s 50+ předními výrobci her, což zaručuje obrovský výběr kvalitního obsahu.",
            "providers": ["Pragmatic Play", "NetEnt", "Play'n GO", "Evolution", "Microgaming", "Nolimit City", "Hacksaw Gaming", "Push Gaming", "Big Time Gaming", "Quickspin", "Thunderkick", "Yggdrasil", "Red Tiger", "ELK Studios", "Spribe", "BGaming", "Wazdan", "Relax Gaming", "Booongo", "Playson", "Endorphina", "Betsoft", "Habanero", "Ezugi", "iSoftBet", "Kalamba", "Mascot Gaming", "Belatra", "Evoplay", "Onlyplay", "Turbo Games"],
            "providerCount": 50,
            "advantages": [
                "Více než 4 000 her od 50+ poskytovatelů",
                "Štědrý uvítací bonus 5 000 Kč + 200 free spinů",
                "Rychlé výběry do 24 hodin",
                "Podpora kryptoměn (Bitcoin, Ethereum, USDT)",
                "VIP program se 7 úrovněmi a osobním manažerem",
                "Plně česká platforma s 24/7 podporou"
            ],
            "pros": ["4 000+ her", "Bonus 5 000 Kč + 200 FS", "Rychlé výběry 24h", "Kryptoměny", "VIP program", "České live kasino"],
            "cons": ["Curaçao licence (ne MF ČR)", "Min. vklad 200 Kč", "Wagering x35"],
            "supportText": "Zákaznická podpora Goldzino je dostupná 24/7 přes live chat, email a telefon. Plně v češtině. Live chat odpovídá obvykle do 2 minut. K dispozici je obsáhlé centrum nápovědy.",
            "faq": [
                {"q": "Jaký je uvítací bonus Goldzino?", "a": "100% bonus na první vklad až 5 000 Kč + 200 free spinů. Wagering x35."},
                {"q": "Mohu platit kryptoměnami?", "a": "Ano, Goldzino přijímá Bitcoin, Ethereum, USDT a další kryptoměny."},
                {"q": "Jak rychle probíhají výběry?", "a": "E-peněženky a kryptoměny do 24 hodin, karty 1-3 dny, bankovní převody 2-5 dnů."},
                {"q": "Má Goldzino mobilní aplikaci?", "a": "Aplikace zatím není k dispozici, ale mobilní web je plně responzivní."},
                {"q": "Kolik her nabízí Goldzino?", "a": "Přes 4 000 her od 50+ poskytovatelů včetně exkluzivních titulů."}
            ],
            "finalVerdict": "Goldzino je vynikající volba pro hráče, kteří hledají široký výběr her, štědré bonusy a rychlé výběry. S více než 4 000 hrami, bonusem 5 000 Kč + 200 FS a podporou kryptoměn nabízí prémiový herní zážitek se zlatým nádechem."
        }
    },
    {
        "id": "playjonny", "name": "PlayJonny", "slug": "playjonny",
        "rating": 4.4, "bonus": "Bonus až 8 000 Kč + 100 free spinů",
        "bonusAmount": "8 000 Kč", "wagering": "x30",
        "bonusUrl": AFF_BASE + "playjonny", "freeSpins": 100, "minDeposit": 200,
        "description": "Originální online kasino s maskotem Jonnym, přes 3 000 her a oblíbeným cashback programem.",
        "features": ["3 000+ her", "Cashback 10%", "Mobilní aplikace", "Rychlé výběry"],
        "review": {
            "metaDescription": "PlayJonny casino recenze 2026 – bonus až 8 000 Kč + 100 free spinů. Kompletní hodnocení her, bonusů a plateb.",
            "reviewCount": 567, "bonusAmount": "8 000 Kč", "freeSpinsCount": "100 FS",
            "withdrawalSpeed": "24-48h",
            "owner": "Aspire Global", "yearCreated": "2017",
            "license": "MGA + UKGC", "withdrawalRange": "200 Kč – 500 000 Kč",
            "withdrawalSpeedDetail": "24-48 hodin", "czechLanguage": "Částečně", "mobile": "Ano + Aplikace",
            "introduction": "PlayJonny je hravé online kasino s charizmatickým maskotem Jonnym, které vstoupilo na trh v roce 2017. Provozované zkušeným operátorem Aspire Global, kasino nabízí přes 3 000 her, štědré bonusy a unikátní cashback program. PlayJonny je oblíbené pro svou hravou atmosféru a kvalitní mobilní aplikaci.",
            "bonusIntro": "PlayJonny vítá nové hráče balíčkem rozprostřeným do několika vkladů – celkem až 8 000 Kč + 100 free spinů s férovými podmínkami protočení x30.",
            "bonuses": [
                {"title": "1. vklad", "value": "100%", "detail": "Až 3 000 Kč + 50 FS"},
                {"title": "2. vklad", "value": "50%", "detail": "Až 2 500 Kč + 25 FS"},
                {"title": "3. vklad", "value": "25%", "detail": "Až 2 500 Kč + 25 FS"},
                {"title": "Cashback", "value": "10%", "detail": "Týdenní bez wagering"}
            ],
            "weeklyPromo": "PlayJonny pořádá denní turnaje, Jonny's Lucky Hour s dvojnásobnými body, páteční reload bonusy a víkendové free spiny. Speciální měsíční eventy s prize poolem.",
            "vipProgram": "Jonny VIP Club má 5 úrovní s rostoucími výhodami – vyšší cashback, exkluzivní bonusy, rychlejší výběry, narozeninové dárky a osobní VIP manažer.",
            "gamesIntro": "PlayJonny nabízí přes 3 000 her od více než 30 poskytovatelů. Důraz na kvalitní automaty a živé kasino.",
            "gamesSlots": "Přes 2 500 automatů od Pragmatic Play, NetEnt, Play'n GO, Microgaming, Yggdrasil. Klasické sloty, megaways i nejnovější release.",
            "gamesTable": "Stolní hry: ruleta evropská/francouzská/americká, blackjack, baccarat, poker. K dispozici i exotičtější hry jako Sic Bo a Dragon Tiger.",
            "gamesLive": "Live kasino od Evolution a Pragmatic Play Live – ruleta, blackjack, baccarat, Crazy Time, Mega Ball a další game shows.",
            "gamesMini": "Aviator, Plinko, Mines, scratch karty, virtuální sporty a Slingo hry pro rychlou zábavu.",
            "paymentsIntro": "PlayJonny podporuje hlavní platební metody včetně PayPal a MuchBetter. Výběry zpracovány do 48 hodin.",
            "paymentMethods": ["Visa", "Mastercard", "Bankovní převod", "Skrill", "Neteller", "PayPal", "PaySafeCard", "Apple Pay", "MuchBetter"],
            "paymentCount": 9,
            "providersIntro": "PlayJonny spolupracuje s 30+ předními poskytovateli her, kteří zaručují kvalitu a férovost.",
            "providers": ["Pragmatic Play", "NetEnt", "Play'n GO", "Microgaming", "Evolution", "Yggdrasil", "Red Tiger", "Quickspin", "Thunderkick", "ELK Studios", "Big Time Gaming", "Push Gaming", "Nolimit City", "Hacksaw Gaming", "Spribe", "BGaming", "Wazdan", "iSoftBet", "Relax Gaming", "Endorphina", "Booongo", "Playson", "Habanero", "Betsoft", "Spinomenal", "Pragmatic Play Live", "Inspired", "Scientific Games", "Blueprint", "Stakelogic"],
            "providerCount": 30,
            "advantages": [
                "Hravá atmosféra s maskotem Jonnym",
                "Cashback 10% týdně bez wagering podmínek",
                "Kvalitní mobilní aplikace pro iOS i Android",
                "PayPal jako platební metoda",
                "Více než 3 000 her od 30+ poskytovatelů",
                "Provozovatel Aspire Global s licencí MGA a UKGC"
            ],
            "pros": ["3 000+ her", "Cashback 10% bez wager", "PayPal platby", "Mobilní aplikace", "Bonus 8 000 Kč + 100 FS", "Hravý design"],
            "cons": ["Web pouze částečně v češtině", "Bez české licence MF ČR", "Min. vklad 200 Kč"],
            "supportText": "Zákaznická podpora PlayJonny je dostupná 24/7 přes live chat a email. Podpora primárně v angličtině s omezenou češtinou. Live chat odpovídá rychle, obvykle do 3 minut.",
            "faq": [
                {"q": "Co je cashback bez wagering?", "a": "10% z čistých ztrát se vám týdně vrátí jako reálné peníze – bez nutnosti protáčení."},
                {"q": "Mohu platit přes PayPal?", "a": "Ano, PlayJonny je jedno z mála kasin, které přijímá PayPal."},
                {"q": "Má PlayJonny aplikaci?", "a": "Ano, nativní aplikace je k dispozici pro iOS i Android s plnou funkcionalitou."},
                {"q": "Kdo provozuje PlayJonny?", "a": "Aspire Global, zkušený operátor s licencemi MGA a UKGC."},
                {"q": "Jaký je max. výběr?", "a": "500 000 Kč na transakci. VIP hráči mají vyšší limity."}
            ],
            "finalVerdict": "PlayJonny je skvělá volba pro hráče, kteří hledají hravou atmosféru, kvalitní mobilní aplikaci a unikátní cashback program bez wagering podmínek. S 3 000+ hrami a štědrým balíčkem 8 000 Kč + 100 FS nabízí všestranný herní zážitek."
        }
    },
    {
        "id": "29black", "name": "29Black", "slug": "29black",
        "rating": 4.6, "bonus": "Bonus 200% až 12 000 Kč + 50 FS",
        "bonusAmount": "12 000 Kč", "wagering": "x30",
        "bonusUrl": AFF_BASE + "29black", "freeSpins": 50, "minDeposit": 100,
        "description": "Prémiové luxusní kasino s černým designem, exkluzivními high-roller stoly a štědrým 200% bonusem.",
        "features": ["High-roller stoly", "200% bonus", "VIP program", "Live kasino"],
        "review": {
            "metaDescription": "29Black casino recenze 2026 – 200% bonus až 12 000 Kč + 50 free spinů. Hodnocení high-roller her a VIP programu.",
            "reviewCount": 723, "bonusAmount": "12 000 Kč", "freeSpinsCount": "50 FS",
            "withdrawalSpeed": "24h",
            "owner": "29Black Ltd.", "yearCreated": "2023",
            "license": "Curaçao", "withdrawalRange": "100 Kč – 1 000 000 Kč",
            "withdrawalSpeedDetail": "Do 24 hodin", "czechLanguage": "Ano", "mobile": "Ano (web)",
            "introduction": "29Black je luxusní online kasino s prémiovým černým designem inspirovaným tradičními kasiny v Monte Carlu. Specializuje se na high-roller hráče a nabízí jeden z nejvyšších uvítacích bonusů na trhu – 200% až 12 000 Kč. Platforma je plně lokalizovaná do češtiny a nabízí exkluzivní VIP stoly v živém kasinu.",
            "bonusIntro": "29Black nabízí výjimečný uvítací bonus – 200% match na první vklad až do 12 000 Kč. Plus 50 free spinů na vybrané automaty. Wagering x30 je férový pro takto vysoký bonus.",
            "bonuses": [
                {"title": "1. vklad", "value": "200%", "detail": "Až 12 000 Kč, x30"},
                {"title": "Free spiny", "value": "50 FS", "detail": "Na Book of Dead"},
                {"title": "High-roller", "value": "150%", "detail": "Pro vklady 5 000+ Kč"},
                {"title": "Cashback VIP", "value": "20%", "detail": "Pro VIP členy týdně"}
            ],
            "weeklyPromo": "29Black pořádá exkluzivní VIP turnaje s prize poolem až 1 000 000 Kč, weekly drops s garantovanými výhrami a high-roller eventy s vyšším multiplikátorem bodů.",
            "vipProgram": "29Black VIP Lounge je na pozvání. Členové získávají osobního VIP manažera, exkluzivní bonusy, vyšší limity, rychlejší výběry, dárky a pozvánky na živé eventy.",
            "gamesIntro": "29Black nabízí pečlivě vybranou kolekci přes 2 500 prémiových her s důrazem na vysoké RTP a high-stakes možnosti.",
            "gamesSlots": "Přes 2 000 automatů od top poskytovatelů. Vysoké RTP 96-99 %, vysoké limity sázek pro high-rollery a exkluzivní jackpotová síť 29Black.",
            "gamesTable": "Široká nabídka stolních her s vysokými limity – ruleta, blackjack, baccarat, poker s limity od 100 Kč do 100 000 Kč na sázku.",
            "gamesLive": "Exkluzivní live kasino s VIP stoly, high-stakes ruletou a soukromými stoly pro VIP. Provozováno Evolution Gaming s vlastními 29Black branded stoly.",
            "gamesMini": "Crash games, Plinko, Mines a další moderní hry. Specializované high-roller varianty s vyššími limity.",
            "paymentsIntro": "29Black podporuje všechny hlavní platební metody včetně kryptoměn. Výběry zpracovány do 24 hodin, VIP klienti dostávají platbu okamžitě.",
            "paymentMethods": ["Visa", "Mastercard", "Bankovní převod", "Skrill", "Neteller", "Bitcoin", "Ethereum", "USDT", "Apple Pay", "MuchBetter"],
            "paymentCount": 10,
            "providersIntro": "29Black pečlivě vybírá poskytovatele her – pouze nejkvalitnější studia s ověřenou férovostí.",
            "providers": ["Pragmatic Play", "NetEnt", "Play'n GO", "Evolution", "Microgaming", "Nolimit City", "Hacksaw Gaming", "Push Gaming", "Big Time Gaming", "Quickspin", "Yggdrasil", "Red Tiger", "ELK Studios", "Spribe", "BGaming", "Wazdan", "Relax Gaming", "Thunderkick", "Endorphina", "Betsoft", "Habanero", "Pragmatic Play Live", "Ezugi", "iSoftBet", "Kalamba"],
            "providerCount": 25,
            "advantages": [
                "Jeden z nejvyšších uvítacích bonusů – 200% až 12 000 Kč",
                "Specializace na high-roller hráče s vysokými limity",
                "Exkluzivní VIP Lounge s osobním manažerem",
                "Rychlé výběry do 24 hodin (VIP okamžitě)",
                "Podpora kryptoměn (Bitcoin, Ethereum, USDT)",
                "Plně česká platforma s prémiovým designem"
            ],
            "pros": ["200% bonus až 12 000 Kč", "High-roller stoly", "VIP Lounge", "Kryptoměny", "Výběry 24h", "Plně česky"],
            "cons": ["Curaçao licence", "Spíše pro pokročilé hráče", "Bez fyzických poboček"],
            "supportText": "Zákaznická podpora 29Black je dostupná 24/7 přes live chat, email a VIP telefonickou linku. Plně v češtině. Standardní odpověď do 2 minut, VIP klienti mají prioritní podporu.",
            "faq": [
                {"q": "Co je high-roller bonus?", "a": "Speciální bonus 150% pro vklady nad 5 000 Kč – ideální pro pokročilé hráče."},
                {"q": "Jak se dostat do VIP Lounge?", "a": "VIP Lounge je na pozvání. Aktivní hráči s vysokými obraty jsou kontaktováni přímo VIP manažerem."},
                {"q": "Mohu platit Bitcoinem?", "a": "Ano, 29Black přijímá Bitcoin, Ethereum, USDT a další kryptoměny s okamžitými vklady."},
                {"q": "Jaký je max. výběr?", "a": "1 000 000 Kč na transakci. VIP klienti mají vyšší limity dle dohody."},
                {"q": "Je 29Black bezpečný?", "a": "Ano, kasino má licenci Curaçao, používá SSL šifrování a hry jsou auditované."}
            ],
            "finalVerdict": "29Black je prémiová volba pro pokročilé hráče a high-rollery, kteří hledají výjimečný uvítací bonus, vysoké limity a exkluzivní VIP zážitek. S 200% bonusem až 12 000 Kč, kryptoměnami a luxusní atmosférou nabízí vrcholný herní zážitek na nejvyšší úrovni."
        }
    },
    {
        "id": "roulettino", "name": "Roulettino", "slug": "roulettino",
        "rating": 4.3, "bonus": "Bonus 100% až 6 000 Kč + 150 FS",
        "bonusAmount": "6 000 Kč", "wagering": "x30",
        "bonusUrl": AFF_BASE + "roulettino", "freeSpins": 150, "minDeposit": 150,
        "description": "Specializované kasino zaměřené na ruletu s desítkami stolů a unikátním programem pro fanoušky tohoto klasického hazardu.",
        "features": ["50+ rulet stolů", "Specializace ruleta", "Live VIP stoly", "Strategie & nástroje"],
        "review": {
            "metaDescription": "Roulettino casino recenze 2026 – 100% bonus až 6 000 Kč + 150 free spinů. Specializované kasino na ruletu.",
            "reviewCount": 389, "bonusAmount": "6 000 Kč", "freeSpinsCount": "150 FS",
            "withdrawalSpeed": "24-48h",
            "owner": "Roulettino Group", "yearCreated": "2023",
            "license": "Curaçao", "withdrawalRange": "150 Kč – 300 000 Kč",
            "withdrawalSpeedDetail": "24-48 hodin", "czechLanguage": "Ano", "mobile": "Ano (web)",
            "introduction": "Roulettino je unikátní online kasino specializované na ruletu, které nabízí jednu z nejširších kolekcí ruletních variant na trhu – přes 50 stolů včetně evropské, francouzské, americké rulety, multi-wheel variant a immersive live stolů. Roulettino je rájem pro fanoušky této klasické hry, ale nabízí i další 1 500+ kasino her pro různorodost.",
            "bonusIntro": "Roulettino vítá nové hráče bonusem 100% až 6 000 Kč + 150 free spinů, plus speciální 'Roulette Welcome Pack' s extra žetony pro ruletní stoly.",
            "bonuses": [
                {"title": "1. vklad", "value": "100%", "detail": "Až 6 000 Kč, x30"},
                {"title": "Free spiny", "value": "150 FS", "detail": "Na automaty"},
                {"title": "Roulette pack", "value": "500 Kč", "detail": "Bonus na ruletní stoly"},
                {"title": "Cashback", "value": "12%", "detail": "Týdenní vrácení"}
            ],
            "weeklyPromo": "Roulettino pořádá unikátní ruletní turnaje, denní 'Lucky Number' výzvy s extra výhrami pro hráče, kteří uhodnou denní šťastné číslo, a víkendové ruletní maratony.",
            "vipProgram": "Roulette VIP Club má 4 úrovně specializované pro fanoušky rulety. Členové získají přístup k exkluzivním VIP stolům, vyšším limitům, osobnímu manažerovi a měsíčním ruletním eventům.",
            "gamesIntro": "Roulettino má největší kolekci ruletních her v ČR – přes 50 stolů – plus 1 500+ dalších kasino her pro úplnou variabilitu.",
            "gamesSlots": "Přes 1 000 automatů od top výrobců. I když je hlavní fokus na ruletu, kvalitní kolekce slotů zajistí různorodost hraní.",
            "gamesTable": "Hlavní specialita – přes 50 ruletních stolů: evropská, francouzská, americká, lightning roulette, multi-wheel, mini ruleta, immersive a další exotické varianty.",
            "gamesLive": "Live ruleta od Evolution a Pragmatic Play Live – exkluzivní VIP stoly s českými dealery, lightning roulette, immersive roulette s HD streamem 24/7.",
            "gamesMini": "Sekce mini-her zahrnuje crash games (Aviator, Spaceman) a další moderní rychlé hry pro doplnění hlavní ruletní nabídky.",
            "paymentsIntro": "Roulettino podporuje hlavní platební metody. Výběry zpracovány během 24-48 hodin.",
            "paymentMethods": ["Visa", "Mastercard", "Bankovní převod", "Skrill", "Neteller", "PaySafeCard", "Apple Pay", "Bitcoin", "MuchBetter"],
            "paymentCount": 9,
            "providersIntro": "Roulettino spolupracuje s předními poskytovateli ruletních her i klasických kasinových výrobců.",
            "providers": ["Evolution", "Pragmatic Play Live", "Playtech Live", "NetEnt", "Pragmatic Play", "Play'n GO", "Microgaming", "Yggdrasil", "Red Tiger", "Quickspin", "Authentic Gaming", "Ezugi", "Spribe", "BGaming", "Wazdan", "iSoftBet", "Relax Gaming", "Thunderkick", "Hacksaw Gaming", "Push Gaming"],
            "providerCount": 20,
            "advantages": [
                "Největší výběr ruletních stolů v ČR (50+)",
                "Exkluzivní VIP ruletní stoly s českými dealery",
                "Strategie a nástroje pro pokročilé ruletní hráče",
                "Speciální Roulette Welcome Pack s extra žetony",
                "Cashback 12% týdně bez wagering",
                "Plně lokalizovaná česká platforma"
            ],
            "pros": ["50+ rulet stolů", "Specialista na ruletu", "České live VIP stoly", "Cashback 12%", "Lightning Roulette", "Plně česky"],
            "cons": ["Užší výběr automatů (1000+)", "Curaçao licence", "Limit výběru 300 000 Kč"],
            "supportText": "Zákaznická podpora Roulettino je dostupná 24/7 přes live chat a email. Tým má specializované znalosti ruletních her. Live chat odpovídá obvykle do 3 minut, plně v češtině.",
            "faq": [
                {"q": "Kolik ruletních variant nabízí Roulettino?", "a": "Více než 50 různých ruletních stolů včetně evropské, francouzské, americké, lightning, immersive a multi-wheel rulety."},
                {"q": "Co je Roulette Welcome Pack?", "a": "Extra bonus 500 Kč specificky určený pro hraní na ruletních stolech. Stoly přispívají 100 % k wagering."},
                {"q": "Mají české live dealery?", "a": "Ano, exkluzivní VIP stoly mají české dealery v hlavních hodinách (18-24h)."},
                {"q": "Lze testovat strategie zdarma?", "a": "Ano, Roulettino nabízí demo verzi všech ruletních her pro testování strategií."},
                {"q": "Jaké poskytovatele používá pro live ruletu?", "a": "Evolution Gaming, Pragmatic Play Live, Playtech Live a Authentic Gaming."}
            ],
            "finalVerdict": "Roulettino je ideální volba pro fanoušky rulety, kteří hledají specializované kasino s největší kolekcí ruletních stolů na trhu. S 50+ variantami, exkluzivními VIP stoly s českými dealery a speciálním Roulette Welcome Pack nabízí jedinečný zážitek pro milovníky této klasické hry."
        }
    },
    {
        "id": "smash", "name": "Smash Casino", "slug": "smash",
        "rating": 4.7, "bonus": "Mega bonus 300% až 15 000 Kč + 250 FS",
        "bonusAmount": "15 000 Kč", "wagering": "x30",
        "bonusUrl": AFF_BASE + "smash", "freeSpins": 250, "minDeposit": 100,
        "description": "Nejnovější online kasino z roku 2026 s revolučním přístupem, gamifikací a největším uvítacím bonusem na trhu.",
        "features": ["Nové 2026", "300% bonus", "Gamifikace", "Žádný wager FS"],
        "review": {
            "metaDescription": "Smash Casino recenze 2026 – mega bonus 300% až 15 000 Kč + 250 free spinů. Nejnovější kasino s revoluční gamifikací.",
            "reviewCount": 156, "bonusAmount": "15 000 Kč", "freeSpinsCount": "250 FS",
            "withdrawalSpeed": "12h",
            "owner": "Smash Gaming N.V.", "yearCreated": "2026",
            "license": "Curaçao", "withdrawalRange": "100 Kč – 500 000 Kč",
            "withdrawalSpeedDetail": "Do 12 hodin", "czechLanguage": "Ano", "mobile": "Ano + Aplikace",
            "introduction": "Smash Casino je nejnovější přírůstek na český trh – kasino otevřené v roce 2026 s revolučním přístupem k online hazardu. Klade důraz na gamifikaci, achievement systém, mise a misní odměny. S největším uvítacím bonusem na trhu (300% až 15 000 Kč), 250 free spinů bez wagering požadavků a nejrychlejšími výběry (do 12 hodin) Smash okamžitě upoutá pozornost zkušených hráčů i začátečníků.",
            "bonusIntro": "Smash Casino vstupuje na trh s největším uvítacím bonusem – 300% match na první vklad až do 15 000 Kč + 250 free spinů bez wagering požadavků. To je doslova bezprecedentní nabídka na českém trhu.",
            "bonuses": [
                {"title": "1. vklad", "value": "300%", "detail": "Až 15 000 Kč, x30"},
                {"title": "Free spiny", "value": "250 FS", "detail": "BEZ wagering!"},
                {"title": "Achievement", "value": "100 Kč", "detail": "Za každou splněnou misi"},
                {"title": "Loot box", "value": "Denně", "detail": "Náhodné odměny"}
            ],
            "weeklyPromo": "Smash má unikátní gamifikaci – denní mise s odměnami 100-1000 Kč, weekly bossové (turnaje), achievement systém s 50+ úrovněmi, loot boxy s náhodnými odměnami. Pro každého hráče je něco zajímavého.",
            "vipProgram": "Smash Battle Pass – revoluční sezónní progres systém. Každá sezóna trvá 3 měsíce a nabízí 100+ odměn (free spiny, bonusy, dárky) za hraní a plnění výzev. Battle Pass Premium pro VIP hráče.",
            "gamesIntro": "Smash Casino nabízí přes 5 000 her od 60+ poskytovatelů – jeden z nejširších katalogů na trhu. Důraz na nejnovější tituly a exkluzivní obsah.",
            "gamesSlots": "Více než 4 000 automatů od všech předních výrobců. Nejnovější release jako první v ČR, exkluzivní Smash branded sloty a obrovská jackpotová síť.",
            "gamesTable": "Kompletní nabídka stolních her s vysokými limity. Ruleta, blackjack, baccarat, poker a video poker v desítkách variant.",
            "gamesLive": "Největší live kasino na českém trhu – Evolution Gaming, Pragmatic Play Live, Ezugi a Authentic Gaming. Včetně exkluzivních Smash branded stolů s českými dealery.",
            "gamesMini": "Crash games (Aviator, JetX, Spaceman, Mines), Plinko, Hi-Lo, Dice a další moderní rychlé hry. Plus Smash exkluzivní mini-hry s gamifikací.",
            "paymentsIntro": "Smash Casino má jedny z nejrychlejších výběrů na trhu – 12 hodin maximum. Podpora kryptoměn pro okamžité transakce.",
            "paymentMethods": ["Visa", "Mastercard", "Bankovní převod", "Skrill", "Neteller", "PaySafeCard", "Apple Pay", "Bitcoin", "Ethereum", "USDT", "MuchBetter", "PayPal"],
            "paymentCount": 12,
            "providersIntro": "Smash Casino spolupracuje s 60+ poskytovateli her – nejširší katalog na trhu s nejnovějšími tituly.",
            "providers": ["Pragmatic Play", "NetEnt", "Play'n GO", "Evolution", "Microgaming", "Nolimit City", "Hacksaw Gaming", "Push Gaming", "Big Time Gaming", "Quickspin", "Yggdrasil", "Red Tiger", "ELK Studios", "Thunderkick", "Spribe", "BGaming", "Wazdan", "Relax Gaming", "Endorphina", "Booongo", "Playson", "Habanero", "Betsoft", "Fantasma", "Peter & Sons", "AvatarUX", "Skywind", "Print Studios", "Onlyplay", "Stakelogic", "Pragmatic Play Live", "Ezugi", "Authentic Gaming", "iSoftBet", "Kalamba", "Mascot Gaming", "Belatra", "Evoplay", "Turbo Games", "4ThePlayer"],
            "providerCount": 60,
            "advantages": [
                "Největší uvítací bonus na českém trhu – 300% až 15 000 Kč",
                "250 free spinů BEZ wagering požadavků – ojedinělé!",
                "Nejrychlejší výběry – do 12 hodin",
                "Revoluční gamifikace s misemi a achievement systémem",
                "Battle Pass se sezónními odměnami",
                "Více než 5 000 her od 60+ poskytovatelů"
            ],
            "pros": ["Mega bonus 300% / 15 000 Kč", "FS bez wagering", "Výběry 12h", "Gamifikace + Battle Pass", "5 000+ her", "12 platebních metod"],
            "cons": ["Velmi nové (2026)", "Curaçao licence", "Kvalita podpory ještě nedokázaná"],
            "supportText": "Smash Casino nabízí 24/7 zákaznickou podporu přes live chat, email a discord komunitu. Plně v češtině. Live chat odpovídá v rekordním čase – pod 1 minutu díky modernímu AI asistentovi.",
            "faq": [
                {"q": "Co znamená 'free spiny bez wagering'?", "a": "Výhry z 250 uvítacích free spinů jsou okamžitě vyplaceny jako reálné peníze – bez nutnosti protáčení!"},
                {"q": "Jak funguje gamifikace?", "a": "Plníte denní mise a výzvy, sbíráte body, postupujete v Battle Pass úrovních a získáváte odměny – jako v moderní videohře."},
                {"q": "Je Smash Casino bezpečné navzdory tomu, že je nové?", "a": "Ano, Smash má licenci Curaçao, používá nejnovější SSL šifrování a hry jsou auditované eCOGRA."},
                {"q": "Co je Battle Pass?", "a": "Sezónní progres systém s 100+ odměnami. Trvá 3 měsíce. Premium verze odemkne extra odměny a exkluzivní obsah."},
                {"q": "Jak rychlé jsou opravdu výběry?", "a": "12 hodin maximum, kryptoměny obvykle během 5-30 minut. Nejrychlejší kasino na českém trhu."}
            ],
            "finalVerdict": "Smash Casino je revoluční přírůstek na český trh, který kombinuje největší uvítací bonus (300% / 15 000 Kč), 250 free spinů BEZ wagering, nejrychlejší výběry (12h) a unikátní gamifikační systém. Ačkoli je velmi nové, jeho ambiciózní nabídka a moderní přístup z něj okamžitě dělají jednoho z nejatraktivnějších operátorů. Pokud hledáte něco svěžího a inovativního, Smash je jasná volba."
        }
    }
]


def main():
    with open(PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    existing_ids = {c['id'] for c in data['casinos']}
    added = 0

    for casino in NEW:
        if casino['id'] in existing_ids:
            print(f'  ⏭  {casino["id"]} already exists, skipping')
            continue
        data['casinos'].append(casino)
        added += 1
        print(f'  ✓ Added {casino["name"]} ({casino["slug"]}) — rating {casino["rating"]}')

    with open(PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Validate
    with open(PATH, 'r', encoding='utf-8') as f:
        validated = json.load(f)

    print(f'\n✅ Total casinos: {len(validated["casinos"])} (+{added} new)')


if __name__ == '__main__':
    main()
