---
title: "ClaudeAgentSDK"
type: entity
tags: [tool, sdk, agent, anthropic, claude-code]
sources: ["raw/01-articles/claude/2025-09-29 - Building agents with the Claude Agent SDK.md"]
last_updated: 2026-06-28
---

## Definition

The Claude Agent SDK is a collection of tools that helps developers build powerful, general-purpose agents on top of [[ClaudeCode]]. It was renamed from the Claude Code SDK in September 2025 to reflect its broader applicability beyond coding tasks.

## Key Information

### Origin

- The Claude Code SDK was originally built to power Claude Code's agentic coding capabilities.
- Over time, [[Anthropic]] teams began using it for deep research, video creation, note-taking, and other non-coding agent workflows.
- The SDK was renamed to **Claude Agent SDK** to signal that the same harness can power any type of agent.

### Core Design Principle

Give Claude access to a computer — file system, bash shell, and external service integrations — so agents can work the way humans do, iterating on their output until the goal is achieved.

### The Agent Loop

The SDK is organized around three phases:

1. **Gather context** — read the file system via agentic search (bash tools like `grep`, `tail`); optionally add semantic search ([[RetrievalAugmentedGeneration]]) for faster but less accurate retrieval; use subagents for parallel queries.
2. **Take action** — custom tools (the primary execution layer), bash commands, code generation, and [[MCP]] server integrations.
3. **Verify work** — rules-based feedback (linting), visual feedback (screenshots/renders), or an LLM judge subagent.

### Context Gathering Features

- **File system as context**: folder and file structure is a form of [[ContextEngineering]] — the agent decides what to load based on the task.
- **Agentic search vs. semantic search**: agentic search (bash-based) is preferred for accuracy and transparency; [[RetrievalAugmentedGeneration|semantic search]] is faster but harder to maintain.
- **Subagents**: run in isolated [[ContextWindow|context windows]]; spin up multiple subagents in parallel to search different queries, returning only relevant excerpts to the orchestrator.
- **Compact feature**: automatically summarizes prior messages when the context limit approaches, built on Claude Code's `/compact` slash command.

### Action Primitives

- **Custom tools**: developer-defined functions (e.g., `fetchInbox`, `searchEmails`) that appear prominently in Claude's context window; design them carefully for context efficiency.
- **Bash**: general-purpose computer access for flexible ad hoc work.
- **Code generation**: precise, composable, reusable output; Claude.ai's file-creation feature (Excel, PowerPoint, Word) is built entirely on code generation.
- **MCP servers**: standardized integrations for Slack, GitHub, Google Drive, Asana, and more — handle authentication and API calls automatically.

### Verification Methods

| Method | Best for | Tradeoff |
|---|---|---|
| Rules-based (linting) | Structured output with clear correctness criteria | Requires explicit rule definitions |
| Visual feedback (screenshots) | UI generation, HTML email, visual tasks | Requires a render step (e.g., Playwright MCP) |
| LLM judge (subagent) | Fuzzy quality criteria (tone, style) | Latency cost; less reliable |

### Best Practices

- Start with agentic search; add semantic search only when speed is necessary.
- Prefer TypeScript over JavaScript for code generation — linting provides additional feedback layers.
- Design tools around primary, frequent actions; use bash for edge cases.
- After building, audit failures carefully and ask: "does the agent have the right tools for this job?"

## Related

- [[summary-2025-09-29 - Building agents with the Claude Agent SDK]] — source article
- [[ClaudeCode]] — the product the SDK underpins
- [[Anthropic]] — creator and publisher
- [[AgenticLoop]] — the gather context → take action → verify work pattern
- [[ClaudeCodeSubagents]] — subagent system for parallelization and context isolation
- [[ContextEngineering]] — treating file/folder structure as agent context
- [[ToolUse]] — tool design for agents
- [[ModelContextProtocol]] — standardized external integrations
- [[RetrievalAugmentedGeneration]] — semantic search compared to agentic search
- [[ContextWindow]] — the memory constraint the compact feature manages
- [[AIAgent]] — the broader agent paradigm
