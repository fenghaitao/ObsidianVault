---
title: "PromptInjection"
type: concept
tags: [security, adversarial, agent-safety, llm]
sources: ["raw/01-articles/claude/2025-08-25 - Piloting Claude in Chrome.md"]
last_updated: 2026-06-28
---

## Definition

Prompt injection is an attack in which malicious content embedded in websites, emails, or documents contains hidden instructions that cause an AI agent to take harmful actions without the user's knowledge or consent — overriding the user's intended instructions with the attacker's.

## Key Information

- Analogous to phishing attacks on humans: just as people encounter phishing in their inboxes, browser-using AIs encounter prompt injection in web content.
- **Attack vectors in browser context**: hidden text on web pages, malicious form fields invisible in the rendered UI (present in the DOM), URL text, tab titles.
- **Example attack**: a malicious email claiming that, for security reasons, emails needed to be deleted — when Claude processed the inbox, it followed these instructions and deleted emails without user confirmation.
- **Consequences**: can cause AIs to delete files, steal data, or make financial transactions.
- **Empirical measurements from Anthropic's [[ClaudeInChrome]] pilot**:
  - 123 test cases, 29 attack scenarios.
  - Baseline autonomous mode attack success rate: **23.6%**.
  - After general mitigations: **11.2%** (meaningful improvement over prior Computer Use capability baseline).
  - Browser-specific challenge set baseline: **35.7%**.
  - After browser-specific mitigations: **0%** (on the four-attack challenge set).
- **Mitigation strategies**:
  - Hardened system prompts directing Claude on sensitive data and high-risk actions.
  - Blocking access to high-risk website categories (financial, adult, pirated content).
  - Classifiers to detect suspicious instruction patterns and unusual data access requests.
  - Permission controls giving users explicit control over what Claude can access and do.
- **Ongoing challenge**: novel attack patterns emerge continuously; controlled internal testing cannot replicate the full complexity of real-world browsing, which is why Anthropic ran a real-world pilot to collect authentic threat data.
- Applies to any [[BrowserUseAgent]] or agentic AI with access to external content — not unique to Claude.

## Related

- [[summary-2025-08-25 - Piloting Claude in Chrome]] — source article with detailed attack data
- [[ClaudeInChrome]] — the product used as the test bed for prompt injection research
- [[BrowserUseAgent]] — the agent category most exposed to prompt injection
- [[AIAgent]] — agents in general face prompt injection when processing external content
- [[Anthropic]] — conducted red-teaming and developed mitigations
- [[PromptEngineering]] — system prompt hardening is one mitigation layer
