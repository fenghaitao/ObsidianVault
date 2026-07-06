---
title: "summary-2026-04-22 - Building agents that reach production systems with MCP"
type: source
tags: [source, original-material]
sources: ["raw/01-articles/claude/2026-04-22 - Building agents that reach production systems with MCP.md"]
last_updated: 2026-07-04
---

## Core Summary

Anthropic lays out three ways to connect agents to external systems — direct API calls, CLIs, and MCP — and argues production agents increasingly converge on MCP because it provides a standardized common layer (auth, discovery, semantics) that a single remote server can expose to any compatible client, whereas direct API calls create an M×N integration problem and CLIs can't reach cloud/mobile/web agents. MCP SDK downloads have grown from 100M to 300M/month in a year, underpinning products like Claude Cowork, Claude Managed Agents, and Claude Code channels. The post then gives concrete design patterns: build remote (not just local) servers; group tools around intent rather than mirroring API endpoints one-to-one; expose a thin code-execution surface for very large APIs (Cloudflare's ~2,500-endpoint server via two tools is the reference example); use MCP Apps and Elicitation (form/URL mode) for richer, interactive tool responses; and standardize auth via CIMD plus Claude Managed Agents' Vaults for token storage/refresh. On the client side, it recommends Tool Search (on-demand tool loading, 85%+ token reduction) and Programmatic Tool Calling (processing results in a code sandbox, ~37% token reduction) for context efficiency. Finally, it frames Skills and MCP as complementary — MCP for access, Skills for the procedural know-how — recommending either bundling both into a plugin or having MCP servers distribute a companion skill (as Canva, Notion, and Sentry already do), with a community MCP extension in progress to make skill-from-server delivery a protocol-level standard.

## Key Points

- Three integration paths: direct API calls (flexible but M×N bespoke-integration problem at scale), CLI (fast/lightweight but confined to environments with a filesystem/shell, auth via local credential files), MCP (standardized common layer — auth, discovery, semantics — reachable by any compatible client in any deployment environment).
- Production agents increasingly run in the cloud and need to reach cloud-hosted systems, which is where MCP's remote-server model matters most.
- Adoption stat: MCP SDK downloads grew from ~100M/month (start of the year) to 300M+/month; protocol underpins Claude Cowork, Claude Managed Agents, and channels in Claude Code.
- Server design patterns: build remote servers for maximum reach; group tools around intent, not endpoints (a single `create_issue_from_thread` beats four chained primitive calls); for very large APIs (Cloudflare, AWS, Kubernetes-scale), expose a thin code-execution surface instead of an intent-grouped toolset — Cloudflare's MCP server covers ~2,500 endpoints with two tools (search, execute) in ~1K tokens.
- Rich semantics: MCP Apps (first official protocol extension) lets a tool return an interactive UI (chart, form, dashboard) rendered inline; Elicitation lets a server pause mid-call to request input — Form mode for structured input (broadly supported), URL mode for browser-based OAuth/payment/credential flows (currently Claude Code, more clients coming).
- Auth: CIMD (Client ID Metadata Documents), from the latest MCP spec, is Anthropic's recommended approach for OAuth client registration — fast first-time auth, fewer re-auth prompts; supported in MCP SDKs, Claude.ai, and Claude Code. Vaults in Claude Managed Agents store and refresh a user's OAuth tokens server-side, referenced by ID at session creation, so agents don't need a custom secret store.
- Client-side context efficiency: Tool Search defers loading tool definitions until needed (85%+ reduction in tool-definition tokens in Anthropic's testing); Programmatic Tool Calling processes tool results inside a code-execution sandbox so only final output reaches context (~37% token reduction on complex multi-step workflows in Anthropic's testing). The two compose across multiple servers.
- Skills + MCP pairing: two patterns — (1) bundle skills and MCP servers together as a plugin (example: Cowork's data plugin ships 10 skills + 8 MCP servers for Snowflake, Databricks, BigQuery, Hex, etc.); (2) distribute a skill directly from an MCP server so the client gets both capability and playbook together — Canva, Notion, and Sentry already do this via Claude's connector directory; an MCP community extension for protocol-level skill delivery is in progress.
- Closing framing: mature integrations end up shipping all three paths (API as foundation, CLI for local-first, MCP for cloud agents), but MCP is described as "the compounding layer" — every client/extension that adopts the spec makes existing MCP servers more capable without additional work from the server builder.
- Anomaly: the raw file contains scraped page-widget artifacts mid-article (a stray italicized "*servers*" fragment before a heading, and a malformed sentence/link around "MCP standardizes how AI agents ([ clients]...)...The server securely exposes..."), consistent with website-scraping boilerplate rather than genuine content or a prompt-injection attempt. No instructions were embedded or followed.

## Related

- [[ModelContextProtocol]] — the concept page this article substantially extends (three connection paths, server design patterns, CIMD/Vaults auth, tool search/programmatic tool calling, skills pairing)
- [[Anthropic]] — publisher of the article and operator of the MCP server directory
- [[ClaudeCodeSkills]] — the skills side of the MCP-and-skills pairing patterns described
- [[ClaudeCodePlugins]] — the plugin-bundling mechanism referenced for combining skills and MCP servers
- [[ClaudeManagedAgents]] — home of the Vaults feature for MCP OAuth credential storage
- [[ClaudeCowork]] — cited as a product underpinned by MCP, and source of the data-plugin example
- [[CodeExecutionTool]] — sandboxed execution model underlying programmatic tool calling and code-orchestration MCP servers
- [[ToolIntegration]] — the general pattern of connecting Claude to external tools, contrasted here with direct API/CLI approaches
- [[Sentry]] — cited as an MCP server that also distributes a companion skill
- [[Notion]] — cited as an MCP server that also distributes a companion skill
- [[Canva]] — cited as an MCP server that also distributes a companion skill
