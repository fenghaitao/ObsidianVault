---
title: "summary-20260513 - Sebastián Ramirez What's New in FastAPI - PyAI Conf 2026"
type: source
tags: [source, pydantic, pyai-conf, fastapi, streaming, sse]
sources: ["raw/03-transcripts/Pydantic/Channel Only/20260513 - Sebastián Ramirez What's New in FastAPI - PyAI Conf 2026.md"]
last_updated: 2026-06-25
---

## Core Summary

Sebastián Ramírez (FastAPI creator) presents new FastAPI features for AI workloads: high-performance JSON serialization via Pydantic's Rust core (just add return type annotations), streaming responses with `yield` (JSON lines, raw bytes, Server-Sent Events), and a bundled FastAPI skill for coding agents. Also announces the VS Code/Cursor extension (2,000+ users) and FastAPI Cloud. The SSE support is particularly relevant for LLM token streaming.

## Key Points

- Return type annotations now trigger Pydantic's Rust-based JSON serialization for major performance gains
- `yield` in path operations enables streaming: JSON lines (with Pydantic serialization), raw bytes, or Server-Sent Events
- SSE support: `EventSourceResponse` class handles ping, ID, retry, comments per the SSE standard
- FastAPI bundles an official skill file updated with each release so coding agents know about new features
- VS Code extension: endpoint explorer, code lens for tests, navigation between tests and endpoints
- FastAPI Cloud: deployment platform with waitlist priority for PyAI Conf attendees
- 12 million downloads/day, 95K GitHub stars, used by OpenAI, Netflix, Uber, CERN

## Related

- [[FastAPI]] — the web framework
- [[SebastianRamirez]] — creator
- [[Pydantic]] — serialization engine
- [[ServerSentEvents]] — streaming protocol
- [[FastAPICloud]] — deployment platform
