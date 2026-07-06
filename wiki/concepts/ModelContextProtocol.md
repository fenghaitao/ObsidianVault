---
title: "ModelContextProtocol"
type: concept
tags: [mcp, protocol, tools, integration, claude-code]
sources: [raw/03-transcripts/Claude/Claude Code 101/08 - MCP in Claude Code.md, raw/01-articles/claude/2025-06-18 - Remote MCP support in Claude Code.md, raw/01-articles/claude/2025-05-22 - New capabilities for building agents on the Anthropic API.md, raw/01-articles/claude/2025-10-31 - What is Model Context Protocol Connect AI to your world.md, "raw/01-articles/claude/2025-12-08 - How Anthropic&#39;s legal team cut review times from days to hours with Claude.md", raw/01-articles/claude/2025-12-18 - Skills for organizations, partners, the ecosystem.md, raw/01-articles/claude/2025-12-19 - Extending Claude’s capabilities with skills and MCP servers.md, raw/01-articles/claude/2026-01-22 - Building agents with Skills Equipping agents for specialized work.md, raw/01-articles/claude/2026-01-26 - Your favorite work tools are now interactive connectors inside Claude.md, raw/01-articles/claude/2026-01-29 - A complete guide to building skills for Claude.md, raw/01-articles/claude/2026-04-22 - Building agents that reach production systems with MCP.md]
last_updated: 2026-07-04
---

## Definition

Model Context Protocol (MCP) is an open standard that enables AI agents like Claude Code to connect to external tools and data sources. It allows Claude to automatically determine when to use connected services to better answer queries.

## Key Information

- **Server types:** HTTP (remote services, hosted by provider) and STDIO (local processes on the user's machine).
- **Remote MCP servers:** MCP now supports remote servers hosted across web and desktop apps, enabling seamless integration with cloud services and web-based tools.
- **Scoping:** local (current project only), user (all projects), project (`.mcp.json` in version control, shared with team).
- **Management:** use `claude mcp add` to add servers, `/mcp` command to view, enable, or disable within a session.
- **Context cost:** MCP tools add persistent tool definitions to the context window even when idle. Disable unused servers.
- **10% threshold:** if MCP tools exceed 10% of context, Claude auto-switches to tool search mode (on-demand discovery, less reliable).
- **Alternatives:** CLI equivalents (e.g., `gh`, `aws`) are more context-efficient. Skills load only a name/description into context and the full content on demand.
- Hundreds of connectors available at claude.com/connectors.

## Origin (October 2025 retrospective)

- Created at [[Anthropic]] by David Soria Parra and Justin Spahr-Summers. David's frustration with constantly copying code between Claude Desktop and his IDE led him to recognize a classic **M×N problem** — M applications each needing custom integrations with N tools — and pitch a protocol to solve it.
- Modeled on the Language Server Protocol; open-sourced in November 2024 with Anthropic's support so the whole AI ecosystem could adopt it.
- Framed as **"USB-C for LLMs"**: before MCP, every application (Google Drive, Slack, Figma) needed its own custom integration code with every AI assistant; MCP provides one universal connector format instead.

## Client/Server Model

- **MCP Clients**: built by AI agents/chatbots (e.g., Claude) to connect to any MCP Server.
- **MCP Servers**: built by companies/developers to expose their tools and data to any MCP Client — one server implementation works with every compatible AI assistant, rather than one integration per assistant.
- Because MCP is open, anyone can build a Client or a Server; the open-source **MCP Registry** (modelcontextprotocol.io) hosts community-built servers beyond Claude's own directory.
- In [[Claude.ai]], MCP Servers are surfaced to end users as **Connectors** — each takes seconds to configure (e.g., Canva, Notion, Linear, Figma).

## Integrations

[[Integrations]] bring MCP to [[Claude.ai]] users through a curated set of pre-built remote MCP servers. As of May 2025, integrations include major platforms like Atlassian (Jira, Confluence), Zapier, Cloudflare, Intercom, Asana, Square, Sentry, PayPal, Linear, and Plaid. Users can connect any number of integrations to enhance Claude's capabilities with deep context about their work and enable automated actions across platforms.

## Anthropic API MCP Connector

The [[Anthropic]] API offers the [[MCPConnector|MCP connector]] (beta, May 2025), which automatically manages remote MCP server connections without requiring custom client code:
- Automatic connection management to remote MCP servers
- Tool discovery and agentic reasoning about tool selection
- Automatic error handling and authentication
- Available remote servers from [[Zapier]], [[Asana]], and hundreds of others
- Works with [[Claude4Opus]] and [[Claude4Sonnet]]

## Open Standard for Skills (December 2025)

Anthropic published **Agent Skills** at agentskills.io as an open standard, drawing on the same portability philosophy as MCP: the same skill should work across Claude and other AI platforms, not just Anthropic's. See [[ClaudeCodeSkills]].

## MCP Apps: Interactive Connectors (January 2026)

**MCP Apps** is an official MCP extension letting any MCP server deliver a rich, interactive UI directly inside a conversation — building Asana project timelines, drafting/sending formatted Slack messages, or visualizing Figma diagrams without switching tabs — in any MCP-supporting AI product, not just Claude. Available on Claude mobile, web, desktop (Free through Enterprise plans) and [[ClaudeCowork|Claude Cowork]]; Salesforce (via Agentforce 360) is planned. Extends MCP beyond data/action connectivity into first-class in-conversation UI.

## MCP vs. Skills: Connectivity vs. Expertise (December 2025)

MCP provides connectivity — secure, standardized access to external systems (GitHub, Salesforce, Notion, internal APIs). [[ClaudeCodeSkills|Skills]] provide the domain expertise and workflow logic that turn that raw access into a reliable, team-specific outcome. Rule of thumb: "If you're explaining *how* to do something, that's a skill. If you need Claude to *access* something, that's MCP." The two compose freely — a single skill can orchestrate multiple MCP servers, and a single MCP server can support many skills — but MCP-level instructions should stay generic (query syntax, API formats) while skill-level instructions handle process-specific sequencing and output formatting, to avoid the two contradicting each other.

## Three Paths to Connect Agents to External Systems (April 2026)

Anthropic frames MCP as one of three approaches for connecting agents to external systems, each suited to a different scale:

- **Direct API calls**: the agent issues HTTP requests (via a code-execution sandbox or generic function-calling tool). Simplest starting point for one agent/one service, but with no common layer, it becomes an **M×N integration problem** at scale — each agent–service pair needs its own auth handling, tool descriptions, and edge cases.
- **CLI**: the agent runs a command-line tool in a shell. Fast and lightweight, works well in local environments and sandboxed containers, but hits hard limits reaching mobile, web, or cloud-hosted platforms with no exposed container; auth relies on the CLI's own credential file.
- **MCP**: provides the common layer as a protocol — a server exposes a system's capabilities with auth, discovery, and semantics standardized, so one remote server reaches any compatible client (Claude, ChatGPT, Cursor, VS Code, and more) in any deployment environment. Requires more upfront investment but the integration becomes portable.

Mature integrations tend to ship all three (API as foundation, CLI for local-first environments, MCP for cloud agents), but as production agents increasingly run in the cloud, MCP is framed as **"the compounding layer"**: as more clients adopt the spec and more extensions land in it, existing MCP servers get more capable without the server builder shipping anything new. MCP SDK downloads grew from ~100M/month at the start of 2026 to 300M+/month by April 2026.

## MCP for Internal Structured Search in Large Codebases (May 2026)

Among large-codebase Claude Code deployments, the most sophisticated teams built MCP servers exposing structured search as a tool Claude can call directly — one of several harness extension points (alongside [[CLAUDE-md|CLAUDE.md]], [[ClaudeCodeHooks|hooks]], [[ClaudeCodeSkills|skills]], and [[ClaudeCodePlugins|plugins]]) that determine how well Claude Code performs on a given codebase, independent of the underlying model. Other teams connect Claude to internal documentation, ticketing systems, or analytics platforms via MCP for the same reason. See [[summary-2026-05-14 - How Claude Code works in large codebases Best practices and where to start]].

## Building Effective MCP Servers (April 2026)

Anthropic's directory has 200+ MCP servers used by millions daily; observed design patterns for reliability:

- **Build remote servers for maximum reach** — only remote servers run across web, mobile, and cloud-hosted agents.
- **Group tools around intent, not endpoints** — fewer, well-described tools outperform exhaustive API mirrors (a single `create_issue_from_thread` beats chaining `get_thread` + `parse_messages` + `create_issue` + `link_attachment`).
- **Design for code orchestration when the surface is large** — for services with hundreds of operations (Cloudflare, AWS, Kubernetes), expose a thin tool surface that accepts code instead: the agent writes a short script, the server runs it in a sandbox against the API, and only the result returns. [[Cloudflare]]'s MCP server is the reference example — two tools (search, execute) cover ~2,500 endpoints in ~1K tokens.
- **Ship rich semantics**: **MCP Apps** (the first official MCP protocol extension) lets a tool return an interactive UI (chart, form, dashboard) rendered inline in chat — servers using it see meaningfully higher adoption/retention. **Elicitation** lets a server pause mid-call to request user input: **Form mode** sends a schema for a native form (missing parameters, destructive-action confirmation, disambiguation — broadly supported); **URL mode** hands the user to a browser for OAuth, payment, or any credential that shouldn't transit the MCP client (currently supported in Claude Code, more clients in progress).
- **Lean on standardized auth**: the latest MCP spec supports **CIMD** (Client ID Metadata Documents) for OAuth client registration — Anthropic's recommended approach, giving a fast first-time auth flow and fewer re-auth prompts; supported in MCP SDKs, Claude.ai, and Claude Code. For runtime token handling, **Vaults** in [[ClaudeManagedAgents]] register a user's OAuth tokens once and let the platform inject/refresh credentials per session by vault ID — no custom secret store needed.

## Context-Efficient MCP Clients (April 2026)

Patterns for MCP client builders to manage context via progressive disclosure:

- **Tool search**: defers loading all tool definitions into context, letting the agent search the catalog at runtime and pull in only relevant tools — cuts tool-definition tokens by 85%+ in Anthropic's testing while maintaining selection accuracy. See [[ToolUse]].
- **Programmatic tool calling**: processes tool results inside a code-execution sandbox rather than returning them raw to the model, so the agent can loop/filter/aggregate across calls with only final output reaching context — roughly 37% token reduction on complex multi-step workflows in Anthropic's testing. See [[CodeExecutionTool]].
- The two patterns compose across multiple servers: leaner context, fewer round-trips, faster responses.

## Pairing MCP Servers with Skills (April 2026)

Two patterns for combining MCP (access) with [[ClaudeCodeSkills|Skills]] (procedural knowledge), extending the December 2025 "connectivity vs. expertise" framing:

- **Bundle skills and MCP servers as a plugin** — the best way to unify multiple context providers with minimal friction. Example: Cowork's data plugin bundles 10 skills and 8 MCP servers for Snowflake, Databricks, BigQuery, Hex, and more. See [[ClaudeCodePlugins]].
- **Distribute a skill from an MCP server** — providers increasingly publish a skill alongside their MCP server so the agent gets both raw capability and an opinionated playbook; [[Canva]], [[Notion]], and [[Sentry]] already do this in Claude's connector directory. The MCP community is developing a protocol-level extension for delivering skills directly from servers, to make this pairing portable across every client.

## MCP Tunnels (May 2026)

**MCP tunnels** (research preview) let agents reach MCP servers inside a customer's private network without exposing them to the public internet. A lightweight gateway deployed by the customer makes a single outbound connection to the tunnel service — no inbound firewall rules, no public endpoints — with traffic encrypted end to end, turning internal databases, private APIs, knowledge bases, and ticketing systems into tools an agent can call. MCP tunnels is supported in both [[ClaudeManagedAgents]] and the Messages API, and is administered from workspace settings in the Claude Console by organization admins. It complements self-hosted sandboxes (see [[Sandboxing]]) as a second mechanism for keeping agent-reachable systems inside the enterprise perimeter. See [[summary-2026-05-19 - New in Claude Managed Agents self-hosted sandboxes and MCP tunnels]].

## Related

- [[Integrations]] — MCP integrations available on Claude.ai
- [[Research]] — uses MCP integrations for searching custom data sources
- [[ToolIntegration]] — Pattern of connecting Claude to external tools via MCP
- [[MCPConnector]] — Anthropic API feature for automatic MCP server management
- [[summary-08 - MCP in Claude Code]] — source summary on Claude Code MCP
- [[summary-2025-06-18 - Remote MCP support in Claude Code]] — remote MCP servers announcement
- [[summary-2025-07-14 - Discover tools that work with Claude]] — tool directory and connectors announcement
- [[summary-2025-05-22 - New capabilities for building agents on the Anthropic API]] — announcement of API MCP connector
- [[ClaudeCode]] — supports MCP for local and remote servers
- [[ContextWindow]] — the memory constraint MCP tools consume
- [[Sentry]] — error tracking platform with MCP integration
- [[Linear]] — project management platform with MCP integration
- [[Asana]] — work management platform with remote MCP server
- [[Zapier]] — workflow automation with remote MCP server
- [[Claude4Opus]] — supports API MCP connector
- [[Claude4Sonnet]] — supports API MCP connector
- [[summary-2025-10-31 - What is Model Context Protocol Connect AI to your world]] — origin story, USB-C framing, and Connectors explainer
- [[summary-2025-12-08 - How Anthropic&#39;s legal team cut review times from days to hours with Claude]] — MCP used to connect Claude to Google Drive, JIRA, Slack, and Calendar
- [[summary-2025-12-18 - Skills for organizations, partners, the ecosystem]] — Agent Skills published as an open standard alongside MCP's precedent
- [[summary-2025-12-19 - Extending Claude’s capabilities with skills and MCP servers]] — MCP-vs-Skills framing, hardware-store analogy, worked examples
- [[summary-2026-01-22 - Building agents with Skills Equipping agents for specialized work]] — MCP as one of four layers in the emerging general-agent architecture
- [[Integrations]] — the connector feature MCP Apps enriches with interactive UI
- [[ClaudeCowork]] — product now supporting MCP Apps
- [[summary-2026-01-26 - Your favorite work tools are now interactive connectors inside Claude]] — MCP Apps announcement
- [[summary-2026-01-29 - A complete guide to building skills for Claude]] — comprehensive Skills-building guide with an MCP + Skills section
- [[Cloudflare]] — reference example for the code-orchestration MCP server design pattern
- [[summary-2026-04-22 - Building agents that reach production systems with MCP]] — three-paths framing, server/client design patterns, and skills+MCP pairing
- [[summary-2026-05-14 - How Claude Code works in large codebases Best practices and where to start]] — MCP as a large-codebase harness extension point for internal structured search
- [[summary-2026-05-19 - New in Claude Managed Agents self-hosted sandboxes and MCP tunnels]] — MCP tunnels launch, connecting agents to private-network MCP servers
- [[ClaudeManagedAgents]] — product supporting MCP tunnels alongside self-hosted sandboxes
