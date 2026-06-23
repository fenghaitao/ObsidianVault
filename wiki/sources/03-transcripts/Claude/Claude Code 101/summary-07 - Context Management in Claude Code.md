---
title: "summary-context-management-in-claude-code"
type: source
tags: [source, claude-code, context-window, compaction, transcript]
sources: [raw/03-transcripts/Claude/Claude Code 101/07 - Context Management in Claude Code.md]
last_updated: 2026-06-23
---

## Core Summary

Context is Claude's working memory; every file read, command run, and message sent consumes context window space. When approaching the limit, Claude auto-compacts by summarizing important details and removing unnecessary results. Users can manually compact with `/compact` or fully reset with `/clear`. Key strategies: use CLAUDE.md for persistent memory, be specific in prompts (vague prompts force more exploration, consuming more context), disable unrelated MCP servers, and use sub-agents for tasks where only the answer matters (they run in separate context windows).

## Key Points

- Context window holds everything: file reads, command outputs, messages, tool call results.
- **Auto-compaction** triggers near the limit, summarizing important details and freeing space (may lose conversation details).
- **`/compact`**: manual compaction, preserves a summary of previous work while freeing context.
- **`/clear`**: full reset, starts from scratch with no memory of prior conversation.
- **`/context`**: displays context size breakdown by category with a visual graph.
- **Rule of thumb:** compact when continuing on the same feature but running out of context; clear when starting a new feature.
- **CLAUDE.md**: put persistent information here so Claude doesn't rediscover it each session.
- **Be specific:** vague prompts force Claude to explore more, consuming more context than a slightly longer but clearer prompt.
- **MCP servers:** all tools load into context by default; disable unrelated ones.
- **Skills:** work like MCP but don't load everything into context.
- **Sub-agents:** run in separate context windows; delegate tasks where only the answer is needed.

## Related

- [[ClaudeCode]] — the tool whose context is managed
- [[ContextWindow]] — the underlying memory constraint
- [[CLAUDE-md]] — persistent memory across sessions
- [[summary-05 - The CLAUDE.md file]] — related source on CLAUDE.md
