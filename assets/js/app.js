// Filter modal global functions
function openFilterModal() {
  var ov = document.getElementById('filterOverlay');
  var md = document.getElementById('filterModal');
  if (ov) ov.classList.add('open');
  if (md) md.classList.add('open');
  document.body.style.overflow = 'hidden';
}
function closeFilterModal() {
  var ov = document.getElementById('filterOverlay');
  var md = document.getElementById('filterModal');
  if (ov) ov.classList.remove('open');
  if (md) md.classList.remove('open');
  document.body.style.overflow = '';
}

function getActiveFilters() {
  var filters = {};
  document.querySelectorAll('[data-filter]').forEach(function(el) {
    var key = el.dataset.filter;
    if (el.type === 'checkbox') {
      if (el.checked) filters[key] = true;
    } else if (el.tagName === 'SELECT') {
      if (el.value) filters[key] = el.value;
    }
  });
  return filters;
}

function applyFilters() {
  var filters = getActiveFilters();
  var cards = document.querySelectorAll('.top-card');
  var visibleCount = 0;

  cards.forEach(function(card) {
    var d = card.dataset;
    var show = true;

    if (filters.payment && (d.payments || '').indexOf(filters.payment) === -1) show = false;
    if (filters.speed && d.speed !== filters.speed) show = false;
    if (filters['min-deposit'] && parseInt(d.minDeposit) > parseInt(filters['min-deposit'])) show = false;
    if (filters['free-spins'] && parseInt(d.freeSpins) === 0) show = false;
    if (filters['no-deposit'] && d.noDeposit !== 'true') show = false;
    if (filters.cashback && d.cashback !== 'true') show = false;
    if (filters['fs-count'] && parseInt(d.freeSpins) < parseInt(filters['fs-count'])) show = false;
    if (filters.app && d.app !== 'true') show = false;
    if (filters.vip && d.vip !== 'true') show = false;
    if (filters.sport && d.sport !== 'true') show = false;
    if (filters.esport && d.esport !== 'true') show = false;
    if (filters.crypto && d.crypto !== 'true') show = false;
    if (filters.license && (d.license || '').indexOf(filters.license) === -1) show = false;
    if (filters.provider && (d.providers || '').indexOf(filters.provider) === -1) show = false;
    if (filters.brand && d.brand !== filters.brand) show = false;

    card.style.display = show ? '' : 'none';
    if (show) visibleCount++;
  });

  // Update filter button count
  var activeCount = Object.keys(filters).length;
  var btn = document.querySelector('.filter-btn');
  if (btn) {
    var existing = btn.querySelector('.filter-count');
    if (existing) existing.remove();
    if (activeCount > 0) {
      var span = document.createElement('span');
      span.className = 'filter-count';
      span.textContent = activeCount;
      btn.appendChild(span);
    }
  }

  // Show "no results" message if needed
  var topsContainer = document.querySelector('.casino-tops');
  if (topsContainer) {
    var existingMsg = topsContainer.querySelector('.no-filter-results');
    if (visibleCount === 0) {
      if (!existingMsg) {
        var msg = document.createElement('div');
        msg.className = 'no-filter-results';
        msg.style.cssText = 'padding:30px;text-align:center;color:#94a3b8;background:rgba(255,255,255,0.02);border:1px dashed rgba(255,255,255,0.1);border-radius:8px;';
        msg.innerHTML = 'Žádné kasino nesplňuje vybraná kritéria. <button onclick="clearFilters()" style="background:none;border:none;color:#22c55e;cursor:pointer;text-decoration:underline;font-size:inherit;">Vymazat filtry</button>';
        topsContainer.appendChild(msg);
      }
    } else if (existingMsg) {
      existingMsg.remove();
    }
  }

  closeFilterModal();
}

function clearFilters() {
  document.querySelectorAll('[data-filter]').forEach(function(el) {
    if (el.type === 'checkbox') el.checked = false;
    else if (el.tagName === 'SELECT') el.value = '';
  });
  document.querySelectorAll('.top-card').forEach(function(card) {
    card.style.display = '';
  });
  var btn = document.querySelector('.filter-btn');
  if (btn) {
    var existing = btn.querySelector('.filter-count');
    if (existing) existing.remove();
  }
  var topsContainer = document.querySelector('.casino-tops');
  if (topsContainer) {
    var existingMsg = topsContainer.querySelector('.no-filter-results');
    if (existingMsg) existingMsg.remove();
  }
}

window.openFilterModal = openFilterModal;
window.closeFilterModal = closeFilterModal;
window.applyFilters = applyFilters;
window.clearFilters = clearFilters;

// Sort dropdown
function toggleSort(e) {
  if (e) e.stopPropagation();
  var dropdown = document.querySelector('.sort-dropdown');
  if (dropdown) dropdown.classList.toggle('open');
}
window.toggleSort = toggleSort;

// Speed bucket → numeric weight (lower = faster)
var SPEED_WEIGHTS = { 'instant': 0, '12h': 1, '24h': 2, '48h': 3, '72h': 4 };

function sortCasinos(sortKey) {
  var tops = document.querySelector('.casino-tops');
  if (!tops) return;
  var cards = Array.from(tops.querySelectorAll('.top-card'));

  var sorted = cards.slice().sort(function(a, b) {
    var d1 = a.dataset, d2 = b.dataset;
    if (sortKey === 'rating') return parseFloat(d2.rating) - parseFloat(d1.rating);
    if (sortKey === 'bonus') return parseInt(d2.bonusNum || 0) - parseInt(d1.bonusNum || 0);
    if (sortKey === 'fs') return parseInt(d2.freeSpins || 0) - parseInt(d1.freeSpins || 0);
    if (sortKey === 'deposit') return parseInt(d1.minDeposit || 999) - parseInt(d2.minDeposit || 999);
    if (sortKey === 'speed') return (SPEED_WEIGHTS[d1.speed] || 99) - (SPEED_WEIGHTS[d2.speed] || 99);
    if (sortKey === 'wagering') return parseInt(d1.wagering || 99) - parseInt(d2.wagering || 99);
    return 0; // relevance: keep original order
  });

  // Reassign data-page based on new order (8 per page)
  var perPage = 8;
  sorted.forEach(function(card, i) {
    card.setAttribute('data-page', Math.floor(i / perPage) + 1);
    tops.appendChild(card); // reorder in DOM
  });

  // Reset to page 1
  tops.setAttribute('data-current-page', '1');
  // Re-trigger pagination display
  if (window._showPage) window._showPage(1);
}
window.sortCasinos = sortCasinos;

document.addEventListener('DOMContentLoaded', function() {
  // Filter game items toggle
  document.querySelectorAll('.filter-game-item').forEach(function(item) {
    item.addEventListener('click', function() {
      this.classList.toggle('active');
    });
  });
  // ESC closes filter modal
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') closeFilterModal();
  });

  // FAQ toggle
  document.querySelectorAll('.faq-q').forEach(function(q) {
    q.addEventListener('click', function() {
      this.classList.toggle('active');
      this.nextElementSibling.classList.toggle('active');
    });
  });

  // Sidebar menu
  var sidebar = document.getElementById('sidebar');
  var overlay = document.getElementById('sidebarOverlay');
  var openBtn = document.getElementById('menuOpen');
  var closeBtn = document.getElementById('menuClose');

  function openMenu() {
    if (sidebar) sidebar.classList.add('open');
    if (overlay) overlay.classList.add('open');
    document.body.style.overflow = 'hidden';
  }
  function closeMenu() {
    if (sidebar) sidebar.classList.remove('open');
    if (overlay) overlay.classList.remove('open');
    document.body.style.overflow = '';
  }

  if (openBtn) openBtn.addEventListener('click', openMenu);
  if (closeBtn) closeBtn.addEventListener('click', closeMenu);
  if (overlay) overlay.addEventListener('click', closeMenu);

  // Sidebar accordion — main headings
  document.querySelectorAll('.sidebar-nav .menu-heading').forEach(function(h) {
    h.addEventListener('click', function() {
      this.parentElement.classList.toggle('open');
    });
  });

  // Sidebar accordion — sub headings
  document.querySelectorAll('.sidebar-nav .sub-heading').forEach(function(h) {
    h.addEventListener('click', function() {
      this.parentElement.classList.toggle('sub-open');
    });
  });

  // Review FAQ toggle
  document.querySelectorAll('.review-faq .faq-q').forEach(function(q) {
    q.addEventListener('click', function() {
      this.closest('.faq-item').classList.toggle('active');
    });
  });

  // Summary box toggle
  document.querySelectorAll('.summary-header').forEach(function(h) {
    h.addEventListener('click', function() {
      this.parentElement.classList.toggle('open');
    });
  });

  // Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(function(a) {
    a.addEventListener('click', function(e) {
      var target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        var offset = 130; // topbar + subnav
        var top = target.getBoundingClientRect().top + window.pageYOffset - offset;
        window.scrollTo({ top: top, behavior: 'smooth' });
      }
    });
  });

  // Review subnav: click + scroll spy (active state)
  var subnav = document.getElementById('reviewSubnav');
  if (subnav) {
    var subnavLinks = subnav.querySelectorAll('a[data-section]');
    var sectionIds = Array.from(subnavLinks).map(a => a.dataset.section);
    var lockSpy = false;

    function setActive(sectionId) {
      subnavLinks.forEach(function(link) {
        link.classList.toggle('active', link.dataset.section === sectionId);
      });
    }

    // Click → immediate active state (and lock scroll spy briefly so it doesn't override)
    subnavLinks.forEach(function(link) {
      link.addEventListener('click', function(e) {
        setActive(this.dataset.section);
        lockSpy = true;
        clearTimeout(window._subnavLockTimer);
        window._subnavLockTimer = setTimeout(function() { lockSpy = false; }, 800);
      });
    });

    function updateActiveSubnav() {
      if (lockSpy) return;
      var scrollY = window.pageYOffset + 200;
      var current = sectionIds[0];
      sectionIds.forEach(function(id) {
        var el = document.getElementById(id);
        if (el && el.offsetTop <= scrollY) current = id;
      });
      setActive(current);
      var activeLink = subnav.querySelector('a.active');
      if (activeLink) {
        var inner = subnav.querySelector('.review-subnav-inner');
        var linkRect = activeLink.getBoundingClientRect();
        var innerRect = inner.getBoundingClientRect();
        if (linkRect.left < innerRect.left || linkRect.right > innerRect.right) {
          activeLink.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
        }
      }
    }
    window.addEventListener('scroll', updateActiveSubnav, { passive: true });
    updateActiveSubnav();
  }

  // Sort options click handlers
  document.querySelectorAll('.sort-option').forEach(function(opt) {
    opt.addEventListener('click', function(e) {
      e.stopPropagation();
      var key = this.dataset.sort;
      var label = this.textContent.replace(/^\W+/, '').trim();
      document.querySelectorAll('.sort-option').forEach(function(o) { o.classList.remove('active'); });
      this.classList.add('active');
      var labelEl = document.getElementById('sortLabel');
      if (labelEl) labelEl.textContent = label;
      var dropdown = document.querySelector('.sort-dropdown');
      if (dropdown) dropdown.classList.remove('open');
      sortCasinos(key);
    });
  });
  // Click outside to close dropdown
  document.addEventListener('click', function(e) {
    var dropdown = document.querySelector('.sort-dropdown');
    if (dropdown && dropdown.classList.contains('open') && !dropdown.contains(e.target)) {
      dropdown.classList.remove('open');
    }
  });

  // Pagination on casino tops
  var tops = document.querySelector('.casino-tops');
  if (tops) {
    var totalPages = parseInt(tops.getAttribute('data-total-pages') || '1');
    var currentPage = 1;

    function showPage(page) {
      page = Math.max(1, Math.min(totalPages, parseInt(page)));
      currentPage = page;
      tops.setAttribute('data-current-page', page);

      // Show/hide cards
      var cards = tops.querySelectorAll('.top-card');
      cards.forEach(function(card) {
        var cardPage = parseInt(card.getAttribute('data-page') || '1');
        card.style.display = (cardPage === page) ? '' : 'none';
      });

      // Update pagination buttons (top + bottom)
      document.querySelectorAll('.pagination-btn').forEach(function(btn) {
        btn.classList.remove('active');
        btn.removeAttribute('aria-disabled');
        var btnPage = btn.getAttribute('data-page');
        if (btnPage === String(page)) btn.classList.add('active');
        if (btnPage === 'prev' && page === 1) btn.setAttribute('aria-disabled', 'true');
        if (btnPage === 'next' && page === totalPages) btn.setAttribute('aria-disabled', 'true');
      });
    }

    // Expose showPage globally so sort can re-trigger it
    window._showPage = showPage;

    if (totalPages > 1) {
      // Attach click handlers to ALL pagination buttons globally
      document.querySelectorAll('.pagination-btn').forEach(function(btn) {
        btn.addEventListener('click', function(e) {
          e.preventDefault();
          var target = this.getAttribute('data-page');
          if (target === 'prev') target = currentPage - 1;
          else if (target === 'next') target = currentPage + 1;
          else target = parseInt(target);
          if (target >= 1 && target <= totalPages && target !== currentPage) {
            showPage(target);
            // Smooth scroll to top of casino list
            var topPagination = document.querySelector('.pagination-wrap');
            if (topPagination) {
              var rect = topPagination.getBoundingClientRect();
              var y = window.pageYOffset + rect.top - 120;
              window.scrollTo({ top: y, behavior: 'smooth' });
            }
          }
        });
      });
      // Init: show page 1
      showPage(1);
    }
  }
});
