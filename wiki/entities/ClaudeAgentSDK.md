---
title: "ClaudeAgentSDK"
type: entity
tags: [tool, agent-framework, anthropic, claude-code]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260518 - Anthropic Workshop： Build Agents That Run for Hours — Ash Prabaker & Andrew Wilson.md"]
last_updated: 2026-06-30
---

## Definition
The Claude Agent SDK is Anthropic's opinionated agent framework built on top of Claude Code. It packages battle-tested agent infrastructure — tools, bash, file system, skills, sub-agents, hooks, compacting, memory, web search — so developers can focus on domain-specific agent design rather than rebuilding harness components.

## Key Information
- Built on Claude Code because users organically started using Claude Code for non-coding tasks, revealing the bash tool and file system as universal agent primitives
- Strongly opinionated: the bash tool is the most powerful agent tool, agents should build their own context, code generation works for non-coding tasks
- Includes sub-agents with best-in-class bash support, handling race conditions and process isolation
- Ships with hooks for deterministic verification and context insertion at event boundaries
- Includes a to-do tool that agents use to maintain and check off tasks
- Supports structured outputs for workflow-like use cases
- Has a plugin marketplace (accessible via /plugins in Claude Code) for skill discovery
- Used for software agents (reliability, security, incident triaging, bug finding), site/dashboard builders, MS Office agents, legal, finance, healthcare
- Architecture: every agent runs in a container with its own file system and bash access; very different from traditional multi-tenant web app architecture
- Sandboxing support for network requests and file system operations outside the workspace
- Laurie Voss used the Claude Agent SDK in his eval workshop to build a financial analysis agent with two sub-agents (research + write report), chosen for its simplicity — "a very very simple framework for building agents... it doesn't have a whole bunch of ceremony"
- The SDK maintains conversation context across turns, enabling multi-step agents where research output feeds into report writing
- In the workshop, the agent used Claude Haiku with one tool (web search) and accept_edits permission mode

## Related
- [[summary-20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic]] — source
- [[summary-20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize]] — source
- [[ThariqShihipar]] — presenter
- [[Anthropic]] — creator
- [[ClaudeCode]] — foundation
- [[BashTool]] — core primitive
- [[SubAgents]] — key feature
- [[Hooks]] — verification mechanism
- [[Sandboxing]] — security layer
- [[LaurieVoss]] — used SDK in eval workshop
- [[Phoenix]] — observability platform used with the SDK
