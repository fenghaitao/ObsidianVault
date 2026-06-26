---
title: "ToolCuration"
type: concept
tags: [agentic-tools, context-engineering, mcp]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Bending a Public MCP Server Without Breaking It — Nimrod Hauser, Baz.md"]
last_updated: 2026-06-26
---

## Definition
Tool curation is the practice of filtering out unnecessary or irrelevant tools from a third-party MCP server or tool library to reduce context window load and prevent agent confusion when choosing among tools.

## Key Information
- Third-party MCP servers often provide many tools (e.g., Playwright provides 21 tools), but not all are needed for every use case.
- Removing irrelevant tools reduces the number of choices the agent must consider, simplifying decision-making.
- Curation reduces context window usage, leaving more room for other information.
- In Baz's spec reviewer example, tools like browser resize, drag, and code execution were excluded because the spec reviewer doesn't need them.
- The practice is implemented via simple list comprehension filtering: get all tools, exclude the ones not needed, return the rest.
- Curation is the first and simplest of the five third-party tool optimization practices.

## Related
- [[summary-20260408 - Bending a Public MCP Server Without Breaking It — Nimrod Hauser, Baz]] — source
- [[ThirdPartyToolOptimization]] — parent framework
- [[ToolWrapping]] — complementary practice (often combined with curation)
- [[Context Management]] — broader context window management
- [[MCP]] — protocol providing the tools
