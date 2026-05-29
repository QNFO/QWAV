/**
 * related.js — Related paper discovery sidebar for Living Papers v2
 * Matches by keyword overlap from the paper catalog.
 */
(function() {
  'use strict';

  const CATALOG_URL = '/papers/catalog.json';
  let catalog = null;

  // ── UI ──────────────────────────────────────────────────────────
  function createWidget() {
    const el = document.createElement('aside');
    el.className = 'related-papers';
    el.setAttribute('aria-label', 'Related papers');
    el.innerHTML = '<h3 class="related-heading">Related Papers</h3><div class="related-loading">Loading…</div>';
    document.querySelector('article').appendChild(el);
    return el;
  }

  function renderPapers(widget, papers) {
    if (!papers.length) {
      widget.querySelector('.related-loading').innerHTML = 'No related papers found.';
      return;
    }
    const html = papers.slice(0, 5).map(p => `
      <a class="related-card" href="/papers/paper.html?p=${p.slug}">
        <div class="related-card-title">${p.title}</div>
        ${p.date ? '<div class="related-card-date">' + new Date(p.date).toLocaleDateString('en-US', {year:'numeric',month:'short'}) + '</div>' : ''}
      </a>
    `).join('');
    widget.querySelector('.related-loading').innerHTML = html;
  }

  // ── Matching ────────────────────────────────────────────────────
  function findRelated(currentSlug, currentKeywords) {
    if (!catalog || !catalog.papers) return [];
    const current = currentSlug.toLowerCase();
    const kwSet = new Set((currentKeywords || []).map(k => k.toLowerCase().trim()));

    const scored = catalog.papers
      .filter(p => p.slug && p.slug.toLowerCase() !== current)
      .map(p => {
        const pKw = (p.keywords || []).map(k => k.toLowerCase().trim());
        const overlap = pKw.filter(k => kwSet.has(k)).length;
        return { ...p, score: overlap };
      })
      .filter(p => p.score > 0)
      .sort((a, b) => b.score - a.score);

    return scored;
  }

  // ── Init ────────────────────────────────────────────────────────
  async function init() {
    const widget = createWidget();
    const slug = window.LIVING_PAPER_PAPER_ID;

    try {
      const res = await fetch(CATALOG_URL);
      if (!res.ok) throw new Error('Catalog unavailable');
      catalog = await res.json();

      // Get current paper keywords from meta
      const kwMeta = document.querySelector('meta[name="keywords"]');
      const keywords = kwMeta ? kwMeta.content.split(',').map(k => k.trim()) : [];
      const related = findRelated(slug, keywords);
      renderPapers(widget, related);
    } catch (e) {
      widget.querySelector('.related-loading').innerHTML = 'Related papers unavailable.';
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    setTimeout(init, 1000); // Wait for paper content to load
  }
})();
