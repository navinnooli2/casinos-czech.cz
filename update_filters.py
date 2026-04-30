#!/usr/bin/env python3
"""Add explicit `filters` object to each casino in casinos.json + fix placeholder URLs."""

import json
import os
import re
import unicodedata

BASE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(BASE, 'data', 'casinos.json')

# Real casino domain mapping (without affiliate placeholder)
CASINO_DOMAINS = {
    'synot-tip': 'https://www.synottip.cz',
    'fortuna': 'https://www.ifortuna.cz',
    'bet365': 'https://www.bet365.com',
    'tipsport': 'https://www.tipsport.cz',
    'pinnacle': 'https://www.pinnacle.com',
    '888-casino': 'https://www.888casino.com',
    'chance': 'https://www.chance.cz',
    'sazka': 'https://www.sazka.cz',
    'betx': 'https://www.betx.cz',
    'apollo-games': 'https://www.apollogames.cz',
    'forbes-casino': 'https://www.forbes-casino.cz',
    'merkurxtip': 'https://www.merkurxtip.cz',
    'kajot-casino': 'https://www.kajotcasino.cz',
    'betor': 'https://www.betor.cz',
    'betano': 'https://www.betano.cz',
    'luckybet': 'https://www.luckybet.cz',
    'mostbet': 'https://www.mostbet.com',
    'doxxbet': 'https://www.doxxbet.cz',
    'victoria-tip': 'https://www.victoriatip.cz',
}


def slugify(s):
    s = unicodedata.normalize('NFD', s).encode('ascii', 'ignore').decode('ascii')
    return s.lower().replace(' ', '-').replace("'", '').replace('.', '')


def license_slug(license_str):
    """Map license string to filter value."""
    l = license_str.lower()
    if 'mf' in l or 'česká' in license_str.lower() or 'mf čr' in l:
        return 'mf-cr'
    if 'mga' in l:
        return 'mga'
    if 'ukgc' in l:
        return 'ukgc'
    if 'curaç' in l or 'curac' in l:
        return 'curacao'
    return slugify(license_str)


def speed_bucket(speed):
    s = speed.lower()
    if 'instant' in s or 'okamžit' in s:
        return 'instant'
    if '12' in s and '24' not in s:
        return '12h'
    if '24' in s and '48' not in s:
        return '24h'
    if '48' in s or '72' in s:
        return '48h'
    return '24h'


def fix_url(slug, current_url):
    """Remove ?aff=PLACEHOLDER from URLs to avoid 404s."""
    if 'PLACEHOLDER' in current_url:
        return CASINO_DOMAINS.get(slug, current_url.split('?')[0])
    return current_url


def build_filters(casino):
    review = casino.get('review', {})
    bonus_lower = casino.get('bonus', '').lower()
    features_str = ' '.join(casino.get('features', [])).lower() + ' ' + bonus_lower

    payments = [slugify(p) for p in review.get('paymentMethods', [])]
    providers = [slugify(p) for p in review.get('providers', [])]

    return {
        "rating": casino.get('rating', 0),
        "minDeposit": casino.get('minDeposit', 0),
        "freeSpins": casino.get('freeSpins', 0),
        "wagering": int(re.sub(r'[^0-9]', '', casino.get('wagering', '0')) or '0'),
        "speed": speed_bucket(review.get('withdrawalSpeed', '24h')),
        "license": license_slug(review.get('license', '')),
        "payments": payments,
        "providers": providers,
        "hasNoDeposit": 'bez vkladu' in bonus_lower or 'no deposit' in bonus_lower,
        "hasFreeSpins": casino.get('freeSpins', 0) > 0,
        "hasCashback": 'cashback' in bonus_lower or any('cashback' in str(b.get('title', '')).lower() for b in review.get('bonuses', [])),
        "hasApp": 'aplikac' in features_str or 'mobiln' in features_str,
        "hasVip": 'vip' in features_str or 'vip' in str(review.get('vipProgram', '')).lower(),
        "hasSport": 'sport' in features_str or 'sázk' in features_str,
        "hasEsport": 'esport' in features_str,
        "hasCrypto": any(p in payments for p in ['bitcoin', 'ethereum', 'usdt', 'litecoin']),
    }


def main():
    with open(PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    fixed_urls = 0
    for casino in data['casinos']:
        # Fix PLACEHOLDER URLs
        old = casino.get('bonusUrl', '')
        new = fix_url(casino['slug'], old)
        if old != new:
            casino['bonusUrl'] = new
            fixed_urls += 1
            print(f"  🔧 {casino['slug']}: {old} → {new}")

        # Add explicit filters
        casino['filters'] = build_filters(casino)

    with open(PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Validate
    with open(PATH, 'r', encoding='utf-8') as f:
        json.load(f)

    print(f"\n✅ Updated {len(data['casinos'])} casinos")
    print(f"🔧 Fixed {fixed_urls} placeholder URLs")
    print(f"🔍 Added explicit filter data to all entries")


if __name__ == '__main__':
    main()
