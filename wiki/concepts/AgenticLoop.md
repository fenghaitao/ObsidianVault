---
title: "AgenticLoop"
type: concept
tags: [ai, agent, loop, automation]
sources: [raw/03-transcripts/Claude/Claude Code 101/03 - How Claude Code Works.md]
last_updated: 2026-06-23
---

## Definition

The agentic loop is the core operational pattern of AI agents: prompt intake, context gathering, model response (text or tool call), action execution, and result verification, repeating until the goal is achieved.

## Key Information

- Steps: (1) user enters a prompt, (2) agent gathers relevant context, (3) model returns text or a tool call, (4) agent executes the action, (5) agent verifies results against the original goal.
- If verification fails, the loop repeats from step 2 with the new information.
- The user can add context, interrupt, or steer the model at any point in the loop.
- This pattern is what distinguishes AI agents from simple chat-based assistants that only do text-in/text-out.
- Claude Code implements this loop in the terminal, with tools, context management, and configurable permissions.

## Related

- [[summary-how-claude-code-works]] — source summary
- [[ClaudeCode]] — the tool that implements the agentic loop
- [[AIAgent]] — the broader agent paradigm
- [[ContextWindow]] — the memory constraint within the loop
