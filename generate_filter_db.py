#!/usr/bin/env python3
"""
Generate flat filter database from casinos.json.
Output: data/casino-filters.json — lightweight DB for filter system.
"""

import json
import os
import re
import unicodedata

BASE = os.path.dirname(os.path.abspath(__file__))


def slugify(s):
    s = unicodedata.normalize('NFD', s).encode('ascii', 'ignore').decode('ascii')
    return s.lower().replace(' ', '-').replace("'", '').replace('.', '')


def license_slug(license_str):
    l = license_str.lower()
    if 'mf' in l or 'mf čr' in l:
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


def extract_filters(casino):
    """Extract all filter-relevant flat data for one casino."""
    review = casino.get('review', {})
    bonus_lower = casino.get('bonus', '').lower()
    features_str = ' '.join(casino.get('features', [])).lower() + ' ' + bonus_lower
    bonuses_str = ' '.join(str(b) for b in review.get('bonuses', [])).lower()

    payments = [slugify(p) for p in review.get('paymentMethods', [])]
    providers = [slugify(p) for p in review.get('providers', [])]
    license_val = license_slug(review.get('license', ''))

    # Extract numeric bonus amount
    bonus_amount_str = casino.get('bonusAmount', '')
    bonus_match = re.search(r'(\d+[\s\d]*)', bonus_amount_str.replace(' ', ''))
    bonus_num = int(bonus_match.group(1).replace(' ', '')) if bonus_match else 0

    return {
        # Identity
        "slug": casino['slug'],
        "name": casino['name'],
        "logo": f"/assets/images/casinos/{casino['slug']}",  # extension auto-detected client-side
        "url": casino.get('bonusUrl', ''),
        "rating": casino.get('rating', 0),
        "reviewUrl": f"/kasina/{casino['slug']}/",

        # Numeric values
        "minDeposit": casino.get('minDeposit', 0),
        "maxWithdrawal": review.get('withdrawalRange', '').split('–')[-1].strip() if review.get('withdrawalRange') else '',
        "freeSpins": casino.get('freeSpins', 0),
        "bonusAmount": bonus_num,
        "wagering": int(re.sub(r'[^0-9]', '', casino.get('wagering', '0')) or '0'),
        "yearCreated": int(re.sub(r'[^0-9]', '', str(review.get('yearCreated', '2020'))) or '2020'),

        # Categorical filters
        "speed": speed_bucket(review.get('withdrawalSpeed', '24h')),
        "license": license_val,
        "country": "cz" if license_val == 'mf-cr' else "international",
        "language": "cs" if 'ano' in str(review.get('czechLanguage', '')).lower() else 'partial',

        # Payment & provider lists (slugified)
        "payments": payments,
        "providers": providers,
        "providerCount": review.get('providerCount', 0),
        "paymentCount": review.get('paymentCount', 0),

        # Bonus features (boolean)
        "hasNoDeposit": 'bez vkladu' in bonus_lower or 'no deposit' in bonus_lower,
        "hasFreeSpins": casino.get('freeSpins', 0) > 0,
        "hasCashback": 'cashback' in bonus_lower or 'cashback' in bonuses_str,
        "hasReload": 'reload' in bonuses_str or 'reload' in features_str,
        "hasVipBonus": 'vip' in bonuses_str,
        "hasSportBonus": 'sport' in bonuses_str,

        # Casino features (boolean)
        "hasApp": 'aplikac' in features_str or 'mobiln' in features_str,
        "hasVip": 'vip' in features_str or 'vip' in str(review.get('vipProgram', '')).lower(),
        "hasSport": 'sport' in features_str or 'sázk' in features_str,
        "hasEsport": 'esport' in features_str,
        "hasLive": 'live' in features_str or 'live' in str(review.get('gamesLive', '')).lower(),
        "hasCrypto": any(p in payments for p in ['bitcoin', 'ethereum', 'usdt', 'litecoin']),
        "hasPayPal": 'paypal' in payments,
        "hasApplePay": 'apple-pay' in payments,
        "hasInstantWithdraw": speed_bucket(review.get('withdrawalSpeed', '24h')) in ['instant', '12h'],
        "hasLowDeposit": casino.get('minDeposit', 0) <= 100,
        "hasLowWager": int(re.sub(r'[^0-9]', '', casino.get('wagering', '99')) or '99') <= 30,

        # Affiliate flag
        "isAffiliate": 'm-traff' in casino.get('bonusUrl', ''),
    }


def main():
    print('🗄️  Building flat filter database from casinos.json...\n')

    with open(os.path.join(BASE, 'data', 'casinos.json'), 'r', encoding='utf-8') as f:
        casinos = json.load(f)['casinos']

    # Build flat filter DB
    db = {
        "version": 2,
        "generated": __import__('datetime').datetime.now().isoformat(),
        "totalCasinos": len(casinos),
        "casinos": [extract_filters(c) for c in casinos],

        # Available filter values (for UI dropdowns)
        "filterOptions": {
            "speeds": ["instant", "12h", "24h", "48h"],
            "licenses": ["mf-cr", "mga", "ukgc", "curacao"],
            "minDeposits": [50, 100, 200, 500],
            "wagerings": [20, 25, 30, 35, 40, 50],
        }
    }

    # Aggregate unique payments and providers across all casinos
    all_payments = set()
    all_providers = set()
    for c in db['casinos']:
        all_payments.update(c['payments'])
        all_providers.update(c['providers'])
    db['filterOptions']['payments'] = sorted(all_payments)
    db['filterOptions']['providers'] = sorted(all_providers)
    db['filterOptions']['brands'] = [{"slug": c['slug'], "name": c['name']} for c in db['casinos']]

    out_path = os.path.join(BASE, 'data', 'casino-filters.json')
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

    print(f'✅ Wrote {out_path}')
    print(f'   - {db["totalCasinos"]} casinos')
    print(f'   - {len(db["filterOptions"]["payments"])} unique payment methods')
    print(f'   - {len(db["filterOptions"]["providers"])} unique providers')
    print(f'   - Affiliates: {sum(1 for c in db["casinos"] if c["isAffiliate"])}')


if __name__ == '__main__':
    main()
