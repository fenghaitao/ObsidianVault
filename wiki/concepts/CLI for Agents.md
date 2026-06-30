---
title: "CLI for Agents"
type: concept
tags: [agents, cli, tool-calling, bash, shell]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260425 - MCP = Mega Context Problem - Matt Carey.md"]
last_updated: 2026-06-29
---

## Definition
CLI for Agents is a progressive discovery approach where agents use shell access to interact with command-line interfaces via `--help` introspection and command parsing, rather than having all tool descriptions loaded into the context window.

## Key Information
- One of three approaches to progressive discovery presented by Matt Carey (alongside tool search and code mode)
- Agent uses shell access to call `--help` on CLI commands, parse the output, and determine which commands and parameters to use
- Used by OpenClaw and widely popular among agent frameworks
- Works well but has a key limitation: requires shell access, which is not always available (e.g., Cloud Code)
- Example: agent calls `wrangler --help`, reads commands, then calls `wrangler d1 --help` to introspect database commands
- Contrasts with MCP tool calling where all tools are loaded into context upfront
- Related to the Bash as Universal Adapter pattern: bash provides access to thousands of tools through one interface

## Related
- [[summary-20260425 - MCP = Mega Context Problem - Matt Carey]] — source
- [[ProgressiveDiscovery]] — the broader pattern this implements
- [[BashAsUniversalAdapter]] — related pattern for agent-tool interaction
- [[OpenClaw]] — agent framework using CLI-based interaction
- [[ToolSearch]] — alternative progressive discovery approach
- [[CodeMode]] — alternative progressive discovery approach
