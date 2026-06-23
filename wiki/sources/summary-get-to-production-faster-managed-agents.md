---
title: "summary-get-to-production-faster-managed-agents"
type: source
tags: [source, claude, managed-agents, production, transcript]
sources: [raw/03-transcripts/Claude/Code with Claude 2026 - London/13 - How to get to production faster with Claude Managed Agents.md]
last_updated: 2026-06-23
---

## Core Summary

Michael and Harrison from Anthropic present Claude Managed Agents as the solution to infrastructure being the bottleneck for agent capabilities. The platform provides composable primitives: agent definitions (system prompt, model, skills, tools, permissions), sandboxed environments, session management with event streams, and observability. Key features: multi-agent orchestration (Claude spawns sub-agents with separate context windows), outcomes (rubric-based iterative improvement), self-hosted sandboxes, and MCP tunnels for private data access. Getting started: use the Claude API skill in Claude Code, the CLI, or copy-paste cookbooks.

## Key Points

- **Infrastructure as bottleneck:** model intelligence is no longer the limiting factor; infrastructure (reliability, scalability, security, latency) is.
- **Agent definition:** bundle of system prompt, model, skills, tools, permissions, and identity.
- **Environment:** sandboxed containers with configurable network allowlists and pre-installed packages. Self-hosted sandboxes (Cloudflare, Modal, Vercel) keep data in your perimeter.
- **Session event stream:** user events (messages, interrupts, tool results, confirmations), agent events (responses, tool calls, multi-agent coordination), session events (lifecycle, errors, outcome processing), span events (long-running operation tracking).
- **Multi-agent orchestration:** Claude spawns other agent threads with separate context windows, passing messages between specialized Claudes.
- **Outcomes:** define a rubric; Claude iterates against it until satisfied.
- **Getting started:** Claude API skill in Claude Code, CLI tool, or API cookbooks.

## Related

- [[ClaudeManagedAgents]] — the platform
- [[summary-build-production-ready-agent]] — hands-on workshop
- [[ClaudeCode]] — the tool with the Claude API skill
