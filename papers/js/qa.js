/**
 * qa.js — Paper-specific Q&A chat panel for Living Papers v2
 * Floating button → slide-out chat → Workers AI answers questions about the paper.
 */
(function() {
  'use strict';

  const AI_ENDPOINT = '/api/ask';
  const STORAGE_KEY = 'qwav_qa_';

  // ── UI ──────────────────────────────────────────────────────────
  let panel = null, messages = [], isOpen = false;

  function createPanel() {
    if (panel) return;
    panel = document.createElement('div');
    panel.className = 'qa-panel';
    panel.setAttribute('role', 'dialog');
    panel.setAttribute('aria-label', 'Ask about this paper');
    panel.innerHTML = `
      <div class="qa-header">
        <span>Ask about this paper</span>
        <button class="qa-close" title="Close">×</button>
      </div>
      <div class="qa-messages"></div>
      <div class="qa-input-row">
        <textarea class="qa-input" placeholder="Ask a question about this paper…" rows="2"></textarea>
        <button class="qa-send" title="Send">→</button>
      </div>
    `;
    document.body.appendChild(panel);

    panel.querySelector('.qa-close').onclick = togglePanel;
    panel.querySelector('.qa-send').onclick = sendMessage;
    panel.querySelector('.qa-input').onkeydown = function(e) {
      if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); sendMessage(); }
    };
  }

  function createButton() {
    const btn = document.createElement('button');
    btn.className = 'qa-fab';
    btn.title = 'Ask about this paper';
    btn.innerHTML = '💬';
    btn.onclick = togglePanel;
    document.body.appendChild(btn);
  }

  function togglePanel() {
    isOpen = !isOpen;
    panel.classList.toggle('open', isOpen);
    if (isOpen) panel.querySelector('.qa-input').focus();
  }

  // ── Messages ────────────────────────────────────────────────────
  function addMessage(role, text) {
    messages.push({ role, text });
    const msgsEl = panel.querySelector('.qa-messages');
    const div = document.createElement('div');
    div.className = 'qa-msg qa-msg-' + role;
    div.textContent = text;
    msgsEl.appendChild(div);
    msgsEl.scrollTop = msgsEl.scrollHeight;
    saveHistory();
  }

  function saveHistory() {
    const slug = window.LIVING_PAPER_PAPER_ID || 'unknown';
    localStorage.setItem(STORAGE_KEY + slug, JSON.stringify(messages));
  }

  function loadHistory() {
    const slug = window.LIVING_PAPER_PAPER_ID || 'unknown';
    const saved = localStorage.getItem(STORAGE_KEY + slug);
    if (saved) {
      messages = JSON.parse(saved);
      const msgsEl = panel.querySelector('.qa-messages');
      msgsEl.innerHTML = '';
      messages.forEach(m => {
        const div = document.createElement('div');
        div.className = 'qa-msg qa-msg-' + m.role;
        div.textContent = m.text;
        msgsEl.appendChild(div);
      });
    }
  }

  // ── AI ──────────────────────────────────────────────────────────
  async function sendMessage() {
    const input = panel.querySelector('.qa-input');
    const q = input.value.trim();
    if (!q) return;
    input.value = '';
    input.disabled = true;
    panel.querySelector('.qa-send').disabled = true;

    addMessage('user', q);

    const thinking = addMessageMsg('assistant', 'Thinking…');

    try {
      const slug = window.LIVING_PAPER_PAPER_ID || 'unknown';
      const res = await fetch(AI_ENDPOINT, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question: q, paper: slug, history: messages.slice(0, -1) })
      });
      if (!res.ok) throw new Error('AI unavailable');
      const data = await res.json();
      thinking.textContent = data.answer || data.text || 'No answer available.';
    } catch (e) {
      thinking.textContent = 'Sorry, the AI service is unavailable right now.';
    }

    input.disabled = false;
    panel.querySelector('.qa-send').disabled = false;
    input.focus();
  }

  function addMessageMsg(role, text) {
    messages.push({ role, text });
    const msgsEl = panel.querySelector('.qa-messages');
    const div = document.createElement('div');
    div.className = 'qa-msg qa-msg-' + role;
    div.textContent = text;
    msgsEl.appendChild(div);
    msgsEl.scrollTop = msgsEl.scrollHeight;
    return div;
  }

  // ── Init ────────────────────────────────────────────────────────
  function init() {
    createPanel();
    createButton();
    loadHistory();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
