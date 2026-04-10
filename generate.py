#!/usr/bin/env python3
"""
Casino Arena — Programmatic Page Generator
Reads keywords.json + casinos.json + template.html → generates pages/
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_json(filename):
    with open(os.path.join(BASE_DIR, 'data', filename), 'r', encoding='utf-8') as f:
        return json.load(f)

def load_template():
    with open(os.path.join(BASE_DIR, 'template.html'), 'r', encoding='utf-8') as f:
        return f.read()

def stars_html(rating):
    full = int(rating)
    half = 1 if rating - full >= 0.3 else 0
    return '★' * full + ('½' if half else '') + '☆' * (5 - full - half)

def build_casino_card(casino, rank):
    fs_badge = ''
    if casino['freeSpins'] > 0:
        fs_badge = f'<span class="badge badge-green">{casino["freeSpins"]} FS</span>'
    
    return f'''<div class="casino-card">
    <div class="casino-rank">#{rank}</div>
    <div class="casino-logo">{casino["name"][:3].upper()}</div>
    <div class="casino-info">
        <div class="casino-name">{casino["name"]}</div>
        <div class="casino-bonus">{casino["bonus"]}</div>
    </div>
    <div class="casino-meta">
        <div class="casino-rating">
            <span class="stars">{stars_html(casino["rating"])}</span>
            <span class="rating-num">{casino["rating"]}/5</span>
        </div>
        {fs_badge}
    </div>
    <div class="casino-cta">
        <a href="{casino["bonusUrl"]}" class="btn" target="_blank" rel="nofollow noopener">Hrát nyní →</a>
    </div>
</div>'''

def build_casino_cards(casinos):
    cards = []
    for i, casino in enumerate(casinos, 1):
        cards.append(build_casino_card(casino, i))
    return '\n'.join(cards)

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

def generate_page(keyword, casinos, template, all_keywords):
    casino_cards = build_casino_cards(casinos)
    faq_html = build_faq_html(keyword.get('faq', []))
    related_html = build_related_html(keyword.get('related', []), all_keywords)
    
    html = template
    html = html.replace('{{slug}}', keyword['slug'])
    html = html.replace('{{title}}', keyword['title'])
    html = html.replace('{{h1}}', keyword['h1'])
    html = html.replace('{{description}}', keyword['description'])
    html = html.replace('{{intro}}', keyword['intro'])
    html = html.replace('{{casino_cards}}', casino_cards)
    html = html.replace('{{seo_content}}', keyword['seo_content'])
    html = html.replace('{{faq_html}}', faq_html)
    html = html.replace('{{related_html}}', related_html)
    
    return html

def main():
    print('🎰 Casino Arena — Generating pages...\n')
    
    casinos_data = load_json('casinos.json')
    keywords_data = load_json('keywords.json')
    template = load_template()
    
    casinos = casinos_data['casinos']
    keywords = keywords_data['keywords']
    
    pages_dir = os.path.join(BASE_DIR, 'pages')
    os.makedirs(pages_dir, exist_ok=True)
    
    count = 0
    for keyword in keywords:
        slug = keyword['slug']
        page_dir = os.path.join(pages_dir, slug)
        os.makedirs(page_dir, exist_ok=True)
        
        html = generate_page(keyword, casinos, template, keywords)
        
        output_path = os.path.join(page_dir, 'index.html')
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)
        
        count += 1
        print(f'  ✓ /{slug}/index.html')
    
    print(f'\n✅ Generated {count} pages in pages/')
    print(f'📊 Casinos: {len(casinos)}')
    print(f'🔑 Keywords: {len(keywords)}')

if __name__ == '__main__':
    main()
