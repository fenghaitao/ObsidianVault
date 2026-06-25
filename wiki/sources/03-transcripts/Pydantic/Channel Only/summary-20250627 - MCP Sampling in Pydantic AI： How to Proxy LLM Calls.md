---
title: "summary-20250627 - MCP Sampling in Pydantic AI： How to Proxy LLM Calls"
type: source
tags: [source, pydantic, mcp, sampling, tutorial]
sources: ["raw/03-transcripts/Pydantic/Channel Only/20250627 - MCP Sampling in Pydantic AI： How to Proxy LLM Calls.md"]
last_updated: 2026-06-25
---

## Core Summary

A short tutorial explaining MCP sampling in PydanticAI: the mechanism by which an MCP server can make LLM calls proxied through the MCP client, eliminating the need to provision each server with its own API keys and quotas. Demonstrates a generate-SVG MCP server that uses sampling to call GPT-4.1 for image generation.

## Key Points

- MCP sampling lets MCP servers call LLMs via the client instead of directly, centralizing API key management
- PydanticAI automatically enables sampling when running as an MCP client
- Distributed tracing in Logfire shows the full call chain: client -> server -> client (LLM call) -> server -> client
- The demo generates an SVG image of a robot in punk style using OpenAI 4.1 proxied through the MCP server

## Related

- [[ModelContextProtocol]] — the protocol enabling sampling
- [[PydanticAI]] — agent framework with built-in MCP sampling support
- [[Logfire]] — observability showing distributed tracing across client and server
