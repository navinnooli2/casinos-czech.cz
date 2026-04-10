#!/usr/bin/env python3
"""
Auto-generate SEO keywords.json from existing pages + new pages
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Slugs to generate - mapped from the crawled pages
PAGES_TO_GENERATE = {
    'bezpecna-kasina': {
        'title': 'Bezpečná Kasina v ČR',
        'h1': 'Bezpečná Online Kasina v České Republice 2026',
        'description': 'Seznam bezpečných online kasin v ČR. Kteráprovozují zde kasina jsou bezpečná a licencovaná?',
        'intro': 'Bezpečnost je nejdůležitější faktor při výběru online kasina. Přinášíme kompletní přehled bezpečných a licencovaných kasin v České republice.',
    },
    'kasino-bez-limitu': {
        'title': 'Kasino Bez Limitu',
        'h1': 'Online Kasina Bez Limitů – Kde Najít Kasino Bez Maximálních Výher?',
        'description': 'Kasina bez limitu v ČR. Hrajte bez omezení maximálních výher v bezpečných online kasinech.',
        'intro': 'Hledáte kasino, kde se nemusíte bát limitů na výhry? Připravili jsme přehled kasin bez omezující maxima.',
    },
    'kasino-na-penize': {
        'title': 'Kasino na Peníze',
        'h1': 'Online Kasina na Skutečné Peníze – Bezpečná Hraní v ČR',
        'description': 'Nejlepší online kasina v ČR na skutečné peníze. Bezpečné, licencované a s nejlepšími bonusy.',
        'intro': 'Chcete hrát v online kasinu o skutečné peníze? Podívejte se na náš soupis nejlepších a nejbezpečnějších kasin.',
    },
    'live-kasino': {
        'title': 'Live Kasino',
        'h1': 'Live Casino – Hrajte se Živými Krupiery Online 2026',
        'description': 'Live kasina v České republice. Hrajte ruletu, blackjack a dalších her se skutečnými krupiery online.',
        'intro': 'Live kasino přináší autentickou atmosféru tradičních kasin přímo na váš počítač. Hrajte se živými krupiery v reálném čase.',
    },
    'mobilni-kasino': {
        'title': 'Mobilní Kasino',
        'h1': 'Mobilní Kasina – Hrajte Online na Telefonu a Tabletu 2026',
        'description': 'Nejlepší mobilní kasina v ČR. Hrajte online hry na smartphonu a tabletu bez aplikace.',
        'intro': 'Mobilní kasina vám umožňují hrát kdykoliv a kdekoliv. Přinášíme přehled nejlepších kasin optimalizovaných pro mobil.',
    },
    'vysoke-rtp-kasino': {
        'title': 'Vysoké RTP Kasino',
        'h1': 'Automaty s Vysokým RTP – Kde Najít Hry s Nejlepší Výplatností?',
        'description': 'Online automaty s vysokým RTP v ČR. Která kasina nabízejí hry s nejlepší dlouhodobou výplatností?',
        'intro': 'RTP (Return to Player) určuje dlouhodobou výplatnost automatů. Hledáte hry s vysokým RTP? Zjistěte, kde je najdete.',
    },
    'kasino-pro-zacatecniky': {
        'title': 'Kasino pro Začátečníky',
        'h1': 'Online Kasino pro Začátečníky – Návod pro Nové Hráče 2026',
        'description': 'Průvodce pro začátečníky v online kasinech. Jak si vybrat kasino, jak se zaregistrovat a začít hrát bezpečně.',
        'intro': 'Začínáte s online hazardem? Připravili jsme kompletní návod pro začátečníky, jak si vybrat kasino a naučit se hrát.',
    },
    'automaty-zdarma': {
        'title': 'Automaty Zdarma',
        'h1': 'Hrací Automaty Zdarma – Hrajte Demo Režim Bez Vkladu',
        'description': 'Hrací automaty zdarma bez vkladu. Hrajte demo verze her v online kasinech bez registrace a rizika.',
        'intro': 'Hrací automaty zdarma umožňují vyzkoušet si hry bez jakékoliv registrace a bez vkladu. Odkud je spustit?',
    },
    'jackpot-kasino': {
        'title': 'Jackpot Kasino',
        'h1': 'Online Automaty s Jackpotem – Kde Vyhrát Velké Částky?',
        'description': 'Automaty s jackpotem v českých online kasinech. Které hry nabízejí největší jackpoty?',
        'intro': 'Automaty s jackpotem nabízejí šanci na velmi vysoké výhry. Podívejte se, kde je najdete v ČR.',
    },
    'kasino-ceska-licence': {
        'title': 'Kasino Česká Licence',
        'h1': 'Kasina s Českou Licencí – Legální Online Hazard v ČR',
        'description': 'Kasina s českou licencí od Ministerstva financí. Jaké kasino má českou licenci a jsou bezpečná?',
        'intro': 'Česká licence od Ministerstva financí je zárukou bezpečnosti. Podívejte se, která kasina ji mají.',
    },
    'nove-kasina-2026': {
        'title': 'Nová Kasina 2026',
        'h1': 'Nová Online Kasina v ČR 2026 – Nejnovější Hry a Bonusy',
        'description': 'Nová online kasina v České republice 2026. Recenze nových provozovatelů, jejich bonusy a zkušenosti.',
        'intro': 'V roce 2026 přibývají nová online kasina na český trh. Přinášíme recenze a přehled nových kasin s jejich bonusy.',
    },
    'online-kasino': {
        'title': 'Online Kasino',
        'h1': 'Online Kasino v ČR – Kompletní Průvodce Hazardními Hrami 2026',
        'description': 'Online kasina v České republice. Jak vybrat kasino, jaké jsou bonusy, a jak hrát bezpečně online.',
        'intro': 'Online kasino je moderní forma tradičního hazardu. Podívejte se, co potřebujete vědět pro bezpečné a zábavné hraní.',
    },
    'top-10-kasin': {
        'title': 'Top 10 Kasin',
        'h1': 'Top 10 Online Kasin v České Republice 2026',
        'description': 'Žebříček top 10 nejlepších online kasin v ČR. Nejlépe hodnocená kasina podle hráčů a našich testů.',
        'intro': 'Která kasina jsou nejlepší v ČR? Zde najdete náš žebříček top 10 kasin seřazené podle kvality a hodnocení.',
    },
    'casino-bonusy-bez-vkladu': {
        'title': 'Casino Bonusy bez Vkladu',
        'h1': 'Casino Bonusy bez Vkladu – Kde Najít Nejlepší Nabídky 2026',
        'description': 'Casino bonusy bez vkladu v ČR. Která kasina nabízejí bonusy za pouhou registraci bez vkladu?',
        'intro': 'Bonusy bez vkladu jsou ideálním způsobem, jak vyzkoušet kasino bez rizika. Přinášíme přehled nejlepších nabídek.',
    },
    'casino-vyherni-automaty': {
        'title': 'Casino Výherní Automaty',
        'h1': 'Výherní Automaty Online – Nejlepší Hry v Kasinech ČR',
        'description': 'Výherní automaty v online kasinech. Které automaty se hrají nejčastěji a mají nejlepší RTP?',
        'intro': 'Výherní automaty jsou populární součástí online kasin. Zjistěte, které automaty patří k nejlepším a nejziskovějším.',
    },
    'sazeni-na-sport': {
        'title': 'Sázení na Sport',
        'h1': 'Online Sázení na Sport – Kurzy a Tipy na Sportovní Sázky 2026',
        'description': 'Sázení na sport online v České republice. Nejlepší sázkové kanceláře, kurzy a tipy pro sportovní sázky.',
        'intro': 'Online sázení na sport se těší obrovské oblíbenosti. Podívejte se na nejlepší sázkové kanceláře a tipy pro sázky.',
    },
    'poker-online': {
        'title': 'Poker Online',
        'h1': 'Online Poker v ČR – Herny, Turnaje a Pravidla 2026',
        'description': 'Online poker v České republice. Jak hrát poker online, kde si hrát a jaká jsou základní pravidla?',
        'intro': 'Online poker je jedním z nejpopulárnějších kasinových her. Přinášíme přehled online pokeroven a pokynů pro hráče.',
    },
    'loterie-online': {
        'title': 'Loterie Online',
        'h1': 'Online Loterie a Losy v ČR – Hrajte Losování Online 2026',
        'description': 'Online loterie v České republice. Sportka, Eurojackpot a další online losování ve vašem počítači.',
        'intro': 'Online loterie a losy vám umožňují účastnit se losování z pohodlí domova. Zjistěte, jak se hrají online.',
    },
    'rtp-automaty': {
        'title': 'RTP Automaty',
        'h1': 'RTP Automatů – Co je to RTP a Jak Vybrat Automaty s Vysokým RTP',
        'description': 'RTP (Return to Player) u automatů. Co znamená RTP a jaké automaty mají nejvyšší RTP?',
        'intro': 'RTP je klíčový faktor pro výběr automatů. Pojďte si vysvětlit, co RTP znamená a jak najít hry s vysokým RTP.',
    },
    'volatilita-automaty': {
        'title': 'Volatilita Automatů',
        'h1': 'Volatilita Automatů – Nízká vs Vysoká Volatilita Vysvětlena',
        'description': 'Volatilita u online automatů. Co je volatilita a jak ji použít pro výběr správného automatu?',
        'intro': 'Volatilita určuje, jak často padají výhry na automatu. Naučte se rozlišovat mezi nízkou a vysokou volatilitou.',
    },
    'dane-z-vyhry': {
        'title': 'Daně z Výhry',
        'h1': 'Daň z Výhry v Online Kasinu – Jaké Jsou Daňové Povinnosti v ČR?',
        'description': 'Daň z výher z online hazardu v ČR. Kolik procent daně musíte zaplatit z výher v kasinech?',
        'intro': 'Výhry z online hazardu v ČR podléhají dani. Zjistěte, jaké máte daňové povinnosti a jak se výhry zdaňují.',
    },
    'sebeomezeni-hazard': {
        'title': 'Sebeomezení Hazard',
        'h1': 'Sebeomezení v Online Kasinech – Jak Chránit Sebe Zodpovědně',
        'description': 'Sebeomezení v online kasinech. Nastavit limity na vklady, dobu hraní a ochránit se zodpovědným hraním.',
        'intro': 'Sebeomezení je důležitý nástroj pro zodpovědné hraní. Podívejte se, jaké omezující opatření jsou dostupná.',
    },
}

def generate_seo_content(slug, title):
    """Generate SEO content based on slug"""
    
    seo_sections = {
        'bezpecna-kasina': '''<h2>Jak Poznám Bezpečné Kasino?</h2>
<p>Bezpečné kasino musí mít licenci od Ministerstva financí ČR. Dále byste měli ověřit, že kasino používá SSL šifrování a splňuje přísné regulační požadavky.</p>
<h2>Znaky Bezpečného Kasina</h2>
<p>Bezpečné kasino má: ✓ Platnou českou licenci ✓ SSL zabezpečení ✓ Regulární audity ✓ Zákaznickou podporu ✓ Transparentní bonusové podmínky</p>
<h2>Jak Chránit Sebe</h2>
<p>Hraní v bezpečném kasinu je důležité, ale také si můžete chránit svou bezpečnost: Nastavit si limity vkladů, Nehrát pod vlivem alkoholu, Odhlásit se, pokud prohráváte příliš.</p>''',
        
        'kasino-bez-limitu': '''<h2>Co Znamená Kasino Bez Limitu?</h2>
<p>Kasino bez limitu znamená, že nemá stanovený maximální limit na výhry. Můžete vyhrát jakoukoliv částku bez omezení, která by vám kasino umožňovalo vybrat.</p>
<h2>Kasina Bez Limitů v ČR</h2>
<p>Mezi kasina bez limitů patří zejména Pinnacle, která se pyšní všeobecně známým principem "bez omezování limitů výher". Toto kasino je oblíbené zejména mezi hráči, kteří chtějí hrát bez omezení.</p>
<h2>Výhody a Nevýhody</h2>
<p>Výhodou je svoboda hrát bez omezení, nevýhodou mohou být vyšší minimální vklady. Kasina bez limitů jsou obvykle zaměřena na profesionální hráče a velké sázkaře.</p>''',
        
        'kasino-na-penize': '''<h2>Jak Začít Hrát na Peníze?</h2>
<p>Abyste mohli hrát na skutečné peníze, musíte: 1) Se zaregistrovat v kasinu 2) Ověřit svou identitu 3) Vložit peníze 4) Vybrat si hru a začít hrát</p>
<h2>Bezpečnost Vkladů a Výběrů</h2>
<p>Všechny legální česká kasina používají bezpečné platební metody jako bankovní převody, platební karty a e-peněženky. Vaše peníze a osobní údaje jsou chráněny šifrováním.</p>
<h2>Odpovědné Hraní</h2>
<p>Hrát na peníze je zábava, ale je důležité hrát odpovědně. Nastavte si limity a buďte opatrní na své finanční možnosti.</p>''',
        
        'live-kasino': '''<h2>Co Je Live Kasino?</h2>
<p>Live kasino je online kasino, kde hrají skuteční krupiéři v reálném čase. Můžete vidět krupiéra na webkameře a komunikovat s ním přes chat.</p>
<h2>Populární Live Hry</h2>
<p>V live kasinech si můžete zahrát: Ruleta - Blackjack - Baccarat - Poker - Game shows a další specifické hry</p>
<h2>Výhody Live Kasina</h2>
<p>Live kasino kombinuje pohodlí online hraní s autentickým zážitkem tradičního kasina. Můžete vidět všechny akce v reálném čase a věřit férovosti hry.</p>''',
        
        'mobilni-kasino': '''<h2>Mobilní Kasino vs. Desktop</h2>
<p>Mobilní kasina vám umožňují hrát na chodu. Nemusíte si instalovat aplikaci - můžete hrát přímo v mobilním prohlížeči na telefonu nebo tabletu.</p>
<h2>Výhody Mobilního Hraní</h2>
<p>Hraní v móbilu kdykoli a kdekoliv, stejné hry a bonusy jako na počítači, rychlé a bezpečné, intuitivní rozhraní optimalizované pro malé obrazovky.</p>
<h2>Kompatibilita</h2>
<p>Moderní kasina jsou optimalizována pro všechny mobilní zařízení včetně iOS (iPhone, iPad) a Android telefonů a tabletů.</p>''',
    }
    
    # Return default content if not specified
    default_content = f'''<h2>O {title}</h2>
<p>{title} je jedním z mnoha aspektů online hazardu v České republice. Tato stránka vám přinese kompletní informace o tomto tématu.</p>
<h2>Co Byste Měli Vědět</h2>
<p>Při hraní online je důležité znát pravidla, podmínky bonusů a dodržovat odpovědné hraní. Vždy si přečtěte podmínky kasina a řiďte se svojí rozpočtem.</p>
<h2>Bezpečnost a Regulace</h2>
<p>Všechna kasina v naším přehledu jsou regulována Ministerstvem financí ČR a splňují přísné podmínky pro ochranu hráčů.</p>'''
    
    return seo_sections.get(slug, default_content)

def generate_faq(slug):
    """Generate FAQ based on slug"""
    return [
        {
            "q": f"Jaké je nejlepší {slug.replace('-', ' ')}?",
            "a": f"Nejlepší {slug.replace('-', ' ')} je podle našich testů takové, které nabízí dobrý poměr bezpečnosti, bonusů a her."
        },
        {
            "q": f"Je {slug.replace('-', ' ')} v ČR legální?",
            "a": "Ano, pokud má kasino licenci od Ministerstva financí ČR, je zcela legální a regulované."
        },
        {
            "q": f"Jaké bonusy nabízí {slug.replace('-', ' ')}?",
            "a": "Kasina obvykle nabízejí registrační bonusy, free spiny, reload bonusy a věrnostní programy. Podmínky se liší."
        }
    ]

def generate_related(slug, all_slugs):
    """Generate related links"""
    related_map = {
        'bezpecna-kasina': ['legalni-kasina-cz', 'kasino-ceska-licence', 'online-kasino'],
        'kasino-bez-limitu': ['kasino-na-penize', 'top-10-kasin', 'online-kasino'],
        'live-kasino': ['online-kasino', 'kasino-pro-zacatecniky', 'mobilni-kasino'],
        'mobilni-kasino': ['online-kasino', 'kasino-pro-zacatecniky', 'automaty-zdarma'],
    }
    return related_map.get(slug, ['nejlepsi-kasina-cz', 'online-kasino', 'kasino-pro-zacatecniky'][:3])

def main():
    print('📝 Generating SEO keywords...\n')
    
    # Load existing keywords if they exist
    keywords_file = os.path.join(BASE_DIR, 'data', 'keywords.json')
    existing_keywords = []
    
    if os.path.exists(keywords_file):
        with open(keywords_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            existing_keywords = data.get('keywords', [])
    
    # Get existing slugs
    existing_slugs = {kw['slug'] for kw in existing_keywords}
    
    # Generate new keywords
    new_keywords = []
    all_slugs = list(PAGES_TO_GENERATE.keys()) + [kw['slug'] for kw in existing_keywords]
    
    for slug, config in PAGES_TO_GENERATE.items():
        if slug in existing_slugs:
            print(f'⏭️  Skipping {slug} (already exists)')
            continue
        
        print(f'✅ Generating {slug}...')
        
        keyword = {
            'slug': slug,
            'title': config['title'],
            'h1': config['h1'],
            'description': config['description'],
            'intro': config['intro'],
            'seo_content': generate_seo_content(slug, config['title']),
            'faq': generate_faq(slug),
            'related': generate_related(slug, all_slugs)
        }
        new_keywords.append(keyword)
    
    # Combine and save
    all_keywords = existing_keywords + new_keywords
    
    output = {
        'keywords': all_keywords
    }
    
    with open(keywords_file, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    
    print(f'\n✅ Generated {len(new_keywords)} new keywords!')
    print(f'📊 Total keywords: {len(all_keywords)}')
    print(f'💾 Saved to: {keywords_file}')

if __name__ == '__main__':
    main()
