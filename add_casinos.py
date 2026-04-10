#!/usr/bin/env python3
"""
Script to add 13 new Czech casinos to data/casinos.json.
Each casino has full review data matching the existing structure.
"""

import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CASINOS_FILE = os.path.join(SCRIPT_DIR, "data", "casinos.json")

new_casinos = [
    {
        "id": "chance",
        "name": "Chance",
        "slug": "chance",
        "rating": 4.5,
        "bonus": "200 Kč bonus + 50 free spinů",
        "bonusAmount": "200 Kč",
        "wagering": "x30",
        "bonusUrl": "https://www.chance.cz/?aff=PLACEHOLDER",
        "freeSpins": 50,
        "minDeposit": 100,
        "description": "Tradiční český herní operátor s dlouhou historií v sázkách i online kasinu, licencovaný Ministerstvem financí ČR.",
        "features": ["Česká licence", "Sportovní sázky", "800+ her", "Rychlé výběry"],
        "review": {
            "metaDescription": "Chance casino recenze 2026 – 200 Kč bonus + 50 free spinů. Kompletní hodnocení her, bonusů, plateb a zákaznické podpory.",
            "reviewCount": 1583,
            "bonusAmount": "200 Kč",
            "freeSpinsCount": "50 FS",
            "withdrawalSpeed": "24-48h",
            "owner": "Chance a.s.",
            "yearCreated": "1991",
            "license": "MF ČR",
            "withdrawalRange": "100 Kč – 500 000 Kč",
            "withdrawalSpeedDetail": "24-48 hodin",
            "czechLanguage": "Ano",
            "mobile": "Ano + Aplikace",
            "introduction": "Chance je jedním z nejstarších a nejvíce zavedených herních operátorů v České republice. Společnost Chance a.s. působí na českém trhu od roku 1991 a za tu dobu si vybudovala silnou pozici jak v oblasti sportovních sázek, tak v online kasinu. Platforma drží licenci od Ministerstva financí ČR, což zaručuje plnou legalitu a ochranu hráčů. Chance nabízí více než 800 her od předních světových výrobců, sportovní sázky na tisíce událostí denně, live kasino a moderní mobilní aplikaci. Díky propojení sázkové kanceláře s kasinem mohou hráči využívat jeden účet pro veškeré herní aktivity.",
            "bonusIntro": "Chance vítá nové hráče bonusem 200 Kč a 50 free spiny po registraci. Podmínky protočení jsou stanoveny na 30x, což je standardní hodnota na českém trhu. Bonus je ideální pro vyzkoušení kasinových her bez velkého rizika.",
            "bonuses": [
                {"title": "Registrační bonus", "value": "200 Kč", "detail": "Po ověření účtu, protočení 30x"},
                {"title": "Free spiny", "value": "50 FS", "detail": "Na vybrané automaty"},
                {"title": "1. vklad bonus", "value": "100%", "detail": "Až do 3 000 Kč"},
                {"title": "Cashback", "value": "10%", "detail": "Týdenní vrácení ztrát až 1 000 Kč"}
            ],
            "weeklyPromo": "Chance pravidelně pořádá turnaje na automatech s prize poolem přes 150 000 Kč, nabízí páteční reload bonusy, víkendové free spiny a speciální akce navázané na sportovní události. Každý měsíc přibývají nové promo akce a sezónní soutěže.",
            "vipProgram": "Věrnostní program Chance odměňuje hráče body za každou sázku. Body lze vyměnit za bonusy, free spiny nebo reálné peníze. VIP hráči získávají osobního správce účtu, vyšší limity výběrů, exkluzivní turnaje a narozeninové odměny.",
            "gamesIntro": "Chance nabízí přes 800 her od více než 15 předních poskytovatelů. Katalog zahrnuje automaty, stolní hry, live kasino, sportovní sázky a rychlé hry. Všechny hry jsou certifikované a pravidelně auditované.",
            "gamesSlots": "Nabídka automatů čítá více než 550 titulů od Pragmatic Play, NetEnt, Play'n GO, Amatic, EGT a dalších. Od klasických ovocných automatů po moderní video sloty s megaways mechanikou. Minimální sázka začíná od 2 Kč, takže je platforma dostupná širokému spektru hráčů.",
            "gamesTable": "Stolní hry zahrnují evropskou a francouzskou ruletu, blackjack v několika variantách, baccarat a video poker. K dispozici jsou i méně tradiční varianty s různými limity sázek pro začátečníky i zkušenější hráče.",
            "gamesLive": "Live kasino od Evolution Gaming přináší živé stoly s profesionálními krupiéry v HD kvalitě. K dispozici je ruleta, blackjack, baccarat a populární game shows jako Crazy Time, Lightning Roulette a Dream Catcher. Vysílání probíhá nepřetržitě.",
            "gamesMini": "Sekce rychlých her obsahuje crash hry jako Aviator a JetX, dále Plinko, Mines, Dice a stírací losy. Tyto hry jsou ideální pro rychlou zábavu s možností okamžitých výher.",
            "paymentsIntro": "Chance podporuje všechny hlavní platební metody dostupné v České republice. Vklady jsou zpracovány okamžitě, výběry trvají 24 až 48 hodin.",
            "paymentMethods": ["Visa", "Mastercard", "Bankovní převod", "PaySafeCard", "Skrill", "Apple Pay", "Google Pay", "Maestro"],
            "paymentCount": 8,
            "providersIntro": "Chance spolupracuje s více než 15 předními výrobci her, což zaručuje pestrý a kvalitní herní katalog.",
            "providers": ["Pragmatic Play", "NetEnt", "Play'n GO", "Evolution", "Amatic", "EGT", "Endorphina", "Novomatic", "Synot Games", "Wazdan", "Spribe", "BGaming", "Yggdrasil", "Red Tiger", "Hacksaw", "iSoftBet"],
            "providerCount": 16,
            "advantages": [
                "Česká licence od Ministerstva financí – plná ochrana hráčů",
                "Více než 30 let zkušeností na českém trhu",
                "Kombinace sportovních sázek a kasina na jedné platformě",
                "Přes 800 certifikovaných her od 16 poskytovatelů",
                "Mobilní aplikace pro iOS i Android s kompletní funkčností",
                "Rychlé výběry do 24-48 hodin s nízkými limity"
            ],
            "pros": [
                "Česká licence MF ČR",
                "30+ let na trhu",
                "800+ her",
                "Sportovní sázky + kasino",
                "Mobilní aplikace",
                "Rychlé výběry 24-48h"
            ],
            "cons": [
                "Menší uvítací bonus oproti konkurenci",
                "Užší výběr platebních metod",
                "Live kasino mohlo mít více stolů"
            ],
            "supportText": "Zákaznická podpora Chance je dostupná přes live chat (denně 8-22h), email a telefonicky. Celý tým mluví česky a odpovídá profesionálně. Live chat obvykle odpoví do 5 minut. K dispozici je také sekce FAQ s nejčastějšími dotazy a návody.",
            "faq": [
                {"q": "Je Chance kasino legální v ČR?", "a": "Ano, Chance a.s. má platnou licenci od Ministerstva financí ČR a je plně legální pro české hráče starší 18 let."},
                {"q": "Jak získám uvítací bonus?", "a": "Bonus 200 Kč + 50 free spinů se připíše automaticky po dokončení registrace a ověření totožnosti."},
                {"q": "Mohu sázet na sporty i hrát kasino?", "a": "Ano, Chance nabízí obojí na jedné platformě s jedním účtem – sportovní sázky, kasino, live kasino i rychlé hry."},
                {"q": "Jaký je minimální vklad?", "a": "Minimální vklad je 100 Kč kartou nebo bankovním převodem."},
                {"q": "Jak rychle proběhne výběr výher?", "a": "Výběry jsou zpracovány do 24-48 hodin. Bankovní převody mohou trvat dalších 1-2 pracovní dny."}
            ],
            "finalVerdict": "Chance je spolehlivá volba pro české hráče, kteří hledají prověřeného operátora s českou licencí a dlouholetou tradicí. S bonusem 200 Kč + 50 free spinů, 800+ hrami a kombinací sázek a kasina nabízí ucelený herní zážitek podpořený více než třiceti lety zkušeností."
        }
    },
    {
        "id": "sazka",
        "name": "Sazka",
        "slug": "sazka",
        "rating": 4.4,
        "bonus": "300 Kč bonus + 30 free spinů",
        "bonusAmount": "300 Kč",
        "wagering": "x35",
        "bonusUrl": "https://www.sazka.cz/?aff=PLACEHOLDER",
        "freeSpins": 30,
        "minDeposit": 100,
        "description": "Legendární česká loterijní a herní společnost s historií od roku 1956, nyní s moderním online kasinem.",
        "features": ["Česká licence", "Loterie + kasino", "Silná značka", "500+ her"],
        "review": {
            "metaDescription": "Sazka casino recenze 2026 – 300 Kč bonus + 30 free spinů. Hodnocení her, bonusů, loterií a zákaznické podpory.",
            "reviewCount": 2105,
            "bonusAmount": "300 Kč",
            "freeSpinsCount": "30 FS",
            "withdrawalSpeed": "24-48h",
            "owner": "Sazka a.s.",
            "yearCreated": "1956",
            "license": "MF ČR",
            "withdrawalRange": "100 Kč – 1 000 000 Kč",
            "withdrawalSpeedDetail": "24-48 hodin",
            "czechLanguage": "Ano",
            "mobile": "Ano + Aplikace",
            "introduction": "Sazka je nejznámější českou herní značkou s historií sahající až do roku 1956. Co začalo jako loterijní společnost, se rozrostlo v moderní online herní platformu nabízející kasino, loterie, sportovní sázky a rychlé hry. Sazka a.s. je synonymem pro sázení v České republice a její jméno zná prakticky každý Čech. S licencí od Ministerstva financí ČR nabízí Sazka bezpečné a regulované herní prostředí s více než 500 hrami, profesionální českou podporou a důvěryhodností budovanou desítky let.",
            "bonusIntro": "Sazka nabízí 300 Kč bonus + 30 free spinů pro nové hráče kasina. Jedná se o jeden z nejvyšších bonusů bez vkladu na českém trhu. Podmínky protočení 35x jsou standardní a bonus umožňuje vyzkoušet platformu bez rizika.",
            "bonuses": [
                {"title": "Registrační bonus", "value": "300 Kč", "detail": "Bez vkladu, protočení 35x"},
                {"title": "Free spiny", "value": "30 FS", "detail": "Na vybrané automaty"},
                {"title": "1. vklad bonus", "value": "50%", "detail": "Až do 2 000 Kč"},
                {"title": "Loterijní bonus", "value": "100 Kč", "detail": "Na první loterijní tiket"}
            ],
            "weeklyPromo": "Sazka nabízí pravidelné loterijní speciály, turnaje na automatech s celkovými výhrami přes 100 000 Kč, víkendové free spiny a sezónní soutěže navázané na velké loterijní losování. Každý pátek nové reload bonusy pro aktivní hráče.",
            "vipProgram": "Věrnostní program Sazka sbírá body za každou sázku v kasinu i loteriích. Body lze vyměnit za bonusy, free spiny, loterijní tikety nebo věcné ceny. Aktivní hráči mají přístup k exkluzivním akcím a vyšším limitům.",
            "gamesIntro": "Sazka nabízí přes 500 her, které kombinují kasinové automaty, stolní hry, live kasino a unikátní loterijní produkty. Katalog je průběžně rozšiřován o nové tituly.",
            "gamesSlots": "Více než 350 automatů od Pragmatic Play, NetEnt, EGT, Amatic a dalších ověřených výrobců. Nabídka zahrnuje klasické ovocné automaty, video sloty a jackpotové hry. Minimální sázka začíná od 2 Kč.",
            "gamesTable": "Stolní hry zahrnují evropskou ruletu, blackjack, baccarat a video poker ve standardních variantách. Limity sázek jsou přizpůsobeny jak začátečníkům, tak zkušeným hráčům.",
            "gamesLive": "Live kasino od Evolution nabízí živé stoly s profesionálními krupiéry. Dostupná je živá ruleta, blackjack, baccarat a vybrané game shows. Vysílání v HD kvalitě.",
            "gamesMini": "Rychlé hry zahrnují crash hry (Aviator), Plinko, Mines a stírací losy. Sazka navíc nabízí unikátní loterijní produkty – Sportka, Šťastných 10, Eurojackpot a další, které jinde nenajdete.",
            "paymentsIntro": "Sazka podporuje hlavní české platební metody. Vklady jsou zpracovány okamžitě, výběry do 24-48 hodin.",
            "paymentMethods": ["Visa", "Mastercard", "Bankovní převod", "PaySafeCard", "Apple Pay", "Google Pay", "Sazka Pay"],
            "paymentCount": 7,
            "providersIntro": "Sazka spolupracuje s 12+ ověřenými výrobci her a průběžně rozšiřuje svou nabídku.",
            "providers": ["Pragmatic Play", "NetEnt", "EGT", "Amatic", "Evolution", "Endorphina", "Synot Games", "Wazdan", "Spribe", "BGaming", "Novomatic", "Play'n GO"],
            "providerCount": 12,
            "advantages": [
                "Nejznámější česká herní značka s historií od roku 1956",
                "Unikátní kombinace kasina a loterií na jedné platformě",
                "Česká licence MF ČR – maximální bezpečnost",
                "Nejvyšší registrační bonus 300 Kč bez vkladu",
                "Důvěryhodná značka, kterou zná každý Čech",
                "Profesionální česká zákaznická podpora"
            ],
            "pros": [
                "300 Kč bez vkladu",
                "Nejznámější česká značka",
                "Loterie + kasino",
                "Česká licence MF ČR",
                "Mobilní aplikace",
                "70 let tradice"
            ],
            "cons": [
                "Menší počet kasinových her (500+)",
                "Podmínky protočení 35x",
                "Méně poskytovatelů her než konkurence"
            ],
            "supportText": "Zákaznická podpora Sazka je dostupná přes live chat (denně 8-22h), email a telefonicky. Tým hovoří výhradně česky a je velmi vstřícný. Live chat odpovídá do 5 minut. Na webu je obsáhlá sekce nápovědy s často kladenými dotazy.",
            "faq": [
                {"q": "Mohu hrát Sportku i kasinové hry na jednom účtu?", "a": "Ano, Sazka nabízí loterie, kasino i sportovní sázky na jedné platformě s jedním účtem a jednou peněženkou."},
                {"q": "Jak získám registrační bonus 300 Kč?", "a": "Bonus se automaticky připíše po registraci a ověření totožnosti. Podmínky protočení jsou 35x."},
                {"q": "Nabízí Sazka mobilní aplikaci?", "a": "Ano, Sazka má mobilní aplikaci pro iOS i Android s plnou funkcionalitou kasina i loterií."},
                {"q": "Jaký je minimální vklad?", "a": "Minimální vklad je 100 Kč kartou nebo bankovním převodem."},
                {"q": "Je Sazka kasino bezpečné?", "a": "Ano, Sazka a.s. má licenci od MF ČR, je regulována českým zákonem a má desítky let zkušeností na trhu."}
            ],
            "finalVerdict": "Sazka je ideální volba pro hráče, kteří chtějí kombinovat loterijní produkty s online kasinem u nejdůvěryhodnější české značky. S bonusem 300 Kč bez vkladu, 30 free spiny a unikátní nabídkou loterií nabízí herní zážitek, který jinde nenajdete."
        }
    },
    {
        "id": "betx",
        "name": "BetX",
        "slug": "betx",
        "rating": 4.2,
        "bonus": "100% bonus až do 5 000 Kč",
        "bonusAmount": "5 000 Kč",
        "wagering": "x30",
        "bonusUrl": "https://www.betx.cz/?aff=PLACEHOLDER",
        "freeSpins": 0,
        "minDeposit": 100,
        "description": "Moderní český online herní operátor s důrazem na inovace, rychlé platby a širokou nabídku her.",
        "features": ["Česká licence", "Moderní platforma", "600+ her", "100% bonus"],
        "review": {
            "metaDescription": "BetX casino recenze 2026 – 100% bonus až do 5 000 Kč. Hodnocení her, bonusů, plateb a mobilního kasina.",
            "reviewCount": 423,
            "bonusAmount": "5 000 Kč",
            "freeSpinsCount": "—",
            "withdrawalSpeed": "24h",
            "owner": "BetX s.r.o.",
            "yearCreated": "2020",
            "license": "MF ČR",
            "withdrawalRange": "100 Kč – 300 000 Kč",
            "withdrawalSpeedDetail": "Do 24 hodin",
            "czechLanguage": "Ano",
            "mobile": "Ano (web)",
            "introduction": "BetX je moderní český herní operátor, který vstoupil na trh v roce 2020 s cílem nabídnout svěží alternativu k zavedeným značkám. Společnost BetX s.r.o. získala licenci od Ministerstva financí ČR a zaměřuje se na intuitivní uživatelský zážitek, rychlé platby a atraktivní bonusovou politiku. Platforma nabízí přes 600 her od ověřených poskytovatelů, sportovní sázky a moderní design optimalizovaný pro mobilní zařízení. BetX klade důraz na transparentnost podmínek a rychlost zpracování výběrů.",
            "bonusIntro": "BetX nabízí 100% bonus na první vklad až do 5 000 Kč. Podmínky protočení 30x jsou standardní. Bonus se aktivuje automaticky při prvním vkladu od 100 Kč a hráči mají 30 dní na splnění podmínek.",
            "bonuses": [
                {"title": "1. vklad bonus", "value": "100%", "detail": "Až 5 000 Kč, protočení 30x"},
                {"title": "Reload bonus", "value": "50%", "detail": "Každý pátek až 2 000 Kč"},
                {"title": "Cashback", "value": "5%", "detail": "Týdenní vrácení ztrát"},
                {"title": "Turnaje", "value": "50 000 Kč", "detail": "Měsíční prize pool"}
            ],
            "weeklyPromo": "BetX nabízí páteční reload bonus 50% až do 2 000 Kč, týdenní cashback 5%, denní výzvy s free spiny a pravidelné turnaje na automatech s celkovým prize poolem 50 000 Kč měsíčně. Nové promo akce každý týden.",
            "vipProgram": "BetX má jednoduchý věrnostní systém s třemi úrovněmi – Standard, Gold a Platinum. S vyšší úrovní rostou výhody: větší cashback, vyšší limity, prioritní výběry a exkluzivní bonusy. Postup je automatický na základě objemu sázek.",
            "gamesIntro": "BetX nabízí přes 600 her od 14 poskytovatelů. Katalog je zaměřen na kvalitu a zahrnuje nejpopulárnější automaty, stolní hry, live kasino a rychlé hry.",
            "gamesSlots": "Více než 450 automatů od Pragmatic Play, NetEnt, Play'n GO, Endorphina a dalších. Zaměření na moderní video sloty s vysokým RTP. Oblíbené tituly jako Gates of Olympus, Sweet Bonanza a Big Bass Bonanza.",
            "gamesTable": "Stolní hry zahrnují evropskou ruletu, blackjack, baccarat a video poker. Nabídka je kompaktní, ale kvalitní, s limity od 5 Kč do 50 000 Kč.",
            "gamesLive": "Live kasino od Evolution přináší živou ruletu, blackjack, baccarat a game shows jako Crazy Time a Monopoly Live. Stoly dostupné 24/7.",
            "gamesMini": "Rychlé hry zahrnují Aviator, Plinko, Mines, Dice a další crash hry od Spribe a Turbo Games. Ideální pro rychlou zábavu.",
            "paymentsIntro": "BetX podporuje české platební metody s důrazem na rychlost. Výběry jsou zpracovány do 24 hodin – jedny z nejrychlejších na českém trhu.",
            "paymentMethods": ["Visa", "Mastercard", "Bankovní převod", "PaySafeCard", "Apple Pay", "Google Pay", "Skrill"],
            "paymentCount": 7,
            "providersIntro": "BetX spolupracuje se 14 ověřenými výrobci her s důrazem na kvalitu a popularitu titulů.",
            "providers": ["Pragmatic Play", "NetEnt", "Play'n GO", "Evolution", "Endorphina", "Wazdan", "Spribe", "BGaming", "Hacksaw", "Push Gaming", "Red Tiger", "Yggdrasil", "Nolimit City", "Turbo Games"],
            "providerCount": 14,
            "advantages": [
                "Vysoký uvítací bonus 100% až do 5 000 Kč",
                "Výběry do 24 hodin – rychlé zpracování",
                "Moderní a přehledný design platformy",
                "Česká licence MF ČR – plná regulace",
                "Transparentní bonusové podmínky",
                "Pravidelné páteční reload bonusy"
            ],
            "pros": [
                "100% bonus až 5 000 Kč",
                "Výběry do 24h",
                "Česká licence MF ČR",
                "Moderní platforma",
                "600+ her",
                "Páteční reload bonus"
            ],
            "cons": [
                "Novější operátor – kratší historie",
                "Žádné free spiny bez vkladu",
                "Chybí mobilní aplikace (pouze web)"
            ],
            "supportText": "Zákaznická podpora BetX je dostupná přes live chat (denně 9-21h) a email. Tým hovoří česky a je velmi vstřícný. Live chat odpovídá do 3 minut. K dispozici je přehledná sekce FAQ.",
            "faq": [
                {"q": "Je BetX legální?", "a": "Ano, BetX s.r.o. má platnou licenci od Ministerstva financí ČR a je plně legální pro české hráče."},
                {"q": "Jak aktivovat bonus na první vklad?", "a": "Bonus 100% se aktivuje automaticky při prvním vkladu od 100 Kč. Maximum bonusu je 5 000 Kč s protočením 30x."},
                {"q": "Jak rychle proběhnou výběry?", "a": "Výběry jsou zpracovány do 24 hodin. Bankovní převody mohou trvat dalších 1-2 pracovní dny."},
                {"q": "Má BetX mobilní aplikaci?", "a": "BetX zatím nemá dedikovanou aplikaci, ale web je plně optimalizovaný pro mobilní zařízení a funguje skvěle na všech telefonech."},
                {"q": "Jaký je minimální vklad?", "a": "Minimální vklad je 100 Kč přes všechny dostupné platební metody."}
            ],
            "finalVerdict": "BetX je svěží volba pro hráče, kteří hledají moderní platformu s atraktivním bonusem. Se 100% bonusem až 5 000 Kč, rychlými výběry do 24 hodin a českou licencí nabízí kvalitní herní zážitek, i když je na trhu relativně krátce."
        }
    },
    {
        "id": "apollo-games",
        "name": "Apollo Games",
        "slug": "apollo-games",
        "rating": 4.1,
        "bonus": "100 Kč bonus + 50 free spinů",
        "bonusAmount": "100 Kč",
        "wagering": "x25",
        "bonusUrl": "https://www.apollogames.cz/?aff=PLACEHOLDER",
        "freeSpins": 50,
        "minDeposit": 50,
        "description": "Český výrobce her s vlastním online kasinem nabízejícím originální automaty a nízký vstupní vklad.",
        "features": ["Česká licence", "Vlastní hry", "Min. vklad 50 Kč", "Nízké protočení x25"],
        "review": {
            "metaDescription": "Apollo Games casino recenze 2026 – 100 Kč bonus + 50 free spinů. Hodnocení vlastních her, bonusů a plateb.",
            "reviewCount": 678,
            "bonusAmount": "100 Kč",
            "freeSpinsCount": "50 FS",
            "withdrawalSpeed": "24-48h",
            "owner": "Apollo Soft s.r.o.",
            "yearCreated": "2015",
            "license": "MF ČR",
            "withdrawalRange": "50 Kč – 200 000 Kč",
            "withdrawalSpeedDetail": "24-48 hodin",
            "czechLanguage": "Ano",
            "mobile": "Ano (web)",
            "introduction": "Apollo Games je unikátní na českém trhu, protože kombinuje roli výrobce her a provozovatele online kasina. Společnost Apollo Soft s.r.o. vyvíjí vlastní automaty a současně provozuje online kasino, kde tyto hry nabízí společně s tituly od dalších renomovaných výrobců. Od roku 2015 si Apollo Games buduje pozici díky originálnímu hernímu obsahu, nízkým vstupním bariérám a přátelskému přístupu k hráčům. Kasino drží licenci od Ministerstva financí ČR a nabízí přes 400 her.",
            "bonusIntro": "Apollo Games nabízí 100 Kč bonus bez vkladu + 50 free spinů na vlastní automaty. Protočení je pouze 25x – jedno z nejnižších na českém trhu. Bonus je perfektní pro vyzkoušení originálních her od Apollo.",
            "bonuses": [
                {"title": "Registrační bonus", "value": "100 Kč", "detail": "Bez vkladu, protočení 25x"},
                {"title": "Free spiny", "value": "50 FS", "detail": "Na Apollo automaty"},
                {"title": "1. vklad bonus", "value": "100%", "detail": "Až do 1 500 Kč"},
                {"title": "Turnaje", "value": "25 000 Kč", "detail": "Měsíční turnaje na Apollo hrách"}
            ],
            "weeklyPromo": "Apollo Games nabízí měsíční turnaje s prize poolem 25 000 Kč na vlastních automatech, denní výzvy s free spiny, reload bonusy a speciální akce při vydání nových Apollo her. Každý měsíc přibývají nové exkluzivní tituly.",
            "vipProgram": "Věrnostní program Apollo odměňuje hráče body za sázky. Body lze vyměnit za free spiny na nové Apollo hry, bonusy nebo reálné peníze. Aktivní hráči mají přednostní přístup k novým hrám a betaverím.",
            "gamesIntro": "Apollo Games nabízí přes 400 her, z nichž značná část pochází z vlastní dílny. Katalog doplňují hry od externích výrobců, stolní hry, live kasino a rychlé hry.",
            "gamesSlots": "Více než 280 automatů, z toho přes 100 vlastních titulů od Apollo Games. Vlastní hry se vyznačují originální grafikou, českými tématy a unikátními bonusovými funkcemi. K dispozici jsou i hry od Pragmatic Play, Amatic, EGT a dalších.",
            "gamesTable": "Stolní hry zahrnují evropskou ruletu, blackjack a video poker v základních variantách. Nabídka je menší, ale pokrývá klíčové tituly.",
            "gamesLive": "Live kasino od Evolution nabízí živou ruletu, blackjack a baccarat. Menší počet stolů, ale kvalitní stream v HD kvalitě s profesionálními krupiéry.",
            "gamesMini": "Rychlé hry zahrnují Aviator, Plinko, Mines a stírací losy. Unikátní vlastní mini-hry od Apollo doplňují nabídku.",
            "paymentsIntro": "Apollo Games podporuje základní české platební metody. Minimální vklad je pouhých 50 Kč – jeden z nejnižších na trhu.",
            "paymentMethods": ["Visa", "Mastercard", "Bankovní převod", "PaySafeCard", "Apple Pay", "Google Pay"],
            "paymentCount": 6,
            "providersIntro": "Apollo Games primárně nabízí vlastní hry a doplňuje je tituly od 10 externích poskytovatelů.",
            "providers": ["Apollo Games", "Pragmatic Play", "Amatic", "EGT", "Evolution", "Endorphina", "Synot Games", "Wazdan", "Spribe", "Novomatic", "BGaming"],
            "providerCount": 11,
            "advantages": [
                "Originální vlastní hry, které jinde nenajdete",
                "Nejnižší protočení bonusu na trhu – pouze 25x",
                "Nízký minimální vklad pouhých 50 Kč",
                "Česká licence MF ČR – bezpečné hraní",
                "České motivy a témata ve vlastních automatech",
                "Přednostní přístup k novým hrám pro věrné hráče"
            ],
            "pros": [
                "Vlastní originální hry",
                "Nízké protočení 25x",
                "Min. vklad 50 Kč",
                "Česká licence MF ČR",
                "České automaty",
                "100 Kč bez vkladu"
            ],
            "cons": [
                "Menší celkový počet her (400+)",
                "Omezená nabídka stolních her",
                "Chybí mobilní aplikace",
                "Nižší maximální limity výběrů"
            ],
            "supportText": "Zákaznická podpora Apollo Games je dostupná přes live chat (denně 9-20h) a email. Tým hovoří česky a je ochotný pomoci s jakýmkoli dotazem. Odpověď na live chatu obvykle do 5 minut.",
            "faq": [
                {"q": "Co jsou Apollo Games automaty?", "a": "Apollo Games vyvíjí vlastní automaty s originální grafikou a českými tématy. Tyto hry nenajdete u žádného jiného operátora."},
                {"q": "Jaké je protočení bonusu?", "a": "Protočení je pouze 25x – jedno z nejnižších na českém trhu, což znamená snazší splnění podmínek."},
                {"q": "Mohu hrát Apollo hry jinde?", "a": "Některé Apollo hry najdete i u jiných operátorů, ale nejširší výběr a exkluzivní novinky jsou k dispozici přímo na apollogames.cz."},
                {"q": "Jaký je minimální vklad?", "a": "Minimální vklad je pouhých 50 Kč – ideální pro hráče s menším rozpočtem."},
                {"q": "Má Apollo Games českou licenci?", "a": "Ano, Apollo Soft s.r.o. má platnou licenci od Ministerstva financí ČR."}
            ],
            "finalVerdict": "Apollo Games je skvělá volba pro hráče, kteří hledají originální herní obsah a nízké vstupní bariéry. S vlastními automaty, protočením pouze 25x, bonusem 100 Kč bez vkladu a minimálním vkladem 50 Kč nabízí unikátní herní zážitek na českém trhu."
        }
    },
    {
        "id": "forbes-casino",
        "name": "Forbes Casino",
        "slug": "forbes-casino",
        "rating": 4.3,
        "bonus": "500 Kč bonus + 100 free spinů",
        "bonusAmount": "500 Kč",
        "wagering": "x30",
        "bonusUrl": "https://www.forbes-casino.cz/?aff=PLACEHOLDER",
        "freeSpins": 100,
        "minDeposit": 200,
        "description": "Prémiová kasinová značka s fyzickými pobočkami po celé ČR a bohatým online kasinem s 700+ hrami.",
        "features": ["Česká licence", "Fyzické kasina", "700+ her", "Prémiový zážitek"],
        "review": {
            "metaDescription": "Forbes Casino recenze 2026 – 500 Kč bonus + 100 free spinů. Hodnocení her, fyzických kasin, bonusů a VIP programu.",
            "reviewCount": 1342,
            "bonusAmount": "500 Kč",
            "freeSpinsCount": "100 FS",
            "withdrawalSpeed": "24h",
            "owner": "Forbes Casino a.s.",
            "yearCreated": "2005",
            "license": "MF ČR",
            "withdrawalRange": "200 Kč – 1 000 000 Kč",
            "withdrawalSpeedDetail": "Do 24 hodin",
            "czechLanguage": "Ano",
            "mobile": "Ano + Aplikace",
            "introduction": "Forbes Casino je prémiová česká kasinová značka, která od roku 2005 provozuje síť fyzických kasin a moderní online platformu. Forbes Casino a.s. je součástí Forbes Group a je synonymem pro kvalitní a exkluzivní herní zážitek. S licencí od Ministerstva financí ČR nabízí bezpečné prostředí jak v kamenných pobočkách po celé České republice, tak na online platformě s více než 700 hrami. Forbes Casino spojuje eleganci tradičního kasina s pohodlím moderního online hraní.",
            "bonusIntro": "Forbes Casino nabízí jeden z nejatraktivnějších uvítacích balíčků – 500 Kč bez vkladu + 100 free spinů. Podmínky protočení 30x jsou standardní. Tento štědrý bonus odráží prémiový přístup značky k novým hráčům.",
            "bonuses": [
                {"title": "Registrační bonus", "value": "500 Kč", "detail": "Bez vkladu, protočení 30x"},
                {"title": "Free spiny", "value": "100 FS", "detail": "Na Top automaty"},
                {"title": "1. vklad bonus", "value": "100%", "detail": "Až do 10 000 Kč"},
                {"title": "VIP cashback", "value": "15%", "detail": "Pro VIP členy"}
            ],
            "weeklyPromo": "Forbes Casino nabízí exkluzivní turnaje s prize poolem přes 250 000 Kč, VIP večery v kamenných kasinech, páteční reload bonusy, denní free spiny a sezónní soutěže. Propojení online a offline přináší unikátní promo akce.",
            "vipProgram": "Forbes VIP Club nabízí pět úrovní – Silver, Gold, Platinum, Diamond a Black. VIP členové získávají vyšší cashback až 15%, osobního správce účtu, pozvánky na exkluzivní VIP večery v kamenných kasinech, rychlejší výběry a narozeninové balíčky.",
            "gamesIntro": "Forbes Casino nabízí přes 700 her od 18 poskytovatelů. Online katalog je doplněn o exkluzivní hry dostupné v kamenných pobočkách. Důraz na kvalitu a rozmanitost.",
            "gamesSlots": "Více než 500 automatů od Pragmatic Play, NetEnt, Play'n GO, Novomatic, Amatic a dalších. Prémiové jackpotové hry, klasické automaty i nejnovější video sloty. Mnoho titulů známých z kamenných Forbes kasin.",
            "gamesTable": "Rozsáhlá nabídka stolních her – ruleta (evropská, francouzská), blackjack, baccarat, poker a craps. Limity od 10 Kč do 200 000 Kč – vhodné pro všechny typy hráčů.",
            "gamesLive": "Live kasino od Evolution a Pragmatic Play Live nabízí desítky živých stolů. VIP stoly s vysokými limity, speed varianty a exkluzivní Forbes-branded stoly. Profesionální krupiéři v HD kvalitě.",
            "gamesMini": "Crash hry (Aviator, JetX), Plinko, Mines, Dice a stírací losy. Forbes Casino nabízí i virtuální sporty a arkádové hry pro změnu tempa.",
            "paymentsIntro": "Forbes Casino podporuje všechny hlavní platební metody a jako bonus nabízí hotovostní vklady a výběry v kamenných pobočkách.",
            "paymentMethods": ["Visa", "Mastercard", "Bankovní převod", "PaySafeCard", "Skrill", "Neteller", "Apple Pay", "Google Pay", "Hotovost (pobočky)"],
            "paymentCount": 9,
            "providersIntro": "Forbes Casino spolupracuje s 18 předními výrobci her a nabízí mix mezinárodních hitů a lokálních favoritů.",
            "providers": ["Pragmatic Play", "NetEnt", "Play'n GO", "Evolution", "Novomatic", "Amatic", "EGT", "Endorphina", "Synot Games", "Wazdan", "Spribe", "Red Tiger", "Hacksaw", "BGaming", "Yggdrasil", "Pragmatic Play Live", "Push Gaming", "iSoftBet"],
            "providerCount": 18,
            "advantages": [
                "Nejvyšší registrační bonus na českém trhu – 500 Kč + 100 FS",
                "Síť kamenných kasin po celé České republice",
                "Prémiový VIP program s exkluzivními výhodami",
                "Výběry do 24 hodin – rychlé zpracování",
                "Propojení online a offline herního zážitku",
                "700+ her od 18 ověřených poskytovatelů"
            ],
            "pros": [
                "500 Kč + 100 FS bez vkladu",
                "Kamenná kasina v ČR",
                "Výběry do 24h",
                "Prémiový VIP program",
                "700+ her",
                "Česká licence MF ČR"
            ],
            "cons": [
                "Vyšší minimální vklad 200 Kč",
                "Některé hry dostupné jen v kamenných kasinech",
                "Omezená zákaznická podpora o víkendech"
            ],
            "supportText": "Zákaznická podpora Forbes Casino je dostupná přes live chat (denně 9-22h), email a telefonicky. Na pobočkách vám pomohou osobně. Podpora je plně v češtině a profesionální. Live chat odpovídá do 3 minut.",
            "faq": [
                {"q": "Má Forbes Casino fyzické pobočky?", "a": "Ano, Forbes Casino provozuje síť kamenných kasin po celé ČR. Můžete si užít online i offline herní zážitek."},
                {"q": "Jak získám bonus 500 Kč?", "a": "Bonus se automaticky připíše po registraci a ověření totožnosti. Free spiny se aktivují v herním lobbyu."},
                {"q": "Mohu vybrat výhry na pobočce?", "a": "Ano, výhry z online kasina lze vybrat i v hotovosti na kamenné pobočce Forbes Casino."},
                {"q": "Jaký je VIP program?", "a": "Forbes VIP Club má 5 úrovní s rostoucími výhodami – cashback až 15%, osobní správce účtu, VIP večery a exkluzivní turnaje."},
                {"q": "Je Forbes Casino bezpečné?", "a": "Ano, Forbes Casino a.s. má českou licenci od MF ČR a provozuje kamenná kasina s plnou regulací."}
            ],
            "finalVerdict": "Forbes Casino je prémiová volba pro hráče, kteří oceňují kvalitu a exkluzivitu. S nejvyšším registračním bonusem 500 Kč + 100 FS, sítí kamenných kasin a prémiový VIP programem nabízí luxusní herní zážitek jak online, tak offline."
        }
    },
    {
        "id": "merkurxtip",
        "name": "MerkurXtip",
        "slug": "merkurxtip",
        "rating": 4.2,
        "bonus": "150 Kč bonus + 75 free spinů",
        "bonusAmount": "150 Kč",
        "wagering": "x30",
        "bonusUrl": "https://www.merkurxtip.cz/?aff=PLACEHOLDER",
        "freeSpins": 75,
        "minDeposit": 100,
        "description": "Online kasino od německé skupiny Gauselmann s tradiční značkou Merkur a širokou nabídkou automatů.",
        "features": ["Česká licence", "Merkur automaty", "500+ her", "Německá kvalita"],
        "review": {
            "metaDescription": "MerkurXtip casino recenze 2026 – 150 Kč bonus + 75 free spinů. Hodnocení Merkur her, bonusů a plateb.",
            "reviewCount": 765,
            "bonusAmount": "150 Kč",
            "freeSpinsCount": "75 FS",
            "withdrawalSpeed": "24-48h",
            "owner": "Merkur Casino a.s.",
            "yearCreated": "2019",
            "license": "MF ČR",
            "withdrawalRange": "100 Kč – 500 000 Kč",
            "withdrawalSpeedDetail": "24-48 hodin",
            "czechLanguage": "Ano",
            "mobile": "Ano (web)",
            "introduction": "MerkurXtip je online kasinová platforma provozovaná společností Merkur Casino a.s., která je součástí německé skupiny Gauselmann – jednoho z největších výrobců herních automatů na světě. Na český trh vstoupil MerkurXtip v roce 2019 a rychle si získal oblibu díky legendárním Merkur automatům a německé kvalitě zpracování. Platforma drží licenci od Ministerstva financí ČR a nabízí přes 500 her, včetně exkluzivních Merkur titulů, které jsou známé z kamenných kasin po celé Evropě.",
            "bonusIntro": "MerkurXtip nabízí 150 Kč bez vkladu + 75 free spinů na populární Merkur automaty. Podmínky protočení 30x jsou férové. Bonus je ideální pro seznámení s legendárními Merkur hrami.",
            "bonuses": [
                {"title": "Registrační bonus", "value": "150 Kč", "detail": "Bez vkladu, protočení 30x"},
                {"title": "Free spiny", "value": "75 FS", "detail": "Na Merkur automaty"},
                {"title": "1. vklad bonus", "value": "100%", "detail": "Až do 5 000 Kč"},
                {"title": "Denní jackpoty", "value": "Různé", "detail": "Denní a hodinové jackpoty"}
            ],
            "weeklyPromo": "MerkurXtip nabízí denní a hodinové jackpoty na Merkur automatech, týdenní turnaje s prize poolem 75 000 Kč, reload bonusy a free spiny na nové hry. Speciální promo akce při vydání nových Merkur titulů.",
            "vipProgram": "Merkur Loyalty program nabízí body za každou sázku na Merkur automatech i ostatních hrách. Body lze vyměnit za bonusy a free spiny. Aktivní hráči postupují úrovněmi s rostoucími výhodami a exkluzivními nabídkami.",
            "gamesIntro": "MerkurXtip nabízí přes 500 her s důrazem na legendární Merkur automaty. Katalog doplňují hry od dalších předních výrobců, stolní hry a live kasino.",
            "gamesSlots": "Více než 350 automatů, z toho přes 80 exkluzivních Merkur titulů – včetně klasik jako Blazing Star, Double Triple Chance, Eye of Horus a Gold of Egypt. Doplněno o hry od Pragmatic Play, NetEnt a dalších.",
            "gamesTable": "Stolní hry zahrnují evropskou ruletu, blackjack, baccarat a video poker. Merkur přidává i vlastní varianty stolních her s unikátními funkcemi.",
            "gamesLive": "Live kasino od Evolution nabízí živou ruletu, blackjack, baccarat a game shows. Profesionální krupiéři v HD kvalitě, stoly dostupné nepřetržitě.",
            "gamesMini": "Rychlé hry zahrnují Aviator, Plinko, Mines, Dice a unikátní Merkur scratch karty. Ideální pro rychlou herní session.",
            "paymentsIntro": "MerkurXtip podporuje hlavní české platební metody s rychlým zpracováním transakcí.",
            "paymentMethods": ["Visa", "Mastercard", "Bankovní převod", "PaySafeCard", "Apple Pay", "Google Pay", "Skrill", "Trustly"],
            "paymentCount": 8,
            "providersIntro": "MerkurXtip nabízí hry od Merkur/Gauselmann a 12 dalších předních výrobců.",
            "providers": ["Merkur Gaming", "Pragmatic Play", "NetEnt", "Play'n GO", "Evolution", "Amatic", "EGT", "Endorphina", "Novomatic", "Synot Games", "Wazdan", "Spribe", "BGaming"],
            "providerCount": 13,
            "advantages": [
                "Legendární Merkur automaty – Blazing Star, Eye of Horus a další",
                "Zázemí německé skupiny Gauselmann – lídra v herním průmyslu",
                "Česká licence MF ČR – plně regulované prostředí",
                "Denní a hodinové jackpoty na vybraných automatech",
                "Exkluzivní Merkur hry nedostupné u jiných operátorů",
                "Kvalitní uvítací balíček 150 Kč + 75 free spinů"
            ],
            "pros": [
                "Legendární Merkur automaty",
                "Německá kvalita (Gauselmann)",
                "Česká licence MF ČR",
                "150 Kč + 75 FS bez vkladu",
                "Denní jackpoty",
                "500+ her"
            ],
            "cons": [
                "Novější na českém online trhu",
                "Chybí mobilní aplikace",
                "Menší nabídka live kasina"
            ],
            "supportText": "Zákaznická podpora MerkurXtip je dostupná přes live chat (denně 9-21h) a email. Tým hovoří česky a je dobře vyškolený. Odpověď na live chatu do 5 minut. Dostupná je také podrobná sekce FAQ.",
            "faq": [
                {"q": "Co jsou Merkur automaty?", "a": "Merkur automaty jsou legendární herní automaty od německé společnosti Gauselmann, známé z kasin po celé Evropě. Tituly jako Blazing Star nebo Eye of Horus patří ke klasikám."},
                {"q": "Je MerkurXtip legální v ČR?", "a": "Ano, Merkur Casino a.s. má licenci od Ministerstva financí ČR a je plně legální pro české hráče."},
                {"q": "Najdu Merkur hry u jiných kasin?", "a": "Některé Merkur hry jsou dostupné i jinde, ale nejširší výběr včetně exkluzivních titulů najdete přímo na MerkurXtip."},
                {"q": "Jak fungují denní jackpoty?", "a": "Denní a hodinové jackpoty musí spadnout do určeného času. Čím blíže k deadline, tím vyšší šance na výhru."},
                {"q": "Jaký je minimální vklad?", "a": "Minimální vklad je 100 Kč přes kartu, bankovní převod nebo PaySafeCard."}
            ],
            "finalVerdict": "MerkurXtip je ideální volba pro fanoušky klasických herních automatů. S legendárními Merkur hrami, zázemím německé skupiny Gauselmann, českou licencí a bonusem 150 Kč + 75 FS nabízí kvalitní herní zážitek s důrazem na tradici a spolehlivost."
        }
    },
    {
        "id": "kajot-casino",
        "name": "Kajot Casino",
        "slug": "kajot-casino",
        "rating": 4.0,
        "bonus": "100 Kč bonus bez vkladu",
        "bonusAmount": "100 Kč",
        "wagering": "x35",
        "bonusUrl": "https://www.kajot-casino.cz/?aff=PLACEHOLDER",
        "freeSpins": 0,
        "minDeposit": 100,
        "description": "Zavedená česká kasinová značka s dlouhou historií kamenných heren a online kasinem s vlastními hrami.",
        "features": ["Česká licence", "Vlastní Kajot hry", "Kamenné herny", "Bez vkladu bonus"],
        "review": {
            "metaDescription": "Kajot Casino recenze 2026 – 100 Kč bonus bez vkladu. Hodnocení Kajot her, bonusů, plateb a zákaznické podpory.",
            "reviewCount": 934,
            "bonusAmount": "100 Kč",
            "freeSpinsCount": "—",
            "withdrawalSpeed": "48h",
            "owner": "KAJOT Group",
            "yearCreated": "1996",
            "license": "MF ČR",
            "withdrawalRange": "100 Kč – 300 000 Kč",
            "withdrawalSpeedDetail": "Do 48 hodin",
            "czechLanguage": "Ano",
            "mobile": "Ano (web)",
            "introduction": "Kajot Casino je jednou z nejznámějších českých herních značek s historií sahající do roku 1996. KAJOT Group začínal jako provozovatel kamenných heren a herních automatů a za téměř tři dekády si vybudoval silnou pozici na českém trhu. Online kasino nabízí charakteristické Kajot automaty, které čeští hráči znají z kamenných provozoven. S licencí od Ministerstva financí ČR a více než 300 hrami nabízí Kajot Casino kombinaci nostalgie a moderního online hraní.",
            "bonusIntro": "Kajot Casino nabízí 100 Kč bonus bez vkladu ihned po registraci. Žádné free spiny, ale čistý peněžní bonus, který lze použít na jakékoliv hry v kasinu. Podmínky protočení 35x.",
            "bonuses": [
                {"title": "Registrační bonus", "value": "100 Kč", "detail": "Bez vkladu, protočení 35x"},
                {"title": "1. vklad bonus", "value": "100%", "detail": "Až do 2 000 Kč"},
                {"title": "Cashback", "value": "10%", "detail": "Týdenní vrácení ztrát"},
                {"title": "Kajot turnaje", "value": "30 000 Kč", "detail": "Měsíční turnaje na Kajot hrách"}
            ],
            "weeklyPromo": "Kajot Casino nabízí měsíční turnaje na vlastních automatech s výhrami přes 30 000 Kč, týdenní cashback 10%, reload bonusy a speciální akce na nové Kajot tituly. Věrní hráči dostávají pravidelné bonusy a free spiny.",
            "vipProgram": "Kajot VIP program je založen na bodovém systému – za každou sázku sbíráte body, které lze vyměnit za bonusy. VIP hráči mají přístup k exkluzivním turnajům, vyšším limitům a osobní podpoře. Postup je automatický.",
            "gamesIntro": "Kajot Casino nabízí přes 300 her s důrazem na vlastní Kajot automaty. Katalog doplňují hry od externích výrobců, stolní hry a live kasino.",
            "gamesSlots": "Více než 200 automatů, z toho přes 60 vlastních Kajot titulů – klasické ovocné automaty, 7's, jokerové hry a tematické sloty. Kajot hry jsou známé jednoduchostí a vysokou frekvencí výher. Doplněno o tituly od Amatic, EGT a Pragmatic Play.",
            "gamesTable": "Stolní hry zahrnují evropskou ruletu, blackjack a video poker v základních variantách. Nabídka je kompaktní, ale funkční.",
            "gamesLive": "Live kasino nabízí živou ruletu a blackjack od Evolution. Menší počet stolů, ale spolehlivý stream a profesionální krupiéři.",
            "gamesMini": "Rychlé hry zahrnují stírací losy, Dice a jednoduché karetní hry. Kajot Casino se zaměřuje spíše na tradiční automaty než na moderní crash hry.",
            "paymentsIntro": "Kajot Casino podporuje základní české platební metody s výběry do 48 hodin.",
            "paymentMethods": ["Visa", "Mastercard", "Bankovní převod", "PaySafeCard", "Apple Pay"],
            "paymentCount": 5,
            "providersIntro": "Kajot Casino primárně nabízí vlastní hry a doplňuje je tituly od 8 dalších výrobců.",
            "providers": ["Kajot Games", "Pragmatic Play", "Amatic", "EGT", "Evolution", "Novomatic", "Endorphina", "Synot Games", "Wazdan"],
            "providerCount": 9,
            "advantages": [
                "Ikonické Kajot automaty známé z českých heren",
                "Česká licence MF ČR – plná regulace a bezpečnost",
                "100 Kč bonus bez vkladu – vyzkoušejte bez rizika",
                "Téměř 30 let zkušeností na českém trhu",
                "Nostalgický herní zážitek s moderním rozhraním",
                "Měsíční turnaje s atraktivními cenami"
            ],
            "pros": [
                "Vlastní Kajot automaty",
                "100 Kč bez vkladu",
                "Česká licence MF ČR",
                "Téměř 30 let tradice",
                "Týdenní cashback 10%",
                "Jednoduché a přehledné rozhraní"
            ],
            "cons": [
                "Menší celkový počet her (300+)",
                "Výběry do 48 hodin",
                "Omezené platební metody",
                "Žádné free spiny k bonusu"
            ],
            "supportText": "Zákaznická podpora Kajot Casino je dostupná přes live chat (denně 9-20h) a email. Tým mluví česky a je vstřícný. Odpověď do 5 minut na live chatu. Sekce FAQ pokrývá základní dotazy.",
            "faq": [
                {"q": "Co jsou Kajot automaty?", "a": "Kajot automaty jsou české herní automaty od KAJOT Group, známé z kamenných heren po celé ČR. Vyznačují se jednoduchostí a vysokou frekvencí výher."},
                {"q": "Je bonus 100 Kč opravdu bez vkladu?", "a": "Ano, 100 Kč se připíše ihned po registraci a ověření účtu. Žádný vklad není potřeba."},
                {"q": "Má Kajot Casino kamenné pobočky?", "a": "KAJOT Group provozuje síť kamenných heren, ale online kasino funguje nezávisle na své platformě."},
                {"q": "Jaký je minimální vklad?", "a": "Minimální vklad je 100 Kč přes kartu nebo bankovní převod."},
                {"q": "Nabízí Kajot Casino live kasino?", "a": "Ano, live kasino nabízí živou ruletu a blackjack od Evolution, i když v menším rozsahu."}
            ],
            "finalVerdict": "Kajot Casino je nostalgická volba pro hráče, kteří znají a milují české herní automaty. S ikonickými Kajot hrami, bonusem 100 Kč bez vkladu a českou licencí nabízí jednoduchý a důvěryhodný herní zážitek. Menší počet her kompenzuje originalita vlastních titulů."
        }
    },
    {
        "id": "betor",
        "name": "Betor",
        "slug": "betor",
        "rating": 3.9,
        "bonus": "100% bonus až do 2 000 Kč",
        "bonusAmount": "2 000 Kč",
        "wagering": "x30",
        "bonusUrl": "https://www.betor.cz/?aff=PLACEHOLDER",
        "freeSpins": 0,
        "minDeposit": 100,
        "description": "Novější český herní operátor s čistým designem, rychlými platbami a zaměřením na sportovní sázky a kasino.",
        "features": ["Česká licence", "Sázky + kasino", "400+ her", "Rychlé platby"],
        "review": {
            "metaDescription": "Betor casino recenze 2026 – 100% bonus až do 2 000 Kč. Hodnocení her, sportovních sázek, plateb a podpory.",
            "reviewCount": 312,
            "bonusAmount": "2 000 Kč",
            "freeSpinsCount": "—",
            "withdrawalSpeed": "24-48h",
            "owner": "Betor a.s.",
            "yearCreated": "2021",
            "license": "MF ČR",
            "withdrawalRange": "100 Kč – 200 000 Kč",
            "withdrawalSpeedDetail": "24-48 hodin",
            "czechLanguage": "Ano",
            "mobile": "Ano (web)",
            "introduction": "Betor je relativně nový hráč na českém herním trhu, který zahájil provoz v roce 2021. Společnost Betor a.s. se zaměřuje na kombinaci sportovních sázek a online kasina na jedné přehledné platformě. Přestože je na trhu krátce, získal Betor licenci od Ministerstva financí ČR a nabízí kvalitní herní zážitek s více než 400 hrami. Platforma se vyznačuje moderním a přehledným designem, rychlými platbami a transparentními podmínkami. Betor cílí na mladší generaci hráčů, kteří oceňují jednoduchost a mobilní přístupnost.",
            "bonusIntro": "Betor nabízí 100% bonus na první vklad až do 2 000 Kč. Podmínky protočení 30x jsou standardní. Bonus se aktivuje automaticky při prvním vkladu od 100 Kč.",
            "bonuses": [
                {"title": "1. vklad bonus", "value": "100%", "detail": "Až 2 000 Kč, protočení 30x"},
                {"title": "Sázkový bonus", "value": "500 Kč", "detail": "Na první sportovní sázku"},
                {"title": "Cashback", "value": "5%", "detail": "Týdenní vrácení ztrát"},
                {"title": "Free spiny", "value": "20 FS", "detail": "Týdenní odměna za aktivitu"}
            ],
            "weeklyPromo": "Betor nabízí týdenní cashback 5%, free spiny za aktivitu, turnaje na automatech a speciální sázkové nabídky na sportovní události. Promo akce se obměňují každý týden.",
            "vipProgram": "Betor zatím nemá formální VIP program, ale aktivní hráči dostávají personalizované nabídky, vyšší bonusy a prioritní zpracování výběrů na základě jejich herní aktivity.",
            "gamesIntro": "Betor nabízí přes 400 her kombinujících kasinové automaty, stolní hry, live kasino a sportovní sázky. Katalog se neustále rozšiřuje.",
            "gamesSlots": "Více než 300 automatů od Pragmatic Play, NetEnt, Play'n GO, Endorphina a dalších. Zaměření na populární a moderní tituly s vysokým RTP. Oblíbené jsou Gates of Olympus, Big Bass Bonanza a Sweet Bonanza.",
            "gamesTable": "Stolní hry zahrnují evropskou ruletu, blackjack a video poker v základních variantách. Kompaktní, ale kvalitní nabídka.",
            "gamesLive": "Live kasino od Evolution nabízí živou ruletu, blackjack a game shows. Menší počet stolů, ale spolehlivý a kvalitní stream.",
            "gamesMini": "Rychlé hry zahrnují Aviator, Plinko, Mines a Dice od Spribe. Ideální pro rychlou zábavu mezi sportovními sázkami.",
            "paymentsIntro": "Betor podporuje české platební metody s důrazem na rychlost a jednoduchost. Výběry do 24-48 hodin.",
            "paymentMethods": ["Visa", "Mastercard", "Bankovní převod", "PaySafeCard", "Apple Pay", "Google Pay"],
            "paymentCount": 6,
            "providersIntro": "Betor spolupracuje s 10 ověřenými výrobci her a postupně rozšiřuje svou nabídku.",
            "providers": ["Pragmatic Play", "NetEnt", "Play'n GO", "Evolution", "Endorphina", "Wazdan", "Spribe", "BGaming", "Red Tiger", "Hacksaw"],
            "providerCount": 10,
            "advantages": [
                "Moderní a přehledný design platformy",
                "Česká licence MF ČR – bezpečné hraní",
                "Kombinace sportovních sázek a kasina",
                "Transparentní bonusové podmínky",
                "Rychlé platby do 24-48 hodin",
                "Optimalizováno pro mobilní zařízení"
            ],
            "pros": [
                "Moderní design",
                "Česká licence MF ČR",
                "Sázky + kasino",
                "100% bonus do 2 000 Kč",
                "Rychlé platby",
                "Přehledné rozhraní"
            ],
            "cons": [
                "Kratší historie na trhu (od 2021)",
                "Menší počet her (400+)",
                "Žádný bonus bez vkladu",
                "Chybí VIP program"
            ],
            "supportText": "Zákaznická podpora Betor je dostupná přes live chat (denně 9-21h) a email. Tým mluví česky a odpovídá rychle. Live chat obvykle do 3 minut. K dispozici je základní sekce FAQ.",
            "faq": [
                {"q": "Je Betor legální v ČR?", "a": "Ano, Betor a.s. má platnou licenci od Ministerstva financí ČR a je plně legální."},
                {"q": "Jak aktivovat bonus na první vklad?", "a": "Bonus 100% se aktivuje automaticky při prvním vkladu od 100 Kč. Maximum je 2 000 Kč s protočením 30x."},
                {"q": "Nabízí Betor sportovní sázky?", "a": "Ano, Betor kombinuje kasino a sportovní sázky na jedné platformě s jedním účtem."},
                {"q": "Jaký je minimální vklad?", "a": "Minimální vklad je 100 Kč přes všechny dostupné platební metody."},
                {"q": "Má Betor mobilní aplikaci?", "a": "Betor zatím nemá dedikovanou aplikaci, ale mobilní web je plně optimalizovaný a funguje výborně na všech zařízeních."}
            ],
            "finalVerdict": "Betor je slibná novinka na českém trhu, ideální pro hráče, kteří hledají moderní platformu s čistým designem a kombinací sázek s kasinem. Se 100% bonusem do 2 000 Kč a českou licencí nabízí solidní základ, i když mu zatím chybí historie a širší herní katalog."
        }
    },
    {
        "id": "betano",
        "name": "Betano",
        "slug": "betano",
        "rating": 4.4,
        "bonus": "100% bonus až do 10 000 Kč",
        "bonusAmount": "10 000 Kč",
        "wagering": "x25",
        "bonusUrl": "https://www.betano.cz/?aff=PLACEHOLDER",
        "freeSpins": 0,
        "minDeposit": 100,
        "description": "Mezinárodní herní platforma od řeckého Kaizen Gaming s obrovskou nabídkou her a sportovních sázek.",
        "features": ["Česká licence", "1500+ her", "Vysoký bonus", "Nízké protočení x25"],
        "review": {
            "metaDescription": "Betano casino recenze 2026 – 100% bonus až do 10 000 Kč. Hodnocení 1500+ her, sportovních sázek a live kasina.",
            "reviewCount": 1087,
            "bonusAmount": "10 000 Kč",
            "freeSpinsCount": "—",
            "withdrawalSpeed": "24h",
            "owner": "Kaizen Gaming",
            "yearCreated": "2016",
            "license": "MF ČR",
            "withdrawalRange": "100 Kč – 1 000 000 Kč",
            "withdrawalSpeedDetail": "Do 24 hodin",
            "czechLanguage": "Ano",
            "mobile": "Ano + Aplikace",
            "introduction": "Betano je mezinárodní herní platforma provozovaná řeckou společností Kaizen Gaming, jedním z nejrychleji rostoucích herních operátorů v Evropě. Na český trh vstoupilo Betano v roce 2022 a rychle se etablovalo díky obrovské nabídce her, atraktivním bonusům a profesionálnímu přístupu. S licencí od Ministerstva financí ČR nabízí Betano plně legální a bezpečnou platformu s více než 1 500 hrami od 25+ poskytovatelů, sportovními sázkami na tisíce událostí a jedním z nejvyšších uvítacích bonusů na trhu.",
            "bonusIntro": "Betano nabízí 100% bonus na první vklad až do 10 000 Kč – jeden z nejvyšších na českém trhu. Navíc s protočením pouze 25x, což je výrazně pod průměrem. Bonus se aktivuje automaticky při prvním vkladu.",
            "bonuses": [
                {"title": "1. vklad bonus", "value": "100%", "detail": "Až 10 000 Kč, protočení 25x"},
                {"title": "Sázkový bonus", "value": "100%", "detail": "Až 3 000 Kč na sázky"},
                {"title": "Free spiny", "value": "50 FS", "detail": "Za první vklad na automaty"},
                {"title": "Cashback", "value": "10%", "detail": "Týdenní vrácení na live kasino"}
            ],
            "weeklyPromo": "Betano nabízí širokou paletu promo akcí – denní jackpot drops, týdenní turnaje s prize poolem 200 000 Kč, live kasino cashback, speciální sázkové nabídky na velké sportovní události a sezónní soutěže s hodnotnými cenami.",
            "vipProgram": "Betano VIP program nabízí čtyři úrovně s rostoucími výhodami – vyšší bonusy, rychlejší výběry, osobní account manažer, exkluzivní turnaje a pozvánky na sportovní události. Postup je na základě herní aktivity.",
            "gamesIntro": "Betano nabízí impozantních 1 500+ her od 25+ poskytovatelů. Jedná se o jeden z nejrozsáhlejších katalogů dostupných na českém trhu, zahrnující automaty, stolní hry, live kasino a sportovní sázky.",
            "gamesSlots": "Více než 1 100 automatů od Pragmatic Play, NetEnt, Play'n GO, Microgaming, Nolimit City, Hacksaw Gaming a dalších. Od klasických slotů po megaways a jackpotové hry. Filtrování podle výrobce, typu a popularity.",
            "gamesTable": "Rozsáhlá nabídka stolních her – ruleta, blackjack, baccarat, poker a craps v desítkách variant. Limity od 5 Kč do 500 000 Kč pro všechny typy hráčů.",
            "gamesLive": "Jedno z největších live kasin na českém trhu s desítkami stolů od Evolution a Pragmatic Play Live. Ruleta, blackjack, baccarat, game shows, speed varianty a VIP stoly.",
            "gamesMini": "Crash hry (Aviator, Spaceman, JetX), Plinko, Mines, Dice, Hi-Lo a další rychlé hry. Virtuální sporty a eSport sázky doplňují nabídku.",
            "paymentsIntro": "Betano podporuje širokou škálu platebních metod s rychlým zpracováním. Výběry do 24 hodin.",
            "paymentMethods": ["Visa", "Mastercard", "Bankovní převod", "PaySafeCard", "Skrill", "Neteller", "Apple Pay", "Google Pay", "MuchBetter", "Trustly"],
            "paymentCount": 10,
            "providersIntro": "Betano spolupracuje s 25+ předními výrobci her – jeden z nejširších výběrů na českém trhu.",
            "providers": ["Pragmatic Play", "NetEnt", "Play'n GO", "Evolution", "Microgaming", "Nolimit City", "Hacksaw", "Push Gaming", "Big Time Gaming", "Quickspin", "Red Tiger", "Yggdrasil", "Thunderkick", "ELK Studios", "Wazdan", "Endorphina", "Spribe", "BGaming", "Relax Gaming", "iSoftBet", "Pragmatic Play Live", "Stakelogic", "Playson", "Betsoft", "Amatic"],
            "providerCount": 25,
            "advantages": [
                "Nejvyšší uvítací bonus na českém trhu – až 10 000 Kč",
                "Nízké protočení pouze 25x – výrazně pod průměrem",
                "Přes 1 500 her od 25+ poskytovatelů",
                "Rychlé výběry do 24 hodin",
                "Zázemí mezinárodního operátora Kaizen Gaming",
                "Kompletní platforma: kasino + sázky + live kasino"
            ],
            "pros": [
                "Bonus až 10 000 Kč",
                "Protočení pouze 25x",
                "1 500+ her",
                "Výběry do 24h",
                "25+ poskytovatelů",
                "Česká licence MF ČR"
            ],
            "cons": [
                "Kratší působení na českém trhu (od 2022)",
                "Žádný bonus bez vkladu",
                "Podpora ne vždy plně v češtině"
            ],
            "supportText": "Zákaznická podpora Betano je dostupná 24/7 přes live chat a email. Podpora v češtině s možností angličtiny. Live chat odpovídá do 2 minut. K dispozici je rozsáhlé centrum nápovědy s FAQ.",
            "faq": [
                {"q": "Je Betano legální v Česku?", "a": "Ano, Betano má licenci od Ministerstva financí ČR a je plně legální pro české hráče."},
                {"q": "Jaký je maximální bonus?", "a": "Uvítací bonus je 100% na první vklad až do 10 000 Kč s protočením pouze 25x."},
                {"q": "Kolik her Betano nabízí?", "a": "Betano nabízí přes 1 500 her od 25+ poskytovatelů – automaty, stolní hry, live kasino a sportovní sázky."},
                {"q": "Jak rychlé jsou výběry?", "a": "Výběry jsou zpracovány do 24 hodin. E-peněženky jsou nejrychlejší, bankovní převody 1-3 dny."},
                {"q": "Nabízí Betano sportovní sázky?", "a": "Ano, Betano je primárně sportovní sázkový operátor s tisíci událostmi denně a živým sázením."}
            ],
            "finalVerdict": "Betano je jednou z nejsilnějších novinek na českém trhu. S bonusem až 10 000 Kč, protočením 25x, 1 500+ hrami a rychlými výběry nabízí kompletní herní platformu na mezinárodní úrovni. Ideální pro hráče, kteří hledají maximální hodnotu za vklad."
        }
    },
    {
        "id": "luckybet",
        "name": "LuckyBet",
        "slug": "luckybet",
        "rating": 4.1,
        "bonus": "200 Kč bonus + 100 free spinů",
        "bonusAmount": "200 Kč",
        "wagering": "x30",
        "bonusUrl": "https://www.luckybet.cz/?aff=PLACEHOLDER",
        "freeSpins": 100,
        "minDeposit": 100,
        "description": "Český operátor kombinující sportovní sázky a online kasino s atraktivním uvítacím balíčkem.",
        "features": ["Česká licence", "Sázky + kasino", "500+ her", "200 Kč + 100 FS"],
        "review": {
            "metaDescription": "LuckyBet casino recenze 2026 – 200 Kč bonus + 100 free spinů. Hodnocení her, sázek, bonusů a plateb.",
            "reviewCount": 534,
            "bonusAmount": "200 Kč",
            "freeSpinsCount": "100 FS",
            "withdrawalSpeed": "24-48h",
            "owner": "LuckyBet s.r.o.",
            "yearCreated": "2020",
            "license": "MF ČR",
            "withdrawalRange": "100 Kč – 300 000 Kč",
            "withdrawalSpeedDetail": "24-48 hodin",
            "czechLanguage": "Ano",
            "mobile": "Ano (web)",
            "introduction": "LuckyBet je český herní operátor, který vstoupil na trh v roce 2020 s cílem nabídnout kompletní sázkovou a kasinovou platformu pro české hráče. Společnost LuckyBet s.r.o. drží licenci od Ministerstva financí ČR a zaměřuje se na kombinaci sportovních sázek, online kasina a live kasina na jedné platformě. S více než 500 hrami, atraktivním uvítacím bonusem 200 Kč + 100 free spinů a profesionální českou podporou si LuckyBet buduje stabilní pozici mezi českými hráči.",
            "bonusIntro": "LuckyBet nabízí 200 Kč bez vkladu + 100 free spinů na vybrané automaty. Podmínky protočení 30x jsou standardní. Kombinace peněžního bonusu a free spinů je jedním z nejatraktivnějších balíčků na českém trhu.",
            "bonuses": [
                {"title": "Registrační bonus", "value": "200 Kč", "detail": "Bez vkladu, protočení 30x"},
                {"title": "Free spiny", "value": "100 FS", "detail": "Na vybrané automaty"},
                {"title": "1. vklad bonus", "value": "100%", "detail": "Až do 5 000 Kč"},
                {"title": "Sázkový bonus", "value": "300 Kč", "detail": "Na první sportovní sázku"}
            ],
            "weeklyPromo": "LuckyBet nabízí týdenní turnaje na automatech s prize poolem 50 000 Kč, denní free spiny za aktivitu, reload bonusy každý pátek a speciální sázkové akce na fotbalové a hokejové zápasy.",
            "vipProgram": "Věrnostní program LuckyBet sbírá body za každou sázku. Body lze vyměnit za bonusy, free spiny a reálné peníze. Aktivní hráči postupují třemi úrovněmi s rostoucími výhodami – vyšší cashback, prioritní výběry a exkluzivní nabídky.",
            "gamesIntro": "LuckyBet nabízí přes 500 her od 15 poskytovatelů. Katalog zahrnuje automaty, stolní hry, live kasino a sportovní sázky.",
            "gamesSlots": "Více než 370 automatů od Pragmatic Play, NetEnt, Play'n GO, Endorphina, Wazdan a dalších. Populární tituly jako Book of Dead, Sweet Bonanza, Gates of Olympus a české automaty. Minimální sázka od 2 Kč.",
            "gamesTable": "Stolní hry zahrnují evropskou ruletu, blackjack, baccarat a video poker. Nabídka pokrývá klíčové tituly s limity pro různé typy hráčů.",
            "gamesLive": "Live kasino od Evolution nabízí živou ruletu, blackjack, baccarat a game shows jako Crazy Time a Lightning Roulette. Kvalitní HD stream s profesionálními krupiéry.",
            "gamesMini": "Rychlé hry zahrnují Aviator, Spaceman, Plinko, Mines a Dice. Ideální doplněk ke sportovním sázkám.",
            "paymentsIntro": "LuckyBet podporuje české platební metody s výběry do 24-48 hodin.",
            "paymentMethods": ["Visa", "Mastercard", "Bankovní převod", "PaySafeCard", "Skrill", "Apple Pay", "Google Pay"],
            "paymentCount": 7,
            "providersIntro": "LuckyBet spolupracuje s 15 ověřenými výrobci her.",
            "providers": ["Pragmatic Play", "NetEnt", "Play'n GO", "Evolution", "Endorphina", "Wazdan", "Spribe", "BGaming", "Red Tiger", "Hacksaw", "Yggdrasil", "Push Gaming", "Amatic", "EGT", "Synot Games"],
            "providerCount": 15,
            "advantages": [
                "Atraktivní uvítací balíček 200 Kč + 100 free spinů",
                "Česká licence MF ČR – bezpečné a legální hraní",
                "Kombinace sportovních sázek a kasina",
                "500+ her od 15 ověřených poskytovatelů",
                "Profesionální česká zákaznická podpora",
                "Pravidelné turnaje a promo akce"
            ],
            "pros": [
                "200 Kč + 100 FS bez vkladu",
                "Česká licence MF ČR",
                "Sázky + kasino",
                "500+ her",
                "15 poskytovatelů",
                "Turnaje a promo akce"
            ],
            "cons": [
                "Novější operátor (od 2020)",
                "Chybí mobilní aplikace",
                "Nižší maximální limity výběrů"
            ],
            "supportText": "Zákaznická podpora LuckyBet je dostupná přes live chat (denně 9-22h) a email. Tým hovoří česky a je vstřícný. Live chat odpovídá do 4 minut. K dispozici je přehledná sekce FAQ.",
            "faq": [
                {"q": "Je LuckyBet legální?", "a": "Ano, LuckyBet s.r.o. má platnou licenci od Ministerstva financí ČR a je plně legální pro české hráče."},
                {"q": "Jak získám bonus 200 Kč + 100 FS?", "a": "Bonus se automaticky připíše po registraci a ověření totožnosti. Free spiny se aktivují v herním lobbyu."},
                {"q": "Nabízí LuckyBet sportovní sázky?", "a": "Ano, LuckyBet nabízí sportovní sázky na fotbal, hokej, tenis, basket a další sporty včetně živého sázení."},
                {"q": "Jaký je minimální vklad?", "a": "Minimální vklad je 100 Kč kartou nebo bankovním převodem."},
                {"q": "Jak rychle proběhne výběr?", "a": "Výběry jsou zpracovány do 24-48 hodin. Bankovní převody mohou trvat dalších 1-2 pracovní dny."}
            ],
            "finalVerdict": "LuckyBet je kvalitní český operátor s atraktivním uvítacím balíčkem 200 Kč + 100 FS. S českou licencí, 500+ hrami a kombinací sázek a kasina nabízí solidní herní zážitek pro české hráče, kteří hledají spolehlivou a českou platformu."
        }
    },
    {
        "id": "mostbet",
        "name": "Mostbet",
        "slug": "mostbet",
        "rating": 3.8,
        "bonus": "100% bonus až do 8 000 Kč",
        "bonusAmount": "8 000 Kč",
        "wagering": "x30",
        "bonusUrl": "https://www.mostbet.cz/?aff=PLACEHOLDER",
        "freeSpins": 0,
        "minDeposit": 50,
        "description": "Mezinárodní herní platforma s obrovským katalogem 2000+ her a širokou škálou platebních metod.",
        "features": ["Mezinárodní platforma", "2000+ her", "Nízký vklad 50 Kč", "Kryptoměny"],
        "review": {
            "metaDescription": "Mostbet casino recenze 2026 – 100% bonus až do 8 000 Kč. Hodnocení 2000+ her, plateb a sportovních sázek.",
            "reviewCount": 456,
            "bonusAmount": "8 000 Kč",
            "freeSpinsCount": "—",
            "withdrawalSpeed": "24-72h",
            "owner": "Bizbon N.V.",
            "yearCreated": "2009",
            "license": "Curaçao",
            "withdrawalRange": "50 Kč – 500 000 Kč",
            "withdrawalSpeedDetail": "24-72 hodin",
            "czechLanguage": "Částečně",
            "mobile": "Ano + Aplikace",
            "introduction": "Mostbet je mezinárodní herní platforma provozovaná společností Bizbon N.V. pod licencí z Curaçao. Na trhu od roku 2009, Mostbet obsluhuje hráče ve více než 90 zemích a nabízí jeden z nejrozsáhlejších herních katalogů – přes 2 000 her od 30+ poskytovatelů. Platforma kombinuje kasino, sportovní sázky, eSport, live kasino a rychlé hry. Mostbet se vyznačuje nízkými vstupními bariérami (min. vklad 50 Kč), širokou škálou platebních metod včetně kryptoměn a agresivní bonusovou politikou.",
            "bonusIntro": "Mostbet nabízí 100% bonus na první vklad až do 8 000 Kč. Podmínky protočení 30x jsou standardní. Bonus se aktivuje automaticky a hráči mají 30 dní na splnění podmínek.",
            "bonuses": [
                {"title": "1. vklad bonus", "value": "100%", "detail": "Až 8 000 Kč, protočení 30x"},
                {"title": "Free spiny", "value": "200 FS", "detail": "Za první vklad na automaty"},
                {"title": "Sázkový bonus", "value": "100%", "detail": "Až 5 000 Kč na sázky"},
                {"title": "Cashback", "value": "10%", "detail": "Týdenní cashback na kasino"}
            ],
            "weeklyPromo": "Mostbet nabízí denní jackpot drops, týdenní turnaje s vysokými prize pooly, cashback na kasino i sázky, bonusy za série výher a speciální promo akce na velké sportovní události. Nabídka se mění denně.",
            "vipProgram": "Mostbet má propracovaný VIP program s 10 úrovněmi. Za každou sázku sbíráte body, které vás posouvají výš. Vyšší úrovně přinášejí lepší cashback, vyšší bonusy, osobní manažera, rychlejší výběry a exkluzivní nabídky.",
            "gamesIntro": "Mostbet nabízí jeden z největších herních katalogů na trhu – přes 2 000 her od 30+ poskytovatelů. Od klasických automatů přes stolní hry po obrovské live kasino a sportovní sázky.",
            "gamesSlots": "Více než 1 500 automatů od Pragmatic Play, NetEnt, Play'n GO, Microgaming, Hacksaw, Nolimit City, BGaming a dalších. Obrovský výběr od klasik po nejnovější release. Jackpotové sítě a exkluzivní tituly.",
            "gamesTable": "Rozsáhlá nabídka stolních her – ruleta, blackjack, baccarat, poker, craps a sic bo v desítkách variant. Limity od 2 Kč do 200 000 Kč.",
            "gamesLive": "Rozsáhlé live kasino od Evolution, Pragmatic Play Live, Ezugi a dalších. Desítky stolů s profesionálními dealery – ruleta, blackjack, baccarat, game shows a speed varianty.",
            "gamesMini": "Obrovský výběr rychlých her – Aviator, Spaceman, JetX, Plinko, Mines, Dice, Hi-Lo, Crash, Limbo a další od Spribe, Turbo Games a dalších. Virtuální sporty a eSport sázky.",
            "paymentsIntro": "Mostbet podporuje širokou škálu platebních metod včetně kryptoměn. Minimální vklad pouhých 50 Kč.",
            "paymentMethods": ["Visa", "Mastercard", "Bankovní převod", "PaySafeCard", "Skrill", "Neteller", "Bitcoin", "Ethereum", "USDT", "Apple Pay", "Google Pay"],
            "paymentCount": 11,
            "providersIntro": "Mostbet spolupracuje s 30+ výrobci her – jeden z nejširších výběrů na trhu.",
            "providers": ["Pragmatic Play", "NetEnt", "Play'n GO", "Evolution", "Microgaming", "Hacksaw", "Nolimit City", "BGaming", "Spribe", "Turbo Games", "Wazdan", "Endorphina", "Red Tiger", "Yggdrasil", "Push Gaming", "Quickspin", "Big Time Gaming", "Thunderkick", "ELK Studios", "Relax Gaming", "Betsoft", "Habanero", "Playson", "Booongo", "Evoplay", "Pragmatic Play Live", "Ezugi", "KA Gaming", "Spinomenal", "Tom Horn"],
            "providerCount": 30,
            "advantages": [
                "Obrovský katalog 2 000+ her od 30+ poskytovatelů",
                "Nízký minimální vklad pouhých 50 Kč",
                "Kryptoměny jako platební metoda (BTC, ETH, USDT)",
                "Vysoký uvítací bonus až 8 000 Kč",
                "Propracovaný VIP program s 10 úrovněmi",
                "Mobilní aplikace pro iOS i Android"
            ],
            "pros": [
                "2 000+ her",
                "Bonus až 8 000 Kč",
                "Min. vklad 50 Kč",
                "Kryptoměny (BTC, ETH)",
                "30+ poskytovatelů",
                "VIP program s 10 úrovněmi"
            ],
            "cons": [
                "Bez české licence (Curaçao)",
                "Web částečně v češtině",
                "Pomalejší výběry (24-72h)",
                "Méně známá značka v ČR"
            ],
            "supportText": "Zákaznická podpora Mostbet je dostupná 24/7 přes live chat a email. Podpora primárně v angličtině, čeština je omezená. Live chat odpovídá do 3 minut. K dispozici je centrum nápovědy v angličtině.",
            "faq": [
                {"q": "Má Mostbet českou licenci?", "a": "Ne, Mostbet operuje pod licencí z Curaçao. Nemá specifickou českou licenci od MF ČR."},
                {"q": "Mohu platit kryptoměnami?", "a": "Ano, Mostbet přijímá Bitcoin, Ethereum, USDT a další kryptoměny pro vklady i výběry."},
                {"q": "Jaký je minimální vklad?", "a": "Minimální vklad je pouhých 50 Kč – jeden z nejnižších na trhu."},
                {"q": "Kolik her Mostbet nabízí?", "a": "Mostbet nabízí přes 2 000 her od 30+ poskytovatelů – automaty, stolní hry, live kasino, sázky a rychlé hry."},
                {"q": "Je Mostbet bezpečný?", "a": "Mostbet má licenci z Curaçao a využívá SSL šifrování. Na trhu působí od roku 2009 s miliony uživatelů celosvětově."}
            ],
            "finalVerdict": "Mostbet je volba pro hráče, kteří hledají maximální rozmanitost her a podporu kryptoměn. S 2 000+ hrami, bonusem 8 000 Kč a nejnižším vkladem 50 Kč nabízí obrovskou hodnotu. Absence české licence je hlavní nevýhodou, ale mezinárodní reputace a široký herní katalog to částečně kompenzují."
        }
    },
    {
        "id": "doxxbet",
        "name": "DOXXbet",
        "slug": "doxxbet",
        "rating": 4.0,
        "bonus": "150 Kč bonus + 50 free spinů",
        "bonusAmount": "150 Kč",
        "wagering": "x30",
        "bonusUrl": "https://www.doxxbet.cz/?aff=PLACEHOLDER",
        "freeSpins": 50,
        "minDeposit": 100,
        "description": "Slovenský operátor s českou licencí nabízející sportovní sázky a online kasino s 600+ hrami.",
        "features": ["Česká licence", "SK + CZ trh", "Sázky + kasino", "600+ her"],
        "review": {
            "metaDescription": "DOXXbet casino recenze 2026 – 150 Kč bonus + 50 free spinů. Hodnocení her, sázek, bonusů a zákaznické podpory.",
            "reviewCount": 623,
            "bonusAmount": "150 Kč",
            "freeSpinsCount": "50 FS",
            "withdrawalSpeed": "24-48h",
            "owner": "DOXX a.s.",
            "yearCreated": "2008",
            "license": "MF ČR + SK",
            "withdrawalRange": "100 Kč – 500 000 Kč",
            "withdrawalSpeedDetail": "24-48 hodin",
            "czechLanguage": "Ano",
            "mobile": "Ano + Aplikace",
            "introduction": "DOXXbet je slovenská herní společnost DOXX a.s., která úspěšně expandovala na český trh. Na Slovensku působí od roku 2008 a postupně si vybudovala silnou pozici v regionu střední Evropy. Pro český trh drží DOXXbet licenci od Ministerstva financí ČR, což zaručuje plnou legalitu a ochranu hráčů. Platforma nabízí kombinaci sportovních sázek a online kasina s více než 600 hrami od 16 poskytovatelů. DOXXbet těží ze znalosti středoevropského trhu a nabízí platformu plně lokalizovanou pro české hráče.",
            "bonusIntro": "DOXXbet nabízí 150 Kč bez vkladu + 50 free spinů pro nové hráče. Podmínky protočení 30x jsou standardní. Bonus je dostupný ihned po registraci a ověření účtu.",
            "bonuses": [
                {"title": "Registrační bonus", "value": "150 Kč", "detail": "Bez vkladu, protočení 30x"},
                {"title": "Free spiny", "value": "50 FS", "detail": "Na vybrané automaty"},
                {"title": "1. vklad bonus", "value": "100%", "detail": "Až do 3 000 Kč"},
                {"title": "Sázkový bonus", "value": "200 Kč", "detail": "Na první sportovní sázku"}
            ],
            "weeklyPromo": "DOXXbet nabízí týdenní turnaje na automatech, reload bonusy, free spiny za aktivitu a speciální sázkové nabídky na české a slovenské sportovní ligy. Pravidelné promo akce na hokej a fotbal.",
            "vipProgram": "DOXXbet věrnostní program sbírá body za sázky v kasinu i na sporty. Body lze vyměnit za bonusy a free spiny. Aktivní hráči získávají personalizované nabídky a vyšší bonusy.",
            "gamesIntro": "DOXXbet nabízí přes 600 her od 16 poskytovatelů. Katalog zahrnuje automaty, stolní hry, live kasino a kompletní sportovní sázky.",
            "gamesSlots": "Více než 430 automatů od Pragmatic Play, NetEnt, Play'n GO, Amatic, EGT, Endorphina a dalších. Široký výběr od klasických slotů po moderní video automaty s megaways mechanikou.",
            "gamesTable": "Stolní hry zahrnují evropskou ruletu, blackjack, baccarat a video poker. Limity od 5 Kč do 100 000 Kč pro různé typy hráčů.",
            "gamesLive": "Live kasino od Evolution nabízí živou ruletu, blackjack, baccarat a game shows. Kvalitní stream s profesionálními krupiéry.",
            "gamesMini": "Rychlé hry zahrnují Aviator, Plinko, Mines, Dice a stírací losy. Virtuální sporty doplňují nabídku.",
            "paymentsIntro": "DOXXbet podporuje české i slovenské platební metody s výběry do 24-48 hodin.",
            "paymentMethods": ["Visa", "Mastercard", "Bankovní převod", "PaySafeCard", "Skrill", "Apple Pay", "Google Pay", "Trustly"],
            "paymentCount": 8,
            "providersIntro": "DOXXbet spolupracuje s 16 ověřenými výrobci her s důrazem na kvalitu a oblíbenost v regionu.",
            "providers": ["Pragmatic Play", "NetEnt", "Play'n GO", "Evolution", "Amatic", "EGT", "Endorphina", "Novomatic", "Synot Games", "Wazdan", "Spribe", "BGaming", "Red Tiger", "Hacksaw", "Yggdrasil", "iSoftBet"],
            "providerCount": 16,
            "advantages": [
                "Dvojí licence – česká MF ČR i slovenská",
                "Zkušenosti ze středoevropského trhu od roku 2008",
                "Kombinace sportovních sázek a kasina",
                "600+ her od 16 ověřených poskytovatelů",
                "Plná lokalizace pro české hráče",
                "Mobilní aplikace pro iOS i Android"
            ],
            "pros": [
                "Česká + slovenská licence",
                "150 Kč + 50 FS bez vkladu",
                "600+ her",
                "Sázky + kasino",
                "Mobilní aplikace",
                "Zkušenosti od 2008"
            ],
            "cons": [
                "Méně známá značka v ČR",
                "Výběry 24-48 hodin",
                "Menší nabídka live kasina"
            ],
            "supportText": "Zákaznická podpora DOXXbet je dostupná přes live chat (denně 9-21h) a email. Tým hovoří česky i slovensky a je vstřícný. Live chat odpovídá do 5 minut. Sekce FAQ pokrývá nejčastější dotazy.",
            "faq": [
                {"q": "Je DOXXbet legální v Česku?", "a": "Ano, DOXXbet má licenci od Ministerstva financí ČR i slovenského regulátora a je plně legální pro české hráče."},
                {"q": "Jak získám bonus 150 Kč?", "a": "Bonus se automaticky připíše po registraci a ověření totožnosti. Free spiny se aktivují v herním lobbyu."},
                {"q": "Nabízí DOXXbet sportovní sázky?", "a": "Ano, DOXXbet nabízí kompletní sportovní sázky včetně českých a slovenských lig, živého sázení a virtuálních sportů."},
                {"q": "Jaký je minimální vklad?", "a": "Minimální vklad je 100 Kč přes kartu, bankovní převod nebo PaySafeCard."},
                {"q": "Funguje DOXXbet i na Slovensku?", "a": "Ano, DOXXbet je původem slovenská společnost a funguje na obou trzích s příslušnými licencemi."}
            ],
            "finalVerdict": "DOXXbet je spolehlivý středoevropský operátor s dvojí licencí a znalostí regionálního trhu. S bonusem 150 Kč + 50 FS, 600+ hrami a kombinací sázek a kasina nabízí kvalitní herní zážitek, podpořený 15+ lety zkušeností na slovenském a českém trhu."
        }
    },
    {
        "id": "victoria-tip",
        "name": "Victoria Tip",
        "slug": "victoria-tip",
        "rating": 3.9,
        "bonus": "100 Kč bonus + 30 free spinů",
        "bonusAmount": "100 Kč",
        "wagering": "x35",
        "bonusUrl": "https://www.victoriatip.cz/?aff=PLACEHOLDER",
        "freeSpins": 30,
        "minDeposit": 100,
        "description": "Střední český herní operátor s českou licencí, sportovními sázkami a rostoucí nabídkou kasinových her.",
        "features": ["Česká licence", "Sázky + kasino", "350+ her", "Jednoduché rozhraní"],
        "review": {
            "metaDescription": "Victoria Tip casino recenze 2026 – 100 Kč bonus + 30 free spinů. Hodnocení her, sázek, bonusů a plateb.",
            "reviewCount": 389,
            "bonusAmount": "100 Kč",
            "freeSpinsCount": "30 FS",
            "withdrawalSpeed": "48h",
            "owner": "Victoria Tip a.s.",
            "yearCreated": "2010",
            "license": "MF ČR",
            "withdrawalRange": "100 Kč – 200 000 Kč",
            "withdrawalSpeedDetail": "Do 48 hodin",
            "czechLanguage": "Ano",
            "mobile": "Ano (web)",
            "introduction": "Victoria Tip je střední český herní operátor, který na trhu působí od roku 2010. Společnost Victoria Tip a.s. provozuje sportovní sázky a online kasino s licencí od Ministerstva financí ČR. Platforma se vyznačuje jednoduchostí, přehledným rozhraním a zaměřením na české hráče. S více než 350 hrami a kompletní nabídkou sportovních sázek nabízí Victoria Tip solidní herní zážitek bez zbytečných komplikací. Kasino postupně rozšiřuje svou nabídku a přidává nové poskytovatele her.",
            "bonusIntro": "Victoria Tip nabízí 100 Kč bez vkladu + 30 free spinů po registraci. Podmínky protočení 35x. Bonus je jednoduchý a přímočarý – ideální pro vyzkoušení platformy.",
            "bonuses": [
                {"title": "Registrační bonus", "value": "100 Kč", "detail": "Bez vkladu, protočení 35x"},
                {"title": "Free spiny", "value": "30 FS", "detail": "Na vybrané automaty"},
                {"title": "1. vklad bonus", "value": "50%", "detail": "Až do 1 500 Kč"},
                {"title": "Cashback", "value": "5%", "detail": "Týdenní vrácení ztrát"}
            ],
            "weeklyPromo": "Victoria Tip nabízí týdenní cashback 5%, reload bonusy, free spiny za aktivitu a speciální sázkové nabídky na české sportovní ligy. Promo akce jsou jednoduché a srozumitelné.",
            "vipProgram": "Victoria Tip nemá formální VIP program, ale aktivní hráči dostávají personalizované bonusy, vyšší cashback a speciální nabídky na základě jejich herní aktivity.",
            "gamesIntro": "Victoria Tip nabízí přes 350 her od 10 poskytovatelů. Katalog se postupně rozšiřuje a zahrnuje automaty, stolní hry, live kasino a sportovní sázky.",
            "gamesSlots": "Více než 250 automatů od Pragmatic Play, Amatic, EGT, Endorphina a dalších. Zaměření na prověřené a oblíbené tituly. Katalog se průběžně rozšiřuje o nové hry.",
            "gamesTable": "Stolní hry zahrnují evropskou ruletu, blackjack a video poker v základních variantách. Jednoduchá, ale funkční nabídka.",
            "gamesLive": "Live kasino od Evolution nabízí živou ruletu a blackjack. Menší počet stolů, ale kvalitní a spolehlivý stream.",
            "gamesMini": "Rychlé hry zahrnují Aviator, Plinko a stírací losy. Menší výběr, ale pokrývá základní kategorie.",
            "paymentsIntro": "Victoria Tip podporuje základní české platební metody s výběry do 48 hodin.",
            "paymentMethods": ["Visa", "Mastercard", "Bankovní převod", "PaySafeCard", "Apple Pay"],
            "paymentCount": 5,
            "providersIntro": "Victoria Tip spolupracuje s 10 ověřenými výrobci her a postupně přidává další.",
            "providers": ["Pragmatic Play", "Amatic", "EGT", "Evolution", "Endorphina", "Synot Games", "Novomatic", "Wazdan", "Spribe", "BGaming"],
            "providerCount": 10,
            "advantages": [
                "Česká licence MF ČR – plná regulace a bezpečnost",
                "Jednoduché a přehledné rozhraní platformy",
                "Kombinace sportovních sázek a kasina",
                "15 let zkušeností na českém trhu",
                "Profesionální česká zákaznická podpora",
                "Transparentní a srozumitelné bonusové podmínky"
            ],
            "pros": [
                "Česká licence MF ČR",
                "Jednoduché rozhraní",
                "100 Kč + 30 FS bez vkladu",
                "Sázky + kasino",
                "15 let na trhu",
                "Česká podpora"
            ],
            "cons": [
                "Menší počet her (350+)",
                "Výběry do 48 hodin",
                "Omezené platební metody",
                "Nižší bonusy oproti konkurenci"
            ],
            "supportText": "Zákaznická podpora Victoria Tip je dostupná přes live chat (denně 9-20h) a email. Tým mluví česky a je ochotný pomoci. Live chat odpovídá do 5 minut. Jednoduchá sekce FAQ na webu.",
            "faq": [
                {"q": "Je Victoria Tip legální?", "a": "Ano, Victoria Tip a.s. má platnou licenci od Ministerstva financí ČR a je plně legální pro české hráče."},
                {"q": "Jak získám registrační bonus?", "a": "Bonus 100 Kč + 30 free spinů se připíše po registraci a ověření účtu."},
                {"q": "Nabízí Victoria Tip sportovní sázky?", "a": "Ano, Victoria Tip nabízí kompletní sportovní sázky na české i mezinárodní soutěže včetně živého sázení."},
                {"q": "Jaký je minimální vklad?", "a": "Minimální vklad je 100 Kč kartou nebo bankovním převodem."},
                {"q": "Rozšiřuje Victoria Tip svou nabídku her?", "a": "Ano, Victoria Tip průběžně přidává nové poskytovatele a hry. Katalog se neustále rozrůstá."}
            ],
            "finalVerdict": "Victoria Tip je solidní volba pro hráče, kteří preferují jednoduchost a přehlednost. S českou licencí, bonusem 100 Kč + 30 FS a kombinací sázek a kasina nabízí bezproblémový herní zážitek. Menší herní katalog je kompenzován přehledným rozhraním a profesionální českou podporou."
        }
    }
]


def main():
    import sys
    sys.stdout.reconfigure(encoding="utf-8")

    # Read existing casinos.json
    print(f"Reading file: {CASINOS_FILE}")
    with open(CASINOS_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    existing_count = len(data["casinos"])
    print(f"Found {existing_count} existing casinos.")

    # Check for duplicate IDs
    existing_ids = {c["id"] for c in data["casinos"]}
    for casino in new_casinos:
        if casino["id"] in existing_ids:
            print(f"WARNING: Casino with ID '{casino['id']}' already exists - skipping.")
        else:
            data["casinos"].append(casino)
            print(f"Added: {casino['name']} (ID: {casino['id']})")

    new_count = len(data["casinos"])
    print(f"\nTotal casinos after adding: {new_count} (added {new_count - existing_count})")

    # Write back to casinos.json
    with open(CASINOS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"File saved: {CASINOS_FILE}")

    # Validate the written file
    with open(CASINOS_FILE, "r", encoding="utf-8") as f:
        validated = json.load(f)

    print(f"Validation: OK - {len(validated['casinos'])} casinos in file.")


if __name__ == "__main__":
    main()
