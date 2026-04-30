#!/usr/bin/env python3
"""Inject the dynamic casino tops HTML into index.html, replacing the hardcoded section."""

import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE)

# Import the generator's functions and data
import json
from generate import build_casino_tops

# Load casinos
with open(os.path.join(BASE, 'data', 'casinos.json'), 'r', encoding='utf-8') as f:
    casinos = json.load(f)['casinos']

# Generate the dynamic tops HTML
tops_html = build_casino_tops(casinos, slug='nejlepsi-kasina-cz')

# Read index.html
index_path = os.path.join(BASE, 'index.html')
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Find the section to replace: from "<h2 class=\"section-title\">Top Kasina v ČR</h2>"
# all the way through the closing </div> of the section-content + filter modal end.
# We'll match from <h2>Top Kasina v ČR</h2> to the closing </div></section> right before the seo-content section.

# Simpler approach: find the start and end markers
start_marker = '<h2 class="section-title">Top Kasina v ČR</h2>'
# The end is the </div> that closes "section-content" / </section> just before the seo-content
# Let's find where the next <section class="seo-content"> or <section class="section"> begins

start_idx = html.find(start_marker)
if start_idx == -1:
    print('❌ Could not find start marker in index.html')
    sys.exit(1)

# Find the closing </section> after the casino-tops + filter modal
# The structure currently is:
#   <h2>Top Kasina v ČR</h2>
#   ... casino cards (hardcoded) ...
#   </div>  (closes casino-tops or section-content)
#   </div>  (closes container)
# </section>  (closes the section)
# Then <!-- FILTER MODAL --> exists separately or <section class="seo-content">

# We'll find the end of the section that contains the cards
# The next "<section" tag after start_idx
next_section = html.find('<section', start_idx + len(start_marker))
if next_section == -1:
    print('❌ Could not find next section')
    sys.exit(1)

# Walk back to find the closing </section> before the next section
# Find the </section> that comes BEFORE the next <section
end_idx = html.rfind('</section>', start_idx, next_section)
if end_idx == -1:
    print('❌ Could not find closing section')
    sys.exit(1)
end_idx += len('</section>')

# We also need to remove the FILTER MODAL block (it will be re-added by build_casino_tops)
# Search for an existing FILTER MODAL block
filter_modal_start = html.find('<!-- FILTER MODAL -->')
filter_modal_end = -1
if filter_modal_start != -1 and filter_modal_start > end_idx:
    # Find end of filter modal: closing </div> after the modal
    modal_close = html.find('<div class="filter-modal" id="filterModal">', filter_modal_start)
    if modal_close != -1:
        # Find the matching closing </div> by counting depth — simpler: find next "<footer" or "<section"
        next_after_modal = html.find('<footer', filter_modal_start)
        if next_after_modal == -1:
            next_after_modal = html.find('<section', filter_modal_start + 50)
        if next_after_modal != -1:
            # Find the </div> right before next_after_modal
            search_end = html.rfind('</div>', filter_modal_start, next_after_modal)
            if search_end != -1:
                filter_modal_end = search_end + len('</div>')

# Build the replacement: new tops HTML wrapped in the section structure
new_section = f'''<h2 class="section-title">Top kasin v ČR – Nejlepší online kasina 2026</h2>
        {tops_html}'''

# Replace start_marker → end_idx with new_section
new_html = html[:start_idx] + new_section + html[end_idx:]

# If there was a separate filter modal block AFTER the section, remove it (build_casino_tops adds it)
if filter_modal_start != -1:
    # Recompute its position in new_html
    filter_modal_start_new = new_html.find('<!-- FILTER MODAL -->')
    if filter_modal_start_new != -1:
        # Find end
        next_after = new_html.find('<footer', filter_modal_start_new)
        if next_after == -1:
            next_after = new_html.find('<section', filter_modal_start_new + 50)
        if next_after != -1:
            end_modal = new_html.rfind('</div>', filter_modal_start_new, next_after)
            if end_modal != -1:
                end_modal += len('</div>')
                # Remove the modal block (since the new tops_html includes its own modal)
                new_html = new_html[:filter_modal_start_new] + new_html[end_modal:]

# Write back
with open(index_path, 'w', encoding='utf-8') as f:
    f.write(new_html)

print(f'✅ Updated index.html with dynamic casino tops ({len(casinos)} casinos)')
print(f'   - Replaced section from char {start_idx} to {end_idx}')
print(f'   - Old size: {len(html)} chars, new size: {len(new_html)} chars')
