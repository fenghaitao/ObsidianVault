---
title: "summary-2026-06-10 - The evolution of agentic surfaces building with Claude Managed Agents"
type: source
tags: [source, claude-blog, managed-agents, agent-architecture]
sources: ["raw/01-articles/claude/2026-06-10 - The evolution of agentic surfaces building with Claude Managed Agents.md"]
last_updated: 2026-07-07
---

## Core Summary

Claude Managed Agents is Anthropic's composable API suite for building and deploying production-grade agents at scale. The article traces the evolution of agentic surfaces from simple API calls to Claude Code's harness, the Claude Agent SDK, and finally Managed Agents — a platform that decouples the agent "brain" (harness/orchestration) from the "hands" (sandbox execution), solving production challenges around hosting, session management, filesystem isolation, credential security, and observability. Key architectural innovations include parallel container spin-up for 60–90% faster time-to-first-token, vault-based credential management with envelope encryption, append-only session event logs enabling resumable runs and native observability, and the flexibility of Anthropic-managed or self-hosted sandboxes. Customer examples from Notion, Rakuten, Sentry, Asana, and Atlassian demonstrate production adoption across industries, with Notion reporting a prototype that turned roughly twelve hours of work into twenty minutes.

## Key Points

- Infrastructure, not prompt quality, is what separates prototypes from production agents — teams burn cycles on security, state management, permissioning, and harness tuning.
- The agentic surface evolved: API (tokens in/out) → Claude Code harness → Claude Agent SDK (same machinery, programmable) → Claude Managed Agents (fully managed infrastructure).
- Managed Agents decouples the brain (harness calling Claude) from the hands (sandbox where code executes), connected by an append-only session event log.
- Credentials are kept out of the sandbox via Vaults with envelope encryption; a proxy fetches and decrypts tokens only on demand.
- Time-to-first-token improved ~60% at p50 and >90% at p95 because Claude begins reasoning while the environment spins up in parallel.
- Sessions persist full event history, sandbox state, and outputs server-side — runs can pause, resume, and be traced step by step.
- Dreaming is a scheduled process that reviews past sessions and memory stores, extracts patterns, and curates memories so agents improve over time.
- Three primary resources: agents (configuration), environments (execution context), and sessions (an agent paired with an environment in an isolated sandbox instance).
- Self-hosted sandboxes and MCP tunnels allow teams to control where code executes and how Anthropic reaches private MCP servers.
- The harness must evolve alongside model intelligence — a fix for context anxiety on Sonnet 4.5 became overhead on Opus 4.5.
- Written by Gagan Bhat and Isabella He (Applied AI team) with contributions from Hema Thanki, Jess Yan, and Molly Vorwerck.

## Related

- [[ClaudeManagedAgents]] — the product this article describes
- [[ClaudeAgentSDK]] — the predecessor SDK that provides Claude Code's harness machinery
- [[ClaudeCode]] — the agentic coding tool whose harness informed the SDK and Managed Agents
- [[AgenticSurfaces]] — the evolution of interfaces for building and deploying agents
- [[ContextAnxiety]] — model behavior pattern that motivated harness adaptation
- [[Sandboxing]] — the execution isolation pattern Managed Agents decouples from orchestration
- [[AgenticMemory]] — memory and dreaming features built on persistent session logs
- [[AnthropicConsole]] — the Claude Developer Console with native visual timeline view
- [[ModelContextProtocol]] — MCP tunnels connect agents to private MCP servers
