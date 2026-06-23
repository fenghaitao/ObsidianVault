---
title: "AIAgent"
type: concept
tags: [ai, agent, llm, automation]
sources: [raw/03-transcripts/Claude/Claude Code 101/01 - What is Claude Code.md, raw/03-transcripts/Claude/Claude Code 101/03 - How Claude Code Works.md]
last_updated: 2026-06-23
---

## Definition

An AI agent is software that can interact with its environment and perform actions to complete a defined goal. The most basic implementation involves a large language model running in a real-time loop, with access to tools, external services, or other AI agents.

## Key Information

- AI agents operate in a loop: observe environment, decide action, execute, observe result, repeat.
- They have access to tools (file systems, APIs, web search), external services, and can coordinate with other agents.
- The agentic approach allows an LLM to work on problems that exceed its context window by strategically retrieving only relevant information.
- Claude Code is an example of an AI agent applied to software development.

## Related

- [[summary-01 - What is Claude Code]] — source summary
- [[summary-03 - How Claude Code Works]] — source on the agentic loop
- [[ClaudeCode]] — an AI agent for coding
- [[AgenticLoop]] — the core operational pattern
- [[ContextWindow]] — the memory constraint agents must work within
