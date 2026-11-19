/* rm-portrait: what the stylesheet cannot do. Appended after each tool's own scripts by build.py. */
(function () {
  var tabs = document.querySelector('.rm-tabs');
  var body = document.querySelector('.rm-body');

  /* The strip of tools scrolls sideways and its scrollbar is hidden: on a phone the current tool's tab was off the
     edge with nothing to say the strip moves. Bring it into view (by the strip's own scroll position, never
     scrollIntoView: inside a frame that also scrolls the page that holds it) and fade the end that has more. */
  function ends() {
    if (!tabs) return;
    var max = tabs.scrollWidth - tabs.clientWidth;
    var x = Math.abs(tabs.scrollLeft);
    var rtl = getComputedStyle(tabs).direction === 'rtl';
    var before = x > 2, after = x < max - 2;
    tabs.classList.toggle('rm-more-start', max > 2 && (rtl ? after : before));
    tabs.classList.toggle('rm-more-end', max > 2 && (rtl ? before : after));
  }
  function showCurrent() {
    if (!tabs) return;
    var on = tabs.querySelector('a.on');
    if (on) {
      var t = tabs.getBoundingClientRect(), a = on.getBoundingClientRect();
      if (a.left < t.left + 1 || a.right > t.right - 1) tabs.scrollLeft += a.left - t.left - (t.width - a.width) / 2;
    }
    ends();
  }
  if (tabs) {
    tabs.addEventListener('scroll', ends, { passive: true });
    showCurrent();
    addEventListener('load', showCurrent);
    addEventListener('resize', showCurrent);
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(showCurrent);
  }

  /* A table whose cells cannot wrap any further (a column of codes, a comparison) scrolls inside its own box rather
     than being cut by the frame: every table gets that box once, tables a tool draws later included. */
  /* A table of four columns or more cannot be read across the narrowest phones (a 240px frame): there each of its
     rows is drawn as a block, one line per cell with the column's name before it (portrait.css, `rm-cols4`). The
     names are copied from the table's own heading row. */
  function label(table) {
    if (table.getAttribute('data-rm-labelled')) return;
    var heads = table.querySelectorAll('thead th');
    if (heads.length < 4) return;
    table.setAttribute('data-rm-labelled', '1');
    table.classList.add('rm-cols4');
    var rows = table.querySelectorAll('tbody tr');
    for (var r = 0; r < rows.length; r++) {
      var cells = rows[r].children;
      for (var c = 1; c < cells.length && c < heads.length; c++) cells[c].setAttribute('data-label', heads[c].textContent.replace(/\s+/g, ' ').trim());
    }
  }
  function boxTables(root) {
    var list = (root || document).querySelectorAll ? (root || document).querySelectorAll('.rm-body table') : [];
    for (var i = 0; i < list.length; i++) {
      var table = list[i], p = table.parentElement;
      label(table);
      if (!p || p.classList.contains('rm-scroll') || (getComputedStyle(p).overflowX !== 'visible' && p !== body)) continue;
      var box = document.createElement('div');
      box.className = 'rm-scroll';
      p.insertBefore(box, table);
      box.appendChild(table);
    }
  }
  boxTables(document);
  if (body && window.MutationObserver) {
    new MutationObserver(function (changes) {
      for (var i = 0; i < changes.length; i++) if (changes[i].addedNodes.length) { boxTables(document); return; }
    }).observe(body, { childList: true, subtree: true });
  }
})();
