---
title: "ClaudeAgentSDK"
type: entity
tags: [tool, agent-framework, anthropic, claude-code]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic.md"]
last_updated: 2026-06-25
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

## Related
- [[summary-20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic]] — source
- [[ThariqShihipar]] — presenter
- [[Anthropic]] — creator
- [[ClaudeCode]] — foundation
- [[BashTool]] — core primitive
- [[SubAgents]] — key feature
- [[Hooks]] — verification mechanism
- [[Sandboxing]] — security layer
