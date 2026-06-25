---
title: "summary-20250806 - Pydantic @ Google London July Meetup - All Talks"
type: source
tags: [source, pydantic, google, meetup, gemini, logfire, mcp]
sources: ["raw/03-transcripts/Pydantic/Channel Only/20250806 - Pydantic @ Google London July Meetup - All Talks.md"]
last_updated: 2026-06-25
---

## Core Summary

Pydantic's July 2025 meetup hosted at Google London. Three talks: Paige Bailey (Google DeepMind) on Gemini's multimodal capabilities, AI Studio, and Gemma open models; David Hewitt (Pydantic) on using Logfire to observe and optimize a Blue Sky firehose agent, including a Rust rewrite for performance; and Samuel Colvin on MCP advanced features including sampling with a PyPI/GitHub research agent demo. The event also announced Logfire availability on GCP Marketplace.

## Key Points

- Paige Bailey demos Gemini 2.5 Pro's native multimodality (image, video, audio, text I/O), AI Studio's "Build" feature for one-click app generation, and Gemma 3N outperforming Gemini 1.5 Pro
- David Hewitt builds a Blue Sky firehose agent with PydanticAI + Gemini 2.0 Flash, discovers Python filtering is the bottleneck, rewrites in Rust for significant speedup
- Samuel Colvin demos MCP sampling: a research agent using GitHub + PyPI MCP servers where the PyPI server uses sampling to generate BigQuery SQL
- Logfire distributed tracing shows cross-process traces between MCP client and server
- Logfire now purchasable through GCP Marketplace for easier enterprise procurement

## Related

- [[Gemini]] — Google's multimodal model family
- [[Logfire]] — Pydantic's observability platform
- [[PydanticAI]] — agent framework used in all demos
- [[ModelContextProtocol]] — advanced features including sampling
- [[GoogleDeepMind]] — Paige Bailey's team
