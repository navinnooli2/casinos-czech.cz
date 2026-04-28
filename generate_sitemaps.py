#!/usr/bin/env python3
"""Generate sitemap index + split sitemaps by category (Rank Math style)."""

import json
import os
from datetime import datetime

BASE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "https://casinos-czech.cz"
TODAY = datetime.now().strftime('%Y-%m-%dT%H:%M:%S+00:00')


def write_sitemap(filename, urls):
    """Write a single sitemap file with given URLs."""
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<?xml-stylesheet type="text/xsl" href="/sitemap.xsl"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for url in urls:
        lines.append('  <url>')
        lines.append(f'    <loc>{url["loc"]}</loc>')
        lines.append(f'    <lastmod>{url.get("lastmod", TODAY)}</lastmod>')
        lines.append(f'    <changefreq>{url.get("changefreq", "monthly")}</changefreq>')
        lines.append(f'    <priority>{url.get("priority", "0.7")}</priority>')
        lines.append('  </url>')
    lines.append('</urlset>')
    path = os.path.join(BASE, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f'  ✓ {filename} ({len(urls)} URLs)')
    return filename


def write_sitemap_index(sitemaps):
    """Write the master sitemap index pointing to all sub-sitemaps."""
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<?xml-stylesheet type="text/xsl" href="/sitemap.xsl"?>',
             '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for sm in sitemaps:
        lines.append('  <sitemap>')
        lines.append(f'    <loc>{DOMAIN}/{sm}</loc>')
        lines.append(f'    <lastmod>{TODAY}</lastmod>')
        lines.append('  </sitemap>')
    lines.append('</sitemapindex>')
    path = os.path.join(BASE, 'sitemap.xml')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f'\n✅ sitemap.xml index ({len(sitemaps)} sitemaps)')


def main():
    print('🗺️  Generating sitemaps...\n')

    # Load data
    casinos = json.load(open(os.path.join(BASE, 'data', 'casinos.json'), encoding='utf-8'))['casinos']
    keywords = json.load(open(os.path.join(BASE, 'data', 'keywords.json'), encoding='utf-8'))['keywords']

    sitemaps = []

    # 1. PAGE SITEMAP (homepage + main info pages)
    page_urls = [
        {"loc": f"{DOMAIN}/", "changefreq": "weekly", "priority": "1.0"},
    ]
    sitemaps.append(write_sitemap('page-sitemap.xml', page_urls))

    # 2. CASINO SITEMAP (all casino reviews)
    casino_urls = []
    # Sort by rating descending for priority
    sorted_casinos = sorted(casinos, key=lambda c: c.get('rating', 0), reverse=True)
    for i, casino in enumerate(sorted_casinos):
        priority = "0.95" if i < 3 else "0.9" if i < 10 else "0.85"
        casino_urls.append({
            "loc": f"{DOMAIN}/kasina/{casino['slug']}/",
            "changefreq": "weekly",
            "priority": priority,
        })
    sitemaps.append(write_sitemap('casino-sitemap.xml', casino_urls))

    # 3. CATEGORY SITEMAP (top lists, rankings)
    category_slugs = ['nejlepsi-kasina-cz', 'top-10-kasin', 'online-kasino', 'nove-kasina-2026',
                      'bezpecna-kasina', 'kasino-bez-limitu', 'kasina-ceska-licence']
    category_urls = []
    for kw in keywords:
        if kw['slug'] in category_slugs:
            category_urls.append({
                "loc": f"{DOMAIN}/{kw['slug']}/",
                "changefreq": "weekly",
                "priority": "0.9",
            })
    sitemaps.append(write_sitemap('category-sitemap.xml', category_urls))

    # 4. BONUS SITEMAP (all bonus & free spin pages)
    bonus_slugs = ['nejlepsi-kasinovy-bonus', 'free-spiny-dnes', 'kasina-bez-vkladu',
                   'casino-bonusy-bez-vkladu', 'kasino-free-spiny', 'kasino-nizka-sazka',
                   'synot-tip-free-spins', 'tipsport-free-spiny']
    bonus_urls = []
    for kw in keywords:
        if kw['slug'] in bonus_slugs:
            bonus_urls.append({
                "loc": f"{DOMAIN}/{kw['slug']}/",
                "changefreq": "daily" if 'free-spiny-dnes' in kw['slug'] else "weekly",
                "priority": "0.85",
            })
    sitemaps.append(write_sitemap('bonus-sitemap.xml', bonus_urls))

    # 5. GAME SITEMAP (game-related pages)
    game_slugs = ['automaty-zdarma', 'casino-vyherni-automaty', 'live-kasino', 'jackpot-kasino',
                  'rtp-automaty', 'volatilita-automaty', 'poker-online', 'sazeni-na-sport',
                  'loterie-online', 'mobilni-kasino']
    game_urls = []
    for kw in keywords:
        if kw['slug'] in game_slugs:
            game_urls.append({
                "loc": f"{DOMAIN}/{kw['slug']}/",
                "changefreq": "weekly",
                "priority": "0.8",
            })
    sitemaps.append(write_sitemap('game-sitemap.xml', game_urls))

    # 6. LICENSE SITEMAP (legal & regulation pages)
    license_slugs = ['legalni-kasina-cz', 'kasina-ceska-licence', 'online-hazard-cz',
                     'dane-z-vyhry', 'sebeomezeni-hazard', 'kasino-pro-zacatecniky',
                     'kasino-na-penize', 'vysoke-rtp-kasino']
    license_urls = []
    for kw in keywords:
        if kw['slug'] in license_slugs:
            license_urls.append({
                "loc": f"{DOMAIN}/{kw['slug']}/",
                "changefreq": "monthly",
                "priority": "0.75",
            })
    sitemaps.append(write_sitemap('license-sitemap.xml', license_urls))

    # 7. CASINO-SPECIFIC PAGES SITEMAP (fortuna-kasino, bet365-kasino etc.)
    specific_slugs = ['fortuna-kasino', 'bet365-kasino']
    specific_urls = []
    for kw in keywords:
        if kw['slug'] in specific_slugs:
            specific_urls.append({
                "loc": f"{DOMAIN}/{kw['slug']}/",
                "changefreq": "monthly",
                "priority": "0.7",
            })
    if specific_urls:
        sitemaps.append(write_sitemap('casino-specific-sitemap.xml', specific_urls))

    # WRITE INDEX
    write_sitemap_index(sitemaps)

    print(f'\n📊 Total: {sum(1 for _ in sitemaps)} sitemap files generated')


if __name__ == '__main__':
    main()
