---
title: "LongSessionEvals"
type: concept
tags: [evals, context-management, agents, testing, long-sessions]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260510 - How we solved Context Management in Agents — Sally-Ann Delucia.md"]
last_updated: 2026-06-29
---

## Definition
Long session evals are a testing technique that measures context degradation over extended agent conversations by loading N turns of history and testing the (N+1)th turn. They make late-session failures testable rather than waiting for user reports.

## Key Information
- Developed by Arize for their AI agent Alex after discovering that smart truncation worked initially but failed late in long conversations.
- Users tend to stay in one chat rather than restarting, causing conversations to grow and failures to appear late — often unnoticed until user reports.
- Technique: load 10 turns of conversation history, then test the 11th turn to evaluate how context quality holds up.
- Makes context degradation bugs testable and measurable rather than relying on user reports or manual inspection.
- Provides a signal for how well context management strategies (like smart truncation) are performing over time.
- Related to broader context quality metrics, which Arize is still developing.

## Related
- [[summary-20260510 - How we solved Context Management in Agents — Sally-Ann Delucia]] — source
- [[ContextManagement]] — parent discipline
- [[SmartTruncation]] — context strategy being evaluated
- [[Evals]] — broader evaluation practice
- [[ContextQuality]] — what long session evals measure
- [[AgentMemory]] — long-term memory solutions that could reduce the need for long sessions
