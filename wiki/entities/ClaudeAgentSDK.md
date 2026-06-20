---
title: "ClaudeAgentSDK"
type: entity
tags: [tool, anthropic, sdk, agent-harness, claude, subagents]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260202 - Turn Claude Code into Your Full Engineering Team with Subagents.md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260212 - I Built a Safer OpenClaw Alternative Using Claude Code.md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260326 - Everything You Thought About Building AI Agents is Wrong.md"
last_updated: 2026-06-20
---

## Definition

The Claude Agent SDK is [[Anthropic]]'s programmatic toolkit for building agentic systems on top of Claude in code — the same engine that powers [[ClaudeCode]], exposed for custom orchestration. [[ColeMedin]] uses it as the wrapper for his [[AgentHarness]] experiments: instead of configuring agents, MCP servers, and [[SubAgent]]s through a `.claude/` folder, you define them in Python and run on your existing Claude Code subscription (cost-effective).

## Key Information

- **Code-defined configuration**: system prompts, sub-agent definitions, MCP servers, and per-agent models are all declared in code (e.g. loaded from markdown prompt files), not the `.claude/` directory used by interactive Claude Code.
- **Sub-agent definitions**: each sub-agent gets a description (how the orchestrator knows when to call it), a prompt loaded from a file, an allowed-tools list (e.g. the [[Arcade]] MCP tools), and a model (`haiku` / `sonnet` / `opus`) — making cost/speed tunable per agent.
- **MCP wiring**: connect MCP servers (Arcade gateway, Playwright MCP, etc.) in the SDK definition, similar to configuring Claude Desktop.
- **Foundation for harnesses**: Anthropic open-sourced a long-running-task harness (initializer + looped coding agent, JSON task-list format) built on the SDK at the end of 2025; Cole builds his "full AI engineer" on top of it.
- **Heartbeat / proactive agents**: Cole also uses the SDK to run [[ClaudeCode]] from Python scripts on a schedule (every ~30 min) — the "heartbeat" of his [[SecondBrain]] that checks memory/email/calendar/tasks and notifies him. Crucially, running the SDK/Claude Code directly is within Anthropic's ToS, unlike using a subscription with [[OpenClaw]].
- **Platform caveat**: sub-agents "don't work that well" on native Windows with the SDK — Cole runs it under **WSL** (or Mac/Linux).

### Building non-coding agents on it ("batteries included")

Per `summary-sdk-vs-framework-agents`, the SDK is increasingly used to build *non-coding* agents because it's batteries-included: managed **conversation history** (no DB needed), built-in tools + **file search** (often no RAG pipeline), [[SubAgent]]s, [[ClaudeSkills]], MCP, hooks, and permissions — often a whole agent in one TypeScript file (Cole's Second-Brain heartbeat).

**Three limitations** (vs a framework like [[PydanticAI]]):
1. **Slower** — reasoning overhead from all the built-in machinery.
2. **Token-heavy / bloated** — comes with the convenience.
3. **Less deterministic** — you don't control exactly how it operates.

Plus the **cost/ToS constraint**: subscriptions are licensed only when *you alone* use the agent; multi-user production needs an API key (expensive). So the SDK fits **single-user, latency-tolerant** use; production/scale favors a framework (see [[AgentSDKvsFramework]]).

## Related

- [[Anthropic]] — author
- [[ClaudeCode]] — the interactive agent built on the same engine; shares the subscription
- [[AgentHarness]] — what the SDK is used to build
- [[SubAgent]] — defined in code via the SDK
- [[Arcade]] — MCP gateway wired into the SDK definition
- [[ColeMedin]] — uses it for harness experiments
- [[SecondBrain]] — the heartbeat runs on the SDK
- [[OpenClaw]] — contrast: direct SDK use is ToS-compliant where subscription+OpenClaw is not
- [[AgentSDKvsFramework]] — when to choose this SDK vs a framework
- [[PydanticAI]] — the framework alternative for production scale
- [[summary-full-engineering-team-subagents]] — primary source
- [[summary-safer-openclaw-alternative]] — heartbeat / proactive use
- [[summary-sdk-vs-framework-agents]] — SDK strengths, limitations, and the decision
