---
title: "Tool, Skill, or Subagent? Decomposing an Agent That Outgrew Its Prompt"
type: source
tags: [agent-architecture, tools, skills, subagents, evals, managed-agents]
sources: [raw/03-transcripts/Claude/Code with Claude 2026 - London Day 2/02 - Tool, skill, or subagent Decomposing an agent that outgrew its prompt.md]
last_updated: 2026-06-23
---

## Core Summary

Will from Anthropic's Applied AI team presents a workshop on decomposing an inventory management agent (Stock Pilot) that accumulated complexity over time, growing to a 400-line system prompt with 12 tools and 3 sub-agent wrappers. The session demonstrates migrating from a custom Messages API harness to Claude Managed Agents, then systematically simplifying: replacing most tools with Claude Code primitives (bash, read, write, code execution), moving business logic from system prompt into skills for progressive disclosure, and keeping only one sub-agent (forecasting) using CMA's native callable agents. The eval score improved from 62% to 92% with dramatically reduced token usage and cost.

## Key Points

- **The accumulation problem:** Agents that work well initially get more requirements bolted on, leading to bloated system prompts, tool proliferation, and eval regression.
- **Skills for progressive disclosure:** Move business logic and policies from the system prompt into skills that Claude pulls into context only when needed. System prompt reduced from 400 to 15 lines.
- **Start with human-like primitives:** Give agents the same tools humans use (file system, code execution, web search, to-do list) before building custom tools. Claude Managed Agents includes these Claude Code primitives by default.
- **Code execution over data loading:** Instead of loading entire CSVs into context, give Claude the ability to write and run Python scripts. This dramatically reduces token usage (200K → much lower).
- **When to use sub-agents:** (1) Parallelization — throw many Claude instances at a big problem. (2) Fresh perspective — separate writer from reviewer, or isolate specialized tasks like forecasting from the main conversation.
- **Callable agents in CMA:** Native sub-agent capability with built-in observability, avoiding communication breakdown between orchestrator and sub-agents.
- **MCP strategy:** Start with Claude Code primitives, then custom local tools, and only publish as MCP server when multiple agents/clients need the same governed toolset. Code execution via CLIs/APIs can often replace MCP.
- **Hill climbing on evals:** Establish baseline → triage failures → modify architecture → rerun → iterate. Evals must evolve as product capability expands.

## Related

- [[ClaudeManagedAgents]] — the platform for deploying the decomposed agent
- [[ClaudeCodeSkills]] — skills as the progressive disclosure mechanism
- [[ClaudeCodeSubagents]] — sub-agent patterns and design
- [[ClaudeCode]] — the primitives (bash, read, write) reused in Managed Agents
- [[ModelContextProtocol]] — when to use MCP vs. code execution
