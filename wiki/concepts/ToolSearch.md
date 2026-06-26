---
title: "Tool Search"
type: concept
tags: [mcp, tool-calling, context, optimization, client]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260419 - The Future of MCP — David Soria Parra, Anthropic.md"]
last_updated: 2026-06-26
---

## Definition
Tool Search is a mechanism for progressive discovery where the model uses a search tool to find relevant tools on demand, rather than having all tool descriptions loaded into the context window at once.

## Key Information
- Core implementation mechanism for progressive discovery in MCP clients
- Available in the Anthropic API and on competitors' APIs
- Can also be built manually: give the model a "tool loading tool" that it calls when it decides it needs a tool
- The model reasons: "Maybe I need a tool now. Let me look up what tools I need." Then loads them on demand
- Demonstrated in Claude Code with a "massive reduction in tool context usage" after implementation
- Contrasts with the naive approach of loading all tools into context at initialization

## Related
- [[summary-20260419 - The Future of MCP — David Soria Parra, Anthropic]] — source
- [[MCP]] — protocol
- [[ProgressiveDiscovery]] — the pattern this mechanism implements
- [[ClaudeCode]] — demonstrated the benefits
- [[DavidSoriaParra]] — presenter
