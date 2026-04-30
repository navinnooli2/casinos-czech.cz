# Casinos-Czech.cz – Project Memory

Site comparatif de casinos en ligne pour le marché tchèque (CZ).

## Tech Stack

- **Static site** : HTML + CSS + vanilla JS
- **Generator** : Python (`generate.py`) qui lit JSON et templates HTML, écrit fichiers à la racine
- **Hosting** : Cloudflare (DNS) + serveur upstream (déploiement auto via GitHub push)
- **Locale** : Czech (cs)

## Structure des fichiers

```
/                                # Toutes les pages keyword sont à la racine
├── index.html                   # Homepage (hardcodé)
├── data/
│   ├── casinos.json             # 24 casinos avec full review data
│   ├── keywords.json            # 35 keyword pages avec SEO content
│   └── mini_games.json          # 10 mini-jeux
├── assets/
│   ├── css/style.css            # Tout le CSS (~3800 lignes, dark theme)
│   ├── js/app.js                # Sidebar menu, filter modal, FAQ toggle
│   ├── images/
│   │   ├── logo.svg / logo.png  # Logo Casinos Czech
│   │   ├── casinos/             # Logos casino (PNG/JPG/SVG)
│   │   └── payments/            # Logos méthodes paiement (Visa, MC, Skrill...)
│   └── icons/                   # Favicons (16, 32, 64, 128, 180px)
├── kasina/                      # Pages avis casino (24 pages)
├── hry/                         # Mini-jeux
│   ├── mini-hry/                # Hub
│   └── {game-slug}/             # 10 pages individuelles
├── {keyword-slug}/              # Pages keyword à la racine (35 pages)
├── template.html                # Template page keyword
├── casino-avis-template.html    # Template page review casino
├── minigame-template.html       # Template page mini-jeu
├── minigames-hub-template.html  # Template hub mini-jeux
├── generate.py                  # Générateur principal
├── generate_sitemaps.py         # Génère sitemap index + 6 sous-sitemaps
└── sitemap.xml + sub-sitemaps   # SEO sitemaps
```

## Casinos (24 total)

### Affiliés m-traff (priorité dans tops)
URL format : `https://m-traff.net/HYcs2BV5?sub_id_1={slug}`

1. **smash** - Smash Casino (4.7) – nouveau 2026
2. **29black** - 29Black (4.6) – luxe/high-roller
3. **goldzino** - Goldzino (4.5) – prémium
4. **playjonny** - PlayJonny (4.4) – cashback 10%
5. **roulettino** - Roulettino (4.3) – spécialiste roulette

### Casinos tchèques (licence MF ČR)
synot-tip, fortuna, tipsport, chance, sazka, forbes-casino, betano, merkurxtip, betx, apollo-games, kajot-casino, luckybet, betor, doxxbet, victoria-tip

### Casinos internationaux
bet365, 888-casino, pinnacle, mostbet

## Pages catégorie principales (~3000 mots, scannable)

- `/nejlepsi-kasina-cz/` - Best casinos
- `/online-kasino/` - Online casinos
- `/nove-kasina-2026/` - New casinos 2026
- `/kasino-bez-limitu/` - No-limit casinos
- `/top-10-kasin/` - Top 10
- `/bezpecna-kasina/` - Safe casinos
- `/kasina-ceska-licence/` - Czech licensed

## Composants UI clés

### Navigation
- **Top banner** : promo banner vert (1 ligne sur mobile via `white-space: nowrap`)
- **Topbar** : 64px sticky, logo + hamburger + search
- **Sidebar menu** : slide-in depuis gauche (style tnbet), accordéons imbriqués

### Cards casino (`.top-card`)
- Layout 3 colonnes : logo+rang+rating | features+check | bonus+CTA vert
- Fond beige/crème + bordure dorée à gauche → hover vert
- Tri : affiliés m-traff en premier, puis par rating desc

### Page avis (review)
- Layout 2 colonnes : article gauche, **widget sticky droite (340px)**
- Mobile : widget en haut, article en dessous
- Widget : logo, **Webscore avec gauge SVG** (image+score), langue, bonus, CTA "Hrát"
- Sections : auteur, notre avis (4 lignes), pros/cons, bonus details, sommaire après top, sections SEO, registrace 5 steps, support 4 channels, FAQ 2 colonnes, similar casinos, verdict

### Filtre modal
- Trigger : bouton "Filtry" vert au-dessus du tableau casino
- Sections : Platba (3 selects), Bonusy (checks + select), Výhody (5 checks), Licence, Poskytovatel
- Chaque `.top-card` a `data-*` attributes utilisés par `applyFilters()` JS
- Reset : `clearFilters()` + bouton "Vymazat vše"

### Footer
- 5 colonnes liens (Kasina/Bonusy/Hry/Platby/O nás) + 1 colonne brand
- Trust badges : 18+, CLVH, AddictAide, Trustpilot, GPWA
- DMCA Protected en bas

## Sitemap (sitemap index)

6 sous-sitemaps thématiques :
- `page-sitemap.xml` (8) - homepage + rankings
- `casino-sitemap.xml` (28) - reviews + casino-specific
- `bonus-sitemap.xml` (6) - bonus pages
- `game-sitemap.xml` (10) - jeux/automaty/live
- `minigame-sitemap.xml` (11) - hub + 10 mini-jeux
- `license-sitemap.xml` (8) - légal/régulation

## Couleurs (CSS variables)

```css
--bg-dark: #0f172a        (deep navy)
--bg-elevated: #1e293b    (cards)
--green: #22c55e          (CTA, success)
--gold: #fbbf24           (accents, ratings)
--red: #ef4444            (rare, danger)
--text: #cbd5e1
--text-muted: #94a3b8
```

## Cache busting

CSS chargé avec `?v=N` (incrémenté à chaque deploy). Actuellement v=24.

## Workflow déploiement

```bash
# Local
python generate.py              # Régénère toutes les pages (35 keyword + 24 review + 10 minigame + 1 hub)
python generate_sitemaps.py     # Régénère sitemaps

# Bump cache CSS
sed -i 's/style.css?v=N/style.css?v=N+1/g' index.html template.html casino-avis-template.html minigames-hub-template.html minigame-template.html

# Deploy
git add -A && git commit -m "..." && git push
```

## Conventions

- **HTML** : pages générées sont à la racine (pas dans `/pages/`) car serveur upstream sert depuis `/`
- **Slugify** dans generate.py : lowercase, sans accents, espaces → `-`, sans `'` ni `.`
- **Pas de PLACEHOLDER dans bonusUrl** : si pas d'affilié, mettre URL casino directe sans `?aff=PLACEHOLDER`
- **Prioriser m-traff** : tri des casinos met les 5 affiliés en premier (smash, 29black, goldzino, playjonny, roulettino)

## Auteur (auteur principal des reviews)

- **Martin Novák** — Expert iGaming
- Avatar : `assets/images/author-mn.jpg` (ou initials "MN" en fallback)
- Editor : Petr Svoboda
- Fact-check : Jana Dvořáková
