---
title: "Cloudflare Workers"
type: entity
tags: [platform, serverless, cloudflare, edge-computing]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260419 - Code Mode： Let the Code do the Talking - Sunil Pai, Cloudflare.md"]
last_updated: 2026-06-26
---

## Definition
Cloudflare Workers is a serverless computing platform created by Kenton at Cloudflare. It provides V8 isolates for fast, secure code execution and is used as the sandbox environment for Cloudflare's code mode and agent execution.

## Key Information
- Created by Kenton at Cloudflare
- Uses V8 isolates for execution — extremely fast startup (~5ms) and ~10 years of security hardening
- Dynamic Workers provide the execution environment for code mode: agents generate code that runs in Workers
- The platform enables capability-based security: start with zero capabilities, grant explicitly
- Default recommendation: no outgoing fetches, only explicitly exposed APIs
- Provides full observability into code execution for audit and debugging
- Part of Cloudflare's DNA of caring about security

## Related
- [[summary-20260419 - Code Mode： Let the Code do the Talking - Sunil Pai, Cloudflare]] — source
- [[Cloudflare]] — parent company
- [[Kenton]] — creator
- [[V8Isolates]] — execution environment
- [[CodeMode]] — paradigm enabled by Workers
