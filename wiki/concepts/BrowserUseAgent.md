---
title: "BrowserUseAgent"
type: concept
tags: [ai-agent, browser, automation, computer-use]
sources: ["raw/01-articles/claude/2025-08-25 - Piloting Claude in Chrome.md"]
last_updated: 2026-06-28
---

## Definition

A browser-using AI agent is an [[AIAgent]] that can perceive the state of a web browser (page content, DOM, URL, tab titles) and take actions within it (clicking buttons, filling forms, navigating pages) to complete tasks on behalf of users.

## Key Information

- Represents the next step beyond passive LLM assistants: the agent interacts directly with web-based software rather than relying on users to relay information.
- **Why inevitable**: so much work happens in browsers that giving AI the ability to see what users are looking at, click buttons, and fill forms makes it substantially more useful.
- Extends [[ComputerUse]] (where Claude could see the user's screen) by introducing a browser-level interface with direct access to DOM state, console errors, and structured page data.
- **Primary safety risk**: [[PromptInjection]] attacks, where malicious content on web pages hijacks the agent's instructions.
- **Browser-specific attack surfaces**: hidden DOM form fields invisible to humans, URL text, tab titles — elements only an AI agent can see.
- **Emerging ecosystem**: browser-using agents powered by frontier models from multiple companies were already emerging as of late 2025, making safety work urgent.
- [[ClaudeInChrome]] is Anthropic's implementation: a Chrome extension providing Claude with browser-use capabilities, piloted in a controlled rollout starting August 2025.
- **Safety architecture**: browser-using agents need layered defenses — system prompt hardening, site-category blocking, suspicious-pattern classifiers, and explicit permission controls.
- Anthropic positions real-world pilots (rather than only internal red-teaming) as necessary because novel attack patterns from actual user browsing cannot be replicated in controlled tests.

## Related

- [[summary-2025-08-25 - Piloting Claude in Chrome]] — source article
- [[ClaudeInChrome]] — Anthropic's browser-using agent implementation
- [[PromptInjection]] — the primary security risk for browser-using agents
- [[AIAgent]] — the parent category
- [[GoogleChrome]] — the browser platform used in Anthropic's pilot
- [[ToolUse]] — lower-level capability that browser use extends
- [[Anthropic]] — developed and piloted browser-use safety mitigations
