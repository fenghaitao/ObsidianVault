---
title: "Matt Carey"
type: entity
tags: [person, cloudflare, code-mode, api]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260419 - Code Mode： Let the Code do the Talking - Sunil Pai, Cloudflare.md"]
last_updated: 2026-06-26
---

## Definition
Matt Carey is an engineer at Cloudflare who created the search+execute code mode approach for the Cloudflare API surface, reducing ~1.2M tokens of tool definitions to ~1,000 tokens by exposing just two tool calls that accept code strings.

## Key Information
- Works at Cloudflare alongside Sunil Pai
- Created a clever approach to the Cloudflare API surface (~2,600 endpoints) by exposing only two tool calls: search and execute
- Search accepts code as input, with the full OpenAPI JSON spec as the function input
- Execute provides functions to call against discovered API endpoints
- Achieved a 99.9% token reduction: from ~1.2M tokens to ~1,000 tokens
- Presented more details at a follow-up talk the next day at the same conference
- The approach enables wide API surfaces to be accessible to LLMs without overwhelming context windows

## Related
- [[summary-20260419 - Code Mode： Let the Code do the Talking - Sunil Pai, Cloudflare]] — source
- [[Cloudflare]] — employer
- [[SunilPai]] — colleague
- [[CodeMode]] — concept he pioneered at Cloudflare
