#!/usr/bin/env python3
"""Replace m-traff URLs of the 12 new casinos with direct casino URLs (no affiliate)."""

import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(BASE, 'data', 'casinos.json')

# Direct URL for each new casino (NO affiliate placeholder)
DIRECT_URLS = {
    'betista': 'https://www.betista.com',
    'needforslots': 'https://www.needforslots.com',
    'billionairespin': 'https://www.billionairespin.com',
    'bdmbet': 'https://www.bdmbet.com',
    'mafia-casino': 'https://www.mafiacasino.com',
    'betify': 'https://www.betify.com',
    'spinsy': 'https://www.spinsy.com',
    'cashed': 'https://www.cashed.com',
    'spinbara': 'https://www.spinbara.com',
    'betriot': 'https://www.betriot.com',
    'casinozer': 'https://www.casinozer.com',
    'rabona-casino': 'https://www.rabona.com',
}


def main():
    with open(PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    fixed = 0
    for casino in data['casinos']:
        slug = casino.get('slug', '')
        if slug in DIRECT_URLS:
            old = casino.get('bonusUrl', '')
            new = DIRECT_URLS[slug]
            if old != new:
                casino['bonusUrl'] = new
                # Also update filters.url if present
                if 'filters' in casino:
                    casino['filters']['url'] = new
                    casino['filters']['isAffiliate'] = False
                fixed += 1
                print(f'  ✓ {slug}: {old} → {new}')

    with open(PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f'\n✅ Fixed {fixed} casino URLs (m-traff → direct)')


if __name__ == '__main__':
    main()
