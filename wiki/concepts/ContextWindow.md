---
title: "ContextWindow"
type: concept
tags: [llm, context, memory, ai]
sources: [raw/03-transcripts/Claude/Claude Code 101/01 - What is Claude Code.md, raw/03-transcripts/Claude/Claude Code 101/07 - Context Management in Claude Code.md, raw/01-articles/claude/2025-08-12 - Claude Sonnet 4 now supports 1M tokens of context.md]
last_updated: 2026-06-28
---

## Definition

The context window is an LLM's working memory -- the maximum amount of text (tokens) it can hold and reason about at once. It can hold a lot, but not everything simultaneously.

## Key Information

- Acts as a constraint on what an LLM can process in a single interaction.
- AI agents work around context window limits by strategically retrieving only relevant information rather than loading everything at once.
- Effective use of Claude Code requires understanding this limitation and structuring prompts and workflows accordingly.
- [[ClaudeEnterprise]] offers a 500K context window, enabling processing of hundreds of sales transcripts, dozens of 100+ page documents, or medium-sized codebases.
- **Retrieval vs. capacity**: a large context window doesn't guarantee accurate retrieval of embedded facts. [[Claude2.1]] (200K tokens) initially showed reluctance to answer based on an "out of place" embedded sentence — see [[LongContextRetrieval]] for the evaluation and the prompting fix that raised accuracy from 27% to 98%.
- [[Claude4Sonnet]] supports a **1 million token context window** (public beta, August 2025) — a 5x increase enabling processing of entire codebases (75,000+ lines), large document sets, and context-aware agents that maintain coherence across hundreds of tool calls. Pricing scales for prompts exceeding 200K tokens; [[PromptCaching]] and [[BatchProcessing]] can offset the additional cost.

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

### Platform-Level Context Management (September 2025)

Anthropic introduced two platform-level features to address context limits in production agents:

- **[[ContextEditing]]**: Automatically removes stale tool calls and results from the context window as an agent approaches token limits. Preserves conversation flow; delivered 29% performance improvement alone and 84% token reduction in a 100-turn web search evaluation.
- **Memory Tool**: File-based CRUD storage that lives outside the context window in developer-managed infrastructure, persisting across conversations. Together with context editing, yields a 39% performance improvement over baseline on internal agentic search evaluations.
- [[Claude4.5Sonnet]] adds built-in context awareness — tracking available tokens throughout a conversation — to power these features.

## Related

- [[summary-01 - What is Claude Code]] — source summary
- [[summary-07 - Context Management in Claude Code]] — source on context management
- [[ClaudeCode]] — tool that operates within context window constraints
- [[AIAgent]] — paradigm for working around context window limits
- [[CLAUDE-md]] — persistent memory across sessions
- [[ClaudeEnterprise]] — enterprise product with 500K context window
- [[Claude4Sonnet]] — model with 1M token context window (public beta, August 2025)
- [[BatchProcessing]] — 50% additional cost savings when used with long context
- [[PromptCaching]] — reduces latency and cost for repeated long-context requests
- [[summary-2024-09-10 - Claude for Enterprise]] — announcement of enterprise context window
- [[summary-2025-08-12 - Claude Sonnet 4 now supports 1M tokens of context]] — 1M context window announcement
- [[ContextEditing]] — platform feature for automatic stale-content removal from context
- [[AgenticMemory]] — external memory mechanism to extend effective context across sessions
- [[Claude4.5Sonnet]] — model with built-in token tracking for context awareness
- [[summary-2025-09-29 - Managing context on the Claude Developer Platform]] — context editing and memory tool announcement
- [[Claude2.1]] — early 200K-token model whose retrieval behavior motivated long-context prompting research
- [[LongContextRetrieval]] — the retrieval pattern and prompting fix for long-context reluctance
