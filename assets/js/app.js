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
        target.scrollIntoView({ behavior: 'smooth' });
      }
    });
  });
});
