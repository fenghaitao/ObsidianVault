---
title: "Hooks"
type: concept
tags: [agents, verification, events, claude-agent-sdk]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260109 - Spec-Driven Development： Agentic Coding at FAANG Scale and Quality — Al Harris, Amazon Kiro.md"]
last_updated: 2026-06-26
---

## Definition
Hooks are event-driven extension points in the Claude Agent SDK that fire at specific moments in the agent loop. They enable deterministic verification and context insertion without modifying the core agent logic.

## Key Information
- Ship with the Agent SDK; developers register handlers for hook events
- Primary use case: deterministic verification — check spreadsheet integrity after each tool call, verify outputs match constraints
- Secondary use case: context insertion — inject changes the user has made to a spreadsheet while the agent was working, providing live context updates
- Can enforce rules like "don't return a response without writing a script" or "make sure you read a file before writing to it"
- Example from Claude Code: if the agent tries to write to a file it hasn't read yet (not in the read cache), a hook throws an error telling it to read first
- Hooks are one of the ways to add determinism to agent behavior, complementing the model's own reasoning
- Guide available in the Agent SDK documentation
- **Amazon Kiro also supports hooks**: Kiro has software hooks as a feature alongside steering and MCP. Used to ensure test cases pass before a task is marked complete, addressing the common LLM problem of claiming completion when tests don't pass.

## Related
- [[summary-20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic]] — source
- [[AgentLoop]] — where hooks fire
- [[Verification in Agentic Loops]] — primary use case
- [[ClaudeAgentSDK]] — the framework
- [[summary-20260109 - Spec-Driven Development： Agentic Coding at FAANG Scale and Quality — Al Harris, Amazon Kiro]] — source
- [[AgentHooks]] — Kiro's implementation of hooks
- [[AmazonKiro]] — IDE with hooks feature
