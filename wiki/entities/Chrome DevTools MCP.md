---
title: "Chrome DevTools MCP"
type: entity
tags: [mcp, tool, google, chrome, debugging, agents, browser-automation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260605 - Building Agent Interfaces： Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google.md"]
last_updated: 2026-06-30
---

## Definition
Chrome DevTools MCP (also called Chrome DevTools for Agents) is a purpose-built MCP server that enables AI coding agents to debug, performance-profile, and audit web pages through Chrome. It is designed specifically for agents rather than humans, returning semantic summaries instead of raw trace data.

## Key Information
- Purpose-built version of Chrome DevTools for AI agents, not a wrapper around the human UI
- Works with any MCP-capable agent harness: Gemini CLI, Claude Code, Codex, OpenClaw, and others
- Originally attempted to feed raw trace files (50K+ lines of JSON) to agents — blew through context windows
- Now returns markdown and semantic summaries with key performance metrics (LCP, INP, CLS)
- Evolved from one monolithic "debug webpage" tool into 25 decomposed tools
- Features tool categorization (hiding niche tools behind CLI parameters) and Slim Mode (3 tools only)
- Offers both MCP server and CLI interface — CLI enables token-efficient command chaining
- Autoconnect feature lets humans share their screen with agents for collaborative debugging
- Designed with intentional friction: autoconnect requires human consent every time per Simon Willison's Lethal Trifecta
- Includes a troubleshooting skill (diagnostic playbook) for setup issues
- QR code available at talks pointing to installation and configuration instructions
- Product Manager: Michael Hablich

## Related
- [[summary-20260605 - Building Agent Interfaces： Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google]] — source
- [[Chrome DevTools]] — human-oriented version
- [[Michael Hablich]] — Product Manager
- [[Google]] — company behind it
- [[MCP]] — protocol it implements
- [[Slim Mode]] — minimal tool mode
- [[CLI For Agents]] — alternative interface
- [[Semantic Summaries]] — key technique
- [[Diagnostic Playbooks]] — troubleshooting skill
- [[Trust Boundaries For Agents]] — security design principle
- [[Browser Agent Security Tiers]] — security model
