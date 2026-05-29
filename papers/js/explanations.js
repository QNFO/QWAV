/**
 * explanations.js — AI-powered equation explanations for Living Papers v2
 * Hover any MathJax equation → Workers AI generates an explanation.
 * Click to pin overlay; click again or press Esc to dismiss.
 */
(function() {
  'use strict';

  const AI_ENDPOINT = '/api/explain'; // Workers AI proxy
  const CACHE_KEY = 'qwav_explanations';
  const cache = JSON.parse(localStorage.getItem(CACHE_KEY) || '{}');

  // ── UI ──────────────────────────────────────────────────────────
  let overlay = null;

  function createOverlay() {
    if (overlay) return overlay;
    overlay = document.createElement('div');
    overlay.className = 'eq-overlay';
    overlay.setAttribute('role', 'tooltip');
    overlay.innerHTML = '<div class="eq-overlay-inner"><div class="eq-overlay-loading">Analyzing equation…</div><button class="eq-overlay-close" title="Dismiss">×</button></div>';
    document.body.appendChild(overlay);
    overlay.querySelector('.eq-overlay-close').onclick = hideOverlay;
    document.addEventListener('keydown', e => { if (e.key === 'Escape') hideOverlay(); });
    document.addEventListener('click', e => { if (!overlay.contains(e.target) && !e.target.closest('.MathJax')) hideOverlay(); });
    return overlay;
  }

  function showOverlay(x, y, tex, explanation) {
    const ov = createOverlay();
    const inner = ov.querySelector('.eq-overlay-inner');
    inner.innerHTML = `
      <div class="eq-overlay-tex">\`${tex.replace(/`/g, '\\`')}\`</div>
      <div class="eq-overlay-explanation">${explanation}</div>
      <button class="eq-overlay-close" title="Dismiss">×</button>
    `;
    ov.querySelector('.eq-overlay-close').onclick = hideOverlay;
    ov.classList.add('visible');
    positionOverlay(ov, x, y);
  }

  function showLoading(x, y) {
    const ov = createOverlay();
    ov.querySelector('.eq-overlay-inner').innerHTML = '<div class="eq-overlay-loading"><span class="spinner"></span> Analyzing equation…</div><button class="eq-overlay-close" title="Dismiss">×</button>';
    ov.querySelector('.eq-overlay-close').onclick = hideOverlay;
    ov.classList.add('visible');
    positionOverlay(ov, x, y);
  }

  function hideOverlay() {
    if (overlay) overlay.classList.remove('visible');
  }

  function positionOverlay(ov, x, y) {
    const rect = ov.getBoundingClientRect();
    let left = x + 10, top = y - rect.height - 10;
    if (top < 10) top = y + 20;
    if (left + rect.width > window.innerWidth - 20) left = window.innerWidth - rect.width - 20;
    ov.style.left = left + 'px';
    ov.style.top = top + 'px';
  }

  // ── AI Fetch ────────────────────────────────────────────────────
  async function fetchExplanation(tex, context) {
    const key = tex.trim();
    if (cache[key]) return cache[key];

    try {
      const res = await fetch(AI_ENDPOINT, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ equation: key, context: context || '' })
      });
      if (!res.ok) throw new Error('AI unavailable');
      const data = await res.json();
      const explanation = data.explanation || data.text || 'No explanation available.';
      cache[key] = explanation;
      localStorage.setItem(CACHE_KEY, JSON.stringify(cache));
      return explanation;
    } catch (e) {
      return 'Could not generate explanation. The AI service may be unavailable.';
    }
  }

  function getContext(el) {
    let p = el.closest('p, li, div');
    if (p) return p.textContent.substring(0, 500);
    return '';
  }

  // ── Equation Detection ──────────────────────────────────────────
  function extractTex(el) {
    const mjx = el.querySelector('mjx-container');
    if (mjx) {
      const data = mjx.getAttribute('data-mjx-tex') || mjx.textContent || '';
      return data.replace(/\s+/g, ' ').trim();
    }
    return el.textContent.replace(/\s+/g, ' ').trim();
  }

  function attachToEquations() {
    // Wait for MathJax to finish rendering
    const check = () => {
      const eqs = document.querySelectorAll('.MathJax, mjx-container');
      if (eqs.length === 0) { setTimeout(check, 500); return; }

      eqs.forEach(el => {
        if (el.dataset.qwavExplained) return;
        el.dataset.qwavExplained = '1';
        el.style.cursor = 'pointer';
        el.title = 'Click for AI explanation';

        let pinned = false;

        el.addEventListener('mouseenter', async function(e) {
          if (pinned) return;
          const tex = extractTex(el);
          if (!tex || tex.length < 2) return;
          const rect = el.getBoundingClientRect();
          showLoading(rect.left, rect.top);
          const explanation = await fetchExplanation(tex, getContext(el));
          if (!pinned) showOverlay(rect.left, rect.top, tex, explanation);
        });

        el.addEventListener('mouseleave', function() {
          if (!pinned) hideOverlay();
        });

        el.addEventListener('click', function(e) {
          e.stopPropagation();
          pinned = !pinned;
          if (pinned) {
            const tex = extractTex(el);
            const rect = el.getBoundingClientRect();
            showLoading(rect.left, rect.top);
            fetchExplanation(tex, getContext(el)).then(explanation => {
              if (pinned) showOverlay(rect.left, rect.top, tex, explanation);
            });
            el.style.outline = '2px solid var(--link)';
            el.style.outlineOffset = '3px';
          } else {
            hideOverlay();
            el.style.outline = '';
          }
        });
      });
    };
    setTimeout(check, 1500);
  }

  // ── Init ────────────────────────────────────────────────────────
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', attachToEquations);
  } else {
    attachToEquations();
  }

  // Expose for external use
  window.LivingPapers = window.LivingPapers || {};
  window.LivingPapers.explanations = { showOverlay, hideOverlay, fetchExplanation };
})();
