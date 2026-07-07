---
title: "AgenticLoop"
type: concept
tags: [ai, agent, loop, automation]
sources: [raw/03-transcripts/Claude/Claude Code 101/03 - How Claude Code Works.md, raw/01-articles/claude/2025-09-29 - Building agents with the Claude Agent SDK.md, "raw/01-articles/claude/2026-06-10 - The evolution of agentic surfaces building with Claude Managed Agents.md"]
last_updated: 2026-06-28
---

## Definition

The agentic loop is the core operational pattern of AI agents: prompt intake, context gathering, model response (text or tool call), action execution, and result verification, repeating until the goal is achieved.

## Key Information

- Steps: (1) user enters a prompt, (2) agent gathers relevant context, (3) model returns text or a tool call, (4) agent executes the action, (5) agent verifies results against the original goal.
- If verification fails, the loop repeats from step 2 with the new information.
- The user can add context, interrupt, or steer the model at any point in the loop.
- This pattern is what distinguishes AI agents from simple chat-based assistants that only do text-in/text-out.
- Claude Code implements this loop in the terminal, with tools, context management, and configurable permissions.
- **Harness evolution**: The agentic loop's implementation (the harness) must evolve alongside model intelligence. A fix for one model generation can become overhead on the next. For example, [[ContextAnxiety]] on [[Claude4.5Sonnet|Claude Sonnet 4.5]] motivated context resets in the loop, but the behavior disappeared on [[Claude4.7Opus|Claude Opus 4.5]], turning the fix into pure overhead. This is a key argument for managed platforms like [[ClaudeManagedAgents]], where the harness evolves automatically with the model.

## Related

- [[summary-03 - How Claude Code Works]] — source summary
- [[ClaudeCode]] — the tool that implements the agentic loop
- [[AIAgent]] — the broader agent paradigm
- [[ContextWindow]] — the memory constraint within the loop
- [[analysis-agent-evolution-loop-to-self-learning]] — the evolution from the loop to self-learning agents
- [[AgenticSurfaces]] — the evolution of agent-building interfaces built on this loop
- [[ContextAnxiety]] — model behavior that illustrates why loop harnesses must evolve
- [[ClaudeManagedAgents]] — the managed platform that evolves the loop harness automatically
- [[summary-2026-06-10 - The evolution of agentic surfaces building with Claude Managed Agents]] — source article on harness evolution
