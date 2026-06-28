---
title: "GoogleChrome"
type: entity
tags: [browser, google, platform]
sources: ["raw/01-articles/claude/2025-08-25 - Piloting Claude in Chrome.md"]
last_updated: 2026-06-28
---

## Definition

Google Chrome is a web browser developed by Google and the platform chosen by [[Anthropic]] for its first browser-using AI agent pilot ([[ClaudeInChrome]]).

## Key Information

- The dominant desktop web browser by market share, making it the natural first target for browser-using AI agents.
- Supports a Chrome Web Store ecosystem for distributing browser extensions.
- [[ClaudeInChrome]] is distributed as an extension installable from the Chrome Web Store.
- Chrome's extension model provides sandboxed access to web page content (DOM, URL, tab state) — the interface Claude uses to perceive and interact with websites.
- Browser-specific attack surfaces exploited in [[PromptInjection]] testing include: hidden DOM form fields, URL text, and tab titles.

## Related

- [[summary-2025-08-25 - Piloting Claude in Chrome]] — source article
- [[ClaudeInChrome]] — the Anthropic Chrome extension
- [[Anthropic]] — built the first Claude browser extension for Chrome
- [[PromptInjection]] — security risk exposed by browser extension access to web content
- [[BrowserUseAgent]] — the broader category of AI agents operating within browsers
