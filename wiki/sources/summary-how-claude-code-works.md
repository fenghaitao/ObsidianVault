---
title: "summary-how-claude-code-works"
type: source
tags: [source, claude-code, agentic-loop, transcript]
sources: [raw/03-transcripts/Claude/Claude Code 101/03 - How Claude Code Works.md]
last_updated: 2026-06-23
---

## Core Summary

Claude Code operates through an agentic loop: the user enters a prompt, Claude gathers context, the model returns text or a tool call, Claude executes the action (e.g., editing a file, running a command), then verifies results against the original goal. If the goal isn't met, the loop repeats. Throughout, the user can add context, interrupt, or steer the model. Key mechanisms include the context window (with automatic compaction), tools as the backbone of agentic behavior, semantic search for tool selection, and configurable permission modes.

## Key Points

- The agentic loop: prompt -> gather context -> model response (text or tool call) -> execute action -> verify results -> repeat if needed.
- Context window determines how much conversation, file contents, and command outputs can be stored; Claude Code compacts the conversation when the limit is reached.
- Tools are what differentiate agents from simple text-in/text-out assistants; Claude Code uses semantic searching to determine when to call a tool.
- Permission modes: default (ask before editing/running), auto-accept edits (edits without asking, still asks for commands), plan mode (read-only, compiles a plan first).
- Giving Claude Code unrestricted permissions carries risk: mistakes are harder to catch before they happen.

## Related

- [[ClaudeCode]] — the tool whose internals are described
- [[AIAgent]] — the agentic loop paradigm
- [[ContextWindow]] — the memory mechanism with compaction
- [[AgenticLoop]] — the core operational pattern
