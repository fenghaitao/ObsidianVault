---
title: "FastMCP"
type: entity
tags: [tool, mcp, python, framework, open-source]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260112 - Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect.md"]
last_updated: 2026-06-26
---

## Definition
FastMCP is the de facto standard Python framework for building MCP (Model Context Protocol) servers, created by Jeremiah Lowin and maintained by Prefect Technologies.

## Key Information
- Introduced almost exactly a year after MCP itself, within days of MCP's announcement
- David from Anthropic called Lowin to say FastMCP was how people should build servers
- A version was incorporated into the official Anthropic MCP SDK
- Later repositioned as the high-level interface to the MCP ecosystem, while the SDK focuses on low-level primitives
- The "fastmcp" vocabulary is being removed from the low-level SDK to avoid confusion
- Downloaded ~1.5 million times in a single day
- One of its most popular features is automatic REST API to MCP conversion, which Lowin now advises against using in production
- Supports middleware hooks for overridable tool listing behavior
- Handles automatic string-to-object deserialization as a workaround for Claude Desktop's limitations with structured arguments
- Plans to add an experiments/optimize flag to the CLI for features like code mode support
- Lowin describes being "overwhelmed" and "back in an open source maintenance seat" due to its popularity

## Related
- [[summary-20260112 - Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect]] — source
- [[JeremiahLowin]] — creator
- [[PrefectTechnologies]] — maintaining company
- [[MCP]] — protocol it implements
- [[ClaudeDesktop]] — client with compatibility issues
