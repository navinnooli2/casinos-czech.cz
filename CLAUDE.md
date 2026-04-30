# CLAUDE.md – Mémoire persistante du projet casinos-czech.cz

> Ce fichier sert de mémoire persistante pour Claude. Il DOIT être mis à jour à chaque modification significative du projet (nouvelle feature, refactor, ajout de dépendance, changement structure, fix bug significatif). Voir [Changelog](#changelog) en bas.

---

## 1. Vue d'ensemble du projet

- **Nom** : casinos-czech.cz
- **Objectif** : Site comparatif de casinos en ligne pour le marché tchèque (CZ). Affiliation marketing principalement via m-traff.net + opérateurs locaux. SEO-first.
- **Type d'application** : Site web statique multi-pages (HTML/CSS/JS) généré par scripts Python à partir de fichiers JSON. Pas de backend, pas de DB serveur.
- **Stack technique** :
  - **Frontend** : HTML5, CSS3 (~3500 lignes, dark theme custom), JavaScript vanilla (pas de framework)
  - **Génération** : Python 3 (scripts `generate*.py`) qui lisent JSON + templates HTML → écrivent fichiers à la racine
  - **Hosting** : Cloudflare DNS + serveur upstream (sert les fichiers statiques depuis la racine)
  - **Repo** : GitHub (`navinnooli2/casinos-czech.cz`), branche `main`
- **Locale** : Czech (cs), valeurs en Kč
- **Statut actuel** : **MVP en production**. Site live sur https://casinos-czech.cz. Itérations rapides sur UX, contenu SEO, et système d'affiliation.

---

## 2. Architecture & structure des dossiers

```
casinos-czech.cz/
├── index.html                         # Homepage (HTML statique manuel)
├── template.html                      # Template page keyword (35 pages)
├── casino-avis-template.html          # Template page review casino (24 pages)
├── minigame-template.html              # Template page mini-jeu (10 pages)
├── minigames-hub-template.html        # Template hub mini-jeux
├── menu-navigation.html               # Snippet menu (legacy, peu utilisé)
│
├── data/                              # ★ DATABASES JSON (source de vérité)
│   ├── casinos.json                   # 24 casinos avec full review data
│   ├── casino-filters.json            # ★ DB plat dédié au filtre (généré par generate_filter_db.py)
│   ├── keywords.json                  # 35 pages keyword + SEO content (~3000 mots / page principale)
│   └── mini_games.json                # 10 mini-jeux + métadonnées
│
├── generate.py                        # ★ Générateur principal (1269 lignes)
├── generate_filter_db.py              # ★ Génère casino-filters.json à partir de casinos.json
├── generate_sitemaps.py               # Génère sitemap index + 6 sous-sitemaps
├── generate_keywords.py               # Helper SEO (legacy)
├── update_filters.py                  # Script one-shot : ajoute filters explicites + fix URLs PLACEHOLDER
├── add_casinos.py                     # Script one-shot : ajoute 13 casinos initiaux
├── add_new_casinos.py                 # Script one-shot : ajoute 5 casinos affiliés (m-traff)
│
├── assets/
│   ├── css/style.css                  # Tout le CSS (~3500 lignes, dark theme cohérent)
│   ├── js/app.js                      # Sidebar menu, filter modal, FAQ, sommaire
│   ├── images/
│   │   ├── logo.svg / logo.png        # Logo Casinos Czech
│   │   ├── author-mn.jpg              # Photo auteur Martin Novák
│   │   ├── casinos/                   # Logos casino (PNG/JPG/SVG, 24 fichiers)
│   │   └── payments/                  # Logos paiement (Visa, MC, Skrill, Neteller, etc.)
│   └── icons/                         # Favicons (16, 32, 64, 128, 180px)
│
├── kasina/                            # Pages avis casino générées (24 dossiers)
│   └── {slug}/index.html
├── hry/                               # Mini-jeux générés
│   ├── mini-hry/index.html            # Hub
│   └── {slug}/index.html              # 10 pages individuelles
├── {keyword-slug}/                    # 35 pages keyword à la racine (free-spiny-dnes, top-10-kasin, etc.)
│   └── index.html
│
├── sitemap.xml                        # Sitemap index pointant vers les 6 sous-sitemaps
├── sitemap.xsl                        # XSL pour affichage humain des sitemaps
├── page-sitemap.xml                   # 8 URLs (homepage + rankings)
├── casino-sitemap.xml                 # 28 URLs (24 reviews + 4 specifics)
├── bonus-sitemap.xml                  # 6 URLs (pages bonus)
├── game-sitemap.xml                   # 10 URLs (jeux/automaty/live)
├── minigame-sitemap.xml               # 11 URLs (hub + 10 mini-jeux)
├── license-sitemap.xml                # 8 URLs (légal/régulation)
├── robots.txt
│
├── PROJECT.md                         # Doc humaine du projet (legacy, partiellement remplacé par CLAUDE.md)
├── CLAUDE.md                          # ★ CE FICHIER (mémoire pour Claude)
├── .gitignore                         # Ignore /casinos-czech.cz/ subdir
└── .gitattributes
```

### Points d'entrée du code

- **`python generate.py`** → Régénère TOUTES les pages (35 keyword + 24 review + 10 mini-jeu + 1 hub) à partir de JSON + templates
- **`python generate_filter_db.py`** → Régénère `data/casino-filters.json` depuis `casinos.json`
- **`python generate_sitemaps.py`** → Régénère sitemap index + sous-sitemaps
- **`index.html`** est édité manuellement (homepage)

### Conventions de nommage

- **Slugify** : lowercase, sans accents (NFD normalize), espaces → `-`, sans apostrophes ni points (`Play'n GO` → `playn-go`)
- **Fichiers** : kebab-case (`casino-avis-template.html`)
- **Variables Python** : snake_case
- **Classes CSS** : kebab-case BEM-like (`.top-card-bonus`, `.filter-modal-header`)
- **Cache busting** : `style.css?v=N` (incrémenté à chaque déploiement)

---

## 3. Fonctionnalités existantes

### ✅ Pages générées (terminé)

| Type | Nb | Source | Template | Output |
|------|----|--------|----------|--------|
| **Pages keyword** | 35 | `data/keywords.json` | `template.html` | `/{slug}/index.html` |
| **Pages review casino** | 24 | `data/casinos.json` | `casino-avis-template.html` | `/kasina/{slug}/index.html` |
| **Pages mini-jeu** | 10 | `data/mini_games.json` | `minigame-template.html` | `/hry/{slug}/index.html` |
| **Hub mini-jeux** | 1 | `data/mini_games.json` | `minigames-hub-template.html` | `/hry/mini-hry/index.html` |
| **Homepage** | 1 | hardcodé | — | `/index.html` |

### ✅ Système d'affiliation (terminé)

- **5 casinos affiliés m-traff** : smash, 29black, goldzino, playjonny, roulettino
- URL format : `https://m-traff.net/HYcs2BV5?sub_id_1={slug}` (sub_id permet tracking par casino)
- **Casinos affiliés affichés en premier** dans tous les tops (`AFFILIATE_PRIORITY` dans `generate.py`)
- Casinos non-affiliés : URL directe vers leur site (sans `?aff=PLACEHOLDER` qui causait des 404)

### ✅ Système de filtre (en cours d'évolution)

- **Filter modal** ouvert via bouton vert "Filtry" au-dessus de chaque tableau casino
- Filtres disponibles : platba, rychlost výběru, min vklad, free spiny, bez vkladu, cashback, app, VIP, sport, eSport, krypto, licence, poskytovatel her, **značka kasina**
- **Database** : `data/casino-filters.json` (généré depuis casinos.json via `generate_filter_db.py`)
- **Data-attributes** sur chaque `.top-card` : `data-brand`, `data-rating`, `data-payments`, `data-providers`, `data-license`, `data-no-deposit`, etc.
- **JS** dans `app.js` : `applyFilters()`, `clearFilters()`, `getActiveFilters()`
- Compteur badge sur le bouton "Filtry (N)" quand des filtres sont actifs
- Message "Žádné kasino nesplňuje kritéria" si aucun match

### ✅ UI components (terminé)

- **Top banner** : promo verte 1 ligne (sticky, white-space:nowrap mobile)
- **Topbar 64px** sticky avec hamburger + logo + search
- **Sidebar menu slide-in** style tnbet (accordéons imbriqués Kasina > Bonusy > Výhody > Typ her)
- **Top casino cards** : layout 3 cols (logo+rang+rating | features | bonus+CTA vert), fond beige/crème, bordure dorée → hover vert
- **Page review 2-col** : article gauche, **widget non-sticky** droite (340px). Mobile : widget en haut.
- **Widget review** (light beige + dark navy mixed) : logo, **Webscore avec gauge SVG semi-circulaire**, langue, bonus, CTA vert "Hrát"
- **Auteur block** : photo Martin Novák + Editor + Fact-checker
- **Notre avis box** : 1 paragraphe synthétique 4 lignes + CTA
- **Pros/Cons inline** 2 colonnes
- **Bonus details** : table dark navy avec lignes (Hodnota / Detail / Wager) + bouton vert
- **Sommaire dépliable** (TOC) après le top casinos
- **Sections SEO scannables** : H2 avec border-left vert, listes stylées (✓ verts), tableaux comparatifs, info-box / warning-box / highlight-box
- **Page mini-jeu** : grande bannière CTA d'affiliation (replace iframe demo) + sidebar info (RTP, volatilité, sázky, max výhra) + sections détaillées
- **Footer multi-colonnes** (5 cols + brand) + trust badges (18+, CLVH, AddictAide, Trustpilot, GPWA) + DMCA Protected

### ✅ SEO

- **Sitemap index** + 6 sous-sitemaps catégorisés (style Rank Math)
- **Meta tags** Open Graph + canonical + robots
- **Pages catégorie principales** : ~3000 mots scannables (12-30 H2, 6-11 tables, 16-26 listes par page)
- **Schema.org** WebSite (homepage)

### 🟡 En cours / améliorations possibles

- **Filtre client-side** : peut être amélioré pour fetch dynamiquement `casino-filters.json` au lieu d'utiliser uniquement les data-attributes HTML
- **Mini-game iframes** : actuellement remplacés par bannière CTA d'affiliation (les iframes demo cassent souvent en CORS). À considérer pour réactivation si on trouve des demos compatibles.
- **Photo auteur** : currently using a placeholder from i.pravatar.cc. À remplacer par une vraie photo si disponible.

---

## 4. Dépendances clés & services externes

### Python (scripts)

- **Standard library uniquement** : `json`, `os`, `re`, `unicodedata`, `datetime`. Pas de pip install.

### Frontend

- **Aucune librairie externe** (pas de jQuery, React, etc.)
- **Pas de build step** (CSS et JS écrits à la main)
- **Pas de CDN externe** (tout self-hosted)

### Services externes

- **Cloudflare** : DNS + proxy + CDN front-end (cache: max-age 14400 sur CSS, 0 sur HTML)
- **GitHub** : versionning + déploiement auto (le serveur upstream pull depuis main)
- **m-traff.net** : programme d'affiliation principal (5 casinos via `?sub_id_1={slug}`)
- **Google favicon CDN** : utilisé une fois pour récupérer logos casino (`https://www.google.com/s2/favicons?sz=256&domain=...`) — résultats sauvés localement

### Secrets

- Aucun secret applicatif (pas d'API key, pas de variable d'environnement)
- Le seul "secret" est l'identifiant `HYcs2BV5` dans les URLs m-traff (token d'affiliation, public)

---

## 5. Commandes utiles

```bash
# Régénérer toutes les pages (workflow standard)
PYTHONIOENCODING=utf-8 python generate.py

# Régénérer la database de filtres après modif casinos.json
PYTHONIOENCODING=utf-8 python generate_filter_db.py

# Régénérer les sitemaps
PYTHONIOENCODING=utf-8 python generate_sitemaps.py

# Bump cache CSS (incrémenter ?v=N dans les 5 fichiers HTML qui référencent style.css)
sed -i 's/style.css?v=24/style.css?v=25/g' index.html template.html casino-avis-template.html minigames-hub-template.html minigame-template.html

# Workflow déploiement complet
python generate_filter_db.py && python generate.py && python generate_sitemaps.py
git add -A
git commit -m "Description"
git push

# Tests rapides
curl -s "https://casinos-czech.cz/?cb=$(date +%s)" | grep -oE 'style.css\?v=[0-9]+'    # Vérifier version CSS live
curl -sI "https://casinos-czech.cz/kasina/synot-tip/" | head -5                       # Vérifier headers
```

### Pas de variables d'environnement

Le projet n'utilise pas de `.env`. Tout est hardcodé dans les scripts (DOMAIN, AFFILIATE_PRIORITY, etc.).

---

## 6. Conventions de code & patterns

### Python

- **Modular builders** : chaque type de HTML est généré par sa propre fonction (`build_top_card`, `build_payment_html`, `build_bonus_pack_html`, etc.)
- **Templates avec placeholders** `{{variable}}` remplacés par `.replace()` (pas de Jinja, pas de Mako)
- **Pas de classes** : tout en fonctions
- **Slugify** centralisé dans `generate.py` et `generate_filter_db.py` (même logique)
- **AFFILIATE_PRIORITY** : tableau ordonné définissant l'ordre des casinos affiliés en haut

### CSS

- **CSS variables (`:root`)** pour la palette : `--bg-dark`, `--bg-elevated`, `--green`, `--gold`, `--red`, `--text`, `--text-muted`, etc.
- **Mobile-first** avec `@media (max-width: 1024px)` et `@media (max-width: 768px)` et `@media (max-width: 600px)`
- **BEM-like naming** : `.review-aside`, `.aside-card`, `.aside-rating-block`
- **!important** utilisé uniquement quand nécessaire (boutons CTA pour battre les liens hérités)
- **Pas de préprocesseur** (Sass/Less)

### HTML

- **Templates** avec placeholders `{{xxx}}` simples
- **Inline event handlers** pour interactions simples (`onclick="openFilterModal()"`)
- **data-attributes** abondamment utilisés pour le filtrage (`data-brand`, `data-rating`, etc.)

### JS

- **Vanilla, ES5+ compatible** (pas de transpilation)
- **Functions globales** pour les callbacks HTML inline (`window.openFilterModal`, `window.applyFilters`)
- **DOMContentLoaded** pour init
- **Pas de framework, pas de bundler**

### Cache busting

- À chaque modif CSS, incrémenter `style.css?v=N` dans tous les fichiers HTML qui le référencent
- Actuellement à `v=25`

---

## 7. Points d'attention / pièges

### ⚠️ Routing serveur

- Le serveur upstream sert les fichiers depuis la **racine** du repo (`/X/index.html` → `https://casinos-czech.cz/X/`)
- Les pages keyword sont donc générées **directement à la racine**, PAS dans un sous-dossier `/pages/`
- **Si tu changes ce comportement, tu casses tout le site** (404 sur toutes les pages)
- Voir `pages_dir = BASE_DIR` dans `generate.py:1043`

### ⚠️ Cache Cloudflare

- HTML : `Cache-Control: max-age=0, must-revalidate` (toujours frais)
- CSS : `max-age=14400` (4h) → **doit toujours bumper `?v=N`** pour forcer rechargement
- Browser cache : Ctrl+Shift+R nécessaire pour voir changements CSS sans bump version

### ⚠️ Affiliation

- Les 5 casinos m-traff DOIVENT garder leur URL `https://m-traff.net/HYcs2BV5?sub_id_1={slug}`
- Les autres casinos NE DOIVENT PAS avoir `?aff=PLACEHOLDER` (404)
- Vérifier après toute modif via : `grep -r "PLACEHOLDER" data/casinos.json`

### ⚠️ Iframes mini-jeux

- Les démos officielles (Spribe, BGaming, etc.) bloquent souvent l'embedding cross-origin (CORS, X-Frame-Options)
- Solution actuelle : remplacer iframe par **bannière CTA d'affiliation**
- Si tu veux réactiver iframes, prévoir overlay click-to-load + fallback

### ⚠️ Slugify / providers / filtre

- **Bug historique** : `Play'n GO` slugifié en `playn-go`, mais le filtre avait l'option `playngo` → mismatch
- Toujours vérifier que les valeurs des `<option value="">` du filter modal correspondent EXACTEMENT aux slugs générés par `slugify()`
- Le filter modal est défini dans 2 endroits : `generate.py` (FILTER_MODAL_HTML) ET `index.html` (statique). Les garder synchronisés.

### ⚠️ Encoding Windows

- Les scripts Python ont besoin de `PYTHONIOENCODING=utf-8` pour print emojis sans crash sous Windows cp1252
- Toujours préfixer : `PYTHONIOENCODING=utf-8 python generate.py`

### ⚠️ Footer / Banner / TOC

- Le **topbar** est sticky, mais le **widget review** ne l'est PAS (user a explicitement demandé qu'il défile avec la page)
- La **bannière du haut** doit tenir sur 1 ligne sur mobile (`white-space: nowrap` + `text-overflow: ellipsis`)
- Le **TOC (sommaire)** doit être APRÈS le top des casinos, pas avant

---

## 8. TODO / Roadmap court terme

### Bugs à surveiller

- [ ] Vérifier que tous les casinos ont bien leur logo (extension correcte) après modifications de `casinos.json`
- [ ] Tester le filtre par marque (`data-brand`) sur toutes les pages keyword
- [ ] Vérifier l'URL de chaque casino régulièrement (les casinos changent leurs domaines)

### Features prioritaires

- [ ] **Filtre client-side avancé** : faire fetch `data/casino-filters.json` depuis le frontend pour des filtres plus sophistiqués (multi-select, range slider pour rating/min deposit)
- [ ] **Page de comparaison** : permettre à l'utilisateur de comparer 2-3 casinos côte à côte
- [ ] **Recherche fonctionnelle** : la search bar du topbar n'a pas encore de logique JS
- [ ] **Mode clair (light theme)** : test page existait, à réintroduire si besoin
- [ ] **Plus de mini-jeux** : ajouter Crash Royale, Goal, Hot Air Balloon, Penalty Shoot-out

### Idées long terme

- [ ] Multi-langue (Slovaque, Polonais)
- [ ] Système de reviews utilisateurs (étoiles + commentaires) — nécessiterait backend
- [ ] Newsletter d'opt-in pour bonus exclusifs
- [ ] Page "Auteurs" avec bios

---

## Changelog

> Format : `YYYY-MM-DD — Type — Description (commit hash si applicable)`

- **2026-04-30** — `feat` — Page bio auteur Martin Novák (`/autori/martin-novak/`) + lien depuis review pages
- **2026-04-30** — `feat` — Plan du site catégorisé (`/plan-stranek/`) + lien dans footer
- **2026-04-30** — `feat` — Sticky sub-nav horizontale tabs sur pages avis (Úvod / Spolehlivost / Bonusy / Hry / Platby / Poskytovatelé / Registrace / Podpora / FAQ / Verdikt) avec scroll spy
- **2026-04-30** — `feat` — Top casino cards expandables : bouton "Zobrazit detaily" qui ouvre panel avec advantages + stats (rating, max výběr, wagering, počet her, rychlost, licence) + description + lien recenze
- **2026-04-30** — `feat` — Création de `data/casino-filters.json` (database flat dédiée au filtre, 24 casinos, 21 paiements, 67 providers). Nouveau script `generate_filter_db.py`. (commit en cours)
- **2026-04-30** — `feat` — Création de **CLAUDE.md** comme mémoire persistante du projet
- **2026-04-30** — `fix` — 19 URLs `?aff=PLACEHOLDER` remplacées par URL directe casino (anti-404). Script `update_filters.py`
- **2026-04-30** — `feat` — Ajout filtre par **brand** (data-brand sur chaque card + sélecteur dans modal)
- **2026-04-30** — `feat` — Ajout photo auteur Martin Novák (`assets/images/author-mn.jpg`) avec CSS object-fit
- **2026-04-29** — `feat` — Section mini-jeux : 10 pages individuelles (Aviator, Chicken Road, Tower Rush, Plinko, Mines, Spaceman, JetX, Dice, Limbo, Hi-Lo) + hub `/hry/mini-hry/`. Iframe demo remplacée par bannière CTA affiliation
- **2026-04-29** — `feat` — Sitemap dédié `minigame-sitemap.xml` ajouté à l'index
- **2026-04-29** — `feat` — Tri des casinos affiliés (m-traff) en premier dans tous les tops
- **2026-04-29** — `refactor` — Réécriture pages catégorie en mode scannable (tableaux + listes + boxes + pros/cons inline) — ~2500-2650 mots, 23-30 H2 par page
- **2026-04-29** — `feat` — Bannière top : 1 ligne sur mobile (white-space: nowrap)
- **2026-04-29** — `refactor` — Widget review simplifié : suppression bouton VÝBĚR + SHRNUTÍ, remplacement bloc rating par Webscore gauge, CTA "Hrát" simple
- **2026-04-28** — `feat` — Filter modal fonctionnel avec data-attributes par casino, JS apply/clear filters
- **2026-04-28** — `feat` — Footer multi-colonnes (5 cols + brand) + trust badges (18+, CLVH, AddictAide, Trustpilot, GPWA) + DMCA
- **2026-04-28** — `feat` — Page review redesign : layout 2-col, widget gauche/droite swap, mobile widget en haut
- **2026-04-28** — `fix` — Routing : pages keyword générées à la racine (pas dans `/pages/`) car serveur upstream sert depuis `/`
- **2026-04-28** — `feat` — Sidebar menu style tnbet (slide-in + accordéons imbriqués)
- **2026-04-28** — `feat` — Mega menu navigation, breadcrumb, author block, sommaire (TOC) dépliable
- **2026-04-28** — `feat` — Récupération des vrais logos casino via Google favicon CDN (10 casinos)
- **2026-04-28** — `feat` — 5 nouveaux casinos affiliés m-traff (smash, 29black, goldzino, playjonny, roulettino)
- **2026-04-28** — `feat` — Sitemap index + 5 sous-sitemaps catégorisés (style Rank Math)
- **2026-04-28** — `feat` — Pages avis casino (24 reviews complètes ~2000+ mots) avec carrousels jeux/paiements/providers
- **2026-04-28** — `feat` — 13 casinos initiaux ajoutés (synot-tip, fortuna, tipsport, chance, sazka, etc.)
- **2026-04-28** — `init` — Création initiale du projet (générateur Python + 6 casinos de base)
