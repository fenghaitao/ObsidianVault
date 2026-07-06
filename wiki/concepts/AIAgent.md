---
title: "AIAgent"
type: concept
tags: [ai, agent, llm, automation]
sources: [raw/03-transcripts/Claude/Claude Code 101/01 - What is Claude Code.md, raw/03-transcripts/Claude/Claude Code 101/03 - How Claude Code Works.md, raw/01-articles/claude/2025-09-29 - Building agents with the Claude Agent SDK.md, raw/01-articles/claude/2025-12-09 - How enterprises are building AI agents in 2026.md]
last_updated: 2026-07-04
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
- **Tool design principle** (April 2026): shape an agent's tools to its actual, demonstrated abilities rather than assumed ones — learned by reading its outputs and experimenting, not designed upfront in the abstract; a deliberately high bar for adding new tools keeps the option-space navigable for the model. See [[summary-2026-04-10 - Seeing like an agent how we design tools in Claude Code]].
- **Anthropic Economic Index (September 2025)**: 40% of U.S. employees report using AI at work, up from 20% in 2023. Anthropic frames the strategic question for enterprises as whether this produces lasting competitive advantage or plateaus into incremental gains — arguing the differentiator is embedding agentic AI into how employees work, how processes run, and what products are possible, and encoding institutional knowledge into compounding systems. See [[summary-2026-04-30 - Building AI agents for the enterprise]].

## 2026 State of AI Agents (December 2025 survey)

Anthropic's survey of 500+ technical leaders (with research firm Material) found enterprise agent adoption shifting from simple automation to complex, cross-functional workflows:

- 57% of organizations deploy agents for multi-stage workflows (16% cross-functional across teams); 81% plan more complex use cases in 2026.
- ~90% use AI to assist development, 86% deploy agents for production code — coding remains the leading adoption category, with data analysis/reporting (60%) and internal process automation (48%) close behind.
- 80% of organizations already report measurable economic ROI from agent investments.
- Top 2026 scaling challenges: integration with existing systems (46%), data access/quality (42%), change management (39%).
- Customer examples: [[ThomsonReuters]] (CoCounsel), [[ESentire|eSentire]], [[Doctolib]], and [[LOreal|L'Oréal]] — see [[summary-2025-12-09 - How enterprises are building AI agents in 2026]].

## Related

- [[summary-01 - What is Claude Code]] — source summary
- [[summary-03 - How Claude Code Works]] — source on the agentic loop
- [[ClaudeCode]] — an AI agent for coding
- [[AgenticLoop]] — the core operational pattern
- [[summary-2026-04-30 - Building AI agents for the enterprise]] — Anthropic Economic Index enterprise-adoption stat and "three pillars" transformation framing
- [[ClaudeCowork]] — product positioned as the vehicle for scaling agentic transformation to every team
- [[ContextWindow]] — the memory constraint agents must work within
- [[ToolUse]] — key capability enabling agent action execution
- [[summary-2024-05-30 - Claude can now use tools]] — tool use GA with enterprise agent examples
- [[ClaudeAgentSDK]] — Anthropic's SDK for building general-purpose agents
- [[ContextEngineering]] — treating file/folder structure as agent context design
- [[summary-2025-09-29 - Building agents with the Claude Agent SDK]] — agent design principles and the three-phase loop
- [[ThomsonReuters]] — cited enterprise-adoption customer
- [[ESentire]] — cited enterprise-adoption customer
- [[Doctolib]] — cited enterprise-adoption customer
- [[LOreal]] — cited enterprise-adoption customer
- [[summary-2025-12-09 - How enterprises are building AI agents in 2026]] — 2026 State of AI Agents survey
- [[summary-2026-04-10 - Seeing like an agent how we design tools in Claude Code]] — "see like an agent" tool-design framing
