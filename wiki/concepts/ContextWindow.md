---
title: "ContextWindow"
type: concept
tags: [llm, context, memory, ai]
sources: [raw/03-transcripts/Claude/Claude Code 101/01 - What is Claude Code.md, raw/03-transcripts/Claude/Claude Code 101/07 - Context Management in Claude Code.md]
last_updated: 2026-06-23
---

## Definition

The context window is an LLM's working memory -- the maximum amount of text (tokens) it can hold and reason about at once. It can hold a lot, but not everything simultaneously.

## Key Information

- Acts as a constraint on what an LLM can process in a single interaction.
- AI agents work around context window limits by strategically retrieving only relevant information rather than loading everything at once.
- Effective use of Claude Code requires understanding this limitation and structuring prompts and workflows accordingly.

### Context Management in Claude Code

- **Auto-compaction:** triggers near the limit, summarizes important details and removes unnecessary tool call results (may lose conversation details).
- **`/compact`:** manual compaction; preserves a summary of previous work while freeing context.
- **`/clear`:** full reset; starts from scratch with no memory of prior conversation.
- **`/context`:** displays context size breakdown by category with a visual graph.
- **Rule of thumb:** compact when continuing on the same feature but running out of context; clear when starting a new feature.
- **Be specific in prompts:** vague prompts force Claude to explore more, consuming more context than a slightly longer but clearer prompt.
- **MCP servers:** all tools load into context by default; disable unrelated ones to save space.
- **Skills:** work like MCP but don't load everything into context.
- **Sub-agents:** run in separate context windows; delegate tasks where only the answer is needed.
- **CLAUDE.md:** put persistent information here so Claude doesn't rediscover it each session.

## Related

- [[summary-01 - What is Claude Code]] — source summary
- [[summary-07 - Context Management in Claude Code]] — source on context management
- [[ClaudeCode]] — tool that operates within context window constraints
- [[AIAgent]] — paradigm for working around context window limits
- [[CLAUDE-md]] — persistent memory across sessions
