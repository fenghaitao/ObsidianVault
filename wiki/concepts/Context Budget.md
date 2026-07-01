---
title: "Context Budget"
type: concept
tags: [context-engineering, llm, performance, cost-optimization]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260420 - Full Workshop： Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi.md"]
last_updated: 2026-06-26
---

## Definition
Context Budget is the practice of managing the total token usage within an LLM's context window to maintain performance and control costs. As context grows through system prompts, tool definitions, few-shot examples, retrieved data, and conversation history, model performance degrades well before the technical context window limit due to the "lost in the middle" problem.

## Key Information
- **What consumes context**: System prompt, tool definitions and schemas, few-shot examples, retrieved data, conversation history
- **Performance degradation**: Worsens significantly after ~200K tokens, far below the 1M token technical limit of modern models
- **Lost in the middle problem**: Long-context models are trained by inserting random facts and retrieving them, which teaches retrieval of single facts but not leveraging the full context. This causes performance to degrade as context grows
- **Management techniques**: Trim content, summarize, retrieve based on criteria, compaction methods (from Claude Code leak), delegation to tools or sub-agents with their own context windows
- **Delegation as primary strategy**: When context becomes too large (e.g., over 20 tools), delegate to sub-agents or tools with isolated context windows. This is what most agent harnesses do
- **Multi-agent trigger**: Context budget overflow is a primary reason to split into multi-agent systems
- **Cost implications**: Larger context = more tokens processed = higher cost per task
- **Few-shot example optimization**: Start with more examples, trim down to the minimum that works, to keep the system prompt lean

## Related
- [[summary-20260420 - Full Workshop： Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi]] — source
- [[Lost in the Middle]] — the training artifact causing context degradation
- [[ContextEngineering]] — broader discipline of managing LLM context
- [[Context Management]] — related techniques for context optimization
- [[MultiAgentArchitecture]] — architectural response to context budget overflow
- [[FewShotExamples]] — contributor to context consumption
- [[Agent Skills]] — progressive disclosure pattern that reduces context usage
- [[ProgressiveDisclosure]] — related technique for managing context
