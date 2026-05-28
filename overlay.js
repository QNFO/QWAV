/**
 * public/overlay.js — Living Paper (#82)
 * Injects equation click-to-explain interactivity into MathJax-rendered paper pages.
 *
 * Architecture:
 *   1. Wait for MathJax to finish rendering (or detect raw LaTeX)
 *   2. Scan DOM for equation elements
 *   3. Attach click handlers — on click, fetch explanation from Worker
 *   4. Render tooltip with explanation, variables, related equations, cite button
 *
 * Deploy: Include via <script> tag in paper page <head> or inject via Service Worker.
 */

(function () {
  'use strict';

  // DEBUG: confirm IIFE executes
  console.log('[LP-DEBUG] overlay.js IIFE started at ' + new Date().toISOString());
  window._LP_OVERLAY_LOADED = true;

  // ── Configuration ──────────────────────────────────────────────
  const CONFIG = {
    apiBase: window.LIVING_PAPER_API || '/api',
    paperId: window.LIVING_PAPER_PAPER_ID || document.title || 'unknown',
    tooltipMaxWidth: 480,
    tooltipOffset: 12,
    loadingTimeout: 20000,
    cachePrefix: 'lp_explain_',
    // MathJax selector patterns (in priority order)
    mathJaxSelectors: [
      'mjx-container[data-latex]',       // MathJax v3+ SVG output
      'script[type="math/tex"]',         // Raw LaTeX (pre-processed)
      'span.MathJax',                    // MathJax v2 HTML output
      '.MathJax_Preview',                // MathJax preview span
    ],
  };

  // ── State ──────────────────────────────────────────────────────
  let tooltipEl = null;
  let activeEquation = null;
  let abortController = null;

  // ── Utility: Extract LaTeX from element ────────────────────────
  function extractLatex(el) {
    // Strategy 1: data-latex on the mjx-container itself
    let dataLatex = el.getAttribute('data-latex');
    if (dataLatex) return dataLatex;

    // Strategy 2: .lp-equation wrapper (set by preserve-latex.js)
    const wrapper = el.closest('.lp-equation');
    if (wrapper) {
      dataLatex = wrapper.getAttribute('data-latex');
      if (dataLatex) return dataLatex;
    }

    // Strategy 3: Any ancestor with data-latex
    dataLatex = el.closest('[data-latex]')?.getAttribute('data-latex');
    if (dataLatex) return dataLatex;

    // Strategy 4: MathJax v2 script[type="math/tex"] sibling or child
    const scriptEl = el.querySelector('script[type="math/tex"], script[type="math/tex; mode=display"]');
    if (scriptEl) return scriptEl.textContent.trim();

    // Strategy 5: Raw LaTeX in text content (last resort)
    const text = el.textContent.trim();
    if (text && text.length > 2) return text;

    return null;
  }

  // ── Utility: Simple hash for dedup ─────────────────────────────
  function simpleHash(str) {
    let hash = 0;
    for (let i = 0; i < str.length; i++) {
      const char = str.charCodeAt(i);
      hash = ((hash << 5) - hash) + char;
      hash |= 0;
    }
    return Math.abs(hash).toString(36);
  }

  // ── Tooltip: Create ────────────────────────────────────────────
  function createTooltip() {
    if (tooltipEl) return tooltipEl;

    tooltipEl = document.createElement('div');
    tooltipEl.id = 'living-paper-tooltip';
    tooltipEl.setAttribute('role', 'dialog');
    tooltipEl.setAttribute('aria-label', 'Equation explanation');
    tooltipEl.innerHTML = `
      <div class="lp-tooltip-arrow"></div>
      <div class="lp-tooltip-header">
        <span class="lp-tooltip-title">Equation Explanation</span>
        <button class="lp-tooltip-close" aria-label="Close">&times;</button>
      </div>
      <div class="lp-tooltip-body">
        <div class="lp-loading">Analyzing equation...</div>
      </div>
    `;

    // Inject styles if not already present
    if (!document.getElementById('living-paper-styles')) {
      const style = document.createElement('style');
      style.id = 'living-paper-styles';
      style.textContent = getStyles();
      document.head.appendChild(style);
    }

    // Close button handler
    tooltipEl.querySelector('.lp-tooltip-close').addEventListener('click', hideTooltip);

    // Click outside to close
    document.addEventListener('click', (e) => {
      if (tooltipEl && !tooltipEl.contains(e.target) && e.target !== activeEquation) {
        hideTooltip();
      }
    });

    // Escape key to close
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && tooltipEl && tooltipEl.style.display !== 'none') {
        hideTooltip();
      }
    });

    document.body.appendChild(tooltipEl);
    return tooltipEl;
  }

  // ── Tooltip: Show ──────────────────────────────────────────────
  function showTooltip(equationEl, latex) {
    const tooltip = createTooltip();
    const body = tooltip.querySelector('.lp-tooltip-body');

    // Position tooltip near the equation
    const rect = equationEl.getBoundingClientRect();
    const scrollTop = window.scrollY || document.documentElement.scrollTop;
    const scrollLeft = window.scrollX || document.documentElement.scrollLeft;

    let top = rect.bottom + scrollTop + CONFIG.tooltipOffset;
    let left = rect.left + scrollLeft;

    // Keep tooltip in viewport
    const tooltipW = CONFIG.tooltipMaxWidth;
    if (left + tooltipW > window.innerWidth + scrollLeft) {
      left = window.innerWidth + scrollLeft - tooltipW - 16;
    }
    if (left < scrollLeft + 8) left = scrollLeft + 8;

    tooltip.style.top = `${top}px`;
    tooltip.style.left = `${left}px`;
    tooltip.style.display = 'block';

    // Loading state
    body.innerHTML = '<div class="lp-loading"><span class="lp-spinner"></span> Analyzing equation...</div>';
    activeEquation = equationEl;

    // Fetch explanation
    fetchExplanation(latex).then((result) => {
      if (activeEquation !== equationEl) return; // user clicked elsewhere

      if (result.error) {
        body.innerHTML = `<div class="lp-error">${escapeHtml(result.message || result.error)}</div>`;
        return;
      }

      body.innerHTML = renderExplanation(result, latex);
    }).catch((err) => {
      if (activeEquation !== equationEl) return;
      body.innerHTML = `<div class="lp-error">Failed to load explanation: ${escapeHtml(err.message)}</div>`;
    });
  }

  // ── Tooltip: Hide ──────────────────────────────────────────────
  function hideTooltip() {
    if (tooltipEl) {
      tooltipEl.style.display = 'none';
    }
    activeEquation = null;
    if (abortController) {
      abortController.abort();
      abortController = null;
    }
  }

  // ── Fetch: Call Worker API ─────────────────────────────────────
  async function fetchExplanation(latex) {
    // Check cache first (sessionStorage)
    const cacheKey = CONFIG.cachePrefix + simpleHash(latex);
    const cached = sessionStorage.getItem(cacheKey);
    if (cached) {
      return JSON.parse(cached);
    }

    abortController = new AbortController();
    const timeout = setTimeout(() => abortController.abort(), CONFIG.loadingTimeout);

    try {
      const response = await fetch(`${CONFIG.apiBase}/explain`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          equation: latex,
          paper_id: CONFIG.paperId,
        }),
        signal: abortController.signal,
      });

      clearTimeout(timeout);

      if (!response.ok) {
        const err = await response.json().catch(() => ({ message: `HTTP ${response.status}` }));
        return { error: true, message: err.message || err.error || `Server error (${response.status})` };
      }

      const result = await response.json();

      // Cache in sessionStorage
      try {
        sessionStorage.setItem(cacheKey, JSON.stringify(result));
      } catch (e) {
        // sessionStorage full — ignore
      }

      return result;
    } catch (err) {
      clearTimeout(timeout);
      if (err.name === 'AbortError') {
        return { error: true, message: 'Request timed out. Try again.' };
      }
      return { error: true, message: 'Network error. Is the API available?' };
    }
  }

  // ── Render: Build explanation HTML ─────────────────────────────
  function renderExplanation(result, latex) {
    const relatedHtml = (result.related_equations && result.related_equations.length > 0)
      ? `
        <div class="lp-related">
          <h4>Related Equations</h4>
          <ul>
            ${result.related_equations.map((r) => `
              <li>
                <a href="${escapeHtml(r.url)}" target="_blank" rel="noopener">
                  <span class="lp-related-paper">${escapeHtml(r.paper_title)}</span>
                  <span class="lp-related-similarity">${(r.similarity * 100).toFixed(0)}% match</span>
                </a>
                <code class="lp-related-eq">${escapeHtml(r.equation?.substring(0, 80) || '')}${r.equation?.length > 80 ? '...' : ''}</code>
              </li>
            `).join('')}
          </ul>
        </div>`
      : '<div class="lp-no-related">No related equations found in corpus.</div>';

    const variablesHtml = (result.variables && Object.keys(result.variables).length > 0)
      ? `
        <div class="lp-variables">
          <h4>Variables</h4>
          <dl>
            ${Object.entries(result.variables).map(([sym, meaning]) => `
              <dt><code>${escapeHtml(sym)}</code></dt>
              <dd>${escapeHtml(meaning)}</dd>
            `).join('')}
          </dl>
        </div>`
      : '';

    const cachedBadge = result.cached
      ? '<span class="lp-cached-badge" title="Served from cache">⚡ cached</span>'
      : '';

    return `
      <div class="lp-explanation">
        <div class="lp-equation-display">$$${escapeHtml(latex)}$$</div>
        <p class="lp-explanation-text">${escapeHtml(result.explanation || result.response || 'No explanation available.')}</p>
        ${cachedBadge}
        ${variablesHtml}
        <div class="lp-domain"><strong>Domain:</strong> ${escapeHtml(result.domain || 'Unknown')}</div>
        ${relatedHtml}
        <div class="lp-actions">
          <button class="lp-cite-btn" data-latex="${escapeAttr(latex)}" data-paper="${escapeAttr(CONFIG.paperId)}">
            📋 Cite Equation
          </button>
        </div>
      </div>
    `;
  }

  // ── Cite Button Handler ────────────────────────────────────────
  function handleCiteClick(e) {
    const btn = e.target.closest('.lp-cite-btn');
    if (!btn) return;

    const latex = btn.getAttribute('data-latex');
    const paper = btn.getAttribute('data-paper');
    const bibtex = `@misc{${paper}_equation,
  title = {Equation from ${paper}},
  note = {\\\\(${latex}\\\\)},
  howpublished = {\\url{https://${paper}.qnfo.org}},
  year = {${new Date().getFullYear()}},
}`;

    navigator.clipboard.writeText(bibtex).then(() => {
      const original = btn.textContent;
      btn.textContent = '✅ Copied!';
      btn.classList.add('lp-copied');
      setTimeout(() => {
        btn.textContent = original;
        btn.classList.remove('lp-copied');
      }, 2000);
    }).catch(() => {
      // Fallback: select text
      const textarea = document.createElement('textarea');
      textarea.value = bibtex;
      textarea.style.position = 'fixed';
      textarea.style.opacity = '0';
      document.body.appendChild(textarea);
      textarea.select();
      document.execCommand('copy');
      document.body.removeChild(textarea);
      btn.textContent = '✅ Copied!';
      setTimeout(() => { btn.textContent = '📋 Cite Equation'; }, 2000);
    });
  }

  // ── Event Delegation: Equation clicks ──────────────────────────
  function handleEquationClick(e) {
    // Find the nearest equation container
    let equationEl = e.target.closest('mjx-container, .MathJax, [data-latex]');

    // If click is on raw LaTeX (inside a code block or span), try to find it
    if (!equationEl) {
      // Check if clicked element contains LaTeX-like content
      const text = e.target.textContent || '';
      if (text.includes('$$') || text.includes('\\')) {
        equationEl = e.target;
      }
    }

    if (!equationEl) return;

    const latex = extractLatex(equationEl);
    if (!latex) return;

    e.preventDefault();
    e.stopPropagation();

    // Toggle: if same equation, hide; else show new
    if (activeEquation === equationEl) {
      hideTooltip();
    } else {
      showTooltip(equationEl, latex);
    }
  }

  // ── Initialization: Scan DOM and attach listeners ──────────────
  function init() {
    // Remove any existing listeners (idempotent)
    document.removeEventListener('click', handleEquationClick, true);

    // Use capture phase to intercept before other handlers
    document.addEventListener('click', handleEquationClick, true);

    // Cite button handler (delegated)
    document.addEventListener('click', handleCiteClick);

    // Add visual indicator: equations get a subtle hover effect
    addVisualIndicators();
  }

  // ── Visual: Add hover indicators to equations ──────────────────
  function addVisualIndicators() {
    const styleId = 'lp-indicator-styles';
    if (document.getElementById(styleId)) return;

    const style = document.createElement('style');
    style.id = styleId;
    style.textContent = `
      /* Clickable equation indicator */
      mjx-container[data-latex],
      .MathJax,
      span.MathJax {
        cursor: pointer;
        transition: background-color 0.2s ease, box-shadow 0.2s ease;
        border-radius: 3px;
        padding: 2px 4px;
      }
      mjx-container[data-latex]:hover,
      .MathJax:hover,
      span.MathJax:hover {
        background-color: rgba(59, 130, 246, 0.08);
        box-shadow: 0 0 0 1px rgba(59, 130, 246, 0.2);
      }
      /* Active equation */
      mjx-container.lp-active,
      .MathJax.lp-active {
        background-color: rgba(59, 130, 246, 0.15);
        box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.4);
      }
    `;
    document.head.appendChild(style);
  }

  // ── Wait for MathJax: retry until found or timeout ─────────────
  function waitForMathJax(maxAttempts = 20, interval = 500) {
    return new Promise((resolve) => {
      let attempts = 0;

      function check() {
        attempts++;
        // Check for MathJax-processed elements
        const hasMathJax = document.querySelector('mjx-container, .MathJax, script[type="math/tex"]');
        if (hasMathJax) {
          resolve(true);
          return;
        }

        // Also check for raw LaTeX
        const bodyText = document.body?.textContent || '';
        const hasLatex = bodyText.includes('$$') || bodyText.includes('\\begin{');

        if (hasLatex || attempts >= maxAttempts) {
          resolve(hasLatex);
          return;
        }

        setTimeout(check, interval);
      }

      check();
    });
  }

  // ── Stylesheet ─────────────────────────────────────────────────
  function getStyles() {
    return `
      #living-paper-tooltip {
        display: none;
        position: absolute;
        z-index: 99999;
        max-width: ${CONFIG.tooltipMaxWidth}px;
        width: 90vw;
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.12), 0 2px 8px rgba(0,0,0,0.08);
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        font-size: 14px;
        line-height: 1.6;
        color: #1a202c;
        overflow: hidden;
      }
      .lp-tooltip-arrow {
        display: none;
      }
      .lp-tooltip-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 14px;
        background: #f7fafc;
        border-bottom: 1px solid #e2e8f0;
      }
      .lp-tooltip-title {
        font-weight: 600;
        font-size: 13px;
        color: #4a5568;
        text-transform: uppercase;
        letter-spacing: 0.05em;
      }
      .lp-tooltip-close {
        background: none;
        border: none;
        font-size: 20px;
        cursor: pointer;
        color: #a0aec0;
        padding: 0 4px;
        line-height: 1;
      }
      .lp-tooltip-close:hover {
        color: #4a5568;
      }
      .lp-tooltip-body {
        padding: 14px;
        max-height: 60vh;
        overflow-y: auto;
      }
      .lp-loading {
        display: flex;
        align-items: center;
        gap: 8px;
        color: #718096;
        font-style: italic;
      }
      .lp-spinner {
        display: inline-block;
        width: 16px;
        height: 16px;
        border: 2px solid #e2e8f0;
        border-top-color: #3b82f6;
        border-radius: 50%;
        animation: lp-spin 0.8s linear infinite;
      }
      @keyframes lp-spin {
        to { transform: rotate(360deg); }
      }
      .lp-error {
        color: #e53e3e;
        padding: 8px;
        background: #fff5f5;
        border-radius: 4px;
      }
      .lp-explanation-text {
        margin: 8px 0 12px;
        color: #2d3748;
      }
      .lp-equation-display {
        font-size: 16px;
        padding: 10px;
        background: #f7fafc;
        border-radius: 4px;
        margin-bottom: 10px;
        overflow-x: auto;
      }
      .lp-cached-badge {
        display: inline-block;
        font-size: 11px;
        color: #718096;
        background: #edf2f7;
        padding: 1px 6px;
        border-radius: 3px;
        margin-left: 8px;
      }
      .lp-domain {
        font-size: 12px;
        color: #718096;
        margin: 8px 0;
      }
      .lp-variables {
        margin: 12px 0;
      }
      .lp-variables h4,
      .lp-related h4 {
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #718096;
        margin: 0 0 6px;
      }
      .lp-variables dl {
        margin: 0;
        display: grid;
        grid-template-columns: auto 1fr;
        gap: 4px 12px;
      }
      .lp-variables dt {
        font-weight: 600;
        color: #2b6cb0;
      }
      .lp-variables dd {
        margin: 0;
        color: #4a5568;
      }
      .lp-related ul {
        list-style: none;
        padding: 0;
        margin: 0;
      }
      .lp-related li {
        padding: 8px 0;
        border-bottom: 1px solid #f7fafc;
      }
      .lp-related li:last-child {
        border-bottom: none;
      }
      .lp-related a {
        text-decoration: none;
        color: #2b6cb0;
        display: flex;
        justify-content: space-between;
        align-items: baseline;
      }
      .lp-related a:hover {
        text-decoration: underline;
      }
      .lp-related-paper {
        font-weight: 500;
      }
      .lp-related-similarity {
        font-size: 11px;
        color: #a0aec0;
        white-space: nowrap;
      }
      .lp-related-eq {
        display: block;
        font-size: 12px;
        color: #718096;
        margin-top: 2px;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
      }
      .lp-no-related {
        color: #a0aec0;
        font-style: italic;
        font-size: 13px;
      }
      .lp-actions {
        margin-top: 12px;
        padding-top: 10px;
        border-top: 1px solid #f7fafc;
      }
      .lp-cite-btn {
        background: #edf2f7;
        border: 1px solid #e2e8f0;
        padding: 6px 12px;
        border-radius: 4px;
        cursor: pointer;
        font-size: 13px;
        color: #4a5568;
        transition: all 0.15s ease;
      }
      .lp-cite-btn:hover {
        background: #e2e8f0;
        border-color: #cbd5e0;
      }
      .lp-cite-btn.lp-copied {
        background: #c6f6d5;
        border-color: #9ae6b4;
        color: #276749;
      }

      /* Mobile responsiveness */
      @media (max-width: 640px) {
        #living-paper-tooltip {
          max-width: 95vw;
          left: 2.5vw !important;
          position: fixed;
          bottom: 16px;
          top: auto !important;
        }
      }
    `;
  }

  // ── Utility: HTML escape ───────────────────────────────────────
  function escapeHtml(str) {
    if (!str) return '';
    const div = document.createElement('div');
    div.textContent = str;
    return div.innerHTML;
  }

  // ── Utility: Attribute escape ──────────────────────────────────
  function escapeAttr(str) {
    return str.replace(/"/g, '&quot;').replace(/'/g, '&#39;');
  }

  // ── Bootstrap ──────────────────────────────────────────────────
  waitForMathJax().then((found) => {
    if (found) {
      init();
      console.log('[LivingPaper] Equation overlay initialized. Paper:', CONFIG.paperId);
    } else {
      console.log('[LivingPaper] No equations detected on this page. Overlay skipped.');
    }
  }).catch((err) => {
    console.error('[LivingPaper] Initialization failed:', err);
  });
})();
