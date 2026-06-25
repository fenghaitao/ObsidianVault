---
title: "FastMCP"
type: entity
tags: [mcp, python, framework, open-source]
sources: [raw/03-transcripts/Pydantic/Channel Only/20260319 - Open Source in the age of AI Panel – PyAI Conf 2026.md, raw/03-transcripts/Pydantic/Channel Only/20260330 - Pamela Fox Improving MCP tool schemas to increase agent reliability - PyAI Conf 2026.md]
last_updated: 2026-06-25
---

## Definition

FastMCP is a Python framework for building MCP (Model Context Protocol) servers, created by Jeremiah Lowin (CEO of Prefect). Simplifies MCP server creation with Python decorators and automatic JSON Schema generation from type annotations.

## Key Information

- Automatically converts Python function signatures to JSON Schema for LLM tool calling
- Had to inline JSON Schema enums because Opus models couldn't handle schema references
- Battle-hardened through community feedback across many models and clients
- Used by Cole Medin for his MCP server template and by Pamela Fox for her MCP schema research
- FastMCP servers can return images, binary data, and interactive apps — not just text

## Related

- [[JeremiahLowin]] — creator
- [[ModelContextProtocol]] — the protocol it implements
- [[Prefect]] — Jeremiah's company
- [[PamelaFox]] — used FastMCP in schema research
