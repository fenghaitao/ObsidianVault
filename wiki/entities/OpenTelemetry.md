---
title: "OpenTelemetry"
type: entity
tags: [observability, standard, tracing, cncf]
sources: [raw/03-transcripts/Pydantic/Channel Only/20250415 - Pydantic, Jason Liu & MCP Meetup - April 8, 2025.md]
last_updated: 2026-06-25
---

## Definition

OpenTelemetry (OTel) is an open standard for observability — traces, metrics, and logs. Logfire is built on top of it. Samuel Colvin notes that OTel was designed for short-lived requests (~200-400ms) and doesn't stream trace data before completion, requiring Logfire to modify the standard for real-time AI trace viewing.

## Related

- [[Logfire]] — built on OpenTelemetry
- [[SamuelColvin]] — discusses OTel limitations for AI
