---
title: "summary-build-production-ready-agent"
type: source
tags: [source, claude, managed-agents, workshop, transcript]
sources: [raw/03-transcripts/Claude/Code with Claude 2026 - London/14 - Build a production-ready agent with Claude Managed Agents.md]
last_updated: 2026-06-23
---

## Core Summary

A hands-on workshop for building with Claude Managed Agents. Covers the four building blocks: agent definition (template with system prompt, skills, tools, MCP servers, per-tool permissions), environment (sandbox config with network, packages, self-hosted options), session (ongoing conversation with event stream), and events (user, agent, session, span types). The workshop walks through building a deal desk product for M&A analysis, with a starter repo and solution code. Self-hosted sandboxes and MCP tunnels (for private server access) were announced at the event.

## Key Points

- **Four building blocks:** agent (template), environment (sandbox config), session (conversation), events (interaction stream).
- **Agent config:** system prompt, model, skills, tools (bash, web search, etc.), MCP servers, per-tool permission controls (auto-execute vs. require approval).
- **Environment:** network access control, pre-installed packages (npm, pip), self-hosted sandboxes (Cloudflare, Modal, Vercel, or custom fleet).
- **Session:** created with agent ID + environment ID; can include GitHub repos and preloaded files.
- **Event types:** user events (messages, images, interrupts, tool results, confirmations, outcome definitions), agent events (responses, tool calls, multi-agent coordination), session events (lifecycle, errors), span events (long operation tracking).
- **MCP tunnels:** secure tunnel to private MCP servers without exposing them to the internet.
- **Demo:** built a deal desk product for M&A analysis with a public starter repo.

## Related

- [[ClaudeManagedAgents]] — the platform
- [[summary-13 - How to get to production faster with Claude Managed Agents]] — companion talk
- [[ClaudeCode]] — the tool used for development
