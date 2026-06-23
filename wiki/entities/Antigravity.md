---
title: "Antigravity"
type: entity
tags: [tool, google, agentic-ide, gemini, frontend]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260604 - Claude Plans, Gemini Designs： The Workflow to Build BEAUTIFUL Frontends.md"
last_updated: 2026-06-21
---

## Definition

Antigravity is Google's agentic IDE, released alongside Gemini 3 (referenced in [[ColeMedin]]'s 2025 recap as effectively the product of Google absorbing Windsurf). Powered by Gemini models, [[ColeMedin]] highlights it as exceptional at **one-shot front-end / UI generation** — producing interfaces that look handcrafted, beating Claude Code / Lovable / Bolt on first-pass design.

## Key Information

- **Gemini-powered UI strength**: Cole's testing with Gemini 3.5 Flash in Antigravity produced one-shot UIs "way better than what you'd usually make" with other tools — a key motivation for the [[CrossProviderWorkflow]] that lets Gemini own UI design.
- **Workflow role** (`summary-claude-plans-gemini-designs`): an alternative to [[Pi]] for running the **UI design** step; you can hand it a skill file (read-and-execute) plus the plan path even though it isn't skill-native like [[ClaudeCode]].
- **Lineage**: emerged from Google's 2025 push (Gemini 3 + the Windsurf team/features); see `summary-ai-exploded-in-2025`.

## Related

- [[CrossProviderWorkflow]] — Antigravity runs the Gemini UI step
- [[Pi]] — the other host for Gemini-powered design
- [[AICodingAssistant]] — Antigravity's category (agentic IDE)
- [[ColeMedin]] — evaluator
- [[summary-20260604 - Claude Plans, Gemini Designs： The Workflow to Build BEAUTIFUL Frontends]] — primary source
- [[summary-20260101 - AI Exploded in 2025 - Here’s Everything That Happened]] — Antigravity's launch context
