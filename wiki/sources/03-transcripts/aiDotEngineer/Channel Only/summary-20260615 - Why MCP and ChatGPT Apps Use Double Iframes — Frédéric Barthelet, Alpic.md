---
title: "summary-20260615 - Why MCP and ChatGPT Apps Use Double Iframes — Frédéric Barthelet, Alpic"
type: source
tags: [source, transcript, mcp, security, iframes, chatgpt]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260615 - Why MCP and ChatGPT Apps Use Double Iframes — Frédéric Barthelet, Alpic.md"]
last_updated: 2026-06-30
---

## Core Summary

Frederic Barthelet from Alpic (MCP hosting) deep-dives into why ChatGPT and MCP apps use double iframes. The outer iframe provides origin isolation (Content Security Policy, no cookie/localStorage access), while the inner iframe renders the app content. This architecture solves the tension between running untrusted third-party UI and maintaining browser security.

## Key Points

- MCP/ChatGPT apps render third-party UI as "views" — HTML snippets displayed after tool calls.
- Double iframe architecture: outer iframe for origin isolation + inner iframe for app content. Prevents script execution within ChatGPT's origin.
- Single srcdoc iframe fails: shares origin/CSP with host, blocking scripts and exposing localStorage/cookies.
- Views are discovered ahead of time via tool list calls, can be cached or served on-demand.
- Content Security Policy: frame-src and script-src directives are critical for app isolation.
- Alpic: MCP hosting company, co-founded by Frederic.

## Related

- [[FredericBarthelet]] — speaker, CTO Alpic
- [[Alpic]] — MCP hosting company
- [[MCP Apps]] — MCP app extension
- [[ContentSecurityPolicy]] — browser security
- [[IframeSandboxing]] — isolation technique
- [[ChatGPT]] — app platform
