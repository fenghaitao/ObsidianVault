---
title: "AIAgent"
type: concept
tags: [ai, agent, llm, automation]
sources: [raw/03-transcripts/Claude/Claude Code 101/01 - What is Claude Code.md, raw/03-transcripts/Claude/Claude Code 101/03 - How Claude Code Works.md, raw/01-articles/claude/2025-09-29 - Building agents with the Claude Agent SDK.md]
last_updated: 2026-06-28
---

## Definition

An AI agent is software that can interact with its environment and perform actions to complete a defined goal. The most basic implementation involves a large language model running in a real-time loop, with access to tools, external services, or other AI agents.

## Key Information

- AI agents operate in a loop: observe environment, decide action, execute, observe result, repeat.
- They have access to tools (file systems, APIs, web search), external services, and can coordinate with other agents.
- The agentic approach allows an LLM to work on problems that exceed its context window by strategically retrieving only relevant information.
- Claude Code is an example of an AI agent applied to software development.
- A key design principle from [[ClaudeAgentSDK]]: give an agent a computer (terminal + file system + tools) so it can work the way humans do, iterating until the goal is achieved.
- The three-phase agent loop: (1) **gather context** — read the environment via agentic file-system search or subagents; (2) **take action** — execute via tools, bash, code generation, or MCP integrations; (3) **verify work** — check output via rules-based feedback, visual feedback, or an LLM judge.
- Agents that can check and improve their own output are fundamentally more reliable: they catch mistakes before they compound and self-correct when they drift.
- [[ContextEngineering]] — the deliberate design of file/folder structure so the agent can selectively pull relevant information into its context — is a first-class agent design concern.

## Related

- [[summary-01 - What is Claude Code]] — source summary
- [[summary-03 - How Claude Code Works]] — source on the agentic loop
- [[ClaudeCode]] — an AI agent for coding
- [[AgenticLoop]] — the core operational pattern
- [[ContextWindow]] — the memory constraint agents must work within
- [[ToolUse]] — key capability enabling agent action execution
- [[summary-2024-05-30 - Claude can now use tools]] — tool use GA with enterprise agent examples
- [[ClaudeAgentSDK]] — Anthropic's SDK for building general-purpose agents
- [[ContextEngineering]] — treating file/folder structure as agent context design
- [[summary-2025-09-29 - Building agents with the Claude Agent SDK]] — agent design principles and the three-phase loop
