---
title: "Ship Your First Managed Agent"
type: source
tags: [managed-agents, workshop, SRE, incident-response, agent-architecture]
sources: [raw/03-transcripts/Claude/Code with Claude 2026 - London Day 2/01 - Ship your first Managed Agent.md]
last_updated: 2026-06-23
---

## Core Summary

Isabella He from Anthropic's Applied AI team presents a hands-on workshop for building a site reliability engineering (SRE) incident response agent using Claude Managed Agents. The session covers the evolution from raw Messages API to Agent SDK to Managed Agents, explaining the key architectural decision to decouple the agent loop (brain) from tool execution (hands) for security, latency, and reliability. Participants build a working agent that debugs incidents by accessing metrics, deployments, and diffs, with streaming events, session persistence, and local tool execution.

## Key Points

- **Evolution path:** Messages API (raw model access) → Agent SDK (harness for Claude Code) → Claude Managed Agents (fully managed infrastructure handling scaling, sandboxing, observability).
- **Brain-hands decoupling:** Agent loop runs server-side on Anthropic infrastructure; tool execution happens in separate sandboxed environments. This enables credential security (vaults), 90%+ reduction in time-to-first-token (P95), and container failure recovery without restarting the agent loop.
- **Three core resources:** Agent endpoint (persona, model, MCP servers, skills), Environments (sandboxed execution containers), Sessions (binding agents to environments with event streaming).
- **Events not tokens:** Sessions work in units of events (user messages, tool calls, agent responses) rather than request-response tokens, enabling streaming, observability, and session resumption.
- **Session persistence:** All conversation state maintained server-side; hard refresh or laptop close doesn't lose progress.
- **Session states:** Idle, running, rescheduling, terminated — enabling webhook-driven resumption and external event handling.
- **Beyond basics:** Skills, sub-agents (multi-agent), memory, dreaming, outcomes (rubric-based task completion), vaults (encrypted credential storage), webhooks, fine-grained permissions.
- **Bring your own compute:** Newly released ability to run agent tool execution in customer's own infrastructure, not just Anthropic's managed environment.

## Related

- [[ClaudeManagedAgents]] — the platform used in this workshop
- [[ClaudeCode]] — the agent tool whose primitives are reused in Managed Agents
- [[AgenticMemory]] — memory and dreaming for self-improving agents
- [[ClaudeCodeSkills]] — skills as a composable agent capability
