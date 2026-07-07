---
title: "Extended Thinking"
type: concept
tags: [thinking, reasoning, model-capability, inference, planning]
sources: [raw/01-articles/claude/2025-03-06 - Get to production faster with the upgraded Anthropic Console.md, "raw/01-articles/claude/2026-05-26 - Code w Claude London 2026 Rethinking how we build.md"]
last_updated: 2026-07-07
---

## Definition

Extended thinking is a capability that enables Claude models to produce step-by-step reasoning visible to the user, with the ability to control the thinking budget by setting a maximum number of thinking tokens. It contrasts with near-instant responses for simpler tasks.

## Key Information

- **Visibility**: Step-by-step thinking is visible to users (unlike internal reasoning scratchpad)
- **Token Control**: Developers can set a max number of thinking tokens to control the budget
- **Flexibility**: Users can choose between near-instant responses or extended reasoning based on task needs
- **Prompt Optimization**: Available in [[AnthropicConsole]] to optimize prompts specifically for extended thinking mode
- **Model Support**: Featured in [[Claude3.7Sonnet]], the latest and most intelligent Claude model

## Extended Thinking vs Adaptive Thinking

- **Extended Thinking**: Visible step-by-step reasoning with token budget control
- **[[AdaptiveThinking]]**: Claude's capability to choose when to think, call tools, or output text based on task requirements
- **Deprecated on newest models**: [[Claude4.7Opus|Opus 4.7]] (April 2026) does not support extended thinking with a fixed token budget at all, relying exclusively on adaptive thinking instead.

## Thinking Budgets and Effort Levels

At Code w/ Claude London 2026 (May 20–21), a breakout session covered optimizing thinking budgets and effort levels across Claude models. This reflects the practical use of extended and adaptive thinking controls to tune model behavior for different tasks — from fast, low-cost responses for simple queries to deep, multi-step reasoning for complex agentic work. See [[summary-2026-05-26 - Code w Claude London 2026 Rethinking how we build]].

## Related

- [[AdaptiveThinking]] — related thinking capability
- [[Claude3.7Sonnet]] — model supporting extended thinking
- [[AnthropicConsole]] — platform offering extended thinking optimization
- [[PromptEngineering]] — discipline enhanced by extended thinking optimization
- [[summary-2025-03-06 - Get to production faster with the upgraded Anthropic Console]] — article introducing extended thinking in console
- [[summary-2026-05-26 - Code w Claude London 2026 Rethinking how we build]] — London 2026 recap, thinking budgets session
- [[Claude4.7Opus]] — model that no longer supports fixed-budget extended thinking
- [[ClaudeCode]] — developer tool where thinking budgets are most relevant
- [[summary-15 - The thinking lever]] — source summary
