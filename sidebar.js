/**
 * public/sidebar.js — Living Paper (#82)
 * Related Concepts sidebar widget.
 *
 * Queries /api/related for concepts similar to the current paper context,
 * displays as a sidebar panel with concept cards linking to related papers.
 *
 * Deploy: Include via <script> tag in paper page <head> or inject via Service Worker.
 */

(function () {
  'use strict';

  // ── Configuration ──────────────────────────────────────────────
  const CONFIG = {
    apiBase: window.LIVING_PAPER_API || '/api',
    paperId: window.LIVING_PAPER_PAPER_ID || document.title || 'unknown',
    sidebarPosition: window.LIVING_PAPER_SIDEBAR_POSITION || 'right', // 'right' or 'left'
    sidebarWidth: 320,
    collapsedWidth: 40,
    autoExpand: true,
    // Extract context from: page title, first <h1>, meta description
    contextSources: [
      () => document.querySelector('h1')?.textContent || '',
      () => document.querySelector('meta[name="description"]')?.getAttribute('content') || '',
      () => document.querySelector('.abstract, #abstract, [data-abstract]')?.textContent || '',
    ],
  };

  // ── State ──────────────────────────────────────────────────────
  let sidebarEl = null;
  let isExpanded = false;
  let conceptResults = [];
  let isLoading = false;

  // ── Create Sidebar DOM ─────────────────────────────────────────
  function createSidebar() {
    if (sidebarEl) return;

    // Inject styles
    if (!document.getElementById('lp-sidebar-styles')) {
      const style = document.createElement('style');
      style.id = 'lp-sidebar-styles';
      style.textContent = getSidebarStyles();
      document.head.appendChild(style);
    }

    sidebarEl = document.createElement('div');
    sidebarEl.id = 'living-paper-sidebar';
    sidebarEl.setAttribute('role', 'complementary');
    sidebarEl.setAttribute('aria-label', 'Related concepts');

    sidebarEl.innerHTML = `
      <button class="lp-sidebar-toggle" aria-label="Toggle concept sidebar" title="Related Concepts">
        <span class="lp-toggle-icon">&#9758;</span>
        <span class="lp-toggle-label">Concepts</span>
      </button>
      <div class="lp-sidebar-panel">
        <div class="lp-sidebar-header">
          <h3>Related Concepts</h3>
          <button class="lp-sidebar-close" aria-label="Close sidebar">&times;</button>
        </div>
        <div class="lp-sidebar-content">
          <div class="lp-sidebar-loading">
            <span class="lp-spinner"></span> Finding related concepts...
          </div>
        </div>
      </div>
    `;

    document.body.appendChild(sidebarEl);

    // Event listeners
    sidebarEl.querySelector('.lp-sidebar-toggle').addEventListener('click', toggleSidebar);
    sidebarEl.querySelector('.lp-sidebar-close').addEventListener('click', collapseSidebar);

    // Keyboard shortcut: Ctrl+Shift+C to toggle
    document.addEventListener('keydown', (e) => {
      if (e.ctrlKey && e.shiftKey && e.key === 'C') {
        e.preventDefault();
        toggleSidebar();
      }
    });

    // If auto-expand, fetch results immediately
    if (CONFIG.autoExpand) {
      fetchConcepts().then(() => {
        if (conceptResults.length > 0) {
          expandSidebar();
        }
      });
    }

    return sidebarEl;
  }

  // ── Toggle / Expand / Collapse ─────────────────────────────────
  function toggleSidebar() {
    if (isExpanded) {
      collapseSidebar();
    } else {
      expandSidebar();
    }
  }

  function expandSidebar() {
    if (!sidebarEl) createSidebar();
    sidebarEl.classList.add('lp-expanded');
    isExpanded = true;

    // Fetch if not yet loaded
    if (conceptResults.length === 0 && !isLoading) {
      fetchConcepts();
    }
  }

  function collapseSidebar() {
    if (sidebarEl) {
      sidebarEl.classList.remove('lp-expanded');
    }
    isExpanded = false;
  }

  // ── Extract page context ───────────────────────────────────────
  function getPageContext() {
    const parts = [];
    for (const source of CONFIG.contextSources) {
      try {
        const text = source();
        if (text && text.trim().length > 5) {
          parts.push(text.trim());
        }
      } catch (e) {
        // source not available — skip
      }
    }
    return parts.join('. ').substring(0, 1000); // limit context length
  }

  // ── Fetch related concepts ─────────────────────────────────────
  async function fetchConcepts() {
    if (isLoading) return;
    isLoading = true;

    const context = getPageContext();
    const contentEl = sidebarEl.querySelector('.lp-sidebar-content');

    contentEl.innerHTML = '<div class="lp-sidebar-loading"><span class="lp-spinner"></span> Finding related concepts...</div>';

    try {
      const response = await fetch(`${CONFIG.apiBase}/related`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          equation: context || CONFIG.paperId,
          paper_id: CONFIG.paperId,
          topK: 10,
        }),
      });

      if (!response.ok) {
        throw new Error(`HTTP ${response.status}`);
      }

      const data = await response.json();
      conceptResults = data.results || [];

      renderConcepts();
    } catch (err) {
      contentEl.innerHTML = `
        <div class="lp-sidebar-error">
          <p>Could not load related concepts.</p>
          <button class="lp-retry-btn" onclick="document.querySelector('#living-paper-sidebar .lp-retry-btn')?.dispatchEvent(new Event('lp-retry'))">Retry</button>
        </div>
      `;
    } finally {
      isLoading = false;
    }
  }

  // ── Render concept cards ───────────────────────────────────────
  function renderConcepts() {
    if (!sidebarEl) return;

    const contentEl = sidebarEl.querySelector('.lp-sidebar-content');

    if (conceptResults.length === 0) {
      contentEl.innerHTML = `
        <div class="lp-sidebar-empty">
          <p>No related concepts found in the corpus for this paper.</p>
          <p class="lp-sidebar-hint">This may improve as more papers are indexed.</p>
        </div>
      `;
      return;
    }

    const cardsHtml = conceptResults.map((concept, i) => `
      <div class="lp-concept-card" data-index="${i}">
        <div class="lp-concept-score">
          <div class="lp-score-bar" style="width: ${Math.round(concept.similarity * 100)}%"></div>
          <span class="lp-score-text">${Math.round(concept.similarity * 100)}%</span>
        </div>
        <a href="${escapeHtml(concept.url)}" target="_blank" rel="noopener" class="lp-concept-link">
          <h4 class="lp-concept-title">${escapeHtml(concept.paper_title)}</h4>
        </a>
        ${concept.section ? `<p class="lp-concept-section">${escapeHtml(concept.section)}</p>` : ''}
        ${concept.equation ? `
          <div class="lp-concept-equation">
            <code>$$${escapeHtml(concept.equation.substring(0, 100))}${concept.equation.length > 100 ? '...' : ''}$$</code>
          </div>
        ` : ''}
      </div>
    `).join('');

    contentEl.innerHTML = `
      <p class="lp-sidebar-count">${conceptResults.length} related concepts found</p>
      <div class="lp-concept-list">
        ${cardsHtml}
      </div>
      <button class="lp-refresh-btn" id="lp-refresh-concepts">&#8635; Refresh</button>
    `;

    // Refresh button
    const refreshBtn = contentEl.querySelector('#lp-refresh-concepts');
    if (refreshBtn) {
      refreshBtn.addEventListener('click', () => {
        conceptResults = [];
        fetchConcepts();
      });
    }
  }

  // ── Styles ─────────────────────────────────────────────────────
  function getSidebarStyles() {
    return `
      #living-paper-sidebar {
        position: fixed;
        top: 50%;
        ${CONFIG.sidebarPosition}: 0;
        transform: translateY(-50%);
        z-index: 99990;
        display: flex;
        flex-direction: row;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        font-size: 13px;
        line-height: 1.5;
        color: #2d3748;
      }

      /* Toggle button — always visible */
      .lp-sidebar-toggle {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 4px;
        width: ${CONFIG.collapsedWidth}px;
        min-height: 80px;
        background: #2d3748;
        color: #fff;
        border: none;
        border-radius: 6px 0 0 6px;
        cursor: pointer;
        font-size: 11px;
        padding: 8px 4px;
        writing-mode: vertical-lr;
        text-orientation: mixed;
        transition: background 0.2s;
      }
      .lp-sidebar-toggle:hover {
        background: #4a5568;
      }
      .lp-toggle-icon {
        font-size: 16px;
      }
      .lp-toggle-label {
        letter-spacing: 0.1em;
        text-transform: uppercase;
        font-weight: 600;
      }

      /* Panel — hidden by default, slides out on expand */
      .lp-sidebar-panel {
        display: none;
        width: ${CONFIG.sidebarWidth}px;
        max-height: 70vh;
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-left: none;
        border-radius: 0 6px 6px 0;
        box-shadow: 2px 2px 16px rgba(0,0,0,0.08);
        overflow: hidden;
        flex-direction: column;
      }
      #living-paper-sidebar.lp-expanded .lp-sidebar-panel {
        display: flex;
      }
      #living-paper-sidebar.lp-expanded .lp-sidebar-toggle {
        display: none;
      }

      .lp-sidebar-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 14px;
        background: #f7fafc;
        border-bottom: 1px solid #e2e8f0;
        flex-shrink: 0;
      }
      .lp-sidebar-header h3 {
        margin: 0;
        font-size: 13px;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #4a5568;
      }
      .lp-sidebar-close {
        background: none;
        border: none;
        font-size: 18px;
        cursor: pointer;
        color: #a0aec0;
      }
      .lp-sidebar-close:hover {
        color: #4a5568;
      }

      .lp-sidebar-content {
        padding: 10px 14px;
        overflow-y: auto;
        flex: 1;
      }
      .lp-sidebar-loading {
        display: flex;
        align-items: center;
        gap: 8px;
        color: #a0aec0;
        font-style: italic;
        padding: 20px 0;
      }
      .lp-sidebar-count {
        font-size: 11px;
        color: #a0aec0;
        margin: 0 0 8px;
      }
      .lp-sidebar-error {
        color: #e53e3e;
        font-size: 12px;
        text-align: center;
        padding: 16px 0;
      }
      .lp-sidebar-empty {
        color: #a0aec0;
        font-size: 12px;
        text-align: center;
        padding: 16px 0;
      }
      .lp-sidebar-hint {
        font-style: italic;
        font-size: 11px;
      }
      .lp-retry-btn,
      .lp-refresh-btn {
        display: block;
        width: 100%;
        padding: 6px;
        margin-top: 8px;
        background: #edf2f7;
        border: 1px solid #e2e8f0;
        border-radius: 4px;
        cursor: pointer;
        font-size: 12px;
        color: #4a5568;
      }
      .lp-retry-btn:hover,
      .lp-refresh-btn:hover {
        background: #e2e8f0;
      }

      /* Concept cards */
      .lp-concept-list {
        display: flex;
        flex-direction: column;
        gap: 8px;
      }
      .lp-concept-card {
        padding: 8px 10px;
        background: #f7fafc;
        border-radius: 4px;
        border: 1px solid #edf2f7;
        transition: border-color 0.15s;
      }
      .lp-concept-card:hover {
        border-color: #bee3f8;
        background: #ebf8ff;
      }
      .lp-concept-score {
        display: flex;
        align-items: center;
        gap: 6px;
        margin-bottom: 4px;
      }
      .lp-score-bar {
        height: 4px;
        background: #3b82f6;
        border-radius: 2px;
        min-width: 4px;
      }
      .lp-score-text {
        font-size: 10px;
        color: #a0aec0;
        white-space: nowrap;
      }
      .lp-concept-link {
        text-decoration: none;
        color: #2b6cb0;
      }
      .lp-concept-link:hover {
        text-decoration: underline;
      }
      .lp-concept-title {
        margin: 0;
        font-size: 13px;
        font-weight: 600;
        color: #2d3748;
        line-height: 1.3;
      }
      .lp-concept-section {
        margin: 2px 0 0;
        font-size: 11px;
        color: #718096;
      }
      .lp-concept-equation {
        margin-top: 4px;
        font-size: 12px;
        color: #4a5568;
        overflow: hidden;
      }
      .lp-concept-equation code {
        background: #edf2f7;
        padding: 2px 4px;
        border-radius: 2px;
        font-size: 11px;
      }

      /* Mobile: move to bottom */
      @media (max-width: 768px) {
        #living-paper-sidebar {
          top: auto;
          bottom: 0;
          ${CONFIG.sidebarPosition}: 0;
          transform: none;
          flex-direction: column;
        }
        .lp-sidebar-toggle {
          writing-mode: horizontal-tb;
          flex-direction: row;
          width: auto;
          min-height: auto;
          padding: 8px 16px;
          border-radius: 6px 6px 0 0;
          font-size: 12px;
        }
        .lp-sidebar-panel {
          width: 100vw;
          max-height: 50vh;
          border-radius: 6px 6px 0 0;
          border: 1px solid #e2e8f0;
        }
      }
    `;
  }

  // ── Utility ────────────────────────────────────────────────────
  function escapeHtml(str) {
    if (!str) return '';
    const div = document.createElement('div');
    div.textContent = str;
    return div.innerHTML;
  }

  // ── Bootstrap ──────────────────────────────────────────────────
  function init() {
    // Wait for page content to be available
    const context = getPageContext();
    if (context.length > 0) {
      createSidebar();
      console.log('[LivingPaper] Concept sidebar initialized. Paper:', CONFIG.paperId);
    } else {
      // Retry after DOMContentLoaded
      window.addEventListener('DOMContentLoaded', () => {
        const retryContext = getPageContext();
        if (retryContext.length > 0) {
          createSidebar();
          console.log('[LivingPaper] Concept sidebar initialized (delayed). Paper:', CONFIG.paperId);
        }
      });
    }
  }

  // Start
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
