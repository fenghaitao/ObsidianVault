---
title: "summary-2025-09-29 - Building agents with the Claude Agent SDK.md"
type: source
tags: [source, original-material]
sources: ["raw/01-articles/claude/2025-09-29 - Building agents with the Claude Agent SDK.md"]
last_updated: 2026-06-28
---

## Core Summary

The Claude Agent SDK (renamed from the Claude Code SDK) is a framework for building general-purpose autonomous agents by giving Claude access to a computer — its file system, bash shell, and external integrations. The article walks through the agent loop (gather context → take action → verify work) using an email agent as a running example.

## Key Points

### Rename: Claude Code SDK → Claude Agent SDK

- [[ClaudeCode]] has become far more than a coding tool; Anthropic uses it for deep research, video creation, note-taking, and powering almost all major agent loops.
- The agent harness behind Claude Code can power many other agent types, so the **Claude Code SDK is renamed to the [[ClaudeAgentSDK]]** to reflect this broader vision.

### Core Design Principle

- Give your agent a computer (terminal + file system + tools) so it can work like a human does.
- File/folder structure serves as a form of [[ContextEngineering]]: it represents information that *could* be pulled into the model's context.

### The Agent Loop

1. **Gather context** — use file system (agentic search), or semantic search (faster but less accurate); subagents can run parallel queries.
2. **Take action** — via custom tools, bash commands, code generation, and MCP server integrations.
3. **Verify work** — rules-based feedback (e.g., linting), visual feedback (screenshots), or an LLM judge subagent.

### Context Gathering Features

- **Agentic search**: Claude uses bash (`grep`, `tail`) to selectively load relevant parts of large files. Preferred over semantic search for accuracy and transparency.
- **Semantic search** ([[RetrievalAugmentedGeneration]]): faster but less accurate, harder to maintain; add only when speed is needed.
- **Subagents**: run in isolated context windows for parallelization and context hygiene; only return relevant excerpts to the orchestrator.
- **Compact feature**: automatically summarizes previous messages when context limit approaches.

### Action Primitives

- **Custom tools** (`fetchInbox`, `searchEmails`): primary, most frequent actions; prominent in the context window so design them carefully.
- **Bash**: general-purpose tool for flexible, ad hoc computer use.
- **Code generation**: precise, composable, reusable; used internally for Excel/PowerPoint/Word document creation on Claude.ai.
- **[[MCP]] servers**: standardized integrations (Slack, GitHub, Google Drive, Asana) that handle authentication and API calls automatically.

### Verification Methods

1. **Rules-based feedback**: explicit rules + failure reasons; code linting (TypeScript preferred over plain JS for richer feedback).
2. **Visual feedback**: screenshots/renders fed back to the model for iterative refinement; Playwright MCP server for automating this loop.
3. **LLM judge**: a separate model or subagent evaluates output on fuzzy criteria; useful for tone/quality checks, but adds latency.

### Best Practices

- After iterating the loop, carefully audit agent failures and ask "does it have the right tools for the job?"
- Start with agentic search; add semantic search only if performance requires it.
- Choose TypeScript over JavaScript when generating code — linting provides additional feedback layers.

## Related

- [[ClaudeAgentSDK]] — the entity described in this article
- [[ClaudeCode]] — the product from which the SDK originates
- [[Anthropic]] — publisher of this article
- [[AIAgent]] — the broader agent paradigm
- [[AgenticLoop]] — the gather context → take action → verify work pattern
- [[ClaudeCodeSubagents]] — subagent parallelization and context isolation
- [[ContextEngineering]] — treating file/folder structure as context
- [[ToolUse]] — tool design for agents
- [[ModelContextProtocol]] — standardized external service integrations
- [[RetrievalAugmentedGeneration]] — semantic search alternative to agentic search
- [[ContextWindow]] — the memory constraint the compact feature manages
