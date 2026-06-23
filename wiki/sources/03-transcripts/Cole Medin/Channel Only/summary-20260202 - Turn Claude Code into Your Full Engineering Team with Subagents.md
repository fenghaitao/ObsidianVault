---
title: "summary-20260202 - Turn Claude Code into Your Full Engineering Team with Subagents"
type: source
tags: [source, original-material, agent-harness, subagents, claude-agent-sdk, arcade]
sources: ["raw/03-transcripts/Cole Medin/Channel Only/20260202 - Turn Claude Code into Your Full Engineering Team with Subagents.md"]
last_updated: 2026-06-20
---

## Core Summary

[[ColeMedin]] extends [[Anthropic]]'s open-source long-running-task harness into a **full "AI engineer"** by giving it a *tool belt* — [[SubAgent]]s that operate Linear (tasks), GitHub (repo/PRs/commits), and Slack (progress updates) — so the agent works *where human engineers work*, not just in code. Built on the [[ClaudeAgentSDK]] (defining agents/MCP/sub-agents in code rather than a `.claude/` folder) and connected to services via [[Arcade]]'s MCP gateway, the harness takes an **AppSpec** (a PRD), scaffolds the project via an initializer agent, then loops coding sessions with fresh context until every Linear task is done. He closes by re-pitching [[Archon]] as the future tool for building custom harnesses — "the [[N8N]] for AI coding."

## Key Points

- **Why a harness**: even with strong [[ContextEngineering]], a too-large request makes a coding agent "fall on its face" — context is the precious resource. A harness is a wrapper of persistence + progress tracking that strings together multiple sessions (state, git workflow), extending how much work fits.
- **The gap it fills**: a real engineer also communicates (Slack), manages tasks (Linear/Jira), and maintains the repo (GitHub). To be a true AI engineer the harness needs those in its tool belt — hence service sub-agents.
- **Built on Anthropic's harness + [[ClaudeAgentSDK]]**: uses Anthropic's open-sourced long-running-task harness and its recommended JSON task-list format. Agents, MCP servers, and sub-agents are defined **in code** via the SDK (not `.claude/`), and it runs on the user's existing Claude Code subscription (cost-effective).
- **[[Arcade]] for connectivity**: one MCP gateway exposes Linear + GitHub + Slack (91 tools) with **agent authorization** (walks users through OAuth), so a team can share the harness without sharing raw API keys. Uses MCP **tool discovery** so 91 tool defs aren't dumped into context.
- **Flow**: an **AppSpec/PRD** is the initial single source of truth → **initializer agent** scaffolds the project, creates the Linear project + issues (becoming the new source of truth, replacing a local `claude_progress.md`), and inits the GitHub repo → **coding loop** runs each session in a fresh context window: get bearings (read Linear), regression-test (one agent often breaks another's work), pick next feature, implement, validate (Playwright MCP), commit, update Linear + handoff, repeat until done.
- **[[SubAgent]] context isolation**: dedicated Linear/GitHub/Slack sub-agents keep the orchestrator's context window lean; each can run a different model (Haiku/Sonnet/Opus) per cost/speed needs — configured per-agent in the SDK.
- **Dynamic behavior**: usually one task per session, but the agent may batch simple tasks; for a trivial Pomodoro-timer demo it built everything in the initializer session. A complex "research dashboard" app generated 44 Linear tasks across many sessions.
- **Future of AI coding**: off-the-shelf harnesses are only a starting point — the real power is **custom** harnesses fit to your own workflow, but nothing makes that easy yet. Cole is pivoting [[Archon]] from a task-management+RAG "command center" into **"the N8N for AI coding"** — a tool to define and orchestrate your own harnesses. Rationale: task management is now built into coding agents, and RAG matters less for coding since agents look up docs well.

## Related

- [[AgentHarness]] — the pattern being extended into a full AI engineer
- [[ClaudeAgentSDK]] — the SDK powering the harness
- [[Arcade]] — MCP gateway for Linear/GitHub/Slack with agent authorization
- [[SubAgent]] — service agents for context isolation
- [[Archon]] — re-pitched as the "N8N for AI coding" harness builder
- [[Anthropic]] — author of the base open-source harness
- [[N8N]] — the analogy for orchestrating custom workflows
- [[ContextEngineering]] — what each session still relies on internally
