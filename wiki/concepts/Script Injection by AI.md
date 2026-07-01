---
title: "Script Injection by AI"
type: concept
tags: [ai, security, desktop, automation, code-generation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260501 - Agents on the Canvas in tldraw — Steve Ruiz, tldraw.md"]
last_updated: 2026-06-29
---

## Definition
Script Injection by AI is the capability and willingness of AI models to modify running applications by injecting JavaScript or other code directly into them. AI models show no hesitation in performing script injection, happily modifying minified code bundles and documenting their approach with patterns like "this is how you should do this."

## Key Information
- **AI's willingness**: AI models have "no qualms at all" about script injection — they document themselves with "this is how you should do this" patterns
- **Enthusiasm**: AI seems to "love" getting its claws into websites and applications, showing eagerness to modify running code
- **Minified code modification**: AI will happily go through minified code bundles and "rip and tear" to make changes
- **Example**: A tldraw team member asked Claude to remove podcasts from Spotify's desktop app — Claude went through the minified bundle code and made the change
- **Canvas interactivity**: In tldraw's desktop app, AI can inject scripts to make static canvas drawings interactive (hover effects, click handlers) even though tldraw doesn't have built-in interactivity primitives
- **Safety concern**: This is a "terrible idea" for web apps but acceptable for offline, file-based desktop apps where the blast radius is contained
- **Unpredictable results**: Script injection can produce surprising, strange, and sometimes broken results (blinking elements, wrong implementations)
- **Motivates local-first**: The desire to enable script injection is a key motivation for local-first, file-over-app architecture

## Related
- [[summary-20260501 - Agents on the Canvas in tldraw — Steve Ruiz, tldraw]] — source
- [[FileOverApp]] — the philosophy that enables safe script injection
- [[Sandboxing]] — the security model for containing script injection risk
- [[Computer Use]] — related capability for desktop automation
- [[Untrusted Code Execution]] — the broader category
- [[Spotify]] — example target of AI script injection
