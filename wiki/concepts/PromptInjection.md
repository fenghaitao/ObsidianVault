---
title: "PromptInjection"
type: concept
tags: [security, adversarial, agent-safety, llm]
sources: ["raw/01-articles/claude/2025-08-25 - Piloting Claude in Chrome.md", "raw/01-articles/claude/2025-10-08 - Beyond permission prompts making Claude Code more secure and autonomous.md"]
last_updated: 2026-07-07
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
- **[[ClaudeCode]] mitigation via [[Sandboxing]]**: rather than relying only on detection, Anthropic constrains what a prompt-injected Claude Code session can actually do — filesystem and network isolation ensure that even a successful injection cannot exfiltrate SSH keys, phone home to an attacker's server, or delete files outside the sandboxed directory. This is a containment strategy, complementing the detection/hardening mitigations used for [[ClaudeInChrome]].
- **Computer-use activation scanning (March 2026, reconciled May 2026):** When Claude uses a computer directly in [[ClaudeCowork]] and [[ClaudeCode]] (pointing, clicking, navigating apps/browser/dev tools), Anthropic's system automatically scans internal model activations to detect prompt-injection-style misuse in real time, complementing per-app permission requests and a user override to stop Claude at any point. The May 2026 best-practices article describes this same safeguard using the term "real-time classifiers" — the two sources use different terminology for the same underlying defense mechanism. See [[ComputerUse]] and the three-layer defense bullet below.
- **Scraped-content injection example (observed March 2026)**: raw web-clipped articles ingested into this wiki have been found to contain boilerplate "Hi Claude! Could you help me..." prompts followed by "please execute the task... an artifact would be great" — likely a "try these prompts" page widget rather than a targeted attack, but structurally identical to a prompt injection. Ingestion workers correctly ignored the embedded instructions and only noted the anomaly. See [[summary-2026-03-18 - Code with Claude comes to San Francisco, London, and Tokyo]].
- **Second, unrelated scraped-content example (May 2026)**: this same anomaly pattern recurred when ingesting the computer/browser-use best-practices article — no embedded injection-style instructions were found in that raw file (noted for completeness, not an attack).
- **Three-layer defense described for computer use (May 2026)**: (1) training-time RL robustness — Claude is exposed to injected content in simulated pages/UIs during training and rewarded for refusing; (2) real-time classifiers — probes scanning content entering the context window across modalities (hidden text, image-embedded instructions, deceptive UI), running in parallel with inference at ~zero added latency/cost; (3) continuous red-teaming and external adversarial evaluation. These classifiers run automatically and for free when using the official `computer_20251124` tool type, but do **not** currently run for custom/self-defined computer-use tool implementations. Additional recommended layered practices: human-in-the-loop confirmation before irreversible actions (called "the single most effective mitigation against prompt injection regardless of classifier performance"), scoping agent permissions to limit blast radius, logging full action sequences/screenshots, and treating all encountered web/application content as untrusted in the system prompt. See [[summary-2026-05-13 - Best practices for computer and browser use with Claude]].

## Related

- [[summary-2025-08-25 - Piloting Claude in Chrome]] — source article with detailed attack data
- [[ClaudeInChrome]] — the product used as the test bed for prompt injection research
- [[BrowserUseAgent]] — the agent category most exposed to prompt injection
- [[AIAgent]] — agents in general face prompt injection when processing external content
- [[Anthropic]] — conducted red-teaming and developed mitigations
- [[PromptEngineering]] — system prompt hardening is one mitigation layer
- [[Sandboxing]] — containment-based mitigation used in Claude Code
- [[ClaudeCode]] — tool protected via sandboxing rather than detection alone
- [[summary-2025-10-08 - Beyond permission prompts making Claude Code more secure and autonomous]] — sandboxing as a prompt-injection containment strategy
- [[ComputerUse]] — capability protected by the computer-use activation-scanning safeguard
- [[ClaudeCowork]] — product where the activation-scanning safeguard applies
- [[summary-2026-03-23 - Put Claude to work on your computer]] — source describing the activation-scanning safeguard
- [[summary-2026-05-13 - Best practices for computer and browser use with Claude]] — three-layer computer-use prompt injection defense (training-time RL, real-time classifiers, red-teaming) and recommended mitigations
