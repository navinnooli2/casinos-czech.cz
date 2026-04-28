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
window.openFilterModal = openFilterModal;
window.closeFilterModal = closeFilterModal;

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
