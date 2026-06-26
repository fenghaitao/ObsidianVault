---
title: "LangChain"
type: entity
tags: [framework, llm, python, mcp]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260108 - DSPy： The End of Prompt Engineering - Kevin Madura, AlixPartners.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Bending a Public MCP Server Without Breaking It — Nimrod Hauser, Baz.md"]
last_updated: 2026-06-26
---

## Definition
LangChain is an LLM application framework used for building agentic workflows. It provides a `load_mcp_tools` method for importing MCP server tools into agent workflows, and is contrasted with DSPy as operating at a lower level of abstraction.

## Key Information
- Kevin Madura contrasts DSPy with LangChain, noting DSPy is less intrusive and allows focusing on what matters.
- With LangChain, developers write low-level constructs like choice messages, content strings, and string parsers.
- DSPy eliminates the need for manual string parsing and message construction, providing a more declarative approach.
- The comparison is not a criticism of LangChain but a distinction in paradigm: DSPy is structured differently.
- **MCP integration**: LangChain's `load_mcp_tools` method is the standard way to import MCP server tools into agent workflows, used in Baz's spec reviewer as the baseline vanilla approach before tool optimization.
- In the baseline approach, tools are loaded as-is without any curation, wrapping, or guardrails, which often leads to subpar agent performance.

## Related
- [[DSPy]] — framework compared to LangChain
- [[summary-20260108 - DSPy： The End of Prompt Engineering - Kevin Madura, AlixPartners]] — source
- [[summary-20260408 - Bending a Public MCP Server Without Breaking It — Nimrod Hauser, Baz]] — source (MCP tool loading)
- [[MCP]] — protocol for tool integration
- [[ThirdPartyToolOptimization]] — framework for improving tools loaded via LangChain
