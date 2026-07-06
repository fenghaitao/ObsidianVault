---
title: "BoltNew"
type: entity
tags: [company, web-development, ai-coding, browser-ide]
sources: ["raw/01-articles/claude/2025-08-12 - Claude Sonnet 4 now supports 1M tokens of context.md", "raw/01-articles/claude/2026-02-09 - Behind the model launch What customers discovered testing Claude Opus 4.6 early.md"]
last_updated: 2026-07-04
---

## Definition

Bolt.new is a browser-based web development platform that integrates AI models — primarily [[Claude4Sonnet]] — to enable developers to build and deploy web applications directly from a web browser without local environment setup.

## Key Information

- Integrates [[Claude4Sonnet]] as its primary model for code generation workflows.
- CEO and Co-founder: Eric Simons.
- Claude Sonnet 4 "consistently outperforms other leading models in production" for their code generation workflows (per Eric Simons, 2025).
- The 1M token [[ContextWindow]] expansion for [[Claude4Sonnet]] allows Bolt.new developers to work on significantly larger projects while maintaining accuracy.
- Use case: real-world coding at production scale.

## Claude Opus 4.6 Early Access (February 2026)

Ran a dedicated Slack channel with deliberately unbiased separate impressions, combining an automated eval platform (build quality, bug fixing, codebase understanding, design aesthetics) with hands-on stress testing. Opus 4.6 diagnosed on the first try a waterfall-graph bug that had failed five-plus attempts with the previous model, identifying 8 parallel HubSpot API calls bypassing rate-limit protection via raw fetch calls. VP of Marketing Garrett Serviss: "The jump in reasoning depth is real."

## Related

- [[Claude4Sonnet]] — primary AI model powering Bolt.new's code generation
- [[ContextWindow]] — expanded to 1M tokens, enabling larger project support
- [[AIAgent]] — agentic coding paradigm used on the platform
- [[summary-2025-08-12 - Claude Sonnet 4 now supports 1M tokens of context]] — source article with customer spotlight
- [[Claude4.6Opus]] — model tested in early access
- [[summary-2026-02-09 - Behind the model launch What customers discovered testing Claude Opus 4.6 early]] — source article
