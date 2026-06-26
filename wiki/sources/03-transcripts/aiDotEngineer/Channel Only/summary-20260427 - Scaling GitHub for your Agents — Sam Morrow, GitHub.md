---
title: "Scaling GitHub for your Agents — Sam Morrow, GitHub"
type: source-summary
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260427 - Scaling GitHub for your Agents — Sam Morrow, GitHub.md"
author: "aiDotEngineer"
date: 2026-04-27
ingested: 2026-06-26
tags: [mcp, github, scaling, security, oauth, tool-design, context-engineering]
---

# Scaling GitHub for your Agents — Sam Morrow, GitHub

## Core Thesis

Sam Morrow, lead of GitHub's MCP server, presents the engineering challenges of building and scaling GitHub's remote MCP server from 100+ tools to a streamlined 40-tool default, achieving over 95% tool success rate and nearly 8 million tool calls per week through stateless architecture, context reduction strategies, and security hardening.

## Key Points

- **Tool Bloat Problem**: GitHub's MCP server initially grew to over 100 tools, causing agent confusion and context window exhaustion. LangChain research from February 2025 confirmed that more tools don't make better agents.
- **Tool Sets**: A grouping concept for related product tools, allowing users to pick which sets they want. However, most users never customized and used defaults.
- **Context Reduction**: Reduced initial context load by 49% by focusing tools on general cases, then further by grouping CRUD tools. Output token reduction of 75%+ on list operations by tailoring responses.
- **Tool Success Rate**: Over 95% success rate achieved by encoding agent intent into the tool surface, making multiple API calls server-side to reduce round trips.
- **Tool Evals**: Instead of micro-optimizing individual tool descriptions, tools are tested against each other to ensure they're called at the right times and not at the wrong times.
- **Security**: Plain-text access tokens are common and problematic. GitHub's remote server supports OAuth 2.1 with PKCE. Dynamic Client Registration was rejected due to unbounded growth and rate limiting concerns.
- **Step-Up OAuth**: Interactive scope escalation that doesn't fail tool calls; VS Code integration allows clean install with later upscoping.
- **Stateless Architecture**: New server instance created on every request with tools added at start based on configuration and policies. Redis used for session storage. No session affinity.
- **Insiders Mode**: Feature flag system for experimental features, currently hosting MCP Apps (human-in-the-loop editing of AI-generated issues).
- **Prompt Injection**: Invariant Labs published a prompt injection exfil attack targeting GitHub MCP, highlighting the "lethal trifecta" problem common to all agent setups.
- **Future Direction**: Server discovery will become automatic, tool use more compositional (bash/piping), thousands of tools will be normal, and OAuth/tool selection will become autonomous.

## Entities Mentioned

- [[SamMorrow]] — Lead of GitHub's MCP server
- [[GitHub]] — Platform with 11M+ Docker downloads of MCP server, 126 contributors
- [[InvariantLabs]] — Security research firm that published prompt injection attack on GitHub MCP
- [[Redis]] — Used for session storage in GitHub's stateless MCP architecture
- [[LangChain]] — Published research confirming more tools don't make better agents
- [[Anthropic]] — Developed tool search tool API for Claude Code
- [[OpenAI]] — Added similar tool search API
- [[CloudFlare]] — Developed code mode approach for MCP
- [[VisualStudioCode]] — Client supporting step-up OAuth with GitHub MCP
- [[ClaudeCode]] — Received tool search tool API from Anthropic

## Concepts Mentioned

- [[ToolSets]] — Grouping concept for related product tools to reduce context load
- [[DynamicToolSelection]] — Agents discover and enable tool sets in chunks
- [[ContextReduction]] — Strategies for reducing context window usage in MCP servers
- [[ToolEvals]] — Testing tools against each other to optimize call timing
- [[PKCE]] — Proof Key for Code Exchange, OAuth security mechanism
- [[StepUpOAuth]] — Interactive OAuth scope escalation without failing tool calls
- [[InsidersMode]] — Feature flag system for experimental MCP features
- [[MCPApps]] — Human-in-the-loop editing of AI-generated content via MCP
- [[AgentIntentEncoding]] — Encoding agent intent into tool surface to reduce failures
- [[StatelessMCPServer]] — Per-request server instances with no session affinity

## Related

- [[MCP]] — Model Context Protocol
- [[summary-20260112 - Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect]]
- [[summary-20260408 - Bending a Public MCP Server Without Breaking It — Nimrod Hauser, Baz]]
- [[summary-20260114 - Identity for AI Agents - Patrick Riley & Carlos Galan, Auth0]]
